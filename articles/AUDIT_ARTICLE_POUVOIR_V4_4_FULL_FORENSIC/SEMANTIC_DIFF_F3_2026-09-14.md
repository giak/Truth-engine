# SEMANTIC_DIFF, tranche F3, entrées de registre pour les investigations nommées

Objet : `01_TARGET/ARTICLE_MASTERWORK_SOUVERAINETE_2026.md`.
Empreinte avant : `c1165fd10e0f951daab72f1e4f1ee72c9b709e121e7046acf2fa7bcfab8afc82` (état après F2).
Empreinte après : **`8d0d526d70f6291382020f5b355eabda52430183640ea38c2de348548fd529b4`**.
Sauvegarde : `/tmp/ARTICLE_MASTERWORK_AVANT_F2.md` (état d’avant F2 ; l’état d’avant F3 est reproductible par l’empreinte `c1165fd1`).

**Une correction de comptage, à la charge de cette trace.** La première rédaction annonçait « 309 → 313 lignes », ce qui était faux d’une unité : elle comptait les segments d’un découpage sur le saut de ligne, qui ajoute un segment vide terminal, là où F1 et F2 comptaient les lignes du fichier (`wc -l`, convention retenue dans tout le dossier). Le compte réel est **308 → 312** : quatre lignes ajoutées, six modifiées. Aucun octet ni aucune empreinte n’est affecté.

Demande : ajouter au registre **une entrée par investigation nommée**, avec ses sources primaires, pour que le lecteur puisse contrôler. F2 avait nommé six investigations sans leur donner de référence ; F3 leur en donne, là où c’est possible.

**Six lignes modifiées, quatre ajoutées** : 66, 67, 113, 128, 181, 215 modifiées ; [65] à [68] ajoutées en fin de registre. 308 → 312 lignes. 46 157 → 48 245 octets.

---

## 1. Ce que le travail de sourçage a produit, et qui n’était pas demandé

La demande supposait que les six investigations pouvaient être sourcées. **Quatre le pouvaient, deux non**, et une septième chose est apparue en chemin : **un chiffre en gras de l’article n’existe pas dans l’investigation qui est censée le porter.** Les trois constats sont dans cette trace.

---

## 2. Les quatre entrées ajoutées

Chaque entrée nomme l’enquête, donne son état vérifiable, puis ses sources. **Aucune URL n’a été composée** : toutes proviennent des tables de sources des investigations elles-mêmes, et leur résolution a été testée le 14 septembre 2026.

### [65] · Enquête « Abu Dhabi Secrets » (INV‑033)

> Enquête « Abu Dhabi Secrets » : opérations d’influence des Émirats arabes unis en Europe conduites par un cabinet privé de renseignement établi à Genève. Mediapart, 4 mars 2023 ; réponse écrite de la Commission européenne P‑9‑2023‑002379 ; RSI, enquête fédérale suisse, 2023.

Source de l’article : l. 66, « L’investigation consacrée à l’influence clandestine et réputationnelle documente le cas où un cabinet privé de renseignement basé à Genève… ».

### [66] · Enquête « Rokh Solis » (INV‑026)

> Enquête « Rokh Solis » : opérations de manipulation de contenu ayant ciblé les élections municipales françaises de mars 2026, opérateur privé identifié, commanditaire non identifié. VIGINUM (SGDSN) ; HATVP, fiche Elnet France.

Source de l’article : l. 67. **La première source est une analyse publique de VIGINUM**, dont le titre porté par le site est « Rokh Solis : Analyse d’un mode opératoire informationnel ayant ciblé les élections municipales de mars 2026 ». C’est la pièce qui établit l’opérateur **et** l’absence de commanditaire identifié : l’entrée du registre rend donc vérifiable ce que F1 avait corrigé.

### [67] · Enquête « Front uni chinois » (INV‑025)

> Enquête « Front uni chinois » : relais de stations de police identifiés par la DGSI, station clandestine constatée par le Conseil d’État. Assemblée nationale, question écrite n° 1675, « Existence de commissariats clandestins chinois sur le territoire national », 2025 ; Conseil d’État, décision sur une station clandestine hébergée par une association du Fujian ; AIVD (Pays‑Bas), rapport annuel 2025, chapitre Chine.

Source de l’article : l. 113. **Le titre même de la question écrite emploie « commissariats clandestins chinois »** : c’est la formulation la plus proche de « stations de police clandestines », et elle est parlementaire. La réserve de F1 tient : la question porte sur **l’existence** de ces commissariats ; c’est le Conseil d’État qui a constaté **une** station hébergée par une association du Fujian.

### [68] · Enquête « cabinets de conseil dans l’État » (INV‑062)

> Enquête « cabinets de conseil dans l’État » : Sénat, rapport n° 578, session 2020‑2021, « Un phénomène tentaculaire : l’influence croissante des cabinets de conseil sur les politiques publiques ».

Source de l’article : l. 128.

### Résolution des sources, testée

| Source | Code | Titre relevé |
|---|---|---|
| `questions.assemblee-nationale.fr/q17/17-1675QE.htm` | **200** | Question n° 1675 : Existence de commissariats clandestins chinois sur le territoire national |
| `aivd.nl/.../jaarverslag/2025/china` | **200** | China, AIVD |
| `sgdsn.gouv.fr/viginum/publications/rokh-solis-...` | **200** | Rokh Solis : Analyse d’un mode opératoire informationnel… |
| `hatvp.fr/fiche-organisation/?organisation=531006237` | **200** | Fiche Elnet France |
| `mediapart.fr/en/journal/france/040323/leaked-data-...` | **200** | Leaked data shows extent of UAE’s meddling in France |
| `rsi.ch/.../Abu-Dhabi-Secrets-aperta-inchiesta-...` | **200** | Abu Dhabi Secrets, aperta inchiesta per spionaggio |
| `senat.fr/rap/r21-578-1/r21-578-111.html` | **200** | Un phénomène tentaculaire : l’influence croissante des cabinets de conseil sur les politiques publiques |
| `europarl.europa.eu/doceo/document/P-9-2023-002379-ASW_EN.html` | **202** | contenu servi, titre non extractible |
| `legifrance.gouv.fr/ceta/id/CETATEXT000054227852` | **403** | **non rendu** : protection contre les robots. L’identifiant est stable et provient du dossier |

**Deux sources ont été écartées** et ne figurent dans aucune entrée : `lemonde.fr` (402, « Accès restreint ») et `leparisien.fr` (403, « Access Denied »). Elles restent des pièces du dossier, mais une entrée de registre qui renvoie à une page inaccessible ne rend rien vérifiable.

## 3. Les deux investigations qui ne peuvent pas être sourcées

**INV‑046 (infrastructures numériques de contrôle) et INV‑063 (Big Four et production de normes) n’ont pas de sources à donner, parce que leurs livrables sont absents du dossier.**

Les deux runs sont pourtant **certifiés** :

| Investigation | Certification | Livrable attendu | Sources déclarées | Présence dans le dossier |
|---|---|---|---|---|
| INV‑046 | `DELIVERY_PASS_R3P1`, SHA‑256 `b3d1aaf1…607d1` | `INV-046_INVESTIGATION.md` | **`SRC=8`** | **absent** : seuls `RUN_CARD.md` et `RUN_HANDOFF.md` existent |
| INV‑063 | `DELIVERY_PASS_R3P1`, SHA‑256 `ee088d01…0181e` | `INV-063_INVESTIGATION.md` | **`SRC=12`** | **absent** : seul `RUN_HANDOFF.md` existe |

Recherche faite sur **tout le dépôt** `truth-engine` : aucune occurrence de ces deux fichiers, ni sous forme de dossier, ni dans une archive. Les tables de sources vivaient dans les livrables manquants ; le handoff, lui, ne nomme aucune source. L’annexe du dossier ne fait que recopier le handoff.

Conséquence pour l’article : **la l. 62 et la l. 129 reposent sur des pièces que ni le lecteur ni l’auditeur ne peuvent atteindre.** Aucune entrée n’a été ajoutée, parce qu’en ajouter une reviendrait à fabriquer une référence. **Deux options, à trancher par l’auteur** : reconstituer les sources de ces deux enquêtes (les documents sont publics et identifiables : le règlement CSA, le règlement (UE) 2024/1183 pour eIDAS, le règlement (UE) 2023/1230 et l’analyse d’impact de la Commission pour les machines), ou retirer l’attribution à une investigation et s’en tenir à ces textes.

## 4. Le septième constat : « 101 voyages parlementaires financés » n’existe pas dans son enquête

En cherchant à quoi rattacher la ligne ELNET du tableau (l. 181), j’ai vérifié la source qui la porte.

**« 101 » est absent de l’intégralité du dossier INV‑027.** Recherche exhaustive : aucune occurrence. Ce que l’investigation établit est d’un autre ordre :

> « dépenses HATVP de **100 à 200 k€ par an de 2021 à 2025**, trois personnes dédiées, objectifs législatifs et diplomatiques explicites, événements et voyages parlementaires **dont plusieurs prises en charge** sont confirmés par les déclarations de l’Assemblée nationale. » (`INV-027_RUN_HANDOFF.md`)

**D’où vient le chiffre.** De l’index d’un **article déjà publié**, `INV-002_CORPUS_MAP.csv`, sur une ligne `NOT_REVERIFIED` : « **101 voyages parlementaires en Israël (2017‑2024)** ». Le masterwork en a retiré « en Israël », gardé le chiffre, et l’a mis en gras dans un tableau. Deux dérives, donc : le chiffre n’est pas dans l’investigation invoquée, et la restriction de périmètre a disparu en chemin.

**Corrigé, lignes 181 et 215.**

| Ligne | Avant | Après |
|---|---|---|
| **181** | « **101 voyages parlementaires financés** (2017‑2024) » | « **Plusieurs voyages parlementaires pris en charge, confirmés par les déclarations de l’Assemblée nationale** (2017‑2024) » |
| **215** | « 101 voyages ELNET » | « Voyages ELNET pris en charge » |

C’est le **septième** fait corrigé sur cet article, après les cinq de F1 : il n’a été trouvé qu’en essayant de le sourcer. C’est l’argument le plus net en faveur de la demande de l’auteur : **une entrée de registre par investigation fait tomber les affirmations qui n’ont pas de pièce**.

## 5. Contrôles

| Contrôle | Résultat |
|---|---|
| Lignes modifiées | **6** : 66, 67, 113, 128, 181, 215 |
| Lignes ajoutées | **4** : entrées [65] à [68] |
| Lignes avant / après | 308 → **312** |
| Registre | 64 → **68** entrées, numérotation continue |
| Renvois `[n]` sans entrée de registre | **0** |
| Entrées jamais citées | **29**, inchangé (les quatre ajoutées sont citées) |
| Occurrences de « 101 voyages » | **0** |
| Cadre de la matrice | l. 215 ramenée à **75** caractères |
| Tiret cadratin | **0** |
| URL composée de mémoire | **aucune** ; toutes issues des tables `SRC` des investigations |

## 6. Ce que F3 laisse ouvert

1. **Deux investigations non sourçables** (§3), et deux paragraphes de l’article qui reposent sur elles : l. 62 et l. 129.
2. **Des affirmations sans entrée de registre, nommées** : « le Luxembourg ou les Pays-Bas » de l’encart EUCS et le rôle de la Chambre de commerce américaine (l. 61) reposent sur l’entrée [51], qui est une déclaration d’associations professionnelles ; « l’échec final sur la reconnaissance de la Palestine » (l. 181) a une source au dossier (INV‑027, SRC‑013, publication de l’Élysée du 22 septembre 2025) mais aucune entrée ; les « 121 investigations instruites » (l. 194) restent un décompte interne.
3. **Les 29 entrées de registre jamais citées**, dont [5] [6] [7] qui portent encore leur description d’avant correction de provenance.
4. **Deux bords de cadre** : l. 160 à 74 dans un cadre à 75, l. 210 à 76. Inchangés, hors objet.
5. **La typographie** : l’article porte encore 290 apostrophes ASCII contre 10 typographiques, en écart avec la charte du dossier.
