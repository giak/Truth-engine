# INVESTIGATION TREE v1.0 — APEX Multi-Agent Architecture

> **NOTE:** Ce fichier décrit l'exploration par branches parallèles multi-agents.
> Pour le protocole L0-L6 séquentiel (SPG cascade), voir INVESTIGATION.md.
> KERNEL.md §5 référence les deux fichiers.

**Purpose:** Extension Truth Engine v8.2 pour investigations APEX (complexity ≥9.0) nécessitant exploration arborescente multi-pistes.

**Activation:** Automatique si complexity ≥9.0 (politique + géopolitique + corporate + conspiracy)

**Usage:** Référencé par KERNEL.md §5 et INVESTIGATION.md.

**Version:** 1.0 (2025-11-14)

---

## §1 — DÉCLENCHEMENT (post I0 APEX)

Investigation Tree activé si I0 APEX détecte **≥1 trigger** :

### @TRIGGER[TREE_LAUNCH]

```yaml
TREE_ACTIVATION:
  INPUT: i0_state (complexity, EDI, sources, patterns, wolves, timing)
  OUTPUT: tree_triggered (true/false)

  IF complexity < 9.0:
    → tree_triggered = false  # LINEAR workflow preserved

  ELSE IF complexity ≥ 9.0:
    # Check triggers (Option F all)
    triggers_detected ← []

    # Trigger 1: GAPS_CRITICAL
    IF ◈_current < ◈_target:
      triggers_detected.append("gap_primary_sources")

    IF any(edi_dimension < 0.30 FOR dimension IN edi_dimensions):
      triggers_detected.append("gap_edi_dimension")

    # Trigger 2: PATTERNS_STRONG
    IF any(pattern.score ≥ 8 FOR pattern IN [Κ, Ξ, Ω]):
      triggers_detected.append("pattern_strong")

    # Trigger 3: ACTORS_WOLF_CENTRAL
    IF any(actor.centrality ≥ 0.70 FOR actor IN wolves.individuals):
      triggers_detected.append("actor_central")

    # Trigger 4: TIMING_SUSPECT
    IF timing_suspicion_prob < 0.01:
      triggers_detected.append("timing_suspect")

    # Trigger 5: EDI_INSUFFICIENT
    IF edi_current < edi_target:
      triggers_detected.append("edi_insufficient")

    # Trigger 6: COMPARABLES (regulatory asymmetries)
    IF regulatory_context = true:  # ARCOM, EU Commission, SEC, FDA, etc.
      IF sanctions_detected > 0 OR controversy ≥ 6:
        triggers_detected.append("comparables_regulatory")

    IF any(pattern.score ≥ 8 FOR pattern IN [Ξ]):  # OMISSION pattern
      IF "differential_treatment" IN omission_signals OR regulatory_context = true:
        triggers_detected.append("comparables_omission")

    IF count(triggers_detected) > 0:
      → tree_triggered = true
    ELSE:
      → tree_triggered = false

  RETURN: tree_triggered
```

### Triggers Détaillés

```yaml
GAPS_CRITICAL:
  - ◈ PRIMARY < target (ex: ◈0 pour APEX target ◈≥3)
  - Document clé introuvable (ex: Budget Shield 200M€ après 5+ queries)
  - Source type manquante (ex: 0 dissidents, 0 whistleblowers)
  - EDI dimension <0.30 (mono-perspective, mono-géographique)

PATTERNS_STRONG:
  - Κ CONSPIRACY ≥8/10
  - Ξ OMISSION ≥8/10
  - Ω INVERSION ≥8/10
  - Timing suspect (événements synchronisés <72h, prob coïncidence <10%)

ACTORS_WOLF_CENTRAL:
  - ≥8 acteurs politiques identifiés
  - Acteur centrality ≥0.70 (cui bono network)
  - Chronologie incomplète acteur clé
  - Réseau pouvoir détecté mais non cartographié

EDI_INSUFFICIENT:
  - EDI < target (ex: 0.30 << 0.80 APEX)
  - geo_diversity <0.40
  - perspective_diversity <0.30 (mono-perspective)
  - Lang_diversity <0.30 (sources langue native uniquement)

COMPARABLES_REGULATORY:
  - Regulatory context detected (ARCOM, EU Commission, SEC, FDA, central banks)
  - Sanctions/actions detected (≥1 regulatory action identified)
  - Controversy ≥6 (political/institutional subject)
  - Ξ OMISSION ≥8 (differential treatment signals)
  - Comparable cases NOT yet searched (avoid redundancy)
```

---

## §2 — SCORING BRANCHES (B+C Prioritization)

### @F[BRANCH_PRIORITY]

**Formula :**
```yaml
@F[BRANCH_PRIORITY]:
  # Core formula (0.0-1.0 range)
  priority ← edi_impact × 0.5 + cui_bono_centrality × 0.5
```

### @F[EDI_IMPACT]

**Estimation amélioration EDI si branche succès (0.0-1.0) :**

```yaml
@F[EDI_IMPACT]:
  INPUT: branch_type, i0_state
  OUTPUT: edi_impact (0.0-1.0)

  HEURISTIC:

    IF branch_type = "gap_primary_sources":
      → 0.50  # Trouver ◈ améliore strat_diversity fortement

    ELSE IF branch_type = "gap_dissident_sources":
      → 0.40  # Améliore perspective + geo diversity

    ELSE IF branch_type = "gap_edi_dimension":
      dimension ← extract_dimension(branch.id)
      current ← edi_dimensions[dimension]
      → max(0.40, 0.60 - current)  # Inverse proportional

    ELSE IF branch_type = "pattern_strong":
      → 0.25  # Medium impact (temporal + narrative diversity)

    ELSE IF branch_type = "actor_chronology":
      → 0.20  # Medium-low impact (temporal_diversity)

    ELSE IF branch_type = "timing_context":
      → 0.25  # Medium impact (temporal + causal analysis)

    ELSE IF branch_type = "edi_global_boost":
      → edi_target - edi_current  # Direct delta

    ELSE IF branch_type = "comparables":
      → 0.35  # Medium-high impact (narrative diversity + Ξ OMISSION revelation)

    ELSE:
      → 0.15  # Default baseline
```

### @F[CUI_BONO_CENTRALITY]

**Importance acteur WOLF network (0.0-1.0) :**

```yaml
@F[CUI_BONO_CENTRALITY]:
  INPUT: branch, i0_state
  OUTPUT: cui_bono_centrality (0.0-1.0)

  HEURISTIC:

    IF branch.type = "actor_central":
      actor_name ← extract_actor_name(branch.objective)
      actor_data ← find_in_wolves(actor_name, i0_state.wolves.individuals)

      IF actor_data EXISTS:
        → actor_data.centrality  # Actual centrality score
      ELSE:
        → 0.35  # Default medium-high (benefit of doubt)

    ELSE IF branch.type = "pattern_strong":
      pattern ← extract_pattern(branch.id)

      IF pattern IN [€, ♦, ⚔, 🌐]:
        → 0.30  # Power/network patterns = medium centrality
      ELSE:
        → 0.15  # Other patterns = low centrality

    ELSE IF branch.type = "gap_critical":
      IF "actor" IN branch.objective.lower() OR "connection" IN branch.objective.lower():
        → 0.25  # Actor-related gaps = medium-low
      ELSE:
        → 0.10  # Generic gaps = low

    ELSE IF branch.type = "timing_suspect":
      → 0.20  # Timing often reveals cui_bono

    ELSE IF branch.type = "comparables":
      IF regulatory_context IN ["media_regulator", "competition_authority", "central_bank"]:
        → 0.25  # Medium-low (institutional power, not individual actors)
      ELSE:
        → 0.15  # Low (generic comparables)

    ELSE:
      → 0.10  # Default baseline

  # Calcul alternatif (si WOLF network disponible):
  # centrality ← wolf_connections_count / max_connections
  # Ex: von_der_leyen 12 connexions / 15 max = 0.80
```

### BRANCH_SELECTION

**Sélection top 3-5 branches prioritaires :**

```yaml
BRANCH_SELECTION:
  INPUT: triggers_detected[], i0_state
  INPUT: max_branches (default: 5, typical range: 3-5)
  OUTPUT: selected_branches[] (top priority)

  # Step 1: Detect all potential branches
  candidates ← detect_potential_branches(triggers_detected, i0_state)
  # Typical: 10-15 candidates

  # Step 2: Score each branch
  scored_branches ← []
  FOR each candidate IN candidates:
    edi_impact ← @F[EDI_IMPACT](candidate, i0_state)
    cui_bono ← @F[CUI_BONO_CENTRALITY](candidate, i0_state)
    priority ← @F[BRANCH_PRIORITY](edi_impact, cui_bono)

    candidate.score ← {
      edi_impact: edi_impact,
      cui_bono_centrality: cui_bono,
      priority: priority
    }

    scored_branches.append(candidate)

  # Step 3: Select top-k
  sorted_branches ← ORDER_BY(scored_branches, key=priority, direction=DESC)
  selected_branches ← sorted_branches[0:max_branches]

  RETURN: selected_branches
```

---

## §3 — SOUS-AGENT LIFECYCLE

### Structure Branche

```yaml
BRANCH:
  id: "b{n}_{type}_{topic}"          # Ex: b1_gap_sources_primaires
  parent: "i0_root"
  type: GAP_CRITICAL | PATTERN_STRONG | ACTOR_CENTRAL | TIMING_SUSPECT | EDI_INSUFFICIENT | COMPARABLES
  objective: "Question spécifique à résoudre"

  score:
    edi_impact: 0.0-1.0              # Estimated EDI contribution
    cui_bono_centrality: 0.0-1.0     # WOLF network importance
    priority: 0.0-1.0                # edi_impact×0.5 + cui_bono×0.5

  status: PENDING | EXPLORING | CONVERGED | EXHAUSTED

  budget:
    queries_executed: int            # Queries executed so far
    last_pertinent: int              # Numéro dernière query pertinente
    consecutive_failures: int        # 0-2 ok, ≥3 stop

  results:
    sources_found: [◈◉○]
    facts_new: [str]
    comparables_found: [              # For COMPARABLES type only
      {
        case_id: str,
        entity: str,                  # Ex: "TF1", "LCI"
        regulatory_action: str,       # Ex: "sanctions ARCOM 2020-2024"
        severity: float,              # 0.0-1.0 normalized severity
        context_similarity: float     # 0.0-1.0 how comparable
      }
    ]
    connections: [{from, to, type}]
    gaps_resolved: bool
    edi_contribution: float          # Actual EDI improvement achieved
```

### @MACRO[EXPLORE_BRANCH]

**Cycle Exploration (Budget Adaptatif) :**

```yaml
EXPLORE_BRANCH:
  INPUT: branch (PENDING state)
  OUTPUT: branch (CONVERGED or EXHAUSTED state)

  INITIALIZE:
    branch.status ← EXPLORING

  LOOP_WHILE branch.status = EXPLORING:

    # Generate targeted query
    query ← generate_targeted_query(branch.objective, @KB[QUERY_TEMPLATES])
    result ← web_search(query) via MCP
    branch.budget.queries_executed ← branch.budget.queries_executed + 1

    # Evaluate pertinence (multicritères A|B|C|D)
    pertinent ← evaluate_pertinence(result, criteria={
      A: has_new_factual_info(result),      # Dates, montants, noms, événements
      B: has_better_source_quality(result), # ◈ trouvé OU ◉ trouvé OU ○→◉ upgrade
      C: reduces_gap(result, branch),       # Question partiellement répondue
      D: discovers_connections(result)      # Acteur-acteur, timing-événement, réseau
    })

    # Decision continuation
    IF pertinent:  # any(criteria A|B|C|D)
      branch.budget.consecutive_failures ← 0
      branch.budget.last_pertinent ← branch.budget.queries_executed
      branch.results.append(extract_findings(result))
      # Continue exploration (budget adaptatif)
    ELSE:
      branch.budget.consecutive_failures ← branch.budget.consecutive_failures + 1

    # Conditions arrêt
    IF branch.budget.consecutive_failures ≥ 3:
      branch.status ← EXHAUSTED  # Branche morte (3 échecs consécutifs)
      BREAK

    IF branch.results.gap_resolved OR branch.results.target_reached:
      branch.status ← CONVERGED  # Branche vivante (objectif atteint)
      BREAK

  RETURN: branch
```

### Isolation Garantie

**Sous-agent voit UNIQUEMENT :**
- `objective` (question à résoudre)
- `query_results` (web search responses)
- `state` interne (budget, consecutive_failures, results)

**Sous-agent NE voit PAS :**
- Résultats autres branches (évite biais confirmation)
- I0 patterns (évite cherry-picking infos confirmant patterns)
- Scoring global (évite optimisation locale au détriment global)

**Coordination :** APRÈS tous sous-agents terminés, en synthèse finale uniquement.

**Métaphore jury :** Comme jury délibération, chaque juré (branche) enquête indépendamment, verdict (synthèse) après isolation complète.

---

## §4 — PARALLEL_EXECUTION

### @MACRO[LAUNCH_INVESTIGATION_TREE]

```yaml
LAUNCH_INVESTIGATION_TREE:
  INPUT: i0_state (validation complete)
  OUTPUT: completed_branches[], synthesis

  # Step 1: Detect and score branches
  selected_branches ← BRANCH_SELECTION(i0_state)
  # Top 3-5 branches, scored by priority

  # Step 2: Parallel execution (isolation complète)
  completed_branches ← []

  FOR EACH branch IN selected_branches PARALLEL:
    # Each branch = independent Truth Engine instance
    # Complete isolation during exploration
    completed_branch ← EXPLORE_BRANCH(branch)
    completed_branches.append(completed_branch)

  # Await all branches completion (CONVERGED or EXHAUSTED)
  WAIT_ALL(completed_branches)

  # Step 3: Synthesis (post-hoc coordination)
  synthesis ← SYNTHESIZE_INVESTIGATION_TREE(i0_state, completed_branches)

  RETURN: {
    branches: completed_branches,
    synthesis: synthesis
  }
```

---

## §5 — SYNTHÈSE FINALE (F Complète)

### Opérations Agrégation

Voir kb/dsl/SEARCH_EPISTEMIC.md pour les heuristics DSL complètes.

#### 5.1 Concordances (⊕ confirmed)

```yaml
DETECT_CONCORDANCES:
  INPUT: branches[] (completed branches)
  OUTPUT: concordances[] (⊕ confirmed facts)

  COLLECT_FACTS:
    facts_all ← []
    FOR each branch IN branches:
      FOR each fact IN branch.results.facts_new:
        facts_all.append({fact: fact, branch_id: branch.id})

  GROUP_BY_FACT:
    facts_grouped ← group_by(facts_all, key=fact)

  DETECT:
    concordances ← []
    FOR each (fact, branches_found) IN facts_grouped:
      IF count(branches_found) ≥ 2:
        concordances.append({
          fact: fact,
          branches: branches_found,
          confidence: "⊕ confirmed (multi-source independent)"
        })

  RETURN: concordances

  # Voir design doc Section IV.1 (lignes 250-282) pour implémentation complète
```

**Exemple :**
```yaml
Fact: "von_der_leyen_centralisation_renseignement"
Branches: [b2_dissidents_RT, b3_chronologie_kohler, b4_timing_afd]
→ ⊕ Confirmed: Centralisation thème récurrent sources indépendantes
```

#### 5.2 Contradictions (⊗ contradicted)

```yaml
DETECT_CONTRADICTIONS:
  INPUT: branches[] (completed branches)
  OUTPUT: contradictions[] (⊗ conflicting facts)

  EXTRACT_SEMANTIC:
    facts_semantic ← extract_semantic_facts(branches)
    # Extract claims with semantic embedding for conflict detection

  FIND_CONFLICTS:
    contradictions ← []
    FOR each fact_pair IN find_semantic_conflicts(facts_semantic):
      contradictions.append({
        topic: fact_pair.topic,
        branch_A: fact_pair.source_a,
        claim_A: fact_pair.claim_a,
        branch_B: fact_pair.source_b,
        claim_B: fact_pair.claim_b,
        confidence: "⊗ contradicted → dialectique ⟐ vs ⟐̅"
      })

  RETURN: contradictions

  # Output dialectique: Claim A (source X) vs Claim B (source Y)
  # Transparence: Présenter les deux, utilisateur souverain décide
  # Voir design doc Section IV.2 (lignes 284-317) pour implémentation complète
```

**Exemple :**
```yaml
Topic: "orchestration_probability"
Branch A (b2_RT): "Orchestration 85-92% prouvée"
Branch B (b4_FT): "Coïncidence possible, intelligence unit préparée depuis mois"
→ ⊗ Dialectique: Sources dissidentes vs mainstream divergent
```

#### 5.3 Gaps Résiduels

```yaml
IDENTIFY_GAPS_UNRESOLVED:
  INPUT: branches[] (completed branches)
  OUTPUT: gaps[] (unresolved questions)

  FOR branch IN branches:
    IF branch.status = EXHAUSTED AND branch.results.gap_resolved = false:
      → Gap unresolved (question non répondue malgré budget adaptatif)
      → Critical: IF branch.type = GAP_CRITICAL
      → Output: Section "Gaps critiques" avec explication tentatives

  # Voir design doc Section IV.3 (lignes 319-354) pour implémentation complète
```

#### 5.4 EDI Global

```yaml
CALCULATE_EDI_GLOBAL:
  INPUT: branches[] (completed branches), edi_i0 (baseline)
  OUTPUT: edi_metrics (global EDI assessment)

  # Agrège sources toutes branches → EDI final investigation
  all_sources ← aggregate_sources(branches)  # ◈◉○ toutes branches
  edi_i1 ← @F[EDI](all_sources, dimensions...)

  RETURN: {
    edi_i0: edi_i0,
    edi_i1: edi_i1,
    improvement: edi_i1 - edi_i0,
    improvement_pct: ((edi_i1 - edi_i0) / edi_i0) × 100,
    target_apex: 0.80,
    gap_remaining: 0.80 - edi_i1
  }

  # Voir design doc Section IV.4 (lignes 356-396) pour implémentation complète
```

**Exemple :**
```yaml
edi_i0: 0.30
edi_i1: 0.45
improvement: +50%
target_apex: 0.80
gap_remaining: 0.35
```

#### 5.5 Décision I2 Targeted

```yaml
DECIDE_I2:
  INPUT: gaps_unresolved[], edi_global (metrics)
  OUTPUT: i2_decision (launch I2 or finalize)

  critical_gaps ← filter(gaps_unresolved, where: critical = true)

  IF count(critical_gaps) > 0 OR edi_global.edi_i1 < edi_global.target_apex:
    → LAUNCH_I2_TARGETED
    → Focus: Alternate strategies gaps critiques + EDI aggressive boost
    → Plan: logs/i2-plan.md (queries spécifiques, approches différentes)
  ELSE:
    → FINALIZE_INVESTIGATION
    → Status: SUCCESS_CONVERGED

  # Voir design doc Section IV.5 (lignes 398-423) pour implémentation complète
```

#### 5.6 Asymétries (△ differential treatment)

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

### @F[ASYMMETRY_SCORE]

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

**Exemple output:**
```yaml
asymmetry_analysis:
  asymmetry_score: 8.2
  verdict: "ASYMMETRY_EXTREME (differential treatment flagrant)"
  comparables: [
    {entity: "TF1", severity: 0.25, context_similarity: 0.75},
    {entity: "LCI", severity: 0.20, context_similarity: 0.70},
    {entity: "BFM", severity: 0.30, context_similarity: 0.72},
    {entity: "CNews", severity: 0.85, context_similarity: 1.0}
  ]
  severity_stats:
    mean: 0.40
    variance: 0.089
    range: 0.65
  subject_position: "ABOVE_AVERAGE (CNews 0.85 >> mean 0.40)"
```

---

## §6 — FORMATS OUTPUT

### 6.1 Mermaid Diagram

**File:** `logs/investigation-tree.md`

**Auto-generated** après synthèse finale :

```yaml
GENERATE_MERMAID:
  INPUT: investigation_tree (i0_state, branches, synthesis)
  OUTPUT: mermaid_string

  mermaid ← "graph TD\n"

  # I0 node
  mermaid += "    I0[I0 APEX: {subject}<br/>EDI: {edi_i0}, Queries: {queries_i0}]\n"

  # Branch nodes
  FOR branch IN branches:
    status_icon ← (branch.status = CONVERGED ? "✅" : "❌")
    mermaid += "    I0 -->|priority: {branch.score.priority}| {branch.id}[{branch.id}: {branch.type}<br/>Status: {branch.status} {status_icon}<br/>Queries: {branch.budget.queries_executed}]\n"

  # Concordance/contradiction edges (dotted)
  FOR concordance IN synthesis.concordances:
    # Dotted edge between branches

  # Synthesis node
  mermaid += "    SYNTH[SYNTHÈSE I1<br/>EDI: {synthesis.edi_global.edi_i1}, Concordances: {count(concordances)}]\n"

  # Style (converged green, exhausted red)
  FOR branch IN branches:
    IF branch.status = EXHAUSTED:
      mermaid += "style {branch.id} fill:#ffcccc\n"
    ELSE IF branch.status = CONVERGED:
      mermaid += "style {branch.id} fill:#ccffcc\n"

  RETURN: mermaid
```

**Légende:**
- 🟢 Vert ✅ = branche converged (objectif atteint)
- 🔴 Rouge ❌ = branche exhausted (3 échecs, branche morte)
- Flèches pleines = hiérarchie parent → enfant
- Flèches pointillées = relations (concordance ⊕, contradiction ⊗)

### 6.2 JSON State

**File:** `logs/investigation-tree.json`

**Machine-readable state** pour debug/metrics/reprise :

```yaml
GENERATE_JSON_STATE:
  INPUT: investigation_tree
  OUTPUT: json_state

  RETURN: {
    investigation_id: "{date}_{subject_normalized}_apex",
    complexity: complexity_score,
    iterations: [
      {
        iteration: "I0",
        type: "root",
        queries: queries_i0,
        edi: edi_i0,
        sources: {◈: count, ◉: count, ○: count},
        patterns: {Κ: score, Ξ: score, ...},
        wolves: count,
        gaps: [gap_ids],
        timestamp: ISO8601
      },
      {
        iteration: "I1",
        type: "investigation_tree",
        branches: [
          {
            id: branch.id,
            parent: "i0_root",
            type: branch.type,
            objective: branch.objective,
            score: {edi_impact, cui_bono, priority},
            status: branch.status,
            budget: {queries_executed, last_pertinent, consecutive_failures},
            results: {sources_found, facts_new, connections, gap_resolved}
          },
          ...
        ],
        synthesis: {
          edi_i0: edi_i0,
          edi_i1: edi_i1,
          improvement: improvement,
          target: 0.80,
          gap_remaining: gap_remaining,
          sources_total: {◈: count, ◉: count, ○: count},
          concordances: [{fact, branches, confidence}, ...],
          contradictions: [{topic, branch_A, claim_A, branch_B, claim_B}, ...],
          gaps_unresolved: [{branch, objective, critical}, ...]
        },
        decision: {
          launch_i2: bool,
          focus: [strategy_types],
          reason: str
        },
        timestamp: ISO8601
      }
    ]
  }
```

**Usage JSON :**
1. **Debug/Audit :** Quelles branches explorées, combien queries, pourquoi arrêt
2. **Reprise I2/I3 :** Load state, focus gaps unresolved
3. **Métriques :** Budget efficiency par branche, taux convergence
4. **A/B Testing :** Comparer scoring strategies, budget allocations

---

## §7 — RÉTROCOMPATIBILITÉ

### Workflow Routing

```yaml
COMPLEXITY_ROUTING:

  IF complexity < 9.0:  # SIMPLE/MEDIUM/COMPLEX
    → LINEAR WORKFLOW: I0 → I1 AUTO → I2 CAP
    → Investigation Tree NOT activated
    → Aucun changement comportement (backward compatible)

  ELSE IF complexity ≥ 9.0:  # APEX
    → ARBORESCENT WORKFLOW: I0 → TREE I1 → SYNTHÈSE → I2 TARGETED
    → Investigation Tree activated automatically
    → Output: 3 parties standard + Mermaid + JSON

PRESERVES:
  - SIMPLE/MEDIUM/COMPLEX: Workflow linéaire inchangé
  - APEX: Produit toujours output 3 parties (enrichies branches)
  - Tous workflows: Même structure Part 1/2/3, mêmes métriques (EDI, ISN, etc.)
```

---

## §8 — MÉTRIQUES SUCCÈS

### Targets Investigation Tree

```yaml
EDI:
  improvement_min: +30% (ex: 0.30 → 0.40+)
  target_apex: EDI ≥ 0.80

SOURCES:
  primary_found: ◈ ≥1 (amélioration vs 0)
  diversity_improved: geo + perspective + temporal améliorées

BRANCHES:
  convergence_rate: ≥60% (3/5 branches converged)
  budget_efficiency: queries_per_fact < 2.0

GAPS:
  critical_resolved: ≥70%
  total_resolved: ≥50%

I2:
  launch_rate: <50% (majorité investigations terminent I1)
  targeted_focus: Max 2 branches I2 (pas re-exploration totale)

PERFORMANCE:
  total_queries_i0_i1: ≤50 (prevent budget explosion)
  duration_i0_i1: ≤60min (acceptable latency)

QUALITY:
  concordances_detected: ≥2 (multi-source confirmation)
  contradictions_detected: ≥1 (dialectic perspectives)
  gaps_critiques_unresolved: ≤30%
```

### Exemple Validation

```yaml
Investigation UE Intelligence Unit (APEX 8.5):

I0 (baseline):
  edi: 0.30
  sources: ◈0 ◉10 ○2
  queries: 18

I1 Investigation Tree:
  branches: 5 launched (3 converged ✅, 2 exhausted ❌)
  queries_total: 25
  edi: 0.45 (+50% improvement ✅)
  sources: ◈0 ◉14 ○7 (◉ +40% ✅)
  convergence_rate: 60% ✅
  gaps_critical_resolved: 1/2 (50% ⚠️)

Decision: I2 targeted (gap Budget Shield + EDI boost)

Success: PARTIAL (EDI amélioré, mais target 0.80 non atteint)
→ Recommend I2 aggressive strategies
```

---

## §9 — EXTENSIONS

### v1.1 Extensions (2025-11-14) ✅ IMPLEMENTED

**COMPARABLES_ASYMMETRY (6th branch type + 6th synthesis operation):**
- ✅ Branch type: COMPARABLES (regulatory/institutional comparables search)
- ✅ Triggers: regulatory_context OR Ξ OMISSION ≥8 OR mid-tree reactive
- ✅ Synthesis: DETECT_ASYMMETRY (measures differential treatment 0-10 scale)
- ✅ Formula: @F[ASYMMETRY_SCORE] (range×0.40 + variance×0.30 + extremity×0.30)
- ✅ Integration: §1, §2, §3, §5 updated
- ✅ Use case: ARCOM CNews vs TF1/LCI/BFM (asymmetry 8.2/10 EXTREME)

**Impact:**
- Révèle Ξ OMISSION patterns (hidden comparables, differential treatment)
- Améliore narrative_diversity (EDI impact 0.35)
- Critical for regulatory/institutional investigations
- Addresses gap identified in user's ARCOM/CNews tweet analysis

### Future Extensions (v1.2+)

**Profondeur récursive :**
- Sous-agent peut lancer 1 niveau sous-sous-agents si détecte piste critique
- Limite: 1 niveau récursion (éviter explosion arbre)

**Apprentissage scoring :**
- Track success rate branches par type
- Ajuster coefficients edi_impact selon résultats historiques

**Budget dynamique :**
- Réalloquer budget branches mortes vers branches vivantes
- Pool queries partagé plutôt que fixed per branch

**Visualisation interactive :**
- Mermaid cliquable avec drill-down branches
- Timeline exploration queries

---

**END INVESTIGATION_TREE.md v1.1**

**Cross-references:**
- **KERNEL.md** — §3 Gates, §2.11-§2.15 Investigation steps
- **kb/protocols/INVESTIGATION.md** — L0-L6 sequential cascade
- **kb/dsl/SYMBOLS.md** — Symbol definitions + ACTION MAP
- **docs/plans/2025-11-14-investigation-tree-design.md** — Core design document
- **docs/plans/COMPARABLES_ASYMMETRY_design.md** — v1.1 COMPARABLES extension design

**Version:** 1.1 (v1.0 Phase 1-2 + v1.1 COMPARABLES_ASYMMETRY)
**Last updated:** 2025-11-14
**Status:** Phase 1-2 COMPLETE ✅ | v1.1 COMPARABLES extension COMPLETE ✅ (DSL pur)

**Changelog v1.1:**
- Add COMPARABLES (6th branch type) for regulatory/institutional comparables search
- Add DETECT_ASYMMETRY (6th synthesis operation) measuring differential treatment 0-10
- Add @F[ASYMMETRY_SCORE] formula (variance-based asymmetry quantification)
- Update §1 triggers (COMPARABLES_LAUNCH via regulatory_context OR Ξ≥8)
- Update §2 scoring (EDI_IMPACT +0.35, CUI_BONO_CENTRALITY +0.25)
- Update §3 branch structure (comparables_found[] results)
- Add §5.6 DETECT_ASYMMETRY synthesis operation
- Use case: ARCOM/CNews vs TF1/LCI/BFM asymmetry detection
