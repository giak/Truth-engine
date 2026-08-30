# IA & Travail — Socle de traçabilité forensique

Snapshot initial : 2026-08-25.

## Finalité

Ce socle permet de remonter d'une assertion d'article à :
source -> evidence/locator -> claim -> relation -> investigation -> fichier -> décision -> version d'article.

Le classeur `.xlsx` est le cockpit de revue. La base `.sqlite` est le registre relationnel normalisé.
Les fichiers bruts sont identifiés par SHA-256.

## Règles de gouvernance

1. SOURCE != CLAIM != EVIDENCE.
2. Une URL seule n'est pas une preuve : conserver un locator/citation courte et ce qu'elle établit.
3. Un statut importé d'une ancienne enquête reste `IMPORTED_UNREVIEWED` tant qu'il n'est pas revérifié.
4. Les sources web cardinales doivent être archivées en PDF/HTML brut avec date d'accès + SHA-256.
5. Toute assertion contestable publiée doit être mappée vers des IDs de claims/evidences.
6. Les contradictions, réfutations et preuves négatives ne sont jamais supprimées.
7. Une version d'article supersède une autre ; elle ne l'écrase pas silencieusement.
8. Tout changement éditorial ou probatoire important doit entrer dans le changelog et le registre de décisions.

## Limite actuelle importante

Le runtime ne fournit pas ici un export brut/verbatim complet de la conversation ChatGPT avec IDs de tours et timestamps.
`11_CONVERSATION` et `CURRENT_CONVERSATION_EVENTS.md` sont donc des résumés structurés produits à partir de la conversation courante.
Ils ne sont PAS présentés comme une archive verbatim.

Action P0 : exporter le chat brut dès qu'il est disponible, calculer son SHA-256, l'enregistrer dans `01_FILES`,
puis créer les arêtes `TURN -> DECISION`, `TURN -> CLAIM`, `TURN -> CHANGELOG`.

## Gates de publication initiales

Le snapshot démarre volontairement en `HOLD` :
- assertions de l'article non mappées vers les preuves ;
- tiers de sources à revoir ;
- snapshots web manquants ;
- investigations importées non revalidées dans ce build.

C'est un comportement attendu : le dashboard montre les trous au lieu de les masquer.
