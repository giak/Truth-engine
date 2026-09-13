---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-056-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-08"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-056"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-056 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-056

```text
SUBJECT = Astroturfing : organisations présentées comme grassroots mais financées ou orchestrées par des intérêts structurés
OBJECT_QUESTION = Dans quels cas des organisations ou campagnes présentées comme spontanées, citoyennes ou grassroots sont-elles en réalité financées, créées, coordonnées ou amplifiées par des intérêts structurés, et quelles preuves permettent de tracer principal/financeur -> intermédiaire ou front group -> message/action -> cible/audience/décideur -> exposition ou effet sans confondre financement, proximité, alignement et orchestration ?
SCOPE = France/UE 2010–2026, avec comparateurs étrangers uniquement lorsque le mécanisme est isomorphe. Tracer origine et gouvernance de l'organisation, financeurs/contrats/subventions, intermédiaires/prestataires, staffing et instructions lorsqu'elles sont documentées, messages/actions, diffusion/mobilisation, cible et effet observable. Prioriser registres, déclarations financières, contrats, grants, documents internes/fuites authentifiées, enquêtes judiciaires/réglementaires, archives et données de plateformes. Distinguer grassroots authentique, advocacy sponsorisée et déclarée, front group, sockpuppet/astroturf et mobilisation rémunérée. Gardes : funding != tasking ; shared_staff != control ; message_similarity != coordination ; organizational_origin != current_control ; campaign_activity != exposure ; exposure != persuasion ; exposure != electoral/policy_effect ; allegation != proof.
MODE = DEEPEN
COVERAGE = PARTIAL
CORPUS_REFS = A013:203962785.un-geyser-de-6-metres-a-clichy-autopsie;A091:181572197.lindustrie-de-linfluence-enquete
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
