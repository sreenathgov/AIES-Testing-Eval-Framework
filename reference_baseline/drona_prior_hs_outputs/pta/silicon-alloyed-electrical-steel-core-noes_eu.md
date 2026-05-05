---
agent: PTA
component: Silicon-Alloyed Electrical Steel Core (NOES)
entity_id: ent_tb3_07
jurisdiction: EU
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
client_fact_note: "Classification depends on width as imported: width <600mm -> 7226.19.10; width >=600mm -> 7225.19.90."
legal_rule_resolved: true
validation_status: validated
corpus_gap: false
batch: TB-3
refinement_run: "2026-04-06"
source_doc: "HS - DR - GapFilling - Electrical Steel Width-Split Resolution.md"
source_section: "GRI Analysis; CN width split at 600mm; slit coil import condition"
ruling_anchor: "EU CN Chapter 72 width split identical to WCO: 7225 (≥600mm), 7226 (<600mm); EU CN 7226.19.10 (other flat-rolled NOES)"
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

EU CN Section XV Note 2 identical to WCO: NOES electrical steel = base metal material of general use → Chapter 72.

**Step 2 — Width-Based Classification**

EU CN Chapter 72 applies the same 600mm width split as WCO:
- **7225**: Flat-rolled products of other alloy steel, width ≥600mm
  - 7225.19: Other (NOES, ≥600mm)
- **7226**: Flat-rolled products of other alloy steel, width <600mm
  - 7226.19: Other (NOES, <600mm)

EU CN 8-digit for 7226.19:
- **7226.19.10**: Of a thickness of less than 0.5mm
- **7226.19.80**: Other (thickness ≥0.5mm)

NOES for motor laminations: thickness typically 0.2-0.5mm (standard EV motor grade is 0.27mm, 0.35mm, or 0.50mm).
- 0.27mm or 0.35mm → **7226.19.10** (thickness <0.5mm)
- 0.50mm → **7226.19.10** (technically <0.5mm) or borderline; confirm specification

**Primary position (motor lamination grade)**: EU CN **7226.19.10** (width <600mm, thickness <0.5mm).

## Classification

- **Code**: 7226.19.10 (EU CN — NOES flat-rolled, width <600mm, thickness <0.5mm; motor lamination grade)
- **Alt Code**: 7225.19.90 (EU CN — if imported as master coil ≥600mm)
- **Basis**: GRI 1 + GRI 6; Section XV Note 2 → Chapter 72; width split at 600mm → 7226; EU CN 8-digit split at 0.5mm; motor lamination NOES (0.27-0.35mm) → 7226.19.10
- **Stability**: stable
- **Confidence**: medium (width/thickness confirmation required per supply chain spec)

## Graph Links

- `classification_node` → [[product_component-silicon-alloyed-electrical-steel-core-noes]]
- `classified_as` → [[hs_code-7226-19-eu]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
