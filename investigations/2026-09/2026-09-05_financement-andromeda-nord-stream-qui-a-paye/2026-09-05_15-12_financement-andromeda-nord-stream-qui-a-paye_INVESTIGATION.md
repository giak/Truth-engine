ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260905-1512-financement-andromeda-nord-stream-qui-a-paye | PARENT_RUN_ID:NONE | AS_OF:2026-09-05
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-05_financement-andromeda-nord-stream-qui-a-paye/2026-09-05_15-12_financement-andromeda-nord-stream-qui-a-paye_INPUT.txt | SUBJECT_SLUG:financement-andromeda-nord-stream-qui-a-paye | SUBJECT_FP:sha256:38eebfd3c18713f7a4685094e8f888307f02f9ab4eee15b9998e8b8ab6d8eda2 | INPUT_SHA256:sha256:f9e1a66c676757704f247ae46d72d04a8ebc42ebe45ebcaee2aba640ae363392
COMPLEXITY:13→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:Examen ADVERSARIAL du volet FINANCIER de l'operation Andromeda' (sabotage Nord Stream 1 & 2, 26/09/2022) : qui a PAYE (location du yacht, equipement, logistique) et par quelles chaines de paiement. Perimetre: (a) cout de l'operation (~300 k$ WSJ / 250 k$ livre Pancevski) et identite des financeurs (hommes d'affaires ukrainiens / citoyen prive); (b) chaine documentee par l'enquete: reservation (Maxim B.) -> paiement (Feeria Lwowa, boite aux lettres Varsovie) -> Rustem A./Abibulayev (depot des comptes, perquisition 2022: 192 325 EUR + 126 682 USD) -> tiers non nomme; (c) structures: Feeria Lwowa, proprietaire Kerch double nationalite, Mola Yachting, societes d'Abibulayev UA/Londres/Cyprus; (d) identification par le parquet federal allemand (08/2025, 7 suspects dont Rustem A. et Valeria T.); (e) lead corpus V234 'Tatiana T./Tracfin' vs Valeria T. - verification; (f) question centrale: financier prive autonome ou intermediaire d'un commanditaire etatique? Limites probatoires (sources anonymes WSJ/Spiegel, absence de jugement, Staatswohl, refus Pologne d'extrader).
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/INVESTIGATION.md,protocol/EPISTEMIC.md,protocol/FACT_VERIFICATION.md,output/TEMPLATE.md,tools/MACROS.md,definitions/CONTROLS.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Run 20 — Financement de l'opération Andromeda (Nord Stream) : qui a payé, par quelles chaînes, et qu'en sait-on vraiment ?

**Investigation ADVERSARIALE du volet financier** du sabotage des gazoducs Nord Stream 1 & 2 (26/09/2022). Question centrale : la chaîne de paiement documentée (réservation → société écran polonaise → homme d'affaires ukrainien → tiers non nommé) prouve-t-elle un financeur privé autonome, ou un intermédiaire d'un commanditaire étatique ? Et le lead du corpus V234 (« Tatiana T. financière, Tracfin ignore la piste FR ») résiste-t-il aux sources ouvertes ?

## Les 6 faits établis (✦, 2 familles indépendantes chacun)

| # | Fait | Ce qui est prouvé | Ce qui ne l'est pas |
|---|---|---|---|
| **FCT-001** | L'enquête allemande (parquet fédéral Karlsruhe ; consortium Die Zeit/ARD/SZ, 08/2025) a identifié **7 suspects** dont **Rustem A., 41 ans, homme d'affaires dont la société a payé le yacht Andromeda**, et une plongeuse **Valeria T., 40 ans** (école de plongée de Kiev) | Que le financier présumé est traité comme suspect par les enquêteurs | Que Rustem A. figure parmi les mandats d'arrêt (non publics nominalement) |
| **FCT-002** | Nom complet : **Roustem/Rustem Abibulayev**, homme d'affaires de Kiev (entreprises UA/Londres/Chypre) — nommé par la presse FR (Le JDD, franceinfo) et le WSJ (emails Google du loueur saisis par les autorités US, transmis à l'Allemagne) | Que l'identification du nom complet est une **identification journalistique recoupée** | Qu'elle émane d'une publication officielle (les sources DE utilisent l'initiale par protection des données) |
| **FCT-003** | Perquisition ukrainienne (automne 2022, affaire **sans lien** avec Nord Stream) : casier de Rustem A. contenant **192 325 EUR + 126 682 USD** en liquide et les tampons de 3 sociétés dont **Feeria Lwowa** ; Abibulayev dépose les comptes de Feeria Lwowa au registre polonais | Une trace financière matérielle documentée (Die Zeit/ARD) | Que ces fonds aient été reliés au paiement du yacht par une décision judiciaire |
| **FCT-004** | Coût déclaré : **~300 000 USD** (WSJ 08/2024, 4 sources ukrainiennes anonymes : hommes d'affaires privés, « partenariat public-privé » supervisé par un général relevant de Zaluzhnyi) ; Der Spiegel (02/2026) : « citoyen privé ukrainien comme financeur principal » | L'ordre de grandeur avancé par les participants | Le chiffre exact et l'identité des financeurs (aucune pièce comptable ; livre Pancevski 2026 : ~250 k$) |
| **FCT-005** | La seule femme du groupe : « **Valeria Ch.** » (Chernyshova selon Izvestia citant Die Zeit), 40 ans, record féminin UA de plongée profonde (**104 m**), aurait contacté elle-même le SBU en 2022 ; le livre WSJ/Pancevski la décrit sous pseudo « **Freya** » sans donner son identité | Que trois identifications coexistent dans la presse | Qu'elles désignent la même personne — aucun acte officiel ne publie son nom |
| **FCT-006** | Statut judiciaire : seuls des membres du commando sont inculpés/arrêtés — **Serhii K.** (Kuznietsov, inculpé 01/07/2026 à Karlsruhe), **Zhuravlev** (arrêté Croatie 08/2026) ; le financier Rustem A./Abibulayev est identifié comme suspect mais **aucune inculpation ni arrestation publique ne le vise** | L'asymétrie procédurale (opérateurs poursuivis, financeur non) | Que cette absence reflète une protection délibérée (Ukraine n'extrade pas, mandats non publics) plutôt que l'état du dossier |

## La chaîne documentée (FCT-001 + FCT-002 + FCT-003)

```
Réservation (email, compte Google US envoyé depuis l'Ukraine)  →  Maxim B. (~30 ans, gestionnaire d'équipages, nie)
Paiement du charter Andromeda (Rostock-Warnemünde, 09/2022)   →  Feeria Lwowa (Varsovie, agence fictive, boîte aux lettres partagée avec ~128 sociétés, turnover +1200% en 2020)
Propriétaire nominale                                          →  femme de 32 ans de Kerch (Crimee), double nationalité UA/RU, nie connaître la société
Dépôt des comptes au registre polonais                         →  Rustem A./Abibulayev (41 ans, Kiev)
Perquisition 2022 (affaire sans lien)                          →  192 325 EUR + 126 682 USD + tampons de 3 sociétés dont Feeria Lwowa
Selon son entourage                                            →  « a payé pour le compte d'un tiers » (jamais nommé)
```

## Les 2 GAP typés (ce que la preuve publique ne tranche pas)

1. **CAUSAL_MECHANISM** (CAU-002) : le WSJ affirme (sources **anonymes** ukrainiennes) que l'agence polonaise « a été créée par le renseignement ukrainien comme couverture pour des transactions financières il y a près d'une décennie » (~2013). Les sources DE/FR documentent une société écran privée sans lien établi avec les services. **Aucun document public ne départage** les deux lectures — opération privée autonome vs vecteur de financement étatique déniable.
2. **INTENT** (CAU-003) : le rôle exact du financier. Entourage : « a payé pour le compte d'un tiers ». Impossible de déterminer s'il est financeur principal autonome, prête-nom, ou intermédiaire d'un commanditaire (état-major, Zaluzhnyi/Chervinsky selon les sources anonymes).

## Le lead V234 du corpus, confronté aux sources ouvertes (CTRL-003)

Le corpus V234 (« Tatiana T. », « Tracfin ignore piste FR ») n'est **confirmé par aucune source ouverte** :
- le registre du parquet fédéral allemand (consortium DE, 08/2025) nomme **Valeria T.** (plongeuse, 40 ans) — pas de « Tatiana T. » ;
- la chaîne de paiement documentée passe par la **Pologne** (Feeria Lwowa), pas par la France ;
- **aucune trace** d'une enquête Tracfin liée à Nord Stream/Andromeda/Abibulayev (recherche contre H : zéro résultat public).

**Conclusion : conflation probable** dans le corpus entre « Valeria T. » (la plongeuse) et le rôle de financier (Abibulayev). Le fragment illustre la dérive possible quand un élément non vérifié circule — le run l'enregistre comme REFUTED (conflation probable), pas comme fait.

## Le cœur de la réponse à la question posée

**Ce qui est établi** : un homme d'affaires ukrainien identifiable (Rustem A./Abibulayev) a payé la location du yacht via une société écran polonaise ; il est suspect aux yeux du parquet fédéral allemand ; la chaîne est documentée par un consortium de presse européen (Die Zeit/ARD/SZ/Expressen/NOS/Intelligence Online), recoupée par le WSJ, la presse FR et confirmée dans ses grandes lignes par l'enquête.

**Ce qui reste ouvert (et le run refuse de trancher)** :
1. l'identité du commanditaire final (« tiers » jamais nommé) ;
2. la nature privée ou étatique du financement (thèse WSJ du renseignement UA : non confirmée, non réfutée) ;
3. le rôle réel d'Abibulayev (financeur, prête-nom ou intermédiaire) ;
4. l'identification unique de la femme (Valeria T./Chernyshova/Freya) ;
5. la portée réelle des mandats d'arrêt allemands (6 mandats rapportés en 08/2025, jamais publiés nominalement).

**L'asymétrie frappante** (FCT-006) : les opérateurs sont poursuivis (inculpation Serhii K., arrestation Zhuravlev), le financier — pourtant identifié comme suspect — n'a fait l'objet d'**aucune inculpation publique** à ce jour. Les causes documentées (enquête impossible en Ukraine en guerre, non-extradition des citoyens UA, refus polonais) n'épuisent pas la question : l'état réel du dossier (mandats non publics) reste hors de portée des sources ouvertes.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:6|CLM:2|AXS:3|CAU:5|CTRL:3|ACT:3

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"priority":"HIGH","status":"SATURATED","subject":"Cout et financeurs declares: ~300 000 USD (WSJ 14/08/2024, participants anonymes) / ~250 000 USD (livre Pancevski 2026); financement par des hommes d affaires ukrainiens prives (WSJ) / un citoyen prive ukrainien (Der Spiegel 02/2026)","type":"LEAD"}
LED-002 | {"priority":"HIGH","status":"SATURATED","subject":"Chaine documentee par l enquete (Die Zeit/ARD/SZ/Expressen/NOS/Intelligence Online 26/09/2023 + WSJ): reservation Andromeda par email (homme ukrainien ~30 ans, gestionnaire d equipages Maxim B.) -> paiement par Feeria Lwowa (agence fictive, boite aux lettres Varsovie) -> Rustem A. (depose les comptes; perquisition automne 2022: 192 325 EUR + 126 682 USD + tampons de 3 societes dont Feeria Lwowa)","type":"LEAD"}
LED-003 | {"priority":"HIGH","status":"SATURATED","subject":"Identite complete du financier: Rustem A. = Roustem/Rustem Abibulayev, homme d affaires de Kiev ~41 ans (Intelligence Online 26/09/2023; franceinfo 21/08/2025; Radio France/Le JDD 03/2024); plusieurs entreprises UA/Londres/Cyprus; entourage: a paye pour le compte d un tiers","type":"LEAD"}
LED-004 | {"priority":"MEDIUM","status":"SATURATED","subject":"WSJ 08/2024: l agence polonaise a ete creee par le renseignement ukrainien comme couverture pour transactions financieres ~10 ans avant (sources anonymes ukrainiennes) - hypothese d un vecteur etatique a verifier vs sources allemandes","type":"LEAD"}
LED-005 | {"priority":"MEDIUM","status":"SATURATED","subject":"Lead corpus V234: Tatiana T. comme financiere + Tracfin ignore piste FR - aucun document public ne confirme un nom Tatiana T. ni une enquete Tracfin Nord Stream; le parquet federal allemand nomme Valeria T. (plongeuse 40 ans, ecole de Kiev) parmi 7 suspects - confusion probable a trancher par recherche contre H","type":"LEAD"}
LED-006 | {"priority":"HIGH","status":"SATURATED","subject":"Statut judiciaire du financier: aucune inculpation publique contre Abibulayev (mandats DE: Serhiy K. inculpe 01/07/2026, Zhuravlev arrete Croatie 19/08/2026); 7 suspects identifies 08/2025 - le financier reste-t-il hors de portee/protege ?","type":"LEAD"}

### CLAIM_REGISTRY_V1
CLM-001 | {"status":"SUPPORTED","subject":"La preuve publique identifie un homme d affaires ukrainien (Rustem A./Abibulayev) comme celui dont la societe a paye la location du yacht Andromeda - mais ni son role exact (financeur principal vs intermediaire payant pour un tiers) ni l identite du commanditaire final ne sont etablis par un jugement","type":"CLAIM"}
CLM-002 | {"status":"SUPPORTED","subject":"Le nom Tatiana T. (corpus V234) et une enquete Tracfin sur le financement Nord Stream ne sont confirmez par aucune source ouverte: le registre du parquet federal allemand nomme Valeria T. (plongeuse), et la chaine de paiement documentee passe par la Pologne (Feeria Lwowa), pas par la France","type":"CLAIM"}

### AXIS_REGISTRY_V1
AXS-001 | {"status":"SATURATED","subject":"Axe 1 (identite): le financeur documente de l operation est Rustem A. = Rustem Abibulayev (entreprise Feeria Lwowa ayant paye le yacht) - la preuve publique (consortium Die Zeit 09/2023 + nom complet Intelligence Online + franceinfo) est-elle solide et independante, ou repose-t-elle sur des sources animees ?","type":"POSITION"}
AXS-002 | {"status":"SATURATED","subject":"Axe 2 (autonomie vs etat): la chaine Maxim B. -> Feeria Lwowa -> Abibulayev -> tiers non nomme prouve-t-elle un financeur prive autonome, ou un intermediaire d un commanditaire etatique (renseignement/armee ukrainienne - WSJ: agence creee par le renseignement UA)? Que dit exactement chaque source et quelles sont les limites (anonymat, absence de jugement) ?","type":"POSITION"}
AXS-003 | {"status":"SATURATED","subject":"Axe 3 (lead V234 vs registre): le corpus V234 (Tatiana T. financiere, Tracfin) resiste-t-il a la confrontation avec les sources ouvertes (Valeria T. plongeuse 40 ans; aucun trace Tracfin)? Conflation ou piste reelle non documentee ?","type":"POSITION"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"confidence":"0.85","evidence":"FCT-001 (Novaya Gazeta + franceinfo, familles A+C) + FCT-002 (Le JDD + WSJ, familles C+B)","kind":"EFFECT","status":"SUPPORTED","subject":"La chaine de paiement documentee converge vers un homme d affaires unique: Rustem A./Abibulayev, dont la societe (Feeria Lwowa) a paye la location du yacht - identifie comme suspect par le consortium Die Zeit/ARD/SZ et par le parquet federal (parmi 7 suspects)"}
CAU-002 | {"confidence":"0.6","evidence":"FCT-002 (WSJ) vs FCT-001 (consortium DE)","gap":"Aucun document public ne tranche si Feeria Lwowa etait une couverture du renseignement ukrainien (these WSJ anonyme) ou une societe ecran privee (these DE/FR): l origine et la finalite de la societe depuis ~2013 ne sont pas etablies","gap_type":"CAUSAL_MECHANISM","kind":"GAP","status":"GAP","subject":"Le caractere prive ou etatique du financement reste indetermine: le WSJ affirme (sources anonymes ukrainiennes) que l agence polonaise a ete creee par le renseignement ukrainien comme couverture financiere ~10 ans avant; les sources allemandes et francaises documentent seulement une societe ecran et un homme d affaires sans etablir de lien avec les services - les deux hypotheses (prive autonome vs vecteur etatique) sont compatibles avec les faits connus"}
CAU-003 | {"confidence":"0.5","evidence":"FCT-002 + FCT-003 (Die Zeit: entourage de Rustem A.)","gap":"Identite du tiers pour le compte duquel Abibulayev aurait paye, et sa relation avec Zaluzhnyi/Chervinsky/l etat-major ukrainien: aucun element public (le nom ne circule que dans les sources anonymes WSJ)","gap_type":"INTENT","kind":"GAP","status":"GAP","subject":"Le role exact du financier reste un GAP type: l entourage d Abibulayev affirme qu il a paye pour le compte d un tiers non nomme - impossible de determiner s il est le financeur principal autonome, un prete-nom, ou un intermediaire d un commanditaire (militaire/etatique)"}
CAU-004 | {"confidence":"0.75","evidence":"FCT-006 (Al Jazeera + Novaya Gazeta)","kind":"EFFECT","status":"SUPPORTED","subject":"L absence d inculpation publique du financier s explique par des facteurs documentes mais non exhaustifs: enquete allemande impossible en Ukraine (guerre), non-extradition des citoyens ukrainiens, refus polonais d extrader Zhuravlev, et focalisation du parquet sur le commando operateur (Serhii K. inculpe, Zhuravlev arrete) - le statut d Abibulayev dans les mandats non publics reste inconnu"}
CAU-005 | {"confidence":"0.7","evidence":"FCT-005 (Izvestia + Guardian)","kind":"EFFECT","status":"SUPPORTED","subject":"Le rapprochement Freya = Valeria Ch./T. est une inference de presse non confirmee par un document judiciaire: la presse russe (Izvestia citant Die Zeit) identifie la seule femme comme Valeria Chernyshova, la presse occidentale (livre Pancevski) la decrit sous pseudo Freya, et le registre des suspects la liste comme Valeria T. - trois identifications sans acte officiel publiant son nom"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"evidence":"FCT-004 refutation (QRY-021)","status":"SATURATED","subject":"CONTROL-1 (montant): le cout de 300000 USD n est corrobore par aucune piece comptable - il repose sur des participants anonymes (WSJ); le Der Spiegel reprend le meme ordre de grandeur, le livre de Pancevski avance un chiffre different: la fourchette 250-300 k$ est une estimation journalistique, pas un cout verifie","type":"CONTROL"}
CTRL-002 | {"evidence":"FCT-002 refutation (QRY-017)","status":"SATURATED","subject":"CONTROL-2 (nom complet): Rustem A. n est identifie comme Abibulayev que par la presse FR et Intelligence Online - les sources allemandes et le parquet federal utilisent l initiale A. par protection des donnees: le nom complet est une identification journalistique recoupee, pas une publication officielle","type":"CONTROL"}
CTRL-003 | {"evidence":"recherche WEB contre-H (QRY-006 decouverte negative) + FCT-005","status":"SATURATED","subject":"CONTROL-3 (piste Tatiana T./Tracfin du corpus V234): recherche contre H - aucune source ouverte ne documente une financiere Tatiana T. ni une enquete Tracfin sur le financement Nord Stream; le corpus V234 semble confondre Valeria T. (plongeuse) et le role de financier (Abibulayev): le lead du corpus n est pas confirme","type":"CONTROL"}

### ACTION_REGISTRY_V1
ACT-001 | {"evidence":"FCT-006","status":"SUPPORTED","subject":"ACT-1: suivre le proces de Serhii K. (Kuznietsov) a Karlsruhe (inculpe 07/2026) - les debats peuvent reveler la chaine de financement reelle et le role exact d Abibulayev","type":"ACTION"}
ACT-002 | {"evidence":"FCT-002 + FCT-003","status":"SUPPORTED","subject":"ACT-2: verifier aupres des registres polonais et ukrainiens l historique complet de Feeria Lwowa (2013-2026): beneficiaires effectifs, flux, lien eventuel avec le renseignement ukrainien (these WSJ) vs societe ecran privee","type":"ACTION"}
ACT-003 | {"evidence":"FCT-006 refutation (QRY-023)","status":"SUPPORTED","subject":"ACT-3: rechercher dans les archives des commissions d enquete et la presse specialisee si un mandat d arret ou une inculpation vise Rustem Abibulayev (les 6 mandats d aout 2025 ne sont pas publics nominalement)","type":"ACTION"}

SEARCH_ACTIVITY_V1:WEB:14|FETCH:9|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | PASS | mnemolite | financement-andromeda-qui-a-paye | MNEMO_Q
SYS-003 | SYS | FOUND | mnemolite | 5d79b1da-9d68-44fa-8c8d-e58bb020594b (V234 Tatiana T/Andromeda/Tracfin); 8ce5a716 (V233 Hersh); 5c4990e2 (Run19 FCT-002) | MEMORY_PROBE
SYS-004 | SYS | PASS | runtime | FCT-001 | REPAIR_FACT
SYS-005 | SYS | PASS | runtime | FCT-002 | REPAIR_FACT
SYS-006 | SYS | PASS | runtime | FCT-003 | REPAIR_FACT
SYS-007 | SYS | PASS | runtime | FCT-004 | REPAIR_FACT
SYS-008 | SYS | PASS | runtime | FCT-005 | REPAIR_FACT
SYS-009 | SYS | PASS | runtime | FCT-006 | REPAIR_FACT
SYS-010 | SYS | PASS | runtime | FCT-001 | REPAIR_FACT
SYS-011 | SYS | PASS | runtime | FCT-006 | REPAIR_FACT
SYS-012 | SYS | PASS | runtime | FCT-006 | REPAIR_FACT
SYS-013 | SYS | PASS | runtime | FCT-004 | REPAIR_FACT
SYS-014 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | ok | - | - | decouverte: enquete allemande Andromeda financement qui a paye location yacht Feeria Lwowa Rustem A homme d'affaires Kiev 2023 2024 2025
QRY-002 | WEB | ok | - | - | decouverte: 'Feeria Lwowa' Nord Stream societe polonaise agence voyages fictive proprietaire Kerch turnover +1200% Expressen Die Zeit
QRY-003 | WEB | ok | - | - | decouverte: 'Rustem Abibulayev' OR Abibulayev Nord Stream yacht Andromeda homme d'affaires ukrainien nom complet Intelligence Online franceinfo
QRY-004 | WEB | ok | - | - | decouverte: WSJ 'drunken evening' Nord Stream financier private businessmen cout 300k$ agence polonaise creee par renseignement ukrainien 2024
QRY-005 | WEB | ok | - | - | decouverte: 'Tatiana' OR 'Valeria' OR 'Freya' Nord Stream femme plongeuse identite Andromeda seule femme equipe suspects parquet allemand 2025 2026
QRY-006 | WEB | ok | - | - | decouverte (contre-H): Tracfin France enquete Nord Stream financement Abibulayev Feeria piste bancaire FR - aucun resultat publique (negative)
QRY-007 | FETCH | FOUND | SRC-001 | https://novayagazeta.eu/en/articles/2025/08/28/german-investigators-identify-all-suspects-in-nord-stream-pipeline-explosion-en-news | FETCH Novaya Gazeta 28/08/2025
QRY-008 | FETCH | FOUND | SRC-002 | https://www.tovima.com/wsj/a-drunken-evening-a-rented-yacht-the-real-story-of-the-nord-stream-pipeline-sabotage/ | FETCH WSJ fulltext (Tovima)
QRY-009 | FETCH | FOUND | SRC-003 | https://www.theguardian.com/business/2026/aug/19/ukrainian-diver-arrested-in-croatia-over-nord-stream-pipeline-bombings | FETCH Guardian 19/08/2026
QRY-010 | FETCH | FOUND | SRC-004 | https://www.lejdd.fr/international/sabotage-des-gazoducs-nord-stream-un-diplomate-ukrainien-mis-en-cause-143296 | FETCH Le JDD 22/03/2024
QRY-011 | FETCH | FOUND | SRC-005 | https://www.franceinfo.fr/monde/europe/manifestations-en-ukraine/un-suspect-ukrainien-arrete-en-italie-dans-l-enquete-sur-le-sabotage-des-gazoducs-nord-stream-en-mer-baltique-en-2022_7446850.html | FETCH franceinfo 21/08/2025
QRY-012 | FETCH | FOUND | SRC-006 | https://www.sueddeutsche.de/projekte/artikel/politik/nord-stream-ukraine-andromeda-sprengung-e706707/ | FETCH SZ 27/08/2025 (paywall partiel, titre+chapo lu)
QRY-013 | FETCH | FOUND | SRC-007 | https://en.iz.ru/en/1944866/2025-08-29/ukrainian-athlete-chernyshova-could-have-taken-part-bombing-nord-streams | FETCH Izvestia EN 29/08/2025
QRY-014 | FETCH | FOUND | SRC-008 | https://www.aljazeera.com/news/2026/7/2/german-prosecutors-charge-ukrainian-suspect-over-nord-stream-explosions | FETCH Al Jazeera 02/07/2026
QRY-015 | FETCH | FOUND | SRC-009 | https://www.zeit.de/politik/2023-09/nord-stream-pipelines-attack-anniversary-english/komplettansicht | FETCH Die Zeit 26/09/2023
QRY-016 | WEB | FOUND_RESOLVED | - | - | REFUTATION FCT-001: la presse DE (NV/Ukraine 09/07/2026, TVP 28/08/2025) indique que les enqueteurs ont identifie TOUS les suspects et emis des mandats d'arret (5 ou 6) - le statut de suspect des 7 personnes (dont le financier Rustem A., 41 ans, et la plongeuse Valeria T., 40 ans) inclut-il reellement le financier, ou celui-ci reste-t-il hors perimetre des mandats publics ?
QRY-017 | WEB | FOUND_RESOLVED | - | - | REFUTATION FCT-002: le nom complet 'Rustem Abibulayev' (41 ans) ne figure que dans la presse FR (Le JDD, franceinfo) et Intelligence Online - les sources allemandes ne nomment que 'Rustem A.'; la forme 'Abibulayev' et son role exact (loueur vs financeur) sont-ils confirmes par les autorites ou seulement une inference journalistique ?
QRY-018 | WEB | FOUND_RESOLVED | - | - | REFUTATION FCT-003: la perquisition du casier de Rustem A. (192 325 EUR + 126 682 USD, tampons de 3 societes dont Feeria Lwowa) releve d'une enquete ukrainienne SANS LIEN avec Nord Stream - cet argent et ces documents prouvent-ils un lien financier avec l'operation Andromeda, ou seulement l'activite generale d'un homme d'affaires (le montant n'a pas ete relie au paiement du yacht) ?
QRY-019 | WEB | FOUND_RESOLVED | - | - | REFUTATION FCT-004: le cout de ~300 000 USD et le financement par des hommes d'affaires prives reposent sur des sources anonymes ukrainiennes (WSJ 14/08/2024, 4 sources) jamais confrontees a des preuves comptables; le livre de Pancevski (05/2026) avance ~250 000 USD - le chiffre exact et l'identite des financeurs restent-ils inverifiables, et le Der Spiegel (02/2026) nomme-t-il reellement le 'citoyen prive' financeur ?
QRY-020 | WEB | FOUND_RESOLVED | - | - | REFUTATION FCT-003: la perquisition (2022) du casier de Rustem A. (192325 EUR et 126682 USD en liquide, tampons de trois societes dont Feeria Lwowa) releve d une enquete ukrainienne sans lien avec Nord Stream - le contenu prouve-t-il un lien financier avec l operation Andromeda, ou seulement l activite generale d un homme d affaires, des lors qu aucun document ni temoin n a relie ces fonds au paiement du yacht et que la saisie n a debouche sur aucune poursuite publique ?
QRY-021 | WEB | FOUND_RESOLVED | - | - | REFUTATION FCT-004: le cout de 300000 USD et le financement par des hommes d affaires prives reposent sur quatre sources ukrainiennes anonymes (WSJ) jamais confrontees a des preuves comptables; le chiffre de 300000 USD est repete par Der Spiegel mais derive de la meme origine anonyme; le livre de Pancevski (2026) avance un cout different - le montant et l identite des financeurs restent-ils inverifiables en l absence de documents bancaires ou de jugement ?
QRY-022 | WEB | FOUND_RESOLVED | - | - | REFUTATION FCT-005: l identification Valeria Ch. (40 ans, record de 104 metres, contact SBU en 2022) repose sur la presse citant Die Zeit (2026) et sur le recit de Pancevski (2026) - mais ni le parquet federal allemand ni un document judiciaire ne publie le nom de la femme; la presse russe donne Chernyshova, la presse occidentale Freya, le registre des suspects Valeria T.: ces trois identifications designent-elles la meme personne ou des femmes differentes (membre d equipage vs plongeuse de l ecole) ?
QRY-023 | WEB | FOUND_RESOLVED | - | - | REFUTATION FCT-006: la presse ukrainienne et allemande rapporte que le parquet federal a identifie tous les suspects et emis des mandats d arret contre six Ukrainiens (aout 2025) - si le financier Abibulayev figure parmi ces mandats, l affirmation selon laquelle aucune inculpation ni arrestation publique ne le vise serait incomplete: verifier si Rustem A. est un des six mandats ou reste hors perimetre public; a ce jour seuls Serhii K. (inculpe) et Zhuravlev (arrete Croatie) ont ete rendus publics

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://novayagazeta.eu/en/articles/2025/08/28/german-investigators-identify-all-suspects-in-nord-stream-pipeline-explosion-en-news
SRC-002 | ◈ | fam:B | https://www.tovima.com/wsj/a-drunken-evening-a-rented-yacht-the-real-story-of-the-nord-stream-pipeline-sabotage/
SRC-003 | ◈ | fam:B | https://www.theguardian.com/business/2026/aug/19/ukrainian-diver-arrested-in-croatia-over-nord-stream-pipeline-bombings
SRC-004 | ◈ | fam:C | https://www.lejdd.fr/international/sabotage-des-gazoducs-nord-stream-un-diplomate-ukrainien-mis-en-cause-143296
SRC-005 | ◈ | fam:C | https://www.franceinfo.fr/monde/europe/manifestations-en-ukraine/un-suspect-ukrainien-arrete-en-italie-dans-l-enquete-sur-le-sabotage-des-gazoducs-nord-stream-en-mer-baltique-en-2022_7446850.html
SRC-006 | ◈ | fam:A | https://www.sueddeutsche.de/projekte/artikel/politik/nord-stream-ukraine-andromeda-sprengung-e706707/
SRC-007 | ◈ | fam:A | https://en.iz.ru/en/1944866/2025-08-29/ukrainian-athlete-chernyshova-could-have-taken-part-bombing-nord-streams
SRC-008 | ◈ | fam:D | https://www.aljazeera.com/news/2026/7/2/german-prosecutors-charge-ukrainian-suspect-over-nord-stream-explosions
SRC-009 | ◈ | fam:A | https://www.zeit.de/politik/2023-09/nord-stream-pipelines-attack-anniversary-english/komplettansicht

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://novayagazeta.eu/en/articles/2025/08/28/german-investigators-identify-all-suspects-in-nord-stream-pipeline-explosion-en-news | A,C | 2026-09-05 | Enquete allemande (parquet federal Karlsruhe; consortium Die Zeit/ARD/SZ): sept suspects identifies dont Rustem A., 41 ans, homme d affaires, dont la societe a paye le yacht Andromeda, et une plongeuse Valeria T., 40 ans, de l ecole de plongee de Kiev - le financier presume est lui-meme traite comme suspect par les enqueteurs | 7 suspects; Rustem A. 41 ans financier presume; Valeria T. 40 ans plongeuse; ecole de plongee Kiev; confirme par SZ 27/08/2025 et Die Zeit | 689734ce-89be-4cf6-833e-06a2d450faac
FCT-002 | FACT | ✦ | https://www.lejdd.fr/international/sabotage-des-gazoducs-nord-stream-un-diplomate-ukrainien-mis-en-cause-143296 | B,C | 2026-09-05 | Nom complet du financier: Roustem/Rustem Abibulayev, homme d affaires ukrainien de Kiev (une quarantaine d annees, entreprises UA/Londres/Cyprus dont elevage porcin et pompes a chaleur) - nomme par la presse FR (Le JDD et franceinfo: la location du voilier a ete reglee par un Ukrainien, Roustem Abibulayev) et par le WSJ (homme d affaires ukrainien ayant loue le bateau, emails Google saisis par les autorites US et transmis a l Allemagne) | Abibulayev; Le JDD + franceinfo + WSJ; location reglee par Abibulayev; emails Google saisis | 329456fd-4d0e-4818-bfeb-f950d3657c93
FCT-003 | FACT | ✦ | https://www.zeit.de/politik/2023-09/nord-stream-pipelines-attack-anniversary-english/komplettansicht | A,C | 2026-09-05 | Perquisition ukrainienne (automne 2022, affaire sans lien avec Nord Stream): casier de Rustem A. contenait 192325 EUR et 126682 USD en liquide et les tampons de trois societes liees dont Feeria Lwowa; Rustem A. est le deposant des rapports financiers de Feeria Lwowa au registre polonais (Die Zeit/ARD) - trace financiere materielle documentee mais jamais reliee au paiement du yacht par une decision judiciaire | 192325 EUR; 126682 USD; tampons 3 societes; Feeria Lwowa; deposant des comptes | d3bba480-b8e5-44d5-9121-a595409ff339
FCT-004 | FACT | ✦ | https://www.tovima.com/wsj/a-drunken-evening-a-rented-yacht-the-real-story-of-the-nord-stream-pipeline-sabotage/ | A,B | 2026-09-05 | Cout et financement declares par les participants (WSJ, quatre sources ukrainiennes anonymes): operation a environ 300000 USD financee par des hommes d affaires prives, partenariat public-prive supervise par un general relevant de Zaluzhnyi; Der Spiegel (dossier de fevrier deux mille vingt-six): citoyen prive ukrainien comme financeur principal, environ 300000 USD - les noms des financeurs ne sont pas publies par ces sources | 300000 USD; hommes d'affaires prives; Zaluzhnyi; Der Spiegel 02/2026; noms non publies | df45f4bc-f480-45e4-9955-36bd69b2d96d
FCT-005 | FACT | ✦ | https://en.iz.ru/en/1944866/2025-08-29/ukrainian-athlete-chernyshova-could-have-taken-part-bombing-nord-streams | A,B | 2026-09-05 | La seule femme du groupe identifiee par l enquete allemande: Valeria Ch. (Chernyshova selon la presse citant Die Zeit), 40 ans, Kiev, record feminin ukrainien de plongee profonde (104 metres), qui aurait contacte elle-meme le SBU en 2022; le recit WSJ/livre Pancevski (2026) decrit la femme de l equipage sous le pseudo Freya (instructrice civile, ancien mannequin) sans donner son identite - le rapprochement Freya egale Valeria Ch. reste une inference de presse, pas un etat de l enquete | Valeria Ch.; Chernyshova; 104 m record; 40 ans; SBU 2022; Freya pseudo; rapprochement non confirme par l'enquete | 52d688cd-9f1d-4525-80c6-6bbe39893cf7
FCT-006 | FACT | ✦ | https://www.aljazeera.com/news/2026/7/2/german-prosecutors-charge-ukrainian-suspect-over-nord-stream-explosions | A,D | 2026-09-05 | Statut judiciaire: seuls des membres du commando sont inculpes ou arretes - Serhii K. (Kuznietsov), coordinateur presume a bord, arrete en Italie puis extrade et inculpe par le parquet federal a Karlsruhe (premier juillet deux mille vingt-six); Volodymyr Zhuravlev arrete en Croatie (aout deux mille vingt-six); le financier Rustem A./Abibulayev est identifie comme suspect par le consortium de presse allemand (aout deux mille vingt-cinq) mais aucune inculpation ou arrestation publique ne le vise a ce jour (septembre deux mille vingt-six) | Serhii K. inculpe 01/07/2026; Zhuravlev Croatie 19/08/2026; financier suspect sans inculpation publique | 6bf577c9-582d-4a11-b14a-ee1cf4ca12a1
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-005
FCT-002 | SRC-004,SRC-002
FCT-003 | SRC-009,SRC-004
FCT-004 | SRC-002,SRC-001
FCT-005 | SRC-007,SRC-003
FCT-006 | SRC-008,SRC-001

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-016 | FOUND_RESOLVED
FCT-002 | QRY-017 | FOUND_RESOLVED
FCT-003 | QRY-020 | FOUND_RESOLVED
FCT-004 | QRY-021 | FOUND_RESOLVED
FCT-005 | QRY-022 | FOUND_RESOLVED
FCT-006 | QRY-023 | FOUND_RESOLVED

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:CONFIRME
FCT-003 | ELIGIBLE:CONFIRME
FCT-004 | ELIGIBLE:CONFIRME
FCT-005 | ELIGIBLE:CONFIRME
FCT-006 | ELIGIBLE:CONFIRME

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 leads (cout/financeurs, chaine Maxim B./Feeria Lwowa/Rustem A., nom complet, WSJ couverture UA, V234 Tatiana T./Tracfin, statut judiciaire) | NEXT_ACTION:SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 scope (financier Andromeda: chaine de paiement, identites, statut judiciaire, lead V234) | NEXT_ACTION:SEARCH_DISCOVERY
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 discovery (6 WEB + 9 FETCH, 9 sources, 6 faits ETOILE, 2 familles independantes chacun) | NEXT_ACTION:FAITS: registre faits + alignement refutations (contract refutation)
CP-004 | FACTS | PASS | LAST_COMPLETED:10 facts registry (6 faits ETOILE 2 familles + refutations alignees) | NEXT_ACTION:CAUSAL analysis
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 causal (5 CAU dont 2 GAP types CAUSAL_MECHANISM et INTENT, 3 CTRL, 3 ACT) | NEXT_ACTION:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 verify (6 faits ETOILE 2 familles, refutations alignees, GAP types, recherche contre-H Tatiana/Tracfin negative) | NEXT_ACTION:sections render
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 accountability (14 sections manuelles, registres derives OK, 6 faits, EDI, 6 refutations) | NEXT_ACTION:gates + finalize

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-05T15:25:17.364572+00:00","fact_mem":{"FCT-001":"689734ce-89be-4cf6-833e-06a2d450faac","FCT-002":"329456fd-4d0e-4818-bfeb-f950d3657c93","FCT-003":"d3bba480-b8e5-44d5-9121-a595409ff339","FCT-004":"df45f4bc-f480-45e4-9955-36bd69b2d96d","FCT-005":"52d688cd-9f1d-4525-80c6-6bbe39893cf7","FCT-006":"6bf577c9-582d-4a11-b14a-ee1cf4ca12a1"},"mnemo_row":"MNEMO_S 818f864d-46c6-47cb-89d4-87736088a941","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"writeback MnemoLite","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"writeback MnemoLite","success":1}],"writeback_row":{"attempted":6,"blocked":0,"eligible":6,"failure":0,"success":6}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_S 818f864d-46c6-47cb-89d4-87736088a941 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:6;attempted:6;success:6;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[6 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-002 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-005 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
FCT-006 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:writeback MnemoLite
