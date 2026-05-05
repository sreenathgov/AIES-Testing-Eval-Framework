---
agent: PRA
ruling_id: CESTAT-CHENNAI-40800-2025
authority: Customs, Excise and Service Tax Appellate Tribunal, Chennai Bench
date: "2025-08-07"
jurisdiction: India
held_code: "9032.89.10"
held_heading: Automatic regulating or controlling instruments and apparatus — other
source_doc: rulings/india/cestat_ruling_electric_motor_vehicle_parts.md
pilot_batch: TB-1
---

## Subject Article

**Body Control Module (BCM) / Intelligent Body Unit (IBU)**

Electronic control unit controlling **vehicle body functions**:
- Windshield wipers
- Climate control (HVAC)
- Headlamps and interior lighting
- Door locks and power windows

Receives signals from sensors throughout the vehicle cabin and actuates corresponding body systems.

> **Critical distinction**: BCM controls VEHICLE BODY FUNCTIONS (cabin comfort, lighting, locks). This is categorically different from a Battery Management System (BMS), which controls BATTERY CELL CHEMISTRY (voltage, current, temperature, state of charge, cell balancing).

---

## Held

**CTH 9032.89.10 — Automatic regulating or controlling instruments and apparatus, other**

**Basis**: GRI 1. BCM is an automatic control apparatus — it receives sensor inputs and automatically controls vehicle body function outputs. Chapter 90 Explanatory Notes cover automatic regulators/controllers.

---

## Applicability to Pilot Components

### BMS (ent_217)
**Not applicable. BCM ≠ BMS.**

| Attribute | BCM | BMS |
|-----------|-----|-----|
| Controls | Vehicle body functions | Battery cell chemistry |
| Domain | Cabin comfort, lighting, locks | Voltage, SoC, cell balancing |
| Chapter 90 Note 2 | Primary function = automatic control | Primary function = switching/protection |
| Classification | 9032 | 8537 |

The CESTAT ruling does not transfer to BMS. Chapter 90 Note 2 correctly excludes BMS — BMS primarily switches and protects (Ch 85), it does not primarily measure/regulate in the Ch 90 instrument sense.

**Override condition 2 fails**: different physical product → override rejected for BMS.

### All other pilot components
Not applicable.

---

## Quality Assessment

| Factor | Assessment |
|--------|------------|
| Binding status | Final CESTAT order — binding on tribunal jurisdiction |
| Age | 2025-08-07 — very recent, high currency |
| Reliability for BCM/IBU | High |
| Reliability for BMS | **Not applicable** — different component |
| Trade practice misapplication risk | **Medium** — practitioners may incorrectly analogize BCM ruling to BMS |
