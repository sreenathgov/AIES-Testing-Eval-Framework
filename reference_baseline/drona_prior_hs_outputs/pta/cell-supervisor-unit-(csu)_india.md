---
agent: PTA
component: Cell Supervisor Unit (CSU)
entity_id: ent_170
jurisdiction: India
fundamental_function: ACTIVE_CONTROL
material_composition: Distributed PCBA with Analog Front End (AFE) ICs, cell-balancing resistor arrays, isolation transceivers, and temperature sensors
is_composite_flagged: false
hs_code_candidate: "8537.10.00"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: cbic_indian_trade_classification_complex.md
source_section: Heading 8537 — boards and panels for electric control; India single 8-digit entry 8537.10.00
ruling_flag: "None"
batch: TB-1
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Yes** | FIRED — Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Measurement serves control; Chapter 90 excluded |

## GRI Analysis

**Resolved at GRI 1** per [[cbic_indian_trade_classification_complex]].

Heading [[hs_code-8537-10-global]] — CSU PCBA with AFE switches and balancing elements meets two-or-more threshold. India classifies at 8537.10.00 (single 8-digit entry, voltage ≤1,000V). CSU cell voltage is within battery pack range (≤1,000V nominal).

## Classification

- **Heading**: 8537.10
- **Subheading**: 8537.10.00 — for a voltage not exceeding 1,000V
- **Code**: 8537.10.00
- **Basis**: GRI 1; India single 8-digit entry

## Graph Links

- `classification_node` → [[product_component-cell-supervisor-unit-csu]]
- `engineering_anchor` → [[cell-supervisor-unit-(csu)]]
- `parent_component` → [[battery-management-system-(bms)]]
- `classified_as` → [[hs_code-8537-10-00-in]]
- `source_doc` → [[cbic_indian_trade_classification_complex]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
