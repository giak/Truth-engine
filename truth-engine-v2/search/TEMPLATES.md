# QUERY TEMPLATES v2.0 — Domain-Adaptive Search Execution

## §1 PRIMARY EVIDENCE TEMPLATES (◈)

### 1.1 Domain Detection

Auto-detect from subject keywords:

| Domain | Keywords |
|--------|----------|
| Political | election, government, policy, parliament, minister, legislation |
| Scientific | study, research, trial, data, peer-reviewed, clinical |
| Corporate | company, CEO, financial, earnings, SEC, lawsuit, merger |
| Geopolitical | war, diplomacy, sanctions, military, treaty, UN, conflict |
| Legal | court, law, statute, ruling, case, regulation, judge |
| Economic | GDP, inflation, trade, central bank, IMF, fiscal, monetary |
| Social | inequality, protest, survey, census, demographics, civil rights |
| Tech | software, algorithm, patent, RFC, specification, source code |
| Historical | archives, records, documents, era, period, century |
| Media | broadcast, press release, transcript, publication, journalism |

### 1.2 Templates by Domain

```yaml
POL: 1) {subject} site:assemblee-nationale.fr OR site:senat.fr filetype:pdf
     2) {subject} archives officielles OR documents parlementaires
     3) {entity} leaked OR FOIA OR négociations

SCI: 1) {subject} site:pubmed.ncbi.nlm.nih.gov OR site:arxiv.org OR doi:
     2) {subject} peer-reviewed study OR clinical trial data filetype:pdf
     3) {subject} original research (NOT review NOT commentary)

CORP: 1) {entity} site:sec.gov filetype:pdf (10-K OR 10-Q OR 8-K)
      2) {entity} court documents OR lawsuit filing OR settlement
      3) {entity} annual report official OR financial filing

GEO: 1) {subject} site:wikileaks.org OR diplomatic cable OR state department
     2) {subject} UN documents OR treaty text OR Security Council resolution
     3) {subject} declassified OR FOIA OR government archives

LEG: 1) {subject} site:courtlistener.com OR court ruling
     2) {subject} statute text OR regulation official OR legal code
     3) {case} oral arguments transcript OR court filing

ECO: 1) {subject} site:imf.org OR site:worldbank.org OR central bank data
     2) {subject} GDP statistics OR trade data OR economic indicators
     3) {country} budget filetype:pdf OR fiscal report

SOC: 1) {subject} census data OR survey results OR demographic statistics
     2) {subject} government report OR official study OR field research
     3) {subject} testimonies OR direct accounts OR primary sources

TECH: 1) {subject} source code OR github OR technical specification
      2) {subject} RFC OR standard OR protocol documentation
      3) {subject} whitepaper OR technical report OR patent filing

HIST: 1) {subject} archives OR historical documents OR primary records
      2) {subject} original documents OR manuscripts OR correspondence
      3) {period} official records OR government archives

MED: 1) {subject} original broadcast OR press conference transcript
     2) {subject} press release official OR statement original
     3) {entity} official communication OR public statement
```

### 1.3 Execution Rules

```yaml
FOR EACH query allocated to PRIMARY_◈:
  1. SELECT template based on domain_detected
  2. EXECUTE with {subject}, {entity}, {period} variables
  3. VALIDATE: RAW doc/data/leak → ◈ | Institutional analysis → ○ | Independent investigation → ◉
  4. IF ◈ < target AND budget > 0: RETRY with alternate ccTLD, filetype, broader keywords
```

---

## §2 GEOGRAPHIC DIVERSITY TEMPLATES (🌍)

### 2.1 Native Region Detection

```yaml
FR → France/Francophonie | EN → USA/UK/Anglosphere | DE → Germany/DACH
ES → Spain/Latam | ZH → China/Taiwan | AR → Middle East/North Africa
RU → Russia/ex-USSR | JA → Japan | KO → Korea | IT → Italy
PT → Portugal/Brazil | NL → Netherlands/Belgium | PL → Poland | TR → Turkey
```

### 2.2 Domain-Adaptive Comparables

**Political**: Social democracy → SPD(DE), PASOK(GR), Labour(UK), PSOE(ES). Populism → Podemos(ES), M5S(IT), Syriza(GR). Far-right → AfD(DE), Vox(ES), FPÖ(AT). Corruption → Lava Jato(BR), 1MDB(MY), Panama Papers.

**Scientific**: Climate → China, India, USA, EU, Brazil regions. Pharma → FDA(USA), EMA(EU), MHRA(UK), PMDA(JP). AI regulation → USA, China, EU(GDPR), UK.

**Corporate**: Auto → USA(Detroit), Germany(VW/BMW), Japan(Toyota), China(BYD). Tech → USA(GAFAM), China(Alibaba/Tencent), EU(SAP/Spotify). Energy → USA(Texas), Middle East(OPEC), Russia, Norway.

**Geopolitical**: War → involved parties + neighbors + non-aligned. Sanctions → sanctioner + sanctioned + third parties.

### 2.3 Query Pattern

```yaml
- "{comparable} + {subject_keywords} + site:{ccTLD} + lang:{code}"
- "{comparable} + {subject_keywords} + regional perspective"
- "{region} + {subject_keywords} + international coverage"
```

### 2.4 Validation Targets

```yaml
geo_diversity = continents/6 × 0.4 + non_native_region_pct × 0.6
TARGETS: SIMPLE ≥0.30 | MEDIUM ≥0.35 | COMPLEX ≥0.40 | APEX ≥0.50
```

---

## §3 ADVERSARY PERSPECTIVE TEMPLATES (H7 🔥)

### 3.1 Sensitivity Triggers

```yaml
KEYWORDS: Politics:[election,government,policy,parliament,legislation]
          Geopolitical:[war,conflict,military,sanctions,intervention]
          Info-ops:[propaganda,disinformation,censorship,manipulation]
          Economic:[corruption,fraud,lobbying,monopoly,cartel]
          Corporate:[scandal,cover-up,whistleblower,lawsuit,pharmaceutical]
          Social:[protest,repression,surveillance,inequality,strike]
IF ANY keyword IN query → H7_MANDATORY = True
```

### 3.2 H7 Complexity Override

IF H7_sensitive = True AND complexity < 4.0 → complexity = 4.0 (MEDIUM minimum). Apply MEDIUM allocations: PRIMARY_◈ ≥2, ADVERSARY_H7 mandatory, CONTEXT_⟐ ≥2, DIVERSITY ≥2, budget 10 queries, EDI target ≥0.50.

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

TEMPLATE_H7_MAP_BASED:
  IF entity IN H7_MAP:
    FOR source IN H7_MAP[entity]:
      query = 'site:{source.url} "{subject}" {keywords}'
      keywords = ["official response", "perspective", "statement", "analysis"]
```

### 3.4 Validation

```yaml
COUNT adversary_sources: 🔥_dissident + ⟐̅_counter
TARGET: (🔥 + ⟐̅) ≥ 2 minimum
IF not met AND H7_triggered: → EDI penalty -0.15 + "⚠️ CARTOGRAPHIE INCOMPLÈTE"
```

---

## §4 DISSIDENT PERSPECTIVES TEMPLATES (🔥 Counter-Power)

**Philosophy**: Examples, not rigid templates. LLM adapts creatively based on domain, geography, and detected patterns. Integrate with @PAT[ICEBERG], @PAT[MONEY], @PAT[FRAMING], @PAT[GAS].

### 4.1 Labor & Social Justice

**ICEBERG + LABOR**: `"{union} critique {methodology} exclusion {hidden_population} {subject}"`
- Unions: CGT, CFDT, FO, Solidaires (FR) | AFL-CIO, SEIU (USA) | DGB, IG Metall (DE) | TUC (UK)
- Methodology: EQTP, BIT definition, sampling bias, statistical manipulation
- Hidden: temps partiel subis, sous-emploi, halo chômage, DEFM B-E, travailleurs précaires

**FRAMING + ECONOMIC**: `"{heterodox_economist} déconstruit framing {dichotomy} {subject}"`
- Economists: Économistes Atterrés, ATTAC, Friot, Lordon, Piketty (FR) | Ha-Joon Chang, Steve Keen (INTL)
- Dichotomy: moyen/médian, croissance/décroissance, compétitivité/solidarité

### 4.2 Corporate & Financial Accountability

**MONEY + CORPORATE**: `"{watchdog} enquête {opacity} {entity} {subject}"`
- Watchdogs: Transparency International, Anticor, Sherpa, PPLAAF, Mediapart, Disclose, Blast, ProPublica
- Opacity: contrats secrets, flux cachés, bénéficiaires réels, conflits intérêt, lobbying caché

**FRAMING + PHARMA**: `"{independent_medical} analyse critique {framing} {subject}"`
- Sources: Prescrire, Formindep, Cochrane Collaboration, Ben Goldacre
- Framing: efficacité absolue vs relative, balance bénéfices/risques, conflicts of interest

### 4.3 Political & Institutional Critique

**GASLIGHTING + POLITICAL**: `"{academic} documente {contradiction} {subject} archives"`
- Contradiction: promesses/actes, discours/votes, annonces/budgets

**CYNICISM + INSTITUTIONAL**: `"{civic_watchdog} suit {facade_vs_reality} {institution}"`
- Watchdogs: Regards Citoyens, Anticor, Observatoire éthique publique, Transparency International
- Facade: votes/abstentions, conflits intérêt, nominations politiques, revolving doors

### 4.4 Geopolitical & Warfare

**WAR + GEOPOLITICAL**: `"{adversary_media} perspective {regional} {conflict} {subject}"`
- Russia: RT, TASS, Sputnik | China: CGTN, Global Times, Xinhua | Iran: PressTV, Fars
- Regional: Al Jazeera, Middle East Eye | LatAm: TeleSUR

**NETWORK + ELITE**: `"{investigative} cartographie {elite_networks} {revolving_doors} {institution}"`
- Sources: Mediapart, Disclose, Blast, The Intercept, ProPublica, OCCRP

### 4.5 Cross-Domain Combinations

| Patterns | Template |
|----------|----------|
| ICEBERG + MONEY (Ξ+€) | "{union} + {watchdog} enquête {hidden_funding} + {labor_exploitation}" |
| FRAMING + GASLIGHTING (Λ+GAS) | "{analyst} déconstruit {frame} + {academic} archives {contradiction}" |
| NETWORK + BIO (🌐+♦) | "{investigative} map {elite_networks} + {biographical} {revolving_doors}" |
| WARFARE + TEMPORAL (⚔+⏰) | "{adversary_media} timeline {escalation} + {geopolitical} {cui_bono}" |

### 4.6 Usage Guidelines

LLM MUST:
1. Understand pattern dialectics — Who contests? Who loses? Who benefits from counter-narrative?
2. Identify domain-specific dissidents — Adapt France → EU → global
3. Target dissident OWN analyses, not media coverage ABOUT dissidents
4. Maintain hostile epistemology (95% suspicion) — Same ◈◉○ stratification applies
5. Balance 50% baseline generic queries + 50% contextualized dissident queries

**Success metric**: Dissident queries return analyses/critiques from counter-powers themselves.

### 4.7 Complexity-Adaptive Application

| Complexity | Dissidents | Contextualized Queries |
|------------|------------|----------------------|
| SIMPLE (0–3) | 2–3 | 2–3 |
| MEDIUM (4–6) | 3–5 | 3–5 |
| COMPLEX (7–8) | 5–7 | 5–7 |
| APEX (9–10) | 7+ cross-domain | 7+ |

---

## §5 RETRY STRATEGIES

```yaml
PRIMARY_RETRY (if ◈ < target):
  Alternate 1: ccTLD (.fr → .gov → .org)
  Alternate 2: filetype (pdf → doc → html)
  Alternate 3: keywords ("leaked" → "documents" → "archives")

GEOGRAPHIC_RETRY (if geo_diversity < target):
  Alternate: broader regions (site:.de → Europe OR international)

ADVERSARY_RETRY (if (🔥 + ⟐̅) < 2):
  Alternate: "{subject} criticism" OR "{subject} opposition" OR "{subject} controversy"
```

---

## §6 Integration

```yaml
STEP 0: Domain + Complexity detection + H7 trigger check
STEP 1: Query allocation: PRIMARY_◈ = min(3, ceil(complexity × 0.30))
        ADVERSARY_H7 = IF trigger: min(3, ceil(complexity × 0.25)) ELSE 0
        DIVERSITY_GEO = budget_remaining - 1
STEP 2: Execute with domain templates
STEP 3: Validate (◈_count, geo_diversity, H7_adversary) + retry if gaps
STEP 4: Output Part 1+2+3 with validation warnings
```

---

*QUERY_TEMPLATES v2.0*
