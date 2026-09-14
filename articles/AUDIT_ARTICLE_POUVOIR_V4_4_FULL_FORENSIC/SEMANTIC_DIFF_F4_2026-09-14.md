# SEMANTIC_DIFF, tranche F4, les deux investigations non sourçables

Objet : `01_TARGET/ARTICLE_MASTERWORK_SOUVERAINETE_2026.md`.
Empreinte avant : `8d0d526d70f6291382020f5b355eabda52430183640ea38c2de348548fd529b4` (état après F3).
Empreinte après : **`ae87a9ba`**.
Sauvegarde : `/tmp/ARTICLE_MASTERWORK_AVANT_F4.md`.

Demande : **reconstituer les sources d’INV‑046 et d’INV‑063 depuis les textes publics identifiables, ou retirer leur attribution**. La tranche F3 avait posé les deux issues sans trancher, parce que les livrables `INV-046_INVESTIGATION.md` et `INV-063_INVESTIGATION.md` sont absents du dépôt et que leurs tables de sources vivaient dans ces livrables.

**Décision : reconstituer, et corriger en même temps.** Les textes primaires sont identifiables et vérifiables, donc l’article n’a plus besoin de s’appuyer sur une pièce inatteignable. Mais la reconstitution seule aurait laissé intact un second défaut, plus grave que l’absence de source : **les deux passages attribuaient à leur investigation des conclusions que la certification de cette investigation refuse.** Une référence ajoutée sur une phrase fausse ne fait que rendre la phrase fausse citable.

**Deux lignes modifiées, deux ajoutées** : 62 et 129 modifiées ; [69] et [70] ajoutées en fin de registre. 312 → 314 lignes. 48 245 → 50 985 octets.

---

## 1. Ce que la certification de chaque investigation dit réellement

Les deux `RUN_HANDOFF` sont présents, certifiés `DELIVERY_PASS_R3P1`, et portent le registre causal. **C’est là que se trouve le défaut, et il est indépendant de la question des sources.**

### INV‑046, « infrastructures numériques de contrôle »

Le handoff déclare deux chaînes `UNRESOLVED` :

| Chaîne | Statut déclaré |
|---|---|
| `QWAC -> reconnaissance navigateur -> interception générale` | **UNRESOLVED** |
| `EUDI + CSA + QWAC -> profil citoyen commun -> sanction politique` | **UNRESOLVED** |

Et un gap matériel explicite, `CLM-001` : « **Aucun pont juridique/technique démontré** ne relie EUDI, QWAC et détection CSA à une décision politique automatisée ou à un profil citoyen commun. »

Or la l. 62 écrivait « L’investigation **démontre** la tentative récurrente d’imposer des exigences d’interception et de **scanning obligatoire** […] **menaçant de créer une architecture technique** d’affaiblissement du chiffrement de bout en bout ». **Deux erreurs dans une phrase** :

1. Elle fait dire « démontre » à une investigation qui certifie `UNRESOLVED` et `CLM-001`. Le delta central du handoff conclut exactement l’inverse : « **aucun pont probant ne ferme aujourd’hui** une architecture intégrée identité→communications→sanction politique ».
2. Elle qualifie le scanning d’**obligatoire**, alors que le handoff écrit « le scanning CSA actuel est **volontaire et temporaire** ».

### INV‑063, « Big Four et production de normes »

Le handoff est plus précis encore, et la l. 129 le contredisait sur trois points :

| Ce qu’écrivait la l. 129 | Ce que la certification déclare |
|---|---|
| « L’investigation documente des **cas** » (pluriel) | **Un** cas est établi au niveau consortium |
| « études d’impact […] se retrouvent **directement intégrées dans le texte final** du règlement » | La chaîne supportée est « expertise externe/étude → préparation réglementaire → **continuité textuelle** dans la norme, **au niveau consortium** » |
| « **confiant aux Big Four la rédaction** des cadres d’évaluation dont ils commercialisent ensuite la mise en conformité » | `Big Four standard-setting access -> specific adopted standard because of Big Four input` = **UNRESOLVED** ; `CLM-005` : « Deloitte-specific marginal causal contribution **is not isolated** » |

La dernière ligne de la l. 129 était donc l’affirmation la plus lourde de l’article, et **la seule que son dossier refusait** : elle transformait un accès documenté en contrôle démontré.

---

## 2. Les sources reconstituées, et vérifiées texte en main

### INV‑046 : quatre pièces, toutes publiques

| Pièce | Vérification |
|---|---|
| Règlement (UE) 2024/1183 (eIDAS 2), **article 45** | **Lu.** « Qualified certificates for website authentication issued in accordance with paragraph 1 of this Article **shall be recognised by providers of web-browsers**. » L’obligation de reconnaissance par les navigateurs a donc bien survécu au texte final, contrairement à ce que laissait croire la formule « insertion de certificats de navigation obligatoires » |
| Règlement (UE) 2024/1183, **article 45a** | **Lu.** Les navigateurs « shall not take any measures contrary to » l’article 45, sauf « substantiated concerns related to security breaches or the loss of integrity of an identified certificate », mesures notifiées et réversibles sur demande de l’autorité compétente. **Le texte porte donc sa propre limite**, que la l. 62 ignorait |
| Règlement (UE) 2021/1232, dérogation ePrivacy dite « Chat Control », rétablie par le règlement (UE) 2026/1881 | **Mémoire `status:CONFIRME`**, source Parlement européen : détection **volontaire**, sans soupçon préalable, **communications chiffrées de bout en bout hors champ** ; en vigueur du 31 juillet 2026 au **3 avril 2028** |
| Proposition de règlement permanent (CSAM), 11 mai 2022 | **Mémoire `status:CONFIRME`** : toujours en négociation, cinq trilogues, impasse au 29 juin 2026, prochain trilogue fixé au 29 septembre 2026 ; **le blocage porte précisément sur la détection obligatoire**, et la position du Conseil prévoit une détection volontaire, le scan du chiffrement de bout en bout ayant été retiré |

### INV‑063 : trois pièces, dont une identifiée par sa propre page de titre

L’identification qui manquait est venue de l’étude elle-même, téléchargée et lue :

> **Impact assessment study on the revision of Directive 2006/42/EC on machinery**, *Final report*, **« Written by Valdani Vicari & Associati, Deloitte, The Vienna Institute for International Economic Studies, Ecorys »**, juin 2020, **DG GROW**, Office des publications de l’Union européenne, **ISBN 978‑92‑76‑01738‑7**, **doi:10.2873/423938**.

**Le consortium inclut donc bien Deloitte**, et il en comprend trois autres membres, ce que la l. 129 passait sous silence. Le corps de l’étude établit la recommandation que la l. 129 attribuait au seul « Big Four » :

> « Results from case studies conducted indicate that a provision or specification of requirements that need to be in place to ensure that software updates are safe **could be beneficial**. » Et : « When it comes to **software that ensures a safety function and is placed on the market independently from the machinery product**, the conclusions show that it **should be covered** by the Directive and be **considered as a safety component**. »

**La continuité est vérifiable texte en main, et elle est plus forte que ce que le handoff résumait.** Le considérant 19 du règlement (UE) 2023/1230 dispose :

> « In order to take into account the increasing use of software as a safety component, **software that performs a safety function and which is placed independently on the market should be considered a safety component**. »

C’est la recommandation de l’étude de juin 2020, reprise comme définition dans le règlement de 2023. La chaîne « étude de consortium → préparation réglementaire → continuité textuelle » n’est donc pas une reconstruction d’intention : elle a un point d’arrivée nommable.

---

## 3. Les deux corrections

| Ligne | Avant | Après |
|---|---|---|
| **62** | « L’investigation […] **démontre** la tentative récurrente d’imposer des exigences d’interception et de **scanning obligatoire** […] **menaçant de créer une architecture technique** d’affaiblissement du chiffrement » | « **Deux tentatives** […] et **leurs issues sont documentées** » ; obligation de reconnaissance des certificats **encadrée par l’article 45a** ; dérogation rétablie jusqu’au 3 avril 2028, détection « **volontaire** », communications chiffrées « **exclues** » ; règlement permanent toujours en négociation, « le blocage porte **précisément sur la détection obligatoire** » ; « **aucune pièce ne ferme le pont** entre elles et une architecture intégrée d’identité, de communications et de sanction » |
| **129** | « documente des **cas** » ; « se retrouvent **directement intégrées dans le texte final** » ; « **confiant aux Big Four la rédaction** des cadres d’évaluation dont ils commercialisent ensuite la mise en conformité » | « **Un cas** documenté porte sur la sécurité des machines » ; l’étude est **nommée avec ses quatre auteurs** ; ses études de cas recommandent de traiter le logiciel de sécurité comme composant de sécurité ; « **le considérant 19 du règlement (UE) 2023/1230 retient précisément cette solution** » ; « **elle n’isole pas la contribution propre de Deloitte et ne démontre ni capture ni contrôle de la décision** » |

**Ce que la correction fait gagner, contre l’intuition.** La l. 62 ne recule pas : elle remplace une architecture « menaçante » par une tentative **dont on connaît l’issue**, et une issue documentée est plus forte qu’une menace non datée. La l. 129 ne recule pas non plus : elle échange « les Big Four rédigent les normes » contre un mécanisme nommable, avec une étude identifiée, une recommandation citée et un considérant qui la reprend.

**Détail typographique.** Les deux lignes corrigées suivent la graphie du masterwork (apostrophes ASCII), et non celle de l’article V4.4/V4.5. Un document ne se normalise pas par tranche ; l’écart du masterwork avec la charte du dossier reste l’ouverture déclarée par F3.

---

## 4. Les deux entrées de registre, et leur statut exact

### [69] · Enquête « infrastructures numériques de contrôle »

Règlement (UE) 2024/1183, articles 45 et 45a · Règlement (UE) 2021/1232, rétabli par le règlement (UE) 2026/1881 · Parlement européen, communiqué du 9 juillet 2026.

### [70] · Enquête « Big Four et production de normes »

*Impact assessment study on the revision of Directive 2006/42/EC on machinery*, VVA, Deloitte, wiiw, Ecorys, juin 2020, ISBN 978‑92‑76‑01738‑7, doi:10.2873/423938 · Analyse d’impact SWD(2021) 82 final · Règlement (UE) 2023/1230, considérant 19.

**Ces deux entrées sont une reconstruction de l’auditeur, pas une récupération.** Les tables de sources des deux investigations restent absentes : ce que F4 a fait, c’est rendre vérifiables les affirmations de l’article en les adossant aux textes primaires, et déclarer que c’est ce qu’elle a fait. **Un lecteur qui suit [69] ou [70] atteint les pièces, pas l’investigation** : le dossier interne n’est ni reconstitué ni remplacé, et les deux livrables manquants le restent.

**Résolution des sources, testée le 14 septembre 2026**

| Source | Code |
|---|---|
| `eur-lex.europa.eu/eli/reg/2024/1183/oj` | **200** |
| `eur-lex.europa.eu/eli/reg/2021/1232/oj` | **200** |
| `eur-lex.europa.eu/eli/reg/2026/1881/oj` | **200** |
| `europarl.europa.eu/.../20260706IPR46318/...` | **202**, contenu servi |
| `eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:52021SC0082` | **200** |
| `eur-lex.europa.eu/eli/reg/2023/1230/oj` | **200** |
| Étude, copie accessible (Osalan, gouvernement basque) | **200**, 11,8 Mo, page de titre lue |
| `consilium.europa.eu/.../council-moves-to-reinstate-interim-measure...` | **403**, **écartée** : protection contre les robots |

La décision d’écarter le communiqué du Conseil suit la règle posée en F3 : une entrée de registre qui renvoie à une page inaccessible ne rend rien vérifiable. Le fait qu’il porte, le rétablissement de la dérogation, est couvert par le communiqué du Parlement, qui répond.

**Deux limites de vérification, déclarées.** D’abord, le texte d’EUR‑Lex n’est pas lisible depuis cet environnement : les articles 45 et 45a de 2024/1183 et le considérant 19 de 2023/1230 ont été lus sur des copies qui reproduisent le texte intégral, et le considérant 19 a été recoupé sur trois sources indépendantes. Ensuite, **la version forte du handoff sur l’analyse d’impact (un cas présenté par la Commission comme confirmant le besoin d’une exigence sur le logiciel de sécurité) n’a pas été vérifiée, et elle n’a pas été portée dans l’article.** La phrase écrite se borne à ce qui est sûr : SWD(2021) 82 a accompagné la proposition. Ce n’est pas un affaiblissement de complaisance, c’est le retrait d’une affirmation dont la pièce n’a pas été ouverte.

---

## 5. Contrôles

| Contrôle | Résultat |
|---|---|
| Lignes modifiées | **2** : 62, 129 |
| Lignes ajoutées | **2** : entrées [69], [70] |
| Lignes avant / après | 312 → **314** |
| Registre | 68 → **70**, numérotation continue |
| Renvois `[n]` du corps sans entrée de registre | **0** |
| Entrées jamais citées | **29**, inchangé, les deux ajoutées étant citées |
| Codes `INV-` visibles dans le corps | **0** |
| Attributions à une investigation sans source primaire | **0** (deux avant) |
| Tiret cadratin | **0** |
| URL composée de mémoire | **aucune** |

---

## 6. Ce que F4 laisse ouvert

1. **Les deux livrables restent absents du dépôt.** F4 ne les reconstitue pas : elle retire à l’article le besoin de s’y appuyer. Si les fichiers existent ailleurs, ils restent à récupérer, et l’entrée [70] devrait alors être confrontée à la table de sources réelle.
2. **Les deux investigations restent non auditables en tant qu’enquêtes** : la question « cette investigation a-t-elle fait ce qu’elle annonce » n’est toujours pas vérifiable, seule la question « les pièces publiques soutiennent-elles la phrase » l’est désormais.
3. **Les 29 entrées de registre jamais citées** restent, dont [5] [6] [7] qui portent encore leur description d’avant correction de provenance.
4. **Trois affirmations de l’article reposent sur des pièces que F4 n’a pas ouvertes** : « le Luxembourg ou les Pays-Bas » de l’encart EUCS et le rôle de la Chambre de commerce américaine (l. 61, adossés à l’entrée [51], qui est une déclaration d’associations professionnelles et non un acte de droit) ; « l’échec final sur la reconnaissance de la Palestine » (l. 181) ; et « les 121 investigations instruites » (l. 194), décompte interne.
5. **Le défaut de fond du masterwork, son énoncé d’architecture intégrée (l. 194), n’est pas touché.** Les corrections de F4 rendent deux pièces vérifiables ; elles ne changent pas le statut probatoire d’une thèse.
