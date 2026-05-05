---
agent: PTA
component: High-Voltage Contactor
entity_id: ent_144
jurisdiction: EU
fundamental_function: ACTIVE_CONTROL
is_composite_flagged: false
hs_code_candidate: "8536.49"
eu_cn_subheading: "8536.49.90"
gri_path: GRI_1
stability: stable
confidence: high
confidence_note: Voltage confirmed ≤1,000V via WS-6 refinement; EU CN 8536.49.90 is established for non-motor-starter EV contactors
source_doc: explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs.md
source_section: Heading 8536 — relays and contactors ≤1,000V
pilot_batch: TB-4
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — electromagnetic switch is Chapter 85 apparatus; Chapter 87 vetoed |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Not applicable |

## GRI Analysis

**Resolved at GRI 1.** EU CN heading 8536.49 for other relays ≤1,000V. WS-6 refinement confirmed the voltage boundary and supports 8536.49.90 for EV disconnect/isolation contactors that are not motor starters.

## Classification

- **Code**: 8536.49.90
- **Subheading text**: Other relays — for a voltage exceeding 60V but not exceeding 1,000V
- **Heading text**: Electrical apparatus for switching or protecting electrical circuits...for a voltage not exceeding 1,000V
