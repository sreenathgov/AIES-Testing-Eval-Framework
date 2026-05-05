---
agent: PTA
component: Silicon IGBTs
entity_id: ent_210
jurisdiction: India
fundamental_function: ACTIVE_CONTROL
material_composition: Silicon semiconductor — Insulated Gate Bipolar Transistor
is_composite_flagged: false
hs_code_candidate: "8541.29.90"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: cbic_indian_trade_classification_complex.md
source_section: Heading 8541 — semiconductor devices; India ITC-HS 8541.29.90 (Other transistors, not ADP/telecom type)
ruling_flag: "None"
batch: TB-1
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Yes** | FIRED — Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Switching device |

## GRI Analysis

**Resolved at GRI 1** per [[cbic_indian_trade_classification_complex]].

Heading 8541 — IGBT is a transistor. India ITC-HS: 8541.29.10 (ADP/telecom-type transistors) vs 8541.29.90 (Other). Silicon IGBTs for EV traction inverters are power transistors — not of the kind used in ADP or telecommunications apparatus. India code: **8541.29.90**.

**Comparison to SiC MOSFETs**: Identical India code. Power transistor function (EV switching) routes both to 8541.29.90.

## Classification

- **Code**: 8541.29.90
- **Basis**: GRI 1; India 8541.29.90 (Other power transistors); identical to SiC MOSFET India classification

## Graph Links

- `classification_node` → [[product_component-silicon-igbts]]
- `engineering_anchor` → [[silicon-igbts]]
- `parent_component` → [[traction-inverter-module]]
- `classified_as` → [[hs_code-8541-29-in]]
- `source_doc` → [[cbic_indian_trade_classification_complex]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
