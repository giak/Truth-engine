# SEMANTIC_DIFF, tranche T2, rattachement de la déclaration de portée

Date : 13 septembre 2026. Article : `01_TARGET/ARTICLE_PUBLISH_CANDIDATE_V4_4_FR.md`. Critique traitée : **F-02, niveau P0**.

| | |
| --- | --- |
| Empreinte avant | `42f5b3745046beb797f8246c3f60fa43d26f085bca112a6d870b7d02e7d13c09` |
| Empreinte après | `02fce501c9be9f2fa7a92344f57a7464f8e003cb1f9dab8f8d69c6e27a7de78f` |
| Sauvegarde avant | `/tmp/ARTICLE_V4_4_AVANT_T2.md` |
| Lignes | 1 seule modifiée (l. 42), aucune ajoutée ni supprimée : 355 → 355 |
| Mots du corps | 10 184 → **10 213** (+29) |

---

## D1. Ce que la phrase faisait, et le défaut

**Avant, fin de l. 42** : « Elle pèse aussi sur le résultat principal de cette enquête : l’écart de preuve entre les leviers et la décision finale peut tenir, en partie, à ce que les documents laissent voir plus volontiers un point de passage qu’un ordre, **de sorte que** ce qui est établi ici est ce qu’un corpus documentaire permet d’établir, plus qu’une description générale de la manière dont le pouvoir s’exerce. »

La phrase portait deux propositions de statut différent et les reliait par un connecteur de conséquence :

- (a) une hypothèse modalisée : l’écart de preuve **peut** tenir **en partie** à l’asymétrie documentaire ;
- (b) la déclaration de portée de tout l’article.

Le connecteur faisait de (b) une conséquence de (a). Or (b) ne dépend pas de (a) : si l’asymétrie documentaire n’expliquait rien, la portée de l’article serait identique. Le défaut était donc de rattachement, pas de sens.

## D2. Après

**Après, fin de l. 42** : « Elle pèse aussi sur le résultat principal de cette enquête : l’écart de preuve entre les leviers et la décision finale peut tenir, en partie, à ce que les documents laissent voir plus volontiers un point de passage qu’un ordre. C’est une hypothèse, et elle n’est pas mesurée ici. La portée de cet article n’en dépend pas : ce qui est établi ici est ce qu’un corpus documentaire permet d’établir, plus qu’une description générale de la manière dont le pouvoir s’exerce, et cela tient à la méthode, qui s’interdit de combler les blancs par supposition. »

Trois phrases, deux statuts :

1. (a) avec sa modalisation intacte ;
2. son statut épistémique nommé, hypothèse non mesurée ;
3. (b) déclarée indépendante de (a) et rattachée à la méthode, qui reprend « non comme un vide à combler par supposition », phrase déjà présente deux lignes plus haut dans le même paragraphe.

## D3. Contrôle champ par champ

| Champ | État | Mesure ou justification |
| --- | --- | --- |
| ACTEUR | inchangé | Aucun acteur nommé ajouté. |
| ACTION / RELATION | inchangée | Les deux propositions sont conservées mot pour mot ; seul leur lien change. |
| QUANTITÉ | inchangée | Aucun chiffre ajouté ni retiré. |
| TEMPORALITÉ | inchangée | Aucune date concernée. |
| MODALITÉ | **préservée, contrôlée** | « peut tenir, en partie » : 1 occurrence avant, 1 après. « peut » : 73 avant, 73 après. « pourrait » : 2 avant, 2 après. La modalisation de (a) n’a pas bougé d’un cran. |
| NÉGATION | renforcée | `\bpas\b` : 108 avant, **110 après**. « n’est pas » : 20 avant, **21 après**. Deux négations ajoutées, aucune perdue. |
| CONDITION | inchangée | Aucune condition retirée ni ajoutée. |
| EXCEPTION | inchangée | Aucune exception concernée. |
| CAUSALITÉ | **corrigée** | « de sorte que » : 1 avant, **0 après**. C’était l’unique occurrence de l’article, vérifié par recherche. « explique » reste à 1 occurrence, inchangée : l’hypothèse n’a pas été durcie en explication. Le nouveau rattachement est explicite (« cela tient à la méthode ») et porte sur la méthode, non sur l’asymétrie documentaire. |
| DEGRÉ DE CERTITUDE | précisé | « hypothèse » : 3 avant, **4 après**. « non mesuré » ou « pas mesuré » : 2 avant, **3 après**. Le statut est nommé au lieu d’être implicite, ce qui prépare l’échelle des quatre degrés de F-11. |

Verdict : **SAFE**. Aucune des cinq régressions bloquantes du protocole (négation perdue, exception retirée, peut devenu va, suggère devenu démontre, associé à devenu cause) n’est atteinte.

## D4. Effet recherché, et ce qu’il ne règle pas

L’objection « votre limite de portée est la conséquence d’une hypothèse non démontrée » n’est plus disponible : la portée ne se présente plus comme une conséquence de l’hypothèse. Elle tient seule, adossée à une règle de méthode déjà énoncée dans le même paragraphe.

Ce que la tranche **ne règle pas** : elle ne démontre pas l’hypothèse, et ne prétend pas le faire. Le texte dit désormais explicitement qu’elle n’est pas mesurée ici. Si une mesure de l’asymétrie documentaire existe un jour dans le dossier d’enquête, elle viendra à cet endroit, et la phrase « elle n’est pas mesurée ici » devra être révisée en même temps.

## D5. HARD_GATE après insertion

Tiret cadratin U+2014 : 0. Tiret demi-cadratin U+2013 : 0. Apostrophes ASCII : 0. Guillemets : 51 ouvrants, 51 fermants. Doubles espaces : 0. `[n]` dans le corps : 0. Tableaux dans le corps : 0. Puces dans le corps : 0. Séparateurs : 7. Figures : 4. Registre : 64 entrées, séquence continue, aucune URL en double dans le registre.

**Précision sur les URL.** Un contrôle sur le document entier signale une URL présente deux fois, `https://giak.substack.com/p/lingerence-sans-mesure`. Elle est en l. 7 (encart) et en l. 283 (« Pour aller plus loin »), donc **hors registre** : c’est un renvoi éditorial, présent avant P6 et avant T2. Ce n’est pas un doublon de source.

## D6. Repères de ligne

T2 ne modifie qu’une ligne, sans en ajouter ni en supprimer. Le décalage de **+4** à partir de l’ancienne l. 155, introduit par P1 à P3, **reste valide**. Les deux entrées [63] et [64] ajoutées par P6 sont après le registre et ne déplacent aucun repère du corps.
