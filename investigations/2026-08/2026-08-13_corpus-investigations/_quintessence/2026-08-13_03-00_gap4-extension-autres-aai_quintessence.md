# Quintessence : GAP-vp4-4, extension du test pantouflage aux autres AAI (Arcom, ACPR/BdF, ADLC, CNIL, AMF)

Source : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_run2-enr/2026-08-11_14-52_gap4-extension-autres-aai_INVESTIGATION.md` (110 lignes, 18 FCT-vp44)
Date extraction : 2026-08-13 03:00 CEST
Pilote : Buffy (FreeBuff) : Sublimator v36 Phase 1 (corpus complet, lot run2-enr)

---

## 1. Métadonnées & trace source

- **Autorité** : KERNEL v2.8, format allégé axe piste, fil VP-P4, GAP-vp4-4 du 13-20
- **Date source** : 2026-08-11 14:52 CEST, STATE FINAL
- **Identifiants source** : 18 FCT-vp44-001 à 018
- **Object** : généraliser le constat d'asymétrie de transparence en étendant le test du pattern pantouflage aux autres AAI (Arcom, ACPR/Banque de France, ADLC, CNIL, AMF) via la même table HATVP
- **Verdict source** : le pattern « AAI → secteur privé » est transversal (6 AAI testées) ; l'asymétrie de transparence est systémique ; circuit le plus pertinent pour l'ENR = État/ministères → fonds investissant dans l'énergie (Thodoroff→Ardian, Djebbari→Magellim)

## 2. Faits atomiques préservés

- FCT-vp44-001 : 778 avis HATVP supplémentaires téléchargés à la source primaire (hatvp.fr) le 11/08/2026, 773 textes extraits (5 PDF image) [L73 (mesuré)]
- FCT-vp44-002 : le scan « secteur concurrentiel » (185 avis) est une formule générique du champ 432-13, pas un marqueur ADLC : bruit, non exploitable [L74 (mesuré)]
- FCT-vp44-003 : avis 2025-178 (06/05/2025) : Valérie Bros, membre non permanent du collège de l'ADLC du 18/03/2019 au 10/10/2024, rejoint Burelle SA et Sofiparc : compatibilité avec réserves [L75 (mesuré)]
- FCT-vp44-004 : avis 2024-8 (16/01/2024) : Romain Charvet, agent CRE (chargé de mission puis adjoint au directeur de la communication et des relations institutionnelles, 2020-2022), rejoint Eramet : compatibilité avec réserves (interdiction de démarches CRE jusqu'au 04/07/2025, et auprès de Carenco) [L76 (mesuré)]
- FCT-vp44-005 : avis 2025-A-5 (02/01/2025) : Raphaëlle Epstein-Richard, secrétaire générale de la CRE (17/02/2017-18/02/2022) puis directrice adjointe du cabinet de Carenco (outre-mer), rejoint SNCF Gares & Connexions (directrice de programme) : hors 432-13 (monopole légal) [L77 (mesuré)]
- FCT-vp44-006 : avis 2025-100 (18/03/2025) : Basile Thodoroff, conseiller « entreprises, participations de l'État, industrie et énergie » du cabinet de Bruno Le Maire (2021-2024), rejoint Ardian France : compatibilité avec réserves (pas de démarche DGE/APE jusqu'au 09/09/2027, ni auprès de Le Maire) [L78 (mesuré)]
- FCT-vp44-007 : avis 2023-35 (07/02/2023) : Jean-Baptiste Djebbari, ex-ministre délégué aux transports, rejoint Magellim, fonds d'investissement dans les énergies vertes : compatibilité avec réserves [L79 (mesuré)]
- FCT-vp44-008 : avis 2023-98/2024-22 : Chantal Jouanno, présidente CNDP, rejoint Accenture (conseil puis directrice de comptes clients) : compatibilité avec réserves, interdiction de toute relation directe avec la CNDP pendant 3 ans [L80 (mesuré)]
- FCT-vp44-009 : avis 2026-10 (27/01/2026) : Éric Lombard, DG CDC (2017-2024) et ministre de l'économie (2024-2025), devient président non rémunéré de la SAS Halmahera : compatibilité avec réserves (pas de démarche CDC jusqu'au 22/12/2027) [L81 (mesuré)]
- FCT-vp44-010 : avis 2026-A-72 (31/03/2026) : Édouard Solier, directeur de cabinet du président de l'Arcom (2025-2026), rejoint Horizons : hors 432-13 (parti politique) [L82 (mesuré)]
- FCT-vp44-011 : avis 2020-183 (06/10/2020, anonymisé) : collaborateur du Président et conseiller ministériel (fiscalité, participations publiques) rejoint une société du secteur de l'énergie à monopole légal : hors 432-13, compatibilité avec réserves [L83 (mesuré)]
- FCT-vp44-012 : le profil de 2020-183 (participations publiques + monopole légal énergie) pointe EDF, mais le résumé est anonymisé : identification non confirmée (HYPOTHÈSE) [L84 (mesuré)]
- FCT-vp44-013 : ACPR/BdF : 2 avis à mot-clé (2022-154, 2023-163), tous anonymisés (agents) : aucun cas nominatif exploitable [L85 (mesuré)]
- FCT-vp44-014 : Arcom : seul cas nominatif = Solier vers Horizons ; aucun cas « Arcom → groupe médias » nominatif ; les agents Arcom sont anonymisés comme ceux de la CRE [L86 (mesuré)]
- FCT-vp44-015 : l'asymétrie de transparence (responsables publiés, agents anonymisés) est généralisée aux 6 AAI testées (CRE, Arcom, ACPR/BdF, ADLC, CNIL, AMF), pas propre à la CRE [L87 (mesuré)]
- FCT-vp44-016 : 2 cas de responsables passant vers des fonds investissant dans l'énergie (Ardian, Magellim) : le circuit « État/AAI → fonds d'infrastructure » est contrôlé par réserves, jamais bloqué [L88 (mesuré)]
- FCT-vp44-017 : la HATVP contrôle les personnes, pas l'architecture de la rente OA/CR : aucun avis ne porte sur le design tarifaire (complément du GAP-ll-1) [L89 (mesuré)]
- FCT-vp44-018 : méthode reproductible : téléchargement de masse + pdftotext + scan mots-clés sur les 806 avis HATVP, applicable à toute autre AAI ou filière [L90 (mesuré)]

## 3. Acteurs nominaux

**Personnes** : Valérie Bros (ADLC→Burelle), Romain Charvet (CRE→Eramet), Raphaëlle Epstein-Richard (CRE→SNCF), Basile Thodoroff (Bercy→Ardian), Jean-Baptiste Djebbari (→Magellim), Chantal Jouanno (CNDP→Accenture), Éric Lombard (CDC→Halmahera), Édouard Solier (Arcom→Horizons), Carenco (contexte).
**Entreprises** : Burelle SA, Sofiparc, Eramet, SNCF Gares & Connexions, Ardian France, Magellim, Accenture, Halmahera, Horizons.
**AAI testées** : CRE, Arcom, ACPR/BdF, ADLC, CNIL, AMF.

## 4. Sources externes citées

Moisson HATVP /tmp/vp44_txt (778 avis, 773 textes), table hatvp_delib_v2.json (809 records), PDF 2025-178, 2024-8, 2025-A-5, 2025-100, 2023-35, 2023-98/2024-22, 2026-10, 2026-A-72, 2020-183 lus intégralement.

## 5. Chronologie datée

2019-2024 : Bros au collège ADLC ; 2020-2022 : Charvet agent CRE ; 2021-2024 : Thodoroff conseiller Bercy ; 2023-2026 : avis rendus (2023-35, 2023-98, 2024-8, 2024-22, 2025-A-5, 2025-100, 2025-178, 2026-10, 2026-A-72) ; 11/08/2026 : moisson et scan.

## 6. Mécanismes / chaînes causales

**M1 — L'asymétrie de transparence systémique** : les « responsables » (ministres, membres du collège, présidents d'AAI) sont publiés nominativement, les « agents » anonymisés ; l'inventaire exhaustif des agents CRE/DGEC/Arcom/ADLC vers les opérateurs est impossible en sources ouvertes. Niveau : L2. [L87 (mesuré)]
**M2 — Le circuit État → fonds d'infrastructure (le plus pertinent pour l'ENR)** : les personnes qui ont conçu ou supervisé les politiques et participations de l'État dans l'énergie (Thodoroff Bercy→Ardian, Djebbari→Magellim) rejoignent les fonds qui investissent dans l'énergie, avec des réserves qui encadrent mais n'empêchent pas la mobilité. Niveau : L2. [L78-L79, L88 (mesuré)]
**M3 — La limite de la source** : la HATVP contrôle les personnes, pas l'architecture (GAP-ll-1) : l'asymétrie documentée est un signal de gouvernance (limite du contrôle citoyen), pas un fait de corruption. Niveau : L2. [L89 (mesuré)]

## 7. Verbatim et citations

- Réserve Thodoroff (2025-100) : « pas de démarche auprès de la DGE et de l'APE jusqu'au 09/09/2027, ni auprès de Bruno Le Maire » [L78 (mesuré)]

## 8. Notes méthodologiques source

- **Fiabilité** : 778 avis téléchargés (source primaire), 773 textes extraits, lecture intégrale des avis nominatifs pertinents ; FCT-vp44-012 marquée HYPOTHÈSE.
- **F-##** : 18/18 identifiants FCT-vp44-001 à 018 préservés verbatim.
- **Méthode** : scan par mots-clés AAI sur 3 familles, distinction bruit générique (« secteur concurrentiel ») vs cas réels, lecture intégrale.

## 9. Limites connues (case-limites)

- GAP-vp44-1 : identifier la société de 2020-183 (EDF probable) ; GAP-vp44-2 : lire les 2 avis ACPR/BdF ; GAP-vp44-3 : prestations Ardian Semiconductor depuis 09/2024 (traité au 15-41) ; GAP-vp44-4 : étendre aux AAI de contrôle (Arcom) et santé (ANSM) ; GAP-vp44-5 : croiser les 806 avis avec les déclarations d'intérêts (circuits indirects type JFC2/Samfi).
- 0 fait d'infraction : le faisceau établit une asymétrie structurelle de contrôle, pas un comportement illégal.
