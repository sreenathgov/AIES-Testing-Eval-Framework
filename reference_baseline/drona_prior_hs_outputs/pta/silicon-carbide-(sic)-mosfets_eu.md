---
agent: PTA
component: Silicon Carbide (SiC) MOSFETs
entity_id: ent_209
jurisdiction: EU
fundamental_function: ACTIVE_CONTROL
material_composition: Silicon Carbide (SiC) semiconductor substrate; power transistor device
is_composite_flagged: false
hs_code_candidate: "8541.29.00"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs.md
source_section: Heading 8541 — semiconductor devices; subheading 8541.29 (transistors, other than photosensitive, dissipation ≥ 1W)
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

**Resolved at GRI 1** per [[explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs]].

Heading 8541 — SiC MOSFET is unambiguously a transistor-class semiconductor device. GRI 1 is determinative.

**Subheading: EU CN 8541.29.00**

EU CN aligns with the WCO nomenclature on the 8541.21 / 8541.29 distinction (dissipation capacity < 1W vs ≥ 1W). SiC power transistors for EV traction inverters have dissipation capacity well above 1W. EU CN 8541.29.00 is the applicable code.

The EU CN does not create specific subheadings for wide-bandgap semiconductors (SiC, GaN) as of the EU 2025/1926 Regulation; SiC MOSFETs remain at 8541.29.00 in EU CN 2025.

## Classification

- **Heading**: 8541
- **Subheading**: 8541.29 — other transistors (dissipation ≥ 1W)
- **Code**: 8541.29.00
- **Basis**: GRI 1; SiC MOSFET is a power transistor with dissipation ≥ 1W; EU CN 8541.29.00

## Graph Links

- `classification_node` → [[product_component-silicon-carbide-sic-mosfets]]
- `engineering_anchor` → [[silicon-carbide-(sic)-mosfets]]
- `parent_component` → [[traction-inverter-module]]
- `classified_as` → [[hs_code-8541-29-eu]]
- `source_doc` → [[explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
