---
agent: PTA
component: Vehicle Control Unit (VCU)
entity_id: ent_218
jurisdiction: EU
fundamental_function: ACTIVE_CONTROL
is_composite_flagged: false
hs_code_candidate: "8537.10"
eu_cn_subheading: "8537.10.91"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: eu_hs_commission_implementing_regulation_(eu)_2025_1926_evs.md
source_section: CN heading 8537.10 — Boards etc. for electric control or distribution, ≤1,000V; Chapter 84 Note 5(E) — dedicated controllers excluded from 8471; subheading 8537.10.91 — Programmable memory controllers
pilot_batch: TB-4
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — electrical control apparatus is Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | Not a part of general use |
| Chapter 90 Note 2 | No | Not a measuring instrument |

## Pre-Classification Note: 8471 vs 8537 Distinction

Same analysis as US jurisdiction. Chapter 84 Note 5(E) excludes dedicated controllers from heading 8471. A VCU is a dedicated vehicle powertrain controller → NOT 8471 → heading 8537 applies.

## GRI Analysis

**Resolved at GRI 1.** EU CN heading 8537.10 applies. Within 8537.10:

- 8537.10.10: Numerical control panels with built-in ADP machine — NO (VCU is not a numerical control panel of this type)
- **8537.10.91: Programmable memory controllers** — a VCU is a programmable controller executing stored firmware algorithms to control vehicle systems. EU customs classification of programmable dedicated controllers consistently falls under 8537.10.91.
- 8537.10.95: Touch-sensitive data input devices — NO
- 8537.10.98: Other — fallback if 8537.10.91 disputed

8537.10.91 is the most specific applicable EU CN subheading for the VCU as a programmable dedicated controller.

## Classification

- **Code**: 8537.10.91
- **Subheading text**: Programmable memory controllers
- **Heading text**: Boards, panels, consoles, desks, cabinets and other bases, equipped with two or more apparatus of heading 8535 or 8536, for electric control or the distribution of electricity, for a voltage not exceeding 1,000 V
