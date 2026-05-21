from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


MIN_PYTHON = (3, 11)

POSITIVE_RUN_ID = "paper_eval_20260520"
NEGATIVE_RUN_ID = "paper_negative_20260520"
INTEGRATED_RUN_ID = "paper_integrated_20260520"
REVIEWER_NEGATIVE_RUN_ID = "reviewer_negative_replay"
REVIEWER_INTEGRATED_RUN_ID = "reviewer_integrated_replay"

EXPECTED_ARTIFACT_COUNT = 40
EXPECTED_COHORT_COUNTS = {"baseline": 28, "fault_injection": 12}
EXPECTED_GATE_DISTRIBUTION = {
    "blocked_pending_rerun": 2,
    "blocked_pending_research": 8,
    "pass": 22,
    "pass_with_notes": 8,
}
EXPECTED_DETECTION = {
    "gate_accuracy": 1.0,
    "micro_recall": 1.0,
    "false_negative_total": 0,
}


@dataclass(frozen=True)
class CheckResult:
    name: str
    ok: bool
    detail: str
    skipped: bool = False


def pass_(name: str, detail: str) -> CheckResult:
    return CheckResult(name=name, ok=True, detail=detail)


def fail(name: str, detail: str) -> CheckResult:
    return CheckResult(name=name, ok=False, detail=detail)


def skip(name: str, detail: str) -> CheckResult:
    return CheckResult(name=name, ok=True, detail=detail, skipped=True)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def env_for_repo(repo_root: Path) -> dict[str, str]:
    env = os.environ.copy()
    src_path = str(repo_root / "src")
    current = env.get("PYTHONPATH")
    env["PYTHONPATH"] = src_path if not current else src_path + os.pathsep + current
    return env


def configure_import_path(repo_root: Path) -> None:
    src_path = str(repo_root / "src")
    if src_path not in sys.path:
        sys.path.insert(0, src_path)


def run_command(repo_root: Path, command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=repo_root,
        env=env_for_repo(repo_root),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def verify_python_version() -> CheckResult:
    version = sys.version_info[:3]
    if version < MIN_PYTHON:
        return fail("python_version", f"Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]}+ required; found {version[0]}.{version[1]}.{version[2]}")
    return pass_("python_version", f"Python {version[0]}.{version[1]}.{version[2]}")


def verify_imports(repo_root: Path) -> CheckResult:
    configure_import_path(repo_root)
    try:
        import legal_extract_eval  # noqa: F401
    except Exception as exc:  # pragma: no cover - message matters more than branch shape
        return fail("package_import", f"Could not import legal_extract_eval: {exc}")
    return pass_("package_import", "legal_extract_eval import succeeded")


def verify_required_runs(repo_root: Path, run_ids: list[str]) -> list[CheckResult]:
    results: list[CheckResult] = []
    for run_id in run_ids:
        run_root = repo_root / "runs" / run_id
        manifest = run_root / "RUN_MANIFEST.json"
        if run_root.is_dir() and manifest.is_file():
            results.append(pass_(f"run_exists:{run_id}", f"{run_root}"))
        else:
            results.append(fail(f"run_exists:{run_id}", f"Missing {run_root} or RUN_MANIFEST.json"))
    return results


def verify_readiness(repo_root: Path) -> CheckResult:
    completed = run_command(
        repo_root,
        [sys.executable, "-m", "legal_extract_eval.readiness", "--repo-root", str(repo_root), "--json"],
    )
    if completed.returncode != 0:
        return fail("readiness", (completed.stderr or completed.stdout).strip())
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        return fail("readiness", f"Readiness did not emit JSON: {exc}")
    if payload.get("status") != "ready" or payload.get("blocker_count") != 0:
        return fail("readiness", json.dumps(payload, sort_keys=True))
    return pass_("readiness", "status=ready blocker_count=0")


def regenerate_reviewer_runs(repo_root: Path) -> list[CheckResult]:
    commands = [
        [
            sys.executable,
            "-m",
            "legal_extract_eval.negative_run",
            "--repo-root",
            str(repo_root),
            "--run-id",
            REVIEWER_NEGATIVE_RUN_ID,
            "--base-run",
            POSITIVE_RUN_ID,
            "--force",
        ],
        [
            sys.executable,
            "-m",
            "legal_extract_eval.integrated_run",
            "--repo-root",
            str(repo_root),
            "--run-id",
            REVIEWER_INTEGRATED_RUN_ID,
            "--positive-run",
            POSITIVE_RUN_ID,
            "--negative-run",
            REVIEWER_NEGATIVE_RUN_ID,
            "--force",
        ],
    ]
    results: list[CheckResult] = []
    for command in commands:
        completed = run_command(repo_root, command)
        module_name = command[command.index("-m") + 1]
        run_id = command[command.index("--run-id") + 1]
        label = f"{module_name}:{run_id}"
        if completed.returncode == 0:
            results.append(pass_(f"regenerate:{label}", completed.stdout.strip()))
        else:
            results.append(fail(f"regenerate:{label}", (completed.stderr or completed.stdout).strip()))
    return results


def verify_integrated_results(repo_root: Path, run_id: str) -> list[CheckResult]:
    report_dir = repo_root / "runs" / run_id / "reports"
    packet_path = report_dir / "integrated_results_packet.json"
    control_path = report_dir / "control_profile.json"
    aggregates_path = report_dir / "integrated_detection_aggregates.json"
    if not packet_path.exists():
        return [fail("integrated_packet", f"Missing {packet_path}")]

    packet = read_json(packet_path)
    controls = read_json(control_path)
    aggregates = read_json(aggregates_path)
    results = [
        compare("artifact_count", packet.get("artifact_count"), EXPECTED_ARTIFACT_COUNT),
        compare("cohort_counts", packet.get("cohort_counts"), EXPECTED_COHORT_COUNTS),
        compare("gate_distribution", packet.get("gate_distribution"), EXPECTED_GATE_DISTRIBUTION),
        compare("control_row_count", len(controls), EXPECTED_ARTIFACT_COUNT),
    ]
    for key, expected in EXPECTED_DETECTION.items():
        results.append(compare(f"detection:{key}", aggregates.get(key), expected))
    return results


def compare(name: str, observed: Any, expected: Any) -> CheckResult:
    if observed == expected:
        return pass_(name, f"{observed}")
    return fail(name, f"expected {expected!r}, observed {observed!r}")


def run_test_phase(repo_root: Path, *, skip_tests: bool) -> list[CheckResult]:
    if skip_tests:
        return [skip("pytest", "skipped by --skip-tests")]

    phases = [
        ("public_release_guardrail", [sys.executable, "-m", "pytest", "-q", "tests/test_public_release_guardrails.py"]),
        ("pytest", [sys.executable, "-m", "pytest", "-q"]),
    ]
    results: list[CheckResult] = []
    for name, command in phases:
        completed = run_command(repo_root, command)
        if completed.returncode == 0:
            summary = (completed.stdout.strip().splitlines() or ["passed"])[-1]
            results.append(pass_(name, summary))
        else:
            output = "\n".join(part for part in (completed.stdout, completed.stderr) if part).strip()
            results.append(fail(name, output[-2000:]))
    return results


def run_review_check(repo_root: Path, *, regenerate: bool, skip_tests: bool) -> list[CheckResult]:
    repo_root = repo_root.resolve()
    results: list[CheckResult] = [verify_python_version(), verify_imports(repo_root)]

    if regenerate:
        results.extend(verify_required_runs(repo_root, [POSITIVE_RUN_ID]))
    else:
        results.extend(verify_required_runs(repo_root, [POSITIVE_RUN_ID, NEGATIVE_RUN_ID, INTEGRATED_RUN_ID]))

    results.append(verify_readiness(repo_root))

    if regenerate and all(result.ok for result in results):
        results.extend(regenerate_reviewer_runs(repo_root))
        target_run = REVIEWER_INTEGRATED_RUN_ID
    else:
        target_run = INTEGRATED_RUN_ID

    if all(result.ok for result in results):
        results.extend(verify_integrated_results(repo_root, target_run))

    if all(result.ok for result in results):
        results.extend(run_test_phase(repo_root, skip_tests=skip_tests))
    return results


def print_results(results: list[CheckResult]) -> None:
    for result in results:
        prefix = "SKIP" if result.skipped else ("PASS" if result.ok else "FAIL")
        print(f"[{prefix}] {result.name}: {result.detail}")
    failed = [result for result in results if not result.ok]
    print("")
    if failed:
        print(f"Reviewer replay check failed: {len(failed)} failing check(s).")
    else:
        print("Reviewer replay check passed.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Verify or regenerate the reviewer-facing HS evaluation replay.")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--regenerate", action="store_true", help="Create reviewer-local negative/integrated replay runs before verification.")
    parser.add_argument("--skip-tests", action="store_true", help="Skip pytest phases; useful for fast smoke checks and unit tests.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    results = run_review_check(args.repo_root, regenerate=args.regenerate, skip_tests=args.skip_tests)
    print_results(results)
    return 0 if all(result.ok for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
