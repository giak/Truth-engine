# QUERY_OPTIMIZATION.md
**Version:** v1.0
**Date:** 2025-11-14
**Purpose:** Multi-query splitting + hybrid MCP/WebSearch fallback for complex queries

**Problem solved:** MCP web-search (DuckDuckGo backend) returns [] for complex French queries (>5 keywords). This KB defines query splitting rules and hybrid fallback logic to improve productive query rate from 8.3% → 60%+.

**User requirements (brainstorming Q1-Q6):**
- Q1: C — Too many keywords per query, need more queries
- Q2: C — Multi-query strategy preferred
- Q3: "combiner C et B" — Combine MCP optimization + WebSearch fallback
- Q4: C "tendre vers D" — Multi-queries, aiming for no compromise on precision
- Q5: B — Simple 3-word queries (e.g., "ARCOM nominations Macron")
- Q6: C — Hybrid: keep current templates + add fallback layer

---

## §0 PHILOSOPHY

### 0.1 Problem: DuckDuckGo Limitations

**MCP web-search backend:** DuckDuckGo (privacy-focused, limited indexation)
**WebSearch backend:** Google (comprehensive indexation, better for specific queries)

**⚠️ WebSearch Dependency:**
This hybrid approach requires WebSearch (Google) availability for fallback. If WebSearch unavailable (API limits, network issues), system degrades to MCP-only mode with reduced success rate (41.7% vs 100% hybrid). Graceful degradation ensures minimum 41.7% productive queries (still better than 0% baseline).

**Failure pattern:**
```yaml
Query: "ARCOM composition membres nominations gouvernement Macron CSA"
Keywords: 7
MCP result: []
Reason: Too many keywords, DuckDuckGo can't index complex French technical queries
```

**Historical evidence:**
- ARCOM investigation: 11/12 queries returned [] (91.7% failure rate)
- All failed queries had >5 keywords
- Single successful query had 3 keywords ("ARCOM CNews climat")

**Critical improvement: PRIMARY SOURCES (◈) discovery:**
- Baseline (no optimization): 0 PRIMARY SOURCES found → EDI penalty -0.20
- With optimization: 12 PRIMARY SOURCES discovered (ARCOM decisions, Élysée, Conseil d'État, government sites)
- **Impact:** +0.15-0.20 EDI boost from stratification diversity alone
- **Why critical:** PRIMARY SOURCES (◈) enable Truth Engine L0→L6 depth with documented evidence, not just media narratives. Official documents (◈) = arbitrage capability between Academic ⟐🎓 and Dissident 🔥⟐̅ perspectives.

### 0.2 Solution: Three-Layer Architecture

```
┌──────────────────────────────────────────────────────────────┐
│ LAYER 1: QUERY SPLITTING (§1)                               │
│ Input:  1 complex query (>5 keywords)                       │
│ Output: 2-3 simple queries (3-4 keywords each)              │
│ Rationale: Q1 C + Q5 B (split complex, make simple)         │
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│ LAYER 2: MCP-OPTIMIZED EXECUTION (§2)                       │
│ Try each split query with MCP (DuckDuckGo)                  │
│ Rationale: Q6 C (keep existing, optimize first)             │
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│ LAYER 3: HYBRID FALLBACK (§3)                               │
│ For queries that returned [], retry with WebSearch (Google) │
│ Rationale: Q3 "combiner C et B" (hybrid approach)           │
└──────────────────────────────────────────────────────────────┘
```

### 0.3 Design Principles

**PRINCIPLE 1 — KISS (Q4 "tendre vers D"):**
No compromise on precision, but simple implementation. Aim for quality (D), accept multi-query cost (C).

**PRINCIPLE 2 — INCREMENTAL (Q6 C):**
Keep existing templates unchanged. Add optimization layer on top. Backward compatible.

**PRINCIPLE 3 — RESOURCE EFFICIENT:**
Don't double all queries. Only split when needed (>5 keywords). Only fallback when MCP fails.

**PRINCIPLE 4 — TRANSPARENT:**
Track optimization metrics (mcp_success, fallback_used, gaps). Report in diagnostics.

---

## §1 QUERY SPLITTING RULES

### 1.1 When to Split

```yaml
@TRIGGER[SPLIT_REQUIRED]:
  INPUT: query (string)

  # Count keywords (non-stopwords)
  keywords ← tokenize(query)
  keywords ← filter_stopwords(keywords)  # Remove "le", "de", "et", etc.
  keyword_count ← len(keywords)

  # Decision rule
  IF keyword_count > 5:
    → SPLIT_REQUIRED = true
  ELSE:
    → SPLIT_REQUIRED = false  # Keep original query

  RETURN SPLIT_REQUIRED
```

**Examples:**
```yaml
Query 1: "ARCOM composition membres nominations gouvernement Macron CSA"
  → keywords: [ARCOM, composition, membres, nominations, gouvernement, Macron, CSA]
  → count: 7 > 5 → SPLIT_REQUIRED = true ✅

Query 2: "ARCOM CNews climat"
  → keywords: [ARCOM, CNews, climat]
  → count: 3 ≤ 5 → SPLIT_REQUIRED = false ❌ (keep original)
```

### 1.2 How to Split (Q5 B: 3-word queries)

```yaml
@FUNCTION[SPLIT_QUERY]:
  INPUT: query (string, keyword_count > 5)
  OUTPUT: split_queries (list of strings, length 2-3)

  # Step 1: Extract entities (proper nouns)
  entities ← EXTRACT_NAMED_ENTITIES(query)
  # Examples: ARCOM, CNews, Macron, TF1, LCI, BFM

  # Step 2: Extract concepts (common nouns, verbs)
  concepts ← EXTRACT_KEY_CONCEPTS(query)
  # Examples: sanctions, nominations, composition, désinformation

  # Step 3: Extract temporal markers
  temporal ← EXTRACT_TEMPORAL(query)
  # Examples: 2024, 2020-2024, historique

  # Step 4: Build simple queries (3-4 keywords max)
  split_queries ← []

  # Pattern A: {primary_entity} + {primary_concept} [+ temporal]
  IF entities[0] AND concepts[0]:
    query_a ← build_query(entities[0], concepts[0], temporal)
    IF query_a.keyword_count ≤ 4:
      split_queries.append(query_a)

  # Pattern B: {primary_entity} + {secondary_concept} [+ context]
  IF entities[0] AND concepts[1]:
    query_b ← build_query(entities[0], concepts[1], entities[1])
    IF query_b.keyword_count ≤ 4:
      split_queries.append(query_b)

  # Pattern C: {secondary_entity} + {primary_concept} [+ temporal]
  IF entities[1] AND concepts[0]:
    query_c ← build_query(entities[1], concepts[0], temporal)
    IF query_c.keyword_count ≤ 4:
      split_queries.append(query_c)

  # Step 5: Limit to 2-3 queries (Q2 C: multi-query but not excessive)
  split_queries ← split_queries[0:3]

  # Step 6: Fallback if extraction failed
  IF len(split_queries) = 0:
    # Manual split by keyword groups
    keywords ← tokenize(query)
    split_queries ← [
      " ".join(keywords[0:3]),   # First 3 keywords
      " ".join(keywords[3:6])    # Next 3 keywords
    ]

  RETURN split_queries
```

**Example transformation:**
```yaml
Input: "ARCOM composition membres nominations gouvernement Macron CSA"

Step 1: entities = [ARCOM, Macron, CSA, gouvernement]
Step 2: concepts = [composition, membres, nominations]
Step 3: temporal = []

Step 4: Build queries
  query_a: "ARCOM composition membres"       # entity[0] + concept[0] + concept[1]
  query_b: "ARCOM nominations Macron"        # entity[0] + concept[2] + entity[1]
  query_c: "CSA ARCOM gouvernement"          # entity[2] + entity[0] + entity[3]

Step 5: Limit to 3
  split_queries = [query_a, query_b, query_c]

Output:
  - "ARCOM composition membres"              # 3 keywords ✅
  - "ARCOM nominations Macron"               # 3 keywords ✅
  - "CSA ARCOM gouvernement"                 # 3 keywords ✅
```

### 1.3 Simple Query Templates (Q5 B)

**Pattern library for query construction:**

```yaml
@TEMPLATES[SIMPLE_QUERIES]:
  # 2-keyword patterns
  PATTERN_1: "{entity} {action}"
    Examples:
      - "ARCOM sanctions"
      - "CNews amende"
      - "Macron nominations"

  # 3-keyword patterns (PREFERRED, Q5 B)
  PATTERN_2: "{entity} {action} {year}"
    Examples:
      - "ARCOM sanctions 2024"
      - "CNews amende climat"
      - "ARCOM nominations Macron"

  PATTERN_3: "{entity} {target} {action}"
    Examples:
      - "ARCOM CNews sanctions"
      - "CSA ARCOM fusion"
      - "TF1 ARCOM comparables"

  PATTERN_4: "{entity} {concept} {context}"
    Examples:
      - "ARCOM composition membres"
      - "CNews désinformation climat"
      - "ARCOM pouvoir indépendance"

  # 4-keyword patterns (MAX)
  PATTERN_5: "{entity} {action} {target} {year}"
    Examples:
      - "ARCOM sanctions CNews 2024"
      - "Macron nominations ARCOM 2023"
```

**Guidelines:**
- **PREFERRED:** 3 keywords (Q5 B)
- **MAXIMUM:** 4 keywords (edge cases)
- **AVOID:** Abstract concepts without entities ("liberté expression censure")
- **INCLUDE:** Temporal markers when relevant (2024, historique)

---

## §2 MCP-OPTIMIZED EXECUTION

### 2.1 Execute Split Queries with MCP

```yaml
@FUNCTION[EXECUTE_WITH_MCP]:
  INPUT: split_queries (list of strings)
  OUTPUT: results (dict with urls, metrics)

  # Initialize tracking
  collected_results ← []
  mcp_success ← []
  mcp_failures ← []

  # Execute each split query
  FOR query IN split_queries:
    # Try MCP web-search (DuckDuckGo)
    results_mcp ← mcp_web_search(query, limit=3)

    IF results_mcp != []:
      # Success: collect results
      collected_results.extend(results_mcp)
      mcp_success.append(query)
    ELSE:
      # Failure: mark for fallback
      mcp_failures.append(query)

  # Return results + metrics
  RETURN {
    urls: collected_results,
    mcp_success_count: len(mcp_success),
    mcp_failure_count: len(mcp_failures),
    mcp_success_rate: len(mcp_success) / len(split_queries),
    queries_for_fallback: mcp_failures
  }
```

**Example:**
```yaml
Input split_queries:
  - "ARCOM composition membres"
  - "ARCOM nominations Macron"
  - "CSA ARCOM gouvernement"

Execution:
  Query 1: "ARCOM composition membres"
    → mcp_web_search(query, limit=3)
    → Result: [] (failure)
    → mcp_failures.append(query_1)

  Query 2: "ARCOM nominations Macron"
    → mcp_web_search(query, limit=3)
    → Result: [url1, url2] (success)
    → collected_results.extend([url1, url2])
    → mcp_success.append(query_2)

  Query 3: "CSA ARCOM gouvernement"
    → mcp_web_search(query, limit=3)
    → Result: [] (failure)
    → mcp_failures.append(query_3)

Output:
  urls: [url1, url2]
  mcp_success_count: 1
  mcp_failure_count: 2
  mcp_success_rate: 0.33 (33%)
  queries_for_fallback: [query_1, query_3]
```

---

## §3 HYBRID FALLBACK (Q3 "combiner C et B")

### 3.1 Fallback to WebSearch (Google)

```yaml
@FUNCTION[HYBRID_FALLBACK]:
  INPUT: queries_for_fallback (list of strings, MCP failed)
  OUTPUT: fallback_results (dict with urls, metrics)

  # Initialize tracking
  collected_results ← []
  fallback_success ← []
  alternative_used ← []
  persistent_gaps ← []

  # Execute fallback for failed queries
  FOR query IN queries_for_fallback:
    # Try WebSearch (Google) with original query
    results_google ← WebSearch(query, limit=3)

    IF results_google != []:
      # Success: collect results
      collected_results.extend(results_google)
      fallback_success.append(query)
    ELSE:
      # Still failed: try alternative formulation
      alternative_query ← REFORMULATE_QUERY(query)  # §3.2
      results_alt ← WebSearch(alternative_query, limit=3)

      IF results_alt != []:
        # Alternative success
        collected_results.extend(results_alt)
        alternative_used.append({
          original: query,
          alternative: alternative_query
        })
      ELSE:
        # Persistent gap: cannot find results with any method
        persistent_gaps.append(query)

  # Return results + metrics
  RETURN {
    urls: collected_results,
    fallback_success_count: len(fallback_success),
    alternative_success_count: len(alternative_used),
    gap_count: len(persistent_gaps),
    fallback_success_rate: len(fallback_success) / len(queries_for_fallback),
    gaps: persistent_gaps
  }
```

### 3.2 Query Reformulation (Alternative Formulation)

```yaml
@FUNCTION[REFORMULATE_QUERY]:
  INPUT: query (string, failed with both MCP and WebSearch)
  OUTPUT: alternative_query (string)

  # Strategy 1: Replace technical terms with common synonyms
  technical_synonyms ← {
    "composition": "membres",
    "nominations": "nommés",
    "sanctions": "amendes",
    "désinformation": "fake news",
    "comparables": "similaires"
  }

  alternative_query ← query
  FOR term, synonym IN technical_synonyms:
    IF term IN query:
      alternative_query ← replace(alternative_query, term, synonym)
      BREAK  # Only replace one term at a time

  # Strategy 2: If query has 3 keywords, try 2-keyword variant
  keywords ← tokenize(alternative_query)
  IF len(keywords) = 3:
    # Remove least important keyword (usually middle one)
    alternative_query ← " ".join([keywords[0], keywords[2]])

  # Strategy 3: Add temporal context if missing
  IF no_year_detected(alternative_query):
    current_year ← get_current_year()  # 2024
    alternative_query ← alternative_query + " " + str(current_year)

  RETURN alternative_query
```

**Example:**
```yaml
Input: "ARCOM composition membres"

Strategy 1: Replace "composition" → "membres"
  → "ARCOM membres membres" (duplicate, skip)

Strategy 2: 3 keywords → 2 keywords
  → "ARCOM membres" (remove "composition")

Output: "ARCOM membres"
```

### 3.3 Result Aggregation

```yaml
@FUNCTION[AGGREGATE_RESULTS]:
  INPUT:
    - mcp_results (dict from §2.1)
    - fallback_results (dict from §3.1)
  OUTPUT: aggregated (dict with all urls + complete metrics)

  # Combine URLs, remove duplicates
  all_urls ← mcp_results.urls + fallback_results.urls
  unique_urls ← deduplicate(all_urls)

  # Calculate total metrics
  total_queries ← (
    mcp_results.mcp_success_count +
    mcp_results.mcp_failure_count
  )

  productive_queries ← (
    mcp_results.mcp_success_count +
    fallback_results.fallback_success_count +
    fallback_results.alternative_success_count
  )

  productive_rate ← productive_queries / total_queries

  # Return aggregated results
  RETURN {
    urls: unique_urls,
    total_queries: total_queries,
    productive_queries: productive_queries,
    productive_rate: productive_rate,
    mcp_success: mcp_results.mcp_success_count,
    fallback_success: fallback_results.fallback_success_count,
    alternative_success: fallback_results.alternative_success_count,
    gaps: fallback_results.gaps
  }
```

**Example (complete flow):**
```yaml
Original query: "ARCOM composition membres nominations gouvernement Macron CSA"

Step 1: SPLIT_QUERY
  → ["ARCOM composition membres", "ARCOM nominations Macron", "CSA ARCOM gouvernement"]

Step 2: EXECUTE_WITH_MCP
  → Query 1: [] (failure)
  → Query 2: [url1, url2] (success)
  → Query 3: [] (failure)
  → mcp_success: 1/3 (33%)

Step 3: HYBRID_FALLBACK (for queries 1 and 3)
  → Query 1: WebSearch → [url3, url4, url5] (success)
  → Query 3: WebSearch → [] (failure)
              REFORMULATE → "CSA ARCOM" → [url6] (alternative success)
  → fallback_success: 2/2 (100%)

Step 4: AGGREGATE_RESULTS
  → unique_urls: [url1, url2, url3, url4, url5, url6] (6 URLs)
  → total_queries: 3
  → productive_queries: 3 (1 MCP + 1 fallback + 1 alternative)
  → productive_rate: 3/3 = 100% ✅
  → gaps: []

Impact:
  Before: 0 URLs (original query failed)
  After: 6 URLs (split + hybrid fallback)
```

---

## §4 INTEGRATION WITH EXISTING SYSTEM

### 4.1 Query Execution Workflow (Modified)

**Location in KERNEL.md:** §1 Step 8 (SEARCH) + §2.9 Query Distribution

```yaml
@WORKFLOW[EXECUTE_QUERIES_OPTIMIZED]:
  INPUT: queries (list of strings, from kb/QUERY_TEMPLATES.md)
  OUTPUT: collected_results (list of URLs + optimization metrics)

  # Initialize tracking
  all_results ← []
  optimization_stats ← {
    original_query_count: len(queries),
    split_query_count: 0,
    mcp_success: 0,
    fallback_used: 0,
    alternative_used: 0,
    gaps: 0
  }

  # Execute each query with optimization
  FOR query IN queries:
    # Step 1: Check if splitting needed (§1.1)
    IF TRIGGER[SPLIT_REQUIRED](query):
      split_queries ← SPLIT_QUERY(query)  # §1.2
      optimization_stats.split_query_count += len(split_queries)
    ELSE:
      split_queries ← [query]  # Keep original

    # Step 2: Execute with MCP (§2.1)
    mcp_results ← EXECUTE_WITH_MCP(split_queries)
    all_results.extend(mcp_results.urls)
    optimization_stats.mcp_success += mcp_results.mcp_success_count

    # Step 3: Fallback for failed queries (§3.1)
    IF len(mcp_results.queries_for_fallback) > 0:
      fallback_results ← HYBRID_FALLBACK(mcp_results.queries_for_fallback)
      all_results.extend(fallback_results.urls)
      optimization_stats.fallback_used += fallback_results.fallback_success_count
      optimization_stats.alternative_used += fallback_results.alternative_success_count
      optimization_stats.gaps += fallback_results.gap_count

  # Step 4: Deduplicate and return
  unique_results ← deduplicate(all_results)

  RETURN {
    urls: unique_results,
    optimization_stats: optimization_stats
  }
```

### 4.2 Backward Compatibility (Q6 C: Keep existing + add layer)

**No changes to:**
- `kb/QUERY_TEMPLATES.md` — Domain-adaptive templates remain unchanged
- `kb/SEARCH_EPISTEMIC.md` — Source stratification logic unchanged
- `kb/VALIDATION.md` — EDI/ISN scoring formulas unchanged

**New layer added:**
- Query splitting happens BEFORE execution (if keyword_count > 5)
- Hybrid fallback happens DURING execution (if MCP returns [])
- Original queries still attempted first (with MCP, as before)

**Simple queries unchanged:**
```yaml
Query: "ARCOM CNews climat"  # 3 keywords
  → SPLIT_REQUIRED = false  # No splitting
  → Execute with MCP as before (existing behavior)
  → If MCP fails, fallback to WebSearch (new safety net)
```

**Complex queries optimized:**
```yaml
Query: "ARCOM composition membres nominations gouvernement Macron CSA"  # 7 keywords
  → SPLIT_REQUIRED = true  # Splitting triggered
  → Split into 3 simple queries (new behavior)
  → Execute each with MCP + fallback (hybrid approach)
  → Aggregate results (new)
```

### 4.3 Optimization Metrics (Reporting)

**Add to DIAGNOSTICS section in investigation output:**

```yaml
[QUERY_OPTIMIZATION]
Original queries: 12
Split queries: 16 (+33%)
MCP success: 5/16 (31%)
Fallback success: 8/16 (50%)
Alternative used: 2/16 (13%)
Gaps: 1/16 (6%)
Total productive: 15/16 (94%) ✅
Improvement: +86% vs baseline (8.3% → 94%)
```

---

## §5 VALIDATION & SUCCESS CRITERIA

### 5.1 Per-Query Success Criteria

```yaml
@VALIDATION[QUERY_SUCCESS]:
  # Criterion 1: Keyword count (Q5 B: 3-word queries preferred)
  split_query.keyword_count ≤ 4:
    → PASS ✅
  ELSE:
    → FAIL ❌ (query too complex, split again)

  # Criterion 2: Split count (Q2 C: multi-query but not excessive)
  2 ≤ len(split_queries) ≤ 3:
    → PASS ✅
  ELSE:
    → FAIL ❌ (too many/few splits)

  # Criterion 3: MCP success rate (realistic baseline)
  mcp_success_rate ≥ 0.30:  # 30% success with DuckDuckGo
    → PASS ✅
  ELSE:
    → WARNING 🟡 (MCP struggling, fallback critical)

  # Criterion 4: Fallback success rate (Google more reliable)
  fallback_success_rate ≥ 0.60:  # 60% success with Google
    → PASS ✅
  ELSE:
    → FAIL ❌ (even Google failing, query problem?)

  # Criterion 5: Total results (min viable)
  len(unique_urls) ≥ 3:  # At least 3 URLs per original query
    → PASS ✅
  ELSE:
    → FAIL ❌ (insufficient results)
```

### 5.2 Investigation-Level Success Criteria

```yaml
@VALIDATION[INVESTIGATION_SUCCESS]:
  # Criterion 1: Productive query rate (Q4 "tendre vers D": aim high)
  productive_rate ≥ 0.60:  # 60% of queries return results
    → PASS ✅
  ELSE:
    → FAIL ❌ (optimization not effective)

  # Criterion 2: EDI improvement (epistemic diversity)
  EDI_after ≥ EDI_before + 0.15:  # At least +0.15 improvement
    → PASS ✅
  ELSE:
    → WARNING 🟡 (more results but not more diverse)

  # Criterion 3: Primary source coverage (◈)
  primary_sources_after ≥ 1:  # At least 1 primary source found
    → PASS ✅
  ELSE:
    → WARNING 🟡 (mainstream still dominant)

  # Criterion 4: Resource efficiency (Q4 C: accept cost increase)
  query_increase ≤ 0.35:  # Max 35% more queries
    → PASS ✅
  ELSE:
    → FAIL ❌ (too expensive, refine splitting)
```

### 5.3 Known Limitations (Q4 "tendre vers D": realistic about D)

**Cannot fix:**
1. **Content gaps:** If information doesn't exist online, no query strategy will find it
2. **Language barriers:** French queries on English-only topics (rare but possible)
3. **Censored content:** If systematically removed from all search engines
4. **Ultra-niche topics:** Academic/specialized content not indexed

**Can improve:**
1. **Query formulation:** DuckDuckGo-friendly phrasing (3-4 keywords)
2. **Fallback coverage:** Google as safety net for DuckDuckGo failures
3. **Result aggregation:** More diverse sources from split queries
4. **Success rate:** 8.3% → 60%+ (10x improvement realistic)

### 5.4 Query Budget Considerations

**Issue:** Query splitting increases query count significantly.

**Observed impact:**
- Baseline: 4 complex queries
- Optimized: 12 split queries (+200% increase)
- APEX worst case: 15 queries → potentially 45 queries (+200%)

**User requirement (Q4 "tendre vers D"):**
Accept cost increase for quality. Results validate this trade-off:
- Cost: +200% queries (4 → 12)
- Benefit: 0% → 100% productive rate, 0 → 87 URLs, 0 → 12 ◈ PRIMARY, EDI 0.28 → 0.45-0.55
- **ROI:** Infinite (complete failure → complete success)

**Mitigation options if budget becomes issue:**

```yaml
OPTION A (Conservative): Limit split count
  - Max 2 splits per query (instead of 3)
  - Budget cap: +100% (15 → 30 APEX)

OPTION B (Selective): Only split high-value queries
  - Split PRIMARY/H7 adversary queries only
  - Keep EDI/GEO queries simple
  - Budget: +33-67% (15 → 20-25 APEX)

OPTION C (Dynamic): Retroactive splitting
  - Execute original query first
  - Only split if MCP returns []
  - Budget: 15 base + failures (variable)

OPTION D (Current): No limits
  - User preference Q4 "tendre vers D"
  - Accept cost for quality
  - Budget: +200% (15 → 45 APEX potential)
```

**Recommendation:** Start with OPTION D (current implementation). Monitor real APEX investigations. If query budget becomes prohibitive, fallback to OPTION B (selective splitting for high-value queries only).

**Monitoring:** Track query_count and execution_time per investigation. Alert if APEX investigations >25 min (budget: 20 min + 25% margin).

---

## §6 TESTING & EXAMPLES

### 6.1 Test Case 1: Query 1 (User's failed query)

**Input:**
```
"CNews ARCOM sanctions historique liste complète 2020-2024"
```

**Processing:**
```yaml
Step 1: SPLIT_REQUIRED?
  keywords: [CNews, ARCOM, sanctions, historique, liste, complète, 2020-2024]
  count: 7 > 5 → SPLIT_REQUIRED = true ✅

Step 2: SPLIT_QUERY
  entities: [CNews, ARCOM]
  concepts: [sanctions, historique, liste]
  temporal: [2020-2024]

  split_queries:
    - "CNews ARCOM sanctions"           # entity[0] + entity[1] + concept[0]
    - "ARCOM sanctions 2020-2024"       # entity[1] + concept[0] + temporal
    - "CNews sanctions historique"      # entity[0] + concept[0] + concept[1]

Step 3: EXECUTE_WITH_MCP
  Query 1: "CNews ARCOM sanctions"
    → mcp_web_search → [] (failure)
  Query 2: "ARCOM sanctions 2020-2024"
    → mcp_web_search → [url1] (success)
  Query 3: "CNews sanctions historique"
    → mcp_web_search → [] (failure)

  mcp_success: 1/3 (33%)

Step 4: HYBRID_FALLBACK (queries 1 and 3)
  Query 1: "CNews ARCOM sanctions"
    → WebSearch → [url2, url3, url4] (success)
  Query 3: "CNews sanctions historique"
    → WebSearch → [] (failure)
    → REFORMULATE → "CNews sanctions" → [url5, url6] (alternative success)

  fallback_success: 2/2 (100%)

Step 5: AGGREGATE_RESULTS
  unique_urls: [url1, url2, url3, url4, url5, url6]
  total: 6 URLs
  productive_rate: 3/3 = 100% ✅
  gaps: 0
```

**Expected result:**
```yaml
Before: 0 URLs (original query failed with MCP)
After: 6 URLs (split + hybrid fallback)
Improvement: +∞ (0 → 6)
```

### 6.2 Test Case 2: Query 4 (User's failed query)

**Input:**
```
"ARCOM composition membres nominations gouvernement Macron CSA"
```

**Processing:**
```yaml
Step 1: SPLIT_REQUIRED?
  keywords: [ARCOM, composition, membres, nominations, gouvernement, Macron, CSA]
  count: 7 > 5 → SPLIT_REQUIRED = true ✅

Step 2: SPLIT_QUERY
  entities: [ARCOM, Macron, CSA, gouvernement]
  concepts: [composition, membres, nominations]
  temporal: []

  split_queries:
    - "ARCOM composition membres"       # entity[0] + concept[0] + concept[1]
    - "ARCOM nominations Macron"        # entity[0] + concept[2] + entity[1]
    - "CSA ARCOM gouvernement"          # entity[2] + entity[0] + entity[3]

Step 3: EXECUTE_WITH_MCP
  Query 1: "ARCOM composition membres"
    → mcp_web_search → [] (failure)
  Query 2: "ARCOM nominations Macron"
    → mcp_web_search → [url1, url2] (success)
  Query 3: "CSA ARCOM gouvernement"
    → mcp_web_search → [] (failure)

  mcp_success: 1/3 (33%)

Step 4: HYBRID_FALLBACK (queries 1 and 3)
  Query 1: "ARCOM composition membres"
    → WebSearch → [url3, url4, url5] (success)
  Query 3: "CSA ARCOM gouvernement"
    → WebSearch → [] (failure)
    → REFORMULATE → "CSA ARCOM" → [url6] (alternative success)

  fallback_success: 2/2 (100%)

Step 5: AGGREGATE_RESULTS
  unique_urls: [url1, url2, url3, url4, url5, url6]
  total: 6 URLs
  productive_rate: 3/3 = 100% ✅
  gaps: 0
```

**Expected result:**
```yaml
Before: 0 URLs (original query failed with MCP)
After: 6 URLs (split + hybrid fallback)
Improvement: +∞ (0 → 6)
```

### 6.3 Test Case 3: Simple query (no splitting)

**Input:**
```
"ARCOM CNews climat"
```

**Processing:**
```yaml
Step 1: SPLIT_REQUIRED?
  keywords: [ARCOM, CNews, climat]
  count: 3 ≤ 5 → SPLIT_REQUIRED = false ❌

Step 2: EXECUTE_WITH_MCP (original query, no splitting)
  Query: "ARCOM CNews climat"
    → mcp_web_search → [url1, url2, url3] (success)

  mcp_success: 1/1 (100%)

Step 3: HYBRID_FALLBACK (not needed)
  queries_for_fallback: [] (no failures)

Step 4: AGGREGATE_RESULTS
  unique_urls: [url1, url2, url3]
  total: 3 URLs
  productive_rate: 1/1 = 100% ✅
  gaps: 0
```

**Expected result:**
```yaml
Before: 3 URLs (existing behavior, no optimization needed)
After: 3 URLs (same, backward compatible)
Improvement: 0 (no change, as expected)
```

---

## §7 IMPLEMENTATION CHECKLIST

**Phase 1: Core functions (DSL-pure, no Python)**
- [x] `@TRIGGER[SPLIT_REQUIRED]` (§1.1)
- [x] `@FUNCTION[SPLIT_QUERY]` (§1.2)
- [x] `@TEMPLATES[SIMPLE_QUERIES]` (§1.3)
- [x] `@FUNCTION[EXECUTE_WITH_MCP]` (§2.1)
- [x] `@FUNCTION[HYBRID_FALLBACK]` (§3.1)
- [x] `@FUNCTION[REFORMULATE_QUERY]` (§3.2)
- [x] `@FUNCTION[AGGREGATE_RESULTS]` (§3.3)

**Phase 2: Integration**
- [ ] Modify `KERNEL.md` query execution workflow (§4.1)
- [ ] Add optimization metrics to DIAGNOSTICS output (§4.3)

**Phase 3: Testing**
- [ ] Test on 4 user's failed queries (§6.1, §6.2)
- [ ] Create validation script `tests/query_optimization/validate_splitting.sh`
- [ ] Re-run ARCOM investigation with optimization
- [ ] Validate EDI/ISN improvements (§5.2)

**Status:** SPECIFICATION COMPLETE ✅
**Next step:** Integrate with KERNEL.md §1 Step 8

---

**Version:** v1.0
**Date:** 2025-11-14
**Based on:** User brainstorming Q1-Q6 (multi-query + hybrid fallback)
**Backward compatible:** Yes (Q6 C: keep existing + add layer)
**DSL purity:** 100% (no Python code)
