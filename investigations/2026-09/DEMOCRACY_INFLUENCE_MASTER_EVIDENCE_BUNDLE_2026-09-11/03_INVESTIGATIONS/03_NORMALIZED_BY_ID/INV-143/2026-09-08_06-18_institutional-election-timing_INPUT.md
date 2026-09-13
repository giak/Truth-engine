---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-143-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-08"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-143"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-143 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-143

```text
SUBJECT = Timing judiciaire et administratif en période électorale : enquêtes, fuites, inéligibilités, sanctions et « October surprises » institutionnelles
OBJECT_QUESTION = Dans quelles conditions l’ouverture, la publicité ou le calendrier d’une procédure judiciaire/administrative avant un scrutin modifie-t-il la compétition politique, et comment distinguer application normale du droit, fuite opportuniste, erreur de calendrier et instrumentalisation démontrée ?
SCOPE = France/Europe avec comparateurs 2015–2026. Complément d’INV-100 : ici le mécanisme est le timing avant scrutin, pas seulement l’annulation. Tracer autorité compétente, calendrier procédural normal, décisions, fuites/communication, couverture, effet mesuré et preuve éventuelle d’intention. Une décision défavorable à un candidat n’est pas en soi une ingérence.
MODE = DEEPEN
COVERAGE = PARTIAL
CORPUS_REFS = A006:209222653.du-narratif-a-lingerence-le-seuil
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.

