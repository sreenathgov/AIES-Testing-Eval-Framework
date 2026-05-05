from __future__ import annotations

from pathlib import Path
from typing import Any

from .models import INTERNAL_AUTHORITY_CLASSES, ValidatorResult


class SourceIntegrityValidator:
    def __init__(
        self,
        repo_root: Path,
        source_asset_manifest: dict[str, Any],
        forensic_manifest: dict[str, Any],
        lineage_map: list[dict[str, Any]],
    ) -> None:
        self.repo_root = repo_root
        self.source_assets = {asset["asset_id"]: asset for asset in source_asset_manifest["assets"]}
        self.forensic_assets = {
            artifact["forensic_artifact_id"]: artifact for artifact in forensic_manifest["artifacts"]
        }
        self.lineage = {entry["fixture_id"]: entry for entry in lineage_map}
        self.enabled = bool(self.source_assets or self.forensic_assets or self.lineage)

    def validate(self, fixture: dict[str, Any]) -> ValidatorResult:
        if not self.enabled:
            return ValidatorResult.pass_()

        checks: list[str] = []
        artifact_id = fixture["artifact_id"]
        chain = fixture.get("legal_authority_chain", [])
        internal_only = bool(chain) and all(
            item.get("authority_class") in INTERNAL_AUTHORITY_CLASSES for item in chain
        )

        if artifact_id not in self.lineage:
            checks.append("fixture_lineage_missing")

        if not internal_only and fixture.get("legal_authority_chain"):
            if not fixture.get("source_asset_ids"):
                checks.append("source_assets_missing")
            if not fixture.get("parsed_asset_ids"):
                checks.append("parsed_assets_missing")

        for asset_id in fixture.get("source_asset_ids", []):
            self._check_source_asset(asset_id, checks)
        for asset_id in fixture.get("parsed_asset_ids", []):
            self._check_source_asset(asset_id, checks)
        for artifact_id in fixture.get("forensic_artifact_ids", []):
            artifact = self.forensic_assets.get(artifact_id)
            if artifact is None:
                checks.append("forensic_artifact_unresolved")
            elif artifact.get("legal_authority_role") != "artifact_origin_only":
                checks.append("forensic_artifact_marked_as_authority")

        return ValidatorResult.pass_() if not checks else ValidatorResult.fail(*checks)

    def _check_source_asset(self, asset_id: str, checks: list[str]) -> None:
        asset = self.source_assets.get(asset_id)
        if asset is None:
            checks.append("source_asset_unresolved")
            return
        path = self.repo_root / asset["harness_relative_path"]
        if not path.exists():
            checks.append("source_asset_file_missing")
        if len(str(asset.get("sha256", ""))) != 64:
            checks.append("source_asset_hash_invalid")
        if int(asset.get("byte_size", 0)) <= 0:
            checks.append("source_asset_empty")
