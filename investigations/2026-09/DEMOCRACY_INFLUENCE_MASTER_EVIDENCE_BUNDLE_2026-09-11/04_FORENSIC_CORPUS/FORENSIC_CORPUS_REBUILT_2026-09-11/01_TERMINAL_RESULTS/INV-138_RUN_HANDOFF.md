---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-138-RUN-HANDOFF"
version: "1.0"
status: "closed"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-138"
---

<!-- DERIVED_FROM: te_run=20260906-2212-france-puissance-influence-exterieure; review=INV-138_POST_RUN_REVIEW.md -->
<!-- DECISION: truth_engine=DELIVERY_PASS_R3P1; renard=NO; inv=CLOSED -->

# RUN_HANDOFF - INV-138

```text
INV_ID = INV-138
TE_STATUS = DELIVERY_PASS_R3P1
TE_RUN_ID = 20260906-2212-france-puissance-influence-exterieure
QRY = 23
SRC = 22
PROVENANCE_FAMILIES = 16
FCT = 26
CHECKPOINTS = 7
MNEMO = MNEMO_UNAVAILABLE degraded
PERSISTENCE = PASS / 26 blocked terminal outcomes
DELIVERABLE_SHA256 = 54cc64ec22dff754b445b41bb921b9dd7b90c1397c4938a891f79675e050d823
RENARD = NO
INV_STATUS = CLOSED
```

## Central delta

La France fournit un contrôle symétrique matériel : elle emploie elle-même un portefeuille documenté allant de l'influence ouverte et consentie à la conditionnalité, aux opérations militaires informationnelles, aux interventions directes dans des rapports de force internes et à une opération trompeuse liée à des individus associés à l'armée. Ce résultat ne permet pas de tout appeler « ingérence » ; il impose au contraire une qualification par propriétés : visibilité, consentement, base juridique, tasking, coercition/clandestinité et effet.

## Highest supported I0..I7

```text
I0 identity/relation = VERIFIED/PARTIAL - institutions et opérateurs ouverts identifiés ; réseau Meta limité à individus associés à l'armée
I1 resources/capability/access = VERIFIED - financements, coopération, L2I, moyens militaires et leviers visa/aide documentés
I2 documented action = VERIFIED - programmes, réseau trompeur, frappes, logistique, armement et exfiltration documentés
I3 coordination/tasking/control = VERIFIED pour dispositifs officiels ; UNKNOWN/PARTIAL pour réseau Meta 2020
I4 exposure/reach = PARTIAL - métriques Meta faibles ; portée hétérogène ailleurs
I5 reception/persuasion = NOT_ESTABLISHED généralement
I6 behavior/institutional/policy change = PARTIAL - effets tactiques directs Tchad/Côte d'Ivoire ; Libye multicausale
I7 counterfactual outcome = NOT_ESTABLISHED
```

## Material gaps / contradictions

- réseau Meta 2020 : affiliation individuelle != commandement institutionnel ;
- candidats : doctrine publique 2023 « aucun candidat » vs rapport AN 2026 évoquant des soutiens/oppositions récents, sans cas nommés dans le passage ;
- visas/aide : intention de pression établie, effet comportemental non quantifié ;
- Libye/Madagascar : action et chronologie mieux établies que l'intention finale et le contrefactuel ;
- les effets I5-I7 restent généralement non identifiés hors effets militaires intermédiaires.

## RENARD decision + reason

`RENARD = NO`. Les gaps exigent pièces de tasking/déclassification, cas primaires nommés ou design causal. Ajouter des exemples génériques serait cumulatif.

## New ideas triaged

```text
Meta 2020 institutional tasking            -> RECHECK sur pièce nouvelle
recent named candidate-support cases       -> RECHECK si pièce primaire
visa/APD country-level causal evaluation   -> DEFER vers étude quantitative
France/UE/US symmetry matrix               -> MERGE vers INV-146
more generic soft-power examples           -> DROP
```

## Registry patch

```text
INV-138 -> CLOSED
truth_engine -> DELIVERY_PASS_R3P1
renard -> NO
result_path -> INV-138_RUN_HANDOFF.md
next_action -> NONE - CLOSED; France-as-sender controls available to INV-146; recheck only on material tasking/candidate/causal evidence.
```
