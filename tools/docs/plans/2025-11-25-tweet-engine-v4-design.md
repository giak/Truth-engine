# Tweet Engine v4.0 — Design Document

**Date**: 2025-11-25
**Status**: Approved
**Input**: Truth Engine investigation output
**Output**: Standalone tweets (MICRO/MEDIUM/LONG)

---

## 1. Overview

Tweet Engine v4.0 transforms Truth Engine investigations into viral-ready tweets with:
- **Hook-first architecture** (first 250 chars are critical)
- **3 length modes** (MICRO <100w, MEDIUM ~350w, LONG 25k chars max)
- **Integrated fact-checking** (inherited from v3.0)
- **3 user checkpoints** (validation at key stages)

**Core Philosophy**: "Stop the scroll first, then inform."

---

## 2. Architecture

```
┌─────────────────────────────────────────┐
│  MODE 0: INTERACTIVE SETUP              │
│  - User selects length (MICRO/MED/LONG) │
│  - User validates hook direction        │
│  - Clarifies tone/angle before writing  │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  LAYER 1: INVESTIGATION ANALYSIS        │
│  - Read Truth Engine logs               │
│  - Extract facts, dates, actors, numbers│
│  - Build FactLedger + AcronymLedger     │
│  - Detect controversy level             │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  LAYER 2: HOOK GENERATOR                │
│  - First 250 chars ONLY                 │
│  - 6 hook formulas (chooses best fit)   │
│  - Title: Emoji + BOLD CAPS             │
│  - → USER VALIDATES HOOK before content │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  LAYER 3: CONTENT ENGINE                │
│  - Adapts to MICRO/MEDIUM/LONG          │
│  - Inverted pyramid structure           │
│  - Consequence lines, bold policy       │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  LAYER 4: FACT-CHECK                    │
│  - Extract claims from draft            │
│  - WebSearch verification               │
│  - Flag errors, propagate corrections   │
│  - Dashboard audit trail (optional)     │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  LAYER 5: QUALITY GATES                 │
│  - Anti-LLM check                       │
│  - Acronym validation                   │
│  - Length enforcement                   │
│  - → USER FINAL VALIDATION              │
└─────────────────────────────────────────┘
```

---

## 3. Hook Generator (Layer 2)

The most critical component — decides if users click "voir plus".

### 3.1 Hook Formulas

| Formula | Pattern | Best For |
|---------|---------|----------|
| **PROVOCATIVE** | `Pourquoi personne ne parle de X ?` | Hidden scandals, ignored facts |
| **CONTRARIAN** | `On vous dit X. Les chiffres disent Y.` | Debunking narratives |
| **CONSEQUENCE** | `Votre facture augmente. Voici pourquoi.` | Direct citizen impact |
| **PATTERN** | `3 ministres. 3 versions. 0 cohérence.` | Inconsistencies, contradictions |
| **EMOTIONAL** | `187,000€/an. C'est ce que gagne X.` | Wealth gaps, injustice |
| **REVELATION** | `Document interne. Ce qu'il révèle.` | Leaks, primary sources |

### 3.2 Hook Structure

```
<emoji> **TITRE ACCROCHEUR EN MAJUSCULES** (6-10 mots)

<hook_line> (1-2 phrases, verbe d'action, effet concret)
```

**Total: ≤250 characters**

### 3.3 Selection Logic

```
IF investigation.has_primary_source → REVELATION
IF investigation.has_contradiction → PATTERN
IF investigation.controversy ≥ 7 → PROVOCATIVE
IF investigation.citizen_impact → CONSEQUENCE
IF investigation.debunks_narrative → CONTRARIAN
ELSE → EMOTIONAL (default: human angle)
```

### 3.4 User Checkpoint

```
HOOK PROPOSÉ:
{generated_hook}

Valider? (Y/n/autre angle)
```

---

## 4. Content Engine (Layer 3)

### 4.1 Length Modes

| Mode | Chars | Words | Sections | Use Case |
|------|-------|-------|----------|----------|
| **MICRO** | <500 | <100 | 0 | Pure hook, max viral potential |
| **MEDIUM** | 1500-2500 | 350-400 | 3-5 | Developed analysis |
| **LONG** | 8000-25000 | 1500-4000 | 7-9 | Full investigation synthesis |

### 4.2 Auto-Detection

```
IF facts_count < 5 → suggest MICRO
IF facts_count 5-12 → suggest MEDIUM
IF facts_count > 12 → suggest LONG
User can override.
```

### 4.3 Structure Templates

**MICRO** (no sections):
```
<hook>
<1-2 bullet points with 👉>
<verdict line>
```

**MEDIUM** (3-5 sections):
```
<hook>
──────────────────────────────────
**I - SECTION TITLE**
<2-3 paragraphs, facts, consequences>
👉 Consequence: ...
──────────────────────────────────
[repeat sections]
**CONCLUSION**
```

**LONG** (7-9 sections): Same as MEDIUM but deeper, with:
- More facts per section
- QA blocks if needed
- Problem→Solution pairs in conclusion

### 4.4 Truth Engine Integration

**Adaptive perspective display**:
- **Clear verdict** → Focus on conclusion, brief mention of other views
- **Complex/contested** → More pedagogical, show multiple perspectives explicitly

---

## 5. Fact-Check Layer (Layer 4)

### 5.1 Process

```
1. EXTRACT from draft:
   - Numbers: €, %, millions, milliards
   - Dates: YYYY-MM-DD, "janvier 2024"
   - Names: persons, organizations
   - Claims: "vote CONTRE", "acquiert", "dénonce"

2. VERIFY via WebSearch (parallel):
   FOR each extraction:
     Query: "{fact} {context}"
     IF confirmed → ✅
     IF contradicted → ❌ + correct value
     IF no source → ⚠️ flag

3. CORRECT if errors found:
   - Fix in draft
   - Propagate to source investigation (optional)
   - Log in audit trail

4. OUTPUT table:
   | Fait | Recherche | Source | Statut |
   |------|-----------|--------|--------|
```

### 5.2 User Checkpoint

```
FACT-CHECK TERMINÉ:
- ✅ Confirmés: 8/10
- ❌ Corrigés: 2/10
- ⚠️ Non vérifiables: 0/10

Corrections appliquées. Continuer? (Y/voir détails)
```

---

## 6. Quality Gates (Layer 5)

### 6.1 Gates

| Gate | Check | FAIL Action |
|------|-------|-------------|
| **G1 - Structure** | Title present, sections formatted, no code blocks | Auto-fix formatting |
| **G2 - Acronyms** | All expanded at first use, no fabrication | Flag + ask user |
| **G3 - Anti-LLM** | No banned phrases, concrete verbs, no clichés | Auto-rewrite flagged phrases |
| **G4 - Accessibility** | No full sentences bold, no ALL CAPS body, short paragraphs | Auto-fix |
| **G5 - Length** | Within mode limits (MICRO/MEDIUM/LONG) | Compress or expand |

### 6.2 Banned Phrases

```
"au cœur de", "à l'aune de", "force est de constater",
"plus que jamais", "il convient de noter", "on sait que",
"tout le monde dit", "il est clair que", "à la croisée des chemins",
"de tout temps", "par essence", "dans ce contexte"
```

### 6.3 Preferred Verbs

```
décide, annonce, vote, signe, sanctionne, finance,
retarde, abroge, suspend, publie
```

### 6.4 Final User Checkpoint

```
QUALITY GATES: ✅ ALL PASS

TWEET FINAL:
{full_tweet}

───────────────────
Chars: 2,450/25,000
Words: 387
Sections: 5
Facts verified: 10/10
───────────────────

Publier? (Y/edit/regenerate)
```

---

## 7. Formatting Rules (Preserved from DSL)

### 7.1 Emojis

| Emoji | Usage |
|-------|-------|
| ⚠️ | Warning/alert hooks |
| 📊 | Statistics, data |
| 👉 | Consequence lines |
| 💣 | Revelations, bombshells |
| 🎯 | Conclusions, verdicts |
| ⚖️ | Balance, arbitrage |

### 7.2 Bold Policy

- **Segments**: 1-4 words only
- **Per section**: 0-3 bold segments max
- **Never**: Full sentences in bold
- **Never**: Bold + italic combined

### 7.3 Acronym Discipline

- **First occurrence**: `Nom complet (ACR) - définition courte`
- **Subsequent**: ACR alone
- **No fabrication**: If expansion not in source, mark `*non établi*`
- **No glossary block**: All expansions inline

### 7.4 Consequence Lines

```
👉 Consequence: [1 phrase, ≤22 mots, angle explicite]
```

Angles: citoyen | budget public | gouvernance | légal | sécurité | industrie

---

## 8. User Commands

| Command | Action |
|---------|--------|
| `Mode TWEET: logs/investigation.md` | Start tweet generation (auto-detect length) |
| `Mode TWEET MICRO: logs/...` | Force MICRO length |
| `Mode TWEET MEDIUM: logs/...` | Force MEDIUM length |
| `Mode TWEET LONG: logs/...` | Force LONG length |

---

## 9. Complete Flow Example

```
USER: Mode TWEET: logs/2025-11-25_reichstadt-refus-debat.md

┌─ MODE 0: SETUP ─────────────────────────────┐
│ Reading investigation...                     │
│ Facts detected: 8                            │
│ Controversy level: 7/10                      │
│ Suggested mode: MEDIUM                       │
│                                              │
│ Confirmer MEDIUM? (Y/micro/long)             │
└──────────────────────────────────────────────┘

USER: Y

┌─ HOOK GENERATION ───────────────────────────┐
│ Formula selected: PROVOCATIVE (controversy≥7)│
│                                              │
│ HOOK PROPOSÉ:                                │
│ ⚠️ **REICHSTADT REFUSE LE DÉBAT PUBLIC**    │
│                                              │
│ Le fact-checker qui juge tout le monde       │
│ refuse d'être jugé. Quand on lui propose     │
│ un débat contradictoire, il fuit.            │
│                                              │
│ Valider? (Y/n/autre angle)                   │
└──────────────────────────────────────────────┘

USER: Y

┌─ CONTENT + FACT-CHECK ──────────────────────┐
│ Generating 5 sections...                     │
│ Fact-checking 8 claims...                    │
│                                              │
│ FACT-CHECK: ✅ 8/8 confirmés                 │
│ Continuer? (Y/voir détails)                  │
└──────────────────────────────────────────────┘

USER: Y

┌─ QUALITY GATES ─────────────────────────────┐
│ G1 Structure: ✅                             │
│ G2 Acronyms: ✅                              │
│ G3 Anti-LLM: ✅                              │
│ G4 Accessibility: ✅                         │
│ G5 Length: ✅ (2,180 chars)                  │
│                                              │
│ TWEET FINAL:                                 │
│ {full tweet displayed}                       │
│                                              │
│ Publier? (Y/edit/regenerate)                 │
└──────────────────────────────────────────────┘

USER: Y

OUTPUT: Tweet ready for publication
```

---

## 10. Next Steps

1. **Implementation**: Create `prompts/systems/tweet-engine-v4.0.md`
2. **Testing**: Test with 3-5 existing investigations
3. **Iteration**: Refine hook formulas based on engagement data

---

**Version**: 4.0
**Architecture**: Hook-First, Fact-Checked, Interactive
**Philosophy**: Stop the scroll first, then inform.
