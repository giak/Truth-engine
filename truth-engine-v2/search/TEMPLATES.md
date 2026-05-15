# QUERY TEMPLATES v2.0 — Domain-Adaptive Search Execution

---

## §1 PRIMARY EVIDENCE TEMPLATES (◈)

| Domain | Keywords | T1 | T2 | T3 |
|--------|----------|----|----|----|
| POL | election,government,policy,minister | site:assemblee-nationale.fr OR site:senat.fr filetype:pdf | archives officielles | {entity} leaked OR FOIA |
| SCI | study,research,trial,peer-reviewed | site:pubmed.ncbi.nlm.nih.gov OR site:arxiv.org OR doi: | peer-reviewed OR clinical trial filetype:pdf | original research NOT review |
| CORP | company,CEO,SEC,lawsuit,merger | site:sec.gov filetype:pdf (10-K OR 10-Q OR 8-K) | court documents OR lawsuit | annual report OR financial filing |
| GEO | war,diplomacy,sanctions,treaty,UN | site:wikileaks.org OR diplomatic cable | UN documents OR treaty text | declassified OR FOIA OR archives |
| LEG | court,statute,ruling,regulation | site:courtlistener.com OR court ruling | statute text OR regulation | oral arguments transcript OR filing |
| ECO | GDP,inflation,trade,IMF,fiscal | site:imf.org OR site:worldbank.org | GDP statistics OR trade data | budget filetype:pdf OR fiscal report |
| SOC | inequality,protest,survey,census | census data OR survey OR demographics | government report OR official study | testimonies OR primary sources |
| TECH | software,algorithm,patent,spec | source code OR github OR spec | RFC OR standard OR protocol | whitepaper OR patent filing |
| HIST | archives,records,documents,era | archives OR historical documents | original documents OR manuscripts | {period} official records |
| MED | broadcast,press,transcript,publication | original broadcast OR transcript | press release OR official statement | official communication OR public statement |

**Execution:** SELECT by domain → EXECUTE → VALIDATE: RAW→◈, Institutional→○, Independent→◉ → IF ◈<target: retry ccTLD/filetype/keywords

---

## §2 GEOGRAPHIC DIVERSITY (🌍)

**Native region:** FR→Francophonie | EN→Anglosphere | DE→DACH | ES→Latam | ZH→China | AR→MENA | RU→ex-USSR | JA→Japan | KO→Korea | PT→Brazil | TR→Turkey

**Comparables (1-liner per domain):**
- Political: SPD(DE) PASOK(GR) Labour(UK) PSOE(ES) / Podemos M5S Syriza / AfD Vox FPÖ
- Scientific: FDA(USA) EMA(EU) MHRA(UK) PMDA(JP) / Climate: CN IN US EU BR
- Corporate: Auto:US/DE/JP/CN | Tech:GAFAM/Alibaba/SAP | Energy:US/OPEC/RU/NO
- Geopolitical: War→involved+neighbors+non-aligned | Sanctions→sanctioner+sanctioned+third

**Query:** `"{comparable} + {keywords} + site:{ccTLD} + lang:{code}"` | `"{comparable} + {keywords} + regional perspective"`

**Validation:** `geo = continents/6×0.4 + non_native_pct×0.6` — S≥0.30 M≥0.35 C≥0.40 A≥0.50

---

## §3 ADVERSARY TEMPLATES (H7 🔥)

**Triggers:** election,government,war,conflict,military,sanctions,propaganda,disinformation,corruption,fraud,pharmaceutical,whistleblower,protest,surveillance,inequality → H7_MANDATORY

**Complexity override:** H7 ∧ cx<4.0 → force MEDIUM (◈≥2, H7 mandatory, budget 10, EDI≥0.50)

**Templates:**
```
DISSIDENT:  "{subject} criticism OR opposition OR counter-narrative"
            "{subject} alternative media OR dissident OR censored"
            "{subject} radical analysis OR anti-establishment OR deplatformed"
COUNTER:    "{entity} scandals OR controversies OR accusations"
            "{subject} independent investigation OR watchdog OR exposé"
            "{subject} adversary perspective OR opposing view"
MAP-BASED:  IF entity IN H7_MAP: site:{source} "{subject}" {keywords}
```

**Validation:** (🔥 + ⟐̅) ≥ 2 minimum. Not met + H7 → EDI -0.15 + "⚠️ CARTOGRAPHIE INCOMPLÈTE"

---

## §4 DISSIDENT PERSPECTIVES (🔥 Counter-Power)

**Philosophy:** Examples, not rigid templates. LLM adapts creatively. Integrate @PAT[ICEBERG], @PAT[MONEY], @PAT[FRAMING], @PAT[GAS].

**Labor:** `"{union} critique {methodology} exclusion {hidden} {subject}"` — Unions: CGT CFDT FO Solidaires (FR) AFL-CIO SEIU (US) DGB IG Metall (DE) TUC (UK) | Hidden: temps partiel subis, sous-emploi, halo chômage

**Economic:** `"{heterodox_economist} déconstruit framing {dichotomy} {subject}"` — Économistes Atterrés, ATTAC, Friot, Lordon, Piketty (FR) | Ha-Joon Chang, Steve Keen (INTL)

**Corporate:** `"{watchdog} enquête {opacity} {entity} {subject}"` — Transparency Intl, Anticor, Sherpa, PPLAAF, Mediapart, Disclose, Blast, ProPublica

**Pharma:** `"{independent_medical} analyse critique {framing} {subject}"` — Prescrire, Formindep, Cochrane, Ben Goldacre

**Political:** `"{academic} documente {contradiction} {subject} archives"` — promesses/actes, discours/votes

**Institutional:** `"{civic_watchdog} suit {facade_vs_reality} {institution}"` — Regards Citoyens, Anticor, Observatoire éthique publique

**Geopolitical:** `"{adversary_media} perspective {regional} {conflict}"` — RT TASS Sputnik (RU) CGTN GlobalTimes (CN) PressTV (IR) AlJazeera MiddleEastEye TeleSUR

**Elite:** `"{investigative} cartographie {elite_networks} {revolving_doors}"` — Mediapart Disclose Blast Intercept ProPublica OCCRP

**Cross-domain:** Ξ+€ → "{union}+{watchdog} {hidden_funding}" | Λ+GAS → "{analyst} {frame}+{academic} {contradiction}" | 🌐+♦ → "{investigative} {elite_networks}+{revolving_doors}" | ⚔+⏰ → "{adversary_media} {escalation}+{cui_bono}"

**Guidelines:** Understand dialectics | Domain-specific dissidents | Target their OWN analyses | 95% suspicion | 50% baseline + 50% contextualized

**Complexity:** S:2-3 dissidents | M:3-5 | C:5-7 | A:7+ cross-domain

---

## §5 RETRY STRATEGIES

```
PRIMARY: ccTLD (.fr→.gov→.org) | filetype (pdf→doc→html) | keywords ("leaked"→"documents")
GEO: broader regions (site:.de→Europe OR international)
ADVERSARY: "{subject} criticism" OR "opposition" OR "controversy"
```

---

## §6 Integration

```
STEP 0: Domain + Complexity + H7 trigger
STEP 1: PRIMARY_◈=min(3,c×0.30) | ADVERSARY_H7=IF trigger:min(3,c×0.25) | DIVERSITY=rest
STEP 2: Execute domain templates
STEP 3: Validate (◈, geo, H7) + retry
STEP 4: Output with validation warnings
```

---

*QUERY TEMPLATES v2.0 — Compressed.*
