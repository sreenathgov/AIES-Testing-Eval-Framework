from __future__ import annotations

from pathlib import Path
from typing import Any

from .agent_role_validator import AgentRoleValidator
from .authority_boundary_validator import AuthorityBoundaryValidator
from .data_loader import (
    load_control_framework,
    load_edges,
    load_fixtures,
    load_forensic_manifest,
    load_gold_cases,
    load_lineage_map,
    load_source_asset_manifest,
    load_source_manifest,
)
from .fixture_admission import validate_fixture_admission
from .graph_adapter import GraphAdapter
from .handoff_validator import HandoffValidator
from .legal_method_validator import LegalMethodValidator
from .material_capture_validator import MaterialCaptureValidator
from .models import EvaluationResult, ValidatorResult
from .provenance_validator import ProvenanceValidator
from .quote_fidelity_validator import QuoteFidelityValidator
from .representation_integrity_validator import RepresentationIntegrityValidator
from .review_trigger_validator import ReviewTriggerValidator
from .source_integrity_validator import SourceIntegrityValidator
from .source_authority_registry import canonical_authority_class
from .supported_synthesis_validator import SupportedSynthesisValidator
from .uncertainty_validator import UncertaintyValidator


class Evaluator:
    def __init__(
        self,
        fixtures: list[dict[str, Any]],
        edges: list[dict[str, Any]],
        source_manifest: dict[str, Any],
        gold_cases: list[dict[str, Any]],
        *,
        repo_root: Path | None = None,
        source_asset_manifest: dict[str, Any] | None = None,
        forensic_manifest: dict[str, Any] | None = None,
        lineage_map: list[dict[str, Any]] | None = None,
        control_framework: dict[str, Any] | None = None,
    ) -> None:
        repo_root = repo_root or Path.cwd()
        self.fixtures = fixtures
        self.edges = edges
        self.source_manifest = source_manifest
        self.control_framework = control_framework or {}
        self.gold_by_artifact = {case["artifact_id"]: case for case in gold_cases}
        self.graph = GraphAdapter.build(fixtures, edges, source_manifest)
        self.source_integrity = SourceIntegrityValidator(
            repo_root,
            source_asset_manifest or {"assets": []},
            forensic_manifest or {"artifacts": []},
            lineage_map or [],
        )
        self.provenance = ProvenanceValidator(source_manifest)
        self.quote_fidelity = QuoteFidelityValidator(
            repo_root,
            source_manifest,
            source_asset_manifest or {"assets": []},
        )
        self.authority = AuthorityBoundaryValidator(source_manifest)
        self.roles = AgentRoleValidator()
        self.capture = MaterialCaptureValidator()
        self.representation = RepresentationIntegrityValidator()
        self.legal_method = LegalMethodValidator()
        self.synthesis = SupportedSynthesisValidator()
        self.uncertainty = UncertaintyValidator()
        self.review_trigger = ReviewTriggerValidator()
        self.handoff = HandoffValidator()

    @classmethod
    def from_repo(cls, repo_root: Path) -> "Evaluator":
        return cls(
            fixtures=load_fixtures(repo_root),
            edges=load_edges(repo_root),
            source_manifest=load_source_manifest(repo_root),
            gold_cases=load_gold_cases(repo_root),
            repo_root=repo_root,
            source_asset_manifest=load_source_asset_manifest(repo_root),
            forensic_manifest=load_forensic_manifest(repo_root),
            lineage_map=load_lineage_map(repo_root),
            control_framework=load_control_framework(repo_root),
        )

    def evaluate_all(self) -> list[EvaluationResult]:
        return [self.evaluate_fixture(fixture) for fixture in self.fixtures]

    def evaluate_fixture(self, fixture: dict[str, Any]) -> EvaluationResult:
        gold = self.gold_by_artifact[fixture["artifact_id"]]
        admission = validate_fixture_admission(fixture)
        source_integrity = self.source_integrity.validate(fixture)
        provenance = self.provenance.validate(fixture)
        quote_fidelity = self.quote_fidelity.validate(fixture)
        authority = self.authority.validate(fixture)
        role = self.roles.validate(fixture)
        capture = self.capture.validate(fixture)
        representation = self.representation.validate(fixture)
        legal_method = self.legal_method.validate(fixture)
        graph = self.graph.validate_fixture(fixture)
        synthesis = self.synthesis.validate(fixture)
        uncertainty = self.uncertainty.validate(fixture)
        review_trigger = self.review_trigger.validate(fixture)

        gold_checks = self._gold_requirement_checks(fixture, gold)
        if gold_checks:
            if any(check.startswith("required_authority") for check in gold_checks):
                authority = self._merge_result(authority, "fail", gold_checks)
            else:
                provenance = self._merge_result(provenance, "fail", gold_checks)

        route, state, handoff = self.handoff.resolve(
            fixture,
            source_integrity=source_integrity,
            provenance=provenance,
            quote_fidelity=quote_fidelity,
            authority=authority,
            role=role,
            capture=capture,
            representation=representation,
            legal_method=legal_method,
            graph=graph,
            synthesis=synthesis,
            uncertainty=uncertainty,
            review_trigger=review_trigger,
        )

        failed_checks = tuple(
            dict.fromkeys(
                admission.failed_checks
                + source_integrity.failed_checks
                + provenance.failed_checks
                + quote_fidelity.failed_checks
                + authority.failed_checks
                + role.failed_checks
                + capture.failed_checks
                + representation.failed_checks
                + legal_method.failed_checks
                + graph.failed_checks
                + synthesis.failed_checks
                + uncertainty.failed_checks
                + review_trigger.failed_checks
                + handoff.failed_checks
            )
        )

        human_review_required = route in {"review", "blocked", "unresolved"} or state != "stable"
        expected_categories = set(gold["expected_failure_categories"])
        passed_gold = (
            route == gold["expected_route"]
            and state == gold["expected_control_state"]
            and human_review_required == gold["human_review_required"]
            and expected_categories.issubset(set(failed_checks))
        )

        return EvaluationResult(
            scenario_id=fixture["scenario_id"],
            artifact_id=fixture["artifact_id"],
            fixture_class=fixture["fixture_class"],
            artifact_type=fixture["artifact_type"],
            agent_stage=fixture.get("agent_stage", ""),
            jurisdiction=fixture.get("jurisdiction", ""),
            candidate_hs_code=fixture.get("candidate_hs_code"),
            candidate_cn_code=fixture.get("candidate_cn_code"),
            authority_status=authority.status,
            provenance_status=provenance.status,
            source_integrity_status=source_integrity.status,
            quote_fidelity_status=quote_fidelity.status,
            capture_status=capture.status,
            representation_status=representation.status,
            legal_method_status=legal_method.status,
            graph_parity_status=graph.status,
            synthesis_status=synthesis.status,
            uncertainty_status=uncertainty.status,
            handoff_status=handoff.status,
            failed_checks=failed_checks,
            expected_route=gold["expected_route"],
            actual_route=route,
            expected_control_state=gold["expected_control_state"],
            final_control_state=state,
            human_review_required=human_review_required,
            passed_gold=passed_gold,
            severity=self._severity(route, state, failed_checks),
            recommended_action=self._recommended_action(route, state),
            details={
                "admission_status": admission.status,
                "source_integrity_status": source_integrity.status,
                "quote_fidelity_status": quote_fidelity.status,
                "capture_status": capture.status,
                "representation_status": representation.status,
                "legal_method_status": legal_method.status,
                "synthesis_status": synthesis.status,
                "review_trigger_status": review_trigger.status,
                "gold_description": gold.get("description"),
            },
        )

    def _gold_requirement_checks(self, fixture: dict[str, Any], gold: dict[str, Any]) -> tuple[str, ...]:
        checks: list[str] = []
        classes = self.authority.authority_classes(fixture)
        anchors = self.authority.source_anchors(fixture)
        required_classes = {canonical_authority_class(value) for value in gold["required_authority_classes"]}
        missing_classes = required_classes - classes
        missing_anchors = set(gold["required_source_anchors"]) - anchors
        if missing_classes:
            checks.append("required_authority_class_missing")
        if missing_anchors:
            checks.append("required_source_anchor_missing")
        return tuple(checks)

    @staticmethod
    def _merge_result(result: ValidatorResult, status: str, checks: tuple[str, ...]) -> ValidatorResult:
        merged_checks = tuple(dict.fromkeys(result.failed_checks + checks))
        if status == "fail" or result.status == "fail":
            return ValidatorResult.fail(*merged_checks)
        if status == "review" or result.status == "review":
            return ValidatorResult.review(*merged_checks)
        return ValidatorResult(status=result.status, failed_checks=merged_checks)

    @staticmethod
    def _severity(route: str, state: str, failed_checks: tuple[str, ...]) -> str:
        if route == "blocked" or state in {"gap", "parity_failure"}:
            return "blocker"
        if route == "review" or state == "contested":
            return "review_trigger"
        if failed_checks:
            return "warning"
        return "pass"

    @staticmethod
    def _recommended_action(route: str, state: str) -> str:
        if route == "promote" and state == "stable":
            return "promote"
        if route == "review":
            return "route_to_human_review"
        if state == "parity_failure":
            return "block_pending_graph_repair"
        if route == "blocked":
            return "block_pending_source_or_authority_repair"
        return "hold_unresolved"
