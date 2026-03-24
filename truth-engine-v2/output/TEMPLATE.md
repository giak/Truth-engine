# OUTPUT TEMPLATE — Investigation + Article Format

**Version:** 2.0
**Usage:** Defines mandatory sections for investigation output and article transformation.

---

## INVESTIGATION OUTPUT (from protocol/INVESTIGATION.md §7)

### Required sections (9):

| # | Section | Language | Content |
|---|---------|----------|---------|
| 1 | RÉSUMÉ EXÉCUTIF | French | ≤500 words: what happened, who, why, unknowns |
| 2 | CHRONOLOGIE | French | ≥10 events: date, description, source, consequence |
| 3 | DOMAINES | French | Thematic sections: facts, actors, consequences, verification |
| 4 | RÉSEAU D'ACTEURS | French | Network map: actors, roles, centrality, connections |
| 5 | CHAÎNES DE CASCADE | French | Chains: event → consequence → consequence → endpoint |
| 6 | CARTE DES PREUVES | English | Sources ◈◉○, facts ✦✧⁅⁂, contradictions, EDI, symbols |
| 7 | VERDICT D'IMPACT | French | Qui gagne / Qui perd / Qui meurt / Qui recule |
| 8 | PÉRIMÈTRE & LIMITES | French | What excluded, why, what needs follow-up |
| 9 | ÉTAT DES CONNAISSANCES | French | CONFIRMÉ ✦ / SUSPECTÉ ✧ ⁕ / INCONNU |

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
