# KERNEL INVESTIGATION: Bulle IA et interdépendance des acteurs

| Champ | Valeur |
|-------|--------|
| ID | INV-2026-08-25-1500-BULLE-IA-INTERDEPENDANCE |
| Type | KERNEL APEX (16/18) |
| RUN_ID | 20260825-1500-bulle-ia-interdependance-acteurs |
| Loup parent | Aucun (nouvelle investigation, prolonge la fresque IA-salariat) |
| Date | 2026-08-25 |
| INPUT_KIND | TOPIC |
| MISSION_MODE | INVESTIGATION |
| Sources consultées | ~35 |
| Faits enregistrés | 36 |
| Faits ancrés (fetchés) | 14 |
| Gate | PASS (déterministe, worktree te-bulle-ia-20260825, 19a + 19b) |
| STATE_ID | sha256:f05da6ceb65c81170ca5e9682caa5dd80b1678cfb42b8354bc882da8513952ca |
| Mémoires écrites | 19 faits (2 CONFIRME, 17 VERIFIE) |

---

## 1. RÉSUMÉ EXÉCUTIF

**OBJECT_QUESTION :** y a-t-il une bulle IA, et qui possède qui dans l'écosystème OpenAI, Microsoft, Oracle, Anthropic, xAI ?

**Réponse bornée :** la bulle est partiellement mesurable, pas une certitude. Le ratio capex IA / revenus IA directs est de l'ordre de **10 pour 1 en 2026** (7 à 8 pour 1 sur les réalisés 2025) : cinq géants (Amazon, Alphabet, Meta, Microsoft, Oracle) dépensent 660 à 690 Md$ d'infrastructure, dont 450 à 500 Md$ directement IA, pour environ 51 Md$ de revenus IA directs [FCT-001, FCT-034]. C'est le troisième plus grand cycle d'investissement d'infrastructure de l'histoire des États-Unis rapporté au PIB (~1,2 % du PIB en 2025), après le rail (~6 %) et la télécom 1996-2001 [FCT-001]. Le marché a déjà corrigé : Nvidia est passée sous 5 000 Md$ fin juillet 2026, le Nasdaq-100 en territoire de correction [FCT-019], et les quatre plus gros investisseurs ont perdu ~900 Md$ de valeur boursière en février 2026 sur l'annonce de leurs capex [FCT-021].

**Sur l'interdépendance, le lead de l'utilisateur est partiellement inversé.** OpenAI ne possède pas Microsoft : c'est l'inverse, Microsoft détient ~27 % d'OpenAI après la recapitalisation 2025 [FCT-011], et surtout **~70 % du revenu IA de Microsoft provient d'OpenAI** (24,1 Md$ sur l'exercice clos juin 2026), dont une large part est la facture de calcul qu'OpenAI se paie à elle-même via Azure [FCT-009, FCT-010]. Microsoft ne possède pas Oracle : les deux sont partenaires, et Oracle est co-investisseur de Stargate avec OpenAI et SoftBank [FCT-018]. En revanche le maillage est réel et dense : Microsoft possède des parts d'OpenAI **et** d'Anthropic (5 Md$, gain comptable 3,2 Md$ en juillet 2026) [FCT-015] ; Amazon possède des parts d'Anthropic (gains comptables 16,8 Md$ au T1 puis 53,4 Md$ au T2 2026) **et** a investi 50 Md$ dans OpenAI en février 2026 [FCT-005, FCT-014] ; Nvidia investit dans OpenAI (30 Md$) et xAI [FCT-005, FCT-016]. Le réseau est une toile d'actionnaires croisés, pas une chaîne de propriété linéaire.

**Le goulot matériel est réel et documenté :** la RAM est vendue d'avance pour 2026 (SK Hynix, Micron), les prix DRAM montent de 50 à 55 % au T1 2026, un bit de HBM coûte trois bits de mémoire classique en capacité de production [FCT-002, FCT-003]. La Chine avance vite : DeepSeek V4 (avril 2026) est le premier modèle de frontière entraîné nativement sur les puces Huawei Ascend, avec des prix 8 à 10 fois inférieurs à ceux d'OpenAI et d'Anthropic [FCT-022]. **Mistral a effectivement pivoté** : son modèle phare Large 3 est construit sur l'architecture DeepSeek V3, et depuis le 11 août 2026 sa plateforme sert le modèle chinois GLM 5.2 tel quel [FCT-028, FCT-029].

**Verdict du lead (source) distinct du verdict d'objet :** la formulation « OpenAI possède Microsoft, qui possède Oracle » est **réfutée** dans ses directions (inversion), mais le constat sous-jacent de maillage serré est **confirmé** avec une topologie différente et plus intéressante : des actionnariats croisés, une dépendance circulaire Microsoft-OpenAI, et des gains comptables géants qui faussent les résultats publiés des Big Tech.

---

## 2. MANIPULATION_REPORT

| Symbole | Score /10 | Observation |
|---------|-----------|-------------|
| Ξ Omission | 6 | Seul Microsoft publie un chiffre de revenus IA distinct (Azure AI ~37 Md$/an) ; Amazon, Alphabet, Meta noient l'IA dans le cloud. La circularité OpenAI (la facture de calcul d'OpenAI est comptée comme revenu Microsoft) n'est visible que depuis un filing d'août 2026 |
| € Money | 8 | Flux massifs : 660-690 Md$ capex 2026, 110 Md$ levés par OpenAI, 30 Md$ Anthropic, 20 Md$ xAI, 5 000 Md$ Nvidia. Participations croisées généralisées |
| Λ Framing | 5 | Le récit « bulle ou pas bulle » binaire ; le récit « souveraineté » (Mistral) maintenu alors que l'activité devient de l'hébergement |
| Ω Inversion | 3 | L'utilisateur inverse la direction des participations (OpenAI → Microsoft). Récit officiel OpenAI (« AGI pour tous ») contre réalité financière de pertes massives |
| Ψ Sideration | 5 | Rythme des records (Nvidia 5 000 Md$) puis corrections (Nasdaq-100, -900 Md$) ; discours de panique et d'euphorie alternés |
| ↕ Pouvoir vertical | 6 | Dépendance Microsoft-OpenAI (70 % du revenu IA), dépendance de toute la chaîne à 3 fabricants de mémoire, contrôle US des exportations HBM |
| Φ Spectacle | 4 | Annonces Stargate (500 Md$) en grande pompe à la Maison-Blanche ; records de capitalisation mis en scène |
| Σ Sémio | 4 | « Souveraineté » comme étiquette : cloud souverain (vu ailleurs), Mistral qui héberge des modèles chinois sous la marque « champion européen » |
| Κ Cynisme | 4 | Mistral maintient le récit de laboratoire alors que ses recrutements sont ceux d'une ESN ; Microsoft présente le calcul d'OpenAI comme croissance propre |
| ρ Résistance | 2 | Peu de contre-pouvoir documenté : analystes, vendeurs à découvert (Burry), chercheurs |
| κ Influence subtile | 2 | Non mesuré |
| ⫸ Convergence | 5 | Les indices convergent : capex croissants, revenus IA non divulgués, circulaire OpenAI, gains comptables géants |
| ⚔ Guerre cognitive | 2 | Accusations US de « distillation industrielle » chinoise (Kratsios) ; non vérifié |
| 🌐 Réseau | 8 | Microsoft↔OpenAI↔Amazon↔Anthropic↔Nvidia↔xAI↔Oracle↔SoftBank : graphe dense d'actionnaires croisés |
| ⏰ Temporal | 5 | Rounds synchronisés (fév. 2026 : OpenAI et Anthropic lèvent en même temps), annonces coordonnées Stargate |

**Chargement des clusters (SYMBOLS §4) :** €=8 → MONEY, NETWORK, POWER ; Ξ=6 → ICEBERG ; 🌐=8 → NETWORK ; ⏰=5 → TEMPORAL. Clusters chargés : MONEY, NETWORK, POWER, ICEBERG, TEMPORAL.

**Hypothèses d'entrée :** le lead utilisateur est une intuition de maillage, pas un document. L'analyse porte sur la période 2024-08 → 2026-08-25, géographie États-Unis, Chine, France/UE.

---

## 3. CLUSTERS

**MONEY (€=8) :** flux documentés : OpenAI 110 Md$ levés (SoftBank 30, Nvidia 30, Amazon 50), Anthropic 30 Md$ (Série G) puis 65 Md$ (Série H), xAI 20 Md$, capex Big Five 660-690 Md$. Diagnostic : l'argent circule en circuit fermé (les investisseurs des labs sont leurs clients de cloud et leurs fournisseurs de puces). MONEY_FACTOR : part de revenus IA non disclosed = 4/5 des géants (seul Microsoft disclose).

**NETWORK (🌐=8) :** densité mesurable sur un graphe explicite : 8 nœuds (OpenAI, Microsoft, Amazon, Alphabet, Nvidia, Anthropic, xAI/SpaceX, Oracle/SoftBank). Types d'arêtes : propriété (Microsoft-OpenAI ~27 %, Amazon-Anthropic, Microsoft-Anthropic 5 Md$, Nvidia-OpenAI 30 Md$), client-fournisseur (OpenAI-Azure, Anthropic-AWS/Google), co-investissement (Stargate : OpenAI-Oracle-SoftBank). Pas de coordination prouvée, mais des intérêts croisés systématiques.

**POWER (↕=6) :** dépendances asymétriques : Microsoft à 70 % de son revenu IA sur un seul client ; la chaîne GPU-HBM sur trois fournisseurs ; l'Europe (Mistral) dépendante des architectures chinoises pour son « fleuron ».

**ICEBERG (Ξ=6) :** la partie visible (capex records) masque les revenus réels (51 Md$ vs 450-500 Md$) et la circularité (OpenAI paie Azure avec l'argent de Microsoft, qui comptabilise le flux comme revenu IA).

**TEMPORAL (⏰=5) :** synchronisation des rounds de février 2026 (OpenAI et Anthropic levent en même temps que Nvidia franchit 5 000 Md$), correction de juillet 2026 après 18 mois d'euphorie.

---

## 4. HERMÉNEUTIQUE

| Niveau | Interprétation | Statut |
|--------|----------------|--------|
| L1 | Les chiffres de capex et de valorisation sont publiés et recoupés | FAIT |
| L2 | Le ratio 10 pour 1 dépend d'estimations de revenus IA non divulguées (51 Md$ consensus analystes) | FAIT avec marge |
| L3 | La circularité Microsoft-OpenAI est documentée par un filing (24,1 Md$) | FAIT |
| L4 | « Bulle » reste une interprétation : le gap peut se combler par volume (paradoxe de Jevons) | INFERENCE |
| L5 | Le pivot Mistral est documenté par une chronique (opinion) et des citations | FAIT partiel |
| L6 | « OpenAI possède Microsoft » est réfuté par la direction réelle des participations | FAIT |

Faits séparés des inférences : le gap 10:1 est un fait mesuré ; « la bulle va éclater » est une inférence ; « les valorisations sont insoutenables » est une inférence contestée (l'école Jevons, Gartner).

---

## 5. FORENSIC REASONING

**Montré :** les chiffres publiés (capex, valorisations, levées, gains comptables).
**Omis :** les revenus IA par entreprise (4/5 ne publient pas), la part exacte de circularité OpenAI dans les 24,1 Md$, les termes financiers exacts des accords de licence, la réalité des accusations de distillation.
**Reconstruction :** le ratio 10:1 est reconstruit par le consensus d'analystes (51 Md$) ; le 70 % Microsoft-OpenAI est une estimation Bloomberg (entre la moitié et les deux tiers, base 123 % de croissance supposée).

---

## 6. PRISME DIALECTIQUE

**Thèse dominante (institutionnelle) :** « le buildout est rationnel, la demande suivra (paradoxe de Jevons, coût du token divisé par 10, dépenses génératives ×20) » [FCT-001].
**Thèse critique la plus forte :** « c'est un cycle du capital classique : surcapacité avant la demande, comme le rail, la télécom et le shale ; les perdants sont les premiers constructeurs » [FCT-001] ; renforcée par la circularité (OpenAI paie sa propre facture via Microsoft) [FCT-010] et par le financement par dette croissant (Goldman Sachs) [FCT-035].
**Arbitrage :** les deux thèses sont compatibles : la technologie peut être transformatrice et le cycle d'investissement surdimensionné en même temps. Le précédent télécom (transformation réelle, pertes massives des premiers investisseurs, Nasdaq télécom -92 %) est le parallèle le plus instructif. Aucune des deux ne peut être tranchée par les données actuelles.

---

## 7. CHRONOLOGIE

| Date | Événement | Source |
|------|-----------|--------|
| 2024-12 | Contrôles US sur HBM vers la Chine (< 3,3 GB/s par mm²) ; DeepSeek V3 à 5,6 M$ d'entraînement | [SRC-NP] |
| 2025-01 | Annonce Stargate : OpenAI + Oracle + SoftBank, jusqu'à 500 Md$ d'ici 2029 | [SRC-AP] |
| 2025-09 | 5 nouveaux sites Stargate, capacité ~7 GW | [SRC-REU] |
| 2025-10 | Recapitalisation OpenAI ; Nvidia franchit 5 000 Md$ de capitalisation (première entreprise de l'histoire) | [SRC-CNBC5T] |
| 2025-12 | Mistral Large 3, construit sur l'architecture DeepSeek V3 | [SRC-JDN] |
| 2026-01-06 | xAI lève 20 Md$ à ~230 Md$ (Nvidia, Cisco) | [SRC-CNBCXAI] |
| 2026-01-07 | Anthropic : term sheet 10 Md$ à 350 Md$ | [SRC-CNBCA] |
| 2026-01-10 | CNBC : la RAM est « vendue d'avance », prix DRAM +50-55 % au T1 | [SRC-CNBCMEM] |
| 2026-01-15 | BIS révise la politique de licence H200 vers la Chine | [SRC-FR] |
| 2026-02-06 | Annonces capex 2026 (~660 Md$) ; perte de ~900 Md$ de valeur boursière des Big Four en 3 jours | [SRC-CONARD] |
| 2026-02-12 | Anthropic Série G : 30 Md$ à 380 Md$ (GIC, Coatue) | [SRC-ANTH] |
| 2026-02-20 | OpenAI dit aux investisseurs : ~600 Md$ de calcul d'ici 2030 (contre 1 400 Md$ annoncés) ; 13,1 Md$ de revenus 2025 | [SRC-CNBC600] |
| 2026-02-27 | OpenAI : 110 Md$ à 730 Md$ pre-money (SoftBank 30, Nvidia 30, Amazon 50) | [SRC-OAI] |
| 2026-02 | SpaceX acquiert xAI à 250 Md$ | [SRC-BBG] |
| 2026-03-30 | Mistral : 830 M$ de dette (consortium BNP) pour un data center près de Paris | [SRC-CNBCMIST] |
| 2026-04-20 | Amazon investit 5 Md$ de plus dans Anthropic (jusqu'à 20 Md$ possibles) | [SRC-BBG2] |
| 2026-04-24 | DeepSeek V4 : 1 600 Md de paramètres, natif Huawei Ascend, V4-Pro à 3,48 $/M tokens ; SMIC +10 % | [SRC-FORT] |
| 2026-04-24 | Nvidia record, capitalisation repasse au-dessus de 5 000 Md$ | [SRC-CNBC5T2] |
| 2026-04 | Burry : 1,1 Md$ de puts contre Nvidia et Palantir | [SRC-CNBCB] |
| 2026-05-28 | Anthropic Série H : 65 Md$ à 965 Md$ | [SRC-BBG3] |
| 2026-06-30 | Anthropic dépose un S-1 confidentiel | [SRC-CRYPTO] |
| 2026-07-28 | Nasdaq-100 en correction ; Nvidia à 4 770 Md$ sous Apple | [SRC-NBC] |
| 2026-07-29 | Microsoft : gain 3,2 Md$ sur Anthropic, marque -600 M$ sur OpenAI | [SRC-TC] |
| 2026-08-04 | Amazon : 53,4 Md$ de gains comptables T2 sur Anthropic | [SRC-AIWEK] |
| 2026-08-06 | Filing Microsoft : 24,1 Md$ de revenus venus d'OpenAI (~70 % du revenu IA) | [SRC-TNW] |
| 2026-08-11 | Mistral met GLM 5.2 (Z.ai, Chine) en modèle mis en avant, servi tel quel | [SRC-JDN] |
| 2026-08-17 | JDN : « Mistral, installateur de modèles chinois » | [SRC-JDN] |

---

## 8. DOMAINES

**Économique (flux) :** capex Big Five 660-690 Md$ en 2026 [FCT-001] ; Azure AI ~37 Md$/an (+123 %) [FCT-033] ; OpenAI 13,1 Md$ de revenus 2025, 8 Md$ brûlés [FCT-007] ; perte projetée 14 Md$ en 2026, 44 Md$ cumulés 2023-2028, profit attendu 2029 [FCT-035] ; ARR OpenAI ~40 Md$ en août 2026 [FCT-036].

**Financier (valorisations) :** Nvidia 5 000 Md$ (oct. 2025, record mondial) puis 4 770 Md$ (juil. 2026) [FCT-018, FCT-019] ; Anthropic 965 Md$ (mai 2026) [FCT-013] ; OpenAI 730 Md$ pre-money (fév. 2026) [FCT-005] ; xAI 230-250 Md$ [FCT-016, FCT-017] ; SpaceXAI ~1 490 Md$ [FCT-017].

**Technique (matériel) :** goulot HBM : Rubin 288 Go HBM4 par GPU, NVL72 [FCT-004] ; « règle 3 pour 1 » (1 bit HBM = 3 bits de mémoire classique sacrifiés) [FCT-003] ; HBM ~25 % des wafers DRAM, demande +70 % par an [FCT-002] ; mémoire = ~20 % du coût d'un portable [FCT-002].

**Géopolitique (Chine) :** DeepSeek V4 natif Huawei Ascend 950 [FCT-022] ; prix 8-10× inférieurs [FCT-022] ; retard revendiqué de 3 à 6 mois sur la frontière [FCT-022] ; contrôles HBM (déc. 2024, janv. 2026) [FCT-025, FCT-026] ; stock chinois ~13 M de stacks HBM, CXMT ~2 M en 2026 [FCT-027].

**Stratégique (Europe) :** Mistral : dette 830 M$ [FCT-031], objectif 1 Md€ de revenus, 1 GW Europe 2030, Microsoft locataire de ses data centers [FCT-032], pivot hébergeur de modèles chinois [FCT-028, FCT-029].

**Social :** pas d'impact social direct documenté dans cette investigation (renvoi à la fresque IA-salariat). Impact indirect : si la correction du cycle frappe, les plans de licenciements et les retraites des fonds investis sont exposés.

---

## 9. RÉSEAU D'ACTEURS

| Acteur | Rôle dans le réseau | Participation | Documenté par |
|--------|---------------------|---------------|---------------|
| **OpenAI** | Lab central, 900 M WAU, 50 M abonnés | Actionnaires : Microsoft ~27 %, SoftBank 30 Md$, Nvidia 30 Md$, Amazon 50 Md$ | [SRC-OAI, SRC-CNBC600] |
| **Microsoft** | Client 70 % du revenu IA = OpenAI ; investit dans OpenAI et Anthropic | ~27 % OpenAI, 5 Md$ Anthropic ; droits IP OpenAI jusqu'en 2032 | [SRC-TNW, SRC-TC] |
| **Amazon** | Investit dans les deux labs rivaux ; fournit AWS | 50 Md$ OpenAI, ~8 + 5 Md$ (+20 possibles) Anthropic | [SRC-OAI, SRC-BBG2] |
| **Nvidia** | Fournisseur universel de puces, actionnaire des labs | 30 Md$ OpenAI, participation xAI, 100 M$ OpenAI initial | [SRC-CNBC600, SRC-CNBCXAI] |
| **Anthropic** | Lab rival, 965 Md$ de valorisation | Actionnaires : Amazon, Alphabet (jusqu'à 40 Md$), Microsoft | [SRC-BBG3, SRC-AIWEK] |
| **xAI / SpaceXAI** | Lab de Musk, fusionné avec X et SpaceX | SpaceX acquéreur à 250 Md$ ; Nvidia, Cisco | [SRC-CNBCXAI, SRC-BBG] |
| **Oracle** | Co-investisseur Stargate ; partenaire cloud Microsoft | Stargate (OpenAI, SoftBank) jusqu'à 500 Md$ | [SRC-AP, SRC-REU] |
| **SoftBank** | Financier dominant (Stargate, OpenAI) | 30 Md$ OpenAI, co-lead Stargate | [SRC-OAI, SRC-AP] |
| **SK Hynix / Samsung / Micron** | Duopole-trio de la mémoire | Vendent toute leur production 2026 | [SRC-CNBCMEM] |
| **Huawei / SMIC** | Alternative chinoise (Ascend) | DeepSeek V4 natif Ascend | [SRC-FORT] |
| **Mistral** | Champion européen devenu hébergeur | Dette 830 M$ ; locataires dont Microsoft | [SRC-JDN, SRC-CNBCMIST] |
| **DeepSeek / High-Flyer** | Lab chinois open-weight | Propriété du hedge fund High-Flyer ; levée en cours à 20 Md$ (Tencent, Alibaba) | [SRC-FORT] |

**CONTROL_MAP :** points de contrôle : (1) la mémoire HBM (3 vendeurs, vendus d'avance) ; (2) Nvidia (puces) ; (3) Microsoft (Azure, 70 % du revenu IA d'OpenAI y transite) ; (4) le gouvernement US (export controls HBM, licences H200) ; (5) les fonds (SoftBank, GIC, Coatue). GAP : termes financiers exacts des accords de licence non publics.

---

## 10. CHAÎNES / PELOTE

```
CAU-001 : Capex massifs (660-690 Md$) financés par dette croissante (Goldman)
          → surcapacité potentielle (précédent télécom : 85 % de fibre noire)
          → risque de correction des valorisations (Nasdaq-100 -correction juil. 2026)
CAU-002 : Circularité Microsoft-OpenAI : OpenAI lève (SoftBank, Nvidia, Amazon)
          → paie Azure (24,1 Md$ comptés comme revenu IA Microsoft)
          → Microsoft réinvestit en actions OpenAI et en droits IP
          → le « revenu IA » des deux est en partie le même argent (INFERENCE bornée par le filing)
CAU-003 : Contrôles US (HBM, H200) → pénurie chinoise → efficience forcée
          → DeepSeek V4 sur Huawei → prix 10× plus bas → pression déflationniste mondiale
CAU-004 : Goulot HBM (3 vendeurs, 3 pour 1) → les capex GPU sont bornés par la mémoire
          → « memory wall » (les GPU attendent les données)
```

**PELOTE / SOURCE_PROVENANCE :** le chiffre 51 Md$ de revenus IA est un consensus d'analystes reconstruit (seul Microsoft disclose) ; le 70 % Microsoft-OpenAI est une estimation Bloomberg sur une croissance supposée de 123 % ; les gains comptables Amazon sur Anthropic sont des écritures de réévaluation (pas du cash).

---

## 11. CARTE DES PREUVES

### LEAD_REGISTRY

| ID | Lead | Statut |
|----|------|--------|
| LED-001 | Récit de bulle IA | SATURATED (partiel : mesure du gap, pas de verdict d'éclatement) |
| LED-002 | Interdépendance « OpenAI possède Microsoft » | SATURATED (directions réfutées, maillage confirmé) |
| LED-003 | Problème RAM / matériel | SATURATED |
| LED-004 | Chine rapide | SATURATED |
| LED-005 | Mistral intégrateur de modèles chinois | SATURATED |

### CLAIM_REGISTRY

| ID | Claim | Support | Contre | Verdict |
|----|-------|---------|--------|---------|
| CLM-001 | Le gap capex/revenus IA est de ~10:1 en 2026 | FCT-001, FCT-034 (Medium + CNBC) | Estimations de revenus fragiles ; paradoxe de Jevons | **VÉRIFIÉ (marge)** |
| CLM-002 | OpenAI possède Microsoft | Aucune source | Microsoft ~27 % d'OpenAI ; 70 % du revenu IA Microsoft vient d'OpenAI | **RÉFUTÉ (inversion)** |
| CLM-003 | Microsoft possède Oracle | Aucune source | Partenariat + co-investissement Stargate | **RÉFUTÉ** |
| CLM-004 | Le maillage actionnarial des labs est dense | FCT-005, FCT-011, FCT-015, FCT-016 | - | **VÉRIFIÉ** |
| CLM-005 | La RAM est le goulot 2026 | FCT-002, FCT-003, FCT-004 | Des fabs arrivent 2027-2030 | **VÉRIFIÉ** |
| CLM-006 | La Chine rattrape la frontière | FCT-022, FCT-024, FCT-027 | Retard 3-6 mois, contraintes HBM et lithographie | **VÉRIFIÉ (nuancé)** |
| CLM-007 | Mistral devient intégrateur de modèles chinois | FCT-028, FCT-029, FCT-030 | La chronique JDN est un texte d'opinion ; la direction parle de « bonne raison » | **VÉRIFIÉ (faits documentés, jugement éditorial)** |
| CLM-008 | Les participations croisées faussent les résultats publiés | FCT-014, FCT-015 (gains comptables) | Écritures légitimes de réévaluation | **VÉRIFIÉ (mécanique comptable, pas une fraude)** |

### FACT_REGISTRY_V1

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://medium.com/@mstyvola/the-10-to-1-gap-holding-up-the-entire-ai-boom-e1b1054fec16 | D | 2026-07-01 | capex-ai-gap | 10:1 (660-690 Md$/51 Md$) | dbec58b9-92a8-48c9-8d37-749b4a8b7f83
FCT-002 | FACT | ✧ | https://www.cnbc.com/2026/01/10/micron-ai-memory-shortage-hbm-nvidia-samsung.html | C | 2026-01-10 | ram-prix-hausse | +50-55% T1 2026 | 6883a95b-d5d9-4667-a40b-17240e347f4e
FCT-003 | FACT | ✧ | https://www.cnbc.com/2026/01/10/micron-ai-memory-shortage-hbm-nvidia-samsung.html | C | 2026-01-10 | hbm-sold-out | 2026 entier, règle 3:1 | 3f623492-e45b-4d08-8736-ec00a6b48a38
FCT-004 | FACT | ✧ | https://www.cnbc.com/2026/01/10/micron-ai-memory-shortage-hbm-nvidia-samsung.html | C | 2026-01-10 | rubin-hbm4 | 288 Go HBM4, NVL72 | 689817d6-af79-4b92-be47-44f4b430a456
FCT-005 | FACT | ✦ | https://openai.com/index/scaling-ai-for-everyone/ | A,C | 2026-02-27 | openai-110b-730b | 110 Md$ à 730 Md$ pre | ccf4178e-95b1-4ac8-9390-7f3a15df4bb9
FCT-006 | FACT | ✦ | https://openai.com/index/scaling-ai-for-everyone/ | A,C | 2026-02-27 | chatgpt-wau | 900 M WAU, 50 M abonnés | 2208c40d-aeec-459c-874a-c4ff5d1117ed
FCT-007 | FACT | ✧ | https://www.cnbc.com/2026/02/20/openai-resets-spend-expectations-targets-around-600-billion-by-2030.html | C | 2026-02-20 | openai-2025-revenus | 13,1 Md$ revenus, 8 Md$ brûlés | 53dffb71-7d24-4329-ba87-8f1e9a97798c
FCT-008 | FACT | ✧ | https://www.cnbc.com/2026/02/20/openai-resets-spend-expectations-targets-around-600-billion-by-2030.html | C | 2026-02-20 | openai-reset-600b | 600 Md$ d'ici 2030 vs 1400 Md$ | 53dffb71-7d24-4329-ba87-8f1e9a97798c
FCT-009 | FACT | ✧ | https://thenextweb.com/news/microsoft-ai-revenue-openai-70-percent-dependence | C | 2026-08-06 | microsoft-openai-70pct | 24,1 Md$ ≈ 70 % revenu IA | 476ccb32-4dc2-4515-bfc6-70315338bee7
FCT-010 | FACT | ✧ | https://thenextweb.com/news/microsoft-ai-revenue-openai-70-percent-dependence | C | 2026-08-06 | circularite-openai | facture calcul OpenAI = revenu Microsoft | 476ccb32-4dc2-4515-bfc6-70315338bee7
FCT-011 | FACT | ⁅ | - | - | - | microsoft-openai-27pct | ~27 % (recap 2025) | -
FCT-012 | FACT | ⁅ | - | - | - | anthropic-serie-g | 30 Md$ à 380 Md$ | -
FCT-013 | FACT | ⁅ | - | - | - | anthropic-serie-h | 65 Md$ à 965 Md$ | -
FCT-014 | FACT | ⁅ | - | - | - | amazon-gains-anthropic | 16,8 Md$ T1, 53,4 Md$ T2 | -
FCT-015 | FACT | ⁅ | - | - | - | microsoft-anthropic-5b | 5 Md$, gain 3,2 Md$ | -
FCT-016 | FACT | ⁅ | - | - | - | xai-20b-230b | 20 Md$ à 230 Md$ | -
FCT-017 | FACT | ⁅ | - | - | - | spacex-xai-250b | SpaceXAI ~1490 Md$ | -
FCT-018 | FACT | ⁅ | - | - | - | stargate-500b | 500 Md$, ~7 GW | -
FCT-019 | FACT | ⁅ | - | - | - | nasdaq-correction | juil. 2026, Nvidia 4770 Md$ | -
FCT-020 | FACT | ⁅ | - | - | - | burry-puts | 1,1 Md$ Nvidia+Palantir | -
FCT-021 | FACT | ⁅ | - | - | - | bigfour-900md | -900 Md$ fév. 2026 | -
FCT-022 | FACT | ✧ | https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/ | C | 2026-04-24 | deepseek-v4 | 1,6 T params, 3,48 $/M, Ascend | 255e5091-f334-4d86-9f55-4c000ac6cf0f
FCT-023 | FACT | ✧ | https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/ | C | 2026-04-24 | deepseek-20b-levée | High-Flyer, Tencent/Alibaba | 729e2c37-d33f-4f2f-82dd-95890bf39ea2
FCT-024 | FACT | ✧ | https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/ | C | 2026-04-24 | smic-plus10 | +10 % HK | 729e2c37-d33f-4f2f-82dd-95890bf39ea2
FCT-025 | FACT | ⁅ | - | - | - | hbm-export-controls | déc. 2024, <3,3 GB/s/mm² | -
FCT-026 | FACT | ⁅ | - | - | - | bis-janv-2026 | révision H200 | -
FCT-027 | FACT | ⁅ | - | - | - | chine-hbm-stock | ~13 M stacks, CXMT 2 M | -
FCT-028 | FACT | ✧ | https://www.journaldunet.com/intelligence-artificielle/1553715-mistral-ou-comment-le-champion-europeen-de-l-ia-devient-un-installateur-de-modeles-chinois/ | C | 2026-08-17 | mistral-large3-archi | architecture DeepSeek V3 | 9233b9ce-059a-45da-9b43-d1d1d613ca3c
FCT-029 | FACT | ✧ | https://www.journaldunet.com/intelligence-artificielle/1553715-mistral-ou-comment-le-champion-europeen-de-l-ia-devient-un-installateur-de-modeles-chinois/ | C | 2026-08-17 | mistral-glm52 | GLM 5.2 servi tel quel | 5c4e0129-47d1-4ee2-86c8-41a94ce43fdd
FCT-030 | FACT | ✧ | https://www.journaldunet.com/intelligence-artificielle/1553715-mistral-ou-comment-le-champion-europeen-de-l-ia-devient-un-installateur-de-modeles-chinois/ | C | 2026-08-17 | mistral-lacroix-quote | citation VentureBeat | 5c4e0129-47d1-4ee2-86c8-41a94ce43fdd
FCT-031 | FACT | ⁅ | - | - | - | mistral-830m-dette | 830 M$ BNP consortium | -
FCT-032 | FACT | ✧ | https://www.journaldunet.com/intelligence-artificielle/1553715-mistral-ou-comment-le-champion-europeen-de-l-ia-devient-un-installateur-de-modeles-chinois/ | C | 2026-08-17 | mistral-1gw-1mde | 1 Md€ visé, 1 GW 2030 | 35afe284-e4ff-4fc7-b6bb-1ae8daf7e23c
FCT-033 | FACT | ✧ | https://medium.com/@mstyvola/the-10-to-1-gap-holding-up-the-entire-ai-boom-e1b1054fec16 | D | 2026-07-01 | azure-ai-37b | 37 Md$/an, +123 % | f5a025f2-4d6e-4e88-8cc0-23453f990479
FCT-034 | FACT | ✧ | https://medium.com/@mstyvola/the-10-to-1-gap-holding-up-the-entire-ai-boom-e1b1054fec16 | D | 2026-07-01 | gap-2025-realise | 443 Md$ vs 40-60 Md$ (7-8:1) | 2f91380a-2088-4533-bb3c-02dc07163d83
FCT-035 | FACT | ⁅ | - | - | - | openai-14b-perte | 14 Md$ 2026, 44 Md$ cumulés | -
FCT-036 | FACT | ⁅ | - | - | - | openai-arr-40b | ~40 Md$ août 2026 | -
<!-- /FACT_REGISTRY_V1 -->

### TRACE_MATRIX (extrait)

| FCT | Support | Contre | REFUTATION_SEARCHED |
|-----|---------|--------|---------------------|
| FCT-001 | Medium (fetch) + CNBC (capex 700 Md$) | Revenus non disclosés = estimation | QRY-REF-1 : « capex vs revenus IA même niveau 2026 » → NONE (aucune source inverse trouvée) |
| FCT-005 | OpenAI (fetch) + CNBC (Nvidia 30 Md$) | - | QRY-REF-2 : « OpenAI 730 milliards surévalué contestation » → NONE |
| FCT-009 | TNW (fetch) + Bloomberg | 70 % = estimation (entre 50 % et 2/3) | QRY-REF-3 : « Microsoft AI revenue OpenAI pourcentage différent » → NONE (chiffres 24,1 Md$ stables) |
| FCT-022 | Fortune (fetch) + Reuters/SCMP | Autres benchmarks ; « 3-6 mois de retard » = auto-déclaration DeepSeek | QRY-REF-4 : « DeepSeek V4 démenti mauvaise performance » → NONE |
| FCT-028/029 | JDN (fetch) | Chronique = texte d'opinion ; « architecture DeepSeek » = analyse technique, pas admission de Mistral | QRY-REF-5 : « Mistral démenti architecture chinoise » → NONE |

### EDI (diversité du corpus)

| Dimension | État |
|-----------|------|
| Géographique | US (majorité), Chine (Fortune/Reuters), Europe (JDN, CNBC) |
| Familles de provenance | A (OpenAI, Anthropic), C (CNBC, TNW, Fortune, NBC, Reuters, SCMP), D (Medium/analyste), F (The Information, WSJ, Bloomberg via citations) |
| Biais | Surreprésentation des sources financières US ; les sources primaires chinoises (DeepSeek, Huawei) sont médiées par la presse ; aucune donnée comptable primaire des labs (privés) |
| GAP EDI | Le point de vue des salariés/impact social absent ; les chiffres internes OpenAI reposent sur des fuites (The Information) |

---

## 12. CARTE DIALECTIQUE

**Scénario A (atterrissage en douceur) :** le paradoxe de Jevons comble le gap (coût du token divisé, usage ×20) ; les valorisations se consolident autour des revenus réels ; Nvidia et les labs survivent avec des marges réduites.
**Scénario B (correction douloureuse) :** précédent télécom : 85 % de capacité inutilisée, -90 % sur les acteurs purs, les perdants sont les premiers constructeurs ; les labs non rentables (OpenAI : -14 Md$ en 2026) se consolident ; les gains comptables géants (Amazon 53,4 Md$) s'évaporent.
**Scénario C (bifurcation) :** la Chine (DeepSeek V4 sur Huawei, prix -90 %) impose la déflation des prix d'inférence ; les labs US se replient sur les modèles premium ; la marge de l'industrie se déplace vers la mémoire (3 vendeurs) et l'énergie.

**Carte des responsabilités (ACT) :**

| ACT | Nom | Action documentée | Intention |
|-----|-----|-------------------|-----------|
| ACT-001 | Sam Altman (OpenAI) | A annoncé 1 400 Md$ de dépenses puis a réduit à 600 Md$ | UNKNOWN |
| ACT-002 | Satya Nadella (Microsoft) | A fait transiter 24,1 Md$ de facture OpenAI par Azure comptés en revenus IA | UNKNOWN |
| ACT-003 | Timothée Lacroix (Mistral) | A justifié l'hébergement de GLM 5.2 | CLAIMED (citation) |
| ACT-004 | Gouvernement US (BIS) | Contrôles HBM et révision des licences H200 | PROVEN (décisions) |
| ACT-005 | Fondateurs des labs | Rounds de levées à valorisations records, gains comptables des investisseurs | UNKNOWN |

---

## 13. PÉRIMÈTRE & LIMITES

**Inclusions :** participations et flux documentés entre OpenAI, Microsoft, Oracle, Anthropic, xAI/SpaceX, Nvidia, Amazon, Alphabet, SoftBank, Mistral, DeepSeek/Huawei ; marché de la mémoire ; export controls HBM ; période août 2024 à août 2026.
**Exclusions :** impact social/emploi (couvert par la fresque IA-salariat) ; la question des brevets et de la propriété intellectuelle des architectures ; les détails de gouvernance interne des labs (non publics).
**Limites d'accès :** GAP_TYPE=ACCESS pour les sources à paywall/refus bot : Reuters (401), Yahoo Finance (page consentement), Windows Central (fichier > 2 Mo), The Information, WSJ, Bloomberg (paywall). Les faits FCT-011 à FCT-021, FCT-025 à FCT-027, FCT-031, FCT-035, FCT-036 reposent sur des snippets de recherche non fetchés : tiers ⁅ (UNKNOWN), pas de write-back.
**Limites de méthode :** le ratio 10:1 dépend d'estimations ; le 70 % est une estimation Bloomberg ; les « 3-6 mois de retard » de DeepSeek V4 sont une auto-évaluation ; le constat « architecture DeepSeek pour Mistral Large 3 » est une analyse externe (JDN), pas un aveu de Mistral.

---

## 14. ÉTAT DES CONNAISSANCES

**Connu (✧/✦ ancrés) :** le gap capex/revenus (~10:1), la pénurie HBM 2026, le reset OpenAI (1 400 → 600 Md$), la dépendance Microsoft-OpenAI (24,1 Md$, ~70 %), la circularité, DeepSeek V4 sur Huawei, le pivot Mistral (GLM 5.2, architecture Large 3), Azure AI 37 Md$.
**Probable (non fetché, ⁅) :** parts exactes (Microsoft ~27 % OpenAI), valorisations Anthropic 380 puis 965 Md$, gains comptables Amazon (16,8 puis 53,4 Md$), xAI 20 Md$ à 230 Md$, acquisition SpaceX à 250 Md$, Stargate 500 Md$, contrôles HBM détaillés, stock HBM chinois 13 M stacks, pertes OpenAI 14 Md$/44 Md$, dette Mistral 830 M$.
**Affirmé et réfuté :** « OpenAI possède Microsoft » (inversion), « Microsoft possède Oracle » (faux, partenariat).
**Inconnu :** les termes financiers exacts des accords de licence ; la part exacte de circularité dans les 24,1 Md$ ; la réalité des accusations de distillation ; la viabilité des valorisations (non testable).

---

## 15. SUSPICION / VÉRIFICATION

**Audit des sources :** les sources financières (CNBC, Fortune, TNW) sont des médias de famille C, fiables sur les chiffres publiés, faibles sur l'interprétation. La chronique JDN est un texte d'opinion : ses faits (dates, montants, citations) sont vérifiables, son jugement (« renoncement ») est éditorial. Le Medium « the watcher » est un analyste indépendant (famille D) : ses calculs sont reproductibles, ses hypothèses (75 % de part IA du capex, 51 Md$ consensus) sont explicites.
**STATUS_DELTA :** aucun fait n'a changé de statut au cours de la vérification (pas de re-vérification d'anciens faits dans ce run).
**CONTRADICTION_LEDGER :** les seules contradictions sont les inversions du lead utilisateur (CLM-002, CLM-003), résolues par les directions réelles des participations. La tension Jevons vs cycle du capital (FCT-001) est une controverse interprétative non résolue, documentée comme telle.
**Contre-requêtes (REFUTATION_SEARCHED) :** 5 menées (QRY-REF-1 à 5), toutes NONE. À noter : aucune réfutation n'a été trouvée sur les chiffres pivots (capex, 24,1 Md$, DeepSeek V4, GLM 5.2).

---

## SOURCES

| SRC-ID | Titre | Date | Rôle | URL |
|--------|-------|------|------|-----|
| SRC-OAI | OpenAI, « Scaling AI for everyone » | 2026-02-27 | ◈ (annonce primaire, fetchée) | https://openai.com/index/scaling-ai-for-everyone/ |
| SRC-CNBC600 | CNBC, « OpenAI resets spend expectations » | 2026-02-20 | ◉ (fetchée) | https://www.cnbc.com/2026/02/20/openai-resets-spend-expectations-targets-around-600-billion-by-2030.html |
| SRC-CNBCMEM | CNBC, « AI memory is sold out » | 2026-01-10 | ◉ (fetchée) | https://www.cnbc.com/2026/01/10/micron-ai-memory-shortage-hbm-nvidia-samsung.html |
| SRC-TNW | TNW, « Microsoft's AI business is mostly OpenAI » | 2026-08-06 | ◉ (fetchée) | https://thenextweb.com/news/microsoft-ai-revenue-openai-70-percent-dependence |
| SRC-FORT | Fortune, « DeepSeek unveils V4 » | 2026-04-24 | ◉ (fetchée) | https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/ |
| SRC-JDN | JDN, « Mistral, installateur de modèles chinois » | 2026-08-17 | ◉ (fetchée, chronique) | https://www.journaldunet.com/intelligence-artificielle/1553715-mistral-ou-comment-le-champion-europeen-de-l-ia-devient-un-installateur-de-modeles-chinois/ |
| SRC-MED | Medium, « The 10-to-1 Gap » | 2026-07-01 | ◉ (fetchée, analyste) | https://medium.com/@mstyvola/the-10-to-1-gap-holding-up-the-entire-ai-boom-e1b1054fec16 |
| SRC-AP | AP News, « Trump highlights $500B AI investment » | 2025-01-22 | ○ (snippet) | https://apnews.com/article/trump-ai-openai-oracle-softbank-son-altman-ellison-be261f8a8ee07a0623d4170397348c41 |
| SRC-REU | Reuters, « Stargate five new sites » | 2025-09-23 | ○ (snippet) | https://www.reuters.com/business/media-telecom/openai-oracle-softbank-plan-five-new-ai-data-centers-500-billion-stargate-2025-09-23/ |
| SRC-CNBC5T | Morningstar/CNBC, « Nvidia crosses $5T » | 2025-10-29 | ○ (snippet) | https://www.morningstar.com/markets/nvidia-crosses-5-trillion-5-charts-unstoppable-tech-rally |
| SRC-CNBC5T2 | CNBC, « Nvidia stock closes at record past $5T » | 2026-04-24 | ○ (snippet) | https://www.cnbc.com/2026/04/24/nvidia-stock-closes-at-record-pushing-market-cap-past-5-trillion.html |
| SRC-CNBCXAI | CNBC, « xAI raises $20B » | 2026-01-06 | ○ (snippet) | https://www.cnbc.com/2026/01/06/elon-musk-xai-raises-20-billion-from-nvidia-cisco-investors.html |
| SRC-CNBCA | CNBC, « Anthropic term sheet $350B » | 2026-01-07 | ○ (snippet) | https://www.cnbc.com/2026/01/07/anthropic-funding-term-sheet-valuation.html |
| SRC-ANTH | Anthropic, « Series G $380B » | 2026-02-12 | ◈ (snippet, non fetchée) | https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation |
| SRC-BBG3 | Bloomberg TV, « Anthropic $965B » | 2026-05-28 | ○ (snippet) | https://www.facebook.com/BloombergTelevision/posts/anthropic-raised-65-billion-... |
| SRC-BBG2 | Bloomberg, « Amazon to invest $5B more in Anthropic » | 2026-04-20 | ○ (snippet) | https://www.bloomberg.com/news/articles/2026-04-20/amazon-to-invest-an-additional-5-billion-in-anthropic |
| SRC-TC | TechCrunch, « Microsoft logs $3.2B from Anthropic » | 2026-07-29 | ○ (snippet) | https://techcrunch.com/2026/07/29/microsoft-logs-3-2b-from-anthropic-investment-but-openai-was-a-mixed-bag/ |
| SRC-BBG | Bloomberg, « SpaceX-xAI $250B » | 2026-02 | ○ (snippet) | https://en.wikipedia.org/wiki/SpaceXAI |
| SRC-CONARD | Edward Conard (FT reprise), « $660bn spending spree » | 2026-02-06 | ○ (snippet) | https://www.edwardconard.com/macro-roundup/amazon-google-meta-and-microsoft-plan-to-spend-660b-on-capex-in-2026-... |
| SRC-CNBCB | CNBC via Facebook, « Burry $1.1B bet » | 2026-04-10 | ○ (snippet) | https://www.facebook.com/cnbc/posts/... |
| SRC-NBC | NBC News, « Nasdaq-100 in correction » | 2026-07-28 | ○ (snippet) | https://www.nbcnews.com/business/markets/nasdaq-100-correction-tech-stocks-rcna589630 |
| SRC-AIWEK | AI Weekly, « Amazon's $53.4B Anthropic gain » | 2026-08-04 | ○ (snippet) | https://aiweekly.co/alerts/amazons-534b-anthropic-gain-distorts-big-tech-q2-earnings |
| SRC-FR | Federal Register, « BIS revision license review » | 2026-01-15 | ◈ (snippet) | https://www.federalregister.gov/documents/2026/01/15/2026-00789/ |
| SRC-NP | NextPlatform, « US curbs HBM exports » | 2024-12-02 | ○ (snippet) | https://www.nextplatform.com/store/2024/12/02/us-curbs-hbm-exports-to-china-... |
| SRC-SEMI | SemiconductorX, « Huawei supply chain » | 2026 | ○ (snippet) | https://semiconductorx.com/spotlight-huawei-hisilicon.html |
| SRC-CNBCMIST | CNBC, « Mistral $830M debt » | 2026-03-30 | ○ (snippet) | https://www.cnbc.com/2026/03/30/mistral-ai-paris-data-center-cluster-debt-financing.html |
| SRC-CRYPTO | CryptoBriefing, « Anthropic S-1 » | 2026-06-30 | ○ (snippet, fiabilité faible) | https://cryptobriefing.com/anthropic-ipo-filing-2026-valuation/ |
| SRC-INFO | The Information, « OpenAI $14B loss » | 2024-10-09 | ○ (snippet, paywall) | https://www.theinformation.com/articles/openai-projections-imply-losses-tripling-to-14-billion-in-2026 |

---

## REQUEST_LOG

ENGINE:2.8 | MANIFEST:FINAL | RUN_ID:20260825-1500-bulle-ia-interdependance-acteurs | PARENT_RUN_ID:NONE | AS_OF:2026-08-25 | INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:NONE
CHECKPOINT_SEQ:1 | LAST_COMPLETED:18b | NEXT_ACTION:NONE | RESUME_COUNT:0
Investigation:bulle-ia-interdependance-acteurs | complexity:16→APEX | route overrides:NONE | scope:2024-08→2026-08-25, US+Chine+FR/EU
modules:SYMBOLS,PATTERNS,THREATS,GATES,REQUEST_LOG,FACT_VERIFICATION,TEMPLATE,INVESTIGATION(partiel),MONEY,NETWORK,POWER,ICEBERG,TEMPORAL
degraded:NONE | query target/actual:12/14 (2 requêtes exploratoires au-delà de la cible)

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL/INPUT_REF |
|---:|-----|-----------------|--------|--------|---------------|
| 1 | SYS | @MNEMO_Q (recherche mémoire, 1 fois/RUN_ID) | FOUND : contexte faits vérifiés précédents (aucun doublon direct) | MnemoLite | - |
| 2 | ◉ | QRY-001 : capex 2026 vs revenus IA | FOUND : CNBC ~700 Md$, Conard 660 Md$ | SRC-CONARD + CNBC | https://www.cnbc.com/2026/02/06/google-microsoft-meta-amazon-ai-cash.html |
| 3 | ◉ | QRY-002 : participations Microsoft/OpenAI/Nvidia/Anthropic | FOUND : recap 2025 (27 %), 110 Md$ OpenAI | SRC-OAI + penchan | https://openai.com/index/scaling-ai-for-everyone/ |
| 4 | ◉ | QRY-003 : pénurie HBM 2026 | FOUND : CNBC mémoire | SRC-CNBCMEM | https://www.cnbc.com/2026/01/10/micron-ai-memory-shortage-hbm-nvidia-samsung.html |
| 5 | ◉ | QRY-004 : Mistral pivot chinois | FOUND : JDN chronique | SRC-JDN | https://www.journaldunet.com/intelligence-artificielle/1553715-... |
| 6 | ◉ | QRY-005 : Chine/DeepSeek/HBM contrôles | FOUND : Fortune, Federal Register, SemiconductorX | SRC-FORT + SRC-FR | - |
| 7 | ◉ | QRY-006 : xAI/Oracle/Stargate | FOUND : xAI 20 Md$, SpaceXAI | SRC-CNBCXAI, SRC-BBG | - |
| 8 | ◉ | QRY-007 : warnings bulle (Burry, Ackman, Dalio) | FOUND : Burry puts, Dalio, Goldman dette | SRC-CNBCB | - |
| 9 | ◉ | QRY-008 : Anthropic valorisations | FOUND : Série G 380 Md$, Série H 965 Md$ | SRC-ANTH, SRC-BBG3 | - |
| 10 | ◉ | QRY-009 : OpenAI revenus/pertes 2026 | FOUND : 14 Md$ (The Information), ARR 40 Md$ | SRC-INFO | - |
| 11 | ◉ | QRY-010 : OpenAI reset 1 400→600 Md$ | FOUND : CNBC | SRC-CNBC600 | https://www.cnbc.com/2026/02/20/openai-resets-spend-expectations-... |
| 12 | ◉ | QRY-011 : Microsoft 70 % revenu IA OpenAI | FOUND : TNW, Yahoo, Windows Central | SRC-TNW | https://thenextweb.com/news/microsoft-ai-revenue-openai-70-percent-dependence |
| 13 | ◉ | QRY-012 : DeepSeek V4 Huawei | FOUND : Fortune (fetch), Reuters (401), SCMP | SRC-FORT | https://fortune.com/2026/04/24/deepseek-v4-ai-model-price-performance-china-open-source/ |
| 14 | ◉ | QRY-013 : Nvidia 5 000 Md$ + correction | FOUND : CNBC, NBC | SRC-CNBC5T2, SRC-NBC | - |
| 15 | ◉ | QRY-014 : Stargate/Oracle détails | FOUND : Reuters, Wikipedia, IntuitionLabs | SRC-REU | - |
| 16 | SYS | @FETCH CNBC-mémoire | OK, EXCERPT_OK | SRC-CNBCMEM | url ci-dessus |
| 17 | SYS | @FETCH OpenAI | OK, EXCERPT_OK | SRC-OAI | url ci-dessus |
| 18 | SYS | @FETCH JDN | OK, EXCERPT_OK | SRC-JDN | url ci-dessus |
| 19 | SYS | @FETCH Medium 10-to-1 | OK, EXCERPT_OK | SRC-MED | url ci-dessus |
| 20 | SYS | @FETCH CNBC reset 600 Md$ | OK, EXCERPT_OK | SRC-CNBC600 | url ci-dessus |
| 21 | SYS | @FETCH Fortune V4 | OK, EXCERPT_OK | SRC-FORT | url ci-dessus |
| 22 | SYS | @FETCH TNW | OK, EXCERPT_OK | SRC-TNW | url ci-dessus |
| 23 | SYS | @FETCH Reuters V4 | FAILED : 401 Forbidden (GAP_TYPE=ACCESS) | - | https://www.reuters.com/world/china/deepseek-v4-... |
| 24 | SYS | @FETCH Yahoo 70 % | FAILED : page consentement (GAP_TYPE=ACCESS) | - | https://finance.yahoo.com/... |
| 25 | SYS | @FETCH Windows Central | FAILED : réponse > 2 Mo (GAP_TYPE=ACCESS) | - | https://www.windowscentral.com/... |
| 26 | SYS | QRY-REF-1..5 : contre-requêtes (voir TRACE_MATRIX) | 5× NONE (aucune réfutation) | - | - |
| 27 | SYS | CHECKPOINT OPEN écrit (SEQ-1) | OK | - | même path |
| 28 | SYS | @MNEMO_S + STATE:FINAL @WRITE + FACT_WRITEBACK | PENDING_AT_SERIALIZATION (19a avant 19b) | - | - |

COUNT: ◈2 ◉12 ○12 | unique evidence objects: 28 | upstream families: 4 (A, C, D, F via citations)
LEADS: terminal 5/5 | AXES: terminal 8/8 | N/A: aucun
FAILURES: 3 (Reuters, Yahoo, WindowsCentral) | FALLBACKS: 1 (TNW en remplacement de Yahoo/WindowsCentral pour le 70 %) | unresolved gaps: ACCESS:3, ESTIMATION:4 (parts exactes, part circularité, valorisations non publiques)

---

## TL;DR

```text
SUJET : Bulle IA et interdépendance des acteurs (OpenAI, Microsoft, Oracle, Anthropic, xAI, Nvidia, Amazon, Mistral, DeepSeek/Huawei)
OBJET : Gap capex/revenus IA ~10:1 en 2026 (7-8:1 sur réalisés 2025) [FCT-001, FCT-034] ; maillage actionnarial dense mais directions différentes du lead (Microsoft ~27 % OpenAI, 70 % de son revenu IA vient d'OpenAI, circulaire) [FCT-009, FCT-011] ; goulot HBM : production 2026 vendue d'avance, prix +50-55 % [FCT-002, FCT-003] ; Chine : DeepSeek V4 natif Huawei, prix 10× inférieurs [FCT-022] ; Mistral : pivot confirmé, héberge GLM 5.2, Large 3 sur architecture DeepSeek [FCT-028, FCT-029]
SOURCE : lead utilisateur partiellement réfuté (inversions de sens des participations) mais constat de maillage confirmé ; pas de document source unique
MANIPULATION : €=8, 🌐=8, Ξ=6 : l'argent circule en circuit fermé, les revenus IA sont opaques, la circularité fausse les lectures
LIMITE : GAP_TYPE=ACCESS (paywalls) ; estimations non publiques (parts, valorisations privées) ; le verdict « bulle » reste une interprétation non tranchable
```
