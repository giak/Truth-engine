# CLUSTER_PROCESSUS_FORENSIQUE.md — Format standard pour le processus forensique

## OBJECTIF

Définir le format standard pour la section "EXÉCUTION DE L'ENQUÊTE" des rapports APEX, garantissant la transparence du raisonnement et la reproductibilité de l'enquête.

## FORMAT MANDATORY

La section "EXÉCUTION DE L'ENQUÊTE" doit contenir les informations suivantes dans l'ordre strict :

### 1. 📋 Protocole d’investigation

Description succinte des phases exécutées au cours de l'investigation, avec les paramètres clés :

- **Date de début/fin**
- **Complexité initiale**
- **Budget de requêtes**
- **Type d'investigation** (APEX, COMPLEX, MEDIUM, SIMPLE)
- **Modes activés** (PERSO_FRESQUE, etc.)

Exemple :

> **Investigation APEX du 20/01/2026** — Crise agricole France Janvier 2026
>
> - Complexité : 8.7/10
> - Budget requêtes : 47 recherches
> - Modes : PERSO_FRESQUE (Annie Genevard)
> - Phases exécutées : L0-L9 Cascade

### 2. 🔍 Request Log (toutes les recherches)

Tableau structuré par branches d'investigation, listant chaque requête avec :

- **Numéro de requête** (séquentiel par branche)
- **Type de source** (◈, ◉, ○)
- **Requête** (texte exact)
- **Résultat** (extrait clé des résultats)
- **Source** (nom complet de la source)

Format par branche :

```markdown
#### BRANCH 1: [Nom de la branche] (X requêtes)

| #   | TYPE | QUERY                                 | RÉSULTAT                                        | SOURCE                          |
| --- | ---- | ------------------------------------- | ----------------------------------------------- | ------------------------------- |
| 1   | ◈    | Prévalence DNC Occitanie Jan 2026     | Rapport préfectoral: 3 foyers suspectés à Léran | Archives départementales Ariège |
| 2   | ◈    | Interdiction exportation DNC Jan 2026 | Arrêté du 15 jan: blocage vers Italie/Suisse    | Ministère Agriculture           |
```

### 3. 📊 Décompte sources

Récapitulatif des sources par type :

- **◈ PRIMARY** : Leaks, FOIA, court docs, data
- **◉ SECONDARY** : Investigative, academic, field
- **○ TERTIARY** : MSM, aggregators, official

Exemple :

> **Décompte sources**: ◈12 ◉19 ○16

## INTEGRATION DANS LES RAPPORTS

Toutes les sections du rapport doivent référencer les requêtes correspondantes dans le Request Log.

### Exemples de références

```markdown
Le plan "un poulailler par département" de Genevard (requête 18) est un effet d'annonce incapable de combler le déficit de 1.2 million de pondeuses (requête 13).

Les données CNPO montrent 27 tests positifs en 48h (requête 8), contredisant directement le tweet d'Annie Genevard.
```

## QUALITY GATES

La section "PROCESSUS FORENSIQUE" est vérifiée dans les Quality Gates avec les critères :

- ✅ Protocole d'investigation complet
- ✅ Request Log listant toutes les requêtes
- ✅ Décompte sources présent
- ✅ Références aux requêtes dans l'analyse

## CONSEILS

- Mettre à jour le Request Log en temps réel pendant l'investigation
- Utiliser des sources vérifiables (éviter les sources anonymes)
- Prioriser les sources primaires (◈) pour les informations sensibles
- Référencer chaque affirmation dans l'analyse

## EXEMPLE COMPLET

```markdown
## PART 1: EXÉCUTION DE L'ENQUÊTE

### 📋 PROTOCOLE D'INVESTIGATION

**Investigation APEX du 20/01/2026** — Crise agricole France Janvier 2026

- Complexité : 8.7/10
- Budget requêtes : 47 recherches
- Modes : PERSO_FRESQUE (Annie Genevard)
- Phases exécutées : L0-L9 Cascade

### 🔍 REQUEST LOG (47 recherches)

#### BRANCH 1: MENSONGE DNC (12 requêtes)

| #   | TYPE | QUERY                                 | RÉSULTAT                                        | SOURCE                          |
| --- | ---- | ------------------------------------- | ----------------------------------------------- | ------------------------------- |
| 1   | ◈    | Prévalence DNC Occitanie Jan 2026     | Rapport préfectoral: 3 foyers suspectés à Léran | Archives départementales Ariège |
| 2   | ◈    | Interdiction exportation DNC Jan 2026 | Arrêté du 15 jan: blocage vers Italie/Suisse    | Ministère Agriculture           |
| 3   | ◉    | Coût DNC élevage bovin 2026           | Étude INRA: 300€/tête + 50% baisse productivité | Journal officiel                |

#### BRANCH 2: PÉNURIE D'ŒUFS (14 requêtes)

| #   | TYPE | QUERY                              | RÉSULTAT                               | SOURCE     |
| --- | ---- | ---------------------------------- | -------------------------------------- | ---------- |
| 1   | ◉    | Déficit pondeuses France Jan 2026  | -1.2 million de pondeuses vs 2025      | INSEE      |
| 2   | ◈    | Importations œufs Ukraine Jan 2026 | +412% vs 2025: 1.8 million d'œufs/jour | Douanes EU |

#### BRANCH 3: NEXUS MERCOSUR (11 requêtes)

| #   | TYPE | QUERY                               | RÉSULTAT                          | SOURCE        |
| --- | ---- | ----------------------------------- | --------------------------------- | ------------- |
| 1   | ○    | Position Genevard Mercosur Jan 2026 | "Opposée, mais accord inévitable" | France Info   |
| 2   | ◈    | Lobbying agroalimentaire Mercosur   | 5.2 million € en 2025             | Leak lobbying |

#### BRANCH 4: GAZINGLIGHTING & RÉPRESSION (10 requêtes)

| #   | TYPE | QUERY                                   | RÉSULTAT                                      | SOURCE       |
| --- | ---- | --------------------------------------- | --------------------------------------------- | ------------ |
| 1   | ◈    | Pathologisation dissidence agricole     | Article L'Opinion: "Les éleveurs radicalisés" | Leak journal |
| 2   | ◉    | Taux arrestations manifesteurs Jan 2026 | 237 arrestations vs 187 en 2025               | Data justice |

### 📊 DÉCOMPTE SOURCES

**Décompte sources**: ◈12 ◉19 ○16
```
