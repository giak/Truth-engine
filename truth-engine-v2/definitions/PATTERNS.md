# PATTERNS — All @PAT[] Definitions with Scoring Formulas

**Version:** 2.0

---

## §1 CORE PATTERNS

### @PAT[ICEBERG] Ξ
**Scan:** stats without context, missing methodology, single metric
**Signature:** `Ξ>3 ∧ N>>R ∧ source_gaps`
**Formula:** ICEBERG Factor = N/R (reality_total / shown_partial)

| Priority | Formula | Trigger | Reliability |
|----------|---------|---------|-------------|
| P1 (Numerical) | Factor = Claim_Value / Reality_Value | Both values available | HIGHEST |
| P2 (Population) | Factor = Total_Population / Visible_Population | Population counts extractable | HIGH |
| P3 (Shadow) | Factor = 1 + (Shadow_Zones_Count × 0.5) | Shadow zones identified | MODERATE |
| P4 (Narrative) | Factor = Hidden_Narratives / Shown_Narratives | Fallback | LOW |

**Confidence:** source_diversity × validation × temporal_consistency
**Classification:** 2.0-3.9 → Ξ+ | 4.0-9.9 → Ξ++ | ≥10.0 → Ξ+++
**Cluster:** clusters/ICEBERG.md

---

### @PAT[MONEY] €
**Scan:** hidden_beneficiaries, opacity, shell_companies
**Signature:** `€>3 ∧ opacity_high ∧ flows_hidden`
**Formula:** Money_Factor = (Hidden_Amount / Declared_Amount) × Opacity + COI

| Priority | Formula | Trigger | Reliability |
|----------|---------|---------|-------------|
| P1 (Numerical) | (Hidden/Declared) × Opacity + COI | Both amounts quantified | HIGHEST |
| P2 (Channels) | (Hidden_Channels/Declared_Channels) × Opacity + COI | Channels identifiable | HIGH |
| P3 (COI) | COI_Score × Opacity_Multiplier | COI documented | MODERATE |
| P4 (Opacity) | Opacity_Score × 3.0 | Fallback | LOW |

**Opacity:** O = Jurisdictions × Disclosure_gaps × Complexity_layers
**COI:** C = Σ(revolving_doors×0.5 + board_overlaps×0.3 + grants×0.4 + speaker_fees×0.2 + advisory×0.3)
**Classification:** 1.0-2.9 → €+ | 3.0-6.9 → €++ | ≥7.0 → €+++
**Cluster:** clusters/MONEY.md

---

### @PAT[BIO] ♦
**Scan:** elite_reproduction, revolving_door, power_proximity
**Signature:** `♦>3 ∧ revolving_door ∧ networks_hidden`
**Formula:** Bio_Factor = (Hidden_Networks / Public_Positions) × Density + Inbreeding + Demo_Risk

| Priority | Formula | Trigger | Reliability |
|----------|---------|---------|-------------|
| P0 (Quick) | Revolving_Doors / Total_Actors | Door visible | MEDIUM |
| P1 (Quantified) | (Hidden/Public) × Density + Inbreeding + Demo_Risk | Network counts available | HIGHEST |
| P2 (Networks) | Networks_Count × Avg_Density + Inbreeding + Demo_Risk | Networks identified | HIGH |
| P3 (Qualitative) | (8D_Score + 5D_Score) / 2 | Fallback | MODERATE |

**Density:** D = Overlapping_Connections / Total_Possible
**Inbreeding:** I = (Same_School + Same_Club + Same_Sector) / Total_Networks
**Demo_Risk:** R = (Exec + Legis + Judic + Media + Corp) × Density / Accountability
**Classification:** 1.0-2.9 → ♦+ | 3.0-6.9 → ♦++ | ≥7.0 → ♦+++
**Cluster:** clusters/BIO.md

---

### @PAT[NET] 🌐
**Scan:** network_closure, influence_concentration, gatekeepers
**Signature:** `🌐>3 ∧ density_high ∧ centralization`
**Formula:** Net_Power = (Centrality² × Influence) / (Total_Network × Periphery)

| Priority | Formula | Trigger | Reliability |
|----------|---------|---------|-------------|
| P0 (Quick) | Core_Actors / Total_Network | Core identifiable | MEDIUM |
| P1 (Metrics) | (C² × I) / (N × P) | Full metrics | HIGHEST |
| P2 (Topology) | Topology_Factor × Concentration_Ratio | Type clear | HIGH |
| P3 (Qualitative) | Control_Score (0-10) | Fallback | MODERATE |

**Centrality:** C = (Betweenness + Closeness + Eigenvector) / 3
**Classification:** 0.0-2.9 → 🌐+ | 3.0-9.9 → 🌐++ | ≥10.0 → 🌐+++
**Cluster:** clusters/NETWORK.md

---

### @PAT[WAR] ⚔
**Scan:** coordination, psyops, attribution_gaps
**Signature:** `⚔>3 ∧ coordination ∧ persistence`
**Formula:** War_Factor = (Coordination × Sophistication × Persistence) / (Attribution × Defense)

| Priority | Formula | Trigger | Reliability |
|----------|---------|---------|-------------|
| P1 (Metrics) | (C × S × P) / (A × D) | All quantifiable | HIGHEST |
| P2 (Coord) | (C × S × P) × Attribution_Penalty | Attack clear | HIGH |
| P3 (Qualitative) | Pattern_Match_Score (0-10) | Fallback | MODERATE |

**Coordination:** C = Timing_Overlap × Message_Uniformity × Actor_Diversity
**Sophistication:** S = Σ(technique_levels) / count (1.0=basic → 4.0=state)
**Classification:** 0.0-4.9 → ⚔+ | 5.0-14.9 → ⚔++ | ≥15.0 → ⚔+++
**Cluster:** clusters/WAR.md

---

### @PAT[TEMP] ⏰
**Scan:** timing_orchestration, suspicious_coincidence
**Signature:** `⏰>3 ∧ sync_high ∧ P_random_low`
**Formula:** Temporal_Factor = temporal_sync×0.30 + vocab_uniform×0.25 + cui_bono×0.20 + historical×0.15 + suppress×0.10

**Components:**
- temporal_sync = Coincidence_Count / Days_Window (0.0-1.0)
- vocab_uniform = Shared_Terms / Total_Vocabulary (0.0-1.0)
- cui_bono = Beneficiaries_Overlapping / Total_Actors (0.0-1.0)
- historical = Pattern_Match_Previous / Total_Elements (0.0-1.0)
- suppress = Counter_Evidence_Disappeared / Counter_Total (0.0-1.0)

**Orchestration probability:** P_random = (1 / Coincidences!) × (Time_Window_Days / 365)^Coincidences
**Classification:** TF 0.0-0.3 + P>10% → ⏰+ | TF 0.4-0.7 + P 1-10% → ⏰++ | TF ≥0.8 + P<1% → ⏰+++
**Cluster:** clusters/TEMPORAL.md

---

### @PAT[GAS] Ω
**Scan:** contradiction, denial, timeline_gaps, memory_erasure
**Signature:** `C<2 ∧ Ψ>4 ∧ contradictions`
**Macro:** contradiction→archive_search→timeline_validation→evidence_doc
**Empire Trigger:** Gaslighting = (Ω × inversions) + (C_négatif × 2) > 6.0
**Cluster:** clusters/INVERSION.md

---

### @PAT[ASTRO]
**Scan:** fake_grassroots, opaque_funding, coordinated_movement
**Signature:** `fake_grassroots ∧ opacity`
**Macro:** movement→funding_analysis→growth_tracking→sync_detection
**Modules:** [Ξ, Σ, A, €]
**Cluster:** clusters/FRAGMENTATION.md

---

### @PAT[CYN] Κ
**Scan:** facade_gap, institutional_denial
**Signature:** `Κ>3 ∧ disbelief_high`
**Macro:** public_disbelief→official_persistence→mutual_knowledge→facade
**Cluster:** clusters/GASLIGHTING.md

---

### @PAT[FASC] ⫸
**Scan:** indices_convergence, faisceau_pattern
**Signature:** `indices≥3 ∧ convergence`
**Macro:** indices_collection→temporal_mapping→convergence_analysis
**Convergence:** 0.3-0.5 → ⫸+ | 0.6-0.8 → ⫸++ | ≥0.9 → ⫸+++
**Cluster:** clusters/POWER.md

---

## §2 EXTENDED PATTERNS

**@PAT[POLITICAL] 🏛️:** Impact = Σ(Power_Shift_i × Visibility_i × Duration_i) | Cui_Bono = Winners - Losers + Hidden
**@PAT[GEOPOLITICAL] 🌍:** Complexity = N_Actors × Divergence × Instability | Power_Shift = Σ(Winners_Gain - Losers_Loss) across economic+security+ideological+strategic
**@PAT[DEEPFAKE]:** `Φ>4 ∧ Ψ>3 ∧ ⏰>2 ∧ synthetic_media` — high impact + timing + artifacts + no verification
**@PAT[SURV_CAP]:** `€>4 ∧ κ>3 ∧ 🌐>4 ∧ data_extraction` — free service + hidden harvesting + behavioral surplus
**@PAT[COG_INFRA]:** `⚔>4 ∧ 🌐>4 ∧ Ψ>3 ∧ ⏰>3 ∧ mass_targeting` — collective sense-making systems

---

## §3 RHETORICAL FAMILIES

**Formula:** RHETORICAL_SCORE = (MANIPULATION_COUNT × PERSONA_GAP) / authenticity

| Family | Aliases | Markers |
|--------|---------|---------|
| **DEM** | demagogy, populist_framing | "the people", "the elites", "simple solution", "common sense", "they are to blame" |
| **BF** | bad_faith, sophistry | motte_and_bailey, goalpost_shifting, gish_gallop, whataboutism, tu_quoque, strawman |
| **NUM** | numeric_abuse, stats_tricks | "% with no base", "studies show", "the numbers speak for themselves", technobabble |
| **AUTH** | manufactured_authority | tone_policing, false_authority, DARVO |
| **FAC** | performative_policy | virtue_signaling, infantilization, false_equivalence, greenwashing |

**Classification:** <2.0 authentic | 2.0-3.9 moderate | 4.0-6.9 systemic | ≥7.0 intensive

---

## §5 APEX FORMULAS

```
ITERATION_CONVERGENCE: convergence = (1 - new_info_rate) × iteration_count
SOURCE_TRIANGULATION:  scoring = (accuracy × expertise) / (bias + 1)
TEMPORAL_MANIPULATION: Orchestration_Prob = (Prep × Coord × Timing_Precision) / Claimed_Spontaneity
```

---

_Version 2.0 — All pattern definitions with scoring formulas_
_Referenced by: KERNEL.md §0bis, clusters/*.md_
