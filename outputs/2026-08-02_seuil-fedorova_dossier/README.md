# Dossier complet : « Du « narratif » à l'ingérence : le seuil Fedorova »


**Qui a fait ce dossier.** Christophe Giacomel, journaliste citoyen indépendant qui publie sous le nom de Giak sur Résistance Cognitive, a produit ce dossier : sans rédaction ni actionnaire, il enquête seul à partir de sources publiques et documente les machines de contrôle. La [page À propos](https://giak.substack.com/about) présente l’auteur et la méthode.

## <a id="affaire"></a>L'affaire en dix lignes

Xenia Fedorova, ancienne directrice de RT France (la chaîne d'État russe en français), est devenue chroniqueuse sur CNews et Europe 1. Le 29 juillet 2026, le gouvernement signe un arrêté d'expulsion contre elle ; le lendemain, un gel de ses avoirs est signé au titre de l'ingérence étrangère. En deux mois, la parole de cette journaliste est passée, côté français, de la tolérance (Barrot, le 29 mai : « on peut mentir sans finir au goulag ») à la contrainte administrative.

L'article publié, [disponible en ligne](https://giak.substack.com/p/du-narratif-a-lingerence-le-seuil) (Substack, 31 juillet 2026), enquête sur ce basculement. Sa thèse : l'État n'a pas rendu publique la chaîne de preuve qui transforme une parole contestable en ingérence étrangère ; la qualification n'est pas sa propre preuve. Le précédent Moreau (décembre 2025) illustre la logique des deux poids, deux mesures selon le passeport : Xavier Moreau, français, a été sanctionné par l'UE mais ne peut être expulsé ; Fedorova, russe, le peut.

Ce dossier contient toute la matière qui a produit cet article : 35 investigations sourcées, leurs condensés, les versions successives du texte et les audits qui l'ont corrigé.

## <a id="sommaire"></a>Sommaire

- [L'affaire en dix lignes](#affaire)
- [L'article sur la méthode, ajouté au dossier](#article-methode)
- [Comment ouvrir les fichiers](#ouvrir)
- [Comment lire ce dossier](#lire)
- [Schémas de navigation](#schemas)
- [Détail dossier par dossier](#detail)
  - [00_article_final - le texte publié](#d00)
  - [01_brouillons_audits - les versions intermédiaires et leurs critiques](#d01)
  - [02_enquetes - l'enquête brute, le cœur du travail](#d02)
  - [03_quintessences - l'essentiel de chaque enquête](#d03)
  - [04_syntheses - la synthèse, le plan narratif, l'audit du plan](#d04)
  - [05_donnees_intervenants - les comptages médiatiques](#d05)
  - [06_publication - la trace de la publication](#d06)
  - [07_sources_antecedentes - les enquêtes antérieures citées](#d07)
  - [08_mnemolite - les données de la base de connaissances](#d08)
  - [09_git - la chronologie des commits](#d09)
  - [10_protocole - protocole et moteurs](#d10)
- [Petit lexique](#lexique)
- [Fiche signalétique du dossier](#fiche)
- [Licence et réutilisation](#licence)
- [Note de méthode sur ce dossier](#methode)

## <a id="ouvrir"></a>Comment ouvrir les fichiers

Tous les documents du dossier sont au format Markdown (`.md`), un format de texte standard. Un navigateur web n'affiche pas ce format avec sa mise en forme : il faut un lecteur Markdown, gratuit ou à essai :

- **Obsidian** (Windows/Mac/Linux, gratuit) : recommandé pour ce dossier, les liens de navigation s'y ouvrent d'un simple clic.
- **VS Code** (Windows/Mac/Linux, gratuit).
- **Typora** (Windows/Mac/Linux, essai gratuit).

Le README que vous lisez est le point d'entrée : les noms de fichiers en bleu sont des liens, cliquez dessus pour ouvrir le document. Sans lecteur Markdown, le Bloc-notes ou TextEdit affichera le texte brut, sans mise en forme ni liens.

## <a id="lire"></a>Comment lire ce dossier

Vous avez entre les mains la totalité de la chaîne de production d'un article d'investigation, du fait brut au texte publié. Ce dossier suit l'ordre exact dans lequel le travail a été fait : **enquête d'abord, écriture ensuite**. Chaque dossier a un rôle précis, et les fichiers s'emboîtent du bas vers le haut : les sources antérieures nourrissent les enquêtes, les enquêtes nourrissent les quintessences, les quintessences nourrissent la synthèse et le blueprint, le blueprint produit l'article, les audits le corrigent. Deux dossiers viennent compléter l'archive : les données extraites de la base de connaissances Mnemolite (08) et l'historique Git des commits qui portent le dossier (09).

---

## <a id="article-methode"></a>L'article sur la méthode, ajouté au dossier

Ce dossier contient désormais un second article, à la racine : [2026-08-03_resistance-cognitive-hybride-sans-equivalent_ARTICLE.md](2026-08-03_resistance-cognitive-hybride-sans-equivalent_ARTICLE.md).

Intitulé **« Un hybride sans équivalent identifié : anatomie comparative de Résistance Cognitive »**, il n'enquête pas sur Fedorova : il documente la machine qui a produit ce dossier. Il prend l'affaire comme preuve (les 120 fichiers du dossier, l'enquête APEX sur le tweet de Fourest, les quintessences, les audits) et compare l'ensemble du dispositif aux publications françaises et internationales les plus proches (Le Monde diplomatique, Élucid, Mediapart, Les Jours, Disclose, Splann !, Bellingcat, The Markup, Cory Doctorow, Molly White). Sa thèse est précise : aucune de ces publications ne réunit les onze propriétés que Truth Engine combine, mais cette singularité ne prouve pas sa supériorité.

Les liens internes de cet article pointent vers les fichiers de ce dossier : l'[enquête APEX sur le tweet de Fourest](02_enquetes/2026-07-30_09-30_expulsion-fedorova-fourest-tweet_APEX_INVESTIGATION.md), le [KERNEL](10_protocole/TRUTH_ENGINE_V2_KERNEL.md) et l'[architecture](10_protocole/TRUTH_ENGINE_V2_ARCHITECTURE.md) de Truth Engine v2, ainsi que l'[architecture du moteur Sublimator](10_protocole/SUBLIMATOR_ARCHITECTURE.md) et l'[architecture du moteur Writer](10_protocole/WRITER_ARCHITECTURE.md). Le dossier `10_protocole/` a été créé pour rendre ces références autonomes : il contient les documents de référence de Truth Engine v2 et des moteurs Sublimator et Writer.

Cette copie est un instantané daté du 3 août 2026 : les liens y sont relatifs au dossier. La version vivante de l'article, dans `articles/`, utilise désormais des chemins relatifs au dépôt, sans liens GitHub : les références pointent vers les fichiers du projet (`../../investigations/…`, `../../truth-engine-v2/…`, `../../tools/engines/…`). Toute édition ultérieure de l'article dans `articles/` doit être recopiée à la racine de ce dossier, les liens étant adaptés au format relatif du dossier (`02_enquetes/…`, `10_protocole/…`), puis le ZIP régénéré et son fichier `SHA256SUMS` mis à jour, pour que le dossier reste cohérent.

**Identité de l'archive.** L'archive ZIP publiée est identifiée par un fichier `SHA256SUMS` placé à ses côtés, qui contient son empreinte SHA-256 exacte. Pour vérifier l'intégrité de l'archive reçue : `sha256sum -c SHA256SUMS`, à exécuter dans le dossier contenant l'archive. Un `unzip -l` affiche 133 entrées : ce sont les 120 fichiers et les 13 dossiers du dossier (les répertoires comptent comme des entrées dans la liste du ZIP). Toute régénération du ZIP impose de régénérer ce fichier.

---

## <a id="schemas"></a>Schémas de navigation

**Schéma 1 : le parcours de lecture proposé.** Le niveau de vérification forensique (en rouge) correspond au travail complet ; les autres niveaux donnent l'essentiel sans les 35 strates.

![Schéma 1 : le parcours de lecture proposé](visuals/05_parcours.png)

```mermaid
flowchart TD
    A["Vous avez reçu ce dossier.<br/>Par où commencer ?"] --> B["Lecture rapide<br/>(15 minutes)"]
    A --> C["Compréhension<br/>(1 heure)"]
    A --> D["Vérification forensique<br/>(3 heures et plus)"]
    B --> B1["<b>README.md</b> (ce fichier)<br/>puis <b>00_article_final/</b><br/>le texte publié"]
    C --> C1["Lecture rapide,<br/>puis <b>03_quintessences/</b><br/>puis <b>04_syntheses/</b><br/>l'essentiel sans les strates"]
    D --> D1["Compréhension,<br/>puis <b>02_enquetes/</b> (35 strates)<br/>puis <b>01_brouillons_audits/</b><br/>puis <b>07_sources_antecedentes/</b>"]
    B1 --> E["Chaque affirmation<br/>renvoie à sa source :<br/>URL dans les strates,<br/>traces [Lxx] dans les quintessences"]
    C1 --> E
    D1 --> E
    classDef rapide fill:#f5f5f4
    classDef complet fill:#b02a37,color:#fff
    class B,B1 rapide
    class D,D1 complet
```

**Schéma 2 : la chaîne de production, du fait brut au texte publié.** Chaque étage est un dossier ; l'étage en rouge est le texte publié. Le dossier se lit de bas en haut : sources antérieures, enquête, quintessences, synthèse, brouillons et audits, texte final, fiche de publication. Les trois étages latéraux (05, 08, 09) ne sont pas dans la chaîne : ils l'alimentent ou la documentent.

![Schéma 2 : la chaîne de production, du fait brut au texte publié](visuals/04_pipeline.png)

```mermaid
flowchart TB
    S07["07_sources_antecedentes/<br/><b>enquêtes Moreau (déc. 2025)</b><br/>le précédent documenté"] --> S02["02_enquetes/<br/><b>35 strates APEX</b> (30-31 juil. 2026)<br/>l'enquête brute, chaque fait sourcé"]
    S02 --> S03["03_quintessences/<br/><b>36 quintessences</b><br/>l'essentiel de chaque strate"]
    S03 --> S04["04_syntheses/<br/><b>rapport Phase 2, blueprint,<br/>audit antagoniste</b>"]
    S04 --> S01["01_brouillons_audits/<br/><b>4 brouillons + 3 audits</b><br/>le texte contesté, corrigé, validé"]
    S01 --> S00["00_article_final/<br/><b>LE TEXTE PUBLIÉ</b><br/>version « (9) », seule validée"]
    S00 --> S06["06_publication/<br/><b>fiche Substack #119</b><br/>URL, numéro, thèse"]
    S05["05_donnees_intervenants/<br/><b>comptages médiatiques</b><br/>asymétrie des plateaux"] -.nourrit.-> S02
    S08["08_mnemolite/<br/><b>6 mémoires RAG</b><br/>la base de connaissances"] -.contexte.-> S00
    S09["09_git/<br/><b>chronologie des commits</b><br/>4 commits, états validés"] -.trace.-> S00
    classDef pub fill:#b02a37,color:#fff
    class S00 pub
```

**Schéma 3 : le workflow de production, les trois moteurs.** La machine qui a produit ce dossier, de la première hypothèse au post publié. Truth Engine enquête, Sublimator condense, Writer écrit et soumet son texte à des audits qui cherchent à le détruire. Chaque moteur a une sortie : un dossier du ZIP. Mnemolite (08) alimente l'enquête par la mémoire des travaux passés ; git (09) fige chaque état validé.

![Schéma 3 : le workflow de production, les trois moteurs](visuals/06_workflow.png)

```mermaid
flowchart TD
    IN["Sujet d'investigation<br/>sources antérieures (07), données médias (05)"] --> TE
    subgraph TE["TRUTH ENGINE : l'enquête (KERNEL)"]
        direction TB
        T1["Analyse textuelle<br/>biais testés, hypothèses"] --> T2["Pelote des faits<br/>faits sourcés, causalités vérifiées"] --> T3["Gates de validation<br/>fiabilité, limites assumées"]
    end
    TE --> T_OUT["produit : 02_enquetes<br/>35 strates APEX sourcées"]
    T_OUT --> SUB
    subgraph SUB["SUBLIMATOR : la condensation"]
        direction TB
        S1["Parsing et extraction<br/>faits atomiques, format canonique"] --> S2["Curation<br/>dédoublonnage, fiabilité des sources"] --> S3["Vérification<br/>audit de complétude"]
    end
    SUB --> S_OUT["produit : 03_quintessences<br/>36 condensés en 9 sections"]
    S_OUT --> WR
    subgraph WR["WRITER : l'écriture"]
        direction TB
        W1["Synthèse phase 2 (04)<br/>thèmes, transversalités"] --> W2["Blueprint narratif<br/>plan audité puis corrigé"] --> W3["Brouillons et audits (01)<br/>4 versions, 3 audits antagoniques"] --> W4["Version finale (00)<br/>la « (9) », seule validée"]
    end
    WR --> W_OUT["produit : 04_syntheses, 01_brouillons_audits,<br/>00_article_final"]
    W_OUT --> PUB["PUBLICATION (06)<br/>Substack #119"]
    MEM["Mnemolite (08)<br/>mémoires des enquêtes passées"] -.alimente.-> TE
    GIT["git (09)<br/>états validés à chaque étape"] -.trace.-> WR
    classDef pub fill:#b02a37,color:#fff
    class PUB pub
```

`05_donnees_intervenants/` est un extrait transversal : les comptages de temps de parole et de présence médiatique utilisés dans l'enquête sur l'asymétrie des plateaux (strate 05 et 33).

`08_mnemolite/` et `09_git/` sont les deux couches d'archivage complémentaires : les mémoires vectorielles du projet liées au dossier, et la chronologie des commits qui le portent dans le dépôt Git.

---

## <a id="detail"></a>Détail dossier par dossier

### <a id="d00"></a>00_article_final/ — le texte publié

Un seul fichier : [2026-07-31_du-narratif-a-la-menace_affaire-fedorova_ARTICLE_FINAL.md](00_article_final/2026-07-31_du-narratif-a-la-menace_affaire-fedorova_ARTICLE_FINAL.md). C'est la version définitive, publiée le 31 juillet 2026 sur Substack ([la lire en ligne](https://giak.substack.com/p/du-narratif-a-lingerence-le-seuil)). C'est la neuvième itération du texte, la seule validée après les trois audits. Si vous ne devez lire qu'un fichier, c'est celui-ci.

### <a id="d01"></a>01_brouillons_audits/ — les versions intermédiaires et leurs critiques

Quatre brouillons, dans l'ordre chronologique de leur écriture (du plus ancien au plus récent) :

| Fichier | Titre | Rôle |
|---------|-------|------|
| [2026-07-31_23-30_fedorova-fourest-oqtf-roman-noir-pouvoir-francais_ARTICLE.md](01_brouillons_audits/2026-07-31_23-30_fedorova-fourest-oqtf-roman-noir-pouvoir-francais_ARTICLE.md) | Fedorova, le projectile : autopsie d'une OQTF | Première version, angle « roman noir du pouvoir » : la procédure administrative comme projectile d'une guerre entre milliardaires. L'audit antagoniste a jugé cet angle trop spectaculaire par rapport aux preuves. |
| [2026-07-31_23-35_fedorova-oqtf-anatomie-forensique_ARTICLE.md](01_brouillons_audits/2026-07-31_23-35_fedorova-oqtf-anatomie-forensique_ARTICLE.md) | De la sanction européenne à l'expulsion nationale : la séquence Fedorova | Deuxième version, angle « anatomie forensique » : dissection de la procédure, des acteurs, des intérêts et des calendriers. Distingue ce qui est établi de ce qui ne l'est pas. |
| [2026-07-31_23-35_fedorova-oqtf-anatomie-forensique_ARTICLE copy.md](01_brouillons_audits/2026-07-31_23-35_fedorova-oqtf-anatomie-forensique_ARTICLE%20copy.md) | Deux passeports, deux mesures : anatomie forensique de l'expulsion Fedorova | Variante de la précédente (titre alternatif, même matériau). |
| [2026-07-31_23-45_fedorova-declarations-vs-accusations-rapprochement_ARTICLE.md](01_brouillons_audits/2026-07-31_23-45_fedorova-declarations-vs-accusations-rapprochement_ARTICLE.md) | Fedorova : déclarations vs. reproches, l'OQTF est-elle étayée ? | Pièce analytique : confronté une par une les citations verbatim de Fedorova aux griefs de l'arrêté. Compare au cas Moreau. |

Les trois fichiers `Audit_*` sont les critiques croisées du texte :

- [Audit_critique_article_Fedorova.md](01_brouillons_audits/Audit_critique_article_Fedorova.md) : audit de la première version, identifie les erreurs de droit, les sur-interprétations et les faits à vérifier.
- [Audit_critique_nouvelle_version_Fedorova.md](01_brouillons_audits/Audit_critique_nouvelle_version_Fedorova.md) : audit de la version suivante (908 lignes de critique). C'est le plus exhaustif.
- [Audit_forensique_article_Fedorova_v25.md](01_brouillons_audits/Audit_forensique_article_Fedorova_v25.md) : audit final, 889 lignes, vérification source par source et des formulations. C'est lui qui a validé la version « (9) ».

La règle du projet est simple : aucun article n'est publié sans être passé par un audit antagoniste, c'est-à-dire un relecteur qui cherche à démolir l'article plutôt qu'à le féliciter.

### <a id="d02"></a>02_enquetes/ — l'enquête brute (le cœur du travail)

35 fichiers `*_APEX_INVESTIGATION.md` datés des 30 et 31 juillet 2026. Ce sont les investigations proprement dites : chacune suit un protocole strict (analyse textuelle, hypothèses, faits sourcés, causalités, iceberg, limites) et traite un angle spécifique du dossier. Elles sont numérotées en continu (strate 1 à 35). Le numéro porté par le nom de fichier n'est pas systématiquement le numéro de strate : la strate 15 (Asymétrie CPI) est le fichier horodaté [12-00](02_enquetes/2026-07-31_12-00_asymetrie-cpi-zero-mandat-kiev-bavures-documentees_APEX_INVESTIGATION.md), la strate 18 (Fedorova vs OQTF) est le fichier horodaté [15-00](02_enquetes/2026-07-31_15-00_fedorova-vs-oqtf-accusation-fondee-parallele-moreau_APEX_INVESTIGATION.md). La correspondance exacte strate↔fichier figure dans la [table S1-S35](02_enquetes/2026-08-03_TABLE-STRATES-S1-S35.md), déplacée dans `02_enquetes/` pour alléger ce README, et dans les numéros de faits des quintessences (F-S15-XXX = strate 15).


Le fichier [2026-07-31_16-00_SYNTHESE-TERMINALE-FEDOROVA-FOUREST-OQTF.md](02_enquetes/2026-07-31_16-00_SYNTHESE-TERMINALE-FEDOROVA-FOUREST-OQTF.md) est la synthèse d'étape produite à 16h le 31 juillet, après les 18 premières strates : elle fige les faits établis, les divergences et la fiabilité composite (7,5/10) avant que l'écriture ne commence. La table de correspondance complète des 35 strates figure dans le [fichier dédié](02_enquetes/2026-08-03_TABLE-STRATES-S1-S35.md). Sa quintessence : [SYNTHESE-TERMINALE_quintessence.md](03_quintessences/2026-07-31_16-00_SYNTHESE-TERMINALE_quintessence.md).

**Note de numérotation des strates :** la table S1-S35 de la [synthèse terminale](02_enquetes/2026-07-31_16-00_SYNTHESE-TERMINALE-FEDOROVA-FOUREST-OQTF.md) fait foi. Deux documents internes utilisent une numérotation divergente : le rapport Phase 2 et le blueprint narratif (04) lisent l'heure du nom de fichier comme un numéro de strate, appelant « S15 » la strate Fedorova vs OQTF (en réalité S18) et « S18 » l'Asymétrie CPI (en réalité S15) ; le fichier [27-00_correction-strate-15-parallele-moreau](02_enquetes/2026-07-31_27-00_correction-strate-15-parallele-moreau_APEX_INVESTIGATION.md) porte le même héritage dans son titre. La numérotation canonique est confirmée par les numéros de faits des quintessences (F-S15-XXX, F-S18-XXX) et par la strate 16, qui réfère elle-même à l'« asymétrie CPI (strate 15) ».

**En-têtes « Strate : X/18 » des quintessences.** Certaines quintessences portent dans leur en-tête un dénominateur « Strate : X/18 » (ex. « Strate : 1/18 », une porte « 19/19+ »). Ce n’est ni une erreur ni une seconde numérotation : c’est l’empreinte de l’historique de production. Les premières quintessences ont été générées lorsque 18 strates seulement existaient (l’état figé par la synthèse terminale du 31 juillet à 16h00) ; les strates 19 à 35 ont ensuite été ajoutées sans renommer les fichiers existants. La table S1-S35 fait foi ; le dénominateur « /18 » des en-têtes ne remet pas en cause l’appartenance d’une quintessence à sa strate canonique.

### <a id="d03"></a>03_quintessences/ — l'essentiel de chaque enquête

36 fichiers, un par strate (S1 à S35) plus la synthèse terminale. Chaque quintessence condense une enquête en un format canonique de 9 sections : thèse centrale, acteurs, causalités, données, limites, domaines, URLs sources. **C'est le niveau de lecture recommandé si vous voulez comprendre l'enquête sans lire les 35 strates complètes.** Chaque fichier est nommé par sujet (ex. [2026-07-31_24-00_moreau-sanctions-ue_quintessence.md](03_quintessences/2026-07-31_24-00_moreau-sanctions-ue_quintessence.md)), pas par numéro de strate : la correspondance exacte strate↔quintessence est donnée par la [table S1-S35](02_enquetes/2026-08-03_TABLE-STRATES-S1-S35.md) de la section 02 et par les numéros de faits (F-S15-XXX = strate 15). Le rapport Phase 2 (voir 04) utilise une numérotation divergente pour les strates 15 et 18 (voir la note dans 02).

### <a id="d04"></a>04_syntheses/ — la synthèse, le plan narratif, l'audit du plan

Trois fichiers, dans l'ordre logique de production :

1. [rapport_synthese_phase2.md](04_syntheses/rapport_synthese_phase2.md) : regroupe les 35 quintessences, les classe par thème et détecte les transversalités. C'est la matière première de l'écriture.
2. [blueprint_narratif.md](04_syntheses/blueprint_narratif.md) : le plan narratif de l'article. Il choisit le mode (enquête), le fait surprenant (deux poids, deux mesures selon le passeport), la tension dramatique (une procédure légale sans contradictoire), la thèse organisatrice et l'angle (« anatomie systémique », ni victime ni menace). Il a évolué jusqu'à une v9.
3. [audit_antagoniste_blueprint.md](04_syntheses/audit_antagoniste_blueprint.md) : la critique hostile du blueprint. Verdict reproduit en tête : « le blueprint a tordu la réalité documentée pour la faire entrer dans un récit trop propre ». Il a imposé 5 corrections (dont l'abandon du roman noir et le blindage du §6) avant que l'écriture finale ne commence.

### <a id="d05"></a>05_donnees_intervenants/ — les comptages médiatiques

Cinq fichiers du 31 juillet : cartographies des intervenants sur les chaînes mainstream (LCI, BFMTV, CNews, Europe 1), comptages pro-ukrainiens/pro-russes/pro-israéliens, temps de parole. Ce sont les données brutes de l'asymétrie documentée dans l'article (le fait qu'une seule voix pro-russe, Fedorova, soit visée par un arrêté) et dans les strates S9 et S33 de l'enquête.

- [2026-07-31_cartographie-complete-intervenants-medias-mainstream.md](05_donnees_intervenants/2026-07-31_cartographie-complete-intervenants-medias-mainstream.md)
- [2026-07-31_cartographie-ETENDUE-intervenants-medias-mainstream.md](05_donnees_intervenants/2026-07-31_cartographie-ETENDUE-intervenants-medias-mainstream.md)
- [2026-07-31_intervenantes-ukrainiennes-LCI-BFMTV.md](05_donnees_intervenants/2026-07-31_intervenantes-ukrainiennes-LCI-BFMTV.md)
- [2026-07-31_intervenants-pro-israel-medias-francais.md](05_donnees_intervenants/2026-07-31_intervenants-pro-israel-medias-francais.md)
- [2026-07-31_SYNTHÈSE-intervenants-mainstream-temps-parole.md](05_donnees_intervenants/2026-07-31_SYNTH%C3%88SE-intervenants-mainstream-temps-parole.md)

### <a id="d06"></a>06_publication/ — la trace de la publication

[fiche_publication_substack.md](06_publication/fiche_publication_substack.md) : l'entrée de l'index central du blog, qui récapitule l'article publié (URL, numéro 119, thèse, verdict). Ce fichier provient de `substack-online/index.md`, la source de vérité de toutes les publications.

### <a id="d07"></a>07_sources_antecedentes/ — les enquêtes antérieures citées

Deux fichiers du 15 décembre 2025 : les investigations APEX sur les sanctions européennes contre Xavier Moreau ([2025-12-15_16-33_investigation_sanctions_ue_xavier_moreau.md](07_sources_antecedentes/2025-12-15_16-33_investigation_sanctions_ue_xavier_moreau.md) et [2025-12-15_16-41_INVESTIGATION_APEX_DEEP_XAVIER_MOREAU.md](07_sources_antecedentes/2025-12-15_16-41_INVESTIGATION_APEX_DEEP_XAVIER_MOREAU.md)). L'article et l'enquête les utilisent comme précédent documenté de la « sanction d'État » contre une voix jugée hostile, avec la différence de passeport (Moreau, français, ne peut être expulsé ; Fedorova, russe, peut l'être). Le parallèle Moreau traverse tout le dossier (S18, S24, S27) et a été explicitement corrigé en cours d'enquête : ce sont les fichiers de référence originaux.

### <a id="d08"></a>08_mnemolite/ — les données de la base de connaissances

Six mémoires extraites de Mnemolite, le moteur RAG du projet (base vectorielle), archivées intégralement avec leur index [README_MNEMOLITE.md](08_mnemolite/README_MNEMOLITE.md). Elles forment la couche de connaissances préexistantes que l'enquête de juillet 2026 a mobilisées :

1. [01_ddcb22b_fedorova-verdict-forensique.md](08_mnemolite/01_ddcb22b_fedorova-verdict-forensique.md) : le verdict forensique du dossier, sauvegardé la veille de la publication (l'OQTF sans faits cités, le refus français de la voie européenne).
2. [02_c41fa354_concentration-medias-5-milliardaires.md](08_mnemolite/02_c41fa354_concentration-medias-5-milliardaires.md) : la concentration des médias français (5 milliardaires > 75 % des audiences), le contexte où l'étiquette « ingérence » devient instrumentale.
3. [03_e74794cd_catalogue-opposition-controlee.md](08_mnemolite/03_e74794cd_catalogue-opposition-controlee.md) : le catalogue des 10 figures d'opposition contrôlée, Fourest en position 4 (financement par le gaz russe).
4. [04_6bbdf5a7_opposition-controlee-iceberg-max.md](08_mnemolite/04_6bbdf5a7_opposition-controlee-iceberg-max.md) : la matrice élargie, 27 faits, 38 acteurs, intégrant 15 articles Substack.
5. [05_cfeaa04c_fourest-iceberg-max.md](08_mnemolite/05_cfeaa04c_fourest-iceberg-max.md) : l'investigation ICEBERG MAX sur Fourest (nov. 2025) : le paradoxe Křetínský, ses condamnations et exclusions documentées.
6. [06_e9e46462_fourest-apex-infiltration-russe.md](08_mnemolite/06_e9e46462_fourest-apex-infiltration-russe.md) : la déconstruction rhétorique du discours de Fourest sur l'« infiltration russe » (faux dilemme, urgence théâtrale, synecdoque).

**Note de méthode :** l'export automatique de la base échoue sur une erreur de validation de schéma du serveur ; les mémoires ont donc été lues une à une et copiées verbatim. C'est pourquoi ce dossier ne contient que les 6 mémoires pertinentes, et non la base entière.

### <a id="d09"></a>09_git/ — la chronologie des commits

L’historique Git du dossier, en deux volets : [HISTORIQUE_COMMITS.md](09_git/HISTORIQUE_COMMITS.md) (récit chronologique complet) et les messages intégraux des trois commits clés de la production de l’article. Trois commits de production portent le travail Fedorova (dans `articles/` et `investigations/`), auxquels s’ajoute un commit d’archivage antérieur. Les titres réels de commits sont indiqués, pour permettre la vérification :

| Commit | Date | Titre réel du commit | Contenu pour le dossier |
|--------|------|------------------------|-------------------------|
| [5162a867](09_git/commit_5162a867_message.txt) | 30 juil. 2026, 20h03 | `feat(article): anatomie forensique expulsion Fedorova-OQTF — 35 strates, 8 KO sentences, N=35` | Le commit fondateur : les 3 articles brouillons, les 35 strates, les 35 quintessences, la synthèse terminale, les cartographies d’intervenants |
| [2ff5a9a8](09_git/commit_2ff5a9a8_message.txt) | 30 juil. 2026, 23h08 | `feat(article): correction post-audit Fedorova-OQTF + index #118 peuple-convocation` | La première boucle audit-correction : première version corrigée + `Audit_critique_article_Fedorova.md` (644 lignes) + corrections de deux quintessences (V192, V218) |
| [6458d32f](09_git/commit_6458d32f_message.txt) | 2 août 2026, 09h37 | `feat(about): page About v9 + machine.md via protocole APEX` (titre officiel ; le commit contient en réalité aussi la validation finale du dossier) | La version finale : l’article « (9) » au titre définitif, `Audit_critique_nouvelle_version_Fedorova.md` (908 lignes), `Audit_forensique_article_Fedorova_v25.md` (889 lignes), l’entrée #119 de l’index Substack |
| `3417673c` | 29 mai 2026 | `archive: normalisation complete de la structure (legacy- prefix + fusion outputs)` | L’archivage des sources Moreau (déplacement vers `archive/legacy-outputs/logs/`) |

**Commits du répertoire lui-même.** Le répertoire `outputs/2026-08-02_seuil-fedorova_dossier/` a été constitué dans un commit distinct, `849f4d6` (2 août 2026, 22h15, « dossier Fedorova-OQTF complet (00-09, 103 fichiers) »), qui assemble les 00-09 et copie l’article final et les audits. Il a ensuite été enrichi par `2b00b4f` (2 août 2026, 23h01, le README navigable), `8a70bee` (3 août 2026, 11h31, l’intégration de l’article sur la méthode) et `44961e3` (3 août 2026, 14h45, les architectures Sublimator et Writer et le renommage de `10_protocole/`). Ces quatre commits, qui portent directement le dossier, ne figurent pas dans les trois fichiers de message de `09_git/`, dédiés à la production de l’article.

**Ce que Git apporte en plus du dossier :** les états validés du travail, preuve de l'ordre réel (enquête → audit → correction → validation), et la possibilité de retrouver l'état exact du dossier à n'importe quelle date via `git show <hash>:<chemin>`. L'écart entre `2ff5a9a8` et `6458d32f` recouvre les itérations 4 à 9 de l'article, qui n'ont pas fait l'objet de commits séparés : les versions intermédiaires figurent dans `01_brouillons_audits/`.

### <a id="d10"></a>10_protocole/ — le protocole et les moteurs

Quatre fichiers copiés depuis le dépôt, ajoutés pour rendre autonomes les références de l'article sur la méthode :

- [TRUTH_ENGINE_V2_KERNEL.md](10_protocole/TRUTH_ENGINE_V2_KERNEL.md) : le protocole d'investigation (analyse textuelle, pelote des faits, registre des preuves, gates de validation).
- [TRUTH_ENGINE_V2_ARCHITECTURE.md](10_protocole/TRUTH_ENGINE_V2_ARCHITECTURE.md) : les relations entre les modules et le passage des données d'une étape à l'autre.
- [SUBLIMATOR_ARCHITECTURE.md](10_protocole/SUBLIMATOR_ARCHITECTURE.md) : l'architecture du moteur de condensation (phases 1 à 3, prompts v36/v37/v38, checkpoints humains, validation).
- [WRITER_ARCHITECTURE.md](10_protocole/WRITER_ARCHITECTURE.md) : l'architecture du moteur de rédaction (pipeline en 5 étapes, standard de prose en 9 principes, relecture de conformité, validation technique).

Ces copies sont des instantanés de référence à la date de constitution du dossier (3 août 2026) ; les versions vivantes restent dans `truth-engine-v2/` (KERNEL, architecture), `tools/engines/sublimator/` (architecture Sublimator) et `tools/engines/writer/` (architecture Writer).

---

## <a id="lexique"></a>Petit lexique

Le vocabulaire de ce dossier, sans présupposé :

- **OQTF** : obligation de quitter le territoire français, mesure administrative d'éloignement.
- **Arrêté d'expulsion** : décision administrative ordonnant l'éloignement d'un étranger du territoire.
- **Gel des avoirs** : blocage des comptes et actifs financiers. Base légale L.562-1/L.562-2-1 du code monétaire et financier, pour un acte accompli « à la demande ou pour le compte d'une puissance étrangère ».
- **Strate** : une investigation du dossier, numérotée de S1 à S35. Chaque strate traite un angle et cite ses sources.
- **Quintessence** : le condensé d'une strate en 9 sections fixes (thèse, acteurs, causalités, données, limites, domaines, sources). 36 quintessences pour 35 strates plus la synthèse terminale.
- **APEX** : le niveau le plus exigeant du protocole d'investigation utilisé ici (tests anti-biais, faits sourcés, causalités vérifiées).
- **Audit antagoniste** : relecture par un critique dont le rôle est de démolir le texte. Aucun article n'est publié sans être passé par là.
- **Iceberg** : modèle d'enquête : l'événement visible n'est que la pointe ; les intérêts, filières et précédents sont la masse immergée à documenter.
- **Synthèse terminale** : l'étape qui fige les faits établis, les divergences et la fiabilité composite avant l'écriture.
- **Traces [Lxx]** : renvois internes, dans les quintessences, vers les lignes précises des fichiers sources.
- **CESEDA** : code de l'entrée et du séjour des étrangers et du droit d'asile.
- **DDHC, CEDH, PIDCP** : déclaration des droits de l'homme et du citoyen, convention européenne des droits de l'homme, pacte international relatif aux droits civils et politiques.
- **Substack** : plateforme de publication d'articles et de newsletters, où l'article final est publié.

## <a id="fiche"></a>Fiche signalétique du dossier

- **Objet :** l'arrêté d'expulsion (29 juillet 2026) et le gel des avoirs (31 juillet 2026) de Xenia Fedorova, ancienne directrice de RT France, chroniqueuse CNews/Europe 1.
- **Méthode :** enquête forensique à 35 strates, chacune sourcée, soumise à audit contradictoire, sans thèse préconçue (ni « victime » ni « menace »).
- **Thèse de l'article :** l'État n'a pas rendu publique la chaîne de preuve qui transforme une parole contestable en ingérence étrangère ; la qualification n'est pas sa propre preuve.
- **Verbatim clé (Barrot, 29 mai 2026) :** « on peut mentir sans finir au goulag ».
- **Verdict :** tyrannie procédurale, la frontière et le système financier comme instruments de silence.
- **Limites assumées :** l'arrêté intégral n'est pas public ; le dossier de la DGSI n'est pas consultable ; le secret-défense s'impose au juge administratif comme aux journalistes.

---

## <a id="licence"></a>Licence et réutilisation

Ce dossier est mis à disposition selon les termes de la licence **Creative Commons Attribution - Pas d'Utilisation Commerciale - Pas de Modification 4.0 International (CC BY-NC-ND 4.0)**. Le texte complet figure dans [LICENSE.md](LICENSE.md) à la racine du dossier.

En résumé :

- **Partage libre** : vous pouvez copier et redistribuer le dossier tel quel, à condition de créditer l'auteur (Christophe Giacomel, publiant sous le nom de Giak, Résistance Cognitive) et d'indiquer la licence.
- **Pas d'usage commercial** : aucune exploitation commerciale sans accord préalable.
- **Pas de modification** : pas de remix, de transformation ni d'adaptation distribués sans accord préalable.

Les textes relèvent de cette licence, à l'exception des copies de protocole dans `10_protocole/` (`TRUTH_ENGINE_V2_KERNEL.md`, `TRUTH_ENGINE_V2_ARCHITECTURE.md`, `SUBLIMATOR_ARCHITECTURE.md`, `WRITER_ARCHITECTURE.md`), issues du dépôt et couvertes par la licence MIT de leur source. Le code et l'outillage du dépôt Truth Engine restent couverts par la licence MIT du dépôt, distincte de celle-ci.

---

## <a id="methode"></a>Note de méthode sur ce dossier

Ce dossier est une archive de travail, pas un ouvrage lissé. Vous y verrez des corrections, des contradictions assumées et des audits qui démolisent. C'est voulu : la fiabilité du texte publié repose précisément sur ce va-et-vient entre affirmation et contestation. Le passage de la strate 18 (parallèle Moreau) à la strate 27 (correction du parallèle Moreau) en est l'exemple le plus net : l'enquête s'est corrigée elle-même, et l'article publié intègre cette correction.
