# Données brutes — Fresque systémique France 1975-2026

> Ce dossier contient les données sources de la fresque systémique : une hyper-matrice de faits atomiques couvrant 52 ans (1975-2026) sur 20 dimensions.

## Architecture

```
01_donnees/
  README.md                                              # ce fichier
  2026-06-25_17-00_france_1975-2026_HYPER_MATRICE_UNIFIEE.md   # fichier maître (376k chars, 4504 événements)
  2026-06-25_17-00_france_1975-1982_HYPER_MATRICE.md           # découpe par décennie (archive)
  2026-06-25_17-00_france_1983-1990_HYPER_MATRICE.md
  ...                                                          # autres découpes décennales
  chroniques/                                                  # découpage annuel + dimension (724 fichiers)
    README.md                                                  # index complet des chroniques
    plages_annees.md                                           # 336 événements avec plages d'années
    1975/                                                      # 60 événements, 12 dimensions
      1975_POL.md
      1975_ECO.md
      ...
    1976/
    ...
    2026/                                                      # 453 événements, 18 dimensions
      2026_POL.md
      ...
```

## Le fichier maître

`2026-06-25_17-00_france_1975-2026_HYPER_MATRICE_UNIFIEE.md` est le fichier source unique.
Il contient **4504 événements** uniques (après dédoublonnage) classés par année et par dimension.

Il est conservé comme **référence canonique**. Les fichiers dans `chroniques/` en sont une **vue éclatée** — ils sont générés par script, ne pas les éditer directement sans répercuter dans le maître.

## Les chroniques (découpage fin)

Le dossier `chroniques/` découpe le fichier maître par année × dimension :

- **53 dossiers années** (1975-2026 + anomalie 2030)
- **724 fichiers** markdown
- **20 dimensions** : POL, ÉCO, SOC, JUR, SANT, ÉDU, AGR, ENV, TEC, CUL, IMM, SPO, REL, DÉMO, TRA, MIL, SCI, DIP, MÉD, TER

Chaque fichier pèse en moyenne **10-50 lignes** — chargeable instantanément par un LLM.

### Pourquoi ce découpage ?

1. **Maintenabilité** : ajouter/supprimer un événement sans toucher 4504 lignes
2. **Performance LLM** : charger uniquement l'année et la dimension pertinente
3. **Évolutivité** : enrichir 2026 sans recharger 1975
4. **Adressabilité** : `chroniques/2024/POL.md` est une adresse stable et prédictible

### Anomalie connue

2 événements datés de **2030** (dossiers `2030/TEC.md`, `2030/DIP.md`). Ils sont conservés tels quels dans la matrice source — probablement des erreurs de datation dans les suppléments originaux.

## Les suppléments

Les autres fichiers `SUPPLEMENT_*.md` sont des apports data issus d'articles ou de recherches ciblées (Défense/Ukraine, Agriculture/DNC, Corruption/État mafia, Énergie/Climat, Pédophilie/Censure, etc.). Ils ont été fusionnés dans la matrice unifiée.

## Conventions de nommage

- Fichiers `chroniques/YYYY/YYYY_DIM.md` : année en 4 chiffres + dimension en 3 lettres sans accent
- Dimensions normalisées : ÉCO→ECO, ÉDU→EDU, DÉMO→DEMO, MÉD→MED
- Codes impact : ✅ positif, ⚠ neutre/mixte, ❌ négatif, 💀 catastrophe

## Métriques

| Métrique | Valeur |
|----------|--------|
| Période | 1975-2026 (52 ans) |
| Événements uniques | 4 504 |
| Dimensions | 20 |
| Fichiers chroniques | 724 |
| Fichier maître | 376 639 chars |
| Source la plus récente | 2026-06-25 |
