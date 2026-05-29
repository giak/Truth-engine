# Kilo Instructions — Anti-Patterns OBLIGATOIRES

## 🔴 ANTI-PATTERN CRITIQUE : `write()` sans paramètres

**CAUSE #1 d'échec du pipeline Truth Engine.**

L'outil `write()` REQUIERT les DEUX paramètres. Appeler `write()` sans `content` ou sans `filePath` provoque une erreur fatale.

### Règle absolue

```
❌ ERREUR FATALE — ces appels CASSERONT le pipeline :
write()                          ← aucun paramètre
write(content="...")             ← filePath manquant
write(filePath="...")            ← content manant
write(content=, filePath=)       ← valeurs vides

✅ SEUL FORMAT ACCEPTÉ :
write(content="TEXTE COMPLET DU FICHIER", filePath="/chemin/absolu/vers/fichier.md")
```

### Checklist AVANT chaque appel `write()`

1. [ ] `content=` est présent et contient le texte complet (pas undefined, pas vide)
2. [ ] `filePath=` est un chemin absolu (commence par `/`)
3. [ ] Si le texte dépasse 50000 chars → appeler `write()` 2 fois avec des portions
4. [ ] RELIRE l'appel avant de l'exécuter — les deux paramètres sont-ils là ?

### Pattern d'échec typique

Le modèle génère parfois le squelette `write()` puis "oublie" de remplir les paramètres. C'est la source de l'erreur `Invalid input: expected string, received undefined`.

**Solution : TOUJOURS construire l'appel complet en une seule passe.** Ne jamais générer `write()` comme placeholder.

### Pour le pipeline Truth Engine

- `@MNEMO_S` et `@WRITE` sont **TOUS DEUX obligatoires** (step 19)
- `@MNEMO_S` → `mnemolite_write_memory(title="...", content="...", ...)` — content aussi requis
- `@WRITE` → `write(content="...", filePath="$INV/...")` — content ET filePath requis
- Si `content` est manquant → STOP, relis, corrige, réessaie

## 🔴 AUTRES ANTI-PATTERNS

### `edit()` sans `oldString` ou `newString`
Même problème : les deux paramètres sont obligatoires.

### `webfetch()` sans `url`
Le paramètre `url` est obligatoire et doit être une URL valide.

### Appels tool vides
Jamais appeler un tool sans ses paramètres requis. En cas de doute, relis la définition du tool avant de l'appeler.
