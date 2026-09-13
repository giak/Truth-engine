# A7 — Décision composée

## État

```text
A7-S01 FOUNDATIONAL FIXTURES = PASS_BOUNDED
A7-S02 REAL DOSSIER REPLAY   = PASS_INTERNAL
A7-S03 ADVERSARIAL REGRESSION = PASS_INTERNAL (9/9)
A7-S04 EXTERNAL COLD AUDIT    = HOLD_EXTERNAL_COLD_AUDIT_ONLY

P0_OPEN = 0
P1_OPEN = 0
P2_OPEN = 1
```

## Décision

**HOLD_EXTERNAL_COLD_AUDIT_ONLY**

Le produit est `PUBLISH_CANDIDATE` au sens A5, mais il n'est pas promu `VALIDATED_CANDIDATE` par A7 tant qu'un contexte réellement frais n'a pas rendu `A7-S04 = PASS_EXTERNAL_COLD`.

Aucune investigation supplémentaire n'est justifiée par ce hold : il s'agit d'une dépendance de validation, pas d'un gap de matière.
