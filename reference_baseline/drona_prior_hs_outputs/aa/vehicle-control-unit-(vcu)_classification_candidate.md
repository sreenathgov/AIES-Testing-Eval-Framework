---
agent: AA
component: Vehicle Control Unit (VCU)
entity_id: ent_218
batch: TB-4
jurisdictions: [US, EU, India]
hs_code_us: "8537.10.91"
hs_code_eu: "8537.10.91"
hs_code_india: "8537.10.00"
jurisdiction_divergence: false
gri_path: GRI_1
classification_stability_us: stable
classification_stability_eu: stable
classification_stability_india: contested
confidence_us: high
confidence_eu: high
confidence_india: medium
ruling_override_applied: false
caar_conflict_india: "CAAR Valco (India, late 2024) ruled VCU/PCU = 8708.99.00. In personam ruling per Indian Customs Act Section 28-J (binds only the applicant, not all importers); not generally binding precedent. 8537.10.00 maintained as AA conclusion per GRI 1 + Section XVII Note 2(f) analysis."
d_ruling_handoff: true
india_monitor_flag: true
india_monitor_reason: "CAAR Valco VCU/PCU ruling is in personam only — monitor for additional CAAR rulings or court decisions on VCU/ECU that may establish general precedent; Bombay HC BEV axle + VCU/PCU challenges ongoing"
founder_override_provenance: true
founder_override_scope: "missing_primary_text_india_case_law"
founder_override_basis: "ey_pwc_secondary_authority"
founder_override_note: "Founder-approved temporary provenance bridge for missing or incompletely acquired Indian primary text. EY and PwC secondary summaries are accepted for the test run only and must be replaced when the underlying India judgments/orders are acquired."
primary_text_status: "partial"
secondary_authority_sources:
  - {"source": "PwC Customs & Trade Newsletter (Oct 2024)", "citation": "2024-VIL-1345-CESTAT-CHE-CU", "forum": "CESTAT (Chennai)", "date": "2024-10", "holding_summary": "ECU retained under 8537 against a proposed 8708 reclassification because the evidentiary basis for automotive-parts routing was insufficient.", "source_type": "secondary", "source_publisher": "PwC", "primary_text_status": "not_yet_acquired", "applies_to_jurisdictions": ["IN"]}
  - {"source": "PwC Customs & Trade Newsletter / TaxGuru synthesis", "citation": "In re Valeo India Pvt. Ltd. (CAAR Mumbai Ruling No. 07/2025)", "forum": "CAAR (Mumbai)", "date": "2025-04-17", "holding_summary": "VCU/PCU treated as integral automotive parts under Chapter 87, creating a direct India-side conflict against the Chapter 85 control-apparatus route.", "source_type": "secondary", "source_publisher": "PwC", "primary_text_status": "partial", "applies_to_jurisdictions": ["IN"]}
override_applies_to_jurisdictions: [IN]
override_review_required_when_primary_acquired: true
refinement_date: "2026-04-06"
pre_gri_exclusion: Section_XVII_Note_2f
source_pta_files:
  - pta/vehicle-control-unit-(vcu)_us.md
  - pta/vehicle-control-unit-(vcu)_eu.md
  - pta/vehicle-control-unit-(vcu)_india.md
source_da_file: da/da_memo_tb4_remaining.md
extraction_timestamp: "2026-04-01T00:00:00Z"
---

## Classification Summary

The Vehicle Control Unit (VCU) classifies at heading 8537.10 across all three jurisdictions. A VCU is a dedicated programmable microprocessor-based controller for vehicle powertrain management — it is a control board/panel (8537.10), not a general-purpose ADP machine (8471).

- **US**: 8537.10.91 — Other (dedicated controller, excluded from 8471 by Chapter 84 Note 5(E))
- **EU**: 8537.10.91 — Programmable memory controllers (EU CN specifically covers dedicated programmable controllers at this subheading)
- **India**: 8537.10.00 — For a voltage not exceeding 1,000V

Overall stability is **mixed**. The US and EU positions are stable/high, but the India position is contested/medium because CAAR Valco creates a live Chapter 87 conflict against the standing 8537.10.00 analysis.

---

## Pre-GRI Filter Results

| Filter | Applied | Result |
|--------|---------|--------|
| Section XVII Note 2(f) | **Yes** | FIRED — electrical control apparatus is Chapter 85; Chapter 87 vetoed |
| Section XV Note 2 | No | Computational control board with microprocessors is not a part of general use |
| Chapter 90 Note 2 | No | VCU is not a measuring instrument; measurement inputs serve its control function |

---

## GRI Cascade: 8471 vs 8537 Determination

**Chapter 84 Note 5(E) applies before GRI 1.** Chapter 84 Note 5 defines ADP machines (heading 8471) and Note 5(E) excludes "machines incorporating or working in conjunction with an automatic data-processing machine and performing a specific function other than data processing." A VCU:
- Executes firmware algorithms for powertrain control (torque demand, regen braking, thermal management)
- Is not a general-purpose computing device
- Cannot be reprogrammed for functions other than vehicle control
- Has no user-facing computing interface

Note 5(E) exclusion confirmed → heading 8471 is NOT applicable.

**Resolved at GRI 1 at heading 8537.** The VCU is a numerical control apparatus — a dedicated programmable controller equipped with multiple electronic control components. Heading 8537 covers "numerical control apparatus" within its scope. GRI 1 is determinative.

---

## Reconciliation: PTA vs DA

PTA: 8537.10 confirmed across all three jurisdictions, with Chapter 84 Note 5(E) exclusion documented.
DA (DA-002-F3): Corroborates 8537.10; secondary sources confirm VCU/ECU exclusion from 8471.

No conflict between PTA and DA.

**CAAR Valco Conflict (India — added TB-2 pass)**:
CAAR Advance Ruling (India, late 2024) in the Valco matter ruled that a Vehicle Control Unit (VCU) and Power Control Unit (PCU) are classifiable at **8708.99.00** (parts and accessories of motor vehicles, Chapter 87). CAAR found that the VCU/PCU serves a primarily vehicular function and is therefore a part of a motor vehicle under Chapter 87, rather than electrical apparatus under Chapter 85.

This directly conflicts with the Section XVII Note 2(f) analysis that routes electrical control apparatus to Chapter 85. The conflict is noted but the AA conclusion (8537.10.00) is maintained because:
1. The CAAR ruling is in personam — it binds only the applicant (Valco), not all importers
2. It does not constitute binding precedent for India customs in general
3. The GRI 1 + Section XVII Note 2(f) analysis remains the established secondary-source and CBP-comparable position
4. The ruling is a single advance ruling, not a court judgment

India stability is updated to **contested**, confidence to **medium**. Post-domain protocol: Monitor for additional CAAR rulings and any Bombay HC decisions on related matters (BEV Axle + VCU/PCU challenges).

---

## EU Subheading Note: 8537.10.91 vs 8537.10.98

EU CN 8537.10.91 "Programmable memory controllers" is the more specific subheading for the VCU, which stores and executes programmable control firmware. This is preferred over 8537.10.98 (Other). If customs authorities characterize the VCU as something other than a "programmable memory controller" (e.g., as a specialized embedded system), 8537.10.98 would apply as the residual. Heading-level classification is unchanged in either case.

## Graph Links

- `classification_node` → [[product_component-vehicle-control-unit-vcu]]
- `engineering_anchor` → [[vehicle-control-unit-(vcu)]]
- `parent_component` → [[integrated-e-axle]]
- `global_anchor` → [[hs_code-8537-10-global]]
- `classified_as` → [[hs_code-8537-10-91-us]]
- `classified_as` → [[hs_code-8537-10-00-in]]
- `classified_as` → [[hs_code-8537-10-91-eu]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
