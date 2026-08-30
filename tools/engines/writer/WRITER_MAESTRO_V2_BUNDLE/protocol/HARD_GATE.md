# HARD_GATE
## Validation objective et factuelle

Séparer deux catégories.

# A. HARD GATE DÉTERMINISTE

Tester automatiquement lorsque possible :

- tiret cadratin interdit ;
- guillemets français équilibrés ;
- espaces insécables selon la charte ;
- doubles espaces ;
- identifiants internes interdits ;
- structure Markdown ;
- URLs attendues ;
- mots explicitement interdits ;
- contraintes de publication.

# B. FACTUAL GATE ASSISTÉ

Contrôler, lorsque le matériau structuré existe :

- chiffres ;
- dates ;
- noms ;
- citations ;
- correspondance avec le FACT_REGISTRY ;
- niveau de preuve ;
- causalités autorisées.

Ne jamais prétendre que le factual gate est déterministe si l’alignement phrase ↔ claim repose sur un LLM.

Verdicts :

- `PASS`
- `FAIL`
- `UNCERTAIN`

`UNCERTAIN` n’est jamais converti automatiquement en `PASS`.
