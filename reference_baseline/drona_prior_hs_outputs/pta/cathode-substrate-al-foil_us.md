---
agent: PTA
component: Cathode Substrate (Al Foil)
entity_id: ent_tb3_05
jurisdiction: US
fundamental_function: CURRENT_COLLECTOR
material_composition: "Aluminum foil; purity ≥99% Al; thickness 10-20μm (≤0.2mm); not backed; rolled but not further worked; used as cathode current collector in lithium-ion battery cells"
is_composite_flagged: false
gri_3_required: false
hs_code_candidate: "7607.11"
gri_path: GRI_1
stability: stable
confidence: high
validation_status: validated
corpus_gap: false
batch: TB-3
refinement_run: "2026-04-06"
source_doc: "HS - DR - GapFilling - Battery Material Tariff Classification Research.md"
source_section: "GRI Analysis; Chapter 76 foil heading; CBP NY N303974"
ruling_anchor: "CBP NY N303974 (bare Al foil → 7607.11; coated Al foil → 8507.90); HTSUS Chapter 76 Note (foil = ≤0.2mm)"
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XV Note 2 (parts of general use) | **YES — FIRED** | Al foil is a "part of general use" per Section XV Note 2 → classifies in base material chapter (Chapter 76), NOT Chapter 85 or 87 |
| Section XVII Note 2(f) | No | Not electrical machinery |
| Chapter 90 Note 2 | No | Not a measuring instrument |

`exclusion_checks_run: ["Section XV Note 2", "Section XVII Note 2(f)", "Chapter 90 Note 2"]`
`section_xv_note_2_fired: true`
`section_xv_result: "Al foil is part of general use → Chapter 76, not Chapter 85"`

## GRI Analysis

**Step 1 — Section XV Note 2 Applies**

Section XV Note 2: "Parts of general use" as defined in Note 2 to Section XV include articles of Chapter 82 or 83 and similar articles of other base metals. However, foils are not enumerated. The controlling analysis is: aluminum foil is a commercial product used across many industries (food packaging, electrical, pharmaceutical, industrial) — it is NOT exclusively or principally used as a battery current collector. Section XV Note 2 therefore routes it to the base metals chapter (Chapter 76) when imported as a standalone material.

**Step 2 — Chapter 76 Classification**

HTSUS Chapter 76 — Aluminum and articles thereof.
Heading 7607: "Aluminum foil (whether or not printed or backed with paper, paperboard, plastics or similar backing materials) of a thickness (excluding any backing) not exceeding 0.2mm."
Subheading 7607.11: "Not backed: Rolled but not further worked."

Battery-grade cathode Al foil: thickness 10-20μm (<0.2mm), bare (uncoated in as-imported state), rolled → **7607.11**.

HTSUS: 7607.11.3000 (for foil of a thickness <0.01mm) or 7607.11.6000 (for thickness ≥0.01mm). Battery-grade foil at 10-20μm = ≥0.01mm → **7607.11.6000**.

**CBP NY N303974 qualification**: CBP ruled that bare (uncoated) Al foil classifies under 7607.11. If the Al foil is coated with electrode material (cathode active material slurry applied) before import, it shifts to 8507.90 as a battery electrode part. Battery-grade Al foil imported as a standalone roll (bare) = 7607.11.

## Classification

- **Code**: 7607.11.6000 (US HTSUS; Al foil ≥0.01mm, not backed, rolled)
- **Basis**: GRI 1; Section XV Note 2 routes bare Al foil to Chapter 76; Heading 7607.11 (not backed, rolled, ≤0.2mm); CBP NY N303974 basis
- **Stability**: stable
- **Confidence**: high

## Conditional Note for DRONA

- IF Al foil = bare, uncoated, imported as roll → **7607.11.6000** (US)
- IF Al foil = pre-coated with cathode active material (electrode) → **8507.90.8000** (US, battery electrode part)
- Cathode substrate as imported (bare roll): 7607.11.6000

## Graph Links

- `classification_node` → [[product_component-cathode-substrate-al-foil]]
- `classified_as` → [[hs_code-7607-11-us]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
