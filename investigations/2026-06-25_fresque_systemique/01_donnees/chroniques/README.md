# Chroniques 1975-2026

Découpage année × dimension de l'HYPER-MATRICE FRANCE 1975-2026.
Source : `01_donnees/2026-06-25_17-00_france_1975-2026_HYPER_MATRICE_UNIFIEE.md`

## Structure

```
chroniques/
  README.md
  plages_annees.md        ← événements sans année unique (ex: 1980-2000)
  1975/
    1975_POL.md            ← événements politiques de 1975
    1975_ECO.md            ← événements économiques de 1975
    1975_SOC.md
    ...
  1976/
    1976_POL.md
    ...
```

- **805 fichiers** répartis dans **54 dossiers années** (1975-2026 + anomalies 2028, 2030)
- **5 804 événements** dans les fichiers année×dimension
- **336 événements** dans `plages_annees.md` (plages d'années)
- **Total : 6 140 événements**, 20 dimensions

## Format d'un fichier chronique

Chaque fichier `YYYY_DIM.md` suit ce format strict :

```markdown
### YYYY_DIM

| Année | Dimension | Description | Code |
|---|---|---|---|
| 2024 | POL | Texte de l'événement | ✅ |
| 2024 | POL | Autre événement | ⚠ |
```

Les 4 codes d'impact :

| Code | Signification | Exemple |
|------|---------------|---------|
| ✅ | Positif / constructif | Loi votée, innovation, progrès social |
| ⚠ | Préoccupant / alerte | Tension, risque, réforme avortée |
| ❌ | Négatif / critique | Répression, échec, crise |
| 💀 | Fatal / catastrophique | Crime, attentat, catastrophe |

## Comment ajouter un événement

**1. Identifier l'année et la dimension**

Exemple : loi sur le logement en 2024 → année `2024`, dimension `SOC`.

Ouvrir `chroniques/2024/2024_SOC.md`.

**2. Ajouter la ligne en respectant le format**

```
| 2024 | SOC | Description précise de l'événement | ⚠ |
```

Règles :
- La description commence par une majuscule, pas de point final
- Pas de pipe `|` dans la description (échapper ou reformuler)
- Le code est un des 4 symboles : ✅ ⚠ ❌ 💀
- L'année dans la 1re colonne = année du dossier (cohérence obligatoire)

**3. Si le fichier n'existe pas**

Créer le fichier `chroniques/2024/2024_DIM.md` avec l'en-tête :

```markdown
### 2024_DIM

| Année | Dimension | Description | Code |
|---|---|---|---|
```

Puis ajouter la ligne. Le dossier année existe déjà.

**4. Si l'année est une plage (ex: 1980-2000)**

Ajouter l'événement dans `plages_annees.md` :

```markdown
| 1980-2000 | ÉCO | Description | ⚠ |
```

**5. Mettre à jour le fichier maître**

Après modification des chroniques, ajouter la même ligne dans le fichier maître `01_donnees/2026-06-25_17-00_france_1975-2026_HYPER_MATRICE_UNIFIEE.md`, dans la section `### YYYY` correspondante.

## Dimensions disponibles (20)

| Code | Dimension |
|------|-----------|
| POL | Politique, institutions |
| ECO | Économie, finances |
| SOC | Social, démographie |
| JUR | Justice, droit |
| SANT | Santé |
| EDU | Éducation |
| AGR | Agriculture |
| ENV | Environnement |
| TEC | Technologie, industrie |
| CUL | Culture, médias |
| IMM | Immigration |
| SPO | Sport |
| REL | Religion |
| DEMO | Démographie |
| TRA | Transports |
| MIL | Militaire |
| SCI | Science, recherche |
| DIP | Diplomatie |
| MED | Média |
| TER | Terrorisme |

## Pourquoi ce découpage ?

- **Chargeable instantanément** par un LLM (1-50 événements par fichier)
- **Maintenable** : on ajoute un événement sans toucher au reste
- **Navigable** : on charge l'année ET la dimension pertinente
- **Référençable** : `chroniques/2024/2024_POL.md` est une adresse stable
- **Évolutif** : on peut enrichir 2026 sans recharger 1975

## Métriques

| Période | Fichiers | Événements | Dimensions |
|---------|---------|------------|------------|
| 1975 | 14 | 98 | POL, ECO, SOC, JUR, AGR, ENV, TEC, CUL, SPO, TRA, MIL, TER, EDU, IMM |
| 1976 | 14 | 99 | POL, ECO, SOC, JUR, ENV, TEC, CUL, IMM, SPO, REL, TER, AGR, SANT, TRA |
| 1977 | 17 | 83 | POL, ECO, SOC, JUR, SANT, EDU, ENV, TEC, CUL, SPO, SCI, DIP, TER, AGR, DEMO, IMM, TRA |
| 1978 | 12 | 79 | POL, ECO, SOC, ENV, TEC, CUL, SPO, TER, AGR, EDU, IMM, JUR |
| 1979 | 12 | 78 | POL, ECO, SOC, JUR, ENV, TEC, CUL, SPO, TER, AGR, REL, SANT |
| 1980 | 14 | 76 | POL, ECO, SOC, JUR, ENV, TEC, CUL, SPO, TER, AGR, DEMO, IMM, MIL, SANT |
| 1981 | 13 | 84 | POL, ECO, SOC, EDU, TEC, CUL, SPO, TRA, TER, AGR, IMM, JUR, SANT |
| 1982 | 13 | 86 | POL, ECO, SOC, EDU, TEC, CUL, SPO, SCI, TER, AGR, DEMO, ENV, JUR |
| 1983-1997 | 222 | 1079 | 16-19 dimensions selon l'année |
| 1998-2007 | 175 | 792 | 11-19 dimensions |
| 2008-2017 | 161 | 827 | 14-17 dimensions |
| 2018-2026 | 158 | 2359 | 15-19 dimensions |
| 2028, 2030 (anomalies) | 4 | 4 | TEC, DIP |
| **TOTAL** | **805** | **5804** | (+336 plages = **6140**) |
