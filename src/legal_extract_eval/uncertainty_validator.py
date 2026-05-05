from __future__ import annotations

from .models import ValidatorResult


UNCERTAINTY_TAGS = {
    "confidence_inflation",
    "divergence_collapsed",
    "jurisdictional_divergence_preserved",
    "comparison_only_divergence_preserved",
    "comparison_only_non_eu_divergence",
    "client_fact_required",
}


class UncertaintyValidator:
    def validate(self, fixture: dict) -> ValidatorResult:
        checks: list[str] = []
        tags = set(fixture.get("known_issue_tags", []))

        for tag in sorted(tags & UNCERTAINTY_TAGS):
            if tag == "comparison_only_non_eu_divergence":
                checks.append("comparison_only_divergence_preserved")
            else:
                checks.append(tag)

        comparison_only = fixture.get("comparison_only", {})
        has_comparison_conflict = any(
            "conflict" in str(value.get("status", ""))
            for value in comparison_only.values()
            if isinstance(value, dict)
        )
        if has_comparison_conflict and fixture.get("handoff_route") == "promote":
            checks.append("divergence_collapsed")

        if "confidence_inflation" in checks and fixture.get("confidence_state") == "high":
            checks.append("unsupported_promotion")

        return ValidatorResult.pass_() if not checks else ValidatorResult.review(*checks)
