---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-094-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-094"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-094 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-094

```text
SUBJECT = Financement étranger direct ou indirect des partis et candidats européens
OBJECT_QUESTION = Dans quels cas et par quels mécanismes des fonds ou avantages d’origine étrangère atteignent-ils directement ou indirectement des partis ou candidats européens, comment l’origine bénéficiaire et les véhicules intermédiaires sont-ils établis, et quelles preuves permettent de distinguer financement légal ou illégal, contournement, commandement politique et effet électoral ?
SCOPE = France/Europe 2012–2026, priorité aux cas où un parti ou candidat reçoit un prêt, don, avantage en nature, prestation, garantie ou soutien financier attribuable à une source étrangère, directement ou via un véhicule intermédiaire. Tracer source et bénéficiaire réel, véhicule, transfert, base juridique, déclaration/contrôle, décision/sanction, coordination ou tasking éventuel et effet. Complément d’INV-093 (financement domestique réglementé) et d’INV-140 (espace électoral indirect hors partis/candidats). Gardes : foreign funding != interference ; funding != command ; loan != donation ; intermediary != concealed principal ; illegality != electoral effect ; sanction != result changed.
MODE = DEEPEN
COVERAGE = PARTIAL
CORPUS_REFS = A116:180061326.qui-a-vraiment-la-tete-dans-le-sable;A119:180052771.qui-est-vraiment-louis-duclos
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
