---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "renard_delta"
artifact_id: "INV-010-RENARD"
version: "1.0"
status: "final"
updated: "2026-09-05"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-010"
---

<!-- DERIVED_FROM: artifact=2026-09-05_16-35_cia-elections-etrangeres-r4_INVESTIGATION.md; handoff=INV-010_RUN_HANDOFF.md; pilot_review=INV-010_PILOT_REVIEW.md -->
<!-- DECISION: renard=CLOSED_NO_FURTHER_MATERIAL_DELTA; scope=Chile_1964_I6_I7_only; cycles=2 -->

# RENARD — INV-010 / Chili 1964 / I6-I7

## Objective

Question unique :

> Des preuves indépendantes des auto-évaluations américaines permettent-elles
> d'établir que l'intervention américaine a matériellement augmenté la marge ou
> la majorité de Frei en 1964 (I6), ou qu'elle a changé l'identité du vainqueur
> (I7) ?

Aucun autre cas n'a été rouvert.

## DECOMPOSE

| Atom | Sub-claim | Needed discriminant | Initial |
|---|---|---|---|
| A1 | intervention US a déplacé la marge de Frei | source indépendante isolant un effet électoral | OPEN |
| A2 | intervention US a changé le vainqueur | contrefactuel crédible sans intervention | OPEN |
| A3 | causes domestiques expliquent une part matérielle du vote Frei | preuve de mobilisation/coalition indépendante de l'aide US | OPEN |

## SHADOW

| Atom | Si effet US causal fort | Si rival domestique fort | Discriminant |
|---|---|---|---|
| A1 | variation attribuable à exposition/traitement US | vote expliqué aussi par implantation PDC, coalition et nouveaux électeurs | étude d'effet indépendante |
| A2 | preuve crédible qu'Allende aurait gagné sans opération | Frei déjà candidat/coalition compétitif sans démonstration de bascule | winner counterfactual |
| A3 | mobilisation domestique secondaire | organisation PDC préexistante + mobilisation sociale massive | historiographie chilienne |

# Cycle 1 — BREAK par causalités domestiques

## NEW

### E1 — Labarca 2017, Latin American Research Review

José Tomás Labarca reconstruit la campagne démocrate-chrétienne 1962–1964 :
élaboration programmatique participative, réseaux de femmes/campesinos/jeunes,
implantation territoriale, massification et mobilisation d'un électorat dont une
grande fraction participait pour la première fois à une présidentielle.

Son résultat est directement discriminant : la magnitude du vote Frei ne peut
être expliquée uniquement par la campagne de peur, l'appui de la droite ou le
soutien extérieur. Il attribue un rôle électoral matériel aux pratiques propres de
la Démocratie chrétienne.

Source consultée :
https://www.cambridge.org/core/journals/latin-american-research-review/article/por-los-que-quieren-un-gobierno-de-avanzada-popular-nuevas-practicas-politicas-en-la-campana-presidencial-de-la-democracia-cristiana-chile-19621964/E9A033E7B37997628DA2119963BFDE67

Status: **SUPPORTED** for A3.

### E2 — Hurtado-Torres 2020, Cornell/Oxford

Sebastián Hurtado-Torres établit un rôle américain important et parfois
direct dans la politique chilienne, mais conclut plus largement que les acteurs
chiliens alliés aux États-Unis avaient leurs motivations, intérêts et dynamiques
propres. Les États-Unis sont un acteur informel puissant, pas un centre qui
détermine mécaniquement les choix politiques chiliens.

Sources consultées :
https://academic.oup.com/cornell-scholarship-online/book/31370/chapter-abstract/264492713
https://academic.oup.com/cornell-scholarship-online/book/31370/chapter-abstract/264497903

Status: **SUPPORTED** for the domestic-agency rival.

## ADVERSARY — Cycle 1

| Axis | H intervention-dominante | Rival domestique | Observation | Favors |
|---|---|---|---|---|
| organisation électorale | ressources US centrales | PDC structurée depuis avant la phase finale | mobilisation PDC documentée dès 1962 | Rival |
| majorité 56% | campagne US explique magnitude | nouveaux électeurs + coalition + organisation expliquent une part importante | sources indépendantes exigent modèle multicausal | Rival |
| contrôle du résultat | US peut « choisir » le vainqueur | acteur chilien autonome | Hurtado-Torres refuse cette réduction | Rival |

### UPDATE after cycle 1

```text
H1 identifiable US margin effect    -> WEAKEN
H2 Frei probably wins anyway        -> MAINTAIN / UNRESOLVED
H3 marginal effect non-identifiable -> STRENGTHEN
```

# Cycle 2 — recherche d'un effet électoral indépendant

## NEW

### E3 — Margaret Power 2008, Diplomatic History

Power documente de façon indépendante la *Scare Campaign* :
campagne multimédia financée et conçue avec intervention américaine, ciblant
particulièrement les femmes et exploitant la peur anticommuniste.

Le point décisif pour I6/I7 est négatif : son étude indique que l'étendue selon
laquelle cette campagne a influencé le vote **n'est pas quantifiable** et qu'aucune
étude contemporaine ne permettait d'en isoler l'effet. Elle rapporte des
évaluations américaines d'impact, mais celles-ci restent des auto-évaluations de
l'opération, pas un contrefactuel indépendant.

Publisher:
https://academic.oup.com/dh/article/32/5/931/397419

Full-text access consulted:
https://www.researchgate.net/publication/230206849_The_Engendering_of_Anticommunism_and_Fear_in_Chile%27s_1964_Presidential_Election

Status:
- campaign existence/reach: **VERIFIED/SUPPORTED**;
- causal vote magnitude: **OPEN**.

### E4 — Navia & Osorio 2015, Latin American Research Review

Les auteurs réanalysent les enquêtes d'Eduardo Hamuy. L'enquête d'août 1964
dans la province de Santiago montre une coalition électorale Frei très large :
fort soutien à droite et au centre, ainsi qu'une fraction substantielle de
répondants de gauche.

Cette donnée est utile comme dénominateur et rival : Frei ne dépendait pas d'un
seul mécanisme de persuasion. Mais l'enquête intervient après le début de la
campagne de peur et ne fournit pas de groupe non exposé ou de contrefactuel
permettant d'attribuer une variation de voix à l'opération américaine.

Source consultée :
https://www.cambridge.org/core/journals/latin-american-research-review/article/las-encuestas-de-opinion-publica-en-chile-antes-de-1973/E4DFB9F599070F5C2228FD3AE28CD2DE

Status:
- breadth of Frei coalition: **SUPPORTED**;
- causal US treatment effect: **OPEN**.

## CONNECTED

Les quatre sources indépendantes s'emboîtent sans produire de contradiction :

```text
US intervention = large and real
+
Scare Campaign = extensive and plausibly persuasive
+
PDC/Frei domestic mobilization = independently strong
+
right/center coalition + new electorate = material
+
no independent treatment-effect design
=
causal marginal vote effect not identifiable
```

## CONTRADICTED

La formulation suivante ne survit pas au standard RENARD :

> « l'intervention américaine a matériellement augmenté la marge/majorité de Frei »

si elle est lue comme une causalité électorale établie.

Elle doit être remplacée par :

> **l'intervention américaine a fourni des ressources, des capacités et une
> campagne de persuasion de grande ampleur ; une contribution au vote est
> plausible, mais son effet marginal sur la marge de Frei n'est pas isolable
> avec les preuves indépendantes consultées.**

Ce delta ne nie pas l'intervention ni sa portée.

## H_STATUS_CHANGES

```text
H1  US intervention -> identifiable contribution to Frei margin
    WEAKEN -> UNRESOLVED

H2  Frei probably wins without US support, margin perhaps affected
    UNRESOLVED

H3  marginal electoral effect cannot be identified from available evidence
    STRENGTHEN -> SUPPORTED
```

## EVIDENCE_DELTA

Before RENARD:

```text
I4 = VERIFIED
I5 = implicit/partial
I6 = PARTIAL / effect on margin-majority supported
I7 = NOT_ESTABLISHED
```

After RENARD:

```text
I4 = VERIFIED
     extensive campaign/action/reach documented

I5 = SUPPORTED (qualitative)
     persuasion mechanism and audience resonance are supported,
     but not numerically isolated

I6 = UNRESOLVED
     contribution plausible; marginal change in vote/margin not independently identified

I7 = NOT_ESTABLISHED
     no credible evidence identifies a different winner without intervention
```

Highest causal level that should be **positively asserted** after RENARD: **I5**.

## RESIDUALS

One residual remains but is no longer actionable with currently accessible
evidence:

> exact marginal vote effect of US-funded intervention.

To move I6/I7, a materially different design would be needed, e.g. credible
variation in exposure with comparable populations, contemporaneous panel data,
or another source that genuinely reconstructs the counterfactual.

No such discriminant was found in two RENARD cycles.

## GAPS

```text
I6 exact magnitude = OPEN
I7 winner counterfactual = OPEN / NOT_ESTABLISHED
```

These are calibrated knowledge limits, not reasons to keep searching indefinitely.

## NEW_IDEAS_TRIAGED

| Idea | Decision | Reason |
|---|---|---|
| build a new investigation solely to quantify 1964 propaganda effect | DROP | no identified discriminating dataset; YAGNI |
| reopen Italy 1948 | DROP | outside RENARD scope |
| reopen Chile 1970 | DROP | outside RENARD scope |
| create exposure-by-radio quasi-experiment | DEFER | only if a concrete historical dataset is later discovered |

## EVALUATE

| Atom | Evidence basis | Independent? | Survives break? | Status | Robustness |
|---|---|---:|---:|---|---|
| A1 margin effect identifiable | Power + Labarca + Navia/Osorio | Y | N | OPEN | LOW |
| A2 winner changed | no valid independent counterfactual | Y search | N/A | OPEN / NOT_ESTABLISHED | OPEN |
| A3 domestic causal contribution | Labarca + Hurtado-Torres + survey structure | Y | Y | SUPPORTED | HIGH |

Epistemic ledger delta:

```text
verified   1
supported  2
disputed   0
open       2
refuted    0
```

No synthetic confidence score.

## REPORT

| Field | Content |
|---|---|
| what_changed_since_last | I6 downgraded from positive PARTIAL causal wording to UNRESOLVED; I5 becomes highest positive causal level |
| surviving_H | multicausal model; large US intervention + autonomous domestic mobilization |
| killed_H | none as logical possibilities; strong causal-margin assertion is not supportable |
| strongest_discriminant | independent scholarship explicitly says vote effect cannot be quantified while documenting strong domestic mobilization |
| remaining_decisive_gap | no valid counterfactual or treatment-effect estimate |
| next_priority | none for this gap without new data |
| material_delta | YES |

## NEXT

```text
RENARD = CLOSED_NO_FURTHER_MATERIAL_DELTA
INV-010 = CLOSE
INV-019 = READY_NOT_LAUNCHED
```

No second RENARD on Chile 1964 I6/I7 unless a new materially discriminating
dataset/source appears.
