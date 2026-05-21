<!-- Reviewer-safe sanitized forensic artifact. This file evidences artifact origin only and is not external legal authority. -->

---
agent: PRA
ruling_id: EU-BTI-EBTI-SAMPLE-FILTERED
authority: EU Binding Tariff Information database — multiple Member State customs authorities
jurisdiction: EU
source_doc: rulings/eu/bti/ebti_sample_targeted_test_run.md
sample_size: 30 records (targeted EV component sample)
member_states: DE (Germany), CZ (Czech Republic), FR (France)
years_covered: 2024–2025
pilot_batch: TB-1
---

## Relevant Entries for Pilot Components

### CZ BTI CZBTI34/018997/2025-580000-04/01

| Field | Value |
|-------|-------|
| Member State | Czech Republic |
| Year | 2025 |
| Article | 80 kW AC traction motor with integrated inverter |
| Held | CN 8501.53.50.10 |
| Heading | 8501.53 — AC motors, multi-phase, >75 kW |

**Basis**: GRI 1. Traction motor with integrated inverter classified at motor heading (8501.53) rather than inverter/converter heading (8504). Essential function is motor propulsion; inverter is ancillary to motor operation.

**Applicability to pilot**:
- Traction Motor (ent_221) → **Corroborates 8501.53.50**. Pilot entity is a standalone motor (no integrated inverter) — even stronger case for 8501.53, no composite good analysis required.

---

## Coverage Gaps

No BTI entries found in the 30-record sample for:
- Standalone BMS PCBA (8537.10)
- HV Contactor (8536.49)
- DC-DC Converter (8504.40)
- OBC (8504.40)
- Standalone Li-Ion Battery Cell (8507.60)

**Implication**: PTA tariff text classification stands without BTI-level corroboration for these components. The EU BTI database has ~200,000 records — this sample is not exhaustive.

---

## Quality Assessment

| Factor | Assessment |
|--------|------------|
| Binding status | BTI rulings are legally binding in the issuing Member State; persuasive EU-wide under uniform CN |
| CZ BTI for traction motor | High quality corroboration |
| Sample coverage | Limited — 30 records, no BTI for most pilot components |
