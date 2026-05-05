---
agent: PTA
component: Electrolyte (LiPF6 Solution)
entity_id: ent_tb3_03
jurisdiction: US
fundamental_function: IONIC_CONDUCTOR
material_composition: "LiPF6 (lithium hexafluorophosphate) dissolved in organic carbonate solvent mixture — ethylene carbonate (EC), dimethyl carbonate (DMC), ethyl methyl carbonate (EMC); with additives (vinylene carbonate, fluoroethylene carbonate)"
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
source_section: "GRI Analysis; Chapter 28 Note 1 boundary; CBP N327146"
ruling_anchor: "CBP N327146 (LiPF6 electrolyte solution → 3824.99.93.97; prepared mixture, not defined compound)"
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

Two analytically distinct products:

**(A) Pure LiPF6 salt**: Lithium hexafluorophosphate as a dry, standalone inorganic compound → HTSUS 2826.90 (other fluorides). This is NOT the commercially traded electrolyte.

**(B) LiPF6 electrolyte solution**: LiPF6 dissolved in a multi-component carbonate solvent mixture with multiple performance additives. This is a **mixture** of multiple chemically distinct compounds — it cannot be classified under Chapter 28 (which requires a single, chemically defined compound). Chapter 28 Note 1 applies: "separate chemically defined compounds" only. A solution of LiPF6 in EC/DMC/EMC + additives = multiple distinct chemical entities → ejected from Chapter 28.

**Step 2 — Chapter 38 Classification**

The electrolyte solution is a "chemical preparation of the chemical or allied industries" prepared for specific use (lithium-ion battery electrolyte). Chapter 38, Heading 3824 — "chemical products and preparations... not elsewhere specified or included." Subheading 3824.99 — Other.

**CBP N327146 (binding precedent)**: LiPF6 electrolyte solution (LiPF6 in organic carbonate solvents with additives) → **3824.99.93.97** (HTSUS — Chemical preparations for specific use, other).

## Classification

- **Code**: 3824.99.93.97 (US HTSUS, per CBP N327146)
- **Basis**: GRI 1; LiPF6 electrolyte solution = multi-component chemical preparation, not a chemically defined compound; ejected from Chapter 28 Note 1; CBP N327146 binding precedent
- **Stability**: stable
- **Confidence**: high

## Note on Pure LiPF6 (separate import stream)

If pure LiPF6 (dry salt, not dissolved) is imported separately: **2826.90.9000** (US HTSUS — other fluorides; other; other).

## Graph Links

- `classification_node` → [[product_component-electrolyte-lipf6-solution]]
- `classified_as` → [[hs_code-3824-99-us]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
