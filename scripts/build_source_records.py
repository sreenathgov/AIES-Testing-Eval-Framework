from __future__ import annotations

import argparse
import json
from pathlib import Path

from legal_extract_eval.source_compilers import build_all_source_outputs


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build legal-safe source record layers for all HS source-corpus documents."
    )
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    repo_root = args.repo_root.resolve()
    manifest = build_all_source_outputs(repo_root)
    print(
        json.dumps(
            {
                "manifest": "data/source_corpus/SOURCE_RECORD_PROFILE_MANIFEST.json",
                "compiled_outputs": manifest["compiled_outputs"],
            },
            indent=2,
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
