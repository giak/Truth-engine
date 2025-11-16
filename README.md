# Truth Engine

**Version**: 8.4
**Principe**: Analyse épistémique hostile. "Un récit = propagande. Cinq récits = cartographie."

---

## What's New in v8.4

### Query Optimization v8.3 (Automatic)
- **Automatic query splitting**: Queries >5 keywords → split into 2-3 simple queries
- **Hybrid fallback**: MCP (DuckDuckGo) → WebSearch (Google) fallback
- **Productive query rate**: 0-40% baseline → 80-100% optimized
- **PRIMARY source discovery**: +20-50% improvement (official docs, government sites)
- **Documentation**: [tests/query_optimization/](tests/query_optimization/)

### Investigation Tree
- **Dialectical decomposition**: Single narrative → Multi-perspective investigation tree
- **Tree depth**: L0-L9 protocols, COMPARABLES_ASYMMETRY analysis
- **KB reference**: [kb/INVESTIGATION_TREE.md](kb/INVESTIGATION_TREE.md) (949 lines)
- **Tests & validation**: [tests/tree/](tests/tree/) (phases 1-2, simulations)

### Architecture Dual-Engine VALIDATED
- **WebSearch** (Google API official): 95%+ success rate
- **MCP web-search** (DuckDuckGo): 60-80% success rate
- **Decision**: Google Search MCP integration ABANDONED (0% success, see [postmortem](docs/postmortems/2025-11-16-google-search-mcp-ABANDONED.md))
- **Configuration**: WebSearch + MCP auto-approval → No manual permission prompts

---

## Structure

```
truth-engine/
├── README.md                    # Ce fichier
├── CLAUDE.md                    # Claude Code instructions
├── system.md                    # Instructions LLM (v7.17)
├── PFD.md                       # Philosophical Foundation (148 concepts)
├── PRD.md                       # Product Requirements (v7.15.1)
├── TAD.md                       # Technical Architecture
├── VISION.md                    # Vision document
├── DASHBOARD.md                 # Dashboard (minimal)
├── kb/                          # Knowledge base (formulas, patterns, protocols)
│   ├── COGNITIVE_DSL.md         # Formulas (IVF/ISN/EDI), symbols, concepts
│   ├── SEARCH_EPISTEMIC.md      # Source classification ◈◉○, EDI 6D
│   ├── PATTERNS.md              # 20 patterns manipulation
│   ├── QUERY_TEMPLATES.md       # Search templates, H7 adversary map
│   ├── INVESTIGATION.md         # Protocols L0-L9
│   ├── INVESTIGATION_TREE.md    # NEW v8.4: Tree investigation protocols
│   ├── VALIDATION.md            # Post-search validation
│   └── HANDOFF_MEMO.md          # Multi-conversation iteration
├── logs/                        # Investigations (auto-created, gitignored)
├── docs/                        # Development documentation
│   ├── development/
│   │   ├── autosave/            # Auto-save system dev docs
│   │   └── mnemolite/           # MnemoLite integration dev docs
│   ├── postmortems/             # NEW v8.4: Failed integration analyses
│   ├── plans/                   # Implementation plans
│   │   └── archived/            # Abandoned plans
│   └── memory/                  # Decision memory files
├── tests/                       # Validation tests & reports
│   ├── tree/                    # NEW v8.4: Investigation Tree validation
│   └── query_optimization/      # NEW v8.3: Query optimization tests
├── prompts/                     # Prompt templates (TWEET generation, etc.)
├── .claude/                     # Claude Code config + hooks
│   ├── hooks/                   # SessionStart, Stop, UserPromptSubmit
│   ├── settings.local.json      # Hook configuration + MCP auto-approval
│   └── .mcp.json                # MCP server configuration
├── .gitignore                   # Git exclusions
└── NOTES.md                     # Évolutions/améliorations (à créer au besoin)
```

---

## Usage

### Claude Code (recommandé)

```bash
# Investigation directe
claude-code "Analyse [sujet]. Charge system.md + kb/*.md. Protocole Truth Engine complet."

# Avec MnemoLite embeddings (si configuré)
claude-code "Analyse [sujet]. Use MnemoLite MCP pour semantic search KB. Truth Engine protocol."

# Investigation APEX avec Investigation Tree
claude-code "Investigation APEX: [sujet complexe].
Load system.md + kb/INVESTIGATION_TREE.md.
Multi-branch dialectical analysis.
Target: EDI≥0.80, sources≥20, wolves≥8 si politique.
Save logs/YYYY-MM-DD_sujet.md"
```

**Auto-approval configuré** (v8.4): WebSearch et MCP tools ne demandent plus de permissions manuelles.

### Claude.ai Projects (fallback)

Upload `system.md` + `kb/` dans Project Knowledge → investigate normalement.

**Limite**: 10 searches/conversation (nécessite HANDOFF multi-conversations si complex).

---

## MCP: MnemoLite Integration

Si MnemoLite MCP configuré (voir [docs/development/mnemolite/](docs/development/mnemolite/) pour setup complet):

```json
// .mcp.json (à la racine du projet)
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

**Prérequis**: MnemoLite Docker running (`cd /home/giak/Work/MnemoLite && docker compose up -d`)

**Usage**:
- Index KB: Via MCP tool `index_project(project_path="/home/giak/projects/truth-engine/kb", repository="truth-engine-kb")`
- Claude Code auto-utilise `search_code` pour semantic search KB contextuel
- Auto-save conversations: Hooks sauvegardent automatiquement dans MnemoLite

**Avantage**: Semantic search KB > chargement linéaire fichiers.

**Documentation**: Voir [MnemoLite QUICKSTART.md](/home/giak/Work/MnemoLite/QUICKSTART.md)

---

## Auto-Save System

Truth Engine utilise un système de sauvegarde automatique des conversations via MnemoLite MCP.

**Fonctionnement**:
- **Hook Stop** (PRIMARY): Sauvegarde immédiate après chaque réponse de Claude (latence 0)
- **Hook UserPromptSubmit** (BACKUP): Failsafe si Stop échoue
- **Hook SessionStart**: Vérification automatique de santé au démarrage

**Configuration**: Automatique si MnemoLite MCP configuré (voir `.claude/hooks/`)

**Validation au démarrage**:
```
═══════════════════════════════════════════════════════════
  ✅ AUTO-SAVE SYSTEM: ACTIVE & HEALTHY
═══════════════════════════════════════════════════════════
  MnemoLite:     Running
  Hook Stop:     Installed & Configured
  API Health:    OK
═══════════════════════════════════════════════════════════
```

**Si erreur**: Le hook SessionStart CRIE avec instructions de fix détaillées.

**Documentation complète**: Voir [docs/development/autosave/AUTOSAVE_COMPLETE.md](docs/development/autosave/AUTOSAVE_COMPLETE.md)

---

## Workflow

### 1. Analyse simple (SIMPLE complexity)
```bash
claude-code "Analyse: 'Chômage 7.4%'. Truth Engine."
```

**Expected**:
- Query Optimization v8.3 automatic splitting (if needed)
- Dual-engine search (WebSearch + MCP web-search)
- EDI ≥ 0.30, sources ≥ 7

### 2. Investigation complexe (COMPLEX complexity)
```bash
claude-code "Investigation COMPLEX: [sujet politique/géopolitique].
Load system.md + kb/.
Target: EDI≥0.70, sources≥15, wolves≥8.
Save logs/YYYY-MM-DD_sujet.md"
```

**Expected**:
- Query Optimization: 10-15 queries auto-split + hybrid fallback
- Investigation Tree: Multi-branch dialectical analysis
- EDI ≥ 0.70, ISN ≥ 9.0 (political topics)

### 3. Investigation APEX (maximum depth)
```bash
claude-code "Investigation APEX: [sujet hautement complexe].
Load system.md + kb/INVESTIGATION_TREE.md.
Multi-perspective tree, COMPARABLES_ASYMMETRY analysis.
Target: EDI≥0.80, sources≥20, wolves≥12.
Save logs/YYYY-MM-DD_sujet.md"
```

**Expected**:
- Investigation Tree depth L6-L9
- Query Optimization: 20-30 queries, PRIMARY source discovery
- EDI ≥ 0.80, ISN ≥ 9.5, wolf report detailed

### 4. Développement continu
- Après investigation: noter gaps/bugs dans `NOTES.md`
- Améliorer KB files directement (pas de process lourd)
- Tester changement: re-run investigation comparative
- Failed integrations: Document in `docs/postmortems/`

---

## Évolution

**Principe KISS**:
- Problème détecté → Fix direct KB file
- Pattern manquant → Ajouter `kb/PATTERNS.md`
- Formula imprécise → Ajuster `kb/COGNITIVE_DSL.md`
- EDI bas → Étendre `kb/QUERY_TEMPLATES.md` (H7 map)
- Integration failed → Postmortem in `docs/postmortems/`

**Documentation développement**: Voir [docs/development/](docs/development/) pour docs techniques auto-save et MnemoLite.

**Pas de roadmap**. Pas de dashboard complexe. Juste: use → feedback → improve → repeat.

---

## KB Files Essentiels

| File | Contenu | Version |
|------|---------|---------|
| `COGNITIVE_DSL.md` | Formulas (IVF/ISN/EDI), symbols, concepts | Stable |
| `SEARCH_EPISTEMIC.md` | Source classification ◈◉○, EDI 6D | Stable |
| `PATTERNS.md` | 20 patterns manipulation (ICEBERG, MONEY, etc) | Stable |
| `QUERY_TEMPLATES.md` | Search templates, H7 adversary map | Stable |
| `INVESTIGATION.md` | Protocols L0-L9 | Stable |
| `INVESTIGATION_TREE.md` | **NEW v8.4**: Tree investigation, COMPARABLES_ASYMMETRY | v8.4 |
| `VALIDATION.md` | Post-search validation loop | Updated |
| `HANDOFF_MEMO.md` | Multi-conversation iteration | Stable |

---

## Métriques (optionnel)

Si tu veux tracker:
- Crée `logs/` avec investigations
- Grep EDI scores: `grep "EDI:" logs/*.md`
- Compare avant/après improvements

**Pas obligatoire**. Focus = quality investigations, pas vanity metrics.

---

## Architecture Decisions

### Dual-Engine Search (v8.4 VALIDATED)

**Current architecture**:
- **WebSearch** (Google API official): 95%+ success, primary engine
- **MCP web-search** (DuckDuckGo): 60-80% success, diversity engine
- **Query Optimization v8.3**: Automatic splitting + hybrid fallback

**Why this architecture**:
- Load tested Google Search MCP (Playwright-based): 0% success rate (25 queries, 100% anti-bot blocking)
- Postmortem: [docs/postmortems/2025-11-16-google-search-mcp-ABANDONED.md](docs/postmortems/2025-11-16-google-search-mcp-ABANDONED.md)
- Decision: Official APIs (WebSearch) > Scraping (Playwright) for reliability

**EDI Impact**:
- Dual-engine: +0.15 to +0.25 EDI boost (algorithmic diversity)
- Query Optimization: +0.15 to +0.27 EDI boost (better source discovery)
- Combined: 80-100% productive query rate

---

## Support

Questions/bugs → `NOTES.md` ou direct edit KB.

Pas de process formel. Itérations rapides.

**Failed integrations** → Postmortem in `docs/postmortems/` for future reference.

---

**Truth Engine v8.4** — KISS edition. Zero bullshit, pure signal.

**Changelog**:
- **v8.4** (2025-11-16): Investigation Tree, Query Optimization v8.3, architecture validated
- **v8.3** (2025-11-15): Query Optimization automatic splitting + hybrid fallback
- **v8.0** (2025-11-09): Base system

**Status**: Production-ready, stable architecture
