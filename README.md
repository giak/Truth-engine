# Truth Engine

**Version**: 11.0
**Principe**: Analyse épistémique hostile. "Un récit = propagande. Cinq récits = cartographie."

---

## What's New in v11.0

### KERNEL v11.0 - Cognitive Operating System
- **DSL complet**: Ξ € Λ Ω Ψ primitives avec formules exécutables
- **Hierarchical Pattern Activation (HPA)**: 4 niveaux d'activation (Core → Clusters → Specialized → Edge Cases)
- **Source Stratification**: ◈◉○ tiers avec confidence scores
- **Narrative Mapping**: 5 perspectives (⟐ ⟐̅ 🌍 🎓 🔥)
- **MnemoLite Integration**: Phase 0.5 MEMORY_LOOKUP automatique

### Architecture 3-Piliers
- **core/**: Système DSL uniquement (KERNEL + patterns + protocoles)
- **outputs/**: Productions générées (investigations, articles, social)
- **tools/**: Infrastructure (docs, tests, scripts)

---

## Structure

```
truth-engine/
├── README.md                    # Ce fichier
├── DISCLAIMER.md                # Avertissements légaux
├── KERNEL.md → core/KERNEL.md   # Point d'entrée du DSL
├── STRUCTURE.md                 # Documentation de la structure
├── package.json                 # Dépendances
│
├── 📦 core/                     # SYSTÈME - Le DSL et patterns
│   ├── KERNEL.md               # Cœur du DSL v11.0
│   ├── patterns/               # 19 clusters de patterns cognitifs
│   │   ├── CLUSTER_ICEBERG.md
│   │   ├── CLUSTER_MONEY.md
│   │   └── ...
│   ├── protocols/              # Protocoles d'investigation
│   │   ├── INVESTIGATION.md
│   │   ├── INVESTIGATION_TREE.md
│   │   ├── OUTPUT_TEMPLATE.md
│   │   └── VALIDATION.md
│   └── dsl/                    # Fichiers DSL
│       ├── COGNITIVE_DSL.md
│       ├── COGNITIVE_DSL_CORE.md
│       ├── MACROS.md
│       └── PATTERNS.md
│
├── 📤 outputs/                  # PRODUCTIONS - Résultats
│   ├── investigations/         # Rapports d'investigation
│   ├── articles/               # Articles Substack
│   ├── social/                 # Tweets, threads
│   ├── logs/                   # Logs historiques
│   ├── results/                # Résultats de tests
│   └── simulations/            # Simulations APEX
│
├── 🛠️ tools/                    # INFRASTRUCTURE
│   ├── docs/                   # Documentation
│   │   ├── user/               # USER_GUIDE.md, PHILOSOPHY.md
│   │   ├── dev/                # MCP, MnemoLite
│   │   ├── specs/              # TAD.md, PRD.md, VISION.md
│   │   ├── audits/             # Audits et analyses
│   │   ├── article-plans/      # Plans d'articles
│   │   └── plans/              # Roadmap et designs
│   ├── tests/                  # Tests et validations
│   ├── scripts/                # Scripts utilitaires
│   └── prompts/                # Prompts et templates
│
└── 🗄️ archive/                  # ARCHIVES
    ├── backups/
    ├── investigations/
    └── projects/
```

---

## Usage

### Démarrage rapide

```bash
# Charger le KERNEL
claude-code "Charge core/KERNEL.md et initialise Truth Engine v11.0"

# Investigation simple
claude-code "Analyse: [sujet]. Truth Engine protocol."

# Investigation APEX complète
claude-code "Investigation APEX: [sujet complexe].
Load core/KERNEL.md + core/patterns/ + core/protocols/.
Target: EDI≥0.80, sources≥20, wolves≥8 si politique.
Save outputs/investigations/YYYY-MM-DD_sujet.md"
```

### Avec MnemoLite

```bash
# Investigation avec mémoire
claude-code "Analyse [sujet]. Use MnemoLite MCP pour semantic search.
Truth Engine v11.0 protocol avec MEMORY_LOOKUP phase 0.5."
```

---

## Boot Sequence (KERNEL v11.0)

```
STATUS: KERNEL LOADED
MODE:   Truth Engine v11.0
AXIOM:  Empire of Lies (95% suspicion baseline)

PRIMITIVES ACTIVE:
  Ξ € Λ Ω Ψ → pattern detection reflexes
  ◈ ◉ ○    → source stratification
  ⟐ ⟐̅ 🌍 🎓 🔥 → narrative mapping
```

---

## Phases d'Investigation (v11.0)

| Phase | Description | Output |
|-------|-------------|--------|
| 0 | TEMPORAL - Capture date | CURRENT_DATE |
| 0.5 | MEMORY_LOOKUP - MnemoLite | Prior investigations |
| 1 | COMPLEXITY_SCAN | SIMPLE/MEDIUM/COMPLEX/APEX |
| 2 | CONCEPT_ACTIVATION | Patterns chargés |
| 3 | TEXTUAL_ANALYSIS | ≥8 concepts analysés |
| 4 | QUERY_GENERATION | Budget requêtes |
| 5 | SPG INVESTIGATION | Systemic Pattern Graph |
| 6 | SOURCE_EVALUATION | EDI calculé |
| 7 | OUTPUT | Rapport structuré |
| 8 | SEARCH_INDEX | Résumé 200-400 mots |
| 9 | KNOWLEDGE_SAVE | MnemoLite memory |

---

## DSL Commands (v11.0)

| Command | Execution |
|---------|-----------|
| `LOAD: <path>` | Read file, integrate context |
| `SCAN: <target>` | Systematic analysis, score [0-10] |
| `SCORE: [0-10]` | Assign score with justification |
| `SEARCH: <query>` | Web search with stratification ◈◉○ |
| `CALCULATE: <X>` | Compute formula, show work |
| `OUTPUT: <format>` | Generate structured output |

---

## KB Files Essentiels (core/)

| File | Contenu | Location |
|------|---------|----------|
| `KERNEL.md` | DSL complet v11.0 | `core/` |
| `CLUSTER_*.md` | 19 patterns clusters | `core/patterns/` |
| `INVESTIGATION.md` | Protocoles L0-L9 | `core/protocols/` |
| `INVESTIGATION_TREE.md` | Multi-branch dialectical | `core/protocols/` |
| `OUTPUT_TEMPLATE.md` | Template de sortie | `core/protocols/` |
| `VALIDATION.md` | Post-search validation | `core/protocols/` |
| `COGNITIVE_DSL.md` | Formulas et symboles | `core/dsl/` |

---

## Quality Gates (v11.0)

Avant output, vérifier:

- [ ] Textual analysis présente? (≥8 concepts analysés)
- [ ] Techniques explicitement nommées? (DSL terms)
- [ ] Sous-entendus révélés? (≥3)
- [ ] Dialectique mappée? (thesis/antithesis/synthesis)
- [ ] EDI ≥ target? (par complexité)
- [ ] Sources stratifiées? (◈◉○ visibles)
- [ ] REQUEST LOG complet? (toutes recherches listées)
- [ ] MnemoLite integration? (memory lookup performed)
- [ ] Calculations done? (EDI, complexity score)
- [ ] Branches synthesis? (≥5 pour APEX)
- [ ] Wolf mapping? (≥8 acteurs pour APEX)

---

## MCP: MnemoLite Integration

Configuration `.mcp.json`:

```json
{
  "mcpServers": {
    "mnemolite": {
      "command": "bash",
      "args": ["/home/giak/Work/MnemoLite/scripts/mcp_server.sh"],
      "env": {
        "DOCKER_COMPOSE_PROJECT": "mnemolite"
      }
    }
  }
}
```

**Usage**:
- Index KB: `index_project(project_path="/home/giak/projects/truth-engine/core", repository="truth-engine")`
- Search: `search_code(query="pattern detection")`
- Save: `write_memory(title="...", content="...", memory_type="investigation")`

---

## Workflow

### 1. Analyse simple (SIMPLE)
```bash
claude-code "Analyse: 'Chômage 7.4%'. Truth Engine."
```

### 2. Investigation complexe (COMPLEX)
```bash
claude-code "Investigation COMPLEX: [sujet politique].
Load core/KERNEL.md.
Target: EDI≥0.70, sources≥15, wolves≥8."
```

### 3. Investigation APEX (maximum depth)
```bash
claude-code "Investigation APEX: [sujet hautement complexe].
Load core/KERNEL.md + core/protocols/INVESTIGATION_TREE.md.
Multi-perspective tree.
Target: EDI≥0.80, sources≥20, wolves≥12."
```

---

## Évolution

**Principe KISS**:
- Problème détecté → Fix direct core/
- Pattern manquant → Ajouter `core/patterns/`
- Formula imprécise → Ajuster `core/dsl/`

**Documentation développement**: Voir `tools/docs/`

**Pas de roadmap complexe**. Use → feedback → improve → repeat.

---

## Changelog

- **v11.0** (2026-01-30): Reorganisation 3-piliers, KERNEL v11.0, structure clean
- **v8.4** (2025-11-16): Investigation Tree, Query Optimization v8.3
- **v8.0** (2025-11-09): Base system

---

**Truth Engine v11.0** — KISS edition. Zero bullshit, pure signal.

**Status**: Production-ready, structure reorganized.
