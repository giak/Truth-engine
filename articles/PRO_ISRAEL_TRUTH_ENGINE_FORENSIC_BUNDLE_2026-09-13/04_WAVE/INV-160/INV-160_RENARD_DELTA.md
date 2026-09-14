---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "renard_delta"
status: "terminal_bounded"
inv_id: "INV-160"
parent_run: "20260913-1303-elnet-finance-topology"
truth_engine_parent: "DELIVERY_PASS_R3P1"
renard: "DONE"
reclass_impact: "GLOBAL"
updated: "2026-09-13"
---

# RENARD DELTA — INV-160

## Autorité

Le livrable Truth Engine certifié d'INV-160 reste **immuable**. Le présent delta a été trouvé **après** la certification et n'est donc pas promu rétroactivement dans les FCT/CLM/CAU du run certifié.

## Lead matériel post-certification

Une recherche bornée ciblant les conventions de grant, comptes analytiques et financements directs d'ELNET France a retrouvé un PDF hébergé par *The Seventh Eye* qui paraît reproduire un export d'ordres/engagements publics israéliens pour 2020.

Une ligne du document indique notamment :

- entité : `ELNET DIALOGUE STRATEGIQUE` / France-Israël ;
- identifiant visible commençant par `531006`, cohérent avec le SIREN français `531006237` d'ELNET France ;
- numéro de commande : `4501854883` ;
- objet visible : `Safe & Smart City Conference` ;
- période : janvier–décembre 2020 ;
- montant : **37 664 EUR** ;
- contre-valeur affichée : **139 454,73 NIS**.

## Statut probatoire

`STRONG_DOCUMENT_LEAD / AUTHENTICITY_AND_PROVENANCE_RECHECK_REQUIRED`

Le fichier présente les caractéristiques d'un export gouvernemental israélien et fournit un numéro d'ordre précis, mais la copie inspectée est hébergée sur le CDN d'un média, pas sur un dépôt gouvernemental israélien actuellement résolu.

Par conséquent :

- `document mirror -> transaction alléguée` = **SUPPORTED AS LEAD** ;
- `source mirror -> archive gouvernementale authentifiée` = **NOT YET CLOSED** ;
- `gouvernement israélien -> ELNET France -> financement de projet 2020` = **MATERIAL IF AUTHENTICATED** ;
- `financement de projet -> commandement général d'ELNET France` = **NOT ESTABLISHED** ;
- `financement -> décision publique française` = **NOT ESTABLISHED**.

## Pourquoi cela change le portefeuille

Si la provenance du document est authentifiée, ce cas compléterait la chaîne déjà certifiée en 2025 :

`MFA israélien -> 72 000 EUR -> ELNET Europe-Israel -> événement au Sénat`

par une relation plus ancienne touchant potentiellement **l'entité française elle-même** :

`acteur public israélien -> ELNET France -> projet identifié en France/Europe`

Cela justifie un run séparé plutôt qu'une modification du FINAL d'INV-160.

## Run proposé

`INV-173 — ELNET France : financements publics israéliens directs 2020–2025`

Question :
`Quels financements publics israéliens directs ont été versés à ELNET France ou à ses entités associées, pour quels projets et livrables, et quelles relations de tasking/contrôle peuvent être établies sans généraliser d'une transaction à l'organisation entière ?`

Priorité de recherche :

1. authentifier la commande `4501854883` auprès d'une source gouvernementale ou archive indépendante ;
2. rechercher tous les ordres/contrats associés au SIREN `531006237`, à ELNET Dialogue Stratégique France-Israël et aux variantes de nom ;
3. reconstruire projets, montants, ministères, livrables et périodes ;
4. comparer aux déclarations HATVP et aux obligations de transparence applicables à la date des faits ;
5. rechercher contrats, factures, conventions ou rapports d'exécution ;
6. tester explicitement `project funding != organizational tasking`.

## Stop rule

Ne pas promouvoir la relation 2020 en FACT certifié tant que l'authenticité/provenance de l'export n'est pas suffisamment fermée.
