---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-054-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-054"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-054 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-054

```text
SUBJECT = ONG de droits humains et contentieux stratégique : recours judiciaire comme instrument de transformation politique
OBJECT_QUESTION = Dans quels cas des ONG de droits humains utilisent-elles le contentieux stratégique pour modifier des normes, pratiques ou décisions publiques en France et en Europe, quels financeurs, soutiens, coordinations et choix de dossiers sont documentés, et jusqu'où peut-on établir une chaîne financement/organisation -> stratégie contentieuse -> décision -> mise en œuvre -> effet politique sans confondre recours légal, proximité, financement ou victoire judiciaire avec tasking, capture ou causalité systémique ?
SCOPE = France/Europe 2015–2026, avec un petit nombre de cas juridiquement documentables et comparables. Tracer identité et gouvernance de l'ONG, financeurs pertinents, choix/objectif du contentieux lorsqu'il est public, représentation juridique, base légale, décision et recours, mise en œuvre, changement institutionnel et preuve éventuelle de coordination/tasking externe. Inclure cas négatifs et échecs. Séparer financement de commandement, accès au juge de contrôle de l'issue, victoire judiciaire d'effet politique durable, contentieux stratégique de procédure abusive. INV-129 synthétisera ensuite lawfare/coercition avec d'autres mécanismes.
MODE = DEEPEN
COVERAGE = PARTIAL
CORPUS_REFS = A006:209222653.du-narratif-a-lingerence-le-seuil;A045:194518266.lingenierie-de-lenclos;A087:182502562.la-justice-spectrale-lere-du-bannissement
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
