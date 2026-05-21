from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
from collections import Counter, defaultdict
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from .metric_calculator import calculate_metric_summary, write_metric_reports
from .negative_run import DETECTION_MATRIX_COLUMNS, load_negative_registry
from .pre_hs_slice import RUN_REPORT_COLUMNS, stress_test_catalog
from .validator_driven_run import build_detection_matrix, detection_aggregates, evaluate_mixed_run


INTEGRATED_CONTROL_COLUMNS = ("cohort", "negative_case_id") + RUN_REPORT_COLUMNS
INTEGRATED_GATE_COLUMNS = (
    "cohort",
    "negative_case_id",
    "scenario_id",
    "artifact_id",
    "component_id",
    "actual_route",
    "severity",
    "gate_id",
    "gate_label",
    "gate_reason_codes",
)
COHORT_METRIC_COLUMNS = (
    "metric_id",
    "baseline_score",
    "baseline_status",
    "baseline_numerator",
    "baseline_denominator",
    "fault_injection_score",
    "fault_injection_status",
    "fault_injection_numerator",
    "fault_injection_denominator",
    "integrated_score",
    "integrated_status",
    "integrated_numerator",
    "integrated_denominator",
)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat()


def create_integrated_run(
    repo_root: Path,
    run_id: str,
    *,
    positive_run: str = "paper_eval_20260520",
    negative_run: str = "paper_negative_20260520",
    overwrite: bool = False,
) -> list[dict[str, Any]]:
    run_root = repo_root / "runs" / run_id
    positive_root = repo_root / "runs" / positive_run
    negative_root = repo_root / "runs" / negative_run
    if not positive_root.exists():
        raise FileNotFoundError(f"Positive run not found: {positive_root}")
    if not negative_root.exists():
        raise FileNotFoundError(f"Negative run not found: {negative_root}")
    if run_root.exists():
        if not overwrite:
            raise FileExistsError(f"Run already exists: {run_root}")
        shutil.rmtree(run_root)

    copy_artifacts(positive_root, negative_root, run_root)
    merge_traces(positive_root, negative_root, run_root, run_id)
    rows = evaluate_mixed_run(repo_root, run_id)
    write_integrated_control_reports(run_root, rows)
    write_integrated_gate_reports(run_root, rows)
    metric_rows = calculate_metric_summary(repo_root, run_id)
    write_metric_reports(repo_root, run_id, metric_rows)
    cohort_metric_rows = write_cohort_metric_comparison(repo_root, run_id, positive_run, negative_run, metric_rows)
    cohort_gate_rows = write_cohort_gate_distribution(run_root, rows)
    detection_rows = write_integrated_detection_matrix(repo_root, run_id, negative_run, rows)
    write_integrated_results_packet(
        repo_root,
        run_id,
        positive_run,
        negative_run,
        rows,
        metric_rows,
        cohort_metric_rows,
        cohort_gate_rows,
        detection_rows,
    )
    write_run_manifest(repo_root, run_id, positive_run, negative_run, rows)
    return rows


def copy_artifacts(positive_root: Path, negative_root: Path, run_root: Path) -> None:
    for dirname in ("pta", "pra", "aa", "audit", "handoff", "inputs", "bundles"):
        for source_root in (positive_root, negative_root):
            source_dir = source_root / dirname
            if not source_dir.exists():
                continue
            target_dir = run_root / dirname
            target_dir.mkdir(parents=True, exist_ok=True)
            for source_file in source_dir.rglob("*"):
                if not source_file.is_file():
                    continue
                rel = source_file.relative_to(source_dir)
                target_file = target_dir / rel
                if target_file.exists():
                    target_file = target_dir / source_root.name / rel
                target_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source_file, target_file)

    merge_graph_artifacts(positive_root, negative_root, run_root)


def merge_graph_artifacts(positive_root: Path, negative_root: Path, run_root: Path) -> None:
    node_by_id: dict[str, dict[str, Any]] = {}
    for source_root in (positive_root, negative_root):
        for entity_path in sorted((source_root / "graph" / "entities").glob("*.json")):
            entity = read_json(entity_path)
            node_id = entity.get("node_id")
            if node_id and node_id not in node_by_id:
                node_by_id[node_id] = entity | {"cohort_origin": "baseline" if source_root == positive_root else "fault_injection"}

    entity_dir = run_root / "graph" / "entities"
    relationship_dir = run_root / "graph" / "relationships"
    entity_dir.mkdir(parents=True, exist_ok=True)
    relationship_dir.mkdir(parents=True, exist_ok=True)
    for node_id, entity in sorted(node_by_id.items()):
        write_json(entity_dir / f"{safe_filename(node_id)}.json", entity)

    seen_edge_ids: set[str] = set()
    for source_root in (positive_root, negative_root):
        cohort = "baseline" if source_root == positive_root else "fault_injection"
        for edge_path in sorted((source_root / "graph" / "relationships").glob("*.json")):
            edge = read_json(edge_path)
            edge_id = edge.get("edge_id") or edge_path.stem
            if edge_id in seen_edge_ids:
                edge_id = f"{cohort}:{edge_id}"
                edge["edge_id"] = edge_id
            seen_edge_ids.add(edge_id)
            write_json(relationship_dir / f"{safe_filename(edge_id)}.json", edge | {"cohort_origin": cohort})


def merge_traces(positive_root: Path, negative_root: Path, run_root: Path, run_id: str) -> None:
    trace_dir = run_root / "trace"
    trace_dir.mkdir(parents=True, exist_ok=True)

    positive_trace = positive_root / "trace"
    negative_trace = negative_root / "trace"
    write_json(
        trace_dir / "agent_trace.json",
        {"run_id": run_id, "events": with_cohort(read_json(positive_trace / "agent_trace.json")["events"], "baseline") + with_cohort(read_json(negative_trace / "agent_trace.json")["events"], "fault_injection")},
    )
    write_json(
        trace_dir / "claim_trace.json",
        {"run_id": run_id, "claims": with_cohort(read_json(positive_trace / "claim_trace.json")["claims"], "baseline") + with_cohort(read_json(negative_trace / "claim_trace.json")["claims"], "fault_injection")},
    )
    positive_rules = read_json(positive_trace / "rule_invocation_graph.json")
    negative_rules = read_json(negative_trace / "rule_invocation_graph.json")
    write_json(
        trace_dir / "rule_invocation_graph.json",
        {
            "run_id": run_id,
            "required_rule_items": with_cohort(positive_rules["required_rule_items"], "baseline") + with_cohort(negative_rules["required_rule_items"], "fault_injection"),
            "inference_edges": with_cohort(positive_rules["inference_edges"], "baseline") + with_cohort(negative_rules["inference_edges"], "fault_injection"),
        },
    )
    for filename, key in (
        ("gating_decisions.json", "decisions"),
        ("uncertainty_signals.json", "signals"),
        ("field_completeness_trace.json", "checks"),
        ("graph_alignment_trace.json", "items"),
        ("abstention_trace.json", "cases"),
    ):
        write_json(
            trace_dir / filename,
            {
                "run_id": run_id,
                key: with_cohort(read_json(positive_trace / filename)[key], "baseline")
                + with_cohort(read_json(negative_trace / filename)[key], "fault_injection"),
            },
        )

    positive_metric_inputs = read_json(positive_trace / "metric_inputs.json")
    negative_metric_inputs = read_json(negative_trace / "metric_inputs.json")
    write_json(
        trace_dir / "metric_inputs.json",
        {
            "run_id": run_id,
            "decisions": with_cohort(positive_metric_inputs["decisions"], "baseline") + with_cohort(negative_metric_inputs["decisions"], "fault_injection"),
            "stress_tests": stress_test_catalog(),
        },
    )
    positive_burden = read_json(positive_trace / "research_burden_trace.json")
    negative_burden = read_json(negative_trace / "research_burden_trace.json")
    tickets = with_cohort(positive_burden["tickets"], "baseline") + with_cohort(negative_burden["tickets"], "fault_injection")
    write_json(
        trace_dir / "research_burden_trace.json",
        {
            "run_id": run_id,
            "tickets": tickets,
            "summary": {
                "total_artifacts": len(tickets),
                "review_or_block_tickets": sum(1 for item in tickets if item["ticket_required"]),
            },
        },
    )
    positive_delta = read_json(positive_trace / "rerun_delta_trace.json")
    negative_delta = read_json(negative_trace / "rerun_delta_trace.json")
    delta_items = with_cohort(positive_delta.get("items", []), "baseline") + with_cohort(negative_delta.get("items", []), "fault_injection")
    comparable = positive_delta["summary"].get("comparable_outputs", 0) + negative_delta["summary"].get("comparable_outputs", 0)
    changed = positive_delta["summary"].get("changed_outputs", 0) + negative_delta["summary"].get("changed_outputs", 0)
    write_json(
        trace_dir / "rerun_delta_trace.json",
        {
            "run_id": run_id,
            "comparison_enabled": comparable > 0,
            "items": delta_items,
            "summary": {
                "comparison_enabled": comparable > 0,
                "comparable_outputs": comparable,
                "changed_outputs": changed,
                "source": "integrated baseline plus controlled negative rerun delta probe",
            },
        },
    )


def with_cohort(items: list[dict[str, Any]], cohort: str) -> list[dict[str, Any]]:
    return [item | {"cohort": cohort} for item in items]


def merge_control_rows(positive_root: Path, negative_root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in read_json(positive_root / "reports" / "control_profile.json"):
        rows.append({"cohort": "baseline", "negative_case_id": None} | row)
    for row in read_json(negative_root / "reports" / "control_profile.json"):
        case_id = row["artifact_id"].removeprefix("NEG_AA_")
        rows.append({"cohort": "fault_injection", "negative_case_id": case_id} | row)
    return rows


def write_integrated_control_reports(run_root: Path, rows: list[dict[str, Any]]) -> None:
    report_dir = run_root / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    write_json(report_dir / "control_profile.json", rows)
    write_csv(report_dir / "control_profile.csv", rows, INTEGRATED_CONTROL_COLUMNS)
    write_markdown_table(
        report_dir / "control_profile.md",
        f"# Integrated {len(rows)}-Artifact Control Profile",
        rows,
        INTEGRATED_CONTROL_COLUMNS,
        f"Integrated artifacts evaluated: {len(rows)}",
    )


def write_integrated_gate_reports(run_root: Path, rows: list[dict[str, Any]]) -> None:
    report_dir = run_root / "reports"
    gate_rows = [
        {
            "cohort": row["cohort"],
            "negative_case_id": row["negative_case_id"],
            "scenario_id": row["scenario_id"],
            "artifact_id": row["artifact_id"],
            "component_id": row["component_id"],
            "actual_route": row["actual_route"],
            "severity": row["severity"],
            "gate_id": row["gate_id"],
            "gate_label": row["gate_label"],
            "gate_reason_codes": row["gate_reason_codes"],
        }
        for row in rows
    ]
    write_json(report_dir / "gate_summary.json", gate_rows)
    write_csv(report_dir / "gate_summary.csv", gate_rows, INTEGRATED_GATE_COLUMNS)
    write_markdown_table(
        report_dir / "gate_summary.md",
        "# Integrated Four-Gate Handoff Summary",
        gate_rows,
        INTEGRATED_GATE_COLUMNS,
        f"Integrated gates evaluated: {len(gate_rows)}",
    )


def write_cohort_metric_comparison(
    repo_root: Path,
    run_id: str,
    positive_run: str,
    negative_run: str,
    integrated_metric_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    report_dir = repo_root / "runs" / run_id / "reports"
    baseline = {row["metric_id"]: row for row in read_json(repo_root / "runs" / positive_run / "reports" / "metric_summary.json")}
    fault = {row["metric_id"]: row for row in read_json(repo_root / "runs" / negative_run / "reports" / "metric_summary.json")}
    integrated = {row["metric_id"]: row for row in integrated_metric_rows}
    rows: list[dict[str, Any]] = []
    for metric_id in integrated:
        rows.append(
            {
                "metric_id": metric_id,
                "baseline_score": baseline[metric_id]["score"],
                "baseline_status": baseline[metric_id]["status"],
                "baseline_numerator": baseline[metric_id]["numerator"],
                "baseline_denominator": baseline[metric_id]["denominator"],
                "fault_injection_score": fault[metric_id]["score"],
                "fault_injection_status": fault[metric_id]["status"],
                "fault_injection_numerator": fault[metric_id]["numerator"],
                "fault_injection_denominator": fault[metric_id]["denominator"],
                "integrated_score": integrated[metric_id]["score"],
                "integrated_status": integrated[metric_id]["status"],
                "integrated_numerator": integrated[metric_id]["numerator"],
                "integrated_denominator": integrated[metric_id]["denominator"],
            }
        )
    write_json(report_dir / "cohort_metric_comparison.json", rows)
    write_csv(report_dir / "cohort_metric_comparison.csv", rows, COHORT_METRIC_COLUMNS)
    write_markdown_table(report_dir / "cohort_metric_comparison.md", "# Cohort Metric Comparison", rows, COHORT_METRIC_COLUMNS)
    return rows


def write_cohort_gate_distribution(run_root: Path, rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    report_dir = run_root / "reports"
    counts: dict[tuple[str, str], int] = Counter((row["cohort"], row["gate_label"]) for row in rows)
    cohort_totals = Counter(row["cohort"] for row in rows)
    total = len(rows)
    output_rows: list[dict[str, Any]] = []
    for cohort in ("baseline", "fault_injection", "integrated"):
        labels = sorted({row["gate_label"] for row in rows})
        for label in labels:
            count = sum(1 for row in rows if (cohort == "integrated" or row["cohort"] == cohort) and row["gate_label"] == label)
            denominator = total if cohort == "integrated" else cohort_totals[cohort]
            output_rows.append(
                {
                    "cohort": cohort,
                    "gate_label": label,
                    "count": count,
                    "share": round(count / denominator, 4) if denominator else 0,
                }
            )
    columns = ("cohort", "gate_label", "count", "share")
    write_json(report_dir / "cohort_gate_distribution.json", output_rows)
    write_csv(report_dir / "cohort_gate_distribution.csv", output_rows, columns)
    write_markdown_table(report_dir / "cohort_gate_distribution.md", "# Cohort Gate Distribution", output_rows, columns)
    return output_rows


def write_integrated_detection_matrix(repo_root: Path, run_id: str, negative_run: str, rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    report_dir = repo_root / "runs" / run_id / "reports"
    registry = load_negative_registry(repo_root)
    fault_rows = [row for row in rows if row["cohort"] == "fault_injection"]
    output_rows = build_detection_matrix(fault_rows, registry["cases"])
    for row in output_rows:
        row["negative_test_passed"] = row["gate_match"] and not row["false_negative_checks"]
    aggregates = detection_aggregates(output_rows)
    columns = DETECTION_MATRIX_COLUMNS + ("negative_test_passed",)
    write_json(report_dir / "integrated_detection_matrix.json", output_rows)
    write_json(report_dir / "integrated_detection_aggregates.json", aggregates)
    write_csv(report_dir / "integrated_detection_matrix.csv", output_rows, columns)
    write_markdown_table(report_dir / "integrated_detection_matrix.md", "# Integrated Detection Matrix", output_rows, columns)
    return output_rows


def write_integrated_results_packet(
    repo_root: Path,
    run_id: str,
    positive_run: str,
    negative_run: str,
    rows: list[dict[str, Any]],
    metric_rows: list[dict[str, Any]],
    cohort_metric_rows: list[dict[str, Any]],
    cohort_gate_rows: list[dict[str, Any]],
    detection_rows: list[dict[str, Any]],
) -> None:
    report_dir = repo_root / "runs" / run_id / "reports"
    gate_counts = Counter(row["gate_label"] for row in rows)
    cohort_counts = Counter(row["cohort"] for row in rows)
    detection_agg = detection_aggregates(detection_rows)
    packet = {
        "run_id": run_id,
        "positive_run": positive_run,
        "negative_run": negative_run,
        "generated_at": now(),
        "artifact_count": len(rows),
        "cohort_counts": dict(sorted(cohort_counts.items())),
        "gate_distribution": dict(sorted(gate_counts.items())),
        "metric_summary": metric_rows,
        "cohort_metric_comparison": cohort_metric_rows,
        "cohort_gate_distribution": cohort_gate_rows,
        "integrated_detection_matrix": detection_rows,
        "integrated_detection_aggregates": detection_agg,
        "interpretation_boundary": (
            f"Primary {len(rows)}-artifact deterministic evaluation with cohort stratification. "
            "Aggregate metrics are diagnostic and do not prove legal correctness."
        ),
        "paper_claim": (
            "In a single integrated validator-driven run, the protocol admitted stable baseline artifacts "
            "and compared controlled fault-injection detections against a registry oracle."
        ),
    }
    write_json(report_dir / "integrated_results_packet.json", packet)

    lines = [
        f"# Integrated {len(rows)}-Artifact Evaluation Results Packet",
        "",
        f"- Run ID: `{run_id}`",
        f"- Positive run: `{positive_run}`",
        f"- Negative run: `{negative_run}`",
        f"- Generated at: {packet['generated_at']}",
        "",
        "## Interpretation Boundary",
        "",
        packet["interpretation_boundary"],
        "",
        "## Table 1. Integrated Run Summary",
        "",
        "| Check | Result |",
        "| --- | --- |",
        f"| Total artifacts | {len(rows)} |",
        f"| Baseline artifacts | {cohort_counts['baseline']} |",
        f"| Fault-injection artifacts | {cohort_counts['fault_injection']} |",
        "",
        "## Table 2. Integrated Gate Distribution",
        "",
        "| Gate Label | Count |",
        "| --- | --- |",
    ]
    for label, count in sorted(gate_counts.items()):
        lines.append(f"| {label} | {count} |")
    lines.extend(
        [
            "",
            "## Table 3. Cohort Gate Distribution",
            "",
            "| Cohort | Gate Label | Count | Share |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in cohort_gate_rows:
        if row["count"]:
            lines.append(f"| {row['cohort']} | {row['gate_label']} | {row['count']} | {row['share']} |")
    lines.extend(
        [
            "",
            "## Table 4. Integrated Metric Summary",
            "",
            "| Metric ID | Numerator | Denominator | Score | Status |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in metric_rows:
        lines.append(f"| {row['metric_id']} | {row['numerator']} | {row['denominator']} | {row['score']} | {row['status']} |")
    lines.extend(
        [
            "",
            "## Table 5. Fault-Injection Detection Matrix",
            "",
            "| Case | Observed Gate | Precision | Recall | F1 | Gate Match |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in detection_rows:
        lines.append(
            f"| {row['negative_case_id']} | {row['observed_gate_label']} | {row['precision']} | {row['recall']} | {row['f1']} | {row['gate_match']} |"
        )
    lines.extend(
        [
            "",
            "## Detection Aggregates",
            "",
            f"- Gate accuracy: {detection_agg['gate_accuracy']}",
            f"- Micro precision: {detection_agg['micro_precision']}",
            f"- Micro recall: {detection_agg['micro_recall']}",
            f"- Micro F1: {detection_agg['micro_f1']}",
            f"- Macro precision: {detection_agg['macro_precision']}",
            f"- Macro recall: {detection_agg['macro_recall']}",
            f"- Macro F1: {detection_agg['macro_f1']}",
            "",
            "## Paper Claim",
            "",
            packet["paper_claim"],
            "",
            "Do not interpret aggregate metric scores alone as proof of legal correctness. The defensible result is the cohort-stratified gate and detection behavior.",
        ]
    )
    (report_dir / "integrated_results_packet.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_run_manifest(repo_root: Path, run_id: str, positive_run: str, negative_run: str, rows: list[dict[str, Any]]) -> None:
    run_root = repo_root / "runs" / run_id
    cohort_counts = Counter(row["cohort"] for row in rows)
    gate_counts = Counter(row["gate_label"] for row in rows)
    write_json(
        run_root / "RUN_MANIFEST.json",
        {
            "run_id": run_id,
            "run_type": f"integrated_{len(rows)}_artifact_evaluation",
            "created_at": now(),
            "positive_run_id": positive_run,
            "negative_run_id": negative_run,
            "total_artifact_count": len(rows),
            "cohort_counts": dict(sorted(cohort_counts.items())),
            "gate_distribution": dict(sorted(gate_counts.items())),
            "command": (
                f"PYTHONPATH=src python3 -m legal_extract_eval.integrated_run --repo-root . "
                f"--run-id {run_id} --positive-run {positive_run} --negative-run {negative_run}"
            ),
            "source_mutation": "Original legal source files were not mutated; this run merges deterministic positive and controlled fault-injection artifacts.",
            "runtime_input_paths": [
                f"runs/{positive_run}",
                f"runs/{negative_run}",
            ],
            "artifact_counts": {
                "control_rows": len(rows),
                "baseline_control_rows": cohort_counts["baseline"],
                "fault_injection_control_rows": cohort_counts["fault_injection"],
                "graph_entities": len(list((run_root / "graph" / "entities").glob("*.json"))),
                "graph_relationships": len(list((run_root / "graph" / "relationships").glob("*.json"))),
                "metric_rows": len(read_json(run_root / "reports" / "metric_summary.json")),
            },
        },
    )


def write_csv(path: Path, rows: list[dict[str, Any]], columns: tuple[str, ...]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            encoded = dict(row)
            for key, value in list(encoded.items()):
                if isinstance(value, list):
                    encoded[key] = ";".join(str(item) for item in value)
                elif isinstance(value, dict):
                    encoded[key] = json.dumps(value, sort_keys=True)
            writer.writerow({column: encoded.get(column, "") for column in columns})


def write_markdown_table(path: Path, title: str, rows: list[dict[str, Any]], columns: tuple[str, ...], footer: str | None = None) -> None:
    lines = [title, "", "| " + " | ".join(columns) + " |", "| " + " | ".join("---" for _ in columns) + " |"]
    for row in rows:
        rendered = []
        for column in columns:
            value = row.get(column, "")
            if isinstance(value, list):
                value = ";".join(str(item) for item in value)
            elif isinstance(value, dict):
                value = json.dumps(value, sort_keys=True)
            rendered.append(str(value))
        lines.append("| " + " | ".join(rendered) + " |")
    if footer:
        lines.extend(["", footer])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def safe_filename(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("_") or "artifact"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create the integrated HS evaluation run.")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--positive-run", default="paper_eval_20260520")
    parser.add_argument("--negative-run", default="paper_negative_20260520")
    parser.add_argument("--force", action="store_true", help="Overwrite an existing integrated run directory.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    rows = create_integrated_run(
        args.repo_root,
        args.run_id,
        positive_run=args.positive_run,
        negative_run=args.negative_run,
        overwrite=args.force,
    )
    print(f"Created integrated run {args.run_id} with {len(rows)} artifacts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
