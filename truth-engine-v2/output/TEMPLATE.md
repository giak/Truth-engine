# OUTPUT TEMPLATE v2.1 — Investigation and article

This file alone defines delivered section sets and filenames. Gates live in `forensic/GATES.md`; statuses in `definitions/SYMBOLS.md`; save order in KERNEL.

## §1 Investigation levels

### SIMPLE — exactly 5 core sections

1. RÉSUMÉ EXÉCUTIF
2. CHRONOLOGIE
3. DOMAINES
4. CARTE DES PREUVES
5. PÉRIMÈTRE & LIMITES

### MEDIUM — exactly 7 core sections

1. RÉSUMÉ EXÉCUTIF
2. CHRONOLOGIE
3. DOMAINES
4. RÉSEAU D’ACTEURS
5. CHAÎNES / PELOTE
6. CARTE DES PREUVES
7. PÉRIMÈTRE & LIMITES

### COMPLEX — exactly 8 core sections

MEDIUM + `CARTE DIALECTIQUE` after `CHAÎNES / PELOTE`.

### APEX — exactly 15 core sections

| # | Section | Required content |
|---:|---|---|
| 1 | RÉSUMÉ EXÉCUTIF | bounded answer, decisive facts, actors, impact, main gaps |
| 2 | MANIPULATION_REPORT | 15 scores, observations, assumptions, loaded clusters |
| 3 | CLUSTERS | inputs, diagnostic result, competing explanation, gap |
| 4 | HERMÉNEUTIQUE | L1–L6, facts separated from inference |
| 5 | FORENSIC REASONING | shown/omitted/reconstruction or NOT APPLICABLE |
| 6 | PRISME DIALECTIQUE | dominant, strongest critical, evidence arbitration |
| 7 | CHRONOLOGIE | sourced relevant events; no forced count |
| 8 | DOMAINES | thematic findings and cross-domain boundaries |
| 9 | RÉSEAU D’ACTEURS | typed sourced edges, centrality only if computed |
| 10 | CHAÎNES / PELOTE | typed causal links, alternatives, coverage and gaps |
| 11 | CARTE DES PREUVES | CLAIM/FACT_REGISTRY, source roles, contradictions, EDI |
| 12 | CARTE DIALECTIQUE | scenarios, tensions, impact and responsibility map |
| 13 | PÉRIMÈTRE & LIMITES | inclusions, exclusions, access/method limits |
| 14 | ÉTAT DES CONNAISSANCES | known/probable/claimed/hypotheses/contested/unknown/refuted |
| 15 | SUSPICION / VÉRIFICATION | source audits, upgrades/downgrades, unresolved checks |

`SOURCES` and `REQUEST_LOG` are mandatory appendices for every factual investigation and do not change the core section count.

## §2 Content rules

- French output, dense and factual; one sentence = one bounded claim.
- Put specific clickable citations next to material claims. `✦` always has a claim-relevant URL.
- Display canonical epistemic status for facts, causal links and responsibility claims.
- Required but unsupported content is `UNKNOWN`, `NONE ESTABLISHED` or `NOT APPLICABLE` with reason.
- Preserve material contradiction; do not smooth it into a synthetic verdict.
- Include formula inputs when a score/metric is reported; otherwise `NOT COMPUTABLE`.
- Persist REQUEST_LOG write/article/writeback rows as `PENDING_AT_SERIALIZATION` per its lifecycle contract.

## §3 TL;DR

```text
SUJET: {scope}
VÉRIFICATION: {strongest bounded finding + status}
MANIPULATION/STRUCTURE: {main diagnostic, explicitly non-verdict}
LIMITE: {largest unresolved gap}
```

## §4 Article — step 15, exactly 6 sections

1. ACCROCHE — strongest confirmed contrast; no unsupported certainty.
2. SECTIONS THÉMATIQUES — evidence-led narrative.
3. IMPACT — gains/losses/deaths/retreats only where established.
4. CONCLUSION — answer within verified scope.
5. BIBLIOGRAPHIE — numbered specific URLs and access/publication dates.
6. LIMITES / DISCLAIMER — unknowns, contested claims and follow-up.

The article may improve readability but cannot upgrade statuses, omit decisive contradictions or merge hypotheses with facts.

## §5 Filenames

```text
YYYY-MM-DD_HH-MM_{SUBJECT_SLUG}_INVESTIGATION.md
YYYY-MM-DD_HH-MM_{SUBJECT_SLUG}_INVESTIGATION_PART1.md
YYYY-MM-DD_HH-MM_{SUBJECT_SLUG}_INVESTIGATION_PART2.md
YYYY-MM-DD_HH-MM_{SUBJECT_SLUG}_ARTICLE.md
```

Use the single-file investigation name at ≤50000 chars; PART1/PART2 only above that threshold.

_Canonical authority: output structure and filenames._
