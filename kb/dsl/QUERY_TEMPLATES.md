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

### 1.2 Templates by Domain (DSL Compact)

```yaml
TEMPLATES_BY_DOMAIN:
  POL:
    1) {subject} site:assemblee-nationale.fr OR site:senat.fr OR site:legifrance.gouv.fr filetype:pdf
    2) {subject} archives officielles OR documents parlementaires OR rapports gouvernementaux
    3) {entity} leaked OR FOIA OR négociations OR débats Bureau National

  SCI:
    1) {subject} site:pubmed.ncbi.nlm.nih.gov OR site:arxiv.org OR doi:
    2) {subject} peer-reviewed study OR clinical trial data OR dataset filetype:pdf
    3) {subject} original research (NOT review NOT commentary) primary data

  CORP:
    1) {entity} site:sec.gov filetype:pdf (10-K OR 10-Q OR 8-K OR proxy statement)
    2) {entity} court documents OR lawsuit filing OR settlement agreement
    3) {entity} annual report official OR financial filing OR audit report

  GEO:
    1) {subject} site:wikileaks.org OR diplomatic cable OR state department
    2) {subject} UN documents OR treaty text OR Security Council resolution
    3) {subject} declassified OR FOIA OR government archives official

  LEG:
    1) {subject} site:courtlistener.com OR site:caselaw OR court ruling
    2) {subject} statute text OR regulation official OR legal code
    3) {case} oral arguments transcript OR court filing OR judgment

  ECO:
    1) {subject} site:imf.org OR site:worldbank.org OR central bank data
    2) {subject} GDP statistics OR trade data OR economic indicators official
    3) {country} budget filetype:pdf OR fiscal report OR treasury data

  SOC:
    1) {subject} census data OR survey results OR demographic statistics
    2) {subject} government report OR official study OR field research
    3) {subject} testimonies OR direct accounts OR primary sources

  TECH:
    1) {subject} source code OR github OR technical specification
    2) {subject} RFC OR standard OR protocol documentation
    3) {subject} whitepaper OR technical report OR patent filing

  HIST:
    1) {subject} archives OR historical documents OR primary records
    2) {subject} original documents OR manuscripts OR correspondence
    3) {period} official records OR government archives OR contemporary sources

  MED:
    1) {subject} original broadcast OR press conference transcript
    2) {subject} press release official OR statement original
    3) {entity} official communication OR public statement OR announcement
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

### 3.2 H7 Adversary Media Map v2.0 (DSL Compact)

**Extension 7→25 sources (core coverage 90% use cases).**
**v3.0: Global South + Regional Expansion (target: 45+ sources)**

```yaml
H7_MAP_v3:
  STATE_MEDIA: # 9 sources
    RU: rt.com(C) | sputniknews.com(C) | tass.com(B)
    CN: globaltimes.cn(C) | xinhuanet.com(B) | chinadaily.com.cn(B)
    IR: presstv.ir(C) | tasnimnews.com(C)
    KP: kcna.kp(D)

  INDEPENDENT_ALT: # 11 sources
    US: theintercept.com(A) | propublica.org(A) | thegrayzone.com(C) | consortiumnews.com(B)
    FR: mediapart.fr(A) | disclose.ngo(A) | bastamag.net(B)
    UK: declassifieduk.org(B) | middleeasteye.net(B) | bellingcat.com(A)
    DE: nachdenkseiten.de(B)

  THINK_TANKS: # 3 sources
    ANTI_INTERVENTIONIST: quincyinst.org(B) | cato.org(B)
    HETERODOX_ECON: cepr.net(B)

  WHISTLEBLOWER: # 2 sources
    PRIMARY_DOCS: wikileaks.org(A) | icij.org(A)

  GLOBAL_SOUTH_EXT: # NEW v3.0 - 20 sources
    # LATAM (Brazil, Mexico, Argentina, Venezuela)
    BR: terra.com.br(B) | uol.com.br(B) | noticias.uol.com.br(B) | CartaCapital.com.br(B)
    MX: proceso.com.mx(B) | aristeguinoticias.com(B) | animalpolitico.com(B)
    AR: pagina12.com.ar(C) | lanacion.com.ar(B) |eltribuno.info(C)
    VE: talcualdigital.com(C) | runenes.com(C) | vpItv.com(C)
    
    # South Asia (India, Pakistan)
    IN: thewire.in(B) | scroll.in(B) | newsclick.in(B) | thehindu.com(B)
    PK: dawn.com(B) | Samaa TV(B)
    
    # Africa (South Africa, Nigeria, Kenya)
    ZA: mailandguardian.co.za(B) | dailymaverick.co.za(B) | news24.com(B)
    NG: punchng.com(B) | vanguardngr.com(B)
    KE: thestandard.co.ke(B) | nation.africa(B)
    
    # MENA (Al Jazeera, Middle East Eye - already in §4 but referenced here)
    QA: aljazeera.com(A) | alemarahenglish.ae(B)

H7_ENTITY_TRIGGERS:
  keywords: [disinformation, propaganda, threat, hostile, aggression, sanctions, interference, manipulation, psyops]
  entities:
    Geopolitical: [Russia, China, Iran, DPRK, Venezuela, Cuba, Brazil, India, South Africa, Nigeria]
    Corporate: [Big Pharma, Big Tech, GAFAM, pharma, tech giants]
    Institutional: [NATO, EU, Pentagon, CIA, FBI]

  → IF detected → mandatory H7 queries
  → Map entity to sources (Russia → rt.com/tass.com/sputniknews.com)
  → Execute: site:{url} "{subject}" [official response|perspective|statement]

ADD_NEW_SOURCE: # Extensibility v3.0
  1) Identify entity mentioned as threat/adversary
  2) Search entity's official media or opposition within
  3) Assess tier (A/B/C/D based on credibility/bias)
  4) Add to map with country/topic/stance metadata
  5) System auto-evolves organically
  6) For Global South: prioritize regional independent media over state-affiliated
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

TEMPLATE_H7_MAP_BASED (v3.0):
  # Auto-generate queries from media map v3.0
  IF entity IN [Russia, China, Iran, DPRK, Venezuela, Brazil, India, South Africa, Nigeria]:
    FOR source IN H7_ADVERSARY_MEDIA_MAP_v3[entity]:
      query = 'site:{source.url} "{subject}" {keywords}'
      keywords = ["official response", "perspective", "statement", "analysis"]
  
  EXAMPLES:
    "Russia disinformation" → 'site:rt.com "disinformation" Russian perspective'
    "China influence" → 'site:globaltimes.cn "influence operations" official response'
    "Brazil environmental" → 'site:terra.com.br "Amazon" perspectiva brasileira'
    "India farmer protests" → 'site:thewire.in "farmer protest" Indian perspective'
    "South Africa mining" → 'site:mailandguardian.co.za "mining" South African perspective'
    "Nigeria corruption" → 'site:punchng.com "corruption" Nigerian perspective'
    "Big Pharma scandal" → 'pharmaceutical industry response OR corporate statement'

ADVERSARY_PERSPECTIVE_CHECK:
  IF subject mentions entity as [threat, enemy, adversary, hostile]:
    adversary_entities = extract_accused(subject)
    
    FOR EACH entity:
      MANDATORY: Find ≥1 source from entity's perspective
      REASON: "Audi alteram partem (hear the other side)"
    
    LOOKUP: H7_ADVERSARY_MEDIA_MAP_v3[entity]
    EXECUTE: Template queries above
    
    EXAMPLES:
      "Russia disinformation" → MUST include rt.com/tass.com sources
      "China influence" → MUST include globaltimes.cn/xinhua sources
      "Brazil environmental" → MUST include terra.com.br/uol.com.br sources
      "India farmer protests" → MUST include thewire.in/scroll.in sources
      "South Africa mining" → MUST include mailandguardian.co.za sources
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

## 4. DISSIDENT PERSPECTIVES TEMPLATES (🔥 Counter-Power)

**Purpose**: Inspire LLM to contextualize queries for counter-power analyses, not mainstream coverage.

**Philosophy**: These are EXAMPLES, not rigid templates. LLM should adapt creatively based on:
- Domain (labor, pharma, tech, politics, geopolitical)
- Geography (France → EU → global)
- Pattern detected (@PAT[ICEBERG], @PAT[MONEY], @PAT[FRAMING], @PAT[GAS]...)

**Integration**: Referenced by system.md §0.4 HERMENEUTIC-DRIVEN PLANNING for query contextualization.

---

### 4.1 Labor & Social Justice

**ICEBERG (Ξ) + LABOR domain:**

Template inspiration: `"{union} critique {methodology} exclusion {hidden_population} {subject}"`

Variables adapt to context:
- `union`: CGT, CFDT, FO, Solidaires (France) | AFL-CIO, SEIU (USA) | DGB, IG Metall (Germany) | TUC (UK) | CCOO, UGT (Spain) | ETUC (EU)
- `methodology`: EQTP, BIT definition, sampling bias, statistical manipulation, méthodologie INSEE
- `hidden_population`: temps partiel subis, sous-emploi, halo chômage, DEFM B-E, travailleurs précaires, auto-entrepreneurs

Concrete examples:
```
Subject: "Salaire médian France 2024"
→ "CGT CFDT critique EQTP exclusion temps partiel statistiques salaires France"

Subject: "Unemployment rate 3.5% USA"
→ "AFL-CIO SEIU critique BIT methodology hidden underemployment gig workers"

Subject: "Arbeitslosigkeit Deutschland 5.2%"
→ "DGB IG Metall Kritik Arbeitslosenstatistik Teilzeitarbeit Mini-Jobs"
```

**FRAMING (Λ) + ECONOMIC domain:**

Template inspiration: `"{heterodox_economist} déconstruit framing {dichotomy} {subject}"`

Variables:
- `heterodox_economist`: Économistes Atterrés, ATTAC France, Bernard Friot, Frédéric Lordon, Thomas Piketty (France) | Ha-Joon Chang, Steve Keen (International) | Modern Monetary Theory economists
- `dichotomy`: moyen/médian, croissance/décroissance, compétitivité/solidarité, dette/investissement, déficit/stimulus

Concrete examples:
```
Subject: "Croissance économique nécessaire"
→ "Économistes Atterrés ATTAC déconstruit framing croissance décroissance productivisme"

Subject: "Dette publique danger"
→ "Bernard Friot Frédéric Lordon analyse critique dette publique framing austérité"
```

---

### 4.2 Corporate & Financial Accountability

**MONEY (€) + CORPORATE domain:**

Template inspiration: `"{watchdog} enquête {opacity} {entity} {subject}"`

Variables:
- `watchdog`: Transparency International, Anticor, Sherpa, PPLAAF, Mediapart, Disclose, Blast, The Intercept, ProPublica
- `opacity`: contrats secrets, flux cachés, bénéficiaires réels, conflits intérêt, lobbying caché, pantouflage, revolving doors
- `entity`: corporation, parti politique, fondation, think tank, cabinet conseil

Concrete examples:
```
Subject: "Pfizer contrats vaccins secrets"
→ "Transparency International Anticor Mediapart enquête contrats secrets Pfizer clauses cachées négociations"

Subject: "McKinsey gouvernement contrats"
→ "Anticor Blast enquête McKinsey conflits intérêt contrats publics pantouflage"

Subject: "Amazon lobbying Brussels"
→ "Corporate Europe Observatory transparency lobbying Amazon EU competition"
```

**FRAMING (Λ) + PHARMA domain:**

Template inspiration: `"{independent_medical} analyse critique {framing} {subject}"`

Variables:
- `independent_medical`: Prescrire, Formindep, Cochrane Collaboration, Health Nerd, Ben Goldacre
- `framing`: efficacité absolue vs relative, balance bénéfices/risques, transparency gaps, conflicts of interest

Concrete examples:
```
Subject: "Vaccin efficacité 95%"
→ "Prescrire Formindep analyse critique efficacité absolue relative vaccins 95% méthodologie"

Subject: "Nouveau médicament révolutionnaire"
→ "Prescrire Cochrane analyse indépendance essais cliniques conflits intérêt Big Pharma"
```

---

### 4.3 Political & Institutional Critique

**GASLIGHTING (GAS) + POLITICAL domain:**

Template inspiration: `"{academic} documente {contradiction} {subject} archives"`

Variables:
- `academic`: historiens, political scientists, investigative researchers, think tanks indépendants
- `contradiction`: promesses/actes, discours/votes, annonces/budgets, rhetoric/policy, before/after

Concrete examples:
```
Subject: "Macron réforme retraites équilibre financier"
→ "chercheurs COR documentent contradiction promesses Macron actes réforme retraites archives rapports"

Subject: "Cameron Brexit promises NHS funding"
→ "researchers document contradiction Brexit campaign promises NHS funding reality"
```

**CYNICISM (Κ) + INSTITUTIONAL domain:**

Template inspiration: `"{civic_watchdog} suit {facade_vs_reality} {institution}"`

Variables:
- `civic_watchdog`: Regards Citoyens, Anticor, Observatoire éthique publique, Transparency International chapters
- `facade_vs_reality`: votes/abstentions, conflits intérêt, nominations politiques, pantouflage, revolving doors, regulatory capture

Concrete examples:
```
Subject: "ARCOM indépendance régulation médias"
→ "Regards Citoyens Anticor nominations ARCOM conflits intérêt gouvernement indépendance"

Subject: "FDA independence pharmaceutical regulation"
→ "Public Citizen FDA revolving doors Big Pharma conflicts of interest regulatory capture"
```

---

### 4.4 Geopolitical & Warfare

**WAR (⚔) + GEOPOLITICAL domain:**

Template inspiration: `"{adversary_media} perspective {regional} {conflict} {subject}"`

Variables (H7 adversary):
- `adversary_media`:
  - Russia: RT, TASS, Sputnik
  - China: CGTN, Global Times, Xinhua
  - LatAm: TeleSUR, Telesur English
  - Iran: PressTV, Fars News
  - Regional: Al Jazeera, Middle East Eye
- `regional`: russe, chinoise, latino-américaine, iranienne, arabe
- `conflict`: Ukraine, Gaza, Taiwan, Syria, Yemen, Venezuela

Concrete examples:
```
Subject: "Ukraine offensive OTAN provocation"
→ "RT TASS CGTN perspective russe chinoise Ukraine offensive OTAN provocation analyse"

Subject: "Gaza 2024 Israel war crimes"
→ "Al Jazeera Middle East Eye Palestinian perspective Gaza Israel crimes guerre 2024"

Subject: "Taiwan tensions China threat"
→ "CGTN Global Times Xinhua Chinese perspective Taiwan reunification US provocations"
```

**NETWORK (🌐) + ELITE ANALYSIS:**

Template inspiration: `"{investigative} cartographie {elite_networks} {revolving_doors} {institution}"`

Variables:
- `investigative`: Mediapart, Disclose, Blast, The Intercept, ProPublica, Organized Crime and Corruption Reporting Project
- `elite_networks`: réseaux élites, pantouflage, revolving doors, Grandes Écoles alumni, think tank networks
- `institution`: gouvernement, régulateurs, cabinets conseil, multinationales

Concrete examples:
```
Subject: "ARCOM composition membres"
→ "Mediapart Blast cartographie réseaux élites ARCOM nominations Macron ENA pantouflage"

Subject: "Revolving doors SEC Wall Street"
→ "ProPublica investigates SEC Wall Street revolving doors Goldman Sachs alumni networks"
```

---

### 4.5 Adaptive Cross-Domain Examples

**LLM should COMBINE patterns when multiple detected:**

**ICEBERG + MONEY (Ξ + €):**

Template: `"{union} + {watchdog} enquête {hidden_funding} + {labor_exploitation}"`

Example:
```
Subject: "Travail détaché BTP exploitation salaires"
→ "CGT CFDT Anticor enquête financement caché travail détaché exploitation BTP dumping social"
```

**FRAMING + GASLIGHTING (Λ + GAS):**

Template: `"{analyst} déconstruit {frame} + {academic} archives {contradiction}"`

Example:
```
Subject: "Dette publique insoutenable réformes nécessaires"
→ "Économistes Atterrés déconstruit framing dette + chercheurs archives contradiction promesses budgétaires Maastricht"
```

**NETWORK + BIO (🌐 + ♦):**

Template: `"{investigative} map {elite_networks} + {biographical} {revolving_doors} {institution}"`

Example:
```
Subject: "McKinsey gouvernement Macron contrats"
→ "Mediapart Anticor cartographie réseaux élites McKinsey + parcours Kasbarian Kohler pantouflage cabinets ministères"
```

**WARFARE + TEMPORAL (⚔ + ⏰):**

Template: `"{adversary_media} timeline {escalation} + {geopolitical} {cui_bono}"`

Example:
```
Subject: "Syria chemical weapons 2018 timeline"
→ "RT TASS timeline escalation Syria chemical weapons 2018 + Russian perspective cui bono regime change"
```

---

### 4.6 Critical Usage Guidelines

**THESE TEMPLATES ARE INSPIRATION FOR LLM CREATIVE REASONING, NOT RIGID FILL-IN-BLANKS.**

LLM MUST:

1. **Understand pattern dialectics**: Who contests? Who loses from status quo? Who benefits from counter-narrative?

2. **Identify domain-specific dissidents**: Adapt France → EU → global based on topic scope

3. **Generate queries that TARGET dissident analyses**: Not mainstream media coverage ABOUT dissidents, but dissidents' OWN analyses

4. **Maintain hostile epistemology (95% suspicion)**: Dissidents are NOT auto-trusted. Same ◈◉○ stratification applies. Dissident claims MUST be validated with evidence.

5. **Balance exploration + exploitation**: 50% baseline generic queries (exploration) + 50% contextualized dissident queries (exploitation)

**Success metric:** Dissident queries return analyses/critiques/investigations from counter-powers themselves, not media reports about them.

**Example GOOD vs BAD:**

❌ BAD (generic): "CGT salaires France"
→ Returns: Media coverage about CGT, unrelated news

✅ GOOD (contextualized): "CGT critique EQTP exclusion temps partiel statistiques salaires"
→ Returns: CGT reports analyzing EQTP methodology, syndical position papers, critiques

❌ BAD (media about dissident): "Transparency International Pfizer"
→ Returns: News articles mentioning both

✅ GOOD (dissident analysis): "Transparency International enquête contrats secrets Pfizer clauses cachées"
→ Returns: Transparency International investigative reports, leaked contract analyses

---

### 4.7 Complexity-Adaptive Application

From system.md §0.4:

- **SIMPLE (0-3)**: Quick heuristics, 1-2 hypotheses max, 2-3 dissidents, 2-3 contextualized queries
- **MEDIUM (4-6)**: Full analysis, 2-3 hypotheses, 3-5 dissidents, 3-5 contextualized queries
- **COMPLEX (7-8)**: Extended analysis, 3-4 hypotheses, 5-7 dissidents, 5-7 contextualized queries
- **APEX (9-10)**: Comprehensive, 4+ hypotheses, 7+ dissidents + cross-domain mapping, 7+ contextualized queries

---

**END §4 DISSIDENT PERSPECTIVES v8.7**

---

**END QUERY_TEMPLATES.md v1.1** (added §4 DISSIDENT PERSPECTIVES)
