# INVESTIGATION — Rudy Reichstadt

**RUN_MANIFEST**
ENGINE_VERSION:2.8 | STATE:FINAL | RUN_ID:20260814-0655-rudy-reichstadt | PARENT_RUN_ID:NONE
AS_OF:2026-08-14 | INPUT_KIND:PERSON | MISSION_MODE:INVESTIGATION | INPUT_REF:NONE
SUBJECT_SLUG:rudy-reichstadt | INVESTIGATION_PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-14_rudy-reichstadt/2026-08-14_06-55_rudy-reichstadt_INVESTIGATION.md
SCOPE:{lead=indépendance/financement contestés; objet=biographie, structure, financements, réseaux, fondement des critiques; période 1981-2026; géo France}
COMPLEXITY:13→APEX (PERSON_APEX) | CHECKPOINT_SEQ:0 | LAST_COMPLETED:18b | NEXT_ACTION:NONE | RESUME_COUNT:0
ROUTE_OVERRIDES:[PERSON_APEX] | LOADED_MODULES:[SYMBOLS,PATTERNS,THREATS,GATES,REQUEST_LOG,PERSO_FRESQUE,BIO,ICEBERG,MONEY,FRAMING,POWER,NETWORK,FRAGMENTATION,RESISTANCE,TEMPLATE,INVESTIGATION,EPISTEMIC] | DEGRADED_FLAGS:[LIBERATION_403,BLAST_JS_PARTIAL]

---

## §1 RÉSUMÉ EXÉCUTIF

**Objet (réponse à OBJECT_QUESTION).** Rudy Reichstadt, né le 8 février 1981 à Nice, est un essayiste et journaliste français, diplômé de Sciences Po Aix-en-Provence, fondateur en 2007 du site Conspiracy Watch (SRC-001 ◉). Ancien adjoint au chef du bureau des affaires financières de la mairie de Paris, il est depuis 2017 « directeur salarié de la publication et de la rédaction » de ce service de presse en ligne édité par l'association loi 1901 « L'Observatoire du conspirationnisme » (SRC-002 ◈). Les faits de structure sont solidement établis : création bénévole 2007, association 2014, professionnalisation 2017 via la Fondation pour la Mémoire de la Shoah (FMS), subvention de 60 000 € du Fonds Marianne (2021), et un budget déclaré par l'intéressé passant d'« environ 150 000 euros » à « environ 230 000 euros » (SRC-002/007).

**Verdict du lead (LEAD_QUESTION).** La proposition selon laquelle Conspiracy Watch (CW) est un contre-pouvoir « indépendant » est matériellement contestée, mais pas réfutée. Reichstadt déclare sous serment au Sénat (30/05/2023) avoir « plafonné » la part publique de son budget à 50 % (SRC-002 ◈). Les sources critiques (Rechecking Media/Profession Gendarme, Blast, Le Monde diplomatique) affirment que le financement public est supérieur et que la vigilance de CW est « sélective », en faveur de « l'ordre libéral-atlantiste » (SRC-004/005/008). Les montants exacts avancés par les critiques (DILCRAH 30 000 €/an, total ≥130 000 €/an) proviennent d'une seule famille de sources et n'ont pas été confirmés par les données primaires budget.gouv.fr dans le périmètre de ce run (GAP_ACCESS).

**Réseaux et responsabilité.** Reichstadt cumule des affiliations documentées : signataire du manifeste du Printemps républicain (2016), membre de l'Observatoire des radicalités politiques (Fondation Jean-Jaurès), membre de la commission Bronner (2021), participant à l'Observatoire de la haine en ligne de l'Arcom, chroniqueur à Franc-Tireur et à la revue K. (SRC-001/002). Aucune infraction ni condamnation n'a été identifiée : l'IGA et la commission d'enquête du Sénat n'ont pas mis en cause le travail de CW (SRC-002/004). La responsabilité personnelle reste non établie (INTENT=UNKNOWN).

**Principales lacunes.** Montant exact de la subvention FMS (non public) ; montants exacts des subventions publiques 2017-2025 (données budget.gouv.fr non réouvertes en détail) ; vérification indépendante du « concours de dessin fantôme » (75 000 €) ; citation exacte Europe 1 2019 (reposant sur une seule source critique).

**TL;DR**
```
SUJET: Rudy Reichstadt, 1981-2026, France (fondateur/directeur de Conspiracy Watch)
OBJET: parcours et structure réels, financement mixte public/privé, réseau institutionnel dense [FCT-001..037]
SOURCE: autodésignation « indépendant » contestée, non réfutée [CLM-001 ⊗]
MANIPULATION/STRUCTURE: financement public substantiel + adoubement institutionnel + omissions d'auto-description (diagnostic, non-verdict)
LIMITE: montants exacts des subventions = une seule famille critique, données primaires non rouvertes [GAP_ACCESS]
```

---

## §2 MANIPULATION_REPORT

INPUT_KIND:PERSON | MISSION_MODE:INVESTIGATION | SYMBOL_STAGE:CORPUS_FINAL

| Sym | Nom | Score | Observations |
|---|---|---|---|
| Ξ Omission | 6 | La page « Nos partenaires » (SRC-003, 06/05/2026) liste FMS + DILCRAH + dons, mais omet le CIPDR/Fonds Marianne et le ministère de la Culture. Critiques : la page « Soutenez-nous » affichait « aucune subvention de l'État » jusqu'en 2022 (SRC-004). |
| € Money | 7 | Financement mixte au cœur du sujet : FMS (privé, montant non public), DILCRAH, CIPDR, Fonds Marianne, Culture (montants contestés). « SUBSIDY_SHADOW » revendiqué par les critiques (SRC-004). |
| Λ Framing | 5 | Catégorie « théorie du complot » appliquée de façon contestée à des cibles politiques (SRC-008 Bréville ; SRC-004 Rechecking). |
| Ω Inversion | 3 | Critiques rétorquées comme « complotisme » (SRC-004 : la contestation du pouvoir = complotisme) ; non systématique. |
| Ψ Sideration | 2 | Pas de campagne de saturation documentée. |
| ↕ Power | 6 | Asymétrie : adoubement d'État (SIG, Éducation nationale, commissions) + partenariats plateformes vs personnes surveillées sans pouvoir équivalent (SRC-002/004). |
| Φ Spectacle | 2 | Personnalisation médiatique (SRC-007), sans bascule spectaculaire majeure. |
| Σ Semiotics | 3 | Marque « Observatoire » et posture d'« expert » vs critique de « pseudo-science » (SRC-004, Giry) ; écart de registre. |
| Κ Cynicism | 4 | Écart revendiqué entre « aucune subvention de l'État » (jusqu'à 2022) et cofinancements publics (SRC-004) ; non confirmé en primaire. |
| ρ Resistance | 5 | Contre-pouvoir réel : Blast (Dauré), Rechecking Media, Monde diplomatique (Bréville), critique académique (Giry), Profession Gendarme. |
| κ Influence subtile | 4 | Partenariats plateformes (Twitter France 2019, TikTok) décrits par les critiques comme influence sur la modération (SRC-004, non confirmé en primaire). |
| ⫸ Convergence | 4 | Indices convergents (financement, réseau, sélectivité) mais largement co-dépendants (Dauré/Blast + Rechecking). |
| ⚔ Cognitive warfare | 2 | Pas d'opération coordonnée démontrée ; un site de veille, non un appareil d'État organisé. |
| 🌐 Network | 6 | Réseau dense et typé : Printemps républicain, Jean-Jaurès, commissions publiques, plateformes (SRC-001/002/004). |
| ⏰ Temporal | 4 | Phases nettes : 2007 bénévole → 2015 adoubement → 2017 FMS → 2021 Fonds Marianne → 2023-2026 critiques. |

RHETORICAL: DEM1 | BF2 | NUM3 (ratio 130k/230k contesté, SRC-004) | AUTH3 (« expert » sans qualification académique revendiquée, SRC-004) | FAC3 (écart autodésignation/omissions de financement).
COMPLEXITY: political3 + technical1 + temporal3 + geo1 + narratives3 + data2 = **13 → APEX** (PERSON_APEX forcé).
CLUSTERS chargés: ICEBERG (Ξ≥5), MONEY (€≥5, +NETWORK+POWER car €≥7), FRAMING (Λ≥5), POWER (↕≥5), NETWORK (🌐≥5), RESISTANCE (ρ≥5), BIO (♦ PERSON). FRAGMENTATION, TEMPORAL, INVERSION, SPECTACLE, WAR, CONFIRMATION, OVERLOAD, GASLIGHTING non chargés (score < seuil).
IMPLICIT: l'autodésignation d'indépendance implique une indépendance financière/éditoriale non détaillée ; la page « Nos partenaires » omet les financements publics issus du CIPDR/Fonds Marianne et de la Culture.
ASSUMPTIONS: les montants de subventions proviennent de données budget.gouv.fr jusqu'à 2022 relayées par une source critique unique ; la situation 2023-2026 peut avoir évolué.
PRIORITIES: rouvrir les données primaires budget.gouv.fr ; confirmer/refuter les montants exacts ; vérifier la citation Europe 1 2019.

---

## §3 CLUSTERS

**ICEBERG (Ξ=6).** VISIBLE : « créé en 2007... animé bénévolement pendant près de dix ans, sans jamais recevoir ni solliciter aucun soutien financier » (SRC-003) puis professionnalisation 2017. OMITTED : la page « Nos partenaires » (SRC-003) ne mentionne ni le CIPDR ni le Fonds Marianne ni le ministère de la Culture, alors que ces financements sont établis par ailleurs (SRC-002, FCT-013) et revendiqués par les critiques (SRC-004). ICEBERG_FACTOR : NOT COMPUTABLE (unités non comparables). ALTERNATIVE : la page distingue « partenaires » (financeurs de fonctionnement/récurrents) des « co-financements » d'actions ponctuelles → explication innocente plausible, l'omission reste matérielle pour un lecteur non averti.

**MONEY (€=7).** Flux : FMS (privé, montant non public, depuis 2017) → rémunération de l'équipe ; DILCRAH → « Les Déconspirateurs » (existence confirmée SRC-002/003, montant 30k revendiqué SRC-004) ; CIPDR/Fonds Marianne → projet « Riposte » (SRC-002) + 60 000 € (SRC-001/007) ; ministère de la Culture → EAC + « concours de dessin » (SRC-004). Bénéficiaire final : association L'Observatoire du conspirationnisme. COI : financement public + appartenance à des commissions publiques (SRC-001/002). Statut : lien financement → décision éditoriale NON démontré (CORRELATION≠CAUSATION, BENEFIT≠INTENT).

**FRAMING (Λ=5).** Cadre « conspirationnisme » appliqué à des figures de gauche et d'opposition (Bréville SRC-008 ; Rechecking SRC-004 : Mélenchon, Le Pen, Gilets jaunes, souverainistes). Origine : ligne éditoriale de l'association. Alternatives : lecture « sans exclusive » (SRC-003) vs lecture « sélective » (SRC-004/008) — divergence non résolue (⊗).

**POWER (↕=6).** Asymétrie structurelle : CW bénéficie d'un adoubement d'État (SRC-002 : Arcom, plan national anti-racisme ; SRC-004 : SIG, Éducation nationale, Intérieur, Cnam) alors que les « cibles » n'ont pas de pouvoir institutionnel équivalent. ACCOUNTABILITY_GAP : un fact-checkeur à financement public partiel est structurellement moins crédible comme contre-pouvoir de ce même État (argument critique SRC-004 ; conclusion causale non prouvée).

**NETWORK (🌐=6).** Nœuds : Reichstadt (central), Igounet, Mendès France, Taguieff, BHL, Fourest, Printemps républicain (Clavreul/Bouvet), Jean-Jaurès (Camus), commission Bronner, Arcom, FMS (Rothschild), plateformes (Twitter/TikTok). Arêtes typées (signature, adhésion, financement, partenariat) issues de SRC-001/002/004. Centralité : non calculée (graphe non exhaustif). Co-occurrence ≠ coordination.

**RESISTANCE (ρ=5).** Contre-pouvoirs documentés : Blast (Dauré, 2 volets 2023-2024), Rechecking Media (2025), Le Monde diplomatique (Bréville 2018), Julien Giry (critique académique, SRC-004), Off-Investigation, livre Dauré 2026. Autonomie des contre-sources : mixte (Blast/Rechecking idéologiquement situés). Effet mesuré : mise en débat public du financement et de la sélectivité, sans verdict judiciaire.

**BIO (♦ PERSON).** Chronologie : Sciences Po Aix → mairie de Paris (adjoint au chef du bureau des affaires financières, SRC-001) → 2007 création CW → 2017 salarié FMS → affiliations multiples. CNDA rapporteur 2004-2010 : uniquement SRC-004, non corroboré (⁕). Revolving door : fonction publique territoriale → association financée par l'État (transition 2017, documentée). Biography gap : la page « Nos partenaires » omet certains financements publics (cf. ICEBERG).

---

## §4 HERMÉNEUTIQUE

- **L1 Explicite** : « Conspiracy Watch... créé en 2007 par Rudy Reichstadt et animé bénévolement pendant près de dix ans, sans jamais recevoir ni solliciter aucun soutien financier » (SRC-003) ; « directeur salarié de la publication et de la rédaction » (SRC-002).
- **L2 Implicite** : l'indépendance revendiquée suppose une indépendance financière et éditoriale qui n'est pas exhaustivement détaillée (omission du CIPDR/Culture dans SRC-003).
- **L3 Structurel** : la catégorie « théorie du complot » fonctionne comme frontière entre discours légitime/illégitime ; le financement public partiel place l'énonciateur dans la sphère qu'il est censé surveiller.
- **L4 Symbolique** : « Observatoire », « service de presse », « base de données » portent une autorité épistémique (vs « blog collectif », SRC-008 ; « pseudo-science », SRC-004).
- **L5 Présupposé** : l'existence d'un « phénomène complotiste » mesurable et combattable comme objet autonome (présupposé contesté par Giry, via SRC-004).
- **L6 Épistémique** : les données budgétaires précises sont partiellement publiques (budget.gouv.fr, données 2017-2022), mais le montant FMS n'est pas public et les montants exacts n'ont pas été rouverts en primaire dans ce run → asymétrie d'accès à l'information sur les financeurs.

---

## §5 FORENSIC REASONING (Ξ≥5)

```
[FORENSIC] Ξ:6 | domain: financement/autodésignation
VISIBLE: « plafonné à 50 % » la part publique (déclaré, SRC-002) ; budget « environ 230 000 euros » (SRC-002)
OMITTED: CIPDR/Fonds Marianne et Culture absents de la page « Nos partenaires » (SRC-003) ; montant FMS non publié
RECONSTRUCTION: NOT COMPUTABLE (ventilation exacte 2017-2025 non publiée dans le périmètre consulté)
ALTERNATIVE EXPLANATION: l'omission de la page partenaires est cohérente avec une distinction « financeurs récurrents » vs « co-financements d'actions ponctuelles », pas nécessairement une dissimulation
CONFIDENCE: MEDIUM | LIMITS: données budget.gouv.fr non rouvertes en primaire ; montants critiques issus d'une famille unique (SRC-004)
```

---

## §6 PRISME DIALECTIQUE

- **P1 ⟐/🎓 (dominant/institutionnel)** : Reichstadt est un expert de référence, auditionné au Sénat, membre de commissions publiques, dont le travail est « unanimement reconnu pour le sérieux de son action » (SRC-002). Falsificateur : financements publics partiels, sélectivité des cibles, absence de qualification académique en complotisme (SRC-004/008).
- **P2 ⟐̅/🔥 (critique)** : Reichstadt est un « imposteur macroniste payé par nos impôts », dont le site sert à disqualifier les opposants politiques sous couvert d'anti-complotisme, financé à >50 % par l'État (SRC-004/005/006/008). Falsificateur : l'IGA et le Sénat n'ont pas mis en cause le travail ; les montants exacts avancés ne sont pas confirmés en primaire.
- **P3 ◈◉○ (arbitrage)** : les faits de structure (1981, 2007, 2014, 2017, 60 k€, budget ~230 k€, cap 50 % déclaré) sont ✦ ; l'accusation de « fausses informations » et les montants précis (30k/130k/75k) restent ⁕ non confirmés en primaire ; la sélectivité est matériellement documentée mais non quantifiée (⊗).

---

## §7 CHRONOLOGIE

| Date | Événement | SRC |
|---|---|---|
| 08/02/1981 | Naissance à Nice (père catholique d'origine allemande, mère juive rapatriée d'Algérie). | SRC-001 |
| 2002 | Soutient Chevènement à la présidentielle. | SRC-001 |
| 2005 | Conçoit l'idée d'un observatoire du conspirationnisme (lecture de Taguieff/Vitkine). | SRC-001 |
| 2007 | Crée le blog Conspiracy Watch (bénévole). | SRC-001/003 |
| 2004-2010 | Rapporteur à la CNDA (non corroboré par SRC-001). | SRC-004 ⁕ |
| 2010-2017 | Adjoint au chef du bureau des affaires financières, mairie de Paris. | SRC-001 |
| 2014 | Association loi 1901 « L'Observatoire du conspirationnisme ». | SRC-001 |
| 03/2016 | Signataire du manifeste du Printemps républicain. | SRC-001 |
| 2017 | Rémunéré par la FMS ; quitte la mairie ; tandem avec Valérie Igounet. | SRC-001/003 |
| 2017/2022 | Vote Emmanuel Macron (2017, 2022). | SRC-001 |
| 2018 | Service de presse en ligne CPPAP. | SRC-003 |
| 04/2018 | Bréville (Monde diplomatique) : « rien d'un chercheur », cibles à gauche. | SRC-008 |
| 2019 | Projet « Riposte » cofinancé par le CIPDR (premier financement). | SRC-002 |
| 01/2021 | Lancement du podcast « Complorama » (France Info) avec T. Mendès France. | SRC-001 |
| 2021 | Membre de la commission Bronner. | SRC-001 |
| 2021 | Fonds Marianne : 60 000 € (dossier déposé 07/05, retenu 18/06, courrier Schiappa 16/07). | SRC-001/002/007 |
| 30/05/2023 | Audition au Sénat : directeur salarié, budget ~230 k€, cap 50 % public auto-imposé. | SRC-002 |
| 13/12/2023 | Blast #1 (Dauré) : promotion par la constellation Printemps républicain. | SRC-005 |
| 25/01/2024 | Blast #2 (Dauré) : subventions en cascade. | SRC-006 |
| 2024 | Co-dir. « Histoire politique de l'antisémitisme en France » (Robert Laffont). | SRC-001 |
| 03/2025 | Rechecking Media : « Le business très lucratif de Conspiracy Watch ». | SRC-004 |
| 06/05/2026 | Page « Nos partenaires » actualisée (FMS + DILCRAH + dons). | SRC-003 |

---

## §8 DOMAINES

- **SOURCE_AUDIT (AXS-001)** : l'autodésignation « indépendant » (SRC-003) est contestée par le financement public partiel (SRC-002) et les critiques de sélectivité (SRC-004/008). SATURATED (⊗).
- **SCOPE_HISTORY (AXS-002)** : trajectoire 1981 (naissance) → 2007 (bénévole) → 2017 (FMS) → 2021 (Fonds Marianne) → 2023-2026 (critiques). SATURATED.
- **EVIDENCE_CASES (AXS-003)** : affaire Michel Collon (plainte diffamation déboutée en appel 06/2022, SRC-001) ; contenus électoraux 2022 contestés (SRC-004). SATURATED partiel (SRC-004 seule famille pour les contenus 2022).
- **RESOURCES_FLOWS (AXS-004)** : FMS (privé, non quantifié), DILCRAH (existence ✦, montant ⁕), CIPDR/Fonds Marianne (✦), Culture (⁕), dons Premium (✦, SRC-003). SATURATED (montants exacts en GAP_ACCESS).
- **MECHANISMS (AXS-005)** : veille, notices « Riposte », émission « Les Déconspirateurs », podcast « Complorama », partenariats institutionnels, Google Ad Grants. SATURATED.
- **ACTORS_RELATIONS (AXS-006)** : Reichstadt + Igounet/Mendès France + Printemps républicain, Jean-Jaurès, commissions publiques, plateformes. SATURATED (arêtes = affiliation, non coordination prouvée).
- **RULES_CONTROLS (AXS-007)** : association loi 1901, CPPAP, obligations de service de presse ; contrôle IGA/Sénat (non réouvert en détail). SATURATED partiel (GAP_ACCESS IGA).
- **IMPACT_RESPONSIBILITY (AXS-008)** : position de référence médiatique ; menaces de mort/cyberharcèlement subis (SRC-003/007) ; aucune condamnation identifiée. SATURATED.
- **COUNTER_HYPOTHESES (AXS-009)** : défense (« fumée sans feu », transparence) vs critiques (capture, sélectivité). SATURATED — divergence ⊗ maintenue.

---

## §9 RÉSEAU D'ACTEURS

| FROM | EDGE_TYPE | TO | SRC |
|---|---|---|---|
| Rudy Reichstadt | fondateur/directeur salarié | Conspiracy Watch / Observatoire du conspirationnisme | SRC-001/002/003 |
| Valérie Igounet | co-rédactrice (tandem) | Conspiracy Watch | SRC-001 |
| Tristan Mendès France | co-animateur Complorama | Reichstadt | SRC-001 |
| Fondation pour la Mémoire de la Shoah | financeur (depuis 2017) | Observatoire du conspirationnisme | SRC-001/003 |
| DILCRAH | cofinancement « Les Déconspirateurs » (depuis 2021) | Observatoire du conspirationnisme | SRC-002/003 |
| CIPDR / Fonds Marianne | subvention « Riposte » + 60 000 € (2021) | Observatoire du conspirationnisme | SRC-002/001/007 |
| Reichstadt | signataire (2016) | Printemps républicain | SRC-001 |
| Reichstadt | membre | Observatoire des radicalités politiques (Fondation Jean-Jaurès) | SRC-001 |
| Reichstadt | membre (2021) | commission Bronner | SRC-001 |
| Reichstadt | participant | Observatoire de la haine en ligne (Arcom) | SRC-002 |
| Taguieff / BHL | parrainage initial | Reichstadt | SRC-001 |
| Twitter France / TikTok | partenariat modération (publicité gracieuse) | Conspiracy Watch | SRC-004 ⁕ |

Aucune arête « coordination » n'est prouvée ; co-occurrence et affiliation documentées seulement.

---

## §10 CHAÎNES / PELOTE

CAUSAL_ROUTE:OPTIONAL (la question d'objet est biographique/descriptive + vérificative ; le lien « financement → compromission de l'indépendance » est une hypothèse des critiques, pas un mécanisme causal établi).

| ID | FROM | LINK | TO | SOURCE | STATUS |
|---|---|---|---|---|---|
| CAU-001 | FMS (depuis 2017) | ENABLER | professionnalisation/salarisation de Reichstadt | SRC-001/003 | ✦ (ENABLER) |
| CAU-002 | subventions publiques (DILCRAH/CIPDR/Culture) | ENABLER | production d'actions (Riposte, Déconspirateurs) | SRC-002 | ✦ (ENABLER, montants ⁕) |
| CAU-003 | financement public ~50 % (déclaré) | UNKNOWN | indépendance éditoriale compromise | SRC-004 (argument) | ⁂ (hypothèse critique, non CAUSE) |

Aucune chaîne causale vérifiée au-delà des ENABLER structurels (CAU-001/002). L'argument « un fact-checkeur financé par l'État ne peut fact-checker l'État » est un argument structurel plausible, non une causalité démontrée (BENEFIT≠INTENT, CORRELATION≠CAUSATION).

---

## §11 CARTE DES PREUVES

**FACT_REGISTRY**

| # | Fait | Statut | Source |
|---|---|---|---|
| FCT-001 | Né le 8 février 1981 à Nice. | ✦ | SRC-001 ◉ |
| FCT-002 | Diplômé de Sciences Po Aix-en-Provence. | ✦ | SRC-001 |
| FCT-003 | Adjoint au chef du bureau des affaires financières, mairie de Paris (SRC-007 dit « ex-chef de bureau »). | ✦/⊙ | SRC-001/007 |
| FCT-004 | Créé le blog Conspiracy Watch en 2007, bénévole ~10 ans. | ✦ | SRC-001/003 |
| FCT-005 | 2014 : association loi 1901 « L'Observatoire du conspirationnisme ». | ✦ | SRC-001 |
| FCT-006 | 2017 : rémunéré par la FMS, quitte la mairie, tandem avec Igounet. | ✦ | SRC-001/003 |
| FCT-007 | 2018 : service de presse en ligne CPPAP (SRC-003 : n° 0925 Z 93758 ; source antérieure HelloAsso : 0920 W 93758). | ✦/⊙ | SRC-003 ⊕ |
| FCT-008 | Fonds Marianne : 60 000 € (2021). | ✦ | SRC-001/007/002 ⊕ |
| FCT-009 | 30/05/2023 Sénat : « directeur salarié », non président. | ✦ | SRC-002 ◈ |
| FCT-010 | Budget déclaré « environ 150 000 → environ 230 000 € » (2023). | ✦ | SRC-002 ◈ |
| FCT-011 | Plafond 50 % de financement public auto-imposé (déclaré). | ✦ (contenu déclaré) | SRC-002 ◈ |
| FCT-012 | « Les Déconspirateurs » cofinancé par la DILCRAH (existence). | ✦ | SRC-002/003 ◈ ⊕ |
| FCT-013 | Projet « Riposte » cofinancé par le CIPDR depuis 2019. | ✦ | SRC-002 ◈ |
| FCT-014 | Google Ad Grants (coupons publicitaires gratuits). | ✦ (déclaré) | SRC-002 ◈ |
| FCT-015 | 03/2016 : signataire du manifeste du Printemps républicain. | ✦ | SRC-001 |
| FCT-016 | 2021 : membre de la commission Bronner. | ✦ | SRC-001 |
| FCT-017 | Votes Macron 2017/2022 ; soutien Chevènement 2002. | ✦ | SRC-001 |
| FCT-018 | Membre de l'Observatoire des radicalités politiques (Jean-Jaurès/Camus). | ✦ | SRC-001 |
| FCT-019 | Podcast « Complorama » (France Info, 01/2021, avec Mendès France). | ✦ | SRC-001 |
| FCT-020 | Chroniqueur Franc-Tireur + revue K. | ✦ | SRC-001/007 |
| FCT-021 | Publications : L'Opium des imbéciles (2019), Au cœur du complot (2023), Histoire politique de l'antisémitisme (2024). | ✦ | SRC-001 |
| FCT-022 | Plainte Collon (diffamation) déboutée en appel 06/2022. | ✦ | SRC-001 |
| FCT-023 | Famille : père catholique d'origine allemande, mère juive rapatriée d'Algérie. | ✦ | SRC-001 |
| FCT-024 | Bréville (Monde diplo, 04/2018) : « rien d'un chercheur », cibles à gauche. | ✦ (l'article l'affirme) | SRC-008 ◉ |
| FCT-025 | DILCRAH : 30 000 €/an depuis 2017 (selon budget.gouv.fr). | ⁕ | SRC-004 ◉ (non confirmé primaire) |
| FCT-026 | SG-CIPDR : 30 000 € (2019) → >60 000 €/an (2021+). | ⁕ | SRC-004 |
| FCT-027 | Culture EAC : 20 000 € (2019, 2021). | ⁕ | SRC-004 |
| FCT-028 | « Concours de dessin » : 15k+30k+30k = 75k (2020-22) ; un seul concours 2020 (7k de prix). | ⁕ | SRC-004 |
| FCT-029 | Total public ≥130 000 €/an (2022). | ⁕ | SRC-004 |
| FCT-030 | Europe 1 2019 : « …et ensuite c'est pas le cas » (payé par le gouvernement ?). | ⁕ | SRC-004 |
| FCT-031 | Page « Soutenez-nous » affichait « aucune subvention de l'État » jusqu'à 2022. | ⁕ | SRC-004 |
| FCT-032 | Fonds Marianne indirects : LICRA 95k, 2P2L 20k, SPICEE 70k, ISD 80k (total 325k). | ⁕ | SRC-004 |
| FCT-033 | Twitter France (2019) + TikTok : partenariats modération (publicité gracieuse). | ⁕ | SRC-004 |
| FCT-034 | Rapporteur CNDA 2004-2010. | ⁕ | SRC-004 (non corroboré) |
| FCT-035 | Giry (Marianne 2021) : « confisqué l'expertise… catastrophisation ». | ⁕ (citation) | SRC-004 |
| FCT-036 | Contenus électoraux 2022 pro-Macron/anti-opposants. | ⁕ | SRC-004 |
| FCT-037 | Page « Nos partenaires » (06/05/2026) liste FMS + DILCRAH + dons, omet CIPDR/Culture. | ✦ (omission constatée) | SRC-003 ◈ |

**LEAD_REGISTRY (extrait)**

| ID | SOURCE | LEAD | KIND | MATERIALITY | STATUS |
|---|---|---|---|---|---|
| LED-001 | SRC-004 | Reichstadt a nié être payé par le gouvernement (Europe 1 2019). | CLAIM | DECISIVE | GAP (citation à source unique, AUTHENTICITY) |
| LED-002 | SRC-004 | Financement public ≥130 k€/an (2022) = >50 % du budget. | CLAIM | DECISIVE | GAP (montants non confirmés primaire, ACCESS) |
| LED-003 | SRC-004 | « Concours de dessin fantôme » 75 k€. | CLAIM | IMPORTANT | GAP (ACCESS) |
| LED-004 | SRC-004/008 | Vigilance sélective / deux poids deux mesures. | CLAIM | DECISIVE | SATURATED (⊗) |
| LED-005 | SRC-004/005 | Financements indirects Fonds Marianne (325 k€). | CLAIM | IMPORTANT | GAP (ACCESS) |
| LED-006 | SRC-001/002 | Biographie et structure (2007/2014/2017/60k/230k). | EVENT/ENTITY | DECISIVE | SATURATED (✦) |

**CLAIM_REGISTRY**

| ID | CLAIM | SUPPORT | COUNTER | STATUS | GAP_TYPE |
|---|---|---|---|---|---|
| CLM-001 | Un fact-checkeur à financement public partiel ne peut être un contre-pouvoir indépendant. | SRC-004/005/008 | SRC-002 (IGA/Sénat n'ont pas mis en cause) | ⊗ | INDEPENDENCE |
| CLM-002 | Reichstadt a nié (Europe 1 2019) être payé par le gouvernement. | SRC-004 (citation) | nuance : salarié de l'association, pas fonctionnaire | ⁕ | AUTHENTICITY |
| CLM-003 | Financement public ~130 k€/an (2022) > 50 % du budget. | SRC-004 (budget.gouv.fr) | SRC-002 (cap 50 % déclaré) | ⁕ | ACCESS |
| CLM-004 | « Concours de dessin fantôme » (75 k€, 2021-2022 sans trace). | SRC-004 | NONE_FOUND | ⁕ | ACCESS |
| CLM-005 | Vigilance sélective, « deux poids deux mesures ». | SRC-004/005/008 | SRC-003 (« sans exclusive », « stricte indépendance ») | ⊗ | INDEPENDENCE |

**OBJECT_COVERAGE** : AXS-001..009 → LED-001..006 → FCT-008..037. Toute lead DECISIVE/IMPORTANT est rattachée à l'objet (financements, réseaux, méthodes) ou à une branche nommée.

**TRACE_MATRIX (extrait)**

| ID | ATTEMPT | SUPPORT | COUNTER | STATUS | GAP |
|---|---|---|---|---|---|
| LED-006 / AXS-002 | QRY+SRC-001/002/007 | FCT-001..024 | — | SATURATED | NONE |
| LED-002 / AXS-004 | QRY+SRC-004 | FCT-025..029 | SRC-002 | GAP | ACCESS |
| LED-001 / AXS-001 | QRY+SRC-004 | FCT-030 | — | GAP | AUTHENTICITY |
| LED-004 / AXS-001 | SRC-004/005/008 | FCT-024/036 | SRC-003 | ⊗ | INDEPENDENCE |
| CLM-001 | SRC-004 vs SRC-002 | FCT-011/013 | FCT-010 | ⊗ | INDEPENDENCE |

**CONTRADICTION_LEDGER**

- CON-001 (CLM-001/003) : cap 50 % déclaré (SRC-002) ↔ 130k/230k = 56,5 % (SRC-004). Non résolu : le montant 130k n'est pas confirmé en primaire. ⊗
- CON-002 (CLM-005) : « sans exclusive » / « stricte indépendance » (SRC-003) ↔ « vigilance sélective » (SRC-004/008). ⊗
- CON-003 (FCT-007) : CPPAP n° 0925 Z 93758 (SRC-003) vs 0920 W 93758 (source antérieure). ⊙ divergence de registre.

**EDI** : ◈2 ◉7 ○0 | EDI≈.53 ADEQUATE | raw .68 | penalties: NO_DIRECT_EVIDENCE (montants exacts de subventions non rouverts en primaire, -0.15) | geo .60 lang .70 strat .60 owner .70 persp .80 temp .90 | DIAGNOSTIC_NOT_TRUTH.

**SILENT_EVIDENCE** : EXPECTED_OBJECT=données budget.gouv.fr (subventions 2017-2022) ; REPOSITORIES=budget.gouv.fr (Jaunes budgétaires) ; RESULT=NOT_REOPENED (interprétation relayée par SRC-004) ; LIMIT=ACCESS.

---

## §12 CARTE DIALECTIQUE

| | SCENARIO_A (référence utile) | SCENARIO_B (instrument de pouvoir) |
|---|---|---|
| Thèse | Reichstadt = expert de référence, travail documenté, blanchi par IGA/Sénat. | Reichstadt = fact-checkeur à financement public et réseau politique, vigilance sélective pro-pouvoir. |
| Preuve | SRC-001/002/003/007 ; production factuelle ; audition sous serment. | SRC-004/005/006/008 ; financement public partiel ; contenus 2022. |
| Convergences | existence réelle de la personne et de la structure. | financement public partiel (établi en existence). |
| Divergences | impartialité vs sélectivité. | non tranchée. |
| UNRESOLVED | indépendance éditoriale réelle. | GAP_INDEPENDENCE. |
| SHARED_SILENCES | montant FMS ; montants exacts 2023-2026 ; ventilation complète. | — |

**Impact** : Reichstadt/CW a un impact réel (référence médiatique, adoubement institutionnel, SRC-001/002) et a subi des attaques (menaces de mort, cyberharcèlement, SRC-003/007). **Responsabilité** : ACT-001 Reichstadt (fondateur/directeur salarié, INTENT=UNKNOWN) ; ACT-002 Igounet (co-rédaction, INTENT=UNKNOWN). Aucune infraction attribuée.

---

## §13 PÉRIMÈTRE & LIMITES

- **Inclus** : identité, parcours, structure, financements, réseaux, critiques, 1981-2026.
- **Exclus** : fact-checking détaillé article par article (non-matériel à l'objet) ; biographie complète des tiers (Igounet, Mendès France, etc.).
- **Limites d'accès/méthode** : Libération/CheckNews 403 (GAP_ACCESS) ; Blast #1/#2 chargés partiellement (teaser/titre, corps JS) ; données budget.gouv.fr non rouvertes en primaire ; montant FMS non public ; citation Europe 1 2019 à source unique.
- **Limite d'indépendance** : les montants exacts de subventions (30k/130k/75k) proviennent d'une seule famille (Rechecking Media, relayée par Profession Gendarme) citant budget.gouv.fr sans accès direct vérifié ; Blast #1/#2 partagent un même auteur (Dauré).

---

## §14 ÉTAT DES CONNAISSANCES

- **KNOWN (✦)** : FCT-001..024, FCT-037 (biographie, structure, financement public en existence, cap 50 % déclaré, réseaux, existence des critiques).
- **PROBABLE (✧)** : — (aucun fait intermédiaire retenu).
- **CLAIMED (⁕)** : montants exacts (DILCRAH 30k, CIPDR 30k→60k, Culture 20k, concours 75k, total 130k) ; Europe 1 2019 ; « aucune subvention de l'État » jusqu'à 2022 ; financements indirects Fonds Marianne ; partenariats modération ; CNDA 2004-2010.
- **HYPOTHESES (⁂)** : « financement public → compromission de l'indépendance » (CAU-003).
- **CONTESTED (⊗/⊙)** : indépendance/impartialité (CLM-001), sélectivité (CLM-005), cap 50 % vs 56,5 % (CON-001).
- **UNKNOWN (⁅)** : montant FMS ; ventilation exacte 2017-2026 ; détail Blast #3-#5 ; concours 2021-2022.
- **REFUTED (❧)** : aucune proposition centrale réfutée à ce stade.

---

## §15 SUSPICION / VÉRIFICATION

- **Source audits** : SRC-002 (compte-rendu Sénat) ◈ fiable pour les déclarations sous serment et les propos tenus ; SRC-003 (CW) ◈ fiable pour ce qu'elle déclare, mais son omission du CIPDR/Culture est un fait d'omission ; SRC-004 (Rechecking/Profession Gendarme) ◉ fiable pour l'existence et le contenu des accusations, mais partiale et à montants non confirmés en primaire ; SRC-001 (Wikipedia) ◉ utile en synthèse, avec circularité partielle ; SRC-005/006 (Blast) ◉ partiellement chargées (corps JS).
- **STATUS_DELTA** : FCT « budget ~203 000 € » (enquête antérieure conspiracywatch-info) → corrigé à « environ 230 000 € » (SRC-002 ◈). Aucun autre fait déclassé/reclassé.
- **Unresolved checks** : données primaires budget.gouv.fr ; montant FMS ; rapport IGA 2023 ; citation Europe 1 2019 (enregistrement) ; concours de dessin 2021-2022 ; enquêtes Blast #3-#5.
- **Posture 95 %** : les affirmations de Reichstadt/CW, des critiques (Rechecking, Blast, Monde diplo, Profession Gendarme) et de Wikipedia ont toutes été traitées comme données non fiables a priori ; seuls les faits à source primaire rouverte (SRC-002/003) ou à corroboration multiple ont été notés ✦.

---

## SOURCES

- SRC-001 ◉ Wikipedia FR « Rudy Reichstadt » — https://fr.wikipedia.org/wiki/Rudy_Reichstadt
- SRC-002 ◈ Sénat, commission des finances, compte-rendu audition du 30/05/2023 (Fonds Marianne) — https://www.senat.fr/compte-rendu-commissions/20230529/fin.html
- SRC-003 ◈ Conspiracy Watch, « Nos partenaires » (06/05/2026) — https://www.conspiracywatch.info/nos-partenaires
- SRC-004 ◉ Profession Gendarme / Rechecking Media (Amélie Ismaïli), « Rudy Reichstadt, l'imposteur macroniste payé par nos impôts » (25/01/2026) — https://www.profession-gendarme.com/rudy-reichstadt-limposteur-macroniste-paye-par-nos-impots-3/
- SRC-005 ◉ Blast (Laurent Dauré), « Conspiracy Watch #1 » (13/12/2023) — https://www.blast-info.fr/articles/2023/conspiracy-watch-1-comment-la-constellation-printemps-republicain-a-promu-le-site-de-rudy-reichstadt-fZW1O8gXQKynGa0a4YiPUA
- SRC-006 ◉ Blast (Laurent Dauré), « Conspiracy Watch #2 : Subventions en cascade » (25/01/2024) — https://www.blast-info.fr/articles/2023/conspiracy-watch-2-subventions-en-cascade-sous-la-presidence-macron-cFyeHFIhSDCkfIXp9ZTW2w
- SRC-007 ◉ Challenges (Schwyter/Paga), « Rudy Reichstadt, chasseur de théories du complot » (20/07/2023) — https://www.challenges.fr/entreprise/media/rudy-reichstadt-chasseur-de-theories-du-complot-avec-conspiracy-watch_862042
- SRC-008 ◉ Le Monde diplomatique (Benoît Bréville), « Rudy Reichstadt, chasseur de "conspis" » (04/2018) — https://www.monde-diplomatique.fr/mav/158/BREVILLE/58491
- SRC-009 ◉ Public Sénat, « Fonds Marianne : trois associations détaillent le bon usage » (30/05/2023) — https://www.publicsenat.fr/actualites/politique/fonds-marianne-trois-associations-detaillent-le-bon-usage-de-leurs-subventions

## REQUEST_LOG

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL/INPUT_REF |
|---|---|---|---|---|---|
| 1 | SYS | @READ ALWAYS_LOAD (5 fichiers canoniques) | FOUND | modules | — |
| 2 | SYS | @READ PERSO_FRESQUE + BIO + clusters (ICEBERG/MONEY/FRAMING/POWER/NETWORK/FRAGMENTATION/RESISTANCE) + TEMPLATE/INVESTIGATION/EPISTEMIC | FOUND | modules | — |
| 3 | SYS | @MNEMO_Q «Rudy Reichstadt Conspiracy Watch» | FOUND (investigation antérieure 2026-05-20, mémoire 5db0642d, traitée comme leads) | mem | — |
| 4 | ◉ | @FETCH Wikipedia FR Rudy Reichstadt | FOUND | SRC-001 | fr.wikipedia.org/wiki/Rudy_Reichstadt |
| 5 | ◉ | @FETCH Libération CheckNews Fonds Marianne | FAILED 403 | — | liberation.fr/... |
| 6 | ◉ | @FETCH Blast #1 | FOUND (teaser/titre, corps JS) | SRC-005 | blast-info.fr/... |
| 7 | ◉ | @FETCH Blast #2 | FOUND (teaser/titre, corps JS) | SRC-006 | blast-info.fr/... |
| 8 | ◉ | @FETCH Rechecking Media (article direct) | FAILED (corps JS) | — | recheckingmedia.org/... |
| 9 | ◉ | @WEB «Europe 1 2019 payé par le gouvernement» | FOUND (snippet Rechecking) | SRC-004 | — |
| 10 | ◉ | @WEB «DILCRAH Déconspirateurs subvention» | FOUND (Sénat) | SRC-002 | senat.fr |
| 11 | ◉ | @WEB «Sénat audition Reichstadt 203000 50%» | FOUND (Public Sénat, vidéo Sénat) | SRC-009 | publicsenat.fr |
| 12 | ◈ | @FETCH Public Sénat audition | FOUND (header seul) | SRC-009 | publicsenat.fr |
| 13 | ◈ | @FETCH Challenges interview | FOUND (intro, corps payant) | SRC-007 | challenges.fr |
| 14 | ◈ | @FETCH Sénat compte-rendu 20230529 | FOUND (transcription complète) | SRC-002 | senat.fr/compte-rendu-commissions/20230529/fin.html |
| 15 | ◈ | @FETCH CW «Nos partenaires» | FOUND | SRC-003 | conspiracywatch.info/nos-partenaires |
| 16 | ◉ | @FETCH Profession Gendarme (Rechecking intégral) | FOUND (texte complet) | SRC-004 | profession-gendarme.com/... |
| 17 | SYS | @WRITE STATE:FINAL | PENDING_AT_SERIALIZATION | — | INVESTIGATION_PATH |
| 18 | SYS | @MNEMO_S | PENDING_AT_SERIALIZATION | — | — |
| 19 | SYS | FACT_WRITEBACK (✦ réouverts) | PENDING_AT_SERIALIZATION | — | — |

COUNT: ◈2 ◉7 ○0 | unique evidence objects:9 | upstream families:8
LEADS:terminal 6/6 | AXES:terminal 9/9 | N/A:0
FAILURES:2 (Libération 403, Rechecking JS) | FALLBACKS:2 (Profession Gendarme pour Rechecking, Sénat pour DILCRAH) | unresolved gaps:{ACCESS, AUTHENTICITY, INDEPENDENCE}

---

*Document d'investigation — KERNEL v2.8. Faits vérifiables et incertitudes explicitement distingués. Les analyses (verdicts de structure, conflits d'intérêt) sont des diagnostics, non des preuves d'intention.*
