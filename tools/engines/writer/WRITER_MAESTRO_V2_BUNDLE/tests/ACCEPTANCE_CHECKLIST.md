# ACCEPTANCE CHECKLIST

Avant de considérer le bundle ou une nouvelle version comme meilleure :

## Architecture
- [ ] Un seul WRITER modifie le texte maître.
- [ ] Les reviewers ne génèrent pas de versions concurrentes.
- [ ] Les responsabilités ne dupliquent pas le fact-checking amont.
- [ ] Les règles stylistiques quantitatives ne sont pas des objectifs.

## Long form
- [ ] Un GLOBAL_STATE est construit avant réécriture locale.
- [ ] Chaque unité locale reçoit le contexte global minimal.
- [ ] Une revue transversale existe après recomposition.
- [ ] Aucune passe générale supplémentaire n’est lancée sans défaut précis.

## Non-régression
- [ ] Les modifications substantielles passent par SEMANTIC_DIFF.
- [ ] Les modalités et degrés de certitude sont préservés.
- [ ] Les négations, exceptions et conditions sont conservées.
- [ ] Les causalités ne sont pas durcies.

## Langue
- [ ] Aucun procédé stylistique n’est obligatoire par quota.
- [ ] Une phrase longue n’est pas condamnée uniquement pour sa longueur.
- [ ] Une phrase courte n’est pas valorisée uniquement pour sa brièveté.
- [ ] Les transitions sont jugées selon leur fonction.

## Tests
- [ ] Mutation-tests exécutés sur un corpus sain.
- [ ] Faux positifs examinés.
- [ ] Régressions introduites par réparation mesurées.
- [ ] Passages protégés réellement préservés.
