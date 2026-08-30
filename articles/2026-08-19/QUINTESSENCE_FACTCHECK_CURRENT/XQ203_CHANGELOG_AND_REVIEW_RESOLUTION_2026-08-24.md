# XQ203 — Journal de révision et résolution des audits

Date de clôture éditoriale : 25 août 2026  
Base gelée : `QUINTESSENCE_ARTICLE_FACTCHECK_TRUST_XQ202_2026-08-24.md`  
Candidate révisée : `QUINTESSENCE_ARTICLE_FACTCHECK_TRUST_XQ203_2026-08-24.md`

## Décision synthétique

XQ203 conserve la thèse centrale, mais en réduit la portée : l’article démontre des modes d’échec possibles et des contre-exemples documentés ; il ne produit ni taux d’erreur sectoriel, ni verdict global sur les fact-checkers. La publication reste conditionnée à une décision humaine de promotion après BAT.

## Résolution par angle d’audit

| Angle | Risque principal détecté | Correction XQ203 | État |
|---|---|---|---|
| Contradiction épistémologique | Mélange entre statut de preuve, état du dossier et état du débat | Séparation en trois questions ; définition matérielle de la « surcertitude » | Résolu |
| Direction éditoriale | Promesse trop large et conclusion répétitive | Nouveau sous-titre, chapeau borné, encadré négatif avancé, conclusion resserrée | Résolu |
| Vérification forensique | Sources internes non rejouables, appels non contrôlés et ouverture AFP insuffisamment décomposée | Liens relatifs vers annexes/données, registre de 112 sources, cartographie de 151 relations et audit propositionnel des experts AFP/Spike | Résolu avec borne explicite |
| Droit | Raccourci entre attestations, passe et obligation vaccinale | Textes distingués ; décret et loi officiels ajoutés ; légalité explicitement hors champ | Résolu |
| Méthodologie | Accord de modèles susceptible d’être présenté comme preuve indépendante | Quatre lectures décrites comme tests adversariaux sur dossier commun ; résultats exacts et limites exposés | Résolu |
| Calibration sémantique | Catégories hétérogènes et verdicts trop binaires | Axes séparés, test de matérialité, distinction non-détection / non-démonstration / impossibilité | Résolu |
| Désinformation / instrumentalisation | Lecture possible comme « tous les fact-checkers mentent » ou comme argument antivaccinal général | Encadré « Ce que cette enquête n’établit pas », contre-preuves favorables et audit des exagérations dans les deux sens | Résolu |
| Avocat du diable | Sous-estimation de l’utilité et de la transparence du fact-checking | Méta-analyses, études comparatives et bons contre-exemples maintenus et mieux intégrés | Résolu |
| Réparation / circulation | Audience supposée commune sans preuve | Portée effective classée `INCONNUE` lorsque non mesurable ; reprise distinguée de corroboration | Résolu |
| KISS / exécution | Cadre abstrait et figures désynchronisées | Cycle ramené à trois niveaux, 14 critères, cinq figures alignées sur le texte puis refondues en style LaTeX monochrome imprimable | Résolu |

## Changements matériels

- Après la passe AFP/Spike : 11 999 mots dans le corps et 14 730 mots au total selon `wc -w`.
- Deux références juridiques primaires ajoutées : sources 102 et 103.
- Référence Yahoo limitée à une trace indexée, sans lui attribuer un contenu non rejouable.
- Archive premium de *Conspiracy Watch* non utilisée comme preuve de contenu ; contextualisation accessible privilégiée.
- Cas *Fact & Furious* borné à ce que les sources permettent effectivement d’établir.
- Test 14/41 documenté : 39 sorties valides communes aux quatre passes, 24 réponses brutes identiques, deux lacunes d’accès, aucun conflit substantiel entre réponses valides déterminées.
- Triple codage documenté : 154 affirmations, accords exacts de 41,6 %, 50,6 % et 75,3 %, coefficients κ faibles ; aucun taux général déduit.
- Cinq figures reconstruites en SVG et PNG, avec légendes synchronisées, puis refondues en style LaTeX/TikZ inspiré : Latin Modern, traits droits, gris uniquement, aucune information portée par la couleur seule.
- PNG normalisés à 2 400 × 1 500 px et 300 ppp ; épreuve simulée en noir et blanc 1 bit à 1 200 × 750 px : `PASS` sur les cinq figures.
- Comparaison textuelle avec les SVG précédents : aucune suppression sémantique substantielle ; seuls la numérotation, les repères de panneaux et la ponctuation changent, avec l’annotation explicative « CHANGEMENT DE STATUT → » en FIG. 03.
- L’ouverture AFP/Spike est reconstruite au niveau des sous-propositions : l’article reconnaît le sérieux formel du fact-check et la solidité de son objection au saut causal, tout en isolant la prémisse trop absolue « ne circule pas ».
- La vérification AFP mobilise plusieurs experts, mais l’affirmation de non-circulation est portée par Oliver Stojković ; Bogdanović/Babic admet de faibles quantités circulantes, David Walt borne la portée de la détection, et les autres experts répondent à d’autres propositions.
- Neuf références [104] à [112] ont été intégrées pour rendre contrôlables la version anglaise AFP, la biodistribution, les travaux Spike, les qualifications/publications de Stojković et l’expertise de Walt.
- SHA-256 courant de XQ203 : `26d902f33a5fcc83a72ae698b879fb41b29fb159c300189b5148757c7af6b456`.
- Paquet de réplication 14/41 assorti d’un manifeste d’empreintes SHA-256.

## Contrôles mécaniques

- 112 définitions de sources ; 112 sources citées au moins une fois.
- 187 appels de citation dans le corps.
- Zéro appel indéfini, zéro source inutilisée, zéro numéro manquant.
- 15 liens relatifs ; zéro cible relative manquante.
- 151 relations uniques section–source.
- Cinq SVG parsés sans erreur ; cinq PNG en niveaux de gris ; contraste minimal du texte courant : 7,46:1.
- Limite honnête : contrôle numérique effectué, mais aucune épreuve papier physique ni certification PDF/X n’a été réalisée.

Les métriques détaillées sont consignées dans `XQ203_MECHANICAL_AUDIT_2026-08-24.json` et `XQ203_FIGURE_PRINT_QA_2026-08-24.md`.


---

## XQ203A — patch de traçabilité post-audit — 25 août 2026

**Nature : données/dashboard uniquement. Article XQ203 inchangé.**

- Texte Yahoo du 23 juillet 2021 récupéré : le statut « corps non rejouable » est invalidé ; patch article P0 requis.
- Chronologie *Conspiracy Watch* corrigée : contextualisation fabrication / fuite accidentelle confirmée dès le 16 avril 2020 ; `Conspiracy News #16.2020` daté correctement au 20 avril 2020.
- `XQ200_COVID_ECOSYSTEM_FRESQUE.csv` : F200-004 corrigé, F200-045 ajouté.
- `XQ200_COVID_CLAIM_AUDIT.csv` : C200-001 enrichi avec la contextualisation précoce.
- `QUINTESSENCE_REPAIR_STRENGTH_CASES_2026-08-24.csv` : RS06 ajouté.
- Nouveau registre `XQ203A_EDITORIAL_FORENSIC_AUDIT_2026-08-25.csv` : 22 findings.
- Nouveau registre `XQ203A_RESEARCH_SOURCE_REGISTRY_2026-08-25.csv` : 8 sources.
- Nouveau `XQ203A_POSTAUDIT_TRACE_2026-08-25.json`.
- SQLite XQ196 canonique retrouvé en Library puis enrichi dans le paquet : 37 findings dont 22 XQ203A, 17 sources dont 8 XQ203A, 8 gaps ; intégrité SQLite `ok`.
- QA typographique : 4 tirets cadratins encore présents -> FAIL.
- QA terminologique : plusieurs premières occurrences non définies -> patch requis.
- QA mobile : 5 figures suffisantes en nombre, mais textes secondaires trop petits en affichage pleine largeur 390 px.
- Preuve QA mobile conservée : `annexes/XQ203A_MOBILE_FIGURE_QA_390PX.png`.
- Cascade d’archéologie documentaire enregistrée et bornes négatives verrouillées.

`XQ203A_ARTICLE_TEXT_CHANGE = NO`  
`XQ203A_TRACEABILITY = UPDATED`  
`PUBLICATION_DECISION = HOLD_FOR_P0_PATCH`
