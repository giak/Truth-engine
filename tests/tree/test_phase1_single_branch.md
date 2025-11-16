# Test Phase 1 — Single Branch (Gap Sources Primaires)

**Phase:** 1 — Core Infrastructure
**Objective:** Validate Investigation Tree v1.0 DSL with simplest possible APEX case
**Branch type:** GAP_CRITICAL (gap_primary_sources)
**Complexity:** 9.0 (APEX threshold)

---

## Test Scenario

**Subject:** "Democracy Shield 200M€ EU budget allocation 2025"

**Why APEX complexity ≥9.0:**
- Political domain (⚔≥2)
- EU institutional context (complexity boost)
- Budget allocation (€≥3)
- Timing proximity (recent announcement)
- Expected pattern signals: Κ (cui_bono), Ξ (omission), Ω (inversion)

**I0 Initial State (simulated):**
```yaml
i0_state:
  complexity: 9.0
  EDI: 0.25
  sources:
    total: 5
    stratification:
      ◈_primary: 0      # GAP DETECTED
      ◉_secondary: 2
      ○_tertiary: 3
    ◈_target: 3         # For APEX political ≥3

  patterns_detected:
    - symbol: Κ
      name: CUI_BONO
      score: 7.5
    - symbol: Ξ
      name: ICEBERG_OMISSION
      score: 6.0

  wolves:
    individuals: []     # Not yet identified
    institutions: ["European_Commission", "Resilience_Centre"]

  timing:
    announcement_date: "2025-11-13"
    analysis_date: "2025-11-14"
    proximity_days: 1
```

---

## Expected Behavior

### 1. Trigger Detection — @TRIGGER[TREE_LAUNCH]

**Expected:**
```yaml
tree_triggered: true

triggers_detected:
  - type: GAP_CRITICAL
    reason: "◈_current (0) < ◈_target (3)"
    gap_size: 3

  - type: PATTERN_STRONG
    reason: "Κ score 7.5 ≥ 8.0 threshold"
    pattern: Κ (CUI_BONO)
```

**Validation:**
- ✅ `tree_triggered = true`
- ✅ At least 1 trigger detected
- ✅ GAP_CRITICAL present in triggers

---

### 2. Branch Detection — DETECT_BRANCHES

**Expected candidates (simplified to 1 for Phase 1):**
```yaml
candidates:
  - id: "b1_gap_primary_sources"
    parent: "i0_root"
    type: GAP_CRITICAL
    objective: "Find ◈ PRIMARY independent sources on Democracy Shield 200M€"

    score:
      edi_impact: 0.50        # @F[EDI_IMPACT] for gap_primary_sources
      cui_bono_centrality: 0.0 # Not ACTOR_CENTRAL branch
      priority: 0.25          # @F[BRANCH_PRIORITY] = 0.50×0.5 + 0×0.5

    status: PENDING

    budget:
      queries_executed: 0
      last_pertinent: 0
      consecutive_failures: 0
```

**Validation:**
- ✅ Candidate generated with type GAP_CRITICAL
- ✅ `edi_impact = 0.50` (as per DSL heuristic)
- ✅ `priority` calculated correctly

---

### 3. Branch Selection — BRANCH_SELECTION

**Expected:**
```yaml
selected_branches: ["b1_gap_primary_sources"]
# Only 1 branch for Phase 1 test
```

**Validation:**
- ✅ Branch selected (top priority)
- ✅ `max_branches = 1` for Phase 1

---

### 4. Branch Exploration — @MACRO[EXPLORE_BRANCH]

**Expected queries (simplified sequence):**

```yaml
ITERATION 1:
  query: "Democracy Shield EU primary sources investigative journalism"
  result: Found ◉ The Guardian article
  pertinent: true (criteria B: better source ◉)
  consecutive_failures: 0
  status: EXPLORING

ITERATION 2:
  query: "Democracy Shield 200M budget allocation leak documents"
  result: No relevant results
  pertinent: false
  consecutive_failures: 1
  status: EXPLORING

ITERATION 3:
  query: "EU Resilience Centre funding primary investigation"
  result: Found ◈ Bellingcat investigation
  pertinent: true (criteria A: new facts + B: ◈ PRIMARY)
  consecutive_failures: 0  # Reset
  status: EXPLORING

ITERATION 4:
  query: "von der Leyen Democracy Shield announcement primary analysis"
  result: No new facts
  pertinent: false
  consecutive_failures: 1
  status: EXPLORING

ITERATION 5:
  query: "Democracy Shield whistleblower sources"
  result: No relevant results
  pertinent: false
  consecutive_failures: 2
  status: EXPLORING

ITERATION 6:
  query: "EU 200M budget Democracy Shield leaked memo"
  result: No relevant results
  pertinent: false
  consecutive_failures: 3  # THRESHOLD REACHED
  status: EXHAUSTED  # Branch stops
```

**Final branch state:**
```yaml
branch_b1:
  status: EXHAUSTED

  budget:
    queries_executed: 6
    last_pertinent: 3  # Iteration 3 was last pertinent
    consecutive_failures: 3

  results:
    sources_found: ["◈×1", "◉×1"]
    facts_new:
      - "Bellingcat investigation confirmed 200M allocation"
      - "Resilience Centre budget details (primary source)"
    connections:
      - from: "European_Commission"
        to: "Resilience_Centre"
        relation: "funds"
    gaps_resolved: false  # ◈_current=1, target=3
    edi_contribution: 0.10  # Partial improvement
```

**Validation:**
- ✅ Budget adaptatif works (stops at consecutive_failures ≥3)
- ✅ Pertinence evaluated correctly (A|B|C|D criteria)
- ✅ Branch stops when unproductive
- ✅ Results captured (sources, facts, connections)

---

### 5. Synthesis (simplified for 1 branch)

**Expected:**
```yaml
synthesis:
  concordances: []  # Only 1 branch, no cross-confirmation
  contradictions: []  # Only 1 branch
  gaps_unresolved:
    - gap: "◈_primary_sources"
      target: 3
      achieved: 1
      remaining: 2

  edi_global:
    before: 0.25
    after: 0.35   # Improved but below APEX target 0.80
    improvement: 0.10
    target: 0.80
    gap: 0.45

  i2_decision:
    trigger: false  # EDI 0.35 < threshold 0.50
    reason: "EDI below I2 threshold, gaps unresolved"
```

**Validation:**
- ✅ EDI improvement calculated (+0.10)
- ✅ I2 not triggered (EDI too low)
- ✅ Gaps identified correctly

---

## Success Criteria — Phase 1

```yaml
MINIMUM:
  - tree_triggered: true
  - branch_detected: 1
  - branch_explored: true
  - budget_adaptatif_works: true  # Stops at 3 failures
  - edi_improvement: > 0

TARGET:
  - formulas_correct: @F[EDI_IMPACT], @F[BRANCH_PRIORITY]
  - pertinence_criteria_works: A|B|C|D evaluation
  - branch_lifecycle_complete: PENDING → EXPLORING → EXHAUSTED

VALIDATION_METHOD:
  - Manual inspection of DSL logic
  - Verification @F[] formulas match specification
  - Budget adaptatif behavior confirmed
```

---

## Test Execution

**Method:** DSL specification review (not executable code)

**Files to verify:**
1. [kb/INVESTIGATION_TREE.md](../../kb/INVESTIGATION_TREE.md:1) — §1 DÉCLENCHEMENT
2. [kb/INVESTIGATION_TREE.md](../../kb/INVESTIGATION_TREE.md:1) — §2 SCORING BRANCHES
3. [kb/INVESTIGATION_TREE.md](../../kb/INVESTIGATION_TREE.md:1) — §3 SOUS-AGENT LIFECYCLE
4. [kb/VALIDATION.md](../../kb/VALIDATION.md:1) — §7 BRANCH SCORING

**Verification steps:**
1. Check @TRIGGER[TREE_LAUNCH] logic matches expected triggers
2. Verify @F[EDI_IMPACT](gap_primary_sources) returns 0.50
3. Confirm EXPLORE_BRANCH loop has consecutive_failures ≥3 stop condition
4. Validate pertinence criteria A|B|C|D defined
5. Check synthesis functions reference correct

---

## Next Steps After Phase 1

If Phase 1 passes:
- **Phase 2:** Test multi-branch (3-5 branches parallel)
- **Phase 3:** Test synthesis with concordances/contradictions
- **Phase 4:** Full APEX integration test

If Phase 1 fails:
- Debug DSL heuristics
- Adjust formulas
- Clarify ambiguities in specification

---

**Created:** 2025-11-14
**Version:** Investigation Tree v1.0 — Phase 1 Test
**Status:** Specification ready, awaiting validation
