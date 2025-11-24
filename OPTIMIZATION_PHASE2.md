# Phase 2 : MCP Optimization - Implémentation

**Date** : 2024-11-24
**Status** : ✅ Implémenté, ⏳ À valider

## Changements effectués

### Context7 désactivé
**Fichier** : `~/.config/Claude/mcp.json`
**Backup** : `~/.config/Claude/mcp.json.backup`

**Avant** :
```json
"context7": {
  "command": "npx",
  "args": ["-y", "@upstash/context7-mcp"],
  "env": {},
  "description": "Context7 - Library documentation search"
}
```

**Après** :
```json
"context7": {
  "disabled": true,
  "command": "npx",
  "args": ["-y", "@upstash/context7-mcp"],
  "env": {},
  "description": "Context7 - Library documentation search (DISABLED: not used by Truth Engine)"
}
```

### Serveurs MCP actifs

**Après Phase 2** :
1. ✅ **MnemoLite** - Code intelligence, semantic search, memory (16 outils)
2. ❌ **Context7** - DÉSACTIVÉ (jamais utilisé)
3. ✅ **web-search** - DuckDuckGo fallback (1 outil)

## Gain Phase 2

| Optimisation | Gain estimé | Status |
|--------------|-------------|--------|
| Context7 désactivé | ~1.5K tokens (0.75%) | ✅ |

**Overhead MCP** :
- Avant : ~10K tokens (5%)
- Après : ~8.5K tokens (4.25%)
- **Réduction : 15% de l'overhead MCP**

## Gains cumulatifs Phase 1+2

| Phase | Optimisations | Gain |
|-------|---------------|------|
| Phase 1 | `.claudeignore` + CLAUDE.md minimaliste + hook audit | 35-55% |
| Phase 2 | Context7 désactivé | +0.75% |
| **TOTAL** | **Phases 1+2** | **36-56%** |

## Validation requise

### ⚠️ IMPORTANT : Redémarrer la session

Pour que la désactivation de Context7 prenne effet :

**Option 1** : Redémarrer Warp
```bash
# Fermer Warp complètement (Cmd+Q / Alt+F4)
# Relancer Warp
```

**Option 2** : Nouvelle session Claude Code
```bash
# Dans Warp, démarrer une nouvelle session Agent Mode
```

### Test investigation SIMPLE

Après redémarrage :

```bash
cd /home/giak/projects/truth-engine
claude "Analyse: 'Unemployment 7.4% France'. Load system.md. Use MnemoLite KB search. Truth Engine protocol SIMPLE."
```

**Métriques à vérifier** :
1. ✅ Investigation se lance sans erreur
2. ✅ MnemoLite `search_code` fonctionne
3. ✅ web-search (DuckDuckGo) disponible en fallback
4. ✅ EDI ≥ 0.30
5. ✅ Pas de référence à Context7 dans les outils disponibles
6. ✅ Pas d'erreur "context exceeded"

### Vérifier la désactivation

Après redémarrage de Warp, dans une nouvelle session Claude :

```bash
# Lister les outils MCP disponibles
# (Devrait montrer MnemoLite + web-search, PAS Context7)
```

## Rollback si nécessaire

Si Context7 s'avère nécessaire (peu probable) :

```bash
# Restaurer config originale
cp ~/.config/Claude/mcp.json.backup ~/.config/Claude/mcp.json

# Redémarrer Warp
```

## Optimisations futures (Phase 3)

Si besoin de gains additionnels :

### Option C : Configuration minimaliste MnemoLite

**Gain potentiel** : +6.5K tokens (~3.25%)

**Risque** : Si `enabledTools` non supporté par MnemoLite, échec config.

**Configuration** :
```json
"mnemolite": {
  "command": "bash",
  "args": ["/home/giak/Work/MnemoLite/scripts/mcp_server.sh"],
  "env": { "DOCKER_COMPOSE_PROJECT": "mnemolite" },
  "enabledTools": [
    "search_code",
    "write_memory",
    "index_project"
  ]
}
```

**Outils désactivés** (13) :
- `update_memory`, `delete_memory`, `reindex_file`, `switch_project`
- `clear_cache`, `ping`
- Resources (6) : `get_search_analytics`, `get_cache_stats`, etc.

**À tester** : Vérifier si MnemoLite supporte `enabledTools` (pas documenté).

## Prochaines étapes

**Immédiat** :
1. ✅ Redémarrer Warp pour appliquer changements
2. ✅ Tester investigation SIMPLE
3. ✅ Valider MnemoLite + web-search fonctionnels

**Phase 3 (optionnel)** :
- Si besoin de plus de gains, explorer Option C (minimaliste MnemoLite)
- Externaliser TAD.md/PFD.md (load on-demand)
- Claude Skills (2025 feature)

---

**Version** : Truth Engine v8.4
**Phase** : 2 (MCP Optimization) - Implémentation Option B
**Gain Phase 2** : ~1.5K tokens (0.75%)
**Gain cumulé** : 36-56% réduction contexte
**Audit complet** : [MCP_AUDIT.md](MCP_AUDIT.md)
