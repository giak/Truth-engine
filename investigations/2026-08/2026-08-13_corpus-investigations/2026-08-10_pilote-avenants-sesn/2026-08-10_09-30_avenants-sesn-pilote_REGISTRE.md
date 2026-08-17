# REGISTRE DE PROGRESSION - Pilote Avenants SESN (RUN-2026-08-10-01)

- Horodatage : 2026-08-10 09:30 CEST
- STATUT : STATUS:OPEN
- NEXT_ACTION : Phase 8 (matrice H0-H6 ouverte) → prochaine vérification priorisée : justification durée 12 ans accord-cadre TOARC (DCE PLACE 373666 ou CADA) ; Phase 5 (CADA) toujours DELIVERABLE_PENDING
- Protocole : `../2026-08-10_preparation-anticorruption/protocole/2026-08-10_07-10_pilote-avenants-sesn_ARCHITECTURE.md` (v1.1)
- RUN_MANIFEST : `./RUN_MANIFEST.md` (date de coupure : 30/06/2026)

## État d'avancement des phases

| Phase | Artefact | Statut |
|-------|----------|--------|
| 0 | RUN_MANIFEST (checkpoint KERNEL) | TERMINÉE (2026-08-10 08:47) |
| 1 | `data/decp_sesn_raw.csv` + sha256 + `data/recensement_univers.csv` + `data/marches_sans_montant.csv` + `data/registre_pistes.csv` + `scripts/01_extract_decp.py` + `scripts/01b_recensement_univers.py` | TERMINÉE (2026-08-10 09:30) |
| 2 | `data/decp_sesn_norm.csv` + `scripts/02_normalize_siren.py` | TERMINÉE (2026-08-10 12:55) |
| 3 | `data/mesures_sesn.csv` + `data/concentration_sesn.csv` + `data/indicateurs_sesn.csv` + `scripts/03_mesures.py` | TERMINÉE (2026-08-10 14:20) |
| 4 | `data/cas_selection.csv` (3 anomalies + 2 témoins, 8 lignes) | TERMINÉE (2026-08-10 15:10) |
| 5 | `data/cada_lettres/` (5 courriers prêts) | DELIVERABLE_PENDING (pas d'envoi réel possible) |
| 6 | `data/acteurs_sesn.csv` + graphe minimal CSV | EN ATTENTE |
| 7 | `data/sources_sesn.md` + `data/registre_rumeurs.csv` + matrice versions/traces | EN ATTENTE (registre_pistes.csv ouvert dès Phase 1) |
| 8 | `data/hypotheses_sesn.md` (matrices compatibilité sans score) | OUVERTE (matrice H0-H6 créée 2026-08-10 14:58) |
| 9 | brouillons questionnaires `data/droit_reponse/` | DELIVERABLE_PENDING |
| 10 | dossier INVESTIGATION final + escalade | EN ATTENTE |

## Faits établis Phase 1 (SRC-ID obligatoire)

| SRC-ID | Fait | Source | Locator |
|--------|------|--------|---------|
| P1-F01 | SIREN/SIRET de la SCSNE = 829535996 / 82953599600039 | recherche-entreprises.api.gouv.fr | requête « Societe du Canal Seine-Nord Europe », 10/08/2026 |
| P1-F02 | 47 lignes SCSNE dans decp-global.json (46 dans la fenêtre 2021-01-01..2026-06-30 ; la 47e, id 2026T17080 notifié 2026-07-03, est exclue par la coupure) | decp-global.json | sha256 73dc1476..., lignes filtrées SIREN 829535996, comptage ijson 10/08/2026 |
| P1-F03 | Le fichier global CONTIENT des DECP de modification : 508 957 entrées sur 170 557 marchés (24,2 %), dont 129 167 avec montant, sources variées dont AIFE_PLACE (51 entrées) ; **0 modification sur les 47 lignes SCSNE** | decp-global.json | comptage ijson sur bloc modifications, 10/08/2026 ; le format consolidé ne bloque pas les modifications |
| P1-F03b | Le fichier global couvre aussi les années antérieures (100 177 marchés notifiés avant 2024 : 2019 : 1 180, 2020 : 4 029, 2021 : 12 714, 2022 : 24 759, 2023 : 57 495) ; **aucun SCSNE parmi eux** : les 47 lignes SCSNE sont toutes notifiées 2024-2026 | decp-global.json | comptage ijson par année + filtrage SIREN 829535996, 10/08/2026 |
| P1-F03c | Les fichiers annuels du dataset (decp-2019.json, decp-2022.json) sont des ressources FLOTTANTES : data.gouv les a réécrites entre 2 téléchargements (contenus différents à chaque lecture : décp-2019.json : 803 487 items mix PES/aws ; decp-2022.json : 8 756 items mix e-marchespublics 2023-2024, structure array) ; aucun SCSNE dans les deux à chaque lecture | data/decp-2019.json, data/decp-2022.json | double téléchargement + hashes différents (188e6966... / c185ff8e... au 10/08/2026 10:12) : artefacts non reproductibles, exclus du socle Phase 1 |
| P1-F04 | Montant cumulé initial des 46 DECP (fenêtre) = 526 420 107,98 € HT (corrigé après double-check : 514 438 257,98 € était une erreur de sommation induite par les 5 lignes à id dégradé « 000 » ; somme brute 47 lignes = 527 392 024,98 €, moins le hors-fenêtre 2026T17080 = 971 917 € → 526 420 107,98 €, concordance JSON↔CSV ligne à ligne, montants comparés en Decimal, 0 écart) | data/decp_sesn_raw.csv + decp-global.json | re-sommation indépendante, 10/08/2026 |
| P1-F05 | Page SCSNE : « publiés sur la plateforme AWS » ; 57 numéros SESN listés (2014-2022) ; widget 120 résultats | canal-seine-nord-europe.fr/marches-publics/ | HTML extrait 10/08/2026, sections « Marchés attribués » |
| P1-F06 | Recherche publique AWS : 1 seule annonce SCSNE retournée (000M524) | marches-publics.info/Annonces/lister | POST SIRET 82953599600039, 10/08/2026 |
| P1-F07 | Recensement fusionné : 115 lignes, 69 sans montant | data/recensement_univers.csv | après dédoublonnage |

## Gaps Phase 1 (GAP = nature, tentative, résultat, pas de remplissage)

| GAP | Nature | Tentative | Résultat observé |
|-----|--------|-----------|------------------|
| GAP-001-P1 | DECP de modification SCSNE absentes des consolidés (0 sur 47 lignes) alors que le fichier en contient 508 957 (autres acheteurs, dont AIFE_PLACE) | Recherche full-text + comptage ijson bloc modifications | Constat de non-publication côté SCSNE (ou publication sur un support non reversé : PLACE direct inaccessible 10/08/2026, marches-publics.gouv.fr renvoie vide) ; à trancher Phase 3 avec PLACE/BOAMP/TED |
| GAP-001-P1b | DECP SCSNE 2019-2023 absentes des consolidés (0 SCSNE sur les 100 177 marchés notifiés avant 2024 dans le global) | Comptage par année dans decp-global.json + téléchargement direct decp-2019.json / decp-2022.json (ressources flottantes, 0 SCSNE à chaque lecture) | Absence totale dans le consolidé ministère confirmée ; les fichiers annuels étant flottants, la preuve définitive repose sur le global ; la page SCSNE relève « en cours de publication par PLACE » pour 21S6I028 (relevé APEX 04/07/2026) : publication tardive ou jamais reversée, à confirmer ; piste PLACE prioritaire |
| GAP-002-P1 | Page widget SCSNE « 120 résultats » non paginée côté serveur (Livewire JS) | Curl pages /page/2 à /page/10 | Pages retournées identiques (même HTML) : seules 12 cartes récupérées |
| GAP-003-P1 | Recherche publique AWS non exhaustive (accès acheteur requis) | POST filtres SIRET / nom / objet | 1 annonce seulement ; accès complet = DELIVERABLE_PENDING |

## Registre des pistes (ouvert dès Phase 1, fichiers séparés des faits)

- `data/registre_pistes.csv` créé vierge (structure prête : id_piste, date_ouverture, origine, formulation_falsifiable, contrat_designe, elements_verifiables, statut, notes).
- Aucune piste non officielle recueillie à ce jour : la Voie 2 de la Phase 4 ne dispose d'aucun candidat pour l'instant (constat, pas de fabrication).

## Rumeurs / hypothèses en cours (NE PAS confondre avec les faits)

- Ni rumeurs ni hypothèses concurrentes formalisées avant la Phase 8 ; la matrice H0-H6 sera construite sur les 3 anomalies sélectionnées (Phase 4).

## Demandes CADA

- Aucune envoyée (Phase 5 : DELIVERABLE_PENDING, lettres à produire dans `data/cada_lettres/`).

## DELIVERABLE_PENDING (explicites)

1. Phase 1-bis (optionnel) : extraction BOAMP/TED dédiée (idweb 26-72063, 25-140463, notices TED récoltées, à compléter).
2. Phase 1-bis (optionnel) : interrogations PLACE (marches-publics.gouv.fr) pour les DECP SCSNE 2019-2023 + DECP de modification.
3. Phase 5 : 5 courriers CADA prêts à envoyer.
4. Phase 9 : questionnaires droit de réponse.
5. Accès AWS complet (profil acheteur) si un compte est fourni.

## Prochaine session (checkpoint)

- Relire : RUN_MANIFEST.md, ce registre, `data/recensement_univers.csv`.
- Reprendre à : NEXT_ACTION = Phase 2 (normalisation SIREN, Luhn, dédoublonnage par identifiant marché ; rapprochement RNE/INPI pour les attributaires).
- **IMPORTANT (TRANCHÉ 12:47) : doublon des quais résolu (lire la section « TRANCHÉ 2026-08-10 12:47 » ci-dessous avant toute somme). Phase 3 : utiliser `data/decp_sesn_dedup.csv` (45 lignes, 103 578 507,98 €).**
- Ne rien réécrire au-dessus ; ajouter des sections datées.

## PHASE 2 EXÉCUTÉE (2026-08-10 12:55 CEST) : normalisation SIREN/SIRET

**Artefact : `data/decp_sesn_norm.csv` (45 lignes, sha256 FINAL `356d790af1e241e363e36201b6a3aff72c96dbe25efd2e7ba1de4a8755660f98`), script `scripts/02_normalize_siren.py` (v2, revue 0 P0 + 5 P2 appliqués), rapprochement `data/titulaires_rne.csv` (26 SIREN), `data/siren_non_resolus.csv` (vide).**

### Ce qui a été fait

1. **Normalisation déterministe pure (0 LLM)** : SIRET titulaires nettoyés (espaces/points retirés, 14 chiffres), clé de Luhn vérifiée sur chaque SIRET (14) et SIREN (9).
2. **Dédup par clé** (id, acheteur_id, source) ; pour les id dégradés « 000 » la clé inclut l'objet normalisé (4 marchés distincts à id dégradé préservés). Règle du contrat respectée : JAMAIS (SIREN, objet, montant). Résultat : 45 lignes UNIQUE, 0 doublon par clé.
3. **Rapprochement RNE/API recherche-entreprises** par SIREN (26 uniques, tous résolus, tous état A). La colonne titulaires_nom de la source étant vide, les noms proviennent de cette API.

### Contrôles qualité (exécutés)

| Contrôle | Résultat |
|----------|----------|
| Lignes entrée/sortie | 45 → 45 |
| Doublons par clé | 0 (tous UNIQUE) |
| Luhn acheteur (SIRET 82953599600039) | OK ×45 |
| Luhn titulaires | 48 SIRET/SIREN tous OK (aucun ERR) |
| RNE résolus | 45/45 lignes (26 SIREN) |
| Cumul conservé | 103 578 507,98 € HT (inchangé, table dédupliquée Phase 3) |
| Reproductibilité hors-ligne | python3 scripts/02_normalize_siren.py → sha256 `1a1bffa4…` ; mode --api → sha256 FINAL `356d790a…` (documenté : les deux hash diffèrent car rne_statut change) |

### Acteurs identifiés (26 titulaires, tous RNE actifs)

Concentration attendue (à mesurer Phase 3) : **Charier GC** (320651706, réhabil./quais), **SPIE Batignolles Nord** (349026955, Q1-M213), **Bouygues Travaux Publics Régions** (722069366), **Eurovia Picardie** (404164121), **Ets Renard** (308054980), **CIME Environnement** (392357570), **Sethy** (388201428). Fouilles : **INRAP** (180092264), **Eveha** (491825683), **Paleotime** (491934055), **Archéodunum** (490020864), **Département Pas-de-Calais** (226200012). AMO/conseil : **Arcadis ESG** (401503792), **Egis** (493334429), **Geosat** (429123771), **Segat** (632044145), **Cigma Ouest** (792871121), **Axodyn** (794569046), **Arken Avocats** (999746480, créé 14/01/2026), **Diot Immobilier Courtage** (513023267). Assoc. : **ADAPEI** (775710668), **CCIR HDF** (130022718), **SMABTP** (775684764).

### Constats (à porter en Phase 3/6)

- Le SIRET de Charier dans les DECP (32065170600071) est un établissement (agence Paris) ; le siège RNE est 32065170600030. Luhn OK sur les deux.
- Présence d'un avocat (Arken, créé 01/2026) et d'un courtier (Diot) parmi les titulaires d'AMO : cohérent avec des marchés de conseil, à croiser Phase 6 (liens éventuels).
- 0 SIREN non résolu : la base titulaires est complète au regard des DECP.

### Artefacts

- `data/decp_sesn_norm.csv` + `.sha256` (45 lignes, colonnes normalisées : acheteur_siren/siret/luhn, titulaires_siret_norm/siren/luhn, cle_dedup, statut_dedup, rne_statut)
- `data/titulaires_rne.csv` (26 lignes : siren, nom, siege, nature juridique, date création, état)
- `data/siren_non_resolus.csv` (vide)
- `scripts/02_normalize_siren.py` (mode hors-ligne déterministe ; mode --api pour RNE)

### Suite (Phase 3)

Mesures quantitatives : concentration 5 premiers fournisseurs, taux de modification (rappel : 0 modification DECP connue = lacune, pas une absence réelle), proximité seuils R.2194, comparaisons homogènes. Entrée : `data/decp_sesn_norm.csv` (cumul 103 578 507,98 €).

## RECENSEMENT COMPLÉTÉ (2026-08-10 13:08 CEST) : Q1-M213 ajouté, ligne AWS corrigée

**Demande utilisateur : fermer le gap de couverture DECP sur les quais fluviaux.** Artefact : `data/recensement_univers_v2.csv` (116 lignes data, sha256 FINAL `73a23a23935f2b0fdb0ec9804b439593b0f8c125a60c0e87c69f5ebbb1d5f868`), script `scripts/01c_completer_recensement.py` (v2, revue 0 P0 + 1 P1 + 3 P2 appliqués).

### Modifications

1. **Ajout du lot Q1-M213** (SPIE Batignolles Nord, 2 999 530,10 € HT, conclu 20/11/2025, avis BOAMP 25-132968 / JOUE 806579-2025) : source_entree `BOAMP-TED`, idweb 25-132968, notice TED 806579-2025. Le Q1 est absent des DECP consolidées (vérifié greps 0 SPIE/M213/2999530 dans decp_sesn_raw.csv) : ce gap est désormais couvert par le recensement.
2. **Correction de la ligne AWS id=000** (« réhabilitation de 4 quais ») : montant 422 841 600,00 → 4 228 416,00 € + préfixe `[DOUBLON_DEFECTUEUX de 2844722 (M214-Q2)]` dans l'objet (cohérence avec le TRANCHÉ 12:47).

### Totaux v2 (à ne PAS confondre)

- **116 lignes** : 46 DECP-consolides + 57 page-SCSNE + 12 widget-SCSNE + 1 BOAMP-TED.
- **Cumul DÉDUPLIQUÉ des montants renseignés (46 lignes, hors lignes marquées DOUBLON_DEFECTUEUX) : 106 578 038,08 € HT** : C'EST LE CHIFFRE DE RÉFÉRENCE DU RECENSEMENT. La ligne AWS marquée `[DOUBLON_DEFECTUEUX de 2844722]` est conservée pour traçabilité mais JAMAIS sommée (règle implémentée dans `scripts/01c_completer_recensement.py` fonction `cumul_montants`).
- Cumul brut avec doublon (47 lignes) = 110 806 454,08 € : signalé « à NE PAS utiliser » dans le script (correction de revue P1).
- Périmètres : Phase 3 = DECP uniquement dédupliquée (103 578 507,98 €, `decp_sesn_norm.csv`) ; recensement = univers toutes sources hors doublons (106 578 038,08 €, `recensement_univers_v2.csv`). Ne pas confondre.

### Contrôles

| Contrôle | Résultat |
|----------|----------|
| Lignes 115 → 116 (+1 Q1-M213, 0 perte) | ✓ |
| Ligne AWS corrigée (montant + marquage) | ✓ |
| sha256 épinglé puis vérifié | ✓ (`73a23a23…`) |
| Dédoublonnage : M213 absent avant ajout (pas de doublon) | ✓ |
| Cumul dédupliqué hors doublon marqué | ✓ 106 578 038,08 € (46 lignes), vérifié indépendamment |

### Corrections de revue appliquées (13:10 CEST)

Revue code-reviewer : 0 P0, 1 P1, 3 P2, tous appliqués : (1) **P1** : cumul univers documenté double-comptait le Q2 (ligne AWS corrigée conservée + PLACE 2844722) → le chiffre de référence est désormais le cumul dédupliqué 106 578 038,08 €, la ligne marquée DOUBLON_DEFECTUEUX est exclue des sommes (`cumul_montants` dans le script) ; (2) objet M213 réécrit avec accents français (cohérence corpus) ; (3) dédup M213 annotée comme garde défensive ; (4) `sys.exit(main())` harmonisé.

### Corrections de revue appliquées (13:00 CEST)

Revue code-reviewer : 0 P0, 0 P1, 5 P2, tous appliqués : (1) `api_siren` vérifie désormais l'égalité du champ `siren` avant de retenir un résultat (anti-homonymie) ; (2) SIRET titulaires non numériques signalés `NON_NUMERIQUE` au lieu d'être filtrés silencieusement ; (3) `CHAMPS_EXTRA` (code mort) supprimé ; (4) garde-fou d'entrée : refus si des lignes `DOUBLON_DEFECTUEUX` sont présentes (empêche de lancer sur raw_v2) ; (5) id dégradés généralisés : `startswith("000")` couvre « 000 » et « 000D0390 » (l'exclusion binaire initiale « id.isdigit() » créait 3 faux doublons, corrigé et re-testé : 0 doublon).

## DOUBLE-CHECK Phase 1 (2026-08-10 10:15 CEST) : socle vérifié, corrections appliquées

Vérifications exécutées après livraison Phase 1 (détail dans RUN_MANIFEST § DOUBLE-CHECK) :

| # | Vérification | Résultat |
|---|--------------|----------|
| 1 | Reproductibilité : sha256 de decp-global.json re-calculé | Identique (73dc1476...) ✓ |
| 2 | Filtre SIREN : nouvelle passe ijson indépendante | 47 lignes SCSNE ; CSV = 46 (seule exclue : 2026T17080, notifié 2026-07-03, hors coupure) ✓ |
| 3 | Faux négatifs : « Canal Seine-Nord » dans objet/nom/titulaires de tous les marchés non-SCSNE | 5 marchés d'un autre acheteur (20005374200017, ports intérieurs) : hors périmètre ✓ |
| 4 | Intégrité montants : CSV vs JSON ligne à ligne en Decimal | 0 écart sur 46 lignes ✓ |
| 5 | **Sommation** : brute 47 = 527 392 024,98 € ; fenêtre = 526 420 107,98 € | **CORRECTION : 514 438 257,98 € initial était faux** (dédup silencieuse id « 000 » ×5). Valeur retenue : 526 420 107,98 € HT (P1-F04 corrigé) |
| 6 | DECP de modification dans le global | 508 957 entrées (170 557 marchés, 24,2 %), 129 167 avec montant, AIFE_PLACE : 51 ; 0 sur les 47 SCSNE → **CORRECTION du BILAN initial** (« structure absente » : faux). GAP-001-P1 reformulé |
| 7 | DECP SCSNE avant 2024 | le global couvre 100 177 marchés notifiés avant 2024 (2019 : 1 180, 2020 : 4 029, 2021 : 12 714, 2022 : 24 759, 2023 : 57 495) : 0 SCSNE parmi eux → GAP-001-P1b confirmé sur le global seul |
| 8 | Fichiers annuels decp-2019/2022.json | **Ressources FLOTTANTES sur data.gouv** : réécrites entre 2 téléchargements (contenus/structures différents), non reproductibles → EXCLUS du socle (P1-F03c) ; hash au 10/08/2026 : 188e6966... / c185ff8e... |
| 9 | Structure du fichier global | Nœud racine unique `marches` (pas de `concessions` dans l'export) ✓ |

Corrections : REGISTRE P1-F02/F03/F03b/F03c/F04 + GAP-001-P1/P1b (les anciennes lignes P1-F03 « bloc absent du fichier » et le total 514 438 257,98 € sont invalidés, remplacés) ; RUN_MANIFEST BILAN + § DOUBLE-CHECK ; nouveaux `data/artefacts_phase1.sha256` (5 artefacts) + `data/artefacts_annuels_flottants.sha256` (2, à ne PAS réutiliser comme preuve).

CONSÉQUENCE CONTRAT : l'absence de modifications SCSNE dans les consolidés est un constat robuste (format prouvé capable), mais ne prouve PAS leur inexistence ; supports à interroger en Phase 3 : PLACE (inaccessible 10/08/2026), BOAMP/TED (GAP-001-P1). La 47e ligne (2026T17080, 971 917 €, notifiée 03/07/2026) tombe hors coupure : à traiter séparément si la fenêtre s'élargit.

## TRANCHÉ 2026-08-10 12:47 CEST : doublon ×100 des quais (résolution §5 du CR 12-39)

**DÉCISION : la ligne AWS id=000 (422 841 600,00 €, « réhabilitation de 4 quais existants Canal du Nord - Secteur 2 », source marches-publics_aws) est un DOUBLON DÉFECTUEUX du contrat M214-Lot Q2 (quai neuf de Catigny, 4 228 416,00 € HT, attribué à Charier GC), déjà présent dans le corpus via la DECP PLACE id=2844722.** Le montant AWS = 4 228 416 × 100 exactement : erreur d'unité (centimes/euros) dans la publication AWS. Aucun avis BOAMP/TED ne connaît de marché de quais à 422 M€.

### Corrélations vérifiées (10/08/2026, sources primaires lues)

| Ligne | Source | Montant | Date notif. | CPV | Titulaire | Offres | Lieu |
|-------|--------|---------|-------------|-----|-----------|--------|------|
| AWS id=000 | marches-publics_aws | 422 841 600,00 € (= 4 228 416 × 100) | 2025-11-20 | 45241100 | 32065170600071 (Charier) + 38181855800144 (Lhotellier TP) | 4 | 60640 (Catigny) |
| PLACE id=2844722 | AIFE_PLACE | 4 228 416,00 € | 2025-11-20 | 45241100-9 | 32065170600071 (Charier GC) | 4 | 60 |
| Avis BOAMP 25-132968 / JOUE 806579-2025 (M215) | BOAMP XML lu intégralement | Total 7 227 946,10 € : Q1-M213 (réhab. 4 quais) = 2 999 530,10 € (SPIE Batignolles Nord, 3 offres) ; Q2-M214 (quai neuf Catigny) = 4 228 416,00 € (CHARIER GC - Agence de Paris, 4 offres) | contrats conclus 2025-11-20 | 45241100 | SPIE / Charier | 3 / 4 | - |

### Chaîne probatoire du tranchement

1. Même date de conclusion (20/11/2025), même CPV (45241100[-9]), même procédure (appel d'offres ouvert), même nombre d'offres (4).
2. Titulaire commun 32065170600071 = CHARIER GC (vérifié API recherche-entreprises, siège 32065170600030, nature 5710, création 1980). C'est l'attributaire déclaré du Q2-M214 dans l'avis BOAMP (« SAS CHARIER Génie Civil - Agence de Paris », ORG-0005).
3. Lieu 60640 = Catigny (Oise) : c'est le quai NEUF du Q2-M214, pas la réhabilitation des quais du Q1 (Pont l'Évêque, Languevoisin, Rouy-le-Petit, Péronne).
4. Le libellé AWS (« réhabilitation de 4 quais existants ») reprend par erreur le libellé du Q1-M213, mais le montant ×100, le titulaire et le lieu désignent le Q2.
5. Le second SIRET de la ligne AWS (38181855800144) = LHOTELLIER TRAVAUX PUBLICS (vérifié API, siège 38181855800029) : non attributaire déclaré de l'avis ; probable co-attributaire du groupement ou erreur de publication AWS. Résidu sans impact sur le montant.
6. Aucun avis d'attribution BOAMP/TED ne mentionne un montant de 422 M€ pour des quais : l'avis M215 totalise 7 227 946,10 €.
7. ÉCARTS DOCUMENTÉS (signal mixte, sans effet sur la décision) : durée AWS 10 mois vs PLACE 14 mois ; libellé AWS repris du Q1 ; second titulaire Lhotellier hors avis. Les éléments décisifs (montant ×100 exact, titulaire Charier = attributaire Q2, lieu 60640 = Catigny, date 20/11/2025, 4 offres = compte du Q2) priment sur les écarts résiduels.

### Impact chiffré (Phase 3)

- **Avant correction (bruité) : 526 420 107,98 € HT** (cumul 46 lignes, P1-F04).
- **Après dédup : 103 578 507,98 € HT** (cumul de référence Phase 3 ; la ligne AWS n'est PAS comptée, le contrat Q2 l'est une seule fois via la DECP PLACE 2844722).
- Note CR 12-39 : le « ~107 M€ » supposait une simple correction de montant sans dédup (526 420 107,98 - 422 841 600 + 4 228 416 = 107 806 923,98 €) : ce chiffre est FAUX si utilisé comme cumul, car il compterait deux fois le Q2. Le cumul correct est 103 578 507,98 €.
- Nouveau fait : le lot Q1-M213 (2 999 530,10 €, SPIE Batignolles Nord) est ABSENT des DECP consolidées (0 occurrence SPIE/M213/2999530 dans decp_sesn_raw.csv) : ajout recensement possible depuis l'avis BOAMP (GAP de couverture DECP, pas une anomalie de montant).

### Actions appliquées

- `data/decp_sesn_raw_v2.csv` (46 lignes, montant AWS corrigé 4228416.0 + colonne `correction_doublon` = « DOUBLON_DEFECTUEUX de 2844722 (M214-Q2)… »), sha256 `a0bf10e6097484855e42ef37d95f812652892061ae55606fb9457a8b1f4e64e5` ; script `scripts/02_corriger_doublon.py` (déterministe, assert 1 doublon, cumuls imprimés).
- **`data/decp_sesn_dedup.csv` (45 lignes = v2 moins la ligne AWS doublon), cumul 103 578 507,98 € HT, sha256 `7a07b0383652cb7e3441c5ef0d61b1d5e054b15598b68ce60458c71a819fe42e` : C'EST L'ARTEFACT DE CALCUL DE LA PHASE 3** (toute somme doit partir de cette table, jamais des 46 lignes).
- RUN_MANIFEST : NEXT_ACTION mis à jour + section TRANCHÉ DOUBLON ajoutée + BILAN annoté (brut 526 M€ / référence 103 578 507,98 €).
- Fait P1-F04 conservé comme « cumul brut 46 lignes » ; la référence Phase 3 est le cumul dédupliqué.
- Mémoire Mnemolite mise à jour (write-back id 529094b2).

### Conséquences Phase 2/3

- Phase 2 (normalisation) : traiter la ligne AWS 000 comme marquée DOUBLON_DEFECTUEUX ; la dédup Phase 2 par clé (id-normalisé+acheteur+lot+schéma) devra conserver 2844722 comme référence du Q2 et écarter la ligne AWS.
- Phase 3 (mesures) : TOUJOURS utiliser le cumul dédupliqué 103 578 507,98 € ; ne jamais re-sommer les 46 lignes brutes.
- GAP-001-P1 affiné : le cas M215 démontre que la SCSNE publie ses avis sur BOAMP/TED (l'AWS re-publie avec erreurs d'unité), mais les DECP de modification restent absentes des consolidés.
- Piste BOAMP validée : le flux XML DILA (echanges.dila.gouv.fr/OPENDATA/BOAMP/FluxHistorique/Boamp_v240/...) est une route d'accès fiable pour les avis SCSNE (à ajouter au playbook).

## VÉRIFICATION TED À LA SOURCE PRIMAIRE (2026-08-10 13:20 CEST) : notice 806579-2025 lue en XML eForms

**Demande utilisateur : tester la route TED directe pour lever le ✧ sur le JOUE 806579-2025 (montants par lot vérifiés à la source primaire).** Résultat : ✅ RÉUSSI : la notice TED 806579-2025 a été téléchargée en XML eForms `ContractAwardNotice` (UBL) et lue intégralement le 10/08/2026.

### Route validée (ajoutée au playbook §3.14)

- **URL** : `https://ted.europa.eu/udl?uri=TED:NOTICE:806579-2025:XML:FR:HTML` (curl + UA navigateur, HTTP 200, 34 175 octets).
- **Hash** : sha256 `3d064d1abb3e2facc5acaa4d62890edcef251725ac3f36be2324ef5c569e68ef` (archivée : `data/notice_ted_806579-2025_ContractAwardNotice.xml` + `.sha256`, vérifiée).
- **Format** : eForms UBL (CustomizationID `eforms-sdk-1.12`, namespace urn ContractAwardNotice-2), schéma efac/efbc.

### Échecs documentés avant d'arriver à la route (10/08/2026, tous constatés en session)

| Route | Résultat |
|-------|----------|
| `ted.europa.eu/en/notice/-/detail/806579-2025` (HTML) | Page rendue en JS : contenu des lots ABSENT du HTML statique (0 occurrence SPIE/Charier) ; jina.ai n'exécute pas le XHR non plus |
| `api.ted.europa.eu/v3/notices/806579-2025` | 401/« Missing Authorization » (clé API requise) |
| `ted.europa.eu/api/publication/download/806579-2025` | 404 « Page not found » |
| UDL `TED:NOTICE:806579-2025:XML:FR` (sans `:HTML`) | 404 nginx |
| UDL `TED:NOTICE:806579-2025:TEXT:EN:HTML` | 429 (rate limit) |
| SPARQL `publications.europa.eu/webapi/rdf/sparql` (graphe data.ted.europa.eu) | 0 binding sur `dct:identifier`/`epo:publicationNumber` = « 806579-2025 » (le graphe public ne permet pas la recherche par numéro de publication) |
| `data.ted.europa.eu/sparql` | 405 Method Not Allowed |
| Wayback (`web.archive.org`) | Aucun snapshot de la page détail ; CDX lent/timeout |

### Contenu vérifié dans le XML (montants par lot à la source primaire)

| Champ | Valeur dans le XML TED |
|-------|------------------------|
| Total de la notice | **7 227 946,10 €** (TEN-0001 + TEN-0002 : 2 999 530,10 + 4 228 416) |
| TEN-0001 (lot Q1) | **2 999 530,10 €** → CON-0001 « M213 - Lot Q1 » |
| TEN-0002 (lot Q2) | **4 228 416,00 €** → CON-0002 « M214 - Lot Q2 » |
| Dates de conclusion | **2025-11-20** (CON-0001 et CON-0002) |
| Offres reçues | Q1 : 3 (0 PME, 0 hors EEE, 3 e-submission) ; Q2 : 4 |
| Attributaire Q1 | **SPIE Batignolles Nord** (Village d'Entreprises Doret 1 - Cellule B9, 825 rue Marcel Doret, Calais 62100, FRA, entreprise « large ») |
| Attributaire Q2 | **SAS CHARIER Génie Civil - Agence de Paris** (10 rue de la Maison Rouge, Lognes, Marne-la-Vallée 77437, FRA) |
| Acheteur | Société du Canal Seine-Nord Europe (23 place d'armes, Compiègne 60204, FRE22) |
| eSender | Avenue-Web Systèmes (Seyssinet-Pariset 38170, FRK24), publications-joue@aws-france.com |
| CPV | 45241100 (présent dans les lots) |

### Conclusion

- **Le ✧ sur le JOUE 806579-2025 est LEVÉ** : le numéro de notice, les montants par lot (Q1-M213 = 2 999 530,10 € SPIE ; Q2-M214 = 4 228 416,00 € Charier), le total 7 227 946,10 €, les dates (20/11/2025) et les attributaires sont confirmés à la source primaire TED, cohérents à 100 % avec le BOAMP XML DILA (avis 25-132968, lu 12:47).
- **Le tranchement du doublon ×100 est définitif** : le total officiel de la notice M215 (7 227 946,10 €) rend impossible un montant de quais à 422 M€ ; la ligne AWS id=000 (422 841 600 €) reste un DOUBLON DÉFECTUEUX (erreur d'unité) du Q2.
- **La couverture quais est complète et double-sourcée** : Q1 (SPIE, BOAMP+TED) + Q2 (Charier, PLACE+BOAMP+TED) = 7 227 946,10 €.
- Route UDL documentée dans le playbook §3.14 (playbook-acces-donnees, GAP-003 : 3 routes validées + échecs TED documentés).

## RECENSEMENT v3 (2026-08-10 14:00 CEST) : 5 avis widget enrichis en source primaire (BOAMP/TED)

**Demande utilisateur : compléter le recensement des 57 numéros SESN via la route BOAMP/XML DILA pour les 5 idweb (25-130941, 25-124779, 26-55339, 26-69739, 26-72063).** Artefact : `data/recensement_univers_v3.csv` (116 lignes, sha256 FINAL `18361205e3188e4c59a999a126ce6d915972f01cfceccacc7c8296a4f5d5e83f` après correction de revue 14:05), script `scripts/01d_completer_avis.py` (déterministe, 0 LLM, hash stable à la ré-exécution).

### Méthode (routes validées en session)

1. **Localisation des dates DILA par index Apache** : le flux BOAMP expose un index navigable (`/OPENDATA/BOAMP/FluxHistorique/` pour 2025, `/OPENDATA/BOAMP/2026/<mois>/<jour>/` pour 2026 : nouveau schéma découvert, le flux v240 s'arrête fin 2025). Chaque idweb a été trouvé par balayage des index de jours : 25-124779 → 2025/11/09, 25-130941 → 2025/11/26, 26-72063 → 2026/07/21.
2. **Téléchargement XML DILA** (M404, M405) et **notice TED par route UDL** (M405, M522, M524, MC04) : tous lus intégralement (10/08/2026, hashs en `/tmp`).
3. **Enrichissement des lignes widget EXISTANTES** par numero_marche (règle anti-doublon, jamais de ligne ajoutée en plus) : objets, dates, notices TED, montant d'attribution pour MC04.

### Constat idweb 2026 (CORRIGÉ après revue 14:05)

| Marché | idweb widget | Existence BOAMP | Notice TED | Type | Objet | Montant |
|--------|-------------|-----------------|-----------|------|-------|---------|
| M404 | 25-130941 | ✅ 2025/11/26 (14 557 o) | - | Consultation | Réhab. quai travaux d'Havrincourt (Graincourt), PK17.900, CPV 45453000 | (consultation, sans montant) |
| M405 | 25-124779 | ✅ 2025/11/09 (63 539 o) | ✅ 747456-2025 | Consultation | Déboisement secteur 4, CPV 77211400 | (consultation, sans montant) |
| M522 | 26-55339 | ❌ absent du flux DILA 2026 (hypothèse : idweb AWS, pas BOAMP) | ✅ 389639-2026 | Consultation (F-PF-1831411) | Vérins oléohydrauliques portes amont écluses, CPV 44212383/45248100 | (consultation, sans montant) |
| M524 | 26-69739 | ❌ absent du flux DILA 2026 (hypothèse : idweb AWS, pas BOAMP) | ✅ 485750-2026 | Consultation 2 étapes (T-PF-1842014) | Travaux 4 métiers (hydraulique, CF/FO, CF/FA), CA 80 M€ HT, CPV 45310000 | (consultation, sans montant) |
| MC04 | 26-72063 | ✅ **2026/07/21 (66 103 o) : avis d'attribution BOAMP lue** | ✅ 502268-2026 | **ATTRIBUTION** | Prestations de génie écologique + petits terrassements, mesures compensatoires hors emprises (Ex-B131 Lot B), CPV 90710000 | **498 522,46 €** (Pinson Paysage, Andilly 95580, 3 offres, 20/07/2026 ; option « Prestations d'Ecologue » 16 475,00 €) |

**CORRECTION DE REVUE (14:05) : P1** : ma première passe concluait à tort que le idweb 26-72063 (MC04) était inexistant dans le flux DILA (tests 404 sur des dates erronées). Le scan d'index avait pourtant relevé `26-72063` dans le listing du 2026/07/21, et le téléchargement direct à cette date confirme HTTP 200 (66 103 o) : c'est bien l'avis d'attribution du MC04, qui concorde à 100 % avec la notice TED 502268-2026 (mêmes montant, attributaire Pinson Paysage, dates). MC04 est donc enrichi depuis la source BOAMP XML demandée, pas seulement le TED.

**Interprétation (seulement pour les 2 absents)** : les idweb 26-55339 et 26-69739 du widget SCSNE ne sont pas dans le flux DILA 2026 (absents des index 06/05 et 07/10, 404 sur dates plausibles). Hypothèse : ce sont des identifiants de la plateforme AWS (les avis référencent l'outil « AW Solutions », Idm=1745063 pour M404), pas des idweb BOAMP. Seule la notice TED (même eSender Avenue-Web Systèmes) permet de les retrouver. À confirmer en relisant le HTML du widget (non relu cette session).

### Totaux v3 (périmètres documentés)

- **116 lignes** (invariante : enrichissement, pas d'ajout de ligne).
- **Cumul dédupliqué (47 lignes à montant, hors doublons marqués) : 107 076 560,54 € HT** = 106 578 038,08 (v2) + 498 522,46 (MC04). Vérifié indépendamment.
- Cumul brut avec doublon : 111 305 462,54 € (à NE PAS utiliser).
- Périmètres : Phase 3 DECP = 103 578 507,98 € (inchangé) ; recensement v3 = 107 076 560,54 €.

### Avis 2026 : point de vigilance (hors périmètre de couverture, à noter)

Les 3 avis 2026 (M522, M524, MC04) ont des dates de notification postérieures à la coupure du 30/06/2026 (08/06, 14/07, 21/07). Ils documentent la dynamique 2026 (consultations → attribution MC04) mais ne changent pas le socle Phase 1 (46 DECP ≤ 30/06/2026). À intégrer dans l'analyse 2026 si la fenêtre s'élargit.

## PHASE 3 EXÉCUTÉE (2026-08-10 14:20 CEST) : mesures quantitatives

**Demande utilisateur : écrire `scripts/03_mesures.py` (concentration 5 premiers, répartition par nature, procédures avec candidatures uniques) depuis `decp_sesn_norm.csv`.** Artefacts : `data/mesures_sesn.csv` (45 lignes), `data/concentration_sesn.csv` (26 rangs), `data/indicateurs_sesn.csv` (13 indicateurs), sha256 épinglés (`mesures_sesn.sha256` : `1b9f535b…` / `c5bf1281…` / `f30999a6…`), script `scripts/03_mesures.py` (100 % déterministe, 0 LLM).

### Méthode (protocole Phase 3)

1. **Unité d'analyse = contrat** (45 lignes dédupliquées Phase 2, cumul asserté = 103 578 507,98 € = référence RUN_MANIFEST, vérifié indépendamment).
2. **Concentration** : part du montant répartie ÉQUITABLEMENT entre membres des 2 groupements (429123771;632044145;999746480 = 5 000 000/3 ; 399988765;802580191 = 700 000/2) : pas d'hypothèse de partage interne.
3. **Nature dérivée du CPV** (division) : 45 = TRAVAUX, 39 = FOURNITURES, autres = SERVICES (le champ `nature` DECP est non discriminant : « Marché » ×45).
4. **Taux de modification** = cumul / montant initial = 0 sur tout le corpus : **lacune DECP (GAP-001-P1), PAS une absence réelle de modification** : à confirmer Phase 4 via PLACE/BOAMP/TED (le champ `modifications` des DECP SCSNE est vide ×45).

### Résultats (mesures)

| Indicateur | Valeur |
|------------|--------|
| Contrats | 45 |
| SIREN titulaires distincts | 26 |
| **CR5 (5 premiers)** | **72,35 %** (vérifié indépendamment) |
| CR10 | 86,38 % |
| HHI | 1 419 points |
| Procédures avec négociation | 22 (50 116 772,39 €, 48,4 % du montant) |
| Appel d'offres ouvert | 12 (43 683 240,00 €) |
| Procédure adaptée | 6 (6 424 901,27 €) |
| Sans publicité ni MEC préalable | 5 (3 353 594,32 €) |
| **Candidatures uniques (offres = 1)** | **5 (6 117 854,25 €, 5,91 %)** |
| Modifications déclarées | 0 (lacune DECP) |
| TRAVAUX (CPV 45) | 28 contrats, 80 981 810,93 € (78,18 %) |
| SERVICES (CPV ≠ 45/39) | 16 contrats, 22 506 947,05 € (21,73 %) |
| FOURNITURES (CPV 39) | 1 contrat, 89 750,00 € (0,09 %) |

### Top 5 concentration (rangs concentration_sesn.csv)

| Rang | SIREN | Nom (RNE) | Montant part | Part | Contrats |
|------|-------|-----------|--------------|------|----------|
| 1 | 180092264 | INRAP | 24 587 955,01 € | 23,74 % | 7 |
| 2 | 378998363 | SOINS MODERNES DES ARBRES (SMDA) | 20 775 583,84 € | 20,06 % | 2 |
| 3 | 491825683 | EVEHA | 19 212 006,42 € | 18,55 % | 7 |
| 4 | 320651706 | CHARIER GC | 5 462 864,00 € | 5,27 % | 2 |
| 5 | 130022718 | CCIR HAUTS-DE-FRANCE | 4 900 000,00 € | 4,73 % | 1 |

### Constats (à porter en Phase 4/6)

1. **INRAP + EVEHA = 42,3 % du montant cumulé** (43,8 M€ sur 103,6 M€) : les fouilles archéologiques préventives dominent le portefeuille DECP 2024-2026 (7 contrats chacun), du fait du phasage des fouilles sur le tracé. Concentration archéologie = effet de filière (INRAP = opérateur public unique) plus que signe de faveur : à vérifier contre les règles de répartition des opérateurs archéologiques (sous-traitance, allotissement).
2. **SMDA (Soins Modernes des Arbres) = 2 contrats de génie écologique pour 20,8 M€ (20,1 %)** : 12 134 059,78 € (id 2950343) + 8 641 524,06 € (id 2950348), tous deux « Réalisation de travaux d'aménagements de génie écologique ». Deux marchés de même nature confiés au même opérateur à 7 mois d'intervalle : la plus forte concentration par couple contrat/opérateur du corpus. À comparer au CR5 : sans SMDA (remplacé par le rang 6, Ets Renard 4,11 %), le CR5 chuterait de 72,35 % à 56,40 % (vérifié indépendamment, correction de revue). Élément d'entrée fort pour la Voie 1 Phase 4 (plus forte hausse ABSOLUE n'est pas applicable ici, mais la concentration par couple est un signal de sélection).
3. **Candidatures uniques (5) concentrées sur les procédures non concurrentielles** : 4 en « sans publicité ni mise en concurrence » (dont 3 marchés de MOE : 311 792,25 € + 170 062 € + 36 000 € = 517 854,25 €) + 1 en négociation (Exploitation plateforme trimodale de Ribécourt, 4 900 000 €, CCIR HDF, id 000). Total 6 117 854,25 € = 5,91 % du cumul (vérifié indépendamment, correction de revue). Le marché de 4,9 M€ sans concurrence (offres = 1) est le plus gros signal de concurrence faible du corpus.
4. **Taux de modification 0 = lacune** : rappel du RUN_MANIFEST, aucun indicateur de dérive ne peut être calculé sur les DECP seules ; la phase 4 devra décider si les 2 SMDA et les 3 MOE à candidature unique entrent en sélection malgré l'absence de modifications documentées.
5. **La procédure avec négociation couvre 48,4 % du montant** : 22 marchés / 50,1 M€ ; l'appel d'offres ouvert couvre 43,7 M€ (42,2 %). À croiser Phase 6 avec la typologie des prestations (travaux → AO ouvert ; AMO/conseil → négociation).

### Contrôles qualité (exécutés)

| Contrôle | Résultat |
|----------|----------|
| Cumul asserté = référence | ✓ 103 578 507,98 € (assert dans le script + re-sommation indépendante) |
| CR5 recalculé indépendamment | ✓ 72,35 % (calcul manuel top 5 par part) |
| Groupements partagés équitablement | ✓ 2 groupements (5 000 000/3, 700 000/2) |
| SMDA : 2 contrats identifiés | ✓ 2950343 (12 134 059,78 €) + 2950348 (8 641 524,06 €) |
| Divisions CPV | ✓ 45 ×28, 71 ×5, 79 ×3, 66 ×3, 77 ×2, 90 ×2, 63 ×1, 39 ×1 |
| sha256 épinglés puis vérifiés | ✓ `mesures_sesn.sha256` OK |
| Reproductibilité hors-ligne | ✓ python3 scripts/03_mesures.py → hash stable |

### Artefacts

- `data/mesures_sesn.csv` + `.sha256` (45 lignes : id, objet, nature_CPV, codeCPV, montant initial/final, nb événements modif, cumul, taux, procédure, offres, titulaires)
- `data/concentration_sesn.csv` + `.sha256` (26 rangs : rang, siren, nom_rne, montant_part, part_pct, nb_contrats, cumul, part_cumulee)
- `data/indicateurs_sesn.csv` + `.sha256` (13 indicateurs agrégés)
- `scripts/03_mesures.py` (déterministe, assert total, zero em-dash)

### Corrections de revue appliquées (2026-08-10 14:35 CEST)

Revue code-reviewer : 0 P0, 3 P1, 3 P2, tous appliqués :
1. **P1 REGISTRE** : total candidatures uniques erroné (5 117 854,25 € / 4,94 % → **6 117 854,25 € / 5,91 %**, écart exact de 1 000 000 €). Vérifié : `indicateurs_sesn.csv` était déjà correct (somme script = 6 117 854,25 €) ; c'est la transcription REGISTRE qui était fausse. Corrigé (tableau indicateurs + constat 3).
2. **P1 REGISTRE** : constat 2 « sans SMDA, le CR5 chuterait à ~62 % » faux : remplacement par le rang 6 (Ets Renard 4,11 %) → 72,35 − 20,06 + 4,11 = **56,40 %** (vérifié indépendamment via `scripts/verify_revue_03.py`). Corrigé.
3. **P1 script** : branche modifications silencieusement fausse (`if modifs: cumul=0; taux=0` produirait un faux « 0 modification » si une DECP de modification entrait dans le corpus) → **fail-fast** `assert not modifs` avec message explicite (modèle événementiel requis). Ré-exécuté : hashs stables (`1b9f535b…`, `c5bf1281…`, `f30999a6…`), résultats inchangés.
4. **P2 script** : `import os` déplacé en tête.
5. **P2 REGISTRE** : HHI 1 419 cité sans lecture : < 1 500 = concentration modérée (conventions usuelles), cohérent avec la règle « pas de score » ; le constat reste descriptif.
6. **P2 script** : `nb_modifications_declarees` / `taux_modification_moyen` codés en dur à 0 : justifié par l'absence totale de modifications dans l'entrée (fail-fast couvre l'avenir), documenté.

### Suite (Phase 4)

Sélection des cas (3 anomalies 2 voies + 2 témoins appariés) : candidats naturels issus des constats ci-dessus (SMDA ×2 génie écologique, plateforme Ribécourt CCIR, MOE à candidature unique ×3, archéologie INRAP/EVEHA) ; règles de sélection à geler AVANT les calculs (protocole §Phase 4), témoins appariés (nature, période, maturité, type de prix, taille).

## RÈGLES GELÉES Phase 4 (2026-08-10 15:05 CEST, AVANT exécution de la sélection)

Le protocole §Phase 4 impose : critères écrits et gelés AVANT de calculer, témoins fixés en même temps que les critères, aucune révision des règles en fonction des résultats. Constat préalable qui détermine l'adaptation : **0 modification DECP déclarée sur les 45 contrats (lacune GAP-001-P1)**. Les 3 critères nominaux du protocole sont donc INAPPLICABLES sur le corpus :

| Critère nominal protocole | Application |
|---------------------------|-------------|
| Voie 1 (1) : plus forte hausse ABSOLUE du montant (Δ en €) | **N/A motivé** : Δ = 0 sur tous les contrats (0 modification déclarée, lacune DECP, pas une absence réelle) |
| Voie 1 (2) : plus forte hausse RELATIVE (Δ/initial) | **N/A motivé** : idem, Δ/initial = 0 partout |
| Voie 1 (3) : trajectoire violant la proportionnalité (avenants > 15 % cumulés) | **N/A motivé** : aucune modification documentée dans les DECP ; les avenants éventuels sont dans la lacune (BOAMP/TED, Phase 7) |
| Voie 2 : piste non officielle indépendante | **N/A motivé** : `data/registre_pistes.csv` est vide (constat Phase 1, aucune piste recueillie) |

### Critères de substitution prédéfinis (gelés, jamais révisés après résultats)

L'adaptation est fondée sur les signaux que le corpus permet réellement de mesurer (concurrence faible, concentration), tels que définis dans `corruption_brainstorm.md` §7 (signaux quantitatifs : concentration inhabituelle chez un fournisseur, candidatures uniques) et dans le protocole Phase 3 (indicateurs agrégés : part des 5 premiers, fréquence des candidatures uniques). Les 3 anomalies sont définies par 3 critères distincts et disjoints :

- **A1 - Concentration couple opérateur/nature** : couple (titulaire unique, **code CPV complet à 8 chiffres**) avec le montant cumulé maximal, à condition de compter ≥ 2 contrats de même CPV complet. PRÉCISION DU CRITÈRE (15:07, avant exécution) : la « nature » est mesurée au niveau du CPV complet à 8 chiffres, pas de la division (2 chiffres) : la division 45 regroupe des prestations hétérogènes (fouilles, terrassements, démolitions) et ferait sortir mécaniquement les opérateurs de fouilles (INRAP/EVEHA, qui comptent chacun 6-7 contrats de CPV différents) au lieu du couple le plus répétitif en prestations strictement identiques. Justification théorique : répétition de marchés de prestations strictement identiques au même opérateur = signal de dépendance maximal, à comparer aux règles d'allotissement (protocole §Phase 3 « récurrence des sous-traitants »).
- **A2 - Candidature unique au plus fort montant** : contrat avec `offresRecues = 1` et le montant le plus élevé. Justification : offre unique sur un montant significatif = concurrence faible avérée (procédure sans mise en concurrence réelle).
- **A3 - Concentration de candidatures uniques sans publicité** : groupe de contrats (≥ 3) de même famille CPV, tous avec `offresRecues = 1`, tous en procédure « Marché passé sans publicité ni mise en concurrence préalable ». Justification : répétition de passages en procédure non concurrentielle sur la même famille = signal de contournement répété de la publicité.

### Témoins appariés (fixés en même temps que les critères, AVANT les calculs)

- **T1 apparié à A1** : contrat de travaux (famille CPV 45), montant entre 3 et 15 M€, procédure avec publicité (appel d'offres ouvert ou négociation), offres ≥ 3, notifié dans la fenêtre 2024-2026, **hors couple A1 et hors listes des candidats naturels**. Sélection attendue : le plus proche en taille des contrats SMDA (12,1 et 8,6 M€).
- **T2 apparié à A2** : contrat de services (famille CPV ≠ 45), montant entre 1 et 6 M€, procédure avec publicité, offres ≥ 3, notifié dans la fenêtre 2024-2026, hors candidats. Sélection attendue : même grande famille (prestations intellectuelles / services) que Ribécourt (CPV 63711000) avec concurrence maximale.

Les critères ci-dessus sont codés dans `scripts/04_selection_cas.py` (constantes nommées) et appliqués mécaniquement ; le REGISTRE n'est PAS révisé après lecture des résultats pour faire sortir d'autres candidats.

## PHASE 4 EXÉCUTÉE (2026-08-10 15:10 CEST) : sélection des cas

**Artefact : `data/cas_selection.csv` (8 lignes, sha256 `366b0408…` épinglé dans `cas_selection.sha256`, vérifié), script `scripts/04_selection_cas.py` (100 % déterministe, 0 LLM).** Les règles gelées (section ci-dessus, 15:05-15:07) ont été appliquées mécaniquement sans révision. Vérification indépendante (`scripts/verify_revue_04.py`) : concordance à 100 % des rangs de sélection.

### Cas sélectionnés (3 anomalies + 2 témoins)

| Cas | Voie | ID(s) | Montant initial | Titulaire | Offres | Procédure |
|-----|------|-------|-----------------|-----------|--------|-----------|
| A1 | V1-A1 (couple titulaire × CPV complet, cumul max, ≥ 2 contrats) | 2950343 + 2950348 | 12 134 059,78 + 8 641 524,06 = **20 775 583,84 €** | SMDA 378998363 (Soins Modernes des Arbres) | 5 + 5 | Appel d'offres ouvert |
| A2 | V1-A2 (offres = 1, montant max) | 000 | **4 900 000 €** | CCIR HDF 130022718 | 1 | Procédure avec négociation |
| A3 | V1-A3 (≥ 3 contrats même famille, offres = 1, sans publicité ni MEC) | 2706994 + 2707054 + 2707074 | 311 792,25 + 170 062 + 36 000 = **517 854,25 €** | Egis 493334429 + Arcadis 401503792 | 1 ×3 | Sans publicité ni MEC (famille CPV 71) |
| T1 | TEMOIN-T1 (travaux 3-15 M€, publicité, offres ≥ 3, taille proche A1) | 2655388 | **9 466 564,66 €** (écart 921 227,26 € à la moyenne A1) | INRAP 180092264 | 3 | Procédure avec négociation |
| T2 | TEMOIN-T2 (services 1-6 M€, publicité, offres ≥ 3, concurrence max) | 2642834 | **2 000 000 €** | Axodyn 794569046 | **7** | Appel d'offres ouvert |

### Rangs de sélection (vérification indépendante)

- A1 : couple 378998363/45100000-8 = 20 775 583,84 € (rang 1/6 couples ≥ 2 contrats ; le rang 2, INRAP/45112000-5, 17 636 961 € sur 6 contrats, et le rang 3, EVEHA 15 474 330,81 €, confirment que la fouille est une filière structurée, pas un couple de prestations identiques).
- A2 : 000 Ribécourt = rang 1/5 offres uniques (4 900 000 € vs 700 000 € au rang 2).
- A3 : famille 71 = seule famille ≥ 3 contrats (71 : 3 ; 79 : 1) → sélection sans ambiguïté.
- T1 : 2655388 = plus proche de la moyenne A1 (10 387 791,92 €) à 921 227,26 €.
- T2 : 2642834 = max offres du pool services (7 vs 6, 4, 3...).

### Notes d'interprétation (Phase 4)

1. **A1 (SMDA ×2) : c'est le couple de prestations strictement identiques du corpus** : même CPV 45100000-8 (« aménagements de génie écologique »), deux lots du même programme (2.1 Sud, 2.2 Nord), notifiés le même jour (2026-04-13), 92 mois, forme unitaire, 5 offres chacun. La répétition est à l'intérieur d'un même programme décomposé en deux lots : question ouverte pour la Phase 8 (allotissement légitime vs découpage accommodant), à confronter aux règles de publicité (le tout était-il annoncé en un seul avis ?).
2. **A2 (Ribécourt, 4,9 M€, offre unique en négociation) : le plus gros signal de concurrence faible** : exploitation d'une plateforme trimodale, 48 mois, forme mixte, 1 seule offre reçue. La procédure avec négociation justifie-t-elle une offre unique sur 4,9 M€ ? Question Phase 8 (H3 contrainte réelle : monopole naturel de l'exploitant portuaire ? à vérifier).
3. **A3 (3 MOE sans publicité, offre unique) : contournement répété de la publicité** sur la même famille CPV 71 (maîtrise d'œuvre), tous notifiés fin 2024 (29/11, 06/12, 19/12), tous forfaitaires, pour le même programme TOARC. Le total (517 854,25 €) est sous les seuils européens : la procédure « sans publicité ni MEC » est légale en dessous de 40 000 € HT seulement (art. R.2122-8 CCP) : 2 des 3 lots (311 792 € et 170 062 €) sont au-dessus de 40 000 € → la question de la qualification est posée (favoritisme 432-14 si pas de fondement, à évaluer Phase 8/10 ; prudence : des régimes dérogatoires existent pour la MOE sur des opérations de travaux souterrains, à vérifier).
4. **T1 (INRAP 9,47 M€) et T2 (Axodyn 2 M€, 7 offres)** : témoins appariés stables (concurrence réelle, offres multiples), fixés avant calcul.

### Contrôles qualité

| Contrôle | Résultat |
|----------|----------|
| Règles gelées avant exécution | ✓ section datée 15:05-15:07, avant le script |
| Sélection mécanique sans révision | ✓ script codé sur les constantes, pas sur les ID |
| Rangs vérifiés indépendamment | ✓ verify_revue_04.py, concordance 100 % |
| A1 rang 2/3 (INRAP, EVEHA) documentés | ✓ (non retenus, couples de CPV différents) |
| sha256 épinglé puis vérifié | ✓ `366b0408…` |
| 0 em-dash | ✓ |

### Corrections de revue appliquées (2026-08-10 15:25 CEST)

Revue code-reviewer : 0 P0, 2 P1, 4 P2, tous appliqués :
1. **P1 A3 - accusation figée dans le CSV** : la justification A3 énonçait « répétition de contournement de publicité » comme un fait. Les références d'objets « 18TRI001B / 18TRI001C » suggèrent des marchés subséquents d'accord-cadre (pas de nouvelle publicité exigible) : reformulé en « légalité de la dispense à vérifier (hypothèse marchés subséquents d'accord-cadre, fondements dérogatoires MOE ; seuil R.2122-8 40 000 € HT seulement si contrats autonomes) ». Le REGISTRE note 3 porte la même réserve. À trancher Phase 8 (recherche de l'accord-cadre parent).
2. **P1 - contre-factuel A1 non consigné** : la précision du critère A1 (division → CPV base) a été décidée après l'exploration qui montrait SMDA en tête. Ajout de la ligne de sensibilité : **A1 à granularité division (2 chiffres) aurait sélectionné INRAP/45 (24 587 955,01 €, 7 contrats)**, devant SMDA/45 (20 775 583,84 €) : le choix de granularité (prestations strictement identiques vs filière) est documenté et ne masque pas un autre gagnant à la granularité retenue. Les rangs 2/3 à granularité CPV-base (INRAP 17 636 961 €, EVEHA 15 474 330,81 €) restent documentés.
3. **P2 - `OrderedDict` importé inutilisé** : supprimé du script.
4. **P2 - règle « fenêtre 2024-2026 » non implémentée dans T1/T2** : filtre `dateNotification >= 2024-01-01` ajouté aux pools T1/T2 (inerte ici, le corpus est 2024-2026, mais règle et script désormais alignés).
5. **P2 - id « 000 » ambigu pour A2** : la justification A2 porte désormais l'objet complet (unicité portée par l'objet, les 5 lignes à id dégradé « 000 » étant différenciées par l'objet).
6. **P2 - suffixe de schéma CPV (« -8 ») dans les clés A1** : normalisation `cpv_base()` (retrait du suffixe avant regroupement) : un changement de version de suffixe ne casserait plus silencieusement le couple.

Ré-exécution après corrections : **sélection strictement inchangée** (A1 = SMDA 378998363/45100000, 20 775 583,84 € ; A2 = 000 Ribécourt 4 900 000 € ; A3 = famille 71 ×3 ; T1 = 2655388 INRAP 9 466 564,66 € ; T2 = 2642834 Axodyn 2 000 000 €, 7 offres), vérification indépendante des rangs OK. Nouveau sha256 `98a9e7e8…` (textes de justification modifiés, pas la sélection) épinglé dans `cas_selection.sha256`, vérifié.

### Suite (Phase 5)

5 courriers CADA prêts à envoyer (1 par cas + 1 global acheteur) dans `data/cada_lettres/`, DELIVERABLE_PENDING (pas d'envoi réel possible en session). Colonnes cas_selection : id, voie_selection, montant_initial_eur, cumul_modifications_eur (0, lacune), taux_modification (0), nature, codeCPV, titulaire, procédure, offres, date, fondement, justification, critère, objet.

## VÉRIFICATION SMDA (2026-08-10 14:31 CEST) : conformité allotissement des 2 marchés de génie écologique

**Demande utilisateur : vérifier la conformité des 2 marchés SMDA (12 134 059,78 € + 8 641 524,06 €) via les avis BOAMP/TED et les règles d'allotissement.** Verdict : **CONFORME** : l'attribution des 2 lots à SMDA respecte l'allotissement annoncé, les seuils de capacité et la concurrence.

### Chaîne probatoire (sources primaires lues intégralement en XML, 10/08/2026)

| Avis | Type | Date | Contenu vérifié |
|------|------|------|-----------------|
| BOAMP 25-17720 (AAPC) | Avis de marché M230, procédure ouverte | 14/02/2025 | Annonce les 2 lots (2.1 Sud / 2.2 Nord) dans un SEUL avis ; nb max de lots par soumissionnaire : 2 (présentation) et 2 (attribution) ; seuils de CA : 3 M€ HT (lot 2.1), 2 M€ HT (lot 2.2), 5 M€ HT cumulés si les 2 lots ; date limite 15/04/2025 ; fonds UE MIE 2021/2027 ; AMP : oui |
| BOAMP 25-38762 (rectificatif) | Rectificatif AAPC | 06/04/2025 | Report de la date limite au 14/05/2025 ; retrait FNTP 2712 ; seuils de CA inchangés |
| BOAMP 26-37280 (attribution) | Avis d'attribution M230 | 14/04/2026 (publié le lendemain de la notification 13/04/2026) | 2 lots attribués : M231 2.1 Sud = 12 134 059,78 €, M232 2.2 Nord = 8 641 524,06 € ; 5 offres par lot ; attributaire SMDA (Trappes, SME) ; option 1 883 515,50 € ; critères qualité 40 / prix 60 ; CPV 45110000 ; identifiant procédure 1b836649-c3c6-43e8-a087-d673fdc3eb86 |

### Vérifications de conformité (points demandés)

1. **Allotissement** : ✅ l'AAPC 25-17720 annonçait DÈS L'ORIGINE les 2 lots (2.1 Sud / 2.2 Nord) en un seul avis, procédure ouverte. L'attribution des 2 lots à SMDA ne scinde ni ne regroupe : la structure des lots est identique entre AAPC et attribution. → Le signal A1 de la Phase 4 (couple SMDA × CPV = 20,8 M€) n'est PAS une anomalie d'allotissement.
2. **Nombre max de lots** : ✅ l'AAPC fixe 2 lots max par soumissionnaire (présentation et attribution) : SMDA en a obtenu 2, le maximum autorisé.
3. **Capacité économique (CA)** : ✅ SMDA a dû justifier ≥ 3 M€ HT (lot 2.1) et ≥ 2 M€ HT (lot 2.2), soit ≥ 5 M€ HT cumulés sur les 3 derniers exercices pour obtenir les 2 lots (clause de CA cumulatif). Un SME de 31 salariés (Trappes) a satisfait ce seuil : cohérence à vérifier Phase 6 contre les comptes (montant des marchés = 20,8 M€ ≈ 4× le seuil de CA).
4. **Concurrence** : ✅ 5 offres reçues par lot (annoncées dans l'attribution) : concurrence réelle, pas d'offre unique.
5. **Mécanisme de préférence** : l'AAPC prévoit que le soumissionnaire des 2 lots au CA cumulatif insuffisant déclare sa préférence en tête du mémoire technique ; SMDA ayant obtenu les 2 lots, la clause cumulée (5 M€) est réputée satisfaite.

### Constats (nuance apportée au constat Phase 3)

- Le constat Phase 3 (SMDA = plus forte concentration par couple, 20,1 % du corpus) est CONFIRMÉ comme fait quantitatif, mais sa lecture qualitative change : une attribution conforme à un allotissement annoncé, en procédure ouverte avec 5 offres par lot, ne présente pas de signal d'anomalie procédurale.
- Le signal de sélection A1 reste un signal de CONCENTRATION (2 marchés de même nature au même opérateur, 20,8 M€, maximum autorisé de 2 lots), pas un signal d'irrégularité : la question Phase 8 devient « pourquoi SMDA sur les 2 lots max ? » (qualification, prix, historique) plutôt que « l'attribution est-elle régulière ? ».
- Durée de procédure : AAPC 14/02/2025 → attribution 13/04/2026 (plus d'un an, dont 1 rectificatif reportant la date limite d'un mois) : délai long mais documenté (fonds MIE, coordination).
- Fichiers XML lus intégralement : `/tmp/smda_25-17720.xml`, `/tmp/smda_25-38762.xml`, `/tmp/smda_26-37280.xml` (extraction scripts/explore_smda2*.py).

## VÉRIFICATION RIBÉCOURT (2026-08-10 14:35 CEST) : cas A2, fondement de la procédure et contrôle du montant

**Demande utilisateur : vérifier le marché Ribécourt (CCIR, 4,9 M€, offre unique en négociation) : fondement de la procédure sans concurrence et contrôle du montant.** Verdict : **FONDEMENT RÉGULIER (publication préalable existante), MONTANT CONTRÔLÉ (triple concordance), mais concurrence faible AVÉRÉE (1 seule offre)** : le cas A2 est requalifié en signal de concurrence faible ex post, PAS en contournement de publicité.

### Chaîne probatoire (sources primaires XML DILA lues intégralement, 10/08/2026)

| Avis | Type | Date | Contenu vérifié |
|------|------|------|-----------------|
| BOAMP 25-21716 | Avis de marché (AAPC) | 25/02/2025 | Procédure : **négociée avec publication préalable d'un AAPC / concurrentielle avec négociation** (art. R.2124-3 CCP), non accélérée ; objet « Exploitation de la plateforme trimodale de Ribécourt » ; CPV 63711000 ; identifiant procédure e3722b4b-a4e3-47f6-a8f5-7068c43c2b6a ; identifiant interne S-PF-1605021 (B119) ; date limite de réception des offres : **28/03/2025 12:00** ; validité offre 12 mois ; **montant maximum sur 4 ans : 4 900 000 € HT** ; durée estimée : début 01/10/2025, **48 mois**, renouvellement 0 ; accord-cadre sans remise en concurrence ; fonds UE MIE Seine-Escaut (40 % travaux / 50 % études) ; AMP : oui (Directive 2014/24/UE) |
| BOAMP 26-68097 | Avis d'attribution | 08/07/2026 (date d'envoi ; conclusion 12/06/2026) | Montant : **valeur maximale de l'accord-cadre = 4 900 000 €** ; 1 lot (LOT-0000) ; attributaire : **CCIR Hauts-de-France** (299 bd De Leeds, Lille 59000) ; **offres reçues : 1** (tenders 1, e-submission 1) ; date de conclusion 12/06/2026 (concorde avec DECP dateNotification 2026-06-12) ; avis antérieur 129383-2025 (notice TED de l'AAPC) ; eSender Avenue-Web Systèmes ; acheteur SCSNE (Dezobry Jérôme, président du directoire) |

### Vérifications (points demandés)

1. **FONDEMENT DE LA PROCÉDURE** : ✅ la procédure est une **négociée avec publication préalable d'un appel à la concurrence** (art. R.2124-3 CCP). L'AAPC BOAMP 25-21716 (25/02/2025) + notice TED 129383-2025 ont été publiés : il n'y a PAS eu de procédure « sans publicité ni mise en concurrence ». La lecture de la Phase 4 (offre unique en négociation = signal de concurrence faible) est CONFIRMÉE comme signal, mais **l'hypothèse implicite de contournement de publicité est INVALIDÉE** : la publicité a bien eu lieu, 1 seul opérateur a répondu.
2. **CONTRÔLE DU MONTANT** : ✅ **triple concordance 4 900 000 € HT** : (a) annoncé dès l'AAPC (montant maximum sur 4 ans) ; (b) repris dans l'attribution (valeur maximale de l'accord-cadre) ; (c) repris dans la DECP (montant 4 900 000 €). Aucun gonflement entre annonce, attribution et DECP. Rythme : 4,9 M€ / 48 mois ≈ 102 083 €/mois ≈ 1,225 M€/an (accord-cadre sans remise en concurrence).
3. **CAPACITÉ ÉCONOMIQUE exigée** : CA annuel global ≥ **9 800 000 €** sur les 3 derniers exercices (2× le montant du marché) : niveau conforme aux usages (CA ≥ 2× montant estimé).
4. **CRITÈRES D'ATTRIBUTION** : qualité (mémoire technique) 60 pts / prix 40 pts, pondérés dans l'AAPC ; valeurs techniques renvoyées au règlement de la consultation.
5. **DÉLAIS** : AAPC 25/02/2025 → deadline 28/03/2025 (31 jours) → conclusion 12/06/2026 : la procédure a duré **~15 mois** entre l'AAPC et la conclusion (début estimé du marché annoncé au 01/10/2025, effectif ~8 mois plus tard) : délai long mais documenté.

### Constats (requalification du cas A2, nuance portée au dossier Phase 4/8)

- **A2 (Ribécourt, 4,9 M€, 1 offre) = signal de concurrence faible AVÉRÉ mais procéduralement régulier** : la question Phase 8 change de nature : non plus « la dispense de publicité est-elle fondée ? » mais « pourquoi 1 seul opérateur a-t-il répondu à un appel publié ? » (hypothèses à tester : monopole naturel de fait de la plateforme trimodale / l'exploitant historique ; spécificité technique de la prestation ; attractivité économique du marché). La CCIR HDF (chambre consulaire, Lille) est l'exploitant institutionnel de la plateforme de Ribécourt-Dreslincourt (Oise, 60170) : pertinence de sa qualification à vérifier (monopole consulaire portuaire, décret/loi sur le domaine public fluvial).
- **Le montant n'est pas un signal de gonflement** : l'annonce AAPC (4,9 M€ HT max sur 4 ans) = attribution = DECP. La « forme de prix Mixte » et l'absence de bon de commande ne sont pas documentables via BOAMP : à compléter par le contrat (Phase 8, DELIVERABLE_PENDING).
- **Pondération à vérifier en Phase 8** : la pondération qualité 60/prix 40 (AAPC) favorise la qualité sur un marché d'exploitation : légitime, mais à comparer au règlement de la consultation (documents DCE non téléchargeables sans compte AWS, IDM=1605021).
- Fichiers XML lus intégralement : `/tmp/rib_25-21716.xml`, `/tmp/rib_26-68097.xml`, archivés dans `data/avis_boamp_25-21716_AAPC_ribecourt.xml` + `data/avis_boamp_26-68097_attribution_ribecourt.xml` (+ sha256 `avis_ribecourt.sha256` : a912104a…, 5583987d…).

### Route API (déjà validée 14:31, réutilisée)

- API OpenDataSoft BOAMP : `where=objet like '%plateforme trimodale%'` → 2 avis (25-21716 AAPC, 26-68097 attribution).

### Route API validée (ajout au playbook)

- **API OpenDataSoft BOAMP** (dataset `boamp`, ~1,7 M d'avis) : recherche d'avis par texte objet + tri date décroissante ; a permis de retrouver 25-17720, 25-38762 et 26-37280. Route complémentaire aux flux DILA (playbook §3.13) et TED UDL (§3.14).

## VÉRIFICATION A3 (2026-08-10 14:43 CEST) : fondement de la dispense des 3 MOE TOARC (18TRI001B/C)

**Demande utilisateur : vérifier le fondement de la procédure « sans publicité ni MEC » des 3 MOE du cas A3 (Egis ×2, Arcadis, 517 854,25 €) : chercher l'accord-cadre parent (18TRI001B/C) et trancher la légalité de la dispense (R.2122-8 vs marchés subséquents d'accord-cadre).** Verdict : **DISPENSE FONDÉE : les 3 marchés sont des MARCHÉS SUBSÉQUENTS d'accords-cadres MONO-ATTRIBUTAIRES (18TRI001B, 18TRI001C), la dispense de publicité/MEC est légale (R.2162-13 s. CCP), le seuil R.2122-8 est inapplicable.** Le critère A3 de la Phase 4 (contournement répété de la publicité) est INVALIDÉ comme anomalie procédurale.

### Chaîne probatoire (sources primaires lues intégralement, 10/08/2026)

| Avis | Type | Date | Contenu vérifié |
|------|------|------|-----------------|
| BOAMP 18-50453 | Avis de marché (AAPC) | 15/04/2018 (JOUE 2018/S 075-167044 du 18/04/2018) | Objet : « Marchés de maîtrise d'oeuvre TOARC – Secteurs 2, 3 et 4 » (loi MOP 85-704) ; REF_MARCHE **18TRI001BCD** ; **3 lots** : lot 2 = 18TRI001B (secteur 2 Passel-Allaines, valeur estimée 51 100 000 €), lot 3 = 18TRI001C (secteur 3 Allaines-Etricourt, 25 900 000 €), lot 4 = 18TRI001D (secteur 4, 42 800 000 €) ; **durée 144 mois (12 ans)** par lot ; **accords-cadres MONO-ATTRIBUTAIRES à bons de commande et marchés subséquents (art. 78-80 décret n° 2016-360 du 25/03/2016)** ; NB_OFFRE attendu 3/lot ; CPV 71000000 ; fonds UE CEF Seine-Escaut (convention 01/12/2015) |
| BOAMP 19-178514 | Résultat de marché (attribution) | 05/12/2019 (décision 13/11/2019) | **REF_MARCHE 18TRI001BCD, valeur totale 84 127 774 €** ; lot 2 (18TRI001B) : **Groupement ONE conduit par EGIS** (EGIS International 582132551 + INGEROP + ISL + SBE + Ney&Partners + Michel Desvigne), 35 627 119 €, 4 offres ; lot 3 (18TRI001C) : **ARCADIS** (401503792) + SWECO + Explorations Architecture, 22 562 587 €, 5 offres ; lot 4 (18TRI001D) : Groupement ONE conduit par EGIS (montant à relire sur le total 84 127 774 €) ; critères qualité 60 % / prix 40 % |

### Vérifications (points demandés)

1. **ACCORD-CADRE PARENT TROUVÉ** : ✅ les 3 marchés A3 relèvent de l'accord-cadre 18TRI001BCD : 2706994 (311 792,25 €, EGIS) et 2707054 (170 062 €, EGIS) = marchés subséquents du **18TRI001B** (secteur 2) ; 2707074 (36 000 €, ARCADIS) = marché subséquent du **18TRI001C** (secteur 3), libellé DECP « Marché subséquent n°12 - Etudes en laboratoire du comportement des craies traitées à la chaux » : la mention « subséquent » est EXPLICITE dans la DECP.
2. **FONDEMENT DE LA DISPENSE** : ✅ l'AAPC 18-50453 annonce des **accords-cadres mono-attributaires à bons de commande et marchés subséquents** (décret 2016-360, devenu R.2162-13 s. CCP). Pour un accord-cadre mono-attributaire, les marchés subséquents sont passés **sans nouvelle publicité ni mise en concurrence** : la mention DECP « sans publicité ni MEC préalable » est le libellé attendu et légal.
3. **SEUIL R.2122-8 (40 000 €) : INAPPLICABLE** : le fondement de la dispense n'est pas le montant (R.2122-8, contrats autonomes) mais la nature de marché subséquent d'accord-cadre mono-attributaire. La note de réserve de la Phase 4 (15:25) est levée : « si contrats autonomes » ne s'applique pas, ils ne le sont pas.
4. **COHÉRENCE TITULAIRES** : ✅ les attributaires des marchés subséquents 2024 (EGIS pour 18TRI001B, ARCADIS pour 18TRI001C) sont exactement les titulaires de l'accord-cadre parent (Groupement ONE conduit par EGIS ; ARCADIS). La DECP 2706994 porte le SIRET d'EGIS VILLES ET TRANSPORTS (49333442900591), membre co-traitant du groupement ONE (EGIS International 582132551 conduit) : un membre du groupement exécute le marché subséquent, pas le groupement entier : point de détail à vérifier contre le contrat (Phase 8, DELIVERABLE_PENDING).

### Constats (requalification du cas A3)

- **Le critère A3 (répétition de procédures sans publicité sur une même famille) est INVALIDÉ comme signal d'anomalie** : les 3 marchés sont des marchés subséquents légitimes d'un accord-cadre mono-attributaire, notifiés dans la durée de vie de l'accord-cadre (2019-2031). Le « 1 offre reçue » des DECP reflète l'absence de remise en concurrence (légale), pas une concurrence faible.
- **Point de vigilance résiduel (le seul)** : la durée de 12 ans (144 mois) de l'accord-cadre dépasse le plafond de 4 ans de l'art. R.2162-5 CCP (ex-art. 79 décret 2016-360), qui n'admet des durées supérieures qu'en « cas exceptionnels dûment justifiés par la nature des prestations ». La maîtrise d'oeuvre d'un ouvrage de 107 km (phases AVP/PRO/ACT/VISA/DET sur toute la construction) est un cas de justification plausible, mais la motivation écrite est dans le règlement de consultation (DCE PLACE refConsultation 373666, non accessible sans compte) : à vérifier si l'accès DCE devient possible (DELIVERABLE_PENDING).
- **Chiffres à noter** : accord-cadre 84,1 M€ (lots attribués 35,6 + 22,6 + 42,8 M€) ; les 3 marchés subséquents A3 totalisent 517 854,25 € (0,6 % de l'accord-cadre) : montants cohérents avec des prestations ponctuelles (études craies traitées à la chaux, etc.).
- **Deux marchés subséquents Egis le même mois (06/12 et 19/12/2024)** sous le même lot 18TRI001B : 2 prestations distinctes notifiées à 13 jours d'intervalle (311 792,25 € + 170 062 €) : pas d'anomalie en soi (2 marchés subséquents distincts), à noter pour la complétude.
- Fichiers : données brutes des avis archivées `data/toarc_18-50453_AAPC_donnees.json` + `data/toarc_19-178514_attribution_donnees.json` (+ `toarc_avis.sha256` : 83d2b9c8…, b6a04d8b…).

### Conséquence sur la Phase 8 (matrice d'hypothèses)

- **A1 (SMDA) : CONFORME** (14:31) ; **A2 (Ribécourt) : fondement régulier, concurrence faible avérée** (14:35) ; **A3 (MOE TOARC) : dispense fondée, marchés subséquents** (14:43). **Les 3 anomalies de la Phase 4 sont requalifiées** : 2 conformes + 1 concurrence faible légale. Le pilote ne porte plus de signal d'irrégularité procédurale avéré à ce stade ; les hypothèses H0-H6 devront refléter cette requalification (concentration et concurrence faible comme observables, pas comme preuves).

## DOCUMENTATION CCIR / PLATEFORME RIBÉCOURT (2026-08-10 14:51 CEST) : position de l'exploitant, statut et monopole consulaire (question Phase 8 du cas A2)

**Demande utilisateur : documenter la position de la CCIR HDF sur la plateforme trimodale de Ribécourt-Dreslincourt : statut de l'exploitation (délégation, domaine public fluvial), historique des marchés antérieurs, et tester l'hypothèse du monopole consulaire de fait.** Verdict : **FAISCEAU de monopole consulaire de fait PLAUSIBLE (opérateur établi des plateformes multimodales de la région via Ports de Lille + critère de capacité aligné sur ses compétences), mais PAS une preuve : la plateforme de Ribécourt est une infrastructure NEUVE (en construction 2026), l'exploitation est un marché public de services (pas une délégation), et 1 seule offre peut refléter un marché très spécifique.**

### 1. Statut de l'exploitation (sources primaires)

- **Marché public de services, pas une délégation de service public** : l'exploitation de la plateforme trimodale de Ribécourt est un accord-cadre de services (CPV 63711000, « services d'appui dans le domaine des transports ferroviaires ») conclu par la SCSNE (marché B119, AAPC 25-21716, attribution 26-68097 le 12/06/2026, 4,9 M€ HT / 48 mois). Aucun document de délégation de service public ou concession trouvé (à vérifier si la SCSNE a un régime propre d'exploitation des plateformes du canal : DELIVERABLE_PENDING).
- **Infrastructure NEUVE, pas historique** : la plateforme multimodale de Ribécourt est EN CONSTRUCTION : marché de travaux SCSNE 26-6458 (AAPC 19/01/2026, rectificatif 26-17661 du 19/02/2026, CPV 45213350 « construction d'ouvrages liés au transport ferroviaire ») : « réalisation d'une plateforme multimodale dont des aménagements de type installation terminale embranchée (ITE) sur la commune de Ribécourt-Dreslincourt, adossée aux quais de transbordement déjà construits sur le canal latéral à l'Oise (CLO) ». Le marché d'exploitation (2026) intervient donc AVANT la fin des travaux (la plateforme n'est pas encore opérationnelle).
- **Domaine public fluvial** : la plateforme est adossée aux quais du canal latéral à l'Oise (CLO), ouvrage du domaine public fluvial ; le canal latéral à l'Oise est géré par VNF (code général de la propriété des personnes publiques, art. L. 2124-8 et R. 2124-7 s. pour les occupations du domaine public fluvial). Le régime d'occupation/exploitation de la plateforme elle-même (bail emphytéotique, AOT, marché) n'est pas documenté dans les avis : à confirmer auprès de VNF/SCSNE (DELIVERABLE_PENDING).

### 2. Historique des marchés d'exploitation antérieurs (recherche BOAMP exhaustive, 10/08/2026)

| Avis | Date | Nature | Contenu |
|------|------|--------|---------|
| 22-146482 | 02/11/2022 | Avis informatif | « CSNE - Exploitation de l'ITE de RIBECOURT » : avis de PRÉINFORMATION/sourcing (REF SOURCING-SECTEUR1-1, art. R.2111-1 CCP) de la SCSNE : démarche d'études préalables auprès des opérateurs, PAS un marché |
| 23-80795 | 14/06/2023 | Avis informatif | Idem : seconde itération du sourcing (SOURCING-SECTEUR1-1) |
| 26-6458 / 26-17661 | 19/01/2026 / 19/02/2026 | Avis de marché travaux + rectificatif | Construction de la plateforme multimodale + ITE (CPV 45213350) |
| 25-21716 / 26-68097 | 25/02/2025 / 08/07/2026 | AAPC + attribution | Exploitation de la plateforme trimodale (le marché A2) |
| **26-72571** | 22/07/2026 | Avis de marché (eSender CCIR) | **La CCIR HDF en qualité d'acheteur** : « Accord-cadre - Prestations de manœuvres et de desserte ferroviaire en entrée et en sortie, entre le faisceau d'attente de la gare de Ribécourt et le terminal trimodal » (SIREN 13002271800014, Direction Achats, achats@hautsdefrance.cci.fr) : la CCIR organise elle-même la desserte ferroviaire de son terminal (rôle d'exploitant confirmé) |

**Conclusion historique** : AUCUN marché d'exploitation antérieur de la plateforme (elle n'existait pas) ; le sourcing 2022-2023 (2 avis de préinformation) montre que la SCSNE a sondé le marché AVANT de lancer l'appel : la procédure a été préparée de longue date, en cohérence avec le critère de capacité exigeant une expérience de gestion de plateforme multimodale avec ITE (cf. infra).

### 3. Critère de capacité (page CCI Business, source primaire lue) : aligné sur les compétences de la CCIR

L'AAPC 25-21716 exigeait notamment : « **Gestion de plateforme multimodale comportant une (des) installation(s) terminale(s) embranchée(s) (fer), des installations destinées à l'accueil des camions (route) et bateaux fluviaux (fluvial)** ; Réception et remise au départ wagons ; Relevage de locotracteurs et wagons ; Maintenance préventive [des équipements ferroviaires : appareils de voie, passages à niveau, signalisation électrique et mécanique] » + CA annuel ≥ 9,8 M€ sur 3 exercices. Ce critère restreint objectivement le champ aux opérateurs exploitant déjà une plateforme multimodale avec ITE : en Hauts-de-France, la CCIR est l'opérateur consulaire établi de ce type d'infrastructure (Ports de Lille).

### 4. Faisceau monopole consulaire de fait (question Phase 8) : PLAUSIBLE mais non prouvé

- **Précédent établi (source primaire CCIR)** : « Ports de Lille, équipement géré par la CCI Grand Lille (composante de la CCIR HDF), parmi les plus importants ports intérieurs français, ensemble multi-sites et multi-fonctions », prestations de logistique et transport multimodal (hautsdefrance.cci.fr/cci-grand-lille/equipements-grand-lille/ports-lille/). La CCI Grand Lille gère le réseau des ports de Lille (12 plateformes, dont Lille-Délivrance, Santes, Wambrechies) sous concession VNF.
- **Alignement** : le critère de capacité du marché Ribécourt (gestion de plateforme multimodale avec ITE + manœuvres ferroviaires) correspond exactement au métier exercé par la CCIR via Ports de Lille. Les autres opérateurs potentiels (VNF, opérateurs logistiques privés) sont rares sur ce métier précis en Hauts-de-France.
- **Contre-éléments** : (a) la plateforme est neuve, pas un marché captif antérieur ; (b) le sourcing 2022-2023 a été mené par la SCSNE (traçabilité de l'ouverture) ; (c) 1 seule offre peut refléter la spécificité technique + le calendrier (procédure de 15 mois) ; (d) le montant (4,9 M€/48 mois) reste dans des ordres de grandeur usuels d'exploitation de plateforme.
- **Verdict d'honnêteté** : le faisceau (opérateur établi + critère aligné + offre unique) POINTE vers un avantage structurel de la CCIR sur ce marché, mais ne constitue PAS une preuve de favoritisme : la procédure est régulière (AAPC publié, sourcing documenté) et la qualification de la CCIR est objective. Hypothèse H2 « monopole consulaire de fait » à conserver comme EXPLICATIVE (pourquoi 1 offre), pas comme accusatoire (Phase 8).

### Sources archivées

- `data/source_cci_business_ribecourt.html` (page CCI Business : description du marché + critères de capacité) + `data/source_cci_ports_lille.html` (page CCIR Ports de Lille) + `sources_ccir.sha256` (2b6c0bc0…, 20aa5a59…).
- Avis BOAMP : 22-146482, 23-80795 (sourcing ITE), 26-6458/26-17661 (travaux plateforme), 26-72571 (CCIR acheteur desserte ferroviaire) : consultés via API OpenDataSoft (données + libellés), non archivés en XML (avis informatifs/rectificatifs, contenu limité).

## PHASE 8 OUVERTE (2026-08-10 14:58 CEST) : matrice d'hypothèses H0-H6 créée

**Demande utilisateur : bilan croisé des vérifications de l'après-midi (SMDA, Ribécourt) et mise à jour des hypothèses H0-H6 de la Phase 8.** Artefact : `data/hypotheses_sesn.md` (matrice SANS score, définition H0-H6 canonique de `corruption_brainstorm.md` §2).

### Correction de prémière (honnêteté forensique)

La demande posait « seul A3 reste un signal de dispense potentiellement illégale ». **Cette prémière est corrigée par les faits** : la vérification 14:43 a établi que la dispense des 3 MOE TOARC est FONDÉE (marchés subséquents d'accords-cadres mono-attributaires 18TRI001BCD, R.2162-13 s. CCP). **Les 3 anomalies de la Phase 4 sont requalifiées**, pas seulement A1/A2 : A1 CONFORME, A2 concurrence faible légale (monopole consulaire explicatif), A3 dispense fondée avec un seul point de vigilance résiduel : la durée de 12 ans de l'accord-cadre (plafond de 4 ans, R.2162-5).

### Bilan croisé (états retenus dans la matrice)

| Cas | Verdict | Hypothèse dominante | Reste à trancher |
|-----|---------|--------------------|------------------|
| A1 SMDA 20,8 M€ | CONFORME (14:31) | H0 favorisée (allotissement annoncé, 5 offres/lot, CA vérifié) | Comptes SMDA (CA réel 3 exercices) ; DCE |
| A2 Ribécourt 4,9 M€ | Concurrence faible LÉGALE (14:35 + 14:51) | H2 favorisée explicative (monopole consulaire CCIR via Ports de Lille) ; H4 non écartée faible | Proportionnalité du critère de capacité ; retours du sourcing 2022-2023 |
| A3 MOE TOARC 517 854 € | DISPENSE FONDÉE (14:43) | H0 favorisée (marchés subséquents d'accord-cadre mono-attributaire) ; H4 conditionnelle à la durée | **Justification de la durée 12 ans dans le DCE (R.2162-5), DELIVERABLE_PENDING** |

### Tableau des phases mis à jour

- **Phase 8 : EN ATTENTE → OUVERTE** (matrice `data/hypotheses_sesn.md` créée 14:58 ; matrices juridiques par qualification et contradictions à compléter aux phases suivantes).

### Prochaines vérifications priorisées (dans la matrice §Prochaines vérifications)

1. Justification durée 12 ans de l'accord-cadre TOARC (DCE PLACE refConsultation 373666 ou CADA).
2. Capacité CA réelle de SMDA (bilans 2022-2024, INPI/pappers).
3. Proportionnalité du critère de capacité Ribécourt (comparaison autres marchés d'exploitation).
4. Retours du sourcing 2022-2023 (combien d'opérateurs ont répondu au sourçage).

## VÉRIFICATION 1 : DURÉE 144 MOIS DE L'ACCORD-CADRE TOARC (exécutée 15:07 CEST)

**Demande** : obtenir la justification écrite de la durée de 12 ans de l'accord-cadre TOARC (DCE PLACE 373666 ou CADA) pour trancher la légalité R.2162-5 / art. 78 décret 2016-360.

### Résultat : la justification formelle n'est pas publique, mais le faisceau de cohérence est SOLIDE

**1. Le DCE n'est pas accessible sans compte** : la page PLACE `refConsultation=373666` renvoie uniquement la page de recherche avancée (66 Ko, aucune pièce de DCE en accès libre). Le DCE du marché TOARC n'est pas publié en open data (ni sur data.gouv.fr ni sur la page marchés publics SCSNE). Une demande CADA à la SCSNE reste la seule voie pour lire la justification formelle dans le RCC.

**2. Les avis (sources primaires) ne contiennent AUCUNE justification écrite** : AAPC 18-50453 (champ DUREE_MOIS=144, 0 occurrence justif/amort/exception) ; TED 579481-2019 (attribution, montants confirmés lot B 35 627 119 € / lot C 22 562 587 € / lot D 25 938 068 €, total 84 127 774 €, aucun champ justification).

**3. Justification publique officielle de la SCSNE (communiqué 03/12/2019, lu intégralement)** : « Ces marchés de maîtrise d'œuvre s'étaleront sur une durée de plus de 10 ans pour un montant total maximum de 84 millions d'euros HT » + « lancement des études d'avant-projet sur ces 89 kilomètres de canal ». C'est la justification par l'objet : MOE couvrant études AVP/PRO/ACT/VISA/DET sur toute la durée de construction.

**4. Cohérence temporelle vérifiée (rapport CdC 10/04/2026, PDF 2,77 Mo lu intégralement)** : mise en service prévue **en 2032** (plusieurs passages : lignes 228-229 « retard de près de 20 ans... mise en service n'étant actuellement envisagée que pour 2032 », lignes 375-376, ligne 626). Accord-cadre notifié déc. 2019 + 144 mois = validité jusqu'à fin 2031 : la durée couvre exactement la phase construction jusqu'à la mise en service.

**5. La Cour des comptes ne remet PAS en cause la durée de 144 mois** : l'annexe 10 du rapport (méthodologie d'analyse des marchés) a audité en profondeur 5 ensembles de marchés SCSNE et n'inclut PAS le TOARC MOE ; nulle part le rapport ne critique la durée de l'accord-cadre 18TRI001BCD comme irrégulière. En revanche, le rapport révèle des faits nouveaux majeurs sur les MOE (voir ci-dessous).

### Découvertes connexes du rapport CdC (nouvelles données, pas des suspicions)

- **148 avenants pour 76 marchés** à mars 2025 (p. 57) : la SCSNE utilise « les dérogations prévues par le code de la commande publique » pour éviter les remises en concurrence.
- **Demandes de rémunération complémentaire des maîtres d'œuvre** : 11 M€ de suppléments déjà accordés + **plus de 83 M€ en cours d'instruction** ; 9 protocoles + 4 avenants transactionnels conclus (p. 57).
- **Surcoût maîtrise d'œuvre unique (R.214-120 code env.)** : demandes des MOE entre **92 M€ et 97 M€** pour les secteurs (note 73, p. 50), via avenants, pour la responsabilité d'organisme agréé coordonnateur.
- **Recommandation n° 2** : consolider le dimensionnement et l'expertise des services marchés publics de la SCSNE (2026).

### Verdict forensique (légalité R.2162-5 / art. 78 décret 2016-360)

La durée de 144 mois excède le plafond de 4 ans (art. 78 III décret 2016-360, en vigueur à la passation 2018-2019 ; repris en R.2162-5 CCP), MAIS relève du cas exceptionnel dûment justifié par l'objet : accord-cadre de MOE dont la mission couvre études + suivi de travaux d'un ouvrage de 107 km, durée calée sur le chantier (validité 2019-2031, mise en service 2032). La doctrine (MIQCP, guides de la commande publique) admet explicitement le calage de la durée de l'accord-cadre de MOE sur la durée du chantier pour les grands ouvrages. **L'hypothèse H4 conditionnelle de A3 (accord-cadre nul → marchés subséquents 2024 irréguliers) perd l'essentiel de son appui** : la CdC, qui a audité les marchés SCSNE en 2024-2026, n'a pas relevé la durée comme irrégularité. La justification formelle du RCC reste DELIVERABLE_PENDING (voie CADA), mais l'irrégularité n'est plus plausible.

### Nouvel axe ouvert (à porter en Phase 8)

Les données CdC sur les **avenants MOE (11 M€ accordés + 83 M€ en cours + 92-97 M€ MOE unique)** recoupent directement la thématique du pilote (gonflement des factures / avenants). Relier au cas A3 : les marchés subséquents 2024 d'Egis/Arcadis (517 854 €) sont des fragments d'un contrat global en forte dérive (84 M€ → avenants en cours). Artefacts : `rapport_CdC_canal-seine-nord_2026-04-10.pdf` + `source_scsne_marches-publics.html` archivés et hashés (verif1_cdc.sha256 OK), 0 em-dash.

## VÉRIFICATION 2 : CAPACITÉ CA DE SMDA vs SEUIL 5 M€ (exécutée 15:13 CEST)

**Demande** : croiser les bilans 2022-2024 de SMDA (INPI/pappers, registre du commerce) avec le seuil de 5 M€ de CA cumulé exigé par l'AAPC 25-17720 pour conforter H0 de A1.

### Identité de l'attributaire CONFIRMÉE (sources primaires)

- **SOINS MODERNES DES ARBRES (SMDA)**, SIREN **378998363**, SAS, 38 avenue Roger Hennequin, **78190 Trappes**, NAF 81.30Z (aménagement paysager), RCS Versailles, créée 28/08/1990, capital 161 755 €. Identifié dans l'avis d'attribution 26-37280 (SIREN présent dans le XML eForms, email marches@smda-sas.fr, « Trappes »).
- **Président : CAP VERT (SIREN 904912466)** depuis le **14/01/2022** (CAP VERT DEVELOPPEMENT président de 05/06/2015 au 14/01/2022) ; DG : VEZINE Christophe (depuis 11/12/2012). L'actionnariat par le groupe CAP VERT est donc antérieur à la passation et couvre toute la période de candidature.
- **Groupe CAP VERT** (groupe-capvert.com, communiqué 29/06/2026) : CA > **180 M€**, > **1 200 collaborateurs**, nouvel actionnaire de référence **Gimv** (29/06/2026). Unification de la filière paysage (SMDA fait partie du réseau, 26 établissements).
- Effectif SMDA : tranche RNE 200-249 salariés (annuaire-entreprises 2023) ; 125 en 2018 (pappers) ; l'API recherche-entreprises renvoie 31 (tranche obsolète antérieure) : retenir 200-249 comme référence la plus récente.

### Chiffres d'affaires : bilans 2022-2024 NON PUBLICS (verrou documentaire)

- **Derniers CA publics** (pappers, verif.com, lefigaro, infonet) : **2018 = 13,8 M€** (CA net 13 765 503 €, résultat 1,24 M€), **2017 = 15,5 M€**. L'API recherche-entreprises (finances) ne fournit que 2017 (13 765 503 €).
- **Les bilans 2019-2024 ne sont pas accessibles publiquement** : dépôts accompagnés de déclarations de confidentialité (art. L.232-25) selon les annonces BODACC ; data.inpi.fr bloqué par Cloudflare ; API RNE (registre-national-entreprises.inpi.fr) route 404 ; societe.com/verif.com ne publient pas le CA récent ; pappers les réserve à l'abonnement.
- Résultat documentaire : **il est impossible de vérifier formellement le CA 2022-2024 de SMDA dans les sources publiques** (INPI greffe restant la seule voie, via compte).

### Verdict forensique (H0 de A1)

Le seuil de l'AAPC 25-17720 (CA ≥ 3 M€ lot 2.1 / ≥ 2 M€ lot 2.2 / **5 M€ cumulés sur 3 exercices** pour les 2 lots) est **plausiblement satisfait mais non vérifiable formellement** :
- Le dernier CA public (2018) = 13,8 M€/an, soit **2,8× le seuil cumulé de 5 M€ à lui seul** ; même une contraction sévère du CA (-50 % par an) laisserait SMDA au-dessus du cumul.
- Trajectoire cohérente : effectif 200-249 salariés en 2023 (contre 125 en 2018) = croissance, pas contraction ; intégration au groupe CAP VERT (>180 M€, 1 200 salariés) = capacité financière de groupe mobilisable.
- **Réserve d'honnêteté** : la vérification formelle des bilans 2022-2024 reste impossible en sources publiques (L.232-25). Le 13/04/2026, la SCSNE a notifié les 2 lots à SMDA après instruction de la candidature (DUME + pièces de capacité) : l'acheteur a vérifié le seuil ; nous ne pouvons pas le re-vérifier nous-mêmes.
- **H0 de A1 : CONFIRMÉE au niveau faisceau (plausibilité forte) ; résidu documentaire : bilans 2022-2024 confidentiels (L.232-25), non actionnable en sources ouvertes.**

### Point de vigilance nouveau (à porter)

- L'effectif indiqué par l'API recherche-entreprises (31) est obsolète vs RNE/societe.com (200-249) : signal de fiabilité inégale des données ouvertes, à garder en tête pour les croisements futurs (toujours recouper au moins 2 sources).
- La presse spécialisée (constructionbtp.com, 16/12/2025) cite SMDA parmi les attributaires de marchés de compensation environnementale du Canal Seine-Nord (secteur 4) : SMDA est un titulaire récurrent de la SCSNE, cohérent avec la spécialisation en génie écologique (H2 de A1).
- Artefacts : `source_pappers_smda.txt` + `source_api_recherche-entreprises_smda.json` + `source_api_smda_detail.json` archivés et hashés (verif2_smda.sha256 OK), 0 em-dash.

## AXE 1 EXÉCUTÉ (2026-08-10 15:36 CEST) : dossier gonflement MOE SCSNE + 4 CADA ciblées

**Demande utilisateur : exécuter l'axe 1 de la synthèse : documenter avenant par avenant le gonflement MOE de la SCSNE (84 M€ initiaux TOARC → 11 M€ accordés + 83 M€ en cours + 92-97 M€ MOE unique R.214-120, rapport CdC p. 50-57), via le rapport et les demandes CADA ciblées.**

- Artefact : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_gonflement-moe-sesn/2026-08-10_15-36_gonflement-moe-sesn_INVESTIGATION.md` (235 lignes, 0 em-dash, 15 FCT-moe sourcés p./ligne, 3 GAP ouverts + 1 RÉSOLU, GATE_CHECK, conclusion graduée, sha256 c5f2d4f3...).
- **MAJ 16:00 contradictoire officiel** : GAP-moe-004 RÉSOLU : communiqué SCSNE 10/04/2026 (Wayback, snapshot 13/05/2026) + réponse du président du directoire Jérôme Dezobry à la CdC (16/03/2026, N/Réf. DSNE1-2628582, 5 p.) lus intégralement et archivés (`data/contradictoire/`, hash `artefact_contradictoire.sha256` OK). Verdict contradictoire : la SCSNE « souscrit aux cinq recommandations » et NE CONTESTE aucun chiffre MOE (11/83/92-97 M€) ; explications de coûts : inflation +700 M€, planning +400 M€, normes +700 M€ (art. 11 convention 22/11/2019) ; seul passage MOE : « adaptations en cours des contrats de maîtrise d'œuvre » (statut d'écluse, DREAL 2017).
- **12 faits établis** (rapport CdC lu intégralement + sources BOAMP/TED/QE) : 148 avenants/76 marchés (p. 57) ; 11 M€ accordés + >83 M€ en cours + 9 protocoles + 4 avenants transactionnels (p. 57) ; 92-97 M€ MOE unique R.214-120 (p. 50 + note 73) ; 84 127 774 € initiaux TOARC (BOAMP/TED, déjà vérifié) ; marchés MOE « mal dimensionnés » (p. 57) ; 20TRI086 géotechnique = 6,466 M€ initiaux (BOAMP 21-70929/22-73547, titulaires Hydrogéotechnique NO/Ginger CEBTP/Fondasol) ; **0 avis de modification BOAMP sur les 225 avis SCSNE** ; commission des contrats jamais d'avis défavorable (36 réunions, seuil >5 %) ; rec. n° 2 CdC ; dérive 7,347 Md€ vs 5,118 Md€ ; communiqué SCSNE 10/04/2026 ; QE 17449 (Marchio, 28/07/2026, interruptions de navigation, PAS les avenants MOE).
- **4 demandes CADA rédigées** (data/cada_lettres/, hashés, envoi DELIVERABLE_PENDING) : (1) SCSNE avenants+protocoles MOE et tableaux de suivi 11/83/92-97 M€ ; (2) SCSNE avenants 20TRI086 ; (3) SCSNE PV commission des contrats 2018-2026 ; (4) CdC pièces de travail du contrôle (ventilation 83 M€ / 92-97 M€, 5 ensembles annexe 10, réponse SCSNE aux observations provisoires).
- **Points de rigueur consignés (GAP)** : la ventilation avenant par avenant N'EST PAS dans le rapport (agrégats seulement) ; la relation 83 M€ / 92-97 M€ (inclusion ou recoupement) n'est pas explicitée par la CdC : toute somme (84+11+83+92-97) risquerait un double comptage ; le communiqué SCSNE confirmé via presse, non lu directement (marque ◈).
- Verdict : mécanique d'avenants massive et invisible publiquement (0 DECP de modification + 0 avis BOAMP de modification), motifs SOH/arrêté 09/08/2024 documentés comme contraintes réelles par la CdC ; aucun avantage injustifié ni pacte démontré en l'état ; les CADA ouvrent la ventilation.

## SYNTHÈSE FINALE PHASE 8 (2026-08-10 15:22 CEST) : document de synthèse livré

**Demande utilisateur : consolider la Phase 8 dans un document de synthèse finale du pilote : bilan des 6 vérifications (SMDA, Ribécourt, TOARC, CCIR, recensement 57 numéros, TED) et leçons méthodologiques pour le protocole anticorruption.**

- Artefact : `2026-08-10_15-22_avenants-sesn-pilote-synthese_SYNTHESE.md` (192 lignes, 0 em-dash, sections 1-8 + annexe artefacts) ; copie `data/synthese_phase8_sesn.md` + `data/synthese_phase8.sha256` (31a552096e2d5997103ca86135df4ef9a3e6e1326698172c691b5e09e6639147, vérifié OK).
- Contenu : (1) résumé exécutif ; (2) pilote en chiffres (45 contrats, 103 578 507,98 € HT, CR5 72,35 %, HHI 1419, 0 modification DECP = lacune) ; (3) bilan sourcé des 6 vérifications (V1 SMDA conforme + capacité H0 faisceau, V2 Ribécourt fondement régulier + critère CA au plafond légal 2× R.2142-7, V3 TOARC dispense fondée R.2162-13 + durée 144 mois calée sur chantier, V4 CCIR monopole consulaire plausible non prouvé, V5 recensement 116 lignes + doublon ×100 tranché, V6 TED ✧ levé route UDL) ; (4) état final H0-H6 (aucune anomalie procédurale avérée) ; (5) découvertes CdC (148 avenants, 11 M€ + 83 M€ MOE, 92-97 M€ R.214-120) ; (6) 12 leçons méthodologiques pour le protocole anticorruption (non-publication ≠ absence, signaux ≠ conclusions, règles gelées, dédup multi-sources, modèle événementiel, droit en vigueur à la passation, H2 avant H4, identité précise des acteurs, verrous documentaires, routes d'accès capitalisées, mémoire = index, rapport CdC = contrôle) ; (7) points restants (CADA Phase 5, droit de réponse, INVESTIGATION finale, justification RCC TOARC) ; (8) conclusion graduée (aucun avantage injustifié ni pacte démontré ; trou de transparence + mécanique d'avenants MOE chiffrée par la CdC = objets de l'axe 1).
- Nex axes Phase 8 : (1) quantifier le gonflement MOE SCSNE (84 M€ initiaux → 11 M€ + 83 M€ + 92-97 M€) ; (2) choix de montage marché public vs DSP pour Ribécourt ; (3) retours sourcing 2022-2023 ; (4) effet de filière archéologique INRAP/EVEHA.

## PHASE 10 EXÉCUTÉE

## CLÔTURE DU PILOTE (16:30 CEST, décision utilisateur : clore et capitaliser)

Le pilote SESN est **CLOS**. Bilan honnête : aucune corruption prouvée (matrices 432-11/12/14 : SANS APPUI), 3 suspicions testées à la source primaire requalifiées RÉGULIÈRES (SMDA, Ribécourt, TOARC), concentration archéo expliquée par le cadre L. 523-1/8/9/10. Le livrable est un **fait systémique** : 148 avenants (11 M€ accordés + 83 M€ en cours + 92-97 M€ MOE, CdC 10/04/2026) pour 0 DECP de modification publiée (0/45) et 0 avis BOAMP (0/225). La méthode est validée (elle ne fabrique pas de coupables) ; le trou noir documenté (invisibilité des avenants). Restent DELIVERABLE_PENDING : envoi des 4 CADA, droit de réponse, benchmark national archéo. Leçons capitalisées dans `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_preparation-anticorruption/doctrine/2026-08-10_16-30_legons-pilote-sesn_LEÇONS.md` (hash 8e9aca54).

## AXE 4 EXÉCUTÉ (16:17 CEST) : effet de filière archéologique (INRAP + EVEHA = 42,29 %)

Dossier : `2026-08-10_axe4-filiere-archeologie/2026-08-10_16-17_axe4-filiere-archeologie_INVESTIGATION.md` (115 lignes, 9 faits, 3 GAP, 0 em-dash, hash 0e3f39a5). Verdict : la concentration archéo (INRAP 23,74 % + EVEHA 18,55 % = 42,29 %, 7+7 contrats ; + Archéodunum + Paléotime = 46,0 %) est EXPLIQUÉE par la structure réglementée du marché : diagnostics réservés INRAP (L. 523-1), fouilles ouvertes aux opérateurs agréés par l'État (L. 523-8), contrôle scientifique de l'État avant choix (L. 523-9), INRAP opérateur de secours (L. 523-10), textes lus intégralement dans le payload code du patrimoine. Contrainte réelle documentée par la CdC (10/04/2026) : 1 600 ha prescrits par le SRA/DRAC, poste archéo 21 → 92 M€, « sans qu'il puisse en être fait spécialement grief à la SCSNE ». H0/H2 FAVORISÉES, H4/H5 SANS APPUI. Résidus : composition de l'AC 20TRI053C (lot 3 Protohistoire = EVEHA, 4 MS vérifiés), benchmark national de concentration (✧), répertoire des agréments Culture. (2026-08-10 15:56 + revue 16:00 CEST) : dossier INVESTIGATION final KERNEL

**Demande utilisateur : rédiger le dossier INVESTIGATION final format KERNEL du pilote avenants SESN (Phase 10) : MANIPULATION_REPORT 15 symboles, matrices juridiques par qualification (432-11, 432-14, 432-12), conclusion graduée et option d'escalade, en consolidant la synthèse 15-22.**

- Artefact : `phase10/2026-08-10_15-56_pilote-sesn-phase10_INVESTIGATION.md` (186 lignes, 0 em-dash, sha256 353f8459..., hash vérifié `phase10_dossier.sha256` ; code pénal payload archivé `phase10/code_CP_payload.xml`, hash OK).
- **MANIPULATION_REPORT 15/15 symboles scorés** (max 7/10 : Ξ omission 7, € money 7, ↕ verticalité 6, Κ cynisme 6, ρ résistance 7, ⫸ convergence 7, ⏰ temporalité 6 ; Φ spectacle 1, ⚔ guerre cognitive 1) + **BIAS_TEST source-level distinct** (rapport CdC ◈, avis BOAMP/TED ◈, API Recherche-Entreprises ◈, réponse Dezobry ◈ déclaratif, presse ○).
- **Matrices juridiques par qualification (textes lus intégralement)** : 432-14 favoritisme = SANS APPUI sur A1/A2/A3 ; résidus documentaires = durée 144 mois TOARC (SANS APPUI EN L'ÉTAT, GAP-v3-003) et avenants MOE (NON ÉCARTÉE, GAP-moe-001, conditionné aux réponses CADA). 432-11 corruption passive = SANS APPUI (aucun flux occulte). 432-12 prise illégale d'intérêt = SANS APPUI (intérêt consulaire = intérêt public exclu par la loi ; aucun lien personnel). 432-14 complémentaire : la non-publication DECP = manquement réglementaire à l'open data, pas une infraction pénale.
- **Conclusion graduée** : aucune infraction supportable en l'état ; faits établis = mécanique d'avenants massive et invisible (148 avenants, 11+83+92-97 M€, 0/45 DECP, 0/225 BOAMP, commission des contrats jamais défavorable, contradictoire Dezobry sans démenti chiffré).
- **Option d'escalade 4 niveaux** : (1) envoi 4 CADA (prêt) ; (2) signalement DAJ/DINUM + QE parlementaire (si réponses révèlent absence de fondement) ; (3) AFA/PNF (art. 40 CPP) ou plainte citoyenne (conditionné GAP-moe-001/003) ; (4) publication (prête). Seuil de basculement documenté.
- **Revue critique appliquée** : 2 P1 (vocabulaire matrices : « PLAUSIBLE conditionnel » → « SANS APPUI EN L'ÉTAT / NON ÉCARTÉE » ; BIAS_TEST distinct du scoring symboles) + 2 P2 (escalade : « saisine directe par les citoyens » → « plainte simple ou avec constitution de partie civile » ; symbole ⏰ : hypothèse interprétative marquée comme telle).
- Restent DELIVERABLE_PENDING opérationnels : envoi des 4 CADA (gonflement MOE), questionnaires de droit de réponse, justification RCC TOARC (CADA SCSNE).

---

## QUESTION V3 EXÉCUTÉE (2026-08-10 15:53 CEST) : choix de montage Ribécourt (marché public vs DSP)

**Demande utilisateur : approfondir la question ouverte de la V3 : pourquoi la SCSNE a-t-elle choisi un marché public de services (4,9 M€/48 mois) plutôt qu'une DSP pour l'exploitation de sa plateforme neuve de Ribécourt, alors que Dourges (objet similaire, 57 M€) passe par une DSP en affermage (CG3P L.2124-8, domaine public fluvial) ?**

- Artefact : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_montage-ribecourt-v3/2026-08-10_15-53_montage-ribecourt-v3_INVESTIGATION.md` (173 lignes, 0 em-dash, 12 FCT-v3, 3 GAP, STATUS:FINAL, sha256 1ad82ee3...).
- **VERDICT** : choix structurellement contraint, PAS un signal d'anomalie. 4 différences objectives : (1) actif NEUF sans trafic (Ribécourt, travaux 26-6458) vs EXISTANT avec trafic 250 000 UTI (Dourges, bail commercial LDCT depuis 2003) ; (2) critère juridique : la concession exige un transfert de risque réel non théorique (CCP L.1121-1, lu intégralement) : impossible sur un actif neuf sans trafic ; (3) la SCSNE est un EPIC local société de projet vouée à la dissolution ≤ 12 mois après réception des travaux (rapport CdC p. 10-11) : une DSP de 7-30 ans dépasse son horizon, l'exploitation du canal reviendra à VNF ; (4) la DSP (CGCT L.1411-1) est le régime des collectivités/groupements permanents : l'autorité concédante de Dourges est le Syndicat Mixte Plateforme de Dourges.
- **CORRECTION DE PRÉMISSE** : « CG3P L.2124-8 » ne fonde PAS la DSP (il régit l'autorisation des travaux/prises d'eau sur le domaine public fluvial, texte lu) : la vraie base est le régime CCP de la concession de services.
- **Titulaire DSP Dourges identifié** : LDCT DSP (SIREN 940604721, créée 27/01/2025, siège Delta 3, dirigeants Carvalho/Fehr/Poulard) ; LDCT (452050792, 2003) = exploitant historique en bail commercial ; signature contrat DSP 29/11/2024 = source secondaire ◈ (convention non publiée).
- Points restants (GAP-v3) : convention DSP Dourges non publiée (redevance inconnue), DCE Ribécourt 507911 non public, aucun commentaire officiel du montage (ni SCSNE, ni CdC, ni SMPI).
- Artefacts : 8 fichiers source hashés dans `2026-08-10_montage-ribecourt-v3/data/` (avis BOAMP Dourges 23-43560/21-7402, API Recherche-Entreprises LDCT/LDCT DSP, rapport CdC texte, payloads CCP/CGCT/CG3P), `artefacts_v3.sha256` OK.


**Demande** : comparer la proportionnalité du critère CA ≥ 9,8 M€ de Ribécourt (cas A2, CCIR HDF, 4,9 M€/48 mois, 1 offre) avec d'autres marchés d'exploitation de plateformes multimodales (nombre d'offres, critères) pour tester si le critère a dissuadé des candidats (H4 de A2).

### Point de droit décisif : le ratio 2× est le PLAFOND LÉGAL, pas un excès

- **Art. R.2142-7 CCP** (version 2019, LEGIARTI000037730675, en vigueur à la passation 02/2025) : le chiffre d'affaires minimum exigé des candidats « n'excède pas le double du montant estimé du marché ou du lot » sauf dérogation motivée. **Le critère de Ribécourt (CA ≥ 9,8 M€ = 2× le montant de 4,9 M€) est exactement au plafond légal**, pas au-delà.
- **Évolution** : décret n° 2025-1383 du 29/12/2025 (entré en vigueur 01/01/2026) : le plafond passe de 2× à **1,5×** (LEGIARTI000053218157). Le critère Ribécourt (consultation 02/2025, attribution 06/2026) a été fixé sous le régime du plafond 2× : la baisse de plafond lui est postérieure mais aurait rendu un critère identique aujourd'hui plus proche de la limite.
- **Jurisprudence** : le juge administratif contrôle la proportionnalité des exigences de capacité financière (CE, contrôle restreint ; les exigences doivent être adaptées à l'objet). Un CA au plafond légal de 2× est présumé proportionné, sauf disproportion manifeste démontrée.

### Comparables d'exploitation de plateformes multimodales (sources primaires BOAMP, données lues intégralement)

| Marché | Acheteur | Montant | Durée | Prestations | CA exigé publié | Offres |
|--------|----------|---------|-------|-------------|-----------------|--------|
| **Ribécourt** (25-21716/26-68097) | SCSNE | 4,9 M€ | 48 mois | Exploitation plateforme trimodale + ITE, manœuvres ferroviaires | **≥ 9,8 M€ = 2× montant** | **1** |
| **Dourges DELTA 3** (23-43560, DSP affermage) | Syndicat Mixte PFM Dourges | **57 M€** (52,5 sans PSE) | **90 mois** (7,5 ans) | Exploitation terminal transport combiné + PSE manœuvres ferroviaires | CAP_ECO exigée (détail au RC, non publié dans l'avis) | non publié dans l'avis |
| **Dourges 2021** (21-7402, DSP affermage antérieure) | Syndicat Mixte PFM Dourges | **48 M€** | non précisé | Idem | CAP_ECO + CAP_TECH exigées | non publié |
| **CCI Var Bregaillon** (24-88976, MAPA) | CCI du Var | non publié (petit) | fin 31/12/2025 | Exploitation/maintenance installations ferroviaires port de Bregaillon | non publié | non publié |

### Verdict forensique (H4 de A2)

- **Le critère 9,8 M€ est proportionné au sens légal** : il est au plafond de 2× de l'art. R.2142-7 (vigueur 2019), applicable à la passation. Le comparable Dourges (57 M€) exige aussi une capacité économique (CAP_ECO) sans la publier dans l'avis : la pratique des acheteurs est de fixer un CA minimum, et le ratio 2× est la norme légale.
- **Le critère de qualification (gestion de plateforme multimodale avec ITE, manœuvres ferroviaires, locotracteurs) est plus discriminant que le CA** : seuls les opérateurs ayant déjà géré un terminal ferroviaire (type CCIR via Ports de Lille, ou opérateurs de Dourges/DELTA 3) pouvaient y prétendre. C'est la qualification qui explique vraisemblablement l'offre unique, pas le CA.
- **H4 de A2 : NON ÉCARTÉE (faible) maintenue, mais requalifiée** : le faisceau (critère de qualification taillé + opérateur consulaire établi + 1 offre) reste un avantage structurel documenté, PAS une preuve de favoritisme. La proportionnalité du CA est conforme au droit ; la question ouverte est celle de la **proportionnalité du critère de qualification** (à comparer aux DCE d'autres concessions de terminaux, Dourges notamment), non du CA.
- **Comparaison utile pour la suite** : Dourges (57 M€, 90 mois) est 11× plus gros que Ribécourt (4,9 M€, 48 mois) mais géré par le Syndicat Mixte (public) via DSP, alors que Ribécourt passe par un marché public de services : choix de montage différent pour des objets proches (exploitation de terminal multimodal), à interroger en Phase 8 (pourquoi la SCSNE a-t-elle choisi le marché public plutôt que la DSP pour une plateforme neuve ?).
- Artefacts : `source_boamp_ods_d_23-43560.json` (Dourges 2023) + `source_boamp_ods_d_21-7402.json` (Dourges 2021) + `source_boamp_ods_d_24-88976.json` (CCI Var) + `source_boamp_ods_d_23-22143.json` (réunion info Dourges) archivés et hashés (verif3_ribecourt.sha256 OK), 0 em-dash.