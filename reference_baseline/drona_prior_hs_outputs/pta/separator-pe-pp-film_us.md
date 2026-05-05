---
agent: PTA
component: Separator (PE/PP Film)
entity_id: ent_tb3_04
jurisdiction: US
fundamental_function: IONIC_BARRIER
material_composition: "Microporous polyethylene (PE) or polypropylene (PP) film; thickness 10-25μm; microporous cellular structure enabling Li-ion transport while preventing electrode short-circuit"
is_composite_flagged: false
gri_3_required: false
hs_code_candidate: "3921.19"
gri_path: GRI_1
stability: stable
confidence: high
validation_status: validated
corpus_gap: false
jurisdiction_divergence: true
jurisdiction_divergence_note: "US: 3921.19.0000 (cellular plastics); EU: 8507.90.31 (<40μm battery separator carve-out); India: 3921.19.90 (cellular plastics)"
batch: TB-3
refinement_run: "2026-04-06"
source_doc: "HS - DR - GapFilling - Battery Material Tariff Classification Research.md"
source_section: "GRI Analysis; Chapter 39 cellular plastics boundary; CBP HQ 967313"
ruling_anchor: "CBP HQ 967313 (microporous PE separator → 3921.19; cellular plastic, not battery part)"
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XV Note 2 (parts of general use) | No | Plastic film, not base metal part |
| Section XVII Note 2(f) | No | Not electrical machinery |
| Chapter 90 Note 2 | No | Not a measuring instrument |

`exclusion_checks_run: ["Section XV Note 2", "Section XVII Note 2(f)", "Chapter 90 Note 2"]`

## GRI Analysis

**Step 1 — Material Identity**

The battery separator is a microporous polymer film — polyethylene (PE, heading 3920/3921) or polypropylene (PP, heading 3920/3921). The microporous structure (pores of ~0.1μm diameter) is created by biaxial stretching or phase-inversion processes.

**Step 2 — Cellular vs. Non-Cellular Plastics**

HTSUS Chapter 39 structures:
- Heading 3920: "Other plates, sheets, film, foil and strip, of plastics, non-cellular and not reinforced..."
- Heading 3921: "Other plates, sheets, film, foil and strip, of plastics" — includes cellular structure

The microporous structure of a battery separator = "cellular" plastics (Chapter 39 Note: cellular plastics defined to include porous plastics with a significant void fraction). PE separator with micropores = cellular PE plastic.

**CBP HQ 967313 (binding precedent)**: CBP classified microporous polyethylene battery separator film under **3921.19.0000** — "Other cellular plastic plates/sheets/film: Other." CBP analysis: the microporous PE film is primarily classified by its plastic material identity and cellular structure. The fact that it functions as a battery separator does not override the plastics classification; it is not "an integral part" of the battery as a separate import item.

HTSUS 3921.19.0000: Cellular plastics, of other polymers (i.e., not polyurethane — PE and PP both classify here).

**Step 3 — Chapter 85 Battery Part Analysis (US)**

HTSUS Chapter 85, Note 2 — parts of batteries (heading 8507): the term "parts" is not defined specifically; CBP applies the principle that parts must be integral and solely/principally used as battery parts. A separator film sold as a standalone roll for multiple downstream applications does not meet the "solely or principally" test → not 8507.90.

**CBP HQ 967313** explicitly rejects 8507.90 classification for PE separator film and confirms 3921.19.0000.

## Classification

- **Code**: 3921.19.0000 (US HTSUS, per CBP HQ 967313)
- **Basis**: GRI 1; microporous PE/PP separator = cellular plastic film; CBP HQ 967313 binding; Chapter 85 battery parts heading rejected
- **Stability**: stable
- **Confidence**: high

## Jurisdiction Divergence Flag

**CRITICAL**: US and EU classify this component differently.
- US: 3921.19.0000 (cellular plastic — plastics-first approach, CBP HQ 967313)
- EU: 8507.90.31 (battery part — <40μm carve-out, Commission Note C/2025/6096)
- India: 3921.19.90 (cellular plastic — follows material-first approach)

This divergence must be flagged in the AA classification candidate and documented for D-RULING handoff.

## Graph Links

- `classification_node` → [[product_component-separator-pe-pp-film]]
- `classified_as` → [[hs_code-3921-19-us]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
