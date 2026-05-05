from __future__ import annotations

import json
from pathlib import Path


def test_control_framework_map_is_complete(repo_root: Path) -> None:
    framework = json.loads((repo_root / "protocol/control_framework.json").read_text())
    family_ids = {family["family_id"] for family in framework["control_families"]}
    dispositions = {metric["disposition"] for metric in framework["metric_dispositions"]}

    assert framework["paper_claim"].startswith("A governed legal extraction pipeline")
    assert len(framework["control_families"]) >= 10
    assert "corpus_source_integrity" in family_ids
    assert "source_grounding_anchor_verification" in family_ids
    assert "material_capture_completeness" in family_ids
    assert "supported_synthesis_control" in family_ids
    assert {"adopt", "rename", "demote_to_diagnostic", "future_work", "reject"} & dispositions
    assert "reject" in dispositions
    assert "future_work" in dispositions


def test_fixtures_expose_advanced_control_fields(fixtures: list[dict]) -> None:
    required_fields = {
        "material_legal_propositions",
        "required_source_anchors",
        "required_gri_path_elements",
        "competing_codes_considered",
        "rejected_codes",
        "legal_hierarchy_expectations",
        "source_temporal_context",
        "review_reason_codes",
        "prohibited_claims",
    }

    for fixture in fixtures:
        assert required_fields.issubset(fixture), fixture["artifact_id"]
        assert fixture["material_legal_propositions"], fixture["artifact_id"]
        assert fixture["source_temporal_context"]["tariff_year"] == "2025"


def test_gold_cases_include_control_family_expectations(gold_cases: list[dict]) -> None:
    for case in gold_cases:
        outcomes = case["expected_control_family_outcomes"]
        assert "corpus_source_integrity" in outcomes
        assert "source_grounding_anchor_verification" in outcomes
        assert "graph_artifact_parity" in outcomes
        assert case["expected_route"] in {"promote", "review", "blocked", "unresolved"}
        assert isinstance(case["human_review_required"], bool)
