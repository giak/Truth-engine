# Évaluation d'une relecture externe — dossier Insee V5

Un relecteur extérieur (autre modèle) a rendu un verdict sévère sur « la nouvelle version » :
méthode meilleure, texte « pas encore blindé », sept corrections dites obligatoires. Ce document
consigne ce que cette relecture vaut, ce qu'elle a trouvé, ce qu'on en a fait, et le défaut de
procédure qu'elle révèle.

---

## 1. Il a relu deux fichiers, dont un a quatre passes de retard

Le partage des citations est net : chaque phrase citée vit dans un seul fichier, et les deux
fichiers sont `2026-09-23_05-48_insee-v4-maestro…ARTICLE.md` (7 523 mots) et le fichier de
travail `2026-09-23_06-00_…v38…ARTICLE.md` (8 846 mots).

| Citation du relecteur | Fichier où elle vit |
|---|---|
| Titre « Ce que l'INSEE ne vous dira jamais » | v4 de 05 h 48 |
| « structurellement bas » | v4 (absent du fichier actuel) |
| « 10 à 18 % » | v4 |
| « habitants manquants » | v4 |
| « quantifie l'imprécision à ±17 500 » | v4 |
| « H1 est morte telle que formulée » | v4 |
| « désigne un **choix** » | v4 |
| « un système qui se trompe dans les deux sens » | v4 |
| « exclut le logement des propriétaires » | v4 |
| Appendices, notes numérotées `[41]`, `[30]` | v4 (supprimés depuis) |
| « Parler de dissimulation serait commode et faux » | fichier actuel |
| « absence de contre-preuve, non une preuve » | fichier actuel |
| « Lorsque l'écart entre deux chiffres est inférieur à leur marge » | fichier actuel |
| « Ce qui est établi, c'est le niveau, 8,3 % » | fichier actuel |
| « Presque tout est publié ; presque rien n'est dit » | fichier actuel |
| « Le mot “chômage” ne désigne pas un fait » | fichier actuel |

**Cinq des sept corrections dites obligatoires portent donc sur des phrases qui n'existent plus**,
et trois de ces phrases figurent depuis 07 h 45 dans la liste noire mécanique du projet
(`check_figures_insee.py`). Un verdict rendu sans nommer la révision qu'il juge ne peut servir
à décider quoi que ce soit.

## 2. Ce qu'il a trouvé de juste, et qui avait survécu à toutes les passes

**a. « Presque rien n'est dit » — la formule avait perdu son sujet.** Le corps écrit, trois
paragraphes plus haut, la version correcte : « Tout ce qu'il faut pour lire un chiffre est
publié ; rien de tout cela n'atteint le lecteur. » La formule de clôture, citée seule, dit que
l'institut ne dit rien — ce que l'article réfute. Elle figurait **deux fois** : dans le corps et
dans la conclusion de la FIG. 01. Le contrôleur avait déjà retiré la moitié de la phrase
(« tout est publié » → « presque tout est publié ») et s'était arrêté en chemin.

**b. La règle générale de la marge érigeait une précision en verdict d'inexistence.**
« Lorsque l'écart entre deux chiffres est inférieur à leur marge, la hausse et la baisse qui
alimentent les débats ne sont pas des événements. » Le projet avait déjà écrit la correction, dans
la raison de sa propre liste noire : *« absolu retiré : un mouvement dans la marge n'y démontre
rien »*. Le corps disait encore « n'**y** signifie rien ». Le contrôle n'a jamais déclenché parce
qu'il ne balayait que les figures.

## 3. Ce qui a été corrigé

| Avant | Après |
|---|---|
| « de sorte qu'un mouvement d'un dixième **n'y signifie rien** » | « … **n'y démontre rien** » (formulation prescrite par la liste noire du projet) |
| « … inférieur à leur marge, la hausse et la baisse … **ne sont pas des événements**. » | « … inférieur à leur marge, **cette marge interdit d'en établir le sens, non d'en nier l'existence** : la hausse et la baisse … **n'y trouvent pas leur preuve**. » |
| « Presque tout est publié ; presque rien **n'est** dit. » | « Presque tout est publié ; presque rien **n'en est** dit. » (corps et FIG. 01) |
| FIG. 01, étage 4 : « la marge **n'est jamais reprise** » | « la marge **s'arrête** ici » (l'universel n'était pas tenu : 19 articles lus sur 29 candidats) |
| FIG. 01, étage 5 : « **rien n'a été caché** » | « **aucune pièce cachée trouvée** » (le dossier établit une absence de contre-preuve, pas une absence de dissimulation) |

Les deux dernières ont été trouvées en relisant le rendu de la FIG. 01 après régénération : elles
portaient le même défaut que la clôture, dans un endroit que le relecteur extérieur n'avait pas
regardé et qu'aucune passe précédente n'avait vu.

## 4. Ce que la relecture a fait changer à l'outillage

La vraie leçon n'est pas dans les phrases, elle est dans la portée du contrôle. La liste noire
ne servait à rien appliquée aux seules figures : c'est dans le corps qu'un sur-claim naît, sans
largeur de panneau ni relecture visuelle pour l'arrêter.

- `check_figures_insee.py` porte désormais un **quatrième contrôle : la liste noire sur le corps**,
  ligne par ligne, citations entre guillemets retirées (« une pièce se cite, elle ne s'écrit
  pas »). 145 lignes de prose examinées, zéro faux positif.
- Motif élargi : « signifie rien » (l'ancien « ne signifie rien » laissait passer « n'y signifie
  rien » — un défaut d'une lettre qui a coûté deux passes).
- Quatre motifs ajoutés, chacun avec sa raison : « presque rien n'est dit » (sujet manquant),
  « ne sont pas des événements » (raccourci retiré), « rien n'a été caché » (universel non tenu),
  « n'est jamais reprise » (universel hors corpus).
- **Essai de régression** : une phrase volontairement fautive (« structurellement bas », « tout
  est publié ») a été injectée dans le corps, le contrôle l'a refusée avec ses deux motifs, puis
  l'injection a été retirée. Le contrôle bloque, il ne conseille pas — code de sortie 1.

## 5. Ce qui reste ouvert, et qui n'est pas tranché

- **Le titre.** « L'Insee publie, il n'explique pas » situe la défaillance du côté de l'institut,
  quand le corps la situe dans la transmission (« rien de tout cela n'atteint le lecteur »).
  Une variante d'un mot existe : « L'Insee publie ; l'explication ne suit pas ».
- **Le vocabulaire des hypothèses.** H2 « est morte » puis « survit en version faible » : la
  distinction est juste, le mot ne l'est pas tout à fait. Formulation forensique possible :
  « la forme forte n'est pas étayée ; une forme faible subsiste ». Même chose pour la colonne de
  verdict de la FIG. 05.

## 6. Ce que cette relecture prouve, au fond

Son diagnostic général est le bon, et il restera le bon : la vulnérabilité du dossier s'est
déplacée des preuves vers l'écart entre les preuves et certaines phrases. Ses trois prises
survivantes sont toutes de cette famille. Son appareil, lui, ne vaut rien : il note un fichier
qui n'est plus le dossier, sans dire lequel il a lu. Et sa prose échoue au test qu'il propose —
« Cela ne permet pas de conclure que la hausse est inexistante ; cela signifie que son ampleur
doit être interprétée avec la précision annoncée » est exactement la langue de bois que le
contrat éditorial interdit.

**Décision de procédure.** Toute relecture externe doit désormais citer la révision qu'elle juge.
L'empreinte est produite par l'outil, elle n'est pas recopiée à la main : `check_figures_insee.py`
termine par « Révision jugée : `<empreinte>` · `<mots>` mots · `<figures>` figures », l'empreinte
portant sur l'article **et** les figures. Sans ce nom, une relecture produit des faux positifs en
série et coûte une passe à corriger des phrases déjà mortes.
