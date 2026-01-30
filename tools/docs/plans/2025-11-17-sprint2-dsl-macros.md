# Sprint 2 : Truth Engine Optimization — DSL Macros Simulation

**Date:** 2025-11-17
**Version:** v8.6 (Sprint 2 cognitive latency reduction)
**Durée:** 3-4h
**Philosophie:** KISS - Le LLM doit **comprendre** son DSL pendant investigation, pas juste l'appliquer post-hoc

---

## Objectifs Sprint 2

**Problème observé:**

Le LLM utilise un DSL complexe (COGNITIVE_DSL.md: 148 concepts, formulas IVF/ISN/EDI) mais ne le **simule pas** pendant l'investigation:
- **Latence cognitive**: Formulas calculées en Part 2 (post-hoc) au lieu de guider recherche en temps réel
- **DSL orphelin**: 80KB COGNITIVE_DSL.md inventé par LLM mais non internalisé (pas de macro expansion)
- **Opportunités manquées**: LLM pourrait ajuster stratégie search si conscient "running EDI = 0.25" pendant investigation

**Exemple symptomatique:**
```
Investigation actuelle:
1. Web search 1-7 (aveugle, pas de feedback EDI en cours)
2. Part 1 output (pas de mention EDI pendant raisonnement)
3. Part 2: "[DIAGNOSTICS] EDI: 0.35" ← TROP TARD pour ajuster

Sprint 2 target:
1. Web search 1: "◈ PRIMARY found, geo FR+0, topic 1 → running EDI ~0.15"
2. Web search 3: "Still no ◈ adversary → EDI stuck 0.15, need H7"
3. Web search 5: "◈ H7 (RT.com) → geo RU+0.15 → running EDI ~0.40, on track"
```

**Solution minimaliste:**

**DSL Macro Expansion** - Forcer LLM "penser tout haut" formulas clés (IVF/ISN/EDI) PENDANT investigation:
1. **PREPROCESSING**: Après complexity, output "Expected IVF/ISN/EDI targets for this complexity"
2. **DURING SEARCH**: Après chaque web search, output running estimate "◈ count: X, geo diversity: Y, running EDI ~Z"
3. **VALIDATION**: Compare running estimates vs final Part 2 metrics (écart >20% = failure)

**Success Criteria:**
- **Running EDI awareness**: LLM mentionne EDI estimate ≥3 fois pendant investigation (baseline: 0 mentions)
- **Target consciousness**: LLM cite EDI target (0.30/0.50/0.70/0.80) pendant PREPROCESSING (baseline: never)
- **Adaptive search**: IF running EDI < target at search 5/10, LLM ajuste stratégie (exemple: force H7 adversary)
- **0 regression**: EDI/ISN final preserved or improved (no quality loss)

---

## Implémentation 1 : Macro Expansion in PREPROCESSING

### Localisation
**Fichier:** `system.md`
**Section:** "## 🧠 PREPROCESSING" après complexity assessment (ligne ~317-330)
**Timing:** IMMÉDIATEMENT après complexity calculation, AVANT query formulation

### Code Ajouté

```markdown
## 🧠 PREPROCESSING (silent execution)

**0. COMPLEXITY** (0-10 scale, 6 dimensions):
   [... existing complexity calculation ...]
   - Average → SIMPLE(0-3)/MEDIUM(4-6)/COMPLEX(7-8)/APEX(9-10)

**0.5 DSL MACRO EXPANSION (v8.6 - Cognitive Simulation):**

**PURPOSE**: LLM must **simulate** DSL formulas in real-time, not post-hoc.

**STEP 1 - OUTPUT TARGET METRICS:**
```yaml
Complexity: {SIMPLE|MEDIUM|COMPLEX|APEX}
→ EDI target: {0.30|0.50|0.70|0.80}
→ ISN target: {domain-specific, see @KB[SEARCH_EPISTEMIC§10]}
→ Sources minimum: {◈≥1|◈≥2|◈≥3|◈≥3}
→ Query budget: {5-7|7-10|10-15|15-20}
```

**STEP 2 - INTERNALIZE FORMULAS:**
```yaml
EDI formula reminder (from @KB[SEARCH_EPISTEMIC§11]):
  EDI = (geo_diversity×0.25 + source_type×0.20 + topic_diversity×0.20
         + time_diversity×0.15 + platform×0.10 + language×0.10)

  → As I search, I will track:
    - geo_diversity: {FR, EU, US, RU, CN, ...} → max 6 unique = 1.0
    - source_type: ◈◉○ ratio → target ◈≥40% for MEDIUM+
    - topic_diversity: Perspectives ⟐ vs 🔥⟐̅ vs 🌍 vs 🎓
```

**STEP 3 - SET ADAPTIVE FLAG:**
```yaml
IF running_EDI < target_EDI at search_count ≥ 50% budget:
  → TRIGGER: Adaptive search (force H7, force ◈ PRIMARY templates, force ⟐̅ dissident)
```

**Example output (visible in investigation logs, not Part 1):**
```
[DSL MACROS INITIALIZED]
Complexity: MEDIUM (5.2/10)
→ EDI target: ≥0.50
→ ISN target: ≥7.0 (general topic)
→ Sources: ◈≥2 PRIMARY required
→ Query budget: 7-10 searches

EDI formula internalized: tracking geo, ◈◉○ ratio, topic perspectives
Adaptive trigger: IF running_EDI < 0.50 at search 5 → force H7/◈
```
```

### Impact
- **Cognitive alignment**: LLM knows targets BEFORE searching (not blind)
- **Real-time feedback**: LLM can adjust strategy mid-investigation
- **Testable**: Logs must contain "[DSL MACROS INITIALIZED]" + target values

---

## Implémentation 2 : Running Metrics During Search

### Localisation
**Fichier:** `system.md`
**Section:** "**1. QUERY FORMULATION**" (ligne ~330-360)
**Timing:** AFTER each web search execution, BEFORE next query

### Code Ajouté

```markdown
**1. QUERY FORMULATION** (@KB[QUERY_TEMPLATES] domain-adaptive):
   [...existing query formulation logic...]

**1.5 RUNNING METRICS TRACKING (v8.6 - Real-time Simulation):**

**AFTER EACH WEB SEARCH:**
```yaml
IF search_count % 2 == 0:  # Every 2 searches (not spam logs)
  → OUTPUT running estimate:

  "Running metrics (search {N}/{budget}):
   - ◈ PRIMARY: {count} (target: {◈_min})
   - Geo diversity: {unique_countries}/6 ({list})
   - Source types: ◈{X}% ◉{Y}% ○{Z}%
   - Topic perspectives: {⟐|🔥⟐̅|🌍|🎓} covered
   → Running EDI estimate: ~{0.00-1.00} (target: {target_EDI})
   → Status: {ON_TRACK | BELOW_TARGET | ADAPTIVE_NEEDED}"
```

**IF running_EDI < target_EDI AND search_count ≥ 50% budget:**
```yaml
→ TRIGGER ADAPTIVE SEARCH:
  "⚠️ Running EDI {value} < target {target} at search {N}.
  Adaptive response:
  - Next queries: Force ◈ PRIMARY templates (official docs, leaks)
  - IF controversy≥6: Force H7 adversary sources (RT, TASS, etc.)
  - IF geo_diversity<0.30: Force 🌍 regional (non-Western) sources"
```

**Example output (visible in investigation logs):**
```
Web search 4 executed: Mediapart investigation results
Running metrics (search 4/10):
 - ◈ PRIMARY: 1 (target: ≥2)
 - Geo diversity: 2/6 (FR, EU)
 - Source types: ◈25% ◉50% ○25%
 - Topic perspectives: ⟐🎓 covered, 🔥⟐̅ missing
 → Running EDI estimate: ~0.32 (target: ≥0.50)
 → Status: BELOW_TARGET

⚠️ Adaptive response triggered:
Next queries will prioritize:
 - ◈ PRIMARY sources (leaks, official documents)
 - 🔥⟐̅ Dissident perspective (missing)
 - 🌍 Regional diversity (currently FR+EU only)
```
```

### Impact
- **Real-time awareness**: LLM sees EDI gap DURING investigation, not after
- **Adaptive behavior**: LLM adjusts search strategy based on running metrics
- **Testable**: Logs must contain "Running metrics" every 2 searches + adaptive trigger if needed

---

## Implémentation 3 : Validation Coherence (Running vs Final)

### Localisation
**Fichier:** `kb/VALIDATION.md`
**Section:** Add new "§6.5 DSL Coherence Check"
**Timing:** POST-VALIDATION, before output finalization

### Code Ajouté

```markdown
## §6.5 DSL Coherence Check (v8.6)

**PURPOSE**: Verify LLM's running estimates were accurate (macro expansion = not hallucination)

**VALIDATION:**
```yaml
IF running_EDI_last_estimate exists:
  deviation = abs(running_EDI_last - final_EDI) / final_EDI

  IF deviation > 0.20:  # 20% error threshold
    → WARNING: "DSL macro estimation inaccurate.
       Running EDI: {running_EDI_last}
       Final EDI: {final_EDI}
       Deviation: {deviation*100}%

       Possible causes:
       - Underestimated source quality (○ counted as ◈)
       - Overestimated geo diversity (duplicates)
       - Topic diversity miscalculated

       → Mark investigation: DSL_CALIBRATION_NEEDED"

  ELIF deviation ≤ 0.20:
    → SUCCESS: "DSL macro simulation accurate (±{deviation*100}%)"
```

**PENALTY IF INACCURATE:**
```yaml
IF DSL_CALIBRATION_NEEDED:
  → No EDI penalty (investigation valid)
  → But flag for meta-analysis: "LLM DSL simulation needs recalibration"
  → Track pattern: Is LLM systematically over/under-estimating?
```

### Impact
- **Accountability**: LLM can't fake running estimates (validated against final)
- **Calibration feedback**: Meta-analysis can detect systematic bias (always overestimates EDI by 15%)
- **No regression**: Invalid estimates = warning only, not investigation failure

---

## Test Cases (Phase 2 Validation)

### Test 1: Simple Topic (EDI target 0.30)
**Query:** "PIB France 2024"
**Expected:**
- PREPROCESSING outputs: "EDI target: ≥0.30"
- Running metrics at search 4: "Running EDI ~0.25-0.35"
- Final EDI: 0.30-0.40
- Deviation: ≤20%

**Success:** ✅ Running estimate within 20% of final

---

### Test 2: Medium Topic with Adaptive Trigger (EDI target 0.50)
**Query:** "Chômage 7.4% France"
**Expected:**
- PREPROCESSING: "EDI target: ≥0.50, ◈≥2"
- Running metrics at search 4: "Running EDI ~0.30, BELOW_TARGET"
- Adaptive trigger: "⚠️ Next queries: Force ◈ PRIMARY + 🔥⟐̅ dissident"
- Searches 5-7: Different templates (ICEBERG pattern, L6 counter-narrative)
- Final EDI: ≥0.50

**Success:** ✅ Adaptive behavior detected, EDI target met

---

### Test 3: Complex Topic (EDI target 0.70)
**Query:** "Ukraine offensive OTAN provocation"
**Expected:**
- PREPROCESSING: "EDI target: ≥0.70, ISN≥9.0, ◈≥3"
- Running metrics search 6: "Geo 3/6 (FR,EU,US), missing RU adversary → EDI ~0.45"
- Adaptive trigger: "⚠️ Force H7 adversary (RT, TASS)"
- Search 8-10: H7 queries executed
- Final EDI: ≥0.70

**Success:** ✅ H7 forced by adaptive logic, EDI target met

---

### Test 4: Calibration Check (Deviation >20%)
**Query:** Any
**Scenario:** LLM estimates "Running EDI ~0.60" but final EDI = 0.40 (50% error)
**Expected:**
- VALIDATION outputs: "⚠️ DSL macro estimation inaccurate (deviation 50%)"
- Flag: DSL_CALIBRATION_NEEDED
- Investigation: VALID (no EDI penalty)
- Meta-analysis: Track pattern

**Success:** ✅ Deviation detected, flagged for calibration

---

### Test 5: No Regression (EDI preserved)
**Query:** Previous Sprint 1 Test 1 "Chômage 7.4%"
**Expected:**
- Sprint 1 baseline EDI: 0.35
- Sprint 2 with macros: EDI ≥0.35 (no degradation)
- New: Running estimates visible in logs

**Success:** ✅ EDI preserved or improved, running metrics present

---

## Success Criteria (Sprint 2)

### Critical (MUST PASS)

- [ ] **SC2.1**: PREPROCESSING outputs DSL targets (EDI, ISN, ◈ min) for 100% of investigations
- [ ] **SC2.2**: Running metrics logged ≥3 times per investigation (every 2 searches)
- [ ] **SC2.3**: Adaptive trigger fires when running_EDI < target at 50% budget (Test 2, Test 3)
- [ ] **SC2.4**: Final EDI deviation from running estimate ≤20% (≥80% of tests)
- [ ] **SC2.5**: NO EDI/ISN regression vs Sprint 1 baseline (Test 5)

### Desirable (SHOULD PASS)

- [ ] **SC2.6**: Adaptive behavior changes query templates (observable in logs)
- [ ] **SC2.7**: H7 adversary forced by adaptive logic on geopolitical topics (Test 3)
- [ ] **SC2.8**: ◈ PRIMARY forced by adaptive logic when below target (Test 2)
- [ ] **SC2.9**: Calibration tracking works (deviation >20% flagged, Test 4)
- [ ] **SC2.10**: Meta-pattern: LLM learns from calibration flags (future improvement)

---

## Metrics to Collect (Phase 2)

### DSL Simulation Metrics (PRIMARY)

| Metric | Target | Measure Method |
|--------|--------|----------------|
| **DSL targets in PREPROCESSING** | 100% | Does output contain "EDI target: X"? (binary per investigation) |
| **Running estimates frequency** | ≥3/investigation | Count "Running metrics (search N)" in logs |
| **Adaptive trigger rate** | IF needed | Does adaptive trigger fire when running_EDI < target? (Test 2, 3) |
| **Estimate accuracy (deviation)** | ≤20% | \|running_EDI_last - final_EDI\| / final_EDI |
| **Calibration flag rate** | <20% investigations | How often deviation >20%? (should decrease over time) |

### Quality Preservation (SECONDARY)

| Metric | Target | Measure Method |
|--------|--------|----------------|
| **EDI regression** | 0 | Sprint 2 EDI ≥ Sprint 1 EDI (same test cases) |
| **ISN regression** | 0 | Sprint 2 ISN ≥ Sprint 1 ISN |
| **Adaptive effectiveness** | +0.10 EDI | Does adaptive trigger improve final EDI vs non-adaptive baseline? |

---

## Implementation Phases

### Phase 1 — Implementation (1-2h)
1. Add "0.5 DSL MACRO EXPANSION" to system.md PREPROCESSING (after complexity)
2. Add "1.5 RUNNING METRICS TRACKING" to system.md QUERY FORMULATION (after searches)
3. Add "§6.5 DSL Coherence Check" to kb/VALIDATION.md
4. Commit changes

**Deliverable:** system.md + kb/VALIDATION.md updated, committed

---

### Phase 2 — Validation (2h)
1. Create test suite: tests/sprint2/test1-5.md (5 test cases)
2. Execute tests via Task agents (parallel execution if possible)
3. Collect metrics: DSL targets present? Running estimates? Adaptive triggers? Deviation?
4. Compile validation-results.md
5. Decision: SUCCESS (5/5 criteria) → v8.6 production | PARTIAL → iterate

**Deliverable:** tests/sprint2/validation-results.md + decision

---

## Risks & Mitigations

### Risk 1: LLM ignores new instructions (too verbose)
**Mitigation:**
- Keep instructions minimal (3 short sections added)
- Use existing @KB references (don't duplicate formulas)
- Test with Test 1 (simple) first

### Risk 2: Running estimates always inaccurate (>20% deviation)
**Mitigation:**
- Accept as baseline, track improvement over time
- Calibration flags = data for meta-analysis
- Even inaccurate estimates > no estimates (cognitive awareness)

### Risk 3: Adaptive trigger too aggressive (spams H7 unnecessarily)
**Mitigation:**
- Trigger only at 50% budget (search 5/10, not search 2/10)
- Require both: running_EDI < target AND controversy≥6 for H7

### Risk 4: Performance regression (slower investigations)
**Mitigation:**
- Running metrics every 2 searches (not every search)
- Minimal compute (count ◈, list geo, estimate EDI - simple operations)
- Expected overhead: <30s per investigation

---

## Expected Outcomes

### If SUCCESS (5/5 criteria)
- **v8.6 Sprint 2 deployed to production**
- LLM now "thinks" DSL formulas during investigation (not post-hoc)
- Adaptive search behavior unlocked (adjusts strategy based on running metrics)
- Foundation for Sprint 3 (Heuristics: "IF pattern X → force action Y")

### If PARTIAL (3-4/5 criteria)
- Identify bottleneck (accuracy? adaptive logic? regression?)
- Quick iteration (fix 1 issue, retest)
- Deploy if SC2.1-2.3+2.5 pass (core functionality + no regression)

### If FAILURE (<3/5 criteria)
- Postmortem: Why did DSL simulation fail? (LLM capacity? Instruction clarity?)
- Rollback to v8.5 Sprint 1
- Alternative approach: External DSL simulator (Python script calculates running EDI, passes to LLM)

---

## Philosophy (Sprint 2)

**Core Insight:** Truth Engine invented a complex DSL (COGNITIVE_DSL.md, 148 concepts) but doesn't internalize it during operation. Sprint 2 fixes this cognitive gap.

**NOT about:**
- ❌ Making DSL more complex
- ❌ Adding new formulas
- ❌ Forcing LLM memorize 148 concepts

**IS about:**
- ✅ LLM simulates core formulas (IVF/ISN/EDI) in real-time
- ✅ Running awareness → adaptive behavior
- ✅ Cognitive alignment: LLM "thinks" what it "knows"

**Analogy:** A chess engine that evaluates positions AFTER the game vs DURING the game. Sprint 2 = during-the-game evaluation.

---

**Version:** Sprint 2 v8.6
**Dependencies:** Sprint 1 v8.5 (Anti-Sycophancy + Fact-Checking)
**Next:** Sprint 3 (Heuristics: Pattern-based autopilot)
**Last updated:** 2025-11-17
