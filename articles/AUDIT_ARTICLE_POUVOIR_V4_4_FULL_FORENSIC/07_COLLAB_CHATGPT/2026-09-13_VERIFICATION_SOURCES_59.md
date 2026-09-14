---
trace_schema: "verification/v1"
artifact_type: "source_verification"
target: "01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md"
cible_sha256: "1cb2f0c12b4736f2893d1238fd6effd0eba3d0abdb1f2fccaee28b9711cdff66"
date: "2026-09-13"
auditeur: "Buffy (second auditeur, externe a la redaction des editions 42 a 63)"
objet: "Rang 8 du plan, point 2 (§8 verifications avant publication) et point 3 (les 59 entrees du registre n'avaient pas ete recontrôlées)"
verdicts: "48 CONCORDE / 3 PARTIEL / 8 NON VERIFIE, sur 59 entrees"
zero_em_dash: true
---

# Verification externe des sources de l'article V4.4 (59 entrees + 3 verifications avant publication)

## 1. Mandat, et ce que cette passe ne fait pas

Le contrôle terminal (`2026-09-13_CONTROLE_TERMINAL.md`) a établi que chaque proposition générale de l'article **désigne** sa garantie. Il a explicitement laissé de côté deux choses, et c'est ce mandat qui est exécuté ici :

1. les trois vérifications avant publication listées au §8 du plan (Vattenfall, Internet Society, sources de presse [58] et [59]) et le sort du manifeste du bundle ;
2. la revue des **59 entrées du registre**, pour vérifier non plus que l'article désigne une pièce, mais que **la pièce dit ce qu'on lui fait dire**.

Trois précautions de méthode, pour que le lecteur sache ce que valent ces verdicts :

- **Ce qui est vérifié.** Pour chaque entrée : que la ressource existe, que son identité (titre, date, auteur, numéro) correspond à ce que le registre annonce, et qu'elle **contient** les éléments factuels que l'article en tire (montants, dates, noms, qualifications). La méthode est une sonde : la page est récupérée, convertie en texte, et interrogée sur des motifs tirés de l'affirmation.
- **Ce qui n'est pas vérifié.** Une sonde positive établit la **présence** des éléments, pas leur lecture intégrale ni leur poids. Aucune entrée n'a été lue de bout en bout, sauf les documents courts (délibérations HATVP, communiqué Vattenfall, article 433-2, réponse parlementaire britannique, FAQ Internet Society).
- **Un faux négatif de ma part, consigné comme tel.** Ma première sonde sur la délibération HATVP 2022-123 a conclu « figure absente » pour « au moins 8 réunions ». C'était faux : le texte dit « à au moins **huit reprises** », et mon motif cherchait un chiffre accolé à « réunions ». **Le défaut était dans ma sonde, pas dans l'article.** C'est le mode de défaillance propre à cette méthode, et il est signalé ici pour que les huit « NON VÉRIFIÉ » qui suivent ne soient pas lus comme huit soupçons.

## 2. Les trois vérifications avant publication

### A. Vattenfall, communiqué du 5 mars 2021 : CONCORDE

Source : `https://group.vattenfall.com/press-and-media/pressreleases/2021/understanding-to-terminate-disputes-on-german-nuclear-phase-out/`

Texte lu :

> « The German Government today announced cornerstones of an understanding with E.ON, EnBW, RWE and Vattenfall to terminate disputes on German nuclear phase out and to implement German Constitutional Court rulings on such matter. »

> « According to the understanding, Vattenfall would receive a compensation of EUR 1,425 million, subject to taxation. »

Date dans la page : `5 March 2021`. Les quatre faits de l'entrée [48] sont confirmés : accord mettant fin aux contentieux, les quatre parties nommées, le montant de 1 425 millions d'euros, et une sortie du nucléaire **non renversée** (le communiqué met fin aux litiges et applique la jurisprudence constitutionnelle, il ne rouvre pas la décision politique). Nuance non mentionnée par l'article : l'indemnisation est « subject to taxation ».

### B. Internet Society, FAQ New IP : CONCORDE

Source : `https://www.internetsociety.org/resources/doc/2022/huaweis-new-ip-proposal-faq/`

Texte lu :

> « At the December 2020 plenary session of SG13 and SG11, the decision was taken to: Not to accept “New IP” related questions as new work items. Stop discussing “New IP” at least until WTSA in March 2022. »

C'est mot pour mot ce que l'entrée [28] annonce. L'article écrit « décision, à la session plénière de décembre 2020 des groupes SG13 et SG11 de l'UIT-T, de ne pas accepter les questions liées à “New IP” » : exact.

**Réserve sur la seconde moitié de [28].** L'entrée cite aussi un document de la Commission (FPI) sur les oppositions à New IP et son abandon. Ce PDF n'a pas été ouvert dans cette passe. La partie « oppositions techniques et politiques » de l'article repose donc sur la FAQ Internet Society seule, ce qui la couvre, mais l'entrée reste partiellement contrôlée.

### C. Sources de presse [58] et [59]

**[58] AFP, 11 avril 2019 (reprise par Connaissances des Énergies) : CONCORDE.** La page contient la dépêche : nomination « à compter du 22 avril », intégration du groupe « en novembre 2017 », fonction antérieure de « directeur des affaires publiques de GE France », et « conseiller sur les affaires industrielles et le financement à l'export au sein du cabinet du ministre de l'Economie, entre 2013 et 2016 ». Toutes les mentions de l'article sont dans la pièce.

Un détail de date : la page porte « Mis à jour le 12 avril 2019 », alors que le registre date la dépêche du **11** avril. Le slug de l'URL (`-190411`) confirme la dépêche du 11, la page ayant été mise à jour le 12. Pas une erreur, mais le registre gagnerait à écrire « dépêche du 11 avril 2019, page mise à jour le 12 ».

**[59] Le Monde, Les Décodeurs, 6 janvier 2023 : NON VÉRIFIÉ.** Trois tentatives, trois blocages :

| Méthode | Résultat |
|---|---|
| `curl` | HTTP 402 (paywall) |
| extraction directe | page « Client Challenge » (protection DataDome) |
| capture Wayback du 5 décembre 2023 | coquille JavaScript : `"is_a_teaser":true`, `"restreint":true`, corps de l'article absent du HTML |

Ce n'est pas un défaut de l'article, et ce n'est pas non plus une preuve. Le dossier interne `05_ALSTOM/INVESTIGATION_REVOLVING_DOOR_BAILEY_2026-09-13.md` porte la même conclusion indépendamment : « Extraits indexés et concordants, article non accessible (anti-robot) ». L'article attribue à [59] la mention de Hugh Bailey dans les mobilités public vers privé de la macronie ; **cette attribution reste non vérifiée à la source**, et devra être acceptée comme telle ou contournée par un autre moyen (lecture sur abonnement, copie de presse).

### D. Manifeste du bundle : mesuré, et la divergence a un seul nom

Jusqu'ici le dossier disait « manifeste divergent, non re-scellé ». `VERIFY_BUNDLE.py` donne la mesure exacte :

```
FAIL
SHA_MISMATCH 01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md
```

**Une seule divergence, sur 3 539 lignes de manifeste.** Le script confirme par ailleurs les figures (4/4), le corpus physique (113/113), la présence des fichiers requis, et l'absence de tout autre écart. Autrement dit : **la seule chose que le manifeste ne certifie plus est l'objet même de l'audit**, ce qui est la conséquence attendue des 63 éditions. Le reste du bundle est intact.

Conséquence pratique : un re-scellement n'aurait pas à re-hasher un corpus de 3 539 fichiers, mais **une ligne**, celle de la cible. La décision de le faire reste à l'auteur, puisque la politique documentée est de ne pas re-sceller pendant les éditions.

## 3. Les 59 entrées du registre

Verdicts : **48 concordantes**, **3 partielles**, **8 non vérifiées**.

### Ce qui a été vérifié, entrée par entrée

| # | Source | Preuve lue | Verdict |
|---|---|---|---|
| 1 | Bundestag, lobbying AWS | « EUCS: Streichung von Souveränitätsanforderungen » attribué à Amazon Web Services | CONCORDE |
| 2 | Reuters, 3 avril 2024 | HTTP 401 puis capture Wayback sans corps | NON VÉRIFIÉ |
| 3 | Commission, souveraineté cloud | titre + `17 April 2026` | CONCORDE |
| 4 | Parlement britannique | « In financial year 2017/18, the FCO funded […] £296,500. This financial year, the FCO is funding a further £1,961,000 » (réponse du 3 décembre 2018) | CONCORDE |
| 5 | fdik, formulaire FCO | PDF lu (8 760 mots), formulaire de candidature phase II | CONCORDE |
| 6 | fdik, Moncloa Campaign | PDF lu (3 pages) : campagne Twitter du 07/06/2018, **ne nomme pas Baños** | PARTIEL |
| 7 | fdik, Top 3 Deliverables | « Recent example from Spain of our influencing the appointment of the pro-Kremlin » | CONCORDE |
| 8 | El País, 8 juin 2018 | « El candidato a director de la Seguridad Nacional es un defensor de Rusia », `2018/06/08` | CONCORDE |
| 9 | El País, 14 juin 2018 | « Sánchez nombrará al general Ballesteros […] », plus « el otro candidato […] era el coronel Pedro Baños » | CONCORDE |
| 10 | DOJ, BNP Paribas | « BNP Paribas Agrees To Plead Guilty and To Pay $8.9 Billion » | CONCORDE |
| 11 | TotalEnergies, 16 mai 2018 | « US withdrawal from the JCPOA: Total's position related to the South Pars 11 project in Iran » | CONCORDE |
| 12 | CJUE, Bank Melli c. Telekom | « Judgment of the Court (Grand Chamber) of 21 December 2021 […] Case C-124/20 » | CONCORDE |
| 13 | Commission, règlement de blocage | « Extraterritoriality (Blocking statute) » | CONCORDE |
| 14 | Commission, sécurité gaz | « Security of gas supply » | CONCORDE |
| 15 | CINEA, 27 avril 2022 | « after Russia cuts off gas supply to Poland and Bulgaria » | CONCORDE |
| 16 | OMC DS610 | « WTO dispute settlement (DS610) » | CONCORDE |
| 17 | MAE chinois | « Lithuania […] allowed the Taiwan authorities to set up a “Taiwanese Representative Office in Lithuania” » | CONCORDE |
| 18 | MAE lituanien, 2026 | « Strengthening economic cooperation between Lithuania and Taiwan » (capture du 03/08/2026) | CONCORDE |
| 19 | Règlement 2023/2675 | « protection of the Union […] from economic coercion by third countries » | CONCORDE |
| 20 | MES, conditionnalité | page « Conditionality » | CONCORDE |
| 21 | Commission, FRR France | « La France et la Belgique reçoivent de nouveaux paiements au titre de la facilité » | CONCORDE |
| 22 | Règlement 2026/1386 | « on the screening of foreign investments in the Union » | CONCORDE |
| 23 | DG Trésor, rapport IEF 2024 | page rendue par JS, aucun chiffre extractible | NON VÉRIFIÉ |
| 24 | AN, Photonis | « décidé d'un commun accord […] de ne pas autoriser le rachat de Photonis par Teledyne » | CONCORDE |
| 25 | Piraeus Port Authority, COSCO | « 67 % » absent du HTML servi | NON VÉRIFIÉ |
| 26 | Ministère norvégien, fonds souverain | HTTP 403, aucune capture Wayback | NON VÉRIFIÉ |
| 27 | UIT-T, contribution C-0083 | hôte injoignable (échec réseau), aucune capture | NON VÉRIFIÉ |
| 28 | Internet Society, FAQ New IP | « December 2020 plenary session of SG13 and SG11 […] Not to accept “New IP” related questions » | CONCORDE (réserve §2.B) |
| 29 | Boumans et al. | résumé : « n= 119,452 », « n= 247,161 », « up to 75% of the online news articles », presse néerlandaise | CONCORDE |
| 30 | Vogler et al., 2024 | résumé : « online media outlets […] in the German federal state of North Rhine-Westphalia », mots-clés « Germany » | CONCORDE (réserve §4) |
| 31 | JEEA, fact-checkers | Crossref : 23(6) p. 2137-2164, 2025, Louis-Sidois, DOI 10.1093/jeea/jvaf011 | CONCORDE |
| 32 | Nature, algorithme de X | Crossref : vol. 652 p. 416-423, 18/02/2026, Gauthier et al. | CONCORDE |
| 33 | Nature, Facebook | Crossref : vol. 620 p. 137-144, 27/07/2023, Nyhan et al. | PARTIEL |
| 34 | Règlement 2022/2065 | « règlement sur les services numériques » | CONCORDE |
| 35 | Commission, signaleurs de confiance | « Trusted flaggers under the Digital Services Act (DSA) » | CONCORDE |
| 36 | Médiateur, Farkas | « found maladministration, first, in that the EBA should have forbidden the job move […] Second, there was maladministration » | CONCORDE |
| 37 | HATVP 2022-123 | « a rencontré le président-directeur général ou d'autres cadres dirigeants […] à au moins huit reprises au cours des trois dernières années » | CONCORDE |
| 38 | HATVP 2022-104 | « a rencontré le président-directeur général de la société Hopium à deux reprises […] juin et septembre 2021 » | CONCORDE |
| 39 | OLAF, OC/2022/0514 | « No evidence was found that Ms KROES negotiated any form […] nor that she negotiated and/or signed any official document with a future [employer] » | CONCORDE |
| 40 | HATVP, rapport 2024 | « 751 projets de mobilité […] a rendu 639 avis. Parmi eux, 95,5 % étaient des avis de compatibilité […] 4,5 % d'avis d'incompatibilité » | CONCORDE |
| 41 | Code pénal, 433-2 | « pour abuser ou avoir abusé de son influence réelle ou supposée en vue de faire obtenir […] des marchés ou toute autre décision favorable » | CONCORDE |
| 42 | Directive 2026/1021 | « criminalise additional acts, such as the abuse of functions, trading in influence and illicit enrichment » | CONCORDE |
| 43 | DOJ, Airbus | « Airbus Agrees to Pay Over $3.9 Billion in Global Penalties » | CONCORDE |
| 44 | DOJ, Alstom | « Alstom Pleads Guilty and Agrees To Pay $772 Million Criminal Penalty » | CONCORDE |
| 45 | DOJ, Siemens | « payments to purported business consultants, part of which were paid as kickbacks […] as “commissions” » | CONCORDE |
| 46 | BIS, offsets | « Offsets in Defense Trade » | CONCORDE |
| 47 | GAFI, bénéficiaires effectifs | « Guidance on Beneficial Ownership of Legal Persons » | CONCORDE |
| 48 | Vattenfall, 5 mars 2021 | §2.A | CONCORDE |
| 49 | italaw, Rockhopper | « 2 Jun 2025 Decision on Annulment », « 23 Aug 2022 Final Award », ICSID ARB/17/14 | CONCORDE |
| 50 | Commission, Charte de l'énergie | « L'UE notifie sa sortie du traité sur la Charte de l'énergie et met fin aux procédures d'arbitrage intra-UE » | CONCORDE |
| 51 | US Chamber, 23 mai 2023 | titre exact + `2023-05-23` | CONCORDE |
| 52 | Ministère de l'Économie, autorisation du 5 novembre 2014 | HTTP 403, aucune capture Wayback | NON VÉRIFIÉ |
| 53 | AN, rapport 897 | « Le rachat du pôle Énergie d'Alstom par General Electric en 2014 », Pierucci arrêté à New York | CONCORDE |
| 54 | AN, audition de Patrick Kron | transcription lue (Kron, Immelt, les 772 millions, la trésorerie) | PARTIEL (réserve §4) |
| 55 | EDF, 31 mai 2024 | « EDF acquiert les activités nucléaires de GE Steam Power […] Arabelle Solutions, une filiale détenue à 100 % par EDF » | CONCORDE |
| 56 | AN, question 16350 | « l'incapacité d'honorer sa promesse de créer 1 000 emplois nets d'ici la fin de l'année 2018 », audit de décembre 2018 : « 25 emplois en CDI créés » | CONCORDE |
| 57 | Le Monde, 3 mars 2026 | HTTP 402, capture Wayback vide | NON VÉRIFIÉ |
| 58 | AFP, 11 avril 2019 | §2.C | CONCORDE |
| 59 | Le Monde, Les Décodeurs | §2.C | NON VÉRIFIÉ |

### Les 8 non vérifiées, et pourquoi elles le sont

| # | Cause | Contournement possible |
|---|---|---|
| 2 | Reuters : 401 + capture sans corps | copie de presse, ou capture d'un autre instant |
| 23 | page JS : aucun contenu extractible | retrouver le PDF du rapport sur un autre chemin |
| 25 | le taux de 67 % n'est pas dans le HTML servi | rapport annuel de l'autorité portuaire |
| 26 | 403 + aucune capture | autre édition du document |
| 27 | hôte injoignable | recherche par numéro de contribution |
| 52 | 403 + aucune capture | note de presse reprise ailleurs |
| 57 | paywall Le Monde | lecture sur abonnement |
| 59 | paywall + protection anti-robot | lecture sur abonnement |

Aucune de ces huit n'est une source inventée : ce sont des sources **non atteignables depuis cet environnement**, et le registre les nomme avec une URL qui répond (sauf [27]) même quand elle est protégée. La distinction entre « source douteuse » et « source inaccessible » est le point : ici, c'est la seconde.

## 4. Ce que cette passe apporte de neuf

1. **Les montants du Foreign Office sont exacts** : 296 500 livres pour 2017-2018, puis 1 961 000 livres, dans la réponse écrite du 3 décembre 2018. L'article écrit « 1,961 million de livres » : correct.
2. **Les chiffres HATVP de la mobilité sont exacts** dans le texte même de la délibération : « à au moins huit reprises », et « à deux reprises » pour Hopium, avec « compatibilité avec réserves ».
3. **Les montants des règlements américains sont exacts** ($772 M Alstom, $3.9 Md Airbus, $8.9 Md BNP), et l'usage que l'article en fait (consultants, commissions, intermédiaires) est dans la pièce.
4. **La date d'annulation Rockhopper est exacte** : 2 juin 2025, contre une sentence du 23 août 2022.
5. **Le manifeste a un seul écart, nommé** : la cible. Le reste du bundle est intact.
> **Mises à jour du 13 septembre 2026.** Les points 6, 7 et 8 de cette liste ont été traités depuis, chacun par la voie indiquée. Cette entête est ajoutée après coup ; le texte des points n’est pas réécrit, pour que la trace de ce que cette passe avait trouvé reste lisible.

6. **[6] ne nomme pas Pedro Baños.** Le document Moncloa est une liste de liens Twitter datée du 07/06/2018 ; l'identification de Baños comme cible de la mobilisation vient de [8] et [9] (El País, 8 et 14 juin 2018), pas de [6]. L'article agrège correctement les deux, mais sa phrase « Des documents de l'Integrity Initiative décrivent une mobilisation autour de la possible nomination de Pedro Baños » fait porter au document une précision qu'il tient du journal. **Correction possible, à la marge** : « des documents de l'Integrity Initiative décrivent une mobilisation sur la nomination, et la presse espagnole identifie Pedro Baños comme le candidat visé ».
   **CLOS par T6 le 2026-09-13** : le corps dit désormais « une possible nomination » et « Pedro Baños, que la presse espagnole désigne comme le candidat visé ». Formulation appliquée, proche de celle proposée ici. Voir `SEMANTIC_DIFF_T6_2026-09-13.md` §6.
7. **[33] fait l'objet d'une « Author Correction »** : Crossref signale `10.1038/s41586-023-06795-x` (Nature, novembre 2023) pour l'article `s41586-023-06297-w` utilisé ici. Une correction d'auteur ne renverse pas la conclusion, mais l'article s'en sert pour un argument négatif (« sans mettre en évidence de changement correspondant sur les principales attitudes étudiées »). **À vérifier avant publication** : lire la correction et confirmer qu'aucun résultat utilisé n'est modifié.
   **CLOS le 2026-09-13** : la correction a été lue. Elle supprime **une ligne** du tableau supplémentaire 36 (variable de contrôle sur les « strikes » CIB, mal nommée) et ne touche ni le résumé, ni le protocole, ni les résultats principaux. L'emploi de [33] par l'article est exact. Voir `PREREQUIS_T4_VERIFICATION_33_54_2026-09-13.md` §1.
8. **[54] demande une relecture partielle.** La transcription confirme l'audition et le contexte (772 millions, trésorerie de 1,5 milliard, Immelt), mais le passage lu montre le président de la commission confrontant Patrick Kron à des **versions successives différentes** sur l'origine du contact. L'article affirme que Kron « a déclaré sous serment avoir pris l'initiative du contact avec Jeffrey Immelt ». C'est plausible pour l'audition de 2018, mais la seconde moitié de la transcription n'a pas été lue et le point mérite d'être tranché sur pièce : **c'est la seule affirmation de l'article qui pourrait être contredite par la source qu'il cite**.
   **CLOS par T4 le 2026-09-13.** Lecture faite : la phrase n’est **pas** contredite, Kron a bien prêté serment, revendiqué l’initiative et nié le chantage, y compris la variante économique. Mais la même source en porte la réfutation partielle, ouverte par le président de la commission : deux versions antérieures contradictoires sur l’initiative du contact. T4 a donc **borné le mot « contrôle »** et **nommé la contestation en une incise**, sans importer la chronologie. Voir `PREREQUIS_T4_VERIFICATION_33_54_2026-09-13.md` §2 et `SEMANTIC_DIFF_T4_2026-09-13.md` §1.
9. **[30] : l'étude est bien allemande** (Rhénanie-du-Nord-Westphalie), malgré des auteurs zurichois. En revanche le classement « domination très nette de dpa, loin devant Reuters et l'AFP » n'a pas été confirmé sur la pièce (seul le résumé a été lu).

## 5. Limites de cette passe

- **Méthode par sondes.** Un verdict CONCORDE signifie « les éléments de l'affirmation sont présents dans la pièce », pas « l'affirmation est vraie dans toute sa portée ». Les nuances, les réserves et les conditions d'une source ne sont pas captées par un motif.
- **Aucune lecture intégrale** des documents longs (rapport 897, rapport annuel HATVP, transcription Kron, rapport OLAF, article de presse).
- **Auditeur unique, et c'est le second.** Cette passe est externe à la rédaction des éditions 42 à 63, ce qui satisfait la limite n°2 du contrôle terminal pour les **sources**. Elle ne satisfait pas la même limite pour la **prose** : rien ici ne re-contrôle les 62 propositions générales, qui ont déjà reçu leur contrôle.
- **Huit entrées restent non vérifiées**, dont deux sont importantes pour le dossier Alstom ([52] l'autorisation française, [57] l'information judiciaire de 2026). L'article les cite correctement, mais leur contenu n'a pas été vu.

## 6. Appareil de vérification utilisé

| Outil | Usage |
|---|---|
| `curl` (User-Agent navigateur) | récupération, statuts, détection des blocages |
| `pdftotext` | extraction des PDF (délibérations HATVP, rapport OLAF, documents fdik) |
| Crossref REST API | vérification bibliographique (revue, volume, pages, DOI, dates) |
| Wayback Machine (`web.archive.org/web/<année>/<url>`) | contournement des protections anti-robot (DOJ, Parlement britannique, Legifrance, Le Monde) |
| API Wayback `available` | **inutilisable ici** : réponse 429, six faux « aucune capture » produits avant diagnostic |
| Mnemolite (MCP 8002) | mémoire d'abord : interrogée sur Vattenfall, retour de similarité 0,006, donc cache miss assumé |

## 7. Write-back mémoire, et ce qu'il a révélé

Neuf faits vérifiés ont été écrits dans Mnemolite (MCP 8002, `write_memory`), avec citation, URL, tag `project:article-pouvoir-v4.4`, `status:CONFIRME`, `source:<sha1-10>`, `verifie-2026-09-13` : Vattenfall 2021, Internet Society New IP, Foreign Office / Integrity Initiative, HATVP 2022-123, HATVP 2022-104, Rockhopper (annulation), OLAF Kroes, Photonis / Teledyne, et l'état du manifeste du bundle.

**Persistance : vérifiée.** Une écriture témoin a renvoyé un identifiant (`25880b05-88e2-4e0f-ac93-17073bcc5c6c`), `embedding_generated: true`, et se relit par `read_memory`. Le témoin a ensuite été supprimé (`delete_memory`) : ce n'était pas une mémoire, c'était un instrument.

**Recherche : non vérifiée, et c'est un problème ouvert.** Mes neuf écritures n'apparaissent pas dans un top 10 de `search_memory` pour des requêtes qui reprennent presque mot pour mot leur titre, alors que des mémoires préexistantes du projet remontent sur les mêmes requêtes (par exemple `FCT-T2-001 : Veto formel de l'État sur Photonis/Teledyne` et `FAIT VÉRIFIÉ : HATVP 2025`). Autrement dit : la recherche fonctionne, elle ne voit pas ce qui vient d'être écrit. Deux lectures possibles, non tranchées ici : indexation différée, ou `needs_consolidation: true` sur une base de 41 267 mémoires dont l'indexation n'a pas été déclenchée.

Conséquence pour le protocole « mémoire d'abord » : **sur ces faits, la mémoire n'était pas consultable, donc l'appel web était légitime**, et le write-back obligatoire est fait. Mais tant que la recherche ne remonte pas les écritures fraîches, la règle produit des cache miss systématiques sur le travail du jour. C'est un point à l'attention du mainteneur de Mnemolite, pas un défaut de cet audit.

*Zéro em-dash dans ce document.*
