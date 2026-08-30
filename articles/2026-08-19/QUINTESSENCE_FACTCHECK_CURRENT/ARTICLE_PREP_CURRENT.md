# ARTICLE PREP — État courant XQ204 post-rollback — 2026-08-25

`PUBLICATION_CANDIDATE = QUINTESSENCE_ARTICLE_FACTCHECK_TRUST_XQ204_2026-08-25.md`
`LATEST_CANDIDATE_SHA256 = 0ddd1ab44ff314d10b49be90036c360374727a2b5f6f1bb64f7e26ad6e051b4e`
`XQ204_PASS_A_PROBATIVE = VALIDATED`
`XQ204_PASS_B_LANGUAGE = VALIDATED`
`XQ204_PASS_C_COGNITIVE = VALIDATED`
`XQ204_PASS_D_MOBILE_FIGURES = REJECTED_VISUAL_REGRESSION_YAGNI`
`XQ204_FIGURE_ROLLBACK = PASS_BYTE_IDENTICAL_XQ203`
`XQ204_PASS_E_POST_ROLLBACK_BAT = PASS_WITH_BOUNDS`
`CANONICAL_FIGURES = XQ203_RESTORED_5_SVG_5_PNG`
`PUBLICATION_TARGET = SUBSTACK`
`MOBILE_FIRST_REQUIREMENT = NONE`
`PUBLICATION_DECISION = HOLD_FOR_EDITORIAL_COMPLETION`
`XQ204F_ORIGINAL_EDITORIAL_BRIEF = PARTIAL_FAIL`


## XQ204F — audit du brief éditorial initial

- Le brief initial n'est pas entièrement exécuté. La typographie mécanique et les acronymes sont largement corrigés, mais le confort de lecture n'a reçu qu'une passe minimale.
- La passe C contient seulement un « Point de lecture », un « À retenir », quelques scissions et une analogie explicite photographie/film ; aucun mini-schéma nouveau.
- L'archéologie documentaire a produit Yahoo et la borne Conspiracy Watch, mais AFP Bridle pré-29/06/2021 et Fact & Furious original/historique restent ouverts.
- `PASS_C = VALIDATED` décrit la conformité de la passe C réduite, pas la satisfaction complète du brief initial.
- Nouvelle gate : `HOLD_FOR_EDITORIAL_COMPLETION`.
- Audit : `annexes/XQ204F_EDITORIAL_BRIEF_FULFILLMENT_AUDIT_2026-08-25.md`.

## État verrouillé

- Les patches probatoires Yahoo / « ×12 » et *Conspiracy Watch* sont intégrés et bornés.
- La passe langue/terminologie est validée : aucun tiret cadratin ni demi-cadratin dans le candidat.
- Le refactoring de lisibilité cognitive est conservé ; aucune simplification probatoire ni nouvelle figure.
- La tentative de recomposition mobile-first (passe D) est **rejetée** : exigence non demandée, régression visuelle, violation YAGNI/no-regression.
- Les cinq SVG et cinq PNG de publication ont été restaurés **octet pour octet** depuis le package XQ203. L’audit de rollback conserve les dix SHA-256.
- Les variantes D rejetées sont archivées uniquement sous `annexes/rejected/XQ204_PASS_D_VISUAL_REGRESSION/` et ne sont référencées par aucun article.
- Le BAT final a été relancé après rollback : 113/113 sources utilisées, 187 appels de citation, 0 citation orpheline, 0 cible relative manquante, SQLite `integrity_check = ok`.
- Bornes toujours ouvertes : formulation AFP Bridle avant le 29/06/2021 ; original complet + historique *Fact & Furious* pharmacovigilance.

## Règle anti-régression figures

`SUBSTACK_PUBLICATION_FIGURES = XQ203_CANONICAL`  
`NO_FIGURE_REDESIGN_WITHOUT_EXPLICIT_EDITORIAL_REQUIREMENT`  
`QA_EXPERIMENT != PUBLICATION_MASTER`

---

## Historique XQ203A et antérieur préservé

# ARTICLE PREP — État courant post-XQ203A — 2026-08-25

`PUBLICATION_MASTER = QUINTESSENCE_ARTICLE_FACTCHECK_TRUST_XQ199_2026-08-24.md`
`LATEST_CANDIDATE = QUINTESSENCE_ARTICLE_FACTCHECK_TRUST_XQ203_2026-08-24.md`
`XQ203A_ARTICLE_TEXT_CHANGE = NO`
`XQ203A_TRACEABILITY_PATCH = DONE`
`XQ203A_SQLITE_UPDATED = YES`
`XQ203A_YAHOO_X12_FULL_TEXT = RECOVERED`
`XQ203A_CW_EARLIEST_CONFIRMED_CONTEXTUALIZATION = 2020-04-16`
`XQ203A_CONSPIRACY_NEWS_16_DATE = 2020-04-20_CORRECTED`
`XQ203A_EM_DASH_COUNT = 4_FAIL`
`XQ203A_MOBILE_FIGURE_QA = NEEDS_PATCH`
`XQ203A_TERMINOLOGY_QA = NEEDS_PATCH`
`XQ200_FRESQUE_EVENTS = 45`
`REPAIR_STRENGTH_CASES = 6`
`PUBLICATION_DECISION = HOLD_FOR_P0_PATCH`

## XQ203A — faits et décisions qui supplantent l’état XQ203

- Yahoo [19] n’est plus une simple trace indexée : le texte intégral est récupérable et doit être analysé. Il identifie le « ×12 » comme produit d’une modélisation Pasteur et appelle explicitement à la prudence. Les passages XQ203 disant son corps non rejouable doivent être corrigés.
- La contextualisation *Conspiracy Watch* fabrication / fuite accidentelle n’apparaît pas seulement en 2021 : une mise à jour du 16 avril 2020 distingue déjà les hypothèses, 7 jours après le texte du 9 avril. `Conspiracy News #16.2020` est publié le 20 avril 2020, pas le 18.
- La donnée F200-004 a été corrigée et F200-045 ajouté pour conserver l’événement du 16 avril.
- Le cas de réparation *Conspiracy Watch* a été ajouté au pilote (`RS06`) comme contextualisation sur un autre artefact à J+7 ; audience overlap et réparation de propagation restent `UNKNOWN`.
- La note AFP du 29 juin 2021 est confirmée ; la formulation antérieure reste un gap documentaire.
- Le fichier XQ203 contient encore 4 tirets cadratins : la gate typographique n’est donc pas passée.
- Les cinq figures sont suffisantes en nombre. Le problème est mobile : leurs plus petits textes passent à ~3,6–3,7 px si une figure entière de 2 400 px est affichée à 390 px. Pas de nouvelles figures par défaut ; adapter les existantes.
- Acronymes/termes à traiter à la première occurrence : `CLEMI`, `OMS`, `FDA`, `EMA`, `SEAE`, `HAS`, `OR`, `IC`, `ARNm`, `PCR`.
- Cascade d’archive verrouillée : `WEB/INDEX -> WAYBACK -> COMMON CRAWL -> BnF -> TRACES INDIRECTES`.
- SQLite canonique XQ196 retrouvé dans la Library, copie de travail vérifiée puis mise à jour dans `data/QUINTESSENCE_XQ196_INV_FC65.sqlite` : base XQ196 préservée, 22 findings XQ203A + 8 sources + 3 gaps et liens de traçabilité ajoutés ; `PRAGMA integrity_check = ok`.
- Règles négatives : `NO_WAYBACK_CAPTURE != PAGE_NEVER_EXISTED` ; `PAYWALL != DONNÉE PERDUE` ; `TRACE_INDIRECTE != SOURCE_PRIMAIRE`.

## P0 avant promotion de XQ203

1. Corriger les deux passages Yahoo.
2. Recaler la chronologie *Conspiracy Watch* sur le 16 avril 2020, sans transformer cette contextualisation en correction du texte du 9 avril.
3. Supprimer les 4 tirets cadratins.
4. Définir les acronymes/abréviations nécessaires à leur première occurrence.
5. Conserver ouverts AFP pré-29/06 et *Fact & Furious* original/historique.

## P1

1. Adapter les 5 figures existantes en mobile-first.
2. Ajouter uniquement des phrases de consolidation ciblées aux zones de forte densité cognitive.
3. Ne pas appliquer une coupe mécanique de tous les paragraphes longs.

---

## Historique XQ203 préservé

# ARTICLE PREP — État courant XQ203 — 2026-08-24

`PUBLICATION_MASTER = QUINTESSENCE_ARTICLE_FACTCHECK_TRUST_XQ199_2026-08-24.md`
`LATEST_CANDIDATE = QUINTESSENCE_ARTICLE_FACTCHECK_TRUST_XQ203_2026-08-24.md`
`LATEST_CANDIDATE_SHA256 = 26d902f33a5fcc83a72ae698b879fb41b29fb159c300189b5148757c7af6b456`
`XQ202_FROZEN_SHA256 = 4b0044fe7197e7fd344abf09438ebbf43fb8ddfe150676fdbf3a83a0e8987624`
`LAST_FULL_GLOBAL_BAT = XQ195`
`XQ199_PUBLICATION_MASTER_NON_REGRESSION = PASS`
`XQ203_MULTI_ANGLE_REVIEW = RESOLVED_WITH_BOUNDS`
`XQ203_TEXTUAL_FORENSIC_QA = PASS_WITH_BOUNDS`
`XQ203_BODY_WORDS_WC = 11999`
`XQ203_TOTAL_WORDS_WC = 14730`
`XQ203_SOURCES = 112`
`XQ203_CITATION_CALLS = 187`
`XQ203_SECTION_SOURCE_RELATIONS = 151`
`XQ203_UNUSED_SOURCES = 0`
`XQ203_ORPHAN_CITATIONS = 0`
`XQ203_RELATIVE_LINKS = 15/15`
`XQ203_FIGURES = 5/5_SYNCED_PRINT_QA`
`XQ203_FIGURE_STYLE = LATEX_TIKZ_INSPIRED_MONOCHROME`
`XQ203_FIGURE_RASTER = 2400x1500_300PPI_GRAYSCALE`
`XQ203_FIGURE_BW_REDUCED_PROOF = 1200x750_1BIT_PASS`
`XQ203_FIGURE_SEMANTIC_DELTA = NONE_SUBSTANTIVE`
`XQ203_ARTICLE_CLAIM_SOURCE_DELTA_AFTER_FIGURES = NONE`
`FIG_SYNC_PRINT_QA = PASS`
`DELTA_BAT = PASS_WITH_BOUNDS`
`NON_REGRESSION = PASS`
`PUBLICATION_DECISION = PENDING_HUMAN`
`PROJECT_GATE = FIG_SYNC_PRINT_QA -> DELTA_BAT -> NON_REGRESSION -> PUBLICATION_DECISION`

## XQ203 — arbitrages verrouillés

- Le corpus démontre des modes d'échec possibles et des contre-exemples ; il ne mesure ni la profession, ni une prévalence sectorielle.
- Le cycle d'audit est ramené à trois niveaux : sélection en amont ; fidélité, validité probatoire, calibration et temporalité dans le verdict ; correction et réparation en aval. La circulation est transversale.
- Degré de soutien, état du dossier et état du débat sont séparés ; « contesté » ne vaut pas verdict de vérité.
- La « surcertitude » n'est retenue qu'après un test de matérialité ; les compressions éditoriales mineures restent hors catégorie.
- Les quatre passes 14/41 sont des tests adversariaux sur un dossier commun, pas quatre preuves ou réplications expérimentales indépendantes.
- Le recodage des 154 affirmations ne soutient aucun taux général robuste ; deux lectures avaient omis une source Pasteur décisive sur le « ×12 ».
- *EUvsDisinfo* [94] reste un contre-exemple partiel et [95] le décalage de périmètre le plus net ; aucune généralisation de fréquence n'en découle.
- *Factoscope* est borné à la temporalité et au périmètre du verdict ; aucune conclusion globale « Factoscope était faux » n'est autorisée.
- *Fact & Furious* / pharmacovigilance reste non clos ; aucune adjudication globale sans original complet et historique de correction.
- La page Yahoo [19] est conservée comme trace indexée seulement ; son corps non rejouable ne soutient aucun claim fort.
- L'archive premium *Conspiracy Watch* [80] ne sert pas de preuve de contenu ; la contextualisation accessible [81] porte l'analyse.
- Les attestations, le passe sanitaire, le passe vaccinal et l'obligation vaccinale restent attribués à leurs textes successifs ; la légalité est hors champ.
- La portée vers l'audience initiale est `INCONNUE` lorsqu'elle n'est pas mesurable ; aucune audience commune n'est supposée.
- L’ouverture AFP/Spike est auditée proposition par proposition : plusieurs experts interviennent, mais la non-circulation catégorique repose sur un seul expert ; les autres avis soutiennent surtout l’absence de preuve de toxicité. Le verdict causal reste défendable, la prémisse absolue ne l’est pas.
- Les sources [104] à [112] documentent la version anglaise AFP, les données réglementaires et expérimentales, les qualifications et publications de l’expert central, ainsi que l’expertise du coauteur de l’étude.
- XQ199 reste le master de publication gelé. XQ203 ne le remplace qu'après décision éditoriale humaine explicite.
- Les cinq figures sont en SVG éditable et PNG niveaux de gris à 300 ppp. Le style est inspiré de LaTeX/TikZ, mais les SVG ne sont pas des exports compilés depuis TikZ. L’épreuve numérique N&B est passée ; une épreuve papier physique reste non effectuée.

## Gaps non bloquants si les bornes XQ203 sont conservées

1. AFP France Bridle 18/06/2021 pré-mise à jour : copie intégrale toujours ouverte.
2. *Fact & Furious* pharmacovigilance : original et historique toujours ouverts.
3. Audience effective des corrections françaises : métriques publiques insuffisantes ; statut `INCONNUE` maintenu.
4. Aucun taux sectoriel d'erreur, de biais ou de réparation à produire à partir du corpus ciblé.
5. `PUBLICATION_DECISION` reste un arbitrage humain ; le BAT technique ne vaut pas promotion automatique.

---

## Historique pré-XQ203 préservé

# ARTICLE PREP — État courant XQ200 — 2026-08-24

`CURRENT_ARTICLE = QUINTESSENCE_ARTICLE_FACTCHECK_TRUST_XQ199_2026-08-24.md`
`CURRENT_SHA256 = 845c95e47f534f8cebb560877f3a4683c85b2e7b92bc441f0a705bae2da96175`
`LAST_FULL_GLOBAL_BAT = XQ195`
`POST_XQ195_DELTA_BAT = XQ199_PASS_WITH_BOUNDS`
`TRACEABILITY = CONSOLIDATED_XQ199`
`ARTICLE_TEXT_CHANGE_XQ197 = NO`
`XQ198_ECOSYSTEM_BOUNDARY_AUDIT = CLOSED_WITH_BOUNDS`
`ARTICLE_TEXT_CHANGE_XQ198 = NO`
`ARTICLE_TEXT_CHANGE_XQ199 = BOUNDARY_PATCH_INTEGRATED`
`XQ199_NON_REGRESSION = PASS`
`PUBLICATION_GATE_XQ199 = READY_FOR_PUBLICATION_DECISION`
`XQ200_FRESQUE = CLOSED_WITH_BOUNDS`
`XQ200_PATCH = EDITORIAL_CANDIDATE_ONLY`
`PROJECT_GATE = EDITORIAL_ARBITRATION_XQ200_PATCH`

## Contrat de traçabilité

Toute modification matérielle future doit produire au minimum :
- un événement dans `QUINTESSENCE_ARTICLE_CONSTRUCTION_TRACE_CURRENT.*` ;
- un delta claim/source si une assertion factuelle change ;
- une mise à jour du registre de sources si une référence entre ou sort ;
- une mise à jour `section -> source` si la structure bouge ;
- un statut explicite `FACT / INFERENCE / UNKNOWN / DECISION` ;
- un impact de gate et, si nécessaire, un impact figure ;
- un hash de l’article candidat.



## XQ199 — patch effectivement publié dans le candidat

- une sous-section courte « Une étiquette aux frontières poreuses » est ajoutée avant l’analyse générale ;
- six références nouvelles [72]→[77] documentent Conspiracy Watch, CLEMI, Fake Off, CheckFirst et Hoaxbuster ;
- aucune formulation « Conspiracy Watch n’est pas un fact-checker » n’est conservée ;
- aucune absence de certification n’est transformée en preuve d’erreur ou de biais ;
- diff XQ196→XQ199 : 2 insertions uniquement, 0 suppression, 0 remplacement ;
- 77 sources, 130 appels, 107 relations section→source ; 5 figures inchangées ;
- BAT delta post-XQ195 : `PASS_WITH_BOUNDS` ; non-régression : `PASS`.

## XQ198 — règle de catégorie avant publication

- `FACT_CHECKER_STRICT != DEBUNKER != EMI != RESEARCH/MONITORING != TOOL != INSTITUTIONAL_STRATCOM`
- `CERTIFICATION != TRUTH`
- `NON_CERTIFIED != FALSE`
- `CONSPIRACY_WATCH = HYBRID_SPECIALIZED_PRESS_DEBUNKING`
- `CONSPIRACY_WATCH_NOT_A_FACTCHECKER_ABSOLUTE = BLOCKED`
- `CHECKFIRST = TECH_RESEARCH_MONITORING_INFRASTRUCTURE`
- `FAKE_OFF_ASSOCIATION != 20_MINUTES_FAKE_OFF`
- `EU_DISINFOLAB = RESEARCH_MONITORING_POLICY_ADVOCACY`
- `EUVSDISINFO = EEAS_INSTITUTIONAL_MONITORING_DEBUNKING`
- `VERA = AI_FACTCHECK_TOOL_NOT_NEWSROOM`
- `CW_IFCN_2026 = CURRENT_CERTIFICATION_CONFLICT / HISTORICAL_STATUS_UNKNOWN_ACCEPTED`
- balayage acteurs = **fermé**, 14 acteurs / 33 preuves / 6 cas label-drift ;
- aucune modification XQ196 ; le bloc article proposé dans le rapport XQ198 est un **patch candidat** soumis au BAT delta s’il est adopté.

## Gaps courants

- `G65-01` — HIGH: Retrouver copie intégrale AFP France Bridle du 18 juin 2021 — `OPEN`
- `G65-02` — HIGH: Construire contrôle apparié français 20-40 claims fact-check vs journalisme non labellisé — `OPEN`
- `G65-03` — HIGH: Mesurer audience overlap de corrections françaises — `OPEN`
- `G65-04` — MEDIUM_HIGH: Réplication indépendante de Louis-Sidois sur fenêtre post-2021 — `OPEN`
- `G65-05` — MEDIUM: Classer historiquement correction vs update vs reformulation AFP — `OPEN`

---

## Historique antérieur préservé

# QUINTESSENCE — ARTICLE PREP CURRENT

**Date :** 2026-08-21  
**Current article :** `QUINTESSENCE_ARTICLE_FACTCHECK_V7C_2026-08-20.md`  
**Master :** 70057 records, integrity `ok`, duplicate IDs/keys `0/0`.

## Modèle survivant

`INFRASTRUCTURE DISTRIBUÉE = STRONGLY_SUPPORTED`  
`MONOLITHIC CONTROL = REJECTED`  
`MONEY -> FRAME | CAPACITY | EARMARK | EXIT | ANTICIPATION = STRONG`  
`MONEY -> VERDICT DIRECTION = NOT ESTABLISHED`  
`CURRENT POLITICAL SELECTION BIAS 2022_2026 = OPEN`  
`FACTEUR OVERLAP -> FAVORITISM = NOT ESTABLISHED`  
`CORRECTION -> RETROACTIVE REPAIR = OPEN`  
`AI INTENDED USE -> SPECIFIC EXECUTION = OPEN`

## V7 restored mechanisms

- sédimentation 2018-2026 ;
- STVD self-falsification ;
- sélection -> corpus -> appariement/priorisation -> sélection ;
- activité rémunérée vs coût marginal public de l'erreur ;
- certification empirique/remédiations + limites ;
- FACTEUR overlap + recusal audit gap ;
- propriété/licence/IA + Vera source gate ;
- ontology translation + prospective reversibility != retroactive repair.

## Gates

`V7_MECHANICAL_QA = PASS`  
`V7_FORENSIC_BOUNDARIES = PASS`  
`V7_TARGETED_JURIST_FACTCHECK_EDITOR_SCAN = PASS`  
`TRIPLE_REVIEW_V7C = PASS`  
`POST_INTRO_NON_REGRESSION = PASS`  
`POST_REWRITE_READER_QA = PASS`  
`RIGHT_OF_REPLY = OPEN`  
`PUBLICATION = HOLD_RIGHT_OF_REPLY_ONLY`

## STOP

Aucune nouvelle collecte horizontale nécessaire pour écrire. Les discriminants restants demandent données non publiques, accès de recherche, corpus longitudinal ou expérimentation.

## V7C

- article courant : `QUINTESSENCE_ARTICLE_FACTCHECK_V7C_2026-08-20.md` ;
- compression V7 -> V7C : -22,4 % sur le corps ;
- aucune source V7 perdue : 70 notes, 90 URL distinctes conservées ;
- aucun invariant central identifié comme perdu ;
- master preuves inchangé ;
- prochaine étape publication : triple revue intégrale V7C + droit de réponse.

## Triple revue complète V7C — 2026-08-20
`TRIPLE_REVIEW_V7C = PASS`
`CONTENT_GATE = PASS`
`RIGHT_OF_REPLY = OPEN`
`PUBLICATION = HOLD_RIGHT_OF_REPLY_ONLY`

Micro-réparations : Meta label/57,8 %, currentness Meta, RiPOST exposition, attribution Logically, note FACTEUR falsifiable, anglicismes/tokens labo.


## Introduction personnelle — intégrée
- `Pourquoi cette enquête` ouvre désormais l'article avant la métrique Meta.
- Fonction : raccorder le fact-checking au corpus des verrous sans transformer l'expérience personnelle en preuve générale.
- Axe : `DROIT_FORMEL != PRISE_RÉELLE` ; `LIBERTÉ_DE_PARLER != POUVOIR_D_ÊTRE_ENTENDU`.
- Corps probatoire, sources et invariants inchangés.


## Réécriture éditoriale lecteur — 2026-08-21
- fond et sources inchangés ;
- article réécrit intégralement pour lisibilité, pédagogie et qualité du français ;
- acronymes/termes obscurs définis à la première apparition ;
- jargon technique traduit ou expliqué ;
- 70/70 notes et 90/90 URL conservées ; invariants critiques PASS ;
- `POST_REWRITE_JURIST_SCAN = PASS` ; `POST_REWRITE_FACTCHECK_SCAN = PASS` ; `POST_REWRITE_EDITOR_SCAN = PASS`.

## P0-D — INV-FC-51 / Pasteur ×12
- Investigation ajoutée au socle de préparation uniquement ; article V7C non modifié automatiquement.
- Claim publiable borné : `MODEL_OUTPUT != DIRECT_EMPIRICAL_MEASUREMENT`.
- Claim publiable borné : `PUBLIC_REPRODUCIBILITY_AT_T = NO` pour le code public retrouvé.
- Gap discriminant : validation empirique directe/hors échantillon du `12,1`.
- Interdit : « modèle non scientifique », « bricolage », « fraude », « Macron savait que c’était faux » sans pièce supplémentaire.
- Next : XQ130–XQ139 sur fact-check/correction du ×12, puis chaîne modèle→politique.

## INV-FC-58 / XQ179 — matrice intégrée de confiance
- 24 cas fact-check; 22 scorés; corpus ciblé/non aléatoire.
- Core Quality global 71.4% = descriptif seulement.
- `NARROW_FACT = 100.0%` vs `EVOLVING_SCIENCE = 46.8%` dans cet échantillon.
- Réparation moyenne applicable = 37.5%.
- `ZERO_UTILITY = REFUTED`.
- `DEFAULT_EPISTEMIC_AUTHORITY = NOT_SUPPORTED`.
- Sélection exclue du score central; biais politique sectoriel non quantifiable sans dénominateur.
- Next : XQ180 red-team/sensibilité avant architecture article.

## INV-FC-59 / XQ180 — red team matrice
- Direction `NARROW_FACT > EVOLVING_SCIENCE` survit au stress pro-fact-check (22.2%), au retrait de Repair (51.9%), au retrait FC020–23 (33.3%) et leave-one-out (49.0%–59.9%).
- Break-test : retirer 6/9 cas faibles de science évolutive réduit l'écart à 9.7%; amplitude = composition-dépendante.
- Repair strict 37.5%; généreux 58.3%; contexte=réparation 79.2%; définition doit être explicite.
- `QUALITATIVE_USE=APPROVED`; `SECTOR_PERCENTAGES=BLOCKED`.
- Next : architecture du nouvel article depuis zéro.


## ARCH-TRUST-02 — architecture exécutable post-XQ180

- Ancienne V7/V7C définitivement dépréciée comme architecture de référence.
- Nouvelle question : utilité spécifique du fact-checking et confiance méritée par son label.
- Covid utilisé comme crash-test, pas comme échantillon de prévalence.
- Architecture 11 blocs + 5 critères : Sélection, Fidélité, Calibration, Temporalité, Réparation.
- Six paquets P1–P6 créés avec claims, cas, contre-preuves, formulation maximale, formulations interdites et transition.
- Gate XQ180 conservé : patterns qualitatifs autorisés, pourcentages sectoriels interdits.
- Prochain livrable : DRAFT_V0 avec traçabilité et scan des phrases non supportées.


## P0 article complet — 2026-08-22
`P0_A_TRACEABILITY = DONE`
`P0_B_SECOND_CODER_PACKAGE = READY_EXTERNAL_RESULT_PENDING`
`P0_C_RIGHT_OF_REPLY_PACKET = READY_SEND_PENDING`
`P1 = NOT_STARTED`

### Continuité éditoriale verrouillée
Le nouvel article est la suite de : https://giak.substack.com/p/qui-fabrique-lautorite-du-vrai

Ne pas redévelopper l'infrastructure déjà couverte (plateformes, argent, certifications, sélection, données, réparation). Lien + rappel très court, puis retour immédiat au crash-test Covid et à la confiance dans le label.

### Second coder
Paquet externe à transmettre : `QUINTESSENCE_SECOND_CODER_BLIND_154_2026-08-22.zip`.
Ne pas transmettre : `QUINTESSENCE_SECOND_CODER_INTERNAL_DO_NOT_SEND_2026-08-22.zip`.
Le retour attendu doit contenir `SECOND_CODER_REPORT.md` avec les 154 codes et un bloc CSV machine-readable.

## Nouvel article confiance fact-check — P1 2026-08-22

**Current article :** `QUINTESSENCE_ARTICLE_FACTCHECK_TRUST_P1_2026-08-22.md`

### Axe éditorial
`QUESTION = utilité spécifique du fact-checking + confiance méritée par le label`
`COVID = CRASH_TEST / NOT PREVALENCE_SAMPLE`
`PRIOR_ARTICLE = https://giak.substack.com/p/qui-fabrique-lautorite-du-vrai`
`NO_REPEAT_INFRASTRUCTURE = LOCKED`

### Résultats robustes intégrés
- vérifications étroites : utilité réelle démontrée ;
- science évolutive : vulnérabilités de fidélité/calibration/temporalité/réparation documentées ;
- `×12 = C2_UNANIMOUS_3_OF_3` dans le test de reproductibilité communication ;
- `9000_QUOI_QUE_NOUS_FASSIONS = NON_C0_3_OF_3 / C2_MAJORITY_2_OF_3` ;
- `ALL_NON_C0_3_OF_3 = 10` ; `UNANIMOUS_C0 = 46` ;
- `GLOBAL_OVERCERTAINTY_RATE = BLOCKED` ;
- `GENERALIZED_OVERCERTAINTY = NOT_SUPPORTED` ;
- `FINE_C0_C1_RELIABILITY = LOW` ;
- majorité de codeurs != preuve ; sources primaires restent décisives.

### P1 appliqués
- continuité/DRY avec article précédent ;
- causalités financeur -> verdict non répétées ;
- FACTEUR/Désinfox/Meta retirés du corps détaillé ;
- Louis-Sidois conservé comme contre-preuve compacte ;
- rival urgence/vulgarisation intégré ;
- autorité épistémique reformulée en conclusion bornée ;
- réparation distinguée de contextualisation sans généraliser l’asymétrie d’audience.

### Gates
`P0_A_TRACEABILITY = CLOSED`
`P0_B_REPLICATION = CLOSED_WITH_DOCUMENTARY_RESERVATION`
`P1 = APPLIED`
`P0_C_RIGHT_OF_REPLY = READY / SEND_PENDING`
`PUBLICATION = HOLD_RIGHT_OF_REPLY`

### QA
- ~5237 mots ;
- 0 tableau Markdown ;
- 0 tiret cadratin ;
- sources pivots inline + annexe de 34 pièces ;
- prochain travail : contradictoire ciblé puis BAT juriste/fact-checker/rédacteur en chef.


## Politique de liens — 2026-08-22
`BODY_EXTERNAL_URLS = 0`
`BODY_SUBSTACK_WIKILINKS = 2`
`SOURCE_URLS = END_SECTION_ONLY`
`FIGURE_LINKS = RELATIVE_LOCAL`
Règle : aucune source externe hyperliée dans la prose ; nommer la source organiquement et consolider l’URL dans `## Sources`.

## Clôture technique XQ199

- `TECHNICAL_PERSISTENCE = COMPLETE`
- `SQLITE_META = XQ199 / INTEGRITY_OK`
- `FINAL_MANIFEST = QUINTESSENCE_XQ199_FINAL_MANIFEST_2026-08-24.json`
- `FINAL_BUNDLE = QUINTESSENCE_XQ199_FINAL_TRACEABILITY_BUNDLE_2026-08-24.zip`
- Cette clôture ne modifie pas le texte de l’article ni son SHA-256.


## XQ200 — état préparatoire

L'enquête longitudinale sur les acteurs fact-check/adjacents identifiés en XQ198 est close avec bornes : **44 événements**, **13 claims**, **10 réparations/contextualisations**, **17 reprises**, **6 gaps**.

Le patch article a été red-teamé mais **n'est pas injecté**. P0 principal corrigé : ne jamais transformer le cas *Conspiracy Watch* en preuve rétrospective que l'organisation aurait eu « tort sur la fuite de laboratoire ». Le finding admissible porte sur le périmètre/catégorie et la calibration du vocabulaire.

Contrôles positifs conservés : *20 Minutes / Fake Off*, *Hoaxbuster*, *EU DisinfoLab*, et réparation explicite de la *Tronche en Biais*.

Prochaine décision : **injecter ou non le patch XQ200**. Si oui, produire une version article suivante + renumérotation des sources + BAT delta/non-régression.

## XQ204 - état final post-rollback

- `CURRENT_CANDIDATE = QUINTESSENCE_ARTICLE_FACTCHECK_TRUST_XQ204_2026-08-25.md`
- `SHA256 = 0ddd1ab44ff314d10b49be90036c360374727a2b5f6f1bb64f7e26ad6e051b4e`
- `PASS_A_PROBATIVE = VALIDATED`
- `PASS_B_LANGUAGE_TYPOGRAPHY = VALIDATED`
- `PASS_C_COGNITIVE_READABILITY = VALIDATED`
- `PASS_D_MOBILE_FIGURES = REJECTED_VISUAL_REGRESSION_YAGNI`
- `FIGURE_ROLLBACK = PASS_BYTE_IDENTICAL_XQ203`
- `PASS_E_FINAL_BAT_POST_ROLLBACK = PASS_WITH_BOUNDS`
- `PUBLICATION_TARGET = SUBSTACK`
- `SOURCES = 113/113 used` ; `CITATION_CALLS = 187` ; `ORPHANS = 0` ; `MISSING_RELATIVE_TARGETS = 0`.
- `EM_DASH = 0` ; `EN_DASH = 0` dans le candidat.
- Figures : 5 SVG + 5 PNG canoniques XQ203 restaurés octet pour octet ; print QA XQ203 conservé.
- Variantes D : archivées uniquement sous `annexes/rejected/XQ204_PASS_D_VISUAL_REGRESSION/`, jamais référencées par l’article.
- Registre de réparation synchronisé à 6 cas ; fresque synchronisée à 45 événements.
- Borne ouverte 1 : formulation exacte AFP Bridle avant la reformulation du 29/06/2021 non récupérée.
- Borne ouverte 2 : original complet + historique Fact & Furious pharmacovigilance non récupérés.
- `PUBLICATION_GATE = PASS_WITH_BOUNDS / READY_FOR_HUMAN_SUBSTACK_PUBLICATION_REVIEW`.
- `NO_SECTOR_PREVALENCE = LOCKED`.
- `NO_FIGURE_REDESIGN_WITHOUT_EXPLICIT_REQUIREMENT = LOCKED`.

## XQ205 — clôture du brief éditorial initial

- `CURRENT_CANDIDATE = QUINTESSENCE_ARTICLE_FACTCHECK_TRUST_XQ205_2026-08-25.md`
- `SHA256 = 8acc476d3ea644668c3c3e47f448c2e46d4b6985dcbd9560cfbdf867e5df1a7a`
- `EDITORIAL_BRIEF_XQ204F = COMPLETED`
- `FRENCH_TYPOGRAPHY = PASS` ; `EM_DASH = 0` ; `EN_DASH = 0`
- `COGNITIVE_AIDS = reader_map + 3 mini_schemes + 4 local_takeaways + establish/not_establish`
- `PARAGRAPHS_GT_100_WORDS = 0`
- `FIGURES = XQ203_CANONICAL_UNCHANGED`
- `SOURCES = 114/114 used/defined` ; `CITATION_CALLS = 188`
- `FACT_FURIOUS_ARCHIVE = PARTIAL_RECOVERY / NO_GLOBAL_VERDICT`
- `AFP_BRIDLE_PRE_29_06_EXACT_WORDING = STILL_NOT_RECOVERED / NON_BLOCKING_WITH_BOUND`
- `PUBLICATION_GATE = PASS_WITH_DOCUMENTARY_BOUNDS`
- audit : `annexes/XQ205_FINAL_EDITORIAL_FORENSIC_AUDIT_2026-08-25.md`
- archéologie : `data/XQ205_ARCHAEOLOGY_REGISTRY_2026-08-25.csv`


### XQ205 — red-team final

- `WAYBACK_DIRECT_ROUTE = ROUTE_INCONCLUSIVE / NO_NEGATIVE_INFERENCE`
- `NO_USABLE_CAPTURE_IN_TOOL != NO_ARCHIVE_EXISTS`
- `FIGURE_HASH_RECHECK = 10/10 PASS_BYTE_IDENTICAL_XQ203`
- `FINAL_ARTICLE_MECHANICAL_BAT = 114/114 SOURCES ; 188 CALLS ; 0 ORPHAN ; 0 MISSING RELATIVE ; 0 EM/EN DASH ; 0 MD TABLE`
- `MAX_PROSE_PARAGRAPH = 92 WORDS ; GT100 = 0`
- `SQLITE_INTEGRITY = OK`
