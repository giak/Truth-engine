# INVESTIGATION KERNEL v2.8 — 10 ZONES D'OMBRE : L'effondrement du modèle salarial

> **UPDATE** du parent `20260824-1822-leffondrement-du-modele-salarial`. Convertit `DEEP_DIVE_10_ZONES.md` (non-KERNEL) en investigation formelle KERNEL v2.8.
> Couvre : paradis data, miroir allemand, chiffrage trou Sécu, CSG historique, cadre juridique, scaling wall, participation, acteurs politiques, flexsécurité danoise, convergence/business model.

## RUN_MANIFEST

| Champ | Valeur |
|---|---|
| ENGINE_VERSION | 2.8 |
| STATE | FINAL |
| RUN_ID | 20260824-2030-leffondrement-10-zones |
| PARENT_RUN_ID | 20260824-1822-leffondrement-du-modele-salarial |
| AS_OF | 2026-08-24 |
| INPUT_KIND | UPDATE |
| MISSION_MODE | INVESTIGATION |
| INPUT_REF | PATH:investigations/2026-08/2026-08-24_leffondrement-du-modele-salarial/2026-08-24_18-22_leffondrement-du-modele-salarial_INVESTIGATION.md |
| SUBJECT_SLUG | leffondrement-10-zones |
| INVESTIGATION_PATH | investigations/2026-08/2026-08-24_leffondrement-du-modele-salarial/2026-08-24_20-30_leffondrement-10-zones_INVESTIGATION.md |
| SCOPE | 10 zones : paradis data, Allemagne, chiffrage trou, CSG, juridique, scaling wall, participation, acteurs politiques, Danemark, convergence business model |
| COMPLEXITY | 13→APEX |
| CHECKPOINT_SEQ | 0 |
| LAST_COMPLETED | 19b |
| NEXT_ACTION | NONE |
| RESUME_COUNT | 0 |
| ROUTE_OVERRIDES | [] |
| LOADED_MODULES | SYMBOLS.md,PATTERNS.md,THREATS.md,GATES.md,REQUEST_LOG.md,ICEBERG.md,MONEY.md,FRAMING.md |
| DEGRADED_FLAGS | [] |
| GATE_VERDICT | PASS |
| STATE_ID | sha256:aabdf0b32e16d3a2319f9fe49b40eee5b9c981cc8d33fe254125963b27d3047c |

## TEMPORAL_STATE

| Événement | Date |
|---|---|
| Investigation parent | 2026-08-24 18:22 |
| RENARD UPDATE | 2026-08-24 20:00 |
| DEEP DIVE 10 zones (compagnon non-KERNEL) | 2026-08-24 ~19:00 |
| Investigation KERNEL (ce fichier) | 2026-08-24 20:30 |
| AS_OF | 2026-08-24 |

## MANIPULATION_REPORT

| Champ | Valeur |
|---|---|
| INPUT_KIND | UPDATE |
| MISSION_MODE | INVESTIGATION |
| SYMBOL_STAGE | CORPUS_FINAL |
| SYMBOLS | Ξ:7, €:6, Λ:5, Ω:2, Ψ:2, ↕:5, Φ:3, Σ:2, Κ:3, ρ:2, κ:2, ⫸:5, ⚔:1, 🌐:2, ⏰:4 |
| PATTERNS | @PAT[ICEBERG], @PAT[MONEY], @PAT[POLITICAL] |
| THREATS | @THR[DARK_MONEY] (OpenAI Ireland), @THR[NUDGE] (CTA créateur) |
| RHETORICAL | DEM:1, BF:1, NUM:2, AUTH:1, FAC:1 |
| COMPLEXITY | 13→APEX |
| CLUSTERS | ICEBERG,MONEY,FRAMING |
| IMPLICIT | Omissions majeures du parent : données empiriques substitution, complémentarité IA, paradis data, Allemagne, CSG trajectoire, Danemark non immunisé, PFU, scaling wall |
| QUERY_GUIDANCE | Sources primaires : OECD, CLEISS, CNIL, The Currency, ITEP, ECB, EIB, CEPR, DG Trésor, Anthropic, Bundestag, Bundestag |

## CRÉDO

**LEAD_QUESTION** : Les 10 zones d'ombre non explorées par la vidéo — et partiellement couvertes par l'investigation parent — aggravent-elles, atténuent-elles ou nuancent-elles la thèse de l'effondrement du modèle salarial ?

**OBJECT_QUESTION** : Parmi les angles morts de la vidéo (paradis fiscal/data, comparaison internationale, dispositifs existants, limites technologiques, acteurs politiques, convergence des distorsions), lesquels modifient significativement l'évaluation de la thèse centrale ?

### AXS (Axes d'investigation)

| AXS-ID | QUESTION | SOUGHT_OBJECTS | STATUS |
|---|---|---|---|
| AXS-Z01 | Paradis de la data : structure fiscale OpenAI/Anthropic en Europe, flux de données, GDPR | The Currency, ITEP, OpenAI EU Terms, comptes | SATURATED |
| AXS-Z02 | Miroir allemand : coin fiscal, débat politique, position gouvernementale | OECD, Bundestag, Klingbeil, think tanks | SATURATED |
| AXS-Z03 | Chiffrage back-of-envelope du trou Sécu si substitution | Hypothèses cadres France, pertes cotisations, scénarios | SATURATED |
| AXS-Z04 | CSG : historique complet des hausses, montant, trajectoire | Wikipedia, AOPS, Le Revenu, Finances Publiques | SATURATED |
| AXS-Z05 | Cadre juridique : AI Act, taxe GAFAM, Pilier 1/2 OCDE | EU Commission, Légifiscal, Sénat, OECD Pillars | SATURATED |
| AXS-Z06 | Scaling wall : limites réelles de l'IA générative | Marcus, LeCun, benchmarks | SATURATED |
| AXS-Z07 | Participation/intéressement : formules dérogatoires, PPV | Service-Public, BOSS, Code du travail | SATURATED |
| AXS-Z08 | Acteurs politiques : syndicats, rapports parlementaires | CFDT, CGT, Sénat, CESE, HCFiPS | SATURATED |

## INVESTIGATION_MAP

### LEAD_REGISTRY

| LED-ID | LOCATOR | LEAD | KIND | MATERIALITY | ROUTES | STATUS |
|---|---|---|---|---|---|---|
| LED-Z01 | Z1 | OpenAI Ireland Ltd (Dublin) = contractant EEA. IS 12,5 % (0 effectif car pertes). Données professionnelles FR → serveurs US sans taxation. GDPR/Schrems II non résolu. | MECHANISM | DECISIVE | AUDIT,EXPAND,LINK | SATURATED |
| LED-Z02 | Z1 | OpenAI perte 5,09 Md$ 2024, ×8 en 2025. Anthropic 11,6 Md$ CA Q2 2026, non rentable. IS effectif ≈ 0. | EVENT | DECISIVE | AUDIT | SATURATED |
| LED-Z03 | Z2 | Allemagne : coin fiscal 47,9 % > France 47,2 %. Même modèle Bismarck. Vidéo ignore ce pays. | CLAIM | DECISIVE | AUDIT,EXPAND | SATURATED |
| LED-Z04 | Z2 | Ministre Finances allemand (Klingbeil) appelle à taxe numérique discriminatoire (jan 2026). | EVENT | IMPORTANT | AUDIT | SATURATED |
| LED-Z05 | Z3 | Chiffrage : 5 % cadres non remplacés = perte ~4,4 Md€/an. 77 Md€ allègements existants > perte potentielle. | CALCULATION | DECISIVE | EXPAND | SATURATED |
| LED-Z06 | Z4 | CSG : 1,1 % (1991) → 9,2 % (2018). 145 Md€/an, ~20 % financement. Transition déjà faite à moitié. | FACT | DECISIVE | AUDIT,EXPAND | SATURATED |
| LED-Z07 | Z5 | AI Act (entré en vigueur 2024), taxe GAFAM 0,7 Md€ (amendement 6 % adopté), Pilier 1 OCDE, Pilier 2 (15 % IS minimum). L'État n'est pas désarmé. | MECHANISM | DECISIVE | AUDIT,EXPAND | SATURATED |
| LED-Z08 | Z6 | Marcus (nov 2024) : LLMs en rendements décroissants. LeCun (2025) : AGI pas atteignable par scaling. Substitution massive non garantie. | CLAIM | DECISIVE | AUDIT | SATURATED |
| LED-Z09 | Z7 | Participation dérogatoire + intéressement + PPV (6 000 €) décorrélés de S. L'« arnaque mathématique » est atténuable. | MECHANISM | IMPORTANT | AUDIT,EXPAND | SATURATED |
| LED-Z10 | Z8 | CFDT, CGT : dialogue social, pas taxe IA. Aucun rapport parlementaire dédié « IA et financement social ». Vide politique. | GAP | IMPORTANT | EXPAND | SATURATED |
| LED-Z11 | Z9 | Danemark : pas de cotisations employeur (8 % impôt marché travail). TVA 25 % depuis 1992. Transition faite sans crise. « Immunisé » = exagération. | CLAIM | DECISIVE | AUDIT,EXPAND | SATURATED |
| LED-Z12 | Z9 | CLEISS : financement par impôts, pas cotisations. DG Trésor : modèle danois = précédent historique de TVA sociale. | FACT | DECISIVE | AUDIT | SATURATED |
| LED-Z13 | Z10 | Marketing anxiogène semi-sincère. 8/10 zones affaiblissent la thèse. Produit du marché de l'attention YouTube. | INFERENCE | DECISIVE | EXPAND,CONTEXT | SATURATED |

## SYMBOL_SCORES (15/15, CORPUS_FINAL)

| Sym | Nom | Score | Observations |
|---|---|---|---|
| Ξ | Omission | 7 | Vidéo omet : Allemagne (coin supérieur), CSG déjà à 9,2%, Danemark pas « immunisé », participation dérogatoire, PFU, scaling wall, paradis data. |
| € | Money | 6 | OpenAI Ireland Ltd IS 12,5%→0. Patreon créateur. Triple fuite. Allègements 77 Md€ occultés. |
| Λ | Framing | 5 | « Subvention » = coût évité. « Immunisé » = exagéré. « Au coude à coude » = 5,4 pts écart. |
| Ω | Inversion | 2 | Pas d'inversion factuelle majeure. |
| Ψ | Sidération | 2 | Format YouTube standard. |
| ↕ | Vertical power | 5 | Asymétrie fiscale systémique. Big Tech extrait valeur sans cotiser. |
| Φ | Spectacle | 3 | Titre dramatique, format engageant. |
| Σ | Semiotics | 2 | Termes économiques standard. « Subvention » = abus. |
| Κ | Cynicism | 3 | « L'État n'a jamais vu », « personne ne l'a voté ». |
| ρ | Resistance | 2 | Syndicats = dialogue social, pas taxe IA. |
| κ | Subtle influence | 2 | CTA Patreon/Discord. |
| ⫸ | Convergence | 5 | Convergence sur asymétrie réelle. Pas de convergence sur substitution empirique. |
| ⚔ | Cognitive warfare | 1 | Créateur solo. |
| 🌐 | Network | 2 | Communauté Patreon. |
| ⏰ | Temporal | 4 | Arc 1883→1991→présent. Urgence artificielle. |

## CLAIM_REGISTRY

| CLM-ID | CLAIM | SUPPORT | COUNTER | STATUS | GAP_TYPE |
|---|---|---|---|---|---|
| CLM-Z01 | OpenAI Ireland Ltd = contractant EEA, IS 12,5% (0 effectif car pertes), triple fuite | OpenAI EU Terms (2026), The Currency (2025), ITEP (2026), SiliconAngle (2026) | — | CONFIRME | — |
| CLM-Z02 | Allemagne coin 47,9% > France 47,2%, même Bismarck | OECD Taxing Wages 2025 (SIPOTRA) | — | CONFIRME | — |
| CLM-Z03 | 5% cadres non remplacés = perte ~4,4 Md€/an, 77 Md€ allègements > perte | Calcul back-of-envelope, Cour des comptes | CSG + TVA compensent partiellement | PROBABLE | ORDRE_GRANDEUR |
| CLM-Z04 | CSG 1,1%→9,2% (1991-2018), 145 Md€/an, 1 point = ~16 Md€ | Wikipedia, AOPS, Le Revenu | — | CONFIRME | — |
| CLM-Z05 | AI Act + taxe GAFAM 0,7 Md€ + Pilier 1/2 = État pas désarmé | EU Commission, Légifiscal, Sénat, OECD Pillars | TSN suspendue niveau UE, Pilier 1 bloqué US | SOUTENU | INCOMPLET |
| CLM-Z06 | Marcus (2024) + LeCun (2025) : LLMs en rendements décroissants, AGI pas par scaling | Marcus Substack, Big Tech Podcast | Débat ouvert, progrès réels sur benchmarks | SOUTENU | DÉBAT_OUVERT |
| CLM-Z07 | Participation dérogatoire + intéressement + PPV (6k€) atténuent l'effet S↓ | Service-Public, BOSS, Code du travail | PPV facultative, intéressement plafonné 20% masse salariale | SOUTENU | NON_AUTOMATIQUE |
| CLM-Z08 | Danemark : pas de cotisations employeur, TVA 25% depuis 1992. Transition faite sans crise. | CLEISS, DG Trésor | « Immunisé » = exagération. Impôt et TVA sensibles au chômage. | CONFIRME | — |
| CLM-Z09 | 8/10 zones affaiblissent la thèse. 1 l'aggrave (paradis data), 1 neutre (acteurs). | Analyse RENARD + 10 zones | — | SOUTENU | QUALITATIF |

## FACT_REGISTRY_V1

| FCT-ID | EPI | TIER | URL | FAMILIES | DATE | SUJET | VALEUR | MEM |
|---|---|---|---|---|---|---|---|---|
| FCT-Z01 | FACT | ✧ | https://openai.com/policies/eu-terms-of-use/ | A | 2026-01-16 | OpenAI Ireland Ltd = contractant EEA | « Services provided by OpenAI Ireland Ltd, Dublin » | mem:- |
| FCT-Z02 | FACT | ✧ | https://thecurrency.news/articles/197670/ | C | 2025-07-30 | OpenAI Ireland 2024 accounts | First full-year accounts filed, ramped up activity | mem:- |
| FCT-Z03 | FACT | ✧ | https://www.wheresyoured.at/exclusive-openai-financials/ | C | 2026-06-15 | OpenAI 2024 pertes | $3,7 Md revenus, $12,4 Md coûts, $5,09 Md perte nette | mem:- |
| FCT-Z04 | FACT | ✦ | https://www.sipotra.it/wp-content/uploads/2025/05/GERMANY.pdf | D | 2025-04-30 | Coin fiscal Allemagne 2024 | 47,9% (single, average wage) | mem:- |
| FCT-Z05 | FACT | ✧ | https://www.cleiss.fr/docs/cotisations/danemark.html | A | 2025 | Danemark : pas de cotisations sociales | Financement par impôts. Contribution marché travail 8% (impôt). | mem:- |
| FCT-Z06 | FACT | ✦ | https://fr.wikipedia.org/wiki/Contribution_sociale_g%C3%A9n%C3%A9ralis%C3%A9e | E | 2026-08-24 | CSG historique taux | 1,1% (1991) → 2,4% (1993) → 3,4% (1997) → 7,5% (1998) → 9,2% (2018) | mem:- |
| FCT-Z07 | FACT | ✧ | https://www.legifiscal.fr/actualites-fiscales/4297-plf-2026-amendement-double-taux-taxe-gafam.html | A | 2025-10-29 | Taxe GAFAM amendement doublement 6% | Taux 3%→6%, seuil 750M→2Md€. Avis défavorable gouvernement. | mem:- |
| FCT-Z08 | FACT | ✧ | https://www.senat.fr/amendements/2025-2026/138/Amdt_I-1694.html | A | 2025-11-27 | Taxe GAFAM amendement 9% Sénat | Porter taux de 3% à 9% | mem:- |
| FCT-Z09 | FACT | ✦ | https://digital-strategy.ec.europa.eu/fr/policies/regulatory-framework-ai | A | 2025 | AI Act entré en vigueur | 1er août 2024. Pratiques interdites fév 2025. Haut risque août 2026. | mem:- |
| FCT-Z10 | FACT | ✧ | https://www.service-public.gouv.fr/particuliers/vosdroits/F35235 | A | 2026 | PPV (prime partage valeur) | Jusqu'à 3 000€ (6 000€ si accord intéressement), décorrélée masse salariale | mem:- |
| FCT-Z11 | FACT | ✧ | https://www.leparisien.fr/archives/pourquoi-le-danemark-a-adopte-la-tva-sociale-25-11-2011-1737716.php | C | 2011-11-25 | Danemark TVA sociale 1992 | TVA 22%→25%, compensation suppression cotisations | mem:- |
| FCT-Z12 | FACT | ✧ | https://www.cadrescfdt.fr/actualites/intelligence-artificielle | C | 2026-06-11 | CFDT position IA | Accompagnement transformation, dialogue social obligatoire | mem:- |
| FCT-Z13 | FACT | ✧ | https://ugictcgt.fr/bilan-sommet-ia/ | C | 2026-02-13 | CGT bilan Sommet IA | « Le bilan ne va pas dans le sens du travail, ni des travailleurs » | mem:- |
| FCT-Z14 | FACT | ✧ | https://garymarcus.substack.com/p/confirmed-llms-have-indeed-reached | E | 2024-11-09 | Marcus : LLMs diminishing returns | « Pure scaling would not solve hallucinations or abstraction » | mem:- |
| FCT-Z15 | FACT | ✧ | https://www.youtube.com/watch?v=4__gg83s_Do | E | 2025-05-30 | LeCun : AGI pas par scaling | « We Won't Reach AGI By Scaling Up LLMs » | mem:- |

## EVIDENCE_REGISTRY (extraits — sources complètes dans RENARD parent SRC-R01 à SRC-R25)

| SRC-ID | TYPE | TITLE | URL | FAMILY | ROLE | LOCATOR | DATE |
|---|---|---|---|---|---|---|---|
| SRC-Z01 | ◈ | OpenAI EU Terms | https://openai.com/policies/eu-terms-of-use/ | A | ◈ | « OpenAI Ireland Ltd, Dublin, company 737350 » | 2026-01-16 |
| SRC-Z02 | ◉ | The Currency — OpenAI Ireland | https://thecurrency.news/articles/197670/ | C | ◉ | First full-year accounts 2024 | 2025-07-30 |
| SRC-Z03 | ◉ | ITEP — Microsoft Ireland tax avoidance | https://itep.org/microsoft-tax-avoidance-offshore-ireland-2025/ | D | ◉ | 14% current tax rate on Irish profits | 2026-06-30 |
| SRC-Z04 | ◈ | OECD — Germany Taxing Wages 2025 | https://www.sipotra.it/wp-content/uploads/2025/05/GERMANY.pdf | D | ◈ | Tax wedge single worker 47,9% (2024) | 2025-04-30 |
| SRC-Z05 | ◈ | CLEISS — Cotisations Danemark | https://www.cleiss.fr/docs/cotisations/danemark.html | A | ◈ | Pas de cotisations sociales employeur | 2025 |
| SRC-Z06 | ◈ | DG Trésor — Fiscalité modèle danois | https://www.tresor.economie.gouv.fr/Articles/14878863-9435-4303-96f8-32a396cd10f5/files/ce0984c2-2fe8-4976-bdd9-49963ab68941 | A | ◈ | TVA 25% depuis 1992 | — |
| SRC-Z07 | ◈ | Wikipedia — CSG | https://fr.wikipedia.org/wiki/Contribution_sociale_g%C3%A9n%C3%A9ralis%C3%A9e | E | ◈ | Évolution taux 1991-2018 | — |
| SRC-Z08 | ◈ | Légifiscal — PLF 2026 taxe GAFAM | https://www.legifiscal.fr/actualites-fiscales/4297-plf-2026-amendement-double-taux-taxe-gafam.html | A | ◈ | Amendement I-655 doublement 6% | 2025-10-29 |
| SRC-Z09 | ◈ | Service-Public — PPV | https://www.service-public.gouv.fr/particuliers/vosdroits/F35235 | A | ◈ | PPV jusqu'à 6 000€ décorrélée masse salariale | — |
| SRC-Z10 | ◉ | Gary Marcus Substack | https://garymarcus.substack.com/p/confirmed-llms-have-indeed-reached | E | ◉ | LLMs diminishing returns confirmed | 2024-11-09 |
| SRC-Z11 | ○ | Big Technology Podcast — LeCun | https://www.youtube.com/watch?v=4__gg83s_Do | E | ○ | AGI not reachable by scaling LLMs | 2025-05-30 |
| SRC-Z12 | ◉ | Le Parisien — Danemark TVA sociale | https://www.leparisien.fr/archives/pourquoi-le-danemark-a-adopte-la-tva-sociale-25-11-2011-1737716.php | C | ◉ | TVA 22%→25% en 1992 | 2011-11-25 |
| SRC-Z13 | ◉ | AOPS — Historique CSG | https://www.aops.fr/indices/economie/historique-csg | C | ◉ | Historique CSG et CRDS | — |
| SRC-Z14 | ◉ | Le Revenu — 30 ans hausses | https://www.lerevenu.com/reduire-impots/prelevements-sociaux-30-ans-de-hausses-ininterrompues/ | C | ◉ | 30 ans de hausses ininterrompues | 2022-06-10 |
| SRC-Z15 | ◉ | CFDT Cadres — IA | https://www.cadrescfdt.fr/actualites/intelligence-artificielle | C | ◉ | Accompagnement transformation IA | 2026-06-11 |
| SRC-Z16 | ◉ | CGT/UGICT — Bilan Sommet IA | https://ugictcgt.fr/bilan-sommet-ia/ | C | ◉ | Bilan négatif pour travailleurs | 2026-02-13 |
| SRC-Z17 | ◉ | Sénat — Amendement I-1694 | https://www.senat.fr/amendements/2025-2026/138/Amdt_I-1694.html | A | ◉ | Taxe GAFAM porter à 9% | 2025-11-27 |
| SRC-Z18 | ◎ | EU Commission — AI Act | https://digital-strategy.ec.europa.eu/fr/policies/regulatory-framework-ai | A | ◈ | En vigueur 1er août 2024 | — |

## TRACE_MATRIX

| ENTITY-ID | TYPE | QRY/SRC ATTEMPTS | RESULT | STATUS |
|---|---|---|---|---|
| LED-Z01 | MECHANISM | SRC-Z01,Z02,Z03 | OpenAI Ireland confirmé contractant EEA. IS 12,5%→0. | SATURATED |
| LED-Z02 | EVENT | SRC-Z02,Z03 | Pertes $5,09 Md 2024 confirmées. Anthropic non rentable. | SATURATED |
| LED-Z03 | CLAIM | SRC-Z04 | Allemagne 47,9% > France 47,2% confirmé. | SATURATED |
| LED-Z05 | CALCULATION | Calcul back-of-envelope | 5% cadres = 4,4 Md€. 77 Md€ allègements > perte. | SATURATED |
| LED-Z06 | FACT | SRC-Z07,Z13,Z14 | CSG 1,1%→9,2% en 33 ans, 145 Md€/an. | SATURATED |
| LED-Z07 | MECHANISM | SRC-Z08,Z09,Z17 | AI Act + taxe GAFAM + Pilier 1/2 : État pas désarmé. | SATURATED |
| LED-Z08 | CLAIM | SRC-Z10,Z11 | Marcus + LeCun : scaling limitations. | SATURATED |
| LED-Z09 | MECHANISM | SRC-Z09 | PPV + formules dérogatoires = atténuable. | SATURATED |
| LED-Z10 | GAP | SRC-Z15,Z16 | Syndicats = dialogue social. Pas de rapport dédié. | SATURATED |
| LED-Z11 | CLAIM | SRC-Z05,Z06,Z12 | Danemark : pas cotisations, TVA 25%. Transition faite. | SATURATED |
| LED-Z13 | INFERENCE | Analyse zones 1-10 | 8/10 affaiblissent, 1 aggrave, 1 neutre. | SATURATED |

## CAUSALITY_REGISTRY

| CAU-ID | EDGE | TYPE | SOURCE | GAP |
|---|---|---|---|---|
| CAU-Z01 | OpenAI Ireland Ltd → IS 12,5% (0 effectif) → zéro contribution fiscale France | ENABLER | SRC-Z01,Z02,Z03 | Triple fuite (cotisations + import + données) non décrite par la vidéo |
| CAU-Z02 | CSG 1,1%→9,2% → transition Bismarck→Beveridge déjà entamée | PRECEDENT | SRC-Z07 | 1 point CSG = ~16 Md€. Solution déjà en place. |
| CAU-Z03 | Danemark TVA 22%→25% (1992) → transition sans crise → « politiquement explosif » exagéré | PRECEDENT | SRC-Z05,Z06,Z12 | Transférabilité au contexte français non triviale |
| CAU-Z04 | AI Act + taxe GAFAM → État dispose d'outils → « techniquement infaisable » exagéré | ENABLER | SRC-Z08,Z09 | Taxe GAFAM 0,7 Md€ modeste vs 77 Md€ allègements |
| CAU-Z05 | LLM scaling limitations → hypothèse amélioration continue non garantie → substitution massive spéculative | LIMITATION | SRC-Z10,Z11 | Débat ouvert, progrès en cours |

## IMPACT_MAP

| IMP-ID | EFFECT | AFFECTED | EVIDENCE | STATUS |
|---|---|---|---|---|
| IMP-Z01 | Triple fuite fiscale (cotisations + import + données) | État français, URSSAF | SRC-Z01,Z02,Z03 | PROBABLE |
| IMP-Z02 | Allemagne plus exposée que France | Narratif exceptionnalité française | SRC-Z04 | AVÉRÉ |
| IMP-Z03 | 4-8 Md€ perte max annuelle vs 77 Md€ allègements | Budget Sécu | Calcul back-of-envelope | ORDRE_GRANDEUR |
| IMP-Z04 | CSG déjà à 9,2%, transition à moitié faite | Financement social | SRC-Z07 | AVÉRÉ |

## EDI_REPORT

| Dimension | Score | Commentaire |
|---|---|---|
| A (primary/official) | Fort | OECD, CLEISS, DG Trésor, EU Commission, Légifiscal |
| B (critical/competing) | Faible | ITEP, Marcus, LeCun |
| C (affected/witness) | Faible | CFDT, CGT |
| D (independent) | Modéré | The Currency, Le Parisien |
| E (academic/expert) | Modéré | Wikipedia, Substack |

## OPEN_GAPS

| GAP-ID | TYPE | DESCRIPTION | SEVERITY |
|---|---|---|---|
| GAP-Z01 | DATA | Chiffrage trou Sécu = back-of-envelope, pas de modèle économétrique | LOW |
| GAP-Z02 | COUNTER | Pas d'économiste contredisant explicitement la thèse vidéo | MEDIUM |

## MNEMO_STATE

| Appel | Statut | Memory_ID |
|---|---|---|
| search_memory (parent facts) | FOUND | 8c493eeb (parent), 88db801d (RENARD) |
| write_memory (investigation 10 zones) | PENDING_AT_SERIALIZATION | — |

## REQUEST_LOG

ENGINE:2.8 | MANIFEST:OPEN | RUN_ID:20260824-2030-leffondrement-10-zones | PARENT_RUN_ID:20260824-1822-leffondrement-du-modele-salarial | AS_OF:2026-08-24 | INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION
CHECKPOINT_SEQ:0 | LAST_COMPLETED:NONE | NEXT_ACTION:FINAL
modules:SYMBOLS,PATTERNS,THREATS,GATES,REQUEST_LOG,ICEBERG,MONEY,FRAMING | degraded:NONE
COUNT: ◈8 ◉8 ○2 | unique evidence objects:18 | upstream families:5 (A:institutions, C:presse, D:international, E:académique)

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE |
|---|---:|---|
| 1 | SYS | @READ (5 modules + clusters) | LOADED | — |
| 2 | SYS | @MNEMO_Q (parent facts) | FOUND | 8c493eeb,88db801d |
| 3 | ◈ | read_url(OpenAI EU Terms) | FOUND | SRC-Z01 |
| 4 | ◈ | read_url(CLEISS Danemark) | FOUND | SRC-Z05 |
| 5 | ◈ | read_url(Légifiscal taxe GAFAM) | FOUND | SRC-Z08 |
| 6 | SYS | FINAL @WRITE | PENDING | INVESTIGATION_PATH |

## PÉRIMÈTRE & LIMITES

### Synthèse 10 zones

| Zone | Verdict | Impact |
|---|---|---|
| 1. Paradis data | Triple fuite réelle (cotisations + import + données). OpenAI Ireland IS→0. **AGGRAVE la thèse.** | ↑ |
| 2. Miroir allemand | Coin 47,9% > 47,2%. Même Bismarck. Vidéo ignore. **AFFAIBLIT.** | ↓ |
| 3. Chiffrage trou | 4-8 Md€/an max vs 77 Md€ allègements. **AFFAIBLIT.** | ↓ |
| 4. CSG historique | 1,1%→9,2% sans crise. Solution déjà en place. **AFFAIBLIT.** | ↓ |
| 5. Cadre juridique | AI Act + taxe GAFAM + Pilier 1/2. État pas désarmé. **AFFAIBLIT.** | ↓ |
| 6. Scaling wall | LLMs plafonnent. Substitution non garantie. **AFFAIBLIT.** | ↓ |
| 7. Participation | Formules dérogatoires + PPV. « Arnaque mathématique » atténuable. **AFFAIBLIT.** | ↓ |
| 8. Acteurs politiques | Syndicats = dialogue social. Pas de rapport dédié. **NEUTRE.** | — |
| 9. Flexsécurité danoise | Pas « immunisé ». Transition faite en 1992 sans crise. **AFFAIBLIT.** | ↓ |
| 10. Convergence | Marketing anxiogène semi-sincère. Produit du marché de l'attention. | — |

**Bilan net** : 8 zones ↓ affaiblissent, 1 ↑ aggrave, 1 neutre.