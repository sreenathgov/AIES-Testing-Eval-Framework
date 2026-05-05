---
agent: PTA
component: Cathode Substrate (Al Foil)
entity_id: ent_tb3_05
jurisdiction: EU
fundamental_function: CURRENT_COLLECTOR
material_composition: "Aluminum foil; purity ≥99% Al; thickness 10-20μm (≤0.2mm); not backed; rolled but not further worked"
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
source_section: "GRI Analysis; Chapter 76 foil heading; bare versus electrode-coated foil"
ruling_anchor: "EU CN Chapter 76 Note (foil = ≤0.2mm); Section XV Note 2 (parts of general use → base metal chapter); EU CN 7607.11.10 (thickness <0.021mm)"
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XV Note 2 (parts of general use) | **YES — FIRED** | Al foil = part of general use → Chapter 76, not Chapter 85 |
| Section XVII Note 2(f) | No | Not electrical machinery |
| Chapter 90 Note 2 | No | Not a measuring instrument |

`exclusion_checks_run: ["Section XV Note 2", "Section XVII Note 2(f)", "Chapter 90 Note 2"]`
`section_xv_note_2_fired: true`

## GRI Analysis

**Step 1 — Section XV Note 2 Applies**

EU CN Section XV Note 2 functions identically to WCO text: parts of general use classifies in base material chapters. Bare aluminum foil is a widely used industrial material → routes to Chapter 76.

**Step 2 — Chapter 76 Classification**

EU CN Heading 7607: "Aluminium foil (whether or not printed or backed with paper, paperboard, plastics or similar backing materials) of a thickness (excluding any backing) not exceeding 0·2 mm."
Subheading 7607.11: "Not backed: Rolled but not further worked."

EU CN 8-digit structure for 7607.11:
- **7607.11.10**: Thickness <0.021mm
- **7607.11.90**: Other (thickness ≥0.021mm to ≤0.2mm)

Battery-grade Al foil: typically 10-20μm:
- 10-20μm = 0.010-0.020mm < 0.021mm → **7607.11.10**

Battery cathode Al foil at standard battery grade (10-20μm) classifies under EU CN **7607.11.10**.

## Classification

- **Code**: 7607.11.10 (EU CN — Al foil <0.021mm, not backed, rolled)
- **Basis**: GRI 1 + GRI 6; Section XV Note 2 → Chapter 76; Heading 7607.11; EU CN 8-digit split at 0.021mm; battery-grade foil (10-20μm) falls in <0.021mm bracket → 7607.11.10
- **Stability**: stable
- **Confidence**: high

## Graph Links

- `classification_node` → [[product_component-cathode-substrate-al-foil]]
- `classified_as` → [[hs_code-7607-11-eu]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
