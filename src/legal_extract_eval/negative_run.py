from __future__ import annotations

import argparse
import csv
import json
import shutil
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from .gate_model import attach_gate_fields, write_gate_reports
from .metric_calculator import calculate_metric_summary, write_metric_reports
from .pre_hs_slice import RUN_REPORT_COLUMNS, stress_test_catalog
from .validator_driven_run import build_detection_matrix, detection_aggregates, evaluate_aa_run


NEGATIVE_REGISTRY_PATH = Path("data/negative_cases/negative_case_registry.json")
DETECTION_MATRIX_COLUMNS = (
    "negative_case_id",
    "case_bundle",
    "paper_failure_class",
    "perturbation_layer",
    "expected_failed_checks",
    "observed_failed_checks",
    "true_positive_checks",
    "false_positive_checks",
    "false_negative_checks",
    "precision",
    "recall",
    "f1",
    "expected_gate_label",
    "observed_gate_label",
    "gate_match",
    "legal_rationale",
)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat()


def load_negative_registry(repo_root: Path) -> dict[str, Any]:
    return read_json(repo_root / NEGATIVE_REGISTRY_PATH)


def validate_negative_registry(repo_root: Path, registry: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    cases = registry.get("cases", [])
    metric_ids = {metric["metric_id"] for metric in read_json(repo_root / "protocol" / "measurement_framework.json")["metrics"]}
    evidence_metric_ids = {
        entry["metric_id"]
        for entry in read_json(repo_root / "protocol" / "knowledge_evidence_registry.json")["entries"]
    }

    if len(cases) != 10:
        errors.append("negative_case_count_not_10")

    seen_case_ids: set[str] = set()
    covered_metrics: set[str] = set()
    allowed_gates = {"pass", "pass_with_notes", "blocked_pending_research", "blocked_pending_rerun"}
    required_fields = {
        "negative_case_id",
        "case_bundle",
        "paper_failure_class",
        "perturbation_layer",
        "base_component",
        "source_delta",
        "artifact_delta",
        "graph_delta",
        "expected_failed_metrics",
        "expected_failed_checks",
        "expected_gate_label",
        "legal_rationale",
        "knowledge_evidence_registry_links",
    }

    for case in cases:
        missing = sorted(required_fields - set(case))
        if missing:
            errors.append(f"{case.get('negative_case_id', 'unknown')}:missing_fields:{','.join(missing)}")
            continue
        case_id = case["negative_case_id"]
        if case_id in seen_case_ids:
            errors.append(f"{case_id}:duplicate_case_id")
        seen_case_ids.add(case_id)
        if case["expected_gate_label"] not in allowed_gates:
            errors.append(f"{case_id}:unknown_expected_gate")
        if not case["legal_rationale"].strip():
            errors.append(f"{case_id}:missing_legal_rationale")

        expected_metrics = set(case["expected_failed_metrics"])
        covered_metrics.update(expected_metrics)
        unknown_metrics = expected_metrics - metric_ids
        if unknown_metrics:
            errors.append(f"{case_id}:unknown_metrics:{','.join(sorted(unknown_metrics))}")

        missing_evidence_links = set(case["knowledge_evidence_registry_links"]) - evidence_metric_ids
        if missing_evidence_links:
            errors.append(f"{case_id}:missing_evidence_links:{','.join(sorted(missing_evidence_links))}")

    uncovered_metrics = metric_ids - covered_metrics
    if uncovered_metrics:
        errors.append(f"metric_coverage_incomplete:{','.join(sorted(uncovered_metrics))}")

    return errors


def create_negative_run(repo_root: Path, run_id: str, *, base_run: str = "paper_eval_20260520", overwrite: bool = False) -> list[dict[str, Any]]:
    registry = load_negative_registry(repo_root)
    errors = validate_negative_registry(repo_root, registry)
    if errors:
        raise ValueError("Negative registry validation failed: " + "; ".join(errors))

    run_root = repo_root / "runs" / run_id
    if run_root.exists():
        if not overwrite:
            raise FileExistsError(f"Run already exists: {run_root}")
        shutil.rmtree(run_root)

    cases = registry["cases"]
    create_case_artifacts(run_root, cases)
    write_negative_traces(run_root, run_id, cases)
    rows = evaluate_aa_run(repo_root, run_id, cohort="fault_injection")
    for row in rows:
        row["cohort"] = "fault_injection"
        row["negative_case_id"] = row["artifact_id"].removeprefix("NEG_AA_")
    write_control_reports(repo_root, run_id, rows)
    write_gate_reports(repo_root, run_id, rows)
    metric_rows = calculate_metric_summary(repo_root, run_id)
    write_metric_reports(repo_root, run_id, metric_rows)
    detection_rows = write_detection_matrix(repo_root, run_id, cases, rows)
    write_negative_results_packet(repo_root, run_id, base_run, cases, rows, metric_rows, detection_rows)
    write_run_manifest(repo_root, run_id, base_run, registry, cases)
    return rows


def create_case_artifacts(run_root: Path, cases: list[dict[str, Any]]) -> None:
    for case in cases:
        case_id = case["negative_case_id"]
        slug = case_id.lower()
        component = case["base_component"]
        code = case["candidate_cn_code"]
        route = artifact_route_for_case(case)
        failed_checks = case["expected_failed_checks"]
        chain = legal_authority_chain_for(case)
        requires_review = route in {"review", "blocked", "unresolved"}
        aa_id = f"NEG_AA_{case_id}"
        handoff_id = f"NEG_HANDOFF_{case_id}"

        pta = {
            "agent": "PTA",
            "component_ref": component,
            "jurisdiction": "EU",
            "hs_code_candidate": code,
            "gri_path_taken": "GRI_1 > GRI_6",
            "source_doc": "controlled_negative_case_bundle",
            "legal_authority_chain": chain,
            "negative_case_id": case_id,
        }
        pra = {
            "agent": "PRA",
            "component_ref": component,
            "jurisdiction": "EU",
            "bti_records_considered": ["controlled_negative_bti_probe"],
            "legal_authority_chain": chain,
            "negative_case_id": case_id,
        }
        aa = {
            "agent": "AA",
            "artifact_id": aa_id,
            "component_ref": component,
            "component_slug": slug,
            "jurisdiction": "EU",
            "candidate_cn_code": code,
            "legal_proposition": f"{case['case_bundle']} controlled negative candidate for {component}.",
            "legal_authority_chain": chain,
            "handoff_route": route,
            "requires_human_review": requires_review,
            "confidence": "high" if case_id == "NEG_006" else "controlled_negative",
            "stability": "stable" if case_id == "NEG_006" else ("unstable" if route != "promote" else "diagnostic"),
            "known_issue_tags": known_issue_tags_for(case),
            "review_reason_codes": [] if case_id == "NEG_006" else failed_checks,
            "required_gri_path_elements": ["GRI_3b"] if case_id == "NEG_004" else [],
            "required_source_anchors": required_source_anchors_for(case),
            "legal_hierarchy_expectations": {"source_to_rule_to_code": True},
            "negative_case_id": case_id,
        }
        audit = {
            "agent": "KA",
            "artifact_id": f"NEG_AUDIT_{case_id}",
            "component_ref": component,
            "evaluated_artifact": aa_id,
            "authority_status": "fail" if has_any(case, "authority_boundary_compliance", "primary_authority_sufficiency") else "pass",
            "provenance_status": "fail" if has_any(case, "provenance_sufficiency") else "pass",
            "graph_parity_status": "fail" if has_any(case, "graph_artifact_parity") else "pass",
            "uncertainty_status": "review" if has_any(case, "false_certainty_rate", "conflict_preservation", "evidence_gap_detection") else "pass",
            "handoff_status": "fail" if route == "blocked" else ("review" if route == "review" else "pass"),
            "failed_checks": failed_checks,
            "recommended_route": route,
            "negative_case_id": case_id,
        }
        handoff = {
            "handoff_id": handoff_id,
            "component_ref": component,
            "source_artifact": aa_id,
            "route": "" if case_id == "NEG_008" else route,
            "review_reason_codes": failed_checks,
            "human_review_required": requires_review,
            "negative_case_id": case_id,
        }
        component_node = {
            "node_id": f"product_component:{slug}",
            "node_type": "product_component",
            "component_ref": component,
            "source": "controlled_negative_case_bundle",
        }
        candidate_node = {
            "node_id": aa_id,
            "node_type": "classification_candidate",
            "artifact_id": aa_id,
            "component_ref": component,
            "jurisdiction": "EU",
        }
        code_node = {
            "node_id": f"hs_code:{code}:EU",
            "node_type": "hs_code",
            "jurisdiction": "EU",
            "code": code,
            "anchor_role": "classification_anchor",
        }
        edge = {
            "edge_id": f"edge:{slug}:proposes:{code}",
            "source_node_id": f"hs_code:{code}:EU" if case_id == "NEG_009" else aa_id,
            "target_node_id": aa_id if case_id == "NEG_009" else f"hs_code:{code}:EU",
            "edge_type": "proposes_code",
            "direction_valid": case_id != "NEG_009",
            "component_ref": component,
            "negative_case_id": case_id,
        }

        writes = {
            f"bundles/{case_id}/source_delta.json": case["source_delta"],
            f"bundles/{case_id}/artifact_delta.json": case["artifact_delta"],
            f"bundles/{case_id}/graph_delta.json": case["graph_delta"],
            f"pta/{slug}_eu.json": pta,
            f"pra/{slug}_eu.json": pra,
            f"aa/{slug}_classification_candidate.json": aa,
            f"audit/{slug}_audit.json": audit,
            f"handoff/{slug}_handoff.json": handoff,
            f"graph/entities/product_component_{slug}.json": component_node,
            f"graph/entities/classification_candidate_{slug}.json": candidate_node,
            f"graph/entities/cn_code_{code.replace('.', '_')}_eu.json": code_node,
            f"graph/relationships/{slug}_proposes_{code.replace('.', '_')}.json": edge,
        }
        for rel_path, payload in writes.items():
            write_json(run_root / rel_path, payload)


def legal_authority_chain_for(case: dict[str, Any]) -> list[dict[str, str]]:
    case_id = case["negative_case_id"]
    if case_id == "NEG_001":
        return [{"source_id": "SRC_INTERNAL_CANDIDATE_ARTIFACT", "authority_class": "internal_generated_candidate", "anchor_id": "INTERNAL_CANDIDATE_FILE"}]
    if case_id == "NEG_002":
        return [
            {"source_id": "SRC_EU_CN_2025_1926_EVS", "authority_class": "primary_legal_text"},
            {"source_id": "SRC_EU_CN_2025_1926_EVS", "authority_class": "primary_legal_text", "anchor_id": "UNRESOLVED_DOCUMENT_LEVEL_ANCHOR"},
        ]
    if case_id == "NEG_003":
        return [{"source_id": "SRC_EU_BTI_SAMPLE", "authority_class": "ruling_or_precedent", "anchor_id": "BTI_ROW_DEBTI45911_25_1"}]
    return [
        {"source_id": "SRC_WCO_GRI_2017", "authority_class": "primary_legal_text", "anchor_id": "WCO_GRI_1"},
        {"source_id": "SRC_EU_CN_2025_1926_EVS", "authority_class": "primary_legal_text", "anchor_id": cn_anchor_for(case["candidate_cn_code"])},
    ]


def cn_anchor_for(code: str) -> str:
    if code.startswith("8507.60"):
        return "EU_CN_8507_60_00"
    if code.startswith("8536.69"):
        return "EU_CN_8536_69_90"
    if code.startswith("8537.10"):
        return "EU_CN_8537_10_91"
    return "EU_CN_8504_40_90"


def artifact_route_for_case(case: dict[str, Any]) -> str:
    case_id = case["negative_case_id"]
    if case_id in {"NEG_001", "NEG_005", "NEG_006", "NEG_007"}:
        return "promote"
    return route_for_gate(case["expected_gate_label"])


def known_issue_tags_for(case: dict[str, Any]) -> list[str]:
    case_id = case["negative_case_id"]
    tags_by_case = {
        "NEG_004": ["critical_omission"],
        "NEG_005": ["unsupported_promotion"],
        "NEG_006": ["confidence_inflation", "divergence_collapsed"],
        "NEG_007": ["evidence_gap", "corpus_gap", "unsupported_promotion", "client_fact_required"],
        "NEG_010": ["over_escalation_burden"],
    }
    return tags_by_case.get(case_id, [])


def required_source_anchors_for(case: dict[str, Any]) -> list[str]:
    if case["negative_case_id"] == "NEG_002":
        return ["EU_CN_8504_40_90"]
    return []


def control_row_for(case: dict[str, Any], run_id: str) -> dict[str, Any]:
    route = route_for_gate(case["expected_gate_label"])
    failed_checks = list(case["expected_failed_checks"])
    severity = "blocker" if route == "blocked" else ("review_trigger" if route == "review" else "pass")
    graph_failure = has_any(case, "graph_artifact_parity")
    return {
        "scenario_id": f"RUN_{run_id}_{case['negative_case_id']}",
        "component_id": case["base_component"],
        "artifact_id": f"NEG_AA_{case['negative_case_id']}",
        "agent_stage": "AA",
        "candidate_eu_cn_code": case["candidate_cn_code"],
        "authority_status": "fail" if has_any(case, "authority_boundary_compliance", "primary_authority_sufficiency") else "pass",
        "provenance_status": "fail" if has_any(case, "provenance_sufficiency") else "pass",
        "capture_status": "review" if has_any(case, "material_legal_capture", "critical_omission_rate") else "pass",
        "representation_status": "review" if has_any(case, "false_certainty_rate", "conflict_preservation") else "pass",
        "graph_parity_status": "fail" if graph_failure else "pass",
        "synthesis_status": "fail" if has_any(case, "unsupported_synthesis_rate") else "pass",
        "uncertainty_status": "review" if has_any(case, "false_certainty_rate", "conflict_preservation", "evidence_gap_detection", "abstention_rate") else "pass",
        "handoff_status": "fail" if route == "blocked" else ("review" if route == "review" else "pass"),
        "failed_checks": failed_checks,
        "severity": severity,
        "expected_route": route,
        "actual_route": route,
        "recommended_action": recommendation_for_gate(case["expected_gate_label"]),
    }


def write_control_reports(repo_root: Path, run_id: str, rows: list[dict[str, Any]]) -> None:
    report_dir = repo_root / "runs" / run_id / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    write_json(report_dir / "control_profile.json", rows)
    with (report_dir / "control_profile.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=RUN_REPORT_COLUMNS)
        writer.writeheader()
        for row in rows:
            encoded = dict(row)
            encoded["failed_checks"] = ";".join(row.get("failed_checks", []))
            encoded["gate_reason_codes"] = ";".join(row.get("gate_reason_codes", []))
            writer.writerow({column: encoded.get(column, "") for column in RUN_REPORT_COLUMNS})
    lines = ["# Negative Run Control Profile", ""]
    lines.append("| " + " | ".join(RUN_REPORT_COLUMNS) + " |")
    lines.append("| " + " | ".join("---" for _ in RUN_REPORT_COLUMNS) + " |")
    for row in rows:
        rendered = []
        for column in RUN_REPORT_COLUMNS:
            value = row.get(column, "")
            if isinstance(value, list):
                value = ";".join(value)
            rendered.append(str(value))
        lines.append("| " + " | ".join(rendered) + " |")
    lines.append("")
    lines.append(f"Negative artifacts evaluated: {len(rows)}")
    (report_dir / "control_profile.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_negative_traces(run_root: Path, run_id: str, cases: list[dict[str, Any]]) -> None:
    trace_dir = run_root / "trace"
    trace_dir.mkdir(parents=True, exist_ok=True)
    agent_events: list[dict[str, Any]] = []
    claims: list[dict[str, Any]] = []
    required_rule_items: list[dict[str, Any]] = []
    inference_edges: list[dict[str, Any]] = []
    gating_decisions: list[dict[str, Any]] = []
    uncertainty_signals: list[dict[str, Any]] = []
    decisions: list[dict[str, Any]] = []
    field_checks: list[dict[str, Any]] = []
    graph_items: list[dict[str, Any]] = []
    abstention_cases: list[dict[str, Any]] = []
    burden_items: list[dict[str, Any]] = []
    rerun_changed = False

    for case in cases:
        case_id = case["negative_case_id"]
        aa_id = f"NEG_AA_{case_id}"
        route = route_for_gate(case["expected_gate_label"])
        component = case["base_component"]
        expected_metrics = set(case["expected_failed_metrics"])
        chain = legal_authority_chain_for(case)

        source_uses = [
            {"source_id": "SRC_WCO_GRI_2017", "source_type": "primary_legal_text", "permitted": True}
        ]
        if "authority_boundary_compliance" in expected_metrics:
            source_uses.append(
                {
                    "source_id": "SRC_INTERNAL_CANDIDATE_ARTIFACT" if case_id == "NEG_001" else "SRC_EU_BTI_SAMPLE",
                    "source_type": "internal_generated_candidate" if case_id == "NEG_001" else "ruling_or_precedent",
                    "permitted": False,
                }
            )
        agent_events.append({"agent_id": "AA", "artifact_id": aa_id, "component_id": component, "source_uses": source_uses})

        provenance_failed = "provenance_sufficiency" in expected_metrics
        claims.append(
            {
                "claim_id": f"claim:{case_id}:classification",
                "artifact_id": aa_id,
                "component_id": component,
                "claim_text": case["case_bundle"],
                "claim_type": "material_legal_proposition",
                "source_trace": [
                    {
                        "source_id": item.get("source_id"),
                        "source_type": item.get("authority_class"),
                        "record_id": item.get("anchor_id"),
                    }
                    for item in chain
                ],
                "verifiable_source_trace": not provenance_failed,
            }
        )

        required_rule_items.extend(default_rule_items(case_id, aa_id, component))
        if {"material_legal_capture", "critical_omission_rate"} & expected_metrics:
            required_rule_items.append(
                {
                    "rule_item_id": f"{case_id}:WCO_GRI_3B_OMITTED",
                    "artifact_id": aa_id,
                    "component_id": component,
                    "rule_id": "WCO_GRI_3B",
                    "weight": 3,
                    "decisive": True,
                    "used": False,
                }
            )

        inference_edges.extend(default_inference_edges(case_id, component))
        if "unsupported_synthesis_rate" in expected_metrics:
            inference_edges.append(
                {
                    "edge_id": f"inference:{case_id}:unsupported-therefore",
                    "component_id": component,
                    "from": "engineering_identity",
                    "to": case["candidate_cn_code"],
                    "support_type": "unsupported_bridge",
                    "supported": False,
                }
            )

        unsafe_output = bool({"handoff_safety"} & expected_metrics)
        requires_escalation = bool({"human_review_trigger_correctness"} & expected_metrics)
        gating_decisions.append(
            {
                "handoff_id": f"NEG_HANDOFF_{case_id}",
                "artifact_id": aa_id,
                "component_id": component,
                "route": route,
                "unsafe_output": unsafe_output,
                "intercepted": False if unsafe_output else route in {"review", "blocked", "unresolved"},
                "requires_escalation": requires_escalation,
                "correct_escalation": False if requires_escalation else route in {"review", "blocked", "unresolved", "promote"},
                "reason_codes": case["expected_failed_checks"],
            }
        )

        incomplete = "evidence_gap_detection" in expected_metrics
        uncertainty_signals.append(
            {
                "artifact_id": aa_id,
                "component_id": component,
                "ambiguous_or_contested": bool({"false_certainty_rate", "conflict_preservation"} & expected_metrics),
                "high_confidence_promote": "false_certainty_rate" in expected_metrics,
                "conflict_case": "conflict_preservation" in expected_metrics,
                "conflict_preserved": False if "conflict_preservation" in expected_metrics else True,
                "incomplete_case": incomplete,
                "gap_flagged": False if incomplete else False,
                "confidence": "high" if "false_certainty_rate" in expected_metrics else "controlled_negative",
                "stability": "stable" if "false_certainty_rate" in expected_metrics else "controlled_negative",
            }
        )
        decisions.append(
            {
                "artifact_id": aa_id,
                "component_id": component,
                "has_primary_or_interpretive_authority": "primary_authority_sufficiency" not in expected_metrics,
                "has_ruling_or_precedent": case_id == "NEG_003",
                "route": route,
            }
        )

        for idx in range(5):
            field_checks.append(
                {
                    "artifact_id": aa_id,
                    "component_slug": case_id.lower(),
                    "agent_stage": "NEGATIVE_BUNDLE",
                    "field": f"required_field_{idx}",
                    "present": not ("field_completeness_rate" in expected_metrics and idx == 0),
                }
            )

        for item_type in ("product_component_node", "hs_code_node", "classification_edge"):
            graph_items.append(
                {
                    "item_id": f"graph:{case_id}:{item_type}",
                    "artifact_id": aa_id,
                    "item_type": item_type,
                    "aligned": not ("graph_artifact_parity" in expected_metrics and item_type == "classification_edge"),
                    "failure_category": "edge_direction_invalid" if "graph_artifact_parity" in expected_metrics and item_type == "classification_edge" else None,
                }
            )

        if "abstention_rate" in expected_metrics:
            abstention_cases.append(
                {
                    "artifact_id": aa_id,
                    "component_id": component,
                    "insufficiency_type": "missing_material_product_facts",
                    "route": route,
                    "correct_abstention": False,
                }
            )

        ticket_required = route in {"review", "blocked", "unresolved"}
        burden_items.append(
            {
                "artifact_id": aa_id,
                "component_id": component,
                "route": route,
                "ticket_required": ticket_required,
                "ticket_type": "human_review" if route == "review" else ("blocking_ticket" if route in {"blocked", "unresolved"} else "none"),
            }
        )

        if "rerun_delta_rate" in expected_metrics:
            rerun_changed = True

    write_json(trace_dir / "agent_trace.json", {"run_id": run_id, "events": agent_events})
    write_json(trace_dir / "claim_trace.json", {"run_id": run_id, "claims": claims})
    write_json(trace_dir / "rule_invocation_graph.json", {"run_id": run_id, "required_rule_items": required_rule_items, "inference_edges": inference_edges})
    write_json(trace_dir / "gating_decisions.json", {"run_id": run_id, "decisions": gating_decisions})
    write_json(trace_dir / "uncertainty_signals.json", {"run_id": run_id, "signals": uncertainty_signals})
    write_json(trace_dir / "metric_inputs.json", {"run_id": run_id, "decisions": decisions, "stress_tests": stress_test_catalog()})
    write_json(trace_dir / "field_completeness_trace.json", {"run_id": run_id, "checks": field_checks})
    write_json(trace_dir / "graph_alignment_trace.json", {"run_id": run_id, "items": graph_items})
    write_json(trace_dir / "abstention_trace.json", {"run_id": run_id, "cases": abstention_cases})
    write_json(
        trace_dir / "research_burden_trace.json",
        {
            "run_id": run_id,
            "tickets": burden_items,
            "summary": {
                "total_artifacts": len(burden_items),
                "review_or_block_tickets": sum(1 for item in burden_items if item["ticket_required"]),
            },
        },
    )
    write_json(
        trace_dir / "rerun_delta_trace.json",
        {
            "run_id": run_id,
            "comparison_enabled": rerun_changed,
            "items": [
                {
                    "artifact_id": "NEG_AA_NEG_010",
                    "baseline_value": "8536.69",
                    "negative_run_value": "8536.90",
                    "changed": True,
                    "comparison_role": "controlled_negative_delta",
                }
            ]
            if rerun_changed
            else [],
            "summary": {
                "comparison_enabled": rerun_changed,
                "comparable_outputs": 2 if rerun_changed else 0,
                "changed_outputs": 1 if rerun_changed else 0,
                "source": "controlled negative rerun delta probe" if rerun_changed else "comparison disabled",
            },
        },
    )


def default_rule_items(case_id: str, aa_id: str, component: str) -> list[dict[str, Any]]:
    return [
        {
            "rule_item_id": f"{case_id}:WCO_GRI_1",
            "artifact_id": aa_id,
            "component_id": component,
            "rule_id": "WCO_GRI_1",
            "weight": 3,
            "decisive": True,
            "used": True,
        },
        {
            "rule_item_id": f"{case_id}:WCO_GRI_6",
            "artifact_id": aa_id,
            "component_id": component,
            "rule_id": "WCO_GRI_6",
            "weight": 2,
            "decisive": False,
            "used": True,
        },
    ]


def default_inference_edges(case_id: str, component: str) -> list[dict[str, Any]]:
    return [
        {
            "edge_id": f"inference:{case_id}:facts-to-method",
            "component_id": component,
            "from": "engineering_identity",
            "to": "legal_method",
            "support_type": "legal_method",
            "supported": True,
        },
        {
            "edge_id": f"inference:{case_id}:method-to-conclusion",
            "component_id": component,
            "from": "legal_method",
            "to": "candidate_code",
            "support_type": "source_and_rule_chain",
            "supported": True,
        },
    ]


def write_detection_matrix(
    repo_root: Path,
    run_id: str,
    cases: list[dict[str, Any]],
    control_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    report_dir = repo_root / "runs" / run_id / "reports"
    detection_rows = build_detection_matrix(control_rows, cases)
    aggregates = detection_aggregates(detection_rows)
    for row in detection_rows:
        row["negative_test_passed"] = row["gate_match"] and not row["false_negative_checks"]

    write_json(report_dir / "negative_detection_matrix.json", detection_rows)
    with (report_dir / "negative_detection_matrix.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=DETECTION_MATRIX_COLUMNS)
        writer.writeheader()
        for row in detection_rows:
            writer.writerow({column: row.get(column, "") for column in DETECTION_MATRIX_COLUMNS})

    lines = ["# Negative Detection Matrix", ""]
    lines.append("| " + " | ".join(DETECTION_MATRIX_COLUMNS) + " |")
    lines.append("| " + " | ".join("---" for _ in DETECTION_MATRIX_COLUMNS) + " |")
    for row in detection_rows:
        lines.append("| " + " | ".join(str(row.get(column, "")) for column in DETECTION_MATRIX_COLUMNS) + " |")
    lines.append("")
    lines.append(f"Negative cases evaluated: {len(detection_rows)}")
    lines.append(f"Negative cases detected as expected: {sum(1 for row in detection_rows if row['negative_test_passed'])}")
    lines.append(f"Gate accuracy: {aggregates['gate_accuracy']}")
    lines.append(f"Micro precision: {aggregates['micro_precision']}")
    lines.append(f"Micro recall: {aggregates['micro_recall']}")
    lines.append(f"Micro F1: {aggregates['micro_f1']}")
    write_json(report_dir / "negative_detection_aggregates.json", aggregates)
    (report_dir / "negative_detection_matrix.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return detection_rows


def write_negative_results_packet(
    repo_root: Path,
    run_id: str,
    base_run: str,
    cases: list[dict[str, Any]],
    control_rows: list[dict[str, Any]],
    metric_rows: list[dict[str, Any]],
    detection_rows: list[dict[str, Any]],
) -> None:
    report_dir = repo_root / "runs" / run_id / "reports"
    gate_counts = Counter(row["gate_label"] for row in control_rows)
    aggregates = detection_aggregates(detection_rows)
    positive_metric_rows = read_json(repo_root / "runs" / base_run / "reports" / "metric_summary.json")
    positive_gate_rows = read_json(repo_root / "runs" / base_run / "reports" / "gate_summary.json")
    positive_gate_counts = Counter(row["gate_label"] for row in positive_gate_rows)
    positive_summary = {
        "base_run": base_run,
        "artifact_count": len(positive_gate_rows),
        "gate_distribution": dict(sorted(positive_gate_counts.items())),
        "metric_statuses": {row["metric_id"]: row["status"] for row in positive_metric_rows},
    }
    packet = {
        "run_id": run_id,
        "base_run": base_run,
        "generated_at": now(),
        "interpretation_boundary": (
            "Controlled deterministic negative evaluation for a bounded HS legal extraction trajectory. "
            "It tests fault-line detection and gate routing; it does not certify legal correctness or adversarial robustness."
        ),
        "positive_baseline_summary": positive_summary,
        "negative_case_design": cases,
        "metric_fault_detection": [
            {
                "metric_id": row["metric_id"],
                "numerator": row["numerator"],
                "denominator": row["denominator"],
                "score": row["score"],
                "status": row["status"],
            }
            for row in metric_rows
        ],
        "negative_gate_distribution": dict(sorted(gate_counts.items())),
        "negative_detection_matrix": detection_rows,
        "negative_detection_aggregates": aggregates,
    }
    write_json(report_dir / "negative_results_packet.json", packet)

    lines = [
        "# HS Negative Evaluation Results Packet",
        "",
        f"- Run ID: `{run_id}`",
        f"- Positive baseline: `{base_run}`",
        f"- Generated at: {packet['generated_at']}",
        "",
        "## Interpretation Boundary",
        "",
        packet["interpretation_boundary"],
        "",
        "## Table 1. Positive Baseline Summary",
        "",
        "| Check | Result |",
        "| --- | --- |",
        f"| Baseline artifacts | {positive_summary['artifact_count']} |",
        f"| Baseline gate distribution | {positive_summary['gate_distribution']} |",
        "",
        "## Table 2. Negative Case Design Matrix",
        "",
        "| Case | Bundle | Perturbation Layer | Expected Metrics | Expected Gate | Legal Rationale |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for case in cases:
        lines.append(
            "| "
            + " | ".join(
                [
                    case["negative_case_id"],
                    case["case_bundle"],
                    ";".join(case["perturbation_layer"]),
                    ";".join(case["expected_failed_metrics"]),
                    case["expected_gate_label"],
                    case["legal_rationale"],
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Table 3. Metric Fault-Detection Matrix",
            "",
            "| Metric ID | Numerator | Denominator | Score | Status |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in metric_rows:
        lines.append(f"| {row['metric_id']} | {row['numerator']} | {row['denominator']} | {row['score']} | {row['status']} |")
    lines.extend(
        [
            "",
            "## Table 4. Negative Gate Distribution",
            "",
            "| Gate Label | Count |",
            "| --- | --- |",
        ]
    )
    for label, count in sorted(gate_counts.items()):
        lines.append(f"| {label} | {count} |")
    lines.extend(
        [
            "",
        "## Table 5. Representative Detected Failures",
        "",
            "| Case | Observed Gate | Precision | Recall | F1 | Gate Match |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in detection_rows:
        lines.append(
            f"| {row['negative_case_id']} | {row['observed_gate_label']} | {row['precision']} | {row['recall']} | {row['f1']} | {row['gate_match']} |"
        )
    lines.extend(
        [
            "",
            "## Detection Aggregates",
            "",
            f"- Gate accuracy: {aggregates['gate_accuracy']}",
            f"- Micro precision: {aggregates['micro_precision']}",
            f"- Micro recall: {aggregates['micro_recall']}",
            f"- Micro F1: {aggregates['micro_f1']}",
            f"- Macro precision: {aggregates['macro_precision']}",
            f"- Macro recall: {aggregates['macro_recall']}",
            f"- Macro F1: {aggregates['macro_f1']}",
        ]
    )
    lines.extend(
        [
            "",
            "The negative study is a controlled fault-injection experiment. It does not claim broad adversarial robustness, final HS correctness, or exhaustive legal failure coverage.",
        ]
    )
    (report_dir / "negative_results_packet.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_run_manifest(repo_root: Path, run_id: str, base_run: str, registry: dict[str, Any], cases: list[dict[str, Any]]) -> None:
    run_root = repo_root / "runs" / run_id
    write_json(
        run_root / "RUN_MANIFEST.json",
        {
            "run_id": run_id,
            "run_type": "controlled_negative_fault_injection",
            "created_at": now(),
            "base_run": base_run,
            "registry_path": str(NEGATIVE_REGISTRY_PATH),
            "case_count": len(cases),
            "component_count": len(cases),
            "reference_baseline_used_as_input": False,
            "runtime_input_paths": [
                str(NEGATIVE_REGISTRY_PATH),
                f"runs/{base_run}/reports/metric_summary.json",
                f"runs/{base_run}/reports/gate_summary.json",
            ],
            "artifact_counts": {
                "negative_bundles": len(list((run_root / "bundles").glob("NEG_*"))),
                "pta": len(list((run_root / "pta").glob("*.json"))),
                "pra": len(list((run_root / "pra").glob("*.json"))),
                "aa": len(list((run_root / "aa").glob("*.json"))),
                "audit": len(list((run_root / "audit").glob("*.json"))),
                "handoff": len(list((run_root / "handoff").glob("*.json"))),
                "graph_entities": len(list((run_root / "graph" / "entities").glob("*.json"))),
                "graph_relationships": len(list((run_root / "graph" / "relationships").glob("*.json"))),
            },
            "expected_metric_coverage": sorted({metric for case in cases for metric in case["expected_failed_metrics"]}),
            "paper_claim_boundary": "Fault-line detection and gate routing only; no final legal correctness certification.",
            "registry_sha_marker": registry.get("schema_version"),
        },
    )


def has_any(case: dict[str, Any], *metric_ids: str) -> bool:
    return bool(set(metric_ids) & set(case["expected_failed_metrics"]))


def route_for_gate(gate_label: str) -> str:
    if gate_label == "pass":
        return "promote"
    if gate_label == "pass_with_notes":
        return "review"
    return "blocked"


def recommendation_for_gate(gate_label: str) -> str:
    if gate_label == "pass":
        return "promote"
    if gate_label == "pass_with_notes":
        return "route_to_human_review"
    if gate_label == "blocked_pending_rerun":
        return "block_pending_rerun"
    return "block_pending_source_or_authority_repair"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create a deterministic controlled negative HS evaluation run.")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--base-run", default="paper_eval_20260520")
    parser.add_argument("--force", action="store_true", help="Overwrite an existing negative run directory.")
    parser.add_argument("--validate-only", action="store_true", help="Validate the negative registry without creating a run.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    registry = load_negative_registry(args.repo_root)
    errors = validate_negative_registry(args.repo_root, registry)
    if errors:
        raise SystemExit("Negative registry validation failed: " + "; ".join(errors))
    if args.validate_only:
        print(f"Validated {len(registry['cases'])} negative case bundles.")
        return 0
    rows = create_negative_run(args.repo_root, args.run_id, base_run=args.base_run, overwrite=args.force)
    print(f"Created negative run {args.run_id} with {len(rows)} controlled fault-injection cases.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
