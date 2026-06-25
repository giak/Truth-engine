# PROTOCOLE D'INVESTIGATION SYSTEMIQUE v2.3 NREF
## Framework d'enquete forensique sur les defaillances de la societe francaise
### Reference des mecanismes, fils, strategies de resistance et standard de preuve
### ARCHÉOLOGIE DES FILS [v2.2] + CONTRE-MESURES OPERATIONNELLES [NOUVEAU v2.3]

---

## PREAMBULE

Ce protocole est la version 2.3 NREF (Non Refutable). Il herite des versions 1.0 a 2.2 qui ont identifie 8 fils systemiques, 42 mecanismes actifs et 10 strategies de resistance. La version 2.1 a ajoute les exigences de verification des sources. La version 2.2 a ajoute l'exigence de remontee archeologique. La version 2.3 ajoute l'exigence de **contre-mesures operationnelles** : chaque enquete doit identifier les actions concretes qui auraient pu empecher la bascule, par qui, et a quel moment.

**Les 5 piliers de la V2.3 :**
1. **Chaine de preuve** : chaque mecanisme identifie doit etre etaye par au moins un traceur verifiable avec URL et citation directe
2. **Contre-version sourcee** : la version officielle des faits doit etre presentee avec une source reelle (nom, date, URL) et refutee point par point
3. **Honneur cognitif** : les incertitudes, les biais de l'enqueteur, ET le statut reel des sources (glyphes verifies) doivent etre declares
4. **Archeologie des fils** : chaque fil actif identifie doit etre remonte jusqu'a son acte de naissance historique — les mecanismes ne sont pas nés avec l'evenement, ils sont le produit d'une stratification de 200+ ans
5. **Contre-mesures operationnelles [NOUVEAU v2.3]** : chaque enquete doit identifier les actions concretes qui auraient pu empecher la bascule ou empecheraient sa recurrence — avec acteur, fenetre d'opportunite, faisabilite, et precedent historique verifie

**These centrale (inchangee) :** Les defaillances francaises ne sont pas des accidents. Elles sont le produit d'une architecture systemique construite sur 200+ ans, maintenue par un ensemble de mecanismes homeostatiques qui transforment la colere en carburant, la resistance en maintenance, et la lucidite en fonction du systeme.

**Constats fondateurs (inchanges) :**
- Le systeme francais produit des defaillances silencieuses sans generer de contre-reaction citoyenne proportionnee
- Ces defaillances ne sont pas des accidents : elles sont le produit d'une architecture construite sur 200+ ans
- L'analyse du « sang contamine » (1984) a revele 8 fils causaux remontant jusqu'en 1791
- Chaque fil est un verrou systemique qui neutralise un contre-pouvoir

**Nouveaux constats v2.1 (inchanges) :**
- Les enquetes v2.0 produisaient des dossiers structures mais les sources n'etaient pas verifiees : les glyphes ✦ etaient attribues sans HEAD check, les URLs n'etaient pas citees, les citations directes manquaient
- Le protocole ne disait pas a l'enqueteur COMMENT verifier ses sources — il disait seulement QUOI produire
- La phase Ultrathinking etait mentionnee mais pas executee (degre 5 sans addendum)
- Une enquete NREF sans sources verifiees est un essai, pas une preuve

**Nouveau constat v2.2 (inchangé) :**
- Les enquetes v2.1 produites identifient les mecanismes (M11, M28, M37...) et les fils (A-H) dans l'evenement etudie, mais elles ne remontent PAS les fils jusqu'a leurs racines historiques. Le chapitre RACINES est devenu un inventaire de causes immediates (0-3 ans de profondeur), pas une archeologie du systeme
- Les 5 enquetes produites montrent que M11+M28+M05 est invariant, mais personne n'a explique COMMENT ce pattern s'est construit sur 200+ ans
- Une enquete systemique sans archeologie des fils est une photographie, pas un diagnostic

**Nouveau constat v2.3 :**
- Les enquetes v2.2 identifient les mecanismes et leurs racines historiques, mais elles ne repondent pas a la question operationnelle : « qu'aurait-on dû faire, a quel moment, par qui, pour que la bascule ne se produise pas et ne se reproduise pas ? »
- Le chapitre RESISTANCE (R01-R10) propose des strategies abstraites mais pas d'actions concretes avec acteur, fenetre d'opportunite et faisabilite
- Les BIFURCATIONS_PERDUES identifient « ou ca aurait pu etre different » mais pas « quoi exactement, par qui »
- Sans contre-mesures operationnelles, l'enquete est une autopsie sans protocole de reanimation

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
# Racines immediates de l'evenement (0-10 ans).
# ============================================================
RACINES:
  - "[cause profonde 1 : loi, institution, decision fondatrice, verrou structurel immediat]"
  - "[cause profonde 2 : remonter au-dela de l'evenement immediat]"
  - "[cause profonde 3 : niveau culturel, cognitif, historique immediat]"

# ============================================================
# CHAPITRE 2.5 — REMONTEE DES FILS [NOUVEAU v2.2]
# Archeologie obligatoire de chaque fil actif.
# Pour chaque fil A-H actif dans VERROUILLAGE, remonter
# jusqu'a son acte de naissance + renforcements historiques.
# Utiliser le referentiel : 2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md
# ============================================================
REMONTEE_DES_FILS:
  reference_document: "2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"
  fils_archeologie:
    - fil: "[lettre A-H : identique a VERROUILLAGE.fils_actifs]"
      acte_naissance:
        date: "[AAAA]"
        evenement: "[loi, decret, evenement constitutif du fil]"
        mecanisme_cree: "[M## cree par cet acte]"
        source: "[URL ou reference du document source]"
      renforcements_historiques:
        - date: "[AAAA]"
          evenement: "[premier renforcement : consolidation du fil]"
          mecanisme_active: "[M##]"
          source: "[URL ou reference]"
        - date: "[AAAA]"
          evenement: "[second renforcement]"
          mecanisme_active: "[M##]"
          source: "[URL ou reference]"
      chaine_causale:
        - "[acte_naissance] → [renforcement 1] → [renforcement 2] → ... → manifestation dans l'evenement"
      manifestation_dans_evenement:
        "[description operationnelle : comment ce fil s'est manifeste dans l'evenement etudie, en reference directe aux donnees de l'enquete]"
    - fil: "[autre fil actif]"
      ...

# ============================================================
# CHAPITRE 3 — BIFURCATIONS PERDUES (inchange)
# ============================================================
BIFURCATIONS_PERDUES:
  - "[moment precis ou ca aurait pu etre different — quoi, qui, pourquoi ca n'a pas eu lieu]"
  - "[autre bifurcation si pertinente]"

# ============================================================
# CHAPITRE 3.5 — CONTRE-MESURES [NOUVEAU v2.3]
# Pour chaque bascule identifiee, repondre a la question :
# « Qu'aurait-on dû faire, par qui, a quel moment, pour
# empecher ou empecher la recurrence ? »
# Les contre-mesures sont operationnelles (acte, acteur,
# fenetre), pas des intentions abstraites.
# ============================================================
CONTRE_MESURES:
  actions_requises:
    - temporalite: "[PENDANT / APRES / PREVENTIF]"
      cible_fil: "[A-H : fil systemique que l'action aurait neutralise]"
      cible_mecanisme: "[M## : mecanisme que l'action aurait bloque]"
      action_concrete: "[quoi exactement — pas une intention, un acte verifiable]"
      acteur: "[qui devait agir — nom, fonction, institution]"
      fenetre_opportunite: "[quand — date ou delai precis]"
      faisabilite: "[eleve / moyen / faible]"
      cout_estime: "[cout politique, economique, social estime]"
      precedent_historique: "[exemple historiquement verifie ou cette action a fonctionne ailleurs]"
      source_preuve: "[URL ou reference attestant que cette action aurait marche]"
      non_faite_parce_que: "[verrou qui l'a empechee — lien vers M## dans VERROUILLAGE]"
    - temporalite: "..."
      # Minimum 2 actions : 1 PENDANT/APRES + 1 PREVENTIF
  verrous_contre_mesures:
    - "[[mecanisme qui a bloque la contre-mesure elle-meme : ex. M11 kayfabe, M22 absorption]"
  apprentissages_pour_futur:
    - "[condition requise pour que la contre-mesure soit applicable la prochaine fois]"

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
| **NREF-11 [NOUVEAU v2.2]** | Chaque fil actif dans VERROUILLAGE a une entree dans REMONTEE_DES_FILS avec acte de naissance + au moins 2 renforcements historiques + chaine causale complete jusqu'a l'evenement | La fiche est marquee [RACINES IMMEDIATES SEULEMENT] |
| **NREF-12 [NOUVEAU v2.3]** | L'enquete contient au moins 2 contre-mesures operationnelles dans CONTRE_MESURES (1 PENDANT/APRES + 1 PREVENTIF) avec acteur identifie, fenetre d'opportunite, faisabilite, et precedent historique verifie | La fiche est marquee [AUTOPTIE SANS REMEDE] |

### Echelle de robustesse v2.3

| Niveau | Conforme a | Interpretation |
|--------|------------|----------------|
| NREF-A | Toutes les exigences 1-12 | Enquete utilisable comme preuve : sources verifiees, contre-version sourcee, archeologie des fils complete, contre-mesures operationnelles identifiees |
| NREF-B | Exigences 1-8 (incluant NREF-9 et NREF-10) | Enquete solide avec sources verifiees mais archeologie ou contre-mesures incompletes |
| NREF-C | Exigences 1-5 | Enquete partiellement etayee, sources non verifiees ou contre-version absente |
| NREF-D | Exigences 1-3 | Enquete de type « essai », refutable |
| NREF-E | Aucune ou 1 seule exigence satisfaite en substance | Enquete refusee — doit etre refaite |

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

### Etape 1.5 — Archeologie des fils [NOUVEAU v2.2]

Apres avoir lance l'enquete (etape 1) et AVANT de produire la fiche YAML (etape 2), l'enqueteur doit consulter le referentiel archeologique et identifier pour chaque fil actif pressenti :

**1.5.1 Consulter le referentiel**
- Ouvrir `2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md`
- Pour chaque fil A-H pressenti comme actif dans l'evenement, reperer son acte de naissance et ses renforcements historiques
- Noter les sources (lois, decrets, rapports) pour verification ulterieure (etape 0)

**1.5.2 Verifier les actes fondateurs**
- HEAD-checker les URLs des actes de naissance identifiés (Legifrance, Gallica, etc.)
- Si un acte fondateur n'est pas verifiable → le marquer ❧ dans la fiche
- Si un nouveau fil est propose (au-dela de A-H) → documenter son acte de naissance et ses renforcements dans le referentiel (mise a jour PARTIE VII)

**1.5.3 Tracer la chaine causale**
- Etablir la sequence : acte de naissance → renforcement 1 → renforcement 2 → ... → manifestation dans l'evenement
- Pour chaque maillon de la chaine, identifier le mecanisme (M##) active
- Verifier que la chaine causale est complete : aucun saut temporel > 50 ans sans explication

**Sanction :** Sans etape 1.5, NREF-11 echoue — la fiche ne peut pas depasser le niveau NREF-B (voir barème NREF v2.2 §III).

### Etape 2 — Produire la fiche YAML v2.3

Les 13 chapitres (1-12 + 3.5 CONTRE_MESURES) doivent etre remplis. Les chapitres 5-10 (PREUVES, CONTRE-VERSION, ACTIVATION, INCERTITUDES, BIAIS, REPLICATION) sont obligatoires. CONTRE_MESURES (3.5) est obligatoire pour viser NREF-A.

### Etape 3 — Auto-verification (inchangee)

1. Cette enquete pointe-t-elle des failles que le systeme pourrait utiliser pour se renforcer ? (M25)
2. La contestation analysee etait-elle de la dissidence reelle ou absorbee ? (M22)
3. Quel etait le pacte tacite que tout le monde maintenait ? (M11/Kayfabe, M37/Hypernormalisation)
4. Quelle strategie de resistance aurait pu (ou a) fonctionne ? (R01-R10)

### Etape 4 — Phase d'Approfondissement (Ultrathinking) [RENFORCE v2.2]

La verification archeologique fait partie integrante de l'Ultrathinking : les 5 questions ci-dessous sont a integrer dans l'addendum (section FAISCEAUX_TRANSVERSAUX ou HYPOTHESES_SYSTEMIQUES) :

1. **Y a-t-il un fil actif que la remontee ne parvient pas a relier a l'evenement ?** → le fil est peut-etre un passager clandestin
2. **La chaine causale saute-t-elle plus de 50 ans sans explication ?** → il manque un renforcement
3. **Un acte de naissance identifie est-il anterieur a 1791 ?** → le fil pourrait avoir une racine encore plus profonde (Ancien Regime, feodalite)
4. **Tous les renforcements sont-ils lies a des mecanismes M## differents ?** → si non, le verrouillage est mono-mecanique (moins grave)
5. **La remontee revele-t-elle un 9e fil ?** → le proposer a la consolidation periodique (PARTIE VII)

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

### Etape 5 — Verification NREF [v2.3]

Passer la fiche au crible du bareme NREF v2.3 (12 exigences : NREF-1 a NREF-12). Calculer le niveau de robustesse (A/B/C/D/E).

**Regles :**
- Si niveau E → la fiche est refusee, retour etape 2
- Si niveau D → la fiche est acceptee mais marquee [ESSAI, REFUTABLE]
- Si niveau C → la fiche est acceptee mais marquee [PARTIELLEMENT ETAYEE]
- Si niveau B → la fiche est acceptee, recommandation de completer les sources (NREF-9) ou la contre-version (NREF-10)
- Si niveau A → la fiche est validee comme preuve

### Etape 5 bis — Verification par second agent [NOUVEAU v2.1]

Une fois l'auto-evaluation NREF terminee (etape 5), un second agent verifie les resultats. Le second agent est un LLM different du premier, ou le meme avec une instruction de contre-expertise explicite : « Tu es un contre-expert, tu dois casser cette enquete. »

Il relit la fiche en adoptant le role de **contre-expert** : son objectif n'est pas de valider le travail, mais de le casser. L'objectif n'est pas de valider le travail — c'est de le casser.

**Le contre-expert doit tester :**
1. **Glyphes de fiabilite** : chaque ✦ est-il verifie par un HEAD 200 OK avec `head_check_date` ?
2. **Sources** : chaque `source_url` existe-t-elle ? Le contenu correspond-il a ce qui est cite ?
3. **Citations directes** : chaque `citation_directe` est-elle textuellement exacte ? (verification du contexte)
4. **Contre-version** : la source officielle est-elle correctement representee ou caricaturee (strawman) ?
5. **BIAIS** : les angles exclus declares sont-ils coherents avec la fiche ? Y a-t-il des angles morts non declares ?
6. **PREUVES** : chaque traceur prouve-t-il bien ce qu'il est cense prouver ? (pas de faux lien logique)
7. **INCERTITUDES** : les questions sans reponse sont-elles honnetes ? Des certitudes cachees persistent-elles ?

**Mecanisme de conflit :**
- Si le contre-expert estime un niveau NREF inferieur au niveau auto-declare par l'enqueteur initial → **conflit**
- La fiche est marquee [CONTRADICTION NON RESOLUE — NIVEAU ESTIME: X]
- L'enqueteur initial doit corriger les points identifies avant de soumettre a nouveau
- Si le conflit persiste apres 2 corrections → la fiche est soumise a un tiers (arbitrage)

**Sanction :** Sans verification par second agent, la fiche ne peut pas depasser le niveau NREF-B.

### Etape 6 — Mise a jour du TABLEAU_DE_BORD.md

Apres avoir produit la fiche, l'addendum Ultrathinking, et la verification NREF, reporter les donnees dans le TABLEAU_DE_BORD.md (`03_framework/TABLEAU_DE_BORD.md`). Cette etape est obligatoire — sans elle, l'enquete n'est pas integree a la fresque cumulative.

**Operations a effectuer :**

1. **Metriques globales** : incrementer « Enquetes v2.1 NREF produites », mettre a jour les cumuls (sources ✦/⁅/❧, HEAD checks)
2. **Enquetes realisees** : ajouter une ligne dans le tableau (ID, Sujet, Code, Dim, Degre, NREF, Sources, Ultrathinking, Second agent, Fils, M## dominants)
3. **Fichiers produits** : ajouter une ligne dans le tableau (Fiche YAML, Source si version anterieure)
4. **Synthese des enquetes** : creer un nouveau bloc (these centrale, citation cle, mecanismes dominants/ secondaires, fils actifs, strategies de resistance, sources, falsifiabilite, pattern dominant)
5. **Suivi des validations** : deplacer les points de vigilance de l'enquete dans la section « En attente » ou « Blocages resolus »
6. **File d'attente** : ajouter les nouvelles pistes issues de l'addendum Ultrathinking (PISTES_FUTURES) et les predictions de REPLICATION

**Regle :** Chaque mise a jour doit etre datee. Le dashboard est le point d'entree unique pour naviguer dans la fresque.

---

## PARTIE VI : TABLEAU DE BORD

### Role

Le TABLEAU_DE_BORD.md (`03_framework/TABLEAU_DE_BORD.md`) est le **point d'entree unique** de la fresque systemique. Il remplit 3 fonctions :

1. **Pilotage operationnel** — combien d'enquetes produites, a quel niveau NREF, qu'est-ce qui bloque (second agent, Ultrathinking)
2. **Fresque cumulative** — enquete apres enquete, les memes mecanismes reapparaissent, les patterns se confirment, la these centrale se verifie par accumulation
3. **Preparation de la reponse** — la synthese de chaque enquete fournit la matiere directement mobilisable pour un article, un essai, ou une synthese transverse

### Sections

Le fichier contient 5 sections :

| Section | Contenu | Mise a jour |
|---------|---------|-------------|
| **Metriques globales** | Nb enquetes, niveau NREF, Ultrathinking, second agent, sources cumulees, HEAD checks, blocages | Apres chaque enquete |
| **Enquetes realisees** | Tableau des investigations v2.1 + fichiers produits | Apres chaque enquete |
| **Synthese des enquetes** | These, citation, mecanismes (dominants + secondaires), fils, strategies, sources, falsifiabilite, pattern | Apres chaque enquete |
| **Suivi des validations** | En attente (second agent, Ultrathinking), points de vigilance, blocages resolus | Apres chaque enquete + chaque validation |
| **File d'attente** | Pistes P1/P2/P3 issues des addendums et des predictions REPLICATION | Apres chaque Ultrathinking |

### Instructions de mise a jour

Voir l'Etape 6 du workflow (ci-dessus) pour la procedure detaillee. En resume :

- Extraire de la fiche YAML produite : ENQUETE (ID), EVENEMENT (titre, code, dimension), VERROUILLAGE (fils, mecanismes, pattern), PREUVES (sources, glyphes), RESISTANCE (strategies), REPLICATION (predictions), ENSEIGNEMENT, CITATION_CLE, DEGRE_SYSTEMICITE
- Extraire de l'addendum Ultrathinking : ANGLES_ALTERNATIFS, ICEBERG_MAX, LIEVRES_ET_LOUPS, PISTES_FUTURES, HYPOTHESES_SYSTEMIQUES
- Extraire de la verification NREF : niveau (A/B/C/D/E), points de vigilance

---

## PARTIE VII : CONSOLIDATION PERIODIQUE [RENFORCEE v2.2]

Toutes les 10 enquetes (ou sur demande) :
1. Analyser les fils les plus actives (pattern detection)
2. Analyser les mecanismes les plus frequents — quels M## reviennent le plus souvent ?
3. Analyser les strategies de resistance les plus pertinentes — quels R## sont les plus adaptes ?
4. Verifier si un 9e fil emerge ou si un nouveau mecanisme doit etre ajoute
5. Croiser les resultats avec les articles Substack existants
6. Mettre a jour l'architecture systemique globale
7. Rediger un rapport de synthese incluant les recommandations de resistance

**Ajout v2.2 — Mise a jour du referentiel archeologique :**
8. **Consolider les apports archeologiques** : chaque enquete peut avoir ajoute des renforcements, corrige des dates, ou propose un nouveau fil dans REMONTEE_DES_FILS
9. **Mettre a jour le referentiel** `03_framework/2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md` avec les nouvelles donnees
10. **Verifier la coherence transversale** : les actes de naissance identifies dans chaque enquete sont-ils coherents entre eux ? Un fil peut-il avoir plusieurs actes de naissance concurrents ?
11. **Identifier les fils manquants** : existe-t-il des evenements dont la remontee archeologique revele un nouveau fil (I, J...) ? Si oui, documenter son acte de naissance, ses renforcements, et sa chaine causale dans le referentiel

---

## PARTIE VIII : EXEMPLE D'ENQUETE (sang contamine)

### Enquete de reference v2.1 (migrer vers v2.2)

**Fichier :** `02_enquetes/2026-06-26_sang_contamine_v2.1_INVESTIGATION.md`

Cette enquete a ete produite avec le protocole v2.1 (format YAML v2.1, 12 chapitres, sources verifiees). Elle doit etre migree vers le format v2.2 avec ajout du chapitre REMONTEE_DES_FILS pour servir de reference complete.

**Resume :**
- Niveau NREF : B → vise NREF-A apres migration v2.2
- Sources : 1 ✦ (HEAD 200 OK) + 3 ⁅ (Legifrance anti-bot) + 4 ❧ (papier/non trouve)
- Mecanismes dominants : M14 (Impuissance apprise), M23 (Ingenierie possession), M05 (Perfusion publique), M28 (DARVO), M11 (Kayfabe politique)
- 8 fils tous actifs (degre 5/5)
- Ultrathinking : ✅ realise (6 sections)
- Second agent : 🔲 a realiser
- REMONTEE_DES_FILS : 🔲 a ajouter (migration v2.2)

### Enquete historique v2.0

**Fichier :** `02_enquetes/archive/2026-06-26_sang_contamine_NREF_INVESTIGATION.md`

Premier test du format NREF (v2.0). L'audit a revele des lacunes ayant conduit a la v2.1 : 0 verification web, 0 URL, glyphes ✦ abusifs, Ultrathinking non execute, niveau NREF gonfle (B revendique, D reel). Conservee comme trace de la correction.

---

## PARTIE IX : ARCHÉOLOGIE DES FILS [NOUVEAU v2.2]

### Principe

L'archeologie des fils est le **4e pilier** du protocole v2.2. Apres la chaine de preuve (v2.1), la contre-version sourcee (v2.1) et l'honneur cognitif (v2.1), l'enqueteur doit desormais remonter chaque fil actif jusqu'a son acte de naissance historique et documenter les renforcements qui l'ont consolide au fil du temps.

**Pourquoi c'est necessaire :**
- Les 5 enquetes produites en v2.1 identifient correctement les mecanismes (M11, M28, M37...) mais le chapitre RACINES reste un inventaire de causes immediates (0-3 ans de profondeur)
- Le pattern M11+M28+M05 est invariant dans 5 cas sur 5, mais personne n'a explique COMMENT ce pattern s'est construit sur 200+ ans
- La promesse fondatrice du protocole — « remonter les fils jusqu'en 1791 » — est restee lettre morte dans les enquetes produites
- Sans archeologie, les mecanismes semblent naitre avec l'evenement. Avec l'archeologie, on voit qu'ils sont le produit d'une stratification historique

### Referentiel archeologique

Le fichier `03_framework/2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md` compile les actes de naissance et renforcements historiques des 8 fils A-H. C'est le referentiel stable que toute enquete v2.2 doit consulter.

**Structure du referentiel :**
- Pour chaque fil A-H : acte de naissance (date, evenement, mecanisme cree) + renforcements historiques (dates, evenements, mecanismes actives) + chaine causale complete
- Frise archeologique synthetique (1660-2026) montrant l'empilement des verrous
- Carte des connexions entre fils (racines croisees : 1791 Le Chapelier = B + C ; 1804 Code civil = C + D ; 1958 = B + D + A)
- Regles d'utilisation dans les enquetes

### Structure obligatoire du chapitre REMONTEE_DES_FILS

Le chapitre 2.5 du format YAML (REMONTEE_DES_FILS) doit contenir pour chaque fil actif identifie dans VERROUILLAGE.fils_actifs :

1. **Reference croisee** : `fil: [lettre]` — meme identifiant que dans VERROUILLAGE
2. **Acte de naissance** : date, evenement, mecanisme cree, source verifiee (glyphe selon HEAD check)
3. **Renforcements historiques** : minimum 2, maximum 6 — chaque avec date, evenement, mecanisme active, source
4. **Chaine causale** : sequence complete de l'acte fondateur a la manifestation dans l'evenement — chaque maillon doit etre explicite (pas de saut temporel > 50 ans sans explication)
5. **Manifestation dans l'evenement** : description operationnelle de comment le fil s'est manifeste dans l'evenement etudie

### Regles de l'archeologie

1. **Tout fil actif doit etre remonte.** Si un fil identifie dans VERROUILLAGE.fils_actifs n'a pas d'entree dans REMONTEE_DES_FILS → NREF-11 echoue → niveau NREF max = B
2. **Un fil sans acte de naissance identifie est un fil hypothetique.** Il doit etre marque [HYPOTHESE] dans la fiche et ne compte pas pour NREF-11
3. **Les actes de naissance anterieurs a 1791** (Colbert, Ordonnance criminelle, etc.) signalent des racines pre-revolutionnaires — le fil est encore plus profond qu'estime
4. **Les renforcements majeurs sont en priorite** : acte de naissance + renforcements majeurs (en gras dans le referentiel) sont obligatoires ; renforcements simples sont recommandes
5. **Un nouveau fil identifie par une enquete** (au-dela de A-H) doit etre propose a la consolidation periodique (PARTIE VII) avec son acte de naissance et ses renforcements

### Regle speciale : candidats auto-referents (Fils I, J, K...)

Un cas particulier se presente lorsqu'un fil candidat a pour **acte de naissance l'evenement enquete lui-meme** (ex. Fil I — Vassalite monetaire : acte de naissance = Maastricht 1992, qui est aussi l'evenement de l'enquete). Cela cree une **circularite douce** : l'enquete confirme en partie le fil par sa propre existence.

**Protocole a suivre pour les candidats auto-referents :**

a. **Chaine causale obligatoire partant d'avant l'evenement** : l'enquete ne peut pas se contenter de decrire l'acte de naissance comme point de depart. Elle DOIT remonter a un antecedent causal clairement identifie (ex. pour Fil I : virage rigueur 1983 comme pre-condition). Cet antecedent doit etre separe de l'evenement par au moins un verrou systemique documente (ex. pour Fil I : virage 1983 -> Maastricht 1992 = 2 verrous distincts). Sans antecedent causal documente (que le seuil soit de 1 an ou 50 ans), le fil candidat reste au statut HYPOTHESE. Le seuil de 10 ans est indicatif — ce qui compte est la documentation d'un verrou prealable separé, pas la duree.

b. **Double marquage explicite** : dans la fiche YAML, le fil candidat auto-referent doit etre marque `[CANDIDAT EN TEST]` dans l'enquete, meme si son statut est eleve. La confirmation ne peut intervenir qu'apres la consolidation periodique (PARTIE VII) et au moins une enquete de replication (ex. Grece 2015 pour Fil I).

c. **Au moins un contre-exemple documente** : l'enquete doit presenter au moins un cas ou le fil aurait du s'activer mais ne l'a pas fait (ex. pour Fil I : Danemark — opt-out sur l'euro, pas de vassalite monetaire). Sans contre-exemple, le fil n'est pas falsifiable et ne peut pas etre confirme.

d. **Limitation methodologique documentee dans BIAIS_ENQUETEUR** : l'enqueteur doit explicitement declarer dans le chapitre 9 que « l'acte de naissance du fil candidat [I/J/K] est l'evenement enquete lui-meme, ce qui cree une circularite douce — la confirmation du fil est partiellement auto-referente. »

**Exemple (Fil I — Maastricht 1992) :**
- Chaine causale : 1983 (virage rigueur) -> 1992 (Maastricht) -> confirmee par les renforcements 1999/2005/2012/2020
- Contre-exemple : Danemark (opt-out 1992, garde sa couronne, se porte bien)
- Marquage : `[CANDIDAT EN TEST]` dans REMONTEE_DES_FILS, promu CONFIRME apres consolidation
- Biais declare : « l'acte de naissance de Fil I est Maastricht 1992, l'evenement enquete — circularite douce »

### Sanction

Sans chapitre REMONTEE_DES_FILS (NREF-11 non satisfait), la fiche ne peut pas depasser le niveau NREF-B, meme si les 10 autres exigences sont satisfaites (voir barème NREF v2.3 §III). L'archeologie des fils est un multiplicateur de profondeur : sans elle, l'enquete reste une photographie, pas un diagnostic.

---

## PARTIE X : CONTRE-MESURES OPERATIONNELLES [NOUVEAU v2.3]

### Principe

Les contre-mesures operationnelles sont le **5e pilier** du protocole v2.3. Apres la chaine de preuve, la contre-version sourcee, l'honneur cognitif et l'archeologie des fils, l'enqueteur doit desormais identifier les actions concretes qui auraient pu empecher la bascule ou empecheraient sa recurrence.

**Pourquoi c'est necessaire :**
- Les enquetes produites identifient les mecanismes (M11, M28, M37...) et les racines historiques (Le Chapelier, Code civil...), mais elles ne disent pas QUOI FAIRE
- Le chapitre RESISTANCE (R01-R10) propose des strategies abstraites (parresia, retrait du consentement) sans acteur ni fenetre d'opportunite
- Les BIFURCATIONS_PERDUES disent « ca aurait pu etre different » mais pas « qui devait faire quoi, quand »
- Sans contre-mesures operationnelles, l'enquete est une autopsie sans protocole de reanimation

### Les deux temporalites

Toute contre-mesure doit etre categorisee selon sa temporalite :

| Temporalite | Definition | Exemple (sang contamine) |
|-------------|------------|--------------------------|
| **PREVENTIF** | Action avant la bascule pour l'empecher | Mai 1983 : imposer un avis scientifique contradictoire (FDA/Behring) avant decision du CNTS |
| **PENDANT** | Action pendant la bascule pour limiter les degats | 1991 : des la revelation Casteret, saisir la CJR et non pas laisser le systeme enterrer l'affaire |
| **APRES** | Action apres la bascule pour empecher la recurrence | 1999 : creer une class action sanitaire au lieu d'une CJR qui acquitte systematiquement les ministres |

### Les trois niveaux d'acteurs

Chaque contre-mesure doit identifier son acteur selon l'echelle suivante :

| Niveau | Acteur typique | Levier | Cout politique |
|--------|----------------|--------|----------------|
| **Micro** | Citoyen, patient, journaliste local, lanceur d'alerte | Temoignage, refus de consentement, verification citoyenne | Faible (individuel) |
| **Meso** | Association, syndicat, ordre professionnel, media | Class action, greve, contre-expertise, petition | Moyen (collectif organise) |
| **Macro** | Gouvernement, Parlement, Conseil constitutionnel, traite | Loi, reforme constitutionnelle, decret, traite | Eleve (changement de cadre) |

### Structure obligatoire du chapitre CONTRE_MESURES

Le chapitre 3.5 du format YAML (CONTRE_MESURES) doit contenir :

1. **Actions requises** : minimum 2 (1 PENDANT/APRES + 1 PREVENTIF) — chaque avec :
   - `temporalite` : PENDANT / APRES / PREVENTIF
   - `cible_fil` : fil A-H que l'action aurait neutralise
   - `cible_mecanisme` : M## que l'action aurait bloque
   - `action_concrete` : acte verifiable, pas une intention (ex. « publier un contre-rapport » pas « sensibiliser »)
   - `acteur` : nom ou fonction (ex. « Edmond Herve, Ministre de la Sante » pas « l'Etat »)
   - `fenetre_opportunite` : date ou delai (ex. « mai 1983 — reception offre Travenol-Hyland »)
   - `faisabilite` : eleve / moyen / faible
   - `cout_estime` : cout politique, economique ou social estime
   - `precedent_historique` : exemple verifie ou cette action a fonctionne (ex. « Allemagne : gouvernement federal impose produits chauffes Behring 1983, 0 mort »)
   - `source_preuve` : URL, rapport, temoignage attestant que l'action aurait marche
   - `non_faite_parce_que` : mecanisme qui l'a bloquee (lien vers VERROUILLAGE)

2. **Verrous des contre-mesures** : mecanismes qui ont bloque la contre-mesure elle-meme (ex. M11 kayfabe, M22 absorption)

3. **Apprentissages pour le futur** : conditions requises pour que la contre-mesure soit applicable la prochaine fois

### Regles des contre-mesures

1. **Toute contre-mesure doit etre operationnelle.** Pas de « il faudrait changer les mentalites » — une action verifiable avec un acteur nomme. Si l'acteur n'est pas identifiable, la contre-mesure est une intention.
2. **Toute contre-mesure doit avoir un precedent.** Elle doit etre etayee par un exemple historique documente (source verifiee) montrant que cette action a fonctionne ailleurs ou a un autre moment. Sans precedent, c'est une hypothese.
3. **Les trois temporalites sont obligatoires.** Minimum 1 PREVENTIF + 1 PENDANT ou APRES. Si une enquete ne peut identifier qu'une seule temporalite, elle doit le justifier dans INCERTITUDES.
4. **Les trois niveaux d'acteurs sont recommandes.** Si toutes les contre-mesures identifiees sont au niveau macro, l'enquete a un biais etatique declare (BIAIS_ENQUETEUR).
5. **La faisabilite n'est pas une excuse.** Meme une contre-mesure de faisabilite « faible » doit etre documentee — c'est son absence qui est informative.

### Sanction

Sans chapitre CONTRE_MESURES (NREF-12 non satisfait), la fiche ne peut pas depasser le niveau NREF-B, meme si les 11 autres exigences sont satisfaites. Les contre-mesures sont le pont entre le diagnostic et l'action : sans elles, l'enquete est une autopsie sans protocole de reanimation.

---

## NOTES DE VERSION

- **v1.0** (2026-06-25) : Version fondatrice. 8 fils identifies a partir de l'enquete sur le sang contamine.
- **v1.1** (2026-06-25) : Enrichissement par 33 mecanismes actifs extraits de 7 articles de la Resistance Cognitive.
- **v1.2** (2026-06-25) : Enrichissement par 9 nouveaux mecanismes (M34-M42) et 10 strategies de resistance (R01-R10).
- **v1.3** (2026-06-25) : Separation stricte entre connaissance (protocole) et mission (prompt). Simplification du YAML.
- **v1.3+** (2026-06-26) : Ajout de la Phase d'Approfondissement Ultrathinking.
- **v2.0** (2026-06-26) : Refonte NREF. 6 nouveaux chapitres YAML (PREUVES, CONTRE-VERSION, ACTIVATION, INCERTITUDES, BIAIS, REPLICATION). Barème de conformite NREF a 8 exigences. Workflow refondu avec etape de Verification NREF.
- **v2.1** (2026-06-26) : Renforcement NREF post-audit. Audit de l'enquete sang contamine v2.0 a revele : 0 verifications web, 0 URLs, glyphes ✦ attribues sans HEAD check, Ultrathinking non execute, niveau NREF gonfle (B revendique, D reel). Corrections : instructions operationnelles de recherche web et HEAD check ajoutees au prompt ; `source_url`, `citation_directe`, `head_check_date` devenus obligatoires dans le schema YAML ; glyphes ✦ soumis a HEAD check reel ; NREF-9 (sources verifiees) et NREF-10 (contre-version sourcee) ajoutes au bareme ; echelle de robustesse recalibree avec niveau E.
- **v2.2** (2026-06-26) : **Ajout de l'archeologie des fils.** Nouveau chapitre YAML 2.5 (REMONTEE_DES_FILS). Nouveau referentiel : `2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md`. Nouveau pilier : chaque fil actif doit etre remonte jusqu'a son acte de naissance historique (1791, 1804, 1660...). Nouvelle exigence NREF-11. Nouvelle partie : PARTIE IX (Archeologie des fils). Nouvelle etape workflow : 1.5 (Archeologie des fils) et 3.5 (Verification archeologique). Echelle de robustesse recalibree : NREF-A necessite desormais 11/11 exigences. Consolidation periodique renforcee : mise a jour du referentiel archeologique.
- **v2.3** (2026-06-26) : **Ajout des contre-mesures operationnelles.** Nouveau chapitre YAML 3.5 (CONTRE_MESURES). Nouveau pilier : chaque enquete doit identifier les actions concretes qui auraient pu empecher la bascule — avec acteur, fenetre d'opportunite, faisabilite, et precedent historique verifie. Nouvelle exigence NREF-12. Nouvelle partie : PARTIE X (Contre-mesures operationnelles). 5 piliers. 13 chapitres. Echelle de robustesse recalibree : NREF-A necessite desormais 12/12 exigences. Les trois niveaux d'acteurs (micro/meso/macro) et les deux temporalites (preventif/reactif) documentes.
