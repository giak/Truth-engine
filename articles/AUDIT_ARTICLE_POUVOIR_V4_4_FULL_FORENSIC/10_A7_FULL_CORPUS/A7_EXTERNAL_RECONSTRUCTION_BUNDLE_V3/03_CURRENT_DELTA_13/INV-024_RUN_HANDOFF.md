---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-024"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "NONE"
updated: "2026-09-11"
---

# RUN_HANDOFF - INV-024

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260911-2318-new-ip-itu-standardisation`
- Deliverable: `2026-09-11_23-18_new-ip-itu-standardisation_INVESTIGATION.md`
- Deliverable SHA-256: `1e313e454216e8223012f910927297235ed8b36d8ab596674b592c0e4d361902`
- State ID: `sha256:95d9de0a4e611960e6e9e02536f59e0148ac037e8d042d2d9c8085121bdc99ec`
- Runtime: `QRY=21 / SRC=12 / FCT=16 / provenance_families=6`
- PRE gate: `PASS`
- DELIVERY gate: `PASS`
- Persistence: `PASS / eligible=16 / attempted=0 / success=0 / failure=0 / blocked=16 / MNEMO_UNAVAILABLE`

## Delta central

INV-024 ferme le résidu `standards technologiques` du précédent bundle Chine par un cas borné : New IP/FVCN à l'UIT-T. Le corpus établit une action conjointe d'agenda-setting au niveau de contributions formelles associant le MIIT et plusieurs entreprises chinoises, son passage dans la procédure UIT-T, puis une contre-mobilisation formelle de l'IETF et d'une coalition incluant la France, la Commission européenne, des États européens et des organisations techniques/sectorielles.

Le résultat aval est négatif pour l'hypothèse forte de capture : les propositions New IP testées n'ont pas franchi l'arête d'adoption au niveau des groupes d'étude puis de WTSA-20. Ce cas établit donc `standard-setting -> tentative d'influence institutionnelle / agenda-setting`, pas `standard-setting -> capture réussie`.

## Registre causal certifié

- `MIIT + entreprises chinoises -> contribution commune -> mise à l'agenda UIT-T` = **SUPPORTED** au niveau de la co-proposition institutionnelle.
- `co-signature État-entreprises -> tasking/contrôle de chaque entreprise par l'État` = **NOT_ESTABLISHED / ATTRIBUTION_GAP**.
- `New IP -> opposition IETF + France/UE/industrie/RIPE -> contre-contributions formelles` = **SUPPORTED**.
- `opposition à New IP = résistance purement géopolitique sans fondement technique` = **REFUTED** : des objections techniques et d'interopérabilité sont documentées.
- `New IP -> standard global adopté / capture de l'UIT` = **REFUTED_IN_BOUNDED_CASE** par la non-adoption du dispositif testé.
- `propriétés techniques controversées -> intention politique maligne de surveillance/contrôle` = **NOT_ESTABLISHED / INTENT_GAP**.
- `standardisation internationale -> arène d'influence avec contre-pouvoirs institutionnels` = **SUPPORTED_BOUNDED**.

## Limites

- Le run n'établit pas de communications privées prouvant un tasking du MIIT envers chaque entreprise co-signataire.
- Il ne mesure pas le poids causal marginal de chaque opposant dans la non-adoption.
- Les risques techniques ou de gouvernance identifiés par les critiques ne prouvent pas l'intention subjective des promoteurs.
- La réfutation de capture vaut pour le cas et la période testés, pas pour toute activité chinoise future de standardisation.

## RENARD

`NO` - ajouter des exemples génériques de participation chinoise à des organismes de standardisation serait cumulatif. Réouvrir seulement sur preuve directe de tasking, sur un successeur New IP/FVCN effectivement adopté, ou sur un effet normatif/gouvernance mesurable nouveau.

## Transition

`INV-024 -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`.
