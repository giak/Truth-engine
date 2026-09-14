# SEMANTIC_DIFF_F10 — Convention des renvois [n], tranchée (2026-09-14)

**Mandat** : « Trancher la convention des 77 renvois [n] du masterwork : sources nommées dans la prose ou numérotation assumée ».

**Empreintes** : `2ebadef5…` (état reçu, 316 lignes) → **`878fda36…`** (état final, 316 lignes, 59 636 octets). Sauvegarde préalable : `/tmp/ARTICLE_MASTERWORK_AVANT_F10.md`.

## 1. L'arbitrage

**La numérotation est assumée, dans le corps comme au registre.** Trois raisons, par ordre de poids :

1. **Le registre du masterwork n'est pas une bibliographie décorative : c'est l'appareil de preuve.** Plusieurs entrées portent des segments audités que la numérotation seule rend contrôlables — [3] (chiffres du rapport VIGINUM 2024 relevés par l'audit du 14 septembre), [69] et [70] (pièces reconstituées par l'audit, avec la clause déclarant la table de sources non archivée). Supprimer les numéros du corps rendrait ces renvois inexprimables sans alourdir chaque phrase d'une description de pièce.
2. **Le corps nomme déjà les sources dans la prose** (« comme le relève le communiqué du département de la Justice », « la délibération HATVP 2022-123 ») : c'est la convention des articles publiés. Le numéro n'y ajoute pas de jargon, il ajoute **l'adresse de la pièce**. Les deux conventions ne concurrencent pas, elles se composent.
3. **Aucun article du corpus n'a de registre à 77 entrées.** Le masterwork est le premier ; la convention `[n]` du registre final numéroté existe déjà chez ChatGPT (plan V4.4, point 7 : « conserver la bibliographie numérotée finale, car les audits y renvoient »). Cette tranche l'étend au corps, qui en était séparé.

**Ce qui est rejeté** : le renvoi systématique à la moindre phrase (une phrase, un `[n]`), qui transforme la prose en note de bas de page. Le renvoi est posé **à l'emplacement de la pièce**, généralement en fin de proposition où la pièce est nommée.

## 2. L'application

Les renvois `[n]` ont été réinsérés dans la prose aux emplacements où le corps nomme une pièce du registre. La rédaction post-F2 les avait supprimés du corps ; la convention tranchée les rend obligatoires là où une pièce est invoquée. **33 emplacements de prose** (59 renvois, certains doubles `[n] [n]` pour une phrase portant deux pièces) :

| Partie | Emplacements posés | Renvois |
|---|---|---|
| Prologue | budget 57,1 Md€ | [76] |
| I.1 BNP | communiqué DOJ ; bilan pénalité+superlatif | [10] ; [10] [75] |
| I.2 Total | communiqué 16 mai ; capital 40 %/25,3 % ; arrêt Bank Melli | [11] [71] ; [74] ; [12] [13] |
| I.3 données | déclaration conjointe EUCS ; 66 M SNDS ; eIDAS 2 art. 45a ; dérogation ePrivacy | [51] ; [73] ; [69] ; [69] |
| I.4 officines | Abu Dhabi Secrets ; Rokh Solis | [65] ; [66] |
| I.5 Doppelgänger | rapport RRN 19 juillet 2023 ; chiffres 2024 ; signalements 7 plateformes | [77] ; [3] ; [3] |
| I.6 Front uni | relais DGSI + Conseil d'État | [67] |
| II.1 Alstom | pièces commission d'enquête + audition Kron ; autorisation IEF ; communiqué DOJ 772 M$ ; engagement 1 000 emplois ; réponse ministérielle 50 M€ ; rachat EDF + Le Monde | [1] [54], [53] ; [52] ; [44] ; [56] [72] ; [72] ; [55], [57] |
| II.2 ISDS | sentence Rockhopper ; annulation + sortie TCE | [49] ; [49], [50] |
| III.1 conseil | rapport Sénat 578 ; consortium Deloitte | [68] ; [70] |
| III.2 New IP | contribution C-0083 ; coalition ISOC | [27] ; [28] |
| III.3 agences | Boumans ; Vogler ; DSA art. 22 ; trusted flaggers ; étude JEEA | [29] ; [30] ; [34] ; [35] ; [31] |

**Une correction de cohérence dans le corps** : la phrase de la partie III.3 mentionnait l'article 22 du DSA sans pièce ; ajout de [34] (texte du DSA) et [35] (page Commission sur les signaleurs de confiance), toutes deux déjà au registre.
| IV.1 mobilités | Bailey ; Djebbari ; Farkas ; Kroes | [58] [59] ; [37] [38] ; [36] ; [39] |
| IV.2 droit pénal | art. 433-2 ; directive 2026/1021 ; rapport HATVP 2024 | [41] ; [42] ; [40] |
| V. garde-fous | Photonis ; Doppelgänger ; New IP ; TCE ; Lituanie | [24] ; [77] ; [28] ; [50] ; [16] [17] |

**Le paragraphe du registre** (« Notes bibliographiques et preuves documentaires ») disait : « Les sources sont citées dans la prose par leur nom. » Il dit désormais : « par leur nom et leur numéro de renvoi `[n]` ». C'est la traduction textuelle de l'arbitrage.

**Couverture vérifiée** : chaque renvoi du corps pointe vers une entrée existante (contrôle automatique, 0 orphelin) ; le registre compte 77 entrées numérotées en continu. Restent **non renvoyés dans le corps** les entrées de contexte, conformément à la déclaration du registre lui-même — leur liste est établie au §4.

## 3. Les correctifs mécaniques trouvés en vérifiant (aucun fait changé)

| L. | Avant | Après | Nature |
|---|---|---|---|
| 57 | « …aux États-Unis, dans son arrêt *Bank Melli Iran c. Telekom Deutschland*. » (fin dupliquée, résidu d'une réécriture antérieure — déjà vue et laissée avant correctif) | fin de phrase unique | répétition |
| 46 | « l'auto-censurer préventive » | « l'autocensure préventive » | grammaire |
| 89 | « Enquête pénal FCPA » | « Enquête pénale FCPA » | accord (cadre monospace) |
| 295 | « sur le pénalités liées » | « sur les pénalités liées » | grammaire (entrée [56]) |
| 297 | entrée [58] attribuait à « General Electric France : communiqué » une URL `connaissancedesenergies.org` (reprise AFP) | « (reprise AFP) » nomme l'hébergeur réel | exactitude d'attribution |

La l. 57 a été corrigée dans la même passe que la pose du renvoi [12] [13] : le correctif mécanique et le renvoi portent la même phrase.

## 4. Ce que la tranche ne prétend pas

- **La couverture n'est pas fermée à 100 % du corps.** Vingt-neuf entrées restent sans renvoi dans la prose. La liste exacte, établie par diff mécanique et reprise au §6 (le premier brouillon de cette liste, écrit de mémoire, citait [59] — qui est citée — et omettait [25] et [26] ; corrigé) : [2], [4], [5]-[9], [14], [15], [18]-[23], [25], [26], [32], [33], [43], [45]-[48], [60]-[64]. C'est cohérent avec la déclaration du registre, mais c'est un choix, pas un oubli ; son sort est tranché au §6.
- **L'unité d'attribution de [58] reste faible** : la nomination de Hugh Bailey repose sur une reprise AFP hébergée par un tiers, pas sur un communiqué GE primaire retrouvé. L'entrée le dit désormais.
- La typographie du masterwork (apostrophes typographiques, 0 tiret cadratin) est inchangée : **372 apostrophes typographiques, 0 ASCII** après corrections.

## 5. Contrôles

- Renvois `[n]` du corps : **61** sur 34 emplacements (dont 8 doubles `[n] [n]`), **0 orphelin** (toutes les cibles existent au registre 1→77).
- Le seul `[n]` hors registre subsistant est la datation du cadre monospace Alstom (« [2010] », « [14 Avril 2013] »), écart déclaré par F3, collision impossible.
- Registre : **77 entrées**, numérotation continue ; 316 lignes, 59 636 octets ; empreinte finale **`878fda36…`** (état F10.1 ; le complément F10.2 du §6 le fait évoluer).

## 6. Complément du même jour (F10.2) — le sort des entrées jamais citées, tranché

**Décision : mention explicite « (contexte) », pas de renvois forcés.** Trois raisons :

1. **Le renvoi serait une pièce absente.** La partie IV.2 énonce les articles 432-11 et 432-13 du Code pénal ; le registre ne porte aucune entrée propre pour ces deux textes ([41] ne couvre que le 433-2). Forcer un renvoi obligerait à créer une pièce nouvelle — exactement ce que les tranches précédentes refusent de faire sans vérification.
2. **La jonction prose-contexte existe déjà quand elle importe.** Le corps nomme ses pièces de contexte par leur nom quand il les invoque (la Lituanie et le différend OMC, les livraisons de gaz russe interrompues, l'accord Vattenfall). Là où aucune phrase n'invoque la pièce, un numéro ne créerait pas un usage, il en simulerait un.
3. **Vingt-neuf renvois prudents seraient vingt-neuf appariements non réclamés par une phrase**, la précision artificielle que le plan de corrections interdit depuis l'origine.

**Application** : 29 balises « (contexte) », une en fin de chaque entrée non citée, posées mécaniquement puis vérifiées par diff — l'ensemble des entrées balisées est identique à l'ensemble des entrées non citées, ni plus ni moins. Le paragraphe d'introduction du registre décrit désormais la convention et dit pourquoi aucune entrée contextuelle n'est retirée.

**Contrôles F10.2** : balises **29** · orphelins **0** · apostrophes ASCII **0** · tiret cadratin **0** · 316 lignes, **60 224 octets** · empreinte `878fda36…` → **`997e76a6…`** · sauvegarde préalable `/tmp/ARTICLE_MASTERWORK_AVANT_F10b.md`.

## 7. Complément du même jour (F10.3) — les articles 432-11 et 432-13 reçoivent leurs entrées

**Mandat** : « Add verified register entries for Articles 432-11 and 432-13 from Légifrance so Part IV.2 stops leaning on [41] ». **Sources** : les deux pages Légifrance lues intégralement en version en vigueur — 432-11 (LEGIARTI000042780056, depuis le 27/12/2020, loi n° 2020-1672) et 432-13 (LEGIARTI000033912762, depuis le 22/01/2017, loi n° 2017-55) — retrouvées par recherche après l'échec d'un identifiant deviné (la page répondue était l'article 311-1 : deviner un identifiant est une faute, l'identifiant réel a été cherché) ; protocole Mémoire d'abord respecté (cache miss, web, write-back `a8e886b2…` et `b46c5fef…`). **La confrontation au texte a trouvé deux défauts de droit dans la partie IV.2**, corrigés en posant les entrées :

1. **La phrase disait l'inverse du délai de l'article 432-13.** Elle écrivait que l'action pénale « exige la preuve que l'ancien agent a effectivement « surveillé » ou « contrôlé » l'entreprise concernée **au cours des trois années précédant sa prise de fonctions privées** ». L'article 432-13 réprime la participation « avant l'expiration d'un délai de trois ans suivant la cessation de ces fonctions » : le délai court **depuis le départ**, il borne la reprise d'une activité privée, il n'impose pas que la surveillance ait eu lieu dans les trois années antérieures. La phrase a été réécrite (délai depuis la cessation ; surveillance, contrats ou avis dans le cadre des fonctions effectivement exercées), avec renvoi [79]. L'argument d'angle mort de la sous-section reste intact — il repose sur l'exigence de fait (surveillance/contrôle/contrats/avis effectifs), que le texte conserve.
2. **[41] ne couvrait pas ce qu'on lui faisait couvrir.** La partie IV.2 citait 432-11, 432-13 et 433-2 sous un renvoi unique [41]. Désormais : [78] (432-11, Corruption passive et trafic d'influence, dix ans et 1 000 000 €) ; [79] (432-13, trois ans et 200 000 €) ; [41] conservé pour 433-2 seul, dont la description est alignée sur le texte (« quiconque sollicite ou agrée des avantages pour abuser de son influence, réelle ou supposée ») et qui porte bien le trafic d'influence côté particulier.

**Insertions au registre** : **[78]** et **[79]**, chacune avec numéro d'article, intitulé exact, peines, version en vigueur et loi de modification, URL Légifrance. Registre : 77 → **79 entrées**, numérotation continue 1→79. Renvois de prose : [78] et [79] posés aux deux phrases de la partie IV.2 (61 → **63 renvois**).

**Erratum du 14 septembre 2026, après relecture complète de l'état final** : le décompte « 61 → 63 » de ce paragraphe est faux. Reconstitué sur les états sauvegardés : **57 occurrences après F10.2** (`/tmp/ARTICLE_MASTERWORK_AVANT_F10b.md`), **62 après F10.3** — l'ajout de [78] ×2 et [79] ×1 aurait dû mener à 60 + 3 = 63, mais un état intermédiaire sauvegardé (`/tmp/ARTICLE_MASTERWORK_AVANT_F10c_check.md`, lui-même postérieur au début de F10.3) porte déjà 60 occurrences avec [78] ×1 et [79] ×2, si bien que la comptabilité pas à pas de F10.3 ne peut plus être reconstituée avec certitude — **62 également après F10.4**. Le chiffre juste à l'état final est **62**, et la comptabilité de transition « 61 » est invérifiable. La relecture complète a en outre montré qu'aucune entrée n'a été perdue (0 orphelin, 0 entrée morte). Conservé tel quel par décision de ne pas réécrire les états de tranche ; le lecteur doit tenir **62** pour le compte exact à partir de F10.3.

**Contrôles F10.3** : orphelins **0** (le seul terme hors registre demeure « [2010] », datation du monospace Alstom) · balises « (contexte) » **29**, inchangées, aucune sur [78]/[79] (les deux nouvelles entrées sont citées) · apostrophes ASCII **0** · tiret cadratin **0** · 318 lignes, **61 826 octets** · empreinte `997e76a6…` → **`150da463…`** · sauvegardes `/tmp/ARTICLE_MASTERWORK_AVANT_F10b.md` (état 59 636) et lecture des pièces avant écriture.

**Ce que F10.3 ne prétendait pas** : la directive 2026/1021 [42] n'avait pas été relue — son renvoi préexistait et aucune phrase ne lui faisait dire autre chose que son objet déclaré. *(Résidu fermé par le §8 ci-dessous.)*

## 8. Complément du même jour (F10.4) — la directive (UE) 2026/1021 lue en intégralité

**Mandat** : « Read directive (EU) 2026/1021 in full and check the harmonization sentence in Part IV.2 against it ».

**Accès aux pièces** : EUR-Lex est resté inaccessible en machine (tamporation 202 à corps vide sur toutes les variantes ELI, TXT/HTML, PDF, avec session ; read_url : « no readable text »). Le **texte intégral** a été lu par ailleurs : **PE-CONS 1/26** (INIT, Conseil, 8 avril 2026, fichier 2023/0135(COD), PDF de 2 294 lignes extraites), l'identité du texte étant confirmée par son intitulé (« on combatting corruption, replacing Council Framework Decision 2003/568/JHA »). Recoupements : **eucrim** (résumé structure par structure de la version JO) et trois notes d'avocats concordantes sur les dates. Protocole Mémoire d'abord : cache miss → web → write-back `5e8c0f67…`.

**Ce que la lecture établit** : directive du 29 avril 2026 ; publication au JOUE le 11 mai 2026 ; **entrée en vigueur le 31 mai 2026** (art. 39 : vingtième jour après publication ; recoupé sur quatre sources concordantes, une note d'avocats portant « 1er juin » demeurant un écart minoritaire) ; transposition à vingt-quatre mois (trente-six pour évaluations de risques et stratégies nationales), soit mai 2028. Elle harmonise un noyau d'incriminations : corruption active et passive, secteurs public et privé (art. 3-5), trafic d'influence (art. 6), exercice illicite de fonctions publiques (art. 7), obstruction (8), enrichissement (9), dissimulation (10), avec minima de peines (5/4/3 ans) et plafonds de amendes pour personnes morales (5 % du CA mondial ou 40 M€ ; 3 % ou 24 M€).

**La confrontation à la phrase de la partie IV.2 a trouvé un défaut** : la phrase disait que « l'ensemble de ces incriminations » — dont **l'article 432-13, la prise illégale d'intérêts** — est « en cours d'harmonisation européenne ». **Le noyau pénal de la directive ne contient pas la prise illégale d'intérêts** ; les conflits d'intérêts relèvent de son volet prévention (art. 21 et suivants). La phrase a été réécrite : elle nomme les dates, le noyau harmonisé, et dit explicitement que la prise illégale d'intérêts et les règles de conflits d'intérêts relèvent du volet prévention et de la réglementation nationale des mobilités, non du noyau pénal. Renvois [78] [79] [42] posés. L'entrée [42] est enrichie (dates, remplacement 2003/568/JHA, délais). L'argument d'angle mort de la sous-section en sort renforcé : le droit européen ne vient pas combler le trou français.

**Contrôles F10.4** : registre **79**, numérotation continue · renvois du corps 63, orphelins **0** · balises « (contexte) » **29**, inchangées · ASCII **0** · cadratin **0** · 318 lignes, **62 439 octets** · empreinte `150da463…` → **`25b32297…`** · PDF source conservé : `/tmp/pe126.pdf`.
- Apostrophes ASCII **0** ; tiret cadratin **0** ; cadres monospace inchangés (24 lignes à 75, 4 à 84 — la matrice de F7 est un tableau Markdown).
