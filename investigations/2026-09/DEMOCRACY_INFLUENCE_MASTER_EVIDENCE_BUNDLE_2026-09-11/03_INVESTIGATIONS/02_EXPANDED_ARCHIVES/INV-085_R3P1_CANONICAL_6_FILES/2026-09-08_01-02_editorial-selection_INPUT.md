---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-085-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-085"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-085 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-085

```text
SUBJECT = Sélection des sujets avant même leur traitement : pouvoir éditorial en amont du verdict
OBJECT_QUESTION = Comment les rédactions, fact-checkers et organisations de vérification sélectionnent-ils les sujets, affirmations ou événements à traiter avant toute conclusion, quels critères, rôles éditoriaux, signaux d'audience ou contraintes institutionnelles sont documentés, et quelles preuves permettent de distinguer agenda éditorial ordinaire, biais de sélection systématique, influence économique/institutionnelle et contrôle externe ?
SCOPE = France/Europe 2019–2026, avec comparateurs internationaux seulement pour des politiques éditoriales isomorphes. Prioriser politiques publiques de sélection des sujets/claims, chartes éditoriales, rôles des éditeurs, critères d'intérêt public/viralité/impact, mécanismes de suggestion ou monitoring, corrections et indépendance déclarée. Tester séparément sélection du sujet, cadrage, verdict et distribution. Ne pas inférer propriété/financement -> sélection sans arête documentée. Gardes : selection != verdict ; agenda != censorship ; ownership != editorial_command ; funding != topic_tasking ; omission != suppression ; correlation != causal_control. Alimenter INV-082 et INV-068.
MODE = RECHECK_EXTEND
COVERAGE = SUBSTANTIAL_PRIOR
CORPUS_REFS = A001:212538645.qui-fact-checke-les-fact-checkers;A002:212051560.qui-fabrique-lautorite-du-vrai;A008:208733314.la-fabrique-de-la-menace-comment;A012:204169916.le-debat-qui-nexistait-pas-6-mecanismes;A025:199654938.medias-censure-et-desinformation;A091:181572197.lindustrie-de-linfluence-enquete
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
