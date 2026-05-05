---
agent: AA
component: Traction Inverter Module
entity_id: ent_196
batch: TB-4
jurisdictions: [US, EU, India]
hs_code_us: "8504.40.40"
hs_code_eu: "8504.40.87"
hs_code_india: "8504.40.10"
jurisdiction_divergence: false
gri_path: GRI_1
classification_stability: stable
confidence: high
ruling_override_applied: false
pre_gri_exclusion: Section_XVII_Note_2f
source_pta_files:
  - pta/traction-inverter-module_us.md
  - pta/traction-inverter-module_eu.md
  - pta/traction-inverter-module_india.md
source_da_file: da/da_memo_tb4_remaining.md
extraction_timestamp: "2026-04-01T00:00:00Z"
---

## Classification Summary

The Traction Inverter Module classifies at heading 8504.40 (static converters) across all three jurisdictions. Subheading variation reflects each jurisdiction's distinct 8-digit structure:

- **US**: 8504.40.40 — Speed drive controllers for electric motors (most specific US subheading for a variable-frequency inverter controlling traction motor speed)
- **EU**: 8504.40.87 — Other static converters, other (residual for non-charger, non-MPPT inverters)
- **India**: 8504.40.10 — Electric inverter (India's dedicated subheading for inverters eliminates ambiguity)

Stability is **stable**. The classification of traction inverters at 8504.40 is well-settled across all three jurisdictions, supported by both primary tariff text and consistent secondary source corroboration.

---

## Pre-GRI Filter Results

| Filter | Applied | Result |
|--------|---------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — DC/AC power conversion is electrical machinery; Chapter 87 vetoed; confined to Chapter 85 |
| Section XV Note 2 | No | SiC/IGBT semiconductor assembly is not a part of general use |
| Chapter 90 Note 2 | No | Not a measuring instrument |

Section XVII Note 2(f) was decisive: even though the traction inverter is an integral part of the EV powertrain, it is electrical machinery (performs DC→AC static conversion) and must be classified in Chapter 85, NOT Chapter 87 (vehicle parts/accessories).

---

## GRI Cascade

**Resolved at GRI 1.** Heading 8504 explicitly covers "static converters (for example, rectifiers)" — the parenthetical examples are illustrative, not limiting. A traction inverter converts DC battery current to variable-frequency AC: this is static conversion by definition (no moving parts; uses switching semiconductors). GRI 1 is determinative without invoking GRI 2, 3, or beyond.

---

## Reconciliation: PTA vs DA

PTA (all three jurisdictions): 8504.40 confirmed from primary tariff text.
DA (DA-002-F1): Corroborates 8504.40 across all secondary sources. India's 85044010 dedicated subheading noted as strong positive confirmation.

No conflict between PTA and DA. Ruling override framework not triggered (no contested ruling on traction inverters in the corpus).

---

## Jurisdiction-Specific Notes

**US — 8504.40.40 vs 8504.40.95**

US subheading 8504.40.40 "Speed drive controllers for electric motors" is the most specific description for a traction inverter: it produces variable-frequency, variable-amplitude AC specifically to control traction motor speed and torque. 8504.40.95 (Other) is the residual. The 8504.40.40 determination has precedent in CBP classification of industrial variable frequency drives (VFDs) and is the appropriate US subheading.

**EU — 8504.40.87**

The EU CN does not have a dedicated VFD/inverter subheading equivalent to the US 8504.40.40. 8504.40.87 (other static converters, other) is the correct residual after excluding accumulator chargers (8504.40.60) and MPPT converters (8504.40.84). The EU 2025/1926 Regulation does not create a specific CN code for traction inverters.

**India — 8504.40.10**

India's dedicated "Electric inverter" subheading (85044010) is the clearest jurisdiction-level classification in this batch. Classification certainty is highest for India.

## Graph Links

- `classification_node` → [[product_component-traction-inverter-module]]
- `engineering_anchor` → [[traction-inverter-module]]
- `parent_component` → [[power-electronics]]
- `global_anchor` → [[hs_code-8504-40-global]]
- `classified_as` → [[hs_code-8504-40-40-us]]
- `classified_as` → [[hs_code-8504-40-10-in]]
- `classified_as` → [[hs_code-8504-40-87-eu]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
