from __future__ import annotations

from .models import EXTERNAL_AUTHORITY_CLASSES, ValidatorResult


class AgentRoleValidator:
    def validate(self, fixture: dict) -> ValidatorResult:
        checks: list[str] = []
        tags = set(fixture.get("known_issue_tags", []))
        stage = fixture.get("agent_stage")
        authority_classes = {
            item.get("authority_class")
            for item in fixture.get("legal_authority_chain", [])
            if item.get("authority_class") in EXTERNAL_AUTHORITY_CLASSES
        }

        if stage == "PTA" and fixture.get("handoff_route") == "promote":
            checks.append("pta_final_adjudication_overreach")
        if stage == "PTA" and "GRI_3b" in fixture.get("gri_path", []) and "pta_requires_aa_review" in tags:
            checks.append("pta_requires_aa_review")
        if stage == "PRA" and "ruling_or_precedent" in authority_classes and "primary_legal_text" not in authority_classes:
            checks.append("pra_ruling_without_primary_law_anchor")
        if stage == "PRA" and "classification_decision" in authority_classes and "primary_legal_text" not in authority_classes:
            checks.append("pra_decision_without_primary_law_anchor")
        if stage == "DA" and fixture.get("handoff_route") == "promote":
            checks.append("da_secondary_context_final_authority")
        if stage == "AA" and fixture.get("handoff_route") == "promote" and not fixture.get("legal_authority_chain"):
            checks.append("aa_invented_authority")
        if "product_identity_mixed_with_classification_state" in tags:
            checks.append("product_identity_mixed_with_classification_state")
        if stage == "KA" and fixture.get("legal_proposition"):
            checks.append("audit_created_legal_proposition")

        return ValidatorResult.pass_() if not checks else ValidatorResult.review(*checks)
