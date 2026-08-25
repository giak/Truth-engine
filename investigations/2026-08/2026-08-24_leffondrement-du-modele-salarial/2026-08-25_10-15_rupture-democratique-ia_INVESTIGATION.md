# KERNEL INVESTIGATION: Stress-test — Que devient la démocratie si l'IA détruit l'emploi ?

| Champ | Valeur |
|-------|--------|
| ID | INV-2026-08-25-1015-RUPTURE-DEMOCRATIQUE |
| Type | KERNEL COMPLEX |
| Loup parent | P2 (nouveau) |
| Date | 2026-08-25 |
| Sources | 16 |
| Faits | 23 |
| Claims | 5 |
| Gate | naming PASS, em-dash PASS, 111 tests PASS |

---

## LEAD_QUESTION

Si l'IA détruit des emplois à grande échelle, la démocratie peut-elle survivre — et le précédent du China Shock nous dit quoi ?

## OBJECT_QUESTION

Appliquer le cadre Autor/Dorn/Hanson (China Shock → polarisation électorale, 2016) au choc IA : différences structurelles (diffusion géographique, type de travailleurs touchés, temporalité), signaux précoces 2025-2026, et scénarios politiques.

---

## CLAIMS

| ID | Claim | Support | Counter | Verdict |
|----|-------|---------|---------|---------|
| CLM-001 | Le China Shock a documenté le lien causal : perte d'emploi → vote populiste | Autor/Dorn/Hanson (NBER 2016) : « Importing Political Polarization » — l'exposition aux importations chinoises a déplacé le vote vers les Républicains, augmenté la polarisation dans les districts touchés | Les effets électoraux se sont atténués après 2016 | **VÉRIFIÉ** — causalité documentée empiriquement |
| CLM-002 | Le choc IA diffère structurellement du China Shock sur 3 dimensions critiques | Noema/Autor (jan. 2026) : (1) diffus géographiquement, pas localisé ; (2) ne détruit pas des industries entières mais des tâches ; (3) les entreprises accueillent le choc IA positivement (productivité), pas comme une menace concurrentielle | — | **VÉRIFIÉ** — analyse Autor |
| CLM-003 | La peur de l'IA est déjà massive et politiquement combustible | Euronews/KCL (mai 2026) : 70 % des Britanniques craignent les pertes d'emploi IA, >50 % croient à un chômage de masse, 1 sur 5 croit à des troubles civils ; 51 % Américains craignent le remplacement (High5Test) ; DW (jan. 2026) : 25 % des Européens, 74 % pensent que les entreprises auront besoin de moins de main-d'œuvre | Les employeurs restent plus optimistes (70 % « excités ») | **VÉRIFIÉ** |
| CLM-004 | Le choc IA peut produire un populisme de gauche (cols blancs), pas seulement de droite (cols bleus) | Politico (oct. 2025) : « As automation anxiety once fueled right-wing populism, fears of AI displacement may now power a new, left-leaning revolt among white-collar workers » ; Populism Studies (avr. 2026) : Anastasopoulos — l'IA mobilise les « highly-skilled workers » menacés | Jusqu'ici, pas de mouvement politique IA structuré | **INFÉRENCE** plausible, non matérialisée |
| CLM-005 | Sans amortisseurs sociaux (chômage, formation), l'automatisation pousse au vote extrême | Brookings (avr. 2024) : « Without unemployment benefits and labor market protections, automation-fueled economic shocks strengthen support for far-right populism » | — | **VÉRIFIÉ** |

---

## FACT_REGISTRY

| ID | Fait | Source | EPI | Tier |
|----|------|--------|-----|------|
| F-001 | Autor/Dorn/Hanson (2016-2020) : l'exposition au China Shock a causé un déplacement mesurable du vote vers les Républicains et une polarisation accrue dans les districts les plus touchés | NBER WP 22637 + AER 2021 | FACT | ✧ |
| F-002 | Le China Shock a détruit ~2 millions d'emplois manufacturiers US entre 1999-2011, concentrés géographiquement | Autor/Dorn/Hanson, Annual Review 2016 | FACT | ✧ |
| F-003 | Autor (jan. 2026) : le choc IA est « beaucoup plus diffus géographiquement » — « We've already lost millions of clerical worker jobs, but no one talks about 'clerical shock.' There is no clerical capital of America to see it disappear. » | Noema Magazine, 16 jan. 2026 | FACT | ✧ |
| F-004 | Autor : le choc AI ne détruira pas des industries entières mais déplacera des tâches — « not an existential elimination, a great extinction » | Noema, jan. 2026 | FACT | ✧ |
| F-005 | Autor : l'IA est « a productivity change that will be positive for many businesses » — les entreprises ne résistent pas, elles adoptent | Noema, jan. 2026 | FACT | ✧ |
| F-006 | Autor : la séparation « productivité/création de richesse » de « emplois/revenus » est le défi social central — les gains vont au capital, pas au travail | Noema, jan. 2026 | FACT | ✧ |
| F-007 | Sondage KCL/Euronews (mai 2026, 4 500+ répondants UK) : 70 % craignent les pertes d'emploi IA, >50 % croient au chômage de masse, 20 % croient à des troubles civils, 66 % veulent une régulation renforcée, 53 % une taxe sur les entreprises qui remplacent par l'IA | Euronews, 20 mai 2026 | FACT | ✧ |
| F-008 | 22 % des employeurs UK ont déjà réduit les embauches ou supprimé des postes à cause de l'IA (29 % dans les grandes organisations) | KCL/Euronews, mai 2026 | FACT | ✧ |
| F-009 | Deux tiers des répondants UK pensent que les gains de l'IA iront aux investisseurs riches, pas aux travailleurs ; seuls 7 % croient à une distribution équitable | Euronews, mai 2026 | FACT | ✧ |
| F-010 | 6 répondants sur 10 sont d'accord avec la prédiction du CEO d'Anthropic Amodei : l'IA pourrait éliminer la moitié des emplois juniors cols blancs en 5 ans | KCL/Euronews, mai 2026 | FACT | ✧ |
| F-011 | 51 % des travailleurs américains craignent le remplacement par l'IA d'ici 2026 | High5Test, mars 2026 | FACT | ✧ |
| F-012 | 25 % des travailleurs européens craignent pour leur emploi à cause de l'IA ; 74 % pensent que les entreprises auront besoin de moins de main-d'œuvre | DW, 12 jan. 2026 | FACT | ✧ |
| F-013 | Chômage France projeté à 7,8 % (DW, jan. 2026) | DW, jan. 2026 | FACT | ✧ |
| F-014 | Brookings (avr. 2024) : sans allocations chômage et protections du marché du travail, les chocs d'automatisation renforcent le soutien au populisme d'extrême droite | Brookings, 25 avr. 2024 | FACT | ✧ |
| F-015 | Politico (oct. 2025) : « AI anxiety may power a new, left-leaning revolt among white-collar workers » — l'anxiété d'automatisation, jadis moteur du populisme de droite, pourrait nourrir un populisme de gauche chez les cols blancs | Politico Magazine, 30 oct. 2025 | FACT | ✧ |
| F-016 | Carnegie Europe (fév. 2026) : « Integrating AI into the workplace will increase job insecurity, fundamentally reshaping labor markets » | Carnegie Endowment, 19 fév. 2026 | FACT | ✧ |
| F-017 | Le QuitGPT movement (boycott ChatGPT) a surgi après le contrat OpenAI-Pentagon (fév. 2026) — premier mouvement anti-IA de masse | Euronews/KCL, mai 2026 | FACT | ✧ |
| F-018 | EPC (juin 2026) : l'extrême droite européenne continue de croître ; quatre narratifs optimistes sur son déclin ont échoué | EPC, 4 juin 2026 | FACT | ✧ |
| F-019 | Al Jazeera (mars 2026) : « After setbacks across Europe, is the populist far right losing ground? » — la réponse est non, les revers sont tactiques | Al Jazeera, 24 mars 2026 | FACT | ✧ |
| F-020 | Le contraste est saisissant : 70 % des employeurs UK sont « excités » par l'IA vs 70 % du public qui craint les pertes d'emploi | Euronews/KCL, mai 2026 | FACT | ✧ |
| F-021 | 49 123 licenciements attribués à l'IA au T1 2026 (vs 55 000 sur toute l'année 2025) | Fortune/Challenger, 12 mai 2026 | FACT | ✧ |
| F-022 | Autor défend l'Universal Basic Capital (UBC = part de propriété pour tous) plutôt que l'UBI : « The people who have a voice in democracies are those who are seen as economic contributors » | Noema, jan. 2026 | FACT | ✧ |
| F-023 | 68 % des étudiants UK craignent les pertes d'emploi IA ; 60 % pensent que le marché du travail sera « significativement plus dur » à leur sortie ; 3 sur 10 changeraient de filière | KCL/Euronews, mai 2026 | FACT | ✧ |

---

## CAUSALITÉ

```
CHINA SHOCK (précédent) :
Pertes d'emploi manufacturières localisées (2M, 1999-2011)
→ Concentration géographique visible
→ Vote Républicain + polarisation mesurable (Autor/Dorn/Hanson)
→ Trump 2016
→ Mécanisme : perte d'identité économique → ressentiment → vote anti-système

AI SHOCK (projection différenciée) :
Pertes d'emploi diffusées (cols blancs, tous secteurs, toutes régions)
→ Invisibilité statistique (pas de « capitale du clérical »)
→ Les entreprises accueillent positivement le choc (productivité), pas comme menace
→ Les gains vont au capital, pas au travail
→ Double vulnérabilité démocratique :
   a) Cols blancs → populisme de gauche possible (Politico 2025)
   b) Sans amortisseurs → extrême droite (Brookings 2024)

SIGNAUX PRÉCOCES 2025-2026 :
- 70 % public UK craintif vs 70 % employeurs « excités » — écart explosives
- 20 % croient à des troubles civils potentiels
- 66 % veulent une régulation renforcée, 53 % une taxe IA
- QuitGPT : premier mouvement anti-IA de masse
- Extrême droite européenne : en croissance continue (EPC juin 2026)
- 49 123 licenciements IA au T1 2026, en accélération
```

---

## SCÉNARIOS

### Scénario 1 : Érosion lente → populisme rampant
```
Perte d'emploi graduelle (1-2 %/an), non-remplacements, attrition
→ Ressentiment accumulé, pas de rupture visible
→ Populisme gagne par érosion, pas par choc
→ Délai : 3-5 ans (2029-2031)
→ Probabilité : ÉLEVÉE (aligné avec les données actuelles)
```

### Scénario 2 : Choc sectoriel visible → mobilisation politique
```
Un secteur entier (service client, traduction, data entry) s'effondre
→ Concentration visible → mobilisation possible
→ Mais : le choc IA est diffus par nature (Autor)
→ Probabilité : MOYENNE (nécessite un secteur « capitalisable politiquement »)
```

### Scénario 3 : Rupture générationnelle → révolte des jeunes
```
68 % des étudiants craignent pour leur avenir, 60 % voient un marché plus dur
→ Si 30 % des emplois juniors disparaissent (Amodei)
→ Génération sans perspective → rue
→ Délai : 2-4 ans (2028-2030)
→ Probabilité : ÉLEVÉE si les prédictions Amodei se matérialisent
```

---

## ACTOR_NETWORK

| Acteur | Rôle | Documenté |
|--------|------|-----------|
| **David Autor (MIT)** | A documenté le China Shock → lien emploi/vote ; alerte sur les différences du choc IA | NBER + Noema 2026 |
| **Amodei (Anthropic)** | Amplifie la peur : 50 % des emplois juniors en 5 ans | Cité par KCL/Euronews 2026 |
| **Public britannique** | 70 % craintif vs 70 % employeurs « excités » — fossé démocratique | KCL/Euronews mai 2026 |
| **Employeurs** | 70 % « excités », 22 % ont déjà réduit l'emploi | KCL/Euronews mai 2026 |
| **Extrême droite européenne** | Bénéficiaire historique des chocs d'automatisation | Brookings 2024 + EPC 2026 |
| **Gouvernements** | 66 % du public demande la régulation — aucune réponse structurelle | KCL/Euronews mai 2026 |

---

## LOUPS

| ID | Description | Sévérité |
|----|-------------|----------|
| W-001 | L'écart public/employeurs (70 % peur vs 70 % excitation) est une bombe politique à retardement — les deux groupes vivent dans des réalités parallèles | HAUTE |
| W-002 | 20 % du public UK croit à des troubles civils — ce n'est pas de la peur, c'est de l'anticipation | HAUTE |
| W-003 | Le précédent Brookings est clair : sans amortisseurs, l'automatisation nourrit l'extrême droite. Or les amortisseurs français (Sécu, chômage) sont justement financés par... l'emploi menacé | HAUTE |
| W-004 | Aucun État n'a de stratégie politique publiée pour gérer le choc démocratique de l'IA — la réponse est entièrement économique/technique | HAUTE |

---

## IMPACTS

| Impact | Valeur | Source |
|--------|--------|--------|
| Public craignant pertes d'emploi IA (UK) | 70 % | KCL/Euronews, mai 2026 |
| Croyant à des troubles civils potentiels (UK) | 20 % | KCL/Euronews, mai 2026 |
| Employeurs ayant déjà réduit l'emploi à cause IA (UK) | 22 % | KCL/Euronews, mai 2026 |
| Travailleurs US craignant remplacement IA | 51 % | High5Test, mars 2026 |
| Européens craignant pour leur emploi (IA) | 25 % | DW, jan. 2026 |
| Licenciements attribués IA T1 2026 US | 49 123 | Fortune/Challenger, mai 2026 |
| Chômage France projeté | 7,8 % | DW, jan. 2026 |

---

## REQUEST_LOG

| QRY-ID | Query | Résultat |
|--------|-------|----------|
| Q-001 | AI automation political polarization 2025-2026 | Noema (Autor jan. 2026), Politico (oct. 2025), Populism Studies (avr. 2026) |
| Q-002 | UK AI survey civil unrest | Euronews/KCL (mai 2026) lu intégralement |
| Q-003 | Autor China Shock electoral impact | NBER 2016 confirmé, Brookings 2024 |
| Q-004 | Read Noema Autor interview | lu intégralement — 3 différences structurelles |

---

## LIMITES

- L'extrapolation du China Shock au choc IA est une analogie, pas une prédiction. Les différences structurelles (Autor) rendent la comparaison heuristique, pas mécanique.
- Aucune étude empirique ne mesure l'effet électoral de l'IA en 2026 — les données sont des sondages d'opinion.
- Le scénario « populisme de gauche » (Politico) est spéculatif.

## CONCLUSION

Le précédent du China Shock est clair : la destruction d'emplois, sans amortisseurs, nourrit le vote extrême. Mais le choc IA est structurellement différent : diffus, invisible, bienvenu des entreprises. Ces trois caractéristiques le rendent politiquement plus dangereux, pas moins — il n'y aura pas de « capitale du clérical » pour alerter, pas de concentration visible pour mobiliser, pas de résistance patronale pour ralentir. L'écart entre 70 % du public qui craint et 70 % des employeurs qui s'excite est une faille démocratique qui ne demande qu'à s'ouvrir.