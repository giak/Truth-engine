# Spec v33.3 — DELTA depuis v33.2 (Agent Syntheseur LLM hôte)

**Date :** 2026-06-06 | **Statut :** DRAFT | **Cible :** SUBLIMATOR v33.3
**Base :** `tools/engines/sublimator/2026-06-06_spec_v33.2.md` (1493 lignes, 21 sections)
**Design :** `docs/superpowers/specs/2026-06-06-syntheur-aggregator-v33.3-design.md` (337 lignes, 14 sections)

## §0 RÉSUMÉ EXÉCUTIF

v33.3 ajoute l'**Agent F (Syntheseur)** = un **PROMPT structuré** + un **orchestrateur thin** + un **validateur mécanique GATE_H**. **Aucun algorithme de détection en Python** : tout le travail de détection (sujet principal, transversalités, thèses, méta-observations, gaps) est fait par le **LLM hôte (opencode)** qui reçoit le prompt et retourne un YAML conforme. Python ne fait que I/O + validation structurelle. Cette approche respecte le design §5 « pas de mécanique » et le principe « LLM hôte détecte ce qui émerge ».

## §0.1 CHANGELOG v33.2 → v33.3

| Type | Section | Contenu |
|------|---------|---------|
| AJOUT | §X.9 | Agent F (Syntheseur) — prompt + orchestrateur thin |
| AJOUT | §Y | GATE_H (7 checks structurels, pas de détection) |
| EXPANSION | §W.13 | synthese.yaml (de 2 lignes → spec complète) |
| INCHANGÉ | §1-§9, §X.1-§X.8, §W.1-§W.12 | v33.2 intact |

## §X.9 AGENT F — PROMPT + ORCHESTRATEUR

### X.9.1 Principe fondamental

**Le LLM hôte fait TOUT le travail de détection.** Python ne fait que :
1. Lire N fichiers quintessence YAML
2. Construire le `user_prompt` (insertion des données)
3. Invoquer `call_llm(system_prompt, user_prompt)` — c'est le LLM hôte
4. Recevoir la réponse YAML du LLM
5. Valider structurellement contre GATE_H (7 checks)
6. Écrire `synthese.yaml` + `synthese_human_review.md`

### X.9.2 Architecture

```
INPUT: N quintessences YAML (v33.1 ou v33.2 schema)
   ↓
[ORCHESTRATEUR PYTHON — thin wrapper]
   1. Charge N YAML
   2. Construit user_prompt = (contexte + N résumés + instructions output YAML)
   3. Appelle call_llm(system_prompt, user_prompt)
   ↓
[LLM HÔTE — opencode = moi]
   4. Lit le prompt
   5. Détecte sujet_majoritaire (chaine §2.1 du design)
   6. Classifie fiches (principales vs annexes §2.2)
   7. Pour chaque fiche, résume (3-5K, working memory)
   8. Cross-corrèle : acteurs, domaines, causalités, thèses, shadows
   9. Détecte transversalités (≥K fiches)
   10. Brainstorm N_theses cardinales candidates
   11. Mappe F### → thèses
   12. Identifie gaps
   13. Méta-observations
   14. Produit YAML 8 sections
   ↓
[ORCHESTRATEUR PYTHON — thin wrapper]
   15. Parse YAML
   16. Exécute 7 GATE_H (validation structurelle)
   17. Si tout passe : écrit synthese.yaml + synthese_human_review.md
   18. Si fail : log erreurs, return code 1 ou 3
```

### X.9.3 SYSTEM PROMPT (constante Python)

Fichier : `tools/engines/sublimator/extractors/syntheur_prompt.py`

```python
SYNTHEUR_SYSTEM_PROMPT = """Tu es l'Agent F (Syntheseur) de SUBLIMATOR v33.3.

MISSION : Recevoir N quintessences YAML et produire 1 synthese.yaml
contenant 8 sections : meta, transversalites, theses_cardinales,
meta_observations, gaps, ce_qui_tient, ce_qui_tombe, erreurs_detectees.

PRINCIPE : Tu fais TOUT le travail de detection (sujet, transversalites,
theses, meta-observations, gaps). Le code Python ne fait que valider
la structure de ton output.

PROCESS OBLIGATOIRE (10 etapes) :

1. LIS N QUINTESSENCES : charge les N fichiers YAML fournis dans le user_prompt.

2. DETECTE SUJET PRINCIPAL via chaine multi-source §2.1 du design v33.3 :
   - Priorite 1 : titre H1 de chaque fiche
   - Priorite 2 : section §1 RESUME EXECUTIF (si presente)
   - Priorite 3 : meta block (Complexite, Date, etc.)
   - Priorite 4 : premier paragraphe substantiel
   - Priorite 5 : filename (kebab-case : YYYY-MM-DD_HH-MM_sujet_TYPE.md)
   - Priorite 6 : headings ## §N
   - Si aucun mot-cle partage par >=50% des fiches -> GATE_H0 (orthogonalite)

3. CLASSIFIE CHAQUE FICHE (3 criteres §2.2 du design) :
   - shadow_factor > 3.0
   - complexity == "APEX"
   - these_centrale contient marqueur opposition
     ("ne...pas", "contredit", "limite", "biais", "recalcul", "audit",
      "refut", "manqu", "absent", "autops")
   - Score 0-1 : principale
   - Score 2 : annexe-complementaire
   - Score 3 : annexe-refutative

4. RESUME chaque fiche en 3-5K chars (working memory) :
   - these_centrale (1 phrase)
   - 3 theses_implicites cles
   - 5-10 F### les plus significatifs
   - 3-5 acteurs majeurs
   - shadow_factor
   - statut (principale / annexe-refutative / annexe-complementaire)

5. CROSS-CORRELE les resumes : acteurs recurrents, domaines partages,
   causalites similaires, theses convergentes/opposees, correlations
   numeriques (shadows vs autres variables).

6. DETECTE TRANSVERSALITES : concepts, acteurs, causalites, theses,
   ou faits presents dans >=K fiches (K fourni en parametre).
   Chaque transversalite : (id TR-NNN, label, type, fiches_concernees,
   f_atomiques, force en %, glyphe agrege pire).

7. BRAINSTORM N_THESES CARDINALES CANDIDATES (N_theses fourni) :
   - position ∈ {continuite, rupture, exception}
   - Pour chaque these : (id THESE-NNN, label, theses_implicites_alignees,
     f_atomiques_justificatifs >=3, fiches_soutien, fiches_opposition,
     shadow_factor median, glyphe_min)
   - Couverture obligatoire : au moins 1 continuite, 1 rupture, 1 exception
     (si N_theses >= 3)

8. IDENTIFIE GAPS : F### qui ne sont dans aucune transversalite ni these.

9. PRODUIS 1+ META-OBSERVATIONS : patterns cross-fiche
   (correlations numeriques, asymetries, distributions inhabituelles).

10. EVALUE ce_qui_tient et ce_qui_tombe de l'hypothese initiale.

OUTPUT : YAML strictement conforme au schema §W.13 (8 sections).
Commence par `synthese:` (indentation 0). Pas de commentaire.
Tous les F### cites doivent exister dans les quintessences fournies.
Tous les glyphes (X/X/X/X) sont obligatoires pour chaque F###.

GATE_H (7 checks structurels executes par Python sur ton output) :
- H0 : orthogonalite detectee -> sujet_majoritaire == "ORTHOGONALITE_DETECTEE"
- H1 : si N>=K, transversalites doit avoir >=1 entree
- H2 : chaque these_cardinale doit avoir >=3 f_atomiques_justificatifs
- H3 : tout F### doit avoir un glyphe (X/X/X/X) parmi {X, X, X, X}
- H4 : pas de circularite (META n'auto-valide pas META, A n'auto-valide pas A)
- H5 : meta_observations doit avoir >=1 entree
- H6 : shadow_factor_agregé doit etre >=1.0 et reporte par chaque these

Tu DOIS produire un YAML qui passe les 7 GATE_H.
Si orthogonalite, ecris sujet_majoritaire: ORTHOGONALITE_DETECTEE
et les autres sections peuvent etre vides.
"""
```

### X.9.4 USER PROMPT (construit dynamiquement)

Format :
```
[CONtexte]
Tu reçois N={N} quintessences.
K (seuil transversalite) = {K}
N_theses (cardinales) = {N_theses}
complexity = {complexity}

[QUINTESSENCE 1/{N}]
{contenu YAML 1}

[QUINTESSENCE 2/{N}]
{contenu YAML 2}

...

[QUINTESSENCE N/{N}]
{contenu YAML N}

[INSTRUCTIONS]
Applique le process 10 etapes de ton system_prompt.
Produis le YAML synthese conforme au schema §W.13.
Respecte strictement les 7 GATE_H.
```

### X.9.5 ORCHESTRATEUR PYTHON

Fichier : `tools/engines/sublimator/extractors/syntheur_orchestrator.py`

```python
def run_synthese(
    quint_files: list[str],
    k: int = 3,
    n_theses: int = 3,
    complexity: str = "MEDIUM",
    output_dir: str = ".",
) -> dict:
    """Orchestrateur thin de l'Agent F.
    
    Returns: {
        "exit_code": 0|1|3,
        "synthese_path": str|None,
        "human_review_path": str|None,
        "system_prompt": str,
        "user_prompt": str,
        "llm_output": str,
        "synthese_yaml": dict|None,
        "gate_h_results": list[(check_id, passed, message)],
        "erreurs": list[str],
    }
    """
```

**Étapes :**
1. Charger N quintessences YAML (try/except par fichier)
2. Construire user_prompt (insertion des N YAML)
3. Appeler `call_llm(SYNTHEUR_SYSTEM_PROMPT, user_prompt)` — lève NotImplementedError tant que LLM_API_KEY n'est pas défini (= le LLM hôte opencode gère)
4. Recevoir YAML du LLM
5. Parser YAML
6. Exécuter 7 GATE_H (cf. §Y)
7. Si exit_code == 0 : écrire synthese.yaml + synthese_human_review.md
8. Retourner dict résultat

## §Y GATE_H — 7 CHECKS STRUCTURELS (MÉCANIQUE)

**Rôle :** valider la STRUCTURE du YAML produit par le LLM hôte. **Pas de validation de contenu** (c'est le travail du LLM hôte).

| ID | Check | Type | Code fail |
|----|-------|------|-----------|
| H0 | `meta.sujet_principal` existe et != "ORTHOGONALITE_DETECTEE" si N≥2 et convergence | Présence + string | 3 |
| H1 | `len(transversalites) >= 1` si N>=K | Count | 1 |
| H2 | Pour chaque these_cardinale : `len(f_atomiques_justificatifs) >= 3` | Count par item | 1 |
| H3 | Pour chaque F### cité : `glyphe in {"X","X","X","X"}` | Regex/format | 1 |
| H4 | Pour chaque F### cité : `fiches_soutien` ne contient pas la fiche source si elle-même META ou audit | Set logic | 1 |
| H5 | `len(meta_observations) >= 1` | Count | 1 |
| H6 | `meta.shadow_factor_agregé >= 1.0` ET chaque these a `shadow_factor >= 1.0` | Numeric | 1 |

**Implémentation :** 7 fonctions dans `gate_h.py`, retourne `(passed: bool, message: str)`. Le orchestrateur collecte les (check_id, passed, message) et halt si l'un fail.

## §W.13 SYNTHESE.YAML (8 SECTIONS — EXPANDED)

Cf. §6 du design doc (YAML complet avec meta, transversalites, theses_cardinales, meta_observations, gaps, ce_qui_tient, ce_qui_tombe, erreurs_detectees).

### W.13.1 Cibles par tier (inchangé du design)

| Tier | Transversalités | Thèses | Méta-obs | F### cités | URLs citées |
|------|----------------|--------|----------|------------|-------------|
| SIMPLE | 1-2 | 1 | 1 | 5-10 | 3-5 |
| MEDIUM | 3-5 | 2 | 2 | 15-25 | 8-12 |
| COMPLEX | 6-9 | 3 | 3 | 30-50 | 15-25 |
| APEX | 10+ | 5 | 5 | 50-80 | 25-40 |

### W.13.2 synthese_human_review.md (1 page, max 2000 chars)

Résumé pour arbitrage humain :
- Sujet principal (1 phrase)
- Top 3 transversalités (1 ligne chacune)
- Top 3 thèses cardinales (1 ligne chacune)
- Top 3 méta-observations (1 ligne chacune)
- Verdict GATE_H (PASS/FAIL par check)
- Top 5 F### justificatifs (avec source)
- Top 3 gaps

## §MIGRATION v33.2 → v33.3

**Aucun fichier v33.2 n'est modifié.** v33.3 ajoute :
- `syntheur_prompt.py` (constante string system_prompt)
- `syntheur_orchestrator.py` (thin wrapper, ~80 lignes)
- `gate_h.py` (7 fonctions de validation structurelle, ~80 lignes)
- `tests/extractors/test_syntheur_prompt.py` (le prompt contient tout)
- `tests/extractors/test_syntheur_orchestrator.py` (E2E mock)
- `tests/extractors/test_gate_h.py` (7 tests, 1 par check)
- `tests/extractors/fixtures/` (mocks LLM output YAML)
- `tools/engines/sublimator/2026-06-06_guide_humain_v33.3.md` (ajout §17)

**Rétrocompatibilité :** Toutes les quintessences v33.1/v33.2 sont acceptées. Aucune migration de données.

## §RÉFÉRENCES

- Design v33.3 : `docs/superpowers/specs/2026-06-06-syntheur-aggregator-v33.3-design.md`
- Spec v33.2 : `tools/engines/sublimator/2026-06-06_spec_v33.2.md` (base inchangée)
- 10 quintessences pilote : `investigations/2026-06-03_sumer_article/_quintessence/`
- Pilote brainstorm 2026-06-06 : 6 transversalités + 3 thèses détectées par LLM hôte
- Convention `call_llm` v33.2 : lève NotImplementedError tant que LLM_API_KEY indéfini (= LLM hôte opencode prend le relais)
