from __future__ import annotations

from legal_extract_eval.report_generator import REPORT_COLUMNS, control_profile_rows, render_markdown


def test_control_profile_report_has_required_columns(evaluator) -> None:
    rows = control_profile_rows(evaluator.evaluate_all())

    assert len(rows) == 15
    assert tuple(rows[0].keys()) == REPORT_COLUMNS
    assert REPORT_COLUMNS == (
        "scenario_id",
        "artifact_id",
        "fixture_class",
        "artifact_type",
        "agent_stage",
        "jurisdiction",
        "candidate_hs_code",
        "candidate_cn_code",
        "authority_status",
        "provenance_status",
        "source_integrity_status",
        "quote_fidelity_status",
        "capture_status",
        "representation_status",
        "legal_method_status",
        "graph_parity_status",
        "synthesis_status",
        "uncertainty_status",
        "handoff_status",
        "failed_checks",
        "severity",
        "expected_route",
        "actual_route",
        "human_review_required",
        "recommended_action",
    )


def test_markdown_report_renders_control_profile(evaluator) -> None:
    report = render_markdown(evaluator.evaluate_all())

    assert report.startswith("# Control Profile Report")
    assert "Gold conformance: 15/15" in report
    assert "FX_BAD_HS_85044084_INTERNAL_AUTHORITY" in report
    assert "internal_source_as_authority" in report
    assert "source_integrity_status" in report
    assert "capture_status" in report
    assert "recommended_action" in report
