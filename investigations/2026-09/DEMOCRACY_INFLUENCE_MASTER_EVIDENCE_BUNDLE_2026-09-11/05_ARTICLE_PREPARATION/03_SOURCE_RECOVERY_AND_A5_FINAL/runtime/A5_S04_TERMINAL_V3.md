# A5-S04 — Décision terminale V3

```text
A2 = PASS_WITH_EXPLICIT_GAP
A3 = PASS
CORPUS_YIELD_COVERAGE = PASS
A4-S02 = PASS
A4-S03 = PASS_AFTER_LOCAL_REPAIR
A4-S04 = PASS
A5_P0_OPEN = 0
A5_P1_OPEN = 0
A5_P2_OPEN = 1_NON_BLOCKING
A5_TERMINAL = PUBLISH_CANDIDATE
NEXT = A7_COLD_AUDIT
```

`PUBLISH_CANDIDATE` ferme la review éditoriale A5. Il ne signifie pas `A7_CERTIFIED`, `CANONICAL` ni `PUBLISHED`. Le prochain gate légitime est l'audit froid réellement indépendant A7.
