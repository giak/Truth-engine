# Query Splitting Bug - Test Case

**Date:** 2025-11-14
**Bug:** Query splitting NOT activating despite queries >5 keywords
**Status:** FAILING (before fix)

## Test Input

**Query 1:**
```
"ARCOM composition membres nominations gouvernement Macron CSA"
```

**Keyword count:** 7
- ARCOM (entity)
- composition (concept)
- membres (concept)
- nominations (concept)
- gouvernement (concept)
- Macron (entity)
- CSA (entity)

**Expected behavior:**
```yaml
SPLIT_REQUIRED: true (7 > 5)
Split into 2-3 queries:
  1. "ARCOM composition membres"
  2. "ARCOM nominations Macron"
  3. "CSA gouvernement membres"
```

**Actual behavior (v8.3 before fix):**
```yaml
SPLIT_REQUIRED: false (incorrectly reported as "0 queries >5 keywords")
Query executed AS-IS with 7 keywords
Result: MCP fails (DuckDuckGo can't handle complex query)
```

## Test Validation Criteria

✅ PASS if:
1. Query is detected as having >5 keywords
2. SPLIT_REQUIRED trigger activates
3. Query is split into 2-3 simple queries (3-4 keywords each)
4. [QUERY_OPTIMIZATION] section reports: "Split queries: 2-3 (from 1 original)"
5. MCP success rate improves (or WebSearch fallback used correctly)

❌ FAIL if:
- Query executed with 7 keywords AS-IS
- [QUERY_OPTIMIZATION] reports: "Split queries: 0"
- No splitting logic visible in execution

## Evidence of Failure

**Investigation:** logs/2025-11-14_15-53-46_arcom_cnews_amende.md
**Line 421:** "Split queries: 0 (aucune query >5 keywords nécessitant split)"
**Line 428-434:** Lists 6 queries with 7-10 keywords that should have been split

**Root cause:** system.md line 310-311 is aspirational documentation, not procedural execution instructions.

---

**Version:** Test case v1.0 (FAILING)
**Next:** Apply fix to system.md, rerun test, validate PASS
