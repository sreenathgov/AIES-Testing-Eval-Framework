from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable


METRIC_REPORT_COLUMNS = (
    "metric_id",
    "name",
    "score",
    "numerator",
    "denominator",
    "status",
    "formula",
    "blocker_override_applied",
    "stress_test_type",
    "linked_validator",
    "notes",
)


@dataclass(frozen=True)
class Fraction:
    numerator: float
    denominator: float
    inverse: bool = False

    @property
    def score(self) -> float:
        if self.denominator == 0:
            return 1.0
        value = self.numerator / self.denominator
        return 1.0 - value if self.inverse else value


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def calculate_metric_summary(repo_root: Path, run_id: str) -> list[dict[str, Any]]:
    framework = read_json(repo_root / "protocol" / "measurement_framework.json")
    trace = load_trace_bundle(repo_root, run_id)
    calculators: dict[str, Callable[[dict[str, Any]], Fraction]] = {
        "authority_boundary_compliance": authority_boundary_compliance,
        "material_legal_capture": material_legal_capture,
        "provenance_sufficiency": provenance_sufficiency,
        "primary_authority_sufficiency": primary_authority_sufficiency,
        "critical_omission_rate": critical_omission_rate,
        "unsupported_synthesis_rate": unsupported_synthesis_rate,
        "false_certainty_rate": false_certainty_rate,
        "conflict_preservation": conflict_preservation,
        "evidence_gap_detection": evidence_gap_detection,
        "handoff_safety": handoff_safety,
        "human_review_trigger_correctness": human_review_trigger_correctness,
        "field_completeness_rate": field_completeness_rate,
        "abstention_rate": abstention_rate,
        "semantic_graph_alignment": semantic_graph_alignment,
        "human_research_burden": human_research_burden,
        "rerun_delta_rate": rerun_delta_rate,
    }
    stress_results = {
        item["stress_test_type"]: item
        for item in trace["metric_inputs"].get("stress_tests", [])
    }
    rows: list[dict[str, Any]] = []
    for metric in framework["metrics"]:
        metric_id = metric["metric_id"]
        fraction = calculators[metric_id](trace)
        score = round(fraction.score, 4)
        stress = stress_results.get(metric["stress_test_type"], {})
        blocker_override = bool(stress.get("expected_control_state") in {"blocked", "review"} and score < 1.0)
        rows.append(
            {
                "metric_id": metric_id,
                "name": metric["name"],
                "score": score,
                "numerator": fraction.numerator,
                "denominator": fraction.denominator,
                "status": metric_status(metric_id, score),
                "formula": metric["formula"],
                "blocker_override_applied": blocker_override,
                "stress_test_type": metric["stress_test_type"],
                "linked_validator": metric["linked_validator"],
                "notes": metric["paper_safe_explanation"],
            }
        )
    return rows


def write_metric_reports(repo_root: Path, run_id: str, rows: list[dict[str, Any]]) -> None:
    report_dir = repo_root / "runs" / run_id / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    write_json(report_dir / "metric_summary.json", rows)
    with (report_dir / "metric_summary.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=METRIC_REPORT_COLUMNS)
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in METRIC_REPORT_COLUMNS})
    lines = [
        "# Metric Summary",
        "",
        "Diagnostic metrics explain the control profile. They do not override blocker or review gates.",
        "",
        "| " + " | ".join(METRIC_REPORT_COLUMNS) + " |",
        "| " + " | ".join("---" for _ in METRIC_REPORT_COLUMNS) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(column, "")) for column in METRIC_REPORT_COLUMNS) + " |")
    lines.append("")
    lines.append(f"Metrics evaluated: {len(rows)}")
    (report_dir / "metric_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    write_metric_stress_reports(repo_root, run_id, rows)


def write_metric_stress_reports(repo_root: Path, run_id: str, rows: list[dict[str, Any]]) -> None:
    report_dir = repo_root / "runs" / run_id / "reports"
    trace = load_trace_bundle(repo_root, run_id)
    by_stress_type = {row["stress_test_type"]: row for row in rows}
    stress_rows: list[dict[str, Any]] = []
    for scenario in trace["metric_inputs"].get("stress_tests", []):
        metric = by_stress_type.get(scenario["stress_test_type"], {})
        stress_rows.append(
            {
                "stress_test_type": scenario["stress_test_type"],
                "expected_failed_metric": scenario["expected_failed_metric"],
                "expected_control_state": scenario["expected_control_state"],
                "linked_metric_id": metric.get("metric_id"),
                "linked_validator": metric.get("linked_validator"),
                "deterministic_detection_rule": True,
                "notes": "Synthetic perturbation contract for reviewer-facing measurement validation.",
            }
        )
    write_json(report_dir / "metric_stress_tests.json", stress_rows)
    columns = (
        "stress_test_type",
        "expected_failed_metric",
        "expected_control_state",
        "linked_metric_id",
        "linked_validator",
        "deterministic_detection_rule",
        "notes",
    )
    lines = ["# Metric Stress Tests", ""]
    lines.append("| " + " | ".join(columns) + " |")
    lines.append("| " + " | ".join("---" for _ in columns) + " |")
    for row in stress_rows:
        lines.append("| " + " | ".join(str(row.get(column, "")) for column in columns) + " |")
    lines.append("")
    lines.append(f"Stress tests specified: {len(stress_rows)}")
    (report_dir / "metric_stress_tests.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def load_trace_bundle(repo_root: Path, run_id: str) -> dict[str, Any]:
    trace_dir = repo_root / "runs" / run_id / "trace"
    return {
        "agent_trace": read_json(trace_dir / "agent_trace.json"),
        "claim_trace": read_json(trace_dir / "claim_trace.json"),
        "rule_invocation_graph": read_json(trace_dir / "rule_invocation_graph.json"),
        "gating_decisions": read_json(trace_dir / "gating_decisions.json"),
        "uncertainty_signals": read_json(trace_dir / "uncertainty_signals.json"),
        "metric_inputs": read_json(trace_dir / "metric_inputs.json"),
        "field_completeness_trace": read_json(trace_dir / "field_completeness_trace.json"),
        "graph_alignment_trace": read_json(trace_dir / "graph_alignment_trace.json"),
        "abstention_trace": read_json(trace_dir / "abstention_trace.json"),
        "research_burden_trace": read_json(trace_dir / "research_burden_trace.json"),
        "rerun_delta_trace": read_json(trace_dir / "rerun_delta_trace.json"),
    }


def authority_boundary_compliance(trace: dict[str, Any]) -> Fraction:
    uses = [
        source_use
        for event in trace["agent_trace"]["events"]
        for source_use in event.get("source_uses", [])
    ]
    permitted = sum(1 for source_use in uses if source_use.get("permitted") is True)
    return Fraction(permitted, len(uses))


def material_legal_capture(trace: dict[str, Any]) -> Fraction:
    rules = trace["rule_invocation_graph"]["required_rule_items"]
    used_weight = sum(item["weight"] for item in rules if item.get("used") is True)
    total_weight = sum(item["weight"] for item in rules)
    return Fraction(used_weight, total_weight)


def provenance_sufficiency(trace: dict[str, Any]) -> Fraction:
    claims = trace["claim_trace"]["claims"]
    sourced = sum(1 for claim in claims if claim.get("verifiable_source_trace") is True)
    return Fraction(sourced, len(claims))


def primary_authority_sufficiency(trace: dict[str, Any]) -> Fraction:
    decisions = trace["metric_inputs"]["decisions"]
    supported = sum(1 for decision in decisions if decision.get("has_primary_or_interpretive_authority") is True)
    return Fraction(supported, len(decisions))


def critical_omission_rate(trace: dict[str, Any]) -> Fraction:
    decisive = [item for item in trace["rule_invocation_graph"]["required_rule_items"] if item.get("decisive") is True]
    missing = sum(1 for item in decisive if item.get("used") is not True)
    return Fraction(missing, len(decisive), inverse=True)


def unsupported_synthesis_rate(trace: dict[str, Any]) -> Fraction:
    edges = trace["rule_invocation_graph"]["inference_edges"]
    unsupported = sum(1 for edge in edges if edge.get("supported") is not True)
    return Fraction(unsupported, len(edges), inverse=True)


def false_certainty_rate(trace: dict[str, Any]) -> Fraction:
    signals = trace["uncertainty_signals"]["signals"]
    ambiguous = [signal for signal in signals if signal.get("ambiguous_or_contested") is True]
    unsafe = sum(1 for signal in ambiguous if signal.get("high_confidence_promote") is True)
    return Fraction(unsafe, len(ambiguous), inverse=True)


def conflict_preservation(trace: dict[str, Any]) -> Fraction:
    conflicts = [signal for signal in trace["uncertainty_signals"]["signals"] if signal.get("conflict_case") is True]
    preserved = sum(1 for signal in conflicts if signal.get("conflict_preserved") is True)
    return Fraction(preserved, len(conflicts))


def evidence_gap_detection(trace: dict[str, Any]) -> Fraction:
    gaps = [signal for signal in trace["uncertainty_signals"]["signals"] if signal.get("incomplete_case") is True]
    flagged = sum(1 for signal in gaps if signal.get("gap_flagged") is True)
    return Fraction(flagged, len(gaps))


def handoff_safety(trace: dict[str, Any]) -> Fraction:
    decisions = [item for item in trace["gating_decisions"]["decisions"] if item.get("unsafe_output") is True]
    intercepted = sum(1 for item in decisions if item.get("intercepted") is True)
    return Fraction(intercepted, len(decisions))


def human_review_trigger_correctness(trace: dict[str, Any]) -> Fraction:
    decisions = [item for item in trace["gating_decisions"]["decisions"] if item.get("requires_escalation") is True]
    correct = sum(1 for item in decisions if item.get("correct_escalation") is True)
    return Fraction(correct, len(decisions))


def field_completeness_rate(trace: dict[str, Any]) -> Fraction:
    checks = trace["field_completeness_trace"]["checks"]
    present = sum(1 for check in checks if check.get("present") is True)
    return Fraction(present, len(checks))


def abstention_rate(trace: dict[str, Any]) -> Fraction:
    cases = trace["abstention_trace"]["cases"]
    correct = sum(1 for case in cases if case.get("correct_abstention") is True)
    return Fraction(correct, len(cases))


def semantic_graph_alignment(trace: dict[str, Any]) -> Fraction:
    items = trace["graph_alignment_trace"]["items"]
    aligned = sum(1 for item in items if item.get("aligned") is True)
    return Fraction(aligned, len(items))


def human_research_burden(trace: dict[str, Any]) -> Fraction:
    summary = trace["research_burden_trace"]["summary"]
    return Fraction(summary.get("review_or_block_tickets", 0), summary.get("total_artifacts", 0), inverse=True)


def rerun_delta_rate(trace: dict[str, Any]) -> Fraction:
    summary = trace["rerun_delta_trace"]["summary"]
    if not summary.get("comparison_enabled", False):
        return Fraction(0, 0)
    return Fraction(summary.get("changed_outputs", 0), summary.get("comparable_outputs", 0), inverse=True)


def metric_status(metric_id: str, score: float) -> str:
    if metric_id == "human_research_burden":
        return "diagnostic"
    if metric_id == "rerun_delta_rate" and score >= 1.0:
        return "comparison_only"
    if metric_id in {"critical_omission_rate", "unsupported_synthesis_rate", "false_certainty_rate", "rerun_delta_rate"}:
        # These are normalized safety scores after inverse-rate conversion.
        pass
    if score >= 1.0:
        return "pass"
    if score >= 0.95:
        return "warning"
    if score >= 0.8:
        return "review_trigger"
    return "blocker"
