# OUTPUT TEMPLATE — Investigation + Article Format

**Version:** 2.0
**Usage:** Defines mandatory sections for investigation output and article transformation.

---

## INVESTIGATION OUTPUT (from protocol/INVESTIGATION.md §7)

### MEDIUM: 7 sections | APEX: 15 sections

| # | Section | Lang | Content | M | A |
|---|---------|------|---------|---|---|
| 1 | RÉSUMÉ EXÉCUTIF | FR | ≤500 words: what happened, who, why, unknowns | ✅ | ✅ |
| 2 | MANIPULATION_REPORT | EN | 15 symbols scored, speaker, implicit claims | — | ✅ |
| 3 | CLUSTERS | EN | Each loaded cluster: score + formula + classification | — | ✅ |
| 4 | HERMÉNEUTIQUE | FR | L1-L6 depth layers | — | ✅ |
| 5 | FORENSIC REASONING | FR | Iceberg: shown/hidden/factor + empire synthèse | — | ✅ |
| 6 | PRISME DIALECTIQUE | FR | 3 perspectives (⟐🎓/🔥⟐̅/◈◉○) force égale | — | ✅ |
| 7 | CHRONOLOGIE | FR | ≥10 events (APEX) | ✅ | ✅ |
| 8 | DOMAINES | FR | Thematic sections | ✅ | ✅ |
| 9 | RÉSEAU D'ACTEURS | FR | Network map + profiles | ✅ | ✅ |
| 10 | CHAÎNES DE CASCADE | FR | All chains quantified | ✅ | ✅ |
| 11 | CARTE DES PREUVES | EN | Sources✦✧⁇❧ + EDI + symbol scores | ✅ | ✅ |
| 12 | CARTE DIALECTIQUE | FR | Scénario A/B + tensions + wolves + impact | — | ✅ |
| 13 | PÉRIMÈTRE & LIMITES | FR | Exclusions + constraints | ✅ | ✅ |
| 14 | ÉTAT DES CONNAISSANCES | FR | KNOWN/SUSPECTED/UNKNOWN | ✅ | ✅ |
| 15 | SUSPICION SCORES | EN | Per-source suspicion + corroboration | — | ✅ |

### FILENAME format:
```
YYYY-MM-DD_HH-MM_<sujet>_INVESTIGATION.md
```

---

## ARTICLE OUTPUT (from protocol/INVESTIGATION.md §8)

### Required sections (6):

| # | Section | Language | Content |
|---|---------|----------|---------|
| 1 | ACCROCHE | French | 1 dense paragraph: 5 key facts, contrast |
| 2 | SECTIONS | French | Thematic narrative: starts with strongest fact, ends with synthesis |
| 3 | VERDICT | French | 4 matrices: qui gagne/perd/meurt/recule |
| 4 | CONCLUSION | French | 1 sentence capturing entire case |
| 5 | BIBLIOGRAPHIE | French | Numbered, with URLs and dates |
| 6 | DISCLAIMER | French | What excluded, why, what needs follow-up |

### FILENAME format:
```
YYYY-MM-DD_HH-MM_<sujet>_ARTICLE.md
```

---

## TL;DR FORMAT (for investigation summary)

| Line | Content | Max Chars |
|------|---------|-----------|
| 1 | **SUJET**: What is being investigated | 80 |
| 2 | **VÉRIFICATION**: Key finding (confirmed/rejected) | 80 |
| 3 | **MANIPULATION**: Main technique from Phase 0 | 80 |

---

## SOFT CHECKS (advisory, do not block)

- [ ] All sources verified
- [ ] Primary sources (◈) confirmed
- [ ] No source detected as fake news
- [ ] Source links functional
- [ ] Detailed calculations shown (no bullshit math)

---

## VALIDATION GATES

| Gate | Required | Check |
|------|----------|-------|
| TEXT_ANALYSIS executed | YES | MANIPULATION_REPORT present |
| MANIPULATION_REPORT complete | YES | All 15 symbols scanned |
| MnemoLite search | YES | N memories found |
| MnemoLite saved | YES | ID recorded |
| Clusters loaded | YES | Threshold files loaded |
| SYMETRIC if accusation | YES | Accusator checked |
| CRÉDO questions | ≥12 | Query-ready format |
| FACT_REGISTRY complete | YES | ✦✧⁅⁂ + ⊕⊗⊙ |
| CAUSALITY_CHAINS built | ≥3 for APEX | Chains with ≥3 links |
| IMPACT_VERDICT all 4 | YES | Qui gagne/perd/meurt/recule |
| CROSS_VERIFICATION | ≥2 domains | Domain-specific check |
| INVESTIGATION_OUTPUT | 9 sections | All sections present |
| EDI calculated | YES | Score with BIAS |
| Severity calculated | YES | Gap analysis |
| COUNTERMEASURES | IF gaps | Explicit actions |

**IF ANY FAIL → BLOCK & RETURN to indicated phase**

---

## DATA STORAGE

**Investigation:** Save to MnemoLite with:
- title: "[INVESTIGATION] {subject} - {date}"
- memory_type: investigation
- tags: themes + keywords
- embedding_source: structured summary

**Article:** Save to `articles/` directory with filename format above.

---

_Version 2.0 — Output format for investigations and articles_
_Referenced by: KERNEL.md §4, protocol/INVESTIGATION.md §7-§8_
