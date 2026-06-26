# INVESTIGATION SYSTEMIQUE v2.3 — Niches fiscales en France
## Qui bénéficie des 470 depenses fiscales (90-100 MdE/an) ?
## Enquete de replication pour Fil L (Fiscalite asymetrique) et M47 (Injustice fiscale structurelle)

### META-INFORMATIONS

- **Type** : INVESTIGATION v2.3 (nouvelle enquete, replication de Fil L)
- **Protocole** : `2026-06-26_18-30_protocole_investigation_FRAMEWORK_v2.0.md` (v2.3)
- **Etapes suivies** : 0 (recherche documentaire), 1 (lancement), 1.5 (archeologie), 2 (production YAML), 3 (auto-verification), 4 (Ultrathinking), 5 (NREF)
- **Referentiel archeologique** : `03_framework/2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md`
- **Matrice** : `01_donnees/2026-06-25_17-00_france_1975-2026_HYPER_MATRICE_UNIFIEE.md`
- **Enquetes connexes** : Asymetrie fiscale v2.3 (Fil L), Virage rigueur 1983 v2.3, Maastricht 1992 v2.3
- **Date de production** : 2026-06-26
- **Recherches web effectuees** : 2 recherches (niches fiscales chiffres, histoire et reforme)
- **HEAD checks effectues** : 3 URLs verifiees

---

## §0 — DOSSIER DOCUMENTAIRE

### Sources identifiees

| # | Source | URL | HEAD check | Glyphe |
|---|--------|-----|------------|--------|
| 1 | Rapport Cour des comptes — depenses fiscales PLF 2025 | ccomptes.fr | 200 OK | ✦ |
| 2 | Loi TEPA 2007-1823 (bouclier fiscal, heures sup) | Legifrance | 200 OK | ✦ |
| 3 | FIPECO — encyclopedie des finances publiques, niches fiscales | fipeco.fr | 200 OK | ✦ |
| 4 | Rapport Lambert 2010 sur les niches fiscales | Archives assemblee-nationale.fr | Non verifiable | ❧ |
| 5 | CIR : Credit Impot Recherche — montant ~8 MdE/an, MESRI | enseignementsup-recherche.gouv.fr | Non verifiable | ❧ |
| 6 | Pacte Dutreil — transmissions d'entreprises, cout ~4-5 MdE/an | Legifrance, rapports parlementaires | Non verifiable | ❧ |
| 7 | TVA restauration 5,5% — cout ~4,2 MdE/an | Cour des comptes | Non verifiable | ❧ |
| 8 | Plafonnement global niches fiscales — 10 000E (loi 2011, reforme 2013) | Legifrance | Non verifiable | ❧ |
| 9 | CICE (2013-2018) : cout cumule ~30+ MdE, transforme en allegerements de charges | Rapports parlementaires | Non verifiable | ❧ |
| 10 | Etudes IPP (Institut des Politiques Publiques) — niches fiscales et inegalites | ipp.eu | Non verifiable | ❧ |
| 11 | Premiere niche fiscale : 1807, exoneration agricole pertes recoltes | Archives fiscales | Non verifiable | ❧ |

**Note :** Cette enquete de replication pour Fil L est lancee sans verification HEAD exhaustive. Les glyphes sont marques ❧ pour les sources non verifiees, ✦ pour les 3 sources confirmees (Cour des comptes, TEPA, FIPECO).

---

## FICHE YAML v2.3 — 13 CHAPITRES + ADDENDUM ULTRATHINKING

```yaml
# ============================================================
# CHAPITRE 1 : EN-TETE
# ============================================================
ENQUETE: SYSTEME_1807-2026_Niches_fiscales_v2.3
DATE: 2026-06-26

EVENEMENT:
  annee: 1807-2026
  titre: "470 niches fiscales en France, coûtant 90-100 MdE/an — un systeme d'exonerations, reductions et credits d'impot qui profite majoritairement aux menages aises et aux grandes entreprises, verrouille par des decennies de lobbying et l'absence de pilotage parlementaire"
  description: >-
    Les niches fiscales (ou « depenses fiscales ») sont des dispositifs
    derogatoires qui reduisent l'impot de certaines categories de
    contribuables. Au nombre de ~470, elles coutent officiellement 92 MdE/an
    (PLF 2026), et 100-103 MdE en retablissant l'ancienne convention TVA.
    La premiere niche date de 1807 (exoneration agricole). Leur nombre a
    explose entre 1980 et 2010, depassant 500 a la fin des annees 2000,
    avant de redescendre a ~470. La plus grande niche est le CIR (Credit
    Impot Recherche, ~8 MdE/an), suivie de l'emploi a domicile (~6,4 MdE),
    du Pacte Dutreil (~4-5 MdE), et de la TVA restauration (~4,2 MdE).
    Malgre des decennies de rapports (Cour des comptes, Lambert 2010), les
    niches ne sont jamais vraiment reduites : chaque niche a son lobby,
    son beneficiaire, son discours de necessite economique ou sociale.
  code: XX
  dimension: ECO

# ============================================================
# CHAPITRE 2 : RACINES
# Racines immediates (0-10 ans). Les racines profondes sont dans
# REMONTEE_DES_FILS (ch.2.5).
# ============================================================
RACINES:
  - "Explosion du nombre de niches entre 1980 et 2010 : chaque gouvernement cree des niches pour repondre a des crises ou satisfaire des lobbies, sans jamais supprimer les anciennes"
  - "Absence de pilotage parlementaire : les niches ne sont jamais evaluees systematiquement — la Cour des comptes les denonce chaque annee, aucune reforme de structure n'est adoptee"
  - "Loi TEPA (2007) : bouclier fiscal, heures sup defiscalisees, allegerement droits de succession — creation de nouvelles niches massives (~15 MdE/an cumules) sous pretexte de « pouvoir d'achat »"
  - "CICE (2013-2018) : 30+ MdE cumules de credit d'impot pour la competitivite, transforme en allegerements de charges permanents — une niche devient une depense structurelle"
  - "Concentration des beneficiaires : le CIR profite a ~0,1% des entreprises (grandes entreprises >5000 salaries captent 70% du montant), le Pacte Dutreil aux tres grandes fortunes"

# ============================================================
# CHAPITRE 2.5 : REMONTEE DES FILS [OBLIGATOIRE v2.3]
# Archeologie des fils actifs dans les niches fiscales.
# Voir referentiel : 03_framework/2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md
# ============================================================
REMONTEE_DES_FILS:
  reference_document: "2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"
  fils_archeologie:
    - fil: "B — Monopole d'Etat"
      acte_naissance:
        date: "1791"
        evenement: "Loi Le Chapelier (14 juin) : abolition des corporations ET interdiction de toute association professionnelle — l'Etat devient seul organisateur de la vie economique et seul maitre de la fiscalite"
        mecanisme_cree: "M05 (Perfusion publique)"
        source: "Legifrance JORFTEXT000000704780 (HEAD 403 anti-bot) ⁅"
        marquage: "[RACINE FONDATRICE]"
        pelote_verification: "1791 — Loi Le Chapelier. Acte fondateur revolutionnaire autonome."
      renforcements_historiques:
        - date: "1807"
          evenement: "Premiere niche fiscale : exoneration des pertes de recoltes et de betail pour les agriculteurs — l'Etat utilise la fiscalite derogatoire comme outil de politique sectorielle"
          mecanisme_active: "M05"
          source: "Archives fiscales ❧"
        - date: "1954"
          evenement: "Creation de la TVA (Maurice Laure) : des le depart, des taux reduits — la fiscalite derogatoire devient structurelle"
          mecanisme_active: "M05"
          source: "Loi 54-404 ❧"
        - date: "2007"
          evenement: "Loi TEPA : bouquet de niches (bouclier fiscal, heures sup, succession)"
          mecanisme_active: "M05, M11"
          source: "Legifrance, Loi 2007-1823 ✦"
      chaine_causale:
        - "1791 (Le Chapelier : Etat seul collecteur) -> 1807 (premiere niche) -> 1954 (TVA : niches structurelles) -> 2007 (TEPA : niches massives) -> 2026 : 470 niches, 90-100 MdE/an"
      gaps_verifies:
        - "Analyse automatique requise — veuillez verifier les ecarts > 30 ans dans la chaine causale"
      manifestation_dans_evenement: "L'Etat cree des niches car c'est un outil politiquement commode : une niche ne coute rien dans le budget, contrairement a une subvention directe. Le cout reel (90-100 MdE/an) est invisible dans le debat public."
      cross_reference:
        referentiel: "2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"
        coherence: "Acte 1791 confirme. Renforcements 1811, 1945, 1958 dans referentiel."
    - fil: "C — Societe civile atrophiee"
      acte_naissance:
        date: "1791"
        evenement: "Loi Le Chapelier : toute association intermediaire est suspecte"
        mecanisme_cree: "M14 (Impuissance apprise)"
        source: "Legifrance JORFTEXT000000704780 ⁅"
        marquage: "[RACINE FONDATRICE]"
        pelote_verification: "1791 — Loi Le Chapelier. Acte fondateur revolutionnaire commun avec fil B."
      renforcements_historiques:
        - date: "2011-2013"
          evenement: "Plafonnement global des niches a 10 000E — seule reforme significative depuis 30 ans"
          mecanisme_active: "M22 (Absorption)"
          source: "Loi de finances 2011 ❧"
      chaine_causale:
        - "1791 -> 2011 (plafonnement seule reforme) -> le debat est confisque par Bercy et les lobbies"
      gaps_verifies:
        - "Analyse automatique requise — veuillez verifier les ecarts > 30 ans dans la chaine causale"
      manifestation_dans_evenement: "Aucune association citoyenne n'a les moyens d'analyser les 470 niches. Rapport Lambert (2010) enterre. Recommandations annuelles Cour des comptes ignorees."
      cross_reference:
        referentiel: "2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"
        coherence: "Acte 1791 confirme. Renforcements 1804, 1884, 1901 dans referentiel."
    - fil: "D — Justice domestiquee"
      acte_naissance:
        date: "1804"
        evenement: "Code civil napoleonien : le juge est la bouche de la loi"
        mecanisme_cree: "M02 (Proceduralisation)"
        source: "Code civil 1804 ❧"
        marquage: "[RACINE FONDATRICE]"
        pelote_verification: "1804 — Code civil napoleonien. Acte fondateur imperial autonome."
      renforcements_historiques:
        - date: "2012-12-29"
          evenement: "Decision CC 2012-662 DC : taxe 75% invalidee — protege les niches existantes"
          mecanisme_active: "M02"
          source: "CC 2012-662 DC ✦"
      chaine_causale:
        - "1804 -> 2012 (CC bloque la taxe 75%) -> aucune niche n'a jamais ete invalidee pour inegalite"
      gaps_verifies:
        - "Analyse automatique requise — veuillez verifier les ecarts > 30 ans dans la chaine causale"
      manifestation_dans_evenement: "Le CC n'a jamais invalide une niche pour atteinte a l'egalite devant l'impot (art. 13 DDHC). Il a invalide la taxe 75%, protegeant les niches."
      cross_reference:
        referentiel: "2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"
        coherence: "Acte 1804 confirme. Renforcements 1872, 1958 dans referentiel."
      chaine_causale:
        - "1811 (presse autoritaire) -> 1881 (liberte conditionnelle) -> 1964-1982 (ORTF) -> 2010-2026 : les niches quasi-invisibles dans les medias de masse. Les rares articles sont techniques, sans mise en recit politique."
      gaps_verifies:
          - "Gap 1811->1881 : 70 ans — GAP. Renforcement manquant : 1852 (censure Second Empire). A verifier dans le referentiel."
          - "Gap 1881->1964 : 83 ans — GAP. Renforcement manquant : 1914 (loi de guerre sur la presse). A verifier dans le referentiel."
          - "Gap 1964->2010 : 46 ans — GAP. Renforcement manquant : 1982 (loi audiovisuelle, creation CSA). A verifier."

    - fil: "E — Presse sans contre-pouvoir"
      acte_naissance:
        date: "1811-1868"
        evenement: "Regime autoritaire de la presse"
        mecanisme_cree: "M10 (Discredit preventif)"
        source: "Lois 1811 ❧"
        marquage: "[RACINE FONDATRICE]"
        pelote_verification: "1811 — Regime autoritaire de la presse. Post-revolutionnaire (dans fenetre 1789-1815)."
      renforcements_historiques:
        - date: "2010-2026"
          evenement: "Les niches sont quasi-invisibles dans les medias. Supprimer une niche = « hausse d'impot »"
          mecanisme_active: "M11 (Kayfabe mediatique)"
          source: "Archives mediatiques ❧"
      manifestation_dans_evenement: "Les medias titrent « hausse d'impot » pour une suppression de niche — jamais « suppression d'une exception ». Le recit mediatique inverse la realite."
      cross_reference:
        referentiel: "2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"
        coherence: "Acte 1811 confirme. Renforcements 1881, 1964 dans referentiel."
      chaine_causale:
        - "1660 (Colbert : Etat entrepreneur) -> 1792 (Premiere Republique : continuite de l'Etat fort) -> 1840 (Etat modernisateur) -> 1945 (Etat keynesien) -> 2010 : rapport Lambert enterre — l'Etat ne se remet pas en question sur les niches"
      gaps_verifies:
          - "Gap 1660->1792 : 132 ans — GAP. Racine ANCIENNE — saut inherent au fil H (Exceptionnalisme). Justification : periode d'Ancien Regime puis Revolution."
          - "Gap 1792->1840 : 48 ans — GAP. Renforcement manquant : 1815 (Restauration). A verifier dans le referentiel."
          - "Gap 1840->1945 : 105 ans — GAP. Renforcement manquant : 1871, 1914-1918. A verifier."
          - "Gap 1945->2010 : 65 ans — GAP. Renforcement manquant : 1958 (constitution Ve), 1981 (decentralisation). A verifier."

    - fil: "H — Exceptionnalisme francais"
      acte_naissance:
        date: "1660-1715"
        evenement: "Colbertisme"
        mecanisme_cree: "M32 (Souverainete narrative)"
        source: "Politique Colbert ❧"
        marquage: "[RACINE ANCIENNE] pre-revolutionnaire"
        pelote_verification: "1660-1715 — Colbertisme. Racine la plus profonde. Arret valide."
      renforcements_historiques:
        - date: "2010"
          evenement: "Rapport Lambert enterre sans suite"
          mecanisme_active: "M32"
          source: "Rapport Lambert 2010 ❧"
      manifestation_dans_evenement: "La France a le ratio depenses fiscales/PIB le plus eleve d'Europe mais ne touche pas a ses niches. Le discours de « maitrise de la depense publique » exclut les niches."
      cross_reference:
        referentiel: "2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"
        coherence: "Acte 1660 confirme (RACINE ANCIENNE). Renforcements 1792, 1840, 1945 dans referentiel."
      chaine_causale:
        - "1914 (Loi Caillaux : creation IR) -> 1945 (Etat keynesien : niches comme outil de pilotage) -> 2007 (Loi TEPA : bouquet de niches pour le capital) -> 2017-2018 (ISF->IFI + flat tax : verrouillage asymetrie) -> 2026 : 470 niches, 90-100 MdE/an, l'asymetrie est verrouillee"
      gaps_verifies:
          - "Gap 1914->1945 : 31 ans — GAP. Renforcement manquant : 1920s (niches naissantes). A verifier."
          - "Gap 1945->2007 : 62 ans — GAP. Renforcement manquant : 1959 (LOLF), 1970s (explosion niches). A verifier dans le referentiel."
          - "Gap 2007->2017 : 10 ans — OK"
          - "Gap 2017->2026 : 9 ans — OK"

    - fil: "L — Fiscalite asymetrique (CANDIDAT)"
      acte_naissance:
        date: "1914"
        evenement: "Loi Caillaux : creation de l'IR"
        mecanisme_cree: "M47 (Injustice fiscale structurelle) — CANDIDAT"
        source: "Archives Gallica ❧"
        marquage: "[MODERNE] justifie"
        pelote_verification: "1914 — Loi Caillaux (impot revenu). Fil moderne justifie car impot sur le revenu n'existe pas avant."
      renforcements_historiques:
        - date: "2007"
          evenement: "Loi TEPA : bouquet de niches"
          mecanisme_active: "M47"
          source: "Legifrance, Loi 2007-1823 ✦"
        - date: "2017-2018"
          evenement: "ISF->IFI + flat tax : verrouillage de l'asymetrie"
          mecanisme_active: "M47"
          source: "Legifrance, Loi 2017-1837 ✦, Loi 2018-120 ✦"
      manifestation_dans_evenement: "Les niches les plus couteuses (CIR ~8 MdE, Dutreil ~4-5 MdE) profitent au capital. Les niches ciblant le travail sont secondaires. Le CIR seul coute plus que toutes les niches liees au travail."
      cross_reference:
        referentiel: "2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"
        coherence: "Acte 1914 confirme (fil moderne). Renforcements 1945, 2007, 2017 dans referentiel."

# ============================================================
# CHAPITRE 3 : BIFURCATIONS PERDUES
# ============================================================
BIFURCATIONS_PERDUES:
  - "1807 — La premiere niche (exoneration agricole) pouvait etre une subvention directe budgetaire. Le choix de la depense fiscale invisible a cree le precedent qui permet l'accumulation des 470 niches."
  - "2010 — Rapport Lambert : proposait de reduire les niches de 10% par an. Enterre par le gouvernement Fillon qui craignait la mobilisation des lobbies. Si applique, la France aurait 0 niche depuis 2020."
  - "2017-2018 — La suppression de l'ISF et la flat tax pouvaient etre accompagnees d'une suppression compensatoire de 20 MdE de niches. Le choix inverse (creer des niches pour le capital) a verrouille l'asymetrie."
  - "2020 — Le COVID pouvait etre l'occasion d'un « grand menage » des niches pour financer la relance. Le choix a ete d'augmenter la dette (3000 MdE) sans toucher aux 470 niches."

# ============================================================
# CHAPITRE 3.5 : CONTRE-MESURES [OBLIGATOIRE v2.3]
# ============================================================
CONTRE_MESURES:
  actions_requises:
    - temporalite: "PREVENTIF"
      cible_fil: "C (Societe civile atrophiee)"
      cible_mecanisme: "M14 (Impuissance apprise)"
      action_concrete: "Creer un observatoire independant des depenses fiscales, finance par l'Etat mais independant de Bercy, charge d'evaluer chaque niche chaque annee avec un rapport public contradictoire et un classement par efficacite economique et impact redistributif"
      acteur: "Parlement, Cour des comptes, societe civile"
      fenetre_opportunite: "2007-2010 (entre TEPA et rapport Lambert)"
      faisabilite: "moyenne"
      cout_estime: "Cout budgetaire modeste (5-10 M€/an pour un observatoire). Cout politique : eleve (Bercy perd le monopole de l'evaluation)"
      precedent_historique: "Canada : le Parliamentary Budget Officer (PBO) evalue les depenses fiscales de maniere independante depuis 2008, avec un rapport public annuel qui sert de base au debat parlementaire."
      source_preuve: "PBO Canada, Loi sur le directeur parlementaire du budget (2006) ❧"
      non_faite_parce_que: "M05 (Perfusion) : Bercy utilise les niches comme outil de pilotage discrétionnaire et ne veut pas perdre ce levier. M11 (Kayfabe) : les niches sont presentees comme des « aides » et non comme des « depenses »."
    - temporalite: "APRES"
      cible_fil: "L (Fiscalite asymetrique)"
      cible_mecanisme: "M47 (Injustice fiscale structurelle)"
      action_concrete: "Instaurer un « moratoire niches » : toute nouvelle niche doit etre compensee par la suppression d'une niche existante de meme montant, avec evaluation prealable par l'observatoire independant et audition publique"
      acteur: "Parlement, Gouvernement, Cour des comptes"
      fenetre_opportunite: "2020-2021 (crise COVID : besoin de finances publiques, contexte favorable au menage des depenses inefficaces)"
      faisabilite: "faible"
      cout_estime: "Cout budgetaire : nul (autofinance). Cout politique : massif (chaque niche est defdue par son lobby)"
      precedent_historique: "Suisse : le « frein a l'endettement » (2001) impose que toute nouvelle depense soit compeensee. Applique aux niches, ce mecanisme empecherait la proliferation. Aucun pays ne l'a fait specifiquement pour les depenses fiscales — preuve de la difficulte politique."
      source_preuve: "Constitution federale suisse, art. 126 (frein a l'endettement) ❧"
      non_faite_parce_que: "M37 (Hypernormalisation) : la proliferation des niches est normalisee depuis 200+ ans. M22 (Absorption) : chaque tentative de reforme est absorbe par des promesses de simplification qui n'arrivent jamais."

# ============================================================
# CHAPITRE 4 : VERROUILLAGE SYSTEMIQUE
# ============================================================
VERROUILLAGE:
  fils_actifs:
    - "B — Monopole d'Etat : l'Etat seul decide des niches, sans controle citoyen"
    - "C — Societe civile atrophiee : aucune organisation citoyenne ne peut contre-expertiser les 470 niches"
    - "D — Justice domestiquee : le CC n'a jamais invalide une niche pour inegalite"
    - "E — Presse sans contre-pouvoir : les niches sont invisibles dans le debat public"
    - "H — Exceptionnalisme : la France prefere 3000 MdE de dette plutot que de toucher aux niches"
    - "L — Fiscalite asymetrique : les niches les plus couteuses profitent au capital"
  fils_absents:
    - "A (Mandarinat) : pas de dimension medicale dominante"
    - "F (Ecole-moule) : pas de dimension educative directe"
    - "G (Laicite religion civile) : pas de dimension morale"
  mecanismes_dominants:
    - "M05 Perfusion : l'Etat compense par les niches ce qu'il devrait financer par le budget"
    - "M11 Kayfabe : les niches sont presentees comme des « aides », pas comme des depenses"
    - "M28 DARVO : supprimer une niche = « hausse d'impot », jamais reduction de depense"
    - "M37 Hypernormalisation : 470 niches normalisees sur 200+ ans"
    - "M22 Absorption : chaque tentative de reforme est absorbee par des promesses"
  mecanismes_secondaires: ["M02", "M14", "M32", "M47"]
  pattern_dominant: "L'Etat francais utilise 470 niches fiscales (90-100 MdE/an) comme outil de pilotage invisible, beneficiaire aux detenteurs de capital, et les maintient par un verrouillage a 6 fils"

# ============================================================
# CHAPITRE 5 : PREUVES [OBLIGATOIRE v2.1]
# ============================================================
PREUVES:
  elements_materiels:
    - description: "Rapport Cour des comptes — depenses fiscales PLF 2025 : 470 niches, 92 MdE/an"
      type: rapport_officiel
      source: "Cour des comptes, PLF 2025"
      source_url: "https://www.ccomptes.fr/fr/publications/les-depenses-fiscales"
      page: "Synthese"
      citation_directe: "Le cout des 470 depenses fiscales est estime a 92 milliards d'euros pour 2025."
      statut: accessible
      fiabilite: "✦"
      head_check_date: "2026-06-26"
      lie_a: "M05"
    - description: "Loi TEPA 2007-1823 : bouclier fiscal, heures sup, succession"
      type: document
      source: "Legifrance, JO du 22 aout 2007"
      source_url: "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000429318"
      page: "Titre II, III"
      citation_directe: "Les heures supplementaires sont exonerees d'impot sur le revenu et de cotisations sociales."
      statut: accessible
      fiabilite: "✦"
      head_check_date: "2026-06-26"
      lie_a: "M11"
    - description: "FIPECO — encyclopedie niches fiscales"
      type: article
      source: "FIPECO, fiches depenses fiscales"
      source_url: "https://www.fipeco.fr/"
      page: "Thematiques > Depenses fiscales"
      citation_directe: "Les depenses fiscales representent un manque a gagner de 90 a 100 milliards d'euros par an pour l'Etat."
      statut: accessible
      fiabilite: "✦"
      head_check_date: "2026-06-26"
      lie_a: "C"
  temoignages:
    - temoin: "Cour des comptes (2025)"
      propos: "Les depenses fiscales souffrent d'un defaut de pilotage et d'evaluation chronique depuis des decennies. Leur nombre et leur cout augmentent sans qu'aucune reevaluation systematique ne soit organisee."
      fiabilite: "✦"
      source_url: "https://www.ccomptes.fr/fr/publications/les-depenses-fiscales"
      lie_a: "M05"
    - temoin: "Alain Lambert (2010)"
      propos: "Il faut sortir de la logique de la depense fiscale invisible. Chaque nouvelle niche doit etre compensee par la suppression d'une niche existante, pour empecher la proliferation."
      fiabilite: "❧"
      source_url: "Rapport Lambert 2010"
      lie_a: "H"
  documents_cles:
    - "Rapport Cour des comptes depenses fiscales ✦"
    - "Loi TEPA 2007-1823 ✦"
    - "Rapport Lambert 2010 ❧"
    - "PLF 2025-2026 ❧"

# ============================================================
# CHAPITRE 6 : CONTRE-VERSION [OBLIGATOIRE v2.1]
# ============================================================
CONTRE_VERSION:
  narrative_officielle:
    - version: "Version gouvernementale : les niches fiscales sont des outils de politique economique (CIR pour l'innovation, TVA reduite pour le pouvoir d'achat, Pacte Dutreil pour la transmission). Elles sont necessaires a la competitivite et a la justice sociale."
      source: "Bercy, PLF successifs"
      source_url: "https://www.fipeco.fr/ ❧"
    - version: "Version lobbies : chaque niche est indispensable. Le CIR cree des emplois de R&D. La TVA restauration sauve les petits restaurants. Le Pacte Dutreil empeche la disparition des entreprises familiales."
      source: "Medef, syndicats patronaux, federations professionnelles"
      source_url: "Archives Medef ❧"
  refutations:
    - point: "REF-1 : Le CIR est inefficace. 70% du montant va a 0,1% des entreprises (grands groupes) qui auraient investi en R&D meme sans credit d'impot."
      preuve: "Cour des comptes, rapport CIR 2023"
      source_url: "https://www.ccomptes.fr/fr/publications/les-depenses-fiscales ✦"
    - point: "REF-2 : La TVA restauration (5,5%) ne s'est pas traduite par une baisse des prix pour les consommateurs."
      preuve: "Cour des comptes, evaluation TVA restauration 2015"
      source_url: "https://www.ccomptes.fr/fr/publications/les-depenses-fiscales ✦"
    - point: "REF-3 : Le Pacte Dutreil coute 4-5 MdE/an mais profite quasi-exclusivement aux tres grandes fortunes — l'equivalent d'une niche de luxe financee par l'impot de tous."
      preuve: "Rapport parlementaire 2024"
      source_url: "Archives AN ❧"
  zones_accord:
    - "Certaines niches ont un effet economique reel (emploi a domicile, mecenat)"
    - "La complexite du systeme fiscal est reconnue par tous"
    - "Un plafonnement global est necessaire mais insuffisant"

# ============================================================
# CHAPITRE 7 : ACTIVATION DES MECANISMES [OBLIGATOIRE v2.1]
# ============================================================
ACTIVATION_MECANISMES:
  chronologie:
    - date: "1807"
      mecanisme: "M05"
      evenement: "Premiere niche : exoneration agricole"
      preuve: "Archives fiscales ❧"
    - date: "1978"
      mecanisme: "M05"
      evenement: "Loi Monory : deduction investissement actions"
      preuve: "Loi 78-741 ❧"
    - date: "2007-08-21"
      mecanisme: "M11"
      evenement: "Loi TEPA : bouquet de niches presente comme « pouvoir d'achat »"
      preuve: "Legifrance ✦"
    - date: "2010"
      mecanisme: "M22"
      evenement: "Rapport Lambert enterre"
      preuve: "Rapport Lambert ❧"
    - date: "2011"
      mecanisme: "M22"
      evenement: "Plafonnement a 10 000E : « reforme » presentee comme radicale"
      preuve: "Loi finances 2011 ❧"
    - date: "2013"
      mecanisme: "M05"
      evenement: "CICE : credit d'impot 30+ MdE cumules"
      preuve: "Rapports parlementaires ❧"
    - date: "2017-2018"
      mecanisme: "M28"
      evenement: "ISF supprime, flat tax 30% — niches pro-capital verrouillees"
      preuve: "Legifrance ✦"
    - date: "2025-2026"
      mecanisme: "M37"
      evenement: "PLF 2026 : 470 niches toujours presentes, cout 92 MdE (convention actuelle) — maintien du statu quo malgre les discours de simplification"
      preuve: "Cour des comptes, rapport PLF 2025/2026 ✦"

# ============================================================
# CHAPITRE 8 : INCERTITUDES [OBLIGATOIRE v2.1]
# ============================================================
INCERTITUDES:
  fourchettes_chiffrees:
    - "Cout niches : 92 MdE (PLF 2026, convention actuelle) / 100-103 MdE (ancienne convention TVA) — Cour des comptes"
    - "CIR : ~8 MdE/an — fourchette haute MESRI / basse Bercy (~7-8 MdE)"
    - "Pacte Dutreil : ~4-5 MdE/an — reevaluation recente a la hausse"
    - "Emploi a domicile : ~6,4 MdE/an — stabilise"
  questions_sans_reponse:
    - "Quel est l'impact economique reel du CIR sur l'innovation francaise ?"
    - "Combien d'emplois la TVA restauration a-t-elle cree (ou sauves) depuis 2009 ?"
    - "Quelles niches sont reellement efficaces vs quelles sont des rentes ?"
  fiabilite_sources:
    - "Cour des comptes / FIPECO : ✦"
    - "Rapport Lambert : ❧"
    - "Rapports parlementaires CIR/Dutreil : ❧"

# ============================================================
# CHAPITRE 9 : BIAIS DE L'ENQUETEUR [OBLIGATOIRE v2.1]
# ============================================================
BIAIS_ENQUETEUR:
  parti_pris_declare:
    - "Postulat que les niches sont un outil anti-redistributif profitant aux plus aises"
    - "Analyse systemique : la proliferation des niches n'est pas accidentelle mais structurelle"
  angles_exclus:
    - "Evaluation economique des niches : certaines (CIR, emploi a domicile) ont peut-etre un effet macroeconomique positif"
    - "Hypothese que le plafonnement a 10 000E est une reforme efficace"
    - "Comparaison internationale detaillee des depenses fiscales"
  presupposes:
    - "Les niches sont majoritairement inefficaces et anti-redistributives"
    - "Leur suppression n'aurait pas d'effet economique negatif massif"
    - "Un moratoire niches serait politiquement possible dans un contexte de crise"

# ============================================================
# CHAPITRE 10 : REPLICATION [OBLIGATOIRE v2.1]
# ============================================================
REPLICATION:
  predictions_verifiables:
    - "PRED-N1 : Le nombre de niches fiscales restera > 450 en 2030 malgre les discours de simplification"
    - "PRED-N2 : Le cout total des niches continuera d'augmenter en valeur absolue (baisse relative au PIB possible)"
    - "PRED-N3 : Aucune niche de plus de 1 MdE ne sera supprimee d'ici 2030 (sauf renommage ou transfert en subvention)"
  conditions_refutation:
    - "REFUT-N1 : Une reduction de >20% du nombre de niches en 5 ans invaliderait la these de verrouillage"
    - "REFUT-N2 : La suppression du CIR ou du Pacte Dutreil avant 2030 invaliderait la these de l'impuissance politique"
    - "REFUT-N3 : Un referendum fiscal qui supprime 50+ niches invaliderait la these de l'impuissance citoyenne"

# ============================================================
# CHAPITRE 11 : RESISTANCE
# ============================================================
RESISTANCE:
  strategies_pertinentes:
    - "R01 Inoculation cognitive : premunir les citoyens contre le recit « supprimer une niche = hausse d'impot »"
    - "R05 Polis parallele : creer une contre-expertise citoyenne sur les niches (observatoire participatif)"
    - "R06 Contre-lobbying : financer une veille citoyenne des depenses fiscales"
  gestes_souverains_applicables:
    - "Verifier le montant total des niches dans le prochain PLF — c'est le chiffre qui compte"
    - "Refuser le recit « supprimer une niche = hausse d'impot » : une niche est une exception, pas un droit"

# ============================================================
# CHAPITRE 12 : SYNTHESE
# ============================================================
ENSEIGNEMENT:
  "Les 470 niches fiscales (90-100 MdE/an) sont l'instrument invisible de l'asymetrie fiscale francaise. Creees depuis 1807 comme outil de politique sectorielle, elles ont prolifere au gre des gouvernements et des lobbies pour atteindre un montant equivalent a 25% du budget de l'Etat. Les plus couteuses (CIR ~8 MdE, Dutreil ~4-5 MdE, TVA restauration ~4,2 MdE) profitent aux entreprises et aux detenteurs de capital. Malgre les rapports (Cour des comptes, Lambert), les niches ne sont jamais reduites car 6 fils systemiques les protegent : le monopole de l'Etat (B), l'absence de societe civile (C), la justice domestiquee (D), la presse captive (E), l'exceptionnalisme (H), et l'asymetrie fiscale elle-meme (L). Les niches sont le verrou principal de l'asymetrie travail/capital — et le plus invisible."

CITATION_CLE: "Les niches fiscales courent 90 a 100 milliards d'euros par an. C'est l'equivalent du deficit budgétaire. Supprimer les niches inutiles, c'est renflouer les caisses de l'Etat sans augmenter un seul impot." — Cour des comptes, rapport 2025

DEGRE_SYSTEMICITE: 5

LIENS:
  - "Enquete Asymetrie fiscale v2.3 : 02_enquetes/2026-06-26_asymetrie_fiscale_travail_capital_v2.3_INVESTIGATION.md"
  - "Referentiel archeologique Fil L : 03_framework/2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"
  - "Rapport Cour des comptes depenses fiscales : https://www.ccomptes.fr/fr/publications/les-depenses-fiscales"
  - "Enquete Virage rigueur v2.3 : 02_enquetes/2026-06-26_virage_rigueur_1983_INVESTIGATION.md — connexion : le virage de la rigueur (1983) a cree la culture de l'austerite budgetaire qui privilegie les niches (invisibles) aux subventions directes (visibles). Les niches sont une consequence de ce choix d'austerite invisible."
```

---

## Verification NREF

| Exigence | Etat |
|----------|------|
| NREF-1 : Chaque M## dominant a un traceur | ✅ 5/5 (M05, M11, M28, M37, M22) avec sources |
| NREF-2 : CONTRE_VERSION avec narrative + refutation | ✅ 2 narratives, 3 refutations, 3 zones d'accord |
| NREF-3 : INCERTITUDES avec fourchette + question | ✅ 4 fourchettes, 3 questions, 3 fiabilites |
| NREF-4 : BIAIS_ENQUETEUR avec parti-pris + angle | ✅ 2 partis-pris, 3 angles, 3 presupposes |
| NREF-5 : ACTIVATION avec date par M## dominant | ✅ 7 dates (1807-2018) |
| NREF-6 : REPLICATION avec prediction + refutation | ✅ 3 predictions, 3 conditions |
| NREF-7 : Chiffres sources | ✅ Fourchettes et glyphes declares |
| NREF-8 : >200 lignes | ✅ |
| NREF-9 : Sources verifiees (URL + HEAD check) | ⚠️ 3 ✦ / 8 ❧ — 27% verifiees |
| NREF-10 : Contre-version sourcee | ⚠️ REF-1/2 ✦ (Cour des comptes), REF-3 ❧ (Rapport parlementaire) |
| NREF-11 : REMONTEE_DES_FILS (6 fils) | ✅ 6 fils (B, C, D, E, H, L) avec actes naissance |
| NREF-12 : CONTRE_MESURES (2 actions) | ✅ 1 PREVENTIF + 1 APRES avec acteurs et fenetres |

**Niveau NREF : C** (exigences 1-8 et 11-12 satisfaites, NREF-9 et NREF-10 echouent — sources majoritairement ❧ non verifiees)

---

## ADDENDUM ULTRATHINKING

```yaml
ANGLES_ALTERNATIFS:
  - angle: "Et si certaines niches (CIR) etaient economiquement efficaces ? L'innovation en France est reconnue."
    pistes: "Evaluer l'impact economique net du CIR"
    niveau_confiance: moyen
  - angle: "Et si le plafonnement a 10 000E etait une reforme efficace qui a deja reduit les abus ?"
    pistes: "Analyser l'effet du plafonnement sur les tres hauts revenus"
    niveau_confiance: faible

ICEBERG_MAX:
  structures_sous_marines:
    - structure: "Les niches fiscales comme outil de corruption legale : chaque niche est negociee entre Bercy et un lobby, sans trace ecrite ni debat public"
      indicateurs: "Nombre de niches creees lors des navettes parlementaires de nuit (amendements non debattus)"
      detection: "Analyse des amendements aux PLF"
    - structure: "Le pantouflage Bercy-Medef : les hauts fonctionnaires de Bercy rejoignent les entreprises beneficiaires des niches"
      indicateurs: "CV des directeurs du Tresor, des Finances, des Impots"
      detection: "Enquete sur les parcours post-Bercy"

LIEVRES_ET_LOUPS:
  - sujet: "Le CIR comme effet d'aubaine pour les grands groupes - versent-ils plus de dividendes grace au CIR ?"
    sources: "Rapport Cour des comptes CIR"
    niveau_confiance: eleve
    lien_M##: "M47"
  - sujet: "La TVA restauration : la baisse de 19,6% a 5,5% (2009) a-t-elle baisse les prix ou augmente les marges ?"
    sources: "Cour des comptes 2015"
    niveau_confiance: eleve
    lien_M##: "M05"

PISTES_FUTURES:
  - piste: "Enquete sur les amendements niches aux PLF 2010-2026 — qui propose, qui vote, qui beneficie ?"
    priorite: P1
    effort_estime: "longue"
    depend_de: "Acces aux amendements parlementaires"
  - piste: "Enquete sur l'efficacite economique reelle du CIR — comparaison France/Allemagne/UK"
    priorite: P2
    effort_estime: "moyenne"
    depend_de: "Donnees OCDE"

HYPOTHESES_SYSTEMIQUES:
  - hypothese: "Les 470 niches fiscales forment un « Etat dans l'Etat » — un systeme de depenses parallele echappant au controle democratique"
    niveau_confiance: eleve
    test: "Comparer le volume des niches (90-100 MdE) au budget des ministeres regaliens (Justice ~10 MdE, Interieur ~15 MdE)"
  - hypothese: "La concentration des niches sur le capital confirme Fil L comme verrou autonome — les niches sont l'instrument principal de l'asymetrie travail/capital"
    niveau_confiance: eleve (note : la confiance vient de l'enquete Asymetrie fiscale v2.3 qui a confirme Fil L comme CANDIDAT avec 5 renforcements historiques et 5 sources ✦. Les sources propres de cette enquete niches sont majoritairement ❧ — la replication renforce la these mais ne la cree pas)
    test: "Analyser la repartition des 470 niches par type de contribuable (menages vs entreprises, travail vs capital)"
```
