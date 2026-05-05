from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from legal_extract_eval.eu_cn_layout_parser import (
    LayoutConfig,
    compile_layout_records,
    extract_layout_blocks,
    ocr_pages_from_canonical,
    render_layout_review,
)


CodeRecord = dict[str, Any]


@dataclass(frozen=True)
class SourceProfile:
    source_id: str
    title: str
    jurisdiction: str
    authority_class: str
    source_type: str
    compiler_profile: str
    original_path: str
    parsed_json_path: str | None
    normalized_json_path: str | None
    output_group: str
    output_stem: str


SOURCE_PROFILES: tuple[SourceProfile, ...] = (
    SourceProfile(
        source_id="SRC_EU_CN_2025_1926_EVS",
        title="Commission Implementing Regulation (EU) 2025/1926, EV-related CN extract",
        jurisdiction="EU",
        authority_class="primary_legal_text",
        source_type="tariff_table_pdf",
        compiler_profile="eu_cn_tariff_table",
        original_path="data/source_corpus/originals/eu/eu_cn_2025_1926_evs.pdf",
        parsed_json_path="data/source_corpus/parsed_v2/eu/eu_cn_2025_1926_evs.json",
        normalized_json_path="data/source_corpus/parsed_v2/eu/eu_cn_2025_1926_evs_normalized.json",
        output_group="eu",
        output_stem="eu_cn_2025_1926_evs",
    ),
    SourceProfile(
        source_id="SRC_EU_CN_EXPLANATORY_NOTES_EVS",
        title="Explanatory Notes to the Combined Nomenclature of the European Union, EV-related extract",
        jurisdiction="EU",
        authority_class="interpretive_legal_note",
        source_type="two_column_code_note_pdf",
        compiler_profile="eu_cn_explanatory_notes_layout",
        original_path="data/source_corpus/originals/eu/eu_cn_explanatory_notes_evs.pdf",
        parsed_json_path="data/source_corpus/parsed_v2/eu/eu_cn_explanatory_notes_evs.json",
        normalized_json_path="data/source_corpus/parsed_v2/eu/eu_cn_explanatory_notes_evs_normalized.json",
        output_group="eu",
        output_stem="eu_cn_explanatory_notes_evs",
    ),
    SourceProfile(
        source_id="SRC_EU_BTI_SAMPLE",
        title="EU BTI targeted sample test run",
        jurisdiction="EU",
        authority_class="ruling_or_precedent",
        source_type="structured_csv",
        compiler_profile="bti_csv_rows",
        original_path="data/source_corpus/originals/bti/ebti_sample_targeted_test_run.csv",
        parsed_json_path="data/source_corpus/parsed_v2/bti/ebti_sample_targeted_test_run.json",
        normalized_json_path="data/source_corpus/parsed_v2/bti/ebti_sample_targeted_test_run_normalized.json",
        output_group="bti",
        output_stem="ebti_sample_targeted_test_run",
    ),
    SourceProfile(
        source_id="SRC_WCO_GRI_2017",
        title="WCO General Rules for the Interpretation of the Harmonized System",
        jurisdiction="WCO",
        authority_class="primary_legal_text",
        source_type="single_flow_legal_text_pdf",
        compiler_profile="wco_gri_rules",
        original_path="data/source_corpus/originals/wco/wco_gri_rules_2017.pdf",
        parsed_json_path="data/source_corpus/parsed/wco/wco_gri_rules_2017.json",
        normalized_json_path="data/source_corpus/parsed/wco/wco_gri_rules_2017_normalized.json",
        output_group="wco",
        output_stem="wco_gri_rules_2017",
    ),
    SourceProfile(
        source_id="SRC_WCO_SECTION_84",
        title="WCO 2022 HS Chapter 84 heading table",
        jurisdiction="WCO",
        authority_class="primary_legal_text",
        source_type="wco_heading_table_pdf",
        compiler_profile="wco_heading_table",
        original_path="data/source_corpus/originals/wco/wco_2022_section_84_complex.pdf",
        parsed_json_path="data/source_corpus/parsed/wco/wco_2022_section_84_complex.json",
        normalized_json_path="data/source_corpus/parsed/wco/wco_2022_section_84_complex_normalized.json",
        output_group="wco",
        output_stem="wco_2022_section_84_complex",
    ),
    SourceProfile(
        source_id="SRC_WCO_SECTION_85",
        title="WCO 2022 HS Chapter 85 heading table",
        jurisdiction="WCO",
        authority_class="primary_legal_text",
        source_type="wco_heading_table_pdf",
        compiler_profile="wco_heading_table",
        original_path="data/source_corpus/originals/wco/wco_2022_section_85_complex.pdf",
        parsed_json_path="data/source_corpus/parsed/wco/wco_2022_section_85_complex.json",
        normalized_json_path="data/source_corpus/parsed/wco/wco_2022_section_85_complex_normalized.json",
        output_group="wco",
        output_stem="wco_2022_section_85_complex",
    ),
    SourceProfile(
        source_id="SRC_WCO_SECTION_87",
        title="WCO 2022 HS Chapter 87 heading table",
        jurisdiction="WCO",
        authority_class="primary_legal_text",
        source_type="wco_heading_table_pdf",
        compiler_profile="wco_heading_table",
        original_path="data/source_corpus/originals/wco/wco_2022_section_87_complex.pdf",
        parsed_json_path="data/source_corpus/parsed/wco/wco_2022_section_87_complex.json",
        normalized_json_path="data/source_corpus/parsed/wco/wco_2022_section_87_complex_normalized.json",
        output_group="wco",
        output_stem="wco_2022_section_87_complex",
    ),
    SourceProfile(
        source_id="SRC_WCO_SECTION_90",
        title="WCO 2022 HS Chapter 90 heading table",
        jurisdiction="WCO",
        authority_class="primary_legal_text",
        source_type="wco_heading_table_pdf",
        compiler_profile="wco_heading_table",
        original_path="data/source_corpus/originals/wco/wco_2022_section_90_complex.pdf",
        parsed_json_path="data/source_corpus/parsed/wco/wco_2022_section_90_complex.json",
        normalized_json_path="data/source_corpus/parsed/wco/wco_2022_section_90_complex_normalized.json",
        output_group="wco",
        output_stem="wco_2022_section_90_complex",
    ),
)


HEADING_DOTTED_RE = re.compile(r"^\d{2}\.\d{2}$")
HS_DOTTED_RE = re.compile(r"^\d{4}\.\d{2}$")
CN_CODE_RE = re.compile(r"^\d{4}(?:\s?\d{2}){0,2}(?:\s?\d{2})?$")
GRI_MAIN_RE = re.compile(r"^(?P<rule>[1-6])\.\s+(?P<text>.+)")
GRI_SUB_RE = re.compile(r"^\((?P<letter>[a-c])\)\s+(?P<text>.+)")


def build_all_source_outputs(repo_root: Path) -> dict[str, Any]:
    compiled: list[dict[str, Any]] = []
    for profile in SOURCE_PROFILES:
        records, qc, markdown, layout_profile = compile_source(profile, repo_root)
        output_dir = repo_root / "data/source_corpus/records" / profile.output_group
        output_dir.mkdir(parents=True, exist_ok=True)

        records_path = output_dir / f"{profile.output_stem}_records.json"
        markdown_path = output_dir / f"{profile.output_stem}_records.md"
        qc_path = output_dir / f"{profile.output_stem}_qc.json"
        layout_profile_path = output_dir / f"{profile.output_stem}_layout_profile.json"

        records_path.write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        markdown_path.write_text(markdown, encoding="utf-8")
        qc_path.write_text(json.dumps(qc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        layout_profile_path.write_text(json.dumps(layout_profile, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

        compiled.append(
            {
                "source_id": profile.source_id,
                "title": profile.title,
                "source_type": profile.source_type,
                "compiler_profile": profile.compiler_profile,
                "record_count": len(records),
                "records_path": str(records_path.relative_to(repo_root)),
                "records_markdown_path": str(markdown_path.relative_to(repo_root)),
                "qc_path": str(qc_path.relative_to(repo_root)),
                "layout_profile_path": str(layout_profile_path.relative_to(repo_root)),
                "review_flag_counts": qc.get("review_flag_counts", {}),
            }
        )

    manifest = {
        "manifest_name": "source_record_profile_manifest",
        "schema_version": "1.0.0",
        "description": "Document-profiled source compilers used to create legal-safe record layers from the HS source corpus.",
        "profiles": [profile.__dict__ for profile in SOURCE_PROFILES],
        "compiled_outputs": compiled,
    }
    manifest_path = repo_root / "data/source_corpus/SOURCE_RECORD_PROFILE_MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return manifest


def compile_source(profile: SourceProfile, repo_root: Path) -> tuple[list[CodeRecord], dict[str, Any], str, dict[str, Any]]:
    layout_profile = build_layout_profile(profile, repo_root)
    compilers: dict[str, Callable[[SourceProfile, Path], tuple[list[CodeRecord], dict[str, Any], str]]] = {
        "eu_cn_tariff_table": compile_eu_cn_tariff_records,
        "eu_cn_explanatory_notes_layout": compile_eu_cn_explanatory_note_records,
        "bti_csv_rows": compile_bti_row_records,
        "wco_gri_rules": compile_wco_gri_rule_records,
        "wco_heading_table": compile_wco_heading_table_records,
    }
    records, qc, markdown = compilers[profile.compiler_profile](profile, repo_root)
    qc["source_id"] = profile.source_id
    qc["compiler_profile"] = profile.compiler_profile
    qc["layout_profile_inferred_type"] = layout_profile.get("inferred_layout_type")
    return records, qc, markdown, layout_profile


def build_layout_profile(profile: SourceProfile, repo_root: Path) -> dict[str, Any]:
    original = repo_root / profile.original_path
    if profile.source_type == "structured_csv":
        with original.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.reader(handle)
            headers = next(reader)
            rows = sum(1 for _ in reader)
        return {
            "source_id": profile.source_id,
            "source_type": profile.source_type,
            "inferred_layout_type": "CSV/structured dataset",
            "visual_engine": "csv_header_scan",
            "sample_pages": [],
            "columns": [_clean_header(header) for header in headers],
            "row_count": rows,
            "review_flags": [],
        }

    parsed = _load_json(repo_root / profile.parsed_json_path) if profile.parsed_json_path else {}
    try:
        import fitz  # type: ignore[import-not-found]

        with fitz.open(original) as document:
            page_count = document.page_count
            sample_indexes = sorted({0, max(0, page_count // 2), max(0, page_count - 1)})
            samples = []
            for page_index in sample_indexes:
                page = document[page_index]
                blocks = [_normalize_space(block[4]) for block in page.get_text("blocks")]
                blocks = [block for block in blocks if block]
                samples.append(
                    {
                        "page": page_index + 1,
                        "block_count": len(blocks),
                        "code_like_block_count": sum(1 for block in blocks if _has_code_signal(block)),
                        "table_header_signal": _table_header_signal(blocks),
                        "sample_text": blocks[:8],
                    }
                )
        visual_engine = "pymupdf"
    except Exception:
        pages = parsed.get("content", {}).get("pages", []) if isinstance(parsed, dict) else []
        blocks_by_page: dict[int, list[str]] = {}
        for block in parsed.get("content", {}).get("blocks", []) if isinstance(parsed, dict) else []:
            text = _normalize_space(block.get("text", ""))
            for page in block.get("page_numbers", []) or [1]:
                blocks_by_page.setdefault(int(page), []).append(text)
        page_count = len(pages) or max(blocks_by_page or {1: []})
        sample_pages = sorted({1, max(1, page_count // 2), page_count})
        samples = []
        for page in sample_pages:
            texts = blocks_by_page.get(page, [])
            samples.append(
                {
                    "page": page,
                    "block_count": len(texts),
                    "code_like_block_count": sum(1 for block in texts if _has_code_signal(block)),
                    "table_header_signal": _table_header_signal(texts),
                    "sample_text": texts[:8],
                }
            )
        visual_engine = "parsed_json_fallback"

    return {
        "source_id": profile.source_id,
        "source_type": profile.source_type,
        "inferred_layout_type": _infer_layout_type(profile, samples),
        "visual_engine": visual_engine,
        "sample_pages": samples,
        "review_flags": [] if visual_engine == "pymupdf" else ["visual_preflight_used_parsed_json_fallback"],
    }


def compile_eu_cn_tariff_records(profile: SourceProfile, repo_root: Path) -> tuple[list[CodeRecord], dict[str, Any], str]:
    data = _load_json(repo_root / _require(profile.normalized_json_path))
    nodes = data.get("payload", {}).get("nodes", [])
    records = [
        _record_from_tariff_node(profile, node, index, code_style="cn")
        for index, node in enumerate(nodes, start=1)
        if _admit_tariff_node(node)
    ]
    qc = _qc_for_records(records)
    qc["source_warnings"] = data.get("review_flags", [])
    return records, qc, render_records_markdown(profile, records)


def compile_wco_heading_table_records(profile: SourceProfile, repo_root: Path) -> tuple[list[CodeRecord], dict[str, Any], str]:
    parsed = _load_json(repo_root / _require(profile.parsed_json_path))
    records: list[CodeRecord] = _wco_note_records(profile, parsed)
    heading_context: str | None = None
    parent_stack: dict[int, str] = {}
    record_index = len(records) + 1
    for table in parsed.get("content", {}).get("tables", []):
        for row_index, row in enumerate(table.get("rows", []), start=1):
            record = _wco_record_from_row(profile, table, row, row_index, record_index, heading_context, parent_stack)
            if record is None:
                continue
            record_index += 1
            if record["record_type"] == "heading":
                heading_context = record["heading_code"]
                parent_stack = {1: record["record_id"]}
            elif record.get("hierarchy_depth") is not None:
                depth = int(record["hierarchy_depth"])
                parent_stack[depth] = record["record_id"]
                for stale_depth in [key for key in parent_stack if key > depth]:
                    parent_stack.pop(stale_depth, None)
            records.append(record)
    qc = _qc_for_records(records)
    qc["table_count"] = len(parsed.get("content", {}).get("tables", []))
    qc["chapter_note_record_count"] = sum(1 for record in records if str(record.get("record_type", "")).startswith("chapter_note"))
    return records, qc, render_records_markdown(profile, records)


def compile_wco_gri_rule_records(profile: SourceProfile, repo_root: Path) -> tuple[list[CodeRecord], dict[str, Any], str]:
    try:
        blocks = _pdf_text_blocks(repo_root / profile.original_path)
        block_source = "pymupdf"
    except RuntimeError:
        blocks = _parsed_json_text_blocks(repo_root / _require(profile.parsed_json_path))
        block_source = "parsed_json_fallback"
    records: list[CodeRecord] = []
    current_main: str | None = None
    current_intro: str | None = None
    for index, block in enumerate(blocks, start=1):
        text = block["text"]
        embedded_subrule = re.match(r"^(?P<rule>[25])\.\s+\((?P<letter>[ab])\)\s+(?P<text>.+)", text)
        main = GRI_MAIN_RE.match(text)
        sub = GRI_SUB_RE.match(text)
        if embedded_subrule:
            current_main = embedded_subrule.group("rule")
            current_intro = None
            rule_id = f"GRI_{current_main}{embedded_subrule.group('letter').upper()}"
            rule_text = text
        elif main and main.group("rule") in {"3", "5"}:
            current_main = main.group("rule")
            current_intro = text
            continue
        elif main:
            current_main = main.group("rule")
            current_intro = None
            rule_id = f"GRI_{current_main}"
            rule_text = text
        elif sub and current_main in {"2", "3", "5"}:
            rule_id = f"GRI_{current_main}{sub.group('letter').upper()}"
            rule_text = text
        else:
            continue
        records.append(
            {
                "record_id": f"WCO_{rule_id}",
                "source_id": profile.source_id,
                "source_title": profile.title,
                "compiler_profile": profile.compiler_profile,
                "jurisdiction": profile.jurisdiction,
                "authority_class": profile.authority_class,
                "record_type": "gri_rule",
                "legal_anchor": rule_id,
                "rule_id": rule_id,
                "title": rule_id.replace("_", " "),
                "parent_rule_intro": current_intro,
                "legal_text": rule_text,
                "source_excerpt": rule_text,
                "source_locator": {
                    "page": block["page"],
                    "bbox": block.get("bbox"),
                    "block_index": block["block_index"],
                    "block_source": block_source,
                },
                "review_flags": [] if block_source == "pymupdf" else ["source_locator_uses_parsed_json_fallback"],
                "ordinal": index,
            }
        )
    expected = {"GRI_1", "GRI_2A", "GRI_2B", "GRI_3A", "GRI_3B", "GRI_3C", "GRI_4", "GRI_5A", "GRI_5B", "GRI_6"}
    found = {record["rule_id"] for record in records}
    qc = _qc_for_records(records)
    qc["missing_expected_rules"] = sorted(expected - found)
    return records, qc, render_records_markdown(profile, records)


def compile_bti_row_records(profile: SourceProfile, repo_root: Path) -> tuple[list[CodeRecord], dict[str, Any], str]:
    csv_path = repo_root / profile.original_path
    records: list[CodeRecord] = []
    with csv_path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        for row_number, raw_row in enumerate(reader, start=2):
            row = {_clean_header(key): _normalize_space(value) for key, value in raw_row.items()}
            bti_ref = row.get("BTI_REFERENCE") or f"row_{row_number}"
            code = row.get("NOMENCLATURE_CODE", "")
            record_id = f"EU_BTI_{_slug(bti_ref)}"
            records.append(
                {
                    "record_id": record_id,
                    "source_id": profile.source_id,
                    "source_title": profile.title,
                    "compiler_profile": profile.compiler_profile,
                    "jurisdiction": profile.jurisdiction,
                    "authority_class": profile.authority_class,
                    "record_type": "bti_ruling_row",
                    "legal_anchor": bti_ref,
                    "bti_reference": bti_ref,
                    "issuing_country": row.get("ISSUING_COUNTRY"),
                    "status": row.get("STATUS"),
                    "nomenclature_code_raw": code,
                    "nomenclature_code": _normalize_code(code),
                    "validity": {
                        "start_date": row.get("START_DATE_OF_VALIDITY"),
                        "end_date": row.get("END_DATE_OF_VALIDITY"),
                        "date_of_issue": row.get("DATE_OF__ISSUE") or row.get("DATE_OF_ISSUE") or row.get("DATE_OF _ISSUE"),
                    },
                    "goods_description": row.get("DESCRIPTION_OF_GOODS"),
                    "classification_justification": row.get("CLASSIFICATION_JUSTIFICATION"),
                    "keywords": [item for item in (row.get("KEYWORDS") or "").split(",") if item],
                    "source_excerpt": _normalize_space(
                        " ".join(
                            filter(
                                None,
                                [
                                    bti_ref,
                                    row.get("NOMENCLATURE_CODE"),
                                    row.get("CLASSIFICATION_JUSTIFICATION"),
                                    row.get("DESCRIPTION_OF_GOODS"),
                                ],
                            )
                        )
                    ),
                    "source_locator": {
                        "csv_row_number": row_number,
                        "row_id": bti_ref,
                    },
                    "review_flags": _bti_review_flags(row),
                    "raw_row": row,
                    "ordinal": row_number - 1,
                }
            )
    qc = _qc_for_records(records)
    return records, qc, render_records_markdown(profile, records)


def compile_eu_cn_explanatory_note_records(profile: SourceProfile, repo_root: Path) -> tuple[list[CodeRecord], dict[str, Any], str]:
    pdf_path = repo_root / profile.original_path
    canonical_json_path = repo_root / _require(profile.parsed_json_path)
    try:
        blocks = extract_layout_blocks(pdf_path, config=LayoutConfig())
        records, qc = compile_layout_records(blocks, ocr_pages=ocr_pages_from_canonical(canonical_json_path))
    except Exception:
        existing = repo_root / "data/source_corpus/parsed_v2/eu/eu_cn_explanatory_notes_evs_layout_records.json"
        qc_existing = repo_root / "data/source_corpus/parsed_v2/eu/eu_cn_explanatory_notes_evs_layout_qc.json"
        records = _load_json(existing)
        qc = _load_json(qc_existing)
        qc.setdefault("review_flag_counts", {})
        qc.setdefault("fallback_used", "existing_layout_records")
    enriched = []
    for index, record in enumerate(records, start=1):
        enriched.append(
            {
                **record,
                "source_id": profile.source_id,
                "source_title": profile.title,
                "compiler_profile": profile.compiler_profile,
                "jurisdiction": profile.jurisdiction,
                "authority_class": profile.authority_class,
                "record_type": "eu_cn_explanatory_note",
                "legal_anchor": _explanatory_anchor(record),
                "source_locator": {
                    "page": record.get("page"),
                    "pages": record.get("pages", []),
                    "bbox": record.get("source_bbox"),
                },
                "ordinal": index,
            }
        )
    qc = _qc_for_records(enriched) | {key: value for key, value in qc.items() if key not in {"record_count", "review_flag_counts"}}
    return enriched, qc, render_layout_review(enriched)


def _record_from_tariff_node(profile: SourceProfile, node: dict[str, Any], index: int, *, code_style: str) -> CodeRecord:
    code = _normalize_code(str(node.get("code") or ""))
    raw_row = node.get("raw_row") or []
    description = _clean_description(str(node.get("description") or ""))
    review_flags = list(node.get("warnings") or [])
    if node.get("requires_review"):
        review_flags.append("source_normalizer_requires_review")
    if not code and node.get("node_type") not in {"label", "chapter", "section"}:
        review_flags.append("missing_code_for_coded_record")
    return {
        "record_id": f"{profile.output_stem.upper()}_{code or 'LABEL'}_{index:04d}",
        "source_id": profile.source_id,
        "source_title": profile.title,
        "compiler_profile": profile.compiler_profile,
        "jurisdiction": profile.jurisdiction,
        "authority_class": profile.authority_class,
        "record_type": f"{code_style}_tariff_row",
        "legal_anchor": code or node.get("description"),
        "code": code or None,
        "heading_code": _normalize_code(str(node.get("heading_code") or "")) or None,
        "hs6_code": _normalize_code(str(node.get("hs6_code") or "")) or None,
        "item_code": _normalize_code(str(node.get("item_code") or "")) or None,
        "description": description,
        "supplementary_unit": node.get("unit"),
        "node_type": node.get("node_type"),
        "hierarchy_depth": node.get("depth"),
        "parent_code": _normalize_code(str(node.get("parent_code") or "")) or None,
        "parent_node_id": node.get("parent_node_id"),
        "source_excerpt": " | ".join(str(item) for item in raw_row if item) or description,
        "source_locator": {
            "pages": node.get("source_pages", []),
            "table_id": node.get("source_table_id"),
            "row_index": node.get("source_row_index"),
        },
        "raw_row": raw_row,
        "review_flags": sorted(set(review_flags)),
        "ordinal": index,
    }


def _wco_record_from_row(
    profile: SourceProfile,
    table: dict[str, Any],
    row: list[Any],
    row_index: int,
    record_index: int,
    heading_context: str | None,
    parent_stack: dict[int, str],
) -> CodeRecord | None:
    cells = [_normalize_space(cell) for cell in row]
    if not any(cells):
        return None
    heading_cell = next((cell for cell in cells[:2] if HEADING_DOTTED_RE.match(cell)), "")
    hs_cell = next((cell for cell in cells[:2] if HS_DOTTED_RE.match(cell)), "")
    description = _wco_description(cells, heading_cell, hs_cell)
    if not description and not heading_cell and not hs_cell:
        return None
    if heading_cell:
        heading_code = _normalize_code(heading_cell)
        code = heading_code
        record_type = "heading"
        depth = 1
        parent_record_id = None
    elif hs_cell:
        code = _normalize_code(hs_cell)
        heading_code = heading_context or code[:4]
        record_type = "subheading"
        depth = max(2, min(6, _dash_depth(description) + 1))
        parent_record_id = parent_stack.get(depth - 1) or parent_stack.get(1)
    else:
        code = None
        heading_code = heading_context
        record_type = "label"
        depth = max(2, min(6, _dash_depth(description) + 1))
        parent_record_id = parent_stack.get(depth - 1) or parent_stack.get(1)
    review_flags = []
    if heading_cell and hs_cell:
        review_flags.append("heading_and_subheading_same_row_requires_review")
    if record_type != "heading" and not heading_code:
        review_flags.append("missing_heading_context")
    if "\n" in " ".join(str(cell) for cell in row):
        review_flags.append("multiline_row")
    return {
        "record_id": f"{profile.output_stem.upper()}_{code or 'LABEL'}_{record_index:04d}",
        "source_id": profile.source_id,
        "source_title": profile.title,
        "compiler_profile": profile.compiler_profile,
        "jurisdiction": profile.jurisdiction,
        "authority_class": profile.authority_class,
        "record_type": record_type,
        "legal_anchor": code or f"{heading_code or 'chapter'} label row {row_index}",
        "code": code,
        "heading_code": heading_code,
        "description": _clean_description(description),
        "hierarchy_depth": depth,
        "parent_record_id": parent_record_id,
        "source_excerpt": " | ".join(cells),
        "source_locator": {
            "pages": table.get("page_numbers", []),
            "table_id": table.get("id"),
            "row_index": row_index,
        },
        "raw_row": row,
        "review_flags": sorted(set(review_flags)),
        "ordinal": record_index,
    }


def _wco_note_records(profile: SourceProfile, parsed: dict[str, Any]) -> list[CodeRecord]:
    records: list[CodeRecord] = []
    chapter = _chapter_from_profile(profile)
    current_note: str | None = None
    note_ordinal = 1
    for block in parsed.get("content", {}).get("blocks", []):
        text = _normalize_space(block.get("text", ""))
        if not text:
            continue
        if text == "Heading H.S. Code":
            break
        if text.lower().startswith("chapter ") or text.lower() == "notes.":
            continue
        if block.get("type") in {"heading", "section_header"} and not re.match(r"^\d+\.-", text):
            continue
        note_match = re.match(r"^(?P<note>\d+)\.-\s*(?P<body>.+)", text)
        sub_match = re.match(r"^\((?P<label>[a-z]+|[ivx]+)\)\s*(?P<body>.+)", text, re.IGNORECASE)
        if note_match:
            current_note = note_match.group("note")
            anchor = f"Chapter {chapter} Note {current_note}"
            record_type = "chapter_note"
        elif sub_match and current_note:
            anchor = f"Chapter {chapter} Note {current_note}({sub_match.group('label')})"
            record_type = "chapter_note_subparagraph"
        elif current_note:
            anchor = f"Chapter {chapter} Note {current_note} continuation {note_ordinal}"
            record_type = "chapter_note_continuation"
        else:
            anchor = f"Chapter {chapter} general note {note_ordinal}"
            record_type = "chapter_note_general"
        pages = block.get("page_numbers") or [1]
        records.append(
            {
                "record_id": f"{profile.output_stem.upper()}_NOTE_{note_ordinal:04d}",
                "source_id": profile.source_id,
                "source_title": profile.title,
                "compiler_profile": profile.compiler_profile,
                "jurisdiction": profile.jurisdiction,
                "authority_class": profile.authority_class,
                "record_type": record_type,
                "legal_anchor": anchor,
                "chapter": chapter,
                "note_number": current_note,
                "description": text,
                "source_excerpt": text,
                "source_locator": {
                    "pages": pages,
                    "block_id": block.get("id"),
                },
                "review_flags": [],
                "ordinal": note_ordinal,
            }
        )
        note_ordinal += 1
    return records


def _pdf_text_blocks(pdf_path: Path) -> list[dict[str, Any]]:
    try:
        import fitz  # type: ignore[import-not-found]
    except Exception as exc:
        raise RuntimeError("PyMuPDF is required to compile WCO GRI rule records.") from exc
    blocks: list[dict[str, Any]] = []
    with fitz.open(pdf_path) as document:
        for page_index, page in enumerate(document, start=1):
            for block_index, raw in enumerate(sorted(page.get_text("blocks"), key=lambda item: (item[1], item[0])), start=1):
                x0, y0, x1, y1, text, *_ = raw
                cleaned = _normalize_space(text)
                if cleaned:
                    blocks.append(
                        {
                            "page": page_index,
                            "block_index": block_index,
                            "bbox": [round(float(x0), 1), round(float(y0), 1), round(float(x1), 1), round(float(y1), 1)],
                            "text": cleaned,
                        }
                    )
    return blocks


def _parsed_json_text_blocks(parsed_json_path: Path) -> list[dict[str, Any]]:
    parsed = _load_json(parsed_json_path)
    blocks: list[dict[str, Any]] = []
    gri_prefixes = iter(["1. ", "2. ", "", "3. ", "", "", "", "4. ", "5. ", "", "", "6. "])
    for index, block in enumerate(parsed.get("content", {}).get("blocks", []), start=1):
        text = _normalize_space(block.get("text", ""))
        if not text:
            continue
        if "wco_gri_rules" in parsed_json_path.name and block.get("type") == "list_item":
            prefix = next(gri_prefixes, "")
            if prefix and not re.match(r"^[1-6]\.", text):
                text = prefix + text
        pages = block.get("page_numbers") or [1]
        blocks.append(
            {
                "page": int(pages[0]),
                "block_index": index,
                "bbox": block.get("bbox"),
                "text": text,
            }
        )
    return blocks


def _admit_tariff_node(node: dict[str, Any]) -> bool:
    text = _normalize_space(node.get("description", ""))
    if not text:
        return False
    if text.lower().startswith(("contents", "page")):
        return False
    return True


def _wco_description(cells: list[str], heading_cell: str, hs_cell: str) -> str:
    parts = []
    for cell in cells:
        if cell and cell not in {heading_cell, hs_cell}:
            parts.append(cell)
    return _normalize_space(" ".join(parts))


def _chapter_from_profile(profile: SourceProfile) -> str:
    match = re.search(r"section_(\d{2})", profile.output_stem)
    return match.group(1) if match else ""


def _dash_depth(description: str) -> int:
    return len(re.match(r"^\s*(-+)", description or "").group(1)) if re.match(r"^\s*(-+)", description or "") else 0


def _clean_description(description: str) -> str:
    return _normalize_space(re.sub(r"\.{4,}", "", description))


def _normalize_code(code: str) -> str:
    return re.sub(r"\D", "", code or "")


def _normalize_space(text: Any) -> str:
    return " ".join(str(text or "").replace("\xa0", " ").split())


def _clean_header(header: str | None) -> str:
    return str(header or "").strip().strip('"').strip().replace(" ", "_")


def _slug(text: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_").upper()
    return slug or "UNNAMED"


def _has_code_signal(text: str) -> bool:
    return bool(re.search(r"\b(?:\d{2}\.\d{2}|\d{4}\.\d{2}|\d{4}(?:\s+\d{2}){1,3})\b", text))


def _table_header_signal(blocks: list[str]) -> bool:
    joined = " ".join(blocks[:12]).lower()
    return ("heading" in joined and "h.s. code" in joined) or ("cn code" in joined and "description" in joined)


def _infer_layout_type(profile: SourceProfile, samples: list[dict[str, Any]]) -> str:
    if profile.source_type == "two_column_code_note_pdf":
        return "two-column code/note layout"
    if profile.source_type == "tariff_table_pdf":
        return "tariff table"
    if profile.source_type == "wco_heading_table_pdf":
        return "WCO heading-code table"
    if profile.source_type == "single_flow_legal_text_pdf":
        return "single-flow legal text"
    if any(sample.get("table_header_signal") for sample in samples):
        return "table-like legal source"
    return profile.source_type


def _bti_review_flags(row: dict[str, str]) -> list[str]:
    flags = []
    for required in ["BTI_REFERENCE", "NOMENCLATURE_CODE", "CLASSIFICATION_JUSTIFICATION", "DESCRIPTION_OF_GOODS"]:
        if not row.get(required):
            flags.append(f"missing_{required.lower()}")
    return flags


def _explanatory_anchor(record: dict[str, Any]) -> str:
    if record.get("code_range"):
        code_range = record["code_range"]
        return f"{code_range['start']} {code_range['connector']} {code_range['end']}"
    return record.get("cn_code") or record.get("heading_code") or f"Chapter {record.get('chapter')} general"


def _qc_for_records(records: list[CodeRecord]) -> dict[str, Any]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    flag_counts: dict[str, int] = {}
    missing_locator: list[str] = []
    for record in records:
        record_id = record["record_id"]
        if record_id in seen:
            duplicates.add(record_id)
            record.setdefault("review_flags", []).append("duplicate_record_id")
        seen.add(record_id)
        if not record.get("source_locator") and not record.get("source_bbox"):
            missing_locator.append(record_id)
            record.setdefault("review_flags", []).append("missing_source_locator")
        for flag in record.get("review_flags", []):
            flag_counts[flag] = flag_counts.get(flag, 0) + 1
    return {
        "record_count": len(records),
        "duplicate_record_ids": sorted(duplicates),
        "missing_source_locator_record_ids": missing_locator,
        "review_flag_counts": dict(sorted(flag_counts.items())),
    }


def render_records_markdown(profile: SourceProfile, records: list[CodeRecord]) -> str:
    lines = [
        f"# {profile.title} Records",
        "",
        "> Layout-aware legal source layer. This file is generated from structured records and should be used for review instead of the generic OCR Markdown projection.",
        "",
        f"- Source ID: `{profile.source_id}`",
        f"- Compiler profile: `{profile.compiler_profile}`",
        f"- Authority class: `{profile.authority_class}`",
        f"- Record count: `{len(records)}`",
        "",
        "| Record ID | Anchor | Type | Page/Row | Flags |",
        "| --- | --- | --- | --- | --- |",
    ]
    for record in records:
        locator = record.get("source_locator", {})
        page_or_row = locator.get("page") or locator.get("pages") or locator.get("csv_row_number") or ""
        if isinstance(page_or_row, list):
            page_or_row = ",".join(str(item) for item in page_or_row)
        flags = ", ".join(record.get("review_flags") or [])
        lines.append(
            f"| `{record['record_id']}` | `{_escape_table(str(record.get('legal_anchor') or ''))}` | `{record.get('record_type')}` | {page_or_row} | {_escape_table(flags)} |"
        )
    lines.extend(["", "---", ""])
    for record in records:
        lines.append(f"## Record `{record['record_id']}`")
        lines.append("")
        lines.append("```text")
        for key in [
            "record_id",
            "source_id",
            "compiler_profile",
            "jurisdiction",
            "authority_class",
            "record_type",
            "legal_anchor",
            "code",
            "heading_code",
            "rule_id",
            "bti_reference",
            "hierarchy_depth",
            "parent_code",
            "parent_record_id",
        ]:
            if key in record:
                lines.append(f"{key}: {record.get(key)}")
        lines.append(f"source_locator: {json.dumps(record.get('source_locator', {}), ensure_ascii=False)}")
        lines.append(f"review_flags: {', '.join(record.get('review_flags') or []) or 'none'}")
        lines.append("```")
        lines.append("")
        body = (
            record.get("description")
            or record.get("legal_text")
            or record.get("note_text")
            or record.get("goods_description")
            or record.get("title")
            or ""
        )
        lines.append("**Legal Text / Description**")
        lines.append("")
        lines.append(str(body))
        if record.get("classification_justification"):
            lines.append("")
            lines.append("**Classification Justification**")
            lines.append("")
            lines.append(str(record["classification_justification"]))
        lines.append("")
        lines.append("**Source Excerpt**")
        lines.append("")
        lines.append(str(record.get("source_excerpt") or ""))
        lines.append("")
    return "\n".join(lines)


def _escape_table(text: str) -> str:
    return _normalize_space(text).replace("|", "\\|")


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _require(value: str | None) -> str:
    if not value:
        raise ValueError("Required profile path is missing.")
    return value
