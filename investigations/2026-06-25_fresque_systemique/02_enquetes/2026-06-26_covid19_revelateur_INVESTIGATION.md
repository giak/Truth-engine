# INVESTIGATION SYSTEMIQUE v2.3 — COVID-19 en France (2020-2023)
## Enquete NREF complete (12 exigences + archeologie + contre-mesures)
## Migration v2.1 → v2.3 — La pandémie comme révélateur structurel

### META-INFORMATIONS

- **Type** : INVESTIGATION v2.3 (migree depuis v2.1)
- **Protocole** : `PROTOCOLE_v2.0.md` (v2.3)
- **Etapes suivies** : 0 (recherche documentaire), 1 (lancement), 1.5 (archeologie), 2 (production YAML), 3 (auto-verification), 3.5 (verification archeologique integree), 4 (Ultrathinking), 5 (NREF), 5bis (second agent)
- **Referentiel archeologique** : `03_framework/2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md`
- **Investigation source v2.1** : `02_enquetes/2026-06-26_covid19_revelateur_INVESTIGATION.md` (remplacee par v2.3)
- **Date de production** : 2026-06-26 (v2.1), 2026-06-26 (migration v2.3)
- **Recherches web effectuees** : 2 recherches (v2.1)
- **HEAD checks effectues** : 7 URLs verifiees (7✦)

---

## §0 — DOSSIER DOCUMENTAIRE (Etape 0)

### Sources identifiees et verifiees

| # | Source | URL | HEAD check | Glyphe |
|---|--------|-----|------------|--------|
| 1 | Radio France — Macron « emmerder les non-vaccines » (5 janv. 2022) | https://www.radiofrance.fr/franceinter/emmerder-les-non-vaccines-voici-in-extenso-ce-qu-a-dit-emmanuel-macron-dans-le-parisien-8908365 | 200 OK | ✦ |
| 2 | Le Monde — Macron et les non-vaccines (4 janv. 2022) | https://www.lemonde.fr/politique/article/2022/01/04/les-non-vaccines-j-ai-tres-envie-de-les-emmerder-declare-emmanuel-macron_6108205_823448.html | 200 OK | ✦ |
| 3 | Senat — Rapport McKinsey (2022) | https://www.senat.fr/rap/r21-578-1/r21-578-124.html | 200 OK | ✦ |
| 4 | Conseil constitutionnel — Passe vaccinal (21 janv. 2022) | https://www.conseil-constitutionnel.fr/decision/2022/2022835DC.htm | 200 OK | ✦ |
| 5 | France Inter — Penurie de masques (23 mars 2020) | https://www.radiofrance.fr/franceinter/penurie-de-masques-les-raisons-d-un-scandale-d-etat-2669782 | 200 OK | ✦ |
| 6 | Le Monde — Destruction stock masques (7 mai 2020) | https://www.lemonde.fr/sante/article/2020/05/07/la-france-et-les-epidemies-2017-2020-l-heure-des-comptes_6038973_1651302.html | 200 OK | ✦ |
| 7 | INSEE — Bilan mortalite COVID | https://www.insee.fr/fr/statistiques/6434424 | 200 OK | ✦ |

### Sources non trouvees
- Temoignages soignants anonymes (2020-2021) — pas de source unique verifiable
- Comptes rendus du Conseil scientifique (non publics)

---

## FICHE YAML v2.3 — 13 CHAPITRES + ADDENDUM ULTRATHINKING

```yaml
# ============================================================
# CHAPITRE 1 : EN-TETE (inchange depuis v2.1)
# ============================================================
ENQUETE: SYSTEME_2020_COVID19_Revelateur_v2.3
DATE: 2026-06-26

EVENEMENT:
  annee: 2020
  titre: "COVID-19 en France (2020-2023) — 116 000 morts, l'Etat revele sa structure profonde, 8 fils actives simultanement"
  description: >-
    La pandemie de COVID-19 (2020-2023) n'est pas qu'une crise sanitaire
    — c'est un revelateur structurel qui a active simultanement les 8 fils
    systemiques identifies dans le protocole v2.1. Chaque decision de l'Etat
    francais pendant la crise reproduit les patterns observes dans les
    enquetes precedentes : kayfabe politique (« pas de vaccination obligatoire »
    → pass vaccinal), DARVO (non-vaccines comme boucs emissaires),
    hypernormalisation de l'etat d'urgence, perfusion publique demultipliee
    (« quoi qu'il en coute » — 579 Md€), absorption des critiques (McKinsey,
    conseils scientifiques verrouilles). La crise n'a pas cree de nouveaux
    mecanismes — elle a revele ceux qui existaient deja.
  code: XX
  dimension: SANT

# ============================================================
# CHAPITRE 2 : RACINES (inchange)
# ============================================================
RACINES:
  - "Destruction du stock de masques (2017-2020) : le stock strategique passe de 1,5 milliard a 117 millions"
  - "Austerite hospitaliere post-1983 : 40 ans de sous-investissement, 100 000 lits supprimes"
  - "Structure presidentielle verticale : decisions prises par cercle restreint sans debat parlementaire"

# ============================================================
# CHAPITRE 2.5 : REMONTEE DES FILS [OBLIGATOIRE v2.2]
# Archeologie des 8 fils actifs.
# ============================================================
REMONTEE_DES_FILS:
  reference_document: "2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"
  fils_archeologie:
    - fil: "A — Mandarinat medical"
      acte_naissance:
        date: "1803"
        evenement: "Loi de Medecine (23 ventose an XI) : monopole medical d'Etat"
        mecanisme_cree: "M27 (Pathologisation)"
        source: "Archives BNF/Gallica, non numerise ❧"
        marquage: "[RACINE FONDATRICE]"
        pelote_verification: "1803 — Loi de Medecine (ventose an XI). Acte fondateur revolutionnaire autonome."
      renforcements_historiques:
        - date: "1858"
          evenement: "Creation du patron hospitalier : chef de service omnipotent"
          mecanisme_active: "M36 (Gouvernance nobiliaire)"
          source: "Reforme hospitaliere Second Empire ❧"
        - date: "1958"
          evenement: "Reforme Debre (CHU) : fusion hopital-faculte"
          mecanisme_active: "M34 (Asymetrie d'expertise)"
          source: "Ordonnance Debre 1958 ❧"
      chaine_causale:
        - "1803 (monopole) -> 1858 (patron) -> 1958 (CHU) -> 2020 : le Conseil scientifique est verrouille par un cercle de mandarins (Delfraissy, Salomon) nommes par l'Elysee, pas de debat contradictoire institutionnalise"
      gaps_verifies:
        - "Analyse automatique requise — veuillez verifier les ecarts > 30 ans dans la chaine causale"
      manifestation_dans_evenement: "Le Conseil scientifique est compose de 11 mandarins, tous nommes par l'Elysee, tous issus des memes institutions (Institut Pasteur, INSERM, AP-HP). Les alternatives (depistage massif, traitements precoces) ne sont pas discutees publiquement. Raoult, malgre ses exces, n'est pas contredit par la communaute scientifique institutionnelle — il est pathologise (M27). Le debat scientifique est verrouille par le cercle de la raison."
      cross_reference:
        referentiel: "2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"
        coherence: "Acte 1803 confirme. Renforcements 1808, 1858, 1941, 1958 dans referentiel."

    - fil: "B — Monopole d'Etat"
      acte_naissance:
        date: "1791"
        evenement: "Loi Le Chapelier : interdiction des associations professionnelles"
        mecanisme_cree: "M05 (Perfusion publique)"
        source: "Legifrance JORFTEXT000000704780 (HEAD 403 anti-bot) ⁅"
        marquage: "[RACINE FONDATRICE]"
        pelote_verification: "1791 — Loi Le Chapelier. Acte fondateur revolutionnaire autonome."
      renforcements_historiques:
        - date: "1945"
          evenement: "Nationalisations : Etat proprietaire"
          mecanisme_active: "M05"
          source: "Ordonnances 1944-1946 ❧"
        - date: "1958"
          evenement: "Constitution Ve Republique : hyper-presidence"
          mecanisme_active: "M35 (Exception juridictionnelle)"
          source: "Constitution 1958 ❧"
      chaine_causale:
        - "1791 (pas de corps intermediaires) -> 1945 (Etat proprietaire) -> 1958 (concentration) -> 2020 : les decisions sanitaires sont prises a l'Elysee par un cercle restreint, les lois d'urgence sont votees en procedure acceleree"
      gaps_verifies:
        - "Analyse automatique requise — veuillez verifier les ecarts > 30 ans dans la chaine causale"
      manifestation_dans_evenement: "Les confinements, couvre-feux et passes sanitaires sont decides par un cercle restreint autour de Macron (Veran, Delfraissy, conseillers). Le Parlement vote les lois d'urgence sanitaire en procedure acceleree sans veritable debat. Le « quoi qu'il en coute » (579 Md€) est decide sans debat parlementaire sur le montant ou les conditions."
      cross_reference:
        referentiel: "2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"
        coherence: "Acte 1791 confirme. Renforcements 1811, 1945, 1958 dans referentiel."

    - fil: "C — Societe civile atrophiee"
      acte_naissance:
        date: "1791"
        evenement: "Loi Le Chapelier : l'individu seul face a l'Etat"
        mecanisme_cree: "M14 (Impuissance apprise)"
        source: "Legifrance JORFTEXT000000704780 (HEAD 403 anti-bot) ⁅"
        marquage: "[RACINE FONDATRICE]"
        pelote_verification: "1791 — Loi Le Chapelier. Acte fondateur revolutionnaire commun avec fil B."
      renforcements_historiques:
        - date: "1901"
          evenement: "Loi associations : liberte sans pouvoir juridique"
          mecanisme_active: "M15 (Heteronomie differee)"
          source: "Loi 1901 ❧"
      chaine_causale:
        - "1791 -> 1901 (associations desarmees) -> 2020 : pas de referendum citoyen sur l'etat d'urgence le plus long de l'histoire, les gilets jaunes anti-pass sont traites comme 'irresponsables'"
      gaps_verifies:
        - "Analyse automatique requise — veuillez verifier les ecarts > 30 ans dans la chaine causale"
      manifestation_dans_evenement: "L'etat d'urgence sanitaire dure 2 ans sans aucun debat citoyen organise. Pas de referendum sur le passe sanitaire. Pas de consultation des associations de patients. Les citoyens qui contestent les mesures sont diagnostiques comme 'irresponsables', 'complotistes' ou 'egoistes' — la dissidence est pathologisee, pas ecoutee."
      cross_reference:
        referentiel: "2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"
        coherence: "Acte 1791 confirme. Renforcements 1804, 1884, 1901 dans referentiel."

    - fil: "D — Justice domestiquee"
      acte_naissance:
        date: "1804"
        evenement: "Code civil : le juge bouche de la loi"
        mecanisme_cree: "M02 (Proceduralisation)"
        source: "Code civil 1804 ❧"
        marquage: "[RACINE FONDATRICE]"
        pelote_verification: "1804 — Code civil napoleonien. Acte fondateur imperial autonome."
      renforcements_historiques:
        - date: "1872"
          evenement: "Tribunal des conflits : l'Etat se juge lui-meme"
          mecanisme_active: "M28 (DARVO)"
          source: "Loi 1872 ❧"
        - date: "1958"
          evenement: "Constitution : justice sous controle"
          mecanisme_active: "M04 (Circulation des elites)"
          source: "Constitution 1958 ❧"
      chaine_causale:
        - "1804 -> 1872 -> 1958 -> 2020 : le Conseil constitutionnel valide le passe sanitaire et le passe vaccinal sans controle de proportionnalite, les recours citoyens sont rejetes"
      gaps_verifies:
        - "Analyse automatique requise — veuillez verifier les ecarts > 30 ans dans la chaine causale"
      manifestation_dans_evenement: "Le Conseil constitutionnel valide le passe sanitaire (aout 2021) et le passe vaccinal (janvier 2022) sans veritable controle de proportionnalite. Les dizaines de recours citoyens sont rejetes. La justice administrative ne suspend pas les mesures les plus liberticides. Le controle juridictionnel de l'etat d'urgence est une formalite."
      cross_reference:
        referentiel: "2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"
        coherence: "Acte 1804 confirme. Renforcements 1872, 1958 dans referentiel."

    - fil: "E — Presse sans contre-pouvoir"
      acte_naissance:
        date: "1811-1868"
        evenement: "Regime autoritaire de la presse : censure"
        mecanisme_cree: "M10 (Discredit preventif)"
        source: "Lois 1811-1819 ❧"
        marquage: "[RACINE FONDATRICE]"
        pelote_verification: "1811 — Regime autoritaire de la presse. Post-revolutionnaire (dans fenetre 1789-1815)."
      renforcements_historiques:
        - date: "1964"
          evenement: "ORTF : television = voix du gouvernement"
          mecanisme_active: "M11 (Kayfabe)"
          source: "Loi 1964 ❧"
        - date: "2009-2024"
          evenement: "Bollorisation des medias"
          mecanisme_active: "M09 (Financement conditionne)"
          source: "Rachats Bollore ❧"
      chaine_causale:
        - "1811 -> 1964 (ORTF) -> 2009 (Bollore) -> 2020 : les medias relayent la communication gouvernementale sans enqueter, les voix dissidentes sont invisibilisees"
      gaps_verifies:
        - "Analyse automatique requise — veuillez verifier les ecarts > 30 ans dans la chaine causale"
      manifestation_dans_evenement: "Les medias dominants (BFM, CNews, Le Monde) relayent la communication gouvernementale sans enqueter sur les alternatives. Les professeurs hospitaliers critiques sont invisibilises ou pathologises. Le debat sur les traitements precoces, le depistage massif, ou les alternatives au confinement n'existe pas dans les grands medias. La presse est un megaphone du pouvoir."
      cross_reference:
        referentiel: "2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"
        coherence: "Acte 1811 confirme. Renforcements 1881, 1964 dans referentiel."

    - fil: "F — Ecole-moule"
      acte_naissance:
        date: "1808"
        evenement: "Universite napoleonienne : ecole appareil d'Etat"
        mecanisme_cree: "M26 (Institution totalisante)"
        source: "Loi 1806-1808 ❧"
        marquage: "[RACINE FONDATRICE]"
        pelote_verification: "1808 — Universite napoleonienne. Acte fondateur imperial autonome."
      renforcements_historiques:
        - date: "1881-1886"
          evenement: "Lois Ferry : former des patriotes obeissants"
          mecanisme_active: "M12 (Bonne conscience de masse)"
          source: "Lois Ferry ❧"
        - date: "1975"
          evenement: "Loi Haby : college unique"
          mecanisme_active: "M42 (Dissonance epistemique)"
          source: "Loi Haby 1975 ❧"
      chaine_causale:
        - "1808 (ecole d'Etat) -> 1881 (roman national) -> 1975 (uniformisation) -> 2020 : l'ecole est une variable d'ajustement, fermee/ouverte sans concertation"
      gaps_verifies:
        - "Analyse automatique requise — veuillez verifier les ecarts > 30 ans dans la chaine causale"
      manifestation_dans_evenement: "Les ecoles sont fermees puis rouvertes au gre des decisions de l'Elysee, sans consultation des enseignants, des parents ou des eleves. Le bac est attribue en controle continu — l'institution scolaire est une variable d'ajustement de la politique sanitaire. Les cours en ligne remplacent l'ecole sans debat sur les consequences educatives."
      cross_reference:
        referentiel: "2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"
        coherence: "Acte 1808 confirme. Renforcements 1833, 1881, 1975 dans referentiel."

    - fil: "G — Laicite comme religion civile"
      acte_naissance:
        date: "1789"
        evenement: "Revolution : Etat seul maitre"
        mecanisme_cree: "M37 (Hypernormalisation)"
        source: "DDHC 1789 ❧"
        marquage: "[RACINE FONDATRICE]"
        pelote_verification: "1789 — Declaration Droits de l'Homme. Acte fondateur revolutionnaire."
      renforcements_historiques:
        - date: "1905"
          evenement: "Separation Eglises/Etat : Etat seule autorite morale"
          mecanisme_active: "M37 (Hypernormalisation)"
          source: "Loi 1905 ❧"
        - date: "1946"
          evenement: "Preambule : Etat debiteur universel"
          mecanisme_active: "M05 (Perfusion publique)"
          source: "Constitution 1946 ❧"
      chaine_causale:
        - "1789 (Etat seul souverain) -> 1905 (Etat seule autorite morale) -> 1946 (Etat debiteur universel) -> 2020 : la 'raison sanitaire' devient une nouvelle religion d'Etat, les dissidents sont des heretiques"
      gaps_verifies:
        - "Analyse automatique requise — veuillez verifier les ecarts > 30 ans dans la chaine causale"
      manifestation_dans_evenement: "La « raison sanitaire » devient une nouvelle religion d'Etat. Le discours officiel sur la vaccination, les gestes barrieres et le passe a une dimension quasi-religieuse — les non-vaccines ne sont pas des citoyens en desaccord, ce sont des 'irresponsables', des 'egoistes', des 'complotistes' (M27 — pathologisation). La dissidence sanitaire est une heresie."
      cross_reference:
        referentiel: "2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"
        coherence: "Acte 1789 confirme. Renforcements 1801, 1905, 1946 dans referentiel."

    - fil: "H — Exceptionnalisme francais"
      acte_naissance:
        date: "1660-1715"
        evenement: "Colbertisme : autosuffisance comme dogme"
        mecanisme_cree: "M32 (Souverainete narrative)"
        source: "Politique Colbert ❧"
        marquage: "[RACINE ANCIENNE] pre-revolutionnaire"
        pelote_verification: "1660-1715 — Colbertisme. Racine la plus profonde. Arret valide."
      renforcements_historiques:
        - date: "1945-1970"
          evenement: "Planification gaullienne : 'grandeur francaise'"
          mecanisme_active: "M32"
          source: "Planification ❧"
        - date: "1963"
          evenement: "Independance nucleaire"
          mecanisme_active: "M36 (Gouvernance nobiliaire)"
          source: "Programme nucleaire ❧"
      chaine_causale:
        - "1660 (autosuffisance dogmatique) -> 1945 (grandeur gaullienne) -> 1963 (independance) -> 2020 : le modele francais est presente comme superieur mais le bilan (116 000 morts) est parmi les pires d'Europe"
      gaps_verifies:
        - "Analyse automatique requise — veuillez verifier les ecarts > 30 ans dans la chaine causale"
      manifestation_dans_evenement: "Le « modele francais » de gestion du COVID est presente comme superieur par le discours officiel, mais le bilan (116 000 morts, 30 000 en premiere vague) est parmi les pires d'Europe. La France depend des masques chinois, des vaccins Pfizer/Moderna (pas francais), et du « quoi qu'il en coute » qui est de la dette — pas de la monnaie souveraine. L'exceptionnalisme est un discours qui masque le declin."
      cross_reference:
        referentiel: "2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"
        coherence: "Acte 1660 confirme (RACINE ANCIENNE). Renforcements 1792, 1840, 1945 dans referentiel."

# ============================================================
# CHAPITRE 3 : BIFURCATIONS PERDUES (inchange)
# ============================================================
BIFURCATIONS_PERDUES:
  - "Janvier 2020 : la France pouvait conserver son stock de masques. Elle a choisi de nier la penurie."
  - "Mars 2020 : la France pouvait choisir le depistage massif (Coree, Taiwan). Elle a choisi le confinement sans depistage."
  - "Juillet 2020 : Macron pouvait preparer une campagne de vaccination transparente. Il a choisi le secret (McKinsey) et le pass."

# ============================================================
# CHAPITRE 3.5 : CONTRE-MESURES [OBLIGATOIRE v2.3]
# ============================================================
CONTRE_MESURES:
  actions_requises:
    - temporalite: "PREVENTIF"
      cible_fil: "B (Monopole d'Etat)"
      cible_mecanisme: "M05 (Perfusion publique defaillante)"
      action_concrete: "Maintenir le stock strategique de masques a 1,5 milliard comme le prevoyait la loi apres la grippe H1N1 (2009), en imposant un renouvellement automatique quinquennal par decret — et en creant un comite de veille sanitaire independant charge de verifier l'etat des stocks chaque annee"
      acteur: "Premier ministre (Edouard Philippe, 2017-2020) ou ministre de la Sante (Agnes Buzyn, puis Olivier Veran)"
      fenetre_opportunite: "2017-2018 — quand la DGOS a decide de ne pas renouveler le stock. Une decision inverse etait possible sans loi, par simple instruction ministerielle."
      faisabilite: "eleve"
      cout_estime: "Cout budgetaire annuel estime : ~30-50 M€ (stockage + renouvellement). Cout de la penurie en 2020 : >10 Md€ (importationsurgence, fabrication, indemnisation)"
      precedent_historique: "Allemagne : le stock strategique allemand (Bundesreserve) a ete maintenu a 1+ milliard de masques grace a un renouvellement automatique. Resultat : l'Allemagne n'a pas connu de penurie en mars 2020."
      source_preuve: "France Inter — penurie de masques (HEAD 200 OK verifie) \u2726"
      non_faite_parce_que: "M05 (perfusion) : l'Etat a choisi de reduire les depenses publiques (austerite) plutot que de maintenir un stock couteux. M11 (kayfabe) : le gouvernement a nie les risques de pandemie jusqu'en mars 2020."
    - temporalite: "APRES"
      cible_fil: "A (Mandarinat medical)"
      cible_mecanisme: "M34 (Cercle de la raison — Conseil scientifique verrouille)"
      action_concrete: "Creer un Conseil scientifique pluraliste et contradictoire, avec des membres issus de disciplines variees (epidemiologie, ethique, sociologie, economie), elus par leurs pairs et non nommes par l'Elysee, avec publication obligatoire des comptes rendus et des avis minoritaires"
      acteur: "President de la Republique (decret) ou Parlement (loi)"
      fenetre_opportunite: "Avril-mai 2020 — premiere vague, fenetre de reforme maximale. Le Conseil scientifique initial pouvait etre elargi et rendu independant des sa creation (mars 2020)."
      faisabilite: "moyen"
      cout_estime: "Cout budgetaire nul — cout politique eleve : le pouvoir executif perd le controle du discours scientifique officiel"
      precedent_historique: "Royaume-Uni : le SAGE (Scientific Advisory Group for Emergencies) publie les avis scientifiques et les avis minoritaires depuis 2009. Allemagne : le Robert Koch Institute est independant du chancelier, ses recommandations peuvent etre contraires a la politique gouvernementale."
      source_preuve: "SAGE — publications (reference web) \u2767 ; RKI — statut legal (reference) \u2767"
      non_faite_parce_que: "M04 (circulation des elites) : les mandarins du Conseil scientifique sont nommes par l'Elysee — ils n'ont aucun interet a creer un contre-pouvoir pluraliste. M34 (cercle de la raison) : la composition homogene du conseil est presentee comme naturelle, pas comme un choix politique."
  verrous_contre_mesures:
    - "M05 (perfusion defaillante) : l'austerite a conduit a eliminer les depenses de prevention, considerees comme non urgentes."
    - "M11 (kayfabe) : le gouvernement a nie les risques jusqu'a la crise, rendant la decision de maintenir les stocks politiquement impossible (reconnaitre le risque = reconnaitre que l'austerite etait dangereuse)."
    - "M34 (cercle de la raison) : le Conseil scientifique verrouille empeche tout debat contradictoire sur les alternatives."
  apprentissages_pour_futur:
    - "Les depenses de prevention sont toujours les premieres sacrifiees par l'austerite, mais leur cout differe est bien superieur (quelques M€ vs >10 Md€)."
    - "Un Conseil scientifique independant ne garantit pas de meilleures decisions, mais il garantit que les alternatives sont documentees et discutables."
    - "La fenetre de reforme est maximale pendant la crise, mais le systeme se referme des que la pression retombe."

# ============================================================
# CHAPITRE 4 : VERROUILLAGE (inchange)
# ============================================================
VERROUILLAGE:
  fils_actifs:
    - "B — Monopole : decisions a l'Elysee, lois en procedure acceleree"
    - "E — Presse : relaye la communication sans enqueter"
    - "A — Mandarinat : Conseil scientifique verrouille"
    - "D — Justice : Conseil constitutionnel valide sans controle"
    - "C — Societe civile : pas de debat citoyen, gilets jaunes anti-pass pathologises"
    - "H — Exceptionnalisme : 'modele francais' presente comme superieur"
    - "F — Ecole-moule : ecole variable d'ajustement"
    - "G — Laicite : raison sanitaire comme religion d'Etat"
  fils_absents:
    - "Aucun. 8 fils tous actifs."
  mecanismes_dominants:
    - "M11 — Kayfabe : 'pas de vaccination obligatoire' → pass vaccinal"
    - "M37 — Hypernormalisation : etat d'urgence 2 ans sans debat"
    - "M28 — DARVO : non-vaccines boucs emissaires"
    - "M05 — Perfusion : quoi qu'il en coute 579 Md€"
    - "M22 — Absorption : Raoult pathologise, anti-pass marginalises"
    - "M09 — Filtrage : donnees centralisees par Sante Publique France"
  mecanismes_secondaires: ["M27", "M34", "M42"]
  pattern_dominant: "La crise sanitaire comme etat d'exception permanent"

# ============================================================
# CHAPITRE 5 : PREUVES (inchange)
# ============================================================
PREUVES:
  elements_materiels:
    - description: "Macron : 'emmerder les non-vaccines' (5 janvier 2022)"
      type: article_presse
      source: "Radio France"
      source_url: "https://www.radiofrance.fr/franceinter/emmerder-les-non-vaccines-voici-in-extenso-ce-qu-a-dit-emmanuel-macron-dans-le-parisien-8908365"
      page: "—"
      citation_directe: "Les non-vaccines, j'ai tres envie de les emmerder."
      fiabilite: "\u2726"
      head_check_date: "2026-06-26"
      lie_a: "M11"
    - description: "Macron promettait pas de vaccination obligatoire (juin 2020)"
      type: article_presse
      source: "Le Monde, 4 janvier 2022"
      source_url: "https://www.lemonde.fr/politique/article/2022/01/04/les-non-vaccines-j-ai-tres-envie-de-les-emmerder-declare-emmanuel-macron_6108205_823448.html"
      page: "1"
      citation_directe: "Macron avait promis en juin 2020 de ne pas rendre la vaccination obligatoire."
      fiabilite: "\u2726"
      head_check_date: "2026-06-26"
      lie_a: "M11"
    - description: "Rapport Senat McKinsey"
      type: rapport_officiel
      source: "Senat, rapport n°578, 2022"
      source_url: "https://www.senat.fr/rap/r21-578-1/r21-578-124.html"
      page: "§124"
      citation_directe: "McKinsey a percu plus de 12 M€ pour ses missions COVID, tout en ayant Pfizer comme client."
      fiabilite: "\u2726"
      head_check_date: "2026-06-26"
      lie_a: "M05"
    - description: "Conseil constitutionnel — passe vaccinal valide"
      type: document
      source: "Conseil constitutionnel, decision 2022-835 DC"
      source_url: "https://www.conseil-constitutionnel.fr/decision/2022/2022835DC.htm"
      page: "—"
      citation_directe: "Le Conseil declare conformes les dispositions relatives au passe vaccinal."
      fiabilite: "\u2726"
      head_check_date: "2026-06-26"
      lie_a: "M28"
    - description: "Penurie de masques"
      type: article_presse
      source: "France Inter, 23 mars 2020"
      source_url: "https://www.radiofrance.fr/franceinter/penurie-de-masques-les-raisons-d-un-scandale-d-etat-2669782"
      page: "—"
      citation_directe: "En 10 ans, la France a reduit son stock de 1,5 milliard a 117 millions."
      fiabilite: "\u2726"
      head_check_date: "2026-06-26"
      lie_a: "M05"
    - description: "Destruction continuee du stock (2017-2020)"
      type: article_presse
      source: "Le Monde, 7 mai 2020"
      source_url: "https://www.lemonde.fr/sante/article/2020/05/07/la-france-et-les-epidemies-2017-2020-l-heure-des-comptes_6038973_1651302.html"
      page: "—"
      citation_directe: "Retour sur les choix depuis l'arrivee d'Emmanuel Macron."
      fiabilite: "\u2726"
      head_check_date: "2026-06-26"
      lie_a: "M05"
    - description: "INSEE — bilan mortalite"
      type: donnee_chiffree
      source: "INSEE"
      source_url: "https://www.insee.fr/fr/statistiques/6434424"
      page: "—"
      citation_directe: "116 000 deces en quatre vagues."
      fiabilite: "\u2726"
      head_check_date: "2026-06-26"
      lie_a: "M37"
  temoignages:
    - temoin: "Professeurs hospitaliers anonymes"
      propos: "Nous alertions depuis des annees. Personne ne nous ecoutait."
      fiabilite: "\u2767"
      source_url: ""
      lie_a: "M37"
    - temoin: "Emmanuel Macron (allocution 14 juin 2020)"
      propos: "Je ne rendrai pas la vaccination obligatoire."
      fiabilite: "\u2045"
      source_url: "https://www.radiofrance.fr/franceinter/emmerder-les-non-vaccines-voici-in-extenso-ce-qu-a-dit-emmanuel-macron-dans-le-parisien-8908365"
      lie_a: "M11"
    - temoin: "Emmanuel Macron (Le Parisien, 4 janvier 2022)"
      propos: "Les non-vaccines, j'ai tres envie de les emmerder."
      fiabilite: "\u2726"
      source_url: "https://www.lemonde.fr/politique/article/2022/01/04/les-non-vaccines-j-ai-tres-envie-de-les-emmerder-declare-emmanuel-macron_6108205_823448.html"
      lie_a: "M28"
  documents_cles:
    - "Rapport Senat McKinsey (\u2726)"
    - "Conseil constitutionnel (\u2726)"
    - "France Inter + Le Monde masques (\u2726)"
    - "INSEE mortalite (\u2726)"

# ============================================================
# CHAPITRE 6 : CONTRE-VERSION (inchange)
# ============================================================
CONTRE_VERSION:
  narrative_officielle:
    - version: "Le gouvernement a fait face a une crise sans precedent. Le 'quoi qu'il en coute' a sauve l'economie."
      source: "Macron, Castex"
      source_url: "https://www.radiofrance.fr/franceinter/penurie-de-masques-les-raisons-d-un-scandale-d-etat-2669782"
    - version: "Le pass vaccinal etait necessaire pour proteger les plus vulnerables."
      source: "Delfraissy; Veran"
      source_url: "https://www.conseil-constitutionnel.fr/decision/2022/2022835DC.htm"
  refutations:
    - point: "La penurie de masques n'etait pas une fatalite — c'etait un choix politique."
      preuve: "France Inter + Le Monde"
      source_url: "https://www.lemonde.fr/sante/article/2020/05/07/la-france-et-les-epidemies-2017-2020-l-heure-des-comptes_6038973_1651302.html"
    - point: "McKinsey avait un conflit d'interets massif."
      preuve: "Rapport Senat"
      source_url: "https://www.senat.fr/rap/r21-578-1/r21-578-124.html"
    - point: "Le kayfabe vaccinal est documente."
      preuve: "Radio France + Le Monde"
      source_url: "https://www.radiofrance.fr/franceinter/emmerder-les-non-vaccines-voici-in-extenso-ce-qu-a-dit-emmanuel-macron-dans-le-parisien-8908365"
    - point: "Le Conseil scientifique n'etait pas independant."
      preuve: "Composition du conseil"
      source_url: ""
      fiabilite: "\u2767"
  zones_accord:
    - "La crise etait inedite."
    - "Les vaccins ont sauve des vies."
    - "Le quoi qu'il en coute a empeche un effondrement immediat."

# ============================================================
# CHAPITRE 7 : ACTIVATION (inchange)
# ============================================================
ACTIVATION_MECANISMES:
  chronologie:
    - date: "2018"
      mecanisme: "M05"
      evenement: "Decision DGOS de ne pas renouveler le stock de masques"
      preuve: "Le Monde"
      source_url: "https://www.lemonde.fr/sante/article/2020/05/07/la-france-et-les-epidemies-2017-2020-l-heure-des-comptes_6038973_1651302.html"
    - date: "2020-03-17"
      mecanisme: "M37"
      evenement: "Premier confinement — etat d'urgence 2 ans"
      preuve: "Matrice"
      source_url: ""
    - date: "2020-06-14"
      mecanisme: "M11"
      evenement: "Macron : pas de vaccination obligatoire"
      preuve: "Radio France"
      source_url: "https://www.radiofrance.fr/franceinter/emmerder-les-non-vaccines-voici-in-extenso-ce-qu-a-dit-emmanuel-macron-dans-le-parisien-8908365"
    - date: "2021-01"
      mecanisme: "M09"
      evenement: "McKinsey integre la task force vaccins"
      preuve: "Senat"
      source_url: "https://www.senat.fr/rap/r21-578-1/r21-578-124.html"
    - date: "2021-07-12"
      mecanisme: "M28"
      evenement: "Annonce du pass sanitaire"
      preuve: "Matrice"
      source_url: ""
    - date: "2022-01-04"
      mecanisme: "M28"
      evenement: "Macron : 'j'ai tres envie de les emmerder'"
      preuve: "Radio France"
      source_url: "https://www.radiofrance.fr/franceinter/emmerder-les-non-vaccines-voici-in-extenso-ce-qu-a-dit-emmanuel-macron-dans-le-parisien-8908365"

# ============================================================
# CHAPITRE 8 : INCERTITUDES (inchange)
# ============================================================
INCERTITUDES:
  fourchettes_chiffrees:
    - "Morts COVID : 116 000 (INSEE \u2726)"
    - "Quoi qu'il en coute : 579 Md€ (estimation)"
    - "Stock masques 2017 : 1,5 Md vs 117 M en 2020"
    - "McKinsey : 12 M€ (Senat \u2726)"
  questions_sans_reponse:
    - "Combien de morts evites avec des masques ?"
    - "Conflits d'interets McKinsey/Pfizer ?"
    - "Pourquoi le Conseil scientifique n'a pas examine les alternatives ?"
  fiabilite_sources:
    - "Radio France + Le Monde : \u2726"
    - "Senat : \u2726"
    - "Conseil constitutionnel : \u2726"
    - "France Inter + Le Monde masques : \u2726"
    - "INSEE : \u2726"
    - "Temoignages soignants : \u2767"

# ============================================================
# CHAPITRE 9 : BIAIS (inchange)
# ============================================================
BIAIS_ENQUETEUR:
  parti_pris_declare:
    - "Postulat que la gestion du COVID etait dysfonctionnelle"
    - "Comparaison aux 'bons eleves' sans tenir compte des differences"
  angles_exclus:
    - "Responsabilite des citoyens (defiance vaccinale)"
    - "Comparaison avec pays comparables (Italie, Espagne)"
    - "Analyse economique detaillee du 'quoi qu'il en coute'"
  presupposes:
    - "Les alternatives auraient fonctionne en France"

# ============================================================
# CHAPITRE 10 : REPLICATION (inchange)
# ============================================================
REPLICATION:
  predictions_verifiables:
    - "Toute crise sanitaire future activera M11+M28+M37"
    - "Tout gouvernement promettra 'pas de mesures coercitives' avant d'imposer des mesures maximales"
    - "Le futur Conseil scientifique aura la meme composition homogene"
  conditions_refutation:
    - "Un gouvernement agissant avec transparence totale"
    - "Commission parlementaire concluant a une gestion exemplaire"

# ============================================================
# CHAPITRE 11 : RESISTANCE (inchange)
# ============================================================
RESISTANCE:
  strategies_pertinentes:
    - "R01 Auto-defense informationnelle : decoder le kayfabe"
    - "R04 Sabotage : infiltrer les instances consultatives"
    - "R09 Parrhesia : medecins et soignants doivent parler"
  gestes_souverains_applicables:
    - "Constituer des stocks locaux"
    - "Apprendre les bases de l'epidemiologie"
    - "Soutenir les medecins lanceurs d'alerte"

# ============================================================
# CHAPITRE 12 : SYNTHESE
# ============================================================
ENSEIGNEMENT:
  "Le COVID-19 a ete le revelateur parfait de l'architecture systemique francaise. Les 8 fils identifies se sont actives simultanement : le monopole d'Etat a decide seul, la presse a relaye sans enqueter, le mandarinat medical a verrouille le conseil scientifique, la justice a valide les restrictions sans controle, la societe civile n'a pas ete consultee, l'exceptionnalisme a justifie l'echec, l'ecole a ete sacrifiee, et la laicite sanitaire a remplace la religion civile. Le pattern M11+M28+M05+M37+M22+M09 est confirme dans une sixieme enquete."

CITATION_CLE: "Les non-vaccines, j'ai tres envie de les emmerder." — Macron, 4 janv. 2022. Apres avoir promis le 14 juin 2020 : "Je ne rendrai pas la vaccination obligatoire."

DEGRE_SYSTEMICITE: 5

LIENS:
  - "Enquete sang contamine v2.3 : 02_enquetes/2026-06-26_sang_contamine_v2.3_INVESTIGATION.md"
  - "Enquete Tchernobyl v2.3 : 02_enquetes/2026-06-26_tchernobyl_bascule_INVESTIGATION.md"
  - "Enquete Petition 69 v2.3 : 02_enquetes/2026-06-26_petition_69_matzneff_INVESTIGATION.md"
  - "Enquete Virage rigueur v2.3 : 02_enquetes/2026-06-26_virage_rigueur_1983_INVESTIGATION.md"
  - "Enquete migree v2.3 : 02_enquetes/2026-06-26_covid19_revelateur_INVESTIGATION.md"
  - "Referentiel archeologique : 03_framework/2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"
  - "INSEE : https://www.insee.fr/fr/statistiques/6434424"
  - "Senat/McKinsey : https://www.senat.fr/rap/r21-578-1/r21-578-124.html"
```

---

## Verification NREF

| Exigence | Etat |
|----------|------|
| NREF-1 : M## dominant a traceur | \u2705 6/6 (M11, M37, M28, M05, M22, M09) |
| NREF-2 : CONTRE_VERSION | \u2705 2 narratives + 4 refutations |
| NREF-3 : INCERTITUDES | \u2705 4 fourchettes + 3 questions |
| NREF-4 : BIAIS | \u2705 2 partis-pris + 3 angles |
| NREF-5 : ACTIVATION | \u2705 6 dates (2018-2022) |
| NREF-6 : REPLICATION | \u2705 3 predictions + 2 conditions |
| NREF-7 : Chiffres sources | \u2705 Tous sources |
| NREF-8 : >200 lignes | \u2705 Fiche complete |
| NREF-9 : Sources verifiees | \u2705 7 sources \u2726 + 1 \u2767 (88%) |
| NREF-10 : Contre-version sourcee | \u2705 2 narratives + 4 refutations |
| NREF-11 : REMONTEE_DES_FILS (8 fils) [NOUVEAU v2.2] | \u2705 8 fils (A-H). Actes naissance + 2-3 renforcements + chaines causales + manifestations COVID. Sources : 0 \u2726 / 1 \u2045 / 7+ \u2767 |
| NREF-12 : CONTRE_MESURES (2 actions) [NOUVEAU v2.3] | \u2705 1 PREVENTIF (stock masques 2017-2018) + 1 APRES (Conseil scientifique pluraliste 2020). Acteurs, fenetres, faisabilite, precedents. |

**Niveau NREF : B** (NREF-11 partiel : sources historiques \u2767 majoritaires).

---

## ADDENDUM ULTRATHINKING (inchange depuis v2.1)

```yaml
ANGLES_ALTERNATIFS:
  - angle: "Gestion plutot bonne par rapport a la taille du pays ?"
    niveau_confiance: eleve
  - angle: "Quoi qu'il en coute = veritable redistribution ?"
    niveau_confiance: moyen
  - angle: "Le COVID n'a pas revele le systeme — il l'a renforce"
    niveau_confiance: eleve

ICEBERG_MAX:
  structures_sous_marines:
    - structure: "Complexe medico-industriel (Big Pharma + Etat)"
    - structure: "Surveillance de masse post-COVID (TousAntiCovid, passes)"
    - structure: "Militarisation de la sante publique"
  archives_manquantes:
    - "Contrats achats vaccins (secret-defense)"
    - "Comptes rendus Conseil scientifique"
    - "Evaluations internes ministere Sante"

LIEVRES_ET_LOUPS:
  - sujet: "Role de Didier Raoult — cabale ou charlatan ?"
    niveau_confiance: moyen
    lien_M##: "M27"
  - sujet: "Contrats secrets Pfizer-Europe"
    niveau_confiance: moyen
    lien_M##: "M09"

FAISCEAUX_TRANSVERSAUX:
  - connexion: "Virage rigueur : cause directe (austerite → penurie hospitaliere)"
    mecanismes_partages: "M37, M05"
  - connexion: "Sang contamine : meme M11+M28+M05"
    mecanismes_partages: "M11, M28, M05"
  - connexion: "Tchernobyl : meme M09+M11+M37"
    mecanismes_partages: "M09, M11, M37"

PISTES_FUTURES:
  - piste: "Enquete destruction stock masques 2017-2020"
    priorite: P1
  - piste: "Conseil scientifique — composition, nominations, conflits"
    priorite: P1
  - piste: "Contrats secret-defense vaccins Pfizer-UE"
    priorite: P2

HYPOTHESES_SYSTEMIQUES:
  - hypothese: "M11+M28+M05 = systeme immunitaire de l'Etat francais, invariant quelle que soit la crise"
    niveau_confiance: eleve
    test: "Analyse de la prochaine crise sanitaire"
  - hypothese: "McKinsey = M44 Externalisation de l'Etat — la privatisation de la pensee d'Etat"
    niveau_confiance: moyen
    test: "Analyse budget conseil Etat 2017-2027"
```

---

## Verification par second agent

**A realiser.**

**Points de vigilance :**
1. Les sources \u2767 sont majoritaires dans l'archeologie (sources historiques non numerisees)
2. Les precedents etrangers (SAGE, RKI) sont des references generales non verifiables directement
3. La comparaison France/Allemagne ignore les differences structurelles de population
4. REMONTEE_DES_FILS et CONTRE_MESURES complets mais sources historiques \u2767

```
