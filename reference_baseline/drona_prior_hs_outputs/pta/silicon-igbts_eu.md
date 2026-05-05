---
agent: PTA
component: Silicon IGBTs
entity_id: ent_210
jurisdiction: EU
fundamental_function: ACTIVE_CONTROL
material_composition: Silicon semiconductor — Insulated Gate Bipolar Transistor
is_composite_flagged: false
hs_code_candidate: "8541.29.00"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs.md
source_section: Heading 8541 — semiconductor devices; EU CN 8541.29.00 (transistors, other than photosensitive, dissipation ≥ 1W)
ruling_flag: "None"
batch: TB-1
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Yes** | FIRED — Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Switching device; not a measuring instrument |

## GRI Analysis

**Resolved at GRI 1** per [[explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs]].

Heading 8541 — IGBT is a transistor-class semiconductor device. EU CN classifies at 8541.29.00 for power transistors with dissipation ≥ 1W. EU CN 2025 (Reg. 2025/1926) does not create specific subheadings for IGBT vs MOSFET within 8541.29; both remain at 8541.29.00.

**Comparison to SiC MOSFETs**: Identical EU code. Substrate and transistor architecture do not create CN subheading distinctions at 8541.29.

## Classification

- **Heading**: 8541
- **Subheading**: 8541.29 — transistors other (dissipation ≥ 1W)
- **Code**: 8541.29.00
- **Basis**: GRI 1; identical to SiC MOSFET EU classification

## Graph Links

- `classification_node` → [[product_component-silicon-igbts]]
- `engineering_anchor` → [[silicon-igbts]]
- `parent_component` → [[traction-inverter-module]]
- `classified_as` → [[hs_code-8541-29-eu]]
- `source_doc` → [[explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
