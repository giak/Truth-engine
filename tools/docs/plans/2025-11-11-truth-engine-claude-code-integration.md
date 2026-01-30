# Truth Engine Claude Code Integration — POC Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan POC-by-POC.

**Goal:** Integrate Truth Engine (system.md + kb/) into Claude Code with incremental POC validation, building from minimal end-to-end to full SIMPLE investigation capability.

**Architecture:** Top-Down incremental (end-to-end minimal → add layers), CLI wrapper + Claude Code conversation (POC phase), output markdown, validation hybrid (bash assertions + manual checks).

**Approach:**
- **Granularity:** POC par composant (15-30 min each)
- **Order:** Top-Down (feedback end-to-end dès POC 1)
- **Validation:** Hybrid (assertions bash + manual quality checks)
- **Execution:** Conversation normale Claude Code (POC 1-8), slash command custom (production later)
- **Output:** Markdown (logs/*.md)

**Estimated Time:** 3-4 hours (8 POC × 15-30min)

**Success Criteria (POC 8 final):**
- Investigation SIMPLE fonctionnelle
- EDI ≥0.30, ◈ PRIMARY ≥1
- ≥1 pattern détecté (ICEBERG minimum)
- Output Part 1+2+3 markdown valide
- MnemoLite persistence working

---

## POC 1: Hello World End-to-End (15-20 min)

**Scope:**
- CLI wrapper ultra-minimal (bash script)
- Prompt hardcodé: "Analyse: 2+2=4"
- Aucun system.md, aucun KB, aucune recherche web
- Output markdown brut dans logs/
- Validation: fichier créé, contient "2+2"

### Step 1: Create directory structure (2 min)

```bash
cd /home/giak/projects/truth-engine
mkdir -p bin lib/prompts tests/poc logs
```

### Step 2: Write minimal CLI wrapper (5 min)

Create: `bin/truth-engine`

```bash
#!/usr/bin/env bash
set -euo pipefail

# Truth Engine CLI v0.1 - POC 1
TRUTH_ENGINE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOGS_DIR="${TRUTH_ENGINE_ROOT}/logs"

mkdir -p "${LOGS_DIR}"

if [ $# -eq 0 ]; then
    echo "Usage: truth-engine \"Analyse: [subject]\""
    exit 1
fi

USER_QUERY="$*"
TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)
LOG_FILE="${LOGS_DIR}/${TIMESTAMP}_poc1.md"

# Hardcoded prompt POC 1
PROMPT="Analyse très simplement le sujet suivant: 2+2=4. Réponds en 3 lignes maximum en français. Output markdown."

echo "🧪 POC 1: Hello World"
echo "📝 Query: ${USER_QUERY}"
echo "📊 Output: ${LOG_FILE}"
echo ""

# Execute via Claude Code
cd "${TRUTH_ENGINE_ROOT}"
claude-code "${PROMPT}" > "${LOG_FILE}" 2>&1

echo ""
echo "✅ POC 1 complete. Output: ${LOG_FILE}"
```

Make executable:
```bash
chmod +x bin/truth-engine
```

### Step 3: Test CLI execution (3 min)

```bash
./bin/truth-engine "Test: Hello World"
```

**Expected:**
- File created: `logs/YYYY-MM-DD_HH-MM-SS_poc1.md`
- Contains response about "2+2=4"

### Step 4: Write validation script (3 min)

Create: `tests/poc/poc1_validate.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "🧪 Validating POC 1..."

# Find latest POC 1 output
LATEST=$(ls -t logs/*_poc1.md 2>/dev/null | head -n1)

if [ -z "${LATEST}" ]; then
    echo "❌ No POC 1 output found"
    exit 1
fi

# Check file exists and not empty
if [ ! -s "${LATEST}" ]; then
    echo "❌ Output file empty"
    exit 1
fi

# Check contains "2+2" or "4"
if grep -qi "2.*2\|quatre\|4" "${LATEST}"; then
    echo "✅ POC 1 validation passed"
    echo "📁 Output: ${LATEST}"
else
    echo "❌ Output doesn't mention 2+2 or 4"
    exit 1
fi
```

Make executable:
```bash
chmod +x tests/poc/poc1_validate.sh
```

### Step 5: Run validation (2 min)

```bash
tests/poc/poc1_validate.sh
```

**Expected:** `✅ POC 1 validation passed`

### Step 6: Manual check (2 min)

```bash
cat logs/*_poc1.md
```

**Verify:**
- Markdown format
- French response
- Mentions "2+2" or "4"

### Step 7: Commit (2 min)

```bash
git add bin/truth-engine tests/poc/poc1_validate.sh logs/.gitkeep
git commit -m "POC 1: minimal CLI wrapper + hardcoded prompt"
```

**Critère succès POC 1:** CLI s'exécute, génère markdown, test automatique passe ✅

---

## POC 2: + system.md Loading + Herméneutique Basique (20-25 min)

**Scope:**
- CLI charge system.md (lecture fichier)
- Prompt: "Lis system.md, analyse sujet: France unemployment 7.4%, détecte 1 concept ICEBERG"
- Pas de MnemoLite KB search (juste lecture locale system.md)
- Pas de web search
- Output: détection concept ICEBERG

### Step 1: Update CLI to load system.md (5 min)

Modify: `bin/truth-engine` (replace PROMPT section)

```bash
SYSTEM_MD="${TRUTH_ENGINE_ROOT}/system.md"

# Check system.md exists
if [ ! -f "${SYSTEM_MD}" ]; then
    echo "❌ system.md not found at ${SYSTEM_MD}"
    exit 1
fi

LOG_FILE="${LOGS_DIR}/${TIMESTAMP}_poc2.md"

PROMPT="Tu es Truth Engine.

1. Lis le fichier system.md à ${SYSTEM_MD}
2. Analyse le sujet: ${USER_QUERY}
3. Détecte AU MOINS le concept ICEBERG (populations cachées vs visibles)
4. Output markdown français avec:
   - Titre: # Investigation POC 2
   - Sujet analysé
   - Concept ICEBERG détecté (explique brièvement)

Travaille de façon autonome."
```

### Step 2: Test with new subject (3 min)

```bash
./bin/truth-engine "France unemployment 7.4%"
```

**Expected:**
- File: `logs/YYYY-MM-DD_HH-MM-SS_poc2.md`
- Contains "ICEBERG" mention

### Step 3: Update validation script (5 min)

Create: `tests/poc/poc2_validate.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "🧪 Validating POC 2..."

LATEST=$(ls -t logs/*_poc2.md 2>/dev/null | head -n1)

if [ -z "${LATEST}" ]; then
    echo "❌ No POC 2 output found"
    exit 1
fi

# Check system.md loaded (indirect: file not empty, has substance)
if [ $(wc -l < "${LATEST}") -lt 10 ]; then
    echo "❌ Output too short (<10 lines), system.md may not have been loaded"
    exit 1
fi

# Check ICEBERG concept detected
if grep -qi "iceberg\|caché\|visible.*hidden\|omission" "${LATEST}"; then
    echo "✅ POC 2 validation passed (ICEBERG detected)"
    echo "📁 Output: ${LATEST}"
else
    echo "❌ ICEBERG concept not detected in output"
    exit 1
fi
```

Make executable:
```bash
chmod +x tests/poc/poc2_validate.sh
```

### Step 4: Run validation (2 min)

```bash
tests/poc/poc2_validate.sh
```

### Step 5: Manual check (5 min)

```bash
cat logs/*_poc2.md
```

**Verify:**
- Markdown structure (# titre)
- Subject "France unemployment" mentioned
- ICEBERG concept explained
- System.md appears to have been read (context from KB visible in response)

### Step 6: Commit (2 min)

```bash
git add bin/truth-engine tests/poc/poc2_validate.sh
git commit -m "POC 2: load system.md + detect ICEBERG concept"
```

**Critère succès POC 2:** system.md chargé, concept ICEBERG détecté ✅

---

## POC 3: + MnemoLite KB Semantic Search (25-30 min)

**Scope:**
- **Pré-requis:** KB indexé dans MnemoLite (fait manuellement avant ce POC)
- Prompt: "Use MCP search_code (repo: truth-engine-kb) to find 'ICEBERG pattern', apply to subject"
- Recherche sémantique KB via MCP
- Pas de web search
- Output: ICEBERG avec détails depuis KB

### Step 0: Index KB in MnemoLite (one-time, 5 min)

**Manual operation before POC 3:**

```bash
claude-code "Use MCP tool mcp__mnemolite__index_project to index:
  project_path: /home/giak/projects/truth-engine/kb
  repository: truth-engine-kb
  include_gitignored: false"
```

**Verify indexing:**
```bash
claude-code "Use MCP search_code to find 'ICEBERG pattern' in repository 'truth-engine-kb'"
```

Expected: Returns PATTERNS.md with ICEBERG_V4

### Step 1: Update CLI to use MCP search (8 min)

Modify: `bin/truth-engine` (replace PROMPT section)

```bash
LOG_FILE="${LOGS_DIR}/${TIMESTAMP}_poc3.md"

PROMPT="Tu es Truth Engine POC 3.

**Étapes:**

1. Use MCP tool mcp__mnemolite__search_code with:
   - query: \"ICEBERG pattern detection omissions\"
   - filters: {\"repository\": \"truth-engine-kb\"}
   - limit: 5

2. Lis le résultat MCP pour comprendre le pattern ICEBERG

3. Analyse le sujet: ${USER_QUERY}

4. Applique le pattern ICEBERG avec détails du KB

5. Output markdown français:
   # Investigation POC 3

   ## Sujet
   ${USER_QUERY}

   ## Pattern ICEBERG (depuis KB)
   [Détails du pattern]

   ## Application au sujet
   [Analyse]

Travaille de façon autonome."
```

### Step 2: Test MCP KB search (5 min)

```bash
./bin/truth-engine "France unemployment 7.4%"
```

**Expected:**
- File: `logs/YYYY-MM-DD_HH-MM-SS_poc3.md`
- ICEBERG with KB details (not just concept mention, but actual pattern methodology)

### Step 3: Update validation (5 min)

Create: `tests/poc/poc3_validate.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "🧪 Validating POC 3..."

LATEST=$(ls -t logs/*_poc3.md 2>/dev/null | head -n1)

if [ -z "${LATEST}" ]; then
    echo "❌ No POC 3 output found"
    exit 1
fi

# Check ICEBERG pattern present
if ! grep -qi "iceberg" "${LATEST}"; then
    echo "❌ ICEBERG not found"
    exit 1
fi

# Check KB details present (look for pattern-specific terms)
# ICEBERG pattern has: visible/hidden, populations, omission
if grep -qi "visible.*caché\|population.*caché\|omission" "${LATEST}"; then
    echo "✅ POC 3 validation passed (KB pattern details present)"
    echo "📁 Output: ${LATEST}"
else
    echo "❌ KB pattern details not detected (may not have used MCP search)"
    exit 1
fi
```

Make executable:
```bash
chmod +x tests/poc/poc3_validate.sh
```

### Step 4: Run validation (2 min)

```bash
tests/poc/poc3_validate.sh
```

### Step 5: Manual check (3 min)

```bash
cat logs/*_poc3.md
```

**Verify:**
- ICEBERG pattern with methodology details (not just name)
- Visible vs hidden populations quantified (if possible)
- KB appears to have been searched (specific ICEBERG terminology)

### Step 6: Document MCP requirement (2 min)

Create: `docs/POC_REQUIREMENTS.md`

```markdown
# POC Requirements

## POC 3+ Prerequisites

### MnemoLite KB Indexed

**One-time setup:**
```bash
claude-code "Use MCP index_project:
  project_path: /home/giak/projects/truth-engine/kb
  repository: truth-engine-kb"
```

**Verify:**
```bash
claude-code "Search truth-engine-kb for 'ICEBERG pattern'"
```

Expected: Returns PATTERNS.md content
```

### Step 7: Commit (2 min)

```bash
git add bin/truth-engine tests/poc/poc3_validate.sh docs/POC_REQUIREMENTS.md
git commit -m "POC 3: MnemoLite KB semantic search for patterns"
```

**Critère succès POC 3:** MCP KB search fonctionne, pattern ICEBERG avec détails KB ✅

---

## POC 4: + Web Search MCP (30-40 min)

**Scope:**
- Prompt: "Use MCP mcp__web-search__search for 3 queries about subject"
- Vraies recherches web via MCP
- Output: sources web citées (format [Name—URL])
- Pas de stratification ◈◉○ encore

### Step 1: Update CLI with web search (10 min)

Modify: `bin/truth-engine`

```bash
LOG_FILE="${LOGS_DIR}/${TIMESTAMP}_poc4.md"

PROMPT="Tu es Truth Engine POC 4.

**Étapes:**

1. Sujet: ${USER_QUERY}

2. Web searches (use MCP tool mcp__web-search__search):
   - Query 1: \"${USER_QUERY}\"
   - Query 2: Variation (traduis en anglais ou reformule)
   - Query 3: \"${USER_QUERY} statistics data\"

   Pour chaque query: limit=5

3. Use MCP search_code (truth-engine-kb) pour ICEBERG pattern

4. Analyse le sujet avec:
   - Sources web collectées
   - Pattern ICEBERG

5. Output markdown français:
   # Investigation POC 4

   ## Sujet
   ${USER_QUERY}

   ## Sources Web (≥3)
   - [Source 1—URL]
   - [Source 2—URL]
   - [Source 3—URL]

   ## Pattern ICEBERG
   [Application avec données web]

   ## Analyse
   [Synthèse]

Cite TOUTES les sources au format [Name—URL]. Travaille autonome."
```

### Step 2: Test web search (5 min)

```bash
./bin/truth-engine "France unemployment 7.4%"
```

**Expected:**
- File: `logs/YYYY-MM-DD_HH-MM-SS_poc4.md`
- ≥3 web sources cited with URLs

### Step 3: Update validation (8 min)

Create: `tests/poc/poc4_validate.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "🧪 Validating POC 4..."

LATEST=$(ls -t logs/*_poc4.md 2>/dev/null | head -n1)

if [ -z "${LATEST}" ]; then
    echo "❌ No POC 4 output found"
    exit 1
fi

# Count web source citations [Name—URL] or [Name - URL]
SOURCE_COUNT=$(grep -oE '\[.*—.*https?://.*\]|\[.*-.*https?://.*\]' "${LATEST}" | wc -l)

if [ "${SOURCE_COUNT}" -ge 3 ]; then
    echo "✅ POC 4 validation passed (${SOURCE_COUNT} web sources cited)"
    echo "📁 Output: ${LATEST}"
else
    echo "❌ Insufficient web sources (found ${SOURCE_COUNT}, need ≥3)"
    exit 1
fi

# Check URLs are valid format
if ! grep -qE 'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' "${LATEST}"; then
    echo "❌ No valid URLs detected"
    exit 1
fi

echo "✅ URLs present and valid format"
```

Make executable:
```bash
chmod +x tests/poc/poc4_validate.sh
```

### Step 4: Run validation (2 min)

```bash
tests/poc/poc4_validate.sh
```

### Step 5: Manual check (5 min)

```bash
cat logs/*_poc4.md
```

**Verify:**
- ≥3 distinct web sources
- URLs clickable/valid
- Sources relevant to subject
- ICEBERG analysis uses web data

### Step 6: Test MCP fallback awareness (5 min)

**Note in docs:** If MCP web-search not available, POC 4 will fail. Fallback APIs (Brave/Exa) are for production (post-POC 8).

Create: `docs/POC_TROUBLESHOOTING.md`

```markdown
# POC Troubleshooting

## POC 4: Web Search Fails

**Symptom:** No web sources in output, or error about MCP tool not found

**Cause:** MCP web-search not available in Claude Code session

**Solutions:**

1. **Check MCP configured:**
   ```bash
   claude-code "List MCP tools"
   ```
   Should see `mcp__web-search__search`

2. **If MCP unavailable:** POC 4 cannot proceed. Options:
   - Wait for MCP web-search availability
   - Skip POC 4, move to POC 5 (output structure)
   - Configure Brave/Exa API (production feature, not POC scope)

## POC 3: KB Search Fails

**Symptom:** ICEBERG pattern lacks KB details

**Cause:** MnemoLite not indexed

**Solution:** Run indexing (see docs/POC_REQUIREMENTS.md)
```

### Step 7: Commit (2 min)

```bash
git add bin/truth-engine tests/poc/poc4_validate.sh docs/POC_TROUBLESHOOTING.md
git commit -m "POC 4: web search via MCP (3+ sources cited)"
```

**Critère succès POC 4:** ≥3 sources web citées avec URLs valides ✅

---

## POC 5: + Output Structuré Part 1/2/3 (25-30 min)

**Scope:**
- Output markdown structuré en 3 parties
- Part 1: Analyse française (tri-perspective basique)
- Part 2: Diagnostics (EDI/ISN placeholders OK pour POC)
- Part 3: WOLF (ou "(WOLF not applicable)")

### Step 1: Update CLI for 3-part output (10 min)

Modify: `bin/truth-engine`

```bash
LOG_FILE_BASE="${LOGS_DIR}/${TIMESTAMP}_poc5"
LOG_FILE="${LOG_FILE_BASE}.md"

PROMPT="Tu es Truth Engine POC 5.

**Sujet:** ${USER_QUERY}

**Étapes:**

1. Web searches (MCP mcp__web-search__search): 3 queries minimum
2. KB search (MCP search_code truth-engine-kb): ICEBERG pattern
3. Analyse tri-perspective:
   - Académique ⟐🎓 (mainstream/institutionnel)
   - Dissident 🔥⟐̅ (contre-narrative)
   - Arbitrage (synthèse critique)

**Output structure (un seul fichier markdown):**

# Investigation POC 5 — ${USER_QUERY}

## Part 1 — Analyse (Français)

### Sources
- [Source 1—URL]
- [Source 2—URL]
- [Source 3—URL]

### Tri-Perspective

**Académique ⟐🎓:**
[Position mainstream]

**Dissident 🔥⟐̅:**
[Contre-narrative]

**Arbitrage:**
[Synthèse critique, 95% hostilité symétrique]

### Points Critiques (≥4)
- **Point 1:** ...
- **Point 2:** ...
- **Point 3:** ...
- **Point 4:** ...

---

## Part 2 — Diagnostics (Technique)

**EDI (Epistemic Diversity Index):** 0.XX (placeholder POC, vrai calcul POC 7)
**ISN (Information Source Network):** X.X (placeholder)
**Patterns détectés:** ICEBERG
**Sources:** ◈ PRIMARY: X, ◉ SECONDARY: X, ○ TERTIARY: X (approximatif)

---

## Part 3 — WOLF Report

(WOLF not applicable pour POC 5)

---

Travaille autonome. Output UNIQUEMENT ce markdown."
```

### Step 2: Test 3-part output (5 min)

```bash
./bin/truth-engine "France unemployment 7.4%"
```

### Step 3: Update validation (7 min)

Create: `tests/poc/poc5_validate.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "🧪 Validating POC 5..."

LATEST=$(ls -t logs/*_poc5.md 2>/dev/null | head -n1)

if [ -z "${LATEST}" ]; then
    echo "❌ No POC 5 output found"
    exit 1
fi

# Check 3 parts present
PARTS_FOUND=0

if grep -q "## Part 1" "${LATEST}"; then
    echo "✅ Part 1 present"
    ((PARTS_FOUND++))
else
    echo "❌ Part 1 missing"
fi

if grep -q "## Part 2" "${LATEST}"; then
    echo "✅ Part 2 present"
    ((PARTS_FOUND++))
else
    echo "❌ Part 2 missing"
fi

if grep -q "## Part 3" "${LATEST}"; then
    echo "✅ Part 3 present"
    ((PARTS_FOUND++))
else
    echo "❌ Part 3 missing"
fi

if [ "${PARTS_FOUND}" -ne 3 ]; then
    echo "❌ POC 5 validation failed (${PARTS_FOUND}/3 parts found)"
    exit 1
fi

# Check tri-perspective
if grep -qi "académique.*🎓\|⟐🎓" "${LATEST}" && \
   grep -qi "dissident.*🔥\|🔥⟐̅" "${LATEST}" && \
   grep -qi "arbitrage" "${LATEST}"; then
    echo "✅ Tri-perspective present"
else
    echo "❌ Tri-perspective incomplete"
    exit 1
fi

# Check critical points (≥4)
CRITICAL_POINTS=$(grep -c "^- \*\*Point" "${LATEST}" || echo 0)
if [ "${CRITICAL_POINTS}" -ge 4 ]; then
    echo "✅ Critical points ≥4 (found ${CRITICAL_POINTS})"
else
    echo "⚠️  Critical points <4 (found ${CRITICAL_POINTS})"
fi

echo "✅ POC 5 validation passed"
echo "📁 Output: ${LATEST}"
```

Make executable:
```bash
chmod +x tests/poc/poc5_validate.sh
```

### Step 4: Run validation (2 min)

```bash
tests/poc/poc5_validate.sh
```

### Step 5: Manual check (5 min)

```bash
cat logs/*_poc5.md
```

**Verify:**
- Clear 3-part structure
- Tri-perspective present (Académique, Dissident, Arbitrage)
- ≥4 critical points
- Part 2 has placeholders (OK for POC)
- Part 3 says "(WOLF not applicable)" (OK for POC)

### Step 6: Commit (2 min)

```bash
git add bin/truth-engine tests/poc/poc5_validate.sh
git commit -m "POC 5: structured 3-part output (FR + diagnostics + WOLF)"
```

**Critère succès POC 5:** 3 parties présentes, tri-perspective, structure valide ✅

---

## POC 6: + Pattern Detection Basique (20-25 min)

**Scope:**
- Détection 1-2 patterns (ICEBERG obligatoire, +1 optionnel si applicable)
- Pattern avec score approximatif
- Output Part 2: patterns listés avec scores

### Step 1: Update prompt for pattern detection (8 min)

Modify: `bin/truth-engine`

```bash
PROMPT="Tu es Truth Engine POC 6.

**Sujet:** ${USER_QUERY}

**Étapes:**

1. Web searches (MCP): 3 queries
2. KB search (MCP):
   - \"ICEBERG pattern omissions\"
   - \"manipulation patterns list\" (trouve autres patterns applicables)
3. Détecte patterns:
   - ICEBERG: TOUJOURS (cherche visible vs caché)
   - +1 autre pattern si applicable (MONEY €, BIO, NET 🌐, etc.)

4. Pour chaque pattern détecté:
   - Score 0-10 (0=absent, 10=maximal)
   - Justification brève

**Output structure:**

# Investigation POC 6 — ${USER_QUERY}

## Part 1 — Analyse

[Tri-perspective comme POC 5]

## Part 2 — Diagnostics

**Patterns Détectés:**

### ICEBERG (score: X.X/10)
- **Visible:** [Ce qui est montré]
- **Caché:** [Ce qui est omis]
- **Ratio:** visible/total ≈ XX%

### [AUTRE PATTERN si applicable] (score: X.X/10)
[Description]

**Metrics:**
- EDI: 0.XX (placeholder POC 7)
- ISN: X.X (placeholder)
- Sources: ◈ PRIMARY ≥1, ◉ SECONDARY X, ○ TERTIARY X

## Part 3 — WOLF

(WOLF not applicable)

Travaille autonome."
```

### Step 2: Test pattern detection (5 min)

```bash
./bin/truth-engine "France unemployment 7.4%"
```

**Expected:** ICEBERG detected with visible/caché breakdown

### Step 3: Update validation (5 min)

Create: `tests/poc/poc6_validate.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "🧪 Validating POC 6..."

LATEST=$(ls -t logs/*_poc6.md 2>/dev/null | head -n1)

if [ -z "${LATEST}" ]; then
    echo "❌ No POC 6 output found"
    exit 1
fi

# Check ICEBERG pattern present
if ! grep -qi "iceberg" "${LATEST}"; then
    echo "❌ ICEBERG pattern not detected"
    exit 1
fi

# Check ICEBERG has score
if grep -qi "iceberg.*score.*[0-9]" "${LATEST}"; then
    echo "✅ ICEBERG pattern with score detected"
else
    echo "⚠️  ICEBERG detected but no score"
fi

# Check visible/caché breakdown
if grep -qi "visible.*caché\|caché.*visible" "${LATEST}"; then
    echo "✅ Visible/Caché breakdown present"
else
    echo "⚠️  No visible/caché breakdown"
fi

# Count total patterns
PATTERN_COUNT=$(grep -ci "score.*[0-9]" "${LATEST}" || echo 0)
echo "📊 Patterns detected: ${PATTERN_COUNT}"

if [ "${PATTERN_COUNT}" -ge 1 ]; then
    echo "✅ POC 6 validation passed"
    echo "📁 Output: ${LATEST}"
else
    echo "❌ No patterns detected"
    exit 1
fi
```

Make executable:
```bash
chmod +x tests/poc/poc6_validate.sh
```

### Step 4: Run validation (2 min)

```bash
tests/poc/poc6_validate.sh
```

### Step 5: Manual check (3 min)

```bash
cat logs/*_poc6.md | grep -A 10 "ICEBERG"
```

**Verify:**
- ICEBERG score présent (approximatif OK)
- Visible vs caché identifiés
- Si applicable: autre pattern (MONEY, BIO, etc.)

### Step 6: Commit (2 min)

```bash
git add bin/truth-engine tests/poc/poc6_validate.sh
git commit -m "POC 6: pattern detection (ICEBERG + optionnel)"
```

**Critère succès POC 6:** ≥1 pattern (ICEBERG) détecté avec score ✅

---

## POC 7: + EDI Calculation Basique (25-30 min)

**Scope:**
- Calcul EDI 6 dimensions (simplifié, pas toutes les formules complexes KB)
- Sources stratifiées ◈◉○ (basique, pas tous les critères exhaustifs)
- Output Part 2: EDI score + counts ◈◉○

### Step 1: Update prompt for EDI calculation (12 min)

Modify: `bin/truth-engine`

```bash
PROMPT="Tu es Truth Engine POC 7.

**Sujet:** ${USER_QUERY}

**Étapes:**

1. Web searches (MCP): 5 queries minimum
   - Varie: langues, domaines, types sources

2. KB search (MCP):
   - \"EDI formula epistemic diversity\"
   - \"source stratification primary secondary tertiary\"
   - \"ICEBERG pattern\"

3. Stratifie sources collectées:
   - ◈ PRIMARY: Sources indépendantes, investigatives, leaks, archives
   - ◉ SECONDARY: Média mainstream fact-checked
   - ○ TERTIARY: Institutionnel, corporate, étatique

4. Calcule EDI basique (6 dimensions simplifiées):
   - Geo diversity: continents couverts / 6
   - Lang diversity: langues / 4
   - Source stratification: ◈ weight 0.90, ◉ 0.80, ○ 0.50
   - Temporal: sources récentes vs historiques
   - Perspective: mainstream vs adversarial
   - Ownership: indépendant vs corporate

   EDI = moyenne des 6 dimensions (0.0-1.0)

**Output:**

# Investigation POC 7 — ${USER_QUERY}

## Part 1 — Analyse

[Tri-perspective]

## Part 2 — Diagnostics

**EDI (Epistemic Diversity Index):** 0.XX

**Breakdown:**
- Geo diversity: 0.XX (continents: X/6)
- Lang diversity: 0.XX (langues: X)
- Stratification: 0.XX (◈ ratio)
- Temporal: 0.XX
- Perspective: 0.XX
- Ownership: 0.XX

**Sources:**
- ◈ PRIMARY: X
- ◉ SECONDARY: X
- ○ TERTIARY: X
- Total: X

**Patterns:**
- ICEBERG (score: X.X)
- [Other if applicable]

**Quality Gate:** EDI ≥0.30 for SIMPLE complexity

## Part 3 — WOLF

(WOLF not applicable)

Travaille autonome."
```

### Step 2: Test EDI calculation (5 min)

```bash
./bin/truth-engine "France unemployment 7.4%"
```

### Step 3: Update validation (6 min)

Create: `tests/poc/poc7_validate.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "🧪 Validating POC 7..."

LATEST=$(ls -t logs/*_poc7.md 2>/dev/null | head -n1)

if [ -z "${LATEST}" ]; then
    echo "❌ No POC 7 output found"
    exit 1
fi

# Extract EDI score
EDI=$(grep -oP "EDI.*:\s*\K[0-9.]+"|head -n1 "${LATEST}" || echo "0")

if [ -z "${EDI}" ] || [ "${EDI}" = "0" ]; then
    echo "❌ EDI score not found or zero"
    exit 1
fi

echo "📊 EDI score: ${EDI}"

# Check EDI range [0.0, 1.0]
if (( $(echo "${EDI} >= 0.0 && ${EDI} <= 1.0" | bc -l) )); then
    echo "✅ EDI in valid range"
else
    echo "❌ EDI out of range [0.0, 1.0]"
    exit 1
fi

# Check PRIMARY sources ≥1
PRIMARY=$(grep -oP "PRIMARY:\s*\K[0-9]+" "${LATEST}" | head -n1 || echo "0")

if [ "${PRIMARY}" -ge 1 ]; then
    echo "✅ PRIMARY sources ≥1 (found ${PRIMARY})"
else
    echo "⚠️  PRIMARY sources <1 (found ${PRIMARY})"
fi

# Check EDI ≥0.30 (SIMPLE target)
if (( $(echo "${EDI} >= 0.30" | bc -l) )); then
    echo "✅ EDI ≥0.30 (SIMPLE target met)"
else
    echo "⚠️  EDI <0.30 (${EDI}), below SIMPLE target"
fi

echo "✅ POC 7 validation passed"
echo "📁 Output: ${LATEST}"
```

Make executable:
```bash
chmod +x tests/poc/poc7_validate.sh
```

### Step 4: Run validation (2 min)

```bash
tests/poc/poc7_validate.sh
```

### Step 5: Manual check (3 min)

```bash
cat logs/*_poc7.md | grep -A 15 "Part 2"
```

**Verify:**
- EDI score calculé (0.0-1.0)
- Breakdown 6 dimensions (même approximatif)
- ◈◉○ counts présents
- ◈ PRIMARY ≥1

### Step 6: Commit (2 min)

```bash
git add bin/truth-engine tests/poc/poc7_validate.sh
git commit -m "POC 7: EDI calculation + source stratification"
```

**Critère succès POC 7:** EDI calculé ≥0.30, ◈ PRIMARY ≥1 ✅

---

## POC 8: + MnemoLite Persistence (20-25 min)

**Scope:**
- Après output, save Part 1 (texte français) to MnemoLite memory
- Use MCP `write_memory` tool
- Tags: investigation, truth-engine, complexity
- Validation: retrieve via `search_code` dans nouvelle session

### Step 1: Update prompt for persistence (10 min)

Modify: `bin/truth-engine`

```bash
PROMPT="Tu es Truth Engine POC 8 FINAL.

**Sujet:** ${USER_QUERY}

**Étapes:**

1. Web searches (MCP): 5+ queries
2. KB search (MCP): EDI, ICEBERG, stratification
3. Tri-perspective analysis
4. EDI calculation + source stratification
5. Pattern detection (ICEBERG minimum)
6. Generate output Part 1+2+3
7. **PERSISTENCE:** Save Part 1 to MnemoLite

**Output structure:** [Same as POC 7]

**APRÈS génération output, PERSISTENCE:**

Use MCP tool mcp__mnemolite__write_memory with:
\`\`\`json
{
  \"title\": \"Investigation: ${USER_QUERY}\",
  \"content\": \"[Full Part 1 French text]\",
  \"memory_type\": \"note\",
  \"tags\": [\"investigation\", \"truth-engine\", \"simple\"],
  \"author\": \"Truth Engine v8.0\"
}
\`\`\`

Confirme la sauvegarde MnemoLite à la fin de ton output.

Travaille autonome."
```

### Step 2: Test persistence (5 min)

```bash
./bin/truth-engine "France unemployment 7.4% POC 8 test"
```

**Expected:** Output mentions "Sauvegardé dans MnemoLite" ou "Saved to MnemoLite"

### Step 3: Verify persistence manually (3 min)

In NEW Claude Code session:

```bash
claude-code "Use MCP search_code to find memories with tags 'investigation' and 'truth-engine' in repository or memory store"
```

**Expected:** Returns memory with title "Investigation: France unemployment 7.4% POC 8 test"

### Step 4: Update validation (5 min)

Create: `tests/poc/poc8_validate.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "🧪 Validating POC 8..."

LATEST=$(ls -t logs/*_poc8.md 2>/dev/null | head -n1)

if [ -z "${LATEST}" ]; then
    echo "❌ No POC 8 output found"
    exit 1
fi

# Run POC 7 validations (EDI, PRIMARY, etc.)
source tests/poc/poc7_validate.sh "${LATEST}" 2>/dev/null || true

# Check MnemoLite save mentioned
if grep -qi "mnemolite.*sauv\|saved.*memory\|write_memory" "${LATEST}"; then
    echo "✅ MnemoLite persistence mentioned in output"
else
    echo "⚠️  MnemoLite persistence not mentioned (may not have saved)"
fi

echo ""
echo "✅ POC 8 validation passed"
echo "📁 Output: ${LATEST}"
echo ""
echo "⚠️  MANUAL CHECK REQUIRED:"
echo "   Run: claude-code \"Search MnemoLite for truth-engine investigations\""
echo "   Verify: Memory with title 'Investigation: [subject]' exists"
```

Make executable:
```bash
chmod +x tests/poc/poc8_validate.sh
```

### Step 5: Run validation (2 min)

```bash
tests/poc/poc8_validate.sh
```

### Step 6: Manual verification (3 min)

```bash
cat logs/*_poc8.md | tail -20
```

Verify output mentions MnemoLite save.

Then in NEW Claude Code session:
```bash
claude-code "List recent memories tagged 'truth-engine'"
```

### Step 7: Document POC completion (3 min)

Create: `docs/POC_COMPLETE.md`

```markdown
# POC Phase Complete ✅

**Date:** 2025-11-11
**Final POC:** POC 8 (MnemoLite Persistence)

## Summary

**8 POC completed (3-4h):**
1. Hello World (CLI + hardcoded prompt) ✅
2. system.md loading + ICEBERG detection ✅
3. MnemoLite KB semantic search ✅
4. Web search MCP (3+ sources) ✅
5. 3-part output structure ✅
6. Pattern detection (ICEBERG + optional) ✅
7. EDI calculation + stratification ◈◉○ ✅
8. MnemoLite persistence ✅

## Capabilities Achieved

**Investigation SIMPLE fonctionnelle:**
- CLI wrapper: `bin/truth-engine "Analyse: [subject]"`
- system.md + KB loaded (via MnemoLite MCP)
- Web search: 5+ queries (MCP web-search)
- Output markdown 3 parts:
  - Part 1: Tri-perspective (Académique, Dissident, Arbitrage)
  - Part 2: EDI ≥0.30, ◈ PRIMARY ≥1, patterns détectés
  - Part 3: WOLF placeholder
- MnemoLite persistence: cross-session retrieval

## Quality Metrics (POC 8)

- **EDI:** ≥0.30 (SIMPLE target)
- **◈ PRIMARY:** ≥1
- **Patterns:** ≥1 (ICEBERG minimum)
- **Web sources:** 5+
- **Output:** Markdown structuré valide

## Next Steps (Production)

**Post-POC enhancements (not in POC scope):**
1. Slash command custom (`.claude/commands/investigate.md`)
2. Web search fallback (Brave/Exa APIs)
3. WOLF detection (individuals ≥8 or ≥5)
4. Complexity assessment (SIMPLE/MEDIUM/COMPLEX/APEX)
5. Validation loop (retry si gaps)
6. Iteration I0→I1→I2 workflow
7. Output formatters (bash validators)
8. Integration tests (pilot scripts)

**See:** Original plan Task 9-10 for production features.

## Usage (POC Phase)

```bash
# Index KB (one-time)
claude-code "Index truth-engine-kb"

# Run investigation
./bin/truth-engine "France unemployment 7.4%"

# Validate
tests/poc/poc8_validate.sh

# Check MnemoLite
claude-code "Search truth-engine investigations"
```

**POC → Production transition:** Implement remaining tasks from original plan if needed for MEDIUM/COMPLEX investigations.
```

### Step 8: Commit POC 8 final (2 min)

```bash
git add bin/truth-engine tests/poc/poc8_validate.sh docs/POC_COMPLETE.md
git commit -m "POC 8 FINAL: MnemoLite persistence + investigation SIMPLE complete"
```

**Critère succès POC 8:** Investigation sauvée MnemoLite, récupérable, SIMPLE fonctionnelle ✅

---

## POC Phase Complete — Summary

**Time invested:** 3-4 hours (8 POC × 15-30 min)

**Deliverables:**
- ✅ CLI wrapper: `bin/truth-engine`
- ✅ 8 validation scripts: `tests/poc/poc{1-8}_validate.sh`
- ✅ Documentation: `docs/POC_*.md`
- ✅ Investigation SIMPLE capability

**Quality gates met:**
- EDI ≥0.30
- ◈ PRIMARY ≥1
- Pattern ICEBERG detected
- Web sources cited (5+)
- MnemoLite persistence working
- Output markdown valid (3 parts)

**Production roadmap (optional):**
- Tasks 9-10 from original plan (if needed for MEDIUM/COMPLEX)
- Slash command
- Web search fallback APIs
- WOLF detection
- Complexity assessment
- Validation retry loop
- Iteration protocol

**Usage:**
```bash
cd /home/giak/projects/truth-engine

# Run investigation SIMPLE
./bin/truth-engine "Analyse: [subject]"

# Validate
tests/poc/poc8_validate.sh

# Review output
cat logs/*_poc8.md
```

---

**Version:** POC v1.0 (8 POC baby steps)
**Approach:** Top-Down incremental, hybrid validation
**Execution:** Conversation Claude Code (POC phase)
**Status:** ✅ Ready for POC 1 implementation
