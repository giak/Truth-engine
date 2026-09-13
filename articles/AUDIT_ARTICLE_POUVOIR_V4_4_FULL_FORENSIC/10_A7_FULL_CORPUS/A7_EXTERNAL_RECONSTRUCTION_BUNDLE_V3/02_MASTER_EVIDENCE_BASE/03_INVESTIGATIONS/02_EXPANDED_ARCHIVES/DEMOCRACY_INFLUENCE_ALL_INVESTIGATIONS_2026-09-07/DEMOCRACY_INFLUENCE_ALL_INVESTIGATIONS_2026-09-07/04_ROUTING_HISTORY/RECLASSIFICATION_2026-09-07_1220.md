---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "routing_reclassification"
artifact_id: "RECLASSIFICATION-2026-09-07-POST-INV044"
version: "1.0"
status: "applied"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
selected: "INV-054"
---

<!-- TRACE: after=INV-044_CLOSED; policy=CORE_INGERENCE_ROUTING_2026-09-06_v1.1-kiss -->
<!-- DECISION: top_tie=INV-054,INV-093; tie_break=canonical_order; select=INV-054; transition=BACKLOG->READY -->
<!-- GATE: INV-054 feeds=INV-052,INV-129; INV-093 feeds=INV-095,INV-102; all four feed=INV-133 -->

# Reclassification post-INV-044 — 2026-09-07 12:20 Europe/Paris

## Material change

INV-044 est `CLOSED / DELIVERY_PASS_R3P1`. Il alimente INV-040 et INV-144, mais ces synthèses gardent respectivement sept et trois constituants ouverts. Le meilleur rendement immédiat reste donc de fermer des constituants qui alimentent plusieurs branches directes d'INV-133.

## Pool de tête matérialisé

Ordre : `model_change > discrimination > dependency_unlock > coverage_gap > utility`.

| INV | CORE class | model_change | discrimination | dependency_unlock | coverage_gap | utility | décision |
|---|---|---|---|---|---|---|---|
| INV-054 | D/E | MEDIUM | HIGH | HIGH | HIGH | HIGH | **SELECT** |
| INV-093 | D/E | MEDIUM | HIGH | HIGH | HIGH | HIGH | TIED |
| INV-094 | D/E | MEDIUM | HIGH | HIGH | HIGH | HIGH | HOLD / child of INV-093 |
| INV-045 | C/E | MEDIUM | HIGH | HIGH | MEDIUM | HIGH | HOLD |
| INV-079 | B/E | MEDIUM | HIGH | HIGH | MEDIUM | HIGH | HOLD |
| INV-085 | C/E | MEDIUM | HIGH | HIGH | MEDIUM | HIGH | HOLD |
| INV-143 | D | MEDIUM | HIGH | LOW | HIGH | HIGH | HOLD |
| INV-141 | B | MEDIUM | HIGH | LOW | HIGH | HIGH | HOLD |
| INV-142 | B | MEDIUM | HIGH | LOW | HIGH | HIGH | HOLD |

## Tie-break

INV-054 et INV-093 ont la même clé ordinale. Chacun alimente deux synthèses directes ou en chaîne vers INV-133. Aucune supériorité épistémique n'est démontrée au niveau du routage courant ; l'ordre canonique sert seulement de tie-break opérationnel. INV-094 reste derrière son investigation parente INV-093 pour ne pas inverser la logique générale/cas.

## Contrat minimal INV-054

Chaîne testée :

`contentieux/objectif -> financement/gouvernance -> coordination éventuelle -> acte de procédure -> décision -> mise en œuvre -> changement institutionnel -> effet politique durable`

Gardes :

```text
strategic_litigation != abuse
funding != command
legal_support != tasking
access_to_court != control_of_outcome
judicial_win != implementation
implementation != durable_political_effect
shared_values != coordinated_campaign
lawful_advocacy != illegitimate_interference
```

## Transition

```text
INV-054 BACKLOG -> READY
ACTIVE = NONE
```
