# GAP ANALYSIS — Chroniques 1789-2026
## Analyse des angles morts, priorités d'enrichissement et recommandations FAIT-MINEUR

**Date :** 2026-06-27
**Type :** RAPPORT
**Source :** `chroniques/README.md` + scan des 825 fichiers (5 989 événements, 20 dimensions, 66 années)
**Méthode :** FAIT-MINEUR v1.0 — PHASE 1: GAP

---

## §1 — PANORAMA GLOBAL

### Métriques de base

| Métrique | Valeur |
|----------|:------:|
| Événements totaux (fichiers) | **5 989** |
| Événements (plages d'années) | **338** |
| Fichiers chroniques | **825** |
| Dossiers années | **66** (1944-2060) |
| Dimensions | **20** |
| Période principale | 1975-2026 (52 ans, 99,6% des données) |
| Période historique | 1944-1974 (~0,2%) |
| Période future | 2028-2060 (~0,1%) |

### Répartition des codes d'impact

| Code | Occurrences | Proportion |
|------|:-----------:|:----------:|
| ❌ Négatif | 2 101 | 35,1% |
| ⚠ Préoccupant | 1 652 | 27,6% |
| ✅ Positif | 1 016 | 17,0% |
| 💀 Fatal | 478 | 8,0% |
| Non standard | 742 | 12,4% |

> **⚠ Alerte :** 12,4% des événements ont un code non standard. Cela suggère que ~742 lignes ont été mal formatées ou importées sans code valide.

### Évolution temporelle (événements par année)

```
1975 ████████████████████████████████████████████░░░░░░░░░░ 99
1984 ████████████████████████████████████████████████████████ 122 (pic pré-2020)
1995 ████████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░ 56
2006 ████████████████████████████████████████████████░░░░░░░ 134
2017 ████████████████████████████████████████████████░░░░░░░ 131
2022 ████████████████████████████████████████████████████████ 186
2024 ████████████████████████████████████████████████████████ 478
2025 ████████████████████████████████████████████████████████ 1 198 (explosion)
2026 ████████████████████████████████████████████████████████ 852
```

---

## §2 — CLASSEMENT DES DIMENSIONS PAR PRIORITÉ

### 🔴🔴 Niveau 1 — CRITIQUE (densité < 0,5 evt/an)

| Dimension | Événements | Années couv. | Densité | Couverture | Saturation | Code dominant |
|-----------|:----------:|:------------:|:-------:|:----------:|:----------:|:-------------:|
| **DEMO** Démographie | **2** | 27 | **0,07** | 52% | 0,2% | ❌ 100% |

**Diagnostic :** 2 événements pour 27 années de couverture annoncée — c'est une coquille vide. Densité 0,07 = un fait tous les 14 ans. La démographie française (natalité, mortalité, pyramide des âges, espérance de vie, mariages, divorces, fécondité) est ABSENTE des chroniques.

**Potentiel estimé :** 50-80 faits (lois natalité, baby-boom, pilule, IVG, PACs, mariage pour tous, transition démographique, vieillissement)

---

### 🔴 Niveau 2 — URGENT (densité < 3 evt/an OU couverture < 50%)

| Dimension | Événements | Années couv. | Densité | Couverture | Saturation | Code dominant |
|-----------|:----------:|:------------:|:-------:|:----------:|:----------:|:-------------:|
| **REL** Religion | **38** | 23 | **1,65** | 44% | 3,9% | ❌/⚠ |
| **SCI** Science | **52** | 28 | **1,86** | 54% | 5,4% | ✅/❌ |
| **EDU** Éducation | **49** | 43 | **1,14** | 83% | 5,1% | ❌/⚠ |
| **MED** Médias | **82** | 18 | **4,56** | 35% | 8,5% | ❌/✅ |
| **TER** Terrorisme | **77** | 24 | **3,21** | 46% | 8,0% | 💀 66% |

**Diagnostics :**

- **REL** : 38 événements — couverture quasi exclusivement catholique. Manquent : autres cultes (islam, judaïsme, bouddhisme), laïcité (1905, 2004), sécularisation, finances cultuelles, controverses.
- **SCI** : 52 événements — le CNRS (créé 1939), les prix Nobel français, les grands programmes (nucléaire, spatial, TGV, Minitel), les scandales (amiante, Mediator), la fuite des cerveaux — tout est sous-couvert.
- **EDU** : 49 événements — PISA, réformes (Haby, Savary, Jospin, allègements), université, Grandes Écoles, budgets, inégalités scolaires. Densité 1,14 = presque vide.
- **MED** : 82 événements mais seulement 18 années couvertes (35%). Manque : concentration médias (Bolloré, Dassault), SIG, presse écrite, radio, numérique, lois (1881, LCEN).
- **TER** : 77 événements dominés par 💀 (66%) — couverture centrée sur les attentats. Manque : antiterrorisme, lois, budgets, fichage, radicalisation, déradicalisation.

**Potentiel estimé :** 30-60 faits par dimension.

---

### 🟡 Niveau 3 — À SURVEILLER (densité < 5 evt/an OU couverture < 80%)

| Dimension | Événements | Années couv. | Densité | Couverture | Saturation | Code dominant |
|-----------|:----------:|:------------:|:-------:|:----------:|:----------:|:-------------:|
| **IMM** Immigration | **121** | 48 | **2,52** | 92% | 12,5% | ❌/⚠ |
| **TRA** Transports | **115** | 40 | **2,88** | 77% | 11,9% | ❌/⚠ |
| **DIP** Diplomatie | **227** | 21 | **10,81** | 40% | 23,5% | ❌/⚠ |
| **MIL** Militaire | **281** | 36 | **7,81** | 69% | 29,1% | ❌/⚠ |
| **ENV** Environnement | **225** | 48 | **4,69** | 92% | 23,3% | ⚠/❌ |

**Diagnostics :**

- **IMM** : Densité faible (2,52) mais bonne couverture. Manque : politiques d'immigration (1974, 1993, 2003, 2018), flux, régularisations, expulsions, asile, intégration.
- **TRA** : 77% de couverture mais lacunes 1990s (trou 1991-2000 dans la donnée brute). Manque : TGV, SNCF, RATP, aérien, infrastructures, grèves.
- **DIP** : Seulement 21 années couvertes (40%) — gros trou avant 1986 et dans les 2000s. Densité haute (10,8) parce qu'une fois présente, bien couverte en 2020s.
- **MIL** : 69% de couverture, trou 1998-2000. Budget défense, OPEX, dissuasion nucléaire, professionnalisation, équipements.
- **ENV** : Bonne couverture mais densité modérée. Grenelle, COP, nucléaire, pollutions, biodiversité.

**Potentiel estimé :** 15-30 faits par dimension.

---

### 🟢 Niveau 4 — ACCEPTABLE (densité >= 5 ET couverture >= 80%)

| Dimension | Événements | Années couv. | Densité | Couverture | Saturation | Code dominant |
|-----------|:----------:|:------------:|:-------:|:----------:|:----------:|:-------------:|
| **POL** Politique | **967** | 52 | **18,60** | 100% | 100% | ❌/⚠/✅ |
| **SOC** Social | **744** | 53 | **14,04** | 100%+ | 77,0% | ❌/⚠/✅ |
| **JUR** Justice | **634** | 53 | **11,96** | 100%+ | 65,6% | ❌/⚠ |
| **TEC** Technologie | **431** | 52 | **8,29** | 100% | 44,6% | ❌/✅/⚠ |
| **ECO** Économie | **391** | 54 | **7,24** | 100%+ | 40,4% | ❌ (93%) |
| **CUL** Culture | **376** | 52 | **7,23** | 100% | 38,9% | ✅/❌/💀 |
| **AGR** Agriculture | **289** | 55 | **5,25** | 100%+ | 29,9% | ❌/⚠ |
| **SPO** Sport | **255** | 52 | **4,90** | 100% | 26,4% | ❌/✅ |
| **SANT** Santé | **245** | 48 | **5,10** | 92% | 25,3% | ❌/⚠ |

**Diagnostics :**

- **ECO** : 93% de ❌ — déséquilibre dialectique critique. Aucun fait positif sur l'économie en 52 ans ? C'est un biais de sélection.
- **POL** : Meilleure couverture. Mais biais❌/⚠ dominant.
- **SANT** : 92% couverture mais manque scandales avant 2000 (amiante, sang contaminé, hormones de croissance, vache folle — saisis dans JUR mais pas SANT).

**Potentiel estimé :** 5-15 faits par dimension (enrichissement ciblé).

---

## §3 — ANALYSE TEMPORELLE : TROUS PAR DÉCENNIE

### Période 1944-1974 (31 ans — quasi-vide)

```
Événements totaux : ~14
Dimensions couvertes : AGR (3), DIP (4), JUR (1), SOC (1) + divers isolés
```

**GAP :** 31 années avec ~14 événements = **angle mort historique massif**. Toute la IVe République, la guerre d'Algérie, les Trente Glorieuses, la construction européenne (CECA, CED, Traité de Rome), la décolonisation — ABSENTS.

**Potentiel :** 200-400 faits (priorité DIP, POL, MIL, ECO, SOC).

### Période 1975-1990 (16 ans — bonne couverture relative)

```
Moyenne : ~100 evts/an
Pic : 122 (1984)
Dimensions actives : ~15/20
```

**GAP :** Manque REL, SCI, EDU, MED, DEMO sur toute la période. DIP et MIL trouées.

**Potentiel :** 50-100 faits.

### Période 1991-2000 (10 ans — déclin suspect)

```
Moyenne : ~55 evts/an (vs 100 en 1980s)
Minimum : 37 (1992, 1993)
```

**GAP :** Chute de ~45% par rapport à la décennie précédente. Pas réaliste — la France n'a pas eu moins d'événements dans les 1990s. C'est un **trou de collecte** : les APEX et suppléments ont moins couvert cette décennie. Maastricht, guerre du Golfe, Yougoslavie, vache folle, chômage de masse, Juppé — sous-représentés.

**Potentiel :** 100-200 faits.

### Période 2001-2013 (13 ans — moyenne)

```
Moyenne : ~75 evts/an
Pic : 134 (2006)
```

**GAP :** Meilleure mais toujours en dessous du niveau 1980s. Manque : élargissement UE, émeutes 2005, CPE, crise 2008, réforme retraites 2010, printemps arabe, affaire Bettencourt, DSK.

**Potentiel :** 50-100 faits.

### Période 2014-2023 (10 ans — montée en puissance)

```
Moyenne : ~140 evts/an
Pic : 186 (2022)
```

**GAP :** Meilleure couverture mais encore inférieure à 2024-2026. Manque : attentats 2015, état d'urgence, gilets jaunes, COVID-19 (partiellement couvert), réforme retraites 2023.

**Potentiel :** 30-50 faits.

### Période 2024-2026 (3 ans — explosion)

```
2024 : 478 evts
2025 : 1 198 evts
2026 : 852 evts
Total 3 ans : 2 528 evts = 42% du total sur 52 ans
```

**⚠ Alerte de distorsion :** 42% des événements sur 6% de la période. C'est un **biais de recency** — les APEX et suppléments ont massivement couvert la période récente. La fresque risque de raconter la France 2024-2026 comme si elle résumait 52 ans.

---

## §4 — ANALYSE DIALECTIQUE : DÉSÉQUILIBRE DES CODES

### Dimensions avec >80% d'un même code

| Dimension | Code dominant | Proportion | Diagnostic |
|-----------|:------------:|:----------:|------------|
| **ECO** | ❌ | **93%** | Économie vue uniquement comme dégradation — biais de sélection |
| **TER** | 💀 | **66%** | Terrorisme vu uniquement comme fatalité — manquent prévention, lois, déradicalisation |
| **DEMO** | ❌ | **100%** | 2 événements, les deux négatifs — statistiquement insignifiant |

### Dimensions avec équilibre acceptable

| Dimension | ✅ | ⚠ | ❌ | 💀 |
|-----------|:--:|:--:|:--:|:--:|
| **CUL** | 136 | 63 | 88 | 89 |
| **TEC** | 120 | 88 | 189 | 34 |
| **POL** | 153 | 295 | 377 | 27 |
| **SOC** | 78 | 225 | 249 | 88 |

### Recommandations dialectiques

1. **ECO** (93% ❌) : Chercher activement des faits ✅ ou ⚠ (réformes, innovations, PIB, emploi, exportations, investissements)
2. **TER** (66% 💀) : Ajouter des faits ⚠ et ✅ (lois antiterrorisme, budgets, fichage, déradicalisation, coopération européenne)
3. **Toutes dimensions** : Viser un ratio ~40% ❌ / 30% ⚠ / 20% ✅ / 10% 💀 comme cible d'équilibre

---

## §5 — SYNTHÈSE DES PRIORITÉS FAIT-MINEUR

### Priorité 1 — Dimensions critiques (🔴🔴 + 🔴)

| Rang | Dimension | Urgence | Justification | Potentiel | Effort |
|:----:|-----------|:-------:|:--------------|:---------:|:------:|
| **1** | **DEMO** | 🔴🔴 | 2 événements / 52 ans | 50-80 faits | 2 sessions |
| **2** | **REL** | 🔴 | 38 événements, 44% couverture | 30-50 faits | 2 sessions |
| **3** | **SCI** | 🔴 | 52 événements, densité 1,9 | 40-60 faits | 2-3 sessions |
| **4** | **EDU** | 🔴 | 49 événements, densité 1,1 | 40-60 faits | 2-3 sessions |
| **5** | **MED** | 🔴 | 82 évts, 35% couverture | 30-50 faits | 2 sessions |
| **6** | **TER** | 🔴 | 77 évts, 46% couverture | 20-40 faits | 1-2 sessions |
| **Total P1** | | | | **210-340 faits** | **11-14 sessions** |

### Priorité 2 — Dimensions à enrichir (🟡)

| Rang | Dimension | Justification | Potentiel | Effort |
|:----:|-----------|:--------------|:---------:|:------:|
| **7** | **IMM** | Densité 2,5 — manque structuration | 20-30 faits | 2 sessions |
| **8** | **TRA** | Densité 2,9, trou 1991-2000 | 15-25 faits | 1 session |
| **9** | **DIP** | 40% couverture, trou pré-1986 | 20-40 faits | 2 sessions |
| **10** | **MIL** | 69% couverture, trou 1998-2000 | 15-25 faits | 1 session |
| **11** | **ENV** | Densité 4,7 — quelques trous | 15-20 faits | 1 session |
| **Total P2** | | | **85-140 faits** | **7 sessions** |

### Priorité 3 — Enrichissement ciblé (🟢)

| Dimension | Action | Potentiel | Effort |
|-----------|:-------|:---------:|:------:|
| **ECO** | Rééquilibrer dialectique (93% ❌ → ajouter ✅/⚠) | 10-20 faits | 1 session |
| **SANT** | Rapatrier faits JUR vers SANT (amiante, sang) | 10-15 faits | 1 session |
| **POL/SOC/JUR/TEC** | Compléter années creuses 1991-2000 | 20-30 faits | 2 sessions |
| **CUL/AGR/SPO** | Maintien | 5-10 faits | 1 session |
| **Total P3** | | **45-75 faits** | **5 sessions** |

### Priorité 4 — Trou historique 1944-1974

| Action | Potentiel | Effort |
|:-------|:---------:|:------:|
| Enrichir 31 années quasi-vides | 200-400 faits | 15-20 sessions |
| Cibler DIP, POL, MIL, ECO, SOC | | |

---

## §6 — RECOMMANDATIONS STRATÉGIQUES

### 1. Attaquer les dimensions 🔴 en premier

Les 6 dimensions 🔴 (DEMO, REL, SCI, EDU, MED, TER) représentent **~15%** des événements mais devraient en représenter **~30%** dans une couverture équilibrée. Le potentiel total est de **210-340 nouveaux faits** en 11-14 sessions FAIT-MINEUR.

### 2. Combler le trou 1991-2000

La chute de -45% par rapport aux 1980s est un artefact de collecte, pas une réalité historique. Prioriser les sessions FAIT-MINEUR qui couvrent cette décennie pour chaque dimension.

### 3. Corriger le biais ECO (93% ❌)

L'économie française n'est pas que négative. Chercher des faits ✅ (innovations, réussites industrielles, réformes structurelles) pour rééquilibrer le tableau.

### 4. Créer la période 1789-1974

La fresque est censée couvrir 1789-2026. Actuellement, seule la période 1975-2026 est couverte (52 ans sur 237). C'est **22%** de la période revendiquée. Un chantier de fond.

### 5. Nettoyer les 742 codes non standard

12,4% des événements (~742 lignes) ont un code d'impact non standard (ni ✅⚠❌💀). Une session de nettoyage permettrait de les corriger.

---

## §7 — FEUILLE DE ROUTE RECOMMANDÉE

```
┌─────────────────────────────────────────────────────────────┐
│ FEUILLE DE ROUTE FAIT-MINEUR — 30 sessions estimées          │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  PHASE 1 (sessions 1-14)  → Dimensions 🔴 (210-340 faits)    │
│  ├── SCI  1970-2026  (3 sessions)                             │
│  ├── EDU  1975-2026  (3 sessions)                             │
│  ├── REL  1905-2026  (2 sessions)                             │
│  ├── DEMO 1975-2026  (2 sessions)                             │
│  ├── MED  1881-2026  (2 sessions)                             │
│  └── TER  1980-2026  (2 sessions)                             │
│                                                               │
│  PHASE 2 (sessions 15-21) → Dimensions 🟡 (85-140 faits)     │
│  ├── IMM  1974-2026  (2 sessions)                             │
│  ├── TRA  1981-2026  (1 session)                              │
│  ├── DIP  1957-2026  (2 sessions)                             │
│  ├── MIL  1975-2026  (1 session)                              │
│  └── ENV  1975-2026  (1 session)                              │
│                                                               │
│  PHASE 3 (sessions 22-26) → Enrichissement ciblé (45-75)      │
│  ├── ECO  rééquilibrage (1 session)                           │
│  ├── SANT rapatriement JUR→SANT (1 session)                   │
│  ├── 1991-2000 trou décennal (2 sessions)                     │
│  └── Nettoyage codes (1 session)                              │
│                                                               │
│  PHASE 4 (sessions 27-46) → Trou historique 1944-1974         │
│  └── 31 années quasi-vides (15-20 sessions)                   │
│                                                               │
│  Total estimé : 540-955 nouveaux faits en 30-46 sessions      │
│                                                               │
│  Potentiel final : ~6 500-7 000 événements                     │
│  Couverture : 20 dimensions × 52 ans → 237 ans (1789-2026)    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## §8 — DONNÉES BRUTES (annexe technique)

### Événements par année

```
1944: 1    | 1975: 99   | 2000: 72   | 2014: 96   | 2024: 478
1945: 1    | 1976: 85   | 2001: 73   | 2015: 126  | 2025: 1198
1957: 1    | 1977: 78   | 2002: 68   | 2016: 113  | 2026: 852
1958: 1    | 1978: 76   | 2003: 74   | 2017: 131  |
1962: 1    | 1979: 83   | 2004: 61   | 2018: 127  |
1963: 2    | 1980: 75   | 2005: 79   | 2019: 84   |
1964: 1    | 1981: 102  | 2006: 134  | 2020: 103  |
1968: 4    | 1982: 96   | 2007: 74   | 2021: 95   |
1970: 1    | 1983: 108  | 2008: 70   | 2022: 186  |
1971: 1    | 1984: 122  | 2009: 79   | 2023: 175  |
           | 1985: 114  | 2010: 81   |            |
           | 1986: 92   | 2011: 73   |            |
           | 1987: 83   | 2012: 65   |            |
           | 1988: 113  | 2013: 72   |            |
           | 1989: 127  |            |            |
           | 1990: 75   |            |            |
```

### Événements par décennie et dimension (sélection)

| Dimension | 1970s | 1980s | 1990s | 2000s | 2010s | 2020s |
|-----------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| POL       | 168   | 150   | 94    | 107   | 85    | 362   |
| SOC       | 112   | 170   | 71    | 69    | 62    | 260   |
| JUR       | 33    | 52    | 30    | 65    | 176   | 278   |
| TEC       | 58    | 61    | 26    | 62    | 54    | 170   |
| ECO       | 0     | 0     | 0     | 0     | 0     | 320*  |
| CUL       | 48    | 18    | 8     | 14    | 32    | 256   |
| AGR       | 22    | 38    | 20    | 16    | 62    | 131   |
| MIL       | 0     | 33    | 8     | 30    | 56    | 149   |
| SPO       | 25    | 47    | 24    | 17    | 22    | 118   |
| SANT      | 13    | 29    | 23    | 27    | 31    | 122   |
| DIP       | 0     | 0     | 18    | 16    | 32    | 143   |
| ENV       | 19    | 43    | 22    | 35    | 31    | 75    |
| IMM       | 9     | 17    | 12    | 16    | 15    | 51    |
| TRA       | 5     | 15    | 6     | 15    | 16    | 52    |
| MED       | 0     | 0     | 3     | 11    | 20    | 48    |
| TER       | 6     | 3     | 4     | 6     | 8     | 50    |
| SCI       | 0     | 2     | 5     | 17    | 14    | 14    |
| EDU       | 0     | 0     | 0     | 10    | 7     | 32    |
| REL       | 3     | 9     | 3     | 10    | 4     | 9     |
| DEMO      | 0     | 0     | 2     | 0     | 0     | 0     |

*\*Note : Les données ECO pré-2020 sont mal capturées par le script car les fichiers ECO antérieurs à 2020 utilisent un format différent. Les 391 événements ECO totaux sont majoritairement dans 2020s.*

---

*GAP ANALYSIS v1.0 — 2026-06-27*
*Méthode : FAIT-MINEUR v1.0 PHASE 1 — données issues du scan des 825 fichiers chroniques*
*Prochain rafraîchissement : après 10 sessions FAIT-MINEUR ou 500 nouveaux faits*
