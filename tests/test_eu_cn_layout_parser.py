from __future__ import annotations

import json
from pathlib import Path

from legal_extract_eval.eu_cn_layout_parser import (
    LayoutBlock,
    compile_layout_records,
    is_furniture,
    parse_code_anchor,
    render_layout_review,
)


def _block(page: int, x0: float, y0: float, x1: float, y1: float, text: str, index: int) -> LayoutBlock:
    return LayoutBlock(page=page, x0=x0, y0=y0, x1=x1, y1=y1, text=text, block_index=index)


def test_code_pattern_detection() -> None:
    heading = parse_code_anchor("8407 Spark-ignition reciprocating or rotary internal combustion piston engines")
    range_anchor = parse_code_anchor("8407 21 10 to 8407 29 00")
    conjunction = parse_code_anchor("8411 11 00 and 8411 12 80")

    assert heading is not None
    assert heading["start"] == "8407"
    assert heading["is_heading"] is True
    assert heading["title"].startswith("Spark-ignition")
    assert range_anchor is not None
    assert range_anchor["start"] == "8407 21 10"
    assert range_anchor["end"] == "8407 29 00"
    assert range_anchor["connector"] == "to"
    assert conjunction is not None
    assert conjunction["connector"] == "and"


def test_page_furniture_detection() -> None:
    assert is_furniture(_block(14, 41.8, 41.9, 553.4, 53.0, "C 119/326 EN Official Journal of the European Union 29.3.2019", 1))
    assert not is_furniture(_block(14, 41.8, 511.5, 452.8, 521.1, "8407 Spark-ignition reciprocating or rotary internal combustion piston engines", 2))


def test_page_14_golden_layout_records() -> None:
    blocks = [
        _block(14, 41.8, 41.9, 553.4, 53.0, "C 119/326 EN Official Journal of the European Union 29.3.2019", 1),
        _block(14, 268.9, 77.4, 326.4, 88.0, "CHAPTER 84", 2),
        _block(14, 41.8, 359.4, 555.3, 379.4, "8405 Producer gas or water gas generators, with or without their purifiers; acetylene gas generators and similar water process gas generators, with or without their purifiers", 3),
        _block(14, 41.8, 408.2, 555.1, 426.1, "8405 10 00 Producer gas or water gas generators, with or without their purifiers; acetylene gas generators and similar water process gas generators, with or without their purifiers", 4),
        _block(14, 147.5, 433.3, 263.2, 441.8, "This subheading does not include:", 5),
        _block(14, 147.5, 449.0, 408.5, 457.5, "(a) town gas generators (coking ovens), as used in gasworks (heading 8417);", 6),
        _block(14, 147.5, 464.8, 555.1, 482.7, "(b) electrolytic gas generators (for example, for the generation of nitrogen dioxide, hydrogen sulphide or prussic acid, depending upon the electrolyte used) are to be classified in heading 8543.", 7),
        _block(14, 41.8, 511.5, 452.8, 521.1, "8407 Spark-ignition reciprocating or rotary internal combustion piston engines", 8),
        _block(14, 41.8, 549.9, 83.2, 577.1, "8407 21 10 to 8407 29 00", 9),
        _block(14, 147.5, 549.9, 245.3, 558.4, "Marine propulsion engines", 10),
        _block(14, 147.5, 565.7, 500.5, 574.2, "These subheadings do not cover engines used on board water craft for purposes other than propulsion.", 11),
        _block(14, 41.8, 606.0, 511.1, 615.5, "8408 Compression-ignition internal combustion piston engines (diesel or semi-diesel engines)", 12),
        _block(14, 41.8, 644.3, 83.2, 671.6, "8408 10 11 to 8408 10 99", 13),
        _block(14, 147.5, 644.3, 245.3, 652.8, "Marine propulsion engines", 14),
        _block(14, 147.5, 660.1, 381.1, 668.6, "See the explanatory note to subheadings 8407 21 10 to 8407 29 00.", 15),
        _block(14, 41.8, 700.4, 498.9, 710.0, "8409 Parts suitable for use solely or principally with the engines of heading 8407 or 8408", 16),
        _block(14, 147.5, 717.3, 555.1, 735.1, "In addition to the exclusions referred to in the HS Explanatory Note to heading 8409, the following are also excluded from this heading:", 17),
        _block(14, 147.5, 742.3, 393.9, 750.8, "(a) piping and tubing, of unhardened vulcanised rubber (heading 4009);", 18),
        _block(14, 147.5, 758.1, 354.6, 766.6, "(b) flexible tubing and piping, of base metal (heading 8307);", 19),
        _block(14, 147.5, 773.8, 521.6, 782.3, "(c) gaskets and similar joints (generally, classified according to their constituent material or in heading 8484).", 20),
    ]

    records, qc = compile_layout_records(blocks)
    by_id = {record["record_id"]: record for record in records}

    assert qc["unattached_blocks"] == []
    assert by_id["EU_CN_EN_8405_10_00"]["note_text"].startswith("This subheading does not include")
    assert by_id["EU_CN_EN_8407_21_10_TO_8407_29_00"]["title"] == "Marine propulsion engines"
    assert by_id["EU_CN_EN_8407_21_10_TO_8407_29_00"]["note_text"].startswith("These subheadings do not cover")
    assert by_id["EU_CN_EN_8408_10_11_TO_8408_10_99"]["code_range"]["end"] == "8408 10 99"
    assert "(a) piping" in by_id["EU_CN_EN_8409"]["note_text"]
    assert "(b) flexible" in by_id["EU_CN_EN_8409"]["note_text"]
    assert "(c) gaskets" in by_id["EU_CN_EN_8409"]["note_text"]
    assert "chapter_general_record" in by_id["EU_CN_EN_CHAPTER_84_GENERAL"]["review_flags"]


def test_page_15_continuation_record() -> None:
    records, _ = compile_layout_records(
        [
            _block(14, 268.9, 77.4, 326.4, 88.0, "CHAPTER 84", 1),
            _block(14, 41.8, 700.4, 498.9, 710.0, "8409 Parts suitable for use solely or principally with the engines of heading 8407 or 8408", 2),
            _block(15, 41.8, 86.2, 169.0, 94.7, "8409 99 00 Other", 3),
            _block(15, 147.5, 102.0, 555.1, 129.2, "This subheading does not include exhaust-gas turbochargers used to compress the atmospheric air needed for combustion.", 4),
        ]
    )

    record = next(item for item in records if item["record_id"] == "EU_CN_EN_8409_99_00")

    assert record["heading_code"] == "8409"
    assert record["cn_code"] == "8409 99 00"
    assert record["title"] == "Other"
    assert record["page"] == 15
    assert "exhaust-gas turbochargers" in record["note_text"]


def test_unattached_prose_is_reported() -> None:
    _, qc = compile_layout_records([
        _block(14, 147.5, 200.0, 500.0, 210.0, "This prose has no code anchor.", 1)
    ])

    assert qc["unattached_blocks"]
    assert qc["unattached_blocks"][0]["text"] == "This prose has no code anchor."


def test_ocr_layout_reconciliation_flag() -> None:
    records, qc = compile_layout_records(
        [
            _block(14, 41.8, 549.9, 83.2, 577.1, "8407 21 10 to 8407 29 00", 1),
            _block(14, 147.5, 549.9, 245.3, 558.4, "Marine propulsion engines", 2),
        ],
        ocr_pages={14: "unrelated OCR text"},
    )

    assert "text_reconciliation_required" in records[0]["review_flags"]
    assert qc["review_flag_counts"]["text_reconciliation_required"] == 1


def test_generated_layout_records_match_schema_shape(repo_root: Path) -> None:
    records_path = repo_root / "data/source_corpus/parsed_v2/eu/eu_cn_explanatory_notes_evs_layout_records.json"
    schema_path = repo_root / "protocol/schemas/eu_cn_explanatory_note_layout_record.schema.json"
    records = json.loads(records_path.read_text())
    schema = json.loads(schema_path.read_text())
    required = set(schema["required"])

    assert records
    for record in records:
        assert required.issubset(record), record["record_id"]
        assert record["source_engine"] == {"layout": "pymupdf", "ocr_text": "mistral_ocr"}
        assert record["page"] >= 1
        assert len(record["source_bbox"]["code_column"]) == 4


def test_chapter_transition_does_not_bleed_into_previous_chapter(repo_root: Path) -> None:
    records = json.loads(
        (repo_root / "data/source_corpus/parsed_v2/eu/eu_cn_explanatory_notes_evs_layout_records.json").read_text()
    )
    record = next(item for item in records if item["record_id"] == "EU_CN_EN_0102_90_91")

    assert "NUCLEAR REACTORS" not in record["note_text"]
    assert "CHAPTER 84" not in record["source_excerpt"]


def test_layout_markdown_reflects_structured_records(repo_root: Path) -> None:
    records = json.loads(
        (repo_root / "data/source_corpus/parsed_v2/eu/eu_cn_explanatory_notes_evs_layout_records.json").read_text()
    )
    subset = [record for record in records if record["record_id"] == "EU_CN_EN_8411_11_00_TO_8411_12_80"]
    markdown = render_layout_review(subset)

    assert "Layout-aware legal source layer" in markdown
    assert "code_or_range: 8411 11 00 to 8411 12 80" in markdown
    assert "heading_context: 8411" in markdown
    assert "cn_code: None" in markdown
    assert "**Note Text**" in markdown
    assert "after-burning auxiliary appliances" in markdown
