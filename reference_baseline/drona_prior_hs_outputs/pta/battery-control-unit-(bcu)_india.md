---
agent: PTA
component: Battery Control Unit (BCU)
entity_id: ent_169
jurisdiction: India
fundamental_function: ACTIVE_CONTROL
material_composition: Centralized multilayer PCBA with microcontrollers, cell-balancing circuits, protection ICs, and communication interfaces housed in plastic or die-cast aluminum enclosure
is_composite_flagged: false
hs_code_candidate: "8537.10.00"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: cbic_indian_trade_classification_complex.md
source_section: Heading 8537 — boards and panels for electric control; subheading 8537.10 (for voltage ≤ 1,000V); India single 8-digit entry 8537.10.00
ruling_flag: "None"
batch: TB-1
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Yes** | FIRED — electrical control apparatus is Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | PCBA is not a part of general use |
| Chapter 90 Note 2 | No | ACTIVE_CONTROL function; measurement serves control |
| Chapter 84 Note 5(E) | **Yes** | Dedicated controller; heading 8471 excluded |

## GRI Analysis

**Resolved at GRI 1** per [[cbic_indian_trade_classification_complex]].

Heading [[hs_code-8537-10-global]] covers boards and panels equipped with apparatus of headings 8535/8536 for electric control. BCU is a PCBA with protection and balancing switching devices meeting the two-or-more threshold. GRI 1 is determinative.

India's ITC-HS maintains a single 8-digit entry under 8537.10: **8537.10.00** — "For a voltage not exceeding 1,000V." India does not subdivide further at the 8-digit level for this heading. The BCU operates at battery pack voltage (nominally 300–800V), within the ≤1,000V specification.

**Competing heading 8507**: Not applicable for standalone BCU PCBA (same analysis as US and EU).

## Classification

- **Heading**: 8537.10
- **Subheading**: 8537.10.00 — for a voltage not exceeding 1,000V
- **Code**: 8537.10.00
- **Basis**: GRI 1; India single 8-digit entry; BCU meets 8537.10 threshold

## Graph Links

- `classification_node` → [[product_component-battery-control-unit-bcu]]
- `engineering_anchor` → [[battery-control-unit-(bcu)]]
- `parent_component` → [[battery-management-system-(bms)]]
- `classified_as` → [[hs_code-8537-10-00-in]]
- `source_doc` → [[cbic_indian_trade_classification_complex]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
