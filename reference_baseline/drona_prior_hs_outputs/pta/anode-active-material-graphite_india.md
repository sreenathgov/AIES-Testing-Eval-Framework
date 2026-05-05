---
agent: PTA
component: Anode Active Material (Graphite)
entity_id: ent_tb3_02
jurisdiction: India
fundamental_function: ELECTROCHEMICAL_ACTIVE
material_composition: "Battery-grade graphite — either (a) natural graphite purified/spheroidized or (b) synthetic/artificial graphite from petroleum coke"
is_composite_flagged: false
gri_3_required: false
hs_code_candidate: "3801.10"
hs_code_candidate_alt: "2504.10"
gri_path: GRI_1
stability: stable
confidence: high
validation_status: validated
corpus_gap: false
batch: TB-3
refinement_run: "2026-04-06"
source_doc: "HS - DR - GapFilling - Battery Material Tariff Classification Research.md"
source_section: "GRI Analysis; Chapter 25 Note 1 boundary; artificial graphite residual"
ruling_anchor: "ITC-HS Chapter 25 Note 1 (same WCO text boundary); ITC-HS 3801.10.00 for artificial graphite"
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XV Note 2 (parts of general use) | No | Chemical/mineral, not mechanical part |
| Section XVII Note 2(f) | No | Not electrical machinery |
| Chapter 90 Note 2 | No | Not a measuring instrument |

`exclusion_checks_run: ["Section XV Note 2", "Section XVII Note 2(f)", "Chapter 90 Note 2"]`

## GRI Analysis

**Step 1 — Natural vs. Synthetic Determination**

India ITC-HS Chapter 25, Note 1 is identical to WCO text: heading 2504 covers natural graphite only in a crude state or products that are merely washed, crushed, ground, powdered, levigated, sifted, screened, concentrated, calcined, or sintered. Battery-grade graphite that has been spheroidized, acid-purified to >99.95% C, and surface-carbon-coated exceeds this boundary.

India applies material-first classification. Surface processing that imparts specific functional properties routes chemical materials to Chapter 38.

**Step 2 — Chapter 38 Artificial Graphite**

ITC-HS Heading 3801 — "Artificial graphite; colloidal or semi-colloidal graphite; preparations based on graphite or other carbon..." Subheading 3801.10.00 — "Artificial graphite."

Synthetic graphite (Acheson process) → 3801.10.00 by definition.
Surface-modified spherical natural graphite → 3801.10.00 (processing exceeds Chapter 25 Note 1 boundary; functional treatment renders it equivalent to artificial graphite for classification purposes).

India does not have a battery-specific subheading equivalent to EU CN 2026's 3801.10.10. ITC-HS 2024 retains 3801.10.00 as a single subheading for all artificial graphite.

## Classification

- **Code**: 3801.10.00 (ITC-HS)
- **Basis**: GRI 1; artificial graphite heading; Chapter 25 Note 1 boundary excludes processed/surface-modified grades; ITC-HS 3801.10.00 for all artificial graphite
- **Stability**: stable
- **Confidence**: high

## Conditional Note for DRONA

- IF graphite = pure natural flake, no surface modification → **2504.10.00** (India ITC-HS)
- IF graphite = synthetic (Acheson) OR surface-modified spherical (battery-grade) → **3801.10.00** (India)
- Battery-grade anode graphite default (India): 3801.10.00

## Graph Links

- `classification_node` → [[product_component-anode-active-material-graphite]]
- `classified_as` → [[hs_code-3801-10-in]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
