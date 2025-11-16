# POST-SEARCH VALIDATION — Self-Correction Loop

**Purpose**: Validate collected sources meet targets BEFORE generating output. If gaps detected + budget remaining → RETRY targeted queries. If gaps + budget exhausted → WARNINGS + penalties.

**Usage**: Referenced by Truth Engine preprocessing step 3 via @KB[VALIDATION]

**Version**: 1.0 (2025-11-06)

---

## 1. VALIDATION FLOW

```yaml
EXECUTE AFTER search queries complete, BEFORE output generation:

STEP_1: Validate ◈ PRIMARY stratification
STEP_2: Validate 🌍 GEOGRAPHIC diversity  
STEP_3: Validate 🔥 H7_ADVERSARY perspectives (if H7 triggered)
STEP_4: Decision (PROCEED with output OR RETRY OR WARNINGS)
```

---

## 2. STEP 1 — Validate PRIMARY Stratification

### 2.1 Count Sources

```yaml
COUNT collected_sources by tier:
  ◈_count = PRIMARY sources (archives, leaks, official docs, datasets)
  ◉_count = SECONDARY sources (investigative journalism, academic, expert)
  ○_count = TERTIARY sources (mainstream media, aggregators, opinion)
```

### 2.2 Check Target

```yaml
DETERMINE target based on complexity:
  SIMPLE (0-3): ◈_target = 1
  MEDIUM (4-6): ◈_target = 2
  COMPLEX (7-8): ◈_target = 3
  APEX (9-10): ◈_target = 3

IF ◈_count < ◈_target:
  → GAP_DETECTED: Primary evidence insufficient
```

### 2.3 Retry or Warn

```yaml
IF GAP_DETECTED AND budget_remaining > 0:
  
  → RETRY: Execute 1-2 additional queries with alternate ◈ templates
  
  → REASON: "Primary evidence gap critical for credibility (ISN_max capped without ◈≥3)"
  
  → Try alternate (see @KB[QUERY_TEMPLATES§4.1]):
    * Different ccTLD (.fr → .gov → .org)
    * Different filetype (pdf → doc → dataset)
    * Broader keywords ("leaked" → "official documents" → "archives")
  
  → AFTER RETRY: Re-run STEP_1 validation

ELSE IF GAP_DETECTED AND budget_exhausted:
  
  → WARNING Part 1:
    "⚠️ SOURCES PRIMAIRES INSUFFISANTES: ◈={◈_count}/{◈_target} (besoin ≥{target} archives/leaks/docs officiels).
     Fiabilité limitée. ITERATION I0→I1 recommandée."
  
  → EDI penalty: -0.10
  
  → ISN_max capped: 7.0 (impossible atteindre 9.0+ politique sans ◈≥3)
  
  → Part 2 [DIAGNOSTICS]: Add flag PRIMARY_GAP

ELSE IF ◈_count ≥ 3:
  
  → BONUS EDI: +0.05
  
  → ISN_max: 10.0 (full range unlocked)
```

---

## 3. STEP 2 — Validate GEOGRAPHIC Diversity

### 3.1 Calculate Diversity

```yaml
CALCULATE geo_diversity:
  continents_covered / 6 × 0.4 + non_native_region_pct × 0.6

WHERE:
  continents_covered = distinct continents in sources (max 6)
  non_native_region_pct = sources outside native_region / total_sources
  
  native_region determined by query_language:
    FR → France/Francophonie
    EN → USA/UK/Anglosphere
    DE → Germany/DACH
    [see @KB[QUERY_TEMPLATES§2.1] for full list]
```

### 3.2 Determine Target

```yaml
TARGET geo_diversity (complexity-adjusted):
  SIMPLE (0-3): ≥0.30 (acceptable)
  MEDIUM (4-6): ≥0.35 (good)
  COMPLEX (7-8): ≥0.40 (excellent)
  APEX (9-10): ≥0.50 (global coverage)

IF geo_diversity < target:
  → GAP_DETECTED: Geographic monoculture
```

### 3.3 Retry or Warn

```yaml
IF GAP_DETECTED AND budget_remaining > 0:
  
  → RETRY: Execute 1-2 GEO queries with comparables templates
  
  → REASON: "Geographic diversity gap compromises perspective balance"
  
  → Use @KB[QUERY_TEMPLATES§2 comparables detection + templates]
  
  → AFTER RETRY: Re-run STEP_2 validation

ELSE IF GAP_DETECTED AND budget_exhausted:
  
  → WARNING Part 1:
    "⚠️ PERSPECTIVE GÉOGRAPHIQUE LIMITÉE: {geo_pct}% sources hors région native ({native_region}).
     Angles internationaux manquants: {list_missing_comparables}."
  
  → EDI penalty: -0.10
  
  → Recommend I1 with targeted GEO queries (list specific comparables missed)
  
  → Part 2 [DIAGNOSTICS]: Add flag GEO_GAP

ELSE IF geo_diversity ≥ 0.40:
  
  → BONUS EDI: +0.05
  
  → Part 1 mention: "✅ Diversité géographique satisfaisante ({continents} continents, {geo_pct}% international)"
```

---

## 4. STEP 3 — Validate H7_ADVERSARY (If Triggered)

### 4.1 Check H7 Trigger

```yaml
IF H7_SENSITIVE_detected = True (see @KB[QUERY_TEMPLATES§3.1]):
  
  COUNT adversary_sources:
    🔥_dissident_count = Dissident sources (deplatformed, censored, radical)
    ⟐̅_counter_count = Counter-hegemonic sources (alternative analysis)
  
  TARGET: (🔥 + ⟐̅) ≥ 2 minimum
  
  IF (🔥 + ⟐̅) < 2:
    → GAP_DETECTED: Adversary perspective absent despite H7 trigger

ELSE (H7 not triggered):
  → SKIP STEP_3 (adversary not mandatory)
```

### 4.2 Retry or Warn

```yaml
IF GAP_DETECTED AND budget_remaining > 0:
  
  → RETRY: Execute 1-2 H7 queries with adversary templates
  
  → REASON: "H7 mandatory for sensitive subjects (dialectic 95% hostility)"
  
  → Queries (see @KB[QUERY_TEMPLATES§3.2]):
    * "{subject} criticism OR opposition OR counter-narrative"
    * "{subject} alternative media OR dissident OR censored perspective"
  
  → AFTER RETRY: Re-run STEP_3 validation

ELSE IF GAP_DETECTED AND budget_exhausted:
  
  → WARNING Part 1:
    "⚠️ CARTOGRAPHIE INCOMPLÈTE: Perspective adversaire absente malgré H7 trigger (sujet sensible).
     Fiabilité compromise. Dialectique 95% hostilité non respectée."
  
  → EDI penalty: -0.15 (higher than other gaps, critical for H7)
  
  → Part 2 [DIAGNOSTICS]: Add flag H7_GAP
  
  → Part 2 [WARNING]: INCOMPLETE_CARTOGRAPHY: adversary_perspective=MISSING

ELSE IF (🔥 + ⟐̅) ≥ 3:
  
  → BONUS: Dialectic balance achieved (note in Part 1)
```

---

## 5. STEP 4 — Validation Complete

### 5.1 Decision Matrix

```yaml
IF all_targets_met (◈≥target AND geo≥target AND (H7_ok OR H7_na)):
  
  → PROCEED output Part 1+2+3 (no warnings)
  
  → EDI bonuses applied (cumulative +0.05 to +0.15 possible)
  
  → ISN_max unlocked 10.0
  
  → Part 1 mentions: "✅ Standards épistémiques atteints"
  
  → Part 2 [DIAGNOSTICS]: Clean (no gap flags)

ELSE IF gaps_remain AND budget_exhausted:
  
  → PROCEED output with WARNINGS in Part 1
  
  → Part 1 "Avertissements" section: Detail gaps with specifics
  
  → Part 1 "Gaps & Credibility Impact" section (end): Quantify impact + recommend iteration
  
  → EDI penalties applied (cumulative -0.10 to -0.25)
  
  → ISN_max capped if ◈<3
  
  → Part 2 [DIAGNOSTICS]: Add gap flags (PRIMARY_GAP, GEO_GAP, H7_GAP)
  
  → Part 2 [WARNING]: List incomplete standards
```

### 5.2 Iteration Recommendation

```yaml
IF gaps_remain AND budget_exhausted:
  
  CALCULATE optimal_budget:
    IF complexity < 4.0: optimal = 10 queries (I0→I1)
    IF complexity 4.0-6.9: optimal = 20 queries (I0→I1→I2)
    IF complexity ≥7.0: optimal = 30 queries (I0→I1→I2 full)
  
  OUTPUT Part 1 recommendation:
    "ITERATION I0→I1 recommandée ({optimal} searches total, 2 conversations).
     Gaps prioritaires I1:
       - ◈ PRIMARY: {X} sources manquantes (need {target-current} more archives/docs)
       - 🌍 GEO: {list missing comparables/regions}
       - 🔥 H7: Adversary perspectives absent (need ≥2 counter/dissident sources)
     
     Usage: Nouvelle conversation Claude.ai Projects → Paste HANDOFF MEMO → 'mode ITERATION I1'
     Protocol: @KB[HANDOFF_MEMO]"
```

---

## 6. Penalties and Bonuses Summary

### 6.1 EDI Penalties

```yaml
PRIMARY_GAP (◈<target):
  - Penalty: -0.10
  - Impact: ISN_max capped 7.0, credibility reduced

GEO_GAP (geo<target):
  - Penalty: -0.10
  - Impact: Monoculture bias, perspective limited

H7_GAP (adversary<2 when H7 triggered):
  - Penalty: -0.15 (higher, critical)
  - Impact: Dialectic broken, 95% hostility violated

CUMULATIVE:
  - Multiple gaps: Penalties stack (-0.10 to -0.25 total)
  - Apply to EDI_raw to get EDI_final
  - EDI formula: @KB[SEARCH_EPISTEMIC§11]
```

### 6.2 EDI Bonuses

```yaml
PRIMARY_EXCELLENCE (◈≥3):
  - Bonus: +0.05
  - Trigger: ≥3 primary sources collected

GEO_EXCELLENCE (geo≥0.40):
  - Bonus: +0.05
  - Trigger: 40%+ non-native region sources

CUMULATIVE:
  - Multiple achievements: Bonuses stack (+0.05 to +0.10 total)
  - Apply to EDI_raw to get EDI_final
```

---

## 7. BRANCH SCORING (Investigation Tree — APEX only)

**Context**: After I0 validation completes for APEX investigations (complexity ≥9.0), detect and score investigation branches for parallel multi-agent exploration.

**Full specifications**: See @KB[INVESTIGATION_TREE] for complete Investigation Tree protocol.

### 7.1 Branch Detection — Heuristique DSL

```yaml
DETECT_BRANCHES:
  INPUT: i0_state (EDI, sources, patterns, wolves, timing)
  OUTPUT: candidates[] (10-15 typical)

  # Trigger 1: Gaps Critical
  @TRIGGER[GAP_CRITICAL]:

    IF ◈_current < ◈_target:
      → candidate: b_primary_sources
         type: GAP_CRITICAL
         objective: "Find ◈ PRIMARY independent sources {subject}"
         edi_impact_estimated: 0.50

    FOR each dimension IN edi_dimensions:
      IF dimension.score < 0.30:
        → candidate: b_edi_{dimension.name}
           type: GAP_CRITICAL
           objective: "Improve {dimension.name} diversity (current: {dimension.score})"
           edi_impact_estimated: max(0.40, 0.60 - dimension.score)

  # Trigger 2: Patterns Strong
  @TRIGGER[PATTERN_STRONG]:

    FOR each pattern IN detected_patterns:
      IF pattern.score ≥ 8:
        → candidate: b_pattern_{pattern.symbol}
           type: PATTERN_STRONG
           objective: "Explore {pattern.name} pattern (score {pattern.score})"
           edi_impact_estimated: 0.25

  # Trigger 3: Actors WOLF Central
  @TRIGGER[ACTOR_CENTRAL]:

    FOR each actor IN wolves.individuals[0:5]:
      IF actor.centrality > 0.60:
        → candidate: b_actor_{actor.name_normalized}
           type: ACTOR_CENTRAL
           objective: "Investigate {actor.name} role and connections"
           cui_bono_centrality_estimated: actor.centrality

  # Trigger 4: Timing Suspect
  @TRIGGER[TIMING_SUSPECT]:

    IF timing_suspicion_prob < 0.01:
      → candidate: b_timing_analysis
         type: TIMING_SUSPECT
         objective: "Analyze temporal coincidences and causality"
         edi_impact_estimated: 0.15

  # Trigger 5: EDI Insufficient
  @TRIGGER[EDI_INSUFFICIENT]:

    IF edi_current < edi_target:
      delta ← edi_target - edi_current
      → candidate: b_edi_global
         type: EDI_INSUFFICIENT
         objective: "Improve global EDI by {delta}"
         edi_impact_estimated: delta

  # Trigger 6: COMPARABLES (v1.1)
  @TRIGGER[COMPARABLES_LAUNCH]:

    # Path A: Regulatory context
    IF regulatory_context = true:
      IF sanctions_detected > 0 OR controversy ≥ 6:
        → candidate: b_comparables_{regulator}
           type: COMPARABLES
           objective: "Find comparable cases {regulator} similar context different treatment"
           edi_impact_estimated: 0.35

    # Path B: Ξ OMISSION pattern
    IF pattern[Ξ].score ≥ 8:
      IF regulatory_context = true OR "differential_treatment" IN omission_signals:
        → candidate: b_comparables_omission
           type: COMPARABLES
           objective: "Find hidden comparables revealing Ξ OMISSION"
           edi_impact_estimated: 0.35
```

### 7.2 Branch Scoring — Formulas DSL

```yaml
@F[BRANCH_PRIORITY]:
  # Core formula (0.0-1.0 range)
  priority ← edi_impact × 0.5 + cui_bono_centrality × 0.5

@F[EDI_IMPACT]:
  # Estimate EDI contribution potential (0.0-1.0)

  HEURISTIC:

    IF branch.type = GAP_CRITICAL:
      IF "primary_sources" IN branch.id:
        → 0.50  # Finding ◈ = major EDI boost

      ELSE IF "edi_" IN branch.id:
        dimension ← extract_dimension(branch.id)
        current ← edi_dimensions[dimension]
        → max(0.40, 0.60 - current)  # Inverse proportional

    ELSE IF branch.type = PATTERN_STRONG:
      → 0.25  # Medium impact

    ELSE IF branch.type = ACTOR_CENTRAL:
      → 0.20  # Medium-low impact

    ELSE IF branch.type = TIMING_SUSPECT:
      → 0.15  # Low impact

    ELSE IF branch.type = EDI_INSUFFICIENT:
      → edi_target - edi_current  # Direct delta

    ELSE IF branch.type = COMPARABLES:
      → 0.35  # Medium-high (narrative diversity + Ξ OMISSION revelation)

    ELSE:
      → 0.10  # Default baseline

@F[CUI_BONO_CENTRALITY]:
  # Estimate WOLF network centrality importance (0.0-1.0)

  HEURISTIC:

    IF branch.type = ACTOR_CENTRAL:
      actor_name ← extract_actor_name(branch.objective)
      actor_data ← find_in_wolves(actor_name, wolves.individuals)

      IF actor_data EXISTS:
        → actor_data.centrality  # Actual centrality score
      ELSE:
        → 0.30  # Default medium

    ELSE IF branch.type = PATTERN_STRONG:
      pattern ← extract_pattern(branch.id)

      IF pattern IN [€, ♦, ⚔, 🌐]:
        → 0.30  # Power/network patterns = medium centrality
      ELSE:
        → 0.15  # Other patterns = low centrality

    ELSE IF branch.type = GAP_CRITICAL:
      IF "actor" IN branch.objective.lower() OR "connection" IN branch.objective.lower():
        → 0.25  # Actor-related gaps = medium-low
      ELSE:
        → 0.10  # Generic gaps = low

    ELSE IF branch.type = TIMING_SUSPECT:
      → 0.05  # Very low centrality

    ELSE IF branch.type = COMPARABLES:
      IF regulatory_context IN ["media_regulator", "competition_authority", "central_bank"]:
        → 0.25  # Medium-low (institutional power, not individual actors)
      ELSE:
        → 0.15  # Low (generic comparables)

    ELSE:
      → 0.10  # Default baseline

SCORE_BRANCH:
  INPUT: candidate (branch without score), i0_state
  OUTPUT: scored_branch (with priority, edi_impact, cui_bono)

  COMPUTE:
    edi_impact ← @F[EDI_IMPACT](candidate, i0_state)
    cui_bono ← @F[CUI_BONO_CENTRALITY](candidate, i0_state)
    priority ← @F[BRANCH_PRIORITY](edi_impact, cui_bono)

  ASSIGN:
    candidate.score.edi_impact ← edi_impact
    candidate.score.cui_bono_centrality ← cui_bono
    candidate.score.priority ← priority

  RETURN: candidate (now scored)
```

### 7.3 Branch Selection — Heuristique DSL

```yaml
SELECT_BRANCHES:
  INPUT: scored_branches[] (all candidates with scores)
  INPUT: max_branches (default: 5, typical range: 3-5)
  OUTPUT: selected_branches[] (top priority only)

  SORT:
    sorted ← ORDER_BY(scored_branches, key=priority, direction=DESC)
    # Descending: highest priority first

  SLICE:
    selected ← sorted[0:max_branches]
    # Take top 3-5 only (prevent combinatorial explosion)

  RETURN: selected
```

### 7.4 Usage in APEX Workflow

```yaml
# After I0 validation completes, if complexity ≥ 9.0:

1. DETECT branches:
   candidates = detect_branches(i0_state)
   # Typical: 10-15 candidates from 5 trigger types

2. SCORE branches:
   FOR each candidate:
     candidate.score = score_branch(candidate, i0_state)
     # priority = edi_impact × 0.5 + cui_bono × 0.5

3. SELECT top priority:
   selected = select_branches(scored_branches, max=5)
   # Top 3-5 branches only (prevent explosion)

4. EXECUTE parallel exploration:
   → See @KB[INVESTIGATION_TREE§4] for sub-agent lifecycle
```

### 7.5 COMPARABLES Detection & Scoring (v1.1)

**Purpose:** Detect regulatory/institutional asymmetries via comparable cases search (6th branch type).

**Trigger conditions:**

```yaml
@TRIGGER[COMPARABLES_LAUNCH]:

  # Path A: Regulatory context detected
  IF regulatory_context = true:  # ARCOM, EU Commission, SEC, FDA, central banks
    IF sanctions_detected > 0 OR controversy ≥ 6:
      → candidate: b_comparables_{regulator}
         type: COMPARABLES
         objective: "Find comparable cases {regulator} {time_window} similar context different treatment"
         edi_impact_estimated: 0.35
         cui_bono_centrality_estimated: 0.25

  # Path B: Ξ OMISSION pattern strong
  IF pattern[Ξ].score ≥ 8:
    IF "differential_treatment" IN omission_signals OR regulatory_context = true:
      → candidate: b_comparables_omission
         type: COMPARABLES
         objective: "Find hidden comparables revealing Ξ OMISSION"
         edi_impact_estimated: 0.35

  # Path C: Mid-tree reactive (during I1)
  IF any_branch.results CONTAINS regulatory_action:
    IF comparable_cases NOT searched:
      → candidate: b_comparables_reactive
         type: COMPARABLES
         parent: {triggering_branch_id}
```

**Scoring integration:**

```yaml
@F[EDI_IMPACT]:
  # ... existing cases ...

  ELSE IF branch.type = COMPARABLES:
    → 0.35  # Medium-high impact
    # Improves: narrative_diversity (reveals hidden comparables)
    #           omission_detection (exposes differential treatment)

@F[CUI_BONO_CENTRALITY]:
  # ... existing cases ...

  ELSE IF branch.type = COMPARABLES:
    IF regulatory_context IN ["media_regulator", "competition_authority", "central_bank"]:
      → 0.25  # Medium-low (institutional power, not individual actors)
    ELSE:
      → 0.15  # Low (generic comparables)
```

**Success criteria:**

```yaml
BRANCH.status:
  CONVERGED: ≥2 comparables found with context_similarity ≥0.60
  EXHAUSTED: 3 consecutive failures, <2 comparables found

SYNTHESIS.asymmetry:
  IF comparables_found ≥ 2:
    → Run DETECT_ASYMMETRY (calculates asymmetry_score 0-10)
    → Verdict: EXTREME (≥7.0) | SIGNIFICANT (≥5.0) | MODERATE (≥3.0) | MINIMAL (<3.0)
  ELSE:
    → Skip asymmetry synthesis (INSUFFICIENT_DATA)
```

**Use case example:**

```yaml
Subject: "ARCOM amende CNews 20k€ désinformation climatique"

Trigger: regulatory_context=true (ARCOM) + sanctions_detected=1 + Ξ=8.5

Branch b5_comparables_arcom:
  comparables_found:
    - TF1: 7 sanctions légères (severity 0.25, similarity 0.75)
    - LCI: 3 sanctions mineures (severity 0.20, similarity 0.70)
    - BFM: 5 sanctions modérées (severity 0.30, similarity 0.72)
    - CNews: 52 sanctions + 20k€ (severity 0.85, similarity 1.0)

Asymmetry analysis:
  score: 8.2/10
  verdict: ASYMMETRY_EXTREME
  subject_position: ABOVE_AVERAGE (CNews 0.85 >> mean 0.40)
  Ξ OMISSION revealed: Clémence TF1/LCI/BFM vs rigueur CNews absent narratifs
```

**Full specifications:** See @KB[INVESTIGATION_TREE§5.6] DETECT_ASYMMETRY + @F[ASYMMETRY_SCORE]

### 7.6 Integration with Validation Flow

```yaml
APEX investigations (complexity ≥9.0):

STEP 0: Complexity detection → APEX detected
STEP 1-2: Query allocation + execution (I0 baseline)
STEP 3: POST-SEARCH VALIDATION (sections 1-6 this file)
  → 3.1: Validate PRIMARY
  → 3.2: Validate GEO
  → 3.3: Validate H7
  → 3.4: Decision (warnings if gaps)
STEP 4-7: Herméneutique, Scoring, Patterns, Wolves
STEP 7b: BRANCH SCORING (this section)  ← NEW for APEX
  → 7b.1: Detect branches (gaps, patterns, actors, timing, EDI)
  → 7b.2: Score branches (edi_impact, cui_bono_centrality)
  → 7b.3: Select top 3-5 priority branches
STEP 8: IF APEX: INVESTIGATION_TREE execution
        ELSE: Output Part 1+2+3 (standard)
```

---

## 8. Integration with Truth Engine

### 8.1 Preprocessing Flow

```yaml
STEP 0: Complexity detection
  → IF <9.0: LINEAR workflow
  → IF ≥9.0: ARBORESCENT workflow (Investigation Tree)

LINEAR workflow (SIMPLE/MEDIUM/COMPLEX):
  STEP 1: Query allocation (PRIMARY, H7, CONTEXT, DIVERSITY, OPP)
  STEP 2: Execute queries with @KB[QUERY_TEMPLATES]
  STEP 3: POST-SEARCH VALIDATION (sections 1-6)
    → 3.1: Validate PRIMARY
    → 3.2: Validate GEO
    → 3.3: Validate H7
    → 3.4: Decision (proceed OR retry OR warnings)
  STEP 4-7: Herméneutique, Scoring, Patterns, Wolves
  STEP 8: Output Part 1+2+3 (with validation warnings if any)

ARBORESCENT workflow (APEX only):
  STEP 1-3: Same as LINEAR (I0 baseline investigation)
  STEP 4-7: Same as LINEAR (I0 baseline scoring)
  STEP 7b: BRANCH SCORING (section 7 this file)
  STEP 8: INVESTIGATION_TREE execution (@KB[INVESTIGATION_TREE])
    → Parallel multi-agent branches
    → Synthesis (concordances ⊕, contradictions ⊗, EDI global)
    → Output Part 1+2+3 enriched + Mermaid + JSON
```

### 8.2 Reference Points

- **Instructions**: @KB[VALIDATION] (this file)
- **Templates**: @KB[QUERY_TEMPLATES] (retry strategies §4)
- **Stratification**: @KB[SEARCH_EPISTEMIC§1.3]
- **EDI calculation**: @KB[SEARCH_EPISTEMIC§11]
- **Iteration protocol**: @KB[HANDOFF_MEMO]
- **Investigation Tree**: @KB[INVESTIGATION_TREE] (APEX multi-agent workflow)

---

**END VALIDATION.md v1.1** (Investigation Tree integration)
**Last updated**: 2025-11-14
