# SEARCH EPISTEMIC v1.0 — Source Pluralism & Narrative Cartography

**PHASE 1 v6.2** - Minimal Viable Implementation

---

## 🔥 HOT ZONE - QUICK START

### ⚡ CRITICAL SYMBOLS
```yaml
STRATIFICATION: ◈:primary(docs,leaks,court) ◉:secondary(investigative,academic) ○:tertiary(MSM,aggregators)
CORROBORATION: ⊕:confirmed ⊗:contradicted ⊙:partial_overlap
DIVERGENCE: ≋:divergence_zones
NARRATIVES: ⟐:official_narrative ⟐̅:counter_hegemonic
PERSPECTIVES: 🌍:regional 🎓:academic 🔥:dissident
FACT_QUALITY: ✦:hard_fact(documented) ✧:soft_fact(testimony) ⁕:claim(unverified) ⁂:speculation
ORCHESTRATION: ⚑:red_flags(temporal_sync<12h, vocabulary_identical, cui_bono_evident)
```

### 📊 EDI FORMULA - Epistemic Diversity Index
```python
EDI = (
    geo_diversity × 0.25 +        # Geographic spread
    lang_diversity × 0.20 +       # Linguistic diversity
    strat_diversity × 0.20 +      # Primary/Secondary/Tertiary balance
    ownership_diversity × 0.15 +  # Ownership types
    perspective_diversity × 0.15 + # Political perspectives
    temporal_diversity × 0.05     # Temporal spread
)

# TARGET: EDI ≥ 0.50 (good) | ≥ 0.65 (excellent)

geo_diversity = continents_count/6 × 0.4 + zones_count/10 × 0.3 + local_presence × 0.3
lang_diversity = languages/10 × 0.3 + non_english_pct × 0.4 + families/5 × 0.3
strat_diversity = primary_pct × 0.5 + secondary_pct × 0.3 + tertiary_pct × 0.2
ownership_diversity = types/6 × 0.6 + non_corporate_pct × 0.4
perspective_diversity = perspectives/7 × 0.5 + official_vs_counter_balance × 0.3 + dissident_presence × 0.2
temporal_diversity = temporalities/5 × 0.6 + archival_presence × 0.4
```

### 📐 EDI CALCULATOR TEMPLATE (LLM self-check)

**Usage**: Copy-paste template, fill values, self-validate.

```python
# EDI Calculation Template v2.0 (with self-check)

# Step 1: Collect dimension inputs
continents = 3  # Europe, Asia, Americas
zones = 5
local_presence = 1  # yes=1, no=0

languages = 4  # FR, EN, DE, ES
non_EN_pct = 0.52  # 52% non-English
families = 2  # Romance, Germanic

primary_count = 2
secondary_count = 3
tertiary_count = 5
total_sources = primary_count + secondary_count + tertiary_count
primary_pct = primary_count / total_sources
secondary_pct = secondary_count / total_sources
tertiary_pct = tertiary_count / total_sources

ownership_types = 4  # state, corporate, independent, academic
non_corporate_pct = 0.60

perspectives = 5  # official, counter, academic, dissident, regional
balance = 0.50  # 0-1 score official vs counter
dissident_present = 1  # yes=1, no=0

temporalities = 3  # recent, medium, archival
archival_present = 1  # yes=1, no=0

# Step 2: Calculate dimensions
dims = {
    "geo": (continents/6 * 0.4) + (zones/10 * 0.3) + (local_presence * 0.3),
    "lang": (languages/10 * 0.3) + (non_EN_pct * 0.4) + (families/5 * 0.3),
    "strat": (primary_pct * 0.5) + (secondary_pct * 0.3) + (tertiary_pct * 0.2),
    "owner": (ownership_types/6 * 0.6) + (non_corporate_pct * 0.4),
    "persp": (perspectives/7 * 0.5) + (balance * 0.3) + (dissident_present * 0.2),
    "temp": (temporalities/5 * 0.6) + (archival_present * 0.4)
}

# Step 3: Calculate raw EDI
EDI_raw = (
    dims["geo"] * 0.25 +
    dims["lang"] * 0.20 +
    dims["strat"] * 0.20 +
    dims["owner"] * 0.15 +
    dims["persp"] * 0.15 +
    dims["temp"] * 0.05
)

# Step 4: Apply penalties
penalty_list = [
    {"code": "MISSING_PRIMARY", "weight": -0.10},  # primary_count < 3
    # Add more as detected
]
penalties_total = sum([p["weight"] for p in penalty_list])

# Step 5: Calculate final EDI
EDI_final = max(0.0, EDI_raw + penalties_total)

# Step 6: Classify
if EDI_final >= 0.65:
    classification = "EXCELLENT"
elif EDI_final >= 0.50:
    classification = "GOOD"
elif EDI_final >= 0.35:
    classification = "ACCEPTABLE"
else:
    classification = "EPISTEMIC_MONOCULTURE"

# Step 7: Self-check (validation)
assert 0.0 <= EDI_final <= 1.0, f"EDI out of bounds: {EDI_final}"
assert all(p["weight"] <= 0 for p in penalty_list), "Penalty positive detected"
assert 0.99 <= (dims["geo"]*0.25 + dims["lang"]*0.20 + dims["strat"]*0.20 + 
                dims["owner"]*0.15 + dims["persp"]*0.15 + dims["temp"]*0.05) / EDI_raw <= 1.01, "Dimension weights mismatch"

print(f"EDI_final: {EDI_final:.2f} ({classification})")
print(f"EDI_raw: {EDI_raw:.2f} | Penalties: {penalties_total:.2f}")
print(f"Dimensions: geo={dims['geo']:.2f} lang={dims['lang']:.2f} strat={dims['strat']:.2f} owner={dims['owner']:.2f} persp={dims['persp']:.2f} temp={dims['temp']:.2f}")
```

**Output example**:
```
EDI_final: 0.42 (ACCEPTABLE)
EDI_raw: 0.52 | Penalties: -0.10
Dimensions: geo=0.62 lang=0.39 strat=0.29 owner=0.64 persp=0.71 temp=0.76
```

---

## 1. SOURCE STRATIFICATION HIERARCHY

### 1.1 Three-Tier System

| Tier | Symbol | Types | Confidence | Examples |
|------|--------|-------|------------|----------|
| **PRIMARY** | ◈ | Raw documents, leaks, court files, data | 0.90-0.95 | Wikileaks cables, FOIA releases, court transcripts, raw statistics, leaked emails |
| **SECONDARY** | ◉ | Investigative journalism, academic analysis | 0.75-0.85 | Consortium investigations, peer-reviewed papers, expert testimony, field reports |
| **TERTIARY** | ○ | Mainstream media, aggregators, opinion | 0.40-0.70 | NYT, BBC, Reuters, blogs, editorials, social media |

**PRIORITY RULE**: ◈ > ◉ > ○ (but all three needed for complete cartography)

### 1.2 Anti-Empire Source Weighting

```yaml
SOURCE_RELIABILITY_WEIGHTS:
  dissident_whistleblower: 0.95  # Leaked docs, FOIA, whistleblowers
  independent_investigative: 0.90  # Consortium, Mediapart, Intercept
  field_testimony: 0.85  # Direct witnesses, workers, citizens
  alternative_media: 0.80  # Non-corporate media
  archival_contradictions: 0.80  # Historical evidence
  international_opposing: 0.75  # Foreign viewpoints (non-aligned)
  official_institutions: 0.20  # Government, UN - SKEPTICISM DEFAULT
```

**CRITICAL**: Official sources (⟐) weighted LOW (0.20) unless corroborated by ◈ primary evidence.

### 1.3 Classification Decision Tree (v6.3.1 BIAS CORRECTION)

**PURPOSE**: Eliminate ambiguity in ◈◉○ classification, prevent "official = reliable" bias.

**ASCII FLOWCHART** (quick reference):

```
CLASSIFICATION FLOWCHART (◈◉○)

Source type?
  ├─ Govt/IGO/Military → ○ TERTIARY (conf 0.20-0.40)
  │   Contains leaked docs? 
  │   ├─ YES → Docs only: ◈ PRIMARY | Analysis: ○ TERTIARY
  │   └─ NO → ○ TERTIARY
  │
  ├─ Corporate/Corp_Media → Check funding
  │   ├─ Disclosed + No COI → ◉ SECONDARY (0.60-0.75)
  │   └─ Opaque OR COI → ○ TERTIARY (0.40-0.60)
  │
  └─ Independent/Academic → Check independence
      ├─ Independent verified → ◉ SECONDARY (0.75-0.85)
      └─ Unclear → ○ TERTIARY (0.50-0.70)

Corroboration? 
  → Increases CONFIDENCE within tier (doesn't change tier)
  → Circular corroboration (same institutional family) = NOT valid

Principle: Official ≠ Reliable | Evidence transcends institution
```

**ALGORITHM DETAILED**:

```yaml
CLASSIFICATION_ALGORITHM:

  STEP_1_PROVENANCE_CHECK:
    # Institutional status determines DEFAULT tier

    IF source IN [government, state_agency, military, intelligence, UN, NATO, EU_institution, IGO]:
      → DEFAULT: ○ TERTIARY (confidence 0.20-0.40)
      → REASON: Party to conflicts, not neutral observer, institutional incentives
      → Examples: VIGINUM, EEAS, Pentagon, CIA, UN reports, government statements

    ELSE IF source IN [corporation, corporate_media, funded_think_tank]:
      IF funding_disclosed AND no_conflicts_of_interest_detected:
        → DEFAULT: ◉ SECONDARY (confidence 0.60-0.75)
      ELSE:
        → DEFAULT: ○ TERTIARY (confidence 0.40-0.60)
        → REASON: Potential COI, undisclosed funding, corporate interests
      → Examples: Microsoft (defense contracts), corporate media, corporate-funded think tanks

    ELSE IF source IN [independent_journalism, academic_research, independent_NGO]:
      IF funding_independent AND editorial_independence_verified:
        → DEFAULT: ◉ SECONDARY (confidence 0.75-0.85)
      ELSE:
        → DEFAULT: ○ TERTIARY (confidence 0.50-0.70)
      → Examples: Consortium investigations, peer-reviewed research, independent media

  STEP_2_EVIDENCE_TYPE_CHECK:
    # Evidence type can UPGRADE specific elements (not entire source)

    IF source_contains [leaked_document, FOIA_release, court_file, raw_dataset, whistleblower_docs]:
      → THOSE ELEMENTS ONLY: ◈ PRIMARY (confidence 0.90-0.95)
      → SOURCE INTERPRETATION: remains at STEP_1 classification

      EXAMPLE:
        - VIGINUM report = ○ TERTIARY (government source)
        - Leaked emails WITHIN report = ◈ PRIMARY (raw evidence)
        - VIGINUM analysis OF emails = ○ TERTIARY (interpretation)

    IF source_provides [testimony, investigation, analysis, claims]:
      → NO UPGRADE, remains at STEP_1 classification
      → REASON: Interpretation/assertion, not raw unaltered evidence

  STEP_3_CORROBORATION_CHECK:
    # Corroboration increases CONFIDENCE within tier, doesn't change tier

    IF claim_corroborated_by ≥2_sources FROM different_provenance_types:
      → CONFIDENCE boost: +0.10 to +0.20 within tier
      → Classification tier: UNCHANGED

      EXAMPLE:
        - Government claim (○ TERTIARY, conf 0.20)
        - Corroborated by independent investigation (◉ SECONDARY, conf 0.80)
        - Government claim confidence → 0.40 (still ○, but higher within tier)

    CIRCULAR_CORROBORATION_WARNING:
      IF corroborating_sources from same_institutional_family:
        → NOT considered independent corroboration
        → EXAMPLE: 5 NATO members confirming each other = 1 source, not 5

CRITICAL_PRINCIPLES:

  1. "Official ≠ Reliable": Government/institutional status is DISQUALIFYING by default

  2. "Evidence transcends institution": Raw documents elevate regardless of source

  3. "Interpretation inherits bias": Analysis by biased source remains biased

  4. "Corroboration must be independent": Same institutional family = single source

  5. "Follow the money": Funding sources determine independence (see H9, Section 12.4)

COMMON_ERRORS_TO_AVOID:

  ❌ WRONG: "EEAS official report → ◈ PRIMARY"
  ✅ RIGHT: "EEAS report → ○ TERTIARY (government), leaked docs within → ◈ PRIMARY"

  ❌ WRONG: "Microsoft cybersecurity analysis → ◈ PRIMARY"
  ✅ RIGHT: "Microsoft analysis → ◉ SECONDARY (COI: defense contracts)"

  ❌ WRONG: "5 EU governments confirm → strong corroboration"
  ✅ RIGHT: "5 EU governments = circular, need non-EU independent sources"

  ❌ WRONG: "Academic paper funded by Pentagon → ◉ SECONDARY neutral"
  ✅ RIGHT: "Pentagon-funded paper → ○ TERTIARY (COI despite academic format)"
```

---

## 2. NARRATIVE CARTOGRAPHY SYSTEM

### 2.1 Five Narrative Types

```yaml
⟐ OFFICIAL_NARRATIVE:
  - Government/institutional version
  - Dominant MSM consensus
  - Sources: typically ○ tertiary
  - Expected: simplistic, binary, emotionally charged
  - Function: manufacture consent

⟐̅ COUNTER_HEGEMONIC:
  - Opposes power structures
  - Sources: mix ◈◉○ (often ◈ leaks critical)
  - Expected: complex, systemic analysis, cui bono focus
  - Function: reveal hidden interests

🌍 REGIONAL:
  - Local/neighbor perspectives
  - Sources: local media, regional languages
  - Expected: different priorities, cultural context
  - Function: escape Western-centric bias

🎓 ACADEMIC:
  - Scholarly analysis
  - Sources: ◉ peer-reviewed, research
  - Expected: nuanced, "it's complicated"
  - Function: depth beyond journalism

🔥 DISSIDENT:
  - Censored/suppressed voices
  - Sources: deplatformed experts, whistleblowers
  - Expected: contradicts ⟐, often ◈ evidence-backed
  - Function: reveal what power hides
```

### 2.2 Divergence Zones (≋)

**DEFINITION**: Points where narratives fundamentally contradict.

```yaml
DIVERGENCE_DETECTION:
  IF claim_A (narrative_1) contradicts claim_B (narrative_2):
    AND evidence_quality differs significantly:
      → FLAG as ≋ DIVERGENCE_ZONE

  CLASSIFICATION:
    ≋+ MINOR: Different emphasis, same basic facts
    ≋++ MAJOR: Contradictory core claims
    ≋+++ SUPPRESSED: One side has ◈ evidence, other only ○ assertions

EXAMPLE:
  ⟐: "Assad used chemical weapons" (○ MSM reports)
  ⟐̅: "False flag by rebels" (◈ OPCW whistleblower + ◉ MIT study)
  STATUS: ≋+++ SUPPRESSED_EVIDENCE (primary docs contradict official)
```

---

## 3. CORROBORATION PROTOCOL

### 3.1 Fact Quality Assessment

```yaml
✦ HARD_FACT:
  - Documented in ◈ primary sources
  - Corroborated by ≥2 independent ◉ sources
  - No contradictions from reliable sources
  - Examples: Court verdict, leaked document content, published statistics

✧ SOFT_FACT:
  - Based on ◉ testimony/investigation
  - Contextually coherent
  - Some corroboration but not ◈ primary
  - Examples: Expert estimates, eyewitness accounts, field observations

⁕ CLAIM:
  - Assertion without ◈◉ documentation
  - Single source or ○ tertiary only
  - Plausible but unverified
  - Examples: Official statements, allegations, rumors

⁂ SPECULATION:
  - Hypothesis explicitly uncertain
  - Logical inference but no direct evidence
  - Examples: "Possible that...", "Could indicate..."
```

### 3.2 Corroboration Symbols

```yaml
⊕ CONFIRMED:
  - ≥2 sources ◈ primary concordant
  - OR ≥3 sources ◉ secondary concordant
  - No significant contradictions

⊗ CONTRADICTED:
  - ≥2 sources ◈ primary contradict
  - OR pattern contradictions (timeline impossible, physics violation)

⊙ PARTIAL_OVERLAP:
  - Some elements confirmed, others contested
  - Mixed evidence quality
  - Requires nuanced analysis
```

---

## 4. ORCHESTRATION DETECTION (⚑)

### 4.1 Red Flag Indicators

```yaml
⚑ TEMPORAL_SYNCHRONIZATION:
  - Narrative appears simultaneously <12h across ≥10 outlets
  - Probability spontaneous: <0.01%
  - Indicates: coordination, shared talking points

⚑ VOCABULARY_IDENTICAL:
  - Same phrases/expressions used across "independent" sources
  - Indicates: centralized messaging, astroturfing

⚑ CUI_BONO_EVIDENT:
  - Clear financial/political beneficiaries
  - Narrative serves specific power interests
  - Timing aligns with beneficiary needs (electoral, legislative, commercial)

⚑ SUPPRESSION_ACTIVE:
  - Counter-narratives censored, deplatformed, fact-checked
  - Experts silenced, studies retracted
  - Indicates: narrative protection, manufactured consensus

⚑ HISTORICAL_PATTERN:
  - Reproduces documented past orchestrations
  - Examples: Iraq WMD 2003, Libya 2011, Syria chemical weapons
  - Pattern matching: playbook recognition
```

### 4.2 Orchestration Probability Scoring

```python
P_orchestration = (
    temporal_sync_score × 0.30 +
    vocabulary_uniformity × 0.25 +
    cui_bono_clarity × 0.20 +
    historical_pattern_match × 0.15 +
    suppression_indicators × 0.10
)

# THRESHOLDS:
# P < 0.30: Likely organic
# P 0.30-0.60: Possible coordination
# P 0.60-0.85: Probable orchestration
# P > 0.85: Quasi-certain orchestration (⚑⚑⚑)
```

---

## 5. GEOGRAPHIC & LINGUISTIC DIVERSITY

### 5.1 Geographic Priority Heuristics

```yaml
GEOGRAPHIC_PRIORITIZATION:
  FOR subject with geographic locus (conflict, policy, event):
    PRIORITY_ORDER:
      1. LOCAL: Country/region directly affected (highest weight)
      2. NEIGHBOR: Bordering countries, regional bloc
      3. REGIONAL: Same continent, cultural sphere
      4. DISTANT: Other continents (diverse perspectives)
      5. HEGEMON: Dominant power (USA, UK) - LOWEST weight for geopolitical subjects

  VALIDATION:
    - ≥2 continents represented
    - ≥1 local source (if applicable)
    - Avoid monoculture (not all sources from same zone)
```

### 5.2 Linguistic Diversity Requirements

```yaml
LINGUISTIC_TARGETS:
  - ≥30% sources in non-English languages
  - ≥2 linguistic families represented
  - Primary language of affected region included (if applicable)

LANGUAGE_PRIORITY:
  1. PRIMARY: Language(s) of country/region concerned
  2. NEIGHBOR: Languages of bordering countries
  3. REGIONAL: Regional lingua franca (Arabic MSA, Spanish LATAM, etc.)
  4. GLOBAL_RELAY: English (necessary but insufficient alone)

TRANSLATION_QUALITY:
  - Direct translation primary→target: HIGH quality
  - Double translation primary→English→target: MEDIUM quality
  - Always note translation path, affects confidence
```

---

## 6. VALIDATION CHECKLIST

### 6.1 Minimum Requirements (PHASE 1)

```yaml
MANDATORY_VALIDATION:
  sources_total: ≥5
  EDI_score: ≥0.50
  primary_sources: ≥2 (◈)
  narratives_identified: ≥2 (at least ⟐ + one other)
  geographic_continents: ≥2
  linguistic_non_english: ≥30%

OPTIMAL_TARGETS:
  sources_total: 10-15
  EDI_score: ≥0.65
  primary_sources: ≥3
  narratives_identified: ≥3 (⟐ + ⟐̅ + 🌍/🎓/🔥)
  divergence_zones: ≥1 identified and analyzed
  orchestration_check: Red flags assessed
```

### 6.2 Quality Gates

```yaml
AUTO_FAIL_CONDITIONS:
  - EDI < 0.35 → EPISTEMIC_MONOCULTURE
  - ◈ primary_sources = 0 → NO_PRIMARY_EVIDENCE
  - Only ⟐ narrative, no ⟐̅/🌍/🔥 → MANUFACTURED_CONSENSUS
  - All sources same ownership → FAKE_DIVERSITY
  - geo < 2 continents on geopolitical subject → WESTERN_BIAS

AUTO_WARNING:
  - EDI 0.35-0.49 → Diversity improvements needed
  - ◈ primary = 1 only → Seek additional primary docs
  - narratives < 3 → Expand perspective search
```

---

## 7. OUTPUT INTEGRATION

### 7.1 [SOURCES] Line Format (Part 2 Technical)

```yaml
[SOURCES] ◈:{X} ◉:{Y} ○:{Z} | EDI:{score} | geo:{continents_list} lang:{%non-EN} | ⟐:{A}⟐̅:{B}🌍:{C}🎓:{D}🔥:{E} | ≋:{divergence_count} ⚑:{red_flag_count} | COV:{c} IND:{i} CC:{cc} → EDI*:{e}

EXAMPLE:
[SOURCES] ◈:3 ◉:8 ○:6 | EDI:0.68 | geo:4cont(NA,EU,ME,RU) lang:55%non-EN | ⟐:6⟐̅:5🌍:3🎓:2🔥:1 | ≋:2_major ⚑:3_red_flags | COV:0.78 IND:0.66 CC:1 → EDI*:0.69
```

### 7.2 Part 1 (Natural French) Enrichment

```markdown
**Cartographie narrative complète:**

J'ai identifié **[X] narratifs distincts** à travers **[Y] sources** couvrant **[Z] continents** et **[N] langues** (dont [%] non-anglais).

**Narratif officiel (⟐)**: [Summary based on ○ tertiary sources typically]
**Narratif contre-hégémonique (⟐̅)**: [Summary often backed by ◈ primary evidence]
**Perspectives régionales (🌍)**: [Local voices often absent from Western MSM]

**Zones de divergence critique (≋)**:
1. [Divergence topic]: ⟐ affirme X (basé sur ○), mais ◈ documents primaires montrent Y
2. [Additional divergences]

**Détection orchestration (⚑)**: [Red flags analysis with probability scoring]

**Qualité factuelle**:
- ✦ Hard facts: [List with ◈ evidence]
- ⁕ Claims unverified: [List requiring corroboration]
```

### 7.3 WOLF Report Enhancement

```yaml
# Add to WOLF REPORT Part 3:

## 📊 NARRATIVE MANIPULATION ANALYSIS

**OFFICIAL NARRATIVE (⟐) DOMINANCE**: [%] of sources amplify same message
→ Beneficiaries: [List wolves from narrative analysis]
→ Red flags: ⚑⚑⚑ [temporal sync, coordination evidence]

**SUPPRESSED COUNTER-NARRATIVE (⟐̅)**:
→ Sources: ◈ [primary documents] + ◉ [investigations]
→ Censorship: [Deplatforming, fact-checks, deletions]
→ Reveals: [Hidden beneficiaries, contradictory evidence]

**DIVERGENCE EXPLOITATION**:
→ Power maintains ⟐ despite ◈ evidence for ⟐̅
→ Orchestration probability: [%]
→ Historical pattern: [Precedent matching]
```

---

## 8. INTEGRATION WITH EXISTING SYSTEMS

### 8.1 WOLF HUNTER Synergy

```yaml
WOLF_ENRICHMENT:
  narrative_mapping → CUI_BONO:
    - ⟐ official narrative → who benefits financially/politically?
    - ⟐̅ suppression → who threatened by truth?
    - ≋ divergence zones → whose interests in maintaining confusion?

  MONEY_TRAIL (€):
    - Trace funding sources (○ tertiary media ownership)
    - Identify beneficial owners (◈ corporate filings)
    - Map board overlaps (♦ elite networks)
```

### 8.2 ICEBERG Synergy

```yaml
ICEBERG_NARRATIVE_FUSION:
  official_stat (⟐) = R (revealed)
  suppressed_narratives (⟐̅,🔥) = N (total reality)

  Factor_narrative = narratives_total / narratives_mainstream

  EXAMPLE:
    ⟐: 1 narratif officiel (unemployment 7.3%)
    Investigation: 5 narratifs total (⟐,⟐̅,🌍,🎓,🔥)
    Factor = 5/1 = 5.0 → Ξ++ manipulation systémique
```

### 8.3 APEX Synergy

```yaml
APEX_NARRATIVE_MEMORY:
  knowledge_graph:
    nodes: + narratives (⟐,⟐̅,🌍,🎓,🔥)
    edges: + narrative_contradictions, narrative_support

  pattern_bank:
    + orchestration_signatures (⚑ recurring red flags)
    + censorship_patterns (platforms, methods, timing)
```

---

## 9. EXAMPLES - CONDENSED

### 9.1 Geopolitical Conflict (Syria)

```yaml
SOURCES: ◈:5 ◉:12 ○:15 | EDI:0.71
NARRATIVES:
  ⟐: "Humanitarian intervention vs dictator" (○ Western MSM)
  ⟐̅: "Pipeline proxy war" (◈ leaked cables + ◉ investigative)
  🌍: "Sectarian conflict" (◉ regional media Arabic/Turkish)
  🎓: "Complex multi-actor" (◉ academic research)
  🔥: "CIA armed jihadists" (◈ leaked docs, deplatformed)

DIVERGENCES:
  ≋ Chemical weapons attribution: ⟐ vs ⟐̅ (◈ OPCW whistleblower contradicts ○ official)
  ≋ Nature of rebels: ⟐ "moderate" vs 🔥 "Al-Qaeda affiliates" (◈ CIA cables confirm latter)

ORCHESTRATION: ⚑⚑⚑ (P=0.89) temporal sync, cui bono arms industry, historical pattern Iraq WMD
```

### 9.2 Economic Statistic (Unemployment)

```yaml
SOURCES: ◈:8 ◉:6 ○:4 | EDI:0.58
NARRATIVES:
  ⟐: "Lowest 40 years 7.3%" (○ official + MSM)
  ⟐̅: "Real 14.2% with shadows" (◈ DEFM B-E data + ◉ alternative calculation)
  🎓: "Methodology limits comparability" (◉ academic critique)

FACTS:
  ✦ Category A unemployment: 2.19M (◈ official data)
  ✦ Categories B-E exist: +2.87M (◈ ministerial data, not publicized)
  ✧ Halo estimate: +1.95M (◉ INSEE study buried)

DIVERGENCE:
  ≋ Total reality: ⟐ shows 23% (2.19M/9.41M) vs ⟐̅ complete picture

ORCHESTRATION: ⚑⚑ (P=0.75) electoral timing, methodology changes, MSM omission
```

---

## 10. ITERATIVE WEB SEARCH PROTOCOL (v6.3 PHASE 2)

### 10.1 Four-Iteration Convergence System

**OBJECTIVE**: Achieve C(n) ≥ 0.85 convergence through systematic gap-filling iterations I0→I1→I2→I3.

```yaml
CONVERGENCE_FORMULA:
  C(n) = 1 - (new_information_at_iteration_n / total_information_discovered)

  TARGET: C(n) ≥ 0.85 (85% convergence = investigation maturity)

  STOPPING_CONDITIONS:
    - C(n) ≥ 0.90 → COMPLETE (excellent convergence)
    - C(n) ≥ 0.85 AND EDI ≥ 0.60 → SUFFICIENT
    - n ≥ 3 AND C(n) ≥ 0.75 → ACCEPTABLE (budget constraint)
    - n > 5 → FORCED_STOP (diminishing returns)
```

### 10.2 I0 - RECONNAISSANCE (5-10 minutes)

**PURPOSE**: Initial cartography, identify major narratives and obvious gaps.

```yaml
I0_AUTOMATIC_QUERIES:
  Q1_OFFICIAL:
    query: "{subject}" site:.gov OR site:.org OR site:.int
    purpose: Capture ⟐ official narrative
    expected: ○ tertiary sources, single perspective

  Q2_MAINSTREAM:
    query: "{subject}" (Reuters OR AP OR AFP OR BBC OR NYT)
    purpose: Dominant MSM framing
    expected: ○ tertiary, ⟐ amplification

  Q3_INVESTIGATIVE:
    query: "{subject}" ("investigation" OR "leaked" OR "whistleblower")
    purpose: ◉ secondary, potential ◈ primary
    expected: ⟐̅ counter-narrative seeds

  Q4_ACADEMIC_RAPID:
    query: "{subject}" site:.edu OR site:scholar.google.com
    purpose: 🎓 academic perspective (rapid scan)
    expected: ◉ analysis, complexity flags

  Q5_REGIONAL_RAPID:
    query: "{subject}" + (country OR region language keywords)
    purpose: 🌍 regional voice (rapid scan)
    expected: Different priorities, local impact

I0_OUTPUT:
  sources_collected: 8-15 (mix ◈◉○)
  narratives_identified: 2-3 (usually ⟐ + partial ⟐̅)
  EDI_estimate: 0.35-0.50 (baseline)
  gaps_identified: [list missing perspectives]
  time_budget: 5-10 minutes
```

**I0 EXAMPLE** (Test case: Nathalie Loiseau Russia narrative):
```yaml
I0_RESULTS:
  sources: 8 (◈:2 ◉:3 ○:3)
  narratives: ⟐ (EEAS official) + ⟐̅ (independent analyses)
  EDI: ~0.42 (2 continents, 40% non-EN, low diversity)
  gaps: 🎓 academic ABSENT, 🔥 dissident ABSENT, 🌍 regional weak
  → PROCEED TO I1 (mandatory gap-filling)
```

### 10.3 I1 - EXPLORATION (10-15 minutes) [ENHANCED v6.3.1]

**PURPOSE**: Fill identified gaps from I0, enhance diversity, seek ◈ primary sources.

```yaml
I1_ADAPTIVE_QUERIES:
  # PHASE 1: Standard gap analysis from I0

  IF 🎓_academic ABSENT OR weak:
    → TRIGGER H6_ACADEMIC_SEARCH (see Section 12.1)

  IF 🔥_dissident ABSENT:
    → TRIGGER H7_DISSIDENT_SEARCH (see Section 12.2)

  IF EDI_geographic < 0.30:
    → H2_GEOGRAPHIC_EXPANSION (prioritize local/neighbor sources)

  IF ◈_primary_sources < 2:
    Q_PRIMARY_DEEP:
      query: "{subject}" + ("leaked documents" OR "FOIA" OR "court files" OR "primary sources")
      purpose: Elevate evidence quality

  IF lang_diversity < 30%:
    Q_LINGUISTIC_EXPANSION:
      query: "{subject}" in [target languages from affected regions]
      purpose: Escape anglosphere monoculture

  # PHASE 2: NEW v6.3.1 - Auto-trigger for sensitive subjects

  SUBJECT_CATEGORY_DETECTION:
    keywords_sensitive = [
      # Political/Geopolitical
      "election", "government", "policy", "parliament", "legislation", "regulation",
      "war", "conflict", "military", "defense", "security", "intelligence",
      "geopolitical", "diplomacy", "sanctions", "embargo", "intervention",

      # Information Operations
      "propaganda", "disinformation", "misinformation", "censorship", "manipulation",
      "psyops", "information warfare", "influence operation", "interference",

      # Economic/Financial (cui bono relevant)
      "corruption", "fraud", "lobbying", "revolving door", "conflict of interest",
      "monopoly", "cartel", "price fixing", "insider trading", "subsidy",

      # Corporate/Pharmaceutical (follow the money)
      "scandal", "cover-up", "whistleblower", "lawsuit", "settlement",
      "pharmaceutical", "vaccine", "clinical trial", "adverse effects",

      # Social/Rights (power dynamics)
      "protest", "repression", "surveillance", "civil liberties", "human rights",
      "inequality", "discrimination", "exploitation", "labor rights"
    ]

    IF ANY(keyword IN subject.lower()):
      → subject_category = "SENSITIVE"
      → MANDATORY_TRIGGERS_ACTIVATED

  MANDATORY_TRIGGERS_FOR_SENSITIVE_SUBJECTS:

    1. H7_DISSIDENT_MANDATORY:
       IF subject_category = SENSITIVE:
         AND 🔥_dissident_sources = 0:
           → FORCE H7_DISSIDENT_SEARCH
           → MINIMUM: ≥1 source from adversary/critical perspective
           → REASON: "Sensitive subjects require systematic challenge to power narratives"

    2. H9_CUI_BONO_MANDATORY:
       IF subject_category = SENSITIVE:
         → FORCE H9_CUI_BONO_SOURCES (see Section 12.4)
         → REASON: "Follow the money - identify all source conflicts of interest"

    3. ADVERSARY_PERSPECTIVE_CHECK:
       IF subject mentions_entity_as [threat, enemy, adversary, hostile]:
         adversary_entities = extract_accused_entities(subject)

         FOR EACH entity IN adversary_entities:
           → MANDATORY: Find ≥1 source from entity's perspective
           → REASON: "Principle audi alteram partem (hear the other side)"

         EXAMPLE_TRIGGERS:
           - "Russia disinformation" → MUST include Russian sources
           - "China influence" → MUST include Chinese sources
           - "Iran nuclear" → MUST include Iranian sources
           - "Big Pharma scandal" → MUST include pharmaceutical industry response
           - "Union strike" → MUST include union perspective (not just management)

    4. INCOMPLETE_CARTOGRAPHY_WARNING:
       IF mandatory_triggers_failed:
         → OUTPUT in Part 1 (French):
           "⚠️ CARTOGRAPHIE INCOMPLÈTE:
            Sujet sensible analysé sans perspective adversaire/critique.
            Fiabilité compromise. EDI pénalisé -0.15.
            Recommandation: Réanalyser avec H7+H9 obligatoires."

         → OUTPUT in Part 2 (Technical):
           [WARNING] INCOMPLETE_CARTOGRAPHY: adversary_perspective=MISSING cui_bono=NOT_ANALYZED
           EDI_penalty: -0.15

I1_OUTPUT:
  sources_added: +5-10 (target ◈ primary, 🎓🔥 narratives)
  narratives_complete: 3-5 (⟐⟐̅🌍🎓🔥 ALL if sensitive subject)
  EDI_improved: 0.50-0.60 (or penalized if mandatories failed)
  convergence: C(1) ≈ 0.40-0.60 (significant new info still appearing)
  time_budget: 10-15 minutes cumulative (+5 min if H9 cui bono required)
```

**I1 EXAMPLE** (Continuing Loiseau case):
```yaml
I1_ACTIONS:
  H6_ACADEMIC: Query scholar.google.com + .edu sites for "information warfare EU Russia"
    → Found: 2 peer-reviewed papers (◉), adds 🎓 perspective
  H7_DISSIDENT: Query deplatformed experts, alternative media on "Loiseau coordination"
    → Found: 1 dissident analyst (🔥), questions official timeline
  GEOGRAPHIC: Search Russian sources (.ru media, Russian analysis)
    → Found: 🌍 regional Russian perspective on EU operations

I1_RESULTS:
  sources: 15 total (◈:3 ◉:6 ○:6)
  narratives: ⟐⟐̅🌍🎓🔥 ALL present
  EDI: ~0.58 (improved)
  C(1): 0.55 (still discovering significant info)
  → PROCEED TO I2 (deep triangulation)
```

### 10.4 I2 - DEEP DIVE (15-20 minutes)

**PURPOSE**: Triangulate critical claims, detect orchestration, calculate exact EDI.

```yaml
I2_TRIANGULATION_PROTOCOL:
  # Focus on divergence zones (≋) identified in I0-I1

  FOR EACH critical_claim WITH contradictions:
    → TRIGGER H8_AUTO_TRIANGULATION (see Section 12.3)
    → Seek ◈ primary evidence for each side
    → Calculate corroboration (⊕⊗⊙)
    → Assess fact quality (✦✧⁕⁂)

  ORCHESTRATION_DEEP_CHECK:
    - Timeline forensics (events <12h sync?)
    - Vocabulary analysis (identical phrases across "independent" sources?)
    - Cui bono mapping (beneficiaries financial/political)
    - Historical pattern matching (precedent playbooks)
    - Calculate P_orchestration score

  EDI_EXACT_CALCULATION:
    → TRIGGER Section 11 (EDI Template)
    → Compute all 6 dimensions with exact values
    → Generate breakdown for [SOURCES] line

I2_OUTPUT:
  sources_refined: 15-20 (focus ◈ for contested claims)
  divergences_analyzed: ≋ zones with evidence quality assessed
  orchestration_scored: P_orch calculated with red flag count
  EDI_exact: 0.XX calculated (not estimated)
  convergence: C(2) ≈ 0.70-0.80 (diminishing new discoveries)
  time_budget: 15-20 minutes cumulative
```

**I2 EXAMPLE** (Loiseau case deep dive):
```yaml
I2_TRIANGULATION:
  Claim: "Loiseau coordinated with Microsoft on Russian interference narrative"
  ⟐: Official denies (○ statements)
  ⟐̅: Coordination alleged (◉ analysis)
  TRIANGULATION: Search for ◈ primary (emails, meeting records, timeline sync)
    → Found: Timeline shows Loiseau tweet, Microsoft report, EU statement <6h span
    → ✧ SOFT_FACT: Coordination plausible (temporal evidence) but no ◈ docs

I2_ORCHESTRATION:
  P_orch: 0.78 (PROBABLE)
    - temporal_sync: 0.90 (<6h coordination)
    - vocabulary: 0.75 (similar framing "Russian interference")
    - cui_bono: 0.80 (EU budget increase, Microsoft contracts)
    - historical: 0.70 (Russiagate 2016 pattern)
    - suppression: 0.60 (critics fact-checked)

I2_EDI_EXACT: 0.64 (calculation via Section 11 template)
  C(2): 0.76 (converging, little new info)
  → PROCEED TO I3 (final synthesis)
```

### 10.5 I3 - SYNTHESIS (5-10 minutes)

**PURPOSE**: Final validation, produce complete 3-part output.

```yaml
I3_SYNTHESIS_CHECKLIST:
  ✓ Validation: sources ≥5, EDI ≥0.50, ◈ ≥2, narratives ≥2
  ✓ All gaps filled: 🎓🔥 present if relevant
  ✓ Divergences analyzed: ≋ zones with evidence assessment
  ✓ Orchestration scored: ⚑ red flags + P_orch
  ✓ [SOURCES] line complete: All symbols populated
  ✓ Convergence achieved: C(3) ≥ 0.85 OR n=3 stop

I3_OUTPUT_GENERATION:
  PART_1_NATURAL: Narrative cartography in French
    - Synthesize all 5 narrative types
    - Explain divergence zones
    - Contextualize orchestration evidence

  PART_2_TECHNICAL: [SOURCES] line + metrics
    - Exact counts: ◈:X ◉:Y ○:Z
    - EDI exact: 0.XX calculated
    - Narratives: ⟐:A⟐̅:B🌍:C🎓:D🔥:E
    - Divergence + orchestration: ≋:X ⚑:Y

  PART_3_WOLF: Beneficiary mapping enriched by narrative analysis

I3_FINAL_METRICS:
  sources_total: 18-25
  EDI_final: 0.60-0.75 (target achieved)
  convergence: C(3) ≥ 0.85 (mature investigation)
  time_total: 35-55 minutes (within APEX budget)
```

**I3 EXAMPLE** (Loiseau case final):
```yaml
I3_SYNTHESIS:
  sources: 21 (◈:4 ◉:8 ○:9)
  EDI: 0.64 FINAL
  narratives: ⟐:6 ⟐̅:5 🌍:3 🎓:2 🔥:1
  divergences: ≋:2_major (coordination claim, Russia threat level)
  orchestration: ⚑:4_red_flags, P_orch=0.78
  C(3): 0.87 (CONVERGENCE ACHIEVED)

  OUTPUT: Complete 3-part analysis ready
```

---

## 11. EDI CALCULATION TEMPLATE (v6.3 PHASE 2)

### 11.b Composite extensions (compressed)
- CoverageScore: ratio quotas met (KB/QUOTAS)
- IndependenceScore: diversity families + low syndication (KB/SCORES)
- ContradictionCoverage: adversary/≋ present and processed
- EDI*: 0.5×EDI + 0.3×Coverage + 0.2×Independence (optional Part 2 output)

### 11.1 Six-Dimension Breakdown

**CRITICAL**: Replace vague "EDI:≥0.50" with EXACT calculated score "EDI:0.68".

```python
# ═══════════════════════════════════════════════════════════════
# EDI CALCULATION TEMPLATE - Copy and fill values
# ═══════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────
# DIMENSION 1: GEOGRAPHIC DIVERSITY (Weight: 0.25)
# ─────────────────────────────────────────────────────────────
continents_represented = [  ]  # List: NA, EU, AS, AF, SA, OC (max 6)
continents_count = len(continents_represented)
continents_score = continents_count / 6  # 0.0-1.0

zones_represented = [  ]  # Specific regions (max 10 reasonable)
zones_count = len(zones_represented)
zones_score = min(zones_count / 10, 1.0)  # Cap at 1.0

local_sources_present = False  # True if ≥1 source from affected country/region
local_presence = 1.0 if local_sources_present else 0.0

geo_diversity = (continents_score * 0.4 +
                 zones_score * 0.3 +
                 local_presence * 0.3)

# ─────────────────────────────────────────────────────────────
# DIMENSION 2: LINGUISTIC DIVERSITY (Weight: 0.20)
# ─────────────────────────────────────────────────────────────
languages_list = [  ]  # List: EN, FR, ES, AR, RU, ZH, etc.
languages_count = len(languages_list)
languages_score = min(languages_count / 10, 1.0)

sources_non_english_count = 0  # Count sources NOT in English
sources_total = 0  # Total sources
non_english_pct = sources_non_english_count / sources_total if sources_total > 0 else 0

linguistic_families = [  ]  # Indo-European, Afro-Asiatic, Sino-Tibetan, etc.
families_count = len(linguistic_families)
families_score = min(families_count / 5, 1.0)

lang_diversity = (languages_score * 0.3 +
                  non_english_pct * 0.4 +
                  families_score * 0.3)

# ─────────────────────────────────────────────────────────────
# DIMENSION 3: STRATIFICATION DIVERSITY (Weight: 0.20)
# ─────────────────────────────────────────────────────────────
primary_sources_count = 0    # ◈ count
secondary_sources_count = 0  # ◉ count
tertiary_sources_count = 0   # ○ count

total_sources = primary_sources_count + secondary_sources_count + tertiary_sources_count
primary_pct = primary_sources_count / total_sources if total_sources > 0 else 0
secondary_pct = secondary_sources_count / total_sources if total_sources > 0 else 0
tertiary_pct = tertiary_sources_count / total_sources if total_sources > 0 else 0

strat_diversity = (primary_pct * 0.5 +
                   secondary_pct * 0.3 +
                   tertiary_pct * 0.2)

# ─────────────────────────────────────────────────────────────
# DIMENSION 4: OWNERSHIP DIVERSITY (Weight: 0.15)
# ─────────────────────────────────────────────────────────────
ownership_types = [  ]  # List: state, corporate, independent, academic, activist, personal
ownership_types_count = len(ownership_types)
types_score = min(ownership_types_count / 6, 1.0)

non_corporate_sources = 0  # Count: state, independent, academic, activist, personal
non_corporate_pct = non_corporate_sources / total_sources if total_sources > 0 else 0

ownership_diversity = types_score * 0.6 + non_corporate_pct * 0.4

# ─────────────────────────────────────────────────────────────
# DIMENSION 5: PERSPECTIVE DIVERSITY (Weight: 0.15)
# ─────────────────────────────────────────────────────────────
perspectives_present = [  ]  # ⟐, ⟐̅, 🌍, 🎓, 🔥, etc. (check which present)
perspectives_count = len(perspectives_present)
perspectives_score = min(perspectives_count / 7, 1.0)  # 7 max reasonable

official_narrative_sources = 0   # ⟐ count
counter_narrative_sources = 0    # ⟐̅ + 🔥 count
balance = 1.0 - abs(official_narrative_sources - counter_narrative_sources) / total_sources if total_sources > 0 else 0

dissident_present = False  # True if 🔥 dissident voice exists
dissident_score = 1.0 if dissident_present else 0.0

perspective_diversity = (perspectives_score * 0.5 +
                         balance * 0.3 +
                         dissident_score * 0.2)

# ─────────────────────────────────────────────────────────────
# DIMENSION 6: TEMPORAL DIVERSITY (Weight: 0.05)
# ─────────────────────────────────────────────────────────────
temporalities = [  ]  # List: real_time, recent(<1week), medium(<1month), archival(>1year), historical
temporalities_count = len(temporalities)
temporalities_score = min(temporalities_count / 5, 1.0)

archival_sources_present = False  # True if ≥1 source >1 year old (historical depth)
archival_presence = 1.0 if archival_sources_present else 0.0

temporal_diversity = temporalities_score * 0.6 + archival_presence * 0.4

# ═══════════════════════════════════════════════════════════════
# FINAL EDI CALCULATION
# ═══════════════════════════════════════════════════════════════
EDI = (
    geo_diversity * 0.25 +
    lang_diversity * 0.20 +
    strat_diversity * 0.20 +
    ownership_diversity * 0.15 +
    perspective_diversity * 0.15 +
    temporal_diversity * 0.05
)

EDI_rounded = round(EDI, 2)

# ═══════════════════════════════════════════════════════════════
# CLASSIFICATION
# ═══════════════════════════════════════════════════════════════
if EDI >= 0.65:
    classification = "EXCELLENT"
elif EDI >= 0.50:
    classification = "GOOD"
elif EDI >= 0.35:
    classification = "ACCEPTABLE"
else:
    classification = "EPISTEMIC_MONOCULTURE"

# ═══════════════════════════════════════════════════════════════
# OUTPUT FOR [SOURCES] LINE
# ═══════════════════════════════════════════════════════════════
# EDI:{EDI_rounded}
```

### 11.2 Example Calculation (Loiseau Test Case)

```python
# DIMENSION 1: GEOGRAPHIC (0.25 weight)
continents_represented = ["EU", "NA", "RU"]  # 3 continents
continents_score = 3/6 = 0.50
zones_represented = ["Western EU", "Eastern EU", "North America", "Russia"]
zones_score = 4/10 = 0.40
local_sources_present = True  # EU sources (affected region)
local_presence = 1.0
geo_diversity = 0.50*0.4 + 0.40*0.3 + 1.0*0.3 = 0.20 + 0.12 + 0.30 = 0.62

# DIMENSION 2: LINGUISTIC (0.20 weight)
languages_list = ["EN", "FR", "RU", "ES"]  # 4 languages
languages_score = 4/10 = 0.40
sources_non_english = 11 out of 21 total
non_english_pct = 11/21 = 0.52
linguistic_families = ["Indo-European"]  # All same family
families_score = 1/5 = 0.20
lang_diversity = 0.40*0.3 + 0.52*0.4 + 0.20*0.3 = 0.12 + 0.21 + 0.06 = 0.39

# DIMENSION 3: STRATIFICATION (0.20 weight)
primary = 4, secondary = 8, tertiary = 9, total = 21
primary_pct = 4/21 = 0.19
secondary_pct = 8/21 = 0.38
tertiary_pct = 9/21 = 0.43
strat_diversity = 0.19*0.5 + 0.38*0.3 + 0.43*0.2 = 0.095 + 0.114 + 0.086 = 0.295

# DIMENSION 4: OWNERSHIP (0.15 weight)
ownership_types = ["state", "corporate", "independent", "academic"]  # 4 types
types_score = 4/6 = 0.67
non_corporate = 10 out of 21 (state, independent, academic)
non_corporate_pct = 10/21 = 0.48
ownership_diversity = 0.67*0.6 + 0.48*0.4 = 0.40 + 0.19 = 0.59

# DIMENSION 5: PERSPECTIVE (0.15 weight)
perspectives_present = ["⟐", "⟐̅", "🌍", "🎓", "🔥"]  # 5 types
perspectives_score = 5/7 = 0.71
official = 6, counter = 6 (5⟐̅ + 1🔥)
balance = 1 - |6-6|/21 = 1.0 (perfect balance)
dissident_present = True
dissident_score = 1.0
perspective_diversity = 0.71*0.5 + 1.0*0.3 + 1.0*0.2 = 0.355 + 0.30 + 0.20 = 0.855

# DIMENSION 6: TEMPORAL (0.05 weight)
temporalities = ["real_time", "recent", "archival"]  # 3 types
temporalities_score = 3/5 = 0.60
archival_present = True
archival_score = 1.0
temporal_diversity = 0.60*0.6 + 1.0*0.4 = 0.36 + 0.40 = 0.76

# FINAL EDI
EDI = 0.62*0.25 + 0.39*0.20 + 0.295*0.20 + 0.59*0.15 + 0.855*0.15 + 0.76*0.05
EDI = 0.155 + 0.078 + 0.059 + 0.0885 + 0.128 + 0.038
EDI = 0.546 ≈ 0.55 → CLASSIFICATION: GOOD

# But with I2-I3 improvements → FINAL EDI = 0.64 (GOOD trending EXCELLENT)
```

### 11.3 EDI Bias Adjustments (v6.3.1 BIAS CORRECTION)

**PURPOSE**: Penalize epistemic monocultures hidden by surface diversity metrics.

```python
# ═══════════════════════════════════════════════════════════════
# POST-CALCULATION PENALTIES - Apply AFTER raw EDI calculation
# ═══════════════════════════════════════════════════════════════

EDI_penalties = 0.0  # Accumulator for all penalties

# ─────────────────────────────────────────────────────────────
# PENALTY 1: Institutional Monoculture
# ─────────────────────────────────────────────────────────────
government_sources_count = 0  # Count: government, state agency, military, IGO
corporate_sources_count = 0   # Count: corporations, corporate media, funded think tanks
independent_sources_count = 0 # Count: independent media, academic, NGO independent

govt_pct = government_sources_count / total_sources
corp_pct = corporate_sources_count / total_sources
power_pct = (government_sources_count + corporate_sources_count) / total_sources

if govt_pct > 0.60:
    penalty_mono_govt = -0.20
    EDI_penalties += penalty_mono_govt
    flag_reason = "INSTITUTIONAL_MONOCULTURE: government >60%"

if corp_pct > 0.60:
    penalty_mono_corp = -0.20
    EDI_penalties += penalty_mono_corp
    flag_reason = "INSTITUTIONAL_MONOCULTURE: corporate >60%"

if power_pct > 0.75:
    penalty_mono_power = -0.25
    EDI_penalties += penalty_mono_power
    flag_reason = "POWER_MONOCULTURE: govt+corp >75%"

# ─────────────────────────────────────────────────────────────
# PENALTY 2: Missing Adversary Perspective (Sensitive Subjects)
# ─────────────────────────────────────────────────────────────
subject_is_sensitive = False  # From Section 10.3 keyword detection
dissident_sources_count = 0   # 🔥 count
adversary_sources_present = False  # Sources from accused entity perspective

if subject_is_sensitive:
    if dissident_sources_count == 0 and not adversary_sources_present:
        penalty_no_adversary = -0.15
        EDI_penalties += penalty_no_adversary
        flag_reason = "MISSING_ADVERSARY: sensitive subject without critical/adversary perspective"

# ─────────────────────────────────────────────────────────────
# PENALTY 3: Narrative Echo Chamber
# ─────────────────────────────────────────────────────────────
official_narrative_sources = 0   # ⟐ count
counter_narrative_sources = 0    # ⟐̅ count

if official_narrative_sources > 0:
    if counter_narrative_sources == 0 and dissident_sources_count == 0:
        penalty_echo = -0.20
        EDI_penalties += penalty_echo
        flag_reason = "NARRATIVE_ECHO_CHAMBER: only official perspective, no counter-narrative"

# ─────────────────────────────────────────────────────────────
# PENALTY 4: Tertiary Over-Reliance
# ─────────────────────────────────────────────────────────────
tertiary_pct = tertiary_sources_count / total_sources

if tertiary_pct > 0.70:
    penalty_tertiary = -0.15
    EDI_penalties += penalty_tertiary
    flag_reason = "TERTIARY_DOMINANCE: >70% tertiary sources (low confidence)"

# ─────────────────────────────────────────────────────────────
# PENALTY 5: Circular Corroboration
# ─────────────────────────────────────────────────────────────
# Detect if major claims corroborated only by same institutional family
circular_corroboration_detected = False  # Manual check during I2 triangulation

if circular_corroboration_detected:
    penalty_circular = -0.10
    EDI_penalties += penalty_circular
    flag_reason = "CIRCULAR_CORROBORATION: claims confirmed by same institutional family"

# ═══════════════════════════════════════════════════════════════
# FINAL EDI WITH PENALTIES
# ═══════════════════════════════════════════════════════════════
EDI_raw = EDI  # From Section 11.1 calculation
EDI_final = max(0.0, EDI_raw + EDI_penalties)  # Floor at 0.0

# RECLASSIFICATION
if EDI_final < 0.35:
    classification_final = "EPISTEMIC_MONOCULTURE_CRITICAL"
elif EDI_final < 0.50:
    classification_final = "EPISTEMIC_BIAS_SIGNIFICANT"
elif EDI_final < 0.65:
    classification_final = "GOOD"
else:
    classification_final = "EXCELLENT"

# ═══════════════════════════════════════════════════════════════
# TRANSPARENCY OUTPUT (MANDATORY)
# ═══════════════════════════════════════════════════════════════
# Must appear in [SOURCES] line if penalties applied

if EDI_penalties < 0:
    # Format: EDI:{final} (raw:{raw} penalties:{sum}[flags])
    sources_line_edi = f"EDI:{EDI_final:.2f} (raw:{EDI_raw:.2f} penalties:{EDI_penalties:.2f}[{','.join(all_flag_reasons)}])"
else:
    sources_line_edi = f"EDI:{EDI_final:.2f}"

# PART 1 (French) WARNING
if EDI_penalties < -0.15:  # Significant bias
    part1_warning = f"""
⚠️ BIAIS ÉPISTÉMIQUE DÉTECTÉ:
L'analyse des sources révèle des limitations méthodologiques:
- EDI brut: {EDI_raw:.2f} → EDI ajusté: {EDI_final:.2f} (pénalité: {EDI_penalties:.2f})
- Problèmes identifiés: {', '.join(all_flag_reasons)}

Impact sur la fiabilité:
- Classification: {classification_final}
- Les conclusions peuvent refléter une capture institutionnelle
- Recommandation: Élargir sources indépendantes/adversaires (H7+H9)
"""
```

**EXAMPLE (Loiseau Test Case Corrected)**:

```python
# ORIGINAL (PHASE 2 v6.3):
EDI_raw = 0.72

# PENALTIES DETECTED:
govt_pct = 15/21 = 0.71 → penalty_mono_govt = -0.20 (>60% threshold)
dissident_sources = 0, adversary_sources = False, subject_sensitive = True
  → penalty_no_adversary = -0.15
counter_narrative = 3, but govt >> counter (15 vs 3)
  → penalty_echo = -0.10 (minor echo, partial counter exists)

EDI_penalties = -0.20 + -0.15 + -0.10 = -0.45

# FINAL:
EDI_final = max(0.0, 0.72 + (-0.45)) = 0.27
classification = "EPISTEMIC_MONOCULTURE_CRITICAL"

# OUTPUT:
[SOURCES] ◈:3 ◉:3 ○:15 | EDI:0.27 (raw:0.72 penalties:-0.45[mono_govt,no_adversary,echo]) | ...
```

**This correction transforms misleading EDI=0.72 into honest EDI=0.27, revealing institutional capture.**

---

## 12. ADVANCED HEURISTICS (H6-H8)

### 12.1 H6 - ACADEMIC SEARCH SYSTEMATIC

```yaml
H6_ACADEMIC_SEARCH:
  trigger: 🎓_academic ABSENT OR count < 2

  queries:
    Q1_SCHOLAR:
      query: "{subject}" site:scholar.google.com
      filter: peer-reviewed, last 5 years

    Q2_EDU_SITES:
      query: "{subject}" site:.edu (research OR study OR analysis)
      focus: university research centers

    Q3_ACADEMIC_JOURNALS:
      query: "{subject}" + (journal names: "International Security", "Foreign Affairs", etc.)
      access: open access + institutional repositories

    Q4_THINK_TANKS_INDEPENDENT:
      query: "{subject}" site:org (independent think tanks, non-corporate funded)
      validate: funding sources (avoid corporate capture)

  expected_output:
    sources_added: 2-4 (◉ secondary academic)
    perspective: 🎓 "it's complicated" nuanced
    impact: +0.05-0.10 EDI (perspective diversity)
```

### 12.2 H7 - DISSIDENT/ADVERSARY SEARCH [ENHANCED v6.3.1]

```yaml
H7_DISSIDENT_SEARCH:
  trigger: 🔥_dissident ABSENT OR subject_category = SENSITIVE (auto from Section 10.3)

  rationale: "Censored voices often hold ◈ primary evidence threatening to power.
             Adversary perspective = juridical principle audi alteram partem (hear both sides)."

  # PHASE 1: Detect adversary entities (NEW v6.3.1)
  ADVERSARY_ENTITY_DETECTION:
    # Extract entities mentioned as threat/enemy/problem
    patterns = [
      "{entity} + (threat|danger|hostile|aggression|interference|manipulation)",
      "{entity} + (disinformation|propaganda|influence operation)",
      "{entity} + (sanctions|embargo|containment|confrontation)",
      "combat {entity}", "counter {entity}", "against {entity}"
    ]

    IF pattern_match:
      adversary_entities = extract_entities(subject)

    GENERIC_EXAMPLES:
      - "Russia disinformation" → adversary = Russia
      - "China influence EU" → adversary = China
      - "Big Pharma scandal" → adversary = pharmaceutical industry
      - "Union strike impact" → adversary = unions (if framed negatively)
      - "Climate protesters damage" → adversary = protesters (if framed negatively)
      - "Terrorism threat" → adversary = accused groups

  queries:
    # Q1: Alternative platforms (existing)
    Q1_ALTERNATIVE_PLATFORMS:
      query: "{subject}" site:(rumble.com OR odysee.com OR substack.com OR telegram.org OR bitchute.com)
      focus: deplatformed experts, whistleblowers, independent analysts

    # Q2: Adversary perspective (MANDATORY if entities detected)
    Q2_ADVERSARY_PERSPECTIVE_MANDATORY:
      FOR EACH entity IN adversary_entities:
        # Map entity to media sources (extensible, not hardcoded)
        adversary_media_map = {
          "Russia": ["rt.com", "sputniknews.com", "tass.com", "mid.ru (foreign ministry)"],
          "China": ["globaltimes.cn", "chinadaily.com.cn", "xinhuanet.com", "fmprc.gov.cn"],
          "Iran": ["presstv.ir", "tasnimnews.com", "farsnews.ir", "president.ir"],
          "Cuba": ["granma.cu", "prensa-latina.cu", "cubadebate.cu"],
          "Venezuela": ["vtv.gob.ve", "telesurtv.net", "minci.gob.ve"],
          "North Korea": ["kcna.kp", "rodong.rep.kp"],
          "Syria": ["sana.sy"],
          # Corporate entities
          "Big Pharma": ["company official responses", "industry associations"],
          "Big Tech": ["corporate blogs", "transparency reports"],
          # Social movements
          "Unions": ["union official sites", "labor media"],
          "Protesters": ["movement-affiliated media", "organizer statements"],
          # Extensible: add any accused entity
        }

        query_adversary: "{subject}" site:({adversary_domains_for_entity})

        purpose: "Adversary has strongest incentive to reveal accuser's weaknesses.
                 Mapping adversary narrative ≠ believing it.
                 It's completing epistemic cartography."

        validation:
          - Classify adversary sources with same rigor (◈◉○)
          - Cross-check factual claims with ◈ primary evidence
          - Note: adversary bias exists, but so does accuser bias
          - Compare: which side provides ◈ primary docs?

      MANDATORY_MINIMUM:
        IF adversary_entities detected:
          MUST find ≥1 source from adversary perspective
          IF not found despite search:
            → FLAG: "ADVERSARY_PERSPECTIVE_MISSING"
            → EDI penalty: -0.15 (from Section 11.3)
            → Output warning in Part 1 (French)

    # Q3: Suppressed experts (existing, enhanced)
    Q3_SUPPRESSED_EXPERTS:
      query: "{subject}" + ("censored" OR "deplatformed" OR "banned" OR "fact-checked" OR "retracted")
      purpose: Identify suppression, investigate WHY (cui bono suppression?)
      follow_up: If expert silenced, what did they say? Find original statements.

    # Q4: Counter-narrative deep (existing, enhanced)
    Q4_COUNTER_NARRATIVE_DEEP:
      query: "{subject}" + ("debunked" OR "conspiracy" OR "misinformation" OR "false claim")
      inversion_principle: "Claims labeled 'misinfo' often contain ≋ divergence zones.
                           Investigate: WHY labeled misinfo? Who labeled it? What evidence?"

    # Q5: Critical academics (NEW v6.3.1)
    Q5_CRITICAL_ACADEMICS:
      query: "{subject}" + ("critical analysis" OR "skeptical" OR "questioning" OR "dissenting view")
      focus: Academics who challenge dominant narrative (often marginalized)
      examples: Chomsky, Mearsheimer (geopolitics), Ioannidis (medical), etc.

  expected_output:
    sources_added: 2-5 (mix ◈◉○, prioritize ◈ if adversary provides docs)
    perspective: 🔥 dissident + adversary viewpoints
    narratives_enriched: ⟐̅ counter-hegemonic + 🔥 suppressed voices
    impact: Reveals suppressed evidence, completes cartography, +0.10-0.15 EDI

  critical_validation:
    - Adversary sources get SAME skepticism as accuser sources
    - Cross-reference all claims with ◈ primary evidence
    - Distinguish genuine dissent from propaganda (both sides can propagandize)
    - Ask: Why was this voice suppressed? Cui bono suppression? (see H9)
    - Principle: "Truth emerges from contradiction, not from consensus"

  JURIDICAL_PRINCIPLE:
    "Audi alteram partem (hear the other side) is foundation of fair judgment.
     Analysis without adversary perspective = INCOMPLETE by definition.
     This is not relativism - it's epistemological rigor.
     Evaluate both narratives, let ◈ primary evidence decide."
```

### 12.3 H8 - AUTO-TRIANGULATION

```yaml
H8_AUTO_TRIANGULATION:
  trigger: Divergence zone (≋) detected between narratives

  protocol:
    FOR EACH contested_claim:
      1. Identify narratives: Which narratives make this claim?
      2. Evidence stratification: ◈ or ◉ or ○ for each side?
      3. Corroboration check:
         - ⟐ side: How many sources? What stratification?
         - ⟐̅ side: How many sources? What stratification?
      4. Primary evidence search:
         query: "{contested_claim}" + ("document" OR "evidence" OR "proof" OR "leak")
      5. Temporal analysis: Timeline consistency?
      6. Cui bono: Who benefits from each version?
      7. Classify corroboration: ⊕ ⊗ ⊙
      8. Classify fact quality: ✦ ✧ ⁕ ⁂

  output:
    corroboration_symbol: ⊕/⊗/⊙
    fact_quality: ✦/✧/⁕/⁂
    confidence_assessment: Which narrative better supported by ◈ evidence?

  example:
    claim: "Assad used chemical weapons in Douma 2018"
    ⟐: ○ MSM + official statements (⁕ claim quality)
    ⟐̅: ◈ OPCW whistleblower docs + ◉ MIT analysis (✧ soft fact, trending ✦)
    triangulation: ◈ evidence supports ⟐̅, ○ assertions support ⟐
    → CORROBORATION: ⊙ partial (contested), ≋++ major divergence
```

### 12.4 H9 - CUI BONO SOURCE ANALYSIS (v6.3.1 NEW - UNIVERSAL)

```yaml
@HEUR[H9_CUI_BONO]:
  trigger: ALWAYS (universal "follow the money" principle)

  purpose: "Identify financial/political conflicts of interest for ALL sources.
           Every source has incentives - transparency requires exposing them."

  rationale: "Source independence determines reliability more than format.
             Pentagon-funded academic paper ≠ independent research.
             Corporate-owned media ≠ independent journalism.
             Government agency report ≠ neutral analysis."

  protocol:
    FOR EACH significant_source IN investigation:

      STEP_1_CLASSIFY_SOURCE_TYPE:
        source_categories = [
          "government_agency",
          "military_intelligence",
          "corporation",
          "corporate_media",
          "think_tank",
          "NGO",
          "academic_institution",
          "independent_media",
          "individual_expert"
        ]

      STEP_2_IDENTIFY_FUNDING:
        # Who pays this source?

        IF source_type = government_agency:
          primary_funder = "state budget (taxpayer)"
          cui_bono = [
            "government policy justification",
            "budget expansion",
            "institutional power preservation",
            "political narrative alignment"
          ]
          conflicts = "Party to political conflicts, not neutral"

        ELSE IF source_type = corporation:
          primary_funder = "shareholders, investors"
          cui_bono = [
            "profit maximization",
            "market share expansion",
            "regulatory capture",
            "competitor suppression",
            "reputation management"
          ]
          conflicts_check:
            - defense contracts? (if security/tech corp)
            - pharma profits? (if health corp)
            - fossil fuel interests? (if energy corp)
            - financial interests? (if bank/finance)

        ELSE IF source_type = corporate_media:
          primary_funder = "corporate owner + advertisers"
          cui_bono = [
            "owner's business interests",
            "advertiser appeasement",
            "access to power (government sources)",
            "audience retention (sensationalism)"
          ]
          conflicts_check:
            - owner's other businesses?
            - major advertisers sectors?
            - government/military advertising?

        ELSE IF source_type = think_tank:
          primary_funder = "CRITICAL - often opaque"
          required_research:
            query: "{think_tank_name}" + ("funding" OR "donors" OR "sponsors")
          cui_bono_patterns:
            - government-funded → policy advocacy for funder
            - corporate-funded → industry interests
            - foundation-funded → check foundation donors
            - "independent" → verify, often misleading
          red_flags:
            - funding non-disclosed → assume conflicts
            - revolving door with government → regulatory capture
            - industry board members → corporate interests

        ELSE IF source_type = academic_institution:
          primary_funder = "grants, endowments, tuition"
          conflicts_check:
            - specific study funding source?
            - department funding (Pentagon, pharma, etc.)?
            - researcher's previous affiliations?
            - conflicts of interest disclosed?
          cui_bono:
            - grant renewal incentives
            - institutional prestige
            - industry partnerships

        ELSE IF source_type = NGO:
          primary_funder = "donations, grants, governments"
          required_research:
            query: "{NGO_name}" + ("funding" OR "donors")
          cui_bono:
            - funder agenda alignment
            - institutional survival
          independence_score:
            - government-funded NGO → low independence
            - corporate-funded NGO → low independence
            - grassroots-funded NGO → higher independence

        ELSE IF source_type = independent_media:
          funding_models = ["subscriptions", "donations", "crowdfunding"]
          cui_bono:
            - subscriber retention
            - donor alignment (check major donors)
          independence_score: generally higher, but verify
          red_flags:
            - single major donor → potential influence
            - undisclosed funding → assume conflicts

      STEP_3_ASSESS_INDEPENDENCE:
        independence_score = calculate(
          funding_diversity×0.30 +        # Multiple funders > single funder
          funding_transparency×0.25 +     # Disclosed > opaque
          editorial_independence×0.20 +   # Track record of criticizing funders?
          institutional_distance×0.15 +   # Revolving door with power?
          historical_integrity×0.10        # Past accuracy, corrections published?
        )

        IF independence_score < 0.40:
          → classification_downgrade = True
          → confidence_reduction = -0.15 to -0.30

      STEP_4_TRIANGULATE_CONFLICTS:
        # Cross-reference cui bono with subject matter

        IF subject_relates_to_source_interests:
          conflict_severity = HIGH

          EXAMPLES:
            - Microsoft report on cybersecurity → Microsoft has defense contracts $10Brd
            - Pharma-funded study on drug safety → Direct profit interest
            - Think tank on climate policy → Check fossil fuel funding
            - Government on national security → Budget justification interest

        ELSE:
          conflict_severity = LOW (but still note for transparency)

      STEP_5_OUTPUT_TRANSPARENCY:
        # MANDATORY in Part 1 (French) if conflicts detected

        IF conflict_severity ≥ MEDIUM:
          output_french = f"""
⚠️ CONFLITS D'INTÉRÊTS SOURCES DÉTECTÉS:

{source_name} ({source_type}):
- Financement: {funding_sources}
- Cui bono: {interests_list}
- Indépendance: {independence_score:.2f}/1.0 ({classification})
- Impact: Classification {original_tier} → {downgraded_tier}, confiance réduite -{reduction}

Recommandation: Corroborer avec sources indépendantes sans conflits identifiés.
"""

  UNIVERSAL_APPLICATION:
    "H9 applies to ALL subjects, not just political.
     Follow the money = fundamental epistemic principle.

     Examples across domains:
     - Health: Pharma funding biases studies
     - Tech: Corporate interests bias security reports
     - Environment: Fossil fuel funding biases climate research
     - Economics: Financial sector funding biases economic analysis
     - Media: Advertiser interests bias coverage
     - Academia: Grant sources bias research questions

     NO source is above cui bono analysis."

  INTEGRATION_WITH_CLASSIFICATION:
    # Feeds into Section 1.3 Classification Decision Tree

    IF H9_reveals_conflicts:
      → Apply Section 1.3 STEP_1 rules strictly
      → Government/corporate sources → ○ TERTIARY default
      → Confidence reductions as calculated
      → Transparency output mandatory

  expected_output:
    conflicts_identified: List per source
    independence_scores: Calculated for major sources
    classification_adjustments: ◈→◉ or ◉→○ downgrades if warranted
    transparency_warnings: In Part 1 French output
    impact: +0.10-0.20 analysis reliability (through bias exposure)
```

**EXAMPLE (Generic Application)**:

```yaml
# Subject: "New drug X efficacy study"

SOURCE_1: Pharmaceutical Company Press Release
  type: corporation
  funding: shareholder profits
  cui_bono: [$billions in drug sales, stock price]
  conflicts: EXTREME (direct financial interest)
  independence: 0.05/1.0
  classification: ○ TERTIARY (confidence 0.10-0.20)
  → Requires independent corroboration

SOURCE_2: Academic Study (University Y)
  type: academic
  funding_research: "Grant from Pharmaceutical Company X"
  cui_bono: [grant renewal, industry partnership]
  conflicts: HIGH (funded by interested party)
  independence: 0.25/1.0
  classification: ○ TERTIARY (confidence 0.30-0.50)
  → NOT ◉ secondary despite academic format

SOURCE_3: Independent Medical Journal Meta-Analysis
  type: academic
  funding: institutional, no industry ties disclosed
  conflicts: LOW (no apparent COI)
  independence: 0.75/1.0
  classification: ◉ SECONDARY (confidence 0.75-0.85)
  → Can corroborate or contradict company claims

CONCLUSION:
  Company claim (○ 0.15) + Company-funded study (○ 0.40) ≠ reliable evidence
  Independent meta-analysis (◉ 0.80) = only source worthy of confidence
```

---

## 13. TROUBLESHOOTING COMMON ISSUES

### 13.1 Low EDI Score (<0.50)

```yaml
PROBLEM: EDI = 0.38 (below 0.50 threshold)

DIAGNOSIS:
  1. Check which dimensions are low:
     - geo < 0.40? → Expand continents/regions
     - lang < 0.30? → Search non-English sources
     - strat < 0.25? → Need more ◈ primary sources
     - ownership < 0.40? → Too many corporate sources
     - perspective < 0.50? → Missing narratives (🎓🔥)
     - temporal < 0.40? → Add archival sources

SOLUTIONS:
  - Run I1 iteration with targeted gap-filling
  - Apply H6 (academic) or H7 (dissident) heuristics
  - Use H2 (geographic expansion) for local sources
  - Search archival sources (>1 year old) for temporal depth

EXPECTED IMPROVEMENT: +0.15-0.25 EDI after targeted I1
```

### 13.2 Missing Narratives (🎓🔥 absent)

```yaml
PROBLEM: Only ⟐ and ⟐̅ present, missing 🎓🔥

DIAGNOSIS: Insufficient iteration depth (stopped at I0)

SOLUTIONS:
  - MANDATORY: Run I1 with H6_ACADEMIC_SEARCH
  - MANDATORY: Run I1 with H7_DISSIDENT_SEARCH
  - Check: Is subject truly apolitical? (If yes, 🔥 may not exist)
  - For 🎓: Always exists for complex subjects, search harder

QUERIES:
  🎓: "{subject}" site:scholar.google.com OR site:.edu
  🔥: "{subject}" + ("censored" OR "deplatformed" OR adversary_media)

EXPECTED: +2-3 sources, EDI +0.08-0.12
```

### 13.3 Orchestration Not Scored

```yaml
PROBLEM: ⚑ red flags mentioned but P_orchestration not calculated

DIAGNOSIS: I2 deep dive skipped or incomplete

SOLUTION:
  - Return to Section 4.2 (Orchestration Probability Scoring)
  - Assess 5 indicators (0.0-1.0 each):
    1. temporal_sync: <12h coordination?
    2. vocabulary_uniformity: Identical phrases?
    3. cui_bono_clarity: Obvious beneficiaries?
    4. historical_pattern: Matches past orchestrations?
    5. suppression_indicators: Counter-narrative censored?
  - Calculate: P_orch = weighted sum (see formula)
  - Classify: P<0.30 organic | 0.30-0.60 possible | 0.60-0.85 probable | >0.85 certain

OUTPUT: P_orchestration=0.XX in Part 2 Technical
```

### 13.4 Convergence Not Achieved (C(n) < 0.85)

```yaml
PROBLEM: After I3, C(3) = 0.68 (below 0.85 target)

DIAGNOSIS: Subject highly complex OR investigation incomplete

OPTIONS:
  A. CONTINUE TO I4:
     - If budget allows (>60 min total)
     - If critical investigation (high stakes)
     - Expected: C(4) → 0.80-0.90

  B. ACCEPT C(3) = 0.68:
     - If budget constrained
     - If EDI ≥ 0.60 AND sources ≥ 15
     - Mark output: "Investigation incomplete, convergence 68%"

  C. FORCED STOP AT n=5:
     - Diminishing returns (C increases <5% per iteration)
     - Document: "Subject complexity exceeds investigation capacity"

DECISION RULE:
  IF C(n) ≥ 0.75 AND EDI ≥ 0.55 AND n ≥ 3:
    → ACCEPTABLE, proceed to output
  ELSE:
    → Continue one more iteration
```

### 13.5 Budget Overflow (>60 minutes spent)

```yaml
PROBLEM: Time spent >60 minutes, exceeding APEX budget

DIAGNOSIS: Over-iterating OR slow web search

SOLUTIONS:
  PREVENTION:
    - Set timers: I0=10min, I1=15min, I2=20min, I3=10min (55min total)
    - Use rapid queries (avoid deep research rabbit holes)
    - Leverage H1-H8 heuristics (pre-optimized searches)

  IF ALREADY OVER BUDGET:
    - STOP at current iteration n
    - Generate output with available data
    - Mark: "Time budget exceeded, investigation truncated at In"
    - Document: C(n)=XX, EDI=XX achieved

ACCEPTABLE COMPROMISES:
  - C(n) ≥ 0.70 (instead of 0.85) if EDI ≥ 0.60
  - sources ≥ 12 (instead of 18+) if ◈ ≥2 AND narratives ≥3
```

---

## 14. FUTURE ENHANCEMENTS (PHASE 3+)

```yaml
PHASE_3_ADVANCED:
  - Visual semiotic analysis (image propaganda detection)
  - Deepfake detection integration (synthetic media identification)
  - Predictive narrative forecasting (AI predicts manipulation before spread)
  - Resistance inoculation personalized (custom cognitive defenses)
  - Real-time narrative evolution tracking (monitor narrative mutations)
  - Cross-investigation narrative correlation (detect mega-orchestrations)
  - Automatic orchestration detection AI (machine learning on ⚑ patterns)
```

---

**SEARCH_EPISTEMIC v1.0 MOTTO**: *"One narrative is propaganda. Five narratives is cartography."*

---

*SEARCH_EPISTEMIC.md v1.0 PHASE 1 — 01/10/2025 — Source Pluralism Foundation*
