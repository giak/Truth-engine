# THREATS — All @THR[] Definitions with Scoring

**Version:** 2.0

---

## §1 CLASSIC THREATS

| Threat | Detection | Signature | Countermeasure |
|--------|-----------|-----------|----------------|
| @THR[SHOCK] **SHOCK** | Ψ>4.5 ∧ τ<48h ∧ Λ_monopoly | trauma → urgency → solution | prebunk + timeline + liberties_track |
| @THR[BIDERMAN] **BIDERMAN** | ≥4/8 coercion techniques | isolation + monopoly + exhaustion + threats | exposure + diversity + cooldown |
| @THR[GASLIGHT] **GASLIGHT_SOC** | Ω>4 ∧ C<2 ∧ contra>3 | denial + contradiction + pathologize + memory_erasure | archive + compare + timeline |
| @THR[INFODEMIC] **INFODEMIC** | (vol×speed×contra)/capacity > 8 | volume > 150/day + acceleration + contradictions | simplify + cooldown + focus |
| @THR[DARK_MONEY] **DARK_MONEY** | €≥2 ∧ opacity≥3 ∧ COI≥5 | hidden_funding → policy_capture | transparency + ownership + trace |
| @THR[REG_CAPTURE] **REGULATORY_CAPTURE** | € ∧ revolving_door ∧ dependency | industry → regulator → industry | independence + term_limits + disclosure |
| @THR[MYTHO] **MYTHOLOGIZATION** | ♦≥2 ∧ narrative_gap≥3 ∧ media_complicity | self_made_myth → meritocracy_illusion | biography_archaeology |
| @THR[NUDGE] **NUDGING** | defaults[90%] ∧ dark_patterns | choice_architecture → behavior_control | friction + awareness + defaults_reset |
| @THR[CIALDINI] **CIALDINI_7** | ≥3/7 triggers active | reciprocity + commitment + social_proof + authority + liking + scarcity + unity | exposure + cooling_period |
| @THR[ASTRO] **ASTROTURFING** | growth_too_rapid ∧ funding_opaque ∧ message_polished | fake_grassroots → manufactured_consent | funding_trace + growth_analysis |

**Biderman 8 techniques:** 1_Isolation, 2_Perceptual_monopoly, 3_Exhaustion, 4_Threats, 5_Indulgences, 6_Omnipotence, 7_Degradation, 8_Absurd

---

## §2 FINANCIAL CONTROL

| Threat | Detection | Mechanism | Countermeasure |
|--------|-----------|-----------|----------------|
| @THR[DARK_MONEY] **DARK_MONEY** | €≥2 ∧ opacity≥3 | hidden_funding → policy_capture | transparency + beneficial_ownership |
| @THR[REG_CAPTURE] **REGULATORY_CAPTURE** | revolving_door ∧ dependency | industry → regulator → industry | independence + disclosure |
| @THR[ECON_HITMAN] **ECONOMIC_HITMAN** | debt_trap ∧ resource_extraction | IMF/WorldBank conditionality | sovereignty + alternative_finance |
| @THR[PHILANTHROCAP] **PHILANTHROCAPITALISM** | charity_mask ∧ power_accumulation | Gates/Soros model | democratic_oversight + tax_justice |

---

## §3 BIOGRAPHICAL MANIPULATION

| Threat | Detection | Mechanism | Countermeasure |
|--------|-----------|-----------|----------------|
| @THR[MYTHO] **MYTHOLOGIZATION** | ♦≥2 ∧ narrative_gap≥3 | self_made_myth → meritocracy_illusion | biography_archaeology |
| @THR[ELITE_REPRO] **ELITE_REPRODUCTION** | ♦ ∧ class_continuity | generational_power → false_meritocracy | transparency + class_analysis |
| @THR[NARR_LAUNDER] **NARRATIVE_LAUNDERING** | ♦ ∧ media_construction | reputation_whitewash → legitimacy | memory_preservation |
| @THR[POWER_PROX] **POWER_PROXIMITY** | ♦≥2 ∧ access_hidden | invisible_influence → democratic_bypass | influence_mapping |

---

## §4 PSYCHOLOGICAL TECHNIQUES

| Technique | Mechanisms | Detection |
|-----------|------------|-----------|
| **NUDGING** | defaults[90%], social_proof, framing, anchoring | Dark patterns: friction, confusion, shame |
| **CIALDINI_7** | reciprocity, commitment, social_proof, authority, liking, scarcity, unity | Artificial triggers, excessive use |
| **NLP** | Milton_model, emotional_anchoring, reframing | Too perfect phrasing |
| **EMOTIONAL** | Fear→Relief→Gratitude→Compliance | Sequence patterns |
| **DIGITAL_DARK** | roach_motel, privacy_zuckering, confirmshaming, FOMO, infinite_scroll | UX asymmetry |

---

## §5 SURVEILLANCE & CONTROL

| Method | Objective | Markers |
|--------|-----------|---------|
| **HONEYPOTS** | Entrap dissidents | too_good_true, zero_repression, escalation_encouraged |
| **CONTROLLED_OPPOSITION** | Channel anger safely | never_repressed, suspect_funding, attacks_true_dissidents |
| **ASTROTURFING** | Fake grassroots | opaque_funding, growth_too_rapid, immediate_media_embrace |
| **PREDICTIVE_SURV** | Pre-crime | biometric + behavioral + social → violence_prob |
| **SOCIAL_CREDIT** | Behavior control | score → rewards/punishments |
| **COG_INFILTRATION** | Forum disruption | consensus_cracking, topic_dilution, forum_sliding |

---

## §6 HYBRID WARFARE

| Domain | Techniques | Characteristics |
|--------|------------|-----------------|
| **HYBRID** | kinetic, cyber, economic, info, legal, diplomatic | plausible_deniability, gray_zone |
| **COLOR_REV** | Regime change template | NGO → trigger → protests → pro-West installed |
| **OVERTON** | Normalize unthinkable | unthinkable → radical → acceptable → sensible → popular → policy |

---

## §7 SCORING FORMULAS

```python
COERCION_SCORE = Σ(Biderman[1-8]) / 8 × context_amplification  # >0.7 → active
SHOCK_SIGNATURE = (Ψ_spike > 4.5) ∧ (τ < 48h) ∧ (Λ_monopoly)  # Freedom_lost = -0.5/cycle
GASLIGHT_INDEX = (Ω × inversion) + (C × 2) + M_erasure  # >6 → reality_inverted
STOCKHOLM_SCORE = (Ψ × Ξ) / (alternatives + 1)  # >5 → defend_oppressors
INFODEMIC_SCORE = (volume × velocity × contradictions) / cognitive_capacity  # >10 → collapse

TOTAL_WAR = Hybrid×0.15 + FalseFlags×0.15 + Financial×0.15 + Bio×0.15 + Weather×0.10 + ColorRev×0.10 + Overton×0.10 + SixthGen×0.10
SOCIAL_CONTROL = Honeypot×0.15 + Astroturf×0.15 + Opposition×0.20 + Surveillance×0.20 + Dependency×0.15 + CogInfiltration×0.15
PSYMANIP = Nudges×0.15 + Cialdini×0.20 + NLP×0.15 + Emotional×0.20 + Addiction×0.15 + CogWar×0.15
```

**Thresholds:** >5.0 = active | >7.0 = established | >9.0 = total

---

## §8 FOUNDATIONAL EXPERIMENTS

**MILGRAM_1961:** 65% obey fatal order | Authority + Ψ → moral suspension
**ASCH_1951:** 75% deny evidence of eyes | Λ + group_pressure → reality denial
**STANFORD_1971:** role → extreme behavior in 6 days | Coercive context → dehumanization

---

## §9 COGNITIVE RESISTANCE

**Resistance Score:** (lucidity + autonomy + memory_integrity + courage) / 4
- lucidity = 1 / (1 + Ψ_susceptibility)
- autonomy = 1 / (1 + Λ_influence)
- memory_integrity = M_retention × M_accuracy
- courage = dissent_willingness / social_pressure

**Classifications:** >0.8 Resister (5%) | 0.6-0.8 Strong (15%) | 0.4-0.6 Moderate (30%) | 0.2-0.4 Vulnerable (35%) | <0.2 Susceptible (15%)

**Cognitive Firewall:** Auto-skepticism for Ψ>4.0 | Source diversity (min 3 types) | Temporal cooling
**Emergency:** [emotional_spike, artificial_urgency, single_source, social_pressure] → PAUSE, QUESTION, DIVERSIFY, DELAY

---

## §10 KEY AUTHORS → CONCEPTS

Debord[spectacle], Baudrillard[simulacre], Klein[shock], Biderman[coercion], Chomsky[manufacture_consent], Bernays[PR], Milgram[obedience], Asch[conformity], Kahneman[cognitive_bias], Zuboff[surveillance_capitalism], Foucault[panoptique], Perkins[economic_hitman], Mayer[dark_money], Stiglitz[regulatory_capture], Bourdieu[social_capital], Mills[power_elite]

---

_Version 2.0 — All threat definitions with scoring_
_Referenced by: KERNEL.md §0bis, clusters/*.md_
