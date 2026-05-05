---
agent: PTA
component: Battery Management System (BMS)
entity_id: ent_217
jurisdiction: India
fundamental_function: ACTIVE_CONTROL
is_composite_flagged: false
hs_code_candidate: "8537.10"
india_itc_hs_subheading: "8537.10.00"
gri_path: GRI_1
stability: stable
confidence: high
confidence_note: CESTAT BCM does not apply to a BMS and the WS-6 refinement corroborated 8537.10.00 using India-specific and cross-jurisdiction authority
source_doc: cbic_schedule_of_tariff_commitment_ev_complex.md
source_section: Heading 8537 — boards and panels for electric control
ruling_flag: "CESTAT Chennai 40800/2025: BCM/IBU → CTH 9032.89.10. BCM controls body functions; BMS controls cell chemistry. BCM ≠ BMS — override rejected in WS-6 refinement."
pilot_batch: TB-1
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — control apparatus is Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | Not applicable |
| Chapter 90 Note 2 | No | NOT APPLICABLE — BMS controls cell-balancing switches and thermal management, not purely measuring |

## GRI Analysis

**Resolved at GRI 1.** India ITC-HS heading 8537.10 for boards/panels for electric control ≤1,000V. India has no dedicated ITC-HS 8-digit code for BMS (unlike traction motor which has 85015330). Standard 8537.10.00 applies.

### CESTAT BCM Ruling Distinction

CESTAT Chennai 40800/2025 classified BCM/IBU at CTH 9032.89.10. BCM (Body Control Module) controls **vehicle body functions** (wipers, climate, headlamps) — categorically different from BMS (Battery Management System) which controls **cell chemistry, balancing, and protection**.

The CESTAT BCM ruling does not apply to BMS.

## Classification

- **Code**: 8537.10.00
- **Subheading text**: Boards, panels for electric control — for a voltage not exceeding 1,000V
- **Heading text**: Boards, panels equipped with apparatus of 8535/8536 for electric control
