---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-045-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-045"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-045 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-045

```text
SUBJECT = EFCSN, IFCN, fact-checkers et financement européen : certification comme infrastructure d’accès
OBJECT_QUESTION = Comment les dispositifs de certification des fact-checkers (notamment EFCSN/IFCN) et les financements ou partenariats européens structurent-ils l’accès à des contrats de plateformes, financements, partenariats institutionnels ou signaux de légitimité, quels critères, audits, recours et conflits sont documentés, et jusqu’où peut-on établir un effet de gatekeeping sans confondre certification, financement, commandement éditorial, délégation publique ou censure ?
SCOPE = France/UE, 2019–2026, avec comparateurs internationaux seulement lorsqu’ils éclairent le mécanisme de certification. Tracer gouvernance des certificateurs, critères, procédure d’admission/retrait, audit/recours, financements pertinents, relations avec plateformes et institutions publiques, avantages d’accès éventuels, exclusions documentées et effets observables. Gardes : certification != state_approval ; funding != editorial_command ; eligibility != guaranteed_access ; non_certification != censorship ; platform_contract != public_delegation ; audit != control. Alimenter INV-040, INV-088 et INV-144.
MODE = RECHECK_EXTEND
COVERAGE = SUBSTANTIAL_PRIOR
CORPUS_REFS = A001:212538645.qui-fact-checke-les-fact-checkers;A002:212051560.qui-fabrique-lautorite-du-vrai;A004:210182384.lingerence-sans-mesure;A072:186844276.tristan-mendes-france-la-machine
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
