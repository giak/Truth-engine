---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "synthesis"
artifact_id: "INV-088-SYNTHESIS"
version: "1.0"
status: "pass"
updated: "2026-09-10"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-088"
input_gate: "INV-088_SYNTHESIS_INPUT_GATE.md"
---

<!-- TRACE: synthesized_from=INV-045,INV-079,INV-089,INV-090,INV-091 -->
<!-- EXECUTION: truth_engine_search=false; generic_collection=false; dependency_delta_only=true -->
<!-- GUARD: certification!=authority_of_truth; funding!=command; trusted_flagger!=removal_order; platform_action!=state_action; restriction!=partisan_censorship; ranking!=manipulation; exposure!=persuasion; persuasion!=electoral_effect -->

# INV-088 — Fact-checking comme infrastructure de qualification

## 1. Verdict central

Le corpus fermé établit une **infrastructure distribuée de qualification, capacité, signalement, décision de visibilité et recommandation**. Ses maillons ont des pouvoirs réels mais distincts :

- certification et financement peuvent conditionner des accès, ressources, programmes ou relations spécifiques ;
- les trusted flaggers disposent d’une priorité procédurale de traitement, pas d’un pouvoir autonome de retrait ;
- les plateformes prennent des décisions réelles de restriction/démotion avec recours et corrections ;
- les systèmes de classement/recommandation modifient effectivement l’exposition ; des expériences montrent que les effets attitudinaux sont contingents et hétérogènes.

La synthèse invalide deux raccourcis symétriques. Premièrement, ces dispositifs ne sont pas « sans pouvoir » : ils structurent capacités, ordre de traitement, visibilité et exposition. Deuxièmement, leur enchaînement ne démontre pas une **architecture générale de censure déléguée**, un tasking étatique transversal, un biais partisan systémique ni un effet électoral causal.

```text
CERTIFICATION_AS_BOUNDED_ACCESS_GATE           = ESTABLISHED
PUBLIC_FUNDING -> CAPACITY/OUTPUT               = ESTABLISHED case-specifically
TRUSTED_FLAGGER -> PRIORITY_OF_REVIEW           = ESTABLISHED
PLATFORM -> VISIBILITY_RESTRICTION/REVERSAL     = ESTABLISHED case-specifically
RANKING/RECOMMENDATION -> DIFFERENTIAL_EXPOSURE = ESTABLISHED
EXPOSURE -> ATTITUDE/ENGAGEMENT_EFFECT          = CONTINGENT / study-specific
STATE/FUNDER -> EDITORIAL_OR_MODERATION_TASKING = NOT_ESTABLISHED generally
SYSTEMATIC_PARTISAN_CENSORSHIP                  = NOT_ESTABLISHED
GENERAL_ELECTORAL_EFFECT                        = NOT_ESTABLISHED
```

## 2. Modèles concurrents

### M1 — Infrastructure pluraliste de qualité/modération
**SUPPORTED/PARTIAL.** Les dispositifs ont des fonctions explicites, des procédures, des recours et des corrections. Ce modèle explique une partie importante des observations sans commandement politique transversal.

### M2 — Gouvernance distribuée de la visibilité
**SUPPORTED.** Plusieurs acteurs distincts influent sur la capacité de produire/qualifier/signaler puis sur le traitement et l’exposition. Le pouvoir est distribué et séquentiel, avec des points de gate réels ; il n’est pas nécessairement centralisé.

### M3 — Capture sectorielle ou biais systémique
**UNRESOLVED.** Des biais ou erreurs peuvent exister et certaines décisions sont renversées, mais les dépendances ne fournissent ni dénominateur politiquement typé commun, ni attribution systématique du motif, ni chaîne de contrôle permettant une généralisation.

### M4 — Censure étatique déléguée / coordination transversale
**NOT_ESTABLISHED.** Les chaînes `financement/désignation -> tasking étatique -> décision plateforme -> suppression politique` ne sont pas fermées transversalement. Priorité de traitement, financement et co-régulation ne valent pas ordre de retrait.

## 3. Chaîne la plus avancée

```text
certification/funding -> capacity/access                  = SUPPORTED bounded
trusted flagger designation -> priority of review         = SUPPORTED
platform policy/decision -> restriction/demotion/reversal = SUPPORTED case-specific
ranking/recommendation -> differential exposure           = SUPPORTED
exposure -> engagement/opinion                            = MIXED / CONTINGENT
-> electoral behavior/outcome                             = NOT_ESTABLISHED generally
```

La nouveauté de synthèse est la **séparation des autorités** : financeur/certificateur, signaleur, plateforme et algorithme de recommandation peuvent intervenir dans la même chaîne sans être le même décideur ni former une coordination prouvée.

## 4. Revue contradictoire / plafond causal

`P0=0 / P1=0 / P2=4`.

1. **AUTHORITY** — le corpus ne fournit pas de matrice décisionnelle complète attribuant chaque restriction à un financeur, certificateur, signaleur ou autorité publique.
2. **DENOMINATOR** — les erreurs, recours et restrictions ne disposent pas d’un dénominateur politiquement typé commun permettant d’établir un biais partisan systémique.
3. **TASKING** — aucune chaîne transversale de tasking étatique/funder -> conclusion éditoriale ou décision de plateforme n’est authentifiée.
4. **EFFECT** — l’exposition a des effets hétérogènes selon plateforme/design ; aucun résultat électoral causal France/UE n’est fermé.

## 5. RENARD

`NO`.

Une collecte générique serait cumulative. Réouvrir seulement sur des logs décisionnels reliant signalement à action et motif, datasets politiquement typés de décisions/recours, communications de tasking authentifiées, ou designs causaux exposition -> attitude/comportement -> résultat.

## 6. Route

- `INV-088 -> CLOSED / SYNTHESIS_PASS / NOT_RUN_BY_DESIGN`.
- Résultat borné vers `INV-133`.
- Ne pas promouvoir « infrastructure distribuée de gouvernance de visibilité » en « censure coordonnée » sans arêtes de responsabilité/coordination.
