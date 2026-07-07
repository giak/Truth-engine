# tools/ — Outils & Engines

Registre des outils réutilisables du projet Truth Engine.

## Structure

| Dossier | Fichiers | Contenu |
|---------|----------|---------|
| `engines/` | 7 | Moteurs de prompt (SUBLIMATOR, substack, tweet, controleur APEX, leonardo, glossaire) |
| `templates/` | 2 | Templates de prompt génériques (analyze-text, simple-prompt) |
| `scripts/` | 3 | Scripts utilitaires CLI (char-tool, char-counter, lint-article) |
| `tools/` (racine) | `audit_ric_mapping.py` | Audit reproductible dossiers RIC Saison 2 (mapping explicite + Phase 1 KISS v1.0 canonique) |

### `audit_ric_mapping.py`

Outil d'audit reproductible pour les dossiers `investigations/2026-07-XX-RIC/` :

- **Mapping explicite 42 entrées** sujet-canonique -> INVESTIGATION + quintessence. PAS de matching algorithmique (substring/regex) : chaque ligne est ecriture a la main, evitement du bug `cnr_1944_democratie_economique` (mauvais substring match dans audit precedent).
- **Validation Phase 1 KISS v1.0 canonique** (knowledge.md) : 0 em-dash (U+2014, octets `0xe2 0x80 0x94`) + >= 8 sections H2 numerotees `## 1.` a `## 9.` + marker Phase 1 KISS dans header (3 variantes regex acceptees).
- **4 modes CLI** : `list` (mapping 42/42) / `coverage` (couverture 1-a-1 avec anti-doublon) / `audit` (conformite Phase 1 KISS v1.0 canonique) / `full` (rapport complet).
- **Parametrable** via `-d PATH` pour reutilisation sur d'autres dossiers Saison 2.
- **LEGACY explicite** : `dossier_v38.md` declare HORS-CANONIQUE, exclus du check coverage.
- **Exit code** : 0 si 42/42 conformes, 1 sinon (integrable CI).

Usage :

```bash
python tools/audit_ric_mapping.py list
python tools/audit_ric_mapping.py coverage
python tools/audit_ric_mapping.py audit
python tools/audit_ric_mapping.py full
python tools/audit_ric_mapping.py -d investigations/2026-07-04-RIC audit
```

## Detail par dossier## Détail par dossier

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
