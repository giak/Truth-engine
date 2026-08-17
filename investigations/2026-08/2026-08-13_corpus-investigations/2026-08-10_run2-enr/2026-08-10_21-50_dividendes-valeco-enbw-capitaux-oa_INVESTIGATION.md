# INVESTIGATION : DIVIDENDES VALECO REN -> ENBW (2023-2025) ET VALEUR CAPITALISEE DES CONTRATS OA RACHETES

- STATE          : FINAL
- DATE           : 2026-08-10 21:50 CEST
- TYPE           : INVESTIGATION (KERNEL v2.8, format allégé axe piste)
- DOSSIER        : 2026-08-10_run2-enr (piste ENR, axe A, suite 20-26/20-36/21-30)
- OBJECT         : quantifier les dividendes remontant de VALECO REN vers EnBW (2023-2025) et la valeur capitalisée des contrats OA rachetés par EnBW en 2019, pour boucler la chaîne du flux public vers le Land de Bade-Wurtemberg
- REPONSE A      : demande utilisateur « lancer une investigation sur les dividendes VALECO REN → EnBW 2023-2025 et la valeur capitalisée des contrats OA rachetés (87 Md€ d'engagements) »
- DONNEES        : fichiers Pappers/verif VALECO REN déjà téléchargés (20-26), rapport EnBW 2023-2024 (chercheur web), calcul /tmp/calc_valeco_flux.py

---

## 0. Cadre

La chaîne documentée (18-58, 20-26, 21-30) : parcs (dont Puech del Vert + Bois de Merdelou) → VALECO REN (434054318) → VALECO SAS (421377946) → EnBW AG (Land Bade-Wurtemberg, ~99 % public). Le flux public (OA 82 €/MWh financé par CSPE/accise) alimente les parcs, dont les bénéfices remontent à VALECO REN, holding pure de dividendes. Cette investigation quantifie : (1) le flux de dividendes 2023-2025, (2) la valeur capitalisée des OA rachetés en 2019, (3) la part dans le groupe EnBW.

## 1. Faits établis

| # | Fait | Source | Date |
|---|------|--------|------|
| FCT-dv-001 | VALECO REN : résultat net 75,3 M€ (2022), 3,11 M€ (2023), 2,33 M€ (2024), 2,08 M€ (2025) ; CAF = RN à 100 % chaque année | Pappers fiche financière (téléchargé, lu) | 2026-08-10 |
| FCT-dv-002 | VALECO REN = holding pure de dividendes : CA 1,51 K€, EBITDA -58,9 K€, résultat 100 % hors exploitation | Pappers + verif.com (20-26) | 2026-08-10 |
| FCT-dv-003 | Actionnariat VALECO REN : VALECO SAS 51 % / FPCI MIROVA - EUROFIDEME 3 49 % (245 actions) au 03/06/2019 ; sortie du FPCI postérieure (2021-2022) | PV 03/06/2019 texte intégral (20-26) | 2019 |
| FCT-dv-004 | Réorganisation 2021-2022 : DAHLIA HOLDING (908112907, 100 % VALECO REN), apport BOIS DE MERDELOU sous 210 B, PV « Reconstitution de l'actif net » 07/07/2022 | Actes déposés RCS Montpellier (20-26) | 2021-2022 |
| FCT-dv-005 | Portefeuille de participations VALECO REN : 20+ filiales (FERME EOLIENNE DE PUECH DEL VERT, FERME EOLIENNE DU BOIS DE MERDELOU, PARC EOLIEN DE L'ENSINET, CENTRALE EOLIENNE DU FENOUILLEDES, PARC EOLIEN DE LA BRUYERE, PARC EOLIEN DE LA CHAUSSEE, ENERGIES RENOUVELABLES DU TUCHANAIS, CENTRALES SOLAIRES (LA DECOUVERTE, CHATEAUVERT), SOCPE LE CHENE COURTEAU, TERRES DE L'ABBAYE, CAMBON ENERGIE, ELEVEN, EOLE SAINT JEAN LACHALM, SOLLDEV INGENIERIE, DAHLIA HOLDING, FLEUR D'EDELWEISS HOLDING, etc.) | Pappers relations d'actionnariat (extrait, lu) | 2026-08-10 |
| FCT-dv-006 | EnBW a racheté 100 % de Valeco en 2019 : prix officiel ~229 M€ (earnings call Q1-2019) ; 300-400 M€ (Figaro, dette/pipeline inclus) ; clôture 03/06/2019 | Earnings call EnBW Q1-2019 (AlphaSpread) + Figaro (20-36) | 2019 |
| FCT-dv-007 | Valeco 2019 : 332 MW en exploitation (276 éolien + 56 solaire), pipeline 1 700 MW, ~300 ETP, CA ~30-50 M€/an | EnBW factbook 2024, rapport 6M 2024 (chercheur web) | 2024 |
| FCT-dv-008 | EnBW groupe : EBITDA segment renouvelables 1,31 Md€ (2023), ~1,2 Md€ (2024) ; capacité totale ~8 100 MW | EnBW rapport annuel 2023 (27/03/2024) + 2024 | 2024-2025 |
| FCT-dv-009 | Les dividendes Valeco → EnBW ne sont PAS ventilés publiquement (pas de ligne nominative dans les comptes consolidés) | EnBW comptes consolidés (chercheur web) | 2026 |
| FCT-dv-010 | Flux OA brut portefeuille Valeco : 620 GWh/an × 82 €/MWh = ~50,8 M€/an ; écart au marché ~35 €/MWh = ~21,7 M€/an de subvention nette | Calcul (20-42 + RNIP 21-30) | 2026 |
| FCT-dv-011 | Capitalisation de l'écart au marché (21,7 M€/an) : ~168 M€ (10 ans, 5 %) à ~225 M€ (15 ans, 5 %) | Calcul /tmp/calc_valeco_flux.py | 2026 |
| FCT-dv-012 | Le prix de 229 M€ (2019) est cohérent avec la capitalisation des flux de soutien restants (168-225 M€) + valeur du pipeline (1 700 MW) + valeur de marché hors OA | Confrontation prix vs capitalisation (calcul notre part) | 2026 |
| FCT-dv-013 | Dividendes potentiels VALECO REN 2023-2025 : 7,52 M€ cumulés (3,11 + 2,33 + 2,08) si distribution à 100 % | Calcul à partir des RN (Pappers) | 2026 |
| FCT-dv-014 | Part remontant vers EnBW : ≥ 51 % (VALECO SAS), potentiellement 100 % après sortie complète du FPCI MIROVA | Analyse actionnariat (20-26) | 2026 |
| FCT-dv-015 | La part Valeco dans EnBW groupe est minoritaire : ~2-3 M€/an de dividendes VALECO REN ≈ < 0,3 % de l'EBITDA renouvelables EnBW | Calcul vs EBITDA 1,31 Md€ (2023) | 2026 |

## 2. Le flux de dividendes 2023-2025

- VALECO REN affiche 3,11 M€ (2023), 2,33 M€ (2024), 2,08 M€ (2025) de résultat net, intégralement hors exploitation (CAF = RN).
- Si distribution à 100 % (holding pure) : **~7,52 M€ cumulés 2023-2025** de dividendes potentiels, dont ≥ 51 % (~3,8 M€) vers VALECO SAS → EnBW, potentiellement 100 % après sortie du FPCI.
- **INCONNU : la politique de distribution (affectations dans les PV d'AG non lues, GAP-dv-1).** Le RN = CAF indique que les montants sont disponibles, pas qu'ils sont distribués.
- **Verdict honnête : le flux récurrent réel est 2-3 M€/an, pas un « détournement massif ».** C'est une goutte dans un groupe qui affiche 1,31 Md€ d'EBITDA renouvelables. Le pic 2022 (75,3 M€) était un événement unique de réorganisation (GAP-1 : abandon de créance/dividendes exceptionnels), pas un flux annuel.

## 3. La valeur capitalisée des contrats OA rachetés en 2019

- Le portefeuille Valeco (332 MW, ~620 GWh/an) génère ~50,8 M€/an de revenus OA bruts (82 €/MWh), dont ~21,7 M€/an d'écart au marché (subvention nette payée par le consommateur).
- **Capitalisation de cet écart : ~168 M€ (10 ans) à ~225 M€ (15 ans) à 5 %.**
- **Le prix de 229 M€ payé par EnBW (2019) est cohérent avec cette capitalisation** : EnBW a acheté, via Valeco, un portefeuille de flux futurs garantis par l'État français. Le vendeur (famille Gay + CDC) a monétisé la subvention publique future, et la CDC a encaissé un TRI de 28 % (20-36).
- **Nuance honnête :** la capitalisation de 168-225 M€ couvre une partie du prix (229 M€), le reste venant du pipeline (1 700 MW) et de la valeur de marché des actifs hors OA. Le « 87 Md€ d'engagements » du 20-42 est le total FRANCE (tous les contrats OA/CR), dont la part EnBW est marginale (332 MW sur un parc national de ~30 GW éoliens+solaires soutenus).

## 4. MANIPULATION_REPORT (15 symboles, notation -2 à +2)

| # | Symbole | Score | Justification |
|---|---------|-------|---------------|
| 1 | FLUX_RECURRENT | -1 | 2-3 M€/an seulement : pas un flux massif récurrent |
| 2 | PIC_2022 | +1 | 75,3 M€ unique (réorganisation), pas un flux annuel |
| 3 | CAPITALISATION_OA | +1 | 168-225 M€ d'écart au marché capitalisé, cohérent avec le prix |
| 4 | PRIX_229 | +1 | EnBW a payé la subvention future capitalisée |
| 5 | SOUVERAINETE | +2 | Argent public français → actionnaire public allemand |
| 6 | TRI_CDC | +1 | La CDC a encaissé 28 % sur la subvention capitalisée |
| 7 | PERTE_FISCALE | 0 | Fiscalité des dividendes intra-groupe non documentée |
| 8 | OPACITE_DIVIDENDES | +1 | Affectations non publiques (GAP-dv-1) |
| 9 | PART_MINORITAIRE | -1 | < 0,3 % de l'EBITDA renouvelables EnBW |
| 10 | PORTEFEUILLE_20 | +1 | 20+ filiales parcs = base de dividendes réelle |
| 11 | RENTE_LEGALE | +1 | Rente par conception (OA voté), pas corruption |
| 12 | PIPELINE | 0 | 1 700 MW : valeur hors OA non chiffrée |
| 13 | ENGAGEMENTS_87 | -1 | La part EnBW des 87 Md€ est marginale (332 MW) |
| 14 | CSPE_PAYEUR | +2 | Le consommateur français paie le flux |
| 15 | CONTRE-PREUVE | -1 | Flux 2-3 M€/an = goutte, pas « pompe massive » |

Score net : +7/30 (faisceau faible à modéré, direction « transfert de souveraineté réel mais quantitativement modeste »).

## 5. VERDICT (honnêteté forensique)

**1. Le flux de dividendes VALECO REN → EnBW est réel mais MODESTE : 2-3 M€/an (7,52 M€ cumulés 2023-2025),** dont ≥ 51 % vers EnBW. Le pic de 75,3 M€ (2022) était un événement unique de réorganisation (sortie du FPCI MIROVA, GAP-1), pas un flux annuel. La « pompe à dividendes » du 18-58 se confirme comme MÉCANISME (holding pure de dividendes, 20+ filiales) mais PAS comme volume massif.

**2. La valeur capitalisée est la vraie maille : EnBW a acheté en 2019 pour ~229 M€ un portefeuille dont 168-225 M€ correspondent à la capitalisation de l'écart de soutien public restant.** Le contribuable français finance, via la CSPE/accise, les flux qui ont été capitalisés au profit du cédant (famille Gay + CDC, TRI 28 %) puis continuent d'alimenter un actionnaire public allemand jusqu'à l'échéance des OA (2032 pour Puech del Vert).

**3. La part des « 87 Md€ d'engagements » imputable à EnBW est marginale :** 332 MW sur ~30 GW soutenus. Le chiffre des 87 Md€ ne doit pas être attribué à Valeco/EnBW : c'est l'ensemble du parc français.

**4. Charge correcte :** ce n'est pas un détournement (0 élément pénal), c'est un **transfert de souveraineté légal et quantifié** : la subvention publique française capitalisée a été monétisée au profit d'actionnaires dont un opérateur public étranger. Le vrai trou de contrôle reste le GAP du 21-10 (CRIM non captée, bouclier non recapté), pas les dividendes Valeco.

## 6. GAPS

| # | Gap | Voie |
|---|-----|------|
| GAP-dv-1 | Affectations des résultats VALECO REN 2023-2025 (distribution vs mise en réserve) | PV d'AG 2023-2026 au RCS Montpellier / Pappers payant |
| GAP-dv-2 | Sortie complète du FPCI MIROVA : date et modalités (rachat par VALECO SAS ?) | PV post-2022, rapports EnBW, GAP-1b du 20-26 |
| GAP-dv-3 | Dividendes réellement versés par les filiales parcs à VALECO REN | Comptes des SARL parcs, affectations |
| GAP-dv-4 | Valeur du pipeline Valeco (1 700 MW) dans le prix de 2019 | Analyse d'acquisition, presse spécialisée 2019 |
| GAP-dv-5 | Part exacte de la subvention capitalisée dans le prix (analyse DCF) | Modèle DCF interne EnBW (non public), estimation à affiner |

## 7. Traçabilité

- Scripts : /tmp/calc_valeco_flux.py (exécuté), fichiers Pappers/verif VALECO REN (/tmp/pappers_vren2.txt, pappers_vren3.txt, verif_vren.txt)
- Liens : 18-58 (chaîne), 20-26 (GAP-1, 75,3 M€), 20-36 (GAP-5, sortie CDC, TRI 28 %), 21-30 (régime OA PDV), 21-10 (GAP-flux-4, CRIM/bouclier), 20-42 (flux PDV)
- Em-dash : 0 (vérifié)
