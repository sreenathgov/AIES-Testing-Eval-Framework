---
agent: KA
audit_id: KA-003
batch: TB-2
components_audited: 5
date: 2026-04-02
result: PASS WITH NOTES
corrections_required: 0
---

## Audit Scope

TB-2 components: Integrated E-Axle (ent_187), Hyper-Integrated E-Axle (ent_269), HV Battery Pack Assembly (ent_100), HV Battery Module (ent_133), Combo Power Electronics Unit (ent_267).

Artifact chain audited:
- PRA (1 file): `pra/cbp_hq_h309485_ruling_record.md`
- PTA (15 files): 5 components × 3 jurisdictions
- DA (2 memos): `da_memo_tb2_e_axle.md`, `da_memo_tb2_battery_pack.md`
- AA (5 files): one per component

---

## Invariant Checks

### I-1: Entity ID Traceability

| Component | entity_id | PTA | AA | Match |
|-----------|-----------|-----|----|-------|
| Integrated E-Axle | ent_187 | ✓ | ✓ | PASS |
| Hyper-Integrated E-Axle | ent_269 | ✓ | ✓ | PASS |
| HV Battery Pack Assembly | ent_100 | ✓ | ✓ | PASS |
| HV Battery Module | ent_133 | ✓ | ✓ | PASS |
| Combo Power Electronics Unit | ent_267 | ✓ | ✓ | PASS |

**Result: PASS**

---

### I-2: GRI Path Consistency (PTA → AA)

| Component | PTA GRI | AA GRI | Match |
|-----------|---------|--------|-------|
| Integrated E-Axle | GRI_3b | GRI_3b | PASS |
| Hyper-Integrated E-Axle | GRI_3b (+ 3c fallback) | GRI_3b_with_GRI_3c_fallback | PASS |
| HV Battery Pack Assembly | GRI_3b | GRI_3b | PASS |
| HV Battery Module | GRI_3b | GRI_3b | PASS |
| Combo Power Electronics Unit | GRI_3b | GRI_3b | PASS |

**Result: PASS**

---

### I-3: HS Code PTA→AA Consistency

| Component | JX | PTA Code | AA Code | Match |
|-----------|-----|----------|---------|-------|
| Integrated E-Axle | US | 8708.99.68 | 8708.99.68 | PASS |
| Integrated E-Axle | EU | 8708.99 | 8708.99 | PASS |
| Integrated E-Axle | IN | 8501.53.30 | 8501.53.30 | PASS |
| Hyper-Integrated E-Axle | US | 8708.99.68 | 8708.99.68 | PASS |
| Hyper-Integrated E-Axle | EU | 8708.99 | 8708.99 | PASS |
| Hyper-Integrated E-Axle | IN | 8501.53.30 | 8501.53.30 | PASS |
| HV Battery Pack Assembly | US | 8507.60.00 | 8507.60.00 | PASS |
| HV Battery Pack Assembly | EU | 8507.60.00 | 8507.60.00 | PASS |
| HV Battery Pack Assembly | IN | 8507.60.00 | 8507.60.00 | PASS |
| HV Battery Module | US | 8507.60.00 | 8507.60.00 | PASS |
| HV Battery Module | EU | 8507.60.00 | 8507.60.00 | PASS |
| HV Battery Module | IN | 8507.60.00 | 8507.60.00 | PASS |
| Combo Power Electronics Unit | US | 8504.40.70 | 8504.40.70 | PASS |
| Combo Power Electronics Unit | EU | 8504.40.60 | 8504.40.60 | PASS |
| Combo Power Electronics Unit | IN | 8504.40.90 | 8504.40.90 | PASS |

**Result: PASS** (15/15)

---

### I-4: GRI 3(b) Essential Character Reasoning (MANDATORY for all TB-2)

All TB-2 components are composite goods requiring GRI 3(b) analysis. AA files must contain `essential_character_reasoning` in frontmatter and substantive analysis in body.

| Component | i4_flag | essential_character_reasoning present | Body analysis present |
|-----------|---------|--------------------------------------|----------------------|
| Integrated E-Axle | ✓ | ✓ | ✓ (vehicular drivetrain housing) |
| Hyper-Integrated E-Axle | ✓ | ✓ | ✓ (vehicular chassis platform; GRI 3(c) fallback) |
| HV Battery Pack Assembly | ✓ | ✓ | ✓ (Li-ion cells dominant) |
| HV Battery Module | ✓ | ✓ | ✓ (Li-ion cells dominant; sub-assembly analysis) |
| Combo Power Electronics Unit | ✓ | ✓ | ✓ (OBC dominant by power + value) |

**Result: PASS**

---

### I-5: Section XVII Note 2(f) Exclusion Check (composite goods)

All TB-2 composite goods with Chapter 85 sub-components must document the Section XVII Note 2(f) exclusion analysis.

| Component | Note 2(f) documented | Outcome |
|-----------|---------------------|---------|
| Integrated E-Axle | ✓ | FIRED — motor is Chapter 85; but e-axle as mechanical+electrical article → Chapter 87 NOT vetoed (see note below) |
| Hyper-Integrated E-Axle | ✓ | FIRED for electrical sub-components; vehicular platform → Chapter 87 governs |
| HV Battery Pack Assembly | ✓ | Not applicable (8507 = Ch 85; not Ch 87 question) |
| HV Battery Module | ✓ | Not applicable (8507 = Ch 85) |
| Combo Power Electronics Unit | ✓ | FIRED — all sub-components Chapter 85 → Chapter 87 vetoed |

**Note on e-axle Note 2(f)**: Section XVII Note 2(f) vetoes Chapter 87 for pure electrical apparatus (Ch 85). However, the e-axle is a composite mechanical + electrical assembly; it is NOT purely electrical apparatus. The traction motor and inverter are Chapter 85, but the gearbox is Chapter 84 and the structural housing is a mechanical drivetrain article. Section XVII Note 2(f) does not mandate Chapter 85 for mixed mechanical/electrical composites — GRI 3 governs. PTA files correctly handle this. No correction needed.

**Result: PASS WITH NOTE** (e-axle Note 2(f) interaction correctly handled in PTA)

---

### I-6: Jurisdiction Divergence Flag Accuracy

| Component | jurisdiction_divergence in AA | Correct? |
|-----------|------------------------------|----------|
| Integrated E-Axle | true | ✓ (India 8501 vs. US/EU 8708) |
| Hyper-Integrated E-Axle | true | ✓ (same divergence) |
| HV Battery Pack Assembly | false | ✓ (all 8507.60.00) |
| HV Battery Module | false | ✓ (all 8507.60.00) |
| Combo Power Electronics Unit | false | ✓ (heading-level agreement; subheading difference is structural) |

**Result: PASS**

---

### I-7: Contested Stability Documentation

All components with `stability: contested` must document the specific legal dispute.

| Component | Stability | Dispute documented? |
|-----------|-----------|---------------------|
| Integrated E-Axle (IN) | contested | ✓ CAAR BEV Axle denied; Bombay HC pending; CAAR VCU/PCU counter-signal |
| Hyper-Integrated E-Axle (IN) | contested | ✓ Same + GRI 3(c) alternative stronger for 8-in-1 configuration |

**Result: PASS**

---

### I-8: PRA Source Integration

PRA file `cbp_hq_h309485_ruling_record.md` must be referenced in relevant artifacts.

| Artifact | PRA referenced? |
|----------|----------------|
| da_memo_tb2_battery_pack.md | ✓ (H309485 cited as DA-F8) |
| HV Battery Pack AA | ✓ (da_source → da_memo_tb2_battery_pack) |
| HV Battery Module AA | ✓ (same) |

**Result: PASS**

---

### I-9: Misrouted Node Policy Compliance

No wikilinks in TB-2 artifacts must point to `drona/knowledge/misrouted/` nodes.

Graph links audit across all TB-2 AA files:
- `[[hs_code-8708-99-68-us]]` — new staging node (to be created in graph stage)
- `[[hs_code-8708-99-eu]]` — new staging node (to be created)
- `[[hs_code-8501-53-30-in]]` — existing valid staging node ✓
- `[[hs_code-8708-99-global]]` — new staging node (to be created, replaces misrouted)
- `[[hs_code-8507-60-00-us/eu/in]]` — new staging nodes (to be created)
- `[[hs_code-8507-60-global]]` — new staging node (to be created)
- `[[hs_code-8504-40-70-us]]`, `[[hs_code-8504-40-60-eu]]`, `[[hs_code-8504-40-90-in]]` — new staging nodes (to be created)
- `[[hs_code-8504-40-global]]` — existing valid staging node ✓

No references to `drona/knowledge/misrouted/` nodes found.

**Result: PASS**

---

## Special Notes

**E-axle India GRI 3(c) documentation (Hyper-Integrated)**:
The Hyper-Integrated E-Axle AA documents both GRI 3(b) and GRI 3(c) paths. This is correct — when 8 sub-functions compete, essential character may be genuinely indeterminate, making the GRI 3(c) path (last-in-schedule heading = 8708) a legitimate alternative that must be documented for completeness. This is not a deficiency.

**Combo Unit subheading divergence framing**:
The AA correctly identifies the US/EU/India subheading differences as tariff-structural (not substantive divergence). `jurisdiction_divergence: false` at heading level is the correct flag. The subheading-level codes differ because the three tariff schedules subdivide 8504.40 differently; all three point to the same commercial article type.

**8507.60 heading-level nodes**:
The existing staging nodes `hs_code-8507-60-us.md` and `hs_code-8507-60-eu.md` must be updated in the graph stage to reference the new 8-digit `hs_code-8507-60-00-{us/eu}.md` nodes. This is a graph-stage action; no AA correction needed.

---

## Corrections Required

None. TB-2 artifact chain is internally consistent and complete.

**TB-2 Audit Result: PASS WITH NOTES**
