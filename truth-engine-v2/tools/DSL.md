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

### Narrative [0-5] + PFD

| Sym | Name | Concept |
|-----|------|---------|
| **Ξ** | Omission | cherry_picking, flooding_zone, factcheck_weaponized, astroturfing |
| **€** | Money | dark_money, hidden_flows, Cui_bono, regulatory_capture |
| **Λ** | Framing | framing_cognitive, overton_window, talking_points, manufacture_consent |
| **Ω** | Inversion | accusatory_inversion, gaslighting, doublethink, reality_denial |
| **Ψ** | Sideration | strategy_tension, infodemia, doom_scrolling, learned_helplessness |
| **↕** | Vertical | top_bottom_asymmetry, class_division, elite_closure |
| **Φ** | Spectacle | society_spectacle, spectacularization, infotainment, virtue_signaling |
| **Σ** | Semiotics | hyperreality, simulacre, greenwashing, sportswashing, wokewashing |
| **Κ** | Cynical | mutual_knowledge_lies, facade_maintenance, institutional_cynicism |
| **ρ** | Resistance | counter_manipulation, cognitive_sovereignty, mental_disobedience |
| **κ** | Subtle | nudge_theory, social_cooling, choice_architecture |
| **⫸** | Bundle | signal_convergence, information_cascade, narrative_synchronization |
| **⚔** | Warfare | coordination_detection, information_operations, psyops |
| **🌐** | Network | elite_closure, institutional_endogamy, network_density |
| **⏰** | Temporal | memory_hole, timeline_manipulation, orchestration_timing |

### Factual + Meta

| Sym | Name | Concept |
|-----|------|---------|
| **V** | Verifiability | Source quality, evidence chains |
| **C** | Coherence | Contradictions, consistency |
| **S** | Sources | OFF/IND/ALT/ACAD/TERR types |
| **T** | Temporality | Sequence, causality verification |
| **M** | Memory | Precedents, pattern recognition |
| **E** | Economic | COI, funding analysis |
| **A** | Actors | Influence mapping, power analysis |
| **♦** | Biographical | hidden_networks, elite_reproduction, power_archaeology |

### Epistemic (v6.2)

| Sym | Name | Conf |
|-----|------|------|
| **◈** | Primary — docs, leaks, FOIA | 0.90–0.95 |
| **◉** | Secondary — investigative, academic | 0.75–0.85 |
| **○** | Tertiary — MSM, aggregators | 0.40–0.70 |
| **⊕⊗⊙** | Corroboration — confirmed/contradicted/partial | |
| **≋** | Divergence — ≋+/++/+++ | |
| **⟐⟐̅** | Narratives — official/counter | |
| **🌍🎓🔥** | Perspectives — regional/academic/dissident | |
| **✦✧⁕⁂** | Fact quality — hard/soft/claim/speculation | |
| **⚑** | Orchestration — red flags | |

### Rhetorical Families

```
DEM: démagogie(0-10) | BF: mauvaise foi(0-10) | NUM: numeric/linguistic(0-10) | AUTH: authority(structural) | FAC: facade(structural)
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

```
→OK[m]→STATUS:**m**✅ | →FAIL[m]→STATUS:**m**❌ | →MCP_FAIL[cx] IF cx∈{COMPLEX,APEX}:FAIL
@CX[level]=complexity∈{level} | @CX_ROUTE[S,M,C,A] | @QRY_MIN=@CX_MIN[5,8,12,15]
@VAL_EDI=@CX_MIN[0.30,0.50,0.70,0.80] | @CONV[s] s≥0.85:COMPLETE s≥0.75:OK ELSE:CONTINUE
@SAVE[slug]=logs/$(date)_{slug}.md → Write → Confirm | Compression: 8:1 avg
```

---

## §8 CONCEPT INDEX — 148 Concepts

**Ψ Sideration [13]**: strategy_tension, infodemia, doom_scrolling, learned_helplessness, acceleration_cognitive, decision_fatigue, cognitive_overload, analysis_paralysis, attention_capture, fear_mongering, trauma_exploitation, urgency_manufactured, time_pressure_artificial

**Ω Inversion [13]**: accusatory_inversion, gaslighting, doublethink, reality_denial, projection_accusatory, truth_inversion, victim_blaming, evidence_rejection, memory_revision, narrative_flip, contradiction_normalization, reality_distortion, cognitive_dissonance_induced

**Ξ Omission [13]**: cherry_picking, flooding_zone, factcheck_weaponized, astroturfing, omission_systematic, context_stripping, selective_reporting, inconvenient_truth_burial, memory_hole, deplatforming_strategic, censorship_algorithmic, shadow_banning, visibility_filtering

**Λ Framing [14]**: framing_cognitive, overton_window, talking_points, manufacture_consent, agenda_setting, priming_semantic, anchoring_cognitive, false_dichotomy, loaded_language, euphemism_treadmill, frame_hijacking, question_begging, narrative_control, debate_boundaries

**Φ Spectacle [10]**: society_spectacle, spectacularization, infotainment, virtue_signaling, theater_security, bread_circuses, distraction_industrial, outrage_porn, clickbait_economy, attention_economy

**Σ Semiotics [10]**: hyperreality, simulacre, greenwashing, sportswashing, wokewashing, pinkwashing, bluewashing, reputation_laundering, symbolic_appropriation, brand_activism_fake

**Κ Cynicism [5]**: mutual_knowledge_lies, facade_maintenance, institutional_cynicism, kayfabe_political, soljenitsyne_cynicism | **ρ Resistance [5]**: counter_manipulation, cognitive_sovereignty, mental_disobedience, resistance_proportional, critical_thinking_active | **κ Subtle [5]**: nudge_theory, social_cooling, choice_architecture, invisible_manipulation, dark_patterns

**⫸ Bundle [5]** | **⚔ Warfare [5]** | **🌐 Network [5]** | **⏰ Temporal [5]** | **€ Money [5]** | **♦ Bio [5]** | **Threats [30]**: shock_doctrine, biderman_coercion, societal_gaslighting, infodemic, lawfare, false_flags, divide_et_impera, surveillance_capitalism + financial[5] + bio_manip[4] + AI_surveillance[8] + experiments[5]

**Total: 148** — Ψ:13 Ω:13 Ξ:13 Λ:14 Φ:10 Σ:10 Κ:5 ρ:5 κ:5 ⫸:5 ⚔:5 🌐:5 ⏰:5 €:5 ♦:5 Threats:30

---

*COGNITIVE DSL v2.0 — 148 Concepts — Complexité = Rébellion*
