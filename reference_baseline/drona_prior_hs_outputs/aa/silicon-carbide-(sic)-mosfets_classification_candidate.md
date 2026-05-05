---
agent: AA
component: Silicon Carbide (SiC) MOSFETs
entity_id: ent_209
batch: TB-1
jurisdictions:
  - US
  - EU
  - India
hs_code_us: 8541.29.00
hs_code_eu: 8541.29.00
hs_code_india: 8541.29.90
jurisdiction_divergence: false
gri_path: GRI_1
classification_stability: stable
confidence: high
ruling_override_applied: false
pre_gri_exclusion: Section_XVII_Note_2f
source_pta_files:
  - pta/silicon-carbide-(sic)-mosfets_us.md
  - pta/silicon-carbide-(sic)-mosfets_eu.md
  - pta/silicon-carbide-(sic)-mosfets_india.md
source_da_file: da/da_memo_tb1_remaining.md
extraction_timestamp: 2026-04-01T00:00:00Z
---

## Classification Summary

Silicon Carbide (SiC) MOSFETs classify at heading 8541.29 across all three jurisdictions. The SiC MOSFET is a power transistor-class semiconductor device with dissipation capacity far exceeding 1W. Heading 8541 is the specific provision for transistors and semiconductor devices.

- **US**: 8541.29.00 — other transistors (dissipation ≥ 1W)
- **EU**: 8541.29.00 — other transistors (dissipation ≥ 1W)
- **India**: 8541.29.90 — other transistors, not ADP/telecom type (power transistors for EV use)

The India subheading variation (8541.29.90 vs 8541.29.00 for US/EU) reflects India's ITC-HS subdivision distinguishing ADP/telecom transistors from other power transistors. This is a statistical subheading variation, not a heading-level divergence. `jurisdiction_divergence: false`.

Stability is **stable**.

---

## Pre-GRI Filter Results

| Filter | Applied | Result |
|--------|---------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — Chapter 85; Chapter 87 vetoed (SiC MOSFETs are components of EV traction inverter but Section XVII Note 2(f) routes them to Chapter 85 as semiconductor devices) |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Switching device; not a measuring instrument |

---

## GRI Cascade

**Resolved at GRI 1.** Heading 8541 explicitly covers transistors and similar semiconductor devices. A SiC MOSFET is unambiguously a transistor-class semiconductor device.

**Subheading distinction**: 8541.21 (dissipation < 1W) vs 8541.29 (dissipation ≥ 1W). SiC power transistors for EV traction inverters operate at 100–600A, 400–800V — dissipation capacity is kiloWatt-scale. 8541.29 is unambiguous.

**Discrete device vs. part of inverter**: Section XVI Note 2(b) states that goods of Chapters 84–85 are classified in their own heading even when identifiable as parts of other machines. SiC MOSFETs traded as discrete semiconductor devices are classified at 8541 regardless of their end use in traction inverters.

---

## Reconciliation: PTA vs DA

PTA: 8541.29.00 (US/EU), 8541.29.90 (India). DA-003-F2 ([[da_memo_tb1_remaining]]): Confirms 8541.29 across all jurisdictions; confirms India 8541.29.90 for power transistors not of ADP/telecom type.

No conflict. Ruling override not triggered.

## Graph Links

- `classification_node` → [[product_component-silicon-carbide-sic-mosfets]]
- `engineering_anchor` → [[silicon-carbide-(sic)-mosfets]]
- `parent_component` → [[traction-inverter-module]]
- `global_anchor` → [[hs_code-8541-29-global]]
- `classified_as` → [[hs_code-8541-29-us]]
- `classified_as` → [[hs_code-8541-29-eu]]
- `classified_as` → [[hs_code-8541-29-in]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
