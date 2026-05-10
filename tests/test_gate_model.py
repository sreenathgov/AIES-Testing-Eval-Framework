from __future__ import annotations

import json
from pathlib import Path

from legal_extract_eval.gate_model import classify_gate


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def test_four_gate_model_maps_core_routes() -> None:
    assert classify_gate({"actual_route": "promote", "severity": "pass", "failed_checks": []})["gate_label"] == "pass"
    assert classify_gate({"actual_route": "review", "severity": "review_trigger", "failed_checks": ["gri_3b_requires_adjudication_review"]})["gate_label"] == "pass_with_notes"
    assert classify_gate({"actual_route": "blocked", "severity": "blocker", "failed_checks": ["missing_source_anchor"]})["gate_label"] == "blocked_pending_research"
    assert classify_gate({"actual_route": "blocked", "severity": "blocker", "failed_checks": ["missing_graph_relationship"]})["gate_label"] == "blocked_pending_rerun"


def test_gate_reports_are_written_and_control_profile_has_gate_fields(repo_root: Path) -> None:
    report_dir = repo_root / "runs" / "paper_frozen_run" / "reports"
    for filename in ("gate_summary.json", "gate_summary.csv", "gate_summary.md"):
        assert (report_dir / filename).exists()

    control_rows = load_json(report_dir / "control_profile.json")
    gate_rows = load_json(report_dir / "gate_summary.json")
    assert len(control_rows) == 28
    assert len(gate_rows) == 28
    assert all(row["gate_id"] for row in control_rows)
    assert all(row["gate_label"] in {"pass", "pass_with_notes", "blocked_pending_research", "blocked_pending_rerun"} for row in control_rows)
    assert {row["gate_label"] for row in gate_rows}.issuperset({"pass", "pass_with_notes"})
