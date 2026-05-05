---
agent: PTA
component: High-Voltage Battery Module
entity_id: ent_133
jurisdiction: US
fundamental_function: ENERGY_STORAGE
material_composition: Li-ion cells, structural frames, Cell Contacting System (CCS), Cell Module Controller (CMC)
is_composite_flagged: true
gri_3_required: true
hs_code_candidate: "8507.60.00"
gri_path: GRI_3b
stability: stable
confidence: high
source_doc: usitc_hts_ch85_2026_complex.md
source_section: Heading 8507.60 — lithium-ion accumulators
ruling_flag: "CBP HQ H309485: Battery Module within Battery Rack System → 8507.60.00. Module-level Li-ion assemblies maintain 8507.60 classification."
batch: TB-2
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | No | Not applicable — storage battery sub-assembly |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | CMC is ancillary measurement/control; same ancillary circuit analysis as BMS in Pack |

## GRI Cascade

**GRI 3(b)**: Li-ion cells give essential character → 8507.60.00. The HV Battery Module is a sub-assembly of the Battery Pack; it contains cells, CCS (busbars/contactors), and CMC (monitoring PCBA). Essential character = Li-ion cells. H309485 confirms module-level classification at 8507.60.00.

## Classification

- **Code**: 8507.60.00
- **Basis**: GRI 3(b); Li-ion cells essential character; H309485 module-level confirmation

## Graph Links

- `classification_node` → [[product_component-hv-battery-module]]
- `engineering_anchor` → [[high-voltage-battery-module]]
- `parent_component` → [[product_component-hv-battery-pack-assembly]]
- `classified_as` → [[hs_code-8507-60-00-us]]
- `ruling_reference` → [[cbp_hq_h309485_ruling_record]]
- `source_doc` → [[usitc_hts_ch85_2026_complex]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
