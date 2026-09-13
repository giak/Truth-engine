---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "routing_policy"
artifact_id: "CORE-INGERENCE-ROUTING-2026-09-06"
version: "1.1-kiss"
status: "active"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
---

<!-- TRACE: correction=post-pilot-topic-drift; preserves=existing_lexicographic_priority -->
<!-- TRACE: control_audit=2026-09-06T21:43+02:00; stale_next_INV-128_removed=true -->
<!-- DECISION: active=NONE; ready=NONE; next=UNSELECTED; reclassify_before_launch=true -->
<!-- TRACE: post_run=INV-138_CLOSED; control_state_refreshed=2026-09-06T22:51+02:00 -->

# Core mission routing — ingérences / influence démocratique

## Diagnostic

Le backlog n'est pas dépourvu d'enquêtes d'ingérence. Le défaut observé après les pilotes était un **biais de routage** : des objets structurels utiles pouvaient battre des opérations directes parce que le tri ne contenait aucun filtre explicite de mission.

La correction reste un préfiltre, pas un nouveau score.

## CORE_MISSION_GATE

Un run est éligible au tri courant s'il relève d'au moins une classe :

```text
A DIRECT_OPERATION
B DIRECT_MECHANISM
C ATTRIBUTION_OR_QUALIFICATION_AUDIT
D ELECTION_OR_INSTITUTIONAL_INTERFERENCE_CASE
E NECESSARY_CONTROL materially unlocking/discriminating A-D
```

Ne passent pas seuls : importance politique générale, cartographie institutionnelle générique, acteur célèbre, proximité idéologique, réseau dense, financement sans mécanisme, simple suspicion.

Dans le pool éligible seulement :

```text
model_change > discrimination > dependency_unlock > coverage_gap > utility
```

## Tie-break

L'ordre canonique du registre n'est **pas** un critère épistémique.

Il peut seulement servir de tie-break opérationnel lorsque :

1. le pool éligible a été matérialisé ;
2. les cinq dimensions ci-dessus ont été enregistrées pour les candidats concernés ;
3. les clés sont réellement identiques ;
4. la décision est tracée dans un artefact de reclassification courant.

Aucun lancement ne doit désormais être justifié par « tie métadonnées + ordre canonique » sans cette matérialisation.

## Invariants forensiques

```text
accusation != fait
official_statement != proof
official_denial != proof
funding != command
access != control
coordination != effect
operation_exists != result_changed
foreign != interference
legal != legitimate
opaque != illegal
convergence != architecture
```

Tout faisceau collectif doit être décomposé en liens testables. Une convergence peut justifier une enquête, jamais remplacer la preuve de ses arêtes.

## État courant

```text
LAST_CLOSED = INV-138
ACTIVE = NONE
READY = NONE
NEXT = UNSELECTED
RECLASSIFY_BEFORE_LAUNCH = YES
```

Les enquêtes `INV-128`, `INV-134`, `INV-135`, `INV-136`, `INV-137` et `INV-138` sont fermées. Le prochain choix doit être recalculé au moment du prochain lancement ; aucune priorité courante n'est figée dans ce document.
