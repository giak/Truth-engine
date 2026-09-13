---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-145-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-145"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-145 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-145

```text
SUBJECT = Qui est un « agent étranger » ? FARA, dispositifs français et européens : mêmes mécanismes, qualifications et sanctions asymétriques
OBJECT_QUESTION = À comportement matériel comparable — financement, représentation d’intérêts, communication, conseil politique, campagne — quand le droit exige-t-il transparence, enregistrement ou sanction comme influence étrangère, et quelles différences de périmètre ou d’application existent entre États-Unis, France et UE ?
SCOPE = Cadres en vigueur 2018–2026 : FARA américain, registre français de l’influence étrangère/HATVP et mécanismes européens pertinents. Comparer définitions, exemptions, obligations, données publiques, sanctions et enforcement sur cas comparables. La différence de droit n’est pas automatiquement un double standard ; la conclusion doit venir de la comparaison.
MODE = DEEPEN
COVERAGE = PARTIAL
CORPUS_REFS = A004:210182384.lingerence-sans-mesure;A006:209222653.du-narratif-a-lingerence-le-seuil
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
