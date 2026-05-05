---
agent: PTA
component: Cell Supervisor Unit (CSU)
entity_id: ent_170
jurisdiction: EU
fundamental_function: ACTIVE_CONTROL
material_composition: Distributed PCBA with Analog Front End (AFE) ICs, cell-balancing resistor arrays, isolation transceivers, and temperature sensors
is_composite_flagged: false
hs_code_candidate: "8537.10.91"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs.md
source_section: Heading 8537 — boards and panels for electric control; CN 8537.10.91 programmable memory controllers
ruling_flag: "None"
batch: TB-1
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Yes** | FIRED — Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Measurement serves control function; Chapter 90 excluded (same analysis as US jurisdiction) |

## GRI Analysis

**Resolved at GRI 1** per [[explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs]].

Heading [[hs_code-8537-10-global]] — CSU PCBA with AFE switching ICs and balancing switches meets the two-or-more apparatus threshold. Board classifies at 8537.10.

**EU CN subheading: 8537.10.91 vs 8537.10.98**

The CSU executes programmable balancing algorithms stored in firmware on the AFE ICs and microcontrollers. The AFE firmware determines balancing thresholds, switching timing, and fault escalation — all programmable parameters. EU CN 8537.10.91 (programmable memory controllers) captures the CSU as a programmable control board whose operation is defined by stored firmware. This is preferred over the residual 8537.10.98.

**Comparison to BDU (EU)**: The BDU was assigned 8537.10.98 because its primary apparatus are electromechanical contactors — not programmable memory. The CSU's primary apparatus are AFE ICs executing programmable firmware. The distinction is clear: CSU → 8537.10.91; BDU → 8537.10.98.

## Classification

- **Heading**: 8537.10
- **Subheading**: 8537.10.91 — programmable memory controllers
- **Code**: 8537.10.91
- **Basis**: GRI 1; CSU executes programmable balancing firmware; EU CN 8537.10.91 is the specific provision

## Graph Links

- `classification_node` → [[product_component-cell-supervisor-unit-csu]]
- `engineering_anchor` → [[cell-supervisor-unit-(csu)]]
- `parent_component` → [[battery-management-system-(bms)]]
- `classified_as` → [[hs_code-8537-10-91-eu]]
- `source_doc` → [[explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
