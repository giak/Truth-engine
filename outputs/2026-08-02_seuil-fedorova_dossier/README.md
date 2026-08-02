# Dossier complet : « Du « narratif » à l'ingérence : le seuil Fedorova »

## Comment lire ce dossier

Vous avez entre les mains la totalité de la chaîne de production d'un article d'investigation, du fait brut au texte publié. Ce dossier suit l'ordre exact dans lequel le travail a été fait : **enquête d'abord, écriture ensuite**. Chaque dossier a un rôle précis, et les fichiers s'emboîtent du bas vers le haut : les sources antérieures nourrissent les enquêtes, les enquêtes nourrissent les quintessences, les quintessences nourrissent la synthèse et le blueprint, le blueprint produit l'article, les audits le corrigent. Deux dossiers viennent compléter l'archive : les données extraites de la base de connaissances Mnemolite (08) et l'historique Git des commits qui portent le dossier (09).

---

## Schéma d'ensemble

```
07_sources_antecedentes/        (déc. 2025)  Enquêtes Moreau : le précédent
        │
        ▼
02_enquetes/                    (30-31 juil. 2026)  35 strates APEX, l'enquête brute
        │  chaque strate produit
        ▼
03_quintessences/               35 quintessences : l'essentiel de chaque strate
        │  regroupées par
        ▼
04_syntheses/                   rapport Phase 2 (agrégat) → blueprint narratif → audit antagoniste
        │
        ▼
01_brouillons_audits/           4 versions d'article + 3 audits critiques
        │  version « (9) » validée
        ▼
00_article_final/               LE TEXTE PUBLIÉ
        │
        ▼
06_publication/                 Fiche de publication Substack (#119)
```

`05_donnees_intervenants/` est un extrait transversal : les comptages de temps de parole et de présence médiatique utilisés dans l'enquête sur l'asymétrie des plateaux (strate 05 et 33).

`08_mnemolite/` et `09_git/` sont les deux couches d'archivage complémentaires : les mémoires vectorielles du projet liées au dossier, et la chronologie des commits qui le portent dans le dépôt Git.

---

## Détail dossier par dossier

### 00_article_final/ — le texte publié

Un seul fichier : `2026-07-31_du-narratif-a-la-menace_affaire-fedorova_ARTICLE_FINAL.md`. C'est la version définitive, publiée le 31 juillet 2026 sur Substack. C'est la neuvième itération du texte, la seule validée après les trois audits. Si vous ne devez lire qu'un fichier, c'est celui-ci.

### 01_brouillons_audits/ — les versions intermédiaires et leurs critiques

Quatre brouillons, dans l'ordre chronologique de leur écriture (du plus ancien au plus récent) :

| Fichier | Titre | Rôle |
|---------|-------|------|
| `2026-07-31_23-30_fedorova-fourest-oqtf-roman-noir-pouvoir-francais_ARTICLE.md` | Fedorova, le projectile : autopsie d'une OQTF | Première version, angle « roman noir du pouvoir » : la procédure administrative comme projectile d'une guerre entre milliardaires. L'audit antagoniste a jugé cet angle trop spectaculaire par rapport aux preuves. |
| `2026-07-31_23-35_fedorova-oqtf-anatomie-forensique_ARTICLE.md` | De la sanction européenne à l'expulsion nationale : la séquence Fedorova | Deuxième version, angle « anatomie forensique » : dissection de la procédure, des acteurs, des intérêts et des calendriers. Distingue ce qui est établi de ce qui ne l'est pas. |
| `2026-07-31_23-35_fedorova-oqtf-anatomie-forensique_ARTICLE copy.md` | Deux passeports, deux mesures : anatomie forensique de l'expulsion Fedorova | Variante de la précédente (titre alternatif, même matériau). |
| `2026-07-31_23-45_fedorova-declarations-vs-accusations-rapprochement_ARTICLE.md` | Fedorova : déclarations vs. reproches, l'OQTF est-elle étayée ? | Pièce analytique : confronté une par une les citations verbatim de Fedorova aux griefs de l'arrêté. Compare au cas Moreau. |

Les trois fichiers `Audit_*` sont les critiques croisées du texte :

- `Audit_critique_article_Fedorova.md` : audit de la première version, identifie les erreurs de droit, les sur-interprétations et les faits à vérifier.
- `Audit_critique_nouvelle_version_Fedorova.md` : audit de la version suivante (908 lignes de critique). C'est le plus exhaustif.
- `Audit_forensique_article_Fedorova_v25.md` : audit final, 889 lignes, vérification source par source et des formulations. C'est lui qui a validé la version « (9) ».

La règle du projet est simple : aucun article n'est publié sans être passé par un audit antagoniste, c'est-à-dire un relecteur qui cherche à démolir l'article plutôt qu'à le féliciter.

### 02_enquetes/ — l'enquête brute (le cœur du travail)

35 fichiers `*_APEX_INVESTIGATION.md` datés des 30 et 31 juillet 2026. Ce sont les investigations proprement dites : chacune suit un protocole strict (analyse textuelle, hypothèses, faits sourcés, causalités, iceberg, limites) et traite un angle spécifique du dossier. Elles sont numérotées en continu (strate 1 à 35) et se lisent dans l'ordre chronologique de leur création. Le numéro porté par le nom de fichier n'est pas systématiquement le numéro de strate : la strate 15 (Asymétrie CPI) est le fichier horodaté `12-00`, la strate 18 (Fedorova vs OQTF) est le fichier horodaté `15-00`. La correspondance exacte strate↔fichier figure dans la synthèse terminale et dans les numéros de faits des quintessences (F-S15-XXX = strate 15).

Thèmes couverts, par strate : le tweet de Fourest (S1), la guerre Křetínský-Bolloré (S2), le piège étatique (S3), la fatwa médiatique (S4), les angles morts Telegram (S5), les chaînons manquants France-Allemagne (S6), le 16e paquet de sanctions UE et la question Plenel (S7), la généalogie de la rupture Élysée-Bolloré (S8), l'asymétrie LCI/CNews (S9), le recrutement de Fedorova (S10), le financement de Franc-Tireur par Křetínský (S11), l'audit de contrôle des contradictions (S12), les gaps résiduels (S13), la couverture des médias russes (S14), l'asymétrie CPI (S15), la vérification V191/Bucha (S16), l'audit des preuves de déportation d'enfants (S17), Fedorova vs OQTF : accusation fondée ? (S18), qui établit le parallèle Moreau, les entretiens « patriotes » (S19-S20), TotalEnergies et le GNL russe (S21), les gaps bloquants et souhaitables (S22-S23), les sanctions UE Moreau (S24), la loi sur les ingérences étrangères (S25), le silence de RSF/CPJ/IPI (S26), la correction du parallèle Moreau (S27), l'anatomie juridique CESEDA vs DDHC/CEDH/PIDCP (S28), la Charte de Munich (S29), la plaidoirie forensique des 15 violations du droit (S30), la chaîne de commandement Faure DGSE→Élysée→Préfecture (S31), l'Arcom court-circuitée (S32), l'asymétrie LCI-Poedie (S33), le couple russe Philippe (S34), le financement approfondi de Franc-Tireur (S35).

Le fichier `2026-07-31_16-00_SYNTHESE-TERMINALE-FEDOROVA-FOUREST-OQTF.md` est la synthèse d'étape produite à 16h le 31 juillet, après les 18 premières strates : elle fige les faits établis, les divergences et la fiabilité composite (7,5/10) avant que l'écriture ne commence.

**Note de numérotation des strates :** la table S1-S35 de la synthèse terminale fait foi. Deux documents internes utilisent une numérotation divergente : le rapport Phase 2 et le blueprint narratif (04) lisent l'heure du nom de fichier comme un numéro de strate, appelant « S15 » la strate Fedorova vs OQTF (en réalité S18) et « S18 » l'Asymétrie CPI (en réalité S15) ; le fichier `27-00_correction-strate-15-parallele-moreau` porte le même héritage dans son titre. La numérotation canonique est confirmée par les numéros de faits des quintessences (F-S15-XXX, F-S18-XXX) et par la strate 16, qui réfère elle-même à l'« asymétrie CPI (strate 15) ».

### 03_quintessences/ — l'essentiel de chaque enquête

36 fichiers, un par strate (S1 à S35) plus la synthèse terminale. Chaque quintessence condense une enquête en un format canonique de 9 sections : thèse centrale, acteurs, causalités, données, limites, domaines, URLs sources. **C'est le niveau de lecture recommandé si vous voulez comprendre l'enquête sans lire les 35 strates complètes.** Chaque fichier est nommé par sujet (ex. `2026-07-31_24-00_moreau-sanctions-ue_quintessence.md`), pas par numéro de strate : la correspondance exacte strate↔quintessence est donnée par la table de la synthèse terminale (voir 02) et par les numéros de faits (F-S15-XXX = strate 15). Le rapport Phase 2 (voir 04) utilise une numérotation divergente pour les strates 15 et 18 (voir la note dans 02).

### 04_syntheses/ — la synthèse, le plan narratif, l'audit du plan

Trois fichiers, dans l'ordre logique de production :

1. `rapport_synthese_phase2.md` : regroupe les 35 quintessences, les classe par thème et détecte les transversalités. C'est la matière première de l'écriture.
2. `blueprint_narratif.md` : le plan narratif de l'article. Il choisit le mode (enquête), le fait surprenant (deux poids, deux mesures selon le passeport), la tension dramatique (une procédure légale sans contradictoire), la thèse organisatrice et l'angle (« anatomie systémique », ni victime ni menace). Il a évolué jusqu'à une v9.
3. `audit_antagoniste_blueprint.md` : la critique hostile du blueprint. Verdict reproduit en tête : « le blueprint a tordu la réalité documentée pour la faire entrer dans un récit trop propre ». Il a imposé 5 corrections (dont l'abandon du roman noir et le blindage du §6) avant que l'écriture finale ne commence.

### 05_donnees_intervenants/ — les comptages médiatiques

Cinq fichiers du 31 juillet : cartographies des intervenants sur les chaînes mainstream (LCI, BFMTV, CNews, Europe 1), comptages pro-ukrainiens/pro-russes/pro-israéliens, temps de parole. Ce sont les données brutes de l'asymétrie documentée dans l'article (le fait qu'une seule voix pro-russe, Fedorova, soit visée par un arrêté) et dans les strates S9 et S33 de l'enquête.

### 06_publication/ — la trace de la publication

`fiche_publication_substack.md` : l'entrée de l'index central du blog, qui récapitule l'article publié (URL, numéro 119, thèse, verdict). Ce fichier provient de `substack-online/index.md`, la source de vérité de toutes les publications.

### 07_sources_antecedentes/ — les enquêtes antérieures citées

Deux fichiers du 15 décembre 2025 : les investigations APEX sur les sanctions européennes contre Xavier Moreau. L'article et l'enquête les utilisent comme précédent documenté de la « sanction d'État » contre une voix jugée hostile, avec la différence de passeport (Moreau, français, ne peut être expulsé ; Fedorova, russe, peut l'être). Le parallèle Moreau traverse tout le dossier (S18, S24, S27) et a été explicitement corrigé en cours d'enquête : ce sont les fichiers de référence originaux.

### 08_mnemolite/ — les données de la base de connaissances

Six mémoires extraites de Mnemolite, le moteur RAG du projet (base vectorielle), archivées intégralement avec leur index `README_MNEMOLITE.md`. Elles forment la couche de connaissances préexistantes que l'enquête de juillet 2026 a mobilisées :

1. `01_ddcb22b_fedorova-verdict-forensique.md` : le verdict forensique du dossier, sauvegardé la veille de la publication (l'OQTF sans faits cités, le refus français de la voie européenne).
2. `02_c41fa354_concentration-medias-5-milliardaires.md` : la concentration des médias français (5 milliardaires > 75 % des audiences), le contexte où l'étiquette « ingérence » devient instrumentale.
3. `03_e74794cd_catalogue-opposition-controlee.md` : le catalogue des 10 figures d'opposition contrôlée, Fourest en position 4 (financement par le gaz russe).
4. `04_6bbdf5a7_opposition-controlee-iceberg-max.md` : la matrice élargie, 27 faits, 38 acteurs, intégrant 15 articles Substack.
5. `05_cfeaa04c_fourest-iceberg-max.md` : l'investigation ICEBERG MAX sur Fourest (nov. 2025) : le paradoxe Křetínský, ses condamnations et exclusions documentées.
6. `06_e9e46462_fourest-apex-infiltration-russe.md` : la déconstruction rhétorique du discours de Fourest sur l'« infiltration russe » (faux dilemme, urgence théâtrale, synecdoque).

**Note de méthode :** l'export automatique de la base échoue sur une erreur de validation de schéma du serveur ; les mémoires ont donc été lues une à une et copiées verbatim. C'est pourquoi ce dossier ne contient que les 6 mémoires pertinentes, et non la base entière.

### 09_git/ — la chronologie des commits

L'historique Git du dossier, en deux volets : `HISTORIQUE_COMMITS.md` (récit chronologique complet) et les messages intégraux des trois commits clés. Quatre commits portent le dossier :

| Commit | Date | Rôle |
|--------|------|------|
| `5162a867` | 30 juil. 2026, 20h03 | Le commit fondateur : les 35 strates, les 3 articles, la synthèse terminale, les cartographies d'intervenants |
| `2ff5a9a8` | 30 juil. 2026, 23h08 | La correction post-audit : première version corrigée + `Audit_critique_article_Fedorova.md` + corrections de deux quintessences (V192, V218) |
| `6458d32f` | 2 août 2026, 09h37 | La version finale : l'article « (9) » au titre définitif, les audits 2 et 3 (908 et 889 lignes), l'entrée #119 de l'index Substack |
| `3417673c` | 29 mai 2026 | L'archivage des sources Moreau (déplacement vers `archive/legacy-outputs/logs/`) |

**Ce que Git apporte en plus du dossier :** les états validés du travail, preuve de l'ordre réel (enquête → audit → correction → validation), et la possibilité de retrouver l'état exact du dossier à n'importe quelle date via `git show <hash>:<chemin>`. L'écart entre `2ff5a9a8` et `6458d32f` recouvre les itérations 4 à 9 de l'article, qui n'ont pas fait l'objet de commits séparés : les versions intermédiaires figurent dans `01_brouillons_audits/`.

---

## Fiche signalétique du dossier

- **Objet :** l'arrêté d'expulsion (29 juillet 2026) et le gel des avoirs (31 juillet 2026) de Xenia Fedorova, ancienne directrice de RT France, chroniqueuse CNews/Europe 1.
- **Méthode :** enquête forensique à 35 strates, chacune sourcée, soumise à audit contradictoire, sans thèse préconçue (ni « victime » ni « menace »).
- **Thèse de l'article :** l'État n'a pas rendu publique la chaîne de preuve qui transforme une parole contestable en ingérence étrangère ; la qualification n'est pas sa propre preuve.
- **Verbatim clé (Barrot, 29 mai 2026) :** « on peut mentir sans finir au goulag ».
- **Verdict :** tyrannie procédurale, la frontière et le système financier comme instruments de silence.
- **Limites assumées :** l'arrêté intégral n'est pas public ; le dossier de la DGSI n'est pas consultable ; le secret-défense s'impose au juge administratif comme aux journalistes.

---

## Note de méthode sur ce dossier

Ce dossier est une archive de travail, pas un ouvrage lissé. Vous y verrez des corrections, des contradictions assumées et des audits qui démolisent. C'est voulu : la fiabilité du texte publié repose précisément sur ce va-et-vient entre affirmation et contestation. Le passage de la strate 18 (parallèle Moreau) à la strate 27 (correction du parallèle Moreau) en est l'exemple le plus net : l'enquête s'est corrigée elle-même, et l'article publié intègre cette correction.
