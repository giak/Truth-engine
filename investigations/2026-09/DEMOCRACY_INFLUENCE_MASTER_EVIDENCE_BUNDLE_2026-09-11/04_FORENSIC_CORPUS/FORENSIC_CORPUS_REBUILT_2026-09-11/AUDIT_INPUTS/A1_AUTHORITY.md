# A1-S01 — Entrée et autorité

Status: **PASS**
Date: 2026-09-11
Protocol: ARTICLE_PROTOCOL EA-R2
Project: democracy-influence-investigations

## Surface active

- Registre terminal canonique: `/mnt/data/DEMOCRACY_INFLUENCE_COMPLETE_BUNDLE_2026-09-11/invchain/INVESTIGATION_REGISTRY.csv`
- Registre SHA-256: `165a29d3748c625c263fb16c433fcf2cdd8202db5edcfc31f8de6cb92cf2fb89`
- Dossiers `CLOSED`: **121 / 147**.
- Répartition CLOSED: `CASE`=13, `CONTROL_SPEC`=6, `PRIMARY`=87, `STRUCTURAL`=2, `SYNTHESIS`=13.
- PRIMARY+CASE CLOSED: **100**.
- RUN_HANDOFF terminaux directement inspectables pour PRIMARY+CASE: **97/100**.
- Récupérations bornées autorisées par synthèse terminale: `INV-139`, `INV-140` via `INV-146`.
- Handoff primaire non récupéré: `INV-035`. Son absence reste une limite de provenance; aucun contenu n'est reconstruit.
- Synthèses terminales actives: **13** (`INV-038, 040, 052, 068, 082, 088, 095, 102, 104, 129, 133, 144, 146`).
- Quintessences A1: `A1_QUINTESSENCES.json/csv/md` = **121 entrées**, une par dossier CLOSED.

## Hiérarchie d'autorité utilisée

1. Investigation/handoff terminal PRIMARY ou CASE pour les résultats propres au run.
2. Synthèse terminale pour les relations multi-investigations, sans promotion de statut.
3. Registre terminal pour identité, type, statut, dépendances et routing.
4. CONTROL_SPEC / STRUCTURAL pour méthode et contrôle, pas comme preuves du fond.
5. Les quintessences sont des représentations dérivées de navigation; elles ne créent aucune corroboration indépendante.

## Gardes

- `121 CLOSED != 121 corroborations indépendantes`.
- `SYNTHESIS != nouvelle preuve`.
- `FINAL/CLOSED != exhaustivité`.
- `NON_ETABLI != ABSENT`.
- `Handoff absent != contenu deviné`.

## Verdict

La surface est suffisante pour exécuter A2 honnêtement. La lacune `INV-035` est visible et non bloquante tant qu'aucune assertion A2 ne dépend exclusivement d'elle.
