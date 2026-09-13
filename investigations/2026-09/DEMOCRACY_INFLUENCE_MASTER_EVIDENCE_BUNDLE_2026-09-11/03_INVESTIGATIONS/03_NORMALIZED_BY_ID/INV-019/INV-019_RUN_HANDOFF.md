---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-019-RUN-HANDOFF"
version: "1.0"
status: "closed"
updated: "2026-09-05"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-019"
---

<!-- DERIVED_FROM: run=20260905-1921-inv019; pilot_review=INV-019_PILOT_REVIEW.md -->
<!-- DECISION: truth_engine=DELIVERY_PASS_R2A2; renard=NO; inv=closed -->

# RUN_HANDOFF — INV-019

```text
TE_STATUS = DELIVERY_PASS_R2A2
RUN_ID = 20260905-1921-inv019
QRY = 22
SRC = 17
PROVENANCE_FAMILIES = 5
FCT = 19
CHECKPOINTS = 7
MNEMO = MNEMO_UNAVAILABLE degraded
PERSISTENCE = PASS
RENARD = NO
INV_STATUS = CLOSED
```

## Central delta

L'architecture américaine est un **écosystème public-financé à plusieurs
régimes de contrôle**, pas une seule agence :

```text
Congress -> State / legacy USAID -> implementing partners
         -> institutions / civil society / media / election support

Congress -> State passthrough -> NED Board
         -> core institutes + direct grantees -> local actors

Congress -> USAGM -> federal networks + nonprofit grantees / OTF
         -> audiences / information access
```

NED combine financement public, identité privée/nonprofit et discrétion d'un
Board distinct. USAGM combine mission stratégique publique et firewall éditorial.

## Historical covert boundary

Documented: certaines fonctions de soutien politique autrefois financées
covert ont ensuite été institutionnalisées dans des mécanismes overt.

Not established: un tasking CIA actuel permanent sur State, NED ou USAGM.

`historical continuity != current command`.

## Highest supported I0..I7

```text
Architecture-wide: I0 VERIFIED / I1 VERIFIED / I2 VERIFIED / I3 SUPPORTED
USAGM: I4 VERIFIED reach/exposure
System-wide: I5 UNRESOLVED / I6 UNRESOLVED / I7 NOT_ESTABLISHED
```

## Material gaps

1. No current CIA control path established.
2. System-wide persuasion/behavior/outcome cannot be inferred from grants,
   outputs or reach.
3. Organizational map is time-sensitive after the 2025 USAID reorganization.

## RENARD

```text
RENARD = NO
```

No concrete current covert bridge emerged; generic secret-link hunting would be
fishing. Causal impact belongs to case-level investigations.

## Registry patch

```text
INV-019 -> CLOSED
truth_engine -> DELIVERY_PASS_R2A2
renard -> NO
INV-049 -> READY_NOT_LAUNCHED
INV-071 -> BLOCKED
INV-103 -> BLOCKED
```
