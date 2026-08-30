# Contrat du validateur externe — V5.1-FROZEN

Le prompt `V5.1-FROZEN` est immuable et son SHA-256 reste la référence.

Le validateur ne juge jamais le fond. Il normalise uniquement la forme et applique les règles mécaniques.

## Normalisations

- Plusieurs blocs `EVIDENCE_YES` ou `EVIDENCE_NO` sont acceptés comme **liste de preuves** lorsqu’un atome mobilise plusieurs sources obligatoires.
- Une même `SOURCE_ID` répétée dans le même côté de preuve est une erreur.
- Les dépassements de 25 mots dans `EXACT_EXCERPT` sont des **warnings de forme**, pas une invalidation probatoire.
- Les divergences `SOURCE_TYPE` par rapport à la taxonomie canonique sont des warnings et sont normalisées en aval.

## Invalidation locale

Un atome devient `PROTOCOL_INVALID` notamment si une source `REQUIRED` nécessaire n’a pas été ouverte, si aucune preuve décisive ouverte ne soutient une réponse ferme, si un atome `TEXT` ferme n’a pas de preuve directe, ou si une preuve `AT_T` viole le cutoff.

Une invalidation locale n’annule pas les autres atomes.
