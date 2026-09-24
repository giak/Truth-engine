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
