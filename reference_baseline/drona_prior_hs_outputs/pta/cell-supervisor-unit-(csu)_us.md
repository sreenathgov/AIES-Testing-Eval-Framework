---
agent: PTA
component: Cell Supervisor Unit (CSU)
entity_id: ent_170
jurisdiction: US
fundamental_function: ACTIVE_CONTROL
material_composition: Distributed PCBA with Analog Front End (AFE) ICs, cell-balancing resistor arrays, isolation transceivers, and temperature sensors
is_composite_flagged: false
hs_code_candidate: "8537.10.91"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: usitc_hts_ch85_2026_complex.md
source_section: Heading 8537 — boards and panels for electric control ≤1,000V; subheading 8537.10.91 (dedicated control boards)
ruling_flag: "None"
batch: TB-1
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Yes** | FIRED — electrical measurement/control apparatus is Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | PCBA is not a part of general use |
| Chapter 90 Note 2 | No | CRITICAL — Chapter 90 Note 2 requires measuring instruments (thermometers, voltmeters, etc.) to be excluded from Chapter 85. The CSU measures cell voltages and temperatures but does so exclusively to execute cell-balancing and fault-protection control algorithms. The measurement function is subordinate to and instrumental in the ACTIVE_CONTROL function. Chapter 90 Note 2 does not apply; Chapter 85 governs. Same analysis as BMS (pilot batch). |

## GRI Analysis

**Resolved at GRI 1** per [[usitc_hts_ch85_2026_complex]].

Heading [[hs_code-8537-10-global]] covers boards equipped with two or more apparatus of headings 8535/8536 for electric control. The CSU PCBA carries:
- **AFE ICs** — analog front-end semiconductors that integrate cell voltage measurement, overcurrent protection switching, and balancing drive circuits. These are mixed-signal control ICs performing switching functions (8536 class);
- **Cell-balancing resistor switches** — switching elements (8536 class) that route current through balancing paths under AFE command.

Two-or-more-apparatus threshold: met. AFE switching circuits + balancing switches = two classes of 8536-equivalent apparatus.

**Chapter 90 Note 2 deeper analysis**: The CSU acquires cell voltage readings (millivolt resolution) and temperature data as inputs. However, the CSU's output is a control signal to the BCU and balancing resistors — not a measurement readout to a user. The WCO Explanatory Notes distinguish measuring instruments (EN 90.XX) from control apparatus that incorporate measuring functionality as ancillary input. The CSU is the latter. Note 2 to Chapter 90 does not route it to Chapter 90.

**Competing heading 8543** (other electrical apparatus): Not applicable; 8537 specifically covers this configuration.

## Classification

- **Heading**: 8537.10
- **Subheading**: 8537.10.91 — dedicated control boards for a voltage not exceeding 1,000V
- **Code**: 8537.10.91
- **Basis**: GRI 1; CSU is a dedicated control board with ≥2 apparatus of 8536; measurement function serves control

## Graph Links

- `classification_node` → [[product_component-cell-supervisor-unit-csu]]
- `engineering_anchor` → [[cell-supervisor-unit-(csu)]]
- `parent_component` → [[battery-management-system-(bms)]]
- `classified_as` → [[hs_code-8537-10-91-us]]
- `source_doc` → [[usitc_hts_ch85_2026_complex]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
