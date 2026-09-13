---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-079-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-079"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-079 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-079

```text
SUBJECT = Associations et prestataires subventionnés pour lutter contre désinformation, haine ou radicalisation
OBJECT_QUESTION = Quels financements, subventions, marchés ou partenariats publics soutiennent en France et dans l’UE des associations ou prestataires chargés de lutter contre la désinformation, la haine ou la radicalisation, quels objectifs, livrables, critères de sélection, contrôles et voies de recours sont documentés, et jusqu’où ces flux créent-ils capacité, accès, délégation ou influence sans confondre financement public, commandement éditorial, modération, censure et effet politique ?
SCOPE = France/UE 2018–2026. Étudier des dispositifs publics documentables de subvention, appel à projets ou marché visant prévention de la radicalisation, lutte contre haine/discrimination, éducation aux médias ou lutte contre désinformation. Tracer autorité financeuse, base du programme, bénéficiaire, montant lorsque public, objet/livrables, critères, reporting/évaluation, éventuelle relation avec plateformes ou autorités et effet observable. Exclure Fonds Marianne comme objet principal (INV-078) et certification fact-checkers déjà traitée par INV-045. Gardes : funding != command ; grant != procurement ; service_contract != editorial_control ; monitoring != removal ; public_support != censorship ; output != political_effect ; overlap != coordination. Alimenter INV-088 et INV-144.
MODE = RECHECK_EXTEND
COVERAGE = SUBSTANTIAL_PRIOR
CORPUS_REFS = A002:212051560.qui-fabrique-lautorite-du-vrai;A004:210182384.lingerence-sans-mesure;A039:198659211.opposition-controlee-anatomie-dun;A072:186844276.tristan-mendes-france-la-machine
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
