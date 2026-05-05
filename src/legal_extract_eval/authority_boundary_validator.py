from __future__ import annotations

from typing import Any

from .models import EXTERNAL_AUTHORITY_CLASSES, INTERNAL_AUTHORITY_CLASSES, PAPER_SCOPE_JURISDICTIONS, ValidatorResult


class AuthorityBoundaryValidator:
    def __init__(self, source_manifest: dict[str, Any]) -> None:
        self.sources = {source["source_id"]: source for source in source_manifest["sources"]}

    def validate(self, fixture: dict[str, Any]) -> ValidatorResult:
        checks: list[str] = []
        for item in fixture.get("legal_authority_chain", []):
            authority_class = item.get("authority_class")
            source_id = item.get("source_id")
            source = self.sources.get(source_id)
            if authority_class in INTERNAL_AUTHORITY_CLASSES:
                checks.append("internal_source_as_authority")
            if authority_class not in EXTERNAL_AUTHORITY_CLASSES and authority_class not in INTERNAL_AUTHORITY_CLASSES:
                checks.append("unknown_authority_class")
            if source and source.get("jurisdiction") not in PAPER_SCOPE_JURISDICTIONS and source.get("jurisdiction") != "internal":
                checks.append("non_paper_scope_authority_used")

        return ValidatorResult.pass_() if not checks else ValidatorResult.fail(*checks)

    @staticmethod
    def authority_classes(fixture: dict[str, Any]) -> set[str]:
        return {
            item.get("authority_class")
            for item in fixture.get("legal_authority_chain", [])
            if item.get("authority_class") in EXTERNAL_AUTHORITY_CLASSES
        }

    @staticmethod
    def source_anchors(fixture: dict[str, Any]) -> set[str]:
        return {
            item.get("anchor_id")
            for item in fixture.get("legal_authority_chain", [])
            if item.get("anchor_id")
        }
