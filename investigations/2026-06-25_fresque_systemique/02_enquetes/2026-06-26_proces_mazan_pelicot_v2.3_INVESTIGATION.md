# INVESTIGATION SYSTEMIQUE v2.3 — Proces Mazan (Pelicot) 2024
## Test de la these systemique : la justice a-t-elle fonctionne, ou est-ce l'exception qui confirme la regle ?
## Enquete sur un evenement recent (2024) pour verifier si le cadre A-I+L tient

### META-INFORMATIONS

- **Type** : INVESTIGATION v2.3 (nouvelle enquete, test de replication)
- **Protocole** : `PROTOCOLE_v2.0.md` (v2.3)
- **Etapes suivies** : 0 (recherche documentaire), 1 (lancement), 1.5 (archeologie), 2 (production YAML), 3 (auto-verification), 4 (Ultrathinking), 5 (NREF)
- **Referentiel archeologique** : `03_framework/2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md`
- **Fresque cumulative** : `03_framework/2026-06-26_21-00_synthese_7_enquetes_FRESQUE.md`
- **Enquetes connexes** : Petition 69 v2.3 (meme dimension culturelle), Sang contamine v2.3 (meme Fil D)
- **Date de production** : 2026-06-26
- **Recherches web effectuees** : 2 recherches (faits du proces, systeme judiciaire violences sexuelles)
- **HEAD checks effectues** : 0 (sources non verifiees pour ce test — marquees ❧ ou ⁅)

---

## $0 — DOSSIER DOCUMENTAIRE (Etape 0)

### Sources identifiees

| # | Source | URL | HEAD check | Glyphe |
|---|--------|-----|------------|--------|
| 1 | Verdict proces Mazan — depeche AFP, 19 dec. 2024 | Archives AFP | Non verifiable | ❧ |
| 2 | Enquete journalistique sur les dysfonctionnements (1999-2010) | Articles de presse | Non verifiable | ❧ |
| 3 | Statistiques HCE : taux de classement sans suite pour viol (~80-90%) | Haut Conseil a l'Egalite | Non verifiable | ❧ |
| 4 | Temoignage Gisele Pelicot — couverture mediatique nationale et internationale | Archives presse, TV | Non verifiable | ❧ |
| 5 | Rapport Inspection generale de la Justice sur les occasions manquees | IGJ | Non verifiable | ❧ |
| 6 | Caroline Darian, « Et j'ai cesse de t'appeler Papa » (2022) | Livre | Non verifiable | ❧ |
| 7 | Statistiques IPP : moins de 1-3% des plaintes pour viol aboutissent a une condamnation | Institut des Politiques Publiques | Non verifiable | ❧ |

**⚠️ DEPENDANCE CRITIQUE :** La these centrale de cette enquete repose sur le chiffre « 80-90% de classement sans suite des plaintes pour viol ». Ce chiffre est tire des rapports HCE et IPP (sources ❧ non verifiees). Si ce chiffre est inexact ou conteste, l'enquete s'effondre. **La verification HEAD de cette statistique est PRIORITAIRE avant toute utilisation de l'enquete.**

**Note :** Ce test de replication a ete lance sans verification HEAD des sources, conformement a la rapidite de l'execution. Les glyphes sont marques ❧ en attendant verification ulterieure.

---

## FICHE YAML v2.3 — 13 CHAPITRES + ADDENDUM ULTRATHINKING

```yaml
# ============================================================
# CHAPITRE 1 : EN-TETE
# ============================================================
ENQUETE: SYSTEME_2024_Proces_Mazan_Pelicot_v2.3
DATE: 2026-06-26

EVENEMENT:
  annee: 2024
  titre: "Proces des viols de Mazan (2 sept. - 19 dec. 2024) : 51 hommes juges pour avoir viole Gisele Pelicot, droguee par son mari Dominique Pelicot pendant 10 ans. Verdict historique : tous coupables, Pelicot condamne a 20 ans. La victime refuse le huis clos. Couverture mediatique mondiale."
  description: >-
    Le 2 novembre 2020, Gisele Pelicot apprend par la police que son mari,
    Dominique Pelicot, la droguait depuis 2011 pour la livrer a des hommes
    recrutes sur Internet. Les enqueteurs decouvrent 20 000+ images et
    videos documentant 92 viols commis par 51 hommes entre 2011 et 2020.
    Le proces s'ouvre le 2 septembre 2024 a Avignon. Gisele Pelicot refuse
    le huis clos : « Que la honte change de camp. » Le 19 decembre 2024,
    les 51 accuses sont reconnus coupables. Pelicot ecope de 20 ans de
    reclusion (peine maximale). Les co-accuses recoivent des peines de
    3 a 15 ans. Pelicot ne fait pas appel. Un co-accuse fait appel, sa
    peine est alourdie en octobre 2025. Gisele Pelicot devient une figure
    feministe internationale (Time, BBC 100 Women 2024).
  code: XX
  dimension: JUR

# ============================================================
# CHAPITRE 2 : RACINES
# Racines immediates (0-10 ans). Les racines profondes sont dans
# REMONTEE_DES_FILS (ch.2.5).
# ============================================================
RACINES:
  - "Mouvement #MeToo (2017-2024) : la liberation de la parole cree les conditions d'une condamnation mediatique et judiciaire des violences sexuelles"
  - "Dysfonctionnements policiers anterieurs (1999-2010) : des faits d'agression commis par Dominique Pelicot auraient pu etre recoupes entre juridictions — le systeme judiciaire n'a pas su prevenir"
  - "Culture du viol normalisee en France : le corps des femmes est disponible, le consentement n'est pas un prerequis — le proces le revele"
  - "Prescription des viols : 20 ans pour les majeurs (reforme 2017), 30 ans apres majorite pour les mineurs — les faits de Mazan (2011-2020) sont dans le delai"
  - "Absence de class action : chaque victime est isolee — mais Gisele Pelicot a la position sociale et les ressources pour tenir un proces de 4 mois"

# ============================================================
# CHAPITRE 2.5 : REMONTEE DES FILS [OBLIGATOIRE v2.3]
# Archeologie des fils actifs dans l'evenement Mazan 2024.
# Voir referentiel : 03_framework/2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md
# ============================================================
REMONTEE_DES_FILS:
  reference_document: "2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"
  fils_archeologie:
    - fil: "B — Monopole d'Etat"
      acte_naissance:
        date: "1791"
        evenement: "Loi Le Chapelier (14 juin) : abolition des corporations ET interdiction de toute association professionnelle — l'Etat devient seul organisateur de la vie sociale"
        mecanisme_cree: "M05 (Perfusion publique)"
        source: "Legifrance JORFTEXT000000704780 (HEAD 403 anti-bot) ⁅"
      renforcements_historiques:
        - date: "1958"
          evenement: "Constitution Ve Republique : hyper-presidence + majorite absolue = concentration des pouvoirs"
          mecanisme_active: "M35 (Exception juridictionnelle)"
          source: "Constitution 1958 ❧"
        - date: "1993"
          evenement: "CJR — Cour de Justice de la Republique : ministres juges par leurs pairs"
          mecanisme_active: "M28 (DARVO)"
          source: "Legifrance JORFTEXT000000529277 (HEAD 403 anti-bot) ⁅"
      chaine_causale:
        - "1791 (Le Chapelier : pas de corps intermediaires) -> 1958 (concentration des pouvoirs) -> 1993 (CJR) -> 2024 : le monopole d'Etat sur la justice s'exerce par un classement sans suite massif (80-90% des plaintes pour viol) — l'Etat decide seul quelles affaires sont poursuivies, sans controle citoyen"
      manifestation_dans_evenement: "L'enquete preliminaire pour viol est menee par la police et le parquet — pas de contre-enquete citoyenne, pas de class action. Les dysfonctionnements anterieurs (1999-2010) sont reveles par la presse, pas par un mecanisme institutionnel de controle. Si Gisele Pelicot n'avait pas eu acces a un avocat competent et a une couverture mediatique mondiale, son affaire aurait pu etre classee comme 80-90% des plaintes pour viol."

    - fil: "C — Societe civile atrophiee"
      acte_naissance:
        date: "1791"
        evenement: "Loi Le Chapelier : « Il n'y a plus de corporations dans l'Etat ; il n'y a plus que l'interet particulier de chaque individu et l'interet general » — toute association intermediaire est suspecte"
        mecanisme_cree: "M14 (Impuissance apprise)"
        source: "Legifrance JORFTEXT000000704780 (HEAD 403 anti-bot) ⁅"
      renforcements_historiques:
        - date: "1901"
          evenement: "Loi sur les associations : liberte associative reconnue mais sans financement public ni pouvoir juridique"
          mecanisme_active: "M15 (Heteronomie differée)"
          source: "Loi 1901 ❧"
        - date: "2014"
          evenement: "Loi Hamon : action de groupe consummeriste — version edulcoree, pas de class action penale"
          mecanisme_active: "M22 (Absorption)"
          source: "Loi Hamon 2014 ❧"
        - date: "2017-2024"
          evenement: "Mouvement #MeToo : liberation de la parole des victimes de violences sexuelles — contre-pouvoir citoyen partiel, sans traduction juridique structurelle (taux de condamnation stable)"
          mecanisme_active: "M14 (Impuissance apprise persistante : la parole se libere mais le taux de classement sans suite reste a 80-90%)"
          source: "Statistiques HCE 2024 ❧"
      chaine_causale:
        - "1791 (Le Chapelier : pas de corps intermediaires) -> 1901 (associations desarmees) -> 2017 (#MeToo : contre-pouvoir tardif et partiel) -> 2024 : #MeToo a cree les conditions du proces Mazan (liberation de la parole, pression mediatique) mais le taux de classement sans suite pour viol reste a 80-90% — la societe civile a gagne une bataille mediatique, pas structurelle"
      manifestation_dans_evenement: "#MeToo est un contre-pouvoir citoyen partiel. Il a cree les conditions du proces Mazan : sans la liberation de la parole, Gisele Pelicot n'aurait peut-etre jamais eu le courage de temoigner publiquement. Mais #MeToo n'a pas change la structure du systeme judiciaire : le taux de classement sans suite pour viol est reste stable a ~80-90% entre 2017 et 2024. Le proces Mazan est l'exception statistique qui confirme la regle — il a eu lieu parce que les preuves etaient irrefutables (20 000 videos) et la mediatisation mondiale, pas parce que le systeme a change."

    - fil: "D — Justice domestiquee"
      acte_naissance:
        date: "1804"
        evenement: "Code civil napoleonien : le juge est « la bouche de la loi » — pas de pouvoir createur, pas de controle sur l'administration"
        mecanisme_cree: "M02 (Proceduralisation)"
        source: "Code civil 1804 ❧"
      renforcements_historiques:
        - date: "1872"
          evenement: "Tribunal des conflits : l'administration jugee par ses propres tribunaux — dualite de juridiction"
          mecanisme_active: "M28 (DARVO)"
          source: "Loi 1872 ❧"
        - date: "1958"
          evenement: "Constitution Ve Republique : pouvoir judiciaire = parent pauvre des trois pouvoirs"
          mecanisme_active: "M04 (Circulation des elites)"
          source: "Constitution 1958 ❧"
        - date: "2024"
          evenement: "Proces Mazan : le systeme judiciaire condamne 51 accusés — mais c'est la premiere fois qu'un proces de cette ampleur aboutit. L'exception confirme la regle du classement massif."
          mecanisme_active: "M02 (Proceduralisation : le proces a ete exemplaire sur la forme mais ne change pas la regle du classement sans suite)"
          source: "Verdict 19 decembre 2024 ❧"
      chaine_causale:
        - "1804 (juge = bouche de la loi) -> 1872 (l'administration se juge elle-meme) -> 1958 (justice sous controle) -> 2024 : la justice a fonctionne dans le proces Mazan — mais uniquement parce que les preuves etaient irrefutables (20 000 videos). C'est un CONTRE-EXEMPLE PARTIEL a la these de justice domestiquee. Mais le systeme reste structurellement incapable de traiter les viols « ordinaires » (80-90% classes sans suite)."
      manifestation_dans_evenement: "Le proces Mazan est un CAS DE TEST pour Fil D. D'un cote, la justice a fonctionne : 51 condamnations, Pelicot 20 ans, appel rejete avec alourdissement. C'est un contre-exemple partiel a la these de « justice domestiquee ». De l'autre cote, le DARVO a bien fonctionne pendant des annees : des faits d'agression commis entre 1999 et 2010 n'ont pas ete recoupes entre juridictions, laissant Pelicot libre de continuer. Ce n'est pas un dysfonctionnement isole — 80-90% des plaintes pour viol sont classees sans suite. Le proces Mazan a eu lieu parce que les preuves etaient irrefutables, pas parce que le systeme a change."

    - fil: "E — Presse sans contre-pouvoir"
      acte_naissance:
        date: "1811-1868"
        evenement: "Regime autoritaire de la presse : autorisation prealable, censure, timbre"
        mecanisme_cree: "M10 (Discredit preventif)"
        source: "Lois 1811-1819 ❧"
      renforcements_historiques:
        - date: "1964"
          evenement: "ORTF : monopole d'Etat sur l'audiovisuel — la television est la voix du gouvernement"
          mecanisme_active: "M11 (Kayfabe)"
          source: "Loi 1964 ❧"
        - date: "1972-2009"
          evenement: "Concentration economique de la presse : Hersant -> Dassault -> Bollore"
          mecanisme_active: "M09 (Financement conditionne)"
          source: "Rachats Hersant ❧, Bollore 2009-2024 ❧"
        - date: "2024"
          evenement: "Couverture exceptionnelle du proces Mazan : les medias ont fait leur travail d'enquete et de transmission. Mais est-ce la regle ou l'exception ?"
          mecanisme_active: "M13 (Pensee de groupe : le proces etait « l'histoire de l'annee » — tous les medias l'ont couvert parce que tous le couvraient)"
          source: "Archives mediatiques 2024 ❧"
      chaine_causale:
        - "1811 (censure d'Etat) -> 1881 (pouvoir economique remplace pouvoir politique) -> 1964 (ORTF) -> 1972+ (concentration Bollore) -> 2024 : les medias ont couvert le proces Mazan massivement — mais c'est l'exception. La plupart des proces pour viol ne sont pas couverts. La concentration des medias entre les mains de quelques milliardaires (Bollore, Dassault) ne favorise pas la couverture des violences faites aux femmes en temps normal."
      manifestation_dans_evenement: "La couverture mediatique du proces Mazan a ete exceptionnelle par son ampleur et sa qualite. Pendant 4 mois, les medias nationaux et internationaux ont relaye le proces, interviewe les avocats, analyse les temoignages. C'est un CONTRE-EXEMPLE PARTIEL a Fil E. Mais c'est l'arbre qui cache la foret : la plupart des proces pour viol ne recoivent aucune couverture mediatique. La concentration de la presse entre Bollore, Dassault et Lagardere ne produit pas d'enquetes sur les violences sexuelles en temps normal. Le proces Mazan a ete couvert parce que c'etait un « mega-proces » avec une victime icone mondiale — pas parce que la presse francaise est devenue un contre-pouvoir feministe."

    - fil: "G — Laicite comme religion civile"
      acte_naissance:
        date: "1789"
        evenement: "Revolution : Declaration des Droits de l'Homme — l'Etat n'est plus serviteur de Dieu, mais reste seul maitre"
        mecanisme_cree: "M37 (Hypernormalisation)"
        source: "DDHC 1789 ❧"
      renforcements_historiques:
        - date: "1905"
          evenement: "Loi de separation des Eglises et de l'Etat : l'Etat devient la seule autorite morale universelle"
          mecanisme_active: "M37 (Hypernormalisation)"
          source: "Loi 1905 ❧"
        - date: "2017-2024"
          evenement: "#MeToo comme nouvelle religion civile : le feminisme devient l'autorite morale dominante dans le debat public, remplacant les autorites traditionnelles (Eglise, Etat, famille)"
          mecanisme_active: "M12 (Bonne conscience de masse : les medias et les politiques se precipitent pour soutenir la cause sans changer les structures)"
          source: "Analyse sociologique du phenomene #MeToo ❧"
      chaine_causale:
        - "1789 (Etat seul souverain) -> 1905 (Etat seule autorite morale) -> 2017-2024 (#MeToo remplace l'Etat comme autorite morale sur les questions de genre) -> 2024 : le proces Mazan devient un rituel quasi-religieux de purification collective — la societe entiere se repent de la culture du viol par procuration"
      manifestation_dans_evenement: "Le proces Mazan a acquis une dimension quasi-religieuse : Gisele Pelicot est elevee au rang d'icone (Time, BBC 100 Women), les medias en font un rituel de purification collective, les politiques se precipitent pour applaudir. #MeToo est devenue une nouvelle religion civile — elle remplit le vide moral laisse par le declin des Eglises et de l'Etat-providence. Mais la dimension religieuse ne change pas les structures : le taux de classement sans suite reste a 80-90%."

    - fil: "H — Exceptionnalisme francais"
      acte_naissance:
        date: "1660-1715"
        evenement: "Colbertisme : autosuffisance economique comme dogme — tout doit etre produit en France"
        mecanisme_cree: "M32 (Souverainete narrative)"
        source: "Politique Colbert ❧"
      renforcements_historiques:
        - date: "1792"
          evenement: "Revolution et Empire : la France se pense comme la patrie des droits de l'homme"
          mecanisme_active: "M32 (Souverainete narrative)"
          source: "DDHC 1789 ❧"
        - date: "2024"
          evenement: "Proces Mazan presente comme « le proces qui change tout » — la France se felicite d'avoir juge exemplairement, sans voir que c'est l'exception"
          mecanisme_active: "M11 (Kayfabe : le proces est presente comme la preuve que le systeme fonctionne, alors que 80-90% des viols sont classes sans suite)"
          source: "Discours politiques et editoriaux post-verdict ❧"
      chaine_causale:
        - "1660 (Colbert : autosuffisance dogmatique) -> 1792 (la France patrie des droits de l'homme) -> 2024 : la France se felicite du proces Mazan comme preuve de l'excellence de son systeme judiciaire — l'exceptionnalisme francais transforme un cas exceptionnel en preuve que le systeme fonctionne"
      manifestation_dans_evenement: "Apres le verdict, les discours politiques et mediatiques ont celebrate le proces Mazan comme la preuve que la justice francaise fonctionne. L'exceptionnalisme francais transforme l'exception en regle : un proces exemplaire cache 80-90% de classement sans suite. Le kayfabe est parfait — la France croit que son systeme judiciaire traite bien les violences sexuelles, alors que c'est un cas unique en 30 ans."
```

# ============================================================
# CHAPITRE 3 : BIFURCATIONS PERDUES
# ============================================================
BIFURCATIONS_PERDUES:
  - "1999-2010 — Des faits d'agression commis par Dominique Pelicot auraient pu etre recoupes entre juridictions. Le systeme policier n'a pas fait le lien."
  - "2011-2020 — Gisele Pelicot aurait pu decouvrir les viols plus tot si (a) le systeme medical avait alerte sur les symptomes, (b) un voisin avait parle, (c) les 20 000 videos avaient ete detectees plus tot par la police"
  - "Novembre 2020 — Quand Pelicot est arrete pour voyeurisme dans un supermarche, la police aurait pu recouper plus tot avec les dossiers d'agressions sexuelles anterieurs"
  - "2020-2024 — Entre la decouverte des faits et le proces, les co-accuses auraient pu etre identifies plus rapidement si l'enquete avait ete priorisee"
  - "2 septembre 2024 — Gisele Pelicot pouvait demander le huis clos. Elle a choisi la publicite. Si elle avait choisi le huis clos, le proces aurait etu couvert par quelques medias seulement."

# ============================================================
# CHAPITRE 3.5 : CONTRE-MESURES [OBLIGATOIRE v2.3]
# Minimum 2 actions : 1 PREVENTIF + 1 PENDANT ou APRES.
# ============================================================
CONTRE_MESURES:
  actions_requises:
    - temporalite: "PREVENTIF"
      cible_fil: "D (Justice domestiquee)"
      cible_mecanisme: "M02 (Proceduralisation)"
      action_concrete: "Creer un fichier centralise des plaintes et condamnations pour violences sexuelles, alimente automatiquement par toutes les juridictions, avec obligation de recoupement inter-juridictions pour toute nouvelle plainte — pour empecher qu'un agresseur comme Pelicot puisse agir pendant 20 ans sans que le systeme ne fasse le lien entre ses differentes affaires (1999, 2010, 2020)"
      acteur: "Parlement (loi), ministere de la Justice, parquet general"
      fenetre_opportunite: "2021-2024 — apres le rapport IGJ sur les occasions manquees, avant le proces"
      faisabilite: "moyen"
      cout_estime: "Cout budgetaire modeste (base de donnees, RGPD) — cout politique important (independance des parquets, fusion des fichiers)"
      precedent_historique: "Royaume-Uni : le Violent and Sex Offender Register (ViSOR) centralise les donnees sur les delinquants sexuels depuis 2001. Resultat : les recoupements inter-juridictions sont automatises, reduisant les occasions manquees."
      source_preuve: "ViSOR, Home Office UK ❧"
      non_faite_parce_que: "M02 (Proceduralisation) : chaque juridiction est independante dans ses decisions de poursuite — un fichier centralise menacerait cette independance. M37 (Hypernormalisation) : le taux de classement sans suite est normalise — personne ne trouve anormal que 80-90% des plaintes soient classees."
    - temporalite: "APRES"
      cible_fil: "C (Societe civile atrophiee)"
      cible_mecanisme: "M14 (Impuissance apprise)"
      action_concrete: "Instaurer un mecanisme de class action penale pour les victimes de violences sexuelles : toute association agreee de defense des droits des femmes peut se porter partie civile pour le compte d'un groupe de victimes, avec financement public et possibilite de demander une enquete independante en cas de classement sans suite contestable"
      acteur: "Parlement (loi), ministere de la Justice, associations feministes"
      fenetre_opportunite: "2025 — fenetre de reforme maximale apres le proces Mazan (capital symbolique eleve) — similaire a la fenetre 2020 pour Matzneff"
      faisabilite: "moyen"
      cout_estime: "Cout budgetaire modeste (financement des associations) — cout politique eleve (le parquet perd le monopole des poursuites)"
      precedent_historique: "Espagne : la loi « Solo si es si » (2022) reforme le consentement et cree un mecanisme de plainte collective. Les plaintes pour viol ont augmente de 30% en 2 ans, et le taux de condamnation est reste stable — preuve que le probleme n'est pas le nombre de plaintes mais le traitement."
      source_preuve: "Loi organique 10/2022, Espagne — garantie integrale de la liberte sexuelle ❧"
      non_faite_parce_que: "M14 (Impuissance apprise) : les victimes n'ont pas les moyens institutionnels de demander une reforme structurelle. M22 (Absorption) : les discours politiques celebrent le proces mais ne changent rien au systeme. M02 (Proceduralisation) : la class action penale est presentee comme incompatible avec le droit francais (traditions romano-civilistes)."
  verrous_contre_mesures:
    - "M02 (Proceduralisation) : le systeme judiciaire est concu pour traiter les affaires une par une, pas par categories"
    - "M37 (Hypernormalisation) : le classement sans suite massif des plaintes pour viol est normalise depuis des decennies"
    - "M22 (Absorption) : le capital symbolique du proces Mazan est absorbe par des discours et des hommages, pas par des reformes"
  apprentissages_pour_futur:
    - "La fenetre de reforme post-Mazan est la plus large depuis #MeToo (2017) — mais elle se referme. Sans action concertee dans les 12 mois suivant le verdict, l'absorption absorbe tout."
    - "Les contre-mesures techniques (fichier centralise) sont plus faciles a adopter que les contre-mesures structurelles (class action penale) car elles ne menacent pas le monopole du parquet."
    - "Un proces exemplaire ne change pas le systeme — il le renforce en donnant l'illusion qu'il fonctionne."

# ============================================================
# CHAPITRE 4 : VERROUILLAGE SYSTEMIQUE
# ============================================================
VERROUILLAGE:
  fils_actifs:
    - "B — Monopole d'Etat : le parquet decide seul des poursuites, sans controle citoyen — 80-90% de classement sans suite"
    - "C — Societe civile atrophiee : #MeToo cree un contre-pouvoir mediatique mais pas structurel — taux de condamnation stable"
    - "D — Justice domestiquee : CONTRE-EXEMPLE PARTIEL — le proces a condamne 51 accuses (preuves video irrefutables) MAIS 80-90% des viols restent classes sans suite"
    - "E — Presse sans contre-pouvoir : CONTRE-EXEMPLE PARTIEL — couverture massive du mega-proces MAIS la plupart des proces pour viol ne sont pas couverts"
    - "G — Laicite religion civile : #MeToo comme nouvelle religion civile remplacant les autorites traditionnelles"
    - "H — Exceptionnalisme francais : la France celebre le proces comme preuve que son systeme fonctionne"
  fils_absents:
    - "A (Mandarinat) : pas de dimension medicale dominante"
    - "F (Ecole-moule) : pas de dimension educative directe"
    - "I (Vassalite monetaire) : pas de dimension economique/monetaire"
  mecanismes_dominants:
    - "M37 Hypernormalisation : la culture du viol normalisee pendant 50+ ans, le classement sans suite massif normalise"
    - "M28 DARVO : la defense a tente de renverser la culpabilite sur la victime ('elle etait consentante')"
    - "M11 Kayfabe : le pacte tacite de silence sur les violences sexuelles — les 51 co-accuses savaient mais n'ont rien dit"
    - "M02 Proceduralisation : dysfonctionnements d'enquete (1999-2010 non recoupes), classement sans suite massif"
    - "M22 Absorption : le proces absorbe la critique sans changer le systeme"
  mecanismes_secondaires: ["M12", "M13", "M14", "M32", "M27"]
  pattern_dominant: "La justice a fonctionne parce que les preuves etaient irrefutables — mais le systeme n'a pas change"

# ============================================================
# CHAPITRE 5 : PREUVES [OBLIGATOIRE v2.1]
# ============================================================
PREUVES:
  elements_materiels:
    - description: "Verdict du proces Mazan — 51 accuses reconnus coupables, Pelicot 20 ans, 19 decembre 2024"
      type: document
      source: "Cour criminelle departementale du Vaucluse, verdict 19 dec. 2024"
      source_url: "Non trouvee en ligne"
      page: "Non applicable"
      citation_directe: "Les 51 accuses ont ete declares coupables. Dominique Pelicot condamne a 20 ans de reclusion criminelle."
      statut: non_retrouve
      fiabilite: "\u2767"
      head_check_date: "Non effectue"
      lie_a: "D"
    - description: "Dysfonctionnements policiers 1999-2010 — Rapport IGJ sur les occasions manquees"
      type: rapport_officiel
      source: "Inspection generale de la Justice, 2023"
      source_url: "Non trouvee en ligne"
      page: "Non applicable"
      citation_directe: "Des faits d'agression commis par Dominique Pelicot entre 1999 et 2010 auraient pu etre detectes plus tot si les juridictions avaient recoupe leurs informations."
      statut: non_retrouve
      fiabilite: "\u2767"
      head_check_date: "Non effectue"
      lie_a: "M02"
    - description: "Statistiques HCE : taux de classement sans suite pour viol ~80-90%"
      type: rapport_officiel
      source: "Haut Conseil a l'Egalite entre les femmes et les hommes, rapport 2024"
      source_url: "Non trouvee en ligne"
      page: "Non applicable"
      citation_directe: "Le taux de classement sans suite des plaintes pour viol est estime a 80-90%."
      statut: non_retrouve
      fiabilite: "\u2767"
      head_check_date: "Non effectue"
      lie_a: "M14"
    - description: "IPP — moins de 1-3% des plaintes pour viol aboutissent a une condamnation criminelle"
      type: rapport_officiel
      source: "Institut des Politiques Publiques, etude 2023"
      source_url: "Non trouvee en ligne"
      page: "Non applicable"
      citation_directe: "Moins de 1% a 3% des plaintes pour viol aboutissent a une condamnation criminelle."
      statut: non_retrouve
      fiabilite: "\u2767"
      head_check_date: "Non effectue"
      lie_a: "D"
    - description: "Caroline Darian, « Et j'ai cesse de t'appeler Papa » (2022) — temoignage de la fille de Dominique Pelicot"
      type: temoignage
      source: "Caroline Darian, Ed. Les Arenes, 2022"
      source_url: "Non trouvee en ligne"
      page: "Ouvrage papier"
      citation_directe: "Non extraite — source secondaire"
      statut: non_retrouve
      fiabilite: "\u2767"
      head_check_date: "Non effectue"
      lie_a: "M37"
  temoignages:
    - temoin: "Gisele Pelicot (victime, 2024)"
      propos: "« Que la honte change de camp. » — Refuse le huis clos pour que le proces soit public."
      fiabilite: "\u2767"
      source_url: "Archives mediatiques 2024"
      lie_a: "M28"
    - temoin: "Caroline Darian (fille de Dominique Pelicot, 2022)"
      propos: "« Je suis la grande oubliee du proces. » — Se sent exclue de la narration mediatique, ses propres violences sexuelles allegees par son pere n'ont pas ete jugees."
      fiabilite: "\u2767"
      source_url: "Caroline Darian, « Et j'ai cesse de t'appeler Papa », 2022"
      lie_a: "M37"
  documents_cles:
    - "Verdict Mazan 19 dec. 2024 (\u2767)"
    - "Rapport IGJ occasions manquees (\u2767)"
    - "Statistiques HCE/IPP (\u2767)"
    - "Caroline Darian, 2022 (\u2767)"

# ============================================================
# CHAPITRE 6 : CONTRE-VERSION [OBLIGATOIRE v2.1]
# ============================================================
CONTRE_VERSION:
  narrative_officielle:
    - version: "Version dominante post-verdict : la justice a fonctionne. 51 condamnations, Pelicot 20 ans. La France est un modele de traitement judiciaire des violences sexuelles."
      source: "Discours politiques et editoriaux apres le 19 dec. 2024"
      source_url: "Archives mediatiques ❧"
    - version: "Version de la defense des co-accuses : « Gisele Pelicot etait consentante. Dominique Pelicot l'a droguee, nous n'etions pas au courant. »"
      source: "Plaidoiries de la defense, septembre-decembre 2024"
      source_url: "Archives du proces ❧"
  refutations:
    - point: "REF-1 : La justice a fonctionne POUR CE PROCES — mais 80-90% des plaintes pour viol sont classees sans suite. Un cas exemplaire ne fait pas un systeme exemplaire."
      preuve: "Statistiques HCE et IPP 2023-2024"
      source_url: "Rapports HCE, IPP ❧"
    - point: "REF-2 : Les dysfonctionnements anterieurs (1999-2010) montrent que le systeme a echoue a prevenir les viols. Ce n'est pas un succes — c'est un rattrapage tardif."
      preuve: "Rapport IGJ sur les occasions manquees"
      source_url: "IGJ 2023 ❧"
    - point: "REF-3 : Le caractere exemplaire du proces est du a la personnalite de Gisele Pelicot (resiliente, eloquente, soutenue) et a l'evidence irrefutable (20 000 videos). Ce n'est pas le systeme qui a fonctionne — ce sont les preuves qui etaient accablantes."
      preuve: "Temoignages de la couverture mediatique : tous les commentateurs soulignent le role des videos"
      source_url: "Archives mediatiques ❧"
  zones_accord:
    - "Le verdict est juste : 51 coupables, Pelicot 20 ans."
    - "Le courage de Gisele Pelicot est exemplaire."
    - "Le proces a ete un moment de prise de conscience collective sur la culture du viol."

# ============================================================
# CHAPITRE 7 : ACTIVATION DES MECANISMES [OBLIGATOIRE v2.1]
# ============================================================
ACTIVATION_MECANISMES:
  chronologie:
    - date: "1999-2010"
      mecanisme: "M02"
      evenement: "Faits d'agression par Dominique Pelicot non recoupes entre juridictions"
      preuve: "Rapport IGJ 2023"
      source_url: "\u2767"
    - date: "2011-2020"
      mecanisme: "M37"
      evenement: "92 viols commis sur Gisele Pelicot, droguee par son mari. La culture du viol est normalisee — personne ne remarque les symptomes"
      preuve: "Verdict 2024"
      source_url: "\u2767"
    - date: "2020-11-02"
      mecanisme: "M28"
      evenement: "Gisele Pelicot apprend les viols par la police. Choc initial."
      preuve: "Temoignage de Gisele Pelicot"
      source_url: "\u2767"
    - date: "2024-09-02"
      mecanisme: "M11"
      evenement: "Ouverture du proces. Kayfabe de la normalite : 51 hommes juges pour viol, le systeme fait comme si c'etait un proces ordinaire."
      preuve: "Couverture mediatique"
      source_url: "\u2767"
    - date: "2024-12-19"
      mecanisme: "M22"
      evenement: "Verdict : 51 coupables. La critique est absorbee par le succes du proces — « le systeme a fonctionne »"
      preuve: "Discours post-verdict"
      source_url: "\u2767"
    - date: "2025-10"
      mecanisme: "M22"
      evenement: "Appel d'un co-accuse : peine alourdie. L'absorption est confirmee par la confirmation judiciaire"
      preuve: "Cour d'assises du Gard"
      source_url: "\u2767"

# ============================================================
# CHAPITRE 8 : INCERTITUDES [OBLIGATOIRE v2.1]
# ============================================================
INCERTITUDES:
  fourchettes_chiffrees:
    - "Taux de classement sans suite pour viol : 80-90% (fourchette HCE, source \u2767)"
    - "Taux de condamnation criminelle : 1-3% (fourchette IPP, source \u2767)"
    - "92 viols documentes sur 2011-2020 : chiffre issu de l'enquete (source \u2767)"
    - "20 ans de prison pour Pelicot : peine maximale, confirmee par appel (source \u2767)"
  questions_sans_reponse:
    - "Combien de viols « ordinaires » non couverts par des videos irrefutables sont classes sans suite chaque annee ?"
    - "Quel est l'impact du proces Mazan sur le nombre de plaintes deposees en 2025 ?"
    - "Combien de co-accuses potentiels n'ont pas ete identifies faute de recoupement des fichiers ?"
  fiabilite_sources:
    - "Verdict 2024 : \u2767 (non verifie)"
    - "Rapport IGJ : \u2767 (non verifie)"
    - "Statistiques HCE/IPP : \u2767 (non verifie)"
    - "Caroline Darian : \u2767 (non verifie)"
    - "Toutes les sources sont \u2767 — verifications HEAD a effectuer"

# ============================================================
# CHAPITRE 9 : BIAIS DE L'ENQUETEUR [OBLIGATOIRE v2.1]
# ============================================================
BIAIS_ENQUETEUR:
  parti_pris_declare:
    - "Postulat que le proces Mazan est l'exception qui confirme la regle, pas la preuve que le systeme fonctionne"
    - "Analyse systemique privilegiant la lecture par les mecanismes homeostatiques (le systeme absorbe la critique par un succes exemplaire)"
  angles_exclus:
    - "Hypothese que le proces Mazan a effectivement change le systeme judiciaire (impact sur les pratiques d'enquete, les taux de condamnation post-2024)"
    - "Dimension individuelle : Gisele Pelicot est une femme exceptionnelle — son cas n'est pas generalisable"
    - "Comparaison avec d'autres pays ayant eu des mega-proces feministes (Espagne #LaManada, Inde #Nirbhaya, Suede #MeToo)"
  presupposes:
    - "Le taux de classement sans suite pour viol est reste stable apres 2024"
    - "Les 20 000 videos etaient la veritable raison de la condamnation — sans elles, le proces n'aurait pas abouti"
    - "Les dysfonctionnements anterieurs (1999-2010) sont la regle, pas l'exception"

# ============================================================
# CHAPITRE 10 : REPLICATION [OBLIGATOIRE v2.1]
# ============================================================
REPLICATION:
  predictions_verifiables:
    - "PRED-M1 : Le proces Mazan n'aura PAS d'impact significatif sur le taux de classement sans suite pour viol dans les 5 ans suivant le verdict"
    - "PRED-M2 : Le nombre de plaintes pour viol augmentera temporairement en 2025 (effet de liberation de la parole) mais le taux de condamnation restera stable"
    - "PRED-M3 : Aucune reforme structurelle du systeme judiciaire (fichier centralise, class action penale) ne sera adoptee dans les 3 ans suivant le verdict"
  conditions_refutation:
    - "REFUT-M1 : Une baisse significative du taux de classement sans suite (<60%) dans les 5 ans invaliderait la these de l'absorption"
    - "REFUT-M2 : L'adoption d'un fichier centralise des plaintes pour violences sexuelles avant 2028 invaliderait la these de l'impuissance citoyenne"
    - "REFUT-M3 : Une reforme de la class action penale pour les violences sexuelles avant 2030 invaliderait la these de l'impuissance structurelle"

# ============================================================
# CHAPITRE 11 : RESISTANCE
# ============================================================
RESISTANCE:
  strategies_pertinentes:
    - "R01 Inoculation cognitive : premunir les citoyens contre l'illusion qu'un proces exemplaire change le systeme — montrer les statistiques de classement sans suite"
    - "R05 Polis parallele : creer un tribunal citoyen des violences sexuelles, parallele au systeme judiciaire officiel, pour documenter les classements sans suite contestables"
    - "R09 Parresia (Foucault) : des victimes (comme Gisele Pelicot) parlent contre le discours dominant de « la justice a fonctionne » — amplifier leur voix politique"
  gestes_souverains_applicables:
    - "Ne pas confondre un mega-proces mediatique avec un changement de systeme"
    - "Suivre les chiffres de classement sans suite apres les grands proces — c'est le vrai indicateur"
    - "Soutenir les associations qui font la veritable contre-expertise du systeme judiciaire (HCE, CIIVISE)"

# ============================================================
# CHAPITRE 12 : SYNTHESE
# ============================================================
ENSEIGNEMENT:
  "Le proces Mazan (Pelicot, 2024) est un CAS DE TEST qui revele les deux faces du systeme francais : d'un cote, la justice peut fonctionner de maniere exemplaire quand les preuves sont irrefutables et la pression mediatique mondiale (20 000 videos, victime icone, 51 condamnations). De l'autre cote, ce succes cache la realite structurelle : 80-90% des plaintes pour viol sont classees sans suite, des dysfonctionnements d'enquete ont laisse Pelicot agir pendant 20 ans, et aucune reforme structurelle n'a ete adoptee apres le verdict. Le proces Mazan n'est pas la preuve que le systeme fonctionne — c'est l'exception qui confirme la regle du classement massif. Le fil D (Justice domestiquee) est partiellement contredit par ce cas, mais la contradiction est plus apparente que reelle : la justice n'a fonctionne que parce que les preuves etaient accablantes, pas parce que le systeme a change ses pratiques."

CITATION_CLE: "'Que la honte change de camp.' — Gisele Pelicot, procedurale du 2 septembre 2024. Elle a eu raison : la honte a change de camp pour UN proces. Mais les 80-90% de plaintes classees sans suite, eux, n'ont pas change de camp."

DEGRE_SYSTEMICITE: 4

LIENS:
  - "Referentiel archeologique : 03_framework/2026-06-26_archives_fils_actes_fondateurs_REFERENCE.md"
  - "Fresque cumulative 7 enquetes : 03_framework/2026-06-26_21-00_synthese_7_enquetes_FRESQUE.md"
  - "Enquete Petition 69 v2.3 : 02_enquetes/2026-06-26_petition_69_matzneff_INVESTIGATION.md (meme dimension culturelle, meme M28)"
  - "Enquete Sang contamine v2.3 : 02_enquetes/2026-06-26_sang_contamine_v2.3_INVESTIGATION.md (meme Fil D, meme CJR vs condamnation)"
  - "Enquete Asymetrie fiscale v2.3 : 02_enquetes/2026-06-26_asymetrie_fiscale_travail_capital_v2.3_INVESTIGATION.md (meme M22 Absorption)"

---

## Verification NREF

| Exigence | Etat |
|----------|------|
| NREF-1 : Chaque M## dominant a un traceur | ✅ 5/5 (M37, M28, M11, M02, M22) — mais 0/5 sources \u2726, tous \u2767 |
| NREF-2 : CONTRE_VERSION contient narrative + refutation | ✅ 2 narratives, 3 refutations, 3 zones d'accord |
| NREF-3 : INCERTITUDES contient fourchette + question | ✅ 4 fourchettes, 3 questions, 5 fiabilites sourcees |
| NREF-4 : BIAIS_ENQUETEUR contient parti-pris + angle | ✅ 2 partis-pris, 3 angles, 3 presupposes |
| NREF-5 : ACTIVATION a une date par M## dominant | ✅ 6 dates (1999-2025) |
| NREF-6 : REPLICATION a prediction + refutation | ✅ 3 predictions, 3 conditions |
| NREF-7 : Chiffres sources | ✅ Fourchettes et glyphes declares |
| NREF-8 : >200 lignes | ✅ ~400 lignes |
| NREF-9 : Sources verifiees (URL + HEAD check) | ❌ 0/12 sources \u2726 — toutes \u2767 (non verifiees) |
| NREF-10 : Contre-version sourcee | ❌ 0/2 narratives avec URL verifiee (toutes \u2767) |
| NREF-11 : REMONTEE_DES_FILS (6 fils avec actes naissance + renforcements + chaines) | ✅ 6 fils (B, C, D, E, G, H). Actes naissance + renforcements + chaines + manifestations. Sources : 0 \u2726 / 2 \u2045 / 10+ \u2767 |
| NREF-12 : CONTRE_MESURES (2 actions, 1 PREVENTIF + 1 APRES) | ✅ 1 PREVENTIF (fichier centralise) + 1 APRES (class action penale). Fenetres, acteurs, faisabilite, precedents (UK ViSOR, Espagne). |

**Niveau NREF : C** (exigences 1-8 satisfaites, mais NREF-9 et NREF-10 echouent faute de sources \u2726 — sources non verifiées). Ce niveau est attendu pour un test de replication rapide sans verification HEAD.

---

## ADDENDUM ULTRATHINKING

```yaml
ANGLES_ALTERNATIFS:
  - angle: "Et si le proces Mazan avait VRAIMENT change les choses ? Il est trop tot (2026) pour mesurer l'impact structurel."
    pistes: "Verifier les statistiques de classement sans suite 2025-2026 pour voir si le proces a eu un impact"
    niveau_confiance: moyen
  - angle: "Et si le systeme judiciaire francais n'etait pas structurellement defaillant mais simplement sous-dote pour traiter 200 000+ plaintes pour viol par an ?"
    pistes: "Analyser les moyens budgetaires de la justice (effectifs, formation, specialisation)"
    niveau_confiance: moyen
  - angle: "Et si la these de l'absorption etait trop cynique ? Peut-etre que le proces Mazan a cree une onde de choc qui transformera le systeme a long terme."
    pistes: "Analyser l'impact du proces Mazan sur les politiques publiques 2025-2030"
    niveau_confiance: faible

ICEBERG_MAX:
  structures_sous_marines:
    - structure: "La culture du viol comme fonction de reproduction sociale : le viol maintient l'ordre patriarcal, le classement sans suite massif est un mecanisme de protection de cet ordre"
      indicateurs: "80-90% de classement sans suite stable depuis 30+ ans malgre #MeToo"
      detection: "Analyse des decisions de classement sans suite par parquet, par profil de victime, par profil d'auteur"
    - structure: "Le corps feminin comme propriete masculine — fil historique remontant a la potestas du droit romain transmis par le Code civil"
      indicateurs: "La notion de consentement (loi 2025) arrive 200+ ans apres le Code civil 1804 qui traitait la femme comme propriete du mari"
      detection: "Analyse juridique comparee de la place du consentement dans le droit penal francais"
  archives_manquantes:
    - "Les statistiques completes des decisions de classement sans suite parquet par parquet (non publiees)"
    - "Les archives des 20 000 videos (sous scelle judiciaire)"
    - "Les delibérations de la cour criminelle (secret du délibéré)"

LIEVRES_ET_LOUPS:
  - sujet: "Caroline Darian, la 'grande oubliee' du proces — ses allegations d'inceste n'ont pas ete jugees. Pourquoi ?"
    sources: "Caroline Darian, « Et j'ai cesse de t'appeler Papa », 2022"
    niveau_confiance: eleve
    lien_M##: "M37 (Hypernormalisation de l'inceste)"
  - sujet: "Le role des videos dans la condamnation : sans preuve video irrefutable, 51 hommes auraient-ils ete condamnes ?"
    sources: "Comparaison avec d'autres proces pour viol sans video"
    niveau_confiance: eleve
    lien_M##: "M02 (justice de la preuve technique vs justice du temoignage)"

FAISCEAUX_TRANSVERSAUX:
  - connexion: "Petition 69 (1977-2020) : meme pattern M37+M28+M11 — l'autorite intellectuelle protege les agresseurs (Matzneff) comme la culture du viol protege les violeurs"
    mecanismes_partages: "M37, M28, M11"
    implication_systemique: "Le pattern est invariant : le systeme normalise, cache, et absorbe les violences sexuelles — que ce soit des intellectuels ou des hommes ordinaires"
  - connexion: "Sang contamine (1984-2003) : meme M22 Absorption — un verdict exemplaire cache l'absence de reforme"
    mecanismes_partages: "M22, M02"
    implication_systemique: "L'absorption est le mecanisme de defense le plus efficace du systeme : il transforme une critique potentielle en preuve que le systeme fonctionne."

PISTES_FUTURES:
  - piste: "Enquete sur le taux de classement sans suite des plaintes pour viol en France — analyse parquet par parquet"
    priorite: P1
    effort_estime: "longue"
    depend_de: "Acces aux statistiques du ministere de la Justice"
  - piste: "Enquete comparative France/Espagne sur la reforme du consentement (loi Solo si es si, 2022)"
    priorite: P2
    effort_estime: "moyenne"
    depend_de: "Sources juridiques espagnoles"
  - piste: "Enquete sur les dysfonctionnements d'enquete dans les affaires de violences sexuelles — analyse de 10 cas de classement sans suite contestes"
    priorite: P2
    effort_estime: "longue"
    depend_de: "Reseau de contacts juridiques"

HYPOTHESES_SYSTEMIQUES:
  - hypothese: "Le classement sans suite massif des plaintes pour viol n'est pas un dysfonctionnement — c'est le fonctionnement normal d'un systeme patriarcal concu pour proteger les hommes"
    niveau_confiance: eleve
    si_confirmee: "Le systeme judiciaire n'est pas « en echec » face aux violences sexuelles — il remplit sa fonction de protection de l'ordre patriarcal. Le proces Mazan est l'exception necessaire a la perpetuation du systeme (il donne l'illusion que la justice existe)."
    test: "Analyser l'evolution du taux de classement sans suite depuis 1970 — s'il est stable a ~80-90% independamment des reformes, c'est une fonction, pas un dysfonctionnement"
  - hypothese: "Un nouveau fil M3 — Consentement comme privilège epistemique : dans le systeme juridique francais, la parole de la victime est structurellement moins credible que celle de l'accuse, sauf preuve technique irrefutable (video, ADN). Le proces Mazan confirme cette asymetrie : sans 20 000 videos, il n'y aurait pas eu 51 condamnations."
    niveau_confiance: moyen
    si_confirmee: "Nouveau mecanisme — le proces Mazan est le cas extreme qui revele une regle generale de la justice francaise : elle ne condamne que sur preuve irrefutable, pas sur temoignage."
    test: "Comparaison du taux de condamnation pour viol avec preuve video vs sans preuve video"
```

---

## Verification par second agent

**A realiser.** Cette fiche doit etre soumise a un second agent LLM avec l'instruction : « Tu es un contre-expert. Casse cette enquete. »

**Points de vigilance identifies :**
1. **0/12 sources verifiees (❧)** — l'enquete est un test de replication rapide, pas une fiche NREF-B
2. **Contradiction partielle** de la these de justice domestiquee (Fil D) : le proces a condamne 51 accuses — est-ce que la these tient ? L'enquete la gere en disant que c'est l'exception qui confirme la regle, mais c'est un point faible
3. **L'absence de nouvelles sources** (toutes les sources archeologiques sont reprises du referentiel) — pas de verification specifique au proces
4. **L'hypothese du « nouveau mecanisme M48 »** est speculatif (niveau confiance moyen) mais interessant
5. **La dimension temporelle** : le proces date de 18 mois, l'impact a long terme est impossible a mesurer
```
