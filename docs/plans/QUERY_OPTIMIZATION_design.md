# QUERY_OPTIMIZATION Design v1.0
**Date:** 2025-11-14
**Status:** DESIGN → IMPLEMENTATION
**Problem:** MCP web-search (DuckDuckGo) returns [] for complex French queries (11/12 failures in ARCOM investigation)

---

## 1. Problem Analysis

### 1.1 Symptoms
From investigation `logs/2025-11-14_11-22-25_arcom-cnews-climat.md`:
- **12/12 queries executed** (100%)
- **1/12 productive** (8.3%) ❌
- **11/12 returned []** → Technical issue, not epistemic

### 1.2 Failed Query Examples
```
Query 1: "CNews ARCOM sanctions historique liste complète 2020-2024"
         → [] (9 keywords, ultra-specific)

Query 2: "ARCOM sanctions TF1 LCI BFM comparables désinformation 2024"
         → [] (8 keywords, multiple entities)

Query 3: "CNews défense amende ARCOM climat liberté expression censure"
         → [] (8 keywords, abstract concepts)

Query 4: "ARCOM composition membres nominations gouvernement Macron CSA"
         → [] (7 keywords, institutional details)
```

### 1.3 Root Cause (Brainstorming Q1: C)
**"il faut plus de requettes"** — Too many keywords in single query

**DuckDuckGo limitations:**
- Struggles with >5-6 keywords
- Poor French technical term indexation
- Less comprehensive than Google for specific queries

**Google (WebSearch) advantages:**
- Better French indexation
- Handles complex queries
- More comprehensive results

---

## 2. Solution Architecture (User Answers Q1-Q6)

### 2.1 Core Strategy: Multi-Query + Hybrid Fallback

**Q1: C** → Too many keywords per query, need more queries
**Q2: C** → Multi-query strategy preferred
**Q3: "combiner C et B"** → Combine MCP optimization + WebSearch fallback
**Q4: C "tendre vers D"** → Multi-queries, aiming for no compromise
**Q5: B** → Simple 3-word queries (e.g., "ARCOM nominations Macron")
**Q6: C** → Hybrid: keep current templates + add fallback

### 2.2 Three-Layer Architecture

```yaml
QUERY_OPTIMIZATION_ARCHITECTURE:

  # Layer 1: Query Splitting (Q1 C, Q2 C, Q5 B)
  SPLIT_COMPLEX_QUERY:
    - Input: 1 complex query (>5 keywords)
    - Output: 2-3 simple queries (3-4 keywords each)
    - Example:
        ❌ "ARCOM composition membres nominations gouvernement Macron CSA"
        ✅ ["ARCOM membres", "ARCOM nominations Macron", "CSA ARCOM transition"]

  # Layer 2: MCP-Optimized Execution (Q3 C, Q6 C)
  EXECUTE_WITH_MCP:
    - Try each split query with MCP (DuckDuckGo)
    - Collect all results
    - If any query returns [], proceed to Layer 3

  # Layer 3: Hybrid Fallback (Q3 B, Q6 C)
  FALLBACK_TO_WEBSEARCH:
    - For queries that returned [] in Layer 2
    - Retry with WebSearch (Google)
    - If still [], try alternative formulation
    - If persistent [], log as gap (existing behavior)
```

### 2.3 Design Principles

1. **KISS (Q4 "tendre vers D"):** No compromise on precision, but simple implementation
2. **Incremental (Q6 C):** Keep existing templates, add new layer
3. **Backward compatible:** Existing investigations still work
4. **Resource efficient:** Don't double all queries, only split when needed

---

## 3. Implementation Specification

### 3.1 Query Splitting Rules

```yaml
SPLIT_RULES:
  # Rule 1: Keyword count threshold
  IF query.keyword_count > 5:
    → SPLIT_REQUIRED = true
  ELSE:
    → SPLIT_REQUIRED = false  # Keep original query

  # Rule 2: Splitting strategy (Q5 B: 3-word queries)
  SPLIT_STRATEGY:
    # Extract core entities
    entities ← extract_named_entities(query)  # ARCOM, CNews, Macron, etc.

    # Extract core concepts
    concepts ← extract_key_concepts(query)    # sanctions, nominations, composition

    # Build simple queries (3-4 keywords max)
    split_queries ← []
    FOR entity IN entities:
      FOR concept IN concepts[0:2]:  # Max 2 concepts per entity
        split_query ← build_query(entity, concept, context_year)
        IF split_query.keyword_count ≤ 4:
          split_queries.append(split_query)

    # Limit to 2-3 queries (Q2 C: multi-query but not excessive)
    RETURN split_queries[0:3]

  # Rule 3: Query templates (Q5 B examples)
  SIMPLE_QUERY_PATTERNS:
    - "{entity} {action}"                    # "ARCOM sanctions"
    - "{entity} {action} {year}"             # "ARCOM nominations 2024"
    - "{entity} {concept}"                   # "CNews désinformation"
    - "{entity} {target} {action}"           # "ARCOM CNews amende"
```

### 3.2 Hybrid Fallback Logic

```yaml
HYBRID_FALLBACK:
  # Step 1: Execute all split queries with MCP
  FOR query IN split_queries:
    results_mcp ← mcp_web_search(query, limit=3)

    IF results_mcp = []:
      # Step 2: Fallback to WebSearch for failed queries
      results_google ← WebSearch(query, limit=3)

      IF results_google != []:
        collected_results.extend(results_google)
        fallback_used.append(query)
      ELSE:
        # Step 3: Try alternative formulation
        alternative_query ← reformulate(query)
        results_alt ← WebSearch(alternative_query, limit=3)

        IF results_alt != []:
          collected_results.extend(results_alt)
          alternative_used.append(query)
        ELSE:
          # Step 4: Log as gap (existing behavior)
          gaps.append(query)
    ELSE:
      collected_results.extend(results_mcp)
      mcp_success.append(query)

  # Return aggregated results
  RETURN {
    results: collected_results,
    mcp_success: len(mcp_success),
    fallback_used: len(fallback_used),
    alternative_used: len(alternative_used),
    gaps: len(gaps)
  }
```

### 3.3 Example Transformation

**Input (failed Query 4):**
```
"ARCOM composition membres nominations gouvernement Macron CSA"
```

**Output (split queries):**
```yaml
split_queries:
  - query_1: "ARCOM membres composition"      # 3 keywords
  - query_2: "ARCOM nominations Macron"       # 3 keywords
  - query_3: "CSA ARCOM transition"           # 3 keywords

execution:
  query_1:
    mcp: [] → fallback: WebSearch → [url1, url2, url3] ✅
  query_2:
    mcp: [url4, url5] ✅
  query_3:
    mcp: [] → fallback: WebSearch → [url6] ✅

result:
  total_results: 6 URLs
  mcp_success: 1/3 (33%)
  fallback_success: 2/3 (67%)
  gaps: 0/3 (0%)
```

**Impact:**
- Before: 0 results (query failed)
- After: 6 results (split + hybrid fallback)

---

## 4. Integration Points

### 4.1 New KB File: kb/QUERY_OPTIMIZATION.md

**Purpose:** Define query splitting and hybrid fallback rules
**Sections:**
1. `§1 SPLITTING_RULES` — When and how to split queries
2. `§2 SIMPLE_QUERY_TEMPLATES` — 3-4 keyword patterns (Q5 B)
3. `§3 HYBRID_FALLBACK` — MCP → WebSearch logic (Q3)
4. `§4 REFORMULATION` — Alternative query generation
5. `§5 VALIDATION` — Success criteria

### 4.2 Modifications to system.md

**Location:** Query execution section (search strategy)

**Changes:**
```yaml
# BEFORE (current):
FOR query IN queries:
  results ← mcp_web_search(query)
  IF results != []:
    collected_results.extend(results)

# AFTER (with optimization):
FOR query IN queries:
  # Step 1: Check if splitting needed
  IF query.keyword_count > 5:
    split_queries ← SPLIT_QUERY(query)  # kb/QUERY_OPTIMIZATION.md §1
  ELSE:
    split_queries ← [query]  # Keep original

  # Step 2: Execute with hybrid fallback
  results ← HYBRID_EXECUTE(split_queries)  # kb/QUERY_OPTIMIZATION.md §3
  collected_results.extend(results.urls)

  # Step 3: Track optimization metrics
  optimization_stats.update(results.metrics)
```

### 4.3 Backward Compatibility (Q6 C)

**Principle:** Keep existing templates, add new layer on top

**No changes to:**
- `kb/QUERY_TEMPLATES.md` — Domain-adaptive templates remain unchanged
- Existing query generation logic — Still produces same queries
- EDI/ISN scoring — No formula changes

**New layer:**
- Query splitting happens BEFORE execution
- Hybrid fallback happens DURING execution
- Original queries still attempted first (with MCP)

---

## 5. Testing Strategy

### 5.1 Test Cases: User's 4 Failed Queries

**Test 1: Query 1**
```yaml
Input: "CNews ARCOM sanctions historique liste complète 2020-2024"
Split:
  - "CNews ARCOM sanctions"
  - "ARCOM sanctions 2020-2024"
  - "CNews sanctions historique"
Expected: ≥4 URLs (at least 1 per split query)
```

**Test 2: Query 2**
```yaml
Input: "ARCOM sanctions TF1 LCI BFM comparables désinformation 2024"
Split:
  - "ARCOM TF1 sanctions"
  - "ARCOM LCI BFM"
  - "ARCOM désinformation 2024"
Expected: ≥4 URLs
```

**Test 3: Query 3**
```yaml
Input: "CNews défense amende ARCOM climat liberté expression censure"
Split:
  - "CNews ARCOM amende"
  - "ARCOM climat censure"
  - "CNews défense expression"
Expected: ≥4 URLs
```

**Test 4: Query 4**
```yaml
Input: "ARCOM composition membres nominations gouvernement Macron CSA"
Split:
  - "ARCOM membres composition"
  - "ARCOM nominations Macron"
  - "CSA ARCOM transition"
Expected: ≥4 URLs
```

### 5.2 Success Criteria

**Per-query metrics:**
- `split_count`: 2-3 queries (Q2 C)
- `keyword_avg`: ≤4 keywords per split query (Q5 B)
- `mcp_success_rate`: ≥30% (realistic for DuckDuckGo)
- `fallback_success_rate`: ≥60% (Google more reliable)
- `total_results`: ≥3 URLs per original query (min viable)

**Investigation-level metrics:**
- `productive_queries`: ≥60% (vs current 8.3%)
- `EDI_improvement`: ≥0.15 increase (0.28 → 0.43+)
- `primary_sources`: ≥1 (vs current 0)

### 5.3 Validation Script

**File:** `tests/query_optimization/validate_splitting.sh`

**Checks:**
1. Keyword count reduction (>5 → ≤4)
2. Split query count (2-3 per complex query)
3. MCP execution (all split queries attempted)
4. Fallback triggering ([] → WebSearch)
5. Result aggregation (no duplicates)
6. Backward compatibility (simple queries unchanged)

---

## 6. Resource Impact

### 6.1 Query Budget (Q4 "tendre vers D": no compromise)

**Current budget:**
- SIMPLE: 5 queries
- MEDIUM: 8 queries
- COMPLEX: 12 queries
- APEX: 15 queries

**After optimization:**
- SIMPLE: 5 queries (unchanged, no splitting needed)
- MEDIUM: 8-10 queries (+25% for splitting)
- COMPLEX: 12-16 queries (+33% for splitting)
- APEX: 15-20 queries (+33% for splitting)

**Justification (Q4 C "tendre vers D"):**
- User wants precision, no compromise
- 25-33% budget increase acceptable if it fixes 11/12 failures
- Split queries are simpler → faster execution
- Hybrid fallback only for failed queries (not all)

### 6.2 Implementation Effort

**Phase 1: Core implementation (2-3 hours)**
1. Create `kb/QUERY_OPTIMIZATION.md` (1h)
2. Modify `system.md` query execution logic (1h)
3. Create splitting + fallback functions (1h)

**Phase 2: Testing (1-2 hours)**
1. Test on 4 failed queries (30min)
2. Create validation script (30min)
3. Re-run ARCOM investigation (30min)

**Phase 3: Documentation (30min)**
1. Update `CLAUDE.md` with optimization info
2. Add examples to `kb/QUERY_OPTIMIZATION.md`

**Total effort:** ~4-6 hours

---

## 7. Expected Impact

### 7.1 Quantitative Improvements

**Before (ARCOM investigation):**
```yaml
Queries executed: 12/12 (100%)
Productive queries: 1/12 (8.3%) ❌
Results: 5 URLs
EDI: 0.28 (target 0.70) ❌
◈ PRIMARY: 0/3 ❌
```

**After (with optimization):**
```yaml
Queries executed: 15-16/15 (100%, +25% splits)
Productive queries: 9-10/15 (60-67%) ✅
Results: 18-24 URLs (estimated)
EDI: 0.45-0.55 (target 0.70) 🟡
◈ PRIMARY: 1-2/3 🟡
```

### 7.2 Qualitative Improvements

1. **Resilience:** Hybrid fallback prevents total query failures
2. **Coverage:** Split queries explore more semantic angles
3. **Diversity:** More URLs → better source stratification
4. **User experience:** Visible improvement in investigation quality

### 7.3 Known Limitations (Q4 "tendre vers D": aim for D but realistic)

**Cannot fix:**
- Content gaps (if info doesn't exist online)
- Language barriers (French-only queries on English topics)
- Censored content (if systematically removed)

**Can improve:**
- Query formulation (DuckDuckGo-friendly)
- Fallback coverage (Google as safety net)
- Result aggregation (more diverse sources)

---

## 8. Implementation Checklist

- [ ] Create `kb/QUERY_OPTIMIZATION.md` (§1-5)
- [ ] Modify `system.md` query execution logic
- [ ] Test splitting on 4 failed queries
- [ ] Create validation script (`tests/query_optimization/validate_splitting.sh`)
- [ ] Re-run ARCOM investigation with optimization
- [ ] Update `CLAUDE.md` with optimization info
- [ ] Validate EDI/ISN improvements

**Status:** READY TO IMPLEMENT
**Next step:** Create `kb/QUERY_OPTIMIZATION.md` specification

---

**Version:** v1.0
**Date:** 2025-11-14
**Based on:** User brainstorming answers Q1-Q6 (multi-query + hybrid fallback strategy)
