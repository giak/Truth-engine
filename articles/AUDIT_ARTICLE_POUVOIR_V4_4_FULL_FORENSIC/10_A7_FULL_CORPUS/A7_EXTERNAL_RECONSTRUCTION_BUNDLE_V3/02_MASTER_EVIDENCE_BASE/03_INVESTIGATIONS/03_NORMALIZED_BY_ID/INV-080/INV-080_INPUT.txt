---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-080-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-080"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-080 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-080

```text
SUBJECT = Sanction administrative sans condamnation judiciaire : gel des avoirs, expulsions, interdictions, réputation et seuil de preuve
OBJECT_QUESTION = Dans quels cas des autorités administratives peuvent-elles imposer ou provoquer gel d’avoirs, interdiction, expulsion, restriction de droits ou autre sanction matérielle sans condamnation pénale préalable, avec quel standard de preuve, quels recours et quelles conséquences, et quelles preuves permettent de distinguer mesure de police ou de sécurité légalement fondée, erreur ou disproportion, coercition politique et instrumentalisation intentionnelle ?
SCOPE = France/Europe 2015–2026, avec comparateurs uniquement lorsqu’ils sont juridiquement isomorphes. Tracer autorité, base juridique, déclencheur, éléments de preuve, standard applicable, contradictoire, durée, mesure imposée, contrôle juridictionnel, recours/correction et effets matériels/politiques. Priorité aux gels/sanctions administratives, interdictions, expulsions ou restrictions prononcées sans condamnation pénale préalable. Gardes : administrative_measure != criminal_guilt ; legality != legitimacy ; allegation != proof ; sanction != political_motive ; institutional_effect != electoral_effect ; judicial_review != proof_of_initial_bad_faith.
MODE = RECHECK_EXTEND
COVERAGE = SUBSTANTIAL_PRIOR
CORPUS_REFS = A006:209222653.du-narratif-a-lingerence-le-seuil;A087:182502562.la-justice-spectrale-lere-du-bannissement
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
