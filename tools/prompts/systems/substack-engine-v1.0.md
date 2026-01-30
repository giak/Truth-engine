# SUBSTACK ENGINE v1.0 — Publication Longue + Tweet Hook

**Philosophy:** Tweet court pour accrocher. Article Substack pour informer. API pour publier.

**Architecture:** 4 phases, 2 checkpoints user, publication API intégrée.

**Input:** Truth Engine investigation output (logs/*.md)
**Output:** Tweet hook (≤235 chars) + Article Substack + Publication API

---

## TRIGGERS

| Command | Action |
|---------|--------|
| `Mode SUBSTACK: logs/file.md` | Génère tweet + article + publie |
| `Mode SUBSTACK DRAFT: logs/file.md` | Génère sans publier |
| `Mode SUBSTACK TWEET: logs/file.md` | Génère tweet seul (avec URL existante) |

---

## PHASE 0 — SETUP

**Trigger:** Any `Mode SUBSTACK` command

### STEP 1: Read Investigation

```yaml
DO:
  - Read the investigation file completely
  - Extract: facts, dates, actors, numbers, claims
  - Count facts for article structure
  - Detect controversy level (0-10)
```

### STEP 2: Build Ledgers (internal)

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

### STEP 3: User Checkpoint #1

**OUTPUT:**

```
⊙ SUBSTACK ENGINE v1.0 — SETUP

Investigation lue: {filename}
Faits détectés: {count}
Niveau controverse: {score}/10

Sections suggérées: {2-5 based on facts_count}
Mots estimés: {800-2000}

Confirmer? (Y/n/ajustements)
```

**WAIT for user response.**

---

## PHASE 1 — HOOK GENERATOR

**Trigger:** After PHASE 0 confirmation

### Hook Formulas (from v4.0)

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

EXAMPLES:
  ⚠️ Pourquoi personne ne parle des 2.3 Md € votés sans débat parlementaire ?
  📊 On vous dit que le Mercosur protège l'agriculture. Les chiffres disent l'inverse.
  💣 Document interne FNSEA. Ce qu'il révèle sur le double discours.
```

---

## PHASE 2 — ARTICLE GENERATOR

**Trigger:** After hook validation

### Article Structure

```markdown
# {TITRE ACCROCHEUR}

## {Sous-titre: hook_line ≤120 chars}

{Paragraphe d'accroche - contexte immédiat, 2-3 phrases}

---

## I - {SECTION TITRE EN MAJUSCULES}

{Paragraph 1: thesis statement, 1-2 phrases}

{Paragraph 2: facts from FactLedger, 2-3 phrases}
- Dates: YYYY-MM-DD format
- Nombres: X.X Md EUR, X.X%
- Attribution: "selon {Actor} ({date})"

{Paragraph 3: analysis/implication, 1-2 phrases}

👉 **Conséquence**: {angle explicite, ≤22 mots}

---

## II - {SECTION TITRE EN MAJUSCULES}

{Same structure as Section I}

👉 **Conséquence**: {angle explicite, ≤22 mots}

---

{Repeat for Sections III, IV, V as needed (2-5 sections total)}

---

## CONCLUSION

{L1: Synthesis - ce que les faits démontrent, reformuler vocabulaire hook}

{L2: Justification - 1 pivot number ou règle déjà citée}

{L3: Next step - question ouverte OU appel à réflexion}
```

### Section Templates

```yaml
ANGLES for 👉 Conséquence:
  - citoyen (impact direct sur les gens)
  - budget public (argent des contribuables)
  - gouvernance (qui décide, comment)
  - légal (violation règles, constitution)
  - sécurité (risques, vulnérabilités)
  - industrie (bénéficiaires économiques)

SECTION COUNT:
  - 5-8 facts → 2 sections
  - 9-15 facts → 3 sections
  - 16-25 facts → 4 sections
  - 26+ facts → 5 sections max
```

### Conclusion Template (from v4.0)

```yaml
FORMAT:
  L1: Synthesis - reformulate hook vocabulary, no meta
  L2: Justification - 1 pivot number or rule already cited
  L3: Next step - actor + verb + object OR open question

CONSTRAINTS:
  - No new information
  - No undefined acronyms
  - Bold: ≤2 segments
  - No emoji in conclusion
```

---

## PHASE 3 — QUALITY GATES

**Trigger:** After article generation

### Gate 1: Tweet Hook

```yaml
CHECK:
  [ ] Length ≤235 chars
  [ ] 1 emoji only, initial position
  [ ] No "Cliquez", "Lien", "Thread"
  [ ] Hook formula applied correctly
  [ ] Action verb present

FAIL_ACTION: Rewrite hook
```

### Gate 2: Article Structure

```yaml
CHECK:
  [ ] Title: # {TITRE} present
  [ ] Subtitle: ## {sous-titre} present
  [ ] Sections: ## I, ## II... (minimum 2)
  [ ] Each section has 👉 Conséquence
  [ ] Conclusion: ## CONCLUSION with L1-L2-L3

FAIL_ACTION: Auto-fix structure
```

### Gate 3: Anti-LLM

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

### Gate 4: Accessibility

```yaml
CHECK:
  [ ] No full sentences in bold
  [ ] Paragraphs short (2-3 sentences)
  [ ] Acronyms expanded at first occurrence
  [ ] Bold segments: 1-4 words, ≤3 per section

FAIL_ACTION: Auto-fix formatting
```

### Gate 5: Length

```yaml
CHECK:
  - Tweet: ≤235 chars
  - Article: 800-2000 words

FAIL_ACTION:
  IF over → Compress (merge redundancy)
  IF under → Expand (add facts from FactLedger)
```

### User Checkpoint #2

**OUTPUT:**

```
✓ QUALITY GATES

G1 Tweet Hook:    ✅/❌ ({chars}/235 chars)
G2 Structure:     ✅/❌
G3 Anti-LLM:      ✅/❌
G4 Accessibility: ✅/❌
G5 Length:        ✅/❌ ({words} mots)

───────────────────────────────────
TWEET HOOK:
───────────────────────────────────
{emoji} {hook_text}

[URL sera ajoutée après publication]
───────────────────────────────────

ARTICLE PREVIEW (500 premiers chars):
───────────────────────────────────
{first_500_chars}...
───────────────────────────────────

Publier? (Y/n/edit)
  Y → Publication API + Output files
  n → Annuler
  edit → Quoi modifier?
```

**WAIT for user response.**

---

## PHASE 4 — PUBLICATION

**Trigger:** After user approval (Y)

### Prerequisites

```yaml
REQUIREMENTS:
  - JPres-Projects/Substack-API running on localhost:8000
  - Credentials configured (.env)
  - Internet connection

VERIFY:
  curl -s http://localhost:8000/docs > /dev/null && echo "API OK"
```

### Publication Workflow

```yaml
STEP 1: Create Draft
  POST http://localhost:8000/drafts/create-markup
  Headers: Content-Type: application/json
  Body:
    {
      "user_id": "giak",
      "title": "{article_title}",
      "subtitle": "{article_subtitle}",
      "markup_content": "{article_body in MARKUP FORMAT - see below}",
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
  - prompts/outputs/YYYY-MM-DD_sujet-meta.json (metadata)
```

### ⚠️ CRITICAL: Substack Markup Format

**L'API Substack utilise un format markup personnalisé, PAS du HTML ni du Markdown brut.**

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
  Code::        # Code block (Code:: language | code)
  Rule::        # Séparateur horizontal ---
  Break::       # Ligne vide
  Subscribe::   # Bouton subscribe
  Share::       # Bouton partage

INLINE FORMATTING (dans Text::):
  **text**      # Gras
  *text*        # Italique
  ~~text~~      # Barré
  `code`        # Code inline
  [text](url)   # Lien

EXAMPLE (conversion d'un article):

  MARKDOWN INPUT:
    ## I - LE VOTE QU'ON CACHE

    Le 23 novembre 2021, le Parlement européen...

    > AI will transform every industry.

    ---

    ## II - 9.6 MILLIARDS

    La France est le **premier bénéficiaire**...

  MARKUP OUTPUT:
    H2:: I - LE VOTE QU'ON CACHE | Text:: Le 23 novembre 2021, le Parlement européen... | Quote:: AI will transform every industry. | Rule:: | H2:: II - 9.6 MILLIARDS | Text:: La France est le **premier bénéficiaire**...
```

### Conversion Markdown → Markup

```yaml
RULES:
  1. Titre H1 (#): Ignoré (passé séparément via title)
  2. Sous-titre H2 (##): H2:: contenu
  3. Paragraphe: Text:: contenu
  4. Citation (>): Quote:: contenu OU PullQuote:: contenu
  5. Séparateur (---): Rule::
  6. Liste à puces: List:: • item1 • item2 • item3
  7. Liste numérotée: NumberList:: 1. item1 1. item2 1. item3
  8. Conserver inline: **gras**, *italique*, [lien](url)
  9. Chaque bloc séparé par " | "
```

### Output: Tweet File

```
{emoji} {hook_text}

{article_url}
```

### Output: Meta JSON

```json
{
  "investigation_source": "logs/YYYY-MM-DD_sujet.md",
  "draft_id": 123456789,
  "article_url": "https://xxx.substack.com/p/slug",
  "api_fix_applied": "draft_create.py:356-359 ZWS workaround",
  "published_at": "2025-11-26T14:30:00Z",
  "status": "PUBLISHED",
  "hook_formula": "FORMULA_NAME",
  "tweet_chars": 234,
  "article_words": 1250,
  "sections_count": 3,
  "facts_verified": "12/12",
  "quality_gates": {
    "G1_hook": true,
    "G2_structure": true,
    "G3_anti_llm": true,
    "G4_accessibility": true,
    "G5_length": true
  },
  "iceberg_max_axes": ["axis1", "axis2", "..."]
}
```

### Final Output

**OUTPUT:**

```
✅ PUBLICATION RÉUSSIE

Article publié: {article_url}
Draft ID: {draft_id}

───────────────────────────────────
TWEET PRÊT À POSTER:
───────────────────────────────────
{emoji} {hook_text}

{article_url}
───────────────────────────────────
Caractères: {count}/280

Fichiers sauvegardés:
- prompts/outputs/{date}_sujet-substack.md
- prompts/outputs/{date}_sujet-tweet.txt
- prompts/outputs/{date}_sujet-meta.json

Copier tweet dans clipboard? (Y/n)
```

---

## ⚠️ KNOWN ISSUES & FIXES

### Issue #1: Bold Text Duplication Bug (FIXED 2025-11-26)

**Symptom:** Bold text (`**text**`) gets duplicated in rendered HTML:
```
Expected: <strong>70%</strong> de sa commission
Actual:   <strong>70%</strong><span>70% de sa commission</span>
```

**Root Cause:** Substack's server-side ProseMirror renderer has a bug that sometimes duplicates marked text into the following text node.

**Fix Applied:** Zero-width space (`\u200B`) inserted after each bold/italic text node.

**Location:** `~/projects/Substack-API/draft_create.py` lines 356-359:
```python
# WORKAROUND: Add zero-width space after bold/italic to prevent Substack duplication bug
if format_type in ('strong', 'em'):
    elements.append({"type": "text", "text": "\u200B"})
```

**Result:** The ZWS breaks the pattern that triggers duplication:
```html
<strong>70%</strong>​ de sa commission  <!-- ​ = ZWS, invisible -->
```

**Verification:** Test article https://giak.substack.com/p/test-zws-fix-delete-me confirms fix works.

---

### Issue #2: Overlapping Regex Patterns (FIXED earlier)

**Symptom:** `**bold**` text matched by both `strong` and `em` patterns, causing double processing.

**Fix Applied:** Skip matches that start before current position.

**Location:** `draft_create.py` lines 326-328:
```python
# Skip overlapping matches
if start < current_pos:
    continue
```

---

## FALLBACK: API Non Disponible

```yaml
IF API unavailable:

  1. NOTIFY user:
     "⚠️ API Substack non accessible sur localhost:8000"
     "Article généré mais non publié."

  2. SAVE article locally:
     - prompts/outputs/YYYY-MM-DD_sujet-substack.md

  3. PROVIDE manual instructions:
     "Pour publier manuellement:"
     "1. Copier le contenu de {file}"
     "2. Créer nouveau post sur Substack"
     "3. Coller et publier"
     "4. Récupérer URL et créer tweet"
```

---

## FORMATTING REFERENCE

### Emojis by Hook Formula

| Formula | Emoji |
|---------|-------|
| PROVOCATIVE | ⚠️ |
| CONTRARIAN | 📊 |
| CONSEQUENCE | 💰 |
| PATTERN | 🔄 |
| EMOTIONAL | 💥 |
| REVELATION | 💣 |

### Bold Policy

```yaml
ALLOWED:
  - Key concepts: 1-4 words
  - Pivot numbers: single figure
  - Actor names: when central
  - Section titles: ## I - TITRE

FORBIDDEN:
  - Full sentences
  - More than 3 bold per section
  - Acronyms alone
```

### Number Formatting

```yaml
PERCENTAGES: "12.3%"
AMOUNTS: "123.4 Md EUR" or "X M EUR"
RANGES: "60-80"
ATTRIBUTION: "selon X (YYYY-MM-DD)"
MAX_PER_SECTION: 3 key figures
```

### Date Formatting

```yaml
ABSOLUTE: YYYY-MM-DD
NEVER: "hier", "aujourd'hui", "demain", "récemment"
```

---

## PHILOSOPHY v1.0

### Principle 1: Hook for Reach

Tweet = billboard. 235 chars to stop the scroll. Article = the content behind the billboard.

### Principle 2: Substack for Depth

Long-form content belongs on Substack, not Twitter threads. Better UX, better SEO, email subscribers.

### Principle 3: User in Control

2 checkpoints before publication. No runaway API calls.

### Principle 4: Anti-LLM Discipline

Concrete verbs, specific facts, no clichés. Sound like a journalist, not a chatbot.

### Principle 5: Automated But Supervised

API handles publication. User validates content. Best of both worlds.

---

**Version:** SUBSTACK ENGINE v1.1
**Date:** 2025-11-26
**Changelog:**
- v1.1 (2025-11-26): Added ZWS fix documentation, updated API call format, expanded meta.json template
- v1.0 (2025-11-26): Initial release

**Architecture:** Hook-First, API-Published, Interactive
**Design:** [docs/plans/2025-11-26-substack-engine-design.md](../../docs/plans/2025-11-26-substack-engine-design.md)
**Based on:** [tweet-engine-v4.0.md](tweet-engine-v4.0.md)
**API Repo:** `~/projects/Substack-API/` (contains `draft_create.py`, `api_server.py`)
