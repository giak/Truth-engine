---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "dashboard"
artifact_id: "DASHBOARD"
version: "2.1-kiss"
status: "generated"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
---

<!-- TRACE: generated_by=control.py; source=INVESTIGATION_REGISTRY.csv; do_not_edit_state_here=true -->
<!-- TRACE: supplemental_snapshots_are_noncanonical=true; snapshot=PROGRAM_SNAPSHOT_2026-09-07.json -->

# Dashboard

Current: **no active item**
Next gate: **reclassification required before any launch**

## Program state

| Metric | Value |
|---|---:|
| TOTAL | 146 |
| CLOSED | 34 |
| BACKLOG | 86 |
| BLOCKED | 12 |
| CONDITIONAL | 7 |
| MERGED | 6 |
| DEFERRED | 1 |
| READY | 0 |
| TE_ACTIVE | 0 |
| CLOSED / DELIVERY_PASS_R3P1 | 20 |

## Pilot baseline

| Pilot | Status | Truth Engine | Next |
|---|---|---|---|
| INV-010 | CLOSED | DELIVERY_PASS_R2A2 | CLOSED — pilot reviewed; targeted RENARD closed. |
| INV-019 | CLOSED | DELIVERY_PASS_R2A2 | CLOSED — pilot PASS; RENARD NO. |
| INV-049 | CLOSED | DELIVERY_PASS_R2A2 | CLOSED — pilot PASS after targeted RENARD; no further material delta. |
| INV-071 | CLOSED | DELIVERY_PASS_R2A2 | CLOSED — pilot PASS; RENARD NO. |
| INV-103 | CLOSED | DELIVERY_PASS_R3P1 | NONE — CLOSED after post-run review; RENARD NO; causal upgrades require new identified designs/data. |

## Critical path

```text
no active item
-> reclassify under CORE_MISSION_GATE
-> materialize current pool
-> select at most one READY
```

## Synthesis dependency watch

| Synthesis | Status | Open direct dependencies |
|---|---|---|
| INV-095 | BLOCKED | INV-119 |
| INV-102 | BLOCKED | INV-095, INV-098, INV-099 |
| INV-129 | BLOCKED | INV-080, INV-124 |
| INV-144 | BLOCKED | INV-045, INV-078, INV-079 |
| INV-133 | BLOCKED | INV-038, INV-040, INV-052, INV-068, INV-082, INV-088, INV-095, INV-102, INV-104, INV-129, INV-144 |

## Forensic snapshot / export

- Program snapshot: `PROGRAM_SNAPSHOT_2026-09-07.json` (derived, non-canonical).
- Analytic point: `ANALYTIC_POINT_2026-09-07.md` (derived, non-canonical).
- Consolidated export: `DEMOCRACY_INFLUENCE_ALL_INVESTIGATIONS_2026-09-07.zip`.
- Export SHA-256: `b2fec50e9cdd5e18806a96cdc7682b3fa23a917af6abe939ecafa1d0a590779f`.
- Runtime locked: `Truth Engine 2.10.6 / R3P1`.
- Runtime bundle SHA-256: `d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30`.
- Corpus SHA-256: `6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052`.

Selection after pilots: `CORE_MISSION_GATE -> model_change > discrimination > dependency_unlock > coverage_gap > utility`.

<!-- GATE: one_READY_or_TE_ACTIVE_max=true -->
<!-- INVARIANT: dashboard_and_snapshots_are_derived; registry_is_state_source -->
