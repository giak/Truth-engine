---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "post_run_review"
artifact_id: "INV-079-POST-RUN-REVIEW"
version: "1.0"
status: "terminal"
updated: "2026-09-07"
inv_id: "INV-079"
---

<!-- TRACE: runtime=2.10.6/R3P1; delivery=PASS; review_scope=delta-only -->
<!-- INCIDENT: persistence_attempt_001=PARTIAL; cause=wrong_writeback_action_for_FCT-004,FCT-010,FCT-028+missing_degraded_flag; persistence_attempt_002=PASS; facts_changed=NO -->

# Post-run review — INV-079

## Verdict

```text
TRUTH_ENGINE = DELIVERY_PASS_R3P1
QRY = 17
SRC = 14
PROVENANCE_FAMILIES = 6
FCT = 28
CHECKPOINTS = 6
G0_G10 = PASS
TESTS = 140 passed / 2 skipped
PERSISTENCE = PASS / attempt 2 / 28 terminal MNEMO_UNAVAILABLE blocks
P0 = 0
P1 = 0
P2 = 3
RENARD = NO
INV_STATUS = CLOSED_AUTHORIZED
```

## Central delta

Le corpus établit un écosystème public réel, récurrent et matériellement financé en France et dans l’UE pour la lutte contre la haine et les discriminations, la prévention de la radicalisation, l’éducation aux médias et la résilience face à la désinformation. Les dispositifs étudiés définissent des priorités, sélectionnent des bénéficiaires ou prestataires, financent des capacités et exigent des livrables, du reporting ou des indicateurs.

Ce résultat ferme `financement public -> sélection -> capacité/livrables` dans plusieurs programmes. Il ne ferme pas une chaîne générale `financeur public -> consigne de contenu -> décision de modération/suppression -> persuasion -> résultat politique`. Les architectures diffèrent en outre entre subvention, appel à projets et marché public : `grant != procurement` et `funding != command` restent matériels.

Conclusion bornée : **économie publique de capacité contre haine/radicalisation/désinformation = ESTABLISHED ; commandement éditorial ou de modération transversal et effet politique causal = NOT_ESTABLISHED.**

## Highest supported I0..I7

- `I0 = VERIFIED` : autorités, programmes, bénéficiaires/catégories et relations formelles.
- `I1 = VERIFIED` : budgets, ressources, capacités et critères de financement.
- `I2 = VERIFIED` : appels, subventions, marchés/relations de programme et livrables documentés.
- `I3 = VERIFIED/PARTIAL bounded` : règles et tasking de programme ; tasking caché au niveau d’un contenu spécifique non établi.
- `I4 = VERIFIED/PARTIAL` : capacité, production, formation, outils ou exposition prévue ; effet uniforme non établi.
- `I5 = NOT_ESTABLISHED generally` : commandement éditorial/modération ou réception politique.
- `I6 = NOT_ESTABLISHED` : changement comportemental politique causal.
- `I7 = NOT_ESTABLISHED` : résultat politique/électoral contrefactuel.

## P2 residuals

1. datasets complets par bénéficiaire, concentration des financements, taux de renouvellement et dénominateurs candidatures/rejets ;
2. contrats, instructions ou workflows plateforme permettant de tester `financeur -> organisation -> output -> décision de modération` au niveau d’un contenu ;
3. chaîne causale `financement/capacité -> exposition -> persuasion/comportement -> résultat` non fermée.

## Incident de persistance

L’essai de persistance n°1 a produit `PARTIAL` : trois faits de tier `✧` avaient reçu l’action `ELIGIBLE:CONFIRME` au lieu de `ELIGIBLE:VERIFIE`, et le flag runtime `MNEMO_UNAVAILABLE` n’était pas encore inscrit. Aucun fait, source ou verdict analytique n’a été modifié. L’essai n°2 corrige uniquement cette sérialisation et passe ; l’historique des deux tentatives et les deux `PERSIST_REBIND` restent dans le RUN_STATE.

## RENARD

`NO` — les plafonds restants exigent des jeux de données bénéficiaires, contrats/instructions internes ou designs causaux. Ajouter des exemples publics similaires serait cumulatif.

## Routing

Delta terminal vers `INV-088` et `INV-144`.
