---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "dashboard"
artifact_id: "DASHBOARD"
version: "2.5-kiss"
status: "generated"
updated: "2026-09-11"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
---

<!-- TRACE: generated_by=control.py; source=INVESTIGATION_REGISTRY.csv; do_not_edit_state_here=true -->
<!-- TRACE: supplemental_snapshots_and_CONTROL_STATE_are_noncanonical=true -->

# Dashboard

Current: **INV-037 / TE_ACTIVE**
Next gate: **continue current item**

## Program state

| Metric | Value |
|---|---:|
| TOTAL | 147 |
| CLOSED | 104 |
| BACKLOG | 25 |
| BLOCKED | 3 |
| CONDITIONAL | 7 |
| MERGED | 6 |
| DEFERRED | 1 |
| READY | 0 |
| TE_ACTIVE | 1 |
| CLOSED / DELIVERY_PASS_R3P1 | 84 |

## Pilot baseline

| Pilot | Status | Truth Engine | Next |
|---|---|---|---|
| INV-010 | CLOSED | DELIVERY_PASS_R2A2 | CLOSED — pilot reviewed; targeted RENARD closed. |
| INV-019 | CLOSED | DELIVERY_PASS_R2A2 | CLOSED — pilot PASS; RENARD NO. |
| INV-049 | CLOSED | DELIVERY_PASS_R2A2 | CLOSED — pilot PASS after targeted RENARD; no further material delta. |
| INV-071 | CLOSED | DELIVERY_PASS_R2A2 | CLOSED — pilot PASS; RENARD NO. |
| INV-103 | CLOSED | DELIVERY_PASS_R3P1 | NONE — CLOSED after post-run review; RENARD NO; causal upgrades require new identified designs/data. |

## Execution portfolio

Advisory planning only. Fresh `CORE_MISSION_V2` reclassification remains the selection authority.

| Lane | Count | IDs |
|---|---:|---|
| TE active | 1 | INV-037 |
| TE next (advisory) | 0 | NONE |
| TE later (advisory) | 10 | INV-015, INV-016, INV-051, INV-053, INV-075, INV-111, INV-112, INV-120, INV-121, INV-122 |
| New TE candidate / needs reclass | 0 | NONE |
| Reframe / HOLD | 12 | INV-009, INV-024, INV-031, INV-032, INV-034, INV-058, INV-105, INV-106, INV-107, INV-108, INV-109, INV-123 |
| Synthesis ready | 3 | INV-038, INV-040, INV-068 |
| Synthesis blocked | 3 | INV-052, INV-104, INV-133 |
| Conditional | 7 | INV-110, INV-113, INV-114, INV-115, INV-116, INV-117, INV-118 |

## Critical path

```text
INV-037 TE_ACTIVE
-> run Truth Engine R3P1
-> terminal RUN_HANDOFF + incremental reclassification/apply
```

## Synthesis dependency watch

| Synthesis | Status | Open direct dependencies |
|---|---|---|
| INV-038 | BACKLOG | NONE |
| INV-040 | BACKLOG | NONE |
| INV-052 | BLOCKED | INV-051, INV-053, INV-058 |
| INV-068 | BACKLOG | NONE |
| INV-104 | BLOCKED | INV-106, INV-107, INV-111, INV-112 |
| INV-133 | BLOCKED | INV-038, INV-040, INV-052, INV-068, INV-104 |

## Forensic snapshot / export

- Program snapshot: `PROGRAM_SNAPSHOT_2026-09-07.json` (derived, non-canonical).
- Analytic point: `ANALYTIC_POINT_2026-09-07.md` (derived, non-canonical).
- Consolidated export: `DEMOCRACY_INFLUENCE_ALL_INVESTIGATIONS_2026-09-07.zip`.
- Export SHA-256: `b2fec50e9cdd5e18806a96cdc7682b3fa23a917af6abe939ecafa1d0a590779f`.
- Runtime locked: `Truth Engine 2.10.6 / R3P1`.
- Runtime bundle SHA-256: `d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30`.
- Corpus SHA-256: `6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052`.

Selection authority: `INVESTIGATION_ORCHESTRATOR.md`.
Hard gate: `CORE_MISSION_V2`.
Ranking: `model_change > discrimination > effect_closure > symmetry_value > dependency_unlock > coverage_gap > utility`.
Reclassification policy: `CORE_MISSION_V2/ranking-7/v1`; unchanged rows may be reused only with a bounded impact frontier; otherwise full-pool fallback.

<!-- GATE: one_selected_READY_or_TE_ACTIVE_or_SYNTHESIS_max=true -->
<!-- INVARIANT: dashboard_and_CONTROL_STATE_are_derived; registry_is_state_source -->
