# PLAN D'INVESTIGATIONS — Vague « Absences de preuves » (campagne 2026-09)

> Version : 1.0 — 2026-09-05
> Source d'ancrage : `campagne_cartographie.json` (généré 2026-09-05, suivi par `_plan_cartographie_campagne.md` / `_design_cartographie_campagne.md`)
> Protocole de recouvrement : `_protocol_renard-core-v3.md` (bascule obligatoire si preuves/pistes insuffisantes)
> Contrat d'exécution : `truth-engine-v2/KERNEL.md` (2.10.6) — exclusivement via `knowledge.md` racine canonique.
> Usage : Truth Engine prend chaque investigation **une par une** et la conduit à APEX (scoring $CX, saturation des AXS, gates PRE/DELIVERY).

---

## 0. Règles de conduite épistémiques (rappel, sans dérogation)

**NON TROUVÉ ≠ INEXISTANT ≠ FAUX** — **AFFIRMÉ ≠ PROUVÉ ≠ VRAI**

Les statuts probatoires à distinguer à tout instant (et à produire en sortie) :

| Statut | Définition opératoire |
|---|---|
| Établi (✦, CONFIRME, L4) | Fait vérifiable sourcé, confirmé au niveau 4 |
| Allégué (✧, VERIFIE, L1-L3) | Affirmation vérifiée partiellement, pas encore confirmée |
| Plausible non démontré | Cohérent et psychologiquement plausible, aucune preuve positive |
| Contredit | Une preuve ou un contrôle établit le contraire |
| Non trouvé après recherche | Recherche bornée effectuée, résultat vide |
| Absence démontrée | L'existence supposée **aurait dû** laisser des traces observables, recherche exhaustive → néant. Seul cas où l'absence devient informative. |

**Article Protocol (règle du projet) : `NON_TROUVÉ → N'EXISTE_PAS` INTERDIT.**  
Le passage « non trouvé » → « absence démontrée » n'est licite que si : (1) l'objet allégué produit normalement des traces (registre, procédure, transaction, contrôle, contentieux) ; (2) la recherche couvre ces dépôts attendus ; (3) le périmètre de recherche est borné et consigné. À défaut, TERMINAL = « non trouvé après recherche (périmètre X) », jamais une conclusion d'inexistence.

**RENARD CORE V3 (lancer si preuves/pistes insuffisantes)**  
Si, sur un atom, **aucune preuve probatoire ET aucun indice/piste exploitable** ne subsistent après les phases de recherche standard, bascule **obligatoire** sur `_protocol_renard-core-v3.md` : `DECOMPOSE` avant toute recherche, `SHADOW` (prédiction des traces attendues sous H/rivaux avant de chercher), `TRACE`/LINEAGE, `BREAK(H)` adversaire, `UPDATE`, puis `EVALUATE` avec EPISTEMIC_LEDGER et CALIBRATION ≥ 0.7. Objectif : **savoir si l'absence est informative**, pas forcer une conclusion. RENARD renforce la discipline ; il ne remplace pas KERNEL (RUN_STATE, gates, `_INVESTIGATION.md` restent contractuels).

**Mode d'exécution KERNEL rappel :**
- `MISSION_MODE` : `VERIFY_ONLY` (objet = un débunk/fact-check borné, `OBJECT_QUESTION := N/A(EXPLICIT_VERIFY_ONLY)`) ou `INVESTIGATION` (objet primaire + branche audit des leads).
- `RUN_ID := YYYYMMDD-HHMM-{SUBJECT_SLUG}` ; un seul `RUN_DIR` par investigation.
- Gates contractuelles :
  `python3 tools/verify/verify.py gate --file $INVESTIGATION_PATH --kernel-contract pre`
  `python3 tools/verify/verify.py gate --file $INVESTIGATION_PATH --kernel-contract delivery`
- **APEX = saturation de l'objet, jamais présence forcée.** `INCONCLUSIVE` zéro-fait-confirmé est un outcome valide et honnête.
- Écriture mémoire : `✦→CONFIRME`, `✧→VERIFIE` ; jamais de fait non confirmé écrit comme vérifié ; `mem:"-"` en sortie d'extraction tant que le write-back n'a pas rebindé.
- Références exactes : les dossiers cités existent dans `campagne_cartographie.json`/dans `investigations/2026-09/`.

## 1. Ancrage & vérification (double-check 2026-09-05)

Vérification programmatique des références de ce plan contre `campagne_cartographie.json` :
- ✅ Tous les CAU cités existent (`CAU-002/003/004/005/007/008`, types CORRELATION_VS_CAUSATION / CAUSALITY / CAUSAL_MECHANISM / EVIDENCE_GAP / INTENT).
- ✅ Tous les faits exemplaires cités sont présents (1+ match chacun) : accusation Nord Stream « no conclusive evidence » ; enquête allemande 7 suspects ; piste ukrainienne NYT 07/03/2023 ; perquisition 192 325 EUR ; Abibulayev ; von der Leyen GPS ; Storm-1516/77 op ; 25 tentatives 2024 ; ELNET 101 voyages ; Cambridge Analytica 87M ; AIQ 656k £ ; Banks 8,5 M £ ; CIA 5 M$/an Italie ; NED 31,3 M$ ; O'Rourke ; Volontè 500 000 EUR ; Francken VRT 17/04/2026.
- ✅ `refutations` = 0 sur 167 faits (constat d'instrument absent, piste-mère INV-30).
- ✅ 2 kernels d'élévation non classés (`classes=[]`, 7 faits chacun) ; 48 ✧ candidats à l'élévation.
- ✅ 27 faits uk-brexit à `mem:"-"` (sentinelles sans lien mémoire).
- ✅ 8 dossiers uk-brexit `empty` (planifiés, jamais exécutés) — vivier INV-14..21.
- 2 alarmes de contrôle > vérifiées manuellement : coquilles de script (accent `é`/`e` ; `len()` sur liste), absentes de la donnée.

## 2. Carte des investigations

Priorité P0 > P1 > P2. Chaque investigation : mode, stance épistémique ((a) absence non informative / (b) absence informative / (c) affirmation non prouvée / (d) déminage structurel), questions, périmètre, traces attendues, ancrage, amorces.

---

### Vague A — Attributions russes & chaînes d'argent (absences informatives)

#### INV-01 — Nord Stream : trancher l'INTENT entre pistes russe/ukrainienne  [P0 · INVESTIGATION · (b)(c)]
- **LEAD_QUESTION** : L'attribution des explosions de Nord Stream (26/09/2022) est-elle établie par les enquêtes judiciaires publiées ?
- **OBJECT_QUESTION** : Quels éléments probatoires permettent (ou excluent) chacune des pistes (russe, ukrainienne, étatique-non-étatique) à partir des actes judiciaires publiés ?
- **Périmètre** : 09/2022 → 09/2026 ; DE/SE/DK/US/UA ; sabotage infra énergétique critique.
- **Traces attendues** : actes du parquet fédéral Karlsruhe, conclusions SE/DK « no conclusive evidence », rapports CIA (nov. 2023) vs WSJ (08/2024), extractions Zhuravlev/Serhiy K.
- **Ancrage** : `2026-09-05_nord-stream-2-accusation-russie-piste-ukraine-silence-allemand` ; CAU-003 INTENT ; FCT « Accusation _Russie_… jamais étayée », « Enquête allemande… 7 suspects », « Piste ukrainienne… NYT 07/03/2023 ».
- **Exigence** : n'abandonner aucune piste sans terminaison probatoire ; la conclusion « attribution non tranchée » est permissible (SATURATED) si les avenues publiques sont épuisées.

#### INV-02 — Nord Stream : qui a payé Andromeda (financement)  [P0 · INVESTIGATION · (b)]
- **LEAD_QUESTION** : La chaîne de financement de l'opération Andromeda est-elle documentée jusqu'à son origine ?
- **OBJECT_QUESTION** : Qui a réellement financé et piloté l'opération (Abibulayev, Feeria Lwowa, comptes saisis) et quels flux montrent les actes bancaires judiciaires ?
- **Traces attendues** : perquisitions (192 325 EUR / 126 682 USD), saisies, mandats, actes de cession, comptes Google saisis.
- **Ancrage** : `2026-09-05_financement-andromeda-nord-stream-qui-a-paye` ; CAU-002 CAUSAL_MECHANISM ; FCT « Enquête allemande… », « Nom complet du financier… », « Perquisition ukrainienne… ».

#### INV-03 — Vague de drones 2025 FR/UE : attribution russe sans preuve matérielle (LE cas « absence de preuve ≠ absence »)  [P0 · INVESTIGATION · (b)(c)]
- **LEAD_QUESTION** : L'attribution à la Russie de la vague de fermetures d'aéroports (2025-2026) est-elle étayée par des traces matérielles ?
- **OBJECT_QUESTION** : Les observations documentées (drones inexpliqués, signalements) permettent-elles de trancher entre opération clandestine étatique (auquel cas l'absence de traces publiques est *cohérente*) et phénomène non-étatique/amplifié ?
- **Périmètre** : 2025 → 2026 ; FR/UE ; basse altitude aéroportuaire ; acteurs : États, média (VRT Pano), industrie.
- **Traces attendues** : NOTAMs, comptes rendus de sécurité, signalements gendarmerie/aviation civile, rapports d'enquête ; **absence de traces = donnée à qualifier formellement**, pas à présumer.
- **Ancrage** : `2026-09-05_drones-aeroports-france-ue-accusations-sans-preuves` ; CAU-005 EVIDENCE_GAP ; FCT « Vague 2025… non confirmés », « Attribution à la Russie… sans preuve matérielle », « Cas Belgique (VRT Pano 17/04/2026) : Francken a exagéré… ».
- **STATUT : LIVRÉ (2026-09-06)** — RUN `20260906-0733-attribution-russie-fermetures-aeroports-europe` (`investigations/2026-09/2026-09-06_attribution-russie-fermetures-aeroports-europe/`) ; gates pre + delivery **PASS** (certifié, état final) ; 13 FCT (7 writeback VERIFIE, 6 EVIDENCE/INFERENCE non éligibles) ; verdict : attribution russe de la vague 2025 **déclarative, non probatoire, ni établie ni réfutée** (H1 possible/OPSEC, R3 amplification dominante, R4 résiduel ouvert, Leipzig cas distinct documenté ADN) ; overlay RENARD CORE V3 post-livraison : EPISTEMIC_LEDGER verified 6 / disputed 1 / open 3 / refuted 0, CALIBRATION 1.0 (caveat : H1 reste OPEN — investigateur insuffisant pour trancher, suffisant pour caractériser les rivaux). Prochain pas (§4) : INV-01 puis INV-02 (fin Vague A P0), puis INV-04..07 (Vague A P1), puis INV-09 (Vague B).

#### INV-04 — Filière antidrones UE : « qui vend, qui gagne » et conflits d'intérêt  [P1 · INVESTIGATION · (b)(c)]
- **LEAD_QUESTION** : Les intérêts économiques de la filière antidrones (« qui vend, qui gagne ») orientent-ils les récits de menace et les ventes ?
- **OBJECT_QUESTION** : Quels marchés/contrats et conflits d'intérêt sont documentables entre fabricants, États et narratifs de menace ?
- **Traces attendues** : marchés publics, appels d'offres défense, registres de lobbying, déclarations HATVP.
- **Ancrage** : `2026-09-05_filiere-antidrones-europe-qui-vend-qui-gagne` ; CAU-002 DISPUTED, CAU-003 CORRELATION_VS_CAUSATION, CAU-005 INTENT.

#### INV-05 — Storm-1516 : corroboration des 77 opérations hors de la source VIGINUM  [P1 · INVESTIGATION · (c)]
- **LEAD_QUESTION** : L'attribution russe (VIGINUM, 77 opérations 2023-2025) est-elle corroborée par des sources indépendantes de l'État attribuant ?
- **OBJECT_QUESTION** : Quelles traces publiques (Threat Intel, rapports, cibles .gov, OSINT) recoupent — ou contredisent — le registre VIGINUM ?
- **Périmètre** : 08/2023 → 03/2025 ; audiences occidentales/FR ; opérations informationnelles.
- **Traces attendues** : rapport VIGINUM technique, publications de chercheurs, index des domaines cibles, trajectoires documentées des RRN/Matriochka.
- **Ancrage** : `2026-09-05_viginum-instrument-pouvoir-debunk-narratifs` ; FCT « ingérence numérique russe Storm-1516 », « Ingerences numeriques etrangeres materielles documentees par VIG… ».

#### INV-06 — Brouillage GPS Baltique : traces indépendantes de l'attribution  [P1 · VERIFY_ONLY · (c)]
- **LEAD_QUESTION (VMO)** : L'attribution du brouillage GPS (dont l'avion von der Leyen, 31/08/2025) à la Russie repose-t-elle sur des preuves matérielles ou sur des affirmations relayées ?
- **Traces attendues** : NOTAMs, rapports de l'EASA/autorités nationales, AP (~80 incidents régional), donnés Pologne/Lituanie (2732/1185 en 01/2025).
- **Ancrage** : `2026-09-05_viginum-instrument-pouvoir-debunk-narratifs` ; FCT « Affaire von der Leyen… attribution russe… affirmation de la Commission relayant des autorités… », « brouillage/spoofing GPS russe… phénomène régionale documenté depuis 2022 ».

#### INV-07 — Voice of Europe : traces des paiements aux MEP  [P1 · VERIFY_ONLY · (b)]
- **LEAD_QUESTION (VMO)** : Les paiements VoE (~1 M€/mois, Medvedchuk/FSB) à des élus UE sont-ils tracés (enquêtes, saisies, condamnations) ?
- **Traces attendues** : actes d'enquête (BE/CZ/DE/FR), saisies, rapports de la commission ingérences 2023, jugements.
- **Ancrage** : `2026-09-05_ingerences-electorales-france-ue` ; FCT ✧ « Voice of Europe paiements MEPs » (url : BBC 68797624).

---

### Vague B — UK Brexit : l'eldorado du non-fait (8 dossiers planifiés-vides + le dossier dense 27 faits)

Le dossier `uk-brexit-ingerences-manipulations-democraties` concentre 27 faits (tous à `mem:"-"`, 27/27 sans lien mémoire) mais les 8 dossiers planifiés n'ont **jamais été exécutés** — chaque piste ci-dessous est un RUN à lancer tel quel.

#### INV-08 — Cambridge Analytica : l'effet causal manquant  [P0 · INVESTIGATION · (c)]
- **LEAD_QUESTION** : L'impact de CA/des données sur le sursaut de vote (ou l'abstention) au référendum 2016 est-il démontré ?
- **OBJECT_QUESTION** : Quel est l'état rigoureux de la recherche (consommation, micro-ciblage, effet causal) — et une absence de littérature d'effet est-elle elle-même informative ?
- **Traces attendues** : conclusions ICO, enquêtes parlementaires DCMS, littérature académique contrôlée.
- **Ancrage** : `2026-09-05_uk-brexit-ingerences-manipulations-democraties` ; FCT ✦ « Cambridge Analytica 87M profils » (jusqu'à 87M, app thisisyourdigitallife).
- **Exigence** : terme « non démontré » uniquement avec bornes de recherche consignées (OBJECT_COVERAGE).

#### INV-09 — Leave.EU/Banks : provenance réelle des 8,5 M £  [P0 · INVESTIGATION · (b)]
- **LEAD_QUESTION** : L'origine des 8,5 M £ de Banks/Leave.EU est-elle tracée ou seulement « suspecte » ?
- **OBJECT_QUESTION** : Quelles sources (Electoral Commission, documentations bancaires, rapport IPT) établissent ou infirment une origine étrangère ?
- **Traces attendues** : rapport Electoral Commission (LeaveEU fined pour infractions), investigations FSB/banques, documents publics.
- **Ancrage** : `2026-09-05_uk-brexit-ingerences-manipulations-democraties` ; FCT ✦ « Aaron Banks 8,5 M£ Leave.EU… suspects d'origine russe… et américaine ».

#### INV-10 — AIQ / AggregateIQ 656 k £ : la machine Vote Leave  [P1 · VERIFY_ONLY · (c)]
- **LEAD_QUESTION (VMO)** : Le lien AIQ ↔ Vote Leave ↔ CA est-il matériellement établi (contrats, données, personnes) ?
- **Ancrage** : `2026-09-05_uk-brexit-ingerences-manipulations-democraties` ; FCT ✦ « AIQ/AggregateIQ 656k£ Vote Leave ».

#### INV-11 — Impact causal du référendum (non établi)  [P0 · INVESTIGATION · (c)]
- **LEAD_QUESTION** : L'effet causal des ingérences documentées sur le résultat du référendum 2016 est-il établi, exclu, ou non-tranchable ?
- **OBJECT_QUESTION** : Quelles analyses causales (régression, attention, scrutins-test) éclairent l'attribution de l'écart (« non établi » ≠ « sans effet ») ?
- **Ancrage** : `2026-09-05_uk-brexit-impact-causal-referendum` (dossier vide, planifié-non-exécuté) + `uk-brexit-ingerences-manipulations-democraties` ; CAU-007, CAU-008 ; FCT ✧ « Impact causal Brexit non établi ».

#### INV-12 — ICO / Electoral Commission / GCHQ-CIP : tout à investiguer (dossier vide)  [P1 · VERIFY_ONLY · (b)]
- **LEAD_QUESTION (VMO)** : Les contrôles publics (ICO sur les data analytics, Electoral Commission sur la collusion « non poursuivie », opérations d'influence présumées de GCHQ) sont-ils constatables dans les archives ?
- **Traces attendues** : rapport ICO (data analytics in political campaigns), site EC, documents CIP publiés.
- **Ancrage** : `2026-09-05_uk-brexit-electoral-commission-ico-ofcom` + `2026-09-05_uk-brexit-gchq-cip-influence-presumee` (les deux vides) ; FCT ✧ « ICO conclusion CA pas impliqué dans Brexit », « Electoral Commission n'a pas poursuivi collusion », « GCHQ/CIP opérations d'influence ».

#### INV-13 — UK think tanks : policy manufacturing  [P1 · INVESTIGATION · (c)]
- **LEAD_QUESTION** : Les think tanks UK pro-Brexit ont-ils produit/promu des policy positions sur commande, et leurs financements sont-ils tracés ?
- **OBJECT_QUESTION** : Qui finance les think tanks pro-Brexit (traçage registres + déclarations) et quelles policy positions en découlent-elles documentablement ?
- **Ancrage** : `2026-09-05_uk-brexit-think-tanks-policy-manufacturing` (vide) ; croiser `2026-09-05_lobbies-thinktanks-clubs-francs-macons` (La Fabrique de l'industrie, charte anti-veto des actionnaires).

#### INV-14 — UK dark money : flux financiers  [P1 · INVESTIGATION · (b)]
- **LEAD_QUESTION** : Les flux de type « dark money » (offshore, paradis de la data) dans la campagne Leave sont-ils documentables ?
- **OBJECT_QUESTION** : Quels circuits financiers non déclarés peuvent être établis à partir des registres, la EC et les enquêtes publiées ?
- **Ancrage** : `2026-09-05_uk-brexit-dark-money-flux-financiers` (vide) + `2026-09-05_uk-brexit-data-paradieses-offshore` (bare, hors-protocole).

#### INV-15 — UK médias & propagande, biais  [P1 · VERIFY_ONLY · (c)]
- **LEAD_QUESTION (VMO)** : Les biais/propagande médiatique pro-Leave sont-ils mesurables dans les corpus publics (tonalité, couverture, erreurs factuelles) ?
- **Ancrage** : `2026-09-05_uk-brexit-medias-propagande-biais` (vide).

#### INV-16 — UK convergences FR-UE  [P2 · INVESTIGATION · (c)]
- **LEAD_QUESTION** : Quelles convergences structurelles (acteurs, techniques, financements) entre les opérations britanniques et européennes de manipulation ?
- **Ancrage** : `2026-09-05_uk-brexit-convergences-france-ue` (vide) ; croiser `2026-09-05_convergences-systemiques-architecture-controle` (bare).

---

### Vague C — Déminage épistémique : les non-trouvés systématiques (recherche positive imposée)

#### INV-17 — Soros & contrôle des médias/politique FR-UE  [P1 · VERIFY_ONLY · (d)]
- **LEAD_QUESTION (VMO)** : Le contrôle de Soros/OSF sur les médias et la politique FR/UE est-il étayé par des preuves (investissements, actionnariat, financements) ?
- **Exigence** : recherche positive des deux côtés (usages documentés ET absence de contrôle) ; terminaison sous forme de statut probatoire, pas « pas trouvé ».
- **Ancrage** : `2026-09-05_ingerences-usa-soros-aipac-fondations-israel` ; LED-005 « Accusations de contrôle d Israel / Soros… debunk, absence de preuve ».

#### INV-18 — Franc-maçonnerie : membres (175k+) ≠ coordination  [P1 · INVESTIGATION · (d)]
- **LEAD_QUESTION** : Un réseau de pouvoir coordonné (francs-maçons) est-il traçable dans les archives, ou s'agit-il de membership non coordonné ?
- **OBJECT_QUESTION** : Quelle est la structure organisationnelle réelle (obédiences, cooptation) et quelles interférences démontrables impliquent-elles des francs-maçons *en tant qu'acteur collectif* ?
- **Ancrage** : `2026-09-05_lobbies-thinktanks-clubs-francs-macons` ; CAU-004 CAU-GAP « franc-maconnerie (175 000+ membres documentés) : aucune preuve vérifiée de coordination » ; LED-005 « complot des cercles/francs-macons : absence de preuve de coordination ».

#### INV-19 — Révolutions de couleur : l'effet causal des financements occidentaux  [P1 · INVESTIGATION · (c)]
- **LEAD_QUESTION** : Les financements documentés (NED 31,3 M$ 1983 ; CIA 5 M$/an sur l'Italie 1948-1968 ; programmes civiques orange) ont-ils un effet causal établi sur les changements de régime ?
- **OBJECT_QUESTION** : Quelles études contrôlées éclairent causalité financement-démocratisation — et l'absence de telles études est-elle informative ?
- **Ancrage** : `2026-09-05_revolutions-couleur-cia-usaid-ned` ; CAU-005 du kernel vague3 « L'effet causal des financements occidentaux documentés (Orange Revolution…) » ; FCT ✦ « La chercheuse Lindsey O'Rourke… », « NED: créé en 1983… 31,3 M$ », « La CIA a fourni en moyenne 5 M$/an d'aide covert à l'Italie… ».

#### INV-20 — État profond FR : traduire l'objet abstrait en mécanismes vérifiables  [P2 · INVESTIGATION · (d)]
- **LEAD_QUESTION** : Que désigne « état profond » dans le débat FR (personnel, réseaux, institutions) et quels de ses mécanismes allégués sont vérifiables ?
- **OBJECT_QUESTION** : Pour chacun des mécanismes (VIGINUM vs société civile, portes tournantes, nominations, opacité administrative), quelle est la preuve positive ou l'absence démontrée ?
- **Ancrage** : `2026-09-05_etat-profond-interferences-interieures-france` (partial, hors-protocole) ; surcharge `classes` override « etat-profond → reseau ».

---

### Vague D — Boucle interne : la démocratie teste ses propres instruments

#### INV-21 — VIGINUM : débunk inverse (chercher activement un énoncé matériellement faux)  [P1 · VERIFY_ONLY · (d)]
- **LEAD_QUESTION (VMO)** : Existe-t-il un énoncé public de VIGINUM (production, rapports, communiqués) matériellement faux et documentable (correction, retrait, opposition) ?
- **Exigence** : symétrie d'exigence — même barre que l'audit des opérations qu'il cible ; aucun point n'entre au registre des « erreurs » sans correction/tiers.
- **Ancrage** : `2026-09-05_viginum-instrument-pouvoir-debunk-narratifs` ; LED-002 « H2 _VIGINUM ment_ : chercher activement un énoncé matériellement faux documenté ».

#### INV-22 — VIGINUM : cadre légal et contrôles effectifs  [P1 · INVESTIGATION · (b)]
- **LEAD_QUESTION** : Les contrôles légaux de VIGINUM (loi 2021, SSN, commission consultative, Parlement) produisent-ils des traces observables et leur efficacité est-elle évaluable ?
- **OBJECT_QUESTION** : Quels rapports/saisines/audits rendent compte du fonctionnement de VIGINUM, et que disent-ils des limites d'usage ?
- **Ancrage** : `2026-09-05_viginum-instrument-pouvoir-debunk-narratifs` ; LED-005 « Cadre légal et contrôles de VIGINUM (loi 2021, SSN, parlement) vs accusations d'ingérence interne ».

#### INV-23 — Efficacité GRECO/HATVP/registre UE/DSA-SREN  [P1 · INVESTIGATION · (b)]
- **LEAD_QUESTION** : Les dispositifs de prévention de la corruption et des ingérences produisent-ils des effets mesurables (évaluations GRECO, bilans HATVP, DSA en force) ?
- **OBJECT_QUESTION** : Quelles évaluations d'impact existent (ou brillent par leur absence) et que disent-elles du gap prévention/effets ?
- **Ancrage** : `2026-09-05_corruption-electorale-france-ue` ; CAU-004 « les mécanismes de prévention (GRECO, HATVP) existent mais leur efficacité s…».

#### INV-24 — Triche électorale : ampleur réelle des fraudes non détectées  [P1 · INVESTIGATION · (b)]
- **LEAD_QUESTION** : L'ampleur réelle du vote multiple/fraudes non détectées (inscriptions, procurations) est-elle chiffrable à partir des contentieux ?
- **OBJECT_QUESTION** : Quels contentieux/statistiques (Procurations Marseille 2020, jurisprudence) éclairent la fraude détectée — et l'absence de statistique officielle est-elle un manque informatif ?
- **Ancrage** : `2026-09-05_triche-electorale-france-ue` ; CAU-005 ; FCT ✧ « fraudes procurations Marseille 2020 condamnations », « machines à voter (vrai ou fake) ».

#### INV-25 — Voie réglementaire : suivi commission 2023 (prêts de personnes) & SREN  [P2 · VERIFY_ONLY · (b)]
- **LEAD_QUESTION (VMO)** : Les actes recommandés (interdiction des prêts de personnes) et SREN (amendes 6% CA, blocage ARCOM 48h) sont-ils mis en œuvre et contrôlés ?
- **Ancrage** : `2026-09-05_ingerences-electorales-france-ue` + `2026-09-05_manipulation-electorale-france-ue` ; ACT-004 (x2) dans `gaps.actions_pending`.

#### INV-26 — L'ingérence économique allemande (nucléaire FR) : convergence vs coordination  [P1 · INVESTIGATION · (c)]
- **LEAD_QUESTION** : La « guerre diplomatique » allemande anti-nucléaire est-elle une coordination démontrable ou une convergence d'intérêts sectoriels ?
- **OBJECT_QUESTION** : Les archives (Telos 07/2023, taxonomie, positions) étayent-elles un « sabotage délibéré » ou une politique allemande autonome ?
- **Ancrage** : `2026-09-05_ingerences-allemagne-ue-nucleaire-francais` ; CAU-004 CAU-PARTIAL « Le corpus #51 et Telos accusent une stratégie allemande anti-nucléaire… » ; FCT ✧ « sortie du nucléaire allemand… politique intérieure… la thèse d'un _sabotage délibéré_ n'est pas étayée par les archives ».

#### INV-27 — Azerbaïdjan (caviar diplomacy PACE) : au-delà de Volontè  [P1 · INVESTIGATION · (b)]
- **LEAD_QUESTION** : Les autres rémunérations (PACE, parlementaires) suivant le modèle du pot-de-vin de 500 000 EUR établi à Milan sont-elles documentables ?
- **OBJECT_QUESTION** : Quels rapports (CE, OLAF, enquêtes) existent sur la corruption parlementaire Azerbaïdjan — et que reste-t-il hors preuve ?
- **Ancrage** : `2026-09-05_ingerences-electorales-france-ue` ; FCT ✧ « caviar diplomacy Azerbaïdjan PACE » (esiweb.org/proposals/caviar-diplomacy).

#### INV-28 — ELNET : 101 voyages et l'entrée du Sénat (11/2025)  [P1 · VERIFY_ONLY + INVESTIGATION · (b)]
- **LEAD_QUESTION** : Les financements ELNET de parlementaires (101 voyages ; sommet Sénat 10/11/2025, 189 000 EUR) sont-ils déclarés/autorisés ?
- **OBJECT_QUESTION** : Quelles infractions au code de conduite du Sénat et à quels degrés de confirmation (assemblées, HATVP) l'investigation aboutit-elle ?
- **Ancrage** : `2026-09-05_infiltration-medias-politiques-france-ue` ; FCT ✦ « ELNET, lobby pro-israélien, a financé 101 voyages », FCT ✧ sommet Sénat + résolution 1000 jamais examinée.

#### INV-29 — NSO/Pegasus : la protection israélienne de l'État  [P1 · INVESTIGATION · (c)]
- **LEAD_QUESTION** : La dissimulation des liens de l'État israélien avec NSO/Pegasus (saisie 07/2020, ordonnance de non-publication) est-elle étayée ?
- **OBJECT_QUESTION** : Quelles preuves (Forbidden Stories/France Inter 2024-2026, enquête judiciaire FR) établissent un comportement d'obstruction et quel effet sur le débat ?
- **Ancrage** : `2026-09-05_ingerences-usa-soros-aipac-fondations-israel` ; CAU-004 CAU-PARTIAL « Israël protège NSO/Pegasus (dissimulation documentée, enquête judicia… » ; FCT ✧ France Inter/Forbidden Stories.

---

### Vague E — Méta / pipeline (la piste-mère : l'instrument qui modélise le négatif)

#### INV-30 — Le fait « négatif » : spécifier le type (refutations structurées = 0 actuellement)  [P2 · INVESTIGATION → design/code]
- **LEAD_QUESTION** : Quels types de faits négatifs doit produire un pipeline KERNEL (fausse allégation, absence informative, contredit, non-trouvé borné) et comment les rendre vérifiables ?
- **OBJECT_QUESTION** : Schéma de refutation (champ `refutations`), tiers terminaux du négatif, comptage honnête (le compteur `with_memory_id`/`with_url` déjà corrigé à 140/166 en 09/2025).
- **Ancrage** : cartographie `refutations == 0/167` (constat : le champ existe, jamais peuplé) ; 3 faits portant un contenu débunk non structuré.

#### INV-31 — Backlog ✧ : élévation des 48 candidats (dont les 14 des kernels `seconde-vague`/`vague3`)  [P1 · VERIFY_ONLY · (c)]
- **LEAD_QUESTION (VMO)** : Sur les 48 faits ✧ non confirmés (dont 14 dans des kernels à `classes=[]`), combien passent en ✦ (CONFIRME), restent ✧, ou tombent en contredit / absence ?
- **Traces attendues** : re-vérification source par source, write-back mémoire `✧→VERIFIE`, `✦→CONFIRME` (jamais l'inverse sans upgrade de niveau).
- **Ancrage** : `2026-09-05_seconde-vague-elevation-faits-non-confirmes` + `2026-09-05_vague3-elevation-faits-non-confirmes-restants` (7 faits chacune, `classes=[]`, exclus de la matrice par design).

#### INV-32 — Write-back mémoire : les 27 faits uk-brexit à `mem:"-"`  [P2 · opérationnel · (b)]
- **LEAD_QUESTION** : Les 27 faits du dossier uk-brexit sans lien mémoire sont-ils re-vérifiés et rebindés (origin_memory_id/origin_verified_at), ou conservés `-` pour cause d'absence ?
- **Ancrage** : `2026-09-05_uk-brexit-ingerences-manipulations-democraties` ; 27/27 `mem:"-"` (denses en contenu : Cambridge Analytica, AIQ, Banks).

---

## 3. Exécution & suivi

- Chaque INV produit un `RUN_DIR` dans `investigations/2026-09/` (`run_id = YYYYMMDD-HHMM-<slug>`), un `_INVESTIGATION.md` livré, et les gates PRE/DELIVERY via `tools/verify/verify.py`.
- Une seule investigation à la fois s'exécute en transaction (le moteur prend la INV une par une, à APEX).
- **Bascule RENARD CORE V3** : après la phase de recherche standard, tout atom dépourvu de preuve probatoire *et* d'indice/piste exploitable passe sous `_protocol_renard-core-v3.md` — `[DECOMPOSE]` → `[SHADOW]` → `TRACE/LINEAGE` → `BREAK(H)`/`[ADVERSARY]` → `UPDATE` → `[EVALUATE]`/`[REPORT]` (EPISTEMIC_LEDGER + CALIBRATION ≥ 0.7 consignés dans le run). La bascule ne modifie ni les RUN_STATE ni les gates KERNEL.
- Après delivery : mettre à jour ce plan (statut de la INV), puis régénérer la cartographie (`python3 investigations/2026-09/mapper_cartographie.py --base investigations/2026-09`) pour comptabiliser les nouveaux faits/les statuts terminaux dans la carte des preuves.
- Vérité, provenance, anti-hallucination, absence de fabrication : non négociables (cf. KERNEL FORBIDDEN).
- Outcome valide : zéro-fait INCONCLUSIVE pour une INV-* est une terminaison légitime si toutes les AXS applicables ont des tentatives et un périmètre consignés.

## 4. Ordre de lancement recommandé

- Vague A : attributions russes & argent (P0 : INV-01, 02, 03 ; P1 : 04, 05, 06, 07) → commencer par INV-03 (le cas-type « absence de preuve ≠ absence »).
- Vague B : UK Brexit (P0 : 08, 09, 11 ; P1 : 10, 12-16) → INV-09 d'abord (provenance des 8,5 M £).
- Vague C : déminage (P1 : 17, 18, 19 ; P2 : 20).
- Vague D : boucle interne (P1 : 21-24, 26-29 ; P2 : 25).
- Vague E : méta (P2 : 30-32).