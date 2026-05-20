from __future__ import annotations

import re
from typing import Any

from .models import ValidatorResult
from .source_authority_registry import canonical_authority_class


CN_CODE_RE = re.compile(r"^\d{4}\.\d{2}(?:\.\d{2})?(?:\.\d{2})?$")


class LegalMethodValidator:
    def validate(self, fixture: dict[str, Any]) -> ValidatorResult:
        checks: list[str] = []
        candidate_cn_code = fixture.get("candidate_cn_code")
        gri_path = set(fixture.get("gri_path", []))
        anchors = {item.get("anchor_id") for item in fixture.get("legal_authority_chain", [])}

        if fixture.get("jurisdiction") == "EU" and candidate_cn_code and not CN_CODE_RE.match(candidate_cn_code):
            checks.append("cn_code_syntax_invalid")

        if "GRI_3b" in gri_path and "WCO_GRI_3B" not in anchors:
            checks.append("gri_3b_anchor_missing")

        if "GRI_3b" in gri_path and fixture.get("agent_stage") == "PTA":
            checks.append("gri_3b_requires_adjudication_review")

        if any(canonical_authority_class(item.get("authority_class")) == "ruling_or_precedent" for item in fixture.get("legal_authority_chain", [])):
            ruling = fixture.get("ruling_applicability", {})
            if ruling.get("binding_status") not in {"sample_bti", "binding_bti", "classification_decision"}:
                checks.append("ruling_binding_status_missing")
            if not ruling.get("product_similarity"):
                checks.append("ruling_product_similarity_missing")

        temporal = fixture.get("source_temporal_context", {})
        if fixture.get("legal_authority_chain") and not temporal.get("tariff_year"):
            checks.append("source_temporal_context_missing")

        return ValidatorResult.pass_() if not checks else ValidatorResult.review(*checks)
