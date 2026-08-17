# RESOLUTION : GAPs a3-2 / a3-5 / a3-3 DU FIL PUECH CORNET, SÉRIE DE PRIX 2021-2025, SÉRIE RNIP COMPLÈTE, SUIVI DU CONTRÔLE FISCAL

- STATE          : FINAL
- DATE           : 2026-08-11 11:26 CEST
- TYPE           : RESOLUTION (KERNEL v2.8, format allégé fil)
- DOSSIER        : 2026-08-10_run2-enr (fil Puech Cornet / 3D ENERGIES)
- OBJECT         : fermer les 3 GAPs résiduels de l'ANGLE 3 (10-55) : GAP-a3-2 (CA MARGNES 2022, exercice de crise), GAP-a3-5 (série de production par tranche), GAP-a3-3 (suivi du contrôle fiscal 3D dans les comptes 2025)
- SOURCES        : comptes MARGNES ENERGIE 2022 (KPMG, texte natif) et 2025 (dépôt RCS, OCR pages ciblées), RNIP/ODRE (9 versions agrégées, champs à plat), PV d'AG MARGNES 2025
- SCRIPTS        : /tmp/a3_extract2022.py, /tmp/a3_ocr2025.py, /tmp/a3_ocr2025b.py, /tmp/a3_rnip_final.py, /tmp/a3_g2_margnes2022.py

---

## 1. GAP-a3-2 : CA 2022 (exercice de crise) et sortie anticipée d'OA

Le compte MARGNES ENERGIE exercice 2022 (audité KPMG, texte natif) fournit le CA de l'année de crise et révèle une **correction majeure de la chronologie OA** :

- **CA 2021 = 2 196 908 € ; CA 2022 = 3 256 450 € (+48,2 %)**. Le CA 2022 (production vendue biens 3 231 057 € + services 25 392 €) est le plus élevé de la série connue.
- **Fait marquant 2022 : « Sortie du contrat d'obligation d'achat des parcs de Margnes et Singladou au 01/04/2022 »**. CORRECTION du FCT-pr-008 (06-51) qui estimait la fin d'OA par calcul (MES + 15 ans : t1 sept 2022, t2 juil 2024). La date réelle documentée par le compte est le **01/04/2022**, pour les deux parcs du groupe (Margnes ET Singladou) : sortie anticipée, vraisemblablement opportuniste (début de la crise des prix 2022, spot annuel 276 €/MWh).
- **Contribution sur la rente inframarginale** : la loi n°2022-1726 du 30/12/2022 (LF 2023) instaure rétroactivement une contribution sur la rente inframarginale « d'un montant égal à la fraction des revenus de marché excédant un seuil forfaitaire, de **100 €/MWh** » (seuil indiqué dans le compte pour ce parc).
- **Prix moyen implicite 2022 = 3 256 450 / 21 270 000 × 1000 ≈ 153 €/MWh** (production version 311222, fenêtre ~2022). Cohérent avec : janvier-mars 2022 en OA (82 €/MWh) + avril-décembre au marché de crise plafonné par la contribution (100 €/MWh) + incertitudes de fenêtre. Le niveau 153 €/MWh confirme que le parc a capté une partie du pic de crise malgré le plafonnement.

### Série de prix implicites complète 2021-2025 (CA / production fenêtres)

| Exercice | CA (€) | Production (GWh, fenêtre) | Prix implicite (€/MWh) | Contexte |
|----------|--------|---------------------------|------------------------|----------|
| 2021 | 2 196 908 | 22,90 | **96** | OA (jusqu'au 01/04/2022), tarif garanti |
| 2022 | 3 256 450 | 21,27 | **153** | Sortie OA 01/04/2022 + crise, plafond inframarginal 100 €/MWh |
| 2023 | 2 079 239 | 19,97 | **104** | Marché (spot annuel 97,2 €/MWh) |
| 2024 | 1 766 765 | 22,54 | **78** | Marché (spot annuel 58,0 €/MWh), écart +35 % vs spot |
| 2025 | 1 587 311 | 22,52 | **70** | Marché (spot 2025 non sourcé dans cette passe) |

Lecture : la sortie d'OA a relevé le prix moyen bien au-dessus du tarif garanti 82 €/MWh de 2022 à 2024, avant la retombée à 70 €/MWh en 2025 (baisse du marché). L'écart 2024 (+35 % vs spot) n'est pas reconduit en 2025 : si une couverture contractuelle a existé (INF-a3-002), elle ne se lit plus en 2025 (prix 70 €/MWh proche du marché attendu).

---

## 2. GAP-a3-5 : série de production par tranche (9 versions RNIP)

Les 9 versions annuelles du dataset RNIP agrégé (311217 à 311225) ont été interrogées pour Fontrieu (81062) avec les champs à plat (nom, filière, puissance, MES, énergie glissante injectée) :

| Version | Date version | t1 (11 500 kW, MES 14/09/2007) | t2 (2 300 kW, MES 29/07/2009) | Total (GWh) |
|---------|--------------|--------------------------------|-------------------------------|-------------|
| 311217 | 31/12/2017 | champ vide | champ vide | - |
| 311218 | 31/12/2018 | champ vide | champ vide | - |
| 311219 | 31/12/2019 | champ vide | champ vide | - |
| 311220 | 31/12/2020 | 21 170 868 | 2 854 690 | **24,03** |
| 311221 | 31/12/2021 | 20 478 159 | 2 420 897 | **22,90** |
| 311222 | 31/12/2022 | 18 716 201 | 2 551 762 | **21,27** |
| 311223 | 21/02/2023 | 18 171 821 | 1 798 509 | **19,97** |
| 311224 | 01/05/2024 | 20 146 493 | 2 393 487 | **22,54** |
| 311225 | 31/12/2025 | 19 870 753 | 2 648 501 | **22,52** |

- La série **confirme exactement les FCT-h-002/003/004 du 07-18** (moyenne 22,20 GWh/an, min 19,97 en 2023, max 24,03 en 2020) : aucun écart entre les deux lectures.
- **Constats d'absence structurels** : (a) versions 311217-311219 (2017-2019) : champ production vide dans le dataset (pas de mesure) ; (b) 2015-2016 : aucune version RNIP agrégé antérieure à 311217 + registres RTE 0 installation à Fontrieu (FCT-h-007) : pas de donnée pré-2020 ; (c) le RNIP agrégé n'existe qu'en **versions discrètes (~2/an)** : aucune publication mensuelle par installation, la série mensuelle 2015-2023 demandée par le GAP-a3-5 est **structurellement indisponible** en open data.

---

## 3. GAP-a3-3 : suivi du contrôle fiscal 3D dans le compte MARGNES 2025

Le compte MARGNES exercice 2025 (déposé au RCS, signé 25/06/2026, OCR des pages d'annexe) documente l'évolution du dossier fiscal :

- **Faits marquants 2025 (reprise intégrale de la provision)** : « La SAEML 3D Energie a fait l'objet d'un contrôle fiscal remettant en cause la durée d'amortissement des parcs éoliens (15 ans retenus, 20 ans selon l'administration). Cette décision est contestée par 3D ENERGIES. Une provision pour charge d'impôt sur les sociétés avait été constatée pour un total de **201 K€ en 2024. Cette provision a été totalement annulée en 2025** (reprise intégrale de 201 K€) liée au total des amortissements pratiqués sur les exercices 2023 à 2025 **inférieur au total des amortissements qui auraient été pratiqués sur 20 ans** selon le calcul de l'administration fiscale ».
- **Chronologie de la provision** : 247 K€ (2023) → 201 K€ (2024, après ajustement de -46 K€) → **0 (2025, annulation totale)**. Tableau des provisions 2025 : ligne « Pour impôts » = 200 890 €.
- **Le contrôle 3D reste en cours/contesté** : aucune issue définitive documentée dans le compte MARGNES 2025 ; l'annulation de la provision chez MARGNES ne clôt pas le contrôle au niveau 3D (tête de groupe).
- **PV d'AG 2025** : bénéfice 2025 = 784 309,94 € ; distribution de l'intégralité du bénéfice + report à nouveau créditeur = **dividende total 1 129 509,35 € (282,37 €/action)** versé à l'associé unique (3D ENERGIES) ; mention « capitaux propres reconstitués à un montant supérieur à la moitié du capital social » : MARGNES était passée sous la moitié du capital avant l'affectation (signal de capitaux propres dégradés, à dater).
- **Provision démantèlement** : 75 000 € par éolienne, 6 éoliennes (parc de Singladou inclus) = 450 000 € après actualisation 2020 ; « les éoliennes seront totalement amorties au 31/12/2031 ».

---

## 4. Table des faits

| # | Fait | Source |
|---|------|--------|
| FCT-a3b-001 | CA MARGNES 2021 = 2 196 908 € ; CA 2022 = 3 256 450 € (+48,2 %), plus haut de la série connue | compte MARGNES 2022 (KPMG, CR) |
| FCT-a3b-002 | Fait marquant 2022 : « Sortie du contrat d'obligation d'achat des parcs de Margnes et Singladou au 01/04/2022 » : CORRIGE le FCT-pr-008 (06-51) qui estimait t1 sept 2022 / t2 juil 2024 par MES + 15 ans | annexe compte MARGNES 2022 |
| FCT-a3b-003 | Loi n°2022-1726 du 30/12/2022 : contribution sur la rente inframarginale, seuil forfaitaire 100 €/MWh indiqué dans le compte pour ce parc | annexe compte MARGNES 2022 |
| FCT-a3b-004 | Prix implicite 2022 ≈ 153 €/MWh (3 256 450 / 21,27 GWh) | calcul, 11/08/2026 |
| FCT-a3b-005 | CA MARGNES 2025 = 1 587 311 € (vs 1 766 765 € en 2024, -10,2 %) ; prix implicite 2025 ≈ 70 €/MWh (22,52 GWh) | OCR compte MARGNES 2025 + calcul |
| FCT-a3b-006 | Série de prix implicites 2021-2025 : 96 / 153 / 104 / 78 / 70 €/MWh | synthèse CA/production |
| FCT-a3b-007 | Bénéfice 2025 = 784 309,94 € ; dividende total distribué = 1 129 509,35 € (282,37 €/action) = bénéfice + report à nouveau, versé à l'associé unique 3D ENERGIES | PV d'AG MARGNES 2025 (texte natif) |
| FCT-a3b-008 | Capitaux propres « reconstitués à un montant supérieur à la moitié du capital social » après affectation 2025 : MARGNES était sous la moitié du capital avant | PV d'AG MARGNES 2025 |
| FCT-a3b-009 | Provision IS MARGNES : 247 K€ (2023) → 201 K€ (2024, -46 K€ d'ajustement) → 0 (2025, annulation totale) | comptes MARGNES 2024 + OCR 2025 |
| FCT-a3b-010 | Annulation 2025 justifiée : amortissements réels pratiqués 2023-2025 (15 ans) inférieurs aux amortissements calculés sur 20 ans par l'administration : risque estimé nul chez MARGNES | OCR faits marquants compte 2025 |
| FCT-a3b-011 | Le contrôle fiscal de la SAEML 3D ENERGIES reste contesté : aucune issue définitive documentée dans le compte MARGNES 2025 | OCR compte 2025 |
| FCT-a3b-012 | Provision pour impôts au bilan 2025 = 200 890 € | OCR compte 2025 |
| FCT-a3b-013 | Provision démantèlement : 75 000 €/éolienne × 6 (Singladou inclus) = 450 000 € après actualisation 2020 ; éoliennes totalement amorties au 31/12/2031 | OCR compte 2025 |
| FCT-a3b-014 | Série RNIP 9 versions (2020-2025) par tranche : voir tableau §2 ; confirme exactement FCT-h-002/003/004 du 07-18 | RNIP/ODRE, 9 versions, 11/08/2026 |
| FCT-a3b-015 | Versions 311217-311219 (2017-2019) : champ production vide : pas de mesure de production dans le dataset | RNIP/ODRE |
| FCT-a3b-016 | 2015-2016 : aucune version RNIP agrégé avant 311217 + registres RTE 0 installation à Fontrieu : pas de donnée pré-2020 | RNIP/ODRE + 07-18 |
| FCT-a3b-017 | Le RNIP agrégé n'existe qu'en versions discrètes (~2/an) : pas de série mensuelle par installation en open data | catalogue ODRE |

## 5. Inférences et hypothèses

| # | Inférence / hypothèse | Statut |
|---|----------------------|--------|
| INF-a3b-001 | La sortie anticipée d'OA au 01/04/2022 (début de crise, spot 276 €/MWh) est une optimisation de la valeur par le groupe 3D : abandon du tarif garanti 82 €/MWh pour le marché, avec plafond inframarginal à 100 €/MWh | INFÉRENCE fondée sur FCT-a3b-002/003 |
| INF-a3b-002 | Le prix 2024 (78 €/MWh, +35 % vs spot) n'est pas reconduit en 2025 (70 €/MWh) : si une couverture contractuelle a existé, elle a expiré ou était partielle | INFÉRENCE (contrat non public) |
| INF-a3b-003 | L'annulation de la provision chez MARGNES (calcul favorable) ne clôt pas le contrôle au niveau 3D, qui reste contesté : le risque fiscal est porté par la tête de groupe, non provisionné dans ce compte | INFÉRENCE |

## 6. GAPs résiduels

| # | Question ouverte | Piste |
|---|------------------|-------|
| GAP-a3b-1 | Montant effectif de la contribution inframarginale versée en 2022 (dette d'IS, calcul) | compte MARGNES 2023 + détail charge d'impôt 2022 |
| GAP-a3b-2 | PV du contrôle fiscal 3D ENERGIES (période, montants redressés, issue) | comptes 2025 de 3D (à déposer), presse, registres fiscaux |
| GAP-a3b-3 | Tarif T2 exact de l'arrêté OA 2006 (pour interpréter le prix implicite 2021 = 96 €/MWh) | Légifrance arrêté 10/07/2006 (bloqué 403 en session), archive |
| GAP-a3b-4 | Date et cause de la dégradation des capitaux propres de MARGNES (passage sous la moitié du capital) | comptes 2021-2023, rapport de gestion |
| GAP-a3b-5 | Nature du contrat de vente 2022-2024 (contrepartie, prix, durée) | presse spécialisée, documents SIEDS/3D (GAP-a3-1 inchangé) |

## 7. Verdict

1. **GAP-a3-2 RÉSOLU** : CA 2022 = 3 256 450 € (+48,2 % vs 2021), sortie anticipée d'OA au **01/04/2022** (correction du 06-51), prix implicite 2022 ≈ 153 €/MWh avec plafond inframarginal à 100 €/MWh. La série de prix 2021-2025 (96/153/104/78/70 €/MWh) est complète.
2. **GAP-a3-5 RÉSOLU** : série annuelle 2020-2025 par tranche confirmée sur 9 versions RNIP (identique au 07-18) ; constats d'absence structurels pour 2015-2019 (aucune donnée pré-2020) et pour le mensuel (RNIP = versions discrètes).
3. **GAP-a3-3 RÉSOLU** : provision fiscale **247 → 201 → 0 K€** (annulée en 2025), contrôle 3D toujours contesté (aucune issue), dividende 2025 de **1 129 509 €** versé à 3D ENERGIES, capitaux propres de MARGNES passés sous la moitié du capital avant reconstitution.
4. **Signal consolidé du fil** : le groupe 3D ENERGIES a optimisé la valeur du parc pendant la crise (sortie d'OA anticipée + plafonnement de l'État), puis le prix est redescendu avec le marché. Le dossier fiscal (durée d'amortissement) est clos comptablement chez MARGNES (provision annulée) mais le contrôle 3D reste ouvert. La chaîne de captage (dividendes 1,13 M€ 2025 vers 3D → SIEDS/SEOLIS) continue.

## 8. Caveats

- Prix implicites : production en fenêtres glissantes (pas années civiles exactes) et CA incluant ~1-5 % de services : approximations centrées.
- Spot 2025 non sourcé dans cette passe (le prix implicite 2025 = 70 €/MWh est comparé au marché attendu, pas à une moyenne annuelle vérifiée).
- La sortie d'OA au 01/04/2022 est documentée par le compte (source primaire comptable) ; la cause exacte (résiliation anticipée consentie, demande du producteur) n'est pas précisée dans le compte.
- OCR du compte 2025 : chiffres clés relus, mais coquilles OCR possibles sur les montants annexes (recalculés par recoupement quand possible).
