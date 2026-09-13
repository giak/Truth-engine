---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-103-RUN-HANDOFF"
version: "1.0"
status: "closed"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-103"
---

<!-- DERIVED_FROM: te_run=20260906-1451-defiance-institutionnelle-francaise; pilot_review=INV-103_PILOT_REVIEW.md -->
<!-- DECISION: truth_engine=DELIVERY_PASS_R3P1; renard=NO; inv=CLOSED -->

# RUN_HANDOFF — INV-103

```text
INV_ID = INV-103
TE_STATUS = DELIVERY_PASS_R3P1
TE_RUN_ID = 20260906-1451-defiance-institutionnelle-francaise
TE_PATH = 2026-09-06_14-51_defiance-institutionnelle-francaise_INVESTIGATION.md
QRY = 15
SRC = 8
PROVENANCE_FAMILIES = 3
FCT = 15
CHECKPOINTS = 7
MNEMO = MNEMO_UNAVAILABLE degraded
PERSISTENCE = PASS / 15 blocked terminal outcomes
RENARD = NO
INV_STATUS = CLOSED
```

## Central delta

La défiance institutionnelle française n'est pas un agrégat uniforme. Le run établit une hiérarchie durablement différenciée entre représentation politique nationale/médias et institutions de proximité, de soin ou de protection (`CLM-001..006`). Il sépare également attachement à la démocratie et jugement de son fonctionnement (`CLM-004`).

Les déterminants mesurés de confiance — voix politique, position sociale subjective, efficacité/moyens, honnêteté, respect — restent des **associations**. `CLM-007` et `CAU-001..004` interdisent de les convertir en causalité générale sans design d'identification.

## Highest supported I0..I7

```text
I0 identity/relation = VERIFIED pour institutions, instruments et relations de mesure
I1 resources/capability/access = N/A à l'objet principal
I2 documented action = N/A à l'objet principal
I3 coordination/tasking/control = N/A à l'objet principal
I4 exposure/reach = N/A à l'objet principal
I5 reception/persuasion = OBSERVED ATTITUDES, pas persuasion attribuée
I6 behavior/institutional change = NOT_ESTABLISHED causalement
I7 counterfactual outcome = NOT_ESTABLISHED
```

## Material gaps / contradictions

1. `CAU-001..003` : direction et taille causales non identifiées ; il faut panel, expérience, quasi-expérience ou autre stratégie d'identification.
2. `CAU-004` : controverses policières et trajectoire agrégée sont temporellement observables, mais leur contribution causale respective n'est pas isolée.
3. `CLM-008` : les deux mesures « 29 % » médias/news proviennent d'instruments différents ; aucune identité de mesure n'est inférée.
4. La série longue reste majoritairement dépendante de la famille CEVIPOF ; le contrôle OCDE est indépendant mais récent.

## RENARD decision + reason

```text
RENARD = NO
```

Aucun résiduel accessible actuel ne promet de changer matériellement le modèle sans nouvelles données longitudinales ou un vrai design causal. Continuer par recherche générique serait du fishing.

## New ideas triaged

```text
nouvelle vague CEVIPOF/OECD                     -> RECHECK lors de publication
panel/expérience sur political voice -> trust   -> RECHECK si design causal disponible
hétérogénéité police par sous-groupes           -> DEFER vers investigation dédiée si claim agrégé devient décisif
learned helplessness                            -> ne pas activer par analogie ; seulement via efficacité politique empirique contemporaine
```

## Registry patch

```text
INV-103 -> CLOSED
truth_engine -> DELIVERY_PASS_R3P1
renard -> NO
result_path -> INV-103_RUN_HANDOFF.md
next_action -> NONE — CLOSED
INV-081 -> READY_NOT_LAUNCHED (post-pilot dynamic selection)
```
