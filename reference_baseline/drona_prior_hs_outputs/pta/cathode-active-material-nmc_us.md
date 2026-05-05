---
agent: PTA
component: Cathode Active Material (NMC)
entity_id: ent_tb3_01
jurisdiction: US
fundamental_function: ELECTROCHEMICAL_ACTIVE
material_composition: "Lithium nickel manganese cobalt oxide (LiNixMnyCozO2); EV-grade = doped with Zr/Ti/Al + surface-coated with boron or tungsten"
is_composite_flagged: false
gri_3_required: false
hs_code_candidate: "3824.99"
gri_path: GRI_1
stability: stable
confidence: high
validation_status: validated
corpus_gap: false
batch: TB-3
refinement_run: "2026-04-06"
source_doc: "HS - DR - GapFilling - DRONA Battery Chemistry Tariff Refinement.md"
source_section: "GRI Analysis; Chapter 28 Note 1 boundary; CBP N323297"
ruling_anchor: "CBP N323297 (Lithium NCM, doped with Zr, coated with boron/tungsten → 3824.99.39)"
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XV Note 2 (parts of general use) | No | Chemical compound, not mechanical part |
| Section XVII Note 2(f) | No | Not electrical machinery |
| Chapter 90 Note 2 | No | Not a measuring instrument |

`exclusion_checks_run: ["Section XV Note 2", "Section XVII Note 2(f)", "Chapter 90 Note 2"]`

## GRI Analysis

**Step 1 — Chemical Processing State Determination**

EV-grade NMC cathode active material is NOT pure stoichiometric LiNiMnCoO₂. Commercial battery-grade NMC is uniformly engineered with:
- **Transition metal dopants** (zirconium, titanium, or aluminum) to suppress capacity fading and oxygen evolution during high-voltage cycling
- **Surface coatings** (boron, tungsten) to prevent transition metal dissolution

Chapter 28, Note 1 (binding USITC text): Chapter 28 applies only to "separate chemically defined compounds, whether or not containing impurities" plus products with "an added stabiliser necessary for their preservation or transport" provided the additions do not "render the product particularly suitable for specific use rather than for general use."

Zirconium dopants and boron coatings are **not** preservation stabilizers — they are deliberate electrochemical performance enhancers that make the material **particularly suitable for** lithium-ion battery cathode use. This violates the Chapter 28 Note 1 boundary.

Consequence: EV-grade doped/coated NMC is **ejected from Chapter 28**.

**Step 2 — Chapter 38 Residual Heading**

GRI 1: Heading 3824 — "Prepared binders for foundry moulds or cores; chemical products and preparations of the chemical or allied industries... not elsewhere specified or included." Subheading 3824.99 — "Other: Other" — captures mixtures of two or more inorganic compounds engineered for specific use.

**CBP N323297 (binding precedent)**: Lithium NCM doped with zirconium and coated with boron/tungsten → **3824.99.3900** (HTSUS — Mixtures of two or more inorganic compounds: Other).

**Note on pure NMC**: If pure, undoped NMC (without dopants or coatings beyond the base LiNiMnCoO₂ stoichiometry) is imported, it classifies under 2841.90 (salts of oxometallic acids). The EU CN 2026 (Regulation 2025/1926) created a specific code 2841.90.40 for this. However, pure NMC is not commercially imported for EV battery manufacturing.

## Classification

- **Code**: 3824.99 (US: 3824.99.3900)
- **Basis**: GRI 1; doped/coated NMC = inorganic chemical preparation not elsewhere specified; ejected from Ch 28 per Note 1 boundary; CBP N323297 binding
- **Stability**: stable (conditional on dopant/coating confirmation — EV-grade always qualifies)
- **Confidence**: high

## Conditional Note for DRONA

- IF NMC = pure stoichiometric, undoped, uncoated → 2841.90 (US)
- IF NMC = doped OR surface-coated (EV-grade standard) → 3824.99.3900 (US)
- EV-grade NMC default: 3824.99.3900

## Graph Links

- `classification_node` → [[product_component-cathode-active-material-nmc]]
- `classified_as` → [[hs_code-3824-99-us]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
