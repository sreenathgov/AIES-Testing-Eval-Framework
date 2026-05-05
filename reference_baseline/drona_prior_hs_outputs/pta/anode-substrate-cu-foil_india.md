---
agent: PTA
component: Anode Substrate (Cu Foil)
entity_id: ent_tb3_06
jurisdiction: India
fundamental_function: CURRENT_COLLECTOR
material_composition: "Copper foil; purity ≥99.85% Cu (refined copper); thickness 6-12μm (≤0.15mm); not backed; rolled"
is_composite_flagged: false
gri_3_required: false
hs_code_candidate: "7410.11"
gri_path: GRI_1
stability: stable
confidence: high
validation_status: validated
corpus_gap: false
batch: TB-3
refinement_run: "2026-04-06"
source_doc: "HS - DR - GapFilling - Battery Material Tariff Classification Research.md"
source_section: "GRI Analysis; Chapter 74 copper foil heading; refined copper threshold"
ruling_anchor: "ITC-HS Section XV Note 2 (parts of general use → Chapter 74); ITC-HS Chapter 74 Note (refined copper ≥99.85%); ITC-HS 7410.11.10"
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XV Note 2 (parts of general use) | **YES — FIRED** | Cu foil = part of general use → Chapter 74 |
| Section XVII Note 2(f) | No | Not electrical machinery |
| Chapter 90 Note 2 | No | Not a measuring instrument |

`exclusion_checks_run: ["Section XV Note 2", "Section XVII Note 2(f)", "Chapter 90 Note 2"]`
`section_xv_note_2_fired: true`

## GRI Analysis

**Step 1 — Section XV Note 2 Applies**

India ITC-HS Section XV Note 2 is identical to WCO text. Copper foil = part of general use → Chapter 74.

**Step 2 — Purity Threshold**

ITC-HS Chapter 74 Note 1: "refined copper" = copper of a minimum purity by weight of 99.85%. Battery-grade Cu foil at ≥99.97% qualifies.

**Step 3 — Chapter 74 Classification**

ITC-HS Heading 7410: "Copper foil... of a thickness not exceeding 0.15mm."
Subheading 7410.11: "Of refined copper."
ITC-HS 8-digit structure:
- 7410.11.10: Of a thickness not exceeding 0.1mm
- 7410.11.20: Of a thickness exceeding 0.1mm

Battery-grade Cu foil at 6-12μm < 0.1mm → **7410.11.10** (ITC-HS).

## Classification

- **Code**: 7410.11.10 (ITC-HS — Cu foil of refined copper, thickness ≤0.1mm)
- **Basis**: GRI 1 + GRI 6; Section XV Note 2 → Chapter 74; refined copper ≥99.85% threshold met; ITC-HS 8-digit split at 0.1mm; battery-grade foil (6-12μm) → 7410.11.10
- **Stability**: stable
- **Confidence**: high

## Graph Links

- `classification_node` → [[product_component-anode-substrate-cu-foil]]
- `classified_as` → [[hs_code-7410-11-in]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
