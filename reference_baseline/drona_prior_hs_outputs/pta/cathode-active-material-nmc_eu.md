---
agent: PTA
component: Cathode Active Material (NMC)
entity_id: ent_tb3_01
jurisdiction: EU
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
source_section: "GRI Analysis; EU CN 2026 NMC split; pure versus EV-grade processed material"
ruling_anchor: "EU CN Chapter 28 Note 1; EU CN 2026 Reg 2025/1926 (2841.90.40 for pure NMC — confirms a contrario that doped NMC is not Ch 28)"
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

EU CN Chapter 28, Note 1 mirrors WCO text: applies only to "separate chemically defined compounds, whether or not containing impurities" and products with preservation stabilisers only, provided additions do not "render the product particularly suitable for specific use rather than for general use."

EV-grade NMC with Zr/Ti/Al dopants and boron/tungsten surface coatings fails this test. Dopants are electrochemical performance modifiers making the material particularly suitable for lithium-ion battery cathode service → Chapter 28 Note 1 boundary violated → EV-grade NMC ejected from Chapter 28.

**EU CN 2026 Note (Regulation 2025/1926)**: EU CN 2026 introduced specific subheading **2841.90.40** for lithium-nickel-manganese-cobalt oxide (LiNiMnCoO₂) in pure stoichiometric form. This confirms the EU interpretation: pure, undoped NMC classifies under 2841.90.40 as an inorganic salt. The introduction of a specific code for pure NMC confirms a contrario that doped/coated NMC is not 2841.90 — it is excluded by Chapter 28 Note 1 and routes to Chapter 38.

**Step 2 — Chapter 38 Residual Heading**

GRI 1: Heading 3824 — "Chemical products and preparations of the chemical or allied industries... not elsewhere specified or included." EU CN 3824.99 — "Other: Other" — captures engineered inorganic preparations specifically prepared for battery cathode use.

## Classification

- **Code**: 3824.99 (EU CN; 8-digit subheading to be confirmed against current EU Tariff Regulation — 3824.99.92 or 3824.99.96 candidate)
- **Basis**: GRI 1; doped/coated NMC = inorganic chemical preparation not elsewhere specified; ejected from Ch 28 per Note 1; EU CN 2026 Reg 2025/1926 2841.90.40 for pure NMC confirms a contrario that doped NMC is not Ch 28
- **Stability**: stable
- **Confidence**: high

## Conditional Note for DRONA

- IF NMC = pure stoichiometric, undoped, uncoated → **2841.90.40** (EU CN 2026, Reg 2025/1926)
- IF NMC = doped OR surface-coated (EV-grade standard) → **3824.99** (EU)
- EV-grade NMC default: 3824.99

## Graph Links

- `classification_node` → [[product_component-cathode-active-material-nmc]]
- `classified_as` → [[hs_code-3824-99-eu]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
