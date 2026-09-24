# BRAINSTORM — Schémas et figures pour la V5 Insee

Cible : `articles/2026-09-23_06-00_insee-v5-v38_ce-que-linsee-ne-vous-dira-jamais_ARTICLE.md` (11 sections, 44 notes, ~8 600 mots).
Grammaire de référence : `tools/engines/visual/chatgpt.md` (prompt maître « figures quasi-LaTeX »), confronté au code réel des SVG de référence, pas à leur description.
Références lues : `articles/2026-08-26/IA_TRAVAIL_ARTICLE_ARCHIVE_2026-08-26/09_REFERENCE_STYLE_FACTCHECK/root_svg/` (4 SVG) et `articles/AUDIT_ARTICLE_POUVOIR_V4_4_FULL_FORENSIC/01_TARGET/figures/svg/` (10 SVG).
Date : 23 septembre 2026, 06 h 11.

---

## 1. Ce que le code des références impose (relevé, pas souvenir)

**Série « IA et travail »** — `FIG_03_MODELE_AU_SLOGAN_X12.svg` déclare :

```
canevas          2400 × 1500, fond #ffffff
kicker gauche    x=90 y=78     kicker droit x=2310 y=78 (text-anchor end)
filet header     y=112, .rule 2.4 px
titre            y=214, .title 60 px, serif
sous-titre       y=278, .sub 29 px, #3d3d3d
panneaux         x=70, 525, 980, 1435, 1890 ; 400 × 380 ; gap 55
classes          .rm .sf .math ; .kicker 27/2.6 ; .tag 24/1.3 ; .head 35 ; .body 26 ; .small 22
couleurs         #111111 · #3d3d3d · #444444 · #555555 · #f3f3f3
traits           .rule 2.4 · .thin 1.7 ; arrow marker 9 px ; hatch 14 px à 45°
```

**Série « Masterwork »** — la réalisation concrète de l'archétype D du prompt maître (« tableau analytique horizontal ») : les **lignes étagées**. `fig09_cascade_verite.svg` empile des bandes horizontales de `1780` de large à `x = 310`, chacune ouverte par une cellule grise de `250` px portant un label sur deux lignes (`ÉTAGE 1 / PRODUCTION`), le corps à `x = 600`, et une note italique alignée à droite en `x = 2066`. Kicker : `FIG. 09 · LA CHAÎNE DE LA VÉRITÉ`, contexte à droite en capitales.

**Correction de la première version de ce document** : j'avais écrit que la géométrie de ces bandes était `1780 × 92` et qu'il s'agissait d'un archétype *absent* du prompt maître. Les deux affirmations sont fausses. Relevé exact des cinq bandes de `fig09` : hauteurs **92, 92, 130, 92, 100**, à `y = 330, 518, 666, 852, 1010` — donc **hauteur variable selon le nombre de lignes, gaps irréguliers**, là où la série « IA et travail » tient une grille stricte de panneaux identiques. Et il ne s'agit pas d'un archétype nouveau mais de la réalisation de l'archétype D, dont le prompt donne le principe sans la géométrie. Conséquence pour notre jeu : les six hypothèses devront accepter des bandes de hauteurs différentes (deux à trois lignes de contenu chacune) ; c'est cohérent avec la référence, mais il faut le décider, pas le subir.

Autrement dit : la bibliothèque disponible n'est pas « un style » mais **cinq archétypes**, dont deux nous serviront — le pipeline (A) et le tableau analytique (D). Le découpage en « quatre objets » (panneau, bande, frise, bandeau) est ma synthèse de lecture, pas une donnée du prompt : à traiter comme telle.

**Intégration** — `gen_lecture_html.py` montre la chaîne de relecture : l'article porte des images markdown `![légende](figures/svg/figNN_....svg)`, et le script produit un HTML autonome en base64 avec **paragraphes numérotés** et figures incorporées. Le dossier de revue est donc déjà instrumenté : il suffit d'y brancher un jeu de figures Insee.

---

## 2. Principe éditorial : une figure doit AJOUTER, pas illustrer

La règle du prompt maître est explicite (« aucun texte qui pourrait être retiré sans perte d'information »). Appliquée à ce dossier, elle donne un test plus dur : **une figure ne doit être dessinée que si elle rend visible ce que la prose ne peut pas dire en une phrase.** Trois figures seulement passent ce test sans effort, et c'est le vrai sujet de ce brainstorm : le reste serait de la décoration certifiée conforme.

Corollaire spécifique au dossier Insee, et c'est la partie neuve : **chaque figure a une chose qu'elle doit empêcher de dire.** Un schéma sur les statistiques publiques n'est pas neutre — il produit des implications visuelles (emboîtement, proportion, causalité, intention) que le texte refuse explicitement. Chaque fiche ci-dessous porte donc sa ligne rouge.

---

## 3. Le jeu de figures : 12 fiches

Format du prompt maître respecté pour chacune (KICKER · TITRE · SOUS-TITRE · ARCHÉTYPE · PANNEAUX · SYNTHÈSE · FOOTER).

### FIG. 01 — LA BIOGRAPHIE D'UN CHIFFRE *(article, priorité 1)*

```
KICKER GAUCHE : FIG. 01 · CHAÎNE DE TRANSMISSION
KICKER DROIT  : DOSSIER INSEE
TITRE         : Où le chiffre perd sa marge
SOUS-TITRE    : De la définition internationale au titre de presse, cinq étages,
                et un seul disparaît sans trace.
ARCHÉTYPE     : pipeline 5 panneaux (x=70 → 1890, 400 × 380)
```

- **(a) DÉFINIR** — « Chômeur au sens du BIT » / sans emploi, disponible, en recherche active / 110 000 personnes interrogées par trimestre [13] / *quatre définitions concurrentes existent* [15].
- **(b) MESURER** — « 8,3 % ± 0,3 » / légende du tableau : « +/- 0,3 point près du niveau et de son évolution » [9] / *la marge est produite par le producteur*.
- **(c) PUBLIER** — « Informations rapides n° 192 » / 7 août 2026, **matin** [8] / *la publication suivante est programmée à 07h30, indice de l'heure de parution* [8]. Précision de provenance : l'heure de 07h30 est celle annoncée pour la publication de novembre, non une pièce horodatant l'IR n° 192 elle-même ; la figure ne doit donc pas écrire « 07h30 » dans la case du 7 août.
- **(d) REPRENDRE** — « dépêche 08h00, puis titres » / Le Figaro : « sixième trimestre consécutif, à 8,3% » [11] / *le ministre contrefactuel : 7,9 %* [12].
- **(e) RESTER** — « ce qui circule » / le niveau sans sa marge : 0 mention sur 19 articles lisibles [40] / *la marche d'un trimestre y tient dans la marge* [9].

**SYNTHÈSE BASSE** : « Le chiffre naît avec sa marge. Il la perd avant le petit déjeuner. »
**LIGNE ROUGE** : ne pas dessiner un chiffre qui « s'altère » (aucune flèche de dégradation, aucune échelle de véracité) — les cinq étages ne sont pas cinq degrés de mensonge, ce sont cinq régimes de statut.

### FIG. 02 — UN MOT, QUATRE NOMBRES *(article, priorité 2)*

```
KICKER  : FIG. 02 · LES DÉFINITIONS DU CHÔMAGE
TITRE   : Quatre nombres officiels pour un seul mot
SOUS-TITRE : Les quatre ensembles ne s'emboîtent pas, et aucun n'est faux.
ARCHÉTYPE  : tableau analytique horizontal (4 bandes étagées, x=310, largeur 1780,
             hauteur selon contenu — 92 pour une ligne, 130 pour deux, à la manière de fig09)
```

| Mesure | 2022 | Ce qu'elle compte | Statut |
|---|---|---|---|
| BIT | 2,23 M | sans emploi, disponible, en recherche active | standard international |
| Halo | 1,86 M | souhaite travailler, ne remplit pas tous les critères | ni chômeur ni inactif franc |
| Catégorie A | 3,14 M | inscrits sur les listes (Pôle emploi devenu France Travail) | mesure administrative |
| Recensement | plus élevé, non comparable | auto-déclaration de 14 à 70 ans | réservée aux structures [15] |

Toutes les valeurs : Insee Flash Pays de la Loire n° 140 [14].
**INSET** (petit axe sous le tableau) : 2010-2022, BIT **−2 points** contre catégorie A **+5 %**, écart attribué par le producteur à des réformes intervenant « indépendamment de la situation réelle » [14].
**LIGNE ROUGE, la plus importante du jeu** : **interdiction absolue de dessiner des cercles emboîtés.** Le halo (1,86 M) est *inférieur* au BIT (2,23 M) : un diagramme de Venn ferait dire au dossier le contraire de ce qu'il établit. Les quatre mesures se recoupent partiellement et ne s'emboîtent pas.

### FIG. 03 — LA MARGE AVANT LE MOT *(article, priorité 3)*

```
KICKER  : FIG. 03 · CE QUE LA MARGE ENLÈVE
TITRE   : Une hausse de 0,2 point dans une marge de 0,3
SOUS-TITRE : Ce qui est publié, ce qui circule, et ce que nous nous appliquons à nous-mêmes.
ARCHÉTYPE  : double branche avec convergence
```

- **Branche gauche, publié** : niveau 8,3 % ± 0,3 [9] ; évolution trimestrielle +0,2 ± 0,3 [8][9] ; évolution annuelle +0,7 [8]. L'intervalle dérivé 8,0-8,6 est **notre notation**, pas un chiffre publié : la figure devra l'afficher comme telle, ou ne pas l'afficher — c'est exactement la règle que le dossier applique au « ±17 500 » sans dénominateur, et il serait incohérent de la relâcher ici.
- **Branche droite, circulé** : « sixième trimestre consécutif » [11] ; contrefactuel ministériel 7,9 % [12] ; 0 mention de marge sur 19 articles [40].
- **Convergence** : le niveau est établi, la série de six hausses trimestrielles ne l'est pas.
- **Bandeau hachuré** (le self-report) : « cette règle vaut aussi pour l'ouverture de cet article ».

**LIGNE ROUGE** : hachures sur la seule case « sixième trimestre », et aucune suppression du contrefactuel ministériel — il est *dans* le dispositif de circulation, pas une erreur à corriger.

### FIG. 04 — LA MANIVELLE ET SES QUATRE VANNES *(article, priorité 4)*

```
KICKER  : FIG. 04 · L'INDEXATION, UN TRANSFERT
TITRE   : Un dixième de point vaut cinq cents millions
SOUS-TITRE : Quatre conventions, quatre gagnants, aucun tourneur commun.
ARCHÉTYPE  : pipeline + sorties (archetype E)
```

- **Entrée** : indice des prix → **1 point d'inflation = près de 5 Md€** de dépenses sociales indexées (Trésor, 5 juillet 2022, verbatim) [18] ; **1/10 de la dette indexée ≈ 2,5 Md€ par point** [18] ; base indexée ≈ 500 Md€ de prestations [19].
- **Vanne 1 — IRL** : hors tabac et hors loyers, loi 2005-841 (applicable 2006, hérite de l'indice du coût de la construction) [21] → plafonné 3,5 % de fin 2022 à début 2024 → **1,5 à 2 Md€ par an aux locataires** [22].
- **Vanne 2 — barème de l'IR** : dérive défavorable 8 années sur 13 (2010-2022), −4,1 points cumulés, trop-perçus estimés 2,8 à 6 Md€ ; gel 2026 ≈ 2 Md€ et ≈ 200 000 foyers imposables de plus [23].
- **Vanne 3 — retraites** : bascule salaires → prix en 1987, ≈ **4 Md€ par an** des retraités vers les cotisants [24].
- **Vanne 4 — SMIC** : revalorisé sur l'indice des prix, 12,31 €/h au 1er juin 2026 [20].
- **Bandeau bas obligatoire** : « L'Insee produit l'indice ; la loi, le décret et la loi de finances produisent la convention. »

**LIGNE ROUGE** : aucun sens de flèche unique, aucune main sur la manivelle. Le mot « gagnant » ne doit jamais devenir « intention ».

### FIG. 05 — L'HYPOTHÈSE TUÉE PAR SON ACCUSÉ *(article, priorité 5)*

```
KICKER  : FIG. 05 · H6, MORTE SUR PUBLICATION DE L'INSEE
TITRE   : Nous cherchions l'indice qui la confirmerait
SOUS-TITRE : Nous avons trouvé celui qui la tue, publié par l'institution accusée.
ARCHÉTYPE  : trois plans horizontaux
```

- **Plan 1 — l'hypothèse** : « l'indice sous-estime le coût du logement en excluant les loyers imputés » → sous-estimation de l'inflation.
- **Plan 2 — ce que l'Insee publie** (Focus n° 152, avril 2019) [25] : poids du logement 14,0 % → 25,8 % avec loyers imputés ; sur la période couverte, évolution comparable, et **1,6 % contre 1,8 % en 2018** : avec les loyers, l'indice est *plus bas*.
- **Plan 3 — ce qui survit du grief** : l'indice n'est pas un indice du coût de la vie (verbatim, section des définitions) [25] ; prix des logements anciens **×2,29** entre 2000 et 2018, hors indice car investissement [25] ; manuel européen « trop étroite » [26].
- **Bandeau** : la comparaison de la FIG. 05 est bornée à la période du Focus (arrêt en 2018) : le contrefactuel post-2018 est incalculable en sources ouvertes.

**LIGNE ROUGE** : le mot « tuée » ne doit pas apparaître sans « sur la période que la publication couvre ».

### FIG. 06 — METZING, DEUX POPULATIONS *(article, priorité 6)*

```
KICKER  : FIG. 06 · DÉNOMINATEUR DE L'ARGENT PUBLIC
TITRE   : 791 habitants comptés, 678 habitants publiés
SOUS-TITRE : Un écart supérieur à 15 %, et un rattrapage documenté.
ARCHÉTYPE  : chaîne bornée (5 blocs)
```

1. **Deux nombres** : dénombrement municipal 2024 **791** / population légale Insee **678** → écart > 15 % (réponse ministérielle du 24 juin 2025) [27].
2. **Un dénominateur** : la population légale pilote dotations, seuils, représentation, ~350 articles de loi [29].
3. **Un ordre de grandeur** : 113 habitants ≈ **9 800 €/an** de dotation forfaitaire — **borne**, calculée sur l'élasticité mesurée (86,9 €/hab), plage 7 300-14 600, corroboration régionale [30].
4. **Le rattrapage** : 678 → 699 → 715 en deux ans ; DGF 2026 = 114 005 € [31].
5. **Ce qui manque** : 8 autres communes contestent (Alpes-Maritimes) ; **aucune série nationale** dénombrements/populations légales [32].

**LIGNE ROUGE** : aucun mot « perte », aucune flèche de prélèvement. La case « borne » doit porter sa mention d'incertitude, et la case 4 doit figurer à la même taille que les autres — c'est une partie du résultat.

### FIG. 07 — LE BROUILLON ET SA CORRECTION *(article, priorité 7)*

```
KICKER  : FIG. 07 · RÉVISIONS DES COMPTES 2023
TITRE   : 0,9 au printemps, 1,9 deux ans plus tard
SOUS-TITRE : La plus forte révision depuis 2003, pour une année dont tout avait été conclu.
ARCHÉTYPE  : continuum + bandeau
```

- **Frise** : comptes 2023, printemps 2024 → **0,9 %** (+1,1 % en jours ouvrables) ; comptes 2024, mai 2025 → **1,4 %** ; compte définitif, mai 2026 → **1,6 %** et **1,9 %** corrigé des jours ouvrables [33].
- **Deux régimes d'erreur, à ne pas confondre** : révisions de croissance → biais **+0,34 point** orienté à la hausse sur 20 ans [34] ; surprises de recettes → deux sens, 2025 : 5,4 % prévu / 5,1 % réalisé, 161 → 152,5 Md€ de déficit, 30,7 Md€ de recettes dont 13,0 d'évolution spontanée [35] ; 2023-2024 : recettes déçues, 2,6 % contre 6,3 % de PIB nominal [36].
- **Bandeau** : l'erratum du 29 mai 2026 est publié le jour même ; ses lecteurs sont les spécialistes déjà sur place [33].

**LIGNE ROUGE** : ne pas fusionner les deux régimes dans un seul graphe, et ne pas dessiner une « tendance de la prévision » : ce sont deux mécanismes distincts.

### FIG. 08 — LES SIX HYPOTHÈSES ET LEUR SORT *(article ou double page, priorité 8 — la figure la plus forte du dossier)*

```
KICKER  : FIG. 08 · CONTRE-ÉPREUVE
TITRE   : Six accusations, un seul survivant de forme faible
SOUS-TITRE : Ce que nous espérions, ce que nous avons trouvé, ce qu'il en reste.
ARCHÉTYPE  : lignes étagées (6 bandes de 1780 de large, hauteurs variables selon le contenu,
             cellule grise de 250 px à gauche, note de provenance alignée à droite)
```

| # | Hypothèse | Espéré | Constat | Verdict |
|---|---|---|---|---|
| H1 | mensonge de l'institut | scandale | méthodologies complètes, erratum, indices alternatifs, résistance à une pression de 2021 [37] | morte, **absence de contre-preuve et non preuve d'intégrité** |
| H2 | bénéficiaire unique | siphon | signes contraires selon convention et année [22][23][24] | morte ; survit en version faible |
| H3 | opacité dissimulatrice | documents cachés | opacité d'expertise : intervalle absent de 19 articles [40], rapports Eurostat « pas toujours publiés » [37], labellisation suspendue du 01/01/2025 au 20/05/2026 [39] | reformulée |
| H4 | PIB révisé pour maquiller le déficit | maquillage | PIB 2025 non révisé, recettes décomposées par la Cour [35] | réfutée |
| H5 | reclassifications dissimulant la dette | sorties d'entités | cessions de titres, Française des Jeux restée dans le périmètre, aucune sortie documentée 2010-2025 [38] | close ; grief déplacé (aucun raccord public de série, > 100 Md€ de marches) |
| H6 | loyers imputés cachant l'inflation | sous-estimation | Focus 152 : 1,6 % contre 1,8 % [25] | tuée par l'accusé |

**SYNTHÈSE BASSE** : « La meilleure infrastructure disponible pour ces objets, et une transmission qui la trahit. »
**LIGNE ROUGE** : hachures réservées aux deux hypothèses tuées ; interdiction d'ajouter une colonne « preuve d'intention ».

### FIG. 09 — LES QUATRE GESTES *(article, clôture)*

```
KICKER  : FIG. 09 · GRILLE DE LECTURE
TITRE   : Quatre questions avant de citer un chiffre
SOUS-TITRE : Applicables à n'importe quel chiffre officiel, en dix secondes.
ARCHÉTYPE  : quatre colonnes panneau (400 × 380) ou quatre bandes étagées
```

| Geste | La question | Ce qu'elle élimine | Payload du dossier |
|---|---|---|---|
| 1. Définition | BIT, catégorie A, recensement ? | la moitié des polémiques | 2,23 / 1,86 / 3,14 M [14] |
| 2. Marge | quel intervalle ? | les mouvements de 0,1 point | 8,3 ± 0,3 [9] ; ±17 500 sans dénominateur [41] |
| 3. Seuil et périmètre | 40, 50, 60 ou 70 % ? quel périmètre ? | les faux désaccords | 2,8 / 5,6 / 9,8 / 14,6 M [16] ; 610 contre 356,4 Md€ [42] |
| 4. Historique | que sont devenues les versions précédentes ? | les récits sur un brouillon | 0,9 → 1,9 [33] ; refonte −0,3 pt [17] |

**LIGNE ROUGE** : la case 3 doit afficher les deux montants **côte à côte à même taille**, jamais l'un au-dessus de l'autre avec un écart — c'est précisément la figure que produirait un mauvais esprit.

### FIG. 10 — FRISE DES CONVENTIONS, 1987-2026 *(annexe)*

`KICKER : FIG. 10 · SÉDIMENTATION DES CONVENTIONS` — archétype frise (modèle `fig12_frise_accumulation.svg`) : 1987 retraites basculées sur les prix [24] · 2005 IRL créé, applicable 2006, en remplacement de l'indice du coût de la construction [21] · 2022-2024 plafond IRL 3,5 % [22] · 2026 gel du barème [23] et SMIC à 12,31 € au 1er juin [20].
**Ce que la frise établit** : cinq décisions discrètes, aucune direction commune. C'est l'anti-figure du complot, et c'est pour cela qu'elle doit exister.

### FIG. 11 — LES QUATRE CLÉS DE RÉVOCATION *(annexe)*

`KICKER : FIG. 11 · CONDITIONS DE RÉVOCATION` — quatre bandes : réservation publiée d'Eurostat sur les comptes ; échec de réplication du BIT par un chercheur indépendant accédant aux microdonnées ; résidu > 0,3 % du PIB non tracé dans l'identité de la dette ; asymétrie démontrée dans l'historique des révisions [44].
**Usage** : c'est la figure qui protège l'article de l'accusation d'allégeance — elle rend le verdict falsifiable.

### FIG. 12 — LE CAFÉ ET LE PANIER (rejetée, et pourquoi)

La tentation est forte : deux colonnes, 1999 et 2026, 10,40 F contre 2,7 à 2,9 €, écart de 10 à 18 % par rapport à l'indice. Je la rejette en figure et je la garde en **encadré typographique** (pas de dessin), pour trois raisons vérifiables : le prix du croissant 1999 est une **borne non mesurée** ; l'écart est **notre recalcul**, sensible à cette borne ; et une figure à deux colonnes imposerait une proportion visuelle alors que le chiffre est une fourchette. Le prompt maître l'interdit en propres termes (« ne pas faire varier la taille des panneaux pour suggérer une proportion non mesurée »).

---

## 4. Priorisation

**Six figures dans l'article** : 01 (chaîne), 02 (quatre nombres), 04 (manivelle), 05 (H6), 06 (Metzing), 08 (six hypothèses) — plus la 09 (grille) si la maquette le supporte, soit 7 au maximum, exactement la densité de la série « IA et travail » (7 figures).
**Trois en annexe** : 03 (marge), 07 (révisions), 10 (frise des conventions), 11 (clés de révocation).
**Rejetée** : 12 (café), remplacée par un encadré.

Justification du classement : les figures 01, 02, 04, 05, 06, 08 portent chacune une **démonstration que la prose ne peut pas produire** — respectivement l'absence de la marge dans la circulation, la non-emboîtement des définitions, l'attribution des conventions, le retournement de H6, la borne de Metzing, et la table des verdicts. Les autres illustrent.

---

## 5. Chaîne de production

- **Un générateur, pas douze fichiers à la main** : `tools/engines/visual/gen_figures_insee.py`, SVG natif déterministe, bibliothèque de composants (`panel()`, `band()`, `frise()`, `synthesis()`, `header()`, `footer()`), constantes du design system en tête de fichier.
- **Nommage** : `articles/2026-09-23_insee_V5/figures/svg/figNN_theme_court.svg`, kicker interne `FIG. NN · THÈME`, contexte droit `DOSSIER INSEE`.
- **Insertion** : images markdown dans l'article aux points d'ancrage prévus (fin de la section correspondante), légende d'une ligne + renvois de notes entre crochets — le mécanisme existe déjà dans `gen_lecture_html.py`.
- **Page de relecture** : dupliquer `gen_lecture_html.py` pour produire `LECTURE_INSEE_V5.html`, figures en base64, paragraphes numérotés, appareil en fin de fichier déclaré « à ne pas lire ».
- **Contrôle automatique** : un script de vérification qui relit chaque SVG et compare chaque nombre à la liste blanche des valeurs de l'article (`/tmp` de l'audit), afin qu'aucune figure ne puisse introduire un chiffre absent du texte. Le prompt maître interdit d'inventer un chiffre ; ici, l'interdiction est mécanisable.

---

## 6. Tests de conformité

Les douze conditions du prompt maître s'appliquent telles quelles. Quatre tests propres à ce dossier s'y ajoutent :

1. **Test du faux emboîtement** : aucune figure ne doit suggérer que les définitions du chômage, les seuils de pauvreté ou les périmètres budgétaires s'emboîtent ou se comparent à même échelle.
2. **Test de l'intention** : aucune flèche ne doit relier une décision publique à un bénéficiaire, ni une convention à un tourneur.
3. **Test de la borne** : tout chiffre marqué « borne » ou « recalcul » dans les notes doit porter la même mention dans la figure.
4. **Test de la réversibilité** : les figures 08 et 11 doivent conserver les verdicts défavorables à notre thèse (H3 reformulée, H5 close avec grief déplacé, conditions de révocation) — une figure qui ne retiendrait que les victoires serait un document de propagande conforme au design system.

---

## 7. Ce que ce brainstorm ne prétend pas être

Aucune figure n'est encore dessinée : ce document est un cahier des charges. Les chiffres cités proviennent tous de l'article V5 et de ses notes, dont l'appareil a été audité le 23 septembre 2026 ; les quatre valeurs qui ne sont pas des mesures directes (le 9 800 €/an, le 10-18 %, l'écart de 4,1 points du barème, les 2,8 à 6 Md€ de trop-perçus) sont des **bornes ou des fourchettes** et doivent porter leur statut dans la figure comme dans le texte. Enfin, un doute éditorial subsiste et je le laisse ouvert : sept figures pour 8 600 mots, c'est la densité de la série de référence, mais l'article Insee est plus dense en texte que ces articles-là — la maquette dira s'il faut en retirer une ou deux.

---

## 8. Provenance des valeurs qui entreront dans les figures

La règle du prompt maître (« n'inventer aucun chiffre ») exige plus qu'une intention : elle exige une traçabilité par valeur. Quatre régimes, à ne pas confondre :

| Figure | Valeurs | Régime de provenance |
|---|---|---|
| **01** | 8,3 % ; ±0,3 (légende du tableau) | **T1 lu en direct** le 23/09/2026 (IR n° 192, légende capturée) |
| | 110 000 répondants | T1, registre de run (non re-fetché par mes soins) |
| | dépêche horodatée 08h00 | **T2 lu en direct** (fil Mediapart) |
| | titres du 7 août | **T4 vérifié par URL** (Le Figaro) |
| | 0 mention sur 19 articles | audit interne du dépôt, biais affichés |
| **02** | 2,23 / 1,86 / 3,14 M ; −2 pts contre +5 % | **T1 lu en direct** (Insee Flash n° 140) |
| | définition au recensement | T1, registre |
| **03** | ±0,3 ; +0,2 ; +0,7 ; contrefactuel 7,9 % | T1 + **T2 lu en direct** (franceinfo 20h00) |
| | intervalle 8,0-8,6 | **calcul nôtre**, à étiqueter ou à retirer |
| **04** | 5 Md€ par point ; 2,5 Md€ par point (dette indexée) | **T1 lu en direct** (Trésor-Info, 5 juillet 2022) |
| | base indexée ≈ 500 Md€ | T2, registre (FIPECO) |
| | IRL : loi 2005-841, applicable 2006 | **T3 juridique recoupé** le 23/09/2026 sur sources concordantes |
| | plafond 3,5 % ; 1,5-2 Md€/an ; barème 8/13 ans ; gel 2 Md€ / 200 000 foyers ; retraites 4 Md€/an ; SMIC 12,31 € | T1/T2 de registre, **non re-fetchés** ; les 2,8-6 Md€ de trop-perçus sont une **fourchette d'acteurs non officiels** |
| **05** | 14,0 → 25,8 % ; 1,6 contre 1,8 en 2018 ; ×2,29 ; le verbatim « n'est pas un indice du coût de la vie » | **T1 lu en direct** (Insee Focus n° 152) |
| | manuel européen « trop étroite » | T2, registre |
| **06** | 791 / 678 / écart > 15 % | T2, réponse ministérielle, registre |
| | 678 → 699 → 715 ; 114 005 € | T1, séries OFGL et Banatic, registre |
| | 9 800 €/an | **calcul nôtre**, borne (plage 7 300-14 600) |
| | absence de série nationale | **absence documentée**, à dire comme telle |
| **07** | 0,9 → 1,4 → 1,6 / 1,9 | **T1 lu en direct** sur trois publications Insee |
| | biais +0,34 point | T3, Rexecode, registre |
| | 5,4 → 5,1 ; 161 → 152,5 Md€ ; 30,7 dont 13,0 | T1 (note de révisions) et T2 (Cour des comptes), registre |
| | 2,6 % contre 6,3 % | T2, Trésor-Éco, registre |
| **08, 09, 10, 11** | verdicts, gestes, jalons, conditions | **interne** au protocole du dépôt, sauf SMIC et IRL vérifiés ci-dessus |

Aucune figure ne peut afficher une valeur d'un régime supérieur à celui de sa pièce. Les valeurs de registre sont traçables mais non re-vérifiées par moi le 23 septembre : les quatre figures les plus exposées (01, 02, 04, 05) reposent majoritairement sur des pièces lues en direct, ce qui n'est pas un hasard mais n'est pas non plus une garantie pour les autres.

---

## 9. Double check du brainstorm (23 septembre 2026)

Ce document a été vérifié contre les fichiers, et il contenait trois erreurs, dont une affirmée sans réserve :

1. **Géométrie des bandes fausse et archétype mal attribué** (corrigé en §1, puis propagé aux fiches FIG. 02 et FIG. 08 qui portaient encore la valeur erronée — la correction avait d'abord été appliquée à un seul endroit, défaut identique à celui relevé plus tôt dans l'appareil de l'article). J'écrivais `1780 × 92` pour toutes les bandes de `fig09_cascade_verite.svg` et j'appelais ce gabarit « absent du prompt maître ». Relevé réel : hauteurs 92, 92, 130, 92, 100, gaps irréguliers ; et il s'agit de la réalisation de l'archétype D du prompt, pas d'une famille nouvelle.
2. **Heure de publication surinférée** (corrigé en §3, FIG. 01). Le `07h30` documenté par la note [8] est l'heure annoncée de la publication *suivante*, pas une pièce horodatant l'IR n° 192. La case « PUBLIER » ne devra pas porter cette heure.
3. **Intervalle dérivé non étiqueté** (corrigé en §3, FIG. 03). `8,0-8,6` est notre arithmétique à partir de 8,3 ± 0,3, pas un chiffre publié : exactement ce que le dossier refuse au « ±17 500 » sans dénominateur.

Une quatrième correction, de cohérence : la figure rejetée du café citait « 2,80 € » là où la valeur est une fourchette de 2,7 à 2,9 €.

Contrôles passés en revanche : la géométrie des panneaux de la série « IA et travail » est exacte (cinq panneaux `400 × 380` à `x = 70 / 525 / 980 / 1435 / 1890`, `y = 390`) ; les deux corpus de référence existent bien (4 SVG et 10 SVG) ; `gen_lecture_html.py` fait ce que j'en dis (images markdown, base64, paragraphes numérotés) ; et **tout nombre du présent document, sauf l'intervalle dérivé mentionné ci-dessus, existe à l'identique dans l'article V5** — le contrôle automatique des listes numériques n'a pas trouvé d'autre écart que les chiffres de la grammaire graphique et les numéros de figure.

Non vérifié, et à dire : `tools/engines/visual/chatgpt.md` évoque un corpus de « 35 SVG » analysés ; je n'en ai localisé et lu que quatorze dans ce dépôt. La grammaire que j'ai relevée vient de ces quatorze, pas de trente-cinq : elle est exacte pour ce que j'ai lu, elle n'est pas exhaustive.

---

## 10. Génération et intégration : exécution du plan

### Ce qui existe maintenant

| Élément | Chemin | Rôle |
|---|---|---|
| Générateur | `tools/engines/visual/gen_figures_insee.py` | 11 figures SVG natives, 2400 × 1500, déterminisme total |
| Contrôle | `tools/engines/visual/check_figures_insee.py` | chiffres, formulations, grammaire, intégration |
| Page de relecture | `tools/engines/visual/gen_lecture_figures.py` → `articles/2026-09-23_insee_V5/LECTURE_FIGURES.html` | les 11 figures inlinées en base64, une par écran |
| Figures | `articles/2026-09-23_insee_V5/figures/svg/*.svg` | 11 fichiers, 200 Ko au total avec la page |

**Intégration** : sept figures dans le corps (01, 02, 04, 05, 06, 08, 09), quatre dans un **appendice C** créé pour elles (03, 07, 10, 11), chaque insertion portant une légende d'une ligne. L'article passe à 8 950 mots, conserve ses 44 notes, ses 44 renvois et zéro tiret cadratin.

### Ce que le rendu a corrigé, et que le XML ne voyait pas

Le premier contrôle mécanique était vert alors que les figures étaient illisibles. Trois défauts n'ont été trouvés qu'en **regardant la page** :

1. **Débordement vertical des bandes étagées** (FIG. 02, FIG. 08) : ma première version empilait les lignes avec un décalage fixe, si bien que la dernière ligne de « trouvé » franchissait le bord inférieur du cadre. Correction : empilement homogène où chaque ligne consomme sa propre hauteur, hauteur de bande recalculée à partir du contenu.
2. **Libellés de cellule grise débordant de leur colonne** (FIG. 08, « BÉNÉFICIAIRE UNIQUE ») : mon estimation de largeur ignorait l'interlettrage des libellés. Correction : facteur conservateur et tracking compté, colonne élargie à 300 px.
3. **Régression de formulation** (FIG. 01) : la figure réaffichait « Tout est publié », l'universel que l'audit avait corrigé en « Presque tout est publié ». Le contrôle ne comparait que les chiffres ; il compare désormais aussi les formulations bannies.

Un quatrième défaut, purement de code, avait été attrapé par le contrôle XML : `parts += rect(...)` étendait une chaîne caractère par caractère au lieu d'ajouter un élément, ce qui produisait un SVG invalide dans les figures 02 et 03.

### Le contrôle, tel qu'il tourne

- **Chiffres** : tout nombre affiché dans une figure doit exister à l'identique dans l'article, hors renvois de note. Passé : aucun chiffre inventé — c'est la mécanisation de la règle « n'inventer aucun chiffre » du prompt maître.
- **Formulations** : sept tours bannis par l'audit sont désormais détectés (`tout est publié`, `trois semaines`, `six malentendus`, `18 heures`, `AFP`, `Metzing a perdu`, `systématiquement trahie`). Test négatif effectué : en réintroduisant volontairement « Tout est publié » dans la FIG. 01, le contrôle échoue et le dit ; après restauration, il repasse.
- **Grammaire** : canevas 2400 × 1500, palette fermée, aucun arrondi, aucun filtre, aucun dégradé.
- **Intégration** : chaque figure référencée dans l'article existe sur disque, et réciproquement.

### Ce qui reste à faire, et qui n'est pas cosmétique

- La **quatrième correction de mise en page** attend encore : la FIG. 06 et la FIG. 09 n'ont pas été relues à l'œil après correction du moteur, seule une partie du jeu l'a été.
- Les **figures ne sont pas encore insérées dans une maquette de publication** : Substack accepte les SVG en import mais le rendu des polices Latin Modern dépend de la plateforme, et une conversion en PNG haute résolution devra être décidée avant mise en ligne.
- Les **onze chiffres de registre** signalés en §8 gardent leur tier : aucune figure ne les élève.
