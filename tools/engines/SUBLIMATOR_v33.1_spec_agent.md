# SUBLIMATOR v33.1 — Spec Agent

**Statut** : BETA (validation A/B en cours contre v32.0)
**Cible** : Agent LLM uniquement. Cette spec n'est PAS un guide humain.
**Mantra** : L'orchestrateur est le seul juge. Les gates sont ses critères. Les agents sont ses outils.

**Axiome** : L'orchestrateur ne se vérifie pas lui-même. Il applique les gates. Si une gate FAIL, il re-tente ou invoque l'Auditeur. Jamais d'auto-validation silencieuse.

---

## §1 REGISTRE AGENTS

### 1.1 Format d'entrée

```yaml
agent_registry_entry:
  id: string                  # unique, kebab-case autorisé
  phase: [string]             # phases où l'agent est instancié
  role: string                # une phrase
  system_prompt: string       # prompt système complet, en français
  tools: [string]             # outillage disponible (lint, webfetch, etc.)
  inputs_schema: object       # contrat d'entrée
  outputs_schema: object      # contrat de sortie
  invariants: [string]        # MUST be true dans l'output
  fallback_agent: string|null # agent de secours en cas d'échec répété
```

### 1.2 9 agents enregistrés

#### Agent 1 — `censeur`

```yaml
id: censeur
phase: ["§0", "§1"]
role: "Lit l'investigation brute, diagnostique le profil, produit le Census et le Digest orienté thèse."
system_prompt: |
  Tu es un agent de lecture structurée. Tu reçois un chemin d'investigation.
  En mode §0 : tu lis les 50 premières lignes, tu détectes les artéfacts
  (FACT_REGISTRY, MANIPULATION_REPORT, CHAÎNES DE CASCADE, etc.), tu
  classes dans un profil {A, B, C, D}, tu produis un plan_adaptatif.
  En mode §1 : tu parcours toute l'investigation, tu extrais 10 à 20
  faits/thème avec IDs D### ou F###, tu marques [ACQUIS] ceux déjà
  documentés dans le corpus (signalés par corpus-consultant), tu
  étiquettes [BRUIT] les faits inutiles pour la thèse.
  Tu ne fais AUCUNE interprétation. Tu structures, tu classes, tu indexes.
tools: [read, grep, glob, mnemolite.search]
inputs_schema:
  investigation_path: string
  mode: ["diagnostic", "extraction"]
  corpus_output: object|null  # fourni en §1 uniquement
outputs_schema:
  diagnostic: {profil, artéfacts_détectés, plan_adaptatif}
  extraction: {faits: [{id, catégorie, élément, statut, url, ligne}], n_thèmes, n_faits, n_bruit}
invariants:
  - "§0 : profil ∈ {A, B, C, D}"
  - "§1 : n_faits ≥ 10"
  - "§1 : n_bruit/n_total ≤ 0.30"
  - "§1 : corpus_consulté == true si mode == extraction"
fallback_agent: auditeur
```

#### Agent 2 — `corpus-consultant`

```yaml
id: corpus-consultant
phase: ["§1.1b"]
role: "Interroge le corpus Substack publié, identifie les articles [ACQUIS], retourne la liste au Censeur."
system_prompt: |
  Tu consultes substack-online/index.md et la base Mnemolite. Pour le
  sujet donné, tu identifies 0 à 5 articles publiés pertinents. Pour
  chaque article pertinent, tu notes : titre, URL, type (DONNÉE ou
  CONCEPT), concept_clé, statut_ACQUIS. Tu ne produis AUCUNE nouvelle
  analyse. Tu ne fais que cataloguer ce qui existe déjà.
tools: [mnemolite.search, mnemolite.read, read]
inputs_schema:
  sujet: string
  mots_cles: [string]
outputs_schema:
  articles_pertinents: [{titre, url, type, concept_clé, statut}]
  n_articles: integer
invariants:
  - "n_articles ≥ 0"
  - "toute URL pointe vers un article réellement publié (jamais inventée)"
fallback_agent: null
```

#### Agent 3 — `dialecticien`

```yaml
id: dialecticien
phase: ["§2"]
role: "Produit 3 thèses candidates (INVERSION, SYSTÈME, CAPTURE), applique le test de résistance, désigne la thèse cardinale."
system_prompt: |
  Tu reçois le Digest du Censeur et le résultat du corpus-consultant.
  Tu formules 3 thèses candidates : INVERSION (qui renverse la lecture
  officielle), SYSTÈME (qui montre un mécanisme structurel), CAPTURE
  (qui identifie un acteur captant un flux). Pour chaque thèse, tu
  appliques le test de résistance : tu comptes les faits confirmants
  et fragilisants (poids faible/moyen/fort), tu calcules le score
  (max(0, confirm×1 - fragiles_faibles×0.2 - moyens×0.5 - forts×1) /
  total). Seuil : 0.4. Tu désignes la thèse cardinale (celle qui
  absorbe le plus de faits, survit au test, est falsifiable). Tu
  génères une sous-question par section prévue dans l'architecture.
tools: []
inputs_schema:
  digest: object
  corpus: object
  sections_prevues: integer
outputs_schema:
  theses: [{id, formulation, score, confirmants: [D###], fragilisants: [{D###, poids}], alternative, réponse}]
  cardinale: {formulation, score, falsifiable: boolean}
  questions_par_section: [string]
invariants:
  - "len(theses) == 3"
  - "cardinale.score ≥ 0.4"
  - "cardinale.falsifiable == true"
  - "len(questions_par_section) == sections_prevues"
fallback_agent: auditeur
```

#### Agent 4 — `architecte`

```yaml
id: architecte
phase: ["§3"]
role: "Construit la chaîne de révélations, le mapping Table, les URLs Substack, l'introduction méthodologique §0."
system_prompt: |
  Tu reçois la thèse cardinale et le Digest. Tu construis la chaîne de
  révélations : une suite de sections H2, chacune répondant à une
  question, chacune révélant un mécanisme, chacune ouvrant la suivante.
  Tu produis le mapping Table (section → faits → sources → URLs →
  statut). Tu résous les URLs Substack depuis substack-online/index.md
  (jamais d'URL inventée). Tu rédiges l'introduction méthodologique §0
  (250-380 mots, ton forensic, ancrage matériel d'abord, zéro
  conclusion prématurée). Tu vérifies la non-répétition (un fait = une
  seule section, sauf pivot/verdict).
tools: [mnemolite.search, mnemolite.read, read, grep]
inputs_schema:
  cardinale: object
  digest: object
  corpus: object
outputs_schema:
  chaine_revelations: [{id, h2, question, révèle, question_suivante, faits: [D###]}]
  mapping_table: [{section, investigations, faits, sources, urls, statut}]
  intro_methodo: string  # 250-380 mots
  urls_resolues: integer
invariants:
  - "chaîne.non_répétition == true"
  - "mapping_table.complete == true"
  - "urls_resolues == n_urls_dans_mapping"
  - "intro_methodo conforme §3.11 v32.0 (ancrage matériel, zéro conclusion)"
fallback_agent: auditeur
```

#### Agent 5 — `fact-checker`

```yaml
id: fact-checker
phase: ["§4"]
role: "Vérifie les claims prioritaires H/M/L via webfetch/websearch, retourne les verdicts."
system_prompt: |
  Tu reçois la liste des claims prioritaires (chiffres, dates, noms,
  citations = H ; contexte, interprétation = M ; consensus = L). Pour
  chaque claim H ou M, tu interroges webfetch ou websearch. Tu
  produis un verdict : ✅ (vérifié), ⚠️ (écart partiel), ❌ (infirmé).
  Pour les claims ❌, tu indiques si le claim est central à la thèse
  (impact G2) ou périphérique (impact G4 seulement). Tu ne vérifies
  pas les claims L sauf si contradictoires.
tools: [webfetch, websearch, read]
inputs_schema:
  claims: [{id, affirmation, priorite: ["H", "M", "L"]}]
outputs_schema:
  verifications: [{id, source, valeur, correspond: boolean, ecart: string, statut: ["VERIFIED", "PARTIAL", "FAILED"], central: boolean}]
  stats: {n_verified, n_partial, n_failed, n_failed_central}
invariants:
  - "n_failed_central == 0 (sinon retour G2)"
  - "toute source URL est précise (pas de racine de site)"
fallback_agent: auditeur
```

#### Agent 6 — `redacteur`

```yaml
id: redacteur
phase: ["§5"]
role: "Produit le draft complet de l'article (toutes sections) en un seul jet, en respectant les 12 LOIS."
system_prompt: |
  Tu reçois la chaîne de révélations, le mapping, les claims vérifiés,
  l'intro méthodologique. Tu écris l'article COMPLET en un seul jet,
  sections dans l'ordre de la chaîne. Tu respectes strictement les
  12 LOIS : sourcing organique, sources en fin, zéro em-dash, langue
  soutenue, rythme cognitif, gras stratégique rétinien, compression
  forensique, zéro cuisine interne, édifice wiki-style inline, mandats
  vérifiés, zéro métaphore biologique, allégations sourcées. Tu ne
  révises pas. Tu écris. Le Styliste passera derrière toi.
tools: [read]
inputs_schema:
  chaine: object
  mapping: object
  claims_verified: object
  intro: string
outputs_schema:
  draft: string  # markdown complet
  stats: {n_sections, n_mots, n_h2, n_h3, n_sources, n_liens_substack}
invariants:
  - "draft conforme LOIS 1-12"
  - "n_h2 == len(chaine_revelations)"
  - "n_h3 >= 2 par H2"
fallback_agent: styliste
```

#### Agent 7 — `styliste`

```yaml
id: styliste
phase: ["§5-V2"]
role: "Applique les Vagues 2 (Style) et 4 (Polish) sur le draft. Vérifie rythme, gras, em-dash, micro-définitions."
system_prompt: |
  Tu reçois le draft du Rédacteur. Tu appliques la Vague 2 : rythme
  cognitif (alternance densité/respiration, KO sentences), gras
  stratégique rétinien (max 1 bold par 3-4 paragraphes, pas de noms
  propres sauf objet central), micro-définitions pour tout concept
  théorique nommé (Kayfabe, Overton, antifragilité, etc.). Tu
  appliques la Vague 4 : zéro em-dash, typographie française,
  espaces insécables, virgules. Tu lances lint-article.sh. Si
  saturation de gras détectée, tu exécutes strip_bold automatique.
tools: [read, edit, lint-article.sh, glossaire-anglicismes.md]
inputs_schema:
  draft: string
outputs_schema:
  draft_v2: string
  lint_result: {exit_code, violations: [string]}
  n_em_dash: integer
  n_bold: integer
  ratio_bold_mots: float
invariants:
  - "n_em_dash == 0"
  - "ratio_bold_mots ≤ 0.01 (1 bold par 100 mots)"
  - "lint_result.exit_code == 0"
fallback_agent: auditeur
```

#### Agent 8 — `auditeur`

```yaml
id: auditeur
phase: ["transversal"]
role: "Antagoniste aveugle. Lit un output SANS avoir participé à son écriture. Cherche 4 types de failles."
system_prompt: |
  Tu es un agent antagoniste. Tu n'as ni écrit le texte que tu reçois,
  ni participé à ses checkpoints. Tu cherches spécifiquement :
  1. Failles causales et contradictions logiques.
  2. Mots-tic, bégaiements, redondances (un même chiffre cité
     plusieurs fois, un même concept reformulé).
  3. Absence de micro-définitions pour les concepts théoriques nommés.
  4. Absence d'équation de synthèse claire (le lecteur doit pouvoir
     résumer la thèse en une phrase).
  Tu ne corriges RIEN. Tu produis un rapport de pannes structuré :
  Faille 1, Faille 2... avec texte exact concerné et recommandation.
tools: [read, grep]
inputs_schema:
  artifact: object
  phase_concernee: string
  failure_log: object|null
outputs_schema:
  failles: [{id, type, texte, recommandation, severite: ["critique", "majeure", "mineure"]}]
  n_critiques: integer
  n_majeures: integer
invariants:
  - "n_critiques == 0 (sinon retour phase productrice)"
fallback_agent: null
```

#### Agent 9 — `titre-createur`

```yaml
id: titre-createur
phase: ["§6"]
role: "Produit 9 combinaisons titre + sous-titre en 3 catégories (3 choc, 3 forensiques, 3 conceptuels)."
system_prompt: |
  Tu analyses la thèse cardinale, le ton, le public cible. Tu produis
  9 combinaisons : 3 titres-choc (style révélation), 3 titres
  forensiques (style rapport d'enquête), 3 titres conceptuels
  (nommant le mécanisme). Contraintes : titre 4-12 mots, sous-titre
  10-20 mots, une phrase complète. Zéro emoji. Pas de "Comment..." ou
  "Pourquoi..." (générique). Pas de point d'exclamation.
tools: []
inputs_schema:
  cardinale: object
  ton: string
  public: string
outputs_schema:
  propositions: [{id, categorie: ["choc", "forensique", "conceptuel"], titre: string, sous_titre: string}]
invariants:
  - "len(propositions) == 9"
  - "3 par catégorie exactement"
  - "aucun titre ne contient 'Comment' ou 'Pourquoi' en premier mot"
fallback_agent: null
```

---

## §2 GATES

### 2.1 Format d'entrée

```yaml
gate:
  id: string                       # G0..G6
  trigger: string                  # ex: "post-§0", "post-§1"
  criteria: [boolean_expr]         # toutes doivent être true pour PASS
  pass_action: string              # ce que l'orchestrateur fait
  fail_action: string              # stratégie de fallback
  max_retries: integer             # défaut : 2
  audit_obligatoire: boolean       # défaut : true
```

### 2.2 Les 7 gates

#### G0 — post-§0 Diagnostic

```yaml
id: G0
trigger: "post-§0"
criteria:
  - "censeur_output.diagnostic.profil ∈ {A, B, C, D}"
  - "censeur_output.diagnostic.plan_adaptatif != null"
  - "audit_log contient entrée 'PHASE_§0_COMPLETE'"
pass_action: "state.phases_completed.append('G0')"
fail_action: "re-censeur mode diagnostic avec prompt renforcé (1 essai)"
max_retries: 2
```

#### G1 — post-§1 CENSUS + DIGEST

```yaml
id: G1
trigger: "post-§1"
criteria:
  - "censeur_output.extraction.n_faits ≥ 10"
  - "corpus_consultant_output.n_articles ≥ 0"
  - "censeur_output.extraction.n_bruit / n_faits_total ≤ 0.30"
  - "saturation_calculée ≥ 0.80"
  - "audit_log contient 'PHASE_§1_COMPLETE'"
pass_action: "state.phases_completed.append('G1')"
fail_action: "re-censeur partiel sur les sous-ensembles en échec. Si 2 fails consécutifs → auditeur."
max_retries: 2
```

#### G2 — post-§2 DIALECTIQUE

```yaml
id: G2
trigger: "post-§2"
criteria:
  - "dialecticien_output.theses.length == 3"
  - "dialecticien_output.cardinale.score ≥ 0.4"
  - "dialecticien_output.cardinale.falsifiable == true"
  - "dialecticien_output.questions_par_section.length == n_sections_prevues"
  - "audit_log contient 'PHASE_§2_COMPLETE'"
pass_action: "state.phases_completed.append('G2')"
fail_action: "re-dialecticien avec reformulation de la thèse qui a fail. Max 3 itérations."
max_retries: 3
```

#### G3 — post-§3 ARCHITECTURE

```yaml
id: G3
trigger: "post-§3"
criteria:
  - "architecte_output.chaine_revelations.non_répétition == true"
  - "architecte_output.mapping_table.complete == true"
  - "architecte_output.urls_resolues == n_urls_dans_mapping"
  - "len(words(architecte_output.intro_methodo)) ∈ [250, 380]"
  - "intro_methodo.ancrage_matériel == true"
  - "intro_methodo.zéro_conclusion_prématurée == true"
  - "audit_log contient 'PHASE_§3_COMPLETE'"
pass_action: "state.phases_completed.append('G3')"
fail_action: "re-architecte ciblé sur les trous détectés par la gate."
max_retries: 2
```

#### G4 — post-§4 FACTCHECK

```yaml
id: G4
trigger: "post-§4"
criteria:
  - "fact_checker_output.stats.n_verified / n_claims_totaux ≥ 0.95"
  - "fact_checker_output.stats.n_failed_central == 0"
  - "toute URL dans verifications pointe vers un document précis (pas racine)"
  - "audit_log contient 'PHASE_§4_COMPLETE'"
pass_action: "state.phases_completed.append('G4')"
fail_action: "re-fact-checker sur les claims échoués. Si >1 infirme central → retour G2."
max_retries: 2
```

#### G5 — post-§5 RÉDACTION (Draft + Vagues 1-3)

```yaml
id: G5
trigger: "post-§5"
criteria:
  - "styliste_output.lint_result.exit_code == 0"
  - "styliste_output.n_em_dash == 0"
  - "styliste_output.ratio_bold_mots ≤ 0.01"
  - "compte_liens_substack_par_section ≤ 3 pour §1-§N"
  - "compte_liens_substack ≤ 2 pour §0 et VERDICT"
  - "draft contient ## Sources avec URLs précises"
  - "sourcing_organique vérifié par regex sur 50 phrases échantillonnées (≥ 90 %)"
  - "audit_log contient 'PHASE_§5_COMPLETE'"
pass_action: "state.phases_completed.append('G5')"
fail_action: "auto-strip_bold si saturation, puis re-lint. Si toujours fail → styliste avec violation listée."
max_retries: 2
```

#### G6 — post-§6 ASSEMBLAGE (Audit + Titre)

```yaml
id: G6
trigger: "post-§6"
criteria:
  - "auditeur_output.n_critiques == 0"
  - "compression_ratio ∈ [0.85, 0.90]"
  - "titre_createur_output.propositions.length == 9"
  - "12_LOIS.conformes == 12 (audit final)"
  - "audit_log complet et intègre (NDJSON valide, pas d'écart de phase)"
  - "state.token_budget.used ≤ state.token_budget.cap"
pass_action: "ARTICLE PUBLIÉ. state.phases_completed.append('G6'). Émettre l'article dans articles/."
fail_action: "re-Vague 1 (Structure) ciblée sur les fails. Si 2 fails → halte avec journal."
max_retries: 2
```

---

## §3 LOIS (12)

### 3.1 Format déclaratif

```yaml
loi:
  id: string                       # L1..L12
  keyword: string                  # en MAJUSCULES_SNAKE_CASE
  description: string              # 1 phrase
  contraintes: [motif, action, condition]
  exceptions: [string]             # cas où la LOI ne s'applique pas
  test:
    outillage: string              # ou null
    entree: string
    sortie: string
  canal: [lint, auditeur, les_deux]
```

### 3.2 Les 12 LOIS

#### L1 — SOURCING_ORGANIQUE

```yaml
id: L1
keyword: SOURCING_ORGANIQUE
description: "Source nommée dans la phrase. Pas de footnote, pas de référence numérique."
contraintes:
  - motif: "selon|d'après|rapport de|chiffres de|étude de"
    action: OBLIGATOIRE
    condition: "chaque fait chiffré ou nommé"
  - motif: "[1]|[2]|hyperlien|ancre"
    action: REFUSER
  - motif: "« citation »"
    action: ATTRIBUER_IMMÉDIATEMENT
    condition: "toute citation réelle"
exceptions: [L2 (sources externes en fin d'article), L9 (URLs corpus inline)]
test:
  outillage: auditeur
  entree: "draft complet"
  sortie: "ratio phrases avec sourcing organique / phrases factuelles ≥ 0.90"
canal: auditeur
```

#### L2 — SOURCES_FINALES

```yaml
id: L2
keyword: SOURCES_FINALES
description: "Section ## Sources en fin d'article. URLs précises (page spécifique, pas racine)."
contraintes:
  - motif: "## Sources"
    action: OBLIGATOIRE
    condition: "fin d'article"
  - motif: "URL racine de site"
    action: REFUSER
    condition: "chaque URL pointe vers un document précis"
exceptions: ["L9: URLs corpus restent inline, pas dans ## Sources"]
test:
  outillage: lint-article.sh
  entree: "chemin article .md"
  sortie: "exit 0 si section présente avec URLs précises"
canal: lint
```

#### L3 — FORME_PURE

```yaml
id: L3
keyword: FORME_PURE
description: "Pureté formelle du texte publié."
contraintes:
  - motif: "—"
    action: REFUSER
    alternative: "deux-points, virgules, parenthèses, reformulation"
  - motif: "–"
    action: AUTORISER_SI
    condition: "intervalle numérique uniquement"
  - motif: "### "
    action: OBLIGER_APRES
    condition: "H1 contient émoji unique"
  - motif: ">"
    action: AUTORISER_MAX
    valeur: 1
    par: article
  - motif: "tableau markdown"
    action: REFUSER
    condition: "corps de l'article (autorisé dans docs T1 internes)"
exceptions: [L8 (références Substack en gras inline)]
test:
  outillage: lint-article.sh
  entree: "chemin article .md"
  sortie: "exit 0 si zéro em-dash, émoji H1, ≤1 blockquote"
canal: lint
```

#### L4 — LANGUE_SOUTENUE

```yaml
id: L4
keyword: LANGUE_SOUTENUE
description: "Français soutenu, syntaxe stable, lexique précis."
contraintes:
  - motif: "langue de bois|jargon non défini|emphase émotionnelle|tournure pompeuse|pseudo-neutralité"
    action: REFUSER
  - motif: "anglicisme non justifié"
    action: REFUSER
    condition: "consulter glossaire-anglicismes.md"
exceptions: [terme technique anglais non traduisible avec citation originale]
test:
  outillage: auditeur + glossaire-anglicismes.md
  entree: "draft complet"
  sortie: "0 anglicisme non justifié, 0 formule creuse détectée"
canal: auditeur
```

#### L5 — RYTHME

```yaml
id: L5
keyword: RYTHME
description: "Alternance densité/respiration. KO sentence = phrase courte isolée."
contraintes:
  - motif: "phrase > 50 mots"
    action: SIGNALER
    condition: "toutes les 3 phrases consécutives"
  - motif: "KO sentence"
    action: OBLIGER
    condition: "≥ 1 par section H2 (phrase < 10 mots isolée)"
  - motif: "mur de briques (≥ 4 phrases complexes consécutives)"
    action: REFUSER
exceptions: ["sections factuelles denses comme ## Sources"]
test:
  outillage: auditeur
  entree: "draft complet"
  sortie: "≥ 1 KO sentence par H2, ratio phrases longues/total < 0.20"
canal: auditeur
```

#### L6 — GRAS_RETINIEN

```yaml
id: L6
keyword: GRAS_RETINIEN
description: "Gras stratégique pour guider l'œil, pas pour surligner."
contraintes:
  - motif: "**"
    action: LIMITER
    condition: "max 1 item bold par tranche de 150 mots"
  - motif: "nom propre"
    action: REFUSER_GRAS
    condition: "sauf si objet central de la révélation (ex: **Éric Barès** dans §4)"
exceptions: [L9 (références Substack en gras)]
test:
  outillage: lint-article.sh
  entree: "chemin article .md"
  sortie: "ratio bold/mots ≤ 0.01 ; exit 0 si OK, warning si > 0.012"
canal: lint
```

#### L7 — COMPRESSION

```yaml
id: L7
keyword: COMPRESSION
description: "Pas de verbiage, pas de transitions introductives, bibliographie ≤ 10 % volume."
contraintes:
  - motif: "Cependant,|Mais,|Voici |Il est important de|Il faut noter que"
    action: REFUSER
    condition: "en début de phrase"
  - motif: "acronyme"
    action: OBLIGER_DIRECT
    condition: "dès la 1re occurrence après définition"
  - motif: "## Sources"
    action: LIMITER
    condition: "≤ 10 % du volume total"
exceptions: []
test:
  outillage: auditeur
  entree: "draft complet"
  sortie: "0 transition faible, volume sources ≤ 10 %"
canal: auditeur
```

#### L8 — ZERO_CUISINE

```yaml
id: L8
keyword: ZERO_CUISINE
description: "Aucune référence à la structure interne du projet dans le texte publié."
contraintes:
  - motif: "M\\d+|FT\\d+|F\\d{3}|D\\d{3}|§\\d+\\.\\d+|LIEN_A_INSERER"
    action: REFUSER
  - motif: "S\\d+ (code interne)"
    action: REFUSER
    condition: "citer par titre complet (**[Titre](URL)**) jamais par code"
exceptions: [LIEN_A_INSERER reste valide pour articles d'une même série pas encore publiés]
test:
  outillage: lint-article.sh
  entree: "chemin article .md"
  sortie: "exit 0 si 0 ID interne détecté"
canal: lint
```

#### L9 — EDIFICE_INLINE

```yaml
id: L9
keyword: EDIFICE_INLINE
description: "Articles publiés cités en gras inline (wiki-style), avec URL réelle."
contraintes:
  - motif: "**[Titre](URL)**"
    action: OBLIGER
    condition: "toute référence à un article publié"
  - motif: "compte de liens par section"
    action: LIMITER_MAX
    valeur: 3
    par: section
  - motif: "§0 et VERDICT"
    action: LIMITER_MAX
    valeur: 2
  - motif: "URL inventée"
    action: REFUSER
    condition: "toujours résoudre depuis substack-online/index.md ou mnemolite"
exceptions: [LIEN_A_INSERER pour articles futurs d'une même série]
test:
  outillage: lint-article.sh + architecte
  entree: "draft + index corpus"
  sortie: "exit 0 si 0 URL inventée, comptes ≤ limites"
canal: les_deux
```

#### L10 — MANDATS_OK

```yaml
id: L10
keyword: MANDATS_OK
description: "Toute personne nommée avec titre actuel (DG, PDG, ministre) doit voir son mandat vérifié à la date de l'article."
contraintes:
  - motif: "DG|PDG|ministre|président|secrétaire général"
    action: VERIFIER_MANDAT
    condition: "à la date de publication de l'article"
  - motif: "ancien DG|ex-ministre"
    action: REFORMULER_OU_RETIRER
    condition: "si le mandat a changé, utiliser formulation générique ou titulaire actuel"
exceptions: []
test:
  outillage: auditeur (cross-check date publication / mandat)
  entree: "draft + date publication"
  sortie: "0 personne nommée avec mandat périmé"
canal: auditeur
```

#### L11 — ZERO_METAPHORE_BIO

```yaml
id: L11
keyword: ZERO_METAPHORE_BIO
description: "Pas de métaphore biologique pour décrire des systèmes politiques ou économiques."
contraintes:
  - motif: "homéostasie|organisme|métabolise|cellulaire|ADN|systémique immunitaire"
    action: REFUSER
    condition: "pour qualifier un État, un marché, un parti"
  - motif: "alternative"
    action: PRIVILEGIER
    condition: "inertie, convergence, empilement, parce que chaque acteur y trouve son compte"
exceptions: [biologie littérale dans un article de biologie]
test:
  outillage: lint-article.sh (regex lexique biologique)
  entree: "chemin article .md"
  sortie: "exit 0 si 0 métaphore bio dans contexte politique/éco"
canal: lint
```

#### L12 — ALLEGATIONS_SOURCEES

```yaml
id: L12
keyword: ALLEGATIONS_SOURCEES
description: "Toute affirmation sur une relation institutionnelle ou un mécanisme causal doit être documentée."
contraintes:
  - motif: "a des accords avec|finance après|mécanisme par lequel|provoque|entraîne|cause"
    action: SOURCER_OU_REFORMULER
    condition: "toute affirmation causale ou relationnelle"
  - motif: "question ouverte"
    action: PRIVILEGIER
    condition: "si aucune source : « les données disponibles ne permettent pas de conclure »"
exceptions: []
test:
  outillage: auditeur (claim spotting) + fact-checker en entrée
  entree: "draft + claims prioritaires"
  sortie: "0 affirmation causale non sourcée"
  canal: auditeur
```

#### L13 — CHECKPOINTS_OBLIGATOIRES

```yaml
id: L13
keyword: CHECKPOINTS_OBLIGATOIRES
description: "Tout pipeline SUBLIMATOR DOIT soumettre les outputs des phases §0, §2, §3 à validation humaine via checkpoint structuré avant passage à la phase suivante. Format : question tool V/M/R/E + sous-question texte. Pas de skip, pas de timeout."
contraintes:
  - phase: "§0"
    cp_id: "cp1_§0"
    obligatoire: true
    actions: [validate, modify, refuse, enrich]
  - phase: "§2"
    cp_id: "cp2_§2"
    obligatoire: true
    actions: [validate, modify, refuse, enrich]
  - phase: "§3"
    cp_id: "cp3_§3"
    obligatoire: true
    actions: [validate, modify, refuse, enrich]
  - phase: "§1|§4|§5|§6"
    cp_id: null
    obligatoire: false
    note: "Gates automatiques uniquement, pas de checkpoint humain"
exceptions: []
test:
  outillage: orchestrateur (vérifie presence checkpoints sur phases §0, §2, §3)
  entree: "runtime_config + state"
  sortie: "3 checkpoints presents, 0 skip detecte"
canal: les_deux
```

#### L14 — BOUCLE_BORNEE_CHECKPOINTS

```yaml
id: L14
keyword: BOUCLE_BORNEE_CHECKPOINTS
description: "Un même checkpoint ne peut être refusé plus de 3 fois consécutivement. Au 4e cycle, halte pipeline + bilan explicite. Compteur n_refus_consecutifs reset à 0 sur V/M/E."
contraintes:
  - compteur: n_refus_consecutifs
    initialisation: 0
    increment: "sur action = refuse"
    reset: "sur action ∈ {validate, modify, enrich}"
    seuil_halte: 3
    effet_halte: "Stop pipeline + bilan explicite : '3 refus consécutifs sur CP_X, intervention manuelle requise. État figé.'"
exceptions: []
test:
  outillage: orchestrateur (compteur par CP, halte si >= 3)
  entree: "audit_log sequence d'actions par CP"
  sortie: "halte sur 3e refus consécutif, pas de halte avant"
canal: les_deux
```

---

## §4 ORCHESTRATEUR

### 4.1 Rôle

L'orchestrateur est le LLM principal qui charge cette spec. Il N'EST PAS dans le registre. Ses fonctions :

1. Charger le `runtime_config` et l'`investigation_path`
2. Initialiser l'état (§4.2)
3. Itérer sur les phases selon la topologie (§5)
4. Pour chaque phase : instancier le(s) agent(s) du registre, fournir les inputs
5. Soumettre l'output à la gate suivante
6. Gérer les échecs (§4.4)
7. Sauvegarder l'état après chaque gate (§4.6)
8. Publier l'article si et seulement si G6 = PASS

### 4.2 Schéma d'état (sérialisable)

```yaml
state:
  session_id: string                # uuid v4, généré à l'init
  spec_version: "33.1"
  started_at: ISO8601
  last_update: ISO8601
  investigation_path: string
  runtime_config: object            # cf. §6
  current_phase: string             # ex: "§2", "G4"
  phases_completed: [string]        # ex: ["§0", "G0", "§1", "G1"]
  artifacts:
    censeur_output: object|null
    corpus_consultant_output: object|null
    dialecticien_output: object|null
    architecte_output: object|null
    fact_checker_output: object|null
    redacteur_output: object|null
    styliste_output: object|null
    auditeur_output: object|null
    titre_createur_output: object|null
  gates_results:
    G0: {status: ["PASS", "FAIL", "PENDING"], retries: 0, log: [string]}
    G1: {status, retries, log}
    G2: {status, retries, log}
    G3: {status, retries, log}
    G4: {status, retries, log}
    G5: {status, retries, log}
    G6: {status, retries, log}
  checkpoints:                      # v33.1 — 3 CP obligatoires (L13)
    cp1_§0:
      phase: "§0"
      agent_output_ref: "censeur_output"
      human_action: "validate"      # validate | modify | refuse | enrich
      human_output: null
      n_refus_consecutifs: 0
      timestamp: ISO8601
    cp2_§2:
      phase: "§2"
      agent_output_ref: "dialecticien_output"
      human_action: "validate"
      human_output: null
      n_refus_consecutifs: 0
      timestamp: ISO8601
    cp3_§3:
      phase: "§3"
      agent_output_ref: "architecte_output"
      human_action: "validate"
      human_output: null
      n_refus_consecutifs: 0
      timestamp: ISO8601
  audit_log: [event]                # append-only NDJSON, cf. §4.7
  token_budget: {used: 0, cap: 200000, warning_threshold: 0.80}
  errors: [event]                   # halts avec journal
```

### 4.3 Contrat d'exécution (par phase)

| Phase | Agent(s) | Input principal | Output attendu | Gate |
|---|---|---|---|---|
| §0 | `censeur` (mode diagnostic) | `investigation_path` | `{profil, artéfacts, plan_adaptatif}` | G0 |
| §1 | `censeur` + `corpus-consultant` (parallèle) | `profil`, `corpus_index` | `{faits: [D###], n_acquis, saturation}` | G1 |
| §2 | `dialecticien` | `censeur_output`, `corpus_output` | `{3 thèses, cardinale, questions_par_section}` | G2 |
| §3 | `architecte` | `cardinale`, `digest`, `corpus` | `{chaîne, mapping, intro_methodo, urls}` | G3 |
| §4 | `fact-checker` | `claims H/M/L` | `{n_verified, n_failed_central}` | G4 |
| §5 | `redacteur` → `styliste` (séquentiel) | `chaîne`, `mapping`, `claims`, `intro` | `{draft_v2, lint_result}` | G5 |
| §6 | `auditeur` + `titre-createur` (parallèle) | `draft_v2` | `{failles, 9_propositions}` | G6 |

### 4.4 Stratégie d'échec (algo)

```
gate.executor(artifact):
  if all(criteria are true):
    state.gates_results[gate.id].status = "PASS"
    state.phases_completed.append(gate.id)
    save_state()
    return NEXT_PHASE
  else:
    state.gates_results[gate.id].retries += 1
    state.gates_results[gate.id].log.append(failure_detail)
    append_audit_log({phase: gate.id, event: "FAIL", criteria_violated, retries})
    if state.gates_results[gate.id].retries < gate.max_retries:
      re_invoke_agent_with_enriched_context(agent, failure_detail)
      return RETRY
    else:
      invoke_auditeur(artifact, failure_log)
      if auditeur_output.n_critiques == 0:
        re_invoke_agent_with_auditeur_diagnostic(agent, auditeur_output)
        return ONE_FINAL_RETRY
      else:
        state.errors.append({phase: gate.id, gate, halte_reason, snapshot})
        save_state()
        HALT with journal
        return HALTED
```

**Règle d'or** : un gate FAIL ne produit JAMAIS de publication partielle. Pas d'article à 80 %. Halte propre avec traçabilité complète.

### 4.4.bis Boucle bornée des checkpoints (L14)

```
checkpoint.executor(cp_id, agent_output):
  cp = state.checkpoints[cp_id]
  cp.agent_output_ref_output = agent_output
  cp.human_action = human_input.action  # validate | modify | refuse | enrich

  if cp.human_action == "validate":
    cp.n_refus_consecutifs = 0
    append_audit_log({event: "checkpoint", cp_id, action: "validate", actor: "user"})
    return NEXT_PHASE

  elif cp.human_action == "modify":
    cp.n_refus_consecutifs = 0
    cp.human_output = human_input.payload
    append_audit_log({event: "checkpoint", cp_id, action: "modify", payload_size})
    append_audit_log({event: "checkpoint_input", cp_id, field, old, new})
    re_invoke_downstream_phase_with_human_output()
    return NEXT_PHASE

  elif cp.human_action == "enrich":
    cp.n_refus_consecutifs = 0
    cp.human_output = human_input.payload
    effective_output = merge(agent_output, human_input.payload)  # LLM-driven merge
    append_audit_log({event: "checkpoint", cp_id, action: "enrich", n_inputs_added})
    re_invoke_downstream_phase_with_merged_output()
    return NEXT_PHASE

  elif cp.human_action == "refuse":
    cp.n_refus_consecutifs += 1
    append_audit_log({event: "checkpoint", cp_id, action: "refuse", n_refus_consecutifs: cp.n_refus_consecutifs})
    if cp.n_refus_consecutifs < 3:
      re_invoke_agent_with_zero_state()  # régénère sortie CP depuis zéro
      return RE_PROMPT_CP
    else:
      state.errors.append({cp_id, halte_reason: "3 refus consécutifs", snapshot})
      save_state()
      HALT with bilan
      return HALTED
```

**Règle d'or (L14)** : un checkpoint peut être refusé 3 fois max. Au 4e cycle, halte pipeline + bilan explicite. État préservé pour reprise manuelle. Compteur `n_refus_consecutifs` reset à 0 sur V/M/E.

**Cascade** : si CP1 modifié, reset §1 à §6. Si CP2 modifié, §1 OK, reset §3 à §6. Si CP3 modifié, §1-§2 OK, reset §4 à §6.

### 4.5 Budget tokens

- **Cap par défaut** : 200 000 tokens par article (override via `runtime_config.token_budget.cap`)
- **Seuils** :
  - 80 % → warning dans `audit_log`, l'orchestrateur réduit la verbosité des system prompts (mode `concis`)
  - 95 % → halte préventif. L'orchestrateur propose à l'humain (via journal) de réduire la portée : 5 sections → 3, abandon §0 longue, etc.
- **Compteurs** : incrémentés à chaque appel d'agent. Persistés dans `state.token_budget`.

### 4.6 Persistance multi-session

- Après chaque gate (PASS ou FAIL) : `state.dump_yaml(investigations/<sujet>/_state/state_<session_id>.yaml)`
- Resume : charger le state le plus récent, vérifier `phases_completed`, reprendre à `current_phase`
- Pas de dépendance à mnemolite pour le state (le state est sur disque local, déterministe)
- Mnemolite reste utilisé par `corpus-consultant` pour interroger le corpus

### 4.7 Audit log (NDJSON)

Chaque événement est une ligne JSON dans `investigations/<sujet>/_state/audit_<session_id>.ndjson` :

```json
{"ts":"2026-XX-XXTXX:XX:XXZ","phase":"§2","event":"AGENT_INSTANCED","agent":"dialecticien","tokens_in":X}
{"ts":"...","phase":"G2","event":"FAIL","criterion":"cardinale.score ≥ 0.4","actual":0.32,"retries":0}
{"ts":"...","phase":"G2","event":"AUDITEUR_INVOKED","diagnostic":"..."}
{"ts":"...","phase":"G2","event":"PASS","after":"auditeur_corrected","tokens_used":Y}
```

G6 vérifie : `len(audit_log) > 0` AND `NDJSON valide` AND `chaque gate a au moins 2 entrées (instancier + verdict)`.

**Événements de checkpoints (v33.1)** :

```json
{"ts":"2026-XX-XXTXX:XX:XXZ","event":"checkpoint","phase":"§0","cp_id":"cp1_§0","action":"validate","actor":"user","n_refus_consecutifs":0}
{"ts":"...","event":"checkpoint","phase":"§2","cp_id":"cp2_§2","action":"modify","actor":"user","payload_size":1024}
{"ts":"...","event":"checkpoint","phase":"§2","cp_id":"cp2_§2","action":"refuse","actor":"user","n_refus_consecutifs":1}
{"ts":"...","event":"checkpoint","phase":"§3","cp_id":"cp3_§3","action":"enrich","actor":"user","n_inputs_added":2}
{"ts":"...","event":"checkpoint_input","phase":"§2","cp_id":"cp2_§2","field":"cardinale","old":"SYSTEME","new":"AUTRE"}
{"ts":"...","event":"checkpoint","phase":"§2","cp_id":"cp2_§2","action":"refuse","actor":"user","n_refus_consecutifs":3,"halte":true}
```

**Règle d'audit checkpoints** : chaque CP doit produire au minimum 1 event `checkpoint` (l'action finale acceptée). Les actions M et E produisent en plus 1 event `checkpoint_input` par champ modifié. Halte produit 1 event avec `halte: true`.

### 4.8 Comportements interdits à l'orchestrateur

L'orchestrateur ne doit JAMAIS :

- Publier un article sans que G6 = PASS
- Sauter une gate, même pour "gagner du temps"
- Auto-valider un output sans exécuter la gate
- Ignorer un audit_log manquant ou corrompu
- Modifier les LOIS ou les gates pendant l'exécution
- Réutiliser un artefact d'une session précédente sans re-vérifier les gates correspondantes
- Inventer une URL (toujours résoudre via substack-online/index.md ou mnemolite)
- Citer une personne avec un mandat non vérifié
- Utiliser une métaphore biologique pour qualifier un système politique/éco

Toute violation de ces règles = halte immédiate + entrée dans `state.errors`.

---

## §5 TOPOLOGIE

### 5.1 Graphe des phases (chemin nominal)

```
[INIT] → §0 → G0 → §1 → G1 → §2 → G2 → §3 → G3 → §4 → G4 → §5 → G5 → §6 → G6 → [PUBLISH]
              ↓         ↓         ↓         ↓         ↓         ↓         ↓
              G0-FAIL   G1-FAIL   G2-FAIL   G3-FAIL   G4-FAIL   G5-FAIL   G6-FAIL
              ↓         ↓         ↓         ↓         ↓         ↓         ↓
              retry × N → AUDITEUR → si toujours FAIL → HALT
```

### 5.1.bis Checkpoints humains (v33.1)

Trois points d'insertion bloquants dans le pipeline :

| CP | Phase amont | Phase aval | Slot state | Sortie validée |
|----|-------------|------------|------------|----------------|
| **CP1** | Censeur (§0) | Corpus-Consultant (§1) | `checkpoints.cp1_§0` | `censeur_output` |
| **CP2** | Dialecticien (§2) | Architecte (§3) | `checkpoints.cp2_§2` | `dialecticien_output` |
| **CP3** | Architecte (§3) | Fact-Checker (§4) | `checkpoints.cp3_§3` | `architecte_output` |

Pas de checkpoint en §1 (saturation auto), §4 (fact-check auto), §5 (drafting auto), §6 (audit/auto).

```mermaid
---
title: SUBLIMATOR v33.1 — Topologie avec checkpoints
config:
  theme: base
  themeVariables:
    primaryColor: "#fff5e6"
    primaryBorderColor: "#d4a017"
---
flowchart LR
    P0["§0 Censeur"]:::phase --> CP1{{"CP1<br/>V/M/R/E"}}:::cp
    CP1 --> P1["§1 Corpus"]:::phase
    P1 --> G1[/"G1"/]:::gate
    G1 --> P2["§2 Dialecticien"]:::phase
    P2 --> CP2{{"CP2<br/>V/M/R/E"}}:::cp
    CP2 --> P3["§3 Architecte"]:::phase
    P3 --> CP3{{"CP3<br/>V/M/R/E"}}:::cp
    CP3 --> P4["§4 Fact-Check"]:::phase
    P4 --> G4[/"G4"/]:::gate
    G4 --> P5["§5 Rédacteur"]:::phase
    P5 --> P6["§6 Audit"]:::phase

    classDef phase fill:#e6f0ff,stroke:#0066cc
    classDef cp fill:#fff5e6,stroke:#d4a017,stroke-width:3px
    classDef gate fill:#e6ffe6,stroke:#009900
```

### 5.2 Légende

- `§N` = phase productrice, instancie un ou plusieurs agents
- `GN` = gate auto, vérifie les critères, déclenche retry/Auditeur/HALT
- `retry × N` = re-instanciation de l'agent avec contexte enrichi (failure_reason + artefact précédent)
- `AUDITEUR` = agent antagoniste aveugle (cf. §1.2.8), appelé après épuisement des retries
- `HALT` = arrêt propre, écriture du `state.errors`, attente d'instruction humaine pour reprise

### 5.3 Parallélisme autorisé

| Phase | Agents parallélisables | Condition |
|---|---|---|
| §1 | `censeur` + `corpus-consultant` | Le Censeur attend le résultat du corpus-consultant avant de marquer [ACQUIS] (synchronisation sur tag) |
| §6 | `auditeur` + `titre-createur` | Indépendants : l'un lit le draft, l'autre génère 9 propositions de titre |

Toutes les autres phases sont séquentielles.

### 5.4 Branches conditionnelles

- **Profil détecté = C en §0** : le Censeur peut sauter §1.2 DIGEST et fusionner Census+Digest dans `01_T1_BRIEF.md` (cf. §0 v32.0 Profil C, conservé). G1 reste obligatoire.
- **`n_articles_pertinents == 0` en §1.1b** : `corpus_consultant_output` peut être `null` sans bloquer G1. Le marqueur [ACQUIS] est simplement absent.
- **Token budget atteint 95 %** : halte préventif, sortie de l'orchestrateur, pas de publication.

### 5.5 État final (succès)

Quand G6 = PASS :

```yaml
final_state:
  phases_completed: ["§0", "G0", "§1", "G1", "§2", "G2", "§3", "G3", "§4", "G4", "§5", "G5", "§6", "G6"]
  article_path: "articles/YYYY-MM-DD_HH-MM_<sujet>_ARTICLE.md"
  audit_log_path: "investigations/<sujet>/_state/audit_<session_id>.ndjson"
  state_path: "investigations/<sujet>/_state/state_<session_id>.yaml"
  gates_results: {G0..G6: {status: "PASS", retries: ≤2}}
  token_budget: {used: ≤cap, percentage: ≤1.0}
```

---

## §6 RUNTIME_CONFIG

### 6.1 Schéma

```yaml
runtime_config:
  spec_version: "33.1"            # figé
  investigation_path: string       # chemin absolu vers le dossier investigation
  corpus_index: string             # chemin vers substack-online/index.md
  profil_auto_detect: boolean      # défaut : true (le Censeur détecte le profil)
  saturation_target: float         # défaut : 0.80
  max_retries_per_gate: integer    # défaut : 2 (override par gate possible)
  enable_auditeur: boolean         # défaut : true
  token_budget:
    cap: integer                   # défaut : 200000
    warning_threshold: float       # défaut : 0.80
  parallelism:
    - phase: "§1"
      agents: ["censeur", "corpus-consultant"]
    - phase: "§6"
      agents: ["auditeur", "titre-createur"]
  output_paths:
    article: "articles/YYYY-MM-DD_HH-MM_<sujet>_ARTICLE.md"
    state: "investigations/<sujet>/_state/state_<session_id>.yaml"
    audit_log: "investigations/<sujet>/_state/audit_<session_id>.ndjson"
```

### 6.2 Trois exemples

#### Exemple A — Enquête lourde (Profil A, FACT_REGISTRY complet)

```yaml
runtime_config:
  spec_version: "33.1"
  investigation_path: "investigations/2026-06-06_sujet_lourd/"
  corpus_index: "substack-online/index.md"
  profil_auto_detect: true
  saturation_target: 0.85
  max_retries_per_gate: 2
  enable_auditeur: true
  token_budget: {cap: 250000, warning_threshold: 0.80}
  parallelism:
    - phase: "§1"
      agents: ["censeur", "corpus-consultant"]
    - phase: "§6"
      agents: ["auditeur", "titre-createur"]
  output_paths:
    article: "articles/2026-06-06_14-30_sujet_lourd_ARTICLE.md"
    state: "investigations/2026-06-06_sujet_lourd/_state/state_<uuid>.yaml"
    audit_log: "investigations/2026-06-06_sujet_lourd/_state/audit_<uuid>.ndjson"
```

#### Exemple B — Enquête standard (Profil B, sans FACT_REGISTRY)

```yaml
runtime_config:
  spec_version: "33.1"
  investigation_path: "investigations/2026-06-06_sujet_standard/"
  corpus_index: "substack-online/index.md"
  profil_auto_detect: true
  saturation_target: 0.80
  max_retries_per_gate: 2
  enable_auditeur: true
  token_budget: {cap: 200000, warning_threshold: 0.80}
  parallelism:
    - phase: "§1"
      agents: ["censeur", "corpus-consultant"]
    - phase: "§6"
      agents: ["auditeur", "titre-createur"]
```

#### Exemple C — Enquête légère (Profil C, prose seule, fast-track)

```yaml
runtime_config:
  spec_version: "33.1"
  investigation_path: "investigations/2026-06-06_sujet_leger/"
  corpus_index: "substack-online/index.md"
  profil_auto_detect: true
  saturation_target: 0.75           # seuil abaissé pour prose seule
  max_retries_per_gate: 2
  enable_auditeur: true
  token_budget: {cap: 150000, warning_threshold: 0.75}
  parallelism:
    - phase: "§1"
      agents: ["censeur", "corpus-consultant"]
    - phase: "§6"
      agents: ["auditeur", "titre-createur"]
  # Profil C : fast-track T1_BRIEF activé (cf. §5.4)
  fast_track: true
```

---

## §7 VALIDATION A/B

### 7.1 Protocole

Trois articles pilotes, A/B contre v32.0. Pour chaque article, deux versions produites en parallèle par deux instances distinctes de l'orchestrateur (une avec spec_version: "32.0", une avec spec_version: "33.0"). Audit externe compare.

### 7.2 Sélection des pilotes

| # | Type de sujet | Profil v32.0 visé | But du test |
|---|---|---|---|
| Pilote 1 | Enquête lourde existante avec FACT_REGISTRY | A | Valider le fast-track Profil A, vérifier que les F### ne sont pas renumérotés en D### |
| Pilote 2 | Enquête standard avec MANIPULATION_REPORT mais sans FACT_REGISTRY | B | Valider que le Censeur + corpus-consultant produisent un digest cohérent |
| Pilote 3 | Enquête légère (prose seule) | C | Valider le fast-track T1_BRIEF, vérifier que la saturation abaissée (0.75) tient |

### 7.3 Critères d'évaluation (note /10 par critère, pondéré)

| Critère | Poids | Outil d'évaluation |
|---|---|---|
| Conformité LOIS 1-12 | 0.25 | lint-article.sh (L2, L3, L6, L8, L9, L11) + Auditeur (L1, L4, L5, L7, L10, L12) |
| Qualité narrative (thèse, fluidité, rythme, micro-définitions) | 0.20 | Auditeur externe (autre LLM, aveugle) |
| Traçabilité (audit_log complet, sources vérifiables, NDJSON valide) | 0.15 | Script de validation NDJSON + grep URLs |
| Performance tokens (consommation totale) | 0.10 | Compteur `state.token_budget` |
| Performance temps (durée totale du pipeline) | 0.10 | Timestamps `audit_log` |
| Saturation corpus (faits utilisés / faits utiles) | 0.10 | Calcul post-hoc depuis `mapping_table` |
| Robustesse gestion d'échecs (cas adverses injectés) | 0.10 | 2 cas adverses injectés (claim volontairement faux, claim sans source) |

### 7.4 Règle de promotion

```yaml
promotion_rule:
  v33_to_stable:
    condition: "score_v33 ≥ score_v32.0 sur chacun des 3 pilotes"
    tie: "promotion"
    superiority: "promotion + note dans changelog"
    inferiority_on_1_pilote: "v33-beta prolongée, correction, nouvel A/B"
    inferiority_on_2_pilotes: "rollback vers v32.0, refonte v34"
```

`score = Σ(critère × poids)`. Calculé par un script tiers (`tools/scripts/score-a-b.sh`, à écrire).

### 7.5 Statut pendant la phase A/B

```yaml
status:
  label: "BETA"
  banner_in_article: true
  banner_text: "Article produit via SUBLIMATOR v33.0 (spec expérimentale en validation A/B)."
  published_during_ab: true    # autorisé
  disclaimer_position: "footer"
```

### 7.6 Critères d'échec de la v33.0 elle-même (post-A/B)

Si après 6 mois d'usage stable v33.0 :

- reste en BETA (3 A/B non concluants) → **dépréciation**, retour à v32.0 comme engine par défaut
- ne réduit pas la complexité (≥ 600 lignes après 3 mois) → **refonte v34** mandatée
- produit plus d'erreurs en cascade que v32.0 (taux de halte > 30 %) → **rollback** vers v32.0

### 7.7 Coexistence avec v32.0

Pendant la phase A/B et tant que v33.0 n'est pas stable, les deux specs coexistent. Le `runtime_config.spec_version` détermine laquelle est utilisée. v32.0 reste l'engine par défaut (opt-out), v33.0 est opt-in.

```yaml
# Pour utiliser v33.0
runtime_config:
  spec_version: "33.1"

# Pour utiliser v32.0 (défaut)
runtime_config:
  spec_version: "32.0"  # ou omis (défaut implicite)
```

---

## §8 MIGRATION DEPUIS v32.0

### 8.1 Actions sur les fichiers d'engine

| # | Action | Source | Destination |
|---|---|---|---|
| 1 | Renommer | `tools/engines/SUBLIMATOR_v28.0.md` (contient v32.0) | `tools/engines/_archive_SUBLIMATOR_v32.0.md` |
| 2 | Renommer | `tools/engines/SUBLIMATOR_v28.0 copy.md` (contient v31.0) | `tools/engines/_archive_SUBLIMATOR_v31.0.md` |
| 3 | Corriger H1 parasite | `tools/engines/promptsmith-leonardo-v4.md` ligne 1 | Retirer la mention "SUBLIMATOR v29.0" (collision de noms) |
| 4 | Créer | — | `tools/engines/SUBLIMATOR_v33.0_spec_agent.md` (ce fichier) |
| 5 | Vérifier linter | `tools/scripts/lint-article.sh` | Compatible v33.0 (règles L2, L3, L6, L8, L9, L11) |
| 6 | Vérifier glossaire | `tools/engines/glossaire-anglicismes.md` | Référencé par L4, à jour |

### 8.2 Mise à jour AGENTS.md

Ajouter dans la section `## Convention de Nommage` ou créer une section dédiée :

```markdown
## Engines disponibles
- **SUBLIMATOR v33.0** (`tools/engines/SUBLIMATOR_v33.0_spec_agent.md`) — engine par défaut pour les nouveaux articles (BETA, A/B contre v32.0)
- **SUBLIMATOR v32.0** (`tools/engines/_archive_SUBLIMATOR_v32.0.md`) — archivé, encore utilisable via `runtime_config.spec_version: "32.0"`
```

### 8.3 Rétrocompatibilité

Les investigations en cours au moment de la bascule v33.0 :

- Si l'investigation a un `_state/state_*.yaml` au format v32.0 → re-censer avec Censeur v33.0 (équivalent §0), repartir de zéro
- Si l'investigation a un brouillon dans `_assemblage/` → passer en mode révision (Profil D, conservé v32.0)

### 8.4 Pas de script de migration automatique

La complexité des états v32.0 (5 phases, 6 CPs, 4 profils) ne se mappe pas 1-1 vers v33.0 (5 phases, 7 gates, profil runtime). Toute migration automatique risque de perte de données. **Recommandation** : repartir d'un state neuf par investigation. L'ancien state est archivé pour traçabilité.

---

## §9 CHANGELOG

```
v33.0 "L'Orchestrateur" — 2026-XX-XX
─────────────────────────────────────
+ Spec purement agent (suppression cible humaine)
+ Validation hybride (lint outillage + multi-agent sémantique)
+ Chorégraphie dynamique : registre 9 agents instanciés à la demande
+ 7 gates auto (remplacement 6 CPs manuels)
+ Profils runtime (remplacement 4 profils hardcodés)
+ État sérialisable YAML (multi-session resume via _state/)
+ Stratégie d'échec explicite (retry N → auditeur → halte propre)
+ Budget tokens cap + warning + halte préventif
+ 12 LOIS conservées, format déclaratif YAML
+ Audit log NDJSON append-only
+ Validation A/B vs v32.0 sur 3 pilotes (critère de promotion)
− §5.5 mise à jour post-publication (hors scope agent)
− §6.5 CP#5 manuel (remplacé par G6)
− §6.3 audit stylistique manuel (absorbé par Auditeur + lint)
− Axiome "L'utilisateur = garde-fou" → "L'orchestrateur est le seul juge"
− 4 profils hardcodés (transformés en runtime_config.profil_auto_detect)
− 6 CPs manuels (remplacés par 7 gates auto)
− 825 lignes → 550 lignes (cible)

v33.1 "L'Orchestrateur + Humain" — 2026-06-06
─────────────────────────────────────────────
+ 3 checkpoints structurés (CP1 §0, CP2 §2, CP3 §3) avec 4 actions V/M/R/E
+ 2 nouvelles LOIS : L13 (CP obligatoire) + L14 (boucle bornée 3 max)
+ Slot `checkpoints` dans le schéma d'état §4.2
+ §4.4.bis algorithme checkpoint.executor()
+ §4.7 events NDJSON `checkpoint` + `checkpoint_input`
+ §5.1.bis table 3 CP + diagramme mermaid topologique
+ §10 CHECKPOINTS section dédiée (7 sous-sections)
+ §9.5 Checkpoints humains dans le guide compagnon

Type : mineur (rétrocompatible)
Migration : aucune action requise (fallback CP validate sur state v33.0)
Test A/B : Sumer/France 2026 rejoué pour mesurer apport CP
```

**Légende** : `+` ajout, `−` suppression/remplacement.

---

*Fin de la spec SUBLIMATOR v33.0. Statut : BETA. Promotion v33-stable conditionnée par A/B réussi sur 3 pilotes.*

---

## §10 CHECKPOINTS (v33.1+)

### 10.1 Principe

Les 3 checkpoints (CP1 §0, CP2 §2, CP3 §3) sont des points d'insertion **obligatoires et bloquants** où l'humain arbitre la sortie de l'agent amont avant passage à l'agent aval. Implémentés via question tool, format V/M/R/E.

L'axiome « L'orchestrateur est le seul juge » (v33.0) est préservé : l'orchestrateur arbitre les critères, l'humain arbitre les choix sémantiques. Les deux juges sont complémentaires, pas concurrents.

### 10.2 Les 4 actions

#### Valider (V)
- L'agent continue avec la sortie actuelle
- Trace : `{"event":"checkpoint","phase":"§X","action":"validate",...}`
- Effet : passage à la phase suivante

#### Modifier (M)
- L'agent pose : « Colle ta version modifiée »
- L'humain colle texte libre OU YAML structuré
- L'agent remplace sa sortie par la version humaine
- Trace : `{"event":"checkpoint","action":"modify","payload_size":N,...}`
- Effet : phase reprend avec nouvel input, recalcul gates si impact

#### Refuser (R)
- L'agent retourne à la phase précédente
- `n_refus_consecutifs += 1`
- Trace : `{"event":"checkpoint","action":"refuse","n_refus_consecutifs":N,...}`
- Effet : retry phase avec **nouveaux inputs** (sortie précédente invalidée), max 3

#### Enrichir (E)
- L'agent pose : « Colle tes ajouts (F### externes, thèses, sections) »
- L'humain colle YAML/texte
- L'agent **fusionne** (sans remplacer) ses outputs + ajouts (LLM-driven merge, halte + sous-question si contradiction)
- Trace : `{"event":"checkpoint","action":"enrich","n_inputs_added":N,...}`
- Effet : phase reprend avec inputs augmentés

### 10.3 Boucle bornée (L14)

Compteur `n_refus_consecutifs` reset à 0 sur V/M/E. Si == 3 → HALTE pipeline + bilan explicite, état préservé pour reprise manuelle.

### 10.4 Cascade

| CP modifié | Impact aval |
|---|---|
| §0 | Reset §1 à §6 (portée changée) |
| §2 | §1 OK, reset §3 à §6 (nouvelle cardinale) |
| §3 | §1, §2 OK, reset §4 à §6 (nouveau plan) |

### 10.5 Question type (template)

```
L'agent a produit [description courte, 2-3 phrases].

Options :
1. Valider — continuer avec cette sortie
2. Modifier — coller ta version
3. Refuser — retour à [phase précédente]
4. Enrichir — ajouter des inputs
```

### 10.6 Rétrocompatibilité

state_*.yaml v33.0 sans slot `checkpoints` → fallback CP validate (aucune interférence). Les runs anciens continuent de fonctionner comme v33.0. La migration v33.0 → v33.1 est **transparente** : pas de script de migration, pas d'action manuelle requise sur les state existants.

### 10.7 Test live A/B

Pour valider v33.1 contre v33.0, on relance l'article Sumer/France publié en v33.0 (article `2026-06-06_07-49_sumer_france_bureaucratie_ARTICLE.md`, 4233 mots). L'humain peut utiliser les CP pour :

- **CP1 §0** : élargir la portée de Sumer/France vers comparaisons multi-civilisationnelles (Rome, Chine, Andurarum)
- **CP2 §2** : imposer une thèse cardinale différente de SYSTEME (ex : tester INVERSION ou CAPTURE)
- **CP3 §3** : ajouter/réordonner des sections (ex : insérer une section Andurarum manquante)

Critère de promotion v33.0 → v33.1 : couverture ≥ 80 % des cas de test, score A/B ≥ v33.0 sur 2/3 critères pondérés.

---

*Fin de la spec SUBLIMATOR v33.1. Statut : BETA. Promotion v33-stable conditionnée par A/B réussi sur 3 pilotes avec checkpoints humains.*
