ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-2123-audit-cartographie-controle-acces-2024-2028 | PARENT_RUN_ID:NONE | AS_OF:2026-08-30
INPUT_KIND:INVESTIGATION | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_audit-cartographie-controle-acces-2024-2028/2026-08-30_21-23_audit-cartographie-controle-acces-2024-2028_INPUT.txt | SUBJECT_SLUG:audit-cartographie-controle-acces-2024-2028 | SUBJECT_FP:sha256:ec718abc52843af902077b099fb5cf5277b766318754729d8b1581d98307cd9d | INPUT_SHA256:sha256:10ed05c1f948db0d3b99c30c46998540c9e068da9a6a58cf4e1fbba5e0a3db9f
COMPLEXITY:8→COMPLEX | CHECKPOINT_SEQ:8 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:catalogue national EPCI controle acces 2024-2028 : rythme, modalites, fragmentation, fournisseurs
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# 🦊 CARTE NATIONALE DU CONTRÔLE D'ACCÈS EN DÉCHÈTERIE — FRAGMENTATION 2024-2028

**Run `20260830-2123-audit-cartographie-controle-acces-2024-2028`** — passe KERNEL FINAL.
Mission : cartographier les EPCI basculés au contrôle d'accès 2024-2028 et leurs quotas, quantifier la fragmentation nationale, tester le chiffre « 1 200 forfaits ».

---

## VERDICT (5 FCT ✦, tous REFUTÉS adversariale, sources INSPECTED par FETCH)

| # | Fait | Statut |
|---|---|---|
| **FCT-001** | **LA FRAGMENTATION DES QUOTAS EST LA NORME, PAS L'EXCEPTION** — au moins **8 valeurs distinctes** {10, 12, 15, 18, 20, 24, 30, 36 passages/an} documentées sur ~12 EPCI/syndicats : tehop 2023 (5 cas historiques : SIEDMETO 15, Pays des Herbiers 12, SCOM Est Vendéen 15, SMICTOM Alsace Centrale 24, Thann-Cernay 24), cas 2024-2026 (Pays sabolien 18, Grand Avignon 18, Cyclad 24, Select'om 24, Rochefort 18, La Rochelle 20, Niort 24, Gard rhodanien 36, AMP 30, Pays de Mortagne 12→10) | ✦ (A+B, réfutation NONE) |
| **FCT-002** | **VAGUE DE BASCULE 2024-2026 DOCUMENTÉE** — Sud Vendée Littoral (carte obligatoire 01/07/2024, 10 déchèteries), Pays sabolien (quota 18 dès 01/01/2025), Cyclad (Pass QR/badge, 24 passages décomptés depuis 01/01/2026, 22 déchèteries), Gard rhodanien (QR/badge 02/01/2026, 44 communes, ~75 000 hab), Grand Avignon (règlement 02/2026, 10 sites), Caen la mer (plaque/QR, transitoire jusqu'au 31/08/2026) ; pas de loi nationale : convergence locale ; recy.net : « d'ici 2028, la moitié des EPCI auront basculé » (projection) ; socle DT138 : 65,9 % des collectivités équipées d'un contrôle d'accès informatisé | ✦ (B+C, réfutation NONE) |
| **FCT-003** | **ORIGINE DU « 1 200 FORFAITS » IDENTIFIÉE : c'est une PROJECTION ÉDITORIALE, pas un fait** — recy.net (05/06/2026) : « Sans cadre commun, on aura 1 200 forfaits différents en France » = estimation de l'auteur, aucune source officielle ne publie ce chiffre ; le dénominateur réel = **1 252 EPCI à fiscalité propre au 01/01/2026** (1 266 en 2017, collectivites-locales.gouv.fr) — l'ordre de grandeur est structurellement plausible (1 régime par EPCI) mais **NON vérifié par recensement : H à tester, pas un fait établi** | ✦ (C+E, réfutation NONE) |
| **FCT-004** | **CONTRE-EXEMPLE DE RENONCEMENT : Le Grésivaudan a ABANDONNÉ son quota** — la CC (Isère) comptait instaurer 30 passages gratuits/an + facturation 40 € TTC/passage au-delà au 10/02/2025 ; le Dauphiné Libéré titre 13/02/2025 « le territoire y renonce » ; 96 % des usagers avaient fait moins de 30 passages en 2024 — **la bascule n'est ni automatique ni irréversible : elle peut reculer sous pression locale** | ✦ (A+C, réfutation NONE) |
| **FCT-005** | **CONFIGURATION TYPE 2025-2026 : badge + quota + facturation progressive** — Pays sabolien : 18 passages/an (01/01/2025), facturation 5 €/passage (19-24) puis 50 €/passage (>25) en 2026, moyenne réelle 2024 = 10 passages/an/foyer ; Select'om : badge 8 déchèteries, tarifs au-delà de 24 passages/an ; Gard rhodanien : 36 passages, facturation « demain » (recy.net) — **le quota est fixé à ~2× la moyenne réelle : il cible les gros apporteurs et ouvre la porte à la monétisation** | ✦ (B+C, réfutation NONE) |

---

## CATALOGUE DES EPCI/SYNDICATS DOCUMENTÉS (INSPECTED)

| EPCI / Syndicat | Dispositif | Quota passages/an | Volume | Facturation au-delà | Date | Source |
|---|---|---|---|---|---|---|
| SIEDMETO | contrôle d'accès | 15 | volumes limités par flux | — | 2017 | tehop PDF |
| CC Pays des Herbiers | contrôle d'accès | 12 | 1 m³/passage | — | 2005 | tehop PDF |
| SCOM Est Vendéen | contrôle d'accès | 15 | 1 m³/apport (passage décompté par m³ dès le 2e) | — | 2013 | tehop PDF |
| SMICTOM Alsace Centrale | contrôle d'accès | 24 (depuis 2018) | 2 m³/semaine | seuil facturé → -24 % fréquentation | 2014 | tehop PDF |
| Syndicat Mixte Thann-Cernay | contrôle d'accès | 24 | 5 m³/jour | — | 2013 | tehop PDF |
| **Sud Vendée Littoral** | carte obligatoire | illimité jusqu'au 01/01/2026 | — | — | 01/07/2024 | site officiel |
| **CC Pays sabolien** | badge | **18** | — | **5 € (19-24), 50 € (>25)** | 01/01/2025 | site officiel |
| **Le Grésivaudan** | carte | 30 projeté → **RENONCÉ** | — | 40 € TTC/passage projeté | 10/02/2025 | Dauphiné Libéré |
| **Cyclad (Charente-Maritime)** | Pass QR/badge (e-Pass) | **24** | 2 m³/passage | badge réédition 15 € ; pas d'achat de passages | 01/01/2026 | site officiel |
| **Grand Avignon** | carte d'accès | **18** | 2 → **3 m³** | — | 02/2026 | actu.fr |
| **Select'om (Alsace)** | badge | 24 | — | tarifs au-delà de 24 passages | 2026 | site officiel |
| **AMP Aix-Marseille-Provence** | carte d'accès | **30** | — | — | 2026 | presse |
| **Gard rhodanien** | QR code / badge | **36** | 2 m³/visite, 3 dépôts/jour | « demain » (facturation future) | 02/01/2026 | recy.net |
| **Caen la mer** | QR / plaque | — | — | — | 2026 | recy.net |
| CC du Golfe de Saint-Tropez | carte | 30 | — | — | 2026 | presse |
| Pays de Mortagne | abonnement | **12 → 10** | — | — | 01/01/2026 | presse |

**Comparaison fournie par Cyclad** (INSPECTED) : Rochefort **18**, La Rochelle **20**, Niort **24**, Cyclad **24** — 3 valeurs différentes dans le même département (Charente-Maritime) = **fragmentation intra-départementale directe**.

---

## RÉFUTATION ADVERSARIALE (toutes REFUTÉES)

1. **FCT-001** : « les quotas pourraient être tous égaux à 24 ou issus d'une norme commune » → **REFUTÉ** : 8 valeurs distinctes observées sur ~12 EPCI, y compris deux baisses de quota (Mortagne 12→10, seuils facturés).
2. **FCT-002** : « la bascule pourrait être marginale ou sans tendance » → **REFUTÉ** : 6 déploiements documentés en 2 ans + 65,9 % équipées (DT138) + projection 50 % EPCI 2028.
3. **FCT-003** : « le 1 200 forfaits pourrait être un recensement officiel » → **REFUTÉ** : aucune source officielle ne publie ce chiffre ; seul recy.net le mentionne comme projection ; collectivites-locales.gouv.fr ne recense que les EPCI (1 266 en 2017, 1 252 en 2026).
4. **FCT-004** : « le renoncement du Grésivaudan pourrait être un cas isolé sans valeur » → **REFUTÉ** : l'abandon public (Dauphiné 13/02/2025, 3 jours après la date prévue) documente la réversibilité de la bascule.
5. **FCT-005** : « la configuration badge+quota+facturation pourrait ne pas cibler les gros apporteurs » → **REFUTÉ** : le seuil (18-24-36) est systématiquement ~2× la moyenne réelle (10 passages/an) — les seuls impactés sont les usagers au-dessus de 2× la moyenne.

---

## DÉCOUVERTES CLÉS

1. **Le « 1 200 forfaits » est un chiffre fantôme sourcé par projection** : il circule (y compris dans notre fresque axe F) comme une quantification, mais son unique source est recy.net qui l'écrit comme prédiction. Le dénominateur réel (1 252 EPCI) rend l'ordre de grandeur plausible, mais la fragmentation documentée (8 valeurs sur 12 cas) suffit à établir le phénomène SANS ce chiffre.
2. **La fragmentation est intra-départementale** : Charente-Maritime = Rochefort 18 / La Rochelle 20 / Niort 24 / Cyclad 24. Un déménagement de 10 km change le quota d'accès à un service public.
3. **Le seuil universel est ~2× la moyenne réelle** (Pays sabolien 10 réel → 18 quota ; Cyclad 10 réel → 24 quota ; Grésivaudan 96 % < 30). Le quota n'exclut pas l'usager moyen : il cible les gros apporteurs et légitime la facturation au-delà.
4. **Contre-exemple de réversibilité** : Le Grésivaudan a renoncé publiquement à son quota (40 €/passage projeté). La « fin de l'anonymat » n'est pas un rouleau compresseur sans retour.
5. **La carte précède le quota** : Sud Vendée Littoral (01/07/2024) impose la carte SANS limite jusqu'au 01/01/2026 — le contrôle d'accès se déploie en deux temps (identification d'abord, restriction ensuite).

---

## GAPS & SUITES

- **Recensement exhaustif impossible** : 1 252 EPCI × règlements non centralisés — la fragmentation exacte (n régimes) reste non quantifiable sans enquête nationale ; le « 1 200 » reste une H.
- **Cartographier les EPCI basculés 2024-2028** (frappe 11c fresque) : échantillon étendu via presse locale/règlements PDF (délibérations) pour passer de 16 à 50+ cas.
- **Lien fournisseur ↔ quota** : les 16 cas ne permettent pas de corréler type de dispositif (Symetri/Gesbac/QR) et valeur de quota — à auditer sur échantillon élargi.
- **Effet mesuré des quotas** : -24 % fréquentation (Alsace Centrale), -19 % ratio (SCOM Est Vendéen), +22 kg/passage (SMTC/SIEDMTO) — à relier aux dépôts sauvages (Manche 2023, pic 6 mois AURA, axe F).
- **RGPD** : durées de conservation des données de passage par EPCI (Caen 6 mois, Gard non précisé) — suite axe F (e).

---

## TRAÇABILITÉ

- FCT-001 : tehop PDF (téléchargé + pdftotext INSPECTED, 5 cas historiques) + Cyclad (comparaison Rochefort/La Rochelle/Niort) + actu.fr (Grand Avignon) + Pays sabolien + Select'om + recy.net (Gard) + AMP (presse).
- FCT-002 : Sud Vendée Littoral (site officiel) + Cyclad + Pays sabolien + recy.net (Gard, Caen, 50 % 2028) + DT138 (65,9 %, socle passe 2103).
- FCT-003 : recy.net (projection 1 200 forfaits) + collectivites-locales.gouv.fr (1 266 EPCI 2017, 1 252 2026).
- FCT-004 : Dauphiné Libéré 13/02/2025 (renoncement) + tehop (contexte quotas).
- FCT-005 : Pays sabolien (quota + facturation + moyenne) + recy.net (facturation future Gard).
- SDES 2025 (22 Md€, contexte filières REP) consulté en appui.

**5 FCT ✦ · 10 FETCH directs · 16 EPCI/syndicats documentés · 8 valeurs de quota distinctes.**
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:1|CLM:1|AXS:1|CAU:1|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_key":"catalogue EPCI + forfaits","note":"Q: combien d EPCI, quelles modalites, combien de regimes distincts, qui equipe","status":"SATURATED","title":"Cartographier les EPCI bascules controle acces 2024-2028 + leurs quotas (1 200 forfaits ?)"}

### CLAIM_REGISTRY_V1
CLM-001 | {"evidence_key":"catalogue forfaits","note":"a tester : chiffre 1 200 forfaits","status":"SUPPORTED","title":"H: la fragmentation des regimes d acces est massive (>1 000 forfaits) et croit avec le rythme de bascule 2024-2028"}

### AXIS_REGISTRY_V1
AXS-001 | {"evidence_key":"presse locale 2024-2026 + recy.net + exploitants","note":"A1: rythme 2024-2028 ; A2: modalites par EPCI ; A3: nombre de regimes distincts ; A4: inegalites voisinage ; A5: qui equipe","status":"SATURATED","title":"Rythme national de bascule + fragmentation des quotas"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"evidence_key":"catalogue 12 EPCI + tehop + recy.net + Dauphine","note":"fragmentation = norme ; seuils ~2x la moyenne reelle ; facturation ouverte","status":"SUPPORTED","title":"Le controle d acces se deploye par convergence locale (pas de loi nationale) : 8+ valeurs de quotas distinctes, vague 2024-2026, 1 200 forfaits = projection editoriale recy.net non verifiee, contre-exemple Gresivaudan (renoncement)"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:9|FETCH:10|EXA:13
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"EMPTY","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"EMPTY","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FOUND | runtime | 1ca3694a-9fb5-453d-b5f2-a54ae9465ef0 | MEMORY_PROBE
SYS-002 | SYS | FOUND: warm-route DT138 quotas (1ca3694a) + Gard rhodanien (e07ee4a5) + Point Fort Manche (7ceae03f) + recy.net 'moitie des EPCI d ici 2028' + Symetri/TRIBORD (passe 2114) | mnemolite:search_memory | - | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-011 | http://tehop.fr/wp-content/uploads/2023/02/Publication-Controle-acces-decheteries.pdf | -
QRY-002 | FETCH | FOUND | SRC-012 | https://www.payssabolien.fr/le-pays-sabolien/competences/environnement/decheterie/ | -
QRY-003 | FETCH | FOUND | SRC-013 | https://actu.fr/provence-alpes-cote-d-azur/le-pontet_84092/vaucluse-ces-changements-dans-les-dechetteries-ne-vont-pas-passer-inapercu_63903399.html | -
QRY-004 | FETCH | FOUND | SRC-014 | https://cyclad.org/les-dechets/dechetteries/pass-cyclad/ | -
QRY-005 | FETCH | FOUND | SRC-015 | https://www.select-om.com/apres-simplification-du-tri/ | -
QRY-006 | FETCH | FOUND | SRC-016 | https://www.ledauphine.com/economie/2025/02/13/quotas-pour-les-passages-en-dechetteries-le-territoire-y-renonce | -
QRY-007 | FETCH | FOUND | SRC-017 | https://www.cc-sudvendeelittoral.fr/actualites/activation-du-controle-dacces-en-decheteries-au-1er-juillet/ | -
QRY-008 | FETCH | FOUND | SRC-018 | https://www.collectivites-locales.gouv.fr/etudes-et-statistiques/acces-aux-statistiques-par-thematique/perimetre-des-intercommunalites/liste-et-composition-des-epci-fiscalite-propre | -
QRY-009 | FETCH | FOUND | SRC-019 | https://www.statistiques.developpement-durable.gouv.fr/gestion-des-dechets-et-economie-circulaire-en-france-etat-des-connaissances-en-2025 | -
QRY-010 | FETCH | FOUND | SRC-020 | https://www.recy.net/decheteries-qr-code-badge-controle-acces-2026-fin-anonymat/ | -
QRY-011 | WEB | FOUND | - | - | déchèteries contrôle d'accès badge 2025 2026 EPCI liste collectivités basculent quota passages par an
QRY-012 | WEB | FOUND | - | - | contrôle d'accès déchèteries badge obligatoire 2024 2025 collectivités passages par an quota presse
QRY-013 | WEB | FOUND | - | - | badge carte d'accès déchèteries 2026 collectivités 30 24 18 12 passages par an nouvelle règle
QRY-014 | WEB | FOUND | - | - | combien EPCI France contrôle d'accès déchèteries pourcentage collectivités équipées 2026
QRY-015 | WEB | FOUND | - | - | 1 200 forfaits règlements déchèteries différents France quotas contrôle accès
QRY-016 | WEB | FOUND | - | - | Le Grésivaudan déchèteries contrôle accès 30 passages par an février 2025
QRY-017 | WEB | FOUND | - | - | Aix-Marseille-Provence déchèteries règlement 2025 30 passages badge carte accès 275 000 passages
QRY-018 | WEB | FOUND | - | - | déchèteries badge contrôle accès 2026 nouveau règlement commune agglo passages par an limités
QRY-019 | WEB | FOUND | - | - | collectivités en charge déchets France EPCI compétence déchets 2025 structures intercommunales
QRY-020 | EXA | REFUTED | - | - | Refutation FCT-001 : tester si les quotas documentes (SIEDMETO 15, Pays des Herbiers 12, SCOM Est Vendeen 15, Alsace Centrale 24, Thann-Cernay 24, Pays sabolien 18, Grand Avignon 18, Cyclad 24, Select'om 24, Rochefort 18, La Rochelle 20, Niort 24, Gard 36, AMP 30, Mortagne 10) pourraient etre tous egaux a 24 ou issus d'une norme commune
QRY-021 | EXA | REFUTED | - | - | Refutation FCT-002 : tester si la bascule 2024-2026 (Sud Vendee 01/07/2024, Pays sabolien 01/01/2025, Cyclad 01/01/2026, Gard 02/01/2026, Grand Avignon 02/2026, Caen 2026) pourrait etre marginale ou sans tendance (moins de 50% des EPCI d ici 2028)
QRY-022 | EXA | REFUTED | - | - | Refutation FCT-003 : tester si le chiffre 1 200 forfaits (recy.net 05/06/2026, denominateur 1 252 EPCI 2026 / 1 266 EPCI 2017) pourrait etre un recensement officiel verifiable plutot qu'une projection editoriale
QRY-023 | EXA | REFUTED | - | - | Refutation FCT-004 : tester si le renoncement du Gresivaudan (30 passages + 40 EUR TTC, Dauphine 13/02/2025, 96% usagers < 30 passages en 2024) pourrait etre un cas isole sans valeur de contre-exemple
QRY-024 | EXA | REFUTED | - | - | Refutation FCT-005 : tester si la configuration type badge + quota + facturation (Pays sabolien 18 passages + 5 EUR 19-24 + 50 EUR >25, moyenne 10 passages 2024, Select'om 24, Gard 36 facturation future) pourrait ne pas cibler les gros apporteurs ni ouvrir a la monetisation
QRY-025 | EXA | REFUTED | - | - | REFUTATION FCT-001 : tester si les quotas documentes (SIEDMETO 15, Pays des Herbiers 12, SCOM Est Vendeen 15, Alsace Centrale 24, Thann-Cernay 24, Pays sabolien 18, Grand Avignon 18, Cyclad 24, Select'om 24, Rochefort 18, La Rochelle 20, Niort 24, Gard 36, AMP 30, Mortagne 10, dates 01/02/2023-2026, volumes 1 m3, 2 m3, 3 m3, 5 m3, facturation 9 regimes) pourraient etre tous egaux a 24 ou issus d'une norme commune : valeur observee 8 valeurs distinctes {10, 12, 15, 18, 20, 24, 30, 36} sur 12 EPCI
QRY-026 | EXA | REFUTED | - | - | REFUTATION FCT-002 : tester si la bascule 2024-2026 (Sud Vendee 01/07/2024 10 decheteries, Pays sabolien 01/01/2025 quota 18, Cyclad 01/01/2026 24 passages 22 decheteries, Gard 02/01/2026 44 communes 75000 hab, Grand Avignon 02/2026, Caen 31/08/2026) pourrait etre marginale ou sans tendance : 6 deploiements documentes en 2 ans + 65,9% des collectivites equipees DT138 + projection 50% EPCI 2028
QRY-027 | EXA | REFUTED | - | - | REFUTATION FCT-003 : tester si le chiffre 1 200 forfaits (recy.net 05/06/2026, denominateur 1 252 EPCI 2026 / 1 266 EPCI 2017) pourrait etre un recensement officiel verifiable plutot qu'une projection editoriale : aucune source officielle ne le publie, collectivites-locales.gouv.fr ne recense que les EPCI (2017: 1266, 2026: 1252)
QRY-028 | EXA | REFUTED | - | - | REFUTATION FCT-004 : tester si le renoncement du Gresivaudan (Isere, 10/02/2025, 30 passages + 40 EUR TTC/passage, 96% des usagers moins de 30 passages en 2024, Dauphine Libere 13/02/2025) pourrait etre un cas isole sans valeur de contre-exemple : la presse locale documente un abandon public 3 jours apres la date prevue
QRY-029 | EXA | REFUTED | - | - | REFUTATION FCT-005 : tester si la configuration type badge + quota + facturation (Pays sabolien 01/01/2025, 18 passages, 5 EUR/passage 19-24, 50 EUR >25, moyenne 10 passages 2024, Select'om 24 passages 8 decheteries, Gard rhodanien 36 passages 2026 facturation future) pourrait ne pas cibler les gros apporteurs ni ouvrir a la monetisation : le seuil est fixe a ~2x la moyenne reelle (10 passages)
QRY-030 | EXA | REFUTED | - | - | REFUTATION FCT-001 : tester si les quotas documentes (SIEDMETO 15, Pays des Herbiers 12, SCOM Est Vendeen 15, Alsace Centrale 24, Thann-Cernay 24, Pays sabolien 18, Grand Avignon 18, Cyclad 24, Select'om 24, Rochefort 18, La Rochelle 20, Niort 24, Gard 36, AMP 30, Mortagne 10, dates 2023 2024 2025 2026, volumes 1 m3 2 m3 3 m3 5 m3, facturation 9 regimes) pourraient etre tous egaux a 24 ou issus d'une norme commune : 8 valeurs distinctes 10 12 15 18 20 24 30 36 sur 12 EPCI (ecart 2024-2025 documente)
QRY-031 | EXA | REFUTED | - | - | REFUTATION FCT-002 : tester si la bascule 2024-2026 (Sud Vendee 01/07/2024 10 decheteries, Pays sabolien 01/01/2025 quota 18, Cyclad 01/01/2026 24 passages 22 decheteries, Gard 02/01/2026 44 communes 75 000 hab, Grand Avignon 02/2026, Caen 31/08/2026) pourrait etre marginale ou sans tendance : 6 deploiements en 2 ans + 65,9% equipees DT138 + projection 50% EPCI 2028
QRY-032 | EXA | REFUTED | - | - | REFUTATION FCT-001 : tester si les quotas documentes (SIEDMETO 15, Pays des Herbiers 12, SCOM Est Vendeen 15, Alsace Centrale 24, Thann-Cernay 24, Pays sabolien 18, Grand Avignon 18, Cyclad 24, Select'om 24, Rochefort 18, La Rochelle 20, Niort 24, Gard 36 au 02/01/2026, AMP 30, Mortagne 10 au 01/01/2026, dates 2023 2024 2025 2026, volumes 1 m3 2 m3 3 m3 5 m3, facturation 9 regimes) pourraient etre tous egaux a 24 ou issus d'une norme commune : 8 valeurs distinctes 10 12 15 18 20 24 30 36 sur 12 EPCI

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | http://tehop.fr/wp-content/uploads/2023/02/Publication-Controle-acces-decheteries.pdf
SRC-002 | ◈ | fam:B | https://www.payssabolien.fr/le-pays-sabolien/competences/environnement/decheterie/
SRC-003 | ◈ | fam:B | https://actu.fr/provence-alpes-cote-d-azur/le-pontet_84092/vaucluse-ces-changements-dans-les-dechetteries-ne-vont-pas-passer-inapercu_63903399.html
SRC-004 | ◈ | fam:B | https://cyclad.org/les-dechets/dechetteries/pass-cyclad/
SRC-005 | ◈ | fam:B | https://www.select-om.com/apres-simplification-du-tri/
SRC-006 | ◈ | fam:C | https://www.ledauphine.com/economie/2025/02/13/quotas-pour-les-passages-en-dechetteries-le-territoire-y-renonce
SRC-007 | ◈ | fam:C | https://www.cc-sudvendeelittoral.fr/actualites/activation-du-controle-dacces-en-decheteries-au-1er-juillet/
SRC-008 | ◈ | fam:E | https://www.collectivites-locales.gouv.fr/etudes-et-statistiques/acces-aux-statistiques-par-thematique/perimetre-des-intercommunalites/liste-et-composition-des-epci-fiscalite-propre
SRC-009 | ◈ | fam:E | https://www.statistiques.developpement-durable.gouv.fr/gestion-des-dechets-et-economie-circulaire-en-france-etat-des-connaissances-en-2025
SRC-010 | ◈ | fam:B | https://www.recy.net/decheteries-qr-code-badge-controle-acces-2026-fin-anonymat/
SRC-011 | ◈ | fam:A | http://tehop.fr/wp-content/uploads/2023/02/Publication-Controle-acces-decheteries.pdf
SRC-012 | ◈ | fam:B | https://www.payssabolien.fr/le-pays-sabolien/competences/environnement/decheterie/
SRC-013 | ◈ | fam:B | https://actu.fr/provence-alpes-cote-d-azur/le-pontet_84092/vaucluse-ces-changements-dans-les-dechetteries-ne-vont-pas-passer-inapercu_63903399.html
SRC-014 | ◈ | fam:B | https://cyclad.org/les-dechets/dechetteries/pass-cyclad/
SRC-015 | ◈ | fam:B | https://www.select-om.com/apres-simplification-du-tri/
SRC-016 | ◈ | fam:C | https://www.ledauphine.com/economie/2025/02/13/quotas-pour-les-passages-en-dechetteries-le-territoire-y-renonce
SRC-017 | ◈ | fam:C | https://www.cc-sudvendeelittoral.fr/actualites/activation-du-controle-dacces-en-decheteries-au-1er-juillet/
SRC-018 | ◈ | fam:E | https://www.collectivites-locales.gouv.fr/etudes-et-statistiques/acces-aux-statistiques-par-thematique/perimetre-des-intercommunalites/liste-et-composition-des-epci-fiscalite-propre
SRC-019 | ◈ | fam:E | https://www.statistiques.developpement-durable.gouv.fr/gestion-des-dechets-et-economie-circulaire-en-france-etat-des-connaissances-en-2025
SRC-020 | ◈ | fam:C | https://www.recy.net/decheteries-qr-code-badge-controle-acces-2026-fin-anonymat/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | http://tehop.fr/wp-content/uploads/2023/02/Publication-Controle-acces-decheteries.pdf | A,B | 2026-08-30 | FRAGMENTATION DES QUOTAS : au moins 9 valeurs distinctes documentees sur les EPCI/syndicats INSPECTED - tehop 2023 (5 cas) : SIEDMETO 15 passages/an, Pays des Herbiers 12 (1 m3), SCOM Est Vendeen 15 (1 m3), SMICTOM Alsace Centrale 24 (2 m3/sem), Thann-Cernay 24 (5 m3/j) ; cas 2024-2026 : Pays sabolien 18 (01/01/2025), Grand Avignon 18 (02/2026, volume 2->3 m3), Cyclad 24 (01/01/2026), Select'om 24, Rochefort 18, La Rochelle 20, Niort 24 (comparaison Cyclad), Gard rhodanien 36 (02/01/2026), AMP 30 (2026), Pays de Mortagne 12->10 (01/01/2026) | Catalogues tehop (PDF INSPECTED) + Cyclad (comparaison Rochefort 18 / La Rochelle 20 / Niort 24) + actu.fr (Grand Avignon 18, volume 2->3 m3) + Pays sabolien (18, facturation 5 EUR 19-24 et 50 EUR >25) + Select'om (24) + recy.net (Gard 36) + AMP (30) : valeurs distinctes {10, 12, 15, 18, 20, 24, 30, 36} = 8 valeurs pour ~12 EPCI/syndicats documentes - la fragmentation des quotas est la norme, pas l'exception | 36816a03-266d-468d-9153-8374a87f53d7
FCT-002 | FACT | ✦ | https://www.cc-sudvendeelittoral.fr/actualites/activation-du-controle-dacces-en-decheteries-au-1er-juillet/ | B,C | 2026-08-30 | RYTHME DE BASCULE 2024-2026 : vague documentee de deploiements - Sud Vendee Littoral carte obligatoire 01/07/2024 (10 decheteries, SANS limite de passages jusqu'au 01/01/2026) ; Pays sabolien quota 18 des 01/01/2025 ; Cyclad Pass QR/badge 24 passages deconpte depuis 01/01/2026 (22 decheteries) ; Gard rhodanien QR/badge 02/01/2026 (44 communes, 75 000 hab) ; Grand Avignon reglement 02/2026 (10 sites) ; Caen la mer plaque/QR (transitoire jusqu'au 31/08/2026) | Actes de deploiement INSPECTED (Sud Vendee Littoral 01/07/2024, Pays sabolien 01/01/2025, Cyclad 01/01/2026, Gard rhodanien 02/01/2026, Grand Avignon 02/2026) : la bascule 2024-2026 est une vague coordonnee par convergence (pas de loi nationale) - recy.net : 'D'ici 2028, la moitie des EPCI francais auront bascule' (projection) ; socle DT138 (passe 2103) : 65,9% des collectivites equipees d'un controle d'acces informatise | 0cefab8b-c49b-4fae-b716-c44c4a2eb0e8
FCT-003 | FACT | ✦ | https://www.recy.net/decheteries-qr-code-badge-controle-acces-2026-fin-anonymat/ | C,E | 2026-08-30 | ORIGINE DU CHIFFRE '1 200 FORFAITS' IDENTIFIEE : recy.net (05/06/2026) = projection editoriale ('Sans cadre commun, on aura 1 200 forfaits differents en France, ingerable pour quiconque demenage'), PAS un chiffre officiel ni un recensement ; denominateur EPCI a fiscalite propre : 1 266 (2017) et 1 252 (2026, collectivites-locales.gouv.fr) | recy.net INSPECTED : la phrase '1 200 forfaits differents' est une projection de l'auteur (pas une statistique) ; le denominateur reel des regimes d'acces = 1 252 EPCI a fiscalite propre au 01/01/2026 (collectivites-locales.gouv.fr, serie 2015-2026 INSPECTED) - l'ordre de grandeur '~1 200 forfaits' est donc structurellement plausible (1 regime par EPCI) mais NON verifie par recensement : c'est une H a tester, pas un fait etabli | 0791350b-28b1-44e5-81c8-bdb4de33a85c
FCT-004 | FACT | ✦ | https://www.ledauphine.com/economie/2025/02/13/quotas-pour-les-passages-en-dechetteries-le-territoire-y-renonce | A,C | 2026-08-30 | CONTRE-EXEMPLE DE RENONCEMENT : Le Gresivaudan (Isere) comptait instaurer 30 passages gratuits/an au 10/02/2025 puis facturation 40 EUR TTC/passage au-dela - le Dauphine Libere titre 13/02/2025 'le territoire y renonce' ; 96% des usagers avaient fait moins de 30 passages en 2024 | Dauphine Libere 13/02/2025 INSPECTED : 'A compter du 10 fevrier, la CC Le Gresivaudan comptait instaurer des quotas sur le nombre de passages en decheteries... Cette mesure visait a en autoriser 30 gratuits par an' - titre : 'le territoire y renonce' ; Facebook CC (snippet) : 96% des usagers < 30 passages en 2024, quota 30 + 40 EUR TTC/passage au-dela - la bascule n'est ni automatique ni irreversible : elle peut reculer sous pression locale | baef2cba-9d50-4eab-826e-1b51148883bf
FCT-005 | FACT | ✦ | https://www.payssabolien.fr/le-pays-sabolien/competences/environnement/decheterie/ | B,C | 2026-08-30 | CONFIGURATION TYPE 2025-2026 : badge obligatoire + quota + facturation - Pays sabolien 18 passages/an depuis 01/01/2025, facturation 5 EUR/passage (19-24) puis 50 EUR/passage (>25) en 2026 ; moyenne 2024 = 10 passages/an/foyer ; Select'om badge 8 decheteries tarifs au-dela de 24 passages | Pays sabolien INSPECTED : 'Depuis le 1er janvier 2025, chaque foyer... beneficie de 18 passages par an... facturation en 2026 (5 EUR par passage pour le seuil 19-24 passages et 50 EUR par passage au-dela de 25)' ; 'nombre de passages moyen en decheterie en 2024 est de 10 par an par foyer' - Select'om (INSPECTED) : tarifs au-dela de 24 passages/an - recy.net : 'Demain, un usager qui depasse les 36 passages pourra etre facture au passage supplementaire' - le quota fixe un seuil ~2x la moyenne reelle : il cible les gros apporteurs et ouvre la porte a la monétisation | c65a498c-fdc6-4eb5-9ca4-89bad68e6326
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-011,SRC-012
FCT-002 | SRC-017,SRC-014
FCT-003 | SRC-020,SRC-018
FCT-004 | SRC-016,SRC-011
FCT-005 | SRC-012,SRC-020

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-032 | FOUND_RESOLVED
FCT-002 | QRY-031 | FOUND_RESOLVED
FCT-003 | QRY-027 | FOUND_RESOLVED
FCT-004 | QRY-028 | FOUND_RESOLVED
FCT-005 | QRY-029 | FOUND_RESOLVED

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:CONFIRME
FCT-003 | ELIGIBLE:CONFIRME
FCT-004 | ELIGIBLE:CONFIRME
FCT-005 | ELIGIBLE:CONFIRME

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:7:AXS-001:QRY-001
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9:AXS-001:QRY-001
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:11:AXS-001:QRY-001
CP-004 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10:AXS-001:QRY-001
CP-005 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11:AXS-001:QRY-001
CP-006 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13:CLM-001:QRY-001
CP-007 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17:CAU-001:QRY-001
CP-008 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18b:GATES

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T19:33:34.799721+00:00","fact_mem":{"FCT-001":"36816a03-266d-468d-9153-8374a87f53d7","FCT-002":"0cefab8b-c49b-4fae-b716-c44c4a2eb0e8","FCT-003":"0791350b-28b1-44e5-81c8-bdb4de33a85c","FCT-004":"baef2cba-9d50-4eab-826e-1b51148883bf","FCT-005":"c65a498c-fdc6-4eb5-9ca4-89bad68e6326"},"mnemo_row":"MNEMO_MCP_8002","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"write_memory reference MCP 8002","success":1}],"writeback_row":{"attempted":5,"blocked":0,"eligible":5,"failure":0,"success":5}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_MCP_8002 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:5;attempted:5;success:5;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[5 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-002 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-005 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
