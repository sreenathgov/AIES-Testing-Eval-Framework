---
agent: PTA
component: Silicon-Alloyed Electrical Steel Core (NOES)
entity_id: ent_tb3_07
jurisdiction: US
fundamental_function: MAGNETIC_CORE
material_composition: "Non-oriented electrical steel (NOES); silicon content 0.5-3.5% by weight; flat-rolled; for traction motor stator/rotor laminations; supplied as slit coil"
is_composite_flagged: false
gri_3_required: false
hs_code_candidate: "7226.19"
hs_code_candidate_alt: "7225.19"
gri_path: GRI_1
stability: stable
confidence: medium
width_determination: "data_pending — typical motor lamination slit coil <600mm; but original coil may be ≥600mm pre-slitting"
client_fact_pending: true
client_fact_key: "coil_width_mm"
client_fact_note: "Classification depends on width as imported: width <600mm -> 7226.19.1000; width >=600mm -> 7225.19.0000."
legal_rule_resolved: true
validation_status: validated
corpus_gap: false
batch: TB-3
refinement_run: "2026-04-06"
source_doc: "HS - DR - GapFilling - Electrical Steel Width-Split Resolution.md"
source_section: "GRI Analysis; Chapter 72 width split at 600mm; slit coil import condition"
ruling_anchor: "HTSUS Chapter 72 width split: 7225 (width ≥600mm), 7226 (width <600mm); CBP guidance on slit coil — classification based on width as imported"
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XV Note 2 (parts of general use) | **YES — FIRED** | Silicon-alloyed steel = base metal article of general use → Chapter 72 |
| Section XVII Note 2(f) | No | Not electrical machinery |
| Chapter 90 Note 2 | No | Not a measuring instrument |

`exclusion_checks_run: ["Section XV Note 2", "Section XVII Note 2(f)", "Chapter 90 Note 2"]`
`section_xv_note_2_fired: true`

## GRI Analysis

**Step 1 — Section XV Note 2 Applies**

Section XV Note 2: silicon-alloyed electrical steel (NOES) is a base metal material of general use (used in motors, generators, transformers) → Chapter 72 (iron and steel).

**Step 2 — Width-Based Classification in Chapter 72**

HTSUS Chapter 72 structures flat-rolled silicon-electrical steel by width:
- **Heading 7225**: Flat-rolled products of other alloy steel, of a width of **600mm or more**
  - 7225.11: Grain-oriented (GOES)
  - 7225.19: Other (= NOES, width ≥600mm)
- **Heading 7226**: Flat-rolled products of other alloy steel, of a width of **less than 600mm**
  - 7226.11: Grain-oriented (GOES)
  - 7226.19: Other (= NOES, width <600mm)

The determining criterion is the **width of the product as imported** (not the original master coil width if it has been slit).

**Step 3 — Motor Lamination Slit Coil Width Analysis**

Traction motor stator cores use NOES lamination stampings. The stamping process uses slit steel coils. Width determination:
- Master coil (mill-produced): typically 1000-1500mm (≥600mm → 7225.19 if imported as master coil)
- Slit coil (for motor lamination stamping): typically cut to 50-500mm widths to match the stator outer diameter of EV traction motors (commonly 150-350mm OD motors → slit coil width typically 200-400mm, i.e., <600mm → 7226.19)

**CBP principle**: Classification is based on the product as imported. If imported as slit coil (width <600mm) → 7226.19. If imported as master coil (width ≥600mm) → 7225.19.

**Default position for motor lamination supply chain**: NOES for motor lamination is commercially sourced as slit coil (width <600mm) → **7226.19.1000** (US HTSUS — other flat-rolled NOES, width <600mm).

**Data gap flag**: Confirmed width requires the specific entity's supply chain specification. This classification is width-dependent, not a legal ambiguity.

## Classification

- **Code**: 7226.19.1000 (US HTSUS — NOES flat-rolled, width <600mm, as slit coil; primary position)
- **Alt Code**: 7225.19.0000 (US HTSUS — if imported as master coil ≥600mm)
- **Basis**: GRI 1; Section XV Note 2 → Chapter 72; width split at 600mm determines heading; motor lamination slit coil typically <600mm → 7226.19
- **Stability**: stable
- **Confidence**: medium (heading/code depends on width as imported; motor lamination slit coil default = 7226.19)

## Width Data Note for DRONA

Width must be confirmed per supply chain specification. Probable: slit coil <600mm → 7226.19. If master coil import: 7225.19.

## Graph Links

- `classification_node` → [[product_component-silicon-alloyed-electrical-steel-core-noes]]
- `classified_as` → [[hs_code-7226-19-us]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
