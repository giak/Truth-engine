# Test 1 : Simple Topic (Baseline DSL Macros)

**Date:** 2025-11-17
**Sprint:** 2 (v8.6 DSL Macros Simulation)
**Type:** DSL awareness baseline (SIMPLE complexity)
**Complexity:** SIMPLE

---

## Test Query

```
Analyse: PIB France 2024
```

---

## Expected Behaviors (Sprint 2)

### 1. DSL Targets in PREPROCESSING (NEW v8.6)

**MUST OUTPUT:**
```
[DSL MACROS INITIALIZED]
Complexity: SIMPLE (2-3/10)
→ EDI target: ≥0.30
→ ISN target: ≥6.0 (economic topic)
→ Sources: ◈≥1 PRIMARY required
→ Query budget: 5-7 searches

EDI formula internalized: tracking geo, ◈◉○ ratio, topic perspectives
```

### 2. Running Metrics During Search (NEW v8.6)

**MUST OUTPUT (every 2 searches):**
```
Running metrics (search 2/7):
 - ◈ PRIMARY: 1 (target: ≥1)
 - Geo diversity: 1/6 (FR)
 - Source types: ◈50% ◉50% ○0%
 → Running EDI estimate: ~0.25-0.35 (target: ≥0.30)
 → Status: ON_TRACK or BELOW_TARGET

Running metrics (search 4/7):
 - ◈ PRIMARY: 1
 - Geo diversity: 2/6 (FR, EU)
 → Running EDI estimate: ~0.30-0.40
 → Status: ON_TRACK
```

### 3. DSL Coherence Check (NEW v8.6)

**Part 2 [DIAGNOSTICS] MUST INCLUDE:**
```
[DSL_COHERENCE] Running EDI: ~0.35, Final EDI: 0.32-0.38, Deviation: <20%
Status: ACCURATE (or INACCURATE_CALIBRATION_NEEDED if >20%)
```

### 4. No Regression (Sprint 1 features preserved)

- Anti-Sycophancy: No user position detected (neutral query) → standard investigation
- Fact-Checking: PIB value cited with ◈ source (INSEE)
- Confidence: ≤95%

---

## Success Criteria

### Critical (MUST PASS)

- [ ] **SC1.1**: PREPROCESSING outputs "[DSL MACROS INITIALIZED]" with EDI target 0.30
- [ ] **SC1.2**: Running metrics logged ≥2 times (search 2, search 4)
- [ ] **SC1.3**: Final EDI ≥0.30 (baseline target met)
- [ ] **SC1.4**: DSL coherence deviation ≤20% (accurate simulation)
- [ ] **SC1.5**: NO regression: Anti-Sycophancy + Fact-Checking working

### Desirable (SHOULD PASS)

- [ ] **SC1.6**: Running EDI estimate within ±0.05 of final EDI
- [ ] **SC1.7**: ◈ PRIMARY found (INSEE for PIB)
- [ ] **SC1.8**: Status "ON_TRACK" by search 4

---

## Execution

```bash
# Launch investigation with v8.6 (Sprint 2)
claude-code "Analyse: PIB France 2024. Load system.md + kb/. Truth Engine protocol."
```

**Save output:** tests/sprint2/results/test1-output.md

---

**Version:** Sprint 2 v8.6
**Expected duration:** ~5 min (SIMPLE topic)
