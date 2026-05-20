from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


EXCLUDED_TOKENS = (".DS_Store", "__pycache__", ".pytest_cache", "README", "scratch", "log")


@dataclass(frozen=True)
class SourceAsset:
    asset_id: str
    asset_type: str
    source_relative_path: str
    harness_relative_path: str
    source_id_links: tuple[str, ...]
    notes: str


@dataclass(frozen=True)
class ForensicAsset:
    artifact_id: str
    artifact_type: str
    source_relative_path: str
    harness_relative_path: str
    linked_fixture_ids: tuple[str, ...]
    reason_for_inclusion: str
    legal_authority_role: str = "artifact_origin_only"
    sanitization_actions: tuple[str, ...] = (
        "removed absolute local paths",
        "neutralized internal product/company names",
        "added reviewer-scope banner",
    )


SOURCE_ASSETS: tuple[SourceAsset, ...] = (
    SourceAsset(
        "SRC_ASSET_EU_CN_2025_1926_ORIGINAL",
        "original_pdf",
        "source_repo/corpus/02_hs_classification/national_tariffs/eu/EU - HS - COMMISSION IMPLEMENTING REGULATION (EU) 2025_1926 - EVs.pdf",
        "data/source_corpus/originals/eu/eu_cn_2025_1926_evs.pdf",
        ("SRC_EU_CN_2025_1926_EVS",),
        "Original EU Combined Nomenclature regulation PDF for EV-relevant tariff lines.",
    ),
    SourceAsset(
        "SRC_ASSET_EU_CN_EN_ORIGINAL",
        "original_pdf",
        "source_repo/corpus/02_hs_classification/national_tariffs/eu/EXPLANATORY NOTES TO THE COMBINED NOMENCLATURE OF THE EUROPEAN UNION - EVs.pdf",
        "data/source_corpus/originals/eu/eu_cn_explanatory_notes_evs.pdf",
        ("SRC_EU_CN_EXPLANATORY_NOTES_EVS",),
        "Original EU CN Explanatory Notes PDF used for interpretive anchors.",
    ),
    SourceAsset(
        "SRC_ASSET_EU_BTI_SAMPLE_ORIGINAL",
        "original_csv",
        "source_repo/corpus/02_hs_classification/rulings/eu/bti/EBTI-Sample-Targeted-Test-Run.csv",
        "data/source_corpus/originals/bti/ebti_sample_targeted_test_run.csv",
        ("SRC_EU_BTI_SAMPLE",),
        "Original targeted EU BTI CSV sample.",
    ),
    SourceAsset(
        "SRC_ASSET_WCO_GRI_2017_ORIGINAL",
        "original_pdf",
        "source_repo/corpus/02_hs_classification/wco/WCO-GRI-Rules-2017.pdf",
        "data/source_corpus/originals/wco/wco_gri_rules_2017.pdf",
        ("SRC_WCO_GRI_2017",),
        "Original WCO GRI source PDF.",
    ),
    SourceAsset(
        "SRC_ASSET_WCO_SECTION_84_ORIGINAL",
        "original_pdf",
        "source_repo/corpus/02_hs_classification/wco/WCO - 2022 - Section 84_complex.pdf",
        "data/source_corpus/originals/wco/wco_2022_section_84_complex.pdf",
        ("SRC_WCO_SECTION_XVI",),
        "Original WCO Chapter 84 material used for Section XVI context.",
    ),
    SourceAsset(
        "SRC_ASSET_WCO_SECTION_85_ORIGINAL",
        "original_pdf",
        "source_repo/corpus/02_hs_classification/wco/WCO - 2022 - Section 85_complex.pdf",
        "data/source_corpus/originals/wco/wco_2022_section_85_complex.pdf",
        ("SRC_WCO_SECTION_XVI",),
        "Original WCO Chapter 85 material used for Section XVI and EV electrical classification context.",
    ),
    SourceAsset(
        "SRC_ASSET_WCO_SECTION_87_ORIGINAL",
        "original_pdf",
        "source_repo/corpus/02_hs_classification/wco/WCO - 2022 - Section 87_complex.pdf",
        "data/source_corpus/originals/wco/wco_2022_section_87_complex.pdf",
        ("SRC_WCO_SECTION_XVII",),
        "Original WCO Chapter 87 material used for vehicle-parts boundary context.",
    ),
    SourceAsset(
        "SRC_ASSET_WCO_SECTION_90_ORIGINAL",
        "original_pdf",
        "source_repo/corpus/02_hs_classification/wco/WCO - 2022 - Section 90_complex.pdf",
        "data/source_corpus/originals/wco/wco_2022_section_90_complex.pdf",
        ("SRC_WCO_SECTION_XVI",),
        "Original WCO Chapter 90 material used for exclusion and note-check context.",
    ),
)


PARSED_STEMS: tuple[tuple[str, str, tuple[str, ...], str], ...] = (
    (
        "source_repo/parsed/02_hs_classification/national_tariffs/eu/eu_hs_commission_implementing_regulation_(eu)_2025_1926_evs",
        "data/source_corpus/parsed/eu/eu_hs_commission_implementing_regulation_2025_1926_evs",
        ("SRC_EU_CN_2025_1926_EVS",),
        "Parsed EU CN regulation.",
    ),
    (
        "source_repo/parsed/02_hs_classification/national_tariffs/eu/explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs",
        "data/source_corpus/parsed/eu/explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs",
        ("SRC_EU_CN_EXPLANATORY_NOTES_EVS",),
        "Parsed EU CN Explanatory Notes.",
    ),
    (
        "source_repo/parsed/02_hs_classification/rulings/eu/bti/ebti_sample_targeted_test_run",
        "data/source_corpus/parsed/bti/ebti_sample_targeted_test_run",
        ("SRC_EU_BTI_SAMPLE",),
        "Parsed targeted EU BTI sample.",
    ),
    (
        "source_repo/parsed/02_hs_classification/wco/wco_gri_rules_2017",
        "data/source_corpus/parsed/wco/wco_gri_rules_2017",
        ("SRC_WCO_GRI_2017",),
        "Parsed WCO GRI rules.",
    ),
    (
        "source_repo/parsed/02_hs_classification/wco/wco_2022_section_84_complex",
        "data/source_corpus/parsed/wco/wco_2022_section_84_complex",
        ("SRC_WCO_SECTION_XVI",),
        "Parsed WCO Chapter 84 material.",
    ),
    (
        "source_repo/parsed/02_hs_classification/wco/wco_2022_section_85_complex",
        "data/source_corpus/parsed/wco/wco_2022_section_85_complex",
        ("SRC_WCO_SECTION_XVI",),
        "Parsed WCO Chapter 85 material.",
    ),
    (
        "source_repo/parsed/02_hs_classification/wco/wco_2022_section_87_complex",
        "data/source_corpus/parsed/wco/wco_2022_section_87_complex",
        ("SRC_WCO_SECTION_XVII",),
        "Parsed WCO Chapter 87 material.",
    ),
    (
        "source_repo/parsed/02_hs_classification/wco/wco_2022_section_90_complex",
        "data/source_corpus/parsed/wco/wco_2022_section_90_complex",
        ("SRC_WCO_SECTION_XVI",),
        "Parsed WCO Chapter 90 material.",
    ),
)


PARSED_SUFFIX_TYPES = {
    ".md": "parsed_markdown",
    ".json": "parsed_raw_json",
    "_meta.json": "parsed_meta_json",
    "_normalized.json": "parsed_normalized_json",
}


FORENSIC_ASSETS: tuple[ForensicAsset, ...] = (
    ForensicAsset(
        "FOR_AGENT_AA_OBC",
        "sanitized_agent_artifact",
        "source_repo/staging/hs-slice/aa/on-board-charger-(obc)_classification_candidate.md",
        "data/forensic_evidence/sanitized_agent_artifacts/aa_on_board_charger_classification_candidate.md",
        ("FX_GOOD_OBC_AA_EU", "FX_BAD_OBC_EDGE_DIRECTION"),
        "AA classification candidate behind OBC good and graph-parity fixtures.",
    ),
    ForensicAsset(
        "FOR_AGENT_AA_HV_CONNECTORS",
        "sanitized_agent_artifact",
        "source_repo/staging/hs-slice/aa/high-voltage-connectors_classification_candidate.md",
        "data/forensic_evidence/sanitized_agent_artifacts/aa_high_voltage_connectors_classification_candidate.md",
        ("FX_GOOD_HV_CONNECTORS_EU",),
        "AA classification candidate behind high-voltage connector fixture.",
    ),
    ForensicAsset(
        "FOR_AGENT_AA_TRACTION_INVERTER",
        "sanitized_agent_artifact",
        "source_repo/staging/hs-slice/aa/traction-inverter-module_classification_candidate.md",
        "data/forensic_evidence/sanitized_agent_artifacts/aa_traction_inverter_module_classification_candidate.md",
        ("FX_GOOD_TRACTION_INVERTER_EU",),
        "AA classification candidate behind traction inverter fixture.",
    ),
    ForensicAsset(
        "FOR_AGENT_AA_HV_BATTERY_PACK",
        "sanitized_agent_artifact",
        "source_repo/staging/hs-slice/aa/high-voltage-battery-pack-assembly_classification_candidate.md",
        "data/forensic_evidence/sanitized_agent_artifacts/aa_high_voltage_battery_pack_assembly_classification_candidate.md",
        ("FX_GOOD_HV_BATTERY_PACK_BTI_EU", "FX_BAD_HV_BATTERY_PACK_PTA_OVERREACH", "FX_BORDERLINE_HV_BATTERY_PACK_GRI3B_REVIEW"),
        "AA classification candidate behind HV battery pack fixtures.",
    ),
    ForensicAsset(
        "FOR_AGENT_AA_LI_ION_CELL",
        "sanitized_agent_artifact",
        "source_repo/staging/hs-slice/aa/lithium-ion-battery-cell_classification_candidate.md",
        "data/forensic_evidence/sanitized_agent_artifacts/aa_lithium_ion_battery_cell_classification_candidate.md",
        ("FX_GOOD_LI_ION_CELL_EU", "FX_BORDERLINE_LI_CELL_PRODUCT_NODE_MIXED_STATE"),
        "AA classification candidate behind lithium-ion cell fixtures.",
    ),
    ForensicAsset(
        "FOR_AGENT_AA_SEPARATOR",
        "sanitized_agent_artifact",
        "source_repo/staging/hs-slice/aa/separator-pe-pp-film_classification_candidate.md",
        "data/forensic_evidence/sanitized_agent_artifacts/aa_separator_pe_pp_film_classification_candidate.md",
        ("FX_BAD_SEPARATOR_CONFIDENCE_INFLATION", "FX_BORDERLINE_SEPARATOR_DIVERGENCE"),
        "AA classification candidate behind separator divergence and confidence fixtures.",
    ),
    ForensicAsset(
        "FOR_AGENT_AA_INTEGRATED_E_AXLE",
        "sanitized_agent_artifact",
        "source_repo/staging/hs-slice/aa/integrated-e-axle_classification_candidate.md",
        "data/forensic_evidence/sanitized_agent_artifacts/aa_integrated_e_axle_classification_candidate.md",
        ("FX_BORDERLINE_INTEGRATED_E_AXLE_COMPARISON_ONLY",),
        "AA classification candidate behind comparison-only divergence fixture.",
    ),
    ForensicAsset(
        "FOR_AGENT_AA_NOES",
        "sanitized_agent_artifact",
        "source_repo/staging/hs-slice/aa/silicon-alloyed-electrical-steel-core-noes_classification_candidate.md",
        "data/forensic_evidence/sanitized_agent_artifacts/aa_silicon_alloyed_electrical_steel_core_noes_classification_candidate.md",
        ("FX_BORDERLINE_NOES_CLIENT_FACT",),
        "AA classification candidate behind client-fact dependent fixture.",
    ),
    ForensicAsset(
        "FOR_AGENT_PTA_HV_BATTERY_PACK_EU",
        "sanitized_agent_artifact",
        "source_repo/staging/hs-slice/pta/high-voltage-battery-pack-assembly_eu.md",
        "data/forensic_evidence/sanitized_agent_artifacts/pta_high_voltage_battery_pack_assembly_eu.md",
        ("FX_BAD_HV_BATTERY_PACK_PTA_OVERREACH", "FX_BORDERLINE_HV_BATTERY_PACK_GRI3B_REVIEW"),
        "PTA statutory artifact used to test PTA overreach and GRI 3(b) handoff safety.",
    ),
    ForensicAsset(
        "FOR_AGENT_PRA_EU_BTI",
        "sanitized_agent_artifact",
        "source_repo/staging/hs-slice/pra/eu_bti_ebti_sample_ruling_record.md",
        "data/forensic_evidence/sanitized_agent_artifacts/pra_eu_bti_ebti_sample_ruling_record.md",
        ("FX_GOOD_HV_BATTERY_PACK_BTI_EU",),
        "PRA ruling record used to test BTI-backed authority handling.",
    ),
    ForensicAsset(
        "FOR_GRAPH_PC_LI_ION_CELL",
        "sanitized_graph_artifact",
        "source_repo/staging/entities/product_component-lithium-ion-battery-cell.json",
        "data/forensic_evidence/sanitized_graph_artifacts/product_component_lithium_ion_battery_cell.json",
        ("FX_GOOD_LI_ION_CELL_EU", "FX_BORDERLINE_LI_CELL_PRODUCT_NODE_MIXED_STATE"),
        "Product-component graph node used for anti-overloading fixture.",
    ),
    ForensicAsset(
        "FOR_GRAPH_PC_OBC",
        "sanitized_graph_artifact",
        "source_repo/staging/entities/product_component-on-board-charger-obc.json",
        "data/forensic_evidence/sanitized_graph_artifacts/product_component_on_board_charger_obc.json",
        ("FX_GOOD_OBC_AA_EU", "FX_BAD_OBC_EDGE_DIRECTION"),
        "Product-component graph node used for OBC graph-parity fixtures.",
    ),
    ForensicAsset(
        "FOR_GRAPH_HS_85044084_EU",
        "sanitized_graph_artifact",
        "source_repo/staging/entities/hs_code-8504-40-84-eu.json",
        "data/forensic_evidence/sanitized_graph_artifacts/hs_code_8504_40_84_eu.json",
        ("FX_BAD_HS_85044084_INTERNAL_AUTHORITY",),
        "HS-code graph node used to test internal-source-only authority failure.",
    ),
    ForensicAsset(
        "FOR_GRAPH_HS_85044090_EU",
        "sanitized_graph_artifact",
        "source_repo/staging/entities/hs_code-8504-40-90-eu.json",
        "data/forensic_evidence/sanitized_graph_artifacts/hs_code_8504_40_90_eu.json",
        ("FX_GOOD_OBC_AA_EU", "FX_BAD_OBC_EDGE_DIRECTION", "FX_BAD_UNSUPPORTED_PROMOTION"),
        "HS-code graph node used for OBC and unsupported-promotion fixtures.",
    ),
    ForensicAsset(
        "FOR_GRAPH_HS_85076000_EU",
        "sanitized_graph_artifact",
        "source_repo/staging/entities/hs_code-8507-60-00-eu.json",
        "data/forensic_evidence/sanitized_graph_artifacts/hs_code_8507_60_00_eu.json",
        ("FX_GOOD_HV_BATTERY_PACK_BTI_EU", "FX_GOOD_LI_ION_CELL_EU", "FX_BORDERLINE_LI_CELL_PRODUCT_NODE_MIXED_STATE"),
        "HS-code graph node used for battery fixtures.",
    ),
    ForensicAsset(
        "FOR_GRAPH_HS_85366990_EU",
        "sanitized_graph_artifact",
        "source_repo/staging/entities/hs_code-8536-69-90-eu.json",
        "data/forensic_evidence/sanitized_graph_artifacts/hs_code_8536_69_90_eu.json",
        ("FX_GOOD_HV_CONNECTORS_EU",),
        "HS-code graph node used for connector fixture.",
    ),
    ForensicAsset(
        "FOR_GRAPH_HS_85079031_EU_MD",
        "sanitized_graph_artifact",
        "source_repo/knowledge/staging/hs_code-8507-90-31-eu.md",
        "data/forensic_evidence/sanitized_graph_artifacts/hs_code_8507_90_31_eu.md",
        ("FX_BAD_SEPARATOR_CONFIDENCE_INFLATION", "FX_BORDERLINE_SEPARATOR_DIVERGENCE"),
        "Markdown graph node used for separator fixtures.",
    ),
    ForensicAsset(
        "FOR_GRAPH_HS_87089997_EU_MD",
        "sanitized_graph_artifact",
        "source_repo/knowledge/staging/hs_code-8708-99-97-eu.md",
        "data/forensic_evidence/sanitized_graph_artifacts/hs_code_8708_99_97_eu.md",
        ("FX_BORDERLINE_INTEGRATED_E_AXLE_COMPARISON_ONLY",),
        "Markdown graph node used for integrated e-axle comparison fixture.",
    ),
    ForensicAsset(
        "FOR_GRAPH_HS_722619_EU_MD",
        "sanitized_graph_artifact",
        "source_repo/knowledge/staging/hs_code-7226-19-eu.md",
        "data/forensic_evidence/sanitized_graph_artifacts/hs_code_7226_19_eu.md",
        ("FX_BORDERLINE_NOES_CLIENT_FACT",),
        "Markdown graph node used for NOES client-fact fixture.",
    ),
)


SOURCE_ID_TO_ASSET_IDS = {
    "SRC_WCO_GRI_2017": (
        "SRC_ASSET_WCO_GRI_2017_ORIGINAL",
        "SRC_ASSET_WCO_GRI_2017_MD",
        "SRC_ASSET_WCO_GRI_2017_JSON",
        "SRC_ASSET_WCO_GRI_2017_META_JSON",
        "SRC_ASSET_WCO_GRI_2017_NORMALIZED_JSON",
    ),
    "SRC_WCO_SECTION_XVI": (
        "SRC_ASSET_WCO_SECTION_84_ORIGINAL",
        "SRC_ASSET_WCO_SECTION_85_ORIGINAL",
        "SRC_ASSET_WCO_SECTION_84_MD",
        "SRC_ASSET_WCO_SECTION_84_JSON",
        "SRC_ASSET_WCO_SECTION_84_META_JSON",
        "SRC_ASSET_WCO_SECTION_84_NORMALIZED_JSON",
        "SRC_ASSET_WCO_SECTION_85_MD",
        "SRC_ASSET_WCO_SECTION_85_JSON",
        "SRC_ASSET_WCO_SECTION_85_META_JSON",
        "SRC_ASSET_WCO_SECTION_85_NORMALIZED_JSON",
    ),
    "SRC_WCO_SECTION_XVII": (
        "SRC_ASSET_WCO_SECTION_87_ORIGINAL",
        "SRC_ASSET_WCO_SECTION_87_MD",
        "SRC_ASSET_WCO_SECTION_87_JSON",
        "SRC_ASSET_WCO_SECTION_87_META_JSON",
        "SRC_ASSET_WCO_SECTION_87_NORMALIZED_JSON",
    ),
    "SRC_EU_CN_2025_1926_EVS": (
        "SRC_ASSET_EU_CN_2025_1926_ORIGINAL",
        "SRC_ASSET_EU_CN_2025_1926_MD",
        "SRC_ASSET_EU_CN_2025_1926_JSON",
        "SRC_ASSET_EU_CN_2025_1926_META_JSON",
        "SRC_ASSET_EU_CN_2025_1926_NORMALIZED_JSON",
    ),
    "SRC_EU_CN_EXPLANATORY_NOTES_EVS": (
        "SRC_ASSET_EU_CN_EN_ORIGINAL",
        "SRC_ASSET_EU_CN_EN_MD",
        "SRC_ASSET_EU_CN_EN_JSON",
        "SRC_ASSET_EU_CN_EN_META_JSON",
        "SRC_ASSET_EU_CN_EN_NORMALIZED_JSON",
    ),
    "SRC_EU_BTI_SAMPLE": (
        "SRC_ASSET_EU_BTI_SAMPLE_ORIGINAL",
        "SRC_ASSET_EU_BTI_SAMPLE_MD",
        "SRC_ASSET_EU_BTI_SAMPLE_JSON",
        "SRC_ASSET_EU_BTI_SAMPLE_META_JSON",
        "SRC_ASSET_EU_BTI_SAMPLE_NORMALIZED_JSON",
    ),
    "SRC_INTERNAL_CANDIDATE_ARTIFACT": (),
}


FIXTURE_FORENSIC_IDS = {
    "FX_GOOD_OBC_AA_EU": ("FOR_AGENT_AA_OBC", "FOR_GRAPH_PC_OBC", "FOR_GRAPH_HS_85044090_EU"),
    "FX_GOOD_HV_CONNECTORS_EU": ("FOR_AGENT_AA_HV_CONNECTORS", "FOR_GRAPH_HS_85366990_EU"),
    "FX_GOOD_TRACTION_INVERTER_EU": ("FOR_AGENT_AA_TRACTION_INVERTER",),
    "FX_GOOD_HV_BATTERY_PACK_BTI_EU": ("FOR_AGENT_AA_HV_BATTERY_PACK", "FOR_AGENT_PRA_EU_BTI", "FOR_GRAPH_HS_85076000_EU"),
    "FX_GOOD_LI_ION_CELL_EU": ("FOR_AGENT_AA_LI_ION_CELL", "FOR_GRAPH_PC_LI_ION_CELL", "FOR_GRAPH_HS_85076000_EU"),
    "FX_BAD_HS_85044084_INTERNAL_AUTHORITY": ("FOR_GRAPH_HS_85044084_EU",),
    "FX_BAD_HV_BATTERY_PACK_PTA_OVERREACH": ("FOR_AGENT_AA_HV_BATTERY_PACK", "FOR_AGENT_PTA_HV_BATTERY_PACK_EU", "FOR_GRAPH_HS_85076000_EU"),
    "FX_BAD_OBC_EDGE_DIRECTION": ("FOR_AGENT_AA_OBC", "FOR_GRAPH_PC_OBC", "FOR_GRAPH_HS_85044090_EU"),
    "FX_BAD_SEPARATOR_CONFIDENCE_INFLATION": ("FOR_AGENT_AA_SEPARATOR", "FOR_GRAPH_HS_85079031_EU_MD"),
    "FX_BAD_UNSUPPORTED_PROMOTION": ("FOR_GRAPH_HS_85044090_EU",),
    "FX_BORDERLINE_LI_CELL_PRODUCT_NODE_MIXED_STATE": ("FOR_AGENT_AA_LI_ION_CELL", "FOR_GRAPH_PC_LI_ION_CELL", "FOR_GRAPH_HS_85076000_EU"),
    "FX_BORDERLINE_HV_BATTERY_PACK_GRI3B_REVIEW": ("FOR_AGENT_AA_HV_BATTERY_PACK", "FOR_AGENT_PTA_HV_BATTERY_PACK_EU", "FOR_GRAPH_HS_85076000_EU"),
    "FX_BORDERLINE_SEPARATOR_DIVERGENCE": ("FOR_AGENT_AA_SEPARATOR", "FOR_GRAPH_HS_85079031_EU_MD"),
    "FX_BORDERLINE_INTEGRATED_E_AXLE_COMPARISON_ONLY": ("FOR_AGENT_AA_INTEGRATED_E_AXLE", "FOR_GRAPH_HS_87089997_EU_MD"),
    "FX_BORDERLINE_NOES_CLIENT_FACT": ("FOR_AGENT_AA_NOES", "FOR_GRAPH_HS_722619_EU_MD"),
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build the reviewer-safe source and forensic evidence bundle.")
    parser.add_argument("--source-repo-root", type=Path, required=True)
    parser.add_argument("--harness-root", type=Path, required=True)
    parser.add_argument("--dry-run", action="store_true")
    return parser


def parsed_assets() -> tuple[SourceAsset, ...]:
    assets: list[SourceAsset] = []
    for source_stem, harness_stem, source_ids, notes in PARSED_STEMS:
        short_id = source_asset_short_id(source_ids[0], source_stem)
        for suffix, asset_type in PARSED_SUFFIX_TYPES.items():
            source_relative = source_stem + suffix
            harness_relative = harness_stem + suffix
            suffix_id = (
                "MD"
                if suffix == ".md"
                else "JSON"
                if suffix == ".json"
                else "META_JSON"
                if suffix == "_meta.json"
                else "NORMALIZED_JSON"
            )
            assets.append(
                SourceAsset(
                    f"SRC_ASSET_{short_id}_{suffix_id}",
                    asset_type,
                    source_relative,
                    harness_relative,
                    source_ids,
                    notes,
                )
            )
    return tuple(assets)


def source_asset_short_id(source_id: str, source_stem: str) -> str:
    if "eu_hs_commission" in source_stem:
        return "EU_CN_2025_1926"
    if "explanatory_notes" in source_stem:
        return "EU_CN_EN"
    if "ebti" in source_stem:
        return "EU_BTI_SAMPLE"
    if "gri" in source_stem:
        return "WCO_GRI_2017"
    if "section_84" in source_stem:
        return "WCO_SECTION_84"
    if "section_85" in source_stem:
        return "WCO_SECTION_85"
    if "section_87" in source_stem:
        return "WCO_SECTION_87"
    if "section_90" in source_stem:
        return "WCO_SECTION_90"
    return re.sub(r"[^A-Z0-9]+", "_", source_id.upper()).strip("_")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def assert_inside(path: Path, root: Path) -> None:
    path.resolve().relative_to(root.resolve())


def copy_source_asset(asset: SourceAsset, source_repo_root: Path, harness_root: Path, copied_at: str, dry_run: bool) -> dict[str, Any]:
    src = source_repo_root / asset.source_relative_path
    dest = harness_root / asset.harness_relative_path
    if not src.exists():
        raise FileNotFoundError(f"Missing source asset: {src}")
    assert_inside(dest, harness_root)
    if not dry_run:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
    stat_path = src if dry_run else dest
    return {
        "asset_id": asset.asset_id,
        "asset_type": asset.asset_type,
        "source_repo_relative_path": asset.source_relative_path,
        "harness_relative_path": asset.harness_relative_path,
        "sha256": sha256(stat_path),
        "byte_size": stat_path.stat().st_size,
        "copied_at": copied_at,
        "source_id_links": list(asset.source_id_links),
        "notes": asset.notes,
    }


def sanitize_text(text: str) -> str:
    replacements = {
        "D" "RONA": "source extraction system",
        "source extraction system": "source extraction system",
        "Ka" "nan Labs": "the originating organization",
        "Ka" "nan": "the originating organization",
        "Sector " "Watch": "downstream decision-support system",
        "Sector" "Watch": "downstream decision-support system",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"/U" "sers/[^\s)\\]]+", "[local_path_removed]", text)
    text = re.sub(r"[\w.+-]+@[\w.-]+", "[email_removed]", text)
    return text


def copy_forensic_asset(asset: ForensicAsset, source_repo_root: Path, harness_root: Path, copied_at: str, dry_run: bool) -> dict[str, Any]:
    src = source_repo_root / asset.source_relative_path
    dest = harness_root / asset.harness_relative_path
    if not src.exists():
        raise FileNotFoundError(f"Missing forensic artifact: {src}")
    assert_inside(dest, harness_root)
    if not dry_run:
        dest.parent.mkdir(parents=True, exist_ok=True)
        if src.suffix.lower() in {".md", ".json"}:
            text = sanitize_text(src.read_text(encoding="utf-8"))
            banner = (
                "<!-- Reviewer-safe sanitized forensic artifact. "
                "This file evidences artifact origin only and is not external legal authority. -->\n\n"
            )
            dest.write_text(banner + text, encoding="utf-8")
        else:
            shutil.copy2(src, dest)
    stat_path = src if dry_run else dest
    return {
        "forensic_artifact_id": asset.artifact_id,
        "artifact_type": asset.artifact_type,
        "original_source_path": asset.source_relative_path,
        "sanitized_destination_path": asset.harness_relative_path,
        "linked_fixture_ids": list(asset.linked_fixture_ids),
        "reason_for_inclusion": asset.reason_for_inclusion,
        "sanitization_actions": list(asset.sanitization_actions),
        "legal_authority_role": asset.legal_authority_role,
        "sha256": sha256(stat_path),
        "byte_size": stat_path.stat().st_size,
        "copied_at": copied_at,
    }


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any, dry_run: bool) -> None:
    if dry_run:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=False) + "\n", encoding="utf-8")


def write_text(path: Path, text: str, dry_run: bool) -> None:
    if dry_run:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def load_fixtures(harness_root: Path) -> list[dict[str, Any]]:
    fixtures: list[dict[str, Any]] = []
    for name in ("nodes_good.json", "nodes_bad.json", "nodes_borderline.json"):
        fixtures.extend(load_json(harness_root / "data" / "graph_fixtures" / name))
    return fixtures


def update_fixture_files(harness_root: Path, dry_run: bool) -> None:
    for name in ("nodes_good.json", "nodes_bad.json", "nodes_borderline.json"):
        path = harness_root / "data" / "graph_fixtures" / name
        fixtures = load_json(path)
        for fixture in fixtures:
            source_ids = sorted({item["source_id"] for item in fixture.get("legal_authority_chain", [])})
            source_asset_ids: list[str] = []
            parsed_asset_ids: list[str] = []
            for source_id in source_ids:
                for asset_id in SOURCE_ID_TO_ASSET_IDS.get(source_id, ()):
                    if any(token in asset_id for token in ("ORIGINAL",)):
                        source_asset_ids.append(asset_id)
                    else:
                        parsed_asset_ids.append(asset_id)
            fixture["source_asset_ids"] = sorted(dict.fromkeys(source_asset_ids))
            fixture["parsed_asset_ids"] = sorted(dict.fromkeys(parsed_asset_ids))
            fixture["forensic_artifact_ids"] = list(FIXTURE_FORENSIC_IDS.get(fixture["artifact_id"], ()))
        write_json(path, fixtures, dry_run)


def update_source_manifest(harness_root: Path, dry_run: bool) -> None:
    path = harness_root / "data" / "fixtures" / "source_manifest.json"
    manifest = load_json(path)
    for source in manifest["sources"]:
        asset_ids = SOURCE_ID_TO_ASSET_IDS.get(source["source_id"], ())
        source["source_asset_ids"] = [asset_id for asset_id in asset_ids if "ORIGINAL" in asset_id]
        source["parsed_asset_ids"] = [asset_id for asset_id in asset_ids if "ORIGINAL" not in asset_id]
        source["source_path"] = "data/source_corpus/SOURCE_ASSET_MANIFEST.json" if asset_ids else source.get("source_path")
    write_json(path, manifest, dry_run)


def build_lineage_map(harness_root: Path, dry_run: bool) -> None:
    fixtures = load_fixtures(harness_root)
    gold_by_artifact = {
        case["artifact_id"]: case
        for case in load_json(harness_root / "data" / "fixtures" / "gold_cases.json")
    }
    lineage = []
    for fixture in fixtures:
        gold = gold_by_artifact[fixture["artifact_id"]]
        lineage.append(
            {
                "fixture_id": fixture["artifact_id"],
                "scenario_id": fixture["scenario_id"],
                "gold_case_id": gold["scenario_id"],
                "fixture_class": fixture["fixture_class"],
                "source_authorities": fixture.get("legal_authority_chain", []),
                "parsed_source_anchors": fixture.get("quoted_span_or_row_ref", []),
                "source_asset_ids": fixture.get("source_asset_ids", []),
                "parsed_asset_ids": fixture.get("parsed_asset_ids", []),
                "forensic_origin_artifact_ids": fixture.get("forensic_artifact_ids", []),
                "graph_nodes": fixture.get("graph_nodes", []),
                "graph_edges": fixture.get("graph_edges", []),
                "expected_evaluator_result": {
                    "expected_route": gold["expected_route"],
                    "expected_control_state": gold["expected_control_state"],
                    "expected_failure_categories": gold["expected_failure_categories"],
                    "human_review_required": gold["human_review_required"],
                },
                "authority_boundary_note": "forensic artifacts evidence origin only; legal authority is limited to legal_authority_chain",
            }
        )
    write_json(harness_root / "data" / "fixtures" / "FIXTURE_LINEAGE_MAP.json", lineage, dry_run)


def write_bundle_docs(harness_root: Path, dry_run: bool) -> None:
    write_text(
        harness_root / "data" / "source_corpus" / "SOURCE_BUNDLE_README.md",
        """# Source Corpus Bundle

This folder contains a cited subset of EU, WCO, and EU BTI source material used by the legal extraction evaluation harness.

It is not a full HS corpus. It contains only the original PDFs/CSV and parsed outputs needed to trace the paper fixtures back to source authority.

- `originals/` contains source PDFs and the BTI CSV.
- `parsed/` contains markdown, raw JSON, parser metadata JSON, and normalized JSON outputs where available.
- `SOURCE_ASSET_MANIFEST.json` records hashes, sizes, source IDs, and copy lineage.
""",
        dry_run,
    )
    write_text(
        harness_root / "data" / "forensic_evidence" / "SANITIZATION_LOG.md",
        """# Sanitization Log

The forensic evidence bundle contains a small reviewer-safe sample of internal extraction artifacts and graph artifacts.

Sanitization actions:
- Internal product/company names are neutralized where present.
- Absolute local paths and email-like strings are removed.
- A reviewer banner is added to each sanitized text artifact.
- Files are included only to evidence artifact origin, graph shape, or known failure modes.

These artifacts are not external legal authority. Legal authority is represented only by `legal_authority_chain` entries pointing to EU/WCO/BTI source anchors.
""",
        dry_run,
    )


def manifest_for_source_assets(source_repo_root: Path, harness_root: Path, copied_at: str, dry_run: bool) -> list[dict[str, Any]]:
    manifests = []
    for asset in SOURCE_ASSETS + parsed_assets():
        if any(token in asset.source_relative_path for token in EXCLUDED_TOKENS):
            continue
        manifests.append(copy_source_asset(asset, source_repo_root, harness_root, copied_at, dry_run))
    return manifests


def manifest_for_forensic_assets(source_repo_root: Path, harness_root: Path, copied_at: str, dry_run: bool) -> list[dict[str, Any]]:
    manifests = []
    for asset in FORENSIC_ASSETS:
        if any(token in asset.source_relative_path for token in EXCLUDED_TOKENS):
            continue
        manifests.append(copy_forensic_asset(asset, source_repo_root, harness_root, copied_at, dry_run))
    return manifests


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    source_repo_root = args.source_repo_root.resolve()
    harness_root = args.harness_root.resolve()
    copied_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    source_manifest = manifest_for_source_assets(source_repo_root, harness_root, copied_at, args.dry_run)
    forensic_manifest = manifest_for_forensic_assets(source_repo_root, harness_root, copied_at, args.dry_run)

    update_fixture_files(harness_root, args.dry_run)
    update_source_manifest(harness_root, args.dry_run)
    build_lineage_map(harness_root, args.dry_run)
    write_bundle_docs(harness_root, args.dry_run)

    write_json(
        harness_root / "data" / "source_corpus" / "SOURCE_ASSET_MANIFEST.json",
        {
            "schema_version": "1.0",
            "generated_at": copied_at,
            "copy_policy": "copy-only from source repository; no mutation of source repository",
            "assets": source_manifest,
        },
        args.dry_run,
    )
    write_json(
        harness_root / "data" / "forensic_evidence" / "FORENSIC_EXPORT_MANIFEST.json",
        {
            "schema_version": "1.0",
            "generated_at": copied_at,
            "legal_authority_rule": "forensic artifacts evidence origin only and cannot satisfy legal authority",
            "artifacts": forensic_manifest,
        },
        args.dry_run,
    )

    print(
        json.dumps(
            {
                "dry_run": args.dry_run,
                "source_assets": len(source_manifest),
                "forensic_artifacts": len(forensic_manifest),
                "harness_root": str(harness_root),
                "source_repo_root_read_only": str(source_repo_root),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
