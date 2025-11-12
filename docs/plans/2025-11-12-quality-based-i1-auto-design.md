# Design: Quality-Based I1 AUTO Triggering (v8.2)

**Date:** 2025-11-12
**Version:** v8.2
**Status:** Approved for implementation

---

## Problem Statement

**v8.1 limitation**: I1 AUTO triggers only on **quantity** (queries_total < minimum), not on **quality**.

**Real-world failure (Mercosur investigation)**:
- Executed 15/12 queries ✅ (quantity met)
- But EDI 0.35 (target 0.70 ❌), 0 ◈ PRIMARY (target 3 ❌)
- I1 AUTO did NOT trigger → Investigation flagged PARTIAL manually
- Result: Investigation INSUFFICIENT despite meeting query minimum

**Root cause**: Protocol doesn't detect when queries execute but return poor quality results (MCP dysfunction, bad keywords, geo/lang gaps).

---

## Solution Overview

**v8.2 adds quality-based triggering**: Dual trigger system (QUANTITY OR QUALITY).

```yaml
QUERY_ENFORCEMENT v8.2:

  # TRIGGER 1: Quantity-based (existing v8.1, preserved)
  IF queries_total < minimum_for_complexity:
    → I1 AUTO triggers

  # TRIGGER 2: Quality-based (NEW v8.2)
  ELIF quality_gaps_detected(EDI, ◈_PRIMARY):
    → Gap severity analysis (MINOR/MODERATE/SEVERE)
    → I1 AUTO triggers if MODERATE or SEVERE
```

**Key design decisions** (from brainstorming):
1. **Metrics**: EDI + ◈ PRIMARY (Option B) — Balance composite diversity + critical investigative sources
2. **Allocation**: Root cause analysis (Option C) — Fix causes (◈, geo, L6), not symptoms
3. **Thresholds**: Severity-based 3-tier (Option C) — MINOR accept, MODERATE I1, SEVERE I1+warning

---

## Architecture

### 1. Quality Gap Detection

```yaml
# After I0 investigation completes, calculate gaps:

EDI_gap = EDI_target - EDI_actual
PRIMARY_gap = PRIMARY_target - PRIMARY_actual

# Targets by complexity:
SIMPLE:  EDI ≥0.30, ◈ ≥1
MEDIUM:  EDI ≥0.50, ◈ ≥2
COMPLEX: EDI ≥0.70, ◈ ≥3
APEX:    EDI ≥0.80, ◈ ≥3

# Severity classification (3-tier):

IF (EDI_gap < 0.10 AND PRIMARY_gap ≤ 1):
  → severity = MINOR
  → action = ACCEPT_I0
  → flag = "ACCEPTABLE - minor gaps (EDI -{X}%, ◈ -{Y})"
  → NO I1 AUTO

ELIF (0.10 ≤ EDI_gap ≤ 0.28) OR (PRIMARY_gap == 2):
  → severity = MODERATE
  → action = I1_AUTO
  → flag = "I0 PARTIAL - I1 AUTO launching (moderate gaps)"
  → queries_I1 = 8

ELIF (EDI_gap > 0.28) OR (PRIMARY_gap == 3 AND EDI_actual < 0.40):
  → severity = SEVERE
  → action = I1_AUTO + I2_WARNING
  → flag = "I0 INSUFFICIENT - I1 AUTO launching (I2 or APEX may be needed)"
  → queries_I1 = 10
```

**Concrete examples**:

| Scenario | EDI | ◈ PRIMARY | Gaps | Severity | Action |
|----------|-----|-----------|------|----------|--------|
| Nearly OK | 0.68 | 2/3 | EDI -0.02 (3%), ◈ -1 | MINOR | Accept I0 ✅ |
| Mediocre | 0.50 | 1/3 | EDI -0.20 (29%), ◈ -2 | MODERATE | I1 AUTO (8q) ⚠️ |
| Mercosur | 0.35 | 0/3 | EDI -0.35 (50%), ◈ -3 | SEVERE | I1 AUTO (10q) + warning ❌ |

### 2. Root Cause Analysis (Generic)

**Simple gap detection** (no over-engineering):

```yaml
gaps = []

IF ◈_PRIMARY < target:
  gaps.append("◈_PRIMARY", missing=target-actual)

IF geo_diversity < (target - 0.15):
  gaps.append("geo_diversity")

IF L6_counter_narrative == MISSING AND controversy ≥ 6:
  gaps.append("L6_counter_narrative")

# Generic allocation:
IF severity == MODERATE:
  queries_I1 = 8
ELIF severity == SEVERE:
  queries_I1 = 10

# Split queries equally across detected gaps:
queries_per_gap = queries_I1 / len(gaps)

# LLM generates queries focusing on each gap type:
# - ◈_PRIMARY: "investigative journalism [subject]", "academic research [subject]"
# - geo_diversity: "[subject] + regional sources", "[subject] + non-Western perspectives"
# - L6_counter_narrative: "[subject] opposition", "[subject] criticism alternative"
```

**Key principle**: Fix causes (◈, geo, L6), not symptoms (EDI). EDI improves automatically when root causes are addressed.

**Example (Mercosur SEVERE)**:
- Gaps detected: [◈_PRIMARY, geo_diversity, L6_counter_narrative] (3 gaps)
- queries_I1 = 10 (SEVERE)
- Split: 3-3-4 queries per gap
- LLM generates domain-adaptive queries using QUERY_TEMPLATES.md + domain knowledge

### 3. Interaction with Existing v8.1 Logic

```yaml
# Quantity and quality triggers are OR logic:

IF queries_total < minimum:
  → I1 AUTO triggers (existing v8.1 logic)
  → Skip quality assessment (quantity failure is blocking)

ELIF quality_gaps_detected():  # NEW v8.2
  → Severity analysis (MINOR/MODERATE/SEVERE)
  → I1 AUTO if MODERATE or SEVERE
  → Root cause analysis + query allocation

ELIF current_iteration ≥ I2:
  → FAIL (existing v8.1 I2 cap logic)
  → Flag INVESTIGATION INSUFFICIENT
```

**Backward compatibility**: v8.1 quantity logic fully preserved. v8.2 adds quality layer on top.

---

## Implementation Details

### File: system.md

**Location**: Lines 79-150 (extends existing QUERY_ENFORCEMENT block)

**Changes**:

1. **Lines 79-100**: Preserve existing v8.1 QUERY_ENFORCEMENT (quantity-based + I2 cap)
2. **Lines 101-150**: Add new QUALITY_ENFORCEMENT block (v8.2)

**New QUALITY_ENFORCEMENT block**:

```yaml
**QUALITY_ENFORCEMENT (v8.2 - quality-based I1 AUTO):**

# Execute AFTER I0 completes, IF queries_total ≥ minimum (quantity OK but quality check needed)

IF queries_total ≥ minimum_for_complexity AND current_iteration == I0:

  # Step 1: Calculate gaps
  EDI_target = {SIMPLE: 0.30, MEDIUM: 0.50, COMPLEX: 0.70, APEX: 0.80}[complexity]
  PRIMARY_target = {SIMPLE: 1, MEDIUM: 2, COMPLEX: 3, APEX: 3}[complexity]

  EDI_gap = EDI_target - EDI_actual
  PRIMARY_gap = PRIMARY_target - PRIMARY_actual

  # Step 2: Severity analysis
  IF (EDI_gap < 0.10 AND PRIMARY_gap ≤ 1):
    → severity = MINOR
    → STATUS: **I0 ACCEPTABLE** ✅
    → FLAG: "Minor gaps (EDI -{EDI_gap:.2f}, ◈ -{PRIMARY_gap}) within tolerance"
    → NO I1 AUTO trigger

  ELIF (0.10 ≤ EDI_gap ≤ 0.28) OR (PRIMARY_gap == 2):
    → severity = MODERATE
    → STATUS: **I0 PARTIAL** ⚠️
    → FLAG: "Moderate quality gaps detected - I1 AUTO launching"
    → queries_I1 = 8
    → TRIGGER I1 AUTO with root cause analysis

  ELIF (EDI_gap > 0.28) OR (PRIMARY_gap == 3 AND EDI_actual < 0.40):
    → severity = SEVERE
    → STATUS: **I0 INSUFFICIENT** ❌
    → FLAG: "Severe quality gaps detected - I1 AUTO launching (I2 or APEX reclassification may be needed)"
    → WARNING: "Investigation gaps severe - I1 may not fully close gaps, I2 iteration likely"
    → queries_I1 = 10
    → TRIGGER I1 AUTO with extended root cause analysis

  # Step 3: Root cause analysis (if I1 AUTO triggers)
  IF severity IN [MODERATE, SEVERE]:

    gaps = []

    IF PRIMARY_actual < PRIMARY_target:
      gaps.append("◈_PRIMARY_missing", count=PRIMARY_gap)

    IF geo_diversity < (geo_diversity_target - 0.15):
      gaps.append("geo_diversity_low")

    IF L6_counter_narrative == MISSING AND controversy ≥ 6:
      gaps.append("L6_counter_narrative_missing")

    # Generic query allocation (split equally across gaps):
    queries_per_gap = queries_I1 / len(gaps)

    # Generate I1 queries focusing on detected gaps:
    # - ◈_PRIMARY: Investigative journalism, academic research, whistleblower sources
    # - geo_diversity: Regional sources, non-Western perspectives, local press
    # - L6_counter_narrative: Opposition voices, counter-hegemonic sources, dissidents

    → OUTPUT I0 with I1 AUTO preview showing:
       * Detected gaps (severity, metrics)
       * Root causes identified
       * I1 query allocation plan (N queries per gap type)
       * Expected I1 gains (EDI +X, ◈ +Y, etc.)
```

### Version Update

**File**: system.md lines 1, 4

```yaml
Line 1: TRUTH ENGINE v8.2 (was v8.1)
Line 4: {"v":"8.2"} (was {"v":"8.1"})
```

---

## Testing Plan

### Test Case 1: Mercosur Scenario (SEVERE gap)

**Input**:
- Complexity: COMPLEX (target EDI 0.70, ◈ 3)
- I0 results: 15 queries, EDI 0.35, ◈ PRIMARY 0
- Gaps: EDI -0.35 (50%), ◈ -3 (100%)

**Expected behavior**:
- Severity: SEVERE ✅
- I1 AUTO triggers with 10 queries ✅
- Gaps detected: [◈_PRIMARY, geo_diversity, L6_counter_narrative]
- Query allocation: 3-3-4 split
- Warning: "I2 or APEX may be needed" ✅

### Test Case 2: Nearly OK (MINOR gap)

**Input**:
- Complexity: COMPLEX (target EDI 0.70, ◈ 3)
- I0 results: 12 queries, EDI 0.68, ◈ PRIMARY 2
- Gaps: EDI -0.02 (3%), ◈ -1

**Expected behavior**:
- Severity: MINOR ✅
- Accept I0, NO I1 AUTO ✅
- Flag: "ACCEPTABLE - minor gaps (EDI -0.02, ◈ -1)" ✅

### Test Case 3: Moderate (I1 AUTO 8 queries)

**Input**:
- Complexity: MEDIUM (target EDI 0.50, ◈ 2)
- I0 results: 8 queries, EDI 0.35, ◈ PRIMARY 0
- Gaps: EDI -0.15 (30%), ◈ -2

**Expected behavior**:
- Severity: MODERATE ✅
- I1 AUTO triggers with 8 queries ✅
- Gaps detected: [◈_PRIMARY, geo_diversity]
- Query allocation: 4-4 split

---

## Benefits

1. **Fixes Mercosur failure**: I1 AUTO would have triggered automatically (EDI 0.35, ◈ 0 = SEVERE)
2. **Generic**: Works for any subject (no domain-specific engineering)
3. **Pragmatic**: 3-tier severity prevents over-triggering (MINOR gaps accepted)
4. **Transparent**: Root cause analysis shows WHY I1 triggers, WHAT it will fix
5. **Backward compatible**: v8.1 quantity logic fully preserved

---

## Breaking Changes

None. v8.2 is additive (extends v8.1, doesn't replace).

**Migration**: Existing investigations continue working. v8.2 quality checks activate automatically if quantity minimum met.

---

## Expected Impact

**Mercosur-like scenarios** (queries execute but low quality):
- v8.1: Manual PARTIAL flag, user must request I1 manually
- v8.2: Automatic I1 AUTO trigger, gap-filling without user intervention

**Quality improvement**:
- EDI +0.20-0.35 typical gain from I1 AUTO (MODERATE→COMPLEX target)
- ◈ PRIMARY +2-3 sources from targeted investigative queries
- Investigation success rate: +40-60% (estimated)

**Edge cases handled**:
- MCP dysfunction (86.7% query failure like Mercosur) → I1 AUTO retries with alternate keywords
- Geographic bias → I1 AUTO explicitly seeks regional sources
- L6 gaps → I1 AUTO queries opposition/counter-hegemonic sources

---

## Implementation Checklist

- [ ] Write design document to docs/plans/
- [ ] Update system.md lines 101-150 (add QUALITY_ENFORCEMENT block)
- [ ] Update system.md lines 1, 4 (version v8.2)
- [ ] Commit changes with message "Truth Engine v8.2: Quality-based I1 AUTO triggering"
- [ ] Test with Mercosur scenario (manual simulation or real re-run)
- [ ] Update USER_GUIDE.md (document v8.2 quality enforcement)

---

**Design validated:** 2025-11-12
**Next step:** Implementation in system.md
