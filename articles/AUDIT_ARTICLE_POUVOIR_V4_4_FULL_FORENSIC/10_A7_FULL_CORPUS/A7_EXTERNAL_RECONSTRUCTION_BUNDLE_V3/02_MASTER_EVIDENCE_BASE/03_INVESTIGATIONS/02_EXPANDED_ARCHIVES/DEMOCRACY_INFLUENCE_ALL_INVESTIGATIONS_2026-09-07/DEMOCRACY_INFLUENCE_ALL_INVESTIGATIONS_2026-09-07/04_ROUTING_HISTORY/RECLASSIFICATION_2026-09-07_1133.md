---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "routing_reclassification"
artifact_id: "RECLASSIFICATION-2026-09-07-1133"
version: "1.0"
status: "applied"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
selected: "INV-044"
---

<!-- TRACE: after=INV-100_CLOSED; policy=CORE_INGERENCE_ROUTING_2026-09-06_v1.1-kiss -->
<!-- DECISION: top_tie=INV-044,INV-054; tie_break=canonical_order; select=INV-044; transition=BACKLOG->READY; launch=false -->
<!-- GATE: INV-044 feeds=INV-040,INV-144; INV-054 feeds=INV-052,INV-129; all four feed=INV-133 -->

# Reclassification post-INV-100 — 2026-09-07 11:33 Europe/Paris

## Material change

`INV-100` est `CLOSED / DELIVERY_PASS_R3P1`. Son résultat ferme le socle juridico-probatoire sur l'annulation/neutralisation électorale et réduit le gain marginal d'`INV-143` : le timing préélectoral reste distinct et matériel, mais il n'introduit plus à lui seul un nouveau modèle de qualification.

La priorité revient donc aux constituants qui ferment simultanément des branches vers `INV-133`.

## Pool de tête matérialisé

Ordre : `model_change > discrimination > dependency_unlock > coverage_gap > utility`.

| INV | CORE class | model_change | discrimination | dependency_unlock | coverage_gap | utility | décision |
|---|---|---|---|---|---|---|---|
| INV-044 | B/C/E | MEDIUM | HIGH | HIGH | HIGH | HIGH | **SELECT** |
| INV-054 | D/E | MEDIUM | HIGH | HIGH | HIGH | HIGH | TIED |
| INV-045 | C/E | MEDIUM | HIGH | HIGH | MEDIUM | HIGH | HOLD |
| INV-079 | B/E | MEDIUM | HIGH | HIGH | MEDIUM | HIGH | HOLD |
| INV-080 | C/D/E | MEDIUM | HIGH | HIGH | MEDIUM | HIGH | HOLD |
| INV-143 | D | MEDIUM | HIGH | LOW | HIGH | HIGH | HOLD |
| INV-141 | B | MEDIUM | HIGH | LOW | HIGH | HIGH | HOLD |
| INV-142 | B | MEDIUM | HIGH | LOW | HIGH | HIGH | HOLD |
| INV-024 | B/D | MEDIUM | HIGH | LOW | HIGH | HIGH | HOLD |

## Tie-break

`INV-044` et `INV-054` ont une clé ordinale strictement identique.

- `INV-044` alimente `INV-040` et `INV-144`;
- `INV-054` alimente `INV-052` et `INV-129`;
- les quatre synthèses sont des dépendances directes d'`INV-133`.

Il n'existe donc pas de supériorité épistémique démontrée entre les deux au niveau du routage courant. Conformément à la politique active, l'ordre canonique du registre sert uniquement de tie-break opérationnel : `INV-044` précède `INV-054`.

## Pourquoi INV-044 reste matériel

La question n'est pas de prouver une « machine de censure » par empilement d'organismes. Elle est de reconstruire des arêtes testables :

`mandat/base juridique -> budget/contrat/subvention -> organisme/intermédiaire -> information/signalement -> action éventuelle -> recours/correction -> effet`

Le dossier peut donc départager plusieurs modèles concurrents : coordination de défense légitime, gouvernance informationnelle distribuée, délégation à des intermédiaires, ou expansion bureaucratique/industrielle. Aucune de ces hypothèses n'est présumée.

## Run-contract repair

La ligne legacy d'`INV-044` n'avait ni `object_question` ni `scope`. Ces deux champs sont ajoutés avant `READY`; aucun claim factuel n'est ajouté.

Gardes :

```text
anti_FIMI != censorship
funding != command
coordination != control
participation != capture
flagging != removal
content_action != political_effect
budget_growth != fabricated_threat
institutional_network != coherent_architecture
```

## Transition

```text
INV-044 BACKLOG -> READY
ACTIVE = NONE
LAUNCH = NO
```

Prochain baby-step : `run-card INV-044`, puis lancement seulement si le gate passe.
