# Lineage de l'article

## Versions principales

1. `2026-08-26_ia-modele-salarial-forensique_ARTICLE.md`
   - état initial de l'article, avant recentrage et investigations approfondies.

2. `2026-08-25_quand-le-travail-ne-vaut-plus-son-temps_V2.md`
   - refactor après audit P0/P1 ; version jugée trop comprimée.

3. `2026-08-25_quand-le-travail-ne-vaut-plus-son-temps_V3.md`
   - reset substantiel ; réintégration du corpus d'enquête et des figures.

4. `2026-08-25_quand-le-travail-ne-vaut-plus-son-temps_V3_1.md`
   - version de travail la plus avancée de cette archive.
   - panel de 30 cas rendu reproductible.
   - corrections P0/P1 du double-check appliquées.
   - statut canonique dans le SQLite V3.1 : `READY_FINAL_REVIEW`.

## Socle de traçabilité

Le **SQLite canonique** est celui extrait de :
`IA_TRAVAIL_V3_1_BUNDLE_2026-08-25.zip`

Contrôle :
- intégrité SQLite : `ok`
- 38 investigations
- 292 sources
- 19 événements conversationnels
- 16 enregistrements de figures
- 30 entrées de queue de corrections
- versions article : V1, V2, V3, V3.1

## Régression détectée au moment de l'archivage

Le fichier `/mnt/data/IA_TRAVAIL_TRACEABILITY_MASTER.sqlite` présent à la racine au 26 août 2026 était revenu à un état ancien :
- seulement `ART-V001`
- 33 investigations
- 232 sources
- 9 événements conversationnels
- aucune table `article_figures`
- aucune table `article_fix_queue`

Ce snapshot est conservé dans :
`04_TRACEABILITY/root_snapshot_regression/`

Il **ne doit pas** être utilisé comme état canonique.
