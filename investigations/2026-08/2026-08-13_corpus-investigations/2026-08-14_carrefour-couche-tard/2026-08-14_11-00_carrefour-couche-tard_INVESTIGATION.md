# INVESTIGATION : « CARREFOUR PROTÉGÉ EN 48 HEURES » — Le veto politique à l'OPA de Couche-Tard (janvier 2021) et la sélectivité du bouclier anti-OPA

## RUN_MANIFEST (FINAL)

```
ENGINE_VERSION : 2.8
STATE          : FINAL
RUN_ID         : 20260814-1100-carrefour-couche-tard
PARENT_RUN_ID  : NONE (INPUT_KIND=TOPIC) ; corpus frère : 20260812-1800-iceberg-max-alstom-areva (sélectivité du décret), 20260809-1535-grille-ief-photonis-latecoere, 20260814-0900-opella-sanofi-cdr (sélectivité du bouclier)
AS_OF          : 2026-08-13
INPUT_KIND     : TOPIC (thème : blocage par le gouvernement de l'OPA de Couche-Tard sur Carrefour en janvier 2021 : mécanisme, temporalité, sélectivité)
MISSION_MODE   : INVESTIGATION
INPUT_REF      : NONE (topique utilisateur, re-pipeline T5 cessions)
SUBJECT_SLUG   : carrefour-couche-tard
INVESTIGATION_PATH : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-14_carrefour-couche-tard/2026-08-14_11-00_carrefour-couche-tard_INVESTIGATION.md
SCOPE          : tentative d'OPA de Couche-Tard (Canada) sur Carrefour, janvier 2021 : révélation (12/01), réaction Le Maire (13/01), abandon (15-16/01), mécanisme (IEF, sécurité alimentaire), cours de Bourse, comparaison Alstom/GE 2014, sélectivité ; géographie : France, Canada
COMPLEXITY     : CX_SCORE=11 → $CX=STANDARD (political 3, technical 1, temporal 2, geo 2, narratives 2, data 1)
CHECKPOINT_SEQ : 0 (run mono-session)
LAST_COMPLETED : 12
NEXT_ACTION    : NONE
RESUME_COUNT   : 0
ROUTE_OVERRIDES: []
LOADED_MODULES : KERNEL v2.8 | SYMBOLS | PATTERNS | THREATS | GATES | REQUEST_LOG | EPISTEMIC | TEMPLATE | INVESTIGATION (tous chargés)
DEGRADED_FLAGS : []
HASH_CAPABILITY: HASH_UNAVAILABLE
```

## 1. RÉSUMÉ EXÉCUTIF

**Réponse à l'OBJECT_QUESTION** (« pourquoi l'État a-t-il pu bloquer l'OPA sur Carrefour en 48 heures alors qu'il n'a pas pu empêcher Alstom/GE en 2014, et qu'est-ce que cela documente sur la sélectivité du contrôle ? ») :

Le 12/01/2021 (soir), l'agence Bloomberg révèle l'approche amicale du groupe canadien **Alimentation Couche-Tard** en vue d'un rapprochement avec **Carrefour** (valorisation implicite **~16,2 Md€**). Dès le **13/01/2021**, le ministre de l'Économie **Bruno Le Maire** déclare « a priori, je ne suis pas favorable à cette opération » et qualifie Carrefour de « chaînon essentiel dans la sécurité alimentaire des Français, dans la souveraineté alimentaire » (premier employeur privé de France). Le **15/01/2021**, il oppose un « non clair et définitif » ; Couche-Tard **abandonne** le même jour (communiqué conjoint le 16/01/2021). Le cours de Carrefour avait bondi de **+10 à 14 %** le 13/01. Le mécanisme : la **pression politique** appuyée sur le contrôle des investissements étrangers (IEF), dont le champ couvrait déjà la **sécurité alimentaire** depuis le décret 2019-1590 du 31/12/2019 — sans qu'une procédure administrative complète soit allée à son terme.

**Verdict sur le LEAD_QUESTION** : **SOUTENU (sélectivité documentée)**. Le contraste avec 2014 est un fait : en 2014, le « décret Montebourg » (14/05/2014) a été signé **après** l'OPA GE (mars 2014) et n'a jamais été utilisé contre GE ; en 2021, l'État a bloqué l'opération en **48 heures** par une déclaration politique. La sélectivité est donc documentée dans les deux sens : l'État protège un acteur grand public très visible (Carrefour, 1er employeur privé) et laisse passer des cessions industrielles contestées (Alstom). Le blocage de Carrefour a été salué de façon transpartisane ; aucun fait pénal n'est documenté.

**Acteurs** : Bruno Le Maire (ministre de l'Économie), Couche-Tard (Brian Hannasch), Carrefour (Alexandre Bompard), DG Trésor (IEF), syndicats (CFDT, CGT), gouvernement français.

## 2. MANIPULATION_REPORT (15 symboles scorés sur corpus)

| # | Symbole | Score | Justification (corpus) |
|---|---------|-------|------------------------|
| 1 | **Ξ** omission | **8/10** | Le contenu exact des discussions (prix, conditions) n'a jamais été publié ; l'avis formel de l'IEF n'a pas été rendu (procédure inaboutie) ; l'analyse économique du blocage (effet sur l'attractivité) n'est pas chiffrée. |
| 2 | **€** money | **6/10** | Valorisation implicite ~16,2 Md€ / 20 G$ ; ~20 €/action ; +10 à 14 % de hausse du cours ; pas de chiffre de coût du blocage. |
| 3 | **Λ** framing | **8/10** | « Souveraineté alimentaire » (gouvernement) vs « protectionnisme arbitraire » (critiques libérales) ; « fleuron national » vs « géant canadien des supérettes » ; la « sécurité alimentaire » élargie aux secteurs protégés en 2019. |
| 4 | **Ω** inversion | **7/10** | Le même État qui n'a pas pu (ou pas voulu) bloquer Alstom en 2014 bloque Carrefour en 48 h en 2021 : le « patriotisme économique » s'exerce sélectivement ; l'outil (IEF) existait en 2014, son usage diffère. |
| 5 | **Ψ** sidération | 4/10 | Champ économique ; peu de pic émotionnel (hors symbolique Carrefour). |
| 6 | **↕** verticalité | **8/10** | Décision politique unilatérale (une déclaration ministérielle suffit) ; salariés et consommateurs non consultés ; le cours de Bourse sanctionne en temps réel ; l'acquéreur abandonne sans recours. |
| 7 | **Φ** spectacle | 3/10 | Épisode bref (4 jours), faible mise en scène. |
| 8 | **Σ** sémiotique | **7/10** | « Carrefour », « premier employeur privé », « sécurité alimentaire » : symbolique sociale forte. |
| 9 | **Κ** cynisme | **7/10** | L'État protège un acteur grand public (2021) mais a validé ou laissé passer des cessions industrielles contestées (Alstom 2014) ; le « bouclier » existe, son usage est politique. |
| 10 | **ρ** résistance | **5/10** | Soutien transpartisan au blocage ; critiques libérales ; pas de recours juridictionnel. |
| 11 | **κ** influence subtile | **5/10** | Rôle des banques-conseils des deux côtés (non documenté publiquement ici) ; négociations en huis clos avant la révélation Bloomberg. |
| 12 | **⫸** convergence | **7/10** | Convergence sans contamination : Bloomberg, déclarations Le Maire, communiqués des deux groupes, presse canadienne convergent sur la même chronologie de 96 heures. |
| 13 | **⚔** guerre cognitive | 2/10 | Pas d'opération coordonnée documentée. |
| 14 | **🌐** réseau | **6/10** | Nœuds : Carrefour, Couche-Tard, Bercy, DG Trésor/IEF, syndicats, actionnaires. |
| 15 | **⏰** temporalité | **8/10** | 12/01 (révélation) → 13/01 (Le Maire) → 15/01 (non définitif, abandon) → 16/01 (communiqué conjoint) : 96 heures, contraste maximal avec 2014 (décret après l'OPA). |

## 3. CHRONOLOGIE

- **31/12/2019** : décret n° 2019-1590 élargissant le champ de l'IEF (dont la sécurité alimentaire).
- **12/01/2021 (soir)** : Bloomberg révèle l'approche de Couche-Tard ; officialisation dans la nuit des discussions exploratoires.
- **13/01/2021** : Bruno Le Maire (France 5) : « a priori, je ne suis pas favorable à cette opération » ; Carrefour = « chaînon essentiel dans la sécurité alimentaire » ; cours Carrefour : +10 à 14 %.
- **15/01/2021** : Le Maire : « non clair et définitif » ; Couche-Tard annonce l'abandon.
- **16/01/2021** : communiqué conjoint Couche-Tard/Carrefour (orientation vers des partenariats opérationnels).

## 4. FACT_REGISTRY (faits sourcés)

| ID | Fait | Chiffre | Source | Statut |
|----|------|---------|--------|--------|
| FCT-001 | 12/01/2021 (soir) : l'agence Bloomberg révèle l'approche amicale de Couche-Tard en vue d'un rapprochement avec Carrefour ; discussions exploratoires officialisées dans la nuit du 12 au 13/01 | 12/01/2021 | SRC-01 Bloomberg via La Presse 12/01/2021 | ✦ |
| FCT-002 | 13/01/2021 : Bruno Le Maire (France 5) : « a priori, je ne suis pas favorable à cette opération » | 13/01/2021 | SRC-02 Challenges 13/01/2021 | ✦ |
| FCT-003 | Le Maire qualifie Carrefour de « chaînon essentiel dans la sécurité alimentaire des Français, dans la souveraineté alimentaire » et rappelle qu'il est le premier employeur privé de France | — | SRC-02 Challenges ; SRC-03 Ouest-France 17/01/2021 | ✦ |
| FCT-004 | 15/01/2021 : Le Maire oppose un « non clair et définitif » au projet | 15/01/2021 | SRC-04 Le Club des Juristes 01/02/2021 | ✦ |
| FCT-005 | 15-16/01/2021 : Couche-Tard abandonne son projet d'OPA ; communiqué conjoint le 16/01/2021 (orientation vers des partenariats opérationnels) | 16/01/2021 | SRC-05 communiqué conjoint Couche-Tard/Carrefour 16/01/2021 | ✦ |
| FCT-006 | Valorisation implicite de l'offre : ~16,2 Md€ (~20 G$, ~20 €/action) | ~16,2 Md€ | SRC-01/05 presse et communiqués | ✧ |
| FCT-007 | Cours de Carrefour le 13/01/2021 : hausse de +10 à 14 % dès l'ouverture (action un temps réservée à la hausse) | +10-14 % | SRC-06 Reuters 13/01/2021 | ✦ |
| FCT-008 | Mécanisme : pression politique appuyée sur le contrôle IEF ; la sécurité alimentaire avait été ajoutée au champ par le décret n° 2019-1590 du 31/12/2019 ; aucune décision administrative IEF écrite définitive n'est documentée (procédure inaboutie) | — | SRC-04 Le Club des Juristes ; SRC-07 Portail-IE | ✦ |
| FCT-009 | Contraste 2014 : le « décret Montebourg » (décret 2014-479 du 14/05/2014) a été signé après le début de l'OPA GE sur Alstom (mars 2014) et n'a pas empêché l'opération | — | SRC-07 Portail-IE ; corpus frère iceberg-max-alstom-areva | ✦ |
| FCT-010 | La sélectivité est documentée : même État qui a laissé passer Alstom/GE (2014) et validé d'autres cessions, bloque Carrefour en 48 h (2021) au nom de la sécurité alimentaire | — | SRC-03 Ouest-France ; SRC-07 Portail-IE | ✦ |
| FCT-011 | Soutien politique transpartisan au blocage (gauche et droite) ; inquiétudes syndicales (CFDT, CGT Carrefour) apaisées | — | SRC-08 Courrier International 17/01/2021 ; SRC-09 BFM 05/02/2021 | ✦ |
| FCT-012 | Critiques libérales : protectionnisme jugé arbitraire, risque pour l'attractivité de la place de Paris | — | SRC-08 Courrier International ; presse | ✧ |
| FCT-013 | Couche-Tard fustige ensuite « les politiques français » (05/02/2021) et maintient son intérêt pour des partenariats | 05/02/2021 | SRC-09 BFM 05/02/2021 | ✦ |
| FCT-014 | Aucune procédure de blocage formelle complète n'a été nécessaire : la déclaration politique a suffi à dissuader l'acquéreur | — | SRC-04 Le Club des Juristes | ✦ |


<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ❧ | - | - | - | 2026-08-14_11-00_carrefour-couche-tard | - | -
FCT-002 | FACT | ❧ | - | - | - | 2026-08-14_11-00_carrefour-couche-tard | - | -
FCT-003 | FACT | ❧ | - | - | - | 2026-08-14_11-00_carrefour-couche-tard | - | -
FCT-004 | FACT | ❧ | - | - | - | 2026-08-14_11-00_carrefour-couche-tard | - | -
FCT-005 | FACT | ❧ | - | - | - | 2026-08-14_11-00_carrefour-couche-tard | - | -
FCT-006 | FACT | ❧ | - | - | - | 2026-08-14_11-00_carrefour-couche-tard | - | -
FCT-007 | FACT | ❧ | - | - | - | 2026-08-14_11-00_carrefour-couche-tard | - | -
FCT-008 | FACT | ❧ | - | - | - | 2026-08-14_11-00_carrefour-couche-tard | - | -
FCT-009 | FACT | ❧ | - | - | - | 2026-08-14_11-00_carrefour-couche-tard | - | -
FCT-010 | FACT | ❧ | - | - | - | 2026-08-14_11-00_carrefour-couche-tard | - | -
FCT-011 | FACT | ❧ | - | - | - | 2026-08-14_11-00_carrefour-couche-tard | - | -
FCT-012 | FACT | ❧ | - | - | - | 2026-08-14_11-00_carrefour-couche-tard | - | -
FCT-013 | FACT | ❧ | - | - | - | 2026-08-14_11-00_carrefour-couche-tard | - | -
FCT-014 | FACT | ❧ | - | - | - | 2026-08-14_11-00_carrefour-couche-tard | - | -
<!-- /FACT_REGISTRY_V1 -->

## 5. CLAIM_REGISTRY

| ID | Claim | Support | Contre-évidence | Statut |
|----|-------|---------|-----------------|--------|
| CLM-001 | « L'État a protégé Carrefour » | Déclarations Le Maire (FCT-002 à 004), abandon (FCT-005) | L'abandon relève de la décision de Couche-Tard ; pas de décision administrative formelle | SOUTENU (protection politique effective) |
| CLM-002 | « Le bouclier anti-OPA est sélectif » | 2014 (décret après l'OPA, GE validé) vs 2021 (blocage 48 h) (FCT-008 à 010) | Cas différents (industriel vs grande distribution) ; le décret 2019-1590 élargit le champ entre les deux | SOUTENU (sélectivité documentée) |
| CLM-003 | « Le blocage a nui à l'attractivité de la France » | Critiques libérales (FCT-012) | Pas de mesure chiffrée ; soutien transpartisan (FCT-011) | CONTESTÉ (non démontré) |
| CLM-004 | « L'outil utilisé était l'IEF » | Sécurité alimentaire dans le champ IEF depuis 2019 (FCT-008) | Pas de procédure formelle aboutie : l'outil a été brandi, pas déployé | PARTIELLEMENT SOUTENU (menace IEF + pression politique) |

## 6. CONTRADICTION_LEDGER

| ID | Contradiction | Résolution | Statut |
|----|---------------|------------|--------|
| CONTR-001 | « Carrefour est protégé par l'État » vs « Alstom a été cédé à GE » | Sélectivité : l'État exerce le contrôle qu'il a, quand il le veut ; les régimes juridiques diffèrent (2014 vs 2019-2021) mais la volonté politique est l'élément discriminant documenté | DOCUMENTÉE (sélectivité) |
| CONTR-002 | « Soutien transpartisan au blocage » vs « critique libérale du protectionnisme » | Débat politique, pas de fait contradictoire ; les deux positions sont documentées (FCT-011/012) | DOCUMENTÉE (non tranchée) |
| CONTR-003 | « Abandon par Couche-Tard » vs « Couche-Tard maintient son intérêt » (02/2021) | L'OPA est abandonnée (fait) ; l'intérêt pour des partenariats opérationnels est maintenu (FCT-013) | DOCUMENTÉE (niveaux distincts) |

## 7. RÉSEAU D'ACTEURS

**Entreprises** : Carrefour, Alimentation Couche-Tard, banques-conseils (non documentées publiquement ici).
**Institutions** : Bercy / ministère de l'Économie, DG Trésor (IEF), gouvernement français.
**Personnes** : Bruno Le Maire, Alexandre Bompard (Carrefour), Brian Hannasch (Couche-Tard).
**Autres** : syndicats (CFDT, CGT), presse économique (Bloomberg, Challenges, Reuters).

## 8. MÉCANISMES / CHAÎNES CAUSALES

**M1 — Le veto politique préventif (48 heures)** : une déclaration ministérielle suffit à dissuader l'acquéreur ; le contrôle IEF est brandi sans être déployé jusqu'à une décision écrite. Type : POLITIQUE. Niveau : L2.
**M2 — La sélectivité du bouclier** : le même État qui a laissé passer Alstom/GE (2014, décret signé après l'OPA) bloque Carrefour (2021) en 48 h : l'usage du contrôle est politique et sélectif. Type : STRUCTUREL. Niveau : L2.
**M3 — La protection des actifs visibles** : le blocage s'exerce pour un acteur grand public (1er employeur privé, alimentaire) ; les cessions industrielles moins visibles (Alstom, puis Opella 2024 avec conditions) suivent d'autres trajectoires. Type : STRUCTUREL. Niveau : L2.

## 9. CARTE DIALECTIQUE (scénarios + responsabilité)

| Scénario | Hypothèse | Support | Contre | Lecture |
|----------|-----------|--------|--------|---------|
| S1 « Protection réelle de la souveraineté alimentaire » | L'État a défendu un actif stratégique | Déclarations + abandon (FCT-002 à 005) ; soutien transpartisan (FCT-011) | La sécurité alimentaire n'était pas menacée par un rachat de distributeur ; l'opération était amicale | PARTIELLEMENT SOUTENU (protection politique) |
| S2 « Sélectivité arbitraire du contrôle » | L'État protège selon la visibilité, pas selon la criticité | Contraste 2014/2021 (FCT-009/010) | Les régimes juridiques et les actifs diffèrent | SOUTENU (sélectivité documentée) |
| S3 « Cession ratée par pression politique » | L'abandon relève de la seule pression gouvernementale | Chronologie 96 h (FCT-001 à 005) | Couche-Tard a aussi évalué le rapport coût/bénéfice | PARTIELLEMENT SOUTENU (la pression est le facteur discriminant documenté) |

**RESPONSIBILITY_MAP** : la décision de blocage relève de la responsabilité politique du gouvernement (Le Maire) ; aucun fait pénal ; l'acquéreur a renoncé volontairement ; les actionnaires de Carrefour ont perdu une prime documentée (+10-14 % puis retombée). (BENEFIT != INTENT).

## 10. VERDICT 3 AXES

- **PÉNAL** : 0 fait pénal documenté.
- **INTÉGRITÉ** : CONTESTÉ — la sélectivité du bouclier anti-OPA est documentée (2014 vs 2021) : l'État dispose du contrôle et l'exerce de façon discrétionnaire ; le même État n'a pas bloqué Alstom/GE.
- **LÉGITIMITÉ** : CONTESTÉ (positif pour l'exécutif) — le blocage a été salué transpartisannement et par les syndicats ; la critique libérale (attractivité) reste non chiffrée.

## 11. PÉRIMÈTRE & LIMITES

**Inclusions** : chronologie janvier 2021, mécanisme IEF, sélectivité vs 2014, cours de Bourse, réactions. 

**Exclusions** : les négociations postérieures (partenariats opérationnels) ; la stratégie de Carrefour ; les autres OPA du secteur.

**GAP déclarés** :
- GAP-001 (ACCESS) : contenu des discussions (prix, conditions) non publié ; avis IEF formel non rendu (procédure inaboutie).
- GAP-002 (METHOD) : effet économique du blocage (attractivité) non chiffré.
- GAP-003 (CAUSALITY) : le lien entre la déclaration de Le Maire et l'abandon de Couche-Tard est documenté par la chronologie (48 h) mais la délibération interne de Couche-Tard n'est pas publique.

## 12. ÉTAT DES CONNAISSANCES

- **CONNU (✦)** : révélation 12/01/2021 ; déclarations Le Maire 13-15/01 ; abandon 15-16/01 ; hausse +10-14 % ; champ IEF incluant la sécurité alimentaire (décret 2019-1590) ; contraste 2014 ; soutien transpartisan ; déclarations Couche-Tard 02/2021.
- **PROBABLE (✧)** : valorisation implicite ~16,2 Md€ ; critiques libérales (attractivité).
- **HYPOTHÈSE (⁂)** : le rôle précis des banques-conseils dans les discussions ; l'effet durable sur l'attractivité.
- **CONTESTÉ (⊗)** : le caractère « protecteur » vs « arbitraire » du blocage ; la menace réelle sur la « sécurité alimentaire ».
- **INCONNU (⁅)** : le prix exact discuté ; l'avis IEF.

## 13. SUSPICION / VÉRIFICATION

- La chronologie (12-16/01/2021) et les déclarations de Le Maire sont confirmées par les sources concordantes (Challenges, Ouest-France, communiqués officiels) : fiables.
- La valorisation ~16,2 Md€ est une lecture de presse (SRC-01/05) : statut ✧.
- L'absence de décision IEF formelle est un constat d'absence (FCT-008/014) : à distinguer d'une décision négative (aucune n'est documentée).
