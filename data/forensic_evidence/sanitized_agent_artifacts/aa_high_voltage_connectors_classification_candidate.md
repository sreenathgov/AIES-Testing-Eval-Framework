<!-- Reviewer-safe sanitized forensic artifact. This file evidences artifact origin only and is not external legal authority. -->

---
agent: AA
component: High-Voltage Connectors
entity_id: ent_182
batch: TB-4
jurisdictions: [US, EU, India]
hs_code_us: "8536.69.80"
hs_code_eu: "8536.69.90"
hs_code_india: "8536.69.90"
jurisdiction_divergence: false
gri_path: GRI_1
classification_stability: stable
confidence: high
ruling_override_applied: false
pre_gri_exclusion: Section_XVII_Note_2f
source_pta_files:
  - pta/high-voltage-connectors_us.md
  - pta/high-voltage-connectors_eu.md
  - pta/high-voltage-connectors_india.md
source_da_file: da/da_memo_tb4_remaining.md
extraction_timestamp: "2026-04-01T00:00:00Z"
---

## Classification Summary

High-Voltage Connectors classify at heading 8536.69 (plugs and sockets — other) across all three jurisdictions. Subheading variation is minor and reflects each jurisdiction's connector form-factor or material subdivisions:

- **US**: 8536.69.80 — Other (EV HV connectors are not coaxial, PCB, ribbon, or other enumerated types → 8536.69.80 residual)
- **EU**: 8536.69.90 — Other (same logic; not coaxial, not PCB)
- **India**: 8536.69.90 — Plugs and sockets, of other materials (silver-plated contacts are the functional metal element; alternatively 8536.69.10 if PBT GF30 housing determines material classification — heading-level unchanged in either case)

Stability is **stable**. Electrical connectors have a long-established place in heading 8536. EV HV connectors operate at 400–800V, within the ≤1,000V ceiling of 8536.

---

## Pre-GRI Filter Results

| Filter | Applied | Result |
|--------|---------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — electrical connectors are electrical apparatus (8536 is Chapter 85); Chapter 87 vetoed |
| Section XV Note 2 | No | PBT GF30 housing + silver contacts do not constitute "parts of general use" under Section XV Note 2 (which covers screws, bolts, springs per headings 7307–7318); connectors are not listed |
| Chapter 90 Note 2 | No | Not a measuring instrument |

---

## Critical Reconciliation: engineering handoff STRUCTURAL Function vs HS Classification

engineering handoff assigned `fundamental_function: STRUCTURAL` to this component, reflecting its engineering role as a mechanical connection point within the battery system housing.

**This does not affect HS classification.** HS classification is determined by what the article IS in the legal tariff text, not by its role in assembly. Heading 8536 explicitly identifies "plugs, sockets, lamp-holders and other connectors" as the named examples of covered apparatus. The article IS an electrical connector. The STRUCTURAL engineering designation is not a valid basis for routing to:
- Chapter 39 (plastics): Excluded by Chapter 39 Note 2(p) — Section XVI articles (including Ch 85) are excluded from Ch 39.
- Chapter 73/74/76 (metals): Section XV Note 2 does not list connectors among parts of general use.
- Chapter 87 (vehicle parts): Section XVII Note 2(f) vetoes.

Classification at 8536.69 is correct and complete.

---

## GRI Cascade

**Resolved at GRI 1.** Heading 8536 text expressly covers "apparatus for making connections to or in electrical circuits" and names "plugs, sockets... and other connectors" as examples. EV HV connectors make high-current connections between HV cables and EV components (battery, inverter, motor). Operating voltage 400–800V is within the ≤1,000V ceiling. GRI 1 is determinative.

Within 8536, the sub-heading cascade:
- 8536.10: Fuses — NO
- 8536.20: Automatic circuit breakers — NO
- 8536.30: Other apparatus for protecting circuits — NO
- 8536.41/8536.49: Relays — NO
- 8536.50: Other switches — NO
- 8536.61/8536.69: Lamp-holders and other plugs/sockets — 8536.69 applies (not lamp-holders)
- 8536.70: Connectors for optical fibres — NO
- 8536.90: Other apparatus — 8536.69 is more specific

**8536.69** is the correct subheading.

---

## India 8-Digit Note

India subdivides 8536.69 by material (85366910 = of plastic; 85366990 = of other materials). The HV Connector has a PBT GF30 plastic housing and silver-plated copper contacts. Two defensible readings:
1. Housing material → 85366910 (of plastic)
2. Functional contact material → 85366990 (of other materials)

India customs practice for mixed-material connectors is not definitively resolved in the available corpus. Both codes result in the same heading-level classification. A conservative importer might declare 85366990 (the "other materials" catchall covering the metal contact element).

## Graph Links

- `classification_node` → [[product_component-high-voltage-connectors]]
- `engineering_anchor` → [[high-voltage-connectors]]
- `parent_component` → [[physical-enclosure]]
- `global_anchor` → [[hs_code-8536-69-global]]
- `classified_as` → [[hs_code-8536-69-80-us]]
- `classified_as` → [[hs_code-8536-69-90-in]]
- `classified_as` → [[hs_code-8536-69-90-eu]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
