---
agent: PTA
component: Separator (PE/PP Film)
entity_id: ent_tb3_04
jurisdiction: EU
fundamental_function: IONIC_BARRIER
material_composition: "Microporous polyethylene (PE) or polypropylene (PP) film; thickness 10-25μm; microporous cellular structure"
is_composite_flagged: false
gri_3_required: false
hs_code_candidate: "8507.90"
gri_path: GRI_1
stability: stable
confidence: high
validation_status: validated
corpus_gap: false
jurisdiction_divergence: true
jurisdiction_divergence_note: "EU: 8507.90.31 (<40μm battery separator, Commission Note C/2025/6096); US: 3921.19.0000 (cellular plastics)"
batch: TB-3
refinement_run: "2026-04-06"
source_doc: "HS - DR - GapFilling - Battery Material Tariff Classification Research.md"
source_section: "GRI Analysis; EU battery separator carve-out below 40 microns"
ruling_anchor: "EU Commission Note C/2025/6096 (PE/PP separator <40μm → 8507.90.31 as battery part); EU CN 2026 Reg 2025/1926"
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XV Note 2 (parts of general use) | No | Battery part classification specifically determined |
| Section XVII Note 2(f) | No | Not electrical machinery |
| Chapter 90 Note 2 | No | Not a measuring instrument |

`exclusion_checks_run: ["Section XV Note 2", "Section XVII Note 2(f)", "Chapter 90 Note 2"]`

## GRI Analysis

**Step 1 — EU Battery Part Carve-Out**

EU CN takes a fundamentally different approach from the US for thin battery separator films.

**EU Commission Note C/2025/6096**: The European Commission issued a classification regulation confirming that PE and PP microporous separator films with thickness **<40μm** are classified under **8507.90.31** as "Parts of electric accumulators: Separators." The basis: at <40μm, these films have no commercial use outside lithium-ion battery cells — they are exclusively battery parts. The thickness threshold (<40μm) is the controlling criterion.

**EU CN 2026 (Regulation 2025/1926)**: Codified the C/2025/6096 determination into the 2026 Combined Nomenclature. Subheading 8507.90.31 was specifically designated for "separators of electric accumulators, of plastics, with a thickness of less than 40 μm."

**Step 2 — Heading 3921 Route Rejected**

EU CN explanatory notes: when a plastics product has a specific subheading in another chapter (here, Chapter 85 via battery part classification regulation), that specific heading prevails over the general plastics headings. For separators <40μm, the Commission Note is binding and overrides the general cellular plastics route.

For separators ≥40μm: no Commission Note carve-out → default to 3921.19 (cellular plastics).

**Commercial battery-grade separators are uniformly <40μm** (typically 10-25μm) → EU classification: 8507.90.31.

## Classification

- **Code**: 8507.90.31 (EU CN 2026; battery separator <40μm, per Commission Note C/2025/6096)
- **Basis**: GRI 1; EU Commission regulation C/2025/6096 binding; EU CN 2026 codified at 8507.90.31; thickness <40μm commercially universal for battery-grade separators
- **Stability**: stable
- **Confidence**: high

## Jurisdiction Divergence Flag

**CRITICAL**: EU and US classify this component differently.
- EU: 8507.90.31 (battery part — function-first, <40μm threshold, Commission binding regulation)
- US: 3921.19.0000 (cellular plastic — material-first, CBP HQ 967313)
- India: 3921.19.90 (cellular plastic — material-first)

This represents a genuine heading-level divergence, not a subheading difference. D-RULING handoff required.

## Graph Links

- `classification_node` → [[product_component-separator-pe-pp-film]]
- `classified_as` → [[hs_code-8507-90-31-eu]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
