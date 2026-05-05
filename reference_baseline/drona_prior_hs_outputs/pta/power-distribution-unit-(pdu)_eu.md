---
agent: PTA
component: Power Distribution Unit (PDU)
entity_id: ent_219
jurisdiction: EU
fundamental_function: ACTIVE_CONTROL
is_composite_flagged: false
hs_code_candidate: "8537.10"
eu_cn_subheading: "8537.10.98"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: eu_hs_commission_implementing_regulation_(eu)_2025_1926_evs.md
source_section: CN heading 8537.10 — Boards etc. for electric control or distribution, ≤1,000V; subheading 8537.10.98 — Other
pilot_batch: TB-4
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — electrical distribution apparatus is Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | Not a part of general use |
| Chapter 90 Note 2 | No | Not a measuring instrument |

## GRI Analysis

**Resolved at GRI 1.** EU CN heading 8537.10 covers boards/panels/bases equipped with two or more 8535/8536 apparatus for electric control or distribution at ≤1,000V. The PDU is such a unit.

Within 8537.10, the EU CN distinguishes:
- 8537.10.10: Numerical control panels with built-in ADP machine — NO
- 8537.10.91: Programmable memory controllers — NO (PDU is not a PLC)
- 8537.10.95: Touch-sensitive data input devices — NO
- 8537.10.98: Other — YES

A PDU is a distribution board assembly housing fuses and relays for power distribution, not a programmable controller or numerical control panel. 8537.10.98 (Other) is the correct residual.

## Classification

- **Code**: 8537.10.98
- **Subheading text**: Other
- **Heading text**: Boards, panels, consoles, desks, cabinets and other bases, equipped with two or more apparatus of heading 8535 or 8536, for electric control or the distribution of electricity, for a voltage not exceeding 1,000 V
