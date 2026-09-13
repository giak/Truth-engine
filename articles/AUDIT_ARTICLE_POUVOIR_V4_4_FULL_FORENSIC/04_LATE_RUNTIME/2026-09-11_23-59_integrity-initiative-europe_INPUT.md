---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-031-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-11"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-031"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-031 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-031

```text
SUBJECT = Integrity Initiative : financement FCO, clusters européens et influence contre-désinformation
OBJECT_QUESTION = Dans le cas Integrity Initiative, quelles preuves relient financement public britannique -> Institute for Statecraft -> clusters nationaux d’experts, journalistes et décideurs -> intervention informationnelle ou mobilisation -> cible médiatique ou institutionnelle -> décision ou exposition, et que permettent-elles réellement de conclure sur contre-désinformation légitime, influence britannique à l’étranger, tasking étatique, activité partisane et effet causal ?
SCOPE = Royaume-Uni, Espagne et France, principalement 2017-2019, avec suites institutionnelles jusqu’en 2026 uniquement lorsqu’elles contrôlent l’attribution ou l’accountability. Cas central : FCO/CSSF -> Institute for Statecraft / Integrity Initiative -> clusters Espagne/France -> action ou diffusion -> média/décideur -> réponse/issue ; campagne dite Moncloa comme test causal et controverse domestique britannique comme contrôle. Prioriser réponses parlementaires britanniques, grant/programme records, documents de projet attribuables, chronologie espagnole indépendante, régulateur caritatif et réponses UE. Gardes : grant != command ; listed contact != active member ; shared counter-disinformation goal != state tasking ; project self-attribution != causal proof ; leaked document != automatically authenticated fact ; official denial != automatic exoneration ; counter-disinformation != neutral by nature ; network != coordination beyond sourced action.
MODE = DEEPEN
COVERAGE = NEW_MECHANISM_GAP
CORPUS_REFS = NONE
DEPENDENCIES = NONE

TRUTH_ENGINE_PACK = TRUTH_ENGINE_2.10.6_R3P1_CANONICAL.zip
TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
ORCHESTRATOR = INVESTIGATION_ORCHESTRATOR.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md. Preserve the selected contract from INVESTIGATION_ORCHESTRATOR.md; do not broaden the run to adjacent context.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
