from __future__ import annotations

from typing import Any

from .models import EXTERNAL_AUTHORITY_CLASSES, INTERNAL_AUTHORITY_CLASSES, ValidatorResult


class SupportedSynthesisValidator:
    def validate(self, fixture: dict[str, Any]) -> ValidatorResult:
        checks: list[str] = []
        tags = set(fixture.get("known_issue_tags", []))
        classes = {item.get("authority_class") for item in fixture.get("legal_authority_chain", [])}

        if fixture.get("legal_proposition") and not (classes & EXTERNAL_AUTHORITY_CLASSES):
            checks.append("missing_external_authority")

        if classes and classes.issubset(INTERNAL_AUTHORITY_CLASSES):
            checks.append("internal_source_as_authority")

        if "unsupported_promotion" in tags:
            checks.append("unsupported_promotion")

        if "divergence_collapsed" in tags:
            checks.append("divergence_collapsed")

        if any(
            claim in fixture.get("prohibited_claims_made", [])
            for claim in fixture.get("prohibited_claims", [])
        ):
            checks.append("prohibited_claim_made")

        if any(check in {"missing_external_authority", "internal_source_as_authority", "unsupported_promotion"} for check in checks):
            return ValidatorResult.fail(*checks)
        return ValidatorResult.pass_() if not checks else ValidatorResult.review(*checks)
