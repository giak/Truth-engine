---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "synthesis"
artifact_id: "INV-095-SYNTHESIS"
version: "1.0"
status: "pass"
updated: "2026-09-10"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-095"
input_gate: "INV-095_SYNTHESIS_INPUT_GATE.md"
---

<!-- TRACE: synthesized_from=INV-093,INV-094,INV-119,INV-081 -->
<!-- EXECUTION: truth_engine_search=false; generic_collection=false; dependency_delta_only=true -->
<!-- GUARD: funding!=command; foreign_flow!=tasking; ownership!=editorial_control; elite_network!=coordination; access!=candidate_selection; structural_filter!=coordinated_gatekeeping; correlation!=causality -->

# INV-095 — Sélection des candidats avant l’élection

## 1. Verdict central

Les quatre dépendances établissent plusieurs **filtres et capacités structurels en amont de la compétition électorale**, mais elles ne ferment pas une architecture coordonnée de présélection des candidats.

- `INV-093` établit un système français de financement électoral multicanal, réglementé et contrôlé, avec des irrégularités et montages illicites dans des cas précis. Il ne ferme pas `financement -> commandement politique`, persuasion ou résultat électoral.
- `INV-094` établit que des flux étrangers peuvent créer capacité, dépendance ou accès potentiel, mais que l’origine étrangère, l’illégalité, le tasking et l’effet électoral sont des objets distincts.
- `INV-119` établit une forte reproduction sociale vers les filières sélectives, des pipelines d’accès à la haute fonction publique et des circulations public-privé historiques, sans fermer `réseau -> agenda commun -> coordination` ni `revolving door -> décision capturée`.
- `INV-081` établit une concentration économique médiatique mesurable sous métrique/univers/date explicites, mais pas l’usage éditorial de cette propriété ni `propriété/financement -> contrôle éditorial`.

La conclusion robuste est donc : **l’environnement de sélection est structurellement inégal en ressources, accès, réseaux et capacités de visibilité, mais le corpus fermé ne démontre ni un mécanisme général de veto/nomination exercé par ces acteurs, ni une coordination transversale qui présélectionnerait les candidats avant le vote.**

```text
STRUCTURAL_RESOURCE_FILTERS                    = ESTABLISHED / heterogeneous
ELITE_SOCIAL_SELECTION_AND_ACCESS              = ESTABLISHED
MEDIA_ECONOMIC_CONCENTRATION                    = ESTABLISHED / bounded
FOREIGN_FINANCE_AS_CAPACITY_OR_DEPENDENCE       = ESTABLISHED case-specifically
RESOURCE/NETWORK/OWNERSHIP -> CANDIDATE_ACCESS  = PARTIAL / indirect only
CANDIDATE_NOMINATION_OR_EXCLUSION_CAUSAL_EDGE   = NOT_ESTABLISHED generally
TRANSVERSAL_TASKING_OR_VETO_ARCHITECTURE        = NOT_ESTABLISHED
COORDINATED_PRE_ELECTION_SELECTION_SYSTEM       = NOT_ESTABLISHED
DOWNSTREAM_ELECTORAL_COUNTERFACTUAL             = NOT_ESTABLISHED
```

## 2. Modèles concurrents

### M1 — Compétition pluraliste sous contraintes inégales
**SUPPORTED.** Les règles, ressources, trajectoires sociales, réseaux professionnels et structures de propriété distribuent inégalement capacités et accès. Ce modèle n’exige ni centre de commandement ni coordination.

### M2 — Filtrage structurel cumulatif
**SUPPORTED/PARTIAL.** Plusieurs filtres indépendants peuvent se cumuler et rendre certaines trajectoires plus probables que d’autres. Le cumul de contraintes est plausible et partiellement documenté, mais les dépendances ne fournissent pas un dénominateur commun de candidats potentiels ni une chaîne complète jusqu’à nomination/exclusion.

### M3 — Captures sectorielles ou cooptations ponctuelles
**UNRESOLVED.** Des mécanismes de conflit, accès privilégié, financement ou concentration peuvent créer des opportunités de capture. Aucun dossier dépendant ne ferme une chaîne bornée `acteur/intérêt -> intervention -> choix de candidat -> décision organisationnelle` permettant de généraliser.

### M4 — Architecture coordonnée de présélection
**NOT_ESTABLISHED.** Aucun corpus terminal ne montre un dispositif transversal où financeurs, propriétaires de médias, grandes écoles, réseaux administratifs et partis exerceraient ensemble un veto ou un tasking coordonné sur les candidatures.

## 3. Registre causal de synthèse

- `origine sociale favorisée -> probabilité supérieure d’accès aux filières sélectives -> accès élitaire` = **SUPPORTED**.
- `école/corps/trajectoire -> contacts et opportunités de circulation` = **SUPPORTED**, mais `network != coordination`.
- `propriété/financement médiatique -> ressources/capacité de diffusion` = **SUPPORTED/PARTIAL selon métrique**, mais `ownership != editorial_control`.
- `financement électoral -> capacité financière/règles/contrôle` = **SUPPORTED**, mais `funding != command`.
- `flux étranger -> capacité/dépendance potentielle` = **SUPPORTED case-specifically**, mais `foreign_flow != tasking`.
- `ressource + réseau + visibilité -> sélection d’un candidat identifiable` = **UNRESOLVED**.
- `financeur/propriétaire/réseau -> veto, nomination ou exclusion identifiable` = **UNRESOLVED**.
- `filtres structurels -> résultat électoral contrefactuel` = **NOT_ESTABLISHED**.

## 4. Revue contradictoire / plafond causal

`P0=0 / P1=0 / P2=4`.

1. **SELECTION EDGE** — aucun dénominateur de candidats potentiels, shortlist, vote d’investiture ou décision organisationnelle comparable ne ferme le passage de l’accès à la sélection effective.
2. **RESPONSIBILITY** — financement, propriété, réseau et proximité ne fournissent pas de tasking, veto ou contrôle attribuable sans pièces supplémentaires.
3. **COORDINATION** — la coexistence de filtres structurels n’établit pas une architecture coordonnée ; une émergence cumulative reste une explication rivale suffisante.
4. **EFFECT** — aucun design ne mesure le contre-factuel `sans ces filtres -> autre offre de candidats -> autre résultat démocratique`.

## 5. RENARD

`NO`.

La collecte générique supplémentaire serait cumulative. Réouvrir seulement sur : données de sélection interne de partis avec dénominateur et décisions ; communications authentifiées de tasking/veto/contrepartie ; footprints versionnés reliant intervention à nomination/exclusion ; ou design causal/comparatif reliant filtre amont à entrée/sortie effective de candidats.

## 6. Route

- `INV-095 -> CLOSED / SYNTHESIS_PASS / NOT_RUN_BY_DESIGN`.
- Le résultat alimente directement `INV-102` et `INV-133`.
- Aucun nouveau PRIMARY|CASE n’est créé par la seule convergence de filtres.
