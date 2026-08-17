# Quintessence : P9, spéculation foncière et PLU (ouverture de piste, v1)

Source : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-11_corpus-anticorruption/2026-08-11_23-58_p9-speculation-fonciere-plu_INVESTIGATION.md` (139 lignes, 25 FCT-p9)
Date extraction : 2026-08-13 04:00 CEST
Pilote : Buffy (FreeBuff) : Sublimator v36 Phase 1 (corpus complet, lot corpus-anticorruption)

---

## 1. Métadonnées & trace source

- **Autorité** : KERNEL v2.8 allégé, ouverture de piste, PARENT : REGISTRE ICEBERG MAX (2026-08-11_23-14)
- **Date source** : 2026-08-11 23:58 CEST, STATE FINAL
- **Identifiants source** : 25 FCT-p9-001 à 025
- **Object** : documenter le pattern « élu propriétaire foncier votant des PLU/modifications de zonage », méthodologie de détection, cas documentés
- **Verdict source** : pattern TRÈS ÉLEVÉ en impact mais faisabilité OSINT MOYENNE ; verdict « ne pas investiguer maintenant » (infrastructure technique manquante), à programmer pour un run dédié (run3-spéculation-foncière)

## 2. Faits atomiques préservés

### Cadre légal

- FCT-p9-001 : article 432-12 du Code pénal : prise illégale d'intérêts punie de cinq ans d'emprisonnement et de 500 000 € d'amende [L28 (mesuré)]
- FCT-p9-002 : le délit couvre le vote d'un PLU si l'élu est propriétaire d'une parcelle concernée par le changement de zonage (jurisprudence constante Cour de cassation) [L29 (mesuré)]
- FCT-p9-003 : l'élu doit se déporter du vote si le PLU concerne directement sa propriété (art. L. 2131-11 CGCT) [L30 (mesuré)]
- FCT-p9-004 : sanction complémentaire : déchéance des droits civiques, inéligibilité (art. 432-17 CP) [L31 (mesuré)]
- FCT-p9-005 : le délit est constitué même sans enrichissement personnel effectif : la simple participation au vote suffit [L32 (mesuré)]

### Données DVF

- FCT-p9-006 : dataset DVF publié par la DGFiP sur data.gouv.fr : toutes les transactions immobilières depuis 5 ans (2021-2025) [L42 (mesuré)]
- FCT-p9-007 : format : TXT pipe-separated, mise à jour semestrielle (avril et octobre) [L43 (mesuré)]
- FCT-p9-008 : champs principaux : date mutation, prix, adresse, code postal, commune, section cadastrale, numéro de parcelle, surface, type de bien, nature de culture [L44 (mesuré)]
- FCT-p9-009 : dernière mise à jour : 7 avril 2026 [L45 (mesuré)]
- FCT-p9-010 : fichiers volumineux (plusieurs Go par millésime), nécessitent infrastructure de traitement (Python pandas, PostgreSQL) [L46 (mesuré)]

### PLU et documents d'urbanisme

- FCT-p9-011 : les PLU sont disponibles sur le site de chaque commune ou intercommunalité, pas centralisés en opendata national [L52 (mesuré)]
- FCT-p9-012 : le Géoportail de l'Urbanisme centralise certains documents d'urbanisme numérisés (PLU, PLUi, cartes communales) [L53 (mesuré)]
- FCT-p9-013 : les délibérations des conseils municipaux sont publiées au registre des délibérations, pas de base nationale unifiée [L54 (mesuré)]

### Cadastre

- FCT-p9-014 : cadastre.gouv.fr : consultation gratuite des parcelles par commune/section/numéro, pas d'API publique [L60 (mesuré)]
- FCT-p9-015 : API Carto (api.gouv.fr) : couche cadastrale disponible pour les applications autorisées, pas d'accès grand public sans habilitation [L61 (mesuré)]

### Cas documentés

- FCT-p9-016 : affaire Levallois-Perret (Balkany) : condamnation pour prise illégale d'intérêts liée à des opérations immobilières, 4 ans prison ferme + inéligibilité (2019-2020) [L95 (mesuré)]
- FCT-p9-017 : affaire du Plateau de Saclay : enquête sur des modifications de PLU ayant bénéficié à des élus propriétaires fonciers, classée sans suite partiellement (2010-2015) [L96 (mesuré)]
- FCT-p9-018 : rapport Cour des comptes 2023 sur « L'artificialisation des sols » : la CdC pointe le rôle des PLU dans la spéculation foncière [L97 (mesuré)]
- FCT-p9-019 : Anticor a déposé plusieurs plaintes pour prise illégale d'intérêts liée à des PLU, notamment dans le Var et les Alpes-Maritimes (2018-2023) [L98 (mesuré)]
- FCT-p9-020 : une enquête du Monde (2023) a utilisé les données DVF pour cartographier les conflits d'intérêts potentiels des élus locaux [L99 (mesuré)]

### Obstacles OSINT

- FCT-p9-021 : le croisement DVF × cadastre × délibérations nécessite un traitement automatisé, le volume DVF est de plusieurs Go/an [L107 (mesuré)]
- FCT-p9-022 : le cadastre ne permet pas d'extraire le propriétaire en masse (limitation technique et légale : pas de réidentification selon art. R112 A-3 LPF) [L108 (mesuré)]
- FCT-p9-023 : les délibérations municipales ne sont pas centralisées en opendata, consultation commune par commune [L109 (mesuré)]
- FCT-p9-024 : les SCI masquent le bénéficiaire effectif, le RBE étant restreint depuis juillet 2024 (CJUE) [L110 (mesuré)]
- FCT-p9-025 : la détection automatisée est techniquement faisable mais nécessite un investissement technique lourd (scripts, base de données, web scraping) [L111 (mesuré)]

## 3. Acteurs nominaux

**Personnes** : Patrick Balkany (Levallois, condamné 4 ans ferme), élus propriétaires fonciers (pattern), élus du Var et Alpes-Maritimes (plaintes Anticor).
**Institutions** : Cour de cassation (jurisprudence 432-12), Cour des comptes (rapport 2023 artificialisation), Anticor, DGFiP (DVF), Le Monde/Les Décodeurs, SCPC (contexte), CJUE.

## 4. Sources externes citées

data.gouv.fr (DVF, API dataset 5c4ae55a), cadastre.gouv.fr, geoportail-urbanisme.gouv.fr, api.gouv.fr (API Carto), Code pénal art. 432-12, CGCT art. L. 2131-11, presse investigation (Mediapart, Le Monde), CdC 2023.

## 5. Chronologie datée

2010-2015 : affaire Plateau de Saclay ; 2018-2023 : plaintes Anticor (Var, Alpes-Maritimes) ; 2019-2020 : condamnation Balkany ; 2021-2025 : millésimes DVF ; 2023 : rapport CdC artificialisation + enquête Le Monde DVF ; 07/2024 : RBE restreint (CJUE) ; 07/04/2026 : dernière MAJ DVF.

## 6. Mécanismes / chaînes causales

**M1 — Le pattern du reclassement gagnant** : un élu propriétaire d'un terrain en zone agricole/naturelle vote une modification du PLU qui le reclassera en constructible (valeur x10 à x100), puis revend avec plus-value massive ; le délit est constitué dès la participation au vote (même sans enrichissement). Niveau : L2. [L28-L32 (mesuré)]
**M2 — La triple couche de donnée existante mais non croisée** : DVF (prix, 30M transactions, MAJ 04/2026) + cadastre (parcelle, sans identité) + délibérations (non centralisées) : chaque couche est accessible, le maillon faible est l'identité du propriétaire. Niveau : L2. [L42-L46, L52-L54, L60-L61 (mesuré)]
**M3 — L'obstacle structurel de l'identité** : cadastre sans réidentification en masse (R112 A-3 LPF), RBE restreint depuis 07/2024 (CJUE), SCI comme écran : la couche « propriétaire » est l'angle mort. Niveau : L2. [L108, L110 (mesuré)]
**M4 — La faisabilité démontrée par la presse** : Le Monde (2023) a prouvé que le croisement DVF × conflits d'intérêts est faisable à grande échelle : preuve de concept OSINT pour un run dédié. Niveau : L2. [L99 (mesuré)]

## 7. Verbatim et citations

- Protocole 5 étapes : extraction DVF ciblée → croisement cadastre → croisement délibérations → croisement permis → signal d'alerte (drapeau rouge si élu propriétaire → vote PLU → revente dans les 24 mois → plus-value > 100 000 €) [L66-L86 (mesuré)]
- Verdict faisabilité : « MOYENNE — données DVF disponibles, mais le croisement PLU × cadastre × propriétaires est complexe » [L102 (mesuré)]

## 8. Notes méthodologiques source

- **Fiabilité** : cadre légal (Légifrance), données (data.gouv.fr), cas documentés (presse/CdC) ; verdict d'ouverture prudent.
- **F-##** : 25/25 identifiants FCT-p9-001 à 025 préservés verbatim.
- **Méthode** : pattern documenté (Anticor, Reporterre, CRC, CdC), protocole de détection en 5 étapes, obstacles OSINT inventoriés, verdict de faisabilité.

## 9. Limites connues (case-limites)

- GAP-p9-001 : télécharger et parser les 5 millésimes DVF (P1) ; GAP-p9-002 : script Python de croisement DVF × PLU × cadastre (P1) ; GAP-p9-003 : sélectionner 3 communes-test (Tarn, Var, Alpes-Maritimes, P2) ; GAP-p9-004 : registres de délibérations (P2) ; GAP-p9-005 : croiser avec les SCI via Pappers/INPI (P2).
- Verdict initial : « ne pas investiguer maintenant », à programmer pour le run3-spéculation-foncière ; la v2 (10-50) relèvera la priorité à P1 (loi 2025-1249 adoucissant le délit).
