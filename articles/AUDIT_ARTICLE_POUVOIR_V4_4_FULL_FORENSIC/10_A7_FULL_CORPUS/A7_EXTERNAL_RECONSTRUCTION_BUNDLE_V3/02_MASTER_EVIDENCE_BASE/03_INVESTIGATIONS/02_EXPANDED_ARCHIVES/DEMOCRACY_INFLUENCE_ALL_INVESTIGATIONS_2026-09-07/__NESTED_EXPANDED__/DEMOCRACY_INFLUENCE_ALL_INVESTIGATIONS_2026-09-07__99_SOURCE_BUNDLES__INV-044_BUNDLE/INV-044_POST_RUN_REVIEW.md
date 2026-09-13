---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "post_run_review"
artifact_id: "INV-044-POST-RUN-REVIEW"
version: "1.0"
status: "closed"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-044"
---

<!-- DERIVED_FROM: te_run=20260907-1141-europe-democracy-shield -->
<!-- DECISION: p0=0; p1=0; p2=3; renard=NO; closure_authorized=true -->

# POST-RUN REVIEW — INV-044

## Verdict

```text
TRUTH_ENGINE = DELIVERY_PASS_R3P1
PRE_GATE = PASS
DELIVERY_GATE = PASS
TESTS = 140 passed / 2 skipped
QRY = 14
SRC = 14
FCT = 27
PROVENANCE_FAMILIES = 5
G0_G10 = PASS
PERSISTENCE = PASS / 27 blocked terminal outcomes / MNEMO_UNAVAILABLE
P0 = 0
P1 = 0
P2 = 3
RENARD = NO
CLOSE = AUTHORIZED
```

## Contradictory review

Le run soutient simultanément deux propositions qui doivent rester ensemble :

1. il existe un écosystème européen structuré, financé et articulé de résilience/gouvernance informationnelle ;
2. le dossier ne ferme pas une chaîne générale `Commission -> ordre éditorial -> retrait -> effet politique`.

Le pont DSA/Code de conduite est matériel et co-régulatoire ; il interdit de réduire l'ensemble à des initiatives purement volontaires sans portée réglementaire. Inversement, financement, coordination, monitoring, fact-checking ou signalement ne démontrent pas en eux-mêmes un commandement centralisé de la modération.

Les contrôles négatifs sont conservés : gouvernance formelle d'EDMO, statut d'observateur de la Commission, frontière déclarée d'EUvsDisinfo sur le retrait, voies de recours DSA et corrections mesurables.

## Highest supported I0..I7

```text
I0 identity/relation = VERIFIED
I1 resources/capability = VERIFIED
I2 documented action = VERIFIED
I3 coordination/tasking/control = VERIFIED for institutional/program coordination; NOT transferable to editorial tasking
I4 exposure/reach = PARTIAL
I5 reception/persuasion = NOT_ESTABLISHED
I6 behavior/institutional change = PARTIAL
I7 counterfactual democratic outcome = NOT_ESTABLISHED
```

## P2 residuals

1. fermer des chaînes cas-par-cas `signal/assessment -> platform or regulator decision -> appeal/correction` ;
2. mesurer exposition, réception et effet comportemental au-delà des outputs institutionnels ;
3. tester dans INV-144 si croissance budgétaire, marchés, métriques et bénéficiaires produisent des incitations d'expansion, sans présumer menace fabriquée.

Ces résidus exigent des cas ou données spécifiques. Une collecte générique supplémentaire serait cumulative : `RENARD=NO`.

## Routing

```text
MERGE -> INV-040 : powers/intermediaries/co-regulation map
MERGE -> INV-144 : budgets/programs/metrics/incentives control
RECHECK -> INV-043/INV-045 only for case-specific moderation/certification edges
```
