# REQUEST LOG — Standard Format for Investigation Reports

## Purpose

Standardize research presentation in APEX reports for transparency and reproducibility.

---

## Table Structure

| # | TYPE | QUERY | RÉSULTAT | SOURCE |
|---|------|-------|----------|--------|
| 1 | ◈ | [requête] | [extrait clé] | [nom source] |
| 2 | ◉ | [requête] | [extrait clé] | [nom source] |

## Column Definitions

### # (Numéro)
- Sequential query number per branch
- Starts at 1 for each branch
- Enables cross-references in justifications

### TYPE (Source Type)
- ◈ PRIMARY: Leak, FOIA, court docs, data
- ◉ SECONDARY: Investigative journalism, academic research
- ○ TERTIARY: MSM, aggregators, official
- Mandatory field for EDI stratification

### QUERY (Requête)
- Exact query text (French or subject language)
- Include branch-specific keywords
- Valid examples: "Prévalence DNC Occitanie Jan 2026", "Importations œufs Ukraine Jan 2026"

### RÉSULTAT (Résultat)
- Key extract from results (max 200 chars)
- Prioritize verifiable factual information
- Valid examples: "Rapport préfectoral: 3 foyers suspectés à Léran", "Douanes EU: +412% vs 2025"

### SOURCE (Source)
- Full source name (not just domain)
- Include specifics: Archives départementales Ariège, Données CNPO, Médiapart, Journal officiel
- Invalid (too vague): "Site internet", "Article de presse"

---

## Branch Grouping

Queries grouped by investigation branch:

### BRANCH 1: [Name] (X queries)

| # | TYPE | QUERY | RÉSULTAT | SOURCE |
|---|------|-------|----------|--------|

### BRANCH 2: [Name] (X queries)

| # | TYPE | QUERY | RÉSULTAT | SOURCE |
|---|------|-------|----------|--------|

---

## Final Count

At end of REQUEST LOG, add source count summary:

**📊 DÉCOMPTE RECHERCHES: ◈X ◉X ○X**

---

## Cross-Reference Integration

All analysis claims must reference corresponding query number:

> Le plan "un poulailler par département" de Genevard (requête 18) est un effet d'annonce incapable de combler le déficit de 1.2 million de pondeuses (requête 13).

---

## Investigation Protocol Header

Before the REQUEST LOG table, include protocol summary:

```markdown
**Investigation [TYPE] du [DATE]** — [SUBJECT]
- Complexité: X.X/10
- Budget requêtes: N recherches
- Modes: [activated modes]
- Phases exécutées: [L0-L9 Cascade or specific]
```

---

## Quality Gates

The REQUEST LOG is verified against:

- ✅ All searches listed (no omissions)
- ✅ Each query has source type (◈◉○)
- ✅ Each query has a result
- ✅ Each query has a valid source
- ✅ Grouped by branches
- ✅ Source stratification detail present
- ✅ Protocol header present
- ✅ Final source count present
- ✅ Cross-references in analysis

---

*REQUEST LOG v2.0 — Transparency + Reproducibility Standard*
