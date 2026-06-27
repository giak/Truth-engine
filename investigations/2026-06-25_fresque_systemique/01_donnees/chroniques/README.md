# Chroniques 1975-2026

Découpage année × dimension de l'HYPER-MATRICE FRANCE.

Source : `01_donnees/2026-06-25_17-00_france_1975-2026_HYPER_MATRICE_UNIFIEE.md`

---

## Structure

```
chroniques/
  README.md
  plages_annees.md         ← événements sans année unique (ex: 1980-2000)
  1975/
    1975_POL.md            ← événements politiques de 1975
    1975_ECO.md            ← événements économiques de 1975
    1975_SOC.md
    ...
  1976/
    1976_POL.md
    ...
```

- **825 fichiers** répartis dans **66 dossiers années** (1944-2060)
- **5 989 événements** dans les fichiers année×dimension
- **338 événements** dans `plages_annees.md` (plages d'années)
- **Dont 5 966 dans la période 1975-2026**, 23 hors période (données historiques issues des suppléments)

---

## Format d'un fichier chronique

Chaque fichier `YYYY_DIM.md` suit ce format strict :

```markdown
### YYYY_DIM

| Année | Dimension | Description | Code |
|---|---|---|---|
| 2024 | POL | Texte de l'événement | ✅ |
| 2024 | POL | Autre événement | ⚠ |
```

**Règles :**
- La description commence par une majuscule, pas de point final
- Pas de pipe `|` dans la description (échapper ou reformuler)
- L'année dans la 1ʳᵉ colonne = année du dossier (cohérence obligatoire)
- Le fichier s'appelle `AAAA_DIM.md` (ex: `2024_POL.md`)

---

## Les 4 codes d'impact

| Code | Signification | Quand l'utiliser |
|------|--------------|------------------|
| ✅ | Positif / constructif | Loi votée, innovation, progrès social, réussite |
| ⚠ | Préoccupant / alerte | Tension, risque, réforme avortée, transition |
| ❌ | Négatif / critique | Répression, échec, crise, blocage, austérité |
| 💀 | Fatal / catastrophique | Crime, attentat, catastrophe, scandale majeur |

---

## Comment ajouter un événement

Voir `PROTOCOLE_ENRICHISSEMENT.md` pour la méthode complète (AFP-compliant : pas de script, le LLM écrit directement).

### Principes

1. **Lire** le fichier cible `chroniques/AAAA/AAAA_DIM.md` — ou le créer s'il n'existe pas (template ci-dessous)
2. **Vérifier** que le fait n'est pas déjà présent (déduplication sémantique)
3. **Ajouter** la ligne à la fin du tableau, AVANT la ligne vide finale
4. **Mettre à jour** le compteur dans l'en-tête (`> N événement(s)`)

### Template si le fichier n'existe pas

```markdown
# Chronique AAAA — Dimension DIM

> Fait atomique extrait de l'HYPER-MATRICE FRANCE 1975-2026.
> 0 événement(s) classé(s) dans la dimension DIM pour l'année AAAA.

| Année | Dimension | Description | Code |
|---|---|---|---|
```

### Si l'année est une plage (ex: 2020-2024)

**Plage courte (≤ 5 ans) :** ranger le fait dans le dossier de l'année de fin (`2024/`), utiliser la plage dans la colonne Année.

**Plage longue (> 5 ans ou décennie complète) :** ajouter dans `plages_annees.md`.

### Si un rapport révèle un fait passé

**Deux lignes :** une pour le fait historique (plage), une pour la révélation (année du rapport).

### Après modification

(Optionnel) Ajouter la même ligne dans le fichier maître HYPER_MATRICE_UNIFIEE.

---

## Dimensions disponibles (20)

| Code | Dimension | Nb événements | Années couvertes |
|------|-----------|:-------------:|:----------------:|
| AGR | Agriculture | 254 | 55 |
| CUL | Culture, médias | 365 | 52 |
| DEMO | Démographie | 70 | 27 |
| DIP | Diplomatie | 92 | 21 |
| ECO | Économie, finances | 1 244 | 53 |
| EDU | Éducation | 318 | 43 |
| ENV | Environnement | 206 | 48 |
| IMM | Immigration | 111 | 48 |
| JUR | Justice, droit | 494 | 53 |
| MED | Média | 173 | 18 |
| MIL | Militaire | 187 | 35 |
| POL | Politique, institutions | 803 | 52 |
| REL | Religion | 36 | 23 |
| SANT | Santé | 186 | 48 |
| SCI | Science, recherche | 43 | 27 |
| SOC | Social, démographie | 659 | 53 |
| SPO | Sport | 243 | 52 |
| TEC | Technologie, industrie | 321 | 52 |
| TER | Terrorisme | 69 | 24 |
| TRA | Transports | 115 | 40 |

---

## Répartition des codes d'impact

| Code | Occurrences | Proportion |
|------|:-----------:|:----------:|
| ❌ Négatif | 2 101 | 35,1 % |
| ⚠ Préoccupant | 1 652 | 27,6 % |
| ✅ Positif | 1 016 | 17,0 % |
| 💀 Fatal | 478 | 8,0 % |
| *Non standard* | *742* | *12,4 %* |
| **Total** | **5 989** | **100 %** |

---

## Pourquoi ce découpage ?

- **Chargeable instantanément** par un LLM (1-50 événements par fichier)
- **Maintenable** : on ajoute un événement sans toucher au reste
- **Navigable** : on charge l'année ET la dimension pertinente
- **Référençable** : `chroniques/2024/2024_POL.md` est une adresse stable
- **Évolutif** : on peut enrichir 2026 sans recharger 1975
