---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "post_run_review"
artifact_id: "INV-134-POST-RUN-REVIEW"
version: "1.0"
status: "pass"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-134"
---

<!-- DERIVED_FROM: te_run=20260906-1805-attribution-ingerence; certification=DELIVERY_PASS_R3P1 -->
<!-- DECISION: review=PASS; renard=NO; close=true -->

# POST-RUN REVIEW — INV-134

```text
P0 = 0
P1 = 0
P2 = 3
REVIEW = PASS
RENARD = NO
```

## ROBUSTE

1. Le run remplace l'attribution binaire par une chaîne d'arêtes vérifiables : `incident -> artefact/infrastructure -> opérateur -> intermédiaire -> commanditaire/État -> tasking/intention -> exposition -> effet`. Une arête forte ne transfère pas automatiquement sa force à l'arête suivante.
2. Le cas Plovdiv/von der Leyen fonctionne comme contrôle négatif : un problème d'approche GPS rapporté par l'équipage demeure compatible avec plusieurs causes, tandis que le récit public initial d'un brouillage russe ciblé n'est pas fermé par les données publiques inspectées. Le démenti russe reste lui aussi un claim, pas une preuve d'absence.
3. Rokh Solis et Portal Kombat montrent correctement la frontière `opérateur/infrastructure != commanditaire` : VIGINUM publie des marqueurs et similarités utiles mais conserve explicitement l'identité du commanditaire comme inconnue dans ces chaînes.
4. RRN/Doppelganger fournit une chaîne publique beaucoup plus forte vers l'appareil d'État russe parce que le DOJ décrit des notes de réunions, propositions de projet et autres documents internes, tandis que le Trésor a pris des mesures administratives distinctes. Le run conserve néanmoins le statut juridique : allégation/affidavit et désignation administrative ne valent pas jugement définitif au fond.
5. Storm-1516 est correctement décomposé : l'attribution d'opérations spécifiques au mode opératoire/écosystème est plus forte que le pont public direct `Storm-1516 -> GRU 29155`, qui ne doit pas être hérité d'une attribution cyber voisine.
6. `CAU-001..002` empêche le saut final : attribution d'une opération, attribution à un État et mesure d'un effet démocratique sont trois propositions distinctes ; persuasion, changement de vote et contrefactuel restent non identifiés dans le corpus scoped.

## P2

1. **Plovdiv** : absence de rapport technique avionique/public complet ou d'enquête bulgare détaillée dans le corpus inspecté. Recheck seulement si une pièce technique nouvelle apparaît.
2. **Rokh Solis / Storm-1516** : certains maillons de commanditaire/tasking restent partiels ou indirects. Recheck uniquement sur document contractuel, financier, judiciaire, renseignement déclassifié ou artefact technique réellement discriminant.
3. **Effet** : les conséquences sur perception, comportement, vote ou décision publique nécessitent des données d'exposition et un design causal ; davantage de rapports d'attribution ne comblera pas ce gap.

## RENARD

```text
RENARD = NO
```

Les résiduels ne menacent pas le modèle central. Ils exigent de nouvelles pièces techniques, de tasking ou de causalité. Ajouter d'autres cas d'attribution sans nouvelle classe de preuve serait cumulatif et violerait le gate delta-only. Les suites matérielles sont déjà routées vers `INV-137` (renseignement -> exécutif -> médias), `INV-144` (économie politique de la contre-ingérence, lorsque ses autres dépendances seront closes) et `INV-146` (symétrie alliés/adversaires, lorsque ses autres dépendances seront closes).
