---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-157"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "NONE"
updated: "2026-09-11"
---

# RUN_HANDOFF — INV-157

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260911-2234-recompense-differee-revolving-door-anticipation`
- Deliverable: `2026-09-11_22-34_recompense-differee-revolving-door-anticipation_INVESTIGATION.md`
- Deliverable SHA-256: `d08d535f30747364a8d1c879d0464fdbddf36b23cee3c9aa538a1f55de9cfbdd`
- State ID: `sha256:4b9a62bc955ba20cb8c626ab56ae7f4a7625c589ffe8dd75066adb42f3dda1c7`
- Runtime: `QRY=16 / SRC=10 / FCT=16 / provenance_families=5`
- PRE gate: `PASS`
- DELIVERY gate: `PASS`
- Persistence: `PASS / eligible=16 / attempted=0 / success=0 / failure=0 / blocked=16 / MNEMO_UNAVAILABLE`

## Delta central

INV-157 ferme un niveau probatoire intermédiaire qui ne doit être confondu ni avec une mobilité professionnelle ordinaire, ni avec une corruption démontrée : **le conflit anticipatoire peut être établi lorsque le recrutement ou la perspective d'un poste privé chevauche des responsabilités publiques encore exercées**, mais le passage à `décision influencée -> quid pro quo -> récompense différée` exige une preuve supplémentaire de négociation/promesse et une arête décisionnelle spécifique.

- **Adam Farkas / EBA -> AFME** : recrutement et entretiens pendant l'exercice des fonctions, absence de récusation sur des matières ensuite couvertes par des restrictions = `ANTICIPATORY_CONFLICT_SUPPORTED`. Une décision précise modifiée en faveur d'AFME = `NOT_ESTABLISHED`.
- **Jean-Baptiste Djebbari / CMA CGM** : chevauchement du portefeuille ministériel, contacts répétés et projet de poste produisent un risque déontologique jugé non neutralisable = `PREVENTIVE_INCOMPATIBILITY_SUPPORTED`; favoritisme antérieur ou contrepartie = `NOT_ESTABLISHED`.
- **Djebbari / Hopium** : deux rencontres antérieures et mobilité sectorielle n'ont pas suffi à établir une atteinte à l'exercice antérieur des fonctions ; compatibilité sous réserves = **contrôle négatif** contre `chronology/proximity -> misconduct`.
- **Neelie Kroes / Uber** : approche en vue d'une coopération future documentée ; OLAF n'a pas établi de négociation professionnelle concrète pendant le mandat ni de traitement réglementaire favorable, tout en conservant un gap d'accès aux données = **contre-cas borné**.

## Registre causal certifié

- `pre-departure recruitment/contact + continuing relevant public duties -> anticipatory conflict risk` = **SUPPORTED / case-specific**.
- `anticipated future job -> specific public decision changed -> later private reward` = **NOT_ESTABLISHED** dans le corpus inspecté.
- `portfolio overlap + repeated contacts + prospective role -> preventive ethics incompatibility` = **SUPPORTED / case-specific**.
- `same-sector mobility + prior meetings -> prior favoritism` = **REFUTED AS AUTOMATIC INFERENCE**.
- `revolving door / ethics restriction / later job -> corruption or quid pro quo` = **REFUTED AS AUTOMATIC EQUIVALENCE**.

## Gaps matériels

- **DECISION_CAUSALITY** : absence de preuve fermant une décision publique précise causée par l'anticipation d'un emploi futur.
- **QUID_PRO_QUO** : aucune promesse/contrepartie actor-specific suffisamment établie dans le périmètre inspecté.
- **ACCESS** : certaines données privées anciennes ou non conservées limitent la reconstruction, notamment dans le dossier Kroes/Uber.
- **DENOMINATOR** : les données HATVP décrivent la gestion des mobilités, pas la prévalence de corruption ou de décisions biaisées.

## RENARD

`NO`. Ajouter des cas génériques de portes tournantes serait cumulatif. Une réouverture devient matérielle seulement avec des preuves primaires nouvelles de négociation avant décision, une contrepartie explicite, une décision actor-specific traçable ou un design causal permettant d'attribuer le changement de décision.

## Reclassification impact

`NONE` sur le pool courant : INV-157 ferme son mécanisme au niveau accessible et laisse des **triggers de RECHECK**, pas un nouveau sujet autonome. Aucun HOLD existant n'est rendu PASS par ce delta.

## Transition

`INV-157 -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`.
