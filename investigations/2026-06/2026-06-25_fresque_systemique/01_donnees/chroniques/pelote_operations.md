# Prompt Pelote — Opérations YAML dans les enquêtes

> Remplace les 5 scripts Python supprimés (standardize_pelote, cleanup_pelote_doublons, fix_final_gaps, complete_pelote, add_cross_reference).
> Utilise ce prompt quand un fichier d'enquête (INVESTIGATION.md) nécessite des corrections dans sa section `REMONTEE_DES_FILS`.
>
> Principe AFP : le LLM comprend le YAML et les variations de format — pas besoin de regex.

## Usage

1. Copier ce prompt
2. Lire le fichier d'enquête cible avec `read_files`
3. Exécuter les opérations demandées avec `str_replace`

---

## Contexte

Tu travailles sur des fichiers d'enquête dans `investigations/2026-06-25_fresque_systemique/02_enquetes/`.
Ces fichiers contiennent une section `REMONTEE_DES_FILS` avec du YAML listant les fils systémiques (A-H + I, L).

Chaque fil a cette structure YAML :

```yaml
    - fil: "X — Nom du fil"
      acte_naissance:
        date: "AAAA"
        evenement: "..."
        mecanisme_cree: "M##"
        source: "..."
      renforcements_historiques:
        - date: "AAAA"
          evenement: "..."
          mecanisme: "M##"
          source: "..."
      chaine_causale:
        - "..."
      manifestation_dans_evenement: "..."
```

## Opérations disponibles

### 1. Ajouter `marquage` et `pelote_verification`

Après `source:` dans `acte_naissance`, ajouter :

```yaml
        marquage: "[RACINE_XXX]"
        pelote_verification: "AAAA — Description de l'acte. Justification du marquage."
```

Table de marquage :

| Fil | Marquage | Pelote verification |
|-----|----------|---------------------|
| A | `[RACINE FONDATRICE]` | 1803 — Loi de Medecine (ventose an XI). Acte fondateur revolutionnaire autonome. |
| B | `[RACINE FONDATRICE]` | 1791 — Loi Le Chapelier. Acte fondateur revolutionnaire autonome. |
| C | `[RACINE FONDATRICE]` | 1791 — Loi Le Chapelier. Acte fondateur revolutionnaire commun avec fil B. |
| D | `[RACINE FONDATRICE]` | 1804 — Code civil napoleonien. Acte fondateur imperial autonome. |
| E | `[RACINE FONDATRICE]` | 1811 — Regime autoritaire de la presse. Post-revolutionnaire (dans fenetre 1789-1815). |
| F | `[RACINE FONDATRICE]` | 1808 — Universite napoleonienne. Acte fondateur imperial autonome. |
| G | `[RACINE FONDATRICE]` | 1789 — Declaration Droits de l'Homme. Acte fondateur revolutionnaire. |
| H | `[RACINE ANCIENNE] pre-revolutionnaire` | 1660-1715 — Colbertisme. Racine la plus profonde. Arret valide. |
| I | `[RACINE CONSTITUTIVE]` | 1992 — Traite de Maastricht. Acte fondateur moderne. Necessite pre-acte 1983 Virage rigueur. |
| L | `[MODERNE] justifie` | 1914 — Loi Caillaux (impot revenu). Fil moderne justifie car impot sur le revenu n'existe pas avant. |

### 2. Ajouter `gaps_verifies`

Apres chaque bloc `chaine_causale:`, ajouter :

```yaml
        gaps_verifies:
          - "Analyse automatique requise — veuillez verifier les ecarts > 30 ans dans la chaine causale"
```

### 3. Ajouter `cross_reference`

Apres chaque `manifestation_dans_evenement:`, ajouter :

```yaml
      cross_reference:
        referentiel: "2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"
        coherence: "XXX"
```

Table de coherence :

| Fil | coherence |
|-----|-----------|
| A | Acte 1803 confirme. Renforcements 1808, 1858, 1941, 1958 dans referentiel. |
| B | Acte 1791 confirme. Renforcements 1811, 1945, 1958 dans referentiel. |
| C | Acte 1791 confirme. Renforcements 1804, 1884, 1901 dans referentiel. |
| D | Acte 1804 confirme. Renforcements 1872, 1958 dans referentiel. |
| E | Acte 1811 confirme. Renforcements 1881, 1964 dans referentiel. |
| F | Acte 1808 confirme. Renforcements 1833, 1881, 1975 dans referentiel. |
| G | Acte 1789 confirme. Renforcements 1801, 1905, 1946 dans referentiel. |
| H | Acte 1660 confirme (RACINE ANCIENNE). Renforcements 1792, 1840, 1945 dans referentiel. |
| I | Acte 1992 confirme. Necessite pre-acte 1983 Virage rigueur documente. |
| L | Acte 1914 confirme (fil moderne justifie). Renforcements 1945, 2007, 2017 dans referentiel. |

### 4. Supprimer les doublons

Si un bloc YAML contient des champs en double (deux `marquage:` a la suite, deux blocs `cross_reference:` consecutifs, etc.), garder la premiere occurrence et supprimer la seconde.

### 5. Ajouter `chaine_causale` manquante

Si un fil n'a pas de bloc `chaine_causale:`, en ajouter un avec une chaine descriptive reliant l'acte de naissance aux renforcements jusqu'a l'evenement de l'enquete, suivi de `gaps_verifies:`.

---

## Exemple complet

Avant :
```yaml
    - fil: "B — Monopole d'État"
      acte_naissance:
        date: "1791"
        evenement: "Loi Le Chapelier"
        mecanisme_cree: "M05"
        source: "Loi Le Chapelier 1791"
      renforcements_historiques:
        - date: "1811"
          evenement: "Regime des tabacs et allumettes"
          mecanisme: "M05"
          source: "Referentiel §B2"
      chaine_causale:
        - "1791 (Le Chapelier) -> 1811 (monopole tabac) -> 1945 (nationalisations) -> evenement"
      manifestation_dans_evenement: "L'evenement illustre le monopole d'Etat"
```

Apres :
```yaml
    - fil: "B — Monopole d'État"
      acte_naissance:
        date: "1791"
        evenement: "Loi Le Chapelier"
        mecanisme_cree: "M05"
        source: "Loi Le Chapelier 1791"
        marquage: "[RACINE FONDATRICE]"
        pelote_verification: "1791 — Loi Le Chapelier. Acte fondateur revolutionnaire autonome."
      renforcements_historiques:
        - date: "1811"
          evenement: "Regime des tabacs et allumettes"
          mecanisme: "M05"
          source: "Referentiel §B2"
      chaine_causale:
        - "1791 (Le Chapelier) -> 1811 (monopole tabac) -> 1945 (nationalisations) -> evenement"
        gaps_verifies:
          - "1791->1811 : 20 ans — OK"
          - "1811->1945 : 134 ans — GAP. Renforcement manquant : 1871. A verifier."
          - "1945->evenement : XX ans — OK"
      manifestation_dans_evenement: "L'evenement illustre le monopole d'Etat"
      cross_reference:
        referentiel: "2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"
        coherence: "Acte 1791 confirme. Renforcements 1811, 1945, 1958 dans referentiel."
```
