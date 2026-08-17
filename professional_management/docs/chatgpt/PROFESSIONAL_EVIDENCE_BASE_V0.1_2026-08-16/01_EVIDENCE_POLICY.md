# Evidence Policy — V0.1

## Contrat

Cette base n'est ni un CV ni un document marketing. Elle sert à empêcher qu'un export professionnel affirme davantage que les pièces ne permettent d'établir.

Règle centrale :

`SOURCE → OBSERVATION → EVIDENCE_EDGE → CLAIM → STATUT → EXPORT`

Une source n'a **pas** de valeur probatoire absolue. La question est : *que prouve-t-elle exactement pour ce claim précis ?*

## Statuts

- **OBSERVED** : mesuré ou constaté directement dans une source de plateforme/artefact.
- **DOCUMENTED** : explicitement documenté dans une pièce pertinente, généralement first-party.
- **CORROBORATED** : plusieurs origines réellement indépendantes convergent.
- **SELF_REPORTED** : affirmation autobiographique ou auto-documentation sans corroboration indépendante.
- **INFERRED** : conclusion raisonnée à partir de claims sous-jacents.
- **CONFLICTED** : données incompatibles à définition/date comparables.
- **UNSUPPORTED** : claim identifié sans pièce probante.
- **UNKNOWN** : information non encore déterminée.
- **REJECTED** : claim abandonné.

## Publicabilité

- **YES** : formulation publiable dans sa portée exacte.
- **CAUTION** : publiable avec attribution/qualification (« le README documente… », « expérience revendiquée… ») ou après une vérification simple.
- **BLOCKED** : ne doit pas apparaître comme fait dans CV/portfolio/offre tant que la gate n'est pas levée.

## Trois preuves commerciales distinctes

1. **Fabrication** : l'artefact existe, le code/architecture est inspectable.
2. **Utilisation** : des utilisateurs/clients s'en servent réellement.
3. **Valeur** : un effet mesuré est attribuable au système (temps, coût, qualité, ROI).

Une preuve de fabrication ne vaut pas preuve d'utilisation. Une preuve d'utilisation ne vaut pas preuve de ROI.

## Indépendance

Deux documents écrits par la même personne ne constituent pas deux corroborations indépendantes.
`CV + portfolio + README + Substack` peuvent relever d'un seul groupe d'origine : `GIACOMEL_SELF`.

## Métriques

Aucune métrique d'un projet vivant n'est écrasée. Chaque valeur est une observation datée avec :
- définition/unité ;
- méthode ;
- source ;
- date ;
- éventuel `supersedes`.

Deux nombres différents ne sont un conflit que si sujet + définition + date/période sont comparables.

## Claims interdits par défaut

Sans preuve spécifique :
- « expert » / « meilleur » ;
- « zéro perte » / « zéro hallucination » ;
- « construit seul » au sens d'auteur exclusif ;
- « production » pour un démonstrateur ;
- ROI, gains %, disponibilité, satisfaction ;
- conformité « 100 % » ;
- sécurité absolue.

## Gate d'export

Un claim `commercial_value=HIGH` et `publicability=BLOCKED` ne doit jamais être injecté dans un export public.
