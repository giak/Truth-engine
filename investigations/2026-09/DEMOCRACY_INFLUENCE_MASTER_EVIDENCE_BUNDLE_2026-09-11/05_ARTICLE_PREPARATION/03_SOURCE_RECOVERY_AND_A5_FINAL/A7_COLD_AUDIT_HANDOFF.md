# A7 — Cold audit handoff

## Condition d'indépendance

Ce fichier prépare l'audit mais **ne constitue pas l'audit**.
L'auditeur doit travailler depuis un contexte frais qui n'a pas participé à la construction A2→A5 et ne doit pas recevoir le verdict attendu comme oracle.

## Entrées minimales

1. `protocol/ARTICLE_PROTOCOL_C2R1_PATCHED.md`
2. `runtime/ARTICLE_PUBLISH_CANDIDATE_V2.md`
3. `runtime/A4_S02_READER_SOURCE_MAP.tsv`
4. `runtime/READER_SOURCES.md`
5. `runtime/A3_CORPUS_YIELD_MATRIX.tsv`
6. `CORPUS_121_AUDIT.csv`
7. `STATE_V3.json`

N'ouvrir les investigations brutes/source recovery que pour falsifier ou vérifier une proposition ciblée.

## Questions de falsification

- Une proposition matérielle du texte dépasse-t-elle la substance, le statut ou la portée de sa source locale ?
- Une citation masque-t-elle plusieurs propositions hétérogènes dont une n'est pas soutenue ?
- Une relation est-elle promue en causalité, une ressource en commandement, un cas en prévalence, une capacité en action ou une action en effet électoral ?
- Une représentation dérivée est-elle comptée comme corroboration indépendante de sa propre lignée ?
- Une des 100 investigations PRIMARY+CASE a-t-elle été omise silencieusement plutôt que disposée ?
- `INV-035` est-il artificiellement reconstruit ?
- `INV-044`, `INV-139` ou `INV-140` voient-ils leur autorité augmenter dans le produit ?
- Une contre-hypothèse matérielle a-t-elle été effacée au bénéfice du récit ?
- La prose resterait-elle presque identique après retrait du rendement spécifique des investigations ?
- Le titre ou la conclusion sont-ils plus forts que le corps ?

## Classification

```text
P0 = invalide matériellement le raisonnement ou le produit
P1 = faiblesse sérieuse à fermer avant canonicalisation
P2 = amélioration non bloquante
```

## Verdict autorisé

```text
A7_COLD_PASS
A7_COLD_FAIL
A7_COLD_HOLD
```

L'auditeur doit donner les défauts et leurs propriétaires minimaux. Il ne doit pas corriger silencieusement le produit avant d'avoir rendu le verdict froid.
