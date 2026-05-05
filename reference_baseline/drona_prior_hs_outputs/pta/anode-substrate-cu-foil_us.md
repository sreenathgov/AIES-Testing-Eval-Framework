---
agent: PTA
component: Anode Substrate (Cu Foil)
entity_id: ent_tb3_06
jurisdiction: US
fundamental_function: CURRENT_COLLECTOR
material_composition: "Copper foil; purity ≥99.85% Cu (refined copper); thickness 6-12μm (≤0.15mm); not backed; rolled; used as anode current collector in lithium-ion battery cells"
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
source_section: "GRI Analysis; Chapter 74 refined copper note; CBP N090878"
ruling_anchor: "CBP N090878 (Cu foil of refined copper → 7410.11); HTSUS Chapter 74 Note ('refined copper' = ≥99.85% purity)"
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XV Note 2 (parts of general use) | **YES — FIRED** | Cu foil = part of general use → Chapter 74, not Chapter 85 |
| Section XVII Note 2(f) | No | Not electrical machinery |
| Chapter 90 Note 2 | No | Not a measuring instrument |

`exclusion_checks_run: ["Section XV Note 2", "Section XVII Note 2(f)", "Chapter 90 Note 2"]`
`section_xv_note_2_fired: true`

## GRI Analysis

**Step 1 — Section XV Note 2 Applies**

Section XV Note 2: copper foil is a base metal article of general use → routes to Chapter 74 (copper and articles thereof), not Chapter 85.

**Step 2 — Purity Threshold Determination**

HTSUS Chapter 74 Note: "Refined copper" = copper of ≥99.85% purity by weight. Battery-grade Cu foil is produced at ≥99.97% purity (electrodeposited copper, electrolytic process) → qualifies as "refined copper."

**Step 3 — Chapter 74 Classification**

HTSUS Heading 7410: "Copper foil (whether or not backed): Not exceeding 0.15mm in thickness."
Subheading 7410.11: "Of refined copper."

Battery-grade Cu foil: thickness 6-12μm (well below 0.15mm), purity ≥99.97% (well above 99.85% threshold) → **7410.11**.

**CBP N090878**: CBP classified copper foil of refined copper (electrolytic, thickness ≤0.15mm, not backed) under **7410.11.0000** (US HTSUS). This ruling directly covers battery-grade copper foil characteristics.

## Classification

- **Code**: 7410.11.0000 (US HTSUS, per CBP N090878)
- **Basis**: GRI 1; Section XV Note 2 → Chapter 74; refined copper (≥99.85%) → heading 7410.11; thickness <0.15mm confirmed; CBP N090878 binding
- **Stability**: stable
- **Confidence**: high

## Conditional Note for DRONA

- IF Cu foil purity <99.85% → copper alloy, potentially 7410.21 (of copper alloys) — not battery-grade
- IF Cu foil = bare, thickness ≤0.15mm, purity ≥99.85% → **7410.11.0000** (US)
- Battery-grade Cu anode foil standard: 7410.11.0000

## Graph Links

- `classification_node` → [[product_component-anode-substrate-cu-foil]]
- `classified_as` → [[hs_code-7410-11-us]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
