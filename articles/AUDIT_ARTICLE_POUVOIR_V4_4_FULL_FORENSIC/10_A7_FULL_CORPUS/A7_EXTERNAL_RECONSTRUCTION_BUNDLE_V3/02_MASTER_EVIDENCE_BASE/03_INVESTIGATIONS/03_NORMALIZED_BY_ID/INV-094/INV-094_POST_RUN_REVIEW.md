---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "post_run_review"
artifact_id: "INV-094-POST-RUN-REVIEW"
version: "1.0"
status: "terminal"
updated: "2026-09-07"
inv_id: "INV-094"
---

<!-- TRACE: runtime=2.10.6/R3P1; delivery=PASS; review_scope=delta-only -->

# Post-run review — INV-094

## Verdict

```text
TRUTH_ENGINE = DELIVERY_PASS_R3P1
QRY = 14
SRC = 14
PROVENANCE_FAMILIES = 7
FCT = 28
CHECKPOINTS = 6
G0_G10 = PASS
TESTS = 140 passed / 2 skipped
PERSISTENCE = PASS / 28 terminal MNEMO_UNAVAILABLE blocks
P0 = 0
P1 = 0
P2 = 3
RENARD = NO
INV_STATUS = CLOSED_AUTHORIZED
```

## Central delta

Les régimes européens de financement politique ne traitent pas l'argent d'origine étrangère comme une catégorie juridique uniforme. Les cas étudiés montrent qu'un flux étranger peut être légal, interdit, sanctionné, opaque ou économiquement réattribué selon la source, le véhicule, la date et le droit applicable. Le prêt RN/FCRB établit un financement étranger important sans établir en lui-même tasking ou commandement politique. Le dossier AfD/Bodensee montre au contraire qu'un véhicule suisse peut masquer le donateur économique et conduire à une sanction, sans établir pour autant un principal étatique étranger.

## Highest supported I0..I7

- `I0-I4 = VERIFIED case-specifically` pour source/catégorie, véhicule, transfert, règle, contrôle et conséquence.
- `I5 = PARTIAL / NOT_ESTABLISHED generally` pour tasking, contrepartie spécifique ou commandement politique.
- `I6 = NOT_ESTABLISHED` pour persuasion électorale attribuable au financement.
- `I7 = NOT_ESTABLISHED` pour résultat électoral contrefactuel.

## P2 residuals

1. bénéficiaire économique/principal ultime non identifié dans certains montages intermédiaires ;
2. contrepartie spécifique, tasking ou quid-pro-quo généralement non établi par les seules pièces financières ;
3. exposition, persuasion et résultat électoral causal non établis.

## RENARD

`NO` — une collecte générique supplémentaire serait cumulative. Les plafonds restants demandent des pièces primaires nouvelles : bénéficiaire effectif, contrats/contreparties, pièces judiciaires ou de poursuite, ou design causal électoral.

## Routing

Delta terminal vers `INV-095`. Après fermeture d'INV-094, `INV-095` reste bloquée par `INV-119` uniquement.

## Incident de vérification tracé

La première tentative PRE a utilisé par erreur `_RUN_STATE.json` comme `--file` du gate au lieu du livrable `_INVESTIGATION.md`; elle a produit un FAIL de projection. Le fichier d'échec est conservé. Le PRE canonique a ensuite passé sur `_INVESTIGATION.md`; aucun fait ni résultat analytique n'a été modifié pour contourner ce gate.
