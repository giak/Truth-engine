# Audit MCP - Phase 2 Optimization

**Date** : 2024-11-24
**Projet** : Truth Engine

## Configuration MCP Découverte

### Fichiers de configuration

1. **`~/.claude-code/mcp.json`** (Warp/Claude Code CLI)
   - 1 serveur : MnemoLite uniquement

2. **`~/.config/Claude/mcp.json`** (Claude Desktop)
   - 3 serveurs : MnemoLite, Context7, web-search

3. **VSCode Insiders** (`~/.config/Code - Insiders/.../cline_mcp_settings.json`)
   - 0 serveurs (config vide)

**Config active pour Truth Engine** : `~/.config/Claude/mcp.json` (utilisée par Warp Agent Mode)

## Serveurs MCP Configurés

### 1. MnemoLite
**Command** : `bash /home/giak/Work/MnemoLite/scripts/mcp_server.sh`
**Status** : ✅ Actif (vérifié via `ping`)
**Description** : Code intelligence, semantic search, memory, graph analysis

**Tools exposés (10)** :
- ✅ **`search_code`** - Hybrid semantic + lexical code search
- ✅ **`write_memory`** - Create persistent memory
- ⚠️ `update_memory` - Update existing memory
- ⚠️ `delete_memory` - Delete memory (soft/hard)
- ✅ **`index_project`** - Index entire project
- ⚠️ `reindex_file` - Reindex single file
- ⚠️ `switch_project` - Switch active project
- ⚠️ `clear_cache` - Admin cache operation
- ⚠️ `ping` - Connectivity test

**Resources exposés (6)** :
- ⚠️ `get_search_analytics` - Search performance metrics
- ⚠️ `get_cache_stats` - Cache statistics
- ⚠️ `supported_languages` - Programming languages list
- ⚠️ `get_health_status` - Health check
- ⚠️ `list_memories` - List memories with filters
- ⚠️ `list_projects` - List indexed projects

**Total overhead estimé** : 16 outils × ~500 tokens = **~8K tokens**

### 2. Context7
**Command** : `npx -y @upstash/context7-mcp`
**Status** : ❓ Non testé
**Description** : Library documentation search

**Tools exposés (estimé 2-3)** :
- `resolve-library-id`
- `get-library-docs`

**Usage Truth Engine** : ❌ **JAMAIS utilisé** (aucune référence dans CLAUDE.md, system.md, KB)

**Total overhead estimé** : 3 outils × ~500 tokens = **~1.5K tokens**

### 3. web-search
**Command** : `npx -y @modelcontextprotocol/server-web-search`
**Status** : ❓ Non testé (probablement actif)
**Description** : Web search capabilities (DuckDuckGo)

**Tools exposés (estimé 1)** :
- `search` - Web search

**Usage Truth Engine** : ✅ **Utilisé** (fallback DuckDuckGo pour investigations)

**Note importante** : Truth Engine utilise AUSSI WebSearch (Google API officiel, non-MCP) comme moteur principal.

**Total overhead estimé** : 1 outil × ~500 tokens = **~500 tokens**

## Analyse d'utilisation Truth Engine

D'après `CLAUDE.md`, `system.md`, et workflows :

### Outils ESSENTIELS (utilisés régulièrement)

#### MnemoLite
1. **`search_code`** ✅ - Recherche sémantique KB (core workflow)
2. **`write_memory`** ✅ - Stockage mémoire inter-sessions
3. **`index_project`** ✅ - Indexation KB initiale

#### web-search
4. **`search`** ✅ - Recherche web DuckDuckGo (fallback)

### Outils OCCASIONNELS (edge cases)

#### MnemoLite
5. **`update_memory`** ⚠️ - Mise à jour mémoire existante (rare)
6. **`reindex_file`** ⚠️ - Réindexation après modification KB (maintenance)
7. **`switch_project`** ⚠️ - Changement projet actif (multi-projet)

### Outils RAREMENT/JAMAIS utilisés

#### MnemoLite
8. **`delete_memory`** ❌ - Suppression mémoire (admin)
9. **`clear_cache`** ❌ - Nettoyage cache (admin)
10. **`ping`** ❌ - Test connectivité (debug)
11. **Resources (6 items)** ❌ - Métriques/analytics (monitoring, non workflow)

#### Context7
12. **TOUS les outils** ❌ - Jamais référencé dans Truth Engine

## Recommandations d'optimisation

### Option A : Désactivation agressive (gain max)

**Serveurs à désactiver** :
```json
{
  "mcpServers": {
    "mnemolite": { "disabled": false },  // GARDER
    "context7": { "disabled": true },    // ❌ DÉSACTIVER (jamais utilisé)
    "web-search": { "disabled": false }  // GARDER (fallback DuckDuckGo)
  }
}
```

**Outils MnemoLite à désactiver** (si supporté par le serveur) :
- `delete_memory`
- `clear_cache`
- `ping`
- `get_search_analytics`
- `get_cache_stats`
- `supported_languages`
- `get_health_status`
- `list_memories` (sauf si workflow multi-mémoire)
- `list_projects` (sauf si workflow multi-projet)

**Gain estimé** :
- Context7 désactivé : **~1.5K tokens**
- MnemoLite outils inutiles : **~4K tokens** (8 outils)
- **Total : ~5.5K tokens (~2.75% sur 200K contexte)**

### Option B : Désactivation prudente (gain modéré, sécurisé)

**Serveurs à désactiver** :
```json
{
  "mcpServers": {
    "mnemolite": { "disabled": false },
    "context7": { "disabled": true },    // ❌ DÉSACTIVER
    "web-search": { "disabled": false }
  }
}
```

**Outils MnemoLite à conserver TOUS** (prudence maintenance/debug)

**Gain estimé** :
- Context7 désactivé : **~1.5K tokens (~0.75%)**

### Option C : Configuration minimaliste (gain maximum, risque)

Créer config MCP spécifique Truth Engine :

```json
{
  "mcpServers": {
    "mnemolite": {
      "command": "bash",
      "args": ["/home/giak/Work/MnemoLite/scripts/mcp_server.sh"],
      "env": { "DOCKER_COMPOSE_PROJECT": "mnemolite" },
      "enabledTools": [
        "search_code",
        "write_memory",
        "index_project"
      ]
    },
    "web-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-web-search"],
      "env": {}
    }
  }
}
```

**Gain estimé** :
- Context7 désactivé : **~1.5K tokens**
- MnemoLite outils limités : **~6.5K tokens** (13 outils désactivés)
- **Total : ~8K tokens (~4% sur 200K contexte)**

**Risque** : Si `enabledTools` non supporté par MnemoLite, config échoue.

## Recommandation finale

**Option B (prudente)** pour Phase 2 :

**Actions immédiates** :
1. ✅ Désactiver Context7 (jamais utilisé, gain assuré 1.5K tokens)
2. ✅ Garder MnemoLite complet (outils admin rarement utilisés mais pas coûteux)
3. ✅ Garder web-search (fallback DuckDuckGo utile)

**Validation** :
- Tester investigation SIMPLE après désactivation Context7
- Vérifier EDI ≥ 0.30, pas d'erreur

**Phase 3 (si besoin)** :
- Explorer `enabledTools` avec MnemoLite (Option C)
- Gain additionnel possible : +6.5K tokens

## Comparaison avec recherches web 2025

D'après les recherches :
- Chrome DevTools MCP : ~20.6K tokens (10.3%)
- Gemini CLI MCP : ~6K tokens (3%)

**Votre overhead actuel** :
- MnemoLite : ~8K tokens (4%)
- Context7 : ~1.5K tokens (0.75%)
- web-search : ~0.5K tokens (0.25%)
- **Total : ~10K tokens (5%)**

**Après Phase 2 Option B** :
- MnemoLite : ~8K tokens (4%)
- web-search : ~0.5K tokens (0.25%)
- **Total : ~8.5K tokens (4.25%)**
- **Réduction : 15% de l'overhead MCP**

## Prochaines étapes

1. **Backup** : `cp ~/.config/Claude/mcp.json ~/.config/Claude/mcp.json.backup`
2. **Désactiver Context7** : Éditer `~/.config/Claude/mcp.json`
3. **Redémarrer session** : Fermer/rouvrir Warp
4. **Test validation** : Investigation SIMPLE Truth Engine
5. **Mesure gain** : Comparer contexte avant/après (si `/stats` disponible)

---

**Version** : Truth Engine v8.4
**Phase** : 2 (MCP Optimization)
**Gain estimé Phase 2** : ~1.5K tokens (0.75% contexte)
**Gain cumulé Phase 1+2** : 35-55% + 0.75% = **36-56%**
