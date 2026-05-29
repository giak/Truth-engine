# Manual Query Splitting Test
**Date:** 2025-11-14
**Purpose:** Validate query splitting strategy on user's 4 failed queries from ARCOM investigation

**Method:** Manual split according to kb/QUERY_OPTIMIZATION.md §1.2, then test with MCP web-search

---

## Test Case 1: Query 1

**Original query (FAILED):**
```
"CNews ARCOM sanctions historique liste complète 2020-2024"
```

**Analysis:**
- Keywords: [CNews, ARCOM, sanctions, historique, liste, complète, 2020-2024]
- Count: 7 > 5 → SPLIT_REQUIRED = true ✅
- Entities: [CNews, ARCOM]
- Concepts: [sanctions, historique, liste]
- Temporal: [2020-2024]

**Split queries (according to §1.2):**
1. `"CNews ARCOM sanctions"` — 3 keywords (entity[0] + entity[1] + concept[0])
2. `"ARCOM sanctions 2020-2024"` — 3 keywords (entity[1] + concept[0] + temporal)
3. `"CNews sanctions historique"` — 3 keywords (entity[0] + concept[0] + concept[1])

**Expected result:**
- Query 1: Should find CNews ARCOM sanctions overview
- Query 2: Should find ARCOM sanctions timeline 2020-2024
- Query 3: Should find CNews sanctions history

**Test execution:** Will test with MCP below

---

## Test Case 2: Query 2

**Original query (FAILED):**
```
"ARCOM sanctions TF1 LCI BFM comparables désinformation 2024"
```

**Analysis:**
- Keywords: [ARCOM, sanctions, TF1, LCI, BFM, comparables, désinformation, 2024]
- Count: 8 > 5 → SPLIT_REQUIRED = true ✅
- Entities: [ARCOM, TF1, LCI, BFM]
- Concepts: [sanctions, comparables, désinformation]
- Temporal: [2024]

**Split queries (according to §1.2):**
1. `"ARCOM TF1 sanctions"` — 3 keywords (entity[0] + entity[1] + concept[0])
2. `"ARCOM LCI BFM"` — 3 keywords (entity[0] + entity[2] + entity[3])
3. `"ARCOM désinformation 2024"` — 3 keywords (entity[0] + concept[2] + temporal)

**Expected result:**
- Query 1: Should find ARCOM TF1 sanctions cases
- Query 2: Should find ARCOM LCI BFM sanctions/decisions
- Query 3: Should find ARCOM désinformation cases in 2024

**Test execution:** Will test with MCP below

---

## Test Case 3: Query 3

**Original query (FAILED):**
```
"CNews défense amende ARCOM climat liberté expression censure"
```

**Analysis:**
- Keywords: [CNews, défense, amende, ARCOM, climat, liberté, expression, censure]
- Count: 8 > 5 → SPLIT_REQUIRED = true ✅
- Entities: [CNews, ARCOM]
- Concepts: [défense, amende, climat, liberté, expression, censure]
- Temporal: []

**Split queries (according to §1.2):**
1. `"CNews ARCOM amende"` — 3 keywords (entity[0] + entity[1] + concept[1])
2. `"ARCOM climat censure"` — 3 keywords (entity[1] + concept[2] + concept[5])
3. `"CNews défense expression"` — 3 keywords (entity[0] + concept[0] + concept[4])

**Expected result:**
- Query 1: Should find CNews ARCOM fine/amende overview
- Query 2: Should find ARCOM climate censorship debates
- Query 3: Should find CNews defense arguments (free expression)

**Test execution:** Will test with MCP below

---

## Test Case 4: Query 4

**Original query (FAILED):**
```
"ARCOM composition membres nominations gouvernement Macron CSA"
```

**Analysis:**
- Keywords: [ARCOM, composition, membres, nominations, gouvernement, Macron, CSA]
- Count: 7 > 5 → SPLIT_REQUIRED = true ✅
- Entities: [ARCOM, Macron, CSA, gouvernement]
- Concepts: [composition, membres, nominations]
- Temporal: []

**Split queries (according to §1.2):**
1. `"ARCOM composition membres"` — 3 keywords (entity[0] + concept[0] + concept[1])
2. `"ARCOM nominations Macron"` — 3 keywords (entity[0] + concept[2] + entity[1])
3. `"CSA ARCOM gouvernement"` — 3 keywords (entity[2] + entity[0] + entity[3])

**Expected result:**
- Query 1: Should find ARCOM composition/members structure
- Query 2: Should find ARCOM nominations by Macron government
- Query 3: Should find CSA to ARCOM transition (government role)

**Test execution:** Will test with MCP below

---

## Manual Testing with MCP (mcp__web-search__search)

Testing all 12 split queries with MCP to validate splitting effectiveness.

### Results will be documented here after testing:

**Test Case 1 splits:**
- [ ] `"CNews ARCOM sanctions"` → MCP result: ?
- [ ] `"ARCOM sanctions 2020-2024"` → MCP result: ?
- [ ] `"CNews sanctions historique"` → MCP result: ?

**Test Case 2 splits:**
- [ ] `"ARCOM TF1 sanctions"` → MCP result: ?
- [ ] `"ARCOM LCI BFM"` → MCP result: ?
- [ ] `"ARCOM désinformation 2024"` → MCP result: ?

**Test Case 3 splits:**
- [ ] `"CNews ARCOM amende"` → MCP result: ?
- [ ] `"ARCOM climat censure"` → MCP result: ?
- [ ] `"CNews défense expression"` → MCP result: ?

**Test Case 4 splits:**
- [ ] `"ARCOM composition membres"` → MCP result: ?
- [ ] `"ARCOM nominations Macron"` → MCP result: ?
- [ ] `"CSA ARCOM gouvernement"` → MCP result: ?

---

## Success Criteria

**Per-query:**
- Keyword count ≤4 ✅ (all split queries have 3 keywords)
- Split count 2-3 ✅ (all test cases have 3 split queries)

**Overall:**
- MCP success rate ≥30% (≥4/12 queries return results)
- Total results ≥12 URLs (≥1 per query on average)
- Improvement vs original: 4 queries × 0 URLs = 0 → target ≥12 URLs

**Next step:** Execute MCP tests, document results, analyze success rate
