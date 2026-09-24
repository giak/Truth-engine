ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260920-1704-insee-biais-modes-calcul-fresque-systemique | PARENT_RUN_ID:NONE | AS_OF:2026-09-20
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-20_insee-biais-modes-calcul-fresque-systemique/2026-09-20_17-04_insee-biais-modes-calcul-fresque-systemique_INPUT.txt | SUBJECT_SLUG:insee-biais-modes-calcul-fresque-systemique | SUBJECT_FP:sha256:65f5d8abf9713f40c4382c528c71296a76a8b09257f6ca339173dcdfe1f58f28 | INPUT_SHA256:sha256:a4fb26f3fe0d07a88ffb33df02ca3110a3d8839973fd48f2916b346aa59e9a39
COMPLEXITY:17→APEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:1946-2026 (focus 2004-2026); France (metropole+Outre-mer), comparaison UE/ONS/Destatis; axes: methodes IPC, perception, gouvernance, recrutements, independance legale, moyens, revisions, indexations, pressions documentees, pauvrete, international, gouvernementalite; exclusions: theorie du complot sans appui documente; limites: archives internes Insee inaccessibles, ampleur budgetaire exacte non etablie
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,search/EPISTEMIC.md,search/TEMPLATES.md,output/TEMPLATE.md,protocol/FACT_VERIFICATION.md,protocol/INVESTIGATION.md,clusters/ICEBERG.md,clusters/MONEY.md,clusters/FRAMING.md,clusters/POWER.md,clusters/RESISTANCE.md,clusters/CONFIRMATION.md,clusters/FRAGMENTATION.md,clusters/NETWORK.md,clusters/TEMPORAL.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# L'INSEE : mesure officielle, dépendances et effets concrets — fresque systémique

## 1. RÉSUMÉ EXÉCUTIF

**Question objet.** Comment l'Insee produit-elle la mesure statistique officielle (prix, pauvreté, croissance), qui décide de ses choix méthodologiques, avec quelles dépendances, et quels effets concrets ces choix produisent-ils sur les montants indexés et la perception publique ?

**Réponse bornée.** L'Insee est un institut techniquement standardisé, juridiquement encadré (FCT-007), mais structurellement enchâssé dans l'exécutif : directeur général nommé en Conseil des ministres sur proposition de Bercy (FCT-002), budget voté dans la loi de finances (programme 220 : 472,5 M€ d'autorisations d'engagement en 2025, en baisse de 2,7 % — SRC-017), direction recrutée dans le canal Polytechnique–ENSAE–Trésor (FCT-008, SRC-006, SRC-023). Sa mesure phare, l'indice des prix à la consommation (IPC), exclut le coût du logement des propriétaires occupants — méthode que le manuel Eurostat lui-même qualifie de « trop étroite » — tandis que l'Allemagne, les États-Unis et le Royaume-Uni l'incluent (FCT-005) ; l'IPC français inclut en revanche les dépenses de santé remboursées, ce qui en fait un indice hybride (SRC-021). Cet indice sert d'indexeur légal : SMIC, IRL, contrats, pensions (FCT-004, FCT-006, CAU-002), y compris via une formule d'IRL qui exclut elle-même les loyers de son calcul (FCT-004). L'écart entre inflation mesurée et inflation perçue est massif et reconnu officiellement : environ six points en moyenne depuis 2004, avec des « bases objectives » reconnaissables à la perception (FCT-001). Les premières estimations de la croissance sont si sensibles au contexte inflationniste que 2023 est passée de 0,9 % à 1,9 % après révision — la plus forte révision depuis 2003 (FCT-003). La pauvreté mesurée atteint 9 817 000 personnes au seuil de 60 % (FCT-009).

**Verdict sur le lead utilisateur (« l'Insee ne reflète pas la réalité »).** Formulé comme assertion générale, ce lead est **partiellement étayé et partiellement réfuté** : l'écart mesure/ressenti est réel et documenté (FCT-001, FCT-005), les choix de champ ont des effets juridiques concrets (FCT-004, FCT-006), mais « ne reflète pas la réalité » au sens d'une falsification délibérée n'est **pas établi** — aucun fait ne démontre de manipulation micro d'un chiffre par l'Insee, et les contre-explications conventionnelles (normes internationales, contraintes de mesure) sont matérielles (CON-002, CON-004). Le sujet réel est celui d'une **convention de mesure enchâssée dans des intérêts d'indexation**, pas d'un complot de chiffres.

**Acteurs.** Direction de l'Insee, ministère de l'Économie, Autorité de la statistique publique, Eurostat, contre-pouvoirs (UFC-Que Choisir, économistes, presse spécialisée).

**Impact.** Chaque dixième de point d'IPC se répercute sur des montants légaux (amplitude exacte : GAP d'accès, CAU-002) ; les révisions transforment rétroactivement le récit économique public (FCT-003) ; la défiance perceptive est structurelle (FCT-001).

**Gaps principaux.** Accès (chiffrage budgétaire des indexations, archives internes, rapport ASP intégral, peer review Eurostat brut), causalité (lien homophilie→méthode non démontré au niveau individuel), périmètre (champs exacts IPC/ERFS).

## 2. MANIPULATION_REPORT

- **INPUT_KIND** : TOPIC. **MISSION_MODE** : INVESTIGATION.
- **SYMBOL_STAGE** : CORPUS_FINAL (évaluation sur corpus inspecté, 28 sources).
- **Symboles (0-10)** : Ξ omission **6** (champ IPC hors logements propriétaires, champ « France hors Mayotte »/métropole selon séries, ruptures ERFS 2010-2012-2020) ; € argent **7** (IPC indexe SMIC/IRL/pensions/OATi ; budget programme 220) ; Λ cadrage **5** (IPC médiatiquement traité comme « coût de la vie » alors que l'Insee le borne à la dépense de consommation — SRC-013, SRC-001) ; Ω inversion **2** (aucune contradiction archivée/dénégation détectée) ; Ψ sidération **2** ; ↕ pouvoir vertical **6** (nomination en Conseil des ministres, tutelle, budget — FCT-002, SRC-017) ; Φ spectacle **3** (médiasation des chiffres mensuels) ; Σ sémiotique **3** (marque « Insee », autorité du chiffre officiel) ; Κ cynisme **3** (maintien d'un champ contesté malgré débat documenté) ; ρ résistance **5** (indices alternatifs UFC, analyses académiques, débats ASP) ; κ influence subtile **4** (architecture légale d'indexation favorable, sans preuve de design de perception) ; ⫸ convergence **5** (familles indépendantes A/E/D convergent sur les limites de champ) ; ⚔ guerre cognitive **1** (aucune opération coordonnée établie) ; 🌐 réseau **6** (canal X-ENSAE-Trésor-Insee documenté) ; ⏰ temporel **4** (calendrier de révisions en fenêtre mai-juin, seuil SMIC 2 %).
- **Observations nommées** : chaque score renvoie aux sources listées dans la CARTE DES PREUVES ; aucun score n'établit d'intention.
- **Patterns chargés** : @PAT[ICEBERG], @PAT[MONEY], @PAT[NET], @PAT[TEMP] ; **Threats** : @THR[REG_CAPTURE] (indicatif, non conclu), @THR[NUDGE] (légal), @THR[MYTHO] (aucun conflit bio/registre trouvé).
- **RHETORICAL** : NUM 5 (abus de moyennes macro pour parler du coût de la vie — SRC-013) ; DEM 1 ; BF 2 ; AUTH 3 ; FAC 2.
- **COMPLEXITY** : 17 → APEX. **Clusters chargés** : ICEBERG, MONEY, FRAMING, POWER, RESISTANCE, CONFIRMATION, FRAGMENTATION, NETWORK, TEMPORAL.
- **Implicites** : l'assertion porteuse (ne reflète pas la réalité) traitée comme lead auditée, jamais comme prémisse. **Speaker** : utilisateur visant un « debunk sous toutes les coutures » — symétrie de scrutation maintenue.
- **Hypothèses de travail** : explication innocente (conventions internationales) vs explication critique (choix servant les indexeurs) — les deux coexistent, voir PRISME DIALECTIQUE.

## 3. CLUSTERS

- **ICEBERG (Ξ=6)** — Omisson sélective : le champ de l'IPC exclut le logement des propriétaires (méthode « too narrow » selon le manuel Eurostat — SRC-021) ; la série pauvreté porte sur la France métropolitaine avec personnes de référence non étudiantes et trois ruptures de série (SRC-010) ; l'IPC « France » exclut Mayotte (SRC-001). Reconstruction bornée : indices catégoriels publiés par l'Insee (locataires/propriétaires — SRC-020) ; facteur iceberg chiffré global : **NOT COMPUTABLE** (unités non comparables).
- **MONEY (€=7)** — Flux : programme 220 (472,5 M€ AE 2025, -2,7 % — SRC-017) ; indexations légales SMIC/IRL/ILAT/pensions/OATi (FCT-004, FCT-006, SRC-024) ; bénéficiaires des choix de champ non chiffrables au run (GAP d'accès, CAU-002). Lien bénéfice→intention : **non établi**.
- **FRAMING (Λ=5)** — Le débat public confond IPC et coût de la vie ; l'Insee fournit un simulateur d'« indice personnalisé » (SRC-013) ; le resserrement du cadre (consommation vs coût de vivre) échappe à la médiatisation. Origine : convention statistique, pas operation de communication démontrée.
- **POWER (↕=6)** — Asymétries : nomination DG par décret en Conseil des ministres (art. 13 Constitution — SRC-003, FCT-002) ; l'ASP contrôle mais n'a qu'un pouvoir d'avis (SRC-025) ; le budget dépend du vote de loi (SRC-017). Contrepoids : loi 1951 art. 1 (FCT-007), Eurostat/ESS (SRC-003), audit annuel (SRC-027).
- **RESISTANCE (ρ=5)** — UFC-Que Choisir publie ses propres relevés (SRC-011) ; Geerolf documente l'isolation internationale et l'hybridité santé (SRC-021) ; Rexecode/OFCE traquent les révisions (SRC-015, SRC-016) ; colloques ASP/CNIS/Académie 2026 sur la fragilisation internationale (SRC-027). Vulnérabilité de ces contre-pouvoirs : dépendance aux données publiées par l'objet critiqué.
- **CONFIRMATION (κ=4)** — Architecture d'indexation : l'IRL exclut les loyers (FCT-004), le SMIC utilise l'IPC des 20 % les plus modestes avec seuil 2 % (FCT-006) — choix légaux aux effets distributionnels, sans preuve d'intention manipulatoire.
- **FRAGMENTATION (⫸=5)** — Convergence de familles indépendantes (A officiel, E académique, D presse, C consommateurs) sur l'écart mesure/ressenti ; convergence ≠ preuve d'orchestration.
- **NETWORK (🌐=6)** — Voir RÉSEAU D'ACTEURS : canal de formation et circulation documenté, aucune preuve d'influence coordonnée.
- **TEMPORAL (⏰=4)** — Révisions en mai-juin (SRC-016), changements de base 2015/2020/2025, seuil automatique SMIC 2 %. Aucune synchronisation suspecte démontrée.

## 4. HERMÉNEUTIQUE

- **L1 explicite** : l'Insee mesure l'inflation par l'IPC sur la consommation des ménages ; l'écart avec la perception est reconnu (« bases objectives » — FCT-001) ; le DG est nommé en Conseil des ministres (SRC-003).
- **L2 implicite** : l'usage légal de l'IPC comme indexeur universel suppose qu'une moyenne macroéconomique soit équitable pour tous les ménages — supposition contredite par la dispersion des paniers (SRC-013).
- **L3 structurel** : le cadre « consommation » découple l'indice du coût du logement propriétaire et des actifs ; l'institution rend des comptes à l'exécutif qui la finance et la nomme, à l'intérieur de garde-fous légaux.
- **L4 symbolique** : le chiffre « Insee » fonctionne comme marque d'objectivité (Σ=3) ; la défiance populaire (écart à 20-25 % estimés — FCT-001) est l'expression symbolique inverse.
- **L5 présupposé** : que la statistique publique puisse être à la fois instrument de gouvernement et preuve neutre — tension théorisée par Desrosières (« penser en même temps que les objets existent et que c'est une convention » — SRC-014).
- **L6 épistémique** : l'Insee produit, retient et contrôle l'accès aux données micro ; les chercheurs y accèdent sous conditions ; le public ne voit que des agrégats ; les contre-pouvoirs s'appuient sur des données partielles. Faits séparés des inférences : les L1 sont sourcés (FCT), les L2-L6 sont des inférences étiquetées comme telles.

## 5. FORENSIC REASONING

**Montré** : écart OPI/IPC ~6 points reconnu (FCT-001) ; exclusion des loyers imputés et isolation internationale (FCT-005) ; dépendance formelle nomination/budget (FCT-002, SRC-017) ; révisions massives (FCT-003) ; indexations légales et formule IRL (FCT-004, FCT-006).
**Omèté par le corpus dominant** : l'impact budgetaire des choix de champ (non chiffré au run — CAU-002) ; l'invisibilité médiatique de l'hybridité santé (SRC-021).
**Reconstruction bornée** : si l'on incluait les loyers imputés (~21 % de poids comme en Allemagne — SRC-021), l'IPC indexerait davantage vers le coût du logement ; la direction de l'effet dépend toutefois des cycles immobiliers (SRC-020 : loyers +1,9 %/an vs IPC 1,4 % sur 1998-2018 ; BdF : impact ±0,3-0,4 pt selon méthode — SRC-014).
**Status** : reconstruction ESTIMATED, jamais substituée aux faits ; aucune preuve de dissimulation intentionnelle.

## 6. PRISME DIALECTIQUE

- **P1 dominant (⟐/🎓)** : l'Insee est audité (Eurostat, ASP, code ESS), ses méthodes sont documentées, ses choix suivent des conventions européennes et des contraintes de mesure réelles ; les indices catégoriels montrent des écarts limités (SRC-020) ; l'indépendance professionnelle est inscrite dans la loi (FCT-007).
- **P2 critique (⟐̅/🔥)** : la dépendance structurelle (nomination, budget, recrutement) produit des choix de champ alignés sur les intérêts des payeurs d'indexations ; l'isolation internationale du champ logement et l'hybridité santé ne s'expliquent pas intégralement par la théorie des indices (SRC-021) ; les pressions gouvernementales sur la statistique publique sont documentées historiquement (SRC-005) ; les révisions initiales nourrissent un récit public faussé au moment où il compte (FCT-003, SRC-015).
- **P3 arbitrage par la preuve** : les faits ✦/✧ confirment l'écart mesure/ressenti (FCT-001), l'exclusion des loyers imputés et son isolation (FCT-005), la dépendance formelle (FCT-002), les révisions massives (FCT-003) ; ils ne confirment **ni** une manipulation délibérée **ni** l'inoffensivité des choix : les contradictions CON-002 à CON-004 restent ouvertes avec leurs deux termes.

## 7. CHRONOLOGIE

- **1833** : statistique publique continue débutée (SRC-007).
- **1941-1944** : SNS sous Vichy ; **1946 (27 avril)** : création de l'Insee par la loi de finances (SRC-007) ; Closon premier DG (1946-1961).
- **1951 (7 juin)** : loi sur l'obligation, la coordination et le secret statistiques — socle toujours en vigueur (FCT-007).
- **1974-1987** : Malinvaud DG ; institutionnalisation CNIS (années 1970-1980 — SRC-007).
- **1992-2003** : Champsaur DG (X63-ENSAE, ex-Prévision — SRC-006) ; **1996** : IPCH européen ; critères de Maastricht structurant les comptes (SRC-004).
- **2003-2007** : Charpin DG ; gratuité de la diffusion (SRC-007). **2003-2008** : Champsaur président de l'ARCEP (revolving door — SRC-006).
- **2004 (26 juin)** : loi statistique : liste annuelle des enquêtes par arrêté ministériel (SRC-025). **2008** : création de l'ASP (loi LME — SRC-003). **2009** : réglement européen 223/2009 ; Le Grand truquage documente des pressions gouvernementales sur la statistique (SRC-005).
- **2012-2025** : Tavernier DG (X-ENSAE, ex-Prévision, Acoss, cabinet ministériel — SRC-023, SRC-018) ; **2020-2022** : épisode inflation, débat ressenti/mesuré.
- **2023 (janvier)** : première estimation croissance 2023 = 0,9 % (SRC-022). **2024** : passage base 2020. **2025 (mai-juin)** : révisions +0,5 pt sur 2023 (SRC-016) ; **juin 2025** : Lenglart DG (FCT-002). **2026 (juin)** : compte définitif 2023 = 1,9 % (FCT-003).
- **2025 (1er décembre)** : fusion des corps administrateur Insee/ISED → corps ISED commun Insee-Trésor-SSM (SRC-026).
- **2026** : IPC passe en base 2025 (séries 2015 arrêtées — SRC-002) ; taux de pauvreté 15,4 %, plus haut mesuré (FCT-009) ; colloques internationaux sur la fragilisation politique des statistiques (SRC-027).

## 8. DOMAINES

- **Juridique** : art. 1 loi 1951 — indépendance professionnelle garantie, ASP de neuf membres (FCT-007) ; art. 13 Constitution — nomination du DG en Conseil des ministres (FCT-002) ; liste des enquêtes arrêtée par le ministre (SRC-025) ; règlement européen 223/2009 applicable (SRC-003). Verdict : indépendance **professionnelle** garantie, indépendance **institutionnelle** non garantie.
- **Technique/statistique** : IPC = panier fixe, pondérations macro, exclusion des loyers imputés, inclusion santé remboursée (FCT-005, SRC-020) ; changements de base réguliers (2015→2025 — SRC-002) ; révisions par vagues (SRC-015, SRC-016). Biais documentés : champ, hybridité, révisions ; les indices catégoriels limitent l'ampleur inter-groupe (SRC-020).
- **Psychologique (perception)** : écart OPI/IPC ~6 points depuis 2004 ; surpondération des prix en hausse et à forte fréquence d'achat (FCT-001) ; l'écart n'est pas de la simple irrationalité (« bases objectives »).
- **Anthropologique** : les nombres gouvernent (Desrosières — SRC-014) ; la statistique produit des « êtres conventionnels » (chômeurs, pauvres) qui font l'objet de luttes ; l'usage public d'un indice techniques le transforme en norme sociale (CON-001).
- **Politique** : dépendance formelle à l'exécutif (FCT-002, SRC-017) ; pressions documentées historiquement (SRC-005) ; cas Insee spécifique non établi au niveau micro (CON-004) ; colloques 2026 sur la fragilisation internationale (SRC-027).
- **Économique** : indexations massives via IPC (FCT-006, CAU-002) ; programme 220 en baisse (SRC-017) ; l'écart inflation « mesurée vs subie » frappe davantage les modestes en 2022-2023 (SRC-026-w) — contre-exemple 2025 (SRC-001-w) : l'effet de composition n'est pas constant.
- **Social** : SMIC, IRL, pensions adossés à la mesure officielle (FCT-004, FCT-006) ; pauvreté 9,8 M (FCT-009) ; seuil relatif = mesure d'inégalité (60 % de la médiane — SRC-010) ; 40 % de seuil = 2,8 M de pauvres, 70 % = 14,6 M (SRC-010).
- **Éthique** : choix de champ = choix distributifs ; l'institution ne documente pas publiquement l'impact distributif de ses conventions (silence L6) ; transparence méthodologique réelle mais asymétrique (complexité).
- **Narratif** : « l'inflation officielle sous-estime la réalité » vs « l'IPC n'est pas un coût de la vie » : les deux récits coexistent ; le second est officiel, le premier dominant dans l'opinion (FCT-001, CON-001).
- **Scientifique** : débat académique documenté (Geerolf — SRC-021) ; le manuel international ne recommande pas l'exclusion (5 méthodes neutres) ; Eurostat qualifie l'exclusion de « too narrow » ; l'Insee publie ses propres réponses (SRC-020).
- **Communication** : publications pédagogiques (« L'essentiel sur… l'inflation » — SRC-001), simulateur d'indice personnalisé (SRC-013) ; la médiation ne corrige que partiellement le cadrage médiatique.
- **Organisationnel** : corps ISED fusionné (SRC-026) ; directions régionales, réseau d'enquêteurs (SRC-007) ; inspection générale de l'Insee analyse la réorganisation des écoles (2026 — SRC-026-w).

## 9. RÉSEAU D'ACTEURS

**Nœuds et arêtes documentés** (tous typés et sourcés, voir ACTOR_NETWORK_MAP runtime) : École polytechnique → direction Insee (Lenglart X1989, Tavernier, Champsaur X1963 — FCT-008, SRC-006) ; ENSAE → corps statistique (fusion ISED 2025 — SRC-026) ; ministère de l'Économie (Prévision/Trésor) → direction Insee (Champsaur, Cotis, Lenglart — SRC-006, SRC-008, SRC-019) ; direction Insee → régulation (Champsaur → ARCEP 2003-2008 — SRC-006) ; DREES → Insee (Lenglart — SRC-019) ; ASP → contrôle annuel du DG (SRC-025, SRC-027) ; Eurostat/ESS → normes et audits (SRC-003) ; CNIL → contrôle des répertoires (SRC-007).
**Carte des contrôles** : ASP (avis, audition — SRC-025), Eurostat (règlement, peer reviews — SRC-003), CNIL (traitements — SRC-007), contre-pouvoirs externes (UFC, académiques — SRC-011, SRC-021). Limites de contrôle : pouvoir d'avis de l'ASP, contenu intégral des rapports non inspecté (CTRL-001, GAP d'accès).
**Métrique de centralité** : NOT COMPUTABLE (graphe non exhaustif) ; homophilie documentée ≠ coordination (invariant KERNEL).

## 10. CHAÎNES / PELOTE

**Arbre CAU-1 (mécanisme principal — SUPPORTED)** : champ de l'IPC (exclusion loyers imputés, inclusion santé remboursée, pondérations macro) → [CAUSE] → mesure d'inflation inférieure au coût de la vie ressenti pour des pans de ménages (écart OPI/IPC ~6 points — FCT-001, FCT-005). Sources : SRC-020, SRC-021, SRC-018, SRC-014.
**Arbre CAU-2 (indexation — SUPPORTED avec GAP)** : usage légal de l'IPC (SMIC, IRL, pensions, OATi, contrats) → [CAUSE] → chaque dixième de point d'IPC se traduit en flux financiers légaux ; l'IRL exclut même les loyers de son calcul (FCT-004, FCT-006). GAP : amplitude exacte en Md€ (GAP_TYPE=ACCESS, CAU-002).
**Arbre CAU-3 (dépendance — SUPPORTED)** : tutelle ministérielle + nomination en Conseil des ministres + budget loi de finances → [ENABLER] → dépendance institutionnelle formelle, tempérée par loi 1951/ASP (FCT-002, FCT-007, SRC-017).
**Arbre CAU-4 (recrutement — CONTEXT avec GAP)** : canal X-ENSAE-Trésor-DREES → [CONTEXT] → homophilie technocratique documentée (FCT-008) ; **lien vers les choix méthodologiques NON démontré** (GAP_TYPE=CAUSALITY — CAU-004). Contre-explication : compétence et vivier professionnels (P1).
**Arbre CAU-5 (révisions — SUPPORTED)** : sources partielles + contexte inflationniste + changements de base → [CAUSE] → premières estimations trompeuses (2023 : 0,9 → 1,9 % — FCT-003, SRC-016).
**Arbre CAU-6 (contrainte européenne — CONTEXT)** : critères de Maastricht, SEC, IPCH → [CONTEXT] → priorisation déficit/inflation au détriment d'autres dimensions (SRC-004).
**Couverture** : 6 arbres ; 2 gaps typés (CAU-002 ACCESS, CAU-004 CAUSALITY) ; aucune chaine longue inventée ; provenance ≠ causalité respecté.

## 11. CARTE DES PREUVES

**Couverture des leads (15/15 SATURATED)** : LED-001 (assertion porteuse : auditée, verdict au RÉSUMÉ) ; LED-002/003/004 (biais IPC, ressenti, bases) ; LED-005/006/009 (gouvernance, pantouflage, sociologie) ; LED-007/013 (indexations, effets) ; LED-008 (révisions) ; LED-010 (pauvreté) ; LED-011/014 (gouvernementalité, histoire) ; LED-012 (international) ; LED-015 (pressions). **Couverture objet (12/12 axes terminalisés SATURATED)** : méthodes IPC (AXS-001), ressenti (AXS-002), gouvernance (AXS-003), endogamie (AXS-004), indépendance (AXS-005), révisions (AXS-006), moyens (AXS-007), indexations (AXS-008), pressions (AXS-009), pauvreté (AXS-010), international (AXS-011), gouvernementalité (AXS-012) — chaque axe porte ses tentatives (QRY) et résultats (FCT/SRC/CAU) dans le registre machine.
**Régime des faits (9)** : FCT-001 ✦ (OPI/IPC 6 pts, familles A+C+D) ; FCT-002 ✧ (nomination DG, A) ; FCT-003 ✦ (révision PIB 2023, A+D+E) ; FCT-004 ✧ (formule IRL, A+C) ; FCT-005 ✦ (loyers imputés exclus/isolation/hybride, A+E) ; FCT-006 ✧ (SMIC indexé 20 % modestes, A) ; FCT-007 ✧ (loi 1951/ASP, A) ; FCT-008 ✧ (circulation Lenglart, A) ; FCT-009 ✧ (pauvreté 9 817 000, A). Détail complet dans le registre machine des faits et sa carte de sources (rendus automatiquement en annexe).
**Réfutations adversariales** : FCT-001 (NONE), FCT-003 (NONE), FCT-005 (NONE) — contre-requêtes exécutées, aucune contre-preuve totale ; contre-preuves partielles intégrées aux libellés ✧ (protection ex post SMIC contestée selon sous-périodes).
**Contradictions (4)** : CON-001 résolue (usage IPC ≠ coût de la vie) ; CON-002/003/004 préservées ouvertes (impact logement, révisions exceptionnelles vs processus normal, garanties vs pressions documentées).
**EDI (diagnostic, pas vérité)** : corpus 28 sources inspectées — 18 famille A (officielle), 3 C, 3 D, 3 E, 1 other:asm ; EDI 0,65 (raw 0,746, pénalité 0,10 concentration famille A 64 %) ; COV 1,0 ; EDI* 0,66 ; cible APEX 0,80 non atteinte (écart routé, voir PÉRIMÈTRE) ; perspectives 4/5 ; couverture des claims décisifs : 8/8 avec objets directs, compteurs FOUND (6) ou NONE_FOUND (2), freshness CURRENT.

## 12. CARTE DIALECTIQUE

- **Scénario A (convention défendable)** : les choix de l'Insee suivent les normes européennes et des contraintes de mesure réelles ; l'indépendance est légalement encadrée et auditée ; les révisions sont le prix honnête de l'estimation rapide. Falsificateur : preuve d'un choix de champ contraire aux normes ET aux intérêts des payeurs.
- **Scénario B (alignement d'intérêts)** : la dépendance structurelle (nomination, budget, recrutement) aligne durablement les conventions de mesure sur les intérêts de l'État payeur d'indexations ; l'isolation du champ logement et l'hybridité santé sont des choix politiques masqués en choix techniques (SRC-021). Falsificateur : preuve documentée d'instruction politique sur un choix méthodologique précis de l'Insee.
- **Convergences** : l'écart mesure/ressenti (toutes familles) ; la dépendance formelle (A).
- **Divergences** : l'ampleur de l'effet logement (SRC-020 limité vs SRC-021 significatif cumulé) ; l'interprétation des révisions (processus vs récit trompeur).
- **Non résolu** : intention (aucun ACT avec intent PROVEN hors cadre légal) ; chiffrage budgétaire (ACCESS).
- **Silences partagés** : archives internes ; impact distributif exact des conventions ; vie interne du corps statistique.
- **Impact et responsabilité** : bénéfices (mesure comparable internationalement, indexation prévisible, pédagogie) ; coûts/harms (défiance structurelle FCT-001, effets de seuil pauvreté SRC-010, révisions récit-fragilisantes FCT-003) ; affectés (salariés au SMIC, locataires/propriétaires, pensionnaires, chercheurs, décideurs) ; réponse/changement (indices catégoriels SRC-020, simulateur SRC-013, débat académique SRC-021, colloques SRC-027). Responsabilité : ACT-001 législateur (intent PROVEN — cadre légal) ; ACT-002 gouvernement (intent UNKNOWN — nomination, budget) ; ACT-003 direction Insee (intent UNKNOWN — choix méthodologiques documentés). Aucune personne nominativement responsable : les carrières documentées (Champsaur, Cotis, Tavernier, Lenglart) établissent un canal de recrutement, pas une faute — ASSOCIATION ≠ COORDINATION, BENEFIT ≠ INTENT.

## 13. PÉRIMÈTRE & LIMITES

**Inclus** : 1946-2026 (focus 2004-2026) ; France (métropole+Outre-mer) ; 12 axes méthodes/gouvernance/effets ; 28 sources inspectées de 5 familles.
**Exclusions (explicites)** : théories conspirationnistes sans appui documenté ; politisation partisane des critiques ; sujets périphériques (démographie fine, prix immobiliers détaillés).
**Limites d'accès (GAP_TYPE=ACCESS)** : rapport ASP intégral (PDF non extractible — SRC-005a) ; peer review Eurostat France (HAL bloqué anti-bot — SRC-029a) ; paywall La Tribune (SRC-012a) ; archives internes Insee ; chiffrage budgétaire des indexations.
**Limites de méthode** : HEAP/EDI cible APEX non atteinte (concentration famille A structurelle pour un objet étatique — pénalité documentée) ; GAP_SEVERITY = 0,30×(0,80-0,65)×1,00 ≈ 0,045 → < 0,20 : poursuite avec divulgation ; homophilie ≠ influence (CAU-004) ; périmètres exacts des champs IPC/ERFS par sous-poste (SCOPE).
**GAP_SEVERITY** : composantes {edi_gap 0,15, coverage_gap 0,0} → 0,045 — procéder avec divulgation.

## 14. ÉTAT DES CONNAISSANCES

- **Connus (✦)** : écart OPI/IPC ~6 points et reconnaissance officielle (FCT-001) ; révision PIB 2023 de 0,9 % à 1,9 % (FCT-003) ; exclusion des loyers imputés de l'IPC, isolation internationale, hybridité santé (FCT-005).
- **Probables (✧)** : mécanique de nomination du DG (FCT-002) ; formule IRL hors loyers (FCT-004) ; indexation SMIC sur IPC des 20 % modestes avec adéquation ex post contestée (FCT-006) ; garanties légales d'indépendance (FCT-007) ; circulation des cadres (FCT-008) ; pauvreté 9 817 000 (FCT-009).
- **Claimés (⁕)** : « la France n'a pas poussé à l'inclusion du logement dans l'IPCH » (SRC-021, hypothèse de l'auteur).
- **Hypothèses (⁂)** : alignement d'intérêts entre conventions de champ et payeurs d'indexations (Scénario B) — non falsifiable au run.
- **Contestés (⊗/⊙)** : ampleur de l'effet logement (CON-002, ⊙) ; caractère exceptionnel vs normal des révisions (CON-003, ⊙) ; effectivité de l'indépendance (CON-004, ⊙).
- **Inconnus (⁅)** : amplitude budgétaire des indexations ; contenu intégral des audits ; pressions Insee-spécifiques documentées.
- **Réfutés (❧)** : aucun fait du registre ; réfutée en revanche la lecture « l'IPC prétend mesurer le coût de la vie » (CON-001, portée à l'usage médiatique, pas à l'institution).

## 15. SUSPICION / VÉRIFICATION

**Audits de sources** : 28 sources inspectées (FETCH observé chacune) ; rôles : 19 ◈, 8 ◉, 1 ○ ; familles dérivées du registre : A=18, C=3, D=3, E=3, other:asm=1 ; aucune circularité inter-familles ; Légifrance et Service-Public comptés comme une seule famille (même éditeur DILA).
**STATUS_DELTA** : aucun downgrade/upgrade en phase 13 ; FCT-006 maintenu ✧ avec contre-preuve intégrée au libellé (protection ex post contestée).
**Vérifications non résolues** : rapport ASP intégral (ACCESS) ; peer review Eurostat (ACCESS) ; chiffrage budgétaire (ACCESS) ; lien individuel homophilie→méthode (CAUSALITY).
**Checks suivants recommandés** : rapports Cour des comptes sur l'indexation ; HICP augmenté OOH d'Eurostat (2024-2026) ; sociologie interne du corps (baromètres, grèves 2022-2023) ; suivi des révisions futures 2024-2026.

---

**Clôture** : le sujet « l'Insee ne reflète pas la réalité » se transforme en question soluble : **quelle réalité l'Insee choisit-elle de refléter, par quelle convention, au bénéfice de quels flux, sous quels contrôles ?** La réponse documentée : une convention de consommation, enchâssée dans l'exécutif, auditée formellement, contestée scientifiquement, aux effets légaux massifs — sans qu'aucun fait n'établisse de manipulation délibérée au niveau micro. C'est la fresque demandée : ni blanc-seing, ni complot — un appareil de pouvoir statistique, documenté chiffre par chiffre.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:15|CLM:8|AXS:12|CAU:6|CTRL:4|ACT:3

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"excerpt":"L'INSEE ne reflete pas la réalité. fait une fresque de l'INSEE, qui bosse dedans, les biographies, les relations, la politique.","kind":"CLAIM","lead":"Assertion utilisateur: L'INSEE ne reflète pas la réalité (a débunker sous toutes les coutures)","materiality":"DECISIVE","routes":["AUDIT","LINK"],"source_ref":"INPUT:2026-09-20_17-04_INPUT.txt","status":"SATURATED"}
LED-002 | {"kind":"MECHANISM","lead":"Biais méthodologiques allégués de l'IPC (méthodes de calcul, pondérations, périmètres)","materiality":"DECISIVE","routes":["EXPAND","LINK"],"status":"SATURATED"}
LED-003 | {"kind":"MECHANISM","lead":"Écart allégué entre inflation mesurée et inflation ressentie (sous-estimation perçue)","materiality":"DECISIVE","routes":["EXPAND","LINK"],"status":"SATURATED"}
LED-004 | {"kind":"EVENT","lead":"Changements de base de l'IPC (1970, 1980, 1990, 1998, 2015) et continuité des séries","materiality":"IMPORTANT","routes":["EXPAND"],"status":"SATURATED"}
LED-005 | {"kind":"ENTITY","lead":"Gouvernance et direction de l'Insee: DG nommé en Conseil des ministres sur proposition de Bercy, rattachement ministériel économique; DG actuel Fabrice Lenglart (depuis juin 2025); précédents: Tavernier 2012-2025, Cotis 2007-2012, Charpin 2003-2007, Champsaur 1992-2003, Milleron, Malinvaud, Ripert, Gruson, Closon","materiality":"DECISIVE","routes":["EXPAND","LINK"],"status":"SATURATED"}
LED-006 | {"kind":"RELATION","lead":"Circulation des cadres: ENSAE/Polytechnique, INSEE-ministères-pantouflage (endogamie technocratique)","materiality":"DECISIVE","routes":["EXPAND","LINK"],"status":"SATURATED"}
LED-007 | {"kind":"CONTEXT","lead":"Indexations légales adossées à l'IPC: SMIC, loyers (IRL/ILAT), retraites, obligations indexées","materiality":"DECISIVE","routes":["LINK"],"status":"SATURATED"}
LED-008 | {"kind":"EVENT","lead":"Calendrier de publication, révisions des séries et usages politiques (fenêtres de sortie)","materiality":"IMPORTANT","routes":["EXPAND"],"status":"SATURATED"}
LED-009 | {"kind":"CLAIM","lead":"Sociologie du corps statistique: recrutement grande école, insee-istes, culture commune","materiality":"IMPORTANT","routes":["EXPAND","LINK"],"status":"SATURATED"}
LED-010 | {"kind":"CLAIM","lead":"Mesure de la pauvreté et des inégalités: seuil relatif 60% de la médiane, évolutions contestées","materiality":"DECISIVE","routes":["EXPAND","LINK"],"status":"SATURATED"}
LED-011 | {"kind":"MECHANISM","lead":"Pouvoir statistique et gouvernementalité: les nombres comme instruments de gouvernement (Desrosières, Foucault)","materiality":"IMPORTANT","routes":["EXPAND"],"status":"SATURATED"}
LED-012 | {"kind":"CONTEXT","lead":"Comparaison internationale: ONS, Destatis, Eurostat, HICP vs IPC — biais structurels partagés","materiality":"IMPORTANT","routes":["EXPAND"],"status":"SATURATED"}
LED-013 | {"kind":"MECHANISM","lead":"Effets concrets des choix méthodologiques: budgets, revalorisations, contrats, perceptions publiques","materiality":"DECISIVE","routes":["LINK","EXPAND"],"status":"SATURATED"}
LED-014 | {"kind":"EVENT","lead":"Histoire institutionnelle: SNS 1941 (Vichy), INSEE 1946, dirigisme, planification, culture métier","materiality":"IMPORTANT","routes":["EXPAND"],"status":"SATURATED"}
LED-015 | {"kind":"EVENT","lead":"Pressions politiques documentées sur la statistique publique (cas concrets, France + UE)","materiality":"DECISIVE","routes":["AUDIT","EXPAND"],"status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"La méthodologie de l'IPC peut sous-estimer l'inflation ressentie (échantillonage, logements, panel, coût du logement hors taxes)","counter":["SRC-013","SRC-025-est-non"],"gap_type":null,"status":"SUPPORTED","support":["SRC-020","SRC-021","SRC-012"]}
CLM-002 | {"claim":"L'INSEE est structurellement dépendante du pouvoir politique: tutelle ministérielle, nominations DG par décret, budget","counter":["SRC-025","SRC-027"],"gap_type":null,"status":"SUPPORTED","support":["SRC-019","SRC-003","SRC-021"]}
CLM-003 | {"claim":"La statistique publique française est hautement standardisée et auditée (Eurostat, ASP, code de bonne conduite ESS)","counter":[],"gap_type":null,"status":"SUPPORTED","support":["SRC-003","SRC-025","SRC-027"]}
CLM-004 | {"claim":"Le recrutement X-ENSAE-ParisTech et la circulation INSEE-ministères créent une homophilie technocratique influençant les priorités","counter":[],"gap_type":null,"status":"SUPPORTED","support":["SRC-006","SRC-008","SRC-023"]}
CLM-005 | {"claim":"L'IPC indexe massivement des montants publics et privés (SMIC, retraites complémentaires, IRL, obligations OATi, contrats)","counter":[],"gap_type":null,"status":"SUPPORTED","support":["SRC-017","SRC-024"]}
CLM-006 | {"claim":"Les choix de communication et de calendrier de l'INSEE façonnent la perception publique (framing, révisions, attentions médiatiques sélectives)","counter":["SRC-022"],"gap_type":null,"status":"SUPPORTED","support":["SRC-015","SRC-016"]}
CLM-007 | {"claim":"Le seuil de pauvreté relatif (60% de la médiane) transforme la mesure de la pauvreté en mesure d'inégalité","counter":["SRC-005"],"gap_type":null,"status":"SUPPORTED","support":["SRC-010"]}
CLM-008 | {"claim":"L'écart inflation ressentie/mesurée est structurel et documenté (baromètres de perception, paniers hétérogènes, prix du logement)","counter":[],"gap_type":null,"status":"SUPPORTED","support":["SRC-018"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-003"],"gap_type":null,"links":["LED-002","LED-003","LED-004","CLM-001"],"question":"Comment l'IPC est-il calculé et quels biais méthodologiques documentés peut-il comporter (échantillonnage, HomeScan, loyers, imputations, bases) ?","result_ids":[],"sought_objects":["méthodologie IPC INSEE (insee.fr, note méthodo)","critiques académiques/presse","bases IPC et changements"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-002","QRY-003"],"gap_type":null,"links":["LED-003","CLM-008"],"question":"L'écart inflation mesurée/ressentie: quelles causes documentées, quels baromètres, quelles réponses INSEE ?","result_ids":[],"sought_objects":["baromètre Crédoc","débat presse 2022-2023","réponses INSEE/Eurostat"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-005","QRY-011","QRY-015"],"gap_type":null,"links":["LED-005","LED-009","CLM-002"],"question":"Gouvernance: comment sont nommés DG/DS/directions? Quel rattachement? Quels profils biographiques (X-ENSAE, Inspection des finances)?","result_ids":[],"sought_objects":["décrets nominations JO","biographies direction","organigramme"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-011"],"gap_type":null,"links":["LED-006","LED-009","CLM-004"],"question":"Endogamie et pantouflage: quelle circulation documentée entre INSEE, ministères, cabinets, secteur privé? Quels exemples nominatifs sourcés?","result_ids":[],"sought_objects":["CV de cadres","mouvements documentés","études sociologiques"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-006","QRY-008"],"gap_type":null,"links":["LED-005","CLM-002","CLM-003"],"question":"Indépendance juridique: que garantit la loi (1951/2004/2008, ASP/CNIS, Eurostat)? Quelles limites documentées?","result_ids":[],"sought_objects":["textes légaux (legifrance)","ASP avis","peer review Eurostat"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-012","QRY-029"],"gap_type":null,"links":["LED-008","CLM-006"],"question":"Révisions et fiabilité: quels épisodes documentés de révisions majeures (croissance, emploi, déficit), quel impact politique?","result_ids":[],"sought_objects":["révisions comptes nationaux","cas déficit/emploi","presse"],"status":"SATURATED"}
AXS-007 | {"attempt_ids":["QRY-016"],"gap_type":null,"links":["LED-013","CLM-002"],"question":"Moyens: effectifs, budget, évolution — est-ce cohérent avec la mission? Quelles pressions budgétaires documentées?","result_ids":[],"sought_objects":["PLF/RAP INSEE","rapports budget","effectifs"],"status":"SATURATED"}
AXS-008 | {"attempt_ids":["QRY-017","QRY-040","QRY-047"],"gap_type":null,"links":["LED-007","LED-013","CLM-005"],"question":"Indexations: quels montants indexés sur l'IPC/IRL/SMIC? Effets d'un point d'IPC sur les dépenses publiques?","result_ids":["FCT-004","FCT-006","CAU-002"],"sought_objects":["SMIC (DGT/INSEE)","IRL (INSEE)","OATi (AFT)","revalorisations"],"status":"SATURATED"}
AXS-009 | {"attempt_ids":["QRY-007","QRY-010"],"gap_type":null,"links":["LED-015","CLM-002"],"question":"Pressions politiques: quels cas documentés (France, UE) d'interférence avec la statistique publique? Que disent les audits?","result_ids":[],"sought_objects":["cas documentés","avis ASP","Eurostat governance","presse investigation"],"status":"SATURATED"}
AXS-010 | {"attempt_ids":["QRY-021","QRY-023"],"gap_type":null,"links":["LED-010","CLM-007"],"question":"Pauvreté/inégalités: comment l'INSEE mesure, quelles critiques (Maurin, Piketty/World Inequality Lab), quels effets de seuil?","result_ids":["FCT-009"],"sought_objects":["définitions seuil pauvreté","critiques méthodologiques","comparaisons"],"status":"SATURATED"}
AXS-011 | {"attempt_ids":["QRY-009","QRY-018"],"gap_type":null,"links":["LED-012","CLM-001"],"question":"Comparaison internationale: comment ONS/Destatis/gouvernances autres traitent-ils les mêmes problèmes (logement, perception, révisions)?","result_ids":[],"sought_objects":["ONS housing inclusion","Destatis","Eurostat HICP"],"status":"SATURATED"}
AXS-012 | {"attempt_ids":[],"gap_type":null,"links":["LED-011","LED-014"],"question":"Fresque anthropologique/politique: comment le pouvoir statistique s'exerce-t-il (Desrosières, gouvernementalité), quelles implications éthiques?","result_ids":[],"sought_objects":["Desrosières","Foucault","études STS"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"edge_type":"CAUSE","gap_type":null,"mechanism":"Champ de l'IPC (consommation, exclusion loyers imputés, inclusion santé remboursée) et pondérations macroéconomiques","sources":["SRC-020","SRC-021","SRC-018","SRC-014"],"status":"SUPPORTED","target":"Mesure d'inflation systématiquement inférieure au coût de la vie ressenti de certains ménages (écart OPI/IPC ~6 points)"}
CAU-002 | {"edge_type":"CAUSE","gap":"Ampleur budgetaire chiffragee exacte (MdE par 0,1 pt d IPC) non etablie: simulations budgetaires non accessibles au run","gap_type":"ACCESS","mechanism":"Usage de l'IPC comme indexeur légal (SMIC, IRL, ILAT, pensions, contrats, OATi)","sources":["SRC-017","SRC-024","SRC-028","SRC-012"],"status":"SUPPORTED","target":"Chaque dixième de point d'IPC se traduit en milliards d'euros de dépenses publiques et de flux privés; l'IRL exclut même les loyers de son calcul"}
CAU-003 | {"edge_type":"ENABLER","gap_type":null,"mechanism":"Tutelle ministérielle, nomination du DG en Conseil des ministres sur proposition de Bercy, budget via programme 220","sources":["SRC-019","SRC-025","SRC-003","SRC-017","SRC-027"],"status":"SUPPORTED","target":"Dépendance institutionnelle formelle de l'Insee envers l'exécutif, tempérée par la loi 1951 et l'ASP"}
CAU-004 | {"edge_type":"CONTEXT","gap":"Le lien association (homophilie X-ENSAE) vers effet methodologique n est pas etabli au niveau individuel","gap_type":"CAUSALITY","mechanism":"Canal de recrutement X-ENSAE et circulation Insee-Trésor-DREES (Champsaur, Cotis, Tavernier, Lenglart)","sources":["SRC-007","SRC-008","SRC-006","SRC-026","SRC-023"],"status":"SUPPORTED","target":"Homophilie technocratique documentée; influence réelle sur les choix méthodologiques NON démontrée au niveau individuel"}
CAU-005 | {"edge_type":"CAUSE","gap_type":null,"mechanism":"Révisions des comptes nationaux (contexte inflationniste, sources partielles, changements de base)","sources":["SRC-022","SRC-015","SRC-016"],"status":"SUPPORTED","target":"Premières estimations de croissance 2023 sous-évaluées d'environ 1 point; débat public nourri de chiffres provisoires"}
CAU-006 | {"edge_type":"CONTEXT","gap_type":null,"mechanism":"Critères européens (Maastricht, SEC, IPCH) contraignant la production statistique nationale","sources":["SRC-004"],"status":"SUPPORTED","target":"Priorisation des indicateurs déficit/inflation au détriment d'autres dimensions (Courrier des statistiques N11)"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"controller":"Autorité de la statistique publique","documented_action":"audition annuelle du DG Insee; avis publics; rapport au Parlement","fct_src":["SRC-025","SRC-027"],"gap":"CONTENU intégral des rapports ASP non inspecté (GAP_TYPE=ACCESS)","information":"rapports annuels, auditions","oversight_outcome":"rapport annuel publié (existence documentée; contenu intégral non inspecté)","rule":"art.1 loi 1951 (v.2010) + décret 2009-250 modifié"}
CTRL-002 | {"controller":"Eurostat / ESS","documented_action":"encadrement normatif; diffusion du principe 1 (indépendance)","fct_src":["SRC-003"],"gap":"Rapport peer review France complet non inspecté (GAP_TYPE=ACCESS)","information":"peer reviews, conformité déclarée","oversight_outcome":"conformité française déclarée (SRC-003)","rule":"règlement (CE) 223/2009, code de bonnes pratiques ESS"}
CTRL-003 | {"controller":"CNIL","documented_action":"autorisations et contrôles des traitements","fct_src":["SRC-007"],"gap":"détails des contrôles récents (GAP_TYPE=ACCESS)","information":"répertoires (RNIPP, Résil, Sirene)","oversight_outcome":"documenté dans la chronologie officielle","rule":"loi informatique et libertés"}
CTRL-004 | {"controller":"Contre-pouvoirs externes (consommateurs, économistes, presse)","documented_action":"production d'indices et analyses alternatifs; débats publics","fct_src":["SRC-011","SRC-021","SRC-015","SRC-016"],"gap":"portée réelle des correctifs sur la décision publique (GAP_TYPE=CAUSALITY)","information":"relevés alternatifs (UFC), analyses (Geerolf, Rexecode/OFCE)","oversight_outcome":"correction publique partielle (framing coût de la vie)","rule":"débat public, publications"}

### ACTION_REGISTRY_V1
ACT-001 | {"documented_action":"loi 1951 art.1 (indépendance professionnelle); loi 2008 création ASP","intent":"PROVEN","name":"Législateur français","responsibility_scope":"cadre légal uniquement","role":"cadre légal de la statistique publique","source":"SRC-025"}
ACT-002 | {"documented_action":"proposition de nomination du DG (Lenglart 2025); pilotage du programme 220 (AE -2,7% 2025)","intent":"UNKNOWN","name":"Gouvernement / ministère de l'Économie","responsibility_scope":"décisions institutionnelles documentées; aucune conclusion d'intention sur les méthodes","role":"tutelle, nomination, budget","source":"SRC-019; SRC-017"}
ACT-003 | {"documented_action":"définition du champ de l'IPC (hors loyers imputés, santé remboursée incluse), méthodes, calendriers, révisions","intent":"UNKNOWN","name":"Direction de l'Insee","responsibility_scope":"choix méthodologiques documentés; aucune faute établie au niveau individuel","role":"producteur des statistiques publiques","source":"SRC-020; SRC-021; SRC-022"}

SEARCH_ACTIVITY_V1:WEB:19|FETCH:28|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND_TANGENTIAL_NO_FP_MATCH | mnemolite-mcp-curl-8002 | http://localhost:8002/mcp | @MNEMO_Q search_memory('INSEE biais inflation méthodes calcul statistiques publiques', hybrid, limit5, tags=[project:truth-engine]) — hits: 268168bc(snapshot triche-electorale), 1f718c6b(Insee Premiere 2055 DMA), ad7c53e5(decheteries) — aucun snapshot:v1 subject-fp:65f5d8ab
SYS-003 | SYS | REPAIR | run_state | QRY-029 | QRY-029 texte enregistré en paraphrase; texte réellement exécuté re-journalisé sous QRY-041; QRY-029 conservé comme ligne historique
SYS-004 | SYS | NONE | mnemolite-mcp-curl-8002 | sys_log:MNEMO_Q canonical row | MNEMO_Q
SYS-005 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | AXS-001/LED-002,LED-004 — INSEE indice des prix à la consommation base 2015 méthodologie insee.fr
QRY-002 | WEB | FOUND | - | - | AXS-002/LED-003,CLM-008 — inflation ressentie supérieure inflation mesurée Crédoc baromètre 2022 2023 INSEE explication
QRY-003 | FETCH | FOUND | SRC-001 | https://www.insee.fr/fr/statistiques/4268033 | FETCH L essentiel sur l inflation (Insee 4268033)
QRY-004 | FETCH | FOUND | SRC-002 | https://www.insee.fr/fr/statistiques/serie/001763852 | FETCH série IPC base 2015 ensemble des ménages (séries arrêtées)
QRY-005 | WEB | FOUND | - | - | AXS-003/LED-005,LED-009,CLM-002 — directeur général de l'Insee biographie nomination décret Tavernier Birot X-ENSAE
QRY-006 | WEB | FOUND | - | - | AXS-005/LED-005,CLM-002,CLM-003 — loi 26 juin 2004 indépendance statistique publique autorité statistique ESS Eurostat France
QRY-007 | WEB | FOUND | - | - | AXS-009/LED-015,CLM-002 — pression politique statistiques publiques France Insee gouvernement cas documenté chômage déficit
QRY-008 | FETCH | FOUND | SRC-003 | https://www.insee.fr/fr/information/4174951 | FETCH Principe 1 ESS indépendance professionnelle (Insee)
QRY-009 | FETCH | FOUND | SRC-004 | https://www.insee.fr/fr/information/8203034?sommaire=8203072 | FETCH Courrier des statistiques N11 — statistiques publiques et débat démocratique 1988-2016
QRY-010 | FETCH | FOUND | SRC-005 | https://laviedesidees.fr/Les-statistiques-un-service-public | FETCH recension Le grand truquage (L. Data 2009) — La Vie des idées
QRY-011 | WEB | FOUND | - | - | AXS-003/AXS-004/LED-005,LED-006 — Paul Champsaur ARCEP Jean-Philippe Cotis ancien directeur général Insee parcours
QRY-012 | WEB | FOUND | - | - | AXS-006/LED-008 — Insee révision croissance 2020 première estimation PIB comptes nationaux base 2020
QRY-013 | FETCH | FOUND | SRC-006 | https://www.insee.fr/fr/information/2014679 | FETCH biographie Paul Champsaur (Insee)
QRY-014 | FETCH | FOUND | SRC-007 | https://www.insee.fr/fr/information/1300622 | FETCH Un peu d histoire — chronologie officielle Insee 80 ans, liste des DG
QRY-015 | WEB | FOUND | - | - | AXS-003/LED-005 — Fabrice Lenglart directeur général Insee nomination 2025 parcours
QRY-016 | WEB | FOUND | - | - | AXS-007/LED-013,CLM-002 — Insee effectifs agents baisse budget 2023 2024 2025 mission économie
QRY-017 | FETCH | FOUND | SRC-008 | https://www.insee.fr/fr/information/8603402 | FETCH biographie officielle Fabrice Lenglart DG Insee
QRY-018 | FETCH | FOUND | SRC-009 | https://www.senat.fr/rap/l24-144-312/l24-144-3123.html | FETCH Sénat PLF 2025 — programme 220 Statistiques et études économiques
QRY-019 | WEB | FOUND | - | - | AXS-010/LED-007,CLM-005 — SMIC indexation IPC IRL indexation loyers Insee
QRY-020 | WEB | FOUND | - | - | AXS-011/LED-012,CLM-001 — ONS CPIH owner occupiers housing costs vs HICP France loyers imputés
QRY-021 | WEB | FOUND | - | - | AXS-010? non — AXS-pauvreté/LED-010,CLM-007 — Insee taux de pauvreté 2024 seuil 60% médiane 9 817 000
QRY-022 | WEB | FOUND | - | - | AXS-002/LED-003 — Crédoc baromètre inflation perçue; UFC Que Choisir indices inflation alternatifs
QRY-023 | FETCH | FOUND | SRC-010 | https://www.insee.fr/fr/statistiques/2408345 | FETCH Personnes pauvres selon le seuil (ERFS 1975-2024)
QRY-024 | FETCH | FOUND | SRC-011 | https://www.quechoisir.org/actualite-alimentation-hygiene-droguerie-les-vrais-chiffres-de-l-inflation-n110542/ | FETCH UFC Que Choisir — les vrais chiffres de l inflation (relevés propres)
QRY-025 | WEB | FOUND | - | - | AXS-001/LED-002 — Insee IPC méthodologie pondérations Budget de famille sources
QRY-026 | FETCH | FOUND | SRC-012 | https://www.latribune.fr/article/economie/28780383207962/inflation-ce-que-change-le-nouveau-calcul-de-lindice-des-prix-de-l-insee | FETCH La Tribune — ce que change le passage base 2015 vers base 2025
QRY-027 | FETCH | FOUND | SRC-013 | https://www.francetransactions.com/le-saviez-vous/pourquoi-l-inflation-publiee-par-l-insee-ne-reflete-t-elle-pas-veritablement-la.html | FETCH FranceTransactions — inflation Insee vs coût de la vie
QRY-028 | FETCH | FOUND | SRC-014 | https://www.persee.fr/doc/polix_0295-2319_1994_num_7_25_1830 | FETCH Persée — recension critique La politique des grands nombres (Desrosières)
QRY-029 | WEB | FOUND | - | - | AXS-006/LED-008,CLM-006 — révision comptes nationaux mai 2025 PIB croissance révisée
QRY-030 | FETCH | FOUND | SRC-015 | https://www.bfmtv.com/economie/economie-social/une-croissance-annuelle-de-0-9-qui-passe-a-1-9-pourquoi-l-insee-a-revu-la-performance-de-l-economie-francaise-des-annees-post-covid-avec-une-hausse-parfois-plus-de-2-fois-plus-forte_AV-202606070045.html | FETCH BFM — révision croissance post-Covid 0,9% vers 1,9% (compte définitif 2023)
QRY-031 | FETCH | FOUND | SRC-016 | https://www.ofce.fr/blog2024/fr/2025/20251124_EA/ | FETCH OFCE — l économie française va mieux qu on ne le pensait (révisions cumulées PIB)
QRY-032 | FETCH | FOUND | SRC-017 | https://www.service-public.gouv.fr/particuliers/vosdroits/F2300 | FETCH Service Public F2300 — Smic revalorisation indexation IPC 20% plus modestes
QRY-033 | FETCH | FOUND | SRC-018 | https://www.insee.fr/fr/statistiques/1521318 | FETCH Insee Analyses 5 — l inflation telle que perçue par les ménages (OPI/IPC)
QRY-034 | FETCH | FOUND | SRC-019 | https://www.economie.gouv.fr/actualites/nomination-de-fabrice-lenglart-au-poste-de-directeur-general-de-linsee | FETCH economie.gouv — nomination Lenglart DG Insee (05/06/2025)
QRY-035 | FETCH | FOUND | SRC-020 | https://www.insee.fr/fr/statistiques/4126450 | FETCH Insee Focus 152 — le logement dans l IPC
QRY-036 | FETCH | FOUND | SRC-021 | https://fgeerolf.com/blog-insee-IPC-loyers.html | FETCH Geerolf — au sujet du Blog Insee sur l IPC et les loyers
QRY-037 | FETCH | FOUND | SRC-022 | https://www.insee.fr/fr/statistiques/8193933 | FETCH Insee Première 1997 — les comptes de la Nation en 2023 (première estimation 0,9%)
QRY-038 | FETCH | FOUND | SRC-023 | http://www.hcfp.fr/jean-luc-tavernier | FETCH HCFP — biographie Jean-Luc Tavernier
QRY-039 | FETCH | FOUND | SRC-024 | https://www.service-public.gouv.fr/particuliers/vosdroits/F13723 | FETCH Service Public F13723 — IRL formule IPC hors tabac hors loyers
QRY-040 | FETCH | FOUND | SRC-025 | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000022405540 | FETCH Legifrance — article 1 loi 1951 (ASP, indépendance professionnelle)
QRY-041 | WEB | FOUND | - | - | Insee mai 2025 révision PIB 2023 2024 croissance révisée 1,1% 0,9% Le Monde Les Echos
QRY-042 | WEB | FOUND | - | - | REFUTATION révision croissance PIB France 2023 0,9% 1,9% compte définitif contesté erreur
QRY-043 | WEB | FOUND | - | - | REFUTATION IPC Insee mesure coût de la vie sous-estimation démontrée prix logement taxes panier
QRY-044 | WEB | FOUND | - | - | REFUTATION ONS Destatis HICP CPIH tout pays CPI inclut loyers imputés expérience comparée
QRY-045 | FETCH | FOUND | SRC-026 | https://www.ensae.fr/actualites/conference-03/10-jean-luc-tavernier-dg-de-linsee-et-alumni-x-ensae | FETCH ENSAE Paris — conférence Jean-Luc Tavernier alumni X-ENSAE
QRY-046 | FETCH | FOUND | SRC-027 | https://academiesciencesmoralesetpolitiques.fr/evenement/colloque-international-cnis-asp-lindependance-des-statistiques-publiques/ | FETCH Académie sciences morales et politiques — colloque international indépendance statistiques publiques 19/06/2026
QRY-047 | FETCH | FOUND | SRC-028 | https://www.anil.org/outils/indices-et-plafonds/tableau-de-lirl/ | FETCH ANIL — tableau de l IRL publié par l Insee

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/4268033
SRC-002 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/serie/001763852
SRC-003 | ◈ | fam:A | https://www.insee.fr/fr/information/4174951
SRC-004 | ◈ | fam:A | https://www.insee.fr/fr/information/8203034?sommaire=8203072
SRC-005 | ◉ | fam:D | https://laviedesidees.fr/Les-statistiques-un-service-public
SRC-006 | ◈ | fam:A | https://www.insee.fr/fr/information/2014679
SRC-007 | ◈ | fam:A | https://www.insee.fr/fr/information/1300622
SRC-008 | ◈ | fam:A | https://www.insee.fr/fr/information/8603402
SRC-009 | ◈ | fam:A | https://www.senat.fr/rap/l24-144-312/l24-144-3123.html
SRC-010 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/2408345
SRC-011 | ◉ | fam:C | https://www.quechoisir.org/actualite-alimentation-hygiene-droguerie-les-vrais-chiffres-de-l-inflation-n110542/
SRC-012 | ○ | fam:D | https://www.latribune.fr/article/economie/28780383207962/inflation-ce-que-change-le-nouveau-calcul-de-lindice-des-prix-de-l-insee
SRC-013 | ◉ | fam:C | https://www.francetransactions.com/le-saviez-vous/pourquoi-l-inflation-publiee-par-l-insee-ne-reflete-t-elle-pas-veritablement-la.html
SRC-014 | ◉ | fam:E | https://www.persee.fr/doc/polix_0295-2319_1994_num_7_25_1830
SRC-015 | ◉ | fam:D | https://www.bfmtv.com/economie/economie-social/une-croissance-annuelle-de-0-9-qui-passe-a-1-9-pourquoi-l-insee-a-revu-la-performance-de-l-economie-francaise-des-annees-post-covid-avec-une-hausse-parfois-plus-de-2-fois-plus-forte_AV-202606070045.html
SRC-016 | ◉ | fam:E | https://www.ofce.fr/blog2024/fr/2025/20251124_EA/
SRC-017 | ◈ | fam:A | https://www.service-public.gouv.fr/particuliers/vosdroits/F2300
SRC-018 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/1521318
SRC-019 | ◈ | fam:A | https://www.economie.gouv.fr/actualites/nomination-de-fabrice-lenglart-au-poste-de-directeur-general-de-linsee
SRC-020 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/4126450
SRC-021 | ◉ | fam:E | https://fgeerolf.com/blog-insee-IPC-loyers.html
SRC-022 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/8193933
SRC-023 | ◈ | fam:A | http://www.hcfp.fr/jean-luc-tavernier
SRC-024 | ◈ | fam:A | https://www.service-public.gouv.fr/particuliers/vosdroits/F13723
SRC-025 | ◈ | fam:A | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000022405540
SRC-026 | ◈ | fam:A | https://www.ensae.fr/actualites/conference-03/10-jean-luc-tavernier-dg-de-linsee-et-alumni-x-ensae
SRC-027 | ◈ | fam:other:asm | https://academiesciencesmoralesetpolitiques.fr/evenement/colloque-international-cnis-asp-lindependance-des-statistiques-publiques/
SRC-028 | ◉ | fam:C | https://www.anil.org/outils/indices-et-plafonds/tableau-de-lirl/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://www.insee.fr/fr/statistiques/1521318 | A,C,E | 2012-07-12 | Inflation perçue par les ménages écart IPC Insee | Depuis 2004, l'inflation perçue (OPI, enquête CAMME, ~2000 ménages) fluctue en moyenne environ 6 points au-dessus de l'IPC; l'Insee et la Banque de France attribuent l'écart principalement à la surpondération des prix en hausse et à forte fréquence d'achat, et reconnaissent que l'OPI possède des bases objectives. | a995399b-01e8-4dc8-bb2f-d0a7ef05cf94
FCT-002 | FACT | ✧ | https://www.economie.gouv.fr/actualites/nomination-de-fabrice-lenglart-au-poste-de-directeur-general-de-linsee | A | 2025-06-05 | Directeur général Insee nomination Conseil des ministres | Le directeur général de l'Insee est nommé en Conseil des ministres (art.13 Constitution); Fabrice Lenglart, nommé le 5 juin 2025 sur proposition de Bercy, succède à Jean-Luc Tavernier (2012-2025); profil X-ENSAE, ex-DREES, France Stratégie, Trésor, Insee. | 8b6fd4b4-def1-41e9-bbac-dde456f7ee35
FCT-003 | FACT | ✦ | https://www.insee.fr/fr/statistiques/8193933 | A,D,E | 2026-06-07 | Révision croissance PIB France 2023 | La croissance française de 2023, initialement estimée à 0,9% (janvier 2024; comptes annuels mai 2024), a été révisée à 1,4% (mai 2025, base 2020) puis à 1,9% corrigé des jours ouvrés (compte définitif, juin 2026): révision cumulée d'environ 1 point, la plus forte depuis 2003. | 82daeeca-eb22-4adf-859e-0a349c7fb025
FCT-004 | FACT | ✧ | https://www.service-public.gouv.fr/particuliers/vosdroits/F13723 | A | 2026-07-12 | IRL indice de référence des loyers IPC hors tabac hors loyers | L'IRL (indexation légale des loyers d'habitation) est calculé à partir de la moyenne de l'évolution des prix à la consommation hors tabac et hors loyers sur les 12 derniers mois; édition T2 2026: +1,15% sur un an. | 0c83fb4e-3cc8-485c-9e4b-719f44ad830c
FCT-005 | FACT | ✦ | https://www.insee.fr/fr/statistiques/4126450 | A,E | 2019-04-18 | Exclusion loyers imputés IPC France HICP | L'IPC français exclut le coût du logement des propriétaires (loyers imputés), comme l'HICP européen — méthode qu'Eurostat qualifie elle-même de trop étroite; l'Allemagne (poids loyers 20,7% dont imputés), les USA (23,5% imputés plus 7,6% réels) et le Royaume-Uni (CPIH) incluent le logement des propriétaires; l'IPC français y inclut en revanche les dépenses de santé remboursées (indice hybride, écart cumulé d'environ 5% avec l'IPCH depuis 1996 selon Geerolf). | bb187cdb-bd17-4b57-9f6e-ea949dcc0a11
FCT-006 | FACT | ✧ | https://www.service-public.gouv.fr/particuliers/vosdroits/F2300 | A | 2026-06-01 | SMIC revalorisation indexation IPC ménages les plus modestes | Le SMIC est revalorisé chaque 1er janvier, indexé sur l'inflation mesurée pour les 20% des ménages aux revenus les plus faibles; en cours d'année, hausse automatique si l'IPC glisse d'au moins 2%; l'adéquation ex post (protection effective des modestes) est contestée selon les sous-périodes (2021-2023 vs 2025). | ba618622-71eb-4d6e-a818-43bc9bf264f0
FCT-007 | FACT | ✧ | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000022405540 | A,other:asm | 2010-06-30 | Autorité de la statistique publique indépendance professionnelle loi | La loi du 7 juin 1951 (art.1, version 2010) dispose que la conception, la production et la diffusion des statistiques publiques sont effectuées en toute indépendance professionnelle, et crée l'Autorité de la statistique publique (neuf membres) chargée d'en veiller au respect. | 324d3e38-37f0-405f-9e09-b758eb96ae3f
FCT-008 | FACT | ✧ | https://www.insee.fr/fr/information/8603402 | A | 2025-06-30 | Circulation des cadres Insee Trésor DREES Fabrice Lenglart | La biographie officielle du DG Lenglart (X1989, ENSAE 1994) documente la circulation Insee-Trésor-Prévision-France Stratégie-DREES-Insee sur trois décennies, illustrant le canal de recrutement de la direction de l'Insee au sein de la haute fonction publique économique. | fdee4b44-2d92-4453-84a9-3f7e83212151
FCT-009 | FACT | ✧ | https://www.insee.fr/fr/statistiques/2408345 | A | 2026-07-09 | Personnes pauvres seuil 60 pourcent France ERFS 2024 | En 2024, au seuil de 60% du niveau de vie médian, le nombre de personnes pauvres est de 9 817 000 (série ERFS, champ France métropolitaine, personne de référence non étudiante; ruptures de série 2010, 2012, 2020); la presse rapporte un taux de pauvreté stabilisé à 15,4%, niveau le plus élevé jamais mesuré sur la série récente. | 16e14263-b2a3-45bf-99f2-4248944c98cf
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-018,SRC-011,SRC-014
FCT-002 | SRC-019,SRC-023,SRC-018
FCT-003 | SRC-022,SRC-015,SRC-016
FCT-004 | SRC-024,SRC-017
FCT-005 | SRC-020,SRC-021
FCT-006 | SRC-017
FCT-007 | SRC-025,SRC-027
FCT-008 | SRC-008,SRC-006,SRC-019
FCT-009 | SRC-010

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-043 | NONE
FCT-003 | QRY-042 | NONE
FCT-005 | QRY-044 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:CONFIRME
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:CONFIRME
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | ELIGIBLE:VERIFIE
FCT-008 | ELIGIBLE:VERIFIE
FCT-009 | ELIGIBLE:VERIFIE

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
CP-005 | CAUSAL:CAU-006 | PASS | LAST_COMPLETED:11:CAU-006 | NEXT_ACTION:12
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-20T16:07:15.454653+00:00","fact_mem":{"FCT-001":"a995399b-01e8-4dc8-bb2f-d0a7ef05cf94","FCT-002":"8b6fd4b4-def1-41e9-bbac-dde456f7ee35","FCT-003":"82daeeca-eb22-4adf-859e-0a349c7fb025","FCT-004":"0c83fb4e-3cc8-485c-9e4b-719f44ad830c","FCT-005":"bb187cdb-bd17-4b57-9f6e-ea949dcc0a11","FCT-006":"ba618622-71eb-4d6e-a818-43bc9bf264f0","FCT-007":"324d3e38-37f0-405f-9e09-b758eb96ae3f","FCT-008":"fdee4b44-2d92-4453-84a9-3f7e83212151","FCT-009":"16e14263-b2a3-45bf-99f2-4248944c98cf"},"mnemo_row":"PASS: 9/9 eligible facts persisted via MCP write_memory (8002); no duplicate_warning; run 2026-09-20_17-04_insee-biais-modes-calcul-fresque-systemique","result":"PASS","writeback_execution":[{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"tier ✦ -> status:CONFIRME (>=2 familles + refutation terminale)","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"tier ✧ -> status:VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"tier ✦ -> status:CONFIRME (>=2 familles + refutation terminale)","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"tier ✧ -> status:VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"tier ✦ -> status:CONFIRME (>=2 familles + refutation terminale)","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"tier ✧ -> status:VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"tier ✧ -> status:VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-008","reason":"tier ✧ -> status:VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-009","reason":"tier ✧ -> status:VERIFIE","success":1}],"writeback_row":{"attempted":9,"blocked":0,"eligible":9,"failure":0,"success":9}}

PERSISTENCE_META: MNEMO_ROW:PASS: 9/9 eligible facts persisted via MCP write_memory (8002); no duplicate_warning; run 2026-09-20_17-04_insee-biais-modes-calcul-fresque-systemique | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:9;attempted:9;success:9;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[9 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✦ -> status:CONFIRME (>=2 familles + refutation terminale)
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✧ -> status:VERIFIE
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✦ -> status:CONFIRME (>=2 familles + refutation terminale)
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✧ -> status:VERIFIE
FCT-005 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✦ -> status:CONFIRME (>=2 familles + refutation terminale)
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✧ -> status:VERIFIE
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✧ -> status:VERIFIE
FCT-008 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✧ -> status:VERIFIE
FCT-009 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:tier ✧ -> status:VERIFIE
