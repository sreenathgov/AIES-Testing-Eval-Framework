---
agent: PTA
component: Cathode Active Material (NMC)
entity_id: ent_tb3_01
jurisdiction: India
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
source_section: "GRI Analysis; Chapter 28 Note 1 boundary; processed inorganic preparation residual"
ruling_anchor: "ITC-HS Chapter 28 Note 1 (WCO identical text); India material-first classification principle"
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

India ITC-HS Chapter 28, Note 1 is identical to WCO text: applies only to "separate chemically defined compounds" and products with preservation stabilisers only, provided additions do not "render the product particularly suitable for specific use rather than for general use."

EV-grade NMC with Zr/Ti/Al dopants and boron/tungsten surface coatings: dopants are electrochemical performance modifiers making the material particularly suitable for lithium-ion battery cathode service → Chapter 28 Note 1 boundary violated → ejected from Chapter 28.

India applies the material-first classification principle for chemicals. Given ejection from Chapter 28, the residual Chapter 38 heading applies.

**Note on pure NMC in India**: India ITC-HS 2024 does not have a specific subheading equivalent to EU CN 2026's 2841.90.40 for pure NMC. India retains general 2841.90.90 for other oxometallates/peroxometallates. Pure, undoped NMC would classify under 2841.90.90.

**Step 2 — Chapter 38 Residual Heading**

GRI 1: ITC-HS Heading 3824 — "Prepared binders for foundry moulds or cores; chemical products and preparations of the chemical or allied industries (including those consisting of mixtures of natural products), not elsewhere specified or included." Subheading 3824.99.00 — "Other" — captures inorganic chemical preparations not elsewhere specified.

## Classification

- **Code**: 3824.99.00 (ITC-HS)
- **Basis**: GRI 1; doped/coated NMC = inorganic chemical preparation not elsewhere specified; ejected from Ch 28 per Note 1 boundary; ITC-HS 3824.99.00 is the residual chemical preparation subheading
- **Stability**: stable
- **Confidence**: high

## Conditional Note for DRONA

- IF NMC = pure stoichiometric, undoped, uncoated → **2841.90.90** (India ITC-HS — general oxometallates)
- IF NMC = doped OR surface-coated (EV-grade standard) → **3824.99.00** (India)
- EV-grade NMC default: 3824.99.00

## Graph Links

- `classification_node` → [[product_component-cathode-active-material-nmc]]
- `classified_as` → [[hs_code-3824-99-in]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
