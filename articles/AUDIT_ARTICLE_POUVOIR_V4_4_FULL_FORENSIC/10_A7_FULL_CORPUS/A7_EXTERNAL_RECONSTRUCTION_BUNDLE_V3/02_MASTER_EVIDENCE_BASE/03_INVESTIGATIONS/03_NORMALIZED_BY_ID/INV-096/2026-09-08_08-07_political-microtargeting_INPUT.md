---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-096-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-08"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-096"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-096 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-096

```text
SUBJECT = Microtargeting électoral et données personnelles en France/UE
OBJECT_QUESTION = Dans quelle mesure le microtargeting politique fondé sur des données personnelles est-il effectivement utilisé en France et dans l’UE, par quels acteurs et chaînes data -> segmentation -> message -> delivery -> exposition, et quelles preuves permettent de distinguer capacité technique, ciblage déclaré, exposition réelle, persuasion, changement de comportement ou de vote et effet électoral ?
SCOPE = France/UE, 2016–2026, avec comparateurs Royaume-Uni/États-Unis uniquement lorsque les mécanismes ou méthodes de mesure sont isomorphes. Tracer source et base d’usage des données -> profil/segment -> commanditaire/campagne -> message/créatif -> plateforme/canal -> règles de delivery -> portée/exposition -> mesure de persuasion/comportement/vote. Prioriser décisions CNIL/EDPB et juridictions, bibliothèques publicitaires et transparence plateformes, données de campagnes, audits/expériences et documents de prestataires lorsque vérifiables. Gardes : data_collection != targeting ; targeting != delivery ; delivery != exposure ; exposure != persuasion ; persuasion != vote_change ; personalization != manipulation ; campaign_use != foreign_interference ; claimed_capability != demonstrated_effect. INV-017 Cambridge Analytica reste un cas discriminant, pas une preuve générale.
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
