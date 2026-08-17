# Quintessence : Choix de montage Ribécourt : marché public de services vs DSP (question V3 de la synthèse pilote)

Source : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_montage-ribecourt-v3/2026-08-10_15-53_montage-ribecourt-v3_INVESTIGATION.md` (151 lignes, 12 FCT-v3-001..012)
Date extraction : 2026-08-13 05:00 CEST
Pilote : Buffy (FreeBuff) : Sublimator v36 Phase 1 (corpus complet, lot bloc DMTG/BNDP/CDC)

---

## 1. Métadonnées & trace source

- **Autorité** : KERNEL v2.8, format léger, axe anticorruption, bloc commande publique / SCSNE
- **Date source** : 2026-08-10 15:53 CEST, STATE FINAL
- **Identifiants source** : 12 FCT-v3-001..012
- **Object** : pourquoi la SCSNE a choisi un marché public de services (4,9 M€/48 mois) plutôt qu'une DSP pour l'exploitation de la plateforme neuve de Ribécourt, alors que le TTC de Dourges (57 M€) passe par une DSP en affermage
- **Verdict source** : le choix est structurellement contraint et cohérent avec le droit : aucune anomalie, la prémisse « CG3P L.2124-8 » est corrigée

## 2. Faits atomiques préservés

- FCT-v3-001 : la plateforme de Ribécourt est une infrastructure NEUVE, en construction 2026 (marché de travaux SCSNE 26-6458, AAPC 19/01/2026, CPV 45213350, ITE sur le canal latéral à l'Oise) ; le marché d'exploitation (12/06/2026) intervient AVANT la fin des travaux [L20 (mesuré)]
- FCT-v3-002 : le TTC de Dourges existe et a un trafic établi (250 000 UTI de capacité) ; le terminal est exploité par une société commerciale dans le cadre d'un bail commercial (avis DSP 23-43560, 24/04/2023) [L24 (mesuré)]
- FCT-v3-003 : la DSP de Dourges 2023 transfère le risque d'exploitation au délégataire : affermage, « exploitation aux risques et périls du délégataire », redevance au concédant, 57 M€ avec PSE (52,5 M€ sans), durée 90 mois, 3,6 M€ d'investissements du délégataire [L28 (mesuré)]
- FCT-v3-004 : le titulaire de la DSP Dourges est LDCT DSP (SIREN 940604721), véhicule créé ad hoc le 27/01/2025 (dirigeants : Jose Carlos Carvalho, Patrick Fehr, Benjamin Poulard) ; LDCT (452050792) est l'exploitant historique du terminal ; signature du contrat ~29/11/2024 (source secondaire ◈) [L32 (mesuré)]
- FCT-v3-005 : la SCSNE est un EPIC local, société de projet vouée à disparaître au plus tard 12 mois après la réception des travaux (ordonnance 2016-489, loi LOM art. 134) ; mise en service annoncée 2032 (rapport CdC 10/04/2026, p. 10-11) [L36 (mesuré)]
- FCT-v3-006 : à l'issue du chantier, l'exploitation revient à VNF, opérateur du domaine public fluvial (L.2111-10 CG3P) [L40 (mesuré)]
- FCT-v3-007 : les 4 ports intérieurs du canal sont pilotés par le SMPI (317 M€), Ribécourt en est hors périmètre : montage direct SCSNE [L44 (mesuré)]
- FCT-v3-008 : le critère juridique de la concession est le transfert du risque d'exploitation, réel et non théorique (CCP L.1121-1) [L48 (mesuré)]
- FCT-v3-009 : la DSP est une concession de services réservée aux collectivités, groupements et établissements publics locaux (CGCT L.1411-1 + CCP L.1121-3) [L52 (mesuré)]
- FCT-v3-010 : L.2124-8 CG3P ne fonde PAS la DSP : il porte sur les travaux sur le domaine public fluvial : correction de prémisse de la question V3 [L56 (mesuré)]
- FCT-v3-011 : le marché de Ribécourt est un accord-cadre de services rémunéré par l'acheteur (pas de transfert de risque) : AAPC 25-21716 (25/02/2025), attribution 26-68097 (12/06/2026), 4,9 M€ HT/48 mois, 1 offre, CCIR HDF [L60 (mesuré)]
- FCT-v3-012 : le rapport CdC ne recommande pas un montage particulier pour les plateformes/ports : aucun commentaire sur le montage Ribécourt (GAP) [L64 (mesuré)]

## 3. Acteurs nominaux

**Institutions** : SCSNE (EPIC local, maître d'ouvrage du canal), VNF (exploitant futur), SMPI (4 ports intérieurs), Syndicat Mixte Plateforme de Dourges (concédant), CCIR HDF (titulaire Ribécourt), LDCT DSP / LDCT (Dourges), Cour des comptes (rapport 10/04/2026), région HdF + 4 départements.

## 4. Sources externes citées

Avis BOAMP 26-6458/26-17661, 23-43560, 21-7402, 25-21716, 26-68097 (JSON archivés), API Recherche-Entreprises (LDCT, LDCT DSP), rapport CdC 10/04/2026, payloads codes.droit.org (CCP, CGCT, CG3P).

## 5. Chronologie datée

05/12/2003 : création LDCT ; 21/04/2016 : ordonnance créant la SCSNE ; 24/12/2019 : loi LOM (SCSNE EPIC local) ; 21/01/2021 : 1re procédure DSP Dourges sans suite ; 24/04/2023 : avis DSP 23-43560 ; 11/08/2023 : comité du SMPI ; 29/11/2024 : signature DSP Dourges (◈) ; 19/01/2025 : AAPC travaux Ribécourt ; 27/01/2025 : création LDCT DSP ; 25/02/2025 : AAPC exploitation Ribécourt ; 12/06/2026 : attribution à la CCIR ; 22/07/2026 : accord-cadre desserte ferroviaire ; 2032 : mise en service, dissolution SCSNE.

## 6. Mécanismes / chaînes causales

**M1  :  La contrainte institutionnelle** : société de projet à durée bornée (dissolution ≤ 12 mois après réception) : une DSP de 7-30 ans dépasse son horizon ; un marché de 48 mois s'y inscrit. Force : EXTRÊME. Niveau : L1. [L36, L40 (mesuré)]
**M2  :  La contrainte du transfert de risque** : sur un actif NEUF sans trafic établi (Ribécourt en construction), aucun opérateur ne porte le risque d'exploitation : une DSP serait sans candidat ou requalifiable en marché public par le juge ; le marché de services (rémunération par l'acheteur) est l'instrument adapté. Force : EXTRÊME. Niveau : L1. [L48, L60 (mesuré)]
**M3  :  La contrainte organique** : la DSP CGCT est réservée aux collectivités/EP locaux ; l'autorité concédante de Dourges est un syndicat mixte permanent avec un actif productif et un opérateur en place : toutes les conditions de l'affermage sont réunies. Force : HAUTE. Niveau : L1. [L52, L56 (mesuré)]
**M4  :  La correction de prémisse** : « CG3P L.2124-8 » (question V3) régit les travaux sur le domaine public fluvial, pas le montage d'exploitation : la vraie comparaison porte sur le régime CCP (marché vs concession). Force : EXTRÊME. Niveau : L1. [L56 (mesuré)]

## 7. Verbatim et citations

- « Le choix du marché public de services à Ribécourt est structurellement contraint et cohérent avec le droit ; il ne constitue pas un signal d'anomalie » [L72 (mesuré)]
- « La concurrence faible (1 offre) s'explique par l'unicité technique et l'avantage structurel de la CCIR : avantage, pas favoritisme » [L93 (mesuré)]

## 8. Notes méthodologiques source

- **Fiabilité** : 12 faits tous sourcés (avis BOAMP lus intégralement, API Recherche-Entreprises, rapport CdC, codes à la source primaire) ; signature DSP 29/11/2024 marquée source secondaire ◈.
- **F-##** : 12/12 identifiants FCT-v3-001..012 préservés verbatim.
- **Méthode** : gate_check complet (0 em-dash, aucun chiffre inventé, aucune URL générique, réserves documentées GAP-v3-001..003), verdict gradué.

## 9. Limites connues (case-limites)

- La convention de DSP de Dourges n'est pas publiée (redevance, clauses exactes) : GAP-v3-001.
- Le DCE de la procédure B119 de Ribécourt n'est pas public : GAP-v3-002.
- Aucun commentaire officiel du choix de montage (SCSNE, CdC, SMPI) : la réponse est une déduction juridique, pas une déclaration : GAP-v3-003.
