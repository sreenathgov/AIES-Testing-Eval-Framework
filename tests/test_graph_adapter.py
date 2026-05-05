from __future__ import annotations

from copy import deepcopy

from legal_extract_eval.graph_adapter import GraphAdapter


def test_good_fixture_graph_parity_passes(
    fixtures: list[dict],
    edges: list[dict],
    source_manifest: dict,
) -> None:
    graph = GraphAdapter.build(fixtures, edges, source_manifest)

    for fixture in fixtures:
        if fixture["fixture_class"] == "good":
            result = graph.validate_fixture(fixture)
            assert result.status == "pass", fixture["artifact_id"]


def test_reversed_edge_fixture_fails_graph_parity(
    fixtures: list[dict],
    fixture_by_id: dict[str, dict],
    edges: list[dict],
    source_manifest: dict,
) -> None:
    graph = GraphAdapter.build(fixtures, edges, source_manifest)
    result = graph.validate_fixture(fixture_by_id["FX_BAD_OBC_EDGE_DIRECTION"])

    assert result.status == "fail"
    assert "edge_direction_invalid" in result.failed_checks
    assert "missing_proposes_code_edge" in result.failed_checks


def test_source_edges_must_resolve_to_source_manifest(
    fixtures: list[dict],
    fixture_by_id: dict[str, dict],
    edges: list[dict],
    source_manifest: dict,
) -> None:
    mutated_edges = deepcopy(edges)
    for edge in mutated_edges:
        if edge["edge_id"] == "E_GOOD_OBC_SUPPORTED_EU_CN":
            edge["target_node_id"] = "source:SRC_UNKNOWN"
            break

    graph = GraphAdapter.build(fixtures, mutated_edges, source_manifest)
    result = graph.validate_fixture(fixture_by_id["FX_GOOD_OBC_AA_EU"])

    assert result.status == "fail"
    assert "edge_endpoint_unresolved" in result.failed_checks


def test_hs_code_is_not_allowed_as_component_parent(
    fixtures: list[dict],
    edges: list[dict],
    source_manifest: dict,
) -> None:
    graph = GraphAdapter.build(fixtures, edges, source_manifest)
    invalid_edges = [
        edge
        for edge in edges
        if edge["edge_type"] == "classified_as" and edge["source_node_id"].startswith("hs_code:")
    ]

    assert invalid_edges
    assert graph.validate_fixture(next(f for f in fixtures if f["artifact_id"] == "FX_BAD_OBC_EDGE_DIRECTION")).status == "fail"
