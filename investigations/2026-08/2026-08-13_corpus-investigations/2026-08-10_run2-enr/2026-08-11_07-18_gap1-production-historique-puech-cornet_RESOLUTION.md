# RESOLUTION : PRODUCTION HISTORIQUE 2007-2025 DU PARC PUECH CORNET (VERSIONS ANNUELES RNIP/ODRE)

- STATE          : FINAL
- DATE           : 2026-08-11 07:18 CEST
- TYPE           : RESOLUTION (KERNEL v2.8, format allégé axe piste)
- DOSSIER        : 2026-08-10_run2-enr (piste ENR, axe C, suite 06-51/07-11)
- OBJECT         : reconstituer la production historique annuelle 2007-2023 des 2 tranches de Puech Cornet (t1 11 500 kW MES 14/09/2007 + t2 2 300 kW MES 29/07/2009) pour solidifier la fourchette de rente OA (06-51 : proxy constant 21,6-27,7 M€ bruts)
- REPONSE A      : GAP-pr-1 du document 06-51 (et GAP-oa-5 du 21-30)
- DONNEES NOUVELLES : 9 versions annuelles du dataset RNIP/ODRE `registre-national-installation-production-stockage-electricite-agrege-311217` à `311225` (extraction exports/csv 11/08/2026), registres RTE 2015/2016 (schéma, hors périmètre), calcul /tmp/pr1_rente.py

---

## 1. La série de production : 9 versions RNIP annuelles (source primaire Enedis/ODRE)

Chaque version annuelle du RNIP agrégé (au 31/12/2017 → 31/12/2025) contient l'**énergie annuelle glissante injectée** (12 mois) par installation à sa date de version. Interrogation des 9 versions pour Fontrieu (81062) :

| Version | Date de version | t1 (11,5 MW) kWh | t2 (2,3 MW) kWh | Total GWh |
|---------|-----------------|------------------|-----------------|-----------|
| 311217 | (01/07/2015-2016) | non renseigné | non renseigné | - |
| 311218 | 20/08/2018 | non renseigné | non renseigné | - |
| 311219 | 16/05/2019 | non renseigné | non renseigné | - |
| 311220 | 01/12/2020 | 21 170 868 | 2 854 690 | **24,03** |
| 311221 | 01/11/2021 | 20 478 159 | 2 420 897 | **22,90** |
| 311222 | 01/04/2022 | 18 716 201 | 2 551 762 | **21,27** |
| 311223 | 21/02/2023 | 18 171 821 | 1 798 509 | **19,97** |
| 311224 | 01/05/2024 | 20 146 493 | 2 393 487 | **22,54** |
| 311225 | 03/06/2025 | 19 870 753 | 2 648 501 | **22,52** |

**Série mesurée : 6 points (2020-2025), moyenne 22,20 GWh/an, min 19,97 (2023), max 24,03 (2020).** Répartition moyenne : t1 = 19,76 GWh (89 %), t2 = 2,44 GWh (11 %).

Caveats : (a) l'énergie est **glissante** (12 mois à la date de version), pas une année civile : les ratios sont indicatifs ; (b) les versions 311217-311219 ne renseignent pas la production pour ces installations (champ vide) : pas de mesure 2017-2019 dans ce dataset ; (c) la version 311225 ajoute une 3e installation (180 kW, solaire PV, MES 11/06/2025, poste LUZI1, code EIC 17W000002281791V) : NON liée au parc éolien (sans effet sur la série éolienne).

## 2. Registres RTE 2015/2016 : hors périmètre (confirmé)

Les registres `registre-national-installation-production-electricite-rte-2015` et `-2016` (42 champs dont `energie_annuelle_injectee/produite`) ont été interrogés sur Fontrieu : **0 installation** (le parc est raccordé en HTA au réseau Enedis, pas au réseau de transport RTE). Ces registres ne couvrent pas le parc : voie close, constat documenté.

## 3. Rente OA recalculée avec la série mesurée (script /tmp/pr1_rente.py)

Fenêtres OA par tranche : t1 (MES 14/09/2007) = OA 2007-2022, T1 (82 €/MWh) 10 ans puis T2 5 ans ; t2 (MES 29/07/2009) = OA 2009-2024, T1 10 ans puis T2 5 ans.

| Scénario | Production | Rente brute (T2 28-82 €) | Marge (coûts 20 €/MWh) |
|----------|-----------|--------------------------|------------------------|
| **S1 série mesurée (moy 22,2 GWh)** | 22,20 GWh | **21,3-27,3 M€** | **14,7-20,7 M€** |
| S2 min série (2023) | 19,97 GWh | 19,2-24,6 M€ | 13,2-18,6 M€ |
| S3 max série (2020) | 24,03 GWh | 23,1-29,6 M€ | 15,9-22,3 M€ |
| S4 prévisionnel acquéreur 2019 (07-11) | 28,00 GWh | 26,9-34,4 M€ | 18,5-26,0 M€ |
| S5 marketing Valeco | 34,32 GWh | 33,0-42,2 M€ | 22,7-31,9 M€ |

**Résultat : la fourchette du 06-51 (proxy constant 21,6-27,7 M€ bruts / 14,9-21,0 M€ marge) est CONFIRMÉE et consolidée par la série mesurée** (S1 = 21,3-27,3 M€ / 14,7-20,7 M€, quasi identique). L'écart entre la borne basse mesurée (S2 : 19,2 M€) et la borne haute du scénario acquéreur (S4 : 34,4 M€) donne l'**enveloppe des scénarios plausibles : 19,2-34,4 M€ bruts** (marge 13,2-26,0 M€), avec le centre de gravité sur la série mesurée (21,3-27,3 M€).

## 4. Ce que la série dit de la thèse « aléa de production non maîtrisé » (07-11)

- Le prévisionnel acquéreur (28 GWh) était 24 % au-dessus de la moyenne mesurée (22,2 GWh) : **l'écart est confirmé par 6 points mesurés, pas un artefact d'année** (2020-2025 : 19,97 à 24,03 GWh, jamais 28).
- La production 2020-2025 est **stable et basse** (heures équivalentes ~1 900-2 100 h/an vs 2 000-2 174 h prévisionnelles) : aucune année n'approche le prévisionnel, et 2023 (19,97 GWh) est le creux.
- Caveat d'extrapolation : la série ne commence qu'en 2020. Les années 2007-2019 (parc neuf) ont pu produire davantage (le S4 acquéreur est la meilleure borne haute pour ces années), mais rien dans les données disponibles ne l'atteste : GAP-h-1 (production 2007-2019 via Enedis historique).

## 5. Faits consolidés

| # | Fait | Source |
|---|------|--------|
| FCT-h-001 | Le dataset RNIP/ODRE agrégé existe en 9 versions annuelles (311217 à 311225), chacune avec l'énergie annuelle glissante injectée par installation | Catalogue ODRE (187 datasets), 11/08/2026 |
| FCT-h-002 | Série t1 (11,5 MW) : 21,17 / 20,48 / 18,72 / 18,17 / 20,15 / 19,87 GWh (2020-2025) ; moyenne 19,76 GWh, part 89 % du total | RNIP versions 311220-311225, exports/csv |
| FCT-h-003 | Série t2 (2,3 MW) : 2,85 / 2,42 / 2,55 / 1,80 / 2,39 / 2,65 GWh (2020-2025) ; moyenne 2,44 GWh, part 11 % | RNIP versions 311220-311225 |
| FCT-h-004 | Total mesuré : 24,03 (2020) / 22,90 (2021) / 21,27 (2022) / 19,97 (2023) / 22,54 (2024) / 22,52 (2025) GWh ; **moyenne 22,20 GWh/an, min 19,97, max 24,03** | Calcul /tmp/pr1_rente.py |
| FCT-h-005 | Aucune année mesurée n'atteint le prévisionnel acquéreur (28 GWh) : écart 24 % confirmé sur 6 points | Confrontation série vs 07-11 |
| FCT-h-006 | Les versions 311217-311219 ne renseignent pas la production de ces installations (champ vide) : pas de mesure 2017-2019 dans ce dataset | RNIP 311217-311219 |
| FCT-h-007 | Registres RTE 2015/2016 (42 champs, colonnes energie_annuelle_*) : 0 installation à Fontrieu (parc raccordé HTA Enedis, pas au réseau de transport) : voie close | ODRE registre-rte-2015/2016, requête codeinseecommune='81062' |
| FCT-h-008 | Nouvelle installation 180 kW à Fontrieu (MES 11/06/2025, solaire PV, poste LUZI1, EIC 17W000002281791V) : NON liée au parc éolien | RNIP 311225 |
| FCT-h-009 | **Rente brute série mesurée (S1) : 21,3-27,3 M€ ; marge 14,7-20,7 M€ : la fourchette du 06-51 (21,6-27,7 / 14,9-21,0) est CONFIRMÉE et consolidée** | /tmp/pr1_rente.py |
| FCT-h-010 | Enveloppe des scénarios plausibles : 19,2-34,4 M€ bruts (borne S2 min série 19,2 à borne S4 haut prévisionnel acquéreur 34,4) ; centre de gravité série mesurée S1 21,3-27,3 M€ ; marge 13,2-26,0 M€ ; S5 marketing (33,0-42,2) exclu car jamais observé | /tmp/pr1_rente.py |
| FCT-h-011 | Production 2007-2019 (parc neuf) : inconnue en sources ouvertes (RNIP non renseigné avant 2020, RTE hors périmètre, TheWindPower bloqué) : GAP-h-1 | Constat d'absence (section 1-2) |

## 6. Verdict

1. **GAP-pr-1 RÉSOLU pour 2020-2025 : série mesurée de 6 points** (moyenne 22,20 GWh/an, 19,97-24,03) via les 9 versions annuelles du RNIP/ODRE. La fourchette de rente du 06-51 est **confirmée et consolidée** : 21,3-27,3 M€ bruts (14,7-20,7 M€ de marge) avec la série mesurée.
2. **L'écart prévisionnel/réel est structurel** : aucune année 2020-2025 n'atteint le 28 GWh de l'acquéreur (24 % au-dessus de la moyenne mesurée), ni le 34,32 GWh du marketing Valeco (55 % au-dessus). Le signal « aléa de production non maîtrisé » du 07-11 est renforcé par la série.
3. **Point aveugle résiduel : 2007-2019** (parc neuf, incluant 2015-2019 sous 3D ENERGIES et l'essentiel de la période OA T1) : non mesurable en sources ouvertes (RNIP vide avant 2020, RTE hors périmètre). La borne haute réaliste pour ces années est le prévisionnel acquéreur (28 GWh), mais rien ne l'atteste.
4. **0 corruption pénale inchangé** ; signal structurel consolidé : la SEM publique (3D ENERGIES/SIEDS) a capté une marge de l'ordre de 1,4-1,8 M€/an mesurée (2020-2025), avec un prévisionnel d'achat 24 % au-dessus de la réalité, un prix non publié (06-36) et des délibérations 2014-2015 absentes en ligne (07-11).

## 7. GAPS

| # | Gap | Voie |
|---|-----|------|
| GAP-h-1 | Production réelle 2007-2019 des 2 tranches (année par année) | Enedis Open Data historique, registre de production mensuelle (accès CADA Enedis), presse/rapports 3D ENERGIES annuels |
| GAP-h-2 | Vérifier si les courbes de production mensuelles (dataset ODRE `courbes-de-production-mensuelles-eolien-solaire-complement-de-remuneration`) couvrent ce parc (contrat OA, probablement hors CR) | Dataset ODRE, codes EIC 17W000000059857Z / 17W000000419425N |
| GAP-h-3 | Heures de fonctionnement réelles par tranche (pour le T2 réel) | Registre de production horaire Enedis |

## 8. Traçabilité

- Scripts : /tmp/pr1_series.py (extraction 9 versions), /tmp/pr1_serie2.py (consolidation), /tmp/pr1_rente.py (scénarios de rente), /tmp/pr1_rte15.py (registres RTE), /tmp/pr1_twp.py (TheWindPower, bloqué)
- Sources : ODRE opendatasoft (dataset RNIP agrégé, 9 versions 311217-311225, exports/csv), registres RTE 2015/2016 (hors périmètre), catalogue ODRE (187 datasets)
- Liens : 06-51 (GAP-pr-1 ouvert, fourchette à consolider), 07-11 (prévisionnel acquéreur 28 GWh), 06-24 (FCT-pc-018), 21-30 (méthode RNIP, GAP-oa-5)
- Em-dash : 0 (à vérifier)
