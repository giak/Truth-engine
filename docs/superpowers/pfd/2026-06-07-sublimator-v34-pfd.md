# PFD — SUBLIMATOR v34 « Léger »

**Date** : 2026-06-07
**Statut** : DRAFT 2 (révisé post-réduction Léger)
**Source** : Vision `docs/superpowers/vision/2026-06-07-sublimator-vision.md` (DRAFT 3)
**Suivra** : PRD, Architecture, Pilote (Étape 4)
**Rôle** : Ce document décline la Vision en fondations concrètes pour l'architecture Léger : 2 modules Python mécaniques + 1 prompt système + LLM hôte pilote. Les Étapes 1 (réduction Python) et 2 (prompt système) sont livrées. Les Étapes 3 (mise à jour docs) et 4 (pilote) restent à faire.

---

## Table des matières

0. Préambule et traçabilité
1. Périmètre IN
2. Non-périmètre OUT
3. Contraintes
4. Architecture cible (modèle Léger)
5. Jalons ordonnés (révisés)
6. Risques et mitigations
7. Critères d'acceptation

---

## §0 Préambule et traçabilité

La Vision Sublimator (DRAFT 3, 2026-06-07) définit l'idéal : 4 briques (Python, Mnemolite, LLM hôte, Humain), 3 phases (per-enquête, cross-enquête, article), 3 checkpoints humains bloquants.

Ce PFD a été révisé le 2026-06-07 pour refléter l'architecture **Léger** adoptée après la question de fond : « a-t-on besoin de tout ce Python ? » La réponse : non. Le LLM hôte est le pilote. Python est réduit à 2 modules mécaniques (head_check + gates). Le prompt système vit dans un fichier Markdown versionné, pas dans des constantes Python.

Les Étapes 1 (réduction Python : 778 → 185 lignes) et 2 (prompt système unique) sont **livrées**. L'Étape 3 (mise à jour des 4 documents) est en cours. L'Étape 4 (pilote grandeur nature) reste à faire.

---

## §1 Périmètre IN

Ce que v34 livre. Chaque élément est factuel, vérifiable, et correspond à un besoin documenté dans la Vision.

### 1.1 Intégration Mnemolite MCP

**Vision** : §8 Brique 2.

Le LLM hôte appelle les 4 outils MCP de Mnemolite directement pendant la conversation :

- `mnemo search "<requête>"` : recherche vectorielle hybride
- `mnemo projects` : liste les projets indexés
- `mnemo read <uuid>` : lit une mémoire par identifiant
- `mnemo health` : vérifie l'état du serveur

**Aucun wrapper Python.** Le LLM hôte est le pilote de la session. Les fichiers markdown locaux restent le fallback.

**Statut** : ✅ Intégré dans le prompt système (`tools/engines/sublimator/prompt-v34.md`).

### 1.2 Modules Python mécaniques (filet minimal)

**Vision** : §8 Brique 1.

Deux modules uniquement, 185 lignes au total :

- **`head_check.py`** (33 lignes) : fonction `head_check(url)` → status HTTP. Fonction `score_fiabilite(url, tier)` → glyphe (✦✧⁅❧). Stdlib uniquement (`urllib`).
- **`gates.py`** (152 lignes) : fonction `validate(yaml_path, yaml_type)` → `(bool, list[str])`. 7 checks H0-H6. Pas de GATE_G (le LLM hôte compte ses F### lui-même).

**Statut** : ✅ Livré (Étape 1). 15 tests PASS.

### 1.3 Prompt système unique

**Vision** : §8 Brique 3.

Un seul fichier `tools/engines/sublimator/prompt-v34.md` (200+ lignes) contient :
- Les 3 phases et leurs formats de sortie
- Les instructions Mnemolite (quand et comment utiliser les 4 outils)
- Les 14 LOIS
- Le protocole V/M/R/E + AIDE
- La règle L14 (3 refus max, halte au 4e)

Pas de `prompts.py`. Le prompt est un fichier Markdown versionné dans git, référencé dans `config/kilo.json`.

**Statut** : ✅ Livré (Étape 2).

### 1.4 Pipeline conversation-bound 3 phases avec checkpoints humains

**Vision** : §3, §5 Pilier 3.

Le LLM hôte pilote les 3 phases dans la conversation. Aucun orchestrateur Python ne coordonne le flux. Le LLM hôte :
- Lit chaque enquête et produit sa quintessence (Phase 1)
- Appelle `head_check(url)` pour vérifier les URLs
- Appelle `gates.validate()` pour valider ses sorties YAML
- S'arrête à chaque CP et attend V/M/R/E
- Passe à la phase suivante uniquement après validation humaine

**Statut** : 🔲 Spécifié dans le prompt système. À tester en pilote (Étape 4).

### 1.5 Article final 6 000-8 000 mots, 14 LOIS, 9 titres

**Vision** : §1, §5 Pilier 3.

Identique à la spec initiale : traçabilité complète, glyphes visibles, zéro em-dash, section Sources. Le LLM hôte rédige puis s'auto-audite (deux passes distinctes).

**Statut** : 🔲 À tester en pilote (Étape 4).

---

## §2 Non-périmètre OUT

Ce que v34 ne fait PAS. Ces éléments sont explicitement exclus pour borner le scope et éviter la dérive. Certains sont des anti-patterns rejetés par la Vision (§6), d'autres sont des fonctionnalités légitimes mais différées à une version ultérieure.

### 2.1 Pipeline autonome (pas de publication automatique)

**Vision** : §6.5 « Pas un autopilot ».

v34 ne publie jamais sans validation humaine. Les 3 checkpoints sont strictement bloquants. Le script `orchestrator.py` s'arrête à chaque CP et attend l'input humain. Aucun flag `--auto-publish`, aucun mode « headless ».

### 2.2 API LLM externe via Python

**Vision** : §7 « Architecture réelle ».

Aucun module Python n'appelle OpenAI, Anthropic, ou autre provider. La fonction `call_llm()` qui n'a jamais existé ne sera pas créée. Le LLM hôte (opencode/Codebuff) est l'agent sémantique. Les prompts sont générés par Python, lus par le LLM hôte dans la conversation, et les outputs sont parsés par Python.

### 2.3 Wrapper Python pour Mnemolite

**Vision** : §8 Brique 1, §8 Brique 2.

Pas de `mnemolite_bridge.py`. Pas de `mnemo_client.py`. Pas de SDK Python enveloppant l'API REST ou le MCP Server de Mnemolite. Le LLM hôte interagit directement avec le MCP Server. Python n'a pas besoin de connaître Mnemolite.

### 2.4 Interface graphique

**Vision** : §8 Brique 4 (l'humain est l'interface).

Pas de dashboard, pas de Vue 3, pas de visualisation nodale des F###. Le journaliste interagit avec le LLM hôte dans la conversation Codebuff. Les checkpoints sont des questions textuelles. L'output est un fichier Markdown.

### 2.5 Multi-journaliste / collaboratif

Un seul journaliste par session. Pas de merge de checkpoints, pas de workflow de revue par les pairs, pas de commentaires inline. La signature est individuelle.

### 2.6 Optimisation SEO ou métriques d'engagement

**Vision** : §6.4 « Pas un outil marketing ».

Aucun keyword stuffing, aucune méta-description automatique, aucun A/B testing de titres, aucun suivi du temps de lecture. La seule métrique est la défendabilité.

### 2.7 Support de nouvelles langues

Français uniquement. La Vision et les 14 LOIS sont calibrées pour le français soutenu. L'extension à d'autres langues est un problème architectural distinct, pas un flag de configuration.

---

## §3 Contraintes

Ce qui limite v34 Léger.

### 3.1 Contraintes techniques

| Contrainte | Détail | Source |
|-----------|--------|--------|
| Python 3.11+ | Version installée 3.12.3. Les 2 modules utilisent le typage moderne et les f-strings. | Code existant |
| Zéro nouveau package | Les dépendances actuelles (pyyaml, pytest) suffisent. `head_check.py` utilise `urllib` (stdlib). | Audit 2026-06-07 |
| Mnemolite doit être UP | Le MCP Server (port 8002) doit être accessible. Fallback markdown local si DOWN. | Vision §8 Brique 2 |
| 15 tests existants doivent rester PASS | `test_gates.py` uniquement. Aucun autre module Python testé. | `pytest tests/extractors/ -v` |
| Prompt système versionné | `tools/engines/sublimator/prompt-v34.md` dans git. Prompt standalone, agnostique du LLM hôte. | Étape 2 |

### 3.2 Contraintes opérationnelles

| Contrainte | Détail | Source |
|-----------|--------|--------|
| Conversation-bound | Le LLM hôte pilote tout dans la conversation. Pas de sous-processus, pas de pipeline autonome. | Vision §7 |
| Pas d'état persistant entre sessions | L'état est dans les fichiers YAML produits (quintessences, synthèse). Le LLM hôte les relit au début de chaque session. | Architecture Léger |
| Pas d'orchestrateur Python | `orchestrator.py` a été supprimé (Étape 1). Le LLM hôte est l'orchestrateur. | Étape 1 |

### 3.3 Contraintes humaines

| Contrainte | Détail | Source |
|-----------|--------|--------|
| 1 journaliste | Une seule personne signe l'article. | Vision §4 |
| ≤ 4 heures de jugement | Budget temps cible. Inclut les 3 CPs + 30 min de relecture. | Vision §1 |
| 3 refus max par CP (L14) | Halte au 4e refus avec bilan. | Vision §5 Pilier 3 |
| Publication toujours manuelle | Copier-coller sur Substack. Aucun déploiement automatique. | Vision §6.5 |

---

## §4 Architecture cible (modèle Léger)

Comment les 4 briques s'articulent. Le LLM hôte est le pilote unique. Python n'est plus qu'un filet mécanique appelé par le LLM hôte.

### 4.1 Diagramme de séquence (textuel)

```
Phase 1 (1 enquête)
  LLM hôte: lit l'enquête brute (Markdown)
  LLM hôte: interroge Mnemolite si pertinent (mnemo search)
  LLM hôte: extrait les F###, produit 12 sections de quintessence
  LLM hôte: appelle head_check(url) pour chaque URL source
  LLM hôte: appelle gates.validate("quintessence.yaml", "quintessence")
  LLM hôte: corrige si gates FAIL
  HUMAIN: CP1 (V/M/R/E)

Phase 2 (N enquêtes)
  LLM hôte: charge N quintessences YAML
  LLM hôte: interroge Mnemolite pour chaque thèse (OBLIGATOIRE)
  LLM hôte: détecte transversalités, formule 5 thèses cardinales
  LLM hôte: produit 8 sections de synthese.yaml
  LLM hôte: appelle gates.validate("synthese.yaml", "synthese")
  HUMAIN: CP2 (V/M/R/E)

Phase 3 (1 article)
  LLM hôte: rédige draft 6000-8000 mots (ROLE_TITRE_CREATEUR, 14 LOIS)
  LLM hôte: s'auto-audite (ROLE_AUDITEUR_ARTICLE, 4 types de failles)
  LLM hôte: appelle head_check(url) pour chaque URL citée
  LLM hôte: vérifie 0 em-dash, 0 ID interne, 0 mandat périmé
  HUMAIN: CP3 (V/M/R/E), relecture 30 min, publication manuelle
```

### 4.2 Contrats d'interface entre briques

**LLM hôte → Python (head_check)** : le LLM hôte appelle `head_check(url)` via un appel shell ou outil. Python retourne le status code HTTP. Le LLM hôte attribue le glyphe.

**LLM hôte → Python (gates)** : le LLM hôte appelle `gates.validate(yaml_path, yaml_type)` après avoir écrit son YAML. Python retourne `(passed, messages)`. Le LLM hôte corrige si FAIL.

**LLM hôte → Mnemolite** : appels MCP directs (search, projects, read, health).

**Humain → LLM hôte** : V/M/R/E à chaque CP, dans la conversation.

### 4.3 Fichiers produits

```
  prompt-v34.md                                  ← Prompt système (la spec vivante, standalone)

investigations/<sujet>/_quintessence/
  {CIV}_quintessence.yaml                  ← Phase 1 (une par enquête)

investigations/<sujet>/_synthese/
  synthese.yaml                             ← Phase 2

articles/
  <date>_<sujet>_ARTICLE.md                ← Phase 3

tools/engines/sublimator/extractors/
  head_check.py                             ← HEAD-check URLs + glyphes
  gates.py                                  ← Validation structurelle H0-H6

tests/extractors/
  test_gates.py                             ← 15 tests
```

---

## 5 Jalons ordonnes (revises post-reduction Leger)

Les Etapes 1 et 2 sont livrees. Les Etapes 3 et 4 restent.

### Jalon 1: Reduction Python → 2 modules [LIVRE]

**Depend de** : rien (nettoyage de l'existant).
**Livrable** : suppression de parse_atomic.py, extract_utile.py, curator.py, gate_g.py, orchestrator.py, _demo_*, _lancer_tout.py. Creation de head_check.py (HEAD-check URLs, 33 lignes) et gates.py (H0-H6 uniquement, 152 lignes).
**Test** : `pytest tests/extractors/ -v` → 15 tests PASS (test_gates.py uniquement).
**Statut** : ✅ Livre le 2026-06-07.

### Jalon 2: Prompt systeme unique [LIVRE]

**Depend de** : Jalon 1 (le prompt reference head_check et gates).
**Livrable** : `tools/engines/sublimator/prompt-v34.md` (200+ lignes) : 3 phases, instructions Mnemolite, 14 LOIS, protocole V/M/R/E, reference a head_check() et gates.validate(). Prompt standalone, agnostique du LLM hôte.
**Test** : Le prompt contient les 14 LOIS, les 4 outils Mnemolite, la regle L14 (3 refus max).
**Statut** : ✅ Livre le 2026-06-07.

### Jalon 3: Mise a jour de la documentation [LIVRE]

**Depend de** : Jalons 1-2 (l'architecture a change).
**Livrable** : Vision, PFD, PRD, Architecture recalibres sur le modele Leger : 2 modules Python, LLM hote pilote, prompt systeme unique, 15 tests.
**Test** : Aucun des 4 documents ne mentionne parse_atomic, extract_utile, curator, gate_g, orchestrator comme modules existants. Aucun ne mentionne 26 ou 37 tests (le chiffre correct est 15). Aucun ne mentionne prompts.py.
**Statut** : ✅ Livre le 2026-06-07 (Etape 3).

### Jalon 4: Pilote v34 Leger [A FAIRE]

**Depend de** : Jalons 1-3.
**Livrable** : Un run complet sur 3-10 enquetes reelles avec le prompt systeme + Mnemolite + head_check + gates. Le LLM hote pilote les 3 phases. L'humain valide aux 3 CPs. L'article est publiable.
**Test** : Article 6000-8000 mots, 100% tracabilite, 14 LOIS respectees, URLs verifiees, 3 CPs valides. Temps humain < 4h.
**Statut** : 🔲 A faire (Etape 4).

---

## 6 Risques et mitigations

Chaque risque a une probabilite estimee (haute/moyenne/basse) et une mitigation concrete, pas un voeu pieux.

### Risque A: Le LLM hote ignore Mnemolite [PROBABILITE: HAUTE]

**Description** : Le LLM hote, par paresse ou habitude, ne declenche pas les appels MCP.

**Mitigation** :
1. Le prompt systeme contient l'instruction explicite : « Tu DOIS utiliser mnemo search avant de formuler une these ou une transversalite. »
2. Le prompt de Phase 2 inclut un champ mnemo_context obligatoire.
3. gates.py (H1) verifie la presence de ce champ dans la synthese YAML.

### Risque B: Saturation de la fenetre de contexte [PROBABILITE: MOYENNE]

**Mitigation** :
1. Le LLM hote travaille enquete par enquete, jamais sur le corpus entier d'un coup.
2. Mnemolite stocke le texte integral ; le LLM hote interroge a la demande.
3. La Phase 2 travaille sur les quintessences YAML (quelques centaines de lignes), pas sur les enquetes brutes.

### Risque C: Hallucination en Phase 3 [PROBABILITE: MOYENNE]

**Mitigation** :
1. Le ROLE_AUDITEUR_ARTICLE verifie la coherence factuelle avant le CP3.
2. Le journaliste, au CP3, verifie un echantillon aleatoire de 5 F###.
3. head_check(url) verifie chaque URL citee.

### Risque D: Boucle de validation infinie [PROBABILITE: BASSE]

**Mitigation** : L14 dans le prompt systeme : 3 refus max par CP. Au 4e, halte avec bilan.

### Risque E: Mnemolite DOWN [PROBABILITE: BASSE]

**Mitigation** : Le LLM hote verifie mnemo health. Si DOWN, fallback markdown local + avertissement dans l'article.

---

## 7 Criteres d'acceptation

Comment on valide que v34 Leger est livree. Chaque critere est binaire (PASS/FAIL).

### 7.1 Tests

- [x] `pytest tests/extractors/ -v` retourne 15 tests PASS (test_gates.py).
- [x] Aucun import de llm_lecteur, llm_curator, llm_verifier dans la codebase.
- [x] Aucun module parse_atomic, extract_utile, curator, gate_g, orchestrator dans extractors/.
- [x] Aucune occurrence de NotImplementedError, call_llm, LLM_API_KEY dans le code.

### 7.2 Mnemolite

- [x] Le prompt systeme contient les instructions pour les 4 outils MCP.
- [ ] Le LLM hote, sur une enquete test, appelle mnemo search sans relance explicite. (→ Pilote Etape 4)
- [ ] Si Mnemolite est DOWN, le pipeline continue en mode degrade avec avertissement. (→ Pilote Etape 4)

### 7.3 Pipeline

- [x] Les 3 CPs sont specifies dans le prompt systeme (V/M/R/E + AIDE).
- [x] L14 est specifiee: 3 refus max par CP, halte au 4e avec bilan.
- [ ] Les 3 phases s'enchainent dans la conversation sans intervention Python. (→ Pilote Etape 4)

### 7.4 Article final

- [ ] L'article final contient 6000-8000 mots. (→ Pilote Etape 4)
- [ ] 14 LOIS respectees. (→ Pilote Etape 4)
- [x] 9 propositions de titre specifiees dans le prompt.
- [x] head_check.py fonctionnel (HEAD HTTP → status code).
- [x] gates.py fonctionnel (H0-H6, 15 tests PASS).

### 7.5 Temps humain

- [ ] Le temps total de jugement humain est inferieur a 4h pour un run de 10 enquetes. (→ Pilote Etape 4)

---

*Fin du PFD Sublimator v34 Leger. Document DRAFT 2 (revise post-reduction). Prochaine etape : PRD puis Architecture recalibres.*
