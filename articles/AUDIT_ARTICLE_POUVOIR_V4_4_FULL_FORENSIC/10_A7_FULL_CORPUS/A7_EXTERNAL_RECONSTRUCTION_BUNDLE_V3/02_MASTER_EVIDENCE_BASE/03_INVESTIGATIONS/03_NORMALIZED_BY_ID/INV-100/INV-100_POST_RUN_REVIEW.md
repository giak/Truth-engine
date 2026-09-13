---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "post_run_review"
artifact_id: "INV-100-POST-RUN-REVIEW"
version: "1.0"
status: "closed_authorized"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-100"
---

<!-- DERIVED_FROM: te_run=20260907-0935-roumanie-annulation-election; delivery_sha=12a9cb06c54fbab16dba416a39b4c1e1355d76c67a492da577bdffb117e0d39e -->
<!-- DECISION: p0=0; p1=0; p2=3; renard=NO; close=true -->

# Post-run review — INV-100

## Verdict

```text
TRUTH_ENGINE = DELIVERY_PASS_R3P1
RUN_ID = 20260907-0935-roumanie-annulation-election
QRY = 12
SRC = 12
PROVENANCE_FAMILIES = 9
FCT = 23
CHECKPOINTS = 6
G0_G10 = PASS
TESTS = 140 passed / 2 skipped
PERSISTENCE = PASS / 23 terminal MNEMO_UNAVAILABLE blocks
DELIVERY_SHA256 = 12a9cb06c54fbab16dba416a39b4c1e1355d76c67a492da577bdffb117e0d39e
P0 = 0
P1 = 0
P2 = 3
RENARD = NO
INV_STATUS = CLOSED_AUTHORIZED
```

## Contradictory review

Le run résiste aux deux raccourcis symétriques : `annulation = preuve d'un coup judiciaire` et `annulation judiciaire = preuve suffisante d'une ingérence étrangère ayant changé le résultat`.

Le noyau établi est plus étroit : l'annulation roumaine est un acte juridictionnel réel ; des irrégularités de campagne et de financement sont documentées et partiellement corroborées administrativement ; l'effet institutionnel est certain. En revanche, la chaîne publique `État étranger -> tasking -> opération -> persuasion -> résultat contrefactuel` n'est pas fermée et l'intention d'instrumentalisation politique des institutions n'est pas démontrée.

Le contrôle autrichien 2016 invalide aussi un faux standard : une juridiction peut annuler lorsque des violations établies sont assez nombreuses pour avoir pu influencer le résultat, sans prouver une fraude effective sur chaque bulletin. Le contrôle de la Commission de Venise impose néanmoins un seuil élevé, des faits clairement établis, une motivation suffisante et des garanties procédurales, notamment lorsque du renseignement classifié intervient.

## P2 bornés

1. **Attribution/tasking étranger** : la publication disponible ne ferme pas l'arête commanditaire étatique -> opérateur ; une amélioration exige des pièces de renseignement déclassifiées supplémentaires, des actes de procédure ou des preuves directes de tasking.
2. **Exposition/persuasion/contre-factuel** : aucun design causal robuste ne permet de quantifier combien d'électeurs ont été persuadés ni qui aurait gagné sans les irrégularités.
3. **Comparabilité procédurale** : l'Autriche est un contrôle utile mais non un précédent contraignant ; une généralisation européenne exigerait un corpus juridictionnel comparatif dédié.

Ces points ne justifient pas un RENARD générique : davantage de recherche ouverte serait surtout cumulative ou incapable de lever les plafonds causaux/attributifs.

## Routing

```text
MERGE -> INV-102 : distinction irrégularité / remède institutionnel / choix réel / légitimité
MERGE -> INV-129 : lawfare, annulation, exclusion et seuil de preuve
RECHECK -> uniquement si nouvelles pièces judiciaires, déclassification matérielle ou causal design identifié
```
