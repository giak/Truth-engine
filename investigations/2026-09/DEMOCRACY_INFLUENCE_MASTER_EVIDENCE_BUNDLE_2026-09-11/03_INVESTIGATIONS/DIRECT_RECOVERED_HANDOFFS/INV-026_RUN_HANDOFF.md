---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-026-RUN-HANDOFF"
version: "1.0"
status: "closed"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-026"
---

<!-- DERIVED_FROM: te_run=20260907-0610-israel-influence-france-ue; review=INV-026_POST_RUN_REVIEW.md -->
<!-- DECISION: truth_engine=DELIVERY_PASS_R3P1; renard=NO; inv=CLOSED -->

# RUN_HANDOFF — INV-026

```text
INV_ID = INV-026
TE_STATUS = DELIVERY_PASS_R3P1
TE_RUN_ID = 20260907-0610-israel-influence-france-ue
QRY = 13
SRC = 13
PROVENANCE_FAMILIES = 10
FCT = 30
CHECKPOINTS = 7
MNEMO = MNEMO_UNAVAILABLE degraded
PERSISTENCE = PASS / 30 blocked terminal outcomes
DELIVERABLE_SHA256 = 86f7d0d457469edf3edb9dffa2e5f55f253cfebefdb0037652cc4ebf5a2d963a
RENARD = NO
INV_STATUS = CLOSED
```

## Central delta

Israël est un émetteur documenté d'influence ouverte en France ; un financement étatique précis d'un événement ELNET Europe est établi ; ELNET France déclare parallèlement ses activités de lobbying en propre ; et Rokh Solis établit une ingérence numérique étrangère liée à un opérateur privé israélien sans commanditaire identifié. L'ensemble interdit aussi bien le déni de mécanismes d'influence que la promotion automatique d'acteurs pro-israéliens en proxies étatiques.

## Highest supported I0..I7

```text
I0 identity/relation = VERIFIED pour acteurs officiels, ELNET et opérateurs privés ; sponsor Rokh Solis UNKNOWN
I1 resources/capability/access = VERIFIED — canaux ambassade, financement événement, voyage presse, capacités influence-for-hire
I2 documented action = VERIFIED — diplomatie publique, lobbying déclaré, événement financé, voyage presse, Rokh Solis
I3 coordination/tasking/control = VERIFIED sur organes officiels et transaction MFA->ELNET Europe ; PARTIAL/UNKNOWN pour tasking général ELNET et sponsor Blackcore
I4 exposure/reach = PARTIAL — accès média documenté ; Rokh Solis très faible visibilité ; Zero Zeno faible engagement
I5 reception/persuasion = NOT_ESTABLISHED
I6 behavior/institutional/electoral change = NOT_ESTABLISHED pour les cas France centraux
I7 counterfactual outcome = NOT_ESTABLISHED
```

## Material gaps / contradictions

- `RESPONSIBILITY`: sponsor Blackcore/Rokh Solis non identifié.
- `RESPONSIBILITY`: financement ELNET d'une activité précise `!=` commandement général.
- `CAUSALITY`: exposition/réception/effet politique ou électoral non fermés.
- `official denial != proof`; `parliamentary allegation != finding`.

## RENARD

`NO` — les résiduels exigent de nouveaux documents de sponsor/tasking ou un design causal, pas davantage de recherche générique.

## New ideas triaged

```text
MERGE -> INV-146 : Israel-as-sender symmetry controls
RECHECK -> Blackcore/Rokh Solis sponsor if judicial/declassified evidence appears
RECHECK -> ELNET state-tasking only on direct contract/instruction evidence
DEFER -> causal electoral/policy effect until independent design/data exists
```

## Registry patch

`INV-026 -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`.
