# INVESTIGATION : « Le volet pénal de l'OPA Alstom/GE — l'information judiciaire sur le rôle de Macron » (2019-2026, IJ en cours)

## RUN_MANIFEST (FINAL)

```
ENGINE_VERSION : 2.8
STATE          : FINAL
RUN_ID         : 20260814-1400-alstom-penal-ij-macron
PARENT_RUN_ID  : NONE (INPUT_KIND=TOPIC) ; corpus frère : 20260814-1300-arabelle-edf-ge-steam-power, 20260812-1800-iceberg-max-alstom-areva, 20260812-1700-alstom-areva-cessions-macron
AS_OF          : 2026-08-13
INPUT_KIND     : TOPIC (thème : volet pénal français de l'OPA Alstom/GE de 2014 — plainte Anticor 2019, signalement Marleix 2019, disjonction 09/12/2022, non-lieu partiel 10-11/2024, information judiciaire parallèle en cours sur le rôle d'Emmanuel Macron, constitution de partie civile Anticor 20/02/2026, 0 mise en examen)
MISSION_MODE   : INVESTIGATION
INPUT_REF      : NONE (topique utilisateur, re-pipeline T5 cessions, vague 5 — bouclage du volet pénal)
SUBJECT_SLUG   : alstom-penal-ij-macron
INVESTIGATION_PATH : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-14_alstom-penal-ij-macron/2026-08-14_14-00_alstom-penal-ij-macron_INVESTIGATION.md
SCOPE          : volet pénal français de l'affaire Alstom/GE : plainte Anticor 07/2019, signalement article 40 (Marleix) 01/2019, constitution de partie civile 12/2020, enquête préliminaire PNF, ordonnance de disjonction 09/12/2022, qualifications pénales (corruption, abus d'autorité, trafic d'influence, prise illégale d'intérêts), non-lieu partiel 25/10/2024 rendu 22/11/2024 + appel Anticor, information judiciaire parallèle sur le rôle de Macron, constitution de partie civile 20/02/2026, statut des personnes (Macron, Kron), 0 mise en examen ; période 2019-2026 ; géographie : France
COMPLEXITY     : CX_SCORE=13 → $CX=STANDARD (political 5, technical 2, temporal 4, geo 1, narratives 3, data 2)
CHECKPOINT_SEQ : 0 (run mono-session)
LAST_COMPLETED : 13
NEXT_ACTION    : NONE
RESUME_COUNT   : 0
ROUTE_OVERRIDES: []
LOADED_MODULES : KERNEL v2.8 | SYMBOLS | PATTERNS | THREATS | GATES | REQUEST_LOG | EPISTEMIC | TEMPLATE | INVESTIGATION (tous chargés)
DEGRADED_FLAGS : []
HASH_CAPABILITY: HASH_UNAVAILABLE
```

## 1. RÉSUMÉ EXÉCUTIF

**Réponse à l'OBJECT_QUESTION** (« où en est la justice française sur la vente d'Alstom Energy à GE en 2014, et quel rôle est-il reproché à Emmanuel Macron ? ») :

Le volet pénal français de l'affaire Alstom s'est structuré en deux temps. **Premier temps (2019-2024, corruption internationale)** : le signalement du député Olivier Marleix au parquet de Paris (**01/2019**, article 40 du code de procédure pénale, à la suite du rapport n° 897 d'avril 2018) et la plainte d'Anticor (**07/2019**, corruption d'agent public étranger et recel, complétée par une constitution de partie civile en **12/2020**) déclenchent une enquête préliminaire du PNF. Le juge d'instruction rend le **25/10/2024** une ordonnance de **non-lieu partiel** (rendue publique par Le Monde le **22/11/2024**), conforme aux réquisitions du parquet, sur le volet corruption internationale visant notamment Patrick Kron (PDG d'Alstom 2003-2016) ; **Anticor interjette appel** début 11/2024. **Second temps (2022-2026, conditions de la cession)** : par une ordonnance de **disjonction du 09/12/2022**, une **information judiciaire distincte** est ouverte sur **les conditions de la cession de la branche énergie d'Alstom à GE en 2014** et le rôle des autorités françaises de l'époque, **en particulier Emmanuel Macron** (SG adjoint de l'Élysée en 2012, supervisant l'étude AT Kearney sur Alstom, 299 000 € ; ministre de l'Économie 2014-2016, signataire de l'autorisation d'investissement de GE en 11/2014). Les qualifications visées : corruption, **abus d'autorité par une personne dépositaire de l'autorité publique**, trafic d'influence, prise illégale d'intérêts. Le **20/02/2026**, **Anticor se constitue partie civile** dans cette information judiciaire (relayé par Le Monde en 03/2026) : accès au dossier, demandes d'actes, recours. À la date, **aucune mise en examen n'est documentée** : Emmanuel Macron bénéficie de l'immunité présidentielle pour ses actes de fonction et n'est pas poursuivi ; le non-lieu partiel n'a pas renvoyé Patrick Kron en correctionnelle sur le volet corruption internationale.

**Verdict sur le LEAD_QUESTION** : **CONTEXTE DOCUMENTÉ, LECTURE DU « SCHÉMA CORRUPTIF » ALLÉGUÉ MAIS NON ÉTABLIE JUDICIAIREMENT**. Le fait est documenté : la justice enquête depuis 2019 (signalement parlementaire + plainte associatif), une information judiciaire dédiée aux conditions de la cession et au rôle de Macron est ouverte depuis le 09/12/2022, le non-lieu partiel de 10-11/2024 porte sur le volet corruption internationale, Anticor a relancé le dossier par sa constitution de partie civile du 20/02/2026. Mais **0 mise en examen** et **aucun élément matériel de « pacte de corruption » publié** : le volet pénal reste ouvert et non tranché — il documente le trouble, pas la preuve. Le rapport Phase 2 doit continuer de distinguer le pénal (en cours, non-lieu partiel, 0 mise en examen) de l'intégrité (gravement contesté : flux circulaire de conseils, sélectivité, perte de souveraineté documentée par le rapport n° 897).

**Acteurs** : Emmanuel Macron, Patrick Kron, Olivier Marleix, Anticor, PNF, parquet de Paris, juge d'instruction (pôle financier de Paris), Frédéric Pierucci, Rothschild, Lazard, cabinets de conseil (AT Kearney), commission d'enquête de l'Assemblée nationale.

## 2. MANIPULATION_REPORT (15 symboles scorés sur corpus)

| # | Symbole | Score | Justification (corpus) |
|---|---------|-------|------------------------|
| 1 | **Ξ** omission | **9/10** | Le contenu des auditions et actes d'enquête de l'IJ parallèle n'est pas public ; le périmètre exact des qualifications retenues par le juge d'instruction n'est pas publié ; aucun élément matériel du « schéma corruptif » allégué n'a été rendu public. |
| 2 | **€** money | **7/10** | 772 M$ (amende DOJ 2014, contexte) ; 299 000 € (étude AT Kearney supervisée par Macron, 2012) ; 12,4 Md€ (cession 2014, contexte) ; honoraires de conseil (Rothschild 12 M€, dossiers frères). |
| 3 | **Λ** framing | **8/10** | « Pacte de corruption » (Anticor/presse d'investigation) vs « non-lieu » (décision) vs « affaire classée sans suite » (lecture des défenseurs) ; le même dossier est décrit comme « relancé » (03/2026) après avoir été « clos partiellement » (11/2024). |
| 4 | **Ω** inversion | **8/10** | Le non-lieu partiel (présenté comme une victoire des mis en cause) coexiste avec une IJ parallèle en cours (présentée comme un affaiblissement) ; la constitution de partie civile du 20/02/2026 « relance » ce que le non-lieu semblait clore. |
| 5 | **Ψ** sidération | **7/10** | Le rôle d'un président de la République dans une cession industrielle scrutée par la justice ; l'ancien banquier Rothschild validant un deal où Rothschild encaisse (contexte) ; pic émotionnel réel. |
| 6 | **↕** verticalité | **9/10** | Les décisions sont au sommet (Élysée, Bercy, PDG) ; les salariés et la souveraineté industrielle subissent ; le contrôle judiciaire lui-même est au sommet (PNF, pôle financier). |
| 7 | **Φ** spectacle | **7/10** | Le non-lieu (11/2024) et la relance par Anticor (03/2026) sont médiatisés au niveau national ; le rôle de Macron dans l'OPA est un sujet récurrent de la presse d'investigation. |
| 8 | **Σ** sémiotique | **7/10** | « Affaire Alstom » (dossier médiatique consolidé), « pacte de corruption », « renvois d'ascenseur », « immunité présidentielle » — un lexique judiciaire/politique chargé. |
| 9 | **Κ** cynisme | **7/10** | Le non-lieu partiel conforme aux réquisitions du PNF, suivi d'un appel et d'une partie civile, documente la tension entre le parquet (conforme) et la partie civile (relance) ; la lenteur (2019-2026) joue pour les mis en cause. |
| 10 | **ρ** résistance | **7/10** | Anticor (plainte 2019, PC 12/2020, appel 11/2024, PC 20/02/2026) ; Olivier Marleix (signalement 01/2019) ; commission d'enquête (rapport n° 897) ; presse d'investigation (Le Monde, Mediapart, Marianne). |
| 11 | **κ** influence subtile | **7/10** | La question des contreparties (banques d'affaires Rothschild/Lazard, cabinets de conseil rémunérés sur l'opération, liens avec la campagne 2016-2017) est au cœur des allégations non établies ; le poids du pouvoir exécutif sur le calendrier est questionné. |
| 12 | **⫸** convergence | **8/10** | Convergence sans contamination : Le Monde (22/11/2024, 03/2026), Le Parisien (07/2019), rapport n° 897 (04/2018), signalement article 40 (01/2019), ordonnances judiciaires (09/12/2022, 25/10/2024), communiqués Anticor documentent la même trajectoire procédurale. |
| 13 | **⚔** guerre cognitive | **5/10** | Pas d'opération coordonnée documentée ; en revanche la qualification du dossier (« pacte de corruption » vs « non-lieu ») fait l'objet d'une bataille narrative entre partie civile et défenses. |
| 14 | **🌐** réseau | **7/10** | Nœuds : Macron, Kron, Marleix, Anticor, PNF, juge d'instruction, Rothschild, Lazard, AT Kearney, Pierucci, commission d'enquête, presse. |
| 15 | **⏰** temporalité | **9/10** | 01/2019 (signalement) → 04/2018 (rapport n° 897) → 07/2019 (plainte Anticor) → 12/2020 (PC) → 09/12/2022 (disjonction) → 25/10/2024 (non-lieu) → 22/11/2024 (publication) → 11/2024 (appel) → 20/02/2026 (PC dans l'IJ) → 03/2026 (relance médiatisée) : trajectoire longue, ouverte, vérifiable. |

## 3. CHRONOLOGIE

- **04/2018** : rapport n° 897 de la commission d'enquête de l'Assemblée nationale (présidée par Olivier Marleix) sur les décisions de l'État en matière de politique industrielle (Alstom, Alcatel, STX) : « faillite des élites », conditions opaques de la cession.
- **01/2019** : Olivier Marleix transmet un signalement au parquet de Paris (article 40 du code de procédure pénale) sur les conditions de la vente de la branche énergie d'Alstom à GE.
- **07/2019** : plainte d'Anticor au PNF (corruption d'agent public étranger, recel) fondée sur la condamnation DOJ (772 M$, 2014) et les travaux de la commission ; enquête préliminaire.
- **12/2020** : constitution de partie civile d'Anticor (le dossier passe en information judiciaire).
- **09/12/2022** : ordonnance de disjonction — ouverture d'une information judiciaire distincte sur les conditions de la cession de la branche énergie à GE (2014) et le rôle des autorités françaises, en particulier Emmanuel Macron.
- **2023-2024** : actes d'instruction sur le volet conditions de cession (auditions, commissions rogatoires, expertises) ; contenu non public.
- **25/10/2024** : ordonnance de non-lieu partiel sur le volet corruption internationale visant notamment Patrick Kron, conforme aux réquisitions du PNF.
- **22/11/2024** : Le Monde révèle le non-lieu partiel et l'existence de l'information judiciaire parallèle liée au rôle de Macron.
- **11/2024** : Anticor interjette appel de l'ordonnance de non-lieu partiel.
- **20/02/2026** : Anticor se constitue partie civile dans l'information judiciaire parallèle (relayé par Le Monde en 03/2026) : accès au dossier, demandes d'actes, recours.
- **2026** : instruction en cours au pôle financier de Paris ; 0 mise en examen documentée à la date.

## 4. FACT_REGISTRY (faits sourcés)

| ID | Fait | Chiffre | Source | Statut |
|----|------|---------|--------|--------|
| FCT-001 | 04/2018 : rapport n° 897 de la commission d'enquête de l'Assemblée nationale (présidée par Marleix) : « faillite des élites », cession Alstom/GE aux conditions opaques | 04/2018 | SRC-01 Assemblée nationale, rapport n° 897 | ✦ |
| FCT-002 | 01/2019 : Olivier Marleix transmet un signalement au parquet de Paris (article 40 CPP) sur les conditions de la vente d'Alstom Energy à GE | 01/2019 | SRC-02 presse (Le Monde, articles 01/2019 et 22/11/2024) ; rapport n° 897 (04/2018) | ✦ |
| FCT-003 | 07/2019 : plainte d'Anticor au PNF (corruption d'agent public étranger, recel) fondée sur la condamnation DOJ (772 M$, 12/2014) et les travaux de la commission ; enquête préliminaire | 07/2019 ; 772 M$ | SRC-03 Le Parisien 22/07/2019 ; Anticor | ✦ |
| FCT-004 | 12/2020 : constitution de partie civile d'Anticor ; le dossier passe en information judiciaire | 12/2020 | SRC-04 Anticor (communiqués) ; presse | ✦ |
| FCT-005 | 09/12/2022 : ordonnance de disjonction — ouverture d'une information judiciaire distincte sur les conditions de la cession de la branche énergie d'Alstom à GE (2014) et le rôle des autorités politiques et économiques françaises, en particulier Emmanuel Macron | 09/12/2022 | SRC-05 ordonnance de disjonction PNF (révélée par Le Monde 22/11/2024) | ✦ |
| FCT-006 | Qualifications pénales visées par l'IJ : corruption, abus d'autorité par une personne dépositaire de l'autorité publique, trafic d'influence, prise illégale d'intérêts | — | SRC-06 Le Monde 22/11/2024 ; presse | ✦ |
| FCT-007 | 25/10/2024 : ordonnance de non-lieu partiel sur le volet corruption internationale visant notamment Patrick Kron (PDG d'Alstom 2003-2016), conforme aux réquisitions du PNF ; pas de renvoi en correctionnelle | 25/10/2024 | SRC-07 ordonnance (signée 25/10/2024) ; Le Monde 22/11/2024 | ✦ |
| FCT-008 | 22/11/2024 : Le Monde révèle le non-lieu partiel et l'existence de l'information judiciaire parallèle en lien avec le rôle d'Emmanuel Macron | 22/11/2024 | SRC-08 Le Monde 22/11/2024 | ✦ |
| FCT-009 | 11/2024 : Anticor interjette appel de l'ordonnance de non-lieu partiel | 11/2024 | SRC-09 Anticor ; presse | ✦ |
| FCT-010 | 20/02/2026 : Anticor se constitue partie civile dans l'information judiciaire parallèle (accès au dossier, demandes d'actes, recours) ; relayé par Le Monde en 03/2026 | 20/02/2026 | SRC-10 Le Monde 03/2026 ; Anticor (acte de PC 20/02/2026) | ✦ |
| FCT-011 | 0 mise en examen documentée à la date : aucun dirigeant (dont Patrick Kron) ni aucune personnalité politique (dont Macron) n'est mis en examen | 0 | SRC-11 synthèse presse 2019-2026 (constat d'absence) | ✦ |
| FCT-012 | Rôle reproché à Macron (phase 1) : SG adjoint de l'Élysée en 2012, il supervisait l'étude du cabinet AT Kearney sur Alstom (299 000 €) | 2012 ; 299 000 € | SRC-12 LCP/commission d'enquête (AT Kearney) | ✦ |
| FCT-013 | Rôle reproché à Macron (phase 2) : ministre de l'Économie 2014-2016, il a autorisé l'investissement de GE (11/2014) dans le cadre du décret n° 2014-479 du 14/05/2014 | 11/2014 | SRC-13 décret 2014-479 (Légifrance) ; presse | ✦ |
| FCT-014 | Le cœur des allégations : un possible « pacte de corruption » ou « renvois d'ascenseur » — banques d'affaires (Rothschild, Lazard) et cabinets de conseil rémunérés sur l'opération auraient soutenu la campagne présidentielle 2016-2017 de Macron | — | SRC-14 Le Monde 03/2026 ; presse d'investigation | ⚠ (allégation rapportée, aucun élément matériel publié) |
| FCT-015 | Emmanuel Macron bénéficie de l'immunité présidentielle pour ses actes de fonction ; aucune poursuite contre lui à la date | — | SRC-15 Constitution (art. 67) ; synthèse presse | ✦ |
| FCT-016 | Le non-lieu partiel constate que des filiales d'Alstom et des niveaux opérationnels avaient déjà été sanctionnés à l'étranger (DOJ, 772 M$, 12/2014) ; le juge estime insuffisantes les charges contre les dirigeants historiques sur ce volet | 772 M$ | SRC-16 ordonnance 25/10/2024 ; presse | ✦ |
| FCT-017 | La thèse de Frédéric Pierucci (« Le Piège américain », 2019 : le DOJ a utilisé le FCPA pour contraindre Alstom à se vendre à GE) n'est pas tranchée judiciairement en France | — | SRC-17 Pierucci « Le Piège américain » (JC Lattès, 2019) ; synthèse | ⚠ (thèse documentée, non tranchée) |
| FCT-018 | Arc documenté : 2019-2026, deux volets (corruption internationale vs conditions de cession), un non-lieu partiel (25/10/2024), une IJ en cours (disjonction 09/12/2022), une partie civile (20/02/2026), 0 mise en examen — le pénal documente le trouble sans le trancher ; l'intégrité reste documentée par le rapport n° 897 (« faillite des élites ») | 0 mise en examen | SRC-18 synthèse FCT-001..017 (constat composé) | ⚠ (calcul composé, inférence étiquetée) |


<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ❧ | - | - | - | 2026-08-14_14-00_alstom-penal-ij-macron | - | -
FCT-002 | FACT | ❧ | - | - | - | 2026-08-14_14-00_alstom-penal-ij-macron | - | -
FCT-003 | FACT | ❧ | - | - | - | 2026-08-14_14-00_alstom-penal-ij-macron | - | -
FCT-004 | FACT | ❧ | - | - | - | 2026-08-14_14-00_alstom-penal-ij-macron | - | -
FCT-005 | FACT | ❧ | - | - | - | 2026-08-14_14-00_alstom-penal-ij-macron | - | -
FCT-006 | FACT | ❧ | - | - | - | 2026-08-14_14-00_alstom-penal-ij-macron | - | -
FCT-007 | FACT | ❧ | - | - | - | 2026-08-14_14-00_alstom-penal-ij-macron | - | -
FCT-008 | FACT | ❧ | - | - | - | 2026-08-14_14-00_alstom-penal-ij-macron | - | -
FCT-009 | FACT | ❧ | - | - | - | 2026-08-14_14-00_alstom-penal-ij-macron | - | -
FCT-010 | FACT | ❧ | - | - | - | 2026-08-14_14-00_alstom-penal-ij-macron | - | -
FCT-011 | FACT | ❧ | - | - | - | 2026-08-14_14-00_alstom-penal-ij-macron | - | -
FCT-012 | FACT | ❧ | - | - | - | 2026-08-14_14-00_alstom-penal-ij-macron | - | -
FCT-013 | FACT | ❧ | - | - | - | 2026-08-14_14-00_alstom-penal-ij-macron | - | -
FCT-014 | FACT | ❧ | - | - | - | 2026-08-14_14-00_alstom-penal-ij-macron | - | -
FCT-015 | FACT | ❧ | - | - | - | 2026-08-14_14-00_alstom-penal-ij-macron | - | -
FCT-016 | FACT | ❧ | - | - | - | 2026-08-14_14-00_alstom-penal-ij-macron | - | -
FCT-017 | FACT | ❧ | - | - | - | 2026-08-14_14-00_alstom-penal-ij-macron | - | -
FCT-018 | FACT | ❧ | - | - | - | 2026-08-14_14-00_alstom-penal-ij-macron | - | -
<!-- /FACT_REGISTRY_V1 -->

## 5. CLAIM_REGISTRY

| ID | Claim | Support | Contre-évidence | Statut |
|----|-------|---------|-----------------|--------|
| CLM-001 | « La justice enquête sur le rôle de Macron dans l'OPA Alstom » | IJ distincte ouverte par disjonction 09/12/2022 (FCT-005) ; qualifications (FCT-006) ; PC Anticor 20/02/2026 (FCT-010) | L'IJ ne vise pas formellement Macron (pas de mise en examen, immunité, FCT-015) ; le rôle exact reste à établir | SOUTENU (fait : IJ dédiée documentée) |
| CLM-002 | « Le non-lieu partiel de 2024 a clos le volet corruption internationale » | Ordonnance 25/10/2024 conforme aux réquisitions du PNF (FCT-007) | Appel d'Anticor interjeté (FCT-009) ; l'IJ parallèle continue (FCT-005) | PARTIELLEMENT SOUTENU (clôture partielle, appel et IJ en cours) |
| CLM-003 | « Anticor a relancé le dossier en 2026 » | Constitution de partie civile 20/02/2026 dans l'IJ (FCT-010), relayée par Le Monde (03/2026) | Une PC ne vaut pas acte d'instruction ; l'issue reste ouverte | SOUTENU (fait : PC documentée) |
| CLM-004 | « Le volet pénal ne tranche pas le volet intégrité » | 0 mise en examen (FCT-011) ; non-lieu partiel (FCT-007) ; rapport n° 897 documentant « faillite des élites » (FCT-001) | Une instruction en cours peut aboutir à des mises en examen ultérieures | SOUTENU (à la date : pénal ouvert, intégrité documentée) |

## 6. CONTRADICTION_LEDGER

| ID | Contradiction | Résolution | Statut |
|----|---------------|------------|--------|
| CONTR-001 | « Affaire classée » (lecture des défenseurs après le non-lieu partiel) vs « affaire relancée » (Anticor, 03/2026) | Le non-lieu partiel ne porte que sur le volet corruption internationale (FCT-007) ; l'IJ parallèle (FCT-005) et l'appel (FCT-009) se poursuivent | DOCUMENTÉE (non tranchée) |
| CONTR-002 | « Pacte de corruption » allégué (Anticor, presse) vs « non-lieu » (décision 10/2024) | Les deux coexistent : l'allégation porte sur les conditions de cession (IJ en cours, FCT-005/006), le non-lieu sur la corruption internationale (FCT-007) ; aucun élément matériel publié | DOCUMENTÉE (non tranchée) |
| CONTR-003 | « Le DOJ a contraint Alstom à se vendre » (Pierucci, 2019) vs « GE a fait une offre librement acceptée » (lecture de la direction) | La thèse de Pierucci est documentée mais non tranchée judiciairement en France (FCT-017) ; l'amende DOJ 772 M$ et les arrestations 2013 sont des faits (FCT-003/016) | DOCUMENTÉE (non tranchée) |

## 7. RÉSEAU D'ACTEURS

**Personnes** : Emmanuel Macron (SG adjoint Élysée 2012, ministre de l'Économie 2014-2016, président ; rôle au centre de l'IJ), Patrick Kron (PDG d'Alstom 2003-2016, visé par le non-lieu partiel), Olivier Marleix (député, président de la commission d'enquête, signalement 01/2019), Frédéric Pierucci (ex-Alstom, auteur du « Piège américain »), juges d'instruction du pôle financier de Paris.
**Institutions** : PNF (parquet national financier), parquet de Paris, pôle financier du tribunal judiciaire de Paris, Assemblée nationale (commission d'enquête, rapport n° 897), Anticor (association, partie civile), DOJ (États-Unis, contexte 772 M$).
**Entreprises** : Alstom, General Electric, Rothschild & Co (conseil), Lazard (conseil), AT Kearney (cabinet, étude 299 000 €), cabinets de conseil.

## 8. MÉCANISMES / CHAÎNES CAUSALES

**M1 — La disjonction comme outil de séparation des volets** : le même dossier est scindé en deux : le volet corruption internationale (jugé, non-lieu partiel 25/10/2024) et le volet conditions de cession / rôle des autorités (disjonction 09/12/2022, IJ en cours). La disjonction protège la durée du volet sensible : le second temps est plus long et plus opaque que le premier. Type : STRUCTUREL. Niveau : L2.
**M2 — La partie civile comme moteur de la relance** : Anticor, seule force de relance documentée, passe par les trois leviers du droit pénal français : signalement/plainte (2019), appel du non-lieu (11/2024), constitution de partie civile dans l'IJ (20/02/2026). Sans la partie civile, le dossier aurait pu s'arrêter au non-lieu partiel. Type : STRUCTUREL. Niveau : L2.
**M3 — L'immunité présidentielle comme plafond de verre procédural** : le rôle central de Macron (2012 SG adjoint, 2014-2016 ministre) est documenté (FCT-012/013), mais l'immunité présidentielle (art. 67 de la Constitution) rend impossible toute mise en examen pour ses actes de fonction pendant son mandat — la responsabilité pénale du principal acteur politique est structurellement inatteignable à la date. Type : STRUCTUREL. Niveau : L1-L2.

## 9. CARTE DIALECTIQUE (scénarios + responsabilité)

| Scénario | Hypothèse | Support | Contre | Lecture |
|----------|-----------|--------|--------|---------|
| S1 « Dossier vide » | Les allégations sont sans fondement ; le non-lieu partiel en atteste | Non-lieu partiel conforme aux réquisitions du PNF (FCT-007) ; 0 mise en examen (FCT-011) | IJ parallèle ouverte (FCT-005) ; appel (FCT-009) ; PC 20/02/2026 (FCT-010) ; rapport n° 897 (FCT-001) | PARTIELLEMENT SOUTENU (non-lieu partiel, mais IJ en cours) |
| S2 « Schéma corruptif à établir » | Les conditions de la cession 2014 cachent des contreparties | IJ dédiée aux conditions de cession (FCT-005) ; qualifications corruption/trafic d'influence/prise illégale d'intérêts (FCT-006) ; allégations de renvois d'ascenseur (FCT-014) | Aucun élément matériel publié (FCT-014 ⚠) ; 0 mise en examen (FCT-011) | PARTIELLEMENT SOUTENU (allégations documentées, preuve non publiée) |
| S3 « Impunité structurelle » | Le système (immunité présidentielle, lenteur, non-lieu partiel) protège les décideurs | Immunité (FCT-015) ; 7 ans d'instruction sans mise en examen (FCT-011, FCT-018) ; non-lieu partiel (FCT-007) | L'IJ est en cours et peut aboutir (FCT-010) ; la relance d'Anticor (FCT-009/010) | RETENU (scénario principal, documenté) |

**RESPONSIBILITY_MAP** : la cession de 2014 relève du gouvernement de l'époque (Macron ministre, autorisation 11/2014) et de la direction d'Alstom (Kron) ; la responsabilité pénale est en cours d'examen (IJ, disjonction 09/12/2022) avec 0 mise en examen à la date ; l'immunité présidentielle couvre Macron pour ses actes de fonction (art. 67). (BENEFIT != INTENT).

## 10. VERDICT 3 AXES

- **PÉNAL** : EN COURS — signalement 01/2019, plainte Anticor 07/2019, disjonction 09/12/2022, non-lieu partiel 25/10/2024 (volet corruption internationale), appel Anticor 11/2024, IJ parallèle en cours sur le rôle de Macron, PC Anticor 20/02/2026 ; **0 mise en examen documentée**.
- **INTÉGRITÉ** : GRAVEMENT CONTESTÉ (non) — le flux circulaire de conseils, la sélectivité (Nokia/Alcatel autorisés, Carrefour bloqué), les conditions opaques documentées par le rapport n° 897 (« faillite des élites », 04/2018) et la durée de l'enquête sans mise en examen documentent un trouble majeur de l'intégrité de la décision publique, distinct de la preuve pénale.
- **LÉGITIMITÉ** : CONTESTÉ — la commission d'enquête, la plainte d'Anticor, la relance de 2026 et la presse d'investigation documentent le déficit de légitimité perçu ; le non-lieu partiel et l'immunité présidentielle renforcent la perception d'impunité (scénario S3).

## 11. PÉRIMÈTRE & LIMITES

**Inclusions** : volet pénal français de l'affaire Alstom/GE (signalement, plainte, information judiciaire, disjonction, non-lieu, appel, partie civile, statut des personnes) ; période 2019-2026 ; géographie : France.

**Exclusions** : le fond de l'opération Alstom/GE (couvert par alstom-areva-cessions-macron et arabelle-edf-ge-steam-power) ; la procédure DOJ américaine (contexte uniquement, FCT-003/016) ; les autres volets de l'affaire hors Alstom.

**GAP déclarés** :
- GAP-001 (ACCESS) : contenu des actes d'instruction de l'IJ parallèle (auditions, expertises, commissions rogatoires) non public ; périmètre exact des qualifications retenues par le juge d'instruction.
- GAP-002 (ACCESS) : élément matériel du « pacte de corruption » allégué (FCT-014) — aucun document publié.
- GAP-003 (CAUSALITY) : lien entre les contreparties alléguées (banques, conseils, campagne 2016-2017) et la décision d'autorisation — non établi, en cours d'examen.

## 12. ÉTAT DES CONNAISSANCES

- **CONNU (✦)** : rapport n° 897 (04/2018) ; signalement Marleix (01/2019) ; plainte Anticor (07/2019) ; PC (12/2020) ; disjonction (09/12/2022) ; qualifications (corruption, abus d'autorité, trafic d'influence, prise illégale d'intérêts) ; non-lieu partiel (25/10/2024) ; publication Le Monde (22/11/2024) ; appel (11/2024) ; PC Anticor dans l'IJ (20/02/2026) ; 0 mise en examen ; rôle de Macron (AT Kearney 2012, autorisation 11/2014) ; immunité présidentielle (art. 67).
- **PROBABLE (✧)** : le périmètre du rôle de Macron dans l'IJ (au centre, d'après Le Monde) ; l'existence d'auditions de membres des cabinets de l'époque.
- **HYPOTHÈSE (⁂)** : l'issue de l'IJ (mises en examen possibles) ; l'issue de l'appel du non-lieu partiel.
- **CONTESTÉ (⊗)** : l'existence d'un « pacte de corruption » (allégué par Anticor/presse, nié par les défenses, non établi) ; la lecture « affaire classée » vs « affaire relancée ».
- **INCONNU (⁅)** : contenu des actes d'instruction ; éléments matériels ; calendrier de fin d'instruction.

## 13. SUSPICION / VÉRIFICATION

- Les dates procédurales (01/2019, 07/2019, 12/2020, 09/12/2022, 25/10/2024, 22/11/2024, 20/02/2026) sont documentées par Le Monde (22/11/2024, 03/2026), Le Parisien (07/2019) et les communiqués Anticor : fiables.
- Le non-lieu partiel et l'IJ parallèle sont des faits rapportés par la presse d'investigation (Le Monde), étiquetés ✦ sur la publication elle-même ; la décision officielle (ordonnance 25/10/2024) n'est pas publiée en intégralité.
- Les allégations de « pacte de corruption » / renvois d'ascenseur (FCT-014) sont des allégations rapportées, aucun élément matériel publié : statut ⚠, à confirmer ou infirmer par l'instruction.
- 0 mise en examen = constat d'absence borné à la date (08/2026) : la situation peut évoluer ; le constat est mis à jour par l'IJ en cours.
- La distinction pénal (en cours, non tranché) vs intégrité (gravement contesté, documenté) est la correction de lecture apportée par cette investigation : le rapport Phase 2 doit la maintenir (fragilité 5 T5).
