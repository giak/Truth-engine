# PROTOCOLE PILOTE « AVENANTS SESN » : BRIEF AUTONOME POUR AGENT À CONTEXTE VIERGE

> Type : ARCHITECTURE. Version : 1.1 (2026-08-10). Statut : DESIGN VALIDÉ (utilisateur, 2026-08-10), intégration des corrections de la revue externe (tmp3, 2026-08-10 : modèle événementiel des modifications, seuils R.2194 par fondement, sélection à deux voies, matrice hypothèses, matrices juridiques par qualification, mémoire comme index probatoire, recensement complet).
> Hiérarchie des points d'entrée : le README du dossier commun est le point d'entrée de LECTURE (navigation) ; le présent document est le contrat d'EXÉCUTION (tout agent exécutant le pilote le lit en premier et suit §0 avant toute autre action).

## §0 NOTICE DE LECTURE OBLIGATOIRE (agent exécutant)

Lire dans cet ordre strict, avant toute recherche ou écriture :

1. Ce fichier (le présent protocole), intégralement.
2. `/home/giak/projects/truth-engine/AGENTS.md` : règles du projet (éthique, nommage, RTK, WRITE+EDIT, protocole mem-first).
3. `/home/giak/projects/truth-engine/truth-engine-v2/KERNEL.md` : le pipeline d'investigation v2.8 (texte canonique). Le §0-§7 du KERNEL gouvernent toutes les phases ; le présent protocole ne le remplace pas, il le spécialise pour un périmètre précis.
4. `/home/giak/projects/truth-engine/investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_preparation-anticorruption/corruption_definition.md` : les 3 niveaux de corruption, les qualifications pénales (dont le favoritisme 432-14, qui ne requiert ni contrepartie ni paiement occulte), le critère du lien de contrepartie (§6 : ce qui ne prouve pas seul).
5. `/home/giak/projects/truth-engine/investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_preparation-anticorruption/corruption_brainstorm.md` : protocole générique (hypothèses concurrentes H0-H6, 5 chaînes, CADA, signaux, analyse quantitative, discipline RAW→FAITS→RELATIONS→HYPOTHÈSES→QUALIFICATIONS).
6. `/home/giak/projects/truth-engine/investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_preparation-anticorruption/corruption_brainstorm_2.md` : doctrine multi-canal (8 familles de sources, grille d'évaluation, registre des rumeurs, matrice versions/traces, relation RÉPÈTE, triangulation).
7. `/home/giak/projects/truth-engine/investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_avenants-5-grands-projets/2026-08-09_22-33_avenants-5-grands-projets_INVESTIGATION.md` : l'enquête APEX existante (état des faits, GAP-001, chiffres CdC/Sénat, acteurs). C'est la ressource héritée la plus importante du pilote.
8. Dossier `/home/giak/projects/truth-engine/investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_surfacturation-commande-publique/` (parent de l'enquête avenants) : mécanismes de surfacturation et GAP-001 ACCESS.

Interdits absolus pendant l'exécution :
- commencer une recherche ou une conclusion avant d'avoir lu les 8 éléments ci-dessus ;
- dévier du pipeline KERNEL : toute sortie dossier doit être un dossier forensique au format INVESTIGATION, jamais un article ;
- inventer un chiffre, une date, un montant ou une URL : toute affirmation décisionnelle doit porter un SRC-ID et un locator (voir §7) ;
- utiliser le mot « preuve » pour un indice isolé : la qualification finale suit la méthode §6 de corruption_definition.md.

## §1 POURQUOI (contexte et justification)

1. **Cadre général.** La corruption en France est rarement identifiable par une preuve directe. Le corpus 2026-08 du projet (40+ investigations : CumCum, Dutreil, HATVP, cessions, EDF OPA, banques-conseils) a établi que l'on dispose surtout d'indices et de faisceaux concordants : surfacturation, avenants au-dessus des seuils, pantouflage, avantages de complaisance. L'ambition du présent pilote est de tester une méthode reproductible qui transforme des gaps documentaires en objets d'enquête.
2. **Le trou noir documentaire (GAP-001).** L'enquête APEX du 09-08 a vérifié qu'aucune institution ne publie le montant cumulé des avenants des 5 grands projets publics (EPR, Grand Paris, JO, Seine-Nord, Hôpital). Les données existent : les données essentielles de la commande publique (DECP) sont obligatoires depuis 2019 (arrêté du 22/03/2019) et contiennent les avenants. Personne ne les agrège, ni EDF, ni la SGP, ni SOLIDEO, ni SESN, ni AP-HP (FCT-001 à FCT-003 de l'enquête APEX).
3. **Le contre-exemple JO 2024.** Le seul projet maîtrisé (6,6 Md€, CdC 29/09/2025, « pas de dérapage », « rares anomalies ») est le seul doté d'une supervision stricte des avenants (SOLIDEO). Corrélation documentée, causalité non établie : le pilote doit produire des données comparables là où l'État n'en produit pas, sans conclure à la causalité.
4. **Pourquoi Seine-Nord.** Ses atouts : volume borné (74-76 marchés), avenants « fréquents » documentés, rapport CdC récent (10/04/2026, 7,347 Md€, dérive +2,2-2,8 Md€ hors frais financiers, ~10 Md€ avec), SESN acheteur public soumis aux DECP, contrôle des données réalisable par un indépendant. Le surcoût est documenté officiellement ; la part imputable est le trou noir.
5. **Hypothèse de travail (à éprouver, jamais prémisse).** Les dérives de coûts passent en partie par des modifications contractuelles dans les seuils autorisés, qui permettent d'augmenter les prix sans nouvelle mise en concurrence : modifications de faible montant (10 % fournitures/services, 15 % travaux, R.2194-8 CCP, cumul plafonné R.2194-9, double plafond en euros), circonstances imprévues (50 % par modification, R.2194-3), clauses de réexamen, prestations supplémentaires, changement de titulaire. La jurisprudence Conseil d'État (modification substantielle = nouvelle concurrence) borne la partie illégale. Le pilote cherche à QUANTIFIER la part passant par ces modifications sur un échantillon borné et à la confronter aux explications officielles (aléas, inflation, retards, besoins perfectibles).
6. **Usage final (décidé).** Mixte, à décider à l'issue selon la qualité du faisceau : (a) signalement AFA/PNF si cohérence suffisante, (b) publication/article si base factuelle + prudence d'expression garanties, (c) base de connaissance interne sinon. Le dossier doit être structuré pour permettre les trois.

## §2 CE QUE L'ON VEUT FAIRE (objectif, périmètre, livrables)

### Objectif central
Produire le premier agrégat public extérieur des modifications contractuelles d'un grand projet public (Canal Seine-Nord Europe) sur les exercices 2021 à 2026, calculer un taux de modification par contrat sur un échantillon borné, sélectionner 3 anomalies + 2 cas témoins, puis déterminer, pour chaque anomalie, QUELLES EXPLICATIONS RESTENT COMPATIBLES avec les faits (H0-H6, voir §Phase 8). L'objectif n'est pas de présupposer une « chaîne de contrepartie » : la reconstruction des chaînes (décision, argent, bénéficiaire, avantages) est un instrument d'organisation des observations, mobilisé seulement si les faits la soutiennent, jamais un objet d'enquête postulé d'emblée.

### Périmètre exact
- Acheteur : SESN (Société du Canal Seine-Nord Europe), établissement public.
- Famille de dépenses : marchés de travaux (génie civil, secteurs hydrauliques, dépendances vertes, fournitures) ; couvrir aussi marchés de maîtrise d'œuvre et de contrôle si nécessaires au calcul.
- Période : exercices 2021 à 2026 inclus (2026 est une année incomplète à la date du pilote : fixer une date de coupure précise dans le RUN_MANIFEST avant tout calcul, ex. 30/06/2026 ; les montants partiels de 2026 sont comparés en années pleines, jamais mélangés).
- Recensement : UNIVERS COMPLET des marchés SESN accessibles (DECP consolidées, page SCSNE, AWS/BOAMP/TED, voir Phase 1), PAS un tirage d'office des 30 plus gros. Les règles de sélection de l'échantillon d'approfondissement sont fixées PAR ÉCRIT AVANT tout calcul (voir Phase 4) et appliquées ensuite, sans ajustement opportuniste en fonction des résultats.
- Marchés sans montant renseigné : NE PAS les exclure du recensement : conservés dans une table séparée `data/marches_sans_montant.csv` (un « taux nul » peut révéler des données incomplètes, pas une absence réelle de modification).
- Unité d'analyse : contrat = données de base + série ordonnée des événements de modification associés (modèle événementiel, voir Phase 1).
- Un contrat peut être publié sur plusieurs supports (DECP, page SCSNE, BOAMP, TED) : le rapprochement est fait par numéro de marché SESN (ex. 21S6I028) puis par identifiant d'avis ; chaque dédoublonnage est documenté.

### Livrables (ordre de production)
1. `data/` : DECP brutes SESN (téléchargées, hashées SHA-256) + table normalisée SIREN/SIRET (CSV) + registre des pistes non officielles (CSV, ouvert dès la Phase 1).
2. `scripts/` : scripts déterministes d'extraction et de calcul (Python ou shell, auto-documentés) : téléchargement DECP, normalisation SIREN, calcul taux de modification, concentration, seuils.
3. Le dossier d'investigation final KERNEL (INVESTIGATION, format §8) avec la conclusion graduée et l'option d'escalade.
4. Un registre de progression (REGISTRE) horodaté : matrices d'hypothèses par anomalie, registre des rumeurs (séparé des faits), matrice versions/traces pour les 3 anomalies.
5. quintessence YAML (via SUMBLIMATOR §parse_atomic/curator si le volume de faits le permet) et write-back Mnemolite (recherche à l'ouverture, écriture à la clôture, tags project:truth-engine + kernel + sesn + avenants).

Chaque livrable répond à une question précise du protocole ; aucun artefact « de remplissage ». Les exigences de format du KERNEL restent dues, mais chaque champ peut être marqué N/A motivé dans le REGISTRE plutôt que rempli mécaniquement.

## §3 COMMENT (méthode en 10 phases, approche C « pilote itératif avec legs »)

Chaque phase produit un artefact réutilisable (script + table + hash) déposé dans le dossier du pilote. L'infrastructure naît de la phase, jamais avant. Respecter l'ordre ; une phase ne commence que si la précédente a livré son artefact.

### Phase 1 : Recensement et extraction (univers complet, modèle événementiel)
- Sources, en rapprochement systématique (aucune n'est suffisante seule) :
  (a) DECP consolidées data.gouv.fr (fichiers consolidés ministère des Finances). AVERTISSEMENT VÉRIFIÉ : depuis l'entrée en vigueur du format DECP 2022 (01/01/2024), les consolidés du ministère sont MOINS EXHAUSTIFS (sources AIFE/API DUME, Atexo, Klekoon, Mégalis, Ternum-BFC non consolidées ; constat forum data.gouv 04/05/2026 et TeamOpenData 07/2025). Une absence dans les consolidés ne prouve pas l'absence de modification.
  (b) Page Marchés publics du SCSNE (canal-seine-nord-europe.fr/marches-publics/, 120 résultats publiés, liens avis BOAMP/TED, numéros de marché SESN).
  (c) Profil d'acheteur AWS (marches-publics.info), support officiel de publication de la SESN.
  (d) BOAMP et TED pour les avis (d'attribution et de modification éventuels).
  (e) PLACE (marches-publics.gouv.fr) pour les DECP publiées par l'intermédiaire du profil d'acheteur.
- Critères de filtrage : pouvoir adjudicateur = SESN (et ses formes socle exactes, à vérifier, ex. « Société du Canal Seine-Nord Europe »), période 2021-2026 avec date de coupure fixée au RUN_MANIFEST, type = marchés (pas uniquement accords-cadres ; tracer le type), version du schéma DECP tracée (format 2022 vs 2019) et date de début d'exécution si présente.
- NOUVELLE FAÇON DE LIRE LES DECP (modèle événementiel, règle anti-double-comptage) : une DECP « modification » n'est PAS un avenant isolé : le champ « Montant modifié du marché public en euros HT » (bloc modifications > montant) est le NOUVEAU MONTANT TOTAL du marché après la modification (montant initial ET modification compris). INTERDICTION d'additionner les « montant modifié » de plusieurs DECP : le montant d'un événement de modification = montant modifié courant − valeur du montant immédiatement précédent (ou montant initial si première modification). La durée modifiée est la durée TOTALE après modification (mois, arrondi supérieur). Les modifications résultant de clauses de variation de prix sont EXONÉRÉES de publication DECP (arrêté 22/12/2022 III) : leur absence n'est pas une absence de modification, à suivre via les autres sources.
- Par contrat, constituer la série ordonnée des événements : événement 1 = attribution (montant initial, titulaires, durée, forme de prix, type de prix) ; événements 2..n = modifications (numéro d'identification de la modification, date de notification, date de publication, montant modifié = nouveau total, durée modifiée, nouveaux titulaires éventuels).
- Artefact : `data/decp_sesn_raw.csv` + `decp_sesn_raw.sha256` + script `scripts/01_extract_decp.py` (ou shell) + `data/recensement_univers.csv` (tous les marchés SESN trouvés toutes sources, avec champs : numéro marché SESN, idweb BOAMP/TED, montant initial, support(s) de publication, version schéma) + `data/marches_sans_montant.csv` (marchés sans montant renseigné, conservés) + `data/registre_pistes.csv` (pistes non officielles, ouvert dès cette phase). HASH_CAPABILITY : si l'environnement ne fournit pas sha256, le noter en DEGRADED_FLAG (pas d'invention).
- Contrôle qualité : nombre total de contrats recensés vs nombre déclaré dans le rapport CdC (74-76 marchés) : écarter ou documenter l'écart ligne par ligne.

### Phase 2 : Normalisation SIREN/SIRET
- Nettoyage strictement déterministe : zéros perdus, espaces, clé de Luhn sur SIRET, dédoublonnage par (identifiant marché, acheteur, lot, version de schéma), jamais par (SIREN, objet, montant) qui fusionne des lots distincts. Interdiction d'utiliser un LLM pour ce nettoyage (règle anti-fausse-précision, AGENTS.md §4).
- Rapprochement RNE/INPI (data.inpi.fr, API SIRENE) pour les attributaires non identifiés.
- Artefact : `data/decp_sesn_norm.csv` + script `scripts/02_normalize_siren.py` + liste des SIREN non résolus.

### Phase 3 : Mesures quantitatives
Pour chaque contrat de l'échantillon : montant initial, montant final (dernière valeur connue), nombre d'événements de modification, montant cumulé des modifications (somme des différences selon le modèle événementiel de la Phase 1, JAMAIS l'addition des « montant modifié »), taux de modification = montant cumulé des modifications / montant initial.
Indicateurs agrégés (cf. corruption_brainstorm §7) :
- part des 5 premiers fournisseurs (concentration) ;
- fréquence des procédures négociées et des candidatures uniques ;
- montants cumulés des modifications rapportés aux montants initiaux ;
- proximité au(x) seuil(s) applicable(s) AU FONDEMENT JURIDIQUE de chaque modification, documenté événement par événement : modifications de faible montant (R.2194-8 : 10 % fournitures/services, 15 % travaux, ET seuils européens ; cumul plafonné R.2194-9, double plafond en euros 140 000/215 000/431 000/5 382 000 €), circonstances imprévues (R.2194-3 : 50 % par modification, modifications successives ne devant pas contourner la publicité/la concurrence), clause de réexamen (R.2194-1), prestations supplémentaires (R.2194-2 à 4), changement de titulaire (R.2194-6) ; au-delà de 10/15 %, une modification n'est pas nécessairement substantielle ni irrégulière (avis CE n° 405540 du 15/09/2022 ; DAJ 2019) : l'indicateur est la proximité au seuil applicable au fondement déclaré, pas un seuil universel de régularité ;
- prix unitaires comparés à des transactions homogènes (tunnels, terrassements, ouvrages d'art) ;
- durée publication → clôture ; récurrence des sous-traitants.
Règles de comparaison : ne comparer que des opérations réellement homogènes : même nature, même date/maturité (un marché signé en 2021 n'est pas comparable à un marché signé en 2025 sur la même base), même type de prix (ferme/actualisable/révisable) et forme (unitaire/forfaitaire/mixte), même transfert de risque, même volume, même période d'exécution. Un taux de modification nul ou quasi nul peut signifier des données incomplètes (DECP manquantes, modifications de prix exonérées de publication) : le vérifier avant de l'interpréter comme absence réelle. Pas de loi de Benford comme détecteur universel ; pas de score de corruption ; pas de corrélation de graphe traitée comme causalité.
Artefact : `data/mesures_sesn.csv` + script `scripts/03_mesures.py` + `data/concentration_sesn.csv`.

### Phase 4 : Sélection des cas (3 anomalies + 2 témoins, règles fixées AVANT les calculs)
Les critères de sélection sont écrits et gélés AVANT de calculer (pas d'ajustement opportuniste sur les résultats). Deux voies indépendantes :
- Voie 1, recensement contractuel (déterministe, sur l'univers recensé) : les 3 cas sont, par critère prédéfini : (1) la plus forte hausse ABSOLUE du montant (Δ en euros) ; (2) la plus forte hausse RELATIVE (Δ / montant initial), sous réserve d'un seuil de matérialité minimale fixé au recensement (un contrat minuscule en % mais insignifiant en euros peut être un artefact) ; (3) la trajectoire qui viole la proportionnalité (avenants successifs dépassant 15 % cumulés pour des travaux, modifications de même nature rapprochées, fondements documentés absents).
- Voie 2, pistes non officielles (registre ouvert en Phase 1) : le cas désigné par une piste indépendante falsifiable (source non officielle, registre des rumeurs, témoignage, signalement interne) qui désigne un contrat précis : la piste doit être formulée de façon falsifiable et testée comme les autres, sans statut privilégié.
- Les 3 anomalies finales : une si possible issue de la Voie 2 si une piste indépendante désigne un contrat, complétée par les deux extrêmes de la Voie 1 (recoupement inter-voies documenté dans `data/cas_selection.csv`).
- 2 cas témoins : des contrats comparables (appariés sur : nature des prestations, période/date de signature, maturité, type de prix et transfert de risque, taille) avec taux de modification quasi nul ou données stables, servant de groupe témoin. Le contraste JO/SOLIDEO de l'enquête APEX inspire le design : témoin = supervision stricte sans dérive.
- Interdiction de choisir les témoins après avoir vu les anomalies (biais de sélection) : la liste des candidats témoins appariés est fixée en même temps que les critères, avant les calculs.
- Artefact : `data/cas_selection.csv` avec justification de sélection (colonnes : id, voie de sélection, montant initial, cumul modifications, taux, nature, fondement documenté, justification, critère préétabli).

### Phase 5 : Demandes CADA ciblées (sur les 3 anomalies + 2 témoins)
- Pièces demandables après signature : acte d'engagement et annexes communicables, rapport d'analyse des offres (occultation des secrets protégés), avenants, bons de commande, factures, PV de réception, décompte général définitif (doctrine CADA marchés publics ; ref. corruption_brainstorm §5).
- Rédaction : demande de documents identifiés (numéro de marché, pièces listées), format électronique natif, acceptation explicite de l'occultation, en lots raisonnables. Adresser à SESN ; noter la date d'envoi.
- Délais : 1 mois, silence = refus ; CADA dans les 2 mois suivant le refus (gratuit, préalable au contentieux).
- IMPORTANT : si la session d'exécution ne peut pas réellement envoyer la demande (pas d'e-mail), produire quand même les 5 courriers prêts à envoyer dans `data/cada_lettres/` horodatés, et le marquer en DELIVERABLE_PENDING dans le registre.
- Artefact : les lettres + registre des réponses obtenues (ou leur absence).

### Phase 6 : Cartographie des acteurs et des contre-flux
- Pour les 5 cas : attributaires (SIREN, RNE), sous-traitants, maître d'œuvre, maîtrise d'ouvrage, membres des jurys/CAC si identifiables.
- Croisements : anciens agents publics dans les attributaires (base HATVP mobilités existante : `2026-08-09_base-hatvp-mobilites`), dirigeants communs entre attributaires (croisement de mandats, cf. `croisement-directeurs-cessions`), bénéficiaires effectifs (accès INPI restreint depuis 31/07/2024 : demande ciblée par intérêt légitime, journaliste/chercheur ; données limitées : nom, mois/année de naissance, pays, nationalité, nature des intérêts ; silence 2 mois = acceptation).
- Renseignement open source complémentaire : OpenSanctions (PEP), OpenCorporates/GLEIF (LEI), fichiers BODACC/DECP.
- Artefact : `data/acteurs_sesn.csv` + noeuds/arêtes du graphe minimal (format CSV : source, relation, cible, document_support).

### Phase 7 : Collecte multi-canal (les sources officielles ne sont ni socle ni déchets)
Applique la doctrine de corruption_brainstorm_2.md : aucune source n'est la vérité, toute source est un acteur situé.
- Les pistes non officielles sont recueillies dès la Phase 1 (`data/registre_pistes.csv`) et alimentent la Voie 2 de la Phase 4 ; la Phase 7 les approfondit (elle n'est PAS leur point de départ).
- 8 familles : documents administratifs ; documents internes/fuites ; témoignages directs ; témoignages indirects ; reportages et enquêtes ; travaux associatifs/syndicaux ; réseaux sociaux/forums ; traces matérielles.
- Pour chaque source : grille d'évaluation (accès, directivité, proximité temporelle, précision, falsifiabilité, authenticité, indépendance, intérêt, cohérence interne/externe, stabilité, complétude).
- Articles de presse : décomposer en affirmations atomiques, remonter la généalogie de chaque information (dépêche AFP répliquée 20 fois = 1 source, pas 20). La relation `RÉPÈTE` est interdite de passage en `CORROBORE`.
- Réseaux sociaux : traiter comme capteur, pas tribunal ; archiver avant contact (Internet Archive, archive.today) ; URL + heure + compte + fichier original ; distinguer auteur original et amplificateurs.
- Témoignages : protocole en 10 points (identité/fonction, récit libre, chronologie, vue/lu/entendu/déduit, mots exacts, documents à l'appui, confrontation progressive, retour, contradictions documentées, conditions de citation). Séparer : OBSERVATION DIRECTE / DOCUMENT VU / DOCUMENT DÉTENU / RÉCIT D'UN TIERS / INTERPRÉTATION / RUMEUR.
- Registre des rumeurs : fichier séparé du dossier des faits (`data/registre_rumeurs.csv`), champs : formulation exacte, première occurrence, origine déclarée, éléments vérifiables, propagation, intérêts possibles, vérifications effectuées, statut. Une rumeur ne passe jamais silencieusement au registre des faits : promotion exigée = trace dure + triangulation indépendante.
- Sécurité : ne jamais promettre une anonymité absolue ; ne pas envoyer de témoignage brut/fuite sensible dans un service LLM tiers sans consentement + anonymisation + évaluation du risque.
- Artefact : `data/sources_sesn.md` (généalogie des sources) + `data/registre_rumeurs.csv` + matrice versions/traces pour les 3 anomalies.

### Phase 8 : Hypothèses concurrentes (matrice de compatibilité, pas de score)
Pour CHAQUE anomalie (les 3 cas) et chaque fait central, construire une matrice (corruption_brainstorm §2.Étape 2, sans note numérique) :
- H0 : décision régulière et économiquement justifiée.
- H1 : mauvaise gestion, impréparation, incompétence.
- H2 : contrainte réelle (urgence, pénurie, technicité, dépendance industrielle).
- H3 : entente entre fournisseurs sans complice public.
- H4 : conflit d'intérêts ou favoritisme (432-14 CP : avantage injustifié par acte contraire aux règles de publicité/mise en concurrence ; NI contrepartie NI paiement occulte requis, la tentative suffit).
- H5 : corruption ou trafic d'influence (contrepartie, pacte, dissimulation).
- H6 : données incomplètes ou mal interprétées.
Les hypothèses ne sont PAS mutuellement exclusives (H4 et H5 peuvent coexister ; H6 affecte toutes les autres) : la matrice ne produit aucun classement « score », elle répond à UNE question : QUELLES EXPLICATIONS RESTENT COMPATIBLES avec les faits ?
Tableau par hypothèse, lignes fixes : observations ATTENDUES si l'hypothèse est vraie ; éléments observés COMPATIBLES ; éléments observés INCOMPATIBLES ; données MANQUANTES pour trancher ; TEST SUIVANT (l'observation ou la pièce qui ferait progresser la discrimination). Chercher activement les éléments disculpants (H0-H3, H6 sont les défauts de base) ; une hypothèse n'est « écartée » que si un élément incompatible est constaté, jamais par absence de preuve.
Reconstituer les chaînes (instrument d'organisation, pas objet d'enquête pré-supposé) : autorité/décision (qui a compétence, préparé, conseillé, signé, contrôlé) ; argent/exécution (enveloppe, contrat, modifications, factures, pénalités, livrables) ; bénéficiaire réel (société, groupe, propriétaires, sous-traitants, intermédiaires) ; avantages et liens (cadeau, emploi, contrat futur, don politique, rétrocommission, avantage à un proche) ; contrôle et neutralisation (qui devait détecter, quelles alertes, pourquoi sans effet). La chaîne de contrepartie n'est reconstituée que si les faits (matrices) la soutiennent ; dans le cas du favoritisme elle n'est pas exigible.
Artefact : `data/hypotheses_sesn.md` (matrice par anomalie : hypothèse × attendus/compatibles/incompatibles/manquantes/test suivant/statut de compatibilité).

### Phase 9 : Droit de réponse et contradiction
- Avant toute conclusion publique : questionnaire factuel, précis, non accusatoire aux personnes concernées ; délai raisonnable ; reproduire loyalement démentis et éléments disculpants ; l'absence de réponse n'est pas un aveu.
- Matrice des contradictions : version institutionnelle vs actes officiels vs traces financières vs documents internes vs témoignages vs médias vs réseaux sociaux vs résultats matériels vs verdict provisoire (établi, corroboré, plausible, non vérifié, contredit, faux).
- Mensonge institutionnel : n'utiliser le terme qu'après démonstration des 3 conditions (information correcte détenue, connaissance du faux, choix de diffusion). Sinon : faux, inexact, incomplet, non étayé, trompeur, contredit, impossible à vérifier.
- Artefact : brouillons des questionnaires dans `data/droit_reponse/`.

### Phase 10 : Qualification pénale par matrice juridique, conclusion graduée, escalade
- Matrice juridique PAR QUALIFICATION candidate, pour chaque anomalie (pas une chaîne pénale unique) : corruption (art. 432-11 et 435-3 CP : pacte, contrepartie, intention), favoritisme (art. 432-14 CP : avantage injustifié par acte contraire aux règles garantissant liberté d'accès et égalité des candidats ; NI contrepartie NI paiement occulte requis, la tentative suffit, l'aptitude à altérer la concurrence suffit, Cass. crim. 19/06/2024 n° 23-84.759), prise illégale d'intérêts (art. 432-12 CP), trafic d'influence (art. 433-1 et 432-11 CP), recel de favoritisme (bénéficiaire).
- Colonnes de la matrice, pour chaque qualification : éléments constitutifs (texte + jurisprudence) ; faits observés FAVORABLES ; faits observés CONTRAIRES ; élément intentionnel (exigible et indices) ; pièces MANQUANTES pour caractériser ; conclusion limitée à la compatibilité : COMPATIBLE / NON ÉTABLIE / EXCLUE (exclue uniquement si un élément incompatible est constaté).
- Toute affirmation devient : « les données établissent X ; la qualification Q est compatible avec les faits ; elle n'est pas démontrée en l'état » (jamais « preuve de corruption » sur un faisceau d'indices).
- Conclusion graduée (corruption_brainstorm §12) : « Les données établissent X et un risque élevé d'atteintes à la probité. Elles ne permettent pas, en l'état, de démontrer un pacte corruptif individuel » si le faisceau s'arrête là.
- Escalade selon la qualification dominante, la compétence matérielle et le statut du déclarant (documenté dans le REGISTRE) : (a) signalement AFA (6 atteintes à la probité) ou PNF (dossiers complexes) avec résumé factuel 2 pages, chronologie, acteurs, montants, qualifications envisagées, index des pièces, éléments contradictoires, questions non résolues ; (b) publication avec base factuelle + prudence d'expression (jurisprudence : bonne foi = intérêt général + base factuelle suffisante + sérieux de l'enquête + prudence + absence d'animosité ; réf. Crim. 25/02/2025 n°23-84.563, méthode en 2 temps) ; (c) base de connaissance interne.
- Le statut de journaliste protégé par le secret des sources (art. 2 loi 1881) exige activité régulière et rétribuée en entreprise de presse : ne pas le présumer pour un enquêteur indépendant non rémunéré ; prudence maximale sur les pièces couvertes par secret (instruction, professionnel, affaires, défense nationale) ; avis d'avocat recommandé avant publication.
- Artefact : dossier INVESTIGATION final + REGISTRE de progression + quintessence + write-back Mnemolite.

## §4 CONVENTIONS DE SORTIE (fichiers et nommage)

Dossier racine du pilote (à créer si absent) :
`investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_pilote-avenants-sesn/`

Fichiers finaux obligatoires (format AGENTS.md, horodatage réel CEST) :
1. `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_pilote-avenants-sesn/YYYY-MM-DD_HH-MM_avenants-sesn-pilote_INVESTIGATION.md` : le dossier forensique final (pipeline KERNEL complet, §0 à §18b ; complexité attendue COMPLEX, minimum MEDIUM : scorer honnêtement via $CX_SCORE).
2. `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_pilote-avenants-sesn/YYYY-MM-DD_HH-MM_avenants-sesn-pilote_REGISTRE.md` : registre de progression (hypothèses, rumeurs, matrice contradictions, demandes CADA et réponses, délais, DELIVERABLE_PENDING).
3. `data/` (DECP brutes + normalisées, mesures, cas sélectionnés, acteurs, registre rumeurs CSV) et `scripts/` (01 à 03 + éventuels) dans le même dossier racine.
4. Le présent protocole reste dans `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_preparation-anticorruption/` : il est le contrat permanent, les nouveaux dossiers le référencent.

Le fichier INVESTIGATION final doit contenir : RUN_MANIFEST, MANIPULATION_REPORT (15 symboles scorés, exigence KERNEL : chaque symbole est scoré sur les faits du dossier, jamais inventé ; un symbole hors périmètre est marqué N/A motivé au lieu d'être forcé), CLUSTERS, HERMÉNEUTIQUE, FORENSIC REASONING, PRISME DIALECTIQUE, CHRONOLOGIE, les matrices d'hypothèses × compatibilité par anomalie, la matrice juridique par qualification, la conclusion graduée, l'option d'escalade (AFA/PNF / publication / base), et l'index des pièces. Les URLs citées doivent être des pages spécifiques cliquables (interdiction : « CDC, rapport annuel »).

## §5 RÈGLES D'EXÉCUTION (agent exécutant : ce qui ne se discute pas)

1. **Mémoire d'abord (mnemolite-mem-first)** : à l'ouverture, `search_memory` (search_mode hybrid) sur « avenants Seine-Nord SESN » + « GAP-001 » + « taux avenant » + « corruption avenants » ; à la clôture, `write_memory` du résultat (tags : project:truth-engine, kernel, sesn, avenants, corruption). La mémoire est un INDEX de faits vérifiés portant source + citation + date de validité, PAS une autorité probatoire : un fait CONFIRMÉ en mémoire est répondable avec source + citation + memory_id et zéro appel web UNIQUEMENT si la mémoire contient la pièce complète (URL, citation, date de vérification). Si la mémoire est incomplète, que la donnée est datée ou volatile (prix, seuils, décisions), ou qu'un doute existe : revérifier (protocole source-verifier) et mettre la mémoire à jour, la date de validité et les conditions de revérification étant consignées dans le write-back.
2. **Vérification forensique** : tout chiffre/date/verdict/URL sensible passe par le protocole source-verifier (Mnemolite d'abord, web après cache miss, write-back obligatoire). Ne jamais citer un rapport (CdC, Sénat) non localisé : statut GAP, pas de remplissage.
3. **Anti-fausse-précision (AGENTS.md §4)** : aucun parseur regex/string-strict ne traite du texte produit par un LLM ; les calculs (taux d'avenant, SIREN, concentration) sont 100 % déterministes, scripts exécutés, résultats archivés. Pas de « score de corruption » agrégé, pas de Benford universel, pas de corrélation = causalité.
4. **Éthique du projet** : zéro flagornerie, droit de contredire l'utilisateur avec preuves, aveu d'ignorance explicite, style direct, français soutenu, zéro em-dash (U+2014) dans tout texte rédigé (utiliser « : », « - », parenthèses).
5. **Précédence** : le KERNEL.md possède l'orchestration/persistance ; le présent protocole possède le périmètre/les phases ; en cas de conflit, KERNEL gagne sur l'ordre et le format de sauvegarde, protocole gagne sur le contenu du pilote.
6. **Reprise d'une session interrompue** : si un STATE:OPEN existe, relire le checkpoint et le registre de progression, reprendre à NEXT_ACTION exact, ne rien réécrire au-dessus ; sinon démarrer au §0.
7. **Temps de travail réaliste** : si une session ne peut couvrir les 10 phases, produire un dossier PARTIEL honnête (STATUS:OPEN, NEXT_ACTION explicite, DELIVERABLE_PENDING listés) : un dossier partiel transparent vaut mieux qu'un dossier complet falsifié. La phase 3 (mesures) et la phase 8 (hypothèses) sont prioritaires ; les phases 5 (CADA) et 9 (droit de réponse) sont des DELIVERABLE_PENDING acceptables en monosaillon si le temps manque, pourvu qu'elles soient tracées dans le REGISTRE.

## §6 RESSOURCES EXISTANTES (à exploiter, pas à refaire)

Corpus juillet 2026 (investigations — les horodatés du 09-07 sont INVALIDES par règle projet, sauf mention contraire ; le corpus août 2026 est valide) :
- `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_avenants-5-grands-projets/2026-08-09_22-33_avenants-5-grands-projets_INVESTIGATION.md` : état des faits sur les 5 projets, chiffres CdC/Sénat, GAP-001 (agrégats d'avenants jamais publiés), mécanisme CCP (L.2194-1 et R.2194-1 à R.2194-9, seuils par fondement : 10/15 % faible montant, 50 % circonstances imprévues), jurisprudence CE « modification substantielle », contraste JO/SOLIDEO. À lire en priorité.
- `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_surfacturation-commande-publique/` : cadre des mécanismes de surfacturation (GAP-001 ACCESS hérité).
- `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_base-hatvp-mobilites/` et `2026-08-09_revolving-doors-ape-bercy/` : mobilités public-privé (pantouflage), utiles Phase 6.
- `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_croisement-directeurs-cessions/` : méthode de croisement de mandats/dirigeants, modèle pour l'analyse de réseau.
- `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_faisceaux-angles-morts_HYPER_MATRICE.md` : modèles de matérialisation des faisceaux.
- `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_bilan-trous-noirs_REGISTRE.md` et `2026-08-09_point-consolide-journee_REGISTRE.md` : registres de suivi des gaps et trous noirs, format de référence pour le REGISTRE du pilote.
- `truth-engine-v2/KERNEL.md` : pipeline v2.8 (déjà cité §0), + `truth-engine-v2/forensic/GATES.md`, `REQUEST_LOG.md`, `definitions/` : à charger (ALWAYS LOAD) selon KERNEL.

Règles de gestion des ressources : un fait trouvé dans une investigation existante est cité avec son FCT-### et sa source, pas re-vérifié au web (sauf doute) ; les URLs mortes (ex. rapport Sénat GPE 2023 en 404) restent en GAP, jamais reconstituées.

## §7 VÉRIFICATION FINALE (avant clôture)

1. Relire le dossier INVESTIGATION en entier : chaque chiffre porte un SRC-ID + locator (page/paragraphe/ligne/cellule), chaque conclusion graduée correspond aux statuts (établi/corroboré/allégué/inféré/contredit/inconnu), aucune URL générique.
2. Relire le REGISTRE : hypothèses concurrentes complètes pour les 3 anomalies, rumeurs confinées (jamais dans les faits), demandes CADA tracées (envoyées OU DELIVERABLE_PENDING), contradictions documentées sans effacement.
3. Vérifier la cohérence des artefacts : `data/` et `scripts/` présents, hash présents, scripts exécutables (au moins documentés), SIREN normalisés, dédoublonnage fait.
4. Vérifier le pipeline KERNEL : MANIPULATION_REPORT (15 symboles scorés), GATES (aucun décisionnel sans source), write-back Mnemolite effectué.
5. Conclusion finale : si le faisceau est complet → STATUS:FINAL, FREEZE ; sinon → STATUS:OPEN + NEXT_ACTION explicite + DELIVERABLE_PENDING. Jamais de dossier « complet » à moitié rempli.
6. Si le temps le permet : exécuter les 26 tests du pipeline extractors (`pytest tests/extractors/ -v`) pour valider les modules de quintessence disponibles.

## §8 LANCEMENT (agent à contexte vierge, chemin d'exécution)

1. Lire ce fichier (§0 à §8), puis les 8 documents de §0.
2. `search_memory` (hybrid) comme indiqué §5.1 ; vérifier s'il existe déjà un STATE:OPEN sur ce sujet (sinon démarrer nouveau RUN_ID).
3. Créer le dossier pilote + `data/` + `scripts/` ; ouvrir le checkpoint KERNEL (Phase 0 du KERNEL, RUN_MANIFEST complet, INVESTIGATION_PATH stable).
4. Exécuter les phases 1 → 10 séquentiellement, avec artefact à chaque phase.
5. À la fin : dossier INVESTIGATION + REGISTRE + artefacts + write-back, puis vérification §7.
6. En cas de blocage (source inaccessible, donnée manquante, contradiction insoluble) : ne pas simuler la réussite : écrire le GAP exact (nature, tentative, méthode, résultat observé) et continuer sur ce qui reste accessible.

Fin du protocole. Le présent document est la référence contractuelle ; toute modification ultérieure passe par une édition du protocole (nouvelle version datée), jamais par un changement tacite en cours d'exécution.

## JOURNAL DES VERSIONS

- **v1.1 (2026-08-10)** : intégration de la revue externe (dossier tmp3, 3 fichiers revus : README, REGISTRE, protocole). Changements : (1) modèle événementiel des modifications DECP (montant modifié = nouveau total, interdit d'additionner, révisions de prix exonérées) ; (2) recensement de l'univers complet multi-sources (DECP consolidées moins exhaustives depuis 2024, SCSNE, AWS, BOAMP, TED), date de coupure fixée au RUN_MANIFEST, marchés sans montant conservés, sélection gérée avant calculs ; (3) sélection à deux voies : max hausse absolue, max hausse relative avec seuil de matérialité, piste indépendante falsifiable (registre ouvert dès la Phase 1) ; témoins appariés (nature, période, maturité, type de prix, transfert de risque, taille) fixés avant les calculs ; (4) seuils juridiques par fondement (R.2194-8 faible montant 10/15 %, cumul R.2194-9, 50 % R.2194-3 circonstances imprévues par modification), indicateur = proximité au seuil applicable au fondement déclaré ; (5) hypothèses H0-H6 en matrice de compatibilité (attendus/compatibles/incompatibles/manquantes/test suivant), pas de score, hypothèses non mutuellement exclusives, objectif reformulé « quelles explications restent compatibles » sans présomption de chaîne de contrepartie ; (6) Phase 10 en matrice juridique par qualification (corruption, favoritisme 432-14 sans contrepartie, prise illégale d'intérêts, trafic d'influence, recel) avec conclusion COMPATIBLE/NON ÉTABLIE/EXCLUE ; escalade selon qualification dominante, compétence et statut du déclarant ; (7) mémoire = index probatoire (source + citation + date de validité), pas autorité ; (8) éditorial : corruption_defintion.md renommé en corruption_definition.md, clé de dédoublonnage (identifiant marché, acheteur, lot, version), « déments » → « démentis », artefacts conditionnés aux questions.