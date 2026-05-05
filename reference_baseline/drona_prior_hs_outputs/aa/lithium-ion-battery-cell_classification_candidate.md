---
agent: AA
component: Lithium-Ion Battery Cell
entity_id: ent_147
pilot_batch: TB-4
hs_code_us: "8507.60"
hs_code_eu: "8507.60"
hs_code_india: "8507.60"
india_itc_hs: "8507.60.00"
gri_path: GRI_1
gri_3b_triggered: false
stability: stable
confidence: high
jurisdiction_divergence: false
ruling_override_applied: false
---

## Classification Summary

**All three jurisdictions: 8507.60 — Lithium-ion electric accumulators**

The most settled classification in the EV space. Section XVII Note 2(f) fires, confirming Chapter 85. Heading 8507.60 directly and unambiguously describes lithium-ion cells.

---

## Pre-GRI Filter Results

| Filter | Result |
|--------|--------|
| Section XVII Note 2(f) | **FIRED** — confirms Chapter 85 across all jurisdictions |
| Section XV Note 2 | Not applicable |
| Chapter 90 Note 2 | Not applicable |

---

## GRI Analysis

**Resolved at GRI 1.** Heading 8507.60 explicitly covers lithium-ion accumulators. No competing headings at the same level of specificity. Classification complete without requiring GRI 2–6.

> **Note on taxonomy_handoff flag**: `gri_3_required: true` was flagged for ent_147. AA analysis: the entity is a *standalone cell*, not a composite article. A single lithium-ion cell is directly described by 8507.60. GRI 3(b) is not triggered for standalone cells — the flag prompted the analysis, which resolved cleanly.

---

## Jurisdictional Classifications

### United States
- **Code**: 8507.60.00
- **Heading**: Electric accumulators — lithium-ion
- **Source**: `pta/lithium-ion-battery-cell_us.md`

### European Union
- **Code**: 8507.60.00
- **Heading**: Electric accumulators — lithium-ion
- **Source**: `pta/lithium-ion-battery-cell_eu.md`

### India (ITC-HS)
- **Code**: 8507.60.00
- **Heading**: Electric accumulators — lithium-ion
- **Source**: `pta/lithium-ion-battery-cell_india.md`

---

## Ruling Corroboration

CBP HQ H155376 (US) classified a battery pack (cells + BMS PCBA + housing) at 8507.80.80. This is consistent with 8507 for battery articles. No conflict — the ruling addressed a composite pack, not a standalone cell.

---

## Reconciliation Notes

PTA, PRA, and DA all converge on 8507.60 without conflict. No ruling override required. Classification complete.

## Graph Links

- `classification_node` → [[product_component-lithium-ion-battery-cell]]
- `engineering_anchor` → [[lithium-ion-battery-cell]]
- `global_anchor` → [[hs_code-8507-60-global]]
- `classified_as` → [[hs_code-8507-60-00-us]]
- `classified_as` → [[hs_code-8507-60-00-in]]
- `classified_as` → [[hs_code-8507-60-00-eu]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
