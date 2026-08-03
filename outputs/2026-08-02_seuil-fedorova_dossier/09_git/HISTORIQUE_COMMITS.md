# Historique Git du dossier Fedorova

**Dépôt :** truth-engine (local)
**Période couverte :** 29 mai 2026 (normalisation des archives) → 3 août 2026 (constitution finale du dossier)

Ce dossier retrace la vie du dossier dans l'historique Git. Quatre commits de production portent directement le travail Fedorova (dans `articles/` et `investigations/`), auxquels s'ajoutent un commit d'archivage antérieur (les enquêtes Moreau de décembre 2025, sources du parallèle central de l'article) et les quatre commits qui ont constitué puis enrichi le répertoire du dossier lui-même (`849f4d6`, `2b00b4f`, `8a70bee`, `44961e3`, section 5 ci-dessous).

---

## Les commits du dossier

### 1. `5162a867` — 30 juillet 2026, 20h03 — LE COMMIT FONDATEUR

**Titre :** `feat(article): anatomie forensique expulsion Fedorova-OQTF — 35 strates, 8 KO sentences, N=35`

**Message complet :**
> - 3 articles: anatomie forensique (4312 mots), roman noir pouvoir, declarations vs accusations
> - 35 strates d'investigation + 35 quintessences + rapport Phase 2 + blueprint narratif
> - Cartographie 60+ intervenants mainstream (Ukraine, Israel, Palestine, USA/OTAN)
> - Asymetrie: 13 pro-ukrainiennes vs 4 pro-russes, 19 pro-israeliennes vs 2-3 palestiniennes
> - CNews: 9 pro-israeliens, 0 palestiniens, 0 ukrainiens
> - Format: chiffres en digits, gras strategique, 3 liens Substack, zero em-dash

**Ce qu'il contient :** l'intégralité du travail d'enquête et la première génération d'articles. C'est le commit le plus massif du dossier (plus de 1 Mo de diff) : les 3 articles brouillons, les 35 strates APEX, la synthèse terminale, les 5 cartographies d'intervenants médias. Il fige l'état du dossier après deux jours d'enquête intensive (30-31 juillet).

**Fichiers clés :**
- `articles/2026-07-31_23-30_fedorova-fourest-oqtf-roman-noir-pouvoir-francais_ARTICLE.md` (v1, roman noir)
- `articles/2026-07-31_23-35_fedorova-oqtf-anatomie-forensique_ARTICLE.md` (v2, anatomie forensique)
- `articles/2026-07-31_23-45_fedorova-declarations-vs-accusations-rapprochement_ARTICLE.md` (v3)
- 35 strates dans `investigations/2026-07/2026-07-30_Caroline-Fourest-Xenia-Fedorova-OQTF/`
- Synthèse terminale + outputs intervenants médias

### 2. `2ff5a9a8` — 30 juillet 2026, 23h08 — LA CORRECTION POST-AUDIT

**Titre :** `feat(article): correction post-audit Fedorova-OQTF + index #118 peuple-convocation`

**Message complet :**
> - Corrections post-audit de l'article anatomie forensique
> - Ajout de l'audit critique de la première version (644 lignes)
> - Corrections de deux quintessences (V192 mandat CPI Poutine, V218 camps filtration russes)
> - Ajout de l'entrée #118 à l'index Substack

**Ce qu'il contient :** la première boucle audit-correction. L'article passe d'une copie « anatomie forensique » à la version corrigée, sous la critique de `Audit_critique_article_Fedorova.md` (644 lignes). Deux quintessences sont corrigées en profondeur (le mandat CPI contre Poutine, les camps de filtration russes) : preuve que l'audit a bien servi à vérifier les faits, pas seulement le style.

### 3. `6458d32f` — 2 août 2026, 09h37 — LA VERSION FINALE PUBLIÉE

**Titre :** `feat(about): page About v9 + machine.md via protocole APEX (vestibule 1105 mots, dossier 2175 mots)`

**Message complet :**
> - Page About v9 + machine.md via protocole APEX

**Ce qu'il contient (pour le dossier Fedorova) :**
- `2026-07-31_du-narratif-a-la-menace_affaire-fedorova_ARTICLE (9).md` : la neuvième itération, celle qui porte le titre définitif « Du « narratif » à l'ingérence : le seuil Fedorova » (466 lignes ajoutées)
- `Audit_critique_nouvelle_version_Fedorova.md` (908 lignes) : l'audit intermédiaire
- `Audit_forensique_article_Fedorova_v25.md` (889 lignes) : l'audit final qui a validé la version publiée
- Mise à jour de `substack-online/index.md` avec l'entrée #119

Le titre de ce commit couvre la page About, mais le commit contient aussi la validation définitive du dossier Fedorova : c'est ici que le texte publié entre dans l'historique.

### 4. `3417673c` — 29 mai 2026 — L'ARCHIVAGE DES SOURCES MOREAU

**Titre :** `archive: normalisation complete de la structure (legacy- prefix + fusion outputs)`

**Ce qu'il contient :** le déplacement des enquêtes Moreau de décembre 2025 (sanctions UE contre Xavier Moreau) vers `archive/legacy-outputs/logs/`. Ce ne sont pas des commits de travail, mais c'est le moment où les sources antérieures citées par l'article (le précédent Moreau) ont été archivées à leur emplacement actuel.


### 5. `849f4d6`, `2b00b4f`, `8a70bee`, `44961e3` — LA CONSTITUTION DU RÉPERTOIRE DU DOSSIER

Les quatre commits précédents portent la production de l’article dans `articles/` et `investigations/`. Le répertoire `outputs/2026-08-02_seuil-fedorova_dossier/` lui-même a été constitué ensuite, en quatre commits :

| Commit | Date | Rôle |
|--------|------|------|
| `849f4d6` | 2 août 2026, 22h15 | La constitution du dossier : 103 fichiers (00-09), l’article final, les audits, la correction de numérotation S15/S18 |
| `2b00b4f` | 2 août 2026, 23h01 | Le README navigable du dossier (sommaire, liens, lexique, 3 schémas) |
| `8a70bee` | 3 août 2026, 11h31 | L’intégration de l’article sur la méthode (« Un hybride sans équivalent »), liens réécrits en relatifs |
| `44961e3` | 3 août 2026, 14h45 | Les architectures Sublimator et Writer dans `10_protocole/` et le renommage précis des fichiers de protocole |

Le message de `849f4d6` annonce « 103 fichiers » : c’est le compte à la constitution du dossier. Le dépôt Git en suit aujourd’hui 114, et le dossier complet en contient 120 : 114 fichiers suivis + 6 visuels (PNG/SVG) ignorés par le dépôt (règle `*.png`, `*.svg` du `.gitignore`) = 120. Le compte Git est passé de 113 à 114 le 3 août 2026, avec l’ajout du fichier de table des strates (`02_enquetes/2026-08-03_TABLE-STRATES-S1-S35.md`).

---

## Chronologie complète du dossier

| Date | Commit | Événement |
|------|--------|-----------|
| 2025-12-15 | (pré-git) | Enquêtes APEX Moreau : sanctions UE contre Xavier Moreau (sources antérieures) |
| 2026-05-29 | `3417673c` | Archivage des enquêtes Moreau dans `archive/legacy-outputs/logs/` |
| 2026-07-29 | (fait brut) | Arrêté d'expulsion contre Fedorova (événement, hors git) |
| 2026-07-30 | `5162a867` | Enquête complète : 35 strates + 3 articles + synthèse terminale |
| 2026-07-30 | `2ff5a9a8` | Audit critique 1 → corrections post-audit |
| 2026-07-31 | (publication) | Article publié sur Substack (post #119) |
| 2026-08-02 | `6458d32f` | Version finale (9) + audits 2 et 3 validant le texte + index #119 |
| 2026-08-02 | `849f4d6` | Constitution du dossier (00-09, 103 fichiers) |
| 2026-08-02 | `2b00b4f` | README navigable du dossier |
| 2026-08-03 | `8a70bee` | Intégration de l’article sur la méthode |
| 2026-08-03 | `44961e3` | Architectures Sublimator/Writer + renommage `10_protocole/` |

---

## Comment utiliser ces fichiers

Les fichiers `commit_<hash>_message.txt` contiennent le message de commit complet (titre + corps), dans l'ordre chronologique du travail. Pour retrouver l'état exact du dossier à un instant donné, l'historique Git du dépôt permet de faire `git show <hash>:<chemin>` sur n'importe quel fichier.

Note de méthode : l'écart entre le commit `2ff5a9a8` (30 juillet, 23h08) et `6458d32f` (2 août, 09h37) recouvre la production des itérations 4 à 9 de l'article, qui n'ont pas fait l'objet de commits séparés : le dépôt fige les états validés, pas chaque essai. Les versions intermédiaires figurent en revanche dans `01_brouillons_audits/`.
