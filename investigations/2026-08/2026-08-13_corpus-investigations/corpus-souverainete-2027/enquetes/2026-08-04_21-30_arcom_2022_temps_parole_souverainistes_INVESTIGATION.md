# ARCOM 2022 — Temps de parole des souverainistes : extraction quantitative

Date : 2026-08-04 | Heure : 21:30 CEST | Type : INVESTIGATION | Source : data.gouv.fr (ARCOM présidentielle 2022)

---

## §1. Méthodologie

**Source** : dataset ARCOM « Temps de parole des candidats — Élection présidentielle 2022 » (data.gouv.fr, dataset 67ee89ca16ae74bc0756195c).

**Périodes analysées** :
- P1 (équité) : 1er janvier - 7 mars 2022
- P2 (équité) : 8 mars - 27 mars 2022
- P3 (égalité) : 28 mars - 8 avril 2022
- P4 (second tour) : 11 avril - 22 avril 2022

**Chaînes cibles** : CNews, BFM TV, France Info, LCI (chaînes d'information en continu).

**Format P1** : 1 colonne « Durée » (HH:MM:SS). **Format P2-P4** : 4 tranches horaires (6h-9h, 9h-18h, 18h-24h, 0h-6h).

**Données brutes téléchargées** : 4 CSV, 174-176 KB chacun. Extraction Python/pandas (~50 lignes de code).

---

## §2. Résultats — Grand total (1er janvier - 22 avril 2022)

Chaînes d'information en continu uniquement (CNews + BFM TV + France Info + LCI).

| # | Candidat | CNews | BFM TV | France Info | LCI | **TOTAL** |
|---|----------|-------|--------|-------------|-----|-----------|
| F-AR2-01 | Macron | 135h41 | 124h08 | 777h10* | 127h14 | **1164h54** |
| F-AR2-02 | Le Pen | 123h14 | 110h51 | 614h16* | 120h04 | **968h40** |
| F-AR2-03 | Pécresse | 100h34 | 52h48 | 327h40* | 102h20 | **583h24** |
| F-AR2-04 | Zemmour | 129h07 | 93h20 | 83h30* | 144h08 | **450h07** |
| F-AR2-05 | Jadot | 39h07 | 44h59 | 96h27* | 57h47 | **238h22** |
| F-AR2-06 | Hidalgo | 33h54 | 33h31 | 90h15* | 51h03 | **208h45** |
| F-AR2-07 | Roussel | 21h28 | 26h40 | 55h50* | 51h19 | **155h19** |
| F-AR2-08 | Dupont-Aignan | 19h30 | 8h08 | 27h39 | 26h07 | **81h25** |
| F-AR2-09 | Lassalle | 10h00 | 5h52 | 21h20 | 22h13 | **59h26** |
| F-AR2-10 | Arthaud | 14h05 | 11h18 | 15h08 | 18h32 | **59h05** |
| F-AR2-11 | Poutou | 7h04 | 7h13 | 21h39 | 21h52 | **57h48** |
| F-AR2-12 | Asselineau | 0h31 | 0h35 | 1h59 | 1h18 | **4h24** |

> \* Note : France Info inclut probablement les rediffusions radio + TV (FranceinfoTV). Les totaux France Info pour Macron, Le Pen, Pécresse, Jadot, Hidalgo, Roussel sont anormalement élevés par rapport aux autres chaînes : vraisemblablement un artefact du dataset (France Info radio + FranceinfoTV agrégés). Les comparaisons inter-chaînes doivent donc se concentrer sur CNews, BFM TV, et LCI. Les totaux restent valides pour les comparaisons inter-candidats.

---

## §3. Ratios

| Comparaison | Ratio | Signification |
|-------------|-------|---------------|
| F-AR2-13 | Macron / Asselineau | **264:1** | Asselineau quasi invisible |
| F-AR2-14 | Le Pen / Asselineau | **219:1** | Même Le Pen reçoit 219× plus |
| F-AR2-15 | Zemmour / Asselineau | **102:1** | Zemmour, 3e plus faible, reçoit 102× plus |
| F-AR2-16 | Macron / Dupont-Aignan | **14:1** | NDA 14× moins que Macron |
| F-AR2-17 | Macron / Lassalle | **20:1** | Lassalle 20× moins que Macron |
| F-AR2-18 | Pécresse / Dupont-Aignan | **7:1** | Même Pécresse (LR) reçoit 7× plus que NDA |

---

## §4. Période 1 (1er janvier - 7 mars 2022) — Détail par chaîne

| Candidat | CNews | BFM TV | France Info | LCI | TOTAL P1 |
|----------|-------|--------|-------------|-----|----------|
| Macron | 110h34 | 103h33 | 239h05 | 104h36 | 557h49 |
| Le Pen | 104h13 | 80h36 | 150h23 | 88h40 | 423h53 |
| Pécresse | 87h39 | 46h17 | 260h07 | 54h56 | 449h00 |
| Zemmour | 112h00 | 73h04 | 104h12 | 60h39 | 349h56 |
| **Dupont-Aignan** | **6h45** | **3h37** | **13h10** | **8h28** | **32h02** |
| **Lassalle** | **2h17** | **2h05** | **6h14** | **3h28** | **14h05** |
| **Asselineau** | **0h31** | **0h35** | **1h59** | **1h18** | **4h24** |

**F-AR2-19** : En P1, Asselineau reçoit 0h31 sur CNews — soit l'équivalent d'UN seul passage. Dupont-Aignan : 6h45 sur CNews. Macron : 110h34.

---

## §5. Période 3 — Égalité stricte (28 mars - 8 avril 2022)

Période où l'ARCOM impose un temps égal à tous les candidats.

| F-AR2-20 | Candidat | Temps P3 |
|-----------|----------|----------|
| | Macron | 40h29 |
| | Le Pen | 37h51 |
| | Pécresse | 38h35 |
| | Zemmour | 36h48 |
| | Jadot | 36h19 |
| | Hidalgo | 36h07 |
| | Roussel | 36h21 |
| | Dupont-Aignan | 34h47 |
| | Lassalle | 35h11 |
| | Poutou | 35h33 |
| | Arthaud | 34h48 |
| | **Asselineau** | **ABSENT** |

**F-AR2-21** : Asselineau est absent de la période d'égalité. Il n'a pas atteint le statut de « candidat » au sens ARCOM (probablement pas les 500 parrainages validés à cette date, ou considéré comme n'ayant pas d'« actualité électorale suffisante »).

---

## §6. Asselineau — Tous médias confondus (P1)

Pour vérifier si l'invisibilité d'Asselineau est spécifique aux chaînes info ou générale.

| F-AR2-22 | Média | Temps P1 |
|-----------|-------|----------|
| | Europe 1 | 1h31 |
| | Sud Radio | 1h31 |
| | LCI | 1h18 |
| | FranceinfoTV | 1h15 |
| | France Info | 0h44 |
| | RFI | 0h39 |
| | BFM TV | 0h35 |
| | France 2 | 0h33 |
| | CNews | 0h31 |
| | Euronews | 0h30 |
| | C8 | 0h29 |
| | RMC | 0h28 |
| | France 24 | 0h25 |
| | **TOTAL P1 (tous médias)** | **11h15** |

**F-AR2-23** : Même en incluant TOUS les médias (radio + TV), Asselineau totalise 11h15 en 66 jours de campagne P1. Soit ~10 minutes par jour, tous médias confondus. Macron : ~8h30 par jour.

**F-AR2-24** : Sud Radio et Europe 1 sont SES deux plus gros pourvoyeurs de temps de parole (1h31 chacun). CNews n'est que 9e (0h31).

---

## §7. Dupont-Aignan et Lassalle — Répartition par chaîne

| F-AR2-25 | Chaîne | Dupont-Aignan | Lassalle |
|-----------|-------|---------------|----------|
| | CNews | 24 % (19h30) | 17 % (10h00) |
| | BFM TV | 10 % (8h08) | 10 % (5h52) |
| | France Info | 34 % (27h39) | 36 % (21h20) |
| | LCI | 33 % (26h07) | 37 % (22h13) |

**F-AR2-26** : CNews donne à Dupont-Aignan 24 % de son temps total (la 2e source après France Info). BFM TV n'en donne que 10 %. CNews n'est PAS le média qui invisibilise le plus les souverainistes — c'est BFM TV qui est le plus restrictif.

**F-AR2-27** : Pour Lassalle, CNews (17 %) est également devant BFM TV (10 %).

---

## §8. Synthèse — Ce que les données ARCOM 2022 établissent

1. **Asselineau est structurellement invisible** (F-AR2-12, F-AR2-13). 4h24 sur les chaînes info en 112 jours de campagne. Ratio 264:1 vs Macron. Ce n'est pas un « traitement défavorable » : c'est une non-existence médiatique.

2. **La période d'égalité (P3) exclut Asselineau** (F-AR2-21). Les 11 autres candidats reçoivent ~35h chacun. Lui : zéro. Le mécanisme ARCOM d'égalité ne s'applique qu'aux candidats déjà reconnus.

3. **CNews n'est pas le pire média pour les souverainistes** (F-AR2-26, F-AR2-27). BFM TV donne MOINS de temps à Dupont-Aignan (10 %) et Lassalle (10 %) que CNews (24 % et 17 %). Le « blackout » est un phénomène transversal, pas spécifique à Bolloré.

4. **Dupont-Aignan et Lassalle sont dans le « peloton des petits »** (F-AR2-08, F-AR2-09). 59-81h contre 155-238h pour Hidalgo/Jadot/Roussel. Un facteur 2-3, pas 100. Ils sont marginalisés mais pas invisibilisés.

5. **Le gap P1→P3 est révélateur** : en P1 (équité, pas égalité), Dupont-Aignan reçoit 32h et Lassalle 14h. En P3 (égalité), ils reçoivent 35h chacun — soit PLUS que leur P1 entière en seulement 12 jours. Le mécanisme d'égalité est la seule période où les « petits » candidats existent médiatiquement.

---

## §9. Limites

- **Post-2022** : aucune donnée individuelle. Les figures non-candidates (Philippot) n'apparaissent pas du tout.
- **France Info** : probable agrégation radio+TV, rendant les comparaisons inter-chaînes fragiles. Les données CNews/BFM/LCI sont plus fiables.
- **Temps de parole ≠ temps d'antenne** : le temps de parole ARCOM mesure les interventions des candidats eux-mêmes. Le temps où on PARLE d'eux (commentaires, éditoriaux) n'est pas mesuré.
- **Qualitatif absent** : 35h d'égalité en P3 ne dit rien sur LE CADRAGE de ce temps (favorable, hostile, neutre).

---

## §10. Fiches connexes

- `2026-08-04_15-30_faisceau_neutralisation_souverainete_INVESTIGATION.md` (fiche D) : mécanismes de neutralisation
- `2026-08-04_20-00_bollore_influence_editoriale_niveau3_INVESTIGATION.md` (fiche R) : niveau 3 Bolloré
- `2026-08-04_20-45_temps_antenne_souverainistes_gap_INVESTIGATION.md` (fiche S) : gap pré-extraction

Source : ARCOM via [data.gouv.fr](https://www.data.gouv.fr/fr/datasets/temps-de-parole-des-candidats-a-lelection-presidentielle-2022/), extraction Python 2026-08-04.
