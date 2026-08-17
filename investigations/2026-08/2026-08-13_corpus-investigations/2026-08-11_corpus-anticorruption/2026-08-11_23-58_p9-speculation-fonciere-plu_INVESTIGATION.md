# INVESTIGATION : P9 - Spéculation foncière et PLU — croisement DVF × délibérations × permis

- STATE          : FINAL
- DATE           : 2026-08-11 23:58 CEST
- TYPE           : INVESTIGATION (KERNEL v2.8 allégé — ouverture de piste)
- PARENT         : ICEBERG MAX REGISTRE `2026-08-11_23-14_iceberg-max_REGISTRE.md`
- OBJECT         : documenter le pattern « élu propriétaire foncier votant des PLU/modifications de zonage », méthodologie de détection, cas documentés
- SOURCES        : data.gouv.fr (DVF), cadastre.gouv.fr, Code pénal art. 432-12, presse investigation

---

## 1. LE PATTERN

Un élu municipal (maire, adjoint à l'urbanisme, conseiller) est propriétaire d'un terrain classé en zone agricole ou naturelle. Le conseil municipal vote une modification du PLU (Plan Local d'Urbanisme) qui reclasse ce terrain en zone constructible. La valeur du terrain est multipliée par 10 à 100. L'élu revend ensuite avec une plus-value massive.

Ce pattern est documenté par :
- L'association Anticor (dossiers thématiques)
- Reporterre (enquêtes ponctuelles)
- Les Chambres régionales des comptes (CRC)
- La Cour des comptes (rapport 2023 sur l'artificialisation des sols)

---

## 2. CADRE LÉGAL

| Fait | Détail | Source |
|---|---|---|
| FCT-p9-001 | Article 432-12 du Code pénal : « Le fait, par une personne dépositaire de l'autorité publique [...] de prendre, recevoir ou conserver, directement ou indirectement, un intérêt quelconque dans une entreprise ou une opération dont elle a, au moment de l'acte, en tout ou partie, la charge d'assurer la surveillance, l'administration, la liquidation ou le paiement, est puni de cinq ans d'emprisonnement et de 500 000 € d'amende » | Code pénal, Légifrance |
| FCT-p9-002 | Le délit de prise illégale d'intérêts couvre le vote d'un PLU si l'élu est propriétaire d'une parcelle concernée par le changement de zonage (jurisprudence constante Cour de cassation) | Cour de cassation |
| FCT-p9-003 | L'élu doit se déporter du vote si le PLU concerne directement sa propriété (art. L. 2131-11 CGCT) | Code général des collectivités territoriales |
| FCT-p9-004 | Sanction complémentaire : déchéance des droits civiques, inéligibilité (art. 432-17 CP) | Code pénal |
| FCT-p9-005 | Le délit est constitué même sans enrichissement personnel effectif : la simple participation au vote suffit | Jurisprudence Cour de cassation |

---

## 3. DONNÉES DISPONIBLES EN OPENDATA

### 3.1. DVF (Demandes de Valeurs Foncières)

| Fait | Détail | Source |
|---|---|---|
| FCT-p9-006 | Dataset DVF publié par la DGFiP sur data.gouv.fr : toutes les transactions immobilières depuis 5 ans (2021-2025) | data.gouv.fr, API dataset 5c4ae55a |
| FCT-p9-007 | Format : TXT pipe-separated (|), mise à jour semestrielle (avril et octobre) | DGFiP |
| FCT-p9-008 | Champs principaux : date mutation, prix, adresse, code postal, commune, section cadastrale, numéro de parcelle, surface, type de bien (maison/appartement/terrain), nature de culture pour les terrains | Notice DVF |
| FCT-p9-009 | Dernière mise à jour : 7 avril 2026 | data.gouv.fr |
| FCT-p9-010 | Les fichiers sont volumineux (plusieurs Go par millésime) — nécessitent infrastructure de traitement (Python pandas, PostgreSQL) | Contrainte technique |

### 3.2. PLU et documents d'urbanisme

| Fait | Détail | Source |
|---|---|---|
| FCT-p9-011 | Les PLU sont disponibles sur le site de chaque commune ou intercommunalité, mais pas centralisés en opendata national | Constat terrain |
| FCT-p9-012 | Le Géoportail de l'Urbanisme (geoportail-urbanisme.gouv.fr) centralise certains documents d'urbanisme numérisés (PLU, PLUi, cartes communales) | geoportail-urbanisme.gouv.fr |
| FCT-p9-013 | Les délibérations des conseils municipaux sont publiées au registre des délibérations (consultable en mairie) et parfois en ligne — pas de base nationale unifiée | CGCT |

### 3.3. Cadastre

| Fait | Détail | Source |
|---|---|---|
| FCT-p9-014 | cadastre.gouv.fr : consultation gratuite des parcelles par commune/section/numéro — pas d'API publique | cadastre.gouv.fr |
| FCT-p9-015 | API Carto (api.gouv.fr) : couche cadastrale disponible pour les applications autorisées — pas d'accès grand public sans habilitation | api.gouv.fr |

---

## 4. MÉTHODOLOGIE DE DÉTECTION (protocole 5 étapes)

### Étape 1 : Extraction DVF ciblée
- Télécharger les millésimes DVF 2021-2025
- Filtrer sur le type de bien « terrain » (nature de culture indiquée)
- Identifier les communes avec un nombre anormal de transactions de terrains passant d'agricole à constructible

### Étape 2 : Croisement cadastre
- Pour chaque transaction suspecte, extraire la section et le numéro de parcelle
- Consulter cadastre.gouv.fr pour identifier le propriétaire (limité : uniquement nom si consultation ponctuelle)
- Alternative : croiser avec le registre des SCI (RNE, Pappers)

### Étape 3 : Croisement délibérations
- Consulter le registre des délibérations de la commune pour la période entourant la transaction
- Identifier les délibérations modifiant le PLU/zonage pour les parcelles concernées
- Vérifier si un élu propriétaire a participé au vote

### Étape 4 : Croisement permis de construire
- Consulter le registre des permis de construire (affichage en mairie, parfois en ligne)
- Vérifier si un permis a été déposé par l'acquéreur juste après la modification du PLU

### Étape 5 : Signal d'alerte
- Drapeau rouge si : élu propriétaire → vote PLU → revente dans les 24 mois → plus-value > 100 000 €

---

## 5. CAS DOCUMENTÉS

| Fait | Détail | Source |
|---|---|---|
| FCT-p9-016 | Affaire Levallois-Perret (Balkany) : condamnation pour prise illégale d'intérêts liée à des opérations immobilières, 4 ans prison ferme + inéligibilité (2019-2020) | Justice, presse |
| FCT-p9-017 | Affaire du Plateau de Saclay : enquête sur des modifications de PLU ayant bénéficié à des élus propriétaires fonciers, classée sans suite partiellement (2010-2015) | Mediapart, Le Monde |
| FCT-p9-018 | Rapport Cour des comptes 2023 sur « L'artificialisation des sols » : la CdC pointe le rôle des PLU dans la spéculation foncière | Cour des comptes |
| FCT-p9-019 | L'association Anticor a déposé plusieurs plaintes pour prise illégale d'intérêts liée à des PLU, notamment dans le Var et les Alpes-Maritimes (2018-2023) | Anticor, presse |
| FCT-p9-020 | Une enquête du Monde (2023) a utilisé les données DVF pour cartographier les conflits d'intérêts potentiels des élus locaux | Le Monde, Les Décodeurs |

---

## 6. OBSTACLES OSINT

| Fait | Détail |
|---|---|
| FCT-p9-021 | Le croisement DVF × cadastre × délibérations nécessite un traitement automatisé (scripts Python) — le volume DVF est de plusieurs Go/an |
| FCT-p9-022 | Le cadastre ne permet pas d'extraire le propriétaire en masse (limitation technique et légale : pas de réidentification selon art. R112 A-3 LPF) |
| FCT-p9-023 | Les délibérations municipales ne sont pas centralisées en opendata — il faut les consulter commune par commune |
| FCT-p9-024 | Les SCI (Sociétés Civiles Immobilières) masquent le bénéficiaire effectif — le RBE étant restreint depuis juillet 2024 (CJUE), cette couche est opaque |
| FCT-p9-025 | La détection automatisée de ce pattern est techniquement faisable mais nécessite un investissement technique lourd (scripts, base de données, web scraping) |

---

## 7. FAISABILITÉ

| Critère | Évaluation |
|---|---|
| Impact | TRÈS ÉLEVÉ — la spéculation foncière est l'un des principaux vecteurs de corruption locale en France |
| Faisabilité OSINT | MOYENNE — données DVF disponibles, mais le croisement PLU × cadastre × propriétaires est complexe |
| Verdict | **Ne pas investiguer maintenant** — nécessite une infrastructure technique (scripts Python, base de données) que nous n'avons pas en session. À programmer pour un run dédié (run3-spéculation-foncière). |

---

## 8. GAPs PRIORITAIRES

| ID | Description | Priorité |
|---|---|---|
| GAP-p9-001 | Télécharger et parser les 5 millésimes DVF (2021-2025) | P1 |
| GAP-p9-002 | Script Python de croisement DVF × PLU × cadastre | P1 |
| GAP-p9-003 | Sélectionner 3 communes-test (Tarn, Var, Alpes-Maritimes) | P2 |
| GAP-p9-004 | Consulter les registres de délibérations de ces 3 communes | P2 |
| GAP-p9-005 | Croiser avec les SCI via Pappers/INPI (dans la limite du RBE restreint) | P2 |

---

## 9. NEXT_ACTION

**P2** : nécessite un run dédié avec infrastructure technique (scripts Python). Priorité inférieure à P10 (JO 2024, surfacturation BTP) qui est plus accessible en OSINT pur.
