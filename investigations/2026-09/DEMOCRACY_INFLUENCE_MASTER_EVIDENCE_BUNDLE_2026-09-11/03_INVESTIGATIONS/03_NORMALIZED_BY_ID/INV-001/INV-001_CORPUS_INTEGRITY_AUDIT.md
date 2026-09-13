# INV-001 — Audit d’intégrité du corpus Substack

**Date d’audit :** 2026-09-05  
**Objet :** intégrité structurelle et réconciliation du snapshot fourni `substack-online(5).zip`  
**SHA-256 archive :** `84f3174f473bbfab6ee55aa516de613b30f35822d8779e6a71afc830bdb5d1b5`  
**Snapshot interne :** fichiers horodatés 2026-08-26 ; `index.md` indique une mise à jour au 2026-08-26.  
**Hors scope :** validité factuelle des 124 articles. INV-001 vérifie l’inventaire, les identités, les versions et la cohérence des représentations du corpus.

## Verdict

**FAIL / corpus non canonique pour INV-002 en l’état.**

Le snapshot est exploitable comme matériau, mais **pas comme inventaire exhaustif et univoque des articles publiés**. `index.md`, `posts.csv` et `posts/*.html` divergent sur les objets présents, leur statut et, ponctuellement, leur date. Une réparation locale/reconstruction de baseline est nécessaire avant cartographie exhaustive des claims.

## Résultats déterministes

| Contrôle | Résultat |
|---|---:|
| HTML présents | 124 |
| IDs numériques Substack uniques dans HTML | 123 |
| IDs numériques HTML dupliqués | 1 |
| Lignes `posts.csv` | 123 |
| CSV `is_published=true` | 122 |
| CSV `is_published=false` | 1 |
| Entrées numérotées `index.md` | 124 |
| IDs index uniques | 124 |
| IDs index manquants dans 1..125 | 113 |
| Lignes table index malformées | 16 |
| Stems CSV↔HTML identiques | 122 |
| Stems CSV sans HTML | 1 |
| Stems HTML sans CSV | 2 |
| URL-slugs index↔HTML exacts | 120 |
| Entrées index à URL placeholder | 1 |
| Entrées index URL sans HTML correspondant | 3 |
| HTML sans slug correspondant dans index | 4 |
| HTML vides / quasi-vides (<100 caractères texte) | 0 |
| HTML non UTF-8 | 0 |
| HTML avec octet NUL | 0 |

## P0 — bloque la cartographie exhaustive

### P0-1 — Il n’existe pas de liste canonique des « articles publiés »

Les trois représentations ne sont pas équivalentes :

- `index.md` contient **124 entrées numérotées** et affirme « 124 posts publiés » ;
- `posts.csv` contient **123 lignes**, dont **122 seulement `is_published=true`** ;
- `posts/` contient **124 HTML mais seulement 123 IDs numériques uniques**, car l’ID `194518266` existe sous deux versions différentes.

Conclusion : **le nombre 124 ne peut pas être utilisé comme cardinal canonique sans résolution des anomalies ci-dessous.**

### P0-2 — Le snapshot n’est pas le corpus public courant au 2026-09-05

Le snapshot est daté du 26 août 2026 et s’arrête éditorialement au post du 25 août. Le Substack public expose au moins un article ultérieur :

- `⏳ Quand le travail ne vaut plus son temps`, publié le **28 août 2026** : `https://giak.substack.com/` (visible dans l’accueil public lors du contrôle du 2026-09-05).

Donc, pour le nouvel article qui doit exploiter **tout le corpus existant**, ce ZIP est au minimum incomplet d’un article récent. Cette obsolescence est normale pour un snapshot du 26 août, mais elle interdit de l’appeler « corpus courant exhaustif ».

## P1 — anomalies de réconciliation

### P1-1 — Deux HTML différents pour le même ID Substack

`194518266` :

- `194518266.3b3.html`
- `194518266.lingenierie-de-lenclos.html`

Les fichiers ne sont ni identiques byte-à-byte ni textuellement identiques. Similarité séquentielle par mots : **0.766**. Le second est celui référencé par `posts.csv` et par l’URL canonique de l’index ; `3b3` doit donc être traité comme **version/révision orpheline candidate**, pas comme article distinct, tant que sa provenance n’est pas établie.

### P1-2 — CSV ↔ HTML

**CSV sans HTML exact :**

- `140803312.coming-soon`

`140803312.coming-soon` est marqué `is_published=true`, mais il ne possède aucun HTML dans le snapshot et correspond à un placeholder « Coming soon ». Le booléen CSV n’est donc pas, à lui seul, un critère suffisant d’article publiable dans notre corpus analytique.

**HTML sans ligne CSV exacte :**

- `181863121.truth-engine-lia-qui-revolutionne`
- `194518266.3b3`

- `194518266.3b3` : duplication/version candidate décrite ci-dessus ;
- `181863121.truth-engine-lia-qui-revolutionne` : **orphelin de métadonnées CSV**, statut de publication à résoudre avant inclusion/exclusion.

### P1-3 — HTML publié présent dans CSV mais absent de l’index

`206006558.police-francaise-anatomie-dun-systeme` est :

- présent en HTML ;
- `is_published=true` dans `posts.csv`, daté du **2026-07-10** ;
- absent de `index.md` ;
- actuellement accessible publiquement sur Substack : `https://giak.substack.com/p/police-francaise-anatomie-dun-systeme`.

L’index n’est donc pas exhaustif même relativement à des éléments publiés présents dans le snapshot.

### P1-4 — Un HTML explicitement non publié est mélangé aux posts

`191030786.linflation-normative-francaise` :

- HTML présent ;
- CSV `is_published=false` ;
- `post_date`, `title` et `subtitle` vides ;
- absent de l’index.

Il doit être classé **DRAFT/UNPUBLISHED** et exclu par défaut de la cartographie des articles publiés, sauf décision explicite contraire.

### P1-5 — Quatre entrées d’index ne correspondent à aucun HTML du snapshot

- #122 `URL_PLACEHOLDER` — 🗄️ L'opacité n'est pas l'absence d'information
- #116 `la-honte-francaise-du-tortionnaire-sisi-aux-soldats-de-zelensky` — 🔒 La honte française : du tortionnaire Sisi aux soldats de Zelensky, une décennie de complicité (2014-2026)
- #115 `lasphyxie-du-golem-derives-systemiques-1789-2026` — 🔒 L'asphyxie du Golem v7 : dérives systémiques d'un verrouillage français (1789-2026) — 5684 mots, 7 actions CP2 appliquées
- #114 `lasphyxie-du-golem-verrouillage-multiseculaire-fr` — 🔒 L'asphyxie du Golem : anatomie forensique d'un verrouillage français qui ne s'est jamais refermé (1789-2026)

Le cas #122 est particulièrement clair : l’URL est littéralement `{URL à compléter manuellement avant publication}`. Cette entrée ne doit pas être comptée comme « publiée » tant que son statut n’est pas résolu.

Les trois autres entrées possèdent des URLs Substack dans l’index mais ne sont présentes ni dans le CSV ni dans les HTML du snapshot. Leur statut actuel n’a pas été établi par les recherches publiques réalisées pendant INV-001 ; ne pas inventer `deleted`, `private` ou `published`.

### P1-6 — 16 lignes Markdown de l’index sont structurellement malformées

Elles commencent comme lignes de table mais n’ont pas le séparateur `|` terminal :

`#21, #64, #65, #66, #67, #68, #69, #80, #81, #82, #83, #84, #85, #86, #87, #88`

Cela n’empêche pas la lecture humaine, mais casse un parsing Markdown strict. Une cartographie automatisée fondée sur le tableau perdrait exactement ces **16 articles** si elle exige six séparateurs.

### P1-7 — Deux divergences de date index ↔ CSV

- #120 `machine` : index `2026-08-03` vs CSV `2026-08-02`
- #117 `la-fabrique-de-la-menace-comment` : index `2026-07-28` vs CSV `2026-07-29`

Contrôle public : `la-fabrique-de-la-menace-comment` est actuellement affiché **29 juillet 2026**, ce qui confirme le CSV et invalide la date du 28 juillet dans l’index. Pour `machine`, le contrôle externe n’a pas fourni de date suffisamment probante pendant cette passe ; rester OPEN.

## P2 — durcissement souhaitable

1. Le ZIP ne contient pas de manifest cryptographique interne. Le présent audit génère `INV-001_CORPUS_MANIFEST.csv` avec taille et SHA-256 de chaque fichier.
2. Le champ `is_published` ne suffit pas à définir le périmètre analytique ; établir une colonne canonique `corpus_status = PUBLISHED | DRAFT | REVISION | ORPHAN | UNRESOLVED` lors de la réparation.
3. Ne pas utiliser le numéro éditorial de `index.md` comme identité primaire. L’identité robuste doit reposer d’abord sur l’ID numérique Substack quand il existe, puis le slug canonique.

## Ce qui résiste à l’audit

- Les 124 HTML sont lisibles en UTF-8 ; aucun n’est vide/quasi-vide et aucun octet NUL n’a été détecté.
- Aucun doublon byte-à-byte ou texte normalisé exact n’a été détecté parmi les HTML.
- `index.md` contient bien **124 numéros distincts** et son propre énoncé « IDs 1-125, #113 absent » est arithmétiquement cohérent.
- L’essentiel du corpus se recoupe : **120 URL-slugs d’index** correspondent exactement à des HTML et **122 stems CSV** correspondent exactement à des HTML.

## Décision

**INV-001 ne passe pas. INV-002 reste bloquée.**

Baby-step recommandé, zéro redesign :

1. produire un **snapshot Substack courant** ou déclarer explicitement que le corpus de travail est figé au 2026-08-26 ;
2. résoudre uniquement les objets divergents : `194518266`, `181863121`, `191030786`, `206006558`, `140803312`, les 4 entrées index-only ;
3. corriger les 16 lignes Markdown et la date confirmée du 29 juillet ;
4. reconstruire une liste canonique unique des articles `PUBLISHED` ;
5. rejouer uniquement les contrôles INV-001 ;
6. **PASS INV-001 -> autoriser INV-002**.

Aucune analyse des thèses du corpus n’a été commencée.
