---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "control_audit"
artifact_id: "REFOCUS-AUDIT-2026-09-08"
version: "1.0"
status: "applied"
updated: "2026-09-08"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
policy_ref: "INVESTIGATION_ORCHESTRATOR.md"
---

<!-- TRACE: audit_scope=routing_drift+current_READY+INV133_dependency_pressure -->
<!-- DECISION: revoke_INV119_READY=true; mass_defer=false; certified_runs_immutable=true -->

# Recentrage du programme — audit et correction

## Verdict après double-check

Le diagnostic de dérive est **confirmé avec correction** :

- `INV-119` n'est pas une investigation intrinsèquement hors sujet ; reproduction/circulation des élites peut devenir pertinente si une arête vers accès, sélection, capture ou décision est démontrée.
- En revanche, son statut `READY` courant n'était pas suffisamment justifié par une reclassification **full-pool mission-first**. Les traces montrent une sélection dans un *current cohort* hérité, après un tie avec `INV-078`, puis sa promotion comme dernier item du cohort après fermeture d'`INV-144`.
- `dependency_unlock` n'est donc pas l'unique faute. Le défaut plus fondamental est l'absence d'un `CORE_MISSION_GATE` mécaniquement défini et l'héritage de cohort entre cycles.
- `INV-144` n'était pas en soi une dérive : l'économie de la contre-ingérence traite directement un mécanisme de qualification/réponse publique et ses incitations. Sa fermeture n'est pas annulée.

## Vérifications factuelles

État avant patch :

```text
TOTAL=146
CLOSED=46
BACKLOG=76
BLOCKED=9
CONDITIONAL=7
MERGED=6
DEFERRED=1
READY=1 (INV-119)
TE_ACTIVE=0
```

`INV-133` a 8 dépendances directes ouvertes et **36 dépendances transitives ouvertes** dans le registre courant :

```text
INV-038 INV-040 INV-041 INV-042 INV-043 INV-046 INV-047 INV-048
INV-051 INV-052 INV-053 INV-057 INV-058 INV-059 INV-061 INV-062
INV-063 INV-064 INV-065 INV-066 INV-067 INV-068 INV-088 INV-089
INV-090 INV-091 INV-095 INV-102 INV-104 INV-106 INV-107 INV-111
INV-112 INV-119 INV-130 INV-131
```

Ce volume explique la pression du DAG, mais ne prouve pas que ces 36 investigations doivent toutes être exécutées pour satisfaire la mission centrale.

Le `control.py` pré-patch :

- validait `READY/TE_ACTIVE`, `object_question`, `scope` et l'invariant d'unicité ;
- ne vérifiait aucun gate mission-current pour un `READY` ;
- affichait seulement la chaîne `CORE_MISSION_GATE -> model_change > discrimination > dependency_unlock > coverage_gap > utility` dans le dashboard ;
- autorisait une synthèse dès `status=BACKLOG + gate=DEPENDENCIES_DONE + deps CLOSED`, donc sans sélection mission-first explicite.

## Correction minimale appliquée

1. création de `INVESTIGATION_ORCHESTRATOR.md v2.0-kiss` ;
2. `CORE_MISSION_V2` hard gate avant tout ranking ;
3. mécanisme-first / acteur-second ;
4. full-pool obligatoire après chaque fermeture/changement matériel ;
5. interdiction d'hériter automatiquement d'un cohort ;
6. classement :
   `model_change > discrimination > effect_closure > symmetry_value > dependency_unlock > coverage_gap > utility` ;
7. synthèse débloquée != synthèse automatiquement prioritaire ;
8. `control.py` refuse désormais un `READY/TE_ACTIVE` sans gate `CORE_MISSION_V2_SELECTED_*` ;
9. `control.py synthesis-card` exige une sélection explicite `CORE_MISSION_V2_SYNTHESIS_SELECTED_*` ;
10. `INV-119 READY -> BACKLOG`, sans run et sans modification probatoire ;
11. aucun mass-defer du backlog ; réévaluation au prochain full-pool seulement.

## État après patch

```text
READY=0
TE_ACTIVE=0
INV-119=BACKLOG / NOT_RUN
NEXT=full-pool CORE_MISSION_V2 reclassification
```

## Non-régression

- `python3 -m py_compile control.py` : PASS
- `python3 control.py validate` : PASS
- `control.py run-card INV-119` : refus attendu (`status=BACKLOG`)
- aucun artefact Truth Engine certifié n'a été réécrit.
