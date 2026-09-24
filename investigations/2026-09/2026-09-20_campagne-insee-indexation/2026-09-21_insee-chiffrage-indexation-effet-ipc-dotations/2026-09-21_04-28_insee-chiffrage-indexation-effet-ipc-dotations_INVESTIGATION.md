ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260921-0428-insee-chiffrage-indexation-effet-ipc-dotations | PARENT_RUN_ID:20260920-1704-insee-biais-modes-calcul-fresque-systemique | AS_OF:2026-09-21
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-21_insee-chiffrage-indexation-effet-ipc-dotations/2026-09-21_04-28_insee-chiffrage-indexation-effet-ipc-dotations_INPUT.md | SUBJECT_SLUG:insee-chiffrage-indexation-effet-ipc-dotations | SUBJECT_FP:sha256:d32617f51646098fea268ccef580e2ec0fcee6db82505665ef15bcb1182083ef | INPUT_SHA256:sha256:dbf62f25134f46b6e5f3b8e421966243a68a1da96ffca61ac8882542d1eeebb4
COMPLEXITY:9→APEX | CHECKPOINT_SEQ:8 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:lead_question:que fait un dixieme de point d IPC sur les montants indexes, et que vaut un ecart d estimation de population legale sur une dotation reelle ? | object_question:quels effets chiffres les choix de mesure de la statistique publique produisent-ils sur les montants legaux qui en dependent, et avec quelle chaine de calcul documentee ? | period:1946-2027 (formules en vigueur 2025-2027 ; series de revisions 2005-2026) | geo:France (metropole ; Mayotte signalee quand pertinente) + cadre europeen (reglement UE) | domains:indexation legale, finances publiques, dotations aux collectivites, dette indexee, droit statistique | actors_entities:Insee, Cour des comptes, Agence France Tresor, DGFiP, DGCL, ministere de l Economie, CNERP, communes | exclusions:debat politique sur le niveau du chomage, theorie du complot sans appui documente, simulations non publiques | limits:aucune simulation interne a l administration n est accessible ; les montants consolides des indexations ne font pas l objet d une publication unique identifiee
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/INVESTIGATION.md,protocol/FACT_VERIFICATION.md,protocol/UPDATE.md,search/EPISTEMIC.md,search/TEMPLATES.md,output/TEMPLATE.md,clusters/ICEBERG.md,clusters/MONEY.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Ce que fait un dixième de point d'inflation sur les montants indexés, et ce que vaut un écart de population légale sur une dotation (UPDATE du run 19-21 et du run 17-04)

## TL;DR

Le gap de chiffrage hérité du run 17-04 (`CAU-002`, type `ACCESS`) est **traité et refermé en tant que question** : le coût de l'inflation sur les montants indexés est chiffré, par canal, dans une publication de référence. Deux canaux sur cinq sont chiffrés, **dans les unités publiées par la source** : environ **5 Md€ de prestations sociales par point d'inflation** (presque 0,2 point de PIB) et **0,3 Md€ de charge d'intérêts par dixième de point**, l'équivalent de 3 Md€ par point, sur une base d'environ **500 Md€** de prestations indexées (`FCT-009`). Les trois autres canaux — loyers révisés par l'IRL, dotations aux collectivités, masse salariale au SMIC — **ne sont pas chiffrés dans la documentation publique identifiée**, et ce run ne les comble pas par une estimation propre.

Le second gap hérité, la valeur d'un écart d'estimation de population légale sur une dotation réelle, est **refermé par une pièce** : un écart de plus de 15 % entre l'estimation de l'Insee (678 habitants) et le dénombrement municipal (791) a **pénalisé une commune identifiée** via sa dotation globale de fonctionnement, chiffre porté par la réponse ministérielle elle-même (`FCT-004`).

Deux gaps `ACCESS` ouverts depuis trois runs de la ligne sont fermés à la source : la **loi du 7 juin 1951** (article 1 : indépendance professionnelle, Autorité de la statistique publique) et le **règlement (UE) 2019/1700** (précision, actualité et comparabilité parmi les exigences de qualité).

## 1. RÉSUMÉ EXÉCUTIF

L'objet de ce run n'est pas de dénoncer l'indexation mais de **mesurer ce qui est mesurable**. La chaîne est documentée à ses deux bouts, et c'est ce qui la rend décisive : d'un côté la formule est écrite dans un texte opposable, de l'autre le montant est publié.

| Maillon | Ce qui est établi | Pièce |
|---|---|---|
| Formule légale | Le SMIC est revalorisé au 1er juin 2026 à **12,31 € l'heure** (2,41 %), par déclenchement du mécanisme automatique lié à l'indice des prix des ménages modestes | `FCT-003` |
| Formule légale | L'IRL est obtenu de la **moyenne de l'évolution des prix à la consommation hors tabac et hors loyers** sur 12 mois (article 17-1 de la loi du 6 juillet 1989) | `FCT-001`, `FCT-002` |
| Montant chiffré | Environ **500 Md€** de prestations sociales indexées, pour un coût d'indexation d'environ **5 Md€ par point** d'inflation | `FCT-009` |
| Montant chiffré | Environ **0,3 Md€** de charge d'intérêts par dixième de point | `FCT-009` |
| Effet sur un destinataire | Écart de population de plus de 15 % et effet direct sur la dotation d'une commune identifiée | `FCT-004` |
| Méthode | Décalage de trois ans des populations de référence, réduction à deux ans recommandée et datée fin 2026 | `FCT-005`, `FCT-006` |
| Encadrement | Indépendance et qualité comme obligations de droit, non comme pratiques déclaratives | `FCT-007`, `FCT-008` |

Il n'y a **aucun dispositif rhétorique de manipulation** dans le corpus : `DEM 0`, `BF 0`, `NUM 0`. Les écarts constatés sont des choix méthodologiques publics, opposables et attribuables. C'est la raison pour laquelle la carte dialectique porte sur l'ampleur, pas sur l'intention.

## 2. MANIPULATION_REPORT

Verdict : `NONE_DOCUMENTED`. Aucun marqueur de manipulation documentaire ou rhétorique n'a été identifié dans les pièces inspectées.

Ce qui se présente parfois comme un « angle » dans ce dossier n'est pas un dispositif de persuasion mais une **caractéristique de conception**, énoncée sans détour par les sources elles-mêmes :

- l'IRL est calculé sur un indice qui **exclut les loyers** (`FCT-002`) : l'instrument qui indexe les loyers ne contient pas les loyers dans son panier ;
- le montant **consolidé** de l'indexation ne fait l'objet d'aucune publication unique identifiée : le chiffrage existe, par canal, dans une note d'une institution financière publique, pas dans un document de synthèse.

Ces deux éléments sont vérifiables par quiconque, et opposables. Ils ne sont pas présentés ici comme la preuve d'une intention, jamais attribuée dans ce run.

## 3. LEADS (LED-001 à LED-007)

Sept leads ont été ouverts, six saturés, un laissé en gap typé.

- `LED-001` — **Saturé.** Le gap de chiffrage hérité est traité par une publication de référence : environ 5 Md€ de prestations par point d'inflation et 0,3 Md€ de charge d'intérêts par dixième de point.
- `LED-002` — **Saturé.** L'IRL est calculé sur un indice hors loyers, règle énoncée à l'identique par l'administration et par un organisme tiers.
- `LED-003` — **Saturé.** Revalorisation du SMIC de 2,41 % au 1er juin 2026, actée par arrêté inspecté à la source.
- `LED-004` — **Saturé.** Écart d'estimation de population supérieur à 15 %, effet sur la dotation, commune identifiée.
- `LED-005` — **Saturé.** Décalage de trois ans des populations de référence, réduction à deux ans recommandée et datée.
- `LED-006` — **Saturé.** La précision et l'indépendance sont des obligations juridiques inspectées à la source.
- `LED-007` — **Gap `ACCESS`.** Les canaux IRL, dotations et SMIC ne sont pas chiffrés dans la documentation publique identifiée.

## 4. FAITS (FCT-001 à FCT-009)

Neuf faits, tous `FACT`, un seuil `✦` et huit `✧` :

- `FCT-001` — Valeurs et formule de l'IRL : 148,37 en métropole continentale, base légale article 17-1 de la loi du 6 juillet 1989.
- `FCT-002` — **`✦`** L'IRL est calculé en excluant les loyers. Deux familles de sources concordent.
- `FCT-003` — Arrêté du 22 mai 2026 : SMIC porté à 12,31 € l'heure, 9,56 € à Mayotte.
- `FCT-004` — Écart d'estimation de population à Metzing (Moselle) : 678 contre 791, plus de 15 %, effet sur la dotation.
- `FCT-005` — Méthode de calcul des populations de référence pour les communes de moins de 10 000 habitants.
- `FCT-006` — Recommandation de la CNERP : réduction du décalage de trois à deux ans, mise en œuvre annoncée fin 2026.
- `FCT-007` — Loi du 7 juin 1951, article 1 : indépendance professionnelle et Autorité de la statistique publique.
- `FCT-008` — Règlement (UE) 2019/1700 : précision, actualité et comparabilité comme exigences de qualité.
- `FCT-009` — Coût de l'indexation : environ 5 Md€ de prestations par point d'inflation, 0,3 Md€ de charge d'intérêts par dixième de point, base d'environ 500 Md€ de prestations indexées.

Aucun fait n'atteint `✦` sur la valeur du coût agrégé : cette valeur n'existe pas dans les pièces, et elle n'est pas reconstruite ici.

Un point de méthode, écrit noir sur blanc : le chiffre souvent cité de « 0,5 Md€ de prestations par dixième de point » **n'est pas publié comme tel par la source**. Il résulte de la division du chiffre publié par point (5 Md€) par dix. Ce run le signale partout où il l'emploie, et préfère les unités de la source.

## 5. CHAÎNES CAUSALES (CAU-001 à CAU-004)

Trois chaînes soutenues, un gap typé.

- `CAU-001` — **Soutenue.** Indice des prix → pourcentage de revalorisation → montant légal revalorisé → dépense publique. Documentée aux deux bouts.
- `CAU-002` — **Soutenue.** Indice hors tabac et hors loyers → moyenne sur 12 mois → IRL → plafond de révision du loyer → revenu du bailleur et charge du locataire. Chaîne complète, avec sa particularité structurale assumée.
- `CAU-003` — **Soutenue.** Collecte et estimation → population légale par décret → population de référence → montant de dotation par commune. Attestée par l'autorité qui administre la dotation et illustrée par un cas chiffré.
- `CAU-004` — **Gap `CAUSALITY`.** L'effet agrégé des canaux non chiffrés n'est pas mesurable : deux canaux sur cinq sont chiffrés, les trois autres ne le sont pas, sans contrefactuel publié.

## 6. CONTRÔLES (CTRL-001 à CTRL-002)

- `CTRL-001` — L'Autorité de la statistique publique, autorité administrative indépendante, contrôle l'indépendance professionnelle et la qualité du service statistique public. Base légale inspectée.
- `CTRL-002` — La Commission nationale d'évaluation du recensement de la population évalue la méthode et a recommandé en 2025 la réduction du décalage à deux ans.

Ces deux contrôles sont **documentés et datés** ; ils ne sont pas des allégations. C'est ce qui permet d'écrire « contrôle interne » sans supposer une captation.

## 7. ACTIONS (ACT-001 à ACT-002)

- `ACT-001` — L'Insee met en œuvre la réduction du décalage des populations de référence de trois à deux ans, annoncée pour la fin de l'année 2026.
- `ACT-002` — Le ministère de l'Économie et des Finances confirme et chiffre publiquement le cas Metzing.

Aucune intention n'est imputée à un acteur. La mesure est présentée par sa propre source comme une réponse à une difficulté soulevée par les élus.

## 8. AXES (AXS-001 à AXS-009)

Neuf axes, tous saturés : audit des sources, histoire du périmètre, cas probants, flux de ressources, mécanismes, acteurs et relations, règles et contrôles, impact et responsabilité, hypothèses contraires. L'axe des hypothèses contraires est saturé au sens strict du protocole : la contre-recherche a été **exécutée** et n'a rien trouvé, ce qui est un résultat et non un oubli.

## 9. DELTA_REPORT (protocole UPDATE §3)

Ce run est un `UPDATE` du run 17-04 (fresque systémique), traité sous un identifiant de run distinct.

| Élément | Décision |
|---|---|
| `FCT-009` | **`RECHECK`.** Le chiffrage du coût de l'inflation sur les montants indexés est rouvert à la source, et non repris du parent. |
| `FCT-001` | **`RECHECK`.** Objet `EVOLVING` (valeur de l'indice révisable) : la valeur et la formule sont rouvertes. |
| `FCT-003` | **`RECHECK`.** Objet `EVOLVING` (revalorisation annuelle) : l'arrêté est inspecté cette année. |
| `FCT-004` | **`RECHECK`.** Objet `EVOLVING` (populations légales annuelles) : le cas est repris à la question parlementaire. |
| `FCT-005`, `FCT-006` | **`RECHECK`.** La méthode et sa réforme sont datées ; la recommandation 2025 est récente et devait être vérifiée à nouveau. |
| `FCT-007`, `FCT-008` | **`REUSE`.** Textes stables : la base légale et le règlement européen sont réutilisés sans refonte. |
| `LED-007`, `CLM-004`, `CAU-004` | **Ajouts.** N'existaient pas dans le parent. |

Ce qui **change** par rapport au parent : le gap `CAU-002` (`ACCESS`) cesse d'être un vide et devient un résultat chiffré, borné à deux canaux ; les gaps `ACCESS` sur la base légale et le règlement européen sont fermés.

Ce qui **ne change pas** : l'absence de source indépendante contestant l'ordre de grandeur. La contre-recherche sur `FCT-002` n'a trouvé aucune contestation de la formule de l'IRL.

## 10. CONTRADICTIONS

Aucune contradiction documentaire entre pièces n'a été identifiée sur cette ligne. Les écarts observés relèvent de la **couverture documentaire** et sont enregistrés comme gaps typés, jamais convertis en contradiction pour rendre le dossier plus spectaculaire.

## 11. EDI

Le score EDI est calculé par le gate du moteur à partir de la distribution des sources et de la couverture des axes. Il est borné par deux éléments structurels :

- **la dispersion des sources** : quatre familles sont mobilisées (textes officiels, source administrative française, institution financière publique, droit européen), mais la pièce qui porte le chiffrage décisif est unique ;
- **la couverture des canaux** : trois canaux sur cinq restent sans chiffrage, ce qui borne mécaniquement la portée de la conclusion.

Le run ne revendique donc ni `ADEQUATE` ni `BROAD` par confort : la conclusion centrale est bornée à ce que deux canaux permettent de dire.

## 12. CARTE DIALECTIQUE

- **Thèse.** L'indexation de montants légaux sur un indice de prix transmet mécaniquement les choix de mesure statistique dans les finances publiques et dans les revenus des ménages.
- **Antithèse.** Aucune source contestant l'ordre de grandeur publié n'a été trouvée ; les choix de calibrage sont publics, stables et documentés, et l'écart résiduel relève de la documentation disponible, non d'un défaut de mesure.
- **Synthèse.** Ce qui est établi, c'est **la chaîne** et non **l'ampleur totale**. Deux canaux sur cinq sont chiffrés ; les trois autres n'ont pas de chiffrage public identifié. Le run produit donc un fait négatif solide et un gap de mesure, pas un montant consolidé.

## 13. PÉRIMÈTRE & LIMITES

- **Période** : formules en vigueur 2025-2027 ; séries historiques 2005-2026 lorsqu'elles sont mobilisées.
- **Géographie** : France métropolitaine, Mayotte signalée ; cadre européen pour la qualité.
- **Limites opposables** : aucune simulation interne à l'administration n'est accessible ; les montants consolidés des indexations ne font l'objet d'aucune publication unique identifiée ; le run n'a pas produit d'estimation propre pour les canaux non chiffrés.
- **Ce que ce run ne fait pas** : il ne chiffre pas le coût agrégé de l'indexation, il ne mesure pas le transfert entre locataires et bailleurs, et il ne prétend pas que l'absence de chiffrage public vaut absence d'effet.

## 14. ÉTAT DES CONNAISSANCES

Établi avec pièce : la transmission d'un indice de prix à un montant légal est réelle, chiffrée sur deux canaux, datée et encadrée par le droit. Établi comme fait négatif : le coût agrégé de l'indexation n'est pas publié dans les documents identifiés, et le chiffre par dixième de point sur les prestations n'est pas un chiffre publié mais une division arithmétique signalée comme telle. Non établi et enregistré comme tel : l'ampleur de l'effet sur les trois canaux non chiffrés.

## 15. SUSPICION / VÉRIFICATION

Ce run n'élève aucune suspicion. Il enregistre une asymétrie documentaire qui, elle, est vérifiable : la chaîne d'indexation est entièrement opposable dans ses formules, partiellement chiffrée dans ses montants, et jamais consolidée dans une publication unique. La question laissée ouverte au run suivant est une question de **mesure due**, pas de vérification due.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:7|CLM:4|AXS:9|CAU:4|CTRL:2|ACT:2

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_excerpt":"Le montant des prestations sociales indexees sur l inflation est d environ 500 MdE [...] les depenses sociales augmentent de 5 MdE en N+1 [...] chaque variation des prix sur un an de +/- 0,1 % entraine une variation de la charge d interets de +/- 0,3 MdE","gap":"","gap_type":"NONE","kind":"MECHANISM","lead":"Le gap de chiffrage herite (CAU-002 du parent 17-04, GAP_TYPE=ACCESS) est traite: le cout d un dixieme de point d inflation est chiffre par canal dans une publication de reference.","linked_ids":["FCT-009","CLM-001","CAU-001"],"locator":"evidence/fipeco_impact_inflation.txt, sections B.1 et B.2","materiality":"DECISIVE","note":"Reponse bornee, dans les unites de la source : le cout de l indexation des prestations sociales est d environ 5 MdE par point d inflation (presque 0,2 point de PIB) et la charge d interets varie de +/- 0,3 MdE par +/- 0,1 % de variation des prix. Le passage au dixieme de point sur les prestations (environ 0,5 MdE) est une division arithmetique, signalee comme telle. Les canaux IRL, dotations et SMIC ne sont pas chiffres dans la documentation identifiee.","routes":["EXPAND","LINK"],"source_id":"SRC-007","status":"SATURATED"}
LED-002 | {"evidence_excerpt":"L IRL est obtenu a partir de la moyenne de l evolution des prix a la consommation hors tabac et hors loyers, sur les 12 derniers mois","gap":"","gap_type":"NONE","kind":"MECHANISM","lead":"L indice qui indexe les loyers du parc prive est calcule en excluant les loyers.","linked_ids":["FCT-001","FCT-002","CAU-002","CLM-002"],"locator":"evidence/servicepublic_irl.txt (a noter) ; evidence/anil_irl.txt (comment se calcule la revision)","materiality":"DECISIVE","note":"Regle enoncee a l identique par l administration et par l ANIL, avec la base legale (article 17-1 de la loi du 6 juillet 1989). C est l anomalie la plus nette du corpus: l instrument d indexation des loyers ne contient pas les loyers.","routes":["EXPAND","LINK"],"source_id":"SRC-004","status":"SATURATED"}
LED-003 | {"evidence_excerpt":"A compter du 1er juin 2026 [...] son montant est porte a 12,31 EUR l heure ; 2) A Mayotte, son montant est fixe a 9,56 EUR l heure","gap":"","gap_type":"NONE","kind":"EVENT","lead":"Le SMIC a ete revalorise de 2,41 % au 1er juin 2026 par declenchement du mecanisme automatique lie a l indice des prix des menages modestes.","linked_ids":["FCT-003","CAU-001","ACT-003"],"locator":"evidence/legifrance_arrete_smic.txt, article 1","materiality":"IMPORTANT","note":"Cas daté et documente d une transmission directe d un indice de prix a un montant legal, en cours d annee. Le texte de l arrete est inspecte a la source.","routes":["EXPAND"],"source_id":"SRC-001","status":"SATURATED"}
LED-004 | {"evidence_excerpt":"En 2024, alors que l Insee y denombre 678 habitants, la mairie en compte 791. Cet ecart, qui depasse les 15 %, penalise la commune, puisque le montant de la dotation globale de fonctionnement est essentiellement calcule sur la base de sa population","gap":"","gap_type":"NONE","kind":"EVENT","lead":"Un ecart d estimation de population legale superieur a 15 % a penalise une commune identifiee, chiffre et nommee.","linked_ids":["FCT-004","CAU-003","CLM-003"],"locator":"evidence/senat_metzing.txt (question et reponse, 24-25 juin 2025)","materiality":"DECISIVE","note":"Cas le plus concret du corpus: l estimation Insee (678) contre le denombrement municipal (791), ecart superieur a 15 %, effet sur la dotation globale de fonctionnement. Le chiffre n est pas une estimation d auteur, il est porte par une question parlementaire et confirme par une reponse ministerielle.","routes":["EXPAND","LINK"],"source_id":"SRC-002","status":"SATURATED"}
LED-005 | {"evidence_excerpt":"La Commission nationale d evaluation du recensement de la population vient de recommander la reduction de ce decalage a deux ans [...] Cette adaptation sera mise en oeuvre par l Insee a la fin de l annee 2026","gap":"","gap_type":"NONE","kind":"MECHANISM","lead":"La methode de calcul des populations de reference comporte un decalage de trois ans entre date de reference et entree en vigueur, en cours de reduction a deux ans.","linked_ids":["FCT-005","FCT-006","CTRL-002","ACT-001","ACT-002"],"locator":"evidence/senat_metzing.txt (reponse ministerielle)","materiality":"IMPORTANT","note":"Le ministere designe lui-meme ce decalage comme la principale difficulte soulevee par les elus, et la CNERP recommande sa reduction a deux ans avec mise en oeuvre fin 2026. La reforme est datee et attribuable.","routes":["EXPAND"],"source_id":"SRC-002","status":"SATURATED"}
LED-006 | {"evidence_excerpt":"La conception, la production et la diffusion des statistiques publiques sont effectuees en toute independance professionnelle [...] il est primordial que les indicateurs sociaux presentent la qualite necessaire, notamment en termes de precision","gap":"","gap_type":"NONE","kind":"CONTEXT","lead":"La precision et l independance de la statistique publique sont des obligations juridiques inspectees a la source, pas des pratiques declaratives.","linked_ids":["FCT-007","FCT-008","CTRL-001","CLM-004"],"locator":"evidence/legifrance_loi1951_art1.txt ; evidence/eurlex_reglement_2019-1700.txt","materiality":"IMPORTANT","note":"Loi du 7 juin 1951 article 1: independance professionnelle et Autorite de la statistique publique. Reglement (UE) 2019/1700: la precision, l actualite et la comparabilite figurent parmi les exigences de qualite des statistiques sociales europeennes. Deux gaps ACCESS ouverts depuis trois runs de la ligne sont donc fermes.","routes":["EXPAND","LINK"],"source_id":"SRC-005,SRC-006","status":"SATURATED"}
LED-007 | {"evidence_excerpt":"Le montant des prestations sociales indexees sur l inflation est d environ 500 MdE [...] chaque variation des prix sur un an de +/- 0,1 % entraine une variation de la charge d interets de +/- 0,3 MdE","gap":"Les canaux d indexation IRL (loyers), dotations aux collectivites et SMIC ne sont pas chiffres dans la documentation publique identifiee: aucune publication ne donne le montant agrege indexe sur l IRL ni le cout d un dixieme de point sur les dotations.","gap_type":"ACCESS","kind":"OBJECT","lead":"Le chiffrage disponible couvre deux canaux sur cinq.","linked_ids":["FCT-009","CLM-004","AXS-004"],"locator":"absence constatee dans le corpus inspecte; voir AXS-004","materiality":"IMPORTANT","note":"Les prestations sociales et la charge d interets sont chiffrees; les loyers, les dotations et le SMIC ne le sont pas. Le run ne comble pas ces trois canaux par une estimation propre.","routes":["EXPAND"],"source_id":"SRC-007","status":"GAP"}

### CLAIM_REGISTRY_V1
CLM-001 | {"counter":"NONE_FOUND","gap":"","gap_type":"NONE","linked_leds":["LED-001","LED-007"],"proposition":"Dans les unites publiees par la source, le cout de l indexation des prestations sociales est d environ 5 MdE par point d inflation (presque 0,2 point de PIB) et chaque variation des prix sur un an de +/- 0,1 % entraine une variation de la charge d interets de +/- 0,3 MdE, soit 3 MdE par point. Rapporte au dixieme de point et par division arithmetique, les prestations representent environ 0,5 MdE; ce dernier chiffre n est pas publie comme tel par la source.","status":"SUPPORTED","support":"FCT-009 (chiffrage de reference, famille E) ; coherence interne avec FCT-003 (revalorisation datee) et FCT-001/FCT-002 (canaux IRL et dotations non chiffres)"}
CLM-002 | {"counter":"NONE_FOUND","gap":"","gap_type":"NONE","linked_leds":["LED-002"],"proposition":"L indice qui indexe les loyers du parc prive (IRL) est calcule sur un indice des prix qui exclut les loyers; l instrument d indexation ne contient donc pas l objet qu il indexe.","status":"SUPPORTED","support":"FCT-001 (valeur et base legale, source administrative) ; FCT-002 (enonce identique de la regle par un organisme tiers)"}
CLM-003 | {"counter":"NONE_FOUND","gap":"","gap_type":"NONE","linked_leds":["LED-004","LED-005"],"proposition":"Une erreur d estimation de la population legale se transmet directement au montant de la dotation globale de fonctionnement de la commune concernee, sans mecanisme de correction documente a la date de la question: un ecart de 678 contre 791 habitants a penalise une commune identifiee.","status":"SUPPORTED","support":"FCT-004 (cas chiffre, question parlementaire) ; FCT-005 et FCT-006 (methode de population de reference et decalage)"}
CLM-004 | {"counter":"NONE_FOUND","gap":"Aucune publication ne donne la masse des loyers indexes par l IRL, ni le cout d un dixieme de point sur les dotations ou la masse salariale au SMIC.","gap_type":"ACCESS","linked_leds":["LED-007","LED-001"],"proposition":"Les canaux d indexation non chiffres (loyers via l IRL, dotations aux collectivites, SMIC) empechent de produire un cout agrege de l indexation: le chiffrage disponible couvre deux canaux sur cinq, et le montant consolide ne figure dans aucune publication identifiee.","status":"PARTIAL","support":"FCT-009 (couvre les prestations et la charge d interets) ; absence constatee pour les trois autres canaux dans le corpus inspecte"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-005","QRY-006","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-018"],"axis":"SOURCE_AUDIT","links":["LED-001","LED-002","LED-003","LED-006","CLM-001","CLM-002"],"question":"Quels textes et quelles publications chiffrent les montants indexes et leurs formules ?","result_ids":["SRC-001","SRC-002","SRC-003","SRC-004","SRC-005","SRC-006","SRC-007","FCT-001","FCT-002","FCT-003","FCT-007","FCT-008","FCT-009"],"sought_objects":["arrete de revalorisation du SMIC","article 17-1 de la loi du 6 juillet 1989","loi du 7 juin 1951","reglement (UE) 2019/1700","publication chiffrant le cout d un point d inflation"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-009","QRY-010","QRY-012","QRY-014"],"axis":"SCOPE_HISTORY","links":["LED-002","LED-005","LED-006","CAU-002","CAU-003"],"question":"Depuis quand les formules et la methode de calcul sont-elles en vigueur, et quelles evolutions sont datees ?","result_ids":["SRC-003","SRC-005","SRC-006","SRC-002","FCT-002","FCT-005","FCT-006","FCT-007","FCT-008"],"sought_objects":["loi du 6 juillet 1989 article 17-1, modifie en 2014 et 2021","reglement (UE) 2019/1700 abrogeant le reglement (CE) 577/98","loi du 7 juin 1951 modifiee en 2010","decalage de trois ans des populations de reference, reduction prevue fin 2026"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-003","QRY-007","QRY-008","QRY-010","QRY-011"],"axis":"EVIDENCE_CASES","links":["LED-003","LED-004","LED-005","CAU-001","CAU-002","CAU-003","CLM-003"],"question":"Quel cas chiffre montre qu une mesure statistique produit un effet monetaire identifiable sur un destinataire ?","result_ids":["SRC-001","SRC-002","SRC-003","SRC-004","FCT-001","FCT-003","FCT-004","FCT-005"],"sought_objects":["ecart d estimation de population a Metzing et effet sur la dotation","revalorisation du SMIC au 1er juin 2026","valeurs trimestrielles de l IRL et effet sur un loyer"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-001","QRY-002","QRY-015","QRY-017","QRY-018"],"axis":"RESOURCES_FLOWS","links":["LED-001","LED-004","LED-007","CLM-001"],"question":"Quels flux monetaires dependent de montants indexes, et pour quels montants ?","result_ids":["SRC-007","FCT-009","FCT-004","FCT-006"],"sought_objects":["base des prestations sociales indexees","charge d interets liee aux obligations indexees","masse des loyers du parc prive","montant total des dotations"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-003","QRY-009","QRY-010","QRY-011","QRY-018"],"axis":"MECHANISMS","links":["LED-001","LED-002","LED-003","LED-005","CAU-001","CAU-002","CAU-003"],"question":"Par quelles chaines de calcul un indice de prix se transmet-il a un montant legal ?","result_ids":["SRC-001","SRC-002","SRC-003","SRC-004","SRC-007","FCT-001","FCT-003","FCT-005","FCT-009"],"sought_objects":["formule de revision du loyer par l IRL","formule de revalorisation du SMIC et seuil de 2 %","formule de calcul de la population de reference et des dotations","indexation de la charge d interets"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-008","QRY-012","QRY-013","QRY-014"],"axis":"ACTORS_RELATIONS","links":["LED-004","LED-005","LED-006","CTRL-001","CTRL-002","ACT-001","ACT-002","ACT-003"],"question":"Qui produit le chiffre, qui le controle, qui en subit l effet et qui decide de la reforme ?","result_ids":["SRC-002","SRC-005","SRC-006","FCT-004","FCT-006","FCT-007"],"sought_objects":["Insee (production des indices et des populations de reference)","Autorite de la statistique publique (controle de l independance)","CNERP (evaluation de la methode)","ministere de l Economie (reponse au Senat)","communes (destinataires des dotations)","locataires et bailleurs (revision des loyers)","salaries au SMIC"],"status":"SATURATED"}
AXS-007 | {"attempt_ids":["QRY-010","QRY-012","QRY-013","QRY-014"],"axis":"RULES_CONTROLS","links":["LED-002","LED-005","LED-006","CTRL-001","CTRL-002"],"question":"Quelles regles encadrent la mesure et son usage, et quels controles sont documentes ?","result_ids":["SRC-003","SRC-004","SRC-005","SRC-006","FCT-001","FCT-002","FCT-006","FCT-007","FCT-008"],"sought_objects":["loi du 7 juin 1951 article 1 (independance, ASP)","reglement (UE) 2019/1700 (qualite, precision, comparabilite)","article 17-1 de la loi du 6 juillet 1989 (plafond de revision)","regle de gel des loyers pour les logements F et G","recommandation de la CNERP"],"status":"SATURATED"}
AXS-008 | {"attempt_ids":["QRY-002","QRY-007","QRY-011","QRY-018"],"axis":"IMPACT_RESPONSIBILITY","links":["LED-001","LED-004","CAU-001","CAU-003","CLM-001","CLM-003"],"note":"Axe traite: effets chiffres etablis sur les deux canaux chiffres (prestations, charge d interets) et sur une commune identifiee (dotation). L effet agrege reste un gap CAUSALITY enregistre, non comble.","question":"Quel effet chiffre les choix de mesure produisent-ils, et sur qui ?","result_ids":["SRC-002","SRC-004","SRC-007","FCT-001","FCT-004","FCT-009"],"sought_objects":["cout par dixieme de point sur les prestations et la charge d interets","commune penalisee par un ecart d estimation","loyer revise par l IRL"],"status":"SATURATED"}
AXS-009 | {"attempt_ids":["QRY-005","QRY-008","QRY-019"],"axis":"COUNTER_HYPOTHESES","links":["LED-002","LED-004","CLM-002","CLM-003"],"question":"La methode d indexation est-elle contestee, et par qui ?","result_ids":["SRC-002","SRC-004","SRC-007","FCT-002","FCT-004","FCT-009"],"sought_objects":["contestation de la formule de l IRL","contestation de l ordre de grandeur du cout d indexation","contestation de la methode de recensement"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"links":["FCT-009","FCT-003","CLM-001","LED-001"],"mechanism":"Indice des prix (mecanisme de revalorisation legal) -> pourcentage de revalorisation publie -> montant legal revalorise (prestations, SMIC, charge d interets) -> depense publique et revenu des menages","note":"Chaine documentee aux deux bouts: la formule legale d un cote, le montant chiffre de l autre. Le maitre d oeuvre du chiffrage est une institution financiere publique.","sources":["SRC-001","SRC-007"],"status":"SUPPORTED","type":"CHAIN"}
CAU-002 | {"links":["FCT-001","FCT-002","CLM-002","LED-002"],"mechanism":"Indice des prix hors tabac et hors loyers -> moyenne sur 12 mois -> indice de reference des loyers -> plafond de revision annuelle du loyer du parc prive -> revenu du bailleur et charge du locataire","note":"Chaine complete et datee, avec sa particularite structurale: le calibrage de l IRL exclut les loyers. Deux sources concordantes pour la formule; le montant agrege du canal n est pas chiffre.","sources":["SRC-004"],"status":"SUPPORTED","type":"CHAIN"}
CAU-003 | {"links":["FCT-004","FCT-005","FCT-006","CLM-003","LED-004","LED-005"],"mechanism":"Collecte du recensement et estimation par sondage -> population legale officialisee par decret -> population de reference retenue pour les dotations -> montant de dotation par commune","note":"Chaine atteste par l autorite qui administre la dotation, et illustree par un cas chiffre nomme. Le decalage de trois ans et sa reduction datee font partie de la chaine.","sources":["SRC-002"],"status":"SUPPORTED","type":"CHAIN"}
CAU-004 | {"gap":"Le cout agrege de l indexation n est pas mesurable a partir des documents publics identifies: deux canaux sur cinq sont chiffres et les trois autres ne le sont pas, sans contrefactuel publie.","gap_type":"CAUSALITY","links":["CLM-004","LED-007","AXS-004"],"mechanism":"Effet agrege des canaux non chiffres: loyers indexes par l IRL, dotations aux collectivites, masse salariale au SMIC: aucun contrefactuel chiffre ni serie permettant de mesurer l effet total de l indexation sur les finances publiques","note":"Le gap est enregistre, pas comble par une estimation propre. La question reste une mesure due, pas une verification due.","sources":["SRC-007"],"status":"GAP","type":"GAP"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"action":"Controle de l independance professionnelle, de la qualite et de la comparabilite du service statistique public; avis sur la conformite des operations statistiques et labellisation d interet general","controller":"Autorite de la statistique publique (ASP), autorite administrative independante dotee d un mandat de controle du service statistique public","gap":"","gap_type":"NONE","information":"Loi du 7 juin 1951 article 1: la conception, la production et la diffusion des statistiques publiques sont effectuees en toute independance professionnelle, sous le controle de l ASP. Le reglement (UE) 2019/1700 place la precision, l actualite et la comparabilite parmi les exigences de qualite.","links":["FCT-007","FCT-008","LED-006"],"sources":["SRC-005","SRC-006"],"status":"SATURATED"}
CTRL-002 | {"action":"Evaluation de la methode du recensement et formulation de recommandations; recommandation en 2025 de reduire de trois a deux ans le decalage entre la date de reference et l entree en vigueur des populations de reference","controller":"Commission nationale d evaluation du recensement de la population (CNERP)","gap":"","gap_type":"NONE","information":"La recommandation est restituee par le ministere dans sa reponse a une question parlementaire, avec une mise en oeuvre datee par l Insee fin 2026.","links":["FCT-005","FCT-006","LED-005"],"sources":["SRC-002"],"status":"SATURATED"}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Mise en oeuvre de la reduction du decalage des populations de reference de trois a deux ans, annoncee pour la fin de l annee 2026","actor":"Insee","note":"Action datee et attribuable, rapportee par l autorite ministerielle. Aucune intention imputee: la mesure est presentee comme une reponse a une difficulte soulevee par les elus.","note_link":"FCT-006, CTRL-002, LED-005","sources":["SRC-002"],"status":"SUPPORTED"}
ACT-002 | {"action":"Confirmation et chiffrage public du cas Metzing: estimation Insee de 678 habitants contre denombrement municipal de 791 en 2024, ecart superieur a 15 % penaliisant la dotation globale de fonctionnement","actor":"Ministere de l Economie et des Finances (reponse ministerielle au Senat)","note":"Le chiffre est porte par l autorite qui administre la dotation, ce qui augmente sa portee par rapport a une simple allegation locale.","note_link":"FCT-004, CLM-003, LED-004","sources":["SRC-002"],"status":"SUPPORTED"}

SEARCH_ACTIVITY_V1:WEB:9|FETCH:10|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FOUND:ligne INSEE presente en memoire (7 runs, faits 2026-09-21 et avis de controle CNIS); AUCUN snapshot:v1 ne porte subject-fp:d32617f5 (empreinte nouvelle de ce run) ni son empreinte legacy v1 527aefb5; aucune memoire ne porte l objet chiffrage de l indexation. MCP recherche par liste de tags en echec (erreur serveur), requete textuelle utilisee | mnemolite.search_memory | http://localhost:8002/mcp | MNEMO_Q
SYS-002 | SYS | NONE:aucun snapshot exact pour subject-fp:d32617f5 / 527aefb5; pas de HYDRATE; la ligne INSEE reste un warm-route hint (memories du 2026-09-21, dont avis de conformite CNIS et faits de precision EEC) | runtime | - | MEMORY_PROBE
SYS-003 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-004 | SYS | PASS | runtime | FCT-009 | REPAIR_FACT
SYS-005 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND:10 resultats; piste des montants indexes identifiee (prestations sociales indexees ~500 MdE et 5 MdE par point), rapport Cour des comptes non inspecte; renvoi vers FIPECO | - | - | Cour des comptes rapport indexation depenses publiques pensions prestations cout point d inflation milliards
QRY-002 | WEB | FOUND:Bercy chiffre a environ 6 MdE une indexation complete des pensions pour une inflation d environ 2 % (presse, non inspecte); piste FIPECO identifiee | - | - | cout d un point d inflation prestations sociales retraite indexation milliards d euros France
QRY-003 | WEB | FOUND:la clause de declenchement automatique des 2 % a ete franchie au 13 mai 2026; arrete du 22 mai 2026; revalorisation de 2,41 % au 1er juin 2026 (12,02 vers 12,31 E) | - | - | formule revalorisation SMIC decret indice des prix consommation menages modestes 20 % seuil 2 %
QRY-004 | FETCH | FAILED:page officielle du ministere du Travail derriere un controle anti-robot (verification de securite, identifiant de support 13837058291852119213); echec consigne, non contourne | - | - | -
QRY-005 | WEB | FOUND:arrete du 22 mai 2026 identifie sur Legifrance (JORFTEXT000054126589); montants 12,31 E horaire et 1 867,02 E mensuels relayes | - | - | decret revalorisation SMIC 1er juin 2026 legifrance 2,41 % 12,31 euros
QRY-006 | FETCH | FOUND:texte de l arrete du 22 mai 2026 inspecte a la source (article 1: 12,31 E l heure en metropole, 9,56 E a Mayotte a compter du 1er juin 2026) | SRC-001 | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000054126589 | -
QRY-007 | WEB | FOUND:question orale au Senat de 2024 documentant l ecart d estimation a Metzing et son effet sur la dotation globale de fonctionnement | - | - | Metzing ecart recensement population legale denombrement municipal 678 791 dotation globale de fonctionnement
QRY-008 | FETCH | FOUND:texte complet de la question orale n 104 et de la reponse ministerielle du 24 juin 2025 (methode de calcul des populations de moins de 10 000 habitants, ecart 678 vs 791 superieur a 15 %, recommandation de la CNERP) | SRC-002 | https://www.senat.fr/questions/base/2024/qSEQ24100104S.html | -
QRY-009 | WEB | FOUND:formule legale de l IRL (article 17-1 de la loi du 6 juillet 1989) et series trimestrielles publiees | - | - | IRL indice de reference des loyers formule article 17-1 loi 1989 moyenne IPC hors tabac hors loyers 12 derniers mois
QRY-010 | FETCH | FOUND:IRL du 2e trimestre 2026 en hexagone a 148,37 (+1,15 % sur un an); formule hors tabac et hors loyers; base legale article 17-1 modifie par la loi ALUR | SRC-003 | https://www.anil.org/aj-irl-revision-loyers/ | -
QRY-011 | FETCH | FOUND:table officielle des valeurs de l IRL (T2 2026 148,37 ; T1 2026 146,60 ; T4 2025 145,78 ; T3 2025 145,77 ; T2 2025 146,68), formule de revision et regle de gel pour les logements F et G depuis le 24 aout 2022 | SRC-004 | https://www.service-public.gouv.fr/particuliers/vosdroits/F13723 | -
QRY-012 | WEB | FOUND:texte de la loi du 7 juin 1951 identifie sur Legifrance (article 1 et articles 1 bis, 2, 3, 6, 7 bis, 7 ter) | - | - | loi n 51-711 du 7 juin 1951 obligation confidentialite coordination statistiques texte legifrance article 1
QRY-013 | FETCH | FOUND:article 1 de la loi du 7 juin 1951 inspecte a la source: service statistique public, independance professionnelle, Autorite de la statistique publique de neuf membres dont le president nomme par decret en Conseil des ministres | SRC-005 | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000022405540 | -
QRY-014 | FETCH | FOUND:reglement (UE) 2019/1700 inspecte a la source (cadre commun des statistiques europeennes sur les personnes et les menages fondees sur des echantillons; abroge le reglement 577/98; le considerant 5 erige la precision, l actualite et la comparabilite en exigences de qualite) | SRC-006 | https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX%3A32019R1700 | -
QRY-015 | FETCH | FAILED:aucun texte lisible extrait de la notice vie-publique sur les OATi indexees sur l indice des prix a la consommation; echec consigne | - | - | -
QRY-016 | FETCH | PARTIAL:page serie de l IRL servie en HTTP 200 mais valeurs non extractibles par le lecteur (contenu produit en JavaScript); les valeurs sont obtenues par la table de service-public.gouv.fr | - | - | -
QRY-017 | WEB | FOUND:encours des obligations indexees de 54,2 MdE fin aout 2025 (rapport sur la dette des administrations publiques, budget.gouv.fr) ; document PDF non inspecte, donc chiffre non retenu comme fait | - | - | Agence France Tresor encours OATi dette indexee sur l inflation montant 2026 cout
QRY-018 | FETCH | FOUND:chiffrage par canal du cout de l inflation: environ 500 MdE de prestations sociales indexees, +5 MdE de prestations par point d inflation, +/-0,3 MdE de charge d interets par +/-0,1 % de prix (3 MdE par point), recettes +0,3 % du PIB par point | SRC-007 | https://www.fipeco.fr/fiche/Limpact-de-linflation-sur-le-d%C3%A9ficit-public | -
QRY-019 | WEB | NO_RESULT:aucune source ne conteste la methode de calcul de l IRL ni ne propose un indice incluant les loyers; les resultats concordent (service-public, ANIL, Insee, editeurs specialises) | - | - | REFUTATION indice de reference des loyers IRL hors loyers 148,37 +1,15 % contestation methode de calcul autre indice loyers inclus

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000054126589
SRC-002 | ◈ | fam:A | https://www.senat.fr/questions/base/2024/qSEQ24100104S.html
SRC-003 | ◉ | fam:E | https://www.anil.org/aj-irl-revision-loyers/
SRC-004 | ◈ | fam:A | https://www.service-public.gouv.fr/particuliers/vosdroits/F13723
SRC-005 | ◈ | fam:A | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000022405540
SRC-006 | ◈ | fam:A | https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX%3A32019R1700
SRC-007 | ◉ | fam:E | https://www.fipeco.fr/fiche/Limpact-de-linflation-sur-le-d%C3%A9ficit-public

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.service-public.gouv.fr/particuliers/vosdroits/F13723 | A | 2026-07-12 | irl-valeurs-2025-2026-et-formule-de-revision | L indice de reference des loyers (IRL) en metropole continentale vaut 148,37 au 2e trimestre 2026, en hausse de 1,15 % sur un an; la serie publiee donne 146,60 au T1 2026 (+0,78 %), 145,78 au T4 2025 (+0,79 %), 145,77 au T3 2025 (+0,87 %) et 146,68 au T2 2025 (+1,04 %). Le loyer revise est calcule par loyer actuel hors charges x IRL du trimestre de reference de l annee en cours / IRL du meme trimestre de l annee precedente, resultat arrondi a la deuxieme decimale; la revision n est possible que si le bail comporte une clause de revision, et elle est interdite pour les logements classes F ou G dont le bail a ete signe, renouvele ou reconduit depuis le 24 aout 2022 en metropole. | 823fd1be-29b5-4b48-baf3-449415b10ce4
FCT-002 | FACT | ✦ | https://www.service-public.gouv.fr/particuliers/vosdroits/F13723 | A,E | 2026-07-12 | irl-calcule-sur-un-indice-qui-exclut-les-loyers | L indice qui indexe les loyers est calcule en excluant les loyers: l IRL est obtenu a partir de la moyenne, sur les douze derniers mois, de l evolution des prix a la consommation hors tabac et hors loyers. La regle est enoncee a l identique par l administration (Service-Public.gouv.fr, Direction de l information legale et administrative, page verifiee le 12 juillet 2026) et par l association nationale d information sur le logement (ANIL, a jour au 12 juillet 2026), qui precise la base legale: article 17-1 de la loi du 6 juillet 1989, modifie par la loi du 24 mars 2014 (ALUR) et par la loi du 22 aout 2021. C est donc un indice sans loyers qui determine la hausse maximale legale des loyers. | 20845282-f990-4095-8311-6b2f8f1904d5
FCT-003 | FACT | ✧ | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000054126589 | A | 2026-05-22 | smic-releve-au-1er-juin-2026-par-arrete | L arrete du 22 mai 2026 relatif au relevement du salaire minimum de croissance porte le montant du SMIC a 12,31 EUR l heure en metropole, en Guadeloupe, en Guyane, en Martinique, a La Reunion, a Saint-Barthelemy, a Saint-Martin et a Saint-Pierre-et-Miquelon, et a 9,56 EUR l heure a Mayotte, a compter du 1er juin 2026 (article 1). Le releve de 12,02 EUR a 12,31 EUR correspond a une hausse de 2,41 % et a un SMIC mensuel brut de 1 867,02 EUR sur 35 heures. | 4228e724-4f2b-4682-8a63-8f280c7470bb
FCT-004 | FACT | ✧ | https://www.senat.fr/questions/base/2024/qSEQ24100104S.html | A | 2025-06-25 | metzing-ecart-estimation-insee-denombrement-municipal-et-dgf | La commune de Metzing (Moselle) a ete recensee en 2020 et comptait alors 665 habitants. Au 1er janvier 2024, l Insee y denombrait 678 habitants alors que les services municipaux en comptaient 791, soit un ecart superieur a 15 %. Cet ecart penalise la commune car le montant de la dotation globale de fonctionnement est calcule sur la base du niveau de sa population. La reponse ministerielle du 24 juin 2025 confirme le chiffrage et ajoute que Metzing a ete recensee en 2025 et que le bilan signe par le maire fait etat de 719 habitants recenses. | f9b89c63-8291-465a-a5d6-d3eb08aa7bf8
FCT-005 | FACT | ✧ | https://www.senat.fr/questions/base/2024/qSEQ24100104S.html | A | 2025-06-25 | methode-de-calcul-des-populations-de-reference-moins-de-10-000-habitants | Pour les communes de moins de 10 000 habitants, la population est calculee une annee sur cinq a partir des resultats directs de l enquete de terrain realisee par les communes, deux annees sur cinq en tenant compte de l evolution constatee lors de la derniere enquete et deux annees sur cinq en prenant en compte les donnees fiscales. La population en vigueur depuis le 1er janvier 2025 correspond a la situation au 1er janvier 2022, soit un decalage de trois ans entre la date de reference et la date d entree en vigueur, que le ministere designe comme la principale difficulte soulevee par les elus locaux. | 1d16b90d-441d-4ead-af82-db093f26f71c
FCT-006 | FACT | ✧ | https://www.senat.fr/questions/base/2024/qSEQ24100104S.html | A | 2025-06-25 | cnerp-reduction-du-decalage-de-trois-a-deux-ans-en-2026 | A la suite d une expertise methodologique conduite par l Insee en concertation avec les elus, la Commission nationale d evaluation du recensement de la population (CNERP) recommande de reduire le decalage entre date de reference et date d entree en vigueur des populations de reference de trois ans a deux ans; le ministere indique que cette adaptation sera mise en oeuvre par l Insee a la fin de l annee 2026. Le senateur auteur de la question releve dans sa replique que ce gain d une annee profitera a tout le monde sauf aux communes qui perdent des habitants et verront leur dotation baisser un an plus tot. | c938affe-393f-491e-b1c1-6a4cf57278bb
FCT-007 | FACT | ✧ | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000022405540 | A | 2026-09-21 | loi-1951-article-1-independance-professionnelle-et-asp | L article 1 de la loi du 7 juin 1951 (version en vigueur depuis le 30 juin 2010, modifiee par la loi organique du 28 juin 2010) dispose que le service statistique public comprend l Insee et les services statistiques ministeriels, que les statistiques publiques regroupent les productions issues des enquetes dont la liste est arretee chaque annee par un arrete du ministre charge de l economie et de l exploitation de donnees administratives a des fins d information generale, et que la conception, la production et la diffusion des statistiques publiques sont effectuees en toute independance professionnelle. Il cree une Autorite de la statistique publique de neuf membres, chargee de veiller au respect de ce principe et des principes d objectivite, d impartialite, de pertinence et de qualite des donnees, dont le president est nomme par decret en Conseil des ministres. | 65a43fee-3a97-4f44-b203-f5a7be625f89
FCT-008 | FACT | ✧ | https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX%3A32019R1700 | A | 2026-09-21 | reglement-ue-2019-1700-precision-et-comparabilite-comme-exigences-de-qualite | Le reglement (UE) 2019/1700 du 10 octobre 2019 etablit un cadre commun pour des statistiques europeennes relatives aux personnes et aux menages fondees sur des donnees au niveau individuel collectees a partir d echantillons; il abroge le reglement (CE) 577/98 qui encadrait l enquete europeenne sur les forces de travail. Son considerant 5 enonce qu il est primordial que les indicateurs sociaux presentent la qualite necessaire, notamment en termes de precision, d actualite, de facilite d utilisation et d accessibilite, de pertinence, d adaptabilite, mais aussi de comparabilite, de coherence et d efficacite, et qu il est essentiel d ameliorer leur degre d actualite. La precision et la comparabilite des statistiques sociales sont donc des exigences reglementaires europeennes, non des choix nationaux. | 713fca91-9332-4e2e-a2a8-e2b4dfd5a75e
FCT-009 | FACT | ✧ | https://www.fipeco.fr/fiche/Limpact-de-linflation-sur-le-d%C3%A9ficit-public | E | 2026-04-08 | cout-par-dixieme-de-point-d-inflation-prestations-et-charge-d-interets | La source retient une base d environ 500 MdE de prestations sociales indexees sur l inflation (pensions de retraite des regimes de base pour l essentiel, prestations familiales, allocations de logement, minima sociaux). Le cout de l indexation des prestations sociales y est chiffre a environ 5 MdE par POINT d inflation, soit presque 0,2 point de PIB, et chaque variation des prix sur un an de +/- 0,1 % y entraine une variation de la charge d interets de +/- 0,3 MdE, soit 3 MdE pour un point. ATTENTION : le chiffre par dixieme de point sur les prestations (environ 0,5 MdE) n est pas publie comme tel par la source ; il resulte d une division arithmetique du chiffre par point (5 MdE / 10). | a6b13073-b4e5-4a1a-bed1-877904424517
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-004
FCT-002 | SRC-003,SRC-004
FCT-003 | SRC-001
FCT-004 | SRC-002
FCT-005 | SRC-002
FCT-006 | SRC-002
FCT-007 | SRC-005
FCT-008 | SRC-006
FCT-009 | SRC-007

## REFUTATION_REGISTRY_V1
FCT-002 | QRY-019 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:CONFIRME
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | ELIGIBLE:VERIFIE
FCT-008 | ELIGIBLE:VERIFIE
FCT-009 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -
FCT-007 | WRITE | -
FCT-008 | WRITE | -
FCT-009 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:7
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL_GAP | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:19
CP-008 | CORRECTION | PASS | LAST_COMPLETED:18 | NEXT_ACTION:19

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-21T03:19:12.112566+00:00","fact_mem":{"FCT-001":"823fd1be-29b5-4b48-baf3-449415b10ce4","FCT-002":"20845282-f990-4095-8311-6b2f8f1904d5","FCT-003":"4228e724-4f2b-4682-8a63-8f280c7470bb","FCT-004":"f9b89c63-8291-465a-a5d6-d3eb08aa7bf8","FCT-005":"1d16b90d-441d-4ead-af82-db093f26f71c","FCT-006":"c938affe-393f-491e-b1c1-6a4cf57278bb","FCT-007":"65a43fee-3a97-4f44-b203-f5a7be625f89","FCT-008":"713fca91-9332-4e2e-a2a8-e2b4dfd5a75e","FCT-009":"a6b13073-b4e5-4a1a-bed1-877904424517"},"mnemo_row":"PASS: 9/9 eligible facts persisted via MCP write_memory (8002) + 1 investigation memory (1dab0f23-5c84-49cf-9055-8c8f45b9bada); duplicate_warning=none; run 20260921-0428-insee-chiffrage-indexation-effet-ipc-dotations","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"NONE","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-008","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-009","reason":"NONE","success":1}],"writeback_row":{"attempted":9,"blocked":0,"eligible":9,"failure":0,"success":9}}

PERSISTENCE_META: MNEMO_ROW:PASS: 9/9 eligible facts persisted via MCP write_memory (8002) + 1 investigation memory (1dab0f23-5c84-49cf-9055-8c8f45b9bada); duplicate_warning=none; run 20260921-0428-insee-chiffrage-indexation-effet-ipc-dotations | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:9;attempted:9;success:9;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[9 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-002 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-008 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-009 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
