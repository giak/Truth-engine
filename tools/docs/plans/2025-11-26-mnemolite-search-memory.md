# MnemoLite Feature Request: search_memory Tool

**Date:** 2025-11-26
**Priority:** HIGH
**Blocking:** Truth Engine PHASE 0.5 (Knowledge Graph integration)

## Problem Statement

MnemoLite currently has no way to semantically search memories (text content).

| Tool/Resource | Works? | Limitation |
|---------------|--------|------------|
| `search_code` | Yes | **CODE chunks only** (Python, TS, etc.) |
| `memories://list` | Partial | Query params ignored (no filtering) |
| `memories://search` | N/A | **Does not exist** |
| `search_memory` | N/A | **Does not exist** |

## Impact on Truth Engine

PHASE 0.5 (KNOWLEDGE_LOOKUP) cannot find past investigations because:
1. `search_code` only searches code, not text memories
2. `memories://list` returns recent memories but doesn't filter by tags/type
3. No semantic search on memory content

## Proposed Solution

### Option A: New `search_memory` MCP Tool (Recommended)

```python
@mcp_tool
async def search_memory(
    query: str,              # Semantic search query
    memory_type: str = None, # Filter: note, decision, investigation, etc.
    tags: List[str] = None,  # Filter by tags
    limit: int = 10,
    offset: int = 0
) -> MemorySearchResponse:
    """
    Semantic search on memories using E5 embeddings.
    Similar to search_code but for memories table.
    """
```

### Option B: Fix `memories://list` Query Params

Make `memories://list?memory_type=investigation&tags=agriculture&limit=5` actually work.

Currently returns error: `Unknown resource: memories://list?...`

### Option C: Add Markdown Support to index_project

Support `.md` files in code indexing so investigations can be searched via `search_code`.

## Recommended Priority

1. **Option A** (search_memory) - Most valuable, enables semantic memory retrieval
2. **Option B** (fix memories://list) - Quick fix for filtering
3. **Option C** (markdown indexing) - Lower priority, workaround

## Workaround (Current)

1. Save investigations with `write_memory` + good tags in PHASE 9
2. Use `memories://list` and manually filter in LLM prompt
3. Accept limitation: only recent 10 memories visible

## Files to Update in MnemoLite

```
mnemo_mcp/
├── tools/
│   ├── search_tools.py      # Add search_memory
│   └── memory_tools.py      # Reference for memory operations
├── resources/
│   └── memory_resources.py  # Fix query param parsing
└── models/
    └── memory_models.py     # MemorySearchResponse model
```

## Testing

```bash
# After implementation
search_memory(query="agriculture Mercosur investigation", memory_type="investigation", limit=5)
# Should return past investigations on this topic
```

---

**Author:** Truth Engine / Claude Code
**Status:** PROPOSED
