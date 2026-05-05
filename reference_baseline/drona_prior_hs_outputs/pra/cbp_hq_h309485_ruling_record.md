---
agent: PRA
ruling_id: CBP-HQ-H309485
jurisdiction: US
ruling_date: "2020-08-12"
ruling_type: "classification_and_origin"
primary_holding: "8507.60"
components_applicable:
  - High-Voltage Battery Pack Assembly (ent_100)
  - High-Voltage Battery Module (ent_133)
source_doc: cbp_hq_h309485_battery_rack.md
batch: TB-2
---

# PRA Record: CBP HQ H309485 — Battery Rack System (LG Chem)

## Ruling Summary

**CBP HQ H309485** (August 12, 2020) is a reconsideration of NY N306055. The ruling addresses:
1. **Country of origin** of LG Chem's Battery Rack System (Model ERT54B22CN21) — held to be China (substantial transformation not achieved in Korea).
2. **Classification**: The Battery Rack System is a lithium-ion battery system classifiable at **HTSUS 8507.60.0020** — lithium-ion storage batteries.

## Article Description

The Battery Rack System is a grid-scale Energy Storage System (ESS) module. It consists of:
- **Battery Modules** containing Li-ion cells (LG Chem JH4 model)
- **Battery Racks** (22 modules per rack, 1,232 cells per rack, connected in parallel)
- **Battery Protection Units** (protection circuitry)
- **Battery Management System** (Master BMS + Rack BMS + Module BMS)

The Battery Rack System is a cabinetized lithium-ion battery system with integrated BMS. It is imported as an assembly.

## Classification Holding

The ruling confirms that a lithium-ion battery system consisting of cells, modules, racks, and BMS — imported as a functional assembly — classifies at **8507.60 (lithium-ion accumulators/storage batteries)**.

**Essential character analysis**: The electrochemical cells and the battery modules (their physical housing of cells) are the components that give the assembly its essential character as a storage battery. The BMS, protection units, and rack hardware are ancillary to the electrochemical energy storage function.

## Applicability to TB-2 Components

### HV Battery Pack Assembly (ent_100)

The HV Battery Pack Assembly is directly analogous to the Battery Rack System: it is a complete lithium-ion battery assembly comprising cells, modules, battery pack housing, BMS, thermal management hardware, and busbars. The essential character is the electrochemical cells → 8507.60.00.

CBP HQ H155376 (June 2011) had already established this principle: when a BMS is presented together with lithium-ion cells as an integrated battery product, the assembly classifies at 8507.60 (formerly 8507.80.80 before HS reclassification). H309485 extends this to larger rack/pack-level assemblies with additional management hardware.

**PRA position for HV Battery Pack**: 8507.60.00 (US). H155376 + H309485 together form a consistent ruling basis.

### HV Battery Module (ent_133)

The HV Battery Module is a sub-assembly of the Battery Pack: it contains Li-ion cells, a cell contacting system (CCS), and a Cell Module Controller (CMC). In the context of H309485, each Battery Module (56 cells) within the Battery Rack System is itself a lithium-ion accumulator sub-assembly.

When imported as a standalone module (not assembled into a complete pack), the HV Battery Module is still a lithium-ion accumulator sub-assembly with its essential character in the cells → 8507.60.00.

**PRA position for HV Battery Module**: 8507.60.00 (US). H309485 confirms that module-level lithium-ion assemblies maintain their 8507.60 classification.

## Limitations

1. H309485 is a **classification AND origin** ruling. The origin finding (China, not Korea) does not affect the classification holding (8507.60).
2. The battery system in H309485 is a grid-scale ESS (not an EV battery pack). The classification principle (essential character = Li-ion cells → 8507.60) applies across all lithium-ion battery assemblies, regardless of end-use application.
3. H309485 does **not** address whether a standalone BMS PCBA without cells classifies at 8507.60 — it does not (see H155376 analysis in the BMS pilot batch).

## Graph Links

- `ruling_source` → [[cbp_hq_h309485_battery_rack]]
- `applies_to` → [[product_component-hv-battery-pack-assembly]]
- `applies_to` → [[product_component-hv-battery-module]]
- `cross_reference` → [[cbp_hq_h155376_bms]]
- `graph_index` → [[d-class-hs_gate1_graph_index]]
