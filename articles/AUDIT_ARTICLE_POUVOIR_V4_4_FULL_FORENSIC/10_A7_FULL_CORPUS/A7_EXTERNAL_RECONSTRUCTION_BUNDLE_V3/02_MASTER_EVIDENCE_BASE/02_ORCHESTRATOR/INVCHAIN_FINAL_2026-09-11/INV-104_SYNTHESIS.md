---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "dependency_synthesis"
artifact_id: "INV-104-SYNTHESIS"
version: "1.0-kiss"
status: "final"
updated: "2026-09-11"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-104"
truth_engine: "NOT_RUN_BY_DESIGN"
input_gate: "PASS"
---

<!-- TRACE: dependency_only=true; web_collection=false; truth_engine=false; dependencies=3/3; removed_dependencies=INV-106,INV-107_by_design_review -->
<!-- DECISION: mistrust_to_vulnerability_bridge=NOT_ESTABLISHED; endpoints_exist_separately=true -->

# INV-104 — Mensonge institutionnel → défiance → vulnérabilité à la manipulation : la boucle causale existe-t-elle ?

## Résultat central

Les trois briques de la boucle existent séparément mais le bridge causal central n'est pas fermé. `INV-103` établit une défiance institutionnelle différenciée et des associations avec voix politique, efficacité, honnêteté, respect et position sociale, sans direction causale générale. `INV-111` établit que négativité, récompense sociale et ranking modifient clic, expression, exposition et parfois attitudes politiques, avec des contrôles nuls selon plateforme/horizon. `INV-112` établit l'exploitation intentionnelle de récits complotistes dans certains cas, ainsi que des mécanismes domestiques et marchands distincts, sans fermer une chaîne générale exposition -> persuasion -> effet électoral.

Aucune des dépendances ne démontre que **la baisse de confiance institutionnelle augmente causalement la susceptibilité individuelle ou collective à une opération de manipulation donnée**. La co-occurrence de défiance, consommation de contenus négatifs, complotisme ou mobilisation peut refléter sélection préalable, identité, griefs, environnement médiatique ou variables communes. Le modèle prudent est donc : `défiance = contexte/vulnérabilité plausible`, pas `défiance -> manipulation réussie` comme causalité établie.

## Chaîne testée

| Arête | Verdict |
|---|---|
| `échec/perception négative -> défiance institutionnelle` | **ASSOCIATED / causality not generally identified** |
| `défiance -> exposition/sélection de contenus manipulatoires` | **NOT_ESTABLISHED** |
| `défiance -> croyance accrue dans un récit manipulatoire` | **NOT_ESTABLISHED** |
| `ranking/négativité -> exposition/engagement` | **SUPPORTED** |
| `actor-specific operation -> contenu complotiste -> visibilité` | **SUPPORTED case-specific** |
| `exposition -> persuasion/attitude` | **HETEROGENEOUS / case-specific** |
| `persuasion -> comportement politique/électoral` | **NOT_ESTABLISHED generally** |

## Modèles concurrents

- **Défiance comme cause de vulnérabilité** : **NOT_ESTABLISHED**.
- **Défiance et vulnérabilité comme effets de causes communes** : **PLAUSIBLE / unresolved**.
- **Sélection préalable** : personnes déjà méfiantes choisissent davantage certains contenus/réseaux : **PLAUSIBLE / unresolved**.
- **Effet de plateforme indépendant de la confiance** : **SUPPORTED** par les expériences de ranking/engagement.
- **Exploitation opportuniste d'un public déjà polarisé/méfiant** : **SUPPORTED/PARTIAL case-specific**, sans effet marginal de la défiance isolé.

## Contradictions et plafonds

`défiance != gullibilité`; `corrélation trust/conspiracy != causalité`; `engagement != persuasion`; `visibilité != croyance`; `croyance != vote`; `exploitation intentionnelle != efficacité`; `effet plateforme != intention politique de la plateforme`.

## Verdict

**SYNTHESIS PASS — causal bridge NOT_ESTABLISHED.** La boucle conceptuelle est plausible et cohérente avec plusieurs mécanismes fermés séparément, mais le corpus actuel ne permet pas de conclure que la perte de confiance envers les institutions cause une vulnérabilité accrue à la manipulation. La démonstration exige un design longitudinal, expérimental ou quasi-expérimental reliant variation de confiance, exposition identifiée, réception puis comportement, avec contrôle de la sélection préalable.

## RENARD

`NO` — le gap est méthodologique, non documentaire. Une recherche générique supplémentaire sur défiance/complotisme serait cumulative.

## Route

Résultat borné à transmettre à `INV-133` comme **non-fermeture causale** : ne pas utiliser la défiance comme explication automatique de la réussite d'une influence.
