# PROMPT PELOTE-MINEUR v1.0
## Pipeline de découverte de faits par FIL CAUSAL — dérouler la pelote de laine jusqu'à l'origine du verrou systémique

**Date :** 2026-06-27
**Type :** PROMPT
**Héritage :** FAIT-MINEUR v1.1 (format chroniques, GATES, injection) + Archives Fils REFERENCE + KERNEL v2.0
**Complémentarité :** FAIT-MINEUR remplit les dimensions par période ; PELOTE-MINEUR trace un fil causal sur toute l'histoire
**Périmètre :** 10 fils confirmés (A-H + I + L) × 237 années (1789-2026)

---

## GLOSSAIRE

| Symbole | Concept | Description |
|---------|---------|-------------|
| ◉ | IMPERATIVE | Règle absolue, commande, obligation |
| ◆ | CONSTRAINT | Condition, limite, borne |
| ⊙ | METRIC | Métrique, checklist, mesure |
| △ | PATTERN | En-tête de section, pattern |
| ⟨ ⟩ | FIL CAUSAL | Un fil systémique documenté dans le référentiel |
| ⭐ | ACTE NAISSANCE | Premier verrou qui crée le fil |
| ⟡ | RENFORCEMENT | Moment où le verrou est consolidé |
| ⚡ | MANIFESTATION | Événement qui révèle le mécanisme en action |
| ⊘ | BIFURCATION PERDUE | Occasion manquée de déverrouiller le fil |
| ⟐ | REFERENCE | Renvoi au référentiel des fils |

---

## △ MISSION — PELOTE-MINEUR

### ◉ Objectif

>Tirer la pelote de laine d'un **fil systémique** (⟨Fil G⟩, ⟨Fil B⟩, etc.) à travers toute l'histoire française (1789-2026) pour découvrir les faits qui **révèlent le mécanisme** du verrou.

Contrairement à FAIT-MINEUR qui cherche **tous les faits manquants d'une dimension** (densité chronologique), PELOTE-MINEUR cherche **les faits qui éclairent un mécanisme** (profondeur causale).

### ◆ Différence FAIT-MINEUR vs PELOTE-MINEUR

| FAIT-MINEUR | PELOTE-MINEUR |
|-------------|---------------|
| Cherche par **DIMENSION** (REL, ECO, EDU...) | Cherche par **FIL CAUSAL** (⟨Fil G⟩, ⟨Fil B⟩...) |
| Remplit les trous temporels | Révèle le MÉCANISME du verrou |
| 1 session = 1 dimension × période | 1 session = 1 fil × toute l'histoire (237 ans) |
| Priorité : **complétude** (densité) | Priorité : **puissance explicative** (profondeur) |
| Sortie : lignes chroniques | Sortie : chaîne causale enrichie + lignes chroniques |
| 5-20 faits par session | 10-30 faits par session |
| Vise zéro angle mort | Vise la compréhension du verrouillage |

### ◆ Exemple : ⟨Fil G⟩ — Laïcité comme religion civile

**Question centrale :** « Comment l'État français est-il devenu la seule autorité morale légitime, au point que quand il échoue, personne ne peut le rappeler à l'ordre ? »

**Ne cherche PAS :** tous les faits de la dimension REL (religion)
**Cherche :** les faits qui révèlent le mécanisme G — l'État absorbant, neutralisant ou éliminant les autorités morales concurrentes

| Fait | Pourquoi il compte pour Fil G |
|------|------------------------------|
| 1685 — Révocation Édit de Nantes | L'État affirme qu'aucune autorité morale ne lui échappe |
| 1793 — Culte Être suprême | L'État tente de devenir LUI-MÊME une Église |
| 1905 — Séparation Églises/État | L'État devient seule autorité morale universelle — les Églises sont réduites à la sphère privée |
| 2004 — Loi signes religieux école | L'école publique (État) peut restreindre l'expression religieuse : le citoyen est d'abord un élève de la République |
| 2021 — Loi séparatisme | L'État contrôle les associations cultuelles, les imams, le financement — aucune autonomie morale hors de lui |

Chacun de ces faits **raconte la même histoire** : l'État qui neutralise un concurrent moral. C'est cela, « tirer la pelote de laine ».

---

## △ PHASE 0: LOAD — Charger le fil

### ◆ Charger le référentiel

```text
⟐ REFERENCE : 03_framework/2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md
   → Lire la section du fil ciblé (ex: « Fil G — Laïcité comme religion civile »)
   → Noter : acte de naissance, renforcements documentés, M## associé, chaîne causale, bifurcation perdue

⟐ SYNTHESE : 03_framework/2026-06-26_21-00_synthese_7_enquetes_FRESQUE.md
   → Lire la section du fil (ex: « §2.7 Fil G »)
   → Noter : dans quelles enquêtes le fil est actif, manifestation typique

⟐ ENQUETES : Lire les enquêtes où le fil est actif (mode manifesté)
   → Pour chaque occurrence, noter comment le fil se manifeste dans l'événement
   → Chercher les faits EXISTANTS qui pourraient enrichir la chaîne causale
```

### ◆ Cartographier les faits connus dans les Chroniques

◉ Scanner les fichiers REL (et autres dimensions touchées par le fil) pour identifier les faits qui documentent DÉJÀ le mécanisme :

```text
→ rtk grep -r '^| ' chroniques/ --include '*_REL.md' | rtk head -50
→ Pour chaque fait, se demander : « Ce fait révèle-t-il le mécanisme du fil ? »
→ Si oui → le marquer comme fait PELOTE existant

⊙ Colonnes de cartographie :
   Année | Fait | Rôle dans le fil | Dimension chronique | Code impact
```

### ◆ À l'issue du chargement, le LLM doit pouvoir répondre :

1. Quel est l'acte de naissance du fil ciblé ?
2. Quels sont ses renforcements déjà documentés ?
3. Quelle est la chaîne causale actuelle ?
4. Quelle est la bifurcation perdue ?
5. Quels faits PELOTE existent déjà dans les chroniques ?
6. Quelles enquêtes ont déjà activé ce fil ?
7. **Quels RENFORCEMENTS MANQUENT dans la chaîne ?** (c'est là qu'on va creuser)

---

## △ PHASE 1: GAP CAUSAL — Identifier les maillons manquants

### ◆ Analyser la chaîne causale actuelle du fil

Pour chaque fil, le référentiel documente des renforcements. Mais entre ces renforcements, il y a des **trous** — des périodes où le mécanisme continue d'opérer mais n'est pas documenté.

### ◆ Types de gaps causaux à identifier

| Gap | Description | Exemple Fil G |
|-----|-------------|---------------|
| **Trou temporel** | Période sans renforcement documenté | 1946 → 2004 (58 ans sans renforcement Fil G) |
| **Trou de manifestation** | Événement qui a ACTIVÉ le mécanisme mais n'est pas dans le fil | Discours de Sarkozy au Latran (2007) — « laïcité positive » |
| **Trou d'absorption** | Moment où l'État a absorbé/neutralisé un concurrent moral | Création CFCM (2002) — l'État organise l'islam |
| **Trou de bifurcation** | Alternative qui aurait pu déverrouiller le fil mais a été ignorée | Rapport Stasi (2003) — une vision libérale possible |
| **Trou de M##** | Renforcement qui ajoute un nouveau mécanisme au fil | Loi séparatisme (2021) — M39 Bouclier républicain |

### ◆ Pour Fil G, les gaps probables (exemples) :

```text
Période 1946-2004 : 58 ans sans renforcement
  → 1951 : Loi Marie (financement public écoles privées) — État intègre le concurrent qu'il ne peut éliminer
  → 1959 : Loi Debré (contrat d'association) — absorption des écoles privées dans le service public
  → 1970-1980 : Évolution des pratiques religieuses (pratique catholique en chute libre)
  → 1984 : Manif pour l'école libre (1,5M) — société civile conteste le monopole éducatif
  → 1989 : Affaire du voile de Creil — premier test de la laïcité face à l'islam
  → 2002-2003 : Création CFCM — l'État organise l'islam de France
  → 2003 : Rapport Stasi — vision officielle de la laïcité

Période post-2021 :
  → 2025-2026 : Évolution de la pratique, sécularisation, nouvelles controverses
```

### ◆ Générer 3-5 cibles de recherche

```text
[P1] ⟨Fil G⟩ 1946-2004 : 58 ans sans renforcement — que s'est-il passé ?
[P2] ⟨Fil G⟩ 2007-2021 : laïcité positive → séparatisme — évolution du concept
[P3] ⟨Fil G⟩ 2025-2026 : sécularisation — point d'arrivée de la chaîne
```

---

## △ PHASE 2: CREDO FIL — Questions de recherche ciblées sur le mécanisme

### ◆ Règles de génération

◉ Chaque question doit cibler un **mécanisme spécifique** du fil :
   - Absorption d'une autorité morale concurrente
   - Renforcement du monopole moral de l'État
   - Contestation du monopole (et échec)
   - Hypernormalisation du verrou
   - Manifestation dans un événement

◉ Pas de question qui appelle des faits « généraux » — chaque question DOIT revenir au fil

### ◆ Questions CREDO pour ⟨Fil G⟩ (exemple)

```text
C — Chronologie :
  Quels sont les moments où l'État a absorbé/encadré une autorité religieuse concurrente ?
  (1905 : séparation ; 1926 : Grande Mosquée Paris ; 2002 : CFCM ; 2021 : séparatisme)

R — Ressources :
  Combien l'État dépense pour les cultes ? (budget cultes, Alsace-Moselle, aumôneries)
  Combien pour l'Observatoire de la laïcité ? Combien pour le CFCM ?

E — Preuves :
  Quels rapports officiels documentent la laïcisation de la société française ?
  Rapport Stasi (2003), rapport Machelon (2006), rapport Obin (2012)
  Rapport Sauvé CIASE (2021) — révèle l'échec de l'autorité morale catholique

D — Doute :
  Qui a contesté le monopole moral de l'État ? Avec quels arguments ?
  (FSSPX, Église catholique, islam, protestants, libres penseurs)
  Quelles alternatives à la laïcité française existent dans d'autres pays ?

O — Omission :
  Quels sujets religieux ont été étouffés, tabous, non débattus ?
  (finances du culte musulman, abus dans l'Église avant 2021, prières de rue)

+ — Rhétorique :
  Comment le discours sur la laïcité a-t-il évolué (1905 → 2004 → 2021) ?
  « Laïcité ouverte » → « laïcité positive » → « laïcité de combat » — chaque mot révèle un renforcement
```

---

## △ PHASE 3: SEARCH — Recherche ciblée sur le mécanisme

### ◉ Méthode (identique à FAIT-MINEUR v1.1)

```text
ÉTAPE 1 — @MNEMO_Q (recherche mémoire locale)
  ◉ OBLIGATOIRE : search_memory(query="{fil} {période}", limit=5, search_mode="hybrid")
  ◉ Chercher les mémoires existantes sur le fil
  → BLOCK si cette étape est sautée

ÉTAPE 2 — @WEB (recherche DuckDuckGo)
  ◉ researcher_web(prompt="{question contextualisée}")
  ◉ NOTER l'URL de chaque résultat
  → Après chaque résultat @WEB, chaîner avec @FETCH sur les sources mentionnées

ÉTAPE 3 — @FETCH (lecture d'URL directe)
  ◉ read_url(url="{url}", max_chars=12000)
  ◉ Extraire : faits (date, description, chiffres), citations directes
  → Chaque fait DOIT avoir une URL source — sinon ❧
```

### ◆ Questions de recherche pour ⟨Fil G⟩ — sessions recommandées

```text
Session 1 — 1789-1905 (naissance du verrou)
  @WEB: « Loi 1905 séparation Églises État articles détails débat parlementaire »
  @WEB: « Alsace-Moselle Concordat 1918 1924 maintien droit local cultes »
  @WEB: « Grande Mosquée de Paris inauguration 1926 financement État »
  @WEB: « École laïque Ferry 1881 1882 1886 lois Jules Ferry détails débat »

Session 2 — 1906-2003 (consolidation silencieuse)
  @WEB: « Loi Marie 1951 financement public écoles privées détail »
  @WEB: « Loi Debré 1959 contrat association école privée détails »
  @WEB: « Manifestation école libre 1984 1,5 million Paris Savary détails »
  @WEB: « CFCM création 2002 2003 Conseil Français Culte Musulman Sarkozy »
  @WEB: « Affaire voile Creil 1989 premier débat laïcité islam école »

Session 3 — 2004-2026 (durcissement et contestation)
  @WEB: « Rapport Stasi 2003 laïcité signes religieux synthèse préconisations »
  @WEB: « Loi 15 mars 2004 signes religieux école débat parlementaire détails »
  @WEB: « Discours Sarkozy Latran 2007 laïcité positive racines chrétiennes »
  @WEB: « Loi 11 octobre 2010 interdiction dissimulation visage burqa détails »
  @WEB: « Loi séparatisme 2021 confortant principes républicains détails »
  @WEB: « Observatoire laïcité dissolution 2017 création 2020 »
```

---

## △ PHASE 4: REGISTRY PELOTE — Registre des faits causalement annotés

### ◆ Format — 8 colonnes

```text
Année       : AAAA ou AAAA-AAAA (plage)
Fil         : A/B/C/D/E/F/G/H/I/L
Fonction    : ⭐ acte naissance / ⟡ renforcement / ⚡ manifestation / ⊘ bifurcation perdue
Description : Texte court qui EXPLIQUE le mécanisme (pas seulement la description du fait)
Code        : ✅ / ⚠ / ❌ / 💀
Dimension   : REL/ECO/EDU/... (pour injection dans chroniques)
URL         : URL de la source
Note        : M## associé, enquête liée, lien causal

→ 5 colonnes obligatoires : Année, Fil, Fonction, Description, Dimension
→ 3 colonnes optionnelles : Code, URL, Note
```

### ◆ Règle de description

◉ La description doit **expliciter le lien avec le mécanisme du fil** — pas juste « Loi X votée » mais « Loi X : l'État absorbe l'autorité concurrente Y en... »

| ❌ Mauvais (FAIT-MINEUR) | ✅ Bon (PELOTE-MINEUR) |
|--------------------------|------------------------|
| Loi de séparation 1905 | 1905 : Loi de séparation — l'État ne reconnaît aucun culte, devient seule autorité morale universelle [Fil G ⟡] |
| Affaire du voile Creil 1989 | 1989 : Affaire Creil — premier test : la République peut-elle tolérer un signe religieux dans son école ? [Fil G ⚡] |
| Loi 2004 signes religieux | 2004 : Loi interdisant les signes religieux ostensibles à l'école — l'école républicaine restreint l'expression religieuse, l'élève est d'abord un citoyen [Fil G ⟡] |

### ◆ Critères de sélection des faits

◉ Un fait est candidat PELOTE s'il répond à AU MOINS UN de ces critères :

1. **Révèle le mécanisme** : le fait montre le fil en action (absorption, renforcement, manifestation)
2. **Remplit un trou causal** : le fait connecte deux renforcements existants
3. **Documente une bifurcation** : le fait montre une alternative au verrouillage
4. **Ajoute un M##** : le fait révèle un mécanisme jusqu'ici non documenté pour le fil
5. **Éclaire une enquête** : le fait est utile à une enquête où le fil est actif

### ◆ Contre-sélection

❌ N'inclure PAS les faits qui sont :
- Déjà documentés dans le référentiel du fil (ne pas dupliquer)
- Sans lien clair avec le mécanisme (juste « dans la même dimension »)
- Déjà dans les chroniques (sauf si utile à la chaîne causale)

---

## △ PHASE 5: GATES PELOTE — Vérification de la pertinence causale

### ◆ 8 vérifications AVANT injection

```text
□ GATE-P1 : PERTINENCE FIL
   Le fait révèle-t-il le mécanisme du fil ciblé ?
   → Critère : si on enlève le fait, la compréhension du mécanisme diminue-t-elle ?
   → Si non → exclure (ce n'est pas un fait PELOTE, c'est un fait FAIT-MINEUR)

□ GATE-P2 : FONCTION CAUSALE
   Le fait a-t-il une fonction claire dans le fil ?
   → ⭐ acte naissance / ⟡ renforcement / ⚡ manifestation / ⊘ bifurcation perdue
   → Si pas de fonction identifiable → reporter en FAIT-MINEUR

□ GATE-P3 : DATATION
   Le fait est-il correctement daté (année précise ou plage) ?

□ GATE-P4 : DÉDUPLICATION
   Le fait n'est-il pas déjà dans les chroniques OU dans le référentiel du fil ?

□ GATE-P5 : CHAÎNE CAUSALE
   Le fait s'intègre-t-il dans la chaîne causale du fil, entre quels renforcements ?
   → Noter : se place entre GX et GY

□ GATE-P6 : SOURCAGE
   Le fait a-t-il au moins 1 URL source ?
   → Si ❧ → tenter 1 recherche supplémentaire, puis [HYPOTHÈSE FORTE]

□ GATE-P7 : COHÉRENCE IMPACT
   Le code impact (✅⚠❌💀) est-il cohérent avec la fonction dans le fil ?

□ GATE-P8 : COMPTEUR
   Le compteur du fichier cible sera-t-il correct après injection ?
```

### ◆ Seuils d'acceptation

| Résultat GATES | Action |
|----------------|--------|
| 8/8 ✅ | Injection directe + mise à jour chaîne causale |
| 6-7/8 ✅ | Injection avec notes de correction |
| < 6/8 ✅ | HALTE — retour PHASE 3 |

### ◆ VÉRIFICATION FINALE : la chaîne causale tient-elle ?

◉ Après les vérifications, reconstruire la **chaîne causale enrichie** du fil :

```text
Format :
  ⭐ AAAA — Acte de naissance : description
    → ⟡ AAAA — Renforcement : description
    → ⟡ AAAA — Renforcement : description
    → ⚡ AAAA — Manifestation : description
    → ⟡ AAAA — Renforcement : description
    → ⊘ AAAA — Bifurcation perdue : description
    → ⚡ AAAA — Manifestation : description

◉ Vérifier que la chaîne est continue : pas de saut > 30 ans (sauf si justifié)
◉ Vérifier que chaque maillon a une source
```

---

## △ PHASE 6: INJECT — Écriture dans les Chroniques + Sidecar

### ◆ Deux sorties sont produites

**Sortie 1 — Chroniques** (format AFP, identique à FAIT-MINEUR)

```text
🔶 Pour chaque fait PELOTE, écrire sa ligne dans le fichier chronique de l'année et de la dimension correspondante :

| AAAA | DIM | Description (version courte, comme FAIT-MINEUR) | ❌ |

🔶 Mettre à jour le compteur (> N événement(s))
🔶 Vérifier les doublons avec les faits existants

◉ Charger la PHASE 6 complète de FAIT-MINEUR v1.1 pour la procédure d'injection standard :
   → Format exact des lignes
   → Création de fichier si inexistant
   → Mise à jour du compteur
   → Cas des plages d'années
```

**Sortie 2 — Sidecar du fil** (fichier dédié dans le dossier du fil)

```text
🔶 Créer/mettre à jour le fichier sidecar dans le dossier dédié :
   → 03_framework/pelote/fil_{X}/YYYY-MM-DD_HH-MM_pelote_fil_X_CHAINE_CAUSALE.md
   → OU dans le dossier de l'enquête si le fil est ciblé sur une enquête spécifique :
     02_enquetes/{enquete}/_pelote/pelote_fil_X_CHAINE_CAUSALE.md

🔶 Format du sidecar :
   # PELOTE — ⟨Fil G⟩ : Chaîne causale enrichie
   ## Mise à jour : 2026-06-27
   ## Session PELOTE : N nouveaux faits

   ### Chaîne causale complète (acte → renforcements → manifestations)

   ⭐ 1789 — Révolution : l'État seul maître (référentiel G3)
     → ⟡ 1793 — Culte Être suprême (G4)
     → ⟡ 1801 — Concordat : absorption de l'Église (G5)
     → ⟡ 1880-1905 — Laïcisation : l'État n'a plus de concurrent moral (G6)
     → ⟡ 1905 — Séparation : l'État seule autorité morale (G7)
     → ⟡ 1946 — Préambule : État débiteur universel (G8)
     → ⟡ 1951 — Loi Marie : financement public écoles privées (NOUVEAU)
     → ⟡ 1959 — Loi Debré : absorption des écoles privées (NOUVEAU)
     → ⚡ 1984 — Manif école libre : contestation du monopole (NOUVEAU)
     → ⟡ 2002 — Création CFCM : l'État organise l'islam (NOUVEAU)
     → ⟡ 2004 — Loi signes religieux école (NOUVEAU)
     → ⟡ 2007 — Latran : laïcité positive (NOUVEAU)
     → ⟡ 2010 — Loi burqa (NOUVEAU)
     → ⟡ 2021 — Loi séparatisme : contrôle renforcé des cultes (NOUVEAU)
     → ⚡ 2025 — Sécularisation : 50% sans religion (NOUVEAU)

   ### Bifurcations perdues documentées

   ⊘ 1905 — Créer des autorités morales concurrentes (référentiel)
     ⊘ 2003 — Suivre le rapport Stasi dans sa vision libérale
     ⊘ 2012 — Dissoudre l'Observatoire de la laïcité sans le remplacer

   ### Nouveaux mécanismes identifiés

   M39 (Bouclier républicain) présent dans loi séparatisme 2021

   ### Gaps restants

   [GAP] 1946-2004 : 58 ans — besoin de renforcements supplémentaires
   [GAP] Impact de Vatican II (1962-1965) sur la laïcisation française
```

---

## △ PHASE 7: MEMORY — Sauvegarde Mnemolite [OBLIGATOIRE]

### ◉ Règle : MEMORY est OBLIGATOIRE — ne pas terminer sans

### ◆ Après chaque session, indexer les découvertes

```text
write_memory(
    title="PELOTE: ⟨Fil {X}⟩ — {N} nouveaux faits, chaîne causale enrichie",
    content="Résumé de la session PELOTE : fil, période, nouveaux faits, maillons ajoutés, gaps restants",
    memory_type="investigation",
    tags=["pelote_mineur", "{fil}", "chaine_causale", "chroniques"]
)
```

### ◆ Informations à conserver

- Fil ciblé et période couverte
- Nombre de nouveaux faits (et fonction : ⟡ / ⚡ / ⊘)
- Chaîne causale avant/après (résumé)
- Nouveaux M## identifiés pour le fil
- Gaps restants pour les sessions futures
- Bifurcations perdues découvertes

---

## △ APPENDICE A: Les 10 fils — cibles PELOTE

| Fil | Nom | Acte naissance | M## | Sessions recommandées |
|:---:|-----|:--------------:|:---:|----------------------|
| **A** | Mandarinat médical | 1803 | M27 | 1803-2026 — monopole médical, ordre, CHU |
| **B** | Monopole d'État | 1791 | M05 | 1791-2026 — Le Chapelier → nationalisations → Maastricht |
| **C** | Société civile atrophiée | 1791 | M14 | 1791-2026 — Le Chapelier → associations → pas de class action |
| **D** | Justice domestiquée | 1804 | M02 | 1804-2026 — Code civil → CJR → impunité des élites |
| **E** | Presse sans contre-pouvoir | 1811 | M10 | 1811-2026 — censure → ORTF → Bollorisation |
| **F** | École-moule | 1808 | M26 | 1808-2026 — Université → Ferry → Haby → PISA |
| **G** | Laïcité religion civile | 1789 | M37 | **1789-2026 — priorité** — séparation → absorption cultes |
| **H** | Exceptionnalisme | 1660 | M32 | 1660-2026 — Colbert → gaullisme → déclin compensé |
| **I** | Vassalité monétaire | 1992 | M43 | 1983-2026 — virage → Maastricht → TSCG → COVID |
| **L** | Fiscalité asymétrique | 1914 | M47 | 1914-2026 — IR → Sécu → ISF supprimé → flat tax |

---

## △ APPENDICE B: Fil G — Cartographie initiale

### Faits déjà dans le référentiel (NE PAS DUPLIQUER)

| # | Date | Fait | Fonction |
|---|------|------|----------|
| G1 | 1562-1598 | Guerres de religion : l'État sort vainqueur | Pré-acte |
| G2 | 1685 | Révocation Édit de Nantes | Pré-acte |
| G3 | 1789 | Révolution : DDHC — l'État seul maître | ⭐ Acte de naissance |
| G4 | 1793-1794 | Culte de l'Être suprême | ⟡ Renforcement |
| G5 | 1801 | Concordat : Napoléon encadre l'Église | ⟡ Renforcement |
| G6 | 1880-1905 | Laïcisation républicaine (Ferry, expulsions congrégations) | ⟡ Renforcement |
| G7 | 1905 | Loi de séparation des Églises et de l'État | ⟡ Renforcement majeur |
| G8 | 1946 | Préambule Constitution : État débiteur universel | ⟡ Renforcement |

### Enquêtes où Fil G est actif

| Enquête | Degré | Manifestation |
|---------|:-----:|---------------|
| Sang contamine (1984-2003) | 3/5 | La parole des experts est indiscutable |
| Tchernobyl (1986) | 2/5 | Pellerin = autorité morale indiscutable |
| Pétition 69 (1977-2020) | 3/5 | L'intellectuel est une autorité morale |
| COVID (2020-2023) | 3/5 | Le conseil scientifique = autorité morale |
| Mazan (2024) | 2/5 | La parole de la victime inférieure à la preuve technique |

### Chroniques REL existantes (instantané au 27/06/2026)

◉ Au moment de la rédaction : ~93 événements dans ~65 fichiers REL
◇ **→ Ne PAS utiliser ce chiffre en dur — charger les fichiers pour le comptage actuel**
→ Charger avant toute session pour éviter les doublons

→ Commande : `grep -rh '^| [0-9]' chroniques/ 2>/dev/null | grep '| REL ' | wc -l`

---

## △ APPENDICE C: Liens avec FAIT-MINEUR

### Quand utiliser quel protocole ?

| Situation | Protocole |
|-----------|-----------|
| Une dimension a < 50 événements sur 237 ans | FAIT-MINEUR (remplir la dimension) |
| Un fil causal doit être exploré sur toute l'histoire | PELOTE-MINEUR (tracer le mécanisme) |
| Après une session FAIT-MINEUR sur REL → extraire les faits qui révèlent Fil G | PELOTE-MINEUR (analyser les résultats) |
| Après une session PELOTE-MINEUR sur Fil G → injecter les faits dans les chroniques | FAIT-MINEUR PHASE 6 (écriture) |
| Session mixte : 50% remplissage dimension + 50% traçage d'un fil | Les DEUX (séquentiel) |

### Ordre recommandé

#### Scénario A — La dimension est déjà remplie (ex: REL = 93 événements)

```text
1. FAIT-MINEUR (déjà exécuté) → réservoir de faits disponible
2. PELOTE-MINEUR → extraire les faits causalement importants du réservoir
3. PELOTE-MINEUR → chercher les faits manquants spécifiques au fil
4. PELOTE-MINEUR → mettre à jour la chaîne causale
```

#### Scénario B — Départ ex-nihilo sur un fil inexploré

```text
1. PELOTE-MINEUR → tracer le fil causal sur toute l'histoire
2. FAIT-MINEUR sur les dimensions → remplir les trous temporels
3. PELOTE-MINEUR → enrichir la chaîne causale avec les nouveaux faits
```

#### Scénario C — Session mixte

```text
1. PELOTE-MINEUR → identifier les faits-clés du mécanisme
2. FAIT-MINEUR → chercher et injecter les faits dans les chroniques
3. Revenir à PELOTE-MINEUR → mettre à jour la chaîne causale
```

---

## △ APPENDICE D: Pièges spécifiques PELOTE

| Piège | Solution |
|-------|----------|
| Confondre « fait de la dimension REL » avec « fait qui révèle Fil G » | Re-questionner : « Ce fait raconte-t-il l'histoire du monopole moral de l'État ? » |
| Ajouter trop de faits sans lien causal | Maximum 20-25 faits par session — prioriser les faits à haute puissance explicative |
| Dupliquer le référentiel | Charger le référentiel AVANT de chercher — ne pas réinjecter G1-G8 |
| Oublier les bifurcations perdues | Chaque session doit documenter AU MOINS 1 bifurcation perdue |
| Négliger les contre-exemples | Si le fil dit X, chercher au moins 1 fait qui dit non-X (résistance, alternative) |
| Surcharger la chaîne causale | Une chaîne de 8-15 maillons est optimale — au-delà, le fil devient confus |
| Ignorer les autres dimensions | Fil G s'exprime aussi dans EDU (école), JUR (justice), POL (politique) |

---

*PELOTE-MINEUR v1.0 — 2026-06-27*
*Héritage : FAIT-MINEUR v1.1 (format chroniques, GATES, injection) + Archives Fils REFERENCE + KERNEL v2.0*
*Complémentarité : FAIT-MINEUR = complétude dimensionnelle / PELOTE-MINEUR = profondeur causale*
*Session pilote recommandée : ⟨Fil G⟩ — Laïcité comme religion civile (1789-2026)*
