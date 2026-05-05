from __future__ import annotations

from legal_extract_eval.evaluator import Evaluator
from legal_extract_eval.perturbation_validator import (
    inflate_confidence,
    remove_legal_authority,
    reverse_first_classification_edge,
)


def test_remove_legal_authority_blocks_good_artifact(
    fixture_by_id: dict[str, dict],
    edges: list[dict],
    source_manifest: dict,
    gold_by_artifact: dict[str, dict],
) -> None:
    fixture = remove_legal_authority(fixture_by_id["FX_GOOD_OBC_AA_EU"])
    evaluator = Evaluator([fixture], edges, source_manifest, [gold_by_artifact[fixture["artifact_id"]]])
    result = evaluator.evaluate_all()[0]

    assert result.actual_route == "blocked"
    assert result.final_control_state == "gap"
    assert "missing_external_authority" in result.failed_checks
    assert "missing_source_anchor" in result.failed_checks
    assert result.passed_gold is False


def test_confidence_inflation_routes_to_review(
    fixture_by_id: dict[str, dict],
    edges: list[dict],
    source_manifest: dict,
    gold_by_artifact: dict[str, dict],
) -> None:
    fixture = inflate_confidence(fixture_by_id["FX_GOOD_OBC_AA_EU"])
    evaluator = Evaluator([fixture], edges, source_manifest, [gold_by_artifact[fixture["artifact_id"]]])
    result = evaluator.evaluate_all()[0]

    assert result.actual_route == "review"
    assert result.final_control_state == "contested"
    assert "confidence_inflation" in result.failed_checks
    assert "unsupported_promotion" in result.failed_checks
    assert result.passed_gold is False


def test_reversed_classification_edge_blocks_graph_parity(
    fixture_by_id: dict[str, dict],
    edges: list[dict],
    source_manifest: dict,
    gold_by_artifact: dict[str, dict],
) -> None:
    fixture = fixture_by_id["FX_GOOD_OBC_AA_EU"]
    reversed_edges = reverse_first_classification_edge(edges)
    evaluator = Evaluator([fixture], reversed_edges, source_manifest, [gold_by_artifact[fixture["artifact_id"]]])
    result = evaluator.evaluate_all()[0]

    assert result.actual_route == "blocked"
    assert result.final_control_state == "parity_failure"
    assert "edge_direction_invalid" in result.failed_checks
    assert "missing_proposes_code_edge" in result.failed_checks
    assert result.passed_gold is False
