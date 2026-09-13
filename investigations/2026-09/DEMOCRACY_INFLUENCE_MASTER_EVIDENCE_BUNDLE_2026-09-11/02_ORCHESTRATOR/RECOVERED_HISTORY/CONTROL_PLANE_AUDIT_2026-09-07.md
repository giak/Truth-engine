---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "control_plane_audit"
artifact_id: "CONTROL-PLANE-AUDIT-2026-09-07-1916"
version: "1.0-kiss"
status: "pass_with_corrections"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
---

<!-- TRACE: audit_time=2026-09-07T19:16+02:00; checkpoint=post-INV-093 -->
<!-- DECISION: certified_investigation_artifacts_modified=false -->
<!-- DECISION: corrections=dashboard_observability+routing_state_boundary+snapshot_integrity+README_tracking -->

# Control-plane audit — 2026-09-07 19:16 Europe/Paris

## Verdict

```text
CONTROL_PLANE = PASS_WITH_CORRECTIONS
CERTIFIED_RUNS_MODIFIED = NO
VALIDATE_AFTER = PASS
TOTAL = 146
CLOSED = 33
BACKLOG = 87
BLOCKED = 12
CONDITIONAL = 7
MERGED = 6
DEFERRED = 1
READY = 0
TE_ACTIVE = 0
DELIVERY_PASS_R3P1_CLOSED = 19
```

## Findings

1. `DASHBOARD.md` était cohérent mais trop pauvre : aucun compteur global, aucune visibilité sur les branches de synthèse encore bloquées.
2. `CORE_INGERENCE_ROUTING_2026-09-06.md` contenait un checkpoint dynamique périmé (`LAST_CLOSED=INV-138`). Une policy ne doit pas devenir une seconde source d'état.
3. Le bundle consolidé, le point analytique et l'index des fermetures existaient mais n'étaient pas reliés explicitement au control plane.
4. Aucun défaut probatoire détecté dans les artefacts d'investigation certifiés; ils n'ont pas été modifiés.

## Corrections appliquées

- `control.py`: dashboard v2.1 générée depuis le registre avec compteurs live, `READY/TE_ACTIVE`, branches `INV-095/102/129/144/133`, hashes runtime/corpus et référence au snapshot/export.
- `CORE_INGERENCE_ROUTING_2026-09-06.md`: suppression du faux état live; la policy renvoie désormais explicitement au registre/dashboard.
- `README.md`: règle d'immutabilité des runs fermés, snapshots dérivés non canoniques, export consolidé et chaîne de trace projet explicités.
- `TRACELOG.md`: export, point programme, audit et corrections ajoutés en append-only.
- `PROGRAM_SNAPSHOT_2026-09-07.json`: snapshot machine-readable avec compteurs, dépendances ouvertes, limites d'export et SHA des sources.

## État opérationnel

```text
ACTIVE = NONE
READY = NONE
NEXT = UNSELECTED
NEXT_GATE = RECLASSIFICATION_POST_INV-093
```

Open synthesis branches:
- INV-095 <- INV-094, INV-119
- INV-102 <- INV-095, INV-098, INV-099
- INV-129 <- INV-080, INV-124
- INV-144 <- INV-045, INV-078, INV-079
- INV-133 <- INV-038, INV-040, INV-052, INV-068, INV-082, INV-088, INV-095, INV-102, INV-104, INV-129, INV-144

## Integrity anchors

- consolidated export SHA-256: `b2fec50e9cdd5e18806a96cdc7682b3fa23a917af6abe939ecafa1d0a590779f`
- registry SHA-256: `c98100a2c1383379d5a03774d39668b5b4b90676ae3c512e5bdcf5048eacaeef`
- TRACELOG SHA-256 after append: `7e7a51c5e51a09be7fb369d9035a4ac93108bf1f79e81379417401a6bdd7c230`
- dashboard SHA-256: `8ee2a561def3822ea330bddf9f2eb68d1bd5511279af71768a177ae5f502d400`
- control.py SHA-256: `4fc0bbca48f57f6a4afeb08b8969da47bb4f5f25270f2f4e4a28ce93f8bbc738`
- routing policy SHA-256: `821eb38462c5110d680fa99473bf88ca2fde3a43ab60c79696f52fadd6dadc8f`
- README SHA-256: `9ed30eae2b7d887aa43f2ab12d59fc83c6505288b0007311eb09f8c249407ebc`
- program snapshot SHA-256: `54071fdd16c244a40e1684c375da4a7975ea6eae1b415bdb66b77cf7790507fb`

## Next

Effectuer une reclassification post-INV-093 sous `CORE_MISSION_GATE` avant tout nouveau `READY`/lancement. Ne pas utiliser le snapshot ou le présent audit comme source d'état à la place du registre.
