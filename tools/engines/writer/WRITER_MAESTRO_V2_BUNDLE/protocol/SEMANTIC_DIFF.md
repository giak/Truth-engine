# SEMANTIC_DIFF
## Contrôle de non-régression

Ce contrôle est heuristique. Il ne constitue pas une preuve formelle d’identité sémantique.

Pour chaque passage substantiellement modifié, extraire AVANT et APRÈS :

```text
ACTEUR:
ACTION / RELATION:
OBJET:
QUANTITÉ:
TEMPORALITÉ:
MODALITÉ:
NÉGATION:
CONDITION:
EXCEPTION:
CAUSALITÉ:
DEGRÉ DE CERTITUDE:
```

Puis comparer :

```text
AVANT:
[...]

APRÈS:
[...]

DIFF:
[...]

VERDICT:
SAFE
ou
CHANGED_BUT_JUSTIFIED
ou
REGRESSION
```

## REGRESSION si, sans justification explicite :

- « peut » devient « va » ;
- « suggère » devient « démontre » ;
- « associé à » devient « cause » ;
- « certains » devient « tous » ;
- disparition d’une négation ;
- disparition d’une exception ;
- changement de sujet ou d’objet ;
- changement de période ;
- transformation d’une hypothèse en fait ;
- transformation d’une relation en intention.

Toute `REGRESSION` bloque la correction.

Pour un article long, comparer également le `GLOBAL_STATE` final au `GLOBAL_STATE` initial.
