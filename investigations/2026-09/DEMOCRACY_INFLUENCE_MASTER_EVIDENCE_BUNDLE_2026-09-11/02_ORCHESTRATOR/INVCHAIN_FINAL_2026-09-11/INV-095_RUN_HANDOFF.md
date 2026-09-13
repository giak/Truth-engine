---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-095-RUN-HANDOFF"
version: "1.0"
status: "closed"
updated: "2026-09-10"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-095"
truth_engine: "NOT_RUN_BY_DESIGN"
renard: "NO"
reclass_impact: "INV-102;INV-133"
---

<!-- DERIVED_FROM: synthesis=INV-095_SYNTHESIS.md; input_gate=INV-095_SYNTHESIS_INPUT_GATE.md -->
<!-- DECISION: truth_engine=NOT_RUN_BY_DESIGN; synthesis=PASS; renard=NO; inv=CLOSED -->

# RUN_HANDOFF — INV-095

```text
INV_ID = INV-095
TE_STATUS = NOT_RUN_BY_DESIGN / type=SYNTHESIS
SYNTHESIS_PATH = INV-095_SYNTHESIS.md
INPUT_GATE = PASS / 4 of 4 canonical terminal handoffs
P0 = 0
P1 = 0
P2 = 4
RENARD = NO
INV_STATUS = CLOSED
```

## Central delta

Le corpus fermé établit des filtres structurels distincts en amont de la compétition — financement/règles, sélection sociale et accès élitaire, concentration économique des médias et flux étrangers pouvant créer capacité ou dépendance. Il ne ferme pas la chaîne générale `ressource/réseau/propriété -> veto/nomination/exclusion d’un candidat identifiable`, et encore moins une coordination transversale entre ces mécanismes. Le modèle soutenu est celui de contraintes et opportunités inégalement distribuées pouvant se cumuler sans centre de commandement démontré ; la thèse d’un système coordonné de présélection politique reste `NOT_ESTABLISHED`.

## Highest supported edge

`filtres structurels -> capacité/accès/réseau/visibilité potentielle = SUPPORTED/PARTIAL` ; `-> sélection effective de candidat = UNRESOLVED` ; `-> résultat électoral contrefactuel = NOT_ESTABLISHED`.

## Material gaps / contradictions

- accès/visibilité ne vaut pas sélection ;
- financement, propriété ou réseau ne valent pas tasking/veto ;
- cumul de filtres ne vaut pas coordination ;
- aucun dénominateur commun de candidatures potentielles ni design causal jusqu’au résultat.

## RENARD

`NO` — upgrade seulement par données internes de nomination/sélection, tasking/veto authentifié, footprint intervention->choix de candidat, ou design causal/comparatif adéquat.

## Route

`INV-095 BACKLOG -> CLOSED`; `truth_engine=NOT_RUN_BY_DESIGN`; `renard=NO`; `result_path=INV-095_RUN_HANDOFF.md`. Débloquer `INV-102`; alimenter `INV-133`.
