# Chroniques 1975-2026

> Découpage annuel et par dimension de l'HYPER-MATRICE FRANCE 1975-2026.
> Source : `01_donnees/2026-06-25_17-00_france_1975-2026_HYPER_MATRICE_UNIFIEE.md`
> Généré le 2026-06-26.

## Structure

```
chroniques/
  README.md
  plages_annees.md           # 340 événements sans année unique
  1975/                         # 12 dimensions, 60 événements
  1976/                         # 11 dimensions, 61 événements
  1977/                         # 13 dimensions, 58 événements
  1978/                         # 8 dimensions, 53 événements
  1979/                         # 9 dimensions, 53 événements
  1980/                         # 9 dimensions, 57 événements
  1981/                         # 9 dimensions, 52 événements
  1982/                         # 9 dimensions, 57 événements
  1983/                         # 16 dimensions, 80 événements
  1984/                         # 16 dimensions, 91 événements
  1985/                         # 16 dimensions, 82 événements
  1986/                         # 16 dimensions, 78 événements
  1987/                         # 16 dimensions, 79 événements
  1988/                         # 17 dimensions, 82 événements
  1989/                         # 16 dimensions, 86 événements
  1990/                         # 16 dimensions, 88 événements
  1991/                         # 14 dimensions, 56 événements
  1992/                         # 13 dimensions, 55 événements
  1993/                         # 13 dimensions, 53 événements
  1994/                         # 9 dimensions, 32 événements
  1995/                         # 11 dimensions, 42 événements
  1996/                         # 11 dimensions, 23 événements
  1997/                         # 8 dimensions, 21 événements
  1998/                         # 11 dimensions, 48 événements
  1999/                         # 14 dimensions, 43 événements
  2000/                         # 13 dimensions, 61 événements
  2001/                         # 15 dimensions, 61 événements
  2002/                         # 11 dimensions, 50 événements
  2003/                         # 12 dimensions, 46 événements
  2004/                         # 13 dimensions, 54 événements
  2005/                         # 13 dimensions, 52 événements
  2006/                         # 19 dimensions, 100 événements
  2007/                         # 14 dimensions, 36 événements
  2008/                         # 16 dimensions, 45 événements
  2009/                         # 16 dimensions, 35 événements
  2010/                         # 15 dimensions, 41 événements
  2011/                         # 14 dimensions, 30 événements
  2012/                         # 15 dimensions, 38 événements
  2013/                         # 15 dimensions, 38 événements
  2014/                         # 14 dimensions, 61 événements
  2015/                         # 15 dimensions, 58 événements
  2016/                         # 14 dimensions, 59 événements
  2017/                         # 17 dimensions, 83 événements
  2018/                         # 15 dimensions, 64 événements
  2019/                         # 15 dimensions, 67 événements
  2020/                         # 16 dimensions, 74 événements
  2021/                         # 15 dimensions, 89 événements
  2022/                         # 15 dimensions, 100 événements
  2023/                         # 16 dimensions, 107 événements
  2024/                         # 17 dimensions, 266 événements
  2025/                         # 19 dimensions, 508 événements
  2026/                         # 18 dimensions, 453 événements
  2030/                         # 2 dimensions, 2 événements
```

## Pourquoi ce découpage ?

Le fichier HYPER_MATRICE_UNIFIEE.md (376k chars, 4504 événements) n'est plus maintenable
en l'état. En le découpant par année et par dimension, chaque fichier devient :

- **Chargeable instantanément** par un LLM (5-50 événements par fichier en moyenne)
- **Maintenable** : on peut ajouter/supprimer un événement sans toucher au reste
- **Navigable** : un LLM peut charger l'année ET la dimension pertinente
- **Évolutif** : on peut enrichir 2026 sans recharger 1975
- **Référençable** : `chroniques/2024/POL.md` est une adresse stable

## Index des années

| Année | Fichiers | Événements | Dimensions |
|---|---|---|---|
| 1975 | 12 | 60 | POL, ECO, SOC, JUR, AGR, ENV, TEC, CUL, SPO, TRA, MIL, TER |
| 1976 | 11 | 61 | POL, ECO, SOC, JUR, ENV, TEC, CUL, IMM, SPO, REL, TER |
| 1977 | 13 | 58 | POL, ECO, SOC, JUR, SANT, EDU, ENV, TEC, CUL, SPO, SCI, DIP, TER |
| 1978 | 8 | 53 | POL, ECO, SOC, ENV, TEC, CUL, SPO, TER |
| 1979 | 9 | 53 | POL, ECO, SOC, JUR, ENV, TEC, CUL, SPO, TER |
| 1980 | 9 | 57 | POL, ECO, SOC, JUR, ENV, TEC, CUL, SPO, TER |
| 1981 | 9 | 52 | POL, ECO, SOC, EDU, TEC, CUL, SPO, TRA, TER |
| 1982 | 9 | 57 | POL, ECO, SOC, EDU, TEC, CUL, SPO, SCI, TER |
| 1983 | 16 | 80 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, REL, DEMO, TRA, MIL |
| 1984 | 16 | 91 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, REL, DEMO, TRA, MIL |
| 1985 | 16 | 82 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, REL, DEMO, TRA, MIL |
| 1986 | 16 | 78 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, REL, DEMO, TRA, MIL |
| 1987 | 16 | 79 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, REL, DEMO, TRA, MIL |
| 1988 | 17 | 82 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, REL, DEMO, TRA, MIL, MED |
| 1989 | 16 | 86 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, REL, DEMO, TRA, MIL |
| 1990 | 16 | 88 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, REL, DEMO, TRA, MIL |
| 1991 | 14 | 56 | POL, ECO, SOC, JUR, SANT, AGR, ENV, TEC, CUL, SPO, REL, MIL, DIP, TER |
| 1992 | 13 | 55 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, SPO, MIL, DIP |
| 1993 | 13 | 53 | POL, ECO, SOC, JUR, EDU, AGR, ENV, TEC, CUL, IMM, SPO, MIL, DIP |
| 1994 | 9 | 32 | POL, SOC, JUR, SANT, EDU, TEC, CUL, MIL, SCI |
| 1995 | 11 | 42 | POL, ECO, SOC, JUR, EDU, TEC, CUL, SPO, REL, MIL, DIP |
| 1996 | 11 | 23 | POL, SOC, JUR, EDU, TEC, CUL, IMM, SPO, REL, MIL, DIP |
| 1997 | 8 | 21 | POL, SOC, JUR, CUL, IMM, DEMO, MIL, SCI |
| 1998 | 11 | 48 | POL, ECO, SOC, JUR, AGR, TEC, CUL, IMM, SPO, SCI, DIP |
| 1999 | 14 | 43 | POL, ECO, SOC, JUR, SANT, AGR, ENV, TEC, CUL, IMM, SPO, REL, DEMO, SCI |
| 2000 | 13 | 61 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, CUL, SPO, TRA, SCI, MED |
| 2001 | 15 | 61 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, SPO, REL, TRA, MIL, SCI |
| 2002 | 11 | 50 | POL, ECO, SOC, JUR, ENV, CUL, IMM, SPO, TRA, SCI, MED |
| 2003 | 12 | 46 | POL, ECO, SOC, SANT, EDU, AGR, TEC, CUL, SPO, REL, TRA, SCI |
| 2004 | 13 | 54 | POL, ECO, SOC, JUR, SANT, AGR, TEC, CUL, SPO, TRA, MIL, SCI, TER |
| 2005 | 13 | 52 | POL, ECO, SOC, JUR, SANT, AGR, TEC, CUL, SPO, REL, DEMO, TRA, TER |
| 2006 | 19 | 100 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, REL, DEMO, TRA, MIL, SCI, MED, TER |
| 2007 | 14 | 36 | POL, ECO, SOC, JUR, SANT, EDU, ENV, TEC, CUL, IMM, SPO, TRA, SCI, MED |
| 2008 | 16 | 45 | POL, ECO, SOC, JUR, SANT, AGR, ENV, TEC, CUL, IMM, SPO, REL, DEMO, TRA, SCI, MED |
| 2009 | 16 | 35 | POL, ECO, SOC, JUR, SANT, EDU, ENV, TEC, CUL, IMM, SPO, REL, DEMO, TRA, SCI, DIP |
| 2010 | 15 | 41 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, TRA, MED, TER |
| 2011 | 14 | 30 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, DEMO, TRA |
| 2012 | 15 | 38 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, TRA, SCI, DIP |
| 2013 | 15 | 38 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, TRA, MIL, SCI |
| 2014 | 14 | 61 | POL, ECO, SOC, JUR, SANT, EDU, ENV, TEC, CUL, IMM, SPO, DEMO, TRA, MIL |
| 2015 | 15 | 58 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, TRA, MIL, MED |
| 2016 | 14 | 59 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, TRA, MIL |
| 2017 | 17 | 83 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, TRA, MIL, SCI, DIP, MED |
| 2018 | 15 | 64 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, TRA, SCI, MED |
| 2019 | 15 | 67 | POL, ECO, SOC, JUR, SANT, EDU, ENV, TEC, CUL, IMM, SPO, TRA, MIL, MED, TER |
| 2020 | 16 | 74 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, SPO, TRA, SCI, DIP, MED, TER |
| 2021 | 15 | 89 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, TRA, MIL, SCI |
| 2022 | 15 | 100 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, TRA, MIL, DIP |
| 2023 | 16 | 107 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, MIL, SCI, DIP, TER |
| 2024 | 17 | 266 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, TRA, MIL, SCI, DIP, MED |
| 2025 | 19 | 508 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, DEMO, TRA, MIL, SCI, DIP, MED, TER |
| 2026 | 18 | 453 | POL, ECO, SOC, JUR, SANT, EDU, AGR, ENV, TEC, CUL, IMM, SPO, DEMO, TRA, MIL, DIP, MED, TER |
| 2030 | 2 | 2 | TEC, DIP |
| Plages | 1 | 336 | — |
| **TOTAL** | **723** | **4504** | **20 dimensions** |
