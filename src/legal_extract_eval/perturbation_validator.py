from __future__ import annotations

from copy import deepcopy
from typing import Callable


def remove_legal_authority(fixture: dict) -> dict:
    mutated = deepcopy(fixture)
    mutated["legal_authority_chain"] = []
    mutated["source_ids"] = []
    return mutated


def inflate_confidence(fixture: dict) -> dict:
    mutated = deepcopy(fixture)
    mutated["confidence_state"] = "high"
    mutated["stability_state"] = "stable"
    tags = set(mutated.get("known_issue_tags", []))
    tags.add("confidence_inflation")
    mutated["known_issue_tags"] = sorted(tags)
    mutated["handoff_route"] = "promote"
    return mutated


def reverse_first_classification_edge(edges: list[dict]) -> list[dict]:
    mutated = deepcopy(edges)
    for edge in mutated:
        if edge.get("edge_type") in {"classified_as", "proposes_code"}:
            edge["source_node_id"], edge["target_node_id"] = edge["target_node_id"], edge["source_node_id"]
            break
    return mutated


PERTURBATIONS: dict[str, Callable[[dict], dict]] = {
    "remove_legal_authority": remove_legal_authority,
    "inflate_confidence": inflate_confidence,
}
