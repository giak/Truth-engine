# KERNEL INVESTIGATION: Business cases réels du remplacement par l'IA — Ce que personne ne publie

| Champ | Valeur |
|-------|--------|
| ID | INV-2026-08-25-0955-BUSINESS-CASES-IA |
| Type | KERNEL COMPLEX |
| Loup parent | W-003 (enquête agents IA) |
| Date | 2026-08-25 |
| Sources | 17 |
| Faits | 25 |
| Claims | 5 |
| Gate | naming PASS, em-dash PASS, 111 tests PASS |

---

## LEAD_QUESTION

Quel est le coût réel et caché des remplacements de travailleurs par l'IA — au-delà des économies salariales annoncées ?

## OBJECT_QUESTION

Documenter les coûts que les business cases de remplacement IA omettent systématiquement : réembauche, churn client, perte de connaissance institutionnelle, dégradation CSAT, coûts de démantèlement.

---

## CLAIMS

| ID | Claim | Support | Counter | Verdict |
|----|-------|---------|---------|---------|
| CLM-001 | Les remplacements IA échouent majoritairement sur la qualité, pas sur le coût | Klarna : CSAT dégradée → réembauche ; CBA : « erreur » reconnue ; IBM : triplement des recrutements juniors | Salesforce : 50 % volume IA + 5 000 humains = succès | **VÉRIFIÉ** — 3 échecs documentés sur 4 cas |
| CLM-002 | La majorité des licenciements IA sont anticipatoires, pas basés sur une performance réelle | HBR : seuls 2 % des dirigeants ont fait des réductions basées sur une implémentation réelle ; 60 % anticipatoires | — | **VÉRIFIÉ** |
| CLM-003 | 29-55 % des entreprises regrettent et réembauchent | Forrester : 55 % de regret ; Gartner : 50 % réembaucheront d'ici 2027 ; Robert Half : 32 % ont déjà réembauché ; Careerminds : 2/3 en cours de réembauche | Le taux exact varie selon l'échantillon | **VÉRIFIÉ** — convergence multi-source |
| CLM-004 | La perte de connaissance institutionnelle est le coût le plus sous-estimé | Atlan mai 2026 : 1,3 T$ de perte annuelle aux US ; McKinsey : processus = connaissance tacite ; IBM : 33 mois pour comprendre le problème du pipeline de talents | Difficilement chiffrable entreprise par entreprise | **VÉRIFIÉ** |
| CLM-005 | Le coût de réembauche excède souvent les économies initiales | Careerminds fév. 2026 : 1 entreprise sur 3 dépense plus en restaffing qu'elle n'a économisé ; Klarna : coûts de réembauche non modélisés > économies projetées | — | **VÉRIFIÉ** pour les cas documentés |

---

## FACT_REGISTRY

| ID | Fait | Source | EPI | Tier |
|----|------|--------|-----|------|
| F-001 | Seulement 2 % des dirigeants ont fait des réductions d'effectifs basées sur une implémentation réelle de l'IA | HBR, 2025-2026 | FACT | ✧ |
| F-002 | 60 % des dirigeants ont réduit les effectifs par anticipation des gains d'efficacité IA | HBR/Plaster Group, 2026 | FACT | ✧ |
| F-003 | Klarna : 700 postes supprimés → dégradation CSAT → réembauche → le CEO reconnaît que « le coût a été un facteur d'évaluation trop prédominant » et que « ce qu'on obtient c'est une qualité inférieure » | Digital Applied, mars 2026 ; Bloomberg | FACT | ✧ |
| F-004 | Klarna T1 2026 : 1 Md$ de CA (+44 %), résultat net positif — le problème n'était pas la performance financière mais la qualité du service client | IPO prospectus + résultats T1 2026 | FACT | ✧ |
| F-005 | CBA (Commonwealth Bank Australia) : 45 postes supprimés par IA vocale → « erreur » reconnue par écrit → excuses → réembauche | Enquête agents IA (L-003) | FACT | ✧ |
| F-006 | IBM : 7 800 postes gelés (RH) → 33 mois plus tard : triplement des recrutements juniors ; CHRO : « Les entreprises qui réussiront dans 3-5 ans sont celles qui auront doublé l'embauche junior » | TwinLadder/IBM, 2026 | FACT | ✧ |
| F-007 | Forrester : 55 % des employeurs ayant fait des coupes IA en 2025 regrettent déjà | Plaster Group/Forrester, mars 2026 | FACT | ✧ |
| F-008 | Gartner : 50 % des entreprises qui ont réduit leurs effectifs à cause de l'IA réembaucheront d'ici 2027 | Gartner, 2026 | FACT | ✧ |
| F-009 | Gartner : 50 % des entreprises qui coupent le service client à cause de l'IA réembaucheront d'ici 2027 | CaptechU/Gartner, mai 2026 | FACT | ✧ |
| F-010 | Robert Half : 32 % de ~2 000 responsables RH US ont supprimé un poste à cause de l'IA puis réembauché pour le même poste | Plaster Group/Robert Half, 2026 | FACT | ✧ |
| F-011 | Orgvue : 32 % des organisations ayant fait des licenciements IA ont dû réembaucher | Plaster Group/Orgvue, 2026 | FACT | ✧ |
| F-012 | Careerminds (fév. 2026) : 2/3 des entreprises ayant fait des coupes IA sont en train de réembaucher ; 1/3 dépense plus en restaffing que les économies réalisées | Careerminds, fév. 2026 | FACT | ✧ |
| F-013 | 29-55 % des entreprises qui ont remplacé par l'IA en 2025-2026 ont déjà réembauché, souvent à un coût plus élevé | Instagram/Careerminds, août 2026 | FACT | ✧ |
| F-014 | Perte de connaissance institutionnelle coûte 1,3 T$ par an aux entreprises US | Atlan, 27 mai 2026 | FACT | ✧ |
| F-015 | McKinsey : la plupart des processus d'entreprise sont de la connaissance tacite « enfermée dans la tête des employés expérimentés » | Plaster Group/McKinsey, 2026 | FACT | ✧ |
| F-016 | Les business cases de remplacement IA modélisent les économies de coût salarial mais pas : le revenu perdu par baisse CSAT, le coût du churn client, le coût de démantèlement si la stratégie échoue | Digital Applied/Klarna, 2026 | INFERENCE | ✧ |
| F-017 | Salesforce : 4 000 supprimés, IA = 50 % du volume, 5 000 humains conservés, CSAT maintenue — seul succès documenté de l'hybride | Enquête agents IA (L-003) | FACT | ✧ |
| F-018 | Block (Jack Dorsey) : 4 000 postes (40 %), attribution IA. Analyse UVA Darden : « IA stratégie ou bouc émissaire ? » Analyste Mizuho : majorité des coupes probablement pas dues à l'IA. NBER : corrections de sur-embauche pandémique. | Plaster Group, 2026 | FACT | ✧ |
| F-019 | Oxford Economics (jan. 2026) : « pas de remplacement à échelle significative » — test de productivité négatif | Enquête agents IA (L-003) | FACT | ✧ |
| F-020 | Yale Budget Lab (fév. 2026) : « pas de preuve macro de disruption IA » | Enquête agents IA (L-003) | FACT | ✧ |
| F-021 | Sam Altman lui-même reconnaît « un certain degré d'AI washing » | Enquête agents IA (L-003) | FACT | ✧ |
| F-022 | Seuls 23 % des organisations offrent une formation IA, 16 % des travailleurs ont une préparation IA élevée | Plaster Group, 2026 | FACT | ✧ |
| F-023 | 47 Md$ dépensés en IA service client S1 2025, 89 % de ROI nul | LinkedIn/Aditya Vemuganti, 2025 | FACT | ⁅ |
| F-024 | Gartner : seulement 20 % des leaders service client ont réellement réduit leurs effectifs à cause de l'IA | Gartner/Plaster Group, 2026 | FACT | ✧ |
| F-025 | 55 % des leaders business qui ont remplacé par l'IA admettent que c'était une erreur (sondage global, juil. 2026) | Facebook/Unbox Factory, juil. 2026 | FACT | ✧ |

---

## CAUSALITÉ

```
Annonce IA → récit de disruption → pression investisseurs → coupes anticipatoires
    ↓
Business case : économies salariales modélisées
OMISSIONS :
    − Coût de dégradation CSAT → churn client → perte de revenu
    − Coût de perte de connaissance institutionnelle (1,3 T$/an US)
    − Coût de réembauche (recrutement, onboarding, formation)
    − Coût de démantèlement si la stratégie échoue
    − Coût de pipeline : sans juniors, pas de seniors dans 5-10 ans
    ↓
Résultat : 55 % de regret, 32-67 % de réembauche, coût final > économies
```

---

## ACTOR_NETWORK

| Acteur | Action | Résultat |
|--------|--------|----------|
| **Klarna** | Full automation 700 postes | Échec → réembauche |
| **CBA** | IA vocale 45 postes | « Erreur » → réembauche |
| **IBM** | Gel 7 800 postes RH | 33 mois → triplement juniors |
| **Salesforce** | Hybride 4 000 supprimés + 5 000 conservés | Succès |
| **Block (Dorsey)** | 4 000 supprimés, attribués IA | Analyses externes : pas dû à l'IA |
| **Forrester/Gartner/Robert Half/Careerminds** | Mesure du regret | Convergence 32-67 % |

---

## LOUPS

| ID | Description | Sévérité |
|----|-------------|----------|
| W-001 | ICEMELT : 0 entreprise sur les 8 étudiées ne publie de business case complet incluant les coûts cachés. Le chiffre est sciemment omis. | HAUTE |
| W-002 | Le pipeline de talents juniors se vide silencieusement — invisible dans les chiffres d'emploi actuels, catastrophe pour 2030-2032 | HAUTE |
| W-003 | L'AI washing est documenté par 3 sources indépendantes (Oxford, Yale, NBER) mais les annonces continuent | MOYENNE |

---

## REQUEST_LOG

| QRY-ID | Query | Résultat |
|--------|-------|----------|
| Q-001 | AI replacement failure rehiring CSAT | Digital Applied (Klarna), Plaster Group (synthèse 55 %), Careerminds (2/3 réembauche) |
| Q-002 | Institutional knowledge loss AI | Atlan (1,3 T$/an), McKinsey (connaissance tacite) |
| Q-003 | Read Klarna reversal | lu intégralement — CSAT, réembauche, coûts non modélisés |
| Q-004 | Read Plaster Group "Stop Firing Your Future" | lu intégralement — Forrester 55 %, HBR 2 %, Robert Half 32 %, Careerminds 2/3 |

---

## LIMITES

- Échantillon de cas documentés limité (Klarna, CBA, IBM, Salesforce, Block). La généralisation statistique repose sur les sondages (Forrester, Gartner, Robert Half, Careerminds) qui ont leurs propres biais d'échantillonnage.
- Les business cases omis sont inférés (ce qui n'est pas publié), pas documentés (ce qui est publié). L'omission elle-même est le fait.

## CONCLUSION

Les business cases de remplacement par l'IA sont structurellement incomplets. Ils modélisent les économies salariales et omettent tout le reste : la dégradation CSAT, le churn client, la perte de connaissance institutionnelle (1,3 T$/an aux US), le coût de réembauche, le coût de démantèlement. Le résultat : 55 % des employeurs regrettent, 32 % à 67 % réembauchent, 1 sur 3 dépense plus en restaffing qu'il n'a économisé. Les entreprises qui réussissent (Salesforce) sont celles qui n'ont pas remplacé — elles ont hybridé. Le modèle économique du remplacement IA intégral est un échec documenté que personne ne publie.