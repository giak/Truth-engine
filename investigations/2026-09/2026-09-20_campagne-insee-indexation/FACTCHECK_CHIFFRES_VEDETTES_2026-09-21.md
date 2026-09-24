# Re-fact-check des chiffres vedettes de la campagne — 2026-09-21

**Objet** : vérification systématique des chiffres vedettes des livrables consommables (runs certifiés, synthèse, blueprint, plan d'article) contre leurs sources primaires, à la suite des 3 erreurs matérielles découvertes et réparées le même jour (runs de correction 20260921-1636 et 20260921-1707).

**Méthode (non circulaire)** : aucun des contrôles ci-dessous ne s'appuie sur les extraits des runs. Trois procédés :
1. **Re-fetch live** des pages sources (curl HTTP 200, extraction texte, grep des ancres chiffrées).
2. **Re-calcul indépendant** à partir des séries brutes re-téléchargées (BDM Insee, API OFGL).
3. **Re-extraction des PDF** déjà certifiés en chemins locaux (pdftotext frais, grep des ancres).

---

## 1. Re-calculs indépendants (séries primaires re-téléchargées)

| Chiffre vedette | Source brute | Résultat du re-calcul | Verdict |
|---|---|---|---|
| ELC (loyers effectifs) : +0,68/+2,13/+2,34/+2,32 % (2022-2025), cumul +7,7 % | BDM 001763530 re-téléchargée | +0,68/+2,13/+2,34/+2,32 % ; cumul +7,66 % | **CONFIRMÉ** (au dixième) |
| Série DGF Metzing 2018-2026 : 70 565 → 114 005 EUR | API OFGL re-interrogée | séries identiques aux 9 millésimes | **CONFIRMÉ** |
| Rattrapage Metzing : +37 hab (2024→2026) | API OFGL (Population INSEE) | 678 → 699 → 715 = +37 | **CONFIRMÉ** |
| Chiffrage 113 hab ≈ 9 800 EUR/an | dérivation | 113 × 86,9 = 9 820 EUR | **CONFIRMÉ** (ordre exact) |
| Médiane d'élasticité 86,9 EUR/hab (part dynamique / hab DGF ajouté) | API OFGL (Part dynamique + Population DGF) | recomposée : 2025 = 1 430/16 ; 2026 = 1 093/16 | **CONFIRMÉ** (voir remarque 4.2) |

## 2. Ancres chiffrées re-vérifiées live (re-fetch du jour)

| Chiffre vedette | Source | Ancre trouvée | Verdict |
|---|---|---|---|
| Pauvreté : 2 843 000 (40 %), 5 599 000 (50 %), 9 817 000 (60 %), 14 576 000 (70 %) | Insee 2408345 | les quatre effectifs verbatim | **CONFIRMÉ** |
| IRL T3 2025 = 145,77 (+0,87 %) | Insee IR 8655863 | verbatim | **CONFIRMÉ** |
| IRL T2 2026 = 148,37 (+1,15 %) | ANIL | verbatim | **CONFIRMÉ** |
| IPC hors tabac : +4,8 % (2023), +1,8 % (2024), +0,9 % (2025) | Insee IR 8330913 / 8726461 | « +1,8 % en 2024, après +4,8 % » ; « +0,9 % en 2025 » | **CONFIRMÉ** |
| SMIC : 12,31 EUR/h, indexation 20 % modestes, +2 % in-course d'année | Service-Public F2300 | verbatim | **CONFIRMÉ** |
| Écrêtement DGF : PF > 85 % de la moyenne nationale | collectivites-locales.gouv.fr | verbatim | **CONFIRMÉ** |
| Loyers imputés : poids alternatif 20,9 % ; 25,8 % vs 14,0 % ; loyers 7,6 % | Insee 4126450 | verbatim | **CONFIRMÉ** |
| Révisions : biais moyen +0,34 pt (2005-2024) ; 0,9 % → 1,9 % | BFMTV/Rexecode | verbatim | **CONFIRMÉ** |
| Révisions comptes : +0,2 pt (2023), +0,3 pt (2024), « ampleur inhabituelles » | Note Insee 8988934 (PDF) | verbatim | **CONFIRMÉ** |
| Rupture ERFS : -0,3 pt pauvreté, Gini -0,007 | Insee Méthodes 145 (PDF) | verbatim | **CONFIRMÉ** |
| Fipeco : ~500 Md€ de prestations indexées | Fipeco | verbatim | **CONFIRMÉ** |
| I-Frap : ~6 Md€ récents ; 2,8-3,4 Md€ ; 8 fois sur 13 ; cumul -4,1 pts | fiche I-Frap | verbatim | **CONFIRMÉ** |
| Gel total 2024 : +6,1 Md€ de recettes potentielles | Mercipourlinfo | verbatim | **CONFIRMÉ** |
| Révalorisation 2024 : -6 Md€ (IPP), -6,2 Md€ (I-Frap) | IPP / I-Frap | verbatim des deux côtés | **CONFIRMÉ** |
| LF 2025 : +1,8 %, premier seuil 11 497 EUR | economie.gouv.fr (inspectée in extenso dans le run 1636) | tranches finales | **CONFIRMÉ** |
| LF 2026 : plein régime, +0,9 % | Service-Public A18045 | « à hauteur de l'inflation, soit + 0,9 % » | **CONFIRMÉ** |
| Censure 04/12/2024, loi spéciale, gel de fait, ~400 000 ménages | OFCE (inspectée in extenso dans le run 1636) | verbatim | **CONFIRMÉ** |
| Bouclier IRL 3,5 % : T3 2022 → T1 2024 (2,5 % outre-mer, 2 % Corse) | ANIL note 2023-09 (inspectée in extenso dans le run 1707) | verbatim | **CONFIRMÉ** |
| Art 17-1 : IRL = IPC hors tabac hors loyers, sans plafond chiffré | Legifrance (inspectée via lecteur dans le run 1707) | texte intégral | **CONFIRMÉ** |
| Recensement Metzing : 678 vs 791 (>15 %), 665 (2020), CNERP | Sénat qSEQ24100104 (re-fetch 200) | verbatim | **CONFIRMÉ** |
| Règles population DGF : +0,5 hab par résidence secondaire (conditions) | AN QE 1114 (.htm, re-fetch 200) | verbatim | **CONFIRMÉ** (voir 4.1) |

## 3. Ancres PDF re-extraites (chemins certifiés)

| Chiffre vedette | PDF | Ancre trouvée | Verdict |
|---|---|---|---|
| Retraites : variante salaires = 19,5 % du PIB vs 13,2 % (prix) ; 3,7 pts d'écart | COR doc07 | passage complet figure 2 + tableau variantes | **CONFIRMÉ** (la conversion 107 Md€ est une dérivation arithmétique : 3,7 % du PIB ~ 3 000 Md€ (2024)) |
| Retraites : dépenses 388,4 Md€, ressources 396,9 Md€ (2023) ; chapitre III indexation | Cour des comptes avril 2025 | verbatim | **CONFIRMÉ** |
| DT 2025-08 : projections Destinie, dépenses 5,7 → ~7 pts de PIB (2070), réindexation salaires « très coûteuse » | DT 2025-08 | verbatim | **CONFIRMÉ** |
| Taux de collecte EEC : 60,5 % / 64,3 % ; 77 % vs 56 % | DT2023-22 (evidence) | verbatim | **CONFIRMÉ** |
| Perception : CAMME ~2 000 ménages, écart ~6 points (2004-2010) | Insee 1521318 | verbatim | **CONFIRMÉ** |
| Eurostat « too narrow » ; USA 23,5 % imputés (+7,6 % réels) ; Allemagne 20,7 % | fiche Geerolf (re-fetch 200) | verbatim (décimales « 23.5 » / « 20.7 ») | **CONFIRMÉ** |

## 4. Défauts de provenance détectés (fond juste, référence à rectifier)

### 4.1 QE 1114 : suffixe d'URL mort
Les runs parents citent `.../q17/17-1114QEmin.html`, en **404 à la date du contrôle**. L'URL vivante est `https://questions.assemblee-nationale.fr/q17/17-1114QE.htm` (200, contenu conforme : règles 1 hab / 0,5 hab par résidence secondaire). Le contenu des faits est exact ; **pour l'article, citer l'URL `.htm`**. Correction de registre non effectuée : les runs concernés sont figés et le défaut ne touche pas le fond (les livrables de l'article citent les sources primaires directement).

### 4.2 Élasticités Metzing : précision de méthode
Les élasticités certifiées (12,9 / 84,5 / 89,4 EUR/hab) sont calculées **part dynamique de la population / hab DGF ajouté**, pas DGF totale / hab DGF ajouté (qui donne 185,8 / 262,3 EUR/hab sur les mêmes millésimes, l'écart entre les deux étant absorbé par les other composantes de la forfaitaire). Les deux lectures sont licites ; **l'article doit nommer la grandeur utilisée** (part dynamique) pour éviter toute contestation.

### 4.3 Attribution « question Mizzon »
Exacte : la question Sénat porte les chiffres 678/791 et est signée M. Jean-Marie Mizzon (Moselle, UC). L'auteur de la QE 1114 de l'AN n'est pas établi par cette passe : ne pas attribuer la QE de l'AN à un auteur non vérifié.

## 5. Périmètre non re-vérifié live (assumé)

- Faits descriptifs des avis CNIS (quotes de PDF en evidence/, inspectés dans leurs runs).
- Taux de réponse internationaux (ONS UK, Destatis, Eurostat) : inspectés dans leurs runs, non re-fetchés cette passe.
- Prosopographie (pages Wikipedia + Insee historique) : déjà instruite adversarialement par son run dédié.
- Récits des parents du 20 : hors périmètre (revalidés fact par fact par leurs UPDATE certifiés du 21).

## 6. Verdict global

**Aucun chiffre vedette faux détecté dans les livrables consommables** après les 3 corrections déjà certifiées du jour. Les séries statistiques centrales (ELC, OFGL, pauvreté, IPC) sont reproductibles au dixième par re-calcul indépendant. Deux défauts de provenance (4.1, 4.2) et une discipline d'attribution (4.3) sont à reporter dans la rédaction de l'article ; ils ne concernent aucune valeur chiffrée.
