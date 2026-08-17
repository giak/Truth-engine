# PROTOCOLE PILOTE « AVENANTS SESN » : BRIEF AUTONOME POUR AGENT À CONTEXTE VIERGE

> Type : ARCHITECTURE. Statut : DESIGN VALIDÉ (utilisateur, 2026-08-10). Ce document est le point d'entrée unique de toute exécution du pilote. Un agent démarrant sans aucun contexte doit lire ce fichier en premier et suivre §0 avant toute autre action.

## §0 NOTICE DE LECTURE OBLIGATOIRE (agent exécutant)

Lire dans cet ordre strict, avant toute recherche ou écriture :

1. Ce fichier (le présent protocole), intégralement.
2. `/home/giak/projects/truth-engine/AGENTS.md` : règles du projet (éthique, nommage, RTK, WRITE+EDIT, protocole mem-first).
3. `/home/giak/projects/truth-engine/truth-engine-v2/KERNEL.md` : le pipeline d'investigation v2.8 (texte canonique). Le §0-§7 du KERNEL gouvernent toutes les phases ; le présent protocole ne le remplace pas, il le spécialise pour un périmètre précis.
4. `/home/giak/projects/truth-engine/investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_preparation-anticorruption/corruption_defintion.md` : les 3 niveaux de corruption, le critère du lien de contrepartie (§6 : ce qui ne prouve pas seul).
5. `/home/giak/projects/truth-engine/investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_preparation-anticorruption/corruption_brainstorm.md` : protocole générique (hypothèses concurrentes H0-H6, 5 chaînes, CADA, signaux, analyse quantitative, discipline RAW→FAITS→RELATIONS→HYPOTHÈSES→QUALIFICATIONS).
6. `/home/giak/projects/truth-engine/investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_preparation-anticorruption/corruption_brainstorm_2.md` : doctrine multi-canal (8 familles de sources, grille d'évaluation, registre des rumeurs, matrice versions/traces, relation RÉPÈTE, triangulation).
7. `/home/giak/projects/truth-engine/investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_avenants-5-grands-projets/2026-08-09_22-33_avenants-5-grands-projets_INVESTIGATION.md` : l'enquête APEX existante (état des faits, GAP-001, chiffres CdC/Sénat, acteurs). C'est la ressource héritée la plus importante du pilote.
8. Dossier `/home/giak/projects/truth-engine/investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_surfacturation-commande-publique/` (parent de l'enquête avenants) : mécanismes de surfacturation et GAP-001 ACCESS.

Interdits absolus pendant l'exécution :
- commencer une recherche ou une conclusion avant d'avoir lu les 8 éléments ci-dessus ;
- dévier du pipeline KERNEL : toute sortie dossier doit être un dossier forensique au format INVESTIGATION, jamais un article ;
- inventer un chiffre, une date, un montant ou une URL : toute affirmation décisionnelle doit porter un SRC-ID et un locator (voir §7) ;
- utiliser le mot « preuve » pour un indice isolé : la qualification finale suit la méthode §6 de corruption_defintion.md.

## §1 POURQUOI (contexte et justification)

1. **Cadre général.** La corruption en France est rarement identifiable par une preuve directe. Le corpus 2026-08 du projet (40+ investigations : CumCum, Dutreil, HATVP, cessions, EDF OPA, banques-conseils) a établi que l'on dispose surtout d'indices et de faisceaux concordants : surfacturation, avenants au-dessus des seuils, pantouflage, avantages de complaisance. L'ambition du présent pilote est de tester une méthode reproductible qui transforme des gaps documentaires en objets d'enquête.
2. **Le trou noir documentaire (GAP-001).** L'enquête APEX du 09-08 a vérifié qu'aucune institution ne publie le montant cumulé des avenants des 5 grands projets publics (EPR, Grand Paris, JO, Seine-Nord, Hôpital). Les données existent : les données essentielles de la commande publique (DECP) sont obligatoires depuis 2019 (arrêté du 22/03/2019) et contiennent les avenants. Personne ne les agrège, ni EDF, ni la SGP, ni SOLIDEO, ni SESN, ni AP-HP (FCT-001 à FCT-003 de l'enquête APEX).
3. **Le contre-exemple JO 2024.** Le seul projet maîtrisé (6,6 Md€, CdC 29/09/2025, « pas de dérapage », « rares anomalies ») est le seul doté d'une supervision stricte des avenants (SOLIDEO). Corrélation documentée, causalité non établie : le pilote doit produire des données comparables là où l'État n'en produit pas, sans conclure à la causalité.
4. **Pourquoi Seine-Nord.** Ses atouts : volume borné (74-76 marchés), avenants « fréquents » documentés, rapport CdC récent (10/04/2026, 7,347 Md€, dérive +2,2-2,8 Md€ hors frais financiers, ~10 Md€ avec), SESN acheteur public soumis aux DECP, contrôle des données réalisable par un indépendant. Le surcoût est documenté officiellement ; la part imputable est le trou noir.
5. **Hypothèse de travail (à éprouver, jamais prémisse).** Les dérives de coûts passent en partie par des avenants dans les seuils (10 % fournitures/services, 15 % travaux, 50 % prestations indispensables, CCP L2194), qui permettent d'augmenter les prix sans nouvelle mise en concurrence. La jurisprudence Conseil d'État (modification substantielle = nouvelle concurrence) borne la partie illégale. Le pilote cherche à QUANTIFIER la part passant par avenants sur un échantillon borné et à la confronter aux explications officielles (aléas, inflation, retards, besoins perfectibles).
6. **Usage final (décidé).** Mixte, à décider à l'issue selon la qualité du faisceau : (a) signalement AFA/PNF si cohérence suffisante, (b) publication/article si base factuelle + prudence d'expression garanties, (c) base de connaissance interne sinon. Le dossier doit être structuré pour permettre les trois.

## §2 CE QUE L'ON VEUT FAIRE (objectif, périmètre, livrables)

### Objectif central
Produire le premier agrégat public extérieur des avenants d'un grand projet public (Canal Seine-Nord Europe) sur 5 exercices, calculer un taux d'avenant par contrat sur un échantillon de 30 contrats, sélectionner 3 anomalies + 2 cas normaux, les qualifier selon la grille des hypothèses concurrentes, et documenter la chaîne de contrepartie (qui a décidé, qui a payé, qui a bénéficié, qui a contrôlé, qui a neutralisé le contrôle).

### Périmètre exact
- Acheteur : SESN (Société du Canal Seine-Nord Europe), établissement public.
- Famille de dépenses : marchés de travaux (génie civil, secteurs hydrauliques, dépendances vertes, ordinateurs_) ; couvrir aussi marchés de maîtrise d'œuvre et de contrôle si nécessaires au calcul.
- Période : 5 exercices, 2021-2026 (DECP disponibles depuis 2019 ; la construction débutant en 2023-2024, ajuster si l'échantillon est vide : étendre à 2019-2026).
- Échantillon : 30 contrats les plus importants en montant initial (ou 30 plus gros cumul contrat+avenants si plus parlant), hors marchés à prix non renseigné.
- Unité d'analyse : contrat = données de base + nombre et montant cumulé des avenants associés.

### Livrables (ordre de production)
1. `data/` : DECP brutes SESN (téléchargées, hashées SHA-256) + table normalisée SIREN/SIRET (CSV).
2. `scripts/` : scripts déterministes d'extraction et de calcul (Python ou shell, auto-documentés) : téléchargement DECP, normalisation SIREN, calcul taux d'avenant, concentration, seuils.
3. Le dossier d'investigation final KERNEL (INVESTIGATION, format §8) avec la conclusion graduée et l'option d'escalade.
4. Un registre de progression (REGISTRE) horodaté : hypothèses concurrentes par anomalie, registre des rumeurs (séparé des faits), matrice versions/traces pour les 3 anomalies.
5. quintessence YAML (via SUMBLIMATOR §parse_atomic/curator si le volume de faits le permet) et write-back Mnemolite (recherche à l'ouverture, écriture à la clôture, tags project:truth-engine + kernel + sesn + avenants).

## §3 COMMENT (méthode en 10 phases, approche C « pilote itératif avec legs »)

Chaque phase produit un artefact réutilisable (script + table + hash) déposé dans le dossier du pilote. L'infrastructure naît de la phase, jamais avant. Respecter l'ordre ; une phase ne commence que si la précédente a livré son artefact.

### Phase 1 : Extraction DECP
- Source : données essentielles de la commande publique, fichiers consolidés data.gouv.fr (lien exact dans le registre de progression) ; en complément : place.des-marches-publics.gouv.fr et BOAMP pour les avis de SESN.
- Critères de filtrage : pouvoir adjudicateur = SESN (et ses formes socle exactes, à vérifier, ex. « Société du Canal Seine-Nord Europe »), période 2019-2026, type = marchés (pas uniquement accords-cadres ; tracer le type).
- Artefact : `data/decp_sesn_raw.csv` + `decp_sesn_raw.sha256` + script `scripts/01_extract_decp.py` (ou shell). HASH_CAPABILITY : si l'environnement ne fournit pas sha256, le noter en DEGRADED_FLAG (pas d'invention).
- Contrôle qualité : nombre total de contrats extraits vs nombre déclaré dans le rapport CdC (74-76 marchés) : écarter ou documenter l'écart.

### Phase 2 : Normalisation SIREN/SIRET
- Nettoyage strictement déterministe : zéros perdus, espaces, clé de Luhn sur SIRET, dédoublonnage par (SIREN, objet, montant). Interdiction d'utiliser un LLM pour ce nettoyage (règle anti-fausse-précision, AGENTS.md §4).
- Rapprochement RNE/INPI (data.inpi.fr, API SIRENE) pour les attributaires non identifiés.
- Artefact : `data/decp_sesn_norm.csv` + script `scripts/02_normalize_siren.py` + liste des SIREN non résolus.

### Phase 3 : Mesures quantitatives
Pour chaque contrat de l'échantillon : montant initial, montant final (si présent dans les données), nombre d'avenants, montant cumulé des avenants, taux d'avenant = montant cumulé avenants / montant initial.
Indicateurs agrégés (cf. corruption_brainstorm §7) :
- part des 5 premiers fournisseurs (concentration) ;
- fréquence des procédures négociées et des candidatures uniques ;
- montants cumulés des avenants rapportés aux montants initiaux ;
- proximité aux seuils 10/15/50 % (CCP L2194) et seuils procéduraux ;
- prix unitaires comparés à des transactions homogènes (tunnels, terrassements, ouvrages d'art) ;
- durée publication → clôture ; récurrence des sous-traitants.
Règle : ne comparer que des opérations réellement homogènes (même nature, même volume, même transfert de risque, même période). Pas de loi de Benford comme détecteur universel ; pas de score de corruption ; pas de corrélation de graphe traitée comme causalité.
Artefact : `data/mesures_sesn.csv` + script `scripts/03_mesures.py` + `data/concentration_sesn.csv`.

### Phase 4 : Sélection des cas (3 anomalies + 2 normaux)
- 3 anomalies : les contrats dont le taux d'avenant est le plus élevé, ou dont la trajectoire contrat → avenants viole la proportionnalité (ex. avenants successifs dépassant 15 % cumulés pour des travaux ; plusieurs avenants de même nature rapprochés).
- 2 cas normaux : des contrats comparables (nature, taille) avec taux d'avenant quasi nul, servant de groupe témoin. Le contraste JO/SOLIDEO de l'enquête APEX inspire le design : témoin = supervision stricte sans dérive.
- Artefact : `data/cas_selection.csv` avec justification de sélection (colonnes : id, montant initial, cumul avenants, taux, nature, justification).

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
- 8 familles : documents administratifs ; documents internes/fuites ; témoignages directs ; témoignages indirects ; reportages et enquêtes ; travaux associatifs/syndicaux ; réseaux sociaux/forums ; traces matérielles.
- Pour chaque source : grille d'évaluation (accès, directivité, proximité temporelle, précision, falsifiabilité, authenticité, indépendance, intérêt, cohérence interne/externe, stabilité, complétude).
- Articles de presse : décomposer en affirmations atomiques, remonter la généalogie de chaque information (dépêche AFP répliquée 20 fois = 1 source, pas 20). La relation `RÉPÈTE` est interdite de passage en `CORROBORE`.
- Réseaux sociaux : traiter comme capteur, pas tribunal ; archiver avant contact (Internet Archive, archive.today) ; URL + heure + compte + fichier original ; distinguer auteur original et amplificateurs.
- Témoignages : protocole en 10 points (identité/fonction, récit libre, chronologie, vue/lu/entendu/déduit, mots exacts, documents à l'appui, confrontation progressive, retour, contradictions documentées, conditions de citation). Séparer : OBSERVATION DIRECTE / DOCUMENT VU / DOCUMENT DÉTENU / RÉCIT D'UN TIERS / INTERPRÉTATION / RUMEUR.
- Registre des rumeurs : fichier séparé du dossier des faits (`data/registre_rumeurs.csv`), champs : formulation exacte, première occurrence, origine déclarée, éléments vérifiables, propagation, intérêts possibles, vérifications effectuées, statut. Une rumeur ne passe jamais silencieusement au registre des faits : promotion exigée = trace dure + triangulation indépendante.
- Sécurité : ne jamais promettre une anonymité absolue ; ne pas envoyer de témoignage brut/fuite sensible dans un service LLM tiers sans consentement + anonymisation + évaluation du risque.
- Artefact : `data/sources_sesn.md` (généalogie des sources) + `data/registre_rumeurs.csv` + matrice versions/traces pour les 3 anomalies.

### Phase 8 : Hypothèses concurrentes et chaînes
Pour CHAQUE anomalie (les 3 cas) et chaque fait central, imposer et scorer les hypothèses (corruption_brainstorm §2.Étape 2) :
- H0 : décision régulière et économiquement justifiée.
- H1 : mauvaise gestion, impréparation, incompétence.
- H2 : contrainte réelle (urgence, pénurie, technicité, dépendance industrielle).
- H3 : entente entre fournisseurs sans complice public.
- H4 : conflit d'intérêts ou favoritisme.
- H5 : corruption ou trafic d'influence.
- H6 : données incomplètes ou mal interprétées.
Définir ce qui confirmerait/invaliderait chaque hypothèse ; chercher activement les éléments disculpants (H0-H3, H6 sont les défauts de base).
Reconstituer les 5 chaînes : autorité/décision (qui a compétence, préparé, conseillé, signé, contrôlé) ; argent/exécution (enveloppe, contrat, avenants, factures, pénalités, livrables) ; bénéficiaire réel (société, groupe, propriétaires, sous-traitants, intermédiaires) ; contre-avantage (cadeau, emploi, contrat futur, don politique, rétrocommission, avantage à un proche) ; contrôle et neutralisation (qui devait détecter, quelles alertes, pourquoi sans effet).
Artefact : `data/hypotheses_sesn.md` (tableau hypothèse × preuve/contre-preuve × statut).

### Phase 9 : Droit de réponse et contradiction
- Avant toute conclusion publique : questionnaire factuel, précis, non accusatoire aux personnes concernées ; délai raisonnable ; reproduire loyalement déments et éléments disculpants ; l'absence de réponse n'est pas un aveu.
- Matrice des contradictions : version institutionnelle vs actes officiels vs traces financières vs documents internes vs témoignages vs médias vs réseaux sociaux vs résultats matériels vs verdict provisoire (établi, corroboré, plausible, non vérifié, contredit, faux).
- Mensonge institutionnel : n'utiliser le terme qu'après démonstration des 3 conditions (information correcte détenue, connaissance du faux, choix de diffusion). Sinon : faux, inexact, incomplet, non étayé, trompeur, contredit, impossible à vérifier.
- Artefact : brouillons des questionnaires dans `data/droit_reponse/`.

### Phase 10 : Qualification, conclusion graduée, escalade
- Reconstitution de la chaîne causale (jamais la simple accumulation) : avantage public accordé → irrégularité de procédure → connaissance préalable → relation entre acteurs → contre-avantage → conscience et dissimulation. Écrire explicitement ce qui est établi, corroboré, allégué, inféré, contredit, inconnu.
- Conclusion graduée (corruption_brainstorm §12) : « Les données établissent X et un risque élevé d'atteintes à la probité. Elles ne permettent pas, en l'état, de démontrer un pacte corruptif individuel » si le faisceau s'arrête là.
- Escalade selon la qualité : (a) signalement AFA (6 atteintes à la probité) ou PNF (dossiers complexes) avec résumé factuel 2 pages, chronologie, acteurs, montants, qualifications envisagées, index des pièces, éléments contradictoires, questions non résolues ; (b) publication avec base factuelle + prudence d'expression (jurisprudence : bonne foi = intérêt général + base factuelle suffisante + sérieux de l'enquête + prudence + absence d'animosité ; réf. Crim. 25/02/2025 n°23-84.563, méthode en 2 temps) ; (c) base de connaissance interne.
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

Le fichier INVESTIGATION final doit contenir : RUN_MANIFEST, MANIPULATION_REPORT (15 symboles scorés, obligatoire), CLUSTERS, HERMÉNEUTIQUE, FORENSIC REASONING, PRISME DIALECTIQUE, CHRONOLOGIE, la matrice hypothèses × preuves, la conclusion graduée, l'option d'escalade (AFA/PNF / publication / base), et l'index des pièces. Les URLs citées doivent être des pages spécifiques cliquables (interdiction : « CDC, rapport annuel »).

## §5 RÈGLES D'EXÉCUTION (agent exécutant : ce qui ne se discute pas)

1. **Mémoire d'abord (mnemolite-mem-first)** : à l'ouverture, `search_memory` (search_mode hybrid) sur « avenants Seine-Nord SESN » + « GAP-001 » + « taux avenant » + « corruption avenants » ; à la clôture, `write_memory` du résultat (tags : project:truth-engine, kernel, sesn, avenants, corruption). Tout fait CONFIRMÉ en mémoire → répondre avec source + citation + memory_id, zéro appel web.
2. **Vérification forensique** : tout chiffre/date/verdict/URL sensible passe par le protocole source-verifier (Mnemolite d'abord, web après cache miss, write-back obligatoire). Ne jamais citer un rapport (CdC, Sénat) non localisé : statut GAP, pas de remplissage.
3. **Anti-fausse-précision (AGENTS.md §4)** : aucun parseur regex/string-strict ne traite du texte produit par un LLM ; les calculs (taux d'avenant, SIREN, concentration) sont 100 % déterministes, scripts exécutés, résultats archivés. Pas de « score de corruption » agrégé, pas de Benford universel, pas de corrélation = causalité.
4. **Éthique du projet** : zéro flagornerie, droit de contredire l'utilisateur avec preuves, aveu d'ignorance explicite, style direct, français soutenu, zéro em-dash (U+2014) dans tout texte rédigé (utiliser « : », « - », parenthèses).
5. **Précédence** : le KERNEL.md possède l'orchestration/persistance ; le présent protocole possède le périmètre/les phases ; en cas de conflit, KERNEL gagne sur l'ordre et le format de sauvegarde, protocole gagne sur le contenu du pilote.
6. **Reprise d'une session interrompue** : si un STATE:OPEN existe, relire le checkpoint et le registre de progression, reprendre à NEXT_ACTION exact, ne rien réécrire au-dessus ; sinon démarrer au §0.
7. **Temps de travail réaliste** : si une session ne peut couvrir les 10 phases, produire un dossier PARTIEL honnête (STATUS:OPEN, NEXT_ACTION explicite, DELIVERABLE_PENDING listés) : un dossier partiel transparent vaut mieux qu'un dossier complet falsifié. La phase 3 (mesures) et la phase 8 (hypothèses) sont prioritaires ; les phases 5 (CADA) et 9 (droit de réponse) sont des DELIVERABLE_PENDING acceptables en monosaillon si le temps manque, pourvu qu'elles soient tracées dans le REGISTRE.

## §6 RESSOURCES EXISTANTES (à exploiter, pas à refaire)

Corpus juillet 2026 (investigations — les horodatés du 09-07 sont INVALIDES par règle projet, sauf mention contraire ; le corpus août 2026 est valide) :
- `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_avenants-5-grands-projets/2026-08-09_22-33_avenants-5-grands-projets_INVESTIGATION.md` : état des faits sur les 5 projets, chiffres CdC/Sénat, GAP-001 (agrégats d'avenants jamais publiés), mécanisme CCP L2194 (seuils 10/15/50 %), jurisprudence CE « modification substantielle », contraste JO/SOLIDEO. À lire en priorité.
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