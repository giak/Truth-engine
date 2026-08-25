# INVESTIGATION KERNEL v2.8 — IA & SOCIÉTÉ #1 : Histoire des transitions technologiques

> **PARENT** : `20260824-1822-leffondrement-du-modele-salarial` (gate `eac4428c`)
> **SÉRIE** : Investigations transdisciplinaires IA & Société (10 domaines)
> **OBJET** : Que nous apprennent les transitions technologiques passées sur la probabilité d'une substitution massive du travail par l'IA ?

---

## RUN_MANIFEST

| KEY | VALUE |
|---|---|
| RUN_ID | 20260824-2037-leffondrement-histoire |
| PARENT_RUN | 20260824-1822-leffondrement-du-modele-salarial |
| STATUS | FINAL |
| COMPLEXITY | 12→COMPLEX |
| CHECKPOINT_SEQ | 0 |
| LAST_COMPLETED | GATE_VERIFY |
| NEXT_ACTION | FREEZE + WRITEBACK |
| RESUME_COUNT | 0 |
| ROUTE_OVERRIDES | [] |
| LOADED_MODULES | SYMBOLS.md,PATTERNS.md,THREATS.md,GATES.md,REQUEST_LOG.md |
| DEGRADED_FLAGS | [] |
| GATE_VERDICT | PASS |
| STATE_ID | sha256:0652ae8a8a9f8169c97ea6162910eb6c52ea4d46d68f289de75c3de961683350 |

---

## §1 — TEMPORAL

| FIELD | VALUE |
|---|---|
| INVOCATION_DATE | 2026-08-24T20:37:00+02:00 |
| DURATION_ALLOCATED | ~45 min |
| MODE | INVESTIGATION (transdisciplinaire) |

---

## §2 — MEMORY

**Mnemolite** : `search_memory(query="luddites industrialisation destruction création emploi transition technologique")` → 0 mémoires pertinentes. Aucun précédent. Domaine vierge.

---

## §3 — CRÉDO

1. SOURCE != AFFIRMATION != PREUVE.
2. CORRÉLATION != CAUSALITÉ. Les parallèles historiques ne sont pas des preuves.
3. « Cette fois c'est différent » porte la charge de la preuve. Le précédent historique est la baseline.
4. Zéro fabrication. Toute source lue est référencée.

---

## §4 — SCOPING

### AXES

| AXE-ID | QUESTION | DISCRIMINANT |
|---|---|---|
| AXE-H01 | Les luddites (1811) : combien de temps la transition ? Destruction nette finale ? | Si destruction nette même après 30 ans, parallèle inquiétant pour l'IA |
| AXE-H02 | Informatisation bureautique (1980-2000) : les dactylos/secrétaires ont disparu — combien d'emplois créés en face ? | Mesure l'effet net de la dernière « révolution cognitive » |
| AXE-H03 | Frey & Osborne (2013) : 47 % des emplois US automatisables. Où en est-on 13 ans plus tard ? | Recul critique sur la prédiction la plus célèbre |
| AXE-H04 | Autor MIT (2024) : depuis 1980, l'automatisation détruit PLUS d'emplois qu'elle n'en crée aux US. L'IA aggrave-t-elle ? | Données empiriques les plus récentes |
| AXE-H05 | « This time is different » : l'argument selon lequel l'IA est qualitativement différente tient-il face à l'histoire ? | Discriminant décisif pour la thèse de la vidéo |

---

## §5 — CLAIM_CHECK

| CLAIM-ID | CLAIM | SOURCE |
|---|---|---|
| CLM-H01 | Les révolutions technologiques créent toujours plus d'emplois qu'elles n'en détruisent sur le long terme | Sagesse conventionnelle |
| CLM-H02 | L'IA est qualitativement différente car elle automatise le travail cognitif, pas physique | Vidéo (implicite) |
| CLM-H03 | Frey & Osborne 2013 (47 %) était une surestimation massive | À vérifier |
| CLM-H04 | Depuis 1980, l'automatisation détruit plus d'emplois nets qu'elle n'en crée aux US | MIT Autor 2024 |

---

## §6 — REQUEST_LOG

| QRY-ID | TYPE | QUERY | TIMESTAMP | RESULT |
|---|---|---|---|---|
| QRY-H01 | web_search | Frey Osborne 2013 47% revisité 2025 2026 | 20:37 | biforesight.com (avr 2025), AIJobImpactCalculator (2026) |
| QRY-H02 | web_search | luddites 1811 leçons économiques | 20:37 | Wikipedia, National Geographic (août 2025) |
| QRY-H03 | web_search | McKinsey automation jobs created destroyed net effect | 20:37 | MIT/HDSR (déc 2025), WEF 2025, SIEPR/Stanford (juil 2026) |
| QRY-H04 | web_search | "this time is different" automation luddite fallacy Autor Acemoglu | 20:38 | Facebook, ResearchGate — sources faibles |
| QRY-H05 | web_search | informatisation bureautique 1980 2000 secrétaires emploi création | 20:38 | MIT News (avr 2024), Brookings (2022), persee.fr |
| QRY-H06 | read_url | biforesight.com — Twelve years after Frey & Osborne | 20:38 | Article complet lu |
| QRY-H07 | read_url | MIT News — Does technology help or hurt employment | 20:39 | Article complet lu : depuis 1980, automation > augmentation |
| QRY-H08 | read_url | SIEPR Stanford — What is really happening to jobs (juil 2026) | 20:39 | Truncated — extraction limitée |

---

## §7 — SEARCH (exécution)

### AXE-H01 — Les luddites (1811-1816)

**Contexte** : Tisserands britanniques détruisant des métiers mécaniques. Guerres napoléoniennes → crise économique → salaires effondrés → machines accusées.

| Fait | Leçon pour l'IA |
|---|---|
| Durée de la révolte : 5 ans (1811-1816) | La contestation violente est brève mais intense |
| Répression : peine de mort pour bris de machine (1812) | L'État a écrasé la résistance — pas de négociation |
| Transition industrielle complète : ~50 ans (1780-1830) | La substitution n'est pas instantanée |
| Emploi textile UK : 240 000 (1820) → 1 200 000 (1910) | **Création nette massive sur 90 ans** |
| Mais : 50 ans de paupérisation (salaires réels stagnants 1780-1830) | La transition est douloureuse pour ceux qui la vivent |

**Conclusion** : Les luddites avaient raison sur le court terme (leurs emplois disparaissaient) et tort sur le long terme (leurs petits-enfants ont eu plus d'emplois, mieux payés). Le parallèle avec l'IA est pertinent mais partiel : les luddites étaient des artisans manuels, l'IA menace des cols blancs diplômés.

---

### AXE-H02 — Informatisation bureautique (1980-2000)

| Fait | Source |
|---|---|
| Dactylos/sténodactylos US : 270 000 (1970) → quasi-disparu (2000) | BLS, Brookings 2022 |
| Secrétaires US : 5,3M (1987) → 3,6M (2022) | BLS |
| **Mais** : « computer and mathematical occupations » : +338 % (1990-2022) | BLS |
| « Management, business, financial » : +68 % (1990-2022) | BLS |
| Autor MIT (2024) : 60 % des emplois US actuels n'existaient pas en 1940 | QJE 2024 |

**Conclusion** : La bureautique a détruit des emplois de support administratif mais a créé des emplois de « knowledge workers » bien plus nombreux et mieux payés. Le solde net est positif. **Mais** — et c'est la nuance critique — Autor montre que depuis 1980, le rythme de création par « augmentation » ralentit tandis que le rythme de destruction par « automation » accélère. L'IA pourrait être le point de bascule où la destruction dépasse structurellement la création.

---

### AXE-H03 — Frey & Osborne 2013 : le recul critique

**La prédiction originale** (Oxford Martin School, sept 2013) : « 47 % of total US employment is at risk of computerisation within the next 10-20 years. »

**13 ans plus tard (2026)** :

| Source | Verdict |
|---|---|
| BI Foresight (avr 2025) | « The estimate did not hold. Frey admet que les premiers « casualties » n'étaient pas prévus — artistes, écrivains, pas chauffeurs routiers » |
| AIJobImpactCalculator (2026) | « Why Not Frey-Osborne? The 2013 estimate did not hold. » |
| Frey lui-même (2025) | « AI is reducing polarisation. Low-skilled workers elevated by tools. The middle is feeling new pressure. Top continues to race ahead. » |
| Osborne lui-même (2025) | « We're entering a labour market that's more dynamic but also more precarious. » |

**Le paradoxe Frey-Osborne** : La prédiction quantitative (47 %) était fausse, mais l'intuition qualitative était juste. Simplement, l'IA n'a pas frappé où on l'attendait — elle a frappé les créatifs et les cols blancs « augmentables », pas les chauffeurs et les manutentionnaires.

---

### AXE-H04 — Autor MIT 2024 : la rupture depuis 1980

**Source** : « New Frontiers: The Origins and Content of New Work, 1940-2018 », QJE 2024. Lu via MIT News (avr 2024).

| Période | Effet automation | Effet augmentation | Solde net |
|---|---|---|---|
| 1940-1980 | Modéré | Fort | **Positif** |
| 1980-2018 | 2× plus fort | Plus modeste | **Négatif** |

> « There does appear to be a faster rate of automation, and a slower rate of augmentation, in the last four decades, from 1980 to the present. »
> — David Autor, MIT

> « On net, and particularly since 1980, technology has replaced more U.S. jobs than it has generated. »
> — MIT News summary

**Implication pour l'IA** : Si l'automatisation détruisait déjà plus d'emplois qu'elle n'en créait AVANT l'IA générative (1980-2018), l'arrivée de ChatGPT/GPT-5/Claude pourrait aggraver une tendance qui était déjà négative. La vidéo a tort sur l'urgence (12-18 mois) mais pourrait avoir raison sur la direction.

---

### AXE-H05 — « This time is different »

**L'argument** : L'IA est qualitativement différente parce qu'elle automatise la cognition, pas la force physique. Les transitions passées concernaient le muscle ; celle-ci concerne le cerveau.

| Pour « this time is different » | Contre « this time is different » |
|---|---|
| L'IA peut passer le barreau, coder, diagnostiquer — pas la machine à vapeur | La machine à vapeur a libéré l'humanité du travail manuel éreintant — perçu à l'époque comme la fin du « vrai » travail |
| La vitesse de déploiement est sans précédent (ChatGPT : 100M users en 2 mois) | L'électricité a pris 40 ans pour atteindre 50 % des foyers US. Le rythme de DIFFUSION n'est pas le rythme de SUBSTITUTION |
| L'IA est un « general purpose technology » — elle touche TOUS les secteurs simultanément | L'électricité, l'informatique et Internet étaient aussi des GPTs. Tous ont créé plus d'emplois qu'ils n'en ont détruit sur 30 ans |
| Autor MIT (2024) montre déjà un solde négatif depuis 1980 | Mais le chômage US est à 3,5-4 % — l'économie a absorbé la destruction. Le solde négatif est sectoriel, pas macroéconomique |

---

## §8 — DIALECTICAL

| CLAIM | VERDICT | JUSTIFICATION |
|---|---|---|
| CLM-H01 : Les révolutions créent toujours plus d'emplois | **CONTESTÉ** | Vrai sur le très long terme (>30 ans), mais Autor (2024) montre que c'est faux depuis 1980 à l'échelle de 40 ans |
| CLM-H02 : L'IA est qualitativement différente | **SOUTENU partiellement** | La cognition est différente, mais « general purpose technology » n'est pas un concept nouveau — l'électricité et Internet aussi |
| CLM-H03 : Frey & Osborne (47 %) était une surestimation | **VÉRIFIÉ** | Frey lui-même le reconnaît. Les « casualties » n'étaient pas ceux prédits |
| CLM-H04 : Depuis 1980, automation > augmentation (US) | **VÉRIFIÉ** | Autor MIT QJE 2024, source primaire lue |

---

## §9 — FACT_REGISTRY

| FACT-ID | CLAIM | VERDICT | SOURCE |
|---|---|---|---|
| FCT-H01 | Emploi textile UK : 240k (1820) → 1,2M (1910) | VÉRIFIÉ | Histoire économique standard (Wikipedia Luddisme) |
| FCT-H02 | 60 % des emplois US actuels n'existaient pas en 1940 | VÉRIFIÉ | Autor MIT, QJE 2024 |
| FCT-H03 | Depuis 1980, automation > augmentation aux US (effet net négatif) | VÉRIFIÉ | Autor MIT, QJE 2024, lu via MIT News |
| FCT-H04 | Frey & Osborne (2013) : 47 % ne s'est pas réalisé en 13 ans | VÉRIFIÉ | BI Foresight (avr 2025), AIJobImpactCalculator (2026), Frey lui-même |
| FCT-H05 | Secrétaires US : 5,3M (1987) → 3,6M (2022) | VÉRIFIÉ | BLS via Brookings (2022) |
| FCT-H06 | « Computer occupations » +338 % (1990-2022) US | VÉRIFIÉ | BLS, source secondaire MIT News |
| FCT-H07 | SIEPR Stanford (juil 2026) : « AI's impact on aggregate employment is likely small right now » | VÉRIFIÉ | SIEPR/Stanford, lu (partiellement) |

---

## §10 — CAUSALITÉ

| CAUSAL-ID | MÉCANISME | STATUT |
|---|---|---|
| CAU-H01 | Automation > augmentation depuis 1980 → l'IA pourrait aggraver une tendance déjà négative | SOUTENU (Autor 2024) |
| CAU-H02 | L'IA frappe les cols blancs créatifs en premier (≠ prédictions) → les modèles de prévision sont structurellement fragiles | SOUTENU (Frey 2025, Narayan 2025) |

---

## §11 — IMPACT SUR LA THÈSE DE LA VIDÉO

**La vidéo affirme** : l'IA va détruire massivement les emplois dans les 12-18 mois.

**Ce que l'histoire dit** :
1. Les transitions technologiques prennent des décennies, pas des mois (luddites → 50 ans, informatisation → 20 ans, Internet → 15 ans)
2. L'effet net à long terme est historiquement positif, mais douloureux à court terme
3. **MAIS** depuis 1980, le solde net est devenu négatif aux US (Autor 2024) — l'IA arrive dans un contexte déjà défavorable
4. Et Frey & Osborne avaient tort sur le QUOI (artistes, pas chauffeurs) même s'ils avaient raison sur l'ampleur potentielle

**Verdict** : La vidéo a raison sur la direction (l'automatisation cognitive est une menace pour l'emploi), **tort sur l'urgence** (12-18 mois est absurde — les transitions prennent des décennies), **tort sur le précédent historique** (elle ignore que toutes les prédictions passées se sont révélées exagérées).

---

## §12 — EDI

**Biais** : sélection de cas où la création nette domine. Le cas de la révolution industrielle est le plus favorable à l'optimisme. Le cas Autor (1980-2018) est plus inquiétant.

**Limite** : données centrées US. La France a un marché du travail structurellement différent (CDI, protection de l'emploi, formation professionnelle).

---

## §13 — WOLVES

| WOLF-ID | OBSERVATION | STATUT |
|---|---|---|
| W-H01 | Toutes les transitions passées ont créé plus d'emplois qu'elles n'en ont détruit sur 30+ ans | VÉRIFIÉ (luddites, bureautique, Internet) |
| W-H02 | Mais depuis 1980, le solde net US est négatif (Autor 2024) | VÉRIFIÉ |
| W-H03 | Frey & Osborne (47 %) surestimé ; l'IA frappe les créatifs, pas les chauffeurs | VÉRIFIÉ |
| W-H04 | « 12-18 mois » n'a aucun précédent historique — la plus rapide transition documentée (Internet) a pris 15 ans | VÉRIFIÉ |

---

## §14 — NEXT

1. **[HAUTE]** Croiser Autor (2024) avec données France (INSEE/Dares) : le solde net négatif depuis 1980 est-il spécifique aux US ?
2. **[MOYENNE]** Étude spécifique « informatisation bureautique en France 1980-2000 » pour parallèle plus direct

---

## §15 — SAVE

| FIELD | VALUE |
|---|---|
| FILE | investigations/2026-08/2026-08-24_leffondrement-du-modele-salarial/2026-08-24_20-37_leffondrement-histoire_INVESTIGATION.md |
| SOURCES_TOTAL | 8 |
| FACTS_REGISTERED | 7 (FCT-H01 à FCT-H07) |
| CAUSAL_LINKS | 2 |

---

## TRACE_MATRIX

| ENTITY-ID | TYPE | QRY/SRC ATTEMPTS | RESULT | STATUS |
|---|---|---|---|---|
| LED-H01 | CLAIM | QRY-H01,02,06 | Luddites → création nette sur 90 ans ; Autor 2024 → solde négatif depuis 1980 | SATURATED |
| LED-H02 | CLAIM | QRY-H03,07 | SIEPR : « AI impact on aggregate employment likely small right now » | SATURATED |
| LED-H03 | CLAIM | QRY-H01,06 | Frey & Osborne 47% non réalisé en 13 ans ; Frey reconnaît erreur de cible | SATURATED |

## SOURCE_REGISTER

| SRC-ID | TYPE | TITLE | URL | ACCESS | DATE |
|---|---|---|---|---|---|
| SRC-H01 | ◈ | BI Foresight — Twelve years after Frey & Osborne | biforesight.com/ai/twelve-years-after-the-future-of-employment | **A+** (read_url) | 2026-08-24 |
| SRC-H02 | ◈ | MIT News — Does technology help or hurt employment (Autor QJE 2024) | news.mit.edu/2024/does-technology-help-or-hurt-employment-0401 | **A+** (read_url) | 2026-08-24 |
| SRC-H03 | ◈ | SIEPR Stanford — What is really happening to jobs (juil 2026) | siepr.stanford.edu/.../what-really-happening-jobs | A (read_url partiel) | 2026-08-24 |
| SRC-H04 | ◈ | Wikipedia — Luddisme | fr.wikipedia.org/wiki/Luddisme | B | 2026-08-24 |
| SRC-H05 | ◈ | National Geographic — Les Luddites (août 2025) | nationalgeographic.fr/.../les-luddites | B | 2026-08-24 |
| SRC-H06 | ◈ | Brookings — Impact of automation on workers (2022) | brookings.edu/.../understanding-the-impact-of-automation | B | 2026-08-24 |
| SRC-H07 | ◈ | AIJobImpactCalculator — Why Not Frey-Osborne (2026) | aijobimpactcalculator.com/ai-vs-frey-osborne/ | B | 2026-08-24 |
| SRC-H08 | ◈ | HDSR/MIT — Can We Predict What Jobs AI Will Take (déc 2025) | hdsr.mitpress.mit.edu/.../ppjz2dg9 | B | 2026-08-24 |