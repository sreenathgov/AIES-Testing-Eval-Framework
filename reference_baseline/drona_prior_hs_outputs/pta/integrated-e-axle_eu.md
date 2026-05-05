---
agent: PTA
component: Integrated E-Axle
entity_id: ent_187
jurisdiction: EU
fundamental_function: ENERGY_CONVERSION
material_composition: Integrated electromechanical system combining traction motor, reduction gearbox, and power electronics in unified structural housing
is_composite_flagged: true
gri_3_required: true
hs_code_candidate: "8708.99"
gri_path: GRI_3b
stability: stable
confidence: high
data_gap_note: "EU CN 8-digit code for e-axle drivetrain parts requires EU CN lookup; heading-level 8708.99 confirmed; 8-digit pending"
source_doc: explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs.md
source_section: Heading 8708 — parts and accessories for motor vehicles; WCO EN Section XVII
ruling_flag: "No specific EU BTI ruling on e-axle available in corpus; WCO HSC position supports 8708.99 for chassis-integrated assemblies"
batch: TB-2
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Considered** | Same analysis as US jurisdiction: composite good; Note 2(f) does not veto 8708 for composite goods where the mechanical drivetrain gives essential character |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Not applicable |

## GRI Cascade

Same GRI 3(b) cascade as US jurisdiction. EU CN applies the WCO GRI identically. The essential character analysis (vehicular drivetrain > motor/electronics for a chassis-integrated assembly) applies uniformly.

**GRI 3(b) resolution**: Heading 8708.99 — vehicular drivetrain parts. EU CN follows WCO GRI 3(b) essential character analysis; same conclusion as US.

**EU CN 8-digit**: EU CN 8708.99 has multiple subdivisions. The precise 8-digit code requires EU CN CN lookup for "other parts of transmissions for motor vehicles" or "other." Without this specific lookup in the corpus, the classification is confirmed at the heading level (8708.99). A heading-level EU node is created with `resolution_status: pending_8digit`.

## Classification

- **Heading**: 8708.99
- **Code**: 8708.99 (heading-level; 8-digit pending EU CN lookup)
- **Basis**: GRI 3(b); vehicular drivetrain essential character; EU CN aligns with WCO GRI analysis

## Graph Links

- `classification_node` → [[product_component-integrated-e-axle]]
- `engineering_anchor` → [[integrated-e-axle]]
- `classified_as` → [[hs_code-8708-99-eu]]
- `source_doc` → [[explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
