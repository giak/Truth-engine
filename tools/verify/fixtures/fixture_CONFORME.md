# Investigation : parution de « La Police parisienne et les Algériens (1944-1962) » de Blanchard

FICHIER : 2026-08-18_17-09_blanchard-police-algeriens-2011_INVESTIGATION.md

## Manifeste

| Champ | Valeur |
|-------|--------|
| ENGINE_VERSION | 2.8 |
| STATE | FINAL |
| NEXT_ACTION | NONE |
| RUN_ID | 20260818-1709-blanchard-police-algeriens-2011 |
| PARENT_RUN_ID | NONE |
| AS_OF | 2026-08-18 |
| INPUT_KIND | CLAIM |
| MISSION_MODE | VERIFY_ONLY |
| INPUT_REF | NONE |
| SUBJECT_SLUG | blanchard-police-algeriens-2011 |
| SCOPE | LEAD_QUESTION: année et éditeur de parution ; OBJECT_QUESTION: référence bibliographique exacte ; période: 2011 ; géo: France |
| COMPLEXITY | SIMPLE |
| CHECKPOINT_SEQ | 0 |
| LAST_COMPLETED | 18b |
| RESUME_COUNT | 0 |
| ROUTE_OVERRIDES | [] |
| LOADED_MODULES | [] |
| DEGRADED_FLAGS | [] |

## Pipeline KERNEL (trace)

ANALYZE : 15 symboles narratifs scorés : Ξ Omission 0, € Money 0, Λ Framing 0, Ω Inversion 0, Ψ Sideration 0, ↕ Vertical power 0, Φ Spectacle 0, Σ Semiotics 0, Κ Cynicism 0, ρ Resistance 1 (recensions académiques indépendantes), κ Subtle influence 0, ⫸ Convergence 2 (éditeur et revues concordent sur 2011), ⚔ Cognitive warfare 0, 🌐 Network 0, ⏰ Temporal 1 (la date de parution est l'objet du claim).
PATTERNS : aucun. THREATS : aucun. RHETORICAL : N/A. COMPLEXITY : 1 → SIMPLE.

BIAS_TEST : sur les sources collectées (directness, provenance, method, interests, independence, relevance) :
- SRC-001 (Nouveau Monde Éditions, page catalogue) : ◈ primary pour « l'éditeur déclare septembre 2011 » ; provenance directe ; intérêt commercial (catalogue) → corroboration indépendante requise.
- SRC-002 (La Vie des Idées, recension de Muriel Cohen, 24 avril 2012) : ◉ analytique ; provenance éditoriale indépendante de l'éditeur ; méthode de recension académique ; intérêt nul sur la date de parution.
Indépendance : aucune filiation capitalistique entre l'éditeur et La Vie des Idées. Pertinence : les deux sources portent précisément sur l'objet du claim.

CRÉDO/SCOPING : LEAD_QUESTION « l'ouvrage de Blanchard est-il paru en 2011 aux éditions Nouveau Monde ? » ; OBJECT_QUESTION « référence bibliographique exacte de La Police parisienne et les Algériens (1944-1962) ».

LEAD_REGISTRY : LEAD-001 (page catalogue de l'éditeur, Nouveau Monde Éditions), LEAD-002 (recension La Vie des Idées, Cohen 2012).

CLAIM_REGISTRY : CLAIM-001 (« l'ouvrage est paru en 2011 aux éditions Nouveau Monde ») → FCT-001.

EVIDENCE_REGISTRY : EVIDENCE-001 (page éditeur, extrait « septembre 2011, ISBN 9782847366273, 450 pages », fetché HTTP 200), EVIDENCE-002 (La Vie des Idées, extrait « Paris, Nouveau Monde éditions, 2011, 447 p. », fetché HTTP 200).

TRACE : F-001 → QRY-001 → SRC-001 → FCT-001 → vérifié L4.

## RÉSUMÉ EXÉCUTIF

Le claim est CONFIRMÉ : l'ouvrage d'Emmanuel Blanchard, La Police parisienne et les Algériens (1944-1962), est paru en septembre 2011 aux éditions Nouveau Monde. Deux familles indépendantes concordent : la page catalogue de l'éditeur (SRC-001) et la recension de La Vie des Idées (SRC-002). Aucune édition de 2021 ni réédition ultérieure n'a été trouvée lors de la recherche de contre-exemples.

## CHRONOLOGIE

- 2011-09 : parution de l'ouvrage chez Nouveau Monde Éditions (SRC-001).
- 2012-04-24 : recension de Muriel Cohen dans La Vie des Idées, confirmant « Paris, Nouveau Monde éditions, 2011 » (SRC-002).

## DOMAINES

- BIBLIOGRAPHIE : référence exacte de l'ouvrage.
- HISTOIRE : contexte d'étude (police parisienne et population algérienne, 1944-1962), hors périmètre du claim.

## CARTE DES PREUVES

- F-001 → FCT-001 (tier 1) : date et éditeur de parution, corroborés par deux familles (éditeur + revue indépendante), dates concordantes.

LEAD_COVERAGE :

| LED-ID | Résultat |
|--------|----------|
| LEAD-001 | SATURATED : extrait de parution confirmé. |
| LEAD-002 | SATURATED : recension confirmant la parution. |

OBJECT_COVERAGE :

| Objectif | Résultat |
|----------|----------|
| Référence bibliographique exacte | SATURATED : titre, auteur, éditeur, année, ISBN. |

INVESTIGATION_MAP :

| AXS-ID | ATTEMPT_IDS | Résultat |
|--------|-------------|----------|
| AXS-BIBLIO | QRY-001 | FCT-001 ✦ |

FACT_REGISTRY_V1 :

| id | epi | tier | url | families | date |
|----|-----|------|-----|----------|------|
| FCT-001 | FACT | 1 | https://www.nouveau-monde.net/catalogue/la-police-parisienne-et-les-algeriens-1944-1962/ | editeur;revue | 2026-08-18 |

TRACE_MATRIX :

| Fait | Claim | Évidence | Statut |
|------|-------|----------|--------|
| F-001 | CLAIM-001 | EVIDENCE-001, EVIDENCE-002 | ✦ CONFIRMED |

## PÉRIMÈTRE & LIMITES

- Périmètre : uniquement le fait matériel de publication (année, éditeur, ISBN), pas le contenu de l'ouvrage ni l'histoire du 17 octobre 1961.
- Limite : le nombre de pages varie selon les sources (450 chez l'éditeur, 447 dans la recension, 448 dans une autre recension). Cette divergence de pagination n'affecte pas le claim borné (année et éditeur) et n'est pas retenue comme contradiction matérielle.
- Limite : la recension La Vie des Idées est une traduction anglaise de la version française ; la donnée bibliographique citée est identique.

## SOURCES

- SRC-001 : Nouveau Monde Éditions, page catalogue « La police parisienne et les Algériens (1944-1962) », extrait « Emmanuel BLANCHARD, septembre 2011, ISBN : 9782847366273, 450 pages » (https://www.nouveau-monde.net/catalogue/la-police-parisienne-et-les-algeriens-1944-1962/).
- SRC-002 : Muriel Cohen, « New Light on a Colonial Massacre », La Vie des Idées, 24 avril 2012, extrait « Reviewed: Emmanuel Blanchard, La Police parisienne et les Algériens (1944-1962), Paris, Nouveau Monde éditions, 2011, 447 p. » (https://laviedesidees.fr/New-Light-on-a-Colonial-Massacre).

## REQUEST_LOG

- QRY-001 : fetch de la page catalogue de l'éditeur (2026-08-18, 17:05 CEST) → FCT-001 (extrait SRC-001).
- QRY-002 : fetch de la recension La Vie des Idées (2026-08-18, 17:06 CEST) → FCT-001 (extrait SRC-002).
- QRY-003 : recherche de contre-exemple « Blanchard "La police parisienne et les Algériens" réédition 2021 édition ultérieure » (2026-08-18, 17:07 CEST) → aucune édition 2021 ni réédition trouvée ; les résultats ne citent que 2011.

## Preuves matérielles L4 (gate EPI=FACT)

- FCT-001 : gate EPI=FACT, 2 familles (éditeur + revue indépendante), sources fetchées SRC-001 et SRC-002 avec extraits littéraux cités dans SOURCES, recherche de contre-exemple exécutée (QRY-003) et documentée, aucun contre-exemple trouvé.
