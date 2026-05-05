---
agent: AA
component: Power Distribution Unit (PDU)
entity_id: ent_219
batch: TB-4
jurisdictions: [US, EU, India]
hs_code_us: "8537.10.91"
hs_code_eu: "8537.10.98"
hs_code_india: "8537.10.00"
jurisdiction_divergence: false
gri_path: GRI_1
classification_stability: stable
confidence: high
ruling_override_applied: false
pre_gri_exclusion: Section_XVII_Note_2f
source_pta_files:
  - pta/power-distribution-unit-(pdu)_us.md
  - pta/power-distribution-unit-(pdu)_eu.md
  - pta/power-distribution-unit-(pdu)_india.md
source_da_file: da/da_memo_tb4_remaining.md
extraction_timestamp: "2026-04-01T00:00:00Z"
---

## Classification Summary

The Power Distribution Unit (PDU) classifies at heading 8537.10 across all three jurisdictions. A PDU is an integrated distribution panel housing fuses, relays, and busbars for HV circuit distribution — the heading 8537 text ("boards, panels... equipped with two or more apparatus of heading 8536, for the distribution of electricity") is an exact match.

- **US**: 8537.10.91 — Other (not motor control center, not appliance-specific)
- **EU**: 8537.10.98 — Other (not numerical control panel with ADP, not programmable controller, not touch screen)
- **India**: 8537.10.00 — For a voltage not exceeding 1,000V (single India entry)

Stability is **stable**. Distribution boards are a long-established 8537 category; the EV PDU application is unambiguous.

---

## Pre-GRI Filter Results

| Filter | Applied | Result |
|--------|---------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — electrical distribution apparatus is Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | PDU assembly is not a part of general use |
| Chapter 90 Note 2 | No | Not a measuring instrument |

---

## GRI Cascade

**Resolved at GRI 1.** Heading 8537 text is an exact statutory match: "boards, panels, consoles, desks, cabinets and other bases, equipped with two or more apparatus of heading 8535 or 8536, for electric control or the distribution of electricity." The PDU satisfies each element:
- Housing/base: ✓ (PDU enclosure)
- Equipped with two or more 8535/8536 apparatus: ✓ (fuses = 8536.10; relays = 8536.41/8536.49; multiple instances of each)
- For distribution of electricity: ✓ (primary purpose is distributing HV current to sub-systems)

---

## Reconciliation: PTA vs DA

PTA: 8537.10 confirmed across all three jurisdictions.
DA (DA-002-F2): Corroborates 8537.10 with note on the 8537 vs 8536 integration threshold — individual fuse → 8536.10; integrated panel → 8537.10.

No conflict. No ruling override triggered.

---

## Key Classification Note: 8537 vs 8536 Individual Component Threshold

The 8537 heading requires the board/panel to be equipped with "two or more apparatus" of 8536. A PDU contains multiple fuses AND multiple relays — the threshold is cleared by design. If a PDU were limited to a single protective device, it would classify at the appropriate 8536 subheading for that device. That is not the case here.

## Graph Links

- `classification_node` → [[product_component-power-distribution-unit-pdu]]
- `engineering_anchor` → [[power-distribution-unit-(pdu)]]
- `parent_component` → [[integrated-e-axle]]
- `global_anchor` → [[hs_code-8537-10-global]]
- `classified_as` → [[hs_code-8537-10-91-us]]
- `classified_as` → [[hs_code-8537-10-00-in]]
- `classified_as` → [[hs_code-8537-10-98-eu]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
