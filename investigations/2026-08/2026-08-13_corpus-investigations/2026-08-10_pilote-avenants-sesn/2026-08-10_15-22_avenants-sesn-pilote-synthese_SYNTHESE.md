# SYNTHÈSE FINALE DU PILOTE AVENANTS SESN : BILAN DES VÉRIFICATIONS ET LEÇONS POUR LE PROTOCOLE ANTICORRUPTION

- Type : SYNTHESE (consolidation de la Phase 8)
- Date : 2026-08-10 15:22 CEST
- RUN : RUN-2026-08-10-01 (pilote avenants SESN)
- Dossier : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_pilote-avenants-sesn/`
- Protocole de référence : `2026-08-10_preparation-anticorruption/protocole/2026-08-10_07-10_pilote-avenants-sesn_ARCHITECTURE.md` (v1.1)
- Documents sources : `RUN_MANIFEST.md`, `2026-08-10_09-30_avenants-sesn-pilote_REGISTRE.md` (702 lignes), `data/hypotheses_sesn.md`
- STATUT : synthèse de clôture de la Phase 8 ; le pilote reste STATUS:OPEN (Phase 5 CADA, 9 droit de réponse, 10 dossier final : DELIVERABLE_PENDING)

Ce document répond à la demande : consolider la Phase 8, établir le bilan des 6 vérifications (SMDA, Ribécourt, TOARC, CCIR, recensement 57 numéros, TED) et tirer les leçons méthodologiques pour le protocole anticorruption du projet.

---

## 1. RÉSUMÉ EXÉCUTIF

Le pilote avenants SESN a testé la méthode complète du protocole anticorruption (recensement d'un univers complet, normalisation déterministe, mesures quantitatives, sélection de cas par règles gelées, vérification de chaque signal à la source primaire, matrice d'hypothèses H0-H6 sans score) sur le Canal Seine-Nord Europe.

**Verdict d'ensemble : aucune anomalie procédurale avérée sur les 3 cas sélectionnés (A1, A2, A3).** Les 3 anomalies de la Phase 4 ont été requalifiées à la source primaire : A1 CONFORME (allotissement annoncé dès l'origine), A2 fondement RÉGULIER avec concurrence faible avérée (1 offre, légal), A3 dispense FONDÉE (marchés subséquents d'accords-cadres mono-attributaires). Ce résultat négatif est lui-même un résultat : il démontre la discipline de la méthode (les signaux quantitatifs ne sont pas des preuves) et il déplace l'attention vers le véritable signal documentaire du corpus.

**Le signal majeur n'est pas dans les 3 anomalies mais dans la lacune de publication et dans le rapport CdC du 10/04/2026** : 148 avenants pour 76 marchés à mars 2025, 11 M€ de suppléments MOE déjà accordés, plus de 83 M€ en cours d'instruction et 92 à 97 M€ de demandes de rémunération MOE unique (art. R.214-120 code de l'environnement). Les DECP consolidées ne contiennent aucune modification SCSNE (0 sur 45 contrats), alors que le même fichier en contient 508 957 pour d'autres acheteurs : la donnée n'existe pas publiquement, mais les avenants existent (prouvé par la CdC).

---

## 2. LE PILOTE EN CHIFFRES (DONNÉES GELÉES ET VÉRIFIÉES)

| Indicateur | Valeur | Source |
|------------|--------|--------|
| Contrats (dédupliqués, fenêtre ≤ 30/06/2026) | 45 | `decp_sesn_dedup.csv` |
| Cumul de référence Phase 3 | 103 578 507,98 € HT | TRANCHÉ 12:47 |
| Cumul recensement univers (47 lignes à montant) | 107 076 560,54 € HT | `recensement_univers_v3.csv` |
| SIREN titulaires distincts | 26 (tous RNE actifs) | Phase 2 |
| CR5 (5 premiers) | 72,35 % | `indicateurs_sesn.csv` |
| CR10 | 86,38 % | idem |
| HHI | 1 419 points (modéré, descriptif) | idem |
| Modifications DECP déclarées | 0 (lacune GAP-001-P1, pas une absence réelle) | idem |
| Candidatures uniques (offres = 1) | 5 (6 117 854,25 €, 5,91 %) | idem |
| Procédures avec négociation | 22 (50 116 772,39 €, 48,4 %) | idem |
| TRAVAUX / SERVICES / FOURNITURES | 78,18 % / 21,73 % / 0,09 % | idem |
| 148 avenants pour 76 marchés (mars 2025) | rapport CdC 10/04/2026, p. 57 | Vérification 1 |
| Suppléments MOE accordés / en cours | 11 M€ / 83 M€ | idem |
| Demandes MOE unique (R.214-120) | 92 à 97 M€ | idem, note 73 |

Top 5 concentration (rangs `concentration_sesn.csv`) : INRAP 23,74 % (7 contrats), SMDA 20,06 % (2 contrats), EVEHA 18,55 % (7 contrats), CHARIER GC 5,27 %, CCIR HDF 4,73 %. INRAP + EVEHA = 42,3 % du montant (fouilles archéologiques préventives, effet de filière structuré).

---

## 3. BILAN DES 6 VÉRIFICATIONS (DÉTAIL SOURCÉ)

### V1. SMDA : conformité de l'allotissement (14:31) + capacité CA (15:13)

- **Demande** : vérifier les 2 marchés de génie écologique SMDA (12 134 059,78 € + 8 641 524,06 €, cas A1) contre l'AAPC et les règles d'allotissement.
- **Verdict : CONFORME.** Chaîne probatoire lue en XML intégralement : AAPC BOAMP 25-17720 (14/02/2025) annonce les 2 lots (2.1 Sud / 2.2 Nord) dans un SEUL avis, procédure ouverte, 2 lots max par soumissionnaire (présentation et attribution), seuils CA 3 M€ / 2 M€ / 5 M€ cumulés, fonds UE MIE ; rectificatif 25-38762 (06/04/2025, report au 14/05/2025) ; attribution 26-37280 (14/04/2026) : 5 offres par lot, SMDA attributaire des 2 lots (le maximum autorisé), qualité 40 / prix 60, CPV 45110000.
- **Capacité (Vérification 2, 15:13)** : SMDA = SOINS MODERNES DES ARBRES, SIREN 378998363, Trappes, NAF 81.30Z, identifié dans le XML d'attribution. Président : CAP VERT (SIREN 904912466) depuis le 14/01/2022 ; groupe CAP VERT CA > 180 M€, > 1 200 collaborateurs, actionnaire de référence Gimv (29/06/2026). Effectif RNE 200-249 salariés (2023). Dernier CA public : 2018 = 13,8 M€ (2,8× le seuil cumulé de 5 M€ à lui seul), 2017 = 15,5 M€.
- **H0 de A1 : CONFIRMÉE au niveau faisceau.** Résidu documentaire honnête : les bilans 2019-2024 sont CONFIDENTIELS (art. L.232-25, dépôts BODACC avec déclaration de confidentialité), data.inpi.fr bloqué par Cloudflare, API RNE en 404, societe.com/verif.com sans CA récent. La vérification formelle des 3 exercices exige l'INPI greffe payant : non actionnable en sources ouvertes.
- **Fait connexe** : SMDA est titulaire récurrent de la SCSNE (presse spécialisée constructionbtp.com 16/12/2025, compensation environnementale secteur 4), cohérent avec H2 (spécialisation génie écologique).
- **Artefacts** : `source_pappers_smda.txt`, `source_api_recherche-entreprises_smda.json`, `source_api_smda_detail.json`, `verif2_smda.sha256` (OK).

### V2. Ribécourt : fondement de la procédure (14:35) + proportionnalité du critère CA (15:19)

- **Demande** : vérifier le marché d'exploitation de la plateforme trimodale de Ribécourt (CCIR HDF, 4,9 M€, 1 offre, négociation, cas A2).
- **Verdict fondement : RÉGULIER.** XML DILA lus intégralement : AAPC BOAMP 25-21716 (25/02/2025) = procédure négociée AVEC publication préalable d'un AAPC (art. R.2124-3 CCP), deadline 28/03/2025, montant maximum sur 4 ans 4 900 000 € HT, 48 mois ; attribution 26-68097 (08/07/2026, conclu 12/06/2026) : valeur maximale 4 900 000 €, 1 seule offre reçue. L'hypothèse de contournement de publicité (Phase 4) est INVALIDÉE : la publicité a eu lieu, 1 seul opérateur a répondu.
- **Verdict montant : CONTRÔLÉ.** Triple concordance 4 900 000 € (AAPC = attribution = DECP) : aucun gonflement. Rythme : 4,9 M€ / 48 mois ≈ 102 083 €/mois.
- **Proportionnalité du critère (Vérification 3, 15:19)** : CA exigé ≥ 9,8 M€ = 2× le montant = **plafond légal exact de l'art. R.2142-7 CCP** (version 2019, LEGIARTI000037730675, en vigueur à la passation) : « n'excède pas le double du montant estimé ». Le décret 2025-1383 (01/01/2026) a abaissé le plafond à 1,5×, mais postérieurement à la consultation. Le critère de CA n'est PAS un excès : le vrai discriminant est la QUALIFICATION (gestion de plateforme multimodale avec ITE, manœuvres ferroviaires, locotracteurs).
- **Comparables (sources primaires BOAMP)** : Dourges DELTA 3 (Syndicat Mixte PFM, DSP affermage, 57 M€ / 90 mois, PSE manœuvres ferroviaires, CAP_ECO exigée, avis 23-43560) ; Dourges 2021 (48 M€, 21-7402) ; CCI Var Bregaillon (MAPA exploitation ferroviaire de port, 24-88976). Dourges (objet quasi identique, 11× plus gros) passe par une DSP : nouvelle question ouverte sur le choix de montage de la SCSNE (marché public de services vs DSP pour une plateforme neuve).
- **H4 de A2 : NON ÉCARTÉE (faible)** : avantage structurel documenté (opérateur consulaire établi), pas une preuve de favoritisme.
- **Artefacts** : `avis_boamp_25-21716_AAPC_ribecourt.xml`, `avis_boamp_26-68097_attribution_ribecourt.xml`, `avis_ribecourt.sha256` ; `source_boamp_ods_d_*.json` ×4, `verif3_ribecourt.sha256` (OK).

### V3. TOARC : fondement de la dispense des 3 MOE (14:43) + durée de 12 ans (15:07)

- **Demande** : vérifier le fondement de la procédure « sans publicité ni MEC » des 3 marchés de maîtrise d'oeuvre (Egis ×2, Arcadis, 517 854,25 €, cas A3) et la légalité de la durée de 12 ans de l'accord-cadre.
- **Verdict dispense : FONDÉE.** Les 3 marchés sont des MARCHÉS SUBSÉQUENTS d'accords-cadres MONO-ATTRIBUTAIRES : AAPC BOAMP 18-50453 (15/04/2018, JOUE 2018/S 075-167044) « Maîtrise d'oeuvre TOARC – Secteurs 2, 3 et 4 », REF_MARCHE 18TRI001BCD, 3 lots, durée 144 mois, accords-cadres mono-attributaires à bons de commande et marchés subséquents (décret 2016-360 art. 78-80, devenu R.2162-13 s. CCP) ; attribution 19-178514 (05/12/2019) : total 84 127 774 €, lot 2 Groupement ONE conduit par EGIS (35 627 119 €), lot 3 ARCADIS (22 562 587 €). La dispense de nouvelle publicité/MEC est légale pour un accord-cadre mono-attributaire ; **R.2122-8 (seuil 40 000 €) est inapplicable** (contrats non autonomes). La DECP 2707074 porte d'ailleurs la mention explicite « Marché subséquent n°12 ».
- **Verdict durée (Vérification 1, 15:07)** : 144 mois > plafond de 4 ans (art. 78 III décret 2016-360 / R.2162-5 CCP), MAIS faisceau de cohérence SOLIDE : (1) communiqué officiel SCSNE 03/12/2019 « ces marchés s'étaleront sur une durée de plus de 10 ans... 84 M€ HT » ; (2) mise en service prévue **2032** (rapport CdC 10/04/2026) : validité 2019-2031 calée sur le chantier (cas exceptionnel dûment justifié par l'objet, doctrine MIQCP) ; (3) la CdC, qui a audité en profondeur 5 ensembles de marchés SCSNE, N'A PAS relevé la durée comme irrégulière. **H4 conditionnelle de A3 (accord-cadre nul) résolue : SANS APPUI.** Résidu : justification formelle du RCC non publique (DCE PLACE refConsultation 373666 inaccessible sans compte), voie CADA possible.
- **Artefacts** : `toarc_18-50453_AAPC_donnees.json`, `toarc_19-178514_attribution_donnees.json`, `toarc_avis.sha256` ; `rapport_CdC_canal-seine-nord_2026-04-10.pdf` (2,77 Mo), `verif1_cdc.sha256` (OK).

### V4. CCIR : position de l'exploitant et monopole consulaire (14:51)

- **Demande** : documenter la position de la CCIR HDF sur la plateforme trimodale de Ribécourt : statut d'exploitation, historique, test de l'hypothèse du monopole consulaire de fait (question Phase 8 de A2).
- **Verdict : faisceau de monopole consulaire de fait PLAUSIBLE mais NON PROUVÉ.** Points établis (sources primaires lues) : (1) la plateforme est une infrastructure NEUVE (travaux SCSNE 26-6458, CPV 45213350, 2026), adossée aux quais du canal latéral à l'Oise (domaine public fluvial, CG3P L.2124-8) : aucun marché d'exploitation antérieur possible ; (2) l'exploitation est un marché public de services (accord-cadre 4,9 M€ / 48 mois), pas une délégation de service public ; (3) le sourcing 2022-2023 (avis 22-146482, 23-80795, art. R.2111-1) documente une préparation longue de la SCSNE ; (4) le critère de capacité (gestion de plateforme multimodale avec ITE, manœuvres ferroviaires, locotracteurs) est aligné sur le métier de la CCIR via Ports de Lille (CCI Grand Lille, concession VNF, 12 plateformes dont Lille-Délivrance, Santes, Wambrechies) ; (5) l'avis 26-72571 (22/07/2026) montre la CCIR passant elle-même un accord-cadre de desserte ferroviaire pour son terminal : rôle d'exploitant confirmé.
- **Lecture : H2 (contrainte réelle / avantage structurel) EXPLICATIVE du 1 offre, pas H4/H5 accusatoire.**
- **Artefacts** : `source_cci_business_ribecourt.html`, `source_cci_ports_lille.html`, `sources_ccir.sha256` (OK).

### V5. Recensement 57 numéros SESN : couverture complétée (13:08 v2 + 14:00 v3)

- **Demande** : fermer les gaps de couverture DECP du recensement des 57 numéros de marché de la page SCSNE.
- **Résultat** : `recensement_univers_v3.csv` (116 lignes, sha256 18361205...). Ajouts : lot Q1-M213 (SPIE Batignolles Nord, 2 999 530,10 €, conclu 20/11/2025, BOAMP 25-132968 / JOUE 806579-2025) : ferme le gap sur les quais ; 5 avis widget enrichis en source primaire (M404 réhab. quai d'Havrincourt, M405 déboisement secteur 4, M522 vérins écluses, M524 travaux 4 métiers CA 80 M€, MC04 attribution 498 522,46 € à Pinson Paysage avec 3 offres). Cumul dédupliqué : 107 076 560,54 € HT.
- **Découverte d'une erreur d'unité** : la ligne AWS id=000 (422 841 600 € « réhabilitation de 4 quais ») était un DOUBLON DÉFECTUEUX du contrat M214-Lot Q2 (4 228 416 €, Charier GC) : erreur ×100 (centimes/euros) dans la publication AWS, tranchée à 12:47 par confrontation BOAMP + TED + PLACE + DECP. Le cumul de référence Phase 3 est 103 578 507,98 € HT (dédupliqué), jamais le brut 526 M€.
- **Constat de couverture** : les idweb widget 26-55339 et 26-69739 n'existent pas dans le flux DILA 2026 (hypothèse : identifiants AWS, pas BOAMP) ; seule la notice TED les retrouve. Les 3 avis 2026 (08/06, 14/07, 21/07) sont postérieurs à la coupure 30/06/2026 : documentés, hors socle.
- **Artefacts** : `recensement_univers_v3.csv` + `.sha256`, `scripts/01d_completer_avis.py` (déterministe, 0 LLM).

### V6. TED : notice JOUE 806579-2025 lue à la source primaire (13:20)

- **Demande** : lever le marqueur ✧ sur le JOUE 806579-2025 par la route TED directe et vérifier les montants par lot.
- **Verdict : ✧ LEVÉ.** Notice téléchargée en XML eForms `ContractAwardNotice` (UBL, CustomizationID eforms-sdk-1.12) via la route UDL `https://ted.europa.eu/udl?uri=TED:NOTICE:806579-2025:XML:FR:HTML` (HTTP 200, 34 175 octets, sha256 3d064d1a...). Montants confirmés à la source primaire : TEN-0001 (Q1-M213) = 2 999 530,10 € → SPIE Batignolles Nord ; TEN-0002 (Q2-M214) = 4 228 416,00 € → SAS CHARIER Génie Civil ; total 7 227 946,10 € ; contrats conclus 2025-11-20 ; 3 offres Q1 / 4 offres Q2 ; acheteur SCSNE Compiègne ; eSender Avenue-Web Systèmes.
- **Cohérence à 100 % avec le BOAMP XML DILA** : le tranchement du doublon ×100 est définitif (aucun avis ne connaît de quais à 422 M€).
- **Route UDL documentée au playbook §3.14** ; échecs documentés avant d'y arriver : page détail JS (contenu vide), API v3 (401), /api/publication/download (404), SPARQL data.ted (0 binding / 405), Wayback (aucun snapshot).
- **Artefacts** : `notice_ted_806579-2025_ContractAwardNotice.xml` + `.sha256` (OK).

---

## 4. PHASE 8 : ÉTAT FINAL DES HYPOTHÈSES H0-H6 (matrice `data/hypotheses_sesn.md`)

| Cas | Verdict | Hypothèses dominantes | Éléments disculpants constatés |
|-----|---------|----------------------|--------------------------------|
| A1 SMDA 20,8 M€ | CONFORME | **H0 FAVORISÉE** (allotissement annoncé, 5 offres/lot, CA plausiblement satisfait) ; H2 PLAUSIBLE (spécialisation) ; H4/H5 SANS APPUI | AAPC 25-17720 annonce les 2 lots dès l'origine ; 2 lots = maximum autorisé ; 5 offres par lot ; dernier CA public 2018 = 13,8 M€ |
| A2 Ribécourt 4,9 M€ | FONDEMENT RÉGULIER, concurrence faible avérée | **H0 FAVORISÉE** (AAPC publié, montant triple-concordant) ; **H2 FAVORISÉE explicative** (monopole consulaire de fait) ; H4 NON ÉCARTÉE (faible) | Procédure négociée avec AAPC (R.2124-3) ; critère CA au plafond légal 2× (R.2142-7) ; sourcing 2022-2023 ; plateforme neuve |
| A3 MOE 517 854 € | DISPENSE FONDÉE | **H0 FAVORISÉE** (marchés subséquents d'accord-cadre mono-attributaire, R.2162-13) ; H4 conditionnelle RÉSOLUE (durée calée sur chantier) | Accord-cadre parent 18TRI001BCD retrouvé (84 127 774 €) ; mention « subséquent » explicite dans la DECP ; CdC sans critique de durée |

**Règle d'honnêteté respectée** : aucune hypothèse n'est « écartée » par absence de preuve, seulement par élément incompatible constaté ; la matrice reste SANS score (aucune quantification de vraisemblance). Après vérifications, **plus aucune candidature unique du corpus ne constitue un signal d'anomalie procédurale** : les 4 « sans publicité ni MEC » sont des marchés subséquents légitimes, la 1 négociation (Ribécourt) est publiée et légale.

**Signaux croisés restants (à porter en poursuite)** : INRAP + EVEHA = 42,3 % du montant (effet de filière archéologique, à tester contre les règles de répartition des opérateurs : H0/H2, pas H4/H5 sans fait) ; procédures avec négociation = 48,4 % (à croiser avec la typologie des prestations).

---

## 5. DÉCOUVERTES CONNEXES (rapport CdC 10/04/2026, lu intégralement)

La Vérification 1 (durée TOARC) a conduit à lire le rapport de la Cour des comptes du 10/04/2026 sur le Canal Seine-Nord Europe, qui recoupe directement la thématique avenants/gonflement du pilote :

1. **148 avenants pour 76 marchés** à mars 2025 (p. 57) : la SCSNE utilise les dérogations du code de la commande publique pour éviter les remises en concurrence.
2. **Suppléments MOE : 11 M€ déjà accordés + plus de 83 M€ en cours d'instruction** ; 9 protocoles + 4 avenants transactionnels conclus.
3. **Demandes de rémunération MOE unique (art. R.214-120 code de l'environnement) : 92 à 97 M€** via avenants (note 73, p. 50), pour la responsabilité d'organisme agréé coordonnateur.
4. **Recommandation n° 2** : consolider le dimensionnement et l'expertise des services marchés publics de la SCSNE.
5. **Mise en service prévue en 2032** (retard de près de 20 ans vs calendrier initial) : contexte de la dérive 2,2 à 2,8 Md€ hors frais financiers documentée par la CdC.

**Lecture** : le pilote n'a pas trouvé d'anomalie dans les 45 DECP, mais le rapport officiel chiffre la mécanique d'avenants que les données ouvertes ne montrent pas. Le montant des avenants MOE (11 M€ + 83 M€ en cours + 92-97 M€) est 5 à 10× supérieur au montant initial des 3 marchés subséquents A3 (517 854 €) : l'objet réel du signal n'est pas la dispense de publicité (légale) mais la dérive de rémunération des maîtres d'oeuvre.

---

## 6. LEÇONS MÉTHODOLOGIQUES POUR LE PROTOCOLE ANTICORRUPTION

Le pilote a validé et enrichi le protocole. Les 12 leçons suivantes sont transférables à toutes les investigations du corpus (commandes publiques, cessions, niches fiscales, mobilités public-privé) :

### 6.1 Sur la méthode d'investigation

1. **La non-publication n'est pas une preuve d'absence.** 0 modification DECP sur les 45 contrats SCSNE n'est pas un fait négatif : c'est une LACUNE (GAP-001-P1), prouvée comme telle par la structure du fichier (508 957 modifications chez d'autres acheteurs) et par le rapport CdC (148 avenants réels). Toute absence doit être qualifiée (lacune documentaire vs absence réelle) avant interprétation.
2. **Les signaux quantitatifs sont des points d'entrée, jamais des conclusions.** Concentration (CR5 72,35 %), candidature unique (5 cas), procédure sans publicité (5 cas) : chacun a été re-vérifié à la source primaire et chacun a été requalifié (2 conformes, 1 concurrence faible légale, dispense fondée). La discipline « signal → vérification XML → requalification ou confirmation » est le coeur du protocole.
3. **Les règles gelées avant calcul protègent contre le biais de sélection.** Les critères A1-A3 et les témoins T1/T2 ont été fixés par écrit avant l'exécution du script, avec témoins appariés (nature, période, maturité, type de prix, taille). Le contre-factuel (A1 à granularité division aurait sélectionné INRAP) a été consigné explicitement : la transparence du choix de granularité vaut plus que la prétendue neutralité d'un critère.
4. **Le dédoublonnage est une enquête en soi.** L'erreur ×100 de la ligne AWS (422,8 M€ vs 4,2 M€) n'a été détectée que par confrontation multi-sources (BOAMP + TED + PLACE + DECP). Règle : jamais de somme sur un cumul non dédupliqué ; clé de dédup (identifiant, acheteur, lot, version de schéma) documentée ; jamais (SIREN, objet, montant) qui fusionne des lots distincts.
5. **Le modèle événementiel est obligatoire pour les avenants.** Une DECP « montant modifié » est un NOUVEAU TOTAL, jamais un incrément : l'addition des montants modifiés double-compte. Cette règle du protocole a été implémentée en fail-fast dans `scripts/03_mesures.py` (assert not modifs) : un script qui croit compter des avenants doit échouer plutôt que produire un faux 0.

### 6.2 Sur l'analyse forensique

6. **La proportionnalité se juge au droit en vigueur à la passation, pas à celui du jour de l'analyse.** Le critère CA 2× de Ribécourt est au plafond légal de l'art. R.2142-7 (vigueur 2019) ; le plafond abaissé à 1,5× par le décret 2025-1383 est postérieur à la consultation. Un anachronisme juridique produirait un faux signal.
7. **L'avantage structurel (H2) précède l'avantage indu (H4).** Le monopole consulaire de fait de la CCIR (opérateur établi via Ports de Lille, critère aligné, plateforme neuve, sourcing documenté) explique l'offre unique sans accuser personne. H2 est FAVORISÉE comme explication ; H4 reste non écartée mais faible. Le faisceau explicatif doit être épuisé avant le faisceau accusatoire.
8. **L'identité précise des acteurs change la lecture.** Un « SME de 31 salariés » qui remporte 20,8 M€ aurait été un signal : l'identification SIREN a révélé une société du groupe CAP VERT (> 180 M€, 200-249 salariés, président CAP VERT depuis 01/2022). La capacité économique de groupe est un élément disculpant documenté, pas une suspicion. Corollaire : la fiabilité inégale des données ouvertes (API recherche-entreprises renvoyant une tranche obsolète de 31 salariés vs RNE 200-249) impose le recoupement d'au moins 2 sources.
9. **Les verrous documentaires se documentent, ils ne se contournent pas.** Bilans confidentiels (L.232-25), DCE non publics (compte PLACE requis), API instables (data.inpi.fr Cloudflare, API RNE 404), fichiers data.gouv FLOTTANTS non reproductibles (decp-2019.json, decp-2022.json réécrits entre deux téléchargements : exclus du socle de preuve). Chaque verrou est consigné avec la voie alternative restante (INPI greffe payant, CADA).

### 6.3 Sur l'infrastructure de données

10. **Les routes d'accès sont un actif à capitaliser.** Le pilote a validé et documenté au playbook : flux XML DILA BOAMP (y compris le nouveau schéma `/OPENDATA/BOAMP/2026/<mois>/<jour>/`), API OpenDataSoft BOAMP (recherche par texte objet, ~1,7 M d'avis), route TED UDL `:XML:FR:HTML` (eForms UBL), API recherche-entreprises. Les échecs (API TED v3 401, SPARQL data.ted 0 binding, Wayback vide) sont aussi documentés : ils évitent de les retenter.
11. **La mémoire est un index probatoire, pas une autorité.** Chaque vérification a fait l'objet d'un write-back Mnemolite (tags project:truth-engine, kernel, sesn, avenants, corruption) avec source + citation + date de validité. Le protocole mem-first est opérationnel : un fait CONFIRMÉ en mémoire avec pièce complète est répondable sans appel web.
12. **Le rapport officiel est la source de contrôle de la donnée ouverte.** La CdC (10/04/2026) fournit ce que les DECP ne montrent pas (148 avenants, 83 M€ en cours, 92-97 M€ MOE unique). Règle : pour tout grand projet, chercher le dernier rapport CdC AVANT de conclure sur les données ouvertes.

---

## 7. POINTS RESTANTS ET PROCHAINS AXES

**DELIVERABLE_PENDING (hérités du pilote) :**
- Phase 5 : 5 courriers CADA prêts à envoyer (dont demande du DCE TOARC refConsultation 373666 pour la justification formelle de la durée 144 mois).
- Phase 9 : questionnaires de droit de réponse.
- Phase 10 : dossier INVESTIGATION final format KERNEL + matrices juridiques par qualification.
- Justification écrite du RCC TOARC (voie CADA SCSNE) ; règlement de consultation Ribécourt (DCE 507911) ; montant du lot 4 (18TRI001D).

**Axes priorisés pour la suite :**
1. **Quantifier le gonflement MOE réel de la SCSNE** : 84 M€ initiaux (accord-cadre TOARC) → 11 M€ accordés + 83 M€ en cours + 92-97 M€ MOE unique (rapport CdC p. 50-57). C'est le vrai signal du pilote, chiffré par la CdC, à documenter avenant par avenant (via CADA si nécessaire).
2. **Question de montage : pourquoi un marché public de services (4,9 M€) plutôt qu'une DSP pour l'exploitation de la plateforme neuve de Ribécourt**, alors que Dourges (objet similaire, 57 M€) passe par une DSP ? Comparer les régimes (CG3P L.2124-8, domaine public fluvial).
3. **Retours du sourcing 2022-2023** (avis 22-146482, 23-80795) : combien d'opérateurs ont répondu au sourçage de l'ITE de Ribécourt ?
4. **Effet de filière archéologique** (INRAP + EVEHA = 42,3 %) : tester contre les règles de répartition des opérateurs d'archéologie préventive (H0/H2).

---

## 8. CONCLUSION GRADUÉE

Les données établissent : (1) un corpus de 45 contrats SESN 2024-2026 cumulant 103 578 507,98 € HT, avec une concentration élevée (CR5 72,35 %, INRAP + EVEHA 42,3 %, SMDA 20,06 %) et une concurrence faible ponctuelle (Ribécourt, 1 offre) ; (2) une lacune totale de publication des modifications DECP côté SCSNE, alors que le format le permet et que le rapport de la Cour des comptes (10/04/2026) documente 148 avenants et jusqu'à 83 M€ de suppléments MOE en cours d'instruction ; (3) trois cas sélectionnés dont aucun ne présente d'anomalie procédurale avérée après vérification à la source primaire (A1 conforme, A2 fondement régulier avec concurrence faible légale, A3 dispense fondée sur accord-cadre mono-attributaire).

Les données ne permettent pas, en l'état, de démontrer un avantage injustifié (432-14) ni un pacte corruptif (432-11) sur l'un des 45 contrats. Elles établissent en revanche un trou de transparence documentaire (absence de DECP de modification) et une mécanique d'avenants MOE officiellement chiffrée par la Cour des comptes, dont la quantification exhaustive reste à faire : c'est l'objet de l'axe 1.

**Le pilote atteint son objectif méthodologique** : il prouve qu'une investigation anticorruption peut produire, en sources ouvertes, un recensement complet, des mesures reproductibles, une sélection de cas par règles gelées et des requalifications honnêtes à la source primaire, sans aucune fabrication ni surinterprétation. Le résultat négatif sur les 3 anomalies est un livrable positif : il neutralise les faux positifs et concentre l'enquête sur les vrais signaux (lacune de publication + avenants MOE).

---

## ANNEXE : INDEX DES ARTEFACTS (tous hashés)

| Catégorie | Artefacts |
|-----------|-----------|
| Données | `decp_sesn_raw.csv`, `decp_sesn_dedup.csv` (45 l., 103 578 507,98 €), `decp_sesn_norm.csv`, `recensement_univers_v3.csv` (116 l.), `marches_sans_montant.csv`, `mesures_sesn.csv`, `concentration_sesn.csv`, `indicateurs_sesn.csv`, `cas_selection.csv`, `titulaires_rne.csv`, `siren_non_resolus.csv` (vide), `registre_pistes.csv` |
| Sources primaires archivées | `rapport_CdC_canal-seine-nord_2026-04-10.pdf`, `notice_ted_806579-2025_ContractAwardNotice.xml`, `avis_boamp_25-21716_AAPC_ribecourt.xml`, `avis_boamp_26-68097_attribution_ribecourt.xml`, `toarc_18-50453_AAPC_donnees.json`, `toarc_19-178514_attribution_donnees.json`, `source_pappers_smda.txt`, `source_api_*_smda*.json`, `source_cci_business_ribecourt.html`, `source_cci_ports_lille.html`, `source_boamp_ods_d_*.json` ×4, `source_scsne_marches-publics.html` |
| Scripts déterministes | `scripts/01_extract_decp.py`, `01b_recensement_univers.py`, `01c_completer_recensement.py`, `01d_completer_avis.py`, `02_corriger_doublon.py`, `02_normalize_siren.py`, `03_mesures.py`, `04_selection_cas.py` (+ explore_* : sondages, non repris en preuve) |
| Hashs | `artefacts_phase1.sha256`, `avis_ribecourt.sha256`, `toarc_avis.sha256`, `sources_ccir.sha256`, `verif1_cdc.sha256`, `verif2_smda.sha256`, `verif3_ribecourt.sha256`, `cas_selection.sha256`, `mesures_sesn.sha256`, tous vérifiés (OK) |
| Mémoire | write-back Mnemolite des 3 vérifications Phase 8 (ids 79d99b59, 069adc97, a4da82eb) + phases antérieures (529094b2 et autres) |

Fin de la synthèse. Contrôle final : ce document ne contient aucun tiret cadratin (U+2014).
