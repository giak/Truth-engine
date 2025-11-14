# Bug Fix: Query Splitting Not Activating

**Date:** 2025-11-14
**Version:** Truth Engine v8.3.1 (hotfix)
**Bug ID:** Query splitting trigger not activating despite queries >5 keywords
**Severity:** CRITICAL
**Status:** FIXED ✅

---

## Summary

**Problem:** Query splitting logic defined in kb/QUERY_OPTIMIZATION.md was not being invoked during investigations. All queries executed with original keyword count, causing MCP (DuckDuckGo) failures on complex queries.

**Root Cause:** system.md line 310-311 contained **aspirational documentation** ("IF query keyword_count > 5 → SPLIT") instead of **procedural execution instructions**.

**Fix:** Transformed execution workflow into explicit 3-step procedure with clear WHEN/WHAT/HOW instructions.

---

## Evidence of Bug

### Investigation #1: ARCOM CNews amende
**File:** logs/2025-11-14_15-53-46_arcom_cnews_amende.md

**Symptom (line 421):**
```yaml
Split queries: 0 (aucune query >5 keywords nécessitant split)
```

**But actual queries executed (line 428-434):**
```
- "rapports parlementaires régulation médias désinformation climatique France ARCOM" (8 keywords)
- "CNews Bolloré réponse amende ARCOM désinformation climatique communiqué officiel" (9 keywords)
- "climatosceptiques liberté expression critique régulation ARCOM censure médias" (8 keywords)
- "historique amendes ARCOM CSA médias sanctions désinformation France" (8 keywords)
```

**Impact:**
- MCP success: 25% (2/8 queries)
- 6 complex queries failed, required WebSearch fallback
- 0 PRIMARY sources found (◈ gap)
- EDI: 0.20/0.70 (-71%)

### Investigation #2: PLF-PLFSS 2025
**File:** logs/2025-11-14_PLF-PLFSS-2025-etudes-impact.md

**Similar symptom:** "0 split queries" despite complex queries present

---

## Root Cause Analysis (Systematic Debugging)

### Phase 1: Investigation

**Data flow traced:**
1. Query templates in kb/QUERY_TEMPLATES.md generate queries
2. Template placeholders {subject} filled with user input
3. Result: queries with 7-10 keywords
4. Expected: Splitting logic should activate (kb/QUERY_OPTIMIZATION.md §1.1)
5. Actual: Queries executed AS-IS, no splitting

**Key finding:** system.md line 310-311 said:
```yaml
- Query optimization @KB[QUERY_OPTIMIZATION]:
  * IF query keyword_count > 5 → SPLIT into 2-3 simple queries
```

This is **descriptive** (explains what optimization does) not **procedural** (tells Claude WHEN/HOW to invoke it).

### Phase 2: Pattern Analysis

**Working examples:** kb/QUERY_OPTIMIZATION.md §1.1 defines @TRIGGER[SPLIT_REQUIRED] correctly

**Broken pattern:** system.md doesn't explicitly invoke @TRIGGER or @FUNCTION

**Difference identified:**
- KB file: "Here's HOW to split (IF invoked)"
- system.md: "Optimization involves splitting" (but no invocation instruction)

### Phase 3: Hypothesis

**Hypothesis:** Claude reads system.md as documentation of features, not as step-by-step execution checklist.

**Test:** Check for explicit "BEFORE executing query" instruction → NOT FOUND

**Confirmation:** Hypothesis validated - no procedural trigger in execution workflow

### Phase 4: Implementation

**Fix applied:** Transform line 308-316 from aspirational to procedural

---

## The Fix

### Before (v8.3 - BROKEN)

```yaml
**2. EXECUTION** (with v8.3 query optimization):
   - Load @KB[QUERY_TEMPLATES§1-3]
   - Query optimization @KB[QUERY_OPTIMIZATION]:
     * IF query keyword_count > 5 → SPLIT into 2-3 simple queries
     * Execute with MCP (DuckDuckGo) first
     * IF MCP returns [] → Fallback WebSearch (Google)
     * Aggregate results, deduplicate
     * Track: mcp_success, fallback_used, productive_rate
```

**Problem:** "IF query keyword_count > 5 → SPLIT" is embedded in bullet point, not executed

---

### After (v8.3.1 - FIXED)

```yaml
**2. EXECUTION** (with v8.3 query optimization):
   - Load @KB[QUERY_TEMPLATES§1-3]
   - FOR EACH query generated, apply optimization (@KB[QUERY_OPTIMIZATION]):

     **STEP 1: Check splitting requirement** (@KB[QUERY_OPTIMIZATION§1.1])
       - Count keywords in query (exclude stopwords: le, la, les, de, du, des...)
       - IF keyword_count > 5 → SPLIT_REQUIRED = true
       - ELSE → SPLIT_REQUIRED = false

     **STEP 2: Split if required** (@KB[QUERY_OPTIMIZATION§1.2])
       - IF SPLIT_REQUIRED = true:
         → Invoke @FUNCTION[SPLIT_QUERY] from @KB[QUERY_OPTIMIZATION§1.2]
         → Replace original query with 2-3 split queries (3-4 keywords each)
         → Track: split_count += 1
       - ELSE:
         → Keep original query unchanged

     **STEP 3: Execute with hybrid fallback** (@KB[QUERY_OPTIMIZATION§2])
       - Try MCP (DuckDuckGo) first for each query
       - IF MCP returns [] → Fallback WebSearch (Google)
       - Track: mcp_success, fallback_used per query

   - Aggregate results from all queries (original + split)
   - Deduplicate URLs across queries
   - Track total: original_queries, split_queries, productive_rate
```

**Fix details:**
1. **"FOR EACH query"** - Makes it explicit WHEN to apply optimization
2. **"STEP 1/2/3"** - Sequential procedural checklist
3. **"Count keywords (exclude stopwords: ...)"** - Explicit HOW to count
4. **"Invoke @FUNCTION[SPLIT_QUERY]"** - Direct function call instruction
5. **"Track: split_count += 1"** - Explicit tracking instruction

---

## Expected Impact After Fix

### Functional Improvements

**Query splitting activation:**
- Before: 0 splits (bug)
- After: 2-3 splits per complex query (expected)

**MCP success rate:**
- Before: 25% (complex queries fail)
- After: 60-80% (simple split queries succeed)

**PRIMARY sources (◈):**
- Before: 0-2 PRIMARY (complex queries miss official sites)
- After: 8-12 PRIMARY (split queries discover official docs)

**EDI improvement:**
- Before: 0.20-0.37 (poor diversity)
- After: 0.45-0.55 (target met)

### Performance Impact

**Query count increase:**
- Baseline: 13 queries
- After split: ~20-25 queries (+54-92%)
- Acceptable per kb/QUERY_OPTIMIZATION.md §5.4 (user chose OPTION D: quality over cost)

**Execution time:**
- Minimal increase (split queries run in parallel batches)
- MCP success improvement reduces fallback delays
- Net result: Similar or faster total time

---

## Validation Plan

### Test Case 1: ARCOM Re-investigation

**Input:** Same subject as logs/2025-11-14_15-53-46_arcom_cnews_amende.md

**Expected results:**
- [QUERY_OPTIMIZATION] section shows: "Split queries: 8-12 (from 4-6 original)"
- MCP success: ≥60% (vs 25% baseline)
- PRIMARY sources: ≥10 (vs 0 baseline)
- EDI: ≥0.45 (vs 0.20 baseline)

**Pass criteria:**
- ✅ split_count > 0
- ✅ EDI improvement ≥0.20
- ✅ PRIMARY ≥8

### Test Case 2: Simple Query Validation

**Input:** "ARCOM CNews climat" (3 keywords)

**Expected results:**
- No splitting (keyword_count ≤ 5)
- Query executed AS-IS
- [QUERY_OPTIMIZATION] reports: "0 splits (queries simple)"

**Pass criteria:**
- ✅ No unnecessary splitting
- ✅ Backward compatibility preserved

---

## Files Modified

1. **system.md** (line 308-333)
   - Replaced aspirational bullet points with procedural STEP 1/2/3
   - Added explicit stopwords list
   - Added FOR EACH query loop structure
   - Added tracking instructions

2. **tests/query_optimization/test_splitting_bug.md** (created)
   - Documented failing test case
   - Evidence of bug with keyword counts

3. **tests/query_optimization/BUG_FIX_splitting_activation.md** (this file)
   - Complete root cause analysis
   - Before/after comparison
   - Validation plan

---

## Commit Message

```
fix: Query splitting not activating (v8.3.1 hotfix)

CRITICAL BUG: Query splitting logic not invoked despite queries >5 keywords

Root cause: system.md line 310-311 was aspirational documentation
("IF query keyword_count > 5 → SPLIT") instead of procedural
execution instructions.

Fix: Transform EXECUTION step 2 into explicit 3-step procedure:
  STEP 1: Check splitting requirement (count keywords, IF >5 true)
  STEP 2: Split if required (invoke @FUNCTION[SPLIT_QUERY])
  STEP 3: Execute with hybrid fallback (MCP → WebSearch)

Evidence:
- Investigation logs show 0 splits despite 8-10 keyword queries
- MCP success 25% (should be 60-80% with splitting)
- EDI 0.20/0.70 (PRIMARY sources missed)

Expected improvement:
- Split activation: 0 → 8-12 per investigation
- MCP success: 25% → 60-80%
- PRIMARY sources: 0 → 8-12
- EDI: +0.20-0.30 improvement

Files modified:
- system.md (line 308-333): Procedural workflow
- tests/query_optimization/test_splitting_bug.md: Test case
- tests/query_optimization/BUG_FIX_splitting_activation.md: Documentation

Validation: Re-run ARCOM investigation, verify split_count > 0

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

---

## Status

**Implementation:** ✅ COMPLETE
**Testing:** ⏳ PENDING (re-run ARCOM investigation)
**Documentation:** ✅ COMPLETE

**Next step:** Execute validation test case to confirm fix works

---

**Version:** v8.3.1 hotfix
**Date:** 2025-11-14
**Type:** Critical bug fix (query splitting activation)
