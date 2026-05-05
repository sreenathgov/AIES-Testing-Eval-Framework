---
agent: AA
component: High-Voltage Contactor
entity_id: ent_144
pilot_batch: TB-4
hs_code_us: "8536.49"
hs_code_eu: "8536.49.90"
hs_code_india: "8536.49.00"
gri_path: GRI_1
gri_3b_triggered: false
stability: stable
confidence: high
jurisdiction_divergence: false
ruling_override_applied: false
voltage_confirmed: "≤1,000V — confirmed via TE Connectivity K1K datasheet ('up to 1000V for severe EV environments') and CAAR Valeo India (CAAR/Mum/ARC/05/2025-26) importation manifest ('not exceeding 1000V' for EV relays and contactors)"
heading_confirmed: "8536 (≤1,000V confirmed — heading 8535 excluded)"
open_data_request: null
refinement_status: resolved_ws6
refinement_date: "2026-04-06"
refinement_source: "drona/parsed/02_hs_classification/Targeted Research/HS - DR - DRONA Refinement_ BMS & HV Contactor.md"
---

## Classification Summary

**Confirmed classification — all three jurisdictions: 8536.49.00 — Other relays, for a voltage exceeding 60 V but not exceeding 1,000 V**

Stability is **stable**. Voltage confirmed ≤1,000V via WS-6 refinement (2026-04-06):
- **TE Connectivity K1K datasheet**: rated operating voltage "up to 1000V" for severe EV environments
- **CAAR Valeo India (CAAR/Mum/ARC/05/2025-26) importation manifest**: entity's HV EV relays and contactors declared "not exceeding 1000V"

Heading 8535 (>1,000V) is excluded. Heading 8536.49 is confirmed anchor.

---

## Pre-GRI Filter Results

| Filter | Result |
|--------|--------|
| Section XVII Note 2(f) | **FIRED** — electromagnetic switch is Chapter 85 apparatus; Chapter 87 vetoed |
| Section XV Note 2 | Not applicable |
| Chapter 90 Note 2 | Not applicable |

---

## GRI Analysis

**Resolved at GRI 1.** Section XVII Note 2(f) routes to Chapter 85. Heading 8536 covers electrical apparatus for switching/protecting electrical circuits for ≤1,000V. Subheading 8536.49 covers "other relays" in the 60V–1,000V band — the correct bracket for EV high-voltage contactors on standard 400V/800V architectures.

> **Voltage flag**: EV systems typically operate at 400–800V, within the ≤1,000V ceiling of heading 8536. Emerging 800V+ architectures (some OEM platforms now exceeding 900V) could push contactor operating voltage toward 1,000V boundary. If confirmed >1,000V → heading **8535**.

---

## Jurisdictional Classifications

### United States
- **Code**: 8536.49
- **Heading**: Electrical apparatus for switching/protecting circuits ≤1,000V — other relays, >60V ≤1,000V
- **Source**: `pta/high-voltage-contactor_us.md`

### European Union
- **Code**: 8536.49.90
- **Basis**: EU CN 8536.49.10 covers contactors "for motor starters"; 8536.49.90 covers other. HV EV disconnect/isolation contactors are not motor starters → 8536.49.90. Voltage ≤1,000V confirmed.
- **Source**: `pta/high-voltage-contactor_eu.md`

### India (ITC-HS)
- **Code**: 8536.49.00
- **Source**: `pta/high-voltage-contactor_india.md`

---

## WS-6 Refinement Resolution (D2-GAP-012 — Closed 2026-04-06)

**Voltage confirmed ≤1,000V.** Open data request closed. Heading 8536 confirmed; heading 8535 excluded.

**Evidence:**
- TE Connectivity Kilovac K1K datasheet: "up to 1000V for severe EV environments" (class-level engineering evidence)
- AMP+ / TE Connectivity HVP 1100 and 500-500L contactors: 750V and 900V DC operating thresholds
- CAAR Valeo India CAAR/Mum/ARC/05/2025-26 importation manifest: EV relays and contactors "not exceeding 1000V" (entity-specific evidence)

**EU CN 8-digit:** 8536.49.10 covers contactors "for motor starters"; 8536.49.90 covers other relays/contactors. HV EV contactors functioning as disconnect switches (not motor starters per se) resolve to **8536.49.90**.

---

## Reconciliation Notes

PTA and DA converge on 8536.49. No PRA ruling found for HV contactors in the pilot corpus. No conflicts. WS-6 refinement (2026-04-06) confirmed voltage ≤1,000V via class-level and entity-specific engineering evidence, upgrading stability from fragile to stable and confidence from medium to high. EU CN 8-digit resolved to 8536.49.90.

## Graph Links

- `classification_node` → [[product_component-high-voltage-contactor]]
- `engineering_anchor` → [[high-voltage-contactor]]
- `parent_component` → [[battery-disconnect-unit-(bdu)]]
- `global_anchor` → [[hs_code-8536-49-global]]
- `classified_as` → [[hs_code-8536-49-us]]
- `classified_as` → [[hs_code-8536-49-90-eu]]
- `classified_as` → [[hs_code-8536-49-00-in]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
