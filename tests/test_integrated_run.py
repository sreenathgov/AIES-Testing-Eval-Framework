from __future__ import annotations

import json
import inspect
from collections import Counter
from pathlib import Path

from legal_extract_eval.integrated_run import create_integrated_run


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


def test_integrated_run_has_expected_cohort_shape(repo_root: Path) -> None:
    run_root = repo_root / "runs" / "paper_integrated_20260520"
    manifest = load_json(run_root / "RUN_MANIFEST.json")
    rows = load_json(run_root / "reports" / "control_profile.json")

    assert manifest["run_type"] == "integrated_40_artifact_evaluation"
    assert manifest["total_artifact_count"] == 40
    assert manifest["cohort_counts"] == {"baseline": 28, "fault_injection": 12}
    assert len(rows) == 40
    assert Counter(row["cohort"] for row in rows) == {"baseline": 28, "fault_injection": 12}
    assert all(row["negative_case_id"] is None for row in rows if row["cohort"] == "baseline")
    assert all(row["negative_case_id"] for row in rows if row["cohort"] == "fault_injection")


def test_integrated_gate_distribution_matches_paper_claim(repo_root: Path) -> None:
    gate_rows = load_json(repo_root / "runs" / "paper_integrated_20260520" / "reports" / "gate_summary.json")
    counts = Counter(row["gate_label"] for row in gate_rows)

    assert counts == {
        "pass": 22,
        "pass_with_notes": 8,
        "blocked_pending_research": 8,
        "blocked_pending_rerun": 2,
    }

    by_cohort = {
        cohort: Counter(row["gate_label"] for row in gate_rows if row["cohort"] == cohort)
        for cohort in {"baseline", "fault_injection"}
    }
    assert by_cohort["baseline"] == {"pass": 22, "pass_with_notes": 6}
    assert by_cohort["fault_injection"] == {
        "pass_with_notes": 2,
        "blocked_pending_research": 8,
        "blocked_pending_rerun": 2,
    }


def test_integrated_detection_matrix_preserves_negative_outcomes(repo_root: Path) -> None:
    rows = load_json(repo_root / "runs" / "paper_integrated_20260520" / "reports" / "integrated_detection_matrix.json")
    aggregates = load_json(repo_root / "runs" / "paper_integrated_20260520" / "reports" / "integrated_detection_aggregates.json")

    assert len(rows) == 12
    assert all(row["negative_test_passed"] is True for row in rows)
    assert all(row["gate_match"] is True for row in rows)
    assert all(row["recall"] == 1.0 for row in rows)
    assert aggregates["gate_accuracy"] == 1.0
    assert aggregates["micro_recall"] == 1.0
    assert {row["negative_case_id"] for row in rows} == {f"NEG_{idx:03d}" for idx in range(1, 13)}


def test_integrated_run_revalidates_instead_of_merging_control_profiles() -> None:
    source = inspect.getsource(create_integrated_run)

    assert "evaluate_mixed_run" in source
    assert "merge_control_rows(" not in source


def test_integrated_metrics_are_present_and_comparison_only_remains_non_dispositive(repo_root: Path) -> None:
    rows = load_json(repo_root / "runs" / "paper_integrated_20260520" / "reports" / "metric_summary.json")
    by_id = {row["metric_id"]: row for row in rows}

    assert set(by_id) == EXPECTED_METRICS
    assert by_id["rerun_delta_rate"]["status"] == "comparison_only"
    assert by_id["evidence_gap_detection"]["denominator"] > 0
    assert by_id["human_research_burden"]["status"] == "diagnostic"


def test_baseline_artifacts_do_not_acquire_fault_injection_checks(repo_root: Path) -> None:
    rows = load_json(repo_root / "runs" / "paper_integrated_20260520" / "reports" / "control_profile.json")
    fault_checks = {
        "internal_source_as_authority",
        "source_anchor_not_resolved",
        "secondary_only_authority_chain",
        "critical_omission",
        "unsupported_promotion",
        "confidence_inflation",
        "evidence_gap",
        "missing_required_handoff_field",
        "graph_parity_failure",
        "over_escalation_burden",
        "quote_anchor_unresolved",
        "product_identity_mixed_with_classification_state",
    }

    for row in rows:
        if row["cohort"] == "baseline":
            assert not (set(row["failed_checks"]) & fault_checks)


def test_integrated_results_packet_has_required_paper_tables(repo_root: Path) -> None:
    text = (repo_root / "runs" / "paper_integrated_20260520" / "reports" / "integrated_results_packet.md").read_text(encoding="utf-8")

    assert "Table 1. Integrated Run Summary" in text
    assert "Table 2. Integrated Gate Distribution" in text
    assert "Table 3. Cohort Gate Distribution" in text
    assert "Table 4. Integrated Metric Summary" in text
    assert "Table 5. Fault-Injection Detection Matrix" in text
    assert "Detection Aggregates" in text
    assert "Do not interpret aggregate metric scores alone as proof of legal correctness" in text
