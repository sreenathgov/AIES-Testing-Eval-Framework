from __future__ import annotations

from typing import Any

from .models import ValidatorResult


REPRESENTATION_TAGS = {
    "product_identity_mixed_with_classification_state": "product_identity_mixed_with_classification_state",
    "confidence_inflation": "confidence_inflation",
    "divergence_collapsed": "divergence_collapsed",
}


class RepresentationIntegrityValidator:
    def validate(self, fixture: dict[str, Any]) -> ValidatorResult:
        checks: list[str] = []
        tags = set(fixture.get("known_issue_tags", []))

        for tag, check in REPRESENTATION_TAGS.items():
            if tag in tags:
                checks.append(check)

        if fixture.get("confidence_state") == "high" and fixture.get("stability_state") == "stable":
            if {"confidence_inflation", "provenance_deficient", "unsupported_promotion"} & tags:
                checks.append("representation_scope_broadened")

        if fixture.get("legal_hierarchy_expectations") is None:
            checks.append("legal_hierarchy_incomplete")

        if fixture.get("comparison_only") and fixture.get("handoff_route") == "promote":
            if any(
                "conflict" in str(value.get("status", ""))
                for value in fixture.get("comparison_only", {}).values()
                if isinstance(value, dict)
            ):
                checks.append("comparison_only_conflict_collapsed")

        return ValidatorResult.pass_() if not checks else ValidatorResult.review(*checks)
