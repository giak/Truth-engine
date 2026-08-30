# LONG FORM
## Stratégie pour articles longs

Ce fichier complète `MAESTRO.md`.

Principe :

> Découper l’exécution, jamais la compréhension.

Pour un long texte, ne pas supposer que le modèle conservera implicitement une attention uniforme sur l’ensemble de l’article.

Construire un `GLOBAL_STATE` compact avant toute réécriture.

---

# 1. Phase 0 : Évaluer la taille

Si l’article et les instructions tiennent confortablement dans le contexte utile :

- lecture globale directe.

Sinon :

- lecture hiérarchique par unités cohérentes ;
- synthèse globale à partir des cartes locales.

Ne jamais découper uniquement sur un nombre arbitraire de mots si une frontière argumentative plus naturelle existe.

---

# 2. Phase 1 : Cartographie

Aucune réécriture.

Construire progressivement :

- thèse centrale ;
- sous-thèses ;
- architecture ;
- fonction de chaque grande section ;
- concepts à terminologie stable ;
- faits/chiffres critiques ;
- degrés de certitude sensibles ;
- objections ;
- répétitions structurelles ;
- passages fragiles ;
- passages à protéger.

---

# 3. Phase 2 : GLOBAL_STATE

Produire un état compact selon `protocol/GLOBAL_STATE.md`.

Le GLOBAL_STATE doit rester assez court pour être réinjecté pendant chaque opération locale.

Il est une mémoire éditoriale, pas un résumé littéraire.

---

# 4. Phase 3 : Réécriture locale sous contrainte globale

Travailler par unités argumentatives ou narratives cohérentes.

Pour chaque unité fournir au WRITER :

```text
GLOBAL_STATE
PREVIOUS_EDGE
CURRENT_SOURCE
NEXT_EDGE
```

`PREVIOUS_EDGE`
: comment finit l’unité précédente et ce qu’elle a déjà établi.

`CURRENT_SOURCE`
: unité source actuelle.

`NEXT_EDGE`
: ce que l’unité suivante devra reprendre ou développer.

Règle :

> Unité de travail locale, état éditorial global.

Ne jamais optimiser une section isolément au détriment de l’article entier.

---

# 5. Phase 4 : Recomposition

Assembler les unités réécrites sans nouvelle optimisation stylistique générale.

Vérifier uniquement :

- raccords ;
- références ;
- répétitions transversales ;
- ordre des démonstrations ;
- stabilité terminologique ;
- stabilité des niveaux de preuve ;
- cohérence entre introduction, corps et conclusion.

---

# 6. Phase 5 : Revue transversale

Questions :

- Une définition apparaît-elle plusieurs fois sans fonction ?
- Une conclusion est-elle annoncée avant sa démonstration ?
- Un chiffre est-il répété sans nécessité ?
- Une section répète-t-elle une conclusion déjà établie ?
- Un concept change-t-il de nom ou de portée ?
- Un pronom renvoie-t-il à un antécédent trop éloigné ?
- Une section nécessite-t-elle une transition réelle ?
- La conclusion finale est-elle encore autorisée par le corps ?

Corriger uniquement les défauts détectés.

Pas de nouvelle « passe de style ».

---

# 7. Phase 6 : SEMANTIC_DIFF global

Comparer les invariants du GLOBAL_STATE à la version finale :

- thèse ;
- propositions cardinales ;
- faits/chiffres sensibles ;
- relations causales ;
- modalités ;
- négations ;
- exceptions ;
- temporalités ;
- degrés de certitude ;
- objections significatives.

Toute divergence injustifiée doit être réparée.

---

# 8. Politique de correction

Ne pas imposer « une seule passe » comme dogme.

Appliquer :

```text
draft
→ revue
→ réparation
→ contrôle
```

Si `PASS` : fin.

Si un défaut précis subsiste :

```text
réparation ciblée
→ contrôle ciblé
```

Aucune nouvelle passe générale sans défaut explicite.

---

# 9. Politique de longueur

Ne jamais imposer une réduction arbitraire de 10 %, 15 % ou autre.

Supprimer :

- répétition inutile ;
- digression ;
- formulation vide ;
- transition redondante.

Conserver toute longueur qui sert réellement :

- une démonstration ;
- une distinction ;
- une objection ;
- une nuance ;
- une explication nécessaire.
