from __future__ import annotations

import argparse
from pathlib import Path

from legal_extract_eval.pre_hs_slice import build_pre_hs_slice


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build the bounded pre-HS legal extraction harness slice.")
    parser.add_argument("--source-repo-root", type=Path, required=True)
    parser.add_argument("--harness-root", type=Path, default=Path.cwd())
    parser.add_argument("--no-frozen-run", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    build_pre_hs_slice(
        args.harness_root.resolve(),
        args.source_repo_root.resolve(),
        create_frozen_run=not args.no_frozen_run,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
