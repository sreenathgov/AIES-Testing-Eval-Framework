---
agent: PTA
component: NdFeB Permanent Magnets
entity_id: ent_207
jurisdiction: India
fundamental_function: ENERGY_CONVERSION
material_composition: Neodymium-Iron-Boron alloy with Dysprosium and Terbium diffusion; sintered rare-earth permanent magnet
is_composite_flagged: false
hs_code_candidate: "8505.11.90"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: cbic_indian_trade_classification_complex.md
source_section: Heading 8505 — permanent magnets; India ITC-HS 8505.11 (of metal); 8505.11.10 (ferrite magnets) vs 8505.11.90 (other)
ruling_flag: "None"
batch: TB-1
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | No | Passive metallic articles; 8505 is Chapter 85; no Chapter 87 conflict |
| Section XV Note 2 | No | Not applicable |
| Note 1 to Chapter 73 | No | Section XVI exclusion applies |
| Chapter 90 Note 2 | No | Not a measuring instrument |

## GRI Analysis

**Resolved at GRI 1** per [[cbic_indian_trade_classification_complex]].

India ITC-HS under 8505.11 also distinguishes ferrite magnets (8505.11.10) from other permanent magnets of metal (8505.11.90). NdFeB is a metallic rare-earth alloy — **not ferrite**. India code: **8505.11.90**.

India's ITC-HS and EU CN share the same subheading structure for 8505.11 in this instance (both distinguish ferrite vs other), confirming that NdFeB → 8505.11.90 across both jurisdictions.

**Import context (India)**: NdFeB magnets used in EV traction motors are predominantly imported from China or Japan. India currently levies basic customs duty on 8505.11.90 magnets. The classification is well-settled in Indian trade practice.

## Classification

- **Heading**: 8505
- **Subheading**: 8505.11.90 — other permanent magnets of metal (not ferrite)
- **Code**: 8505.11.90
- **Basis**: GRI 1; NdFeB is metallic rare-earth alloy, not ferrite; India ITC-HS 8505.11.90

## Graph Links

- `classification_node` → [[product_component-ndfeb-permanent-magnets]]
- `engineering_anchor` → [[ndfeb-permanent-magnets]]
- `parent_component` → [[rotor-assembly]]
- `classified_as` → [[hs_code-8505-11-in]]
- `source_doc` → [[cbic_indian_trade_classification_complex]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
