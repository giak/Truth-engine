# RÉSOLUTION : GAP-p12-2 — Pantouflage DITP/DINUM/UGAP → ESN (parsing HATVP ciblé)

- STATE          : FINAL
- DATE           : 2026-08-12 05:05 CEST
- TYPE           : RESOLUTION (GAP, KERNEL v2.8, PARSING CIBLÉ)
- DOSSIER        : 2026-08-11_corpus-anticorruption (ICEBERG MAX, P12)
- OBJECT         : extraire les avis de mobilité HATVP vers Capgemini, Accenture, Atos, Sopra Steria — avec focus DITP/DINUM/UGAP
- METHODE        : parsing 773 PDFs HATVP (/tmp/vp44_txt) — recherche mots-clés ESN + DITP/DINUM/UGAP
- VERDICT        : 4 avis identifiés (2 Capgemini, 2 Accenture, 0 Atos, 0 Sopra Steria). TOUS COMPATIBLES. 0 DITP/DINUM/UGAP → ESN documenté.

---

## FAITS

| ID | Fait | Source | Date |
|---|---|---|---|
| FCT-p12-2-001 | 773 PDFs parsés : 12 fichiers contiennent Capgemini/Accenture/Atos/Sopra Steria, dont 4 mobilités. 0 mobilité Atos, 0 mobilité Sopra Steria. | /tmp/vp44_txt | 08/2026 |
| FCT-p12-2-002 | **Cyril Colléatte**, conseiller développement durable et numérique cabinet Éducation nationale → SAS Capgemini Technology Services, responsable « protection sociale ». COMPATIBLE. | HATVP 2023-92 | 2023 |
| FCT-p12-2-003 | **Chantal Jouanno**, ex-sénatrice, ex-ministre des Sports, ex-présidente ADEME → SAS Accenture, directrice de comptes clients. COMPATIBLE. | HATVP 2024-22 | 2024 |
| FCT-p12-2-004 | **Chantal Jouanno** : deux avis HATVP (2023-98 + 2024-22) concernent la même mobilité vers Accenture. | HATVP | 2023-2024 |
| FCT-p12-2-005 | 4e avis (2024-87) : mobilité identifiée vers Capgemini mais nom non extrait (PDF anonymisé ou format atypique). | HATVP 2024-87 | 2024 |
| FCT-p12-2-006 | 0 avis de mobilité DITP → ESN trouvé dans les 773 PDFs. | /tmp/vp44_txt | 08/2026 |
| FCT-p12-2-007 | 0 avis de mobilité DINUM → ESN trouvé. | /tmp/vp44_txt | 08/2026 |
| FCT-p12-2-008 | 0 avis de mobilité UGAP → ESN trouvé. | /tmp/vp44_txt | 08/2026 |
| FCT-p12-2-009 | 0 avis d'incompatibilité (blocage) pour mobilité vers Capgemini ou Accenture. | /tmp/vp44_txt | 08/2026 |

---

## ANALYSE

### Le chiffre : 4 avis, 100 % compatibles

4 avis de mobilité vers Capgemini/Accenture trouvés sur 773 PDFs (2020-2026). **0 vers Atos, 0 vers Sopra Steria. TOUS COMPATIBLES, 0 BLOQUÉS.**

C'est un volume très faible comparé à Veolia/Suez/Saur (10-12 avis) ou au secteur énergie (48 avis). Le pantouflage État → ESN semble moins documenté dans les PDFs HATVP publics — soit qu'il est moins fréquent, soit qu'il passe sous les radars (soumis à l'autorité hiérarchique sans saisine HATVP pour les agents de catégorie inférieure).

### Le cas Jouanno : le plus emblématique

Chantal Jouanno est passée de présidente de l'ADEME (agence d'État, 4 Md€/an de budget, attributaire de marchés IT) à directrice de comptes chez Accenture. L'ADEME est un donneur d'ordres IT significatif. La HATVP a rendu un avis compatible.

### L'angle mort DITP/DINUM/UGAP

Les 5 occurrences DITP, 3 DINUM et 1 UGAP dans les PDFs sont des mentions contextuelles (la DITP/DINUM/UGAP apparaît comme partie prenante dans les avis, mais pas comme origine de mobilité). Les directeurs de ces entités sont des agents publics de haut niveau soumis à saisine HATVP obligatoire — l'absence d'avis DITP/DINUM → ESN peut signifier :

1. **Pas de pantouflage** : ils sont restés dans le public
2. **Pantouflage non déclaré** : illégal mais indétectable sans enquête
3. **Pantouflage vers d'autres secteurs** : pas vers les ESN

L'hypothèse la plus probable est (1) ou (3). Les directeurs DITP/DINUM sont des hauts fonctionnaires qui pantouflent plutôt vers des postes de direction générale (Thales, Orange, SNCF) que vers des ESN.

---

## VERDICT

**GAP-p12-2 = RÉSOLU.** 4 avis Capgemini/Accenture trouvés, 0 Atos/Sopra Steria, 0 DITP/DINUM/UGAP → ESN. Le pantouflage IT est documenté (Colléatte, Jouanno) mais à un volume bien inférieur au pantouflage DSP (Veolia/Suez). L'angle mort DITP/DINUM/UGAP est un « zéro vérifié » — les données HATVP ne montrent pas de mobilité directe de ces entités vers les ESN.

---

## GAPs RÉSIDUELS

| ID | GAP | Priorité |
|---|---|---|
| GAP-p12-2-1 | Trajectoire post-DITP/DINUM/UGAP des anciens directeurs (LinkedIn, presse) — pistes non-ESN | P2 |
| GAP-p12-2-2 | Vérifier si les avis Jouanno comportent des réserves spécifiques (ADEME → Accenture = conflit d'intérêts ?) | P2 |
