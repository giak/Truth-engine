---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-111-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-11"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-111"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-111 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-111

```text
SUBJECT = Économie de l’indignation : médias et plateformes transforment-ils la colère en produit plutôt qu’en action ?
OBJECT_QUESTION = Les systèmes médiatiques et plateformes récompensent-ils structurellement les contenus suscitant indignation ou conflit, et quels effets mesurables ces incitations produisent-elles sur exposition, engagement, production de contenu et comportement politique ?
SCOPE = France/Europe avec comparateurs internationaux, principalement 2015–2026. Tracer métrique/incitation économique ou algorithmique -> sélection/production de contenu -> exposition -> engagement/émotion -> comportement éventuel. Prioriser données de plateformes, expériences, études de recommandation, économie des médias et changements de politique. Gardes : engagement != persuasion ; outrage != manipulation ; corrélation contenu-performance != causalité ; incitation commerciale != tasking politique ; viralité != mobilisation.
MODE = RECHECK_EXTEND
COVERAGE = SUBSTANTIAL_PRIOR
CORPUS_REFS = A008:208733314.la-fabrique-de-la-menace-comment;A012:204169916.le-debat-qui-nexistait-pas-6-mecanismes;A025:199654938.medias-censure-et-desinformation;A065:189043675.la-machine-a-silence;A072:186844276.tristan-mendes-france-la-machine;A082:183123537.lempire-du-mensonge-rapport-dautopsie;A091:181572197.lindustrie-de-linfluence-enquete
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
