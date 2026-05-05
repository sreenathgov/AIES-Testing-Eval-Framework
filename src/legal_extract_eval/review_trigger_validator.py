from __future__ import annotations

from typing import Any

from .models import ValidatorResult


REVIEW_TAGS = {
    "pta_final_adjudication_overreach",
    "pta_requires_aa_review",
    "product_identity_mixed_with_classification_state",
    "jurisdictional_divergence_preserved",
    "comparison_only_non_eu_divergence",
    "client_fact_required",
    "confidence_inflation",
    "divergence_collapsed",
}


class ReviewTriggerValidator:
    def validate(self, fixture: dict[str, Any]) -> ValidatorResult:
        checks: list[str] = []
        tags = set(fixture.get("known_issue_tags", []))
        review_reasons = set(fixture.get("review_reason_codes", []))
        expected_review = bool(tags & REVIEW_TAGS) or fixture.get("fixture_class") == "borderline"

        if expected_review and not review_reasons:
            checks.append("review_reason_codes_missing")

        if expected_review and fixture.get("handoff_route") == "promote":
            checks.append("review_trigger_missing_route")

        if fixture.get("handoff_route") == "review" and not review_reasons:
            checks.append("review_route_missing_reason_code")

        return ValidatorResult.pass_() if not checks else ValidatorResult.review(*checks)
