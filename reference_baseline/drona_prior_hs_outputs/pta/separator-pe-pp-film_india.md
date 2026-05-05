---
agent: PTA
component: Separator (PE/PP Film)
entity_id: ent_tb3_04
jurisdiction: India
fundamental_function: IONIC_BARRIER
material_composition: "Microporous polyethylene (PE) or polypropylene (PP) film; thickness 10-25μm; microporous cellular structure"
is_composite_flagged: false
gri_3_required: false
hs_code_candidate: "3921.19"
gri_path: GRI_1
stability: stable
confidence: medium
validation_status: validated
corpus_gap: false
jurisdiction_divergence: true
jurisdiction_divergence_note: "India: 3921.19.90 (cellular plastics — material-first); EU: 8507.90.31 (battery separator carve-out); US: 3921.19.0000"
batch: TB-3
refinement_run: "2026-04-06"
source_doc: "HS - DR - GapFilling - Battery Material Tariff Classification Research.md"
source_section: "GRI Analysis; Chapter 39 cellular plastics boundary; material-first treatment"
ruling_anchor: "ITC-HS Chapter 39 Note; India material-first classification; no Indian ruling on battery separator classification found"
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XV Note 2 (parts of general use) | No | Plastic film, not base metal |
| Section XVII Note 2(f) | No | Not electrical machinery |
| Chapter 90 Note 2 | No | Not a measuring instrument |

`exclusion_checks_run: ["Section XV Note 2", "Section XVII Note 2(f)", "Chapter 90 Note 2"]`

## GRI Analysis

**Step 1 — Material Identity**

India follows the material-first classification principle for plastics. The separator is a microporous polymer film with a cellular structure.

**Step 2 — Chapter 39 Cellular Plastics**

ITC-HS Heading 3921 — "Other plates, sheets, film, foil and strip, of plastics" including cellular structures.

India has not adopted a specific carve-out for battery separators equivalent to EU Commission Note C/2025/6096. In the absence of a binding Indian ruling or CBIC circular creating a battery-part classification for separator films, the default material-first route applies:

Microporous PE separator → cellular PE plastic → 3921.19.90 (Other cellular plastic plates/sheets/film: Other, not of polyurethane)
Microporous PP separator → cellular PP plastic → 3921.19.90 (same subheading)

**Step 3 — Chapter 85 Battery Part Analysis (India)**

ITC-HS Chapter 85, Heading 8507 parts: India does not have a specific subheading for battery separators (unlike EU 8507.90.31). In the absence of a specific carve-out, a separator sold as a separate import item classifies by its material composition → Chapter 39.

**Note**: India's battery-sector customs regime is evolving rapidly. A future CBIC circular or advance ruling could shift this position toward Chapter 85, following the EU model. This classification should be monitored.

## Classification

- **Code**: 3921.19.90 (ITC-HS — cellular plastic film, other)
- **Basis**: GRI 1; India material-first; no Indian battery-separator carve-out equivalent to EU C/2025/6096; default cellular plastics classification
- **Stability**: stable
- **Confidence**: medium (no binding Indian ruling; EU divergence creates precedent pressure)

## Jurisdiction Divergence Flag

India follows the US approach (cellular plastics) rather than the EU approach (battery part). Monitor for CBIC advance ruling or circular that may shift India toward EU position.

## Graph Links

- `classification_node` → [[product_component-separator-pe-pp-film]]
- `classified_as` → [[hs_code-3921-19-in]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
