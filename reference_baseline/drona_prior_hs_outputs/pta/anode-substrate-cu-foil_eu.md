---
agent: PTA
component: Anode Substrate (Cu Foil)
entity_id: ent_tb3_06
jurisdiction: EU
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
ruling_anchor: "EU CN Chapter 74 Note (refined copper ≥99.85%); EU CN 7410.11.00 (foil of refined copper ≤0.15mm)"
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

EU CN Section XV Note 2 is identical to WCO text. Copper foil is a base metal article of general use → Chapter 74.

**Step 2 — Purity Threshold**

EU CN Chapter 74 Note 1: "refined copper" = copper of a minimum purity by weight of 99.85%. Battery-grade electrodeposited Cu foil at ≥99.97% qualifies.

**Step 3 — Chapter 74 Classification**

EU CN Heading 7410: "Copper foil... of a thickness (excluding any backing) not exceeding 0.15mm."
Subheading 7410.11: "Of refined copper."
EU CN 8-digit: **7410.11.00** (single 8-digit subheading for foil of refined copper — no further EU CN split at this level).

Battery-grade Cu foil: 6-12μm, ≥99.97% purity → **7410.11.00** (EU CN).

## Classification

- **Code**: 7410.11.00 (EU CN — Cu foil of refined copper, thickness ≤0.15mm)
- **Basis**: GRI 1 + GRI 6; Section XV Note 2 → Chapter 74; refined copper ≥99.85% threshold met; EU CN 7410.11.00
- **Stability**: stable
- **Confidence**: high

## Graph Links

- `classification_node` → [[product_component-anode-substrate-cu-foil]]
- `classified_as` → [[hs_code-7410-11-eu]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
