---
agent: PTA
component: Silicon-Alloyed Electrical Steel Core (NOES)
entity_id: ent_tb3_07
jurisdiction: India
fundamental_function: MAGNETIC_CORE
material_composition: "Non-oriented electrical steel (NOES); silicon content 0.5-3.5% by weight; flat-rolled; for traction motor stator/rotor laminations"
is_composite_flagged: false
gri_3_required: false
hs_code_candidate: "7226.19"
hs_code_candidate_alt: "7225.19"
gri_path: GRI_1
stability: stable
confidence: medium
width_determination: "data_pending — typical motor lamination slit coil <600mm"
client_fact_pending: true
client_fact_key: "coil_width_mm"
client_fact_note: "Classification depends on width as imported: width <600mm -> 7226.19.00; width >=600mm -> 7225.19.00."
legal_rule_resolved: true
validation_status: validated
corpus_gap: false
batch: TB-3
refinement_run: "2026-04-06"
source_doc: "HS - DR - GapFilling - Electrical Steel Width-Split Resolution.md"
source_section: "GRI Analysis; ITC-HS width split at 600mm; slit coil import condition"
ruling_anchor: "ITC-HS Section XV Note 2 (base metal → Chapter 72); ITC-HS Chapter 72 width split: 7225 (≥600mm), 7226 (<600mm); ITC-HS 7226.19.00"
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XV Note 2 (parts of general use) | **YES — FIRED** | Silicon-alloyed electrical steel = base metal of general use → Chapter 72 |
| Section XVII Note 2(f) | No | Not electrical machinery |
| Chapter 90 Note 2 | No | Not a measuring instrument |

`exclusion_checks_run: ["Section XV Note 2", "Section XVII Note 2(f)", "Chapter 90 Note 2"]`
`section_xv_note_2_fired: true`

## GRI Analysis

**Step 1 — Section XV Note 2 Applies**

India ITC-HS Section XV Note 2 is identical to WCO text. NOES electrical steel = base metal material of general use → Chapter 72.

**Step 2 — Width-Based Classification**

ITC-HS Chapter 72 applies the same 600mm width split:
- **7225**: Flat-rolled products of other alloy steel, width ≥600mm
  - 7225.19.00: Other (NOES, ≥600mm)
- **7226**: Flat-rolled products of other alloy steel, width <600mm
  - 7226.19.00: Other (NOES, <600mm)

India ITC-HS does not further subdivide 7226.19 at the 8-digit level by thickness (unlike EU CN). India retains 7226.19.00 as a single subheading.

Motor lamination slit coil (width <600mm, per commercial supply chain default) → **7226.19.00** (ITC-HS).

## Classification

- **Code**: 7226.19.00 (ITC-HS — NOES flat-rolled, width <600mm)
- **Alt Code**: 7225.19.00 (ITC-HS — if imported as master coil ≥600mm)
- **Basis**: GRI 1 + GRI 6; Section XV Note 2 → Chapter 72; width split at 600mm; motor lamination slit coil default <600mm → 7226.19.00
- **Stability**: stable
- **Confidence**: medium (width confirmation required; no India-specific NOES ruling found)

## Graph Links

- `classification_node` → [[product_component-silicon-alloyed-electrical-steel-core-noes]]
- `classified_as` → [[hs_code-7226-19-in]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
