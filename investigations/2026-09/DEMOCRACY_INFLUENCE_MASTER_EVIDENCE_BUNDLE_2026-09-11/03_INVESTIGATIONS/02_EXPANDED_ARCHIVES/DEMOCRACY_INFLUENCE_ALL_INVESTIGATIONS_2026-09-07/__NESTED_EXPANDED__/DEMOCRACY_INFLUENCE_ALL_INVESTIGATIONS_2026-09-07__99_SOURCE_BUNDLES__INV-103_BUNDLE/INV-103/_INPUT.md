---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-103-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-103"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-103 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-103

```text
SUBJECT = Défiance institutionnelle française : mesurer précisément qui n’est plus cru et pourquoi
OBJECT_QUESTION = Comment la confiance et la défiance se distribuent-elles réellement entre institutions en France, comment ont-elles évolué, et quelles causes sont soutenues par des preuves plutôt que par de simples corrélations ?
SCOPE = France, 2010–2026 avec focus 2020–2026. Séparer institutions politiques nationales, locales, médias, justice, police/armée, santé et démocratie comme régime. Examiner séries temporelles, comparateurs, déterminants et limites causales ; éviter l’agrégat vague 'défiance envers les institutions'.
MODE = DEEPEN
COVERAGE = PARTIAL
CORPUS_REFS = A010:205911763.le-verrou-invisible-anatomie-du-ric;A014:202848231.lecart-legalitelegitimite-la-signature;A021:199655311.la-justice-fantome-020-du-pib-86;A022:199655164.le-verrou-28-recours-au-493-57-dabstention;A041:198170736.le-paradoxe-francais-66-de-colere;A057:192293819.la-democratie-en-cage;A059:191154925.pourquoi-les-electeurs-francais-votent;A082:183123537.lempire-du-mensonge-rapport-dautopsie;A106:180194877.407-mensonges-lautopsie-dun-systeme
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
