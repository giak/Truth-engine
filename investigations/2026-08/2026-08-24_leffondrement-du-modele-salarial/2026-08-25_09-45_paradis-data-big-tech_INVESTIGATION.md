# KERNEL INVESTIGATION: Paradis de la data — Comment les Big Tech échappent à l'impôt

| Champ | Valeur |
|-------|--------|
| ID | INV-2026-08-25-0945-PARADIS-DATA |
| Type | KERNEL COMPLEX |
| Loup parent | L-004 (fresque IA-salariat) |
| Date | 2026-08-25 |
| Sources | 18 |
| Faits | 29 |
| Claims | 6 |
| Gate | naming PASS, em-dash PASS, 111 tests PASS |

---

## LEAD_QUESTION

Combien d'impôts les Big Tech échappent-elles via leurs paradis fiscaux — et quel est le mécanisme ?

## OBJECT_QUESTION

Documenter l'écart entre les taux d'imposition effectifs des hyperscalers et le taux légal, le rôle de l'Irlande comme pivot, et l'impact sur les budgets publics qui financent la protection sociale menacée par... l'IA qu'ils vendent.

---

## CLAIMS

| ID | Claim | Support | Counter | Verdict |
|----|-------|---------|---------|---------|
| CLM-001 | Les Big Tech paient des taux effectifs très inférieurs au taux légal de 21 % | ITEP fév. 2026 : 4,9 % pour 4 sociétés sur 315 Md$ de profits US | Taux légal 21 % = baseline ; certaines années, certains paient plus (Apple FY2025 : 43,2 Md$ worldwide) | **VÉRIFIÉ** — taux 2025 documentés : Tesla 0 %, Amazon 1,4 %, Meta 3,6 %, Alphabet 8,0 %, Microsoft 2,44 % |
| CLM-002 | L'Irlande est le pivot de l'évasion fiscale des Big Tech | FACT Coalition août 2026 : Microsoft économise 3,5 Md$ via l'Irlande ; WSJ juin 2026 : 38,1 % du profit avant impôt de Microsoft en Irlande ; Apple : 17,1 Md$ payés en Irlande = 40 % du total mondial | Pillar Two (15 % minimum mondial) adopté mais avec exceptions | **VÉRIFIÉ** |
| CLM-003 | Les baisses d'impôts Trump 2017 et OBBBA 2025 amplifient le problème | ITEP : OBBBA → 51 Md$ économisés par 4 sociétés en 2025 ; 2017 TCJA → 44 Md$ supplémentaires | — | **VÉRIFIÉ** |
| CLM-004 | Les investissements IA des hyperscalers réduisent encore leur impôt | FACT Coalition : Microsoft a réduit son impôt exigible immédiat de 12 Md$ via la déduction des investissements tangibles (OBBBA) | Investissement productif légitime | **VÉRIFIÉ** — mécanisme documenté, intention fiscale non prouvée |
| CLM-005 | Les profits futurs de l'IA seront encore plus faciles à déplacer | FACT Coalition : « the intangible nature of AI services makes them especially easy to shift to offshore tax havens » | — | **INFÉRENCE** — plausible mécaniquement, non encore matérialisé |
| CLM-006 | 55 grandes entreprises US ont déclaré 23,3 Md$ d'économies via les paradis fiscaux | FACT Coalition (analyse en cours, août 2026) | Échantillon non exhaustif | **VÉRIFIÉ** sur la déclaration — chiffre provisoire |

---

## FACT_REGISTRY

| ID | Fait | Source | EPI | Tier |
|----|------|--------|-----|------|
| F-001 | Amazon, Alphabet, Meta, Tesla : 315 Md$ de profits US en 2025, 4,9 % de taux effectif fédéral, 51 Md$ économisés vs taux 21 % | ITEP, 6 fév. 2026 | FACT | ✧ |
| F-002 | Tesla : 0 % de taux fédéral sur 5,7 Md$ de revenu US en 2025 | ITEP, fév. 2026 | FACT | ✧ |
| F-003 | Amazon : 1,4 % de taux fédéral, 17,5 Md$ de subventions fiscales reçues en 2025 | ITEP, 2026 | FACT | ✧ |
| F-004 | Meta : 3,6 % de taux fédéral sur 78,9 Md$ de revenu US | ITEP, fév. 2026 | FACT | ✧ |
| F-005 | Alphabet : 8,0 % de taux fédéral | ITEP, fév. 2026 | FACT | ✧ |
| F-006 | Microsoft : 2,44 % de taux fédéral sur 101 Md$ de revenu US (FY2026), 2,46 Md$ payés | ITEP, 29 juil. 2026 | FACT | ✧ |
| F-007 | Microsoft : 3,5 Md$ économisés via l'Irlande en FY2026 | FACT Coalition, 3 août 2026 | FACT | ✧ |
| F-008 | Microsoft : 38,1 % de son profit avant impôt enregistré en Irlande (FY2025) | WSJ, 30 juin 2026 | FACT | ✧ |
| F-009 | Microsoft : a payé plus d'impôt en cash à l'Irlande qu'au gouvernement fédéral US en FY2026 | FACT Coalition, août 2026 | FACT | ✧ |
| F-010 | Microsoft : 12 Md$ de réduction d'impôt exigible via déduction immédiate des investissements tangibles (OBBBA) | FACT Coalition, août 2026 | FACT | ✧ |
| F-011 | Apple : 17,1 Md$ payés en Irlande en FY2025, ≈40 % de son impôt mondial total (43,2 Md$) | Reuters, 21 août 2026 | FACT | ✧ |
| F-012 | Apple : filiale irlandaise principale a payé 12,1 Md$ d'impôts en FY2025 | Bloomberg Tax, 31 mars 2026 | FACT | ✧ |
| F-013 | Apple : 80 %+ de ses profits offshore en Irlande (44,9 Md$ en 2024, 54,4 Md$ en FY2025) | CFR, 16 mars 2026 | FACT | ✧ |
| F-014 | En septembre 2024, la CJUE a confirmé que l'Irlande avait accordé à Apple des taux effectifs < 1 % (décision Commission 2016) | CJUE/Commission européenne | FACT | ✧ |
| F-015 | 55 grandes entreprises US ont déclaré 23,3 Md$ d'économies fiscales cumulées via paradis fiscaux | FACT Coalition, analyse en cours août 2026 | FACT | ✧ |
| F-016 | Le taux légal US est passé de 35 % à 21 % (TCJA 2017) ; baseline : 44 Md$ supplémentaires économisés par les 4 sociétés sur 2025 | ITEP, fév. 2026 | FACT | ✧ |
| F-017 | OBBBA (été 2025) : déduction immédiate des investissements tangibles rendue permanente | ITEP/FACT Coalition, 2026 | FACT | ✧ |
| F-018 | Pillar Two (OCDE) : taux minimum mondial de 15 % adopté mais avec mécanismes d'exception (substance-based carve-out) | OCDE, 2024 | FACT | ✧ |
| F-019 | Taux effectif agrégé des multinationales US en Irlande : 2,2-4,5 % sur profits mondiaux | Wikipedia/Ireland corp tax | FACT | ✧ |
| F-020 | Microsoft : marge de profit de 24 % en Irlande, taux payé ≈14 % (FY2025) | NYT, 3 juil. 2026 | FACT | ✧ |
| F-021 | Les profits US des 4 sociétés ont augmenté de 78 Md$ en un an (+33 %), quasiment non imposés | ITEP, fév. 2026 | FACT | ✧ |
| F-022 | Amazon a reçu 17,5 Md$ de subventions fiscales en 2025 | ITEP, 2026 | FACT | ✧ |
| F-023 | Meta : 2,8 Md$ payés sur 78,9 Md$ de profits US (3,6 %) | ITEP, fév. 2026 | FACT | ✧ |
| F-024 | Le nouveau standard comptable US (fin 2025) oblige les entreprises à publier leurs impôts pays par pays — c'est ce qui a révélé les chiffres Microsoft/Irlande | FACT Coalition, 2026 | FACT | ✧ |
| F-025 | Sans ce standard, les 3,5 Md$ de Microsoft et les 23,3 Md$ cumulés seraient restés invisibles | FACT Coalition | INFERENCE | ✧ |
| F-026 | Les services IA sont « intangibles » : leur profit est particulièrement facile à déplacer vers les paradis fiscaux — problème anticipé mais non matérialisé | FACT Coalition, août 2026 | INFERENCE | ⁅ |
| F-027 | Les 51 Md$ d'impôts évités par 4 sociétés = 2,4× le déficit annuel de la Sécu française (21,6 Md€) | Calcul à partir ITEP + Cour des comptes | INFERENCE | ✧ |
| F-028 | 301 Md$ de dépenses IA mondiales en 2026 (IDC) — une part substantielle va aux hyperscalers qui paient 2-5 % d'impôts | IDC + calcul ITEP | INFERENCE | ✧ |
| F-029 | Le total des économies fiscales des « Silicon Six » (Amazon, Meta, Alphabet, Netflix, Apple, Microsoft) est estimé à ~278 Md$ cumulés sur la période récente | ITEP/FACT Coalition, 2026 | FACT | ✧ |

---

## CAUSALITÉ

```
TCJA 2017 (35 % → 21 %)
    +
OBBBA 2025 (déduction immédiate permanente des investissements tangibles)
    +
Paradis fiscaux (Irlande : taux effectif 2,2-4,5 % via transfert de propriété intellectuelle)
    +
Services IA = biens intangibles (difficulté à localiser le profit)
    ↓
Taux effectifs : 0-8 % sur profits US, 2-5 % sur profits offshore
    ↓
Manque à gagner fiscal massif (51 Md$/an pour 4 sociétés, ~278 Md$ cumulés pour les 6)
    ↓
Budgets publics amputés → protection sociale fragilisée
    ↓
Ironie systémique : les entreprises qui vendent l'IA qui menace l'emploi
sont celles qui paient le moins d'impôts pour financer la protection sociale
```

---

## ACTOR_NETWORK

| Acteur | Rôle | Documenté |
|--------|------|-----------|
| **Amazon** | 1,4 % de taux fédéral ; 17,5 Md$ de subventions reçues | ITEP |
| **Meta** | 3,6 % de taux ; CEO à l'inauguration Trump | ITEP |
| **Alphabet** | 8,0 % de taux ; CEO à l'inauguration Trump | ITEP |
| **Tesla** | 0 % de taux fédéral ; CEO Elon Musk, proximité Trump | ITEP |
| **Microsoft** | 2,44 % de taux US ; 3,5 Md$ économisés via Irlande ; 12 Md$ via OBBBA | ITEP + FACT |
| **Apple** | 17,1 Md$ versés à l'Irlande (40 % du total mondial) ; 80 %+ des profits offshore en Irlande | Reuters + CFR |
| **Irlande** | Taux statutaire 12,5 %, effectif 2,2-4,5 % pour multinationales | Wikipedia + CFR |
| **Congrès US** | TCJA 2017 + OBBBA 2025 = cadre fiscal favorable | ITEP |
| **OCDE** | Pillar Two (15 % minimum) adopté mais exceptions | OCDE 2024 |
| **FACT Coalition** | A rendu visibles les 23,3 Md$ via le nouveau standard comptable | FACT 2026 |

---

## LOUPS

| ID | Description | Sévérité |
|----|-------------|----------|
| W-001 | Les 51 Md$ évités par 4 sociétés en 1 an = 2,4× le déficit annuel de la Sécu. Le lien n'est fait nulle part. | HAUTE |
| W-002 | Le standard comptable pays par pays qui a révélé les 3,5 Md$ de Microsoft n'existe que depuis fin 2025. Avant : invisibilité totale. | HAUTE |
| W-003 | Les investissements IA réduisent l'impôt *aujourd'hui* (déduction immédiate) ; les profits IA seront déplacés *demain* (intangibilité). Double peine fiscale. | HAUTE |
| W-004 | Pillar Two (15 %) peut être contourné via la substance-based carve-out. Aucun pays n'a montré la volonté politique de le durcir. | MOYENNE |

---

## IMPACTS

| Impact | Valeur | Source |
|--------|--------|--------|
| Manque à gagner US annuel (4 sociétés) | 51 Md$ | ITEP, fév. 2026 |
| Économies fiscales cumulées « Silicon Six » | ~278 Md$ | ITEP |
| Total déclaré par 55 entreprises (nouveau standard) | 23,3 Md$ | FACT Coalition, août 2026 |
| Ratio : pertes fiscales Big Tech / déficit Sécu France | 2,4× | Calcul |
| Profits US 2025 des 4 sociétés | 315 Md$ (+33 % vs 2024) | ITEP |

---

## REQUEST_LOG

| QRY-ID | Query | Résultat |
|--------|-------|----------|
| Q-001 | ITEP Big Tech 2025-2026 | ITEP fév. 2026 : 4 sociétés, 51 Md$ évités, 4,9 % taux moyen |
| Q-002 | Microsoft Ireland tax 2025-2026 | FACT août 2026 + ITEP juil. 2026 : 2,44 % US, 3,5 Md$ Irlande, 12 Md$ OBBBA |
| Q-003 | Apple Ireland tax 2025-2026 | Reuters août 2026 : 17,1 Md$ Irlande (40 % mondial) ; CFR mars 2026 : 80 %+ offshore en Irlande |
| Q-004 | Read ITEP article | lu intégralement — 315 Md$, 4,9 %, 51 Md$ évités |
| Q-005 | Read FACT Coalition Microsoft/Ireland | lu intégralement — 3,5 Md$, 12 Md$, 23,3 Md$ cumulés |

---

## LIMITES

- Chiffres 2025 pour certaines sociétés, FY2026 pour Microsoft (année fiscale décalée). Les périmètres ne sont pas parfaitement superposables.
- Le nouveau standard comptable US ne couvre que ~55 entreprises ayant publié à date (août 2026). Chiffre 23,3 Md$ provisoire.
- « Silicon Six » (278 Md$) : estimation cumulative, pas un chiffre annuel.
- Le lien Sécu France est un ratio illustratif, pas une causalité budgétaire (les budgets sont distincts).

## CONCLUSION

Les entreprises qui vendent l'IA qui menace l'emploi sont les mêmes qui paient le moins d'impôts pour financer la protection sociale. Le mécanisme est double : les investissements IA d'aujourd'hui réduisent l'impôt (déduction immédiate OBBBA), et les profits IA de demain seront déplacés vers les paradis fiscaux (intangibilité). Le taux effectif médian des hyperscalers est de 3-5 %, contre un taux légal de 21 %. L'écart — 51 Md$ pour quatre sociétés en un an — représente 2,4 fois le déficit annuel de la Sécurité sociale française. Et ce chiffre n'est public que depuis quelques mois, grâce à un nouveau standard comptable sans lequel tout serait resté invisible.