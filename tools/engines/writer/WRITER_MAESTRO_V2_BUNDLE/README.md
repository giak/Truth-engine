# WRITER MAESTRO v2 : Bundle

## But

Réécrire ou produire de longs textes français en privilégiant, dans cet ordre :

1. faits ;
2. sens ;
3. niveau de preuve ;
4. validité du raisonnement ;
5. cohérence ;
6. intelligibilité ;
7. syntaxe et précision lexicale ;
8. naturel du français ;
9. rythme ;
10. élégance ;
11. effet rhétorique.

Le principe d’architecture est simple :

> Multi-agent pour la critique, mono-agent pour la plume.

Les reviewers diagnostiquent. Un seul WRITER modifie le texte maître.

---

## Contenu

```text
WRITER_MAESTRO_V2_BUNDLE/
├── README.md
├── MAESTRO.md
├── LONG_FORM.md
├── prompts/
│   ├── REWRITE_ARTICLE.md
│   ├── ARCHITECT.md
│   ├── LINGUIST.md
│   └── RED_TEAM.md
├── protocol/
│   ├── GLOBAL_STATE.md
│   ├── REVIEW_FORMAT.md
│   ├── SEMANTIC_DIFF.md
│   └── HARD_GATE.md
├── tests/
│   ├── MUTATION_TESTS.md
│   └── ACCEPTANCE_CHECKLIST.md
└── examples/
    └── INVOCATION.md
```

---

# Démarrage rapide

## Cas A : Article court ou moyen

Charge :

1. `MAESTRO.md`
2. `prompts/REWRITE_ARTICLE.md`
3. ton article

Puis demande l’exécution.

## Cas B : Article long

Charge :

1. `MAESTRO.md`
2. `LONG_FORM.md`
3. `prompts/REWRITE_ARTICLE.md`
4. ton article

Le mode LONG FORM impose une cartographie globale avant toute réécriture et maintient un `GLOBAL_STATE` compact pendant le travail.

---

# Entrées facultatives

Le système peut aussi recevoir :

- un `FACT_REGISTRY` ;
- un blueprint narratif ;
- une charte éditoriale ;
- des contraintes de publication ;
- un corpus documentaire.

S’ils existent, ils priment sur les connaissances générales supposées du modèle.

---

# Règle de sobriété

Ne pas produire systématiquement tous les artefacts internes.

Le `GLOBAL_STATE`, les diagnostics et le `SEMANTIC_DIFF` servent le processus. Ils ne sont rendus à l’utilisateur que si celui-ci les demande.

---

# Principe d’arrêt

Aucune nouvelle passe générale si aucun défaut précis ne la justifie.

Cycle normal :

```text
cartographier
→ rédiger
→ diagnostiquer
→ arbitrer
→ réparer
→ contrôler
→ terminer
```

Si un défaut précis subsiste :

```text
réparation ciblée
→ contrôle ciblé
```

Jamais :

```text
réécrire
→ repolir
→ repolir
→ repolir
```

---

# Limites

Ce protocole réduit les risques de régression ; il ne prouve pas mathématiquement leur absence.

Le `SEMANTIC_DIFF` est un contrôle heuristique. Pour les faits critiques, un registre structuré ou une vérification externe reste préférable.

Les très longs textes ne doivent pas dépendre d’une mémoire implicite du modèle : le mode LONG FORM construit une représentation globale compacte et la réinjecte pendant les réécritures locales.
