# Truth Engine v8.0 Validation Test

**Date:** 2025-11-12
**Version:** v8.0
**Objective:** Validate 9 improvements from post-POC evaluation

---

## Test Specification

### Test Subject
**Topic:** "France unemployment 7.4% October 2024"

**Expected Triggers:**
- Content type: Political ✅
- Controversy ≥6 (employment statistics) ✅
- Ξ likely ≥7 (ICEBERG pattern - categories A-E hidden) ✅
- Should trigger: Deep search, WOLF threshold adjustment

---

## Validation Criteria (9 Checks)

### ✅ **Check 1: Confidence Contextualized**
**Location:** Part 2 [DIAGNOSTICS]

**Expected:**
```
Conf: XX% LEVEL sur pattern_name (data uncertainty: YY%)
```

**NOT:** Single `Conf: XX% LEVEL` without breakdown

**Validation:**
- [ ] Pattern confidence separated from data uncertainty
- [ ] Format: "sur {pattern_name}" present
- [ ] Both percentages shown

---

### ✅ **Check 2: Factor Best Estimate + Bounds**
**Location:** Pattern ICEBERG calculation (if triggered)

**Expected:**
```
Factor: X.X [min-max] validated
  Best: X.X (Source: ◈/◉ highest reliability)
  Validated bounds: [min-max] (N methodologies ≥0.70)
  Full alternatives: [min-max] (all N methodologies)
  Data uncertainty: XX% (divergence ×Y)
```

**NOT:** Single `Factor: 3.37` without bounds

**Validation:**
- [ ] Best estimate shown with source attribution
- [ ] Validated bounds present (≥0.70 reliability)
- [ ] Full alternatives shown
- [ ] Data uncertainty percentage calculated

---

### ✅ **Check 3: Triggered Deep Search**
**Location:** Part 2 [SOURCES] or investigation notes

**Expected (if Ξ≥7 OR ♦≥6):**
```
Deep searches triggered:
- OFFICIAL_DOCS: "rapports parlementaires" + "Cour des Comptes"
- PRIMARY_INVESTIGATIVE: leak/whistleblower searches
- EU_COMPARATIVE: Eurostat comparisons (if France-specific)
```

**Validation:**
- [ ] Check if Ξ≥7 (should trigger)
- [ ] Deep searches noted in [SOURCES] or execution logs
- [ ] At least 1 deep search category executed

---

### ✅ **Check 4: Dynamic WOLF Threshold**
**Location:** Part 2 [WOLVES] or Part 3

**Expected:**
```
Threshold adjusted: base X - controversy Y - complexity Z = {adjusted}
(e.g., Political base:8, controversy:7, complexity:6 → 8-2-1 = 5)
```

**NOT:** Fixed threshold "8 for political"

**Validation:**
- [ ] Threshold calculation shown with controversy/complexity factors
- [ ] Adjusted threshold ≠ base (8 for political)
- [ ] Formula visible in output

---

### ✅ **Check 5: Partial WOLF Output**
**Location:** Part 3 — WOLF

**Expected (if wolves found ≥ 70% threshold but < 100%):**
```
## Part 3 — WOLF (Partial: X/Y actors)

**Status**: Investigation I0 identified X actors (Z% of threshold)
**Actors Identified**: [list]
**Iteration Guidance**: [I1 recommendations]
**Partial Analysis**: [limited cui bono]
```

**NOT:** "(WOLF not applicable)" when 6/8 found

**Validation:**
- [ ] Check wolves_found vs threshold_adjusted
- [ ] If ≥70%: Partial WOLF present (not "not applicable")
- [ ] Iteration guidance included

---

### ✅ **Check 6: Autonomous I1 Preview in REFLECTION**
**Location:** Part 2 [REFLECTION]

**Expected:**
```
ITERATION_RECOMMENDATION:
  STATUS: ITERATION RECOMMENDED 🔄
  PRIORITY_GAPS: [EDI, ◈, WOLF, etc.]
  ESTIMATED_QUERIES: 10 auto-generated

AUTONOMOUS_I1_PREVIEW:
  Auto-queries would target:
    1. [EDI geo 3 queries] - EU Eurostat, regional, OECD
    2. [◈ PRIMARY 2 queries] - rapports, investigations
    ...
  Execute: "I1 AUTO logs/YYYY-MM-DD_HH-MM-SS_subject.md"
```

**Validation:**
- [ ] REFLECTION section present
- [ ] ITERATION_RECOMMENDATION with status
- [ ] AUTONOMOUS_I1_PREVIEW with query breakdown
- [ ] Execute command provided

---

### ✅ **Check 7: GAP_ANALYSIS in REFLECTION**
**Location:** Part 2 [REFLECTION]

**Expected:**
```
GAP_ANALYSIS:
  EDI_gap: target - current = gap (XX% below)
  Sources_gap: ◈ target:X current:Y gap:Z
  Wolves_gap: threshold:X found:Y gap:Z
  Pattern_gaps: [list unconfirmed patterns with signals]
  Depth_gap: L6 counter-narrative {reached|NOT reached}
```

**Validation:**
- [ ] All 5 gap dimensions present
- [ ] Numerical gaps calculated
- [ ] Clear indication of what's missing

---

### ✅ **Check 8: DIAGNOSTICS Format Updated**
**Location:** Part 2 [DIAGNOSTICS] first line

**Expected:**
```
IVF:X.X ISN:Y.Y Conf:ZZ% LEVEL sur pattern_name (data uncertainty: WW%)
```

**NOT:** Old format `IVF:X.X ISN:Y.Y Conf:ZZ%` without contextualization

**Validation:**
- [ ] "sur pattern_name" present in Conf output
- [ ] Data uncertainty percentage in parentheses
- [ ] LEVEL (VERY_HIGH|HIGH|MODERATE|LOW|VERY_LOW) present

---

### ✅ **Check 9: REFLECTION Always Present**
**Location:** Part 2 (after [SOURCES], [PATTERNS], [WOLVES])

**Expected:**
```
[REFLECTION] (ALWAYS PRESENT - Iteration guidance v8.0):
INVESTIGATION_STATUS: [...]
GAP_ANALYSIS: [...]
ITERATION_RECOMMENDATION: [...]
META_NOTES: [...]
```

**Validation:**
- [ ] [REFLECTION] section exists
- [ ] At minimum: INVESTIGATION_STATUS, GAP_ANALYSIS, ITERATION_RECOMMENDATION
- [ ] Not omitted (should be ALWAYS PRESENT per v8.0 spec)

---

## Test Execution

**Command:**
```bash
# Simple test (I0 only - check new outputs)
Investigation: "France unemployment 7.4% October 2024"
Protocol: Truth Engine v8.0 full
Output: logs/2025-11-12_v8_validation_test.md
```

**Expected Outcome:**
- All 9 checks ✅ PASS
- New v8.0 features visible in output
- No regressions from v7.17

---

## Success Criteria

**PASS:** ≥8/9 checks validated ✅
**PARTIAL:** 6-7/9 checks validated ⚠️
**FAIL:** <6/9 checks validated ❌

**Critical Checks (must pass):**
1. Confidence Contextualized (Check 1)
6. REFLECTION with I1 Preview (Check 6)
9. REFLECTION Always Present (Check 9)

If any critical check fails → v8.0 implementation incomplete.

---

## Post-Test Actions

IF PASS (≥8/9):
1. Update system.md version: v7.17 → v8.0
2. Document validated features in CHANGELOG
3. Optional: Execute I1 AUTO to test iteration workflow

IF PARTIAL (6-7/9):
1. Fix failing checks
2. Re-run validation
3. Document known limitations

IF FAIL (<6/9):
1. Debug failing components
2. Rollback if critical features broken
3. Re-implement with corrections
