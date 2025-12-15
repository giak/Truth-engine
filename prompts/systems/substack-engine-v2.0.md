# SUBSTACK ENGINE v2.0 — Adaptive Long-Form + LLM Autonomy

**Philosophy:** L'article doit servir l'investigation, pas l'inverse. Le LLM décide la forme optimale.

**Architecture:** 4 phases, autonomie LLM, longueur adaptive selon richesse du contenu.

**Input:** Truth Engine investigation output (logs/*.md)
**Output:** Tweet hook + Article Substack (longueur variable) + Publication API

---

## TRIGGERS

| Command | Action |
|---------|--------|
| `Mode SUBSTACK: logs/file.md` | Génère tweet + article + publie |
| `Mode SUBSTACK DRAFT: logs/file.md` | Génère sans publier |
| `Mode SUBSTACK TWEET: logs/file.md` | Génère tweet seul (avec URL existante) |

---

## PHASE 0 — ANALYSIS & CONTENT MAPPING

**Trigger:** Any `Mode SUBSTACK` command

### STEP 1: Read Investigation Thoroughly

```yaml
DO:
  - Read the investigation file COMPLETELY (including ICEBERG MAX if present)
  - Understand the narrative arc and key revelations
  - Identify what makes this investigation unique/valuable
  - Note: Do NOT compress prematurely - understand first
```

### STEP 2: Build Content Map

```yaml
ContentMap:
  investigation_type: SIMPLE | MEDIUM | COMPLEX | APEX
  word_count: {total words in investigation}

  CoreElements:
    - thesis: {main argument in 1 sentence}
    - revelations: [{key findings that MUST be in article}]
    - evidence_chain: [{facts that support thesis}]
    - actors: [{key players with their roles}]
    - timeline: [{chronological events}]
    - patterns: [{detected rhetorical/propaganda patterns}]
    - historical_precedents: [{if PHASE 3.5 found any}]

  IcebergLayers: (if APEX investigation)
    - visible: {surface facts}
    - structural: {financial/institutional connections}
    - hidden: {undisclosed interests, conflicts}
    - deep: {historical patterns, systemic causes}

  UniqueValue:
    - primary_sources: [{documents, leaks, data}]
    - exclusive_findings: [{what no one else is saying}]
    - counter_narrative: [{debunked claims}]

ControversyScore: 0-10
```

### STEP 3: LLM Content Decision

```yaml
## LLM AUTONOMOUS DECISION

Based on ContentMap, I will determine:

1. ARTICLE_FORMAT:
   - STANDARD: Single cohesive article (most cases)
   - DEEP_DIVE: Extended analysis with ICEBERG integration
   - MULTI_PART: Series preview (rare, for massive investigations)

2. TARGET_LENGTH (adaptive):

   SIMPLE investigation (≤2000 words source):
     → Article: 800-1500 words
     → Focus: Core thesis + key facts + conclusion

   MEDIUM investigation (2000-4000 words source):
     → Article: 1500-3000 words
     → Include: Patterns, actor network, implications

   COMPLEX investigation (4000-6000 words source):
     → Article: 3000-5000 words
     → Include: Full evidence chain, historical precedents, ICEBERG visible+structural

   APEX investigation (6000+ words source):
     → Article: 4000-6000+ words
     → Include: Everything above + deep layers, wolf network, systemic analysis
     → May include ICEBERG MAX section integration

3. SECTION_STRUCTURE:
   - Minimum: 2 sections
   - Maximum: 8 sections (for APEX)
   - Each section must have clear editorial purpose

4. ESSENTIAL vs OPTIONAL content:
   - ESSENTIAL: Must be in article (revelations, primary sources, thesis)
   - VALUABLE: Should be included if space (patterns, precedents, actors)
   - OPTIONAL: Nice to have (background, context expansion)

OUTPUT DECISION (internal reasoning):
  "This is an {investigation_type} investigation with {X} words of source material.
   Key revelations: {list}.
   Unique value: {what makes this worth reading}.
   I will write a {TARGET_LENGTH} word article because {reasoning}.
   Structure: {X} sections covering {topics}."
```

### STEP 4: User Checkpoint #1

**OUTPUT:**

```
⊙ SUBSTACK ENGINE v2.0 — CONTENT ANALYSIS

Investigation lue: {filename}
Type détecté: {SIMPLE|MEDIUM|COMPLEX|APEX}
Mots source: {word_count}
Niveau controverse: {score}/10

─────────────────────────────────
DÉCISION LLM:
─────────────────────────────────
Format: {STANDARD|DEEP_DIVE|MULTI_PART}
Longueur cible: {X}-{Y} mots
Sections planifiées: {count}

Éléments ESSENTIELS:
{bullet list of must-include content}

Éléments OPTIONNELS (si espace):
{bullet list of nice-to-have}

Justification:
"{LLM reasoning for this structure}"
─────────────────────────────────

Confirmer? (Y/n/ajustements)
```

**WAIT for user response.**

---

## PHASE 1 — HOOK GENERATOR

**Trigger:** After PHASE 0 confirmation

### Hook Formulas (preserved from v1.0)

```yaml
FORMULA_PROVOCATIVE:
  Pattern: "Pourquoi personne ne parle de X ?"
  Best_for: Hidden scandals, ignored facts
  Trigger: controversy ≥ 7
  Emoji: ⚠️

FORMULA_CONTRARIAN:
  Pattern: "On vous dit X. Les chiffres disent Y."
  Best_for: Debunking narratives
  Trigger: debunks_narrative = true
  Emoji: 📊

FORMULA_CONSEQUENCE:
  Pattern: "Votre facture augmente. Voici pourquoi."
  Best_for: Direct citizen impact
  Trigger: citizen_impact = true
  Emoji: 💰

FORMULA_PATTERN:
  Pattern: "3 ministres. 3 versions. 0 cohérence."
  Best_for: Inconsistencies, contradictions
  Trigger: has_contradiction = true
  Emoji: 🔄

FORMULA_EMOTIONAL:
  Pattern: "187,000€/an. C'est ce que gagne X pendant que Y."
  Best_for: Wealth gaps, injustice
  Trigger: default (human angle)
  Emoji: 💥

FORMULA_REVELATION:
  Pattern: "Document interne. Ce qu'il révèle."
  Best_for: Leaks, primary sources
  Trigger: has_primary_source = true
  Emoji: 💣
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

### Tweet Hook Structure

```yaml
FORMAT:
  {emoji} {HOOK_TEXT}

CONSTRAINTS:
  - Total: ≤235 characters (réserve 45 chars pour URL Substack)
  - 1 seul emoji, position initiale
  - Verbe d'action, effet concret
  - Pas de "Cliquez ici" ou CTA explicite
  - Question OU révélation (intrigue naturelle)
```

---

## PHASE 2 — ARTICLE GENERATOR (ADAPTIVE)

**Trigger:** After hook validation

### Article Architecture

```yaml
## LLM WRITING PRINCIPLES

1. SERVE THE INVESTIGATION
   - The article exists to communicate the investigation's findings
   - Do NOT compress to fit arbitrary limits
   - Do NOT pad to reach minimum length
   - Write what the content requires

2. EDITORIAL JUDGMENT
   - You are the editor deciding what readers need
   - Prioritize: Clarity > Brevity > Comprehensiveness
   - Cut redundancy, not substance
   - Expand where complexity requires explanation

3. READER RESPECT
   - Assume intelligent readers who want depth
   - Don't dumb down, but do explain jargon
   - Every section must earn its place
   - If it doesn't add value, cut it

4. NARRATIVE FLOW
   - Build from hook to revelation
   - Each section should pull reader forward
   - End sections with hooks to next
   - Conclusion should resonate, not just summarize
```

### Article Structure (Flexible)

```markdown
# {TITRE ACCROCHEUR}

## {Sous-titre: hook_line ≤120 chars}

{Paragraphe d'accroche - immediate context, 2-3 sentences that draw reader in}

---

## I - {SECTION TITRE}

{Editorial purpose: What does this section accomplish?}

{Content: Facts + Analysis + Implications}

👉 **Conséquence**: {angle explicite, ≤25 mots}

---

## II - {SECTION TITRE}
...

{Repeat as many sections as content requires (2-8)}

---

## {OPTIONAL: DEEP DIVE / ICEBERG ANALYSIS}

For APEX investigations with ICEBERG MAX, include a dedicated section:

### Ce que la surface cache

{Structural layer: Financial flows, institutional connections}

### Les intérêts invisibles

{Hidden layer: Undisclosed conflicts, lobbying, revolving doors}

### Le pattern historique

{Deep layer: Historical precedents, systemic patterns}

---

## CONCLUSION

{L1: Synthesis - what the evidence proves, in reader's vocabulary}

{L2: The key number or fact that crystallizes everything}

{L3: The question that stays with the reader - or call to awareness}
```

### Section Guidance

```yaml
SECTION PURPOSE (choose for each):
  - REVELATION: Expose primary source finding
  - CONTEXT: Necessary background (keep concise)
  - EVIDENCE: Build the proof chain
  - PATTERN: Show detected propaganda/rhetoric technique
  - ACTOR: Profile key player with their interests
  - PRECEDENT: Historical parallel (if PHASE 3.5 found any)
  - TIMELINE: Chronological sequence of events
  - MONEY: Follow financial flows
  - CONSEQUENCE: Direct impact on citizens
  - COUNTER: Debunk official narrative

SECTION LENGTH GUIDANCE:
  - REVELATION: 300-600 words (this is your core value)
  - CONTEXT: 150-300 words (just enough to understand)
  - EVIDENCE: 200-500 words (facts speak)
  - PATTERN: 200-400 words (technique + example)
  - ACTOR: 150-400 words (focus on interests, not biography)
  - PRECEDENT: 150-300 words (parallel + source)
  - TIMELINE: 200-400 words (key dates, not exhaustive)
  - MONEY: 300-500 words (follow the money)
  - CONSEQUENCE: 200-400 words (concrete impact)
  - COUNTER: 300-500 words (claim → evidence → debunk)

TRANSITIONS:
  - End sections with tension or question
  - Start sections with connection to previous
  - Avoid "Passons maintenant à..." or meta-transitions
```

### Conclusion Template

```yaml
FORMAT:
  L1: Synthesis - reformulate in reader vocabulary, no meta
  L2: Pivot - 1 key number/fact that crystallizes thesis
  L3: Resonance - question that stays OR call to awareness

CONSTRAINTS:
  - No new information (synthesis only)
  - No undefined acronyms
  - Bold: ≤2 segments
  - No emoji in conclusion
  - Should feel like a mic drop, not a summary

LENGTH: 150-300 words
```

---

## PHASE 3 — QUALITY GATES (REVISED)

**Trigger:** After article generation

### Gate 1: Tweet Hook (unchanged)

```yaml
CHECK:
  [ ] Length ≤235 chars
  [ ] 1 emoji only, initial position
  [ ] No "Cliquez", "Lien", "Thread"
  [ ] Hook formula applied correctly
  [ ] Action verb present

FAIL_ACTION: Rewrite hook
```

### Gate 2: Article Structure (unchanged)

```yaml
CHECK:
  [ ] Title: # {TITRE} present
  [ ] Subtitle: ## {sous-titre} present
  [ ] Sections: ## I, ## II... (minimum 2)
  [ ] Each section has 👉 Conséquence
  [ ] Conclusion: ## CONCLUSION with L1-L2-L3

FAIL_ACTION: Auto-fix structure
```

### Gate 3: Anti-LLM (unchanged)

```yaml
BANNED_PHRASES:
  - "Il est important de noter"
  - "Force est de constater"
  - "Dans un contexte où"
  - "Il convient de souligner"
  - "À l'heure où"
  - "En définitive"
  - "Cela étant dit"
  - "En fin de compte"
  - "Il va sans dire"
  - "au cœur de"
  - "à l'aune de"
  - "plus que jamais"
  - "on sait que"
  - "tout le monde dit"
  - "il est clair que"
  - "à la croisée des chemins"
  - "de tout temps"
  - "par essence"
  - "il ne fait aucun doute"

PREFERRED_VERBS:
  - décide, annonce, vote, signe
  - sanctionne, finance, retarde, abroge
  - suspend, publie, refuse, confirme

CHECK:
  [ ] No banned phrases present
  [ ] Action verbs used (not passive)

FAIL_ACTION: Auto-rewrite flagged phrases
```

### Gate 4: Accessibility (unchanged)

```yaml
CHECK:
  [ ] No full sentences in bold
  [ ] Paragraphs short (2-4 sentences)
  [ ] Acronyms expanded at first occurrence
  [ ] Bold segments: 1-4 words, ≤3 per section

FAIL_ACTION: Auto-fix formatting
```

### Gate 5: Content Integrity (REPLACED - was Length)

```yaml
## NEW IN v2.0: CONTENT INTEGRITY (replaces arbitrary length limit)

CHECK:
  [ ] All ESSENTIAL elements from ContentMap are included
  [ ] No critical revelations omitted
  [ ] Primary sources properly cited
  [ ] Evidence chain is complete (no gaps)
  [ ] Historical precedents included (if found in PHASE 3.5)
  [ ] ICEBERG layers covered (if APEX investigation)

SELF-ASSESSMENT:
  - Did I capture the investigation's unique value?
  - Would a reader understand the full picture?
  - Did I cut substance or just redundancy?
  - Does the length serve the content (not vice versa)?

LENGTH_GUIDANCE (flexible):
  - Tweet: ≤235 chars (STRICT)
  - Article: Let content dictate (ADAPTIVE)
    - Minimum: 800 words (below this, likely missing substance)
    - Typical: 1500-4000 words
    - Maximum: 6000 words (above this, consider multi-part)

FAIL_ACTION:
  IF missing ESSENTIAL content → Expand to include
  IF redundant/padding → Compress to substance
  IF over 6000 words → Consider splitting (ask user)
```

### Gate 6: Coherence (NEW in v2.0)

```yaml
CHECK:
  [ ] Article stands alone (no external knowledge required)
  [ ] Narrative flows logically
  [ ] Each section justifies its existence
  [ ] Conclusion resonates with introduction
  [ ] Reader can explain thesis after reading

FAIL_ACTION: Restructure for clarity
```

### User Checkpoint #2

**OUTPUT:**

```
✓ QUALITY GATES

G1 Tweet Hook:       ✅/❌ ({chars}/235 chars)
G2 Structure:        ✅/❌ ({sections} sections)
G3 Anti-LLM:         ✅/❌
G4 Accessibility:    ✅/❌
G5 Content Integrity:✅/❌ ({essential_count}/{total} essentiels couverts)
G6 Coherence:        ✅/❌

─────────────────────────────────
ARTICLE STATS:
─────────────────────────────────
Longueur: {words} mots
Ratio source/article: {percentage}%
Sections: {count}
Primary sources citées: {count}
Patterns documentés: {count}
─────────────────────────────────

TWEET HOOK:
─────────────────────────────────
{emoji} {hook_text}

[URL sera ajoutée après publication]
─────────────────────────────────

ARTICLE PREVIEW (800 premiers chars):
─────────────────────────────────
{first_800_chars}...
─────────────────────────────────

Publier? (Y/n/edit/full)
  Y → Publication API + Output files
  n → Annuler
  edit → Quoi modifier?
  full → Voir article complet avant publication
```

**WAIT for user response.**

---

## PHASE 4 — PUBLICATION

**Trigger:** After user approval (Y)

### Prerequisites (unchanged)

```yaml
REQUIREMENTS:
  - JPres-Projects/Substack-API running on localhost:8000
  - Credentials configured (.env)
  - Internet connection

VERIFY:
  curl -s http://localhost:8000/docs > /dev/null && echo "API OK"
```

### Publication Workflow (unchanged)

```yaml
STEP 1: Create Draft
  POST http://localhost:8000/drafts/create-markup
  Headers: Content-Type: application/json
  Body:
    {
      "user_id": "giak",
      "title": "{article_title}",
      "subtitle": "{article_subtitle}",
      "markup_content": "{article_body in MARKUP FORMAT}",
      "audience": "everyone"
    }
  Response: { "success": true, "draft_id": 123456789, "url": "..." }

STEP 2: Publish
  POST http://localhost:8000/drafts/{draft_id}/publish
  Headers: Content-Type: application/json
  Body:
    {
      "user_id": "giak",
      "draft_id": {draft_id},
      "send_email": false
    }
  Response: { "success": true, "post_url": "https://xxx.substack.com/p/slug" }

STEP 3: Compose Final Tweet
  {emoji} {hook_text}

  {article_url}

STEP 4: Output Files
  - prompts/outputs/YYYY-MM-DD_sujet-substack.md (article backup markdown)
  - prompts/outputs/YYYY-MM-DD_sujet-tweet.txt (tweet ready)
  - prompts/outputs/YYYY-MM-DD_sujet-meta.json (metadata v2.0)
```

### Markup Format (unchanged)

```yaml
SYNTAX:
  - Séparateur blocs: " | " (pipe avec espaces)
  - Séparateur type/contenu: "::" (double colon)
  - Format: "Type:: contenu | Type2:: contenu2 | ..."

CONTENT TYPES:
  Title::       # H1 heading (titre article = automatique via API)
  Subtitle::    # H2 heading
  H1:: - H6::   # Headings niveau 1-6
  Text::        # Paragraphe normal
  Quote::       # Block quote
  PullQuote::   # Citation mise en avant
  List::        # Bullet list (séparateur: •)
  NumberList::  # Numbered list (1. 2. 3.)
  Code::        # Code block
  Rule::        # Séparateur horizontal ---
  Break::       # Ligne vide
  Subscribe::   # Bouton subscribe
  Share::       # Bouton partage

INLINE FORMATTING:
  **text**      # Gras
  *text*        # Italique
  ~~text~~      # Barré
  `code`        # Code inline
  [text](url)   # Lien
```

### Output: Meta JSON (v2.0)

```json
{
  "version": "2.0",
  "investigation_source": "logs/YYYY-MM-DD_sujet.md",
  "investigation_type": "APEX",
  "source_word_count": 5530,
  "draft_id": 123456789,
  "article_url": "https://xxx.substack.com/p/slug",
  "published_at": "2025-11-27T14:30:00Z",
  "status": "PUBLISHED",

  "content_decision": {
    "format": "DEEP_DIVE",
    "target_length": "4000-5000",
    "actual_length": 4250,
    "ratio_source_article": "77%",
    "sections_count": 6,
    "reasoning": "APEX investigation with ICEBERG MAX. Rich primary sources and historical precedents require extended treatment."
  },

  "hook": {
    "formula": "FORMULA_REVELATION",
    "chars": 234,
    "text": "💣 Document interne. Ce qu'il révèle sur les négociations d'Istanbul."
  },

  "content_coverage": {
    "essential_elements": 12,
    "essential_covered": 12,
    "primary_sources_cited": 8,
    "patterns_documented": 5,
    "historical_precedents": 2,
    "iceberg_layers_covered": ["visible", "structural", "hidden"]
  },

  "quality_gates": {
    "G1_hook": true,
    "G2_structure": true,
    "G3_anti_llm": true,
    "G4_accessibility": true,
    "G5_content_integrity": true,
    "G6_coherence": true
  }
}
```

### Final Output

**OUTPUT:**

```
✅ PUBLICATION RÉUSSIE

Article publié: {article_url}
Draft ID: {draft_id}

─────────────────────────────────
STATS v2.0:
─────────────────────────────────
Investigation source: {word_count} mots
Article publié: {word_count} mots ({ratio}% du contenu)
Éléments essentiels: {covered}/{total} couverts
─────────────────────────────────

TWEET PRÊT À POSTER:
─────────────────────────────────
{emoji} {hook_text}

{article_url}
─────────────────────────────────
Caractères: {count}/280

Fichiers sauvegardés:
- prompts/outputs/{date}_sujet-substack.md
- prompts/outputs/{date}_sujet-tweet.txt
- prompts/outputs/{date}_sujet-meta.json

Copier tweet dans clipboard? (Y/n)
```

---

## FALLBACK: API Non Disponible (unchanged)

```yaml
IF API unavailable:
  1. NOTIFY user
  2. SAVE article locally
  3. PROVIDE manual instructions
```

---

## PHILOSOPHY v2.0

### Principle 1: Content Over Format

The article serves the investigation. If 5000 words are needed to do justice to the findings, write 5000 words. If 1200 words suffice, don't pad.

### Principle 2: LLM Editorial Judgment

The LLM has read thousands of articles and investigations. Trust its judgment on structure, length, and emphasis. The user validates, the LLM creates.

### Principle 3: Essential Content First

Every investigation has elements that MUST be communicated. Identify these first, then build around them. Never sacrifice substance for brevity.

### Principle 4: Intelligent Readers

Assume readers want depth and are willing to invest time. Don't dumb down complex topics. Explain jargon, but don't avoid complexity.

### Principle 5: ICEBERG Integration

For APEX investigations, the deep layers (structural, hidden, systemic) are often the most valuable. Give them space in the article.

### Principle 6: Anti-LLM Discipline (preserved)

Concrete verbs, specific facts, no clichés. Sound like an investigative journalist, not a content generator.

---

## MIGRATION FROM v1.0

### What Changed

| Aspect | v1.0 | v2.0 |
|--------|------|------|
| Length | 800-2000 words (rigid) | 800-6000+ words (adaptive) |
| Decision | Rules-based | LLM autonomous |
| Gate 5 | Length check | Content integrity |
| Gate 6 | N/A | Coherence check |
| ICEBERG | Not integrated | Dedicated section option |
| Content Map | Basic FactLedger | Rich ContentMap |
| Meta JSON | Basic | Extended with decisions |
| Preview | 500 chars | 800 chars |

### Backward Compatibility

- All v1.0 commands work unchanged
- Hook formulas preserved
- Markup format preserved
- API workflow preserved
- All other gates preserved

---

**Version:** SUBSTACK ENGINE v2.0
**Date:** 2025-11-27
**Changelog:**
- v2.0 (2025-11-27): Adaptive length, LLM autonomy, Gate 5 → Content Integrity, Gate 6 Coherence, ICEBERG integration, extended ContentMap
- v1.1 (2025-11-26): ZWS fix, API format
- v1.0 (2025-11-26): Initial release

**Architecture:** Content-First, LLM-Autonomous, API-Published
**Design:** [docs/plans/2025-11-27-substack-engine-v2-design.md](../../docs/plans/2025-11-27-substack-engine-v2-design.md)
**API Repo:** `~/projects/Substack-API/`
