# SUBLIMATOR v27.0 — Two-Tier Pipeline Design

**Date**: 2026-05-18
**Status**: Draft — pending review
**Trigger**: Pain points from "pourquoi-francais-ne-se-revoltent-pas" article (200+ facts, 9 sections, reactive fact-checking, vague URLs, skipped dialectic)

---

## Problem Statement

The v26.0 pipeline collapses at scale (>100 facts, >5 sections, >10 investigations):
1. **Digest unreadable** — exhaustive extraction creates massive, unnavigable documents
2. **No section→investigation mapping** — writers lose track of which investigation feeds which section
3. **Vague URLs** — sources collected at the end, often just domain names
4. **Unmanageable matrix** — 200+ facts with no routing to sections
5. **Reactive fact-checking** — sources searched during writing, not before
6. **Dialectic skipped** — §4 never applied, no theses tested
7. **All combined** — the entire pipeline breaks at this scale

---

## Architecture: Two-Tier Pipeline

### Tier 1 — Article (one pass, before any writing)
```
Census → Condensed Digest → Dialectic → Architecture → Fact-Check Plan
```
**Output**: Validated thesis, section plan, investigation→section mapping, proactive fact-check list.

### Tier 2 — Sections (iterative, one section at a time)
```
Section Digest → Section Matrix (with URLs) → Writing → Validation → Next section
```
**Output**: Each section is autonomous, sourced, verified before moving on.

---

## File Structure

```
YYYY-MM-DD_<sujet>/
├── 00_CENSUS.md              # Tier 1: investigation inventory
├── 01_DIGEST.md              # Tier 1: thesis-oriented digest (not exhaustive)
├── 02_DIALECTIQUE.md         # Tier 1: 3 theses + resistance test + cardinal thesis
├── 03_ARCHITECTURE.md        # Tier 1: revelation chain + mapping table + URLs to collect
├── 04_FACT_CHECK_PLAN.md     # Tier 1: claims to verify before writing
├── sections/                  # Tier 2: one file per section
│   ├── sec_01_<titre>.md     #   → section digest + section matrix + written text
│   ├── sec_02_<titre>.md
│   └── ...
├── 05_ARTICLE.md             # Final assembly
├── 06_SOURCES.md             # Precise URLs, categorized
└── 07_SATURATION_AUDIT.md    # Quality gate
```

---

## Tier 1 Workflow

### Step 1: CENSUS (00_CENSUS.md)
- Quick inventory: name, size, type, dominant theme
- No exhaustive extraction. Just: "this dossier is about X, this one about Y"
- Output: 5-column table max

### Step 2: CONDENSED DIGEST (01_DIGEST.md)
- **Thesis-oriented digest**, not exhaustive v26.0 style
- Extract facts that can form an argumentation
- Format: by theme, 10-20 facts max per theme, numbered D###
- Noise facts marked `[BRUIT]` (ignored for thesis building)
- **Rule**: if a fact doesn't serve a potential thesis → mark but don't prioritize

### Step 3: DIALECTIC (02_DIALECTIQUE.md)
- 3 candidate theses from digest themes
- Resistance test for each thesis
- Cardinal thesis selection
- **New**: cardinal thesis generates **one question per section** (each section answers a sub-question supporting the thesis)

### Step 4: ARCHITECTURE (03_ARCHITECTURE.md)
- Revelation chain (classic)
- **New mandatory**: Mapping Table
```
| Section | Investigations sources | Key facts (D###) | URLs to collect | Status |
|---------|----------------------|-------------------|-----------------|--------|
| §1 Paradoxe | inv_A, inv_B | D001, D005, D012 | INSEE, OCDE, CEVIPOF | □ |
| §2 Peur | inv_C, inv_D | D023, D034, D045 | Légifrance, Amnesty | □ |
```
- For each section: list of precise URLs to collect BEFORE writing
- Fact-checking plan: which claims are "at risk" and must be verified

### Step 5: FACT-CHECK PLAN (04_FACT_CHECK_PLAN.md)
```
| Claim | Current source | Verification needed | Target URL | Status |
|-------|---------------|---------------------|------------|--------|
| TAJ 65M files | inv_C | Confirm CNIL 2025 | cnil.fr/... | □ |
| PISA 21% variance | inv_E | Confirm OECD | oecd.org/pisa | □ |
```

### Checkpoint #1 (after Tier 1)
```
〔VERIFICATION NEEDED #1 : Tier 1 complete ?〕

Cardinal thesis: [formulation]
Sections planned: {N}
Investigation→section mapping: □
Fact-check plan: {N} claims to verify
URLs to collect: {N}

□ Thesis solid?
□ Mapping complete?
□ Ready for Tier 2?

[WAIT FOR RESPONSE BEFORE CONTINUING]
```

---

## Tier 2 Workflow (per section)

### Step T2.1: Section Digest
- Extract ONLY facts from global digest relevant to this section
- File: `sections/sec_01_<titre>.md`
- Header:
```markdown
# Section 01 : [Title]
Answers: [thesis question]
Source investigations: [list]
Facts mobilized: [D###, D###, ...]
```

### Step T2.2: Section Matrix + URLs
- Transform D### into F### (sectional numbering, not global)
- **BEFORE writing**: collect precise URLs for every fact
- Every fact has its verified URL in the sectional matrix
```markdown
| # | Fact | Precise URL | Status |
|---|------|-------------|--------|
| F01 | TAJ 65M files | https://www.cnil.fr/fr/taj-... | ✅ |
| F02 | PISA 21% variance | https://www.oecd.org/pisa/... | ✅ |
```

### Step T2.3: Writing
- Write section with verified facts
- Organic sourcing (LOI 1)
- No F### in text
- Checkpoint #4 after each section

### Step T2.4: Validation
```
〔VERIFICATION NEEDED #4 : Section {X} ?〕

Section "[Title]" written.
Facts used: {N}/{section total}
URLs verified: {N}/{total}
Fact-checked claims: {N}/{plan}

□ Corrections?
□ Missing facts?
□ Errors?

[WAIT FOR RESPONSE]
```

**Critical rule**: NEVER move to next section until current section is validated.

---

## Final Assembly

1. Concatenate all validated sections → `05_ARTICLE.md`
2. Compile all sectional URLs → `06_SOURCES.md` (categorized PRIMARY/SECONDARY/TERTIARY + Truth Engine related)
3. Quality gate → `07_SATURATION_AUDIT.md`

---

## Key Changes from v26.0 → v27.0

| Aspect | v26.0 | v27.0 |
|--------|-------|-------|
| Digest | Exhaustive (10% ratio rule) | Thesis-oriented (10-20 facts/theme) |
| Matrix | Global (200+ facts, unmanageable) | Sectional (per section, with URLs) |
| URLs | Collected at end, often vague | Collected BEFORE writing, precise |
| Fact-checking | Reactive (during writing) | Proactive (Tier 1 plan, Tier 2 execution) |
| Dialectic | Often skipped | Mandatory Tier 1 step |
| Section routing | None | Mapping Table (investigation→section) |
| Writing | One pass, risk of compression | Iterative, one section at a time |
| Checkpoints | 5 checkpoints | 5 checkpoints + per-section URL verification |

---

## Self-Review

- [x] No placeholders or TBDs
- [x] No internal contradictions (Tier 1 feeds Tier 2 cleanly)
- [x] Scope is focused: one pipeline improvement spec
- [x] Requirements are explicit (Mapping Table, URLs before writing, sectional matrices)
- [x] File structure is clear and complete
- [x] Checkpoints are defined with exact formats
- [x] Backward compatible: v26.0 rules (LOI 1-11) still apply in Tier 2 writing
