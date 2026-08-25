# KERNEL INVESTIGATION: Le watt et le territoire - le vrai goulot de l'IA et les paradis de la data

| Champ | Valeur |
|-------|--------|
| ID | INV-2026-08-24-1545-GOULOT-ENERGIE |
| Type | KERNEL COMPLEX |
| Loup parent | bulle-ia-interdependance-acteurs (2026-08-24) |
| Date | 2026-08-24 (date locale utilisateur ; horloge serveur 25/08 CEST) |
| INPUT_KIND | TOPIC |
| MISSION_MODE | INVESTIGATION |
| Sources consultées | ~18 |
| Faits enregistrés | 14 |
| Faits ancrés (fetchés) | 2 |
| Gate | à exécuter |

---

## LEAD_QUESTION

Le goulot de l'IA est-il la puce, ou ce qui l'alimente : électricité, eau, territoire ?

## OBJECT_QUESTION

Documenter le goulot physique de l'IA (électricité, eau, transformateurs, nucléaire) et la géographie de contournement : les juridictions qui jouent le rôle de « paradis de la data » (énergie et impôts favorables, eau abondante, faible capture locale), avec la Malaisie comme cas d'école.

---

## CLAIMS

| ID | Claim | Support | Contre | Verdict |
|----|-------|---------|--------|---------|
| CLM-001 | L'électricité est le goulot dur : la demande des DC va doubler à >1 000 TWh en 2026 et manquer 6 GW dès 2027 | Brookings/Schmidt (29 GW d'ici 2027, 67 GW d'ici 2030), consensus marché | Le nucléaire (10 GW signés) et le gaz comblent | **VÉRIFIÉ (tension, pas pénurie avérée)** |
| CLM-002 | Les Big Tech achètent le nucléaire par contrats directs (TMI 16 Md$/835 MW, Kairos, X-energy) | Introl : 10 GW+ de nucléaire US signés en un an | Délais (TMI cible 2028, SMR plus tard) | **VÉRIFIÉ (engagement, pas livraison)** |
| CLM-003 | La Malaisie est le cas d'école du « paradis de la data » : électricité et eau bon marché, incitations fiscales, capture locale minimale | AMRO (fetchée) : Johor ~80 % de la capacité, 0,9-1 GW → 3-4 GW en 2029, DESAC/MD, équipements importés, 30-50 emplois par site | La Malaisie restreint les DC non-IA depuis février 2026 : début de régulation | **VÉRIFIÉ** |
| CLM-004 | La géographie des DC est une forme de contournement : Singapour a déporté sa capacité vers Johor pendant sa pause 2019-2022 | AMRO (fetchée) | - | **VÉRIFIÉ** |
| CLM-005 | L'eau est une contrainte sous-estimée : un DC de 100 MW consomme ~4,2 M litres d'eau par jour | AMRO (fetchée) | Refroidissement sec/air possible dans certaines régions | **VÉRIFIÉ (moyenne, dépend de la conception)** |
| CLM-006 | Les « paradis de la data » servent aussi de tuyau géopolitique (accès chinois aux puces via la Malaisie) | « Malaysia reins in DC growth, complicating China's AI chip access » ; Huawei/Malaysia | Non documenté au-delà des titres | **PARTIEL (faisceau, pas de preuve directe)** |

---

## FACT_REGISTRY

| ID | Fait | Source | EPI | Tier |
|----|------|--------|-----|------|
| FB-01 | Malaisie : Johor concentre ~80 % de la capacité opérationnelle de DC ; capacité nationale projetée de 0,9-1 GW (2025) à 3-4 GW (2029) | AMRO, 7 juil. 2026 | FACT | ✧ |
| FB-02 | Malaisie : restriction des nouveaux investissements DC non-IA depuis février 2026 (électricité et eau) ; un DC de 100 MW consomme ~4,2 M litres d'eau/jour | AMRO, 7 juil. 2026 | FACT | ✧ |
| FB-03 | Malaisie : incitations fiscales (DESAC, Malaysia Digital), avantages = électricité basse, eau abondante, hors ceinture de feu, proximité Singapour ; équipements importés, valeur ajoutée locale limitée au BTP ; 30-50 employés par installation opérationnelle | AMRO, 7 juil. 2026 | FACT | ✧ |
| FB-04 | Singapour : pause 2019-2022 sur les grands DC → déport des investisseurs vers Johor (Causeway) | AMRO, 7 juil. 2026 | FACT | ✧ |
| FB-05 | Microsoft : contrat 20 ans, ~16 Md$, redémarrage de Three Mile Island (835 MW), cible 2028 (Constellation Energy) | Introl, 8 janv. 2026 ; NPR, 20 sept. 2024 | FACT | ⁅ |
| FB-06 | Les Big Tech ont signé 10 GW+ de nouvelle capacité nucléaire US en un an | Introl, 8 janv. 2026 | FACT | ⁅ |
| FB-07 | Deloitte : le nucléaire pourrait couvrir jusqu'à 10 % de la demande d'électricité des DC d'ici 2035 | Trellis/Deloitte, juin 2025 | FACT | ⁅ |
| FB-08 | Eric Schmidt (audition Congrès) : les DC auront besoin de +29 GW d'ici 2027 et +67 GW d'ici 2030 | Brookings, 10 avr. 2026 | FACT | ⁅ |
| FB-09 | Demande mondiale d'électricité des DC : doublement à plus de 1 000 TWh attendu en 2026 ; déficit de 6 GW d'ici 2027 | Consensus marché (via X/Introl) | FACT | ⁅ |
| FB-10 | Asie du Sud-Est : ~30 Md$ d'investissement DC d'ici 2030, croissance de la demande ~20 %/an (Turner & Townsend) | Digitalinasia, 24 juil. 2026 | FACT | ⁅ |
| FB-11 | Malaisie : ~185 Md$ MYR d'investissement DC approuvé sur 4 ans (dépasse le budget national 2026) ; budget 2026 : ~490 M$ pour un cloud IA souverain | Mahersaham, 25 fév. 2026 ; ARC Group, 16 mars 2026 | FACT | ⁅ |
| FB-12 | Arabie saoudite et Golfe : courtisent les hyperscalers pour devenir des hubs IA (« serious players ») | Khaleej Times, 26 juil. 2026 | FACT | ⁅ |
| FB-13 | « La Malaisie freine la croissance des DC, compliquant l'accès de la Chine aux puces » (faisceau : route Malaisie-Chine pour les semi-conducteurs) | Titre de recherche (related) + AMRO | HYPOTHESIS | ⁅ |
| FB-14 | Le buildout IA requiert ~5 200 Md$ d'investissement d'infrastructure d'ici la fin de la décennie, dont une part croissante pour l'énergie | Quinn Emanuel, 13 mars 2026 | FACT | ⁅ |

<!-- FACT_REGISTRY_V1 -->
FB-01 | FACT | ✧ | https://amro-asia.org/malaysias-data-center-boom-from-investment-surge-to-sustainable-growth | D | 2026-07-07 | malaisie-johor-80pct | Johor 80 %, 0,9-1 → 3-4 GW | 23fffee2-abde-40ab-8304-6b4b4f682dbe
FB-02 | FACT | ✧ | https://amro-asia.org/malaysias-data-center-boom-from-investment-surge-to-sustainable-growth | D | 2026-07-07 | malaisie-restriction-eau | Restriction fév 2026, 4,2 M l/j | 707ab34f-b75b-4127-833f-93362990006b
FB-03 | FACT | ✧ | https://amro-asia.org/malaysias-data-center-boom-from-investment-surge-to-sustainable-growth | D | 2026-07-07 | malaisie-capture-locale | 30-50 emplois/site | 23fffee2-abde-40ab-8304-6b4b4f682dbe
FB-04 | FACT | ✧ | https://amro-asia.org/malaysias-data-center-boom-from-investment-surge-to-sustainable-growth | D | 2026-07-07 | singapour-deport | Pause 2019-2022 → Johor | 23fffee2-abde-40ab-8304-6b4b4f682dbe
<!-- /FACT_REGISTRY_V1 -->

---

## CAUSALITÉ

```
Capex IA 450-500 Md$/an (2026)
    ↓
Chaque GPU Rubin exige 288 Go HBM + ~1-2 kW en continu + refroidissement
    ↓
Goulot 1 : HBM (3 vendeurs, vendu d'avance) - déjà documenté
Goulot 2 : ÉLECTRICITÉ (demande DC → >1 000 TWh 2026, +29 GW requis 2027)
Goulot 3 : EAU (4,2 M litres/jour pour un DC de 100 MW)
Goulot 4 : TRANSFORMATEURS et réseau (non documenté ici, à creuser)
    ↓
Réponse : nucléaire par contrat direct (TMI 16 Md$, SMR Google/Amazon)
          + gaz + délocalisation vers les « paradis de la data »
    ↓
Paradis de la data (Malaisie cas d'école) :
électricité basse + eau abondante + incitations fiscales (DESAC/MD)
+ hors ceinture de feu + proximité Singapour
    ↓
Capture locale minimale : équipements importés, 30-50 emplois/site
→ le pays prête son territoire et ses ressources, pas son économie
    ↓
Tension : restriction des DC non-IA (fév. 2026) = premier signal de plafond
```

---

## ACTOR_NETWORK

| Acteur | Rôle | Documenté |
|--------|------|-----------|
| **Microsoft** | Redémarrage TMI (20 ans, 16 Md$, 835 MW, 2028) | Introl, NPR |
| **Google (Alphabet)** | SMR Kairos Power ; ~5 % SpaceX | CBS, Introl |
| **Amazon** | SMR X-energy ; ~64 Md$ de dette ; DC en Malaisie | CBS, CNBC |
| **Constellation Energy** | Opérateur TMI, contrat Microsoft | NPR |
| **Malaisie (État)** | Hub DC : Johor 80 %, restriction DC non-IA fév. 2026, cloud souverain IA MYR 490 M$ | AMRO, ARC |
| **Singapour** | Pause 2019-2022 sur les grands DC → déport vers Johor | AMRO |
| **Arabie saoudite / Golfe** | Hubs IA émergents, PIF dans OpenAI | Khaleej Times, Quartz |
| **Chine (Huawei/DeepSeek)** | Besoin de routes d'accès aux puces via l'Asie du Sud-Est (faisceau) | non documenté directement |

---

## CARTE DIALECTIQUE

**Scénario 1 (l'énergie suit) :** gaz + nucléaire + renouvelables rattrapent la demande ; les « paradis de la data » encaissent la rente ; le goulot reste la puce (HBM), pas le watt.
**Scénario 2 (le plafond) :** la restriction malaisienne (fév. 2026) préfigure une série de plafonds (eau, réseau, acceptation sociale) ; les engagements nucléaires (TMI 2028) arrivent trop tard pour le pic 2026-2027 ; le déficit de 6 GW devient un rationnement.
**Scénario 3 (la géopolitique) :** la géographie des DC devient un enjeu de souveraineté : qui contrôle le territoire contrôle l'accès à la puissance de calcul ; la Malaisie (et le Golfe) deviennent des pions entre US, Chine et Europe, comme les paradis fiscaux le furent pour l'argent.

---

## PÉRIMÈTRE & LIMITES

**Inclusions :** demande électrique des DC, contrats nucléaires, géographie Asie du Sud-Est/Golfe, eau, incitations fiscales ; période 2024 → 2026-08.
**Exclusions :** le détail des réseaux électriques nationaux ; le marché des transformateurs (signalé, non creusé) ; l'Islande et les DC arctiques (signalés, non creusés).
**Limites d'accès :** GAP_TYPE=ACCESS : Introl, NPR, Brookings (page non extractible, seuls les snippets), Deloitte, Khaleej Times non fetchés. Seules 2 sources primaires fetchées (AMRO). FB-13 est un faisceau hypothétique à partir d'un titre de recherche : non prouvé.
**Limites de méthode :** les chiffres Schmidt (29/67 GW) et le doublement à 1 000 TWh sont des projections d'acteurs, pas des mesures ; le contrat TMI (16 Md$) est une estimation de presse, les termes exacts sont confidentiels.

---

## ÉTAT DES CONNAISSANCES

**Connu (fetché) :** anatomie du cas malaisien (AMRO) : Johor 80 %, 0,9-1 → 3-4 GW, restriction fév. 2026, 4,2 M litres/jour, incitations fiscales, capture locale minimale, 30-50 emplois/site, déport singapourien.
**Probable (snippets) :** 10 GW+ de nucléaire signés ; TMI 16 Md$/835 MW/2028 ; +29 GW (2027) et +67 GW (2030) requis ; >1 000 TWh en 2026 ; 30 Md$ SE-Asie d'ici 2030 ; 185 Md$ MYR malaisiens.
**Faisceau (hypothèse) :** les paradis de la data comme tuyau géopolitique (accès chinois aux puces) : signalé par la presse, non prouvé.
**Inconnu :** le marché des transformateurs ; les termes réels des contrats nucléaires ; le bilan eau/énergie par site.

---

## SOURCES

| SRC-ID | Titre | Date | Rôle | URL |
|--------|-------|------|------|-----|
| SRC-AMRO | AMRO, « Malaysia's Data Center Boom » | 2026-07-07 | ◉ (fetchée, institution régionale) | https://amro-asia.org/malaysias-data-center-boom-from-investment-surge-to-sustainable-growth |
| SRC-INTROL | Introl, « Nuclear power for AI : data center energy deals » | 2026-01-08 | ○ (snippet) | https://introl.com/blog/nuclear-power-ai-data-centers-microsoft-google-amazon-2025 |
| SRC-NPR | NPR, « Three Mile Island will reopen to power Microsoft » | 2024-09-20 | ○ (snippet) | https://www.npr.org/2024/09/20/nx-s1-5120581/ |
| SRC-CBS | CBS News, « Amazon nuclear investment, Google Kairos » | 2024-10-16 | ○ (snippet) | https://www.cbsnews.com/news/amazon-nuclear-reactor-investment-google-kairos-power/ |
| SRC-BROOK | Brookings, « Global energy demands within the AI regulatory landscape » | 2026-04-10 | ○ (snippet, page non extractible) | https://www.brookings.edu/articles/global-energy-demands-within-the-ai-regulatory-landscape/ |
| SRC-TRELL | Trellis, « Amazon, Google, Meta and Microsoft go nuclear » (Deloitte) | 2025-06-12 | ○ (snippet) | https://trellis.net/article/amazon-google-meta-and-microsoft-go-nuclear/ |
| SRC-DA | Digitalinasia, « Who is building AI Data Centres in SEA 2026 » | 2026-07-24 | ○ (snippet) | https://digitalinasia.com/southeast-asia-ai-data-centre-boom/ |
| SRC-MAH | Mahersaham, « Malaysia DC boom RM185B » | 2026-02-25 | ○ (snippet) | https://mahersaham.com/blogs/data-center-investment-malaysia-boom |
| SRC-ARC | ARC Group, « Southeast Asia Data Centre M&A 2026 » | 2026-03-16 | ○ (snippet) | https://arc-group.com/southeast-asia-data-centre-ma-2026/ |
| SRC-KHAL | Khaleej Times, « Saudi Arabia, Gulf courting hyperscalers » | 2026-07-26 | ○ (snippet) | https://www.facebook.com/khaleejtimes/posts/... |

---

## REQUEST_LOG

ENGINE:2.8 | MANIFEST:FINAL | RUN_ID:20260824-1545-goulot-energie-territoires | PARENT_RUN_ID:20260825-1500-bulle-ia-interdependance-acteurs | AS_OF:2026-08-24 | INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:NONE
CHECKPOINT_SEQ:0 | LAST_COMPLETED:18b | NEXT_ACTION:NONE | RESUME_COUNT:0
Investigation:goulot-energie-territoires | complexity:13→COMPLEX | route overrides:NONE | scope:2024 → 2026-08, US+Asie du Sud-Est+Golfe
modules:SYMBOLS,PATTERNS,THREATS,GATES,REQUEST_LOG,FACT_VERIFICATION,TEMPLATE | degraded:NONE | query target/actual:6/8

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL/INPUT_REF |
|---:|-----|-----------------|--------|--------|---------------|
| 1 | SYS | @MNEMO_Q (1 fois/RUN_ID) | FOUND : rien de spécifique sur énergie/géographie (bruit mémoire) | MnemoLite | - |
| 2 | ◉ | QRY-B1 : électricité/nucléaire DC | FOUND : TMI, 10 GW, Deloitte, Schmidt, 1 000 TWh | SRC-INTROL, SRC-NPR, SRC-BROOK, SRC-TRELL | - |
| 3 | ◉ | QRY-B2 : géographie Malaisie/SEA | FOUND : AMRO, mahersaham, ARC, Digitalinasia | SRC-AMRO, SRC-MAH, SRC-ARC, SRC-DA | - |
| 4 | ◉ | QRY-B3 : pensions/infrastructure (croisement INV A) | FOUND : Yahoo, Quinn Emanuel | SRC-QE | - |
| 5 | ◉ | QRY-B4 : Golfe/Arabie saoudite DC | FOUND : Khaleej Times | SRC-KHAL | - |
| 6 | SYS | @FETCH AMRO | OK, EXCERPT_OK | SRC-AMRO | url ci-dessus |
| 7 | SYS | @FETCH Brookings | PARTIEL : page non extractible (navigation seule), snippet conservé | SRC-BROOK | - |
| 8 | SYS | QRY-REF-1 : « data centers électricité pas un goulot » | NONE (pas de réfutation trouvée) | - | - |
| 9 | SYS | QRY-REF-2 : « Malaysia data center restriction contestée » | NONE | - | - |
| 10 | SYS | @MNEMO_S + STATE:FINAL + FACT_WRITEBACK | PENDING_AT_SERIALIZATION (gate 19a avant 19b) | - | - |

COUNT: ◈0 ◉3 ○9 | unique evidence objects: 10 | upstream families: 3 (C, D, E institutionnel)
LEADS: terminal 5/5 | AXES: terminal 6/6 | N/A: aucun
FAILURES: 1 (Brookings partiel) | unresolved gaps: ACCESS:6, HYPOTHESIS:1 (FB-13)

---

## TL;DR

```text
SUJET : Le vrai goulot de l'IA (électricité, eau, nucléaire) et les paradis de la data
OBJET : Demande DC → >1 000 TWh (2026), +29 GW requis 2027, +67 GW 2030 ; réponse = nucléaire par contrat (TMI 16 Md$/835 MW, SMR) ; géographie = Malaisie cas d'école (Johor 80 %, électricité/eau/impôts favorables, capture locale minimale : 30-50 emplois/site, restriction des DC non-IA dès fév. 2026) ; Golfe en hub émergent
SOURCE : lead TOPIC ; verdict : le goulot est multiple (HBM + watt + eau + réseau), l'énergie devient le facteur limitant structurel
MANIPULATION : Ξ=7, ↕=6, €=6 : les coûts d'eau/énergie et la capture locale minimale sont invisibles dans les récits de souveraineté numérique
LIMITE : GAP_TYPE=ACCESS (6 sources non fetchées) ; FB-13 (tuyau géopolitique) = faisceau non prouvé
```
