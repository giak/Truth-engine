# INVESTIGATION — QE n° 11677 (Lachaud) : la réponse du 10/03/2026 reconnaît un « enrichissement en cours » de la BNDP

```
IDENT        : INV-QE11677-2026-08-10
STATE          : FINAL
TYPE         : INVESTIGATION
KERNEL       : v2.8
DATE         : 2026-08-10 08:46 CEST
PATH         : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_qe11677-bndp-eenregistrement/
AUTEUR       : Buffy (session KERNEL APEX)
OBJECT       : Exécuter le GAP-001 du bilan 08-08 (question écrite ou document public chiffrant le coût du module statistique e-enregistrement) — résolution partielle + fait nouveau BNDP
LIEN         : bilan 2026-08-10_08-08_bilan-connaissance-patrimoniale (GAP-001)
```

## 0. TEXT_ANALYSIS

**Requête** : identifier une question écrite parlementaire ou un document public chiffrant le coût exact du module statistique e-enregistrement (le CPO ne dit que « quelques dizaines de millions »).

**Périmètre** : documents publics 2025-2026 (questions écrites AN/Sénat, réponses ministérielles, rapports). Objet : coût du module statistique de la plateforme e-Enregistrement / enrichissement de la BNDP / enquête DMTG.

**CRÉDO** : ne pas conclure au chiffrage exact si aucun document ne le produit. Documenter tout fait nouveau touchant la BNDP (le fil du corpus).

## 1. PISTES

| # | Piste | Statut |
|---|-------|--------|
| P1 | Sénat 760 p. 15 : note de bas de page 118 → « Question écrite n° 11677, 17e législature, réponse au JO le 10 mars 2026, p. 2216 » | ✅ IDENTIFIÉE |
| P2 | Question écrite n° 11677 sur questions.assemblee-nationale.fr/q17/17-11677QE.htm | ✅ LUE |
| P3 | Recherche d'éventuelles autres QE chiffrant le module statistique | ❌ NON IDENTIFIÉE (aucune autre QE ne chiffre le module) |

## 2. BIAS TEST

| Symbole | Score | Justification |
|---------|-------|---------------|
| 🟥 Causalité simple | 2/15 | La réponse relie « enrichissement en cours » au « rétablissement de l'accès public » sans causalité démontrée |
| 🟧 Anachronisme | 1/15 | Dates cohérentes (question 12/2025, réponse 03/2026) |
| 🟧 Sélection | 1/15 | Source primaire unique (AN) + croisement Sénat 760 (note 118) |
| 🟩 Biais de confirmation | 2/15 | La réponse introduit un élément contraire au fil (travail « en cours ») — bonne résistance |
| **Total** | **6/75** | Résistance correcte |

## 3. FACT_REGISTRY

| # | Fait | Statut | Source |
|---|------|--------|--------|
| FCT-001 | La question écrite n° 11677 (Bastien Lachaud, LFI, 6e circ. Seine-Saint-Denis) est publiée au JO le 16/12/2025, p. 10174 | CONFIRMÉ (lecture primaire page AN) | SRC-001 |
| FCT-002 | La réponse ministérielle est publiée au JO le 10/03/2026 ; la page AN indique « p. 2116 » (le Sénat 760 note 118 indique « p. 2216 » — divergence mineure non tranchée) | CONFIRMÉ (lecture primaire + croisement Sénat) | SRC-001, SRC-002 |
| FCT-003 | La question documente l'arrêt de la publication des données fiscales successions/donations depuis 2010, rompant une continuité statistique de 184 années (depuis les lois des 5 et 19/12/1790) | CONFIRMÉ (verbatim question) | SRC-001 |
| FCT-004 | La question estime les niches fiscales liées aux droits de succession et de donation à 20,8 Md€ en 2024 | CONFIRMÉ (verbatim question) | SRC-001 |
| FCT-005 | La réponse reconnaît que la dernière enquête DMTG date de 2010 et « n'a pas pu être mise à jour depuis » | CONFIRMÉ (verbatim réponse) | SRC-001 |
| FCT-006 | La réponse qualifie la BNDP d'« outil de gestion insuffisamment renseigné pour permettre des usages statistiques ou scientifiques » | CONFIRMÉ (verbatim réponse) | SRC-001 |
| FCT-007 | La réponse affirme qu'« un travail d'enrichissement [de la BNDP] à partir des actes notariés est en cours, pour reconstruire l'information manquante jusqu'au déploiement de e-Enregistrement » | CONFIRMÉ (verbatim réponse) | SRC-001 |
| FCT-008 | Calendrier e-Enregistrement selon la réponse : dons manuels opérationnels avec obligation de téléprocédure en vigueur depuis le 01/01/2026 | CONFIRMÉ (verbatim réponse) | SRC-001 |
| FCT-009 | Calendrier e-Enregistrement selon la réponse : déclarations de succession par les notaires en phase pilote « sans droits », déploiement progressif prévu au S2 2026 | CONFIRMÉ (verbatim réponse) | SRC-001 |
| FCT-010 | **La réponse ne chiffre PAS le coût du module statistique e-enregistrement** (« quelques dizaines de M€ » du CPO = seul chiffrage identifié à date dans les documents accessibles — GAP-001 partiellement ouvert) | CONSTAT D'ABSENCE | SRC-001 |
| FCT-011 | Tension documentée : Bercy affirme l'enrichissement « en cours » (réponse 10/03/2026) mais le Sénat 760 (publié 17/06/2026, constat issu de son enquête antérieure) relève le module statistique non financé (0,5 ETP) — recouvrement temporel des deux constats non précisé | CONSTAT (croisement corpus) | SRC-001, SRC-003 |


<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ❧ | - | - | - | 2026-08-10_08-46_qe11677-bndp-eenregistrement | - | -
FCT-002 | FACT | ❧ | - | - | - | 2026-08-10_08-46_qe11677-bndp-eenregistrement | - | -
FCT-003 | FACT | ❧ | - | - | - | 2026-08-10_08-46_qe11677-bndp-eenregistrement | - | -
FCT-004 | FACT | ❧ | - | - | - | 2026-08-10_08-46_qe11677-bndp-eenregistrement | - | -
FCT-005 | FACT | ❧ | - | - | - | 2026-08-10_08-46_qe11677-bndp-eenregistrement | - | -
FCT-006 | FACT | ❧ | - | - | - | 2026-08-10_08-46_qe11677-bndp-eenregistrement | - | -
FCT-007 | FACT | ❧ | - | - | - | 2026-08-10_08-46_qe11677-bndp-eenregistrement | - | -
FCT-008 | FACT | ❧ | - | - | - | 2026-08-10_08-46_qe11677-bndp-eenregistrement | - | -
FCT-009 | FACT | ❧ | - | - | - | 2026-08-10_08-46_qe11677-bndp-eenregistrement | - | -
FCT-010 | FACT | ❧ | - | - | - | 2026-08-10_08-46_qe11677-bndp-eenregistrement | - | -
FCT-011 | FACT | ❧ | - | - | - | 2026-08-10_08-46_qe11677-bndp-eenregistrement | - | -
<!-- /FACT_REGISTRY_V1 -->

## 4. PELOTE

```
Sénat 760 p. 15 (CPO : « quelques dizaines de millions »)
        └── note 118 ──► QE n° 11677 (Lachaud, 16/12/2025)
                              └── réponse 10/03/2026 (Ministère répondant : Action et comptes publics)
                                      ├── (a) DMTG : enquête 2010 jamais mise à jour
                                      ├── (b) BNDP : « insuffisamment renseignée » → enrichissement « en cours » (actes notariés)
                                      ├── (c) e-Enregistrement : dons manuels 01/01/2026 ✅ ; succession pilote S2 2026
                                      └── (d) AUCUN chiffrage du module statistique
                                             └── ⚠ tension : Sénat 760 (06/2026) : module non financé, 0,5 ETP
```

## 5. GATE_CHECK

- **GAP-001 (bilan 08-08) : PARTIELLEMENT RÉSOLU.** La QE 11677 existe et a été identifiée/lue intégralement ; mais elle ne chiffre pas le module statistique. Le seul chiffrage public reste « quelques dizaines de millions » (CPO via Sénat 760 p. 15). Conclusion honnête : **le chiffrage exact n'existe pas dans les documents publics accessibles à ce jour.**
- **Fait nouveau** : la réponse officielle reconnaît un enrichissement de la BNDP « en cours » — à croiser avec le Sénat 760 (module non financé). Divergence documentée, non résolue.

## 6. SOURCES (SRC)

| # | Source | Type | Date accès |
|---|--------|------|-----------|
| SRC-001 | Question écrite n° 11677 + réponse 10/03/2026 — questions.assemblee-nationale.fr/q17/17-11677QE.htm (lue via jina + HTML direct AN) | Primaire (AN) | 10/08/2026 |
| SRC-002 | Sénat, rapport n° 760 (17/06/2026), p. 15, note 118 — senat.fr/rap/r25-760/r25-76015.html | Primaire (Sénat) | 10/08/2026 |
| SRC-003 | Dossier 2026-08-10_08-08_bilan-connaissance-patrimoniale (module statistique non financé, 0,5 ETP) | Corpus | 10/08/2026 |

## 7. LIMITES

1. **Divergence de pagination** : la page AN dit « p. 2116 », le Sénat 760 dit « p. 2216 » pour la réponse au JO. Non tranchée (source JO papier non consultée) — sans impact sur le contenu.
2. La réponse ministérielle est une **affirmation** (« travail en cours ») non vérifiée par ailleurs (pas de livrable, pas de calendrier d'achèvement, pas de financement documenté).
3. Le chiffrage exact du module statistique reste **inconnu** — le GAP-001 est partiellement résolu, pas clos.
4. Le recouvrement temporel entre la réponse Bercy (03/2026) et le constat du Sénat 760 (enquête antérieure à sa publication du 17/06/2026) n'est pas précisé : la « tension » est documentée, sa chronologie interne reste à établir.

## 8. VERDICT

**GAP-001 (bilan 08-08) partiellement résolu.** La QE n° 11677 (Lachaud, 16/12/2025, réponse 10/03/2026) a été identifiée et lue intégralement. Elle fournit : (1) la confirmation officielle que la BNDP est « insuffisamment renseignée » pour la statistique ; (2) l'annonce d'un enrichissement « en cours » à partir des actes notariés ; (3) le calendrier e-Enregistrement (dons manuels 01/01/2026, succession S2 2026). **Mais elle ne chiffre pas le module statistique.** Le fil du corpus est renforcé d'un cran : le gouvernement lui-même qualifie la BNDP d'outil de gestion insuffisant pour la statistique — cohérent avec l'Insee (audition 07/04/2026) et le Sénat 760. La tension « enrichissement en cours » (03/2026) vs « module non financé » (06/2026) est documentée sans la résoudre.

## 9. RECOMMANDATIONS

1. Suivre la livraison effective de l'enrichissement BNDP annoncé (aucun livrable public identifié à date) — point de contrôle au PLF 2027 (octobre 2026).
2. Vérifier la pagination JO exacte (2116 vs 2216) via la version PDF de la page AN (bouton « Télécharger le format pdf »).
3. Chercher d'éventuelles autres QE 2026 sur le coût de l'enrichissement BNDP (aucune trouvée à date).

## 10. LEÇON

La donnée existe, l'enrichissement est annoncé, le chiffrage n'existe pas. Le gouvernement répond aux parlementaires en promettant un travail « en cours » que le contrôle parlementaire (Sénat 760) ne voit pas financé deux mois plus tard. C'est le même pattern que le reste du corpus : **des promesses de rattrapage sans ligne budgétaire, des données qui restent confinées.** Le prochain test décisif reste le PLF 2027.

---
*Fichier créé 2026-08-10 08:46 CEST — KERNEL v2.8 — Buffy*
