# SEARCH EPISTEMIC v2.0 — Source Pluralism & Narrative Cartography

## §1 SOURCE STRATIFICATION (◈◉○)

### 1.1 Three-Tier Classification

| Tier | Symbol | Types | Confidence |
|------|--------|-------|------------|
| **PRIMARY** | ◈ | Raw documents, leaks, court files, FOIA, data | 0.90–0.95 |
| **SECONDARY** | ◉ | Investigative journalism, academic research, expert testimony | 0.75–0.85 |
| **TERTIARY** | ○ | Mainstream media, aggregators, opinion, official statements | 0.40–0.70 |

**Priority**: ◈ > ◉ > ○ (all three needed for complete cartography)

### 1.2 Source Reliability Weights

```yaml
dissident_whistleblower: 0.95   # Leaked docs, FOIA, whistleblowers
independent_investigative: 0.90 # Consortium, Mediapart, Intercept
field_testimony: 0.85           # Direct witnesses, workers
alternative_media: 0.80         # Non-corporate media
archival_contradictions: 0.80   # Historical evidence
international_opposing: 0.75    # Non-aligned foreign viewpoints
official_institutions: 0.20     # Government, UN — SKEPTICISM DEFAULT
```

**Critical**: Official sources (⟐) weighted LOW (0.20) unless corroborated by ◈ primary evidence.

### 1.3 Classification Decision Tree

```
Source type?
  ├─ Govt/IGO/Military → ○ TERTIARY (conf 0.20–0.40)
  │   Contains leaked docs?
  │   ├─ YES → Docs only: ◈ PRIMARY | Analysis: ○ TERTIARY
  │   └─ NO → ○ TERTIARY
  ├─ Corporate/Corp_Media → Check funding
  │   ├─ Disclosed + No COI → ◉ SECONDARY (0.60–0.75)
  │   └─ Opaque OR COI → ○ TERTIARY (0.40–0.60)
  └─ Independent/Academic → Check independence
      ├─ Independent verified → ◉ SECONDARY (0.75–0.85)
      └─ Unclear → ○ TERTIARY (0.50–0.70)

Corroboration → increases CONFIDENCE within tier (doesn't change tier)
Circular corroboration (same institutional family) = NOT valid
```

### 1.4 Classification Algorithm

```yaml
STEP_1_PROVENANCE:
  IF source ∈ [government, state_agency, military, intelligence, UN, NATO, EU_institution, IGO]:
    → ○ TERTIARY (conf 0.20–0.40) — Party to conflicts, not neutral
  ELIF source ∈ [corporation, corporate_media, funded_think_tank]:
    IF funding_disclosed AND no_COI → ◉ SECONDARY (0.60–0.75)
    ELSE → ○ TERTIARY (0.40–0.60)
  ELIF source ∈ [independent_journalism, academic_research, independent_NGO]:
    IF independent → ◉ SECONDARY (0.75–0.85)
    ELSE → ○ TERTIARY (0.50–0.70)

STEP_2_EVIDENCE_TYPE:
  IF contains [leaked_document, FOIA, court_file, raw_dataset, whistleblower_docs]:
    → THOSE ELEMENTS ONLY: ◈ PRIMARY (0.90–0.95)
    → Source interpretation remains at STEP_1 tier
  IF provides [testimony, investigation, analysis, claims]:
    → NO UPGRADE, remains STEP_1 classification

STEP_3_CORROBORATION:
  IF claim corroborated by ≥2 sources from different provenance:
    → CONFIDENCE boost +0.10 to +0.20 within tier
    → Tier: UNCHANGED
  Circular corroboration (same institutional family) = NOT independent
```

**Critical Principles**:
1. "Official ≠ Reliable" — Institutional status is DISQUALIFYING by default
2. "Evidence transcends institution" — Raw documents elevate regardless of source
3. "Interpretation inherits bias" — Analysis by biased source remains biased
4. "Corroboration must be independent" — Same institutional family = single source
5. "Follow the money" — Funding sources determine independence

---

## §2 DIVERSITY ANALYSIS

### 2.1 Geographic Priority Heuristics

```yaml
PRIORITY_ORDER:
  1. LOCAL: Country/region directly affected (highest weight)
  2. NEIGHBOR: Bordering countries, regional bloc
  3. REGIONAL: Same continent, cultural sphere
  4. DISTANT: Other continents (diverse perspectives)
  5. HEGEMON: Dominant power (USA, UK) — LOWEST weight for geopolitical subjects

VALIDATION:
  - ≥2 continents represented
  - ≥1 local source (if applicable)
  - Avoid monoculture (not all sources from same zone)
```

### 2.2 Linguistic Diversity Requirements

```yaml
TARGETS:
  - ≥30% sources in non-English languages
  - ≥2 linguistic families represented
  - Primary language of affected region included (if applicable)

PRIORITY:
  1. PRIMARY: Language(s) of country/region concerned
  2. NEIGHBOR: Languages of bordering countries
  3. REGIONAL: Regional lingua franca (Arabic MSA, Spanish LATAM, etc.)
  4. GLOBAL_RELAY: English (necessary but insufficient alone)

TRANSLATION_QUALITY:
  - Direct primary→target: HIGH
  - Double primary→English→target: MEDIUM
  - Always note translation path (affects confidence)
```

### 2.3 Perspective Diversity

Five narrative types required for complete cartography:

| Symbol | Type | Source | Function |
|--------|------|--------|----------|
| ⟐ | Official | Government, MSM consensus | Manufacture consent |
| ⟐̅ | Counter-hegemonic | Mixed ◈◉○, often ◈ leaks critical | Reveal hidden interests |
| 🌍 | Regional | Local media, regional languages | Escape Western-centric bias |
| 🎓 | Academic | ◉ peer-reviewed research | Depth beyond journalism |
| 🔥 | Dissident | Censored, deplatformed experts | Reveal what power hides |

### 2.4 Ownership Diversity

```yaml
TYPES: [state, corporate, independent, academic, activist, personal] (max 6)
TARGET: non-corporate ≥ 50%
FORMULA: ownership_diversity = (types/6 × 0.6) + (non_corporate_pct × 0.4)
```

### 2.5 Temporal Diversity

```yaml
TEMPORALITIES: [real_time, recent(<1w), medium(<1m), archival(>1y), historical] (max 5)
TARGET: ≥3 temporalities represented
FORMULA: temporal_diversity = (temporalities/5 × 0.6) + (archival_present × 0.4)
```

---

## §3 CORROBORATION (⊕⊗⊙)

### 3.1 Fact Quality Assessment

| Symbol | Quality | Criteria |
|--------|---------|----------|
| ✦ | Hard fact | Documented in ◈ primary, corroborated by ≥2 independent ◉, no contradictions |
| ✧ | Soft fact | Based on ◉ testimony/investigation, contextually coherent, some corroboration |
| ⁕ | Claim | Assertion without ◈◉ documentation, single source or ○ tertiary only |
| ⁂ | Speculation | Hypothesis explicitly uncertain, logical inference, no direct evidence |

### 3.2 Corroboration Protocol

| Symbol | Status | Criteria |
|--------|--------|----------|
| ⊕ | Confirmed | ≥2 sources ◈ concordant OR ≥3 sources ◉ concordant, no significant contradictions |
| ⊗ | Contradicted | ≥2 sources ◈ contradict OR pattern contradictions (timeline impossible, physics violation) |
| ⊙ | Partial | Some elements confirmed, others contested, mixed evidence quality |

### 3.3 Divergence Zones (≋)

Points where narratives fundamentally contradict:

| Level | Symbol | Definition |
|-------|--------|------------|
| Minor | ≋+ | Different emphasis, same basic facts |
| Major | ≋++ | Contradictory core claims |
| Suppressed | ≋+++ | One side has ◈ evidence, other only ○ assertions |

---

## §4 EDI CALCULATION — Epistemic Diversity Index

### 4.1 Six-Dimension Formula

```
EDI = (geo_diversity × 0.25) + (lang_diversity × 0.20) + (strat_diversity × 0.20)
    + (ownership_diversity × 0.15) + (perspective_diversity × 0.15) + (temporal_diversity × 0.05)
```

**Dimension formulas**:

```
geo_diversity   = (continents/6 × 0.4) + (zones/10 × 0.3) + (local_presence × 0.3)
lang_diversity  = (languages/10 × 0.3) + (non_english_pct × 0.4) + (families/5 × 0.3)
strat_diversity = (primary_pct × 0.5) + (secondary_pct × 0.3) + (tertiary_pct × 0.2)
ownership_div   = (types/6 × 0.6) + (non_corporate_pct × 0.4)
perspective_div = (perspectives/7 × 0.5) + (official_vs_counter_balance × 0.3) + (dissident_present × 0.2)
temporal_div    = (temporalities/5 × 0.6) + (archival_presence × 0.4)
```

**Classification**:

| EDI | Classification |
|-----|---------------|
| ≥ 0.65 | EXCELLENT |
| ≥ 0.50 | GOOD |
| ≥ 0.35 | ACCEPTABLE |
| < 0.35 | EPISTEMIC_MONOCULTURE |

### 4.2 Composite Extensions

```
CoverageScore       = met_quotas / total_quotas
IndependenceScore   = f(diversity_families, low_syndication)
ContradictionCoverage = adversary_present × divergence_processed
EDI* = 0.5×EDI + 0.3×Coverage + 0.2×Independence
```

### 4.3 BIAS Penalties (Post-Calculation)

Applied AFTER raw EDI. `EDI_final = max(0.0, EDI_raw + penalties)`

| Penalty | Trigger | Weight |
|---------|---------|--------|
| P1: Institutional Monoculture | govt >60% OR corp >60% | -0.20 |
| P1b: Power Monoculture | govt+corp >75% | -0.25 |
| P2: Missing Adversary | sensitive subject + no dissident/adversary | -0.15 |
| P3: Narrative Echo Chamber | only ⟐, no ⟐̅/🔥 | -0.20 |
| P4: Tertiary Over-Reliance | tertiary >70% | -0.15 |
| P5: Circular Corroboration | claims confirmed by same institutional family | -0.10 |

**Transparency output** (mandatory if penalties applied):
```
EDI:{final} (raw:{raw} penalties:{sum}[flags])
```

### 4.4 EDI Targets by Topic

| Topic | Minimum EDI | Notes |
|-------|------------|-------|
| Simple factual | 0.30 | Basic corroboration sufficient |
| Sensitive political | 0.50 | H7 adversary mandatory |
| Geopolitical conflict | 0.65 | All 5 narratives + ◈ primary |
| APEX investigation | 0.75 | Full 4-iteration + orchestration |

---

## §5 CONVERGENCE — 4-Iteration Protocol

### 5.1 Convergence Formula

```
C(n) = 1 - (new_information_at_iteration_n / total_information_discovered)
```

**Target**: C(n) ≥ 0.85 (85% convergence = investigation maturity)

**Stopping conditions**:
- C(n) ≥ 0.90 → COMPLETE
- C(n) ≥ 0.85 AND EDI ≥ 0.60 → SUFFICIENT
- n ≥ 3 AND C(n) ≥ 0.75 → ACCEPTABLE (budget constraint)
- n > 5 → FORCED_STOP (diminishing returns)

### 5.2 Iteration Phases

| Phase | Purpose | Sources | EDI | Convergence | Time |
|-------|---------|---------|-----|-------------|------|
| **I0** Reconnaissance | Initial cartography, identify narratives/gaps | 8–15 | ~0.40 | — | 5–10 min |
| **I1** Exploration | Fill gaps, enhance diversity, seek ◈🎓🔥 | +5–10 | ~0.55 | C(1)~0.50 | 10–15 min |
| **I2** Deep Dive | Triangulate claims, detect orchestration, exact EDI | +5 | exact | C(2)~0.75 | 15–20 min |
| **I3** Synthesis | Final validation, produce 3-part output | final | ≥0.60 | C(3)≥0.85 | 5–10 min |

**Full budget**: 35–55 minutes, 18–25 sources, EDI 0.60–0.75, C(3)≥0.85

### 5.3 Orchestration Detection (⚑)

Probability scoring:
```
P_orchestration = temporal_sync × 0.30 + vocabulary_uniformity × 0.25
                + cui_bono_clarity × 0.20 + historical_pattern × 0.15
                + suppression_indicators × 0.10
```

| P | Classification |
|---|---------------|
| < 0.30 | Likely organic |
| 0.30–0.60 | Possible coordination |
| 0.60–0.85 | Probable orchestration |
| > 0.85 | Quasi-certain (⚑⚑⚑) |

Red flag indicators:
- ⚑ TEMPORAL_SYNC: Narrative appears <12h across ≥10 outlets (P spontaneous <0.01%)
- ⚑ VOCABULARY_IDENTICAL: Same phrases across "independent" sources
- ⚑ CUI_BONO_EVIDENT: Clear financial/political beneficiaries
- ⚑ SUPPRESSION_ACTIVE: Counter-narratives censored/deplatformed
- ⚑ HISTORICAL_PATTERN: Reproduces documented past orchestrations

### 5.4 Heuristics (H6–H9)

| ID | Heuristic | Trigger | Effect |
|----|-----------|---------|--------|
| H6 | Academic Search | 🎓 absent or <2 | +2–4 ◉ sources, EDI +0.08 |
| H7 | Dissident/Adversary | 🔥 absent OR sensitive subject | +2–5 sources, EDI +0.15, adversary mandatory |
| H8 | Auto-Triangulation | ≋ divergence detected | ⊕⊗⊙ corroboration, ✦✧⁕⁂ classification |
| H9 | Cui Bono Source | ALWAYS (universal) | Funding research, COI detect, independence score |

---

## §6 ADVERSARY MEDIA MAP (H7)

### 6.1 H7 Sensitivity Triggers

Subject keywords triggering mandatory H7: `election, government, war, conflict, military, sanctions, propaganda, disinformation, corruption, fraud, pharmaceutical, whistleblower, protest, surveillance, inequality`

IF ANY keyword detected → H7_MANDATORY = True

### 6.2 Complexity Override

IF H7_sensitive = True AND complexity < 4.0 → Force complexity = 4.0 (MEDIUM minimum). Sensitive subjects require elevated verification regardless of content length.

### 6.3 Media Map v3.0 (45+ sources)

**State Media**: RU: rt.com(C), sputniknews.com(C), tass.com(B) | CN: globaltimes.cn(C), xinhuanet.com(B), chinadaily.com.cn(B) | IR: presstv.ir(C), tasnimnews.com(C) | KP: kcna.kp(D)

**Independent Alternative**: US: theintercept.com(A), propublica.org(A), thegrayzone.com(C), consortiumnews.com(B) | FR: mediapart.fr(A), disclose.ngo(A), bastamag.net(B) | UK: declassifieduk.org(B), middleeasteye.net(B), bellingcat.com(A) | DE: nachdenkseiten.de(B)

**Think Tanks**: quincyinst.org(B), cato.org(B), cepr.net(B)

**Whistleblower Primary Docs**: wikileaks.org(A), icij.org(A)

**Global South**: BR: terra.com.br(B), uol.com.br(B), CartaCapital.com.br(B) | MX: proceso.com.mx(B), animalpolitico.com(B) | AR: pagina12.com.ar(C), lanacion.com.ar(B) | IN: thewire.in(B), scroll.in(B), thehindu.com(B) | PK: dawn.com(B) | ZA: mailandguardian.co.za(B), dailymaverick.co.za(B) | NG: punchng.com(B) | KE: nation.africa(B) | QA: aljazeera.com(A)

### 6.4 Adversary Query Template

```yaml
IF entity ∈ adversary_entities:
  FOR source IN H7_MAP[entity]:
    query = 'site:{source.url} "{subject}" {keywords}'
    keywords = ["official response", "perspective", "statement", "analysis"]
  MANDATORY: ≥1 source from adversary perspective
  IF not found → EDI penalty -0.15 + warning in Part 1
```

### 6.5 Validation Targets

```yaml
MANDATORY:
  sources_total ≥ 5, EDI ≥ 0.50, ◈ ≥ 2, narratives ≥ 2
  geo_continents ≥ 2, lang_non_english ≥ 30%

OPTIMAL:
  sources 10–15, EDI ≥ 0.65, ◈ ≥ 3, narratives ≥ 3, divergences ≥ 1, orchestration assessed

AUTO_FAIL:
  EDI < 0.35 → EPISTEMIC_MONOCULTURE
  ◈ = 0 → NO_PRIMARY_EVIDENCE
  Only ⟐ → MANUFACTURED_CONSENSUS
  All same ownership → FAKE_DIVERSITY
  geo < 2 continents on geopolitical → WESTERN_BIAS
```

### 6.6 Output Format

```
[SOURCES] ◈:{X} ◉:{Y} ○:{Z} | EDI:{score} (raw:{r} penalties:{p}[flags])
| geo:{continents} lang:{%non-EN} | ⟐:{A}⟐̅:{B}🌍:{C}🎓:{D}🔥:{E}
| ≋:{divergence_count} ⚑:{red_flag_count} | COV:{c} IND:{i} CC:{cc} → EDI*:{e}
```

---

*SEARCH_EPISTEMIC v2.0 — "One narrative is propaganda. Five narratives is cartography."*
