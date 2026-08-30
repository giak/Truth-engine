# START HERE

## Usage le plus simple pour un article long

Fournis au modèle :

1. ce bundle ;
2. l’article à réécrire ;
3. éventuellement le `FACT_REGISTRY`, le blueprint et la charte éditoriale.

Puis donne simplement l’instruction :

> Lis `MAESTRO.md`, `LONG_FORM.md` et `prompts/REWRITE_ARTICLE.md`. Exécute le protocole LONG FORM sur l’article fourni. Utilise les fichiers du dossier `protocol/` uniquement lorsqu’ils sont requis par le workflow. Retourne uniquement l’article final complet. Ne modifie pas une formulation correcte sans gain démontrable. Ne durcis aucun fait, aucune causalité ni aucun niveau de preuve.

## Si l’article est court ou moyen

> Lis `MAESTRO.md` et `prompts/REWRITE_ARTICLE.md`. Réécris l’article et retourne uniquement le texte final.

## Si tu veux seulement un audit

> Lis `MAESTRO.md`, `prompts/LINGUIST.md` et `prompts/RED_TEAM.md`. Audite l’article sans le réécrire. Retourne uniquement les P0/P1 fondés et dédupliqués.

## Important

`tests/` contient un protocole de validation du système. Ces tests ne sont pas exécutés automatiquement par le bundle. Ils servent à comparer plusieurs modèles ou plusieurs versions de MAESTRO sur un corpus de référence.
