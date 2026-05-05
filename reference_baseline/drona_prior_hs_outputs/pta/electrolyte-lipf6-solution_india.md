---
agent: PTA
component: Electrolyte (LiPF6 Solution)
entity_id: ent_tb3_03
jurisdiction: India
fundamental_function: IONIC_CONDUCTOR
material_composition: "LiPF6 dissolved in organic carbonate solvent mixture (EC/DMC/EMC) with additives"
is_composite_flagged: true
gri_3_required: false
hs_code_candidate: "3824.99"
gri_path: GRI_1
stability: stable
confidence: high
validation_status: validated
corpus_gap: false
batch: TB-3
refinement_run: "2026-04-06"
source_doc: "HS - DR - GapFilling - Battery Material Tariff Classification Research.md"
source_section: "GRI Analysis; Chapter 28 Note 1 boundary; prepared electrolyte mixture"
ruling_anchor: "ITC-HS Chapter 28 Note 1 (single defined compound); India material-first principle → Chapter 38 residual"
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XV Note 2 (parts of general use) | No | Chemical preparation, not mechanical part |
| Section XVII Note 2(f) | No | Not electrical machinery |
| Chapter 90 Note 2 | No | Not a measuring instrument |

`exclusion_checks_run: ["Section XV Note 2", "Section XVII Note 2(f)", "Chapter 90 Note 2"]`

## GRI Analysis

**Step 1 — Solution vs. Pure Compound**

India ITC-HS Chapter 28, Note 1 is identical to WCO text: "separate chemically defined compounds" only. The LiPF6 electrolyte solution — LiPF6 dissolved in EC/DMC/EMC with additives — is a multi-component mixture, not a single defined compound. Ejected from Chapter 28.

**Pure LiPF6 in India**: ITC-HS 2826.90.90 (other fluorides — other). Not the commercially traded electrolyte form.

**Step 2 — Chapter 38 Classification**

India ITC-HS Heading 3824 — "Prepared binders for foundry moulds or cores; chemical products and preparations of the chemical or allied industries..., not elsewhere specified or included." The electrolyte solution is a chemical preparation formulated for lithium-ion battery service → 3824.99.00.

India does not have a battery-specific sub-code for electrolyte solutions. ITC-HS 2024 retains 3824.99.00 as the residual subheading.

## Classification

- **Code**: 3824.99.00 (ITC-HS)
- **Basis**: GRI 1; LiPF6 electrolyte solution = multi-component chemical preparation, not a defined compound; ejected from Chapter 28 Note 1; ITC-HS 3824.99.00 residual
- **Stability**: stable
- **Confidence**: high

## Graph Links

- `classification_node` → [[product_component-electrolyte-lipf6-solution]]
- `classified_as` → [[hs_code-3824-99-in]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
