# Sprint 2 Test 1 Summary — SIMPLE Topic DSL Macros Baseline

**Date:** 2025-11-17
**Test:** PIB France 2024 (SIMPLE complexity)
**Sprint:** 2 (v8.6 DSL Macros Simulation)
**Tester:** Claude Code Agent
**Output:** tests/sprint2/results/test1-output.md

---

## Critical Criteria Results

### ❌ SC1.1: DSL MACROS INITIALIZED — FAIL

**Expected:**
```
[DSL MACROS INITIALIZED]
Complexity: SIMPLE (2-3/10)
→ EDI target: ≥0.30
→ ISN target: ≥6.0 (economic topic)
→ Sources: ◈≥1 PRIMARY required
→ Query budget: 5-7 searches

EDI formula internalized: tracking geo, ◈◉○ ratio, topic perspectives
```

**Actual:** NOT PRESENT in output

**Reason:** v8.6 DSL Macros feature defined in system.md lines 325-360 (PREPROCESSING step 0.5) but NOT executed by LLM during investigation. Feature exists in specification but not implemented in runtime behavior.

**Status:** ❌ FAIL

---

### ❌ SC1.2: Running Metrics Logged ≥2 Times — FAIL

**Expected:**
```
Running metrics (search 2/7):
 - ◈ PRIMARY: 1 (target: ≥1)
 - Geo diversity: 1/6 (FR)
 - Source types: ◈50% ◉50% ○0%
 → Running EDI estimate: ~0.25-0.35 (target: ≥0.30)
 → Status: ON_TRACK or BELOW_TARGET
```

**Actual:** NOT PRESENT in output

**Reason:** v8.6 Running Metrics feature defined in system.md lines 418-446 (PREPROCESSING step 2.5) but NOT executed during web searches. LLM did not output running estimates after searches 2, 4, etc.

**Status:** ❌ FAIL

---

### ✅ SC1.3: Final EDI ≥0.30 — PASS

**Expected:** Final EDI ≥0.30 (SIMPLE baseline target)

**Actual:** EDI = 0.34 (documented in Part 2 [SOURCES])

**Calculation verified:**
- geo_diversity: 0.33 × 0.25 = 0.08
- source_type: 0.60 × 0.20 = 0.12
- topic_diversity: 0.55 × 0.20 = 0.11
- temporal_diversity: 0.40 × 0.15 = 0.06
- platform_diversity: 0.30 × 0.10 = 0.03
- language_diversity: 0.40 × 0.10 = 0.04
- EDI_raw: 0.44 - penalty 0.10 (◈<3) = **0.34**

**Status:** ✅ PASS (0.34 ≥ 0.30, +13.3% surplus)

---

### ❌ SC1.4: DSL Coherence Deviation ≤20% — FAIL

**Expected:**
```
[DSL_COHERENCE] Running EDI: ~0.35, Final EDI: 0.32-0.38, Deviation: <20%
Status: ACCURATE (or INACCURATE_CALIBRATION_NEEDED if >20%)
```

**Actual:** NOT PRESENT in output

**Reason:** No running EDI estimates logged during investigation → Cannot calculate deviation between running estimates and final EDI. Feature prerequisite (SC1.2 running metrics) not implemented.

**Status:** ❌ FAIL (cannot measure, prerequisite missing)

---

### ✅ SC1.5: No Regression (Anti-Sycophancy + Fact-Checking) — PASS

**Anti-Sycophancy Check:**
- User query: "Analyse: PIB France 2024" (neutral, no user position detected)
- Expected: Standard investigation without position detection
- Actual: ✅ No user position detected, standard multi-perspective investigation executed
- Tri-perspectif present: ⟐🎓 Académique, 🔥⟐̅ Dissident, 🎯 Arbitrage
- 95% symmetric hostility maintained: Critique both official (INSEE révisions opacity) AND dissident (CGT 2613 Mds€ unexplained gap)

**Fact-Checking Check:**
- Expected: PIB value cited with ◈ PRIMARY source (INSEE)
- Actual: ✅ "PIB français s'établit à **2 919,9 milliards d'euros en 2024** (◈ INSEE)"
- Confidence: 92% MODERATE (≤95% ceiling respected)
- "Je ne sais pas" capability demonstrated: "Écart CGT non expliqué... Je ne sais pas quelle méthodologie CGT utilise"

**Status:** ✅ PASS (both v8.5 features working correctly)

---

## Overall Test Result

### Critical Criteria: 2/5 PASS (40%)

- ❌ SC1.1: DSL MACROS INITIALIZED — **FAIL**
- ❌ SC1.2: Running Metrics Logged — **FAIL**
- ✅ SC1.3: Final EDI ≥0.30 — **PASS**
- ❌ SC1.4: DSL Coherence — **FAIL**
- ✅ SC1.5: No Regression — **PASS**

### Desirable Criteria (Reference)

- ⚠️ SC1.6: Running EDI estimate within ±0.05 — **N/A** (running estimates not logged)
- ✅ SC1.7: ◈ PRIMARY found (INSEE) — **PASS** (2 PRIMARY sources: INSEE, OECD)
- ⚠️ SC1.8: Status "ON_TRACK" by search 4 — **N/A** (status not logged)

---

## Root Cause Analysis

### Problem: v8.6 DSL Macros Features Not Executing

**Defined in system.md but not implemented:**

1. **PREPROCESSING step 0.5** (lines 325-360):
   - DSL MACRO EXPANSION specification exists
   - OUTPUT format defined: "[DSL MACROS INITIALIZED]..."
   - **But:** LLM does not execute this step during preprocessing

2. **PREPROCESSING step 2.5** (lines 418-446):
   - RUNNING METRICS TRACKING specification exists
   - OUTPUT format defined: "Running metrics (search N/budget)..."
   - **But:** LLM does not output metrics during web searches

**Why features not executing:**

- **Specification ≠ Implementation**: system.md contains YAML blocks describing desired behavior, but these are passive instructions, not executable code
- **LLM lacks awareness**: During investigation, LLM follows general Truth Engine protocol but doesn't explicitly reference/execute step 0.5 and 2.5
- **No enforcement mechanism**: No validation check saying "STOP if [DSL MACROS INITIALIZED] not output"

**Required for v8.6:**

1. **Explicit triggers** in system.md:
   - After complexity assessment: "MANDATORY OUTPUT [DSL MACROS INITIALIZED] block"
   - After each web search: "IF search_count % 2 == 0 THEN OUTPUT running metrics"

2. **Enforcement checks**:
   - Post-investigation validation: "IF [DSL MACROS INITIALIZED] not found in output → INVESTIGATION FAILED"
   - Quality gate: "IF running metrics count < 2 → flag INCOMPLETE"

3. **Stronger prompting**:
   - Move DSL Macros from "step 0.5" (optional-sounding) to "MANDATORY PREPROCESSING"
   - Add examples showing exact output format expected

---

## Investigation Quality (Despite DSL Macros Failure)

### Strengths

1. ✅ **Final metrics accurate**: EDI 0.34, ISN 6.8, ◈2 all calculated correctly
2. ✅ **Multi-perspective**: Tri-perspectif maintained (Academic, Dissident, Arbitrage)
3. ✅ **Primary sources**: INSEE, OECD confirmed PIB 2920 Mds€ +1,1%
4. ✅ **Patterns detected**: ICEBERG (PIB net ajusté -94 Mds€ carbone), FRAMING (croissance/décroissance)
5. ✅ **Honest gaps**: "Je ne sais pas" for CGT methodology, missing parliamentary reports
6. ✅ **Hostile epistemology**: Critique both official (INSEE opacity) AND dissident (CGT unexplained gap)

### Weaknesses (v8.6 Specific)

1. ❌ **No preprocessing visibility**: User cannot see EDI target, query budget, formula internalization
2. ❌ **No real-time tracking**: User cannot monitor progress during investigation (running EDI hidden)
3. ❌ **No adaptive triggers**: "IF running_EDI < target at 50% budget" logic never activated (not monitored)
4. ❌ **No coherence validation**: Cannot verify LLM's internal EDI simulation accuracy

---

## Recommendations

### For v8.6 Implementation

**Priority 1 (CRITICAL):**

1. **Add enforcement block** in system.md after complexity assessment:
   ```yaml
   AFTER complexity assessment, BEFORE query execution:
     → MANDATORY OUTPUT (visible, non-silent):
     "[DSL MACROS INITIALIZED]
     Complexity: {SIMPLE|MEDIUM|COMPLEX|APEX} ({score}/10)
     → EDI target: ≥{0.30|0.50|0.70|0.80}
     → ISN target: ≥{domain_specific}
     → Sources: ◈≥{1|2|3|3} PRIMARY required
     → Query budget: {5-7|7-10|10-15|15-20} searches

     EDI formula internalized: tracking geo, ◈◉○ ratio, topic perspectives
     Adaptive trigger: IF running_EDI < {target} at search {N} → force H7/◈"

     IF this block not output → INVESTIGATION FAILS quality gate
   ```

2. **Add running metrics enforcement** after EXECUTION step:
   ```yaml
   AFTER EACH WEB SEARCH:
     search_count += 1

     IF search_count % 2 == 0:  # Every 2 searches
       → MANDATORY OUTPUT (visible):
       "Running metrics (search {search_count}/{budget}):
        - ◈ PRIMARY: {count} (target: {◈_min})
        - Geo diversity: {unique_countries}/6 ({list})
        - Source types: ◈{X}% ◉{Y}% ○{Z}%
        → Running EDI estimate: ~{0.00-1.00} (target: {target_EDI})
        → Status: {ON_TRACK | BELOW_TARGET}"
   ```

3. **Add DSL_COHERENCE check** in Part 2 DIAGNOSTICS (after final EDI calculated):
   ```yaml
   [DSL_COHERENCE]
   Running EDI estimates: [{list all running estimates}]
   Final EDI: {final_calculated}
   Deviation: max(|running - final|) = {deviation} ({pct}%)
   Status: {ACCURATE if ≤20% | INACCURATE_CALIBRATION_NEEDED if >20%}
   ```

**Priority 2 (DESIRABLE):**

4. Add example investigation in system.md showing complete DSL Macros output
5. Create validation script checking [DSL MACROS INITIALIZED] presence in logs/
6. Add REFLECTION note tracking DSL coherence over multiple investigations

### For This Test

**Verdict:** Test 1 Sprint 2 **FAILS** critical requirements (2/5 pass). v8.6 DSL Macros features defined but not implemented in runtime behavior.

**Next steps:**
1. Implement Priority 1 enforcement blocks in system.md
2. Re-run Test 1 with updated system.md
3. Validate running metrics logged ≥2 times
4. Validate DSL coherence deviation ≤20%
5. Only proceed to Test 2 (MEDIUM) when Test 1 passes 5/5 critical criteria

---

**Test Status:** ❌ FAIL (40% pass rate, <80% required)
**Investigation Quality:** ✅ ACCEPTABLE (EDI 0.34, targets met, despite missing v8.6 features)
**Blocker:** DSL Macros specification exists but not executed by LLM during investigation
