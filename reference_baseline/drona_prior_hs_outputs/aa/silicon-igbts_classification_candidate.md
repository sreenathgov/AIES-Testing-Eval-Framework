---
agent: AA
component: Silicon IGBTs
entity_id: ent_210
batch: TB-1
jurisdictions: [US, EU, India]
hs_code_us: "8541.29.00"
hs_code_eu: "8541.29.00"
hs_code_india: "8541.29.90"
jurisdiction_divergence: false
gri_path: GRI_1
classification_stability: stable
confidence: high
ruling_override_applied: false
pre_gri_exclusion: Section_XVII_Note_2f
source_pta_files:
  - pta/silicon-igbts_us.md
  - pta/silicon-igbts_eu.md
  - pta/silicon-igbts_india.md
source_da_file: da/da_memo_tb1_remaining.md
extraction_timestamp: "2026-04-01T00:00:00Z"
---

## Classification Summary

Silicon IGBTs (Insulated Gate Bipolar Transistors) classify at heading 8541.29 across all three jurisdictions. Identical heading and subheading to SiC MOSFETs. The IGBT is a transistor-class semiconductor device; substrate material (Si vs SiC) does not create a tariff distinction.

- **US**: 8541.29.00
- **EU**: 8541.29.00
- **India**: 8541.29.90 (not ADP/telecom type)

Stability is **stable**.

---

## Pre-GRI Filter Results

| Filter | Applied | Result |
|--------|---------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Switching device |

---

## GRI Cascade

**Resolved at GRI 1.** Same analysis as SiC MOSFETs. IGBT is a transistor. Dissipation capacity ≥ 1W (EV power device). 8541.29 is determinative.

**SiC MOSFET vs Silicon IGBT**: Both are power transistors, both are discrete semiconductor devices, both are traded as components for traction inverter module assembly. No tariff distinction exists between them at the heading or subheading level. AA confirms identical classification.

---

## Reconciliation: PTA vs DA

PTA: Identical to SiC MOSFET analysis. DA-003-F2 ([[da_memo_tb1_remaining]]): Confirms 8541.29; India 8541.29.90. No conflict.

## Graph Links

- `classification_node` → [[product_component-silicon-igbts]]
- `engineering_anchor` → [[silicon-igbts]]
- `parent_component` → [[traction-inverter-module]]
- `global_anchor` → [[hs_code-8541-29-global]]
- `classified_as` → [[hs_code-8541-29-us]]
- `classified_as` → [[hs_code-8541-29-eu]]
- `classified_as` → [[hs_code-8541-29-in]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
