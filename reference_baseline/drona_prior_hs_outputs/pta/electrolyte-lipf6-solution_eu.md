---
agent: PTA
component: Electrolyte (LiPF6 Solution)
entity_id: ent_tb3_03
jurisdiction: EU
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
ruling_anchor: "EU CN Chapter 28 Note 1 (single defined compound requirement); EU Explanatory Notes heading 3824 (prepared chemical mixtures for specific industrial use)"
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

EU CN Chapter 28, Note 1 applies identically: "separate chemically defined compounds" only. The LiPF6 electrolyte solution — LiPF6 dissolved in EC/DMC/EMC with additives — is a multi-component mixture. Not classifiable under Chapter 28.

**Pure LiPF6 in EU**: Would classify under EU CN 2826.90.80 (other fluorides — other). Not the commercially traded form.

**Step 2 — Chapter 38 Classification**

EU CN Heading 3824, Explanatory Notes: chemical preparations for specific industrial use that are not classifiable under other headings route here. The electrolyte solution is specifically formulated for lithium-ion battery electrolyte service → 3824.99.

EU CN 3824.99 — further divided at 8-digit level. For inorganic salt solutions used in industrial processes: 3824.99.92 or 3824.99.96 (Other — classification depends on whether mixtures of inorganic compounds or not). The LiPF6 in organic solvent is a mixed organic/inorganic preparation → 3824.99.96 (other) pending verification of current EU tariff schedule.

## Classification

- **Code**: 3824.99 (EU CN; 8-digit: 3824.99.96 candidate — mixed organic/inorganic preparation, other)
- **Basis**: GRI 1; LiPF6 electrolyte solution = multi-component chemical preparation; ejected from Chapter 28 Note 1; EU CN 3824.99 residual chemical preparations heading
- **Stability**: stable
- **Confidence**: high

## Graph Links

- `classification_node` → [[product_component-electrolyte-lipf6-solution]]
- `classified_as` → [[hs_code-3824-99-eu]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
