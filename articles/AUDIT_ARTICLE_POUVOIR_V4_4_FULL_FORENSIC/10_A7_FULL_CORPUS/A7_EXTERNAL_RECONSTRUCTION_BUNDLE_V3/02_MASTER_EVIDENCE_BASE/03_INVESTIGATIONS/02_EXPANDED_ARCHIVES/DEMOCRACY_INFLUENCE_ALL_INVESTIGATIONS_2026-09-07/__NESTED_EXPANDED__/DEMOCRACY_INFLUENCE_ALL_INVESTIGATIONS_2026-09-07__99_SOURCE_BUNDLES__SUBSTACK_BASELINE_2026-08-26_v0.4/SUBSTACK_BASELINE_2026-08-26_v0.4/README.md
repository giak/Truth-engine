# SUBSTACK BASELINE — 2026-08-26

Baseline canonique reconstruite à partir de `substack-online(5).zip`.

- **Gel explicite :** 2026-08-26.
- **Archive source SHA-256 :** `84f3174f473bbfab6ee55aa516de613b30f35822d8779e6a71afc830bdb5d1b5`.
- **Articles canoniques publiés analysables :** **121**.
- **HTML canoniques :** **121**.
- **Objets exclus/non canoniques :** **8** (`EXCLUSIONS.csv`).

## Règle d'inclusion

Un article entre dans la baseline si et seulement si :

1. `posts.csv` indique `is_published=true` ;
2. un HTML de stem exact `post_id` existe dans le snapshot ;
3. le slug n'est pas le placeholder `coming-soon`.

Cette règle privilégie la cohérence reproductible du snapshot. Elle **ne prétend pas** représenter le Substack courant après le 26 août 2026.

## Résolutions

- `194518266.lingenierie-de-lenclos` = version canonique ; `194518266.3b3` = version orpheline conservée sous `excluded/html/`.
- `191030786.linflation-normative-francaise` = draft non publié, exclu.
- `181863121.truth-engine-lia-qui-revolutionne` = brouillon confirmé par l’utilisateur, classé `DRAFT_EXCLUDED`.
- `206006558.police-francaise-anatomie-dun-systeme` = réintégré : CSV publié + HTML présent.
- `140803312.coming-soon` = placeholder CSV sans HTML, exclu.
- Les quatre objets `index.md` sans contenu HTML/CSV restent tracés mais exclus du corpus de contenu.

## Fichiers

- `index.md` : index canonique riche, régénéré et parseable.
- `posts.csv` : métadonnées canoniques 1:1 avec `posts/*.html`.
- `posts/` : 121 HTML canoniques.
- `EXCLUSIONS.csv` : anomalies résolues / objets hors baseline.
- `excluded/html/` : bytes des HTML exclus conservés pour traçabilité.
- `MANIFEST_SHA256.csv` : hash/size de chaque artefact de baseline.
