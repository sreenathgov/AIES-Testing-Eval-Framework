from __future__ import annotations

from copy import deepcopy

from legal_extract_eval.agent_role_validator import AgentRoleValidator


def test_pta_cannot_promote_final_classification(fixture_by_id: dict[str, dict]) -> None:
    result = AgentRoleValidator().validate(fixture_by_id["FX_BAD_HV_BATTERY_PACK_PTA_OVERREACH"])

    assert result.status == "review"
    assert "pta_final_adjudication_overreach" in result.failed_checks


def test_pra_decision_needs_primary_law_anchor(fixture_by_id: dict[str, dict]) -> None:
    fixture = deepcopy(fixture_by_id["FX_GOOD_HV_BATTERY_PACK_BTI_EU"])
    fixture["agent_stage"] = "PRA"
    fixture["legal_authority_chain"] = [
        item for item in fixture["legal_authority_chain"] if item["authority_class"] == "classification_decision"
    ]

    result = AgentRoleValidator().validate(fixture)

    assert result.status == "review"
    assert "pra_ruling_without_primary_law_anchor" in result.failed_checks


def test_da_material_cannot_route_as_final_authority(fixture_by_id: dict[str, dict]) -> None:
    fixture = deepcopy(fixture_by_id["FX_GOOD_OBC_AA_EU"])
    fixture["agent_stage"] = "DA"
    fixture["handoff_route"] = "promote"

    result = AgentRoleValidator().validate(fixture)

    assert result.status == "review"
    assert "da_secondary_context_final_authority" in result.failed_checks


def test_audit_agent_cannot_create_legal_proposition(fixture_by_id: dict[str, dict]) -> None:
    fixture = deepcopy(fixture_by_id["FX_GOOD_OBC_AA_EU"])
    fixture["agent_stage"] = "KA"

    result = AgentRoleValidator().validate(fixture)

    assert result.status == "review"
    assert "audit_created_legal_proposition" in result.failed_checks
