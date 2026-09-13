---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-137-RUN-HANDOFF"
version: "1.0"
status: "closed"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-137"
---

<!-- DERIVED_FROM: te_run=20260906-2025-renseignement-executif-medias; review=INV-137_POST_RUN_REVIEW.md -->
<!-- DECISION: truth_engine=DELIVERY_PASS_R3P1; renard=NO; inv=CLOSED -->

# RUN_HANDOFF — INV-137

```text
INV_ID = INV-137
TE_STATUS = DELIVERY_PASS_R3P1
TE_RUN_ID = 20260906-2025-renseignement-executif-medias
TE_PATH = 2026-09-06_20-25_renseignement-executif-medias_INVESTIGATION.md
QRY = 18
SRC = 18
PROVENANCE_FAMILIES = 10
FCT = 23
CHECKPOINTS = 7
MNEMO = MNEMO_UNAVAILABLE degraded
PERSISTENCE = PASS / 23 blocked terminal outcomes
DELIVERABLE_SHA256 = 8dc049a5ba14faa972fd2db9f3aca2d8eeedf2954fc085900b51a4a5db92ee04
RENARD = NO
INV_STATUS = CLOSED
```

## Central delta

`CLM-001..009` remplace l'alternative binaire « renseignement vrai / propagande » par une chaîne falsifiable : `évaluation -> confiance -> sélection/déclassification -> briefing -> cadrage médiatique -> réaction -> validation/correction`. La divulgation peut être une influence stratégique volontaire et exacte; elle devient problématique lorsque provenance, confiance ou caveats sont perdus, sur-certifiés ou intentionnellement trompeurs.

Ukraine 2022 fournit le contrôle positif : l'alerte centrale d'invasion était substantiellement correcte, sans valider tous les sous-claims publics. Les « Russian bounties » fournissent le contrôle de dégradation : le récit public initial a dépassé la confiance ensuite divulguée, sans preuve d'une manipulation intentionnelle. Nord Stream montre un renseignement anonyme caveaté, partiellement corroboré ensuite au niveau participant, sans fermer le commanditaire étatique. `CAU-001..002` maintient les effets comportementaux/politiques non identifiés.

## Highest supported I0..I7

```text
I0 identity/relation = VERIFIED/PARTIAL — institutions, porte-parole et certaines chaînes de diffusion sont identifiables; sources classifiées/anonymes restent opaques
I1 resources/capability/access = VERIFIED — capacité de déclassification/briefing et accès médiatique documentés
I2 documented action = VERIFIED — disclosures, briefings, publications et corrections documentés
I3 coordination/tasking/control = VERIFIED for declared strategic disclosure Ukraine; UNKNOWN/PARTIAL for anonymous bounty/Nord Stream source intent
I4 exposure/reach = PARTIAL — large agenda/political exposure documentée qualitativement, métriques hétérogènes
I5 reception/persuasion = NOT_ESTABLISHED généralement
I6 behavior/institutional/policy change = PARTIAL/NOT_ESTABLISHED; réactions politiques observées mais effet propre non identifié
I7 counterfactual outcome = NOT_ESTABLISHED
```

## Material gaps / contradictions

- Murayev 2022 : sous-claim public non fermé par un dossier probatoire public.
- Russian bounties : confiance publique initiale > confiance ensuite divulguée; source intent/tasking non établi.
- Nord Stream : participant-level hypothesis renforcée; tasking gouvernemental ukrainien non établi.
- `CAU-001..002` : effet propre des disclosures sur opinion, sanctions, politique, dissuasion ou vote non identifié.
- Provenance : plusieurs récits dérivent de pools de renseignement classifiés ou de sources anonymes non accessibles; multiplication éditoriale != corroboration indépendante.

## RENARD decision + reason

```text
RENARD = NO
```

Les gaps exigent déclassification, décision judiciaire ou design causal. Une collecte générique supplémentaire sur les mêmes mécanismes serait cumulative.

## New ideas triaged

```text
Murayev source-level/declassified evidence       -> RECHECK si pièce nouvelle
Russian bounties full IC/source chain            -> RECHECK si déclassification
Nord Stream final judicial findings              -> RECHECK si événement matériel
counter-interference disclosure incentives       -> MERGE vers INV-144
ally/adversary disclosure standards              -> MERGE vers INV-146
quantitative caveat-survival study                -> DO futur si besoin méthodologique
more anonymous-briefing examples                  -> DROP
```

## Registry patch

```text
INV-137 -> CLOSED
truth_engine -> DELIVERY_PASS_R3P1
renard -> NO
result_path -> INV-137_RUN_HANDOFF.md
next_action -> NONE — CLOSED; disclosure/confidence model available to INV-144/146; recheck Murayev/bounties/Nord Stream only on material declassification/judicial evidence.
```
