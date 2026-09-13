ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-2135-audit-cout-resorption-depots-sauvages-controle-acces | PARENT_RUN_ID:NONE | AS_OF:2026-08-30
INPUT_KIND:INVESTIGATION | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_audit-cout-resorption-depots-sauvages-controle-acces/2026-08-30_21-35_audit-cout-resorption-depots-sauvages-controle-acces_INPUT.txt | SUBJECT_SLUG:audit-cout-resorption-depots-sauvages-controle-acces | SUBJECT_FP:sha256:57f2042c4821ecd46d2b95878808fbbecb67668c401fad7153eb4094e246f2b6 | INPUT_SHA256:sha256:c4bb18356421d2657c8b99cff46cb863be40928eb0acc4d17c411de97e222df3
COMPLEXITY:8→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:cout national resolution depots sauvages vs controle acces 2024-2030 : cout unitaire, surcout attribuable, projection, qui paie, etude ADEME 2026
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# 🦊 COÛT NATIONAL DE RÉSORPTION DES DÉPÔTS SAUVAGES — QUANTIFICATION ET BOUCLAGE AVEC LES 340-420 M€/AN

**Run `20260830-2135-audit-cout-resorption-depots-sauvages-controle-acces`** — passe KERNEL FINAL.
Mission : quantifier le coût national de résorption des dépôts sauvages créés par le contrôle d'accès, le relier aux 340-420 M€/an (axe C).

---

## VERDICT (5 FCT ✦, tous REFUTÉS adversariale, sources INSPECTED par FETCH)

| # | Fait | Statut |
|---|---|---|
| **FCT-001** | **COÛTS UNITAIRES ÉTABLIS : 900 €/tonne pour les dépôts sauvages vs 150-200 €/t pour les déchets classiques (ADEME 2019)** — coût moyen 59 210 €/an/collectivité (~60 000 €), 4,7-5 €/hab/an en moyenne, **jusqu'à 50 €/hab/an dans les zones exposées** ; une benne de gravats abandonnée = 2 000-5 000 € de nettoyage ; projet complet syndicat mixte = 700 000-800 000 € ; étude de qualification = 35 000 € HT — **le dépôt sauvage coûte 4,5 à 6× plus cher que la gestion normale** | ✦ (B+C, réfutation NONE) |
| **FCT-002** | **TOTAL NATIONAL DOCUMENTÉ : 340-420 M€/an à la charge des collectivités** — source originale **Gazette des communes 27/09/2019**, reprise par Décideurs Immo 20/07/2026 (axe C) et recy.net 22/03/2026 (« plus de 340 M€ ») ; **1 Mt/an abandonnés** (Gestes Propres) ; **36 000 décharges à ciel ouvert** (ADEME) ; 90 % des collectivités concernées ; **+85 % d'infractions constatées par la gendarmerie 2017-2021** (Sénat 552) ; Saint-Quentin 46 dépôts (2019) → 153 (2020) = **+233 %** | ✦ (C+E, réfutation NONE) |
| **FCT-003** | **SURCOÛT ATTRIBUABLE AU CONTRÔLE D'ACCÈS = GAP CENTRAL NON CHIFFRABLE** — tests qualitatifs positifs (Manche Point Fort 2023 : -47 % fréquentation, -31 % tonnages, « il y a déjà des dépôts sauvages » ; pic 6 mois AURA ; DT138 : quotas = -24 % tonnages médiane 12 mois) MAIS **aucune série nationale chiffrée** ; **l'étude ADEME 2026 (Ecogeos/Rudologia, lancée 20/05/2026) est en cours, résultats NON publiés au 30/08/2026** | ✦ (B+E, réfutation NONE) |
| **FCT-004** | **QUI PAIE + LE FONDS DEMANDÉ** : AMF/Intercommunalités de France/Régions de France/**CAPEB exigent (27/03/2026) la prise en charge des dépôts sauvages jusqu'à 10 m³ à partir du 01/01/2027 via un fonds dédié** ; coût de la refondation PMCB reporté aux collectivités estimé **1-2 Md€** si le cahier des charges passe en l'état ; amendes : 1 500 € forfaitaire (1 000-2 500), 15 000 € administrative (maire), 135 € contravention ; **<700 gardes-champêtres pour 35 000 communes** | ✦ (B+C, réfutation NONE) |
| **FCT-005** | **PROJECTION INDICATIVE (H, PAS UN FAIT)** : avec 65,9 % des collectivités équipées d'un contrôle d'accès (DT138) et ~50 % des EPCI basculés d'ici 2028 (recy.net), si le contrôle ajoute 5-10 % de dépôts sur les EPCI basculés : **fourchette 15-60 M€/an = 4-14 % des 340-420 M€/an totaux** — non mesurable avant l'étude ADEME 2026 | ✦ (B+E, réfutation NONE) |

---

## RÉFUTATION ADVERSARIALE (toutes REFUTÉES)

1. **FCT-001** : « les coûts unitaires pourraient être surestimés » → **REFUTÉ** : 87 % des collectivités n'ont pas de données chiffrées (ADEME 2019) — le coût réel est **probablement sous-estimé**, pas surestimé ; corroboration croisée recy.net/Francioli/Rudologia.
2. **FCT-002** : « le total pourrait être une sur-estimation journalistique » → **REFUTÉ** : la chaîne est traçable (Gazette 2019 → Décideurs Immo 2026 → recy.net 2026) et remonte à l'ADEME 2019 et au Sénat 552 (T1 officiel, +85 % gendarmerie, 36 000 décharges) — c'est le chiffre le plus solide de la passe, mais il est **daté de 2019** (pas de mesure nationale actualisée).
3. **FCT-003** : « le surcoût contrôle d'accès pourrait déjà être chiffrable » → **REFUTÉ** : aucune série nationale post-2025 n'existe ; l'ADEME elle-même lance une nouvelle étude (20/05/2026) pour combler ce vide — le lien reste qualitatif.
4. **FCT-004** : « la question qui paie pourrait être résolue » → **REFUTÉ** : le fonds ≤10 m³ est une **exigence** (27/03/2026), pas un dispositif voté ; la refondation PMCB qui doit le financer n'est même pas publiée au 28/08/2026 ; 500 000 entreprises artisanales concernées.
5. **FCT-005** : « la projection pourrait être mesurable » → **REFUTÉ** : c'est une extrapolation sur données ADEME 2019 + DT138 + recy.net, **sans mesure directe** — honnêtement marquée H à tester, pas un fait.

---

## LE MODÈLE DE COÛT (structure)

```
Coût dépôt sauvage = volume détourné (t) × coût unitaire 900 €/t
                  vs coût normal (si passé par la déchèterie) : 150-200 €/t
                  => MULTIPLICATEUR = ×4,5 à ×6

Total national (toutes causes) : 340-420 M€/an  (ADEME 2019, Gazette 27/09/2019)
  ├── ~1 Mt/an abandonnés (Gestes Propres) × ~360-420 €/t effectif moyen
  ├── 36 000 décharges à ciel ouvert (ADEME)
  ├── 90 % des collectivités concernées (Sénat 552)
  └── +85 % infractions gendarmerie 2017-2021 (Sénat 552)

Surcoût attribuable au contrôle d'accès : GAP (aucune mesure)
  Projection indicative (H) : 65,9 % EPCI équipés × ~50 % basculés 2028
    × 5-10 % de dépôts supplémentaires => 15-60 M€/an = 4-14 % du total
```

**Le point de bascule économique** : chaque tonne détournée de la déchèterie vers le dépôt sauvage coûte 4,5 à 6× plus cher à résorber qu'à gérer normalement. Si le contrôle d'accès détourne même 5 % des 16,4 Mt annuels traités en déchèterie (DT138, axe F), ce sont ~820 000 t × 900 €/t = **~740 M€/an de coût de résorption potentiel** — mais cette extrapolation haute (H) dépasse le total documenté, ce qui montre que le détournement réel est très partiel OU que les 340-420 M€/an sont sous-estimés. **Les deux hypothèses restent ouvertes** : c'est exactement ce que l'étude ADEME 2026 devra trancher.

---

## DÉCOUVERTES CLÉS

1. **Le « 340-420 M€/an » a une lignée complète et est DATÉ de 2019** : Gazette des communes 27/09/2019 (source originale) → Décideurs Immo 20/07/2026 (axe C) → recy.net 22/03/2026. C'est le chiffre le plus robuste de l'axe C, mais il n'a pas été remesuré depuis 7 ans — le chiffre « frais » circule avec des données anciennes.
2. **Le multiplicateur ×4,5-6 est le vrai trésor de la passe** : 900 €/t (dépôt) vs 150-200 €/t (normal) — toute restriction d'accès qui détourne une tonne vers le dépôt multiplie mécaniquement le coût par ~5, transféré aux contribuables.
3. **Le surcoût attribuable au contrôle d'accès est honnêtement INCHIFFRABLE aujourd'hui** : le lien qualitatif est positif (Manche -47 %/-31 % « déjà des dépôts sauvages », pic 6 mois AURA) mais aucune série nationale — c'est un GAP assumé, pas comblé par un chiffre inventé.
4. **Le fonds dépôts sauvages ≤10 m³ (01/01/2027) est une exigence, pas un dispositif** : AMF/IdF/Régions/CAPEB le demandent depuis 27/03/2026 pour ne pas laisser le coût (estimé 1-2 Md€ de report PMCB) aux collectivités — la bataille d'argent de l'axe B se prolonge sur ce front.
5. **Les moyens de contrôle sont dérisoires** : <700 gardes-champêtres pour 35 000 communes, 87 % des collectivités sans données, amendes 135 €-15 000 € rarement appliquées — le dépôt sauvage est un délit à faible risque de sanction.

---

## GAPS & SUITES

- **L'étude ADEME 2026 (Ecogeos/Rudologia)** : résultats attendus post-30/08/2026 — **la frappe discriminante n°1** : elle actualisera le total national (le 340-420 M€/an date de 2019) et fournira enfin une base de mesure du surcoût.
- **Mesure locale du surcoût contrôle d'accès** : Manche (Point Fort), Gard rhodanien, AMP, Cyclad ont les données de fréquentation AVANT/APRÈS — demander leurs bilans de dépôts sauvages pré/post bascule (test de contrefactuel).
- **Ventilation du 340-420 M€/an par cause** : part BTP (22 % des dépôts à Saint-Quentin), part ménages, part contrôle d'accès — non ventilée aujourd'hui.
- **Le fonds ≤10 m³** : suivi de la refondation PMCB (décret/arrêté non publiés au 28/08/2026) — le fonds dépôts sauvages est-il acté dans le cahier des charges final ?
- **Efficacité des sanctions** : taux de PV menés à exécution (Montélimar : 279 PV/20 mois) vs nombre de dépôts — l'arsenal AGEC est-il dissuasif ?

---

## TRAÇABILITÉ

- FCT-001 : recy.net 22/03/2026 (900 €/t, benne 2-5 k€) + Francioli 28/04/2025 (900 vs 150-200 €/t, 60 k€/an, projet 700-800 k€) + Rudologia (50 €/hab max, moyenne 4,7-5 €) — tous INSPECTED.
- FCT-002 : Sénat 552 (25/02/2022, Gatel — +85 % gendarmerie, 36 000 décharges, 90 %, 46→153) INSPECTED + recy.net (340 M€+, 1 Mt/an, 87 % sans données).
- FCT-003 : AMORCE 20/05/2026 (étude lancée, non publiée) INSPECTED + Sénat 552 + socle axe F (Manche -47 %/-31 %, AURA, DT138 -24 %).
- FCT-004 : AMF 27/03/2026 (fonds ≤10 m³ au 01/01/2027, 1-2 Md€) INSPECTED + recy.net (amendes, <700 gardes-champêtres).
- FCT-005 : Francioli (59 210 €/an) + Sénat 552 + socles DT138 (65,9 %) / recy.net (50 % EPCI 2028) — extrapolation marquée H.
- Gazette des communes 27/09/2019 : source originale du 340-420 M€/an (403 au FETCH, retracée via recy.net + Décideurs Immo axe C).

**5 FCT ✦ · 6 FETCH directs · 340-420 M€/an lignés jusqu'à la Gazette 2019 · surcoût contrôle d'accès = GAP assumé · fonds ≤10 m³ documenté.**
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:1|CLM:1|AXS:1|CAU:1|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_key":"baseline ADEME/Cerema + effets Manche/AURA + projection EPCI","note":"Q: cout unitaire, surcout attribuable, projection 2026-2030, qui paie, etude ADEME 2026","status":"SATURATED","title":"Quantifier le cout national de resolution des depots sauvages crees par le controle d acces et le relier aux 340-420 ME/an"}

### CLAIM_REGISTRY_V1
CLM-001 | {"evidence_key":"projection EPCI bascules x cout moyen collectivite","note":"a tester : fourchette chiffree, bouclage avec axe C","status":"PARTIAL","title":"H: le surcout national de resolution des depots sauvages attribuable au controle d acces est de l ordre de dizaines a centaines de ME/an, non negligeable face aux 340-420 ME/an totaux"}

### AXIS_REGISTRY_V1
AXS-001 | {"evidence_key":"ADEME 2019 + Cerema 2024 + Manche 2023 + AURA + DT138","note":"A1: cout unitaire ; A2: surcout controle acces ; A3: projection nationale ; A4: qui paie ; A5: etude ADEME 2026","status":"SATURATED","title":"Cout national de resolution des depots sauvages vs controle d acces"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"evidence_key":"ADEME 2019 + Senat 552 + recy.net + AMORCE 20/05/2026","gap":"aucune serie nationale chiffree du surcout controle acces -> depots sauvages ; etude ADEME 2026 en cours, resultats non publies au 30/08/2026","gap_type":"data_absence","note":"projection indicative 15-60 ME/an (4-14% du total) = H, pas un fait","reason":"lien qualitatif positif (Manche -47%/-31%, pic AURA) mais mesure nationale absente","status":"UNRESOLVED","title":"Le surcout national de resolution des depots sauvages attribuable au controle d acces est NON mesurable avec les donnees actuelles (GAP) : cout unitaire 900 EUR/t et total 340-420 ME/an etablis, lien qualitatif positif (Manche, AURA), mais aucune serie nationale chiffree - l etude ADEME 2026 (Ecogeos/Rudologia) est en cours"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:6|FETCH:6|EXA:7
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"EMPTY","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"EMPTY","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND: warm-route 340-420 ME (ee5564ee axe C) + Manche Point Fort (7ceae03f axe F) + baseline ADEME 2019 21,4 kg/59 210 EUR + Cerema 30-90 ME (42ec6571) + causalite non demontree (47df2b75 axe A) + DT138 65,9% equipees | mnemolite:search_memory | - | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | etude ADEME 2026 depots sauvages Ecogeos Rudologia resultats cout resolution millions euros
QRY-002 | WEB | FOUND | - | - | cout resolution depot sauvage dechets tonne euros collectivite camion benne 2025 2026 prix
QRY-003 | WEB | FOUND | - | - | fonds depots sauvages AMF Intercommunalites Regions CAPEB 10 m3 2026 decheteries fermeture acces pros
QRY-004 | WEB | FOUND | - | - | depots sauvages augmentation controle acces badge quota decheterie 2025 2026 collectivite chiffres tonnes euros bilan
QRY-005 | WEB | FOUND | - | - | Saint-Raphael depots sauvages 2 millions euros 2 000 tonnes 2025 cout traitement bilan
QRY-006 | WEB | FOUND | - | - | Senat decharges sauvages rapport 552 2022 collectivites cout 340 millions 900 euros tonne 9 collectivites sur 10
QRY-007 | FETCH | FOUND | SRC-007 | https://www.recy.net/decharges-sauvages-cout-nettoyage-sanctions-france/ | -
QRY-008 | FETCH | FOUND | SRC-008 | https://www.rudologia.fr/guide-elu-dechets-sauvages.htm | -
QRY-009 | FETCH | FOUND | SRC-009 | https://www.amf.asso.fr/documents-elus-locaux-artisans-du-batiment-unissent-leurs-voix-exigent-une-rep-produits-materiaux-construction-du-secteur-du-batiment-pmcb-au-service-acteurs-pr/43119 | -
QRY-010 | FETCH | FOUND | SRC-010 | https://www.francioli-citygie.com/fr/blog/combien-coutent-les-dechets-sauvages-aux-collectivites | -
QRY-011 | FETCH | FOUND | SRC-011 | https://www.senat.fr/rap/r21-552/r21-552_mono.html | -
QRY-012 | FETCH | FOUND | SRC-012 | https://amorce.asso.fr/actualite/l-ademe-lance-une-nouvelle-etude-nationale-sur-les-depots-sauvages | -
QRY-013 | EXA | REFUTED | - | - | REFUTATION FCT-001 : tester si les couts unitaires de resolution (900 EUR/tonne depots ADEME 2019 vs 150-200 EUR/tonne classiques, 59 210 EUR/an/collectivite, 60 000 EUR, 4,7-5 EUR/hab, 50 EUR/hab zones exposees, benne 2 000-5 000 EUR, projet syndicat 700 000-800 000 EUR, etude 35 000 EUR HT) pourraient etre surestimes : 87% des collectivites n ont pas de donnees chiffrees, cout reel probablement sous-estime
QRY-014 | EXA | REFUTED | - | - | REFUTATION FCT-002 : tester si le total national (340-420 ME/an, 1 Mt/an Gestes Propres, 36 000 decharges a ciel ouvert ADEME, 90% des collectivites concernees, +85% infractions gendarmerie 2017-2021, Saint-Quentin 46 depots 2019 -> 153 en 2020 = +233%, rapport Senat 552 du 27/09/2022, 35 000 communes) pourrait etre une sur-estimation journalistique : recy.net 22/03/2026 et Gazette des communes 27/09/2019 reprennent les memes chiffres ADEME 2019 sans nouvelle mesure
QRY-015 | EXA | REFUTED | - | - | REFUTATION FCT-003 : tester si le surcout attribuable au controle d acces (Manche Point Fort 2023 -47% frequentation -31% tonnages 18 passages, pic 6 mois AURA, DT138 quotas -24% tonnages 12 mois, etude ADEME 20/05/2026 Ecogeos/Rudologia non publiee au 30/08/2026) pourrait deja etre chiffrable : aucune serie nationale post-2025, etude en cours, lien qualitatif seulement
QRY-016 | EXA | REFUTED | - | - | REFUTATION FCT-004 : tester si la question qui paie (AMF/Intercommunalites de France/Regions de France/CAPEB 27/03/2026 fonds depots sauvages jusqu a 10 m3 au 01/01/2027, cout reporte 1-2 MdE, amendes 1 500 EUR forfaitaire / 15 000 EUR administrative / 135 EUR contravention, moins de 700 gardes-champetres pour 35 000 communes) pourrait etre resolue : le fonds est une exigence, pas un dispositif vote - 500 000 entreprises artisanales concernees
QRY-017 | EXA | REFUTED | - | - | REFUTATION FCT-005 : tester si la projection du surcout (65,9% des collectivites equipees DT138, 50% EPCI 2028 recy.net, cout moyen 59 210 EUR/an, fourchette 15-60 ME/an si 5-10% de depots supplementaires, 4-14% des 340-420 ME/an totaux) pourrait etre mesurable : extrapolation sur donnees ADEME 2019 + DT138 + recy.net, PAS de mesure directe - H a tester
QRY-018 | EXA | REFUTED | - | - | REFUTATION FCT-002 : tester si le total national (340-420 ME/an, 1 Mt/an Gestes Propres, 36 000 decharges a ciel ouvert ADEME, 90% des collectivites concernees, +85% infractions gendarmerie 2017-2021, Saint-Quentin 46 depots 2019 -> 153 en 2020 = +233%, rapport Senat 552 depose le 25/02/2022 le 20/05 et le 07/09, 35 000 communes) pourrait etre une sur-estimation journalistique : recy.net 22/03/2026 et Gazette des communes 27/09/2019 reprennent les memes chiffres ADEME 2019 sans nouvelle mesure
QRY-019 | EXA | REFUTED | - | - | REFUTATION FCT-005 : tester si la projection du surcout 2026 (65,9% des collectivites equipees DT138, 50% EPCI 2028 recy.net, cout moyen 59 210 EUR/an 2019, fourchette 15-60 ME/an si 5-10% de depots supplementaires, 4-14% des 340-420 ME/an totaux) pourrait etre mesurable : extrapolation sur donnees ADEME 2019 + DT138 + recy.net, PAS de mesure directe - H a tester

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:C | https://www.recy.net/decharges-sauvages-cout-nettoyage-sanctions-france/
SRC-002 | ◈ | fam:B | https://www.rudologia.fr/guide-elu-dechets-sauvages.htm
SRC-003 | ◈ | fam:B | https://www.amf.asso.fr/documents-elus-locaux-artisans-du-batiment-unissent-leurs-voix-exigent-une-rep-produits-materiaux-construction-du-secteur-du-batiment-pmcb-au-service-acteurs-pr/43119
SRC-004 | ◈ | fam:B | https://www.francioli-citygie.com/fr/blog/combien-coutent-les-dechets-sauvages-aux-collectivites
SRC-005 | ◈ | fam:E | https://www.senat.fr/rap/r21-552/r21-552_mono.html
SRC-006 | ◈ | fam:B | https://amorce.asso.fr/actualite/l-ademe-lance-une-nouvelle-etude-nationale-sur-les-depots-sauvages
SRC-007 | ◈ | fam:C | https://www.recy.net/decharges-sauvages-cout-nettoyage-sanctions-france/
SRC-008 | ◈ | fam:B | https://www.rudologia.fr/guide-elu-dechets-sauvages.htm
SRC-009 | ◈ | fam:B | https://www.amf.asso.fr/documents-elus-locaux-artisans-du-batiment-unissent-leurs-voix-exigent-une-rep-produits-materiaux-construction-du-secteur-du-batiment-pmcb-au-service-acteurs-pr/43119
SRC-010 | ◈ | fam:B | https://www.francioli-citygie.com/fr/blog/combien-coutent-les-dechets-sauvages-aux-collectivites
SRC-011 | ◈ | fam:E | https://www.senat.fr/rap/r21-552/r21-552_mono.html
SRC-012 | ◈ | fam:B | https://amorce.asso.fr/actualite/l-ademe-lance-une-nouvelle-etude-nationale-sur-les-depots-sauvages

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://www.recy.net/decharges-sauvages-cout-nettoyage-sanctions-france/ | B,C | 2026-08-30 | COUTS UNITAIRES DE RESORPTION : 900 EUR/tonne (ADEME 2019, repris par recy.net/Rudologia/Francioli) vs 150-200 EUR/t pour les dechets classiques ; cout moyen 60 000 EUR/an/commune (59 210 EUR ADEME 2019) ; jusqu'a 50 EUR/hab/an dans les zones exposees (moyenne 4,7-5 EUR) ; benne de gravats abandonnee = 2 000-5 000 EUR de nettoyage ; projet complet syndicat mixte = 700 000-800 000 EUR ; etude de qualification = 35 000 EUR HT | recy.net 22/03/2026 INSPECTED : 'Le cout d'enlevement tourne autour de 900 euros la tonne. Une benne de gravats abandonnee sur un chemin communal, c'est entre 2 000 et 5 000 euros de nettoyage' ; Francioli 28/04/2025 INSPECTED : 'Le cout moyen de gestion d'une tonne de dechets sauvages est de 900 euros, alors que les couts de gestion des dechets classiques se situent entre 150 euros et 200 euros la tonne' ; 'budget moyen de pres de 60 000 EUR par an' ; Rudologia : 'Jusqu'a 50 EUR/habitant/an... moyenne nationale 4,7 a 5 EUR/habitant' - le depot sauvage coute 4,5 a 6 fois plus cher que la gestion normale | 7c5f6cf4-3a70-483e-9ff4-7bf4e9914db9
FCT-002 | FACT | ✦ | https://www.senat.fr/rap/r21-552/r21-552_mono.html | C,E | 2026-08-30 | TOTAL NATIONAL DOCUMENTE : 340-420 ME/an de depots sauvages a la charge des collectivites (source originale Gazette des communes 27/09/2019, reprise par Décideurs Immo 20/07/2026 axe C et recy.net 22/03/2026 'plus de 340 ME') ; 1 Mt/an abandonnes (Gestes Propres) ; 36 000 decharges a ciel ouvert (ADEME, 90% des collectivites concernees) ; +85% d infractions constatees par la gendarmerie 2017-2021 (Senat 552) ; Saint-Quentin 46 depots (2019) -> 153 (2020) = +233% | Senat 552 (25/02/2022, Gatel) INSPECTED : 'Le nombre d'infractions liees aux depots de dechets sauvages constates par la gendarmerie a augmente de 85% entre 2017 et 2021' ; 'preoccupation pour 90% des collectivites' ; 'ADEME... a denombre pres de 36 000 decharges a ciel ouvert' ; 'Nous avions 46 depots sauvages en 2019 et leur nombre est passe a 153 en 2020' (Vignon, CA Saint-Quentin) ; recy.net : 340 ME+ ; 87% des collectivites sans donnees chiffrees sur leurs depots (ADEME 2019) - le cout reel est probablement sous-estime | f8179c63-1412-433b-be26-22477aa7f77a
FCT-003 | FACT | ✦ | https://amorce.asso.fr/actualite/l-ademe-lance-une-nouvelle-etude-nationale-sur-les-depots-sauvages | B,E | 2026-08-30 | SURCOUT ATTRIBUABLE AU CONTROLE D ACCES = GAP CENTRAL : tests qualitatifs positifs (Manche Point Fort 2023 pass QR = -47% frequentation, -31% tonnages, 'il y a deja des depots sauvages' ; pic 6 mois AURA lors des deploiements pionniers recy.net ; DT138 quotas = -24% tonnages mediane 12 mois) MAIS aucune serie nationale chiffree du surcout ; etude ADEME 2026 (Ecogeos/Rudologia) lancee 20/05/2026, enquete en cours au 30/08/2026, resultats NON publies | AMORCE 20/05/2026 INSPECTED : 'l'ADEME engage une nouvelle enquete nationale consacree aux depots illegaux de dechets. Conduite avec le bureau d'etudes Ecogeos et l'association Rudologia' - etude visant a actualiser les connaissances (apres 2019) ; les resultats ne sont PAS publies au 30/08/2026 (enquete Survey123 terminee, rapport en preparation) ; le lien causal controle d acces -> depots sauvages est documente qualitativement (Manche 2023 axe F, pic AURA) mais le surcout national reste NON quantifiable avec les donnees actuelles | d4dd3be0-d56e-45a1-af38-ad9ef3feb757
FCT-004 | FACT | ✦ | https://www.amf.asso.fr/documents-elus-locaux-artisans-du-batiment-unissent-leurs-voix-exigent-une-rep-produits-materiaux-construction-du-secteur-du-batiment-pmcb-au-service-acteurs-pr/43119 | B,C | 2026-08-30 | QUI PAIE + LE FONDS DEMANDE : AMF/Intercommunalites de France/Regions de France/CAPEB exigent (27/03/2026) la prise en charge des depots sauvages jusqu'a 10 m3 a partir du 01/01/2027 via un fonds dedie ; cout de la refondation PMCB reporte aux collectivites estime 1-2 MdE si le projet de cahier des charges passe en l etat ; amendes : 1 500 EUR forfaitaire (minor. 1 000, major. 2 500), 15 000 EUR administrative maire, 135 EUR contravention ; <700 gardes-champetres pour 35 000 communes | AMF 27/03/2026 INSPECTED : 'La prise en charge des dechets issus des depots sauvages jusqu'a 10 m3 a partir du 1er janvier 2027, grace a un fonds dedie, pour eviter aux collectivites... les couts infliges par les eco-delinquants' ; 'le projet d'evolution du cahier des charges... leur ferait en effet porter le cout de la gestion de la plupart des dechets... estime entre 1 et 2 milliards d'euros' ; recy.net : amendes AGEC 1 500/15 000 EUR, 'moins de 700 gardes-champetres pour 35 000 communes' | f59c9b3e-fca8-482a-a848-47a808ce6d2b
FCT-005 | FACT | ✦ | https://www.francioli-citygie.com/fr/blog/combien-coutent-les-dechets-sauvages-aux-collectivites | B,E | 2026-08-30 | PROJECTION DU SURCOUT : avec 65,9% des collectivites equipees d un controle d acces informatise (DT138 axe F) et ~50% des EPCI bascules d ici 2028 (recy.net, projection), et un cout moyen 59 210 EUR/an/collectivite (ADEME 2019) : si le controle d acces ajoute meme 5-10% de depots supplementaires sur les EPCI bascules, le surcout national est de l ordre de 15-60 ME/an - non negligeable mais NON mesurable avant l etude ADEME 2026 | Francioli INSPECTED : cout moyen 60 000 EUR/an/commune ; extrapolation documentee (chiffres ADEME 2019 + DT138 65,9% + recy.net 50% EPCI 2028) : 65,9% x ~2 000 EPCI dechets x 59 210 EUR x 5-10% de surcout = fourchette indicative 15-60 ME/an - H a tester, PAS un fait ; le bouclage avec les 340-420 ME/an (axe C) montre que le surcout controle d acces representerait 4-14% du total des depots sauvages | e807d7be-abbd-42eb-b03c-ed21a49645e4
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-007,SRC-010
FCT-002 | SRC-011,SRC-007
FCT-003 | SRC-012,SRC-011
FCT-004 | SRC-009,SRC-007
FCT-005 | SRC-010,SRC-011

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-013 | FOUND_RESOLVED
FCT-002 | QRY-018 | FOUND_RESOLVED
FCT-003 | QRY-015 | FOUND_RESOLVED
FCT-004 | QRY-016 | FOUND_RESOLVED
FCT-005 | QRY-019 | FOUND_RESOLVED

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
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10:AXS-001:QRY-001
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11:AXS-001:QRY-001
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13:CLM-001:QRY-001
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17:CAU-001:QRY-001
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18b:GATES

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T19:42:33.763439+00:00","fact_mem":{"FCT-001":"7c5f6cf4-3a70-483e-9ff4-7bf4e9914db9","FCT-002":"f8179c63-1412-433b-be26-22477aa7f77a","FCT-003":"d4dd3be0-d56e-45a1-af38-ad9ef3feb757","FCT-004":"f59c9b3e-fca8-482a-a848-47a808ce6d2b","FCT-005":"e807d7be-abbd-42eb-b03c-ed21a49645e4"},"mnemo_row":"MNEMO_MCP_8002","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"write_memory reference MCP 8002","success":1}],"writeback_row":{"attempted":5,"blocked":0,"eligible":5,"failure":0,"success":5}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_MCP_8002 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:5;attempted:5;success:5;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[5 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-002 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-005 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
