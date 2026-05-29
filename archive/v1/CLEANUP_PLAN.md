# Plan de Nettoyage Truth Engine

**Date**: 2025-11-08
**Objectif**: Organiser le projet après développement auto-save + MnemoLite

---

## État Actuel

### Fichiers CORE Truth Engine (✅ À GARDER)
```
/
├── system.md              # Core LLM instructions
├── kb/                    # Knowledge base (16 files)
├── PFD.md                 # Philosophical Foundation
├── PRD.md                 # Product Requirements
├── TAD.md                 # Technical Architecture
├── VISION.md              # Vision document
├── DASHBOARD.md           # Dashboard (minimal)
├── CLAUDE.md              # Claude Code instructions
└── README.md              # Project README
```

### Fichiers Auto-Save/MnemoLite (🗂️ À ORGANISER)
```
/
├── AUTOSAVE_COMPLETE.md                    # ✅ Doc finale - GARDER
├── RESEARCH_AUTOSAVE_V2.md                 # 📚 Recherche - ARCHIVER
├── WORKFLOW_AUTOSAVE.md                    # 📚 Dev docs - ARCHIVER
├── AUTOMATION_MNEMOLITE_SETUP.md           # 📚 Dev docs - ARCHIVER
├── RAPPORT_SAUVEGARDE_CONVERSATIONS.md     # 📚 Dev docs - ARCHIVER
├── MCP_SETUP.md                            # 📚 Dev docs - ARCHIVER
└── MCP_STATUS.md                           # 📚 Status - ARCHIVER
```

### Hooks Claude Code (✅ À GARDER)
```
.claude/
├── hooks/
│   ├── SessionStart/check-autosave-setup.sh
│   ├── Stop/auto-save-exchange.sh
│   └── UserPromptSubmit/auto-save-previous.sh
├── settings.local.json
└── .mcp.json
```

---

## Plan de Nettoyage

### 1. Créer Structure `docs/`

```
docs/
├── development/          # Docs de développement
│   ├── autosave/        # Système auto-save
│   └── mnemolite/       # MnemoLite integration
└── archive/             # Anciens docs (si besoin)
```

### 2. Déplacements Proposés

**Vers `docs/development/autosave/`** :
- RESEARCH_AUTOSAVE_V2.md
- WORKFLOW_AUTOSAVE.md
- RAPPORT_SAUVEGARDE_CONVERSATIONS.md

**Vers `docs/development/mnemolite/`** :
- AUTOMATION_MNEMOLITE_SETUP.md
- MCP_SETUP.md
- MCP_STATUS.md

**À GARDER à la racine** :
- AUTOSAVE_COMPLETE.md (documentation finale utilisateur)

### 3. Créer `.gitignore`

```gitignore
# Logs
logs/
*.log

# Debug
/tmp/
*.debug

# Claude Code local
.claude/sessions/

# Python
__pycache__/
*.py[cod]
*$py.class

# Env
.env
.venv
venv/

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/

# Auto-save specific
/tmp/hook-autosave-debug.log
/tmp/mnemo-saved-exchanges.txt
```

### 4. Mettre à jour README.md

- ✅ Corriger config MnemoLite MCP (bash script, pas command)
- ✅ Ajouter section Auto-Save System
- ✅ Pointer vers docs/ pour dev docs
- ✅ Nettoyer références obsolètes

### 5. Vérifier Structure Finale

```
truth-engine/
├── README.md                    # ✅ Updated
├── CLAUDE.md                    # ✅ Claude Code instructions
├── AUTOSAVE_COMPLETE.md         # ✅ Auto-save documentation
├── system.md                    # ✅ Core LLM instructions
├── kb/                          # ✅ Knowledge base
├── PFD.md, PRD.md, TAD.md      # ✅ Core docs
├── VISION.md, DASHBOARD.md     # ✅ Meta docs
├── .gitignore                   # ✅ NEW
├── .mcp.json                    # ✅ MCP config
├── .claude/                     # ✅ Claude Code config + hooks
├── docs/                        # ✅ NEW
│   └── development/
│       ├── autosave/            # Dev docs auto-save
│       └── mnemolite/           # Dev docs MnemoLite
└── logs/                        # Auto-created by investigations
```

---

## Validation

### Après nettoyage, vérifier :

```bash
# 1. Structure propre
ls -la /home/giak/projects/truth-engine/

# 2. Hooks fonctionnels
cat .claude/settings.local.json

# 3. MCP config OK
cat .mcp.json

# 4. Auto-save opérationnel
# Démarrer nouvelle session Claude Code
# Expected: "AUTO-SAVE SYSTEM: ACTIVE & HEALTHY"
```

---

## Commandes Nettoyage

```bash
cd /home/giak/projects/truth-engine

# Créer structure docs/
mkdir -p docs/development/{autosave,mnemolite}

# Déplacer fichiers auto-save
mv RESEARCH_AUTOSAVE_V2.md docs/development/autosave/
mv WORKFLOW_AUTOSAVE.md docs/development/autosave/
mv RAPPORT_SAUVEGARDE_CONVERSATIONS.md docs/development/autosave/

# Déplacer fichiers MnemoLite
mv AUTOMATION_MNEMOLITE_SETUP.md docs/development/mnemolite/
mv MCP_SETUP.md docs/development/mnemolite/
mv MCP_STATUS.md docs/development/mnemolite/

# Créer .gitignore
touch .gitignore

# Mettre à jour README
# (édition manuelle ou script)
```

---

## Checklist Final

- [ ] docs/ structure créée
- [ ] Fichiers dev déplacés vers docs/
- [ ] AUTOSAVE_COMPLETE.md reste à racine
- [ ] .gitignore créé
- [ ] README.md mis à jour
- [ ] Test auto-save fonctionne
- [ ] Test MCP fonctionne
- [ ] Test Truth Engine investigation fonctionne

---

**Status**: Plan proposé, en attente validation
