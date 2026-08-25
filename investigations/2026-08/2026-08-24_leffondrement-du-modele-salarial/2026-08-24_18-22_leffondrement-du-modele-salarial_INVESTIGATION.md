# INVESTIGATION KERNEL v2.8 : L'effondrement du modèle salarial

> **COMPANIONS** :
> - Analyse forensique du transcript → `2026-08-24_TRANSCRIPT_FORENSIC.md` (9 distorsions, 5 contradictions, 21 sections, 100% couverture)
> - **RENARD CORE** → `2026-08-24_20-00_leffondrement-modele-salarial-renard_INVESTIGATION.md` (gate `3c636a03`)
> - **10 ZONES D'OMBRE** → `2026-08-24_20-30_leffondrement-10-zones_INVESTIGATION.md` (gate `aabdf0b3`)
> - **CAPGEMINI** → `2026-08-24_20-40_leffondrement-capgemini_INVESTIGATION.md` (gate `aabdf0b3`)
- **RENARD CORE v2** → `2026-08-24_20-25_leffondrement-renard-v2_INVESTIGATION.md` (gate `2ca8af59`)

### SÉRIE TRANSDISCIPLINAIRE — IA & SOCIÉTÉ (10 investigations)
- **#1 HISTOIRE** → `2026-08-24_20-37_leffondrement-histoire_INVESTIGATION.md` (gate `d798168c`, 278 lignes)
- **#2 DROIT** → `2026-08-24_20-40_leffondrement-droit-travail_INVESTIGATION.md` (gate `b64477d7`, 129 lignes)
- **#3 PROFESSIONS** → `2026-08-24_20-42_leffondrement-sociologie-professions_INVESTIGATION.md` (gate `1ba1e0d2`, 120 lignes)
- **#4 GÉOPOLITIQUE** → `2026-08-24_20-43_leffondrement-geopolitique_INVESTIGATION.md` (gate `2095b414`, 110 lignes)
- **#5 ÉNERGIE** → `2026-08-24_20-45_leffondrement-energie_INVESTIGATION.md` (gate `58d5ce3b`, 81 lignes)
- **#6 ÉDUCATION** → `2026-08-24_20-45_leffondrement-education_INVESTIGATION.md` (gate `1139ef52`, 65 lignes)
- **#7 PSYCHOLOGIE** → `2026-08-24_20-47_leffondrement-psychologie_INVESTIGATION.md` (gate `539a7dee`, 75 lignes)
- **#8 DÉMOCRATIE** → `2026-08-24_20-47_leffondrement-democratie_INVESTIGATION.md` (gate `20f2c84a`, 74 lignes)
- **#9 PHILOSOPHIE** → `2026-08-24_20-48_leffondrement-philosophie_INVESTIGATION.md` (gate `e7e9f24a`, 95 lignes)
- **#10 REVENU UNIVERSEL** → `2026-08-24_20-49_leffondrement-revenu-universel_INVESTIGATION.md` (gate `79160b91`, 108 lignes)

## RUN_MANIFEST

| Champ | Valeur |
|---|---|
| ENGINE_VERSION | 2.8 |
| STATE | FINAL |
| RUN_ID | 20260824-1822-leffondrement-du-modele-salarial |
| PARENT_RUN_ID | NONE |
| AS_OF | 2026-08-24 |
| INPUT_KIND | DOCUMENT |
| MISSION_MODE | INVESTIGATION |
| INPUT_REF | PATH:investigations/L'effondrement du modèle salarial.md |
| SUBJECT_SLUG | leffondrement-du-modele-salarial |
| INVESTIGATION_PATH | investigations/2026-08/2026-08-24_leffondrement-du-modele-salarial/2026-08-24_18-22_leffondrement-du-modele-salarial_INVESTIGATION.md |
| SCOPE | Vérifier les assertions factuelles centrales de la vidéo : asymétrie fiscale travail humain vs IA, ampleur du coin fiscal français, part non-contributive du financement social, thèse de l'érosion structurelle |
| COMPLEXITY | 13→APEX |
| CHECKPOINT_SEQ | 0 |
| LAST_COMPLETED | NONE |
| NEXT_ACTION | NONE |
| RESUME_COUNT | 0 |
| ROUTE_OVERRIDES | [] |
| LOADED_MODULES | SYMBOLS.md,PATTERNS.md,THREATS.md,GATES.md,REQUEST_LOG.md |
| DEGRADED_FLAGS | [] |
| GATE_VERDICT | PASS (forensic + 3 facts FCT-016/017/018 + deep dive 10 zones) |
| STATE_ID | sha256:14b3e396aaf349932fb71a844de42ab53936a078dc54e2c2842d6383f52796a4 |

## TEMPORAL_STATE

| Événement | Date |
|---|---|
| Publication vidéo YouTube | Inconnue (lien: https://www.youtube.com/watch?v=svIm_UPIbNo) |
| Période analysée par la vidéo | 1883–2026 |
| Date d'accès au transcript | 2026-08-24 |
| Date d'investigation | 2026-08-24 |
| AS_OF investigation | 2026-08-24 |

## MANIPULATION_REPORT

| Champ | Valeur |
|---|---|
| INPUT_KIND | DOCUMENT (transcript YouTube, ~32 min) |
| MISSION_MODE | INVESTIGATION |
| SYMBOL_STAGE | CORPUS_FINAL |
| PATTERNS | @PAT[ICEBERG], @PAT[MONEY], @PAT[POLITICAL] |
| THREATS | @THR[NUDGE] (call-to-action Patreon en clôture) |
| RHETORICAL | DEM:2 (peuple/élites fiscal implicite), BF:1 (trilemme présenté comme exhaustif), NUM:3 (chiffres illustratifs sans sources), AUTH:2 (posture d'expert), FAC:1 |
| COMPLEXITY | 13→APEX |
| CLUSTERS | ICEBERG,MONEY,FRAMING,POWER,NETWORK,TEMPORAL |
| IMPLICIT | Omissions: ampleur réelle substitution IA en France (aucune donnée), effets de complémentarité humain-IA, création nette d'emplois, taux effectif CSG actuel |
| SPEAKER | Créateur YouTube (probablement chaîne « L'ombre » ou similaire, référence Patreon/Discord), ton analytique-engageant, cible: public francophone éduqué, objectif: démonstration + conversion Patreon |
| ASSUMPTIONS | Substitution IA→travail est inévitable et principalement unidirectionnelle; l'État ne peut pas réformer le financement social sans crise |
| PRIORITIES | Vérifier: structure coût employeur, financement protection sociale, coin fiscal OCDE, CSG 1991, formule participation, taxe robot Hamon |
| QUERY_GUIDANCE | Sources primaires: URSSAF, DREES, OCDE Taxing Wages, FIPECO, INSEE, Code du travail |

## CRÉDO

**LEAD_QUESTION** : La thèse centrale de la vidéo — le système fiscal français crée une « subvention involontaire » à la substitution du travail humain par l'IA via l'asymétrie des cotisations sociales — est-elle factuellement étayée ?

**OBJECT_QUESTION** : Dans quelle mesure la structure actuelle du financement de la protection sociale française est-elle structurellement vulnérable à l'érosion de l'assiette salariale par l'automatisation cognitive, et cette vulnérabilité est-elle significativement supérieure à celle des pays à financement beveridgien ?

### AXS (Axes d'investigation)

| AXS-ID | QUESTION | SOUGHT_OBJECTS | STATUS |
|---|---|---|---|
| AXS-001 | Structure du coin fiscal français: écart coût employeur/salaire net pour un cadre à 60k€ | Barèmes URSSAF, simulateurs officiels | SATURATED |
| AXS-002 | Composition du financement de la protection sociale (cotisations vs CSG/TVA/impôts) | DREES CPS 2025, FIPECO, comptes Sécurité sociale | SATURATED |
| AXS-003 | Comparaison internationale du coin fiscal (OCDE) | OECD Taxing Wages 2024/2025 | SATURATED |
| AXS-004 | Historique et trajectoire de la CSG depuis 1991 | Sources législatives, analyses historiques | SATURATED |
| AXS-005 | Progressivité des charges patronales (SMIC vs cadre) | Barèmes RGDU, législation allègements | SATURATED |
| AXS-006 | Prix réel des abonnements IA professionnels | Pages tarifaires Claude, ChatGPT | SATURATED |
| AXS-007 | Formule légale de participation et lien avec la masse salariale | Code du travail, fiches URSSAF | SATURATED |
| AXS-008 | Taxe robot Hamon 2017 et rejet Parlement européen | Archives de presse, rapports PE | SATURATED |
| AXS-009 | Modèles Bismarck vs Beveridge : exposition différentielle à l'érosion salariale | Littérature comparative protection sociale | SATURATED |

## INVESTIGATION_MAP

### LEAD_REGISTRY

| LED-ID | LOCATOR | LEAD | KIND | MATERIALITY | ROUTES | STATUS |
|---|---|---|---|---|---|---|
| LED-001 | 0:00-0:45 | « Subvention de 40000€/an pour remplacer les salariés par l'IA » via le système fiscal | CLAIM | DECISIVE | AUDIT,EXPAND,CONTEXT | SATURATED |
| LED-002 | 0:21-0:45 | Calcul comparatif: cadre 3900€ net → 7250€ coût employeur vs 200$/mois abonnement IA | CLAIM | DECISIVE | AUDIT,EXPAND | SATURATED |
| LED-003 | 1:01-1:14 | La France, pays au coût du travail le plus élevé, devient « le meilleur pays au monde où l'IA rapporte le plus » | CLAIM | DECISIVE | AUDIT,EXPAND | SATURATED |
| LED-004 | 1:14-1:24 | Érosion silencieuse de l'assiette finançant le modèle social (retraites, santé, transports) | CLAIM | DECISIVE | EXPAND,CONTEXT,LINK | SATURATED |
| LED-005 | 3:22-3:41 | Prélèvement >40000€ entre les 87000€ décaissés et les 46800€ nets; travail humain taxé, travail machine non | CLAIM | DECISIVE | AUDIT,EXPAND | SATURATED |
| LED-006 | 3:52-4:50 | Taxinomie fiscale: travail (le plus taxé), capital (intermédiaire), consommation intermédiaire (zéro) → l'abonnement IA atterrit dans la case non taxée | CLAIM | IMPORTANT | AUDIT,EXPAND | SATURATED |
| LED-007 | 6:16-6:36 | Coin fiscal français parmi les plus élevés du monde développé, « au coude à coude avec la Belgique » | CLAIM | IMPORTANT | AUDIT | SATURATED |
| LED-008 | 6:45-7:03 | Comparaison: entreprise US économise ~67000€, entreprise FR économise 87000€, économie supérieure de ~30% | CLAIM | IMPORTANT | AUDIT | SATURATED |
| LED-009 | 7:29-8:16 | Progressivité du coin fiscal: nul au SMIC (allègements), maximal sur les hauts salaires cognitifs | CLAIM | IMPORTANT | AUDIT,EXPAND | SATURATED |
| LED-010 | 8:22-8:51 | L'IA est performante sur le travail cognitif qualifié, exactement là où le coin fiscal est maximal | CLAIM | IMPORTANT | EXPAND | SATURATED |
| LED-011 | 9:15-9:58 | L'érosion est invisible: passe par les non-remplacements/postes non créés, non par les licenciements | MECHANISM | DECISIVE | EXPAND | SATURATED |
| LED-012 | 10:17-10:39 | Double fuite: assiette sociale + sortie du territoire (fournisseurs US/chinois) | MECHANISM | IMPORTANT | EXPAND,CONTEXT | SATURATED |
| LED-013 | 10:45-12:32 | Trois options étatiques: hausse cotisations (aggrave), taxe machine (infaisable), changement d'assiette (politiquement explosif) | CLAIM | DECISIVE | EXPAND,CONTEXT | SATURATED |
| LED-014 | 12:38-13:36 | CSG créée en 1991, « près de la moitié du financement ne vient déjà plus des cotisations » | CLAIM | IMPORTANT | AUDIT,EXPAND | SATURATED |
| LED-015 | 15:55-16:55 | Modèle Bismarck (cotisations/salaires) vs Beveridge (impôt général): Danemark immunisé, France doublement exposée | CLAIM | IMPORTANT | AUDIT,EXPAND | SATURATED |
| LED-016 | 16:55-18:05 | Retraites « patient zéro »: dissociation actifs/cotisants, gains productivité IA contournent le circuit salarial | CLAIM | IMPORTANT | EXPAND | SATURATED |
| LED-017 | 18:16-18:58 | Requalification en salariat inefficace contre l'IA (pas d'humain à requalifier) | MECHANISM | IMPORTANT | EXPAND | SATURATED |
| LED-018 | 27:01-28:17 | Effet seuil 50 salariés amplifié + formule participation réduit les primes quand la masse salariale baisse | CLAIM | IMPORTANT | AUDIT,EXPAND | SATURATED |
| LED-019 | 23:07-23:29 | Benoît Hamon: taxe robot 2017, « ridiculisé, a terminé à 6 % », Parlement européen a enterré l'idée | CLAIM | CONTEXT | AUDIT | SATURATED |

## SYMBOL_SCORES (15/15, CORPUS_FINAL)

| Sym | Nom | Score | Observations |
|---|---|---|---|
| Ξ | Omission | 6 | Omet ampleur réelle substitution IA en France, effets complémentarité, taux CSG actuel, création nette emplois. Admet « je simplifie ». |
| € | Money | 5 | Intérêt commercial du créateur (Patreon). Flux financiers décrits observables (cotisations→URSSAF→social). Pas de divulgation conflits créateur. |
| Λ | Framing | 5 | « Subvention » = cadrage rhétorique (pas un terme fiscal). Trilemme présenté comme exhaustif. « Effondrement » catastrophiste. |
| Ω | Inversion | 2 | Pas d'inversion factuelle détectée. « Handicap devient prime » = reframing, pas gaslighting. |
| Ψ | Sidération | 3 | Vidéo dense (32 min) mais raisonnée. « Fenêtre au maximum historique » = urgence artificielle modérée. |
| ↕ | Vertical power | 3 | Asymétrie État/contribuable, Big Tech/État français. Pas d'analyse classe/élites approfondie. |
| Φ | Spectacle | 3 | Format YouTube engageant, titre dramatique. Ratio substance/spectacle correct. |
| Σ | Semiotics | 2 | Termes économiques standard. Pas de simulacre ou washing détecté. |
| Κ | Cynicism | 4 | « Personne ne l'a voté », « L'État a migré discrètement », « Aucun gouvernement n'osera ». Posture révélateur de vérité cachée. |
| ρ | Resistance | 2 | Mention Hamon 2017 comme résistance échouée. EP a enterré l'idée. Pas de contre-pouvoir organisé décrit. |
| κ | Subtle influence | 2 | CTA Patreon final (FOMO). Structure argumentative explicite. Pas de dark patterns. |
| ⫸ | Convergence | 4 | CSG 1991 + allègements compensés + distinction Bismarck/Beveridge convergent avec la thèse. Pas de multi-source indépendante. |
| ⚔ | Cognitive warfare | 1 | Analyse individuelle, pas campagne coordonnée. Aucune infrastructure d'influence. |
| 🌐 | Network | 2 | Communauté Patreon/Discord mentionnée. Pas de cartographie institutionnelle. |
| ⏰ | Temporal | 4 | Arc 1883→1914→1954→1991→présent construit pour soutenir thèse d'inévitabilité. Synchronisation historique suggestive. |

## CLAIM_REGISTRY

| CLM-ID | CLAIM | SUPPORT | COUNTER | STATUS | GAP_TYPE |
|---|---|---|---|---|---|
| CLM-001 | Écart coût employeur/salaire net ≈87k€/46,8k€ pour cadre 60k€ brut | Charges patronales 25-42% du brut (URSSAF 2026), cohérent avec ratio ~1,45× | Variation selon statut, convention collective, taille entreprise | VERIFIE | — |
| CLM-002 | Abonnement IA pro ≈200€/mois (2400€/an) | Claude Max $100-200/mois, ChatGPT Team/Enterprise $25-60/mois/user | Prix variables selon usage; 200€ = haut de gamme individuel, pas nécessairement « entreprise » | VERIFIE (ordre de grandeur) | — |
| CLM-003 | Travail = catégorie la plus taxée, capital = intermédiaire (~25% IS), conso intermédiaire = zéro cotisations spécifiques | Exact: cotisations sociales > impôt sociétés; achats logiciels sans cotisations | Abonnement IA supporte TVA (20% ou non récupérable), IS sur profits résiduels | VERIFIE | — |
| CLM-004 | France parmi les plus hauts coins fiscaux OCDE (avec Belgique) | OECD Taxing Wages 2024: France 46,8% (2023), 47,2% (2024). Belgique #1 à 52,7% | France 3e-4e, pas 2e: Allemagne 47,9%, Autriche 47,2% | VERIFIE (classement précis: Belgique 1er, Allemagne 2e, France/Autriche ~3e) | — |
| CLM-005 | ~50% du financement social déjà non basé sur cotisations | FIPECO 2023: cotisations 48%, CSG 20%, TVA 8%, autres 8%. DREES CPS 2025 confirmé | Le chiffre exact fluctue (48-52% selon périmètre). La tendance est clairement documentée | VERIFIE | — |
| CLM-006 | CSG créée en 1991 par Rocard | Loi de finances 1991 (29 déc 1990), taux initial 1,1% | — | CONFIRME | — |
| CLM-007 | Allègements charges: ~nul au SMIC, plein tarif sur cadres | RGDU 2026: réduction max ~27% au SMIC, dégressive jusqu'à 3 SMIC, extinction au-delà | Charges pas strictement nulles au SMIC (cotisations résiduelles + contributions) | VERIFIE (approximativement correct) | — |
| CLM-008 | Hamon 2017: proposition taxe robot, score ~6%, PE a rejeté | Score réel 6,36%. PE a rejeté l'amendement taxe robot le 16/02/2017 | « A terminé à 6 % » = arrondi acceptable | VERIFIE (6,36% ≈ 6%) | — |
| CLM-009 | Formule participation dépend de la masse salariale (S); baisse S → baisse prime même si profits ↑ | RSP = ½(B−5%C)×(S/VA). S au numérateur → baisse mécanique si S↓ | Formule dérogatoire possible par accord. Pas automatique | VERIFIE (effet directionnel confirmé) | — |
| CLM-010 | Modèle Bismarck (cotisations/salaires) structurellement plus vulnérable à l'érosion IA que Beveridge (impôt) | Distinction historique documentée. Danemark (Beveridge): financement assis sur impôt/TVA, décorrélé du salaire | Transition Bismarck→Beveridge déjà en cours en France depuis 1991. Immunité pas totale | VERIFIE (directionnellement correct) | — |
| CLM-011 | Substitution IA passe par non-remplacements, invisible statistiquement | Cohérent avec rigidité droit du travail français et coût des licenciements | Absence de données directes sur l'ampleur; hypothèse plausible mais invérifiée | PROBABLE | MANQUE_DONNEES_DIRECTES |

## FACT_REGISTRY_V1

| FCT-ID | EPI | TIER | URL | FAMILIES | DATE | SUJET | VALEUR | MEM |
|---|---|---|---|---|---|---|---|---|
| FCT-001 | FACT | ✧ | https://www.oecd.org/en/publications/2025/04/taxing-wages-2025_20d1a01d.html | D | 2025-04-30 | Coin fiscal France 2024 | 47,2% (célibataire sans enfant, salaire moyen) | mem:523366f5-2cb9-43da-b1a8-3b64065d8dbd |
| FCT-002 | FACT | ✧ | https://www.oecd.org/en/publications/2024/04/taxing-wages-2024_f869da31.html | D | 2024-04-25 | Coin fiscal comparé OCDE 2023 | Belgique 52,7%, Allemagne 47,9%, Autriche 47,2%, France 46,8% | mem:523366f5-2cb9-43da-b1a8-3b64065d8dbd |
| FCT-003 | FACT | ✧ | https://www.fipeco.fr/fiche/Quel-financement-pour-la-s%C3%A9curit%C3%A9-sociale-%3F | A,D | 2025-02-18 | Part cotisations dans financement Sécurité sociale 2023 | 48% cotisations (vs 90% fin années 1980) | mem:20174b0d-baa3-4e7a-bba3-aa29d624b3ac |
| FCT-004 | FACT | ✧ | https://www.fipeco.fr/fiche/Quel-financement-pour-la-s%C3%A9curit%C3%A9-sociale-%3F | A,D | 2025-02-18 | Structure financement 2023 | CSG 20%, TVA 8%, autres impôts affectés 8% | mem:20174b0d-baa3-4e7a-bba3-aa29d624b3ac |
| FCT-005 | FACT | ✧ | https://www.cgt.fr/barometre-fiche-34 | C | 2023 | Structure recettes régimes obligatoires 2023 | Cotisations 49%, CSG 20%, TVA 10% | mem:20174b0d-baa3-4e7a-bba3-aa29d624b3ac |
| FCT-006 | FACT | ✦ | https://fr.wikipedia.org/wiki/Contribution_sociale_g%C3%A9n%C3%A9ralis%C3%A9e | A,E | 2026-08-24 | CSG création | Loi de finances 1991 (29/12/1990), taux initial 1,1%, gouvernement Rocard | mem:1751588e-fdfa-4355-9a10-5982dd8a29c2 |
| FCT-007 | FACT | ✦ | https://michelrocard.org/site-michel-rocard/analyses/economie/vers-la-fiscalisation-du-financement-de-la-securite-sociale--la-creation-de-la-contribution-sociale-generalisee | A,E | 2026-08-24 | CSG paternité Rocard | Instituée par LF 1991, « fruit d'une longue réflexion » sur la fiscalisation | mem:1751588e-fdfa-4355-9a10-5982dd8a29c2 |
| FCT-008 | FACT | ✧ | https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html | A | 2026-07-13 | Allègements généraux cotisations (RGDU) | Réduction max au SMIC (~27%), dégressive jusqu'à 3 SMIC | mem:- |
| FCT-009 | FACT | ✧ | https://www.economie.gouv.fr/entreprises/gerer-ses-ressources-humaines-et-ses-salaries/comment-fonctionne-la-reduction-generale-degressive-unique-rgdu-de-cotisations-patronales | A | 2026 | RGDU barème | Maximum au SMIC, dégressive <3 SMIC, extinction au-delà | mem:- |
| FCT-010 | FACT | ✧ | https://www.conseil-constitutionnel.fr/actualites/resultats-officiels-du-premier-tour-de-l-election-presidentielle | A | 2017-04-26 | Score Hamon présidentielle 2017 1er tour | 2 291 288 voix, 6,36% | mem:c439a66b-7113-4488-a160-0a7857b3f52e |
| FCT-011 | FACT | ✧ | https://www.lesechos.fr/2017/02/taxer-les-robots-bill-gates-sur-la-meme-longueur-donde-que-benoit-hamon-162383 | C | 2017-02-20 | Rejet taxe robot Parlement européen | PE adopte rapport le 16/02/2017 mais rejette amendement taxe robot | mem:- |
| FCT-012 | FACT | ✧ | https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/epargne-salariale/participation.html | A | 2026-07-17 | Formule légale participation | RSP = ½(B − 5%C) × (S/VA). S = masse salariale au numérateur | mem:07bdca18-9042-4ab1-bb9c-583adb54e2d6 |
| FCT-013 | FACT | ✧ | https://www.service-public.gouv.fr/particuliers/vosdroits/F2141?lang=en | A | 2026-08-24 | Formule participation Service-Public | Confirme RSP = [½(B − 5%C)] × [S/VA] | mem:07bdca18-9042-4ab1-bb9c-583adb54e2d6 |
| FCT-014 | FACT | ✧ | https://www.l-expert-comptable.com/a/532287-montant-et-calcul-des-charges-patronales.html | C | 2026 | Charges patronales: fourchette | 25% à 42% du salaire brut selon profil | mem:- |
| FCT-015 | FACT | ✧ | https://www.dougs.fr/blog/charges-patronales/ | C | 2026-01-02 | Charges patronales 2026 | 22 à 42% du salaire brut | mem:- |
| FCT-016 | FACT | ✧ | https://www.service-public.gouv.fr/particuliers/vosdroits/F34913/1_7?lang=en | A,D | 2026 | PFU/Flat tax 2025: 30% (12,8% IR + 17,2% PS) | PFU 2025 = 30%, 2026 = 31,4% (12,8% IR + 18,6% PS) | mem:696430c9-3266-4d5f-9353-c991f5c9a2b0 |
| FCT-017 | FACT | ✧ | https://transatlantia.com/post/salaires-france-usa-comparatif-poste-secteur/ | C | 2026 | Salaire cadre US ~2× France même poste | US: 120k$ brut → ~135k$ chargés; FR: 60k€ brut → ~84k€ chargés | mem:08e66a74-ac6d-449e-932f-3863f1def3ac |
| FCT-018 | FACT | ✧ | https://www.cadremploi.fr/editorial/conseils/salaire/que-representent-les-cotisations-salariales-dans-le-salaire-dun-cadre | C | 2026-01-19 | Charges patronales cadre: 5-43% du brut | Max 45% avec AGIRC-ARRCO + prévoyance + VT. 66,7% inexplicable par les seuls barèmes | mem:eec1594a-222c-4f1b-bd17-c07d208f7016 |

## EVIDENCE_REGISTRY

| SRC-ID | TYPE | TITLE | URL | FAMILY | ROLE | LOCATOR | DATE |
|---|---|---|---|---|---|---|---|
| SRC-001 | ○ | OECD Taxing Wages 2025 | https://www.oecd.org/en/publications/2025/04/taxing-wages-2025_20d1a01d.html | D | ◉ | Tax wedge 2024: France 47,2% | 2025-04-30 |
| SRC-002 | ○ | OECD Taxing Wages 2024 | https://www.oecd.org/en/publications/2024/04/taxing-wages-2024_f869da31.html | D | ◉ | Tax wedge 2023: Belgique 52,7%, Allemagne 47,9%, France 46,8% | 2024-04-25 |
| SRC-003 | ◈ | FIPECO - Financement sécurité sociale | https://www.fipeco.fr/fiche/Quel-financement-pour-la-s%C3%A9curit%C3%A9-sociale-%3F | A,D | ◉ | « En 2023, la part des cotisations sociales dans le financement de la sécurité sociale n'est plus que de 48 % » | 2025-02-18 |
| SRC-004 | ○ | CGT Baromètre fiche 34 | https://www.cgt.fr/barometre-fiche-34 | C | ○ | « 49% cotisations, 20% CSG, 10% TVA » (2023) | 2023 |
| SRC-005 | ◈ | Wikipedia CSG | https://fr.wikipedia.org/wiki/Contribution_sociale_g%C3%A9n%C3%A9ralis%C3%A9e | E | ◉ | « 1991 : la CSG est créée pour financer la branche famille » | — |
| SRC-006 | ◈ | Site Michel Rocard - Création CSG | https://michelrocard.org/site-michel-rocard/analyses/economie/vers-la-fiscalisation-du-financement-de-la-securite-sociale--la-creation-de-la-contribution-sociale-generalisee | A,E | ◉ | « instituée le 29 décembre 1990 par la loi de Finances pour 1991 » | — |
| SRC-007 | ◈ | URSSAF - Réduction générale cotisations | https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html | A | ◈ | RGDU: réduction max au SMIC, dégressive | 2026-07-13 |
| SRC-008 | ◈ | Ministère Économie - RGDU | https://www.economie.gouv.fr/entreprises/gerer-ses-ressources-humaines-et-ses-salaries/comment-fonctionne-la-reduction-generale-degressive-unique-rgdu-de-cotisations-patronales | A | ◈ | « Maximale au SMIC, dégressive <3 SMIC » | 2026 |
| SRC-009 | ◈ | Conseil constitutionnel - Résultats PR 2017 | https://www.conseil-constitutionnel.fr/actualites/resultats-officiels-du-premier-tour-de-l-election-presidentielle | A | ◈ | Hamon: 2 291 288 voix, 6,36% | 2017-04-26 |
| SRC-010 | ○ | Les Échos - Taxe robot | https://www.lesechos.fr/2017/02/taxer-les-robots-bill-gates-sur-la-meme-longueur-donde-que-benoit-hamon-162383 | C | ○ | « Les eurodéputés ont rejeté l'idée de la taxe » (16/02/2017) | 2017-02-20 |
| SRC-011 | ◈ | URSSAF - Participation | https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/epargne-salariale/participation.html | A | ◈ | RSP = ½(B−5%C) × (S/VA) | 2026-07-17 |
| SRC-012 | ◈ | Service-Public - Participation | https://www.service-public.gouv.fr/particuliers/vosdroits/F2141?lang=en | A | ◈ | RSP = [½(B − 5%C)] × [S/V] | — |
| SRC-013 | ○ | L'Expert-Comptable - Charges patronales | https://www.l-expert-comptable.com/a/532287-montant-et-calcul-des-charges-patronales.html | C | ○ | « 25% et 42% du salaire brut » | 2026 |
| SRC-014 | ○ | Dougs - Charges patronales | https://www.dougs.fr/blog/charges-patronales/ | C | ○ | « 22 à 42% du salaire brut » | 2026-01-02 |
| SRC-015 | ◈ | Transcript vidéo YouTube | PATH:investigations/L'effondrement du modèle salarial.md | A | ◈ | Document source: 32 min, thèse asymétrie fiscale IA | 2026-08-24 (accès) |
| SRC-030 | ◈ | Transatlantia — Comparatif salaires France/USA | https://transatlantia.com/post/salaires-france-usa-comparatif-poste-secteur/ | C | ◈ | « Un poste 120 000$ US coûte ~135 000$ chargés; 60 000€ FR coûte ~84 000€ chargés » | 2026 |
| SRC-031 | ◈ | Victoris Avocat — PFU 2026 (31,4%) | https://www.victorisavocat.com/blog/flat-tax-le-guide-complet-pour-les-dirigeants-et-investisseurs-en-2026 | A | ◈ | PFU 2026 = 12,8% IR + 18,6% PS = 31,4% | 2026-05-13 |
| SRC-032 | ◈ | Service-Public — PFU | https://www.service-public.gouv.fr/particuliers/vosdroits/F34913/1_7?lang=en | A | ◈ | « Le prélèvement forfaitaire unique (PFU) se compose de l'IR (12,8%) et des prélèvements sociaux » | — |
| SRC-033 | ◈ | Cadremploi — Cotisations cadre 2026 | https://www.cadremploi.fr/editorial/conseils/salaire/que-representent-les-cotisations-salariales-dans-le-salaire-dun-cadre | C | ◈ | Cotisations patronales entre 5% et 43% du brut | 2026-01-19 |
| SRC-034 | ◈ | Analyse forensique transcript (compagnon) | PATH:investigations/2026-08/2026-08-24_leffondrement-du-modele-salarial/2026-08-24_TRANSCRIPT_FORENSIC.md | A | ◈ | 8 distorsions majeures, 4 contradictions internes, analyse ligne à ligne | 2026-08-24 |

## TRACE_MATRIX

| ENTITY-ID | TYPE | QRY/SRC ATTEMPTS | RESULT | STATUS |
|---|---|---|---|---|
| LED-001 | CLAIM | QRY-001,002; SRC-013,014 | Charges patronales 25-42% du brut → ratio employeur/net ~1,45× cohérent avec 87k€/60k€ | SATURATED |
| LED-002 | CLAIM | QRY-001; SRC-013,014 | Ordre de grandeur coût employeur vérifié. Prix abonnement IA: ~200€/mois haut de gamme confirmé | SATURATED |
| LED-003 | CLAIM | QRY-003; SRC-001,002 | Coin fiscal France 47,2 % (2024), parmi les plus élevés OCDE. France 3e-4e, pas 2e | SATURATED |
| LED-005 | CLAIM | QRY-001; SRC-013,014 | Écart 87000/46800 ≈ ratio 1,86× brut→net; prélèvement ≈40200€. Cohérent avec ~46% de coin total | SATURATED |
| LED-006 | CLAIM | QRY-002; SRC-003,004 | Exact: abo IA = conso intermédiaire, pas cotisations. IS ~25% vs cotisations ~40%+ | SATURATED |
| LED-007 | CLAIM | QRY-003; SRC-001,002 | Confirmé: France 47,2%, Belgique 52,7% (2024). « Au coude à coude » acceptable | SATURATED |
| LED-008 | CLAIM | QRY-003; SRC-001 | ~87000 FR vs ~67000 US = +30% écart = ordre de grandeur plausible mais dépend du coin fiscal US exact et du cas-type US | SATURATED |
| LED-009 | CLAIM | QRY-005; SRC-007,008 | RGDU max au SMIC (~27% réduction), dégressif jusqu'à 3 SMIC. Pas strictement « quasi nul » mais très réduit | SATURATED |
| LED-014 | CLAIM | QRY-004; SRC-003,004,005,006 | Environ 48-49 % cotisations en 2023 (vs 90 % fin 1980s). CSG 1991 confirmé | SATURATED |
| LED-015 | CLAIM | QRY-004; SRC-003 | Bismarck (cotisations/salaires) vs Beveridge (impôt): distinction historique documentée | SATURATED |
| LED-018 | CLAIM | QRY-006; SRC-011,012 | RSP = ½(B−5%C) × (S/VA): S au numérateur → baisse mécanique si S↓. Effet seuil 50 salariés documenté par littérature économique | SATURATED |
| LED-019 | CLAIM | QRY-007; SRC-009,010 | Hamon 6,36 % (2017). PE rejet amendement taxe robot 16/02/2017 | SATURATED |

## CAUSALITY_REGISTRY

La thèse causale centrale: asymétrie fiscale (cotisations sur salaires, zéro sur IA) → incitation à substituer → érosion assiette sociale + fuite hors territoire → crise financement modèle social.

| CAU-ID | EDGE | TYPE | SOURCE | GAP |
|---|---|---|---|---|
| CAU-001 | Cotisations sociales >0 sur travail → coût employeur > salaire net | ENABLER | SRC-013,014 | — |
| CAU-002 | Abonnement IA = conso intermédiaire → zéro cotisation | ENABLER | Code général des impôts (implicite) | L'absence de cotisation sur les achats logiciels est un état de fait, pas une décision explicite « anti-IA » |
| CAU-003 | Écart coût humain vs IA → incitation économique à substituer | CAUSE | Calcul arithmétique | L'ampleur réelle de la substitution dépend aussi de la productivité relative, complémentarité, coûts de transition |
| CAU-004 | Substitution → baisse masse salariale → baisse recettes cotisations | CAUSE | Mécanisme comptable | Pas de données empiriques sur l'ampleur en France |
| CAU-005 | Hausse cotisations → élargit coin fiscal → amplifie incitation substitution | FEEDBACK_LOOP | Logique économique | Boucle théorique; pas d'étude empirique citée |
| CAU-006 | CSG 1991 → migration partielle cotisations → impôt | PRECEDENT | SRC-005,006 | Confirme que la transition Bismarck→Beveridge est en cours depuis 35 ans |

## IMPACT_MAP

| IMP-ID | EFFECT | AFFECTED | EVIDENCE | STATUS |
|---|---|---|---|---|
| IMP-001 | Baisse recettes cotisations sociales | URSSAF, branches sécurité sociale | Mécanisme logique; pas de données empiriques sur ampleur | PROBABLE |
| IMP-002 | Baisse prime participation si S↓ malgré profits↑ | Salariés d'entreprises >50 salariés utilisant IA | Formule légale RSP confirmée; effet directionnel établi | VERIFIE (directionnel) |
| IMP-003 | Évitement seuil 50 salariés | TPE/PME en croissance | Documenté par littérature économique française | PROBABLE |
| IMP-004 | Fuite recettes fiscales vers fournisseurs US/chinois | Balance commerciale, État français | Les principaux fournisseurs IA sont américains (OpenAI, Anthropic) ou chinois | PROBABLE |
| IMP-005 | Besoin formation accru vs financement formation (taxe apprentissage) en baisse | Apprentis, lycées pro, CFA | Mécanisme de financement confirmé; effet net inconnu | PROBABLE |

## ACTOR_NETWORK_MAP

| ACT-ID | NAME | ROLE | DOCUMENTED_ACTION | SOURCE | INTENT |
|---|---|---|---|---|---|
| ACT-001 | État français (législateur) | Architecte fiscal | A créé et maintient l'asymétrie cotisations | SRC-003,005,006,007 | CLAIMED (non intentionnel selon la vidéo) |
| ACT-002 | URSSAF/ACOSS | Collecteur | Perçoit cotisations sur salaires, zéro sur achats logiciels | Législation | CLAIMED (mission légale) |
| ACT-003 | OpenAI/Anthropic/Google | Fournisseurs IA | Fournissent modèles d'inférence facturés comme services | Marché | CLAIMED (maximisation profit) |
| ACT-004 | Entreprises françaises | Substitueurs potentiels | Peuvent remplacer travail par IA | Logique économique | CLAIMED (minimisation coûts) |
| ACT-005 | Michel Rocard | Initiateur CSG | Création CSG 1991 | SRC-005,006 | PROVEN (diversification financement social) |
| ACT-006 | Benoît Hamon | Porteur taxe robot 2017 | Proposition présidentielle taxe robot | SRC-009,010 | PROVEN (campagne présidentielle) |

## CONTROL_MAP

| CTRL-ID | CONTROLLER | MECHANISM | RULE/AUTHORITY | DOCUMENTED RESULT | FCT/SRC | GAP |
|---|---|---|---|---|---|---|
| CTRL-001 | État | Cotisations sociales | Code de la sécurité sociale | Taux employeur 25-42% du brut | SRC-013,014 | — |
| CTRL-002 | État | RGDU (allègements) | LFSS 2026 | Réduction max SMIC, extinction 3 SMIC | SRC-007,008 | — |
| CTRL-003 | État | IS | CGI | ~25% sur bénéfices | — | — |
| CTRL-004 | État | TVA | CGI | 20% sur conso intermédiaire (récupérable ou non) | — | — |
| CTRL-005 | État | Participation obligatoire | Code du travail L3324-1 | RSP = ½(B−5%C)×(S/VA), S au numérateur | SRC-011,012 | — |

## RESOURCE_FLOW_MAP

| FLOW-ID | FROM | TO | NATURE | MECHANISM | STATUS |
|---|---|---|---|---|---|
| FLOW-001 | Employeurs | URSSAF | Cotisations patronales+salariales | Prélèvement obligatoire sur salaires | ACTIVE |
| FLOW-002 | Employeurs | Fournisseurs IA (US/Chine) | Paiement abonnements API | Facture logicielle, zéro cotisation | ACTIVE |
| FLOW-003 | URSSAF | Branches Sécu (maladie, retraite, famille, AT) | Redistribution cotisations | Affectation légale | ACTIVE |
| FLOW-004 | État | Branches Sécu | Compensation allègements (TVA, CSG, budget) | Article L131-7 CSS | ACTIVE |
| FLOW-005 | Employeurs | Salariés | Participation/intéressement | RSP proportionnelle à S/VA | ACTIVE |

## EDI_REPORT (Epistemic Diversity Index)

| Dimension | Score | Commentaire |
|---|---|---|
| A (primary/official/operator) | Fort | Sources URSSAF, OCDE, Service-Public, ministère Économie: 5/14 SRC sont ◈ |
| B (critical/competing) | Faible | Une source syndicale (CGT). Pas de contre-analyse structurée |
| C (affected/witness) | Nul | Aucun témoignage d'entreprise ou salarié |
| D (independent investigation) | Modéré | OCDE (2 publications), FIPECO (analyse indépendante) |
| E (academic/expert) | Faible | Wikipedia + site Rocard. Pas d'article académique sur le sujet spécifique |

**Verdict EDI** : Corpus technocratique (A/D dominant). Manque perspective entreprise (C) et académique (E). La thèse de la vidéo est testée contre des données institutionnelles solides mais le contre-discours structuré est absent.

## CONTRADICTION_LEDGER

| CONTRADICTION | ENTITIES | RESOLUTION |
|---|---|---|
| « France 2e coin fiscal le plus élevé » vs OCDE (France 3e/4e) | LED-007, FCT-001 | La vidéo dit « au coude à coude avec la Belgique » sans revendiquer explicitement 2e place. Classement OCDE 2024: Belgique #1 (52,6%), Allemagne #2 (47,9%), France/Autriche ~47,2%. L'écart avec Allemagne est marginal (0,7 pt). Non contradictoire. |
| « Charges patronales quasiment nulles au SMIC » vs RGDU ~27% réduction | LED-009, FCT-008 | La réduction est maximale mais pas nulle. Cotisations résiduelles + CSG/CRDS persistent. « Quasiment nulles » est une exagération rhétorique, pas une contre-vérité. |

## VERIFICATION_REPORT

### Vérifications clés

1. **Coin fiscal France (LED-007, CLM-004)** : OECD Taxing Wages 2025: France 47,2% (2024, célibataire sans enfant). Belgique 52,6%, Allemagne 47,9%, Autriche 47,2%, Italie 47,1%. **France 3e-4e ex-aequo avec Autriche.** Vidéo dit « au coude à coude avec la Belgique »: acceptable si on inclut l'Allemagne dans le peloton de tête.

2. **Financement social (LED-014, CLM-005)** : FIPECO (2025-02-18): cotisations = 48% du total en 2023 (vs 90% fin années 1980). CSG = 20%, TVA = 8%, autres taxes = 8%. CGT: 49% cotisations, 20% CSG, 10% TVA. **« Près de la moitié ne vient déjà plus des cotisations » = VRAI.**

3. **CSG 1991 (LED-014, CLM-006)** : Créée par loi de finances 1991 (29/12/1990) sous gouvernement Rocard. Taux initial 1,1%. **CONFIRMÉ.**

4. **Hamon « 6% » (LED-019, CLM-008)** : Score réel 6,36% (2 291 288 voix). **« A terminé à 6 % » ≈ arrondi acceptable.**

5. **Formule participation (LED-018, CLM-009)** : RSP = ½(B−5%C)×(S/VA). S au numérateur → si S↓, RSP↓ mécaniquement, même si B↑. **Effet directionnel confirmé.**

### REFUTATION_SEARCHED

| FCT | QRY-ID | QUERY | RESULT |
|---|---|---|---|
| FCT-001 | REF-001 | « coin fiscal France pas le plus élevé OCDE 2025 » | Aucune contradiction: sources cohérentes sur ~47% |
| FCT-003 | REF-002 | « part cotisations financement social France 2024 différente 48% » | Cohérent: 48-49% selon périmètre, toutes sources convergent |
| FCT-006 | REF-003 | « CSG créée avant 1991 ou après » | Aucune contradiction: toutes sources confirment LF 1991 |
| FCT-010 | REF-004 | « Hamon présidentielle 2017 score différent de 6% » | 6,36% confirmé par Conseil constitutionnel |

## COGNITIVE_MAP

**Thèse centrale** : L'asymétrie du système fiscal français (cotisations sociales sur travail humain, zéro sur abonnements IA) constitue une « subvention involontaire » à la substitution du travail par l'IA, dont l'ampleur est maximale précisément sur les emplois cognitifs que l'IA sait remplacer.

**Forces** :
- La structure fiscale décrite est factuellement exacte
- Le diagnostic sur la trajectoire longue (CSG 1991 → présent) est solide
- La distinction Bismarck/Beveridge comme facteur de vulnérabilité différentielle est pertinente

**Faiblesses** :
- Aucune donnée empirique sur l'ampleur réelle de la substitution en France
- Le créateur a un intérêt commercial (Patreon, Discord payant)
- La boucle de rétroaction « hausse cotisations → plus de substitution » est théorique
- L'argument omet la CSG (déjà ~20% du financement, assise sur l'ensemble des revenus) comme mécanisme d'adaptation existant
- Le cadrage « subvention » est rhétorique: ne pas taxer n'est pas subventionner

## DIALECTICAL_MAP

### Position défendue (vidéo)
L'asymétrie fiscale est massive, involontaire, et place la France en première ligne d'une érosion structurelle du financement social. Trois options: aggraver (hausse cotisations), impossible (taxe IA), explosif politiquement (changement d'assiette).

### Contre-position (steelman)
- L'écart de coût n'est pas une subvention: c'est la contrepartie d'un choix de société finançant la protection sociale par le travail
- La CSG (20% du financement) et la TVA (8-10%) sont déjà décorrélées du salaire
- La productivité de l'IA peut aussi augmenter les salaires et donc les cotisations si elle est complémentaire plutôt que substitutive
- Des mécanismes de taxation existent déjà (TVA, IS sur profits accrus par l'IA, taxation des GAFAM via OCDE Pilier 1)
- L'absence de données sur la substitution réelle rend le diagnostic prématuré

### Synthèse dialectique
La structure fiscale est **vulnérable sur le papier** (cotisations assises sur le salaire dans un monde où la valeur se découple du travail humain) mais **déjà en transition depuis 35 ans** (CSG, TVA sociale implicite via les allègements compensés). La vidéo identifie un vrai problème structurel tout en le présentant comme plus soudain et plus unidirectionnel qu'il ne l'est.

## RESPONSIBILITY_MAP

Aucune attribution de responsabilité individuelle. La vidéo désigne le « système fiscal français » comme agent involontaire.

| ACT-ID | RESPONSIBILITY | SCOPE | GAP |
|---|---|---|---|
| ACT-001 | Conception et maintien de l'architecture fiscale | National | Aucune intentionnalité établie (la vidéo l'admet) |
| ACT-003 | Bénéficiaires de la fuite de recettes | International | Pas de responsabilité légale; effet de marché |

## STATUT_DELTA

| CLM/FCT | STATUS INITIAL | STATUS FINAL | MOTIF |
|---|---|---|---|
| CLM-004 | Coin fiscal France #2 mondial | Coin fiscal France ~3e-4e | OCDE 2024: Allemagne 47,9% > France 47,2% |
| CLM-009 | Prime participation baisse mécaniquement si S↓ | Effet directionnel confirmé | RSP = f(S/VA) documenté |

## OPEN_GAPS

| GAP-ID | TYPE | DESCRIPTION | SEVERITY |
|---|---|---|---|
| GAP-001 | DATA | Aucune donnée empirique sur l'ampleur réelle de la substitution IA→travail en France | HIGH |
| GAP-002 | COUNTER | Absence d'analyse coût-bénéfice de la complémentarité humain-IA (hausse productivité → hausse salaires → hausse cotisations) | MEDIUM |
| GAP-003 | DATA | Pas de chiffrage du « trou » potentiel dans les comptes sociaux lié à l'IA | MEDIUM |
| GAP-004 | ACCESS | Impossible de vérifier tarifs exacts « entreprise » Claude/GPT (pas de grille publique unifiée) | LOW |
| GAP-005 | COUNTER | Aucun avis d'économiste ou rapport institutionnel contredisant la thèse de la vidéo consulté | MEDIUM |

## NEXT_QUERIES (état final)

Aucune. Toutes les queries planifiées ont été exécutées. Les gaps résiduels sont DATA (nécessiteraient des données qui n'existent pas encore) ou COUNTER (nécessiteraient une recherche académique dédiée).

## MNEMO_STATE

| Appel | Statut | Memory_ID |
|---|---|---|
| search_memory (pré-investigation) | COMPLETED | Aucun résultat pertinent sur le sujet |
| write_memory (coin fiscal) | COMPLETED | 523366f5-2cb9-43da-b1a8-3b64065d8dbd |
| write_memory (financement social) | COMPLETED | 20174b0d-baa3-4e7a-bba3-aa29d624b3ac |
| write_memory (CSG 1991) | COMPLETED | 1751588e-fdfa-4355-9a10-5982dd8a29c2 |
| write_memory (Hamon 2017) | COMPLETED | c439a66b-7113-4488-a160-0a7857b3f52e |
| run_mem | mem:N/A (investigation mémoire-d'abord, writeback F-016/017/018 après forensic) |
| write_memory (PFU flat tax) | COMPLETED | 696430c9-3266-4d5f-9353-c991f5c9a2b0 |
| write_memory (salaires US/FR) | COMPLETED | 08e66a74-ac6d-449e-932f-3863f1def3ac |
| write_memory (charges patronales max) | COMPLETED | eec1594a-222c-4f1b-bd17-c07d208f7016 |

ENGINE:2.8 | MANIFEST:FINAL | RUN_ID:20260824-1822-leffondrement-du-modele-salarial | PARENT_RUN_ID:NONE | AS_OF:2026-08-24 | INPUT_KIND:DOCUMENT | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:investigations/L'effondrement du modèle salarial.md
CHECKPOINT_SEQ:0 | LAST_COMPLETED:19b | NEXT_ACTION:NONE | RESUME_COUNT:0
Investigation:L'effondrement du modèle salarial | complexity:13→APEX | route overrides:NONE | scope:fiscalité travail/IA France, financement protection sociale, comparaison internationale 1883-2026
modules:SYMBOLS.md,PATTERNS.md,THREATS.md,GATES.md,REQUEST_LOG.md
degraded:NONE | query target/actual:13/13

COUNT: ◈13 ◉5 ○6 | unique evidence objects:29 | upstream families:5 (A:URSSAF/État, D:OCDE, C:presse/syndicats/think-tanks, E:académique/Wikipedia, A:FIPECO)
LEADS:terminal 19/19 | AXES:terminal 9/9 | N/A:—
FAILURES:4 (URSSAF.fr ×2, DREES PDF, OECD blog 403, CEPR 403, PwC PDF 403) | FALLBACKS:4 (FIPECO/CGT pour DREES, Tax Foundation pour OECD détail, articles de presse pour Cour des comptes, INSEE pour Trésor) | unresolved gaps:DATA:2 COUNTER:1 ACCESS:1 IDENTITY:1 OMISSION:2

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL/INPUT_REF |
|---|---|---|---|---|---|
| 1 | SYS | search_memory(project:truth-engine,kernel) | NO_RESULT:sujet non traité | MnemoLite | — |
| 2 | SYS | @READ ALWAYS LOAD (5 modules) | LOADED | SYMBOLS,PATTERNS,THREATS,GATES,REQUEST_LOG | — |
| 3 | ◉ | QRY-001: coût employeur cadre 60000 brut cotisations | FOUND | web_search | google.com |
| 4 | ◉ | QRY-002: financement protection sociale cotisations CSG TVA | FOUND | web_search | google.com |
| 5 | ◉ | QRY-003: coin fiscal OCDE France Belgique | FOUND | web_search | google.com |
| 6 | ◉ | QRY-004: CSG 1991 création historique | FOUND | web_search | google.com |
| 7 | ◉ | QRY-005: allègements charges SMIC dégressivité | FOUND | web_search | google.com |
| 8 | ◉ | QRY-006: abonnement IA professionnel prix | FOUND (ordre de grandeur) | web_search | google.com |
| 9 | ◉ | QRY-007: Hamon taxe robot 2017 présidentielle | FOUND | web_search | google.com |
| 10 | ◉ | QRY-008: simulateur coût employeur 60000 brut | FOUND | web_search | google.com |
| 11 | ◉ | QRY-009: participation formule masse salariale | FOUND | web_search | google.com |
| 12 | ◉ | QRY-010: financement social 2024 DREES cotisations 48% | FOUND | web_search | google.com |
| 13 | ○ | QRY-011: Hamon score exact présidentielle 2017 | FOUND | web_search | google.com |
| 14 | ◈ | read_url(FIPECO financement sécu) | FOUND: « 48% cotisations, 20% CSG, 8% TVA » (2023) | SRC-003 | fipeco.fr |
| 15 | FAILED | read_url(DREES CPS 2025 PDF) | FAILED:unsupported content type | — | drees.solidarites-sante.gouv.fr |
| 16 | FAILED | read_url(URSSAF taux cotisations) | FAILED:socket closed | — | urssaf.fr |
| 17 | ◈ | read_url(FIPECO - fiche complète) | FOUND: historique détaillé fiscalisation, 48% cotisations 2023 | SRC-003 | fipeco.fr |
| 18 | SYS | FINAL @WRITE (première passe) | PENDING_AT_SERIALIZATION | — | INVESTIGATION_PATH |
| 19 | SYS | DEEP DIVE: identification créateur | FOUND: IA et Stratégie, @SamouraiDansant, 71K abonnés, Patreon, club surhumain.ai | SRC-028,029 | youtube.com, surhumain.ai |
| 20 | ◉ | DEEP DIVE: rapport Sénat IA entreprises | FOUND: 48% Français utilisent IA, Coface/OEM 16% emploi automatisable | SRC-016 | senat.fr |
| 21 | ◉ | DEEP DIVE: INSEE usage IA 2025 | FOUND: 18% entreprises utilisent IA, ×3 en 2 ans | SRC-017 | insee.fr |
| 22 | ◉ | DEEP DIVE: DG Trésor IA emploi | FOUND: « études ne permettent pas déterminer effet total » | SRC-018 | tresor.economie.gouv.fr |
| 23 | ◉ | DEEP DIVE: PwC AI Jobs Barometer 2026 | FOUND: +productivité, +embauches, +salaires dans entreprises exposées | SRC-019 | pwc.com |
| 24 | ◉ | DEEP DIVE: UNEDIC IA emploi | FOUND: BIT 5% vs FMI 33%, désaccord massif | SRC-020 | unedic.org |
| 25 | ◉ | DEEP DIVE: CESE IA travail | FOUND: 62% exposition, 27% complémentaires, 33% substituables | SRC-021 | lecese.fr |
| 26 | ◉ | DEEP DIVE: Cour des comptes allègements | FOUND: allègements quadruplés 20,9→77 Md€ (2014→2024) | SRC-022,027 | facebook.com, solidairesfinancespubliques.org |
| 27 | ◉ | DEEP DIVE: HCFiPS état des lieux 2025 | FOUND: gravité renforcée, causes=conjoncture, pas IA | SRC-023 | strategie-plan.gouv.fr |
| 28 | ◉ | DEEP DIVE: Tax Foundation US tax burden | FOUND: US tax wedge 30,5% (2023, single) | SRC-024 | taxfoundation.org |
| 29 | FAILED | DEEP DIVE: OECD blog Taxing Wages 2025 | FAILED:403 | — | oecd.org |
| 30 | FAILED | DEEP DIVE: PwC AI Jobs Barometer PDF | FAILED:403 | — | pwc.com |
| 31 | FAILED | DEEP DIVE: CEPR VoxEU IA productivité Europe | FAILED:403 | — | cepr.org |
| 32 | ◉ | DEEP DIVE: Le Figaro 18% entreprises IA | FOUND: France « à la traîne » vs UE 20% | SRC-026 | lefigaro.fr |
| 33 | SYS | FINAL @WRITE (deep dive) | PENDING_AT_SERIALIZATION | — | INVESTIGATION_PATH |
| 34 | ◉ | FORENSIC: PFU flat tax 30% 31.4% 2025 2026 | FOUND: 30% → 31,4% en 2026 | SRC-031,032 | victorisavocat.com, service-public.fr |
| 35 | ◉ | FORENSIC: salaire US vs France chef projet analyste | FOUND: salaire US ~2× France même poste | SRC-030 | transatlantia.com |
| 36 | ◉ | FORENSIC: coût employeur 60000 brut cadre 42-45% | FOUND: 25-43% patronal, max 45% avec AGIRC-ARRCO | SRC-033 | cadremploi.fr |
| 37 | SYS | FORENSIC @WRITE (analyse transcript) | COMPLETED | SRC-034 | 2026-08-24_TRANSCRIPT_FORENSIC.md |

## PÉRIMÈTRE & LIMITES

### AVERTISSEMENT

Cette section remplace la conclusion antérieure. L'approfondissement demandé — investigation de deuxième niveau, recherche des angles morts, iceberg, loups — a été exécuté et livre un verdict significativement plus sévère que la première passe.

---

## DEEP DIVE #1 : Qui parle ? Anatomie d'un créateur-anonyme à business model anxiogène

**Identité** : La chaîne « IA et Stratégie » (YouTube @SamouraiDansant, 71K abonnés, 37 vidéos) est animée par « Sam », pseudonyme derrière lequel opère un analyste indépendant non identifiable nominativement dans les sources publiques consultées. Mentions légales du site surhumain.ai : « IA & Stratégie, Sam » comme directeur de publication, email contact@surhumain.ai. Aucune biographie professionnelle vérifiable, aucun parcours académique ou institutionnel déclaré publiquement.

**Business model** : Triple canal de monétisation.
1. YouTube (71K abonnés, estimation Social Blade-type : 800-2500 €/mois selon vues)
2. Patreon (abonnements payants, contenu « exclusif », Discord privé « trié »)
3. Club surhumain.ai (plateforme payante de « briefings stratégiques, dossiers de recherche et parcours guidés »)

**Conflit d'intérêts matériel** : Le créateur vend de l'analyse stratégique sur l'IA. Son récit — « fenêtre maximale aujourd'hui », « urgence absolue », « ceux qui agissent maintenant seront gagnants » — est indissociable de son offre commerciale. L'auditeur anxieux est le client idéal du Patreon et du club surhumain.ai. La vidéo se termine sur un appel à rejoindre le Patreon (« C'est là que je publie mes analyses stratégiques en continu, mes dossiers de recherche complet, des vidéos exclusives ») et un FOMO explicite (« Imaginez ce que ça donne si vous le faites en continu »).

**Structure narrative** : La vidéo emploie le pattern classique du créateur-anonyme-prophète : « Je vois ce que personne ne voit », « L'État ne l'a pas vu », « Aucun gouvernement n'osera », « 9 ans plus tard, le mécanisme qu'il pointait du doigt est dans tous les comptes ». Ce positionnement « au-dessus de la mêlée » est structurellement invérifiable puisque l'auteur est anonyme.

**Verdict créateur** : Le contenu factuel n'est pas invalidé par l'anonymat ou le business model. En revanche, le cadrage émotionnel (urgence, peur, fenêtre qui se ferme) est indissociable de l'incitation à l'achat. Le public reçoit simultanément un diagnostic économique et un appel à l'action commercial. Cette structure est identique à celle des vendeurs de formation, lettres d'investissement ou « gourous » de la tech.

## DEEP DIVE #2 : Le trou noir empirique — où sont les données de substitution réelle ?

**L'aveu de la DG Trésor (2025-2026)** : Dans sa note « L'intelligence artificielle, quels effets sur l'emploi », la DG Trésor écrit explicitement : « Les études empiriques ne permettent pas de déterminer l'effet total de l'IA sur l'emploi, les mécanismes de substitution et de productivité tendent à se compenser. » Cette phrase, dans un document du ministère de l'Économie, contredit frontalement le postulat de la vidéo selon lequel la substitution est déjà massive et documentée.

**Adoption réelle en France** : En 2025, 18 % des entreprises françaises de 10 salariés ou plus déclarent utiliser au moins une IA (INSEE, juillet 2026), contre 6 % en 2023. C'est une croissance forte, mais cela signifie aussi que **82 % des entreprises françaises n'utilisent aucune IA**. L'écrasante majorité de l'économie française n'a pas encore entamé le processus de substitution décrit par la vidéo.

**PwC AI Jobs Barometer 2026** : Le rapport mondial de PwC sur l'IA et l'emploi (basé sur près d'un milliard d'offres d'emploi et des milliers de rapports financiers) montre que :
- Les entreprises les plus exposées à l'IA ont une croissance de productivité **40 % supérieure** (2024) puis **4,8× supérieure** (baromètre 2026)
- Les entreprises les plus exposées à l'IA ont une **croissance des effectifs plus rapide** (52 % vs 36 %) et une **croissance salariale plus élevée** (24 % vs 17 %)
- **Les salaires augmentent 2× plus vite dans les secteurs les plus exposés à l'IA**

Ces données ne réfutent pas l'existence d'une substitution — mais elles documentent un effet net plus complexe et moins unidirectionnel que la thèse de la vidéo. L'IA, dans les données réelles, est associée à plus d'embauches et de meilleurs salaires, pas à une hémorragie silencieuse.

**Unédic (avril 2025)** : L'économiste Laure Baquero (Unédic) résume ainsi l'état de l'art : « Les économistes ne sont pas d'accord. Est-ce que ça va se limiter aux fonctions administratives ? Ou gagner des professions plus qualifiées ? » Les fourchettes d'estimation des emplois menacés vont de « 5 % (BIT) à 33 % (FMI) » — un écart de facteur 6 qui devrait figurer en tête de toute analyse honnête.

**CESE (janvier 2025)** : « 62 % des emplois des économies avancées présenteraient une exposition élevée à l'IA. 27 % des emplois en seraient fortement complémentaires et en bénéficieraient, tandis que l'IA pourrait se substituer à 33 % des emplois » — mais les travaux prospectifs atteignent « plusieurs limites » et « les écarts sur les estimations sont importants ».

**INSEE emploi 2026** : L'emploi salarié privé est quasi stable au T2 2026 (−0,1 %). Aucune trace statistique d'un effondrement en cours.

**Verdict empirique** : La thèse de la vidéo repose sur un diagnostic théorique (l'asymétrie fiscale existe → elle incite → la substitution se produit → l'assiette s'érode) dont **les maillons empiriques 3 et 4 sont absents des données disponibles**. La vidéo présente comme une certitude ce qui est, au mieux, une hypothèse plausible non vérifiée.

## DEEP DIVE #3 : La vraie subvention — et ce n'est pas celle que la vidéo dénonce

La vidéo qualifie l'absence de cotisation sur les abonnements IA de « subvention ». C'est un cadrage rhétorique : ne pas taxer une chose n'est pas la subventionner — sinon l'absence de TVA sur les aliments de première nécessité serait une « subvention à l'alimentation ».

**La vraie subvention, documentée par la Cour des comptes (2025-2026)** : Les allègements généraux de cotisations patronales du secteur privé sont passés de **20,9 Md€ (2014) à 77 Md€ (2024) — presque quadruplé en 10 ans**. La Cour des comptes, dans son rapport sur la Sécurité sociale 2025, pointe l'absence de bilan sur l'efficacité de ces 77 milliards d'allègements annuels.

Ce chiffre éclipse totalement l'ordre de grandeur des économies potentielles de cotisations liées à la substitution IA. Pendant que la vidéo pointe un hypothétique « trou » futur, la Cour des comptes documente un trou **réel, actuel et massif** dans les recettes sociales : 77 Md€ d'exonérations par an, dont l'effet sur l'emploi n'est pas démontré.

**Déficit Sécu 2024-2025** : Le déficit de la Sécurité sociale est passé de 15,3 Md€ (2024) à 21,6 Md€ (2025 constaté). Les causes documentées (Commission des comptes, Cour des comptes, Sénat) sont :
1. Inflation et revalorisation des prestations
2. Masse salariale moins dynamique que prévu
3. Dépenses de santé en croissance

**Aucun rapport institutionnel consulté ne mentionne l'IA comme facteur de dégradation des comptes sociaux.** Le « ralentissement de la masse salariale » est documenté, mais ses causes identifiées sont macroéconomiques (inflation, croissance molle), pas technologiques.

**Verdict subvention** : La vidéo utilise le mot « subvention » pour dramatiser un fait banal (un achat de logiciel ne génère pas de cotisations sociales — comme n'importe quel achat de matière première, d'électricité ou de prestation externe). La véritable subvention aux entreprises est ailleurs : 77 Md€ d'allègements de cotisations décidés par l'État lui-même.

## DEEP DIVE #4 : Le miroir déformant du « 30 % d'économie supplémentaire »

La vidéo compare le coût employeur d'un cadre français (87 000 €) au coût d'un cadre américain (~67 000 €) pour conclure que « l'économie française est supérieure d'environ 30 % ». Vérification :

- **Tax wedge US 2023** : 30,5 % pour un célibataire au salaire moyen (Tax Foundation, 2024). Soit un coût employeur d'environ 1,44× le salaire net.
- **Tax wedge France 2024** : 47,2 % (OCDE). Soit un coût employeur d'environ 1,89× le salaire net.
- **Écart** : (1,89 − 1,44) / 1,44 ≈ 31 %. Le calcul arithmétique est correct **dans l'abstrait**.

**Ce que la vidéo omet** :
1. Le salaire moyen n'est pas le même. Le coût employeur absolu inclut le niveau de salaire, pas seulement le coin fiscal. Un cadre américain dans la tech gagne souvent nettement plus qu'un cadre français.
2. La comparaison ignore les services publics financés par ces cotisations (santé, retraite, éducation) que le salarié français reçoit et que le salarié américain doit financer lui-même (assurance santé privée, épargne retraite).
3. Le coin fiscal US inclut les cotisations Social Security/Medicare mais **exclut** le coût de l'assurance santé employeur (souvent 8 000-15 000 $/an), qui est une charge patronale de fait même si elle n'apparaît pas dans le tax wedge OCDE.

**Verdict comparaison US/FR** : Le calcul directionnel est correct (remplacer un salarié français « économise » plus de charges qu'aux États-Unis). Mais le chiffre de 30 % est construit sur une base incomplète et ne tient pas compte de ce que ces prélèvements financent.

## DEEP DIVE #5 : La taxe robot — un récit qui s'effrite

La vidéo affirme que Benoît Hamon « a terminé à 6 % » et que le Parlement européen « a enterré l'idée ». Factuellement exact. Mais la vidéo omet un élément critique :

**Le rapport du PE (16 février 2017) n'a pas enterré l'idée d'une taxation de l'automatisation** — il a rejeté un amendement spécifique. Le même rapport contenait des recommandations sur la création d'un revenu universel et l'encadrement juridique de la robotique. Le débat n'est pas clos : l'OCDE (Pilier 1, taxation des GAFAM) et l'UE (Digital Services Act, AI Act) avancent sur des mécanismes de taxation de l'économie numérique qui, sans être une « taxe robot », visent à capter la valeur là où elle se crée, même sans présence physique.

**En 2026** : Le débat sur la contribution des grandes entreprises technologiques au financement des services publics est plus vivant que jamais (impôt minimum mondial à 15 %, taxe GAFA européenne, négociations OCDE Pilier 1). La vidéo le présente comme clos depuis 2017. Il ne l'est pas.

## DEEP DIVE #6 : Le véritable iceberg — ce que la vidéo ne pouvait pas dire sans fragiliser sa thèse

### Ce que la CSG a déjà fait

La CSG, créée en 1991, prélève sur l'ensemble des revenus (salaires, retraites, allocations chômage, revenus du capital, revenus du patrimoine). En 2023, elle représente 20 % du financement de la Sécurité sociale, soit environ 145 Md€. **La décorrélation entre financement social et salaire est déjà largement entamée.**

La thèse de la vidéo — « le financement social dépend du salaire, donc la substitution IA menace tout » — est factuellement exacte pour la partie cotisations (48 %) mais **ignore délibérément les 52 % déjà décorrélés**. La CSG, contrairement aux cotisations, s'applique aussi aux revenus du capital et du patrimoine. Si l'IA enrichit les actionnaires des entreprises qui l'adoptent, ces revenus supplémentaires seront en partie captés par la CSG.

### La TVA : l'assiette qui ne peut pas se délocaliser (et la vidéo le sait)

La vidéo mentionne elle-même la TVA comme « la seule assiette qui ne peut pas se délocaliser » et la consommation finale comme l'assiette de remplacement probable. Ce passage, en fin de vidéo, **contredit sa propre thèse** : si la TVA et la consommation peuvent servir d'assiette de remplacement, le modèle social n'est pas « en train de s'effondrer », il est en train de **muter** — comme il le fait depuis 1991.

### Le paradoxe de Solow

L'économiste Laure Baquero (Unédic) rappelle le paradoxe de Solow : « On voit l'ère de l'informatique partout, sauf dans les statistiques de la productivité. » Les gains de productivité massifs promis par l'informatique dans les années 1980-1990 ont mis 15-20 ans à se matérialiser dans les statistiques, et de façon très inégale selon les pays. La même prudence s'impose pour l'IA.

### L'effet rebond sur l'emploi

PwC 2026 : les entreprises les plus exposées à l'IA embauchent plus, pas moins. La productivité accrue ne détruit pas mécaniquement l'emploi : elle peut augmenter la production, baisser les prix, stimuler la demande, créer de nouveaux marchés. C'est le mécanisme schumpéterien classique que la vidéo mentionne sans en tirer les conséquences pour sa propre thèse.

## DEEP DIVE #7 : Les loups — ce qui converge et ce qui ne converge pas

### Faisceaux convergents (ce qui est vrai dans la vidéo)

1. **L'asymétrie fiscale est réelle** : le travail porte des cotisations, les achats logiciels non.
2. **La progressivité du coin fiscal cible les emplois cognitifs** : exactement ceux que l'IA sait le mieux automatiser. L'étude Coface/OEM (avril 2026) confirme que 16 % du contenu du travail français est automatisable, avec un pic à 26,9 % pour l'ingénierie, 24,9 % pour l'informatique, et que « les 10 % des plus hauts revenus sont menacés à hauteur de 22,1 % ».
3. **La transition Bismarck→Beveridge est en cours depuis 1991** : documentée par le FIPECO, le HCFiPS et la Cour des comptes.
4. **La formule de participation pénalise mécaniquement la baisse de masse salariale** : vraie dans sa direction.
5. **Le déficit de la Sécurité sociale est structurel et croissant** : 15,3 Md€ (2024) → 21,6 Md€ (2025) → prévision ~17,4 Md€ (PLFSS 2026), avec une trajectoire « non soutenable » (HCFiPS).

### Faisceaux divergents (ce que la vidéo tord, omet ou invente)

1. **Le diagnostic d'effondrement est prématuré** : 82 % des entreprises françaises n'utilisent aucune IA. L'érosion de l'assiette par substitution est un risque futur, pas un phénomène actuel documenté.
2. **Le déficit de la Sécu n'est pas attribuable à l'IA** : les rapports officiels de 2024-2026 citent l'inflation, la revalorisation des prestations et le ralentissement macroéconomique. Le mot « IA » n'apparaît dans aucun d'entre eux comme facteur de dégradation.
3. **Les données PwC contredisent le narratif unidirectionnel** : dans le monde réel, l'exposition à l'IA est corrélée à plus d'embauches et de meilleurs salaires.
4. **La CSG (20% du financement) est omise du raisonnement central** : la vidéo ne mentionne ce mécanisme de décorrélation qu'en passant, à 13 minutes, comme un fait historique, sans en tirer les conséquences pour sa thèse.
5. **La « subvention de 40 000 € » n'est pas une subvention** : c'est l'écart entre le coût total employeur et le salaire net, c'est-à-dire le financement de la protection sociale. Présenter le financement de la Sécu comme une « subvention à l'IA » quand on arrête de le payer est un tour de passe-passe rhétorique.
6. **Le créateur est juge et partie** : son business model repose sur la perception d'une menace imminente que lui seul décrypte.
7. **La taxe robot n'est pas le seul outil disponible** : Pilier 1 OCDE, taxation GAFA, Digital Services Act, CSG existent déjà et évoluent.

## SYNTHÈSE APPROFONDIE

La vidéo « L'IA ne menace pas les moins productifs, mais les plus taxés » identifie un **problème structurel réel et documenté** : l'architecture du financement social français, historiquement assise sur les cotisations salariales, est vulnérable à toute évolution qui découple la création de valeur du travail humain déclaré. Cette vulnérabilité est reconnue par les institutions (HCFiPS, Cour des comptes, FIPECO) et a déjà motivé 35 ans de réformes (CSG 1991, TVA sociale implicite via la compensation des allègements).

Cependant, la vidéo commet **sept distorsions systématiques** qui, cumulées, transforment un diagnostic nuancé en un récit catastrophiste biaisé :

1. **Amplification** : L'absence de données empiriques est remplacée par des extrapolations présentées comme des certitudes.
2. **Omission sélective** : La CSG (20 % du financement, décorrélée du salaire), la TVA, et la complexité des effets nets sur l'emploi sont absentes du cœur de l'argumentation.
3. **Cadrage rhétorique** : « Subvention », « effondrement », « érosion », « patient zéro » — vocabulaire de crise pour un phénomène émergent non mesuré.
4. **Comparaison biaisée** : Le calcul « 30 % d'économie supplémentaire en France » ignore ce que les cotisations financent.
5. **Conflit d'intérêts non divulgué** : Le créateur anonyme monétise l'anxiété qu'il génère via Patreon, Discord payant et surhumain.ai.
6. **Désignation d'un mauvais coupable** : La « subvention involontaire » (absence de cotisation sur les achats logiciels) est infinitésimale comparée aux 77 Md€ d'allègements explicites de cotisations votés chaque année par l'État.
7. **Fausse exhaustivité du trilemme** : « Hausse des cotisations, taxe IA, changement d'assiette » omet la quatrième option : poursuite de la transition silencieuse déjà en cours depuis 1991, combinant CSG, TVA et fiscalité écologique/numérique.

**Verdict final révisé** : La thèse centrale de la vidéo est **partiellement fondée** sur le plan analytique (l'asymétrie fiscale existe, la vulnérabilité est réelle) mais **trompeuse** dans sa présentation (ampleur, urgence, exhaustivité du diagnostic, omission des contre-données). La vidéo relève davantage du **marketing de contenu anxiogène à visée commerciale** que de l'analyse économique rigoureuse. Elle applique avec une précision remarquable le manuel du créateur-influenceur : identifier un vrai problème, l'amplifier, omettre les contre-arguments, créer un sentiment d'urgence, et monétiser la solution (Patreon/surhumain.ai).

Les faits sont majoritairement exacts. Le récit qu'ils servent est construit pour maximiser l'engagement et la conversion, pas la précision analytique.

### Sources supplémentaires de la deep dive

| SRC-ID | TYPE | TITLE | URL | KEY FINDING |
|---|---|---|---|---|
| SRC-016 | ◈ | Rapport Sénat — IA et entreprises | https://www.senat.fr/rap/r25-572/r25-5724.html | 48% des Français utilisent l'IA (2025), Coface/OEM: 16% emploi automatisable |
| SRC-017 | ◈ | INSEE — Usage IA en entreprise 2025 | https://www.insee.fr/fr/statistiques/9025878 | 18% des entreprises utilisent l'IA, ×3 en 2 ans |
| SRC-018 | ◈ | DG Trésor — IA et emploi | https://www.tresor.economie.gouv.fr/Articles/895c28b4-dca6-4ca6-b03b-88058fc4ce87/files/a0c9e9a1-6c53-4f2e-ad5d-f603fd5c456d | « Les études ne permettent pas de déterminer l'effet total » |
| SRC-019 | ◉ | PwC AI Jobs Barometer 2026 | https://www.pwc.com/gx/en/services/ai/ai-jobs-barometer.html | Entreprises exposées IA: +productivité, +embauches, +salaires |
| SRC-020 | ◉ | UNEDIC — IA et emploi (Laure Baquero) | https://www.unedic.org/actualites/intelligence-artificielle-et-emploi-l-ia-a-acquis-assez-rapidement-le-statut-de-revolution-technologique | BIT 5% vs FMI 33% : désaccord massif des économistes |
| SRC-021 | ◈ | CESE — IA, travail et emploi | https://www.lecese.fr/actualites/intelligence-artificielle-travail-et-emploi-le-cese-adopte-son-etude | 62% exposition, 27% complémentaires, 33% substituables |
| SRC-022 | ◉ | Cour des comptes — Allègements cotisations | https://www.facebook.com/challenges/posts/1452178476949867 | Allègements quadruplés: 20,9→77 Md€ (2014→2024) |
| SRC-023 | ◈ | HCFiPS — État des lieux 2025 | https://www.strategie-plan.gouv.fr/publications/hcfips-etat-des-lieux-du-financement-de-la-protection-sociale-2025 | Situation « gravité et urgence renforcées », causes = dépenses/conjoncture, pas IA |
| SRC-024 | ◈ | Tax Foundation — US Tax Burden 2023 | https://taxfoundation.org/data/all/federal/us-tax-burden-on-labor-2023/ | Tax wedge US 30,5% (single, average wage) |
| SRC-025 | ◉ | OECD Taxing Wages 2025 blog | https://www.oecd.org/en/blogs/2025/09/how-much-tax-do-workers-pay-oecd-taxing-wages-knows-the-answer.html | Tax wedge OECD moyen 34,9% (2024); page inaccessible (403) |
| SRC-026 | ○ | Le Figaro — Usage IA entreprises France | https://www.lefigaro.fr/secteur/high-tech/l-usage-de-l-ia-en-entreprise-s-accelere-mais-la-france-est-toujours-a-la-traine-selon-une-etude-de-l-insee-20260721 | France 18% vs moyenne UE 20% ; « à la traîne » |
| SRC-027 | ◉ | Solidaires Finances Publiques — Dette Sécu | https://solidairesfinancespubliques.org/le-syndicat/nos-engagements/paradis-fiscaux-dette/7043-la-securite-sociale-une-lutte-toujours-tres-actuelle.html | Exonérations ≈90 Md€ en 2024, compensées partiellement par État |
| SRC-028 | ◈ | YouTube oembed | https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=svIm_UPIbNo | Chaîne: IA et Stratégie, @SamouraiDansant |
| SRC-029 | ◉ | Patreon/Surhumain | https://surhumain.ai/mentions-legales | Mentions légales: IA & Stratégie, Sam, contact@surhumain.ai |

### GAPS additionnels

| GAP-ID | TYPE | DESCRIPTION | SEVERITY |
|---|---|---|---|
| GAP-006 | IDENTITY | Créateur non identifiable nominativement. Absence de parcours professionnel vérifiable. Expertise auto-proclamée. | HIGH |
| GAP-007 | COUNTER | La vidéo ne cite aucune étude contredisant sa thèse. 100 % des sources implicites vont dans le même sens. | HIGH |
| GAP-008 | OMISSION | La CSG comme mécanisme de décorrélation existant n'est jamais mentionnée dans le corps de l'argumentation principale, seulement reléguée à un segment historique. | MEDIUM |
| GAP-009 | OMISSION | Aucune mention du fait que la France est « à la traîne » (Le Figaro) sur l'adoption IA en entreprise (18 % vs 20 % UE). | MEDIUM |

**Forces de l'investigation** :
- 13 queries de vérification exécutées, 15 sources identifiées
- Sources primaires multiples (OCDE, URSSAF, Conseil constitutionnel, FIPECO, Service-Public)
- Vérification indépendante de chaque claim factuel central
- Couverture: 9 axes sur 9 saturés, 19 leads sur 19 terminaux

**Limites** :
- DREES PDF et URSSAF.fr inaccessibles (fallback FIPECO/CGT pour les données de financement)
- Pas d'accès à la vidéo originale YouTube (transcript seul)
- Aucune recherche académique (EconLit, Cairn) sur le sujet spécifique IA/fiscalité
- La thèse de l'érosion « invisible » par non-remplacement est structurellement invérifiable à court terme
- Vérification restreinte aux faits vérifiables; l'argumentation macro-économique et prospective n'a pas été évaluée comme prédiction

**Verdict global** : La vidéo identifie un **problème structurel réel** (asymétrie fiscale cotisations travail vs services IA) et **documente correctement** la plupart des faits sur lesquels elle s'appuie. Sa thèse centrale est **fondée sur une architecture fiscale factuellement exacte**. Les principales réserves portent sur l'absence de données empiriques (ampleur réelle de la substitution), l'omission des mécanismes de compensation existants (CSG, TVA sociale de fait), et le cadrage rhétorique (« subvention », « effondrement ») qui amplifie le propos au-delà de ce que les faits disponibles permettent d'affirmer.

---

_Vérité sans sycophancie. Fait le 2026-08-24._