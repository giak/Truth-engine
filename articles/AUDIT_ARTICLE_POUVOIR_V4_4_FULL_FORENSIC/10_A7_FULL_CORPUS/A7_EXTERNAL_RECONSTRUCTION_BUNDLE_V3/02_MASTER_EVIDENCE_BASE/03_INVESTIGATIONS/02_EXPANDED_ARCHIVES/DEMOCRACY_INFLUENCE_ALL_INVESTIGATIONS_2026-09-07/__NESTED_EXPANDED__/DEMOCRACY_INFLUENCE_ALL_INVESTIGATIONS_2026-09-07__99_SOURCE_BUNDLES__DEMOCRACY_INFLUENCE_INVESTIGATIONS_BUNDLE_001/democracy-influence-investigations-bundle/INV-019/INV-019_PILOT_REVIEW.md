---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "pilot_review"
artifact_id: "INV-019-PILOT-REVIEW"
version: "1.0"
status: "pass"
updated: "2026-09-05"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-019"
---

<!-- DERIVED_FROM: run=20260905-1921-inv019 -->
<!-- DECISION: pilot=PASS; renard=NO -->

# INV-019 — revue du pilote

## Verdict

```text
P0 = 0
P1 = 0
P2 = 1
PILOT = PASS
RENARD = NO
```

## ROBUSTE

### Architecture publique sans faux centre unique

Le run distingue trois régimes : `State / legacy-USAID`, `NED`, `USAGM`.
Ils partagent financement public et finalités stratégiques mais pas le même
régime de contrôle.

### Funding != control

NED est correctement qualifiée comme hybride : appropriation publique,
identité privée/nonprofit et discrétion d'un Board distinct. Les lacunes de
coordination documentées par GAO empêchent de promouvoir automatiquement
financement et alignement en commandement opérationnel unique.

### Overt != neutral

Les programmes ouverts poursuivent explicitement des objectifs de démocratie,
liberté, élections, médias, société civile et intérêts américains. Leur caractère
overt ne les rend pas politiquement neutres.

### Historical continuity != current CIA tasking

La continuité historique de fonctions avec certaines activités autrefois
financées covert est documentée. Le run refuse correctement d'en déduire une
chaîne actuelle `CIA -> State/NED/USAGM -> bénéficiaires`.

Aucune source consultée n'établit cette chaîne actuelle. Cette absence de preuve
publique n'est pas transformée en preuve d'absence.

### I0..I7

```text
I0 = VERIFIED
I1 = VERIFIED
I2 = VERIFIED
I3 = SUPPORTED
I4 = VERIFIED pour USAGM (reach)
I5 = UNRESOLVED à l'échelle de l'écosystème
I6 = UNRESOLVED
I7 = NOT_ESTABLISHED
```

La quantité de fonds, projets ou audience n'est pas promue en persuasion ou
effet politique causal.

## P2 — temporalité

L'architecture a matériellement changé en 2025-2026 avec l'arrêt de la mise en
œuvre de l'aide extérieure par USAID et le transfert de fonctions/awards à
State. Tout réemploi ultérieur doit garder `AS_OF` visible.

## RENARD = NO

Les résiduels sont réels mais aucun ne justifie un RENARD maintenant.

- **Current CIA tasking** : aucun document, acteur ou mécanisme concret n'a
  émergé comme lead discriminant. Chercher génériquement une liaison secrète
  serait du fishing.
- **I5-I7** : l'effet causal doit être testé dans des cas précis avec exposition
  et outcome, pas sur une architecture couvrant des milliers de projets et pays.

Réouverture seulement si apparaît un document concret de tasking clandestin,
une chaîne de commandement testable, un cas précis permettant I5-I7 ou une
contradiction matérielle avec les contrôles documentés.

```text
TRUTH_ENGINE = DELIVERY_PASS_R2A2
RENARD = NO
INV-019 = CLOSED
NEXT_PILOT = INV-049 READY_NOT_LAUNCHED
```

Aucun redesign du METHOD_PACK ou du runtime n'est requis.
