# COMPARABLES_ASYMMETRY — Design Specification

**Date:** 2025-11-14
**Version:** Investigation Tree v1.0 → v1.1 extension
**Status:** Design complete, ready for integration

---

## Context

**Problem identified:** User's manual investigation tweet (ARCOM/CNews) was superior to simulation because it included critical comparables (TF1 7 sanctions légères vs CNews 52 sanctions + 20k€ inédite).

**Gap in Investigation Tree v1.0:** No mechanism to systematically detect and measure regulatory/institutional asymmetries (same authority, different treatments).

**Solution:** COMPARABLES_ASYMMETRY as hybrid architecture (6th branch type + 6th synthesis operation).

---

## Brainstorming Answers Summary

Based on `/superpowers:brainstorm` session (2025-11-14):

| Question | Answer | Implication |
|----------|--------|-------------|
| Q1: Découverte quand? | B (I1/I2, pas I0) | Can be triggered MID-TREE during exploration |
| Q2: Focus asymétrie? | A (même régulateur, contextes similaires) | Regulatory/institutional focus |
| Q3: Nature? | B + C (Ξ OMISSION sub-type AND synthesis op) | Dual architecture required |
| Q4: Trigger? | A / B (context OR Ξ≥8) | Multiple trigger paths |
| Q5: Succès? | C (comparables found, asymmetry measurable) | Not binary detection |
| Q6: Mesure? | B (scale 0-10) | Quantitative asymmetry score |
| Q7: Architecture? | A (hybrid: branch + synthesis) | Both components needed |

---

## Architecture Design

### 1. Branch Type: COMPARABLES (6th type)

**Purpose:** Search for comparable cases to detect differential treatment patterns.

**Trigger conditions** (multiple paths):

```yaml
@TRIGGER[COMPARABLES_LAUNCH]:
  # Path A: Regulatory/institutional context detected
  IF regulatory_context = true:  # ARCOM, EU Commission, SEC, FDA, etc.
    IF sanctions_detected > 0 OR controversy ≥ 6:
      → Launch COMPARABLES branch

  # Path B: Ξ OMISSION pattern strong
  IF pattern[Ξ].score ≥ 8:
    IF "differential_treatment" IN omission_signals:
      → Launch COMPARABLES branch

  # Path C: Mid-tree discovery (during I1 branches exploration)
  IF any_branch.results CONTAINS regulatory_action:
    IF comparable_cases NOT searched:
      → Launch COMPARABLES branch (reactive trigger)
```

**Branch structure:**

```yaml
BRANCH_COMPARABLES:
  id: "b{n}_comparables_{regulator}_{subject}"
  parent: "i0_root" OR "{triggering_branch_id}"  # Can be root or child
  type: COMPARABLES
  objective: "Find comparable cases {regulator} {time_window} similar context different treatment"

  score:
    edi_impact: 0.35              # Medium-high (narrative diversity + omission revelation)
    cui_bono_centrality: 0.25     # Medium-low (institutional analysis, not individual actors)
    priority: 0.30                # (0.35×0.5 + 0.25×0.5)

  status: PENDING | EXPLORING | CONVERGED | EXHAUSTED

  budget:
    queries_executed: int
    consecutive_failures: int

  results:
    comparables_found: [
      {
        case_id: str,
        entity: str,               # Ex: "TF1", "LCI", "BFM"
        regulatory_action: str,    # Ex: "sanctions ARCOM 2020-2024"
        severity: float,           # 0.0-1.0 normalized severity
        context_similarity: float  # 0.0-1.0 how comparable to main subject
      }
    ]
    asymmetry_raw: float          # Variance in severity scores
    asymmetry_score: 0-10         # @F[ASYMMETRY_SCORE] output
```

---

### 2. Formulas Integration

#### @F[EDI_IMPACT] — Add COMPARABLES case

```yaml
@F[EDI_IMPACT]:
  # ... existing cases ...

  ELSE IF branch_type = "comparables":
    → 0.35  # Medium-high impact
    # Improves: narrative_diversity (reveals hidden comparables)
    #           omission_detection (exposes differential treatment)
    # Less than gap_primary_sources (0.50) but > actor_chronology (0.20)
```

**Rationale:** COMPARABLES reveals Ξ OMISSION patterns (hidden context), improving narrative diversity significantly.

#### @F[CUI_BONO_CENTRALITY] — Add COMPARABLES case

```yaml
@F[CUI_BONO_CENTRALITY]:
  # ... existing cases ...

  ELSE IF branch_type = "comparables":
    IF regulatory_context IN ["media_regulator", "competition_authority", "central_bank"]:
      → 0.25  # Medium-low (institutional power, not individual actors)
    ELSE:
      → 0.15  # Low (generic comparables)
```

**Rationale:** COMPARABLES focuses on institutional analysis, not individual WOLF actors (lower cui_bono centrality).

---

### 3. Synthesis Operation: DETECT_ASYMMETRY

**Purpose:** Measure differential treatment across comparable cases (0-10 scale).

```yaml
DETECT_ASYMMETRY:
  INPUT: branches[] (completed branches with comparables_found)
  OUTPUT: asymmetry_analysis (score 0-10, comparables list, verdict)

  # Step 1: Collect all comparables
  all_comparables ← []
  FOR branch IN branches:
    IF branch.type = COMPARABLES AND branch.status = CONVERGED:
      all_comparables.extend(branch.results.comparables_found)

  # Step 2: Filter by context similarity (keep ≥0.60)
  relevant_comparables ← filter(all_comparables, where: context_similarity ≥ 0.60)

  IF count(relevant_comparables) < 2:
    → RETURN: {
         asymmetry_score: 0,
         verdict: "INSUFFICIENT_DATA (need ≥2 comparables)",
         comparables: relevant_comparables
       }

  # Step 3: Calculate severity variance
  severities ← [c.severity FOR c IN relevant_comparables]
  severity_mean ← mean(severities)
  severity_variance ← variance(severities)
  severity_range ← max(severities) - min(severities)

  # Step 4: Identify main subject severity
  subject_severity ← find_subject_severity(relevant_comparables, subject_name)

  # Step 5: Calculate asymmetry score (0-10)
  asymmetry_score ← @F[ASYMMETRY_SCORE](
    severity_variance,
    severity_range,
    subject_severity,
    severity_mean,
    relevant_comparables
  )

  # Step 6: Classify asymmetry
  IF asymmetry_score ≥ 7.0:
    verdict ← "ASYMMETRY_EXTREME (differential treatment flagrant)"
  ELSE IF asymmetry_score ≥ 5.0:
    verdict ← "ASYMMETRY_SIGNIFICANT (pattern détectable)"
  ELSE IF asymmetry_score ≥ 3.0:
    verdict ← "ASYMMETRY_MODERATE (variance notable)"
  ELSE:
    verdict ← "ASYMMETRY_MINIMAL (treatment homogène)"

  RETURN: {
    asymmetry_score: asymmetry_score,
    verdict: verdict,
    comparables: relevant_comparables,
    severity_stats: {
      mean: severity_mean,
      variance: severity_variance,
      range: severity_range
    },
    subject_position: subject_severity > severity_mean ? "ABOVE_AVERAGE" : "BELOW_AVERAGE"
  }
```

---

### 4. Formula: @F[ASYMMETRY_SCORE]

**Purpose:** Convert severity variance into interpretable 0-10 asymmetry score.

```yaml
@F[ASYMMETRY_SCORE]:
  INPUT:
    severity_variance: float      # Statistical variance of severity scores
    severity_range: float         # max - min (0.0-1.0)
    subject_severity: float       # Severity for main subject (0.0-1.0)
    severity_mean: float          # Mean severity across comparables
    comparables: list             # All relevant comparables

  OUTPUT: asymmetry_score (0-10 scale)

  HEURISTIC:

    # Component 1: Range-based score (40% weight)
    # High range = high differential treatment
    range_score ← severity_range × 10  # 0.0-1.0 → 0-10

    # Component 2: Variance-based score (30% weight)
    # High variance = inconsistent treatment
    variance_normalized ← min(severity_variance / 0.15, 1.0)  # Cap at 0.15
    variance_score ← variance_normalized × 10

    # Component 3: Subject extremity (30% weight)
    # Subject far from mean = asymmetry signal
    subject_deviation ← abs(subject_severity - severity_mean)
    extremity_score ← min(subject_deviation / 0.40, 1.0) × 10  # Cap at 0.40

    # Weighted sum
    asymmetry_score ← (
      range_score × 0.40 +
      variance_score × 0.30 +
      extremity_score × 0.30
    )

    # Apply bonus: If subject is BOTH extreme AND outlier direction matters
    IF subject_severity > severity_mean:  # Subject treated MORE severely
      IF subject_severity > (severity_mean + 2×stddev):
        asymmetry_score ← min(asymmetry_score + 1.5, 10.0)  # Bonus outlier
    ELSE:  # Subject treated LESS severely (clémence)
      IF subject_severity < (severity_mean - 2×stddev):
        asymmetry_score ← min(asymmetry_score + 1.5, 10.0)  # Bonus outlier

    # Round to 1 decimal
    → round(asymmetry_score, 1)

  EXAMPLES:
    # Case 1: ARCOM CNews vs TF1/LCI/BFM
    # CNews: severity 0.85 (20k€ inédite + 52 sanctions)
    # TF1/LCI/BFM: severity mean 0.30 (sanctions légères)
    # range: 0.55, variance: 0.12, deviation: 0.55
    # → asymmetry_score = 8.2 (EXTREME)

    # Case 2: EU fines homogènes
    # All companies: severity 0.60-0.65
    # range: 0.05, variance: 0.001, deviation: 0.02
    # → asymmetry_score = 1.3 (MINIMAL)
```

---

## Integration Points

### kb/INVESTIGATION_TREE.md

**§1 DÉCLENCHEMENT:**
- Add `@TRIGGER[COMPARABLES_LAUNCH]` (3 trigger paths: regulatory context, Ξ≥8, mid-tree reactive)

**§2 SCORING BRANCHES:**
- Add COMPARABLES case to `@F[EDI_IMPACT]` → 0.35
- Add COMPARABLES case to `@F[CUI_BONO_CENTRALITY]` → 0.25 (regulatory) / 0.15 (generic)

**§3 SOUS-AGENT LIFECYCLE:**
- Update `BRANCH.type` enum: add `| COMPARABLES`
- Add `comparables_found[]` to `results` structure

**§5 SYNTHÈSE FINALE:**
- Add new subsection **5.6 Asymmetries (△ differential)**
- Add `DETECT_ASYMMETRY` operation (full spec above)
- Add `@F[ASYMMETRY_SCORE]` formula (0-10 scale)

**§6 FORMATS OUTPUT:**
- Update Mermaid generation: Add `△ asymmetry` edges between subject and comparables
- Update JSON export: Include `asymmetry_analysis` in synthesis

### kb/VALIDATION.md

**§7 BRANCH SCORING:**
- Add subsection 7.5: COMPARABLES Detection & Scoring
- Document trigger conditions (regulatory context, Ξ≥8, mid-tree)
- Document scoring (edi_impact 0.35, cui_bono 0.25)

### system.md

**§INVESTIGATION_TREE:**
- Update branch types list: 6 types (add COMPARABLES)
- Add asymmetry synthesis operation to workflow description

---

## Success Criteria

**Branch-level success:**
- ✅ CONVERGED: ≥2 comparables found with context_similarity ≥0.60
- ✅ EXHAUSTED: 3 consecutive failures, <2 comparables found

**Synthesis-level success:**
- ✅ Asymmetry measurable: asymmetry_score calculated (0-10)
- ✅ Verdict assigned: EXTREME (≥7.0) | SIGNIFICANT (≥5.0) | MODERATE (≥3.0) | MINIMAL (<3.0)
- ❌ INSUFFICIENT_DATA: <2 comparables (synthesis skipped)

---

## Example Workflow

**Test case:** "ARCOM amende CNews 20k€ désinformation climatique"

```yaml
# I0 APEX detection
i0_state:
  complexity: 9.0
  patterns:
    Ξ: 8.5  # OMISSION pattern detected
    Λ: 7.2  # FRAMING pattern
  regulatory_context: true  # ARCOM = media regulator
  sanctions_detected: 1  # CNews 20k€

# TRIGGER COMPARABLES
@TRIGGER[COMPARABLES_LAUNCH]:
  Path A: regulatory_context=true AND sanctions_detected>0 → ✅ TRIGGER

# BRANCH b5_comparables_arcom launched
BRANCH:
  id: "b5_comparables_arcom_cnews"
  type: COMPARABLES
  objective: "Find comparable cases ARCOM 2020-2024 media sanctions similar infraction context"
  score:
    edi_impact: 0.35
    cui_bono_centrality: 0.25
    priority: 0.30

  results:
    comparables_found:
      - case_id: "TF1_2020_2024"
        entity: "TF1"
        regulatory_action: "7 sanctions légères ARCOM"
        severity: 0.25
        context_similarity: 0.75
      - case_id: "LCI_2020_2024"
        entity: "LCI"
        regulatory_action: "3 sanctions mineures"
        severity: 0.20
        context_similarity: 0.70
      - case_id: "BFM_2020_2024"
        entity: "BFM TV"
        regulatory_action: "5 sanctions modérées"
        severity: 0.30
        context_similarity: 0.72
      - case_id: "CNEWS_2020_2024"
        entity: "CNews (Bolloré)"
        regulatory_action: "52 sanctions + 20k€ inédite"
        severity: 0.85
        context_similarity: 1.0  # Subject itself

  status: CONVERGED  # ≥2 comparables found ✅

# SYNTHESIS DETECT_ASYMMETRY
asymmetry_analysis:
  asymmetry_score: 8.2
  verdict: "ASYMMETRY_EXTREME (differential treatment flagrant)"
  comparables: [TF1, LCI, BFM, CNews]
  severity_stats:
    mean: 0.40
    variance: 0.089
    range: 0.65  # 0.85 - 0.20
  subject_position: "ABOVE_AVERAGE (CNews severity 0.85 >> mean 0.40)"

# OUTPUT (Part 1 French)
### Asymétries Détectées

**Comparables ARCOM 2020-2024:**
- TF1: 7 sanctions légères (severity 0.25)
- LCI: 3 sanctions mineures (severity 0.20)
- BFM: 5 sanctions modérées (severity 0.30)
- **CNews (Bolloré): 52 sanctions + 20k€ inédite (severity 0.85)**

**△ Asymétrie:** 8.2/10 — EXTREME (differential treatment flagrant)

CNews traité **2.8× plus sévèrement** que moyenne concurrents (0.85 vs 0.25).
Range 0.65 = variance maximale entre entités comparables.

**Ξ OMISSION révélé:** Clémence TF1/LCI/BFM vs rigueur CNews absente narratifs mainstream.
```

---

## Output Integration

### Part 1 (French natural language)

Add new subsection after "Contradictions":

```markdown
### Asymétries △

**{N} comparables trouvés:** {regulator} {time_window}

| Entité | Action régulatrice | Severity | Context similarity |
|--------|-------------------|----------|-------------------|
| {entity1} | {action1} | {severity1} | {similarity1} |
| **{subject}** | {action_subject} | **{severity_subject}** | 1.0 |

**△ Asymmetry Score:** {score}/10 — {verdict}

{subject} traité **{ratio}× {direction}** que moyenne ({severity_subject} vs {mean}).

**Ξ OMISSION révélé:** {omission_description}
```

### Part 2 (Diagnostics)

Add to `[SYNTHESIS]` section:

```
[ASYMMETRY] △{asymmetry_score}/10 ({verdict}) — {N} comparables
```

### Part 3 (WOLF)

If COMPARABLES branch converged, add subsection:

```markdown
### Asymétries Institutionnelles

**Régulateur:** {regulator_name}
**Comparables:** {N} entités, time window {years}
**Asymmetry:** {score}/10 ({verdict})

**Cui bono differential treatment?**
- Hypothesis: {cui_bono_analysis based on asymmetry direction}
```

---

## Validation Test

**File:** `tests/tree/test_comparables_asymmetry.md`

**Test case:** "ARCOM CNews 20k€ inédite désinformation climatique"

**Expected behavior:**
- Complexity 9.0 → APEX triggered
- Ξ OMISSION ≥8 → COMPARABLES branch launched
- Branch b5_comparables finds: TF1, LCI, BFM cases
- DETECT_ASYMMETRY: asymmetry_score 8.2/10 (EXTREME)
- Output includes △ asymmetries section with comparative table

---

## Version Update

**Investigation Tree:** v1.0 → v1.1
**Branch types:** 5 → 6 (add COMPARABLES)
**Synthesis operations:** 5 → 6 (add DETECT_ASYMMETRY)
**Formulas:** +2 (@F[ASYMMETRY_SCORE], COMPARABLES cases in EDI_IMPACT/CUI_BONO)

---

**Status:** Design complete ✅
**Next:** Integration into kb/INVESTIGATION_TREE.md, kb/VALIDATION.md, system.md
**Validation:** Create test_comparables_asymmetry.md + validation script
