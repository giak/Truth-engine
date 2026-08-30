# AUDIT FORENSIQUE SPÉCIFIQUE DES FIGURES — R17

## Objet

Audit dédié des huit figures de la R16, avec contrôle de quatre dimensions :

1. cohérence sémantique avec le texte ;
2. niveau de causalité et de certitude suggéré par le visuel ;
3. séparation des métriques et des catégories ;
4. intégrité graphique et mécanique du SVG.

Verdict sur la R16 : **HOLD_FIGURES**. Aucun chiffre de figure faux détecté, mais cinq P1 sémantiques et trois P2 de précision/lecture ont été identifiés. Tous sont corrigés dans la R17.

## Matrice d'audit

| Figure | R16 | Gravité | Défaut | Réparation R17 | Verdict |
|---|---|---|---|---|---|
| FIG. 00 | Fresque historique | P1 | La ligne « droits sociaux » contenait aussi carrière, crédit, logement, statut : catégorie trop étroite et donc trompeuse. | Ligne renommée « Revenus, droits et trajectoires s’adossent à » ; sous-titre et conclusion bornés. | PASS |
| FIG. 01 | Chaîne de conversion | P1 | Mélange entre « gain brut », « temps net libéré », « capacité disponible » et gain économique, alors que la R16 distingue capacité nette libérée et productivité. | Chaîne normalisée : capacité technique → temps brut → frottements → capacité nette libérée → usage de la capacité ; rappel que la capacité libérée n’est pas encore une productivité. | PASS |
| FIG. 02 | Déplacement de contrainte | P1 | La grande flèche Validation → Données → Fiabilité → Demande → Autorité suggérait une succession unique que le texte ne soutient pas. | Suppression de la flèche directionnelle ; mention explicite « contraintes non ordonnées ». | PASS |
| FIG. 03 | Emploi visible / contrefactuel | P2 | « Contrefactuel » était trop catégorique pour le recrutement différé, qui peut parfois laisser une trace ; « licenciement direct » était plus étroit que la catégorie. | « Principalement contrefactuel », « recrutement reporté ou évité », « licenciement enregistré », synthèse plus générale. | PASS |
| FIG. 04 | Demande et prix | P2 | « Capacité nette » et « point de départ mesuré » étaient moins précis que la définition du texte ; la chaîne pouvait être prise pour un ordre causal. | « Capacité nette libérée », « point de départ à établir », footer « ordre non causal ». | PASS |
| FIG. 05 | Exposition en réseau | P2 | Les flèches amont → latéral → aval et prix → budgets → parts de marché → statuts → volume imposaient une circulation unidirectionnelle. | Suppression des flèches inter-blocs ; variables de transmission rendues bidirectionnelles. | PASS |
| FIG. 06 | Production d’expérience | P1 | La R16 visuelle affirmait « certaines embauches de début de carrière ↓ » sous une flèche causale IA, alors que Stanford/Census donnent surtout des associations et que l’effet net futur n’est pas établi. | « certaines embauches peuvent ↓ », « certaines tâches d’entrée », apprentissage également modalisé ; footer explicite Stanford/Census non causaux, QJE apprentissage, effet net inconnu. | PASS |
| FIG. 07 | Registre d’incidence | P1 | « Gain économique net » incluait « temps libéré », ce qui réintroduisait la confusion que la R16 avait corrigée entre capacité nette libérée et gain/productivité économique. « Circuit du dividende IA » pouvait aussi faire croire à une grandeur mesurée. | « Effet initial à établir », « capacité nette libérée », « circuit analytique d’incidence », variables de partage non séquentielles. | PASS |

## Contrôles factuels ciblés

### FIG. 00

La figure reste une fresque analytique et non une chronologie causale. Les jalons utilisés restent cohérents avec les sources du corps : Thompson (travail orienté par la tâche), OIT 1919, Taylor 1911, histoire française de la durée du travail, tertiarisation et transformation socioprofessionnelle Insee. Les périodes sont présentées comme régimes superposés et non comme ruptures exactes.

### FIG. 06

Le canal « portes d’entrée » ne doit pas être représenté comme causalement établi. Stanford (révision août 2026) observe un écart d’emploi chez les 22–25 ans exposés mais qualifie les résultats de descriptifs ; le Census CES-26-27 observe une baisse relative des embauches et de l’emploi dans les cellules les plus exposées, sans suffire à identifier une causalité générale. Le QJE établit en revanche, dans un contexte précis de service client, que les moins expérimentés bénéficient davantage de l’assistance et progressent plus vite. La R17 encode désormais cette asymétrie de preuve.

### FIG. 07

La figure ne traite plus une heure libérée comme un « gain économique net ». Elle impose d’abord d’établir la nature de l’effet : capacité nette libérée, qualité, coût évité, capacité supplémentaire. L’incidence vient ensuite. Cette correction est nécessaire pour rester cohérent avec la section II de l’article.

## QA graphique et mécanique

- 8/8 SVG parsés sans erreur XML.
- 8/8 rendus Inkscape réussis.
- 8/8 figures contenues dans leur viewBox 2400 × 1500 ; aucun objet détecté hors canevas.
- Polices TeX Gyre Termes et TeX Gyre Heros disponibles au rendu.
- Aucun tiret cadratin dans les SVG.
- 8/8 références Markdown correspondent à un SVG présent.
- Prévisualisations PNG générées pour les huit figures.
- Inspection visuelle manuelle : pas de collision de texte, pas de clipping, hiérarchie et contraste cohérents.

## Limite de l'audit

Les figures analytiques ne sont pas des modèles estimés. Le contrôle vérifie la compatibilité avec les sources et le texte, la modalité causale, les catégories et la représentation graphique. Il ne reproduit pas les estimations économétriques des travaux académiques cités.

## Verdict

**R16 : HOLD_FIGURES**

**R17 : GO_FIGURES**

La R17 ne modifie le corps de l'article qu'à un seul endroit : le libellé Markdown de la FIG. 07 passe de « Du gain économique à la personne » à « De l’effet économique à la personne ». Les 71 sources et tous les autres claims du texte restent inchangés.
