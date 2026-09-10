# Réconciliation des comptes Substack — 2026-09-10

Trois sources, trois totaux apparents (124 / 121 / 125). Vérification croisée ID par ID
(posts.csv × index.md × `posts/*.html`, matching par titre normalisé). Résultat :

## Le chiffre canonique

**120 articles réels publiés** (période 2025-11-26 → 2026-08-25).

```text
122 lignes posts.csv is_published=true, type=newsletter
 − 1  « Coming soon » (140803312, 2024-01-18, placeholder)
 − 0  (la page « type=page » 209458739 n'est jamais comptée dans les 122 : type≠newsletter)
 = 120
```

Corroboration : 119 titres de `index.md` matchent l'export + 1 publié absent de l'index
(`Police française…`, 206006558, 2026-07-10) = 120.

## Les trois sources

| Source | Total apparent | Réalité |
|---|---|---|
| `posts.csv` (export officiel 2026-08-26) | 122 published | **120 réels** : 122 − « Coming soon ». La ligne `type=page` est hors des 122. |
| `index.md` | « 124 » | **119 publiés réels** listés + **5 brouillons locaux jamais publiés** (114, 115, 116, 120, 122) + l'écart de date #117 (28 vs 29). Le « 124 » d'en-tête compte donc des lignes non publiées — et oublie 1 publié. |
| `posts/*.html` | 125 fichiers | **124 posts uniques** : le fichier `194518266.3b3.html` est une **vieille version** (avril) du même post que `194518266.lingenierie-de-lenclos.html` (août, version export). S'y ajoutent 2 fichiers `.csv` mal nommés dans `posts/` (`194518266.delivers.csv`, `194518266.opens.csv`) à nettoyer. |

## Écarts détaillés

1. **Brouillons listés dans index.md comme publiés** (5) : #114 « L'asphyxie du Golem v7 »,
   #115 « L'asphyxie du Golem (série) », #116 « La honte française », #120 « La machine qui
   documente les machines », #122 « L'opacité n'est pas l'absence d'information ».
   Aucun n'existe dans l'export ni sur le site live (vérifié 2026-09-10). Le verrouillage 🔒
   dans le titre n'est pas un statut de publication.
2. **Publié absent d'index.md** (1) : « Police française : anatomie d'un système de contrôle »
   (206006558, 2026-07-10) — présent dans l'export, absent de la table.
3. **Date #117** : index.md dit 2026-07-28, l'export 2026-07-29 (« La fabrique de la menace »,
   208733314). L'export fait foi.
4. **#122 de index.md porte une URL placeholder** `{{URL à compléter manuellement avant
   publication}}` — confirmant son statut de brouillon.
5. **Doublon de fichier** : `194518266.3b3.html` = ancienne version d'un post publié ; les
   fichiers `*.delivers.csv` / `*.opens.csv` dans `posts/` ne sont pas des posts.

## Verdict

- **Source canonique pour tout décompte : `posts.csv` (export officiel)**, filtre
  `is_published=true AND type=newsletter AND titre ≠ « Coming soon »`.
- `index.md` = vue éditoriale utile (thèses, mots-clés) mais **pas** un registre de publication ;
  ses compteurs d'en-tête étaient faux (124) et sa table mélange publiés et brouillons.
- Le chiffre public borné reste : **« plus de 120 articles depuis novembre 2025 (export août 2026) »** —
  plancher daté, conservateur, utilisé dans PEB (MET-0011, STRONG) et le playbook LinkedIn.

## Actions appliquées

- MET-0011 (PEB) : 121 → **120**, note corrigée (122 − Coming soon − 0 ; la page n'a jamais
  été dans le compte — erreur d'arithmétique de la note précédente assumée ici).
- index.md : correction de l'en-tête et note de renvoi vers ce fichier.
- Nettoyage `posts/194518266.3b3.html` + 2 `.csv` égarés : à valider avant suppression.
