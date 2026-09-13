---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-081-RUN-HANDOFF"
version: "1.0"
status: "closed"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-081"
---

<!-- DERIVED_FROM: te_run=20260906-1555-propriete-medias-francais; review=INV-081_POST_RUN_REVIEW.md -->
<!-- DECISION: truth_engine=DELIVERY_PASS_R3P1; renard=NO; inv=CLOSED -->

# RUN_HANDOFF — INV-081

```text
INV_ID = INV-081
TE_STATUS = DELIVERY_PASS_R3P1
TE_RUN_ID = 20260906-1555-propriete-medias-francais
TE_PATH = 2026-09-06_15-55_propriete-medias-francais_INVESTIGATION.md
QRY = 15
SRC = 15
PROVENANCE_FAMILIES = 12
FCT = 16
CHECKPOINTS = 7
MNEMO = MNEMO_UNAVAILABLE degraded
PERSISTENCE = PASS / second terminal attempt; first PARTIAL retained in history
DELIVERABLE_SHA256 = 0fc4ee6583cdc16a5f02801795f0248c30baa437239d48871390f527f478238c
RENARD = NO
INV_STATUS = CLOSED
```

## Central delta

`CLM-001..008` remplace le slogan global « 9/11 milliardaires possèdent 80-90 % des médias » par un objet mesurable : **métrique × univers × date × définition du contrôle**. Le 91,4 % retrouvé est borné à la diffusion des quotidiens nationaux généralistes en 2021 (`CLM-002`). Les cartes historiques ne sont pas réutilisables sans recheck, notamment après le changement d'actionnariat du Groupe Le Monde (`CLM-003 / CTRL-001`).

La concentration reste matériellement documentée comme enjeu structurel (`CLM-004 / CTRL-003`) mais aucun score de risque, pourcentage d'audience, part de diffusion ou relation de financement n'est converti en « part de propriété de tous les médias ». `CLM-007 / CAU-001..002` conserve explicitement la frontière vers INV-082.

## Highest supported I0..I7

```text
I0 identity/relation = VERIFIED pour les relations juridiques/organisationnelles explicitement documentées
I1 resources/capability/access = VERIFIED/PARTIAL — propriété, actifs et financement documentent ressources/capacité, pas leur usage éditorial
I2 documented action = VERIFIED pour acquisitions/transferts/financements corporatifs ; N/A comme action d'influence
I3 coordination/tasking/control = NOT_ESTABLISHED au niveau éditorial
I4 exposure/reach = MEASURED_BY_SECTOR pour diffusion/audience ; pas une exposition d'influence attribuée
I5 reception/persuasion = NOT_ESTABLISHED
I6 behavior/institutional/electoral change = NOT_ESTABLISHED
I7 counterfactual outcome = NOT_ESTABLISHED
```

## Material gaps / contradictions

- `CLM-005`: méthodologie des chiffres parlementaires 2026 non reproduite.
- `CLM-008`: pas encore de base officielle Arcom unifiée couvrant audiovisuel + presse + online.
- `CAU-001`: propriété -> intervention/contrôle éditorial non établie ; objet aval INV-082.
- `CAU-002`: financement -> contrôle éditorial non établi sans droits/traces propres.

## RENARD decision + reason

```text
RENARD = NO
```

Les gaps centraux restants exigent soit une future publication méthodologique/base de données, soit une investigation causale distincte. Une recherche descriptive supplémentaire non bornée augmenterait surtout l'hétérogénéité des dénominateurs.

## New ideas triaged

```text
méthode source des 93% / 60% / 50% publiée       -> RECHECK
base Arcom/EMFA étendue presse + online           -> RECHECK
transaction matérielle sur groupe/titre majeur    -> RECHECK
propriété/financement -> sélection éditoriale      -> MERGE vers INV-082
nouvelle carte « milliardaires » sans dénominateur -> DROP comme preuve ; garder seulement comme LEAD
```

## Registry patch

```text
INV-081 -> CLOSED
truth_engine -> DELIVERY_PASS_R3P1
renard -> NO
result_path -> INV-081_RUN_HANDOFF.md
next_action -> NONE — CLOSED; output available to INV-082 and INV-095 when their other dependencies are satisfied.
INV-082 -> remains BLOCKED on INV-085
INV-095 -> remains BLOCKED on INV-093, INV-094, INV-119
```
