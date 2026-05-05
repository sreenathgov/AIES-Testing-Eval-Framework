---
agent: AA
component: Cell Supervisor Unit (CSU)
entity_id: ent_170
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
  - pta/cell-supervisor-unit-(csu)_us.md
  - pta/cell-supervisor-unit-(csu)_eu.md
  - pta/cell-supervisor-unit-(csu)_india.md
source_da_file: da/da_memo_tb1_remaining.md
extraction_timestamp: "2026-04-01T00:00:00Z"
---

## Classification Summary

The Cell Supervisor Unit (CSU) classifies at heading [[hs_code-8537-10-global]] across all three jurisdictions. The CSU is a distributed PCBA with AFE ICs, cell-balancing switches, and isolation transceivers. It executes programmable cell-balancing and fault-detection algorithms.

- **US**: 8537.10.91 — dedicated control board
- **EU**: 8537.10.91 — programmable memory controllers (CSU executes programmable balancing firmware)
- **India**: 8537.10.00 — single 8-digit entry

Stability is **stable**.

---

## Pre-GRI Filter Results

| Filter | Applied | Result |
|--------|---------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | **Critical analysis** — NOT fired. The CSU measures cell voltages and temperatures but its output is control signals for balancing and protection. Measurement is ancillary input to ACTIVE_CONTROL. WCO EN 90.XX excludes active control apparatus from Chapter 90. Chapter 85 governs. |

---

## GRI Cascade: Chapter 90 Note 2 Deep Analysis

**Chapter 90 Note 2** states that goods of Chapter 90 (measuring/testing instruments) are not classified in Chapters 84/85 if they are more specifically described in Chapter 90. The CSU acquires cell voltage and temperature readings, which could superficially suggest Chapter 90 (instruments for measuring electrical quantities).

However:
1. The CSU does not output measurement data to a user or system — it inputs data to its own control algorithms
2. The CSU's primary output is a balancing drive signal and fault escalation signal to the BCU
3. Heading 9030 (instruments for measuring electrical quantities) covers standalone measurement articles; the CSU is not used to measure — it uses measurement to control
4. WCO EN Note to Chapter 90: "This Chapter does not cover... apparatus of heading 8537 which incorporate measuring functions as ancillary elements"

Chapter 90 Note 2 does not route the CSU to Chapter 90. Heading [[hs_code-8537-10-global]] governs.

---

## Reconciliation: PTA vs DA

PTA: 8537.10.91 (US/EU), 8537.10.00 (India). DA-003-F1 ([[da_memo_tb1_remaining]]): Corroborates Chapter 90 Note 2 analysis; no conflicting ruling.

No conflict. Ruling override not triggered.

## Graph Links

- `classification_node` → [[product_component-cell-supervisor-unit-csu]]
- `engineering_anchor` → [[cell-supervisor-unit-(csu)]]
- `parent_component` → [[battery-management-system-(bms)]]
- `global_anchor` → [[hs_code-8537-10-global]]
- `classified_as` → [[hs_code-8537-10-91-us]]
- `classified_as` → [[hs_code-8537-10-91-eu]]
- `classified_as` → [[hs_code-8537-10-00-in]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
