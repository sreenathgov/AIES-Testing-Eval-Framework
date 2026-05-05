from __future__ import annotations

import json
from pathlib import Path

from legal_extract_eval.source_compilers import SOURCE_PROFILES


def _load(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def test_source_record_profile_manifest_is_complete(repo_root: Path) -> None:
    manifest = _load(repo_root / "data/source_corpus/SOURCE_RECORD_PROFILE_MANIFEST.json")

    assert len(manifest["profiles"]) == 8
    assert len(manifest["compiled_outputs"]) == 8
    assert {profile.source_id for profile in SOURCE_PROFILES} == {
        output["source_id"] for output in manifest["compiled_outputs"]
    }
    assert {profile.compiler_profile for profile in SOURCE_PROFILES} == {
        "eu_cn_tariff_table",
        "eu_cn_explanatory_notes_layout",
        "bti_csv_rows",
        "wco_gri_rules",
        "wco_heading_table",
    }


def test_every_compiler_emits_json_markdown_qc_and_layout_profile(repo_root: Path) -> None:
    manifest = _load(repo_root / "data/source_corpus/SOURCE_RECORD_PROFILE_MANIFEST.json")

    for output in manifest["compiled_outputs"]:
        records_path = repo_root / output["records_path"]
        markdown_path = repo_root / output["records_markdown_path"]
        qc_path = repo_root / output["qc_path"]
        layout_profile_path = repo_root / output["layout_profile_path"]

        assert records_path.exists(), records_path
        assert markdown_path.exists(), markdown_path
        assert qc_path.exists(), qc_path
        assert layout_profile_path.exists(), layout_profile_path

        records = _load(records_path)
        markdown = markdown_path.read_text(encoding="utf-8")
        qc = _load(qc_path)
        layout_profile = _load(layout_profile_path)

        assert records
        assert qc["record_count"] == len(records)
        assert "generic" not in output["compiler_profile"]
        assert "Layout-aware legal source layer" in markdown
        assert records[0]["record_id"] in markdown
        assert layout_profile["inferred_layout_type"]
        for record in records:
            assert record.get("source_id")
            assert record.get("authority_class")
            assert record.get("source_locator") or record.get("source_bbox"), record["record_id"]


def test_eu_cn_explanatory_note_range_is_not_flattened(repo_root: Path) -> None:
    records = _load(repo_root / "data/source_corpus/records/eu/eu_cn_explanatory_notes_evs_records.json")
    record = next(item for item in records if item["record_id"] == "EU_CN_EN_8411_11_00_TO_8411_12_80")

    assert record["code_range"] == {"start": "8411 11 00", "end": "8411 12 80", "connector": "to"}
    assert record["heading_code"] == "8411"
    assert record["legal_anchor"] == "8411 11 00 to 8411 12 80"
    assert "after-burning auxiliary appliances" in record["note_text"]


def test_wco_gri_rules_are_segmented_into_legal_rule_records(repo_root: Path) -> None:
    records = _load(repo_root / "data/source_corpus/records/wco/wco_gri_rules_2017_records.json")
    rule_ids = {record["rule_id"] for record in records}

    assert rule_ids == {"GRI_1", "GRI_2A", "GRI_2B", "GRI_3A", "GRI_3B", "GRI_3C", "GRI_4", "GRI_5A", "GRI_5B", "GRI_6"}
    assert next(record for record in records if record["rule_id"] == "GRI_3A")["parent_rule_intro"].startswith(
        "3. When by application"
    )
    assert _load(repo_root / "data/source_corpus/records/wco/wco_gri_rules_2017_qc.json")["missing_expected_rules"] == []


def test_wco_heading_table_preserves_code_hierarchy_and_flags_ambiguous_rows(repo_root: Path) -> None:
    section_85 = _load(repo_root / "data/source_corpus/records/wco/wco_2022_section_85_complex_records.json")
    static_converters = next(record for record in section_85 if record.get("code") == "850440")
    lithium_ion = next(record for record in section_85 if record.get("code") == "850760")
    chapter_note = next(record for record in section_85 if record["legal_anchor"] == "Chapter 85 Note 3")

    assert chapter_note["record_type"] == "chapter_note"
    assert "electric accumulators" in chapter_note["description"]
    assert static_converters["heading_code"] == "8504"
    assert static_converters["parent_record_id"]
    assert static_converters["source_locator"]["table_id"]
    assert lithium_ion["description"] == "- Lithium-ion"

    section_87_qc = _load(repo_root / "data/source_corpus/records/wco/wco_2022_section_87_complex_qc.json")
    assert section_87_qc["review_flag_counts"]["heading_and_subheading_same_row_requires_review"] >= 1


def test_bti_csv_rows_preserve_row_identity_dates_and_justification(repo_root: Path) -> None:
    records = _load(repo_root / "data/source_corpus/records/bti/ebti_sample_targeted_test_run_records.json")
    first = records[0]

    assert len(records) == 30
    assert first["bti_reference"] == "DEBTI58842/24-1"
    assert first["source_locator"] == {"csv_row_number": 2, "row_id": "DEBTI58842/24-1"}
    assert first["validity"]["date_of_issue"] == "05/03/2025"
    assert "AV 1" in first["classification_justification"]


def test_eu_cn_tariff_records_flag_unsafe_continuation_merges(repo_root: Path) -> None:
    records = _load(repo_root / "data/source_corpus/records/eu/eu_cn_2025_1926_evs_records.json")
    qc = _load(repo_root / "data/source_corpus/records/eu/eu_cn_2025_1926_evs_qc.json")

    assert any(record["code"] == "84072110" for record in records)
    assert qc["review_flag_counts"]["description_continuation_merged"] > 0
    assert qc["review_flag_counts"]["source_normalizer_requires_review"] > 0
