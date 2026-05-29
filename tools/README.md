# tools/ — Outils & Engines

Registre des outils réutilisables du projet Truth Engine.

## Structure

| Dossier | Fichiers | Contenu |
|---------|----------|---------|
| `engines/` | 7 | Moteurs de prompt (SUBLIMATOR, substack, tweet, controleur APEX, leonardo, glossaire) |
| `templates/` | 2 | Templates de prompt génériques (analyze-text, simple-prompt) |
| `scripts/` | 3 | Scripts utilitaires CLI (char-tool, char-counter, lint-article) |

## Détail par dossier

### engines/
Engines principaux du système de prompt. Chaque fichier est un système complet, autonome et copiable.

- `SUBLIMATOR_v28.0.md` — Engine central d'investigation
- `substack-engine-v2.0.md` — Moteur de rédaction Substack
- `substack-writer-v4.0.md` — Writer O.S. pour articles longs
- `tweet-engine-v4.0.md` — Moteur de génération de tweets viraux
- `CONTROLEUR_APEX_v2.1.md` — Protocole d'audit systématique
- `promptsmith-leonardo-v4.md` — Engine de génération visuelle
- `glossaire-anglicismes.md` — Glossaire anti-anglicismes (référence persistée)

### templates/
Templates réutilisables, indépendants de tout sujet spécifique.

- `analyze-text.md` — Template d'analyse de texte + enquête
- `simple-prompt.md` — Template minimaliste

### scripts/
Utilitaires CLI pour les tâches courantes.

- `char-tool.sh` — Comptage et troncature de tweets
- `char_counter.py` — Compteur de caractères (version Python)
- `lint-article.sh` — Linting d'articles contre les LOIS SUBLIMATOR
