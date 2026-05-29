# Convention de Nommage - Truth Engine

## Règle Générale

**Format obligatoire**: `YYYY-MM-DD_HH-MM_<sujet>_<type>.md`

## Dossiers Concernés

- `investigations/`
- `articles/`
- `outputs/`

## Structure du Nom

| Élément | Format | Exemple |
|---------|--------|---------|
| Date | `YYYY-MM-DD` | `2026-03-16` |
| Heure | `HH-MM` | `14-30` |
| Sujet | `kebab-case` | `reseaux_influence_elections` |
| Type | `MAJUSCULES` | `ARTICLE`, `HYPER_MATRICE`, `ARCHITECTURE` |

## Types de Fichiers

| Type | Description |
|------|-------------|
| `ARTICLE` | Article final prêt pour publication |
| `HYPER_MATRICE` | Matrice de données avec faits atomiques |
| `ARCHITECTURE` | Architecture narrative + thèse |
| `SATURATION_AUDIT` | Audit de vérification |
| `REGISTRE` | Registre systémique |
| `INVESTIGATION` | Enquête brute |
| `CONCLUSION` | Conclusions de l'enquête |

## Exemples

```
2026-03-16_14-30_reseaux_influence_elections_ARTICLE.md
2026-03-16_10-15_electeurs_bourreaux_HYPER_MATRICE.md
2026-03-16_09-00_electeurs_bourreaux_ARCHITECTURE.md
2026-03-16_09-30_electeurs_bourreaux_SATURATION_AUDIT.md
```

## Règles

1. **Date** = date de création ou de modification majeure
2. **Heure** = heure de création (optionnel si même jour)
3. **Sujet** = sujet principal en kebab-case (minuscules, tirets)
4. **Type** = en majuscules, underscore si plusieurs mots
5. **Pas d'espaces** = toujours kebab-case ou underscores
6. **Pas d'accents** = pas de caractères accentués dans les noms de fichiers

## Application

Cette règle s'applique à TOUT nouveau fichier créé dans ces dossiers.
