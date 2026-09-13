---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-145-RUN-HANDOFF"
version: "1.0"
status: "closed"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-145"
---

<!-- DERIVED_FROM: te_run=20260907-0538-inv145-recovery; review=INV-145_POST_RUN_REVIEW.md -->
<!-- DECISION: truth_engine=DELIVERY_PASS_R3P1; renard=NO; inv=CLOSED -->

# RUN_HANDOFF — INV-145

```text
INV_ID = INV-145
TE_STATUS = DELIVERY_PASS_R3P1
TE_RUN_ID = 20260907-0538-inv145-recovery
QRY = 9
SRC = 9
PROVENANCE_FAMILIES = 5
FCT = 21
CHECKPOINTS = 7
MNEMO = MNEMO_UNAVAILABLE degraded
PERSISTENCE = PASS / 21 blocked terminal outcomes
DELIVERABLE_SHA256 = 2bc95a3d85ae5b0d7abda185b350067600ca3bd8e544d10a942f157940ac0c5a
RENARD = NO
INV_STATUS = CLOSED
```

## Central delta

FARA, le dispositif français et le projet européen ne qualifient pas le même objet de transparence étrangère. L'asymétrie textuelle et de périmètre est démontrée ; une asymétrie d'enforcement fondée sur le statut allié/adversaire ne l'est pas.

## Highest supported I0..I7

```text
I0 identity/relation = VERIFIED — principal/mandant/sponsor et relations juridiques documentés
I1 resources/capability/access = VERIFIED — obligations, registres, contrôles et sanctions documentés
I2 documented action = VERIFIED — enforcement FARA et fonctionnement initial du registre français documentés
I3 coordination/tasking/control = LEGALLY_DEFINED / CASE_SPECIFIC — les textes définissent les relations, la preuve factuelle reste cas par cas
I4 exposure/reach = N/A pour le cœur juridique ; données de registre non assimilées à une mesure d'influence
I5 reception/persuasion = NOT_ESTABLISHED / hors cœur du run
I6 behavior/institutional change = NOT_COMPARABLE entre régimes avec les données actuelles
I7 counterfactual outcome = NOT_ESTABLISHED
```

## Material gaps / contradictions

- `BASELINE` : absence de fenêtre française pluriannuelle comparable avec dénominateur d'enforcement.
- `TEMPORAL` : cadre UE non final au 2026-09-07.
- `CAUSALITY` : effet dissuasif/transparence non identifié causalement entre régimes.
- Différence de droit `!=` différence illégitime `!=` application sélective.

## RENARD

`NO` — les résiduels dépendent de futures données juridiques/enforcement ou d'un design causal identifié ; recherche générique cumulative.

## New ideas triaged

```text
MERGE -> INV-146 : legal-design asymmetry control
RECHECK -> future HATVP multi-year enforcement data
RECHECK -> final EU directive/transposition/enforcement
DEFER -> matched US/France causal enforcement comparison until denominators exist
```

## Registry patch

```text
INV-145: TE_ACTIVE -> CLOSED
truth_engine: NOT_RUN -> DELIVERY_PASS_R3P1
renard: UNDECIDED -> NO
result_path: INV-145_RUN_HANDOFF.md
```
