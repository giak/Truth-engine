---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "dependency_synthesis"
artifact_id: "INV-052-SYNTHESIS"
version: "1.0-kiss"
status: "final"
updated: "2026-09-11"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-052"
truth_engine: "NOT_RUN_BY_DESIGN"
input_gate: "PASS"
---

<!-- TRACE: dependency_only=true; web_collection=false; truth_engine=false; dependencies=5/5; removed_dependency=INV-058_by_design_review -->
<!-- DECISION: funding_to_capacity_agenda_access=SUPPORTED; funding_to_command_capture=NOT_ESTABLISHED_GENERAL -->

# INV-052 — Philanthrocapitalisme : financement privé, définition des problèmes et pouvoir public

## Résultat central

Le corpus établit que des financeurs privés, philanthropiques ou publics peuvent modifier matériellement la **capacité**, l'**agenda**, les métriques, l'expertise disponible et l'accès institutionnel d'organisations intermédiaires. Plusieurs chaînes ferment `ressources -> programme/capacité -> output/advocacy -> accès ou contribution institutionnelle`. Ce pouvoir est réel même sans ordre explicite : sélectionner ce qui est financé modifie l'ensemble des problèmes et solutions qui disposent de ressources pour être formulés, mesurés et défendus.

Le corpus ne ferme cependant pas un modèle général `financeur -> commandement -> bénéficiaire -> décision capturée`. Les contrôles sont nombreux : gouvernances autonomes, grants à flexibilité variable, séparation juridique de certaines activités financées et politiques, recours judiciaires auto-dirigés, et absence répétée de preuve de tasking sur une action ou une clause précise. L'effet le mieux soutenu est donc **structurel et capacitaire**, parfois agenda-setting, plus rarement décisionnel et presque jamais causalement attribuable à un seul financeur.

## Chaîne consolidée

| Arête | Verdict |
|---|---|
| `financeur -> ressources/capacité` | **SUPPORTED** |
| `priorités/conditions de financement -> agenda/opportunity set` | **SUPPORTED/PARTIAL** |
| `ressources -> advocacy/expertise/service` | **SUPPORTED** |
| `advocacy/expertise -> accès/output institutionnel` | **SUPPORTED case-specific** |
| `financeur -> tasking d'une action/position précise` | **NOT_ESTABLISHED generally** |
| `financeur -> clause/décision publique causée` | **UNRESOLVED generally** |
| `financement -> capture` | **NOT_ESTABLISHED generally** |

## Apports des dépendances

- `INV-049` : OSF -> grants/ressources et objectifs vérifiés ; coordination/tasking des bénéficiaires non établie ; More in Common fournit un bridge vers recherche d'opinion sans commandement prouvé.
- `INV-051` : Rockefeller/Paris ferme une contribution matérielle à une stratégie municipale ; financement fléché OMS réduit la discrétion d'allocation ; advocacy/access Reset/EDRi sont établis, sans donor-specific authorship.
- `INV-053` : financement d'ONG migration -> capacité et advocacy/accès ; contrôle SOS Méditerranée montre une séparation juridique entre subvention humanitaire et activité politique.
- `INV-054` : contentieux stratégique peut produire des obligations institutionnelles ; financement de capacité est réel, donor tasking d'un dossier précis non établi.
- `INV-057` : objectifs de financeurs, grants et monitoring produisent des outputs mission-alignés avec autonomie variable ; mission alignment et monitoring ne ferment pas command/tasking.

## Modèles concurrents

- **Soutien pluraliste / capacité opérationnelle** : **SUPPORTED**.
- **Agenda-setting par sélection des bénéficiaires/problèmes** : **SUPPORTED/PARTIAL**.
- **Dépendance financière réduisant l'autonomie** : **PARTIAL / case-specific**, nécessite gouvernance/conditions concrètes.
- **Tasking direct du bénéficiaire** : **NOT_ESTABLISHED generally**.
- **Capture de décision publique par philanthrocapitalisme** : **NOT_ESTABLISHED generally**.

## Contrôles et plafonds

`financement != commandement`; `mission alignment != tasking`; `bénéficiaire != proxy`; `advocacy != adoption`; `accès != capture`; `output != effet`; `dépendance budgétaire != causalité décisionnelle`.

## Verdict

**SYNTHESIS PASS.** Le philanthrocapitalisme exerce un pouvoir politique **structurel** lorsqu'il sélectionne les capacités, agendas, métriques et intermédiaires qui deviennent disponibles dans l'espace public et institutionnel. Ce pouvoir peut produire de l'accès et des outputs identifiables. En revanche, le corpus ne justifie pas de convertir cette capacité de cadrage et de financement en commandement général des bénéficiaires ou en capture causale des décisions publiques.

## RENARD

`NO` — les upgrades utiles nécessitent clauses de grant/tasking, gouvernance de décision, legislative footprints ou contrefactuels de politique publique, pas une nouvelle collecte générique sur les financeurs.

## Route

Résultat borné à transmettre à `INV-133`.
