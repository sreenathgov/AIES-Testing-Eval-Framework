---
agent: PTA
component: Cathode Substrate (Al Foil)
entity_id: ent_tb3_05
jurisdiction: India
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
ruling_anchor: "ITC-HS Section XV Note 2 (parts of general use → base metal chapter); ITC-HS 7607.11.10 (Al foil not backed, rolled)"
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

India ITC-HS Section XV Note 2 is identical to WCO text. Aluminum foil is a material of general use → routes to Chapter 76 (aluminum and articles thereof).

**Step 2 — Chapter 76 Classification**

ITC-HS Heading 7607: "Aluminium foil... of a thickness not exceeding 0.2mm."
Subheading 7607.11: "Not backed: Rolled but not further worked."
ITC-HS 7607.11.10: "Of a thickness not exceeding 0.1mm"

Battery-grade Al foil at 10-20μm ≤ 0.1mm → **7607.11.10** (ITC-HS).

Note: ITC-HS uses 0.1mm as the split point (vs. EU's 0.021mm). Battery foil at 10-20μm is well below 0.1mm → 7607.11.10 in India.

## Classification

- **Code**: 7607.11.10 (ITC-HS — Al foil not backed, rolled, thickness ≤0.1mm)
- **Basis**: GRI 1 + GRI 6; Section XV Note 2 → Chapter 76; Heading 7607.11; ITC-HS 8-digit split at 0.1mm; battery-grade foil (10-20μm) → 7607.11.10
- **Stability**: stable
- **Confidence**: high

## Graph Links

- `classification_node` → [[product_component-cathode-substrate-al-foil]]
- `classified_as` → [[hs_code-7607-11-in]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
