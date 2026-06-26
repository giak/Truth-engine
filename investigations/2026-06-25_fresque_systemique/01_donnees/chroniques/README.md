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

**Utiliser l'outil CLI** `tools/enrich_chronique.py` (voir `PROTOCOLE_ENRICHISSEMENT.md` pour la méthode complète).

### Cas simple (année unique)

```bash
python3 tools/enrich_chronique.py 2024_SOC.md "| 2024 | SOC | Description précise | ⚠ |"
```

L'outil gère : création du dossier si besoin, template correct (accents, format), détection des doublons, mise à jour du compteur en en-tête.

### Si le fichier n'existe pas

Même commande, l'outil crée le dossier et le fichier automatiquement :

```bash
python3 tools/enrich_chronique.py 1945_DIP.md "| 1945-12-26 | DIP | Création du franc CFA | ❌ |"
```

### Si l'année est une plage (ex: 2020-2024)

**Plage courte (≤ 5 ans) :** ranger le fait dans le dossier de l'année de fin, utiliser la plage dans la colonne Année :

```bash
python3 tools/enrich_chronique.py 2024_SANT.md "| 2020-2024 | SANT | Sous-financement cumulé Ségur : 1,7 Md€ | ❌ |"
```

→ Plage dans la colonne Année (`2020-2024`), fichier dans le dossier de l'année de fin (`2024/`).

**Plage longue (> 5 ans ou décennie complète) :** ajouter dans `plages_annees.md` comme avant.

```bash
python3 tools/enrich_chronique.py --file plages_annees.md "| 1980-2000 | SANT | Évolution du système de santé | ⚠ |"
```

→ L'outil enrich_chronique.py gère aussi `plages_annees.md` avec `--file`.

### Si un rapport révèle un fait passé (cas fréquent)

**Deux lignes :** une pour le fait historique (plage d'années), une pour la révélation (année du rapport).

```bash
# Ligne historique : dans le dossier de l'année de fin
python3 tools/enrich_chronique.py 2024_SANT.md "| 2020-2024 | SANT | Sous-financement cumulé Ségur : 1,7 Md€ | ❌ |"

# Ligne révélation : dans le dossier de l'année du rapport
python3 tools/enrich_chronique.py 2026_SANT.md "| 2026 | SANT | Rapport IGAS révèle le sous-financement Ségur de 1,7 Md€ (18 fév 2026) | ❌ |"
```

### Après modification

(Optionnel) Ajouter la même ligne dans le fichier maître :
`01_donnees/2026-06-25_17-00_france_1975-2026_HYPER_MATRICE_UNIFIEE.md`

L'outil enrich_chronique.py met à jour le fichier chronique. Le fichier maître est une copie de consolidation — utile si tu veux garder l'hyper-matrice synchronisée, mais pas nécessaire pour le fonctionnement des chroniques.

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
