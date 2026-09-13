---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "routing_reclassification"
artifact_id: "RECLASSIFICATION-2026-09-07-1523"
version: "1.1"
status: "applied"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
selected: "INV-093"
---

<!-- TRACE: after=INV-054_CLOSED; policy=CORE_INGERENCE_ROUTING_2026-09-06_v1.1-kiss -->
<!-- DECISION: top_tie=INV-093,INV-124; tie_break=canonical_order; select=INV-093; transition=BACKLOG->READY; launch=false -->
<!-- GATE: INV-093 feeds=INV-095,INV-102; INV-124 feeds=INV-129; all feed=INV-133 -->

# Reclassification post-INV-054 — 2026-09-07 15:23 Europe/Paris

## Material change

`INV-054` est `CLOSED / DELIVERY_PASS_R3P1`. Son delta alimente `INV-052` et `INV-129` et il sort du pool.

Le graphe complet est recalculé sous la clé publiée :

`model_change > discrimination > dependency_unlock > coverage_gap > utility`.

## Pool de tête matérialisé

| INV | CORE class | model_change | discrimination | dependency_unlock | coverage_gap | utility | décision |
|---|---|---|---|---|---|---|---|
| INV-093 | B/C/E | MEDIUM | HIGH | HIGH | HIGH | HIGH | **SELECT** |
| INV-124 | C/E | MEDIUM | HIGH | HIGH | HIGH | HIGH | TIED |
| INV-045 | C/E | MEDIUM | HIGH | HIGH | MEDIUM | HIGH | HOLD |
| INV-079 | B/E | MEDIUM | HIGH | HIGH | MEDIUM | HIGH | HOLD |
| INV-080 | C/D/E | MEDIUM | HIGH | HIGH | MEDIUM | HIGH | HOLD |
| INV-085 | C/E | MEDIUM | HIGH | HIGH | MEDIUM | HIGH | HOLD |
| INV-143 | D | MEDIUM | HIGH | LOW | HIGH | HIGH | HOLD |
| INV-141 | B | MEDIUM | HIGH | LOW | HIGH | HIGH | HOLD |
| INV-142 | B | MEDIUM | HIGH | LOW | HIGH | HIGH | HOLD |

## Tie-break

`INV-093` et `INV-124` ont une clé ordinale identique. `priority=P1/P2` n'est pas ajouté artificiellement à la clé : la politique active ne l'autorise pas comme sixième critère.

- `INV-093` alimente `INV-095` et `INV-102` ;
- `INV-124` alimente `INV-129` ;
- ces synthèses alimentent `INV-133`.

Aucune supériorité épistémique n'est démontrée par la clé courante. L'ordre canonique du registre est donc utilisé uniquement comme tie-break opérationnel : `INV-093` précède `INV-124`.

`INV-045` reste très utile et touche trois synthèses (`INV-040`, `INV-088`, `INV-144`), mais son corpus `SUBSTANTIAL_PRIOR` réduit son `coverage_gap` à MEDIUM ; il est donc derrière avant tout tie-break.

## Run-contract repair

La ligne legacy d'`INV-093` n'avait ni `object_question` ni `scope`. Les deux champs sont ajoutés avant `READY`, sans claim factuel.

Gardes :

```text
donation != loan
loan != illicit_financing
service != hidden_benefit
irregularity != fraud
rejected_or_adjusted_accounts != corruption
funding != political_command
foreign_financing != domestic_financing_mechanism
```

## Transition

```text
INV-093 BACKLOG -> READY
ACTIVE = NONE
LAUNCH = NO
```

Prochain baby-step : `run-card INV-093`, puis lancement seulement si le gate passe.
