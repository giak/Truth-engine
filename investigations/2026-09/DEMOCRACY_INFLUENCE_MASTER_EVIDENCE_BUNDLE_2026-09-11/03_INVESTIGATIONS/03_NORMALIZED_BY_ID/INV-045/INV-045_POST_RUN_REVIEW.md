---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "post_run_review"
artifact_id: "INV-045-POST-RUN-REVIEW"
version: "1.0"
status: "terminal"
updated: "2026-09-07"
inv_id: "INV-045"
---

<!-- TRACE: runtime=2.10.6/R3P1; delivery=PASS; review_scope=delta-only -->

# Post-run review — INV-045

## Verdict

```text
TRUTH_ENGINE = DELIVERY_PASS_R3P1
QRY = 17
SRC = 14
PROVENANCE_FAMILIES = 5
FCT = 28
CHECKPOINTS = 6
G0_G10 = PASS
TESTS = 140 passed / 2 skipped
PERSISTENCE = PASS / 28 terminal MNEMO_UNAVAILABLE blocks
P0 = 0
P1 = 0
P2 = 3
RENARD = NO
INV_STATUS = CLOSED_AUTHORIZED
```

## Central delta

EFCSN et IFCN opèrent des systèmes de certification fondés sur des standards, évaluations, gouvernance et mécanismes de plainte/revue. Cette certification produit **des effets d’accès réels mais bornés** : l’EFCSN est un critère explicite d’éligibilité pour certains sous-programmes FACTEUR/Database Grants, et le statut IFCN est une condition nécessaire mais non suffisante pour certains programmes de plateformes.

Le financement public européen est matériel : la Commission a signé une subvention de 5 M€ portée par un consortium dirigé par l’EFCSN, dont une part importante est redistribuée à des organisations de fact-checking. Le corpus ne permet cependant pas de convertir `financement -> capacité/accès` en `financement -> commandement éditorial`.

Les contrôles négatifs sont matériels : d’autres appels européens ont des conditions d’éligibilité plus larges ; les hubs EDMO ont leur propre architecture et une exigence d’indépendance à l’égard des autorités publiques ; IFCN précise que son statut peut être nécessaire sans être suffisant pour accéder à certains programmes de plateformes.

Conclusion bornée : **certification comme infrastructure d’accès = ESTABLISHED, program-specific ; autorité publique universelle, contrôle éditorial et effet politique causal = NOT_ESTABLISHED.**

## Highest supported I0..I7

- `I0 = VERIFIED` : acteurs, gouvernance, programmes et relations institutionnelles.
- `I1 = VERIFIED` : financements, critères d’éligibilité, ressources et capacités d’accès.
- `I2 = VERIFIED` : procédures de certification, appels, subventions et dispositifs d’accès documentés.
- `I3 = VERIFIED/PARTIAL bounded` : coordination institutionnelle et relations de programme ; tasking éditorial non établi.
- `I4 = VERIFIED/PARTIAL` : accès à certains financements, outils, repositories ou programmes ; effet universel non établi.
- `I5 = NOT_ESTABLISHED generally` : contrôle de la sélection ou conclusion éditoriale.
- `I6 = NOT_ESTABLISHED` : persuasion/comportement politique causé par certification/financement.
- `I7 = NOT_ESTABLISHED` : résultat politique/électoral contrefactuel.

## P2 residuals

1. dénominateur complet des candidatures, rejets, retraits et avantages d’accès selon programme ;
2. contrats et décisions internes permettant d’identifier d’éventuelles conditions éditoriales ou un tasking au niveau des contenus ;
3. chaîne causale `certification/financement -> output éditorial -> exposition -> comportement politique -> résultat` non fermée.

## RENARD

`NO` — une collecte générique supplémentaire serait cumulative. Les résidus demandent des contrats de plateforme, dossiers de sélection/subvention, communications internes ou designs causaux, pas davantage de pages publiques générales.

## Routing

Delta terminal vers `INV-040`, `INV-088` et `INV-144`.
