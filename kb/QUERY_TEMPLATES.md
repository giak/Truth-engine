# QUERY TEMPLATES — Domain-Adaptive Search Execution

**Purpose**: Explicit WHERE/HOW templates for collecting ◈ primary sources, 🌍 geographic diversity, and 🔥 adversary perspectives.

**Usage**: Referenced by Truth Engine preprocessing (instructions_claude.md) via @KB[QUERY_TEMPLATES]

**Version**: 1.0 (2025-11-06)

---

## 1. PRIMARY EVIDENCE TEMPLATES (◈)

### 1.1 Domain Detection

Auto-detect domain from subject keywords:

```yaml
DOMAINS:
  Political: [election, government, policy, parliament, minister, legislation, party, vote]
  Scientific: [study, research, trial, data, peer-reviewed, clinical, hypothesis, experiment]
  Corporate: [company, CEO, financial, earnings, SEC, lawsuit, merger, acquisition]
  Geopolitical: [war, diplomacy, sanctions, military, treaty, UN, conflict, alliance]
  Legal: [court, law, statute, ruling, case, regulation, judge, verdict]
  Economic: [GDP, inflation, trade, central bank, IMF, World Bank, fiscal, monetary]
  Social: [inequality, protest, survey, census, demographics, civil rights, movement]
  Tech: [software, algorithm, patent, RFC, specification, source code, API]
  Historical: [archives, records, documents, era, period, century, historian]
  Media: [broadcast, press release, transcript, publication, journalism, news]
```

### 1.2 Templates by Domain

**POLITICAL** (◈_POL):
```
1. "{subject} site:assemblee-nationale.fr OR site:senat.fr OR site:legifrance.gouv.fr filetype:pdf"
2. "{subject} archives officielles OR documents parlementaires OR rapports gouvernementaux"
3. "{entity} leaked OR FOIA OR négociations OR débats Bureau National"
```

**SCIENTIFIC** (◈_SCI):
```
1. "{subject} site:pubmed.ncbi.nlm.nih.gov OR site:arxiv.org OR doi:"
2. "{subject} peer-reviewed study OR clinical trial data OR dataset filetype:pdf"
3. "{subject} original research (NOT review NOT commentary) primary data"
```

**CORPORATE** (◈_CORP):
```
1. "{entity} site:sec.gov filetype:pdf (10-K OR 10-Q OR 8-K OR proxy statement)"
2. "{entity} court documents OR lawsuit filing OR settlement agreement"
3. "{entity} annual report official OR financial filing OR audit report"
```

**GEOPOLITICAL** (◈_GEO):
```
1. "{subject} site:wikileaks.org OR diplomatic cable OR state department"
2. "{subject} UN documents OR treaty text OR Security Council resolution"
3. "{subject} declassified OR FOIA OR government archives official"
```

**LEGAL** (◈_LEG):
```
1. "{subject} site:courtlistener.com OR site:caselaw OR court ruling"
2. "{subject} statute text OR regulation official OR legal code"
3. "{case} oral arguments transcript OR court filing OR judgment"
```

**ECONOMIC** (◈_ECO):
```
1. "{subject} site:imf.org OR site:worldbank.org OR central bank data"
2. "{subject} GDP statistics OR trade data OR economic indicators official"
3. "{country} budget filetype:pdf OR fiscal report OR treasury data"
```

**SOCIAL** (◈_SOC):
```
1. "{subject} census data OR survey results OR demographic statistics"
2. "{subject} government report OR official study OR field research"
3. "{subject} testimonies OR direct accounts OR primary sources"
```

**TECH** (◈_TECH):
```
1. "{subject} source code OR github OR technical specification"
2. "{subject} RFC OR standard OR protocol documentation"
3. "{subject} whitepaper OR technical report OR patent filing"
```

**HISTORICAL** (◈_HIST):
```
1. "{subject} archives OR historical documents OR primary records"
2. "{subject} original documents OR manuscripts OR correspondence"
3. "{period} official records OR government archives OR contemporary sources"
```

**MEDIA** (◈_MED):
```
1. "{subject} original broadcast OR press conference transcript"
2. "{subject} press release official OR statement original"
3. "{entity} official communication OR public statement OR announcement"
```

### 1.3 Execution Rules

```yaml
FOR EACH query allocated to PRIMARY_◈:
  
  1. SELECT template based on domain_detected
     IF multiple domains → prioritize by evidence_requirement score
  
  2. EXECUTE query with template
     Variables:
       {subject} = main keywords from query
       {entity} = organization/person identified
       {period} = temporal span if detected
  
  3. VALIDATE results (apply SEARCH_EPISTEMIC §1.3):
     Is it RAW document/data/leak? → ◈ PRIMARY (conf 0.90-0.95)
     Is it institutional analysis? → ○ TERTIARY (conf 0.20-0.40)
     Is it independent investigation? → ◉ SECONDARY (conf 0.75-0.85)
  
  4. IF ◈_collected < target AND budget_remaining > 0:
     RETRY with alternate:
       - Different ccTLD (.fr → .gov → .org)
       - Different filetype (pdf → doc → html)
       - Broader keywords ("leaked" → "documents" → "archives")
```

---

## 2. GEOGRAPHIC DIVERSITY TEMPLATES (🌍)

### 2.1 Native Region Detection

```yaml
Extract query_language:
  FR → native = France/Francophonie
  EN → native = USA/UK/Anglosphere
  DE → native = Germany/DACH
  ES → native = Spain/Latam
  ZH → native = China/Taiwan
  AR → native = Middle East/North Africa
  RU → native = Russia/ex-USSR
  JA → native = Japan
  KO → native = Korea
  IT → native = Italy
  PT → native = Portugal/Brazil
  NL → native = Netherlands/Belgium
  PL → native = Poland
  TR → native = Turkey
  [...extend 20+ languages]
```

### 2.2 Comparables Detection (Domain-Adaptive)

**POLITICAL**:

```yaml
IF subject contains [social democracy, socialist party, left betrayal]:
  comparables = [SPD (Germany), PASOK (Greece), Labour (UK), PSOE (Spain)]
  queries:
    - "SPD Sozialdemokratie Arbeitern verraten site:.de lang:de"
    - "PASOK social democracy betrayal working class site:.gr"
    - "Labour Blair Third Way betrayal site:.uk"

IF subject contains [populism, anti-establishment]:
  comparables = [Podemos (Spain), M5S (Italy), Syriza (Greece), Sanders (USA)]

IF subject contains [far-right, nationalism]:
  comparables = [AfD (Germany), Vox (Spain), FPÖ (Austria), PiS (Poland)]

IF subject contains [corruption, scandal]:
  comparables = [Lava Jato (Brazil), 1MDB (Malaysia), Panama Papers (global)]
```

**SCIENTIFIC**:

```yaml
IF subject contains [climate, emissions]:
  regions = [China, India, USA, EU, Brazil]
  queries:
    - "carbon emissions China policy site:.cn"
    - "climate India policy mitigation site:.in"

IF subject contains [pharmaceutical, vaccine, drug]:
  jurisdictions = [FDA (USA), EMA (EU), MHRA (UK), PMDA (Japan)]

IF subject contains [AI, technology regulation]:
  regions = [USA (Silicon Valley), China, EU (GDPR), UK]
```

**CORPORATE**:

```yaml
IF subject contains [auto industry]:
  regions = [USA (Detroit), Germany (VW/BMW), Japan (Toyota), China (BYD)]

IF subject contains [tech giants, GAFAM]:
  comparables = [USA (GAFAM), China (Alibaba/Tencent), EU (SAP/Spotify)]

IF subject contains [energy, oil]:
  regions = [USA (Texas), Middle East (OPEC), Russia, Norway]
```

**GEOPOLITICAL**:

```yaml
IF subject contains [war, conflict]:
  perspectives = [involved parties + neighbors + non-aligned]

IF subject contains [sanctions, trade war]:
  perspectives = [sanctioner + sanctioned + third parties affected]
```

### 2.3 Query Templates

```yaml
TEMPLATE_GEO:
  - "{comparable} + {subject_keywords} + site:{ccTLD} + lang:{code}"
  - "{comparable} + {subject_keywords} + regional perspective"
  - "{region} + {subject_keywords} + international coverage"

EXAMPLES:
  PS trahisons → "SPD Sozialdemokratie Arbeitern verraten site:.de lang:de"
  Climate tax → "carbon tax China policy site:.cn emission reduction"
  Pharma scandal → "pharmaceutical trials Africa unethical site:.ke OR site:.ng"
```

### 2.4 Validation Targets

```yaml
CALCULATE geo_diversity:
  continents_covered / 6 × 0.4 + non_native_region_pct × 0.6

TARGETS by complexity:
  SIMPLE (0-3): ≥0.30
  MEDIUM (4-6): ≥0.35
  COMPLEX (7-8): ≥0.40
  APEX (9-10): ≥0.50
```

---

## 3. ADVERSARY PERSPECTIVE TEMPLATES (H7 🔥)

### 3.1 H7 Sensitivity Triggers

```yaml
SENSITIVITY_KEYWORDS:
  Politics: [election, government, policy, parliament, legislation, minister, president, party, vote, coalition, opposition]
  Geopolitical: [war, conflict, military, defense, sanctions, intervention, diplomacy, treaty, alliance, invasion]
  Info-ops: [propaganda, disinformation, misinformation, censorship, manipulation, psyops, influence operation]
  Economic: [corruption, fraud, lobbying, revolving door, monopoly, cartel, insider trading, subsidy, bailout]
  Corporate: [scandal, cover-up, whistleblower, lawsuit, settlement, pharmaceutical, clinical trial, adverse effects]
  Social: [protest, repression, surveillance, inequality, exploitation, strike, civil liberties, discrimination]

IF ANY(keyword IN query) → H7_MANDATORY = True
```

### 3.1bis H7_COMPLEXITY_OVERRIDE (Force MEDIUM for Sensitive Short-Form)

**PROBLEM**: Short-form content (tweets 20-50 words) scores SIMPLE (complexity 0-3) via dimension averaging, BUT if H7_SENSITIVE trigger detected → CONTRADICTION. Sensitive subjects require elevated verification standards regardless of content length.

**SOLUTION**:

```yaml
IF H7_SENSITIVE_detected = True (keywords above):
  AND complexity_score < 4.0:
    
    → complexity_score_adjusted = 4.0 (FORCE MEDIUM minimum)
    
    → RATIONALE:
      "Sensitive subjects (political, geopolitical, info-ops, corruption, etc.)
       require elevated verification standards regardless of content length.
       Short tweet on controversial topic ≠ simple factual statement."
    
    → APPLY MEDIUM allocations (vs SIMPLE):
      * PRIMARY_◈ ≥ 2 queries (vs 1 for SIMPLE)
      * ADVERSARY_H7 mandatory (vs optional)
      * CONTEXT_⟐ ≥ 2 queries (vs 1)
      * DIVERSITY ≥ 2 queries (including 1 GEO mandatory)
      * Budget target: 10 queries (vs 5 SIMPLE)
    
    → APPLY MEDIUM targets:
      * EDI target ≥0.50 (vs 0.30 SIMPLE)
      * ◈ minimum ≥2 (vs 1 SIMPLE)
      * geo_diversity ≥0.35 (vs 0.30 SIMPLE)
      * ISN target ≥7.0 (vs lower)
    
    → OUTPUT Part 2:
      [DIAGNOSTICS] COMPLEXITY_OVERRIDE: H7_detected → {calculated}(SIMPLE) elevated to 4.0(MEDIUM)

EXAMPLE:
  Input: Tweet Carole Delga 23 words "PS pas postures travaille classes populaires"
  Complexity calculated: 2.03 (SIMPLE)
  H7 trigger: YES ("Parti socialiste" = political keyword)
  
  OVERRIDE:
    complexity_score: 2.03 → 4.0 (MEDIUM)
    Budget: 5 → 10 queries
    Allocations:
      PRIMARY_◈: 1 → 2 queries
      ADVERSARY_H7: 0 → 2 queries (mandatory)
      CONTEXT_⟐: 1 → 2 queries
      DIVERSITY: 2 → 3 queries (including GEO)
      OPPORTUNISTIC: 1 query
      Total: 10/10
    Targets:
      EDI: 0.30 → 0.50
      ◈: 1 → 2 minimum
      geo: 0.30 → 0.35
  
  RESULT:
    Prevents underestimation of politically sensitive short-form content
```

### 3.2 H7 Adversary Media Map v2.0

**Extension 7→25 sources (core coverage 90% use cases).**

```yaml
H7_ADVERSARY_MEDIA_MAP_v2:
  
  STATE_MEDIA (9 sources):
    Russia:
      - rt.com (English, propaganda tier C)
      - sputniknews.com (multilang, tier C)
      - tass.com (official news, tier B)
    China:
      - globaltimes.cn (nationalist, tier C)
      - xinhuanet.com (official agency, tier B)
      - chinadaily.com.cn (English, tier B)
    Iran:
      - presstv.ir (state broadcaster, tier C)
      - tasnimnews.com (semi-official, tier C)
    DPRK:
      - kcna.kp (official agency, tier D)
  
  INDEPENDENT_ALT (11 sources):
    USA:
      - theintercept.com (Snowden docs, tier A)
      - propublica.org (investigative nonprofit, tier A)
      - thegrayzone.com (anti-imperialist, tier C)
      - consortiumnews.com (anti-war, tier B)
    France:
      - mediapart.fr (investigative, tier A)
      - disclose.ngo (Forbidden Stories, tier A)
      - bastamag.net (social/alternative, tier B)
    UK:
      - declassifieduk.org (foreign policy, tier B)
      - middleeasteye.net (Middle East, tier B)
      - bellingcat.com (OSINT, tier A)
    Germany:
      - nachdenkseiten.de (critical, tier B)
  
  THINK_TANKS (3 sources):
    Anti-interventionist:
      - quincyinst.org (restraint foreign policy, tier B)
      - cato.org (libertarian non-interventionist, tier B)
    Heterodox_econ:
      - cepr.net (progressive economics, tier B)
  
  WHISTLEBLOWER (2 sources):
    Primary_docs:
      - wikileaks.org (leaked docs, tier A)
      - icij.org (Panama/Pandora Papers, tier A)

# Auto-detection patterns
H7_ENTITY_TRIGGERS:
  keywords: [disinformation, propaganda, threat, hostile, aggression, sanctions, interference, manipulation, psyops]
  entities:
    Geopolitical: [Russia, China, Iran, DPRK, Venezuela, Cuba]
    Corporate: [Big Pharma, Big Tech, GAFAM, pharma, tech giants]
    Institutional: [NATO, EU, Pentagon, CIA, FBI]
  
  → IF detected → mandatory H7 queries
  → Map entity to sources (Russia → rt.com/tass.com/sputniknews.com)
  → Execute: site:{url} "{subject}" [official response|perspective|statement]

# Extensibility
ADD_NEW_SOURCE:
  1. Identify entity mentioned as threat/adversary
  2. Search entity's official media or opposition within
  3. Assess tier (A/B/C/D based on credibility/bias)
  4. Add to map with country/topic/stance metadata
  5. System auto-evolves organically
```

### 3.3 Adversary Query Templates

```yaml
TEMPLATE_H7_DISSIDENT:
  1. "{subject} criticism OR opposition OR counter-narrative"
  2. "{subject} alternative media OR dissident OR censored perspective"
  3. "{subject} radical analysis OR anti-establishment OR deplatformed"

TEMPLATE_H7_COUNTER:
  1. "{entity} scandals OR controversies OR accusations"
  2. "{subject} independent investigation OR watchdog OR exposé"
  3. "{subject} adversary perspective OR opposing view"

TEMPLATE_H7_MAP_BASED (v2.0 NEW):
  # Auto-generate queries from media map
  IF entity IN [Russia, China, Iran, DPRK]:
    FOR source IN H7_ADVERSARY_MEDIA_MAP_v2[entity]:
      query = 'site:{source.url} "{subject}" {keywords}'
      keywords = ["official response", "perspective", "statement", "analysis"]
  
  EXAMPLES:
    "Russia disinformation" → 'site:rt.com "disinformation" Russian perspective'
    "China influence" → 'site:globaltimes.cn "influence operations" official response'
    "Big Pharma scandal" → 'pharmaceutical industry response OR corporate statement'

ADVERSARY_PERSPECTIVE_CHECK:
  IF subject mentions entity as [threat, enemy, adversary, hostile]:
    adversary_entities = extract_accused(subject)
    
    FOR EACH entity:
      MANDATORY: Find ≥1 source from entity's perspective
      REASON: "Audi alteram partem (hear the other side)"
    
    LOOKUP: H7_ADVERSARY_MEDIA_MAP_v2[entity]
    EXECUTE: Template queries above
    
    EXAMPLES:
      "Russia disinformation" → MUST include rt.com/tass.com sources
      "China influence" → MUST include globaltimes.cn/xinhua sources
      "Big Pharma scandal" → MUST include pharma industry response
```

### 3.3 Validation

```yaml
COUNT adversary_sources:
  🔥_dissident_count (deplatformed, censored, radical)
  ⟐̅_counter_count (counter-hegemonic, alternative)

TARGET: (🔥 + ⟐̅) ≥ 2 minimum

IF target not met AND H7_triggered:
  → EDI penalty: -0.15
  → WARNING: "⚠️ CARTOGRAPHIE INCOMPLÈTE: Perspective adversaire absente"
```

---

## 4. RETRY STRATEGIES (Budget Remaining)

### 4.1 PRIMARY Evidence Retry

```yaml
IF ◈_collected < target:
  
  ALTERNATE 1 (ccTLD):
    Original: site:assemblee-nationale.fr
    Retry: site:.gov OR site:.fr OR site:.eu
  
  ALTERNATE 2 (filetype):
    Original: filetype:pdf
    Retry: filetype:doc OR filetype:html OR dataset
  
  ALTERNATE 3 (keywords):
    Original: "leaked documents"
    Retry: "official documents" OR "archives" OR "primary sources"
```

### 4.2 Geographic Retry

```yaml
IF geo_diversity < target:
  
  ALTERNATE (broader regions):
    Original: site:.de lang:de
    Retry: Europe OR international OR global perspective
  
  ALTERNATE (English sources international):
    Original: regional lang-specific
    Retry: "{subject} international site:.org OR site:.edu"
```

### 4.3 Adversary Retry

```yaml
IF (🔥 + ⟐̅) < 2:
  
  ALTERNATE (broader adversary):
    Original: "{subject} dissident perspective"
    Retry: "{subject} criticism" OR "{subject} opposition" OR "{subject} controversy"
```

---

## 5. Common Errors to Avoid

```yaml
PRIMARY STRATIFICATION:
  ❌ "Government report analysis" = ○ TERTIARY (interpretation)
  ✅ "Government data tables raw" = ◈ PRIMARY (raw evidence)
  
  ❌ "Official statement press coverage" = ○ TERTIARY (mediated)
  ✅ "Official statement original text" = ◈ PRIMARY (raw document)
  
  ❌ "EEAS report conclusions" = ○ TERTIARY (govt institution)
  ✅ "Leaked emails within report" = ◈ PRIMARY (raw evidence)

GEOGRAPHIC:
  ❌ All sources French/anglophone = monoculture
  ✅ 40%+ non-native (DE, GR, ES, CN sources) = diversity
  
  ❌ "5 EU governments confirm" = circular (same family)
  ✅ EU + non-EU (Russia, China, USA) = independent

ADVERSARY:
  ❌ Only official narrative = asymmetric bias
  ✅ Official + counter + dissident = 95% hostility symmetric
  
  ❌ "Russia bad" with zero Russian sources = propaganda
  ✅ "Russia bad" + Russian response + third parties = balance
```

---

## 6. Integration with Truth Engine

### 6.1 Preprocessing Flow

```yaml
STEP 0 — Domain + Complexity Detection:
  → Detect domain (political, scientific, etc.)
  → Calculate complexity (0-10)
  → H7 trigger check (sensitive keywords)

STEP 1 — Query Allocation:
  → PRIMARY_◈ = min(3, ceil(complexity × 0.30))
  → ADVERSARY_H7 = IF H7_trigger: min(3, ceil(complexity × 0.25)) ELSE 0
  → DIVERSITY_GEO = budget_remaining - 1

STEP 2 — Execute with Templates:
  → Load @KB[QUERY_TEMPLATES]
  → Apply domain-specific templates
  → Execute searches

STEP 3 — Validate + Retry:
  → Check ◈_count, geo_diversity, H7_adversary
  → IF gaps + budget_remaining: RETRY with alternates
  → ELSE: WARNING + penalties

STEP 4 — Output:
  → Part 1+2+3 with validation warnings
```

### 6.2 Reference Points

- **Instructions**: @KB[QUERY_TEMPLATES] (this file)
- **Stratification**: @KB[SEARCH_EPISTEMIC §1.3]
- **Validation**: instructions_claude.md POST-SEARCH VALIDATION (lines 496-613)

---

**END QUERY_TEMPLATES.md v1.0**
