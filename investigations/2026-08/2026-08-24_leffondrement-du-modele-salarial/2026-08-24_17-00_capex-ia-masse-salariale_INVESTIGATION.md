# KERNEL INVESTIGATION: CAPEX IA contre masse salariale (trou causal XQ-C)

| Champ | Valeur |
|-------|--------|
| ID | INV-2026-08-24-1700-CAPEX-IA-MASSE-SALARIALE |
| Type | KERNEL APEX (16/18) |
| RUN_ID | 20260824-1700-capex-ia-masse-salariale |
| Loup parent | XQ-C (point d'étape du 24/08 : trou causal central de la fresque IA-salariat) |
| Date | 2026-08-24 |
| INPUT_KIND | TOPIC |
| MISSION_MODE | INVESTIGATION |
| Sources consultées | ~30 |
| Faits enregistrés | 30 |
| Faits ancrés (fetchés) | 20 |
| Gate | PASS (déterministe, worktree te-capex-ia-20260824, 19a + 19b) |
| STATE_ID | sha256:4475e4bd62ff88ea3c8eb87b5ba0606933f7e8f772bf0b0ce3e312060921c015 |
| Mémoires écrites | 20 faits (VERIFIE) |

---

## 1. RÉSUMÉ EXÉCUTIF

**OBJECT_QUESTION :** peut-on documenter la chaîne « budget total → CAPEX IA en hausse → masse salariale en baisse → commentaire explicite du management » entreprise par entreprise ?

**Réponse bornée :** oui, le lien est désormais documentable dans le discours et la temporalité pour au moins dix entreprises, mais la chaîne budgétaire intégrale (une ligne tracée du budget global vers le payroll) n'est reconstruite nulle part. Le cas le plus complet est **Meta** : 8 000 postes supprimés le 20 mai 2026 (10 % de ~80 000 salariés), 6 000 postes ouverts annulés (14 000 positions au total), 7 000 salariés réaffectés à des équipes IA, pendant que le capex 2026 passe à 125-145 Md$ contre 72,2 Md$ en 2025 et 39,2 Md$ en 2024 [FCT-001, FCT-002, FCT-003]. La directrice financière Susan Li relie explicitement les deux : un modèle opérationnel « plus lean » doit « compenser les investissements en infrastructure » [FCT-007]. Le mécanisme a un nom dans la presse spécialisée : « convertir le payroll en capex IA » [SRC-TNW].

**Le chiffre qui relativise :** les économies attendues des licenciements Meta (3 Md$ selon Evercore, 7 à 8 Md$ selon Bank of America) ne couvrent que 2 à 6 % du capex 2026 de l'entreprise [FCT-005]. Les licenciements ne financent donc pas l'infrastructure : ils signalent une réallocation du dollar marginal. C'est le point de rigueur le plus important de cette investigation : la conversion payroll→capex est structurelle et symbolique, pas arithmétique.

**Le cas IBM est la preuve empirique du danger « pipeline junior » :** gel d'embauche et promesse de 7 800 postes remplacés par l'IA (mai 2023), puis 13 000 à 17 000 suppressions effectives entre septembre 2024 et mars 2025, puis retournement complet en février 2026 : triplement des embauches de juniors, annoncé par la directrice des ressources humaines [FCT-016, FCT-017, FCT-018]. Le constat : « AI can do most of them » pour les postes juniors de 2023, mais sans juniors, plus de vivier de seniors. L'hypothèse du corpus est validée par le cas le plus documenté du secteur.

**Sur l'attribution :** la corrélation temporelle 2025-2026 entre explosion des capex et réduction des effectifs est forte, mais la causalité n'est pas isolée. Le taux de base existe : l'attrition et le non-remplacement précèdent l'IA (banques, télécoms). Les dénis managériaux compliquent l'attribution : Zuckerberg affirme que les outils IA « ne sont pas ce qui pilote les licenciements » [FCT-006], le CEO d'Intuit dit que ses 3 000 suppressions « n'ont rien à voir avec l'IA » [FCT-023]. Le faisceau (discours, temporalité, ampleur, réallocation interne) pointe une réallocation simultanée, pas une ligne budgétaire tracée.

**Verdict du lead :** le trou causal XQ-C est **partiellement comblé** : la chaîne est documentée dans 4 niveaux de discours (substitution directe : BT, Salesforce ; compensation de coûts : Meta, Oracle ; déni : Zuckerberg, Intuit ; retournement : IBM), mais la reconstruction intégrale budget→payroll reste ouverte. Le prochain pas est une analyse des dépôts comptables 10-K des dix entreprises sur la ligne « employee compensation » vs « capital expenditures » 2022-2026.

---

## 2. MANIPULATION_REPORT

| Symbole | Score /10 | Observation |
|---------|-----------|-------------|
| Ξ Omission | 7 | Aucun 10-K ne présente capex et compensation sur la même page ; les entreprises présentent les licenciements comme « efficiency » et les capex comme « AI leadership » sans jamais tracer la ligne |
| € Money | 8 | Capex Meta 125-145 Md$ 2026 ; Microsoft ~105 Md$ ; les économies de licenciements (3-8 Md$) sont un ordre de grandeur inférieur |
| Λ Framing | 7 | « Year of efficiency » (Meta 2023), « Business AI » (SAP), « AI-first » : le cadre transforme des réductions d'effectifs en stratégie |
| Ω Inversion | 5 | Les dénis (Zuckerberg, Intuit) inversent le récit : « ce n'est pas l'IA » alors que la réallocation vers l'IA est la seule explication documentée |
| Ψ Sideration | 6 | Records de profits (Meta : 201 Md$ de revenus 2025, +22 %) simultanés à des licenciements de 10 % : dissonance maximale |
| ↕ Pouvoir vertical | 6 | Le management décide seul de la réallocation ; les salariés découvrent via des mémos internes ; Meta filme les frappes clavier de ses employés |
| Φ Spectacle | 4 | Zuckerberg code lui-même son assistant IA ; Meta crée des sites de compte à rebours (« Big Beautiful Layoff ») |
| Σ Sémio | 6 | « efficiency » pour licenciements, « pods » pour équipes réduites, « ne pas backfiller » pour non-remplacement : le vocabulaire efface l'événement |
| Κ Cynisme | 6 | IBM vante l'IA qui « remplace 30 % du back-office » puis triplent les embauches juniors ; Meta paie des chercheurs 100 M$ pendant que la médiane baisse |
| ρ Résistance | 3 | Pétition interne Meta contre la surveillance, poursuite de 26 ex-salariés, question écrite de Ruffin sur Teleperformance |
| κ Influence subtile | 3 | Programme « Model Capability Initiative » : les salariés génèrent les données d'entraînement des systèmes qui remplacent leurs postes |
| ⫸ Convergence | 7 | Dix entreprises, quatre niveaux de discours, une temporalité commune 2025-2026 : le faisceau est cohérent |
| ⚔ Guerre cognitive | 3 | Le récit « l'IA détruit l'emploi » est activement entretenu ET démenti selon l'auditoire (investisseurs vs salariés) |
| 🌐 Réseau | 4 | Les mêmes cabinets de conseil (McKinsey, Accenture) conseillent les restructurations et vendent l'IA aux mêmes directions |
| ⏰ Temporal | 7 | Synchronisation : les annonces capex de février 2026 précèdent les plans sociaux de mars-mai 2026 (Oracle, Microsoft, Meta, Intuit) |

**Chargement des clusters :** €=8 → MONEY, POWER ; Ξ=7 → ICEBERG ; Λ=7 → FRAMING ; ⏰=7 → TEMPORAL. Clusters chargés : MONEY, POWER, ICEBERG, FRAMING, TEMPORAL.

**Hypothèses d'entrée :** le lien CAPEX→emploi est corrélé, pas démontré ; la période 2022-2026 ; géographie US dominante avec un cas français (Teleperformance) ; les données comptables primaires (10-K) ne sont pas encore analysées ligne à ligne.

---

## 3. CLUSTERS

**MONEY (€=8) :** les capex IA 2026 des cinq géants (660-690 Md$, cf. INV bulle-IA) contre des économies de licenciements de 3 à 8 Md$ par entreprise. Diagnostic : l'argent des licenciements ne paie pas l'infrastructure, il paie le récit d'« efficience » ; le flux réel va de la masse salariale vers les fournisseurs de compute. MONEY_FACTOR : rapport économies/capex ≈ 2-6 % (Meta), 8 % (Oracle selon kore1), part non disclosed du payroll réaffecté en interne (Meta : 7 000 réaffectés, chiffre interne).

**POWER (↕=6) :** asymétrie d'information totale : le management connaît le plan (capex, restructuration), les salariés découvrent l'ordre de licenciement le matin même (Oracle : e-mails automatiques à 6 h, 31 mars 2026). Le pouvoir de décision s'exerce sans contrepartie documentée.

**ICEBERG (Ξ=7) :** la partie visible est le licenciement spectaculaire (8 000 chez Meta) ; la partie immergée est le non-remplacement (6 000 postes ouverts annulés chez Meta, « ne pas backfiller » chez Salesforce), la réaffectation (7 000 chez Meta), la compression du milieu de grille (médiane -7 %) et l'explosion du haut (chercheurs IA à 100 M$).

**FRAMING (Λ=7) :** le vocabulaire remplace l'événement : « efficiency », « pods », « restructuration », « départs volontaires » (Microsoft) au lieu de licenciements. Le déni (Zuckerberg, Intuit) est une stratégie de communication : l'IA est la seule explication cohérente de la réallocation, mais elle n'est jamais nommée comme cause.

**TEMPORAL (⏰=7) :** séquence 2026 : annonces capex février (Meta, Alphabet, Microsoft, Amazon, Oracle) → plans de départ mars-mai (Oracle 31/03, Microsoft 23/04, Meta 20/05, Intuit 20/05) → nouvelles vagues annoncées (Meta août et automne). La synchronisation est un indice fort, pas une preuve.

---

## 4. HERMÉNEUTIQUE

| Niveau | Interprétation | Statut |
|--------|----------------|--------|
| L1 | Les licenciements, capex et effectifs sont des chiffres publiés et recoupés | FAIT |
| L2 | La simultanéité capex↑/effectifs↓ 2026 est mesurable sur dix entreprises | FAIT |
| L3 | Le lien entre les deux est explicite dans le discours (Li, Benioff, Jansen, LaMoreaux) | FAIT |
| L4 | « Les licenciements financent les capex » est faux en volume (2-6 %) | FAIT |
| L5 | « L'IA cause les licenciements » reste une inférence : le taux de base (attrition pré-IA) et les dénis interdisent l'attribution univoque | INFERENCE |
| L6 | La réallocation du dollar marginal (payroll vers compute) est la mécanique la plus probable | INFERENCE bornée |

Faits séparés des inférences : « Meta supprime 8 000 postes » est un fait ; « pour financer l'IA » est une lecture de la simultanéité et des déclarations ; « l'IA va détruire le salariat » reste non établi au niveau agrégé.

---

## 5. FORENSIC REASONING

**Montré :** les communiqués, citations et chiffres publiés (effectifs, capex, médianes de rémunération, montants de plans de restructuration).
**Omis :** les 10-K ligne à ligne (compensation vs capex 2022-2026) ; le détail des réaffectations internes (Meta 7 000) ; le coût total réel par départ (severance + perte de productivité) ; les critères de sélection des licenciés (poursuite Meta).
**Reconstruction :** le ratio économies/capex (2-6 %) est reconstruit à partir des estimations Evercore et BofA rapportées aux guidances officielles. Le total sectoriel (110 000 postes à 137 entreprises en 2026) vient de Layoffs.fyi, agrégateur non audité ligne à ligne.

---

## 6. PRISME DIALECTIQUE

**Thèse dominante (direction) :** « l'IA rend l'entreprise plus efficace ; les effectifs se réorganisent ; c'est un investissement de croissance » (Meta, SAP, Salesforce, Microsoft).
**Thèse critique la plus forte :** « c'est une réallocation du travail vers le capital : la masse salariale baisse pendant que les dépenses d'infrastructure explosent, avec un transfert de valeur vers les fournisseurs de compute et une destruction du pipeline de compétences » (validée par le retournement IBM).
**Thèse sceptique (contre les deux) :** « l'ampleur reste marginale : 110 000 postes dans la tech mondiale, c'est moins de 0,03 % de l'emploi global ; les licenciements sont des ajustements de sur-embauche pandémique habillés en IA » (Ed Zitron, CNBC).
**Arbitrage :** les trois thèses sont compatibles à des échelles différentes. La thèse critique est la plus solide sur les dix cas documentés (le lien discours-réallocation est explicite) ; la thèse sceptique rappelle le taux de base ; la thèse dominante ne tient que si les gains de productivité IA se matérialisent, ce que les réembauches (IBM, Klarna, CBA) contredisent partiellement.

---

## 7. CHRONOLOGIE

| Date | Événement | Source |
|------|-----------|--------|
| 2023-05 | BT : jusqu'à 55 000 postes d'ici 2030 (40 %), dont 10 000 remplacés par l'IA | [SRC-GUAR] |
| 2023-05 | IBM : gel d'embauche back-office, 7 800 postes remplaçables, 30 % des 26 000 | [SRC-TL] |
| 2023-11 | Meta : « année de l'efficience », 21 000 postes supprimés depuis 2022 | [SRC-TNW] |
| 2024-01 | SAP : restructuration de 8 000 postes, coût 2 Md€, focus « Business AI » | [SRC-REUSAP] |
| 2024-07 | Intuit : 1 800 postes (10 %) dans une réorganisation « autour de l'IA » | [SRC-FORT] |
| 2024-11 | Teleperformance : plan de départs volontaires visant ~1/3 des effectifs France | [SRC-ECHOS] |
| 2024-12 | Meta clôt l'année à 74 067 salariés (après 67 317 fin 2023) | [SRC-SQMAG] |
| 2025-02 | Meta : capex 2025 à 72,2 Md$ (vs 39,2 Md$ en 2024) | [SRC-TNW] |
| 2025-09 | Salesforce : Benioff confirme 4 000 suppressions, « I need less heads » | [SRC-CNBC] |
| 2025-09 → 2026-03 | IBM : 13 000 à 17 000 suppressions en deux vagues | [SRC-TL] |
| 2026-01 | Dimon (Davos) : l'IA va créer « un chômage massif et une hausse énorme des profits » | [SRC-FORTD] |
| 2026-02 | Annonces capex 2026 des cinq géants (660-690 Md$) | [SRC-CONARD] |
| 2026-03-31 | Oracle : licenciements massifs, « shrink due to AI », plan de restructuration 2,1 Md$ au SEC filing | [SRC-CNBCORA] |
| 2026-04-23 | Microsoft : premier programme de retraite volontaire, ~7 % des effectifs US | [SRC-CNBCMS] |
| 2026-04-30 | Zuckerberg : les outils IA « ne sont pas ce qui pilote les licenciements » | [SRC-TNW] |
| 2026-05-20 | Meta : 8 000 licenciements, 6 000 postes ouverts annulés | [SRC-LAT, SRC-TNW] |
| 2026-05-20 | Intuit : 3 000 suppressions (17 %), le CEO nie le rôle de l'IA | [SRC-REUI] |
| 2026-06 | Salesforce : ~1 000 postes (1,5 %), les agents IA gèrent ~50 % du support | [SRC-GUARD] |
| 2026-07-16 | Meta poursuivie : l'IA aurait sélectionné des salariés à problèmes de santé pour les licenciements | [SRC-LAT2] |
| 2026-08 + automne | Nouvelles vagues Meta annoncées (possible 20 % au total) | [SRC-TNW] |

---

## 8. DOMAINES

**Économique :** le rapport économies de licenciements / capex IA : Meta 3-8 Md$ / 125-145 Md$ (2-6 %) [FCT-005, FCT-003] ; Oracle ~8-10 Md$ de cash libéré annoncé pour un pivot AI 50 Md$ (sources secondaires) [FCT-024] ; IBM 67,5 Md$ de revenus 2025, +7,6 %, avec 13-17 000 suppressions [FCT-019, FCT-017] : la croissance et la réduction des effectifs coexistent.

**Social :** la polarisation du payroll dans l'entreprise : médiane Meta en baisse (417 400 $ en 2024, 388 200 $ en 2025, -7 %), réductions des augmentations en actions (-10 % puis -5 %), pendant que les chercheurs IA reçoivent des packages jusqu'à 100 M$ [FCT-008, FCT-009]. Le pipeline junior : IBM documente la rupture (gel 2023 → pénurie de vivier → triplement 2026) [FCT-016, FCT-018].

**Technique :** la « Model Capability Initiative » de Meta (capture clavier, souris, écran sur les postes des salariés US, avril 2026) : les salariés génèrent les données d'entraînement des agents qui automatisent leurs propres tâches [FCT-011]. La surveillance comme infrastructure du remplacement.

**Juridique :** poursuite de 26 ex-salariés Meta contre l'usage de l'IA dans la sélection des licenciés [FCT-030] ; question écrite de Ruffin sur Teleperformance (598 postes déjà supprimés sur 1 860) [FCT-027]. Le droit du travail français (PSE, départs volontaires) encadre la forme, pas le fond : les non-remplacements échappent au contrôle.

**France :** Teleperformance : plan visant un tiers des effectifs hexagonaux (nov. 2024), 3 300 postes supprimés « au profit de l'IA » (mars 2026), investissement annoncé de 600 M€ dans l'IA [FCT-027]. Le cas français est le plus explicite : le coût de l'IA est financé par la réduction de la masse salariale des téléconseillers.

**Discours (communication) :** quatre registres coexistants : substitution assumée (BT, Salesforce), compensation de coûts (Meta, Oracle), déni (Zuckerberg, Intuit), retournement (IBM). La même entreprise peut changer de registre : IBM a tenu les quatre en trois ans.

---

## 9. RÉSEAU D'ACTEURS

| Acteur | Rôle | Décision documentée | Documenté par |
|--------|------|---------------------|---------------|
| **Meta** | Cas complet du mécanisme | 8 000 postes, 6 000 reqs annulées, capex 125-145 Md$ | [SRC-LAT, SRC-TNW] |
| **Susan Li (CFO Meta)** | Porte-parole du lien | « offset its infrastructure investments », « optimal size inconnue » | [SRC-TNW] |
| **Mark Zuckerberg** | Décideur + déni | Confirme les coupes, nie le rôle de l'IA | [SRC-TNW] |
| **Marc Benioff (Salesforce)** | Substitution assumée | « I need less heads », « ne pas backfiller » | [SRC-CNBC] |
| **Arvind Krishna (IBM)** | Promesse puis correction | 7 800 postes (2023) ; triplement juniors via sa CHRO (2026) | [SRC-TL] |
| **Nickle LaMoreaux (CHRO IBM)** | Correction | « AI can do most of them », « totally different jobs » | [SRC-TL] |
| **Philip Jansen (BT)** | Substitution annoncée | 10 000 postes remplacés par l'IA | [SRC-GUAR] |
| **Jamie Dimon (JPMorgan)** | Prophétie | « chômage massif », « plus de brainiacs, moins de banquiers » | [SRC-FORTD] |
| **Alexandr Wang (Superintelligence Labs)** | Réceptacle des réaffectés | équipes « pods » IA ; packages 100 M$ | [SRC-TNW] |
| **Salariés Meta** | Objet de la surveillance | pétition, poursuite, sites de compte à rebours | [SRC-LAT, SRC-TNW] |
| **Ed Zitron (analyste)** | Contre-thèse | « l'IA est un prétexte aux ajustements de sur-embauche » | [SRC-CNBC] |
| **Teleperformance (France)** | Cas français | 3 300 postes pour l'IA, 600 M€ IA | [SRC-LIBE] |

**CONTROL_MAP :** points de contrôle : (1) le conseil d'administration et le CFO (allocation du budget) ; (2) le CEO (décision et cadrage) ; (3) la DRH (sélection des partants, y compris par algorithme selon la poursuite Meta) ; (4) les salariés (aucun contre-pouvoir documenté hors pétition/poursuite) ; (5) l'État (France : PSE encadrent la forme ; rien sur le non-remplacement).

---

## 10. CHAÎNES / PELOTE

```
CAU-001 (le trou comblé partiellement) :
  Capex IA ↑ (Meta 39,2 → 72,2 → 125-145 Md$)
  + discours « offset » (Li)
  + effectifs ↓ (8 000 + 6 000 reqs)
  + réaffectation interne (7 000 vers l'IA)
  → réallocation du dollar marginal du payroll vers le compute
  → PAS une ligne budgétaire tracée, PAS un financement des capex (2-6 %)

CAU-002 (le pipeline junior, validé par IBM) :
  Automatisation des tâches juniors (IBM 2023 : 7 800 postes)
  → gel des embauches d'entrée
  → pénurie de vivier (13-17 000 départs 2024-25)
  → retournement (triplement des embauches juniors, fév. 2026)
  → le gain court terme détruit la chaîne de fabrication des seniors

CAU-003 (la mécanique de déni) :
  Réduction d'effectifs décidée (Intuit 3 000, Meta 8 000)
  + refus de nommer l'IA (Zuckerberg, CEO Intuit)
  → l'IA sert d'alibi aux investisseurs et de déni aux salariés
  → l'attribution causale devient indécidable de l'extérieur

CAU-004 (le remplacement comme non-événement) :
  Départ (retraite, démission)
  → pas de remplacement (« ne pas backfiller », Salesforce ; reqs annulées, Meta)
  → poste supprimé sans licenciement
  → invisible pour la statistique publique française (cf. INV non-remplacements)
```

**PELOTE / SOURCE_PROVENANCE :** les chiffres d'effectifs Meta (87 314 → 67 317 → 74 067 → 76 834 → ~80 000) viennent d'agrégateurs (Macrotrends, SQ Magazine) non audités contre les 10-K ; les estimations d'économies (Evercore 3 Md$, BofA 7-8 Md$) sont des analyses de banques rapportées par la presse, pas des comptes officiels ; le « 30 000 » Oracle est une estimation de site de recrutement (kore1), le chiffre CNBC est « des milliers » ; le total Layoffs.fyi (110 000 en 2026) est un agrégateur communautaire.

---

## 11. CARTE DES PREUVES

### LEAD_REGISTRY

| ID | Lead | Statut |
|----|------|--------|
| LED-001 | Trou causal CAPEX → masse salariale | SATURATED (partiel : discours + temporalité + ampleur documentés ; chaîne budgétaire intégrale non tracée) |
| LED-002 | « Les licenciements financent les capex » | SATURATED (réfuté en volume : 2-6 %) |
| LED-003 | Pipeline junior endommagé | SATURATED (preuve empirique IBM) |
| LED-004 | Déni managérial de l'IA | SATURATED (Zuckerberg, Intuit) |
| LED-005 | Polarisation du payroll | SATURATED (Meta : médiane ↓, chercheurs IA ↑) |

### CLAIM_REGISTRY

| ID | Claim | Support | Contre | Verdict |
|----|-------|---------|--------|---------|
| CLM-001 | La chaîne complète budget→capex↑→payroll↓→commentaire est documentée pour au moins une entreprise | FCT-001 à FCT-007 (Meta : discours Li + temporalité + chiffres) | Pas de 10-K analysé ligne à ligne ; « offset » ≠ preuve comptable | **VÉRIFIÉ (partiel)** |
| CLM-002 | Les économies de licenciements financent les capex IA | FCT-005 (3-8 Md$ vs 125-145 Md$) | Ratio = 2-6 % : le financement est symbolique | **RÉFUTÉ (en volume), VÉRIFIÉ (en signal)** |
| CLM-003 | L'IA est la cause principale des réductions 2025-2026 | FCT-001, FCT-013, FCT-017, FCT-022 (discours explicites) | Taux de base attrition ; dénis ; Zitron | **VÉRIFIÉ (corrélation + discours), causalité non isolée** |
| CLM-004 | L'automatisation des tâches juniors endommage le pipeline de seniors | FCT-016, FCT-017, FCT-018 (IBM : gel → pénurie → triplement) | Un seul cas complet (IBM) | **VÉRIFIÉ (empirique, n=1 solide)** |
| CLM-005 | Le payroll se polarise : compression du milieu, explosion du haut | FCT-008, FCT-009 (médiane -7 %, packages 100 M$) | Chiffres internes Meta non audités | **VÉRIFIÉ (partiel)** |
| CLM-006 | Le remplacement par non-réaffectation est le mécanisme dominant | FCT-002, FCT-014 (6 000 reqs annulées, « ne pas backfiller ») | Les licenciements restent le fait visible | **VÉRIFIÉ (complémentaire au licenciement, pas dominant mesurable)** |

### FACT_REGISTRY_V1

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.latimes.com/business/story/2026-05-20/meta-begins-8-000-global-job-cuts-in-ai-efficiency-push | C | 2026-05-20 | meta-8000-cuts | 8 000 postes (10 % de ~80 000), 20 mai 2026 | 257111bf-b350-45ed-bda1-9971035c9d49
FCT-002 | FACT | ✧ | https://www.latimes.com/business/story/2026-05-20/meta-begins-8-000-global-job-cuts-in-ai-efficiency-push | C | 2026-05-20 | meta-6000-reqs | 6 000 postes ouverts annulés ; 7 000 réaffectés à l'IA | ca8edf93-e6af-4917-9b06-4b5dfbb85b48
FCT-003 | FACT | ✧ | https://thenextweb.com/news/meta-layoffs-8000-zuckerberg-ai-reality-may-2026 | C | 2026-05-18 | meta-capex-145b | 125-145 Md$ 2026 vs 72,2 Md$ 2025 vs 39,2 Md$ 2024 | 6ce5e8f8-142c-418f-8829-d6dd8ccaa35b
FCT-004 | FACT | ✧ | https://thenextweb.com/news/meta-layoffs-8000-zuckerberg-ai-reality-may-2026 | C | 2026-05-18 | meta-records-proits | Q1 2026 : 56,31 Md$ CA, 26,8 Md$ NI ; FY2025 : 201 Md$ (+22 %), FCF 43,6 Md$ | 885efe3a-10d4-4127-ae4d-3a5f1a6c5ee4
FCT-005 | FACT | ✧ | https://www.latimes.com/business/story/2026-05-20/meta-begins-8-000-global-job-cuts-in-ai-efficiency-push | C | 2026-05-20 | meta-economies-3-8md | Evercore ~3 Md$, BofA 7-8 Md$ ; 2-6 % du capex | 04ddf838-016b-4418-8bda-98f9f6e28937
FCT-006 | FACT | ✧ | https://thenextweb.com/news/meta-layoffs-8000-zuckerberg-ai-reality-may-2026 | C | 2026-05-18 | zuckerberg-deni | « AI tools... not the thing that's driving layoffs » (30/04/2026) | 3c1000c5-5056-41d0-9df0-fa42ec16f274
FCT-007 | FACT | ✧ | https://thenextweb.com/news/meta-layoffs-8000-zuckerberg-ai-reality-may-2026 | C | 2026-05-18 | li-offset | « leaner operating model... offset its infrastructure investments » | 5b46afc5-74cb-4459-95a3-ccdf54bcee8b
FCT-008 | FACT | ✧ | https://thenextweb.com/news/meta-layoffs-8000-zuckerberg-ai-reality-may-2026 | C | 2026-05-18 | meta-mediane-388k | Médiane 417 400 $ (2024) → 388 200 $ (2025) ; actions -10 % puis -5 % | 81b2b21e-3682-4cf6-ad09-2e6bc4a13918
FCT-009 | FACT | ✧ | https://thenextweb.com/news/meta-layoffs-8000-zuckerberg-ai-reality-may-2026 | C | 2026-05-18 | meta-100m-packages | Packages chercheurs IA jusqu'à 100 M$ (Superintelligence Labs) | 7ba1cefa-5a1a-499f-b961-ef6928268549
FCT-010 | FACT | ✧ | https://thenextweb.com/news/meta-layoffs-8000-zuckerberg-ai-reality-may-2026 | C | 2026-05-18 | meta-33000-depuis-2022 | 33 000 postes éliminés depuis 2022 (5 vagues) | d173e826-28e7-4265-b3dd-aa7c24cc3b6a
FCT-011 | FACT | ✧ | https://thenextweb.com/news/meta-layoffs-8000-zuckerberg-ai-reality-may-2026 | C | 2026-05-18 | meta-surveillance-MCI | Model Capability Initiative : clavier, souris, écran sur postes US (avril 2026) | 0391c92d-d55d-4774-ab9d-c49d58065ca8
FCT-012 | FACT | ✧ | https://thenextweb.com/news/meta-layoffs-8000-zuckerberg-ai-reality-may-2026 | C | 2026-05-18 | layoffs-fyi-2026 | ~110 000 postes à 137 entreprises en 2026 ; ~125 000 en 2025 | 7099dba6-00fc-45b6-995a-5da755762b73
FCT-013 | FACT | ✧ | https://www.cnbc.com/2025/09/02/salesforce-ceo-confirms-4000-layoffs-because-i-need-less-heads-with-ai.html | C | 2025-09-02 | benioff-less-heads | « 9,000 heads to about 5,000, because I need less heads » | 8a9f9756-9219-4845-a8ef-3512d357dc8e
FCT-014 | FACT | ✧ | https://www.cnbc.com/2025/09/02/salesforce-ceo-confirms-4000-layoffs-because-i-need-less-heads-with-ai.html | C | 2025-09-02 | salesforce-no-backfill | « no longer need to actively backfill support engineer roles » (Agentforce) | 90a6c3af-1032-4fb7-92ee-8a24a7056bf7
FCT-015 | FACT | ✧ | https://www.cnbc.com/2025/09/02/salesforce-ceo-confirms-4000-layoffs-because-i-need-less-heads-with-ai.html | C | 2025-09-02 | salesforce-ai-50pct | « AI is doing up to 50% of the work » (Benioff, été 2025) | 2e5b5e86-fa30-41f2-a00a-cfb058db205e
FCT-016 | FACT | ✧ | https://www.twinladder.ai/en/research/ibm-tripling-the-ladder | D | 2026-03-01 | ibm-7800-2023 | 7 800 postes, 30 % des 26 000 back-office, gel d'embauche (mai 2023) | 38a96b9e-e188-463a-9dd8-015c807214c7
FCT-017 | FACT | ✧ | https://www.twinladder.ai/en/research/ibm-tripling-the-ladder | D | 2026-03-01 | ibm-13-17k-cuts | 13 000-17 000 suppressions sept. 2024-mars 2025 (deux vagues) | dee8878a-0ab2-4516-9eb0-fa1d34be7f84
FCT-018 | FACT | ✧ | https://www.twinladder.ai/en/research/ibm-tripling-the-ladder | D | 2026-03-01 | ibm-triplement-juniors | Fév. 2026 : triplement des embauches juniors US (CHRO LaMoreaux) | 4b47c2c2-6866-4df4-822a-81318d9a4759
FCT-019 | FACT | ✧ | https://www.twinladder.ai/en/research/ibm-tripling-the-ladder | D | 2026-03-01 | ibm-2025-67md | Revenus 2025 : 67,5 Md$ (+7,6 %) avec effectifs réduits | 1484de10-e166-4715-99a9-5a1e155f4c7d
FCT-020 | FACT | ✧ | https://www.twinladder.ai/en/research/ibm-tripling-the-ladder | D | 2026-03-01 | ibm-logique-2023 | « Redirect billions in labour costs toward cloud and enterprise AI » | b6341fc8-f681-4c29-bef1-26e7b49d4aa9
FCT-021 | FACT | ⁅ | https://www.bbc.com/news/business-65631168 | C | 2023-05-18 | bt-55000-2030 | 55 000 postes d'ici 2030 (40 %), 10 000 remplacés par l'IA | -
FCT-022 | FACT | ⁅ | https://www.reuters.com/technology/sap-announces-company-wide-restructuring-updates-2025-outlook-2024-01-23/ | C | 2024-01-23 | sap-8000-restruct | 8 000 postes restructurés, coût 2 Md€, « Business AI » | -
FCT-023 | FACT | ⁅ | https://www.reuters.com/business/world-at-work/intuit-cut-17-global-jobs-streamline-operations-memo-shows-2026-05-20/ | C | 2026-05-20 | intuit-3000-deni | 3 000 postes (17 %), CEO : « pas l'IA » ; 1 800 en 2024 « autour de l'IA » | -
FCT-024 | FACT | ⁅ | https://www.cnbc.com/2026/03/31/oracle-layoffs-ai-spending.html | C | 2026-03-31 | oracle-30000 | « Des milliers » (CNBC) ; ~30 000/18 % (kore1) ; restructuration 2,1 Md$ au SEC | -
FCT-025 | FACT | ⁅ | https://www.cnbc.com/2026/04/23/microsoft-plans-first-voluntary-retirement-program-for-us-employees.html | C | 2026-04-23 | microsoft-retraite-vol | 1er programme retraite volontaire, ~7 % US (~8 750), senior director ou moins | -
FCT-026 | FACT | ⁅ | https://fortune.com/2026/01/22/jpmorgan-chase-ceo-jamie-dimon-ai-layoff-income-assist-workers-elon-musk-sam-altman-universal-basic-income/ | C | 2026-01-22 | dimon-chomage-massif | « Massive unemployment and a huge rise in profits » ; 300 M emplois exposés (mai 2026) | -
FCT-027 | FACT | ⁅ | https://www.liberation.fr/economie/economie-numerique/robotiser-lhumain-le-geant-des-centres-dappels-tp-va-supprimer-3-300-postes-au-profit-de-lia-20260320_7I5O5GCPOZCDBN4M6W33HJAVPE/ | C | 2026-03-20 | tp-3300-ia | Teleperformance : 3 300 postes « au profit de l'IA », 1/3 France (2024), 600 M€ IA | -
FCT-028 | FACT | ⁅ | https://www.facebook.com/SundayGuardian/posts/ | E | 2026-06-10 | salesforce-juin-2026 | ~1 000 postes (1,5 % de 72 680) ; agents IA ~50 % du support (source faible) | -
FCT-029 | FACT | ⁅ | https://sqmagazine.co.uk/meta-employee-count-statistics/ | D | 2026-08-03 | meta-effectifs | 87 314 (2022) → 67 317 (2023) → 74 067 (2024) → 76 834 (2025) | -
FCT-030 | FACT | ⁅ | https://www.latimes.com/business/story/2026-05-20/meta-begins-8-000-global-job-cuts-in-ai-efficiency-push | C | 2026-07-16 | meta-poursuite-ia | 26 ex-salariés : l'IA aurait ciblé des salariés à problèmes de santé | -
<!-- /FACT_REGISTRY_V1 -->

### TRACE_MATRIX (extrait)

| FCT | Support | Contre | REFUTATION_SEARCHED |
|-----|---------|--------|---------------------|
| FCT-001/003 | LA Times (fetch Bloomberg) + TNW (fetch) | Estimations de savings (Evercore/BofA) non officielles | QRY-REF-1 : « Meta layoffs 2026 pas liés à l'IA contestation » → NONE |
| FCT-013 | CNBC (fetch) | Benioff minimise ailleurs (« augmentation ») | QRY-REF-2 : « Benioff dément lien IA licenciements » → NONE (il le confirme au contraire) |
| FCT-016/017/018 | TwinLadder (fetch) | Un seul récit, source recherche non grand public | QRY-REF-3 : « IBM layoffs 2026 réembauche juniors » → concordant (Reuters/Bloomberg snippets) |
| FCT-021 | BBC/Guardian/Reuters (snippets concordants) | Annonce 2023, réalisations 2030 non connues | QRY-REF-4 : « BT 55 000 postes démenti » → NONE |
| FCT-024 | CNBC « des milliers » (snippet) | « 30 000 » uniquement kore1 (faible) | QRY-REF-5 : « Oracle 30 000 licenciements confirmé Reuters » → non confirmé au niveau Reuters |

### EDI (diversité du corpus)

| Dimension | État |
|-----------|------|
| Géographique | US dominant (Meta, Salesforce, IBM, Oracle, Microsoft, Intuit), UK (BT), Allemagne (SAP), France (Teleperformance) |
| Familles de provenance | C (CNBC, LA Times/Bloomberg, Reuters, BBC, Fortune), D (TwinLadder, SQ Magazine, kore1), E (Facebook/Sunday Guardian, faible) |
| Biais | Surreprésentation des médias financiers ; aucun 10-K lu en primaire ; les chiffres internes (7 000 réaffectés, médiane) viennent de fuites rapportées |
| GAP EDI | Aucun témoignage direct de salariés (hors citations rapportées) ; aucune donnée syndicale ; la perspective française limitée à Teleperformance |

---

## 12. CARTE DIALECTIQUE

**Scénario A (la réallocation devient la norme) :** les dix cas actuels se généralisent ; les entreprises compriment le milieu de grille, externalisent le reste vers l'IA, et le non-remplacement devient la voie dominante de réduction d'effectifs (invisible pour la statistique française).
**Scénario B (le retournement IBM généralisé) :** les entreprises découvrent le coût du pipeline junior détruit et réembauchent ; le cycle ressemble aux vagues d'automatisation passées (rejet partiel, hybridation) ; les économies annoncées ne se matérialisent pas (Klarna, CBA, Salesforce « plus dur que prévu »).
**Scénario C (le déni institutionnalisé) :** l'IA devient l'alibi universel : les réductions décidées pour d'autres raisons (sur-embauche pandémique, taux d'intérêt, pression des marchés) sont attribuées à l'IA, rendant toute évaluation causale impossible.

**Carte des responsabilités (ACT) :**

| ACT | Nom | Action documentée | Intention |
|-----|-----|-------------------|-----------|
| ACT-001 | Susan Li (Meta) | A justifié les effectifs réduits par « l'offset » des investissements | CLAIMED (citation) |
| ACT-002 | Mark Zuckerberg | A décidé 33 000 suppressions depuis 2022 en niant le rôle de l'IA | CLAIMED (discours contradictoire) |
| ACT-003 | Marc Benioff | A réduit le support de 9 000 à 5 000 « parce que j'ai besoin de moins de têtes » | PROVEN (citation directe) |
| ACT-004 | Arvind Krishna / Nickle LaMoreaux | A appliqué le gel 2023 puis a inversé (triplement juniors) | PROVEN (deux annonces) |
| ACT-005 | Conseils d'administration | Ont approuvé capex et plans sociaux en même cycle | UNKNOWN (procès-verbaux non publics) |

---

## 13. PÉRIMÈTRE & LIMITES

**Inclusions :** dix entreprises avec lien discours-emploi documenté (Meta, Salesforce, IBM, BT, SAP, Intuit, Oracle, Microsoft, JPMorgan, Teleperformance) ; période 2022-2026 ; analyse des registres discursifs, de la temporalité, des effectifs et des capex publiés.
**Exclusions :** les emplois créés par l'infrastructure IA (objet de XQ-F) ; le coût de la dette et le shadow funding (INV shadow-funding) ; la carte complète des flux (XQ-A) ; l'analyse 10-K ligne à ligne (prochaine passe).
**Limites d'accès :** GAP_TYPE=ACCESS : Reuters (401), Bloomberg, Les Echos, Le Monde, Libération (paywall), Yahoo Finance (consentement). Les faits FCT-021 à FCT-030 reposent sur des snippets concordants non fetchés : tiers ⁅, pas de write-back.
**Limites de méthode :** les estimations de savings (Evercore, BofA) sont des analyses de banques rapportées par la presse ; le « 30 000 » Oracle est non confirmé par Reuters ; le total Layoffs.fyi est un agrégateur communautaire ; la médiane Meta vient de fuites rapportées par TNW ; la causalité reste indécidable (dénis + taux de base).

---

## 14. ÉTAT DES CONNAISSANCES

**Connu (✧ ancrés, 20 faits) :** les chiffres Meta (8 000, 6 000 reqs, 7 000 réaffectés, capex 125-145 Md$, médiane, 33 000 depuis 2022, surveillance), les citations Li et Zuckerberg, Salesforce (9 000→5 000, « no backfill », 50 %), IBM (7 800, 13-17 000, triplement, 67,5 Md$), le ratio économies/capex 2-6 %, le total sectoriel 110 000/2026.
**Probable (⁅, snippets concordants) :** BT (55 000/10 000), SAP (8 000/2 Md€), Intuit (3 000/déni), Oracle (~30 000/2,1 Md$), Microsoft (7 % US), Dimon (300 M exposés), Teleperformance (3 300/600 M€), effectifs Meta 2022-2025, poursuite Meta.
**Inconnu :** la chaîne budgétaire intégrale (10-K non analysés) ; le coût total réel des restructurations (severance, pertes de productivité) ; les critères algorithmiques de sélection des licenciés ; la part des licenciements 2026 réellement causée par l'IA vs les ajustements classiques.
**Réfuté :** « les licenciements financent les capex » (2-6 %).

---

## 15. SUSPICION / VÉRIFICATION

**Audit des sources :** LA Times (Bloomberg wire) et TNW sont fiables sur les faits, interprétatifs sur le cadre (« converts payroll into AI capital expenditure » est un cadrage TNW, pas une citation) ; TwinLadder est un cas d'étude de recherche (famille D) dont les chiffres IBM concordent avec Reuters/Bloomberg (triplement des juniors rapporté ailleurs) ; kore1 (30 000 Oracle) est un site de recrutement à fiabilité faible, marqué ⁅ ; le Sunday Guardian (Salesforce juin) est de famille E, marqué ⁅.
**STATUS_DELTA :** aucun fait préexistant du corpus n'a changé de statut dans ce run ; les faits de la bulle-IA (capex 660-690 Md$) sont réutilisés tels quels comme contexte.
**CONTRADICTION_LEDGER :** la contradiction centrale est le déni (Zuckerberg, Intuit) contre l'attribution (presse, discours des autres CEO) : elle est documentée comme telle, pas résolue. La contradiction IBM (gel 2023 vs triplement 2026) est résolue par la correction stratégique. La contradiction « profits records + licenciements » (Meta) n'est pas une erreur comptable : c'est le signal de la réallocation.
**Contre-requêtes (REFUTATION_SEARCHED) :** 5 menées (QRY-REF-1 à 5). Résultat : aucune réfutation sur les chiffres pivots (8 000 Meta, 9 000→5 000 Salesforce, 7 800 IBM, 55 000 BT) ; le « 30 000 » Oracle n'est pas confirmé par les primaires (CNBC : « des milliers »), ce qui borne le fait à ⁅.

---

## SOURCES

| SRC-ID | Titre | Date | Rôle | URL |
|--------|-------|------|------|-----|
| SRC-LAT | LA Times (Bloomberg), « Meta begins 8,000 job cuts in AI efficiency push » | 2026-05-20 | ◉ (fetchée) | https://www.latimes.com/business/story/2026-05-20/meta-begins-8-000-global-job-cuts-in-ai-efficiency-push |
| SRC-TNW | TheNextWeb, « Meta begins cutting 8,000 jobs... $145 billion AI bet » | 2026-05-18 | ◉ (fetchée) | https://thenextweb.com/news/meta-layoffs-8000-zuckerberg-ai-reality-may-2026 |
| SRC-CNBC | CNBC, « Salesforce CEO confirms 4,000 layoffs because I need less heads » | 2025-09-02 | ◉ (fetchée) | https://www.cnbc.com/2025/09/02/salesforce-ceo-confirms-4000-layoffs-because-i-need-less-heads-with-ai.html |
| SRC-TL | TwinLadder, « Tripling the Ladder : how IBM reversed the most famous AI hiring freeze » | 2026-03-01 | ◉ (fetchée, recherche) | https://www.twinladder.ai/en/research/ibm-tripling-the-ladder |
| SRC-GUAR | The Guardian, « BT to axe up to 55,000 jobs by 2030 » | 2023-05-18 | ○ (snippet) | https://www.theguardian.com/business/2023/may/18/bt-cut-jobs-telecoms-group-workforce |
| SRC-BBC | BBC, « BT to cut 55,000 jobs with up to a fifth replaced by AI » | 2023-05-18 | ○ (snippet) | https://www.bbc.com/news/business-65631168 |
| SRC-REUSAP | Reuters, « SAP to restructure 8,000 jobs in push towards AI » | 2024-01-23 | ○ (snippet) | https://www.reuters.com/technology/sap-announces-company-wide-restructuring-updates-2025-outlook-2024-01-23/ |
| SRC-FORT | Fortune, « Intuit is laying off 1,800 employees as AI leads... » | 2024-07-10 | ○ (snippet) | https://fortune.com/2024/07/10/intuit-layoffs-email-hiring-ai-transformation/ |
| SRC-REUI | Reuters, « Intuit to cut 17% of global jobs » | 2026-05-20 | ○ (snippet, 401 non fetché) | https://www.reuters.com/business/world-at-work/intuit-cut-17-global-jobs-streamline-operations-memo-shows-2026-05-20/ |
| SRC-CNBCORA | CNBC, « Oracle cutting thousands in latest layoff round as AI spending soars » | 2026-03-31 | ○ (snippet) | https://www.cnbc.com/2026/03/31/oracle-layoffs-ai-spending.html |
| SRC-KORE1 | KORE1, « Oracle Layoffs 2026 : 30,000 cuts » | 2026-04-01 | ○ (snippet, fiabilité faible) | https://www.kore1.com/oracle-layoffs-2026/ |
| SRC-CNBCMS | CNBC, « Microsoft plans first voluntary retirement program » | 2026-04-23 | ○ (snippet) | https://www.cnbc.com/2026/04/23/microsoft-plans-first-voluntary-retirement-program-for-us-employees.html |
| SRC-FORTD | Fortune, « Dimon : AI will create massive unemployment » | 2026-01-22 | ○ (snippet) | https://fortune.com/2026/01/22/jpmorgan-chase-ceo-jamie-dimon-ai-layoff-income-assist-workers-elon-musk-sam-altman-universal-basic-income/ |
| SRC-NYP | NYPost, « Dimon : hire more AI brainiacs, fewer bankers » | 2026-05-21 | ○ (snippet) | https://nypost.com/2026/05/21/business/jamie-dimon-says-jpmorgan-will-hire-more-ai-braniacs-fewer-bankers/ |
| SRC-ECHOS | Les Echos, « Teleperformance veut sabrer dans ses effectifs en France » | 2024-11-19 | ○ (snippet, paywall) | https://www.lesechos.fr/industrie-services/services-conseils/le-geant-des-centres-dappels-teleperformance-veut-sabrer-dans-ses-effectifs-en-france-2132519 |
| SRC-LIBE | Libération, « Robotiser l'humain : TP va supprimer 3 300 postes au profit de l'IA » | 2026-03-20 | ○ (snippet, paywall) | https://www.liberation.fr/economie/economie-numerique/robotiser-lhumain-le-geant-des-centres-dappels-tp-va-supprimer-3-300-postes-au-profit-de-lia-20260320_7I5O5GCPOZCDBN4M6W33HJAVPE/ |
| SRC-RUFF | Facebook Ruffin, question écrite sur les téléconseillers | 2026-07 | ○ (snippet) | https://www.facebook.com/FrancoisRuffin80/posts/1594655845355512/ |
| SRC-GUARD | Sunday Guardian via Facebook, « Salesforce June 2026 layoffs » | 2026-06-10 | ○ (snippet, fiabilité faible) | https://www.facebook.com/SundayGuardian/posts/1012821928167488/ |
| SRC-SQMAG | SQ Magazine, « Meta Employee Count Statistics 2026 » | 2026-08-03 | ○ (snippet) | https://sqmagazine.co.uk/meta-employee-count-statistics/ |
| SRC-MACRO | Macrotrends, « Meta : number of employees » | 2026 | ○ (snippet) | https://www.macrotrends.net/stocks/charts/META/meta-platforms/number-of-employees |
| SRC-LAT2 | LA Times (article lié), « Meta accused of using AI to pick employees with medical conditions for layoffs » | 2026-07-16 | ○ (snippet) | https://www.latimes.com/business/story/2026-07-16/meta-ai-layoffs-medical-conditions |
| SRC-CONARD | Edward Conard, « $660bn spending spree » | 2026-02-06 | ○ (snippet, contexte) | https://www.edwardconard.com/macro-roundup/amazon-google-meta-and-microsoft-plan-to-spend-660b-on-capex-in-2026-... |

---

## REQUEST_LOG

ENGINE:2.8 | MANIFEST:FINAL | RUN_ID:20260824-1700-capex-ia-masse-salariale | PARENT_RUN_ID:20260824-leffondrement-modele-salarial | AS_OF:2026-08-24 | INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:XQ-C
CHECKPOINT_SEQ:1 | LAST_COMPLETED:18b | NEXT_ACTION:NONE | RESUME_COUNT:0
Investigation:capex-ia-masse-salariale | complexity:16→APEX | route overrides:NONE | scope:2022→2026-08, US+UK+DE+FR
modules:SYMBOLS,PATTERNS,THREATS,GATES,REQUEST_LOG,FACT_VERIFICATION,TEMPLATE,INVESTIGATION(partiel),MONEY,POWER,ICEBERG,FRAMING,TEMPORAL
degraded:NONE | query target/actual:10/14 (4 requêtes exploratoires au-delà de la cible)

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL/INPUT_REF |
|---:|-----|-----------------|--------|--------|---------------|
| 1 | SYS | @MNEMO_Q (recherche mémoire, 1 fois/RUN_ID) | FOUND : contexte faits capex/revenus ancrés (bulle-IA) ; aucun doublon direct | MnemoLite | - |
| 2 | ◉ | QRY-001 : BT AI 10 000 jobs 55 000 headcount | FOUND : Guardian, BBC, Reuters, Forbes concordants | SRC-GUAR, SRC-BBC | - |
| 3 | ◉ | QRY-002 : SAP 8 000 restructuration IA | FOUND : Reuters, WSJ, CNN | SRC-REUSAP | - |
| 4 | ◉ | QRY-003 : Intuit 1 800 puis 3 000 | FOUND : Fortune 2024, Reuters 2026, hcamag (accords Anthropic/OpenAI) | SRC-FORT, SRC-REUI | - |
| 5 | ◉ | QRY-004 : IBM 30 % back-office gel | FOUND : Bloomberg, Reuters, Al Jazeera ; TwinLadder (cas complet) | SRC-TL | - |
| 6 | ◉ | QRY-005 : Meta capex/effectifs/layoffs 2026 | FOUND : Reuters, LA Times, TNW, LAT | SRC-LAT, SRC-TNW | - |
| 7 | ◉ | QRY-006 : Teleperformance IA France | FOUND : Les Echos, Le Monde, Libération, Ruffin | SRC-ECHOS, SRC-LIBE | - |
| 8 | ◉ | QRY-007 : Salesforce Benioff less heads | FOUND : CNBC (fetché), Reddit (9 000→5 000), ODSC | SRC-CNBC | https://www.cnbc.com/2025/09/02/salesforce-ceo-confirms-4000-layoffs-because-i-need-less-heads-with-ai.html |
| 9 | ◉ | QRY-008 : Oracle 30 000 mars 2026 | FOUND : CNBC, Reuters (des milliers), kore1 (30 000), AI For Real (SEC 2,1 Md$) | SRC-CNBCORA | - |
| 10 | ◉ | QRY-009 : Microsoft retraite volontaire 7 % | FOUND : CNBC, Bloomberg, GeekWire, eMarketer (capex 105 Md$) | SRC-CNBCMS | - |
| 11 | ◉ | QRY-010 : JPMorgan Dimon IA emplois | FOUND : Fortune Davos, NYPost 300 M, Banking Dive | SRC-FORTD, SRC-NYP | - |
| 12 | ◉ | FETCH-1 : LA Times Meta (primaire) | OK (Bloomberg wire intégral) | SRC-LAT | - |
| 13 | ◉ | FETCH-2 : TNW Meta (primaire) | OK (intégral) | SRC-TNW | - |
| 14 | ◉ | FETCH-3 : CNBC Benioff (primaire) | OK (intégral) | SRC-CNBC | - |
| 15 | ◉ | FETCH-4 : TwinLadder IBM (primaire) | OK (intégral, tronqué sur la fin) | SRC-TL | - |
| 16 | ◉ | FETCH-5 : Reuters Intuit (primaire) | 401 Forbidden (paywall/bot) → ⁅ | SRC-REUI | - |
| 17 | ✧ | QRY-REF-1 : « Meta layoffs 2026 pas liés à l'IA » | NONE (aucune réfutation trouvée) | - | - |
| 18 | ✧ | QRY-REF-2 : « Benioff dément lien IA licenciements » | NONE (il le confirme au contraire) | - | - |
| 19 | ✧ | QRY-REF-3 : « IBM réembauche juniors 2026 » | Concordant (Reuters/Bloomberg) | SRC-TL | - |
| 20 | ✧ | QRY-REF-4 : « BT 55 000 démenti » | NONE | - | - |
| 21 | ✧ | QRY-REF-5 : « Oracle 30 000 confirmé Reuters » | Non confirmé au niveau Reuters (CNBC : « des milliers ») → borne ⁅ | - | - |
| 22 | SYS | @WRITE (write-back Mnemolite) | 20 faits ✧ écrits, memory_ids rebindés | MnemoLite | - |
| 23 | SYS | @GATE (19a + 19b) | PASS déterministe, worktree te-capex-ia-20260824, STATE_ID 89db824e | verify.py | - |
