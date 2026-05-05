---
agent: PTA
component: Anode Active Material (Graphite)
entity_id: ent_tb3_02
jurisdiction: US
fundamental_function: ELECTROCHEMICAL_ACTIVE
material_composition: "Battery-grade graphite — either (a) natural graphite purified to >99.95% C, spheroidized (2504.10) or (b) synthetic/artificial graphite from petroleum coke, surface-modified (3801.10)"
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
source_section: "GRI Analysis; Chapter 25 Note 1 boundary; CBP N325161"
ruling_anchor: "CBP N325161 (surface-modified spherical graphite → 3801.10, not 2504.10); HTSUS Chapter 25 Note (natural minerals, not processed)"
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

Two legally distinct product streams:

**(A) Natural graphite route (2504.10)**:
HTSUS Chapter 25 covers natural minerals and mineral products. Heading 2504 — "Natural graphite." Subheading 2504.10 — "In powder or flakes." Chapter 25 Note 1: these provisions apply only to products in a crude state or only washed, crushed, ground, powdered, levigated, sifted, screened, concentrated, calcined, or sintered. Purification to >99.95% C by acid leaching = chemical processing → may fall outside Chapter 25 Note 1 boundary.

**CBP N325161 analysis**: CBP ruled that surface-modified spherical graphite (natural graphite that has been spheroidized, purified, and surface-coated with carbon to control reactivity) is NOT classifiable under 2504.10. The surface modification constitutes processing that moves the product beyond the Chapter 25 Note 1 boundary. Classification → 3801.10.

**(B) Artificial/synthetic graphite route (3801.10)**:
HTSUS Heading 3801 — "Artificial graphite; colloidal or semi-colloidal graphite; preparations based on graphite or other carbon in the form of pastes, blocks, plates or other semi-manufactures." Subheading 3801.10 — "Artificial graphite."

Petroleum coke-derived graphite (calcined petroleum coke heat-treated to ≥2500°C in the Acheson process to produce graphitic carbon) = artificial graphite → 3801.10.

**Step 2 — Primary Classification for Battery-Grade Graphite**

Commercial battery-grade anode graphite is invariably either:
- Synthetic graphite (Acheson process) → 3801.10.0000
- Surface-modified spherical natural graphite (spheroidized + purified + carbon-coated) → 3801.10.0000 per CBP N325161

Pure, unmodified natural graphite flakes (if commercially imported as such, rare for battery applications) → 2504.10.1000 (powder/flake).

**Primary code for EV battery anode graphite**: 3801.10.0000 (US HTSUS)

## Classification

- **Code**: 3801.10.0000 (US HTSUS — primary for battery-grade, both synthetic and surface-modified natural)
- **Basis**: GRI 1; artificial graphite heading by material processing state; CBP N325161 binding for surface-modified natural graphite → 3801.10; Acheson process synthetic graphite → 3801.10 by heading description
- **Stability**: stable
- **Confidence**: high

## Conditional Note for DRONA

- IF graphite = pure natural flake, no surface modification → **2504.10.1000** (US)
- IF graphite = synthetic (Acheson process) OR surface-modified spherical (battery-grade) → **3801.10.0000** (US, per CBP N325161)
- Battery-grade anode graphite default: 3801.10.0000

## Graph Links

- `classification_node` → [[product_component-anode-active-material-graphite]]
- `classified_as` → [[hs_code-3801-10-us]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
