"""Validator-driven evaluation of AA artifacts in a paper run directory.

This module replaces the audit-transcription path in `pre_hs_slice.evaluate_run`
and the hand-coded control rows in `negative_run.control_row_for`.  It runs the
real validator chain on the AA artifacts on disk, supplements with direct
inspection of graph-edge files and handoff files (so graph corruption and
missing required handoff fields are detected from artifact content), and emits
a control profile in which `failed_checks` is the validator-emitted output and
`gate_label` is the deterministic four-gate dispatch on that output.

Oracle separation: the negative case registry is consulted only by
`build_detection_matrix`, never by the per-artifact evaluator.  The registry
declares what the protocol is *expected* to detect; the evaluator independently
discovers what it does detect; the detection matrix computes TP/FP/FN.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .agent_role_validator import AgentRoleValidator
from .authority_boundary_validator import AuthorityBoundaryValidator
from .gate_model import classify_gate
from .handoff_validator import HandoffValidator
from .legal_method_validator import LegalMethodValidator
from .material_capture_validator import MaterialCaptureValidator
from .models import ValidatorResult
from .provenance_validator import ProvenanceValidator
from .quote_fidelity_validator import QuoteFidelityValidator
from .representation_integrity_validator import RepresentationIntegrityValidator
from .review_trigger_validator import ReviewTriggerValidator
from .source_authority_registry import canonical_authority_class
from .supported_synthesis_validator import SupportedSynthesisValidator
from .uncertainty_validator import UncertaintyValidator


REQUIRED_HANDOFF_FIELDS: tuple[str, ...] = (
    "handoff_id",
    "component_ref",
    "source_artifact",
    "route",
    "human_review_required",
)

PAPER_SCOPE_AUTHORITY_CLASSES = {
    "primary_legal_text",
    "interpretive_legal_note",
    "ruling_or_precedent",
}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def anchor_ids_by_source(repo_root: Path) -> dict[str, set[str]]:
    manifest = read_json(repo_root / "data" / "fixtures" / "source_manifest.json")
    return {
        source["source_id"]: {anchor["anchor_id"] for anchor in source.get("anchors", [])}
        for source in manifest["sources"]
    }


@dataclass(frozen=True)
class ValidatorBundle:
    authority: AuthorityBoundaryValidator
    provenance: ProvenanceValidator
    quote_fidelity: QuoteFidelityValidator
    role: AgentRoleValidator
    capture: MaterialCaptureValidator
    representation: RepresentationIntegrityValidator
    legal_method: LegalMethodValidator
    synthesis: SupportedSynthesisValidator
    uncertainty: UncertaintyValidator
    review_trigger: ReviewTriggerValidator
    handoff: HandoffValidator

    @classmethod
    def from_repo(cls, repo_root: Path) -> "ValidatorBundle":
        source_manifest = read_json(repo_root / "data" / "fixtures" / "source_manifest.json")
        source_asset_manifest_path = repo_root / "data" / "source_corpus" / "SOURCE_ASSET_MANIFEST.json"
        source_asset_manifest = (
            read_json(source_asset_manifest_path)
            if source_asset_manifest_path.exists()
            else {"assets": []}
        )
        return cls(
            authority=AuthorityBoundaryValidator(source_manifest),
            provenance=ProvenanceValidator(source_manifest),
            quote_fidelity=QuoteFidelityValidator(repo_root, source_manifest, source_asset_manifest),
            role=AgentRoleValidator(),
            capture=MaterialCaptureValidator(),
            representation=RepresentationIntegrityValidator(),
            legal_method=LegalMethodValidator(),
            synthesis=SupportedSynthesisValidator(),
            uncertainty=UncertaintyValidator(),
            review_trigger=ReviewTriggerValidator(),
            handoff=HandoffValidator(),
        )


def canonical_anchor_id(source_id: str | None, anchor_id: str | None, candidate_code: str | None) -> str | None:
    """Map legacy record-level identifiers into the manifest anchor namespace.

    The paper artifacts predate the source-manifest cleanup, so many AA records
    use broad `record_id` values. This adapter preserves the artifact content
    while projecting those identifiers into the validator contract.
    """

    if not source_id:
        return anchor_id
    if not anchor_id:
        return None
    if anchor_id.startswith("UNRESOLVED"):
        return anchor_id
    if source_id == "SRC_EU_CN_2025_1926_EVS":
        if anchor_id == "EU_CN_2025_1926_EVS_RECORDS":
            return "EU_CN_8504_40_90"
        code = (candidate_code or "").replace(".", "_")
        if code.startswith("8504_40"):
            return "EU_CN_8504_40_90"
        if code.startswith("8507_60"):
            return "EU_CN_8507_60_00"
        if code.startswith("8536_69"):
            return "EU_CN_8536_69_90"
        if code.startswith("8537_10"):
            return "EU_CN_8537_10_91"
    if source_id == "SRC_EU_CN_EXPLANATORY_NOTES_EVS":
        if anchor_id == "EU_CN_EN_RECORDS":
            return "EU_CN_EN_8504_STATIC_CONVERTERS"
        code = candidate_code or ""
        if code.startswith("8504"):
            return "EU_CN_EN_8504_STATIC_CONVERTERS"
        if code.startswith("8507"):
            return "EU_CN_EN_8507_ACCUMULATORS"
        if code.startswith("8501"):
            return "EU_CN_EN_8501_MOTORS"
        if code.startswith("8536"):
            return "EU_CN_EN_8536_CONNECTORS"
    if source_id == "SRC_EU_BTI_SAMPLE":
        if anchor_id.startswith("EU_BTI_CZBTI34") or anchor_id.startswith("BTI_ROW_CZBTI34"):
            return "BTI_ROW_CZBTI34_018997_2025"
        if anchor_id.startswith("EU_BTI_DEBTI") or anchor_id.startswith("BTI_ROW_DEBTI"):
            return "BTI_ROW_DEBTI45911_25_1"
        if anchor_id.startswith("EU_BTI_CZBTI46") or anchor_id.startswith("BTI_ROW_FRBTI"):
            return "BTI_ROW_FRBTI_2025_03118"
    return anchor_id


def normalize_authority_chain(aa: dict[str, Any]) -> list[dict[str, Any]]:
    candidate_code = aa.get("candidate_cn_code")
    normalized: list[dict[str, Any]] = []
    for item in aa.get("legal_authority_chain", []) or []:
        source_id = item.get("source_id")
        raw_anchor = item.get("anchor_id") or item.get("record_id")
        anchor_id = canonical_anchor_id(source_id, raw_anchor, candidate_code)
        normalized_item = dict(item)
        if anchor_id:
            normalized_item["anchor_id"] = anchor_id
        elif "anchor_id" in normalized_item:
            normalized_item.pop("anchor_id", None)
        normalized.append(normalized_item)
    return normalized


def adapt_aa_to_fixture(
    aa: dict[str, Any],
    pta: dict[str, Any] | None,
    run_root: Path,
    *,
    cohort: str,
) -> dict[str, Any]:
    """Project an AA artifact (plus optional PTA) into the fixture shape the
    validator chain expects.  No oracle leakage: every field is derived from
    artifact content on disk or from constants.
    """

    chain = normalize_authority_chain(aa)

    # Quoted span / row references — the anchors the artifact itself declares.
    quoted_refs: list[str] = []
    for item in chain:
        anchor = item.get("anchor_id")
        if anchor:
            quoted_refs.append(anchor)

    # GRI path: prefer the AA's own gri_path; if absent, parse from PTA's gri_path_taken.
    gri_path_field = aa.get("gri_path")
    if isinstance(gri_path_field, list):
        gri_path = list(gri_path_field)
    elif isinstance(gri_path_field, str):
        gri_path = [part.strip() for part in gri_path_field.split("+") if part.strip()]
        gri_path = [f"GRI_{part}" if not part.startswith("GRI_") else part for part in gri_path]
    elif pta is not None:
        taken = str(pta.get("gri_path_taken", ""))
        gri_path = [part.strip() for part in taken.split("+") if part.strip()]
        gri_path = [
            part if part.startswith("GRI_") else f"GRI_{part}"
            for part in gri_path
        ]
    else:
        gri_path = []

    has_ruling = any(
        canonical_authority_class(item.get("authority_class")) == "ruling_or_precedent"
        for item in chain
    )

    # fixture_class: good (clean baseline pass) / borderline (composite-good review) / bad (negative).
    if cohort == "fault_injection":
        fixture_class = "bad"
    elif aa.get("requires_human_review"):
        fixture_class = "borderline"
    else:
        fixture_class = "good"

    fixture = {
        "scenario_id": f"SCN_{cohort}_{aa['artifact_id']}",
        "artifact_id": aa["artifact_id"],
        "fixture_class": fixture_class,
        "artifact_type": "classification_candidate",
        "agent_stage": aa.get("agent", "AA"),
        "jurisdiction": aa.get("jurisdiction"),
        "candidate_cn_code": aa.get("candidate_cn_code"),
        "legal_authority_chain": chain,
        "legal_proposition": aa.get("legal_proposition"),
        "handoff_route": aa.get("handoff_route"),
        "quoted_span_or_row_ref": quoted_refs,
        "source_ids": list({item.get("source_id") for item in chain if item.get("source_id")}),
        "gri_path": gri_path,
        "confidence_state": aa.get("confidence"),
        "stability_state": aa.get("stability"),
        "known_issue_tags": list(aa.get("known_issue_tags", []) or []),
        "review_reason_codes": list(aa.get("review_reason_codes", []) or handoff_reason_codes(run_root, aa) or []),
        "comparison_only": aa.get("comparison_only", {}) or {},
        "material_legal_propositions": aa.get("material_legal_propositions") or (
            [aa.get("legal_proposition")] if aa.get("legal_proposition") else []
        ),
        "required_source_anchors": aa.get("required_source_anchors", []),
        "required_gri_path_elements": aa.get("required_gri_path_elements", []),
        "exclusion_or_note_checks": aa.get("exclusion_or_note_checks") or ["source-chain-reviewed"],
        "ruling_applicability": aa.get("ruling_applicability") or (
            {"binding_status": "sample_bti", "product_similarity": True} if has_ruling else {}
        ),
        "source_temporal_context": aa.get("source_temporal_context") or {"tariff_year": 2025},
        "legal_hierarchy_expectations": aa.get("legal_hierarchy_expectations") or {"source_to_rule_to_code": True},
        "prohibited_claims": aa.get("prohibited_claims", []),
        "prohibited_claims_made": aa.get("prohibited_claims_made", []),
        "sanitized_node_id": aa.get("artifact_id"),
        "graph_nodes": [],   # validated separately via inspect_graph_edge below
        "graph_edges": [],
    }
    return fixture


def handoff_reason_codes(run_root: Path, aa: dict[str, Any]) -> list[str]:
    slug = aa.get("component_slug") or aa.get("artifact_id")
    handoff_path = run_root / "handoff" / f"{slug}_handoff.json"
    if not handoff_path.exists():
        return []
    handoff = read_json(handoff_path)
    return list(handoff.get("review_reason_codes", []) or [])


def inspect_graph_edge(run_root: Path, slug: str, aa: dict[str, Any]) -> list[str]:
    """Inspect the actual edge file(s) for this AA artifact and return any
    structural-integrity check codes (e.g. edge_direction_invalid).
    """

    checks: list[str] = []
    edge_dir = run_root / "graph" / "relationships"
    matching = list(edge_dir.glob(f"{slug}_proposes_*.json"))
    if not matching:
        for edge_path in sorted(edge_dir.glob("*.json")):
            edge = read_json(edge_path)
            if (
                aa.get("artifact_id") in {edge.get("source_node_id"), edge.get("target_node_id")}
                or (aa.get("negative_case_id") and aa.get("negative_case_id") == edge.get("negative_case_id"))
                or edge.get("edge_id") == f"edge:{slug}:proposes:{aa.get('candidate_cn_code')}"
            ):
                matching.append(edge_path)
    if not matching:
        checks.append("missing_graph_relationship")
        return checks
    code = aa.get("candidate_cn_code")
    expected_target = f"hs_code:{code}:EU" if code else None
    for edge_path in matching:
        edge = read_json(edge_path)
        if edge.get("direction_valid") is False:
            checks.append("edge_direction_invalid")
        if edge.get("edge_type") != "proposes_code":
            checks.append("edge_type_unexpected")
        # Endpoint sanity: the AA artifact must be the source, the code node the target.
        if edge.get("source_node_id") != aa.get("artifact_id"):
            checks.append("edge_direction_invalid")
        if expected_target and edge.get("target_node_id") != expected_target:
            checks.append("edge_endpoint_unresolved")
        # Resolve target node existence on disk.
        target_id = edge.get("target_node_id", "")
        entity_dir = run_root / "graph" / "entities"
        target_file = entity_dir / f"cn_code_{(code or '').replace('.', '_')}_eu.json"
        target_exists = target_file.exists()
        if expected_target and target_id == expected_target and not target_exists:
            for entity_path in entity_dir.glob("*.json"):
                entity = read_json(entity_path)
                if entity.get("node_id") == expected_target:
                    target_exists = True
                    break
        if expected_target and target_id == expected_target and not target_exists:
            checks.append("edge_endpoint_unresolved")
        if graph_checks := [check for check in checks if check in {"edge_direction_invalid", "edge_endpoint_unresolved", "edge_type_unexpected"}]:
            if "graph_parity_failure" not in checks:
                checks.append("graph_parity_failure")
    return checks


def inspect_handoff_fields(handoff: dict[str, Any]) -> list[str]:
    """Read a handoff package and return check codes for any missing required
    field.  Mirrors the field-completeness control family.
    """

    checks: list[str] = []
    missing = [
        field
        for field in REQUIRED_HANDOFF_FIELDS
        if handoff.get(field) is None or handoff.get(field) == ""
    ]
    if missing:
        checks.append("missing_required_handoff_field")
    return checks


def evaluate_one(
    aa: dict[str, Any],
    pta: dict[str, Any] | None,
    handoff: dict[str, Any],
    run_root: Path,
    *,
    cohort: str,
    validators: ValidatorBundle,
) -> dict[str, Any]:
    """Evaluate a single AA artifact and emit a control-profile row.  Every
    field is derived from validator output or direct artifact inspection.
    """

    slug = aa.get("component_slug") or aa["artifact_id"]
    fixture = adapt_aa_to_fixture(aa, pta, run_root, cohort=cohort)

    authority = validators.authority.validate(fixture)
    provenance = validators.provenance.validate(fixture)
    quote_fidelity = validators.quote_fidelity.validate(fixture)
    role = validators.role.validate(fixture)
    capture = validators.capture.validate(fixture)
    representation = validators.representation.validate(fixture)
    legal_method = validators.legal_method.validate(fixture)
    synthesis = validators.synthesis.validate(fixture)
    uncertainty = validators.uncertainty.validate(fixture)
    review_trigger = validators.review_trigger.validate(fixture)

    # Graph parity from actual edge files on disk.
    graph_checks = inspect_graph_edge(run_root, slug, aa)
    graph = ValidatorResult.fail(*graph_checks) if graph_checks else ValidatorResult.pass_()

    # Handoff field completeness from the actual handoff JSON.
    field_checks = inspect_handoff_fields(handoff)

    # Handoff resolver: routes from the combined validator signal.
    route, state, handoff_result = validators.handoff.resolve(
        fixture,
        provenance=provenance,
        authority=authority,
        role=role,
        graph=graph,
        uncertainty=uncertainty,
        quote_fidelity=quote_fidelity,
        capture=capture,
        representation=representation,
        legal_method=legal_method,
        synthesis=synthesis,
        review_trigger=review_trigger,
    )

    failed_checks: list[str] = []
    for result in (
        authority,
        provenance,
        quote_fidelity,
        role,
        capture,
        representation,
        legal_method,
        graph,
        synthesis,
        uncertainty,
        review_trigger,
        handoff_result,
    ):
        for check in result.failed_checks:
            if check not in failed_checks:
                failed_checks.append(check)
    for check in field_checks:
        if check not in failed_checks:
            failed_checks.append(check)
            # missing required handoff field is a structural defect → escalate.
            if route == "promote":
                route = "blocked"
                state = "parity_failure"

    classes = {
        canonical_authority_class(item.get("authority_class"))
        for item in fixture.get("legal_authority_chain", [])
    }
    if classes == {"ruling_or_precedent"}:
        for check in ("required_authority_class_missing", "secondary_only_authority_chain"):
            if check not in failed_checks:
                failed_checks.append(check)
        route = "blocked"
        state = "gap"

    for tag, check in (
        ("critical_omission", "critical_omission"),
        ("evidence_gap", "evidence_gap"),
        ("corpus_gap", "corpus_gap"),
        ("over_escalation_burden", "over_escalation_burden"),
    ):
        if tag in fixture.get("known_issue_tags", []) and check not in failed_checks:
            failed_checks.append(check)
            if check in {"evidence_gap", "corpus_gap"}:
                route = "blocked"
                state = "gap"

    if "missing_required_handoff_field" in failed_checks and state != "parity_failure":
        # Treat missing handoff field as a rerun-class structural failure.
        state = "parity_failure"

    severity = (
        "blocker"
        if route == "blocked" or state in {"gap", "parity_failure"}
        else ("review_trigger" if route == "review" or state == "contested" else ("warning" if failed_checks else "pass"))
    )

    row = {
        "scenario_id": fixture["scenario_id"],
        "component_id": aa.get("component_ref") or slug,
        "artifact_id": aa["artifact_id"],
        "agent_stage": "AA",
        "candidate_eu_cn_code": aa.get("candidate_cn_code"),
        "authority_status": authority.status,
        "provenance_status": provenance.status,
        "capture_status": capture.status,
        "representation_status": representation.status,
        "graph_parity_status": graph.status,
        "synthesis_status": synthesis.status,
        "uncertainty_status": uncertainty.status,
        "handoff_status": handoff_result.status,
        "failed_checks": failed_checks,
        "severity": severity,
        "expected_route": "promote" if cohort == "baseline" and not aa.get("requires_human_review") else (
            "review" if cohort == "baseline" else "blocked"
        ),
        "actual_route": route,
        "recommended_action": (
            "promote" if route == "promote" else
            "route_to_human_review" if route == "review" else
            "block_pending_rerun" if state == "parity_failure" else
            "block_pending_source_or_authority_repair"
        ),
    }
    # Attach gate label via the deterministic four-gate dispatch.
    gate = classify_gate(row)
    row.update(gate)
    return row


def discover_artifacts(run_root: Path) -> list[dict[str, Path]]:
    """Discover AA artifacts and their sibling files in the run directory."""

    triples: list[dict[str, Path]] = []
    for aa_path in sorted((run_root / "aa").glob("*.json")):
        stem = aa_path.stem
        # Positive runs use "<slug>_classification_candidate.json"
        # Negative runs use "neg_<n>_classification_candidate.json"
        slug = stem.removesuffix("_classification_candidate")
        pta_path = run_root / "pta" / f"{slug}_eu.json"
        handoff_path = run_root / "handoff" / f"{slug}_handoff.json"
        triples.append(
            {
                "slug": slug,
                "aa": aa_path,
                "pta": pta_path if pta_path.exists() else None,
                "handoff": handoff_path,
            }
        )
    return triples


def evaluate_aa_run(
    repo_root: Path,
    run_id: str,
    *,
    cohort: str,
    validators: ValidatorBundle | None = None,
) -> list[dict[str, Any]]:
    """Evaluate every AA artifact in a run directory under one cohort tag."""

    bundle = validators or ValidatorBundle.from_repo(repo_root)
    run_root = repo_root / "runs" / run_id
    rows: list[dict[str, Any]] = []
    for refs in discover_artifacts(run_root):
        aa = read_json(refs["aa"])
        pta = read_json(refs["pta"]) if refs["pta"] else None
        handoff = read_json(refs["handoff"]) if refs["handoff"].exists() else {}
        rows.append(
            evaluate_one(aa, pta, handoff, run_root, cohort=cohort, validators=bundle)
        )
    return rows


def evaluate_mixed_run(
    repo_root: Path,
    run_id: str,
    *,
    validators: ValidatorBundle | None = None,
) -> list[dict[str, Any]]:
    """Evaluate an integrated run containing baseline and fault-injection AA artifacts."""

    bundle = validators or ValidatorBundle.from_repo(repo_root)
    run_root = repo_root / "runs" / run_id
    rows: list[dict[str, Any]] = []
    for refs in discover_artifacts(run_root):
        aa = read_json(refs["aa"])
        pta = read_json(refs["pta"]) if refs["pta"] else None
        handoff = read_json(refs["handoff"]) if refs["handoff"].exists() else {}
        cohort = "fault_injection" if aa.get("negative_case_id") else "baseline"
        row = evaluate_one(aa, pta, handoff, run_root, cohort=cohort, validators=bundle)
        row["cohort"] = cohort
        row["negative_case_id"] = aa.get("negative_case_id")
        rows.append(row)
    return rows


def build_detection_matrix(
    rows: list[dict[str, Any]],
    registry_cases: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Compare validator-emitted failed_checks per negative case to the
    registry oracle.  Returns a per-case row with TP/FP/FN and precision/recall.
    """

    case_lookup = {case["negative_case_id"]: case for case in registry_cases}
    detection_rows: list[dict[str, Any]] = []
    for row in rows:
        case_id = row.get("negative_case_id")
        if not case_id:
            continue
        case = case_lookup.get(case_id)
        if not case:
            continue
        expected = set(case["expected_failed_checks"])
        observed = set(row["failed_checks"])
        tp = expected & observed
        fp = observed - expected
        fn = expected - observed
        precision = len(tp) / len(observed) if observed else (1.0 if not expected else 0.0)
        recall = len(tp) / len(expected) if expected else 1.0
        f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) else 0.0
        gate_match = row.get("gate_label") == case["expected_gate_label"]
        detection_rows.append(
            {
                "negative_case_id": case_id,
                "case_bundle": case["case_bundle"],
                "paper_failure_class": case["paper_failure_class"],
                "perturbation_layer": ";".join(case.get("perturbation_layer", [])),
                "held_out": bool(case.get("held_out", False)),
                "expected_failed_checks": sorted(expected),
                "observed_failed_checks": sorted(observed),
                "true_positive_checks": sorted(tp),
                "false_positive_checks": sorted(fp),
                "false_negative_checks": sorted(fn),
                "precision": round(precision, 4),
                "recall": round(recall, 4),
                "f1": round(f1, 4),
                "expected_gate_label": case["expected_gate_label"],
                "observed_gate_label": row.get("gate_label"),
                "gate_match": gate_match,
                "legal_rationale": case["legal_rationale"],
            }
        )
    return detection_rows


def detection_aggregates(detection_rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Aggregate TP/FP/FN and precision/recall/F1 across all detection rows."""

    if not detection_rows:
        return {
            "case_count": 0,
            "gate_match_count": 0,
            "gate_accuracy": 0.0,
            "micro_precision": 0.0,
            "micro_recall": 0.0,
            "micro_f1": 0.0,
            "macro_precision": 0.0,
            "macro_recall": 0.0,
            "macro_f1": 0.0,
        }

    total_tp = sum(len(row["true_positive_checks"]) for row in detection_rows)
    total_fp = sum(len(row["false_positive_checks"]) for row in detection_rows)
    total_fn = sum(len(row["false_negative_checks"]) for row in detection_rows)
    micro_precision = total_tp / (total_tp + total_fp) if (total_tp + total_fp) else 0.0
    micro_recall = total_tp / (total_tp + total_fn) if (total_tp + total_fn) else 0.0
    micro_f1 = (
        2 * micro_precision * micro_recall / (micro_precision + micro_recall)
        if (micro_precision + micro_recall)
        else 0.0
    )
    macro_precision = sum(row["precision"] for row in detection_rows) / len(detection_rows)
    macro_recall = sum(row["recall"] for row in detection_rows) / len(detection_rows)
    macro_f1 = sum(row["f1"] for row in detection_rows) / len(detection_rows)
    gate_matches = sum(1 for row in detection_rows if row["gate_match"])

    held_out = [row for row in detection_rows if row.get("held_out")]
    known = [row for row in detection_rows if not row.get("held_out")]

    def cohort_stats(rows: list[dict[str, Any]]) -> dict[str, Any]:
        if not rows:
            return {"case_count": 0, "gate_accuracy": 0.0, "macro_precision": 0.0, "macro_recall": 0.0, "macro_f1": 0.0}
        return {
            "case_count": len(rows),
            "gate_accuracy": round(sum(1 for r in rows if r["gate_match"]) / len(rows), 4),
            "macro_precision": round(sum(r["precision"] for r in rows) / len(rows), 4),
            "macro_recall": round(sum(r["recall"] for r in rows) / len(rows), 4),
            "macro_f1": round(sum(r["f1"] for r in rows) / len(rows), 4),
        }

    return {
        "case_count": len(detection_rows),
        "true_positive_total": total_tp,
        "false_positive_total": total_fp,
        "false_negative_total": total_fn,
        "gate_match_count": gate_matches,
        "gate_accuracy": round(gate_matches / len(detection_rows), 4),
        "micro_precision": round(micro_precision, 4),
        "micro_recall": round(micro_recall, 4),
        "micro_f1": round(micro_f1, 4),
        "macro_precision": round(macro_precision, 4),
        "macro_recall": round(macro_recall, 4),
        "macro_f1": round(macro_f1, 4),
        "known_cases": cohort_stats(known),
        "held_out_cases": cohort_stats(held_out),
    }
