# Design v33.3 — Agent Syntheseur (Agrégation N fiches)

**Date :** 2026-06-06 | **Auteur :** Truth Engine v33.3 | **Statut :** DRAFT (self-review pending) | **Cible :** SUBLIMATOR v33.3

## §0 RÉSUMÉ EXÉCUTIF

L'agent **Syntheseur (Agent F)** est la 6ème étape du pipeline SUBLIMATOR. Il agrège N quintessences (N=2 à 20+) en une **fiche synthèse** contenant : transversalités (concepts partagés dans ≥K fiches), thèses cardinales candidates (3-5), méta-observations, gaps. Purement **LLM hôte** (pas de Python pré-processing, pas d'embeddings). Le sujet principal est détecté depuis l'**agrégat** des N fiches via une chaîne multi-source (titre H1 → §1 résumé exécutif → meta block → premier paragraphe → filename → headings). Généricité absolue : fonctionne pour tout sujet (dette antique, climat, immigration, finance, etc.) et tout format d'enquête (avec ou sans §1, avec ou sans meta block, etc.).

## §1 CONTEXTE & MOTIVATION

### 1.1 État actuel (post-v33.2)
- 10/10 fiches quintessence commitées (S, R, C, MA, I, IN, AM, A, HUB, META)
- 212 F###, 109 acteurs, 106 URLs, 50 causalités, 159 chronologies
- Spec v33.2 §W.13 « Agrégation N fiches » = 2 lignes (sous-spécifié)
- Spec v33.2 §3 « agent dialecticien » = 11 sections mais SUR 1 ENQUÊTE uniquement
- Draft `_draft_ARTICLE.md` = 191 lignes, basé seulement sur Sumer

### 1.2 Problème
Le pipeline actuel s'arrête à la fiche d'enquête. **Aucune phase d'agrégation** N→1. Pour rédiger l'article Substack final, l'humain (ou LLM hôte) doit relire manuellement les 10+ fiches, repérer les transversalités, brainstormer les thèses, vérifier les F###. Travail long, répétitif, non-traçable, non-répétable.

### 1.3 Pilote de validation
Le 2026-06-06, un brainstorm manuel sur les 10 fiches Sumer a détecté **6 transversalités** et **3 thèses cardinales** en 1 prompt (~17K chars) :
- T1 (INVERSION) : l'article original est à l'envers (modernes ont PERDU des solutions)
- T2 (MULTI-LINÉARITÉ) : « 3 civilisations » est illusion d'optique occidentale
- T3 (BIAIS COMME OBJET) : le shadow ↔ marginalisation (1.5× MA ↔ 6.4× AM)
- Méta : la corrélation shadow↔centralité exige de croiser `shadow_factor` (nombre) avec `ces_civilisations_sont_absentes_de` (qualitatif) — invisible aux algos mécaniques (Jaccard, embeddings)

**Conclusion pilote** : un LLM hôte avec prompt bien conçu > 3 algorithmes mécaniques hybrides. Le design v33.3 ne doit pas ré-introduire de Python pré-processing.

## §2 CONTRAINTES DE GÉNÉRICITÉ

### 2.1 Détection du sujet principal (multi-source, multi-format)

**Principe :** le sujet principal est détecté depuis l'**agrégat** des N fiches, pas depuis une fiche unique imposée. Le Syntheseur essaie une chaîne de sources par fiche, dans l'ordre, jusqu'à obtenir un sujet exploitable.

**Chaîne de fallback (par fiche) :**

| Priorité | Source | Pattern de reconnaissance | Fiabilité |
|----------|--------|--------------------------|-----------|
| 1 | **Titre H1** | `# INVESTIGATION — {sujet}` ou `# AUDIT — {sujet}` ou `# {sujet}` | Maximale (résumé par l'auteur) |
| 2 | **§1 RÉSUMÉ EXÉCUTIF** (si convention respectée) | `## §1 RÉSUMÉ EXÉCUTIF` | Haute (5 faits clés + acteurs) |
| 3 | **Meta block** (header YAML-like) | `**Complexité :** X \| **Date :** Y \| ...` + titre H1 | Haute (descripteurs denses) |
| 4 | **Premier paragraphe substantiel** | Premier bloc >200 chars après les headers | Moyenne (peut être générique) |
| 5 | **Filename** (kebab-case) | `YYYY-MM-DD_HH-MM_<sujet>_<type>.md` → split sur `_` | Moyenne (sujets courts, codes imposés) |
| 6 | **Headings `## §N`** (top 5) | Mots-clés des sections, pondérés par position | Basse (peut être trompeur) |

**Agrégation :**
- Pour chaque fiche, le Syntheseur extrait `(sujet_brut, 5_mots_cles, these_testee, statut)` via la chaîne ci-dessus
- `sujet_principal` = sujet_majoritaire (par fréquence de mots-clés, stop-words exclus)
- Si aucun sujet_majoritaire > 50% des fiches → GATE_H0 (orthogonalité probable)
- Le Syntheseur **ne présume pas** qu'il y a « une première fiche » : il travaille sur l'ensemble

**Exemple concret (Sumer pilote) :**
- Fiche S : titre « Sumer versus France » + §1 « confronte 7 problèmes France à sumériens »
- Fiche R : titre « Rome versus France » + §1 « unit Rome et France par filiation CJC »
- Fiche AM : titre « Amériques précolombiennes » + filename `CIVILISATION_MANQUANTE`
- Fiche META : titre « Recalcul shadow meta » + filename `RECALCUL`
- → Sujet_majoritaire = « dette / bureaucratie / France vs civilisations antiques » (5+ fiches convergent)
- → 4 fiches annexes détectées par autres critères (cf. §2.2)

### 2.2 Fiches annexes (iceberg max / contre-rapports)
- Détection générique (pas de mots-clés hardcodés) :
  - **Critère 1** : `shadow_factor > 3×` (la fiche se signale comme « à charge »)
  - **Critère 2** : `complexity = APEX` (enquête longue, souvent audit/autopsy)
  - **Critère 3** : `these_centrale` contient un marqueur d'**opposition faible** (« ne...PAS », « contredit », « limite », « biaisé », « recalcul », « audit », « réfut... », « manqu... », « absent... »)
  - Au moins 2 des 3 critères → statut `annexe-refutative`
- Le Syntheseur les signale explicitement dans `meta.annexes_detectees` : « 3 fiches annexes (X, Y, Z) traitent le sujet principal en mode réfutatif »
- Leurs F### comptent pour les transversalités mais avec glyphe **renforcé** (✧/⁅ au lieu de ✦/✧) car ils sont à charge par construction

### 2.3 Orthogonalité
- Si 2+ fiches ont une these_centrale **incompatible** avec le sujet principal (ex: fiche sur le climat dans une agrégation dette antique)
- Comportement : **GATE_H0** (nouveau) = HALTE explicite, demande à l'humain de regrouper
- Pas de forçage par projection métaphorique
- Pas de fusion hasardeuse

### 2.4 Paramètres
- **K** (seuil transversalité) : défaut 3, configurable 2-5
- **N_theses** : défaut 3, configurable 1-5
- **complexity** : médiane des complexités des N fiches, configurable SIMPLE/MEDIUM/COMPLEX/APEX

## §3 POSITION DANS LE PIPELINE

```
PHASE 1 — ENQUÊTES INDIVIDUELLES (v33.0-v33.2, inchangé)
  Pour chaque enquête i ∈ [1, N] :
    Agent A (parseur regex) → F### détectés
    Agent B (LLM lecteur cursif) → 11 sections de quintessence
    Agent C (LLM curator) → fusion Jaccard + scoring
    Agent D (LLM verifier) → cross-check
    Agent E (humain) → validation
    → Sortie : quintessence_i.yaml (12 sections)

PHASE 2 — NOUVELLE AGRÉGATION N→1 (v33.3)
  Agent F (Syntheseur, LLM hôte only) :
    1. Charger N quintessences
    2. Détecter sujet_majoritaire via chaîne multi-source §2.1
    3. Classifier fiches : principales vs annexes-réfutatives (§2.2)
    4. Pour chaque fiche : résumer en 3-5K chars (working memory LLM)
    5. Cross-corréler : acteurs, domaines, causalités, thèses, shadows
    6. Détecter transversalités (≥K fiches)
    7. Brainstormer N_theses cardinales candidates
    8. Mapper F### → thèses
    9. Identifier gaps (F### isolés)
    10. Méta-observations (patterns cross-fiche)
    11. Sortir synthese.yaml
    → GATE_H : 7 checks (H0 orthogonalité, H1-H6 standards)
    → Sortie : synthese.yaml (8 sections)
```

## §4 CONTRACTS

### 4.1 INPUT
- N fichiers `*_quintessence.yaml` valides (v33.1 ou v33.2 schema)
- **Pas d'ordre imposé** : le Syntheseur détecte le sujet_majoritaire via §2.1 (chaîne multi-source)
- Paramètres : K (défaut 3), N_theses (défaut 3), complexity (défaut = médiane des complexités des fiches)
- Optionnel : `synthese_config.yaml` (override des défauts)
- Optionnel : `--principal <fiche_id>` pour forcer manuellement la fiche principale (override de la détection auto)

### 4.2 OUTPUT
- 1 fichier `synthese.yaml` (8 sections, voir §6)
- 1 fichier `synthese_human_review.md` (résumé 1 page pour arbitrage humain)
- Code retour : 0 (succès), 1 (GATE_H fail), 2 (refus humain), 3 (orthogonalité GATE_H0)

### 4.3 Garanties
- Traçabilité : tout F### cité → source (fiche + section)
- Reproductibilité : même input + même prompt = même output (LLM deterministe cfg=0)
- Auditabilité : GATE_H reproductible mécaniquement
- Non-régression : le Syntheseur ne MODIFIE aucune fiche source

## §5 ALGORITHME DE DÉTECTION (LLM HÔTE)

### 5.1 Pourquoi pas de mécanique
Le pilote 2026-06-06 a démontré qu'un LLM hôte détecte des transversalités **invisibles aux algos mécaniques** :
- Corrélation shadow_factor ↔ centralité occidentale (1.5× MA ↔ 6.4× AM)
- Cette transversalité exige de croiser un nombre avec un constat qualitatif
- Jaccard : rate (similarité textuelle)
- Embeddings : rate (sémantique de surface)
- LLM hote : capture (sémantique profonde + cross-numeric)

### 5.2 Prompt système (esquisse)
```
Tu es l'Agent F — Syntheseur SUBLIMATOR. Tu reçois N quintessences YAML.
Mission : agréger en 1 fiche synthèse (synthese.yaml).

PROCESS :
1. Charge les N quintessences YAML
2. Pour chaque fiche i, extrais le sujet via la chaîne §2.1 :
   - Essaye titre H1 → §1 RÉSUMÉ EXÉCUTIF → meta block → 1er § → filename → headings
   - Première source qui matche = sujet_brut_i
3. Calcule sujet_majoritaire = agrégat (fréquence mots-clés, stop-words exclus)
4. Si sujet_majoritaire < 50% des fiches → GATE_H0 (orthogonalité)
5. Classifier chaque fiche : principale vs annexe-refutative (§2.2)
6. Pour chaque fiche i, produis un résumé structuré 3-5K :
   - these_centrale (1 phrase)
   - 3 theses_implicites cles
   - 5-10 F### les plus significatifs
   - 3-5 acteurs majeurs
   - shadow_factor
   - statut (principale / annexe-refutative / annexe-complementaire)
7. Cross-corrèle les résumés :
3. Cross-corrèle les résumés :
   - Acteurs recurrents (memes personnes/concepts dans >=K fiches)
   - Domaines partages (memes champs disciplinaires)
   - Causalites similaires
   - Theses convergentes / opposées
4. Detecte transversalites : concepts, acteurs, causalites, theses
   presents dans >=K fiches
5. Brainstorm N_theses cardinales candidates :
   - Continuité (ce qui persiste à travers les fiches)
   - Rupture (ce qui change, les seuils, les seuils-de-rupture)
   - Exception (ce qui distingue une fiche des autres, pourquoi)
6. Pour chaque these, identifie 3-5 F### justificatifs (toutes fiches)
7. Identifie les gaps : F### isoles, pas dans transversalites
8. Produis 1-3 meta-observations (patterns cross-fiche :
   correlations numeriques, asymetries, distributions)
9. Evalue ce_qui_tient et ce_qui_tombe du sujet principal

GATE_H :
- H1 : si N>=K, au moins 1 transversalite detectee
- H2 : chaque these a >=3 F### justificatifs
- H3 : tout F### cite a un glyphe (X/X/X/X)
- H4 : pas de circularite (META n'auto-valide pas META)
- H5 : au moins 1 meta-observation
- H6 : shadow_factor rapporte pour chaque these

FORMAT SORTIE : synthese.yaml (8 sections)

EXEMPLE OUTPUT (1 these cardinale) :
```yaml
- id: THESE-001
  label: "Multi-linearite de la transmission"
  position: continuite
  theses_implicites_alignees:
    - "Rome est dans le Code civil francais par filiation DIRECTE"
    - "Le Moyen Age est la CEINTURE DE TRANSMISSION entre Rome et la France"
    - "L'Islam est le chainon MANQUANT de la transmission vers l'Europe"
  f_atomiques_justificatifs: [F-CJC-DIRECT, F-MA-BOLOGNE, F-ISL-CORDOUE]
  fiches_soutien: [R, MA, I]
  fiches_opposition: [AM]
  shadow_factor: 2.5
  glyphe_min: X
```

## §6 YAML OUTPUT (8 SECTIONS)

```yaml
synthese:
  meta:
    date: YYYY-MM-DD
    source_fiches: N
    complexity: SIMPLE|MEDIUM|COMPLEX|APEX
    sujet_principal:
      these_testee: "..."
      faits_cles: ["...", "..."]
      acteurs_principaux: ["...", "..."]
    shadow_factor_agregé: Nx  # médiane pondérée des ombres des fiches
    annexes_detectees: [ficheX, ficheY]  # si applicable

  transversalites:
    - id: TR-001
      label: "Concept partage"
      type: acteur|domaine|causalite|these|fait
      fiches_concernees: [fiche1, fiche2, fiche3]
      f_atomiques: [F-XXX-NNN, F-XXX-NNN]
      force: "X% des fiches"
      glyphe_agregé: X/X/X/X

  theses_cardinales:
    - id: THESE-001
      label: "These cardinale 1"
      position: continuite|rupture|exception
      theses_implicites_alignees: [these_text, these_text]
      f_atomiques_justificatifs: [F-XXX-NNN, ...]
      fiches_soutien: [fiche1, fiche2]
      fiches_opposition: [fiche3]
      shadow_factor: Nx
      glyphe_min: X

  meta_observations:
    - observation: "Pattern transversal detecte"
      evidence: "..."
      fiches_concernees: [fiche1, fiche2]
      implication: "..."

  gaps:
    - gap: "F### isole"
      f_atomiques: [F-XXX-NNN]
      fiches: [fiche1]
      raison: "Pas de recurrence >=K"

  ce_qui_tient:
    - these_originale: "..."
      soutient_transversalites: [TR-001, TR-002]
      soutient_theses: [THESE-001]

  ce_qui_tombe:
    - these_originale: "..."
      contredit_par: [THESE-002]
      f_atomiques_contraires: [F-XXX-NNN]
      shadow_factor: Nx

  erreurs_detectees:
    - type: circularite|orthogonalite|gap_critique
      description: "..."
      action: "GATE_H declenche"
```

## §7 GATE_H SPÉCIFICATION

| ID | Critère | Action si fail |
|----|---------|----------------|
| H0 | Orthogonalité détectée (≥2 fiches incompatibles avec sujet) | HALTE explicite, code retour 3 |
| H1 | N<K → au moins 1 transversalité détectée | HALTE, code retour 1 |
| H2 | Chaque thèse ≥3 F### justificatifs | HALTE, code retour 1 |
| H3 | Tout F### cité a glyphe (✦/✧/⁅/❧) | HALTE, code retour 1 |
| H4 | Pas de circularité (META ∉ fiches validant META) | HALTE, code retour 1 |
| H5 | ≥1 méta-observation | HALTE, code retour 1 |
| H6 | shadow_factor agrégé ≥1 et reporté par thèse | HALTE, code retour 1 |

## §8 CIBLES PAR TIER

| Tier | Transversalités | Thèses | Méta-obs | F### cités | URLs citées |
|------|----------------|--------|----------|------------|-------------|
| SIMPLE | 1-2 | 1 | 1 | 5-10 | 3-5 |
| MEDIUM | 3-5 | 2 | 2 | 15-25 | 8-12 |
| COMPLEX | 6-9 | 3 | 3 | 30-50 | 15-25 |
| APEX | 10+ | 5 | 5 | 50-80 | 25-40 |

## §9 TESTS (5 MOCKS)

1. **mock_2_identiques** : 2 fiches au contenu quasi-identique → 100% des F### en transversalités, 1 thèse, K=2 obligatoire
2. **mock_2_orthogonales** : 2 fiches sans overlap → 0 transversalités directes, GATE_H0 si forçage activé
3. **mock_5_cluster3** : 5 fiches, 1 cluster de 3 partageant un acteur, 2 isolées → 1 transversalité, K=3
4. **test_K_param** : K=2 vs K=3 vs K=4 → nombre de transversalités évolue de façon monotone décroissante
5. **test_circularité** : META + 5 fiches dont META est dérivée → GATE_H fail H4, code retour 1
6. **test_annexe** : 1 principale + 2 annexes-réfutatives → statut annexe détecté, transversalités annotées
7. **test_orthogonalité** : 1 dette antique + 1 climat → GATE_H0, code retour 3

## §10 LIMITES & NON-OBJECTIFS

### 10.1 Limites assumées
- **Coût LLM** : 1 prompt principal (matrice maître) + 1 prompt de brainstorm = 2 appels LLM
- **Déterminisme** : cfg=0 requis, sinon résultats variables
- **Token budget** : matrice maître 10 fiches × 4K = 40K chars + brainstorm prompt 20K = 60K total (compatible 200K context)
- **Pas de garantie causale** : transversalité = corrélation, pas causalité

### 10.2 Non-objectifs
- Ne rédige PAS l'article Substack (rôle de l'agent Rédacteur en aval)
- Ne MODIFIE aucune fiche source (lecture seule)
- Ne produit PAS de recommandations politiques
- Ne fait PAS d'embedding, de Jaccard, ou de pré-processing Python
- Ne contourne PAS GATE_H0 (orthogonalité = HALTE)

## §11 QUESTIONS OUVERTES

1. **Multi-agrégation** : peut-on enchaîner plusieurs Syntheseur (ex: 10 fiches → 3 sous-synthèses → 1 synthèse finale) ? Pour l'instant : NON, 1 seule passe.
2. **Cache** : faut-il cacher les résumés LLM (3-5K par fiche) entre passes ? Pour l'instant : NON, recalcul à chaque appel.
3. **Visualisation** : faut-il produire un graphe d'acteurs/domaines (matplotlib, mermaid) ? Pour l'instant : NON, YAML only.
4. **Ré-injection** : doit-on ré-injecter la synthèse comme nouvelle fiche (META_v2) pour une 2ème passe ? Pour l'instant : NON, c'est un output terminal.

## §12 ROADMAP

1. **2026-06-06** : Design doc (ce fichier) → self-review → user-review → validation
2. **2026-06-07** : Spec v33.3 (intégration §X.6 dans `tools/engines/sublimator/2026-06-06_spec_v33.2.md` → v33.3)
3. **2026-06-07** : Plan d'implémentation (`docs/superpowers/plans/2026-06-06-syntheur-v33.3.md`)
4. **2026-06-08** : Tests mocks (5 fichiers YAML minimaux) + exécution `pytest tests/extractors/test_syntheur.py`
5. **2026-06-08** : Guide humain v33.3 (ajout §17 « Agrégation N fiches »)
6. **2026-06-09** : Pilote réel sur 10 fiches Sumer → produit 1 `synthese.yaml` + 1 `synthese_human_review.md`

## §13 RÉFÉRENCES

- Spec v33.2 : `tools/engines/sublimator/2026-06-06_spec_v33.2.md` (1493 lignes)
- Design v33.2 : `docs/superpowers/specs/2026-06-06-sublimator-v33.2-extraction-design.md`
- 10 quintessences : `investigations/2026-06-03_sumer_article/_quintessence/`
- Pilote brainstorm 2026-06-06 : 6 transversalités + 3 thèses détectées
- Draft article : `investigations/2026-06-03_sumer_article/_draft_ARTICLE.md` (191 lignes)
- RÉSUMÉ EXÉCUTIF convention : §1 de chaque investigation, 5 faits clés + acteurs + gaps
