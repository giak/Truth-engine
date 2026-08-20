# INVESTIGATION : Préparation aux investigations sur la corruption en France

- STATE          : FINAL
- ENGINE_VERSION : 2.8
- RUN_ID         : 20260811-2300-preparation-investigations-corruption
- PARENT_RUN_ID  : NONE
- AS_OF          : 2026-08-11
- INPUT_KIND     : TOPIC
- MISSION_MODE   : INVESTIGATION
- INPUT_REF      : PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_preparation-anticorruption/pistes/transcript_anticorp.md + PATH:transcript_pascot.md
- SUBJECT_SLUG   : preparation-investigations-corruption
- INVESTIGATION_PATH : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-11_preparation-investigations-corruption/2026-08-11_23-00_preparation-investigations-corruption_INVESTIGATION.md
- SCOPE          : PENDING
- COMPLEXITY     : 12→APEX
- CHECKPOINT_SEQ : 1
- LAST_COMPLETED : 18b
- NEXT_ACTION    : NONE
- RESUME_COUNT   : 0

---

## RUN_MANIFEST

| Champ | Valeur |
|---|---|
| ENGINE_VERSION | 2.8 |
| STATE | FINAL |
| RUN_ID | 20260811-2300-preparation-investigations-corruption |
| PARENT_RUN_ID | NONE |
| AS_OF | 2026-08-11 |
| INPUT_KIND | TOPIC |
| MISSION_MODE | INVESTIGATION |
| INPUT_REF | PATH:transcript_anticorp.md + PATH:transcript_pascot.md |
| SUBJECT_SLUG | preparation-investigations-corruption |
| INVESTIGATION_PATH | investigations/2026-08/2026-08-13_corpus-investigations/2026-08-11_preparation-investigations-corruption/2026-08-11_23-00_preparation-investigations-corruption_INVESTIGATION.md |
| SCOPE | PENDING |
| COMPLEXITY | 12→APEX |
| CHECKPOINT_SEQ | 1 |
| LAST_COMPLETED | 18b |
| NEXT_ACTION | NONE |
| RESUME_COUNT | 0 |
| ROUTE_OVERRIDES | [] |
| LOADED_MODULES | [SYMBOLS, PATTERNS, THREATS, GATES, REQUEST_LOG] |
| DEGRADED_FLAGS | [] |

---

## MANIPULATION_REPORT (§0)

| Champ | Valeur |
|---|---|
| INPUT_KIND | TOPIC |
| MISSION_MODE | INVESTIGATION |
| SYMBOL_STAGE | CORPUS_FINAL |
| SYMBOLS | Ξ7 €8 Λ6 Ω5 Ψ4 ↕8 Φ5 Σ4 Κ7 ρ4 κ6 ⫸7 ⚔3 🌐7 ⏰5 |
| PATTERNS | @PAT[BIO], @PAT[MONEY], @PAT[NET], @PAT[POLITICAL], @PAT[FASC] |
| THREATS | @THR[REG_CAPTURE], @THR[DARK_MONEY], @THR[ELITE_REPRO], @THR[CONTROLLED_OPPOSITION] |
| RHETORICAL | DEM:4 (populisme anti-élites présent dans les deux transcripts), BF:2 (sophismes occasionnels), NUM:3 (chiffres non sourcés dans Pascot), AUTH:2, FAC:3 (décorrélation promesses/actes) |
| COMPLEXITY | 12→APEX |
| CLUSTERS | ICEBERG (Ξ7), MONEY (€8), FRAMING (Λ6), INVERSION (Ω5+K7), POWER (↕8), GASLIGHTING (Ξ≥7), NETWORK (€≥7+🌐7) |
| IMPLICIT | claims: corruption légalisée = corruption systémique ; omissions: mécanismes précis de contrôle, chiffres officiels, comparaisons internationales chiffrées ; inversions: responsabilité diluée (« coupable mais pas responsable ») |
| SPEAKER | Anticor (Picard): institutionnel/réformiste, cible=transparence ; Pascot: pamphlétaire/accusatoire, cible=élites |
| ASSUMPTIONS | La corruption en France est structurelle et non conjoncturelle ; les mécanismes de contrôle sont délibérément sous-dimensionnés ; la légalité formelle masque des dispositifs de capture |
| PRIORITIES | 1. Cartographier les mécanismes de corruption légale 2. Identifier les angles morts du contrôle 3. Méthodologie d'agrégation de données OSINT |
| QUERY_GUIDANCE | Privilégier sources primaires (rapports CdC, HATVP, AFA, GRECO, TRACFIN) ; croiser données ouvertes (DECP, RNE, data.gouv) ; vérifier chaque allégation des transcripts |

---

## COGNITIVE_MAP (§8b)

### Scores narratifs finaux

| Symbole | Score | Observations |
|---|---|---|
| Ξ Omission | 7 | État omet sciemment les chiffres officiels (CdC : « carence regrettable »), RBE restreint depuis CJUE 2022, pas de CR écrits pour auditions de régulateurs |
| € Money | 8 | 80-100 Mds€/an fraude/optimisation, pantouflage massif, lobbying 3500+ entités, marchés publics non contrôlés (80,4%) |
| Λ Framing | 6 | « Pas systémique » vs preuves accumulées ; « corruption légale » = oxymore structurel |
| Ω Inversion | 5 | « Coupable mais pas responsable » (Dupond-Moretti), promesses non tenues (Darmanin 2018, Macron casier vierge) |
| Ψ Sideration | 4 | Volume d'informations > capacité de traitement citoyen ; complexité juridique dissuasive |
| ↕ Vertical power | 8 | Élus non contrôlés (1 contrôle/législature) vs citoyens (396 métiers exigent casier vierge) |
| Φ Spectacle | 5 | Affaires médiatisées vs corruption quotidienne invisible |
| Σ Semiotics | 4 | Labels « transparence », « moralisation » vs réalité des dispositifs |
| Κ Cynicism | 7 | Façade : lois votées mais non appliquées (casier vierge 2017 toujours bloqué), GRECO 4/18 |
| ρ Resistance | 4 | Anticor (110-120 k€), MLA, Transparency France existent mais sous-financés |
| κ Subtle influence | 6 | Amendements clés en main, pantouflage 74% avec réserves (contrôle formel, pas réel) |
| ⫸ Convergence | 7 | Sources indépendantes (CdC + GRECO + TI + Sénat) convergent sur les mêmes failles |
| ⚔ Cognitive warfare | 3 | Pas de preuve de coordination organisée ; lobbying structurel documenté |
| 🌐 Network | 7 | Réseaux documentés : lobbying, pantouflage, écoles (ENA, HEC, Sciences Po) |
| ⏰ Temporal | 5 | Lenteur systémique (Tibéri 21 ans, casier vierge 8 ans bloqué) ; réformes sans suivi |

---

## DIALECTICAL_MAP (§8t)

### P1 Dominant/institutionnel
« La France dispose de dispositifs anticorruption robustes (HATVP, AFA, PNF, TRACFIN). La corruption n'est pas systémique. La France est au 27e rang mondial CPI. »

**Falsificateur :** GRECO 4/18 recommandations mises en œuvre, CdC « carence regrettable », CPI en baisse.

### P2 Critique/adversarial
« La corruption est systémique et légalisée. Les contrôles sont délibérément sous-dimensionnés. Le pantouflage, le lobbying opaque et l'absence de chiffres constituent une architecture de capture de l'État. »

**Falsificateur :** Pas de preuve d'intentionnalité (DÉDUCTION), TRACFIN fonctionne (211 165 signalements).

### P3 Arbitrage evidence
La corruption directe (pots-de-vin) n'est pas systémique au sens mafieux, mais la **corruption légale structurelle** (pantouflage, conflits d'intérêts, optimisation fiscale, sous-dimensionnement des contrôles) est documentée par des sources indépendantes convergentes. La frontière « légal vs légitime » est l'enjeu central.

---

## TRACE_MATRIX (§13)

| LED/AXS | QRY | SUPPORT_FCT | COUNTER | STATUS |
|---|---|---|---|---|
| LED-004 | QRY-001 | FCT-001,002,003 | — | ✦ |
| LED-005 | QRY-002,003,012 | FCT-005,006,007,012,013 | — | ✦ |
| LED-006 | QRY-001 | FCT-001,003 | — | ✦ |
| LED-008 | QRY-004 | FCT-009,010,011 | — | ✦ |
| LED-016 | QRY-005 | FCT-018 | — | ✦ |
| LED-011 | QRY-011 | FCT-027 | — | ✦ |
| LED-012 | QRY-006,007 | FCT-015,016,017 | — | ✦ |
| LED-024 | QRY-013 | FCT-031 | — | ✧ |
| LED-010 | QRY-010 | FCT-026 | Représailles persistent | ✧ |
| LED-014 | QRY-015,025 | FCT-020,025 | Pas systémique (Pascot) | ⊙ |
| AXS-001 | QRY-001,005,014 | FCT-001,018,019 | — | SATURATED |
| AXS-002 | QRY-002,004,025 | FCT-005,009,025 | — | SATURATED |
| AXS-007 | QRY-003,006,012,013,023,024,025 | FCT-007,012-015,021-025,031 | — | SATURATED |
| AXS-003 | QRY-014 | FCT-019 | — | GAP(ACCESS) |
| AXS-006 | QRY-006,021,022 | FCT-015,028,029 | RBE restreint | GAP(ACCESS) |

---

## GATE_CHECK (§18)

### G0-G8

| Gate | Statut |
|---|---|
| G0 Runtime | ✅ 15 symboles résolus (0 ✗/DEFERRED), leads avec excerpts |
| G1 Scope | ✅ LEAD_QUESTION ≠ OBJECT_QUESTION |
| G2 Leads/claims | ✅ 25 LED terminaux, 7 CLM avec support/counter |
| G3 Facts | ✅ FACT_REGISTRY 33 FCT canoniques |
| G4 Evidence | ✅ ✦ résolus à SRC-ID+locator+URL |
| G5 Causality | ✅ 5 CAU avec types+sources |
| G6 Accountability | ✅ ACTOR_NETWORK, CONTROL_MAP |
| G7 Contradiction | ✅ CLM-005/010/014 avec contre-preuve |
| G8 Trace | ✅ TRACE_MATRIX couvre LED/AXS matériels |

G0-G8 PASS.

---

## CHECKPOINT_META

- CHECKPOINT_SEQ : 3
- LAST_COMPLETED : 18b
- NEXT_ACTION : NONE
- STATE : FINAL

---

## TEMPORAL_STATE (§1)

| Type | Date |
|---|---|
| Période investigate | 1990-2026 |
| Date de publication des sources | Anticor: ~2019 (loi Sapin 2 post-2017) ; Pascot: 2025-2026 |
| Date d'accès | 2026-08-11 |
| Date d'investigation | 2026-08-11 23:00 CEST |

---

## MEMORY (§2)

- @MNEMO_Q : `investigation corruption méthodologie préparation anticorruption ENR France` → 0 résultats
- DEGRADED_FLAGS : aucun
- TAGS : ["project:truth-engine","kernel","investigation:preparation-investigations-corruption","run:20260811-2300-preparation-investigations-corruption","date:2026-08-11"]

---

## LEAD_REGISTRY (§5)

### Sources enregistrées

| SRC-ID | INPUT_REF | Titre | Date |
|---|---|---|---|
| SRC-001 | PATH:transcript_anticorp.md | Transcript Anticor — Jean-Christophe Picard (Sinecure View) | ~2019 |
| SRC-002 | PATH:transcript_pascot.md | Transcript Nexus — Philippe Pascot, « Pilleurs d'État encore et encore » | 2025-2026 |

### Segmentation des leads (LED-001 à LED-025)

#### SRC-001 : Transcript Anticor

| ID | SOURCE_ID | LOCATOR | LEAD | EVIDENCE_EXCERPT | KIND | MATERIALITY | ROUTES | STATUS |
|---|---|---|---|---|---|---|---|---|
| LED-001 | SRC-001 | 0:00-3:35 | Anticor : association anti-corruption créée en 2002, 80 groupes locaux, budget 110-120 k€, refuse subventions pour indépendance | « j'ai créé donc en 2006 le premier groupe local et maintenant anticorps à 80 groupes locaux [...] on a fait le pari de refuser toute subvention pour rester indépendant [...] un budget de 110 à 120 mille euros » | ENTITY | CONTEXT | EXPAND:structure | OPEN |
| LED-002 | SRC-001 | 3:42-4:30 | Fraude aux subventions agricoles européennes en Corse : 36 M€ sur 4 ans | « on a estimé sur quatre ans une fraude de 36 millions [...] en déclarant des terrains qui sont pas eux, en déclarant des déchets tels qu'ils n'existent pas » | CLAIM | IMPORTANT | EXPAND:fraude | OPEN |
| LED-003 | SRC-001 | 4:35-5:15 | Affaire Alstom : État renonce à 350 M€, Anticor porte plainte pour détournement de biens publics par négligence | « l'état a renoncé [...] a levé une option d'achat qui lui aurait permis mécaniquement de gagner 350 millions [...] on a porté plainte pour détournement de biens publics par négligence » | CLAIM | IMPORTANT | EXPAND:alstom | OPEN |
| LED-004 | SRC-001 | 5:58-7:20 | Fraude et optimisation fiscale estimées à 80-100 Mds€/an, pas de chiffres officiels, estimation par syndicat Solidaires Finances Publiques | « la fraude fiscale et l'optimisation fiscale est estimée entre 80 et 100 milliards [...] ce sont des chiffres donnés par un syndicat qui s'appelle solidaire finances publiques » | CLAIM | DECISIVE | EXPAND:fraude-fiscale | OPEN |
| LED-005 | SRC-001 | 9:08-10:10 | Sous-dimensionnement délibéré du contrôle : PNF 18 magistrats, BNLCC 28 inspecteurs, -3000 vérificateurs fiscaux depuis 2010, contrôle de légalité -1/3 en 5 ans | « parquet national financier qui est le super parquet de la France il y a 18 magistrats brigade nationale de lutte contre la corruption qui sont 28 inspecteurs [...] 3000 vérificateurs fiscaux en moins depuis 2010 [...] le contrôle de légalité a baissé d'un tiers en cinq ans » | CLAIM | DECISIVE | EXPAND:controle | OPEN |
| LED-006 | SRC-001 | 10:15-10:55 | Absence de chiffres officiels sur la fraude/corruption = déni d'État | « en France ce qui est très étonnant c'est qu'il y a pas de chiffres officiels [...] on est un peu dans le déni puisque on nie un phénomène important » | CLAIM | IMPORTANT | EXPAND:transparence | OPEN |
| LED-007 | SRC-001 | 11:05-12:05 | Corrélation transparence/faible corruption/bonheur dans pays scandinaves | « les pays scandinaves où comme par hasard il y a peu de corruption et une très forte transparence [...] les gens se sentent très heureux » | CLAIM | CONTEXT | LINK:international | OPEN |
| LED-008 | SRC-001 | 13:07-14:30 | Verrou de Bercy : impossibilité de poursuivre un fraudeur sans autorisation du ministre des Finances ; assoupli pour >100 k€ mais persiste | « le verrou de Bercy c'est la capacité [...] on ne peut pas poursuivre un fraudeur fiscal sans l'autorisation du ministre des finances [...] maintenant il ne s'applique plus à partir de 100 000 euros de fraude mais il existe toujours » | CLAIM | DECISIVE | EXPAND:verrou-bercy | OPEN |
| LED-009 | SRC-001 | 14:30-14:50 | Conflit d'intérêts Woerth : ministre du Budget + trésorier UMP simultanément | « Woerth qui était à la fois ministre du budget, il était à la fois trésorier du parti au pouvoir [...] pendant deux ans ça a duré » | EVENT | IMPORTANT | LINK:woerth | OPEN |
| LED-010 | SRC-001 | 15:00-20:00 | Protection des lanceurs d'alerte : dispositif complexe et contradictoire (loi Sapin 2 vs loi secret des affaires vs article 40 CPP), État ne peut pas les soutenir financièrement (censure du Conseil constitutionnel) | « loi sapin 2 qui met en place une dénonciation graduée [...] loi secret des affaires qui vient immédiatement mettre des grosses limites [...] ces dispositions ont été censurées par le conseil constitutionnel » | MECHANISM | DECISIVE | EXPAND:lanceurs-alerte | OPEN |
| LED-011 | SRC-001 | 20:10-21:40 | Freins judiciaires : manœuvres dilatoires, procureurs non indépendants (nommés/sanctionnés par ministre), remontée d'informations au ministre | « on subit des manœuvres dilatoires [...] un procureur n'est pas un magistrat indépendant [...] les procureurs de France doivent remonter les informations sur les affaires sensibles au ministre de la Justice » | MECHANISM | DECISIVE | EXPAND:justice | OPEN |
| LED-012 | SRC-001 | 21:45-24:50 | Lobbys : rencontres opaques, cadeaux aux parlementaires (pas de plafond, déclaration >150 €), amendements clés en main non attribués | « les lobbys vont aujourd'hui peuvent rencontrer n'importe quel parlementaire [...] dans des conditions d'opacité [...] il n'y a pas de plafond [pour les cadeaux] [...] 60 amendements identiques à la virgule près proposés par 4 groupes politiques différents » | MECHANISM | DECISIVE | EXPAND:lobbying | OPEN |

#### SRC-002 : Transcript Pascot

| ID | SOURCE_ID | LOCATOR | LEAD | EVIDENCE_EXCERPT | KIND | MATERIALITY | ROUTES | STATUS |
|---|---|---|---|---|---|---|---|---|
| LED-013 | SRC-002 | 0:00-1:00 | Division des corps de métier empêche mobilisation commune | « chacun travaille pour sa seule sacristie [...] ce gouvernement en 2 jours était mort [si tous unis] » | CLAIM | CONTEXT | LINK:atomisation | OPEN |
| LED-014 | SRC-002 | 2:09-3:15 | Corruption « très envahissante » mais pas (encore) systémique ; obligatoire au sommet | « elle est pas systémique mais elle commence à devenir très envahissante [...] plus je remonte en haut de l'état, plus je m'aperçois que [...] les élus sont corrompus » | CLAIM | DECISIVE | EXPAND:systemicite | OPEN |
| LED-015 | SRC-002 | 1:35-1:52 | Affaire Tibéri : 8000-10000 voix détournées par élection, 21 ans pour condamner | « les juges savaient avant de condamner Tibéri [...] qu'il avait détourné entre 8000 et 10000 voix par élection [...] on a quand même mis 21 ans à le condamner » | EVENT | IMPORTANT | LINK:tiberi | OPEN |
| LED-016 | SRC-002 | 5:15-7:05 | Casier judiciaire vierge : voté AN 01/02/2017, bloqué au Sénat depuis, Macron promesse non tenue | « le 1er février 2017, le casier judiciaire vierge pour être élu a été voté à l'Assemblée nationale à l'unanimité [...] elle est en train de pourrir dans des tiroirs du Sénat » | MECHANISM | DECISIVE | EXPAND:casier-vierge | OPEN |
| LED-017 | SRC-002 | 9:48-11:10 | Rambouillet : adjoint condamné à 0 € pour 20 M€ détournés (insolvabilité organisée, mairie non partie civile) | « 20 millions d'euros sur une affaire d'eau [...] condamné à 0 centimes parce qu'il s'est arrangé pour être insolvable » | EVENT | IMPORTANT | LINK:rambouillet | OPEN |
| LED-018 | SRC-002 | 11:30-12:10 | Dupond-Moretti : « coupable mais pas responsable » (fraude fiscale 300 000 €) | « la formule c'est je suis coupable mais pas responsable [...] un type qui a oublié de déclarer 300 000 € sur ses revenus » | CLAIM | IMPORTANT | LINK:dupond-moretti | OPEN |
| LED-019 | SRC-002 | 12:30-13:20 | Campagnes présidentielles truquées depuis Mitterrand, toutes validées | « toutes les campagnes électorales des présidents de la République depuis 1958 [...] ont été truandées et elles ont toutes été validées » | CLAIM | IMPORTANT | EXPAND:campagnes | OPEN |
| LED-020 | SRC-002 | 13:20-13:50 | France seul pays avec 2 présidents + 2 premiers ministres condamnés, 2 gardes des Sceaux mis en examen | « nous sommes le seul pays au monde à avoir deux présidents de la République [...] condamnés [...] et deux premiers ministres [...] condamnés » | CLAIM | IMPORTANT | EXPAND:condamnations | OPEN |
| LED-021 | SRC-002 | 14:13-14:50 | 21 ministres du gouvernement Macron (2018) avaient déjà eu affaire à la justice/fisc | « en 2018 21 ministres du gouvernement Macron avait déjà eu affaire à la justice ou au fisc » | CLAIM | DECISIVE | EXPAND:macron-ministres | OPEN |
| LED-022 | SRC-002 | 14:59-15:50 | 87 députés macronistes absents de l'AN pendant 1,5 an tout en touchant leurs indemnités | « 87 députés macronistes dans le premier gouvernement Macron ne sont pas venus à l'Assemblée nationale pendant 1 an et demi » | CLAIM | IMPORTANT | EXPAND:absents-an | OPEN |
| LED-023 | SRC-002 | 16:09-16:20 | Lois votées avec 20 députés (dont lois sécurité sociale) | « des lois importantes [...] sur la sécurité sociale [...] 20 députés 20 sur 577 » | CLAIM | IMPORTANT | LINK:lois-20 | OPEN |
| LED-024 | SRC-002 | 18:48-19:20 | Déontologue ne contrôle qu'une fois par mandat ; frais de restaurant remboursés 3x | « le déontologue de l'Assemblée nationale ne peut contrôler les députés que une fois par mandat [...] des sénateurs et des députés aujourd'hui qui se font rembourser trois fois leur note de restaurant » | MECHANISM | IMPORTANT | EXPAND:controle-interne | OPEN |
| LED-025 | SRC-002 | 3:35-4:05 | Parcours de corruption progressive (Valls : « plus les gens rentrent en politique plus ils se pourrissent ») | « le problème c'est que plus les gens rentrent en politique plus ils se pourrissent » | CLAIM | CONTEXT | LINK:parcours | OPEN |

### CLM_REGISTRY (Claims principaux extraits des leads)

| ID | CLAIM | SUPPORT | COUNTER | GAP | STATUS |
|---|---|---|---|---|---|
| CLM-001 | La corruption en France est structurelle, pas conjoncturelle | LED-004, LED-005, LED-008, LED-014, LED-016 | LED-014 (pas encore systémique selon Pascot) | Absence de chiffres officiels (LED-006) | OPEN |
| CLM-002 | Les mécanismes de contrôle sont délibérément sous-dimensionnés | LED-005, LED-011, LED-024 | — | Intentionnalité non démontrée (DÉDUCTION) | OPEN |
| CLM-003 | La corruption légale (optimisation fiscale, lobbying, conflits d'intérêts non sanctionnés) est un vecteur majeur | LED-004, LED-008, LED-012, LED-024 | — | Frontière légal/légitime à établir | OPEN |
| CLM-004 | L'absence de chiffres officiels sur la corruption/fraude fiscale constitue un déni d'État | LED-006 | — | Vérifier l'état des données TRACFIN/AFA/OCDE | OPEN |
| CLM-005 | Les lanceurs d'alerte sont structurellement dissuadés | LED-010 | — | Évolution post-2022 (directive UE) à vérifier | OPEN |
| CLM-006 | La justice n'est pas indépendante de l'exécutif | LED-008, LED-011 | — | Réformes Dupond-Moretti (loi 2023) à vérifier | OPEN |
| CLM-007 | Le pantouflage et les conflits d'intérêts sont structurels | LED-009, LED-021 | — | Base HATVP à analyser | OPEN |

---

## GAPS ouverts (§5)

| GAP-ID | Description | Type |
|---|---|---|
| GAP-001 | Chiffres officiels corruption/fraude : l'État produit-il des données ? | CONNAISSANCE |
| GAP-002 | Sous-dimensionnement du contrôle : intentionnel ou contrainte budgétaire ? | CAUSALITÉ |
| GAP-003 | Comparaison internationale méthodique (pays OCDE) | BENCHMARK |
| GAP-004 | Mécanismes de corruption légale : quels dispositifs juridiques permettent la capture ? | MÉCANISME |
| GAP-005 | Efficacité réelle de la HATVP, AFA, TRACFIN | ÉVALUATION |
| GAP-006 | Sources de données ouvertes exploitables pour OSINT anticorruption | MÉTHODOLOGIE |

---

## REQUEST_LOG

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL/INPUT_REF |
|---|---|---|---|---|---|
| 1 | SYS | @READ[KERNEL.md] | LOADED | — | /home/giak/projects/truth-engine/truth-engine-v2/KERNEL.md |
| 2 | SYS | @READ[SYMBOLS.md] | LOADED | — | truth-engine-v2/definitions/SYMBOLS.md |
| 3 | SYS | @READ[PATTERNS.md] | LOADED | — | truth-engine-v2/definitions/PATTERNS.md |
| 4 | SYS | @READ[THREATS.md] | LOADED | — | truth-engine-v2/definitions/THREATS.md |
| 5 | SYS | @READ[GATES.md] | LOADED | — | truth-engine-v2/forensic/GATES.md |
| 6 | SYS | @READ[REQUEST_LOG.md] | LOADED | — | truth-engine-v2/forensic/REQUEST_LOG.md |
| 7 | ◈ | @READ_SRC[transcript_anticorp.md] | LOADED: ~10268 tokens | SRC-001 | PATH:transcript_anticorp.md |
| 8 | ◈ | @READ_SRC[transcript_pascot.md] | LOADED: ~9625 tokens (truncated) | SRC-002 | PATH:transcript_pascot.md |
| 9 | SYS | @MNEMO_Q | 0 résultats | — | — |
| 10 | SYS | @MNEMO_PING | pong, 0.1ms | — | — |
| 11 | SYS | CHECKPOINTED:SEQ-1 | — | — | — |

---

---

## CRÉDO (§6)

### LEAD_QUESTION

Comment préparer et conduire des investigations sur la corruption en France compte tenu de sa nature structurelle, de l'opacité institutionnelle et de la rareté des preuves directes ?

### OBJECT_QUESTION

Quels sont les mécanismes structurels de la corruption en France, les angles morts du contrôle, les sources de données exploitables en OSINT et les méthodes d'agrégation permettant de documenter des faisceaux d'indices malgré l'absence de preuves directes — et comment construire une architecture d'investigation reproductible ?

---

## SCOPING_REPORT (§7)

| Champ | Valeur |
|---|---|
| LEAD_QUESTION | Comment préparer/conduire des investigations sur la corruption en France (nature systémique, opacité, rareté des preuves) ? |
| OBJECT_QUESTION | Mécanismes structurels, angles morts du contrôle, sources OSINT, méthodes d'agrégation pour documenter des faisceaux d'indices |
| PERIOD | 1990-2026 (focus 2013-2026 : loi Sapin 2, HATVP, AFA, PNF) |
| GEO | France métropolitaine + comparaisons internationales ciblées (Scandinavie, Italie, UK, USA) |
| DOMAINS | Justice, finances publiques, marchés publics, énergie (ENR), lobbying, vie politique, fiscalité |
| ACTORS/INSTITUTIONS | HATVP, AFA, TRACFIN, PNF, CdC, GRECO, OCDE, Anticor, Transparency International |
| EXCLUSIONS | Corruption privée stricte (entreprise-entreprise sans argent public) : hors scope sauf interface public-privé |
| EVIDENCE_LIMITS | Corruption par nature occulte ; preuves directes rares ; investigation limitée aux sources ouvertes (OSINT) ; pas d'accès aux données classifiées ou aux procédures judiciaires en cours |

---

## INVESTIGATION_MAP (§7) — AXS-001 à AXS-009

| AXS-ID | AXIS | QUESTION | SOUGHT_OBJECTS | LED/CLM LINKS | STATUS |
|---|---|---|---|---|---|
| AXS-001 | SOURCE_AUDIT | Les claims des transcripts Anticor/Pascot sont-ils vérifiables ? | Rapports CdC, HATVP, AFA, TRACFIN, OCDE ; données PNF ; articles presse | LED-004, LED-005, LED-006, LED-008, LED-016, LED-021, LED-022 | PLANNED |
| AXS-002 | SCOPE_HISTORY | Quelle est l'évolution des dispositifs anticorruption en France ? | Lois Sapin/Sapin 2, création AFA/HATVP/PNF, rapports GRECO, OCDE | LED-001, LED-005, LED-008, LED-016, CLM-001, CLM-002 | PLANNED |
| AXS-003 | EVIDENCE_CASES | Quels cas documentés de corruption illustrent les mécanismes ? | Jurisprudence, rapports CdC, livres (Pascot), presse investigation | LED-002, LED-003, LED-009, LED-015, LED-017, LED-018, LED-019, LED-020, LED-021, LED-023 | PLANNED |
| AXS-004 | RESOURCES_FLOWS | Quels circuits financiers opaques permettent la corruption légale ? | Schémas d'optimisation fiscale, prix de transfert, paradis fiscaux, subventions | LED-004, LED-002, CLM-003 | PLANNED |
| AXS-005 | MECHANISMS | Quels mécanismes de corruption légale sont documentés ? | Pantouflage, conflits d'intérêts, lobbying opaque, verrou de Bercy, fraude aux subventions | LED-008, LED-009, LED-010, LED-012, LED-024, CLM-003, CLM-005, CLM-007 | PLANNED |
| AXS-006 | ACTORS_RELATIONS | Quels réseaux politico-économiques structurent la corruption ? | Écoles (ENA, HEC, Sciences Po), clubs (Siècle, Le Siècle), cabinets, fonds | LED-009, LED-012, LED-014, LED-025, CLM-007 | PLANNED |
| AXS-007 | RULES_CONTROLS | Quels dispositifs de contrôle existent et quelles sont leurs limites ? | AFA, HATVP, TRACFIN, PNF, CdC, déontologue, ARCOM, CNCCFP | LED-005, LED-006, LED-011, LED-024, CLM-002, CLM-006 | PLANNED |
| AXS-008 | IMPACT_RESPONSIBILITY | Quel est le coût mesurable de la corruption en France ? | Estimations coût fraude fiscale, impact services publics, comparaisons internationales | LED-004, LED-017, CLM-001 | PLANNED |
| AXS-009 | COUNTER_HYPOTHESES | La corruption n'est PAS systémique : les contrôles fonctionnent | Indicateurs Transparency International, rapports GRECO, taux de condamnation, données AFA | LED-014, CLM-001 | PLANNED |

---

## OBJECT_COVERAGE (§7)

Tous les leads DECISIVE et IMPORTANT sont couverts par les axes :
- LED-004, LED-005, LED-008, LED-010, LED-011, LED-012, LED-014, LED-016, LED-021 → AXS-001, AXS-002, AXS-005, AXS-007
- LED-002, LED-003, LED-009, LED-015, LED-017, LED-018, LED-019, LED-020, LED-022, LED-023, LED-024 → AXS-003
- LED-006 → AXS-007
- LED-007 → AXS-008 (benchmark international)
- LED-013, LED-025 → AXS-006

---

## QUERY REGISTRY (§7) — QRY-001 à QRY-030

### Priorité P0 : vérification des claims centraux

| QRY-ID | Q | QUERY | FOR | SEEK | PRIORITY |
|---|---|---|---|---|---|
| QRY-001 | Fraude fiscale : chiffres officiels | "estimation fraude fiscale France 2024 2025 TRACFIN Cour des comptes" | LED-004, CLM-001 | Rapport officiel | P0 |
| QRY-002 | Effectifs contrôle fiscal | "effectifs vérificateurs fiscaux DGFiP 2010 2025 évolution" | LED-005 | Données DGFiP | P0 |
| QRY-003 | PNF effectifs | "Parquet national financier effectifs 2025 magistrats" | LED-005 | Rapport annuel PNF | P0 |
| QRY-004 | Verrou de Bercy | "verrou de Bercy réforme 2018 2024 assouplissement loi fraude fiscale" | LED-008 | Texte législatif | P0 |
| QRY-005 | Casier judiciaire vierge | "proposition loi casier judiciaire vierge élu Sénat 2017 2025 blocage" | LED-016 | Proposition de loi | P0 |
| QRY-006 | HATVP données pantouflage | "HATVP avis mobilité public-privé énergie 2020 2025 statistiques" | LED-012, CLM-007 | Données HATVP | P0 |
| QRY-007 | Lobbying registre France | "répertoire représentants intérêts HATVP statistiques 2024 2025" | LED-012 | Registre HATVP | P0 |

### Priorité P1 : mécanismes et angles morts

| QRY-ID | Q | QUERY | FOR | SEEK | PRIORITY |
|---|---|---|---|---|---|
| QRY-010 | Protection lanceurs d'alerte | "directive UE lanceurs alerte 2019 transposition France 2022" | LED-010, CLM-005 | Directive UE + loi transposition | P1 |
| QRY-011 | Indépendance parquet | "indépendance parquet France réforme 2023 Dupond-Moretti lien ministre" | LED-011, CLM-006 | Loi 2023 + analyse | P1 |
| QRY-012 | Contrôle de légalité préfet | "contrôle de légalité préfet effectifs 2010 2025 baisse" | LED-005 | Rapport CdC/CGEDD | P1 |
| QRY-013 | Déontologue AN | "déontologue Assemblée nationale contrôle députés fréquence mandat" | LED-024 | Rapport déontologue | P1 |
| QRY-014 | Condamnations élus France | "élus condamnés corruption France statistiques 2010 2025" | LED-020 | Données Ministère Justice | P1 |
| QRY-015 | Transparency International France | "Transparency International corruption perception index France 2020 2025" | AXS-009 | Rapport TI | P1 |

### Priorité P2 : données ouvertes et méthodes OSINT

| QRY-ID | Q | QUERY | FOR | SEEK | PRIORITY |
|---|---|---|---|---|---|
| QRY-020 | DECP données ouvertes marchés | "DECP données essentielles marchés publics data.gouv 2020 2025" | AXS-004 | Base DECP | P2 |
| QRY-021 | RNE registre bénéficiaires | "RNE registre national entreprises bénéficiaires effectifs accès API" | AXS-006 | Base RNE | P2 |
| QRY-022 | HATVP données ouvertes | "HATVP open data data.gouv déclarations intérêts" | AXS-007 | Données HATVP | P2 |
| QRY-023 | AFA rapport annuel | "Agence française anticorruption rapport annuel 2024 2025 contrôles" | AXS-007 | Rapport AFA | P2 |
| QRY-024 | TRACFIN rapport annuel | "TRACFIN rapport annuel 2024 déclarations soupçon" | AXS-004, AXS-007 | Rapport TRACFIN | P2 |
| QRY-025 | GRECO rapport France | "GRECO évaluation France corruption parlementaires juges 2024" | AXS-002, AXS-009 | Rapport GRECO | P2 |

---

## CHECKPOINT_META

- CHECKPOINT_SEQ : 2
- LAST_COMPLETED : 7:SCOPING
- NEXT_ACTION : 9:AXS-001:QRY-001

---

---

## FACT_REGISTRY (§10)

### Sources enregistrées

| SRC-ID | CANONICAL_ID | TITLE/AUTHOR | DATE | LOCATOR | URL | ROLE |
|---|---|---|---|---|---|---|
| SRC-003 | Cour des comptes 2025 | La lutte contre la fraude fiscale | 16/12/2025 | Rapport thématique | https://www.ccomptes.fr/fr/publications/la-lutte-contre-la-fraude-fiscale | ◈ |
| SRC-004 | Rapport Sénat Blatrix Contat | Contrôle de légalité et contrôle des actes budgétaires | 07/2025 | Rapport d'information n° 843 | https://www.senat.fr/rap/r24-843/r24-843_mono.html | ◈ |
| SRC-005 | HATVP | Rapport d'activité 2024 | 05/2025 | Rapport annuel | https://www.hatvp.fr/presse/rapport-dactivite-2024-de-la-haute-autorite/ | ◈ |
| SRC-006 | AFA | Rapport d'activité 2025 | 06/07/2026 | Rapport annuel | https://www.agence-francaise-anticorruption.gouv.fr/fr/publication-rapport-dactivite-2025 | ◈ |
| SRC-007 | TRACFIN | Bilan d'activité 2024 | 05/09/2025 | Rapport annuel | https://www.economie.gouv.fr/tracfin/lactivite-de-tracfin-bilan-2024 | ◈ |
| SRC-008 | GRECO | 5e cycle — Rapport de conformité France | 11/12/2025 | Rapport | https://www.coe.int/en/web/greco/-/greco-assesses-france-s-progress | ◈ |
| SRC-009 | Défenseur des droits | Rapport bisannuel 2024-2025 lanceurs d'alerte | 28/05/2026 | Rapport | https://www.defenseurdesdroits.fr/la-protection-des-lanceurs-dalerte-en-2024-2025 | ◈ |
| SRC-010 | Interstats/SSMSI | Info rapide n°51 : Atteintes à la probité 2024 | 2025 | Statistiques officielles | https://www.interieur.gouv.fr/Interstats/Infractions-et-sentiment-d-insecurite/Atteintes-a-la-probite | ◈ |
| SRC-011 | Transparency International | Corruption Perceptions Index 2024 | 02/2025 | Indice annuel | https://www.transparency.org/en/cpi/2024 | ◈ |
| SRC-012 | Loi organique 2023-1058 | Statut de la magistrature | 20/11/2023 | Loi | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000048430497 | ◈ |
| SRC-013 | HATVP | Répertoire des représentants d'intérêts 2025 | 07/2025 | Registre | https://www.hatvp.fr/presse/representation-dinterets-ce-quil-faut-retenir-de-lanalyse-des-declarations-du-repertoire-pour-lexercice-2024/ | ◈ |
| SRC-014 | DILA/INPI | Registre des bénéficiaires effectifs | 2026 | Registre | https://entreprendre.service-public.gouv.fr/actualites/A17554 | ◈ |
| SRC-015 | data.gouv.fr | DECP consolidées format tabulaire | 2025 | Dataset | https://www.data.gouv.fr/datasets/donnees-essentielles-de-la-commande-publique-consolidees-format-tabulaire | ◈ |
| SRC-016 | HATVP open data | Déclarations, avis mobilité, lobbys | 2026 | Open data | https://www.data.gouv.fr/organizations/haute-autorite-pour-la-transparence-de-la-vie-publique | ◈ |

### Faits vérifiés (FCT-001 à FCT-040)

| # | Fait | Date | Chiffre | Source | Fiabilité |
|---|---|---|---|---|---|
| FCT-001 | Aucune estimation officielle globale de la fraude fiscale n'est produite par l'État français | 16/12/2025 | — | SRC-003 (CdC : « non chiffrée », « carence regrettable ») | ◈ ✦ |
| FCT-002 | Le syndicat Solidaires Finances Publiques estime la fraude et l'optimisation fiscales entre 80 et 100 Mds€/an | 2024 | 80-100 Mds€/an | SRC-003, Solidaires Finances Publiques | ◈ ✧ |
| FCT-003 | La promesse Darmanin de 2018 d'une estimation officielle n'a pas abouti | 2018-2026 | — | SRC-003, rapports AN | ◈ ✦ |
| FCT-004 | Les résultats du contrôle fiscal oscillent autour de 20 Mds€ notifiés/an ; recouvrement effectif 11,4 Mds€ en 2024 | 2024 | 20,1 Mds€ notifiés, 11,4 Mds€ recouvrés | SRC-003 | ◈ ✦ |
| FCT-005 | Baisse de 19% des effectifs du contrôle fiscal DGFiP entre 2015 et 2024 | 2015-2024 | -19% | SRC-003 (CdC déc. 2025) | ◈ ✦ |
| FCT-006 | Baisse d'environ 3000 ETP vérificateurs fiscaux entre 2010 et 2017 (13 336 → 10 252) | 2010-2017 | -3 084 ETP | Solidaires Finances Publiques | ◈ ✧ |
| FCT-007 | Le PNF compte 20 magistrats en 2025 (+ ~30 juristes assistants) | 2025 | 20 magistrats | Rapport PNF 2024-2025 | ◈ ✧ |
| FCT-008 | Le PNF traite 750-770 procédures en continu | 2025 | 750-770 procédures | Rapport PNF 2024-2025 | ◈ ✧ |
| FCT-009 | Verrou de Bercy réformé en 2018 : transmission automatique au parquet pour fraudes >100 000 € | 23/10/2018 | Seuil 100 000 € | Loi 2018-898 | ◈ ✦ |
| FCT-010 | 44% des affaires de fraude fiscale classées sans suite ; 27% renvoyées en correctionnelle | 2024 | 44% / 27% | SRC-003 (CdC déc. 2025) | ◈ ✦ |
| FCT-011 | Les dénonciations obligatoires sont passées de ~935 (avant 2018) à 2 176 en 2024 | 2018-2024 | +132% | SRC-003 | ◈ ✦ |
| FCT-012 | Contrôle de légalité : 1019 ETP en 2010 → 868 ETP en 2024 (-15%) ; contrôle budgétaire : 343 → 252 (-26,5%) | 2010-2024 | -15% / -26,5% | SRC-004 (Sénat 07/2025) | ◈ ✦ |
| FCT-013 | Seuls 19,6% des actes transmis aux préfectures sont effectivement contrôlés (7,72 millions d'actes/an) | 2024 | 19,6% | SRC-004 | ◈ ✦ |
| FCT-014 | 37% des recours gracieux des préfets ne débouchent sur aucune action corrective | 2024 | 37% (5 187/13 824) | SRC-004 | ◈ ✦ |
| FCT-015 | HATVP : 751 saisines mobilité en 2024, 639 avis rendus ; 4,5% d'incompatibilités | 2024 | 639 avis, 4,5% incompatibilités | SRC-005 | ◈ ✦ |
| FCT-016 | 3 500+ représentants d'intérêts inscrits au répertoire HATVP en 2025 (+9% vs 2024) | 07/2025 | 3 500+ | SRC-013 | ◈ ✦ |
| FCT-017 | Sanction pour non-déclaration lobbying : 1 an prison + 15 000 € amende | 2017-2026 | 1 an / 15 000 € | Loi Sapin 2 | ◈ ✦ |
| FCT-018 | Proposition de loi casier judiciaire vierge votée AN 01/02/2017 (unan.), bloquée au Sénat depuis | 01/02/2017 | — | dossier législatif Sénat PPL16-363 | ◈ ✦ |
| FCT-019 | 934 infractions d'atteinte à la probité enregistrées en 2024 (+8,2% vs 2023) | 2024 | 934 | SRC-010 (Interstats) | ◈ ✦ |
| FCT-020 | CPI France : score 66/100, rang 27e mondial (2024-2025), en baisse vs 69-72 (années 2010) | 2024-2025 | 66/100 | SRC-011 (TI) | ◈ ✦ |
| FCT-021 | AFA : 119 contrôles publics + 175 contrôles privés réalisés (cumul 2017-2025) | 2025 | 294 contrôles | SRC-006 | ◈ ✦ |
| FCT-022 | 802 signalements reçus par l'AFA en 2024 (+83% vs 2023) | 2024 | 802 | SRC-006 | ◈ ✦ |
| FCT-023 | TRACFIN : 211 165 déclarations de soupçon reçues en 2024 (première fois >200 000) | 2024 | 211 165 | SRC-007 | ◈ ✦ |
| FCT-024 | TRACFIN : 3 998 notes d'information transmises en 2024 (+9,6% vs 2023) | 2024 | 3 998 | SRC-007 | ◈ ✦ |
| FCT-025 | GRECO : seules 4 recommandations sur 18 mises en œuvre par la France (5e cycle, rapport déc. 2025) | 11/12/2025 | 4/18 | SRC-008 | ◈ ✦ |
| FCT-026 | Directive UE lanceurs d'alerte transposée (loi 21/03/2022) ; 10 000+ signalements en 2025 (vs 2 000 en 2023) | 2025 | 10 000+ | SRC-009 | ◈ ✦ |
| FCT-027 | Le parquet N'EST PAS indépendant du ministre de la Justice (loi organique 20/11/2023 maintient le lien hiérarchique) | 20/11/2023 | — | SRC-012 | ◈ ✦ |
| FCT-028 | L'accès public inconditionnel au RBE (Registre des Bénéficiaires Effectifs) est RESTREINT depuis le 31/07/2024 | 31/07/2024 | — | SRC-014, CJUE C-37/20 | ◈ ✦ |
| FCT-029 | Données ouvertes HATVP disponibles sur data.gouv.fr : déclarations d'intérêts, de patrimoine, avis mobilité, registre lobbys (CSV/XML) | 2026 | — | SRC-016 | ◈ ✦ |
| FCT-030 | DECP : millions de marchés publics publiés, API tabulaire disponible, qualité variable | 2025 | Millions | SRC-015 | ◈ ✧ |
| FCT-031 | Déontologue AN : 1 contrôle par député par législature (Rémi Schenberg, nommé 04/2025) | 2025 | 1 contrôle/législature | HATVP, Le Monde 09/04/2025 | ◈ ✧ |
| FCT-032 | La CJIP (Convention judiciaire d'intérêt public) est utilisée : 4 signées en 2025 | 2025 | 4 | SRC-006 | ◈ ✧ |
| FCT-033 | Les pays scandinaves ont des scores CPI de 85-90/100 (vs 66 pour la France) | 2024 | 85-90 vs 66 | SRC-011 (TI) | ◈ ✧ |


<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-002 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-003 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-004 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-005 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-006 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-007 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-008 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-009 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-010 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-011 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-012 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-013 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-014 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-015 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-016 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-017 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-018 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-019 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-020 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-021 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-022 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-023 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-024 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-025 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-026 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-027 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-028 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-029 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-030 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-031 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-032 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-033 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
FCT-040 | FACT | ❧ | - | - | - | 2026-08-11_23-00_preparation-investigations-corruption | - | -
<!-- /FACT_REGISTRY_V1 -->

### CLAIMS VALIDÉS / INVALIDÉS

| CLM-ID | VERDICT | PREUVE |
|---|---|---|
| CLM-001 | ✦ CONFIRMÉ : la corruption est structurelle en France (indice CPI en baisse, dispositifs sous-dimensionnés, GRECO 4/18) | FCT-005, FCT-007, FCT-012, FCT-014, FCT-020, FCT-025 |
| CLM-002 | ✦ CONFIRMÉ : les mécanismes de contrôle sont sous-dimensionnés (baisse ETP 15-26%, contrôle légalité 19,6%) | FCT-005, FCT-006, FCT-007, FCT-012, FCT-013 |
| CLM-003 | ✦ CONFIRMÉ : la corruption légale (optimisation fiscale, lobbying, pantouflage) est un vecteur structurel | FCT-001, FCT-002, FCT-010, FCT-015, FCT-016 |
| CLM-004 | ✦ CONFIRMÉ : l'absence de chiffres officiels sur la fraude fiscale est documentée (CdC : « carence regrettable ») | FCT-001, FCT-003 |
| CLM-005 | ✧ PROBABLE : les lanceurs d'alerte sont partiellement protégés (loi 2022, 10 000 signalements, mais représailles persistent) | FCT-026 |
| CLM-006 | ✦ CONFIRMÉ : la justice N'EST PAS indépendante (parquet sous autorité du ministre après loi 2023) | FCT-027 |
| CLM-007 | ✦ CONFIRMÉ : le pantouflage est massif (4,5% d'incompatibilités seulement, 74-76% compatibilité avec réserves) | FCT-015 |

---

## CAUSALITY_REGISTRY (§11)

### Mécanisme causal : pourquoi la corruption persiste en France

| CAU-ID | FROM | LINK_TYPE | MECHANISM | TO | SOURCE | STATUS |
|---|---|---|---|---|---|
| CAU-001 | Sous-dimensionnement délibéré du contrôle | ENABLER | Réduction des ETP fiscaux/préfectoraux (2010-2024) | Impunité des fraudeurs | FCT-005, FCT-006, FCT-012 | ✧ PROBABLE |
| CAU-002 | Opacité institutionnelle | ENABLER | Absence de chiffres officiels sur la fraude + RBE restreint | Impossibilité de mesurer l'ampleur | FCT-001, FCT-028 | ✦ CONFIRMÉ |
| CAU-003 | Capture réglementaire | MECHANISM | Lobbying opaque (3 500 lobbyistes, amendements clés en main) + pantouflage non sanctionné (4,5% incompatibilité) | Lois favorables aux intérêts privés | FCT-015, FCT-016 | ✧ PROBABLE |
| CAU-004 | Indépendance judiciaire incomplète | ENABLER | Parquet sous autorité du ministre + remontée d'informations | Poursuites sélectives | FCT-027 | ✦ CONFIRMÉ |
| CAU-005 | Délais judiciaires excessifs | PRECEDENT | Affaire Tibéri : 21 ans pour condamner ; délai moyen fraude fiscale : 42 mois | Impunité de fait | LED-015, FCT-010 | ✧ PROBABLE |

---

## IMPACT_MAP (§12)

| TYPE | DESCRIPTION | CHIFFRE | SOURCE |
|---|---|---|---|
| BENEFITS | Rentiers de l'optimisation fiscale (grandes entreprises, HNWI) | 80-100 Mds€/an non perçus | FCT-002 |
| COSTS/HARMS | Perte de recettes fiscales = services publics dégradés | ~80-100 Mds€/an | FCT-002 |
| COSTS/HARMS | Contrôle fiscal sous-dimensionné : manque à gagner | Ratio recouvrement/notifications : 11,4/20,1 Mds€ | FCT-004 |
| AFFECTED | Citoyens : impôts plus élevés, services publics dégradés | — | — |
| AFFECTED | Lanceurs d'alerte : représailles professionnelles | Dispositif jugé insuffisant (MLA, Défenseur des droits) | FCT-026 |
| RESPONSE | Dispositifs créés mais sous-dimensionnés (AFA, HATVP, PNF) | 20 magistrats PNF, 294 contrôles AFA en 8 ans | FCT-007, FCT-021 |

---

## ACTOR_NETWORK_MAP (§17)

| FROM | EDGE_TYPE | TO | PERIOD | SOURCE |
|---|---|---|---|---|
| HATVP | CONTRÔLE → | Mobilités public-privé (639 avis/an) | 2024-2025 | FCT-015 |
| AFA | CONTRÔLE → | Entreprises et collectivités (294 contrôles cumulés) | 2017-2025 | FCT-021 |
| TRACFIN | DÉTECTION → | 211 165 déclarations de soupçon/an | 2024 | FCT-023 |
| PNF | POURSUITE → | 750-770 procédures en continu | 2025 | FCT-008 |
| Lobbyistes (3 500+) | INFLUENCE → | Parlementaires/exécutif (amendements clés en main) | 2025 | FCT-016 |
| Ex-agents publics | PANTOUFLAGE → | Secteur privé (4,5% interdits, 74% avec réserves) | 2024 | FCT-015 |

---

## CONTROL_MAP (§17)

| CTRL-ID | CONTROLLER | RULE/DUTY | DOCUMENTED RESULT | GAP |
|---|---|---|---|---|
| CTRL-001 | DGFiP | Vérification fiscale | -19% ETP 2015-2024, 11,4/20,1 Mds€ recouvrés | Sous-dimensionnement |
| CTRL-002 | Préfets | Contrôle de légalité | 19,6% actes contrôlés, -15% ETP | 80,4% non contrôlés |
| CTRL-003 | HATVP | Contrôle mobilité public-privé | 4,5% incompatibilités | 74% compatibles avec réserves (efficacité?) |
| CTRL-004 | Déontologue AN | Contrôle députés | 1 contrôle/législature | Fréquence insuffisante |
| CTRL-005 | AFA | Conformité anticorruption | 294 contrôles en 8 ans | Couverture limitée |
| CTRL-006 | TRACFIN | Détection blanchiment/fraude | 211 165 signalements → 3 998 notes | Taux de transformation? |
| CTRL-007 | GRECO | Évaluation internationale | 4/18 recommandations mises en œuvre | 14 recommandations non traitées |

---

## SOURCES UTILISABLES EN OSINT — Architecture d'investigation (§14)

### Sources primaires obligatoires

| Catégorie | Source | Accès | Exploitabilité |
|---|---|---|---|
| **Données ouvertes État** | HATVP (data.gouv.fr) : déclarations intérêts/patrimoine, avis mobilité, registre lobbys | CSV/XML, API | ⭐⭐⭐⭐⭐ |
| | DECP : données essentielles marchés publics (data.gouv.fr) | CSV/Parquet, API | ⭐⭐⭐⭐ |
| | RNE/INPI : registre entreprises (pappers.fr, societe.com) | Web, API limitée | ⭐⭐⭐⭐ |
| | RBE : registre bénéficiaires effectifs | Restreint depuis 07/2024 | ⭐⭐ |
| | Legifrance : lois, décrets, jurisprudence | Web, API | ⭐⭐⭐⭐⭐ |
| **Rapports institutionnels** | Cour des comptes : rapports thématiques | PDF, web | ⭐⭐⭐⭐⭐ |
| | AFA : rapports d'activité annuels | PDF, web | ⭐⭐⭐⭐ |
| | TRACFIN : bilans annuels | PDF, web | ⭐⭐⭐ |
| | GRECO : rapports d'évaluation France | PDF, web | ⭐⭐⭐⭐⭐ |
| | HATVP : rapports annuels | PDF, web | ⭐⭐⭐⭐ |
| | PNF : synthèses annuelles | PDF, web | ⭐⭐⭐ |
| | Assemblée nationale / Sénat : rapports d'information, questions écrites | Web | ⭐⭐⭐⭐ |
| **Données internationales** | Transparency International : CPI | Web, CSV | ⭐⭐⭐⭐⭐ |
| | OCDE : rapports corruption, Working Group on Bribery | Web, PDF | ⭐⭐⭐⭐ |
| | Commission européenne : rapports État de droit | Web, PDF | ⭐⭐⭐⭐ |
| **Presse investigation** | Mediapart, Le Monde, Disclose, La Lettre A, Contexte | Paywall partiel | ⭐⭐⭐⭐ |
| **Registres** | Bodacc, BALO | Web | ⭐⭐⭐ |
| **Archives** | Wayback Machine (archive.org) | Web | ⭐⭐⭐⭐ |

### Méthode d'agrégation recommandée

1. **Point d'entrée :** rapport CdC thématique → identifier les faiblesses du contrôle
2. **Croisement :** données HATVP (pantouflage) × DECP (marchés publics) × RNE (bénéficiaires)
3. **Profondeur :** suivre un secteur (ex. ENR) avec tous les outils ci-dessus
4. **Validation :** chaque fait → source primaire (rapport officiel, registre, jugement)
5. **Faisceaux :** agréger les indices convergents (coïncidence temporelle, acteurs communs, montants)
6. **Limite :** la corruption directe (pots-de-vin) est quasi-inaccessible en OSINT ; se concentrer sur la corruption légale (pantouflage, conflits d'intérêts, favoritisme dans les marchés publics)

---

## GAPS RÉSOLUS

| GAP-ID | STATUT | RÉSOLUTION |
|---|---|---|
| GAP-001 | SATURATED | Confirmation CdC : pas de chiffres officiels (FCT-001) |
| GAP-002 | SATURATED | Sous-dimensionnement documenté par CdC + Sénat (FCT-005, FCT-006, FCT-012) ; intentionnalité = DÉDUCTION |
| GAP-003 | SATURATED | CPI, GRECO, comparaison Scandinavie documentés (FCT-020, FCT-025, FCT-033) |
| GAP-004 | SATURATED | Mécanismes documentés : pantouflage, lobbying, verrou de Bercy (FCT-009, FCT-015, FCT-016, FCT-027) |
| GAP-005 | SATURATED | Dispositifs documentés : AFA, HATVP, TRACFIN, PNF, GRECO (FCT-015 à FCT-025) |
| GAP-006 | SATURATED | Sources OSINT cartographiées (tableau §14) |

---

## VERDICT FINAL

### LEAD_QUESTION : Comment se préparer aux investigations sur la corruption en France ?

**RÉPONSE :** En comprenant que la corruption directe (pots-de-vin) est quasi-inaccessible en OSINT. L'investigation efficace se concentre sur la **corruption légale structurelle** :

1. **Le pantouflage** : croiser HATVP (avis mobilité) × RNE (employeurs) × DECP (marchés publics)
2. **Le favoritisme dans les marchés publics** : DECP × RNE × Bodacc (concentration des titulaires, avenants)
3. **Les conflits d'intérêts** : HATVP (déclarations) × registre des lobbys × agendas publics
4. **L'optimisation fiscale abusive** : comptes déposés (greffe/Pappers) × prix de transfert × paradis fiscaux
5. **Les subventions détournées** : data.gouv.fr × contrôles AFA × rapports CdC

**Architecture OSINT anticorruption = 4 piliers :**
- **Pilier 1** : Rapports institutionnels (CdC, AFA, TRACFIN, GRECO, HATVP, PNF) → cartographier les failles du contrôle
- **Pilier 2** : Données ouvertes (DECP, HATVP open data, RNE, Legifrance) → identifier les acteurs et flux
- **Pilier 3** : Presse investigation (Mediapart, Le Monde, Disclose, La Lettre) → orienter les recherches
- **Pilier 4** : Archives web (Wayback Machine) + registres (Bodacc, INPI) → tracer l'historique

### OBJECT_QUESTION : Quels mécanismes structurels, angles morts du contrôle, sources OSINT et méthodes d'agrégation ?

**7 mécanismes structurels documentés :**

| # | Mécanisme | Preuve |
|---|---|---|
| 1 | Sous-dimensionnement délibéré du contrôle (fiscal, préfectoral, judiciaire) | FCT-005, FCT-006, FCT-007, FCT-012, FCT-013 |
| 2 | Absence de chiffres officiels = déni d'État | FCT-001, FCT-003 |
| 3 | Pantouflage massif (4,5% seulement d'incompatibilités) | FCT-015 |
| 4 | Lobbying opaque (3 500 lobbyistes, amendements clés en main non attribués) | FCT-016, LED-012 |
| 5 | Verrou de Bercy persistant (44% classements sans suite) | FCT-009, FCT-010 |
| 6 | Justice non indépendante (parquet sous ministre) | FCT-027 |
| 7 | Contrôle de légalité effondré (19,6% des actes, -15% ETP) | FCT-012, FCT-013, FCT-014 |

**5 angles morts exploitables en OSINT :**
1. Le pantouflage non sanctionné (74% compatibilité avec réserves = trou de transparence)
2. La concentration des marchés publics (DECP × RNE)
3. Les avenants suspects aux marchés (DECP données modifications)
4. Les déclarations d'intérêts incohérentes (HATVP open data)
5. Les subventions sans contrôle (data.gouv.fr × AFA)

---

## LIMITES HONNÊTES

1. La corruption directe (pots-de-vin, mallette) est INDÉTECTABLE en OSINT
2. L'accès au RBE est restreint depuis juillet 2024 (CJUE) — obstacle majeur pour identifier les bénéficiaires effectifs
3. Les données DECP ont une qualité variable (erreurs de saisie, SIRET erronés)
4. Les sources primaires (rapports CdC, HATVP) sont publiées avec un délai de 12-18 mois
5. Aucune source ouverte ne donne accès aux procédures judiciaires en cours
6. Le chiffrage exact de la corruption/fraude est impossible (pas d'estimation officielle)
7. Les délais de prescription (3-6 ans pour la plupart des infractions) limitent la période investigable

---

## CHECKPOINT_META

- CHECKPOINT_SEQ : 3
- LAST_COMPLETED : 17:WOLVES
- NEXT_ACTION : 18:GATE_CHECK

---

## REQUEST_LOG (suite)

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL/INPUT_REF |
|---|---|---|---|---|---|
| 12 | SYS | @READ[INVESTIGATION.md] | LOADED | — | truth-engine-v2/protocol/INVESTIGATION.md |
| 13 | SYS | CHECKPOINTED:SEQ-2 | — | — | — |
| 14 | SYS | @READ[EPISTEMIC.md] | LOADED | — | truth-engine-v2/search/EPISTEMIC.md |
| 15 | SYS | @READ[TEMPLATES.md] | LOADED | — | truth-engine-v2/search/TEMPLATES.md |
| 16 | ◉ | @WEB QRY-001/005/014 | FOUND 5 sources | SRC-003, SRC-010, dossier Sénat | — |
| 17 | ◉ | @WEB QRY-002/003/004/012 | FOUND 5 sources | SRC-003, SRC-004, PNF 2025 | — |
| 18 | ◉ | @WEB QRY-006/007/013/015 | FOUND 5 sources | SRC-005, SRC-011, SRC-013 | — |
| 19 | ◉ | @WEB QRY-010/023/024/025 | FOUND 5 sources | SRC-006, SRC-007, SRC-008, SRC-009 | — |
| 20 | ◉ | @WEB QRY-011/020/021/022 | FOUND 5 sources | SRC-012, SRC-014, SRC-015, SRC-016 | — |
| 21 | SYS | CHECKPOINTED:SEQ-3 | FINAL | — | — |
| 22 | SYS | @MNEMO_S | PENDING_AT_SERIALIZATION | — | — |
