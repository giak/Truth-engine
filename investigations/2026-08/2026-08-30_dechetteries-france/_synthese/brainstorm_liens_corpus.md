# BRAINSTORM — Intégration des liens wiki corpus dans l'article déchèteries

> Date : 2026-08-31 · Aligné sur `prompt-v38_phase3.md` §3.1 (Mapping Substack) et `prompt-phase2_5_raisonnement_narratif.md` (Q6 orchestration).
> Décision de cadrage : le dossier `substack-online/` est un corpus d'articles publiés, **on n'y touche pas**. Les liens se font dans le sens article → corpus, avec URLs verbatim relevées depuis `substack-online/index.md`.

---

## 1. Position de l'article dans l'édifice : un « verrou » de plus

L'édifice Truth Engine documente une typologie de verrous : constitutionnel (Le verrou invisible #1, L'asphyxie du Golem #114/#115), médiatique (Le Verrou #14, La Machine à silence #56), financier (Comment la richesse verrouille le système #44), judiciaire (La Justice Fantôme #12), numérique (Le Numérique colonisé #13), informationnel (Qui fabrique l'autorité du vrai #123, L'ingérence sans mesure #121).

**L'article déchèteries ajoute un type manquant : le verrou de proximité.** Le seul verrou que le citoyen touche physiquement, sans jamais le voir comme tel. C'est la démonstration que le pattern se reproduit à l'échelle d'un guichet communal : captation (soutiens REP > revente), contrôle (badges, quotas), exclusion (pros, non-connectés), transfert de coût (dépôts sauvages), opacité (donnée d'exploitation non publiée).

**Thèse d'édifice : si la structure du verrou se reproduit jusque dans l'équipement qui récupère les gravats, elle n'est pas un accident, c'est un pattern systémique.**

---

## 2. Mapping Substack (v38 §3.1) — table candidate

| Rôle dans l'article | Article lié | URL verbatim (index) | Emplacement proposé |
|---|---|---|---|
| **Article-concept** (cadre « verrou institutionnel ») | **Le verrou invisible** #1 | `https://giak.substack.com/p/le-verrou-invisible-anatomie-du-ric` | §0 introduction (1 des 2 max) |
| **Article-concept** (captation de la valeur/dépendance) | **L'architecture de la dépendance** #2 | `https://giak.substack.com/p/larchitecture-de-la-dependance` | §3 L'argent du guichet |
| **Article-concept** (verrouillage numérique = QR code) | **Le Numérique colonisé** #13 | `https://giak.substack.com/p/le-numerique-colonise-70-des-donnees` | §6 Les exclus (illectronisme) |
| **Article-concept** (arsenal de contrôle) | **La Machine à silence** #56 | `https://giak.substack.com/p/la-machine-a-silence` | §5 Le verrou (badges/quotas) |
| **Article-donnée** (opacité = accès différencié) | **L'opacité n'est pas l'absence d'information** #122 | ❌ **PAS D'URL PUBLIÉE** (placeholder dans l'index) | **EXCLU** (règle v38 : s'abstenir si URL non verbatim) |
| **Article-donnée** (angle mort de la gestion publique) | **La Justice Fantôme** #12 | `https://giak.substack.com/p/la-justice-fantome-020-du-pib-86` | §8 À qui profite (Cour des comptes/DSP) |
| **Article-concept** (régime d'accès à la donnée) | **L'ingérence sans mesure** #121 | `https://giak.substack.com/p/lingerence-sans-mesure` | §8 (machine qui s'étend plus vite que sa mesure) |
| **Article-concept** (méthode d'audit de la donnée officielle) | **Qui fabrique l'autorité du vrai ?** #123 | `https://giak.substack.com/p/qui-fabrique-lautorite-du-vrai` | §0 ou §9 (méthode) |

---

## 3. Règles v38 à respecter (contraintes dures)

1. **URLs verbatim** : les liens ci-dessus sont extraits exactement de `substack-online/index.md`. Aucune URL devinée.
2. **Post 122 exclu** : l'index affiche `{{URL à compléter manuellement avant publication}}` pour « L'opacité n'est pas l'absence d'information ». La règle v38 §3.1 impose de **s'abstenir** : on ne lie pas un article non publié. Le retirer de la liste des 4 du bloc « Pour aller plus loin ».
3. **Anti-saturation** : max 3 liens Substack par section ; max 2 dans §0 et dans le verdict. Donc :
   - §0 : max 2 (Le verrou invisible + 1 autre)
   - §3, §5, §6, §8 : max 3 chacun (on visera 1-2 par section, sobriété)
   - Total visé : **5-6 liens** dans le corps + bloc final, pas 8.
4. **Format de citation** : `**[Titre complet](URL)**` directement dans le corps du texte, pas en note de fin.
5. **Un mécanisme déjà documenté = cité, pas réexpliqué** : ne pas redéfinir « verrou institutionnel » ou « illectronisme » si le corpus l'a déjà fait ; renvoyer.
6. **Zéro em-dash** dans tout lien comme dans la prose.

---

## 4. Proposition d'implantation (5 liens + bloc final réduit)

### 4.1 §0 Introduction méthodologique (2 max)

> « Cet article s'inscrit dans une série d'enquêtes sur les verrous français : **[Le verrou invisible](https://giak.substack.com/p/le-verrou-invisible-anatomie-du-ric)** a documenté l'absence d'initiative populaire, **[Qui fabrique l'autorité du vrai ?](https://giak.substack.com/p/qui-fabrique-lautorite-du-vrai)** l'audit de la donnée officielle. Il en est le versant le plus ordinaire : le verrou du quotidien, celui qu'on franchit avec ses poubelles. »

### 4.2 §3 L'argent du guichet (1 lien)

> « La collectivité reste le payeur de dernier ressort ; l'éco-organisme reste le propriétaire des matériaux, par contrat. Cette relation de dépendance n'est pas propre aux déchets : **[L'architecture de la dépendance](https://giak.substack.com/p/larchitecture-de-la-dependance)** la documente à l'échelle des 64 secteurs de l'économie. »

### 4.3 §5 Le verrou (1 lien)

> « Chaque badge, chaque quota transforme la déchèterie en point de contrôle. L'arsenal existe déjà à l'échelle nationale : **[La Machine à silence](https://giak.substack.com/p/la-machine-a-silence)** en a documenté la construction législative depuis 2015. »

### 4.4 §6 Les exclus (1 lien)

> « L'accès suppose désormais deux conditions : le numérique et l'automobile. Le versant numérique de cette exclusion est documenté : **[Le Numérique colonisé](https://giak.substack.com/p/le-numerique-colonise-70-des-donnees)** mesure la dépendance française aux GAFAM, dont le QR code de déchèterie est un cas d'application municipale. »

### 4.5 §8 À qui profite le guichet (2 liens)

> « La Cour des comptes juge ces délégations un "angle mort de la gestion publique" : le même diagnostic vaut pour la justice, **[sous-dimensionnée au point d'être une justice fantôme](https://giak.substack.com/p/la-justice-fantome-020-du-pib-86)**. Et la machine s'étend plus vite que sa mesure, comme **[l'ingérence sans mesure](https://giak.substack.com/p/lingerence-sans-mesure)** l'a montré ailleurs : le contrôle d'accès se déploie sans série nationale sur ses effets. »

### 4.6 Bloc final « Pour aller plus loin » (réduit de 4 à 3 liens + 1 nom sans lien)

> **Pour aller plus loin.** Cet article poursuit une série d'enquêtes sur les verrous français : **[Le verrou invisible](URL)** (l'absence d'initiative populaire), **[La Machine à silence](URL)** (l'arsenal de contrôle numérique), **[Le Numérique colonisé](URL)** (la dépendance aux GAFAM). Il en est le versant le plus ordinaire : le verrou du quotidien, celui qu'on franchit avec ses poubelles.

> **⚠️ Le post 122 (L'opacité n'est pas l'absence d'information) est RETIRÉ du bloc final** : pas d'URL publiée → règle v38, s'abstenir. Le remplacer par un nom sans lien est interdit aussi (un titre de post publié se cite avec son URL ; un titre non publié ne se cite pas). À réintégrer quand le post 122 sera publié.

---

## 5. Ce que le corpus gagne (réciproque, sans toucher au dossier)

La réciproque (liens depuis les anciens articles vers le nouveau) est **hors périmètre** : `substack-online/` est un corpus publié qu'on ne modifie pas. La réciproque se fera naturellement par l'indexation du nouvel article dans `substack-online/index.md` au moment de la publication (entrée 126), qui listera ses liens sortants.

---

## 6. Décisions à trancher

1. **Nombre total de liens** : proposition = 6 dans le corps (§0×2, §3, §5, §6, §8×2) + 3 dans le bloc final = 9 liens. La règle v38 limite à 3 par section, pas au total : 9 est dans les clous. Alternative plus sobre : 4 dans le corps (supprimer §5 ou §6) + 3 final = 7.
2. **Le bloc final cite « L'opacité » sans lien ?** Non (règle v38). Soit on le garde nommé sans hyperlien (hors règles), soit on le retire. Recommandation : **retirer**, réintégrer à la publication du post 122.
3. **§0 : Le verrou invisible + Qui fabrique l'autorité du vrai ?** ou **Le verrou invisible + L'architecture de la dépendance** ? Le premier couple (verrou + méthode) pose le cadre et la méthode ; le second (verrou + dépendance) pose le cadre et la thèse économique. Recommandation : **verrou invisible + architecture de la dépendance** en §0 (la thèse économique est le cœur de l'article), et glisser « Qui fabrique l'autorité du vrai » en §9 verdict (méthode) si on veut 1 lien au verdict.
