# README : Dossier commun de préparation aux investigations anticorruption

Ce dossier est le point d'entrée de LECTURE de la préparation méthodologique aux investigations anticorruption du projet Truth Engine : tout nouvel agent, toute nouvelle session, toute enquête sur ce thème commence ici, puis suit l'ordre de lecture ci-dessous. Le protocole pilote (`*_ARCHITECTURE.md`) est le contrat d'EXÉCUTION : un agent doit l'exécuter le lit en premier et suit son §0 avant toute autre action.

## Rôle du dossier

Il rassemble la doctrine, le protocole pilote et le suivi de traçabilité : ce que l'on veut faire, pourquoi, comment, et où on en est. Il est conçu pour qu'un LLM à contexte vierge puisse reprendre le travail sans contexte antérieur : lire ce README, puis le protocole, puis exécuter.

## Structure du dossier (règle R12)

La racine ne contient QUE ce README. Les fichiers sont rangés par nature :
- `doctrine/` : références stables (3 doctrines) et capitalisation (leçons 16-30) ;
- `protocole/` : contrats opérationnels (pilote 07-10, playbook 12-38, règles 17-02, canaux 17-10, registre des demandes 17-11) ;
- `suivi/` : dashboard (07-19) et comptes rendus de session (12-39) ;
- `pistes/` : fiches d'enquêtes planifiées (07-29) ;
- `data/` : artefacts bruts et hashes ;
- `archive/` : revues et documents historiques (tmp3-revue-externe-2026-07-45).

## Contenu

| Fichier (chemin relatif) | Rôle | Statut |
|---------|------|--------|
| `doctrine/corruption_definition.md` | Doctrine juridique : les 3 niveaux de corruption, les qualifications pénales, les formes systémiques, le critère du lien de contrepartie (§6) | Référence |
| `doctrine/corruption_brainstorm.md` | Protocole générique d'enquête : hypothèses concurrentes H0-H6, 5 chaînes, CADA, signaux d'alerte, analyse quantitative, discipline probatoire (grille §8 avec axe P/L/LL), **§6 pattern opacité institutionnelle (auditions commission eco jamais transcrites, sauf art. 13)**, **§13 axe légitimité (légal ≠ légitime, grille de conclusion 3 axes obligatoire, sous-section contrôle déclaratif des fonctions bénévoles point 6 FAQ HATVP + application FEDEREC/Carenco)**, témoins, droit de réponse, signalement | Référence (v1.5, 2026-08-11) |
| `doctrine/corruption_brainstorm_2.md` | Doctrine multi-canal : 8 familles de sources, grille d'évaluation, registre des rumeurs, matrice versions/traces, relation `RÉPÈTE`, triangulation, mensonge institutionnel | Référence |
| `doctrine/2026-08-10_16-30_legons-pilote-sesn_LEÇONS.md` | **Capitalisation du pilote SESN** : bilan honnête (aucune corruption prouvée, fait systémique = 148 avenants invisibles), 7 leçons méthodologiques (L1-L7 : concentration vs agrément d'État, marchés subséquents, CADA en phase 1 bis, rapports CdC d'abord, non-publication DECP ≠ infraction, seuils légaux, format), résidus actionnables, prochains axes | Référence (16:30, hash 8e9aca54) |
| `protocole/2026-08-10_07-10_pilote-avenants-sesn_ARCHITECTURE.md` | Protocole opérationnel du pilote v1.1 : recensement complet des modifications contractuelles SESN (exercices 2021-2026, univers multi-sources DECP/SCSNE/AWS/BOAMP/TED), modèle événementiel, méthode en 10 phases, conventions de sortie, règles d'exécution | Contrat exécuté (pilote CLOS 16:30) |
| `protocole/2026-08-10_12-38_playbook-acces-donnees_ARCHITECTURE.md` | **Playbook d'accès aux données** : 13 familles de sources institutionnelles (Légifrance, AN, Sénat, CdC, HATVP, CSS, CASD, CNIS, budget, archives, INPI, académiques, presse), 10 outils génériques, 4 canaux d'accès forcé (CADA, QE, commission d'enquête, CSS), bibliothèque /tmp des documents déjà extraits. Chaque route est datée et sourcée aux 68 dossiers du 09-10/08/2026 | Référence opérationnelle |
| `protocole/2026-08-10_17-02_regles-organisation_ARCHITECTURE.md` | **Règles d'organisation des fichiers (contraintes absolues)** : un travail = un dossier dédié, racine plate (pas de sous-dossier intermédiaire), vérification par grep avant création, mise à jour des références après déplacement, protocoles transverses dans le dossier commun, structure du dossier commun R12, check-list de clôture R1-R12 | CONTRAT (à lire avant toute création de dossier ou de fichier) |
| `protocole/2026-08-10_17-10_canaux-numeriques-acces_ARCHITECTURE.md` | **Canaux numériques de demande d'accès** : décision (abandon voie papier, OSINT numérique prioritaire), tableau des canaux numériques par institution (CADA en ligne vérifié, madada, emails CRE/CdC/SCSNE, PRADA economie.gouv.fr), procédure numérique standard, conversion des lettres en modèles email | CONTRAT EN VIGUEUR |
| `protocole/2026-08-10_17-11_registre-demandes-acces_REGISTRE.md` | **Registre central des demandes d'accès** (transverse à toutes les enquêtes) : inventaire des 8 demandes rédigées (SESN ×4, ENR ×2, BNDP ×2) avec cible, objet, canal numérique, pièce, statut ; pipeline D09-D11 (HATVP, Archives nationales, INPI) ; procédure de suivi des délais (1 mois, refus tacite, saisine CADA en ligne) | CONTRAT EN VIGUEUR |
| `suivi/2026-08-10_07-19_preparation-anticorruption_REGISTRE.md` | Dashboard de traçabilité : état des artefacts, des fact-checks, des décisions, des sessions | Suivi |
| `suivi/2026-08-10_12-39_pilote-sesn-reprise_COMPTE_RENDU.md` | Compte rendu de la reprise du pilote SESN (deux chantiers parallèles : enquêtes + préparation) | Suivi |
| `pistes/2026-08-10_07-29_energies-renouvelables-piste_PISTE.md` | Piste d'enquête planifiée : énergies renouvelables (éolien, solaire) | Piste |

## Comment lire (ordre recommandé)

1. Ce README.
2. `protocole/2026-08-10_17-02_regles-organisation_ARCHITECTURE.md` : les règles d'organisation des fichiers, dont la structure du dossier commun R12 (à lire AVANT toute création de dossier ou de fichier, elles sont contraignantes).
3. `protocole/2026-08-10_17-10_canaux-numeriques-acces_ARCHITECTURE.md` : les canaux numériques de demande d'accès (décision : pas de voie papier ; à consulter avant toute demande de document).
4. `protocole/2026-08-10_17-11_registre-demandes-acces_REGISTRE.md` : le registre central des demandes d'accès (à mettre à jour à chaque nouvelle demande, où qu'elle soit rédigée).
5. `doctrine/corruption_definition.md` : la base juridique et conceptuelle.
6. `doctrine/corruption_brainstorm.md` : le protocole générique.
7. `doctrine/corruption_brainstorm_2.md` : l'extension multi-canal.
8. `protocole/2026-08-10_12-38_playbook-acces-donnees_ARCHITECTURE.md` : le référentiel des routes d'accès aux sources (à consulter avant toute récupération de document).
9. `protocole/2026-08-10_07-10_pilote-avenants-sesn_ARCHITECTURE.md` : le contrat d'exécution du pilote, qui référence lui-même les fichiers du KERNEL (`truth-engine-v2/KERNEL.md`).
10. `suivi/2026-08-10_07-19_preparation-anticorruption_REGISTRE.md` : le dashboard, état courant du chantier.
11. `doctrine/2026-08-10_16-30_legons-pilote-sesn_LEÇONS.md` : les leçons du premier pilote (à lire avant tout nouveau pilote).

## Règles transverses

- Tout fichier produit dans `investigations/` respecte la convention de nommage horodaté `YYYY-MM-DD_HH-MM_<sujet>_<type>.md` (voir AGENTS.md).
- Toute vérification de fait suit le protocole mnemolite-mem-first : Mnemolite d'abord, web après cache miss, write-back obligatoire.
- Les sources officielles sont une famille de traces parmi d'autres : ni socle de vérité, ni déchets à exclure (corruption_brainstorm_2.md §13).
- La conclusion graduée est la norme : on écrit ce qui est établi, corroboré, allégué, inféré, contredit, inconnu. Jamais « preuve » pour un indice isolé.
