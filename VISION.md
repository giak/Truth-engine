# Truth Engine Vision — Usage × Développement

**Brainstorm deep**: Utilisation + amélioration continue en parallèle

---

## 🧠 Insight Fondamental

Truth Engine n'est pas un **produit fini** mais un **système cognitif évolutif**.

**Paradoxe clé**: 
- Usage = génère feedback (EDI bas, patterns manquants, sources insuffisantes)
- Feedback = améliore système
- Système amélioré = meilleur usage
- **Loop auto-renforçant**

Avec Claude Code + MCP, cette loop devient **autonome**.

---

## 🔄 Dual-Track Architecture

### Track 1: USAGE (Investigations)

**Input**: Sujets à analyser (tweets, articles, claims)  
**Process**: Truth Engine protocol (system.md + KB)  
**Output**: 
- Partie 1 (Natural FR analysis)
- Partie 2 (Technical metrics EDI/ISN/patterns)
- Partie 3 (WOLF report si applicable)
- **Meta-output**: Logs → `logs/YYYY-MM-DD_subject.json`

### Track 2: DÉVELOPPEMENT (Meta-Analysis)

**Input**: Logs investigations (Track 1 outputs)  
**Process**: Pattern recognition sur échecs/succès  
**Output**: 
- KB improvements (add patterns, extend H7 map, fix formulas)
- System refinements (adjust thresholds, add heuristics)
- **Meta-meta-output**: `CHANGELOG.md` + reindex KB

---

## 💡 Concepts Clés

### 1. Self-Supervised Learning (sans ML)

**Principe**: Truth Engine s'améliore via ses propres investigations.

**Mécanisme**:
```
Investigation N → EDI=0.42 (FAIL) → Analyse cause:
  - H7 adversary manquant (Russia topic, no RT/TASS)
  - Pattern COORDINATION non détecté (temporal sync présent)
  
→ Fixes:
  - Extend kb/QUERY_TEMPLATES.md H7 map (add missing sources)
  - Add kb/PATTERNS.md COORDINATION detection rules
  
→ Reindex KB (MnemoLite)
  
Investigation N+1 (même type) → EDI=0.58 (PASS)
```

**Pas de dataset externe**. Pas de training. Juste: use → observe → fix → reuse.

### 2. MnemoLite comme "Mémoire Épisodique"

**Analogie cerveau**:
- KB = mémoire sémantique (concepts, formulas, patterns)
- Logs investigations = mémoire épisodique (expériences passées)
- MnemoLite = hippocampe (indexe + recall contextuel)

**Usage**:
```python
# Investigation similaire détectée
semantic_search("chômage 7.4%") → recall logs précédents
  → "Investigation 2025-10-15: même claim, EDI=0.48, gap: DEFM B-E manquants"
  
# Stratégie adaptative
if similar_past_investigation:
    pre_load_gaps_from_past()  # Évite répéter erreurs
    target_EDI = past_EDI + 0.10  # Progressive improvement
```

### 3. Adversarial Testing (Rouge Team)

**Insight**: Truth Engine détecte manipulation... mais peut-on **manipuler Truth Engine**?

**Test cases à créer**:
```markdown
# logs/adversarial/case_001_circular_corroboration.md

Attack: 5 sources MSM répètent même claim (circular corroboration)
Truth Engine response: Should detect "institutional family" → downgrade conf
Expected: ○ TERTIARY all sources, EDI penalty
Result: [À tester]

# logs/adversarial/case_002_iceberg_invisible.md

Attack: Stats manipulation sans P0/P1 obvious (subtle ICEBERG)
Truth Engine response: Should detect via DEFM analysis
Expected: ICEBERG pattern Factor≥2.0
Result: [À tester]
```

**Bénéfice**: Strengthen detection, identify blind spots.

### 4. Evolutionary KB (Genetic Algorithm Analogie)

**Mutation**: Modify KB rules (ex: EDI weights, H7 triggers)  
**Selection**: Measure performance (EDI avg, ISN avg, investigation success rate)  
**Fitness**: Keep changes if metrics improve, rollback si dégradent

**Exemple**:
```bash
# Test EDI weight change
git checkout -b experiment/edi-geo-boost
# Edit kb/SEARCH_EPISTEMIC.md: geo_diversity weight 0.25 → 0.30
# Run 10 investigations comparatives
# Measure: EDI_avg, geo_coverage_avg
# If improvement > 5% → merge. Else → discard branch.
```

**Workflow Git-based evolution** = version control improvements.

---

## 🚀 Workflows Concrets

### Workflow A: Investigation Simple (Quotidien)

```bash
# 1. User input
echo "Chômage France 7.4% T1 2025" > /tmp/query.txt

# 2. Claude Code autonomous
claude-code "
Load /home/giak/projects/truth-engine/system.md + kb/ (via MnemoLite semantic search).
Subject: $(cat /tmp/query.txt)

MCP tools:
- search_code(query='EDI formula') → recall KB
- context7 web search → 10-15 sources
- write_memory(title='Investigation chômage', content='...')

Execute Truth Engine protocol.
Save: logs/$(date +%Y-%m-%d)_chomage.json
"

# 3. Output structured JSON
cat logs/2025-11-07_chomage.json
# {
#   "subject": "Chômage 7.4%",
#   "edi": {"raw": 0.52, "final": 0.42, "penalties": [...]},
#   "sources": {"primary": 2, "secondary": 4, "tertiary": 6},
#   "patterns": ["ICEBERG"],
#   "wolves": 5,
#   "isn": 7.8,
#   "duration_sec": 180
# }
```

**Durée**: 3-5 min  
**Output**: Rapport FR + JSON metrics

---

### Workflow B: Batch Investigations (Nuit)

**Principe**: Investigate multiple sujets pendant sommeil, analyse batch matin.

```bash
# 1. Liste sujets (curated ou trending topics)
cat > subjects.txt << EOF
Chômage 7.4% France
PS trahisons classes populaires
Pfizer contrats secrets UE
Ukraine offensive Bakhmut
IA regulation Brussels
EOF

# 2. Cron job nuit (2h AM)
# crontab -e: 0 2 * * * /home/giak/projects/truth-engine/batch.sh

# batch.sh
while IFS= read -r subject; do
  claude-code "Investigate: $subject. Truth Engine protocol. Save logs/"
  sleep 300  # 5min entre investigations (rate limit respect)
done < subjects.txt

# 3. Morning analysis
claude-code "
Analyse batch logs/2025-11-07_*.json
Identify:
- EDI moyen, min, max
- Patterns fréquents
- Gaps communs (H7 missing? ◈ insufficient?)
Propose KB improvements.
"
```

**Durée batch**: 5 sujets × 5min = 25min (autonome)  
**Morning review**: 5min read synthesis

---

### Workflow C: Meta-Development (Hebdomadaire)

**Principe**: Analyse cumulative semaine → améliore KB structurellement.

```bash
# 1. Aggregate week logs
claude-code "
Analyse all logs/2025-11-*.json (7 jours)

Metrics:
- EDI moyen: calculate avg, stddev, trend
- Patterns détectés: frequency distribution
- H7 coverage: trigger rate, missing sources frequency
- Wolves mapping: success rate (≥8 political, ≥5 corporate)
- Investigation failures: EDI<0.35 OR sources<10

Identify top 3 systemic issues.
"

# 2. Generate improvement proposals
# Output: IMPROVEMENTS_WEEK_45.md
# Example output:
# Issue #1: H7 coverage 72% (target 90%)
#   → Missing: Venezuela (TeleSUR), Cuba (Granma), DPRK (KCNA)
#   → Action: Extend kb/QUERY_TEMPLATES.md H7 map +3 sources
#
# Issue #2: COORDINATION pattern detected 0% (12 cases obvious)
#   → Cause: Pattern definition trop strict (requires P_orch>0.80)
#   → Action: Lower threshold P_orch>0.65 + add heuristics
#
# Issue #3: EDI geo_diversity faible (0.28 avg, target 0.40)
#   → Cause: Query templates favorisent sources EN/FR
#   → Action: Add regional TLD queries (site:.ru, site:.cn, site:.br)

# 3. Apply improvements (human review + commit)
# Edit KB files
git add kb/QUERY_TEMPLATES.md kb/PATTERNS.md
git commit -m "Week 45 improvements: H7 +3, COORDINATION threshold, geo TLD"

# 4. Reindex KB
curl -X POST http://localhost:8001/api/v1/index/reindex \
  -d '{"repository": "truth-engine-kb"}'

# 5. Validate improvements (A/B test)
# Run 5 investigations pre-improvement vs post-improvement
# Compare EDI, H7 coverage, pattern detection rate

# 6. Document failures & rejected approaches (NEW in v8.4)
# If integration/feature tested and REJECTED, create postmortem:
#
# docs/postmortems/YYYY-MM-DD-feature-ABANDONED.md
# ├── Root cause analysis
# ├── Load test results (quantitative)
# ├── Decision rationale (why rejected)
# └── Lessons learned
#
# docs/memory/YYYY-MM-DD-feature-abandoned.md (concise version)
# └── Quick reference for future similar proposals
#
# Example: Google Search MCP (Nov 2025)
# - Load tested 25 queries → 0% success (anti-bot blocking)
# - Decision: Official APIs > Scraping (2025 reality)
# - Saved 8-10h dev time by testing BEFORE full integration
```

**Durée**: 1h/semaine (+ 30min for postmortems if applicable)
**Impact**: Continuous quality improvement + institutional memory of failures

---

## 🔬 Expérimentations Avancées

### Exp #1: Dual-LLM Architecture

**Hypothesis**: 2 LLMs = meilleur que 1 pour adversarial analysis.

**Setup**:
- LLM A (Claude Code): Execute investigation (current workflow)
- LLM B (Claude Desktop): **Red Team** attack investigation A
  - "Find biases in investigation A"
  - "Challenge EDI calculation"
  - "Identify missing adversary angles"
- LLM A: Respond to critiques, re-investigate if valid

**Expected**: EDI +0.10-0.15 via adversarial refinement.

**Implementation**:
```bash
# Investigation A
claude-code "Investigate X" → output_A.json

# Red Team B
claude-desktop "
Load output_A.json
Red Team mode: Find flaws (bias, gaps, circular logic).
Output: critique.md
"

# Re-investigation A (if critiques valid)
claude-code "
Load critique.md
Re-investigate X addressing critiques.
Target: EDI ≥ output_A.edi + 0.10
"
```

---

### Exp #2: Pattern Auto-Discovery

**Hypothesis**: LLM peut **détecter nouveaux patterns** non codés dans KB.

**Setup**:
```bash
# Analyse batch investigations
claude-code "
Analyse logs/2025-11-*.json (30 investigations)

Task: Unsupervised pattern discovery
- Cluster investigations par similarités (topics, sources, narratives)
- Identify recurring structures NOT in kb/PATTERNS.md
- Propose new pattern definitions (name, detection rules, examples)

Output: NEW_PATTERNS.md
"
```

**Exemple output attendu**:
```markdown
# NEW_PATTERNS.md

## Pattern: EXPERT_CAPTURE (nouveau)

**Definition**: Experts "indépendants" cités par MSM = funded by industry.

**Detection**:
- Expert quoted ≥3 sources MSM
- Expert affiliation = think tank OR university
- Funding check (H9): corporate ≥60%
- Narrative aligns with corporate interests

**Examples**:
- Climate debate: Expert X (MIT) quoted NYT/WSJ/FT → funding check: ExxonMobil, Shell
- Pharma: Expert Y (Hopkins) → funding: Pfizer, J&J

**Formula**:
P_capture = (expert_media_freq × 0.40) + (funding_corporate_pct × 0.40) + (narrative_alignment × 0.20)
If P_capture > 0.70 → EXPERT_CAPTURE detected

**Add to**: kb/PATTERNS.md
```

---

### Exp #3: Continuous Benchmark

**Hypothesis**: Mesurer Truth Engine performance = science, pas guessing.

**Setup**: Dataset test curated (gold standard).

```bash
# test_cases/
# ├── case_001_iceberg_obvious.json      # Expected: ICEBERG detected, Factor≥2.0
# ├── case_002_circular_corroboration.json # Expected: Penalty, EDI≤0.40
# ├── case_003_h7_adversary.json         # Expected: H7 triggered, adversary≥2
# └── ... (20 cases)

# Benchmark script
claude-code "
For each test_cases/*.json:
  1. Run investigation
  2. Compare output vs expected
  3. Calculate accuracy:
     - Pattern detection: precision, recall
     - EDI: MAE (mean absolute error)
     - H7 coverage: trigger accuracy

Output: benchmark_results.json
{
  'pattern_detection': {'precision': 0.92, 'recall': 0.85},
  'edi_mae': 0.08,
  'h7_accuracy': 0.88,
  'overall_score': 0.88
}
"

# Track benchmark over time (regression detection)
git commit benchmark_results.json -m "Benchmark week 45: overall 0.88"
```

**Bénéfice**: Detect regressions après KB changes. Validate improvements quantitatively.

---

## ✅ Completed Features

### v8.3 — Query Optimization (Nov 15, 2025)

**Problem**: Complex queries (>5 keywords) often return empty results or miss PRIMARY sources.

**Solution**:
- Automatic query splitting: >5 keywords → 2-3 simple queries (3-4 keywords each)
- Hybrid fallback: MCP (DuckDuckGo) first, WebSearch (Google) fallback if needed
- Aggregate and deduplicate results across all queries

**Impact**:
- Productive query rate: 0-40% baseline → 80-100% with optimization
- PRIMARY source (◈) discovery: +105% (official docs, government sites)
- EDI improvement: +0.15-0.27 typical boost
- Backward compatible: Simple queries (<5 keywords) unchanged

**Validation**: [tests/query_optimization/](tests/query_optimization/) (17 test files, comprehensive audit)

**Documentation**: [kb/QUERY_OPTIMIZATION.md](kb/QUERY_OPTIMIZATION.md:1) (technical implementation)

---

### v8.4 — Investigation Tree + Architecture Validated (Nov 16, 2025)

**Problem**: APEX complexity topics (≥8) require multi-perspective dialectical analysis beyond linear investigation.

**Solution**:
- Investigation Tree: Multi-branch analysis (branches A/B/C for different narratives)
- COMPARABLES_ASYMMETRY: Cross-branch comparison methodology for double standards
- Each branch: Independent investigation with full evidence collection

**Impact**:
- Dialectical decomposition: Official vs Dissident vs Regional perspectives mapped in parallel
- Double standard detection: "Why outrage for X but silence for Y?" systematically quantified
- EDI targets achieved: SIMPLE≥0.30 ✅, MEDIUM≥0.50 ✅, COMPLEX≥0.70 ✅, APEX≥0.80 ✅
- Dual-Engine validated: WebSearch (95%+ success) + MCP web-search (60-80%) operational

**Validation**: [tests/tree/](tests/tree/) (12 test files including COMPARABLES_ASYMMETRY methodology)

**Documentation**: [kb/INVESTIGATION_TREE.md](kb/INVESTIGATION_TREE.md:1) (949 lines)

**MCP Integration**: MnemoLite (semantic KB search) + Context7 (library docs) + web-search (DuckDuckGo)

---

### REJECTED — Google Search MCP (Nov 16, 2025)

**Attempted**: Integrate `web-agent-master/google-search` (Playwright-based Google scraping) as third search engine.

**Load Test Results (25 queries)**:
- Burst (0s delay): 0/10 success (0%)
- Moderate (5s delay): 0/10 success (0%)
- Conservative (30s delay): 0/5 success (0%)
- **TOTAL: 0/25 success (0%)**

**Root Cause**: Google anti-bot overlay blocks 100% of Playwright headless searches. No mitigation successful.

**Decision**:
- KEEP existing dual-engine (WebSearch official API + MCP web-search DuckDuckGo)
- REJECT Playwright scraping (0% success rate, 13-20min latency per investigation)
- Official APIs > Scraping (2025 reality)

**Lessons Learned**:
1. Playwright Google scraping = non-viable 2025 (anti-bot insurmountable)
2. Load testing critical before integration (saved 8-10h dev time)
3. Existing architecture already optimal (avoid "solutionnisme")

**Documentation**:
- Postmortem: [docs/postmortems/2025-11-16-google-search-mcp-ABANDONED.md](docs/postmortems/2025-11-16-google-search-mcp-ABANDONED.md:1)
- Memory: [docs/memory/2025-11-16-google-search-mcp-abandoned.md](docs/memory/2025-11-16-google-search-mcp-abandoned.md:1)

---

## 🎯 Roadmap Évolutionnaire (KISS)

**Pas de phases fixes**. Juste **priorités émergentes** basées sur usage réel.

### Priorité P0 (Immediate, cette semaine)

1. ✅ **Setup MCP complet** (COMPLETED — MnemoLite + Context7 + web-search)
2. ✅ **10+ investigations test** (COMPLETED — tests/query_optimization/ + tests/tree/)
3. **Première meta-analysis** (identifier 1-2 gaps critiques)
4. **1-2 KB improvements** (fix gaps détectés)

### Priorité P1 (Court terme, ce mois)

1. **Workflow batch** (investigations nocturnes automatisées)
2. **Logging structured** (JSON format standardisé — expand beyond current markdown logs)
3. **Meta-development weekly** (review logs → improve KB systematically)
4. ✅ **Git workflow** (COMPLETED — branch experiments, A/B testing, postmortem documentation)

### Priorité P2 (Moyen terme, Q1 2025)

1. **Pattern auto-discovery** (unsupervised clustering logs)
2. **Adversarial testing** (red team cases, robustness)
3. **Benchmark continuous** (gold standard dataset + tracking)
4. **Dual-LLM experiments** (Claude Code + Desktop collaboration)

### Priorité P3 (Long terme, exploration)

1. **Multi-agent swarm** (3+ LLMs investigate parallel → synthesis)
2. **External APIs** (integrate Brave/Exa search si Context7 insuffisant)
3. **Public showcase** (demo investigations + methodology transparency)
4. **Academic paper** (formaliser Truth Engine comme framework)

---

## 🧪 Métriques de Succès

**Pas de vanity metrics**. Focus = signal.

### Métriques Usage (Track 1)

| Metric | Baseline | Target Month 1 | Target Month 3 |
|--------|----------|----------------|----------------|
| **Investigations/semaine** | 0 | 10 | 30 |
| **EDI moyen** | - | 0.50 | 0.60 |
| **H7 coverage** | - | 80% | 90% |
| **Pattern detection rate** | - | 60% | 80% |
| **Investigation failures** | - | <20% | <10% |

### Métriques Développement (Track 2)

| Metric | Baseline | Target Month 1 | Target Month 3 |
|--------|----------|----------------|----------------|
| **KB improvements/mois** | 0 | 3 | 8 |
| **New patterns added** | 20 | 22 | 25 |
| **H7 map size** | 25 | 30 | 40 |
| **Benchmark score** | - | 0.85 | 0.90 |
| **Regression incidents** | - | 0 | 0 |

---

## 💎 Principes Directeurs

### 1. Feedback Loop > Planning

Pas de roadmap rigide. **Observe usage → detect patterns → improve → repeat.**

### 2. Measure Everything (Quietly)

JSON logs = data. Git commits = experiments. Pas de dashboard complexe, juste `grep` et analyse.

### 3. Fail Fast, Learn Faster

Investigation EDI=0.35? **Good**. C'est du feedback. Fix KB, retest, iterate.

### 4. Document Discoveries

Nouveau pattern détecté? → Add kb/PATTERNS.md immediately.  
Formula imprécise? → Fix kb/COGNITIVE_DSL.md same day.

### 5. No Gold Plating

Si feature pas utilisée après 1 mois → delete. YAGNI strict.

---

## 🔮 Vision Long-Terme

**Truth Engine devient**:
- Auto-amélioration continue (self-supervised learning symbolic)
- Benchmark épistémique (standard qualité investigations)
- Framework open (autres peuvent fork + adapter)
- Résistant adversarial (red team tested)
- Scientifiquement validé (benchmark public, reproductible)

**Horizon 6 mois**: 
- 100+ investigations
- 30+ patterns
- 50+ H7 sources
- Benchmark score 0.90+
- Zero regression incidents
- Academic paper draft

**Horizon 12 mois**:
- Framework generalisable (pas juste politique/corporate)
- Multi-domaine (science, law, tech, finance)
- Community-driven (contributions externes KB)
- Industry adoption (journalistes, fact-checkers, chercheurs)

---

## 🚀 Action Immediate

**Maintenant (next 30 min)**:
1. Config MCP Claude Desktop
2. Index KB Truth Engine
3. Investigation test #1: "Chômage 7.4%"
4. Observer résultat, noter gaps
5. Fix 1 gap immédiat si évident

**Loop démarre**. Iteration #1. KISS. Build momentum.

---

---

**Truth Engine v8.4** (Nov 16, 2025)
Not a product. A living system. Use → Learn → Evolve → Repeat.

**Recent breakthroughs:**
- ✅ Query Optimization v8.3 (productive query rate: 0-40% → 80-100%)
- ✅ Investigation Tree v8.4 (multi-branch dialectical analysis for APEX topics)
- ✅ Dual-Engine validated (WebSearch 95%+ + MCP web-search 60-80%)
- ✅ Postmortem workflow (institutional memory of failures — Google Search MCP case study)

**Architecture status:** Production-ready. MCP integration complete. EDI targets achieved across all complexity tiers.
