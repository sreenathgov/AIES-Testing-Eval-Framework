---
agent: PTA
component: Silicon Carbide (SiC) MOSFETs
entity_id: ent_209
jurisdiction: India
fundamental_function: ACTIVE_CONTROL
material_composition: Silicon Carbide (SiC) semiconductor substrate; power transistor device
is_composite_flagged: false
hs_code_candidate: "8541.29.90"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: cbic_indian_trade_classification_complex.md
source_section: Heading 8541 — semiconductor devices; India ITC-HS 8541.29.90 (Other transistors, not used in ADP machines/telecom, dissipation ≥ 1W)
ruling_flag: "None"
batch: TB-1
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) [[wco_2022_section_87_complex]] | **Yes** | FIRED — Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | Switching device; not a measuring instrument |

## GRI Analysis

**Resolved at GRI 1** per [[cbic_indian_trade_classification_complex]].

Heading 8541 — SiC MOSFET is a transistor-class semiconductor device. GRI 1 is determinative.

**India ITC-HS subheading: 8541.29.10 vs 8541.29.90**

India's ITC-HS subdivides 8541.29 as follows:
- **8541.29.10**: Transistors of a kind used in automatic data-processing machines or in telecommunications apparatus
- **8541.29.90**: Other

SiC MOSFETs for EV traction inverters are **power transistors** used in power conversion applications — not ADP machines or telecommunications apparatus. These are high-voltage, high-current power switches for inverter bridge circuits. They are not of the kind used in ADP/telecom apparatus.

**India code: 8541.29.90** (Other transistors with dissipation ≥ 1W, not ADP/telecom type).

## Classification

- **Heading**: 8541
- **Subheading**: 8541.29.90 — Other transistors (not ADP/telecom type; dissipation ≥ 1W)
- **Code**: 8541.29.90
- **Basis**: GRI 1; SiC power transistors are not ADP/telecom-grade devices; India residual 8541.29.90 applies

## Graph Links

- `classification_node` → [[product_component-silicon-carbide-sic-mosfets]]
- `engineering_anchor` → [[silicon-carbide-(sic)-mosfets]]
- `parent_component` → [[traction-inverter-module]]
- `classified_as` → [[hs_code-8541-29-in]]
- `source_doc` → [[cbic_indian_trade_classification_complex]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
