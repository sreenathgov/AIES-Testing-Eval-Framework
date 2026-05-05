---
agent: PTA
component: Battery Control Unit (BCU)
entity_id: ent_169
jurisdiction: EU
fundamental_function: ACTIVE_CONTROL
material_composition: Centralized multilayer PCBA with microcontrollers, cell-balancing circuits, protection ICs, and communication interfaces housed in plastic or die-cast aluminum enclosure
is_composite_flagged: false
hs_code_candidate: "8537.10.91"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs.md
source_section: Heading 8537 — boards and panels for electric control; CN 8537.10.91 programmable memory controllers
ruling_flag: "None — no contested EU BTI or CJEU ruling on standalone BCU PCBA"
batch: TB-1
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Yes** | FIRED — electrical control apparatus is Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | PCBA is not a part of general use |
| Chapter 90 Note 2 | No | ACTIVE_CONTROL — measurement serves control; Chapter 90 not applicable |
| Chapter 84 Note 5(E) | **Yes** | Dedicated controller — not a general-purpose ADP machine; heading 8471 excluded |

## GRI Analysis

**Resolved at GRI 1** per [[explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs]].

Heading [[hs_code-8537-10-global]] covers boards, panels, and bases equipped with two or more apparatus of headings 8535/8536 for electric control. The BCU PCBA carries protection devices (8536) and cell-balancing switching circuits (8536) — two-or-more threshold met. The BCU is thus a board/panel for electric control at heading 8537.10.

**EU CN subheading: 8537.10.91 vs 8537.10.98**

EU CN 8537.10.91 covers "programmable memory controllers." A BCU stores and executes programmable battery management firmware on its microcontrollers — it is a controller that uses programmable memory to execute state-specific control logic. EU CN 8537.10.91 is the more specific provision; 8537.10.98 (Other) is residual.

**Note**: If EU customs authorities consider the BCU primarily as a "dedicated protection board" rather than a "programmable memory controller," the residual 8537.10.98 would apply. Heading-level classification is unchanged.

**Competing heading 8507**: Not applicable for standalone BCU PCBA without battery cells (same analysis as US jurisdiction).

## Classification

- **Heading**: 8537.10
- **Subheading**: 8537.10.91 — programmable memory controllers
- **Code**: 8537.10.91
- **Basis**: GRI 1; BCU is a programmable control board with firmware-executable battery management logic

## Graph Links

- `classification_node` → [[product_component-battery-control-unit-bcu]]
- `engineering_anchor` → [[battery-control-unit-(bcu)]]
- `parent_component` → [[battery-management-system-(bms)]]
- `classified_as` → [[hs_code-8537-10-91-eu]]
- `source_doc` → [[explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
