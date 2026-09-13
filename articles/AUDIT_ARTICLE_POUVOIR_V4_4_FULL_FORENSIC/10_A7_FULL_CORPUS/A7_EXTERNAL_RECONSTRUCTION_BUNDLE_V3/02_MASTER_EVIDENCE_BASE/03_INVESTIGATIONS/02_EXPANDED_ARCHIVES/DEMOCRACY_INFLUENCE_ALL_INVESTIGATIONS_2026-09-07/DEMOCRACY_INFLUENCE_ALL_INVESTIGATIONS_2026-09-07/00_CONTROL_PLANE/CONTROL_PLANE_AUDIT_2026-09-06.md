---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "control_plane_audit"
artifact_id: "CONTROL-PLANE-AUDIT-2026-09-06"
version: "1.0"
status: "pass_with_corrections"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
---

<!-- TRACE: audit_time=2026-09-06T21:43+02:00 -->
<!-- DECISION: certified_investigation_artifacts_modified=false -->
<!-- DECISION: corrections=stale_routing+trace_timestamp_annotation+stale_next_action_normalization+selection_guard -->

# Control-plane audit — 2026-09-06

## Verdict

```text
CONTROL_PLANE = PASS_WITH_CORRECTIONS
CERTIFIED_RUNS_MODIFIED = NO
READY = 0
TE_ACTIVE = 0
VALIDATE_BEFORE = PASS
VALIDATE_AFTER = PASS
```

Le registre est structurellement cohérent. Les défauts trouvés étaient des défauts de **suivi et de traçabilité**, pas des défauts probatoires dans les enquêtes certifiées.

## État canonique

```text
TOTAL = 146
CLOSED = 22
BACKLOG = 97
BLOCKED = 13
CONDITIONAL = 7
MERGED = 6
DEFERRED = 1
READY = 0
TE_ACTIVE = 0
```

IDs : `INV-001..INV-146`, uniques et contigus.

Runs d'investigation fermés avec DELIVERY PASS :
`INV-010 ; INV-019 ; INV-022 ; INV-023 ; INV-039 ; INV-049 ; INV-071 ; INV-081 ; INV-103 ; INV-128 ; INV-134 ; INV-135 ; INV-136 ; INV-137`

Dernier run fermé : `INV-137`.

## Contrôles de cohérence

- aucun ID dupliqué ;
- aucune dépendance vers un ID inexistant ;
- aucun `READY` ou `TE_ACTIVE` résiduel ;
- les 13 investigations `BLOCKED` ont toutes au moins une dépendance encore non `CLOSED` ;
- `control.py validate` passe avant et après correction ;
- le dashboard généré indique `no active item`.

## Corrections appliquées

### C1 — politique de routage périmée

`CORE_INGERENCE_ROUTING_2026-09-06.md` était encore `status=active` avec :

```text
NEXT = INV-128
STATUS = READY_NOT_LAUNCHED
```

alors qu'INV-128, INV-134, INV-135, INV-136 et INV-137 sont fermées.

Correction : version `1.1-kiss`, `NEXT=UNSELECTED`, `ACTIVE=NONE`, `READY=NONE`, et obligation de reclassifier avant tout prochain lancement.

### C2 — ordre temporel INV-137

Le TRACELOG et le `run_id` certifié d'INV-137 portent un composant `20:25`, alors qu'INV-136 n'est fermé qu'à `20:50`.

Correction : **aucun artefact certifié n'a été réécrit**. Une ligne `TRACE_CORRECTION` est ajoutée : le composant horaire d'INV-137 ne doit pas être utilisé comme horloge canonique inter-run. L'ordre canonique est :

```text
INV-136 CLOSED
-> INV-137 selected/launched
-> INV-137 CLOSED
```

### C3 — 90 next_action périmés

90 lignes `BACKLOG` contenaient encore « Après validation du pilote ».

Correction locale : seul `next_action` est normalisé vers le routage courant. Aucun `status`, `gate`, `priority`, `dependency`, `scope`, `mode` ou `coverage` n'a été modifié.

### C4 — garde de sélection

Le tie-break par ordre canonique avait été invoqué pour INV-136/137 sans artefact courant matérialisant les cinq dimensions de classement.

Correction prospective :

```text
CORE_MISSION_GATE
-> matérialiser le pool
-> enregistrer model_change
-> discrimination
-> dependency_unlock
-> coverage_gap
-> utility
-> seulement si égalité exacte : ordre canonique comme tie-break opérationnel
```

Les résultats d'INV-136/137 ne sont pas invalidés ; seule la justification de sélection était sous-documentée.

### C5 — doublons Library du control plane

Des copies suffixées accidentelles coexistaient avec les noms canoniques : `INVESTIGATION_REGISTRY(1).csv`, `INVESTIGATION_REGISTRY(2).csv`, `TRACELOG(1).md`, `DASHBOARD(1).md`, `CORE_INGERENCE_ROUTING_2026-09-06(1).md`, `CORE_INGERENCE_ROUTING_2026-09-06(2).md` et `CONTROL_PLANE_AUDIT_2026-09-06(1).md`.

Les copies trace/dashboard/routing étaient identiques au canonique ; `INVESTIGATION_REGISTRY(1).csv` et `INVESTIGATION_REGISTRY(2).csv` étaient des copies non canoniques du registre, dont au moins une version plus ancienne. Correction : suppression des copies suffixées, conservation d'un seul nom canonique par artefact de contrôle. Aucun artefact certifié d'investigation n'est touché.

## Dépendances bloquantes actuelles

- `INV-038` : INV-130, INV-131
- `INV-040` : INV-041, INV-042, INV-043, INV-044, INV-045, INV-046, INV-047, INV-048
- `INV-052` : INV-051, INV-053, INV-054, INV-057, INV-058
- `INV-068` : INV-059, INV-061, INV-062, INV-063, INV-064, INV-065, INV-066, INV-067, INV-085
- `INV-082` : INV-085
- `INV-088` : INV-045, INV-079, INV-089, INV-090, INV-091
- `INV-095` : INV-093, INV-094, INV-119
- `INV-102` : INV-093, INV-095, INV-098, INV-099, INV-100
- `INV-104` : INV-106, INV-107, INV-111, INV-112
- `INV-129` : INV-054, INV-080, INV-100, INV-124
- `INV-133` : INV-038, INV-040, INV-052, INV-068, INV-082, INV-088, INV-095, INV-102, INV-104, INV-129, INV-144, INV-146
- `INV-144` : INV-044, INV-045, INV-078, INV-079
- `INV-146` : INV-026, INV-033, INV-138, INV-139, INV-140, INV-145

## Prochaine transition autorisée

Aucune enquête n'est pré-sélectionnée.

Avant le prochain lancement :

1. recalculer le pool `CORE_MISSION_GATE` ;
2. matérialiser les cinq critères dans un nouvel artefact de reclassification ;
3. sélectionner une seule investigation ;
4. passer `BACKLOG -> READY -> TE_ACTIVE`.

Cette règle évite à la fois le retour au drift structurel et les tie-breaks non traçables.
