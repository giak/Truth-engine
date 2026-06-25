# DIAGNOSTIC MNEMOLITE — Recherche sémantique français

**Date :** 2026-06-07 | **Mémoires :** 35 561 | **Embedding rate :** 99%

---

## Architecture réelle (3 chemins de recherche distincts)

```
┌─────────────────────────────────────────────────────────────┐
│                      MNEMOLITE                               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  CHEMIN A : MCP search_memory (utilisé par Sublimator)      │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ SearchMemoryTool.execute()                            │   │
│  │   ↓ is_tag_only = True (HARDCODÉ ligne 770)          │   │
│  │   ↓ query_embedding = None                           │   │
│  │   ↓ HYBRID SEARCH JAMAIS APPELÉ                      │   │
│  │   ↓ MemoryRepository.search_by_tags()                │   │
│  │   → TAG-ONLY, zéro vectoriel                         │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  CHEMIN B : REST /v1/search/?vector_query=...               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ search_routes.search()                                │   │
│  │   ↓ embedding_service.generate_embedding(query)       │   │
│  │   ↓ HybridMemorySearchService.search(embedding=...)   │   │
│  │   ↓ RRF fusion (lexical + vectoriel)                 │   │
│  │   → VECTORIEL, mais modèle anglais                   │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  CHEMIN C : MemoryRepository.search_by_vector()             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Requiert un vecteur pré-calculé                       │   │
│  │ JAMAIS appelé par le MCP (query_embedding = None)    │   │
│  │ JAMAIS appelé par le REST                             │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  PIPELINE D'EMBEDDING                                       │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ POST /api/v1/memories                                 │   │
│  │   ↓ SentenceTransformerEmbeddingService()             │   │
│  │   ↓ model = "nomic-ai/nomic-embed-text-v1.5"         │   │
│  │   ↓ Monolingue ANGLAIS (768D)                        │   │
│  │   ↓ pgvector HNSW (halfvec)                          │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## 3 problèmes indépendants

### Problème 1 : MCP → TAG_ONLY hardcodé

**Fichier :** `api/mnemo_mcp/tools/memory_tools.py:770`

```python
# CRITICAL FIX: Skip embedding generation in search_memory to avoid 10s+ cold start.
is_tag_only = True
```

- Le code de recherche hybride existe (HybridMemorySearchService avec RRF fusion)
- Le code de génération d'embedding pour la query existe (lignes 748-753)
- **Mais `is_tag_only = True` court-circuite TOUT** → `query_embedding = None` → fallback vers `search_by_tags()`
- Raison : éviter le cold start de 10s+ du chargement du modèle SentenceTransformer
- **Conséquence : le Sublimator, via MCP, ne peut PAS faire de recherche sémantique**

### Problème 2 : Modèle d'embedding MONOLINGUE ANGLAIS

**Fichier :** `.env`

```
EMBEDDING_MODEL=nomic-ai/nomic-embed-text-v1.5    ← actif
# EMBEDDING_MODEL=intfloat/multilingual-e5-base    ← commenté (recommandé pour français)
```

- `nomic-embed-text-v1.5` : entraîné sur de l'anglais uniquement, 768 dimensions
- `multilingual-e5-base` : multilingue (français inclus), même dimension, déjà supporté dans le code
- **Conséquence : même si on active le vectoriel MCP, la similarité français/français sera médiocre**

### Problème 3 : Métadonnées vides dans l'index de recherche

```json
{"metadata": {}}  // ← titres et tags absents des résultats
```

- Le `/v1/search/` retourne des résultats mais sans titres ni tags
- Les résultats sont identifiables uniquement par le contenu textuel
- **Conséquence : les résultats de recherche sont difficilement exploitables**

---

## SOLUTION RECOMMANDÉE (2 changements, ~5 lignes)

### Étape 1 : Changer le modèle d'embedding

**Fichier :** `/home/giak/Work/MnemoLite/.env`

```diff
- EMBEDDING_MODEL=nomic-ai/nomic-embed-text-v1.5
+ EMBEDDING_MODEL=intfloat/multilingual-e5-base
```

**Impact :** Nécessite une ré-indexation complète (~35K mémoires). Script de rebuild à écrire.

**Temps estimé :** ~2-3h pour ré-indexer 35K mémoires (dépend du CPU).

### Étape 2 : Rendre le mode de recherche configurable dans le MCP

**Fichier :** `api/mnemo_mcp/tools/memory_tools.py` (ligne ~770)

```diff
  # CRITICAL FIX: Skip embedding generation in search_memory to avoid 10s+ cold start.
- is_tag_only = True
+ is_tag_only = search_mode not in ("hybrid", "semantic")
```

Et ajouter le paramètre à la signature de `execute()` :

```diff
  async def execute(
      self,
      ctx: Context,
      query: Optional[str] = None,
      tags: Optional[List[str]] = None,
      project_id: Optional[str] = None,
      memory_type: Optional[str] = None,
      consumed: Optional[bool] = None,
      limit: int = 10,
+     search_mode: str = "tag",  # "tag" (défaut, rapide) | "hybrid" | "semantic"
  ) -> Dict[str, Any]:
```

**Impact :** 
- `search_mode="tag"` (défaut) : comportement actuel, pas de cold start
- `search_mode="hybrid"` : génère l'embedding de la query → RRF fusion lexical+vectoriel
- Le Sublimator utilise `search_mode="hybrid"` pour la recherche sémantique
- Le cold start (~10s) n'arrive qu'au PREMIER appel hybrid — ensuite le modèle est en cache

**Temps estimé :** 5 minutes.

### Étape 3 (optionnel) : Mettre à jour le prompt Sublimator v34

Une fois les changements Mnemolite appliqués, mettre à jour le prompt :

```diff
- search_memory(query="mots-clés de l'enquête")
+ search_memory(query="mots-clés de l'enquête", search_mode="hybrid")
```

---

## POURQUOI PAS D'AUTRES SOLUTIONS

| Solution alternative | Pourquoi pas |
|---------------------|-------------|
| Utiliser le REST `/v1/search/` depuis le MCP | Le MCP n'a pas d'outil pour ça. Il faudrait ajouter un outil MCP wrapper. Plus de code. |
| Changer `is_tag_only = False` sans paramètre | Toutes les recherches MCP subiraient le cold start → regression de perf |
| Passer à `multilingual-e5-large` | 1024D, plus lent, pas de gain significatif sur la similarité sémantique pour notre usage |
| Utiliser l'API OpenAI pour les embeddings | Dépendance externe, coût, latence réseau |

---

## PLAN D'EXÉCUTION

| Étape | Action | Effort | Risque |
|-------|--------|--------|--------|
| 1 | Modifier `.env` → `multilingual-e5-base` | 1 ligne | Aucun |
| 2 | Redémarrer Mnemolite | 10s | Court downtime |
| 3 | Ré-indexer les 35K mémoires (script de rebuild) | ~2-3h | CPU bound |
| 4 | Ajouter `search_mode` param au MCP `search_memory` | ~5 lignes | Faible |
| 5 | Tester : `search_memory(query="...", search_mode="hybrid")` | 5 min | Vérification |
| 6 | Mettre à jour le prompt Sublimator v34.1 | 2 lignes | Aucun |

**Total estimé :** 3-4h (dont 2-3h de ré-indexation en background).
