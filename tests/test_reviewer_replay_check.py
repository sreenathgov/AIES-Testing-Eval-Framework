from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path


def load_reviewer_script(repo_root: Path):
    script_path = repo_root / "scripts" / "reviewer_replay_check.py"
    spec = importlib.util.spec_from_file_location("reviewer_replay_check", script_path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_expected_constants_match_current_integrated_packet(repo_root: Path) -> None:
    module = load_reviewer_script(repo_root)
    packet = module.read_json(repo_root / "runs" / module.INTEGRATED_RUN_ID / "reports" / "integrated_results_packet.json")
    aggregates = module.read_json(repo_root / "runs" / module.INTEGRATED_RUN_ID / "reports" / "integrated_detection_aggregates.json")

    assert packet["artifact_count"] == module.EXPECTED_ARTIFACT_COUNT
    assert packet["cohort_counts"] == module.EXPECTED_COHORT_COUNTS
    assert packet["gate_distribution"] == module.EXPECTED_GATE_DISTRIBUTION
    for key, value in module.EXPECTED_DETECTION.items():
        assert aggregates[key] == value


def test_reviewer_check_non_mutating_path_passes_with_tests_skipped(repo_root: Path) -> None:
    completed = subprocess.run(
        [
            sys.executable,
            "scripts/reviewer_replay_check.py",
            "--repo-root",
            str(repo_root),
            "--skip-tests",
        ],
        cwd=repo_root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )

    assert completed.returncode == 0, completed.stdout + completed.stderr
    assert "Reviewer replay check passed." in completed.stdout
    assert "[SKIP] pytest" in completed.stdout


def test_missing_expected_run_path_reports_failure(repo_root: Path, tmp_path: Path) -> None:
    module = load_reviewer_script(repo_root)
    results = module.verify_required_runs(tmp_path, [module.POSITIVE_RUN_ID])

    assert len(results) == 1
    assert results[0].ok is False
    assert "Missing" in results[0].detail


def test_skip_tests_avoids_pytest_invocation(repo_root: Path, monkeypatch) -> None:
    module = load_reviewer_script(repo_root)

    def fail_if_called(*_args, **_kwargs):
        raise AssertionError("pytest command should not run when --skip-tests is used")

    monkeypatch.setattr(module, "run_command", fail_if_called)
    results = module.run_test_phase(repo_root, skip_tests=True)

    assert len(results) == 1
    assert results[0].skipped is True
