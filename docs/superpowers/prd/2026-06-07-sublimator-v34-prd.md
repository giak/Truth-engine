# PRD — SUBLIMATOR v34 « Léger »

**Date** : 2026-06-07
**Statut** : DRAFT 2 (révisé post-réduction Léger)
**Source** : PFD `docs/superpowers/pfd/2026-06-07-sublimator-v34-pfd.md` (DRAFT 2)
**Rôle** : Ce document spécifie le « comment » de chaque livrable v34 Léger. Deux modules Python mécaniques + un prompt système + le LLM hôte pilote.

---

## Table des matières

0. Préambule
1. Module `head_check.py` — vérification HTTP des URLs
2. Module `gates.py` — validation structurelle H0-H6
3. Prompt système — `tools/engines/sublimator/prompt-v34.md`
4. Formats YAML — quintessence, synthèse
5. Tests — 15 tests pour gates.py
6. Contrat LLM hôte — interface conversationnelle
7. Critères d'acceptation

---

## §0 Préambule

La réduction v34 Léger (juin 2026) a pivoté l'architecture. Le LLM hôte est le pilote unique : il lit les enquêtes, extrait les F###, interroge Mnemolite, produit les YAML, rédige l'article. Python est réduit à 2 modules mécaniques que le LLM hôte appelle comme des outils.

**Modules Python actifs :**
- `head_check.py` : 33 lignes, vérification HTTP des URLs + scoring glyphes
- `gates.py` : 152 lignes, validation structurelle H0-H6 des YAML

**Modules supprimés (Étape 1) :**
- `parse_atomic.py`, `extract_utile.py`, `curator.py`, `gate_g.py`, `orchestrator.py`, `_demo_end_to_end.py`, `_demo_sumer.py`, `_lancer_tout.py`

**Prompt système :**
- `tools/engines/sublimator/prompt-v34.md` : 200+ lignes, 3 phases, 14 LOIS, instructions Mnemolite, protocole V/M/R/E

---

## §1 Module `head_check.py` — vérification HTTP des URLs

### REQ-HEAD-001 : Interface

Fichier : `tools/engines/sublimator/extractors/head_check.py`

```python
import urllib.request
import urllib.error
from typing import Optional

def head_check(url: str, timeout: int = 10) -> Optional[int]:
    """
    Vérifie qu'une URL est vivante par requête HTTP HEAD.

    Args:
        url: URL à tester (doit commencer par http:// ou https://).
        timeout: timeout en secondes (défaut 10).

    Returns:
        Le code de statut HTTP (200, 301, 404, etc.) si la requête aboutit.
        None si l'URL est invalide, le host unreachable, ou timeout.
    """
```

### REQ-HEAD-002 : Scoring fiabilité

```python
def score_fiabilite(url: str, tier: int, timeout: int = 10) -> dict:
    """
    Attribue un glyphe de fiabilité à une URL.

    Args:
        url: URL à tester.
        tier: Niveau de la source (1 = primaire, 2+ = secondaire).
        timeout: timeout HTTP.

    Returns:
        dict avec les clés :
        - 'url': l'URL testée
        - 'status': le code HTTP (ou None)
        - 'tier': le tier fourni
        - 'glyphe': "✦" (tier1+200), "✧" (tier2++200), "⁅" (4xx/5xx/None), "❧" (pas d'URL)
    """
```

### REQ-HEAD-003 : Dépendances

Stdlib uniquement (`urllib.request`, `urllib.error`). Aucun package externe. Pas de `requests`.

### REQ-HEAD-004 : Utilisation par le LLM hôte

Le LLM hôte appelle `head_check(url)` via un appel shell ou outil. Exemple :

```
head_check("https://www.insee.fr/fr/statistiques/8375635") → 200
head_check("https://broken-link.example.com") → None
```

Le LLM hôte utilise le code de retour pour attribuer le glyphe dans le YAML de quintessence.

---

## §2 Module `gates.py` — validation structurelle H0-H6

### REQ-GATE-001 : Interface

Fichier : `tools/engines/sublimator/extractors/gates.py`

```python
def validate(yaml_path: str, yaml_type: str = "quintessence") -> tuple[bool, list[str]]:
    """
    Valide un fichier YAML (quintessence ou synthèse) contre les checks H0-H6.

    Args:
        yaml_path: Chemin vers le fichier YAML à valider.
        yaml_type: "quintessence" ou "synthese".

    Returns:
        (passed, messages) où passed est True si tous les checks passent,
        et messages liste les descriptions de chaque échec.
    """
```

Note : pas de GATE_G (complétude mécanique). Le LLM hôte compte ses F### lui-même et valide la complétude sémantiquement. Pas de paramètre `complexity`.

### REQ-GATE-002 : H0 — YAML parsable

Le fichier est parsable par `yaml.safe_load()`. Le root doit être un `dict`.

Message d'échec : `"H0: Fichier YAML invalide — {exception}"`

### REQ-GATE-003 : H1 — Sections obligatoires

**Quintessence** (12 clés) : `these_centrale`, `theses_implicites`, `faits_atomiques`, `acteurs`, `causalites`, `perspectives_dialectiques`, `limites`, `wolves`, `iceberg`, `chronologie`, `domaines`, `urls_prioritaires`.

**Synthèse** (8 clés) : `sujet_majoritaire`, `theses_cardinales`, `meta_observations`, `transversalites`, `cartes_positions`, `gaps`, `shadow_factor_global`, `mnemo_context`.

Message d'échec : `"H1: Section(s) manquante(s) — {liste}"`

### REQ-GATE-004 : H2 — Types valides

| Section | Type |
|---------|------|
| `these_centrale` | `str` non vide |
| `theses_implicites` | `list[str]` de longueur 3 |
| `faits_atomiques` | `list[dict]` non vide |
| `theses_cardinales` | `list[dict]` longueur 3-5 |
| `transversalites` | `list[dict]` non vide |
| `shadow_factor_global` | `int` ou `float` |
| `mnemo_context` | `dict` avec clé `searches` |

### REQ-GATE-005 : H3 — Glyphes valides

Chaque `faits_atomiques[].glyphe` est dans `{"✦", "✧", "⁅", "❧"}`. Le glyphe vide est rejeté.

Message d'échec : `"H3: Glyphe invalide pour '{id}' — '{glyphe}'"`

### REQ-GATE-006 : H4 — Identifiants uniques

Les `id` des `faits_atomiques` sont tous uniques.

Message d'échec : `"H4: F### dupliqué — '{id}'"`

### REQ-GATE-007 : H5 — Thèses justifiées

Chaque `theses_cardinales[].f_atomiques_justificatifs` a ≥ 3 éléments. Applicable uniquement si `yaml_type == "synthese"` (les quintessences n'ont pas de `theses_cardinales`).

Message d'échec : `"H5: Thèse '{titre}' a seulement {n} F### (min 3)"`

### REQ-GATE-008 : H6 — Références cohérentes

Tous les `f_atomiques_justificatifs` référencés dans `theses_cardinales` et `transversalites` existent dans `faits_atomiques`. Applicable uniquement si `yaml_type == "quintessence"` (la synthèse n'a pas de `faits_atomiques`).

Message d'échec : `"H6: F### '{id}' référencé mais absent de faits_atomiques"`

### REQ-GATE-009 : Exécution des checks

Ordre H0 → H6. Mode collecte : tous les checks sont exécutés même si un échoue. `passed` = True seulement si tous passent.

### REQ-GATE-010 : Utilisation par le LLM hôte

Le LLM hôte appelle `gates.validate(yaml_path, yaml_type)` après avoir écrit son YAML. Si FAIL, il corrige et re-valide avant de présenter le CP à l'humain.

---

## §3 Prompt système

### REQ-PROMPT-001 : Fichier

`tools/engines/sublimator/prompt-v34.md` — fichier Markdown versionné dans git. Prompt **standalone**, agnostique du LLM hôte (Claude, ChatGPT, Codebuff, Gemini…). L'utilisateur le copie-colle comme premier message d'une session fraîche. Aucun outil spécifique requis.

### REQ-PROMPT-002 : Contenu obligatoire

Le prompt système contient :

1. **Architecture** : les 4 briques, le LLM hôte comme pilote
2. **Phase 1 — Quintessence** : format YAML 12 sections, utilisation de `head_check(url)` et `gates.validate()`, protocole CP1
3. **Phase 2 — Synthèse** : format YAML 8 sections, Mnemolite obligatoire (`mnemo_context`), protocole CP2
4. **Phase 3 — Article** : rédaction (ROLE_TITRE_CREATEUR) puis auto-audit (ROLE_AUDITEUR_ARTICLE), 14 LOIS, 9 titres, protocole CP3
5. **14 LOIS** (L1 à L14) intégrales
6. **Protocole checkpoints** : V/M/R/E/AIDE, L14 (3 refus max, halte au 4e)
7. **Gestion Mnemolite** : `mnemo health` au démarrage, fallback markdown si DOWN
8. **Règles absolues** : zéro hallucination, zéro em-dash, zéro flagornerie, français soutenu

### REQ-PROMPT-003 : Instructions Mnemolite

- Phase 1 : `mnemo search` optionnel mais recommandé (mentionner les résultats dans `iceberg`)
- Phase 2 : `mnemo search` OBLIGATOIRE pour chaque thèse cardinale. Le champ `mnemo_context.searches` doit être rempli
- `mnemo health` au début de chaque session. Si DOWN → note `mnemolite_status: DOWN`, utilise le fallback markdown, ajoute un avertissement

---

## §4 Formats YAML

### REQ-YAML-001 : Quintessence (Phase 1 output)

```yaml
civ: "S"
complexity: "MEDIUM"
date_extraction: "2026-06-07"
enquete_source: "chemin/vers/enquete.md"

these_centrale: "En une phrase, la thèse démontrée."
theses_implicites:
  - "Thèse implicite 1"
  - "Thèse implicite 2"
  - "Thèse implicite 3"

faits_atomiques:
  - id: "F-S001"
    enonce: "Énoncé factuel précis, chiffré, daté."
    source_url: "https://..."
    source_section: "§3.2"
    head_status: 200
    tier: 1
    glyphe: "✦"

acteurs:
  - nom: "Nom complet"
    role: "Rôle"
    faits_lies: ["F-S001"]

causalites:
  - cause: "F-S001"
    effet: "F-S004"
    mecanisme: "Comment A cause B"

perspectives_dialectiques:
  - position: "Thèse"
    argument: "..."
  - position: "Antithèse"
    argument: "..."
  - position: "Synthèse"
    argument: "..."

limites:
  - "Ce que l'enquête ne couvre pas"

wolves:
  - nom: "Contradicteur"
    argument: "Ce qu'il dirait"
    reponse: "Notre réponse"

iceberg:
  - "Sujet immergé"
  - "Résultat Mnemolite: [si pertinent]"

chronologie:
  - date: "-3100"
    evenement: "Fait daté"
    source_fait: "F-S002"

domaines:
  - "Dette"
  - "Bureaucratie"

urls_prioritaires:
  - url: "https://..."
    description: "Pourquoi cette source est cruciale"
    head_status: 200

shadow_factor: 3.2
mnemo_queries:
  - query: "capture institutionnelle Sumer"
    results_count: 12
```

### REQ-YAML-002 : Synthèse (Phase 2 output)

```yaml
date_synthese: "2026-06-07"
complexity: "APEX"
n_enquetes: 10
civs_concernees: ["S", "R", "MA", "I", "C", "IN", "AM", "A", "HUB", "META"]
total_faits_atomiques: 212

sujet_majoritaire: "En une phrase, le sujet éclairé par les N enquêtes."

theses_cardinales:
  - titre: "THESE-001 : Titre"
    enonce: "Énoncé complet."
    position: "continuité"
    f_atomiques_justificatifs: ["F-R002", "F-MA001", "F-I007", "F-C001", "F-R006"]
    shadow: 2.5

meta_observations:
  - id: "OBS-001"
    enonce: "Pattern cross-fiche"
    fiches_concernees: ["R", "MA", "I", "C"]

transversalites:
  - id: "TR-001"
    concept: "Nom du concept"
    description: "..."
    fiches_concernees: ["S", "AM", "R"]
    faits_communs: ["F-S006", "F-AM006", "F-R003"]

cartes_positions:
  - fiche: "S"
    position: "continuité"
    justification: "..."

gaps:
  - "GAP-001 : Sujet jamais traité"

shadow_factor_global: 3.8

mnemo_context:
  searches:
    - query: "transmission droit romain Bologne"
      results: 8
      top_hits: ["memo-abc", "memo-def"]
  cross_series_detected: true
  cross_series_details: "..."
```

---

## §5 Tests

### REQ-TEST-001 : Tests gates.py (15 tests)

Fichier : `tests/extractors/test_gates.py`

| Test | Check | Description |
|------|-------|-------------|
| `test_h0_yaml_valide` | H0 | Fichier parsable → pass |
| `test_h0_yaml_invalide` | H0 | Fichier corrompu → fail |
| `test_h0_root_not_dict` | H0 | Root = liste → fail |
| `test_h1_quintessence_complete` | H1 | 12 clés → pass |
| `test_h1_quintessence_incomplete` | H1 | Clé manquante → fail |
| `test_h1_synthese_complete` | H1 | 8 clés → pass |
| `test_h2_type_invalide` | H2 | Mauvais type → fail |
| `test_h3_glyphe_valide` | H3 | Glyphe ✦ → pass |
| `test_h3_glyphe_invalide` | H3 | Glyphe "X" → fail |
| `test_h3_glyphe_vide` | H3 | Glyphe vide → fail |
| `test_h4_faits_uniques` | H4 | IDs uniques → pass |
| `test_h4_fait_duplique` | H4 | ID dupliqué → fail |
| `test_h5_these_sous_referencee` | H5 | Thèse avec 2 F### → fail |
| `test_h6_reference_orpheline` | H6 | F### absent → fail |
| `test_h6_noop_synthese` | H6 | H6 skip sur synthèse → pass |

**Total** : 15 tests. Lancement : `python3 -m pytest tests/extractors/test_gates.py -v`

### REQ-TEST-002 : Tests head_check.py

Pas de tests unitaires. Les appels HTTP réels sont testés manuellement en pilote (Étape 4).

---

## §6 Contrat LLM hôte — interface conversationnelle

### REQ-CONTRAT-001 : Protocole d'échange

1. **LLM hôte lit** l'enquête brute (fichier Markdown) ou les YAML de quintessence
2. **LLM hôte interroge** Mnemolite si pertinent
3. **LLM hôte produit** sa sortie (YAML ou Markdown)
4. **LLM hôte appelle** `head_check(url)` pour vérifier les URLs
5. **LLM hôte appelle** `gates.validate(yaml_path, yaml_type)` pour valider la structure
6. **LLM hôte corrige** si gates FAIL, puis présente le CP à l'humain
7. **Humain répond** V/M/R/E. Si R → re-génération. Si V → phase suivante

### REQ-CONTRAT-002 : Détection mode dégradé

Avant chaque phase, le LLM hôte exécute `mnemo health`. Si la réponse n'est pas « OK » :
- Note `mnemolite_status: DOWN` dans le YAML
- Utilise le fallback markdown local
- Ajoute un avertissement dans `limites`

### REQ-CONTRAT-003 : Gestion des erreurs

Si le LLM hôte produit un YAML mal formé (non parsable par `yaml.safe_load()`) :
- `gates.validate()` détecte l'erreur (H0 fail)
- Le LLM hôte corrige et re-valide avant de présenter le CP
- Le compteur de refus n'est PAS incrémenté (l'erreur est détectée avant le CP)

---

## §7 Critères d'acceptation

### 7.1 head_check.py

- [x] REQ-HEAD-001 à REQ-HEAD-003 implémentés
- [x] Stdlib uniquement (`urllib`)
- [x] Fonctionnel : `head_check("https://httpbin.org/status/200")` retourne 200

### 7.2 gates.py

- [x] REQ-GATE-001 à REQ-GATE-010 implémentés
- [x] 15 tests PASS dans `test_gates.py`
- [x] Pas de GATE_G, pas de paramètre `complexity`

### 7.3 Prompt système

- [x] REQ-PROMPT-001 à REQ-PROMPT-003 : fichier versionné + contenu obligatoire
- [x] 14 LOIS présentes
- [x] Instructions Mnemolite pour les 4 outils
- [x] Protocole V/M/R/E + L14
- [x] Usage documenté en en-tête (session dédiée, pas de chargement automatique)

### 7.4 YAML

- [x] REQ-YAML-001 : quintessence 12 sections (spécifié dans le prompt)
- [x] REQ-YAML-002 : synthèse 8 sections, mnemo_context obligatoire

### 7.5 Tests

- [x] 15 tests PASS
- [x] Couverture H0-H6 complète

### 7.6 Modules supprimés

- [x] Zéro fichier parse_atomic.py, extract_utile.py, curator.py, gate_g.py, orchestrator.py dans extractors/
- [x] Zéro test obsolète dans tests/extractors/
- [x] Zéro import de modules supprimés dans la codebase

### 7.7 Pilote (Étape 4)

- [ ] Run complet sur 3-10 enquêtes réelles
- [ ] 3 CPs validés par l'humain
- [ ] Article publiable, 100 % traçabilité
- [ ] Temps humain < 4h

---

*Fin du PRD Sublimator v34 Léger. Document DRAFT 2 (révisé post-réduction). Prochaine étape : Architecture détaillée recalibrée, puis Pilote (Étape 4).*
