---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-123"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "NONE"
updated: "2026-09-12"
---

# RUN_HANDOFF — INV-123

## Certification

- Run: `20260912-0026-eucs-cloud-sovereignty-lobbying`
- Truth Engine: `DELIVERY_PASS_R3P1`
- QRY: `24` (`WEB=8`, `FETCH=16`)
- SRC: `16`; provenance families: `12`; FCT: `16`
- PRE: `PASS`, state `sha256:3ddf61d4098d646af9c726fb95d0f879cf9cebdab949510ef890f977589ba33b`
- DELIVERY: `PASS`, state `sha256:9fbde237a5295f2f54a28405c8aa893b3ca575587306ee9ac55f630f0fc318d9`
- Deliverable SHA-256: `b8989066afc0a4ebf0281bac155ce5172e5640af12786c3a07bc603ae8bdd53d`
- Persistence: `eligible=16 / attempted=0 / success=0 / failure=0 / blocked=16 / MNEMO_UNAVAILABLE`

## Delta central

Le cas EUCS établit une chaîne d'influence normative plus forte qu'une simple proximité : AWS a déclaré dans un registre officiel un objectif explicite de suppression des exigences de souveraineté ; des coalitions industrielles ont mené des démarches publiques et transatlantiques convergentes ; le draft 2024 a ensuite évolué dans le sens demandé.

Cela ferme `intérêt commercial -> lobbying explicite -> cible normative -> delta de texte congruent`.

Cela ne ferme pas `lobbying -> cause déterminante du delta`. Les positions des États membres, des clients cloud et des fournisseurs européens étaient divisées, et aucun objet décisionnel inspecté n'alloue le poids causal du changement à AWS/BSA/CCIA plutôt qu'aux autres préférences et arbitrages.

## Verdict causal

- `AWS -> objectif explicite de lobbying pour retirer les critères` = **SUPPORTED**.
- `coalitions industrielles -> pression répétée/multi-canal` = **SUPPORTED**.
- `EUCS 2024 -> retrait des critères de souveraineté` = **SUPPORTED_AS_DRAFT_DELTA**.
- `lobbying -> policy-delta congruence` = **SUPPORTED**.
- `Big Tech lobbying -> cause déterminante du retrait` = **NOT_ESTABLISHED / CAUSALITY_GAP**.
- `capture` = **NOT_ESTABLISHED**.
- `corruption / quid pro quo` = **REFUTED_IN_SCOPE**.
- `retrait 2024 -> abandon permanent de souveraineté cloud` = **REFUTED_BOUNDED**, au regard de l'architecture de souveraineté appliquée par la Commission en 2026.

## Reopen

Réouvrir uniquement sur : minutes/positions ECCG, justification interne ENISA/Commission, logs de réunions actor-specific, ou autre pièce permettant d'attribuer marginalement le changement du texte.
