---
agent: PTA
component: Anode Active Material (Graphite)
entity_id: ent_tb3_02
jurisdiction: EU
fundamental_function: ELECTROCHEMICAL_ACTIVE
material_composition: "Battery-grade graphite — either (a) natural graphite purified/spheroidized (2504.10) or (b) synthetic/artificial graphite from petroleum coke, surface-modified (3801.10)"
is_composite_flagged: false
gri_3_required: false
hs_code_candidate: "3801.10"
hs_code_candidate_alt: "2504.10"
gri_path: GRI_1
stability: stable
confidence: high
validation_status: validated
corpus_gap: false
batch: TB-3
refinement_run: "2026-04-06"
source_doc: "HS - DR - GapFilling - Battery Material Tariff Classification Research.md"
source_section: "GRI Analysis; Chapter 25 Note 1 boundary; EU CN 2026 graphite subheading"
ruling_anchor: "EU CN 2026 Reg 2025/1926 (3801.10.10 for battery-grade artificial graphite — new specific subheading); EU Explanatory Notes Ch 38 heading 3801"
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XV Note 2 (parts of general use) | No | Chemical/mineral, not mechanical part |
| Section XVII Note 2(f) | No | Not electrical machinery |
| Chapter 90 Note 2 | No | Not a measuring instrument |

`exclusion_checks_run: ["Section XV Note 2", "Section XVII Note 2(f)", "Chapter 90 Note 2"]`

## GRI Analysis

**Step 1 — Natural vs. Synthetic Determination**

EU CN applies the same Chapter 25 Note 1 boundary as the WCO: heading 2504 covers natural graphite only in a crude or minimally processed state. Spheroidization, purification to >99.95%, and surface carbon-coating take battery-grade natural graphite outside Chapter 25 Note 1.

**Step 2 — EU CN 2026 New Subheading**

EU CN 2026 (Regulation 2025/1926) introduced **3801.10.10** specifically for "artificial graphite used in the manufacture of lithium-ion battery electrodes." This new subheading confirms the EU's intent: battery-grade graphite (whether from synthetic or processed-natural origin) classifies under 3801.10, with 3801.10.10 as the specific subcode for battery electrode use.

**3801.10.10 vs 3801.10.90**: EU CN 2026 split 3801.10 into:
- 3801.10.10 — artificial graphite for lithium-ion battery electrodes (new, battery-specific)
- 3801.10.90 — other artificial graphite

Battery-grade anode graphite = 3801.10.10 (EU CN 2026).

**Pure natural graphite flakes**: EU CN 2504.10.10 (crystalline, <0.1mm particle size) or 2504.10.90 (other). If surface-modified → 3801.10.10.

## Classification

- **Code**: 3801.10.10 (EU CN 2026, Reg 2025/1926 — battery electrode graphite)
- **Basis**: GRI 1 (heading) + GRI 6 (subheading); EU CN 2026 specific subheading for Li-ion battery electrode graphite; Chapter 25 Note 1 boundary excludes surface-modified/spheroidized grades
- **Stability**: stable
- **Confidence**: high

## Conditional Note for DRONA

- IF graphite = pure natural flake, no surface modification → **2504.10** (EU CN)
- IF graphite = synthetic (Acheson) OR surface-modified spherical (battery-grade) → **3801.10.10** (EU CN 2026)
- Battery-grade anode graphite default (EU): 3801.10.10

## Graph Links

- `classification_node` → [[product_component-anode-active-material-graphite]]
- `classified_as` → [[hs_code-3801-10-eu]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
