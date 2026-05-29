# CLUSTER_REQUEST_LOG.md — Format standard pour le REQUEST LOG

## OBJECTIF

Standardiser la présentation des recherches dans les rapports APEX pour garantir la transparence et la reproductibilité.

## FORMAT MANDATORY

Toutes les recherches effectuées dans une investigation doivent être listées dans un tableau structuré avec les informations suivantes :

## TABLEAU REQUEST LOG

| #   | TYPE | QUERY     | RÉSULTAT      | SOURCE       |
| --- | ---- | --------- | ------------- | ------------ |
| 1   | ◈    | [requête] | [extrait clé] | [nom source] |
| 2   | ◉    | [requête] | [extrait clé] | [nom source] |
| ... | ...  | ...       | ...           | ...          |

## COLONNES DÉTAILLÉES

### 1. NUMÉRO (#)

- Numéro séquentiel de la requête
- Démarre à 1 pour chaque branche
- Facilite les références dans les justifications

### 2. TYPE DE SOURCE (TYPE)

- Utiliser les symboles DSL :
  - ◈ : PRIMARY (Leak, FOIA, court docs, data)
  - ◉ : SECONDARY (Investigative, academic, field)
  - ○ : TERTIARY (MSM, aggregators, official)
- Ce champ est obligatoire pour la stratification EDI

### 3. REQUÊTE (QUERY)

- Texte exact de la requête effectuée (en français)
- Inclure des mots-clés spécifiques à la branche
- Exemples valides :
  - "Prévalence DNC Occitanie Jan 2026"
  - "Importations œufs Ukraine Jan 2026"
  - "Votes Mercosur Strasbourg Jan 20"

### 4. RÉSULTAT (RÉSULTAT)

- Extrait clé des résultats (max 200 caractères)
- Prioriser les informations factuelles vérifiables
- Exemples valides :
  - "Rapport préfectoral: 3 foyers suspectés à Léran"
  - "Douanes EU: +412% vs 2025"
  - "Vote: 412 pour, 389 contre"

### 5. SOURCE (SOURCE)

- Nom complet de la source (pas seulement le domaine)
- Inclure des détails spécifiques :
  - Archives départementales Ariège
  - Données CNPO
  - Médiapart
  - Journal officiel
- Exemples invalides (trop vagues) :
  - "Site internet"
  - "Article de presse"
  - "Source fiable"

## GROUPE PAR BRANCHES

Les requêtes doivent être regroupées par branches d'investigation avec un sous-titre clairement identifié :

### BRANCH 1: [Nom de la branche] (X requêtes)

| #   | TYPE | QUERY | RÉSULTAT | SOURCE |
| --- | ---- | ----- | -------- | ------ |
| 1   | ◈    | ...   | ...      | ...    |

### BRANCH 2: [Nom de la branche] (X requêtes)

| #   | TYPE | QUERY | RÉSULTAT | SOURCE |
| --- | ---- | ----- | -------- | ------ |
| 1   | ◉    | ...   | ...      | ...    |

## DÉCOMPTE FINAL

À la fin du REQUEST LOG, ajouter un décompte récapitulatif des sources :

**📊 DÉCOMPTE RECHERCHES: ◈X ◉X ○X**

## INTEGRATION DANS LES JUSTIFICATIONS

Toutes les affirmations dans l'analyse doivent référencer la requête correspondante :

Exemple valide :

> Le plan "un poulailler par département" de Genevard (requête 18) est un effet d'annonce incapable de combler le déficit de 1.2 million de pondeuses (requête 13).

## QUALITY GATES

Le REQUEST LOG est vérifié dans les Quality Gates avec les critères :

- ✅ Toutes les recherches listées (aucune omission)
- ✅ Chaque requête a un type de source
- ✅ Chaque requête a un résultat
- ✅ Chaque requête a une source valide
- ✅ Groupement par branches
- ✅ Détail de la stratification des sources

## EXEMPLE COMPLET

```markdown
### BRANCH 1: MENSONGE DNC (12 requêtes)

| #   | TYPE | QUERY                                 | RÉSULTAT                                        | SOURCE                          |
| --- | ---- | ------------------------------------- | ----------------------------------------------- | ------------------------------- |
| 1   | ◈    | Prévalence DNC Occitanie Jan 2026     | Rapport préfectoral: 3 foyers suspectés à Léran | Archives départementales Ariège |
| 2   | ◈    | Interdiction exportation DNC Jan 2026 | Arrêté du 15 jan: blocage vers Italie/Suisse    | Ministère Agriculture           |
| 3   | ◉    | Coût DNC élevage bovin 2026           | Étude INRA: 300€/tête + 50% baisse productivité | Journal officiel                |
```

## CONSEILS

- Mettre à jour le REQUEST LOG en temps réel pendant l'investigation
- Vérifier chaque ligne pour la cohérence et la précision
- Utiliser des sources vérifiables (éviter les sources anonymes)
- Prioriser les sources primaires (◈) pour les informations sensibles

---

## PROTOCOLE D'INVESTIGATION (de CLUSTER_PROCESSUS_FORENSIQUE)

Description succinte des phases exécutées au cours de l'investigation :

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

## DÉCOMPTE SOURCES

Récapitulatif des sources par type :

- **◈ PRIMARY** : Leaks, FOIA, court docs, data
- **◉ SECONDARY** : Investigative journalism, academic research
- **○ TERTIARY** : MSM, aggregators, official

Exemple :

> **Décompte sources**: ◈12 ◉19 ○16

## INTÉGRATION DANS LES RAPPORTS

Toutes les sections du rapport doivent référencer les requêtes correspondantes dans le Request Log.

Exemples de références :

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

## EXEMPLE COMPLET (PROTOCOLE + REQUEST LOG)

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
