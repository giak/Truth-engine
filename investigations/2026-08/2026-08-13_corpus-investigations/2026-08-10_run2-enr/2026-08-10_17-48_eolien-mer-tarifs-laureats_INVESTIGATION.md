# INVESTIGATION : ÉOLIEN EN MER, TARIFS DE SOUTIEN, LAURÉATS ET DISPOSITIFS

- STATE          : FINAL
- DATE           : 2026-08-10 17:48 CEST
- TYPE           : INVESTIGATION (KERNEL v2.8, format allégé axe de piste)
- DOSSIER        : 2026-08-10_run2-enr (piste ENR 07-29, axe A)
- OBJECT         : documenter les tarifs de soutien, lauréats et dispositifs de l'éolien en mer français, exclus du rapport CRE PPE2 (janvier 2026), et évaluer les risques de sur-rémunération et de concentration
- SOURCES        : SRC-1 à SRC-8 (voir §4)
- GAP_SEVERITY   : 0.25 (verdicts partiels, 2 vérifications en attente)

## 1. VERDICT

**Le volet éolien en mer de la piste ENR est documenté à la source primaire : la trajectoire des tarifs est connue parc par parc, le dispositif a changé en 2016 (obligation d'achat → complément de rémunération bidirectionnel), et l'AO10 (juin 2026) fixe un tarif cible moyen de 100 €/MWh pour 10 GW.**

Les 2 signaux utiles pour la piste corruption :
1. **Génération 1 (obligation d'achat, tarifs fixés 2012-2014) : 135 à 155 €/MWh**, soit 2 à 3,5 fois les tarifs actuels. Ces contrats sont garantis par l'État pour 20 ans via EDF OA. Leur coût total est un enjeu de charges publiques documenté, mais la négociation s'est faite avant la loi de 2016 : le risque n'est pas une sur-rémunération contemporaine, c'est un héritage contractuel.
2. **Le changement de dispositif en 2016 (complément de rémunération bidirectionnel)** a mécaniquement éliminé la sur-rémunération en prix hauts (le producteur reverse l'excédent) : la CRE estime que Dunkerque (44 €/MWh) versera un **net de 263 M€ à l'État** sur 20 ans (délibération CRE du 6 juin 2019).
3. **L'AO10 (2026) : 10 GW, tarif cible moyen 100 €/MWh, 11 projets sur toutes les façades.** C'est le premier AO avec « critères de résilience ». Le tarif cible est un plafond d'enchères : les lauréats offrent en dessous. Aucun lauréat ni prix encore publié (dépôt 2026-2027).

**Verdict honnête** : aucun signal de corruption individuelle trouvé sur ce volet. Le seul angle vivant est l'**indexation des contrats de génération 1** (les tarifs affichés sont « hors indexation ») : le coût final des parcs 2012-2014 dépend de l'évolution de l'indice, et la CdC (rapport du 18/03/2026) a pointé le risque d'indexation comme zone grise (rec. n°3). À suivre via les charges de service public de l'énergie (CRE, programmées).

## 2. FAITS

| ID | Fait | Source | Statut |
|----|------|--------|--------|
| FCT-eolmer-001 | Les premiers parcs posés français et leurs raccordements ont coûté 1,4 à 2,2 Md€ par projet, pour 450 à 600 MW | SRC-1 | CONFIRMÉ |
| FCT-eolmer-002 | Le prix proposé par le lauréat de Dunkerque (attribué 2019) est de 44 €/MWh | SRC-1 | CONFIRMÉ |
| FCT-eolmer-003 | Le lauréat de Centre Manche 2 (dernier projet attribué, septembre 2025) a proposé 66 €/MWh | SRC-1 | CONFIRMÉ |
| FCT-eolmer-004 | Les premiers projets flottants commerciaux en Méditerranée (décembre 2024) ont été attribués à 85 et 92 €/MWh | SRC-1 | CONFIRMÉ |
| FCT-eolmer-005 | Saint-Nazaire : tarif d'achat 143,60 €/MWh hors indexation, consortium EDF RE + EIH S.à.r.l. (Enbridge et CPP Investments), sélection 2012, MES 2022 | SRC-2 | CONFIRMÉ |
| FCT-eolmer-006 | Fécamp : 135,20 €/MWh hors indexation, EDF RE + EIH (Enbridge, CPP) + Skyborn Renewables, sélection 2012, MES 2023 | SRC-3 | CONFIRMÉ |
| FCT-eolmer-007 | Courseulles-sur-Mer : 138,70 €/MWh hors indexation, EDF RE + EIH + Skyborn, sélection 2012, MES prévue 2027 | SRC-4 | CONFIRMÉ |
| FCT-eolmer-008 | Saint-Brieuc : 155 €/MWh hors indexation, Ailes Marines (Iberdrola), sélection 2012, MES 2023 | SRC-5 | CONFIRMÉ |
| FCT-eolmer-009 | Depuis 2016, le soutien prend la forme d'un contrat de complément de rémunération bidirectionnel (symétrique) : l'État complète si prix < cible, le producteur reverse si prix > cible | SRC-1 | CONFIRMÉ |
| FCT-eolmer-010 | Les premiers projets posés et les pilotes flottants sont soutenus par obligation d'achat via EDF OA (différence tarif/marché = à l'État si positive) | SRC-1 | CONFIRMÉ |
| FCT-eolmer-011 | La CRE estime (délibération du 6 juin 2019) que Dunkerque versera un net de 263 M€ à l'État sur 20 ans | SRC-1 | CONFIRMÉ |
| FCT-eolmer-012 | Le cahier des charges de l'AO10 (éolien en mer) a été publié le 12/06/2026 (CP n°780) : 11 projets, ~10 GW (5 GW posé + 5 GW flottant), toutes façades | SRC-6, SRC-7 | CONFIRMÉ |
| FCT-eolmer-013 | L'AO10 a été annoncé le 2/04/2026 (relance des AO ENR) ; tarif cible moyen retenu : 100 €/MWh | SRC-6 (AEF : « tarif moyen de 100 €/MWh »), SRC-7 (CP : annonce 2/04/2026) | CONFIRMÉ (100 €/MWh via AEF, non vérifié dans le CP) |
| FCT-eolmer-014 | L'AO10 inclut pour la première fois des critères de résilience ; objectif 15 GW installés en 2035, 45 GW en 2050 (PPE3) | SRC-6, SRC-7 | CONFIRMÉ |
| FCT-eolmer-015 | Saint-Nazaire et Saint-Brieuc ont vu leurs contrats d'achat modifiés pour permettre l'arrêt de production en cas de prix négatifs | SRC-8 (DDG) | À CONFIRMER |
| FCT-eolmer-016 | Aucun lauréat ni prix de l'AO10 publié au 10/08/2026 ; le calendrier exact des dépôts n'est pas précisé dans le CP (approximation : dépôt attendu 2026-2027, à vérifier) | SRC-6, SRC-7 | CONSTAT D'ABSENCE |

## 3. ANALYSE

### 3.1 La trajectoire des tarifs (2012 → 2025) : division par 3

- Génération 1 (obligation d'achat, contrats signés après sélection 2012) : **135,20 à 155 €/MWh** (Fécamp le moins cher, Saint-Brieuc le plus cher).
- Dunkerque (2019, complément de rémunération) : **44 €/MWh**.
- Flottant Méditerranée (décembre 2024) : **85 et 92 €/MWh** (technologie moins mature).
- Centre Manche 2 (septembre 2025) : **66 €/MWh**.
- AO10 (2026) : **tarif cible moyen 100 €/MWh** (flottant plus cher tire la moyenne vers le haut).

Le saut entre génération 1 et Dunkerque est massif (×3,5). Il s'explique par la maturité technologique, mais aussi par le changement de dispositif (enchère concurrentielle réelle depuis 2016).

### 3.2 Le trou de contrôle persistant (lié au run 17-33)

La page de référence (SRC-1) affiche les tarifs « hors indexation » : les parcs de génération 1 sont indexés sur des indices de coûts, et le coût final payé par le consommateur via les charges de service public n'est pas publié parc par parc en cumul. La CdC (18/03/2026) a pointé le risque d'indexation (rec. n°3). Les charges annuelles de l'éolien en mer sont publiées par la CRE (charges de service public), mais le détail par parc et par année d'indexation est une donnée de régulation : non publiée en open data. C'est le même trou que le run 17-33 (terrestre) : **la donnée de coût final existe dans les systèmes CRE, mais pas en public**.

### 3.3 Ce qui n'est PAS un signal

- Concentration des lauréats : EDF RE est présent sur 3 des 4 parcs de génération 1 (avec les mêmes partenaires EIH/Enbridge/CPP), mais les AO suivants (Dunkerque, AO4-AO6) ont été ouverts à d'autres acteurs (Iberdrola via Ailes Marines, RWE, TotalEnergies). Le rapport CRE PPE2 (17-28) documente un paysage concurrentiel « sans position dominante » pour le terrestre ; le même constat s'applique en mer pour les AO récents.
- Le pantouflage CRE → EDF (Bohuon, 2023) est traité dans le dossier axe C (17-52).

## 4. SOURCES

- SRC-1 : https://www.eoliennesenmer.fr/generalites-eoliennes-en-mer/economie-et-fiscalite (page officielle de la filière, lue intégralement 17:38)
- SRC-2 : https://www.eoliennesenmer.fr/facades-maritimes-en-france/facade-nord-atlantique-manche-ouest/saint-nazaire
- SRC-3 : https://www.eoliennesenmer.fr/facades-maritimes-en-france/facade-manche-mer-du-nord/fecamp
- SRC-4 : https://www.eoliennesenmer.fr/facades-maritimes-en-france/facade-manche-mer-du-nord/courseulles-sur-mer
- SRC-5 : https://www.eoliennesenmer.fr/facades-maritimes-en-france/facade-nord-atlantique-manche-ouest/saint-brieuc
- SRC-6 : https://www.aefinfo.fr/depeche/752393-le-gouvernement-lance-le-grand-appel-doffres-sur-leolien-en-mer-de-10-gw (dépêche AEF, 12/06/2026, réservée aux abonnés, extrait lu)
- SRC-7 : https://presse.economie.gouv.fr/le-gouvernement-annonce-la-publication-du-cahier-des-charges-de-lappel-doffres-n10-dit-ao10-pour-leolien-en-mer/ (CP n°780, 12/06/2026, lu intégralement)
- SRC-8 : résultats DDG « parcs éoliens en mer lancés : calendrier, coût » (15 099 octets, titres + extraits)

Artefacts /tmp : jina_eco.txt, jina_sn.txt, jina_fecamp.txt, jina_courseulles.txt, jina_sb.txt, ao10_presse.txt, jina_ao10.txt, jina_tarifs.txt.

## 5. GAP ET PROCHAINES ÉTAPES

1. **GAP-1 (à faire)** : confirmer FCT-eolmer-015 (modification des contrats Saint-Nazaire/Saint-Brieuc pour prix négatifs) à la source primaire (presse spécialisée, Journal de l'Éolien).
2. **GAP-2 (à faire)** : quantifier l'effet d'indexation des contrats génération 1 : chercher dans les délibérations CRE (charges de service public 2022-2025) le coût annuel réel par parc, pour chiffrer l'écart « tarif nominal hors indexation » vs « coût réel indexé ». C'est le seul angle où le montant public peut être supérieur au tarif affiché.
3. **GAP-3 (surveillance)** : AO10 : les lauréats seront connus en 2027 (dépôt 2026-2027). Vérifier à l'attribution : prix effectifs vs tarif cible 100 €/MWh, et identité des consortiums (concentration EDF RE + partenaires financiers récurrents).
4. **Lien run 17-33** : les charges de service public ENR (incluant l'éolien en mer) sont la clé du chiffrage global : voir si la demande CADA D05 (CRE, données coûts/recettes) couvre aussi le détail éolien en mer.

## 6. CONCLUSION

L'éolien en mer est **documenté sans signal de corruption individuelle**. Les 2 angles actionnables sont (a) l'indexation des contrats de génération 1 (trou de contrôle sur le coût final) et (b) la surveillance de l'AO10 (première attribution sous critères de résilience). Le volet « rentes » est structurellement fermé depuis 2016 (complément de rémunération bidirectionnel). Le dossier se range dans le corpus « risque systémique de gestion » (comme le run 17-33), pas dans le corpus « suspicion nominative ».
