# A1-S04 — Provenance et mémoire

Status: **PASS_WITH_LIMITATION**

## Provenance

- Registre terminal: `INVESTIGATION_REGISTRY.csv` SHA-256 `165a29d3748c625c263fb16c433fcf2cdd8202db5edcfc31f8de6cb92cf2fb89`.
- Bundle historique 2026-09-07 utilisé uniquement comme source de fichiers déjà produits; il ne représente pas le corpus final à lui seul.
- Library utilisée pour récupérer les handoffs terminaux absents des bundles locaux.
- `INV-139` et `INV-140`: uniquement via la récupération bornée explicitement déclarée dans `INV-146_SYNTHESIS.md`; aucun détail absent n'est reconstruit.
- `INV-035`: pas de RUN_HANDOFF récupéré; seule la métadonnée de registre est conservée.

## Mémoire / représentations dérivées

`INV-133` et les synthèses intermédiaires sont utilisés comme index de relations multi-runs. Toute assertion détaillée nécessitant un cas précis doit revenir au handoff correspondant avant publication.

## Limite

Le corpus est complet au niveau du registre des 121 CLOSED et quasi-complet au niveau des handoffs PRIMARY+CASE; il n'est pas prétendu que tous les fichiers runtime bruts de chaque enquête ont été relus.
