from __future__ import annotations

import json
import inspect
from pathlib import Path

from legal_extract_eval.negative_run import (
    create_negative_run,
    load_negative_registry,
    validate_negative_registry,
)


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
    "field_completeness_rate",
    "abstention_rate",
    "graph_artifact_parity",
    "human_research_burden",
    "rerun_delta_rate",
}


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def test_negative_case_registry_is_decision_complete(repo_root: Path) -> None:
    registry = load_negative_registry(repo_root)
    cases = registry["cases"]

    assert validate_negative_registry(repo_root, registry) == []
    assert len(cases) == 10
    assert {case["negative_case_id"] for case in cases} == {f"NEG_{idx:03d}" for idx in range(1, 11)}
    assert {metric for case in cases for metric in case["expected_failed_metrics"]} == EXPECTED_METRICS
    assert all(case["legal_rationale"] for case in cases)
    assert all(case["knowledge_evidence_registry_links"] for case in cases)


def test_negative_run_outputs_cover_all_fault_lines(repo_root: Path) -> None:
    run_root = repo_root / "runs" / "paper_negative_20260520"
    manifest = load_json(run_root / "RUN_MANIFEST.json")
    detection_rows = load_json(run_root / "reports" / "negative_detection_matrix.json")
    metric_rows = load_json(run_root / "reports" / "metric_summary.json")
    gate_rows = load_json(run_root / "reports" / "gate_summary.json")

    assert manifest["run_type"] == "controlled_negative_fault_injection"
    assert manifest["case_count"] == 10
    assert set(manifest["expected_metric_coverage"]) == EXPECTED_METRICS
    assert len(detection_rows) == 10
    assert all(row["negative_test_passed"] is True for row in detection_rows)
    assert all(row["gate_match"] is True for row in detection_rows)
    assert all(row["recall"] == 1.0 for row in detection_rows)
    assert {row["gate_label"] for row in gate_rows} == {
        "pass_with_notes",
        "blocked_pending_research",
        "blocked_pending_rerun",
    }

    by_metric = {row["metric_id"]: row for row in metric_rows}
    for metric_id in EXPECTED_METRICS:
        assert by_metric[metric_id]["status"] != "not_applicable"
    assert by_metric["rerun_delta_rate"]["status"] == "comparison_only"
    assert by_metric["graph_artifact_parity"]["status"] != "pass"
    assert by_metric["evidence_gap_detection"]["denominator"] > 0
    assert by_metric["human_research_burden"]["status"] == "diagnostic"


def test_negative_run_gate_expectations_are_observed(repo_root: Path) -> None:
    detection_rows = load_json(repo_root / "runs" / "paper_negative_20260520" / "reports" / "negative_detection_matrix.json")
    by_case = {row["negative_case_id"]: row for row in detection_rows}

    assert by_case["NEG_001"]["observed_gate_label"] == "blocked_pending_research"
    assert by_case["NEG_002"]["observed_gate_label"] == "blocked_pending_research"
    assert by_case["NEG_003"]["observed_gate_label"] == "blocked_pending_research"
    assert by_case["NEG_004"]["observed_gate_label"] == "pass_with_notes"
    assert by_case["NEG_008"]["observed_gate_label"] == "blocked_pending_rerun"
    assert by_case["NEG_009"]["observed_gate_label"] == "blocked_pending_rerun"
    assert by_case["NEG_010"]["observed_gate_label"] == "pass_with_notes"


def test_negative_run_is_not_control_row_transcription() -> None:
    source = inspect.getsource(create_negative_run)

    assert "control_row_for" not in source
    assert "evaluate_aa_run" in source


def test_negative_detection_matrix_reports_oracle_comparison(repo_root: Path) -> None:
    aggregates = load_json(repo_root / "runs" / "paper_negative_20260520" / "reports" / "negative_detection_aggregates.json")
    rows = load_json(repo_root / "runs" / "paper_negative_20260520" / "reports" / "negative_detection_matrix.json")

    assert aggregates["gate_accuracy"] == 1.0
    assert aggregates["micro_recall"] == 1.0
    assert aggregates["false_negative_total"] == 0
    for row in rows:
        assert set(row) >= {
            "true_positive_checks",
            "false_positive_checks",
            "false_negative_checks",
            "precision",
            "recall",
            "f1",
            "gate_match",
        }


def test_negative_results_packet_has_paper_tables(repo_root: Path) -> None:
    packet = repo_root / "runs" / "paper_negative_20260520" / "reports" / "negative_results_packet.md"
    text = packet.read_text(encoding="utf-8")

    assert "Table 1. Positive Baseline Summary" in text
    assert "Table 2. Negative Case Design Matrix" in text
    assert "Table 3. Metric Fault-Detection Matrix" in text
    assert "Table 4. Negative Gate Distribution" in text
    assert "Table 5. Representative Detected Failures" in text
    assert "Detection Aggregates" in text
    assert "does not claim broad adversarial robustness" in text
