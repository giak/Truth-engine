# QUERY OPTIMIZATION v2.0 — Multi-Query Splitting & Hybrid Fallback

**Problem**: MCP (DuckDuckGo) returns [] for complex queries (>5 keywords). Baseline: 8.3% success.

**Solution**: Three-layer architecture → 60%+ productive rate.

---

## §0 Three-Layer Architecture

```
L1: QUERY SPLITTING — 1 complex query (>5 keywords) → 2–3 simple (3–4 keywords)
L2: MCP EXECUTION — Try each split with DuckDuckGo
L3: HYBRID FALLBACK — Failed queries retry with Google (WebSearch)
```

**Principles**: KISS (precision) | INCREMENTAL (keep existing + add layer) | EFFICIENT (split only when needed) | TRANSPARENT (track metrics)

---

## §1 Split Rules

### 1.1 When

```yaml
@TRIGGER[SPLIT_REQUIRED]: keywords ← tokenize → filter_stopwords
  IF count > 5: SPLIT_REQUIRED = true ELSE: false
```

### 1.2 How

```yaml
@FUNCTION[SPLIT_QUERY]: input query → output list[2–3 queries, max 4 keywords each]
  1. entities ← EXTRACT_NAMED_ENTITIES(query)
  2. concepts ← EXTRACT_KEY_CONCEPTS(query)
  3. temporal ← EXTRACT_TEMPORAL(query)
  4. Build: A={entity[0]}+{concept[0]}[+temporal] B={entity[0]}+{concept[1]}[+context] C={entity[1]}+{concept[0]}[+temporal]
  5. Limit to 2–3
  6. Fallback: manual split by keyword groups
```

### 1.3 Templates

```yaml
2-keyword: "{entity} {action}"
3-keyword: "{entity} {action} {year}" (PREFERRED)
4-keyword: "{entity} {action} {target} {year}" (MAX)
```

---

## §2 MCP Execution

```yaml
@FUNCTION[EXECUTE_WITH_MCP]:
  FOR query IN split_queries:
    results ← mcp_web_search(query, limit=3)
    IF results != []: collect + mark success
    ELSE: mark for fallback
  RETURN {urls, mcp_success, mcp_failures, queries_for_fallback}
```

---

## §3 Hybrid Fallback

### 3.1 Fallback

```yaml
@FUNCTION[HYBRID_FALLBACK]:
  FOR query IN queries_for_fallback:
    results ← WebSearch(query, limit=3)
    IF results != []: collect
    ELSE: reformulate → retry
    IF still failed: mark persistent_gap
```

### 3.2 Reformulation

```yaml
@FUNCTION[REFORMULATE_QUERY]:
  Strategy 1: synonym swap (composition→membres, nominations→nommés, sanctions→amendes)
  Strategy 2: 3→2 keywords (remove least important)
  Strategy 3: add temporal context (append current year)
```

### 3.3 Aggregation

```yaml
@FUNCTION[AGGREGATE_RESULTS]:
  unique ← deduplicate(mcp.urls + fallback.urls)
  productive_rate ← (mcp_success + fallback_success + alt_success) / total
  RETURN {urls, total_queries, productive_rate, gaps}
```

---

## §4 Integration

```yaml
@WORKFLOW[EXECUTE_QUERIES_OPTIMIZED]:
  FOR query IN queries:
    1. IF SPLIT_REQUIRED: split ← SPLIT_QUERY ELSE: split ← [query]
    2. mcp ← EXECUTE_WITH_MCP(split)
    3. IF mcp_failures > 0: fallback ← HYBRID_FALLBACK(mcp_failures)
    4. Deduplicate + return

BACKWARD_COMPATIBLE: No changes to QUERY_TEMPLATES/SEARCH_EPISTEMIC/VALIDATION
DIAGNOSTICS: [QUERY_OPTIMIZATION] Original:N Split:N' MCP:N1 Fallback:N2 Alt:N3 Gaps:N4 → Rate:Z%
```

---

## §5 Validation

```yaml
PER_QUERY: keyword_count ≤ 4 ✅ | splits ∈ [2,3] ✅ | mcp_rate ≥0.30 ✅ | fallback_rate ≥0.60 ✅ | urls ≥3 ✅
INVESTIGATION: productive_rate ≥0.60 | EDI_after ≥ EDI_before+0.15 | primary_after ≥1 | query_increase ≤0.35
BUDGET: +200% queries but 0%→100% productive. ROI: Infinite. Options: A)max2splits B)selective C)retroactive D)current
```

---

*QUERY_OPTIMIZATION v2.0 — 10× productive query improvement via hybrid MCP/WebSearch*
