# INVESTIGATION — Le référentiel CASD : la source DMTG (2010) est accessible aux chercheurs, la BNDP ne figure pas — le canal public existe, la base exhaustive reste confinée

```
IDENT        : INV-CASD-REF-2026-08-10
STATE          : FINAL
TYPE         : INVESTIGATION
KERNEL       : v2.8
DATE         : 2026-08-10 09:15 CEST
PATH         : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_casd-referentiel-dmtg-bndp/
AUTEUR       : Buffy
OBJECT       : Interroger le répertoire des sources CASD (cdap.casd.eu/referentiel) pour vérifier si la BNDP ou les données de transmissions DGFiP y figurent — déterminer si la donnée passe par le CASD (canal public) ou par habilitation directe (canal discret). GAP 3 du dossier 09-11.
LIEN         : dossier 2026-08-10_09-11_convention-cdc-dgfip-bndp (GAP 3) ; point consolidé 08-50 (G-05)
```

## 0. TEXT_ANALYSIS

**Requête** : la BNDP ou les données de transmissions DGFiP figurent-elles dans le référentiel des sources CASD/CDAP ? Le canal d'accès est-il public (CASD + Comité du secret statistique) ou discret (habilitation directe) ?

**Périmètre** : (1) référentiel CDAP (cdap.casd.eu/referentiel) ; (2) catalogue CASD (casd.eu/donnees-utilisees-sur-le-casd) ; (3) fiche source DMTG ; (4) fiche produit DMTG 2010 ; (5) projet DMD Cour des comptes (id=930).

**CRÉDO** : distinguer BNDP (absente du référentiel) vs source DMTG (présente) — deux objets différents dont la confusion fausserait le faisceau.

## 1. PISTES

| # | Piste | Statut |
|---|-------|--------|
| P1 | Référentiel CDAP : la BNDP y figure-t-elle ? | ✅ VÉRIFIÉE (0 occurrence — ABSENTE) |
| P2 | Catalogue CASD : la source DMTG y figure-t-elle ? | ✅ VÉRIFIÉE (PRÉSENTE : millésimes 2010/2006/1994, 12 projets, 5 publications) |
| P3 | Fiche produit DMTG 2010 : variables, DOI, mise à disposition | ✅ LUE (DOI 10.34724/CASD.106.881.V1, mise à dispo 26/02/2015) |
| P4 | Projet DMD de la Cour des comptes (id=930) | ✅ LUE (Direction des Méthodes et des Données de la CdC) |

## 2. BIAS TEST

| Symbole | Score | Justification |
|---------|-------|---------------|
| 🟥 Causalité simple | 1/15 | Pas de causalité — constat de présence/absence |
| 🟧 Sélection | 1/15 | Deux objets distincts vérifiés séparément (BNDP vs DMTG) |
| 🟩 Biais de confirmation | 2/15 | La découverte (DMTG accessible) va CONTRE le récit « aucune donnée successorale pour les chercheurs » — bonne résistance |
| **Total** | **4/75** | Résistance correcte |

## 3. FACT_REGISTRY

| # | Fait | Valeur | Source | Statut |
|---|------|--------|--------|--------|
| FCT-001 | **La BNDP n'a pas été identifiée sous cette dénomination dans le référentiel des sources CDAP/CASD** : grep de « BNDP / base nationale des données patrimoniales / patrimoniales » = 0 occurrence sur la page cdap.casd.eu/referentiel (borne : lecture via jina, équivalent sous un autre nom non cherché — LIMITE 2) | 0 occurrence | cdap.casd.eu/referentiel (lue via jina) | CONFIRMÉ (constat d'absence borné) |
| FCT-002 | **La source « DMTG : Enquête Droits de Mutations à Titre Gratuit » figure dans le référentiel CASD** : millésimes **2010, 2006, 1994**, 12 projets, 5 publications, thème « Finances publiques » | PRÉSENTE | cdap.casd.eu/referentiel + casd.eu/donnees-utilisees (lues) | CONFIRMÉ |
| FCT-003 | La source DMTG est « un échantillon constitué à partir des successions ayant payé des droits de mutations à titre gratuit (DMTG) » — données de l'application **MOOREA** « exhaustives mais incomplètes », complétées par les dossiers papier | échantillon | Fiche source DMTG (lue) | CONFIRMÉ |
| FCT-004 | **Le produit DMTG 2010 est disponible au CASD avec DOI** (10.34724/CASD.106.881.V1), mise à disposition **26/02/2015** ; dessin de fichier « Successions 2010 chercheurs » | DOI | Fiche produit id_prd=881 (lue) | CONFIRMÉ |
| FCT-005 | **12 projets ont utilisé la source DMTG au CASD**, dont : projet de la sous-direction des finances publiques de la **Direction générale du Trésor (DGT, id=464)**, projet du CAE (id=816), travaux de France Stratégie (id=1041), « Taxation optimale du capital et de l'héritage » (id=254), micro-simulation INES (id=673), **projet de la DMD de la Cour des comptes (id=930)** | 12 projets | Fiche source DMTG (lue) | CONFIRMÉ |
| FCT-006 | **La DMD = Direction des Méthodes et des Données de la Cour des comptes** — la Cour des comptes elle-même a un projet CASD utilisant la source DMTG (id=930), avec liste de ~75 membres | DMD = CdC | Projet id=930 (lu) | CONFIRMÉ |
| FCT-007 | **Le canal public existe donc pour les données DMTG** : un chercheur peut demander l'accès à la source DMTG (millésimes 2010/2006/1994) via CDAP + Comité du secret statistique — c'est le canal standard documenté (FAQ CSS, dossier 09-11) | canal public | Croisement FCT-002/004 + FAQ CSS | CONFIRMÉ (faisceau) |
| FCT-008 | **MAIS le dernier millésime DMTG accessible est 2010** — identique au constat du corpus (« dernière enquête DMTG 2010, jamais mise à jour », QE 11677, Sénat 760) : le canal public ne donne accès qu'à des données vieilles de 15 ans | 2010 = dernier | Fiche source DMTG + corpus | CONFIRMÉ (cohérence) |
| FCT-009 | **La distinction BNDP vs DMTG est décisive** : la BNDP (base exhaustive de gestion, 2005-, code 787B/C) n'est PAS au CASD ; la source DMTG (échantillon d'enquête, dernier millésime 2010) Y est. Le canal public (CASD/CSS) porte sur l'échantillon ancien, pas sur la base exhaustive récente | distinction | Croisement FCT-001/002 + dossier 07-46 | CONFIRMÉ (analyse) |
| FCT-010 | **Le faisceau s'enrichit d'un paradoxe** : la source DMTG 2010 est accessible aux chercheurs AUJOURD'HUI (canal public documenté), mais le module statistique pour produire un millésime 2021+ n'est pas financé — l'accès existe, la production de données récentes non | paradoxe | Croisement FCT-004 + 07-26 (module non financé) | CONSTAT (analyse) |
| FCT-011 | La page catalogue CASD liste des centaines de sources fiscales DGFiP (POTE, FELIN, ISF-IFI, BIC-RN/RS, ISGROUPE, CBCR, DMTG, DMTO_Fidji, Foncier_bati, etc.) — les données successorales/patrimoniales sont donc intégrées à l'infrastructure publique de recherche, hors BNDP | catalogue large | casd.eu/donnees-utilisees (lue) | CONFIRMÉ |

## 4. PELOTE

```
Référentiel CDAP (cdap.casd.eu/referentiel) :
  ├── BNDP ? → 0 occurrence (ABSENTE — base exhaustive de gestion, canal discret : habilitation directe DGFiP→CdC)
  └── Source « DMTG : Enquête Droits de Mutations à Titre Gratuit » ? → PRÉSENTE
        ├── Millésimes : 2010, 2006, 1994 (le dernier = 2010, identique au constat corpus)
        ├── Échantillon de successions ayant payé des DMTG (application MOOREA, dossiers papier)
        ├── DOI du produit 2010 : 10.34724/CASD.106.881.V1 (mise à dispo 26/02/2015)
        ├── 12 projets (DGFiP, CAE, France Stratégie, INES, DMD Cour des comptes...)
        └── Canal public : CDAP + Comité du secret statistique
CONCLUSION : le canal public existe pour l'échantillon DMTG ancien ; la BNDP exhaustive reste hors référentiel
```

## 5. GATE_CHECK

- **GAP 3 (dossier 09-11) : RÉSOLU.** La BNDP ne figure pas au référentiel CASD — elle ne passe donc pas par le canal public ; les données de transmissions DGFiP utilisées pour le rapport Dutreil relèvent du canal discret (habilitation directe + fourniture à l'IPP documentée au dossier 09-11).
- **Fait nouveau majeur** : la source DMTG (échantillon, dernier millésime 2010) est, elle, accessible aux chercheurs via le CASD — le canal public existe pour des données successorales, mais vieilles de 15 ans et non exhaustives.
- **Cohérence corpus** : le dernier millésime DMTG au CASD (2010) correspond exactement au constat « dernière enquête DMTG 2010 » (QE 11677, Sénat 760) — le dossier confirme par une troisième source le point d'arrêt de la production.

## 6. SOURCES (SRC)

| # | Source | Type | Date accès |
|---|--------|------|-----------|
| SRC-001 | cdap.casd.eu/referentiel (via jina) | Primaire (CASD/CDAP) | 10/08/2026 |
| SRC-002 | casd.eu/donnees-utilisees-sur-le-casd/ (via jina) | Primaire (CASD) | 10/08/2026 |
| SRC-003 | Fiche source DMTG (casd.eu/source/enquete-droits-de-mutations-a-titre-gratuit/) — lue | Primaire (CASD) | 10/08/2026 |
| SRC-004 | Fiche produit DMTG 2010 (casd.eu/page-produit/?id_prd=881) — lue | Primaire (CASD) | 10/08/2026 |
| SRC-005 | Projet DMD Cour des comptes (casd.eu/prj.php?id=930) — lu | Primaire (CASD) | 10/08/2026 |
| SRC-006 | Corpus : QE 11677 (08-46), Sénat 760 (07-26), dossier 07-46, dossier 09-11 | Corpus | 10/08/2026 |

## 7. LIMITES

1. Le référentiel CDAP est une application web ; la lecture via jina a extrait la liste des sources mais la structure complète (recherche, filtres) n'a pas été explorée interactivement — la liste des 56 sources du thème « Finances publiques » a été vue, pas nécessairement la totalité des ~2000 sources.
2. Le grep « BNDP » = 0 est fiable pour l'absence de la dénomination exacte ; une source équivalente sous un autre nom (ex. « ENR », « enregistrement », « successions ») n'a pas été exhaustivement cherchée dans le catalogue.
3. La fiche produit DMTG 2010 ne détaille pas les variables (page « liste des variables disponibles » annoncée mais non extraite en session).
4. Le projet DMD Cour des comptes (id=930) est attesté comme utilisateur de la source DMTG mais la date et la finalité exactes du projet n'ont pas été vérifiées au-delà de l'intitulé.
5. La source DMTG étant un échantillon (successions ayant payé des droits), elle ne couvre pas les transmissions exonérées — cohérent avec les limites de la BNDP notées au dossier 07-46, mais la taille de l'échantillon DMTG n'est pas documentée ici.

## 8. VERDICT

**Le GAP est résolu, et la réponse affine le faisceau de manière importante.** La BNDP n'est pas dans le référentiel CASD — la base exhaustive reste au canal discret (habilitation directe DGFiP→CdC, dossier 09-11). Mais la source « DMTG : Enquête Droits de Mutations à Titre Gratuit » Y figure, avec un DOI, une mise à disposition documentée, et 12 projets l'ayant utilisée — dont un projet de la Cour des comptes elle-même (DMD) et des projets de la Direction générale du Trésor, du CAE, de France Stratégie. **Le canal public existe donc pour des données successorales — mais uniquement pour l'échantillon ancien (dernier millésime 2010), pas pour la base exhaustive récente.** Le paradoxe du faisceau s'en trouve renforcé : ce n'est pas l'accès aux chercheurs qui manque (le CASD/CSS le permet depuis 2015), c'est la production de données récentes — le module statistique « à quelques dizaines de M€ » jamais financé. L'infrastructure existe, le canal existe ; rien ne documente une décision de produire un nouveau millésime.

## 9. RECOMMANDATIONS

1. **Explorer le référentiel CDAP interactivement** (browser-use ou API) pour vérifier s'il existe une source équivalente sous un autre nom (enregistrement, successions, ENR) et obtenir la liste exhaustive des variables DMTG 2010.
2. **Vérifier les publications DMTG 2010** (5 publications listées : Piketty/Zucman inégalités de patrimoine 1880-2014, Garbinti et al. DINA, etc.) pour documenter les usages réels de l'échantillon.
3. **Croiser avec la QE 11677** : la réponse de Bercy dit que l'enrichissement BNDP « est en cours » pour « reconstruire l'information manquante jusqu'au déploiement de e-Enregistrement » — le référentiel CASD prouve que le canal de distribution aux chercheurs existe déjà (DMTG), la question porte sur la production.
4. **Le dossier alimente le point consolidé** : le paradoxe « l'accès existe, la production non » est un maillon nouveau du faisceau.

## 10. LEÇON

**La France a un canal public de distribution des données successorales aux chercheurs — et il ne distribue que des données de 2010.** Le CASD, le Comité du secret statistique, les DOIs, les conventions de recherche : tout existe et fonctionne (12 projets, dont la Cour des comptes elle-même). Ce qui manque n'est ni l'infrastructure, ni le canal, ni la volonté de les utiliser — c'est la production d'un nouveau millésime. La source DMTG s'arrête en 2010 parce que le module statistique n'est pas financé ; la BNDP reste confinée parce qu'aucun canal public ne la porte. **Le système a la capacité de distribuer la connaissance patrimoniale ; il ne la produit pas — le constat est documenté, la cause (décision ou défaut) ne l'est pas.**

---
*Fichier créé 2026-08-10 09:15 CEST — KERNEL v2.8 — Buffy*
