# INVESTIGATION APEX : « LES 110 DONATAIRES DU DUTREIL » — TENTATIVE DE NOMINATION DU PREMIER CENTILE (65 % DE LA DÉPENSE) PAR LES VOIES PUBLIQUES

## RUN_MANIFEST (FINAL)

```
ENGINE_VERSION : 2.8
STATE          : FINAL
RUN_ID         : 20260809-2256-dutreil-110-donataires
PARENT_RUN_ID  : 20260809-2215-beneficiaires-niches-cessions (GAP-007 : FCT-009 à 012 — Dutreil 5,5 Md€ 2024, 1er centile 65 %)
AS_OF          : 2026-08-09
INPUT_KIND     : UPDATE (croisement du constat statistique CdC avec les voies légales de nomination : presse, registres, notariat, base de données Sénat)
MISSION_MODE   : INVESTIGATION
INPUT_REF      : NONE (topique : « identifier les transmissions notifiées à la presse ou aux registres pour tenter de nommer les plus gros bénéficiaires »)
SUBJECT_SLUG   : dutreil-110-donataires
NOTE_SLUG      : « les 110 » = le dernier centile des bénéficiaires du pacte Dutreil 2024 (65 % de la dépense, 30 M€ de moyenne)
INVESTIGATION_PATH : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_dutreil-110-donataires/2026-08-09_22-56_dutreil-110-donataires_INVESTIGATION.md
SCOPE          : nomination des bénéficiaires du dernier centile Dutreil (2024) ; mécanisme (2000-2024) ; coût et concentration (CdC 18/11/2025) ; voies légales de nomination (BODACC, annonces légales, registre pactes, notariat, Challenges, presse) ; réforme (CdC, Sénat 760) ; période 2000-2026 ; France
COMPLEXITY     : CX_SCORE=13 → $CX=APEX (political 3, technical 2, temporal 3, geo 1, narratives 2, data 2)
CHECKPOINT_SEQ : 0 (run mono-session)
LAST_COMPLETED : 18b
NEXT_ACTION    : NONE
RESUME_COUNT   : 0
ROUTE_OVERRIDES: []
LOADED_MODULES : KERNEL v2.8 | SYMBOLS | PATTERNS | THREATS | GATES | REQUEST_LOG | EPISTEMIC | TEMPLATE (héritage des runs parents)
DEGRADED_FLAGS : []
HASH_CAPABILITY: HASH_UNAVAILABLE
```

## 1. RÉSUMÉ EXÉCUTIF

**Réponse à l'OBJECT_QUESTION** (« peut-on nommer les 110 donataires du premier centile Dutreil ? ») :

**NON, par aucune voie légale directe — mais l'enquête établit que ce n'est pas un mur technique : c'est une option de droit, exactement comme le secret fiscal du CIR avant l'Annexe 12 du Sénat 808.** Le cœur de l'enquête :

1. **La citation source est désormais confirmée à la source primaire** : la page de publication du rapport de la Cour des comptes « Le Pacte Dutreil : un dispositif fiscal en forte croissance à mieux cibler » (ccomptes.fr, 18/11/2025, lue via le snapshot Wayback du jour même) énonce : « Cette dépense fiscale est très concentrée sur le **dernier centile, qui représente 65 % de son total : les 110 donataires concernés en 2024 ont bénéficié d'un avantage fiscal moyen de 30 M€** » (FCT-006). **Correction terminologique du corpus 22-15 : la CdC dit « dernier centile » (le plus élevé), pas « premier centile »** — même population, formulation à corriger.
2. **Le constat d'absence est structurel et documenté** : aucun registre public des pactes Dutreil (déclarations 2022-C et actes notariés couverts par le secret fiscal et professionnel), le BODACC ne publie pas les mutations d'actions, les annonces légales n'exigent pas la publication des donations d'actions, les notaires (CSN) ne publient que des statistiques agrégées (FCT-012). **Les seules sources publiques de valorisation sont les palmarès (Challenges « Fortunes de France »), par recoupements financiers indirects, sans accès aux actes (FCT-013).**
3. **La CdC elle-même livre les clés de caractérisation que le corpus n'avait pas** : le nombre réel de transmissions est **5 000-6 000 en 2024** (la fourchette officielle 2 000-3 000 était sous-estimée), l'actif éligible atteint **20 Md€ en 2024 (12 Md€ en 2023)**, la dépense est passée de **1,2 Md€ (2020 et 2021) à >3,3 Md€ (2023) puis >5,5 Md€ (2024)** — et surtout : **l'augmentation s'explique « par la présence d'une très grosse opération sur chacune des années 2023 et 2024 »** (FCT-004). **C'est la seule piste nominative : les 110 sont en partie portés par 1-2 opérations géantes par an, identifiables par la presse.**
4. **La piste des opérations géantes est en cours de test** : la transmission du contrôle de Vivendi à Cyrille Bolloré (annoncée 06/2023, ~35 % du capital, ordre de grandeur 1,5 Md€) est la candidate naturelle de l'« opération 2023 » — la mention explicite du pacte Dutreil par la presse n'est pas encore confirmée (FCT-014, réserve ✧).
5. **La traçabilité est un choix de droit, et le Sénat l'a dit** : le rapport d'information n° 760 (Husson/Raynal, 17/06/2026, « l'imposition des hauts patrimoines ») qualifie le Dutreil d'« angle mort statistique majeur » des successions et recommande (n° 6) la **mention systématique du recours au pacte Dutreil dans les actes notariés**, qui alimenteraient une **base de données en cours de constitution sur les successions** (FCT-010). Le Sénat documente aussi les 13 324 foyers IFI à revenu nul ou négatif (hérité 22-15).
6. **Le blocage politique est documenté ET confirmé par la loi** : le jour même de la publication du rapport CdC (18/11/2025), **Sébastien Lecornu défend la niche** (Le Monde) ; la **loi n° 2026-103 du 19/02/2026 de finances pour 2026** n'a adopté qu'une « réforme a minima » (conservation 4→6 ans, exclusion des actifs somptuaires) en rejetant les recommandations de fond de la CdC (progressivité, FBO, pacte réputé acquis) — détail au dossier 2026-08-09_23-40_plf-2026-dutreil-reforme-a-minima (23:40) ; **MAJ 10/08/2026 03:55 : amendement n° 3173 (Mattei, actifs somptuaires) et sous-amendement gouvernemental n° 3552 (4→6 ans, art. 787 C) vérifiés à la SOURCE PRIMAIRE assemblee-nationale.fr (PDF lus intégralement, adopté 15/01/2026) — GAP-002 du 23-40 partiellement RÉSOLU (Juvin reste ✧)** ; réponse aux rec. du Sénat 760 : inexistante à date (PLF 2027) (FCT-011).

**Verdict sur le LEAD_QUESTION** (« nommer les plus gros bénéficiaires ») : **STRUCTURELLEMENT INNOMMABLE PAR VOIE LÉGALE, MAIS CARACTÉRISABLE ET TRAÇABLE À CONDITION DE RÉFORME.** Les noms des 110 sont protégés par le secret fiscal et notarial — ce n'est pas une impossibilité technique (l'Annexe 12 du CIR l'a démontré), c'est une option de droit que le Sénat propose de lever (recommandation n° 6) et que le gouvernement défend de ne pas lever. La seule porte nominative ouverte aujourd'hui : les « très grosses opérations » annuelles nommées par la presse économique.

**Acteurs** : 110 donataires anonymes (dernier centile), familles dirigeantes (dynasties du CAC 40 et du non-coté), DGFiP (données fiscales inédites), IPP (partenariat d'évaluation), Cour des comptes (rapport 18/11/2025), Sénat 760 (Husson/Raynal), Bercy/Lecornu (défense de la niche), notaires (CSN), presse économique (Le Monde, Boursorama, Alternatives Économiques, Challenges, Economie Matin).

**Principales limites** : les noms eux-mêmes ne sont pas accessibles (secret) ; la mention Dutreil de l'« opération Bolloré » n'est pas confirmée ; la base de données Sénat « en cours de constitution » n'est pas documentée dans son avancement ; le rapport CdC complet (PDF 20251118-Pacte Dutreil.pdf) n'a pas été lu intégralement (la synthèse officielle publiée en page l'a été).

## 2. MANIPULATION_REPORT (15 symboles scorés sur corpus)

| # | Symbole | Score | Justification (corpus) |
|---|---------|-------|------------------------|
| 1 | **Ξ** omission | **9/10** | Aucun registre public des pactes Dutreil ; le BODACC et les annonces légales ne couvrent pas les donations d'actions ; la DGFiP détient les noms sans les publier ; la « base de données sur les successions » du Sénat est en cours de constitution. |
| 2 | **€** money | **9/10** | Dépense >5,5 Md€ 2024 (1,2 Md€ 2020/2021) ; actif éligible 20 Md€ 2024 ; 110 donataires = 65 % ; 30 M€ de moyenne ; ~8 % de taux d'imposition effectif vs 34 % droit commun. |
| 3 | **Λ** framing | 7/10 | « Transmission familiale d'entreprise » (vertueux) vs « niche fiscale » (critique) ; « outil de pérennité du contrôle familial » (CdC reconnaît l'effet) vs « avantage très important procuré à un nombre réduit de familles » (CdC critique). |
| 4 | **Ω** inversion | **9/10** | Le dispositif créé pour sauver les PME industrielles bénéficie au commerce (44 % de la VA) ; la cible prioritaire déclarée (industrie) ne pèse que 13 % des transmissions ; « le plus favorable d'Europe » (CdC) sans évaluation depuis 2000 jusqu'en 2025 ; l'effet d'emploi/investissement n'est pas observé mais la niche est défendue. |
| 5 | **Ψ** sidération | 3/10 | Champ froid pour le grand public (chiffres techniques), chaud pour les initiés (30 M€ par donataire). |
| 6 | **↕** verticalité | **9/10** | 110 donataires = 65 % de la dépense (5 000-6 000 transmissions/an : les 2 % du haut captent les deux tiers) ; 30 M€ vs 1,8 M€ de moyenne nationale ; ~8 % vs 34 % de taux effectif. |
| 7 | **Φ** spectacle | 2/10 | Aucun spectacle médiatique ; la publication du rapport a été noyée dans les débats budgétaires. |
| 8 | **Σ** sémiotique | 4/10 | « Pacte », « transmission », « famille » : vocabulaire du patrimoine affectif naturalisant un transfert fiscal massif vers les plus hauts patrimoines. |
| 9 | **Κ** cynisme | **9/10** | Le dispositif « n'a jamais été évalué depuis sa création » (2000-2025) ; les noms sont secrets alors que l'impôt sur les petites transmissions est public (droits de mutation) ; Lecornu défend la niche le jour même de la publication du rapport ; la fourchette officielle 2 000-3 000 transmissions/an était fausse depuis des années. |
| 10 | **ρ** résistance | **8/10** | CdC (rapport complet 18/11/2025), IPP (partenariat), Sénat 760 (17/06/2026, recommandation n° 6), presse (Le Monde, Alternatives Économiques, Economie Matin, Boursorama). |
| 11 | **κ** influence subtile | 7/10 | Architecture par défaut : l'abattement 75 % sans progressivité profite proportionnellement aux très grosses transmissions ; les « très grosses opérations » annuelles gonflent la dépense sans débat ciblé ; la sous-estimation officielle du nombre de transmissions a faussé le débat public. |
| 12 | **⫸** convergence | 7/10 | CdC 18/11/2025 + Sénat 760 06/2026 + évaluations IPP convergent : coût massif, concentration extrême, effets économiques faibles, traçabilité absente — trois institutions indépendantes. |
| 13 | **⚔** guerre cognitive | 1/10 | Aucune campagne organisée documentée (le lobby notarial/patronal n'est pas documenté dans ce dossier). |
| 14 | **🌐** réseau | 7/10 | 110 donataires anonymes, dynasties familiales, notaires, DGFiP, IPP, CdC, Sénat, Bercy, presse. |
| 15 | **⏰** temporalité | **8/10** | 2000 création ; 2003 loi Dutreil ; 2018-2024 3 000-4 000 transmissions/an ; 2023 12 Md€ et 3,3 Md€ ; 2024 20 Md€, 5 000-6 000 transmissions, 5,5 Md€, opérations géantes ; 18/11/2025 rapport CdC + défense Lecornu ; 17/06/2026 Sénat 760. |

**BIAS TEST (15/15 scorés).** Aucun symbole au-delà de 9. Les champs 1, 4, 6, 9 signalent le noyau : une dépense en explosion, ultra-concentrée, invisible, défendue politiquement.

**PATTERNS** : @PAT[ICEBERG] (Ξ=9), @PAT[MONEY] (€=9), @PAT[POWER] (↕=9), @PAT[CYN] (Κ=9), @PAT[TIME] (⏰=8). **THREATS** : @THR[REG_CAPTURE] (niche sanctuarisée), @THR[OPACITY] (pas de registre), @THR[SUBSIDY] (effets non observés).

**RHETORICAL** : NUM (5,5 Md€, 65 %, 30 M€, 20 Md€, 5 000-6 000, 8 % vs 34 %) ; AUTH (CdC, Sénat 760, IPP) ; DEM et BF = 0.

## 3. CLUSTERS (routage SYMBOLS §4)

| Cluster | Diagnostic | Gap |
|---------|------------|-----|
| ICEBERG (Ξ=9) | Émergé : coût, concentration, secteurs, effets. Immergé : les noms (secret), le détail des opérations géantes, la base de données Sénat. | Nomination impossible. |
| MONEY (€=9) | Flux : contribuable → État (20,9 Md€ DMTG) → exonération Dutreil (>5,5 Md€) → 110 donataires (65 %) + 4 900-5 900 autres. | Qui exactement dans les 110 ? |
| POWER (↕=9) | 110 = 65 % ; 30 M€ vs 1,8 M€ ; ~8 % vs 34 %. | — |
| INVERSION (Ω=9, Κ=9) | PME industrielles (cible) vs commerce (44 % VA) ; « jamais évalué » 2000-2025 ; défense politique le jour de la publication. | — |
| CONFIRMATION (κ=7) | Abattement sans progressivité ; sous-estimation officielle du nombre de transmissions. | — |
| FRAGMENTATION (⫸=7) | CdC + Sénat 760 + IPP convergent. | — |
| NETWORK (🌐=7) | Dynasties, notaires, DGFiP, contrôleurs. | Lobby notarial non documenté. |
| TEMPORAL (⏰=8) | 2000 → 2026 : évaluation tardive, réforme non engagée. | — |

## 4. HERMÉNEUTIQUE (statut : ANALYSE)

- **L1 (texte) :** CdC 18/11/2025 (page officielle de publication — snapshot Wayback du jour même), Sénat 760 (17/06/2026), Le Monde 18/11/2025 (Lecornu), Alternatives Économiques 25/11/2025, Economie Matin, Boursorama 24/10/2025 (synthèse AFP/Le Monde), corpus 22-15 (FCT-009 à 012).
- **L2 (structure) :** deux strates de visibilité — (a) statistique complète (coût, centiles, secteurs, effets) publiée par la CdC sur données DGFiP inédites ; (b) nominative inexistante (aucun registre, secret notarial). **L'asymétrie n'est pas accidentelle : elle résulte du choix de ne pas créer de registre** (le Sénat 760 le formule en recommandation n° 6).
- **L3 (intérêt) :** la DGFiP sait qui sont les 110 (elle a produit les données du centile) ; les notaires savent (actes) ; le gouvernement défend la niche ; les familles bénéficient de l'anonymat — la traçabilité a trois opposants silencieux.
- **L4 (sémiotique) :** « pacte », « famille », « transmission » naturalisent le transfert ; « dernier centile » (CdC) est plus précis que « premier centile » (corpus) — même population (top 1 %), la CdC ordonne par taille croissante.
- **L5 (comparaison) :** avec le CIR (22-15, 22-42) : l'Annexe 12 du Sénat 808 a prouvé que la publication nominative est possible quand une commission d'enquête l'exige. Le Dutreil n'a pas d'équivalent d'annexe — parce qu'aucune commission ne l'a exigé (la question du Sénat 760 était l'imposition des hauts patrimoines, pas la divulgation des noms).
- **L6 (contexte) :** débats PLF 2026 (amendements commission des finances : allongement durée de détention) ; rapport CdC publié le jour de l'ouverture des débats budgétaires — noyé dans la séquence.

**Lecture concurrente** : les 110 sont des chefs d'entreprise légitimes qui transmettent leur outil de travail ; le secret protège leur sécurité ; le dispositif assure la pérennité du contrôle familial (effet documenté par l'IPP). La synthèse retenue : l'effet sur la pérennité du contrôle est réel mais ses effets économiques (investissement, emploi) ne sont pas observés — la dépense massive au profit d'un centile anonyme ne se justifie pas économiquement dans l'état des preuves, et la traçabilité est techniquement triviale (mention notariale).

## 5. FORENSIC REASONING (ICEBERG MAX)

**Émergé (chiffré, source primaire)** : dépense >5,5 Md€ 2024 (>3,3 Md€ 2023, 1,2 Md€ 2020/2021) ; actif éligible 20 Md€ 2024 ; 5 000-6 000 transmissions 2024 ; 110 donataires = 65 % ; 30 M€ moyen ; 1,8 M€ moyenne nationale ; commerce 44 % VA / 35 % emploi vs industrie 13 % transmissions ; ~8 % vs 34 % taux effectif ; 523 000 salariés / 45 Md€ VA par an ; effet contrôle familial documenté (10 % vs 18 % de changement de contrôle) ; aucun effet investissement (5,3 % → 4,5 %) ni emploi (~25 % de sortie à 9 ans, identique).

**Surface (chiffré, corroboration en cours)** : « très grosse opération sur chacune des années 2023 et 2024 » (CdC) — candidates nominatives à confirmer (Bolloré/Vivendi 2023 ~35 % ~1,5 Md€, chercheur en cours) ; le rapport complet CdC (PDF 20251118-Pacte Dutreil.pdf) non lu intégralement.

**Immergé (jamais publié)** : les noms des 110 ; le détail des opérations géantes 2023/2024 (montant exact, famille) ; la base de données Sénat « en cours de constitution » ; les déclarations 2022-C.

**ICEBERG LOAD :** 9 strates émergées confirmées (source primaire), 2 surface, 4 immergées. La signature : la statistique est exhaustive, la nomination est nulle — l'asymétrie est le fait.

## 6. PRISME DIALECTIQUE

- **Thèse (dominante) :** « Le pacte Dutreil protège l'entreprise familiale française de l'absorption étrangère : 523 000 salariés, 45 Md€ de VA, pérennité du contrôle familial (10 % de changement de contrôle vs 18 %), un des dispositifs les plus favorables d'Europe. »
- **Antithèse (critique) :** « Le Dutreil est une niche à 5,5 Md€ dont 65 % vont à 110 donataires anonymes, qui a doublé en 4 ans, qui profite au commerce plutôt qu'à l'industrie, sans effet documenté sur l'investissement ni l'emploi — et qui n'a jamais été évaluée de 2000 à 2025. »
- **Arbitrage par les preuves :** la thèse est confirmée pour un seul effet (pérennité du contrôle familial, IPP) ; l'antithèse est confirmée sur le coût (5,5 Md€), la concentration (65 %/110), le ciblage (commerce > industrie) et l'absence d'effets investissement/emploi (IPP). **La synthèse** : un dispositif à l'effet réel mais étroit (contrôle familial) et au coût massif et concentré — la justification économique est faible, la défense est politique (Lecornu), la traçabilité est refusée.

**Réfutation testée** : « la concentration est un artefact : 110 opérations géantes par an, pas une classe » — la CdC confirme les opérations géantes annuelles (2023/2024) mais la concentration à 65 % est un fait de structure (dernier centile, pas 110 opérations aléatoires) ; « le secret protège les chefs d'entreprise » — l'argument de sécurité est réel mais la mention notariale dans une base statistique (Sénat 760, recommandation n° 6) n'exige aucune publication nominative : la traçabilité et la discrétion sont compatibles. Les deux réfutations bornent le verdict.

## 7. CHRONOLOGIE

| Année | Événement | Source | Statut |
|-------|-----------|--------|--------|
| 2000 | Création du dispositif (allégement des transmissions) | CdC 18/11/2025 | ✦ |
| 01/08/2003 | Loi pour l'initiative économique « Dutreil » : élargissement (art. 787 B CGI) | CdC 18/11/2025 | ✦ |
| 2018-2024 | 3 000-4 000 transmissions/an (la fourchette 2 000-3 000 citée était sous-estimée) | CdC 18/11/2025 | ✦ |
| 2020-2021 | Dépense fiscale ~1,2 Md€/an | CdC 18/11/2025 | ✦ |
| 2023 | Actif éligible 12 Md€ ; dépense >3,3 Md€ ; « très grosse opération » | CdC 18/11/2025 | ✦ |
| 2024 | 5 000-6 000 transmissions ; actif 20 Md€ ; dépense >5,5 Md€ ; 110 donataires = 65 % (30 M€ moyen) ; « très grosse opération » | CdC 18/11/2025 | ✦ |
| 24/10/2025 | Le Monde consulte la synthèse du rapport ; Boursorama/AFP (5,5 Md€, recommandations) | Boursorama | ✦ |
| 18/11/2025 | Publication du rapport CdC ; Lecornu défend la niche le même jour (Le Monde) | CdC / Le Monde | ✦ |
| 25/11/2025 | Alternatives Économiques : citation « 110 donataires, 30 M€ » | AE | ✦ |
| 17/06/2026 | Sénat 760 (Husson/Raynal) : Dutreil = angle mort statistique ; recommandation n° 6 (mention notariale + base de données) ; 13 324 foyers IFI à IR nul | Sénat | ✦ |

## 8. DOMAINES (par axe)

| Axe | Question | Résultat clé | Faits | Statut |
|-----|----------|--------------|-------|--------|
| AXS-001 MÉCANISME | Comment fonctionne le Dutreil ? | Abattement 75 % (art. 787 B) ; taux effectif ~8 % vs 34 % droit commun ; instauré 2000, élargi 2003 | FCT-001 | SATURATED |
| AXS-002 VOLUME | Combien de transmissions, quel actif ? | 5 000-6 000 en 2024 (fourchette officielle sous-estimée) ; actif 20 Md€ 2024 ; 1,8 M€ moyen | FCT-002/003 | SATURATED |
| AXS-003 COÛT | Combien coûte le dispositif ? | >5,5 Md€ 2024 (1,2 Md€ 2020/2021) ; ~1/4 des DMTG encaissées ; opérations géantes 2023/2024 | FCT-004/005 | SATURATED |
| AXS-004 CONCENTRATION | Qui concentre ? | Dernier centile = 65 % ; 110 donataires ; 30 M€ moyen (citation CdC primaire) | FCT-006 | SATURATED |
| AXS-005 SECTEURS/EFFETS | Quels effets économiques ? | Commerce 44 % VA vs industrie 13 % des transmissions ; effet contrôle familial réel ; aucun effet investissement/emploi (IPP) | FCT-007/008 | SATURATED |
| AXS-006 RÉFORME | Quelle traçabilité possible ? | CdC : 2 axes (optimisation, progressivité) ; Sénat 760 : recommandation n° 6 (mention notariale + base de données) ; Lecornu défend | FCT-009 à 011 | SATURATED |
| AXS-007 NOMINATION | Voies légales de nomination ? | Aucune (pas de registre, BODACC/annonces légales ne couvrent pas, secret notarial) ; Challenges = recoupements indirects ; piste opérations géantes en cours | FCT-012 à 014 | ANALYSE (réserve ✧) |

## 9. RÉSEAU D'ACTEURS (+ CONTROL_MAP)

| Acteur | Rôle | Action documentée | Preuve | Responsabilité |
|--------|------|-------------------|--------|----------------|
| 110 donataires | Bénéficiaires | 65 % de la dépense, 30 M€ moyen | FCT-006 | Bénéfice ≠ intention |
| DGFiP | Détenteur des données | Données fiscales inédites fournies à la CdC ; noms jamais publiés | FCT-004/015 | ROLE (pouvait ne pas publier) |
| Cour des comptes | Contrôleur | Rapport 18/11/2025 complet + synthèse publiée | FCT-004 à 009 | ρ |
| IPP | Évaluateur | Partenariat : effets économiques (contrôle familial oui, investissement/emploi non) | FCT-008 | 🎓 |
| Sénat 760 (Husson/Raynal) | Législateur (contrôle) | Recommandation n° 6 : mention notariale + base de données | FCT-010 | ρ |
| Bercy / Lecornu | Décideur | Défend la niche (18/11/2025) | FCT-011 | DÉCISION (refus de réforme) |
| Notaires (CSN) | Rédacteurs des actes | Statistiques agrégées uniquement ; secret professionnel | FCT-012 | ROLE |
| Presse | Révélateur partiel | Le Monde, AE, Economie Matin, Boursorama : chiffres, pas de noms | FCT-011/014 | ρ (limité) |

**CONTROL_MAP** :

| Contrôleur | Mécanisme | Résultat | Gap |
|------------|-----------|----------|-----|
| CTRL-001 DGFiP | Données fiscales (centiles) | Concentration documentée (65 %/110) | Noms non publiés |
| CTRL-002 CdC | Rapport + synthèse publique | Coût 5,5 Md€, effets faibles | Rapport complet non lu intégralement (ce dossier) |
| CTRL-003 Sénat 760 | Rapport d'information | Recommandation n° 6 (traçabilité) | Base de données « en cours de constitution » non documentée |
| CTRL-004 Bercy | Défense de la niche | Amendements limités (durée de détention) | Pas de plafonnement ni progressivité |

## 10. CHAÎNES / PELOTE (causalité)

**CAU-001 : La dépense Dutreil explose parce que le nombre de transmissions et la taille des opérations augmentent — avec des opérations géantes annuelles.**
Étage 1 : fourchette officielle sous-estimée (2 000-3 000 vs 5 000-6 000 réels en 2024) (FCT-002). Étage 2 : actif éligible 12 → 20 Md€ (2023 → 2024) (FCT-003). Étage 3 : CdC : « la présence d'une très grosse opération sur chacune des années 2023 et 2024 » explique l'augmentation récente (FCT-004). Type : STRUCTUREL + ÉVÉNEMENTIEL. Confidence : high (source CdC).

**CAU-002 : L'anonymat des 110 n'est pas une impossibilité technique mais une option de droit.**
Étage 1 : aucun registre public des pactes ; déclarations 2022-C et actes couverts par le secret (FCT-012). Étage 2 : la CdC a obtenu les données DGFiP (FCT-015) ; le Sénat 808 a forcé l'Annexe 12 du CIR (hérité 22-15) ; le Sénat 760 propose la mention notariale (FCT-010). Étage 3 : personne n'a exigé la divulgation pour le Dutreil. Type : STRUCTUREL. Confidence : high.

**CAU-003 : La justification économique de la dépense est faible, la défense est politique.**
Étage 1 : IPP : aucun effet investissement ni emploi ; seul effet = pérennité du contrôle familial (FCT-008). Étage 2 : CdC : « effets économiques favorables attendus non observés » (FCT-009). Étage 3 : Lecornu défend la niche le jour de la publication (FCT-011). Type : POLITIQUE. Confidence : high sur les faits, la motivation (lobby notarial/patronal) n'est pas documentée.

**CAU-004 (rejetée) : « Les 110 sont des fraudeurs ».** Réfutée : aucun fait pénal documenté dans ce dossier ; la question est l'optimisation légale (le « family buy out » et le « pacte réputé acquis » que la CdC veut supprimer sont légaux). Le bénéfice n'implique pas l'intention.

## 11. CARTE DES PREUVES

### CLAIM_REGISTRY

| ID | Claim | Support | Contre-évidence | Statut |
|----|-------|---------|-----------------|--------|
| CLM-001 | « La citation 110/65 %/30 M€ est confirmée à la source primaire CdC » | Page ccomptes.fr (snapshot Wayback 18/11/2025) : « très concentrée sur le dernier centile, qui représente 65 % de son total : les 110 donataires concernés en 2024 ont bénéficié d'un avantage fiscal moyen de 30 M€ » | Le corpus 22-15 disait « 1er centile » (même population, terminologie corrigée) | SOUTENU (source primaire) |
| CLM-002 | « La dépense passe de 1,2 à >5,5 Md€ en 4 ans » | CdC : >3,3 Md€ 2023, >5,5 Md€ 2024, 1,2 Md€ 2020 et 2021 | Le corpus 22-15 mentionnait « 5,5 Md€ en 2024 » sans le 1,2 Md€ 2021 | SOUTENU (corrigé et précisé) |
| CLM-003 | « Le nombre réel de transmissions est 5 000-6 000 en 2024, pas 2 000-3 000 » | CdC : « la fourchette régulièrement citée de 2 000 à 3 000 donations par an était sous-estimée » | La fourchette officielle restait citée | SOUTENU (correction documentée) |
| CLM-004 | « La concentration est portée en partie par 1-2 opérations géantes par an » | CdC : « la présence d'une très grosse opération sur chacune des années 2023 et 2024 » | L'identification nominative des opérations reste à confirmer (FCT-014 ✧) | SOUTENU (fait CdC), PARTIELLEMENT RÉSOLU (nomination) |
| CLM-005 | « Aucune voie légale ne permet de nommer les 110 » | BODACC : pas de publication des mutations d'actions ; annonces légales : pas d'obligation ; aucun registre des pactes ; CSN : statistiques agrégées | La presse (Challenges, recoupements) et les opérations géantes offrent des portes indirectes | SOUTENU (constat d'absence structurel) |
| CLM-006 | « La traçabilité est techniquement triviale et politiquement refusée » | Sénat 760 recommandation n° 6 (mention notariale + base de données) vs défense Lecornu 18/11/2025 | La base de données Sénat est « en cours de constitution » (avancement inconnu) | SOUTENU (faisceau) |

### FACT_REGISTRY (16 faits)

| ID | Fait | Chiffre | Source | Statut |
|----|------|---------|--------|--------|
| FCT-001 | Dutreil : instauré 2000, élargi par la loi Dutreil du 01/08/2003 (art. 787 B CGI) ; abattement 75 % sous conditions de détention ; taux moyen d'imposition des transmissions ~8 % vs 34 % en droit commun | 75 % ; 8 % vs 34 % | SRC-01 CdC 18/11/2025 | ✦ |
| FCT-002 | Nombre de transmissions : 3 000-4 000/an depuis 2018 ; **5 000-6 000 en 2024** (la fourchette officielle 2 000-3 000 était sous-estimée) | 5 000-6 000 | SRC-01 | ✦ |
| FCT-003 | Actif éligible : **12 Md€ 2023, 20 Md€ 2024** ; montant moyen par donataire ~1,8 M€ | 12/20 Md€ ; 1,8 M€ | SRC-01 | ✦ |
| FCT-004 | Dépense fiscale : **>3,3 Md€ 2023, >5,5 Md€ 2024** (1,2 Md€ en 2020 et 2021) ; augmentation expliquée par le nombre de transmissions ET « la présence d'une très grosse opération sur chacune des années 2023 et 2024 » | 1,2 → >5,5 Md€ | SRC-01 | ✦ |
| FCT-005 | Dépense Dutreil 2024 ≈ **un quart** des 20,9 Md€ de droits de mutation encaissés (successions + donations, 2023 et 2024) | ~25 % | SRC-01 | ✦ |
| FCT-006 | LA CITATION : « Cette dépense fiscale est très concentrée sur le **dernier centile, qui représente 65 % de son total : les 110 donataires concernés en 2024 ont bénéficié d'un avantage fiscal moyen de 30 M€** » | 65 % ; 110 ; 30 M€ | SRC-01 (page CdC, snapshot 18/11/2025) | ✦ |
| FCT-007 | Secteurs : **commerce sur-représenté (44 % de la VA, 35 % de l'emploi)** ; industrie (cible prioritaire déclarée) : **13 % des transmissions**, 21 % de la VA, 23 % de l'emploi ; 523 000 salariés et 45 Md€ de VA par an en moyenne 2018-2024 | 44 % vs 13 % | SRC-01 | ✦ |
| FCT-008 | Effets économiques (IPP) : pérennité du contrôle familial réelle (10 % de changement de contrôle l'année de transmission, 27 % à 5 ans, 40 % à 10 ans vs 18/42/48 % sans Dutreil) ; **aucun effet significatif sur l'investissement** (5,3 % → 4,5 %) **ni l'emploi** (~25 % de sortie à 9 ans, identique aux deux groupes) | contrôle : oui ; invest/emploi : non | SRC-01/02 | ✦ |
| FCT-009 | Recommandations CdC — 2 axes : (1) supprimer les optimisations (biens non professionnels éligibles, « pacte réputé acquis », allongement de la détention, **inéligibilité du « family buy out »**) ; (2) réduire la dépense (revoir le taux d'exonération, **progressivité du barème**, réduire l'avantage aux secteurs réglementés — expert-comptables, pharmacies — et non exposés à la concurrence internationale) | 2 axes | SRC-01 | ✦ |
| FCT-010 | Sénat 760 (Husson/Raynal, 17/06/2026) : Dutreil = « angle mort statistique majeur » des successions ; **recommandation n° 6** : « Prévoir la mention systématique du recours à un pacte Dutreil dans les actes notariés, lesquels alimenteront la base de données en cours de constitution sur les successions » (citation exacte) ; 13 324 foyers IFI à IR nul ou négatif (données 2024) | Rec. n° 6 ; 13 324 | SRC-03 Sénat 760 | ✦ |
| FCT-011 | Refus politique : **Sébastien Lecornu défend la niche Dutreil** le 18/11/2025 (Le Monde), jour de la publication du rapport CdC ; amendements limités en commission des finances (allongement de la durée de détention) | 18/11/2025 | SRC-04 Le Monde | ✦ |
| FCT-012 | Aucune voie légale de nomination : BODACC ne publie pas les mutations d'actions ; annonces légales sans obligation pour les donations d'actions ; **aucun registre public des pactes Dutreil** (déclarations 2022-C et actes notariés confidentiels — secret fiscal/professionnel) ; CSN : statistiques agrégées uniquement ; Bpifrance : macro uniquement | 0 voie | SRC-08 (vérification par chercheur) | ✧ |
| FCT-013 | Challenges « Fortunes de France » : seule source publique de valorisation des holdings familiales (bilans RCS, décotes, comparables boursiers) — recoupements indirects, sans accès aux actes de donation | recoupements | SRC-09 Challenges | ✧ |
| FCT-014 | Piste nominative résiduelle : les « très grosses opérations » 2023/2024 (CdC) — candidate 2023 : transmission du contrôle de Vivendi à Cyrille Bolloré (annoncée 06/2023, ~35 % du capital, ordre de grandeur ~1,5 Md€) ; mention explicite du Dutreil par la presse non confirmée à date | ~1,5 Md€ (ordre) | SRC-10 presse (chercheur en cours) | ✧ |
| FCT-015 | Méthodologie CdC : données fiscales inédites de la DGFiP, « jamais exploitées » + partenariat de recherche IPP (comparaison 2010-2018) | DGFiP+IPP | SRC-01 | ✦ |
| FCT-016 | Rapport CdC complet disponible : PDF « 20251118-Pacte Dutreil.pdf » + synthèse « 20251118-Synthese-Pacte Dutreil.pdf » + réponse ministérielle « 20251118-reponse-Pacte Dutreil.pdf » (ccomptes.fr) | 3 PDF | SRC-01 | ✦ |

### CONTRADICTION_LEDGER

| ID | Contradiction | Résolution | Statut |
|----|---------------|------------|--------|
| CONTR-001 | Corpus 22-15 : « 1er centile » vs CdC : « dernier centile » | Même population (top 1 %) ; la CdC ordonne par taille croissante — formulation corrigée (FCT-006) | RÉSOLUE (terminologie) |
| CONTR-002 | « 5,5 Md€ en 2024 » (corpus) vs « >5,5 Md€ » + « >3,3 Md€ 2023 » + « 1,2 Md€ 2020 ET 2021 » (CdC) | Le corpus simplifiait ; la CdC précise la trajectoire complète — dossier corrigé | RÉSOLUE (précision) |
| CONTR-003 | « Le Dutreil sauve les PME industrielles » (récit officiel) vs « commerce 44 % de la VA, industrie 13 % des transmissions » (CdC) | Le ciblage affiché (industrie) ne correspond pas au ciblage réel (commerce/distribution) | DOCUMENTÉE (Ω=9) |
| CONTR-004 | « Le secret protège les bénéficiaires » vs « la traçabilité est techniquement triviale » | La mention notariale statistique (Sénat 760 rec. n° 6) est compatible avec la discrétion : pas de publication nominative nécessaire | RÉSOLUE (borne le verdict) |
| CONTR-005 | « Le Dutreil favorise la transmission » vs « la dépense a doublé sans évaluation 2000-2025 » | Le nombre de transmissions et le coût ont augmenté en parallèle ; la CdC distingue effet (contrôle) et coût (massif, concentré) | DOCUMENTÉE |

### EDI

```
geo:0.75 lang:0.85 strat:0.80 owner:0.70 persp:0.85 temp:0.85
EDI_raw = .25×.75 + .20×.85 + .20×.80 + .15×.70 + .15×.85 + .05×.85 = 0.7975
Pénalité : MISSING_COUNTER (-.10) : perspective des 110 donataires (défense du dispositif, réalité de la transmission) absente.
EDI = 0.6975 (BROAD, sous la cible APEX 0.80, écart déclaré)
COV = 0.85 | IND = 0.70 | CC = 3/3
EDI* = .5×.6975 + .3×.85 + .2×.70 = 0.74
Perspectives : ⟐ 3 | ⟐̅ 1 | 🎓 2 (IPP, DGFiP-données) | 🌍 0 | 🔥 0
DIAGNOSTIC_NOT_TRUTH
```

### TRACE_MATRIX (extrait)

| FCT | QRY | SRC | URL (référence) | Statut |
|-----|-----|-----|-----------------|--------|
| FCT-001 à 009, 015, 016 | QRY-001/002/003 | SRC-01 | ccomptes.fr/fr/publications/le-pacte-dutreil-un-dispositif-fiscal-en-forte-croissance-mieux-cibler (lu via snapshot Wayback 20251118102524, jour de publication) | ✦ |
| FCT-008 | QRY-003 | SRC-02 | ipp.eu (partenariat CdC-IPP, effet contrôle familial, absence d'effet invest/emploi) | ✦ |
| FCT-010 | QRY-004 | SRC-03 | senat.fr/rap/r25-760/r25-7601.html (r25-7600.html) — recommandation n° 6 | ✦ |
| FCT-011 | QRY-004 | SRC-04 | lemonde.fr 18/11/2025 « Budget : Sébastien Lecornu défend la niche Dutreil... » | ✦ |
| FCT-012 | QRY-005 | SRC-08 (vérification par chercheur) | bodacc.fr ; Légifrance (annonces légales) ; notaires.fr/CSN ; declarations 2022-C (BOFiP) | ✧ |
| FCT-013 | QRY-005 | SRC-09 | challenges.fr « Fortunes de France » (méthodologie) | ✧ |
| FCT-014 | QRY-006 | SRC-10 | presse économique (Les Echos/L'Agefi/Le Monde) — Bolloré/Vivendi — en cours | ✧ |

## 12. CARTE DIALECTIQUE (scénarios + responsabilité)

| Scénario | Hypothèse | Support | Contre | Lecture |
|----------|-----------|--------|--------|---------|
| S1 « Rente du dernier centile » | Les 110 captent 65 % sans contrepartie économique | 30 M€ moyen ; aucun effet invest/emploi (IPP) ; opérations géantes annuelles | Effet de pérennité du contrôle familial documenté | Retenue (faisceau) |
| S2 « Outil de transmission » | Le Dutreil remplit sa mission (transmettre) | 5 000-6 000 transmissions/an ; 523 000 salariés ; contrôle préservé | Coût ×4,6 en 4 ans ; ciblage commerce > industrie | Retenue (partiel) |
| S3 « Anonymat de droit » | Les noms sont secrets par choix, pas par nécessité | Aucun registre ; Sénat 760 rec. n° 6 (traçabilité triviale) ; analogie Annexe 12 CIR | Secret fiscal/professionnel légitime | Retenue (verdict) |

**IMPACT_MAP** :

| Acteur | Gain | Perte |
|--------|------|-------|
| 110 donataires | ~30 M€ d'avantage moyen chacun (65 % de >5,5 Md€) | — |
| 4 900-5 900 autres donataires | 35 % de la dépense (1,8 M€ moyen) | — |
| État | Pérennité supposée des entreprises | >5,5 Md€/an (vs 20,9 Md€ DMTG) |
| Contribuables | — | Niche concentrée sans effets économiques documentés |
| Commerce/distribution | 44 % de la VA transmise | — |
| Industrie (cible affichée) | — | 13 % des transmissions seulement |

**RESPONSIBILITY_MAP** : aucun auteur d'intention n'est établi (BENEFIT != INTENT). Rôles : législateur (2000/2003, abattement 75 % sans progressivité), DGFiP (noms jamais publiés), gouvernement (défense de la niche 18/11/2025), Sénat 760 (proposition de traçabilité), CdC/IPP (évaluation). Responsabilité systémique : une dépense en explosion ultra-concentrée a prospéré 25 ans sans évaluation ni traçabilité ; la traçabilité est proposée (Sénat) et non engagée.

## 13. PÉRIMÈTRE & LIMITES

**Inclusions** : nomination des 110 (voies légales) ; mécanisme et coût (CdC 18/11/2025, source primaire) ; concentration (citation exacte) ; secteurs ; effets économiques (IPP) ; réforme (CdC, Sénat 760) ; blocage politique (Lecornu). Période 2000-2026.

**Exclusions explicites** : les noms eux-mêmes (secret) ; la fraude (aucun fait pénal) ; le détail des actes notariés ; le rapport CdC complet en PDF (seule la synthèse officielle publiée en page a été lue intégralement).

**GAP déclarés** :
- GAP-001 (ACCESS) : noms des 110 — secret fiscal/notarial, aucun registre public.
- GAP-002 (VERIFY) : **RÉSOLU EN NON TRANCHÉ 23:14** (dossier 2026-08-09_23-14_resolution-gap002-bollore-operation2024) : la mention Dutreil Bolloré est NI CONFIRMÉE NI INFIRMÉE — constat d'absence multi-moteurs (3 requêtes Google News RSS à 0 résultat ; aucune source presse ne nomme les opérations 2023/2024) ; éligibilité établie (cotées 10 %/20 %), gain ~338 M€ chiffré (⁂) ; verrou secret fiscal ; restent GAP-002b (Blast/Oxfam non lus) et GAP-003 (base Sénat).
- GAP-003 (ACCESS) : **RÉSOLU 23:25** (dossier 2026-08-09_23-25_base-donnees-successions-eenregistrement) : la base = plateforme e-enregistrement DGFiP (S2 2026) + module statistique NON FINANCÉ (CPO, dizaines de M€) ; dernière étude DMTG 2010 ; numérisation complète 2029 (rec. n° 3) ; assurance-vie ≥ 2033 ; écart 35-40 % patrimoine déclaré vs macro ; interrogeable : NON par le public ; traçabilité Dutreil suspendue au financement ; reste GAP-003b (corps du rapport).
- GAP-004 (CORPUS) : perspective des 110 donataires et des notaires absente (MISSING_COUNTER, EDI).

## 14. ÉTAT DES CONNAISSANCES

- **CONNU (✦)** : citation primaire CdC (110/65 %/30 M€) ; trajectoire 1,2 → >5,5 Md€ ; 5 000-6 000 transmissions 2024 ; actif 20 Md€ ; commerce 44 % VA vs industrie 13 % ; effets IPP (contrôle oui, invest/emploi non) ; recommandations CdC ; Sénat 760 rec. n° 6 ; défense Lecornu ; absence de registre public.
- **PROBABLE (✧)** : les opérations géantes 2023/2024 sont nominables par la presse (candidate Bolloré) ; Challenges fournit les valorisations de holdings.
- **HYPOTHÈSE (⁂)** : la majeure partie des 65 % est portée par un petit nombre d'opérations géantes annuelles.
- **CONTESTÉ (⊗)** : la justification économique du dispositif (effet contrôle vs coût).
- **INCONNU (⁅)** : noms des 110 ; détail des opérations 2023/2024 ; base de données Sénat ; part exacte des opérations géantes dans les 65 %.
- **RÉFUTÉ (❧)** : « les 110 sont des fraudeurs » ; « le secret est une impossibilité technique » (l'Annexe 12 du CIR et la rec. n° 6 du Sénat 760 démontrent le contraire).

## 15. SUSPICION / VÉRIFICATION

**AUDIT DU LEAD** : input UPDATE (nomination des 110 par voies publiques). Le verdict d'objet est distinct du verdict de lead : « peut-on nommer les 110 ? » reçoit une réponse honnête en deux volets — non par voie légale directe (constat d'absence structurel), oui partiellement par la caractérisation (opérations géantes annuelles, secteurs, palmarès).

**Vérifications contradictoires exécutées** : CONTR-001 à 005 (terminologie centile, trajectoire de coût, ciblage secteurs, traçabilité, évaluation). Citation primaire re-lue à la source (ccomptes.fr via snapshot Wayback du jour de publication — vérification d'authenticité : URL + timestamp + HTTP 200). Sénat 760 relu (recommandation n° 6, texte exact). Le Monde/Boursorama/Economie Matin/AE recoupés.

**Verdict final : STRUCTURELLEMENT INNOMMABLE PAR VOIE LÉGALE, MAIS CARACTÉRISABLE ET TRAÇABLE À CONDITION DE RÉFORME.** Les noms des 110 sont protégés par le secret fiscal et notarial — une option de droit, pas un mur technique : la CdC a prouvé que les données existent (elle les a utilisées), le Sénat 760 a proposé la traçabilité (mention notariale), le gouvernement a choisi de défendre la niche. **Le résultat le plus actionnable : les « très grosses opérations » annuelles nommées par la presse économique (2023 : candidate Bolloré/Vivendi) sont la seule porte nominative actuelle, et la recommandation n° 6 du Sénat 760 est la clé de la levée du secret à terme.**

---

# ANNEXE A. SOURCES

| SRC-ID | Source | Locator / date | Rôle | URL |
|--------|--------|----------------|------|-----|
| SRC-01 | Cour des comptes, « Le Pacte Dutreil : un dispositif fiscal en forte croissance à mieux cibler » (page officielle de publication + synthèse) | 18/11/2025 (snapshot Wayback 20251118102524, HTTP 200, page lue intégralement) | ◈ | https://www.ccomptes.fr/fr/publications/le-pacte-dutreil-un-dispositif-fiscal-en-forte-croissance-mieux-cibler |
| SRC-01b | CdC : PDF du rapport complet | 18/11/2025 | ◈ | https://www.ccomptes.fr/sites/default/files/2025-11/20251118-Pacte%20Dutreil.pdf |
| SRC-01c | CdC : synthèse officielle | 18/11/2025 | ◈ | https://www.ccomptes.fr/sites/default/files/2025-11/20251118-Synthese-Pacte%20Dutreil.pdf |
| SRC-02 | IPP (partenariat CdC) : comparaison 2010-2018, effets économiques Dutreil | 18/11/2025 | 🎓 | (via SRC-01, résultats cités dans la page CdC) |
| SRC-03 | Sénat, rapport d'information n° 760 (Husson/Raynal), « l'imposition des hauts patrimoines » | 17/06/2026 (relu : recommandation n° 6) | ◈ | https://www.senat.fr/rap/r25-760/r25-7601.html |
| SRC-04 | Le Monde, « Budget : Sébastien Lecornu défend la niche Dutreil malgré les critiques de la Cour des comptes » | 18/11/2025 | ◈ | https://www.lemonde.fr/politique/article/2025/11/18/budget-sebastien-lecornu-defend-la-niche-dutreil-malgre-les-critiques-de-la-cour-des-comptes_6653842_823448.html |
| SRC-05 | Boursorama/AFP, « la Cour des comptes étrille le pacte Dutreil, 5,5 milliards en 2024 » (lu intégralement) | 24/10/2025 | ◈ | https://www.boursorama.com/actualite-economique/actualites/transmission-familiale-d-entreprise-la-cour-des-comptes-etrille-le-pacte-dutreil-qui-a-coute-5-5-milliards-d-euros-aux-caisses-publiques-en-2024-69c21d7107f8082e11185a7ef4fbdd87 |
| SRC-06 | Alternatives Économiques, « Le pacte Dutreil, une niche fiscale qui profite aux héritiers et coûte cher » (citation exacte 110/30 M€) | 25/11/2025 | ◈ | https://www.alternatives-economiques.fr/le-pacte-dutreil-une-niche-fiscale-qui-profite-aux-heritiers-et-coute-cher-aux-finances-publiques |
| SRC-07 | Economie Matin, « Pacte Dutreil : l'offensive de la Cour des comptes » (110 donataires 65 %, 523 000 salariés, 45 Md€ VA — lu) | ~11/2025 | ◉ | https://www.economiematin.fr/pacte-dutreil-offensive-cour-des-comptes |
| SRC-08 | BODACC (registre du commerce) ; DILA/Légifrance (annonces légales) ; CSN/notaires.fr ; BOFiP (déclarations 2022-C/2022-T) | consultés 09/08/2026 | ◈ | https://www.bodacc.fr ; https://www.notaires.fr |
| SRC-09 | Challenges « Fortunes de France » (méthodologie de valorisation des holdings) | annuel | ◉ | https://www.challenges.fr/fortunes |
| SRC-10 | Presse économique — transmission Bolloré/Vivendi 2023 (candidate opération géante 2023) | 06/2023-2024 | ◉ (chercheur en cours) | Les Echos / L'Agefi / Le Monde |

# ANNEXE B. REQUEST_LOG

```
ENGINE:2.8 | MANIFEST:FINAL | RUN_ID:20260809-2256-dutreil-110-donataires | PARENT_RUN_ID:20260809-2215 | AS_OF:2026-08-09 | INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:NONE
CHECKPOINT_SEQ:0 | LAST_COMPLETED:18b | NEXT_ACTION:NONE | RESUME_COUNT:0
Investigation:dutreil-110-donataires | complexity:13→APEX | route overrides:NONE | scope:2000-2026, France
modules:KERNEL|SYMBOLS|PATTERNS|THREATS|GATES|REQUEST_LOG|EPISTEMIC|TEMPLATE|INVESTIGATION
degraded:NONE | query target/actual: 7/7 (3 agents + 4 basher/lectures directes)
COUNT: ◈10 ◉2 | unique evidence objects:16 | upstream families:6
LEADS:terminal 1/1 | AXES:terminal 7/7 | N/A:none
FAILURES:1 (Bolloré : mention Dutreil non confirmée — GAP-002) | FALLBACKS:2 (jina ccomptes bloqué → snapshot Wayback du jour de publication ; page Annexe non concernée)
unresolved gaps:GAP-001..GAP-004 (ACCESS/VERIFY/ACCESS/CORPUS)
```

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL/INPUT_REF |
|---:|---|---|---|---|---|
| 1 | SYS | @MNEMO_Q « Dutreil 110 donataires centile » + lecture parent 22-15 | Constat hérité : 5,5 Md€ 2024, 1er centile 65 % (~30 M€), FCT-009 à 012 | 22-15 | investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_beneficiaires-niches-cessions/ |
| 2 | ◈ | QRY-001/002/003 (AXS-001 à 005) : rapport CdC Dutreil — citation, coût, volume, secteurs, effets | FOUND : citation primaire « dernier centile 65 %, 110 donataires, 30 M€ » ; 1,2 → >5,5 Md€ ; 5 000-6 000 transmissions ; 20 Md€ ; commerce 44 % VA ; effets IPP ; opérations géantes 2023/2024 ; 2 axes de réforme | SRC-01 | ccomptes.fr (via snapshot Wayback 20251118102524, page lue) |
| 3 | ◈ | QRY-004 (AXS-006) : Sénat 760 + réponse politique | FOUND : rec. n° 6 (mention notariale + base de données successions) ; 13 324 foyers IFI ; Lecornu défend la niche 18/11/2025 | SRC-03/04 | senat.fr/rap/r25-760 ; lemonde.fr 18/11/2025 |
| 4 | ◈ | QRY-005 (AXS-007) : voies légales de nomination | FOUND : aucune (BODACC, annonces légales, registre pactes, CSN, Bpifrance) ; Challenges = recoupements | SRC-08/09 | bodacc.fr ; notaires.fr ; challenges.fr |
| 5 | ◉ | QRY-006 (AXS-007 bis) : opérations géantes nominables | PARTIEL : candidate Bolloré/Vivendi 2023 (~35 %, ~1,5 Md€) ; mention Dutreil non confirmée | SRC-10 | presse économique (chercheur en cours) |
| 6 | SYS | Vérification : citation primaire relue à la source (snapshot Wayback jour de publication) ; recoupement Le Monde/Boursorama/AE/Economie Matin | CONTR-001 à 005 résolus ; corrections corpus 22-15 (dernier centile, 1,2 Md€ 2020 ET 2021, >5,5) | SRC-01/05/06/07 | — |
| 7 | SYS | @MNEMO_S + FACT_WRITEBACK | PENDING_AT_SERIALIZATION | — | — |
| 8 | SYS | STATE:FINAL write | PENDING_AT_SERIALIZATION (ce fichier) | — | investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_dutreil-110-donataires/2026-08-09_22-56_dutreil-110-donataires_INVESTIGATION.md |

# ANNEXE C. GATES (G0-G10)

| Gate | Vérification | Résultat |
|------|--------------|----------|
| G0 | Modules chargés ; manifest FINAL ; 15 symboles scorés, aucun ✗ | ✅ |
| G1 | LEAD vs OBJECT distincts ; 7 axes terminaux ; périmètre explicite | ✅ |
| G2 | 6 CLM avec support/counter/gap | ✅ |
| G3 | FACT_REGISTRY 16 faits, statuts canoniques | ✅ |
| G4 | Chaque ✦ → SRC-ID + URL ; ✧ pour corroboration restante (FCT-013/014) | ✅ |
| G5 | CAU-001 à 004 typés, arrêt à l'évidence, CAU-004 rejetée (pas de fraude) | ✅ |
| G6 | CONTROL_MAP + RESPONSIBILITY_MAP ; rôles ≠ responsabilités | ✅ |
| G7 | CONTR-001 à 005 documentés et résolus | ✅ |
| G8 | TRACE_MATRIX ; QRY-001 à 006 tracés ; IDs résolus | ✅ |
| G9 | Manifest FINAL, NEXT_ACTION NONE, aucun PENDING requis | ✅ |
| G10 | Un seul chemin ; une seule write FINAL ; PENDING_AT_SERIALIZATION honnête | ✅ |

**GAP_SEVERITY** : edi_gap = (0.80-0.6975)/0.80 = 0.128 ; query_gap = N/A ; coverage_gap = 0. GAP_SEVERITY = 0.128 × 1.00 = 0.13 < 0.20 → procéder avec divulgation (gaps GAP-001 à GAP-004 déclarés).

---

*TL;DR : SUJET : « les 110 donataires du Dutreil » — tentative de nomination du dernier centile (65 % de la dépense, 30 M€ de moyenne) par les voies publiques. OBJET : la citation est confirmée à la source primaire (CdC, page de publication lue via snapshot Wayback du 18/11/2025 : « très concentrée sur le dernier centile, qui représente 65 % de son total : les 110 donataires concernés en 2024 ont bénéficié d'un avantage fiscal moyen de 30 M€ ») ; la dépense est passée de 1,2 Md€ (2020 et 2021) à >3,3 Md€ (2023) puis >5,5 Md€ (2024), le nombre de transmissions est 5 000-6 000 en 2024 (fourchette officielle sous-estimée), l'actif éligible 20 Md€ ; la concentration est portée en partie par « une très grosse opération sur chacune des années 2023 et 2024 » — seule piste nominative (candidate 2023 : Bolloré/Vivendi, ~1,5 Md€, non confirmée). Aucune voie légale ne nomme les 110 (aucun registre public des pactes, BODACC et annonces légales ne couvrent pas les donations d'actions, secret notarial) ; le Sénat 760 (17/06/2026) propose la traçabilité (rec. n° 6 : mention notariale + base de données), le gouvernement (Lecornu, 18/11/2025) défend la niche. VERDICT : STRUCTURELLEMENT INNOMMABLE PAR VOIE LÉGALE, MAIS CARACTÉRISABLE ET TRAÇABLE À CONDITION DE RÉFORME — l'anonymat est une option de droit, pas un mur technique. SOURCE : UPDATE du 22-15 (GAP-007). MANIPULATION : Ξ=9, €=9, ↕=9, Ω=9, Κ=9. LIMITE : GAP-001 à GAP-004 (noms secrets, opérations géantes à confirmer, base de données Sénat, perspective des 110 absente). CORRECTIONS corpus : « dernier centile » (pas « premier »), « 1,2 Md€ 2020 ET 2021 », « >5,5 Md€ ».*
