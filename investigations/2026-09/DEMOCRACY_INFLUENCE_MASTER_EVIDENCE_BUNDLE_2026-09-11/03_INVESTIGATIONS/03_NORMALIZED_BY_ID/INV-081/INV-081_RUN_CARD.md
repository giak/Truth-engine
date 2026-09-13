---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_card"
artifact_id: "INV-081-RUN_CARD"
version: "1.0-kiss"
status: "ready"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-081"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-081 -->
<!-- GATE: requires=status=READY+type(PRIMARY|CASE)+object_question+scope; state=passed -->

# RUN_CARD — INV-081

```text
SUBJECT = Propriété réelle des médias français : reconstruire les chiffres sans reprendre 9 milliardaires/80-90 % sans dénominateur
OBJECT_QUESTION = Quelle est la concentration réelle de la propriété et du contrôle des médias d'information français, selon des dénominateurs explicites et comparables (audience, diffusion, chiffre d'affaires, titres/chaînes/sites et contrôle capitalistique), et que permettent réellement de conclure ces mesures sur le pluralisme sans confondre propriété, audience et contrôle éditorial ?
SCOPE = France, état actuel et trajectoire 2010–2026 lorsque les séries sont comparables. Identifier bénéficiaires effectifs/groupes de contrôle, périmètre des actifs d'information, parts selon plusieurs dénominateurs explicites, service public et indépendants, changements de propriété et limites méthodologiques. Tester spécifiquement les slogans '9 milliardaires' et '80–90 %' sans accepter un pourcentage sans univers, date et métrique. Exclure l'inférence automatique propriété -> ligne éditoriale, qui relève d'INV-082.
MODE = RECHECK_EXTEND
COVERAGE = SUBSTANTIAL_PRIOR
CORPUS_REFS = A012:204169916.le-debat-qui-nexistait-pas-6-mecanismes;A014:202848231.lecart-legalitelegitimite-la-signature;A022:199655164.le-verrou-28-recours-au-493-57-dabstention;A025:199654938.medias-censure-et-desinformation;A036:199422722.la-caste-parasite-qui-gouverne-la;A049:193809543.audiovisuel-public-anatomie-dune;A091:181572197.lindustrie-de-linfluence-enquete
DEPENDENCIES = NONE

TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
METHOD_PACK = METHOD_PACK.md
```

Use Truth Engine 2.10.6 / R3P1 and METHOD_PACK.md.
Do not write the article. Do not execute RENARD inside Truth Engine.
After Truth Engine, create a concise RUN_HANDOFF per METHOD_PACK §10.
