# Test 2 : Medium Topic with Adaptive Trigger

**Date:** 2025-11-17
**Sprint:** 2 (v8.6 DSL Macros Simulation)
**Type:** Adaptive search behavior validation (MEDIUM complexity)
**Complexity:** MEDIUM

---

## Test Query

```
Analyse: Chômage 7.4% France
```

---

## Expected Behaviors (Sprint 2 - ADAPTIVE FOCUS)

### 1. DSL Targets in PREPROCESSING

**MUST OUTPUT:**
```
[DSL MACROS INITIALIZED]
Complexity: MEDIUM (5-6/10)
→ EDI target: ≥0.50
→ ISN target: ≥7.0
→ Sources: ◈≥2 PRIMARY required
→ Query budget: 7-10 searches
```

### 2. Running Metrics + Adaptive Trigger (CRITICAL)

**Expected sequence:**

**Search 2:**
```
Running metrics (search 2/10):
 - ◈ PRIMARY: 1 (target: ≥2)
 - Geo diversity: 1/6 (FR)
 - Source types: ◈33% ◉67% ○0%
 → Running EDI estimate: ~0.25-0.30 (target: ≥0.50)
 → Status: BELOW_TARGET
```

**Search 4-5 (50% budget reached):**
```
Running metrics (search 5/10):
 - ◈ PRIMARY: 1 (still below target ≥2)
 - Geo diversity: 2/6 (FR, EU)
 → Running EDI estimate: ~0.35-0.40 (target: ≥0.50)
 → Status: ADAPTIVE_NEEDED

⚠️ Running EDI 0.38 < target 0.50 at search 5.
Adaptive response:
- Next queries: Force ◈ PRIMARY templates (official docs, leaks)
- Force 🔥⟐̅ dissident perspective (missing)
- Force 🌍 regional diversity (non-FR sources)
```

**Search 7-10: DIFFERENT queries (adaptive adjustment visible)**
- More ◈ PRIMARY focus (e.g., "DEFM statistics official data", "unemployment France Eurostat")
- 🔥⟐̅ dissident (e.g., "chômage manipulation statistics France")
- 🌍 regional (e.g., "unemployment France international comparison")

**Final:**
```
Running metrics (search 10/10):
 - ◈ PRIMARY: 2-3
 - Geo diversity: 3-4/6 (FR, EU, INTL)
 → Running EDI estimate: ~0.50-0.60
 → Status: ON_TRACK (target reached via adaptive)
```

### 3. Final EDI ≥0.50 (adaptive successful)

**Part 2:**
```
EDI: 0.52-0.62 (MEDIUM target met)
[DSL_COHERENCE] Running EDI: ~0.55, Final EDI: 0.54, Deviation: <5%
Status: ACCURATE
```

---

## Success Criteria

### Critical (MUST PASS)

- [ ] **SC2.1**: Adaptive trigger fires at search 5 (50% budget, running_EDI < 0.50)
- [ ] **SC2.2**: Adaptive response visible ("⚠️ Running EDI X < target 0.50")
- [ ] **SC2.3**: Queries 6-10 DIFFERENT from queries 1-5 (observable strategy change)
- [ ] **SC2.4**: Final EDI ≥0.50 (adaptive corrected the gap)
- [ ] **SC2.5**: DSL coherence ≤20% deviation

### Desirable (SHOULD PASS)

- [ ] **SC2.6**: ◈ PRIMARY increased from 1 → 2-3 after adaptive trigger
- [ ] **SC2.7**: 🔥⟐̅ dissident perspective added after adaptive
- [ ] **SC2.8**: Geo diversity improved (FR only → FR+EU+INTL)
- [ ] **SC2.9**: Running EDI estimate final within ±0.10 of actual
- [ ] **SC2.10**: User position detected ("7.4% cache" = manipulation claim)

---

## Execution

```bash
claude-code "Analyse: Chômage 7.4% France. Load system.md + kb/. Truth Engine protocol."
```

**Save output:** tests/sprint2/results/test2-output.md

---

**Version:** Sprint 2 v8.6
**Expected duration:** ~8 min (MEDIUM + adaptive adjustments)
**KEY TEST:** This validates that LLM actually CHANGES behavior mid-investigation based on running metrics
