---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-122-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-11"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-122"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-122 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-122

```text
SUBJECT = Industrie de défense : commandes publiques, lobbying, think tanks, médias et politique étrangère
OBJECT_QUESTION = Dans quels dossiers de défense des commandes, activités de lobbying, financements de think tanks ou réseaux d'expertise peuvent-ils être reliés à une décision d'acquisition ou de politique étrangère identifiable, sans confondre intérêt industriel, expertise, sécurité nationale et capture ?
SCOPE = France/UE, principalement 2010–2026, sur programmes ou décisions bornés. Tracer industriel/financeur -> lobbying/expertise/réseau -> décideur/procédure -> décision ou modification identifiable -> effet économique/politique. Prioriser marchés, registres, auditions, déclarations d'intérêts, financements et chronologies décisionnelles. Gardes : contrat != influence ; expertise financée != conclusion dictée ; lobbying != capture ; intérêt stratégique != prétexte ; proximité != tasking.
MODE = RECHECK_EXTEND
COVERAGE = SUBSTANTIAL_PRIOR
CORPUS_REFS = A023:199655095.la-defense-rongee-449-md-sans-munitions;A058:191802696.la-guerre-des-autres;A063:189855247.le-sanctuaire-inverse-comment-la;A075:186127641.limpasse-persique-pourquoi-loccident;A083:183424330.lagonie-du-souverain-la-singularite;A090:181766389.les-telegraphistes-de-la-terreur;A105:180223640.larmee-potemkine-quand-le-spectre;A107:180162835.service-militaire-volontaire-ce-que;A115:180081515.ukraine-ce-que-hayer-trump-et-zelenskyy
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
