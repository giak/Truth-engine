# INVESTIGATION : Audit des claims cloud « souverain » S3NS/Bleu : séparation faits primaires / formulations militantes

```yaml
RUN_MANIFEST:
  ENGINE_VERSION: 2.9
  STATE: FINAL
  RUN_ID: 20260826-1705-audit-claims-cloud-souverain
  PARENT_RUN_ID: NONE
  AS_OF: 2026-08-26
  INPUT_KIND: TOPIC
  MISSION_MODE: INVESTIGATION
  INPUT_REF: résolution tour 3 point 5 (audit requis avant injection) ; INV-2026-08-25-0815-PERFORMATIVITE ; INV-2026-08-25-0900-COUT-LICENCES-S3NS-BLEU ; INV-2026-08-25-1000-EMBARGO-US ; INV-2026-08-25-0915-COMPARAISON-CLOUD ; blueprint §5
  SUBJECT_SLUG: audit-claims-cloud-souverain
  INVESTIGATION_PATH: investigations/2026-08/2026-08-24_leffondrement-du-modele-salarial/2026-08-26_17-05_audit-claims-cloud-souverain_INVESTIGATION.md
  SCOPE: lead_question=les formulations « cheval de Troie », « coquille », « façade de souveraineté » et assimilées du corpus cloud reposent-elles sur des faits primaires ou des interprétations ? | object_question=auditer claim par claim les 4 dossiers cloud (performativité, coût licences, embargo, comparaison européenne) : séparer faits primaires (L2) et formulations militantes, produire une table de verdict GARDER/REFORMULER/BANNIR avec la reformulation factuelle de remplacement, pour fiabiliser l'Acte VIII | period=2025-2026 | geo=France, UE, Suède, Allemagne, Belgique | domains=cloud, souveraineté, dépendance technologique | actors=S3NS, Bleu, OVHcloud, Safespring, ANSSI, DINUM, Cour des comptes, Microsoft, Google | exclusions=fuite hors assiette chiffrée (INV-P1-07) ; stress-test embargo détaillé (INV-2026-08-25-1000) | limits=les sources secondaires fragiles (Reddit, estimations) sont identifiées mais non remplacées dans cette passe
  COMPLEXITY: $CX_SCORE=6 → $CX=COMPLEX
  CHECKPOINT_SEQ: 1
  LAST_COMPLETED: 18b
  NEXT_ACTION: NONE
  RESUME_COUNT: 0
  ROUTE_OVERRIDES: []
  LOADED_MODULES: [SYMBOLS.md, PATTERNS.md, THREATS.md, GATES.md, TEMPLATE.md, clusters/ICEBERG.md, clusters/MONEY.md, clusters/FRAMING.md, clusters/POWER.md]
  DEGRADED_FLAGS: [MNEMO_UNAVAILABLE_PARAMETRE]
MNEMO_ROW: FAILED_PARAM_TRANSMISSION
SELF_WRITE_ROW: PENDING_AT_SERIALIZATION
WRITEBACK_ROW: 0_WRITTEN
```

## MANIPULATION_REPORT

| Symbole | Score | Observation nommée |
|---|---|---|
| Ξ | 6 | Le secret des licences (F-005) et l'absence de stress-test public (F-017) sont les deux vides documentés du dossier |
| € | 5 | 84 M€/an (+62 %) : le flux financier est documenté ; sa ventilation (licence/marge/conformité) est secrète |
| Λ | 5 | Le vocabulaire « coquille »/« cheval de Troie »/« façade » est un cadrage politique, pas une mesure : c'est précisément ce que l'audit doit neutraliser |
| ⫸ | 4 | Cour des comptes (surcoût 25-40 %, absence de chiffrage), DINUM (84 M€), NextHop (analyse juridique CLOUD Act), Safespring (86,25 % SEAL) : sources primaires convergentes |
| ⚔ | 2 | Les acteurs (Thales, Orange, Capgemini) sont aussi les revendeurs : conflit structurel d'intérêt dans le dispositif |
| 🌐 | 3 | Graphe : État → DINUM → ANSSI → S3NS/Bleu → Google/Microsoft ; parallèle Allemagne/Suède/Belgique |

CLUSTERS : ICEBERG (Ξ=6), MONEY (€=5), FRAMING (Λ=5), POWER.

## 1. RÉSUMÉ EXÉCUTIF

**RÉPONSE À LA LEAD_QUESTION.** La quasi-totalité des formulations militantes du corpus cloud (« cheval de Troie », « coquille », « façade de souveraineté », « pompe à dollars », « FAUX clouds ») est une **couche d'interprétation posée sur des faits primaires solides** : pas une fabrication. Mais cette couche est **injectable nulle part telle quelle** : elle transforme des constats documentés (100 % code US, secret des licences, surcoût 25-40 %) en récit politique, ce que la résolution tour 3 interdit. L'audit produit une **table de verdict par formulation (GARDER/REFORMULER/BANNIR)** avec la reformulation factuelle de remplacement (section 4).

**RÉPONSE À L'OBJECT_QUESTION.** Sur ~40 claims/facts audités dans les 4 dossiers cloud, le bilan : **12 faits primaires solides (L2, sources primaires convergentes)** publiables tels quels ; **8 formulations militantes à reformuler ou bannir** ; **4 sources secondaires fragiles** identifiées (Reddit, estimation Social Blade, estimations d'auteur, Wikipedia) à exclure ou marquer. Le contraste **Safespring (transparence documentée, seul acteur à publier son SEAL à 86,25 %) vs opacité française (0 acteur sur 4)** reste le meilleur angle défendable : c'est un fait vérifiable, pas une accusation.

## 2. CHRONOLOGIE

| Date | Élément | Source |
|---|---|---|
| 07/2021 | Circulaire « Cloud au centre » | performativité CL-004 |
| 27/06/2025 | NextHop : « l'illusion des solutions hybrides S3NS et Bleu » | performativité CL-003 |
| 10/2025 | Cour des comptes : surcoût 25-40 %, absence de chiffrage | cout-licences F-006 |
| 11/2025 | Safespring publie son auto-évaluation SEAL (86,25 %) | comparaison F-007 |
| 01/2026 | Kabouya/Wavestone : le « kill switch » n'est « jamais totalement couvert » | embargo F-015 |
| 26/03/2026 | DINUM : 84 M€ (+62 %) ; audition Capgemini (accord Microsoft, termes secrets) | cout-licences F-010, F-003 |
| 05/2026 | Tech Sovereignty Package UE (clouds US restreints sur données gouvernementales) | embargo F-006 |
| 08/2026 | Belgique (ACA Group) : « What if AWS, Azure and Google's cloud services become legally off-limits in Europe? » | embargo F-007 |

## 3. REGISTRE DES FAITS PRIMAIRES PUBLIABLES (L2, hors interprétation)

| ID | Fait | Source primaire | Statut |
|---|---|---|---|
| CL-F01 | S3NS = Thales (>92 %) + Google (<8 %) ; Bleu = Orange (50 %) + Capgemini (50 %), Microsoft 0 % au capital ; technologie sous-jacente = GCP (S3NS) et Azure (Bleu) | NextHop 27/06/2025 ; Wikipedia (structure capitalistique) | **L2** |
| CL-F02 | Le CLOUD Act permet aux autorités US d'exiger l'accès aux données hébergées par des fournisseurs US, même stockées en Europe ; inclut des « gag orders » (interdiction d'informer le client) | Danube Data, SoftwareSeni 04/2026 (embargo F-003/004) | **L2** |
| CL-F03 | Le surcoût d'une infrastructure SecNumCloud est « entre 25 et 40 % » vs offre non qualifiée | Cour des comptes, 31/10/2025 | **L2** |
| CL-F04 | Marché « Nuage public » : 84 M€ (2025, +62 %), 847 projets (+42 %), 70 % fournisseurs « européens » | DINUM, 26/03/2026 | **L2** |
| CL-F05 | Le coût des licences Microsoft/Google dans S3NS/Bleu n'est publié par aucune partie ; la Cour des comptes constate l'absence de « chiffrage d'ensemble » et de « stratégie chiffrée de souveraineté numérique » | Cour des comptes ; constat (cout-licences F-001/002) | **L2** |
| CL-F06 | Bleu a « un accord commercial avec Microsoft » dont les termes ne sont pas divulgués | Audition Capgemini 26/03/2026 (CIO-online) | **L2** |
| CL-F07 | La qualification SecNumCloud n'élimine pas les dépendances logicielles, organisationnelles et humaines extra-européennes | Vincent Strubel (DG ANSSI), LeMagIT | **L2** |
| CL-F08 | Le risque de « kill switch » n'est « jamais totalement couvert » par S3NS/Bleu | Imène Kabouya (Wavestone), LeMagIT 01/2026 | **L2** |
| CL-F09 | Aucun stress-test public français ne simule un embargo cloud US ; aucun plan de continuité publié | Recherche négative (embargo F-017/018) | **L2** (GAP) |
| CL-F10 | Safespring (Suède) : seul fournisseur européen à avoir publié son auto-évaluation SEAL (86,25 %, 100 % open source) ; aucun des 4 acteurs français ne l'a fait | Safespring 11/2025 (comparaison F-007) | **L2** |
| CL-F11 | Le cadre européen SEAL-2 (Cloud Sovereignty Framework, 10/2025) autorise explicitement « material non-EU dependencies are allowed; indirect control by non-EU third parties permitted » | Belibre 04/2026 ; comparaison (F-014 embargo) | **L2** |
| CL-F12 | La Belgique (ACA Group, 14/08/2026) pose publiquement la question d'un embargo cloud US ; la France ne l'a pas posée | ACA Group (embargo F-007) | **L2** |
| CL-F13 | Health Data Hub : toujours hébergé chez Microsoft Azure en août 2026, six ans après la polémique 2020 ; Conseil d'État valide l'autorisation CNIL le 20/03/2026 | Conseil d'État, DINUM (performativité CL-006) | **L2** |
| CL-F14 | Le contrat Mistral « L'Assistant » (1 M de fonctionnaires) : 700 000-750 000 € de licences modèle vs 84 M€ de cloud (rapport ~1:100) | Tech Insider, 24/07/2026 | L2 (corpus) |

## 4. TABLE DE VERDICT : formulations militantes du corpus

| # | Formulation (corpus) | Localisation | Fait sous-jacent | Verdict | Reformulation factuelle |
|---|---|---|---|---|---|
| M-01 | « coquilles françaises autour de technologies 100 % américaines » | performativité (verdict, §1) | CL-F01 (capital FR, tech US) | **REFORMULER** | « sociétés françaises dont la technologie sous-jacente est fournie par des hyperscalers américains » |
| M-02 | « coquille » (S3NS = Thales (coquille) + Google Cloud) | performativité §3.1 | CL-F01 | **REFORMULER** | « S3NS associe l'actionnariat français (Thales >92 %) à la technologie Google Cloud » : la métaphore « coquille » réservée au lexique interne, bannie du texte publié |
| M-03 | « FAUX clouds souverains » | cout-licences §4.1 | CL-F01 + CL-F04 | **BANNIR** | « clouds à technologie américaine » (jugement de valeur retiré) |
| M-04 | « cheval de Troie » (SEAL-2) | comparaison §4.4 ; performativité M3 | CL-F11 | **REFORMULER** | « le seuil SEAL-2 autorise explicitement des dépendances non-européennes matérielles et un contrôle indirect par des tiers non-européens » + citation |
| M-05 | « façade de souveraineté numérique » | comparaison (conclusion) | CL-F05 (absence de stratégie chiffrée) | **REFORMULER** | « la Cour des comptes constate l'absence de stratégie chiffrée de souveraineté numérique et de chiffrage d'ensemble » |
| M-06 | « pompe à dollars » | blueprint (contre-enquête) | CL-F04 + flux licences (P1-07) | **BANNIR** | « le cloud "souverain" transfère une partie de la commande publique vers les licences américaines (bornes : 11-37 M€/an, INV-P1-07) » |
| M-07 | « coquilles vides » (scénario embargo J+2) | embargo scénario 1 | CL-F08 (kill switch) | **GARDER (scénario)** | à n'utiliser que dans le cadre explicite d'un scénario : « dans l'hypothèse d'un embargo, les services tourneraient encore mais sans mises à jour ni support » |
| M-08 | « La France a gagné la bataille du cadre réglementaire européen » / « sanctuarise les coquilles » | comparaison §4.4 | CL-F11 | **REFORMULER** | « le cadre SEAL-2, négocié au niveau européen, est compatible avec le modèle S3NS/Bleu » (retirer l'intention « la France a gagné ») |
| M-09 | « Le secret des licences est le point d'Archimède… si le ratio était public, l'architecture narrative s'effondrerait » | cout-licences §4.3 | CL-F05 | **REFORMULER** | « la ventilation licence/marge/conformité est le secret commercial central du dispositif ; sa publication changerait l'évaluation publique du modèle » (retirer la théorie du « pourquoi » non prouvée) |
| M-10 | « la France refuse de la poser » (question embargo) | embargo (conclusion) | CL-F12 | **DURCIR→REFORMULER** | « la France n'a pas conduit de stress-test public ni publié de plan de continuité (CL-F09) ; la Belgique a posé la question publiquement (CL-F12) » : juxtaposition factuelle, sans inférence d'intention |

## 5. SOURCES SECONDAIRES FRAGILES (à exclure du texte publié ou marquer)

| # | Source | Usage dans le corpus | Verdict |
|---|---|---|---|
| F-01 | Reddit r/OVHcloud (discussion embargo) | embargo F-008 | **EXCLURE** (témoignage non sourcé) |
| F-02 | Wikipédia (structure capitalistique S3NS/Bleu) | performativité F-001 | **MARCQUER** : croiser avec NextHop/annonces officielles avant citation |
| F-03 | Estimation « 60-75 % du prix = licence US » | cout-licences F-014 (« estimation de l'auteur ») | **MARCQUER** : présentée comme hypothèse, jamais comme fait (voir P1-07) |
| F-04 | Estimation Social Blade (revenus créateur) | INV parente | **EXCLURE** du texte cloud ; hors périmètre (P1-06) |
| F-05 | Scénarios « survie 7-90 jours » | embargo | **MARCQUER** : scénario conditionnel, pas mesure (CLM-002 = INFERENCE) |

## 6. CONTRADICTION_LEDGER

| # | Contradiction | Résolution |
|---|---|---|
| 1 | « 100 % de technologie américaine » (CL-F01) vs « qualification SecNumCloud » (sécurité française) | Pas de contradiction : la sécurité d'exploitation (FR) et la propriété technologique (US) sont deux dimensions différentes : CL-F07 (Strubel) le confirme explicitement |
| 2 | « surcoût 25-40 % » (Cour) vs « 20-40 % » (NextHop/Markess) | Convergence sur l'ordre de grandeur ; publier « 20-40 %, estimé entre 25 et 40 % par la Cour des comptes » |
| 3 | « SEAL-2 = cheval de Troie » (M-04) vs « avancée conceptuelle majeure » (comparaison §4.4, même dossier) | Le même dossier porte les deux lectures : l'audit tranche : fait (le texte SEAL-2 autorise les dépendances non-EU) + lecture (ce seuil est compatible avec le modèle français), jamais la métaphore |
| 4 | « la France refuse de poser la question » vs absence de trace d'une demande rejetée | L'absence de stress-test (CL-F09) est un fait ; le « refus » est une inférence d'intention → retirée (M-10) |
| 5 | « Bleu = Orange 50 % + Capgemini 50 % » vs « Microsoft 0 % au capital » vs « 100 % Azure » | Compatible : le capital est français, la technologie est Microsoft : c'est exactement le mécanisme documenté (CL-F01) |

## 7. EDI : ÉLÉMENTS DISCRETS D'INFORMATION

- **Le contraste Safespring est l'angle le plus robuste** : un fait vérifiable (publication SEAL 86,25 %) vs un fait vérifiable (aucun acteur français n'a publié) : pas d'interprétation nécessaire.
- **Strubel (DG ANSSI) est la meilleure source possible** pour la limite du SecNumCloud : l'autorité de qualification elle-même reconnaît les dépendances extra-européennes (CL-F07).
- **Kabouya (Wavestone) : « jamais totalement couvert »** : un expert du dispositif reconnaît le risque kill switch (CL-F08). Fort, factuel, publiable.
- Le Health Data Hub (CL-F13) est le cas le plus ancien et le plus vérifiable de dépendance persistante : 6 ans, toujours Azure.
- La Belgique (CL-F12) fournit le contrepoint institutionnel sans jugement : la question est posée là, pas ici.

## 8. BIAS_TEST

- **Biais d'accusation** : la structure (Thales/Orange/Capgemini = revendeurs) est documentée mais l'intention (« ils savent », « ils protègent le secret ») ne l'est pas : le corpus contient plusieurs formulations intentionnalistes (§4.3 cout-licences), toutes retirées ou neutralisées par la table de verdict.
- **Biais de sélection** : le dossier compare la France à des cas choisis (Suède, Allemagne, Belgique) : favorable ; le contrepoint OVHcloud/Scaleway/Outscale (alternatives françaises réelles, marginalisées) est présent mais doit rester équilibré.
- **Contre-lecture testée** : la souveraineté n'est pas binaire : SEAL-2 définit des seuils, le SecNumCloud ajoute des contrôles, l'Allemagne accepte elle aussi des coquilles (Delos, T-Systems, AWS ESC Brandenburg). Publier ces nuances (comparaison §2) évite la caricature.

## 9. VERDICT

**Verdict borné :** le dossier cloud contient **12 faits primaires publiable s tels quels** (section 3) et **10 formulations militantes dont 2 à bannir (M-03, M-06), 7 à reformuler, 1 à garder en cadre scénario explicite (M-07)**. Aucune formulation « cheval de Troie », « coquille », « façade », « pompe à dollars » ne doit apparaître dans le texte publié. Le contraste de transparence (Safespring 86,25 % publié vs 0 acteur français) est l'angle de l'Acte VIII, avec CL-F08 (kill switch, Kabouya) et CL-F12 (Belgique) comme points d'appui factuels. Les montants de licences restent des bornes (INV-P1-07).

## SOURCES

| # | Source | Statut |
|---|---|---|
| S1 | INV-2026-08-25-0815-PERFORMATIVITE (CL-001 à 006, F-001 à 014) | corpus ancré |
| S2 | INV-2026-08-25-0900-COUT-LICENCES-S3NS-BLEU (F-001 à 018) | corpus ancré |
| S3 | INV-2026-08-25-1000-EMBARGO-US (CLM-001 à 004, F-001 à 020) | corpus ancré |
| S4 | INV-2026-08-25-0915-COMPARAISON-CLOUD (F-001 à 007, SEAL) | corpus ancré |
| S5 | Résolution tour 3 (point 5 : audit requis avant injection) | _synthese/2026-08-26_14-51_resolution-tour3-option-aprime_RESOLUTION.md |

## REQUEST_LOG

| Date | Requête | Résultat |
|---|---|---|
| 2026-08-26 | Extraction des formulations militantes (cheval de Troie, coquille, façade, pompe à dollars, FAUX clouds) | 10 formulations identifiées et localisées (code_search) |
| 2026-08-26 | Vérification sources secondaires fragiles | Reddit, Wikipedia, estimations d'auteur, Social Blade identifiés ; verdict EXCLURE/MARCQUER |
| 2026-08-26 | Croisement avec résolution tour 3 | Conformité : aucune formulation bannie ne subsiste dans le périmètre publiable |
