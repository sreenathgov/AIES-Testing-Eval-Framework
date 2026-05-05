from __future__ import annotations

from copy import deepcopy

from legal_extract_eval.authority_boundary_validator import AuthorityBoundaryValidator
from legal_extract_eval.models import EXTERNAL_AUTHORITY_CLASSES, PAPER_SCOPE_JURISDICTIONS
from legal_extract_eval.provenance_validator import ProvenanceValidator


def test_external_authority_anchors_are_below_document_level(
    fixtures: list[dict],
    source_manifest: dict,
) -> None:
    sources = {source["source_id"]: source for source in source_manifest["sources"]}
    anchors = {
        (source["source_id"], anchor["anchor_id"]): anchor
        for source in source_manifest["sources"]
        for anchor in source.get("anchors", [])
    }

    for fixture in fixtures:
        for item in fixture["legal_authority_chain"]:
            if item["authority_class"] not in EXTERNAL_AUTHORITY_CLASSES:
                continue

            source = sources[item["source_id"]]
            anchor = anchors[(item["source_id"], item["anchor_id"])]

            assert source["jurisdiction"] in PAPER_SCOPE_JURISDICTIONS
            assert anchor["document_level_only"] is False


def test_internal_origin_is_not_legal_authority(
    fixture_by_id: dict[str, dict],
    source_manifest: dict,
) -> None:
    fixture = fixture_by_id["FX_GOOD_OBC_AA_EU"]

    assert fixture["artifact_origin"]["origin_type"].startswith("internal")
    assert all(item["authority_class"] != "internal_generated_candidate" for item in fixture["legal_authority_chain"])
    assert ProvenanceValidator(source_manifest).validate(fixture).status == "pass"
    assert AuthorityBoundaryValidator(source_manifest).validate(fixture).status == "pass"


def test_internal_candidate_authority_fails(
    fixture_by_id: dict[str, dict],
    source_manifest: dict,
) -> None:
    fixture = fixture_by_id["FX_BAD_HS_85044084_INTERNAL_AUTHORITY"]

    provenance = ProvenanceValidator(source_manifest).validate(fixture)
    authority = AuthorityBoundaryValidator(source_manifest).validate(fixture)

    assert provenance.status == "fail"
    assert authority.status == "fail"
    assert "internal_source_as_authority" in provenance.failed_checks
    assert "missing_external_authority" in provenance.failed_checks
    assert "internal_source_as_authority" in authority.failed_checks


def test_missing_anchor_fails_provenance(
    fixture_by_id: dict[str, dict],
    source_manifest: dict,
) -> None:
    fixture = deepcopy(fixture_by_id["FX_GOOD_OBC_AA_EU"])
    fixture["legal_authority_chain"][0].pop("anchor_id")

    result = ProvenanceValidator(source_manifest).validate(fixture)

    assert result.status == "fail"
    assert "missing_source_anchor" in result.failed_checks


def test_non_paper_scope_authority_is_rejected(
    fixture_by_id: dict[str, dict],
    source_manifest: dict,
) -> None:
    manifest = deepcopy(source_manifest)
    manifest["sources"].append(
        {
            "source_id": "SRC_US_COMPARISON_SAMPLE",
            "title": "US comparison sample",
            "authority_class": "primary_legal_text",
            "jurisdiction": "US",
            "source_path": None,
            "anchors": [
                {
                    "anchor_id": "US_SAMPLE_ANCHOR",
                    "anchor_type": "comparison",
                    "locator": "comparison only",
                    "label": "Comparison-only source",
                    "quoted_span": "comparison only",
                    "document_level_only": False,
                }
            ],
        }
    )
    fixture = deepcopy(fixture_by_id["FX_GOOD_OBC_AA_EU"])
    fixture["legal_authority_chain"].append(
        {
            "source_id": "SRC_US_COMPARISON_SAMPLE",
            "authority_class": "primary_legal_text",
            "anchor_id": "US_SAMPLE_ANCHOR",
        }
    )

    result = AuthorityBoundaryValidator(manifest).validate(fixture)

    assert result.status == "fail"
    assert "non_paper_scope_authority_used" in result.failed_checks
