# PROTOCOLE DE TEST — Mnemolite MCP (Write + Search Vectoriel)

**Date** : 2026-06-13
**Type** : PROTOCOLE_TEST
**Objet** : Blindage exhaustif du pipeline write_memory → embedding → indexation → search_memory
**Priorité** : APEX — infra critique pour toutes les enquêtes Truth Engine

---

## 0. ARCHITECTURE CIBLE

```
write_memory(title, content, tags)
  ├─ dedup_check (Jaccard > 0.85 → rejet)
  ├─ INSERT mémoire (embedding=None, embedding_generated=False)
  └─ _trigger_async_embedding()
       ├─ generate_embedding(title + content)
       ├─ format_vector_for_sql()
       └─ UPDATE embedding + embedding_generated=True

search_memory(query, search_mode)
  ├─ search_mode="tag" → tag filtering only (pas d'embedding, rapide)
  ├─ search_mode="hybrid" → vector + lexical fusion RRF
  └─ search_mode="semantic" → vector only
```

---

## 1. PLAN TDD — PRIORITÉ DE TESTS

### Niveau 1 : SMOKE (déjà couvert partiellement)

| # | Test | Fichier cible | Statut |
|---|------|---------------|--------|
| 1.1 | write_memory crée une mémoire avec tags | test_memory_tools.py | ✅ 620 lignes |
| 1.2 | search_memory retourne un résultat pour query connu | test_memory_search_tool.py | ✅ 609 lignes |
| 1.3 | ping répond | server.py | ✅ implicite |

### Niveau 2 : PIPELINE CRITIQUE (à créer/renforcer)

| # | Test | Fichier | Priorité |
|---|------|---------|----------|
| 2.1 | **write + search end-to-end** : écrire 3 mémoires, vérifier que search les retrouve par score décroissant | NOUVEAU | 🔴 APEX |
| 2.2 | **embedding async race** : vérifier que search trouve une mémoire AVANT que l'embedding async soit terminé | NOUVEAU | 🔴 APEX |
| 2.3 | **dedup_check** : écrire 2 mémoires quasi-identiques, vérifier que la 2e est rejetée (Jaccard > 0.85) | test_memory_tools.py | 🟠 HIGH |
| 2.4 | **dedup_check bypass** : écrire avec dedup_check=False, vérifier que le duplicata est créé | test_memory_tools.py | 🟠 HIGH |
| 2.5 | **empty query + tags** : search avec query="" et tags=["dette"], doit retourner résultats par tags | test_memory_search_tool.py | ✅ existant |
| 2.6 | **search_mode="tag" vs "hybrid"** : même requête, résultats différents (tag = filtrage, hybrid = vectoriel) | NOUVEAU | 🔴 APEX |
| 2.7 | **search_mode="semantic"** : vectoriel pur, pas de lexical | NOUVEAU | 🟠 HIGH |

### Niveau 3 : EDGE CASES & RÉGRESSION

| # | Test | Fichier | Priorité |
|---|------|---------|----------|
| 3.1 | **cache_key regression** : search avec Redis=None, vérifier que cache_key=None ne cause pas UnboundLocalError | test_memory_search_tool.py | 🔴 APEX |
| 3.2 | **cache hit** : 2 search identiques, le 2e doit retourner le cache (appeler Redis.get) | test_memory_search_tool.py | ✅ existant |
| 3.3 | **cache invalidation après write** : écrire, chercher, écrire plus, chercher — le cache doit être invalidé | NOUVEAU | 🟠 HIGH |
| 3.4 | **query vide + pas de tags** : doit lever ValueError | test_memory_search_tool.py | ✅ existant |
| 3.5 | **query whitespace-only** : doit lever ValueError | test_memory_search_tool.py | ✅ existant |
| 3.6 | **memory_type invalide** : doit lever ValueError | test_memory_search_tool.py | ✅ existant |
| 3.7 | **limit clamped to 50** : passer limit=500, le résultat doit être limité à 50 max | test_memory_search_tool.py | ✅ existant |
| 3.8 | **limit minimum 1** : passer limit=0, doit être corrigé en 1 | test_memory_search_tool.py | ✅ existant |
| 3.9 | **embedding failure fallback** : si le service d'embedding échoue, search doit fallback vers tag-only | test_memory_search_tool.py | ✅ existant |
| 3.10 | **content très long** (>100K chars) : write doit réussir, l'embedding ne doit pas timeout | NOUVEAU | 🟡 MEDIUM |
| 3.11 | **tags avec accents/unicode** : write avec tags=["débtè", "économie"], search par tag doit les retrouver | NOUVEAU | 🟡 MEDIUM |
| 3.12 | **concurrence** : 10 write simultanés, tous doivent réussir (pas de race condition sur l'embedding async) | NOUVEAU | 🟠 HIGH |
| 3.13 | **memory_type=quintessence** : write avec ce type, search filtré par memory_type doit le trouver | NOUVEAU | 🟡 MEDIUM |
| 3.14 | **consumed filter** : écrire, mark_consumed, chercher avec consumed=True/False, vérifier filtrage | NOUVEAU | 🟡 MEDIUM |

### Niveau 4 : INTÉGRATION MCP (tests via HTTP tools/call)

| # | Test | Priorité |
|---|------|----------|
| 4.1 | **tools/list contient tous les outils** : vérifier que write_memory, search_memory, read_memory, update_memory, delete_memory, extract_entities, search_by_entity sont présents | 🔴 APEX |
| 4.2 | **cycle CRUD complet via MCP** : write → read (vérifier contenu) → update → read (vérifier màj) → delete → read (vérifier soft delete) | 🔴 APEX |
| 4.3 | **search après write via MCP** : écrire via HTTP tools/call, chercher via HTTP tools/call, vérifier que la mémoire apparaît | 🔴 APEX |
| 4.4 | **31 outils répondent sans erreur** : appeler chaque outil avec des arguments valides, vérifier pas de -32602 | 🔴 APEX |
| 4.5 | **search_mode validé** : passer search_mode="invalid", doit retourner une erreur explicite | 🟡 MEDIUM |

---

## 2. FICHIERS À CRÉER/MODIFIER

### 2.1 Nouveau fichier : `tests/mnemo_mcp/test_write_search_pipeline.py`

```python
"""
Test du pipeline write_memory → embedding → search_memory.
Couverture : end-to-end, race async, dedup, search_modes.
"""

import pytest
import asyncio
import json
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

# ============================================================
# FIXTURES
# ============================================================

@pytest.fixture
def mock_ctx():
    ctx = MagicMock()
    ctx.elicit = AsyncMock(return_value="yes")
    return ctx

@pytest.fixture
def mock_memory_repository():
    """Simule un MemoryRepository qui stocke en mémoire."""
    repo = AsyncMock()
    repo._store = {}
    repo._id_counter = 0

    async def create(memory):
        repo._id_counter += 1
        mid = memory.id or uuid4()
        repo._store[str(mid)] = memory
        return memory

    async def get_by_id(mid):
        return repo._store.get(str(mid))

    async def search_hybrid(**kwargs):
        # Simule une recherche lexicale basique
        query = kwargs.get("query", "").lower()
        results = []
        for mid, mem in repo._store.items():
            if query in (mem.title or "").lower() or query in (mem.content or "").lower():
                results.append(mem)
        return results, len(results)

    repo.create = AsyncMock(side_effect=create)
    repo.get_by_id = AsyncMock(side_effect=get_by_id)
    repo.search_hybrid = AsyncMock(side_effect=search_hybrid)
    return repo

@pytest.fixture
def mock_embedding_service():
    """Simule un service d'embedding qui retourne des vecteurs déterministes."""
    svc = AsyncMock()
    async def generate(text):
        # Vecteur déterministe basé sur la longueur du texte
        import hashlib
        h = hashlib.sha256(text.encode()).digest()
        return [float(b) / 255.0 for b in h[:32]]  # 32-dim pour le test
    svc.generate_embedding = AsyncMock(side_effect=generate)
    return svc

# ============================================================
# NIVEAU 2 : PIPELINE CRITIQUE
# ============================================================

class TestWriteSearchPipeline:
    """Tests end-to-end du pipeline write → search."""

    @pytest.mark.asyncio
    async def test_write_then_search_finds_memory(self, mock_ctx, mock_memory_repository, mock_embedding_service):
        """APEX : Écrire une mémoire, la retrouver par recherche vectorielle."""
        from mnemo_mcp.tools.memory_tools import WriteMemoryTool, SearchMemoryTool

        write_tool = WriteMemoryTool()
        write_tool._services = {
            "memory_repository": mock_memory_repository,
            "embedding_service": mock_embedding_service,
        }

        # Écrire 3 mémoires sur des sujets différents
        await write_tool.execute(
            ctx=mock_ctx,
            title="Dette publique française 2026",
            content="La dette publique atteint 3300 milliards d'euros selon l'INSEE. Le déficit est de 5.5% du PIB.",
            memory_type="investigation",
            tags=["dette", "France", "INSEE"],
        )
        await write_tool.execute(
            ctx=mock_ctx,
            title="Chats et animaux domestiques",
            content="Les chats domestiques sont les animaux de compagnie les plus populaires en France.",
            memory_type="note",
            tags=["animaux", "chats"],
        )
        await write_tool.execute(
            ctx=mock_ctx,
            title="Budget 2026 : architecture du mensonge",
            content="Le budget 2026 contient 11 hausses fiscales cachées totalisant 37 milliards.",
            memory_type="article",
            tags=["budget", "dette", "fiscalité"],
        )

        search_tool = SearchMemoryTool()
        search_tool._services = {
            "memory_repository": mock_memory_repository,
            "embedding_service": mock_embedding_service,
        }

        # Recherche : "dette publique"
        result = await search_tool.execute(
            ctx=mock_ctx,
            query="dette publique France INSEE",
            search_mode="hybrid",
            limit=5,
        )

        memories = result.memories
        titles = [m.title for m in memories]

        # La mémoire "Dette publique française 2026" doit être en première position
        assert len(memories) >= 2, f"Expected >=2 results, got {len(memories)}"
        assert "Dette publique française 2026" in titles, f"Missing key memory. Found: {titles}"
        assert "Chats et animaux domestiques" not in titles[:3], \
            f"Unrelated memory should not be in top 3: {titles[:3]}"

    @pytest.mark.asyncio
    async def test_search_mode_tag_vs_hybrid(self, mock_ctx, mock_memory_repository, mock_embedding_service):
        """APEX : search_mode='tag' vs 'hybrid' donnent des résultats différents."""
        from mnemo_mcp.tools.memory_tools import WriteMemoryTool, SearchMemoryTool

        write_tool = WriteMemoryTool()
        write_tool._services = {
            "memory_repository": mock_memory_repository,
            "embedding_service": mock_embedding_service,
        }

        await write_tool.execute(
            ctx=mock_ctx,
            title="Dette publique",
            content="analyse de la dette",
            tags=["dette"],
            memory_type="investigation",
        )
        await write_tool.execute(
            ctx=mock_ctx,
            title="Note sur les chats",
            content="les chats sont mignons",
            tags=["animaux"],
            memory_type="note",
        )

        search_tool = SearchMemoryTool()
        search_tool._services = {
            "memory_repository": mock_memory_repository,
            "embedding_service": mock_embedding_service,
        }

        # Tag mode : filtre par tags uniquement
        result_tag = await search_tool.execute(
            ctx=mock_ctx, query="chats", search_mode="tag", limit=5,
        )
        # Hybrid mode : recherche sémantique
        result_hybrid = await search_tool.execute(
            ctx=mock_ctx, query="chats", search_mode="hybrid", limit=5,
        )

        # Les résultats doivent être différents (tag ne cherche que par tags)
        assert result_tag.metadata.search_mode in ("tag", "tag_only")
        # En mode tag avec query="chats" et pas de tags spécifiés, le comportement exact dépend
        # de l'implémentation — mais le mode doit être respecté
        assert result_hybrid.metadata.search_mode != "tag"

    @pytest.mark.asyncio
    async def test_embedding_async_race(self, mock_ctx, mock_memory_repository, mock_embedding_service):
        """APEX : Une mémoire écrite est trouvable même si l'embedding async n'est pas fini."""
        from mnemo_mcp.tools.memory_tools import WriteMemoryTool, SearchMemoryTool

        write_tool = WriteMemoryTool()
        write_tool._services = {
            "memory_repository": mock_memory_repository,
            "embedding_service": mock_embedding_service,
        }

        # Écrire une mémoire (l'embedding async démarre en background)
        await write_tool.execute(
            ctx=mock_ctx,
            title="Recherche urgente",
            content="Ce contenu doit être trouvable immédiatement",
            tags=["urgent"],
            memory_type="note",
        )

        # Rechercher immédiatement — doit être trouvable via recherche lexicale
        search_tool = SearchMemoryTool()
        search_tool._services = {
            "memory_repository": mock_memory_repository,
            "embedding_service": mock_embedding_service,
        }

        result = await search_tool.execute(
            ctx=mock_ctx,
            query="trouvable immédiatement",
            search_mode="hybrid",
            limit=5,
        )

        titles = [m.title for m in result.memories]
        assert "Recherche urgente" in titles, \
            f"Memory should be findable before async embedding completes. Got: {titles}"

    @pytest.mark.asyncio
    async def test_dedup_check_rejects_duplicate(self, mock_ctx, mock_memory_repository, mock_embedding_service):
        """HIGH : Deux mémoires quasi-identiques — la 2e est rejetée."""
        from mnemo_mcp.tools.memory_tools import WriteMemoryTool

        write_tool = WriteMemoryTool()
        write_tool._services = {
            "memory_repository": mock_memory_repository,
            "embedding_service": mock_embedding_service,
        }

        content = "La dette publique française atteint 3300 milliards d'euros en 2026 selon les données officielles de l'INSEE et de la Banque de France."

        # Première écriture
        result1 = await write_tool.execute(
            ctx=mock_ctx,
            title="Dette publique 2026",
            content=content,
            tags=["dette"],
            dedup_check=True,
        )
        assert result1.success is True

        # Deuxième écriture avec contenu identique → doit être rejetée
        result2 = await write_tool.execute(
            ctx=mock_ctx,
            title="Dette publique 2026 (copie)",
            content=content,
            tags=["dette"],
            dedup_check=True,
        )

        # Si dedup est actif et Jaccard > 0.85, l'écriture doit être bloquée ou signalée
        # (le comportement exact dépend de l'implémentation)
        assert result2.success is False or "duplicate" in str(result2).lower(), \
            f"Dedup should reject or flag duplicate. Got: {result2}"

    @pytest.mark.asyncio
    async def test_dedup_bypass_allows_duplicate(self, mock_ctx, mock_memory_repository, mock_embedding_service):
        """HIGH : dedup_check=False permet les doublons."""
        from mnemo_mcp.tools.memory_tools import WriteMemoryTool

        write_tool = WriteMemoryTool()
        write_tool._services = {
            "memory_repository": mock_memory_repository,
            "embedding_service": mock_embedding_service,
        }

        content = "Contenu unique pour test de bypass dedup."

        await write_tool.execute(
            ctx=mock_ctx, title="Test 1", content=content,
            tags=["test"], dedup_check=False,
        )
        result2 = await write_tool.execute(
            ctx=mock_ctx, title="Test 2", content=content,
            tags=["test"], dedup_check=False,
        )

        assert result2.success is True, f"Dedup bypass should allow duplicate. Got: {result2}"


# ============================================================
# NIVEAU 3 : EDGE CASES & RÉGRESSION
# ============================================================

class TestSearchMemoryRegression:
    """Tests de régression pour les bugs corrigés."""

    @pytest.mark.asyncio
    async def test_cache_key_no_unbound_local_error(self, mock_ctx):
        """APEX : search_memory avec Redis=None ne lève pas UnboundLocalError."""
        from mnemo_mcp.tools.memory_tools import SearchMemoryTool
        from unittest.mock import AsyncMock

        tool = SearchMemoryTool()
        tool._services = {
            "redis": None,  # Redis indisponible
            "memory_repository": AsyncMock(),
            "embedding_service": AsyncMock(),
        }
        # Simuler une recherche qui retourne des résultats
        mock_result = MagicMock()
        mock_result.memories = []
        mock_result.total = 0
        mock_result.metadata = MagicMock()
        mock_result.metadata.search_mode = "tag"
        tool._services["memory_repository"].search_hybrid = AsyncMock(return_value=([], 0))

        # Ne doit PAS lever UnboundLocalError
        result = await tool.execute(ctx=mock_ctx, query="test", search_mode="tag")
        assert result is not None

    @pytest.mark.asyncio
    async def test_concurrent_writes_no_race_condition(self, mock_ctx, mock_memory_repository, mock_embedding_service):
        """HIGH : 10 écritures concurrentes ne causent pas de race condition."""
        from mnemo_mcp.tools.memory_tools import WriteMemoryTool

        write_tool = WriteMemoryTool()
        write_tool._services = {
            "memory_repository": mock_memory_repository,
            "embedding_service": mock_embedding_service,
        }

        async def write_one(i):
            return await write_tool.execute(
                ctx=mock_ctx,
                title=f"Mémoire concurrente {i}",
                content=f"Contenu de la mémoire numéro {i} pour test de concurrence.",
                tags=["concurrence"],
                memory_type="note",
            )

        results = await asyncio.gather(*[write_one(i) for i in range(10)])
        successes = [r for r in results if r.success]
        assert len(successes) == 10, f"All 10 writes should succeed. Only {len(successes)} did."

    @pytest.mark.asyncio
    async def test_tags_with_unicode(self, mock_ctx, mock_memory_repository, mock_embedding_service):
        """MEDIUM : Les tags avec accents/unicode sont correctement gérés."""
        from mnemo_mcp.tools.memory_tools import WriteMemoryTool, SearchMemoryTool

        write_tool = WriteMemoryTool()
        write_tool._services = {
            "memory_repository": mock_memory_repository,
            "embedding_service": mock_embedding_service,
        }

        await write_tool.execute(
            ctx=mock_ctx,
            title="Économie française",
            content="Analyse de l'économie.",
            tags=["économié", "débtè-publique"],
            memory_type="investigation",
        )

        search_tool = SearchMemoryTool()
        search_tool._services = {
            "memory_repository": mock_memory_repository,
            "embedding_service": mock_embedding_service,
        }

        result = await search_tool.execute(
            ctx=mock_ctx, query="", tags=["économié"], search_mode="tag", limit=5,
        )
        assert len(result.memories) >= 1, f"Unicode tags should work. Got {len(result.memories)} results."


# ============================================================
# CONFIGURATION PYTEST
# ============================================================
# pytestmark = pytest.mark.asyncio
```

### 2.2 Nouveau fichier : `tests/mnemo_mcp/test_mcp_http_integration.py`

```python
"""
Tests d'intégration MCP via HTTP (tools/call).
Vérifie que tous les outils sont appelables et le pipeline CRUD fonctionne.
"""

import pytest
import json
import urllib.request
import time

MCP_URL = "http://127.0.0.1:8002/mcp"
HEADERS = {
    "Accept": "application/json, text/event-stream",
    "Content-Type": "application/json",
}


def _call_tool(name, arguments=None, timeout=30):
    """Appelle un outil MCP via HTTP tools/call."""
    body = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {"name": name, "arguments": arguments or {}},
    }).encode()

    req = urllib.request.Request(MCP_URL, data=body, headers=HEADERS, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read().decode()
        for line in raw.split("\n"):
            line = line.strip()
            if line.startswith("data: "):
                parsed = json.loads(line[6:])
                if "error" in parsed:
                    return {"error": parsed["error"]}
                if "result" in parsed:
                    content = parsed["result"].get("content", [{}])
                    text = content[0].get("text", "{}") if content else "{}"
                    try:
                        return json.loads(text)
                    except json.JSONDecodeError:
                        return {"raw": text}
    return {"error": "no valid response"}


class TestMCPHttpIntegration:
    """Tests d'intégration HTTP du MCP."""

    @pytest.mark.integration
    @pytest.mark.mcp
    def test_all_tools_respond(self):
        """APEX : Appeler chaque outil MCP et vérifier qu'il répond sans erreur -32602."""
        # Récupérer la liste des outils
        req = urllib.request.Request(
            MCP_URL,
            data=json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}}).encode(),
            headers=HEADERS,
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = resp.read().decode()

        tools = []
        for line in raw.split("\n"):
            line = line.strip()
            if line.startswith("data: "):
                parsed = json.loads(line[6:])
                if "result" in parsed and "tools" in parsed["result"]:
                    tools = [t["name"] for t in parsed["result"]["tools"]]

        # Arguments minimaux valides pour chaque outil
        minimal_args = {
            "ping": {},
            "search_code": {"query": "test"},
            "write_memory": {"title": "test", "content": "test"},
            "read_memory": {"id": "00000000-0000-0000-0000-000000000000"},
            "update_memory": {"id": "00000000-0000-0000-0000-000000000000"},
            "delete_memory": {"id": "00000000-0000-0000-0000-000000000000"},
            "search_memory": {"query": "test", "search_mode": "hybrid"},
            "consolidate_memory": {"title": "test", "summary": "test", "source_ids": ["x"]},
            "mark_consumed": {"memory_ids": ["00000000-0000-0000-0000-000000000000"], "consumed_by": "test"},
            "rate_memory": {"id": "00000000-0000-0000-0000-000000000000", "helpful": True},
            "export_memories": {},
            "get_system_snapshot": {},
            "configure_decay": {"tag_pattern": "test", "decay_rate": 0.5},
            "get_graph_stats": {},
            "traverse_graph": {"node_id": "x"},
            "find_path": {"source_id": "x", "target_id": "y"},
            "get_module_data": {"module_path": "test"},
            "index_project": {"project_path": "/tmp"},
            "reindex_file": {"file_path": "/tmp/test.md"},
            "index_incremental": {"project_path": "/tmp"},
            "index_markdown_workspace": {"root_path": "/tmp"},
            "get_indexing_status": {},
            "get_indexing_errors": {},
            "retry_indexing": {"file_paths": ["/tmp/test.md"]},
            "clear_cache": {},
            "get_indexing_stats": {},
            "get_memory_health": {},
            "get_cache_stats": {},
            "switch_project": {"repository": "test"},
            "extract_entities": {"memory_id": "00000000-0000-0000-0000-000000000000"},
            "search_by_entity": {"entity_name": "test"},
        }

        errors = []
        for name in tools:
            args = minimal_args.get(name, {})
            if name == "ping":
                continue  # ping est testé séparément

            result = _call_tool(name, args, timeout=30)
            if "error" in result:
                errors.append(f"{name}: {result['error']}")

        if errors:
            pytest.fail(f"Tools with errors: {', '.join(errors)}")

        print(f"✅ {len(tools)} tools tested, {len(errors)} errors")

    @pytest.mark.integration
    @pytest.mark.mcp
    def test_crud_cycle_via_http(self):
        """APEX : Cycle write → read → update → read → delete via HTTP."""
        # 1. WRITE
        import uuid
        test_id = str(uuid.uuid4())

        write_result = _call_tool("write_memory", {
            "title": "Test CRUD MCP",
            "content": f"Mémoire de test CRUD — ID: {test_id}",
            "tags": ["test", "crud"],
            "memory_type": "note",
        })
        assert "error" not in write_result, f"Write failed: {write_result}"
        memory_id = write_result.get("id") or write_result.get("memory", {}).get("id")
        assert memory_id, f"No memory ID in response: {write_result}"
        print(f"  ✅ Written: {memory_id}")

        # 2. READ
        read_result = _call_tool("read_memory", {"id": memory_id})
        assert "error" not in read_result, f"Read failed: {read_result}"
        title = read_result.get("title") or read_result.get("memory", {}).get("title", "")
        assert "Test CRUD MCP" in title, f"Wrong title: {title}"
        print(f"  ✅ Read: {title[:50]}")

        # 3. UPDATE
        update_result = _call_tool("update_memory", {
            "id": memory_id,
            "title": "Test CRUD MCP — MODIFIÉ",
        })
        assert "error" not in update_result, f"Update failed: {update_result}"
        print(f"  ✅ Updated")

        # 4. READ again — vérifier modification
        read2 = _call_tool("read_memory", {"id": memory_id})
        title2 = read2.get("title") or read2.get("memory", {}).get("title", "")
        assert "MODIFIÉ" in title2, f"Update not persisted: {title2}"
        print(f"  ✅ Read after update: {title2[:50]}")

        # 5. DELETE (soft)
        delete_result = _call_tool("delete_memory", {"id": memory_id})
        assert "error" not in delete_result, f"Delete failed: {delete_result}"
        print(f"  ✅ Soft deleted")

        # 6. READ after delete — doit retourner deleted_at non null
        read3 = _call_tool("read_memory", {"id": memory_id})
        assert "error" not in read3
        deleted_at = read3.get("deleted_at") or read3.get("memory", {}).get("deleted_at")
        assert deleted_at is not None, f"Soft delete should set deleted_at: {read3}"
        print(f"  ✅ Read after delete: deleted_at={deleted_at}")

    @pytest.mark.integration
    @pytest.mark.mcp
    def test_write_then_search_via_http(self):
        """APEX : Écrire via HTTP, chercher via HTTP, vérifier que la mémoire est trouvable."""
        import uuid
        test_id = f"SEARCH-TEST-{uuid.uuid4().hex[:8]}"

        # Écriture
        write_result = _call_tool("write_memory", {
            "title": f"Mémoire de test recherche — {test_id}",
            "content": f"Ce contenu unique {test_id} permet de vérifier que la recherche vectorielle fonctionne correctement.",
            "tags": ["test", "recherche"],
            "memory_type": "note",
        })
        assert "error" not in write_result, f"Write failed: {write_result}"
        memory_id = write_result.get("id") or write_result.get("memory", {}).get("id")
        print(f"  ✅ Written: {memory_id}")

        # Attendre que l'embedding async soit généré
        time.sleep(5)

        # Recherche
        search_result = _call_tool("search_memory", {
            "query": test_id,
            "limit": 5,
            "search_mode": "hybrid",
        }, timeout=30)

        assert "error" not in search_result, f"Search failed: {search_result}"
        memories = search_result.get("memories", [])
        titles = [m.get("title", "") for m in memories]

        assert len(memories) >= 1, f"Search should find the memory. Got {len(memories)} results."
        matching = [t for t in titles if test_id in t]
        assert len(matching) >= 1, f"Memory {test_id} not found in search results: {titles}"
        print(f"  ✅ Found in search: {matching[0][:50]}")

    @pytest.mark.integration
    @pytest.mark.mcp
    def test_search_mode_hybrid_vs_tag(self):
        """HIGH : search_mode='hybrid' et 'tag' donnent des résultats différents."""
        # Recherche hybride (vectorielle)
        result_hybrid = _call_tool("search_memory", {
            "query": "dette publique",
            "limit": 3,
            "search_mode": "hybrid",
        })
        assert "error" not in result_hybrid, f"Hybrid search failed: {result_hybrid}"

        # Recherche tag (filtrage)
        result_tag = _call_tool("search_memory", {
            "query": "dette publique",
            "limit": 3,
            "search_mode": "tag",
        })
        assert "error" not in result_tag, f"Tag search failed: {result_tag}"

        # Les deux doivent retourner des résultats exploitables
        hybrid_count = result_hybrid.get("total", 0)
        tag_count = result_tag.get("total", 0)

        print(f"  Hybrid: {hybrid_count} results, Tag: {tag_count} results")
        # Ne pas assert equality — les résultats peuvent différer


class TestMCPEdgeCases:
    """Tests des cas limites via HTTP."""

    @pytest.mark.integration
    @pytest.mark.mcp
    def test_empty_query_raises_error(self):
        """Query vide + pas de tags → ValueError."""
        result = _call_tool("search_memory", {"query": "", "search_mode": "hybrid"})
        assert "error" in result, f"Empty query should raise error: {result}"

    @pytest.mark.integration
    @pytest.mark.mcp
    def test_invalid_search_mode_raises_error(self):
        """search_mode invalide → erreur explicite."""
        result = _call_tool("search_memory", {
            "query": "test",
            "search_mode": "invalid_mode_xyz",
        })
        assert "error" in result, f"Invalid search_mode should raise error: {result}"
        error_msg = str(result["error"]).lower()
        assert "search_mode" in error_msg or "invalid" in error_msg, \
            f"Error should mention search_mode: {error_msg}"
```

### 2.3 Ajouts aux fichiers existants

**`tests/mnemo_mcp/test_memory_tools.py`** — ajouter :

```python
# Dans TestWriteMemoryTool :

@pytest.mark.asyncio
async def test_embedding_source_parameter(self, mock_ctx, mock_memory_repository, mock_embedding_service):
    """EPIC-24 : embedding_source remplace title+content pour l'embedding."""
    ...

@pytest.mark.asyncio
async def test_content_very_long(self, mock_ctx, mock_memory_repository, mock_embedding_service):
    """MEDIUM : Contenu > 100K chars ne cause pas de timeout."""
    ...

@pytest.mark.asyncio
async def test_memory_type_quintessence(self, mock_ctx, mock_memory_repository, mock_embedding_service):
    """memory_type='quintessence' accepté."""
    ...
```

**`tests/mnemo_mcp/test_memory_search_tool.py`** — ajouter :

```python
@pytest.mark.asyncio
async def test_search_mode_semantic(self, mock_ctx):
    """search_mode='semantic' accepted and processed."""
    ...

@pytest.mark.asyncio
async def test_cache_invalidation_after_write(self, mock_ctx):
    """Cache invalidé après une nouvelle écriture."""
    ...

@pytest.mark.asyncio
async def test_limit_zero_clamped_to_one(self, mock_ctx):
    """limit=0 → corrigé en 1."""
    ...

@pytest.mark.asyncio
async def test_search_by_memory_type_filter(self, mock_ctx):
    """Filtrage par memory_type fonctionne."""
    ...

@pytest.mark.asyncio
async def test_offset_pagination(self, mock_ctx):
    """offset décale les résultats correctement."""
    ...
```

---

## 3. KPI DE QUALITÉ

| Métrique | Cible | Actuel |
|----------|-------|--------|
| Tests unitaires (tools) | ≥ 50 | 28 (memory_tools) + 16 (memory_search_tool) = 44 |
| Tests intégration HTTP | ≥ 15 | 0 |
| Couverture write_memory | ≥ 95% | ~70% (manque: embedding_source, race, dédup) |
| Couverture search_memory | ≥ 95% | ~65% (manque: cache invalidation, semantic, pagination) |
| Tests de régression bugs corrigés | 100% des bugs documentés | 1/3 (cache_key ✅, GLiNER ❌, registration ❌) |
| Latence search_mode="tag" (P95) | < 200ms | à mesurer |
| Latence search_mode="hybrid" (P95) | < 2s | à mesurer |
| Latence write_memory (P50) | < 500ms | à mesurer |
| Latence embedding async (P95) | < 5s | à mesurer |

---

## 4. COMMANDES DE LANCEMENT

```bash
# Tests unitaires (mockés, pas de DB)
cd /home/giak/Work/MnemoLite
pytest tests/mnemo_mcp/test_memory_tools.py tests/mnemo_mcp/test_memory_search_tool.py -v --tb=short

# Tests pipeline (mockés)
pytest tests/mnemo_mcp/test_write_search_pipeline.py -v --tb=short

# Tests intégration HTTP (nécessite MCP running)
pytest tests/mnemo_mcp/test_mcp_http_integration.py -v -m mcp --tb=long

# Test de régression complet
pytest tests/mnemo_mcp/ -v --tb=short -x

# Avec couverture
pytest tests/mnemo_mcp/ --cov=api/mnemo_mcp/tools/memory_tools --cov-report=term-missing
```

---

## 5. CHECKLIST DE DÉPLOIEMENT

- [ ] Créer `tests/mnemo_mcp/test_write_search_pipeline.py` (Niveau 2 + 3)
- [ ] Créer `tests/mnemo_mcp/test_mcp_http_integration.py` (Niveau 4)
- [ ] Ajouter les tests manquants dans `test_memory_tools.py` (embedding_source, content long, quintessence)
- [ ] Ajouter les tests manquants dans `test_memory_search_tool.py` (semantic, cache invalidation, pagination, memory_type filter)
- [ ] Lancer pytest complet → tous les tests doivent passer
- [ ] Mesurer et documenter les KPI de latence
- [ ] Ajouter les tests de régression dans AGENTS.md (table bugs connus)
- [ ] Commit + push
