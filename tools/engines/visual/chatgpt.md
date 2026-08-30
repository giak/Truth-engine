Oui. Le problème est maintenant identifié précisément : **ce n’est pas le contenu de la figure qui cloche, c’est que je n’ai pas reproduit la grammaire graphique réelle des SVG de référence**.

J’ai analysé leur code SVG, pas seulement leur apparence. Ils sont beaucoup plus systématiques que ce que j’avais reproduit.

### Ce que les SVG de référence font réellement

Ils utilisent tous un canevas **2400 × 1500**, avec une grille presque éditoriale :

* marge gauche/droite : **90 px**
* cartouche supérieur à `y = 78`
* premier filet horizontal à `y = 112`
* titre centré autour de `y = 214`
* sous-titre autour de `y = 278`
* zone analytique principale entre environ `y = 360` et `1100`
* synthèse/conclusion entre `1100` et `1350`
* filet final à `y = 1410`
* sources / qualification en bas à `y = 1460`

Ce n’est pas du tout une simple succession de rectangles.

## La typographie est le cœur du rendu

Les références déclarent explicitement :

```text
Latin Modern Roman
Latin Modern Sans
```

C’est précisément ce qui donne cette impression **LaTeX / publication scientifique**.

La hiérarchie est elle aussi rigoureuse :

```text
Kicker        Latin Modern Sans   27 px   bold
              tracking 2.6 px

Titre         Latin Modern Roman  60 px   medium

Sous-titre    Latin Modern Roman  29 px   gris

Intertitre    Latin Modern Roman  34–42 px

Corps         Latin Modern Sans   26–29 px

Notes         Latin Modern Roman  22–27 px italic
```

Mes essais avaient essentiellement une typographie générique de diagramme.

C’est une différence énorme.

---

# Ce qui donne la qualité des références

## 1. Aucun coin arrondi

Les références ont des rectangles **secs**.

Pas de cartes d’application web.

Pas de pill shapes.

Pas de shadow.

Pas de « UI ».

C’est une **planche éditoriale**.

---

## 2. Très peu de niveaux de gris

En réalité, la palette est presque seulement :

```text
#111111    texte / traits
#444444    notes secondaires
#555555    traits fins
#FFFFFF    fond
#F3F3F3    panneau secondaire
```

Et parfois des **hachures**.

Mais les hachures ont un sens : anomalie, étape critique, catégorie spéciale, changement de statut.

Elles ne sont jamais décoratives.

---

## 3. Une vraie hiérarchie des traits

Les références distinguent :

```text
1.3–1.7 px   filet secondaire
2.4 px       cadre normal / règle
3 px         flèche structurante
3.6–5 px     élément critique
```

Mes figures utilisaient pratiquement le même poids partout.

Résultat : aucune hiérarchie.

---

# 4. Les flèches ne traversent pratiquement jamais les objets

C’est une différence fondamentale.

Dans les SVG de référence, les flèches sont :

* courtes ;
* horizontales ou verticales ;
* centrées exactement sur les objets ;
* placées **dans le vide entre les panneaux** ;
* presque jamais diagonales.

Exemple réel :

```text
panel 1       panel 2
│             │
└─── → ───────┘
```

et non :

```text
        ╲
         ↘
          box
```

C’est pourquoi les références donnent une impression de rigueur mathématique.

---

# 5. Les panneaux ne sont pas des « boîtes de texte »

Ils ont une architecture interne.

Typiquement :

```text
┌──────────────────────────┐
│ (a)   EN AMONT           │
│ ───────────────────────  │
│                          │
│ Sélection                │  ← Roman, grand
│                          │
│ • affirmation exacte     │  ← Sans
│ • critère de sélection   │
│ • provenance initiale    │
│                          │
│ - - - - - - - - - - -  │
│ Pourquoi cet énoncé      │  ← Roman italic
│ entre-t-il dans le radar?│
└──────────────────────────┘
```

C’est extrêmement différent de :

```text
┌─────────────┐
│ TITRE       │
│ texte texte │
│ texte texte │
└─────────────┘
```

---

# 6. Le vide est une composante graphique

C’est probablement ce que j’avais le plus raté.

Les références n’essaient pas de remplir les 2400 × 1500.

Elles laissent :

* 80 px ;
* 100 px ;
* parfois 150 px

entre les groupes.

Cette respiration produit l’élégance.

---

# 7. Elles utilisent quelques archétypes, pas un layout différent à chaque fois

L’analyse des 35 SVG montre en réalité **quelques familles répétées**.

### Archétype A : chaîne de 5 étapes

Comme :

> *Du modèle au slogan : où change le statut ?*

Cinq panneaux identiques :

```text
[A] → [B] → [C] → [D] → [E]
```

puis un grand bandeau de conclusion.

### Archétype B : trois grands panneaux

```text
┌────────┐    ┌────────┐    ┌────────┐
│   a    │ →  │   b    │ →  │   c    │
└────────┘    └────────┘    └────────┘
```

### Archétype C : axe / continuum

Une grande ligne horizontale avec points, puis trois blocs analytiques en dessous.

### Archétype D : tableau analytique horizontal

Trois lignes ou trois régimes comparés.

### Archétype E : chaîne + décisions finales

Cinq panneaux en haut, trois sorties en bas :

```text
                  ┌─ MAINTENIR
pipeline ─────────┼─ RESSERRER
                  └─ RETIRER
```

C’est presque une **bibliothèque de composants LaTeX/TikZ**.

---

# Et surtout : notre première figure appelle précisément l’archétype A

J’ai essayé de lui inventer un design.

Erreur.

Elle correspond naturellement au template existant **« Du modèle au slogan »**.

Je la construirais exactement ainsi :

```text
FIG. 01 · CHAÎNE DE CONVERSION                    IA ET TRAVAIL
────────────────────────────────────────────────────────────────


          Du benchmark au gain réellement disponible

    Entre la performance technique et la capacité utile,
            plusieurs coûts changent le statut du gain.


┌────────────┐ → ┌────────────┐ → ┌────────────┐ → ┌────────────┐ → ┌────────────┐
│ CAPACITÉ   │   │ GAIN BRUT  │   │ FROTTEMENTS│   │ GAIN NET   │   │ CAPACITÉ   │
│ TECHNIQUE  │   │            │   │            │   │            │   │ DISPONIBLE │
│────────────│   │────────────│   │────────────│   │────────────│   │────────────│
│            │   │            │   │            │   │            │   │            │
│ benchmark  │   │ temps      │   │ contrôle   │   │ temps      │   │ capacité   │
│ précision  │   │ économisé  │   │ correction │   │ utile      │   │ mobilisable│
│ robustesse │   │ avant      │   │ exceptions │   │ après      │   │ dans       │
│            │   │ frictions  │   │ intégration│   │ frictions  │   │ l’activité │
│            │   │            │   │            │   │            │   │            │
│ conditions │   │ contexte   │   │ souvent    │   │ mesure     │   │ pas encore │
│ du test    │   │ observé    │   │ hors bench │   │ économique │   │ distribuée │
└────────────┘   └────────────┘   └────────────┘   └────────────┘   └────────────┘
```

Mais avec **exactement la géométrie des références** :

```text
x = 70
x = 525
x = 980
x = 1435
x = 1890

largeur = 400
hauteur = 380

gap = 55 px
```

Ce ne sont pas des dimensions inventées : ce sont celles du SVG de référence.

---

# Et je changerais aussi le contenu

Notre première figure actuelle essaie encore trop d’expliquer.

La référence est meilleure parce que chaque panneau contient seulement :

* un concept ;
* deux ou trois éléments ;
* une note épistémique.

Je propose donc :

### (a) CAPACITÉ TECHNIQUE

**Benchmark**

précision
robustesse
couverture

*ce que le modèle peut faire*

### (b) GAIN BRUT

**Temps économisé**

avant contrôle
dans le cas observé

*pas encore un gain économique*

### (c) FROTTEMENTS

**Coûts résiduels**

contrôle
corrections
intégration
exceptions

*souvent hors benchmark*

### (d) GAIN NET

**Temps utile**

après contrôle
à qualité comparable

*ce que l’organisation gagne*

### (e) CAPACITÉ DISPONIBLE

**Usage du gain**

volume
délai
qualité
redéploiement

*pas encore sa distribution*

Là, on a une figure analytique.

---

# Puis un bandeau inférieur comme les références

Pas trois slogans flottants.

Un vrai bloc gris :

```text
│
│  Un gain technique n’est pas encore un gain économique.
│
│  Et un gain économique n’indique pas encore qui reçoit la valeur.
│
```

Puis une règle.

Puis une phrase finale importante :

> **Le benchmark mesure une capacité. L’économie commence après.**

Ça ressemble déjà beaucoup plus à la logique graphique et intellectuelle de tes SVG.

---

# Même le header doit changer

Pas :

> FIGURE V3.3-01

mais exactement dans le système des références :

**FIG. 01 · CHAÎNE DE CONVERSION**

à gauche.

Et :

**IA ET TRAVAIL**

à droite.

C’est ce genre de détail qui fait immédiatement passer de « diagramme » à « planche d’article ».

---

# Ce que je dois donc reproduire, et pas seulement imiter

Je fixerais un **design system immuable** :

```text
CANVAS      2400 × 1500

MARGE X       90
HEADER Y       78
RULE Y        112
TITLE Y       214
SUBTITLE Y    278
BODY TOP      390
BOTTOM RULE  1410
FOOTER Y     1460

SERIF       Latin Modern Roman
SANS        Latin Modern Sans

BLACK       #111111
GRAY TEXT   #444444
LIGHT FILL  #F3F3F3

RULE        2.4 px
THIN        1.7 px
ARROW       3 px
CRITICAL    5 px
```

Et ensuite **aucune figure n’a le droit de sortir de cette grammaire**.

---

# Une autre différence importante : il ne faut pas que les 7 figures soient identiques

Même design system.

Mais archétypes différents selon l’idée.

Je mapperais :

| Figure                   | Archétype référence                        |
| ------------------------ | ------------------------------------------ |
| 01 Gain net              | **Pipeline 5 panneaux**                    |
| 02 Déplacement du goulot | **Axe / continuum analytique**             |
| 03 Emploi contrefactuel  | **3 plans / comparaison horizontale**      |
| 04 Demande / prix        | **Pipeline + bifurcation**                 |
| 05 Exposition réseau     | **3 niveaux / circulation transverse**     |
| 06 Expérience junior     | **Axe double + convergence**               |
| 07 Incidence             | **circulation transverse + bandeau final** |

Même famille graphique, mais aucune monotonie.

---

## Ce que je considère maintenant comme le standard

Pour qu’une figure passe :

1. **aucun rounded rectangle** ;
2. **aucune flèche diagonale sauf nécessité absolue** ;
3. alignement sur une grille numérique ;
4. pas plus de 3 niveaux typographiques dans le corps ;
5. Latin Modern Roman/Sans ;
6. une phrase analytique forte dans la zone basse ;
7. un footer de provenance réel ;
8. 2400 × 1500 ;
9. un seul gris ;
10. aucun chiffre non vérifié ;
11. aucune décoration ;
12. aucun texte qui pourrait être retiré sans perte d’information.

C’est cela qu’il fallait comprendre par **« même style et même rigueur »**.

Le prochain prototype ne doit donc plus être « inspiré » des références. Il doit être **construit sur leur grille et leur système typographique**, en SVG natif déterministe.


---

# PROMPT MAÎTRE - SÉRIE DE FIGURES QUASI-LATEX

## Référence

Reproduire le design system des figures analytiques validées de la série **IA et travail**. Le rendu doit appartenir visuellement à la même famille que les SVG de référence fournis, pas seulement être noir et blanc.

## Design system immuable

- Canevas SVG : **2400 x 1500**.
- Fond : `#ffffff`.
- Marge latérale principale : **90 px**.
- Header : kicker gauche `x=90 y=78`, kicker droit `x=2310 y=78`, filet horizontal `y=112`.
- Titre centré : autour de `y=214`, taille **60 px**, serif TeX.
- Sous-titre : autour de `y=278`, taille **29 px**, serif TeX gris foncé.
- Footer : filet à `y=1410`, note gauche et contexte droit à `y=1460`.
- Typographie serif : **TeX Gyre Termes / Latin Modern Roman**.
- Typographie sans : **TeX Gyre Heros / Latin Modern Sans**.
- Kicker : sans bold 27 px, tracking 2.6 px.
- Titre de panneau : sans bold 27 px, capitales.
- Titre analytique interne : serif 34-42 px.
- Corps : sans 26-29 px.
- Note épistémique : serif italique 27 px.
- Noir principal : `#111111`.
- Gris texte : `#3d3d3d` à `#555555`.
- Gris de panneau : `#f3f3f3`.
- Cadre normal : 2.4 px.
- Cadre accentué : 3.6 à 5 px.
- Trait fin : 1.7 px.
- Flèche structurante : 3 px.
- Angles droits uniquement.
- Aucun arrondi, aucune ombre, aucun dégradé, aucune couleur décorative.

## Grammaire de composition

1. Header éditorial fin et stable.
2. Titre et sous-titre centrés avec beaucoup d'espace blanc.
3. Corps analytique construit avec l'un des archétypes suivants :
   - trois grands panneaux horizontaux ;
   - cinq panneaux séquentiels 400 px de large ;
   - continuum horizontal avec cinq points ;
   - deux branches symétriques avec convergence ;
   - pipeline de cinq étapes suivi de trois sorties.
4. Flèches courtes, rectilignes, centrées dans les intervalles.
5. Pas de flèche diagonale si une ligne orthogonale est possible.
6. Les panneaux d'un même niveau ont exactement la même hauteur.
7. Un panneau critique peut être gris clair, à bord plus épais ou hachuré, mais jamais coloré.
8. Utiliser les hachures uniquement pour signaler un changement de statut, une anomalie ou un élément soumis à un test critique.
9. Terminer par une synthèse forte : bloc gris clair, circulation transverse ou conclusion serif de 48-50 px.
10. Footer avec qualification méthodologique, jamais décoratif.

## Discipline épistémique

- N'inventer aucun chiffre.
- N'inventer aucune source.
- Ne pas faire varier la taille des panneaux pour suggérer une proportion non mesurée.
- Corrélation n'implique pas causalité.
- Une hypothèse doit être identifiée comme telle.
- Une figure conceptuelle reste conceptuelle.
- Aucun pictogramme, aucun avatar, aucune métaphore visuelle décorative.

## Prompt de contenu

Après ce bloc maître, ajouter :

```text
FIGURE : [numéro]
KICKER GAUCHE : [ex. FIG. 03 · OBSERVABILITÉ DE L'EMPLOI]
KICKER DROIT : [ex. DOSSIER D'ANALYSE]
TITRE : [...]
SOUS-TITRE : [...]
ARCHÉTYPE : [3 panneaux / 5 panneaux / continuum / double branche / pipeline+sorties]

PANNEAU (a)
Titre : [...]
Corps : [...]
Note épistémique : [...]

PANNEAU (b)
...

SYNTHÈSE BASSE : [...]
FOOTER GAUCHE : [...]
FOOTER DROIT : [...]
```

## Test de conformité

Rejeter et refaire la figure si l'une de ces conditions est vraie :

- elle ressemble à PowerPoint, Canva, une UI ou une infographie marketing ;
- elle emploie des coins arrondis ;
- la police ne ressemble pas à une composition TeX ;
- les flèches traversent les panneaux ou le texte ;
- les marges sont irrégulières ;
- les panneaux d'un même rang ne sont pas alignés ;
- le texte est trop dense ;
- une donnée non fournie a été inventée ;
- les notes basses ne sont pas visuellement secondaires ;
- la figure ne semble pas appartenir immédiatement à la même série éditoriale.

## Règle finale

Le but n'est pas de produire une jolie infographie. Le but est de produire une **figure d'article analytique, froide, quasi-LaTeX, reproductible et éditorialement cohérente**.
