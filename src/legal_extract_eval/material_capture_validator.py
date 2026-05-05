from __future__ import annotations

from typing import Any

from .models import ValidatorResult


class MaterialCaptureValidator:
    def validate(self, fixture: dict[str, Any]) -> ValidatorResult:
        checks: list[str] = []

        if not fixture.get("material_legal_propositions"):
            checks.append("material_legal_propositions_missing")

        required_anchors = set(fixture.get("required_source_anchors", []))
        declared_anchors = set(fixture.get("quoted_span_or_row_ref") or [])
        if not required_anchors.issubset(declared_anchors):
            checks.append("required_source_anchor_not_captured")

        required_gri = set(fixture.get("required_gri_path_elements", []))
        actual_gri = set(fixture.get("gri_path", []))
        if not required_gri.issubset(actual_gri):
            checks.append("required_gri_path_element_missing")

        candidate_code = fixture.get("candidate_cn_code") or fixture.get("candidate_hs_code") or ""
        if candidate_code.count(".") >= 2 and "GRI_6" not in actual_gri:
            checks.append("gri_6_missing_for_subheading_claim")

        if "critical_omission" in fixture.get("known_issue_tags", []):
            checks.append("capture_gap_requires_review")

        if not fixture.get("exclusion_or_note_checks") and fixture.get("fixture_class") == "good":
            checks.append("exclusion_or_note_check_missing")

        return ValidatorResult.pass_() if not checks else ValidatorResult.review(*checks)
