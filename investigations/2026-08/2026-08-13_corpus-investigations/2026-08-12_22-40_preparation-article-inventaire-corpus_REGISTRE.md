# PREPARATION ARTICLE PHASE 3 — INVENTAIRE FORENSIQUE DU CORPUS

- STATE   : CORPS CORRIGÉ (12 corrections P0 appliquées au corpus le 12/08 23:15-23:30 CEST, cf. registre 23-10)
- DATE    : 2026-08-12 22:40 CEST (wall-clock réel)
- TYPE    : REGISTRE (inventaire pré-article)
- DECISIONS : article unique long 8-12k mots ; thèse « Légalité sans intégrité » ; vérification de tous les claims retenus à la source primaire
- PERIMETRE : investigations/2026-08/2026-08-13_corpus-investigations/ (corpus 9-12 août 2026)

---

## 1. CHIFFRAGE REEL DU CORPUS (recomptage, 12/08 22:40 CEST)

| Metrique | Valeur | Source du recomptage |
|---|---|---|
| Fichiers .md dans investigations/2026-08/2026-08-13_corpus-investigations/ (hors data/, cada_lettres/) | **285** | `find . -name '*.md'` |
| Dont dossiers 08-06 (ingérences russes, hors périmètre article) | 42 | idem |
| Dont corpus article (9-12 août) | ~243 | idem |
| FCT annoncés par la synthèse finale (13-30) | ~1 820 | synthèse 13-30 |
| FCT annoncés par le point 21:15 | 1 663 | point 21:15 |
| FCT annoncés par le point 19:45 | 1 661 | point 19:45 |
| FCT annoncés par la synthèse 12:15 | ~1 466 | synthèse 12:15 |
| Découvertes majeures annoncées | 15 / 18 / 23 selon les synthèses | 12:15 / 13:30 / 21:15 |

> **CONSTAT D'INVENTAIRE 1** : les synthèses se contredisent entre elles sur les métadonnées (docs 216 vs 242 vs ~304 ; FCT 1 466 vs 1 538 vs 1 661 vs 1 663 vs 1 820 ; découvertes 15 vs 18 vs 23). Aucune n'est fiable en l'état pour une citation en article. **Tout chiffre repris en article devra être recompté mécaniquement (grep des préfixes FCT) avant publication.**

---

## 2. DOSSIERS PRINCIPAUX ET LEUR ETAT

| Dossier | Fichiers | Objet | Verdict de synthèse | Statut pour article |
|---|---|---|---|---|
| `2026-08-10_run2-enr/` | 93 | Capture rente ENR (Valeco/EnBW, CRE, pantouflage, Puech Cornet) | Capture légale ENR, 0 corruption pénale | **Noyau dur — dossier le plus approfondi du corpus** |
| `2026-08-11_corpus-anticorruption/` | 35 | ICEBERG MAX : 16 pistes sectorielles | 3 invariants sur 16 secteurs | **Noyau dur — tableau sectoriel** |
| `2026-08-12_alstom-areva-cessions-macron/` | 5 | Cessions stratégiques 2014-2024 | Cycle « céder puis racheter », 6 hypothèses falsifiées | **Socle de crédibilité — falsifications documentées** |
| `2026-08-12_buzyn-vaccination-enfants/` | 5 | Vaccination obligatoire 2017 | 4 lièvres CONFIRMÉS, 4/8 GAPs résolus | **Étude de cas — retiré de V2, réintégrable si sourcé** |
| `2026-08-12_run4-autoroutes-aeroports-flamanville/` | 1 | Autoroutes, ADP, EPR | 5 mécanismes confirmés, Vinci transversal | **Absent des 2 articles — à intégrer** |
| `2026-08-12_run5-speculation-fonciere-dvf/` | 1 | Foncier, loi 2025-1249, Cabrol | 20e secteur documenté | **Absent des 2 articles — à intégrer** |
| `2026-08-09_*` (29 dossiers) | ~35 | Dutreil, CumCum, OPA EDF, revolving doors Bercy, commande publique | Infrastructure documentaire, 7 clusters | **Source des études de cas Dutreil/CJIP/pantouflage** |
| `2026-08-10_*` (42 dossiers hors run2) | ~133 | Pilotes SESN, BNDP, DMTG, avenants | Faisceaux complémentaires | **À écarter sauf besoin (portée limitée)** |
| `2026-08-10_preparation-anticorruption/` | 20 | Doctrine, protocole, règles | Méthodologie | **Référence méthode (corruption_brainstorm.md)** |
| Synthèses racine (08-12) | 7 | Points consolidés, cloture GAPs, contradictoire | État du corpus | **Point d'entrée de relecture** |

---

## 3. MATRICE DES CLAIMS CANDIDATS POUR L'ARTICLE

Statut : la colonne « Statut preuve » reflète ce que le corpus déclare. La Phase 3 vérifiera chaque claim retenu à la source primaire.

### Bloc A : Le double standard (candidat axe central)

| Claim | Chiffres | Sources primaires déclarées | Statut preuve |
|---|---|---|---|
| Fraude CPF réprimée : 48 réseaux démantelés en 2 ans | 48 réseaux, 534 M€ saisis, 3 lois 2022-2026 | ONAF, Sénat, RUN_MANIFEST run2 | CONFIRMÉ corpus ; à revérifier |
| Rente ENR jamais contrôlée : 18 ans, rec. n°1 CdC non appliquée | 18 ans, 0 CJIP | CdC 18/03/2026, fascicule réponses | CONFIRMÉ corpus ; à revérifier |
| HATVP : 1 seul blocage sur 598 compatibilités avec réserves | 598, 1 → **corrigé : au moins 2 incompatibilités** (2025-103 Carenco + 2024-294 agent AAI) | RA HATVP 2023, avis 2025-103, 2024-294 | **ERRATA 20:45 : « 1 seul » INFIRMÉ, ratio 0,33 %** |
| AFA : 27 contrôles en 2024 pour ~400 Md€ de commande publique | 27, 101 depuis 2018, 400 Md€ | RA AFA 2024, Sénat n° 830 | CONFIRMÉ corpus ; à revérifier |
| CJIP : 20 signées, 12,145 Md€, 0 poursuite personne physique | 20, 12,145 Md€ | Plaquette PNF, dossiers 08-09 | CONFIRMÉ corpus ; à revérifier |
| PNF : McKinsey 4 ans, Uber 3 ans, JO 3 ans, SIAAP 2 ans = 0 mise en examen publique | 0 mise en examen | P1-P8 v3, GAPs 13:15 | CONFIRMÉ corpus ; à revérifier |

### Bloc B : Rente légale (ENR, autoroutes, nucléaire, foncier)

| Claim | Chiffres | Sources primaires | Statut preuve |
|---|---|---|---|
| Valeco Ren : capital 100 % allemand depuis 11/2022 | EnBW 51 %, KlimaVest/Commerzbank 49 % | RCS (Pappers), communiqués De Pardieu/Le Monde du Droit 11/2022 | CONFIRMÉ source primaire |
| Distributions Valeco 2023-2025 | ~31,3 M€ (pic 26,8 M€ 2023) | **Reconstitution par delta fonds propres (bilans déposés)** | **RECONSTITUTION — doit être étiquetée** |
| Tarif OA éolien terrestre | 82 €/MWh 10 ans puis tarif réduit 5 ans | Arrêtés 2008/2014 | **CONFIRMÉ — V1 a écrit « sans plafond », FAUX (plafond borné)** |
| Autoroutes : privatisées 14,8 Md€ en 2006, dividendes 34-40 Md€ | 14,8 / 34-40 Md€ | FIPECO, Sénat | CONFIRMÉ corpus run4 ; à revérifier |
| Rachat autoroutes estimé 45-50 Md€ (IGF/CGEDD 2023) | 45-50 Md€ | Marianne/IGF | À revérifier (presse secondaire) |
| Flamanville : 3,3 Md€ → 23,7 Md€ (CdC 01/2025), 12 ans de retard | 23,7 Md€ | CdC 01/2025 | CONFIRMÉ corpus ; à revérifier |
| Pacte Dutreil : >5,5 Md€ en 2024, 110 donataires = 65 % | 5,5 Md€ / 110 / 65 % | CdC 18/11/2025, IPP n° 62 | CONFIRMÉ corpus (V2) ; à revérifier |

### Bloc C : Déplacement des frontières pénales

| Claim | Chiffres | Sources primaires | Statut preuve |
|---|---|---|---|
| Loi 2025-1249 : modification art. 432-12 (prise illégale d'intérêts) | 4 changements (altérant, connaissance de cause, intérêt public exclu, motif impérieux) | Légifrance, art. 432-12 | CONFIRMÉ — V2 vérifié verbatim |
| Cass. crim. 6/05/2026 n° 24-81.451 : « sens moins sévère » | 1 arrêt publié au bulletin | Légifrance | CONFIRMÉ (fact-check livre) |
| AMF a « fortement soutenu » la loi | 1 déclaration | AMF | CONFIRMÉ corpus run5 ; à revérifier |
| Conseil constitutionnel non saisi | 1 constat d'absence | — | À documenter |

### Bloc D : Entrelacement expertise-intérêt

| Claim | Chiffres | Sources primaires | Statut preuve |
|---|---|---|---|
| Andra : EDF+CEA au CA de l'agence (contre-exemple corrigé) | 3 producteurs au CA jusqu'en 2010 | CdC 04/06/2025 | CONFIRMÉ — V2 l'utilise comme contre-exemple |
| Vinci : actionnaire ADP (8 %) + concessionnaire autoroutier + obligations échangeables 500 M€ | 8 %, 500 M€ | Boursorama, CP Vinci 25/02/2026 | CONFIRMÉ corpus run4 ; à revérifier |
| Bouygues : 29 % Alstom à la cession + génie civil Flamanville | 29,3 % | Les Echos 2014, rapport Folz | CONFIRMÉ corpus ; à revérifier |
| Corps des Mines : navette EDF/Areva/ministeres | pattern | Dossier 08-09 revolving doors | QUALITATIF — pas de registre nominatif |

### Bloc E : Garde-fous sans moyens / asymétrie d'observabilité

| Claim | Chiffres | Sources primaires | Statut preuve |
|---|---|---|---|
| HATVP : 438 avis 2023, 111 publiés / 327 non | 111/327 | RA HATVP 2023 | CONFIRMÉ — V2 |
| Suivi des réserves HATVP non exhaustif (aveu) | 1 phrase RA 2023 | RA HATVP 2023 | CONFIRMÉ — V2 |
| 0 registre des administrateurs de CA publics (scraping 12 837 DPI) | 12 837 DPI, 0 admin CA | data.gouv.fr, jaune budgétaire PLF 2026 | CONFIRMÉ corpus (GAP-p14-1) ; à revérifier |
| Auditions régulateurs non transcrites vs commission finances | 145 CR finances vs 0 CR éco | assemblee-nationale.fr, transcription whisper | CONFIRMÉ corpus run2 ; à revérifier |
| DVF anonymisée (RGPD) : croisement élus/transactions impossible | 30 M+ transactions | Cerema | CONFIRMÉ corpus run5 ; à revérifier |
| 80 % marchés publics non contrôlés, gré à gré 170 Md€ | 170 Md€ | Sénat n° 830 | CONFIRMÉ corpus ; à revérifier |

### Bloc F : Étude de cas Buzyn (retiré de V2, réintégrable)

| Claim | Chiffres | Sources primaires | Statut preuve |
|---|---|---|---|
| CE n° 397151 (08/02/2017) : 3 outils juridiques non utilisés | 3 outils, injonction 6 mois | Légifrance/CETATEXT000034056265 | CONFIRMÉ corpus (GAP-001 résolu) |
| Rapport Fischer : objectif = levée de l'obligation, clause supprimée | 1 rapport | vie-publique.fr | CONFIRMÉ corpus (GAP-002) |
| Touraine 26/04/2016 : « On le trouve si on le demande » | 1 citation | déclaration ministérielle, contredite par CE | CONFIRMÉ corpus (GAP-007) |
| Continuité HAS→ministère Buzyn (CTV 22/03/2017 → ministre 17/05/2017 → annonce 05/07/2017) | 49 jours | décisions HAS, JO | CONFIRMÉ corpus (C4) |
| DPI Buzyn HAS : 404, archivée | 1 constat d'absence | hatvp.fr | CONSTAT D'ABSENCE |

### Bloc G : Alstom-Areva (5 découvertes + 6 falsifications)

| Claim | Chiffres | Sources primaires | Statut preuve |
|---|---|---|---|
| Cycle « céder puis racheter » sur 6 cas | 25-35 Md€ coût net estimé | Dossier alstom 17-00 (bloc E) | ANALYSE — chiffre consolidé, pas une pièce |
| Rothschild 12 M€ honoraires sur Alstom, Macron ex-Rothschild valide | 12 M€ | Presse, dossier 17-00 | CONFIRMÉ corpus ; à revérifier |
| DOJ : Pierucci arrêté 04/2013, Alstom 772 M$ (12/2014) | 772 M$ | Dossier 17-00, presse | CONFIRMÉ corpus ; à revérifier |
| 6 hypothèses FALSIFIÉES (dont « corruption directe Macron ») | 6 | Dossier 18-45 | **ATOUT MÉTHODOLOGIQUE — à mettre en avant** |
| En Marche 2016-2017 : 16 M€, 48 % réseau haute finance | 16 M€ | Dossier 18-45 | CONFIRMÉ corpus ; à revérifier |

---

## 4. INVENTAIRE DES ERRATA ET CORRECTIONS INTERNES (obligatoire avant écriture)

Ces corrections doivent être respectées dans l'article ; certaines infirment la V1 :

| # | Correction | Fichier source | Impact article |
|---|---|---|---|
| 1 | Dividendes Valeco : ~31,3 M€ (pas 7,52 M€) — reconstitution delta FP | `21-36_gap1-affectations-valeco-ren_RESOLUTION.md` | V1 = 31,3 M€ OK, mais doit rester étiqueté reconstitution |
| 2 | « 1 seul blocage HATVP » → **au moins 2 incompatibilités** (2025-103 Carenco + 2024-294 agent AAI) | `20-45_cloture-7-gaps_RESOLUTION.md` | **V1 et V2 datées : le chiffre « 1 » est faux depuis 20:45** |
| 3 | Tarif OA éolien : plafond borné 10 ans 82 € puis 5 ans réduit — PAS « sans plafond » | `22-30_fascicule-reponses-administrations_RESOLUTION.md` | **V1 contient une erreur factuelle (« sans plafond »)** |
| 4 | Errata 2024-294 vs 2024-225 (avis AAI) | `14-50_gap1-26-incompatibilites-hatvp_INVESTIGATION.md` | Référencer le bon numéro |
| 5 | Rec. n°1 CdC = collecte des coûts (plan d'audit + tableau de bord), pas rec. n°3 | `18-53` + `19-07_angle3` | V1 correcte, à maintenir |
| 6 | Fillon : peine NON définitive (pourvoi juil. 2025) | Pass 3 corruption-systemique | Ne pas écrire « condamné définitivement » |
| 7 | « 80-100 Md€ coût corruption » : RECUSÉ par la CdC (estimation Solidaires 2013) ; fraude documentée 17,4-25,6 Md€ ; dépenses fiscales 91,83 Md€ | Pass 3 | **Ne pas reprendre « 80-100 Md€ » comme fait** |
| 8 | Sortie contrat OA Margnes/Singladou : 01/04/2022 (corrige estimation sept 2022/juil 2024) | `11-26_gaps-a3-2-3-5` | Détail run2, hors article principal |
| 9 | MIROVA : toujours actionnaire au 03/06/2019 (sortie postérieure, 2021-2022) | `20-26_gap1-valeco-ren-753m` | V1 : « sortie 2023 » non, la cession à KlimaVest = 11/2022 |
| 10 | Cabrol : 2 500 € amende + 800 € dommages (pas « onze ans » pour la condamnation seule) | run5, V2 | V2 correcte |

---

## 5. LIMITES OSINT DOCUMENTEES (à déclarer dans l'article)

| Limite | Détail | Fichier |
|---|---|---|
| Secret de l'instruction | PNF McKinsey, Uber, JO 2024, SIAAP, Alstom : 0 mise en examen publique, contenu inconnu | GAPs 13:15 |
| Secret des affaires | CEPS (prix médicaments), commissions armes, contrats de concession | P3, P6 |
| Secret fiscal/notarial | Identité des 110 donataires Dutreil | dutreil-110 |
| Montant cession Mirova→KlimaVest | Transaction privée entre fonds, non publiée | GAP-mv-1 |
| DPI Buzyn HAS | Archivée 6 mois après départ | GAP-004 buzyn |
| Débats internes vaccination | Communicabilité 25 ans (art. L213-2 CRPA) | GAP-006 buzyn |
| Registre CA publics | 0 registre existe — constat d'absence | GAP-p14-1 |
| Coordination directe | Aucune preuve de coordination centrale ; documentée comme structurelle | Transversal |

---

## 6. ETAT DU CONTRADICTOIRE EXTERNE (hérité du 23-00)

- Registre prêt : `2026-08-12_23-00_contradictoire-v2_REGISTRE.md`
- 6 lettres (CRE, HATVP, ministère énergie, Valeco/EnBW, Commerz Real/KlimaVest, Mirova) + 3 notices (CdC, Sénat, Andra)
- Délai 21 jours, échéance 02/09/2026
- **À compléter : expéditeur [Prénom NOM, médium]**

---

## 7. ETAT APRES CORRECTIONS P0 (23:30 CEST)

Les 12 corrections P0 du registre 23-10 ont été appliquées à :
- `2026-08-12_12-15_synthese-massive-2-jours_SYNTHESE.md` (7 remplacements : ONAF global, plafond borné, 2 incompatibilités)
- `2026-08-12_13-30_synthese-massive-finale_SYNTHESE.md` (12 remplacements)
- `2026-08-12_21-15_point-consolide-final-definitif_POINT.md` (3 remplacements)
- `2026-08-12_run4-autoroutes-..._INVESTIGATION.md` (2 remplacements : attribution Bercy via Sénat)
- `2026-08-11_corpus-anticorruption/2026-08-12_11-00_p11-fraude-cpf-v2_INVESTIGATION.md` (1 remplacement §4)
- `2026-08-11_corpus-anticorruption/2026-08-12_13-00_iceberg-max-v4_REGISTRE.md` (2 remplacements)
- `2026-08-09_corruption-systemique-france/2026-08-09_09-29_..._INVESTIGATION.md` (7 remplacements : 968 Interstats n° 51, 170 Md€ contrats ≥ 90 k€ HT)
- `2026-08-12_15-00_run3-enrichissement_REGISTRE.md` (3 remplacements)

Vérification grep de contrôle : les marqueurs erronés (« 48 reseaux ONAF », « 534 M EUR saisis », « sans plafond de rendement », « 1 seul blocage », « 934 infractions ») ont disparu des fichiers canoniques.

## 8. PROCHAINES ETAPES (Phase 5)

1. Sélection des dossiers de l'article selon le critère de preuve (claim → source primaire → contexte → contre-preuve → qualification → conclusion)
2. Construction de l'échafaudage : 8-12k mots, sections reliées aux claims ci-dessus
3. Vérification claim par claim à la source primaire (mnemolite-mem-first) : en priorité les claims non encore vérifiés des blocs A/B/D/E/F/G
4. Réintégration décidée : run4 (autoroutes/ADP/Flamanville), run5 (foncier), Buzyn, Alstom (falsifications)
5. Audit multi-rôles puis contradictoire externe puis publication

---

*Inventaire forensique — 285 fichiers, 8 dossiers principaux, 7 blocs de claims candidats, 10 ERRATA documentés, 8 limites OSINT. 12 août 2026, 22:40 CEST. Phase 0 de la préparation.*
