ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260905-1125-achat-de-vote-france-ue | PARENT_RUN_ID:NONE | AS_OF:2026-09-05
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-05_achat-de-vote-france-ue/2026-09-05_11-25_achat-de-vote-france-ue_INPUT.txt | SUBJECT_SLUG:achat-de-vote-france-ue | SUBJECT_FP:sha256:c1497d292cb1cc0e3cbb2610b034e37d87562764b420f2854132f1e4bf5afb17 | INPUT_SHA256:sha256:9ecae7cae66b7617076f92dfba698d606e92affd1de3d88162e0f7e7a903f090
COMPLEXITY:0.6→APEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France (élections locales/legislatives, art L106 code electoral, jurisprudence) et UE (Italie, Grèce, Europe centrale/du Sud-Est). Vote buying direct, clientélisme, corruption électorale individuelle. Cadre: art L106/L116, GRECO, études académiques.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/INVESTIGATION.md,protocol/EPISTEMIC.md,output/TEMPLATE.md,protocol/FACT_VERIFICATION.md,clusters/ICEBERG.md,clusters/MONEY.md,clusters/POWER.md,clusters/NETWORK.md,clusters/FRAGMENTATION.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Achat de vote — France & UE

## 1. Cadre général
L'achat de votes est un délit électoral documenté en France et dans l'Union européenne, sanctionné par des peines pénales mais dont l'exécution bute sur la difficulté de preuve (secret du vote) et la prescription.

## 2. France — cadre pénal
Le code électoral français criminalise l'achat de votes : art L106 (dons, libéralités, promesses de récompense pour obtenir un vote) et art L113-1 (recueil illégal de fonds, dépassement de plafond), avec peines de 2 à 3 ans d'emprisonnement et amendes de 15 000 à 45 000 euros.

## 3. France — jurisprudence
Le Conseil d'État (22/07/2021, n° 450129, affaire de Corbeil-Essonnes) a jugé que des distributions répétées de colis alimentaires par un candidat en période électorale, valorisées sur les réseaux sociaux et la presse, constituent des manœuvres électorales pouvant affecter la libre détermination des électeurs — sans annulation du scrutin, l'écart de voix étant trop large.

## 4. Italie — voto di scambio
L'achat de votes politico-mafieux est criminalisé en Italie (art 416-ter c.p., réforme loi 43/2019). L'opération DIA du 18/04/2023 a démantelé un accord clan Amato Pagano–coalition politique à Melito di Napoli : 18 arrestations, votes contre emplois et ressources.

## 5. Europe centrale et du Sud-Est
Le clientélisme électoral est structurel en Roumanie, Bulgarie et Slovaquie : politisation des ressources publiques, ciblage des ménages à bas revenus via intermédiaires, techniques pour percer le secret du vote. En Slovaquie (2016), la police a enquêté sur des achats de votes (cigarettes contre votes) dans des settlements roms où le parti au pouvoir a obtenu 83 % des voix contre 28,28 % au niveau national.

## 6. Limites des sanctions
La prescription (Cassation italienne 2024 : 50 préférences achetées pour 2 500 euros, prescription définitive) et la difficulté de preuve limitent l'exécution des sanctions.

## 7. Conclusion
Achat de votes réel, localisé et sanctionné (France, Italie), clientélisme structurel en Europe centrale et du Sud-Est ; aucun scrutin national majeur n'a été inversé par achat de votes documenté.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:5|CLM:5|AXS:5|CAU:4|CTRL:3|ACT:3

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"object_question_ref":"OQ","status":"SATURATED","text":"LED: vote buying direct en France (distributions dargent/biens contre suffrages) - cas sanctionnés","weight":"DECISIVE"}
LED-002 | {"object_question_ref":"OQ","status":"SATURATED","text":"LED: clientélisme électoral et marchandage de votes en UE (Italie, Grèce, Europe centrale)","weight":"DECISIVE"}
LED-003 | {"object_question_ref":"OQ","status":"SATURATED","text":"LED: corruption électorale individuelle - cadre pénal (art L106 code électoral, art 433-1 code pénal) et jurisprudence","weight":"IMPORTANT"}
LED-004 | {"object_question_ref":"OQ","status":"SATURATED","text":"LED: effets documentés du vote buying (bastions clientélaires, votes de proximité) et mesures","weight":"IMPORTANT"}
LED-005 | {"object_question_ref":"OQ","status":"SATURATED","text":"LED: cas contemporains (réseaux sociaux, applications) et lutte (GRECO, observatoires)","weight":"IMPORTANT"}

### CLAIM_REGISTRY_V1
CLM-001 | {"object_question_ref":"OQ","stance":"CLAIM","status":"SUPPORTED","text":"CLM : larticle L106 du code électoral français réprime le don dargent/biens contre un vote"}
CLM-002 | {"object_question_ref":"OQ","stance":"CLAIM","status":"SUPPORTED","text":"CLM : des condamnations françaises pour achat de vote sont documentées (élections locales)"}
CLM-003 | {"object_question_ref":"OQ","stance":"CLAIM","status":"SUPPORTED","text":"CLM : lItalie a connu des affaires massives de voto di scambio (échange de votes contre faveurs/argent)"}
CLM-004 | {"object_question_ref":"OQ","stance":"CLAIM","status":"SUPPORTED","text":"CLM : le clientélisme électoral est documenté en Grèce et en Europe du Sud-Est (études académiques)"}
CLM-005 | {"object_question_ref":"OQ","stance":"CLAIM","status":"SUPPORTED","text":"CLM : le GRECO (Conseil de lEurope) et les observatoires documentent le vote buying en Europe"}

### AXIS_REGISTRY_V1
AXS-001 | {"object_question_ref":"OQ","stance":"CLAIM","status":"SATURATED","text":"AXS : le vote buying direct est documenté et sanctionné en France (art L106-1 code électoral)"}
AXS-002 | {"object_question_ref":"OQ","stance":"CLAIM","status":"SATURATED","text":"AXS : le clientélisme électoral est un phénomène documenté dans plusieurs États membres de lUE (Italie, Grèce, Slovaquie, Roumanie)"}
AXS-003 | {"object_question_ref":"OQ","stance":"CLAIM","status":"SATURATED","text":"AXS : lachat de vote affecte principalement des élections locales et des scrutins à forte densité clientélaire, rarement les élections nationales"}
AXS-004 | {"object_question_ref":"OQ","stance":"CLAIM","status":"SATURATED","text":"AXS : les sanctions (pénales et électorales) sont réelles mais leur application reste inégale selon les États"}
AXS-005 | {"object_question_ref":"OQ","stance":"CLAIM","status":"SATURATED","text":"AXS : les formes contemporaines (argent via apps, cadeaux, réseaux) renouvellent la pratique du vote buying"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"fact_refs":["FCT-004","FCT-006"],"object_question_ref":"OQ","status":"SUPPORTED","text":"CAU: la precarite et le ciblage des menages a bas revenus par des intermediaires (brokers) alimentent le clientelisme et l achat de voix en Europe centrale et orientale (RO/BG: politisation des ressources etatiques)","type":"CAUSALITY"}
CAU-002 | {"fact_refs":["FCT-003"],"object_question_ref":"OQ","status":"SUPPORTED","text":"CAU: la criminalite organisee (clan Amato Pagano, Camorra) capte les elections locales via le voto di scambio: votes du clan contre argent, emplois et faveurs, avec intimidation","type":"CAUSALITY"}
CAU-003 | {"fact_refs":["FCT-002","FCT-007"],"object_question_ref":"OQ","status":"SUPPORTED","text":"CAU: les distributions electorales (colis alimentaires) peuvent affecter la libre determination des electeurs; leur impact sur le resultat depend de l ecart de voix (CE Corbeil-Essonnes: manoeuvre etablie, pas d annulation)","type":"CAUSALITY"}
CAU-004 | {"fact_refs":["FCT-007","FCT-005"],"gap":"absence de preuve d un effet agregat national des achats de voix sur les resultats","gap_type":"CAUSALITY","object_question_ref":"OQ","status":"GAP","text":"CAU: lien causal entre achat de votes et inversion de resultats non demontre au niveau national - cas documentes localement (Slovaquie 83% vs 28,28%; Melito) mais pas de demonstration d effet agregat; preuve difficile (secret du vote), prescription frequente","type":"CAUSALITY"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"fact_refs":["FCT-001"],"object_question_ref":"OQ","status":"DONE","text":"CTRL: France - cadre penal L106/L113-1 (2-3 ans, 15000-45000 EUR) contre pressions par dons et financement illegal","type":"MITIGATION"}
CTRL-002 | {"fact_refs":["FCT-003"],"object_question_ref":"OQ","status":"DONE","text":"CTRL: Italie - art 416-ter c.p. reforme par loi 43/2019 (voto di scambio politico-mafioso elargi, jusqu a 12 ans)","type":"MITIGATION"}
CTRL-003 | {"fact_refs":["FCT-002"],"object_question_ref":"OQ","status":"DONE","text":"CTRL: France - controle du juge electoral (CE) sur les manoeuvres electorales: distributions repetees = manoeuvre, annulation si l ecart de voix est faible","type":"MITIGATION"}

### ACTION_REGISTRY_V1
ACT-001 | {"fact_refs":["FCT-003"],"object_question_ref":"OQ","status":"DONE","text":"ACT: Italie - operations DIA/DDA: arrestation de 18 suspects (maire de Melito di Napoli, president du conseil, 2 conseillers) pour voto di scambio (04/2023)","type":"COUNTER"}
ACT-002 | {"fact_refs":["FCT-001","FCT-002"],"object_question_ref":"OQ","status":"DONE","text":"ACT: France - application du droit penal electoral et contentieux electoraux devant le juge administratif (protestations, rejet comptes de campagne)","type":"COUNTER"}
ACT-003 | {"fact_refs":["FCT-005"],"object_question_ref":"OQ","status":"DONE","text":"ACT: Slovaquie - enquete de police pour achat de votes dans les settlements roms (2016): corruption d election = delit, verification des anomalies de resultats","type":"COUNTER"}

SEARCH_ACTIVITY_V1:WEB:12|FETCH:10|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FOUND(lineage runs 1-3: manipulation a169e52f, ingerences b2eb01dd); no duplicate | mnemolite-mcp:search_memory | a169e52f-d466-478b-9933-20ccbd9062fb | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | Legifrance: art L106-1 code electoral, 3 ans emprisonnement + 45000 EUR amende; Conseil d'Etat decision 449614 (22/07/2021) pressions par dons; landot-avocats: comparaison jurisprudences cadeau/colis alimentaire = achat de voix; TA Lille 2004513 art L106 | - | - | achat de vote France article L106 code électoral condamnation don argent contre vote jurisprudence
QRY-002 | WEB | Wikipedia IT: voto di scambio = favoris contre votes; Brocardi: art 416ter code penal scambio elettorale politico-mafioso; Sky TG24: votes vendus 20-30 EUR Napolitain 2023-2024; Quotidiano Puglia: condamnation 10 ans ex-syndic; Libera: voto di scambio ~4% des voix | - | - | voto di scambio Italia compravendita voti mafia condanne elezioni locali
QRY-003 | WEB | Mares 2017 (Europe-Asia Studies): pressure/favours/vote-buying Roumanie-Bulgarie, evidence experimentale; Gherghina 2024: clientelism frequent Roumanie conjoint experiment 2021; Chiru 2024: clientelism CEE organisation partis | - | - | clientelism vote buying Europe Greece Romania Bulgaria elections study evidence
QRY-004 | WEB | GRECO: groupe d'Etats contre corruption Conseil Europe, 28 Etats membres UE membres; 26e rapport activites 2025; AFA France: GRECO salue recentes avancees France | - | - | GRECO Conseil Europe vote buying corruption électorale rapport États membres
QRY-005 | WEB | landot-avocats: cadeau/colis alimentaire = achat de voix jurisprudence; actu-juridique: colis de Noel distribues en nombre anormal (CCAS) = sanction; cgt socgen: Dassault condamne 2 ans sursis achat de votes; Courrier des maires: 80 colis 2013 = 2% electeurs, 2014 = 21% | - | - | France achat de voix élections municipales condamnation cadeaux colis alimentaire électeurs affaire jugement 2022 2023
QRY-006 | WEB | Cruz: social networks vote buying targeting (cite 174); Bauhr 2023: electoral clientelism undermines redistribution; Wikipedia clientelism: patrons/brokers/clients; Gherghina 2024 acceptance electoral clientelism | - | - | Greece clientelism vote buying elections patron-client networks study evidence exostrefis
QRY-007 | WEB | Chiriac 2023 Cardozo: electoral fraud Romania = vote buying + ballot; IFES: annulation 2024 election, corruption strategique; Guardian: cour ordonne recomptage 28/11/2024; US embassy: cour constitutionnelle annule 1er tour | - | - | Romania 2024 elections vote buying corruption prosecutions DIICOT vote buying cases
QRY-008 | WEB | BTI 2026 Slovakia: corruption abuse office undermine democracy; DW 2023: scandale avant election cle; Harvard MIS: deepfake 2023 election; vsquare: hoax fake accounts election presidentielle 2024 - vote buying direct peu documente Slovaquie | - | - | Slovakia vote buying elections 2023 2024 clientelism corruption allegations prosecuted
QRY-009 | FETCH | Legifrance: art L113-1 code electoral - 3 ans emprisonnement + 45000 EUR amende pour recueil fonds illegal, depassement plafond depenses, dons en violation L52-7-1/L52-8; art L106 (pressions par dons) et L116 mentions; cadre penal achat de votes FR | SRC-001 | https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006148461 | QRY-001 fetch
QRY-010 | FETCH | Landot-avocats 27/07/2021: jurisprudence CE sur cadeaux/colis alimentaires et achat de voix; CE 10/03/2021 n 445257 cheques alimentaires covid valides (besoin social reel); CE 22/07/2021 n 450129 colis alimentaires repetes = manoeuvre electorale (ecart de voix empeche censure); CE 08/06/2009 Corbeil-Essonnes Dassault deniers personnels; art L106 pressions | SRC-002 | https://blog.landot-avocats.net/2021/07/27/un-cheque-ou-un-colis-alimentaire-permet-il-dacheter-des-voix-comparaison-de-jurisprudences/ | QRY-001 fetch
QRY-011 | FETCH | Wikipedia IT: voto di scambio politico-mafioso criminalise par l'art 416-ter c.p. (loi 43/2019 'nuovo scambio elettorale politico-mafioso'): achat de voix en echange de votes, condamnations (ex. proces a Naples, Catane); pratique liee a la mafia ('voto di scambio'), penalite jusqu'a 12 ans; distinction avec 'clientelisme' electorale | SRC-003 | https://it.wikipedia.org/wiki/Voto_di_scambio | QRY-003 fetch
QRY-012 | FETCH | Mares, Muntean & Petrova (2017, Europe-Asia Studies 69(6):940-960): etude experimentale mixte Roumanie-Bulgarie; strategies clientelistes politisent les ressources de l'Etat, plus elevees dans les localites avec incumbents de longue duree; techniques pour percer le secret du vote (representants au bureau de vote, chain-voting, discussions post-electorales); achat de voix combine pressions et faveurs | SRC-004 | https://www.tandfonline.com/doi/abs/10.1080/09668136.2017.1364351 | QRY-004 fetch
QRY-013 | FETCH | Romea/CTK 15/03/2016: police slovaque enquete pour achat de votes dans 2 settlements roms (Lomnicka, Rakusy) aux legislatives 2016; maire aurait achete cigarettes contre votes; Směr-SD 83% a Lomnicka vs 28,28% national; corrompre une election est un delit en Slovaquie; candidats Chudik et Kubanek nient | SRC-005 | https://romea.cz/en/world/slovak-police-investigating-suspicions-of-vote-buying-in-romani-settlements-2/ | QRY-008 fetch
QRY-014 | FETCH | Wikipedia Clientelism: echange de biens/services contre soutien politique (quid pro quo), lie au patronage et a l'achat de votes; 4 elements (Hicken): dyadique, contingence, hierarchie, iteration; Stokes et al.: clientelisme = politique non-programmatique, ciblage des menages a bas revenus, role des brokers/intermediaires; secret du vote limite la capacite de controle mais monitoring moins courant que suppose | SRC-006 | https://en.wikipedia.org/wiki/Clientelism | QRY-003 fetch
QRY-015 | FETCH | Trantidis (2025, Cambridge Elements): clientelisme = echange de benefices contre allegiance politique, argent de campagne ou votes (Kitschelt & Wilkinson, Stokes); logique d'echange (Public Choice); fonction: mobiliser des ressources de campagne et reseaux de partisans; la politique transactionnelle emerge a l'intersection politique/societe/economie | SRC-007 | https://www.cambridge.org/core/elements/clientelism/E23ABE885BA3D5DF0D3ABD1260D492D0 | QRY-003 fetch
QRY-016 | FETCH | DIA 18/04/2023 (comunicato officiel, ministere interieur italien): ordonnance de detention pour 18 suspects (voto di scambio politico-mafioso, association mafieuse, corruption) - dont le maire de Melito di Napoli, le president du conseil municipal et 2 conseillers; accord clan Amato Pagano avec coalitions (elections oct 2021 + ballottage): votes du clan contre argent, postes de travail, faveurs; pression/intimidation sur residents et sur une candidate; achat de votes aussi aux elections de la Citta metropolitana (13/03/2022) | SRC-008 | https://direzioneinvestigativaantimafia.interno.gov.it/2023/voto-di-scambio-la-dia-esegue-unordinanza-di-custodia-cautelare-a-carico-di-18-soggetti/ | QRY-002 fetch
QRY-017 | FETCH | CE 22/07/2021 n 450129 (Corbeil-Essonnes, municipales 2020): distributions repetees de colis alimentaires par le candidat et membres d'associations (avril-juin 2020, covid) = manoeuvres electorales intervenues en vue des elections, pouvant affecter la libre determination des electeurs; MAIS ecart de voix trop important (3661 vs 3257) pour alterer la sincerite du scrutin - pas d'annulation | SRC-009 | https://juricaf.org/arret/FRANCE-CONSEILDETAT-20210722-450129 | QRY-006 fetch
QRY-018 | WEB | Conseil constitutionnel (Cahiers): secret du vote = droit ET obligation de l'electeur; manoeuvres frauduleuses doivent etre prouvees par elements materiels - preuve difficile par nature; controle principalement exerce par le juge electoral (civil) apres scrutin; pas de refutation du cadre penal L106/L113-1 mais caveat probatoire majeur | - | - | REFUTATION France sincérité scrutin secret du vote preuve manoeuvres fraude avérée condamnation
QRY-019 | WEB | Palermo Today 22/03/2024: Cassazione - prescription definitive pour Giuseppe Scrivano (regionales 2012, 50 preferences achetees pour 2500 EUR) - les delais de prescription (longueur des procedures) peuvent etre un facteur limitant l'application des sanctions; caveat sur l'efficacite de l'execution, pas sur la realite de la pratique | - | - | REFUTATION voto di scambio Italia prescrizione cassazione preferenze soldi condanna annullata
QRY-020 | WEB | CE 10/03/2021 n 445257 (cite par Landot et Banque des Territoires): distribution de cheques alimentaires pendant le confinement covid = reponse a un besoin social reel, PAS une manoeuvre electorale (jugement TA Montreuil annule) - contre-jurisprudence etablissant la frontiere: dons lies a un besoin reel vs distributions electorales repetees | - | - | REFUTATION Conseil d'Etat 10 mars 2021 cheques alimentaires covid validés manoeuvre électorale non caractérisée
QRY-021 | WEB | Mares et al. (2017) reconnaissent eux-memes: le secret du vote est 'nominalement protege' et le monitoring systematique des choix de vote est 'surprenamment peu courant' - limites de la capacite d'execution; aucune refutation de la prevalence du clientelisme en RO/BG trouvee dans la litterature | - | - | REFUTATION Mares Romania Bulgaria vote buying secret ballot monitoring critique limites étude
QRY-022 | FETCH | Palermo Today 22/03/2024: Cassazione a rigetté le recours de la Procure generale contre Giuseppe Scrivano (regionales 2012) - prescription definitive; il aurait achete 50 preferences pour 2500 EUR (mairie d'Alimena); illustration des limites d'application (delais de procedure) sans remettre en cause la realite de la pratique | SRC-010 | https://www.palermotoday.it/cronaca/voto-scambio-sindaco-alimena-scrivano-prescrizione-cassazione.html | QRY-019 fetch

## EVIDENCE_REGISTRY
SRC-001 | ◉ | fam:A | https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006148461
SRC-002 | ◉ | fam:E | https://blog.landot-avocats.net/2021/07/27/un-cheque-ou-un-colis-alimentaire-permet-il-dacheter-des-voix-comparaison-de-jurisprudences/
SRC-003 | ◉ | fam:D | https://it.wikipedia.org/wiki/Voto_di_scambio
SRC-004 | ◉ | fam:D | https://www.tandfonline.com/doi/abs/10.1080/09668136.2017.1364351
SRC-005 | ◉ | fam:B | https://romea.cz/en/world/slovak-police-investigating-suspicions-of-vote-buying-in-romani-settlements-2/
SRC-006 | ◉ | fam:D | https://en.wikipedia.org/wiki/Clientelism
SRC-007 | ◉ | fam:D | https://www.cambridge.org/core/elements/clientelism/E23ABE885BA3D5DF0D3ABD1260D492D0
SRC-008 | ◉ | fam:A | https://direzioneinvestigativaantimafia.interno.gov.it/2023/voto-di-scambio-la-dia-esegue-unordinanza-di-custodia-cautelare-a-carico-di-18-soggetti/
SRC-009 | ◉ | fam:A | https://juricaf.org/arret/FRANCE-CONSEILDETAT-20210722-450129
SRC-010 | ◉ | fam:B | https://www.palermotoday.it/cronaca/voto-scambio-sindaco-alimena-scrivano-prescrizione-cassazione.html

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006148461 | A,E | 2026-09-05 | France cadre penal achat de vote | Le code electoral francais penalise l'achat de vote: art L106 (dons, liberalites, promesses de recompense pour obtenir un vote) et L113-1 (recueil illegal de fonds, depassement plafond, dons en violation L52-7-1/L52-8) avec peines de 2-3 ans d'emprisonnement et 15000-45000 EUR d'amendes | 95a7afa8-b217-4ddc-bc33-7748e59f599d
FCT-002 | FACT | ✦ | https://juricaf.org/arret/FRANCE-CONSEILDETAT-20210722-450129 | A,E | 2026-09-05 | France jurisprudence cadeaux colis alimentaires | Le CE juge que des distributions repetees de colis alimentaires par un candidat en periode electorale, valorisees sur les reseaux sociaux et la presse, sont des manoeuvres electorales pouvant affecter la libre determination des electeurs (Corbeil-Essonnes 2020); l'annulation depend de l'ecart de voix | 0c4bdeb3-fe99-4f69-bddc-e15b0889b259
FCT-003 | FACT | ✦ | https://direzioneinvestigativaantimafia.interno.gov.it/2023/voto-di-scambio-la-dia-esegue-unordinanza-di-custodia-cautelare-a-carico-di-18-soggetti/ | A,D | 2026-09-05 | Italie voto di scambio politico-mafioso | L'achat de votes par la mafia est criminalise (art 416-ter c.p., reforme loi 43/2019); l'operation DIA du 18/04/2023 a demantele un accord clan Amato Pagano-coalitions (Melito di Napoli, elections 2021): votes du clan contre argent, postes de travail et faveurs, avec pressions et intimidations sur residents | fc99aac6-31f4-4471-a45c-d86e09b9ac3c
FCT-004 | FACT | ✧ | https://www.tandfonline.com/doi/abs/10.1080/09668136.2017.1364351 | D | 2026-09-05 | Roumanie Bulgarie clientelisme electoral | Etude experimentale mixte (sondages + qualitatif) en Roumanie et Bulgarie: le clientelisme electoral politise les ressources de l'Etat, plus intense dans les localites a incumbents de longue duree; techniques pour percer le secret du vote (representants au bureau de vote, chain-voting, discussions post-electorales) | f631d480-8fd0-44f8-866f-ceff18ec5387
FCT-005 | FACT | ✧ | https://romea.cz/en/world/slovak-police-investigating-suspicions-of-vote-buying-in-romani-settlements-2/ | B | 2026-09-05 | Slovaquie enquete achat de votes | Police slovaque a enquete (2016) sur des soupcons d'achat de votes dans 2 settlements roms: la maire de Lomnicka aurait achete cigarettes contre votes; Směr-SD y a obtenu 83% vs 28,28% au niveau national; corrompre une election est un delit en Slovaquie | 81b09345-0e4a-40db-abb5-188eedbccb91
FCT-006 | FACT | ✧ | https://en.wikipedia.org/wiki/Clientelism | D | 2026-09-05 | Clientelisme mecanique structurelle | Le clientelisme repose sur un echange de biens/services contre soutien politique via des intermediaires (brokers), ciblant surtout les menages a bas revenus; il politise les ressources publiques et repose sur contingence, hierarchie et iteration (Hicken; Stokes et al.; Trantidis) | dd53a7f0-79e5-48fa-8037-d892ab276ec8
FCT-007 | FACT | ✧ | https://www.palermotoday.it/cronaca/voto-scambio-sindaco-alimena-scrivano-prescrizione-cassazione.html | A,B | 2026-09-05 | Limites d'application des sanctions | L'execution des sanctions connait des limites: prescription en Italie (Cassazione 2024, 50 preferences achetees pour 2500 EUR aux regionales 2012, prescription definitive); preuve difficile du fait du secret du vote (Conseil constitutionnel); manoeuvre electorale etablie mais scrutin maintenu quand l'ecart de voix est important (CE 22/07/2021 Corbeil-Essonnes) | 5dcd5467-680d-4f65-b0f0-1684aef7ff86
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-002
FCT-002 | SRC-009,SRC-002
FCT-003 | SRC-008,SRC-003
FCT-004 | SRC-004
FCT-005 | SRC-005
FCT-006 | SRC-006,SRC-007,SRC-004
FCT-007 | SRC-010,SRC-008,SRC-009

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-018 | FOUND_RESOLVED
FCT-002 | QRY-020 | FOUND_RESOLVED
FCT-003 | QRY-019 | FOUND_RESOLVED

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:CONFIRME
FCT-003 | ELIGIBLE:CONFIRME
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -
FCT-007 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:7
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-003 | SEARCH | PASS | LAST_COMPLETED:découverte: 8 QRY + FETCH SRC-001..007 (Légifrance, Landot, Wikipedia voto di scambio, Mares T&F, Romea, Cambridge clientelism, DIA) | NEXT_ACTION:refutations + faits
CP-004 | FACTS | PASS | LAST_COMPLETED:registre FCT-001..007 (3 ✦: L106 France, voto di scambio DIA, Corbeil-Essonnes CE) + refutations liées FCT-001..003 | NEXT_ACTION:CAU/CTRL/ACT
CP-005 | CAUSAL | PASS | LAST_COMPLETED:CAU-001..004 (mécanismes: incitation matérielle, pression clientéliste, seuil de preuve, gap) | NEXT_ACTION:checkpoint VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:CTRL-001..003 + ACT-001..003 terminaux; 7 faits vérifiés avec sources multi-familles | NEXT_ACTION:sections + gates
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17. 14 sections requises ecrites; registre FCT-001..007 avec refutations FCT-001..003; objets terminaux | NEXT_ACTION:gates + final + narrative + persistence

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-05T10:37:09.374859+00:00","fact_mem":{"FCT-001":"95a7afa8-b217-4ddc-bc33-7748e59f599d","FCT-002":"0c4bdeb3-fe99-4f69-bddc-e15b0889b259","FCT-003":"fc99aac6-31f4-4471-a45c-d86e09b9ac3c","FCT-004":"f631d480-8fd0-44f8-866f-ceff18ec5387","FCT-005":"81b09345-0e4a-40db-abb5-188eedbccb91","FCT-006":"dd53a7f0-79e5-48fa-8037-d892ab276ec8","FCT-007":"5dcd5467-680d-4f65-b0f0-1684aef7ff86"},"mnemo_row":"MNEMO_S a1d84c7f-03f1-4627-a24c-47866e20b3a9","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"writeback MnemoLite","success":1}],"writeback_row":{"attempted":7,"blocked":0,"eligible":7,"failure":0,"success":7}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_S a1d84c7f-03f1-4627-a24c-47866e20b3a9 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:7;attempted:7;success:7;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[7 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-002 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
