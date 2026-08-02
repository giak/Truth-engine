# Suivi — Page About « Comment ces articles sont écrits »

> Fichier de suivi du travail sur le texte pédagogique de la page About.
> Chaque tâche est listée ci-dessous avec son état. Les articles produits suivent
> la convention de nommage du projet : `YYYY-MM-DD_HH-MM_<sujet>_<type>.md`.

## État d'avancement

- [x] Design validé (structure 6 blocs, ton, chiffres) — voir `DESIGN.md`
- [x] Intégration des apports de la page About existante (langage symbolique,
      garde-fous, Immunité Cognitive, positionnement, libre de droit)
- [x] Intégration de Mnemolite (la mémoire du système) : recherche mémoire avant
      le web, sauvegarde après chaque enquête, nuance SKIP vs HALTE (KERNEL step 2),
      capitalisation entre enquêtes, chiffres réels vérifiés via MCP
- [x] Intégration de la diversité des LLM : croisement des biais, pas la puissance.
      Preuves : auditor (5 modèles locaux Ollama), Buffy=deepseek-v4-pro, Theo=Gemini,
      rapports ChatGPT dans le dossier Arte
- [x] Double check forensique des chiffres (2026-08-01) : tableau d'audit dans DESIGN.md
- [x] Correction du draft About (`page-about/about-draft.md`) avec chiffres vérifiés (déplacé depuis substack-online/ le 2026-08-02)
- [x] Rédaction du texte complet (~1 500-2 500 mots) : `2026-08-01_22-20_comment-articles-sont-ecrits_TEXTE-ABOUT.md`
- [x] Relecture style (AGENTS.md : zéro em-dash, espaces insécables, guillemets)
- [x] Intégration page About (Substack) : `page-about/about-page.md` (déplacé depuis substack-online/ le 2026-08-02)
- [ ] Validation humaine
- [x] Réorganisation page-about (2026-08-02) : `machine.md` créé, `about-draft.md`
      et `about-page.md` déplacés dans `page-about/` (v8)
- [x] Brainstorm fond validé (`BRAINSTORM.md`) : décisions actées en §7
      (A + B, question IA frontale, défauts connus publiés, démonstration Clichy)
- [x] Application v8b : réécriture `about-page.md` et `machine.md`
- [ ] Validation humaine des textes v8b
## Journal

### 2026-08-01 — Design validé, apports About intégrés

- Création du dossier `page-about/`
- Écriture de `DESIGN.md` : décisions validées, structure en 6 blocs,
  chiffres Arte sourcés, non-retenus explicites.
- Intégration de la page About : scan symbolique avant recherche, garde-fous
  (refus de publier incomplet, sources stratifiées, diversité épistémique),
  positionnement « entre les trois », Immunité Cognitive, libre de droit.
- Intégration de Mnemolite : la mémoire du système (recherche mémoire avant web,
  sauvegarde post-enquête, capitalisation). Chiffres vérifiés via MCP.
- Vérification chiffres : 148 concepts, 15 symboles, 9 patterns, 5 familles,
  16 clusters, 19 protocoles, 105 enquêtes, 2,9M mots, 80 %.

### 2026-08-01 — Double check forensique (demande explicite)

Audit de chaque affirmation du design contre le dépôt, 95 % de suspicion.
Résultats : plusieurs chiffres publiés sont faux ou invérifiables.

| Affirmation initiale | Verdict |
|----------------------|---------|
| « 148 concepts » | ⚠️ déclaration interne DSL.md, recompte partiel ~66-73, non reproductible |
| « 9 patterns » | ⚠️ PATTERNS.md : 10 définitions §1, 17 @PAT[] uniques |
| « 16 clusters » | ⚠️ 15 fichiers réels, 17 avec index/template, plan Arte dit 17 |
| « 19 protocoles d'investigation » | ❌ introuvable dans le dépôt (protocol/ = 2 fichiers) |
| « 105 enquêtes » | ⚠️ 714 fichiers INVESTIGATION réels, INDEX dit 261 dossiers |
| « 2,9 millions de mots » | ⚠️ draft About dit « 3,2 millions » : contradiction interne |
| « 117 articles / 8 mois » | ⚠️ draft About dit 116, articles/ = 67 fichiers ARTICLE |
| « 25 enquêtes Arte » | ❌ dossier documente 19 INVESTIGATION + 19 quintessences |
| « 19 sources Arte » (commentaire) | ⚠️ README du dossier dit 32 sources |
| « 16-30 h par article » | ⚠️ déclaration de l'auteur, non vérifiable |
| « mémoire DOWN = refus de travailler » | ❌ KERNEL step 2 : SKIP + continue ; HALTE réservé au pipeline Sublimator |
| « 4 764 enquêtes indexées » | ⚠️ entrées de mémoire, avec doublons et tests ; 714 fichiers réels |
| « le système n'a rien oublié » | ❌ exagération : recherche limitée à 5 résultats sur 10 fichiers |

Corrections appliquées dans DESIGN.md. Leçon : le texte pédagogique ne doit
citer que des chiffres ✅ vérifiés ou attribuer chaque chiffre ⚠️ à sa source
exacte (« le dépôt compte 19 enquêtes », « la page annonce 105 »).

### 2026-08-01 — Corrections appliquées au draft About

Mesures finales (commande `find` + `wc -w` + posts.csv) :

| Mesure | Valeur |
|--------|--------|
| Fichiers .md (investigations+articles+outputs) | 3 233 |
| Mots (investigations + articles, .md) | 2 230 877 (2,2 M) |
| Mots corpus complet .md (incl. outputs, book) | 4 406 289 (4,4 M) |
| Mots HTML publiés (substack-online/posts) | 389 039 |
| Posts posts.csv | 116 lignes, 114 is_published=true |
| Période posts | 2024-01-18 → 2026-07-28 (production dense 2025-11 → 2026-07) |
| Dossiers d'enquête datés 2026-* | 204 (2026-02 : 1, 03 : 12, 04 : 30, 05 : 14, 06 : 61, 07 : 86) |
| Git log « article #117 » | = ligne du CSV (116 posts + header), PAS 117 articles publiés |
| « 148 concepts » | introuvable dans DSL.md ❌ ; 40 symboles vérifiés (15 narratifs + 17 épistémiques + 8 factuels) |
| « 237 ans » RIC | ✅ ancré 1789 (2026−1789 = 237) ; la référence « loi Le Chapelier 1791 » était une incohérence (2026−1791 = 235) |
| « 64 secteurs, 1 710 Md€ » | ✅ La Laisse : 64 secteurs, 1 710 Md€, 57,3 % du PIB (F2 tier 1 ✦) |
| « 9 propriétaires, 90 % audience » | ✅ enquête BFM (3 occurrences, ①②, §) |
| « 14 juillet : 9 sections, 20 faits, 8 faisceaux » | ✅ 9 sections (REFERENCE_PLAN V32-V253 §1), 8 faisceaux (rapport phase 2), 20 faits (format tier 1) |

Corrections écrites dans `substack-online/about-draft.md` :

1. « Huit mois, 116 articles, 3,2 millions de mots » → « Depuis novembre 2025 :
   114 articles publiés, plus de deux millions de mots d'enquête documentés »
2. « 237 ans … jusqu'à la loi Le Chapelier de 1791 » → « depuis 1789 »
3. Section L'AMPLEUR : « 116 articles, 3,2 M mots, 148 concepts, 16 clusters,
   19 protocoles » → « 114 articles publiés, plus de 2,2 M de mots d'enquête,
   40 symboles narratifs, 15 clusters, des protocoles d'investigation documentés »
4. LA MÉTHODE : « 148 concepts codés » → « 40 symboles (15 narratifs,
   17 épistémiques, 8 factuels) »
5. Vérifié et conservé : « 9 propriétaires 90 % », « 64 secteurs, 1 710 Md€ »,
   « 14 juillet : 9 sections, 20 faits, 8 faisceaux »
6. Nettoyage em-dash restant (ligne 17 : « documentée — » → « documentée : »)

### 2026-08-01 — Rédaction du texte pédagogique

Fichier : `page-about/2026-08-01_22-20_comment-articles-sont-ecrits_TEXTE-ABOUT.md`
(horodatage réel 22:20 CEST).

- 1 701 mots, structure 6 blocs conforme à DESIGN.md
- Ouverture (question récurrente, réponse 3 phases, positionnement 3 mondes,
  annonce du plan) ; Phase 1 (20 étapes, scan symbolique 40 symboles, mémoire
  d'abord, matrice de faits, garde-fous, preuve Arte 94 min / 30 séquences) ;
  Phase 2 (quintessences, croisement, 3 perspectives, mémoire relie, 19 enquêtes
  Arte) ; Phase 3 (contraintes, premier jet jamais l'article, diversité des
  modèles, preuves Arte : 15 passes, 6 actes, 28 timecodes, 25 corrections,
  3 rapports) ; Le coût réel (16-30 h attribué à l'auteur, 30+ révisions,
  lecture à voix haute) ; La traçabilité (dépôt, mémoire, libre de droit,
  punchline Immunité Cognitive)
- Chiffres tous vérifiés ou attribués : aucune occurrence des chiffres ❌
  (148, 19 protocoles, 25 enquêtes, 105, 3,2M, 117) ; « dix-neuf enquêtes »
  et « sept cents fichiers » attribués au dépôt ; « seize à trente heures »
  explicitement déclaration de l'auteur
- Contrôles automatiques passés : 0 em-dash, 0 en-dash, 0 double espace,
  46 espaces insécables, guillemets « » correctement espacés
- Diversité des LLM : « on croise les sources, et on croise les modèles qui
  les lisent » — sans nommer les modèles (vulgarisation), conforme au design
- Mnemolite présentée comme « la mémoire du système », sans nom propre ni
  chiffre précis non attribué (« des dizaines de milliers d'entrées »)

### 2026-08-01 — v3 : registre manifeste validé (« la machine qui documente les machines »)

Retours auteur successifs : la v2 « ne veut rien dire » (phrases plaquées) ; le ton
« je » artisan/ébéniste rejeté (« bizarre ») ; l'échantillon impersonnel forensique
rejeté (« l'exemple est pourri ») ; l'échantillon manifeste partiellement validé
(« tu commences à saisir, mais pas encore ça ») → investigation approfondie :
lecture de `index.md` (ouvertures d'articles, registre : parallélismes + chiffres +
thèse) et de `archive/legacy-content/pages/about.md` (voix canonique).

Décision de design (v4) : le texte pédagogique est UNE PIÈCE du corpus, pas un
commentaire sur lui. Cadre : la machine qui documente les machines de contrôle.
Structure 6 blocs en mécanismes (anomalie, cadrage, matière, réduction, vérification,
prix et trace) + verdict. Formules binaires « Ce n'est pas X : c'est Y. »,
reprises du manifeste (« Je documente les machines de contrôle. Vous décidez. »,
« Cartographier l'architecture du mensonge institutionnel… »).

v3 écrite dans `2026-08-01_22-20_comment-articles-sont-ecrits_TEXTE-ABOUT.md` :
- 1 388 mots, 0 em-dash, 0 en-dash, 0 double espace, 56 espaces insécables,
  guillemets « » corrects
- Chiffres : tous vérifiés (44 min / 51 000 / 13 000 abonnés / 5,3 Md€ Clichy ;
  9 propriétaires 90 % BFM ; 40 symboles 15+17+8 ; 95 % ; 5 perspectives ;
  4 degrés ✦✧⁅❧ ; 6 dimensions EDI ; 14 juillet 9 sections 20 faits 8 faisceaux ;
  Arte 19 enquêtes 94 min 30 séquences 28 timecodes 15 passes 25 corrections
  3 rapports 6 actes 30 révisions ; 16-30 h attribué ; 5 000-15 000 mots)
- Registre : vérifié par l'utilisateur sur l'échantillon d'ouverture (44 min, BFMTV)
- À faire : validation humaine, intégration page About

### 2026-08-01 — Réécriture complète (retour auteur : « ce n'est pas très français »)

Critique reçue : phrases mal tournées, explications non fluides. Réécriture
de fond en comble (v2) :

- Suppression des constructions plaquées : « Le message de cette section est
  simple », « En une phrase », questions rhétoriques mécaniques
- Suppression des répétitions de structure « Le système X : ... » ; variété
  des sujets et des rythmes (phrases courtes après les longues)
- Transitions naturelles : « Vient ensuite le travail de recherche proprement
  dit », « Cette étape est décisive pour une raison simple »
- Ouverture reformulée : « La question revient sous chaque article »
- v2 = 1 552 mots ; mêmes chiffres, même structure, mêmes contraintes
- Contrôles automatiques repassés : 0 em-dash, 0 en-dash, 0 double espace,
  0 point-virgule sans insécable, 0 chiffre ❌

### 2026-08-01 — Intégration page About (Substack)

Fichier final : `substack-online/about-page.md` (2 139 mots).

- Structure : manifeste d'ouverture (5 entreprises, 80 %) → « Voici ce que vous
  recevez » → 4 teasers (14 juillet, débat BFM, geyser Clichy, architecture de la
  dépendance) → S'abonner → L'AMPLEUR (7 thématiques) → « La machine qui documente
  les machines » (texte v3 complet : anomalie, cadrage, matière, réduction,
  vérification, prix et trace, verdict) → POURQUOI → Libre de droit → Soutenir →
  Contact → citation de clôture
- Chiffres : tous issus d'about-draft.md corrigé (114 articles, 2,2 M mots,
  40 symboles, 15 clusters, 9 propriétaires 90 %, 64 secteurs 1 710 Md€,
  14 juillet 9 sections 20 faits 8 faisceaux, Clichy 44 min 51 000/13 000 abonnés)
- Contrôles : 0 em-dash, 0 en-dash, 0 double espace, 79 insécables,
  3 paires de guillemets fermées
- Titres convertis : « La machine qui documente les machines » en ##,
  sous-blocs en ### (sous-section de la page About)

### 2026-08-01 — v4 : socle « Empire du Mensonge », zéro exemple d'article (retour auteur)

Retours auteur (violents, justifiés) : « on ne vend pas des barils de lessive »,
« laisse tomber les exemples des articles », « ce n'est pas la bonne explication :
tout le monde ment, empire du mensonge », « on peut prendre n'importe quel
contenu, cela passe par l'analyse de Truth Engine qui a inspiré, et vice versa
cet article ». Pointé : https://giak.substack.com/p/lempire-du-mensonge-rapport-dautopsie

Audit forensique des exemples (révélateur) :
- « 13 000 abonnés » (draft Clichy) : FAUX, l'article dit « Moscow : 13 500 »
  = VUES, pas abonnés. Draft confondait vues et abonnés.
- « compte coordonné Storm-1516 (13 000 abonnés) » : FAUX, l'article dit que
  Sereti n'est PAS Storm-1516 (« il n'est pas coordonné avec ses opérations ») ;
  c'est @camille_moscow qui est documentée Storm-1516. Attribution inversée.
- « 51 000 abonnés » ✅ (Sereti : 51 831 abonnés) ; « 44 minutes » ✅
  (12h20 / 13h04) ; « 5,3 Md€ » ✅ (4,3 contrat SEDIF-Veolia + 1 Md FMHP).

Réécriture complète de la section méthode (page About) sur le socle de l'article
fondateur, documenté lignes 868-899 du post : hostilité symétrique (« Un récit
= propagande. Cinq récits = cartographie. »), hiérarchie ◈◉○ (primaires
prévalent), EDI (simple ≥ 0,30 ; complexe ≥ 0,70 ; APEX ≥ 0,80), patterns
Λ Ω Ψ Φ € ⚔ ρ, boucle contenu → analyse → investigation → article → méthode,
« La lucidité n'est pas un dogme : c'est une méthode. » / « Si ce texte vous
convainc trop facilement, c'est que vous n'avez pas appliqué le protocole. »

Nouvelle structure section méthode (6 blocs, zéro exemple d'article) :
1. N'importe quel contenu (95 % suspicion, même grille officiel/dissident)
2. Les sources : ◈◉○
3. La diversité épistémique (EDI)
4. La grille des patterns (Λ Ω Ψ Φ € ⚔ ρ)
5. La boucle (le rapport fondateur a inspiré la méthode et inversement)
6. La trace (matrice, dépôt versionné)

Contrôles : 0 em-dash, 0 en-dash, 0 double espace, 40 insécables, 0 occurrence
de Clichy/BFM/Arte/geyser/14 juillet/Storm/Veolia/SEDIF/44 minutes/19 enquêtes.

### 2026-08-01 — v4b : la chaîne de production réintégrée (retour auteur « c'est passé à la trappe ? »)

La refonte v4 avait jeté la production avec les exemples. Réintégration d'une
section « Comment un article est écrit » (4 blocs, registre autopsie, 0 exemple) :
- L'investigation : constituer le dossier (mémoire avant le web, grille des
  patterns scorée 0-10, recherche de la manipulation avant les faits, matrice
  ✦✧⁅❧, garde-fous : refus de publier incomplet, EDI 6 dimensions)
- La réduction : distiller le dossier (quintessences, thèses nées de la
  confrontation, jamais la mémoire du modèle)
- L'écriture : le premier jet n'est jamais l'article (passes forensiques,
  corrections classées par gravité, rapports d'audit conservés, croisement des
  modèles, synthèse + veto final)
- Le coût : la rigueur a un prix (16-30 h attribué à l'auteur, 5 000-15 000 mots)

Page complète : 1 500 mots, 64 insécables, 0 em-dash, 0 en-dash, 0 double
espace, 0 exemple d'article. Structure : manifeste → recevoir → S'abonner →
L'AMPLEUR → La méthode (6 blocs) → Comment un article est écrit (4 blocs) →
POURQUOI → Libre de droit/Soutenir/Contact → citation.

### 2026-08-02 — v5 : audit antagoniste + corrections intégrales (demande « applique tout »)

Audit antagoniste demandé par l'auteur (« qu'en penses-tu ? fait un audit et
critique antagoniste »). Vérifications script contre le dépôt, puis corrections
toutes appliquées.

| Point de critique | Verdict script | Correction appliquée |
|-------------------|----------------|----------------------|
| « 114 articles publiés » (l.3, l.21) | posts.csv = 114 is_published=true, mais index.md (maj 2026-07-31) référence 118 posts (IDs 1-119, manque 113) ; registre officiel à jour = index | « 118 articles publiés » (2 occurrences) |
| « 40 symboles narratifs » | faux : 40 symboles au total = 15 narratifs + 17 épistémiques + 8 factuels (SYMBOLS.md) | « 40 symboles codés » ; « symbole » défini au premier usage (« langage de symboles codés, des patterns ») |
| « 5 entreprises 80 % » (ouverture) | contredit le corpus sourcé : « 9 propriétaires ~90 % audience (RSF et Acrimed) » (post BFM, Le Verrou) ; DESIGN.md marquait 5/80 % comme déclaration non sourcée | ouverture = « neuf propriétaires ~90 % (selon RSF et Acrimed) » |
| « 2,2 M de mots » accolé aux articles publiés | articles publiés = 381 175 mots réels (~3 300/art) ; 2,2 M = fichiers d'enquête .md | « mots de dossiers d'enquête » (étiqueté, retiré de l.3) |
| « Neuf mois » | nov 2025 → août 2026 = dix mois | « Dix mois de production » |
| Double emploi méthode/article | matrice dite 2× (mot à mot), ◈◉○ 2×, EDI 2×, clusters 2×, « 5 000-15 000 mots » 2× | fusion : glyphes ✦✧⁅❧ détaillés déplacés dans « La trace » (une seule matrice) ; « symbole noté 0-10 » supprimé ; investigation = mémoire d'abord + manipulation avant faits |
| « 95 % officiel / même rigueur dissident » | tension avec hostilité symétrique ; « 95 %/95 % » extrapolait (le fondateur ne chiffre pas le dissident) | « une suspicion initiale de 95 % sur le récit officiel, et la même grille appliquée au récit dissident » |
| « Un récit = propagande. Cinq récits = cartographie. » sans justification | le « cinq » venait du legacy (« Cinq perspectives croisées pour cartographier ») | « Cinq perspectives croisées : un récit = propagande, cinq récits = cartographie. » |
| « Aucune alarme » | terme obscur | supprimé |
| « Je n'ai pas trouvé d'équivalent » | prétention absolue non prouvable | « Je n'ai pas trouvé, à ma connaissance, d'équivalent » |
| « le protocole s'est en retour affiné » | syntaxe | « la méthode s'est en retour affinée sur ce qu'elle a produit » |
| Voix canonique perdue | « Je cartographie. Vous décidez. » absent de v4/v4b | rétablie en clôture du POURQUOI |
| « 8 M sans médecin », « 3 200 Md€ », « -43 points PISA », « 0,20 % PIB » | ✅ confirmés dans le corpus (articles santé, dette, école) | conservés |
| « 15 clusters » | ✅ 15 fichiers réels dans truth-engine-v2/clusters | conservé |

Résultat final `substack-online/about-page.md` : 1 409 mots, 39 NBSP avant « : »,
17 avant « ; », 0 espace simple avant ponctuation, 0 em-dash, 0 en-dash,
0 double espace. Chiffres : 118 articles, 10 mois, 2,2 M mots de dossiers,
40 symboles codés, 15 clusters, 9 propriétaires 90 % (RSF/Acrimed).

⚠️ Reste à trancher (documenté, non bloquant) : le post #113 absent de l'index
(118 lignes référencées vs 119 numérotés) ; « rapport fondateur » = article
183123537, publié mais absent de l'index local des posts (compté dans les 118 ?).

### 2026-08-02 — v6 : Option A, une page, une voix (retour auteur « moyen »)

L'auteur juge le résultat v5 « moyen ». Audit de structure (pas de style) :

| Défaut diagnostiqué | Manifestation |
|---------------------|---------------|
| Trois documents cousus | manifeste marketing + livre blanc système + manuel de production + confession, sans colonne vertébrale |
| Voix machine sans « je » | première occurrence « Je » à la ligne 90/100 (vérifié par script) |
| Densité technique | 7 symboles de grille + 4 degrés ✦✧⁅❧ + seuils EDI 0,30/0,70/0,80 + 95 % + 6 dimensions dans quelques centaines de mots, contre le design « vulgarisé » |
| Redoublement structurel | « La méthode » (6 blocs) + « Comment un article est écrit » (4 blocs) disent la même chose |
| Exemples ressuscités | L'AMPLEUR = catalogue d'articles (8 M sans médecin, 3 200 Md€, -43 PISA) alors que v4 avait banni les exemples |
| POURQUOI défensif et tardif | « je n'ai pas trouvé d'équivalent » en dernière section, après deux chapitres techniques |

Décision : **Option A, une page, une voix** (`substack-online/about-page.md`).
Le texte « machine » retourne à sa vocation de pièce autonome (page-about/).

Nouvelle structure : tagline canonique en ouverture → constat (9 propriétaires,
90 %, RSF/Acrimed) → **Pourquoi ce blog** (le « je » dès le 2e bloc) → Ce que
vous recevez → S'abonner → **La méthode : l'hostilité symétrique** (une seule
section, 3 symboles de grille Λ Ω €, matrice ✦✧⁅❧, sources stratifiées, 95 %,
cinq perspectives) → Le bilan en chiffres → La trace → Soutenir → Contact →
citation de clôture.

Mesures v6 (script, état final vérifié 2026-08-02) : 751 mots ; 32 NBSP
(23 avant « : », 7 avant « ; ») ; 0 espace simple avant ponctuation ; 0 em-dash ;
0 en-dash ; 0 double espace ; 1 paire de guillemets correctement espacée ;
symboles de grille : Λ Ω € (1 occurrence chacun, Ψ Φ ⚔ ρ absents) ; matrice
✦✧⁅❧ 1 occurrence chacun. Forme canonique retenue : « un récit = propagande,
cinq récits = cartographie » (forme enregistrée au registre v5).

Chiffres : 118 articles, dix mois, 2,2 M mots de dossiers (étiqueté), 40 symboles
(15+17+8), 15 clusters, 9 propriétaires ~90 % (RSF et Acrimed), 95 % de suspicion,
16-30 h (déclaration de l'auteur), 5 000-15 000 mots. Tous vérifiés ou attribués,
conformes à l'audit v5.

### 2026-08-02 — v6b : formulations récupérées de la réponse au commentaire

Retour auteur : la réponse au commentaire « écriture IA innommable » (Nicolas
Bihan, brouillon `outputs/2026-07-29_reponse_lecteur_ecriture_IA_courte.md`)
contient des formulations plus fortes que la page About. Récupérées sans répondre
au commentaire (conforme au design « silence sur les critiques ») :
- « l'humain n'est pas en surveillance passive : il est aux commandes à chaque étape »
- « un modèle de langage livré à lui-même ment, se trompe, flagorne, hallucine »

Mesures re-mesurées après intégration : 751 mots ; 32 NBSP (23 avant « : »,
7 avant « ; ») ; 0 espace simple avant ponctuation ; 0 em-dash ; 0 en-dash.

Le brouillon de réponse a été corrigé (chiffres de l'audit v5 : 25 → dix-neuf
enquêtes documentées, 117/8 mois → 118/dix mois, 16-30 h attribué, sources sans
chiffre contesté) et ses em-dash retirés (488 mots, 19 NBSP, 0 espace simple).

Nouvelle note rédigée : `outputs/2026-08-02_06-09_commentaire-qui-ne-conteste-
rien_ARTICLE.md` (509 mots, 23 NBSP, 0 em-dash, 0 espace simple avant
ponctuation) : le commentaire comme échantillon, syllogisme + analyse par
l'absence, chiffres vérifiés uniquement. ⚠️ à acter : statut de la note
(réponse de commentaire vs article publié) ; le suffixe ARTICLE suppose une
intention de publication qui rompt la posture « la démonstration suffit ».

### 2026-08-02 — v6c : application de la recommandation (architecture vestibule)

Analyse cognitive multi-rôles (éditeur, auditeur forensique, architecte de
conversion, lecteur sceptique, relecteur senior) sur le besoin de la page About.
Verdict : la page est un vestibule à deux étages, pas un manuel ; la conversion
prime, la méthode est subordonnée. Application :

- Ajout d'une référence au texte séparé « La machine qui documente les machines »
  (document de référence du protocole complet) en fin de section méthode.
  Hyperlien à ajouter lors de la publication de ce texte en post.
- La section méthode reste subordonnée : identité → preuve → promesse → CTA d'abord.
- Chiffres conservés dans la page : ensemble vérifié par l'audit v5/v6 (118 articles,
  dix mois, 2,2 M mots de dossiers étiqueté, 40 symboles 15+17+8, 15 clusters,
  9 propriétaires ~90 % RSF/Acrimed, 95 % suspicion, 16-30 h attribué,
  5 000-15 000 mots). Migration complète vers le texte machine = décision auteur,
  optionnelle.
- Mesures v6c (script) : 771 mots ; 34 NBSP ; 0 em-dash ; 0 espace simple avant
  ponctuation. La page est passée de 751 (v6) à 771 mots : les mesures v6c
  surclassent les mesures v6/v6b (l'entrée v6 « état final vérifié » est
  historiquement datée).

⚠️ Page live encore périmée (80 % cinq entreprises, 105 enquêtes, 148 concepts,
19 protocoles, 2,9 M mots) : à remplacer par cette version.

### 2026-08-02 — v7 : texte « machine » préparé pour publication (post)

Le texte machine (`page-about/2026-08-01_22-20_comment-articles-sont-ecrits_
TEXTE-ABOUT.md`) est préparé comme post publiable. Audit chiffres contre les
audits v4/v5 : 6 corrections appliquées (python, NBSP préservés) :

| Chiffre v3 | Verdict | Correction v7 |
|-----------|---------|---------------|
| « compte coordonné de 13 000 » | ❌ vues confondues avec abonnés (audit v4 : 13 500 = VUES) | « 13 500 vues » |
| « Les 30 dernières secondes de BFMTV » | ❌ non sourcé ; index : « Autopsie de 30 minutes de direct », Club BFM du 27 juin 2026 | « Les trente minutes de direct du Club BFM du 27 juin 2026 » |
| « 9 propriétaires contrôlant 90 % » | ⚠️ sans attribution | « environ 90 % (selon RSF et Acrimed) » |
| « 15 familles documentées » | ⚠️ écart (audit : 15 clusters) | « 15 clusters documentés » |
| « 16 à 30 heures de travail » | ⚠️ non attribué | ajout « déclaration de l'auteur, il ne sort d'aucun compteur » |
| « trente révisions » | ⚠️ non attribué | « plus de trente révisions, attestées par le journal de versionnement du dépôt » |

Chiffres vérifiés conservés : 44 minutes, 51 000 abonnés, 5,3 Md€, 4 invités /
3 sans expertise / lieutenant-colonel 21 ans, 40 symboles (15+17+8),
9 sections / 20 faits / 8 faisceaux (14 juillet), 19 investigations Arte,
94 minutes / 30 séquences / 28 timecodes / 3 rapports, 15 passes / 25 corrections /
3 rapports / 6 actes, 5 000-15 000 mots, 95 % suspicion, cinq perspectives.

Titre/sous-titre préparés : « La machine qui documente les machines » /
« Anatomie du protocole qui produit ce blog : pièces, assemblage, contrôle,
défauts connus. »

Mesures v7 (script) : 1 438 mots ; 58 NBSP ; 0 em-dash ; 0 en-dash ; 0 espace
simple avant ponctuation. Prêt à publier comme post.

### 2026-08-02 — v7b : post « machine » publié, hyperlien câblé

Le texte machine est publié sur Substack : https://giak.substack.com/p/machine
(titre affiché « Machine », publié le 2 août 2026 ; horodatage brut JSON-LD
NewsArticle : `2026-08-02T06:32:14+02:00` (CEST), soit `04:32:14Z` en UTC,
converti pour posts.csv ; pas de sous-titre sur la page live). L'hyperlien de la
page About (v6c) a été câblé : « [La machine qui documente les machines](https://giak.substack.com/p/machine) ».
Page About : 771 mots ; 34 NBSP ; 0 em-dash ; 0 espace simple avant ponctuation.

Registres mis à jour :
- index.md : entrée #120 ajoutée en tête du tableau (Machine, 2026-08-02),
  total « Total posts publiés » passé à 119 (cf. note de correction ci-dessous :
  écrit 120 par convention ID max, puis corrigé à 119). Format sans segment
  `— *sous-titre*` (décision : le post live n'a pas de sous-titre, vérifié
  navigateur ; les autres lignes du tableau en portent un).
  Note validation : la ligne statistique a désormais la forme exacte
  `| **Total posts publiés** | **119** (IDs 1-120, #113 absent) |`. Le total a
  d'abord été écrit « 120 » (convention ID max), puis corrigé en 119 pour
  respecter la convention de comptage v5 (118 lignes avant → 119 après un seul
  ajout : progression +1 cohérente). Tout grep antérieur sur
  `| **Total posts publiés** | **120** |` renverra 0.
- posts.csv : ligne ajoutée `machine,2026-08-02T04:32:14.000Z,true,...` (source
  déclarée de l'index, désormais alignée ; 118 lignes). Correction fuseau : la
  valeur brute CEST a d'abord été écrite à tort en `Z`, puis convertie en UTC
  (04:32:14Z).

⚠️ Dérive documentée : la page About v6c affiche « 118 articles publiés »,
chiffre du registre index au 2026-07-31. L'index a désormais un compteur à 120
mais 119 lignes réelles : le post #113 reste absent (audit v5). À trancher avec
l'auteur : conserver le périmètre antérieur ou mettre à jour la page About.
→ Tranché en v8c (2026-08-02) : 119 conservé (convention v5), voir entrée v8c.
  Note : le « compteur à 120 » de cette entrée v7b venait de la convention ID max
  (erronée), écartée au profit de la convention lignes référencées (119).

### 2026-08-02 — v8 : réorganisation page-about + BRAINSTORM fond

Retour auteur : « on a la partie technique et fact check, mais le fond, la
narration, les explications, la pédagogie, ce n'est pas encore ça. on peut faire
largement mieux ». Demande : créer `page-about/machine.md`, ranger
`substack-online/about-draft.md` et `substack-online/about-page.md` dans
`page-about/`, brainstormer plus profondément le contenu.

Réorganisation des fichiers (2026-08-02) :
- `substack-online/about-draft.md` → `page-about/about-draft.md` (git mv,
  historique conservé)
- `substack-online/about-page.md` → `page-about/about-page.md` (non suivi, mv)
- `page-about/machine.md` créé : copie canonique du texte publié
  (2026-08-01_22-20_comment-articles-sont-ecrits_TEXTE-ABOUT.md). C'est le
  fichier de travail de référence pour toute réécriture future du texte
  « machine » ; l'artefact daté TEXTE-ABOUT est figé comme archive de ce qui a
  été publié (ne plus l'éditer, pour éviter deux sources de vérité divergentes)
- Référence à `about-draft.md` dans book/book/audit-apex-v7/01_CORPUS.md
  laissée telle quelle (audit d'archive figé, décrit l'état à une date)

Brainstorm de fond écrit : `page-about/BRAINSTORM.md` (2026-08-02). Contenu :
- Diagnostic : machine décrite jamais montrée ; « pourquoi » manque derrière le
  « quoi » ; « défauts connus » promis au sous-titre jamais listés ; lecteur
  objet pas sujet ; deux questions non traitées (« pourquoi te croire ? »,
  « c'est écrit par une IA ? »)
- Principe directeur : la page comme échantillon (montrer une chaîne de preuve,
  une ligne de matrice, une correction réelle)
- Trois architectures narratives : A parcours du lecteur (questions dans
  l'ordre où il les pose), B démonstration filée (un seul exemple de bout en
  bout), C récit de la contre-machine (histoire de la construction) ;
  combinaison recommandée A + B, voix factuelle de C
- Section manquante : les défauts connus (matière documentée : mémoire limitée
  à 5 résultats, heures déclarées, registre #113 absent, doublons mémoire,
  articles de moindre qualité, quatre systèmes de comptage incompatibles)
- Structure recommandée pour la page About (8 blocs) et questions ouvertes
  (4) : chaîne de démonstration, traitement frontal de la question IA,
  périmètre défauts, partage démo page/machine

⚠️ À trancher avec l'auteur avant toute réécriture : les 4 questions ouvertes
en fin de BRAINSTORM.md, dont la plus importante (question IA : la traiter
frontalement ou continuer à la contourner ?).

### 2026-08-02 — v8b : décisions actées, deux textes réécrits

Décisions validées par l'auteur (ask_user) sur BRAINSTORM.md §7 :
1. Architecture narrative A + B (parcours du lecteur + démonstration filée),
   voix factuelle du « je » ;
2. Question IA traitée frontalement (« Ce blog est écrit avec une IA. Voici
   pourquoi ce n'est pas ce que vous croyez. ») ;
3. Défauts connus publiés (y compris « certains articles sont de moindre
   qualité », déclaration personnelle assumée) ;
4. Chaîne de démonstration : Clichy (deux tweets du 27 juin 2026 à 44 minutes
   d'intervalle, 51 000 abonnés / 13 500 vues, 5,3 Md€ = 4,3 SEDIF-Veolia +
   1 Md€ FMHP ; URL : https://giak.substack.com/p/un-geyser-de-6-metres-a-
   clichy-autopsie) ;
5. Périmètre : démonstration partagée page About + texte machine.

Réécritures appliquées (2026-08-02) :
- `page-about/about-page.md` (vestibule) : structure A+B 8 blocs (constat →
  démonstration Clichy 3 clics → question IA frontale → ce que vous recevez →
  méthode en trois idées → défauts connus → bilan chiffré → trace/soutenir/
  contact/verdict). Bilan : 119 articles publiés (convention v5 : lignes du
  registre index après ajout du post machine #120 ; passage assumé de 118,
  réversible).
- `page-about/machine.md` (dossier) : structure mécanique conservée
  (anomalie → cadrage → matière → réduction → vérification → prix et trace →
  verdict) + section « Les défauts connus » nouvelle qui honore le sous-titre,
  « pourquoi » derrière chaque mécanisme (pourquoi 95 %, pourquoi la mémoire
  avant le web, pourquoi croiser les modèles, pourquoi la matrice), fil
  conducteur Clichy en ouverture.

⚠️ Chiffres : les deux textes utilisent 119 articles (registre index, #113
absent). « 51 000 abonnés » (texte publié) conservé dans les deux textes pour
cohérence (51 831 exacts, audit v4). Tous les autres chiffres viennent des
audits v4/v5/v7 (44 min, 13 500 vues, 5,3 Md€, 9 propriétaires 90 %, 40
symboles 15+17+8, 15 clusters, 95 %, 16-30 h déclarés, 5 000-15 000 mots,
Arte : 94 min / 30 séquences / 28 timecodes / 15 passes / 25 corrections /
3 rapports / 6 actes / 30+ révisions / 19 investigations, 14 juillet :
9 sections / 20 faits / 8 faisceaux).

### 2026-08-02 — v8c : compteur d'articles tranché (119 confirmé)

Décision demandée par l'auteur : confirmer 119 ou revenir à 118 pour la page
About. Vérification forensique du registre :

| Source | État réel | Verdict |
|--------|-----------|---------|
| index.md (registre officiel, convention v5 : lignes référencées) | 119 lignes (IDs 1-120, #113 absent) | ✅ source de référence |
| posts.csv | 118 lignes (header + 117 data), 115 is_published=true | ⚠️ source secondaire incomplète, déjà en retard en v5 (114 publiés vs 118 référencés avant machine) |
| about-page.md | « 119 articles publiés » (ligne 45) | ✅ déjà aligné |
| machine.md | aucun compteur d'articles (section « défauts connus » seulement) | ✅ sans objet |

Décision : **119 articles publiés conservé**. Convention v5 (compter les lignes
référencées de l'index) : 118 lignes avant l'ajout du post machine #120, 119
après (progression +1 cohérente). Le post #113 reste absent de l'index
(numéroté dans la séquence 1-120 mais non référencé) : caveat documenté, sans
impact sur le compteur (convention lignes, pas IDs). posts.csv reste une source
secondaire en retard, documentée comme telle (v5). Aucune modification de texte
nécessaire : about-page.md et machine.md sont déjà à 119.

### 2026-08-02 — v8d : vestibule allégé (892 mots, cible 800-900 atteinte)

Retour reviewer + followup auteur : le vestibule faisait 944 mots, au-dessus de
la cible 800-900 du BRAINSTORM §5. Allègement appliqué (script python, NBSP et
apostrophes préservés) :

- Détail de la matrice ✦✧⁅❧ retiré du vestibule : « du vérifié au spéculatif »
  (le détail des quatre degrés reste dans machine.md, section « La matière »)
- Détail « (15 narratifs, 17 épistémiques, 8 factuels) » retiré du bilan :
  « 40 symboles codés » (le détail reste dans machine.md, section
  « Le cadrage »)
- Redondances supprimées : « Rien n'est présenté comme établi sans l'être »
  (doublon de la règle de la matrice) ; « C'est un outil puissant et
  profondément faillible » (redondant avec ment/se trompe/flagorne/hallucine) ;
  « Et la trace conserve tout : chaque version, chaque correction, chaque
  source » resserré en « La trace conserve tout » (la triple énumération reste
  dans la section « La trace ») ; « l'humain n'est pas en surveillance
  passive » retiré de l'identité (déjà présent dans la section IA, une seule
  occurrence conservée)

Mesures finales v8d (script) : 892 mots ; 30 NBSP ; 0 em-dash ; 0 double
-espace ; 0 espace simple avant ponctuation ; 0 glyphe ✦✧⁅❧ restant dans le
vestibule. Tous les chiffres conservés identiques (119 articles, 2,2 M mots de
dossiers, 40 symboles, 15 clusters, 95 %, 5 000-15 000 mots).

⚠️ À vérifier : le comptage NBSP a baissé (36 → 30) car trois énumérations ont
été supprimées ; aucune régression sur les autres contrôles.

### 2026-08-02 — v8e : relecture voix haute (machine.md), 8 micro-corrections

Relecture voix haute demandée par l'auteur (rythme, transitions, formules) sur
les deux textes v8d. Passe de style indépendante (code-reviewer) + relecture
directe. Résultat : 8 micro-corrections appliquées, toutes dans
`page-about/machine.md` (le vestibule n'a reçu aucune correction : ses seuls
points relevés étaient des échos verbatim assumés) :

1. « exigé plus : plus de » → « exigé davantage : plus de » (jingle « plus :
   plus »)
2. Double compte 19/dix-neuf dans « La réduction » : « mobilisé dix-neuf
   enquêtes antérieures » → « mobilisé des enquêtes antérieures » (le 19 reste
   dans la première occurrence : « croisé 19 investigations existantes »)
3. « soumis à des passes… 15 passes » → « subit des passes… 15 pour »
   (répétition « passes… passes »)
4. « doublons et des entrées de test, reconnus » → « : c'est reconnu »
   (accord ambigu, « reconnus » accolé à « entrées » féminin)
5. « une conclusion plus prudente que le dossier » → « une conclusion trop
   prudente au regard du dossier » (formule elliptique)
6. « un langage symbolique de 40 symboles » → « un langage de 40 symboles »
   (jingle « symbolique… symboles »)
7. « C'est la seule promesse que ce blog ne vous fera pas deux fois » →
   « C'est la seule promesse que ce blog se permet, et il ne la répétera
   pas » (formule ambiguë)
8. Triple « déjà » dans « La matière » : « sources déjà vérifiées » →
   « sources validées »

Observations sans correction (bookends verbatim assumés entre vestibule et
dossier : « on remonte au fait, du fait à la source… », « la différence entre
une affirmation et une chaîne de preuve », « Vous n'êtes pas un citoyen
informé » ; « angles morts » deux fois en écho ; « dossier Arte » ~5× ;
« La trace conserve tout. » en phrase-punch assumée).

Mesures finales v8e (script) : machine.md = 1 786 mots, 76 NBSP, 0 em-dash,
0 double espace, 0 espace simple avant ponctuation ; about-page.md inchangé
(892 mots, 30 NBSP, 0 em-dash). Aucun chiffre altéré.

### 2026-08-02 — v8f : audit APEX de la page About + correction répétition chiffrée

Application du protocole APEX (fourni par l'auteur, archivé dans
`page-about/PROTOCOLE_APEX.md`) à la page About complète (vestibule 892 mots +
dossier 1 786 mots). Audit complet restitué dans
`page-about/2026-08-02_09-07_audit-apex-about_AUDIT.md` (7 livrables :
diagnostic, 3 architectures, comparaison, choix argumenté, texte final,
3 vulnérabilités résiduelles, vérifications documentaires).

Verdict de l'audit : les deux textes v8d/v8e tiennent ; architecture B forensique
confirmée comme dominante (6 critères sur 7), îlot A conservé (la méthode en
trois idées), C écartée. Une seule correction strictement fondée appliquée
(la répétition chiffrée intra-fichier) :

- machine.md, lignes 31 et 41 : « 94 minutes, 30 séquences, 28 timecodes »
  donné deux fois à dix lignes d'intervalle (La matière / La réduction). La
  seconde occurrence allégée : « découpé les 94 minutes du documentaire en
  séquences chronométrées, vérifié chaque timecode » (le 19 investigations et
  les 3 rapports restent uniques ; les 94 minutes restent nommées). Aucun
  chiffre perdu.

Vestibule : aucune modification (892 mots conservés). Bookends verbatim
inter-textes conservés (échos assumés, validés en v8e).

Trois vulnérabilités résiduelles documentées (dans l'audit) : V1 paradoxe
d'ouverture (affirmations-choc non chaînées en tête d'un espace qui promet
« rien sans sa chaîne », assumé comme style de marque) ; V2 la trace n'est pas
adressée (pas de lien vers le dépôt, décision d'auteur requise) ; V3 les
compteurs Arte (15 passes / 30 révisions) non articulés (correction exige une
donnée du journal de versionnement, pas une inférence).

Vérifications documentaires encore nécessaires (liste complète dans l'audit §7) :
relation passes/révisions Arte ; adresse du dépôt + licence réelle (LICENSE
présent à la racine) ; référence précise RSF/Acrimed ; re-confirmation statique
du bilan (119 tranché en v8c, aucun écart relevé).

Mesures v8f (script) : machine.md = 1 786 mots (la substitution est neutre en
tokens : retrait de « 30 » et « 28 », ajout de « les » et « chaque »), 0 em-dash,
0 espace simple avant ponctuation ; about-page.md inchangé (892 mots, 0 em-dash).

### 2026-08-02 — v9 : réécriture complète des deux textes (retour auteur « tu n'as pas appliqué »)

Retour auteur : l'audit APEX restait de la critique, il fallait écrire les pages.
Réécriture complète de `about-page.md` (vestibule) et `machine.md` (dossier)
selon le protocole APEX (`PROTOCOLE_APEX.md`), avec pour étalon la version
ChatGPT fournie par l'auteur : la dépasser, pas la copier.

Apports repris de la version ChatGPT, greffés sur nos forces :

- **Vestibule** : questions systématiques (qui décide, qui paie, qui bénéficie,
  qui supporte les conséquences, qui peut interrompre le mécanisme, pourquoi la
  correction annoncée ne se produit jamais) ; reformulation de la question de
  départ (« qui tire les ficelles ? » → « par quelles règles, incitations,
  dépendances et routines... ») ; distinctions épistémiques intégrées à la
  méthode (4e idée : « La méthode distingue ce que le récit dominant confond ») ;
  section « Pourquoi « Résistance Cognitive » ? » (la première dépossession est
  celle du jugement).
- **Machine** : section « Ce que chaque dossier reconstruit » (8 couches : faits,
  chronologie, acteurs, mécanismes, contradictions, explications concurrentes,
  conséquences, limites) ; section « Ce que la méthode ne confond jamais »
  (6 distinctions, alignées sur le protocole APEX §4 et KERNEL) ; contrat avec
  le lecteur dans le verdict (« Je ne vous demande pas de me croire... ») ;
  « La rigueur n'est ni la prudence systématique ni la radicalité systématique ».

Conservé (nos forces, absentes de la version ChatGPT) : démonstration Clichy
(44 min, 51 000/13 500, 5,3 Md€ = 4,3 + 1), IA frontale (+ « Truth Engine n'est
ni une source, ni un oracle »), défauts connus publiés, trace/dépôt versionné,
chiffres vérifiés (119, 2,2 M, 40 symboles, 15 clusters, 95 %), taglines
canoniques, devise de clôture.

Décisions actées :

- **Longueur** : cible vestibule portée de 800-900 à ~1 100 mots (étalon ChatGPT
  ~1 400, demande auteur « fait mieux ») ; machine à ~2 170 mots.
- **Cohérence distinctions** : vocabulaire aligné entre les deux textes
  (corrélation/causalité, plus de « concomitance ») ; vestibule 5 distinctions
  sans compte annoncé, machine « six distinctions » : pas de contradiction.

Mesures v9b (script) : about-page.md = 1 105 mots ; machine.md = 2 175 mots ;
0 em-dash ; 0 en-dash ; 0 espace simple avant ponctuation ; 0 double espace ;
guillemets équilibrés (4/4 et 2/2) ; chiffres vérifiés conservés ; aucun chiffre
interdit (148, 105, 2,9 M, 80 %, 117, 118, 19 protocoles, 3,2 M).

⚠️ Audit APEX (`2026-08-02_09-07_audit-apex-about_AUDIT.md`) §5 « v8d/v8e
validés en l'état » : dépassé par la réécriture v9 (note de révision ajoutée
en §5 du fichier d'audit, voir le pointeur).

### 2026-08-02 — v9c→v9f : différenciation des deux textes (retour auteur « j'ai l'impression que les textes sont les mêmes »)

Retour auteur : « les textes de about et machine sont les mêmes ». Mesure
objective (script, n-grammes de 6 mots communs) : **147 segments partagés**
entre `about-page.md` et `machine.md`. Diagnostic : en v9, j'avais gonflé le
vestibule avec des blocs entiers du dossier (IA, défauts, trace, bilan, devise
quasi recopiés). Or leurs fonctions sont opposées : le vestibule **convertit**
(pourquoi lire, pourquoi croire, comment s'abonner), le dossier **démontre**
(comment c'est fait, pièce par pièce).

Quatre passes de différenciation, toutes mesurées :

| Passe | Traitement | Segments 6 mots communs |
|-------|-----------|-------------------------|
| v9 | état initial | 147 |
| v9c | vestibule réécrit en texte court et autonome (~850-900 mots visés), le détail reste dans le dossier | — |
| v9d | script 8+8 paires : échos verbatim reformulés dans chaque texte (IA, trace, défauts, contrat, devise de travail) | 32 |
| v9e | 8 échos stylistiques brisés (registre a un trou/comporte une lacune, article long va de/atteint, signaler pas à l'éviter/le cacher, phrase de l'article/de l'article publié) + restauration de la clause « les objections retenues ou écartées » perdue à v9d | 27 |
| v9f | 2 micro-corrections reviewer (retrait « de travail encadré » redondant → « environnement d'investigation » ; virgule au lieu du 2e deux-points dans la phrase des défauts) | 23 |

Résultat final : **23 segments communs, tous factuels ou intentionnels** :
chaîne Clichy (geyser, 51 000/13 500, 5,3 Md€, 27 juin), devise canonique
« Cartographier l'architecture du mensonge institutionnel... » (citée dans les
deux textes), titre « La machine qui documente les machines » (renvoi croisé),
chiffre « 5 000 à 15 000 mots ». Zéro écho stylistique résiduel.

Fonctions désormais distinctes et vérifiées par relecture reviewer :
- `about-page.md` (vestibule, 844 mots) : constat → identité → preuve Clichy →
  IA frontale (ni source ni oracle) → ce que vous recevez → s'abonner → méthode
  en trois idées (95 %, manipulation avant faits, matrice, refus de confondre) →
  défauts publiés → bilan (119, 2,2 M, 40 symboles, 15 clusters) → trace →
  pourquoi « Résistance Cognitive » → soutenir → contact → devise
- `machine.md` (dossier, 2 134 mots) : anomalie → cadrage (40 symboles,
  15 clusters, 95 %) → matière (matrice ✦✧⁅❧, Arte 94 min/30 séquences/
  28 timecodes, 8 couches) → réduction → vérification (15 passes/25 corrections/
  3 rapports) → 6 distinctions → prix et trace → défauts connus → verdict
  (contrat : faits, sources, liens, objections retenues ou écartées, distance
  preuve-conclusion)

Contraintes validées sur les deux fichiers : 0 em-dash, 0 en-dash,
0 espace simple avant ponctuation, 0 double espace, guillemets équilibrés
(3/3 et 2/2), NBSP avant « : » et « ; », apostrophes typographiques.
Chiffres vérifiés conservés (119 articles, 2,2 M, 40 symboles, 15 clusters,
95 %, 44 min, 51 000, 13 500, 5,3 Md€, 16-30 h, 5 000-15 000).

⚠️ Question ouverte pour l'auteur (reviewer, non bloquante) : le bloc
« Qui décide ? Qui paie ? Qui bénéficie ? Qui supporte les conséquences ?
Qui peut interrompre le mécanisme ? » du benchmark ChatGPT a disparu du
vestibule lors du raccourcissement v9c. Le restaurer en version compacte
(une ligne, ~12 mots, budget ~900 mots) est recommandé par la relecture :
c'est un dispositif de conversion propre au vestibule (le dossier ne l'a
jamais porté), sans menace sur la différenciation. À trancher par l'auteur.

### 2026-08-02 — v9g : micro-corrections de relecture finale

Trois points de la relecture finale appliqués sur `page-about/about-page.md` :

1. Micro-défaut de français : « la même suspicion initiale de 95 % sur le
   récit officiel » → « une suspicion initiale de 95 % sur le récit officiel »
   (le « même » pendait sans second terme de comparaison)
2. « Truth Engine n'est ni une source, ni un oracle : c'est un environnement
   d'investigation » (retrait de « de travail encadré », redondant avec
   « l'humain est aux commandes à chaque étape »)
3. Virgule au lieu du 2e deux-points : « certains articles sont de moindre
   qualité, je le dis »

Mesures finales (script) : about-page.md = 843 mots ; machine.md = 2 134 mots ;
0 em-dash ; 0 en-dash ; 0 espace simple avant ponctuation ; 0 double espace ;
guillemets équilibrés (3/3 et 2/2). Chevauchement 6-mots : 23 segments, tous
factuels ou intentionnels (chaîne Clichy, devise, titre, chiffres).

Reste une décision d'auteur (question ouverte ci-dessus) : restaurer ou non le
bloc de questions « Qui décide ? Qui paie ? Qui bénéficie ?... » dans le
vestibule. La relecture recommande la restauration compacte (~12 mots) ;
l'auteur tranche.
→ **Tranché en v9h (2026-08-02) : restauré + CTA renforcé, voir entrée v9h.**

### 2026-08-02 — v9h : décisions auteur (ask_user) appliquées au vestibule

Deux décisions auteur (ask_user, options validées) appliquées à
`page-about/about-page.md` :

1. **Bloc de questions restauré** en une ligne après le constat d'ouverture,
   avant l'identité : « Qui décide ? Qui paie ? Qui bénéficie ? Qui supporte
   les conséquences ? Qui peut interrompre le mécanisme ? ». Ce bloc du
   benchmark ChatGPT avait disparu lors du raccourcissement v9c ; il est
   propre au vestibule (le dossier ne le porte pas), donc sans menace sur la
   différenciation (chevauchement 6-mots inchangé : 23 segments factuels).
2. **CTA S'abonner renforcé** : « Gratuit. Chaque semaine. Aucun engagement.
   Chaque enquête arrive directement dans votre boîte. » (sans répéter
   « Aucun paywall, aucune publicité », déjà dans « Ce que vous recevez »).

Mesures v9h (script) : about-page.md = 870 mots (budget ~850-900 respecté) ;
0 em-dash ; 0 en-dash ; 0 espace simple avant ponctuation ; 0 double espace ;
guillemets équilibrés (3/3) ; NBSP avant « ? » et « : » présentes ; apostrophes
typographiques. machine.md inchangé (2 134 mots).

Répétition intra-texte assumée : « Gratuit » et « Chaque semaine » figurent
chacun deux fois dans le vestibule (« Un article gratuit chaque semaine »
dans Ce que vous recevez + « Gratuit. Chaque semaine. » dans le CTA) :
renforcement rhétorique volontaire de la cadence hebdomadaire, pas un accident.

État final de la passe de différenciation v9c→v9h : deux textes distincts par
la fonction (vestibule convertit, dossier démontre) et par le lexique ;
chevauchement 6-mots = 23 segments, tous factuels ou intentionnels (chaîne
Clichy, devise, titre, chiffres) ; contraintes au vert sur les deux fichiers.

### 2026-08-02 — v9i : relecture voix haute, deux micro-corrections

Relecture voix haute demandée par l'auteur (rythme, transitions, formules)
sur les deux textes v9h. Deux micro-corrections justifiées appliquées :

1. **Précision factuelle (chaîne partagée)** : « un compte coordonné de
   13 500 vues » → « un compte coordonné dont le tweet a cumulé 13 500
   vues », dans les deux textes. Les vues appartiennent au tweet, pas au
   compte (un compte a des abonnés) ; reliquat de la confusion vues/abonnés
   traquée depuis l'audit v4. Chiffres 51 000 et 13 500 inchangés.
2. **Écho intra-vestibule** : « un protocole où l'humain reste aux commandes
   à chaque étape » → « un protocole où l'humain reste aux commandes » (la
   section IA porte déjà « l'humain est aux commandes à chaque étape » ; le
   doublon de 3 mots « aux commandes » restant est un renforcement assumé).

Mesures v9i (script) : about-page.md = 871 mots ; machine.md = 2 138 mots ;
0 em-dash ; 0 en-dash ; 0 espace simple avant ponctuation ; 0 double espace ;
guillemets équilibrés (3/3 et 2/2). Chevauchement 6-mots = 27 segments,
tous factuels (la formule partagée « dont le tweet a cumulé 13 500 vues »
génère 4 segments supplémentaires de la chaîne Clichy : identité factuelle,
pas des échos stylistiques). Relecture reviewer : passe confirmée, un point
de trace aligné (23 → 27) après mesure finale.

## Chiffres à reconfirmer avec l'auteur avant publication

- « 25 enquêtes distinctes » pour l'article Arte : dépôt = 19 (décider du chiffre)
- « 16-30 h minimum » par article : à assumer comme déclaration personnelle ou retirer
- « 2,9 millions de mots » (page live) : corrigé à « plus de 2,2 M » (mesure dépôt) ;
  la page live doit être mise à jour pour refléter le draft
- « 105 enquêtes » (page live) : corrigé implicitement ; la page live doit être mise à jour
- « 19 sources » vs « 32 sources » pour l'article Arte : à trancher

## Rappels

- **Zéro em-dash (—)** dans le corps du texte
- Termes techniques expliqués au premier usage (niveau vulgarisé)
- Silence sur les critiques : la démonstration suffit
- Cohérence avec la page About existante : symboles déjà présentés réutilisables tels quels
- Chiffres ⚠️ : citer comme « publiés sur cette page », jamais comme assertion nouvelle
- Chiffres ❌ : à retirer du texte ou de la page About elle-même
- La diversité des LLM : raconter le croisement des biais (entraînement, harnais,
  contexte système), pas la performance. Preuves : auditor 5 modèles, Arte multi-modèles.
