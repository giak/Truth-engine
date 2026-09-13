---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "synthesis"
artifact_id: "INV-102-SYNTHESIS"
version: "1.0"
status: "pass"
updated: "2026-09-10"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-102"
input_gate: "INV-102_SYNTHESIS_INPUT_GATE.md"
---

<!-- TRACE: synthesized_from=INV-093,INV-095,INV-098,INV-099,INV-100 -->
<!-- EXECUTION: truth_engine_search=false; generic_collection=false; dependency_delta_only=true -->
<!-- GUARD: constrained_offer!=no_choice; funding!=command; clientelism!=individual_vote_buying; fraud!=error; fraud!=changed_result; annulment!=instrumentalization; legality!=substantive_legitimacy; abstention_and_strategic_vote=UNRESOLVED_BY_INPUT_SET -->

# INV-102 — Consentement sans choix réel

## 1. Verdict central

Les dépendances établissent plusieurs mécanismes capables de **contraindre, déformer ou neutraliser ponctuellement le choix électoral**, mais elles ne démontrent pas que le consentement électoral français est, de façon générale, un consentement « sans choix réel ».

- `INV-093` montre que le financement électoral structure ressources, règles et contrôles, sans établir `financement -> commandement`, persuasion ou résultat.
- `INV-095` établit des filtres structurels inégaux en ressources, accès, réseaux et visibilité potentielle, sans fermer `filtre -> nomination/exclusion identifiable` ni une architecture coordonnée de présélection.
- `INV-098` établit le vote-buying direct dans des cas précis et des mécanismes plus larges de clientélisme/favoritisme, sans dénominateur national ni effet électoral général.
- `INV-099` établit fraude et erreurs électorales case-specifically, tout en séparant accusation, fréquence, fraude et modification du résultat.
- `INV-100` établit, dans le cas roumain borné, l’annulation comme effet institutionnel certain ; attribution étrangère complète, persuasion, résultat contrefactuel et instrumentalisation intentionnelle ne sont pas fermés.

La synthèse soutient donc un modèle de **choix institutionnellement réel mais exposé à des contraintes hétérogènes**, certaines structurelles, certaines transactionnelles, certaines irrégulières et certaines juridictionnelles. Leur coexistence ne suffit pas à établir un verrou coordonné ni l’absence générale d’alternative substantielle.

```text
ELECTORAL_CHOICE_FORMALLY_EXISTS                 = NOT_REFUTED_BY_DEPENDENCIES
UPSTREAM_RESOURCE/ACCESS_CONSTRAINTS              = ESTABLISHED / PARTIAL to candidate selection
VOTE_BUYING                                      = ESTABLISHED case-specifically
CLIENTELISM/POLITICAL_FAVORITISM                  = ESTABLISHED in bounded mechanisms
ELECTORAL_FRAUD                                  = ESTABLISHED case-specifically
ERROR != FRAUD                                   = ESTABLISHED distinction
INSTITUTIONAL_ANNULMENT_CAN_NULLIFY_CAST_CHOICE   = ESTABLISHED case-specifically
GENERAL_COORDINATED_CHOICE_LOCK                   = NOT_ESTABLISHED
GENERAL_NO_REAL_CHOICE                            = NOT_ESTABLISHED
ABSTENTION_MECHANISM                              = UNRESOLVED_BY_INPUT_SET
STRATEGIC_VOTING_MECHANISM                        = UNRESOLVED_BY_INPUT_SET
GENERAL_CAUSAL_LEGITIMACY_EFFECT                  = NOT_ESTABLISHED
```

## 2. Modèles concurrents

### M1 — Choix réel sous contraintes normales et inégales
**SUPPORTED/PARTIAL.** Les électeurs disposent d’un choix institutionnel, mais l’offre et les ressources ne sont pas distribuées uniformément. Les dépendances ne donnent pas de critère empirique permettant de transformer toute inégalité en absence de choix.

### M2 — Déformations ponctuelles et sectorielles du consentement
**SUPPORTED.** Vote-buying, clientélisme, fraude, erreurs et annulations peuvent affecter des individus, scrutins ou décisions institutionnelles. Leurs mécanismes, standards juridiques et effets sont non isomorphes et doivent rester séparés.

### M3 — Verrou structurel cumulatif de l’offre
**UNRESOLVED.** `INV-095` établit des filtres amont mais pas leur conversion générale en nomination/exclusion. Aucun dénominateur national de candidats potentiels, alternatives éliminées ou sélection organisationnelle ne ferme la thèse d’un verrou de l’offre.

### M4 — Architecture coordonnée supprimant le choix réel
**NOT_ESTABLISHED.** Aucun ensemble de dépendances ne démontre une coordination transversale reliant financeurs, structures de sélection, clientélisme, fraude et interventions institutionnelles en un mécanisme commun de neutralisation du consentement.

## 3. Chaînes probatoires distinctes

- `ressources/règles -> capacité de campagne` = **SUPPORTED**, mais `-> commandement/sélection` non fermé.
- `filtres sociaux/réseaux/visibilité -> opportunité d’accès` = **SUPPORTED/PARTIAL**, mais `-> nomination/exclusion` non fermé.
- `avantage ciblé/transaction -> vote individuel` = **VERIFIED case-specifically** pour vote-buying ; non généralisable au clientélisme agrégé.
- `fraude -> irrégularité juridiquement qualifiée` = **VERIFIED case-specifically** ; `-> résultat changé` non automatique.
- `annulation -> effet institutionnel sur le scrutin` = **VERIFIED case-specifically** ; `-> instrumentalisation` non établie.
- `ensemble de ces mécanismes -> absence générale de choix réel` = **NOT_ESTABLISHED**.

## 4. Revue contradictoire / plafond causal

`P0=0 / P1=0 / P2=4`.

1. **COVERAGE** — abstention et vote stratégique sont au titre mais ne sont pas directement traités par les cinq entrées ; aucune conclusion n’est autorisée sur ces mécanismes.
2. **DENOMINATOR** — absence de dénominateur commun permettant d’estimer combien de choix/candidatures/votes sont matériellement affectés par chaque mécanisme.
3. **COMPOSITION** — additionner sélection amont, clientélisme, fraude et annulation comme s’ils formaient un mécanisme coordonné violerait l’isomorphie probatoire.
4. **LEGITIMACY/CAUSALITY** — aucune métrique ou design causal commun ne transforme les effets bornés en mesure générale du caractère « réel » du choix ou de la légitimité du consentement.

## 5. RENARD

`NO`.

Une collecte générique supplémentaire ne réparerait pas les plafonds. Une réouverture nécessiterait au minimum des designs dédiés sur l’offre/candidature, l’abstention et le vote stratégique, des dénominateurs nationaux comparables pour fraude/clientélisme, ou un design causal liant contrainte identifiée à choix disponible, comportement et résultat.

## 6. Route

- `INV-102 -> CLOSED / SYNTHESIS_PASS / NOT_RUN_BY_DESIGN`.
- Résultat borné vers `INV-133`.
- La formule « consentement sans choix réel » reste une **hypothèse de modèle non établie**, pas une conclusion du corpus fermé.
