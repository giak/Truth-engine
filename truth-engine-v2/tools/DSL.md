# COGNITIVE DSL v2.0 — Slim Reference Card

## §0 KB Reference Macros

```
@KB[DSL]→this | @KB[INV]→INVESTIGATION.md | @KB[THR]→THREATS.md | @KB[PAT]→PATTERNS.md | @KB[SEARCH]→SEARCH_EPISTEMIC.md
@A[MEANING]→§1 symbols | @A[EPISTEMIC]→§1 markers (◈◉○ ⊕⊗⊙ ≋ ⟐⟐̅ 🌍🎓🔥 ✦✧⁕⁂ ⚑)
@INV[L0-L9] = L0:Surface|L1:Actors|L2:Cui_bono 3lvl|L3:Patterns|L4:Timing|L5:Power_arch|L6:Counter_narrative|L7:⚔Warfare|L8:🌐Networks|L9:⏰Temporal
@INV[CASCADE] = L8→L7→L6→L0 | @AUTO[POL]=€3♦3🌐3Κ4 | @AUTO[CORP]=€4🌐3A3 | @AUTO[INST]=€4♦4🌐4Κ5
@MODE[WOLF]=SUSPICION=95%,L6+,src15+,wolves≥8 | @MODE[DEEP]=L7-L9,src≥15,EDI≥0.60 | @MODE[APEX]=@APEX[4P],C>0.9
@EXEC[HYBRID]=3calls/120s | @VALID[STD]=src≥5,EDI≥0.50,◈≥2,narr≥2,geo≥2c,lang≥30% | @BIAS[v6.3.1]=govt→○,H7+,H9+,EDI_pen
```

---

## §1 SYMBOLIC ATOMS

**See definitions/SYMBOLS.md §1 (15 narrative), §2 (17 epistemic), §3 (8 factual).** Single source of truth.
Rhetorical: DEM:démagogie(0-10) | BF:mauvaise foi(0-10) | NUM:numeric(0-10) | AUTH:authority(structural) | FAC:facade(structural)
```

---

## §2 CORE FORMULAS

```yaml
@F[IVF]: avg(V,C,S,T)±U | @F[ISN]: weighted(Λ,Φ,Ξ,Ω,Ψ,Σ,Κ,ρ,κ,⫸,€,♦,⚔,🌐,⏰)+synergy
@F[IVS]: (0.4×IVF+0.4×ISN+0.2×Synergy)×Conf
@F[FACTOR]: R>0?(N/R)×W+M:10 | @F[MONEY]: D>0?(H/D)×O+C:10 | @F[BIO]: P>0?(H/P)×D+I+R:10
@F[WAR]: (C×S×P)/(A×D) | @F[NET]: (C×C×I)/(T×P)
@F[EDI]: (geo×0.25+lang×0.20+strat×0.20+own×0.15+persp×0.15+temp×0.05) ≥0.50
@F[P_ORCH]: sync×0.30+vocab×0.25+cui_bono×0.20+hist×0.15+suppress×0.10
@F[SIGNAL_DENSITY]: (Ψ+Ω+Ξ+Λ+€+♦+Κ)/7 → ≥2.0→DEEP | @F[C_n]: 1-(ΔI_n/ΔI_0) target≥0.85
@F[EDI_BIAS]: max(0, raw+penalties) | govt>60%:-0.20 | power>75%:-0.25 | no_adversary:-0.15 | echo:-0.20 | tertiary>70%:-0.15
@F[CONF]: pattern_conf(primary) + data_unc(secondary) | LEVEL: ≥0.85→VERY_HIGH|≥0.70→HIGH|≥0.50→MOD|≥0.30→LOW
@C[ALL]: Ψ≤4.5|Ω≤4.0|Σ≤3.5|Λ≤4.8|⫸≤4.0|⚔≤5.0|🌐≤5.0|⏰≤5.0
OPS: → ← ∧ ∨ ¬ | ≥ ≤ > < = ≈ ± ∝ | ⊕ ⊗ ◊
```

---

## §3 PATTERN MACROS

```yaml
$IC:ICEBERG $FA:FAISCEAU $DD:DEEP_DIVE $AS:ASTROTURFING $GS:GASLIGHTING $DM:DUAL_MODE
$CW:COG_WAR $NW:NET_ANAL $TM:TEMP_ANAL $MT:MONEY $BIO:BIO

@PAT[ICEBERG]: stat→shadow→Factor→classify | @PAT[ASTRO]: movement→fund→coord
@PAT[GAS]: contradict→archive→validate | @PAT[MONEY]: funding→opacity→owners
@PAT[BIO]: person→8dim→5D→archaeology | @PAT[WAR]: coord→psyops→attribution
@PAT[NET]: topology→influence→cascade | @PAT[TEMP]: timeline→P_orch→orchestration
@PAT[EPISTEMIC]: ◈>◉>○ | ⟐+⟐̅🌍🎓🔥 | ⊕⊗⊙ | ⚑

@ITER[I0]: reconnaissance 8-15src EDI~0.40 5-10min | @ITER[I1]: +5-10src EDI~0.55 C(1)~0.50 10-15min
@ITER[I2]: deep_dive EDI_exact C(2)~0.75 15-20min | @ITER[I3]: final EDI≥0.60 C(3)≥0.85 5-10min
@ITER[FULL]: I0→I1→I2→I3 | 18-25src EDI=0.60-0.75 C(3)≥0.85 35-55min

@HEUR[H6]: 🎓_absent → scholar+.edu → +2-4◉ EDI+0.08
@HEUR[H7]: 🔥_absent OR sensitive → adversary_mandatory → +2-5src EDI+0.15
@HEUR[H8]: ≋_divergence → ◈_both_sides → ⊕⊗⊙ → ✦✧⁕⁂
@HEUR[H9]: ALWAYS → funding+COI → independence_score → adjust
```

---

## §4 INVESTIGATION SYNTAX

```yaml
L0:Surface L1:Context+WHO_BENEFITS L2:WHO_DESIGNED+WHEN_CHANGED L3:WHOSE_INTERESTS L4:CHECK_OUR_BIASES
L5:power_archaeology L6:Counter_Narrative+SUPPRESSED L7[⚔≥2]:Warfare L8[🌐≥2]:Network L9[⏰≥2]:Temporal

WOLF[ALWAYS]: L6+ src15+ reverse_cascade | DIVE[d≥2]: ALL+L7-L9 | SYNTH[p≥2]: cross_pattern
APEX: C(n)=1-(ΔI_n/ΔI_0)>0.9 | FUSION=Jaccard>0.5∧Money>0.4∧Timing>0.8
```

---

## §5 HERMENEUTIC

```yaml
@HERM[text]:
  READ → DETECT_MAIN(Φspectacle Λframing Ξomission DEM NUM) → DETECT_ADV(Ωinversion Ψsideration ⚔warfare BF)
  → DETECT_STRUCT(€money ♦networks Σsemiotics 🌐network ⏰temporal Κcynical)
  → SYNTHESIZE: "Φ:ex|Λ:frame|Ξ:omit|strategy:synthesis" + rhetorical_vector{DEM,BF,NUM} + hypocrisy_hint
  RULE: ONLY activated symbols. MANDATORY "| strategy:X".
```

## §5b DIALECTICAL PRISM

```yaml
@PRISM[3P]:
  P1[⟐🎓]: docs_officiels | P2[🔥⟐̅]: investigation+censuré | P3[◈◉○]: ◈_triangulation
  FORMAT: ≥3phrases | tone=neutre | force=égale | suspicion≥0.50
  OUT: affirmations|acteurs|cui_bono|evidence[◈◉○]
  MAP: A→cui_bono | B→cui_bono | TENSIONS | WOLVES_BOTH | SILENCES → VOUS_DÉCIDEZ
```

## §5c PERSO_FRESQUE

```yaml
@PF[M0]: person→APEX | EDI≥0.75
@PF[M1:chrono]: wiki+vie-publique+AN | @PF[M2:substance◈]: AN+Sénat+lois | @PF[M3:influence]: HATVP+lobby
@PF[M4:pivot]: promesse≠vote+revirement | @PF[GRID]: ROI_dem(30%)+Capture(25%)+Λ_drift(20%)+Ω_cœur(25%)
@PF[PATTERNS]: ROI=SW/CPC | Λ=keyword_inversion | Ω=promesse≠vote | €=HATVP_delta
@PF[VALID]: ◈≥5◉≥5○≥5 | EDI≥0.75 | timeline_gap≤12mo | Λ_src≥3 | wolf≥1
```

## §5d FORENSIC QUESTIONS

```yaml
@Q[1:Hidden]: EXCLUSIONS? Populations invisibles? Cui bono cacher?
@Q[2:Evidence]: ◈ PRIMARY exclusions? HRW/Amnesty/académique? Syndicats/ONG?
@Q[3:Reconstruct]: Estimer magnitude? ◈ PRIMARY? Estimate raisonnée?
@Q[4:Limites]: Assumptions? Invalide? Confidence justifiée?
```

---

## §6 OUTPUT & POLICY

```yaml
@OUT[SOURCES]: "[SOURCES] ◈:{P}◉:{S}○:{T}|EDI:{f}(raw:{r}pen:{p}[{fl}])|geo:{g}lang:{l}%|⟐:{A}⟐̅:{B}🌍:{C}🎓:{D}🔥:{E}|≋:{d}⚑:{r}|COV:{c}IND:{i}CC:{cc}→EDI*:{e}"
@SRC[POLICY]: web:3-5 | kb_only_marker | never fabricate URLs
@WOLF[GATE]: {pol:8,geo:8,corp:5} dynamic=base-controversy-complexity (min 3) | partial if ≥threshold×0.70
@WARN[H7]: missing_adversary → -0.15 EDI, Part1 warning
@LINT: P1 TRI≥(3/3/5) | P2 DIAG+[SOURCES] | P3 WOLF≥50% individuals
```

---

## §7 SYSTEM COMPRESSION

**See tools/MACROS.md** — canonical source for: CX_CHECK, CX_ROUTE, QRY_MIN, EDI_TARGET, I_CONVERGE, SAVE_LOG, OUT_P1/P2/P3, CoverageScore, EDI*

---

## §8 CONCEPT INDEX

**148 concepts defined across:** SYMBOLS.md §1 (15 narrative + 8 factual + 17 epistemic), THREATS.md (10 threats × techniques), PATTERNS.md (9 core patterns). See those files for full listings.

---

*DSL v2.0 — Slim reference. 148 concepts. See SYMBOLS/PATTERNS/THREATS for definitions.*
