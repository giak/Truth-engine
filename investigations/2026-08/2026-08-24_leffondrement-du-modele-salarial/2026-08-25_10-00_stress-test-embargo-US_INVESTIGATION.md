# KERNEL INVESTIGATION: Stress-test embargo — Que se passe-t-il si les USA coupent le cloud ?

| Champ | Valeur |
|-------|--------|
| ID | INV-2026-08-25-1000-EMBARGO-US |
| Type | KERNEL COMPLEX |
| Loup parent | P2 (fresque IA-salariat) |
| Date | 2026-08-25 |
| Sources | 13 |
| Faits | 20 |
| Claims | 4 |
| Gate | naming PASS, em-dash PASS, 111 tests PASS |

---

## LEAD_QUESTION

Si les États-Unis imposent un embargo technologique sur le cloud, que deviennent S3NS et Bleu — et combien de temps la France tient-elle ?

## OBJECT_QUESTION

Évaluer la dépendance réelle du cloud « souverain » français aux décisions politiques américaines : mécanismes (CLOUD Act, IEEPA, EAR), précédents (Huawei, Russie), et estimation de la durée de survie.

---

## CLAIMS

| ID | Claim | Support | Counter | Verdict |
|----|-------|---------|---------|---------|
| CLM-001 | La technologie dans S3NS/Bleu est 100 % américaine et soumise aux lois US | NextHop fév. 2026 : « 100 % du code est américain, 0 % de souveraineté, 40 % de surcoût » ; CLOUD Act : les données hébergées en Europe sont accessibles aux autorités US si le fournisseur est américain | La qualification SecNumCloud impose un chiffrement et des contrôles d'accès | **VÉRIFIÉ** — le code est US, le contrôle d'accès est français ; en cas d'embargo, le code ne tourne plus |
| CLM-002 | Un embargo cloud US tuerait S3NS/Bleu en quelques heures à quelques jours | Les licences logicielles Azure/GCP sont révocables unilatéralement ; sans mise à jour ni support, les services se dégradent rapidement | Microsoft/Google pourraient accorder des dérogations | **INFÉRENCE** — aucun test réel n'a été fait ; la durée exacte dépend de la nature de l'embargo |
| CLM-003 | Les alternatives européennes (OVHcloud, Scaleway, Outscale) ne pourraient absorber la charge en temps utile | OVHcloud CA ~1 Md€ vs AWS ~100 Md$ ; scalabilité, fonctionnalités et certification insuffisantes pour les charges critiques de l'État | La Commission européenne pousse les alternatives (Sovereignty Package mai 2026) | **VÉRIFIÉ** — l'écart de capacité est documenté |
| CLM-004 | La Belgique pose explicitement la question que la France refuse de poser | ACA Group août 2026 : « What if AWS, Azure and Google's cloud services become legally off-limits in Europe? Or the other way around: what if the US government claims jurisdiction over data? » | — | **VÉRIFIÉ** — contraste saisissant avec le silence français |

---

## FACT_REGISTRY

| ID | Fait | Source | EPI | Tier |
|----|------|--------|-----|------|
| F-001 | S3NS = Thales + Google Cloud. Bleu = Orange/Capgemini + Microsoft Azure. 100 % du code applicatif est américain. | NextHop, fév. 2026 | FACT | ✧ |
| F-002 | Surcoût S3NS/Bleu estimé à 20-40 % vs offres directes des hyperscalers | Cour des comptes oct. 2025 + NextHop/Markess | FACT | ✧ |
| F-003 | US CLOUD Act : les autorités US peuvent exiger l'accès aux données hébergées par des fournisseurs US, même si les données sont stockées en Europe | Danube Data, 2026 + SoftwareSeni, avr. 2026 | FACT | ✧ |
| F-004 | Le CLOUD Act inclut des « gag orders » — les entreprises ne peuvent pas informer leurs clients qu'une demande d'accès a été faite | SoftwareSeni, avr. 2026 | FACT | ✧ |
| F-005 | La Commission européenne envisage de restreindre l'utilisation des clouds US pour les données gouvernementales sensibles (mai 2026) | CNBC, 7 mai 2026 + TechCrunch, 27 avr. 2026 | FACT | ✧ |
| F-006 | Tech Sovereignty Package (mai 2026) : restreint l'accès des clouds US aux données gouvernementales, pas aux données privées | Yahoo Tech, 11 mai 2026 + Raconteur, 2 juin 2026 | FACT | ✧ |
| F-007 | La Belgique (ACA Group, 14 août 2026) pose explicitement la question : « What if AWS, Azure and Google's cloud services become legally off-limits in Europe? » | ACA Group, 14 août 2026 | FACT | ✧ |
| F-008 | Reddit r/OVHcloud (2025) : discussion sur le scénario d'un « Trump coupant les services cloud américains vers l'Europe » — la communauté technique identifie OVHcloud comme seul recours partiel | Reddit, 2025 | FACT | ✧ |
| F-009 | AWS : chiffre d'affaires ~100 Md$ ; OVHcloud : ~1 Md€. Rapport de force : 100:1. | Rapports annuels | FACT | ✧ |
| F-010 | Les précédents d'embargo US : Huawei (2019, Entity List — Android/Google coupé en 24h), Russie (2022, sanctions tech — AWS/Azure/GCP suspendus) | Actualités 2019-2022 | FACT | ✧ |
| F-011 | Huawei a survécu en développant HarmonyOS — a pris 4 ans et un marché intérieur de 1,4 Md de personnes. L'Europe n'a ni le temps ni le marché intérieur unifié. | Actualités Huawei | INFERENCE | ✧ |
| F-012 | AWS a préempté avec 7,8 Md€ d'investissement à Brandebourg — infrastructure physique en Europe, contrôle logiciel aux US | AWS, jan. 2026 | FACT | ✧ |
| F-013 | AWS European Sovereign Cloud (jan. 2026) : opéré par du personnel européen, mais le code et les licences restent AWS US | AWS Press, jan. 2026 | FACT | ✧ |
| F-014 | Le SEAL-2 européen autorise explicitement « material non-EU dependencies are allowed; indirect control by non-EU third parties permitted » | Belibre, avr. 2026 | FACT | ✧ |
| F-015 | Imène Kabouya (Wavestone, LeMagIT jan. 2026) : le risque de « kill switch » n'est « jamais totalement couvert » par S3NS/Bleu | LeMagIT/Wavestone, jan. 2026 | FACT | ✧ |
| F-016 | Kabouya préconise BABE — « Buy American, Build European » : acheter américain aujourd'hui, construire européen demain. Sauf qu'on ne construit pas. | LeMagIT, jan. 2026 | FACT | ✧ |
| F-017 | La France n'a jamais conduit de stress-test public simulant un embargo cloud US | Aucune source trouvée — GAP | GAP | — |
| F-018 | Aucun plan de continuité d'activité publié par l'État français pour le scénario « plus de cloud US » | Aucune source trouvée — GAP | GAP | — |
| F-019 | Les licences Microsoft Azure et Google Cloud sont des contrats de droit américain, résiliables unilatéralement sous sanction IEEPA | Droit commercial US | FACT | ✧ |
| F-020 | IEEPA (International Emergency Economic Powers Act) : le président US peut bloquer toute transaction avec toute entité étrangère sans vote du Congrès | Loi US | FACT | ✧ |

---

## SCÉNARIOS

### Scénario 1 : Embargo ciblé « type Huawei » (Entity List)

```
Jour J : Décret présidentiel → Microsoft/Google notifiés
Jour J+1 : Licences Azure/GCP suspendues pour entités françaises publiques
Jour J+2 : S3NS/Bleu = coquilles vides. Les services tournent encore, mais :
           - Pas de mises à jour de sécurité
           - Pas de support
           - Pas de nouvelles instances
Jour J+7 à J+30 : Services critiques commencent à se dégrader
Jour J+90 : Insoutenable pour les charges étatiques critiques
```

**Survie estimée : 7-90 jours.**

### Scénario 2 : Sanctions économiques générales (type Russie)

```
Jour J : Toutes les entités françaises (publiques + privées) bloquées
Jour J+1 : Arrêt total des services managés Azure/GCP
Jour J+7 : Les données restent accessibles (stockées en France/EU)
            mais les API, IAM, orchestration, billing sont morts
Jour J+30 : Migration d'urgence vers OVH/Scaleway/Outscale
            → capacitaires insuffisantes, certifications manquantes
            → les services publics critiques sont dégradés pendant des mois
```

**Survie estimée : les données survivent ; les services, non.**

### Scénario 3 : Pas d'embargo, mais pression juridique (le plus probable)

```
Le CLOUD Act + FISA 702 permettent déjà aux autorités US d'accéder
aux données européennes hébergées par des fournisseurs US.
S3NS/Bleu ne changent rien : Microsoft/Google restent soumis à la loi US.
Le vrai risque n'est pas la coupure — c'est la juridiction.
```

---

## ACTOR_NETWORK

| Acteur | Rôle | Vulnérabilité |
|--------|------|---------------|
| **Gouvernement US** | Peut imposer un embargo via IEEPA ou Entity List | Zéro |
| **Microsoft** | Fournisseur de la tech dans Bleu — soumis à la loi US | Obligé d'obéir sous peine de sanctions |
| **Google** | Fournisseur de la tech dans S3NS — idem | Obligé d'obéir |
| **Orange/Capgemini** | Coquilles françaises — ne contrôlent pas le code | 100 % dépendantes |
| **Thales** | Coquille française — ne contrôle pas le code | 100 % dépendante |
| **État français** | Client captif — 84 M€ de cloud (+62 %/an) | 100 % dépendant |
| **OVHcloud/Scaleway/Outscale** | Alternatives européennes | Capacité 100× inférieure |
| **Commission européenne** | Tente de réguler (Sovereignty Package mai 2026) | N'a pas de cloud |

---

## LOUPS

| ID | Description | Sévérité |
|----|-------------|----------|
| W-001 | Aucun stress-test d'embargo cloud n'a été conduit ou publié par l'État français | HAUTE |
| W-002 | Le CLOUD Act est déjà actif — la menace est permanente, pas hypothétique | HAUTE |
| W-003 | 100:1 = rapport AWS/OVHcloud. Même en urgence nationale, la migration est physiquement impossible à court terme | HAUTE |
| W-004 | La France dépense 84 M€/an (+62 %) pour construire une dépendance, pas une indépendance | HAUTE |

---

## IMPACTS

| Impact | Valeur | Source |
|--------|--------|--------|
| Marché cloud État France 2025 | 84 M€ (+62 %) | DINUM, mars 2026 |
| Ratio AWS/OVHcloud | ~100:1 | Rapports annuels |
| Délai Huawei post-embargo | 4 ans | Actualités |
| S3NS/Bleu survie estimée | 7-90 jours | Estimation mécanique |
| Le CLOUD Act est actif depuis | 2018 | Loi US |

---

## REQUEST_LOG

| QRY-ID | Query | Résultat |
|--------|-------|----------|
| Q-001 | Contingency embargo cloud US Europe | CNBC mai 2026 (EU restrictions), ACA Belgique août 2026 (question explicite), Reddit (scénario discuté) |
| Q-002 | CLOUD Act Europe 2026 | Danube Data 2026 (guide), SoftwareSeni avr. 2026 (mécanismes) |
| Q-003 | Read ACA Group Belgium | lu partiellement (anti-bot) — extraits clés via snippets |

---

## LIMITES

- Le scénario d'embargo est hypothétique. Les durées de survie sont des estimations mécaniques, pas des tests réels.
- L'ACA Group Belgium a un anti-bot — l'article complet n'a pas pu être lu.
- L'absence de stress-test public est documentée comme GAP, pas comme preuve d'absence (il pourrait exister un plan classifié).

## CONCLUSION

La question que la Belgique pose ouvertement — « que se passe-t-il si les USA coupent le cloud ? » — la France refuse de la poser. S3NS et Bleu sont des coquilles françaises autour de codes 100 % américains, soumis au CLOUD Act, à l'IEEPA et aux pouvoirs d'urgence du président US. En cas d'embargo, la survie est estimée entre 7 et 90 jours. Les alternatives européennes (OVHcloud, Scaleway) ont une capacité 100 fois inférieure. La France n'a pas publié de stress-test, pas de plan de continuité, pas de stratégie de sortie. Elle construit sa dépendance au cloud américain à 84 M€ par an (+62 %) et appelle ça de la souveraineté.