# SEARCH EPISTEMIC v2.0 — Source Pluralism & Narrative Cartography

---

## §1 SOURCE STRATIFICATION (◈◉○)

| Tier | Symbol | Types | Confidence |
|------|--------|-------|------------|
| **PRIMARY** | ◈ | Raw documents, leaks, court files, FOIA, data | 0.90–0.95 |
| **SECONDARY** | ◉ | Investigative journalism, academic research, expert testimony | 0.75–0.85 |
| **TERTIARY** | ○ | Mainstream media, aggregators, opinion, official statements | 0.40–0.70 |

**Priority**: ◈ > ◉ > ○. **Critical**: Official (⟐) weighted LOW (0.20) unless corroborated by ◈.

**Source reliability weights:** dissident_whistleblower:0.95 independent_investigative:0.90 field_testimony:0.85 alternative_media:0.80 archival_contradictions:0.80 international_opposing:0.75 official_institutions:0.20

**Classification algorithm:**
```
STEP_1: Govt/IGO/Military → ○ (0.20-0.40) | Corporate → check funding → ◉ or ○ | Independent/Academic → ◉ (0.75-0.85)
STEP_2: Contains leaked docs? → those elements only: ◈ (0.90-0.95). Source interpretation stays at STEP_1 tier.
STEP_3: ≥2 independent sources corroborate? → confidence +0.10-0.20 within tier. Circular = NOT valid.
Principles: Official≠Reliable | Evidence transcends institution | Interpretation inherits bias | Follow the money
```

---

## §2 DIVERSITY ANALYSIS

**Geographic:** Priority: LOCAL→NEIGHBOR→REGIONAL→DISTANT→HEGEMON(lowest). ≥2 continents, ≥1 local, avoid monoculture.

**Linguistic:** ≥30% non-English, ≥2 language families, primary language of affected region. Translation path affects confidence.

**Perspective (5 narratives):** ⟐ Official (consent) | ⟐̅ Counter (hidden interests) | 🌍 Regional (escape Western bias) | 🎓 Academic (depth) | 🔥 Dissident (what power hides)

**Ownership:** TYPES: [state, corporate, independent, academic, activist, personal]. Target: non-corporate ≥50%. Formula: `(types/6 × 0.6) + (non_corporate_pct × 0.4)`

**Temporal:** TYPES: [real_time, recent(<1w), medium(<1m), archival(>1y), historical]. Target: ≥3 temporalities. Formula: `(temporalities/5 × 0.6) + (archival_present × 0.4)`

---

## §3 CORROBORATION (⊕⊗⊙ ≋)

**Fact quality:** ✦ Hard (◈+⊕) | ✧ Soft (◉ coherent) | ⁕ Claim (○ only) | ⁂ Speculation (hypothesis)

**Corroboration:** ⊕ Confirmed (≥2◈ or ≥3◉ concordant) | ⊗ Contradicted (≥2◈ contradict) | ⊙ Partial (mixed)

**Divergence zones:** ≋+ (different emphasis) | ≋++ (contradictory claims) | ≋+++ (one side ◈, other ○)

---

## §4 EDI CALCULATION

**Formula (see KERNEL §1 step 16 for compact version):**
```
EDI = geo×0.25 + lang×0.20 + strat×0.20 + owner×0.15 + persp×0.15 + temp×0.05
```

**Dimension sub-formulas (NOT in KERNEL):**
```
geo:   (continents/6 × 0.4) + (zones/10 × 0.3) + (local_presence × 0.3)
lang:  (languages/10 × 0.3) + (non_english_pct × 0.4) + (families/5 × 0.3)
strat: (primary_pct × 0.5) + (secondary_pct × 0.3) + (tertiary_pct × 0.2)
owner: (types/6 × 0.6) + (non_corporate_pct × 0.4)
persp: (perspectives/7 × 0.5) + (official_vs_counter × 0.3) + (dissident_present × 0.2)
temp:  (temporalities/5 × 0.6) + (archival_presence × 0.4)
```

**Classification:** ≥0.65 EXCELLENT | ≥0.50 GOOD | ≥0.35 ACCEPTABLE | <0.35 EPISTEMIC_MONOCULTURE

**BIAS penalties (see KERNEL §1 step 16 for compact):**
| Penalty | Trigger | Weight |
|---------|---------|--------|
| P1: Institutional | govt>60% OR corp>60% | -0.20 |
| P1b: Power | govt+corp>75% | -0.25 |
| P2: No Adversary | sensitive + no dissident | -0.15 |
| P3: Echo Chamber | only ⟐, no ⟐̅/🔥 | -0.20 |
| P4: Tertiary Over | ○>70% | -0.15 |
| P5: Circular | same institutional family | -0.10 |

**Composite:** `EDI* = 0.5×EDI + 0.3×Coverage + 0.2×Independence` where Coverage=met_quotas/total, Independence=f(diversity, low_syndication)

**Output:** `EDI:{final} (raw:{raw} penalties:{sum}[flags]) | COV:{c} IND:{i} CC:{cc} → EDI*:{e}`

---

## §5 CONVERGENCE — 4-Iteration Protocol

```
C(n) = 1 - (new_info_at_n / total_info_discovered)    Target: ≥0.85
```

**Stopping:** ≥0.90→COMPLETE | ≥0.85+EDI≥0.60→SUFFICIENT | n≥3+C≥0.75→ACCEPTABLE | n>5→STOP

| Phase | Purpose | Sources | EDI | Convergence | Time |
|-------|---------|---------|-----|-------------|------|
| I0 Recon | Cartography + gaps | 8–15 | ~0.40 | — | 5–10m |
| I1 Explore | Fill gaps + ◈🎓🔥 | +5–10 | ~0.55 | C(1)~0.50 | 10–15m |
| I2 Deep | Triangulate + orchestration | +5 | exact | C(2)~0.75 | 15–20m |
| I3 Synthesis | Validation + output | final | ≥0.60 | C(3)≥0.85 | 5–10m |

**Budget:** 35–55min, 18–25 sources, EDI 0.60–0.75

**Orchestration (⚑):**
```
P_orch = temporal_sync×0.30 + vocab×0.25 + cui_bono×0.20 + historical×0.15 + suppress×0.10
```
<0.30 organic | 0.30-0.60 possible | 0.60-0.85 probable | >0.85 quasi-certain ⚑⚑⚑

**Red flags:** ⚑TEMPORAL_SYNC (<12h, ≥10 outlets) | ⚑VOCAB_IDENTICAL | ⚑CUI_BONO | ⚑SUPPRESSION | ⚑HISTORICAL

**Heuristics:** H6 Academic(🎓<2→+2-4◉) | H7 Adversary(🔥absent→+2-5src) | H8 Triangulation(≋detected→⊕⊗⊙) | H9 Cui Bono(ALWAYS→funding+COI)

---

## §6 ADVERSARY MEDIA MAP (H7)

**Trigger keywords:** election, government, war, conflict, military, sanctions, propaganda, disinformation, corruption, fraud, pharmaceutical, whistleblower, protest, surveillance, inequality

**Complexity override:** H7_triggered ∧ complexity<4.0 → force MEDIUM

**Media Map v3.0 (45+ sources):**
- **State:** RU:rt.com(C) sputnik(C) tass(B) | CN:globaltimes(C) xinhua(B) chinadaily(B) | IR:presstv(C) tasnim(C) | KP:kcna(D)
- **Independent:** US:intercept(A) propublica(A) grayzone(C) consortium(B) | FR:mediapart(A) disclose(A) bastamag(B) | UK:declassified(B) middleeasteye(B) bellingcat(A) | DE:nachdenkseiten(B)
- **Think tanks:** quincy(B) cato(B) cepr(B)
- **Whistleblower:** wikileaks(A) icij(A)
- **Global South:** BR:terra(B) uol(B) CartaCapital(B) | MX:proceso(B) animalpolitico(B) | AR:pagina12(C) lanacion(B) | IN:wire(B) scroll(B) hindu(B) | PK:dawn(B) | ZA:mail&guardian(B) dailymaverick(B) | NG:punch(B) | KE:nation(B) | QA:aljazeera(A)

**Query:** `site:{source} "{subject}" {keywords}` — MANDATORY: ≥1 adversary source. Not found → EDI -0.15.

**Validation targets:**
```yaml
MANDATORY: sources≥5, EDI≥0.50, ◈≥2, narratives≥2, geo≥2cont, lang≥30%non-EN
OPTIMAL:   sources 10-15, EDI≥0.65, ◈≥3, narratives≥3, divergences≥1
AUTO_FAIL: EDI<.35→MONOCULTURE | ◈=0→NO_PRIMARY | Only⟐→CONSENSUS | Same ownership→FAKE_DIVERSITY
```

**Output:** `[SOURCES] ◈:{X}◉:{Y}○:{Z} | EDI:{f}(raw:{r}pen:{p}[fl]) | geo:{g}lang:{l}% | ⟐:{A}⟐̅:{B}🌍:{C}🎓:{D}🔥:{E} | ≋:{d}⚑:{r} | COV:{c}IND:{i}CC:{cc}→EDI*:{e}`

---

_Version 2.0 — Source Pluralism & Narrative Cartography. Compressed._
