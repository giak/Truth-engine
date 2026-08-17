# RESOLUTION : REGIME OA EXACT DU PUECH DEL VERT (RNIP/ENEDIS, ARRETES TARIFAIRES)

- STATE          : FINAL
- DATE           : 2026-08-10 21:30 CEST
- TYPE           : RESOLUTION (KERNEL v2.8, format allégé axe piste)
- DOSSIER        : 2026-08-10_run2-enr (piste ENR, axe A, suite 20-42/21-10)
- OBJECT         : vérifier le régime exact du contrat d'obligation d'achat du Puech del Vert (arrêté 17/11/2008 vs 17/06/2014, option AO, tarif, durée) via le registre RNIP/Enedis et les textes
- REPONSE A      : GAP-flux-1 du document 20-42 (suggéré en priorité)
- DONNEES NOUVELLES : dataset RNIP/Enedis agrege 31/12/2024 (archivé data/rnip_couffrau_ARCHIVE.md + data/rnip_couffrau_barre.csv + data/rnip_lacaune.csv), API recherche-entreprises.data.gouv.fr, Légifrance (arrêtés 2008/2014)

---

## 1. Découverte majeure : le parc Puech del Vert est à BARRE, pas Lacaune, et la MES est 2017

| Élément | Valeur RNIP (source primaire Enedis) | Dossier antérieur | Verdict |
|---------|--------------------------------------|-------------------|---------|
| Nom | COUFFE05 - ADP 05 DE LA FERME EOLIENNE DE COUFFRAU (PUECH DEL VERT) | « Puech del Vert, Lacaune » | Nom confirmé |
| Commune | **BARRE (code INSEE 81023, Tarn)** | Lacaune (dossier 18-51) | **CORRIGÉ : Barre** |
| Puissance | 11 500 kW (11,5 MW) | ~11,5 MW | Confirmé |
| Mise en service | **10/05/2017** | MES 2012 (18-51) / MES 2017 (chercheur 20-42) | **CORRIGÉ : 10/05/2017, RNIP tranche** |
| idpeps | RTE-COUFFE05000000000000006880 | - | Nouveau |
| Production 2024 | 24 202 829 kWh (24,2 GWh) | estimation 22 GWh (20-42) | **CORRIGÉ : 24,2 GWh (facteur ~24 %)** |
| Gestionnaire | Enedis | - | - |

Source : ODRE, dataset `registre-national-installation-production-stockage-electricite-agrege-311224`, route exports/csv interrogée le 10/08/2026 (archivé dans data/).

## 2. Le complexe éolien de Couffrau (Barre) : 6 ADP + 2 installations anciennes

| idpeps | Parc | MES | Puissance (MW) | Prod 2024 (GWh) |
|--------|------|-----|----------------|-----------------|
| COUFFE01 | LA BESSIERE | (vide, ancien) | 13,8 | 29,1 |
| COUFFE02 | PUECH DE L HOMME | (vide, ancien) | 16,1 | 44,2 |
| COUFFE03 | MURASSON | (vide, ancien) | 2,3 | 5,6 |
| COUFFE04 | MURATEL | (vide, ancien) | 11,5 | 25,9 |
| **COUFFE05** | **PUECH DEL VERT** | **10/05/2017** | **11,5** | **24,2** |
| COUFFE06 | BOIS DE MERDELOU | 10/05/2017 | 16,1 | 51,6 |
| (Confidentiel) | 2 installations | 2007 | 15 + 9 | 15,7 + 5,8 |

**FAIT NOUVEAU STRUCTURANT :** COUFFE06 BOIS DE MERDELOU (16,1 MW, 51,6 GWh, MES 10/05/2017) est le parc objet de l'apport partiel d'actif vers DAHLIA HOLDING documenté au GAP-1 (20-26). Le Puech del Vert et le Bois de Merdelou font partie du MÊME complexe Couffrau, tous deux MES 10/05/2017, tous deux sociétés Valeco (siège Montpellier).

## 3. SIREN des sociétés d'exploitation (API recherche-entreprises.data.gouv.fr, 10/08/2026)

| Société | SIREN | Siège | Création |
|---------|-------|-------|----------|
| FERME EOLIENNE DE PUECH DEL VERT | **495 300 600** | Montpellier | 01/04/2007 |
| FERME EOLIENNE DU BOIS DE MERDELOU | **494 229 396** | Montpellier | 05/02/2007 |

Le complexe Couffrau n'a PAS de société unique au RNE (recherche « ferme eolienne de couffrau » = 0 résultat) : chaque ADP est une société distincte. Ceci CONFIRME la structure SPV par parc documentée au 18-30 (gérant Daumard, président Valeco) et au 17-52 (axe B : SPV × contrats × RBE).

## 4. Régime tarifaire : arrêté 17/11/2008 vs 17/06/2014 (Légifrance, confirmé)

| Élément | Arrêté 17/11/2008 | Arrêté 17/06/2014 | Impact PDV |
|---------|-------------------|-------------------|------------|
| Tarif T1 (10 premières années) | **82 €/MWh** (8,2 c€/kWh) | **82 €/MWh** (8,2 c€/kWh) | Identique dans les deux cas |
| Durée contrat | 15 ans | 15 ans | 2017 → 2032 |
| Tarif T2 (années 11-15) | 28 à 82 €/MWh selon heures (2000-3600 h) | 28 à 82 €/MWh selon heures | Variable selon heures |
| Option S2 (arrêté 2014) | - | ~72 €/MWh (jusqu'à 74 selon rotor) | Non retenue (hypothèse) |
| Clause de transition | - | Art. 3 : demande complète avant 18/06/2014 → arrêté 2008 | Dépend de la date de demande |

URLs : JORFTEXT000019917183 (2008), JORFTEXT000029167875 (2014), JORFTEXT000019996802 (2008, annexe T1).

**Conclusion :** pour un parc MES 10/05/2017, le tarif T1 applicable est **82 €/MWh dans les deux régimes** (transition 2008 si demande complète antérieure à juin 2014, sinon 2014). Le GAP-flux-1 sur le T1 est RÉSOLU : l'hypothèse du 20-42 (82 €/MWh T1) est **confirmée à la source**. La distinction 2008/2014 ne change QUE le T2 (années 11-15), dont l'impact sur le flux est faible.

## 5. Incohérence du 18-58 RÉSOLUE

Le 18-58 (FCT-ch1-018) notait : « le PPA 2021 dit OA échue, or PDV MES 2012 + 15 ans = 2027 : incohérence ».

**Résolution :** la MES réelle de PDV est 10/05/2017 (RNIP), pas 2012. L'OA court donc jusqu'en **2032**, pas 2027. Le PPA 2021 (Solvay/ilek) couvre les parcs ANCIENS du complexe (COUFFE01-04, MES 2006-2013, OA échue 2021-2028), pas le Puech del Vert ni le Bois de Merdelou (MES 2017, OA encore en cours). L'hypothèse « 2 parcs plus anciens » du 18-58 est CONFIRMÉE : les 2 parcs du PPA sont parmi COUFFE01-04, pas PDV/BDM.

**Conséquence sur la chaîne :** les parcs du PPA 2021 (Solvay, industriel belge) sont les parcs anciens ; le Puech del Vert reste sous OA 82 €/MWh jusqu'en 2032, alimentant la chaîne VALECO REN → VALECO SAS → EnBW.

## 6. Recalcul du flux avec données réelles (script /tmp/calc_pdv_v2.py)

| Période | Flux net |
|---------|----------|
| 2017-2026 (10 ans T1 82 €/MWh, prod 24,2 GWh) | -0,56 M€ (l'État perçoit au net) |
| 2017-2031 (15 ans, T2 28 €/MWh hypothèse basse) | **-5,64 M€ (l'État perçoit au net)** |
| Pic 2022 seul | -4,69 M€ (prix 276 €/MWh) |

**Conclusion confirmée et renforcée :** même avec la production réelle RNIP (24,2 GWh, +10 % vs l'estimation), le solde net sur 15 ans est NÉGATIF pour le consommateur : -5,64 M€. Le parc ne « vole » pas le contribuable au net ; la crise 2022 a tout remboursé. La conclusion du 20-42 tient.

## 7. Faits consolidés

| # | Fait | Source |
|---|------|--------|
| FCT-oa-001 | Puech del Vert = COUFFE05, commune BARRE (81023), 11,5 MW, MES 10/05/2017, idpeps RTE-COUFFE05000000000000006880 | RNIP/Enedis (dataset agrege 311224) |
| FCT-oa-002 | Production 2024 réelle : 24,2 GWh (24 202 829 kWh), facteur de charge ~24 % | RNIP/Enedis, même source |
| FCT-oa-003 | Le dossier 18-51 (Lacaune/MES 2012) est CORRIGÉ : commune Barre, MES 2017 | Confrontation RNIP vs 18-51 |
| FCT-oa-004 | Complexe Couffrau = 6 ADP (COUFFE01-06) + 2 installations 2007, ~95 MW à Barre | RNIP/Enedis |
| FCT-oa-005 | COUFFE06 BOIS DE MERDELOU (16,1 MW, 51,6 GWh, MES 2017) = parc de l'apport DAHLIA HOLDING (GAP-1, 20-26) : même complexe que PDV | RNIP + 20-26 |
| FCT-oa-006 | SIREN FERME EOLIENNE DE PUECH DEL VERT = 495300600, Montpellier, créée 01/04/2007 | API recherche-entreprises.data.gouv.fr |
| FCT-oa-007 | SIREN FERME EOLIENNE DU BOIS DE MERDELOU = 494229396, Montpellier, créée 05/02/2007 | API recherche-entreprises.data.gouv.fr |
| FCT-oa-008 | Aucune société « Couffrau » au RNE : chaque ADP est une société distincte (structure SPV par parc) | API recherche-entreprises (0 résultat) |
| FCT-oa-009 | Tarif T1 arrêté 2008 : 82 €/MWh (8,2 c€/kWh) pendant 10 ans, contrat 15 ans | Légifrance JORFTEXT000019917183 + 000019996802 |
| FCT-oa-010 | Tarif T1 arrêté 2014 : 82 €/MWh pendant 10 ans, contrat 15 ans ; option S2 ~72 €/MWh ; clause de transition art. 3 | Légifrance JORFTEXT000029167875 |
| FCT-oa-011 | Pour MES 2017 : T1 = 82 €/MWh dans les deux régimes (2008 par transition ou 2014) | Analyse croisée art. 3 + tarifs |
| FCT-oa-012 | OA PDV court 2017 → 2032 (pas 2027) : l'incohérence du 18-58 est résolue | RNIP (MES 2017) + durée 15 ans |
| FCT-oa-013 | Les parcs du PPA 2021 (Solvay) sont parmi COUFFE01-04 (MES 2006-2013, OA échue) : pas PDV/BDM | RNIP + 18-58 |
| FCT-oa-014 | Flux net cumulé PDV 2017-2031 avec prod réelle : -5,64 M€ (État perçoit) | Recalcul /tmp/calc_pdv_v2.py |
| FCT-oa-015 | Pic 2022 : -4,69 M€ pour l'État (prix 276 €/MWh vs tarif fixe 82) | Recalcul, prix RTE 2022 |

## 8. Verdict

1. **Régime OA du Puech del Vert RÉSOLU :** arrêté tarifaire 2008 ou 2014 selon la date de demande complète (indéterminable sans le contrat), mais le **T1 est 82 €/MWh dans les deux cas** : l'hypothèse du 20-42 est confirmée, le calcul du flux est robuste.
2. **Découvertes structurantes :** (a) le parc est à Barre, pas Lacaune (correction du 18-51) ; (b) MES 2017 (correction), OA jusqu'en 2032 ; (c) le Puech del Vert et le Bois de Merdelou (apport DAHLIA) sont dans le même complexe Couffrau : la réorganisation 2021-2022 du GAP-1 concerne des parcs jumeaux du même site.
3. **Le flux reste NÉGATIF pour le consommateur au net (-5,64 M€)** : la conclusion anti-sycophancie du 20-42 tient, même avec la production réelle.
4. **Angle vivant :** le T2 (années 11-15, 2027-2032) dépend des heures de fonctionnement : si le parc tourne > 3 600 h, le T2 est proche de 82 €/MWh, pas 28 €/MWh. La production RNIP (24,2 GWh pour 11,5 MW = ~2 100 h) suggère un T2 faible, mais à vérifier (GAP-oa-1).

## 9. GAPS

| # | Gap | Voie |
|---|-----|------|
| GAP-oa-1 | Heures de fonctionnement réelles du PDV (pour le T2 2027-2032) | RTE data, registre de production horaire |
| GAP-oa-2 | Date exacte de la demande complète de raccordement (pour trancher 2008 vs 2014) | Contrat OA EDF OA, demande CADA CRE |
| GAP-oa-3 | Liste des parcs du PPA 2021 (Solvay) : lesquels exactement parmi COUFFE01-04 | Communiqué PPA, presse 2021 |
| GAP-oa-4 | Dividendes de la SARL PDV 2017-2026 vers VALECO REN (affectations) | Comptes déposés TC Montpellier |
| GAP-oa-5 | Production réelle PDV 2017-2023 (année par année) | RNIP historique / RTE |

## 10. Traçabilité

- Artefacts RNIP : data/rnip_couffrau_ARCHIVE.md, data/rnip_couffrau_barre.csv, data/rnip_lacaune.csv (dataset ODRE agrege 311224, extraction 10/08/2026)
- Scripts : /tmp/calc_pdv_v2.py (flux), /tmp/archive_rnip_couffrau.md
- Sources : RNIP/Enedis (ODRE), API recherche-entreprises.data.gouv.fr, Légifrance (JORFTEXT 000019917183 / 000029167875 / 000019996802)
- Liens : 20-42 (flux), 21-10 (GAP-flux-4), 20-26 (GAP-1 DAHLIA), 18-51 (carte Tarn, corrigé), 18-58 (chaîne, incohérence résolue), 17-52 (SPV), 18-30 (SIREN)
- Em-dash : 0 (vérifié)
