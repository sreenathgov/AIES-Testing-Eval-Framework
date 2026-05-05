---
agent: PTA
component: High-Voltage Battery Pack Assembly
entity_id: ent_100
jurisdiction: US
fundamental_function: ENERGY_STORAGE
material_composition: Composite good — aluminum enclosure, Li-ion electrochemical cells, cooling plates, busbars, BMS electronics, thermal management hardware
is_composite_flagged: true
gri_3_required: true
hs_code_candidate: "8507.60.00"
gri_path: GRI_3b
stability: stable
confidence: high
source_doc: usitc_hts_ch85_2026_complex.md
source_section: Heading 8507 — electric storage batteries; subheading 8507.60 (lithium-ion)
ruling_flag: "CBP HQ H155376 (Jun 2011): BMS+cells → 8507.80.80 (now 8507.60). CBP HQ H309485 (Aug 2020): Li-ion Battery Rack System → 8507.60.00. Both rulings confirm essential character = electrochemical cells."
batch: TB-2
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Considered** | HV Battery Pack is not a motor vehicle part — it is a storage battery. No Chapter 87 conflict arises. Note 2(f) is not directly relevant; the question is 8507 vs other Chapter 85 headings. |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Not applicable |

## GRI Cascade

**GRI 1 fails**: The HV Battery Pack Assembly contains electrochemical cells (8507), BMS electronics (8537), thermal management (8419), aluminum enclosure (7610 — but overridden by Section XVI Note), and busbars/cabling (8544). No single heading covers this composite.

**GRI 3(a) fails**: Multiple headings each describe only part of the assembly.

**GRI 3(b) — Essential Character**:

The essential character of the HV Battery Pack Assembly is determined by the Li-ion electrochemical cells. The cells:
- Constitute the majority of the assembly's weight, volume, and value
- Perform the sole energy storage function — all other components (BMS, thermal management, housing) exist to protect, manage, and enable the cells
- Are the article's defining electrochemical identity

**WCO EN 85.07** confirms: "storage batteries which incorporate ancillary monitoring circuits are classified in this heading." The BMS in the HV Battery Pack is an "ancillary monitoring circuit" that monitors and balances cell states — it is ancillary to the cells.

**CBP HQ H155376** (June 2011): BMS + Li-ion cells assembled together → 8507.80.80 (now 8507.60). The BMS does not change the classification of the assembly when presented with cells.

**CBP HQ H309485** (August 2020): Battery Rack System (cells + modules + BMS) → 8507.60.00. Thermal management hardware, protection units, and rack hardware do not change the essential character.

GRI 3(b) resolves: **8507.60** (lithium-ion accumulators/batteries).

## Classification

- **Heading**: 8507.60
- **Code**: 8507.60.00
- **Basis**: GRI 3(b); Li-ion cells give essential character; H155376 + H309485 corroborate

## Graph Links

- `classification_node` → [[product_component-hv-battery-pack-assembly]]
- `engineering_anchor` → [[high-voltage-battery-pack-assembly]]
- `classified_as` → [[hs_code-8507-60-00-us]]
- `ruling_reference` → [[cbp_hq_h155376_bms]]
- `ruling_reference` → [[cbp_hq_h309485_ruling_record]]
- `source_doc` → [[usitc_hts_ch85_2026_complex]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
