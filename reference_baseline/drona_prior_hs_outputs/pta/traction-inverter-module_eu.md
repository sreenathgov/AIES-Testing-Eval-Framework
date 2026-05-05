---
agent: PTA
component: Traction Inverter Module
entity_id: ent_196
jurisdiction: EU
fundamental_function: ENERGY_CONVERSION
is_composite_flagged: false
hs_code_candidate: "8504.40"
eu_cn_subheading: "8504.40.87"
gri_path: GRI_1
stability: stable
confidence: high
source_doc: eu_hs_commission_implementing_regulation_(eu)_2025_1926_evs.md
source_section: CN heading 8504.40 — Static converters; subheading 8504.40.87 — Other (not accumulator chargers, not MPPT)
pilot_batch: TB-4
---

## Exclusion Checks

| Check | Fired | Result |
|-------|-------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — DC/AC conversion is electrical machinery (Chapter 85); Chapter 87 vetoed |
| Section XV Note 2 | No | Not a part of general use |
| Chapter 90 Note 2 | No | Not a measuring instrument |

## GRI Analysis

**Resolved at GRI 1.** EU CN heading 8504.40 covers static converters. A traction inverter converts DC to variable-frequency AC — it is a static converter.

Within 8504.40, the EU CN structure distinguishes:
- 8504.40.60: Accumulator chargers — NO (traction inverter charges nothing)
- 8504.40.84: With maximum power point tracking functionality — NO (MPPT applies to solar inverters)
- 8504.40.87: Other static converters, other — YES (residual for inverters not otherwise specified)
- 8504.40.95: Other — residual catchall

8504.40.87 is the correct EU CN 8-digit subheading for EV traction inverters — non-charging, non-MPPT static converters.

## Classification

- **Code**: 8504.40.87
- **Subheading text**: Static converters — other, other
- **Heading text**: Electrical transformers, static converters (for example, rectifiers) and inductors; parts thereof
