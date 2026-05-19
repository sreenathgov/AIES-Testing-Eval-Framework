from __future__ import annotations

import argparse
from pathlib import Path

from .pre_hs_slice import create_run, evaluate_run, write_run_reports


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Execute a deterministic EU HS extraction harness run.")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--run-id", required=True)
    parser.add_argument(
        "--mode",
        choices=("live", "template"),
        default="template",
        help="template is deterministic and API-free; live is reserved for API-backed agent execution.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.mode == "live":
        raise SystemExit(
            "API-backed live execution is intentionally not enabled by default. "
            "Use --mode template for the reproducible paper harness run."
        )
    create_run(args.repo_root, args.run_id, mode="fresh_template")
    rows = evaluate_run(args.repo_root, args.run_id)
    write_run_reports(args.repo_root, args.run_id, rows)
    print(f"Created run {args.run_id} with {len(rows)} evaluated AA artifacts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
