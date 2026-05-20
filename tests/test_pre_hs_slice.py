from __future__ import annotations

import json
from pathlib import Path

from legal_extract_eval.pre_hs_slice import (
    RUN_REPORT_COLUMNS,
    SELECTED_COMPONENT_SLUGS,
    assert_pre_hs_purity,
    audit_runtime_paths,
    evaluate_run,
)


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def test_selected_28_component_bundle_is_clean(repo_root: Path) -> None:
    bundle = load_json(repo_root / "data" / "engineering_handoff" / "selected_28_components.json")
    components = bundle["components"]

    assert len(components) == 28
    assert [component["component_slug"] for component in components] == list(SELECTED_COMPONENT_SLUGS)
    for component in components:
        assert component["status_at_handoff"] == "pre_hs_verified_engineering_input"
        assert assert_pre_hs_purity(component) == ()


def test_source_record_manifest_covers_eu_wco_bti(repo_root: Path) -> None:
    manifest = load_json(repo_root / "data" / "source_corpus" / "source_record_manifest.json")
    entries = manifest["records"]
    source_ids = {entry["source_id"] for entry in entries}
    jurisdictions = {entry["jurisdiction"] for entry in entries}

    assert "SRC_EU_CN_2025_1926_EVS" in source_ids
    assert "SRC_EU_CN_EXPLANATORY_NOTES_EVS" in source_ids
    assert "SRC_WCO_GRI_2017" in source_ids
    assert "SRC_EU_BTI_SAMPLE" in source_ids
    assert {"EU", "WCO"}.issubset(jurisdictions)
    assert all((repo_root / entry["harness_relative_path"]).exists() for entry in entries)
    assert all((repo_root / entry["markdown_review_path"]).exists() for entry in entries)


def test_agent_specs_and_hs_slice_schemas_exist(repo_root: Path) -> None:
    for agent in ("pta", "pra", "da", "aa", "ka"):
        path = repo_root / "protocol" / "agent_specs" / f"{agent}.md"
        assert path.exists()
        assert "Paper-scope note" in path.read_text(encoding="utf-8")

    schema_dir = repo_root / "protocol" / "schemas" / "hs_slice"
    expected = {
        "StatutoryClassificationRecord.json",
        "RulingRecord.json",
        "ClassificationCandidate.json",
        "AuditReport.json",
        "RulingHandoffPackage.json",
    }
    assert expected.issubset({path.name for path in schema_dir.glob("*.json")})


def test_optional_reference_baseline_is_sealed_from_runtime(repo_root: Path) -> None:
    baseline_manifest = repo_root / "reference_baseline" / "BASELINE_MANIFEST.json"
    if baseline_manifest.exists():
        manifest = load_json(baseline_manifest)
        assert manifest["runtime_input_allowed"] is False
        assert manifest["artifact_count"] > 0

    path_audit = audit_runtime_paths(repo_root, "paper_frozen_run")
    assert path_audit.baseline_isolated


def test_paper_frozen_run_shape_and_reports(repo_root: Path) -> None:
    run_root = repo_root / "runs" / "paper_frozen_run"
    manifest = load_json(run_root / "RUN_MANIFEST.json")
    counts = manifest["artifact_counts"]

    assert manifest["component_count"] == 28
    assert manifest["reference_baseline_used_as_input"] is False
    assert counts["pta"] == 28
    assert counts["pra"] == 28
    assert counts["aa"] == 28
    assert counts["audit"] == 28
    assert counts["handoff"] == 28
    assert counts["graph_relationships"] == 28

    rows = evaluate_run(repo_root, "paper_frozen_run")
    assert len(rows) == 28
    assert all(row["actual_route"] == row["expected_route"] for row in rows)

    report_json = load_json(run_root / "reports" / "control_profile.json")
    assert len(report_json) == 28
    report_csv_header = (run_root / "reports" / "control_profile.csv").read_text(encoding="utf-8").splitlines()[0]
    assert report_csv_header.split(",") == list(RUN_REPORT_COLUMNS)


def test_run_outputs_are_eu_scope_and_comparison_only_is_non_authoritative(repo_root: Path) -> None:
    for aa_path in sorted((repo_root / "runs" / "paper_frozen_run" / "aa").glob("*.json")):
        aa = load_json(aa_path)
        assert aa["jurisdiction"] == "EU"
        assert isinstance(aa.get("comparison_only"), dict)
        assert all(
            item["source_id"].startswith(("SRC_EU", "SRC_WCO"))
            for item in aa["legal_authority_chain"]
        )
