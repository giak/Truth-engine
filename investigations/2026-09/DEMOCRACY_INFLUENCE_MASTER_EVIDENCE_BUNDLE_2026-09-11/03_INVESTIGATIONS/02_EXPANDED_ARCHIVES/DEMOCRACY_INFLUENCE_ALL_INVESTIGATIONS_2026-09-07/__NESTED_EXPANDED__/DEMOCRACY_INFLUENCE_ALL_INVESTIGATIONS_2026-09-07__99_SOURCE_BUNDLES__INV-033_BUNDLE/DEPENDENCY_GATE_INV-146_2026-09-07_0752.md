---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "dependency_gate"
artifact_id: "DEPENDENCY-GATE-INV-146-20260907-0752"
version: "1.0"
status: "pass"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-146"
---

<!-- DERIVED_FROM: INV-033 CLOSED / DELIVERY_PASS_R3P1 -->
<!-- DECISION: dependency_gate=PASS; INV-146 BLOCKED -> BACKLOG; auto_READY=false; reason=type_SYNTHESIS -->

# Dependency gate — INV-146

## Verdict

```text
DEPENDENCIES_DONE = PASS
DIRECT_DEPENDENCIES = 10
OPEN_DEPENDENCIES = 0
INV-146 = BACKLOG
AUTO_READY = NO / type=SYNTHESIS
```

## Dependency status

| Dependency | Status |
|---|---|
| INV-019 | CLOSED |
| INV-022 | CLOSED |
| INV-026 | CLOSED |
| INV-033 | CLOSED |
| INV-128 | CLOSED |
| INV-134 | CLOSED |
| INV-138 | CLOSED |
| INV-139 | CLOSED |
| INV-140 | CLOSED |
| INV-145 | CLOSED |

## Transition

`INV-146 BLOCKED -> BACKLOG`.

Le gate de dépendances est satisfait. Aucune exécution Truth Engine n’est lancée ici. La synthèse doit être reclassifiée/lancée explicitement selon son contrat de type `SYNTHESIS`; `control.py` réserve `READY/TE_ACTIVE` aux types `PRIMARY|CASE`.
