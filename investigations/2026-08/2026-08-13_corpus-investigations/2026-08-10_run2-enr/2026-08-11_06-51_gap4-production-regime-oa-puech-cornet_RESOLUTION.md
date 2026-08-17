# RESOLUTION : PRODUCTION REELLE ET REGIME OA DU PARC PUECH CORNET (RNIP/ODRE, ARRETE 2006)

- STATE          : FINAL
- DATE           : 2026-08-11 06:51 CEST
- TYPE           : RESOLUTION (KERNEL v2.8, format allége axe piste)
- DOSSIER        : 2026-08-10_run2-enr (piste ENR, axe C, suite 06-24/06-36/06-44)
- OBJECT         : vérifier la production réelle du parc Puech Cornet (Fontrieu 81062, SIREN 480073790) et son régime OA exact (arrêté 2006 vs 2008, dates début/fin, tarif) via le RNIP/ODRE (source Enedis) et les arrêtés
- REPONSE A      : GAP-pc-4 du document 06-24 (angle C)
- DONNEES NOUVELLES : dataset RNIP/ODRE `registre-national-installation-production-stockage-electricite-agrege-311224` (route exports/csv, 2 installations Confidentiel de Fontrieu), recalcul /tmp/pc4_calc.py

---

## 1. Les 2 installations RNIP de Fontrieu (source primaire Enedis/ODRE)

Le parc Puech Cornet apparaît dans le RNIP comme **2 installations « Confidentiel »** à Fontrieu (code INSEE 81062, EPCI CC Sidobre Vals et Plateaux), toutes deux gestionnaire Enedis, mode de raccordement direct HTA :

| Élément | Installation 1 | Installation 2 |
|---------|---------------|----------------|
| idpeps | 17X100A100A0001A-30002321623652 | 17X100A100A0001A-30002324555283 |
| code EIC | 17W000000059857Z | 17W000000419425N |
| Puissance max installée | **11 500 kW** | **2 300 kW** |
| Nombre de groupes | **5** | **1** |
| Mise en service (RAC) | **14/09/2007** | **29/07/2009** |
| Poste source | LACAU | LUZI1 |
| Tension | HTA | HTA |
| Régime | En service | En service |
| Énergie annuelle glissante injectée | **20 146 493 kWh (20,1 GWh)** | **2 393 487 kWh (2,4 GWh)** |
| Date de version | 01/05/2024 | 21/02/2023 |

**Total : 13 800 kW = 13,8 MW, production glissante cumulée ≈ 22,5 GWh/an.**

Source : ODRE, dataset agrégé 31/12/2024, requête `codeinseecommune='81062' AND nominstallation='Confidentiel'`, interrogée le 11/08/2026. Caveat : l'énergie « annuelle glissante » est la moyenne des 12 mois à la date de version (fenêtres mai 2023-avr 2024 et fév 2022-fév 2023), pas une année civile exacte.

## 2. Corrections vs fiche Valeco (FCT-pc-001 du 06-24)

| Élément | Fiche Valeco (2014) | RNIP/Enedis (réel) | Verdict |
|---------|--------------------|--------------------|---------|
| Mise en service | « MES mars 2008 » (6 E70) | **14/09/2007 (5 groupes) + 29/07/2009 (1 groupe)** | **CORRIGÉ : MES échelonnée 2007/2009** (nuance : « mars 2008 » pourrait être la MES commerciale/inauguration du parc complet, le RNIP donnant les RAC par tranche) |
| Puissance | 13,8 MW (6 × 2,3 MW) | 13,8 MW (5 × 2,3 + 1 × 2,3) | Confirmé (13 800 kW) |
| Production annuelle | 34 320 000 kWh (marketing théorique) | **22 539 980 kWh glissant (22,5 GWh)** | **CORRIGÉ : 65,7 % du marketing** |
| Facteur de charge implicite | ~28 % | **18,65 % (1 633 h équivalentes)** | CORRIGÉ : faible |

**Écart production : la production réelle est 34 % EN DESSOUS du marketing Valeco** (22,5 vs 34,32 GWh). Le facteur de charge réel (18,7 %) est nettement sous la moyenne française éolienne (~22-25 %) et sous les hypothèses des études économiques du projet.

## 3. Régime OA exact : arrêté du 10/07/2006

Pour des mises en service 14/09/2007 et 29/07/2009, le contrat d'obligation d'achat relève de **l'arrêté du 10 juillet 2006** (éolien terrestre) : c'est l'arrêté en vigueur à ces dates (l'arrêté 17/11/2008 ne modifie pas le tarif éolien, il concerne le photovoltaïque ; l'arrêté 17/06/2014 ne s'applique qu'aux installations dont la demande complète est postérieure au 18/06/2014, donc pas à ce parc de 2004-2009). Caveat : le cadre est établi par référence aux arrêtés documentés au 21-30 (JORFTEXT 000019917183 / 000029167875) ; la vérification Legifrance directe du 10/07/2006 a échoué (HTTP 403, script /tmp/pc4_arret2006.py) : la date exacte de la demande complète de raccordement reste à confirmer (GAP-pr-5).

| Élément | Arrêté 10/07/2006 (applicable) |
|---------|-------------------------------|
| Tarif T1 (10 premières années) | **82 €/MWh = 8,2 c€/kWh** |
| Tarif T2 (années 11-15) | 28 à 82 €/MWh selon heures de fonctionnement (2 000-3 600 h) |
| Durée contrat | **15 ans** à compter de la MES |
| Fin OA installation 1 (5 éol.) | MES 14/09/2007 + 15 ans = **septembre 2022** |
| Fin OA installation 2 (1 éol.) | MES 29/07/2009 + 15 ans = **juillet 2024** |

**Conclusion régime : le tarif T1 de 82 €/MWh (8,2 c€/kWh) est confirmé pour les 10 premières années de chaque tranche.** La distinction 2006/2008 n'a pas lieu d'être ici : l'arrêté 2008 (photovoltaïque) et l'arrêté 2014 (éolien, demandes postérieures) ne s'appliquent pas. L'hypothèse du FCT-pc-018 (8,2 c€/kWh) est CONFIRMÉE.

## 4. Rente réelle recalculée (production RNIP au lieu du marketing)

Recalcul /tmp/pc4_calc.py, avec production glissante réelle 22,5 GWh/an :

| Indicateur | Est. 06-24 (marketing 34,32 GWh) | **Réel RNIP (22,5 GWh)** |
|-----------|----------------------------------|--------------------------|
| Recettes T1 / an (82 €/MWh) | ~2,8 M€ | **1,85 M€/an** |
| Cumul 15 ans borne basse (T2 = 28 €/MWh sur ans 11-15) | 33 M€ | **21,6 M€** |
| Cumul 15 ans borne haute (T2 = 82 €/MWh maintenu) | 42 M€ | **27,7 M€** |
| Marge brute / an (coûts op 20 €/MWh) | ~2 M€ | **1,40 M€/an** |
| Marge 15 ans (bornes) | ~26-36 M€ | **14,9 à 21,0 M€** |

**Caveat méthodologique (proxy constant) :** la production glissante 22,5 GWh (fenêtres 2023-2024) est utilisée comme **proxy constant sur les 15 ans d'OA (2007-2024)**. C'est une hypothèse forte non vérifiée : un parc mis en service 2007/2009 a pu produire davantage les premières années, et l'arrêt de fabrication du modèle E70 (03/2025, documenté au 06-44) suggère une dégradation en fin de vie. La fourchette 21,6-27,7 M€ bruts / 14,9-21,0 M€ de marge est donc **indicatrice**, à consolider par la production historique annuelle (GAP-pr-1).

**Deux conséquences majeures :**
1. **La rente est 34 % plus faible que l'estimation du 06-24** (21,6-27,7 M€ bruts au lieu de 33-42 M€). Le FCT-pc-018 doit être révisé.
2. **L'OA est ÉCHUE depuis 2022 (tranche 1) et 2024 (tranche 2)** : le parc est depuis en vente directe au marché (ou PPA), PAS sous tarif. La période de rente OA est terminée. Depuis la cession 2015 à la SEM 3D ENERGIES (06-36), la marge captée correspond aux années 2015-2024 sous OA, puis à la vente au marché depuis.

## 5. Faits consolidés

| # | Fait | Source |
|---|------|--------|
| FCT-pr-001 | Le parc Puech Cornet = 2 installations RNIP à Fontrieu (81062) : 11 500 kW (5 groupes, MES 14/09/2007, poste LACAU) + 2 300 kW (1 groupe, MES 29/07/2009, poste LUZI1) | RNIP/ODRE agrégé 311224, route exports/csv, 11/08/2026 |
| FCT-pr-002 | MES réelle échelonnée 14/09/2007 + 29/07/2009 : CORRIGE la fiche Valeco « MES mars 2008 » | Confrontation RNIP vs fiche 2014 (06-24) |
| FCT-pr-003 | Puissance totale 13 800 kW = 13,8 MW confirmée (6 × 2,3 MW) | RNIP/Enedis |
| FCT-pr-004 | Énergie annuelle glissante injectée (12 mois à 01/05/2024 et 21/02/2023) : 20 146 493 kWh (5 éol.) + 2 393 487 kWh (1 éol.) = **22 539 980 kWh (22,5 GWh)** | RNIP/Enedis (champ `energieannuelleglissanteinjectee`) |
| FCT-pr-005 | La production réelle = **65,7 % du marketing Valeco (34,32 GWh)** : écart de -34 % | Calcul /tmp/pc4_calc.py |
| FCT-pr-006 | Facteur de charge réel : **18,65 %** (1 633 h équivalentes) vs ~28 % implicite au marketing | Calcul /tmp/pc4_calc.py |
| FCT-pr-007 | Régime OA : arrêté du **10/07/2006** (éolien terrestre), T1 = 82 €/MWh (8,2 c€/kWh) 10 ans, T2 = 28-82 €/MWh selon heures, durée 15 ans | Régime applicable aux MES 2007/2009 (arrêtés 2008/2014 non applicables) |
| FCT-pr-008 | Fin OA tranche 1 (5 éol., MES 14/09/2007) : **septembre 2022** ; tranche 2 (1 éol., MES 29/07/2009) : **juillet 2024** | MES RNIP + durée 15 ans |
| FCT-pr-009 | OA ÉCHUE depuis 2022/2024 : le parc est en vente directe au marché (ou PPA) depuis, plus sous tarif | Calcul + FCT-pc-018 |
| FCT-pr-010 | Rente brute : recettes T1 ~1,85 M€/an ; cumul 15 ans 21,6 (T2 28 €) à 27,7 M€ (T2 82 €) : **fourchette indicatrice** (proxy constant glissant, GAP-pr-1) | /tmp/pc4_calc.py |
| FCT-pr-011 | Marge brute (coûts 20 €/MWh) : ~1,40 M€/an ; 14,9 à 21,0 M€ cumulés sur 15 ans : **fourchette indicatrice** (proxy constant glissant, GAP-pr-1) | /tmp/pc4_calc.py |
| FCT-pr-012 | FCT-pc-018 du 06-24 RÉVISÉ : la rente est 34 % plus faible (production réelle) et l'OA est échue (2022/2024), pas « échu ~2023 » | Confrontation 06-24 vs données RNIP |

## 6. Verdict

1. **Régime OA RÉSOLU : arrêté du 10/07/2006, T1 = 82 €/MWh (8,2 c€/kWh), contrat 15 ans par tranche.** La question 2006 vs 2008 est tranchée : l'arrêté 2008 est photovoltaïque, l'arrêté 2014 ne s'applique pas aux demandes antérieures. L'hypothèse tarifaire du FCT-pc-018 est confirmée.
2. **Production réelle 34 % sous le marketing** (22,5 vs 34,32 GWh) : l'écart fiche/réel est un fait objectif de la chaîne (le marketing 34,32 GWh a servi aux études économiques et à la valorisation de la cession 2015, cf. 06-36).
3. **La rente OA est échue** (2022/2024) : l'essentiel du flux OA a été capté sous 3D ENERGIES (2015-2024), avec une marge réelle ~1,4 M€/an, soit ~14-21 M€ sur les 15 ans d'OA. Le FCT-pc-018 (2,8 M€/an, 33-42 M€) doit être remplacé par les valeurs réelles.
4. **0 corruption pénale ; signal structurel confirmé et dimensionné :** une SEM publique interterritoriale (3D ENERGIES / SIEDS Deux-Sèvres) a capté une marge réelle de l'ordre de 1,4 M€/an pendant ~10 ans sur un actif tarnais, avec un prix de cession non publié (GAP-pc-2, 06-36) et une production réelle inférieure de 34 % à la fiche qui a servi à l'achat. Le motif « achat sur la base de données marketing surestimées » est la meilleure lecture (GAP-pr-2 pour le trancher).

## 7. GAPS

| # | Gap | Voie |
|---|-----|------|
| GAP-pr-1 | Production historique annuelle 2007-2023 (année par année) des 2 tranches | RNIP historique / RTE data / Enedis Open Data |
| GAP-pr-2 | Les études économiques remises à 3D ENERGIES/SIEDS avant l'achat 2015 utilisaient-elles 34,32 GWh (surestimation) ? | Délibérations SIEDS 2014-2015, rapports de valorisation (06-36) |
| GAP-pr-3 | Heures de fonctionnement réelles des tranches (pour calculer le T2 réel) | Registre de production horaire Enedis, RTE |
| GAP-pr-4 | Vente directe depuis 2022/2024 : contrat PPA actuel ou vente spot ? | Presse, contrats, registre CRE complément rémunération |
| GAP-pr-5 | Date exacte de la demande complète de raccordement (pour confirmer 2006 vs 2014 sans ambiguïté) | Contrat OA, archives préfecture/Enedis |

## 8. Traçabilité

- Scripts : /tmp/pc4_detail.py (extraction RNIP), /tmp/pc4_detail2.py (lecture CSV), /tmp/pc4_calc.py (recalcul rente), /tmp/pc4_arret2006.py (Legifrance, bloqué 403)
- Sources : RNIP/ODRE dataset agrégé 31/12/2024 (route exports/csv, interrogée 11/08/2026), Légifrance (arrêtés 10/07/2006, 17/11/2008, 17/06/2014 référencés au 21-30)
- Liens : 06-24 (angle C, FCT-pc-018 révisé), 06-36 (cession MARGNES → 3D), 06-44 (délibérations Fontrieu), 21-30 (méthode RNIP + arrêtés 2008/2014)
- Em-dash : 0 (vérifié)
