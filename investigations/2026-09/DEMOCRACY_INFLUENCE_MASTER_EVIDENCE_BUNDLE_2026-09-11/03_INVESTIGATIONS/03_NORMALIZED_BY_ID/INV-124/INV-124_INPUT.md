---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-124-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-124"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-124 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-124

```text
SUBJECT = Debanking, paiements, sanctions et accès financier comme infrastructure privée/publique de coercition
OBJECT_QUESTION = Par quels mécanismes banques, prestataires de paiement, réseaux de cartes, plateformes et dispositifs de sanctions ou de conformité peuvent-ils restreindre l’accès financier d’acteurs politiques, médiatiques, associatifs, économiques ou individuels, sur quelle base et avec quels recours, et quelles preuves permettent de distinguer gestion de risque ou conformité, coercition financière, commandement public/privé et effet politique ?
SCOPE = France/Europe 2015–2026, avec comparateurs étrangers uniquement lorsque le mécanisme est isomorphe. Tracer déclencheur, acteur décisionnaire, base juridique ou contractuelle, articulation public/privé, service ou flux affecté, notification/motif, durée, recours/réintégration, coût économique et effet politique éventuel. Distinguer debanking, gel/sanction, fermeture de compte, refus de paiement, déréférencement financier et conformité AML/KYC. Gardes : debanking != censorship ; compliance != political motive ; private decision != state command ; sanction != guilt ; access restriction != political effect ; complaint/association != proof.
MODE = DEEPEN
COVERAGE = PARTIAL
CORPUS_REFS = A067:188810196.le-gulag-digital-surveilles-a-100;A083:183424330.lagonie-du-souverain-la-singularite;A087:182502562.la-justice-spectrale-lere-du-bannissement;A109:180129975.leurope-construit-elle-un-credit-40d;A110:180128122.leurope-construit-elle-un-credit
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
