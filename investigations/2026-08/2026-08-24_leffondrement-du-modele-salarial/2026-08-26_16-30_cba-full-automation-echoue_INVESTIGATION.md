# INVESTIGATION — CBA : le troisième « échec » du full automation (et sa persistance différée)

```yaml
RUN_MANIFEST:
  ENGINE_VERSION: 2.9
  STATE: FINAL
  RUN_ID: 20260826-1615-cba-full-automation-echoue
  PARENT_RUN_ID: NONE
  AS_OF: 2026-08-26
  INPUT_KIND: TOPIC
  MISSION_MODE: INVESTIGATION
  INPUT_REF: NONE
  SUBJECT_SLUG: cba-full-automation-echoue
  INVESTIGATION_PATH: investigations/2026-08/2026-08-24_leffondrement-du-modele-salarial/2026-08-26_16-30_cba-full-automation-echoue_INVESTIGATION.md
  SCOPE: lead_question=le cas CBA constitue-t-il bien un « échec » du remplacement par IA, et que documente-t-il exactement ? | object_question=que révèle la séquence CBA 2024-2026 (annonce, retournement, poursuite des coupes) sur la fiabilité du « full automation » et sur la trajectoire réelle de l'emploi de support ? | period=2024-07-2026-07 | geo=Australie (onshore), Inde, Afrique du Sud | domains=emploi, IA, relations industrielles, offshoring | actors=CBA, FSU, Fair Work Commission, Microsoft, OpenAI, Nutun, Bloomberg Intelligence | exclusions=autres cas (Klarna/IBM traités ailleurs), équilibre financier détaillé de CBA | limits=Reuters 401 (snippet), Bloomberg paywall, nombre de retours effectifs non publié
  COMPLEXITY: $CX_SCORE=9 → $CX=APEX
  CHECKPOINT_SEQ: 1
  LAST_COMPLETED: 18b
  NEXT_ACTION: NONE
  RESUME_COUNT: 0
  ROUTE_OVERRIDES: []
  LOADED_MODULES: [SYMBOLS.md, PATTERNS.md, THREATS.md, GATES.md, TEMPLATE.md, clusters/ICEBERG.md, clusters/MONEY.md, clusters/FRAMING.md, clusters/POWER.md, clusters/RESISTANCE.md, clusters/FRAGMENTATION.md]
  DEGRADED_FLAGS: [MNEMO_UNAVAILABLE_PARAMETRE, REUTERS_401, BLOOMBERG_PAYWALL, NOMBRE_RETOURS_NON_PUBLIE]
MNEMO_ROW: FAILED_PARAM_TRANSMISSION
SELF_WRITE_ROW: PENDING_AT_SERIALIZATION
WRITEBACK_ROW: 0_WRITTEN
```

## 1. RÉSUMÉ EXÉCUTIF

**RÉPONSE À L'OBJECT_QUESTION.** Le cas CBA documente un **échec immédiat de la substitution** : la banque annonce le 28/07/2025 la suppression de 45 postes de service client au motif d'un « voice-bot » IA censé réduire les appels, puis fait machine arrière le 21/08/2025, s'excuse, reconnaît une « erreur » (les rôles n'étaient pas redondants, les volumes d'appels montaient), et offre aux salariés retour, redéploiement ou départ (FCT-001 à FCT-006). Mais l'échec du *moment* ne clôt pas le phénomène : en juillet 2026, des centaines de postes de chat support sont coupés via l'externalisateur Nutun (Johannesburg) tandis que la plateforme IA Microsoft résout ~9 conversations sur 10 sans humain, et le syndicat chiffre ~800 rôles CBA supprimés en un an (FCT-008, FCT-009). **La leçon n'est pas « l'IA a échoué, réembauche » : c'est que la substitution ratée sur un périmètre mesurable (call centre onshore) coexiste avec une substitution réussie ailleurs (chat, offshoring), et que le retournement public n'a ni empêché ni mesuré la suite.**

**RÉPONSE À LA LEAD_QUESTION (verdict borné).** Oui, le corpus « CBA 45 agents → excuses » est vérifiable et exact sur l'essentiel (date corrigée : juillet-août 2025, pas décembre). Deux nuances obligatoires : (1) « réembauche » est impropre : CBA a offert le retour en option, le nombre de retours effectifs n'a jamais été publié, et le syndicat attendait un nombre élevé de départs ; (2) le qualificatif « échec » vaut pour la tentative immédiate, pas pour la trajectoire 2026. Le KO sentence du blueprint (« trois entreprises ont remplacé des humains par l'IA, toutes les trois les ont réembauchés ») doit être reformulé : « **deux** ont fait machine arrière publiquement (CBA, avec retour optionnel non quantifié ; Klarna/IBM nuances ailleurs), et la pression de substitution a persisté après coup ».

**Faits clés** : FCT-001 à FCT-011 (détail §11). **Gap central** : aucun chiffre public du taux de retour effectif ni du coût du retournement (GAP-001).

## 2. MANIPULATION_REPORT

| Symbole | Score | Observation nommée |
|---|---|---|
| Ξ | 5 | Nombre de retours effectifs jamais publié ; coût du retournement absent ; les coupes 2026 (Nutun) nettement moins médiatisées que le « backflip » |
| € | 6 | Bénéfice record 10,25 Md$ (FY2025) pendant les suppressions ; économies visées ; offshoring Inde/SA à moindre coût |
| Λ | 6 | Cadrage institutionnel « error » vs syndical « outright lie » ; « dress up job cuts as innovation » (FSU) ; la justification « réduction de 2 000 appels/semaine » contredite par les faits |
| Ω | 3 | Inversion : la preuve avancée (baisse des appels) est devenue son contraire |
| Ψ | 2 | Angoisse documentée des 45 salariés (stress, factures) |
| ↕ | 5 | Décision unilatérale, consultation insuffisante reconnue, recours Fair Work |
| Φ | 3 | Spectacularisation du « backflip » (médias) vs silence sur la suite |
| Σ | 2 | Récit « investir dans nos gens » vs coupes simultanées |
| Κ | 4 | Façade d'innovation responsable maintenue (Microsoft blog « reimagine ») pendant les coupes 2026 |
| ρ | 6 | FSU : dispute Fair Work, victoire « massive », documentation des volumes réels |
| κ | 1 | Non établi |
| ⫸ | 6 | CBA, ANZ, NAB, Bendigo, Visa, Mastercard, Microsoft : vague convergente de coupes liées IA 2025-2026 |
| ⚔ | 0 | Aucune coordination organisée établie |
| 🌐 | 3 | Réseau CBA-Microsoft-OpenAI-Nutun-filiale Inde |
| ⏰ | 3 | Séquence serrée : annonce 28/07 → retournement 21/08 → coupes 2026 |

CLUSTERS chargés : ICEBERG, MONEY, FRAMING, POWER, RESISTANCE, FRAGMENTATION. PATTERNS : @PAT[ICEBERG] (rétention d'information), @PAT[FASC] (convergence sectorielle). THREATS : aucune signature @THR majeure ; @THR[SHOCK] non retenu (pas de péril personnel documenté).

## 3. CLUSTERS (diagnostic)

- **ICEBERG (Ξ=5)** : la partie visible (45 postes, retournement) masque la masse invisible (centaines de postes Nutun 2026, 176 postes tech, 800 rôles/an selon FSU). ICEBERG_FACTOR = NON COMPUTABLE (dénominateur global des effectifs de support CBA non public).
- **MONEY (€=6)** : flux : CBA (bénéfice 10,25 Md$) → économie de coûts → externalisation Nutun/Inde. 2 000 embauches récentes « dont beaucoup en Inde » (Comyn, ABC). La substitution joue par les prix du travail, pas seulement par l'IA.
- **FRAMING (Λ=6)** : « error » (CBA) vs « lie » (FSU) : le désaccord porte sur l'intention, pas sur les faits (volumes en hausse, rôles non redondants reconnus). Contexte du « backflip » déchargé du récit « l'IA échoue » : le récit 2026 (Microsoft/OpenAI) reprend la même opération ailleurs.
- **POWER (↕=5)** : asymétrie structurelle : décision unilatérale, information détenue par l'employeur, recours coûteux (Fair Work). Le retournement n'est pas une preuve de symétrie.
- **RESISTANCE (ρ=6)** : FSU documenté : constats de terrain (volumes), escalade tribunal, communication. Efficace dans ce cas précis (retournement), borné (ne bloque pas la suite).
- **FRAGMENTATION (⫸=6)** : 7 institutions financières + Microsoft convergent sur des coupes liées IA en 2025-2026 ; indépendance des sources (ABC, Reuters, Bloomberg, ACS) établie, pas de source commune unique.

## 4. HERMÉNEUTIQUE (L1-L6)

- L1 : CBA a annoncé 45 suppressions liées au voice-bot (28/07/2025). FAIT (FCT-001).
- L2 : CBA a fait machine arrière, présenté des excuses et qualifié l'annonce d'« error » (21/08/2025). FAIT (FCT-002).
- L3 : la justification (baisse des appels) est contredite par les volumes en hausse, reconnue par CBA au tribunal (« This error meant the roles were not redundant »). FAIT (FCT-003, FCT-004).
- L4 : l'intention (« mensonge » vs « erreur ») n'est pas tranchable depuis les sources publiques : le syndicat affirme, la banque reconnaît un défaut d'évaluation. HYPOTHESIS, non prouvé (FCT-005).
- L5 : la substitution s'est poursuivie hors périmètre onshore (chat Nutun 2026, Hey CommBank 9/10). FAIT (FCT-008).
- L6 : l'effet net sur l'emploi CBA est non mesurable (GAP-001).

## 5. FORENSIC REASONING (montré / omis / reconstruction)

- **Montré** : chronologie complète (annonce → retournement → 2026), extraits verbatim ABC/Ars/FSU, chiffres de volumes, bénéfice record, option de retour.
- **Omis par les sources publiques** : nombre de salariés effectivement revenus ; coût direct du retournement ; montant des indemnités de départ ; détail des critères de redondance ; l'ampleur exacte des coupes 2026 (Bloomberg cité, chiffre « hundreds » non précisé).
- **Reconstruction (interdite ici)** : aucun chiffre de « retour » n'est reconstruit : GAP-001 explicite. Le corpus legacy « réembauche » était une reconstruction abusive : remplacée par « retour proposé en option, non quantifié ».

## 6. PRISME DIALECTIQUE

- **⟐ Position dominante (CBA/Microsoft)** : « erreur ponctuelle d'évaluation, corrigée ; notre investissement IA rend service aux clients ; l'emploi se déplace vers des tâches à plus haute valeur ». Support : déclarations publiques CBA, blog Microsoft, embauches récentes (mais largement en Inde).
- **⟐̅ Position critique la plus forte (FSU)** : « l'IA a servi de couverture à des coupes de coûts et à un pivot vers l'offshoring ; la victoire ne compense pas le stress et ne bloque pas la suite ». Support : volumes constatés, admissions CBA, coupes 2026, revendication 176 postes tech. La force de la position FSU tient aux admissions mêmes de CBA (FCT-003/004), pas à sa seule rhétorique.
- **Arbitrage par la preuve** : sur les faits (volumes, redondance), CBA et FSU convergent après le retournement (les deux reconnaissent la non-redondance). Le désaccord résiduel porte sur l'intention (erreur vs mensonge) : non tranchable (L4). Sur la trajectoire, les faits 2026 (Nutun, chat IA) donnent raison à la vigilance syndicale : la substitution a eu lieu hors du périmètre contesté.

## 7. CHRONOLOGIE

| Date | Événement | Source |
|---|---|---|
| fin 2024 | Lancement de « Hey CommBank », premier chatbot bancaire génératif australien | ACS |
| ~28/07/2025 | CBA annonce 45 suppressions (direct banking) liées au voice-bot ; FSU dénonce ~90 rôles au total | ABC, Reuters (snippet) |
| 29/07/2025 | Reuters : backlash syndical | Reuters (snippet, 401) |
| ~20-21/08/2025 | Retournement : CBA s'excuse auprès des 45, « error », rôles non redondants ; options retour/redéploiement/départ ; FSU « massive win » | ABC, Ars, Bloomberg |
| 21/08/2025 | FSU : « damage already done », Angrisano : « dress up job cuts as innovation » | ABC, Ars |
| semaine ~14/08/2025 | Partenariat CBA-OpenAI (détection fraude) annoncé | Ars |
| mai 2026 | Hey CommBank résout ~9 conversations sur 10 sans humain | ACS |
| 09/07/2026 | FSU interpelle CBA (nouvelle dispute) | fsunion (snippet) |
| 30/07/2026 | ACS : centaines de postes chat support coupés via Nutun (Johannesburg) ; 176 postes tech selon FSU ; ~800 rôles en un an | ACS |

## 8. DOMAINES

- **Emploi/substitution** : échec immédiat onshore (45) + succès différé hors périmètre (chat 9/10, Nutun). L'unité pertinente n'est pas « l'entreprise » mais « le canal ».
- **Relations industrielles** : le Fair Work Commission comme dernier rempart effectif ; la consultation insuffisante reconnue par CBA ; la victoire procédurale ne crée pas de droit de regard permanent.
- **Offshoring** : Inde (embauches tech, 2 000 « dont beaucoup en Inde »), Afrique du Sud (Nutun). L'IA et l'offshoring avancent ensemble : le récit « IA vs humain » masque « IA + coûts du travail ».
- **Récit médiatique** : le « backflip » a saturé l'attention (juillet-août 2025) ; les coupes 2026 sont passées quasi inaperçues (Φ).

## 9. RÉSEAU D'ACTEURS

| Acteur | Rôle | Action documentée | Source | Intent |
|---|---|---|---|---|
| CBA | Employeur ◈ | Annonce 45 coupes, retournement, excuses ; partenaire Microsoft/OpenAI | ABC, Ars, ACS | CLAIMED |
| FSU | Syndicat 🔥 | Dispute Fair Work, documentation volumes, victoire, alertes 2026 | Ars, ABC, ACS | CLAIMED |
| Fair Work Commission | Tribunal ◈ | Arbitre la dispute ; reçoit l'admission CBA | Ars | N/A |
| Microsoft | Fournisseur ◈ | Plateforme IA 2 M conversations/mois ; blog « reimagine » | ACS | CLAIMED |
| OpenAI | Fournisseur ◈ | Partenariat fraude (2025) | Ars | CLAIMED |
| Nutun | Sous-traitant (SA) | Fournissait les contractants du chat ; coupes 2026 | ACS (via Bloomberg) | UNKNOWN |
| Bloomberg Intelligence | Analyste ◉ | Estimation 200 000 emplois bancaires mondiaux 3-5 ans | Ars | N/A |
| Salariés (45) | Affectés | Choix retour/redéploiement/départ ; stress | ABC, Ars | UNKNOWN |

CONTROL_MAP : la décision d'effectif relève de la direction ; le contrôle externe passe par le tribunal du travail (ex post) ; aucune obligation de suivi post-coupes (taux de retour non publié) ; l'information sur les volumes (justification des redondances) est détenue par l'employeur.

## 10. CHAÎNES / PELOTE (mécanismes de l'objet)

CAUSAL_ROUTE=REQUIRED. Recherche effectuée, arrêt à la preuve.

- **CAU-001 Sous-estimation des volumes → non-redondance (SUPPORTED)** : CBA justifie les redondances par la baisse attendue des appels ; les volumes montent ; CBA admet au tribunal n'avoir pas considéré que la hausse se poursuivrait → rôles non redondants → retournement. Enchaînement admis par l'employeur lui-même (FCT-003/004). Type : MECHANISM.
- **CAU-002 Substitution déplacée hors périmètre (SUPPORTED)** : le chat IA (9/10 résolutions) et l'externalisation Nutun absorbent le travail de support hors call centre onshore ; la suppression physique des postes suit avec un décalage. Type : MECHANISM, partiellement sourcé (ACS/Bloomberg).
- **CAU-003 L'IA comme couverture de coupes de coûts (HYPOTHESIS, syndicale)** : FSU : « cynical cost-cutting exercise » et pivot Inde/SA. Élément de support : bénéfice record + embauches offshores + admissions. Intention non démontrée (L4). Type : ENABLER, statut HYPOTHESIS.
- **CAU-004 Amplification sectorielle (CONTEXT)** : Bloomberg Intelligence 200 000 emplois bancaires mondiaux ; ANZ ~3 500 ; Microsoft 50k→40k : l'événement CBA s'inscrit dans une vague convergente, pas un cas isolé (FCT-010/011). Type : CONTEXT.
- **GAP-001** : aucun chiffre public du taux de retour ni du coût du retournement → effet net sur l'emploi CBA non mesurable.

SOURCE_PROVENANCE du récit « 3 échecs sur 3 » : synthèse T3 du corpus (Klarna/CBA/IBM) → cas CBA vérifié ici avec deux corrections (date juillet-août 2025 ; « réembauche » = retour optionnel non quantifié) ; le « 3 sur 3 » devient « 3 retours en arrière documentés, dont 1 réembauche complète revendiquée (Klarna) et 1 retour optionnel non quantifié (CBA) ».

## 11. CARTE DES PREUVES

### FACT_REGISTRY_V1

`FCT-001 | FACT | ✦ | https://www.abc.net.au/news/2025-08-21/cba-backtracks-on-ai-job-cuts-as-chatbot-lifts-call-volumes/105679492 + Reuters (snippet) | ABC◈+Reuters○ | 2025-07-28 | cba-full-automation-echoue | CBA annonce ~45 suppressions de postes service client (direct banking) liées au « voice-bot » IA ; FSU dénonce ~90 rôles au total | mem:-`

`FCT-002 | FACT | ✦ | ABC + Ars (https://arstechnica.com/tech-policy/2025/08/bank-forced-to-rehire-workers-after-lying-about-chatbot-productivity-union-says/) | ABC◈+Ars◈ | 2025-08-21 | cba-full-automation-echoue | Retournement : CBA s'excuse auprès des 45, qualifie la décision d'« error », reconnaît des rôles non redondants ; options retour/redéploiement/départ ; FSU « massive win » | mem:-`

`FCT-003 | FACT | ✦ | ABC + Ars | ABC◈+Ars◈ | 2025-08-21 | cba-full-automation-echoue | Volumes d'appels en hausse (overtime, team leaders aux téléphones) ; CBA avait justifié les coupes par une baisse de 2 000 appels/semaine | mem:-`

`FCT-004 | FACT | ✧ | Ars (admission au tribunal Fair Work) | Ars◈ | 2025-08-21 | cba-full-automation-echoue | Admission CBA : « This error meant the roles were not redundant » ; la banque n'avait pas considéré la poursuite de la hausse des appels | mem:-`

`FCT-005 | EVIDENCE | ✧ | Ars (déclaration FSU rapportée) | Ars◈ | 2025-08-21 | cba-full-automation-echoue | FSU qualifie la justification de « outright lie » et allègue des recrutements de rôles similaires en Inde ; intention non démontrée | mem:-`

`FCT-006 | FACT | ✧ | ABC + Ars | ABC◈+Ars◈ | 2025-08-21 | cba-full-automation-echoue | Nombre de retours effectifs jamais publié ; FSU s'attend à un nombre élevé de départs | mem:-`

`FCT-007 | FACT | ✧ | ABC | ABC◈ | 2025-08-21 | cba-full-automation-echoue | Bénéfice record CBA 10,25 Md$ (FY2025) ; ~2 000 embauches récentes « dont beaucoup en Inde » (Comyn) | mem:-`

`FCT-008 | FACT | ✧ | ACS (https://ia.acs.org.au/article/2026/ai-drives-fresh-commbank-job-cuts.html) | ACS◈ (Bloomberg cité) | 2026-07-30 | cba-full-automation-echoue | 2026 : centaines de postes chat support coupés via Nutun (Johannesburg) ; plateforme IA Microsoft 2 M conversations/mois ; Hey CommBank résout ~9 conversations sur 10 sans humain (mai 2026) | mem:-`

`FCT-009 | EVIDENCE | ✧ | ACS (déclaration FSU) | ACS◈ | 2026-07-30 | cba-full-automation-echoue | FSU : 176 postes tech/ingénierie supplémentaires envisagés (certains republiés via filiale Inde) ; ~800 rôles CBA supprimés en un an | mem:-`

`FCT-010 | FACT | ✧ | Ars (Bloomberg Intelligence) | Ars◈ | 2025 | cba-full-automation-echoue | Estimation Bloomberg Intelligence : jusqu'à 200 000 emplois bancaires mondiaux supprimés d'ici 3-5 ans sous l'effet de l'IA | mem:-`

`FCT-011 | FACT | ✧ | ACS | ACS◈ | 2026-07-30 | cba-full-automation-echoue | Contexte sectoriel : Microsoft service client 50k→40k ; ANZ ~3 500 rôles ; Visa −7 % (~2 600) ; Mastercard ~4 % | mem:-`

`FCT-012 | CLAIMED | ⁅ | Reuters (401, snippet) | Reuters○ | 2025-07-29 | cba-full-automation-echoue | Annonce Reuters : ~90 rôles supprimés selon le syndicat (dont 45 direct banking) ; page inaccessible en session | mem:-`

Aucun write-back Mnemolite (outil paramétré indisponible) ; mem:- conservé.

### CONTRADICTION_LEDGER

1. **Justification CBA (baisse des appels) vs faits (hausse)** : contredite par CBA elle-même après coup ; résolue par admission (FCT-003/004).
2. **Corpus « réembauche » vs sources** : le corpus présentait CBA comme « réembauché les 45 » ; les sources documentent une offre de retour en option, non un retour effectif. Correction actée (FCT-006).
3. **« Échec » vs « succès différé »** : le retournement 2025 et les coupes 2026 ne sont pas contradictoires mais séquentiels : échec du canal onshore immédiat, substitution réussie du canal chat à terme.
4. **Reuters « 90 rôles » vs CBA « 45 »** : périmètre syndical vs périmètre banque ; non résolu (Reuters inaccessible, FCT-012 ⁅).

### TRACE_MATRIX (extrait)

| FCT | QRY/SRC | REFUTATION_SEARCHED | Résultat |
|---|---|---|---|
| FCT-001/002 | QRY-1 (annonce) + QRY-2 (backtrack) | QRY-3 « CBA chatbot 45 réembauche contredit » | NONE (ABC, Bloomberg, Ars, Yahoo concordants) |
| FCT-003 | QRY-2 | QRY-4 « CBA call volumes decrease chatbot proof » | NONE (hausse documentée) |
| FCT-008 | QRY-5 (ACS 2026) | QRY-6 « CommBank 2026 job cuts AI contredit » | NONE |
| FCT-010 | QRY-2 | QRY-7 « Bloomberg 200000 jobs banks AI » | NONE (estimation concordante) |

### EDI

Familles : A ◈ (CBA, Microsoft), C 🔥 (FSU), D (ACS, Ars, ABC = presse d'investigation ; Bloomberg Intelligence = analyste). B (concurrents) absent ; E (académique) absent. GAP EDI B/E documenté ; les faits centraux reposent sur au moins deux familles indépendantes inspectées (ABC/Ars ; ABC/ACS).

## 12. CARTE DIALECTIQUE

- **Scénario 1 (lecture optimiste)** : le retournement CBA prouve que le full automation se heurte à la réalité des volumes ; les banques apprennent, la consultation s'améliore, l'emploi se redéploie (Comyn : « people have migrated to higher-value work »). Faiblesse : les coupes 2026 et l'absence de mesure du redéploiement contredisent la confiance.
- **Scénario 2 (lecture pessimiste)** : le retournement est une péripétie de surface ; la substitution continue par d'autres canaux (chat, offshoring), moins visibles et sans tribune ; les 200 000 emplois Bloomberg matérialisent la trajectoire. Faiblesse : extrapolation sectorielle, CBA reste très rentable et embauche (même en Inde).
- **Scénario 3 (lecture forensique, retenue ici)** : ce que documente réellement le cas, c'est un **déplacement de canal et de juridiction** : l'IA ne « supprime » pas l'emploi d'un bloc, elle le déplace vers les canaux automatisables et les pays à bas coût, avec des effets différés et mal mesurés. La variable décisive n'est pas la performance de l'IA (le chat à 9/10 fonctionne) mais la **localisation et la comptabilisation** des postes.

## 13. PÉRIMÈTRE & LIMITES

**Inclusions** : séquence CBA 2024-2026, relations industrielles, offshoring, contexte sectoriel. **Exclusions** : Klarna/IBM (autres dossiers), finances détaillées CBA, droit du travail australien exhaustif. **Limites d'accès** : Reuters 401 (snippet), Bloomberg paywall (citée via Ars/ACS), nombre de retours effectifs non publié, « hundreds » de postes Nutun non chiffré exactement, données de volumes non auditées (constats syndicaux). **Limites de méthode** : l'attribution d'intention (erreur vs mensonge) est hors de portée des sources publiques (L4) ; la revendication « 800 rôles en un an » est syndicale et non auditée par une source indépendante.

## 14. ÉTAT DES CONNAISSANCES

| Statut | Contenu |
|---|---|
| CONNU | Annonce 45, retournement, excuses, non-redondance reconnue, options offertes, coupes 2026 Nutun, chat 9/10, bénéfice record |
| PROBABLE | Volumes en hausse au moment des coupes (constats FSU + admission CBA) ; poursuite de la substitution par canal/juridiction |
| ALLÉGUÉ | « Outright lie » ; recrutements de rôles similaires en Inde ; 176 postes tech ; ~800 rôles/an |
| HYPOTHÈSE | L'IA comme couverture de coupes de coûts (intention) |
| INCONNU | Taux de retour effectif, coût du retournement, ampleur exacte des coupes Nutun |
| RÉFUTÉ | « CBA a réembauché les 45 » (au sens de réintégration effective démontrée) : non démontré, remplacé par « retour proposé en option » |

## 15. SUSPICION / VÉRIFICATION

- **Sources auditées** : ABC (public, reportage nommé), Ars (enquête, citations Bloomberg), ACS (journalisme spécialisé, Bloomberg cité), FSU (syndicat, intérêt militant assumé). Aucune fabrique de citation détectée ; les citations sont datées et attribuées.
- **STATUS_DELTA** : FCT-006 : « réembauche » (corpus) → « retour optionnel non quantifié » (vérifié). FCT-001 : date corrigée (juillet-août 2025, pas décembre 2025).
- **Checks restants** : taux de retour (jamais publié, GAP), chiffre exact des coupes Nutun (Bloomberg, paywall), revendications FSU 2026 (à confirmer par source indépendante).
- **Verdict d'ensemble** : cas vérifié, intégré à l'Acte II de l'Option A′ avec les deux corrections obligatoires (date, « retour en option ») et la nuance « échec immédiat / persistance différée ».

## SOURCES

1. ABC News, Stephanie Chalmers, « Commonwealth Bank backtracks on AI job cuts, apologises for 'error' as call volumes rise », 21/08/2025 (INSPECTÉ) : https://www.abc.net.au/news/2025-08-21/cba-backtracks-on-ai-job-cuts-as-chatbot-lifts-call-volumes/105679492
2. Ars Technica, Ashley Belanger, « Bank forced to rehire workers after lying about chatbot productivity, union says », 21/08/2025 (INSPECTÉ) : https://arstechnica.com/tech-policy/2025/08/bank-forced-to-rehire-workers-after-lying-about-chatbot-productivity-union-says/
3. ACS Information Age, Denham Sadler, « AI drives fresh CommBank job cuts », 30/07/2026 (INSPECTÉ) : https://ia.acs.org.au/article/2026/ai-drives-fresh-commbank-job-cuts.html
4. Reuters, « Australian lender CBA to cut 45 jobs in AI shift, draws union backlash », 29/07/2025 (401 en session ; snippet conservé) : https://www.reuters.com/business/world-at-work/australian-lender-cba-cut-45-jobs-ai-shift-draws-union-backlash-2025-07-29/
5. Bloomberg, « Australia's Biggest Bank Reverses Plan to Replace Jobs With AI Chatbots », 20/08/2025 (paywall ; cité via Ars/ACS) : https://www.bloomberg.com/news/articles/2025-08-21/commonwealth-bank-reverses-job-cuts-decision-over-ai-chatbots
6. Yahoo Finance AU (snippet) : https://au.finance.yahoo.com/news/commonwealth-bank-backflips-on-controversial-axing-of-dozens-of-jobs-for-ai-chatbot-massive-win-for-workers-221239241.html
7. Finance Sector Union (snippet) : https://www.fsunion.org.au/cba-backflips-on-ai-cuts-but-the-threat-remains/

## REQUEST_LOG

| # | Type | Cible | Résultat |
|---|---|---|---|
| 1 | @WEB | CBA chatbot 45 jobs rehired apology | ABC identifié (position 1) |
| 2 | @WEB | CBA call centre AI 45 rôles | Reuters, ABC, Bloomberg, Yahoo identifiés |
| 3 | @FETCH | ABC News 21/08/2025 | 200, INSPECTÉ |
| 4 | @FETCH | ACS Information Age 30/07/2026 | 200, INSPECTÉ |
| 5 | @FETCH | Reuters 29/07/2025 | 401 FORBIDDEN → GAP ACCESS, snippet conservé |
| 6 | @FETCH | Ars Technica 21/08/2025 | 200, INSPECTÉ |
| 7 | @WEB | réfutation (contredit/révision) | NONE |
| 8 | @WEB | Bloomberg 200k emplois bancaires | estimation concordante |
| 9 | @MNEMO_Q | recherche mémoire | ÉCHEC paramètres (session) → MNEMO_UNAVAILABLE |

**Gate 19a (exécuté 14h03 UTC) :** verdict **BLOCKED** (branche protégée main). Checks : naming PASS, no-em-dash PASS (67 fichiers, 0 occurrence), tests extractors PASS. state_id `46a85b6de765a2d7ed73d18a00651884ae046ee8cd45bb69d0f789bbe7b4aa4f`. Aucune certification de livraison sur main : worktree requis (voir P0-01).

---
*Fin du dossier. Corrections apportées au corpus : date (juillet-août 2025), « retour en option » ≠ « réembauche », nuance « échec immédiat / persistance différée ».*
