# INVESTIGATION — Complete Pipeline

**Version:** 2.0
**Language:** English (user-facing narrative output in French)
**Referenced by:** KERNEL.md §1

---

## §0 SCOPING

**Input:** subject (any topic)
**Output:** SCOPING_REPORT

### Steps:
1. **Central question:** 1 sentence capturing the core investigation
2. **Domains:** Which domains are relevant? (MILITARY, FINANCIAL, DIPLOMATIC, HUMANITARIAN, ENERGY, LEGAL, TECHNICAL, SOCIAL, ENVIRONMENTAL)
3. **Actors:** Who are the key actors? (named individuals, not institutions)
4. **Questions:** Generate 12-20 CRÉDO questions in query-ready format
5. **Evidence types:** What evidence exists? (leaks, FOIA, court docs, satellite, market data)
6. **Exclusions:** What is OUT of scope? (and why)

### Complexity Scoring (6 dimensions):

| Dimension | Points | Rule |
|-----------|--------|------|
| political_sensitivity | 1-3 | ≥2 crises = 3, national = 2, EU/intl = 1 |
| technical_depth | 1-2 | Multiple regulatory frameworks = 2 |
| temporal_span | 1-5 | ≤7d=1, wks=2, 1-10yr=3, decades=4, centuries=5 |
| geographical_scope | 1-5 | Local=1, ≥3 regions=2, national=3, EU=4, global=5 |
| conflicting_narratives | 1-3 | ≥3 groups = 3 |
| data_availability | 1-2 | Contradictory data = 2 |

**Classification:** score <3 = SIMPLE | <6 = MEDIUM | <8 = COMPLEX | ≥8 = APEX

### Complexity-Driven Budget:

| Level | Queries | Wolves | Domains | ✦ Facts | Chains | Sections |
|-------|---------|--------|---------|---------|--------|----------|
| SIMPLE | 12 | 5 | 2 | 5 | 1 | 5 |
| MEDIUM | 18 | 5 | 3 | 8 | 2 | 7 |
| COMPLEX | 25 | 8 | 4 | 10 | 3 | 8 |
| APEX | 35+ | 12 | 5 | 15 | 5 | 9 |

---

## §1 ANALYSIS

**Input:** text (article, report, transcript, social media)
**Output:** MANIPULATION_REPORT

### Steps:
1. Load definitions/SYMBOLS.md §1 (15 narrative symbols)
2. Load definitions/PATTERNS.md (all @PAT[])
3. Load definitions/THREATS.md (all @THR[])
4. Load clusters/*.md (thresholds in definitions/SYMBOLS.md §4)
5. Execute scan using loaded definitions
6. Generate MANIPULATION_REPORT

### MANDATORY:
- Scan ALL 15 symbols (Ξ € Λ Ω Ψ ↕ Φ Σ Κ ρ κ ⫸ ⚔ 🌐 ⏰)
- Check ALL @PAT[] patterns from definitions/PATTERNS.md
- Check ALL @THR[] threats from definitions/THREATS.md
- Check rhetorical families (DEM, BF, NUM, AUTH, FAC)

### MANIPULATION_REPORT format:
```
SYMBOLS_DETECTED: {Ξ, €, Λ, ...} with scores [0-10]
PATTERNS_ACTIVATED: [@PAT[ICEBERG], ...]
THREATS_DETECTED: [@THR[SHOCK], ...]
RHETORICAL_FAMILIES: {DEM, BF, NUM, AUTH, FAC}
CLUSTERS_TO_LOAD: [list]
IMPLICIT_CLAIMS: [what is implied, not said, inverted]
SPEAKER_PROFILE: {tone, target, goal}
VERIFICATION_PRIORITIES: [what to verify first]
QUERY_GUIDANCE: [how techniques guide searches]
```

### SYMBOL → ACTION (from definitions/SYMBOLS.md §7):
Each symbol with score ≥5 generates investigation branches:
- Ξ ≥ 5 → BRANCH "Hidden reality" + forensic/REASONING.md
- € ≥ 5 → BRANCH "Financial flows" + clusters/MONEY.md
- ⏰ ≥ 5 → BRANCH "Timing forensics" + P_random calculation
- etc.

---

## §2 SEARCH

**Input:** MANIPULATION_REPORT + CRÉDO questions
**Output:** Search results

### Steps:
1. Execute queries with budget (12/18/25/35+)
2. Stratify sources ◈◉○ (see search/EPISTEMIC.md §1)
3. Track coverage
4. Reallocate at 50% if gaps (see KERNEL §2.5)

### Query Distribution:
| Category | % | Focus |
|----------|---|-------|
| PRIMARY (◈) | 35% | Leaks, FOIA, data |
| ADVERSARY | 20% | Counter-narrative |
| CONTEXT | 20% | Academic, regional |
| DIVERSITY | 15% | Alternative perspectives |
| WOLF | 10% | Specific actors named |

### Reallocation (at 50% queries):
```
IF ◈_collected < target × 0.5 → +15% from DIVERSITY to PRIMARY
IF adversary_sources < 2 → +10% from CONTEXT to ADVERSARY
IF geo_diversity < target × 0.5 → +10% from WOLF to DIVERSITY
IF wolves_identified < 3 AND complexity ≥ 6 → +10% from DIVERSITY to WOLF
```

---

## §3 CONSTRUCTION

**Input:** Search results
**Output:** FACT_REGISTRY + KNOWLEDGE_STATE

### Steps:
For each search result:
1. **EXTRACT:** what happened, who, when, where, how much
2. **CLASSIFY:** ✦ hard_fact / ✧ soft_fact / ⁕ claim / ⁂ speculation
3. **SOURCE:** ◈◉○ tier (see search/EPISTEMIC.md §1)
4. **CROSS-CHECK:** found in ≥2 independent sources?
   → ⊕ confirmed / ⊗ contradicted / ⊙ partial
5. **REGISTER:** add to FACT_REGISTRY

### FACT_REGISTRY:
```
✦ CONFIRMED: [N] facts (≥2 independent sources, ⊕)
✧ PROBABLE: [N] facts (1 strong ◈ source, coherent)
⁕ CLAIMED: [N] facts (asserted ○, not cross-verified)
⁂ SPECULATED: [N] hypotheses (logical inference, no direct evidence)
⊗ CONTRADICTED: [N] contradictions (sources disagree)
⊙ PARTIAL: [N] partially confirmed
```

### KNOWLEDGE_STATE:
```
KNOWN: [summary of ✦ confirmed facts]
SUSPECTED: [summary of ✧ probable + ⁕ claimed]
UNKNOWN: [gaps identified]
```

### MANDATORY FOR APEX:
- ≥10 confirmed facts (✦)
- ≥3 contradictions identified (⊗)
- KNOWLEDGE_STATE with all 3 states
- Each fact linked to source (◈◉○)

### FEEDBACK:
IF FACT_REGISTRY ✦ < minimum (APEX:10, COMPLEX:8, MEDIUM:5) → RETURN to §2
IF FACT_REGISTRY ⊗ == 0 for APEX → RETURN to §2 with H7 adversarial search

---

## §4 CAUSALITY

**Input:** FACT_REGISTRY + SYMBOL_SCORES (from §1)
**Output:** TIMELINE + CASCADE_CHAINS + CROSS_DOMAIN_FLOWS + SUSPICIOUS_TIMING

### Steps:
1. **TIMELINE:** Order all ✦ confirmed facts chronologically
2. **LINK:** For each fact, ask "what caused this?" and "what did this cause?"
3. **CHAIN:** Build chains of ≥3 links (event → consequence → consequence → endpoint)
4. **CROSS-DOMAIN:** Trace how consequences flow across domains:
   - MILITARY → ENERGY → FOOD → HUMANITARIAN
   - MILITARY → FINANCIAL → INSIDER_TRADING → LEGAL
   - DIPLOMATIC → GEOPOLITICAL → ECONOMIC → SOCIAL
5. **QUANTIFY:** Each chain endpoint must be quantified (deaths, $, %, populations)

### SYMBOL_CAUSAL_QUESTIONS (generated for each symbol ≥5):
```
Ξ ≥ 5: "What is hidden? Who excluded? Why? What's the real number?"
€ ≥ 5: "Who profits? How much? Via which channels? Who loses?"
Λ ≥ 5: "What frame is imposed? What alternatives excluded? Who benefits?"
Ω ≥ 5: "What's the inversion? What's the real reality? Who inverts?"
⏰ ≥ 5: "What's the suspicious timing? What's P_random? Who orchestrated?"
⚔ ≥ 5: "Who coordinates? What sophistication? Who's the target?"
🌐 ≥ 5: "Who's at center? What topology? Who controls?"
♦ ≥ 5: "What hidden networks? What elite reproduction? What democratic risk?"
```

### TIMELINE format:
```
[DATE] → [EVENT] → [SOURCE ◈◉○] → [CONSEQUENCE]
```

### CASCADE_CHAINS format:
```
Chain N: [event] → [consequence] → [consequence] → [endpoint (quantified)]
```

### SUSPICIOUS_TIMING:
Events with ⏰≥5 or P_random < 1% (see definitions/PATTERNS.md @PAT[TEMP])

### MANDATORY FOR APEX:
- ≥10 timeline events
- ≥3 cascade chains with ≥3 links each
- ≥1 cross-domain flow
- ≥1 suspicious timing flagged (⏰)
- Each chain endpoint quantified

### FEEDBACK:
IF CAUSALITY_CHAINS < minimum (APEX:3, COMPLEX:2) → RETURN to §2

---

## §5 IMPACT

**Input:** FACT_REGISTRY + CAUSALITY_CHAINS + WOLF_PROFILES (from §6)
**Output:** IMPACT_VERDICT (4 matrices)

### IMPACT_VERDICT:
**Qui gagne.** [Actor] — [gain quantifié]. [Actor] — [gain].
**Qui perd.** [Actor] — [perte quantifiée]. [Actor] — [perte].
**Qui meurt.** [Chiffre] — [contexte humanitaire].
**Qui recule.** [Actor] — [signes de déclin].

### Rules:
- Each entry MUST have ≥1 number (deaths, $, %)
- "Qui meurt" MUST prioritize human cost over economic cost
- "Qui recule" MUST identify structural decline (not tactical)
- "Qui gagne" MUST include ≥1 entity that benefits from the crisis
- "Qui perd" MUST include both direct losses and indirect consequences

### Verification:
- Cross-check "Qui gagne" with € MONEY_Factor results
- Cross-check "Qui meurt" with humanitarian sources
- Flag if ANY dimension (mil/eco/geo/human) is missing
- Flag if "Qui meurt" is empty (human cost always exists)

### Connections to existing tools:
- € MONEY_Factor → feeds "Qui gagne"
- ♦ BIO_Factor → feeds actor profiles
- 🌐 NET_Power → feeds "Qui recule"
- ⚔ WAR_Factor → feeds conflict analysis
- @PAT[POLITICAL] → Cui_Bono_Political
- @PAT[GEOPOLITICAL] → Cui_Bono_Geopolitical

### MANDATORY FOR APEX:
- All 4 matrices populated
- ≥1 quantified entry per matrix
- "Qui meurt" non-empty
- Cross-referenced with symbol outputs (€♦🌐⚔)

---

## §6 VERIFICATION

**Input:** FACT_REGISTRY
**Output:** VERIFICATION_REPORT

### Steps:
For each ✦ CONFIRMED or ✧ PROBABLE fact:
1. **CLASSIFY by domain:**
   - MILITARY: weapon, operation, casualty, capability, deployment
   - FINANCIAL: amount, trade, transaction, market, insider
   - DIPLOMATIC: meeting, agreement, negotiation, threat, treaty
   - HUMANITARIAN: victims, displacement, famine, health, education
   - ENERGY: oil, gas, shipping, disruption, reserves
   - LEGAL: law, regulation, court, sanction, subpoena
   - TECHNICAL: system, capability, infrastructure, satellite

2. **VERIFY with domain-specific protocol:**
   - MILITARY: DoD + satellite + independent observers → CONFIRMED / UNCONFIRMED / COVERED_UP
   - FINANCIAL: SEC + market data + court docs → VERIFIED / PATTERN / SUSPICIOUS / CONFIRMED_FRAUD
   - HUMANITARIAN: Amnesty + UN + Red Cross + local sources → CONFIRMED / DISPUTED / UNVERIFIED
   - DIPLOMATIC: State Dept + leaked cables + participant statements → CONFIRMED / LEAKED / DENIED

3. **FLAG contradictions:**
   - If official narrative contradicts independent sources → ⊗ CONTRADICTED
   - If official count << independent count → COVER-UP suspected

4. **UPGRADE facts:**
   - ⁕ → ✧ (if corroborated by ≥1 additional source)
   - ✧ → ✦ (if cross-verified by ≥2 independent sources)

### VERIFICATION_REPORT:
```
VERIFIED: [N] facts upgraded
CONADICTIONS: [N] official vs independent
COVER-UPS: [N] identified
PER-DOMAIN: mil/fin/dip/hum/energy/legal/tech breakdown
```

### MANDATORY FOR APEX:
- ≥2 domains verified
- ≥1 contradiction documented
- ≥1 fact upgraded (⁕→✧ or ✧→✦)
- VERIFICATION_REPORT with per-domain breakdown

### FEEDBACK:
IF domains_verified < minimum (APEX:2) → RETURN to §2
IF unverified_facts > 30% → RETURN to §2 with corroboration queries

---

## §7 INVESTIGATION OUTPUT (in French)

**Input:** All previous phases (§0-§6)
**Output:** Complete investigation (9 sections)

### Structure (mandatory sections):

**1. RÉSUMÉ EXÉCUTIF** (≤500 words, in French)
- Ce qui s'est passé (5 faits clés)
- Qui l'a fait (acteurs clés avec profils ♦ BIO)
- Pourquoi c'est important (impact quantifié)
- Ce qu'on ne sait pas (gaps de KNOWLEDGE_STATE)

**2. CHRONOLOGIE** (chronological, ≥10 events, in French)
- Tous les événements ✦ confirmés dans l'ordre
- Chaque événement: date, description, source ◈◉○, conséquence
- Timing suspect signalé (⏰ avec P_random)

**3. DOMAINES** (thematic sections, in French)
- Une section par domaine central
- Chaque section: faits, acteurs, conséquences, vérification
- Chaque section: "voile levé" (forensic/REASONING.md reconstruction)

**4. RÉSEAU D'ACTEURS** (in French)
- Carte réseau (🌐 NET_Power + ♦ BIO_Factor)
- Profils d'acteurs: nom, rôle, centralité, connexions
- Rôles: instigateur, exécutant, bénéficiaire, victime, dissident

**5. CHAÎNES DE CASCADE** (in French)
- Toutes les chaînes de §4
- Chaque chaîne: événement → conséquence → conséquence → point final
- Chaque point final: impact quantifié

**6. CARTE DES PREUVES** (in English — technical)
- Sources: ◈ N, ◉ N, ○ N
- Faits: ✦ N, ✧ N, ⁕ N, ⁂ N
- Contradictions: [liste avec ⊗]
- Cover-ups: [liste]
- EDI: score calculé (search/EPISTEMIC.md §4)
- Scores symboles: Ξ€ΛΩΨ↕ΦΣΚρκ⫸⚔🌐⏰ [scores]

**7. VERDICT D'IMPACT** (in French)
- Qui gagne / Qui perd / Qui meurt / Qui recule (de §5)

**8. PÉRIMÈTRE & LIMITES** (in French)
- Ce qui est EXCLU (liste explicite)
- Pourquoi (périmètre, temps, accès)
- Ce qui nécessiterait un suivi

**9. ÉTAT DES CONNAISSANCES** (in French)
- CONFIRMÉ: ce qu'on a confirmé ✦
- SUSPECTÉ: ce qu'on pense ✧ ⁕
- INCONNU: les gaps restants

### TONE:
Factual, dense, no filler. Each sentence = 1 fact.
FORMAT: Markdown with tables, citations, section headers.
LENGTH: No artificial limit. As long as needed for completeness.

### THIS IS THE INVESTIGATION. NOT THE ARTICLE.
The article is a post-processing of this investigation (see §8).

---

## §8 ARTICLE TRANSFORMATION (in French)

**Input:** Investigation from §7
**Output:** Publishable article (in French)

### Steps:
1. **ACCROCHE:** Compress RÉSUMÉ EXÉCUTIF → 1 dense paragraph (5 facts)
   - Use contrast (date X vs date Y)
   - No intro fluff

2. **SECTIONS:** Transform DOMAINES sections → thematic narrative
   - Each section starts with strongest fact
   - Each section ends with 1-line synthesis (blockquote)

3. **VERDICT:** Transform VERDICT D'IMPACT → 4-line matrices
   - Qui gagne / Qui perd / Qui meurt / Qui recule

4. **CONCLUSION:** 1 sentence capturing the entire case

5. **BIBLIOGRAPHIE:** Numbered, with URLs and dates

6. **DISCLAIMER:** From PÉRIMÈTRE & LIMITES
   - What was NOT covered
   - Why (scope, time, access)
   - What would need follow-up

### TONE:
Dense, factual, no filler. Each sentence = 1 fact. French language purity (see AGENTS.md).
LENGTH: No artificial limit.

### THIS IS THE ARTICLE. Separate from investigation.

---

## WOLVES

### Categories:
- GOVERNMENT: officials, ministers, presidents, PMs
- OPPOSITION: party leaders, critics
- CORPORATE: companies, CEOs, industry actors
- CIVIL_SOCIETY: NGOs, activists, unions
- INTERNATIONAL: foreign officials, ambassadors
- EXPERTS: academics, think tanks, analysts
- MEDIA: journalists, editors, outlets

### Auto-Detect from content:
- If € (money) high → expect CORPORATE
- If ↕ (vertical) high → expect EXPERTS
- If Ξ (iceberg) high → expect INSTITUTIONAL
- If Λ (framing) high → expect MEDIA

### Minimums:
- GOVERNMENT: ≥2 (if present)
- OPPOSITION: ≥1 (if present)
- CORPORATE: ≥1 (if € detected)
- EXPERTS: ≥1 (if technical_depth ≥ 2)
- MEDIA: ≥1 (if Λ detected)
- INTERNATIONAL: ≥1 (if geo ≥ 3)
- TOTAL: APEX ≥12, COMPLEX ≥8, MEDIUM ≥5

### Output:
```
WOLF_CATEGORY: [name] → ROLE: [role] → CENTRALITY: [0-1]
SECTOR_DETECTED: [list of sectors present in narrative]
```

---

## FEEDBACK LOOPS

```
§3 → §2: IF FACT_REGISTRY ✦ < minimum OR ⊗ == 0 → RETURN with gap queries
§4 → §2: IF CAUSALITY_CHAINS < minimum → RETURN with chain-completion queries
§6 → §2: IF domains_verified < minimum OR unverified >30% → RETURN with corroboration queries

MAX FEEDBACK LOOPS: 2 per investigation (prevent infinite loops)
```

---

## CRÉDO DIMENSIONS

| Dim | Focus | Symbols |
|-----|-------|---------|
| C | Timing, history, absentees | ⏰, Ξ |
| R | Cui bono, wolves, networks | €, ♦, 🌐 |
| E | Verification, primary sources | ◈, ⊕, ⊗ |
| D | Contradictions, gaps | Ω, Ψ, Ξ |
| O | Precedents, comparables | ⏰, Ξ |
| + | Multi-angle (pol/eco/geo/cult) | Λ, Φ, Σ |

**Format:** "Q:{question} → query:{search_string}"
**Min/Max:** 12-20 questions

---

## ACCUSATION TRIGGER

```
IF input CONTAINS accusation (X accuses Y of Z):
  THEN AUTO_GENERATE:
    - "Does X do same?" → query:"{X} exclusion médiatique comparaison"
    - "Who benefits from accusing?" → query:"{X} avantage politique {topic}"
    - "What's X's track record?" → query:"{X} historiques critiques médias"
  OUTPUT MUST INCLUDE: "SYMETRIC: {X} accuses {Y} but {X} also..."
```

---

## PERSO_FRESQUE

When investigation subject is a person → FORCE APEX + LOAD protocol/PERSO_FRESQUE.md
EDI target minimum: 0.75 pour APEX_FRESQUE

---

_Version 2.0 — Complete investigation pipeline_
_One concept, one place. No duplication._
