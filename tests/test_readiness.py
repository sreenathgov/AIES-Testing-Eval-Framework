from __future__ import annotations

import json
import hashlib
from copy import deepcopy
from pathlib import Path

from legal_extract_eval.readiness import _check_run_graph_schema, _check_source_authority_consistency, _check_source_bundle, run_readiness_check
from legal_extract_eval.source_authority_registry import (
    canonical_authority_class,
    concrete_source_ids,
    registry_mismatches_for_record_manifest_entry,
    registry_mismatches_for_source,
)


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def test_readiness_preflight_reports_ready_without_generating_run(repo_root: Path) -> None:
    before = {path.relative_to(repo_root): path.stat().st_mtime_ns for path in (repo_root / "runs").glob("*/*")}

    report = run_readiness_check(repo_root)

    after = {path.relative_to(repo_root): path.stat().st_mtime_ns for path in (repo_root / "runs").glob("*/*")}
    assert report.status == "ready"
    assert report.blocker_count == 0
    assert before == after


def test_source_authority_registry_accepts_legacy_bti_alias(source_manifest: dict) -> None:
    source = next(item for item in source_manifest["sources"] if item["source_id"] == "SRC_EU_BTI_SAMPLE")

    assert source["authority_class"] == "classification_decision"
    assert canonical_authority_class(source["authority_class"]) == "ruling_or_precedent"
    assert registry_mismatches_for_source(source) == ()


def test_source_authority_registry_maps_grouped_wco_aliases() -> None:
    assert concrete_source_ids("SRC_WCO_SECTION_XVI") == (
        "SRC_WCO_SECTION_84",
        "SRC_WCO_SECTION_85",
        "SRC_WCO_SECTION_90",
    )
    assert concrete_source_ids("SRC_WCO_SECTION_XVII") == ("SRC_WCO_SECTION_87",)


def test_source_record_manifest_uses_concrete_registered_sources(repo_root: Path) -> None:
    manifest = load_json(repo_root / "data/source_corpus/source_record_manifest.json")

    for entry in manifest["records"]:
        assert registry_mismatches_for_record_manifest_entry(entry) == (), entry["source_id"]


def test_readiness_detects_unregistered_fixture_source(source_manifest: dict) -> None:
    source = deepcopy(source_manifest["sources"][0])
    source["source_id"] = "SRC_UNREGISTERED"

    assert registry_mismatches_for_source(source) == ("source_id_not_registered",)


def test_knowledge_evidence_registry_covers_all_metric_ids(repo_root: Path) -> None:
    framework = load_json(repo_root / "protocol/measurement_framework.json")
    registry = load_json(repo_root / "protocol/knowledge_evidence_registry.json")

    metric_ids = {metric["metric_id"] for metric in framework["metrics"]}
    registry_ids = {entry["metric_id"] for entry in registry["entries"]}

    assert registry_ids == metric_ids
    for entry in registry["entries"]:
        assert entry["paper_section"]
        assert entry["control_family"]
        assert entry["legal_rationale"]
        assert entry["supporting_source"]
        assert entry["evidence_status"]


def test_existing_run_graph_artifacts_match_graph_schemas(repo_root: Path) -> None:
    graph_root = repo_root / "runs" / "paper_frozen_run" / "graph"
    node_ids = set()

    for node_path in (graph_root / "entities").glob("*.json"):
        node = load_json(node_path)
        assert node["node_id"]
        node_ids.add(node["node_id"])
        assert node["node_type"] in {
            "product_component",
            "engineering_identity_record",
            "classification_candidate",
            "statutory_classification_record",
            "ruling_record",
            "audit_report",
            "handoff_package",
            "hs_code",
            "source",
            "legal_proposition",
            "artifact_origin",
            "comparison_metadata",
        }
    for edge_path in (graph_root / "relationships").glob("*.json"):
        edge = load_json(edge_path)
        assert edge["edge_type"] == "proposes_code"
        assert edge["source_node_id"].startswith("AA_EU_")
        assert edge["target_node_id"].startswith("hs_code:")
        assert edge["source_node_id"] in node_ids
        assert edge["target_node_id"] in node_ids


def test_readiness_detects_unresolved_graph_edge_endpoint(tmp_path: Path) -> None:
    graph_root = tmp_path / "runs" / "demo" / "graph"
    (graph_root / "entities").mkdir(parents=True)
    (graph_root / "relationships").mkdir()
    (graph_root / "entities" / "candidate.json").write_text(
        json.dumps({"node_id": "AA_EU_demo", "node_type": "classification_candidate"}),
        encoding="utf-8",
    )
    (graph_root / "relationships" / "bad_edge.json").write_text(
        json.dumps(
            {
                "edge_id": "edge:demo",
                "edge_type": "proposes_code",
                "source_node_id": "AA_EU_demo",
                "target_node_id": "hs_code:missing:EU",
            }
        ),
        encoding="utf-8",
    )

    issues = []
    _check_run_graph_schema(tmp_path, "demo", issues)

    assert any(issue.code == "graph_edge_endpoint_unresolved" for issue in issues)


def test_readiness_detects_source_record_hash_mismatch(tmp_path: Path) -> None:
    source_root = tmp_path / "data" / "source_corpus"
    records_root = source_root / "records" / "eu"
    records_root.mkdir(parents=True)
    asset_path = source_root / "asset.json"
    record_path = records_root / "records.json"
    qc_path = records_root / "qc.json"
    asset_path.write_text("{}", encoding="utf-8")
    record_path.write_text("[]", encoding="utf-8")
    qc_path.write_text(json.dumps({"record_count": 0}), encoding="utf-8")
    good_asset_hash = hashlib.sha256(asset_path.read_bytes()).hexdigest()
    (source_root / "SOURCE_ASSET_MANIFEST.json").write_text(
        json.dumps(
            {
                "assets": [
                    {
                        "harness_relative_path": "data/source_corpus/asset.json",
                        "sha256": good_asset_hash,
                        "byte_size": asset_path.stat().st_size,
                        "source_id_links": ["SRC_EU_CN_2025_1926_EVS"],
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    (source_root / "SOURCE_RECORD_PROFILE_MANIFEST.json").write_text(
        json.dumps(
            {
                "profiles": [
                    {
                        "original_path": "data/source_corpus/asset.json",
                        "parsed_json_path": "data/source_corpus/asset.json",
                        "normalized_json_path": "data/source_corpus/asset.json",
                    }
                ],
                "compiled_outputs": [
                    {
                        "records_path": "data/source_corpus/records/eu/records.json",
                        "records_markdown_path": "data/source_corpus/records/eu/records.json",
                        "qc_path": "data/source_corpus/records/eu/qc.json",
                        "layout_profile_path": "data/source_corpus/records/eu/records.json",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    (source_root / "source_record_manifest.json").write_text(
        json.dumps(
            {
                "records": [
                    {
                        "harness_relative_path": "data/source_corpus/records/eu/records.json",
                        "sha256": "bad_hash",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )

    issues = []
    _check_source_bundle(tmp_path, issues)

    assert any(issue.code == "source_record_manifest_hash_mismatch" for issue in issues)


def test_readiness_detects_unresolved_source_alias_records(tmp_path: Path) -> None:
    fixtures_root = tmp_path / "data" / "fixtures"
    source_root = tmp_path / "data" / "source_corpus"
    fixtures_root.mkdir(parents=True)
    source_root.mkdir(parents=True)
    (fixtures_root / "source_manifest.json").write_text(
        json.dumps(
            {
                "sources": [
                    {
                        "source_id": "SRC_WCO_SECTION_XVI",
                        "authority_class": "interpretive_legal_note",
                        "jurisdiction": "WCO",
                        "anchors": [{"anchor_id": "WCO_SECTION_XVI_NOTE_3"}],
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    (source_root / "source_record_manifest.json").write_text(json.dumps({"records": []}), encoding="utf-8")

    issues = []
    _check_source_authority_consistency(tmp_path, issues)

    assert any(issue.code == "source_anchor_record_unresolved" for issue in issues)
