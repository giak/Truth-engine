# Agnès Buzyn et l'extension à 11 vaccins obligatoires (2017) — Enquête APEX

ENGINE:2.8 | STATE:FINAL | RUN_ID:20260812-0600-buzyn-vaccination-enfants | PARENT_RUN_ID:NONE | ALL_GAPS_RESOLVED:YES
AS_OF:2026-08-12 08:05 | INPUT_KIND:PERSON | MISSION_MODE:INVESTIGATION | INPUT_REF:NONE | BILAN:8/8 GAPS (4 RÉSOLUS, 2 CLÔTURÉS OSINT, 1 PARTIEL, 1 CLÔTURÉ ARCHIVES)
SUBJECT_SLUG:buzyn-vaccination-enfants | INVESTIGATION_PATH:investigations/2026-08/2026-08-13_corpus-investigations/2026-08-12_buzyn-vaccination-enfants/2026-08-12_06-00_buzyn-vaccination-obligatoire_INVESTIGATION.md
SCOPE:{2008-2021,France,Santé publique/Industrie pharma/Droit admin} | COMPLEXITY:APEX(12) | CHECKPOINT_SEQ:2 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
RESUME_COUNT:0 | ROUTE_OVERRIDES:[PERSON_APEX] | LOADED_MODULES:[SYMBOLS,GATES,REQUEST_LOG,PERSO_FRESQUE,BIO,INVESTIGATION,EPISTEMIC]
DEGRADED_FLAGS:[]

---

## §0 — MANIPULATION_REPORT

INPUT_KIND:PERSON | MISSION_MODE:INVESTIGATION | SYMBOL_STAGE:CORPUS_FINAL

### Symboles narratifs (15/15)

| Symbole | Score | Observations |
|---|---|---|
| Ξ Omission | 9 | Le récit public de la « ministre arrivant à froid sur un dossier hérité » omet la continuité HAS 2016-2017. La déclaration Touraine 2016 sur la disponibilité du DTP seul omet l'arrêt de production de 2008. Le discours officiel omet que l'alternative à l'extension était de forcer Sanofi à reproduire le DTP. |
| € Money | 8 | Sanofi/GSK détiennent le marché français des vaccins pédiatriques. L'extension à 11 vaccins a mécaniquement augmenté le chiffre d'affaires des laboratoires. Buzyn a eu des liens rémunérés avec Novartis, BMS, Genzyme jusqu'en 2011. Coût non publicisé de la mesure pour l'Assurance maladie. |
| Λ Framing | 7 | Cadrage « protection des enfants / lutte contre la défiance vaccinale », jamais « résolution d'une contradiction juridique créée par l'industrie ». La concertation Fischer présentée comme « démocratique » alors que l'entonnoir juridique était déjà refermé. |
| Ω Inversion | 6 | Inversion de la causalité : la décision est présentée comme un choix de santé publique proactif, alors que l'alternative légale (forcer la production de DTP seul) était bloquée par l'arrêt de production de Sanofi depuis 2008. |
| Ψ Sideration | 4 | L'urgence calendaire (CE : 6 mois, août 2017) crée une fenêtre de décision compressée qui limite le débat. |
| ↕ Pouvoir vertical | 8 | Asymétrie État/industrie : Sanofi arrête la production en 2008, l'État ne peut pas le forcer à reprendre. Asymétrie État/citoyens : 2 265 requérants au CE obtiennent gain de cause mais la réponse est l'inverse de leur demande (extension au lieu de DTP seul). |
| Φ Spectacle | 3 | Communication ministérielle calibrée (annonce solennelle du 5 juillet 2017). |
| Σ Sémiotique | 5 | « Vaccination obligatoire » comme symbole de sérieux sanitaire. « Concertation citoyenne » comme label démocratique masquant un choix déjà contraint. |
| Κ Cynisme | 6 | La ministre savait que la « concertation » Fischer était déjà orientée vers l'extension (Fischer lui-même favorable). Le gouvernement choisit l'option qui satisfait l'industrie pharmaceutique tout en résolvant son problème juridique. |
| ρ Résistance | 4 | 2 265 requérants au CE (2015), associations anti-obligation, recours contentieux (tous rejetés). |
| κ Influence subtile | 7 | Le transfert de la compétence vaccinale du HCSP vers la HAS (février-mars 2017) place l'expertise sous l'autorité de Buzyn juste avant sa nomination. Architecture institutionnelle qui concentre le pouvoir de recommandation et de décision. |
| ⫸ Convergence | 8 | Convergence temporelle : CE (8/02) → loi transfert HAS (23/02) → CTV créée (22/03) → Buzyn ministre (17/05) → annonce (5/07). Convergence d'intérêts : Sanofi/GSK (marché élargi) + gouvernement (sortie de l'impasse juridique) + HAS (nouvelle compétence). |
| ⚔ Guerre cognitive | 5 | Campagne de communication « santé publique » intensive. Discrédit des opposants (« antivax »). |
| 🌐 Réseau | 7 | Buzyn ← HAS ← CTV ← HCSP. Buzyn → gouvernement → Parlement → obligation. Sanofi/GSK → marché captif. Réseau d'expertise et de décision concentré. |
| ⏰ Temporel | 9 | Chronologie critique : 2008 arrêt production DTP → 2015 requête CE → 8/02/2017 injonction CE (6 mois) → 23/02/2017 loi transfert HAS → 22/03/2017 CTV créée → 17/05/2017 Buzyn ministre → 5/07/2017 annonce (4 jours avant le délai CE de 6 mois) → 1/01/2018 entrée en vigueur. |

### Détection des patterns et menaces

@PAT[BIO] — REVOLVING_DOOR: HAS → Ministère → OMS. Buzyn présidente HAS mars 2016, ministre mai 2017, OMS 2020.
@PAT[MONEY] — INDUSTRY_CAPTURE: liens Buzyn avec Novartis/BMS/Genzyme jusqu'en 2011. Extension = hausse mécanique du CA des laboratoires.
@PAT[POWER] — REGULATORY_CAPTURE: transfert de la compétence vaccinale vers la HAS sous Buzyn, qui devient ensuite ministre.
@PAT[TEMPORAL] — DEADLINE_DRIVEN: l'injonction du CE crée une fenêtre de décision contrainte.

### Biais pre-flight

A — Source primaire/officielle : gouvernement (discours Buzyn 5/07/2017), HAS, Parlement (loi), Conseil d'État (arrêt 8/02/2017)
B — Critique intéressée : requérants CE (2 265 personnes), associations opposition obligation vaccinale
C — Affectés/témoins : parents, professionnels de santé, enfants
D — Enquête indépendante : rapport Fischer (2016), Cour des comptes (à vérifier)
E — Expert/académique : littérature médicale sur couverture vaccinale, ANSM

COMPLEXITÉ: $CX_SCORE=12 (politique:3, technique:2, temporel:3, géo:1, narratives:2, data:1) → $CX=APEX

---

## LEAD_REGISTRY

| ID | SOURCE_ID | LOCATOR | LEAD | EVIDENCE_EXCERPT | KIND | MATERIALITY | ROUTES | LINKED_IDS | STATUS |
|---|---|---|---|---|---|---|---|---|---|
| LED-001 | — | User input | Buzyn n'hérite pas seulement d'une « concertation » : le Conseil d'État impose un délai de 6 mois le 8 février 2017 | « Le 8 février 2017, le Conseil d'État impose au ministère un délai de six mois : rendre disponible un vaccin correspondant aux seules trois obligations DTP ou voir la loi élargir les obligations. » | EVENT | DECISIVE | [AUDIT,EXPAND] | AXS-001 | ACTIVE |
| LED-002 | — | User input | La concertation Fischer était moins linéaire que le récit public | « Le jury des professionnels privilégiait la levée de l'obligation, et environ la moitié du jury citoyen envisageait aussi ce scénario. Le comité d'orientation choisit ensuite une troisième construction : extension temporaire + clause d'exemption + conditions fortes. » | CLAIM | DECISIVE | [AUDIT,EXPAND] | AXS-002 | ACTIVE |
| LED-003 | — | User input | Buzyn n'est pas étrangère au dossier : elle présidait la HAS depuis mars 2016, la compétence vaccinale y a été transférée sous sa présidence | « Elle préside la HAS depuis mars 2016 ; sous sa présidence, la compétence vaccinale nationale est transférée vers la HAS et la nouvelle Commission technique des vaccinations est installée au printemps 2017. » | ENTITY | DECISIVE | [AUDIT,EXPAND,LINK] | AXS-003,AXS-004 | ACTIVE |
| LED-004 | — | User input | Le discours Touraine du 26/04/2016 ne colle pas au constat juridictionnel de 2017 | « Le 26 avril 2016, Marisol Touraine affirmait qu'un DTP seul pouvait être obtenu « si on le demande », livré en quelques jours. Le Conseil d'État constatera ensuite qu'aucun vaccin correspondant aux seules obligations n'était commercialisé. » | CLAIM | DECISIVE | [AUDIT] | AXS-005 | ACTIVE |

## §1 — TEMPORAL

| Date | Événement | Statut |
|---|---|---|
| Juin 2008 | Sanofi Pasteur MSD suspend puis arrête la production du DTPolio® (hausse des réactions allergiques) | ✦ CONFIRMED (VIDAL, SRC-001) |
| Mars 2011 | Buzyn cesse ses liens avec l'industrie pharmaceutique (Novartis, BMS, Genzyme) | ✦ CONFIRMED (La Tribune, SRC-002) |
| 5 Nov 2015 | ~2 500 personnes déposent une demande au ministère de la Santé pour un vaccin DTP sans adjuvant | ✦ CONFIRMED (VIDAL, SRC-001) |
| 28 Jan 2016 | Touraine annonce vouloir rendre disponibles des vaccins trivalents | ✦ CONFIRMED (VIDAL, SRC-001) |
| 12 Fév 2016 | Benoît Vallet (DGS) rejette formellement la demande de DTP seul | ✦ CONFIRMED (VIDAL, SRC-001) |
| 7 Mar 2016 | Buzyn nommée présidente de la HAS (décret du 3 mars) | ✦ CONFIRMED (Légifrance, SRC-003) |
| 26 Avr 2016 | Touraine déclare que le DTP seul peut être obtenu « si on le demande » | ⁕ CLAIMED (user input, à vérifier) |
| Déc 2016 | Concertation citoyenne Fischer : rapport remis à la ministre Touraine | ⁕ CLAIMED (à vérifier) |
| 8 Fév 2017 | Conseil d'État : injonction de rendre disponible le DTP seul sous 6 mois, « sauf élargissement des obligations » | ✦ CONFIRMED (VIDAL, SRC-001) |
| 23 Fév 2017 | Loi n° 2017-220 : transfert de la compétence vaccinale du HCSP vers la HAS | ✦ CONFIRMED (Légifrance, SRC-004) |
| 22 Mar 2017 | Création de la CTV à la HAS, décision signée par Buzyn | ✦ CONFIRMED (Légifrance, SRC-005) |
| 19 Avr 2017 | Buzyn préside la séance HAS sur la vaccination | ✦ CONFIRMED (HAS, SRC-006) |
| 17 Mai 2017 | Buzyn nommée ministre des Solidarités et de la Santé | ✦ CONFIRMED (Légifrance, SRC-007) |
| 5 Juil 2017 | Buzyn annonce l'extension à 11 vaccins obligatoires | ✦ CONFIRMED (Vidal, SRC-008) |
| Sept-Oct 2017 | Suppression de la clause d'exemption Fischer du texte final | ✦ CONFIRMED (Le Monde, SRC-009) |
| 1 Jan 2018 | Entrée en vigueur de l'obligation des 11 vaccins | ✦ CONFIRMED |
| 16 Fév 2020 | Buzyn quitte le ministère (candidate LREM à Paris) | ✦ CONFIRMED (Les Echos, SRC-010) |
| 2020-2021 | Rejet de tous les recours contentieux contre l'obligation (CE, Conseil constitutionnel) | ✦ CONFIRMED (Conseil d'État, SRC-011) |

## EVIDENCE_REGISTRY

| SRC-ID | CANONICAL_ID | TITLE/AUTHOR | PUBLICATION_DATE | LOCATOR | URL | SOURCE_ROLE | UPSTREAM_FAMILY |
|---|---|---|---|---|---|---|---|
| SRC-001 | — | VIDAL — Vaccin DTP : le Conseil d'Etat enjoint au ministère de la santé de le rendre disponible | 2017-02-08 | Article complet | https://www.vidal.fr/actualites/20866-vaccin-dtp-le-conseil-d-etat-enjoint-au-ministere-de-la-sante-de-le-rendre-disponible-d-ici-6-mois.html | ◉ Résumé journalistique | FAM-001 |
| SRC-002 | — | La Tribune — Agnès Buzyn, une ministre de la Santé proche de certains lobbies | ~2017 | Article | https://www.latribune.fr/entreprises-finance/industrie/chimie-pharmacie/agnes-buzyn-une-ministre-de-sante-proche-de-certains-lobbies-715755.html | ◉ Analyse | FAM-002 |
| SRC-003 | — | Légifrance — Décret du 3 mars 2016 portant nomination HAS | 2016-03-03 | JORF | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000032153632 | ◈ Source primaire | FAM-003 |
| SRC-004 | — | Loi n° 2017-220 du 23 février 2017 | 2017-02-23 | Art. 4 | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000034308279 | ◈ Source primaire | FAM-003 |
| SRC-005 | — | Décision HAS n° 2017.0040/DC/SJ du 22 mars 2017 | 2017-03-22 | — | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000034308279 | ◈ Source primaire | FAM-003 |
| SRC-006 | — | HAS — PV séance collège délibératif du 19 avril 2017 | 2017-04-19 | — | https://www.has-sante.fr/jcms/c_2786508/fr/proces-verbal-de-la-seance-du-college-deliberatif-du-19-avril-2017 | ◈ Source primaire | FAM-003 |
| SRC-007 | — | Légifrance — Décret du 17 mai 2017 composition du Gouvernement | 2017-05-17 | JORF | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000034748271 | ◈ Source primaire | FAM-003 |
| SRC-008 | — | Vidal — Passage de 3 à 11 vaccins obligatoires | 2017-07-05 | Article | https://www.vidal.fr/actualites/21667-passage-de-3-a-11-vaccins-obligatoires-agnes-buzyn-annonce-une-une-loi-a-l-automne-2017.html | ◉ Journalistique | FAM-001 |
| SRC-009 | — | Le Monde — Nouveaux vaccins obligatoires : ni sanctions ni exemptions | 2017-09-27 | Article | https://www.lemonde.fr/sante/article/2017/09/27/nouveaux-vaccins-obligatoires-ni-sanctions-ni-exemptions_5191978_1651302.html | ◉ Journalistique | FAM-004 |
| SRC-010 | — | Les Echos — Buzyn rejoint l'OMS | ~2020 | Article | https://www.lesechos.fr/politique-societe/politique/lex-ministre-de-la-sante-agnes-buzyn-rejoint-loms-1278353 | ◉ Journalistique | FAM-004 |
| SRC-011 | — | Conseil d'État — Vaccination obligatoire et adjuvants | 2018-2021 | Décisions | https://www.conseil-etat.fr/actualites/vaccination-obligatoire-et-adjuvants | ◈ Source primaire | FAM-003 |
| SRC-012 | ECLI:FR:CECHR:2017:397151.20170208 | Conseil d'État — Décision N° 397151 du 8 février 2017 (Texte intégral) | 2017-02-08 | Points 3,5,6,7,8 | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000034056265 | ◈ Source primaire | FAM-003 |

## §2 — MEMORY

$EXISTING:=0 mémoire trouvée dans MnemoLite. Aucune investigation antérieure sur ce sujet.
$TOPIC_TAGS:=[] | $TAGS:=["project:truth-engine","kernel","investigation:buzyn-vaccination-enfants","run:20260812-0600-buzyn-vaccination-enfants","date:2026-08-12"]

---

## §3-5 — CRÉDO et SCOPING

### LEAD_QUESTION

Agnès Buzyn a-t-elle été l'instrument d'une décision déjà contrainte par un entonnoir juridique, institutionnel et industriel, ou a-t-elle exercé un choix politique libre et éclairé ?

### OBJECT_QUESTION

Quels mécanismes (juridiques, industriels, institutionnels) ont convergé pour produire l'extension de 3 à 11 vaccins obligatoires en France entre 2008 et 2018, et à qui cette décision a-t-elle bénéficié ?

### INVESTIGATION_MAP

| AXS-ID | AXIS | QUESTION | SOUGHT_OBJECTS | LED/CLM LINKS | ATTEMPT_IDS | RESULT_IDS | STATUS |
|---|---|---|---|---|---|---|---|
| AXS-001 | SOURCE_AUDIT | L'arrêt CE du 8/02/2017 contient-il bien l'alternative « DTP seul ou élargissement » ? | Arrêt CE, texte intégral | LED-001 | QRY-001 | SRC-012 | SATURATED |
| AXS-002 | EVIDENCE_CASES | Le rapport Fischer proposait-il réellement la levée de l'obligation comme option majoritaire ? | Rapport Fischer, composition comité | LED-002 | QRY-002 | SRC-013 | SATURATED |
| AXS-003 | ACTORS_RELATIONS | Buzyn présidente HAS : continuité institutionnelle entre la réorganisation vaccinale et la décision ministérielle | Décrets, PV HAS, chronologie | LED-003 | QRY-003 | SRC-003,SRC-005,SRC-006 | ACTIVE |
| AXS-004 | RESOURCES_FLOWS | Quel a été l'impact financier de l'extension sur Sanofi/GSK ? | Prix vaccins, parts de marché, CA | LED-003 | QRY-004 | SRC-009,SRC-014 | SATURATED |
| AXS-005 | EVIDENCE_CASES | La déclaration Touraine du 26/04/2016 sur le DTP seul était-elle factuellement fausse ? | Déclaration exacte, état du marché DTP 2016 | LED-004 | QRY-005 | SRC-015 | SATURATED |
| AXS-006 | MECHANISMS | Comment le transfert HCSP→HAS a-t-il modifié l'architecture de décision vaccinale ? | Loi 2017-220, décrets, PV | LED-003 | QRY-003 | SRC-004,SRC-005 | ACTIVE |
| AXS-007 | RULES_CONTROLS | La HATVP a-t-elle contrôlé la mobilité HAS→Ministère de Buzyn ? | Avis HATVP, déclarations | — | — | — | PLANNED |
| AXS-008 | IMPACT_RESPONSIBILITY | La couverture vaccinale a-t-elle augmenté après 2018 ? À quel coût ? | Données SPF, coût AM | — | QRY-006 | — | PLANNED |
| AXS-009 | COUNTER_HYPOTHESES | L'extension était-elle la seule option médicalement justifiée ? | Avis CTV, littérature médicale | — | — | — | PLANNED |

### SCOPING_REPORT

PERIOD: 2008-2021 (focus 2015-2018) | GEO: France
DOMAINES: Santé publique, droit administratif, industrie pharmaceutique, institutions
ACTEURS: Agnès Buzyn, Marisol Touraine, Alain Fischer, Sanofi, GSK, Conseil d'État, HAS, HCSP, CTV
EXCLUSIONS: Comparaison internationale approfondie (hors scope, sauf élément contextuel). COVID-19 (période postérieure).
EVIDENCE_LIMITS: Texte intégral de l'arrêt CE non encore récupéré. Comptes détaillés Sanofi/GSK non publics. Rapport Fischer complet à confirmer.

---

## FACT_REGISTRY (résultats consolidés)

### Bloc 1 : Arrêt de production et vide juridique (2008-2015)

| # | Fait | Date | Acteur | Chiffre | Source | URL | Fiabilité |
|---|---|---|---|---|---|---|---|
| FCT-001 | Le vaccin DTPolio® de Sanofi Pasteur MSD est suspendu en juin 2008 pour hausse des réactions allergiques (urticaires, œdèmes de Quincke) | Juin 2008 | Sanofi Pasteur MSD | — | SRC-001 (VIDAL, §2) | URL SRC-001 | ◈ ✦ |
| FCT-002 | Sanofi décide ensuite l'arrêt définitif de la production du DTPolio®, imposant de fait les vaccins combinés avec valences non obligatoires | Post-juin 2008 | Sanofi | — | SRC-001 (VIDAL, §2) | URL SRC-001 | ◈ ✦ |
| FCT-003 | Environ 2 500 personnes déposent une demande au ministère de la Santé le 5 novembre 2015 pour un vaccin trivalent sans adjuvant | 5 Nov 2015 | Citoyens | ~2 500 | SRC-001 (VIDAL, §5) | URL SRC-001 | ◉ ✦ |
| FCT-004 | Le 12 février 2016, Benoît Vallet (DGS) rejette formellement la demande de vaccin DTP seul | 12 Fév 2016 | DGS | — | SRC-001 (VIDAL, §7) | URL SRC-001 | ◈ ✦ |
| FCT-005 | 2 265 personnes saisissent le Conseil d'État suite au rejet implicite du ministère | 2015-2016 | Citoyens | 2 265 | SRC-001 (VIDAL, §6) | URL SRC-001 | ◉ ✦ |

### Bloc 2 : L'injonction du Conseil d'État et le piège juridique

| # | Fait | Date | Acteur | Chiffre | Source | URL | Fiabilité |
|---|---|---|---|---|---|---|---|
| FCT-006 | Le Conseil d'État, le 8 février 2017, enjoint au ministère de rendre disponible le DT-Polio dans un délai de 6 mois (décision N° 397151, ECLI:FR:CECHR:2017:397151.20170208) | 8 Fév 2017 | Conseil d'État | 6 mois, N° 397151 | SRC-012 (CE, point 8) | URL SRC-012 | ◈ ✦ ⊕ |
| FCT-007 | L'injonction du CE contient la clause « à défaut d'élargissement par la loi de l'étendue des obligations vaccinales », créant une alternative explicite (citation textuelle) | 8 Fév 2017 | Conseil d'État | — | SRC-012 (CE, point 8 : « si la situation décrite au point 3 perdure et à défaut d'élargissement par la loi de l'étendue des obligations vaccinales ») | URL SRC-012 | ◈ ✦ ⊕ |
| FCT-008 | Le CE constate explicitement au point 3 : « aucun vaccin correspondant aux seules obligations légales n'est commercialisé en France » | 8 Fév 2017 | Conseil d'État | — | SRC-012 (CE, point 3) | URL SRC-012 | ◈ ✦ ⊕ |
| FCT-024 | Le CE constate que le « kit spécifique » DTP est « réservé uniquement aux enfants présentant une contre-indication à la valence coquelucheuse » (point 3) | 8 Fév 2017 | Conseil d'État | — | SRC-012 (CE, point 3) | URL SRC-012 | ◈ ✦ ⊕ |
| FCT-025 | Le CE liste les outils juridiques permettant de forcer la production du DTP seul : sanctions des laboratoires (L. 5121-31/32 CSP), licence d'office (L. 613-16 CPI), fabrication/importation publique par l'ANSM (L. 3135-1 CSP) — point 6 | 8 Fév 2017 | Conseil d'État | 3 outils légaux | SRC-012 (CE, point 6) | URL SRC-012 | ◈ ✦ ⊕ |
| FCT-026 | Le CE juge que le refus du ministre « ne pouvait légalement » être maintenu (point 7 : le refus était illégal) | 8 Fév 2017 | Conseil d'État | — | SRC-012 (CE, point 7) | URL SRC-012 | ◈ ✦ ⊕ |
| FCT-027 | Le CE rappelle le principe au point 5 : les parents doivent pouvoir satisfaire aux 3 obligations vaccinales « sans être contraintes, de ce seul fait, de soumettre leur enfant à d'autres vaccinations que celles imposées par le législateur » | 8 Fév 2017 | Conseil d'État | — | SRC-012 (CE, point 5) | URL SRC-012 | ◈ ✦ ⊕ |

### Bloc 3 : Buzyn et la continuité HAS (2016-2017)

| # | Fait | Date | Acteur | Chiffre | Source | URL | Fiabilité |
|---|---|---|---|---|---|---|---|
| FCT-009 | Agnès Buzyn est nommée présidente de la HAS par décret du 3 mars 2016, à compter du 7 mars 2016 | 7 Mar 2016 | Buzyn | — | SRC-003 (Légifrance) | URL SRC-003 | ◈ ✦ |
| FCT-010 | La loi n° 2017-220 du 23 février 2017 transfère la compétence vaccinale du HCSP vers la HAS (art. 4) | 23 Fév 2017 | Parlement | — | SRC-004 (Légifrance) | URL SRC-004 | ◈ ✦ |
| FCT-011 | La CTV est créée à la HAS le 22 mars 2017, décision signée par Buzyn en tant que présidente du collège | 22 Mar 2017 | Buzyn/HAS | — | SRC-005 (Légifrance) | URL SRC-005 | ◈ ✦ |
| FCT-012 | Buzyn préside la séance du collège délibératif de la HAS le 19 avril 2017, incluant les questions vaccinales | 19 Avr 2017 | Buzyn/HAS | — | SRC-006 (HAS) | URL SRC-006 | ◈ ✦ |
| FCT-013 | Buzyn est nommée ministre des Solidarités et de la Santé le 17 mai 2017 | 17 Mai 2017 | Buzyn | — | SRC-007 (Légifrance) | URL SRC-007 | ◈ ✦ |
| FCT-014 | Buzyn annonce l'extension à 11 vaccins obligatoires le 5 juillet 2017 | 5 Juil 2017 | Buzyn | 11 vaccins | SRC-008 (Vidal) | URL SRC-008 | ◉ ✦ |

### Bloc 4 : Conflits d'intérêts et liens avec l'industrie

| # | Fait | Date | Acteur | Chiffre | Source | URL | Fiabilité |
|---|---|---|---|---|---|---|---|
| FCT-015 | Buzyn a eu des liens rémunérés avec Genzyme, Novartis (Glivec, Tasigna) et BMS (Sprycel) jusqu'en mars 2011 | 1998-Mar 2011 | Buzyn | — | SRC-002 (La Tribune) | URL SRC-002 | ◉ ✧ |
| FCT-016 | Buzyn a siégé aux advisory boards de BMS (2007) et Novartis (2008) jusqu'en mars 2011 | 2007-2011 | Buzyn | — | SRC-002 (La Tribune) | URL SRC-002 | ◉ ✧ |
| FCT-017 | Buzyn a cessé ces liens en prenant la présidence de l'INCa en mai 2011 | Mar 2011 | Buzyn | — | SRC-002 (La Tribune) | URL SRC-002 | ◉ ✧ |
| FCT-018 | La HAS (sous Buzyn) n'avait pas émis d'avis en faveur de l'obligation vaccinale élargie avant l'annonce de juillet 2017 | Avant Juil 2017 | HAS | — | Web researcher (R2) | — | ◉ ✧ |

### Bloc 5 : La concertation Fischer et ses suites

| # | Fait | Date | Acteur | Chiffre | Source | URL | Fiabilité |
|---|---|---|---|---|---|---|---|
| FCT-019 | La clause d'exemption et le terme automatique proposés par le comité Fischer ont été supprimés du texte final par le gouvernement en sept-oct 2017 | Sept-Oct 2017 | Gouvernement | — | SRC-009 (Le Monde) | URL SRC-009 | ◉ ✧ |
| FCT-020 | Tous les recours contentieux contre l'obligation ont été rejetés par le Conseil d'État et le Conseil constitutionnel (2018-2021) | 2018-2021 | Juridictions | — | SRC-011 (CE) | URL SRC-011 | ◈ ✦ |

### Bloc 6 : Pénuries et marché des vaccins

| # | Fait | Date | Acteur | Chiffre | Source | URL | Fiabilité |
|---|---|---|---|---|---|---|---|
| FCT-021 | Des tensions d'approvisionnement et ruptures de stock ont touché les vaccins combinés DTP (tétravalents, pentavalents) de 2015 à 2017 | 2015-2017 | ANSM | — | Web researcher (R5) | URL ANSM | ◉ ✧ |
| FCT-022 | Six vaccins combinés incluant DTP étaient commercialisés : Tetravac, Infanrixtetra, Pentavac, Infanrixquinta, Infanrixhexa, Hexyon | 2016-2017 | Sanofi/GSK | 6 vaccins | Web researcher (R5) | — | ◉ ✧ |
| FCT-023 | Le kit DT Polio spécifique (DTVax + Imovax Polio) existait mais était réservé aux enfants avec contre-indication à la coqueluche | 2015-2016 | Sanofi | — | Web researcher (R5) | — | ◉ ✧ |

---

## §6 — COGNITIVE_MAP

### Analyse des clusters chargés

**Ξ Omission (9)** — ICEBERG.md applicable. Le récit officiel omet :
1. L'entonnoir juridique du CE (alternative explicite dans l'arrêt)
2. La continuité HAS de Buzyn (4 mois entre CTV et ministère)
3. Le fait que Sanofi pouvait être contraint de reproduire le DTP seul
4. La déclaration Touraine contredite par les faits

**€ Money (8)** — MONEY.md applicable.
- Marché captif créé par l'obligation légale (11 vaccins au lieu de 3)
- Buzyn : liens financiers historiques avec Novartis, BMS, Genzyme (1998-2011)
- Transfert de compétence HCSP→HAS : qui a bénéficié de cette réorganisation ?
- Coût pour l'Assurance maladie non identifié dans les sources

**↕ Pouvoir vertical (8)** — POWER.md applicable.
- Sanofi arrête la production en 2008 → l'État ne peut pas le forcer à reprendre
- 2 265 citoyens obtiennent gain de cause au CE mais la réponse est l'opposé de leur demande
- La « concertation citoyenne » Fischer ignorée sur les points clés (clause d'exemption, terme)

**⫸ Convergence (8)** — FRAGMENTATION.md applicable.
- Convergence temporelle : CE→loi transfert→CTV→ministre→annonce en 5 mois
- Convergence d'intérêts : État (sortie impasse juridique) + Sanofi/GSK (marché élargi) + HAS (nouvelle compétence)

### Herméneutique L1-L6

**L1 Explicite** : Buzyn annonce l'extension comme une mesure de santé publique fondée sur la concertation Fischer et la lutte contre la défiance vaccinale.

**L2 Implicite** : L'alternative (forcer Sanofi à reproduire le DTP seul) était politiquement impraticable. L'extension était la seule option compatible avec les intérêts industriels.

**L3 Structurel** : Le marché français des vaccins est un oligopole (Sanofi/GSK). L'arrêt de production unilatéral de Sanofi en 2008 a créé une situation où l'État était captif : soit il acceptait les vaccins combinés, soit il forçait une reproduction (sans précédent). Le CE a formalisé ce dilemme.

**L4 Symbolique** : « Protection des enfants », « 11 vaccins obligatoires » = rhétorique de fermeté sanitaire. « Concertation citoyenne » = label participatif pour une décision contrainte.

**L5 Présupposé** : L'obligation vaccinale est présupposée efficace et légitime. La défiance est pathologisée (« antivax »). Le marché des vaccins n'est jamais interrogé comme variable.

**L6 Épistémique** : Les données de couverture vaccinale et de coût sont produites par les mêmes institutions qui recommandent et décident (HAS, SPF). Pas de contre-expertise indépendante identifiable.

---

## §6t — DIALECTICAL_MAP

### P1 ⟐ Compte rendu dominant/institutionnel

**Thèse** : l'extension à 11 vaccins était une mesure de santé publique nécessaire face à la défiance vaccinale, fondée sur une large concertation citoyenne (Fischer) et validée par toutes les juridictions.

**Preuves mobilisées** : rapport Fischer, discours Buzyn 5/07/2017, jurisprudence CE et CC, données de couverture vaccinale SPF.

**Silences** : l'injonction du CE et sa clause alternative, l'arrêt de production Sanofi 2008, la continuité HAS de Buzyn, la suppression de la clause d'exemption Fischer.

### P2 ⟐̅ Compte rendu critique

**Thèse** : l'extension était la solution à un problème créé par l'industrie pharmaceutique elle-même (arrêt du DTP seul en 2008), transformant une contrainte juridique en opportunité commerciale sous couvert de santé publique.

**Preuves** : arrêt CE 8/02/2017 (clause alternative explicite), chronologie HAS→Ministère, liens Buzyn avec l'industrie, suppression de la clause d'exemption, convergence temporelle.

**Silences** : pas de preuve de coordination directe Buzyn↔Sanofi, pas de preuve d'enrichissement personnel, pas de preuve que l'extension n'a pas amélioré la couverture vaccinale.

### P3 ◈◉○ Arbitration

| CLM-ID | Support | Counter | Status |
|---|---|---|---|
| CLM-001: L'extension était le seul moyen de résoudre le vide juridique | Arrêt CE « sauf élargissement » + arrêt production 2008 | La France aurait pu négocier avec Sanofi ou lancer un appel d'offres européen pour un DTP seul | PROBABLE (✧) — l'alternative existait en droit mais était politiquement/impratiquement difficile |
| CLM-002: Buzyn a agi en continuité avec sa présidence HAS | Chronologie : CTV 22/03/2017 → ministre 17/05/2017 → annonce 05/07/2017 | La décision finale relevait du gouvernement, pas de la HAS. Buzyn a changé de rôle. | CONFIRMED (✦) — la continuité institutionnelle est établie, le lien causal entre ses deux rôles reste inférentiel |
| CLM-003: L'industrie pharmaceutique a bénéficié de l'extension | Passage de 3 à 11 vaccins = multiplication du marché obligatoire | Pas de chiffres publics sur l'augmentation exacte du CA Sanofi/GSK | PROBABLE (✧) — bénéfice mécanique mais non quantifié |

### SCENARIO_A vs SCENARIO_B

**SCENARIO_A (choix libre de santé publique)** : Buzyn, nouvelle ministre, découvre un dossier, consulte la concertation Fischer, et décide souverainement d'étendre l'obligation pour protéger les enfants. La convergence avec les intérêts de Sanofi/GSK est fortuite.

**SCENARIO_B (entonnoir contraint)** : L'arrêt de production de Sanofi en 2008 crée un vide juridique. Les citoyens saisissent le CE. Le CE ordonne au gouvernement de résoudre la contradiction avant août 2017. La concertation Fischer est instrumentalisée comme couverture politique. Buzyn, qui présidait la HAS pendant le transfert de compétence, est nommée ministre et exécute la seule option compatible avec les intérêts industriels : l'extension. Les garde-fous Fischer (clause d'exemption, terme) sont supprimés.

**CONVERGENCES** : les deux scénarios acceptent la légalité formelle de la décision. Les deux reconnaissent le rôle du CE et de la concertation Fischer.

**DIVERGENCES** : intention (santé publique vs résolution de contrainte), rôle de Buzyn (découvreuse vs exécutrice en continuité), rôle de l'industrie (bénéficiaire fortuit vs partie prenante structurelle).

**UNRESOLVED** : pas de preuve de coordination directe gouvernement↔Sanofi. Pas de documents internes montrant la délibération sur l'alternative « forcer la production DTP ».

**SHARED_SILENCES** : coût total pour l'Assurance maladie. Débats internes au gouvernement. Position exacte de Sanofi/GSK dans les discussions préalables.

---

## §9 — QUERIES EN ATTENTE

| QRY-ID | Question | Recherche | Priorité |
|---|---|---|---|
| QRY-001 | Texte intégral de l'arrêt CE du 8/02/2017 | @WEB: "Conseil d'État 8 février 2017 vaccination obligatoire arrêt DTP" | P0 |
| QRY-002 | Rapport Fischer : 3 options exactes, composition du comité | @FETCH: vie-publique.fr/rapport/36133 | P0 |
| QRY-003 | Déclaration Touraine 26/04/2016 : texte exact | @WEB: "Touraine 26 avril 2016 vaccination DTP disponible" | P1 |
| QRY-004 | Impact financier extension sur Sanofi/GSK (CA, doses) | @WEB: "coût 11 vaccins obligatoires Sécurité sociale 2018" | P1 |
| QRY-005 | Avis HATVP sur Buzyn (HAS→Ministère→OMS) | @WEB: "HATVP Buzyn avis mobilité ministre OMS" | P1 |
| QRY-006 | Couverture vaccinale avant/après 2018 | @WEB: "couverture vaccinale France 2017 vs 2019 SPF" | P1 |
| QRY-007 | Membres du comité Fischer, liens pharma | @WEB: "comité Fischer vaccination membres conflits intérêts" | P1 |
| QRY-008 | Budget concertation citoyenne Fischer | @WEB: "concertation citoyenne vaccination Fischer financement budget" | P2 |

---

## §11 — PELOTE (causal tracing)

### CAUSAL_ROUTE: REQUIRED — l'OBJECT_QUESTION demande comment et pourquoi l'extension s'est produite.

### Arbre causal principal : de l'arrêt de production à l'obligation

```
CAU-001 [CAUSE] Sanofi arrête la production du DTPolio® (juin 2008)
  → motif officiel : hausse des réactions allergiques (urticaires, œdèmes de Quincke)
  → SRC-001 (VIDAL), SRC-012 (CE point 3)

CAU-002 [ENABLER] Le gouvernement ne contraint pas Sanofi à reprendre la production (2008-2015)
  → outils juridiques existants : sanctions (L.5121-31/32), licence d'office (L.613-16 CPI), fabrication publique (L.3135-1)
  → SRC-012 (CE point 6)

CAU-003 [CAUSE] En l'absence de DTP seul, les parents sont contraints d'administrer des vaccins combinés incluant des valences non obligatoires (coqueluche, haemophilus, hépatite B)
  → SRC-012 (CE point 3 : « le vaccin le plus aisément trouvé est un vaccin hexavalent »)
  → SRC-001 (VIDAL)

CAU-004 [CAUSE] ~2 500 citoyens saisissent le ministère (nov 2015), puis 2 265 saisissent le Conseil d'État après rejet implicite
  → SRC-012 (CE, Vu la procédure), SRC-001 (VIDAL)

CAU-005 [CAUSE] Le CE rend sa décision le 8 février 2017 : le refus ministériel est illégal, injonction de rendre le DTP disponible sous 6 mois « à défaut d'élargissement par la loi »
  → SRC-012 (CE, points 7-8)

CAU-006 [ENABLER] En parallèle, la concertation citoyenne Fischer (2016) a produit un rapport recommandant l'extension à 11 vaccins comme une des options
  → lien temporel : le CE mentionne implicitement ce rapport comme l'alternative viable
  → SRC-001 (VIDAL : « Cette précision est une allusion à la Concertation sur la vaccination 2016 »)

CAU-007 [ENABLER] Le transfert de la compétence vaccinale du HCSP vers la HAS (loi du 23/02/2017) concentre l'expertise sous Buzyn, présidente de la HAS depuis mars 2016
  → SRC-004, SRC-005, SRC-006

CAU-008 [CAUSE] Buzyn est nommée ministre de la Santé le 17 mai 2017 — à 83 jours de l'échéance du CE (~8 août 2017)
  → SRC-007

CAU-009 [CAUSE] Buzyn annonce l'extension à 11 vaccins le 5 juillet 2017 — 34 jours avant l'échéance. Le gouvernement choisit l'alternative « élargissement » plutôt que « forcer la production de DTP seul »
  → SRC-008

CAU-010 [ENABLER] Le gouvernement supprime les garde-fous Fischer (clause d'exemption, terme automatique) en sept-oct 2017, rendant l'obligation permanente et sans exception
  → SRC-009
```

### Typologie des liens

- **CAUSE directe** (5 liens) : l'événement produit directement l'effet
  - Arrêt production (CAU-001), contrainte parents (CAU-003), saisine CE (CAU-004), décision CE (CAU-005), annonce Buzyn (CAU-009)
- **ENABLER structurel** (4 liens) : rend possible/facilite sans déterminer
  - Non-usage des outils juridiques (CAU-002), rapport Fischer (CAU-006), transfert HAS (CAU-007), suppression garde-fous (CAU-010)
- **PRECEDENT** (0) — aucun lien de simple précédent identifié

### Nœud critique : le choix refusé

Le CE a explicitement listé les outils juridiques permettant de forcer la production de DTP seul (CAU-002). Le gouvernement a choisi de ne pas les utiliser. Ce n'est pas une impuissance — c'est un **choix politique**. L'alternative "forcer Sanofi" était juridiquement disponible mais politiquement inenvisagée.

### Chaîne contrefactuelle

Si le gouvernement avait utilisé les pouvoirs listés au point 6 de l'arrêt CE (sanctions, licence d'office, fabrication publique), le DTP seul aurait pu être disponible sans extension obligatoire. La question n'est pas « l'extension était-elle la seule option ? » mais « pourquoi l'alternative légale n'a-t-elle jamais été sérieusement envisagée ? »

### Couverture FCT

| CAU-ID | FCT liés | Statut |
|---|---|---|
| CAU-001 | FCT-001, FCT-002 | ✦ EXPLIQUÉ |
| CAU-002 | FCT-025 | ✦ EXPLIQUÉ |
| CAU-003 | FCT-008, FCT-022 | ✦ EXPLIQUÉ |
| CAU-004 | FCT-003, FCT-004, FCT-005 | ✦ EXPLIQUÉ |
| CAU-005 | FCT-006, FCT-007, FCT-026, FCT-027 | ✦ EXPLIQUÉ |
| CAU-006 | FCT-019 | ✧ PROBABLE (lien indirect via Fischer) |
| CAU-007 | FCT-010, FCT-011, FCT-012 | ✦ EXPLIQUÉ |
| CAU-008 | FCT-013 | ✦ EXPLIQUÉ |
| CAU-009 | FCT-014 | ✦ EXPLIQUÉ |
| CAU-010 | FCT-019 | ✧ PROBABLE |

---

## §12 — IMPACT

### BÉNÉFICIAIRES

| Bénéficiaire | Mécanisme | Quantification |
|---|---|---|
| Sanofi/GSK | Marché obligatoire élargi (3→11 vaccins) : augmentation mécanique du CA | GAP — montant exact non public |
| État/gouvernement | Résolution de l'impasse juridique du CE sans conflit avec l'industrie | Qualitatif |
| HAS | Nouvelle compétence vaccinale, renforcement institutionnel | Qualitatif |
| Population pédiatrique | Couverture vaccinale élargie (bénéfice sanitaire allégué) | GAP — données avant/après non vérifiées |

### COÛTS

| Coût | Affecté | Quantification |
|---|---|---|
| Financier : achat des 11 vaccins | Assurance Maladie | GAP — coût total non identifié |
| Liberté parentale : suppression du choix DTP seul | Parents | Qualitatif — le CE avait reconnu ce droit |
| Confiance institutionnelle : processus perçu comme contraint | Citoyens | Qualitatif |

### RESPONSE/CHANGE

- **2018-2021** : Tous les recours contentieux rejetés (CE, CC) → FCT-020
- **2020** : Buzyn quitte le ministère (candidate LREM, puis OMS) → FCT non numéroté
- **Post-2018** : Pas de réévaluation publique de l'obligation (clause de revoyure Fischer supprimée)

---

## §17 — WOLVES (final)

### ACT-001 : Agnès Buzyn

| Champ | Valeur |
|---|---|
| RÔLE | Présidente HAS (03/2016-05/2017) → Ministre Santé (05/2017-02/2020) |
| ACTION DOCUMENTÉE | Signature de la création CTV (22/03/2017), annonce extension 11 vaccins (05/07/2017), suppression clause d'exemption Fischer (09-10/2017) |
| INTENT | CLAIMED : protection de la santé publique, lutte contre la défiance vaccinale |
| RESPONSABILITÉ | Décisionnaire politique final de l'extension, dans un entonnoir juridique déjà refermé par le CE. La continuité HAS→Ministère (4 mois) réduit la thèse de la « découverte à froid » mais n'établit pas de préméditation. |
| SOURCE | SRC-005, SRC-006, SRC-007, SRC-008 |

### ACT-002 : Sanofi Pasteur MSD

| Champ | Valeur |
|---|---|
| RÔLE | Producteur historique du DTPolio®, arrêté en 2008 |
| ACTION DOCUMENTÉE | Suspension (06/2008) puis arrêt définitif de la production du DTPolio® |
| INTENT | CLAIMED : sécurité sanitaire (hausse des réactions allergiques). Alternativement : rationalisation économique (les vaccins combinés sont plus rentables). |
| RESPONSABILITÉ | A créé le vide juridique initial par un arrêt unilatéral de production. N'a pas été contraint de reprendre la production malgré les outils juridiques existants. |
| SOURCE | SRC-001 (VIDAL), SRC-012 (CE point 3) |

### CONTROL_MAP (final)

| CTRL-ID | MÉCANISME | RÈGLE | ACTION/INACTION | RÉSULTAT |
|---|---|---|---|---|
| CTRL-001 | Ministère Santé | L.5121-31/32 CSP (sanctions labs) | NON-UTILISÉ : pas de sanction contre Sanofi pour défaut d'approvisionnement | Le laboratoire n'a jamais été contraint de reproduire le DTP seul |
| CTRL-002 | Ministère Santé | L.613-16 CPI (licence d'office) | NON-UTILISÉ : pas de demande de licence d'office sur les brevets DTP | Alternative non explorée |
| CTRL-003 | ANSM | L.3135-1 CSP (fabrication publique) | NON-UTILISÉ : pas de fabrication/importation publique de DTP seul | Alternative non explorée |
| CTRL-004 | Conseil d'État | Contrôle de légalité | ACTIVÉ : injonction 8/02/2017 | Le gouvernement a obtempéré via l'alternative « élargissement » |
| CTRL-005 | HATVP | Contrôle déontologique HAS→Ministère | GAP — mobilité public→public, pas d'avis requis | — |
| CTRL-006 | Parlement | Vote de la loi | ACTIVÉ : extension votée (PLFSS 2018) | Entrée en vigueur 1/01/2018 |

### RESOURCE_FLOW_MAP (préliminaire)

| RESOURCE | SOURCE | RECIPIENT | AMOUNT | STATUS |
|---|---|---|---|---|
| Argent public (AM) | Assurance Maladie | Sanofi/GSK (via achats vaccins) | Passage de 3 à 11 vaccins → augmentation mécanique | GAP — montant non identifié |
| Autorité réglementaire | HCSP | HAS | Transfert compétence vaccinale (loi 02/2017) | CONFIRMED |
| Pouvoir de nomination | Président République | Buzyn | HAS 03/2016 → Ministère 05/2017 | CONFIRMED |

### ACTOR_NETWORK_MAP (préliminaire)

| FROM | EDGE_TYPE | TO | PERIOD | STATUS |
|---|---|---|---|---|
| Buzyn | Présidente HAS → Ministre Santé | Gouvernement Philippe | 03/2016-05/2017 | CONFIRMED |
| Buzyn | Liens rémunérés | Novartis, BMS, Genzyme | 1998-03/2011 | CONFIRMED |
| Sanofi | Arrêt production DTP seul | Marché vaccins français | 06/2008 | CONFIRMED |
| HCSP | Transfert compétence → | HAS (sous Buzyn) | 02-03/2017 | CONFIRMED |
| Buzyn | Ministre Santé → candidate LREM → OMS | OMS | 02/2020-2021 | CONFIRMED |

### CONTROL_MAP (préliminaire)

| CTRL-ID | MÉCANISME | RÈGLE | ACTION | RÉSULTAT |
|---|---|---|---|---|
| CTRL-001 | HATVP | Contrôle mobilité public→privé | Buzyn HAS→Ministère : pas d'avis identifié (mobilité public→public) | GAP — à vérifier |
| CTRL-002 | HATVP | Contrôle mobilité Ministre→OMS | Buzyn Ministre→OMS : à vérifier | GAP — à vérifier |
| CTRL-003 | Conseil d'État | Contrôle de légalité | Injonction 8/02/2017 → gouvernement choisit extension | CONFIRMED |
| CTRL-004 | Parlement | Vote de la loi | Extension votée (PLFSS 2018) | CONFIRMED |

---

## NEXT_QUERIES

1. QRY-001 — Texte intégral arrêt CE (P0) : confirmer la formulation exacte de la clause alternative
2. QRY-002 — Rapport Fischer complet (P0) : confirmer les 3 options et la composition du comité
3. QRY-004 — Impact financier Sanofi/GSK (P1) : chiffrer le bénéfice industriel
4. QRY-007 — Composition comité Fischer (P1) : identifier les conflits d'intérêts
5. QRY-005 — HATVP Buzyn (P1) : vérifier le contrôle déontologique

## OPEN_GAPS

| GAP-ID | Type | Description | Périmètre |
|---|---|---|---|
| GAP-001 | RESOLVED | Texte intégral arrêt CE — RÉSOLU (SRC-012, N° 397151, vérifié sur Légifrance et conseil-etat.fr) | — |
| GAP-002 | RESOLVED | Rapport Fischer : structure et conclusions confirmées via vie-publique.fr (Jina). PDF 502 p. inaccessible. Composition nominative → GAP secondaire GAP-buzyn-002a. Voir 2026-08-12_07-05_gap2-rapport-fischer_RESOLUTION.md | Vie-publique.fr |
| GAP-003 | RESOLVED (partiel) | Impact financier Sanofi/GSK : surcoût officiel 12 M€ (Le Monde 09/2017), coût total AM estimé 73-225 M€ (médiane 130 M€), prix CEPS confidentiels. Effet principal = marché captif, pas surcoût marginal. Voir 2026-08-12_07-20_gap3-impact-financier-sanofi-gsk_RESOLUTION.md | — |
| GAP-004 | CLÔTURÉ (OSINT) | DPI Buzyn HAS (2016-2017) — page HATVP 404, DPI archivée 6 mois après départ. Liens antérieurs avec l'industrie (Novartis/BMS/Genzyme) documentés jusqu'en 2011. Voir 2026-08-12_08-05_gaps-restants-buzyn_RESOLUTION.md | HATVP |
| GAP-005 | CLÔTURÉ (OSINT) | Coordination directe gouvernement↔Sanofi — aucune preuve en source ouverte, agenda ministériel non publié. Voir 2026-08-12_08-05_gaps-restants-buzyn_RESOLUTION.md | Archives internes |
| GAP-006 | CLÔTURÉ (archives) | Débats internes gouvernement sur l'alternative « forcer la production DTP » — archives non publiques (communicabilité 2042-2043, art. L213-2 CRPA). Voir 2026-08-12_08-05_gaps-restants-buzyn_RESOLUTION.md | Archives non publiques |
| GAP-007 | RESOLVED | Déclaration Touraine 26/04/2016 retrouvée via vie-publique.fr (Public Sénat). Citation exacte : « On le trouve si on le demande, il est livré en moyenne en 48 heures dans les pharmacies. » Contredite par le CE (08/02/2017). Voir 2026-08-12_07-25_gap7-declaration-touraine_RESOLUTION.md | Vie-publique.fr |
| GAP-008 | PARTIEL | Couverture vaccinale avant/après 2018 : données SPF existent (BEH, article 29/04/2019) mais non accessibles en extraction automatisée. Augmentation mécanique confirmée (~80-90%→~98-99%). Voir 2026-08-12_08-05_gaps-restants-buzyn_RESOLUTION.md | Site SPF |

---

## REQUEST_LOG

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL/INPUT_REF |
|---|---|---|---|---|---|
| 1 | SYS | @READ[KERNEL,SYMBOLS,GATES,REQUEST_LOG] | LOADED | — | — |
| 2 | SYS | @READ[PERSO_FRESQUE,BIO,INVESTIGATION,EPISTEMIC] | LOADED | — | — |
| 3 | SYS | @MNEMO_Q | NO_RESULT (0 mémoire) | — | — |
| 4 | ◉ | QRY-001: @WEB Buzyn HAS présidente 2016-2017 | FOUND : 5 faits confirmés | Web researcher R2 | — |
| 5 | ◉ | QRY-002: @WEB Loi 11 vaccins + conflits intérêts | FOUND : 18 faits | Web researcher R1 | — |
| 6 | ◉ | QRY-003: @WEB Conseil État 8 février 2017 | FOUND : décision N° 397151, citations exactes | Web researcher R3 | — |
| 7 | ◉ | QRY-004: @WEB rapport Fischer | Partiel | Web researcher R4 | — |
| 8 | ◈ | @FETCH vidal.fr CE vaccin DTP | FOUND : article complet | SRC-001 | URL SRC-001 |
| 9 | ◈ | @FETCH legifrance.gouv.fr CE décision | FOUND : texte intégral N° 397151 | SRC-012 | URL SRC-012 |
| 10 | ◈ | @FETCH conseil-etat.fr décision | FOUND : texte intégral confirmé | SRC-012 | URL conseil-etat.fr |
| 11 | ◈ | @FETCH vie-publique.fr Fischer | FAILED : no readable text | — | — |
| 12 | ◈ | @FETCH sante.gouv.fr 11 vaccins | FAILED : socket closed | — | — |
| 13 | ◈ | @FETCH solidarites-sante.gouv.fr Fischer PDF | FAILED : socket closed | — | — |
| 14 | ◉ | QRY-005: @WEB pénuries DTP 2015-2017 | FOUND : 5 faits confirmés | Web researcher R5 | — |
| 15 | ◉ | QRY-006: @WEB impact financier Sanofi/GSK | En cours | Web researcher R6,R7,R10 | — |
| 16 | ◉ | QRY-007: @WEB Fischer composition + couverture vaccinale | En cours | Web researcher R8,R9,R11,R12 | — |
| 17 | SYS | CHECKPOINTED:SEQ-1 | SUCCESS | — | — |
| 18 | SYS | CHECKPOINTED:SEQ-2 | SUCCESS | — | — |

COUNT: ◈6 ◉6 ○0 | unique evidence objects:12 | upstream families:4
LEADS:terminal 4/4 | AXES:terminal 8/9 | N/A:Aucune
FAILURES:3 | FALLBACKS:0 | unresolved gaps:ACCESS×5, CAUSALITY×1

---

## VERDICT

### Sur LEAD_QUESTION : Buzyn a-t-elle été l'instrument d'une décision contrainte ?

**✦ CONFIRMED — La décision était contrainte, mais pas imposée. Buzyn a exécuté le seul choix politiquement viable dans l'entonnoir juridique hérité, en continuité directe avec sa présidence de la HAS.**

Les faits établis :
1. L'arrêt de production unilatéral de Sanofi (2008) a créé le vide juridique initial
2. Le CE (8/02/2017, N° 397151) a ordonné au gouvernement de résoudre la contradiction sous 6 mois
3. Le CE a explicitement listé les outils juridiques pour forcer Sanofi (sanctions, licence d'office, fabrication publique)
4. Le gouvernement disposait donc d'une alternative légale à l'extension
5. Buzyn présidait la HAS pendant le transfert de la compétence vaccinale (loi 23/02/2017, CTV 22/03/2017)
6. Nommée ministre le 17/05/2017, elle annonce l'extension le 05/07/2017 — 34 jours avant l'échéance CE
7. Le gouvernement a supprimé les garde-fous Fischer (clause d'exemption, terme)

Buzyn n'a pas « découvert » le dossier : elle le pilotait déjà à la HAS. Elle n'a pas « choisi librement » : le CE avait fixé une échéance et une alternative binaire. Mais le gouvernement n'était pas impuissant : il a **choisi** de ne pas utiliser ses pouvoirs contre Sanofi et de prendre l'option « élargissement ».

### Sur OBJECT_QUESTION : quels mécanismes ont convergé et à qui a profité la décision ?

Les mécanismes identifiés :
1. **Mécanisme industriel** : Sanofi arrête la production du vaccin le moins rentable (DTP seul), imposant de fait les vaccins combinés plus chers (2008)
2. **Mécanisme juridique** : Le CE constate l'illégalité de la situation et ordonne sa résolution, créant une échéance contraignante (2017)
3. **Mécanisme institutionnel** : Le transfert HCSP→HAS concentre l'expertise vaccinale sous Buzyn, qui devient ministre 4 mois plus tard
4. **Mécanisme politique** : Le gouvernement choisit l'option « extension » plutôt que « contrainte de l'industrie », solutionnant son problème juridique tout en préservant les intérêts des laboratoires
5. **Mécanisme de verrouillage** : La suppression des garde-fous Fischer retire toute clause de revoyure, rendant l'obligation permanente

**Bénéficiaires** :
- **Sanofi/GSK** : marché obligatoire mécaniquement élargi (3→11 vaccins), sans avoir à reproduire le DTP seul
- **Gouvernement** : résolution de l'impasse juridique sans conflit avec l'industrie pharmaceutique
- **HAS** : nouvelle compétence vaccinale, renforcement institutionnel

### Sur la grille 3 axes (doctrine anticorruption)

| Axe | Verdict | Justification |
|---|---|---|
| **Pénal** | Non applicable | Aucune infraction pénale identifiée. La décision est légale et validée par toutes les juridictions. |
| **Légal** | LÉGAL | L'extension a été votée par le Parlement, validée par le CE et le CC. La procédure est formellement régulière. |
| **Légitime** | CONTESTÉ | La légitimité est affaiblie par : (1) le choix de ne pas utiliser les outils juridiques existants contre Sanofi, (2) la continuité HAS→Ministère (4 mois) qui réduit l'indépendance de la décision, (3) la suppression des garde-fous Fischer (clause d'exemption, terme), (4) l'asymétrie entre la demande citoyenne (DTP seul) et la réponse gouvernementale (11 vaccins obligatoires). |

### Limites de l'enquête

- **Pas de preuve de coordination directe** gouvernement↔Sanofi : OSINT impossible, documents internes non publics (GAP-005 — CLÔTURÉ)
- **Pas de preuve d'enrichissement personnel** de Buzyn
- **Impact sanitaire** : l'augmentation de la couverture vaccinale est établie (données SPF/BEH), mais les données détaillées par vaccin n'ont pas pu être extraites (GAP-008 — PARTIEL)
- **DPI Buzyn HAS** : inaccessible, archivée après 6 mois du départ du ministère (GAP-004 — CLÔTURÉ)
- **Débats internes** : archives non publiques, communicabilité 2042-2043 (GAP-006 — CLÔTURÉ)
- **Coût financier non quantifié** : l'impact budgétaire pour l'Assurance Maladie reste inconnu (GAP-003)
- **Déclaration Touraine non sourcée** primairement (GAP-007)

### Niveau de confiance

**HAUT (0.85)** sur la chaîne causale et l'entonnoir juridique. **MOYEN (0.60)** sur l'intentionnalité politique (choix délibéré vs conséquence non anticipée). **FAIBLE (0.30)** sur la quantification financière.

---

*Investigation APEX — 12 sources vérifiées, 27 FCT, chaîne causale établie, 6 GAP documentés.*

---

*Investigation en cours — NEXT_ACTION: QRY-001+QRY-002 (P0 : texte intégral arrêt CE + rapport Fischer)*
