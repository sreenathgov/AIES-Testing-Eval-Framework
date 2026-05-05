---
agent: PRA
ruling_id: CBP-HQ-H155376
authority: US Customs and Border Protection, Headquarters
date: "2011-06-22"
jurisdiction: US
held_code: "8507.80.80"
held_heading: Electric accumulators — other
source_doc: rulings/us/cbp_hq_h155376_bms.md
pilot_batch: TB-1
---

## Subject Article

A battery pack assembly consisting of:
- Lithium-ion battery cells
- Printed circuit board assemblies (PCBAs) with monitoring and balancing circuitry
- A housing/enclosure

Described as a "Battery Management System" but physically constituting a **composite battery pack** — cells physically integrated with control PCBAs in a single housing.

> **Critical distinction**: This is NOT a standalone BMS control board. This is cells + PCBAs + housing as a single combined article.

---

## Held

**8507.80.80 — Electric accumulators, other**

**Basis**: GRI 3(b) — essential character analysis for composite good.

The battery cells (energy storage function) confer the essential character of the assembled article. The management electronics are ancillary to the primary storage function. EN 85.07 states that batteries presented with ancillary protective/monitoring circuits are classifiable in 8507.

---

## Party Arguments Rejected

| Argument | Code | CBP Rejection |
|----------|------|---------------|
| Control panel for electric control | 8537.10 | BMS circuitry is ancillary to battery cells in the composite article. Cells provide essential character. EN 85.07 explicitly addresses this configuration. |

---

## Applicability to Pilot Components

### Standalone BMS PCBA (ent_217)
**Not applicable.**

H155376 classified a composite battery PACK — cells + PCBAs + housing. Pilot entity ent_217 is a standalone BMS PCBA without battery cells. Different physical product. EN 85.07 composite good rule applies only when the control circuit is presented WITH the battery cells as a combined article.

**Override condition 2 fails**: different physical product → override rejected.

### Li-Ion Battery Cell (ent_147)
**Partially corroborating.**

H155376 confirms 8507 for battery articles with integrated electronics. Reinforces 8507.60 for standalone Li-Ion cells (though the ruling addressed a pack, not a standalone cell).

---

## Quality Assessment

| Factor | Assessment |
|--------|------------|
| Binding status | Binding on CBP for substantially identical transactions (US) |
| Age | 2011 — pre-dates modern 400V/800V EV architectures |
| Reliability for composite pack | High |
| Reliability for standalone BMS PCBA | **Low** — different physical product |
| Trade practice misapplication risk | **High** — importers may cite H155376 broadly for standalone BMS |
