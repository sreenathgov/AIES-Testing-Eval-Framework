from __future__ import annotations

from .models import RECOGNIZED_ARTIFACT_TYPES, ValidatorResult


EXCLUDED_ORIGIN_TOKENS = ("readme", "scratch", "log", "notes")


def validate_fixture_admission(fixture: dict) -> ValidatorResult:
    checks: list[str] = []

    if fixture.get("artifact_type") not in RECOGNIZED_ARTIFACT_TYPES:
        checks.append("unrecognized_artifact_type")

    origin_label = str(fixture.get("artifact_origin", {}).get("origin_label", "")).lower()
    if any(token in origin_label for token in EXCLUDED_ORIGIN_TOKENS):
        checks.append("excluded_non_artifact_file")

    if fixture.get("fixture_class") not in {"good", "bad", "borderline"}:
        checks.append("missing_fixture_class")

    has_legal_content = bool(str(fixture.get("legal_proposition", "")).strip())
    has_graph_node = bool(fixture.get("graph_nodes"))
    has_route = bool(fixture.get("handoff_route"))
    if not (has_legal_content or has_graph_node or has_route):
        checks.append("not_parseable_legal_artifact")

    has_source_link = bool(fixture.get("source_ids") or fixture.get("legal_authority_chain"))
    intentionally_absent = "source_linkage_intentionally_absent" in fixture.get("known_issue_tags", [])
    if not has_source_link and not (fixture.get("fixture_class") == "bad" and intentionally_absent):
        checks.append("source_linkage_missing_without_bad_fixture_tag")

    return ValidatorResult.pass_() if not checks else ValidatorResult.fail(*checks)
