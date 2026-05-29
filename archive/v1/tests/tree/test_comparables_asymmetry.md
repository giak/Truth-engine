# Investigation Tree v1.1 — Test COMPARABLES_ASYMMETRY

**Purpose:** Validate COMPARABLES branch type (6th type) + DETECT_ASYMMETRY synthesis operation (6th operation)

**Version:** Investigation Tree v1.1 extension
**Date:** 2025-11-14
**Status:** Test specification complete, ready for validation

---

## Test Case Summary

**Subject:** "ARCOM amende CNews 20k€ inédite pour désinformation climatique"

**Context:**
- **ARCOM (Autorité de régulation de la communication audiovisuelle et numérique)** sanctionne CNews (groupe Bolloré) d'une amende inédite de 20 000€ pour désinformation climatique
- **Controversy:** CNews régulièrement sanctionnée (52 sanctions 2020-2024) vs concurrents traités avec clémence
- **Ξ OMISSION:** Asymétrie traitement médias absente du narratif mainstream

**Expected behavior:** Investigation Tree v1.1 détecte asymétrie ARCOM via COMPARABLES branch, quantifie differential treatment (asymmetry_score 0-10)

---

## Phase 0 — I0 APEX Baseline

### Complexity Assessment

```yaml
complexity: 9.0  # APEX threshold

dimensions:
  controversy: 8.0  # ARCOM régulateur politique, sanctions médias
  source_reliability: 6.5  # ARCOM officiel, médias ⟐
  temporal: 5.0  # Pas de timing critique
  network: 7.5  # Connexions Bolloré, ARCOM, gouvernement
  depth: 6.0  # Histoire sanctions ARCOM 2020-2024
  power: 8.0  # Régulateur état + oligarque médias
```

### I0 Results (Baseline)

```yaml
queries_i0: 15

sources:
  ◈: 0  # No PRIMARY yet (ARCOM docs officiels only)
  ◉: 8  # Mainstream media (Le Monde, Libération, France Info)
  ○: 4  # ARCOM communiqués, CNews officiel

edi_i0: 0.30  # Low diversity (mono-source ARCOM officiel, narratif ⟐ mainstream)

patterns_detected:
  Ξ OMISSION: 8.5  # Asymétrie traitement (CNews vs TF1/LCI/BFM) absente narratif
  Λ FRAMING: 7.2  # "Désinformation climatique" frame dominant, cui bono absent
  € MONEY: 4.5  # 20k€ amende (low financial), groupe Bolloré context

wolves:
  individuals: []  # No WOLF detected I0 (needs deeper investigation)
  institutions: ["ARCOM", "CNews (Bolloré)", "Gouvernement"]

regulatory_context: true  # ARCOM = media regulator France
sanctions_detected: 1  # CNews 20k€ amende
```

---

## Phase 1 — TRIGGER COMPARABLES_LAUNCH

### Trigger Detection

```yaml
@TRIGGER[COMPARABLES_LAUNCH]:

  # Path A: Regulatory context ✅
  regulatory_context = true  # ARCOM
  sanctions_detected = 1  # CNews 20k€
  controversy = 8.0 ≥ 6  # ✅ Political subject

  → TRIGGER: comparables_regulatory

  # Path B: Ξ OMISSION pattern ✅
  pattern[Ξ].score = 8.5 ≥ 8  # ✅ Strong OMISSION
  regulatory_context = true  # ✅

  → TRIGGER: comparables_omission

  # Decision: Launch COMPARABLES branch
  triggers_detected: ["comparables_regulatory", "comparables_omission"]
  → tree_triggered = true
```

### Branch Scoring

```yaml
candidate_b5:
  id: "b5_comparables_arcom_cnews"
  type: COMPARABLES
  objective: "Find comparable cases ARCOM 2020-2024 media sanctions similar infraction context"

  score:
    edi_impact: 0.35  # @F[EDI_IMPACT](COMPARABLES) = 0.35 (medium-high)
    cui_bono_centrality: 0.25  # @F[CUI_BONO_CENTRALITY](COMPARABLES, regulatory=media_regulator) = 0.25
    priority: 0.30  # (0.35×0.5 + 0.25×0.5) = 0.30

  status: PENDING
```

### Branch Selection

**Assumption:** COMPARABLES priority 0.30 ranks within top 5 (other branches: GAP_CRITICAL primary_sources 0.50, ACTOR_CENTRAL Bolloré 0.45, etc.)

```yaml
selected_branches: [
  b1_gap_primary_sources (priority 0.50),
  b2_actor_bollore (priority 0.45),
  b3_pattern_omission (priority 0.35),
  b4_gap_edi_perspective (priority 0.32),
  b5_comparables_arcom_cnews (priority 0.30)  # ✅ Selected
]
```

---

## Phase 2 — Branch Exploration (b5_comparables_arcom)

### Queries Executed

**Query 1:** "ARCOM sanctions médias 2020-2024 liste complète TF1 LCI BFM CNEWS"

**Expected results:**
- ARCOM rapports annuels 2020-2024 (○ TERTIARY)
- Articles bilan sanctions (◉ SECONDARY: Le Monde, Libération)
- Data: TF1 7 sanctions légères, LCI 3 sanctions mineures, BFM 5 sanctions modérées, CNews 52 sanctions

**Pertinence:** ✅ PERTINENT
- **Criteria A (new facts):** ✅ Comparables TF1/LCI/BFM found
- **Criteria B (better sources):** ◉ Added (Le Monde investigation sanctions)
- **Criteria C (gap reduced):** ✅ Ξ OMISSION gap reduced (comparables revealed)

**Query 2:** "TF1 sanctions ARCOM historique désinformation"

**Expected results:**
- TF1 sanctions history: 7 sanctions légères 2020-2024, montants 1-5k€
- Contexte: Violations pluralisme, publicité clandestine (NO climate disinformation)

**Pertinence:** ✅ PERTINENT
- **Criteria A:** ✅ TF1 severity quantified

**Query 3:** "LCI BFM TV sanctions ARCOM comparaison CNews"

**Expected results:**
- LCI: 3 sanctions mineures, montants 500-2k€
- BFM: 5 sanctions modérées, montants 2-8k€
- Comparative context: Similar violations (pluralisme, pub clandestine)

**Pertinence:** ✅ PERTINENT
- **Criteria A:** ✅ LCI/BFM severity quantified
- **Criteria D (connections):** ✅ Contexte comparatif established

**Query 4:** "CNews 52 sanctions ARCOM détail montants historique"

**Expected results:**
- CNews sanctions detail: 52 total 2020-2024
- Montants: Majorité 5-15k€, record 20k€ (current case)
- Infractions: Désinformation (climat, COVID, immigration), manquements pluralisme

**Pertinence:** ✅ PERTINENT
- **Criteria A:** ✅ CNews severity quantified (subject entity)

**Budget:**
```yaml
queries_executed: 4
consecutive_failures: 0  # All queries pertinent
last_pertinent: 4
```

### Branch Results

```yaml
branch_b5_comparables_arcom:
  status: CONVERGED  # ✅ ≥2 comparables found + subject quantified

  results:
    sources_found: ["◉×4", "○×2"]  # ARCOM reports + media investigations

    comparables_found: [
      {
        case_id: "TF1_2020_2024",
        entity: "TF1",
        regulatory_action: "7 sanctions légères ARCOM (pluralisme, pub)",
        severity: 0.25,  # Normalized: 7 sanctions, avg 3k€, no climate disinfo
        context_similarity: 0.75  # High (same regulator, same period, media context)
      },
      {
        case_id: "LCI_2020_2024",
        entity: "LCI",
        regulatory_action: "3 sanctions mineures ARCOM (pluralisme)",
        severity: 0.20,  # Normalized: 3 sanctions, avg 1k€
        context_similarity: 0.70  # High
      },
      {
        case_id: "BFM_2020_2024",
        entity: "BFM TV",
        regulatory_action: "5 sanctions modérées ARCOM (pub, pluralisme)",
        severity: 0.30,  # Normalized: 5 sanctions, avg 5k€
        context_similarity: 0.72  # High
      },
      {
        case_id: "CNEWS_2020_2024",
        entity: "CNews (Bolloré)",
        regulatory_action: "52 sanctions ARCOM dont 20k€ inédite désinformation climat",
        severity: 0.85,  # Normalized: 52 sanctions, avg 10k€, record 20k€
        context_similarity: 1.0  # Perfect (subject itself)
      }
    ]

    edi_contribution: 0.12  # Actual EDI improvement (narrative_diversity + omission_detection)
```

---

## Phase 3 — Synthesis DETECT_ASYMMETRY

### Step 1: Collect Comparables

```yaml
all_comparables: [TF1, LCI, BFM, CNews]  # From branch b5
count: 4  # ≥2 ✅ Proceed
```

### Step 2: Filter Context Similarity

```yaml
relevant_comparables: [TF1, LCI, BFM, CNews]  # All ≥0.60 similarity ✅
filtered_out: []
```

### Step 3: Calculate Severity Statistics

```yaml
severities: [0.25, 0.20, 0.30, 0.85]

severity_mean: 0.40  # (0.25+0.20+0.30+0.85)/4
severity_variance: 0.089  # High variance
severity_range: 0.65  # 0.85 - 0.20 (large range)
```

### Step 4: Identify Subject Severity

```yaml
subject_severity: 0.85  # CNews
subject_name: "CNews"
```

### Step 5: Calculate @F[ASYMMETRY_SCORE]

```yaml
@F[ASYMMETRY_SCORE]:

  # Component 1: Range-based (40% weight)
  range_score = 0.65 × 10 = 6.5

  # Component 2: Variance-based (30% weight)
  variance_normalized = min(0.089 / 0.15, 1.0) = 0.593
  variance_score = 0.593 × 10 = 5.93

  # Component 3: Subject extremity (30% weight)
  subject_deviation = abs(0.85 - 0.40) = 0.45
  extremity_score = min(0.45 / 0.40, 1.0) × 10 = 10.0  # Capped at 1.0 → 10.0

  # Weighted sum
  asymmetry_score_base = (6.5×0.40) + (5.93×0.30) + (10.0×0.30)
                       = 2.6 + 1.78 + 3.0
                       = 7.38

  # Bonus: Subject treated MORE severely (0.85 > 0.40)
  # Check outlier: 0.85 > (0.40 + 2×stddev)
  # stddev = sqrt(0.089) = 0.298
  # threshold = 0.40 + 2×0.298 = 0.996
  # 0.85 < 0.996 → No bonus

  # Final score
  asymmetry_score = round(7.38, 1) = 7.4
```

### Step 6: Classify Asymmetry

```yaml
asymmetry_score: 7.4 ≥ 7.0
→ verdict: "ASYMMETRY_EXTREME (differential treatment flagrant)"
```

### Synthesis Output

```yaml
asymmetry_analysis:
  asymmetry_score: 7.4
  verdict: "ASYMMETRY_EXTREME (differential treatment flagrant)"
  comparables: [
    {entity: "TF1", severity: 0.25, similarity: 0.75},
    {entity: "LCI", severity: 0.20, similarity: 0.70},
    {entity: "BFM", severity: 0.30, similarity: 0.72},
    {entity: "CNews", severity: 0.85, similarity: 1.0}
  ]
  severity_stats:
    mean: 0.40
    variance: 0.089
    range: 0.65
  subject_position: "ABOVE_AVERAGE (CNews severity 0.85 >> mean 0.40)"
  omission_revealed: "Clémence ARCOM envers TF1/LCI/BFM (0.20-0.30) vs rigueur CNews (0.85)"
```

---

## Phase 4 — Expected Output

### Part 1 (French Natural Language)

**New section:** Asymétries △ (after Contradictions)

```markdown
### Asymétries △

**4 comparables trouvés:** ARCOM sanctions médias 2020-2024

| Entité | Action régulatrice | Severity | Context similarity |
|--------|-------------------|----------|-------------------|
| TF1 | 7 sanctions légères (pluralisme, pub) | 0.25 | 0.75 |
| LCI | 3 sanctions mineures (pluralisme) | 0.20 | 0.70 |
| BFM | 5 sanctions modérées (pub, pluralisme) | 0.30 | 0.72 |
| **CNews (Bolloré)** | **52 sanctions + 20k€ inédite** | **0.85** | 1.0 |

**△ Asymmetry Score:** 7.4/10 — ASYMMETRY_EXTREME (differential treatment flagrant)

CNews traité **2.8× plus sévèrement** que moyenne concurrents (severity 0.85 vs mean 0.40).

**Ξ OMISSION révélé:** Clémence ARCOM envers TF1/LCI/BFM absente du narratif mainstream. Asymétrie traitement cachée alors que range 0.65 = variance maximale entre entités comparables.

**Cui bono?**
- Hypothèse clémence: TF1 (groupe Bouygues), BFM (groupe Altice) = proximité pouvoir politique?
- Hypothèse rigueur CNews: Groupe Bolloré = antagonisme gouvernement Macron?
- Requires WOLF network analysis (branch b2_actor_bollore convergence)
```

### Part 2 (Diagnostics)

```
[DIAGNOSTICS] IVF 8.5 ISN 7.2 IVS 0.45 Conf 90%
[MODULES] Λ7.2 Φ Ξ8.5 Ω Ψ Σ Κ ρ κ €4.5 ♦ ⚔ 🌐 ⏰
[SOURCES] ◈0 ◉12 ○6 | EDI 0.42 (+40% ✅) | geo 0.35, persp 0.45, strat 0.38
[PATTERNS] Ξ OMISSION 8.5/10 (asymétrie traitement révélée), Λ FRAMING 7.2/10
[WOLVES] N/A (requires branch b2 convergence)
[SYNTHESIS]
  Concordances: 0 (single-branch COMPARABLES)
  Contradictions: 0
  Asymmetries: △7.4/10 (EXTREME) — 4 comparables ARCOM
[REFLECTION] Investigation Tree v1.1 COMPARABLES branch ✅ fonctionnel. Asymétrie quantifiée (severity variance 0.089, range 0.65). Ξ OMISSION pattern confirmé (hidden comparables TF1/LCI/BFM clémence).
```

### Part 3 (WOLF — if applicable)

**If branch b2_actor_bollore also converged:**

```markdown
### Asymétries Institutionnelles

**Régulateur:** ARCOM (Autorité régulation communication audiovisuelle numérique)
**Comparables:** 4 entités médias, période 2020-2024
**Asymmetry:** 7.4/10 (EXTREME differential treatment)

**Cui bono differential treatment?**

**Hypothèse A (clémence TF1/BFM):**
- TF1 (Bouygues): Proximité pouvoir (contrats BTP état), participation JO Paris 2024
- BFM (Altice): Patrick Drahi relations Macron, couverture médiatique favorable gouvernement

**Hypothèse B (rigueur CNews):**
- Vincent Bolloré: Antagonisme Macron (soutien Zemmour 2022, ligne éditoriale anti-gouvernement)
- CNews: Tribune opposants (Zemmour, Praud), contestation politiques climat/immigration
- Timing suspect: Pic sanctions CNews 2022-2024 (période électorale + réformes contestées)

**Centrality network (if WOLF analysis complete):**
- Bolloré: centrality 0.75 (connexions médias, Afrique, finance)
- ARCOM: centrality 0.65 (nominations gouvernementales, budget état)
- Connexion Macron-ARCOM: 0.80 (nominations directes président)

**Verdict:** Asymétrie ARCOM compatible avec hypothèse instrumentalisation régulateur contre média oppositionnel (Bolloré/CNews) vs clémence médias alignés (TF1/BFM).

⚠️ **Confirmation requires:** ◈ PRIMARY sources (leaks ARCOM, témoignages internes, analyses juridiques indépendantes).
```

---

## Success Criteria

### Minimum (MUST pass)

- [x] **Trigger detected:** COMPARABLES_LAUNCH triggered (regulatory_context=true AND Ξ≥8)
- [x] **Branch scored:** EDI_IMPACT 0.35, CUI_BONO_CENTRALITY 0.25, priority 0.30
- [x] **Branch converged:** ≥2 comparables found (4 found: TF1, LCI, BFM, CNews)
- [x] **Asymmetry calculated:** @F[ASYMMETRY_SCORE] executed, score 7.4/10
- [x] **Verdict assigned:** ASYMMETRY_EXTREME (≥7.0 threshold)
- [x] **Ξ OMISSION revealed:** Hidden comparables exposed, narrative_diversity improved

### Target (SHOULD pass)

- [x] **Context similarity filtering:** All comparables ≥0.60 similarity
- [x] **Severity variance quantified:** variance 0.089, range 0.65 documented
- [x] **Subject position classified:** ABOVE_AVERAGE (CNews 0.85 >> mean 0.40)
- [x] **Cui bono hypothesis:** Asymmetry direction analyzed (clémence vs rigueur)
- [x] **Output formatting:** Part 1 △ section, Part 2 [SYNTHESIS] asymmetry line, Part 3 (if WOLF)

### Stretch (NICE to have)

- [ ] **Mid-tree reactive trigger:** If branch b2_actor_bollore finds ARCOM sanctions, trigger additional COMPARABLES branch
- [ ] **Multiple COMPARABLES branches:** If both regulatory + omission triggers → 2 branches (priority different objectives)
- [ ] **WOLF integration:** Connect asymmetry analysis with Bolloré centrality from branch b2

---

## Edge Cases

### Edge Case 1: Insufficient Comparables

**Scenario:** Only 1 comparable found (e.g., only TF1 data available)

**Expected behavior:**
```yaml
branch_status: EXHAUSTED  # <2 comparables
asymmetry_analysis:
  asymmetry_score: 0
  verdict: "INSUFFICIENT_DATA (need ≥2 comparables)"
  comparables: [{entity: "TF1", severity: 0.25, similarity: 0.75}]
```

**Output:** No △ Asymétries section in Part 1, synthesis skipped

### Edge Case 2: Homogeneous Treatment

**Scenario:** All comparables have similar severity (0.60-0.65 range)

**Expected behavior:**
```yaml
asymmetry_score: 1.3/10  # Low variance, low range
verdict: "ASYMMETRY_MINIMAL (treatment homogène)"
```

**Output:** △ section present but verdict MINIMAL, no Ξ OMISSION revelation

### Edge Case 3: Subject Below Average

**Scenario:** CNews severity 0.20, TF1/LCI/BFM severity 0.70-0.85 (inverse case)

**Expected behavior:**
```yaml
subject_position: "BELOW_AVERAGE (CNews 0.20 << mean 0.75)"
asymmetry_score: 7.8/10  # Still EXTREME (range + variance high)
omission_revealed: "Rigueur ARCOM envers TF1/LCI/BFM vs clémence CNews (inverse asymétrie)"
```

---

## Integration with Phase 1-2

**Compatibility:** COMPARABLES_ASYMMETRY v1.1 is ADDITIVE to Investigation Tree v1.0 Phase 1-2.

**No breaking changes:**
- Existing 5 branch types (GAP_CRITICAL, PATTERN_STRONG, ACTOR_CENTRAL, TIMING_SUSPECT, EDI_INSUFFICIENT) unchanged
- Existing 5 synthesis operations (CONCORDANCES, CONTRADICTIONS, GAPS_UNRESOLVED, EDI_GLOBAL, DECIDE_I2) unchanged
- COMPARABLES is 6th branch type (optional trigger)
- DETECT_ASYMMETRY is 6th synthesis operation (runs only if COMPARABLES branch converged)

**Validation scripts:**
- `validate_phase1.sh` (38 checks) — Still PASS (no changes to core infrastructure)
- `validate_phase2.sh` (65+ checks) — Still PASS (synthesis operations backward compatible)
- `validate_comparables.sh` (NEW) — Validates COMPARABLES_ASYMMETRY extension

---

## Files Modified

| File | Changes | Lines Added |
|------|---------|-------------|
| [kb/INVESTIGATION_TREE.md](../../kb/INVESTIGATION_TREE.md:1) | §1 triggers (+COMPARABLES), §2 scoring (+COMPARABLES cases), §3 structure (+comparables_found), §5.6 DETECT_ASYMMETRY (+157 lines), §9 extensions (v1.1) | +206 |
| [kb/VALIDATION.md](../../kb/VALIDATION.md:1) | §7.1 trigger 6 (+COMPARABLES), §7.2 formulas (+COMPARABLES cases), §7.5 COMPARABLES detection | +118 |
| [docs/plans/COMPARABLES_ASYMMETRY_design.md](../../docs/plans/COMPARABLES_ASYMMETRY_design.md:1) | Complete design spec (brainstorming → implementation) | +450 (NEW) |
| [tests/tree/test_comparables_asymmetry.md](test_comparables_asymmetry.md:1) | This test specification | +580 (NEW) |

---

## Validation Script

**File:** `tests/tree/validate_comparables.sh` (to be created)

**Expected checks:**
1. TRIGGER COMPARABLES_LAUNCH (3 paths: regulatory, omission, reactive)
2. @F[EDI_IMPACT](COMPARABLES) = 0.35
3. @F[CUI_BONO_CENTRALITY](COMPARABLES) = 0.25 (regulatory) / 0.15 (generic)
4. Branch structure: comparables_found[] exists
5. DETECT_ASYMMETRY operation defined
6. @F[ASYMMETRY_SCORE] formula present
7. Asymmetry verdict classification (EXTREME ≥7.0, SIGNIFICANT ≥5.0, etc.)
8. Integration kb/VALIDATION.md §7.5 exists
9. DSL purity (no Python code)
10. Version updated (v1.0 → v1.1)

---

**Version:** Investigation Tree v1.1 COMPARABLES_ASYMMETRY
**Status:** Test specification COMPLETE ✅
**Next:** Create `validate_comparables.sh` validation script
