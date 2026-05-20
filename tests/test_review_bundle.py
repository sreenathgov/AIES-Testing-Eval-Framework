from __future__ import annotations

import hashlib
import json
from pathlib import Path


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def test_source_bundle_resolves_for_every_external_source(repo_root: Path) -> None:
    source_manifest = json.loads((repo_root / "data/fixtures/source_manifest.json").read_text())
    asset_manifest = json.loads((repo_root / "data/source_corpus/SOURCE_ASSET_MANIFEST.json").read_text())
    asset_by_id = {asset["asset_id"]: asset for asset in asset_manifest["assets"]}

    for source in source_manifest["sources"]:
        if source["authority_class"] == "internal_generated_candidate":
            assert source.get("source_asset_ids", []) == []
            assert source.get("parsed_asset_ids", []) == []
            continue

        assert source["source_asset_ids"], source["source_id"]
        assert source["parsed_asset_ids"], source["source_id"]
        for asset_id in source["source_asset_ids"] + source["parsed_asset_ids"]:
            asset = asset_by_id[asset_id]
            path = repo_root / asset["harness_relative_path"]
            assert path.exists(), asset_id
            assert source["source_id"] in asset["source_id_links"]


def test_source_and_forensic_hash_integrity(repo_root: Path) -> None:
    source_manifest = json.loads((repo_root / "data/source_corpus/SOURCE_ASSET_MANIFEST.json").read_text())
    forensic_manifest = json.loads((repo_root / "data/forensic_evidence/FORENSIC_EXPORT_MANIFEST.json").read_text())

    source_assets = [
        (asset["asset_id"], asset["harness_relative_path"], asset["sha256"], asset["byte_size"])
        for asset in source_manifest["assets"]
    ]
    forensic_assets = [
        (
            asset["forensic_artifact_id"],
            asset["sanitized_destination_path"],
            asset["sha256"],
            asset["byte_size"],
        )
        for asset in forensic_manifest["artifacts"]
    ]

    for asset_id, relative_path, expected_hash, expected_size in source_assets + forensic_assets:
        path = repo_root / relative_path
        assert path.exists(), asset_id
        assert path.stat().st_size == expected_size
        assert _sha256(path) == expected_hash
        assert len(expected_hash) == 64


def test_fixture_lineage_map_covers_all_fixtures(repo_root: Path, fixtures: list[dict]) -> None:
    lineage = json.loads((repo_root / "data/fixtures/FIXTURE_LINEAGE_MAP.json").read_text())
    lineage_by_id = {entry["fixture_id"]: entry for entry in lineage}

    assert set(lineage_by_id) == {fixture["artifact_id"] for fixture in fixtures}
    for fixture in fixtures:
        entry = lineage_by_id[fixture["artifact_id"]]
        assert entry["gold_case_id"] == fixture["scenario_id"]
        assert entry["fixture_class"] == fixture["fixture_class"]
        assert entry["graph_nodes"] == fixture["graph_nodes"]
        assert entry["graph_edges"] == fixture["graph_edges"]
        assert entry["forensic_origin_artifact_ids"] == fixture["forensic_artifact_ids"]


def test_fixtures_link_assets_without_treating_internal_origin_as_authority(fixtures: list[dict]) -> None:
    for fixture in fixtures:
        intentionally_absent = "source_linkage_intentionally_absent" in fixture.get("known_issue_tags", [])
        internal_only = all(
            item.get("authority_class") == "internal_generated_candidate"
            for item in fixture.get("legal_authority_chain", [])
        )

        if not intentionally_absent and not internal_only:
            assert fixture["source_asset_ids"], fixture["artifact_id"]
            assert fixture["parsed_asset_ids"], fixture["artifact_id"]

        assert fixture["forensic_artifact_ids"], fixture["artifact_id"]
        legal_source_ids = {item.get("source_id") for item in fixture.get("legal_authority_chain", [])}
        assert not (legal_source_ids & set(fixture["forensic_artifact_ids"]))


def test_forensic_artifacts_are_origin_only(repo_root: Path) -> None:
    forensic_manifest = json.loads((repo_root / "data/forensic_evidence/FORENSIC_EXPORT_MANIFEST.json").read_text())

    assert forensic_manifest["legal_authority_rule"].startswith("forensic artifacts evidence origin only")
    for artifact in forensic_manifest["artifacts"]:
        assert artifact["legal_authority_role"] == "artifact_origin_only"
        assert artifact["linked_fixture_ids"]


def test_scope_rule_remains_eu_wco_bti_only(repo_root: Path, fixtures: list[dict]) -> None:
    source_manifest = json.loads((repo_root / "data/fixtures/source_manifest.json").read_text())
    jurisdiction_by_source = {source["source_id"]: source["jurisdiction"] for source in source_manifest["sources"]}

    for fixture in fixtures:
        for item in fixture.get("legal_authority_chain", []):
            jurisdiction = jurisdiction_by_source[item["source_id"]]
            assert jurisdiction in {"EU", "WCO", "internal"}

        comparison_only = fixture.get("comparison_only", {})
        assert all(key in {"US", "IN"} for key in comparison_only)


def test_export_script_is_copy_only_and_harness_bounded(repo_root: Path) -> None:
    script = (repo_root / "scripts/build_review_bundle.py").read_text()
    forbidden_calls = ("shutil.move", "Path.rename", "Path.unlink", "shutil.rmtree", "os.remove", "os.unlink")
    for call in forbidden_calls:
        assert call not in script
    assert "shutil.copy2" in script

    source_manifest = json.loads((repo_root / "data/source_corpus/SOURCE_ASSET_MANIFEST.json").read_text())
    for asset in source_manifest["assets"]:
        assert not asset["harness_relative_path"].startswith("/")
        assert asset["source_repo_relative_path"].startswith("source_repo/")
