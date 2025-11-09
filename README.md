# Truth Engine

**Version**: 8.0  
**Principe**: Analyse épistémique hostile. "Un récit = propagande. Cinq récits = cartographie."

---

## Structure

```
truth-engine/
├── README.md                    # Ce fichier
├── CLAUDE.md                    # Claude Code instructions
├── AUTOSAVE_COMPLETE.md         # Auto-save system documentation
├── system.md                    # Instructions LLM (v7.17)
├── PFD.md                       # Philosophical Foundation (148 concepts)
├── PRD.md                       # Product Requirements (v7.15.1)
├── TAD.md                       # Technical Architecture
├── VISION.md                    # Vision document
├── DASHBOARD.md                 # Dashboard (minimal)
├── kb/                          # Knowledge base (formulas, patterns, protocols)
├── logs/                        # Investigations (auto-créé)
├── docs/                        # Development documentation
│   └── development/
│       ├── autosave/            # Auto-save system dev docs
│       └── mnemolite/           # MnemoLite integration dev docs
├── .claude/                     # Claude Code config + hooks
│   ├── hooks/                   # SessionStart, Stop, UserPromptSubmit
│   ├── settings.local.json      # Hook configuration
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
```

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

**Documentation complète**: Voir [AUTOSAVE_COMPLETE.md](AUTOSAVE_COMPLETE.md) | Dev docs: [docs/development/autosave/](docs/development/autosave/)

---

## Workflow

### 1. Analyse simple
```bash
claude-code "Analyse: 'Chômage 7.4%'. Truth Engine."
```

### 2. Investigation complexe
```bash
claude-code "Investigation APEX: [sujet complexe]. 
Load system.md + kb/. 
Target: EDI≥0.60, sources≥15, wolves≥8 si politique.
Save logs/YYYY-MM-DD_sujet.md"
```

### 3. Développement continu
- Après investigation: noter gaps/bugs dans `NOTES.md`
- Améliorer KB files directement (pas de process lourd)
- Tester changement: re-run investigation comparative

---

## Évolution

**Principe KISS**:
- Problème détecté → Fix direct KB file
- Pattern manquant → Ajouter `kb/PATTERNS.md`
- Formula imprécise → Ajuster `kb/COGNITIVE_DSL.md`
- EDI bas → Étendre `kb/QUERY_TEMPLATES.md` (H7 map)

**Documentation développement**: Voir [docs/development/](docs/development/) pour docs techniques auto-save et MnemoLite.

**Pas de roadmap**. Pas de dashboard complexe. Juste: use → feedback → improve → repeat.

---

## KB Files Essentiels

| File | Contenu |
|------|---------|
| `COGNITIVE_DSL.md` | Formulas (IVF/ISN/EDI), symbols, concepts |
| `SEARCH_EPISTEMIC.md` | Source classification ◈◉○, EDI 6D |
| `PATTERNS.md` | 20 patterns manipulation (ICEBERG, MONEY, etc) |
| `QUERY_TEMPLATES.md` | Search templates, H7 adversary map |
| `INVESTIGATION.md` | Protocols L0-L9 |

---

## Métriques (optionnel)

Si tu veux tracker:
- Crée `logs/` avec investigations
- Grep EDI scores: `grep "EDI:" logs/*.md`
- Compare avant/après improvements

**Pas obligatoire**. Focus = quality investigations, pas vanity metrics.

---

## Support

Questions/bugs → `NOTES.md` ou direct edit KB.

Pas de process formel. Itérations rapides.

---

**Truth Engine v8.0** — KISS edition. Zero bullshit, pure signal.
