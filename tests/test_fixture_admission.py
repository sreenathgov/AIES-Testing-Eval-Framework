from __future__ import annotations

from copy import deepcopy

from legal_extract_eval.fixture_admission import validate_fixture_admission


def test_curated_fixtures_pass_admission(fixtures: list[dict]) -> None:
    assert len(fixtures) == 15
    assert {fixture["fixture_class"] for fixture in fixtures} == {"good", "bad", "borderline"}
    assert sum(1 for fixture in fixtures if fixture["fixture_class"] == "good") == 5
    assert sum(1 for fixture in fixtures if fixture["fixture_class"] == "bad") == 5
    assert sum(1 for fixture in fixtures if fixture["fixture_class"] == "borderline") == 5

    for fixture in fixtures:
        result = validate_fixture_admission(fixture)
        assert result.status == "pass", fixture["artifact_id"]


def test_admission_rejects_non_artifact_files(fixtures: list[dict]) -> None:
    fixture = deepcopy(fixtures[0])
    fixture["artifact_type"] = "notes_file"
    fixture["fixture_class"] = ""
    fixture["artifact_origin"]["origin_label"] = "README scratch log notes"
    fixture["legal_proposition"] = ""
    fixture["graph_nodes"] = []
    fixture["handoff_route"] = ""
    fixture["source_ids"] = []
    fixture["legal_authority_chain"] = []
    fixture["known_issue_tags"] = []

    result = validate_fixture_admission(fixture)

    assert result.status == "fail"
    assert "unrecognized_artifact_type" in result.failed_checks
    assert "excluded_non_artifact_file" in result.failed_checks
    assert "missing_fixture_class" in result.failed_checks
    assert "not_parseable_legal_artifact" in result.failed_checks
    assert "source_linkage_missing_without_bad_fixture_tag" in result.failed_checks


def test_bad_fixture_can_intentionally_lack_source_linkage(fixtures: list[dict]) -> None:
    fixture = deepcopy(fixtures[0])
    fixture["fixture_class"] = "bad"
    fixture["source_ids"] = []
    fixture["legal_authority_chain"] = []
    fixture["known_issue_tags"] = ["source_linkage_intentionally_absent"]

    result = validate_fixture_admission(fixture)

    assert "source_linkage_missing_without_bad_fixture_tag" not in result.failed_checks
