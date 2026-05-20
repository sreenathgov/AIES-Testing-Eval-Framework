from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping

from .source_authority_registry import PAPER_SCOPE_JURISDICTIONS, PAPER_SCOPE_SOURCE_CLASSES

EXTERNAL_AUTHORITY_CLASSES = frozenset(
    {
        "primary_legal_text",
        "interpretive_legal_note",
        "ruling_or_precedent",
    }
)

INTERNAL_AUTHORITY_CLASSES = frozenset({"internal_generated_candidate"})

RECOGNIZED_ARTIFACT_TYPES = frozenset(
    {
        "engineering_identity_record",
        "statutory_classification_record",
        "ruling_record",
        "classification_candidate",
        "adjudication_bundle",
        "audit_report",
        "handoff_package",
        "hs_code",
    }
)

ARTIFACT_TYPE_TO_NODE_TYPE = {
    "engineering_identity_record": "engineering_identity_record",
    "statutory_classification_record": "statutory_classification_record",
    "ruling_record": "ruling_record",
    "classification_candidate": "classification_candidate",
    "adjudication_bundle": "adjudication_bundle",
    "audit_report": "audit_report",
    "handoff_package": "handoff_package",
    "hs_code": "hs_code",
}

REVIEW_CHECKS = frozenset(
    {
        "pta_final_adjudication_overreach",
        "pta_requires_aa_review",
        "product_identity_mixed_with_classification_state",
        "jurisdictional_divergence_preserved",
        "comparison_only_divergence_preserved",
        "client_fact_required",
        "confidence_inflation",
        "divergence_collapsed",
        "capture_gap_requires_review",
        "gri_6_missing_for_subheading_claim",
        "gri_3b_requires_adjudication_review",
        "representation_scope_broadened",
        "legal_hierarchy_incomplete",
        "unsupported_synthesis_review",
        "review_trigger_missing_route",
    }
)


@dataclass(frozen=True)
class ValidatorResult:
    status: str
    failed_checks: tuple[str, ...] = ()

    @classmethod
    def pass_(cls) -> "ValidatorResult":
        return cls(status="pass", failed_checks=())

    @classmethod
    def fail(cls, *checks: str) -> "ValidatorResult":
        return cls(status="fail", failed_checks=tuple(dict.fromkeys(checks)))

    @classmethod
    def review(cls, *checks: str) -> "ValidatorResult":
        return cls(status="review", failed_checks=tuple(dict.fromkeys(checks)))


@dataclass(frozen=True)
class EvaluationResult:
    scenario_id: str
    artifact_id: str
    fixture_class: str
    artifact_type: str
    agent_stage: str
    jurisdiction: str
    candidate_hs_code: str | None
    candidate_cn_code: str | None
    authority_status: str
    provenance_status: str
    source_integrity_status: str
    quote_fidelity_status: str
    capture_status: str
    representation_status: str
    legal_method_status: str
    graph_parity_status: str
    synthesis_status: str
    uncertainty_status: str
    handoff_status: str
    failed_checks: tuple[str, ...]
    expected_route: str
    actual_route: str
    expected_control_state: str
    final_control_state: str
    human_review_required: bool
    passed_gold: bool
    severity: str
    recommended_action: str
    details: Mapping[str, Any] = field(default_factory=dict)

    def as_row(self) -> dict[str, Any]:
        return {
            "scenario_id": self.scenario_id,
            "artifact_id": self.artifact_id,
            "fixture_class": self.fixture_class,
            "artifact_type": self.artifact_type,
            "agent_stage": self.agent_stage,
            "jurisdiction": self.jurisdiction,
            "candidate_hs_code": self.candidate_hs_code,
            "candidate_cn_code": self.candidate_cn_code,
            "authority_status": self.authority_status,
            "provenance_status": self.provenance_status,
            "source_integrity_status": self.source_integrity_status,
            "quote_fidelity_status": self.quote_fidelity_status,
            "capture_status": self.capture_status,
            "representation_status": self.representation_status,
            "legal_method_status": self.legal_method_status,
            "graph_parity_status": self.graph_parity_status,
            "synthesis_status": self.synthesis_status,
            "uncertainty_status": self.uncertainty_status,
            "handoff_status": self.handoff_status,
            "failed_checks": list(self.failed_checks),
            "expected_route": self.expected_route,
            "actual_route": self.actual_route,
            "expected_control_state": self.expected_control_state,
            "final_control_state": self.final_control_state,
            "human_review_required": self.human_review_required,
            "passed_gold": self.passed_gold,
            "severity": self.severity,
            "recommended_action": self.recommended_action,
        }
