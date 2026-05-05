---
agent: AA
component: DC-DC Converter
entity_id: ent_216
pilot_batch: TB-1
hs_code_us: "8504.40"
hs_code_eu: "8504.40.90"
hs_code_eu_resolution_basis: "Exact-match: Commission Implementing Regulation (EU) No 1110/2012 (DC→DC converter = 8504.40.90); Swedish National Board of Trade (Kommerskollegium) explicitly maps EV DC-DC converters to ex 8504.40.90. Code 8504.40.84 ('Inverters') is excluded — DC→DC performs no AC conversion."
hs_code_eu_gap_status: "D2-GAP-014 closed"
refinement_date: "2026-04-06"
hs_code_india: "8504.40.90"
india_correction_note: "Corrected consistency pass: India ITC-HS 8504.40 subdivides into .10 (electric inverter, DC→AC) and .90 (other). DC-DC is DC→DC, not a DC→AC inverter → 8504.40.90. Code 8504.40.00 was pre-CAAR Valco (TB-2 corpus). Confirmed by CAAR Valco ruling and Combo Unit TB-2 analysis."
gri_path: GRI_1
gri_3b_triggered: false
stability: stable
confidence: high
jurisdiction_divergence: false
ruling_override_applied: false
---

## Classification Summary

**All three jurisdictions: 8504.40 — Static converters**

Unambiguous. "Static converters" is the subheading, and DC-DC conversion is exactly what static converters do. Section XVII Note 2(f) routes to Chapter 85. No competing headings. No ruling conflicts.

---

## Pre-GRI Filter Results

| Filter | Result |
|--------|--------|
| Section XVII Note 2(f) | **FIRED** — static converter (power electronics) is Chapter 85 apparatus; Chapter 87 vetoed |
| Section XV Note 2 | Not applicable |
| Chapter 90 Note 2 | Not applicable |

---

## GRI Analysis

**Resolved at GRI 1.** Heading 8504 covers "electrical transformers, static converters (for example, rectifiers) and inductors." DC-DC Converter = static converter. No competing headings after Chapter 87 veto.

---

## Jurisdictional Classifications

### United States
- **Code**: 8504.40
- **Source**: `pta/dc-dc-converter_us.md`

### European Union
- **Code**: 8504.40.90
- **Basis**: Exact-match: Commission Implementing Regulation (EU) No 1110/2012 — DC→DC converter = 8504.40.90. Swedish National Board of Trade (Kommerskollegium) explicitly maps EV DC/DC converters to ex 8504.40.90. Code 8504.40.84 ('Inverters') excluded — DC→DC performs no AC conversion (D2-GAP-014 closed).
- **Source**: `pta/dc-dc-converter_eu.md`

### India (ITC-HS)
- **Code**: 8504.40.00
- **Source**: `pta/dc-dc-converter_india.md`

---

## Reconciliation Notes

Straightforward. No conflicts across PTA, PRA, DA. DA Memo DA-001-F4 corroborates. Same heading as OBC (8504.40) but different component — DC-DC converts DC→DC; OBC converts AC→DC (rectifier). Both are static converters; both correctly classify at 8504.40.

## Graph Links

- `classification_node` → [[product_component-dc-dc-converter]]
- `engineering_anchor` → [[dc-dc-converter]]
- `parent_component` → [[integrated-e-axle]]
- `global_anchor` → [[hs_code-8504-40-global]]
- `classified_as` → [[hs_code-8504-40-us]]
- `classified_as` → [[hs_code-8504-40-00-in]]
- `candidate_code` → [[hs_code-8504-40-84-eu]]
- `candidate_code` → [[hs_code-8504-40-90-eu]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
