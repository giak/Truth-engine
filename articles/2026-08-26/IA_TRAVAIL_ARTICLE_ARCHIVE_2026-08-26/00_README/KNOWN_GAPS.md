# Gaps et limites de l'archive

## 1. Conversation brute
Le transcript verbatim complet de ChatGPT n'est pas exportable depuis l'environnement actuel.
Disponible : `05_CONVERSATION/CURRENT_CONVERSATION_EVENTS.md`, qui est une synthèse structurée.

## 2. Snapshots web immuables
Le registre contient de nombreuses URLs et statuts de vérification, mais la majorité des pages web n'ont pas de snapshot local immuable.
La colonne `archive_snapshot` de la base contient encore de nombreux `MISSING`.

Conséquence :
- les raisonnements et URLs sont archivés ;
- la preuve web brute hors ligne n'est pas complète.

## 3. Recherches web intermédiaires
Les pages de résultats de recherche et réponses des moteurs/outils ne sont pas toutes conservées comme fichiers autonomes.
Les résultats importants ont été remontés dans les rapports, le dashboard et la base.

## 4. Images
Les images retenues et plusieurs itérations rejetées disponibles localement sont incluses.
Les métadonnées internes complètes du moteur d'image ne sont pas toutes exportées comme fichiers séparés.

## 5. État canonique
Utiliser le SQLite dans `04_TRACEABILITY/canonical_v3_1/`.
Le SQLite dans `root_snapshot_regression/` est volontairement conservé comme trace d'une régression de version.
