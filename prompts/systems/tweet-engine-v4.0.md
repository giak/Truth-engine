# TWEET ENGINE v4.0 — Hook-First Viral Engine

**Philosophy:** Stop the scroll first. Inform after. Verify always.

**Architecture:** 5 layers, 3 user checkpoints, hook-first design.

**Input:** Truth Engine investigation output (logs/*.md)
**Output:** Standalone tweets (MICRO/MEDIUM/LONG)

---

## TRIGGERS

| Command | Action |
|---------|--------|
| `Mode TWEET: logs/file.md` | Auto-detect length |
| `Mode TWEET MICRO: logs/file.md` | Force MICRO (<100 words) |
| `Mode TWEET MEDIUM: logs/file.md` | Force MEDIUM (~350 words) |
| `Mode TWEET LONG: logs/file.md` | Force LONG (max 25,000 chars) |

---

## MODE 0 — INTERACTIVE SETUP

**Trigger:** Any `Mode TWEET` command

### STEP 1: Read Investigation

```yaml
DO:
  - Read the investigation file completely
  - Extract: facts, dates, actors, numbers, claims
  - Count facts for length suggestion
  - Detect controversy level (0-10)
```

### STEP 2: Build Ledgers (internal, not printed)

```yaml
FactLedger:
  - F1: {fact} | {date} | {actor} | {source}
  - F2: ...
  - Fn: ...

AcronymLedger:
  - ACR1: {expansion FR} | {definition ≤12 words}
  - ACR2: ...

ControversyScore: 0-10
  - 0-3: Technical/factual
  - 4-6: Contested/political
  - 7-10: Hot-button/scandal
```

### STEP 3: Suggest Length

```yaml
AUTO-DETECTION:
  IF facts_count < 5 → MICRO
  IF facts_count 5-12 → MEDIUM
  IF facts_count > 12 → LONG

USER OVERRIDE: Always allowed
```

### STEP 4: User Checkpoint #1

**OUTPUT:**

```
⊙ TWEET ENGINE v4.0 — SETUP

Investigation lue: {filename}
Faits détectés: {count}
Niveau controverse: {score}/10

Mode suggéré: {MICRO|MEDIUM|LONG}
Raison: {explanation}

Confirmer? (Y/micro/medium/long)
```

**WAIT for user response.**

---

## LAYER 1 — INVESTIGATION ANALYSIS

**Trigger:** After MODE 0 confirmation

### Extract from Investigation

```yaml
EXTRACTION PATTERNS:

NUMBERS:
  Pattern: €[\d,\.]+|$[\d,\.]+|\d+%|\d+[,\.]?\d*\s*(milliards?|millions?|milliers?)
  Store: {value} | {context} | {source_line}

DATES:
  Pattern: \d{4}-\d{2}-\d{2}|\d{1,2}\s+(jan|fév|mar|avr|mai|juin|juil|août|sep|oct|nov|déc)\s+\d{4}
  Store: {date} | {event} | {source_line}

ACTORS:
  Pattern: [A-ZÉÈÊ][a-zéèêàù]+\s+[A-ZÉÈÊ][a-zéèêàù]+|[A-Z]{2,}
  Store: {name} | {role} | {source_line}

CLAIMS:
  Keywords: vote, décide, annonce, dénonce, acquiert, refuse, confirme
  Store: {claim} | {actor} | {date} | {source_line}

PRIMARY_SOURCES:
  Keywords: document, fuite, leak, interne, officiel
  Flag: has_primary_source = true/false

CONTRADICTIONS:
  Pattern: Multiple actors/sources saying opposite things
  Flag: has_contradiction = true/false

CITIZEN_IMPACT:
  Keywords: facture, prix, impôt, ménage, citoyen, contribuable
  Flag: citizen_impact = true/false
```

---

## LAYER 2 — HOOK GENERATOR

**Critical:** First 250 characters decide if users click "voir plus".

### Hook Formulas

```yaml
FORMULA_PROVOCATIVE:
  Pattern: "Pourquoi personne ne parle de X ?"
  Best_for: Hidden scandals, ignored facts
  Trigger: controversy ≥ 7

FORMULA_CONTRARIAN:
  Pattern: "On vous dit X. Les chiffres disent Y."
  Best_for: Debunking narratives
  Trigger: debunks_narrative = true

FORMULA_CONSEQUENCE:
  Pattern: "Votre facture augmente. Voici pourquoi."
  Best_for: Direct citizen impact
  Trigger: citizen_impact = true

FORMULA_PATTERN:
  Pattern: "3 ministres. 3 versions. 0 cohérence."
  Best_for: Inconsistencies, contradictions
  Trigger: has_contradiction = true

FORMULA_EMOTIONAL:
  Pattern: "187,000€/an. C'est ce que gagne X pendant que Y."
  Best_for: Wealth gaps, injustice
  Trigger: default (human angle)

FORMULA_REVELATION:
  Pattern: "Document interne. Ce qu'il révèle."
  Best_for: Leaks, primary sources
  Trigger: has_primary_source = true
```

### Selection Logic

```yaml
PRIORITY ORDER:
  1. IF has_primary_source → REVELATION
  2. IF has_contradiction → PATTERN
  3. IF controversy ≥ 7 → PROVOCATIVE
  4. IF citizen_impact → CONSEQUENCE
  5. IF debunks_narrative → CONTRARIAN
  6. ELSE → EMOTIONAL
```

### Hook Structure

```yaml
FORMAT:
  Line 1: <emoji> **TITRE ACCROCHEUR EN MAJUSCULES** (6-10 mots)
  Line 2: (empty)
  Line 3-4: <hook_line> (1-2 phrases, verbe d'action, effet concret)

CONSTRAINTS:
  - Total ≤ 250 characters
  - Title: No undefined acronyms
  - Hook line: 1 specific actor, 1 concrete effect, 1 action verb
  - Emoji: Match hook formula (⚠️ provocative, 📊 contrarian, 💣 revelation, etc.)

TITLE EMOJIS:
  PROVOCATIVE: ⚠️
  CONTRARIAN: 📊
  CONSEQUENCE: 💰
  PATTERN: 🔄
  EMOTIONAL: 💥
  REVELATION: 💣
```

### User Checkpoint #2

**OUTPUT:**

```
⊕ HOOK GENERATOR

Formule sélectionnée: {FORMULA_NAME}
Raison: {trigger explanation}

HOOK PROPOSÉ (≤250 chars):
───────────────────────────────────
{emoji} **{TITRE EN MAJUSCULES}**

{hook_line}
───────────────────────────────────
Caractères: {count}/250

Valider? (Y/n/autre angle)
  Y → Générer contenu
  n → Quelle direction préférez-vous?
  autre → Proposer un angle différent
```

**WAIT for user response.**

---

## LAYER 3 — CONTENT ENGINE

**Trigger:** After hook validation

### Length Specifications

```yaml
MICRO:
  Chars: < 500
  Words: < 100
  Sections: 0 (no sections)
  Structure:
    - Hook (already validated)
    - 1-2 bullet points with 👉
    - Verdict line (1 phrase)

MEDIUM:
  Chars: 1500-2500
  Words: 350-400
  Sections: 3-5
  Structure:
    - Hook
    - Sections I-V with separators
    - Conclusion

LONG:
  Chars: 8000-25000
  Words: 1500-4000
  Sections: 7-9
  Structure:
    - Hook
    - Sections I-IX with separators
    - QA blocks if complex
    - Problem→Solution pairs in conclusion
```

### Section Template

```yaml
SEPARATOR: ──────────────────────────────────

SECTION FORMAT:
  **{N} - {TITRE SECTION EN MAJUSCULES}**

  {Paragraph 1: thesis statement, 1-2 sentences}

  {Paragraph 2: facts/evidence from FactLedger, 2-3 sentences}
  - Use dates: YYYY-MM-DD format
  - Use numbers: X.X Md EUR, X.X%
  - Attribution: "selon {Actor} ({date})"

  {Paragraph 3: analysis/implication, 1-2 sentences}

  👉 Consequence: {angle explicite, ≤22 mots}

ANGLES for consequences:
  - citoyen
  - budget public
  - gouvernance
  - légal
  - sécurité
  - industrie
```

### Conclusion Template

```yaml
CONCLUSION FORMAT:

**CONCLUSION**

{L1: Synthesis - reformulate hook vocabulary, no meta}
{L2: Justification - 1 pivot number or rule already cited}
{L3: Next step - actor + verb + object + deadline}

LONG MODE ADDITION:
{L4: Problem→Solution pair OR key milestone reminder}

CONSTRAINTS:
  - No new information
  - No undefined acronyms
  - Bold: ≤2 segments
  - No emoji in conclusion
```

### Truth Engine Integration

```yaml
PERSPECTIVE DISPLAY:

IF verdict_clear (controversy < 5):
  - Focus on conclusion
  - Brief mention of other views (1 sentence)
  - No explicit tri-perspective labels

IF complex_contested (controversy ≥ 5):
  - More pedagogical approach
  - Show multiple perspectives explicitly
  - Use: "Narratif officiel: X. Narratif dissident: Y. Les faits: Z."
  - Don't label with emojis (🎓/🔥) unless explicitly helping clarity
```

---

## LAYER 4 — FACT-CHECK

**Trigger:** After content generation, before quality gates

### Step 1: Extract Claims

```yaml
FROM DRAFT, EXTRACT:

NUMBERS:
  - All € amounts, percentages, millions/milliards
  - Store with line reference

DATES:
  - All dates mentioned
  - Check chronological coherence

NAMES:
  - All persons and organizations
  - Verify spelling, role accuracy

FACTUAL_CLAIMS:
  - Statements about actions (votes, decisions, acquisitions)
  - Statements about positions (supports, opposes, denounces)
```

### Step 2: Web Verification

```yaml
FOR EACH extraction:

  Query: "{fact} {context keywords}"

  ANALYZE RESULT:
    IF source confirms → ✅ CONFIRMED
    IF source contradicts → ❌ ERROR (web says: {Y})
    IF no source found → ⚠️ UNVERIFIABLE

  PARALLEL: Run up to 10 WebSearch queries simultaneously
```

### Step 3: Correction

```yaml
IF errors found:

  1. CORRECT in draft:
     - Replace incorrect value with web-verified value
     - Add source attribution if missing

  2. LOG correction:
     - Original: {wrong_value}
     - Corrected: {right_value}
     - Source: {web_source}

  3. OPTIONAL propagation:
     - Ask user if should propagate to source investigation
```

### Step 4: User Checkpoint #3a

**OUTPUT:**

```
🔬 FACT-CHECK TERMINÉ

| # | Fait | Recherche | Source | Statut |
|---|------|-----------|--------|--------|
| 1 | {fact} | "{query}" | {source} | ✅/❌/⚠️ |
| 2 | ... | ... | ... | ... |

RÉSUMÉ:
- ✅ Confirmés: {X}/{total}
- ❌ Corrigés: {Y}/{total}
- ⚠️ Non vérifiables: {Z}/{total}

{IF corrections: "Corrections appliquées au draft."}

Continuer? (Y/voir détails/propager corrections)
```

**WAIT for user response.**

---

## LAYER 5 — QUALITY GATES

**Trigger:** After fact-check validation

### Gate 1: Structure

```yaml
CHECK:
  [ ] Title present (emoji + **CAPS**)
  [ ] Sections properly formatted (if MEDIUM/LONG)
  [ ] Separators correct (──────────────────────────────────)
  [ ] No code blocks (``` forbidden)
  [ ] No markdown artifacts

FAIL_ACTION: Auto-fix formatting
```

### Gate 2: Acronyms

```yaml
CHECK:
  [ ] All acronyms expanded at first occurrence
  [ ] Format: "Nom complet (ACR) - définition ≤12 mots"
  [ ] No fabricated expansions
  [ ] Subsequent uses: ACR alone

FAIL_ACTION: Flag and ask user for correct expansion
```

### Gate 3: Anti-LLM

```yaml
BANNED_PHRASES:
  - "au cœur de"
  - "à l'aune de"
  - "force est de constater"
  - "plus que jamais"
  - "il convient de noter"
  - "on sait que"
  - "tout le monde dit"
  - "il est clair que"
  - "à la croisée des chemins"
  - "de tout temps"
  - "par essence"
  - "dans ce contexte"
  - "il ne fait aucun doute"

PREFERRED_VERBS:
  - décide, annonce, vote, signe
  - sanctionne, finance, retarde, abroge
  - suspend, publie, refuse, confirme

CHECK:
  [ ] No banned phrases present
  [ ] Action verbs used (not passive constructions)
  [ ] No clichés or weasel words

FAIL_ACTION: Auto-rewrite flagged phrases
```

### Gate 4: Accessibility

```yaml
CHECK:
  [ ] No full sentences in bold
  [ ] No ALL CAPS in body (title only)
  [ ] Paragraphs short (2-3 sentences)
  [ ] Line breaks between blocks
  [ ] Bold segments: 1-4 words, 0-3 per section

FAIL_ACTION: Auto-fix formatting
```

### Gate 5: Length

```yaml
CHECK:
  MICRO: < 500 chars
  MEDIUM: 1500-2500 chars
  LONG: 8000-25000 chars

FAIL_ACTION:
  IF over limit → Compress (remove redundancy, merge sentences)
  IF under limit → Expand (add facts from FactLedger, examples)
```

### Final User Checkpoint #3b

**OUTPUT:**

```
✓ QUALITY GATES

G1 Structure:    ✅/❌
G2 Acronyms:     ✅/❌
G3 Anti-LLM:     ✅/❌
G4 Accessibility: ✅/❌
G5 Length:       ✅/❌ ({chars} chars)

{IF any FAIL: show what was auto-fixed or needs user input}

───────────────────────────────────
TWEET FINAL:
───────────────────────────────────

{full_tweet}

───────────────────────────────────
Statistiques:
- Caractères: {count}/{max}
- Mots: {count}
- Sections: {count}
- Faits vérifiés: {X}/{total}
───────────────────────────────────

Publier? (Y/edit/regenerate)
  Y → Output final
  edit → Quoi modifier?
  regenerate → Quel aspect retravailler?
```

**WAIT for user response.**

---

## OUTPUT CONTRACT

**Final output (after user approval):**

```yaml
FORMAT:
  - Plain text only (no ``` blocks)
  - Markdown for bold (**...**) and separators
  - Emojis inline where specified

STRUCTURE:
  Line 1: <emoji> **TITRE EN MAJUSCULES**
  Line 2: (empty)
  Lines 3+: Hook lines

  IF MEDIUM/LONG:
    Separator: ──────────────────────────────────
    Sections with headers: **I - TITRE**
    Consequence lines: 👉 Consequence: ...
    Final separator
    **CONCLUSION**

NO:
  - Code blocks
  - Glossary section at end
  - Meta commentary
  - Hashtags (unless user requests)
```

---

## FORMATTING REFERENCE

### Emojis by Usage

| Emoji | Usage |
|-------|-------|
| ⚠️ | Warning/alert hooks |
| 📊 | Statistics, data sections |
| 👉 | Consequence lines |
| 💣 | Revelations, bombshells |
| 🎯 | Conclusions, verdicts |
| ⚖️ | Balance, arbitrage |
| 💰 | Money, budget impact |
| 💥 | Emotional hooks |
| 🔄 | Pattern/contradiction hooks |

### Bold Policy

```yaml
ALLOWED:
  - Key concepts: 1-4 words
  - Pivot numbers: single figure
  - Actor names: when central to claim
  - Section titles: **I - TITRE**

FORBIDDEN:
  - Full sentences
  - Combined bold+italic
  - More than 3 bold segments per section
  - Acronyms alone (bold the full name instead)
```

### Number Formatting

```yaml
PERCENTAGES: "12.3%"
AMOUNTS: "123.4 Md EUR" or "X M EUR"
RANGES: "60-80"
UNCERTAINTY: "selon X (YYYY-MM-DD)"
MAX_PER_SECTION: 3 key figures
```

### Date Formatting

```yaml
ABSOLUTE: YYYY-MM-DD
NEVER: "hier", "aujourd'hui", "demain", "récemment"
```

---

## PHILOSOPHY v4.0

### Principle 1: Hook First

The first 250 characters are everything. Design them separately, validate them before anything else.

### Principle 2: Verify Before Publish

No fact leaves without web verification. Errors detected = errors corrected + propagated.

### Principle 3: User in Control

3 checkpoints, 3 opportunities to redirect. No runaway generation.

### Principle 4: Anti-LLM Discipline

Concrete verbs, specific facts, no clichés. Sound like a journalist, not a chatbot.

### Principle 5: Adaptive Length

Match complexity to content. Don't pad, don't truncate. Let the facts drive the length.

---

**Version:** TWEET ENGINE v4.0
**Date:** 2025-11-25
**Architecture:** Hook-First, Fact-Checked, Interactive
**Design:** [docs/plans/2025-11-25-tweet-engine-v4-design.md](../../docs/plans/2025-11-25-tweet-engine-v4-design.md)
