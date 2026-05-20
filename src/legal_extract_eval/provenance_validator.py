from __future__ import annotations

from typing import Any

from .models import EXTERNAL_AUTHORITY_CLASSES, INTERNAL_AUTHORITY_CLASSES, ValidatorResult
from .source_authority_registry import canonical_authority_class


class ProvenanceValidator:
    def __init__(self, source_manifest: dict[str, Any]) -> None:
        self.sources = {source["source_id"]: source for source in source_manifest["sources"]}
        self.anchors = {
            (source["source_id"], anchor["anchor_id"]): anchor
            for source in source_manifest["sources"]
            for anchor in source.get("anchors", [])
        }

    def validate(self, fixture: dict[str, Any]) -> ValidatorResult:
        checks: list[str] = []
        chain = fixture.get("legal_authority_chain", [])

        if fixture.get("legal_proposition") and not chain:
            checks.append("missing_external_authority")
            checks.append("missing_source_anchor")

        external_count = 0
        for item in chain:
            source_id = item.get("source_id")
            authority_class = canonical_authority_class(item.get("authority_class"))
            anchor_id = item.get("anchor_id")
            if authority_class in INTERNAL_AUTHORITY_CLASSES:
                checks.append("internal_source_as_authority")
                continue
            if authority_class in EXTERNAL_AUTHORITY_CLASSES:
                external_count += 1
            if source_id not in self.sources:
                checks.append("source_id_unresolved")
                continue
            if not anchor_id:
                checks.append("missing_source_anchor")
                continue
            anchor = self.anchors.get((source_id, anchor_id))
            if anchor is None:
                checks.append("source_anchor_not_resolved")
            elif anchor.get("document_level_only") is True:
                checks.append("document_level_only_source_anchor")

        if chain and external_count == 0:
            checks.append("missing_external_authority")

        if fixture.get("legal_proposition") and not fixture.get("quoted_span_or_row_ref"):
            checks.append("missing_source_anchor")

        return ValidatorResult.pass_() if not checks else ValidatorResult.fail(*checks)
