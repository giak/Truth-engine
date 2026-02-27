# INVESTIGATOR

**Assistant Cognitif d'Enquête Journalistique basé sur la Compression Sémantique**

---

## Aperçu

INVESTIGATOR est un système de prompt engineering utilisant la compression sémantique pour créer un assistant cognitif d'investigation journalistique. Il combine raisonnement structuré, préparation de recherches, gestion de preuves, analyse de relations et construction de chronologies dans un système unifié optimisé pour l'économie de tokens (~1200 tokens).

---

## Structure du Projet

```
investigator/
├── prompt.md                    # Prompt système à copier dans votre LLM
├── templates/
│   └── memory/                  # Templates pour la persistance
│       ├── entities.md          # Registre des entités
│       ├── sources.md           # Sources et fiabilité
│       ├── hypotheses.md        # Pistes et hypothèses
│       ├── timeline.md          # Chronologie
│       ├── graph.md             # Relations et graphe
│       └── search_log.md        # Historique recherches
├── examples/
│   └── phantom_foundations.md   # Exemple complet d'utilisation
├── docs/
│   └── plans/
│       └── 2026-02-21-investigator-design.md  # Document de design
└── doc_source/                  # Sources documentaires
    ├── brainstorm.md            # Processus de brainstorming
    └── cs.txt                   # Guide compression sémantique
```

---

## Démarrage Rapide

### 1. Activer INVESTIGATOR

Copiez le contenu de `prompt.md` et collez-le au début de votre conversation avec un LLM.

### 2. Fournir l'Input

```
Using INVESTIGATOR, analyze:

[input: description, documents, ou requête]

Mode: [exploratory|verification|synthesis|reporting]
Output: [report|executive|graph|timeline|evidence|guide]
```

### 3. Persister la Mémoire

Créez un dossier dans `investigation/{YYYY-MM-DD}_{slug}/` et utilisez les templates pour sauvegarder l'état de l'enquête.

---

## Composants Cognitifs

| Symbole | Composant | Fonction |
|---------|-----------|----------|
| ΩI | Investigation Core | Coordination et raisonnement |
| Ξ | Research Engine | Préparation des recherches |
| Θ | Thread Tracker | Pistes et hypothèses |
| Φ | Fact Evaluator | Évaluation des preuves |
| Γ | Graph Builder | Entités et relations |
| Τ | Timeline Engine | Chronologie |
| Μ | Memory | Contexte et persistance |

---

## Formats de Sortie

| Format | Description |
|--------|-------------|
| `report` | Rapport d'enquête complet |
| `executive` | Synthèse exécutive |
| `graph_output` | Graphe de relations |
| `timeline_output` | Chronologie structurée |
| `evidence_dossier` | Dossier de preuves |
| `guide` | Guide d'investigation |

---

## Fonctionnalités

- ✅ Extraction d'entités (personnes, organisations, lieux, événements, documents, flux financiers)
- ✅ Graphe de relations avec détection d'anomalies
- ✅ Timeline chronologique avec détection de lacunes
- ✅ Gestion des preuves avec échelle de fiabilité
- ✅ Préparation de recherches web multi-disciplinaires
- ✅ Analyse herméneutique de l'input
- ✅ Mémoire persistante avec horodatage

---

## Principes

1. **Intégrité des sources** - Toute affirmation attribuée à une source vérifiable
2. **Transparence de la confiance** - Niveaux d'incertitude explicites
3. **Neutralité des hypothèses** - Recherche active de preuves contradictoires
4. **Précision temporelle** - Les dates comptent
5. **Clarté des entités** - Distinction relations confirmées vs inférées

---

## Documentation

- [Design Document](docs/plans/2026-02-21-investigator-design.md) - Spécifications complètes
- [Exemple d'utilisation](examples/phantom_foundations.md) - Scénario d'enquête fictive

---

## Références

- [Compression Sémantique - Guide Complet](https://giak.gitlab.io/portfolio/article/ai/compression-semantique-guide.html) par Christophe Giacomel

---

## Licence

MIT
