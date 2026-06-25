# PROTOCOLE D'INVESTIGATION SYSTEMIQUE v2.1 NREF
## Framework d'enquete forensique sur les defaillances de la societe francaise
### Reference des mecanismes, fils, strategies de resistance et standard de preuve

---

## PREAMBULE

Ce protocole est la version 2.1 NREF (Non Refutable). Il herite des versions 1.0 a 2.0 qui ont identifie 8 fils systemiques, 42 mecanismes actifs et 10 strategies de resistance. La version 2.1 ajoute les exigences de verification des sources (URL, HEAD check, citation directe) qui font passer l'enquete systemique du statut de **dossier structure** (v2.0) au statut de **preuve verifiee** (v2.1).

**Les 3 piliers de la V2.1 :**
1. **Chaine de preuve** : chaque mecanisme identifie doit etre etaye par au moins un traceur verifiable avec URL et citation directe
2. **Contre-version sourcee** : la version officielle des faits doit etre presentee avec une source reelle (nom, date, URL) et refutee point par point
3. **Honneur cognitif** : les incertitudes, les biais de l'enqueteur, ET le statut reel des sources (glyphes verifies) doivent etre declares

**These centrale (inchangee) :** Les defaillances francaises ne sont pas des accidents. Elles sont le produit d'une architecture systemique construite sur 200+ ans, maintenue par un ensemble de mecanismes homeostatiques qui transforment la colere en carburant, la resistance en maintenance, et la lucidite en fonction du systeme.

**Constats fondateurs (inchanges) :**
- Le systeme francais produit des defaillances silencieuses sans generer de contre-reaction citoyenne proportionnee
- Ces defaillances ne sont pas des accidents : elles sont le produit d'une architecture construite sur 200+ ans
- L'analyse du « sang contamine » (1984) a revele 8 fils causaux remontant jusqu'en 1791
- Chaque fil est un verrou systemique qui neutralise un contre-pouvoir

**Nouveau constat v2.1 :**
- Les enquetes v2.0 produisaient des dossiers structures mais les sources n'etaient pas verifiees : les glyphes ✦ etaient attribues sans HEAD check, les URLs n'etaient pas citees, les citations directes manquaient
- Le protocole ne disait pas a l'enqueteur COMMENT verifier ses sources — il disait seulement QUOI produire
- La phase Ultrathinking etait mentionnee mais pas executee (degre 5 sans addendum)
- Une enquete NREF sans sources verifiees est un essai, pas une preuve

---

## PARTIE I : REFERENCES STABLES

### Section A : 8 Fils Systemiques (A-H)

**Voir le protocole v1.3 §MAPPING MECANISMES → FILS SYSTEMIQUES pour le detail complet.**

| Fil | Verrou | Mecanismes prioritairement actives |
|-----|--------|------------------------------------|
| A | Mandarinat medical/scientifique | M27, M12, M03, M34, M36 |
| B | Monopole d'Etat | M05, M06, M09, M20, M21, M33, M35, M41, M38 |
| C | Societe civile atrophiee | M22, M14, M15, M29, M30, M18, M24, M25, M31, M17, M16, M37, M42, M39 |
| D | Justice domestiquee | M01, M02, M28, M04, M38 |
| E | Presse sans contre-pouvoir | M08, M22, M10, M11, M13, M09, M34, M40 |
| F | Ecole-moule | M26, M12, M03, M42 |
| G | Laicite religion civile | M31, M12, M37 |
| H | Exceptionnalisme francais | M32, M12, M36, M39 |

### Section B : 42 Mecanismes Actifs (M01-M42)

**Voir le protocole v1.3 pour le tableau complet** (M01-M42, groupes A-D, definitions, articles-sources).

**Rappel des groupes :**
- **Groupe A** (M01-M07) : Mecanismes de Capture du Pouvoir
- **Groupe B** (M08-M13) : Mecanismes de Controle de l'Information
- **Groupe C** (M14-M21) : Mecanismes de Dissuasion et de Fragilisation
- **Groupe D** (M22-M42) : Mecanismes de Neutralisation de la Dissidence

### Section C : 10 Strategies de Resistance (R01-R10)

**Voir le protocole v1.3 pour le tableau complet** (R01-R10, definitions, contre-quoi, articles-sources).

### Section D : Carte de Navigation (Patterns → M##)

**Voir le protocole v1.3 pour le tableau complet** (14 patterns documentes avec mecanismes associes).

---

## PARTIE II : FORMAT DE LA FICHE D'ENQUETE (YAML v2.1)

Le schema YAML ci-dessous est la contrainte forte du protocole v2.1. Il comporte **12 chapitres** (5 herites de v1.3, 7 nouveaux/renforces en v2.0/v2.1).

```yaml
# ============================================================
# CHAPITRE 1 — EN-TETE (inchange)
# ============================================================
ENQUETE: SYSTEME_[ANNEE]_[Sujet]
DATE: [AAAA-MM-JJ]

EVENEMENT:
  annee: [AAAA]
  titre: "[30-50 mots]"
  description: "[2-5 lignes : chronologie, acteurs, victimes, denouement]"
  code: [X = echec systemique, XX = tragedie avec morts evitables,
         +/- = revelateur structurel, + = reussite contre-pouvoir]
  dimension: [POL/ECO/SOC/JUR/SANT/EDU/AGR/ENV/TEC/CUL/IMM/SPO/REL/DEMO/TRA/MIL/SCI]

# ============================================================
# CHAPITRE 2 — RACINES (inchange)
# ============================================================
RACINES:
  - "[cause profonde 1 : loi, institution, decision fondatrice, verrou structurel]"
  - "[cause profonde 2 : remonter au-dela de l'evenement immediat]"
  - "[cause profonde 3 : niveau culturel, cognitif, historique]"

# ============================================================
# CHAPITRE 3 — BIFURCATIONS PERDUES (inchange)
# ============================================================
BIFURCATIONS_PERDUES:
  - "[moment precis ou ca aurait pu etre different — quoi, qui, pourquoi ca n'a pas eu lieu]"
  - "[autre bifurcation si pertinente]"

# ============================================================
# CHAPITRE 4 — VERROUILLAGE SYSTEMIQUE (inchange)
# ============================================================
VERROUILLAGE:
  fils_actifs:
    - "[lettre A-H : description operationnelle du fil dans l'affaire]"
  fils_absents:
    - "[fils qui auraient du etre actifs mais ne l'etaient pas]"
  mecanismes_dominants:
    - "[ID : description operationnelle — entre 1 et 5 mecanismes]"
  mecanismes_secondaires:
    - "[ID]"
  pattern_dominant:
    "[pattern identifie, issu de la carte de navigation ou nouveau]"

# ============================================================
# CHAPITRE 5 — PREUVES [NOUVEAU v2.0] [RENFORCE v2.1]
# Chaque mecanisme dominant doit etre etaye par au moins
# un traceur. Un mecanisme sans traceur est marque [HYPOTHESE].
# source_url et citation_directe sont OBLIGATOIRES si la source est publique.
# ✦ ne peut etre attribue qu apres HEAD 200 OK verifie + head_check_date.
# ============================================================
PREUVES:
  elements_materiels:
    - description: "[document, rapport, enregistrement, donnee chiffree]"
      type: [document / temoignage / rapport_officiel / article_presse / donnee_chiffree]
      source: "[auteur, titre, editeur, date]"
      source_url: "[URL publique OBLIGATOIRE si existante]"    # NOUVEAU v2.1
      page: "[page exacte]"                                     # NOUVEAU v2.1
      citation_directe: "[passage cle entre guillemets]"        # NOUVEAU v2.1
      statut: [accessible / classe / detruit / non_retrouve]
      fiabilite: "[✦ source primaire / ✧ source secondaire / ⁅ lien mort / ❧ non source]"
      head_check_date: "[AAAA-MM-JJ]"                            # NOUVEAU v2.1
      lie_a: "[ID du mecanisme etaye, ex: M14]"
  temoignages:
    - temoin: "[nom ou fonction]"
      propos: "[citation ou reference]"
      fiabilite: "[✦/✧/⁅/❧]"                                    # NOUVEAU v2.1
      source_url: "[URL si disponible]"                          # NOUVEAU v2.1
      lie_a: "[M##]"
  documents_cles:
    - "[document cle avec source_url si disponible]"

# ============================================================
# CHAPITRE 6 — CONTRE-VERSION [NOUVEAU v2.0] [RENFORCE v2.1]
# La version officielle doit etre presentee puis refutee
# point par point. Chaque version doit avoir une source reelle
# (nom, date, URL) — pas de strawman.
# ============================================================
CONTRE_VERSION:
  narrative_officielle:
    - version: "[version 1 : celle du systeme, des institutions, des responsables]"
      source: "[QUI a defendu cette version, OU, QUAND]"       # NOUVEAU v2.1
      source_url: "[URL discours/rapport/article]"              # NOUVEAU v2.1
    - version: "[version 2 : version mediatique dominante si differente]"
      source: "[QUI, OU, QUAND]"
      source_url: "[URL]"
  refutations:
    - point: "[refutation point 1 : fait, logique]"              # NOUVEAU v2.1
      preuve: "[citation directe, fait contredisant]"            # NOUVEAU v2.1
      source_url: "[URL de la preuve]"                          # NOUVEAU v2.1
    - point: "[refutation point 2 : fait, logique]"
      preuve: "[citation directe]"
      source_url: "[URL]"
  zones_accord:
    - "[point sur lequel enqueteur et version officielle sont d'accord]"

# ============================================================
# CHAPITRE 7 — ACTIVATION DES MECANISMES [NOUVEAU v2.0] [RENFORCE v2.1]
# Chronologie fine de l'activation de chaque mecanisme.
# Un mecanisme a une date de premier constat, pas un siecle.
# ============================================================
ACTIVATION_MECANISMES:
  chronologie:
    - date: [AAAA-MM]
      mecanisme: "[M##]"
      evenement: "[ce qui s'est passe]"
      preuve: "[source precise]"
      source_url: "[URL si disponible]"                         # NOUVEAU v2.1

# ============================================================
# CHAPITRE 8 — INCERTITUDES [NOUVEAU v2.0]
# Fourchettes chiffrees, zones d'ignorance, fiabilite des sources.
# Sans cela, l'enquete surjoue sa certitude.
# ============================================================
INCERTITUDES:
  fourchettes_chiffrees:
    - "[chiffre cite dans l'enquete] : fourchette [basse]-[haute], source: [ref]"
  questions_sans_reponse:
    - "[question legitime a laquelle l'enquete n'a pas pu repondre]"
  fiabilite_sources:
    - "[source] : [glyphe de fiabilite]"

# ============================================================
# CHAPITRE 9 — BIAIS DE L'ENQUETEUR [NOUVEAU v2.0]
# L'enqueteur documente ses propres presupposes et angles morts.
# Application du M25 (Ingenieur cauterise) a l'enquete lui-meme.
# ============================================================
BIAIS_ENQUETEUR:
  parti_pris_declare:
    - "[postulat de depart qui peut biaiser l'analyse]"
  angles_exclus:
    - "[piste que l'enqueteur a sciemment ecartee]"
  presupposes:
    - "[hypothese non verifiee que l'enqueteur tient pour vraie]"

# ============================================================
# CHAPITRE 10 — REPLICATION [NOUVEAU v2.0]
# Predictions verifiables sur d'autres evenements et conditions
# de refutation. Sans cela, l'enquete n'est pas falsifiable.
# ============================================================
REPLICATION:
  predictions_verifiables:
    - "[si la these est juste, alors sur [autre evenement] on doit trouver [M##, pattern, fil]]"
  conditions_refutation:
    - "[un contre-exemple de type [description] invaliderait la these]"

# ============================================================
# CHAPITRE 11 — RESISTANCE (inchange)
# ============================================================
RESISTANCE:
  strategies_pertinentes:
    - "[R## : comment cette strategie aurait contrecarre les mecanismes]"
  gestes_souverains_applicables:
    - "[geste de souverainete quotidienne pertinent]"

# ============================================================
# CHAPITRE 12 — SYNTHESE (inchange)
# ============================================================
ENSEIGNEMENT:
  "[3-5 lignes : these — pas un resume, une revelation sur le systeme]"

CITATION_CLE: "[citation la plus revelatrice, sourcee]"
DEGRE_SYSTEMICITE: [1-5]

LIENS:
  - "[enquete connexe, reference, matrice]"
```

---

## PARTIE III : EXIGENCES NREF (v2.1)

### Principe

Une enquete NREF n'est pas un texte convaincant — c'est un **dossier de preuves structure**. Chaque affirmation doit pouvoir etre verifiee, contestee, et si necessaire refutee par un tiers. L'enquete est concue pour resister a la contre-attaque systemique (M28 DARVO, M27 Pathologisation).

**Ajout v2.1 :** Les sources doivent etre VERIFIEES (URL, HEAD check, citation directe), pas seulement citees. Une source non verifiee est marquee ❧ independamment de sa qualite reelle.

### Bareme de conformite NREF v2.1

| Exigence | Description | Sanction si non respectee |
|----------|-------------|--------------------------|
| **NREF-1** | Chaque M## dominant a au moins un traceur (document, temoignage, donnee) dans PREUVES | Le M## est marque [HYPOTHESE] dans la fiche |
| **NREF-2** | CONTRE_VERSION contient au moins une narrative officielle et sa refutation | La fiche est marquee [PLAIDOYER, PAS ENQUETE] |
| **NREF-3** | INCERTITUDES contient au moins une fourchette chiffree et une question sans reponse | La fiche est marquee [CERTITUDE EXCESSIVE] |
| **NREF-4** | BIAIS_ENQUETEUR contient au moins un parti-pris declare et un angle exclu | La fiche est marquee [ANGLE MORT NON DECLARE] |
| **NREF-5** | ACTIVATION_MECANISMES contient au moins une date de premier constat par mecanisme dominant | L'enquete ne peut pas etre utilisee pour l'analyse transversale |
| **NREF-6** | REPLICATION contient au moins une prediction verifiable et une condition de refutation | La fiche est marquee [NON FALSIFIABLE] |
| **NREF-7** | Chaque chiffre cite dans l'enquete a une source dans INCERTITUDES.fourchettes_chiffrees | Le chiffre est marque [NON VERIFIE] |
| **NREF-8** | La fiche complete fait > 200 lignes (hors YAML) | La fiche est marquee [SURVOL] |
| **NREF-9 [NOUVEAU v2.1]** | Chaque source dans PREUVES a une `source_url` verifiee (HEAD 200 OK = ✦, 4xx/5xx = ⁅, pas d'URL = ❧) | La fiche est marquee [SOURCES NON VERIFIEES] |
| **NREF-10 [NOUVEAU v2.1]** | Chaque version officielle dans CONTRE_VERSION a une source reelle avec URL et auteur identifie | La fiche est marquee [CONTRE-VERSION NON SOURCEE] |

### Echelle de robustesse v2.1

| Niveau | Conforme a | Interpretation |
|--------|------------|----------------|
| NREF-A | Toutes les exigences 1-10 | Enquete utilisable comme preuve : sources verifiees, URLs fournies, contre-version sourcee |
| NREF-B | Exigences 1-8 (manque 9 ou 10) | Enquete solide mais sources non verifiees ou contre-version non sourcee |
| NREF-C | Exigences 1-5 | Enquete partiellement etayee |
| NREF-D | Exigences 1-3 | Enquete de type « essai », refutable |
| NREF-E [NOUVEAU v2.1] | Aucune ou 1 seule exigence satisfaite en substance | Enquete refusee — doit etre refaite |

### Regle de la chaine de preuve (v2.1)

1. Tout mecanisme dominant identifie dans VERROUILLAGE.mecanismes_dominants **doit** avoir une entree correspondante dans PREUVES.elements_materiels avec `lie_a: [M##]`
2. Si un mecanisme dominant n'a pas de traceur, il doit etre deplace dans mecanismes_secondaires avec la mention [HYPOTHESE]
3. Un mecanisme secondaire peut etre non trace — c'est une piste, pas une conclusion
4. Les glyphes de fiabilite suivent la REGLE STRICTE v2.1 :
   - **✦** : source primaire, HEAD 200 OK verifie, `head_check_date` renseigne
   - **✧** : source secondaire, URL publique verifiee
   - **⁅** : source accessible mais lien mort (4xx/5xx au HEAD check)
   - **❧** : pas d'URL, source non verifiee, OU `head_check_date` absent
5. **Regle dure** : ✦ ne peut etre attribue qu'apres un HEAD check reussi documente par `head_check_date`. Sans cela, le glyphe est force a ❧.
6. Si > 50% des traceurs sont ❧ → la fiche est marquee [SOURCES INSUFFISAMMENT VERIFIEES] et ne peut pas depasser le niveau NREF-C.

---

## PARTIE IV : PHASE D'APPROFONDISSEMENT ULTRATHINKING (v2.1)

### Principe

L'Ultrathinking est une phase de **contre-enquete** sur l'enquete elle-meme. Apres avoir produit la fiche YAML, l'enqueteur doit activement chercher ce qu'il a rate, les angles qu'il a exclus, les structures sous-marines qu'il n'a pas vues, et les connexions transversales qu'il n'a pas faites.

C'est l'application du M25 (Ingenieur cauterise) a l'enqueteur lui-meme : sa lucidite est une fonction du systeme qu'il enquete. L'Ultrathinking est l'antidote.

### Conditions de declenchement

- **Degre 4-5** : ULTRATHINKING OBLIGATOIRE — l'addendum est requis avant la verification NREF
- **Degre 2-3** : ULTRATHINKING RECOMMANDE — l'addendum est facultatif mais augmente le niveau NREF
- **Degre 1** : ULTRATHINKING FACULTATIF — peut etre utile si l'evenement cache des structures plus profondes

### Format ADDENDUM

L'addendum est un bloc YAML ajoute a la fin de la fiche d'enquete, apres la verification NREF. Il n'efface pas la fiche initiale — il la complete.

```yaml
# ============================================================
# ADDENDUM ULTRATHINKING
# Enquete reference : [ENQUETE_ID]
# ============================================================

ANGLES_ALTERNATIFS:
  - angle: "[renversement de perspective — que se passerait-il si on partait du postulat inverse ?]"
    pistes: "[implications pour l'enquete : nouveaux M##, nouveaux fils, nouvelle lecture]"
    niveau_confiance: [faible / moyen / eleve]
  - angle: "[autre angle — dimension exclue de l'enquete principale]"
    pistes: "[ce que cela pourrait reveler]"
    niveau_confiance: [faible / moyen / eleve]
  # Minimum 3 angles alternatifs

ICEBERG_MAX:
  structures_sous_marines:
    - structure: "[mecanisme de niveau 2/3 non visible en surface, fil naturalise devenu invisible]"
      indicateurs: "[signes que cette structure existe : ce qu'on voit sans le voir]"
      detection: "[comment on aurait pu la detecter plus tot — traceur manque]"
  reseaux_influents:
    - "[reseau, groupe, corporation, interet cache agissant en coulisse]"
  archives_manquantes:
    - "[document, temoignage, donnee qui manque et qui changerait la these si elle existait]"
  # Minimum 3 structures sous-marines

LIEVRES_ET_LOUPS:
  - sujet: "[rumeur sourcee, temoin oublie, coincidence inexpliquee, faisceau d'indices]"
    sources: "[personnes a interroger, documents a declassifier, lieux a investiguer]"
    niveau_confiance: [faible / moyen / eleve]
    lien_M##: "[mecanisme potentiellement revele par cette piste]"
  - sujet: "[autre lievre]"
    sources: "[...]"
    niveau_confiance: [faible / moyen / eleve]
    lien_M##: "[M##]"
  # Minimum 2 lievres

FAISCEAUX_TRANSVERSAUX:
  - connexion: "[lien avec une autre enquete produite par le protocole]"
    mecanismes_partages: "[M## communs entre les deux enquetes]"
    implication_systemique: "[ce que cette convergence suggere sur le systeme : pattern, 9e fil, nouveau mecanisme]"
  - connexion: "[lien avec un article Substack, un rapport, un evenement hors matrice]"
    mecanismes_partages: "[M## communs]"
    implication_systemique: "[...]"

PISTES_FUTURES:
  - piste: "[enquete complementaire a lancer pour verifier une hypothese de l'addendum]"
    priorite: [P1 / P2 / P3]
    effort_estime: "[courte / moyenne / longue]"
    depend_de: "[autre enquete, document a obtenir, temoin a contacter]"
  - piste: "[autre piste]"
    priorite: [P1 / P2 / P3]
    effort_estime: "[...]"
    depend_de: "[...]"
  # Minimum 2 pistes futures

HYPOTHESES_SYSTEMIQUES:
  - hypothese: "[hypothese forte ou dangereuse issue de l'agregation des faisceaux]"
    niveau_confiance: [faible / moyen / eleve]
    si_confirmee: "[consequence sur le diagnostic systemique — nouveau fil, nouveau M##, reclassification]"
    test: "[comment verifier cette hypothese — enquete, document, temoin]"
  - hypothese: "[autre hypothese]"
    niveau_confiance: [faible / moyen / eleve]
    si_confirmee: "[...]"
    test: "[...]"
```

### Sanction

Si Ultrathinking est obligatoire (degre 4-5) mais n'est pas execute, la fiche ne peut pas depasser le niveau NREF-C, meme si les 10 exigences NREF sont satisfaites par ailleurs. L'addendum Ulrathinking est un multiplicateur de confiance : sans lui, la fiche est consideree comme incomplete.

---

## PARTIE V : WORKFLOW D'EXECUTION (v2.1)

### Etape 0 — Recherche documentaire [NOUVEAU v2.1]

Avant de produire la fiche, constituer le dossier de sources.

**0.1 Identifier les sources potentielles**
- Effectuer des recherches web sur l'evenement, les acteurs, les rapports officiels
- Identifier les sources primaires (rapports officiels, transcriptions, articles de presse, lois)
- Identifier les sources contradictoires (defense des accuses, versions officielles, articles favorables au systeme)
- Noter les lacunes documentaires : sources introuvables, archives classees, periodes sans couverture

**0.2 Verifier l'accessibilite des sources**
- Pour chaque source potentielle : tenter d'obtenir une URL publique ou un identifiant stable (DOI, ISBN, cote d'archive)
- HEAD-checker chaque URL : 200 OK = ✦, 4xx/5xx = ⁅, pas d'URL accessible = ❧
- Verifier que le contenu correspond bien a ce qui est annonce (pas de detournement d'URL)

**0.3 Extraire les citations directes**
- Pour chaque source cle, extraire le passage pertinent entre guillemets avec la reference de page
- Ne pas citer de memoire — toujours verifier le texte exact

**0.4 Constituer le dossier documentaire**
- Lister les sources avec : URL, glyphe reel, citation directe, page
- Identifier les sources manquantes → les marquer [RECHERCHE COMPLEMENTAIRE NECESSAIRE]
- Si aucun traceur verifiable n'est trouve pour un mecanisme presuppose → le marquer [HYPOTHESE] avant meme d'ecrire la fiche

### Etape 1 — Lancer l'enquete

Utiliser `2026-06-26_21-00_prompt_investigation_v2_PROMPT.md` (renforce v2.1) — le point d'entree unique du protocole.

### Etape 2 — Produire la fiche YAML v2.1

Les 12 chapitres (1-12) doivent etre remplis. Les chapitres 5-10 (PREUVES, CONTRE-VERSION, ACTIVATION, INCERTITUDES, BIAIS, REPLICATION) sont obligatoires.

### Etape 3 — Auto-verification (inchangee)

1. Cette enquete pointe-t-elle des failles que le systeme pourrait utiliser pour se renforcer ? (M25)
2. La contestation analysee etait-elle de la dissidence reelle ou absorbee ? (M22)
3. Quel etait le pacte tacite que tout le monde maintenait ? (M11/Kayfabe, M37/Hypernormalisation)
4. Quelle strategie de resistance aurait pu (ou a) fonctionne ? (R01-R10)

### Etape 4 — Phase d'Approfondissement (Ultrathinking) [RENFORCE v2.1]

Deployer la phase Ultrathinking (§IV) selon les conditions de declenchement :
- **Degre 4-5** : ULTRATHINKING OBLIGATOIRE — sanction NREF-C max sans addendum
- **Degre 2-3** : ULTRATHINKING RECOMMANDE — augmente le niveau NREF
- **Degre 1** : ULTRATHINKING FACULTATIF

L'addendum doit suivre le **format ADDENDUM** defini en §IV (ANGLES_ALTERNATIFS, ICEBERG_MAX, LIEVRES_ET_LOUPS, FAISCEAUX_TRANSVERSAUX, PISTES_FUTURES, HYPOTHESES_SYSTEMIQUES).

**Minimum attendu :**
- 3 angles alternatifs
- 3 structures sous-marines (ICEBERG_MAX)
- 2 lievres ou loups
- 2 connexions transversales
- 2 pistes futures (dont 1 P1)
- 1 hypothese systemique

### Etape 5 — Verification NREF [NOUVEAU v2.0]

Passer la fiche au crible du bareme NREF v2.1 (10 exigences). Calculer le niveau de robustesse (A/B/C/D/E).

**Regles :**
- Si niveau E → la fiche est refusee, retour etape 2
- Si niveau D → la fiche est acceptee mais marquee [ESSAI, REFUTABLE]
- Si niveau C → la fiche est acceptee mais marquee [PARTIELLEMENT ETAYEE]
- Si niveau B → la fiche est acceptee, recommandation de completer les sources (NREF-9) ou la contre-version (NREF-10)
- Si niveau A → la fiche est validee comme preuve

### Etape 6 — Tableau de bord

Ajouter les donnees de l'enquete au TABLEAU_DE_BORD.md (mecanismes dominants, strategies pertinentes, niveau NREF, nouvelles pistes de l'addendum).

---

## PARTIE VI : TABLEAU DE BORD

**A creer.** Le tableau de bord est un fichier separe qui agrege toutes les enquetes produites. Voir le plan v2.0 pour la structure proposee.

Colonnes minimales :
| Date | ID | Sujet | Annee | Code | Dim | Degre | Fils actifs | M## dominants | Pattern | NREF | Citation-cle |
|-----|-----|-------|-------|------|-----|-------|-------------|---------------|---------|------|--------------|

---

## PARTIE VII : CONSOLIDATION PERIODIQUE (inchangee)

Toutes les 10 enquetes (ou sur demande) :
1. Analyser les fils les plus actives (pattern detection)
2. Analyser les mecanismes les plus frequents — quels M## reviennent le plus souvent ?
3. Analyser les strategies de resistance les plus pertinentes — quels R## sont les plus adaptes ?
4. Verifier si un 9e fil emerge ou si un nouveau mecanisme doit etre ajoute
5. Croiser les resultats avec les articles Substack existants
6. Mettre a jour l'architecture systemique globale
7. Rediger un rapport de synthese incluant les recommandations de resistance

---

## PARTIE VIII : EXEMPLE D'ENQUETE (sang contamine)

**Fichier :** `02_enquetes/2026-06-26_sang_contamine_NREF_INVESTIGATION.md`

Cette enquete a ete produite avec le protocole v2.0 (format YAML v2.0, 12 chapitres). Elle est le premier test du format NREF. L'audit a revele des lacunes (sources non verifiees, URLs absentes, Ultrathinking non execute) qui ont conduit a la v2.1. Elle sert d'exemple de reference pour les points a ameliorer.

---

## NOTES DE VERSION

- **v1.0** (2026-06-25) : Version fondatrice. 8 fils identifies a partir de l'enquete sur le sang contamine.
- **v1.1** (2026-06-25) : Enrichissement par 33 mecanismes actifs extraits de 7 articles de la Resistance Cognitive.
- **v1.2** (2026-06-25) : Enrichissement par 9 nouveaux mecanismes (M34-M42) et 10 strategies de resistance (R01-R10).
- **v1.3** (2026-06-25) : Separation stricte entre connaissance (protocole) et mission (prompt). Simplification du YAML.
- **v1.3+** (2026-06-26) : Ajout de la Phase d'Approfondissement Ultrathinking.
- **v2.0** (2026-06-26) : Refonte NREF. 6 nouveaux chapitres YAML (PREUVES, CONTRE-VERSION, ACTIVATION, INCERTITUDES, BIAIS, REPLICATION). Barème de conformite NREF a 8 exigences. Workflow refondu avec etape de Verification NREF.
- **v2.1** (2026-06-26) : Renforcement NREF post-audit. Audit de l'enquete sang contamine v2.0 a revele : 0 verifications web, 0 URLs, glyphes ✦ attribues sans HEAD check, Ultrathinking non execute, niveau NREF gonfle (B revendique, D reel). Corrections : instructions operationnelles de recherche web et HEAD check ajoutees au prompt ; `source_url`, `citation_directe`, `head_check_date` devenus obligatoires dans le schema YAML ; glyphes ✦ soumis a HEAD check reel ; NREF-9 (sources verifiees) et NREF-10 (contre-version sourcee) ajoutes au bareme ; echelle de robustesse recalibree avec niveau E.
