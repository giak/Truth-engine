# README : Dossier commun de préparation aux investigations anticorruption

Ce dossier est le point d'entrée unique de la préparation méthodologique aux investigations anticorruption du projet Truth Engine. Tout nouvel agent, toute nouvelle session, toute enquête sur ce thème commence ici.

## Rôle du dossier

Il rassemble la doctrine, le protocole pilote et le suivi de traçabilité : ce que l'on veut faire, pourquoi, comment, et où on en est. Il est conçu pour qu'un LLM à contexte vierge puisse reprendre le travail sans contexte antérieur : lire ce README, puis le protocole, puis exécuter.

## Contenu

| Fichier | Rôle | Statut |
|---------|------|--------|
| `corruption_defintion.md` | Doctrine juridique : les 3 niveaux de corruption, les qualifications pénales, les formes systémiques, le critère du lien de contrepartie (§6) | Référence |
| `corruption_brainstorm.md` | Protocole générique d'enquête : hypothèses concurrentes H0-H6, 5 chaînes, CADA, signaux d'alerte, analyse quantitative, discipline probatoire, témoins, droit de réponse, signalement | Référence |
| `corruption_brainstorm_2.md` | Doctrine multi-canal : 8 familles de sources, grille d'évaluation, registre des rumeurs, matrice versions/traces, relation `RÉPÈTE`, triangulation, mensonge institutionnel | Référence |
| `2026-08-10_07-10_pilote-avenants-sesn_ARCHITECTURE.md` | Protocole opérationnel du pilote : agréger les avenants SESN (30 contrats, 5 exercices), méthode en 10 phases, conventions de sortie, règles d'exécution | Contrat actif |
| `YYYY-MM-DD_HH-MM_preparation-anticorruption_REGISTRE.md` | Dashboard de traçabilité : état des artefacts, des fact-checks, des décisions, des sessions | Suivi |

## Comment lire (ordre recommandé)

1. Ce README.
2. `corruption_defintion.md` : la base juridique et conceptuelle.
3. `corruption_brainstorm.md` : le protocole générique.
4. `corruption_brainstorm_2.md` : l'extension multi-canal.
5. Le protocole pilote (`*_ARCHITECTURE.md`) : le contrat d'exécution, qui référence lui-même les fichiers du KERNEL (`truth-engine-v2/KERNEL.md`).
6. Le dashboard (`*_REGISTRE.md`) : l'état courant du chantier.

## Règles transverses

- Tout fichier produit dans `investigations/` respecte la convention de nommage horodaté `YYYY-MM-DD_HH-MM_<sujet>_<type>.md` (voir AGENTS.md).
- Toute vérification de fait suit le protocole mnemolite-mem-first : Mnemolite d'abord, web après cache miss, write-back obligatoire.
- Les sources officielles sont une famille de traces parmi d'autres : ni socle de vérité, ni déchets à exclure (corruption_brainstorm_2.md §13).
- La conclusion graduée est la norme : on écrit ce qui est établi, corroboré, allégué, inféré, contredit, inconnu. Jamais « preuve » pour un indice isolé.
