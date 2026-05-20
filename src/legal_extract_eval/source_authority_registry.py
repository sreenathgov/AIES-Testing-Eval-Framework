from __future__ import annotations

from dataclasses import dataclass
from typing import Any


PAPER_SCOPE_JURISDICTIONS = frozenset({"EU", "WCO"})
PAPER_SCOPE_SOURCE_CLASSES = frozenset({"EU", "WCO", "BTI"})

CANONICAL_AUTHORITY_CLASSES = frozenset(
    {
        "primary_legal_text",
        "interpretive_legal_note",
        "ruling_or_precedent",
        "internal_generated_candidate",
    }
)

AUTHORITY_CLASS_ALIASES = {
    "classification_decision": "ruling_or_precedent",
}

SOURCE_ID_ALIASES = {
    "SRC_WCO_SECTION_XVI": ("SRC_WCO_SECTION_84", "SRC_WCO_SECTION_85", "SRC_WCO_SECTION_90"),
    "SRC_WCO_SECTION_XVII": ("SRC_WCO_SECTION_87",),
}


@dataclass(frozen=True)
class SourceAuthority:
    source_id: str
    jurisdiction: str
    authority_class: str
    source_role: str
    concrete_source_ids: tuple[str, ...] = ()

    @property
    def is_alias(self) -> bool:
        return bool(self.concrete_source_ids)


SOURCE_AUTHORITIES: dict[str, SourceAuthority] = {
    "SRC_EU_CN_2025_1926_EVS": SourceAuthority(
        "SRC_EU_CN_2025_1926_EVS",
        "EU",
        "primary_legal_text",
        "eu_combined_nomenclature_tariff_text",
    ),
    "SRC_EU_CN_EXPLANATORY_NOTES_EVS": SourceAuthority(
        "SRC_EU_CN_EXPLANATORY_NOTES_EVS",
        "EU",
        "interpretive_legal_note",
        "eu_combined_nomenclature_explanatory_notes",
    ),
    "SRC_EU_BTI_SAMPLE": SourceAuthority(
        "SRC_EU_BTI_SAMPLE",
        "EU",
        "ruling_or_precedent",
        "eu_bti_ruling_rows",
    ),
    "SRC_WCO_GRI_2017": SourceAuthority(
        "SRC_WCO_GRI_2017",
        "WCO",
        "primary_legal_text",
        "wco_general_rules_of_interpretation",
    ),
    "SRC_WCO_SECTION_84": SourceAuthority(
        "SRC_WCO_SECTION_84",
        "WCO",
        "primary_legal_text",
        "wco_chapter_84_heading_and_note_records",
    ),
    "SRC_WCO_SECTION_85": SourceAuthority(
        "SRC_WCO_SECTION_85",
        "WCO",
        "primary_legal_text",
        "wco_chapter_85_heading_and_note_records",
    ),
    "SRC_WCO_SECTION_87": SourceAuthority(
        "SRC_WCO_SECTION_87",
        "WCO",
        "primary_legal_text",
        "wco_chapter_87_heading_and_note_records",
    ),
    "SRC_WCO_SECTION_90": SourceAuthority(
        "SRC_WCO_SECTION_90",
        "WCO",
        "primary_legal_text",
        "wco_chapter_90_heading_and_note_records",
    ),
    "SRC_WCO_SECTION_XVI": SourceAuthority(
        "SRC_WCO_SECTION_XVI",
        "WCO",
        "interpretive_legal_note",
        "legacy_grouped_section_xvi_alias",
        SOURCE_ID_ALIASES["SRC_WCO_SECTION_XVI"],
    ),
    "SRC_WCO_SECTION_XVII": SourceAuthority(
        "SRC_WCO_SECTION_XVII",
        "WCO",
        "interpretive_legal_note",
        "legacy_grouped_section_xvii_alias",
        SOURCE_ID_ALIASES["SRC_WCO_SECTION_XVII"],
    ),
    "SRC_INTERNAL_CANDIDATE_ARTIFACT": SourceAuthority(
        "SRC_INTERNAL_CANDIDATE_ARTIFACT",
        "internal",
        "internal_generated_candidate",
        "artifact_origin_only_not_legal_authority",
    ),
}


def canonical_authority_class(authority_class: str | None) -> str | None:
    if authority_class is None:
        return None
    return AUTHORITY_CLASS_ALIASES.get(authority_class, authority_class)


def concrete_source_ids(source_id: str) -> tuple[str, ...]:
    authority = SOURCE_AUTHORITIES.get(source_id)
    if authority and authority.concrete_source_ids:
        return authority.concrete_source_ids
    return (source_id,)


def source_ids_overlap(left: str, right: str) -> bool:
    return bool(set(concrete_source_ids(left)) & set(concrete_source_ids(right)))


def registry_mismatches_for_source(source: dict[str, Any]) -> tuple[str, ...]:
    source_id = source.get("source_id")
    authority = SOURCE_AUTHORITIES.get(source_id)
    if authority is None:
        return ("source_id_not_registered",)

    checks: list[str] = []
    jurisdiction = source.get("jurisdiction")
    authority_class = canonical_authority_class(source.get("authority_class"))
    if jurisdiction != authority.jurisdiction:
        checks.append("source_jurisdiction_mismatch")
    if authority_class != authority.authority_class:
        checks.append("source_authority_class_mismatch")
    return tuple(checks)


def registry_mismatches_for_record_manifest_entry(entry: dict[str, Any]) -> tuple[str, ...]:
    source_id = entry.get("source_id")
    authority = SOURCE_AUTHORITIES.get(source_id)
    if authority is None:
        return ("source_id_not_registered",)
    if authority.is_alias:
        return ("record_manifest_uses_grouped_source_alias",)

    checks: list[str] = []
    if entry.get("jurisdiction") != authority.jurisdiction:
        checks.append("record_jurisdiction_mismatch")
    if canonical_authority_class(entry.get("authority_class")) != authority.authority_class:
        checks.append("record_authority_class_mismatch")
    return tuple(checks)
