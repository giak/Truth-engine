---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "pilot_review"
artifact_id: "INV-010-PILOT-REVIEW"
version: "1.0"
status: "pass_with_targeted_renard"
updated: "2026-09-05"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-010"
---

<!-- DERIVED_FROM: artifact=2026-09-05_16-35_cia-elections-etrangeres-r4_INVESTIGATION.md; handoff=INV-010_RUN_HANDOFF.md -->
<!-- DECISION: pilot=PASS_WITH_TARGETED_RENARD; renard_scope=Chile_1964_I6_I7_only -->

# INV-010 — revue du pilote

## Verdict

```text
P0 = 0
P1 = 1
P2 = 1
PILOT = PASS_WITH_TARGETED_RENARD
RENARD = REQUIRED
SCOPE = CHILE_1964_I6_I7_ONLY
```

Le pilote remplit sa fonction : il sépare preuve d'intervention, coordination,
exposition, effet observé et résultat contrefactuel. Le runtime R2A.2 est
DELIVERY PASS. Aucun redesign supplémentaire n'est requis.

## ROBUSTE

1. **Existence des interventions.** Italie 1948 et Chili 1964/1970 disposent
   de traces primaires suffisantes pour établir l'action américaine.

2. **Anti-déterminisme.** Le run ne déduit pas automatiquement
   `operation -> winner changed`.

3. **Italie 1948.** L'intervention est établie ; la causalité sur le vainqueur
   reste ouverte face aux causes domestiques et aux analyses indépendantes.

4. **Chili 1970.** Le test immédiat est observable : Allende arrive premier
   malgré l'opération anti-Allende. Track II reste distinct de l'effet électoral.

5. **I6/I7.** La distinction entre changement du résultat observé et
   contrefactuel du vainqueur est maintenue.

## P1 — saturation trop forte sur Chili 1964

Le run marque l'axe `effect and counterfactual` comme `SATURATED`, alors que :

- le claim d'effet sur marge/majorité reste `PARTIAL`;
- la causalité correspondante reste `UNRESOLVED`;
- les deux faits centraux Chili 1964 utilisés pour ce claim appartiennent à la
  même famille de provenance officielle américaine;
- l'évaluation causale décisive est en partie une auto-évaluation CIA/USG.

Une vérification post-pilote a identifié une source académique indépendante
directement discriminante :

José Tomás Labarca, *Latin American Research Review* (2017),
“Por los que quieren un gobierno de avanzada popular”:
https://www.cambridge.org/core/journals/latin-american-research-review/article/por-los-que-quieren-un-gobierno-de-avanzada-popular-nuevas-practicas-politicas-en-la-campana-presidencial-de-la-democracia-cristiana-chile-19621964/E9A033E7B37997628DA2119963BFDE67

Cette étude insiste sur la mobilisation propre de la Démocratie chrétienne,
l'élargissement massif du corps électoral et l'implantation sociale de la
campagne Frei. Elle ne nie pas l'appui américain ; elle montre qu'expliquer la
majorité de Frei par cet appui seul est insuffisant.

Conséquence : `SATURATED` était trop fort pour le sous-problème I6/I7 Chili 1964.

## P2 — formulation I6 à resserrer

La formulation actuelle :

> U.S. covert support affected Frei electoral margin/majority.

est plausible et soutenue par les archives américaines, mais elle doit rester
accompagnée de la limite :

> contribution matérielle plausible ; magnitude marginale non isolée.

RENARD doit déterminer si I6 reste `PARTIAL`, monte, ou se resserre vers
`UNRESOLVED contribution`.

## Décision RENARD

### REQUIRED

Le gate METHOD_PACK est satisfait :

```text
central discriminating gap           YES
causality / impact fragile           YES
central causal claim one-family      YES
accessible independent source        YES
potential model change               YES
```

### Scope

**Chili 1964 uniquement.**

Question :

> Des preuves indépendantes des auto-évaluations américaines permettent-elles
> d'établir que l'intervention américaine a matériellement augmenté la marge ou
> la majorité de Frei (I6), ou qu'elle a changé l'identité du vainqueur (I7) ?

Tester trois modèles concurrents :

```text
H1  intervention US -> contribution matérielle identifiable à la marge
H2  Frei aurait probablement gagné sans elle, mais marge/majorité possiblement affectée
H3  effet marginal non identifiable avec les preuves disponibles
```

### Exclusions

Ne pas rouvrir :

```text
Italy 1948
Chile 1970
Track II
existence du financement
architecture générale CIA
autres pays
article final
```

### Stop condition

Arrêter dès que :

```text
A  une preuve indépendante discriminante modifie le statut I6/I7
B  les sources indépendantes confirment seulement la pluralité des causes
   sans permettre une attribution causale supplémentaire
C  aucune preuve indépendante suffisamment discriminante n'est accessible
```

Dans B ou C :

```text
I6 = PARTIAL or UNRESOLVED, calibrated
I7 = NOT_ESTABLISHED
RENARD = CLOSED_NO_FURTHER_MATERIAL_DELTA
```

Aucun deuxième RENARD sur ce même gap sans nouvelle preuve matérielle.

## Pilot decision

```text
INV-010 = PILOT_REVIEW
TRUTH_ENGINE = DELIVERY_PASS_R2A2
RENARD = REQUIRED
NEXT = RUN_TARGETED_RENARD_CHILE1964_I6_I7
INV-019 = BLOCKED
```
