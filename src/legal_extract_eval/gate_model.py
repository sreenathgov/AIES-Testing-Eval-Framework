from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any


GATE_REPORT_COLUMNS = (
    "scenario_id",
    "artifact_id",
    "component_id",
    "actual_route",
    "severity",
    "gate_id",
    "gate_label",
    "gate_reason_codes",
)


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def classify_gate(row: dict[str, Any]) -> dict[str, Any]:
    failed_checks = set(row.get("failed_checks", []))
    route = row.get("actual_route")
    severity = row.get("severity")

    rerun_checks = {
        "missing_graph_relationship",
        "graph_parity_failure",
        "edge_direction_invalid",
        "edge_endpoint_unresolved",
        "malformed_graph_node",
        "missing_required_handoff_field",
        "rerun_delta_threshold_breach",
    }
    research_checks = {
        "missing_legal_authority_chain",
        "missing_external_authority",
        "missing_source_anchor",
        "source_anchor_not_resolved",
        "document_level_only_source_anchor",
        "internal_source_as_authority",
        "required_authority_class_missing",
        "secondary_only_authority_chain",
        "evidence_gap",
        "corpus_gap",
        "unsupported_promotion",
    }

    if failed_checks & rerun_checks or row.get("graph_parity_status") == "fail":
        return {
            "gate_id": "gate_4",
            "gate_label": "blocked_pending_rerun",
            "gate_reason_codes": sorted(failed_checks & rerun_checks) or ["graph_or_rerun_failure"],
        }
    if route in {"blocked", "unresolved"} or severity == "blocker" or failed_checks & research_checks:
        return {
            "gate_id": "gate_3",
            "gate_label": "blocked_pending_research",
            "gate_reason_codes": sorted(failed_checks & research_checks) or ["research_or_authority_gap"],
        }
    if route == "review" or severity == "review_trigger" or failed_checks:
        return {
            "gate_id": "gate_2",
            "gate_label": "pass_with_notes",
            "gate_reason_codes": sorted(failed_checks) or ["review_route_declared"],
        }
    return {
        "gate_id": "gate_1",
        "gate_label": "pass",
        "gate_reason_codes": [],
    }


def attach_gate_fields(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    enriched: list[dict[str, Any]] = []
    for row in rows:
        gate = classify_gate(row)
        enriched.append(row | gate)
    return enriched


def write_gate_reports(repo_root: Path, run_id: str, rows: list[dict[str, Any]]) -> None:
    report_dir = repo_root / "runs" / run_id / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    gate_rows = [
        {
            "scenario_id": row["scenario_id"],
            "artifact_id": row["artifact_id"],
            "component_id": row["component_id"],
            "actual_route": row["actual_route"],
            "severity": row["severity"],
            "gate_id": row["gate_id"],
            "gate_label": row["gate_label"],
            "gate_reason_codes": row["gate_reason_codes"],
        }
        for row in rows
    ]
    write_json(report_dir / "gate_summary.json", gate_rows)
    with (report_dir / "gate_summary.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=GATE_REPORT_COLUMNS)
        writer.writeheader()
        for row in gate_rows:
            encoded = dict(row)
            encoded["gate_reason_codes"] = ";".join(row.get("gate_reason_codes", []))
            writer.writerow({column: encoded.get(column, "") for column in GATE_REPORT_COLUMNS})
    lines = [
        "# Four-Gate Handoff Summary",
        "",
        "| " + " | ".join(GATE_REPORT_COLUMNS) + " |",
        "| " + " | ".join("---" for _ in GATE_REPORT_COLUMNS) + " |",
    ]
    for row in gate_rows:
        rendered = []
        for column in GATE_REPORT_COLUMNS:
            value = row.get(column, "")
            if isinstance(value, list):
                value = ";".join(value)
            rendered.append(str(value))
        lines.append("| " + " | ".join(rendered) + " |")
    lines.append("")
    counts: dict[str, int] = {}
    for row in gate_rows:
        counts[row["gate_label"]] = counts.get(row["gate_label"], 0) + 1
    lines.append("## Counts")
    for label, count in sorted(counts.items()):
        lines.append(f"- {label}: {count}")
    (report_dir / "gate_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
