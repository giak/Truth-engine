# Audit exhaustif des 121 CLOSED — reconstruction du corpus forensique

Date: 2026-09-11

## Verdict

Le libellé **« 121 artefacts forensiques » est faux**. Il y a **121 dossiers logiques CLOSED**, mais ils ne sont ni 121 artefacts physiques uniques ni 121 unités de preuve équivalentes.

Le corpus reconstruit distingue:

- **96** `run_handoff` originaux de PRIMARY/CASE: noyau de résultats forensiques de premier ordre dans le projet.
- **1** récupération bornée `INV-044`: `recovery_handoff` construit depuis le terminal narrative, pas handoff terminal original.
- **2** récupérations bornées `INV-139` et `INV-140`: seulement via `INV-146_SYNTHESIS.md`; aucune indépendance supplémentaire.
- **1** PRIMARY sans artefact terminal récupéré: `INV-035`; exclu de la preuve.
- **13** SYNTHESIS: couche dérivée, utile pour relations/compression, **pas preuve indépendante nouvelle**.
- **8** CONTROL/STRUCTURAL: méthode et contrôle, pas preuve de cas; physiquement ils se réduisent à 3 fichiers (`INV-001`, `INV-002`, `METHOD_PACK.md`).

Ainsi, les 121 lignes logiques sont mappées vers **113 fichiers physiques présents** dans la reconstruction, avec `INV-035` explicitement absent.

## Audit d'intégrité

- CLOSED dans le registre: **121/147**.
- Répartition CLOSED: {'STRUCTURAL': 2, 'CONTROL_SPEC': 6, 'PRIMARY': 87, 'CASE': 13, 'SYNTHESIS': 13}.
- IDs A1 vs registre CLOSED: **121/121 exacts**, aucun doublon d'ID.
- Dépendances CLOSED -> CLOSED: **cohérentes** dans le contrôle structurel effectué.
- `result_path` distincts dans le registre: **116** seulement pour 121 lignes, notamment parce que `INV-003..008` partagent le même METHOD_PACK.
- `result_path` physiquement présent dans le bundle gelé du 11/09: **49/121**; le bundle n'est donc pas autoportant pour le corpus CLOSED.
- Handoffs PRIMARY/CASE récupérés localement pendant l'audit: **97/97** fichiers attendus par la couche A1, mais l'un d'eux (`INV-044`) est explicitement un recovery handoff.
- Correspondance `inv_id` interne / nom du dossier sur ces 97 fichiers: **97/97**.
- Marqueur Truth Engine du handoff compatible avec le registre: **97/97**.
- Duplicats binaires parmi les 97 fichiers récupérés: **0**.
- Handoffs sans SHA-256 historique embarqué: **19/97**. Le nouveau manifest SHA-256 fixe l'intégrité à partir de cette reconstruction, sans prétendre recréer une chaîne historique absente.

## Défauts de la réduction A1

A1 est un index de navigation dérivé, pas le corpus probatoire canonique:

- `summary` vide à l'origine: **10/121**: INV-018, INV-044, INV-078, INV-085, INV-089, INV-091, INV-098, INV-099, INV-100, INV-143.
- `edge` vide: **108/121**.
- `gaps` vide: **32/121**.
- Les **10** summaries manquants de PRIMARY/CASE ont été récupérés depuis leurs handoffs bruts lorsque possible: INV-018, INV-044, INV-078, INV-085, INV-089, INV-091, INV-098, INV-099, INV-100, INV-143.
- Les champs A1 ne sont jamais promus au rang de preuve indépendante; ils restent des aides de navigation.

## Provenance réellement observée

- BOUNDED_SYNTHESIS_RECOVERY: **2**
- DERIVED_SYNTHESIS: **13**
- DIRECT_CURRENT_BUNDLE: **36**
- DIRECT_HISTORICAL_BUNDLE: **17**
- DIRECT_LIBRARY_RECOVERY: **44**
- METHOD_CONTROL: **6**
- MISSING_HANDOFF: **1**
- STRUCTURAL_CONTROL: **2**

## Règles canoniques du corpus reconstruit

1. `CLOSED` signifie état de workflow, pas force probatoire.
2. `TERMINAL_INVESTIGATION_HANDOFF` peut porter le résultat d'une investigation, mais plusieurs dossiers ne valent jamais corroboration indépendante par simple comptage.
3. `DERIVED_SYNTHESIS` ne crée aucune preuve nouvelle.
4. `BOUNDED_RECOVERY_*` ne doit jamais être présenté comme artefact terminal original ni corroboration indépendante.
5. `CONTROL_*` sert à la méthode, aux taxonomies et aux garde-fous, pas à établir un fait de cas.
6. `INV-035` reste une lacune explicite; aucune reconstruction sémantique n'est autorisée en son absence.
7. Absence de preuve / artefact introuvable n'est jamais convertie en preuve d'absence.
8. La source canonique d'un claim reste la chaîne de sources/faits de l'investigation; le handoff est le résultat terminal, pas une pièce primaire externe.

## Corpus à utiliser désormais

Pour une analyse forensique nouvelle:

- **Tier A**: les 96 handoffs originaux (`01_TERMINAL_RESULTS`).
- **Tier B**: `INV-044` dans `02_BOUNDED_RECOVERY`, utilisable uniquement avec son plafond explicite.
- **Tier C**: `INV-139/140` uniquement par les passages attribués dans `INV-146_SYNTHESIS.md`; aucune extrapolation.
- **Tier D**: les 13 synthèses pour navigation/relations, jamais comme double comptage de preuve.
- **Tier M**: les 3 artefacts de contrôle couvrant 8 dossiers logiques.
- **Tier X**: `INV-035`, exclu tant que l'artefact terminal n'est pas retrouvé.

Le fichier `CORPUS_121_AUDIT.csv` conserve les 121 lignes logiques et leur classe d'autorité. `SOURCE_INDEX.csv` déduplique les fichiers physiques. `MANIFEST_SHA256.csv` rend la reconstruction vérifiable byte-for-byte.
