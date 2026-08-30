# XQ203 — Contrôle forensique des figures pour impression

Date : 24 août 2026 ; contrôle de non-régression après patch AFP/Spike le 25 août 2026  
Périmètre : FIG. 01 à FIG. 05, formats SVG et PNG  
Décision : `FIG_SYNC_PRINT_QA = PASS`

## Résultat honnête

Les cinq figures ont été refondues dans un langage visuel proche de LaTeX/TikZ : police Latin Modern, règles fines, angles droits, gris légers, hachures et doubles cadres. Elles restent des SVG écrits directement, et non des exports compilés depuis TikZ.

Le contrôle numérique confirme leur aptitude à une impression standard en niveaux de gris. Il ne remplace pas une épreuve papier physique, un contrôle d’imprimeur ni une certification PDF/X.

## Contrôles exécutés

| Contrôle | Méthode | Résultat |
|---|---|---|
| Validité structurelle | Parsing XML des cinq SVG | PASS — 5/5 |
| Rendu | Inkscape vers PNG | PASS — 5/5 |
| Dimensions | Inspection ImageMagick | PASS — 2 400 × 1 500 px |
| Densité | Métadonnée PNG | PASS — 300 ppp (118,11 px/cm) |
| Couleur | Inspection des canaux raster | PASS — `Gray/Grayscale`, aucune couleur résiduelle |
| Palette SVG | Noir, graphite et gris uniquement | PASS |
| Contraste du texte | Ratio minimal calculé : `#555555` sur blanc | PASS — 7,46:1 |
| Réduction | 1 200 × 750 px | PASS visuel — 5/5 |
| Noir et blanc strict | Seuil 1 bit à 82 % après réduction | PASS visuel — 5/5 |
| Contenu | Diff des nœuds textuels avec les SVG précédents | PASS WITH NOTE |
| Synchronisation article | Noms de fichiers et cibles relatives inchangés | PASS — 5/5 |

## Contenu : ce qui a réellement changé

- Aucune phrase factuelle ou méthodologique substantielle n’a été retirée.
- La numérotation est normalisée (`FIG. 01` à `FIG. 05`).
- Les panneaux reçoivent des repères `(a)`, `(b)`, `(c)` lorsque cela facilite la lecture.
- Les séparateurs typographiques `|` ou `•` deviennent des points médians `·` sans changement de catégorie.
- FIG. 03 ajoute « CHANGEMENT DE STATUT → », explicitation graphique de son titre et de la transition déjà décrite.
- Lors de la refonte graphique du 24 août, aucun claim, aucune citation et aucune source de l’article n’avaient été modifiés. Le patch forensique AFP/Spike du 25 août a ensuite modifié le texte et porté le registre à 112 sources, sans changer le contenu sémantique, les légendes ni les cibles des cinq figures. Le SHA-256 courant de l’article est `26d902f33a5fcc83a72ae698b879fb41b29fb159c300189b5148757c7af6b456`.

## Empreintes avant / après

Les empreintes « avant » proviennent du paquet XQ203 gelé avant cette refonte graphique.

| Figure | SVG avant | SVG après | PNG avant | PNG après |
|---|---|---|---|---|
| FIG. 01 | `c14b4bc2b70f33790fc6c39f22ef6cec394a5b508fb382316661b76a94c14d8a` | `4ff8a69f22eaccf1aae4963d45d205a8cd2cf3641bbca9ecafc227b51fdc0df7` | `3b2c2e6cd188e46ba41961f0bdd48c384abd9391e3327f0e73d1ee5e1322c79f` | `163e4b38be25f9a1fc2a03ce38db9be1bcc4f4fa5d0630dde4bcb83e2b87ddbd` |
| FIG. 02 | `f77b35ab4ee45048c6f66034142c6fbc91c66e20aec88a5e2984f9e1420a915f` | `0a6143aae5ac1be17f5f195f6a84146f9fb3db1298ee91076dece9ba5c78edb8` | `eb2c4323d69dbc68d06b37192c66da3d23fbc40fb8eeaf30236faac8b69ed07c` | `07713c717b3f3af0c0a9d4bf3f8f494af47c28e75dae3eb378d8f8b306a4c4db` |
| FIG. 03 | `8365f676c58b9fe0f1b4de7dcdf8d4321b48dd95e8b3b1c87ca7c84eea202763` | `be4275e48fc448e882d3f269d95ebc506c7fa50a86e038e877d0a0c2d132efae` | `414948ca9e53725b76df58906bf4b6eb45a2b50f44d4f1933bd09e7d3edcfa8c` | `a704f1711ad4c3f7ec67e9b554162b434de57483fa48976052e923c48623b21d` |
| FIG. 04 | `5b79f0743e6381309e148ebb8c05de4dc525a6c42b0743179812ebdcf9d5b5e6` | `220293fce6558fce44bf75e9415429290de06e64539976c84c394af64519790d` | `765a7ced6bd9734c031c3e97a71f5c6686d4f32ad00cb1c878bb2e8ea9ca39d7` | `f32f435740d80916c2a55b224e29437355145d34116fccede02402f459181671` |
| FIG. 05 | `5d77c796a78e1192f44e618fb67020d3de0d7452549533412cc197602bd53595` | `a3499d165aa982e17583fdee455407676ea68f3cc4f7dd13cc2b0d23719ee404` | `e5d2224d252cd8a153f66041e32b5ca7cef55a037fb7bd5d71d5ef72aade4ab1` | `b22a72ebe333052d7a918138e0fc6d044b6aba799ab70125c7907e520b81b1d7` |

## Limites et décision de publication

- Le PNG constitue le rendu figé le plus portable ; le SVG reste éditable et dépend de la disponibilité de Latin Modern pour éviter une substitution de police.
- Les trames très claires peuvent disparaître sur une imprimante monochrome agressive ; les doubles cadres et libellés conservent néanmoins l’information.
- `PUBLICATION_DECISION` reste `PENDING_HUMAN`. Le passage de ce gate visuel ne promeut pas automatiquement XQ203 à la place du master XQ199.
