from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


CODE_RE = re.compile(r"^\d{4}(?:\s+\d{2}(?:\s+\d{2})?)?$")
CODE_PREFIX_RE = re.compile(
    r"^(?P<start>\d{4}(?:\s+\d{2}(?:\s+\d{2})?)?)"
    r"(?:\s+(?P<connector>to|and)\s+(?P<end>\d{4}(?:\s+\d{2}(?:\s+\d{2})?)?))?"
    r"(?:\s+(?P<title>.+))?$",
    re.IGNORECASE,
)
CHAPTER_RE = re.compile(r"^CHAPTER\s+(?P<chapter>\d{1,2})$")
FURNITURE_RE = re.compile(
    r"^(?:C\s+\d+/\d+|L\s+\d+/\d+|EN|Official Journal of the European Union|"
    r"\d{1,2}\.\d{1,2}\.\d{4}|Page)$",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class LayoutConfig:
    code_column_max_x: float = 120.0
    text_column_min_x: float = 125.0
    header_max_y: float = 65.0
    footer_min_y: float = 815.0
    same_band_tolerance: float = 18.0


@dataclass(frozen=True)
class LayoutBlock:
    page: int
    x0: float
    y0: float
    x1: float
    y1: float
    text: str
    block_index: int

    @property
    def bbox(self) -> list[float]:
        return [round(self.x0, 1), round(self.y0, 1), round(self.x1, 1), round(self.y1, 1)]

    @property
    def zone(self) -> str:
        if self.x0 < 120:
            return "code_column"
        if self.x0 >= 125:
            return "text_column"
        return "bridge"


def normalize_space(text: str) -> str:
    return " ".join(str(text or "").split())


def normalize_code(code: str | None) -> str | None:
    if not code:
        return None
    return normalize_space(code)


def code_to_id(code: str) -> str:
    return normalize_code(code).replace(" ", "_")  # type: ignore[union-attr]


def parse_code_anchor(text: str) -> dict[str, Any] | None:
    text = normalize_space(text)
    match = CODE_PREFIX_RE.match(text)
    if not match:
        return None
    start = normalize_code(match.group("start"))
    end = normalize_code(match.group("end"))
    connector = match.group("connector")
    title = normalize_space(match.group("title") or "")
    if not start or not CODE_RE.match(start):
        return None
    if end and not CODE_RE.match(end):
        return None
    return {
        "start": start,
        "end": end,
        "connector": connector.lower() if connector else None,
        "title": title,
        "is_range": bool(end),
        "is_heading": bool(re.fullmatch(r"\d{4}", start)),
    }


def extract_layout_blocks(pdf_path: Path, config: LayoutConfig = LayoutConfig()) -> list[LayoutBlock]:
    try:
        import fitz  # type: ignore[import-not-found]
    except Exception as exc:  # pragma: no cover - environment guard
        raise RuntimeError("PyMuPDF is required for EU CN layout parsing. Install pymupdf.") from exc

    blocks: list[LayoutBlock] = []
    with fitz.open(pdf_path) as document:
        for page_index, page in enumerate(document, start=1):
            raw_blocks = page.get_text("blocks")
            for block_index, raw in enumerate(sorted(raw_blocks, key=lambda item: (item[1], item[0])), start=1):
                x0, y0, x1, y1, text, *_ = raw
                cleaned = normalize_space(text)
                if not cleaned:
                    continue
                block = LayoutBlock(
                    page=page_index,
                    x0=float(x0),
                    y0=float(y0),
                    x1=float(x1),
                    y1=float(y1),
                    text=cleaned,
                    block_index=block_index,
                )
                if is_furniture(block, config):
                    continue
                blocks.append(block)
    return blocks


def is_furniture(block: LayoutBlock, config: LayoutConfig = LayoutConfig()) -> bool:
    text = normalize_space(block.text)
    if block.y0 <= config.header_max_y or block.y0 >= config.footer_min_y:
        return True
    if FURNITURE_RE.match(text):
        return True
    if "Official Journal of the European Union" in text and block.y0 < 80:
        return True
    return False


def _empty_record(
    *,
    anchor: dict[str, Any],
    block: LayoutBlock,
    chapter: str | None,
    heading_context: str | None,
    title: str,
    config: LayoutConfig,
) -> dict[str, Any]:
    start = anchor["start"]
    end = anchor.get("end")
    if anchor.get("is_heading"):
        heading_context = start
    record_id = f"EU_CN_EN_{code_to_id(start)}"
    if end:
        record_id += f"_{anchor['connector'].upper()}_{code_to_id(end)}"
    code_bbox = block.bbox
    title_bbox = None
    if title and block.x1 > config.text_column_min_x:
        code_bbox = [round(block.x0, 1), round(block.y0, 1), round(config.code_column_max_x, 1), round(block.y1, 1)]
        title_bbox = [round(config.text_column_min_x, 1), round(block.y0, 1), round(block.x1, 1), round(block.y1, 1)]
    return {
        "record_id": record_id,
        "chapter": chapter,
        "heading_code": start if anchor.get("is_heading") else heading_context,
        "cn_code": None if end or anchor.get("is_heading") else start,
        "code_range": {
            "start": start,
            "end": end,
            "connector": anchor.get("connector"),
        }
        if end
        else None,
        "title": title,
        "note_text": "",
        "page": block.page,
        "pages": [block.page],
        "source_bbox": {
            "code_column": code_bbox,
            "text_column": title_bbox,
        },
        "source_blocks": [
            {
                "page": block.page,
                "bbox": block.bbox,
                "zone": block.zone,
                "text": block.text,
            }
        ],
        "source_excerpt": block.text,
        "source_engine": {
            "layout": "pymupdf",
            "ocr_text": "mistral_ocr",
        },
        "review_flags": [],
    }


def _empty_chapter_record(chapter: str, block: LayoutBlock) -> dict[str, Any]:
    return {
        "record_id": f"EU_CN_EN_CHAPTER_{chapter}_GENERAL",
        "chapter": chapter,
        "heading_code": None,
        "cn_code": None,
        "code_range": None,
        "title": "",
        "note_text": "",
        "page": block.page,
        "pages": [block.page],
        "source_bbox": {
            "code_column": block.bbox,
            "text_column": None,
        },
        "source_blocks": [
            {
                "page": block.page,
                "bbox": block.bbox,
                "zone": block.zone,
                "text": block.text,
            }
        ],
        "source_excerpt": block.text,
        "source_engine": {
            "layout": "pymupdf",
            "ocr_text": "mistral_ocr",
        },
        "review_flags": ["chapter_general_record"],
    }


def compile_layout_records(
    blocks: Iterable[LayoutBlock],
    *,
    ocr_pages: dict[int, str] | None = None,
    config: LayoutConfig = LayoutConfig(),
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    records: list[dict[str, Any]] = []
    qc = {
        "record_count": 0,
        "review_flag_counts": {},
        "unattached_blocks": [],
        "duplicate_record_ids": [],
    }
    current: dict[str, Any] | None = None
    chapter: str | None = None
    heading_context: str | None = None

    for block in sorted(blocks, key=lambda item: (item.page, item.y0, item.x0)):
        if is_furniture(block, config):
            continue

        chapter_match = CHAPTER_RE.match(block.text)
        if chapter_match:
            chapter = chapter_match.group("chapter")
            current = _empty_chapter_record(chapter, block)
            records.append(current)
            continue

        anchor = parse_code_anchor(block.text)
        if anchor and block.x0 <= config.code_column_max_x:
            current = _empty_record(
                anchor=anchor,
                block=block,
                chapter=chapter,
                heading_context=heading_context,
                title=anchor.get("title") or "",
                config=config,
            )
            if anchor.get("is_heading"):
                heading_context = anchor["start"]
            records.append(current)
            if current["title"] and not _text_supported_by_ocr(current["title"], block.page, ocr_pages):
                current["review_flags"].append("text_reconciliation_required")
            continue

        if current is None:
            qc["unattached_blocks"].append(
                {"page": block.page, "bbox": block.bbox, "text": block.text}
            )
            continue

        _attach_text_block(current, block, ocr_pages=ocr_pages)

    _finalize_records(records)
    _populate_qc(qc, records)
    return records, qc


def _attach_text_block(
    record: dict[str, Any],
    block: LayoutBlock,
    *,
    ocr_pages: dict[int, str] | None,
) -> None:
    text = block.text
    if not record["title"]:
        record["title"] = text
        record["source_bbox"]["text_column"] = block.bbox
    elif _is_same_y_band(record["source_bbox"]["code_column"], block.bbox) and not record["note_text"]:
        if record["title"] == record["source_blocks"][0]["text"]:
            record["title"] = text
        else:
            record["note_text"] = _append_text(record["note_text"], text)
        record["source_bbox"]["text_column"] = record["source_bbox"]["text_column"] or block.bbox
    else:
        record["note_text"] = _append_text(record["note_text"], text)
        record["source_bbox"]["text_column"] = record["source_bbox"]["text_column"] or block.bbox

    record["pages"] = sorted(set(record["pages"] + [block.page]))
    record["source_blocks"].append(
        {
            "page": block.page,
            "bbox": block.bbox,
            "zone": block.zone,
            "text": text,
        }
    )
    record["source_excerpt"] = _append_text(record["source_excerpt"], text)
    if not _text_supported_by_ocr(text, block.page, ocr_pages):
        record["review_flags"].append("text_reconciliation_required")


def _append_text(existing: str, addition: str) -> str:
    existing = normalize_space(existing)
    addition = normalize_space(addition)
    if not existing:
        return addition
    if existing.endswith("-"):
        return existing[:-1] + addition
    return f"{existing} {addition}"


def _is_same_y_band(code_bbox: list[float], text_bbox: list[float], tolerance: float = 18.0) -> bool:
    return abs(code_bbox[1] - text_bbox[1]) <= tolerance


def _text_supported_by_ocr(text: str, page: int, ocr_pages: dict[int, str] | None) -> bool:
    if not ocr_pages:
        return True
    needle = re.sub(r"\W+", "", text).lower()
    haystack = re.sub(r"\W+", "", ocr_pages.get(page, "")).lower()
    if not needle:
        return True
    return needle[:80] in haystack


def _finalize_records(records: list[dict[str, Any]]) -> None:
    for record in records:
        record["review_flags"] = sorted(set(record["review_flags"]))
        if record["source_bbox"]["text_column"] is None:
            record["review_flags"].append("record_lacks_text_column_bbox")
        if not record["page"] or not record["source_bbox"]["code_column"]:
            record["review_flags"].append("record_lacks_page_or_code_bbox")
        if record["code_range"] and not record["code_range"]["end"]:
            record["review_flags"].append("code_range_split_incorrectly")
        if record["heading_code"] and record["cn_code"] and record["heading_code"] == record["cn_code"]:
            record["review_flags"].append("four_digit_heading_treated_as_cn_code")
        record["review_flags"] = sorted(set(record["review_flags"]))


def _populate_qc(qc: dict[str, Any], records: list[dict[str, Any]]) -> None:
    seen: set[str] = set()
    duplicates: set[str] = set()
    flag_counts: dict[str, int] = {}
    for record in records:
        record_id = record["record_id"]
        if record_id in seen:
            duplicates.add(record_id)
            record["review_flags"].append("duplicate_record_id")
        seen.add(record_id)
        for flag in record["review_flags"]:
            flag_counts[flag] = flag_counts.get(flag, 0) + 1
    qc["record_count"] = len(records)
    qc["review_flag_counts"] = dict(sorted(flag_counts.items()))
    qc["duplicate_record_ids"] = sorted(duplicates)


def ocr_pages_from_canonical(canonical_json_path: Path) -> dict[int, str]:
    data = json.loads(canonical_json_path.read_text(encoding="utf-8"))
    pages: dict[int, list[str]] = {}
    for block in data.get("content", {}).get("blocks", []):
        for page in block.get("page_numbers", []) or []:
            pages.setdefault(int(page), []).append(str(block.get("text", "")))
    return {page: "\n".join(texts) for page, texts in pages.items()}


def render_layout_review(records: list[dict[str, Any]]) -> str:
    lines = [
        "# EU CN Explanatory Notes Layout Records",
        "",
        "> Layout-aware legal source layer. This file is generated from structured records and should be used for review instead of the generic OCR Markdown projection.",
        "",
        "| Record ID | Page | Legal anchor | Title | Flags |",
        "| --- | ---: | --- | --- | --- |",
    ]
    for record in records:
        anchor = _record_anchor_label(record)
        title = _escape_table(record.get("title") or "")
        flags = ", ".join(record.get("review_flags") or [])
        lines.append(
            f"| `{record['record_id']}` | {record.get('page')} | `{anchor}` | {title} | {flags} |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")
    for record in records:
        code_label = _record_anchor_label(record)
        lines.append(f"## Record `{record['record_id']}`")
        lines.append("")
        lines.append("```text")
        lines.append(f"record_id: {record['record_id']}")
        lines.append(f"page: {record.get('page')}")
        lines.append(f"pages: {', '.join(str(page) for page in record.get('pages', []))}")
        lines.append(f"chapter: {record.get('chapter')}")
        lines.append(f"heading_context: {record.get('heading_code')}")
        lines.append(f"cn_code: {record.get('cn_code')}")
        lines.append(f"code_or_range: {code_label}")
        lines.append(f"source_bbox.code_column: {record.get('source_bbox', {}).get('code_column')}")
        lines.append(f"source_bbox.text_column: {record.get('source_bbox', {}).get('text_column')}")
        if record.get("review_flags"):
            lines.append(f"review_flags: {', '.join(record['review_flags'])}")
        else:
            lines.append("review_flags: none")
        lines.append("```")
        lines.append("")
        lines.append("**Title**")
        lines.append("")
        lines.append(record.get("title") or "")
        lines.append("")
        lines.append("**Note Text**")
        lines.append("")
        lines.append(record.get("note_text") or "")
        lines.append("")
        lines.append("**Source Excerpt**")
        lines.append("")
        lines.append(record.get("source_excerpt") or "")
        lines.append("")
    return "\n".join(lines)


def _record_anchor_label(record: dict[str, Any]) -> str:
    code = record["code_range"] or record["cn_code"] or record["heading_code"]
    if isinstance(code, dict):
        return f"{code['start']} {code['connector']} {code['end']}"
    if code:
        return str(code)
    if record.get("chapter"):
        return f"Chapter {record['chapter']} general"
    return "unanchored"


def _escape_table(text: str) -> str:
    return normalize_space(text).replace("|", "\\|")
