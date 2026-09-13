---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "dependency_synthesis"
artifact_id: "INV-040-SYNTHESIS"
version: "1.0-kiss"
status: "final"
updated: "2026-09-11"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-040"
truth_engine: "NOT_RUN_BY_DESIGN"
input_gate: "PASS_WITH_RECOVERY"
---

<!-- TRACE: dependency_only=true; web_collection=false; truth_engine=false; dependencies=9/9; recovery=INV-044 -->
<!-- GATE: all_direct_dependencies=CLOSED; all_terminal_outputs_usable=true; state=passed -->
<!-- DECISION: best_model=polycentric_delegation_with_asymmetric_agenda_access_and_fragmented_accountability; unitary_capture=NOT_ESTABLISHED -->

# INV-040 — Déficit démocratique européen : réalité mesurable versus slogan politique

## Question

Dans quelle mesure l’architecture institutionnelle de l’Union européenne distribue-t-elle initiative, expertise, accès, veto, contrôle et responsabilité de façon susceptible de produire un déficit démocratique mesurable, et quels mécanismes relèvent plutôt de la délégation, de la co-législation ou de contre-pouvoirs réels ?

## Gate d’entrée

La synthèse consomme exclusivement les neuf sorties terminales fermées prévues par le DAG. Aucun Truth Engine et aucune collecte web ne sont exécutés. `INV-044` est consommée via un handoff de récupération borné, explicitement limité au contenu terminal disponible ; aucune conclusion n’est renforcée au-delà de ce matériau.

| Dépendance | Entrée | Statut |
|---|---|---|
| INV-039 | `INV-039_RUN_HANDOFF.md` | TERMINAL_HANDOFF / SHA256 `f161f85f3b3e4ac598054a114b461a01b480ef2fb646c39112e3ff7df8733748` |
| INV-041 | `INV-041_RUN_HANDOFF.md` | TERMINAL_HANDOFF / SHA256 `755ca22180fafb8699be5da76c9ebd24d62e5ed39d17312906942491763342f9` |
| INV-042 | `INV-042_RUN_HANDOFF.md` | TERMINAL_HANDOFF / SHA256 `ee30ab176cfb9f73b9f225cb9ff05d0d994d3913f667954800580c20ccb87925` |
| INV-043 | `INV-043_RUN_HANDOFF.md` | TERMINAL_HANDOFF / SHA256 `f9a2ef582d9a35ca8b7de6dfefeaf578dacac1544834a7a4cbb4ee2ba14f3ac9` |
| INV-044 | `INV-044_RUN_HANDOFF.md` | RECOVERY_BOUNDED / SHA256 `e85cbeebba1a91a9a084b1ed811144dee0e9db755c867b30fd0b5ae2ecf1fda1` |
| INV-045 | `INV-045_RUN_HANDOFF.md` | TERMINAL_HANDOFF / SHA256 `dceb321e6ed9d0f0e13be5d6cd7a12cfacbdda929b2ec10c0a83eaa70088cc01` |
| INV-046 | `INV-046_RUN_HANDOFF.md` | TERMINAL_HANDOFF / SHA256 `eb957002612d086217cba34030f91e3b867844744ad07a9811e06aabb9359b12` |
| INV-047 | `INV-047_RUN_HANDOFF.md` | TERMINAL_HANDOFF / SHA256 `117e7b67c5ad6c68fc006ca02c7991665b9b561bc5ede80f942ddb9cca492533` |
| INV-048 | `INV-048_RUN_HANDOFF.md` | TERMINAL_HANDOFF / SHA256 `02ae047dac6d31df1353295080acb7130200919098357b5af1fbca5af5c4a3a2` |

## Résultat central

Le corpus ne soutient pas une mesure unique du « déficit démocratique » européen. Il soutient plutôt un **profil mécanistique** : l’Union combine une forte délégation institutionnelle, une initiative réglementaire asymétrique, une dépendance élevée à l’expertise et des inégalités d’accès observables, avec une responsabilité politique souvent fragmentée entre Commission, Conseil, Parlement, États, autorités spécialisées et juridictions. Ces propriétés peuvent réduire la lisibilité du mandant, du décideur marginal et du point exact où une préférence devient règle.

En sens inverse, le corpus établit des **contre-pouvoirs réels et non décoratifs** : co-législation Parlement–Conseil, frontières de compétence et vetos étatiques, contrôle juridictionnel, objection aux actes délégués, recours DSA, exigences de transparence et mécanismes de réexamen. Les dossiers informationnels et numériques montrent des capacités publiques ou co-régulées importantes, mais ne ferment ni une chaîne générale de commandement éditorial ni une architecture intégrée `identité -> communication -> sanction politique`.

Le modèle le mieux soutenu est donc celui d’une **gouvernance polycentrique et technico-juridique, avec asymétries d’agenda, d’expertise et d’accès, et responsabilité fragmentée**, plutôt qu’un modèle de capture unitaire. Le terme « déficit démocratique » devient empiriquement utile seulement lorsqu’il est décomposé en dimensions mesurables : visibilité de l’initiative, traçabilité de l’influence, égalité d’accès, réversibilité/recours, contrôle des délégations et capacité d’attribuer une décision à un responsable identifiable.

## Tests de modèles concurrents

| Modèle | Verdict | Base dependency-only |
|---|---|---|
| **M1 — Délégation / co-législation polycentrique** | **SUPPORTED** | INV-039 ferme la distribution du pouvoir par type de décision ; INV-041 ferme proposition Commission -> négociation/co-législation -> acte final ; INV-043, 047 et 048 montrent des mécanismes de supervision, recours, sanction et adaptation bornés. |
| **M2 — Capture sectorielle par acteurs privés** | **PARTIAL / case-specific, NOT_ESTABLISHED generally** | INV-041/042 établissent consultation, expertise, accès et asymétries ; aucune chaîne générale `acteur privé nommé -> clause précise -> adoption` n’est fermée. |
| **M3 — Réseau transversal de gouvernance informationnelle** | **SUPPORTED comme écosystème, NOT_ESTABLISHED comme commandement unitaire** | INV-043/044/045 établissent co-régulation, financement, certification, coordination et accès programmatiques ; tasking éditorial universel, retrait automatique d’État et effet politique causal restent non établis. |
| **M4 — Alignement émergent sans centre unique** | **PLAUSIBLE / PARTIAL** | Des institutions, régulateurs, plateformes, certificateurs et bénéficiaires peuvent converger autour de normes et objectifs communs ; le corpus ne permet pas de transformer cette convergence en coordination cachée ou capture. |
| **M5 — Architecture cohérente de coercition politique intégrée** | **NOT_ESTABLISHED** | INV-046 ne ferme pas l’intégration EUDI/QWAC/CSA vers profil citoyen/sanction ; INV-047/048 ferment des contraintes juridiques et économiques réelles mais pas une obéissance politique générale ou un contrôle idéologique terminal. |

## Dimensions effectivement mesurables

1. **Initiative et agenda** — asymétrie réelle en faveur de la Commission dans la procédure ordinaire, mais adoption non unilatérale (`INV-039`, `INV-041`).
2. **Accès et expertise** — ressources et expertise augmentent l’accès dans certaines arènes ; l’effet marginal sur le texte final doit être démontré dossier par dossier (`INV-042`).
3. **Traçabilité** — registres, consultations et transparence créent des traces utiles mais incomplètes ; contacts informels et attribution marginale restent des angles morts (`INV-041`, `INV-042`).
4. **Délégation technique** — DSA, certification, identité numérique et dispositifs informationnels créent des capacités administratives/co-régulées réelles ; capacité ne signifie pas commandement politique (`INV-043`, `INV-045`, `INV-046`).
5. **Recours et réversibilité** — recours DSA, juridictions, objection aux actes délégués et contrôles procéduraux constituent des contre-pouvoirs observables (`INV-041`, `INV-043`, `INV-047`).
6. **Contrainte externe** — sanctions, conditionnalité commerciale et pouvoir réglementaire produisent des coûts/adaptations mesurables ; `contrainte économique != changement politique causal` (`INV-047`, `INV-048`).

## Ce qui est établi

- la distribution du pouvoir européen varie fortement selon la base juridique et la phase de décision ;
- l’initiative, l’expertise et l’accès sont asymétriques et peuvent produire une distance entre préférence citoyenne, contribution technique et texte final ;
- les mécanismes de consultation/lobbying sont institutionnalisés mais leur causalité marginale sur les décisions reste souvent non identifiée ;
- l’écosystème informationnel européen comporte financement public, coordination, certification et co-régulation réels ;
- les instruments juridiques, numériques, commerciaux et de sanctions peuvent produire des contraintes matérielles mesurables ;
- les contre-pouvoirs législatifs, juridictionnels et procéduraux sont eux aussi matériels.

## Ce qui n’est pas établi

- une autorité unique gouvernant de manière générale l’Union ;
- une capture privée générale du processus réglementaire ;
- une chaîne universelle `financement/certification -> conclusion éditoriale dictée -> effet politique` ;
- une architecture intégrée `identité -> communications -> profil citoyen -> sanction politique` ;
- une équivalence entre pouvoir réglementaire, coercition économique et changement politique terminal ;
- un indicateur agrégé unique permettant d’ordonner objectivement « le déficit démocratique » de l’UE.

## Contradictions et plafonds causaux

- `complexité institutionnelle != déficit démocratique` : il faut identifier le mécanisme précis de perte de contrôle, visibilité ou responsabilité ;
- `délégation != capture` : une compétence spécialisée peut être politiquement autorisée et juridiquement contrôlée ;
- `consultation/access != adoption` : une influence causale exige une empreinte législative versionnée ou une attribution décisionnelle ;
- `financement/certification != tasking éditorial` ;
- `supervision/modération != effet sur opinion ou résultat électoral` ;
- `sanction/compliance != adhésion politique` ;
- `norme commune != coercition` lorsque l’adhésion est négociée, réciproque ou assortie de voies de recours.

## Verdict

**SYNTHESIS PASS.** Le « déficit démocratique européen » est **partiellement objectivable**, mais seulement par sous-mécanismes. Le corpus soutient une dilution/fragmentation de la responsabilité et des asymétries d’initiative, d’expertise et d’accès ; il ne soutient pas une absence générale de contrôle démocratique ni une capture cohérente et unitaire du système. Les mécanismes de délégation et de pouvoir réglementaire sont accompagnés de contre-pouvoirs matériels, dont l’efficacité doit être évaluée dossier par dossier.

## Gaps résiduels

- legislative footprints versionnés reliant contributions nommées et clauses finales ;
- dénominateurs complets des accès formels/informels et de leur distribution ;
- métriques transversales de responsabilité/attribution de décision comparables entre procédures ;
- designs causaux sur effets politiques aval des dispositifs informationnels, sanctions et contraintes normatives ;
- audit post-déploiement des ponts techniques et contrôles EUDI/CSA/QWAC.

## RENARD / collecte additionnelle

`NO`. Une collecte générique supplémentaire serait cumulative. Les améliorations utiles nécessitent des designs ciblés : empreinte législative, dénominateurs d’accès, attribution de décision et causalité aval.

## Route

Résultat borné à transmettre à `INV-133`. `INV-038` et `INV-068` restent des synthèses distinctes et ne sont pas préemptées par cette conclusion.
