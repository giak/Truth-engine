# Quintessence : Le référentiel CASD : la source DMTG (2010) accessible aux chercheurs, la BNDP absente du canal public

Source : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_casd-referentiel-dmtg-bndp/2026-08-10_09-15_casd-referentiel-dmtg-bndp_INVESTIGATION.md` (55 lignes, 11 FCT-001..011)
Date extraction : 2026-08-13 05:00 CEST
Pilote : Buffy (FreeBuff) : Sublimator v36 Phase 1 (corpus complet, lot bloc DMTG/BNDP/CDC)

---

## 1. Métadonnées & trace source

- **Autorité** : KERNEL v2.8, format léger, axe anticorruption, bloc connaissance patrimoniale (DMTG/BNDP)
- **Date source** : 2026-08-10 09:15 CEST, STATE FINAL
- **Identifiants source** : 11 FCT-001..011
- **Object** : vérifier si la BNDP ou les données de transmissions DGFiP figurent au référentiel CASD : canal public (CASD + CSS) ou canal discret (habilitation directe)
- **Verdict source** : le canal public existe pour l'échantillon DMTG ancien (dernier millésime 2010) ; la BNDP exhaustive reste hors référentiel et confinée

## 2. Faits atomiques préservés

- FCT-001 : la BNDP n'a pas été identifiée sous cette dénomination dans le référentiel CDAP/CASD : grep BNDP/« base nationale des données patrimoniales »/patrimoniales = 0 occurrence (constat d'absence borné) [L45 (mesuré)]
- FCT-002 : la source « DMTG : Enquête Droits de Mutations à Titre Gratuit » figure au référentiel CASD : millésimes 2010, 2006, 1994, 12 projets, 5 publications, thème Finances publiques [L46 (mesuré)]
- FCT-003 : la source DMTG est un échantillon de successions ayant payé des DMTG : données de l'application MOOREA « exhaustives mais incomplètes », complétées par les dossiers papier [L47 (mesuré)]
- FCT-004 : le produit DMTG 2010 est disponible au CASD avec DOI (10.34724/CASD.106.881.V1), mise à disposition 26/02/2015, fichier « Successions 2010 chercheurs » [L48 (mesuré)]
- FCT-005 : 12 projets ont utilisé la source DMTG au CASD, dont un projet de la Direction générale du Trésor (id=464), le CAE (id=816), France Stratégie (id=1041), « Taxation optimale du capital et de l'héritage » (id=254), micro-simulation INES (id=673), la DMD de la Cour des comptes (id=930) [L49 (mesuré)]
- FCT-006 : la DMD = Direction des Méthodes et des Données de la Cour des comptes : la Cour elle-même a un projet CASD utilisant la source DMTG (id=930, ~75 membres) [L50 (mesuré)]
- FCT-007 : le canal public existe donc pour les données DMTG : CDAP + Comité du secret statistique, c'est le canal standard documenté [L51 (mesuré)]
- FCT-008 : MAIS le dernier millésime DMTG accessible est 2010 : identique au constat du corpus (dernière enquête DMTG 2010, jamais mise à jour, QE 11677, Sénat 760) [L52 (mesuré)]
- FCT-009 : la distinction BNDP vs DMTG est décisive : la BNDP (base exhaustive de gestion, 2005-, codes 787B/C) n'est PAS au CASD ; la source DMTG (échantillon, dernier millésime 2010) Y est [L53 (mesuré)]
- FCT-010 : paradoxe : la source DMTG 2010 est accessible aux chercheurs aujourd'hui, mais le module statistique pour produire un millésime 2021+ n'est pas financé : l'accès existe, la production de données récentes non [L54 (mesuré)]
- FCT-011 : le catalogue CASD liste des centaines de sources fiscales DGFiP (POTE, FELIN, ISF-IFI, BIC-RN/RS, ISGROUPE, CBCR, DMTG, DMTO_Fidji, Foncier_bati...) : les données successorales/patrimoniales sont intégrées à l'infrastructure publique de recherche, hors BNDP [L55 (mesuré)]

## 3. Acteurs nominaux

**Institutions** : CASD, CDAP, Comité du secret statistique, DGFiP, Direction générale du Trésor (id=464), CAE, France Stratégie, DMD Cour des comptes (id=930), INES.

## 4. Sources externes citées

cdap.casd.eu/referentiel, casd.eu/donnees-utilisees-sur-le-casd, fiche source DMTG, fiche produit DMTG 2010 (id_prd=881), projet DMD id=930, corpus (QE 11677, Sénat 760, dossier 07-46, 09-11).

## 5. Chronologie datée

26/02/2015 : mise à disposition du produit DMTG 2010 (DOI) ; 2010 : dernier millésime ; 2005 : création BNDP ; 18/11/2025 : rapport Dutreil (exploitation BNDP) ; 10/08/2026 : vérification référentiel.

## 6. Mécanismes / chaînes causales

**M1  :  La ville à deux quartiers** : le quartier public (CASD/CSS) distribue l'échantillon DMTG 2010 à 8-12 projets habilités ; le quartier discret (habilitation directe DGFiP → CdC) distribue la base exhaustive et les transmissions 2005-2024, à la seule Cour. Force : EXTRÊME. Niveau : L2. [L45-L50 (mesuré)]
**M2  :  Le paradoxe accès/production** : l'accès aux chercheurs existe (DOI, CDAP, CSS) depuis 2015 ; ce qui manque est la production d'un nouveau millésime (module statistique « quelques dizaines de M€ » jamais financé). Force : HAUTE. Niveau : L2. [L52-L54 (mesuré)]
**M3  :  Le déplacement du manque** : le « manque de données » n'est ni l'infrastructure ni le canal ni la volonté de les utiliser : c'est la production. Force : HAUTE. Niveau : L2. [L54 (mesuré)]

## 7. Verbatim et citations

- « La France a un canal public de distribution des données successorales aux chercheurs, et il ne distribue que des données de 2010 » [L57 (mesuré)]
- « Le système a la capacité de distribuer la connaissance patrimoniale ; il ne la produit pas : le constat est documenté, la cause (décision ou défaut) ne l'est pas » [L58 (mesuré)]

## 8. Notes méthodologiques source

- **Fiabilité** : sources primaires CASD/CDAP lues via jina ; constat d'absence BNDP borné (dénomination exacte) ; FCT-006/008/010 marqués faisceau ou constat.
- **F-##** : 11/11 identifiants FCT-001..011 préservés verbatim.
- **Méthode** : deux objets vérifiés séparément (BNDP vs DMTG), bias test 4/75, croisement corpus (QE 11677, Sénat 760).

## 9. Limites connues (case-limites)

- La lecture via jina n'a pas exploré interactivement le référentiel (~2000 sources) : la liste des 56 sources du thème Finances publiques a été vue.
- Le grep « BNDP » = 0 est fiable pour la dénomination exacte ; une source équivalente sous un autre nom (ENR, enregistrement, successions) n'a pas été exhaustivement cherchée.
- La fiche produit DMTG 2010 ne détaille pas les variables (page annoncée non extraite).
- La date et la finalité exactes du projet DMD (id=930) n'ont pas été vérifiées au-delà de l'intitulé.
- La taille de l'échantillon DMTG n'est pas documentée ici.
