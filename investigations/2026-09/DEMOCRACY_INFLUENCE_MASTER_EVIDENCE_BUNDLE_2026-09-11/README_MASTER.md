# DEMOCRACY INFLUENCE MASTER EVIDENCE BUNDLE — 2026-09-11

## Objet

Bundle maître de conservation et de reprise du programme d'investigations sur les mécanismes d'influence / ingérence démocratique et de la préparation de l'article.

Il rassemble, sans fabriquer les pièces absentes :

1. le KERNEL Truth Engine canonique `2.10.6-R3P1` ;
2. le control-plane / orchestrateur final et son historique récupéré ;
3. les archives d'investigations disponibles, y compris le snapshot maître du 2026-09-07 et les bundles canoniques postérieurs ;
4. une vue normalisée par `INV-xxx`, dédupliquée par SHA-256 mais reliée à chaque provenance ;
5. le corpus forensique V1 reconstruit ;
6. Article Protocol, A1→A5, patch `CORPUS_YIELD_COVERAGE`, source recovery lecteur et candidat `PUBLISH_CANDIDATE` ;
7. les scripts et rapports d'audit utilisés pour la reconstruction/replay.

## Règle d'intégrité

`ABSENT != RECONSTRUIT`. Aucune pièce machine absente n'a été synthétisée pour compléter artificiellement un dossier.
Les doublons binaires sont conservés dans les archives originales et dédupliqués uniquement dans `03_NORMALIZED_BY_ID`, avec traçabilité dans `PROVENANCE_INDEX.csv`.

## Couverture registry

- lignes registry : 147
- CLOSED : 121
- classes tous dossiers : {'PARTIAL_MACHINE_ARTIFACTS': 81, 'NO_ARTIFACT_RECOVERED': 26, 'HANDOFF_OR_DERIVED_ONLY': 27, 'CANONICAL_6_COMPLETE': 13}
- classes CLOSED : {'PARTIAL_MACHINE_ARTIFACTS': 81, 'HANDOFF_OR_DERIVED_ONLY': 27, 'CANONICAL_6_COMPLETE': 13}
- types : {'STRUCTURAL': 2, 'CONTROL_SPEC': 6, 'PRIMARY': 99, 'CASE': 13, 'MERGED': 6, 'SYNTHESIS': 13, 'DEFER_CONTEXT': 1, 'CONDITIONAL_CASE': 7}

La matrice exacte est `03_INVESTIGATIONS/INVESTIGATION_ARTIFACT_MATRIX.csv`.

## Structure

- `01_KERNEL/` — Truth Engine canonique + version décompressée.
- `02_ORCHESTRATOR/` — `control.py`, `INVESTIGATION_ORCHESTRATOR.md`, `CONTROL_STATE.json`, registry, dashboard, reclassifications, apply/replay logs et historique récupéré.
- `03_INVESTIGATIONS/01_RAW_ARCHIVES/` — archives originales intactes.
- `03_INVESTIGATIONS/02_EXPANDED_ARCHIVES/` — contenu de chaque archive séparé par provenance.
- `03_INVESTIGATIONS/03_NORMALIZED_BY_ID/` — vue de travail par investigation, sans effacer les versions divergentes.
- `04_FORENSIC_CORPUS/` — corpus V1 reconstruit et audit 121.
- `05_ARTICLE_PREPARATION/` — Article Protocol et replays jusqu'à A5.
- `06_BUILD_AND_AUDIT/` — scripts et catalogues ayant servi à la reconstruction.

## Limites connues

- `INV-035` demeure un gap historique : aucun artefact terminal n'a été retrouvé dans le corpus V1.
- `INV-044` comporte une récupération bornée, pas un original `run_handoff`.
- `INV-139` et `INV-140` restent bornés via la synthèse `INV-146` lorsqu'aucun original indépendant n'est disponible.
- Tous les dossiers n'ont pas leurs six fichiers canoniques machine. Le statut exact est déclaré par dossier dans la matrice ; aucune absence n'est masquée.
- Les 13 synthèses et les artefacts de contrôle/méthode ne constituent pas de nouvelles corroborations indépendantes.
- A7 froid n'est pas simulé : le dernier état Article Protocol reste `PUBLISH_CANDIDATE -> A7_COLD_AUDIT`.
