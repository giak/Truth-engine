# Quintessence : P3, croisement tarifs des appels d'offres PPE2 vs coûts, chiffrage des sur-rémunérations potentielles

Source : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_run2-enr/2026-08-10_17-33_surremunerations-enr-croisement_INVESTIGATION.md` (53 lignes, 0 identifiant FCT : fichier de croisement/calcul, traité en note)
Date extraction : 2026-08-13 03:00 CEST
Pilote : Buffy (FreeBuff) : Sublimator v36 Phase 1 (corpus complet, lot run2-enr)

---

## 1. Métadonnées & trace source

- **Autorité** : KERNEL v2.8, volet restant de P3 du run2-enr (trou de contrôle CdC : sur-rémunérations potentielles des filières ENR soutenues)
- **Date source** : 2026-08-10 17:33 CEST, STATE FINAL
- **Identifiants source** : aucun FCT (fichier de travail, calculs LCOE)
- **Object** : sur-rémunération potentielle = tarif garanti (CR, AO PPE2) − coût complet de production estimé (LCOE) − rémunération normale du capital ; calcul sur LCOE reconstitués à partir des CAPEX publics du rapport CRE PPE2
- **Verdict source** : AUCUNE sur-rémunération avérée chiffrable aux données publiques sur les AO PPE2 (écarts 0 à 15 €/MWh selon hypothèses) ; les sur-rémunérations avérées relèvent des guichets ouverts (PV 2006-2010 « notoirement surévalué ») et de l'indexation automatique (rec. n°3 CdC) ; le trou de contrôle est confirmé (collecte des coûts jugée « trop lourde » par la CRE)

## 2. Faits atomiques préservés (extraction du croisement)

- Tarif AO PPE2 moyen (dernières périodes) : éolien terrestre 86,62 €/MWh, PV au sol 74,13 €/MWh, PV bâtiment 96,48 €/MWh (CRE PPE2, communiqué 18/02/2026) [L8 (mesuré)]
- CAPEX : éolien ~1 750 €/kW (bas 1 600 €/kW 11/2021, haut 2 100 €/kW 12/2022), PV sol ~900 €/kWc, PV bâtiment ~1 150 €/kWc (CRE PPE2, l.824-828 et 851-869) [L9 (mesuré)]
- Heures équivalent pleine puissance : éolien ~2 400 (HDF 2 483, NA 2 355, Occitanie 2 630), PV sol ~1 400, PV bâtiment ~1 100 (hypothèses marquées) [L10 (mesuré)]
- Volume retenu cumulé (fin 2021-30/06/2025) : 18,2 GW cumulés, 2 074 projets (répartition par filière non sourcée : tableaux en images) [L12 (mesuré)]
- LCOE reconstitué (WACC nominal 7 %, durée 25 ans, CRF 0,085) : éolien ~77 €/MWh (fourchette 70-85), PV sol ~64 €/MWh (55-70), PV bâtiment ~97 €/MWh (85-105) [L19 (mesuré)]
- Écart tarif − LCOE : éolien +1 à +17 €/MWh (médiane ~10), PV sol +4 à +19 €/MWh (médiane ~10), PV bâtiment -9 à +11 €/MWh (médiane ~0) [L20 (mesuré)]
- Enjeu en volume : ~18,2 GW retenus → ~32 TWh/an ; avec écart médian ~10 €/MWh : borne haute ~300 M€/an (suppose que tout l'écart soit une rente, improbable) ; à comparer à 5,7 Md€ d'aides attendues sur 2024-2047 (238 M€/an) et 87 Md€ d'engagements SPE [L21 (mesuré)]
- Le scénario de prix de marché CRE (70 €2024/MWh en 2030) impliquerait un CR versé de 4 à 26 €/MWh selon filière [L22 (mesuré)]
- Sur-rémunérations AVÉRÉES documentées par la CdC : guichets ouverts (PV 2006-2010 « notoirement surévalué », effet d'aubaine, arrêté annulé par le CE faute de notification à la Commission ; afflux non endigués : petit PV bâtiment, biométhane) [L31 (mesuré)]
- Indexation automatique des tarifs : recommandation n°3 CdC ; le contradictoire CRE cite « des évolutions tarifaires supérieures à l'évolution des coûts d'exploitation » (l.178) : point où une sur-rémunération peut se matérialiser sans nouvel AO [L32 (mesuré)]
- Trou de contrôle confirmé : la CRE reconnaît avoir peu mis en œuvre la collecte annuelle des coûts et recettes (contradictoire §1) et se déclare défavorable à une transmission systématique au profit d'un échantillonnage : les coûts réels par projet ne sont nulle part [L33 (mesuré)]
- Hepp éolien moyenne nationale ~2 200 (pas 2 400) : LCOE ~83 €/MWh, écart réduit à ~3-4 €/MWh : la fourchette 0-15 €/MWh couvre cette variation [L46 (estimé)]

## 3. Acteurs nominaux

**Institutions** : CRE (rapport n°2026-01 du 15/01/2026, communiqué 18/02/2026, contradictoire au rapport CdC), Cour des comptes (synthèse 18/03/2026, rec. n°1 et n°3), Conseil d'État (annulation arrêté PV).
**Catégories** : producteurs ENR (filières éolien terrestre, PV au sol, PV bâtiment), contribuables (SPE 87 Md€).

## 4. Sources externes citées

Rapport CRE n°2026-01 (15/01/2026, CAPEX et tarifs, l.824-828, 851-869, 1638-1639), synthèse CdC 18/03/2026 + contradictoire CRE (archivés dans data/), communiqué CRE 18/02/2026.

## 5. Chronologie datée

2006-2010 : PV guichet ouvert « notoirement surévalué », arrêté annulé par le CE ; 11/2021 : bas CAPEX éolien ; 12/2022 : haut CAPEX éolien ; 15/01/2026 : rapport CRE PPE2 ; 18/02/2026 : communiqué tarifs AO ; 18/03/2026 : rapport CdC + contradictoire ; 2024-2047 : 5,7 Md€ d'aides attendues.

## 6. Mécanismes / chaînes causales

**M1 — Le tarif de référence n'est pas un coût** : il intègre la rémunération normale du capital et les risques, et le CR ne se déclenche qu'en dessous du prix de marché : les écarts 0-15 €/MWh ne qualifient pas une sur-rémunération. Niveau : L2. [L19-L22 (mesuré)]
**M2 — Le mécanisme ex post vivant : l'indexation automatique** : rec. n°3 CdC ; la CRE cite elle-même des évolutions tarifaires supérieures aux coûts d'exploitation : point de matérialisation possible sans nouvel AO. Niveau : L2. [L32 (mesuré)]
**M3 — Le trou de contrôle, pas un accident** : les coûts réels par projet sont indisponibles par construction (collecte jugée « trop lourde », échantillonnage préféré) : le chiffrage exact est INDISPONIBLE, la démonstration de l'opacité est le livrable réel. Niveau : L2. [L33 (mesuré)]
**M4 — La voie opérationnelle : 2 CADA (D05 CRE, D06 DGEC)** : résultats des collectes d'échantillonnage (biogaz début 2024, hydro < 4,5 MW début 2025), état du plan d'audit (rec. n°1), ventilation coûts/recettes ; bilan des fraudes et sanctions, recouvrement des indus (rec. n°4). Niveau : L2. [L37 (mesuré)]

## 7. Verbatim et citations

- « des évolutions tarifaires supérieures à l'évolution des coûts d'exploitation » (contradictoire CRE, l.178) [L32 (mesuré)]
- « Les coûts réels par projet ne sont donc nulle part : le chiffrage exact est INDISPONIBLE par construction, pas par accident » [L33 (mesuré)]

## 8. Notes méthodologiques source

- **Fiabilité** : calculs transparents (formule LCOE donnée, hypothèses marquées) ; aucune preuve de sur-rémunération n'est tirée de ce document.
- **F-##** : 0 identifiant FCT dans la source (fichier de croisement) : les faits sont tracés par ligne.
- **Méthode** : LCOE = (CAPEX €/kW × CRF)/hepp + OPEX, WACC nominal 7 %, durée 25 ans, CRF 0,085 ; double vérification par scénario de marché CRE.

## 9. Limites connues (case-limites)

- Aucun chiffre de ce document ne constitue une preuve de sur-rémunération : la borne 300 M€/an est « strictement indicative » (coûts réels = hypothèse ET marge normale = 0).
- Volume par filière non sourcé (tableaux en images) ; hepp PV standard ; OPEX conventionnels ; le tarif AO n'est pas un prix versé garanti.
- P3 réduit à deux mécanismes documentés et non chiffrables aux données publiques : indexation (rec. n°3) et guichets ouverts.
