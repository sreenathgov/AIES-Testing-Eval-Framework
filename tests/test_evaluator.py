from __future__ import annotations


def test_all_fixtures_conform_to_gold_cases(results_by_id: dict[str, object]) -> None:
    assert len(results_by_id) == 15
    assert all(result.passed_gold for result in results_by_id.values())


def test_good_artifacts_promote_with_stable_control_state(results_by_id: dict[str, object]) -> None:
    good_ids = [
        "FX_GOOD_OBC_AA_EU",
        "FX_GOOD_HV_CONNECTORS_EU",
        "FX_GOOD_TRACTION_INVERTER_EU",
        "FX_GOOD_HV_BATTERY_PACK_BTI_EU",
        "FX_GOOD_LI_ION_CELL_EU",
    ]

    for artifact_id in good_ids:
        result = results_by_id[artifact_id]
        assert result.actual_route == "promote"
        assert result.final_control_state == "stable"
        assert result.failed_checks == ()


def test_internal_source_only_artifact_is_blocked(results_by_id: dict[str, object]) -> None:
    result = results_by_id["FX_BAD_HS_85044084_INTERNAL_AUTHORITY"]

    assert result.actual_route == "blocked"
    assert result.final_control_state == "gap"
    assert "internal_source_as_authority" in result.failed_checks
    assert "missing_external_authority" in result.failed_checks


def test_graph_parity_failure_blocks_handoff(results_by_id: dict[str, object]) -> None:
    result = results_by_id["FX_BAD_OBC_EDGE_DIRECTION"]

    assert result.actual_route == "blocked"
    assert result.final_control_state == "parity_failure"
    assert "edge_direction_invalid" in result.failed_checks
    assert "missing_proposes_code_edge" in result.failed_checks


def test_borderline_cases_route_to_review(results_by_id: dict[str, object]) -> None:
    borderline_ids = [
        "FX_BORDERLINE_LI_CELL_PRODUCT_NODE_MIXED_STATE",
        "FX_BORDERLINE_HV_BATTERY_PACK_GRI3B_REVIEW",
        "FX_BORDERLINE_SEPARATOR_DIVERGENCE",
        "FX_BORDERLINE_INTEGRATED_E_AXLE_COMPARISON_ONLY",
        "FX_BORDERLINE_NOES_CLIENT_FACT",
    ]

    for artifact_id in borderline_ids:
        result = results_by_id[artifact_id]
        assert result.actual_route == "review"
        assert result.final_control_state == "contested"
        assert result.human_review_required is True
