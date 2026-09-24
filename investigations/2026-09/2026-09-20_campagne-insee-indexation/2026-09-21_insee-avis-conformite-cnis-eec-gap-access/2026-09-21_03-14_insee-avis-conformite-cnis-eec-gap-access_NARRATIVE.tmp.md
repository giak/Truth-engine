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
