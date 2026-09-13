---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-039-RUN-HANDOFF"
version: "1.0"
status: "closed"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-039"
---

<!-- DERIVED_FROM: te_run=20260906-1639-pouvoir-institutions-ue; review=INV-039_POST_RUN_REVIEW.md -->
<!-- DECISION: truth_engine=DELIVERY_PASS_R3P1; renard=NO; inv=CLOSED -->

# RUN_HANDOFF — INV-039

```text
INV_ID = INV-039
TE_STATUS = DELIVERY_PASS_R3P1
TE_RUN_ID = 20260906-1639-pouvoir-institutions-ue
TE_PATH = 2026-09-06_16-39_pouvoir-institutions-ue_INVESTIGATION.md
QRY = 16
SRC = 16
PROVENANCE_FAMILIES = 12
FCT = 19
CHECKPOINTS = 7
MNEMO = MNEMO_UNAVAILABLE degraded
PERSISTENCE = PASS / 19 blocked terminal outcomes
DELIVERABLE_SHA256 = ca5113fdeba13fe444538d3d76cc80227d811a50356a002398312d16e1838e8c
RENARD = NO
INV_STATUS = CLOSED
```

## Central delta

`CLM-001..009` remplace le classement global « qui gouverne réellement l'UE ? » par une carte **pouvoir × type de décision × phase × base juridique**. Les États gardent la frontière des compétences et certains vetos ; la Commission domine l'initiative ordinaire mais pas l'adoption seule ; Parlement et Conseil codécident sous OLP ; le Conseil européen est non-législateur en droit mais acteur d'agenda en pratique ; BCE et CJUE exercent des pouvoirs forts mais spécialisés.

`CLM-009 / CAU-001` sépare explicitement lobbying, accès et ressources d'une preuve de capture ou d'effet causal. `CAU-002` conserve la même discipline pour les mandats politiques du Conseil européen.

## Highest supported I0..I7

```text
I0 identity/relation = VERIFIED — institutions, compétences et relations procédurales
I1 resources/capability/access = VERIFIED/PARTIAL — pouvoirs juridiques et accès de lobbying documentés
I2 documented action = VERIFIED — proposition, codécision, mandats politiques, exécution/enforcement documentés
I3 coordination/tasking/control = VERIFIED uniquement pour procédures formelles; NOT_ESTABLISHED comme contrôle unifié de l'UE
I4 exposure/reach = N/A à l'objet structurel; lobbying access documented sans exposition persuasive mesurée
I5 reception/persuasion = NOT_ESTABLISHED
I6 behavior/institutional change = VERIFIED pour effets juridiques des actes; NOT_ESTABLISHED causalement pour lobbying/mandats politiques
I7 counterfactual outcome = NOT_ESTABLISHED
```

## Material gaps / contradictions

- `CAU-001` : lobbying -> contenu final / contrôle de politique, causalité non identifiée.
- `CAU-002` : mandat Conseil européen -> vitesse/contenu/adoption d'un texte, causalité générale non identifiée.
- Les équilibres varient par base juridique ; aucun score unique inter-domaines n'est construit.

## RENARD decision + reason

```text
RENARD = NO
```

Les deux gaps nécessitent un design causal ciblé, pas davantage de recherche descriptive. `INV-041` et `INV-042` sont les routes naturelles pour approfondir respectivement production réglementaire et lobbying.

## New ideas triaged

```text
Commission proposal -> final-text delta by procedure       -> MERGE vers INV-041
lobby positions/amendments -> adopted text                -> MERGE vers INV-042
European Council file-level causal trace                  -> RECHECK si claim causal devient décisif
Treaty / voting-rule reform                               -> RECHECK lors d'un changement matériel
generic extra institutional ranking                       -> DROP
```

## Registry patch

```text
INV-039 -> CLOSED
truth_engine -> DELIVERY_PASS_R3P1
renard -> NO
result_path -> INV-039_RUN_HANDOFF.md
next_action -> NONE — CLOSED; output available to INV-040; synthesis remains blocked by other constitutive investigations.
```
