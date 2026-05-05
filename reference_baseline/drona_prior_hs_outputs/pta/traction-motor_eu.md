---
agent: PTA
component: Traction Motor
entity_id: ent_221
jurisdiction: EU
fundamental_function: ENERGY_CONVERSION
is_composite_flagged: false
hs_code_candidate: "8501.53"
eu_cn_subheading: "8501.53.50"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs.md
source_section: Chapter 85, heading 8501.53 — AC motors multi-phase >75 kW
ruling_corroboration: EU BTI CZBTI34/018997/2025-580000-04/01 (80 kW AC traction motor → CN 8501.53.50.10)
pilot_batch: TB-4
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — electric motor is Chapter 85 apparatus; Chapter 87 vetoed |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Not applicable |

## GRI Analysis

**Resolved at GRI 1.**

CN heading 8501.53 for AC multi-phase motors >75 kW. EU BTI ruling (CZ, CZBTI34/018997/2025-580000-04/01) classified an 80 kW AC traction motor with integrated inverter at CN 8501.53.50.10. Standalone traction motor without inverter → 8501.53 with higher confidence (no composite good analysis required).

**Competing headings**: 8708 excluded by Section XVII Note 2(f).

## Classification

- **Code**: 8501.53.50
- **Subheading text**: Other AC motors, multi-phase, of an output exceeding 75 kW
- **Heading text**: Electric motors and generators (excluding generating sets)
