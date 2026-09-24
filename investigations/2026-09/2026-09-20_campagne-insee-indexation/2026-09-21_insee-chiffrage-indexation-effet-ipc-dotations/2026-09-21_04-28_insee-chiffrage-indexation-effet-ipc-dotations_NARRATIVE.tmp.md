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
