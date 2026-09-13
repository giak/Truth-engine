---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-120-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-11"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-120"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-120 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-120

```text
SUBJECT = Finance et banques : lobbying, revolving doors, dépendance réglementaire et pouvoir de marché sur la décision publique
OBJECT_QUESTION = Dans quels dossiers financiers ou bancaires des actions de lobbying, des revolving doors ou une dépendance réglementaire peuvent-elles être reliées à une modification identifiable de règle ou de décision publique, avec contrôle des explications institutionnelles rivales ?
SCOPE = France/UE, principalement 2010–2026, sur dossiers réglementaires bornés. Tracer acteur financier -> contribution/lobbying/revolving door -> accès/intervention -> delta de texte ou décision -> effet distributif. Prioriser registres de lobbying, consultations, versions de textes, agendas, déclarations d'intérêts et décisions. Gardes : lobbying != capture ; revolving door != conflit prouvé ; conflit != décision capturée ; poids économique != tasking ; alignement de politique != causalité.
MODE = DEEPEN
COVERAGE = PARTIAL
CORPUS_REFS = A034:199653976.la-dette-instrumentalisee-3-200-milliards;A035:199655748.largent-qui-disparait-80-a-100-milliards;A046:194422681.le-leviathan-de-verre;A053:193017697.comment-la-richesse-verrouille-le;A054:192726440.le-vampire-de-la-croissance;A062:190192234.le-grand-manege-de-la-depossession;A083:183424330.lagonie-du-souverain-la-singularite;A089:182308074.france-2025-lanatomie-dune-feodalite
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
