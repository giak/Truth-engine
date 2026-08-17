# RESOLUTION : AFFECTATIONS DES RESULTATS VALECO REN 2023-2025 (GAP-dv-1)

- STATE          : FINAL
- DATE           : 2026-08-10 21:36 CEST
- TYPE           : RESOLUTION (KERNEL v2.8)
- DOSSIER        : 2026-08-10_run2-enr
- OBJECT         : lire les PV d'AG 2023-2026 de VALECO REN (affectations des résultats 2022-2025) pour confirmer les dividendes réellement versés vers VALECO SAS, puis EnBW (51 %) et KlimaVest (49 %)
- LIENS          : 21-50 (dividendes, estimation 2-3 M/an), 22-05 (sortie MIROVA, KlimaVest), 20-26 (GAP-1, 75,3 M 2022), 21-30 (régime OA PDV), GAP-dv-3 (dividendes filiales parcs)
- SOURCES        : Pappers (page entreprise 434054318, liste des actes + agrégats financiers 2022-2025), API recherche-entreprises (RN 2024 = 2 328 837 EUR), societe.com (annonce JAL, capital 2 125 500 EUR), INPI data (liste documents, bloqué Cloudflare), registre RNE (bloqué Cloudflare)

## 1. CONSTAT D'ABSENCE : LES PV D'AG NE SONT PAS AU RCS

Fait juridique vérifié sur la liste des actes déposés (Pappers, source INPI/RNE) :

| # | Acte | Date |
|---|------|------|
| 1 | Renouvellement(s) de mandat(s) de commissaire(s) aux comptes | 27/02/2023 |
| 2 | Reconstitution de l'actif net | 07/07/2022 |
| 3 | Poursuite d'activité malgré un actif net < moitié du capital | 04/09/2020 |
| 4 | Nomination de directeur général / changement de président | 09/08/2019 |
| 5 | Document inconnu | 31/10/2017 |
| 6 | Refonte des statuts | 05/10/2016 |
| 7 | (Transformation en SAS 2016, statuts, capital 2001-2016) | 2001-2016 |

- **Le dernier acte déposé au RCS date du 27/02/2023.** Aucun PV d'AG, aucune décision d'affectation des résultats 2022-2025 n'est déposée.
- **Cause structurelle : VALECO REN est une SAS depuis le 11/02/2016** (transformation documentée). Pour une SAS, les décisions d'affectation du résultat (approbation des comptes, distribution) sont prises par l'associé unique ou la collectivité des associés **sans obligation de dépôt au RCS**. Seuls les actes modifiant les statuts, le capital, les dirigeants ou les commissaires aux comptes sont déposés.
- Les comptes sociaux (bilans) sont en revanche **déposés chaque année, 2016 à 2025** (listés sur Pappers, PDF derrière Cloudflare : data.inpi.fr et pappers.fr bloquent les téléchargements automatisés ; les agrégats sont visibles).

## 2. RECONSTITUTION PAR DELTA DES FONDS PROPRES (BILANS DEPOSES)

Données publiques (Pappers, bilans déposés) :

| Exercice | Fonds propres fin (M EUR) | Résultat net (M EUR) |
|----------|---------------------------|----------------------|
| 2022 | 78,5 | 75,3 (exceptionnel, réorganisation GAP-1) |
| 2023 | 54,8 | 3,11 |
| 2024 | 52,6 | 2,33 (API : 2 328 837 EUR exact) |
| 2025 | 54,7 | 2,08 |

Méthode : FP(n) = FP(n-1) + RN(n) - DIST(n) + autres mouvements. Hypothèse : aucun autre mouvement de capitaux propres (aucun acte d'augmentation de capital déposé 2023-2025 ; dernier acte = renouvellement CAC 27/02/2023).

| Exercice | Calcul | Distribution reconstituée |
|----------|--------|---------------------------|
| 2023 | 78,5 + 3,11 - 54,8 | **+26,81 M EUR** |
| 2024 | 54,8 + 2,33 - 52,6 | **+4,53 M EUR** |
| 2025 | 52,6 + 2,08 - 54,7 | **-0,02 M EUR (≈ 0)** |

**Total 2023-2025 : ~31,3 M EUR distribués**, dont :
- vers EnBW via VALECO SAS (51 %) : ~15,97 M EUR
- vers KlimaVest ELTIF (49 %) : ~15,35 M EUR

## 3. CORROBORANT COMPTABLE : RESORPTION DU BFR HORS EXPLOITATION

| Exercice | BFR hors exploitation (M EUR) | Variation |
|----------|-------------------------------|-----------|
| 2022 | 23,1 | - |
| 2023 | 0,931 | **-22,17 M EUR (encaissement)** |
| 2024 | 0,604 | -0,33 |
| 2025 | 1,46 | +0,86 |

- Le BFR hors exploitation 2022 de 23,1 M EUR (créances sur filiales, très probablement dividendes à recevoir des parcs) **se résorbe en 2023 (+22,2 M EUR d'encaissement)**, exactement l'année de la distribution massive reconstituée (26,8 M EUR).
- La trésorerie reste stable (3,36 M EUR en 2022 → 3,67 M EUR en 2023) : la distribution a été financée par l'encaissement des créances filiales + le RN 2023, pas par la trésorerie.
- **Cohérence de bout en bout** : les filiales parcs remontent leurs dividendes à VALECO REN (créances 2022, encaissées 2023), qui redistribue ~26,8 M EUR à ses actionnaires (VALECO SAS 51 % + KlimaVest 49 %).

## 4. CORRECTION DU 21-50 (ANTI-SYCOPHANCIE)

- Le 21-50 estimait **2-3 M EUR/an** de dividendes potentiels (7,52 M EUR cumulés 2023-2025 si distribution à 100 % du RN).
- **La reconstitution montre un flux réel ~4 fois supérieur : ~31,3 M EUR**, concentré sur **2023 (26,8 M EUR)**, année charnière : sortie de MIROVA (nov. 2022, cession à KlimaVest) + résultat exceptionnel 2022 (75,3 M EUR, réorganisation GAP-1).
- La distribution 2023 de 26,8 M EUR sur le résultat 2022 de 75,3 M EUR = taux de distribution de ~36 % la première année, le solde (48,5 M EUR) restant en réserves (FP 2023 = 54,8 M EUR dont réserves).

## 5. LIMITES ET GAPS RESIDUELS

1. **Le delta des fonds propres est une inférence**, pas une pièce directe : il isole les mouvements de capitaux propres nets. L'hypothèse « aucun autre mouvement » est étayée par l'absence d'actes déposés, mais les PV d'AG (seule preuve directe) ne sont pas publics pour une SAS.
2. **GAP-dv-1a** : obtenir les décisions d'affectation via le RCS papier / infogreffe payant, ou une demande CADA auprès du greffe (si considéré administratif), ou les rapports du commissaire aux comptes.
3. **GAP-dv-3 (lié)** : la répartition entre filiales parcs (PDV, Bois de Merdelou, etc.) qui ont généré les 23,1 M EUR de créances 2022 reste à documenter (comptes des SARL parcs, RNIP).
4. **Le 75,3 M EUR (2022)** : sa composition exacte (apport Bois de Merdelou → DAHLIA HOLDING, plus-values) est documentée au 20-26 ; son affectation (réserve vs distribution) reste en partie inférée.

## 6. FAITS (FCT-dv1)

| # | Fait | Source | Date |
|---|------|--------|------|
| FCT-dv1-001 | Le dernier acte déposé au RCS de VALECO REN date du 27/02/2023 (renouvellement CAC) | Pappers/INPI (liste des actes) | 2026 |
| FCT-dv1-002 | Aucun PV d'AG ni décision d'affectation 2023-2026 déposé au RCS | Pappers (23 actes listés, dernier 2023) | 2026 |
| FCT-dv1-003 | VALECO REN est une SAS depuis la transformation du 11/02/2016 | Actes Pappers (rapport commissaire à la transformation) | 2026 |
| FCT-dv1-004 | Pour une SAS, les décisions d'affectation du résultat ne sont pas déposées au RCS (pas d'obligation légale) | Droit des sociétés (L. 227-1 s. code de commerce), constat registre | 2026 |
| FCT-dv1-005 | Les comptes sociaux (bilans) sont déposés chaque année 2016-2025 | Pappers (liste comptes 2016-2025) | 2026 |
| FCT-dv1-006 | Fonds propres VALECO REN : 78,5 M (2022), 54,8 M (2023), 52,6 M (2024), 54,7 M (2025) | Pappers (agrégats bilans) | 2026 |
| FCT-dv1-007 | Résultat net : 75,3 M (2022), 3,11 M (2023), 2,33 M (2024), 2,08 M (2025) | Pappers + API recherche-entreprises (2024 = 2 328 837 EUR) | 2026 |
| FCT-dv1-008 | Delta FP 2023 : 78,5 + 3,11 - 54,8 = 26,81 M EUR distribués en 2023 | Calcul sur bilans déposés | 2026 |
| FCT-dv1-009 | Delta FP 2024 : 54,8 + 2,33 - 52,6 = 4,53 M EUR distribués en 2024 | Calcul sur bilans déposés | 2026 |
| FCT-dv1-010 | Delta FP 2025 : 52,6 + 2,08 - 54,7 = -0,02 M EUR (≈ 0) | Calcul sur bilans déposés | 2026 |
| FCT-dv1-011 | Total distributions 2023-2025 : ~31,3 M EUR (dont 26,8 M EUR en 2023) | Calcul | 2026 |
| FCT-dv1-012 | BFR hors exploitation 2022 = 23,1 M EUR, résorbé à 0,931 M EUR en 2023 (+22,2 M EUR encaissés) | Pappers (agrégats bilans) | 2026 |
| FCT-dv1-013 | Trésorerie stable 2022-2023 (3,36 → 3,67 M EUR) : la distribution 2023 est financée par l'encaissement des créances filiales | Pappers | 2026 |
| FCT-dv1-014 | Flux vers EnBW via VALECO SAS (51 %) : ~15,97 M EUR cumulés 2023-2025 | Calcul (répartition 51/49, actes 22-05) | 2026 |
| FCT-dv1-015 | Flux vers KlimaVest (49 %) : ~15,35 M EUR cumulés 2023-2025 | Calcul (répartition 51/49, actes 22-05) | 2026 |
| FCT-dv1-016 | Capital social VALECO REN : 2 125 500 EUR (annonce JAL, décision 25/06/2020 perte capitaux propres) | societe.com (annonce légale) | 2026 |

## 7. VERDICT

**Le GAP-dv-1 est RÉSOLU par reconstitution comptable (confiance élevée, inférence sur pièces publiques) :**
- Les PV d'AG 2023-2026 ne sont **pas publics** (SAS, pas de dépôt) : constat d'absence définitif aux données ouvertes.
- Mais les bilans déposés permettent de reconstituer : **~31,3 M EUR distribués 2023-2025, dont un pic de 26,8 M EUR en 2023** (~36 % du résultat exceptionnel 2022 de 75,3 M EUR), corroboré par la résorption de 22,2 M EUR de créances filiales la même année.
- **Correction du 21-50 : le flux réel est ~4 fois supérieur à l'estimation initiale (2-3 M EUR/an).** La chaîne « filiales parcs → VALECO REN → VALECO SAS → EnBW/KlimaVest » transporte ~31 M EUR sur 3 ans, pas 7,5 M EUR.
- Verdict global inchangé sur la qualification : transfert de souveraineté légal, 0 corruption pénale, mais **l'ordre de grandeur du flux public capté par des actionnaires allemands (EnBW Land de Bade-Wurtemberg + Commerzbank via KlimaVest) est nettement plus élevé que documenté au 21-50**.
