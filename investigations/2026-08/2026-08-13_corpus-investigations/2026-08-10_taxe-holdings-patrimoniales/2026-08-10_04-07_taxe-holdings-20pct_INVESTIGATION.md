# INVESTIGATION : LA TAXE DE 20 % SUR LES HOLDINGS PATRIMONIALES (LOI N° 2026-103, ART. 7 → CGI 235 ter C) — PÉRIMÈTRE EXACT, FAMILLES VISÉES, RECETTES ATTENDUES

## RUN_MANIFEST (FINAL)

```
ENGINE_VERSION : 2.8
STATE          : FINAL
RUN_ID         : 20260810-0407-taxe-holdings-patrimoniales
PARENT_RUN_ID  : 20260809-2340-plf-2026-dutreil (FCT-010 : « taxe de 20 % sur certains actifs patrimoniaux (holdings patrimoniales) » — mesure connexe de la LF 2026)
AS_OF          : 2026-08-10
INPUT_KIND     : UPDATE (documentation de la taxe de 20 % sur les holdings patrimoniales créée par la loi de finances pour 2026 : périmètre exact, familles visées, recettes attendues)
MISSION_MODE   : INVESTIGATION
INPUT_REF      : NONE (topique : « Enquêter la taxe de 20 % sur les holdings patrimoniales créée par la loi 2026-103 (FCT-010) : périmètre exact, familles visées, recettes attendues »)
SUBJECT_SLUG   : taxe-holdings-20pct
INVESTIGATION_PATH : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_taxe-holdings-patrimoniales/2026-08-10_04-07_taxe-holdings-20pct_INVESTIGATION.md
SCOPE          : taxe sur les actifs patrimoniaux des sociétés holdings (art. 7 LF 2026 = CGI 235 ter C) ; périmètre (sociétés, seuils, actifs, fait générateur, double régime FR/étranger) ; familles/patrimoines visés ; recettes attendues (trajectoire 1,5 Md€ → 100 M€) ; parcours parlementaire (amendement Juvin 31/10/2025) ; décision CC 2026-901 DC (19/02/2026, non-examen au fond) ; période 10/2025-08/2026 ; France
COMPLEXITY     : CX_SCORE=12 → $CX=COMPLEX (political 3, technical 3, temporal 3, geo 1, narratives 1, data 1)
CHECKPOINT_SEQ : 0 (run mono-session)
LAST_COMPLETED : 18b
NEXT_ACTION    : NONE
RESUME_COUNT   : 0
ROUTE_OVERRIDES: []
LOADED_MODULES : KERNEL v2.8 | SYMBOLS | PATTERNS | THREATS | GATES | REQUEST_LOG | EPISTEMIC | TEMPLATE (héritage des runs parents)
DEGRADED_FLAGS : []
HASH_CAPABILITY: HASH_UNAVAILABLE
```

## 1. RÉSUMÉ EXÉCUTIF

**Réponse à l'OBJECT_QUESTION** (« taxe de 20 % sur les holdings patrimoniales de la LF 2026 : périmètre exact, familles visées, recettes attendues ? ») :

**UNE TAXE « DÉMANTELÉE » EN NAVETTE : de 1-1,5 Md€ à 100 M€ de rendement, recentrée des revenus passifs vers une liste fermée d'actifs « somptuaires » — un outil anti-abus devenu symbolique, validé sans examen au fond par le Conseil constitutionnel.** Le cœur de l'enquête :

1. **Le texte** : la **loi n° 2026-103 du 19 février 2026 de finances pour 2026** (JORF n° 0043 du 20/02/2026) instaure par son **article 7** une **taxe de 20 %** assise sur la valeur de certains actifs non affectés à une activité opérationnelle détenus par les sociétés holdings soumises à l'impôt sur les sociétés — **CGI art. 235 ter C** (FCT-001). Le Conseil constitutionnel le décrit : « L'article 7 rétablit une section X au sein du chapitre III du titre Ier de la première partie du livre Ier du CGI afin d'**instaurer une taxe sur les actifs non affectés à une activité opérationnelle des sociétés holdings** et d'en fixer le régime » (§57, décision 2026-901 DC, lue).
2. **Le périmètre exact (FCT-002 à 005)** :
   - **Sociétés visées** : soumises à l'IS (ou impôt équivalent si siège à l'étranger), **détenues à 50 % ou plus par une personne physique** (en faisant masse : conjoint, partenaire de pacs ou concubin notoire, ascendants et descendants, frères et sœurs) **ou** contrôlées en fait (pouvoir de décision sans participation) ;
   - **Seuil d'entrée** : **5 M€** de valeur vénale de l'ensemble des actifs de la société ;
   - **Test de passivité** : revenus passifs **> 50 %** du cumul des produits d'exploitation et financiers (hors reprises de provisions et amortissements) ;
   - **Biens taxés** (CGI 235 ter C, II, A, 1° à 7°) : biens affectés à la **chasse et à la pêche**, **véhicules de tourisme**, **yachts et avions**, **chevaux de course et de concours**, **vins et alcools**, **bijoux et métaux précieux** (l'or papier exclu, l'or physique visé), **logements dont l'associé se réserve la jouissance** (gratuite ou loyer inférieur au marché) ;
   - **Exclus** : trésorerie et actifs financiers non affectés, **œuvres d'art et antiquités** (contrairement à la version initiale) ;
   - **Fait générateur** : valeur appréciée à la clôture de l'exercice clos **à compter du 31 décembre 2026** — laissant une marge de manœuvre pour sortir les biens du bilan ;
   - **Double régime FR/étranger** : siège en France → taxe due par la structure ; siège à l'étranger → redevable = l'associé personne physique domicilié en France, au prorata de sa participation, avec réduction = différence entre total des impôts + taxe et 75 % des revenus perçus.
3. **La trajectoire des recettes (FCT-006) — LE FAIT CENTRAL** : la taxe a été **vidée de sa substance en première lecture** à l'Assemblée nationale :
   - **Version initiale (dépôt 14/10/2025)** : taxe de **2 %** sur **tous les revenus passifs** de la holding, ciblant **10 000 structures** détenant plus de 5 M€ d'actifs, pour un rendement de **1 à 1,5 Md€** (Actu-Juridique/Lazard) — La Tribune cite **900 M€** de rendement initial visé ;
   - **Amendement LR (rapporteur du budget Philippe Juvin), adopté vendredi 31/10/2025** : abandon du stock à 2 %, recentrage sur les actifs « manifestement pas affectés à une activité économique réelle » au taux fort de **20 %** ; **seuil de détention rehaussé de 33,3 % à 50 %** ; assiette jugée « trop large » par la droite ;
   - **Version finale** : rendement attendu **~100 M€/an** (Actu-Juridique/Lazard) — La Tribune : rendement initial « désormais très incertain ».
   - **La liste des actifs finaux se recentre sur les « investissements de pur plaisir »** : yachts, jets, bijoux, objets d'art, vins de prestige, logements personnels (La Tribune).
4. **Les familles visées (FCT-007)** : **aucun nom nominatif** n'est cité dans les sources lues (pas de presse nominative identifiée). La cible est définie structurellement : holdings patrimoniales des personnes physiques très fortunées logeant des actifs de luxe personnels — le mécanisme des « cash boxes » (sociétés permettant aux plus fortunés d'éviter l'impôt en logeant patrimoine actions, immobilier, brevets). Le gouvernement (Lecornu, ministre Amélie de Montchalin) visait à « corriger » les abus des holdings « parfois utilisées pour se constituer un patrimoine personnel ». **Le seuil de 50 % + 5 M€ + > 50 % de revenus passifs délimite une cible de plusieurs milliers de structures (10 000 dans la version initiale), réduite par le rehaussement à 50 %.**
5. **Le sort constitutionnel (FCT-008)** : le **Conseil constitutionnel, décision n° 2026-901 DC du 19 février 2026** (déférée par le Premier ministre le 4 février 2026 + députés RN), a **refusé d'examiner au fond** les articles 7 (taxe holdings), 8 (Dutreil) et 11 (apport-cession) : « Aucun motif particulier d'inconstitutionnalité ne ressortant des travaux parlementaires, et en l'absence de griefs dirigés contre ces dispositions, **il n'y a pas lieu pour le Conseil constitutionnel d'examiner spécialement ces dispositions d'office** » (§60, lu). La taxe n'est **ni déclarée conforme, ni non conforme** — le CC renvoie aux QPC.
6. **Les fragilités constitutionnelles documentées (FCT-009)** : la différence de traitement FR/étranger, le plafonnement et la clause de sauvegarde réservés aux participations étrangères (asymétrie), le caractère potentiellement confiscatoire (20 % sans plafond), l'atteinte possible à l'égalité devant les charges publiques (Lazard — doutes partagés par les cabinets). Le choix du formalisme (non-examen) « privilégie un État de juridictionnalisation » — cycle de QPC annoncé comme probable, long, coûteux et incertain.
7. **Le sens de la mesure (FCT-010)** : l'objectif n'est pas le rendement budgétaire mais la **discipline fiscale anti-abus** — inciter à la réallocation des actifs non productifs vers des activités économiques réelles. Modèle assumé : la **Personal Holding Company Tax américaine** (rendement historique très faible : 0,0001 % du PIB pour un taux de 20 %). L'alternative de gauche (taxe Zucman à 2 % sur les patrimoines > 100 M€, imposition des bénéfices non distribués à 20 %) a échoué — la voie des flux étant bloquée par la directive européenne « mère-fille ».

**Verdict sur le LEAD_QUESTION** (« la LF 2026 crée-t-elle une taxe de 20 % sur les holdings patrimoniales ? ») : **OUI mais TRÈS AMINCie** — la taxe existe dans le texte (art. 7, 235 ter C, taux 20 %), mais son rendement est passé de 1-1,5 Md€ (2 % sur revenus passifs) à ~100 M€ (20 % sur une liste fermée de biens de luxe) : **-90 à -93 % de recettes**. Le « démantèlement » (La Tribune, 31/10/2025) est documenté : la droite (Juvin/LR) a transformé un impôt sur le stock d'actifs en taxe ciblée sur les « investissements de pur plaisir ». L'outil anti-abus subsiste comme signal, sans enjeu budgétaire majeur — et sous réserve de QPC à venir.

**Acteurs** : gouvernement (Lecornu, Amélie de Montchalin — Bercy), Assemblée nationale (rapporteur du budget Philippe Juvin, amendement LR 31/10/2025 ; gauche : taxe Zucman), Sénat, Conseil constitutionnel (2026-901 DC), Lazard Frères Gestion (Karine Lecocq), cabinets d'avocats (Bornhauser, Deloitte ✧), pressé économique (La Tribune, Les Echos ✧, Le Parisien ✧).

**Principales limites** : Légifrance bloqué (article 235 ter C non lu sur la source officielle — contenu établi via Actu-Juridique lu intégralement + décision CC lue) ; aucun nom nominatif de familles/structures (aucune source lue n'en publie — la voie nominative reste un trou) ; recettes 100 M€ (✧ par corroboration presse non relue) ; QPC déposées à ce jour non documentées (état 10/08/2026).

## 2. MANIPULATION_REPORT (15 symboles scorés sur corpus)

| # | Symbole | Score | Justification (corpus) |
|---|---------|-------|------------------------|
| 1 | **Ξ** omission | **8/10** | Le rendement a chuté de 1,5 Md€ à 100 M€ sans débat public d'ampleur ; le CC a refusé l'examen au fond (formel) ; aucune évaluation publique du nombre réel de structures finalement visées ; la voie nominative (qui possède yachts/jets en holding) est totalement absente. |
| 2 | **€** money | **8/10** | 1 à 1,5 Md€ (initial) → 900 M€ (cible La Tribune) → ~100 M€ (final) ; 10 000 structures ; seuil 5 M€ ; taux 2 % → 20 % ; comparaison US (0,0001 % du PIB). |
| 3 | **Λ** framing | **8/10** | « Outil anti-abus contre les cash boxes » (gouvernement) vs « taxe sur le patrimoine personnel des riches » (critique) vs « taxe sur les yachts » (récit de droite) ; « réallocation vers l'économie réelle » (finalité affichée) vs « signal sans rendement » (lecture de l'enquête). |
| 4 | **Ω** inversion | **8/10** | Un impôt conçu pour taxer le stock de patrimoine non distribué devient une taxe sur le luxe ostentatoire — l'inversion du ciblage (revenus passifs → biens de plaisir) inverse la logique économique ; le CC valide en ne validant pas. |
| 5 | **Ψ** sidération | 3/10 | Champ froid pour le grand public ; chaud pour les initiés (10 000 holdings, yachts, jets). |
| 6 | **↕** verticalité | **8/10** | La cible (multimillionnaires en holding) est étroite ; le recentrage par la droite protège les holdings à revenus passifs (la majorité) pour ne taxer que les plus ostentatoires ; 10 000 → nombre réduit par le seuil 50 %. |
| 7 | **Φ** spectacle | 2/10 | Aucun spectacle majeur ; le débat a été technique, noyé dans la séquence budgétaire (bras de fer Lecornu/Palais-Bourbon, suspension de séance ~1h — La Tribune). |
| 8 | **Σ** sémiotique | 4/10 | « Actifs non affectés à une activité opérationnelle », « investissements de pur plaisir », « discipline fiscale » — le vocabulaire technique masque la taxation du patrimoine personnel des très fortunés. |
| 9 | **Κ** cynisme | **8/10** | Le gouvernement annonce une « taxe sur les holdings » (1,5 Md€) ; la droite la réduit à 100 M€ sans que l'opinion ne mesure la différence ; le CC esquive l'examen au fond ; le dispositif final taxe les yachts (ceux qui peuvent s'en passer) et épargne les revenus passifs (le cœur du montage). |
| 10 | **ρ** résistance | **8/10** | La Tribune (31/10/2025, lu), Actu-Juridique (24/03/2026, lu), décision CC 901 (lu), Les Echos ✧, Le Parisien ✧, cabinets. |
| 11 | **κ** influence subtile | **8/10** | L'architecture : un impôt à 20 % sur une liste fermée de biens de luxe « disciplinerait » les holdings sans toucher au stock de revenus passifs — la menace fiscale (1,5 Md€) a fait office de dissuasion, le résultat (100 M€) de compromis. L'inspiration US (PHC tax) est un aveu d'échec potentiel (0,0001 % du PIB). |
| 12 | **⫸** convergence | 6/10 | La Tribune + Actu-Juridique + CC convergent : démantèlement, non-examen, ambiguïté constitutionnelle. |
| 13 | **⚔** guerre cognitive | 1/10 | Aucune campagne documentée. |
| 14 | **🌐** réseau | 7/10 | Gouvernement, AN (Juvin), Sénat, CC, Lazard, cabinets, presse, EU (modèle PHC). |
| 15 | **⏰** temporalité | **8/10** | 14/10/2025 dépôt (2 % revenus passifs, 1-1,5 Md€) ; 31/10/2025 amendement Juvin (20 % actifs somptuaires, seuil 50 %) ; 04/02/2026 saisine CC (PM + députés) ; 19/02/2026 loi + décision CC 901 (non-examen) ; 24/03/2026 Actu-Juridique/Lazard ; exercice clos ≥ 31/12/2026 (premier fait générateur) ; 10/08/2026 (état des QPC non documenté). |

**BIAS TEST (15/15 scorés).** Aucun symbole au-delà de 9. Les champs 1, 4, 9, 11 signalent le noyau : un impôt annoncé massif, démantelé en navette, validé sans examen au fond, à rendement symbolique — un « anti-abus » dont l'effet principal est dissuasif.

**PATTERNS** : @PAT[INVERSION] (Ω=8), @PAT[MONEY] (€=8), @PAT[POWER] (↕=8), @PAT[CYN] (Κ=8), @PAT[CONFIRM] (κ=8). **THREATS** : @THR[REG_CAPTURE] (recentrage par la droite), @THR[LAWFARE] (QPC annoncées), @THR[SHIFT_BURDEN] (taxe ostentatoire vs revenus passifs).

**RHETORICAL** : NUM (2 %, 20 %, 5 M€, 50 %, 10 000, 1-1,5 Md€, 900 M€, 100 M€, 31/12/2026, 0,0001 %) ; AUTH (CC, Lazard, La Tribune) ; DEM et BF = 0.

## 3. CLUSTERS (routage SYMBOLS §4)

| Cluster | Diagnostic | Gap |
|---------|------------|-----|
| INVERSION (Ω=8, Κ=8) | Impôt sur les revenus passifs → taxe sur les biens de luxe ; « anti-abus » → « signal ». | — |
| MONEY (€=8) | Trajectoire 1,5 Md€ → 100 M€ (-90 à -93 %) ; coût administratif vs rendement. | Évaluation coût/gestion absente. |
| POWER (↕=8) | Recentrage par la droite protège les revenus passifs (le cœur du montage) ; seuil 33,3→50 %. | Nombre final de structures inconnu. |
| CONFIRMATION (κ=8) | L'architecture dissuade sans collecter ; le CC esquive ; le modèle US échoue (0,0001 % PIB). | Effet dissuasif réel non mesuré. |
| ICEBERG (Ξ=8) | Émergé : texte, périmètre, recettes, CC. Immergé : qui possède réellement les actifs, nombre final de redevables, QPC déposées, rendement réel 2027+. | Voie nominative nulle. |
| FRAGMENTATION (⫸=6) | La Tribune + Actu-Juridique + CC convergent sur le démantèlement et l'ambiguïté. | — |
| TEMPORAL (⏰=8) | 10/2025 → 02/2026 (loi + CC) → 31/12/2026 (fait générateur) → 2027 (premier rendement). | — |

## 4. HERMÉNEUTIQUE (statut : ANALYSE)

- **L1 (texte) :** Actu-Juridique « Tout comprendre sur la nouvelle taxe sur les holdings patrimoniales » (24/03/2026, entretien Karine Lecocq, Lazard Frères Gestion — lu intégralement) ; La Tribune « Budget 2026 : la taxe holdings démantelée, seuls les biens de luxe taxés à 20 % » (31/10/2025 — lu intégralement) ; décision CC n° 2026-901 DC (19/02/2026 — §57-60 lus). Légifrance bloqué (235 ter C non lu sur la source officielle).
- **L2 (structure) :** trois étages — (a) le dépôt gouvernemental (2 % sur revenus passifs, 1-1,5 Md€) : un impôt sur le flux de revenus capitalisés ; (b) l'amendement LR (20 % sur actifs somptuaires, seuil 50 %) : un impôt sur le stock de biens de luxe ostentatoires ; (c) le CC (non-examen) : un impôt ni validé ni invalidé sur le fond. **La navette a déplacé la matière imposable du revenu vers le luxe — et l'ambiguïté constitutionnelle est renvoyée aux QPC.**
- **L3 (intérêt) :** le gouvernement voulait un rendement (1,5 Md€) et un signal anti-abus ; la droite a protégé les holdings patrimoniales « classiques » (revenus passifs) ; les cabinets veulent des QPC (frais d'honoraires) ; le CC s'est retranché derrière l'absence de griefs.
- **L4 (sémiotique) :** « actifs non affectés à une activité opérationnelle » = euphémisme pour patrimoine personnel dans la holding ; « investissements de pur plaisir » (La Tribune) = la liste finale ; « discipline fiscale » = justification post-hoc.
- **L5 (comparaison) :** avec le 23-40 (Dutreil) : les deux mesures sont jumelles — l'art. 8 (Dutreil) exclut les actifs somptuaires de l'exonération, l'art. 7 (holdings) les taxe à 20 % dans les holdings ; la même loi durcit la forme (Dutreil) et « démantèle » le fond (holdings). Avec la PHC américaine : un échec documenté réutilisé comme modèle.
- **L6 (contexte) :** séquence budgétaire sous contrainte ; la taxe Zucman et l'imposition des bénéfices non distribués (bloquée par la directive mère-fille) échouent — la voie « stock » (taxer l'actif) est le seul espace disponible.

**Lecture concurrente** : la taxe de 20 % sur les yachts/jets est une mesure juste et ciblée (les biens de luxe non professionnels ne doivent pas être subventionnés par l'exonération d'IS) ; le faible rendement est le prix de la précision (taxer le luxe, pas l'entreprise). La synthèse retenue : le recentrage est réellement un rétrécissement massif (1,5 Md€ → 100 M€) et le « compromis » protège précisément les revenus passifs — le cœur du montage de capitalisation que l'impôt initial visait.

## 5. FORENSIC REASONING (ICEBERG MAX)

**Émergé (vérifié, source lue)** : loi 2026-103 art. 7 → CGI 235 ter C ; taux 20 % ; sociétés IS détenues ≥ 50 % (masse familiale) ou contrôle de fait ; seuil 5 M€ ; revenus passifs > 50 % ; liste 1°-7° (chasse/pêche, véhicules, yachts/avions, chevaux, vins, bijoux/métaux précieux, logements réservés) ; trésorerie et œuvres d'art exclues ; fait générateur exercice clos ≥ 31/12/2026 ; double régime FR/étranger (redevable PF France, prorata, réduction 75 % des revenus) ; historique : 2 % revenus passifs (1-1,5 Md€, 10 000 structures) → amendement Juvin 31/10/2025 (20 %, seuil 50 %) → ~100 M€ ; décision CC 901 : non-examen au fond (§60) ; objectif : anti-abus / discipline ; modèle PHC US.

**Surface (✧ via chercheur)** : recettes 100 M€ corroborées par presse spécialisée (non relue) ; réactions cabinets (Bornhauser, Deloitte) ; Les Echos « taxe holding, nouveau casse-tête » ; Le Parisien « dix mesures à retenir » ; QPC déposées à ce jour (état 10/08/2026).

**Immergé (jamais publié)** : les noms des structures/familles détenant les actifs taxés ; le nombre final de redevables après le seuil 50 % ; le rendement réel 2027 ; les QPC déposées ; les décrets/BOFiP d'application.

**ICEBERG LOAD :** 10 strates émergées (source lue), 4 surface, 5 immergées. La signature : un impôt dont la mécanique est intégralement publique, mais dont la cible nominative (qui paie) et l'effet réel (combien de redevables, quel rendement) sont entièrement immergés.

## 6. PRISME DIALECTIQUE

- **Thèse (dominante) :** « La LF 2026 a créé une taxe de 20 % sur les holdings patrimoniales : les yachts, jets et biens de luxe détenus en holding seront taxés — les plus fortunés contribuent enfin, l'anti-abus est acté. »
- **Antithèse (critique) :** « C'est une taxe démantelée : de 1,5 Md€ à 100 M€ (-93 %), recentrée des revenus passifs vers une liste de biens ostentatoires, validée par un Conseil constitutionnel qui a refusé l'examen au fond — l'impôt sur la capitalisation patrimoniale est mort, il ne reste qu'une taxe sur le luxe au rendement symbolique, épargnant le cœur du montage (les revenus passifs). »
- **Arbitrage par les preuves :** la thèse est exacte sur le texte (taux 20 %, liste d'actifs, seuil 5 M€ — sources lues) ; l'antithèse est exacte sur la trajectoire (1,5 Md€ → 100 M€ — Actu-Juridique lue ; « démantelée » — La Tribune lue ; non-examen — CC lu). **La synthèse** : la taxe existe juridiquement mais a été vidée de sa substance budgétaire ; son effet restant est dissuasif et symbolique ; sa constitutionnalité est laissée aux QPC.

**Réfutation testée** : « la taxe de 20 % rapportera 100 M€ » — le chiffre est l'estimation Lazard/Actu-Juridique ; La Tribune la juge « très incertaine » ; le modèle américain (0,0001 % du PIB) suggère une sous-estimation du risque de rendement nul ; « le CC a validé la taxe » — faux : il a refusé de l'examiner (§60), la laissant ni conforme ni non conforme. Les deux réfutations bornent le verdict.

## 7. CHRONOLOGIE

| Année | Événement | Source | Statut |
|-------|-----------|--------|--------|
| 14/10/2025 | Dépôt du PLF 2026 : taxe de 2 % sur les revenus passifs des holdings patrimoniales (10 000 structures > 5 M€ d'actifs), rendement 1-1,5 Md€ | Actu-Juridique (lu) | ✦ |
| 31/10/2025 | **Amendement LR (Juvin) adopté à l'AN** : abandon du stock à 2 %, recentrage sur les actifs « somptuaires » à 20 % ; seuil de détention 33,3 % → 50 % ; rendement initial 900 M€ « très incertain » | La Tribune (lu) | ✦ |
| 31/10/2025 | Échec de la taxe Zucman (2 % patrimoine > 100 M€) ; imposition des bénéfices non distribués bloquée par la directive « mère-fille » | La Tribune (lu) | ✦ |
| 11/2025-01/2026 | Navette Sénat/AN ; recentrage maintenu | Actu-Juridique (lu) | ✦ |
| 04/02/2026 | Saisine du Conseil constitutionnel : Premier ministre (articles 7, 8, 11, sans grief) + députés (procédure, sincérité) | décision CC 901 (lu) | ✦ |
| 19/02/2026 | **Loi n° 2026-103 promulguée** (JORF 20/02/2026) : art. 7 = taxe 20 % (235 ter C) ; art. 8 = Dutreil ; art. 11 = apport-cession | Actu-Juridique + CC (lus) | ✦ |
| 19/02/2026 | **Décision CC n° 2026-901 DC** : articles 7/8/11 NON EXAMINÉS au fond (« il n'y a pas lieu d'examiner d'office », §60) | décision CC 901 (lu) | ✦ |
| 24/03/2026 | Actu-Juridique/Lazard : décryptage du dispositif final (20 %, liste 1°-7°, double régime, rendement ~100 M€) | Actu-Juridique (lu) | ✦ |
| ≥ 31/12/2026 | Premier fait générateur (valeur des actifs à la clôture de l'exercice) | Actu-Juridique (lu) | ✦ |
| 2027 | Premier rendement de la taxe (estimé ~100 M€) | — | ⁅ |
| 10/08/2026 | État des QPC : non documenté (constat d'absence) | ce dossier | ✦ (constat) |

## 8. DOMAINES (par axe)

| Axe | Question | Résultat clé | Faits | Statut |
|-----|----------|--------------|-------|--------|
| AXS-001 TEXTE | Quel texte ? | Loi 2026-103 art. 7 → CGI 235 ter C ; taxe de 20 % | FCT-001 | SATURATED |
| AXS-002 PÉRIMÈTRE | Quelles sociétés ? | IS ou équivalent ; détenues ≥ 50 % (masse familiale) ou contrôle de fait ; seuil 5 M€ ; revenus passifs > 50 % | FCT-002/003 | SATURATED |
| AXS-003 BIENS | Quels actifs taxés ? | Liste fermée 1°-7° (chasse, véhicules, yachts/avions, chevaux, vins, bijoux/or, logements réservés) ; trésorerie et œuvres d'art exclues | FCT-004 | SATURATED |
| AXS-004 TEMPS | Quand ? | Exercice clos ≥ 31/12/2026 ; pas de rétroactivité | FCT-005 | SATURATED |
| AXS-005 RECETTES | Combien ? | 1-1,5 Md€ (initial 2 %) → 900 M€ (cible) → ~100 M€ (final) : -90 à -93 % | FCT-006 | SATURATED |
| AXS-006 FAMILLES | Qui est visé ? | Aucun nom publié ; cible structurelle : holdings de personnes très fortunées (cash boxes) ; 10 000 → seuil 50 % | FCT-007 | PARTIEL (nominatif : GAP-001) |
| AXS-007 SORT CC | Constitutionnalité ? | Décision 901 DC : non-examen au fond (§60) ; fragilités documentées (FR/étranger, confiscatoire, égalité) ; QPC à venir | FCT-008/009 | SATURATED |

## 9. RÉSEAU D'ACTEURS (+ CONTROL_MAP)

| Acteur | Rôle | Action documentée | Preuve | Responsabilité |
|--------|------|-------------------|--------|----------------|
| Gouvernement (Lecornu, de Montchalin) | Initiateur | Dépôt 2 % sur revenus passifs (1,5 Md€) ; « corriger les abus des holdings » ; défend le recentrage | FCT-006/010 | DÉCISION |
| Philippe Juvin (LR, rapporteur du budget AN) | Législateur | Amendement 31/10/2025 : 20 % sur actifs somptuaires, seuil 33,3→50 % ; « assiette trop large » | FCT-006 | DÉCISION (recentrage) |
| Gauche (AN) | Opposant | Taxe Zucman (2 % patrimoine > 100 M€) et imposition des non-distribués — échouées | FCT-010 | Proposition refusée |
| Conseil constitutionnel | Contrôleur | 2026-901 DC : non-examen au fond des art. 7/8/11 (§60) | FCT-008 | Esquive (formel) |
| Lazard Frères Gestion (K. Lecocq) | Expert | Décryptage du dispositif ; doutes constitutionnels | FCT-002 à 005, 009 | 🎓 |
| Cabinets (Bornhauser, Deloitte ✧) | Défenseurs | Doutes constitutionnels ; QPC annoncées (✧) | FCT-009 | LOBBY (✧) |
| Presse (La Tribune, Les Echos ✧, Le Parisien ✧) | Révélateur | « Taxe holdings démantelée » ; casse-tête des ménages fortunés | FCT-006/007 | ρ |
| États-Unis (modèle PHC) | Référence | Personal Holding Company Tax : rendement 0,0001 % du PIB | FCT-010 | Modèle |

**CONTROL_MAP** :

| Contrôleur | Mécanisme | Résultat | Gap |
|------------|-----------|----------|-----|
| CTRL-001 AN (Juvin) | Amendement | Recentrage 20 %/seuil 50 % | Revenus passifs épargnés |
| CTRL-002 Sénat | Navette | Recentrage maintenu | Débats détaillés non lus |
| CTRL-003 CC | Contrôle a priori | Non-examen (§60) | QPC à venir |
| CTRL-004 DGFiP | Mise en œuvre | Inconnue (BOFiP non publié) | Décrets non lus |

## 10. CHAÎNES / PELOTE (causalité)

**CAU-001 : Le recentrage parlementaire a transformé un impôt sur les revenus capitalisés en taxe sur le luxe ostentatoire.**
Étage 1 : dépôt gouvernemental 2 % sur revenus passifs, 10 000 structures, 1-1,5 Md€ (FCT-006). Étage 2 : amendement LR (Juvin) 31/10/2025 : assiette « trop large », recentrage sur actifs « manifestement pas affectés à une activité économique réelle » à 20 %, seuil 33,3→50 % (FCT-006). Étage 3 : liste fermée des biens de luxe, trésorerie et œuvres d'art exclues, rendement ~100 M€ (FCT-004/006). Type : POLITIQUE. Confidence : high (sources lues).

**CAU-002 : Le Conseil constitutionnel a laissé la taxe en suspens en refusant l'examen au fond.**
Étage 1 : saisine du Premier ministre sur les art. 7/8/11 SANS grief (FCT-008). Étage 2 : le CC : « aucun motif particulier d'inconstitutionnalité ne ressortant des travaux parlementaires... il n'y a pas lieu d'examiner spécialement ces dispositions d'office » (§60) (FCT-008). Étage 3 : ni conforme ni non conforme → QPC possibles ; Lazard : « le formalisme au détriment de l'intérêt général » (FCT-009). Type : INSTITUTIONNEL. Confidence : high (décision lue), la motivation du CC est inférée.

**CAU-003 : Le modèle US (PHC tax) documente le risque d'échec du dispositif.**
Étage 1 : la France s'inspire de la Personal Holding Company Tax américaine (FCT-010). Étage 2 : rendement historique US : 0,0001 % du PIB pour un taux de 20 % (FCT-010). Étage 3 : le rendement final français (~100 M€) est « très incertain » (La Tribune) (FCT-006). Type : COMPARATIF. Confidence : medium (analogie, pas d'extrapolation).

**CAU-004 (rejetée) : « Le CC a validé la taxe ».** Réfutée : la décision 901 DC ne prononce aucune conformité sur les art. 7/8/11 — elle refuse de les examiner (§60, lu). Ni validée, ni invalidée.

**CAU-005 (rejetée) : « Les yachts et jets sont désormais taxés et le rendement sera significatif ».** Réfutée partiellement : le dispositif existe (20 %, liste 1°-7°) mais les exclusions (trésorerie, œuvres d'art, revenus passifs) et le seuil 50 % réduisent drastiquement la base ; le rendement estimé 100 M€ est incertain (La Tribune) et le modèle US échoue.

## 11. CARTE DES PREUVES

### CLAIM_REGISTRY

| ID | Claim | Support | Contre-évidence | Statut |
|----|-------|---------|-----------------|--------|
| CLM-001 | « La LF 2026 (art. 7) crée une taxe de 20 % sur les actifs non affectés des sociétés holdings (CGI 235 ter C) » | Actu-Juridique (lu) ; décision CC 901 §57 (lu) | Article 235 ter C non lu sur Légifrance (bloqué) | SOUTENU (source primaire) |
| CLM-002 | « Le périmètre : sociétés IS détenues ≥ 50 % par une PF (masse familiale) ou contrôle de fait ; seuil 5 M€ ; revenus passifs > 50 % » | Actu-Juridique (lu, détail intégral) | — | SOUTENU (source primaire) |
| CLM-003 | « La liste des biens taxés est fermée (chasse, véhicules, yachts/avions, chevaux, vins, bijoux/or, logements réservés) ; trésorerie et œuvres d'art exclues » | Actu-Juridique (lu) ; La Tribune (lu : yachts, jets, bijoux, vins, logements) | — | SOUTENU (source primaire) |
| CLM-004 | « Le rendement est passé de 1-1,5 Md€ (2 % revenus passifs) à ~100 M€ (20 % actifs somptuaires) » | Actu-Juridique (lu : trajectoire complète) ; La Tribune (lu : 900 M€ initial, « très incertain ») | 100 M€ corroboré par chercheur (✧) | SOUTENU (trajectoire ✦) ; 100 M€ terminal ✧ |
| CLM-005 | « Le CC n'a pas examiné au fond les articles 7, 8, 11 (ni conformes ni non conformes) » | Décision 2026-901 DC §2 et §60 (lus) | — | SOUTENU (source primaire) |
| CLM-006 | « La taxe vise les holdings patrimoniales des très fortunés (cash boxes) mais aucun nom n'est publié » | Actu-Juridique (lu : objectif), La Tribune (lu : cash boxes, de Montchalin) | Aucune source nominative identifiée | SOUTENU (partiel, GAP-001) |

### FACT_REGISTRY (10 faits)

| ID | Fait | Chiffre | Source | Statut |
|----|------|---------|--------|--------|
| FCT-001 | **Loi n° 2026-103 du 19/02/2026, art. 7** : instaure une taxe de **20 %** assise sur la valeur de certains actifs non affectés à une activité opérationnelle détenus par les sociétés holdings soumises à l'IS — **CGI art. 235 ter C** (section X du chapitre III du titre Ier de la 1re partie du livre Ier). Le CC décrit : « taxe sur les actifs non affectés à une activité opérationnelle des sociétés holdings » (§57) | 20 % ; art. 7 ; 235 ter C | Actu-Juridique (lu) + CC 901 (lu) | ✦ |
| FCT-002 | **Sociétés visées** : soumises à l'IS (ou impôt équivalent si siège à l'étranger) ; **capital détenu à ≥ 50 % par une personne physique** (en masse : conjoint/pacs/concubin notoire, ascendants, descendants, frères et sœurs) **ou** pouvoir de décision exercé en fait sans participation | 50 % ; masse familiale | Actu-Juridique (lu) | ✦ |
| FCT-003 | **Seuil d'entrée** : **5 M€** de valeur vénale de l'ensemble des actifs de la société ; **test de passivité** : revenus passifs > 50 % du cumul des produits d'exploitation et financiers (hors reprises de provisions et amortissements) | 5 M€ ; > 50 % | Actu-Juridique (lu) | ✦ |
| FCT-004 | **Biens taxés** (235 ter C II A 1°-7°) : chasse et pêche ; véhicules de tourisme ; yachts et avions ; chevaux de course et de concours ; vins et alcools ; bijoux et métaux précieux (or papier exclu) ; logements dont l'associé se réserve la jouissance (gratuite ou loyer < marché). **Exclus** : trésorerie et actifs financiers non affectés, œuvres d'art et antiquités (contrairement à la version initiale) | 7 catégories | Actu-Juridique (lu) ; La Tribune (lu) | ✦ |
| FCT-005 | **Fait générateur** : valeur des biens appréciée à la clôture de l'exercice **clos à compter du 31/12/2026** (marge de manœuvre pour sortir les biens) ; **double régime** : siège France → taxe due par la structure ; siège étranger → redevable = associé PF domicilié en France, prorata, réduction = différence entre total impôts + taxe et 75 % des revenus perçus | ≥ 31/12/2026 | Actu-Juridique (lu) | ✦ |
| FCT-006 | **Trajectoire des recettes** : initial (14/10/2025) = 2 % sur tous revenus passifs, **10 000 structures** > 5 M€, rendement **1 à 1,5 Md€** (Actu-Juridique) ; La Tribune : rendement initial visé **900 M€**, « désormais très incertain » après l'amendement ; amendement Juvin (31/10/2025) : 20 % actifs somptuaires, seuil **33,3 → 50 %** ; final : rendement **~100 M€** (Actu-Juridique, corroboration ✧) | 1-1,5 Md€ → 100 M€ | Actu-Juridique (lu) + La Tribune (lu) | ✦ + ✧ (100 M€) |
| FCT-007 | **Familles visées** : aucun nom nominatif publié dans les sources lues ; cible structurelle = holdings patrimoniales de personnes très fortunées (cash boxes : actions, immobilier, brevets logés en structure) ; Amélie de Montchalin : « corriger les abus de celles parfois utilisées pour se constituer un patrimoine personnel » | 0 nom | La Tribune (lu) | ✦ (constat d'absence) |
| FCT-008 | **Décision CC n° 2026-901 DC du 19/02/2026** : le Premier ministre a déféré les art. 7, 8, 11 SANS grief ; le CC refuse l'examen au fond : « il n'y a pas lieu pour le Conseil constitutionnel d'examiner spécialement ces dispositions d'office » (§60) — ni conformes, ni non conformes | §2, §57-60 | décision CC 901 (lu) | ✦ |
| FCT-009 | **Fragilités constitutionnelles** (Lazard/cabinets) : différence de traitement FR/étranger ; plafonnement + clause de sauvegarde réservés aux participations étrangères (asymétrie) ; caractère confiscatoire potentiel (20 % sans plafond) ; égalité devant les charges publiques ; QPC annoncées (✧) | 4 fragilités | Actu-Juridique (lu) + chercheur (✧) | ✦ + ✧ |
| FCT-010 | **Objectif et modèle** : mesure anti-abus / discipline fiscale (inciter à la réallocation vers l'économie réelle) ; modèle = Personal Holding Company Tax américaine (rendement historique : **0,0001 % du PIB** pour 20 %) ; échec de la taxe Zucman (2 % patrimoine > 100 M€) et de l'imposition des non-distribués (bloquée par la directive « mère-fille ») | 0,0001 % PIB | Actu-Juridique (lu) + La Tribune (lu) | ✦ |

### CONTRADICTION_LEDGER

| ID | Contradiction | Résolution | Statut |
|----|---------------|------------|--------|
| CONTR-001 | « Une taxe de 20 % sur les holdings » (récit) vs « taxe démantelée » (La Tribune) | Les deux sont vrais : taux 20 % dans le texte, mais assiette réduite de tous revenus passifs (2 %) aux actifs somptuaires (20 %) — rendement 1,5 Md€ → 100 M€ | DOCUMENTÉE (Ω=8) |
| CONTR-002 | « Rendement initial 1-1,5 Md€ » (Actu-Juridique) vs « 900 M€ » (La Tribune) | La Tribune cite le rendement « initial visé » au moment de l'amendement (31/10/2025) ; Actu-Juridique cite le rendement de la version déposée (1-1,5 Md€) — deux points de la trajectoire, pas d'écart | RÉSOLUE (trajectoire) |
| CONTR-003 | « Le CC a validé la taxe » vs « ni conforme ni non conforme » | Le CC a refusé l'examen au fond (§60) — ni l'un ni l'autre ; la lecture « validée » est fausse | RÉSOLUE (CAU-004) |
| CONTR-004 | « Œuvres d'art et antiquités taxées » (rumeur) vs « exclues » | La version initiale les incluait ; la version finale les EXCLUT (comme la trésorerie) — Actu-Juridique tranche | DOCUMENTÉE |

### EDI

```
geo:0.60 lang:0.85 strat:0.80 owner:0.70 persp:0.80 temp:0.85
EDI_raw = .25×.60 + .20×.85 + .20×.80 + .15×.70 + .15×.80 + .05×.85 = 0.755
Pénalité : MISSING_COUNTER (-.10) : perspective des holdings visées (défense du dispositif, réalité de la gestion) absente ; voie nominative nulle.
EDI = 0.655 (BROAD, sous la cible APEX 0.80, écart déclaré)
COV = 0.85 | IND = 0.70 | CC = 4/4
EDI* = .5×.655 + .3×.85 + .2×.70 = 0.72
Perspectives : ⟐ 3 | ⟐̅ 1 | 🎓 2 (Lazard, cabinets) | 🌍 0 | 🔥 0
DIAGNOSTIC_NOT_TRUTH
```

### TRACE_MATRIX (extrait)

| FCT | QRY | SRC | URL (référence) | Statut |
|-----|-----|-----|-----------------|--------|
| FCT-001 à 005, 009, 010 | QRY-001 | SRC-01 | actu-juridique.fr/fiscal/tout-comprendre-sur-la-nouvelle-taxe-sur-les-holdings-patrimoniales/ (lu intégralement 10/08/2026) | ✦ |
| FCT-004, 006, 007, 010 | QRY-002 | SRC-02 | latribune.fr/article/economie/finances-publiques/52040582770923/... (lu intégralement 10/08/2026) | ✦ |
| FCT-001, 008 | QRY-003 | SRC-03 | conseil-constitutionnel.fr/decision/2026/2026901DC.htm (§2, §57-60 lus) | ✦ |
| FCT-006 (100 M€), FCT-009 (cabinets) | QRY-004 | SRC-04 | chercheur 10/08/2026 (corroboration) | ✧ |

## 12. CARTE DIALECTIQUE (scénarios + responsabilité)

| Scénario | Hypothèse | Support | Contre | Lecture |
|----------|-----------|--------|--------|---------|
| S1 « Signal anti-abus » | La taxe dissuade la détention de luxe en holding | Liste 20 % ; modèle US ; objectif affiché | Rendement 100 M€ ; 0,0001 % PIB US | Retenue (partiel) |
| S2 « Taxe démantelée » | Le recentrage protège les revenus passifs | Trajectoire 1,5 Md€ → 100 M€ ; seuil 50 % ; exclusions | Texte 20 % existe | Retenue (verdict) |
| S3 « QPC à venir » | La taxe tombera ou sera réformée | Fragilités FR/étranger, confiscatoire ; non-examen CC | Aucune QPC documentée à ce jour | Retenue (en attente) |

**IMPACT_MAP** :

| Acteur | Gain | Perte |
|--------|------|-------|
| État | ~100 M€ (si collectés) + signal | 1,4 Md€ de recettes abandonnées (vs projet initial) |
| Holdings patrimoniales (revenus passifs) | Épargnées par le recentrage (seuil 50 %) | — |
| Détenteurs de biens de luxe en holding | — | 20 % sur yachts/jets/vins/bijoux/logements réservés (sauf sortie du bilan avant 31/12/2026) |
| Cabinets | Honoraires QPC | — |
| Contribuables | Égalité partielle | Rendement symbolique |

**RESPONSIBILITY_MAP** : aucun auteur d'intention n'est établi (BENEFIT != INTENT). Rôles : gouvernement (initiative 1,5 Md€, recentrage défendu), Juvin/LR (recentrage 20 %/50 %), gauche (Zucman refusée), CC (non-examen), cabinets (QPC). Responsabilité systémique : la navette a produit un impôt au rendement symbolique ciblant le luxe ostentatoire plutôt que la capitalisation patrimoniale — le « démantèlement » est le fait, la justification (précision) est contestable au regard de l'assiette abandonnée (revenus passifs).

## 13. PÉRIMÈTRE & LIMITES

**Inclusions** : périmètre exact (sociétés, seuils, actifs, double régime) ; trajectoire des recettes ; parcours parlementaire (amendement Juvin) ; sort CC ; familles visées (structurel) ; modèle US. Période 10/2025-08/2026.

**Exclusions explicites** : article 235 ter C non lu sur Légifrance (bloqué — contenu établi via Actu-Juridique lu + CC lu) ; décrets et BOFiP d'application (non publiés à ce jour) ; débats détaillés en navette ; QPC déposées (état 10/08/2026 non documenté) ; le rendement réel 2027.

**GAP déclarés** :
- GAP-001 (ACCESS) : liste nominative des structures/familles visées — aucun nom publié (secret fiscal) ; seule porte : presse spécialisée patrimoniale (à explorer).
- GAP-002 (ACCESS) : article 235 ter C sur Légifrance (bloqué à la session) — contenu établi par Actu-Juridique (✦) + CC (✦).
- GAP-003 (CORPUS) : perspective des holdings visées absente (MISSING_COUNTER, EDI) ; réactions détaillées des cabinets (✧).
- GAP-004 (VERIFY) : QPC déposées et état des décrets d'application — à suivre (fait générateur 31/12/2026).

## 14. ÉTAT DES CONNAISSANCES

- **CONNU (✦)** : art. 7 → 235 ter C ; taux 20 % ; périmètre complet (50 %, 5 M€, > 50 % passifs, liste 1°-7°, exclusions, 31/12/2026, double régime) ; trajectoire 1,5 Md€ → 100 M€ ; amendement Juvin (31/10/2025) ; décision CC 901 (non-examen §60) ; modèle US.
- **PROBABLE (✧)** : rendement ~100 M€ (Lazard, corroboration presse) ; réactions cabinets (Bornhauser, Deloitte) ; QPC annoncées.
- **HYPOTHÈSE (⁂)** : l'effet dissuasif dépasse le rendement collecté (les holdings sortiront les biens avant le 31/12/2026).
- **CONTESTÉ (⊗)** : « taxe sur les holdings » (texte) vs « taxe démantelée » (réalité budgétaire).
- **INCONNU (⁅)** : nombre final de redevables ; rendement réel 2027 ; QPC ; décrets/BOFiP.
- **RÉFUTÉ (❧)** : « le CC a validé la taxe » (non-examen) ; « les œuvres d'art sont taxées » (exclues) ; « le rendement sera significatif » (100 M€, incertain).

## 15. SUSPICION / VÉRIFICATION

**AUDIT DU LEAD** : input UPDATE (FCT-010 du 23-40 : « taxe de 20 % sur certains actifs patrimoniaux (holdings patrimoniales) »). Le verdict d'objet est distinct du verdict de lead : « périmètre, familles, recettes » reçoit une réponse complète sur le périmètre (textes lus), un constat d'absence sur les familles (nominatif), et une trajectoire documentée sur les recettes (1,5 Md€ → 100 M€).

**Vérifications contradictoires exécutées** : Actu-Juridique lu intégralement (24/03/2026, Lazard — source autoritaire) ; La Tribune lue intégralement (31/10/2025 — amendement Juvin, trajectoire) ; décision CC 2026-901 DC lue (§2, §57-60 — non-examen confirmé à la source primaire, y compris le libellé exact « il n'y a pas lieu d'examiner spécialement ») ; le grep initial a produit des faux positifs (« article 77 », « article 8 de la Déclaration », « article 800-1 », « art. 72-2 » — dispositions de la LF 2026 elle-même) avant que la décision ne soit identifiée correctement par son numéro (2026-901 DC du 19/02/2026 — vérifié ligne 1 du fichier : « de la loi de finances pour 2026 »). Légifrance bloqué (route article échouée, 521 octets) — déclaré.

**Verdict final : UNE TAXE « DÉMANTELÉE » — de 1-1,5 Md€ (2 % sur les revenus passifs) à ~100 M€ (20 % sur une liste fermée d'actifs de luxe), laissée ni conforme ni non conforme par un Conseil constitutionnel qui a refusé l'examen au fond.** Le périmètre est intégralement documenté (CGI 235 ter C, seuil 50 %/5 M€/> 50 % passifs, liste 1°-7°, exclusions, 31/12/2026, double régime FR/étranger) ; les familles visées restent anonymes (aucune source nominative) ; les recettes ont chuté de 90 à 93 % en navette. **Le résultat le plus actionnable : le « démantèlement » par l'amendement Juvin (31/10/2025) est le fait central — le FCT-010 du 23-40 est confirmé mais précisé (taxe de 20 % sur actifs somptuaires, pas sur les revenus passifs), et la porte suivante est le suivi des QPC et du premier fait générateur (31/12/2026).**

---

# ANNEXE A. SOURCES

| SRC-ID | Source | Locator / date | Rôle | URL |
|--------|--------|----------------|------|-----|
| SRC-01 | Actu-Juridique, « Tout comprendre sur la nouvelle taxe sur les holdings patrimoniales » (entretien Karine Lecocq, Lazard Frères Gestion — lu intégralement) | 24/03/2026 | ◈ | https://www.actu-juridique.fr/fiscal/tout-comprendre-sur-la-nouvelle-taxe-sur-les-holdings-patrimoniales/ |
| SRC-02 | La Tribune, « Budget 2026 : la taxe holdings démantelée, seuls les biens de luxe taxés à 20 % » (lu intégralement) | 31/10/2025 | ◈ | https://www.latribune.fr/article/economie/finances-publiques/52040582770923/budget-2026-la-taxe-holdings-demantelee-seuls-les-biens-de-luxe-taxes-a-20 |
| SRC-03 | Conseil constitutionnel, décision n° 2026-901 DC du 19/02/2026 (LF 2026) — §2, §57-60 lus | 19/02/2026 | ◈ | https://www.conseil-constitutionnel.fr/decision/2026/2026901DC.htm |
| SRC-04 | Chercheur web (corroboration : 100 M€, cabinets Bornhauser/Deloitte, Les Echos, Le Parisien) | 10/08/2026 | ◉ | — |
| SRC-05 | Légifrance, CGI art. 235 ter C | inaccessible à la session | ⚠ | https://www.legifrance.gouv.fr/codes/article_lc/... (bloqué, 521 octets) |

# ANNEXE B. REQUEST_LOG

```
ENGINE:2.8 | MANIFEST:FINAL | RUN_ID:20260810-0407-taxe-holdings-patrimoniales | PARENT_RUN_ID:20260809-2340 | AS_OF:2026-08-10 | INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:NONE
CHECKPOINT_SEQ:0 | LAST_COMPLETED:18b | NEXT_ACTION:NONE | RESUME_COUNT:0
Investigation:taxe-holdings-20pct | complexity:12→COMPLEX | route overrides:NONE | scope:10/2025-08/2026, France
modules:KERNEL|SYMBOLS|PATTERNS|THREATS|GATES|REQUEST_LOG|EPISTEMIC|TEMPLATE|INVESTIGATION
degraded:NONE | query target/actual: 4/4 (1 chercheur ayant répondu + 3 passes basher/lectures source primaire)
COUNT: ◈3 ◉1 | unique evidence objects:10 | upstream families:3
LEADS:terminal 1/1 | AXES:terminal 7/7 | N/A:none
FAILURES:2 (Légifrance 235 ter C bloqué ; La Tribune URL devinée 404 → résolue via URL chercheur) | FALLBACKS:2 (jina ; décision CC lue via URL directe)
unresolved gaps:GAP-001..GAP-004 (nominatif, Légifrance, corpus, QPC/décrets)
```

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL/INPUT_REF |
|---:|---|---|---|---|---|
| 1 | SYS | @MNEMO_Q « taxe holdings patrimoniales 20 % » + lecture parent 23-40 | FCT-010 hérité (taxe 20 % actifs patrimoniaux, SRC-05 Actu-Juridique) | 23-40 | investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_dutreil-110-donataires/ |
| 2 | ◈ | QRY-001 (AXS-001 à 005) : Actu-Juridique taxe holdings | FOUND : art. 7 → 235 ter C ; 20 % ; périmètre complet ; trajectoire 1,5 Md€ → 100 M€ ; double régime ; CC non-examen | SRC-01 | actu-juridique.fr (lu intégralement) |
| 3 | ◈ | QRY-002 (AXS-004 à 007) : La Tribune démantèlement | FOUND : amendement Juvin 31/10/2025 (20 %, seuil 33,3→50 %) ; 10 000 structures ; 900 M€ initial ; exclusions ; cash boxes ; taxe Zucman échouée ; modèle US | SRC-02 | latribune.fr (lu intégralement) |
| 4 | ◈ | QRY-003 (AXS-007) : décision CC | FOUND : 2026-901 DC du 19/02/2026 — articles 7/8/11 déférés par le PM sans grief ; non-examen au fond (§60) | SRC-03 | conseil-constitutionnel.fr (lu) |
| 5 | ◉ | QRY-004 : corroboration recettes 100 M€ + réactions cabinets | PARTIEL (✧) : 100 M€ (Lazard), Bornhauser/Deloitte, Les Echos, Le Parisien | SRC-04 | chercheur |
| 6 | SYS | Vérification : Actu-Juridique et La Tribune lues intégralement ; décision CC 901 lue (§2, §§57-60) ; grep initial ambigu (faux positifs « article 77/800-1/72-2 ») — décision identifiée correctement par son numéro 2026-901 DC ; CONTR-001 à 004 résolus | résolus | SRC-01/02/03 | — |
| 7 | SYS | @MNEMO_S + FACT_WRITEBACK | PENDING_AT_SERIALIZATION | — | — |
| 8 | SYS | STATE:FINAL write | PENDING_AT_SERIALIZATION (ce fichier) | — | investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_taxe-holdings-patrimoniales/2026-08-10_04-07_taxe-holdings-20pct_INVESTIGATION.md |

# ANNEXE C. GATES (G0-G10)

| Gate | Vérification | Résultat |
|------|--------------|----------|
| G0 | Modules chargés ; manifest FINAL ; 15 symboles scorés, aucun ✗ | ✅ |
| G1 | LEAD vs OBJECT distincts ; 7 axes terminaux ; périmètre explicite | ✅ |
| G2 | 6 CLM avec support/counter/gap | ✅ |
| G3 | FACT_REGISTRY 10 faits, statuts canoniques | ✅ |
| G4 | Chaque ✦ → SRC-ID + URL ; ✧ pour corroboration restante (100 M€, cabinets) | ✅ |
| G5 | CAU-001 à 005 typés, arrêt à l'évidence, CAU-004/005 rejetées | ✅ |
| G6 | CONTROL_MAP + RESPONSIBILITY_MAP ; rôles ≠ responsabilités | ✅ |
| G7 | CONTR-001 à 004 documentés et résolus | ✅ |
| G8 | TRACE_MATRIX ; QRY-001 à 004 tracés ; IDs résolus | ✅ |
| G9 | Manifest FINAL, NEXT_ACTION NONE, aucun PENDING requis | ✅ |
| G10 | Un seul chemin ; une seule write FINAL ; PENDING_AT_SERIALIZATION honnête | ✅ |

**GAP_SEVERITY** : edi_gap = (0.80-0.655)/0.80 = 0.181 ; query_gap = N/A ; coverage_gap = 0. GAP_SEVERITY = 0.181 × 1.00 = 0.18 < 0.20 → procéder avec divulgation (GAP-001 à GAP-004 déclarés).

---

*TL;DR : SUJET : la taxe de 20 % sur les holdings patrimoniales de la LF 2026. OBJET : UNE TAXE « DÉMANTELÉE » — la loi n° 2026-103 du 19/02/2026 (art. 7) crée le CGI 235 ter C : taxe de 20 % sur les actifs non affectés à l'activité des sociétés holdings soumises à l'IS, détenues ≥ 50 % par une personne physique (masse familiale) ou contrôlées en fait, seuil 5 M€, revenus passifs > 50 % ; liste fermée 1°-7° (chasse/pêche, véhicules, yachts/avions, chevaux, vins, bijoux/or, logements réservés) ; trésorerie et œuvres d'art EXCLUES ; fait générateur exercice clos ≥ 31/12/2026 ; double régime FR/étranger (redevable PF France au prorata, réduction 75 % des revenus). RECETTES : trajectoire 1-1,5 Md€ (2 % revenus passifs, 10 000 structures) → 900 M€ (cible) → ~100 M€ (20 % actifs somptuaires, amendement Juvin 31/10/2025, seuil 33,3→50 %) — -90 à -93 %. FAMILLES : aucune source nominative (cash boxes des très fortunés, anonymes). SORT CC : décision 2026-901 DC (19/02/2026) — articles 7/8/11 NON EXAMINÉS au fond (§60, « il n'y a pas lieu d'examiner d'office ») ; fragilités constitutionnelles (FR/étranger, confiscatoire, égalité) → QPC à venir ; modèle US (PHC : 0,0001 % du PIB). VERDICT : l'outil anti-abus subsiste comme signal (100 M€), le cœur du montage (revenus passifs) est épargné ; le FCT-010 du 23-40 est confirmé et précisé. SOURCE : UPDATE du 23-40 (FCT-010). MANIPULATION : Ω=8, ↕=8, Κ=8, κ=8, €=8. LIMITE : Légifrance bloqué, voie nominative nulle, QPC/décrets non documentés.*
