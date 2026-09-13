---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-098-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-08"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-098"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-098 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-098

```text
SUBJECT = Achat de votes, clientélisme et redistribution électoraliste : formes modernes et réalité française
OBJECT_QUESTION = Quelles formes d'achat de votes, de clientélisme électoral et de redistribution explicitement conditionnée à un soutien politique sont documentées en France, avec quelles preuves, quelle fréquence et quels effets, et comment les distinguer de politiques publiques ciblées, promesses électorales, services de circonscription ou redistribution ordinaire sans quid pro quo démontré ?
SCOPE = France 2000–2026, avec comparateurs internationaux uniquement pour des mécanismes ou méthodes de mesure isomorphes. Prioriser décisions judiciaires, rapports officiels, travaux empiriques et cas documentant une chaîne avantage/ressource -> intermédiaire/candidat -> bénéficiaire/groupe -> condition ou attente de soutien -> preuve/recours/effet. Distinguer achat direct de voix, clientélisme, patronage, ciblage budgétaire et promesse programmatique. Gardes : redistribution != vote_buying ; targeted_policy != clientelism ; benefit != quid_pro_quo ; allegation != proof ; conviction_case != prevalence ; correlation != causal_exchange ; local_case != national_architecture ; material_transfer != electoral_effect.
MODE = GREENFIELD
COVERAGE = NEW
CORPUS_REFS = NONE
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
