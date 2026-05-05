---
agent: AA
component: Battery Control Unit (BCU)
entity_id: ent_169
batch: TB-1
jurisdictions: [US, EU, India]
hs_code_us: "8537.10.91"
hs_code_eu: "8537.10.91"
hs_code_india: "8537.10.00"
jurisdiction_divergence: false
gri_path: GRI_1
classification_stability: stable
confidence: high
ruling_override_applied: false
pre_gri_exclusion: Section_XVII_Note_2f
source_pta_files:
  - pta/battery-control-unit-(bcu)_us.md
  - pta/battery-control-unit-(bcu)_eu.md
  - pta/battery-control-unit-(bcu)_india.md
source_da_file: da/da_memo_tb1_remaining.md
extraction_timestamp: "2026-04-01T00:00:00Z"
---

## Classification Summary

The Battery Control Unit (BCU) classifies at heading [[hs_code-8537-10-global]] across all three jurisdictions. The BCU is a centralized PCBA that integrates protection ICs, cell-balancing circuits, and microcontrollers executing battery management firmware. It is a dedicated control board meeting the heading 8537.10 two-or-more-apparatus threshold.

- **US**: 8537.10.91 — dedicated control board, ≤1,000V
- **EU**: 8537.10.91 — programmable memory controllers (BCU executes programmable firmware)
- **India**: 8537.10.00 — single 8-digit entry (voltage ≤1,000V)

Stability is **stable**. Classification of standalone BMS-hierarchy PCBAs at 8537.10 is consistent across all three jurisdictions and well-supported by primary tariff text and DA corroboration.

---

## Pre-GRI Filter Results

| Filter | Applied | Result |
|--------|---------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — electrical control apparatus is Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | PCBA is not a part of general use |
| Chapter 90 Note 2 | No | ACTIVE_CONTROL — measurement serves control; Chapter 90 not applicable |
| Chapter 84 Note 5(E) | **Yes** | Dedicated controller excluded from heading 8471 |

---

## GRI Cascade: 8507 vs 8537 Determination

**Chapter 84 Note 5(E) applies before GRI 1.** The BCU is a dedicated controller — not a general-purpose ADP machine. Heading 8471 is excluded.

**Resolved at GRI 1.** Heading [[hs_code-8537-10-global]] covers boards equipped with two or more apparatus of headings 8535/8536 for electric control. The BCU carries protection devices (8536 class) and cell-balancing switches (8536 class) — threshold met. GRI 1 is determinative.

**8507 (storage batteries) considered and rejected**: CBP HQ H155376 classified a battery pack (BMS + cells + housing) as 8507.80. The BCU is not a battery pack. A standalone BCU PCBA without battery cells is not a storage battery under any interpretation. EN 85.07 composite rule does not apply.

---

## Reconciliation: PTA vs DA

PTA: 8537.10.91 (US/EU), 8537.10.00 (India) — from [[battery-control-unit-(bcu)_us]], [[battery-control-unit-(bcu)_eu]], [[battery-control-unit-(bcu)_india]].
DA (DA-003-F1 [[da_memo_tb1_remaining]]): Corroborates 8537.10 for all BMS hierarchy components. No conflicting ruling in corpus.

No conflict. Ruling override not triggered.

---

## EU Subheading Note: 8537.10.91 vs 8537.10.98

Same distinction as VCU (TB-4 batch): EU CN 8537.10.91 (programmable memory controllers) is preferred for the BCU because it executes programmable battery management firmware on its microcontrollers. If EU customs authorities consider the BCU primarily as a protection board rather than a programmable memory controller, 8537.10.98 would apply. Heading-level classification is unchanged in either case.

## Graph Links

- `classification_node` → [[product_component-battery-control-unit-bcu]]
- `engineering_anchor` → [[battery-control-unit-(bcu)]]
- `parent_component` → [[battery-management-system-(bms)]]
- `global_anchor` → [[hs_code-8537-10-global]]
- `classified_as` → [[hs_code-8537-10-91-us]]
- `classified_as` → [[hs_code-8537-10-00-in]]
- `classified_as` → [[hs_code-8537-10-91-eu]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
