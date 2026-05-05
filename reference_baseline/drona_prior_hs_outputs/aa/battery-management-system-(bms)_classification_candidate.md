---
agent: AA
component: Battery Management System (BMS)
entity_id: ent_217
pilot_batch: TB-1
hs_code_us: "8537.10"
hs_code_eu: "8537.10"
hs_code_india: "8537.10"
india_itc_hs: "8537.10.00"
gri_path: GRI_1
gri_3b_triggered: false
stability: stable
confidence: high
jurisdiction_divergence: false
ruling_override_applied: false
ruling_override_rejected: CBP HQ H155376 (fails condition 2 — different physical product)
refinement_status: resolved_ws6
refinement_date: "2026-04-06"
refinement_source: "drona/parsed/02_hs_classification/Targeted Research/HS - DR - DRONA Refinement_ BMS & HV Contactor.md"
---

## Classification Summary

**All three jurisdictions: 8537.10 — Boards and panels for electric control, ≤1,000V**

This is the pilot's most contested classification. Two positions exist in trade practice:

| Position | Code | Basis |
|----------|------|-------|
| **PTA (adopted)** | 8537.10 | GRI 1 — standalone BMS PCBA = assembly of control apparatus |
| **Trade practice pressure** | 8507.80 | CBP H155376 — battery pack composite good analysis |

AA conclusion: **8537.10 is correct for a standalone BMS PCBA.** CBP H155376 addressed a different physical product (battery pack with cells). Override rejected. See analysis below.

---

## Pre-GRI Filter Results

| Filter | Result |
|--------|--------|
| Section XVII Note 2(f) | **FIRED** — control apparatus is Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | Not applicable |
| Chapter 90 Note 2 | **NOT APPLICABLE** — BMS fundamental function = ACTIVE_CONTROL (switching, balancing, protection). BMS acts on measurements rather than purely measuring. Distinguished from BCM (body controller → Ch 90) by domain: cell chemistry vs cabin body functions. |

---

## GRI Analysis

**Resolved at GRI 1.** Heading 8537 covers boards and panels equipped with two or more apparatus of heading 8535 or 8536, for electric control. A standalone BMS PCBA is an assembly of:
- Cell-balancing MOSFETs/switches (8536 class)
- Overcurrent protection devices (8535 class)
- Monitoring and control microcontrollers

This is electric control apparatus. Heading 8537.10 applies directly.

### Competing heading: 8507 (storage batteries)

EN 85.07 states that batteries presented with ancillary protective/monitoring circuits are classifiable as batteries (composite good, GRI 3(b), essential character = battery cells). This is the basis for CBP H155376.

**However**: This reasoning applies only when BMS circuits are presented **together with battery cells** as a combined article. A standalone BMS PCBA without battery cells is not a storage battery and falls outside the EN 85.07 composite good rule.

---

## Ruling Override Analysis

### CBP HQ H155376 (US, June 22 2011)

| Override Condition | Result |
|-------------------|--------|
| 1. Same jurisdiction (US) | ✓ Yes |
| 2. Same physical product | ✗ **No** |
| 3. More specific than tariff text | N/A — condition 2 failed |
| 4. Recent, not superseded | N/A — condition 2 failed |

**Condition 2 analysis**: H155376 classified a *battery pack* — lithium-ion cells + PCBAs + housing as a composite good. Pilot entity ent_217 is a standalone BMS PCBA ("Printed circuit board assembly with monitoring ICs, microcontrollers, cell-balancing circuits, communication interfaces"). Different physical product.

**Override rejected. 8537.10 stands for US.**

---

### CESTAT Chennai 40800/2025 (India, August 7 2025)

| Override Condition | Result |
|-------------------|--------|
| 1. Same jurisdiction (India) | ✓ Yes |
| 2. Same physical product | ✗ **No** |

**Condition 2 analysis**: CESTAT classified a *Body Control Module (BCM)* — controls vehicle body functions: windshield wipers, climate control, headlamps, interior lighting. **BCM ≠ BMS.** BMS controls battery cell chemistry, balancing, and protection. Entirely different component and control domain.

**Override rejected. 8537.10 stands for India.**

---

## Jurisdictional Classifications

### United States
- **Code**: 8537.10
- **Stability**: stable
- **Confidence**: high
- **Basis**: GRI 1; 8504 exclusionary wall confirmed (CBP HQ H176833); CBP H155376 override rejected (different physical product — battery pack, not standalone PCBA)
- **Residual risk note**: If a BMS is ever imported *with battery cells as a combined article*, reclassify via GRI 3(b) → 8507.xx. Standalone BMS PCBA: 8537.10 stable/high.
- **Source**: `pta/battery-management-system-(bms)_us.md`

### European Union
- **Code**: 8537.10.91 (8-digit — programmable memory type; confirm against product spec for 8537.10.99)
- **Stability**: stable
- **Confidence**: high
- **Basis**: EU CN heading 8537.10; same GRI 1 analysis as US; no EU BTI ruling applicable to standalone BMS PCBA. 8504 route excluded.
- **Source**: `pta/battery-management-system-(bms)_eu.md`

### India (ITC-HS)
- **Code**: 8537.10.00
- **Stability**: stable
- **Confidence**: high
- **Basis**: GRI 1; Section XVII Note 2(f) vetoes Chapter 87; CAAR Valeo by-contrast corroboration (BMS = physical electrical execution apparatus, not digital signal processor); CESTAT BCM (9032) ruling not applicable — BCM ≠ BMS.
- **Source**: `pta/battery-management-system-(bms)_india.md`

---

## WS-6 Refinement Resolution (D2-GAP-011 — Closed 2026-04-06)

**Status upgraded: contested/medium → stable/high**

Post-domain refinement Workstream WS-6 applied multi-jurisdictional legal corroboration:

**8504 exclusionary wall confirmed:** CBP HQ H176833 + H249299 establish that standalone BMS PCBAs are power-control apparatus (gates/switches traction current), not power-conversion apparatus (no inductive coils, no AC rectification). Heading 8504 permanently quarantined.

**9032 threat neutralized via GRI 3(b):** USTR Federal Register 9032.89.4000 carve-out applies strictly to isolated battery balancers. A standalone BMS incorporating cell-balancing as a subordinate function has essential character of electric control/distribution apparatus (macro-level switching + safety relay control + pre-charge circuit management). GRI 3(b) → 8537.10.

**India CAAR Valeo corroboration (CAAR/Mum/ARC/05/2025-26):** By ruling that the VCU = 8708.99.00 because it only processes digital signals, the CAAR defined the BMS by contrast — the BMS is the apparatus that physically executes the electrical control the VCU commands. Section XVII Note 2(f) permanently quarantines BMS in Chapter 85.

**Retained risk note:** If a BMS is ever imported *with battery cells as a combined article*, reclassify via GRI 3(b) → 8507.xx. Standalone BMS PCBA: 8537.10 stable/high.

---

## Reconciliation Notes

Tariff text (8537.10) is clear for standalone BMS. Both rulings fail the override conditions. DA Memo DA-002 pre-documented the four-condition framework result. WS-6 refinement (2026-04-06) upgraded confidence from medium to high via legal corroboration: CBP HQ H176833, CAAR Valeo India, USTR 9032.89.4000 carve-out analysis. Classification: 8537.10, **stable, high confidence**.

## Graph Links

- `classification_node` → [[product_component-battery-management-system-bms]]
- `engineering_anchor` → [[battery-management-system-(bms)]]
- `parent_component` → [[energy-storage-subsystem]]
- `global_anchor` → [[hs_code-8537-10-global]]
- `classified_as` → [[hs_code-8537-10-us]]
- `classified_as` → [[hs_code-8537-10-00-in]]
- `candidate_code` → [[hs_code-8537-10-91-eu]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
