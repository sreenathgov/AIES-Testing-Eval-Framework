---
agent: PTA
component: Power Distribution Unit (PDU)
entity_id: ent_219
jurisdiction: US
fundamental_function: ACTIVE_CONTROL
is_composite_flagged: false
hs_code_candidate: "8537.10"
us_hts_subheading: "8537.10.91"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: usitc_hts_ch85_2026_complex.md
source_section: Heading 8537.10 — Boards, panels, consoles etc. equipped with two or more apparatus of 8535 or 8536, for a voltage not exceeding 1,000V; subheading 8537.10.91 — Other
pilot_batch: TB-4
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — electrical distribution apparatus is Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | Assembly of fuses, relays, busbars is not a part of general use |
| Chapter 90 Note 2 | No | Not a measuring instrument |

## GRI Analysis

**Resolved at GRI 1.** US HTS heading 8537 covers "boards, panels, consoles, desks, cabinets and other bases, equipped with two or more apparatus of heading 8535 or 8536, for electric control or the distribution of electricity."

A Power Distribution Unit (PDU) is precisely this: an integrated housing equipped with fuses (8536.10), relays (8536.41/8536.49), and busbars, assembled for the purpose of distributing high-voltage current to EV sub-systems. The heading text matches the physical description without ambiguity.

The PDU is not a motor control center (8537.10.60) and not assembled for domestic appliances (8537.10.30). Subheading 8537.10.91 (Other) is the correct residual.

Note: 8537 requires "two or more apparatus of 8535 or 8536." A PDU by definition contains multiple fuses and relays → threshold satisfied.

## Classification

- **Code**: 8537.10.91
- **Subheading text**: Other
- **Heading text**: Boards, panels, consoles, desks, cabinets and other bases, equipped with two or more apparatus of heading 8535 or 8536, for electric control or the distribution of electricity, for a voltage not exceeding 1,000 V
