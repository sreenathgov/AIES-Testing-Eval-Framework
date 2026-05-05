from __future__ import annotations

import argparse
from pathlib import Path

from .evaluator import Evaluator
from .pre_hs_slice import evaluate_run, write_run_reports
from .report_generator import render_json, render_markdown


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the offline legal extraction control profile.")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--run-id", help="Evaluate a generated pre-HS slice run under runs/<run-id>.")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of markdown.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.run_id:
        rows = evaluate_run(args.repo_root, args.run_id)
        write_run_reports(args.repo_root, args.run_id, rows)
        if args.json:
            import json

            print(json.dumps(rows, indent=2, sort_keys=True))
        else:
            report = args.repo_root / "runs" / args.run_id / "reports" / "control_profile.md"
            print(report.read_text(encoding="utf-8"))
        return 0 if all(row["expected_route"] == row["actual_route"] for row in rows) else 1

    evaluator = Evaluator.from_repo(args.repo_root)
    results = evaluator.evaluate_all()
    print(render_json(results) if args.json else render_markdown(results))
    return 0 if all(result.passed_gold for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
