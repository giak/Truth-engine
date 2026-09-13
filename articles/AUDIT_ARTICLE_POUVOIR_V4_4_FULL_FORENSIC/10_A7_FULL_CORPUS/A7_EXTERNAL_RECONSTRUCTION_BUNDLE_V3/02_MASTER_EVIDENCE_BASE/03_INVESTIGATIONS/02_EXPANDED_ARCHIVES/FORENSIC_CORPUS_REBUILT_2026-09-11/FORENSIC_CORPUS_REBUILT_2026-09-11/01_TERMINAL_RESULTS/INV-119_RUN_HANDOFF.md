---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-119"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-095"
updated: "2026-09-10"
---

# RUN_HANDOFF — INV-119

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260910-1208-elite-reproduction-circulation`
- Deliverable: `INV-119_INVESTIGATION.md`
- Deliverable SHA-256: `d11138d4de79d418204708a64e5382c9811ae4d5d4017daaa68111d56cdb6a0d`
- Corpus runtime: `QRY=24 / SRC=20 / FCT=29 / provenance_families=5`
- Persistence: `PASS / eligible=29 / blocked=29 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

INV-119 ferme un mécanisme structurel de reproduction et de concentration des élites françaises sans valider un modèle de coordination ou de capture générale. Les gradients sociaux vers les filières sélectives sont élevés et contemporains ; l'ENA autour de 2019-2020 était fortement homogène socialement, mais boursiers, voies Talents et évolutions récentes interdisent le modèle d'une caste totalement fermée. L'Inspection des finances présente historiquement une forte circulation public-privé et fournit un accès professionnel de haut niveau, mais sa structure pyramidale constitue une explication institutionnelle rivale à la capture, et la réforme post-2023 modifie substantiellement le recrutement : les taux historiques ne peuvent donc pas être projetés mécaniquement sur l'IGF actuelle. Les mobilités public-privé sont un canal documenté de risque de conflit d'intérêts, soumis à un contrôle HATVP réel avec réserves et incompatibilités. Le modèle soutenu est `sélection sociale -> accès élitaire -> concentration de trajectoires/réseaux -> opportunités de circulation et de conflit`; les chaînes `réseau -> agenda commun -> coordination` et `revolving door -> décision capturée` restent non fermées. INV-095 peut utiliser les mécanismes supportés de sélection, concentration et accès, mais pas les promouvoir en système coordonné de présélection politique sans traces supplémentaires.

## Registre causal certifié

- `origine sociale favorisée -> probabilité supérieure d'accès aux filières sélectives/CPGE/diplômes avancés` = **SUPPORTED** — gradient robuste, mécanismes fins non isolés causalement.
- `sélection éducative élitaire -> accès ENA/INSP et pipeline de haute fonction publique` = **SUPPORTED** — accès ne garantit ni poste terminal ni pouvoir de décision.
- `IGF -> missions/contacts de haut niveau -> opportunités de réseau et de circulation intersectorielle` = **SUPPORTED** — réseau/opportunité != coordination.
- `appartenance historique IGF -> transitions vers privé/banque` = **SUPPORTED** historiquement — non projetable telle quelle après réforme 2023 sans dénominateur courant.
- `mobilité public-privé -> risque de conflit -> contrôle HATVP/réserves/incompatibilité` = **SUPPORTED** — contrôle ne prouve ni absence ni présence d'influence effective.
- `école/corps/réseau commun -> agenda politique commun -> action coordonnée` = **UNRESOLVED** — aucune chaîne authentifiée de tasking/coordination identifiée.
- `concentration élitaire + revolving doors -> capture d'une décision publique précise` = **UNRESOLVED** — aucune attribution décisionnelle/contre-factuelle fermée.

## Gaps matériels certifiés

- **TEMPORAL_COVERAGE** — obtenir une série INSP post-réforme d'origine sociale directement comparable aux catégories ENA antérieures.
- **DENOMINATOR** — obtenir un dénominateur administratif post-2023 des sorties IGF par destination.
- **RESPONSIBILITY** — pour coordination, exiger communications authentifiées, stratégie commune ou interventions synchronisées au-delà du seul réseau partagé.
- **CAUSALITY** — pour capture, exiger acteur nommé, intérêt privé pertinent, droit de décision antérieur, contact/intervention ultérieur, décision ou delta de texte identifiable et contrôle des explications rivales.

## RENARD

`NO`

Recherche générique supplémentaire cumulative. Réouvrir uniquement sur une série sociale post-réforme comparable, un dénominateur IGF post-2023, une chaîne authentifiée de coordination, ou un cas décisionnel borné de conflit/capture.

## Reclassification

Impact direct : `INV-095`.

## Transition attendue

`INV-119 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis reclassification de `INV-095` après fermeture de sa dernière dépendance directe. `INV-102` reste un effet transitif dépendant de l'issue d'INV-095 et n'est pas déclaré comme impact direct de ce handoff.
