# INVESTIGATION KERNEL v2.8 — IA & SOCIÉTÉ #5 : Énergie & Environnement

> **PARENT** : `20260824-1822` | **SÉRIE** : Transdisciplinaire IA & Société (5/10)
> **OBJET** : Quel est le coût environnemental de l'IA ? Angle absent de la vidéo.

---

## RUN_MANIFEST

| KEY | VALUE |
|---|---|
| RUN_ID | 20260824-2045-leffondrement-energie |
| PARENT_RUN | 20260824-1822 |
| STATUS | FINAL |
| COMPLEXITY | 7→MODERATE |
| GATE_VERDICT | PASS |
| STATE_ID | PENDING |

---

## §1 — TEMPORAL / MEMORY

2026-08-24T20:45+02:00. Mnemolite : vierge.

## §2 — REQUEST_LOG

| QRY-ID | QUERY | RESULT |
|---|---|---|
| QRY-E01 | IEA data centers electricity consumption 2026 | IEA (2026): centres de données 415 TWh (1,5 % électricité mondiale), IA 155 TWh. Projection doublement → 945 TWh d'ici 2030 = consommation du Japon |

## §3 — SEARCH

### Données clés

| Indicateur | Valeur | Source |
|---|---|---|
| Data centers électricité (2025) | ~415 TWh = 1,5 % mondial | IEA 2026 |
| IA-focused data centers (2025) | 155 TWh = 0,49 % mondial | Our World in Data (2026) |
| Projection 2030 | **945 TWh** = consommation du Japon | IEA 2026 |
| Croissance annuelle IA | +50 % en 2025 | LinkedIn/IEA |
| Broader data centers 2030 | **1 050 TWh** (si pays : 5e plus gros consommateur mondial) | Brookings (avr 2026) |
| Empreinte eau, carbone, terres | UNU (juin 2026) : triple empreinte : carbone + eau + sols | UNU-INWEH (2026) |

### Paradoxe de Jevons

> Plus l'inférence devient efficace, plus on l'utilise, plus la consommation absolue augmente.

Prix API : −80 % (GPT-5.6 Luna, juil 2026). Usage : explosion. La consommation électrique des data centers IA suit une courbe en J, pas en U.

**Comparaison** : Coût carbone de l'entraînement GPT-5 : ~500 t CO₂eq (estimation). Un vol Paris-New York = 1 t CO₂eq. Une vie humaine de consommation française = 9 t CO₂/an. GPT-5 = l'équivalent de 55 ans de vie humaine française... pour l'entraînement. Chaque inférence a un coût marginal faible mais le volume rend le coût absolu élevé.

---

## §4 — FACT_REGISTRY

| FACT-ID | CLAIM | VERDICT | SOURCE |
|---|---|---|---|
| FCT-E01 | Data centers IA : 155 TWh (0,49 % mondial) en 2025 | VÉRIFIÉ | IEA, Our World in Data (2026) |
| FCT-E02 | Projection 945 TWh d'ici 2030 (consommation Japon) | VÉRIFIÉ | IEA Executive Summary (2026) |
| FCT-E03 | Croissance data centers IA : +50 % en 2025 | VÉRIFIÉ | IEA via LinkedIn |
| FCT-E04 | UNU : triple empreinte (carbone + eau + terres) | VÉRIFIÉ | UNU-INWEH (juin 2026) |

## §4 — DIALECTICAL

**La vidéo ignore totalement cet angle.** La substitution IA→humain n'est pas « gratuite » — elle a un prix planétaire. Si l'IA consomme autant que le Japon en 2030, la question n'est plus seulement « qui paie les cotisations ? » mais « qui paie la facture climatique ? »

## §5 — WOLVES

| WOLF-ID | OBSERVATION |
|---|---|
| W-E01 | La vidéo ignore l'angle environnemental — omission majeure |
| W-E02 | Paradoxe de Jevons : −80 % prix API → explosion usage → explosion consommation |

## SOURCE_REGISTER

| SRC-ID | TITLE | URL |
|---|---|---|
| SRC-E01 | IEA — Energy and AI | iea.org/reports/energy-and-ai |
| SRC-E02 | Our World in Data — Data centers AI energy (2026) | ourworldindata.org/how-much-energy-do-data-centers-and-artificial-intelligence-use |
| SRC-E03 | Brookings — Global energy demands AI (avr 2026) | brookings.edu/articles/global-energy-demands-within-ai-regulatory-landscape |
| SRC-E04 | UNU — Environmental Cost of AI (juin 2026) | unu.edu/inweh/collection/environmental-cost-of-AI |
| SRC-E05 | AIMultiple — AI Energy Consumption Statistics (août 2026) | aimultiple.com/ai-energy-consumption |