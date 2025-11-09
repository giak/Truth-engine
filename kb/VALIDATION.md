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

## 7. Integration with Truth Engine

### 7.1 Preprocessing Flow

```yaml
STEP 0: Complexity detection
STEP 1: Query allocation (PRIMARY, H7, CONTEXT, DIVERSITY, OPP)
STEP 2: Execute queries with @KB[QUERY_TEMPLATES]
STEP 3: POST-SEARCH VALIDATION (this file)
  → 3.1: Validate PRIMARY
  → 3.2: Validate GEO
  → 3.3: Validate H7
  → 3.4: Decision (proceed OR retry OR warnings)
STEP 4-7: Herméneutique, Scoring, Patterns, Wolves
STEP 8: Output Part 1+2+3 (with validation warnings if any)
```

### 7.2 Reference Points

- **Instructions**: @KB[VALIDATION] (this file)
- **Templates**: @KB[QUERY_TEMPLATES] (retry strategies §4)
- **Stratification**: @KB[SEARCH_EPISTEMIC§1.3]
- **EDI calculation**: @KB[SEARCH_EPISTEMIC§11]
- **Iteration protocol**: @KB[HANDOFF_MEMO]

---

**END VALIDATION.md v1.0**
