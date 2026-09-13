# A5-S04 — Statut terminal du replay

Status: **HOLD_BEFORE_TERMINAL_DISPOSITION**

A5 ne prononce pas `PUBLISH_CANDIDATE` tant que P1-01 reste ouvert. Il ne choisit pas `MORE_INVESTIGATION` : aucun nouveau fait n'est nécessaire pour le contrat actuel. Il ne choisit pas `SHORTER_OUTPUT` ni `NO_ARTICLE` : le produit long est matériellement justifié.

```text
A2 = PASS_WITH_EXPLICIT_GAP
A3_CORPUS_YIELD_COVERAGE = PASS
A4_MATERIAL_REPLAY = PASS
A5_P0_OPEN = 0
A5_P1_OPEN = 1  # reader citation layer
A5_TERMINAL = HOLD
NEXT_OWNER = A4-S02 targeted source recovery, only for publication readiness
```
