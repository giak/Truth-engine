# Rapport d'exhaustivité — bundle maître 2026-09-11

## Verdict

Le bundle est **exhaustif sur les artefacts récupérés et les archives de programme disponibles dans cette session**, mais il ne fabrique pas les artefacts historiques qui n'ont jamais été conservés ou n'ont pas été retrouvés.

Il faut distinguer deux sens de « complet » :

- **complet comme conservation du corpus récupérable** : oui, les snapshots/archives retrouvés, les pièces directes récupérées, l'orchestrateur, le KERNEL, le corpus forensique et la préparation Article Protocol sont inclus ;
- **chaque dossier possède rétroactivement ses 6 fichiers canoniques** : non. La convention des 6 fichiers n'a pas été conservée uniformément sur toute l'histoire du programme.

## Registry final

- 147 dossiers logiques au registry final.
- 121 `CLOSED`.
- 100 `PRIMARY|CASE` fermés.
- 13 `SYNTHESIS` fermées.
- 8 `CONTROL_SPEC|STRUCTURAL` fermés.

## Couverture des 100 PRIMARY|CASE

- classes : `{'PARTIAL_MACHINE_ARTIFACTS': 63, 'HANDOFF_OR_DERIVED_ONLY': 24, 'CANONICAL_6_COMPLETE': 13}`
- dossier complet selon le canon minimal `INPUT + RUN_STATE + NARRATIVE + INVESTIGATION + MNEMO_SNAPSHOT + CERTIFICATION` : 13/100.
- `RUN_HANDOFF` récupéré : 97/100.
- document d'investigation plein/récupéré : 63/100.
- `_RUN_STATE.json` ou équivalent récupéré : 36/100.
- `_CERTIFICATION.json` récupéré : 33/100.

Dossiers actuellement identifiés `CANONICAL_6_COMPLETE` dans la vue normalisée :

`INV-022, INV-023, INV-044, INV-056, INV-078, INV-080, INV-085, INV-090, INV-096, INV-098, INV-099, INV-103, INV-143`

La ligne par ligne est dans `03_INVESTIGATIONS/INVESTIGATION_ARTIFACT_MATRIX.csv` et `CANONICAL_6_GAPS_PRIMARY_CASE.csv`.

## Corpus forensique

Le corpus V1 conserve la distinction d'autorité déjà auditée :

- 96 handoffs originaux `run_handoff` de dossiers PRIMARY/CASE ;
- 1 récupération bornée `INV-044` ;
- `INV-139` et `INV-140` bornés via `INV-146_SYNTHESIS.md` lorsque l'original indépendant n'est pas disponible ;
- `INV-035` reste absent comme artefact terminal reconstructible ;
- 13 synthèses sont des dérivés et ne créent pas de corroboration indépendante ;
- 8 objets contrôle/structure restent méthodologiques.

## Orchestrateur / control-plane

`02_ORCHESTRATOR/INVCHAIN_FINAL_2026-09-11/` conserve notamment :

- `INVESTIGATION_ORCHESTRATOR.md` ;
- `control.py` ;
- `CONTROL_STATE.json` et états historiques ;
- `INVESTIGATION_REGISTRY.csv` et snapshots `pre_*` ;
- `DASHBOARD.md` ;
- reclassifications CORE_MISSION_V2 ;
- plans de reclassification ;
- `apply` / replay logs lorsqu'ils existent ;
- dépendances, handoffs, synthèses et snapshots incorporés au control-plane.

`02_ORCHESTRATOR/RECOVERED_HISTORY/` ajoute les audits/plans récupérés hors snapshot final (`CONTROL_PLANE_AUDIT`, `REFOCUS_AUDIT`, `PROGRAM_SNAPSHOT`, `INVESTIGATION_PORTFOLIO_PLAN`, etc.).

## KERNEL

`01_KERNEL/` contient le ZIP canonique Truth Engine `2.10.6-R3P1` et sa version décompressée, dont `tools/runtime/run_state.py` et `tools/verify/verify.py`.

Certains runs historiques signalent d'autres marqueurs (notamment R2A2). Le présent bundle ne prétend pas reconstruire un KERNEL historique absent si son archive exacte n'a pas été retrouvée.

## Préparation de l'article

`05_ARTICLE_PREPARATION/` conserve trois strates :

1. run Article Protocol initial sur les 121 CLOSED ;
2. correction `CORPUS_YIELD_COVERAGE` et reconstruction A2/A3 depuis le corpus V1 ;
3. récupération des sources lecteur, replay A4-S02→A5 et candidat `PUBLISH_CANDIDATE`.

Sont inclus : matrices de couverture, contrats A3, progression A4, drafts, support maps, source maps, reviews A5, protocole patché, patch, catalogues sources, article candidat et handoff A7 froid.

## Connaissance négative à préserver

- `INV-035` : gap, pas « inexistant ».
- `INV-044` : recovery, pas original.
- `INV-139/140` : autorité bornée ; ne pas les promouvoir par répétition de synthèse.
- absence d'un JSON historique : absence de pièce récupérée, jamais autorisation d'en fabriquer un.

## Contrôle d'intégrité

- `MANIFEST_SHA256.csv` couvre chaque fichier du bundle hors le manifest lui-même au moment de sa génération.
- `03_INVESTIGATIONS/PROVENANCE_INDEX.csv` relie la vue normalisée aux archives/directories sources.
- `03_INVESTIGATIONS/SOURCE_ARCHIVES.csv` donne le SHA-256 et le résultat `ZipFile.testzip()` de chaque archive source incluse.
- les archives originales sont conservées intactes sous `03_INVESTIGATIONS/01_RAW_ARCHIVES/`.
