# RUN_MANIFEST - Pilote Avenants SESN (Phase 1)

- RUN_ID : RUN-2026-08-10-01
- Protocole : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_preparation-anticorruption/protocole/2026-08-10_07-10_pilote-avenants-sesn_ARCHITECTURE.md` (v1.1, contrat d'exécution)
- KERNEL : `truth-engine-v2/KERNEL.md` (pipeline v2.8)
- Ouverture : 2026-08-10 08:47 CEST
- STATUT : **CLOS** (clôture 16:30, décision utilisateur : clore et capitaliser ; bilan : aucune corruption prouvée, 3 cas requalifiés réguliers, fait systémique documenté = invisibilité des 148 avenants dans les données ouvertes ; leçons dans `2026-08-10_preparation-anticorruption/doctrine/2026-08-10_16-30_legons-pilote-sesn_LEÇONS.md`)
- STATUT historique : OPEN (Phase 1 livrée ; Phase 2 TERMINÉE 13:00 ; Phase 3 TERMINÉE 14:20 ; Phase 4 TERMINÉE 15:10, revue 0 P0/0 P1/2 P2 appliqués ; Vérification SMDA TERMINÉE 14:31 ; Vérification Ribécourt TERMINÉE 14:35 ; Vérification A3 TOARC TERMINÉE 14:43 ; Documentation CCIR/Ribécourt TERMINÉE 14:51 ; Phase 8 OUVERTE 14:58 ; Vérification 1 durée TOARC TERMINÉE 15:07 ; Vérification 2 capacité SMDA TERMINÉE 15:13 ; Vérification 3 proportionnalité Ribécourt TERMINÉE 15:19 ; **Synthèse finale Phase 8 LIVRÉE 15:22** : `2026-08-10_15-22_avenants-sesn-pilote-synthese_SYNTHESE.md` (copie hashée `data/synthese_phase8_sesn.md`, sha256 31a55209..., `data/synthese_phase8.sha256`), 0 em-dash ; **Question V3 (montage Ribécourt marché public vs DSP) EXÉCUTÉE 15:53** : dossier `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_montage-ribecourt-v3/2026-08-10_15-53_montage-ribecourt-v3_INVESTIGATION.md` (12 FCT, 3 GAP, sha256 1ad82ee3...), verdict : choix structurellement contraint (SCSNE société de projet à dissolution, transfert de risque CCP L.1121-1, DSP CGCT L.1411-1, actif neuf vs Dourges existant) ; correction de prémisse L.2124-8 ; titulaire DSP Dourges = LDCT DSP (940604721) ; artefacts hashés `artefacts_v3.sha256` OK. ; **Axe 1 gonflement MOE EXÉCUTÉ 15:36 + MAJ 16:00** : dossier `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_gonflement-moe-sesn/2026-08-10_15-36_gonflement-moe-sesn_INVESTIGATION.md` (15 FCT, 3 GAP ouverts + 1 RÉSOLU, sha256 c5f2d4f3...), 4 demandes CADA rédigées (SCSNE ×3 + CdC) dans `data/cada_lettres/`, envoi DELIVERABLE_PENDING ; contradictoire officiel archivé et lu (communiqué 10/04/2026 + réponse Dezobry 16/03/2026 : souscrit aux 5 rec., ne conteste aucun chiffre MOE), `data/contradictoire/` hashé ; **PHASE 10 (dossier final KERNEL) LIVRÉE
- AXE 4 (filière archéologique) : INVESTIGATION 16-17 livrée, 9 faits, verdict H0/H2 FAVORISÉES (concentration 42,29 % expliquée par agrément d'État + contrôle L. 523-9 + prescriptions SRA), hash 0e3f39a5 15:56 + revue appliquée 16:00** : `phase10/2026-08-10_15-56_pilote-sesn-phase10_INVESTIGATION.md` (186 l., 0 em-dash, MANIPULATION_REPORT 15 symboles scorés + BIAS_TEST source-level, FACT_REGISTRY 14 faits, matrices juridiques 432-11/432-14/432-12 sur textes lus, conclusion graduée + escalade 4 niveaux, sha256 353f8459... ; revue : 2 P1 + 2 P2 appliqués, dont vocabulaire « SANS APPUI EN L'ÉTAT / NON ÉCARTÉE » substitué à « PLAUSIBLE conditionnel ») ; restent DELIVERABLE_PENDING : envoi des 4 CADA, questionnaires droit de réponse)
- NEXT_ACTION : Phase 8 → prochaine vérification priorisée : retours du sourcing SCSNE 2022-2023 (avis 22-146482, 23-80795, combien d'opérateurs ont répondu) ; nouvel axe ouvert : avenants MOE SCSNE (11 M€ accordés + 83 M€ en cours + 92-97 M€ MOE unique, rapport CdC 10/04/2026 p. 50-57) + question du montage marché public vs DSP pour l'exploitation de la plateforme de Ribécourt ; Phase 5 (CADA) toujours DELIVERABLE_PENDING

## Périmètre (gelé avant tout calcul)

- Acheteur : SESN (Société du Canal Seine-Nord Europe), établissement public.
- Période : exercices 2021 à 2026 inclus.
- DATE DE COUPURE : 30/06/2026 (gelée avant tout calcul ; les montants partiels de 2026 sont comparés en années pleines, jamais mélangés).
- Recensement : UNIVERS COMPLET des marchés SESN accessibles (DECP consolidées data.gouv, page SCSNE, AWS/BOAMP/TED, PLACE), PAS un tirage des 30 plus gros.
- Marchés sans montant : conservés dans `data/marches_sans_montant.csv`, jamais exclus.
- Unité d'analyse : contrat = données de base + série ordonnée des événements de modification (modèle événementiel).
- Rapprochement inter-sources : par numéro de marché SESN (ex. 21S6I028) puis par identifiant d'avis ; chaque dédoublonnage documenté.
- Complexité attendue : COMPLEX (scorer honnêtement via $CX_SCORE au §0 KERNEL).

## Sources Phase 1 (aucune suffisante seule, rapprochement systématique)

1. DECP consolidées data.gouv.fr (fichiers ministère des Finances) - AVERTISSEMENT : moins exhaustives depuis format 2022 (01/01/2024) ; une absence ne prouve pas l'absence de modification.
2. Page Marchés publics SCSNE : https://www.canal-seine-nord-europe.fr/marches-publics/ (120 résultats, liens avis BOAMP/TED, numéros SESN).
3. Profil d'acheteur AWS : https://www.marches-publics.info/ (support officiel de publication).
4. BOAMP et TED pour les avis (d'attribution et de modification).
5. PLACE (marches-publics.gouv.fr) pour les DECP publiées via profil d'acheteur.

## Modèle événementiel (règle anti-double-comptage, Phase 1 protocole)

- Le champ « Montant modifié du marché public en euros HT » (bloc modifications) = NOUVEAU MONTANT TOTAL après modification.
- INTERDICTION d'additionner les « montant modifié » de plusieurs DECP.
- Montant d'un événement = montant modifié courant - valeur du montant immédiatement précédent (ou montant initial si 1re modification).
- Durée modifiée = durée TOTALE après modification (mois, arrondi supérieur).
- Modifications résultant de clauses de variation de prix = EXONÉRÉES de publication DECP (arrêté 22/12/2022 III) : leur absence n'est pas une absence de modification.

## Contrôle qualité Phase 1

- Nombre total de contrats recensés vs nombre déclaré rapport CdC (74-76 marchés) : écarter ou documenter l'écart ligne par ligne.

## BILAN EXÉCUTION (08:47-09:15 CEST, 2026-08-10)

- **DECP consolidées** (ministère des Finances, dataset 5cd57bf68b4c4179299eb0e9, decp-global.json) : téléchargé (1,0 Go, sha256 73dc1476cc81c9b61060be8434d79e21346831dce1691d4c21413d2a7256b575), filtré SIREN 829535996 (vérifié API recherche-entreprises) : **47 lignes SCSNE** dont **46 dans la fenêtre** (toutes notifiées 2024-2026 ; la 47e, id 2026T17080 notifié 2026-07-03, exclue par la coupure du 30/06/2026), montant cumulé = 526 420 107,98 € HT (**BRUT 46 lignes, pré-dédup ; référence Phase 3 = 103 578 507,98 € HT dédupliqué, voir section TRANCHÉ DOUBLON ci-dessous** ; corrigé après double-check, voir § DOUBLE-CHECK). **Le fichier global CONTIENT des DECP de modification** : 508 957 entrées sur 170 557 marchés (sources variées, dont AIFE_PLACE = 51) ; **zéro** sur les 47 lignes SCSNE.
- **GAP-001 Phase 1 CONSTATÉ (affiné)** : la SCSNE n'a publié aucune DECP de modification dans les consolidés (0/47), alors que le format le permet et que d'autres acheteurs alimentent le bloc (508 957 entrées) ; de plus aucune DECP SCSNE avant 2024 (vérifié : decp-2019.json 0/233 213, decp-2022.json 0/384 148). La page marché 21S6I028 portait « DECP en cours de publication par PLACE » (relevé APEX 04/07/2026) : hypothèse de publication tardive/non reversée, à trancher en Phase 3 (PLACE direct accessible ? BOAMP/TED).
- **Page SCSNE** (canal-seine-nord-europe.fr/marches-publics/) : « Les marchés publics de la SCSNE sont publiés sur la plateforme AWS » ; liste statique : 57 numéros de marché SESN (2014-2022) + liens TED/BOAMP ; widget Livewire « 120 résultats », 12 cartes visibles (page racine, récupérées 10/08/2026).
- **AWS marches-publics.info** : recherche avancée (POST /Annonces/lister) par SIRET acheteur 82953599600039 + nom « CANAL SEINE-NORD » : **1 annonce retournée** (réf 000M524, équipements oléohydrauliques, date limite 25/08/2026). Constat : la recherche publique AWS ne couvre qu'une fraction des avis (accès complet réservé aux acheteurs connectés) : GAP à noter, à croiser avec BOAMP/TED.
- **BOAMP/TED** : liens idweb et notices récoltés depuis la page SCSNE (33 notices TED, idweb BOAMP dans les cartes) : recensement `idweb_boamp`/`notice_ted` rempli partiellement ; extraction BOAMP dédiée = DELIVERABLE_PENDING (Phase 1-bis optionnelle).
- **Recensement fusionné** : 115 lignes (`recensement_univers.csv`), 46 DECP + 57 page-SCSNE + 12 widget ; 69 sans montant (`marches_sans_montant.csv`) ; registre des pistes créé vierge (ouvert en Phase 1).
- **Écart vs CdC (74-76)** : 115 recensés > 74-76 (le recensement couvre plus : anciens marchés 2014-2022 + consultations) ; l'écart inverse porte sur les DECP 2021-2023 absentes des consolidés : vérifié par téléchargement direct, 0 SCSNE dans decp-2019.json (233 213 marchés) et decp-2022.json (384 148 marchés). L'hypothèse « publiées sur PLACE, non reversées » reste à confirmer (PLACE direct inaccessible au 10/08/2026).
- **Bug corrigé** : dédoublonnage initial fusionnait les 5 marchés AWS à ID dégradé « 000 » ; corrigé (clé = id + objet pour les ID dégradés), 6 lignes préservées.
- HASH_CAPABILITY : sha256 disponible (scripts 01 + 01b exécutés avec venv /tmp/opencode/pilote-venv, ijson 3.5.1).

## DOUBLE-CHECK Phase 1 (10/08/2026, 09:15-10:10 CEST)

Vérifications indépendantes exécutées sur les artefacts Phase 1, résultats et corrections :

| # | Vérification | Méthode | Résultat |
|---|--------------|---------|----------|
| 1 | Reproductibilité du téléchargement | sha256 reinterpreté sur decp-global.json (1,0 Go) | Identique : 73dc1476cc81c9b61060be8434d79e21346831dce1691d4c21413d2a7256b575 ✓ |
| 2 | Filtre SIREN | Nouvelle passe ijson indépendante (startswith 829535996) vs CSV | 47 lignes JSON ; CSV = 46 (seule exclue : 2026T17080, notifiée 2026-07-03 hors coupure) ✓ |
| 3 | Faux négatifs du filtre | Recherche « canal seine-nord » / « seine nord europe » dans objet + nom acheteur + titulaires de TOUS les marchés non-SCSNE | 5 marchés d'un autre acheteur (20005374200017, ports intérieurs) : HORS PÉRIMÈTRE SCSNE, non pertinents ✓ |
| 4 | Intégrité des montants | Comparaison ligne à ligne CSV vs JSON en Decimal | 0 écart sur 46 lignes ; montants JSON en Decimal (pas de perte float) ✓ |
| 5 | **Sommation cumulée** | Re-sommation : brute 47 = 527 392 024,98 € ; fenêtre 46 = 526 420 107,98 € ; CSV 46 = 526 420 107,98 € | **CORRECTION : le chiffre 514 438 257,98 € publié initialement était faux** (erreur de dédup silencieuse sur les 5 lignes à id « 000 »). Le montant corrigé fait foi : 526 420 107,98 € HT |
| 6 | DECP de modification dans le fichier | Comptage ijson du bloc modifications sur les 704 699 marchés + sous-ensemble SCSNE | 508 957 entrées (170 557 marchés, 24,2 %), 129 167 avec montant, AIFE_PLACE : 51 ; **0 pour les 47 lignes SCSNE** → CORRECTION du BILAN initial (« structure absente » était faux) |
| 7 | DECP SCSNE avant 2024 | Comptage par année dans decp-global.json (le fichier couvre les années antérieures : 1 180 marchés notifiés 2019, 12 714 en 2021, 24 759 en 2022, 57 495 en 2023, soit 100 177 avant 2024) | 0 SCSNE parmi les 100 177 marchés notifiés avant 2024 ✓ (GAP-001-P1b confirmé, preuve fondée sur le global) ; les fichiers annuels décp-2019.json/decp-2022.json ont été re-téléchargés (8 756 items pour 2022, 803 487 pour 2019, ressources flottantes, 0 SCSNE à chaque lecture) mais ne sont pas reproductibles (hashes différents des premières lectures) → exclus du socle de preuve |
| 8 | Structure du fichier | Parsing ijson des clés racine | Un seul nœud racine `marches` (pas de nœud `concessions` dans cet export) ✓ |

**Corrections appliquées** : REGISTRE P1-F02/F03/F03b/F03c/F04 + GAP-001-P1/P1b ; RUN_MANIFEST BILAN ; artefacts de preuve : `data/artefacts_phase1.sha256` (5 artefacts reproductibles) + `data/artefacts_annuels_flottants.sha256` (decp-2019.json 188e6966..., decp-2022.json c185ff8e... au 10/08/2026 10:12, NON reproductibles : data.gouv les réécrit ; exclus du socle Phase 1).

## RECENSEMENT v2 (2026-08-10 13:08 CEST) - Q1-M213 ajouté, ligne AWS corrigée

- `data/recensement_univers_v2.csv` (116 lignes : 46 DECP + 57 page-SCSNE + 12 widget + 1 BOAMP-TED), sha256 73a23a23... ; script `scripts/01c_completer_recensement.py` v2 (revue 0 P0 + 1 P1 + 3 P2 appliqués).
- Lot Q1-M213 (SPIE Batignolles Nord, 2 999 530,10 € HT, conclu 20/11/2025, BOAMP 25-132968 / JOUE 806579-2025) ajouté : ferme le gap de couverture DECP sur les quais.
- Ligne AWS id=000 corrigée : 422 841 600 → 4 228 416 € + marquage DOUBLON_DEFECTUEUX de 2844722.
- Cumul DÉDUPLIQUÉ du recensement : 106 578 038,08 € HT (46 lignes, hors doublons marqués) ; cumul brut 110 806 454,08 € « à NE PAS utiliser » (ligne AWS DOUBLON_DEFECTUEUX jamais sommée). ≠ cumul Phase 3 103 578 507,98 € (DECP seule).

## VÉRIFICATION TED SOURCE PRIMAIRE (2026-08-10 13:20 CEST) - notice 806579-2025 lue en XML eForms

- **✧ sur le JOUE 806579-2025 LEVÉ** : notice TED téléchargée en XML eForms `ContractAwardNotice` (route `ted.europa.eu/udl?uri=TED:NOTICE:806579-2025:XML:FR:HTML`, HTTP 200, 34 175 octets, sha256 `3d064d1abb3e2facc5acaa4d62890edcef251725ac3f36be2324ef5c569e68ef`, copie `data/notice_ted_806579-2025_ContractAwardNotice.xml` + `.sha256`).
- **Montants confirmés à la source primaire** : TEN-0001 (Q1-M213) = 2 999 530,10 € → SPIE Batignolles Nord (Calais 62100, « large ») ; TEN-0002 (Q2-M214) = 4 228 416,00 € → SAS CHARIER Génie Civil - Agence de Paris (Lognes 77437) ; total 7 227 946,10 € ; contrats CON-0001/CON-0002 conclus 2025-11-20 ; acheteur SCSNE (Compiègne 60204) ; 3 offres Q1 / 4 offres Q2 ; CPV 45241100.
- **Cohérence à 100 % avec le BOAMP XML DILA (12:47)** : le tranchement du doublon ×100 est définitif (aucun avis ne connaît de quais à 422 M€).
- **Route UDL documentée au playbook §3.14** (playbook-acces-donnees, GAP-003 : 4 routes validées). Échecs documentés : page détail JS (contenu vide en curl/jina), API v3 (401), /api/publication/download (404), SPARQL data.ted (0 binding / 405), Wayback (aucun snapshot).

## RECENSEMENT v3 (2026-08-10 14:00 CEST) - 5 avis widget enrichis en source primaire

- `data/recensement_univers_v3.csv` (116 lignes, sha256 18361205...) ; script `scripts/01d_completer_avis.py` (déterministe, 0 LLM, hash stable).
- **Découverte route DILA 2026** : nouveau schéma `/OPENDATA/BOAMP/2026/<mois>/<jour>/` (le FluxHistorique v240 s'arrête fin 2025) ; index Apache navigable par jour, idweb localisés par balayage.
- **M404** (25-130941, 2025/11/26, BOAMP XML) : réhab. quai travaux d'Havrincourt (Graincourt), PK17.900, CPV 45453000, consultation (AWS Idm=1745063).
- **M405** (25-124779 + TED 747456-2025, 2025/11/09) : déboisement secteur 4, CPV 77211400, consultation.
- **M522** (TED 389639-2026, 2026/06/08) : vérins oléohydrauliques portes amont écluses, consultation (F-PF-1831411).
- **M524** (TED 485750-2026, 2026/07/14) : travaux 4 métiers, CA 80 M€, consultation 2 étapes (T-PF-1842014).
- **MC04** (BOAMP 26-72063 + TED 502268-2026, 2026/07/21) : **ATTRIBUTION 498 522,46 €** à Pinson Paysage (Andilly 95580) : prestations de génie écologique + petits terrassements, mesures compensatoires hors emprises (Ex-B131 Lot B), CPV 90710000, 3 offres, option « Prestations d'Ecologue » 16 475,00 €.
- **CONSTAT (corrigé après revue 14:05)** : seul 26-72063 EXISTE dans le flux DILA 2026 (2026/07/21, HTTP 200, 66 103 o, avis d'attribution MC04, concordance 100 % avec le TED). Les idweb widget 26-55339 et 26-69739 N'EXISTENT PAS dans le flux DILA 2026 (absents des index, 404) : hypothèse identifiants AWS (Idm), pas BOAMP. Pour un idweb 2026 : vérifier l'existence dans l'index AVANT de chercher ; si absent, passer par la notice TED.
- **Cumul recensement v3 dédupliqué : 107 076 560,54 € HT** (47 lignes à montant) = v2 106 578 038,08 + MC04 498 522,46. Phase 3 DECP inchangée : 103 578 507,98 €.
- Point de vigilance : les 3 avis 2026 (08/06, 14/07, 21/07) sont postérieurs à la coupure 30/06/2026 : hors socle Phase 1, à intégrer si la fenêtre s'élargit.

## TRANCHÉ DOUBLON (2026-08-10 12:47 CEST) - section ajoutée au REGISTRE

- La ligne AWS id=000 (422 841 600 €, « réhabilitation de 4 quais », marches-publics_aws) est un DOUBLON DÉFECTUEUX du contrat M214-Lot Q2 (4 228 416 €, Charier GC, quai neuf de Catigny), déjà compté via DECP PLACE 2844722. Erreur d'unité ×100 (centimes/euros) dans la publication AWS.
- Source primaire : avis BOAMP 25-132968 (XML DILA lu intégralement) / JOUE 806579-2025, marché M215 = M213 (Q1, 2 999 530,10 €, SPIE Batignolles Nord) + M214 (Q2, 4 228 416 €, CHARIER GC), total 7 227 946,10 €, conclus 2025-11-20. Aucun avis ne connaît de quais à 422 M€.
- **CUMUL DE RÉFÉRENCE PHASE 3 (dédupliqué) : 103 578 507,98 € HT** (corrige le 526 420 107,98 € brut ; le « ~107 M€ » du CR 12-39 était une correction sans dédup = double comptage du Q2).
- Artefacts : `data/decp_sesn_raw_v2.csv` (46 lignes, montant corrigé + colonne correction_doublon, sha256 a0bf10e6...), `scripts/02_corriger_doublon.py`.
- Fait nouveau : Q1-M213 (SPIE) absent des DECP consolidées (gap de couverture, pas anomalie de montant).

## VÉRIFICATION SMDA (2026-08-10 14:31 CEST) - conformité allotissement des 2 marchés de génie écologique

- **Demande utilisateur** : vérifier la conformité des 2 marchés SMDA (12 134 059,78 € + 8 641 524,06 €, A1 de la Phase 4) via les avis BOAMP/TED et les règles d'allotissement.
- **VERDICT : CONFORME** (détail dans le REGISTRE, section datée 14:31). Chaîne probatoire en XML lu intégralement : AAPC BOAMP 25-17720 (14/02/2025, M230, procédure ouverte, 2 lots 2.1 Sud / 2.2 Nord annoncés dès l'origine en un seul avis, nb max 2 lots par soumissionnaire, seuils de CA 3 M€/2 M€/5 M€ cumulés, date limite 15/04/2025, fonds UE MIE) ; rectificatif 25-38762 (06/04/2025, report au 14/05/2025) ; attribution BOAMP 26-37280 (14/04/2026, M231 = 12 134 059,78 € + M232 = 8 641 524,06 €, 5 offres par lot, SMDA Trappes, option 1 883 515,50 €, qualité 40/prix 60, CPV 45110000, procédure 1b836649-c3c6-43e8-a087-d673fdc3eb86).
- **Lecture du signal A1 mise à jour** : concentration confirmée (20,1 % du corpus, 2 lots max autorisés obtenus), PAS d'anomalie procédurale. La question Phase 8 devient « pourquoi SMDA sur les 2 lots max ? » (qualification, prix, historique), pas « l'attribution est-elle régulière ? ».
- **Route API validée (ajout playbook)** : API OpenDataSoft BOAMP (dataset `boamp`, ~1,7 M avis) = recherche d'avis par texte objet + tri date décroissante (a retrouvé 25-17720, 25-38762, 26-37280).

## VÉRIFICATION RIBÉCOURT (2026-08-10 14:35 CEST) - cas A2 : fondement de la procédure + contrôle du montant

- **Demande utilisateur** : vérifier le marché Ribécourt (CCIR HDF, 4,9 M€, offre unique en négociation) : fondement de la procédure sans concurrence et contrôle du montant.
- **VERDICT** : fondement RÉGULIER, montant CONTRÔLÉ, concurrence faible AVÉRÉE (détail dans le REGISTRE, section datée 14:35). XML DILA lus intégralement : AAPC BOAMP 25-21716 (25/02/2025) + attribution BOAMP 26-68097 (08/07/2026, conclu 12/06/2026).
- **Fondement** : procédure négociée AVEC publication préalable d'un AAPC (art. R.2124-3 CCP), non accélérée, deadline offres 28/03/2025 12:00, notice TED 129383-2025 : PAS de procédure sans publicité. L'hypothèse implicite de la Phase 4 (contournement de publicité) est INVALIDÉE.
- **Montant** : triple concordance 4 900 000 € HT (AAPC « montant maximum sur 4 ans » = attribution « valeur maximale accord-cadre » = DECP). Aucun gonflement. Accord-cadre sans remise en concurrence, 48 mois (≈ 102 083 €/mois), renouvellement 0, début estimé 01/10/2025.
- **Concurrence** : 1 seule offre reçue (tenders 1, e-submission 1) malgré la publication : signal de concurrence faible AVÉRÉ, procéduralement régulier. Question Phase 8 : « pourquoi 1 seul opérateur a-t-il répondu ? » (monopole consulaire de fait de la CCIR HDF sur la plateforme de Ribécourt-Dreslincourt ? spécificité technique ? attractivité).
- **Capacité** : CA ≥ 9 800 000 € sur 3 exercices (2× montant) ; pondération qualité 60 / prix 40. Durée de procédure : ~15 mois (AAPC 25/02/2025 → conclusion 12/06/2026).
- **Artefacts** : `data/avis_boamp_25-21716_AAPC_ribecourt.xml` + `data/avis_boamp_26-68097_attribution_ribecourt.xml` + `avis_ribecourt.sha256` (a912104a…, 5583987d…).

## VÉRIFICATION A3 TOARC (2026-08-10 14:43 CEST) - fondement de la dispense des 3 MOE

- **Demande utilisateur** : vérifier le fondement de la procédure « sans publicité ni MEC » des 3 MOE (Egis ×2, Arcadis, 517 854,25 €) : chercher l'accord-cadre parent (18TRI001B/C) et trancher (R.2122-8 vs marchés subséquents d'accord-cadre).
- **VERDICT : DISPENSE FONDÉE** (détail REGISTRE 14:43). Les 3 marchés (2706994, 2707054, 2707074) sont des **marchés subséquents d'accords-cadres MONO-ATTRIBUTAIRES** : AAPC BOAMP 18-50453 (15/04/2018, JOUE 2018/S 075-167044) « Marchés de maîtrise d'oeuvre TOARC – Secteurs 2, 3 et 4 », REF_MARCHE 18TRI001BCD, 3 lots (B/C/D), durée 144 mois, accords-cadres mono-attributaires à bons de commande et marchés subséquents (décret 2016-360 art. 78-80) ; attribution BOAMP 19-178514 (05/12/2019, décision 13/11/2019) : total 84 127 774 €, lot 2 = groupement ONE conduit par EGIS (35 627 119 €), lot 3 = ARCADIS (22 562 587 €).
- **Dispense légale** (R.2162-13 s. CCP : marchés subséquents d'accord-cadre mono-attributaire sans nouvelle publicité/MEC) ; **R.2122-8 inapplicable** (contrats non autonomes). Critère A3 de la Phase 4 INVALIDÉ comme anomalie procédurale.
- **Point de vigilance résiduel** : durée de 12 ans de l'accord-cadre > plafond de 4 ans (R.2162-5, ex-art. 79 décret 2016-360) : justification exceptionnelle à vérifier dans le DCE (PLACE refConsultation 373666, DELIVERABLE_PENDING).
- **Artefacts** : `data/toarc_18-50453_AAPC_donnees.json` + `data/toarc_19-178514_attribution_donnees.json` + `toarc_avis.sha256` (83d2b9c8…, b6a04d8b…).

## DOCUMENTATION CCIR / RIBÉCOURT (2026-08-10 14:51 CEST) - position de l'exploitant, monopole consulaire

- **Demande utilisateur** : documenter la position de la CCIR HDF sur la plateforme trimodale de Ribécourt : statut d'exploitation, historique des marchés antérieurs, test de l'hypothèse du monopole consulaire de fait (question Phase 8 du cas A2).
- **Verdict** : faisceau de monopole consulaire de fait PLAUSIBLE mais NON prouvé (détail REGISTRE 14:51). Points établis : (1) la plateforme est une infrastructure NEUVE (travaux SCSNE 26-6458, 2026, adossée aux quais du canal latéral à l'Oise CLO, domaine public fluvial VNF) : pas d'exploitation antérieure possible ; (2) l'exploitation est un marché public de services (accord-cadre 4,9 M€/48 mois), pas une délégation de service public ; (3) le sourcing 2022-2023 (avis 22-146482, 23-80795, art. R.2111-1) documente une préparation longue de la SCSNE ; (4) le critère de capacité (gestion de plateforme multimodale avec ITE, manœuvres ferroviaires, locotracteurs, CA ≥ 9,8 M€) est aligné sur le métier de la CCIR via Ports de Lille (CCI Grand Lille, concession VNF, 12 plateformes) : avantage structurel plausible, pas une preuve ; (5) le 26-72571 (22/07/2026) montre la CCIR passant elle-même un accord-cadre de desserte ferroviaire pour son terminal (rôle d'exploitant confirmé).
- **Hypothèse Phase 8** : H2 « monopole consulaire de fait » à conserver comme EXPLICATIVE (pourquoi 1 seule offre), pas accusatoire.
- **Artefacts** : `data/source_cci_business_ribecourt.html` + `data/source_cci_ports_lille.html` + `sources_ccir.sha256` (2b6c0bc0…, 20aa5a59…).

## PHASE 8 OUVERTE (2026-08-10 14:58 CEST) - matrice d'hypothèses H0-H6

- **Demande utilisateur** : bilan croisé des vérifications de l'après-midi (SMDA, Ribécourt) et mise à jour H0-H6. Artefact : `data/hypotheses_sesn.md` (matrice SANS score, H0-H6 canonique corruption_brainstorm §2).
- **CORRECTION DE PRÉMISSE** : la demande posait « seul A3 reste un signal de dispense potentiellement illégale » : INEXACT selon les faits (14:43) : la dispense A3 est FONDÉE (marchés subséquents d'accord-cadre mono-attributaire 18TRI001BCD, R.2162-13). Les 3 anomalies sont requalifiées (A1 conforme, A2 concurrence faible légale, A3 dispense fondée) ; seul point de vigilance résiduel = durée 12 ans de l'accord-cadre TOARC (R.2162-5, DCE à vérifier, DELIVERABLE_PENDING).
- **Bilan** : aucune anomalie procédurale avérée dans le pilote à ce stade ; concentration et concurrence faible comme observables (H2 explicatif), pas comme preuves. Prochaines vérifications priorisées dans la matrice (durée TOARC, CA SMDA, proportionnalité critère Ribécourt, retours sourcing 2022-2023).

## VÉRIFICATION 3 PROPORTIONNALITÉ RIBÉCOURT (2026-08-10 15:19 CEST) - critère CA ≥ 9,8 M€ (H4 de A2)

- **Demande utilisateur** : comparer la proportionnalité du critère CA ≥ 9,8 M€ de Ribécourt avec d'autres marchés d'exploitation de plateformes multimodales pour tester si le critère a dissuadé (H4 de A2).
- **VERDICT** : le critère 9,8 M€ = **2× montant = plafond légal exact de l'art. R.2142-7 CCP** (vigueur 2019, LEGIARTI000037730675) : proportionné au sens du droit ; le décret 2025-1383 (01/01/2026) a abaissé le plafond à 1,5×, postérieur à la consultation. Le critère vraiment discriminant est la QUALIFICATION (gestion de plateforme multimodale avec ITE, manœuvres ferroviaires, locotracteurs), pas le CA (détail REGISTRE 15:19).
- **Comparables (sources primaires BOAMP, donnees lues intégralement)** : Dourges DELTA 3 (DSP affermage, 57 M€/90 mois, PSE manœuvres ferroviaires, CAP_ECO exigée, Syndicat Mixte PFM Dourges, 23-43560) ; Dourges 2021 (48 M€, 21-7402) ; CCI Var Bregaillon (MAPA exploitation ferroviaire port, 24-88976) ; concession port fluvial L'Isle-Adam (26-66891, DSP).
- **Nouvelle question Phase 8** : pourquoi la SCSNE a-t-elle choisi un marché public de services (4,9 M€/48 mois) plutôt qu'une DSP pour exploiter sa plateforme trimodale NEUVE, alors que Dourges (objet similaire, 11× plus gros) passe par une DSP ? Choix de montage à interroger.
- **Artefacts** : `source_boamp_ods_d_23-43560.json` + `source_boamp_ods_d_21-7402.json` + `source_boamp_ods_d_24-88976.json` + `source_boamp_ods_d_23-22143.json` + `verif3_ribecourt.sha256` (f86941c3…, 93de69c8…, 262fda63…, 301b1ba6…).

## VÉRIFICATION 2 CAPACITÉ SMDA (2026-08-10 15:13 CEST) - seuil 5 M€ cumulés (AAPC 25-17720)

- **Demande utilisateur** : croiser les bilans 2022-2024 de SMDA (INPI/pappers) avec le seuil de 5 M€ de CA cumulé exigé par l'AAPC 25-17720 pour conforter H0 de A1.
- **VERDICT** : H0 de A1 CONFIRMÉE au niveau faisceau ; vérification formelle impossible en sources ouvertes (détail REGISTRE 15:13). SMDA = SOINS MODERNES DES ARBRES, SIREN 378998363, Trappes, NAF 81.30Z, SIREN confirmé dans le XML d'attribution 26-37280. Président : CAP VERT (SIREN 904912466) depuis 14/01/2022 (CAP VERT DEVELOPPEMENT depuis 2015) ; groupe CAP VERT CA > 180 M€, > 1 200 salariés, actionnaire de référence Gimv (29/06/2026). Dernier CA public : 2018 = 13,8 M€ (2,8× le seuil cumulé de 5 M€), 2017 = 15,5 M€ ; effectif 200-249 (RNE 2023) vs 125 (2018) = trajectoire croissante.
- **Verrou documentaire** : bilans 2019-2024 NON PUBLICS (confidentialité L.232-25, data.inpi.fr bloqué Cloudflare, API RNE 404, societe.com/verif.com sans CA récent). La vérification formelle des 3 exercices 2022-2024 nécessite l'INPI greffe payant. L'acheteur SCSNE a instruit la candidature (DUME + pièces de capacité) avant notification 13/04/2026.
- **Fait connexe** : presse spécialisée (constructionbtp.com 16/12/2025) cite SMDA parmi les attributaires de marchés de compensation environnementale du canal (secteur 4) : titulaire récurrent, cohérent avec H2 de A1 (spécialisation génie écologique).
- **Artefacts** : `source_pappers_smda.txt` + `source_api_recherche-entreprises_smda.json` + `source_api_smda_detail.json` + `verif2_smda.sha256` (4db15fec…, 3c4b4515…, db244696…).

## VÉRIFICATION 1 DURÉE TOARC (2026-08-10 15:07 CEST) - légalité des 144 mois (R.2162-5 / art. 78 décret 2016-360)

- **Demande utilisateur** : obtenir la justification écrite de la durée de 12 ans de l'accord-cadre TOARC (DCE PLACE 373666 ou CADA).
- **VERDICT** : justification formelle non publique (DCE inaccessible sans compte), MAIS faisceau de cohérence SOLIDE (détail REGISTRE 15:07) : (1) communiqué officiel SCSNE 03/12/2019 « ces marchés s'étaleront sur une durée de plus de 10 ans... 84 M€ HT » (justification par l'objet) ; (2) mise en service prévue **2032** (rapport CdC 10/04/2026, lignes 228-229/375-376/626) : validité 144 mois (2019-2031) calée sur le chantier ; (3) la CdC, qui a audité les marchés SCSNE (annexe 10 : 5 ensembles), N'A PAS relevé la durée comme irrégulière.
- **Légalité** : 144 mois > plafond 4 ans (art. 78 III décret 2016-360 en vigueur à la passation, repris R.2162-5 CCP) mais cas exceptionnel dûment justifié par l'objet (MOE couvrant études + suivi de travaux d'un ouvrage de 107 km) : doctrine MIQCP admet le calage sur la durée du chantier. **H4 conditionnelle de A3 (accord-cadre nul) résolue : SANS APPUI**.
- **NOUVEAU FAIT MAJEUR (rapport CdC p. 50-57, lu intégralement)** : 148 avenants pour 76 marchés à mars 2025 ; suppléments MOE 11 M€ accordés + **83 M€ en cours d'instruction** ; 9 protocoles + 4 avenants transactionnels ; demandes MOE unique **92-97 M€** (R.214-120 code env., note 73) ; recommandation n° 2 (consolider services marchés publics). Recoupe la thématique avenants/gonflement du pilote : nouvel axe Phase 8.
- **Artefacts** : `data/rapport_CdC_canal-seine-nord_2026-04-10.pdf` (2,77 Mo) + `data/source_scsne_marches-publics.html` + `verif1_cdc.sha256` (33b5d05e…, acf8a06f…). Résidu DELIVERABLE_PENDING : justification formelle du RCC (voie CADA SCSNE si besoin).

## Artefacts Phase 1

- `data/decp_sesn_raw.csv` + `data/decp_sesn_raw.sha256`
- `data/recensement_univers.csv` (tous marchés toutes sources : numéro marché SESN, idweb BOAMP/TED, montant initial, support(s), version schéma)
- `data/marches_sans_montant.csv`
- `data/registre_pistes.csv` (pistes non officielles, ouvert dès cette phase)
- `scripts/01_extract_decp.py` (ou shell, déterministe, auto-documenté)
- HASH_CAPABILITY : si sha256 indisponible, noter DEGRADED_FLAG (pas d'invention).

## Conventions

- Tout fichier : format AGENTS.md, horodatage réel CEST.
- Toute affirmation décisionnelle : SRC-ID + locator (page/ligne/cellule).
- Sources : URLs de pages spécifiques cliquables, jamais « CDC, rapport annuel ».
- Mémoire d'abord : recherche Mnemolite à l'ouverture (faite), write-back à la clôture (tags : project:truth-engine, kernel, sesn, avenants, corruption).
