# Quintessence : Outputs IPP/CREST de la donnée DMTG : un seul usage documenté (AER 2023), le screening web avait affabulé des mentions

Source : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_outputs-ipp-dmtg-hors-fiche/2026-08-10_10-48_outputs-ipp-dmtg-hors-fiche_INVESTIGATION.md` (6 FCT-001..006)
Date extraction : 2026-08-13 05:30 CEST
Pilote : Buffy (FreeBuff) : Sublimator v36 Phase 1 (corpus complet, lot bloc DMTG/BNDP/CDC)

---

## 1. Métadonnées & trace source

- **Autorité** : KERNEL v2.8, format léger, axe anticorruption, bloc connaissance patrimoniale (DMTG)
- **Date source** : 2026-08-10 10:48 CEST, STATE FINAL
- **Identifiants source** : 6 FCT-001..006
- **Object** : identifier les publications IPP/CREST utilisant l'enquête DMTG hors de la fiche source CASD (GAP 1 du 10-31)
- **Verdict source** : constat d'absence : la seule publication IPP utilisant DMTG est le commentaire AER 2023 (déjà dans la fiche) ; la vérification primaire corrige un biais de screening web

## 2. Faits atomiques préservés

- FCT-001 : commentaire AER 2023 : auteurs = BACH L., BOZIO A., GUILLOUZOUIC-LE CORFF A., MALGOUYRES C. (4 auteurs : Arthur Guillouzouic-Le Corff, une seule personne, pas d'« Alice Le Corff » distincte) ; AER 113(7), 07/2023, pp. 2048-52, DOI 10.1257/aer.20221432 : la seule publication IPP documentée utilisant DMTG, déjà dans la fiche CASD (pub n° 5) [L32 (mesuré)]
- FCT-002 : note IPP n° 92 « Quels impôts les milliardaires paient-ils ? » (06/2023, PDF lu intégralement, 97 Ko texte) : la seule occurrence « DMTG » (l. 765) est HISTORIQUE (« Jusqu'au milieu des années 1980, les droits de mutation à titre gratuit (DMTG) étaient très élevés... », réf. Piketty 2001) : pas une utilisation de l'échantillon 2010 [L33 (mesuré)]
- FCT-003 : rapport IPP n° 36 « Évaluer les effets de l'impôt sur la fortune » (10/2021, PDF lu intégralement, 20 p., 459 Ko) : 0 occurrence DMTG/succession ; données = ISF-IFI + IR : l'affirmation du screening web (« DMTG mobilisée ») est réfutée [L34 (mesuré)]
- FCT-004 : CEPR DP20660 « Do Billionaires Pay Taxes? » (09/2025, même quatuor) : résumé officiel lu : aucune mention DMTG ; données = « French households' tax records linked to the corporations they control » (version anglaise actualisée de la note 92) [L35 (mesuré)]
- FCT-005 : rapport IPP n° 46 « Le plafonnement de l'impôt sur la fortune » (2023) : non vérifiable en session : HAL bloqué par Anubis, absent de la Wayback des uploads ipp.eu 2023 [L36 (mesuré)]
- FCT-006 : cartographie IPP/DMTG : un seul usage documenté (AER 2023, déjà dans la fiche CASD) ; aucune publication IPP DMTG hors fiche trouvée (borné : rapport 46 non vérifié) [L37 (mesuré)]

## 3. Acteurs nominaux

**Institutions** : IPP/CREST (quatuor Bach, Bozio, Guillouzouic-Le Corff, Malgouyres), CASD (fiche source + fiche de publication id=457), CEPR, HAL (bloqué), PSE/WID.world.

## 4. Sources externes citées

Fiche CASD id=457 + fiche de publication, note IPP n° 92 (PDF), rapport IPP n° 36 (PDF), cepr.org/publications/dp20660, API HAL (bloquée), CDX Wayback.

## 5. Chronologie datée

10/2021 : rapport IPP n° 36 ; 06/2023 : note IPP n° 92 ; 07/2023 : AER 113(7) ; 2023 : rapport IPP n° 46 (non vérifié) ; 09/2025 : CEPR DP20660 ; 10/08/2026 : vérification primaire (GAP 1 du 10-31 résolu).

## 6. Mécanismes / chaînes causales

**M1 — La vérification primaire contre le biais de screening** : un agent de recherche web avait attribué des mentions DMTG à des documents qui ne les contiennent pas (rapport 36) ou ne les contiennent qu'en contexte historique (note 92) : toute revendication d'usage doit être vérifiée dans le texte du document. Force : EXTRÊME. Niveau : L1. [L33-L34 (mesuré)]
**M2 — Le canal IPP singulier** : la donnée successorale DMTG est exploitée par les chercheurs via un seul canal IPP (EVREFIS/AER 2023) : le « canal standard » produit peu d'outputs documentés. Force : HAUTE. Niveau : L2. [L37 (mesuré)]
**M3 — La correction nominative** : Arthur Guillouzouic-Le Corff, une seule personne (pas « Guillouzouic + Alice Le Corff ») : la fiche CASD à 4 auteurs est exacte. Force : EXTRÊME. Niveau : L1. [L32 (mesuré)]

## 7. Verbatim et citations

- « Le screening web initial avait affabulé des mentions DMTG dans ces documents : vérification primaire faite, elles n'existent pas » [L41 (mesuré)]
- « L'absence d'outputs IPP DMTG hors fiche est un constat descriptif, pas un signe de dissimulation (l'équipe IPP publicit massivement ses méthodes et données) » [L42 (mesuré)]

## 8. Notes méthodologiques source

- **Fiabilité** : 2 PDF lus intégralement (note 92, rapport 36) + fiche CASD AER + résumé CEPR ; G1-G5 passés ; FCT-005 « non vérifié » ; FCT-006 « borné ».
- **F-##** : 6/6 identifiants FCT-001..006 préservés.
- **Méthode** : screening web puis vérification primaire de chaque document (téléchargement + grep), réfutation explicite des affirmations du screening, anti-sycophancie.

## 9. Limites connues (case-limites)

- Le rapport IPP n° 46 (plafonnement) n'a pas pu être lu (HAL derrière Anubis, aucun miroir) : s'il utilisait DMTG, la carte FCT-006 devrait être révisée : limite principale.
- Artefact d'extraction possible sur le rapport 36 (459 Ko pour 20 pages ≈ 23 Ko/page) : le constat d'absence repose néanmoins sur l'intégralité du texte extrait.
- Le CEPR DP20660 vérifié sur le résumé seul (PDF derrière inscription) : mention dans le texte complet non exclue à 100 %.
- GAPs : rapport 46 (retenter), texte complet CEPR, co-auteurs ponctuels.
