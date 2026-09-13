# A7-S04 — Audit froid

Status: **HOLD_EXTERNAL_COLD_AUDIT_ONLY**

## Ce qui est fait

Un handoff froid spécifique au produit a été construit dans :

`/mnt/data/article_run/A7_COLD_PRODUCT_HANDOFF_INGERENCES/`

Il contient uniquement :

- la vue publication de l'article ;
- VISION ;
- PFD ;
- l'index des 13 sources publiques visibles ;
- un prompt d'audit produit ;
- les métadonnées/hashes nécessaires à l'intégrité du handoff.

Il exclut volontairement : protocole d'implémentation, runtime state, support map, audits internes, réparations, anciens verdicts et trace graph.

`VERIFY_HANDOFF.py` : **PASS** sur produit, VISION, PFD, footnotes, absence d'historique d'implémentation et présence des fichiers requis.

## Limite

Cette session ne peut pas produire un audit réellement indépendant d'elle-même. Une nouvelle passe ici serait `PASS_INTERNAL_NOT_INDEPENDENT`, interdite comme substitut d'A7-S04.

## Gate

```text
A7-S04 = HOLD_EXTERNAL_COLD_AUDIT_ONLY
VALIDATED_CANDIDATE = NOT_YET
PUBLICATION_AUTHORIZATION_BY_A7 = BLOCKED
```
