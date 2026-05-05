---
agent: PTA
component: NdFeB Permanent Magnets
entity_id: ent_207
jurisdiction: EU
fundamental_function: ENERGY_CONVERSION
material_composition: Neodymium-Iron-Boron alloy with Dysprosium and Terbium diffusion; sintered rare-earth permanent magnet
is_composite_flagged: false
hs_code_candidate: "8505.11.90"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs.md
source_section: Heading 8505 — permanent magnets; EU CN 8505.11 (of metal); 8505.11.10 (ferrite) vs 8505.11.90 (other)
ruling_flag: "None"
batch: TB-1
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | No | Permanent magnets are passive metallic articles; 8505 is already in Chapter 85; no Chapter 87 conflict |
| Section XV Note 2 | No | Not applicable |
| Note 1 to Chapter 73 | No | Section XVI exclusion applies; 8505.11 captures metallic permanent magnets |
| Chapter 90 Note 2 | No | Not a measuring instrument |

## GRI Analysis

**Resolved at GRI 1** per [[explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs]].

Heading 8505.11 — permanent magnets of metal. GRI 1 determinative (same analysis as US).

**EU CN subheading: 8505.11.10 vs 8505.11.90**

EU CN subdivides 8505.11:
- **8505.11.10**: Ferrite permanent magnets (ceramic iron oxide magnets — e.g., barium ferrite, strontium ferrite)
- **8505.11.90**: Other permanent magnets of metal

NdFeB permanent magnets are **rare-earth metallic alloy** magnets (Nd₂Fe₁₄B matrix), NOT ferrite magnets. Ferrite magnets are ceramic iron oxide compounds. The distinction is material-based and unambiguous:
- Ferrite = ceramic oxide → 8505.11.10
- NdFeB (metallic rare-earth alloy) → **8505.11.90** (Other permanent magnets of metal)

EU code: **8505.11.90**.

## Classification

- **Heading**: 8505
- **Subheading**: 8505.11.90 — other permanent magnets of metal (not ferrite)
- **Code**: 8505.11.90
- **Basis**: GRI 1; NdFeB is a metallic rare-earth alloy magnet, not ferrite; EU CN 8505.11.90 applies

## Graph Links

- `classification_node` → [[product_component-ndfeb-permanent-magnets]]
- `engineering_anchor` → [[ndfeb-permanent-magnets]]
- `parent_component` → [[rotor-assembly]]
- `classified_as` → [[hs_code-8505-11-eu]]
- `source_doc` → [[explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
