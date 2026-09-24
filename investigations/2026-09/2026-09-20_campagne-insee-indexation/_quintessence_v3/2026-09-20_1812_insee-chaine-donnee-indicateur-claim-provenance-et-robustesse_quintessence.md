# QUINTESSENCE : insee-chaine-donnee-indicateur-claim-provenance-et-robustesse
Source : investigations/2026-09/2026-09-20_campagne-insee-indexation/2026-09-20_insee-chaine-donnee-indicateur-claim-provenance-et-robustesse/2026-09-20_18-12_insee-chaine-donnee-indicateur-claim-provenance-et-robustesse_INVESTIGATION.md (RUN_ID 20260920-1812, ENGINE 2.10.6, COMPLEXITY 18 APEX, G0-G10 PASS, certification DELIVERY PASS par UPDATE 20260921-1030)

## 1. Métadonnées & trace source
Investigation TOPIC APEX sur la chaîne réalité → données → collecte → sélection → modèle → statistique → narration → décision, pour 6 indicateurs (chômage BIT, recensement, IPC, PIB, ERFS/pauvreté, BDF). 9 faits, 38 requêtes, 7 checkpoints. Verdict : le chiffre officiel reflète une réalité définie pour être mesurée ; aucune manipulation documentée ; multi-présentabilité massive ; le premier chiffre domine le récit.

## 2. Faits atomiques préservés
- F-01 ✧ Taux de chômage BIT (2,7 M / 8,3 % T2 2026) publié avec incertitude ±0,3 pt (niveau et évolution) ; enquête Emploi rénovée 2021 impose le recalcul des séries ; l'Insee qualifie elle-même le recul 2020 de « en trompe-l'œil ». EPI:FACT mem:46193d3f-f889-4f44-991f-6b001f4397bb [L367] (mesuré)
- F-02 ✧ Divergence structurelle BIT vs catégorie A (2010-2022 : BIT -2 pts vs catégorie A +5 %, Pays de la Loire) attribuée aux réformes (retraite/dispense seniors, RSA 2009, durcissement 2021, radiations) intervenant « indépendamment de la situation réelle » du marché du travail. EPI:FACT mem:25a43ded-fb6a-4ac0-8ccc-6f765d3bc068 [L368] (mesuré)
- F-03 ✦ Population légale/référence = estimation par sondage (rotation 1/5 des communes <10k, 8 % des adresses pour ≥10k) officialisée par décret annuel depuis 2008, référencée par ~350 articles législatifs (DGF, conseillers, seuils) ; écart >15 % documenté entre estimation Insee (678) et dénombrement municipal (791) à Metzing (2024) ; correction CNERP engagée (délai 3→2 ans). EPI:FACT mem:dad9d305-19ff-4191-95a9-00a2ff13994c [L369] (mesuré)
- F-04 ✧ Trois définitions du chômage coexistent : BIT (3 critères), catégorie A (administratif), chômeur au sens du recensement (auto-déclaration, plus élevé). EPI:FACT mem:dab61379-34b1-4808-adde-ad00c8688212 [L370] (mesuré)
- F-05 ✧ Recensement : EAR 2021 reportée (Covid), méthodes adaptées 2022-2027 ; millésime 2023 comparable uniquement à des millésimes distants d'au moins 6 ans ; Mayotte : dérogation puis cyclone Chido. EPI:FACT mem:5bae61ea-ac18-48f4-bacd-3ea296e4e077 [L371] (mesuré)
- F-06 ✧ Comptes nationaux sur sources administratives (ESANE/DGFiP, douanes, ENL 2019 pour loyers réels et imputés, redressements fiscaux pour activité dissimulée) ; révision ordinaire 3 ans ; rebasing base 2020 révisant 1949-2023. EPI:FACT mem:7718bab2-4b99-4292-a7ce-c7552191e438 [L372] (mesuré)
- F-07 ✦ Biais moyen haussier des révisions de croissance +0,34 pt (2005-2024, Rexecode) ; 2023 : 0,9 % → 1,9 % corrigé des jours ouvrés / 1,6 % non corrigé, plus forte révision depuis 2003 ; erratum Insee Première 2105 publié le jour même (29 mai 2026). EPI:FACT mem:0e7b6e8b-6941-4b24-9e67-ad37fbd256f7 [L373] (mesuré)
- F-08 ✦ Pauvreté facteur 5 selon le seuil : 2 843 000 (40 %) / 5 599 000 (50 %) / 9 817 000 (60 %) / 14 576 000 (70 %) en 2024 ; l'Observatoire des inégalités privilégie le seuil 50 %. EPI:FACT mem:a22a2146-1f94-4fa9-8978-9c1a97f0ef4e [L374] (mesuré)
- F-09 ✧ ERFS : imputations structurelles de revenus absents des sources fiscales (Patrimoine 2011/2015, PPAP 2019, aides 2020 « fragilités » reconnues) ; refonte 2021 rehausse niveaux de vie, abaisse pauvreté et inégalités (-0,3 pt documenté en aval). EPI:FACT mem:5fffa41a-57cb-497e-ac22-318b511182bd [L375] (mesuré)Traces registre : premier fait à la ligne 367, dernier à la ligne 375 de la source [L367-L375] (mesuré).
Inventaire source : FCT-001→F-01 … FCT-009→F-09, ordre conservé (mesuré).

## 3. Acteurs nominaux
Insee ; DGFiP ; Cnaf ; Cnav ; CCMSA ; maires (collecte) ; Eurostat ; ASP ; CNIS ; CNERP ; CNIL ; Rexecode ; Observatoire des inégalités ; inegalites.fr ; BFM ; sénateurs Mizzon et Pluchet.

## 4. Sources externes citées
Loi du 7 juin 1951 (amende 38 €) ; décret 2003-485 ; règlement CE 223/2009 ; normes BIT ; SEC/comptes européens ; questions sénatoriales 2024 ; réponse ministérielle Metzing ; CNERP 2025.

## 5. Chronologie datée
1946 création ; 1951 loi ; 1970-2002 enquête Emploi annuelle ; 1996 appariement EEC-fiscal (naissance ERF) ; 2002 publication annuelle des populations ; 2003 décret 2003-485 ; 2004 recensement rénové (rotation 1/5) ; 2005 ERFS ; 2008 premier décret d'authentification ; ruptures ERFS 2010/2012 ; 2020 « fragilités » reconnues ; 2021 refonte EEC/ERFS + report EAR ; 2024 base 2020 + questions sénatoriales ; 2025 réponse Metzing + CNERP (3→2 ans) + décret populations 2023 ; 2026 compte définitif 2023, erratum, séries pauvreté 2024, lancement EBF 2026.

## 6. Mécanismes / chaînes causales
- M1 (L2) : Estimation par sondage → authentification par décret → référence de ~350 articles de loi (DGF, seuils) → l'erreur d'estimation devient un enjeu juridique et budgétaire. Preuves : F-03. Verrou : légal. [L369] (mesuré)
- M2 (L2) : Conventions de seuil et de définition (pauvreté 40/50/60/70 % ; trois chômages) → facteur 5 et divergences structurelles entre indicateurs d'un même phénomène. Preuves : F-08, F-04, F-02. Verrou : méthodologique. [L374, L370, L368] (mesuré)
- M3 (L2) : Imputations et refontes (ERFS, EEC) → ruptures de série chiffrées, re-calages des niveaux publiés. Preuves : F-09, F-01, F-05. Verrou : méthodologique. [L375, L367, L371] (mesuré)
- M4 (L3) : Biais haussier des révisions + primauté du premier chiffre → le récit économique public se forme sur des estimations systématiquement basses, la correction arrive après (F-07). Verrou : calendaire/organisationnel. [L373] (mesuré)

## 7. Verbatim et citations
- « en trompe-l'œil » (Insee, recul du chômage 2020) (estimé).
- « fragilités » reconnues (Insee, imputations ERFS 2020) (estimé).
- « indépendamment de la situation réelle » (document DARES/Insee sur la divergence BIT/catégorie A) (estimé).

## 8. Notes méthodologiques source
Certification : APEX, EDI 0,42 vs cible 0,80 (concentration famille A structurelle), GAP_SEVERITY ≈ 0,114 < 0,20 : poursuite avec divulgation. Réfutations ❧ : « le chiffre officiel = fait primaire » (CLM-001/003), « la révision 2023 est sans biais de direction » (CLM-006), « les imputations sont sans effet documenté » (CLM-007), « conventions = manipulation » (CLM-008). Un seul cas local vérifié (Metzing) : illustration, pas prévalence. Classements ROBUSTE/SENSIBLE/FRAGILE : reconstructions argumentées, non méta-analyses.

## 9. Limites connues de cette extraction (case-limites)
PDF méthodologiques non extractibles au run parent (clos par pdf-méthodo) ; taux de réponse détaillés non centralisés (clos par taux-de-réponse) ; chiffrage DGF non produit (clos par metzing/dgcl) ; microdonnées inaccessibles ; traces [Lxx] estimées.
