# CROISEMENT TARIFS DES APPELS D'OFFRES PPE2 VS COÛTS : CHIFFRAGE DES SUR-RÉMUNÉRATIONS POTENTIELLES (P3)

> Type : INVESTIGATION. Date : 2026-08-10 17:33 CEST. Objet : volet restant de P3 du run2-enr (trou de contrôle CdC : sur-rémunérations potentielles des filières ENR soutenues).
> Méthode : sur-rémunération potentielle = tarif garanti (complément de rémunération, AO PPE2) − coût complet de production estimé (LCOE) − rémunération normale du capital. Les coûts réels déclarés n'étant ni collectés exhaustivement ni publiés, le calcul repose sur des LCOE reconstitués à partir des CAPEX publics du rapport CRE PPE2, avec hypothèses transparentes.
> Sources : rapport CRE n°2026-01 (15/01/2026, CAPEX et tarifs), synthèse CdC 18/03/2026 + contradictoire CRE (archivés dans `data/`).

## 1. DONNÉES DE BASE (sources primaires)

| Paramètre | Éolien terrestre | PV au sol | PV bâtiment | Source |
|-----------|------------------|-----------|-------------|--------|
| Tarif AO PPE2 moyen (dernières périodes) | 86,62 €/MWh | 74,13 €/MWh | 96,48 €/MWh | CRE PPE2, communiqué 18/02/2026 |
| CAPEX | 1 700-1 800 €/kW (stabilisé ~1 750 €/kW en 02/2025 ; bas 1 600 €/kW 11/2021, haut 2 100 €/kW 12/2022) | ~900 €/kWc | ~1 150 €/kWc (en baisse ~-100 €/kWc) | CRE PPE2, l.824-828 et 851-869 |
| Heures équivalent pleine puissance (hepp) | ~2 400 (HDF 2 483, NA 2 355, Occitanie 2 630) | ~1 400 (hypothèse standard) | ~1 100 (hypothèse standard) | CRE PPE2 (l.1638-1639) ; hypothèses marquées |
| OPEX (fixe + variable) | ~15 €/MWh (hypothèse) | ~9 €/MWh (hypothèse) | ~8 €/MWh (hypothèse) | Hypothèses conventionnelles |
| Volume retenu cumulé (fin 2021-30/06/2025) | ~8 GW (hypothèse de répartition, non sourcée : les tableaux du rapport sont en images) | ~9 GW (idem) | inclus PV bâtiment | CRE PPE2 (18,2 GW cumulés, 2 074 projets) |

## 2. RECONSTITUTION DU LCOE (calcul transparent, WACC nominal 7 %, durée 25 ans, CRF = 0,085)

Formule : LCOE ≈ (CAPEX €/kW × CRF) / hepp + OPEX, exprimé en €/MWh (CAPEX en €/kW = €/MWh × hepp × 1 000⁻¹ sur l'annuité).

| Filière | CAPEX annualisé (€/MW-an) | Coût capital par MWh | + OPEX | LCOE estimé | Tarif AO | Écart (tarif − LCOE) |
|---------|---------------------------|----------------------|--------|-------------|----------|----------------------|
| Éolien terrestre | 1 750 000 × 0,085 = 148 750 | 148 750 / 2 400 = 62,0 €/MWh | +15 | ~77 €/MWh (fourchette 70-85) | 86,62 | +1 à +17 €/MWh (médiane ~10) |
| PV au sol | 900 000 × 0,085 = 76 500 | 76 500 / 1 400 = 54,6 €/MWh | +9 | ~64 €/MWh (fourchette 55-70) | 74,13 | +4 à +19 €/MWh (médiane ~10) |
| PV bâtiment | 1 150 000 × 0,085 = 97 750 | 97 750 / 1 100 = 88,9 €/MWh | +8 | ~97 €/MWh (fourchette 85-105) | 96,48 | -9 à +11 €/MWh (médiane ~0) |

Enjeu en volume : ~18,2 GW retenus → production annuelle estimée ~32 TWh (éolien ~19 TWh + PV ~13 TWh, sous l'hypothèse de répartition non sourcée ci-dessus). Avec un écart médian de ~10 €/MWh, l'enjeu serait de l'ordre de **~300 M€/an** : il s'agit d'une **borne haute strictement indicative**, qui supposerait que la totalité de l'écart médian tarif − LCOE soit une rente (coûts réels = hypothèse ET marge normale = 0), ce qui est improbable. Comparé à : 5,7 Md€ d'aides attendues sur 2024-2047 (238 M€/an) et 87 Md€ d'engagements de charges SPE. À titre de contexte, le scénario de prix de marché de la CRE (70 €2024/MWh en 2030) impliquerait un complément de rémunération versé de l'ordre de 4 à 26 €/MWh selon filière, sans préjuger de la marge (dépend des coûts réels).

## 3. VERDICT HONNÊTE : AUCUNE SUR-RÉMUNÉRATION AVÉRÉE CHIFFRABLE AUX DONNÉES PUBLIQUES

1. **Sur les AO PPE2 (éolien, PV sol, PV bâtiment)** : les écarts tarif − coût complet estimé sont de l'ordre de 0 à 15 €/MWh selon les hypothèses (WACC, durée, hepp, OPEX, prix de marché futur). C'est insuffisant pour qualifier une sur-rémunération : le tarif de référence n'est pas un coût, il intègre la rémunération normale du capital et les risques, et le complément de rémunération ne se déclenche qu'en dessous du prix de marché. **Non concluant, pas de rente démontrable.**
2. **Là où les sur-rémunérations sont AVÉRÉES** (et documentées par la CdC) : les **guichets ouverts**, pas les appels d'offres. La CdC rappelle le photovoltaïque 2006-2010 « notoirement surévalué » (effet d'aubaine, intervention législative, arrêté annulé par le Conseil d'État faute de notification à la Commission) et les afflux de demandes non endigués par les modulations tarifaires (petit PV bâtiment, biométhane).
3. **Le mécanisme de sur-rémunération ex post vivant** : l'**indexation automatique des tarifs** (recommandation n°3 de la CdC). Le contradictoire CRE lui-même cite « des évolutions tarifaires supérieures à l'évolution des coûts d'exploitation » (l.178) : c'est le point où une sur-rémunération peut se matérialiser sans nouvel appel d'offres.
4. **Le trou de contrôle est confirmé, pas résorbé** : la CRE reconnaît avoir peu mis en œuvre la collecte annuelle des coûts et recettes (contradictoire, §1) et se déclare **défavorable à une transmission systématique** au profit d'un échantillonnage. Les coûts réels par projet ne sont donc nulle part : le chiffrage exact est INDISPONIBLE par construction, pas par accident.

## 4. IMPLICATIONS POUR LE RUN2-ENR (P3)

1. **P3 (volet sur-rémunérations)** : réduit à deux mécanismes documentés et non chiffrables aux données publiques : l'indexation (rec. n°3 CdC) et les guichets ouverts. Aucune rente avérée chiffrable sur les AO PPE2.
2. **La démonstration de l'opacité** est le livrable réel : l'État s'apprête à verser 5,7 Md€ d'aides PPE2 (et porte 87 Md€ d'engagements) sans publication des coûts réels, la collecte étant jugée « trop lourde » par la CRE, et la CdC demandant en vain (rec. n°1, échéance 2026) un plan d'audit des filières et un tableau de bord de l'économie des filières.
3. **Voie opérationnelle** : les 2 CADA du run deviennent la seule issue. D05 (CRE) : résultats des collectes d'échantillonnage déjà menées (biogaz électricité début 2024, hydro < 4,5 MW début 2025 ; biométhane injecté, petite hydro et petit PV bâtiment lors de collectes antérieures non datées), état d'avancement du plan d'audit (rec. n°1), et ventilation coûts/recettes agrégées par filière si communicable. D06 (DGEC) : bilan des fraudes et sanctions, recouvrement des indus (rec. n°4), suites données aux rec. n°1 et n°3.

## 5. LIMITES DE CE CROISEMENT (à lire avant toute utilisation)

1. Le tarif AO est un tarif de référence, pas un prix versé garanti en toutes circonstances : le CR ne compense que la différence avec le marché, et les producteurs peuvent être redevables si le marché dépasse le tarif.
2. Le LCOE reconstitué repose sur des hypothèses (WACC nominal 7 %, durée 25 ans, hepp PV standard, OPEX conventionnels) : les écarts de 0 à 15 €/MWh varient du simple au double selon ces hypothèses. Aucun chiffre de ce document ne constitue une preuve de sur-rémunération.
3. Les coûts réels déclarés (la seule donnée qui permettrait de trancher) ne sont ni collectés exhaustivement ni publiés : c'est le trou de contrôle, documenté aux deux sources.
4. Les données d'échantillonnage existent (CRE en a mené) mais ne sont pas publiées dans le rapport PPE2 : la demande CADA D05 est calibrée pour les obtenir.
5. Les hepp retenues pour l'éolien (2 400) sont celles des régions les plus productives (HDF 2 483, NA 2 355, Occitanie 2 630) : la moyenne nationale est plutôt ~2 200 hepp, ce qui élèverait le LCOE éolien à ~83 €/MWh et réduirait l'écart à ~3-4 €/MWh. La fourchette 0-15 €/MWh couvre cette variation.

STATE          : FINAL
VERSION        : 1.0
CREATED        : 2026-08-10_17-33 CEST
HASH           : (consigné dans dossier_enr.sha256 après mise à jour)
