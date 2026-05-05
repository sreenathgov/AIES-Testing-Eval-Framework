---
agent: PTA
component: Battery Management System (BMS)
entity_id: ent_217
jurisdiction: EU
fundamental_function: ACTIVE_CONTROL
is_composite_flagged: false
hs_code_candidate: "8537.10"
eu_cn_subheading: "8537.10.91 or 8537.10.99"
gri_path: GRI_1
stability: stable
confidence: high
confidence_note: 8537.10 is established for the standalone BMS PCBA after WS-6 refinement; 8507 pressure applies only when cells are imported with the control assembly
source_doc: explanatory_notes_to_the_combined_nomenclature_of_the_european_union_evs.md
source_section: Heading 8537 — boards and panels for electric control ≤1,000V
pilot_batch: TB-1
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — control apparatus is Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Not applicable — ACTIVE_CONTROL; BMS acts on measurements rather than purely measuring |

## GRI Analysis

**Resolved at GRI 1.** CN heading 8537.10 for boards/panels for electric control ≤1,000V. EU CN Regulation 2025/1926 does not create a dedicated BMS heading that displaces the standalone control-board analysis. If a BMS is imported together with battery cells as a composite good, GRI 3(b) may redirect to heading 8507, but that is not the present article.

## Classification

- **Code**: 8537.10 (EU CN 8-digit remains product-spec dependent; heading-level classification is stable)
- **Subheading text**: Boards, panels for electric control — for a voltage not exceeding 1,000V
- **Heading text**: Boards, panels equipped with apparatus of 8535/8536 for electric control
