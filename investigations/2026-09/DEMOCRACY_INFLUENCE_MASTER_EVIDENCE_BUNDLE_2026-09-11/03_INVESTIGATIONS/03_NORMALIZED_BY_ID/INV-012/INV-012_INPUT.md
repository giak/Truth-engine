---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-012-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-09"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-012"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-012 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-012

```text
SUBJECT = COINTELPRO et ingénierie politique intérieure américaine : infiltration, fragmentation, surveillance, neutralisation
OBJECT_QUESTION = Quelles opérations de COINTELPRO ont effectivement utilisé infiltration, surveillance, désinformation, provocation, fragmentation ou neutralisation contre des organisations et mouvements politiques intérieurs américains, quelles chaînes de commandement et actions sont documentées, et quels effets organisationnels, comportementaux ou démocratiques peuvent être attribués sans confondre surveillance, intention, action, dommage et causalité politique ?
SCOPE = États-Unis, principalement 1956–1971, avec suites judiciaires, parlementaires et déclassifiées nécessaires à l'attribution. Tracer autorité/mandat -> cible -> collecte/infiltration -> action disruptive ou informationnelle -> intermédiaire éventuel -> réaction de la cible -> dommage organisationnel/comportemental -> effet politique. Prioriser documents FBI déclassifiés, Church Committee, décisions judiciaires, dossiers officiels et travaux historiques fondés sur archives. Gardes : surveillance != disruption ; infiltration != provocation ; document interne != exécution ; proximité != tasking ; opération != effet politique ; illégalité/abus != changement électoral ; cas historique != preuve d'une pratique actuelle.
MODE = DEEPEN
COVERAGE = PARTIAL
CORPUS_REFS = A071:186904003.larchitecture-de-la-censure-europeenne;A082:183123537.lempire-du-mensonge-rapport-dautopsie
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
ORCHESTRATOR = INVESTIGATION_ORCHESTRATOR.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md. Preserve the selected contract from INVESTIGATION_ORCHESTRATOR.md; do not broaden the run to adjacent context.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
