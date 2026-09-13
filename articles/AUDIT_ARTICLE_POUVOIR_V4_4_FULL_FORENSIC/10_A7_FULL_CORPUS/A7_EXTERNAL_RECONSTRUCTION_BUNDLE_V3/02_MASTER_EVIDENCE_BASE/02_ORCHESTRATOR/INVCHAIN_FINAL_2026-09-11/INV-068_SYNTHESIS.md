---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "dependency_synthesis"
artifact_id: "INV-068-SYNTHESIS"
version: "1.0-kiss"
status: "final"
updated: "2026-09-11"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-068"
truth_engine: "NOT_RUN_BY_DESIGN"
input_gate: "PASS"
---

<!-- TRACE: dependency_only=true; web_collection=false; truth_engine=false; dependencies=9/9 -->
<!-- DECISION: intermediation_chain=SUPPORTED_PARTIAL; covert_laundering_or_consensus_manufacture=NOT_ESTABLISHED_GENERAL -->

# INV-068 — Narrative laundering : intérêt → think tank → expert → média → décideur → apparence de consensus indépendant

## Résultat central

Le corpus ferme une architecture d'intermédiation réelle mais pas une chaîne générale de « blanchiment narratif » au sens fort. Les arêtes les mieux établies sont `ressources/financement -> capacité/participation/accès`, `sélection institutionnelle/éditoriale -> expertise/exposition`, puis, dans certains cas, `expertise/advice -> préparation ou reprise normative`. Elles montrent comment une préférence, une expertise ou un intérêt peut gagner visibilité, légitimité procédurale et accès à des décideurs.

La chaîne se rompt régulièrement avant `financeur -> tasking du contenu`, `répétition -> persuasion`, et surtout `exposition/reprise -> adoption/décision causée`. Des contre-exemples sont documentés : administrations qui réécrivent ou rejettent le conseil, financement public bottom-up sans agenda thématique imposé, groupes d'experts pluralistes, règles de conflit/transparence, et sélection éditoriale autonome. L'apparence d'indépendance peut donc être imparfaitement informative sans être nécessairement le produit d'une coordination cachée.

## Chaîne mécanistique consolidée

| Arête | Verdict |
|---|---|
| `financeur/intérêt -> ressource/capacité` | **SUPPORTED** |
| `ressource/capacité -> accès/participation/expertise` | **SUPPORTED** |
| `sélection -> exposition/reprise institutionnelle` | **SUPPORTED** |
| `expertise/conseil -> préparation normative` | **SUPPORTED case-specific** |
| `expertise -> clause/adoption précise` | **PARTIAL / case-specific** |
| `financeur -> tasking/contenu dicté` | **NOT_ESTABLISHED generally** |
| `répétition/exposition -> persuasion` | **UNRESOLVED / heterogeneous** |
| `répétition/exposition -> décision publique causée` | **NOT_ESTABLISHED generally** |
| `réseau -> coordination transversale` | **NOT_ESTABLISHED generally** |

## Apports des dépendances

- `INV-059/061` : think tanks français et américains ferment financement/ressources -> droits de participation, événements, auditions, expertise et accès ; donor/state tasking et adoption restent non établis.
- `INV-062/063` : consultants et Big Four peuvent intervenir matériellement dans la préparation de politiques/normes ; une continuité textuelle case-specific existe, sans fermer cabinet unique -> décision souveraine/capture générale.
- `INV-064` : les cabinets PR/public affairs convertissent explicitement des mandats clients en réunions, expertise, suggestions, événements et stratégies d'influence ; l'effet sur opinion ou décision reste hétérogène.
- `INV-065/085` : sélection des experts et des sujets constitue un gate éditorial réel ; répétition et différences de sélection sont observables mais ne ferment ni financement -> message dicté ni exposition -> persuasion.
- `INV-066` : le financement peut orienter l'agenda de recherche et parfois le processus ; `financement -> résultat dicté` est réfuté comme règle universelle.
- `INV-067` : composition des groupes d'experts -> advice est fermée, conflit mal géré et reprise normative existent case-specifically ; capture générale non établie.

## Modèles concurrents

- **Intermédiation pluraliste avec asymétries de ressources** : **SUPPORTED**.
- **Capture sectorielle ponctuelle / risque de conflit** : **PARTIAL / case-specific**.
- **Coordination cachée financeur -> expert -> média -> décideur** : **NOT_ESTABLISHED generally**.
- **Consensus apparent produit par répétition et sélection** : **PLAUSIBLE/PARTIAL**, mais causalité vers croyance/adoption non fermée.
- **Tasking transversal d'un réseau cohérent** : **NOT_ESTABLISHED**.

## Plafonds causaux

`funding != command`; `participation != adoption`; `expert selection != tasking`; `citation/reprise != causalité`; `répétition != persuasion`; `réseau != coordination`; `conflit != capture`; `préparation normative != décision souveraine`.

## Verdict

**SYNTHESIS PASS.** Le mécanisme matériel le mieux soutenu est une chaîne d'**intermédiation et d'amplification institutionnelle** où ressources, accès, sélection et expertise modifient l'ensemble des opportunités de visibilité et de contribution. Le concept de « narrative laundering » n'est justifié que dans des cas actor-specific où dissimulation, tasking ou contrôle du contenu sont établis ; il ne peut pas être appliqué par défaut à tout financement, expertise médiatique ou reprise institutionnelle.

## RENARD

`NO` — les upgrades matériels exigent communications de tasking, legislative footprints versionnés, journaux de sélection/rejet ou designs causaux exposition -> croyance/décision.

## Route

Résultat borné à transmettre à `INV-133`.
