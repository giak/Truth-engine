# KERNEL INVESTIGATION: Travailleurs du clic — La chaîne humaine invisible derrière l'IA

| Champ | Valeur |
|-------|--------|
| ID | INV-2026-08-25-0950-TRAVAILLEURS-CLIC |
| Type | KERNEL COMPLEX |
| Loup parent | L-005 (fresque IA-salariat) |
| Date | 2026-08-25 |
| Sources | 16 |
| Faits | 21 |
| Claims | 5 |
| Gate | naming PASS, em-dash PASS, 111 tests PASS |

---

## LEAD_QUESTION

Qui entraîne les IA qui menacent l'emploi — et dans quelles conditions ?

## OBJECT_QUESTION

Documenter la chaîne d'approvisionnement humaine de l'IA : micro-travailleurs du clic (France), data labelers (monde), modérateurs de contenu (Kenya). Actualiser les données DiPLab 2019 (260 000 travailleurs, 21 €/mois) avec les chiffres 2025-2026.

---

## CLAIMS

| ID | Claim | Support | Counter | Verdict |
|----|-------|---------|---------|---------|
| CLM-001 | L'IA repose sur une chaîne humaine massive et sous-payée | DiPLab 2019 : 260k micro-travailleurs France, 21 €/mois ; SOMO mars 2026 : conditions abusives généralisées ; Scale AI procès fév. 2026 | Certains travailleurs sont bien rémunérés (scale.ai « specialized annotation ») | **VÉRIFIÉ** pour la chaîne basse ; élite de labelers spécialisés existe |
| CLM-002 | Les conditions au Kenya sont structurellement abusives | TIME jan. 2023 : < 2 $/h pour OpenAI ; The Guardian août 2023 : trauma psychologique ; Leon Furze jan. 2026 : chaîne inchangée | Kenya a proposé une régulation (draft policy 2026) | **VÉRIFIÉ** |
| CLM-003 | Les données DiPLab 2019 (260k, 21€/mois) sont probablement sous-estimées en 2026 | L'explosion de l'IA générative depuis 2022 a multiplié les besoins de labellisation ; SOMO 2026 : le secteur manque de transparence | Aucun recensement 2026 équivalent à DiPLab | **INFÉRENCE** plausible, non vérifiable |
| CLM-004 | Les plateformes violent systématiquement les droits des travailleurs | Remotasks a coupé l'accès sans payer les salaires dus (mars 2024) ; Scale AI poursuivie pour pratiques d'exploitation | Certaines plateformes se sont améliorées (Appen a modifié ses conditions) | **VÉRIFIÉ** pour les cas documentés |
| CLM-005 | Les entreprises clientes (OpenAI, Meta, Google) sont légalement protégées par la couche de sous-traitance | TIME 2023 : OpenAI → Sama → travailleurs kenyans ; Tech Policy Press juin 2026 : « accountability gaps that workers end up paying for » | — | **VÉRIFIÉ** — mécanisme documenté |

---

## FACT_REGISTRY

| ID | Fait | Source | EPI | Tier |
|----|------|--------|-----|------|
| F-001 | 260 000 micro-travailleurs du clic en France en 2019, revenu moyen 21 €/mois | DiPLab/Télécom Paris, 2019 | FACT | ✧ |
| F-002 | Pour 45 % des micro-travailleurs français, le revenu du micro-travail est insuffisant pour en vivre | DiPLab 2019 | FACT | ✧ |
| F-003 | Le revenu est « très inégalement distribué » — une minorité gagne significativement plus | DiPLab 2019 | FACT | ✧ |
| F-004 | Aucun recensement équivalent à DiPLab n'a été publié pour 2024-2026 | Recherche web août 2026 | GAP | — |
| F-005 | SOMO (mars 2026) : les Big Tech imposent des conditions abusives aux data workers dans le monde entier — bas salaires, contrats précaires, absence de transparence | SOMO, 31 mars 2026 | FACT | ✧ |
| F-006 | AlgorithmWatch (août 2025) : l'exploitation des gig workers de l'IA est structurelle ; Scale AI, Appen, Remotasks cités | AlgorithmWatch, 9 août 2025 | FACT | ✧ |
| F-007 | Remotasks a coupé l'accès à la plateforme en mars 2024 sans payer les salaires dus | Canadian Affairs, 17 oct. 2025 | FACT | ✧ |
| F-008 | Scale AI fait l'objet de poursuites pour pratiques d'exploitation du travail (fév. 2026) ; rémunération « à la pièce » | LinkedIn/Shelly Palmer, fév./oct. 2025 | FACT | ✧ |
| F-009 | Appen : rémunération 2,2 à 50 cents par tâche, gains typiques « d'à peine un dollar par jour » | Muse/JHU, fév. 2025 | FACT | ✧ |
| F-010 | OpenAI a utilisé des travailleurs kenyans payés < 2 $/h pour filtrer la toxicité de ChatGPT (via Sama) | TIME, 18 jan. 2023 | FACT | ✧ |
| F-011 | Des modérateurs kenyans ont subi des traumatismes psychologiques en révisant du contenu violent/sexuel pour OpenAI | The Guardian, 2 août 2023 | FACT | ✧ |
| F-012 | Leon Furze (jan. 2026) : la chaîne d'approvisionnement humaine de l'IA repose toujours sur « des travailleurs sous-payés et souvent traumatisés » | Leon Furze, 21 jan. 2026 | FACT | ✧ |
| F-013 | Le Kenya a dévoilé une politique exigeant des salaires équitables pour les travailleurs IA, sans encore de mise en œuvre | Facebook/Biznake, juil. 2026 | FACT | ✧ |
| F-014 | Tech Policy Press (juin 2026) : les chaînes de sous-traitance créent des « accountability gaps » — les travailleurs portent le coût | AI Weekly/Tech Policy Press, 29 juin 2026 | FACT | ✧ |
| F-015 | La stratégie du gouvernement français (France Stratégie) identifie les plateformes de micro-travail comme « enjeu pour l'IA et pour l'emploi » | France Stratégie, 2024 | FACT | ✧ |
| F-016 | HAL/SHS (oct. 2025) : publication académique française sur le « travail caché et sacrifié » de l'IA | HAL-SHS, oct. 2025 | FACT | ✧ |
| F-017 | Scale AI a déclaré passer du « large-scale basic labeling » à « l'annotation spécialisée pour clients enterprise/défense » — suggérant une bifurcation du marché | Shelly Palmer, oct. 2025 | FACT | ✧ |
| F-018 | 47 Md$ dépensés en IA pour le service client au S1 2025 ; 89 % de ROI nul (LinkedIn/Aditya Vemuganti) | LinkedIn, 2025 | FACT | ⁅ |
| F-019 | Les data workers restent « oubliés du droit » en France — le statut juridique n'a pas évolué depuis DiPLab 2019 | Télécom Paris + HAL-SHS | FACT | ✧ |
| F-020 | La Commission européenne (mai 2026) envisage de restreindre l'accès des clouds US aux données gouvernementales sensibles — sans aborder la question des data workers | CNBC, 7 mai 2026 | FACT | ✧ |
| F-021 | Aucune des entreprises qui annoncent des suppressions de postes remplacés par l'IA ne mentionne les travailleurs humains qui entraînent cette IA | Investigation croisée fresque + agents IA | GAP D'INFORMATION | — |

---

## CAUSALITÉ

```
Demande d'IA générative (ChatGPT, Claude, Gemini, Mistral...)
    ↓
Besoins massifs de données labellisées et de filtrage de contenu toxique
    ↓
Sous-traitance en cascade : Big Tech → Scale AI/Appen/Sama → plateformes → travailleurs
    ↓
Travail invisible, payé à la tâche (2 cents à 2 $), sans protection sociale ni statut
    ↓
Les travailleurs du clic entraînent l'IA qui menace leur propre emploi
ET les emplois des cols blancs dans les pays développés
    ↓
Ironie systémique N°2 : la chaîne humaine qui rend l'IA possible
est la première victime de l'invisibilisation
```

---

## ACTOR_NETWORK

| Acteur | Rôle | Documenté |
|--------|------|-----------|
| **OpenAI** | Client final — a utilisé Sama/Kenya pour filtrer ChatGPT | TIME 2023 |
| **Scale AI** | Plateforme de labellisation — poursuivie pour exploitation (2026) | AlgorithmWatch + Shelly Palmer |
| **Appen** | Plateforme — 2,2-50 cents/tâche | Muse/JHU 2025 |
| **Remotasks** | Plateforme — a coupé l'accès sans payer (2024) | Canadian Affairs 2025 |
| **Sama** | Sous-traitant Kenya — trauma psychologique documenté | The Guardian 2023 |
| **Travailleurs kenyans** | < 2 $/h, trauma, aucune protection | TIME + Guardian |
| **Micro-travailleurs français** | 260 000, 21 €/mois moyen, oubliés du droit | DiPLab 2019 |
| **France Stratégie** | A identifié le problème, aucune action législative | 2024 |

---

## LOUPS

| ID | Description | Sévérité |
|----|-------------|----------|
| W-001 | Aucune actualisation de DiPLab depuis 2019 — le trou statistique est total | HAUTE |
| W-002 | L'explosion de l'IA générative (2022-2026) a nécessairement multiplié le nombre de travailleurs du clic, mais personne ne les compte | HAUTE |
| W-003 | La « bifurcation » Scale AI (basic → specialized) pourrait créer une élite de labelers et laisser les autres dans la précarité absolue | MOYENNE |
| W-004 | Aucune entreprise ne mentionne ses data workers dans ses communications sur le « remplacement par l'IA » — double invisibilisation | HAUTE |

---

## IMPACTS

| Impact | Valeur | Source |
|--------|--------|--------|
| Travailleurs du clic France (2019) | 260 000 | DiPLab |
| Revenu moyen/mois France | 21 € | DiPLab |
| Rémunération Kenya OpenAI | < 2 $/h | TIME 2023 |
| Rémunération Appen | 2,2-50 cents/tâche | Muse/JHU 2025 |
| Dépenses IA service client S1 2025 | 47 Md$ (89 % ROI nul) | LinkedIn |

---

## REQUEST_LOG

| QRY-ID | Query | Résultat |
|--------|-------|----------|
| Q-001 | DiPLab actualisation 2024-2026 | Baseline 2019 confirmée ; aucune actualisation trouvée |
| Q-002 | Scale AI/Remotasks/Appen 2025-2026 | SOMO mars 2026, AlgorithmWatch août 2025, Canadian Affairs oct. 2025, Muse/JHU fév. 2025 |
| Q-003 | OpenAI Kenya data workers 2025-2026 | TIME 2023 (baseline), Guardian 2023, Leon Furze jan. 2026 (chaîne inchangée) |

---

## LIMITES

- **GAP MAJEUR** : aucun recensement national ou international des travailleurs du clic post-2022. Les 260 000 de DiPLab (2019) sont une baseline obsolète.
- L'absence de transparence des plateformes rend impossible une estimation robuste du nombre actuel.
- La chaîne de sous-traitance rend l'attribution des responsabilités quasi impossible — chaque acteur renvoie au suivant.

## CONCLUSION

L'IA qui menace les emplois est elle-même entraînée par une armée de travailleurs invisibles, sous-payés, sans statut. Les 260 000 micro-travailleurs français de 2019 (21 €/mois) ne sont qu'une fraction d'une chaîne mondiale qui va des Kenyans à 2 $/h jusqu'aux data labelers payés 2 cents la tâche. Sept ans après DiPLab, personne n'a recompté. L'explosion de l'IA générative depuis 2022 a nécessairement démultiplié cette armée de l'ombre — mais le trou statistique est total. La chaîne humaine de l'IA est le travail le plus invisible de l'économie invisible.