---
agent: PTA
component: Silicon IGBTs
entity_id: ent_210
jurisdiction: US
fundamental_function: ACTIVE_CONTROL
material_composition: Silicon semiconductor with MOSFET gate structure and bipolar transistor output stage (Insulated Gate Bipolar Transistor)
is_composite_flagged: false
hs_code_candidate: "8541.29.00"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: usitc_hts_ch85_2026_complex.md
source_section: Heading 8541 — semiconductor devices; subheading 8541.29 (transistors, dissipation ≥ 1W)
ruling_flag: "None"
batch: TB-1
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Yes** | FIRED — semiconductor devices are Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Switching device; not a measuring instrument |

## GRI Analysis

**Resolved at GRI 1** per [[usitc_hts_ch85_2026_complex]].

Heading 8541 — the IGBT (Insulated Gate Bipolar Transistor) is a transistor-class semiconductor device. The IGBT combines a MOSFET gate with a bipolar output stage to achieve high current capacity with low gate drive requirements. It is explicitly a transistor within heading 8541. GRI 1 is determinative.

**Subheading: 8541.21 vs 8541.29**

Silicon IGBTs for EV traction inverters are power devices with dissipation capacity in the range of tens to hundreds of watts. Dissipation capacity is clearly ≥ 1W. **8541.29** applies.

**Comparison to SiC MOSFETs**: Both SiC MOSFETs and Silicon IGBTs are power transistors classified under 8541.29. The substrate material (SiC vs Si) does not create a tariff classification distinction under US HTS — both are transistors with dissipation ≥ 1W. Code is identical: **8541.29.00**.

## Classification

- **Heading**: 8541
- **Subheading**: 8541.29 — transistors, other (dissipation ≥ 1W)
- **Code**: 8541.29.00
- **Basis**: GRI 1; IGBT is a power transistor with dissipation ≥ 1W; same US code as SiC MOSFETs

## Graph Links

- `classification_node` → [[product_component-silicon-igbts]]
- `engineering_anchor` → [[silicon-igbts]]
- `parent_component` → [[traction-inverter-module]]
- `classified_as` → [[hs_code-8541-29-us]]
- `source_doc` → [[usitc_hts_ch85_2026_complex]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
