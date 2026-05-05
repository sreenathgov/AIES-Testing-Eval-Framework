---
agent: PTA
component: High-Voltage Connectors
entity_id: ent_182
jurisdiction: US
fundamental_function: STRUCTURAL
is_composite_flagged: false
hs_code_candidate: "8536.69"
us_hts_subheading: "8536.69.80"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: usitc_hts_ch85_2026_complex.md
source_section: Heading 8536 — Electrical apparatus for making connections to or in electrical circuits; subheading 8536.69 — Other (plugs and sockets); subheading 8536.69.80 — Other
pilot_batch: TB-4
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — electrical connectors are Chapter 85 apparatus (heading 8536 covers them explicitly); Chapter 87 vetoed |
| Section XV Note 2 | No | Connectors with PBT GF30 housing + silver contacts are NOT parts of general use under Section XV Note 2 (which covers screws, bolts, springs per headings 7307, 7312, 7315, 7317, 7318) |
| Chapter 90 Note 2 | No | Not a measuring instrument |

## Important: D-CLASS-ENG Functional Function ≠ HS Classification

D-CLASS-ENG assigned `fundamental_function: STRUCTURAL` to this component, reflecting its role in the assembly (providing physical connection points within the battery system housing). This designation is correct for engineering taxonomy purposes.

However, HS classification is determined by what the article IS, not its engineering role in assembly. These connectors ARE electrical apparatus for making connections to or in electrical circuits — heading 8536 covers them by express statutory text. The STRUCTURAL designation does not route them to material-based chapters (Ch 39 plastics or Ch 73/76 metals) because:
1. Chapter 39 Note 2(p): Articles of Section XVI (which includes Ch 85) are excluded from Chapter 39.
2. Section XV Note 2 does not list connectors among parts of general use.
3. Heading 8536 explicitly names "plugs, sockets, lamp-holders and other connectors" as examples of covered apparatus.

## GRI Analysis

**Resolved at GRI 1.** US HTS heading 8536 explicitly covers "electrical apparatus for... making connections to or in electrical circuits (for example, switches, relays, fuses, surge suppressors, **plugs, sockets**, lamp-holders **and other connectors**, junction boxes), for a voltage not exceeding 1,000 V."

High-voltage EV connectors operate at 400–800V — within the ≤1,000V voltage ceiling of heading 8536. They provide electrical connection between HV cables and EV components (battery, inverter, motor). They are within the enumerated examples.

Within 8536, subheading 8536.69 covers "Other" plugs and sockets (not lamp-holders). EV HV connectors are multi-pin locking connectors for high-current HV circuits. US subheadings under 8536.69:
- 8536.69.40: Coaxial; cylindrical multicontact; rack and panel; printed circuit; ribbon/flat cable connectors — these are specific connector form factors
- **8536.69.80: Other** — EV HV connectors with locking mechanisms, HVIL circuits, and custom pin configurations do not fit the enumerated sub-categories; 8536.69.80 is the correct residual

## Classification

- **Code**: 8536.69.80
- **Subheading text**: Other (plugs and sockets)
- **Heading text**: Electrical apparatus for switching or protecting electrical circuits, or for making connections to or in electrical circuits... for a voltage not exceeding 1,000 V
