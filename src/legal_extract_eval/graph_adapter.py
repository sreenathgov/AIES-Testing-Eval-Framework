from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Any

from .models import ARTIFACT_TYPE_TO_NODE_TYPE, ValidatorResult


ALLOWED_EDGE_DIRECTIONS: dict[str, set[tuple[str, str]]] = {
    "artifact_origin": {
        ("classification_candidate", "artifact_origin"),
        ("statutory_classification_record", "artifact_origin"),
        ("hs_code", "artifact_origin"),
    },
    "describes": {
        ("classification_candidate", "product_component"),
        ("statutory_classification_record", "product_component"),
        ("engineering_identity_record", "product_component"),
    },
    "proposes_code": {
        ("classification_candidate", "hs_code"),
        ("statutory_classification_record", "hs_code"),
    },
    "classified_as": {
        ("product_component", "hs_code"),
    },
    "supported_by": {
        ("classification_candidate", "source"),
        ("statutory_classification_record", "source"),
        ("ruling_record", "source"),
        ("hs_code", "source"),
    },
    "contains": {
        ("source", "legal_proposition"),
    },
    "evaluates": {
        ("audit_report", "classification_candidate"),
        ("audit_report", "statutory_classification_record"),
    },
    "routes": {
        ("handoff_package", "classification_candidate"),
        ("handoff_package", "statutory_classification_record"),
    },
    "comparison_only": {
        ("classification_candidate", "comparison_metadata"),
    },
}


@dataclass(frozen=True)
class GraphAdapter:
    nodes: dict[str, str]
    edges: dict[str, dict[str, Any]]
    source_ids: frozenset[str]

    @classmethod
    def build(
        cls,
        fixtures: list[dict[str, Any]],
        edges: list[dict[str, Any]],
        source_manifest: dict[str, Any],
    ) -> "GraphAdapter":
        nodes: dict[str, str] = {}
        for source in source_manifest["sources"]:
            nodes[f"source:{source['source_id']}"] = "source"
        for fixture in fixtures:
            for node in fixture.get("graph_nodes", []):
                nodes[node["node_id"]] = node["node_type"]
        return cls(
            nodes=nodes,
            edges={edge["edge_id"]: edge for edge in edges},
            source_ids=frozenset(source["source_id"] for source in source_manifest["sources"]),
        )

    def validate_fixture(self, fixture: dict[str, Any]) -> ValidatorResult:
        checks: list[str] = []
        node_id = fixture.get("sanitized_node_id")
        expected_node_type = ARTIFACT_TYPE_TO_NODE_TYPE.get(fixture.get("artifact_type"))
        if node_id not in self.nodes:
            checks.append("missing_graph_node")
        elif expected_node_type and self.nodes[node_id] != expected_node_type:
            checks.append("node_type_mismatch")

        fixture_edges = [self.edges.get(edge_id) for edge_id in fixture.get("graph_edges", [])]
        if any(edge is None for edge in fixture_edges):
            checks.append("missing_graph_edge")
        concrete_edges = [edge for edge in fixture_edges if edge is not None]

        outgoing_by_type: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for edge in concrete_edges:
            source_type = self.nodes.get(edge["source_node_id"])
            target_type = self.nodes.get(edge["target_node_id"])
            if source_type is None or target_type is None:
                checks.append("edge_endpoint_unresolved")
                continue
            allowed = ALLOWED_EDGE_DIRECTIONS.get(edge["edge_type"], set())
            if (source_type, target_type) not in allowed:
                checks.append("edge_direction_invalid")
            outgoing_by_type[edge["edge_type"]].append(edge)
            if edge["edge_type"] == "supported_by":
                source_id = edge["target_node_id"].removeprefix("source:")
                if source_id not in self.source_ids:
                    checks.append("source_edge_unresolved")

        if fixture.get("artifact_type") in {"classification_candidate", "statutory_classification_record"}:
            proposed_targets = {
                edge["target_node_id"]
                for edge in concrete_edges
                if edge["edge_type"] == "proposes_code" and edge["source_node_id"] == node_id
            }
            candidate_code = fixture.get("candidate_cn_code") or fixture.get("candidate_hs_code")
            if candidate_code:
                expected_target = f"hs_code:{candidate_code}:EU"
                if expected_target not in proposed_targets:
                    checks.append("missing_proposes_code_edge")

        return ValidatorResult.pass_() if not checks else ValidatorResult.fail(*checks)
