---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-039-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-039"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-039 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-039

```text
SUBJECT = Qui exerce réellement le pouvoir dans l’UE ? Commission, Conseil, Parlement, CJUE, BCE, États, lobbies
OBJECT_QUESTION = Selon le type de décision, qui dispose réellement de quels pouvoirs dans l'Union européenne entre Commission, Conseil européen, Conseil de l'UE, Parlement, CJUE, BCE et États membres, et où l'accès des lobbies peut-il influer sans être confondu avec une autorité formelle ou un contrôle de résultat ?
SCOPE = Union européenne, architecture en vigueur et pratique 2010–2026, avec priorité au cadre actuel. Distinguer initiative/agenda, codécision et veto, budget, actes d'exécution et délégués, mise en œuvre nationale, nominations, contrôle juridictionnel, politique monétaire, sanctions/conditionnalité et révision des traités. Comparer pouvoir juridique formel, capacité d'agenda, contrôle de mise en œuvre et influence d'accès. Ne pas produire un classement global unique des institutions et ne pas inférer capture à partir du lobbying seul.
MODE = RECHECK_EXTEND
COVERAGE = SUBSTANTIAL_PRIOR
CORPUS_REFS = A014:202848231.lecart-legalitelegitimite-la-signature;A022:199655164.le-verrou-28-recours-au-493-57-dabstention;A024:199655040.leurope-piege-francais-12-contentieux;A037:199049245.le-changement-de-regime-pourquoi;A057:192293819.la-democratie-en-cage
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
