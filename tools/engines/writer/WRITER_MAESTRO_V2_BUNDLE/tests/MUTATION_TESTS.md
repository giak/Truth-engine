# MUTATION TESTS
## Banc de tests de prose

But : tester si les reviewers détectent les défauts sans dégrader les passages sains.

Construire progressivement un corpus de référence.

Pour chaque fragment sain, produire des mutations contrôlées.

## Familles minimales

### M1 : Durcissement épistémique
Original :
« Ces données suggèrent une relation. »

Mutation :
« Ces données démontrent une relation. »

Attendu :
détection P0.

### M2 : Causalité abusive
Original :
« A finance B. B participe à C. »

Mutation :
« A contrôle C par l’intermédiaire de B. »

Attendu :
détection P0 sauf preuve spécifique.

### M3 : Connecteur nécessaire supprimé
Retirer un « pourtant », « en revanche », « parce que » ou autre marqueur lorsque la relation devient ambiguë.

Attendu :
détection méso, pas doctrine « connecteurs = mauvais ».

### M4 : Connecteur mécanique ajouté
Ajouter « Par ailleurs » entre deux phrases sans relation.

Attendu :
détection P1/P2.

### M5 : Pronom ambigu
Remplacer un nom clair par « il », « elle », « celui-ci » avec deux antécédents possibles.

Attendu :
détection P1.

### M6 : Phrase longue claire découpée
Transformer une période cohérente en plusieurs phrases hachées qui perdent leur hiérarchie logique.

Attendu :
le reviewer doit défendre la structure saine.

### M7 : Faux synonyme
Remplacer « dépendance » par « influence », ou « possible » par « probable ».

Attendu :
détection P0/P1 selon portée.

### M8 : Punchline artificielle
Insérer un fragment spectaculaire sans fonction ni preuve.

Attendu :
détection rhétorique.

### M9 : Répétition structurelle
Répéter une conclusion déjà démontrée dans trois sections.

Attendu :
détection transversale.

### M10 : Régression par correction
Donner au système une version source correcte et une « amélioration » plus élégante mais sémantiquement plus forte.

Attendu :
SEMANTIC_DIFF = REGRESSION.

---

# Métriques utiles

Mesurer séparément :

- rappel : défauts injectés détectés ;
- précision : critiques réellement fondées / critiques émises ;
- faux positifs sur passages sains ;
- régressions introduites par les réparations ;
- stabilité des passages explicitement protégés.

Ne pas utiliser une « note globale de style » comme métrique principale.
