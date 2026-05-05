from __future__ import annotations

from .models import REVIEW_CHECKS, ValidatorResult


class HandoffValidator:
    def resolve(
        self,
        fixture: dict,
        *,
        provenance: ValidatorResult,
        authority: ValidatorResult,
        role: ValidatorResult,
        graph: ValidatorResult,
        uncertainty: ValidatorResult,
        source_integrity: ValidatorResult | None = None,
        quote_fidelity: ValidatorResult | None = None,
        capture: ValidatorResult | None = None,
        representation: ValidatorResult | None = None,
        legal_method: ValidatorResult | None = None,
        synthesis: ValidatorResult | None = None,
        review_trigger: ValidatorResult | None = None,
    ) -> tuple[str, str, ValidatorResult]:
        checks: list[str] = []
        source_integrity = source_integrity or ValidatorResult.pass_()
        quote_fidelity = quote_fidelity or ValidatorResult.pass_()
        capture = capture or ValidatorResult.pass_()
        representation = representation or ValidatorResult.pass_()
        legal_method = legal_method or ValidatorResult.pass_()
        synthesis = synthesis or ValidatorResult.pass_()
        review_trigger = review_trigger or ValidatorResult.pass_()
        all_checks = set(
            source_integrity.failed_checks
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
        )

        if graph.status == "fail":
            return "blocked", "parity_failure", ValidatorResult.fail(*graph.failed_checks)

        blocking_results = (source_integrity, provenance, quote_fidelity, authority, synthesis)
        if any(result.status == "fail" for result in blocking_results):
            for result in blocking_results:
                checks.extend(result.failed_checks)
            if fixture.get("handoff_route") == "promote":
                checks.append("unsupported_promotion")
            return "blocked", "gap", ValidatorResult.fail(*checks)

        review_results = (role, capture, representation, legal_method, uncertainty, review_trigger)
        if all_checks & REVIEW_CHECKS or any(result.status == "review" for result in review_results):
            for result in review_results:
                checks.extend(result.failed_checks)
            if {"confidence_inflation", "divergence_collapsed"} & all_checks and fixture.get("handoff_route") == "promote":
                checks.append("unsupported_promotion")
            return "review", "contested", ValidatorResult.review(*checks)

        if fixture.get("handoff_route") == "review":
            return "review", "contested", ValidatorResult.review("review_route_declared")

        if fixture.get("handoff_route") == "blocked":
            return "blocked", "gap", ValidatorResult.fail("blocked_route_declared")

        return "promote", "stable", ValidatorResult.pass_()
