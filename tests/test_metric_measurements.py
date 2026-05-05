from __future__ import annotations

import json
from pathlib import Path

from legal_extract_eval.metric_calculator import METRIC_REPORT_COLUMNS, calculate_metric_summary


EXPECTED_METRICS = {
    "authority_boundary_compliance",
    "material_legal_capture",
    "provenance_sufficiency",
    "primary_authority_sufficiency",
    "critical_omission_rate",
    "unsupported_synthesis_rate",
    "false_certainty_rate",
    "conflict_preservation",
    "evidence_gap_detection",
    "handoff_safety",
    "human_review_trigger_correctness",
}


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def test_measurement_framework_is_decision_complete(repo_root: Path) -> None:
    framework = load_json(repo_root / "protocol" / "measurement_framework.json")
    metrics = framework["metrics"]

    assert {metric["metric_id"] for metric in metrics} == EXPECTED_METRICS
    for metric in metrics:
        assert metric["control_family"]
        assert metric["linked_validator"]
        assert metric["numerator"]
        assert metric["denominator"]
        assert " / " in metric["formula"]
        assert metric["blocker_override_rule"]
        assert metric["stress_test_type"]
        assert metric["report_field"]
        assert metric["paper_safe_explanation"]


def test_trace_artifacts_exist_and_have_expected_shape(repo_root: Path) -> None:
    trace_dir = repo_root / "runs" / "paper_frozen_run" / "trace"
    expected_files = {
        "agent_trace.json",
        "claim_trace.json",
        "rule_invocation_graph.json",
        "gating_decisions.json",
        "uncertainty_signals.json",
        "metric_inputs.json",
    }

    assert expected_files == {path.name for path in trace_dir.glob("*.json")}
    assert len(load_json(trace_dir / "claim_trace.json")["claims"]) == 28
    assert len(load_json(trace_dir / "gating_decisions.json")["decisions"]) == 28
    assert len(load_json(trace_dir / "uncertainty_signals.json")["signals"]) == 28
    assert len(load_json(trace_dir / "metric_inputs.json")["stress_tests"]) == 11


def test_metric_calculator_outputs_all_colleague_metrics(repo_root: Path) -> None:
    rows = calculate_metric_summary(repo_root, "paper_frozen_run")

    assert {row["metric_id"] for row in rows} == EXPECTED_METRICS
    for row in rows:
        assert set(METRIC_REPORT_COLUMNS).issubset(row)
        assert 0 <= row["score"] <= 1
        assert row["status"] in {"pass", "warning", "review_trigger", "blocker"}

    by_id = {row["metric_id"]: row for row in rows}
    assert by_id["authority_boundary_compliance"]["score"] == 1.0
    assert by_id["material_legal_capture"]["denominator"] > 0
    assert by_id["provenance_sufficiency"]["denominator"] == 28
    assert by_id["critical_omission_rate"]["score"] == 1.0
    assert by_id["unsupported_synthesis_rate"]["score"] == 1.0
    assert by_id["false_certainty_rate"]["denominator"] > 0
    assert by_id["handoff_safety"]["denominator"] > 0
    assert by_id["human_review_trigger_correctness"]["denominator"] > 0


def test_metric_reports_and_stress_tests_are_written(repo_root: Path) -> None:
    report_dir = repo_root / "runs" / "paper_frozen_run" / "reports"
    for filename in (
        "metric_summary.json",
        "metric_summary.csv",
        "metric_summary.md",
        "metric_stress_tests.json",
        "metric_stress_tests.md",
    ):
        assert (report_dir / filename).exists()

    metric_rows = load_json(report_dir / "metric_summary.json")
    stress_rows = load_json(report_dir / "metric_stress_tests.json")
    assert len(metric_rows) == 11
    assert len(stress_rows) == 11
    assert {row["expected_failed_metric"] for row in stress_rows} == EXPECTED_METRICS
    assert all(row["deterministic_detection_rule"] is True for row in stress_rows)


def test_authority_and_claim_traces_are_paper_scope(repo_root: Path) -> None:
    trace_dir = repo_root / "runs" / "paper_frozen_run" / "trace"
    agent_events = load_json(trace_dir / "agent_trace.json")["events"]
    claim_trace = load_json(trace_dir / "claim_trace.json")["claims"]

    for event in agent_events:
        for source_use in event.get("source_uses", []):
            assert source_use["source_id"].startswith(("SRC_EU", "SRC_WCO"))
            assert source_use["permitted"] is True

    for claim in claim_trace:
        assert claim["verifiable_source_trace"] is True
        assert claim["source_trace"]
        assert all(item["source_id"].startswith(("SRC_EU", "SRC_WCO")) for item in claim["source_trace"])
