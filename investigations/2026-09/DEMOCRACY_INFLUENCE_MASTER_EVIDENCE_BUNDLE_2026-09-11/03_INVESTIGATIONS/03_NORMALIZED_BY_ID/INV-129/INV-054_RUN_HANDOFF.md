---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-054-RUN-HANDOFF"
version: "1.0"
status: "closed"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-054"
---

<!-- DERIVED_FROM: te_run=20260907-1222-strategic-litigation-ngo; review=INV-054_POST_RUN_REVIEW.md -->
<!-- DECISION: truth_engine=DELIVERY_PASS_R3P1; renard=NO; inv=CLOSED -->

# RUN_HANDOFF — INV-054

```text
INV_ID = INV-054
TE_STATUS = DELIVERY_PASS_R3P1
TE_RUN_ID = 20260907-1222-strategic-litigation-ngo
QRY = 11
SRC = 11
PROVENANCE_FAMILIES = 5
FCT = 24
CHECKPOINTS = 6
MNEMO = MNEMO_UNAVAILABLE degraded
PERSISTENCE = PASS / 24 terminal blocked outcomes
DELIVERABLE_SHA256 = 9b02a7b42d2289c9ea2e2b0d47481f091a4bccc35118d0448f9620ab8b409c03
P0 = 0
P1 = 0
P2 = 3
RENARD = NO
INV_STATUS = CLOSED
```

## Central delta

Le contentieux stratégique est un mécanisme intentionnel et documenté d'influence juridique : certaines organisations sélectionnent, soutiennent et suivent des affaires afin de produire des changements de droit ou de pratique. Des décisions comme Grande-Synthe, l'Affaire du Siècle ou KlimaSeniorinnen montrent que ce canal peut produire des obligations institutionnelles matérielles. Mais les contrôles négatifs montrent aussi que `stratégie + accès au juge != contrôle du résultat`.

Le financement de capacité est vérifié ; le tasking externe d'une affaire précise n'est pas établi. `jugement -> mise en œuvre -> effet politique durable` reste également une chaîne partielle.

## Highest supported I0..I7

```text
I0 identity/relation = VERIFIED
I1 resources/capability = VERIFIED
I2 documented action = VERIFIED
I3 coordination/tasking = VERIFIED for self-directed organisational coordination; external donor tasking NOT_ESTABLISHED
I4 exposure/reach = PARTIAL
I5 reception/persuasion = NOT_APPLICABLE / NOT_ESTABLISHED as system pathway
I6 behavior/institutional change = VERIFIED/PARTIAL case-specific
I7 counterfactual outcome = NOT_ESTABLISHED
```

## Material gaps

- financement d'organisation `!=` commandement d'un contentieux précis ;
- stratégie contentieuse `!=` procédure abusive ;
- accès au juge `!=` contrôle du jugement ;
- victoire judiciaire `!=` mise en œuvre complète ;
- mise en œuvre `!=` effet politique durable contrefactuel.

## Routing

```text
MERGE -> INV-052 : funded civil-society capacity and autonomy/tasking boundary
MERGE -> INV-129 : strategic litigation / legal coercion comparison and judgment-execution boundary
RECHECK -> only on case-level donor tasking, execution records or causal designs
```
