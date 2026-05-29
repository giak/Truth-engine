# SYMBOLS — Single Source of Truth for All Symbol Definitions

**Authority:** This is the ONLY file that defines symbols. KERNEL.md §0bis references this file.
**Version:** 1.0 (fusion of KERNEL §0bis A, KERNEL §2.10, COGNITIVE_DSL_CORE.md §1, COGNITIVE_DSL.md §1)

---

## §1 NARRATIVE SYMBOLS (15 — always scan)

| Symbol | Name | Concept | Techniques to Detect |
|--------|------|---------|---------------------|
| **Ξ** | Xi | Omission | cherry_picking, flooding_zone, factcheck_weaponized, astroturfing |
| **€** | Euro | Money | dark_money, hidden_flows, Cui_bono, regulatory_capture |
| **Λ** | Lambda | Framing | framing_cognitive, overton_window, talking_points, manufacture_consent |
| **Ω** | Omega | Inversion | accusatory_inversion, gaslighting, doublethink, reality_denial |
| **Ψ** | Psi | Sideration | strategy_tension, infodemia, doom_scrolling, learned_helplessness |
| **↕** | UpDown | Vertical | top_bottom_asymmetry, class_division, vertical_solidarity, elite_closure |
| **Φ** | Phi | Spectacle | society_spectacle, spectacularization, infotainment, virtue_signaling |
| **Σ** | Sigma | Semiotics | hyperreality, simulacre, greenwashing, sportswashing, wokewashing |
| **Κ** | Kappa | Cynical | mutual_knowledge_lies, facade_maintenance, institutional_cynicism |
| **ρ** | Rho | Resistance | counter_manipulation, cognitive_sovereignty, mental_disobedience |
| **κ** | Kappa_s | Subtle | nudge_theory, social_cooling, choice_architecture |
| **⫸** | Bundle | Aggregation | signal_convergence, information_cascade, narrative_synchronization |
| **⚔** | Warfare | Cognitive | coordination_detection, information_operations, psyops |
| **🌐** | Network | Analysis | elite_closure, institutional_endogamy, network_density |
| **⏰** | Temporal | Analysis | memory_hole, timeline_manipulation, orchestration_timing |

---

## §2 EPISTEMIC SYMBOLS (source stratification)

| Symbol | Name | Concept | Features |
|--------|------|---------|----------|
| **◈** | Primary | Raw evidence | Documents, leaks, court files, FOIA (confidence: 0.90-0.95) |
| **◉** | Secondary | Investigation | Investigative journalism, academic research (confidence: 0.75-0.85) |
| **○** | Tertiary | Mainstream | MSM, aggregators, opinion (confidence: 0.40-0.70) |
| **⊕** | Confirmed | Corroboration | ≥2 sources ◈ or ≥3 sources ◉ concordant |
| **⊗** | Contradicted | Refutation | ≥2 sources ◈ contradict, pattern violations |
| **⊙** | Partial | Mixed | Some elements confirmed, others contested |
| **≋** | Divergence | Contradiction | Narratives fundamentally contradict (≋+/++/+++) |
| **⟐** | Official | Narrative | Government/institutional version (typically ○) |
| **⟐̅** | Counter | Narrative | Counter-hegemonic, opposes power (often ◈) |
| **🌍** | Regional | Perspective | Local/neighbor viewpoints, escape Western bias |
| **🎓** | Academic | Perspective | Scholarly nuanced analysis |
| **🔥** | Dissident | Perspective | Censored/suppressed voices, deplatformed |
| **✦** | Hard fact | Quality | Documented ◈ + corroboration ⊕ |
| **✧** | Soft fact | Quality | Testimony ◉, contextually coherent |
| **⁕** | Claim | Quality | Unverified assertion, single source |
| **⁂** | Speculation | Quality | Explicit hypothesis, logical inference |
| **⚑** | Orchestration | Red flag | Temporal sync <12h, vocab identical, cui bono, suppression |

---

## §3 FACTUAL SYMBOLS

| Symbol | Name | Concept |
|--------|------|---------|
| **V** | Verifiability | Fact check — source quality, evidence chains |
| **C** | Coherence | Logic — contradictions, consistency |
| **S** | Sources | Diversity — OFF/IND/ALT/ACAD/TERR types |
| **T** | Temporality | Timeline — sequence, causality verification |
| **M** | Memory | History — precedents, pattern recognition |
| **E** | Economic | Financial — COI, funding analysis |
| **A** | Actors | Players — influence mapping, power analysis |
| **♦** | Biographical | Archaeology — hidden_networks, elite_reproduction, influence_mapping |

---

## §4 CLUSTER THRESHOLDS

| Primitive | Threshold | Cluster File | Mandatory |
|-----------|-----------|--------------|-----------|
| Ξ (Iceberg) | ≥3 | kb/patterns/CLUSTER_ICEBERG.md | YES (lower) |
| € (Money) | ≥3 | kb/patterns/CLUSTER_MONEY.md | YES (lower) |
| Λ (Framing) | ≥4 | kb/patterns/CLUSTER_FRAMING.md | YES (lower) |
| Ω (Inversion) | ≥4 | kb/patterns/CLUSTER_INVERSION.md | YES (lower) |
| Ψ (Overload) | ≥4 | kb/patterns/CLUSTER_OVERLOAD.md | YES (lower) |
| ↕ (Vertical) | ≥4 | kb/patterns/CLUSTER_TEMPORAL_VERTICAL.md | YES (lower) |
| ⏰ (Temporal) | ≥5 | kb/patterns/CLUSTER_TEMPORAL_VERTICAL.md | |
| ⚔ (Warfare) | ≥5 | kb/patterns/CLUSTER_WAR.md | |
| 🌐 (Network) | ≥5 | kb/patterns/CLUSTER_NETWORK.md | |
| ♦ (Biographical) | ≥5 | kb/patterns/CLUSTER_BIO.md | |
| Φ (Spectacle) | ≥5 | kb/patterns/CLUSTER_SPECTACLE.md | |
| Σ (Semiotics) | ≥5 | kb/patterns/CLUSTER_FRAGMENTATION.md | |
| Κ (Cynical) | ≥5 | kb/patterns/CLUSTER_GASLIGHTING.md | |
| ρ (Resistance) | ≥5 | kb/patterns/CLUSTER_RESISTANCE.md | |
| κ (Subtle) | ≥5 | kb/patterns/CLUSTER_CONFIRMATION.md | |

**LOAD RULES:**
- Score ≥5 → LOAD CLUSTER_*.md (mandatory)
- Score 3-4 → OUTPUT "{pattern}_NOTE: partial detected"
- Score <3 → NOTE_ONLY (1 line)
- **Mandatory (lower):** Ξ≥3, €≥3, Λ≥4, Ω≥4, Ψ≥4, ↕≥4 → LOAD even below ≥5

**IF score ≥ 7 (HIGH) — LOAD ADDITIONAL:**
- Ξ → kb/patterns/CLUSTER_GASLIGHTING.md
- € → kb/patterns/CLUSTER_NETWORK.md + CLUSTER_POWER.md
- Ω → kb/patterns/CLUSTER_CONFIRMATION.md

---

## §5 SYMBOL → ACTION MAP

### Ξ ICEBERG [score]
- **3-4:** NOTE "partial omission" → +1 query hidden data
- **5-6:** BRANCH "Hidden reality" → FORENSIC_REASONING + 2 queries
- **7-8:** DEEP_DIVE "Systematic omission" → ICEBERG_MAX + 3 queries + shadow multiplier
- **9-10:** EXPOSE "Major cover-up" → maximum resources + primary sources mandatory

### € MONEY [score]
- **3-4:** NOTE "financial element" → +1 query money trail
- **5-6:** BRANCH "Financial flows" → trace money + shell companies + 2 queries
- **7-8:** DEEP_DIVE "Dark money" → CLUSTER_MONEY + CLUSTER_NETWORK + 3 queries
- **9-10:** EXPOSE "Systemic corruption" → SEC + court docs + leaked data

### Λ FRAMING [score]
- **3-4:** NOTE "frame imposed" → +1 query alternatives
- **5-6:** BRANCH "Frame deconstruction" → CLUSTER_FRAMING + 2 queries
- **7-8:** DEEP_DIVE "Manufactured consent" → overton window analysis + 3 queries
- **9-10:** EXPOSE "Total reality control" → all framing layers exposed

### Ω INVERSION [score]
- **3-4:** NOTE "inversion detected" → document contradiction
- **5-6:** BRANCH "Reality check" → CLUSTER_INVERSION + 2 queries
- **7-8:** DEEP_DIVE "Systematic gaslighting" → DARVO + timeline + 3 queries
- **9-10:** EXPOSE "Reality completely inverted" → counter-evidence mandatory

### Ψ SIDERATION [score]
- **3-4:** NOTE "emotional saturation" → document technique
- **5-6:** BRANCH "Overload analysis" → CLUSTER_OVERLOAD + 2 queries
- **7-8:** DEEP_DIVE "Learned helplessness" → doom scrolling + 3 queries
- **9-10:** EXPOSE "Population paralysis" → resistance mechanisms identified

### ↕ VERTICAL [score]
- **3-4:** NOTE "power asymmetry" → document hierarchy
- **5-6:** BRANCH "Stratification analysis" → CLUSTER_TEMPORAL_VERTICAL + 2 queries
- **7-8:** DEEP_DIVE "Elite closure" → top/bottom analysis + 3 queries
- **9-10:** EXPOSE "Caste system" → structural inequality mapped

### Φ SPECTACLE [score]
- **3-4:** NOTE "distraction detected" → document theater
- **5-6:** BRANCH "Behind curtain" → CLUSTER_SPECTACLE + 2 queries
- **7-8:** DEEP_DIVE "Total theater" → ignore drama, focus structure + 3 queries
- **9-10:** EXPOSE "Reality completely obscured" → leaked/hidden truth only

### Σ SEMIOTICS [score]
- **3-4:** NOTE "symbol hijacking" → document manipulation
- **5-6:** BRANCH "Semiotic analysis" → CLUSTER_FRAGMENTATION + 2 queries
- **7-8:** DEEP_DIVE "Hyperreality" → simulacre + greenwashing + 3 queries
- **9-10:** EXPOSE "Complete reality replacement" → authentic vs performed

### Κ CYNICAL [score]
- **3-4:** NOTE "facade detected" → document gap
- **5-6:** BRANCH "Institutional analysis" → CLUSTER_GASLIGHTING + 2 queries
- **7-8:** DEEP_DIVE "Mutual knowledge lies" → everyone knows, nobody acts + 3 queries
- **9-10:** EXPOSE "Total institutional corruption" → systematic facade

### ρ RESISTANCE [score]
- **3-4:** NOTE "opposition detected" → document resistance
- **5-6:** BRANCH "Resistance mapping" → CLUSTER_RESISTANCE + 2 queries
- **7-8:** DEEP_DIVE "Counter-power" → effectiveness analysis + 3 queries
- **9-10:** EXPOSE "Revolutionary conditions" → system delegitimized

### κ SUBTLE [score]
- **3-4:** NOTE "nudging detected" → document technique
- **5-6:** BRANCH "Choice architecture" → CLUSTER_CONFIRMATION + 2 queries
- **7-8:** DEEP_DIVE "Social cooling" → surveillance effects + 3 queries
- **9-10:** EXPOSE "Complete behavioral control" → freedom eroded

### ⫸ BUNDLE [score]
- **3-4:** NOTE "signal convergence" → document patterns
- **5-6:** BRANCH "Cascade analysis" → information cascade + 2 queries
- **7-8:** DEEP_DIVE "Narrative synchronization" → multi-actor coordination + 3 queries
- **9-10:** EXPOSE "Total narrative control" → all signals aligned

### ⚔ WARFARE [score]
- **3-4:** NOTE "coordination detected" → document pattern
- **5-6:** BRANCH "Warfare analysis" → CLUSTER_WAR + 2 queries
- **7-8:** DEEP_DIVE "Psyops" → sophistication + attribution + 3 queries
- **9-10:** EXPOSE "Information war" → state-level operations identified

### 🌐 NETWORK [score]
- **3-4:** NOTE "network closure" → document connections
- **5-6:** BRANCH "Network mapping" → CLUSTER_NETWORK + 2 queries
- **7-8:** DEEP_DIVE "Power topology" → gatekeepers + influence + 3 queries
- **9-10:** EXPOSE "Total oligarchy" → complete network mapped

### ⏰ TEMPORAL [score]
- **3-4:** NOTE "timing pattern" → document in timeline
- **5-6:** BRANCH "Timing forensics" → calculate P_random + check orchestration
- **7-8:** DEEP_DIVE "Orchestration" → TEMP_ENGINE_V4 full calculation + 3 queries
- **9-10:** EXPOSE "Confirmed orchestration" → name orchestrators + trace decisions

---

## §6 CLAMPS (maximum scores)

```
Ψ ≤ 4.5 | Ω ≤ 4.0 | Σ ≤ 3.5 | Λ ≤ 4.8 | ⫸ ≤ 4.0 | ⚔ ≤ 5.0 | 🌐 ≤ 5.0 | ⏰ ≤ 5.0
```

---

## §7 RESONANCE (symbol interactions)

```
Ψ ≈ Ω: fear + inversion → amplified
Λ ≈ Σ: framing + semiotics → coordinated
€ ≈ ♦: money + power → elite_network
Ξ ≈ ⏰: omission + temporal → orchestrated hiding
⚔ ≈ 🌐: warfare + network → coordinated influence
```

---

_Version 1.0 — Single source of truth for all symbol definitions_
_Referenced by: KERNEL.md §0bis, COGNITIVE_DSL_CORE.md, COGNITIVE_DSL.md_
