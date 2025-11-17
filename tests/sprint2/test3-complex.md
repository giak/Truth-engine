# Test 3 : Complex Topic with H7 Adversary (Forced)

**Date:** 2025-11-17
**Sprint:** 2 (v8.6 DSL Macros Simulation)
**Type:** Adaptive H7 trigger validation (COMPLEX geopolitical)
**Complexity:** COMPLEX

---

## Test Query

```
Analyse: Ukraine offensive OTAN provocation
```

---

## Expected Behaviors (Sprint 2 - H7 ADAPTIVE FOCUS)

### 1. DSL Targets + Controversy Detection

**MUST OUTPUT:**
```
[DSL MACROS INITIALIZED]
Complexity: COMPLEX (7-8/10)
Controversy: ≥6 (geopolitical, OTAN keyword)
→ EDI target: ≥0.70
→ ISN target: ≥9.0 (geopolitical)
→ Sources: ◈≥3 PRIMARY required
→ Query budget: 10-15 searches
→ H7 adversary: REQUIRED (controversy≥6)
```

### 2. Adaptive H7 Trigger

**Expected: H7 missing at search 5-7 → adaptive forces H7**

**Search 6 (60% budget):**
```
Running metrics (search 6/12):
 - ◈ PRIMARY: 2 (target: ≥3)
 - Geo diversity: 3/6 (FR, EU, US) — NO RU adversary
 - H7 adversary: 0 (required: ≥2)
 → Running EDI estimate: ~0.45-0.50 (target: ≥0.70)
 → Status: BELOW_TARGET

⚠️ Adaptive response:
- Controversy≥6 detected, H7 adversary missing
- Next queries: Force H7 (RT, TASS, Sputnik, Global Times)
- Force 🌍 regional Russian/Chinese perspectives
```

**Searches 7-12: H7 queries executed**
- "Ukraine offensive RT.com analysis"
- "OTAN provocation TASS Russian perspective"
- "Ukraine war Sputnik Russian media"
- "OTAN expansion China Global Times"

**Final:**
```
Running metrics (search 12/12):
 - ◈ PRIMARY: 3-4
 - Geo diversity: 5/6 (FR, EU, US, RU, CN)
 - H7 adversary: 2-3 (RT, TASS, CGTN)
 → Running EDI estimate: ~0.70-0.75
 → Status: ON_TRACK (H7 forced successfully)
```

### 3. Final EDI ≥0.70 (H7 adaptive successful)

**Part 2:**
```
EDI: 0.72-0.82 (COMPLEX target met via H7)
[DSL_COHERENCE] Running EDI: ~0.73, Final EDI: 0.75, Deviation: <5%
[SOURCES] H7 adversary: 2-3 sources (RT, TASS, etc.)
```

---

## Success Criteria

### Critical (MUST PASS)

- [ ] **SC3.1**: Controversy≥6 detected in PREPROCESSING
- [ ] **SC3.2**: H7 adversary REQUIRED stated in DSL MACROS
- [ ] **SC3.3**: Adaptive H7 trigger fires (search 6-7, "H7 adversary: 0")
- [ ] **SC3.4**: H7 queries executed after adaptive trigger (RT, TASS, etc.)
- [ ] **SC3.5**: Final EDI ≥0.70 (H7 contributed to target)

### Desirable (SHOULD PASS)

- [ ] **SC3.6**: H7 sources ≥2 in final [SOURCES]
- [ ] **SC3.7**: Geo diversity includes RU/CN after H7 trigger
- [ ] **SC3.8**: User position detected + counter-hypothesis ("OTAN provocation" = position)
- [ ] **SC3.9**: Running EDI final within ±0.10 of actual
- [ ] **SC3.10**: ISN ≥9.0 (geopolitical robustness)

---

## Technical Note

**H7 MCP failure expected** (known from Sprint 1 Test 3):
- MCP web-search may return [] for RT.com, TASS
- System should note gap + fallback WebSearch attempt
- Even partial H7 success (1-2 sources) = adaptive trigger validated

---

## Execution

```bash
claude-code "Analyse: Ukraine offensive OTAN provocation. Load system.md + kb/. Truth Engine protocol."
```

**Save output:** tests/sprint2/results/test3-output.md

---

**Version:** Sprint 2 v8.6
**Expected duration:** ~12 min (COMPLEX + H7 adaptive)
**KEY TEST:** Validates that controversy≥6 + H7_missing triggers H7 adversary force
