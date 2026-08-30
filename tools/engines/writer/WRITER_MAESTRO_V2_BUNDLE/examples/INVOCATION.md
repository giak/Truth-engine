# EXEMPLES D’INVOCATION

## 1. Réécriture simple

Charge :

- `MAESTRO.md`
- `prompts/REWRITE_ARTICLE.md`
- article

Instruction :

> Exécute la tâche de réécriture. Retourne uniquement l’article final.

---

## 2. Article long

Charge :

- `MAESTRO.md`
- `LONG_FORM.md`
- `prompts/REWRITE_ARTICLE.md`
- article

Instruction :

> Exécute en mode LONG FORM. Construis d’abord le GLOBAL_STATE, puis réécris par unités cohérentes. Ne rends que l’article final.

---

## 3. Audit sans réécriture

Charge :

- `MAESTRO.md`
- `prompts/LINGUIST.md`
- `prompts/RED_TEAM.md`
- article

Instruction :

> Audite uniquement. Ne réécris rien. Fusionne et déduplique les P0/P1 ; conserve séparément les désaccords.

---

## 4. Avec dossier factuel

Charge en plus :

- FACT_REGISTRY ;
- blueprint ;
- charte de publication.

Instruction :

> Le FACT_REGISTRY et le blueprint sont les références du fond. MAESTRO traite la composition et la langue. Toute affirmation non soutenue par le matériau autorisé doit être retirée, qualifiée ou signalée.
