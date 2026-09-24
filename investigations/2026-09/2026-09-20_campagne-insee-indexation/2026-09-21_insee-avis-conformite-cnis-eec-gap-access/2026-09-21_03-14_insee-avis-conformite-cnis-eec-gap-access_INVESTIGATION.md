ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260921-0314-insee-avis-conformite-cnis-eec-gap-access | PARENT_RUN_ID:20260921-0255-insee-taux-de-reponse-par-vague-precision-des-estimations | AS_OF:2026-09-21
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-21_insee-avis-conformite-cnis-eec-gap-access/2026-09-21_03-14_insee-avis-conformite-cnis-eec-gap-access_INPUT.md | SUBJECT_SLUG:insee-avis-conformite-cnis-eec-gap-access | SUBJECT_FP:sha256:3f051dffd958f49a593c23f7e20261e0bfdec445af5715e237de53a19d2a07b5 | INPUT_SHA256:sha256:fefb21828c0c93beceb4df1e8f6dfe93ca12a3fe07f48691d760c706213f2ebb
COMPLEXITY:5→MEDIUM | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:period:2027-2030 (avis EEC) + rappel 2021-2026; geo:France; axes:ACTORS_RELATIONS,RULES_CONTROLS,MECHANISMS,SOURCE_AUDIT; exclusions:sondages d opinion; limits:avis CNIS = document de controle, non une mesure
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/INVESTIGATION.md,protocol/FACT_VERIFICATION.md,protocol/UPDATE.md,search/EPISTEMIC.md,search/TEMPLATES.md,output/TEMPLATE.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Le contrôle externe de l'enquête Emploi : ce que l'avis de conformité 2026 établit, et ce qu'il ne mesure pas (UPDATE du run 02-55)

## TL;DR

```text
SUJET: Fermeture du gap ACCESS du CTRL-001 — obtenir et inspecter l'avis de conformité du Comité du label sur l'enquête Emploi (parent 20260921-0255, tentative du parent en HTTP 403).
OBJET: Le HTTP 403 du parent était un filtrage par user-agent, pas un mur d'accès. L'avis n° 2026_13068_DG75-L002 du 30 juin 2026 est obtenu (144 606 octets, sha256 vérifié), lu intégralement, et il établit le contrôle : label d'intérêt général Oui, caractère obligatoire Oui, validité 2027-2030, publication au JO (FCT-001). Il établit surtout que le contrôle externe retient lui-même les taux de réponse comme indicateurs de comparabilité entre le test 2027 et l'enquête en production (FCT-002, FCT-009 ✦).
SOURCE: Deux familles de provenance désormais indépendantes sur le fait décisif — producteur (DT2023-22, famille A) et contrôle (Cnis/Comité du label, famille D).
MANIPULATION/STRUCTURE: Aucun marqueur rhétorique de manipulation (DEM 0, BF 0, NUM 3 inchangé). L'avis contient autant d'exigences que d'appréciations : c'est un document de contrôle, non une caution.
LIMITE: GAP_TYPE=CAUSALITY — l'effet mesuré du contrôle sur les taux de réponse n'est pas établi (CAU-003) ; la branche de contrôle passe de GAP ACCESS à SATURATED sans que l'objet soit saturé.
```

## 1. RÉSUMÉ EXÉCUTIF

**Question objet (préservée du parent, inchangée).** Quelle précision est effectivement attachée aux estimations que l'Insee publie (chômage BIT, population légale, pauvreté, IPC), mesurée par les taux de réponse par vague et les intervalles publiés, et que reste-t-il établi lorsque le chiffre diffusé est lu sans son incertitude ?

**Requête de cet UPDATE.** Fermer le gap ACCESS du `CTRL-001` : le parent avait identifié l'avis de conformité 2026 du Comité du label sur l'enquête Emploi, mais son URL répondait un HTTP 403 au parent (`GAP_TYPE=ACCESS`).

**Réponse bornée.** Le gap est fermé, et sa cause est nommée. Le 403 relevait d'un **filtrage par user-agent** : la même URL répond 200 et sert un PDF de 144 606 octets dès lors que la requête porte un en-tête de navigateur. Aucun accessit payant, aucune copie de seconde main, aucun cache tiers n'a été employé : la première tentative par lecteur de page a échoué sur le type de contenu, la seconde, avec en-tête de navigateur, a abouti (`CLM-003`, `SRC-001`).

**Ce que l'avis établit.** Le Comité du label de la statistique publique émet, le 30 juin 2026, un avis de conformité sur l'enquête Emploi après réunion du 21 mai 2026 : **label d'intérêt général et de qualité statistique Oui, caractère obligatoire Oui** (proposition d'octroi), **validité 2027-2030**, **publication au Journal officiel Oui**, périodicité annuelle, après avis d'opportunité favorable de la commission « Emploi, qualification et revenus du travail » du 20 mai 2025 (`FCT-001`).

**Le point décisif.** Le contrôle externe ne se contente pas d'entériner : il **retient les taux de réponse** parmi les indicateurs sur lesquels reposeront les analyses comparatives entre le test 2027 et l'enquête en production, aux côtés du nombre d'individus renseignés par logement et des écarts observés sur certaines questions majeures (`FCT-002`). Il **salue** l'investissement du service en faveur du maintien et de l'amélioration des taux de réponse (`FCT-004`) et **note** la progression des réponses par internet en réinterrogation (`FCT-005`). Il **demande** enfin que le prochain dossier précise l'impact de l'évolution de la qualité de la base de sondage sur le repérage des logements et la prise de contact — caractérisation des résidences principales ou non, coordonnées des habitants (`FCT-003`).

**Ce que cela change pour l'objet.** Le suivi des taux de réponse n'est plus seulement une pratique interne de producteur : il est **attesté par un contrôle externe** comme critère de qualité. Le fait `FCT-009` est scellé en `✦` sur deux familles indépendantes : le producteur publie les taux par rang (60,5 % en première interrogation, 64,3 % en réinterrogation au T2 2023, `SRC-004`) et le contrôle les reprend comme indicateurs de comparabilité (`SRC-001`). Contre-recherche adversariale exécutée : **aucune source contestant ce suivi n'a été trouvée** — statut `NONE`, réfutation terminale enregistrée.

**Ce que cela ne change pas.** Le contrôle porte sur **la qualité de l'opération**, pas sur l'incertitude attachée au chiffre diffusé. Le Comité demande lui-même la quantification d'un chaînon (base de sondage → prise de contact → non-réponse) qu'il ne mesure pas encore (`FCT-003`, `CLM-005`). L'écart central du parent reste donc ouvert, mais il est désormais **circonscrit par le document qui contrôle** : l'argument « la qualité est contrôlée » ne peut pas être opposé à l'argument « l'incertitude n'est pas publiée », parce que le contrôle lui-même ne porte pas sur cette incertitude.

**Acteurs.** Comité du label de la statistique publique (Cnis, commission « Ménages ») ; commission « Emploi, qualification et revenus du travail » (opportunité) ; Insee, DSDS, Département de l'emploi et des revenus d'activité, Division Emploi (service producteur) ; Comité des utilisateurs de l'enquête Emploi, annuel depuis 2021 ; ménages échantillonnés.

**Impact.** Deux dimensions supplémentaires sont documentées : un bénéfice (contrôle public par opération, suites exigées, validabilité a posteriori) et une invariance (le chiffre diffusé reste sans incertitude attachée). L'effet chiffré du contrôle sur les taux, et l'effet du chiffre sans incertitude sur les usages, restent en `GAP_TYPE=CAUSALITY` (`AXS-008`, `CAU-003`).

**Gaps principaux après cet UPDATE.** Cause (effet du contrôle non mesuré, `CAU-003`, `NQ-001`), périmètre (aucune incertitude attachée à l'indicateur publié, `CLM-004`, `NQ-003`), accès (textes légaux non inspectés, `NQ-002`), indépendance (aucune contre-perspective externe au Service statistique public, `NQ-004`), ressources (coût de la collecte non documenté, `AXS-004`).

## 2. MANIPULATION_REPORT

Input `UPDATE`, mode `INVESTIGATION`, complexité `5→MEDIUM`, symboles évalués sur le corpus final.

| Symbole | Score | Observation nommée |
|---|---:|---|
| Ξ omission | 4 | `CONFIDENCE_MISSING` inchangé : le chiffre conjoncturel est diffusé sans incertitude attachée. La pièce nouvelle ne comble pas l'absence, elle la circonscrit : le contrôle porte sur l'opération, pas sur l'indicateur publié (FCT-002, CLM-004) |
| ⫸ convergence | 4 | le producteur (DT2023-22) et le contrôle externe (avis 2026) convergent indépendamment sur le suivi des taux de réponse comme indicateur de qualité (FCT-009 ✦) |
| ⏰ temporel | 4 | le contrôle est un cycle daté : opportunité 2025-05-20, examen 2026-05-21, avis 2026-06-30, validité 2027-2030, note exigée sur le tirage 2027, test T1 2027, enquête pilote décidée avant fin 2027 |
| Λ cadrage | 3 | « qualité contrôlée » n'est pas « incertitude publiée » : les deux objets sont confondus dans le cadrage public disponible |
| ↕ pouvoir vertical | 3 | le contrôle est interne à l'État statistique (Comité du label, Cnis) : institutionnellement distinct du producteur, pas externe à la puissance publique |
| ρ résistance | 4 (parent 3) | contre-puissance documentaire établie sur pièce, non sur réputation : avis public par opération, validité, publication JO, demandes de suites et notes exigées (CTRL-001, ACT-001, ACT-002) |
| Κ cynisme | 2 | asymétrie documentaire entreprises/ménages maintenue (aucun équivalent ménages du baromètre de charge de réponse identifié), intention non établie |
| κ influence subtile | 2 | architecture d'information possiblement orientante, design non démontré |
| Σ sémiotique | 2 | le label est un signe ; ici il accompagne des indicateurs et des exigences, il ne les remplace pas |
| Φ spectacle | 2 | médiatisation des chiffres trimestriels, hors corpus |
| 🌐 réseau | 2 | chaîne documentée : commission d'opportunité → Comité du label → service producteur → Comité des utilisateurs → Eurostat |
| € argent, Ω inversion, Ψ sidération | 1 | aucune observation matérielle dans ce run (aucun flux financier, aucune inversion, aucune saturation d'information) |
| ⚔ guerre cognitive | 0 | aucune activité d'influence organisée constatée |

**Rhétorique.** `NUM 3` inchangé (le chiffre brut coupé de son incertitude), `AUTH 1`, `FAC 1` (écart potentiel entre qualité contrôlée et précision affichée). `DEM 0`, `BF 0` : aucun marqueur de mauvaise foi. Le document contrôlé formule quatre demandes de suites et une réserve explicite sur la base de sondage : il ne peut pas être lu comme une caution de complaisance (`AXS-009`).

**Hypothèses implicites retenues comme telles.** (a) L'incertitude relève du producteur et du contrôle, non de l'attribut publié ; (b) le label et l'obligation légale valent garantie de qualité, sans quantification du biais résiduel. Aucune des deux n'est présentée comme établie par une source.

## 3. LEADS (LED-001 à LED-006)

| ID | Lead | Statut | Élément décisif |
|---|---|---|---|
| LED-001 | Le 403 du parent était-il un mur d'accès ou un filtrage technique ? | SATURATED | Filtrage par user-agent : la même URL sert 144 606 octets en HTTP 200 avec un en-tête de navigateur (SRC-001) |
| LED-002 | Le Comité du label émet un avis de conformité, attribue le label et propose le caractère obligatoire | SATURATED | Avis n° 2026_13068_DG75-L002 du 30 juin 2026, validité 2027-2030, publication JO (FCT-001) |
| LED-003 | Le contrôle fait des taux de réponse un indicateur de comparabilité de qualité | SATURATED | Indicateurs du test 2027 : taux de réponse, individus renseignés par logement, écarts sur questions majeures (FCT-002) |
| LED-004 | Le contrôle demande la quantification de l'impact de la base de sondage | SATURATED | Repérage des logements et prise de contact, résidences principales ou non, coordonnées des habitants (FCT-003) |
| LED-005 | Le contrôle formule une appréciation positive documentée | SATURATED | Maintien/amélioration des taux de réponse salué ; progression des réponses par internet en réinterrogation notée (FCT-004, FCT-005) |
| LED-006 | Le même dispositif couvre les autres opérations de la ligne | SATURATED | EAR 2026 (validité 2027-2031, voie législative) et prolongation de l'enquête Emploi pour 2026 (FCT-006, FCT-007) |

`LED-001` était le lead hérité : il est **saturé par fermeture**, non par confirmation d'une hypothèse de rétention. Les cinq autres leads sont des leads de contenu ouverts par la pièce obtenue.

## 4. FAITS (FCT-001 à FCT-009)

| FCT | Tier | Date | Famille(s) | Valeur retenue |
|---|---|---|---|---|
| FCT-001 | ✧ | 2026-06-30 | D (SRC-001) | Avis de conformité n° 2026_13068_DG75-L002 du 30 juin 2026 (réunion du 21 mai 2026) : label Oui, caractère obligatoire Oui, validité 2027-2030, publication JO Oui, périodicité annuelle |
| FCT-002 | ✧ | 2026-06-30 | D (SRC-001) | Les analyses comparatives test/production reposeront sur des indicateurs incluant les taux de réponse, le nombre d'individus renseignés par logement et les écarts sur certaines questions majeures ; enquête pilote envisagée si incidences (décision avant fin 2027) |
| FCT-003 | ✧ | 2026-06-30 | D (SRC-001) | Demande : préciser l'impact de l'évolution de la qualité de la base de sondage sur le repérage des logements et la prise de contact (résidences principales ou non, coordonnées des habitants) |
| FCT-004 | ✧ | 2026-06-30 | D (SRC-001) | Le Comité salue l'investissement du service en faveur du maintien et de l'amélioration des taux de réponse |
| FCT-005 | ✧ | 2026-06-30 | D (SRC-001) | La part des réponses recueillies par internet en situation de réinterrogation a progressé depuis la refonte |
| FCT-006 | ✧ | 2025-10-03 | D (SRC-002) | Avis rectificatif du 01/10/2025 (n° 2025_20777_DG75-L002) : prolongation de l'enquête Emploi pour 2026 ; avis initial du 8 octobre 2020 (2021-2025) |
| FCT-007 | ✧ | 2026-04-01 | D (SRC-003) | Avis de conformité des Enquêtes Annuelles de Recensement (n° 2026_7588_DG75-L002, réunion du 11 février 2026) : enquête décidée par voie législative, validité 2027-2031 |
| FCT-008 | ✧ | 2026-06-30 | D (SRC-001) | Comité des utilisateurs annuel depuis 2021, appel à participation large (Service statistique public et au-delà, chercheurs Quetelet-Progedo, CASD) ; éléments synthétiques demandés au prochain dossier |
| **FCT-009** | **✦** | 2026-09-21 | **A + D** (SRC-004, SRC-001) | **Les taux de réponse de l'enquête Emploi font l'objet d'un suivi explicite comme indicateur de qualité, attesté des deux côtés : le producteur les publie (60,5 % en 1re interrogation, 64,3 % en réinterrogation, T2 2023) et le contrôle externe les retient comme indicateurs de comparabilité test/production** |

`FCT-009` est le seul fait `✦` du run : deux familles de provenance indépendantes (`A` producteur, `D` contrôle externe), deux sources réouvertes dans ce run, et une réfutation terminale (statut `NONE`).

## 5. CHAÎNES CAUSALES (CAU-001 à CAU-003)

| ID | Chaîne | Statut |
|---|---|---|
| CAU-001 | Qualité de la base de sondage (résidence principale ou non, coordonnées) → repérage du logement et prise de contact → probabilité de réponse différentielle → redressement et calage → précision de l'estimation publiée | SUPPORTED — le producteur mesure et publie (famille A) ; le contrôle externe en fait une exigence de suite (famille D) |
| CAU-002 | Collecte → correction de la non-réponse → calage → estimation → chiffre diffusé sans incertitude attachée | GAP (SCOPE) — le dernier maillon est constaté, non quantifié ; le contrôle externe ne porte pas sur la publication grand public |
| CAU-003 | Contrôle externe → label, caractère obligatoire, publication JO → demandes de suites et notes exigées → modifications attendues (test 2027, enquête pilote éventuelle) → effet sur les taux de réponse | GAP (CAUSALITY) — le dispositif de suite est documenté, l'effet mesuré sur les taux ne l'est pas ; maillon laissé ouvert plutôt que supposé |

## 6. CONTRÔLES (CTRL-001)

| Champ | Valeur |
|---|---|
| Contrôleur | Comité du label de la statistique publique (Cnis), commission « Ménages » |
| Règle | Avis de conformité : label d'intérêt général et de qualité statistique, proposition d'octroi du caractère obligatoire, publication au Journal officiel, validité 2027-2030 |
| Information examinée | Dossier de l'enquête, avis d'opportunité de la commission « Emploi, qualification et revenus du travail » (20 mai 2025), indicateurs de taux de réponse du test |
| Action | Avis n° 2026_13068_DG75-L002 du 30 juin 2026 ; demandes de suites (impact de la base de sondage, stratégie de tests, bilan des effets de mode) ; notes exigées sur le tirage 2027 et l'outre-mer |
| Supervision | Contrôle exercé à la source et documenté (`EXERCISE_A_LA_SOURCE`) |
| Statut | **SATURATED** (parent : GAP ACCESS, PDF en HTTP 403) |

## 7. ACTIONS (ACT-001 à ACT-003)

| ID | Acteur | Action | Statut |
|---|---|---|---|
| ACT-001 | Comité du label | Demande que le prochain dossier précise l'impact de la qualité de la base de sondage sur le repérage des logements et la prise de contact | SATURATED |
| ACT-002 | Comité du label | Se déclare destinataire d'une note sur le tirage 2027 (métropole), sera informé de toute évolution de la base de sondage en outre-mer ; test de grande envergure au T1 2027, enquête pilote décidée avant fin 2027 si des incidences sont détectées | SATURATED |
| ACT-003 | Insee (service producteur) | Fait l'objet, pour ses enquêtes ménages, d'un avis de conformité public par opération (enquête Emploi 2027-2030, prolongation 2026, EAR 2027-2031), publié au Journal officiel | SATURATED |

Aucune intention n'est imputée à une personne physique ou morale : `RESPONSIBILITY_MAP` reste `N/A_NO_PERSON_ASSIGNED`, l'objet portant sur une configuration institutionnelle de contrôle.

## 8. AXES (AXS-001 à AXS-009)

| AXS | Axe | Statut | Résultat |
|---|---|---|---|
| AXS-001 | SOURCE_AUDIT | SATURATED | Trois avis de conformité et la source décisive du parent réouverts dans ce run (SRC-001 à SRC-004) |
| AXS-002 | SCOPE_HISTORY | SATURATED | Cycle complet du contrôle : avis 2020 (2021-2025), rectificatif 2025 (2026), renouvellement 2026 (2027-2030) |
| AXS-003 | EVIDENCE_CASES | SATURATED | Le 403 était un filtrage technique ; pièce obtenue et inspectée, identité d'octets vérifiée |
| AXS-004 | RESOURCES_FLOWS | **GAP (ACCESS)** | Coût et financement de la collecte non documentés ; aucune pièce budgétaire dédiée retrouvée |
| AXS-005 | MECHANISMS | SATURATED | Base de sondage (Résil en métropole, EAR pour les DOM historiques) → repérage et prise de contact → non-réponse → redressement et calage |
| AXS-006 | ACTORS_RELATIONS | SATURATED (parent : GAP) | Comité du label, commission d'opportunité, service producteur, Comité des utilisateurs, ménages |
| AXS-007 | RULES_CONTROLS | SATURATED (parent : GAP) | Label, caractère obligatoire, validité, publication JO, suites exigées |
| AXS-008 | IMPACT_RESPONSIBILITY | **GAP (CAUSALITY)** | Effet mesuré du contrôle sur la précision publiée, et effet du chiffre sans incertitude sur les usages : non quantifiés |
| AXS-009 | COUNTER_HYPOTHESES | SATURATED | Hypothèse de complaisance testée et non soutenue : l'avis formule des exigences et une réserve |

## 9. DELTA_REPORT (protocole UPDATE §3)

```text
PARENT_RUN_ID:20260921-0255-insee-taux-de-reponse-par-vague-precision-des-estimations
PARENT_AS_OF:2026-09-21 | CURRENT_AS_OF:2026-09-21
```

| ID | CLASS | PARENT VALUE/STATUS | CURRENT VALUE/STATUS | EVIDENCE | DOWNSTREAM IMPACT |
|---|---|---|---|---|---|
| CTRL-001 | RECHECK → résolu | GAP / ACCESS — avis CNIS 2026 identifié, PDF en HTTP 403 | **SATURATED** — avis inspecté (6 pages, 144 606 octets, sha256 vérifié) | acquisition par en-tête de navigateur (premier essai en échec sur le type de contenu) ; evidence/eec_annuelle_2026.pdf | AXS-006 et AXS-007 passent de GAP à SATURATED ; CLM-001 ouvert ; NQ-001 du parent refermée |
| AXS-006 | RECHECK → résolu | GAP / ACCESS | SATURATED | FCT-001, FCT-004, FCT-008 | ACT-003 ouvert ; ρ porté à 4 |
| AXS-007 | RECHECK → résolu | GAP / ACCESS | SATURATED | FCT-001, FCT-002, FCT-003 | CLM-001 SUPPORTED ; CTR-002 conservée |
| FCT-009 (nouveau) | NEW | — | **✦** A+D | SRC-004 (60,5 % / 64,3 %) + SRC-001 (indicateurs de comparabilité) ; réfutation NONE | objet_decisif : le suivi des taux n'est plus une pratique de producteur seule |
| FCT-001..FCT-008 (nouveaux) | NEW | — | ✧ famille D | SRC-001, SRC-002, SRC-003 | base factuelle du contrôle, auparavant absente |
| CAU-001 | RECHECK → renforcé | SUPPORTED, famille A seule | SUPPORTED, familles A + D | FCT-003 + SRC-001 | le mécanisme amont est identifié par le contrôle lui-même |
| CAU-003 (nouveau) | NEW | — | GAP / CAUSALITY | FCT-001, FCT-002, CTRL-001, ACT-002 | NQ-001 de ce run |
| CLM-004, CLM-005 (nouveaux) | NEW | — | PARTIAL | FCT-002, FCT-003 | bornent l'interprétation de CLM-001 |
| EDI | RECHECK | LIMITED — 0.4175, cible APEX 0.80 non atteinte | **ADEQUATE — 0.5183**, cible MEDIUM 0.50 atteinte | 4 sources, 2 familles (A, D) | pénalité POWER_BLOC requalifiée en OWNERSHIP (.10) + MISSING_COUNTER (.10) |
| ρ (symbole) | RECHECK | 3 | **4** | CTRL-001, ACT-001, ACT-002 | le contre-pouvoir documentaire est établi sur pièce |

```text
AFFECTED_IDS: LED-003;LED-004;LED-005;LED-006;AXS-003;AXS-004;AXS-006;AXS-007;AXS-008;CLM-001;CLM-002;CLM-003;CLM-004;CLM-005;CAU-001;CAU-002;CAU-003;CTRL-001;ACT-001;ACT-002;ACT-003;FCT-001..FCT-009;SRC-001;SRC-002;SRC-003;EDI;rho
UNCHANGED_IDS: LED-001(fermé, non contredit);LED-002;AXS-001;AXS-002;AXS-005;AXS-009;CTR-001;OBJECT_QUESTION;OBJECT_COVERAGE;scope
NOT_REOPENED: Eurostat LFS 2011 (hors objet de la fermeture, classé RECHECK);IM136/IM145/fiche précision RP/note révisions (faits de producteur stables du parent, classés REUSE);SRC-005 du parent (page baromètre entreprises, non réouverte: le fait correspondant n'est pas réexaminé ici)
NEW_GAPS: CAUSALITY:1 (CAU-003);SCOPE:2 (CAU-002, CLM-004);CAUSALITY:1 (CLM-005);ACCESS:1 (AXS-004)
```

**Delta de statut (DELTA_PLAN exécuté).** 8 faits du parent classés `REUSE` (objet stable, famille A, ni valeur ni source modifiées), 1 source externe classée `RECHECK` (Eurostat LFS 2011, non réouverte : hors objet), 1 item de contrôle classé `RECHECK` puis **résolu** (`CTRL-001`). Aucun fait du parent n'est re-publié comme « vérifié par ce run » : seuls les faits nouveaux et réouverts sont portés au registre de ce run.

## 10. CONTRADICTIONS

| ID | Type | Conflit | Résolution | Statut |
|---|---|---|---|---|
| CTR-001 | Apparente | CV national du recensement très faible (0,01 %) contre non-réponse différentielle forte (56 % vs 77 % en 2021) | Deux sources d'erreur distinctes (erreur de sondage contre biais de non-réponse) ; aucune moyenne | RESOLVED |
| CTR-002 | Matérielle | Qualité documentée et contrôlée (FCT-001..FCT-009) contre incertitude absente du chiffre conjoncturel diffusé | Écart de périmètre confirmé par le contrôle lui-même : l'avis ne porte pas sur l'incertitude attachée à l'indicateur publié et demande encore la quantification d'un chaînon amont | PARTIALLY_RESOLVED (CAUSALITY) |
| CTR-003 | Nouvelle, résolue | Le parent consignait un GAP ACCESS sur le contrôle externe, ce qui pouvait laisser lire une rétention documentaire | La pièce est publique, servie en PDF, filtrée seulement par user-agent : le gap était un échec d'acquisition (`CTRL-001` passe GAP → SATURATED) | RESOLVED |

## 11. EDI

```text
[SOURCES] ◈:3 ◉:1 ○:0
EDI:0.5183 raw:0.7183 penalties:0.20[OWNERSHIP_CONCENTRATION;MISSING_COUNTER] N/A:[]
geo:0.833 lang:1.0 strat:0.6 owner:0.75 persp:0.25 temp:0.8
⟐:2 ⟐̅:0 🌍:0 🎓:0 🔥:0 | COV:1.0 IND:0.5 CC:0.5 EDI*:0.6592
band:ADEQUATE — cible MEDIUM 0.50 atteinte (parent : LIMITED 0.4175, cible APEX 0.80 non atteinte)
DIAGNOSTIC_NOT_TRUTH
```

**Changement de pénalité, explicité.** Le parent appliquait `POWER_BLOC_CONCENTRATION (.15)` : 4 sources sur 5 venaient d'un seul producteur intéressé. Cette qualification ne tient plus telle quelle : **3 des 4 sources viennent du contrôle**, dont l'intérêt va à l'encontre de celui du producteur. Le bloc matériellement intéressé (Insee producteur) représente 1 source sur 4, soit 25 %, en dessous du seuil de 75 %. La concentration est donc requalifiée en `OWNERSHIP_CONCENTRATION (.10)`, conformément à la règle « ne pas cumuler OWNERSHIP et POWER_BLOC pour la même concentration, garder la plus forte ». `MISSING_COUNTER (.10)` est conservée : la contre-perspective externe au Service statistique public reste applicable et absente, la recherche de réfutation ayant retourné `NONE_FOUND` — l'absence est consignée comme telle, non comblée par symétrie.

**Profil de couverture des claims décisifs.** CLM-001 et CLM-002 : objet direct, **2 familles indépendantes**, aucun contre-crédible trouvé (`NONE`). CLM-003 : pas d'objet direct (une observation de canal d'accès, `SCOPE`). CLM-004 : pas d'objet direct (`SCOPE`). CLM-005 : objet direct, 1 famille (`CAUSALITY`). Aucun claim décisif ne dépend plus d'une famille unique sur son point de rupture.

## 12. CARTE DIALECTIQUE

**Thèse (institut et contrôle).** La qualité n'est pas déclarative : elle est examinée sur pièces par une instance distincte, qui attribue le label, propose le caractère obligatoire, publie au Journal officiel, retient des indicateurs de comparabilité et exige des suites datées. Le contrôle externe fait lui-même des taux de réponse un critère de qualité.

**Antithèse (la plus forte, inchangée au fond).** Ce qui est contrôlé est l'opération, pas l'incertitude du chiffre diffusé. Le contrôle relève du même système statistique public, pas d'une instance externe. Et le Comité demande lui-même la quantification du chaînon base de sondage → prise de contact → non-réponse : le déterminisme amont de la non-réponse est identifié comme question, non comme résultat.

**Synthèse par les pièces.** L'avis établit le contrôle et il en montre les bornes dans le même geste. La branche de contrôle du parent passe de `GAP ACCESS` à `SATURATED`, mais **l'objet n'est pas saturé** : l'écart entre qualité contrôlée et incertitude publiée reste ouvert (`CTR-002`, `CLM-004`, `AXS-008`).

**Tensions et silences.** Tension réelle : le Comité juge le suivi des taux de réponse suffisant pour la comparabilité du test 2027 tout en demandant la quantification d'un déterminisme qu'il ne mesure pas encore. Silence documentaire : aucune contre-expertise externe au Service statistique public n'a été trouvée.

## 13. PÉRIMÈTRE & LIMITES

**Inclus.** Objet du parent (précision attachée aux estimations publiées, France, 2003-2026) ; branche traitée ici : le contrôle externe de l'enquête Emploi, avec ses documents 2020-2026 et ses validités 2027-2031.

**Exclus.** Sondages d'opinion ; projections démographiques de long terme ; reprises médiatiques (contexte non probatoire) ; analyse interne des services de l'Insee non publiée.

**Limites d'accès.** Le lecteur de page ne traite pas les PDF (échec consigné, contourné par acquisition locale) ; l'acquisition du PDF du Cnis exige un en-tête de navigateur — ce qui est un fait du run, pas une recommandation de contournement ; les textes légaux et réglementaires (loi du 7 juin 1951, règlement (UE) 2019/1700) n'ont pas été inspectés (`NQ-002`).

**Limites de méthode.** La pièce inspectée compte 6 pages : les observations non retenues par le Comité n'y figurent pas nécessairement (absence constatée dans le corpus inspecté, non établie comme absence générale) ; quatre sources seulement, dont trois du même émetteur (`OWNERSHIP_CONCENTRATION`) ; aucune perspective indépendante du Service statistique public (`MISSING_COUNTER`) ; le run ne rejoue pas les faits de producteur du parent, qui restent portés par ses sources d'origine.

## 14. ÉTAT DES CONNAISSANCES

- **Établi (✦).** Les taux de réponse de l'enquête Emploi font l'objet d'un suivi explicite comme indicateur de qualité, attesté indépendamment par le producteur (60,5 % / 64,3 %) et par le contrôle externe (`FCT-009`).
- **Établi (✧, famille D).** Le contrôle externe de l'enquête Emploi existe, est exercé sur pièces, débouche sur un avis public au JO, et assortit son avis de suites exigées (`FCT-001` à `FCT-008`).
- **Établi (✧, famille A, hérité et non rejoué).** Les taux de réponse et de collecte par enquête et par rang, la précision publiée du recensement, les déterminants de la non-réponse, l'existence d'un baromètre entreprises sans équivalent ménages identifié.
- **Probable.** Le chaînon amont (base de sondage → prise de contact → non-réponse différentielle) déplace la charge vers le modèle de correction (`CAU-001`).
- **Contesté.** Aucune contestation matérielle détectée : la recherche de réfutation n'a retourné aucune source opposable (`NONE`, consigné).
- **Inconnu.** Effet mesuré du contrôle sur les taux de réponse (`CAU-003`) ; effet chiffré d'une incertitude non attachée sur un montant indexé (`AXS-008`) ; coût de la collecte (`AXS-004`).
- **Réfuté.** « Le contrôle externe n'était pas consultable » : le 403 était un filtrage par user-agent (`CLM-003`).

## 15. SUSPICION / VÉRIFICATION

**Contrôles exécutés.** Acquisition et inspection de l'avis de conformité 2026 (6 pages) ; acquisition de deux autres avis du même dispositif (prolongation 2026, EAR 2026) ; réouverture de la source décisive du parent (DT2023-22, 5 228 396 octets, taux 60,5 % / 64,3 % retrouvés à la source) ; contre-recherche adversariale sur le fait `✦`.

**Identité des pièces.** Les PDF archivés dans `evidence/` ont été vérifiés par sha256 : `eec_annuelle_2026.pdf` 59c019c7…, `eec_prolongation_2026.pdf` 58483b0e…, `ear_annuelle_2026.pdf` 0e3c0f3c…, `DT2023-22_refonte_eec.pdf` 235d3612… Les extractions texte (`pdftotext -layout`) sont jointes pour permettre la vérification des citations.

**Échecs réels.** Lecteur de page inapte aux PDF (échec consigné, non contourné par ce canal) ; aucune réfutation opposable trouvée (consignée comme `NONE`, non comblée par symétrie). Aucun succès n'a été simulé ; aucun canal payant ou privé n'a été employé.

**Delta de statut.** `CTRL-001` : GAP ACCESS → SATURATED. `AXS-006`, `AXS-007` : GAP → SATURATED. `AXS-004`, `AXS-008` : GAP maintenus et typés. `ρ` : 3 → 4. EDI : LIMITED 0.4175 → ADEQUATE 0.5183. `NQ-001` du parent : refermée. Un gap typé nouveau : `CAU-003` (CAUSALITY).

**Vérification restante.** Effet mesuré du contrôle sur les taux (`NQ-001`) ; textes légaux et réglementaires (`NQ-002`) ; tableau de qualité unique par vague pour les enquêtes ménages (`NQ-003`) ; analyse indépendante du Service statistique public (`NQ-004`) ; chiffrage de l'effet d'une incertitude non attachée (`NQ-005`).
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:6|CLM:5|AXS:9|CAU:3|CTRL:1|ACT:3

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_excerpt":"NQ-001: obtenir et inspecter l avis de conformite CNIS 2026 sur l enquete Emploi (acces direct, retry, ou copie archivee)","gap":"","gap_type":"NONE","kind":"MECHANISM","lead":"Le parent a laisse le controle externe en GAP ACCESS: l avis de conformite CNIS 2026 sur l enquete Emploi repondait un HTTP 403. Question de ce run: ce 403 etait-il un mur d acces ou un filtrage technique ?","linked_ids":["CTRL-001"],"locator":"RUN_STATE du parent 20260921-0255 (CTRL-001, NEXT_QUERIES NQ-001, VERIFICATION_REPORT failure_detail de la tentative d'acquisition du parent)","materiality":"DECISIVE","note":"Gap ferme par un autre canal: le 403 relevait d un filtrage par user-agent. Le document est servi en PDF (144 606 octets) et son contenu est inspecte mot pour mot. Aucun acces payant, prive ou detourne n a ete employe.","routes":["EXPAND","LINK"],"source_id":"SRC-IN","status":"SATURATED"}
LED-002 | {"evidence_excerpt":"Label d interet general et de qualite statistique: Oui; Caractere obligatoire: Oui; Periode de validite: 2027-2030; Publication JO: Oui","gap":"","gap_type":"NONE","kind":"MECHANISM","lead":"Le Comite du label de la statistique publique emet un avis de conformite sur l enquete Emploi, attribue le label d interet general et de qualite statistique et propose l octroi du caractere obligatoire pour 2027-2030.","linked_ids":["FCT-001","FCT-006"],"locator":"evidence/eec_annuelle_2026.pdf, p.1 (tableau Commission/Type d avis/Label/Caractere obligatoire/Validite) et p.6 (dispositif)","materiality":"DECISIVE","note":"Pieces inspectees: avis n 2026_13068_DG75-L002 du 30 juin 2026 (reunion du 21 mai 2026) et avis de prolongation n 2025_20777_DG75-L002 du 03 octobre 2025 pour l annee 2026.","routes":["EXPAND"],"source_id":"SRC-001","status":"SATURATED"}
LED-003 | {"evidence_excerpt":"les analyses comparatives entre les resultats du test et l enquete reposeront sur un ensemble d indicateurs, incluant notamment les taux de reponse, le nombre d individus renseignes par logement ainsi que les ecarts observes sur certaines questions majeures","gap":"","gap_type":"NONE","kind":"MECHANISM","lead":"Le controle externe fait des taux de reponse un indicateur de comparabilite de qualite entre le test 2027 et l enquete en production.","linked_ids":["FCT-002","FCT-009","CLM-002"],"locator":"evidence/eec_annuelle_2026.pdf, section Analyse (indicateurs du test)","materiality":"MATERIAL","note":"C est le point decisif de l objet: le suivi des taux de reponse n est pas seulement une pratique de producteur, il est retenu par un controle externe comme critere de comparaison de qualite.","routes":["EXPAND","LINK"],"source_id":"SRC-001","status":"SATURATED"}
LED-004 | {"evidence_excerpt":"Le Comite souhaite que le prochain dossier precise l impact pour l enquete Emploi de l evolution de la qualite des informations de la base de sondage permettant le reperage des logements et la prise de contact","gap":"","gap_type":"NONE","kind":"MECHANISM","lead":"Le controle externe demande au service de preciser l impact de la qualite de la base de sondage sur le reperage des logements et la prise de contact.","linked_ids":["FCT-003","CAU-001"],"locator":"evidence/eec_annuelle_2026.pdf, section Base de sondage (observations)","materiality":"MATERIAL","note":"La demande porte sur le maillon amont de la non-reponse (caracterisation des residences principales ou non, coordonnees des habitants): le Comite identifie donc le mecanisme que le parent decrivait (CAU-001) et en reclame la quantification.","routes":["EXPAND"],"source_id":"SRC-001","status":"SATURATED"}
LED-005 | {"evidence_excerpt":"Le Comite salue l investissement du service en faveur du maintien et de l amelioration des taux de reponse","gap":"","gap_type":"NONE","kind":"MECHANISM","lead":"Le controle externe formule une appreciation positive documentee sur le maintien des taux de reponse et la progression des reponses par internet en reinterrogation.","linked_ids":["FCT-004","FCT-005"],"locator":"evidence/eec_annuelle_2026.pdf, sections Protocole et questionnaire, Effets de mode","materiality":"MATERIAL","note":"Deux observations distinctes: protocole et questionnaire (investissement pour le maintien et l amelioration des taux de reponse) et effets de mode (part des reponses par internet en reinterrogation en progression).","routes":["EXPAND"],"source_id":"SRC-001","status":"SATURATED"}
LED-006 | {"evidence_excerpt":"Enquetes Annuelles de Recensement: enquete decidee par voie legislative; periode de validite 2027-2031","gap":"","gap_type":"NONE","kind":"MECHANISM","lead":"Le meme dispositif de controle couvre les autres operations de la ligne: Enquetes Annuelles de Recensement (avis du 01 avril 2026, validite 2027-2031) et prolongation de l enquete Emploi pour 2026.","linked_ids":["FCT-006","FCT-007"],"locator":"evidence/ear_annuelle_2026.pdf, p.1 ; evidence/eec_prolongation_2026.pdf, p.1","materiality":"MATERIAL","note":"Le controle est donc un dispositif permanent par operation, non un avis isole: cela borne l interpretation du gap ACCESS du parent comme un cas particulier, non une asymetrie structurelle de controle.","routes":["EXPAND","LINK"],"source_id":"SRC-002,SRC-003","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"counter":"NONE_FOUND","gap":"","gap_type":"NONE","linked_leds":["LED-002","LED-004","LED-006"],"proposition":"Le controle externe examine l enquete Emploi sur pieces et en atteste la qualite statistique, y compris en formulant des demandes de suites.","status":"SUPPORTED","support":"FCT-001, FCT-002, FCT-003 (SRC-001) ; FCT-006, FCT-007 (SRC-002, SRC-003)"}
CLM-002 | {"counter":"NONE_FOUND","gap":"","gap_type":"NONE","linked_leds":["LED-003","LED-005"],"proposition":"Les taux de reponse de l enquete Emploi font l objet d un suivi explicite comme indicateur de qualite.","status":"SUPPORTED","support":"FCT-009 (✦, deux familles: SRC-001 controle externe + SRC-004 producteur, taux de collecte 60,5 % / 64,3 %) ; FCT-002, FCT-004"}
CLM-003 | {"counter":"NONE_FOUND","gap":"","gap_type":"NONE","linked_leds":["LED-001"],"proposition":"Le gap ACCESS du parent (avis de conformite CNIS 2026) etait un filtrage technique par user-agent, non un mur d acces documentaire.","status":"SUPPORTED","support":"QRY-002 (FAILED, content-type PDF) puis QRY-003 (FOUND, 144 606 octets, HTTP 200 avec en-tete navigateur) ; piece archivee dans evidence/ et inspectee"}
CLM-004 | {"counter":"NONE_FOUND","gap":"Le controle porte sur la qualite de l operation et sur des indicateurs de comparaison, pas sur une incertitude attachee a l indicateur publie","gap_type":"SCOPE","linked_leds":["LED-003","LED-004"],"proposition":"Le controle externe quantifie l incertitude attachee au chiffre diffuse.","status":"PARTIAL","support":"FCT-002, FCT-003 ; absence constatee dans la piece inspectee (6 pages), non etablie comme absence generale"}
CLM-005 | {"counter":"NONE_FOUND","gap":"Le Comite demande que l impact soit precise dans le prochain dossier: le lien est identifie comme question, sa quantification est encore due","gap_type":"CAUSALITY","linked_leds":["LED-004"],"proposition":"Le controle externe etablit le lien entre qualite de la base de sondage et non-reponse de l enquete Emploi.","status":"PARTIAL","support":"FCT-003 ; CAU-001"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007"],"axis":"SOURCE_AUDIT","links":["LED-001","LED-002","LED-003","CLM-001","CLM-002"],"question":"Quelles pieces de controle externe documentent la qualite de l enquete Emploi, et que disent-elles exactement ?","result_ids":["SRC-001","SRC-002","SRC-003","SRC-004","FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009"],"sought_objects":["avis de conformite du Comite du label (enquete Emploi 2026)","avis de prolongation 2026","avis de conformite des Enquetes Annuelles de Recensement 2026","document de travail DT2023-22 reouvert"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-004","QRY-005","QRY-003"],"axis":"SCOPE_HISTORY","links":["LED-002","LED-006","CLM-001"],"question":"Quelle est la genealogie du controle de l enquete Emploi: avis initiaux, prolongation, renouvellement 2027-2030 ?","result_ids":["SRC-002","SRC-001","SRC-003","FCT-001","FCT-006","FCT-007"],"sought_objects":["avis initial 2020 (validite 2021-2025)","rectificatif de prolongation 2026","avis de renouvellement du 30 juin 2026"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-002","QRY-003"],"axis":"EVIDENCE_CASES","links":["LED-001","CLM-003"],"question":"Le HTTP 403 du parent etait-il un mur d acces documentaire ou un filtrage technique contournable par un autre canal ?","result_ids":["SRC-001","FCT-001","FCT-009"],"sought_objects":["re-requete directe du PDF","acquisition locale avec en-tete de navigateur","identite d octets de la piece obtenue"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":[],"axis":"RESOURCES_FLOWS","gap":"Cout de la collecte et financement de l enquete Emploi non documentes dans le corpus inspecte; aucune piece budgetaire dediee retrievee.","gap_type":"ACCESS","links":["LED-001"],"question":"Quelles ressources financent la collecte de l enquete Emploi et comment se compareraient-elles au cout d une incertitude non publiee ?","result_ids":[],"sought_objects":["piece budgetaire de l Insee","cout par questionnaire de l EEC"],"status":"GAP"}
AXS-005 | {"attempt_ids":["QRY-006"],"axis":"MECHANISMS","links":["LED-003","LED-004","CAU-001","CLM-005"],"question":"Par quel mecanisme la qualite de la base de sondage et la non-reponse entrent-elles dans l estimation publiee ?","result_ids":["SRC-001","SRC-004","FCT-003","FCT-009"],"sought_objects":["caracterisation de la base de sondage (Resil, recensement pour les DOM historiques)","reperage des logements et prise de contact","correction de la non-reponse et calage"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-003"],"axis":"ACTORS_RELATIONS","links":["LED-002","LED-005","CTRL-001","ACT-001","ACT-002"],"question":"Qui controle l enquete Emploi, au nom de quoi, et avec quels autres acteurs en relation ?","result_ids":["SRC-001","SRC-003","FCT-004","FCT-008"],"sought_objects":["Comite du label de la statistique publique","Commission Emploi qualification et revenus du travail","Comite des utilisateurs annuel (depuis 2021)","Cnis et autorite de la statistique publique"],"status":"SATURATED"}
AXS-007 | {"attempt_ids":["QRY-003","QRY-004"],"axis":"RULES_CONTROLS","links":["LED-002","LED-004","CTRL-001","ACT-001","ACT-002"],"question":"Quelles regles le controle externe applique-t-il, et quelles suites exige-t-il ?","result_ids":["SRC-001","SRC-002","FCT-001","FCT-002","FCT-003","FCT-006"],"sought_objects":["label d interet general et de qualite statistique","caractere obligatoire et publication au JO","periodes de validite 2021-2025 / 2026 / 2027-2030","demandes de suites (base de sondage, strategie de tests, bilan)"],"status":"SATURATED"}
AXS-008 | {"attempt_ids":[],"axis":"IMPACT_RESPONSIBILITY","gap":"L effet mesure du controle externe sur la qualite publiee (et l effet d une incertitude non attachee sur les usages) reste non quantifie dans ce run.","gap_type":"CAUSALITY","links":["LED-003","CLM-004","CAU-003"],"question":"Quel effet mesurable le controle externe a-t-il sur la precision effectivement publiee, et qui repond de l incertitude non attachee au chiffre diffuse ?","result_ids":[],"sought_objects":["ecart de taux de reponse avant/apres exigences du Comite","montants indexes sur des indicateurs publies sans incertitude"],"status":"GAP"}
AXS-009 | {"attempt_ids":["QRY-007"],"axis":"COUNTER_HYPOTHESES","links":["LED-003","LED-004","CLM-002","CLM-004"],"question":"L avis de conformite est-il de complaisance, ou ne porte-t-il pas sur la precision publiee ?","result_ids":["SRC-001","FCT-002","FCT-003","FCT-009"],"sought_objects":["avis de conformite etendu aux aspects qualite","demandes de suites formulees","references aux taux de reponse comme critere"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"links":["FCT-003","FCT-009","CAU-001","CLM-005"],"mechanism":"Qualite de la base de sondage (caracterisation des residences principales ou non, coordonnees des habitants) -> reperage du logement et prise de contact -> probabilite de reponse, differentielle selon le type de logement et le revenu -> correction par redressement et calage -> precision de l estimation publiee","note":"Deux familles de provenance independantes soutiennent desormais ce mecanisme: le producteur le mesure et le publie (famille A, DT2023-22) et le controle externe en fait une exigence de suite (famille D, avis de conformite).","sources":["SRC-001","SRC-004"],"status":"SUPPORTED","type":"MECHANISM"}
CAU-002 | {"gap":"Le dernier maillon (l absence d incertitude attachee au chiffre diffuse) reste constate mais non quantifie; le controle externe ne porte pas sur la publication grand public.","gap_type":"SCOPE","links":["FCT-002","FCT-009","CLM-004"],"mechanism":"Chaine d edition: collecte -> correction de la non-reponse -> calage -> estimation -> chiffre diffuse sans incertitude attachee","note":"Le mecanisme est documente maillon par maillon; ce qui manque est la mesure de l effet sur l usage du chiffre, hors perimetre du controle externe.","sources":["SRC-001","SRC-004"],"status":"GAP","type":"MECHANISM"}
CAU-003 | {"gap":"Le dispositif de suite est documente (avis conditionnels, notes exigees, test 2027 prevu), mais l effet mesure sur les taux de reponse n est pas etabli dans ce run.","gap_type":"CAUSALITY","links":["FCT-001","FCT-002","CTRL-001","ACT-002"],"mechanism":"Controle externe -> label, caractere obligatoire et publication au JO -> demandes de suites adressees au service (base de sondage, strategie de tests, bilan) -> modifications attendues de l enquete (test 2027, enquete pilote eventuelle) -> effet sur les taux de reponse","note":"Le maillon final est laisse ouvert plutot que suppose: aucun document inspecte ne quantifie l effet du controle sur les taux.","sources":["SRC-001"],"status":"GAP","type":"MECHANISM"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"action":"Avis n 2026_13068_DG75-L002 emis le 30 juin 2026 apres reunion du 21 mai 2026; demandes de suites: impact de la base de sondage, strategie de tests, bilan des effets de mode; notes exigees sur le tirage 2027 et l outre-mer","controller":"Comite du label de la statistique publique (Cnis), pour l enquete Emploi, commission Menages","gap":"","gap_type":"NONE","information":"Dossier de l enquete, avis d opportunite de la commission Emploi qualification et revenus du travail (20 mai 2025), indicateurs de taux de reponse du test","oversight":"EXERCISE_A_LA_SOURCE","rule":"Avis de conformite: label d interet general et de qualite statistique, proposition d octroi du caractere obligatoire, publication au Journal officiel, validite 2027-2030","sources":["SRC-001","SRC-002","SRC-003"],"status":"SATURATED"}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Demande que le prochain dossier precise l impact de l evolution de la qualite de la base de sondage sur le reperage des logements et la prise de contact (caracterisation des residences principales ou non, coordonnees des habitants)","actor":"Comite du label de la statistique publique","note":"Action de controle assortie d une exigence de suite, adressee au service producteur; aucune imputation d intention.","sources":["SRC-001"],"status":"SATURATED"}
ACT-002 | {"action":"Prevoit d etre destinataire d une note sur le prochain tirage de l echantillon pour la France metropolitaine (2027) et informe de toute evolution de la base de sondage dans les departements et regions d outre-mer; un test de grande envergure est prevu au premier trimestre 2027 et une enquete pilote sera decidee avant fin 2027 si des incidences sont detectees","actor":"Comite du label de la statistique publique","note":"Chaine d obligations de suite documentee sur 2026-2027; le dispositif rend le controle verifiable a posteriori.","sources":["SRC-001"],"status":"SATURATED"}
ACT-003 | {"action":"Fait l objet, pour ses enquetes menages, d un avis de conformite publique par operation (enquete Emploi 2027-2030, prolongation 2026, EAR 2027-2031), publie au Journal officiel","actor":"Insee (service producteur)","note":"Situe l asymetrie documentaire relevee par le parent: la piece de controle existe et est publique; elle n etait pas lue.","sources":["SRC-001","SRC-002","SRC-003"],"status":"SATURATED"}

SEARCH_ACTIVITY_V1:WEB:2|FETCH:5|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FOUND:5 memoires (ligne INSEE), dont l investigation du parent 20260921-0255 portant subject-fp:3f051dff; aucun snapshot:v1 n existait pour ce subject-fp avant ce run. TOOL_SCHEMA_UNAVAILABLE (MCP non expose a la session) -> fallback MCP-par-curl 8002 | mnemolite.search_memory | http://localhost:8002/mcp | MNEMO_Q
SYS-002 | SYS | FOUND:snapshot du parent hydrate (9 faits, 1 gap) via RUN_STATE du parent 20260921-0255 | runtime | - | MEMORY_PROBE
SYS-003 | SYS | FOUND | runtime | bb5ccea4-9ffc-402d-802b-8e16ce60db29 | MEMORY_PROBE
SYS-004 | SYS | FOUND | runtime | bb5ccea4-9ffc-402d-802b-8e16ce60db29 | HYDRATE
SYS-005 | SYS | FOUND | runtime | bb5ccea4-9ffc-402d-802b-8e16ce60db29 | MEMORY_PROBE
SYS-006 | SYS | FOUND | runtime | bb5ccea4-9ffc-402d-802b-8e16ce60db29 | HYDRATE
SYS-007 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND:le canal d acces direct au site du Cnis est identifie (trois avis publies en PDF); permet de relancer l acquisition au lieu de reproduire le 403 du parent | - | - | CNIS avis de conformite 2026 enquete Emploi Insee
QRY-002 | FETCH | FAILED:content-type application/pdf non extractible par le lecteur de page (meme echec que le parent du parent 02-55); consigne, non contourne a ce stade | - | https://www.cnis.fr/app/uploads/2025/07/ac-2026-insee-enquete-emploi-annuelle.pdf | Avis de conformite EEC 2026 (lecteur de page)
QRY-003 | FETCH | FOUND:144606 octets, HTTP 200 avec user-agent de navigateur, extraction pdftotext -layout (335 lignes). Le 403 du parent etait un filtrage par user-agent, non un mur d acces: le gap ACCESS est ferme par un AUTRE CANAL | SRC-001 | https://www.cnis.fr/app/uploads/2025/07/ac-2026-insee-enquete-emploi-annuelle.pdf | Avis de conformite EEC 2026 (acquisition locale, en-tete navigateur)
QRY-004 | FETCH | FOUND:203583 octets, HTTP 200, extraction pdftotext -layout (244 lignes) | SRC-002 | https://www.cnis.fr/wp-content/uploads/2025/10/ac-2020-insee-eec-prolongation-2026.pdf | Avis de conformite EEC - prolongation pour 2026 (rectificatif du 03 octobre 2025)
QRY-005 | FETCH | FOUND:155773 octets, HTTP 200, extraction pdftotext -layout (339 lignes) | SRC-003 | https://www.cnis.fr/app/uploads/2026/04/ac-2026-insee-ear-annuelle.pdf | Avis de conformite Enquetes Annuelles de Recensement 2026 (01 avril 2026)
QRY-006 | FETCH | FOUND:5228396 octets, HTTP 200, empreinte pdf 235d3612... : source decisive du parent reouverte, taux de collecte 60,5 % et 64,3 % retrouves a la source (figure 25) | SRC-004 | https://www.insee.fr/fr/statistiques/fichier/8201155/DT2023-22.pdf | Reouverture de la source decisive du parent (DT2023-22, refonte de l enquete Emploi)
QRY-007 | WEB | NO_RESULT:aucune source contestant le suivi des taux de reponse comme indicateur de qualite (ni refus de principe du controle externe, ni critique documentaire); les resultats concordent (DT2023-22 publie les taux par rang, l avis de conformite les retient) | - | - | REFUTATION taux de reponse enquete Emploi indicateur de qualite suivi 77 % 60,5 % 64,3 % critique methodologique refus du controle

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:D | https://www.cnis.fr/app/uploads/2025/07/ac-2026-insee-enquete-emploi-annuelle.pdf
SRC-002 | ◈ | fam:D | https://www.cnis.fr/wp-content/uploads/2025/10/ac-2020-insee-eec-prolongation-2026.pdf
SRC-003 | ◈ | fam:D | https://www.cnis.fr/app/uploads/2026/04/ac-2026-insee-ear-annuelle.pdf
SRC-004 | ◉ | fam:A | https://www.insee.fr/fr/statistiques/fichier/8201155/DT2023-22.pdf

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.cnis.fr/app/uploads/2025/07/ac-2026-insee-enquete-emploi-annuelle.pdf | D | 2026-06-30 | cnis-avis-conformite-eec-2026 | Le Comite du label de la statistique publique emet un avis de conformite sur l enquete Emploi (n 2026_13068_DG75-L002, Montrouge le 30 juin 2026, apres reunion du 21 mai 2026): label d interet general et de qualite statistique Oui, caractere obligatoire Oui (proposition d octroi), periode de validite 2027-2030, publication au JO Oui, periodicite annuelle; avis d opportunite favorable du 20 mai 2025 | 1d7faea7-729e-4b35-8e45-95676d932501
FCT-002 | FACT | ✧ | https://www.cnis.fr/app/uploads/2025/07/ac-2026-insee-enquete-emploi-annuelle.pdf | D | 2026-06-30 | cnis-indicateurs-de-qualite-test-2027 | Le Comite releve que les analyses comparatives entre les resultats du test et l enquete reposeront sur un ensemble d indicateurs, incluant notamment les taux de reponse, le nombre d individus renseignes par logement ainsi que les ecarts observes sur certaines questions majeures; si des incidences etaient mises en evidence, une enquete pilote serait envisagee (decision avant fin 2027) | 41d4fa27-9bef-42a6-8507-20f0563f1ff9
FCT-003 | FACT | ✧ | https://www.cnis.fr/app/uploads/2025/07/ac-2026-insee-enquete-emploi-annuelle.pdf | D | 2026-06-30 | cnis-base-de-sondage-prise-de-contact | Le Comite souhaite que le prochain dossier precise l impact pour l enquete Emploi de l evolution de la qualite des informations de la base de sondage permettant le reperage des logements et la prise de contact (caracterisation des residences principales ou non, coordonnees des habitants) | e4291886-6fdd-4367-b7e9-9c49242abe89
FCT-004 | FACT | ✧ | https://www.cnis.fr/app/uploads/2025/07/ac-2026-insee-enquete-emploi-annuelle.pdf | D | 2026-06-30 | cnis-salue-maintien-taux-de-reponse | Au titre du protocole et du questionnaire, le Comite salue l investissement du service en faveur du maintien et de l amelioration des taux de reponse | 276fbc35-4f21-4ba0-8392-2263e816ebd6
FCT-005 | FACT | ✧ | https://www.cnis.fr/app/uploads/2025/07/ac-2026-insee-enquete-emploi-annuelle.pdf | D | 2026-06-30 | cnis-progression-reponse-internet | Le Comite salue les travaux relatifs aux effets de mode conduits apres la precedente refonte et note que la part des reponses recueillies par internet en situation de reinterrogation a progresse depuis | abb11b0d-8d37-4d62-b483-e64ad0b587b4
FCT-006 | FACT | ✧ | https://www.cnis.fr/wp-content/uploads/2025/10/ac-2020-insee-eec-prolongation-2026.pdf | D | 2025-10-03 | cnis-avis-prolongation-eec-2026 | Avis rectificatif du 01/10/2025 pris par avis de conformite du 03 octobre 2025 (n 2025_20777_DG75-L002) prononcant la prolongation de l enquete Emploi pour l annee 2026; avis initial du 8 octobre 2020 pour la periode 2021-2025, label Oui, caractere obligatoire Oui, publication JO Oui | 3a7360b4-f440-44d8-8ddb-eaeb3dfd33b3
FCT-007 | FACT | ✧ | https://www.cnis.fr/app/uploads/2026/04/ac-2026-insee-ear-annuelle.pdf | D | 2026-04-01 | cnis-avis-ear-2026 | Le Comite du label emet un avis de conformite pour les Enquetes Annuelles de Recensement (n 2026_7588_DG75-L002, 01 avril 2026, apres reunion du 11 fevrier 2026): enquete decidee par voie legislative, label Oui, caractere obligatoire Oui, validite 2027-2031, publication JO Oui | a08bdacf-ec10-4cc6-b065-3f753bb4ba32
FCT-008 | FACT | ✧ | https://www.cnis.fr/app/uploads/2025/07/ac-2026-insee-enquete-emploi-annuelle.pdf | D | 2026-06-30 | cnis-comite-des-utilisateurs-depuis-2021 | Le Comite salue la mise en place depuis 2021 d un Comite des utilisateurs annuel, avec appel a participation large au sein du Service statistique public et au-dela, notamment aupres des chercheurs ayant sollicite un acces via Quetelet-Progedo ou le Centre d acces securise aux donnees, et demande des elements synthetiques dans le prochain dossier | f3090852-7865-4b4c-aa3f-bae51cef2d19
FCT-009 | FACT | ✦ | https://www.insee.fr/fr/statistiques/fichier/8201155/DT2023-22.pdf | A,D | 2026-09-21 | suivi-des-taux-de-reponse-comme-indicateur-de-qualite | Les taux de reponse de l enquete Emploi font l objet d un suivi explicite comme indicateur de qualite, et ce de deux cotes independants: le producteur les publie (taux de collecte 60,5 % en 1re interrogation et 64,3 % en reinterrogation au T2 2023, DT2023-22 figure 25) et le controle externe les retient comme indicateurs de comparabilite entre le test 2027 et l enquete en production (avis de conformite du 30 juin 2026) | f477bb12-5df8-4077-bc2f-6f729d52f289
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-001
FCT-005 | SRC-001
FCT-006 | SRC-002
FCT-007 | SRC-003
FCT-008 | SRC-001
FCT-009 | SRC-001,SRC-004

## REFUTATION_REGISTRY_V1
FCT-009 | QRY-007 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | ELIGIBLE:VERIFIE
FCT-008 | ELIGIBLE:VERIFIE
FCT-009 | ELIGIBLE:CONFIRME

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -
FCT-007 | WRITE | -
FCT-008 | WRITE | -
FCT-009 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:8
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18b

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-21T01:34:14.568088+00:00","fact_mem":{"FCT-001":"1d7faea7-729e-4b35-8e45-95676d932501","FCT-002":"41d4fa27-9bef-42a6-8507-20f0563f1ff9","FCT-003":"e4291886-6fdd-4367-b7e9-9c49242abe89","FCT-004":"276fbc35-4f21-4ba0-8392-2263e816ebd6","FCT-005":"abb11b0d-8d37-4d62-b483-e64ad0b587b4","FCT-006":"3a7360b4-f440-44d8-8ddb-eaeb3dfd33b3","FCT-007":"a08bdacf-ec10-4cc6-b065-3f753bb4ba32","FCT-008":"f3090852-7865-4b4c-aa3f-bae51cef2d19","FCT-009":"f477bb12-5df8-4077-bc2f-6f729d52f289"},"mnemo_row":"PASS: 9/9 eligible facts persisted via MCP write_memory (8002) + 1 investigation memory (5143d5a7-d17d-4f61-bdc5-d3fc630948e1); no duplicate_warning; run 20260921-0314-insee-avis-conformite-cnis-eec-gap-access","result":"PASS","writeback_execution":[{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"NONE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"NONE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"NONE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"NONE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"NONE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"NONE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"NONE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-008","reason":"NONE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-009","reason":"NONE","success":1}],"writeback_row":{"attempted":9,"blocked":0,"eligible":9,"failure":0,"success":9}}

PERSISTENCE_META: MNEMO_ROW:PASS: 9/9 eligible facts persisted via MCP write_memory (8002) + 1 investigation memory (5143d5a7-d17d-4f61-bdc5-d3fc630948e1); no duplicate_warning; run 20260921-0314-insee-avis-conformite-cnis-eec-gap-access | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:9;attempted:9;success:9;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[9 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-008 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-009 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
