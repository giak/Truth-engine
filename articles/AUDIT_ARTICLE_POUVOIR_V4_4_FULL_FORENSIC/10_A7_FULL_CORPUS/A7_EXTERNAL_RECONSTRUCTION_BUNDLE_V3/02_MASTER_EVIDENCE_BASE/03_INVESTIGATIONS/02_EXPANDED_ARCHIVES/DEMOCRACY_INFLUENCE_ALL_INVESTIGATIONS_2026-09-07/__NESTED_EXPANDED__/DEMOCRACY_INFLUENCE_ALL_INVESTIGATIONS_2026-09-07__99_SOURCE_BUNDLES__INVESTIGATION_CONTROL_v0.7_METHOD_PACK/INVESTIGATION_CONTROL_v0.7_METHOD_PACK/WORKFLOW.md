# INVESTIGATION CONTROL — Workflow canonique

## Principe

Une seule source de vérité : `INVESTIGATION_REGISTRY.csv`.

`DASHBOARD.md` est **généré** depuis le registre. Ne pas l’éditer à la main.
`TRACELOG.md` est append-only et ne duplique pas les logs internes de Truth Engine.

## États

`IDEA -> BACKLOG -> READY -> TE_ACTIVE -> TE_DONE -> CLOSED`

Branches possibles après `TE_DONE` :

- `RENARD_REQUIRED -> RENARD_ACTIVE -> RENARD_DONE -> CLOSED`
- `MERGED` : doublon absorbé par une autre investigation.
- `DEFERRED` : utile mais non prioritaire.
- `DROPPED` : faible valeur / hors sujet / redondant.
- `BLOCKED` : dépendance non satisfaite.

## Triage obligatoire de toute idée

Chaque nouvelle idée est ajoutée **dans le même registre** avec `kind=IDEA`, puis évaluée avant exécution :

- `coverage_initial` : `NEW | PARTIAL | SUBSTANTIAL_PRIOR | UNKNOWN` ;
- `decision` : `DO | RECHECK | MERGE | DEFER | DROP | TRIAGE` ;
- `depth` : `DEEPEN | RECHECK | ENOUGH | UNKNOWN` ;
- `priority` : `P0 | P1 | P2` ;
- `dependencies` ;
- justification courte dans `notes`.

Aucune idée n’est lancée tant que `decision=TRIAGE`.

## Ordre minimal

1. `INV-001` intégrité corpus.
2. `INV-002` cartographie corpus.
3. Requalifier **toutes** les lignes `evaluation=PROVISIONAL` en `CONFIRMED` ou les modifier.
4. Lancer les investigations P0/P1 par dépendance et valeur discriminante.
5. Après chaque run : mettre à jour le registre + une ligne macro dans `TRACELOG.md`.

## Truth Engine

Truth Engine reste le moteur d’investigation primaire. Ne pas recopier ses QRY/SRC/FCT/logs dans ce projet : stocker seulement le chemin/référence du résultat.

Exception W0 : les audits purement structurels de fichiers/corpus (`INV-001` notamment) sont exécutés directement sur les artefacts. Ne jamais prétendre à un run Truth Engine si son runtime canonique n’a pas été exécuté ; utiliser `truth_engine=N/A_STRUCTURAL`.

## RENARD — usage delta-only

RENARD n’est **pas automatique**. Il est déclenché après Truth Engine seulement si au moins un critère est vrai :

1. gap matériel P0/P1 encore ouvert ;
2. causalité, intention, coordination ou impact central insuffisamment discriminé ;
3. claim central dépend d’une seule famille probatoire ;
4. contradiction/résiduel inattendu susceptible de changer le modèle ;
5. investigation à fort enjeu dont le résultat reste fragile au test adversarial ;
6. nouvelle piste à fort `model_change` découverte en fin de run.

Sinon `renard=NO` et on ferme : ne pas approfondir pour approfondir.

## Fermeture d’une investigation

`CLOSED` seulement si :

- résultat Truth Engine enregistré ;
- décision RENARD prise ;
- gaps matériels restants explicités ;
- nouvelles idées issues du run ajoutées au registre et triées au moins en `IDEA` ;
- `next_action` vide ou explicite vers une dépendance suivante.

## Après INV-002

`coverage_initial` conserve la qualification du brainstorm initial. `coverage_current` est la qualification corpus-aware courante. Après INV-002, ne modifier que `coverage_current`; préserver `coverage_initial` pour la trace.

`HUMAN_REVIEW_INV-002` est un gate explicite : aucune investigation P0 suivante n’est lancée avant revue de la cartographie.
