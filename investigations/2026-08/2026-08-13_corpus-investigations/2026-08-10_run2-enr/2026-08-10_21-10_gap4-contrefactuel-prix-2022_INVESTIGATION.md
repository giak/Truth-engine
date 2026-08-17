# INVESTIGATION : GAP-FLUX-4 - QUANTIFICATION DU SURCOUT 2022 ET PART IMPUTABLE AU COUPLAGE EUROPEEN

- STATE          : FINAL
- DATE           : 2026-08-10 21:10 CEST
- TYPE           : INVESTIGATION (KERNEL v2.8, format allégé axe piste)
- DOSSIER        : 2026-08-10_run2-enr (piste ENR, axe A, suite 20-42)
- OBJECT         : quantifier la part du prix de l'électricité 2022 imputable au couplage européen (market coupling PCR/EUPHEMIA) et chiffrer le surcoût payé par les consommateurs français
- REPONSE A      : GAP-flux-4 du document 20-42 (suggéré en priorité) ; thèse utilisateur « le prix de l'électricité en France est fixé par l'Europe, détournement massif »
- CONTRADICTION  : le calcul naïf du 20-42 (78-92 Md€) supposait un prix isolé France de 45-80 €/MWh SANS tenir compte de la crise d'offre nucléaire française de 2022 ; présent document teste cette hypothèse contre les faits

---

## 0. Hypothèses testées

- H0 : le couplage européen a imposé à la France le prix allemand (prix fixé par le gaz allemand) : surcoût massif imputable à l'Europe.
- H1 : le prix français 2022 (276 €/MWh) reflète une crise d'OFFRE propre (65 % du nucléaire à l'arrêt) : la France a payé SA rareté, pas celle de l'Allemagne.
- H2 : le transfert massif est réel mais passe par d'autres canaux mesurables (bouclier tarifaire, échec de capture de la rente, factures des entreprises).

---

## 1. Faits établis (sources primaires/secondaires directes)

| # | Fait | Source | Date source |
|---|------|--------|-------------|
| FCT-g4-001 | Prix day-ahead moyen annuel France 2022 : 276 €/MWh (multiplication par 2,5 vs 2021) | RTE, Bilan électrique 2022/2023 (analysesetdonnees.rte-france.com) | 02/2023 |
| FCT-g4-002 | Prix day-ahead moyen annuel France 2021 : 109 €/MWh | RTE/Connaissance des Énergies | 02/2023 |
| FCT-g4-003 | Prix day-ahead moyen annuel Allemagne 2022 : ~235 €/MWh, INFÉRIEUR au prix français (276) | Open Energy Tracker (données Bundesnetzagentur) | 08/2026 |
| FCT-g4-004 | La France a été IMPORTATRICE NETTE en 2022 : -16,5 TWh, première fois depuis 1980 | RTE, Bilan électrique 2022, chapitre échanges | 02/2023 |
| FCT-g4-005 | Indisponibilité nucléaire : minimum historique 21,7 GW le 28/08/2022, ~65 % du parc à l'arrêt (36/56 réacteurs) | RTE, Bilan électrique 2022, synthèse PDF | 02/2023 |
| FCT-g4-006 | Taux de convergence des prix horaires FR-DE 2022 : ~24 % du temps seulement | CRE, rapport mise en œuvre calcul capacité 70 % (juillet 2023) | 07/2023 |
| FCT-g4-007 | Prix moyen août 2022 France : ~492 €/MWh ; pic journalier historique 743,8 €/MWh le 30/08/2022 | Sénat, rapport d'information n° 670 (2022-2023), 01/06/2023 | 06/2023 |
| FCT-g4-008 | Prix spot France : <20 €/MWh au printemps 2020 → >300 €/MWh fin septembre 2022 (x15) | Sénat n° 670, même source | 06/2023 |
| FCT-g4-009 | Coût complet du nucléaire français historique : 50-60 €/MWh | CdC / RTE (cité par Sénat 670, RAC/FNH) | 2022-2023 |
| FCT-g4-010 | EDF : PERTE NETTE 2022 de -17,9 Md€ (résultat net part du groupe) ; impact des mesures réglementaires sur EBITDA : -10,2 Md€ | CP EDF 17/02/2023 | 02/2023 |
| FCT-g4-011 | ARENH : 100 TWh à 42 €/MWh + allocation additionnelle 20 TWh à 46,2 €/MWh (mars 2022) ; EDF rachète sur le marché à ~257 €/MWh moyen | EDF/CP 14/03/2022 | 03/2022 |
| FCT-g4-012 | Bouclier tarifaire électricité : ~21,5 Md€ (2021-2024) ; ~21,8 Md€ en 2022 selon la CRE ; coût global électricité+gaz 26,3 Md€ | Vie publique / CdC, rapport boucliers mars 2024 | 03/2024 |
| FCT-g4-013 | CRIM (contribution rente inframarginale, loi 2023, rétroactif 01/07/2022) : prévision 12,3 Md€ en LFI, perçue seulement ~400 M€ en 2022 (+300 M€ en 2023) ; écart qualifié d'« extraordinairement rare » par la CdC | Impots.gouv.fr / Connaissance des Énergies (AFP) / CdC | 04/2024 |
| FCT-g4-014 | Commission européenne, proposition 14/03/2023 (SWD(2023) 58) : le merit-order soumet nucléaire et ENR à la volatilité du gaz (TTF +1000 % vs décennie précédente aux pics été 2022) | Commission européenne / DG ENER + JRC | 03/2023 |
| FCT-g4-015 | Phuc-Vinh Nguyen (Institut Jacques Delors) : prix de gros +254 % entre T2 2021 et T2 2022 | IJ Delors / Toute l'Europe | 2023-2024 |
| FCT-g4-016 | Bénéficiaires du choc 2022 : producteurs ENR non plafonnés (avant déc. 2022), traders, pays exportateurs ; perdants : entreprises/collectivités exposées au marché, budget public (bouclier) ; EDF perdant net (régulé) | Synthèse CRE/AFP + comptes EDF | 2023-2024 |
| FCT-g4-017 | Plafonnement des revenus ENR : article 38 loi 2022-1157 (16/08/2022), seuils français < plafond européen 180 €/MWh (ex. ~90 €/MWh nucléaire, filières ENR spécifiques) | Légifrance / délibérations CRE | 12/2022 |

---

## 2. Le contrefactuel : calcul de notre part (script /tmp/calc_contrefactuel_2022.py)

### 2.1 Bornes théoriques (à ne PAS lire comme « imputable au seul couplage »)

| Scénario prix isolé France | Surcoût unitaire vs 276 | Surcoût total (400 TWh exposés) |
|---------------------------|-------------------------|--------------------------------|
| 80 €/MWh (pessimiste) | 195 €/MWh | ~78 Md€ |
| 60 €/MWh (médian = coût nucléaire) | 215 €/MWh | ~86 Md€ |
| 45 €/MWh (optimiste) | 230 €/MWh | ~92 Md€ |

**Ces bornes sont des MAXIMA THÉORIQUES, pas un chiffre imputable au couplage.** Elles supposent que la France aurait pu produire tout son volume au coût nucléaire, or le parc était à 65 % à l'arrêt (FCT-g4-005) : la France ne POUVAIT pas fournir ~460 TWh au coût nucléaire en 2022. Un prix isolé de 45-60 €/MWh était physiquement impossible cette année-là.

### 2.2 La contre-preuve décisive (FCT-g4-003, 004, 006)

1. **Le prix français (276) était SUPÉRIEUR au prix allemand (235)** : l'Allemagne ne « fixait » pas un prix bas imposé à la France ; c'est l'inverse, la rareté française a tiré le prix français au-dessus du marché voisin.
2. **Convergence FR-DE : 24 % seulement du temps** : sur ~76 % des heures, les prix n'étaient pas unifiés (le plus souvent prix FR > prix DE, la France important).
3. **Cause dominante du prix français : la pénurie nucléaire française** (65 % du parc à l'arrêt) qui a forcé des imports massifs (-16,5 TWh) et l'usage de centrales à gaz marginales EN FRANCE.

### 2.3 La part « couplage » réellement imputable

Le mécanisme couplage a joué dans la TRANSMISSION (imports d'électricité produite au gaz européen, prix alignés par le merit-order), mais le déclencheur était national. Estimation honnête :
- Surcoût du VOLUME IMPORTÉ (16,5 TWh × écart prix import ~200 €/MWh vs coût théorique) : ~3 Md€ (borne).
- Surcoût du VOLUME PRODUIT EN FRANCE au gaz marginal (la France a fait tourner ses centrales à gaz pour compenser : plusieurs dizaines de TWh) : c'est le poste dominant, mais il relève de la CRISE D'OFFRE, pas du couplage.
- Le transfert comptablement MESURÉ (FCT-g4-012/013) : bouclier électricité ~21,5 Md€ + CRIM perçue 0,4 Md€ = l'État a dépensé ~21 Md€ nets, les entreprises exposées ont payé de plein fouet, EDF a perdu 17,9 Md€.

---

## 3. MANIPULATION_REPORT (15 symboles, notation -2 à +2)

| # | Symbole | Score | Justification |
|---|---------|-------|---------------|
| 1 | CHOC_OFFRE_NATIONALE | +2 | 65 % nucléaire à l'arrêt = cause dominante documentée (RTE) |
| 2 | PRIX_FR_SUP_DE | +2 | 276 vs 235 €/MWh : la thèse « l'Allemagne fixe notre prix » est réfutée pour 2022 |
| 3 | CONVERGENCE_FAIBLE | +1 | 24 % seulement d'heures convergentes (CRE) |
| 4 | COUPLAGE_TRANSMISSION | +1 | Vecteur de transmission via imports, pas cause première |
| 5 | RENTE_ABSENTE_EDF | +2 | EDF perdu 17,9 Md€ : aucune rente nucléaire captée par le producteur public |
| 6 | BOUCLIER_COUT | +2 | 21,5 Md€ : transfert budget public → ménages |
| 7 | CRIM_ECHEC | +2 | 400 M€ perçus vs 12,3 Md€ prévus : capture des superprofits RATÉE |
| 8 | ENTREPRISES_PAYEUSES | +1 | Exposées au marché de gros, non protégées par le bouclier |
| 9 | ENR_PLUS_QUE_PLAFOND | -1 | Avant déc. 2022, ENR non plafonnées ont capté les prix hauts (mais courte fenêtre) |
| 10 | TTF_VOLATILITE | +1 | +1000 % : le gaz européen a amplifié, mais via l'offre FR importée |
| 11 | PEREQUATION_EUROPEENNE | 0 | Le couplage péréquate les prix, n'explique pas la hausse FR |
| 12 | IMPORTS_16_TWH | +1 | -16,5 TWh nets = exposition au marché voisin |
| 13 | X15_SPOT | 0 | <20 → >300 €/MWh : ampleur réelle mais multi-causale |
| 14 | TRANSFERT_NET_ETAT | +1 | ~21 Md€ nets dépensés (bouclier - CRIM) |
| 15 | DISCOURS_POLITIQUE | 0 | Le récit « l'Europe nous vole » simplifie : la crise nucléaire FR est nationale |

Score net : +17/30 (faisceau « crise d'offre nationale dominante + transferts réels mesurables »).

---

## 4. VERDICT (honnêteté forensique, contre la thèse initiale)

**1. La thèse « le couplage européen a imposé à la France le prix allemand » est RÉFUTÉE pour 2022 :** le prix français était supérieur au prix allemand (276 vs 235 €/MWh), la convergence FR-DE était de 24 %, et la cause dominante du prix français était la pénurie nucléaire nationale (65 % du parc à l'arrêt, -16,5 TWh d'imports nets). L'utilisateur pointait « l'Europe UERSS corrompue » : la mécanique européenne a amplifié et transmis, mais le déclencheur était français (corrosion sous contrainte, décisions de maintenance).

**2. Le transfert massif est CONFIRMÉ, mais par d'autres canaux (tous mesurables) :**
- **21,5 Md€ de bouclier tarifaire** : le budget public a payé pour contenir la facture des ménages (transfert impôt/future dette → consommation) ;
- **L'échec de la CRIM** : prévue à 12,3 Md€, perçue 400 M€ : les superprofits de 2022 (dont ENR non plafonnées avant déc. 2022, traders, exportateurs) n'ont PAS été récupérés. C'est le vrai trou de régulation, documenté par la CdC ;
- **Les entreprises et collectivités** ont payé le prix de gros de plein fouet (non couverts par le bouclier) : transfert non chiffré précisément, à documenter (GAP-g4-2).

**3. La charge correcte n'est pas « le couplage vole la France » mais :**
- la France a payé SA propre rareté (choix industriels : corrosion, maintenance) ;
- le mécanisme de prix marginal européen a transmis l'amplitude (pas la cause) ;
- l'État a dépensé 21,5 Md€ de bouclier SANS récupérer la rente (CRIM 0,4 Md€) : la solidarité publique a profité aux fournisseurs et à certains producteurs, pas au budget.

**4. Position sur le fil du dossier :** ce résultat renforce le GAP-flux-1 du 20-42 (les ENR à tarif fixe ont protégé l'État en 2022 : FCT-flux-003) et NUANCE l'angle « couplage = détournement » de l'utilisateur. Le transfert le plus documentable reste le couple bouclier 21,5 Md€ + échec CRIM, pas le market coupling.

---

## 5. GAPS et prochaines étapes

| # | Gap | Voie |
|---|-----|------|
| GAP-g4-1 | Prix moyen Allemagne 2022 à confirmer à la source primaire (EPEX/ENTSO-E plutôt que Open Energy Tracker) | Télécharger les données ENTSO-E Transparency 2022 |
| GAP-g4-2 | Chiffrer le surcoût payé par les entreprises/collectivités exposées au marché 2022 (volume exposé × écart) | Enquête CRE/RTE « volumes achetés au spot par segment » |
| GAP-g4-3 | Suivre le sort de la CRIM au PLF 2026-2027 (le dispositif s'est-il arrêté ? recettes finales 2023-2024 ?) | LFI 2024/2025/2026, rapports CdC |
| GAP-g4-4 | Documenter la « capture » pré-déc. 2022 des ENR non plafonnées (quels producteurs, quels montants) | Listes CRE contrats CR, comptes des SPV |
| GAP-g4-5 | Coût du nucléaire 2022 (disponibilité basse → coût marginal réel du parc, pas le coût complet historique) | RTE/EDF rapports 2023 |

---

## 6. Traçabilité

- Script de calcul : /tmp/calc_contrefactuel_2022.py (exécuté, sorties §2.1)
- Sources : RTE (Bilan 2022), Sénat n° 670, CRE (rapport 70 % capacité), EDF (CP résultats 2022), Vie publique/CdC (boucliers), Impots.gouv.fr (CRIM), Commission européenne (SWD 2023/58)
- Relié à : 20-42 (flux PDV), 20-26 (VALECO REN), 20-36 (sortie CDC), 16-39 (prémices P1-P3)
- Em-dash : 0 (vérifié)
