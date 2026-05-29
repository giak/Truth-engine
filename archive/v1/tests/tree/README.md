# Investigation Tree v1.0 — Test Suite

**Purpose:** Validation tests pour Investigation Tree (Truth Engine v8.2 → v8.3 extension)

**Status:** Phase 1 ✅ COMPLETE | Phase 2 ✅ COMPLETE | Phase 3 🔄 NEXT

---

## Quick Start

### Run Phase 1 Validation
```bash
./tests/tree/validate_phase1.sh
```

**Expected output:** `✅ Phase 1 Validation PASSED`

---

## Test Files

### Phase 1 — Core Infrastructure (✅ COMPLETE)

| File | Purpose | Status |
|------|---------|--------|
| [test_phase1_single_branch.md](test_phase1_single_branch.md:1) | Test scenario: Single branch (gap_primary_sources) | ✅ Spec complete |
| [validate_phase1.sh](validate_phase1.sh:1) | Validation script (38 checks) | ✅ All checks pass |
| [PHASE1_RESULTS.md](PHASE1_RESULTS.md:1) | Results documentation | ✅ Phase 1 complete |

**Validated:**
- @TRIGGER[TREE_LAUNCH] with 5 trigger types
- @F[BRANCH_PRIORITY] formula (edi×0.5 + cui_bono×0.5)
- @F[EDI_IMPACT] heuristics (gap_primary_sources = 0.50)
- @MACRO[EXPLORE_BRANCH] with budget adaptatif
- Pertinence criteria A|B|C|D
- Synthesis operations (concordances, contradictions, gaps)
- Parallel execution @MACRO[LAUNCH_INVESTIGATION_TREE]
- Rétrocompatibilité (linear <9.0 vs arborescent ≥9.0)
- DSL purity (0 Python code)

### Phase 2 — Multi-Branch Synthesis (✅ COMPLETE)

| File | Purpose | Status |
|------|---------|--------|
| [test_phase2_multi_branch.md](test_phase2_multi_branch.md:1) | Test scenario: 4 branches parallel (EU AI Act) | ✅ Spec complete |
| [validate_phase2.sh](validate_phase2.sh:1) | Validation script (65+ checks) | ✅ All checks pass |
| [PHASE2_RESULTS.md](PHASE2_RESULTS.md:1) | Results documentation | ✅ Phase 2 complete |

**Validated:**
- DETECT_CONCORDANCES (⊕ facts ≥2 branches) — 3 concordances expected
- DETECT_CONTRADICTIONS (⊗ conflicting facts) — 2 contradictions expected
- IDENTIFY_GAPS_UNRESOLVED (△ remaining gaps) — 1 gap expected
- CALCULATE_EDI_GLOBAL (aggregation) — EDI 0.35 → 0.49 (+40%)
- DECIDE_I2 (trigger logic) — FINALIZE (acceptable quality)
- GENERATE_MERMAID (visualization) — Graph TD format specified
- GENERATE_JSON_STATE (export) — Complete schema validated

**Test subject:** "EU AI Act 2024 implementation timeline" (complexity 9.5)
- 4 branches: 2×ACTOR_CENTRAL (von der Leyen, Breton), 2×GAP_CRITICAL (primary sources, dissident)
- Convergence: 75% (3/4 branches)
- Sources: ◈1→4, ◉4→9, ○3→4

### Phase 3 — Integration & Testing (⏸ PLANNED)

| File | Purpose | Status |
|------|---------|--------|
| test_phase3_full_integration.md | End-to-end APEX workflow | ⏸ TODO |
| validate_phase3.sh | Full integration validation | ⏸ TODO |
| PHASE3_RESULTS.md | Results documentation | ⏸ TODO |

**To validate:**
- Full I0 → TREE → I2 workflow
- Rétrocompatibilité (SIMPLE/MEDIUM/COMPLEX unchanged)
- Edge cases (all EXHAUSTED, single CONVERGED, early stop)
- Performance (budget efficiency)

---

## Implementation Files

Investigation Tree DSL specifications:

| File | Content | Lines |
|------|---------|-------|
| [kb/INVESTIGATION_TREE.md](../../kb/INVESTIGATION_TREE.md:1) | Complete Tree v1.0 spec (§1-§9) | 713 |
| [kb/VALIDATION.md](../../kb/VALIDATION.md:1) | Section 7 BRANCH SCORING | +174 |
| [system.md](../../system.md:1) | APEX routing integration | ~26 |
| [docs/plans/2025-11-14-investigation-tree-design.md](../../docs/plans/2025-11-14-investigation-tree-design.md:1) | Design document (all phases) | 1100+ |

---

## Test Methodology

**Type:** Specification-based validation (not execution-based)

**Rationale:** Truth Engine is LLM prompt system (KB markdown files), not executable code.

**Approach:**
1. **Specification documents** define expected behavior (test_phase*.md)
2. **Validation scripts** check DSL implementation matches specifications (validate_phase*.sh)
3. **Results documents** track achievements and lessons learned (PHASE*_RESULTS.md)

**Validation checks:**
- Pattern matching (grep) for required DSL elements
- Formula correctness (@F[], @TRIGGER[], @MACRO[] definitions)
- Logic flow (IF/ELSE, LOOP_WHILE, status transitions)
- Integration points (system.md, kb/VALIDATION.md references)
- DSL purity (no Python code)

---

## DSL Components Validated

### Formulas (@F[])
- `@F[BRANCH_PRIORITY]` — Branch scoring (edi×0.5 + cui_bono×0.5)
- `@F[EDI_IMPACT]` — Estimated EDI improvement per branch type
- `@F[CUI_BONO_CENTRALITY]` — Actor centrality in cui bono network

### Triggers (@TRIGGER[])
- `@TRIGGER[TREE_LAUNCH]` — Investigation Tree activation (5 trigger types)

### Macros (@MACRO[])
- `@MACRO[EXPLORE_BRANCH]` — Single branch exploration loop
- `@MACRO[LAUNCH_INVESTIGATION_TREE]` — Parallel orchestration

### Heuristics
- `DETECT_BRANCHES` — Generate branch candidates
- `SCORE_BRANCH` — Calculate priority scores
- `BRANCH_SELECTION` — Select top N branches
- `DETECT_CONCORDANCES` — Find cross-branch confirmations
- `DETECT_CONTRADICTIONS` — Find conflicts
- `IDENTIFY_GAPS_UNRESOLVED` — Map remaining gaps
- `CALCULATE_EDI_GLOBAL` — Aggregate EDI
- `DECIDE_I2` — Trigger I2 logic
- `COMPLEXITY_ROUTING` — Linear vs arborescent workflow

### Structures
- `BRANCH` — Branch state (id, type, score, status, budget, results)
- `i0_state` — Initial investigation state
- `synthesis` — Tree synthesis output

---

## Success Criteria

### Phase 1 ✅
- [x] kb/INVESTIGATION_TREE.md created (713 lines DSL)
- [x] All formulas defined
- [x] All triggers specified
- [x] Budget adaptatif logic (consecutive_failures ≥3)
- [x] Synthesis operations defined
- [x] Rétrocompatibilité routing
- [x] Integration points (system.md, kb/VALIDATION.md)
- [x] 38/38 validation checks passed
- [x] 0 Python code (100% DSL pur)

### Phase 2 ✅
- [x] Multi-branch test case (4 branches: EU AI Act 2024)
- [x] Synthesis operations validated (all 5: concordances, contradictions, gaps, edi_global, i2_decision)
- [x] EDI global calculation tested (0.35 → 0.49, +40%)
- [x] I2 decision logic confirmed (FINALIZE, no critical gaps)
- [x] Mermaid visualization format (graph TD with ⊕⊗ edges)
- [x] JSON state export format (complete schema validated)
- [x] Convergence rate acceptable (75%, 3/4 branches)
- [x] ◈ PRIMARY target achieved (1→4 sources)

### Phase 3 (TODO)
- [ ] Full I0 → TREE → I2 workflow
- [ ] Rétrocompatibilité confirmed (SIMPLE/MEDIUM/COMPLEX)
- [ ] Edge cases handled
- [ ] Performance acceptable

---

## Contributing

When adding tests:

1. **Create test specification** (test_phase*.md)
   - Test scenario with subject
   - Expected behavior (input → output)
   - Success criteria

2. **Create validation script** (validate_phase*.sh)
   - Check DSL specifications match test expectations
   - Report ✅/❌ for each check
   - Exit 0 if passed, exit 1 if failed

3. **Document results** (PHASE*_RESULTS.md)
   - Summary of achievements
   - Validation results
   - Files modified/created
   - Lessons learned
   - Next steps

4. **Update this README**
   - Add new test files to table
   - Update status (⏸ TODO → 🔄 IN PROGRESS → ✅ COMPLETE)
   - Document new success criteria

---

## References

- [Investigation Tree Design Document](../../docs/plans/2025-11-14-investigation-tree-design.md:1)
- [Truth Engine CLAUDE.md](../../CLAUDE.md:1) — Project instructions
- [kb/COGNITIVE_DSL.md](../../kb/COGNITIVE_DSL.md:1) — DSL patterns reference
- [kb/INVESTIGATION.md](../../kb/INVESTIGATION.md:1) — Investigation depth protocols
- [kb/VALIDATION.md](../../kb/VALIDATION.md:1) — Post-search validation

---

**Version:** Investigation Tree v1.0
**Last updated:** 2025-11-14
**Status:** Phase 1 ✅ | Phase 2 ✅ | Phase 3 🔄
