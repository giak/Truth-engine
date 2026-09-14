# SEMANTIC_DIFF, tranche F5, la recherche des deux livrables et la confrontation des entrées [69] et [70]

Objet : `01_TARGET/ARTICLE_MASTERWORK_SOUVERAINETE_2026.md`.
Empreinte avant : `ae87a9ba` (état après F4).
Empreinte après : **`dbeccfe7`**.
Sauvegarde : `/tmp/ARTICLE_MASTERWORK_AVANT_F4.md` reste l’état d’avant F4 ; l’état d’avant F5 est reproductible par l’empreinte `ae87a9ba`.

Demande : **récupérer les deux livrables manquants s’ils existent ailleurs, et confronter l’entrée [70] à leur table de sources réelle.**

**Réponse en deux temps.** Les deux livrables **n’existent nulle part dans le dépôt**, et l’absence est maintenant **documentée par le dossier lui-même**, non plus seulement constatée par l’auditeur. Et la confrontation demandée **n’a pas de second terme** : la table de sources à laquelle confronter l’entrée [70] n’existe pas non plus. Ce que le dossier contient à sa place oblige en revanche à **corriger les deux entrées**, et c’est fait.

---

## 1. La recherche des livrables : six vérifications, toutes négatives

Périmètre tenu : **strictement le dossier projet** `/home/giak/projects/truth-engine`. Aucune recherche hors de lui.

| # | Vérification | Méthode | Résultat |
|---|---|---|---|
| 1 | Nom de fichier | `find` sur tout le projet, `INV-046*`, `INV-063*`, `*INVESTIGATION*` | **Aucun livrable.** 1 986 fichiers « INVESTIGATION » existent, couvrant **64 identifiants** d’investigation, dont les voisins INV‑044, INV‑045, INV‑047, INV‑049, INV‑062, INV‑066. INV‑046 et INV‑063 n’y sont pas |
| 2 | **Empreinte du contenu** | `sha256sum` des **26 631 fichiers** du projet, comparés aux empreintes déclarées par les deux handoffs (`b3d1aaf1…607d1`, `ee088d01…0181e`) | **Aucune correspondance.** Un fichier renommé aurait été trouvé ; il ne l’est pas |
| 3 | Contenu des archives | les **176 archives** du projet, listées une par une | Quatre contiennent des fichiers INV‑046/INV‑063 : `DEMOCRACY_INFLUENCE_COMPLETE_BUNDLE` et `FORENSIC_CORPUS_REBUILT`, et leurs copies. **Toutes ne contiennent que `RUN_CARD` et `RUN_HANDOFF`** |
| 4 | Historique git | `git log --all`, `git rev-list --all --objects` sur les **8 branches** | Les seuls objets sont les `RUN_CARD` et `RUN_HANDOFF`. **Aucun livrable n’a jamais été commité, ni supprimé** |
| 5 | Chemin d’origine exact | déduit du fichier de certification (voir §2) | Le chemin `investigations/2026-09/2026-09-10_chat-control-eudi/2026-09-10_23-10_chat-control-eudi_INVESTIGATION.md` **n’existe pas**. Le dossier du run ne contient que le JSON de certification |
| 6 | Fichier renommé ou brouillon | recherche textuelle des chaînes propres aux deux livrables (« profil citoyen commun », « QWAC », « EUDI + CSA », « chat-control-eudi », « big-four-norm-production ») | **Toutes les occurrences sont des handoffs, registres, index ou documents d’audit.** Aucun livrable, aucun brouillon |

**Conclusion de la recherche : les deux livrables sont absents, et cette absence est vérifiée par six voies indépendantes.**

---

## 2. Ce que la recherche a trouvé à leur place, et qui tranche la question

Trois pièces du dossier **déclarent elles-mêmes** l’absence, ce que la tranche F3 n’avait pas vu.

### La matrice d’artefacts du bundle

`03_INVESTIGATIONS/INVESTIGATION_ARTIFACT_MATRIX.csv` classe chaque investigation par complétude :

```
INV-046,CLOSED,PRIMARY,W3,…,handoff=1,…,artifact_file_count=2,HANDOFF_OR_DERIVED_ONLY,INV-046_RUN_HANDOFF.md
INV-063,CLOSED,PRIMARY,W5,…,handoff=1,…,artifact_file_count=1,HANDOFF_OR_DERIVED_ONLY,INV-063_RUN_HANDOFF.md
```

**Le bundle lui-même déclare que ces deux investigations n’ont qu’un handoff pour artefact, et que leur `result_path` EST le handoff.** Elles appartiennent à une classe documentée de **27 investigations** sur 147 (`HANDOFF_OR_DERIVED_ONLY`), aux côtés de INV‑041, INV‑042 et INV‑048. Répartition complète : 81 `PARTIAL_MACHINE_ARTIFACTS`, 27 `HANDOFF_OR_DERIVED_ONLY`, 26 `NO_ARTIFACT_RECOVERED`, 13 `CANONICAL_6_COMPLETE`.

### Le fichier de certification d’INV‑046

`…/invchain/te/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-10_chat-control-eudi/2026-09-10_23-10_chat-control-eudi_CERTIFICATION.json` :

> `"verdict": "PASS"`, `"head": "NO_GIT"`, `"deliverable": "investigations/2026-09/2026-09-10_chat-control-eudi/2026-09-10_23-10_chat-control-eudi_INVESTIGATION.md"`, `"deliverable_sha256": "b3d1aaf1…607d1"`

Deux choses en sortent. Le livrable a **un chemin d’origine et une empreinte**, et `"head": "NO_GIT"` explique pourquoi git ne l’a jamais vu : **le run a été produit hors dépôt**. Seul ce JSON a été rapatrié dans l’arborescence d’archives, pas le livrable. Aucun équivalent n’existe pour INV‑063 : son run `20260910-0621-big-four-norm-production` n’apparaît **que dans les handoffs**, sans dossier de run ni certification.

### Les quintessences A1, qui montrent que toute la chaîne aval a travaillé sans les livrables

`05_ARTICLE_PREPARATION/01_INITIAL_121_RUN/runtime/A1_QUINTESSENCES.csv`, colonnes `mode` et `source` :

```
INV-046,…,DIRECT_TERMINAL_HANDOFF,/mnt/data/DEMOCRACY_INFLUENCE_COMPLETE_BUNDLE_2026-09-11/invchain/INV-046_RUN_HANDOFF.md,…
INV-063,…,DIRECT_TERMINAL_HANDOFF,/mnt/data/DEMOCRACY_INFLUENCE_COMPLETE_BUNDLE_2026-09-11/invchain/INV-063_RUN_HANDOFF.md,…
```

**Le pipeline aval a consommé le handoff, jamais le livrable.** Ce n’est pas une perte survenue après coup : la chaîne qui a produit l’article n’a jamais eu la table de sources.

**Effet secondaire utile.** La quintessence d’INV‑046, indépendante du handoff puisqu’elle est une condensation ultérieure, reprend mot pour mot la conclusion que F4 avait confrontée : « **aucun pont probant ne ferme aujourd’hui** une architecture intégrée identité→communications→sanction politique ». **La correction de la l. 62 tient donc contre deux copies**, l’original et sa quintessence.

---

## 3. La confrontation demandée : elle n’a pas de second terme

L’entrée [70] devait être confrontée à « la table de sources réelle ». **Cette table n’existe pas.** Les 8 sources déclarées par INV‑046 et les 12 déclarées par INV‑063 vivaient dans les livrables, et rien d’autre ne les porte.

Ce que le dossier contient à la place, et **qui oblige à corriger les deux entrées** : la colonne `corpus_refs` du registre courant donne, elle, les **entrées déclarées** de chaque investigation.

| | Entrées déclarées par le registre | Ce que l’entrée du registre de l’article cite |
|---|---|---|
| **INV‑046** | `A067` le goulag digital, `A071` l’architecture de la censure européenne, `A074` ce que Macron appelle protection, `A109` et `A110` « l’Europe construit-elle un crédit » : **cinq articles déjà publiés du corpus** | le règlement (UE) 2024/1183, le règlement (UE) 2021/1232 rétabli, un communiqué du Parlement |
| **INV‑063** | `A035` « l’argent qui disparaît », `A056` « le réseau qui nous facture » : **deux articles déjà publiés du corpus** | l’étude VVA/Deloitte/wiiw/Ecorys, l’analyse d’impact SWD(2021) 82, le règlement (UE) 2023/1230 |

**Les deux listes ne se recouvrent pas, et elles ne mesurent pas la même chose.** `corpus_refs` est le corpus de départ de l’enquête ; les pièces de l’entrée sont ce dont la **phrase de l’article** a besoin pour être vérifiable. Les confondre serait l’erreur que F4 avait précisément évitée en écrivant « reconstruction de l’auditeur » : l’entrée ne restitue pas la table de l’enquête, elle **remplace** une pièce inatteignable par des pièces atteignables.

**C’est ce que les deux entrées ne disaient pas, et que F5 corrige.** Une entrée préfixée « Enquête « Big Four et production de normes » : » se lit naturellement comme le dossier de cette enquête. Elle ne l’est pas.

### Le correctif, appliqué aux deux entrées

À la fin de **[69]** et de **[70]**, une clause unique :

> La table de sources de cette enquête n’est pas archivée : les pièces ci-dessus ont été réunies par l’audit du 14 septembre 2026.

Deux phrases, aucune ligne ajoutée au corps, et le lecteur sait désormais **ce qu’il tient** en suivant le renvoi : des pièces vérifiables, et non le dossier interne.

---

## 4. Une nuance à porter au crédit du handoff, et une limite qui reste

En cherchant, F4 n’avait pas porté dans l’article la version forte du handoff d’INV‑063 (un cas présenté par la Commission comme **confirmant le besoin** d’une exigence sur le logiciel de sécurité). La lecture du texte de l’étude précise ce point :

> « Results from case studies conducted indicate that a provision or specification of requirements that need to be in place to ensure that software updates are safe **could be beneficial**. »

La formulation de la source est **plus prudente** que celle du handoff : « pourrait être bénéfique », et non « confirme le besoin ». Ce que F4 avait vérifié, à savoir la recommandation sur le logiciel de sécurité indépendant et sa reprise au considérant 19, reste exact ; **la présentation qu’en fait l’analyse d’impact de la Commission n’a toujours pas été ouverte**, et l’article continue de ne pas s’en servir. La retenue de F4 n’était donc pas excessive : elle évitait une reformulation plus forte que sa source.

---

## 5. Contrôles

| Contrôle | Résultat |
|---|---|
| Lignes ajoutées ou supprimées | **0** (314 avant, 314 après) |
| Lignes modifiées | **2** : entrées [69] et [70], par ajout d’une clause finale |
| Empreinte | `ae87a9ba` → **`dbeccfe7`** |
| Octets | 50 985 → **51 255** |
| Registre | **70**, numérotation continue |
| Renvois `[n]` du corps sans entrée | **0** |
| Entrées jamais citées | **29**, inchangé |
| Tiret cadratin | **0** |
| Fichiers du projet balayés par empreinte | **26 631** |
| Archives inspectées | **176** |
| Branches git vérifiées | **8** |

---

## 6. Ce que F5 laisse ouvert

1. **Les deux livrables restent introuvables dans le dossier projet.** La recherche hors du dossier n’a pas été faite, et ne le sera pas sans demande explicite : le périmètre a été tenu.
2. **Le certificat d’INV‑063 n’existe pas** dans le dossier, seul celui d’INV‑046. On ne connaît donc pas le chemin d’origine ni l’empreinte de son livrable tel que le certificat les aurait portés.
3. **La confrontation des entrées aux `corpus_refs` est consignée ici, pas dans l’article** : décision assumée, parce que ces références sont des identifiants internes et des articles déjà publiés du corpus, qui n’apportent rien au contrôle du lecteur. Si l’auteur veut que le registre expose aussi ces entrées déclarées, c’est une décision qui lui revient.
4. **Le défaut de fond du masterwork (l. 194) reste entier** : la disponibilité ou l’absence des livrables ne change pas le statut probatoire d’une thèse.
