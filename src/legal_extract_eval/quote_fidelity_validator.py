from __future__ import annotations

from pathlib import Path
from typing import Any

from .models import EXTERNAL_AUTHORITY_CLASSES, ValidatorResult


class QuoteFidelityValidator:
    def __init__(
        self,
        repo_root: Path,
        source_manifest: dict[str, Any],
        source_asset_manifest: dict[str, Any],
    ) -> None:
        self.repo_root = repo_root
        self.sources = {source["source_id"]: source for source in source_manifest["sources"]}
        self.anchors = {
            (source["source_id"], anchor["anchor_id"]): anchor
            for source in source_manifest["sources"]
            for anchor in source.get("anchors", []) or []
        }
        self.assets = {asset["asset_id"]: asset for asset in source_asset_manifest["assets"]}
        self.enabled = bool(self.assets)

    def validate(self, fixture: dict[str, Any]) -> ValidatorResult:
        if not self.enabled:
            return ValidatorResult.pass_()

        checks: list[str] = []
        quoted_refs = set(fixture.get("quoted_span_or_row_ref") or [])

        for item in fixture.get("legal_authority_chain", []):
            if item.get("authority_class") not in EXTERNAL_AUTHORITY_CLASSES:
                continue
            source_id = item.get("source_id")
            anchor_id = item.get("anchor_id")
            anchor = self.anchors.get((source_id, anchor_id))
            if anchor is None:
                checks.append("quote_anchor_unresolved")
                continue
            if anchor_id not in quoted_refs:
                checks.append("quote_anchor_not_declared_by_fixture")
            if not str(anchor.get("quoted_span", "")).strip():
                checks.append("quote_span_missing")
            if not self._has_readable_parsed_asset(source_id):
                checks.append("parsed_source_text_unavailable")

        return ValidatorResult.pass_() if not checks else ValidatorResult.fail(*checks)

    def _has_readable_parsed_asset(self, source_id: str | None) -> bool:
        if source_id is None:
            return False
        source = self.sources.get(source_id)
        if not source:
            return False
        for asset_id in source.get("parsed_asset_ids", []):
            asset = self.assets.get(asset_id)
            if not asset:
                continue
            path = self.repo_root / asset["harness_relative_path"]
            if path.exists() and path.stat().st_size > 0:
                return True
        return False
