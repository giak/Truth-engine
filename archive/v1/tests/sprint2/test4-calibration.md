# Test 4 : Calibration Check (Deviation Detection)

**Date:** 2025-11-17
**Sprint:** 2 (v8.6 DSL Macros Simulation)
**Type:** DSL coherence validation (deviation >20% detection)
**Complexity:** MEDIUM

---

## Test Query

```
Analyse: Pfizer contrats secrets corruption
```

---

## Objective

**NOT to test investigation quality** (that's Sprint 1 Test 4).

**TO TEST:** DSL Coherence Check §6.5 correctly detects inaccurate running estimates.

**Scenario:** If LLM estimates "Running EDI ~0.60" but final EDI = 0.40, deviation = 50% → MUST flag `DSL_CALIBRATION_NEEDED`.

---

## Expected Behaviors

### 1. Standard DSL Macros (baseline)

```
[DSL MACROS INITIALIZED]
Complexity: COMPLEX (7/10)
→ EDI target: ≥0.70
```

### 2. Running Estimates (may be inaccurate)

```
Running metrics (search 6/12):
 → Running EDI estimate: ~0.50-0.65 (LLM's best guess)
```

### 3. DSL Coherence Check (CRITICAL)

**Part 2 [DIAGNOSTICS] MUST INCLUDE:**
```
[DSL_COHERENCE]
Running EDI (last estimate): {X}
Final EDI (validated): {Y}
Deviation: {abs(X-Y)/Y * 100}%

IF deviation ≤20%:
  Status: ACCURATE

IF deviation >20%:
  Status: INACCURATE_CALIBRATION_NEEDED
  ⚠️ DSL macro estimation inaccurate.
  Possible causes:
  - Underestimated source quality (○ counted as ◈)
  - Overestimated geo diversity (duplicates)
  - Topic diversity miscalculated
```

**KEY:** System MUST calculate deviation and flag if >20%, regardless of whether investigation passed or failed.

---

## Success Criteria

### Critical (MUST PASS)

- [ ] **SC4.1**: [DSL_COHERENCE] section present in Part 2
- [ ] **SC4.2**: Deviation calculated: abs(running_EDI_last - final_EDI) / final_EDI
- [ ] **SC4.3**: IF deviation >20% → Status: INACCURATE_CALIBRATION_NEEDED
- [ ] **SC4.4**: IF deviation ≤20% → Status: ACCURATE
- [ ] **SC4.5**: NO EDI penalty applied (coherence check = informational only)

### Desirable (SHOULD PASS)

- [ ] **SC4.6**: Possible causes listed if inaccurate (source quality, geo, topic)
- [ ] **SC4.7**: Investigation remains VALID regardless of calibration status
- [ ] **SC4.8**: Flag appears in DIAGNOSTICS for meta-analysis tracking

---

## Execution

```bash
claude-code "Analyse: Pfizer contrats secrets corruption. Load system.md + kb/. Truth Engine protocol."
```

**Save output:** tests/sprint2/results/test4-output.md

---

## Validation

**Manual check:**
1. Find running_EDI_last in logs (last "Running metrics" before Part 2)
2. Find final_EDI in Part 2 [DIAGNOSTICS]
3. Calculate deviation: abs(running - final) / final
4. Verify system calculated same deviation
5. Verify flag correct: ACCURATE (<20%) or INACCURATE (>20%)

**Note:** We don't care if LLM is accurate or not. We test that the CHECK WORKS.

---

**Version:** Sprint 2 v8.6
**Expected duration:** ~10 min (COMPLEX topic)
**KEY TEST:** Validates §6.5 DSL Coherence Check calculates deviation correctly
