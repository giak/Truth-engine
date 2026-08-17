# Quintessence : Préparation aux investigations sur la corruption en France (cadrage structurel)

Source : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-11_corpus-anticorruption/2026-08-11_23-00_preparation-investigations-corruption_INVESTIGATION.md` (626 lignes, 33 FCT-001 à 033)
Date extraction : 2026-08-13 04:00 CEST
Pilote : Buffy (FreeBuff) : Sublimator v36 Phase 1 (corpus complet, lot corpus-anticorruption)

---

## 1. Métadonnées & trace source

- **Autorité** : KERNEL v2.8, INPUT_KIND TOPIC, RUN 20260811-2300, COMPLEXITY 12→APEX, SCOPE PENDING
- **Date source** : 2026-08-11 23:00 CEST, STATE FINAL, CHECKPOINT_SEQ 3 (LAST_COMPLETED 17:WOLVES)
- **Identifiants source** : 33 FCT-001 à 033 (FACT_REGISTRY §10), 7 CLM, 5 CAU, 7 CTRL
- **Object** : se préparer aux investigations sur la corruption en France : mécanismes structurels, angles morts du contrôle, sources OSINT, méthodes d'agrégation
- **Verdict source** : la corruption directe (pots-de-vin) est quasi inaccessible en OSINT ; l'investigation efficace se concentre sur la corruption légale structurelle (pantouflage, favoritisme, conflits d'intérêts, optimisation fiscale, subventions détournées) ; 7 mécanismes structurels documentés

## 2. Faits atomiques préservés (FACT_REGISTRY)

- FCT-001 : aucune estimation officielle globale de la fraude fiscale n'est produite par l'État français (CdC : « non chiffrée », « carence regrettable », 16/12/2025) [L400 (mesuré)]
- FCT-002 : Solidaires Finances Publiques estime la fraude et l'optimisation fiscales entre 80 et 100 Mds€/an [L401 (mesuré)]
- FCT-003 : la promesse Darmanin de 2018 d'une estimation officielle n'a pas abouti [L402 (mesuré)]
- FCT-004 : résultats du contrôle fiscal : ~20 Mds€ notifiés/an ; recouvrement effectif 11,4 Mds€ en 2024 [L403 (mesuré)]
- FCT-005 : baisse de 19 % des effectifs du contrôle fiscal DGFiP entre 2015 et 2024 [L404 (mesuré)]
- FCT-006 : baisse d'environ 3000 ETP vérificateurs fiscaux entre 2010 et 2017 (13 336 → 10 252) [L405 (mesuré)]
- FCT-007 : le PNF compte 20 magistrats en 2025 (+ ~30 juristes assistants) [L406 (mesuré)]
- FCT-008 : le PNF traite 750-770 procédures en continu [L407 (mesuré)]
- FCT-009 : verrou de Bercy réformé en 2018 : transmission automatique au parquet pour fraudes > 100 000 € [L408 (mesuré)]
- FCT-010 : 44 % des affaires de fraude fiscale classées sans suite ; 27 % renvoyées en correctionnelle [L409 (mesuré)]
- FCT-011 : les dénonciations obligatoires sont passées de ~935 (avant 2018) à 2 176 en 2024 [L410 (mesuré)]
- FCT-012 : contrôle de légalité : 1019 ETP en 2010 → 868 ETP en 2024 (-15 %) ; contrôle budgétaire : 343 → 252 (-26,5 %) [L411 (mesuré)]
- FCT-013 : seuls 19,6 % des actes transmis aux préfectures sont effectivement contrôlés (7,72 millions d'actes/an) [L412 (mesuré)]
- FCT-014 : 37 % des recours gracieux des préfets ne débouchent sur aucune action corrective [L413 (mesuré)]
- FCT-015 : HATVP : 751 saisines mobilité en 2024, 639 avis rendus ; 4,5 % d'incompatibilités [L414 (mesuré)]
- FCT-016 : 3 500+ représentants d'intérêts inscrits au répertoire HATVP en 2025 (+9 % vs 2024) [L415 (mesuré)]
- FCT-017 : sanction pour non-déclaration lobbying : 1 an prison + 15 000 € amende (loi Sapin 2) [L416 (mesuré)]
- FCT-018 : proposition de loi casier judiciaire vierge votée AN 01/02/2017 (unan.), bloquée au Sénat depuis [L417 (mesuré)]
- FCT-019 : 934 infractions d'atteinte à la probité enregistrées en 2024 (+8,2 % vs 2023) [L418 (mesuré)]
- FCT-020 : CPI France : score 66/100, rang 27e mondial (2024-2025), en baisse vs 69-72 (années 2010) [L419 (mesuré)]
- FCT-021 : AFA : 119 contrôles publics + 175 contrôles privés réalisés (cumul 2017-2025) [L420 (mesuré)]
- FCT-022 : 802 signalements reçus par l'AFA en 2024 (+83 % vs 2023) [L421 (mesuré)]
- FCT-023 : TRACFIN : 211 165 déclarations de soupçon reçues en 2024 (première fois > 200 000) [L422 (mesuré)]
- FCT-024 : TRACFIN : 3 998 notes d'information transmises en 2024 (+9,6 % vs 2023) [L423 (mesuré)]
- FCT-025 : GRECO : seules 4 recommandations sur 18 mises en œuvre par la France (5e cycle, rapport déc. 2025) [L424 (mesuré)]
- FCT-026 : directive UE lanceurs d'alerte transposée (loi 21/03/2022) ; 10 000+ signalements en 2025 (vs 2 000 en 2023) [L425 (mesuré)]
- FCT-027 : le parquet N'EST PAS indépendant du ministre de la Justice (loi organique 20/11/2023 maintient le lien hiérarchique) [L426 (mesuré)]
- FCT-028 : l'accès public inconditionnel au RBE est RESTREINT depuis le 31/07/2024 (CJUE C-37/20) [L427 (mesuré)]
- FCT-029 : données ouvertes HATVP disponibles sur data.gouv.fr : déclarations d'intérêts, de patrimoine, avis mobilité, registre lobbys (CSV/XML) [L428 (mesuré)]
- FCT-030 : DECP : millions de marchés publics publiés, API tabulaire disponible, qualité variable [L429 (mesuré)]
- FCT-031 : déontologue AN : 1 contrôle par député par législature (Rémi Schenberg, nommé 04/2025) [L430 (mesuré)]
- FCT-032 : la CJIP est utilisée : 4 signées en 2025 [L431 (mesuré)]
- FCT-033 : les pays scandinaves ont des scores CPI de 85-90/100 (vs 66 pour la France) [L432 (mesuré)]

## 3. Acteurs nominaux

**Institutions de contrôle** : DGFiP, PNF (20 magistrats), AFA (294 contrôles cumulés), HATVP (639 avis/an), TRACFIN (211 165 déclarations), préfets (contrôle de légalité), déontologue AN (Rémi Schenberg), GRECO.
**Personnes** : Bruno Darmanin (promesse 2018 non aboutie), Rémi Schenberg (déontologue AN).
**Catégories** : fraudeurs fiscaux, lobbyistes (3 500+), ex-agents publics en pantouflage, lanceurs d'alerte, rentiers de l'optimisation fiscale (grandes entreprises, HNWI).

## 4. Sources externes citées

SRC-003 (CdC déc. 2025 : « non chiffrée », « carence regrettable »), SRC-004 (Sénat 07/2025), SRC-005 (HATVP), SRC-006 (AFA), SRC-007 (TRACFIN), SRC-008 (GRECO 11/12/2025), SRC-009 (loi 21/03/2022), SRC-010 (Interstats), SRC-011 (Transparency International), SRC-012 (loi organique 20/11/2023), SRC-013 (HATVP 07/2025), SRC-014 (CJUE C-37/20), SRC-015 (DECP), SRC-016 (data.gouv.fr HATVP).

## 5. Chronologie datée

1997 : convention OCDE (contexte) ; 2010-2017 : -3 084 ETP vérificateurs ; 01/02/2017 : PPL casier vierge votée AN ; 2018 : verrou de Bercy réformé (23/10), promesse Darmanin ; 2019-2025 : rapports CdC ; 2020 : fusion CDFP/HATVP ; 21/03/2022 : loi lanceurs d'alerte ; 20/11/2023 : loi organique parquet ; 31/07/2024 : RBE restreint (CJUE) ; 2024 : 934 infractions probité, 802 signalements AFA, 211 165 déclarations TRACFIN ; 2025 : CPI 66/100, 4 CJIP, GRECO 4/18, 3 500+ lobbyistes ; 16/12/2025 : rapport CdC fraude fiscale.

## 6. Mécanismes / chaînes causales

**M1 — Le sous-dimensionnement délibéré du contrôle (CAU-001)** : réduction des ETP fiscaux/préfectoraux 2010-2024 (-19 %, -3 084, -15 %, -26,5 %) → impunité des fraudeurs ; contrôle de légalité à 19,6 % des actes, 37 % des recours sans suite. Niveau : L2 (PROBABLE). [L404-L406, L411-L413 (mesuré)]
**M2 — L'opacité institutionnelle (CAU-002)** : absence de chiffres officiels sur la fraude (CdC : « carence regrettable ») + RBE restreint → impossibilité de mesurer l'ampleur. Niveau : L2 (CONFIRMÉ). [L400, L427 (mesuré)]
**M3 — La capture réglementaire (CAU-003)** : lobbying opaque (3 500+ RI, amendements clés en main) + pantouflage non sanctionné (4,5 % d'incompatibilités) → lois favorables aux intérêts privés. Niveau : L2 (PROBABLE). [L414-L416 (mesuré)]
**M4 — L'indépendance judiciaire incomplète (CAU-004)** : parquet sous autorité du ministre (loi organique 20/11/2023) + remontée d'informations → poursuites sélectives. Niveau : L2 (CONFIRMÉ). [L426 (mesuré)]
**M5 — Les délais judiciaires excessifs (CAU-005)** : affaire Tibéri : 21 ans pour condamner ; délai moyen fraude fiscale : 42 mois → impunité de fait. Niveau : L2 (PROBABLE). [L409 (mesuré)]

## 7. Verbatim et citations

- Verdict LEAD_QUESTION : « la corruption directe (pots-de-vin) est quasi-inaccessible en OSINT. L'investigation efficace se concentre sur la corruption légale structurelle » [L552 (mesuré)]
- CLM-001 CONFIRMÉ : « la corruption est structurelle en France (indice CPI en baisse, dispositifs sous-dimensionnés, GRECO 4/18) » [L438 (mesuré)]
- CLM-006 CONFIRMÉ : « la justice N'EST PAS indépendante (parquet sous autorité du ministre après loi 2023) » [L443 (mesuré)]
- CLM-007 CONFIRMÉ : « le pantouflage est massif (4,5 % d'incompatibilités seulement, 74-76 % compatibilité avec réserves) » [L444 (mesuré)]

## 8. Notes méthodologiques source

- **Fiabilité** : 7 claims validés (CLM-001 à 007, dont 6 CONFIRMÉS) ; 16 sources (SRC-003 à SRC-016) ; hiérarchisation des hypothèses marquées (PROBABLE vs CONFIRMÉ).
- **F-##** : 33/33 identifiants FCT-001 à 033 préservés verbatim.
- **Méthode** : FACT_REGISTRY, CAUSALITY_REGISTRY (5 chaînes causales), IMPACT_MAP, ACTOR_NETWORK_MAP, CONTROL_MAP (7 contrôles), architecture OSINT en 4 piliers (rapports institutionnels, données ouvertes, presse investigation, archives web).

## 9. Limites connues (case-limites)

- Limites honnêtes (7) : pots-de-vin indétectables en OSINT ; RBE restreint (obstacle majeur) ; qualité variable des données DECP ; délai 12-18 mois des sources primaires ; pas d'accès aux procédures judiciaires en cours ; chiffrage exact impossible (pas d'estimation officielle) ; prescription 3-6 ans limitant la période investigable.
- 5 angles morts exploitables : pantouflage non sanctionné (74 % compatibilité avec réserves), concentration des marchés (DECP × RNE), avenants suspects (DECP modifications), déclarations d'intérêts incohérentes (HATVP open data), subventions sans contrôle (data.gouv.fr × AFA).
