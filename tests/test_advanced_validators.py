from __future__ import annotations

from copy import deepcopy
from pathlib import Path

from legal_extract_eval.data_loader import (
    load_forensic_manifest,
    load_lineage_map,
    load_source_asset_manifest,
)
from legal_extract_eval.legal_method_validator import LegalMethodValidator
from legal_extract_eval.material_capture_validator import MaterialCaptureValidator
from legal_extract_eval.quote_fidelity_validator import QuoteFidelityValidator
from legal_extract_eval.representation_integrity_validator import RepresentationIntegrityValidator
from legal_extract_eval.review_trigger_validator import ReviewTriggerValidator
from legal_extract_eval.source_integrity_validator import SourceIntegrityValidator
from legal_extract_eval.supported_synthesis_validator import SupportedSynthesisValidator


def test_source_integrity_resolves_assets_and_lineage(
    repo_root: Path,
    fixture_by_id: dict[str, dict],
) -> None:
    validator = SourceIntegrityValidator(
        repo_root,
        load_source_asset_manifest(repo_root),
        load_forensic_manifest(repo_root),
        load_lineage_map(repo_root),
    )

    result = validator.validate(fixture_by_id["FX_GOOD_OBC_AA_EU"])

    assert result.status == "pass"


def test_quote_fidelity_requires_declared_anchor(
    repo_root: Path,
    fixture_by_id: dict[str, dict],
    source_manifest: dict,
) -> None:
    fixture = deepcopy(fixture_by_id["FX_GOOD_OBC_AA_EU"])
    fixture["quoted_span_or_row_ref"].remove("WCO_GRI_1")
    validator = QuoteFidelityValidator(repo_root, source_manifest, load_source_asset_manifest(repo_root))

    result = validator.validate(fixture)

    assert result.status == "fail"
    assert "quote_anchor_not_declared_by_fixture" in result.failed_checks


def test_material_capture_detects_missing_gri_6_for_cn_claim(
    fixture_by_id: dict[str, dict],
) -> None:
    fixture = deepcopy(fixture_by_id["FX_GOOD_OBC_AA_EU"])
    fixture["gri_path"] = ["GRI_1"]

    result = MaterialCaptureValidator().validate(fixture)

    assert result.status == "review"
    assert "gri_6_missing_for_subheading_claim" in result.failed_checks


def test_legal_method_detects_malformed_cn_code(fixture_by_id: dict[str, dict]) -> None:
    fixture = deepcopy(fixture_by_id["FX_GOOD_OBC_AA_EU"])
    fixture["candidate_cn_code"] = "8504-40-90"

    result = LegalMethodValidator().validate(fixture)

    assert result.status == "review"
    assert "cn_code_syntax_invalid" in result.failed_checks


def test_ruling_applicability_is_checked(fixture_by_id: dict[str, dict]) -> None:
    fixture = deepcopy(fixture_by_id["FX_GOOD_HV_BATTERY_PACK_BTI_EU"])
    fixture["ruling_applicability"] = {}

    result = LegalMethodValidator().validate(fixture)

    assert result.status == "review"
    assert "ruling_binding_status_missing" in result.failed_checks
    assert "ruling_product_similarity_missing" in result.failed_checks


def test_supported_synthesis_blocks_internal_authority(fixture_by_id: dict[str, dict]) -> None:
    result = SupportedSynthesisValidator().validate(
        fixture_by_id["FX_BAD_HS_85044084_INTERNAL_AUTHORITY"]
    )

    assert result.status == "fail"
    assert "internal_source_as_authority" in result.failed_checks


def test_representation_integrity_detects_overloaded_product_node(
    fixture_by_id: dict[str, dict],
) -> None:
    result = RepresentationIntegrityValidator().validate(
        fixture_by_id["FX_BORDERLINE_LI_CELL_PRODUCT_NODE_MIXED_STATE"]
    )

    assert result.status == "review"
    assert "product_identity_mixed_with_classification_state" in result.failed_checks


def test_review_trigger_requires_reason_codes(fixture_by_id: dict[str, dict]) -> None:
    fixture = deepcopy(fixture_by_id["FX_BORDERLINE_NOES_CLIENT_FACT"])
    fixture["review_reason_codes"] = []

    result = ReviewTriggerValidator().validate(fixture)

    assert result.status == "review"
    assert "review_reason_codes_missing" in result.failed_checks
