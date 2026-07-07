# Phase 1 — Sublimator : quintessence.md d'une enquête

## Mission

À partir d'une enquête (Markdown long), produire une extraction re-structurée
de la data utile pour réfléchir plus tard à un article.

Phase 1 ne sait rien des phases suivantes. Elle ne fait que ça.

## Sortie

`investigations/<sujet>/_quintessence/<YYYY-MM-DD_HH-MM>_<sujet>_quintessence.md`.

Markdown. Sections H2. Le nombre varie selon la source, pas de quota.

## Critères de qualité [GO] Phase 1

Une quintessence est [GO] si :

1. **Fidèle** — toute data extraite correspond à une ligne de la source (mesurée via `grep -n`).
2. **Re-parcourable** — un lecteur peut naviguer la quintessence sans relire la source.
3. **Comparable** — plusieurs quintessences utilisent les mêmes dimensions nommées.

## Refus (ce que Phase 1 ne fait PAS)

- Écrire l'article.
- Proposer un angle, une thèse.
- Hiérarchiser doxa vs contre-doxa.
- Anticiper une phase suivante.
- Justifier ce qui est utile ou inutile (elle extrait, ne juge pas).

## Sortie typique

Chaque quintessence peut contenir, selon ce que la source porte :

- Métadonnées & trace source
- Faits atomiques préservés (1 fait / 1 entrée, trace `[Lxx]`)
- Acteurs nominaux
- Sources externes citées
- Chronologie datée
- Mécanismes / chaînes causales
- Verbatim et citations
- Notes méthodologiques source (si elle en a)

## Verdict [GO] Phase 1

Les 3 critères de qualité sont remplis.

## Cas-limites

- Source vide → quintessence vide mais produite (le fichier existe).
- Source sans aucune dimension identifiable → quintessence minimale avec Métadonnées & trace seulement.
- Source hors-périmètre (langue étrange, format cassé) → HALTE et signale.

## Workflow

1. `grep -n '^## \|^### ' <source>` pour mesurer les sections.
2. Pour chaque section, capturer la data verbatim ou paraphrasée stricte, en marquant la position `[Lxx]` ou `[§X.Y:Lxx]`.
3. Émettre le fichier Markdown dans `investigations/<sujet>/_quintessence/`.
4. Auditer les 3 critères de qualité.

## Historique versions

| Version | Date | Statut |
|---|---|---|
| v40 v1 | 2026-07-07 | Baseline spec 8 500 mots sur-spécifiée, anticipant Phase 2/2.5/3. |
| v40 v2 | 2026-07-07 | Refonte KISS : mission + 3 critères + refus + workflow. ~60 lignes. |
