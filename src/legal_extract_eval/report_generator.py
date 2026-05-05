from __future__ import annotations

import json
from typing import Iterable

from .models import EvaluationResult


REPORT_COLUMNS = (
    "scenario_id",
    "artifact_id",
    "fixture_class",
    "artifact_type",
    "agent_stage",
    "jurisdiction",
    "candidate_hs_code",
    "candidate_cn_code",
    "authority_status",
    "provenance_status",
    "source_integrity_status",
    "quote_fidelity_status",
    "capture_status",
    "representation_status",
    "legal_method_status",
    "graph_parity_status",
    "synthesis_status",
    "uncertainty_status",
    "handoff_status",
    "failed_checks",
    "severity",
    "expected_route",
    "actual_route",
    "human_review_required",
    "recommended_action",
)


def control_profile_rows(results: Iterable[EvaluationResult]) -> list[dict]:
    return [
        {
            "scenario_id": result.scenario_id,
            "artifact_id": result.artifact_id,
            "fixture_class": result.fixture_class,
            "artifact_type": result.artifact_type,
            "agent_stage": result.agent_stage,
            "jurisdiction": result.jurisdiction,
            "candidate_hs_code": result.candidate_hs_code or "",
            "candidate_cn_code": result.candidate_cn_code or "",
            "authority_status": result.authority_status,
            "provenance_status": result.provenance_status,
            "source_integrity_status": result.source_integrity_status,
            "quote_fidelity_status": result.quote_fidelity_status,
            "capture_status": result.capture_status,
            "representation_status": result.representation_status,
            "legal_method_status": result.legal_method_status,
            "graph_parity_status": result.graph_parity_status,
            "synthesis_status": result.synthesis_status,
            "uncertainty_status": result.uncertainty_status,
            "handoff_status": result.handoff_status,
            "failed_checks": ";".join(result.failed_checks),
            "severity": result.severity,
            "expected_route": result.expected_route,
            "actual_route": result.actual_route,
            "human_review_required": result.human_review_required,
            "recommended_action": result.recommended_action,
        }
        for result in results
    ]


def render_markdown(results: Iterable[EvaluationResult]) -> str:
    result_list = list(results)
    rows = control_profile_rows(result_list)
    lines = ["# Control Profile Report", ""]
    lines.append("| " + " | ".join(REPORT_COLUMNS) + " |")
    lines.append("| " + " | ".join("---" for _ in REPORT_COLUMNS) + " |")
    for row in rows:
        rendered = [str(row[column]) for column in REPORT_COLUMNS]
        lines.append("| " + " | ".join(rendered) + " |")
    lines.append("")
    total = len(rows)
    passed = sum(1 for result in result_list if result.passed_gold)
    lines.append(f"Gold conformance: {passed}/{total}")
    return "\n".join(lines)


def render_json(results: Iterable[EvaluationResult]) -> str:
    return json.dumps([result.as_row() for result in results], indent=2, sort_keys=True)
