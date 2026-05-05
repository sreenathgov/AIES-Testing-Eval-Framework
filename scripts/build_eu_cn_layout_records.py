from __future__ import annotations

import argparse
import json
from pathlib import Path

from legal_extract_eval.eu_cn_layout_parser import (
    LayoutConfig,
    compile_layout_records,
    extract_layout_blocks,
    ocr_pages_from_canonical,
    render_layout_review,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build layout-aware EU CN Explanatory Notes records from PDF geometry and Mistral canonical JSON."
    )
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--code-column-max-x", type=float, default=120.0)
    parser.add_argument("--text-column-min-x", type=float, default=125.0)
    parser.add_argument("--header-max-y", type=float, default=65.0)
    parser.add_argument("--footer-min-y", type=float, default=815.0)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    repo_root = args.repo_root.resolve()
    pdf_path = repo_root / "data/source_corpus/originals/eu/eu_cn_explanatory_notes_evs.pdf"
    canonical_json_path = repo_root / "data/source_corpus/parsed_v2/eu/eu_cn_explanatory_notes_evs.json"
    output_dir = repo_root / "data/source_corpus/parsed_v2/eu"
    output_dir.mkdir(parents=True, exist_ok=True)

    config = LayoutConfig(
        code_column_max_x=args.code_column_max_x,
        text_column_min_x=args.text_column_min_x,
        header_max_y=args.header_max_y,
        footer_min_y=args.footer_min_y,
    )
    blocks = extract_layout_blocks(pdf_path, config=config)
    records, qc = compile_layout_records(
        blocks,
        ocr_pages=ocr_pages_from_canonical(canonical_json_path),
        config=config,
    )

    records_path = output_dir / "eu_cn_explanatory_notes_evs_layout_records.json"
    records_markdown_path = output_dir / "eu_cn_explanatory_notes_evs_layout_records.md"
    review_path = output_dir / "eu_cn_explanatory_notes_evs_layout_review.md"
    qc_path = output_dir / "eu_cn_explanatory_notes_evs_layout_qc.json"

    review_markdown = render_layout_review(records)
    records_path.write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    records_markdown_path.write_text(review_markdown, encoding="utf-8")
    review_path.write_text(review_markdown, encoding="utf-8")
    qc_path.write_text(json.dumps(qc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "records": str(records_path),
                "records_markdown": str(records_markdown_path),
                "review": str(review_path),
                "qc": str(qc_path),
                "record_count": len(records),
                "review_flag_counts": qc["review_flag_counts"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
