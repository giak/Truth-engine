---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-066"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-065;INV-121"
updated: "2026-09-09"
---

# RUN_HANDOFF — INV-066

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260909-1800-research-funding-agenda-independence`
- Deliverable: `INV-066_INVESTIGATION.md`
- Deliverable SHA-256: `cc621f6ff8b6bb97895c632fb6228b27b4fa09dbf62c67979cebc6bc7f7fb8ad`
- Corpus runtime: `QRY=36 / SRC=18 / FCT=27 / provenance_families=5`
- Persistence: `PASS / eligible=27 / blocked=27 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

INV-066 établit une frontière causale plus précise que « le financeur contrôle la science ». Le financement public peut orienter explicitement l’agenda de recherche par les priorités, programmes et appels, tandis que des dispositifs bottom-up comme l’ERC fournissent un contre-modèle direct à l’idée d’un contrôle thématique inhérent au financement public. Dans les partenariats public-privé et la recherche sponsorisée, le corpus documente des points de contrôle matériels — gouvernance d’agenda, design, analyse, écriture, propriété des données et droits de publication — ainsi qu’une association agrégée avec des conclusions plus favorables au sponsor dans certains domaines. Mais les contre-exemples et résultats nuls réfutent la proposition universelle « financement -> résultat dicté ». Le modèle retenu distingue donc agenda-setting, capacité de contrôle du processus, biais/conclusions observés et contrôle effectif d’un résultat ; ces arêtes doivent être démontrées séparément. Les règles d’open science, de publication des essais et de transparence financière améliorent l’auditabilité sans prouver l’indépendance ni mesurer à elles seules la réduction du biais.

## Registre causal certifié

- `public strategic priority -> programme/call budget structure -> changed opportunity set and topic distribution` = **SUPPORTED** — Agenda steering changes funded opportunity structures; it does not establish direction of scientific findings.
- `joint Commission-industry agenda governance -> SRIA/topic formation -> IHI call agenda` = **SUPPORTED** — The closed edge is topic/call co-governance, not control of project findings or downstream policy.
- `sponsor involvement in design/analysis/writing -> increased control over research process -> association with sponsor-favorable conclusions` = **SUPPORTED** — Observational meta-research does not randomly assign sponsor involvement and cannot isolate all confounding or selection mechanisms.
- `data ownership/publication constraints -> capacity to delay suppress or selectively report research output` = **UNRESOLVED** — Contractual capacity is documented; actual selective suppression attributable to these clauses was not measured in the inspected cohort.
- `open-science/trial-reporting/disclosure rules -> greater public observability -> potential constraint on selective opacity` = **SUPPORTED** — Greater observability is established by rule; reduction of sponsorship bias is not measured here.

## Gaps matériels certifiés

- `CLM-004` / **CAUSALITY** — Observed sponsorship associations do not isolate which sponsor mechanism causes each favorable result or conclusion.
- `CLM-007` / **CAUSALITY** — No inspected design identifies the marginal effect of these transparency regimes on sponsor-induced bias across France or the EU.

## RENARD

`NO`

## Reclassification

Impact direct : `INV-065;INV-121`.

## Transition attendue

`INV-066 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant après REVIEW explicite.
