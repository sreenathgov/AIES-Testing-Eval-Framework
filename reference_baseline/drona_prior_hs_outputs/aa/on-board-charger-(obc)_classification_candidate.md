---
agent: AA
component: On-Board Charger (OBC)
entity_id: ent_215
pilot_batch: TB-1
hs_code_us: "8504.40"
hs_code_eu: "8504.40.90"
hs_code_eu_resolution_basis: "Exact-match: Swedish National Board of Trade (Kommerskollegium) maps 'On-board charger with/without DC-DC converter' to ex 8504.40.90. EU Comitology Register: static conversion is the principal function (Section XVI Note 3). Code 8504.40.84 ('Inverters') excluded — OBC performs AC→DC rectification, not DC→AC inversion."
hs_code_eu_gap_status: "D2-GAP-015 closed"
refinement_date: "2026-04-06"
hs_code_india: "8504.40.90"
india_correction_note: "Corrected consistency pass: India ITC-HS 8504.40 subdivides into .10 (electric inverter, DC→AC) and .90 (other). OBC is AC→DC, not a DC→AC inverter → 8504.40.90. Code 8504.40.00 was pre-CAAR Valco (TB-2 corpus). Confirmed by CAAR Valco ruling and Combo Unit TB-2 analysis."
gri_path: GRI_1
gri_3b_triggered: false
stability: stable
confidence: high
jurisdiction_divergence: false
ruling_override_applied: false
---

## Classification Summary

**All three jurisdictions: 8504.40 — Static converters**

OBC is a rectifier (AC grid power → DC for battery charging). Heading 8504 explicitly names rectifiers as examples of static converters. Unambiguous classification.

---

## Pre-GRI Filter Results

| Filter | Result |
|--------|--------|
| Section XVII Note 2(f) | **FIRED** — rectifier/power electronics is Chapter 85 apparatus; Chapter 87 vetoed |
| Section XV Note 2 | Not applicable |
| Chapter 90 Note 2 | Not applicable |

---

## GRI Analysis

**Resolved at GRI 1.** Heading 8504: "Electrical transformers, static converters *(for example, rectifiers)* and inductors." Rectifiers are explicitly named. OBC = rectifier = static converter.

> **Note on potential confusion with 8507.90 (battery charger parts)**: OBC's primary function is AC-to-DC energy conversion (rectification), not charging as an isolated operation. The OBC *enables* charging by converting power; the battery is the charging target. OBC correctly classifies as the conversion apparatus (8504), not a battery accessory (8507).

---

## Jurisdictional Classifications

### United States
- **Code**: 8504.40
- **Source**: `pta/on-board-charger-(obc)_us.md`

### European Union
- **Code**: 8504.40.90
- **Basis**: Exact-match: Swedish National Board of Trade maps OBC (with and without DC-DC) to ex 8504.40.90. EU Comitology Register — static conversion is principal function (Section XVI Note 3). 8504.40.84 ('Inverters') excluded — OBC performs AC→DC, not DC→AC (D2-GAP-015 closed).
- **Source**: `pta/on-board-charger-(obc)_eu.md`

### India (ITC-HS)
- **Code**: 8504.40.00
- **Source**: `pta/on-board-charger-(obc)_india.md`

---

## Reconciliation Notes

Clean classification. Same heading as DC-DC Converter (8504.40) — both are static converters, different physical products. DA Memo DA-001-F5 corroborates and confirms rectifier framing over the 8507.90 alternative. No conflicts.

## Graph Links

- `classification_node` → [[product_component-on-board-charger-obc]]
- `engineering_anchor` → [[on-board-charger-(obc)]]
- `parent_component` → [[integrated-e-axle]]
- `global_anchor` → [[hs_code-8504-40-global]]
- `classified_as` → [[hs_code-8504-40-us]]
- `classified_as` → [[hs_code-8504-40-00-in]]
- `candidate_code` → [[hs_code-8504-40-84-eu]]
- `candidate_code` → [[hs_code-8504-40-90-eu]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
