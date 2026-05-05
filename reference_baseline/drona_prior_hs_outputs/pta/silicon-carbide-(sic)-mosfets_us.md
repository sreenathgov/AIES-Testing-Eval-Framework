---
agent: PTA
component: Silicon Carbide (SiC) MOSFETs
entity_id: ent_209
jurisdiction: US
fundamental_function: ACTIVE_CONTROL
material_composition: Silicon Carbide (SiC) semiconductor substrate with gate oxide, source/drain metallization; power transistor device
is_composite_flagged: false
hs_code_candidate: "8541.29.00"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: usitc_hts_ch85_2026_complex.md
source_section: Heading 8541 — semiconductor devices; subheading 8541.21 (transistors dissipation < 1W) vs 8541.29 (Other — dissipation ≥ 1W)
ruling_flag: "None"
batch: TB-1
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Yes** | FIRED — semiconductor devices are Chapter 85 apparatus; Chapter 87 vetoed even though SiC MOSFETs are components of the traction inverter in the EV drivetrain |
| Section XV Note 2 | No | Semiconductor devices are not parts of general use |
| Chapter 90 Note 2 | No | ACTIVE_CONTROL (switching function); semiconductor device is not a measuring instrument |

## GRI Analysis

**Resolved at GRI 1** per [[usitc_hts_ch85_2026_complex]].

Heading 8541 covers "Diodes, transistors and similar semiconductor devices; photosensitive semiconductor devices; light-emitting diodes (LED); mounted piezoelectric crystals." A SiC MOSFET is a transistor-class semiconductor device — this is unambiguous. GRI 1 is determinative.

**Subheading determination — 8541.21 vs 8541.29**

The critical distinction within heading 8541 is dissipation capacity:
- **8541.21**: transistors with a dissipation capacity of less than 1W
- **8541.29**: Other transistors (dissipation capacity ≥ 1W)

SiC MOSFETs used in EV traction inverters are **power transistors** designed to handle switching currents of 100–600A at bus voltages of 400–800V. Their dissipation capacity is measured in watts to kilowatts under normal switching loss conditions. A single SiC MOSFET switch event at EV power levels involves millisecond-scale switching losses far exceeding 1W steady-state dissipation. Classification at **8541.29** is unambiguous.

**Competing heading 8543** (other electrical apparatus): Not applicable. Heading 8541 specifically names transistors and semiconductor devices. GRI 1 resolves.

**US statistical suffix**: Under US HTS 2026 Chapter 85, 8541.29 is the final statistical breakdown for this category (no further subdivision). The 8-digit code is **8541.29.00**.

## Classification

- **Heading**: 8541
- **Subheading**: 8541.29 — transistors, other than photosensitive transistors, other (dissipation capacity ≥ 1W)
- **Code**: 8541.29.00
- **Basis**: GRI 1; SiC MOSFET is a power transistor with dissipation capacity ≥ 1W

## Graph Links

- `classification_node` → [[product_component-silicon-carbide-sic-mosfets]]
- `engineering_anchor` → [[silicon-carbide-(sic)-mosfets]]
- `parent_component` → [[traction-inverter-module]]
- `classified_as` → [[hs_code-8541-29-us]]
- `source_doc` → [[usitc_hts_ch85_2026_complex]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
