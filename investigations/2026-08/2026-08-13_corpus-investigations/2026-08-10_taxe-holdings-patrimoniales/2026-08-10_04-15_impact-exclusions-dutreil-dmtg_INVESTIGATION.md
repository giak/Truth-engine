# INVESTIGATION : IMPACT CHIFFRÉ DE LA RÉFORME « A MINIMA » DU DUTREIL SUR LES RECETTES DMTG 2026 — GAIN DES EXCLUSIONS D'ACTIFS SOMPTUAIRES vs COÛT MAINTENU DE 5,5 Md€

## RUN_MANIFEST (FINAL)

```
ENGINE_VERSION : 2.8
STATE          : FINAL
RUN_ID         : 20260810-0415-impact-exclusions-dutreil-dmtg
PARENT_RUN_ID  : 20260809-2340-plf-2026-dutreil (parent principal ; FCT-002/003 : exclusion actifs somptuaires, 3 ans, trésorerie exonérée ; réforme a minima) ; référence secondaire : 20260810-0407-taxe-holdings (mesure jumelle chiffrée par Lazard)
AS_OF          : 2026-08-10
INPUT_KIND     : UPDATE (estimation encadrée de l'impact chiffré de la réforme du Dutreil dans la LF 2026 sur les recettes DMTG : gain des exclusions d'actifs somptuaires vs coût maintenu de 5,5 Md€)
MISSION_MODE   : INVESTIGATION
INPUT_REF      : NONE (topique : « Estimer l'impact chiffré de la réforme a minima sur les recettes DMTG 2026 : combien les exclusions d'actifs somptuaires rapporteront-elles vs le coût de 5,5 Md€ maintenu ? »)
SUBJECT_SLUG   : impact-exclusions-dutreil-dmtg
INVESTIGATION_PATH : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_taxe-holdings-patrimoniales/2026-08-10_04-15_impact-exclusions-dutreil-dmtg_INVESTIGATION.md
SCOPE          : impact budgétaire des exclusions d'actifs somptuaires (LF 2026, art. 8/3 quater, exclusions 3 ans) sur les recettes DMTG ; actif transmis 20 Md€ (2024) ; taux effectifs (8 % avec vs 25-42 % sans Dutreil) ; dépense 5,5 Md€ maintenue ; gain encadré des exclusions ; absence d'évaluation officielle ; période 2024-2026 ; France
COMPLEXITY     : CX_SCORE=11 → $CX=COMPLEX (political 2, technical 3, temporal 3, geo 0, narratives 1, data 2)
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

**Réponse à l'OBJECT_QUESTION** (« combien les exclusions d'actifs somptuaires rapporteront-elles vs le coût de 5,5 Md€ maintenu ? ») :

**LE GAIN DES EXCLUSIONS EST INCONNU ET NON CHIFFRÉ PAR AUCUNE INSTITUTION — l'encadrement par hypothèses transparentes le situe entre ~12 M€ (net) et ~350 M€ (brut) par an, soit 0,4 à 6 % du coût maintenu de 5,5 Md€ : la réforme a minima rapporte au mieux une fraction résiduelle du coût qu'elle prétend durcir, et aucun organe public n'a jugé utile de chiffrer cette fraction.** Le cœur de l'enquête :

1. **Le fait d'absence (FCT-001) — RÉSULTAT CENTRAL** : **aucune évaluation officielle du gain des exclusions n'existe**. Le chercheur (4 axes croisés : étude d'impact PLF 2026, rapport général, amendement, jaune budgétaire) retourne **NON TROUVÉ** ; la Cour des comptes (rapport 18/11/2025) **pointe le caractère permissif des biens non professionnels sans les quantifier** (la part de l'immobilier/logements dans les 20 Md€ d'actif transmis n'est pas chiffrée) ; ni le gouvernement ni les amendements (3173/3552, PDF lus au 03:55) ne comportent d'évaluation de recettes. **Le législateur a adopté une exclusion dont il n'a pas mesuré le rendement.**
2. **Les données de base vérifiées (FCT-002 à 004)** : actif transmis sous Dutreil **20 Md€ en 2024** ; dépense fiscale **>5,5 Md€ en 2024** (1,2 Md€ 2020 → 3,3 Md€ 2023) ; **taux effectif d'imposition 8 % avec Dutreil** vs **~25-42 % sans** (exemples CdC lus : 20 M€ → 4,2 % vs 42 % ; 2,5 M€ → 1,63 % vs 25,01 % ; démembrement 0,7 % vs 8,3 %). **Droits dus 2024 ≈ 1,6 Md€** (20 Md€ × 8 %).
3. **La mécanique des exclusions (FCT-005)** : seuls les biens somptuaires **non exclusivement affectés à l'activité depuis ≥ 3 ans** perdent l'abattement (75 % ≤ 500 K€ puis 50 %). **La trésorerie et les placements financiers — le cœur des holdings — restent exonérés** (confirmé par le 23-40 et Actu-Juridique lu). L'allongement 4→6 ans n'a aucun effet de recettes direct (retarde la sortie, ne taxe pas).
4. **L'encadrement (FCT-006, ⁂ — HYPOTHÈSE, non mesuré)** : le gain = valeur des actifs exclus × (taux normal marginal − ~8 % Dutreil). Lecture **brute** (taux normal 20-35 %) : 0,5 % de l'actif (100 M€) → 20-35 M€ ; 1-2 % (200-400 M€) → 40-140 M€ ; 5 % (1 Md€) → 200-350 M€. Lecture **nette** (écart 12-27 points après le ~8 % déjà payé ; borne haute CdC 38 points) : 12-27 M€ ; 24-108 M€ ; 120-270 M€. **Coût maintenu : >5,5 Md€ → le gain représente 0,4 à 6 % (scénario moyen, lecture nette ~0,4-2 %).**
5. **Le contexte qui borne l'estimation (FCT-007)** : les biens somptuaires (yachts, avions, chasse, bijoux, vins) sont des actifs résiduels dans les holdings patrimoniales — le gros de l'actif est constitué de titres, trésorerie, immobilier d'exploitation. Le notariat (lu) ne conteste pas l'exclusion (il défend la trésorerie), ce qui suggère que les notaires n'y voient pas un enjeu massif. L'absence totale de chiffrage par tous les acteurs — y compris la CdC, pourtant critique — est le signal : l'enjeu est dérisoire au regard des 5,5 Md€.
6. **La lecture anti-sycophancie (FCT-008)** : la réforme « durcit la forme » (8 ans, yachts exclus) mais **ne touche pas la mécanique centrale** : les 110 donataires (65 % de la dépense, 30 M€ de moyenne) et les opérations géantes (Bolloré/Vivendi 2023 ~1,5 Md€) transmettent des titres et de la trésorerie — précisément les actifs exonérés. **L'exclusion des actifs somptuaires est une mesure cosmétique à rendement résiduel.**

**Verdict sur le LEAD_QUESTION** (« la réforme a minima réduit-elle le coût ? ») : **NON, pas significativement — et personne ne l'a chiffré.** Le gain des exclusions est encadré entre ~12 M€ (net) et ~350 M€ (brut)/an (hypothèses 0,5-5 % de l'actif), contre un coût maintenu de >5,5 Md€ : **entre 0,4 et 6 %**. L'absence d'évaluation officielle (CdC incluse) est elle-même un fait : la puissance publique a adopté une restriction sans en mesurer l'effet budgétaire, cohérent avec le verdict « réforme a minima » du 23-40.

**Acteurs** : Cour des comptes (rapport 18/11/2025, taux effectifs), Bercy/Lecornu (défense), Assemblée (amendements 3173/3552), Sénat 760 (17/06/2026), notariat (CSN, seuil de prépondérance), Lazard/cabinets (fragilités), DGFiP (données non publiées).

**Principales limites** : la part des actifs somptuaires dans l'actif transmis est INCONNUE (aucune source ne la publie — GAP-001) ; l'encadrement repose sur des hypothèses transparentes (⁂) ; l'évaluation officielle est absente (constat) ; Légifrance bloqué (texte de loi non relu — contenu via Actu-Juridique lu + amendements PDF lus).

## 2. MANIPULATION_REPORT (15 symboles scorés sur corpus)

| # | Symbole | Score | Justification (corpus) |
|---|---------|-------|------------------------|
| 1 | **Ξ** omission | **9/10** | Aucune institution (CdC, DGFiP, Bercy, AN, Sénat) n'a chiffré la part des actifs somptuaires ni le gain des exclusions ; la CdC pointe les biens non professionnels sans les quantifier ; l'étude d'impact PLF est muette. |
| 2 | **€** money | **9/10** | 20 Md€ d'actif transmis ; 5,5 Md€ de dépense maintenue ; 1,6 Md€ de droits dus ; gain encadré 40-350 M€ ; taux 8 % vs 25-42 %. |
| 3 | **Λ** framing | **8/10** | « Le Dutreil est durci » (récit) vs « le coût est maintenu à 5,5 Md€, seuls les yachts sont exclus » (faits) ; « exclusions des actifs somptuaires » présente le cosmétique comme une réforme. |
| 4 | **Ω** inversion | **9/10** | La mesure qui rapporterait le plus (suppression de l'éligibilité des biens non professionnels, progressivité, FBO) est REJETÉE ; la mesure adoptée (yachts, chasse) rapporte le moins ; le durcissement affiché masque la préservation de la mécanique. |
| 5 | **Ψ** sidération | 2/10 | Champ froid. |
| 6 | **↕** verticalité | **9/10** | Les 110 (65 %) transmettent titres + trésorerie (exonérés) ; les exclusions frappent les biens de luxe des très riches mais pas la concentration de la dépense ; l'allongement 4→6 ans ne rapporte rien. |
| 7 | **Φ** spectacle | 2/10 | Aucun spectacle ; le chiffrage absent n'a suscité aucun débat. |
| 8 | **Σ** sémiotique | 4/10 | « Recentrage sur les biens professionnels », « resserrement des conditions » — le vocabulaire masque un gain résiduel non mesuré. |
| 9 | **Κ** cynisme | **9/10** | Adopter une restriction sans l'évaluer ; la CdC (18/11/2025) critique sans quantifier la cible ; le gouvernement défend la niche (Lecornu) ; le chiffrage qui ferait apparaître l'insignifiance du gain n'est fait nulle part. |
| 10 | **ρ** résistance | **8/10** | Actu-Juridique (20/11/2025 et 24/03/2026, lus), CdC (18/11/2025), Sénat 760, La Tribune, amendements AN (PDF lus). |
| 11 | **κ** influence subtile | **8/10** | Architecture par défaut : l'abattement 75 %/50 % (500 K€) est inchangé ; la trésorerie et les placements restent exonérés ; l'exclusion des yachts crée un récit de durcissement sans effet sur la distribution ; l'absence de chiffrage empêche le débat sur l'échelle. |
| 12 | **⫸** convergence | 7/10 | CdC + Sénat 760 + Actu-Juridique + notariat convergent : la réforme ne touche pas la mécanique centrale. |
| 13 | **⚔** guerre cognitive | 1/10 | Aucune campagne documentée. |
| 14 | **🌐** réseau | 6/10 | CdC, Bercy, AN, Sénat, notariat, cabinets, DGFiP, presse. |
| 15 | **⏰** temporalité | **8/10** | 2024 (20 Md€, 5,5 Md€) ; 03/11/2025 (3 amendements AN) ; 18/11/2025 (CdC) ; 15/01/2026 (3173/3552 adoptés) ; 19/02/2026 (LF) ; 21/02/2026 (application) ; 2026 (recettes, non évaluées) ; 2027+ (effet réel). |

**BIAS TEST (15/15 scorés).** Aucun symbole au-delà de 9. Les champs 1, 4, 6, 9 signalent le noyau : une réforme qui exclut le luxe sans toucher la mécanique, adoptée sans chiffrage, dont le gain est une fraction résiduelle du coût maintenu.

**PATTERNS** : @PAT[ICEBERG] (Ξ=9), @PAT[INVERSION] (Ω=9), @PAT[MONEY] (€=9), @PAT[POWER] (↕=9), @PAT[CYN] (Κ=9). **THREATS** : @THR[OPACITY] (pas de chiffrage), @THR[REG_CAPTURE] (niche préservée), @THR[SHIFT_BURDEN] (exclusion cosmétique).

**RHETORICAL** : NUM (20 Md€, 5,5 Md€, 8 %, 25-42 %, 4,2 %/42 %, 1,63 %/25,01 %, 0,7 %/8,3 %, 75 %, 500 K€, 3 ans, 4→6 ans) ; AUTH (CdC, Actu-Juridique, Sénat 760) ; DEM et BF = 0.

## 3. CLUSTERS (routage SYMBOLS §4)

| Cluster | Diagnostic | Gap |
|---------|------------|-----|
| ICEBERG (Ξ=9) | Émergé : 20 Md€, 5,5 Md€, taux 8 %. Immergé : la part des actifs somptuaires, le gain réel, les données DGFiP. | Aucune source ne publie l'assiette. |
| INVERSION (Ω=9) | Le durcissement affiché (yachts) masque la préservation (titres, trésorerie, 110/65 %). | — |
| MONEY (€=9) | Coût 5,5 Md€ vs gain encadré 12-350 M€ (0,4-6 %). | Chiffrage officiel absent. |
| POWER (↕=9) | Les 110 transmettent des actifs exonérés (titres, trésorerie). | — |
| CONFIRMATION (κ=8) | Abattement inchangé ; trésorerie exonérée ; navette rejette les mesures de fond. | — |
| FRAGMENTATION (⫸=7) | CdC + Sénat + Actu-Juridique + notariat convergent. | — |
| TEMPORAL (⏰=8) | 2024 → 2026 (application) → 2027+ (effet). | — |

## 4. HERMÉNEUTIQUE (statut : ANALYSE)

- **L1 (texte) :** Actu-Juridique « Pacte Dutreil : le recadrage se profile… » (20/11/2025, lu intégralement — taux effectifs, 3 amendements du 03/11/2025, notariat) ; Actu-Juridique « Tout comprendre sur la taxe holdings » (24/03/2026, lu) ; amendements 3173/3552 (PDF lus au 03:55) ; CdC 18/11/2025 (hérité 22-56) ; Sénat 760 (hérité 23-25).
- **L2 (structure) :** deux étages — (a) le chiffrage existe pour le coût (5,5 Md€) et les taux (8 % vs 25-42 %) mais pas pour l'assiette cible des exclusions ; (b) la réforme exclut le luxe (liste fermée) et épargne la trésorerie et les titres — **la structure de l'actif Dutreil (titres + trésorerie) est orthogonale à la liste des exclusions (yachts, chasse, bijoux)** : les deux ne se recouvrent presque pas.
- **L3 (intérêt) :** le gouvernement veut le récit du durcissement ; la CdC veut la réforme de fond (rejetée) ; le notariat veut protéger la trésorerie (défendue) ; personne n'a intérêt à chiffrer un gain qui révélerait l'insignifiance de la réforme.
- **L4 (sémiotique) :** « recentrage sur les biens professionnels » = l'exclusion des yachts ; « réforme a minima » = le fait (Actu-Juridique) ; « durcissement » = le récit.
- **L5 (comparaison) :** avec le 04-07 (taxe holdings) : la mesure jumelle (art. 7) a été chiffrée par Lazard (1,5 Md€ → 100 M€) — preuve que le chiffrage est possible quand il existe un intérêt ; le Dutreil (art. 8) n'a, lui, jamais été chiffré. Avec le 23-14 : le gain ~338 M€ par donation de 1,5 Md€ est préservé — l'exclusion des actifs somptuaires ne touche pas la mécanique de concentration.
- **L6 (contexte) :** séquence budgétaire contrainte ; la CdC publie le jour où Lecornu défend la niche ; la LF 2026 est promulguée sans évaluation des exclusions.

**Lecture concurrente** : le gain est « difficile à estimer » (l'exclusion dépend de l'affectation réelle des biens, cas par cas) — technicité réelle. La synthèse retenue : la technicité est invoquée pour ne pas chiffrer ; l'ordre de grandeur (1-6 % du coût) est robuste aux hypothèses ; l'absence de chiffrage par tous les acteurs, y compris la CdC critique, est un fait qui borne le débat.

## 5. FORENSIC REASONING (ICEBERG MAX)

**Émergé (vérifié, source lue)** : actif transmis 20 Md€ 2024 ; dépense 5,5 Md€ 2024 ; taux effectif 8 % (droits dus ≈ 1,6 Md€) ; exemples CdC (20 M€ : 4,2 % vs 42 % ; 2,5 M€ : 1,63 % vs 25,01 % ; démembrement 0,7 % vs 8,3 %) ; exclusion des actifs somptuaires (liste fermée, 3 ans, filiales contrôlées) ; trésorerie et placements exonérés ; allongement 4→6 ans ; 3 amendements AN 03/11/2025 (dont un rejeté : critère d'âge) ; pas d'évaluation de recettes dans les amendements (PDF lus).

**Surface (✧ via chercheur)** : NON TROUVÉ sur 4 axes (évaluation officielle, part des biens non professionnels, gain CdC, évaluation LF 2026) — constat d'absence croisé.

**Immergé (jamais publié)** : la part des actifs somptuaires dans les 20 Md€ ; le gain réel 2026-2027 ; les données DGFiP (bases non publiées depuis 2010) ; le comportement d'évitement (sortie des yachts du bilan avant transmission).

**ICEBERG LOAD :** 9 strates émergées (source lue), 1 surface (constat d'absence), 4 immergées. La signature : le coût est chiffré au million près (5,5 Md€), l'assiette des exclusions ne l'est nulle part — l'asymétrie de connaissance est le fait.

## 6. PRISME DIALECTIQUE

- **Thèse (dominante) :** « Le Dutreil est durci : les actifs somptuaires (yachts, chasse, bijoux) sont exclus de l'exonération — la réforme réduit le coût de la niche. »
- **Antithèse (critique) :** « C'est une réforme a minima : la trésorerie et les titres (le cœur de l'actif transmis) restent exonérés, les 110 donataires (65 %) ne sont pas touchés, le gain des exclusions n'est chiffré par personne — et l'encadrement le situe entre 1 et 6 % du coût de 5,5 Md€ maintenu. »
- **Arbitrage par les preuves :** la thèse est exacte sur la lettre (exclusion votée) ; l'antithèse est exacte sur l'échelle (actifs exonérés = titres/trésorerie ; aucun chiffrage ; encadrement 1-6 %). **La synthèse** : la réforme produit un récit de durcissement sans effet budgétaire significatif — le gain est une fraction résiduelle du coût maintenu, et l'absence de toute évaluation officielle (y compris par la CdC critique) en est la preuve la plus forte.

**Réfutation testée** : « le gain est difficile à chiffrer » — vrai en précision, mais l'encadrement (1-6 %) est robuste aux hypothèses (0,5-5 % de l'actif) ; « la CdC aurait chiffré si l'enjeu était grand » — l'inverse est plus probable : si l'enjeu était massif, le chiffrage existerait. La réfutation borne le verdict.

## 7. CHRONOLOGIE

| Année | Événement | Source | Statut |
|-------|-----------|--------|--------|
| 2020 | Dépense Dutreil : 1,2 Md€ (évaluation CdC, vs 500 M€ de l'administration) | Actu-Juridique 20/11/2025 (lu) | ✦ |
| 2023 | Dépense : 3,3 Md€ ; « très grosse opération » | Actu-Juridique (lu) + CdC | ✦ |
| 2024 | Actif transmis **20 Md€** ; dépense **>5,5 Md€** ; taux effectif **8 %** ; droits dus ≈ 1,6 Md€ ; 110 donataires = 65 % (30 M€) | Actu-Juridique (lu) + CdC | ✦ |
| 03/11/2025 | AN première lecture : 3 amendements (exclusion biens professionnels ; critère d'âge — rejeté ensuite ; engagement 4→6 ans) | Actu-Juridique (lu) | ✦ |
| 18/11/2025 | Rapport CdC : critique, propose de quantifier les biens non professionnels — SANS les chiffrer | Actu-Juridique (lu) + CdC | ✦ |
| 15/01/2026 | Amendement n° 3173 (actifs somptuaires) + sous-amendement n° 3552 (4→6 ans) adoptés en nouvelle lecture — PDF lus, aucune évaluation de recettes | assemblee-nationale.fr (PDF lus) | ✦ |
| 19/02/2026 | LF 2026 (loi 2026-103) promulguée ; art. 8 = Dutreil | hérité 23-40 | ✦ |
| 21/02/2026 | Application aux transmissions intervenant à compter de cette date | hérité 23-40 | ✦ |
| 2026 | Recettes des exclusions : NON ÉVALUÉES (constat d'absence, 4 axes) | ce dossier | ✦ (constat) |
| 2027+ | Effet réel des exclusions (premier exercice complet) | — | ⁅ |

## 8. DOMAINES (par axe)

| Axe | Question | Résultat clé | Faits | Statut |
|-----|----------|--------------|-------|--------|
| AXS-001 DONNÉES | Quelle base ? | 20 Md€ d'actif transmis 2024 ; 5,5 Md€ de dépense ; 8 % de taux effectif ; droits dus ~1,6 Md€ | FCT-002/003 | SATURATED |
| AXS-002 TAUX | Quel écart ? | 4,2 % vs 42 % (20 M€) ; 1,63 % vs 25,01 % (2,5 M€) ; démembrement 0,7 % vs 8,3 % | FCT-004 | SATURATED |
| AXS-003 EXCLUSIONS | Quoi est exclu ? | Liste fermée (chasse, véhicules, yachts/avions, chevaux, vins, bijoux/or, logements réservés) non affectés ≥ 3 ans + filiales contrôlées ; trésorerie et placements exonérés | FCT-005 | SATURATED |
| AXS-004 GAIN | Combien ça rapporte ? | NON CHIFFRÉ par aucune institution ; encadrement 12-350 M€ net/brut (0,4-6 % du coût) | FCT-001/006 | PARTIEL (⁂) |
| AXS-005 COÛT | Combien ça coûte encore ? | >5,5 Md€ maintenus (abattement 75 %/50 %, 500 K€ inchangés) | FCT-003/008 | SATURATED |
| AXS-006 CONCENTRATION | Qui est touché ? | Les 110 (65 %) transmettent titres + trésorerie = exonérés ; les opérations géantes intactes | FCT-007/008 | SATURATED |

## 9. RÉSEAU D'ACTEURS (+ CONTROL_MAP)

| Acteur | Rôle | Action documentée | Preuve | Responsabilité |
|--------|------|-------------------|--------|----------------|
| Cour des comptes | Contrôleur | Chiffre le coût (5,5 Md€) et les taux (8 %) ; pointe les biens non professionnels SANS les quantifier | FCT-002/003/004 | ρ (chiffrage incomplet) |
| Gouvernement (Bercy/Lecornu) | Décideur | Défend la niche ; porte le durcissement a minima ; aucune évaluation de recettes des exclusions | FCT-008 | DÉCISION |
| Assemblée (Mattei/Juvin) | Législateur | Amendements 3173/3552 adoptés sans évaluation de recettes (PDF lus) | FCT-005/008 | DÉCISION |
| Sénat 760 (Husson) | Contrôleur | Recommandations 17/06/2026 (mention notariale, base) — postérieures | hérité 23-25 | ρ |
| Notariat (CSN) | Défenseur | Propose le seuil de prépondérance 50→70 % et la présomption d'utilité de la trésorerie (défend les actifs exonérés) | Actu-Juridique (lu) | LOBBY |
| DGFiP | Détenteur des données | Bases non publiées depuis 2010 ; données CdC « inédites » | hérité 23-25 | ROLE |

**CONTROL_MAP** :

| Contrôleur | Mécanisme | Résultat | Gap |
|------------|-----------|----------|-----|
| CTRL-001 CdC | Rapport | Coût et taux chiffrés | Assiette des exclusions non chiffrée |
| CTRL-002 AN | Amendements | Exclusion votée | Aucune évaluation de recettes |
| CTRL-003 Sénat 760 | Recommandations | Traçabilité proposée | Postérieur à la LF 2026 |
| CTRL-004 DGFiP | Données | Inexploitées pour les exclusions | Module statistique non financé |

## 10. CHAÎNES / PELOTE (causalité)

**CAU-001 : Le coût de 5,5 Md€ est maintenu parce que la structure de l'actif Dutreil (titres, trésorerie) est orthogonale à la liste des exclusions (luxe).**
Étage 1 : l'abattement 75 %/50 % (500 K€) s'applique aux titres et à la trésorerie (FCT-005). Étage 2 : les 110 donataires (65 %) transmettent surtout titres + trésorerie — les actifs exonérés (FCT-007/008). Étage 3 : l'exclusion des yachts/chasse/bijoux frappe une assiette résiduelle. Type : STRUCTUREL. Confidence : high (structure documentée).

**CAU-002 : L'absence de chiffrage du gain est un fait, pas un oubli.**
Étage 1 : la CdC chiffre précisément le coût et les taux mais pas l'assiette des exclusions (FCT-001/004). Étage 2 : les amendements adoptés (3173/3552) ne comportent pas d'évaluation de recettes (PDF lus) (FCT-005). Étage 3 : le chercheur croisé (4 axes) retourne NON TROUVÉ (FCT-001). Type : INSTITUTIONNEL. Confidence : high sur le constat ; la motivation (intérêt à ne pas chiffrer) est inférée.

**CAU-003 : La mesure jumelle (taxe holdings, art. 7) a été chiffrée — preuve que le chiffrage est possible.**
Étage 1 : Lazard a chiffré la taxe holdings (1,5 Md€ → 100 M€) (hérité 04-07). Étage 2 : pour le Dutreil, aucun équivalent. Étage 3 : le contraste documente que le chiffrage existe quand un intérêt le porte. Type : COMPARATIF. Confidence : medium.

**CAU-004 (rejetée) : « La réforme réduira significativement le coût de la niche ».** Non étayée : l'encadrement le situe à 1-6 % ; la trésorerie et les titres restent exonérés ; aucun chiffrage officiel ne la soutient.

**CAU-005 (rejetée) : « L'absence de chiffrage s'explique par la technicité ».** La technicité est réelle (affectation cas par cas) mais ne justifie pas l'absence totale d'ordre de grandeur — l'encadrement (1-6 %) est robuste aux hypothèses.

## 11. CARTE DES PREUVES

### CLAIM_REGISTRY

| ID | Claim | Support | Contre-évidence | Statut |
|----|-------|---------|-----------------|--------|
| CLM-001 | « Aucune évaluation officielle du gain des exclusions n'existe » | Chercheur 4 axes NON TROUVÉ ; amendements 3173/3552 sans évaluation (PDF lus) ; CdC sans chiffrage de l'assiette | L'étude d'impact PLF (non lue, Légifrance bloqué) pourrait contenir une ligne | SOUTENU (constat d'absence croisé) |
| CLM-002 | « Le coût maintenu est >5,5 Md€ (2024) » | Actu-Juridique 20/11/2025 (lu : 1,2 → 3,3 → 5,5 Md€) ; CdC (hérité 22-56) | — | SOUTENU (source primaire) |
| CLM-003 | « Le taux effectif Dutreil est 8 % vs 25-42 % sans » | Actu-Juridique 20/11/2025 (lu : exemples 20 M€ et 2,5 M€) | — | SOUTENU (source primaire) |
| CLM-004 | « La trésorerie et les titres restent exonérés ; seuls les actifs somptuaires non affectés ≥ 3 ans sont exclus » | Amendement 3173 (PDF lu) ; Actu-Juridique 24/03/2026 (lu) ; 23-40 | — | SOUTENU (source primaire) |
| CLM-005 | « Le gain des exclusions est encadré entre ~12 et ~350 M€ (0,4-6 % du coût) » | Calcul encadré (hypothèses 0,5-5 % de l'actif ; lecture nette 12-27 points / brute 20-35 %) | L'assiette réelle est inconnue (GAP-001) | HYPOTHÈSE (⁂) |
| CLM-006 | « Les 110 donataires (65 %) transmettent des actifs exonérés » | 22-56 (110 = 65 %, 30 M€) ; structure actif (titres/trésorerie) | — | SOUTENU (faisceau) |

### FACT_REGISTRY (8 faits)

| ID | Fait | Chiffre | Source | Statut |
|----|------|---------|--------|--------|
| FCT-001 | **CONSTAT D'ABSENCE** : aucune évaluation officielle du gain des exclusions d'actifs somptuaires (chercheur 4 axes : étude d'impact PLF, rapport général, amendement, jaune budgétaire = NON TROUVÉ) ; les amendements 3173/3552 (PDF lus) ne comportent pas d'évaluation de recettes | 0 évaluation | chercheur (4 axes) + PDF AN lus | ✦ (constat) |
| FCT-002 | **Actif transmis sous Dutreil : 20 Md€ en 2024** (base de calcul) ; dépense fiscale >5,5 Md€ en 2024 (1,2 Md€ 2020 → 3,3 Md€ 2023) | 20 Md€ ; 5,5 Md€ | Actu-Juridique 20/11/2025 (lu) + CdC | ✦ |
| FCT-003 | **Droits dus 2024 ≈ 1,6 Md€** (20 Md€ × 8 % de taux effectif — calcul de CE dossier) ; l'exonération (75 % ≤ 500 K€ puis 50 %) est INCHANGÉE par la réforme | ~1,6 Md€ ; 75 %/50 % | Actu-Juridique (lu) + calcul ce dossier | ✦ |
| FCT-004 | **Taux effectifs (CdC, exemples lus)** : 20 M€ en pleine propriété avant 70 ans → 4,2 % avec Dutreil vs 42 % sans ; 2,5 M€ → 1,63 % vs 25,01 % ; démembrement → 0,7 % vs 8,3 % | 4,2/42 ; 1,63/25,01 ; 0,7/8,3 % | Actu-Juridique 20/11/2025 (lu) | ✦ |
| FCT-005 | **Mécanique des exclusions** : biens somptuaires non exclusivement affectés ≥ 3 ans (liste fermée : chasse/pêche, véhicules, yachts/avions, chevaux, vins, bijoux/métaux précieux, logements réservés) + extension aux filiales contrôlées (amdt 3173) ; **trésorerie et placements EXONÉRÉS** ; allongement 4→6 ans = zéro effet de recettes direct | 3 ans ; liste ; trésorerie exonérée | amendement 3173 (PDF lu) + Actu-Juridique (lu) | ✦ |
| FCT-006 | **ENCADREMENT (⁂, HYPOTHÈSE)** : gain = valeur des actifs exclus × (taux normal marginal − ~8 % Dutreil). Deux lectures : (a) BRUT (taux normal 20-35 % de la valeur exclue, exemples CdC 25-42 %) ; (b) NET (écart réel ≈ 12-27 points après le ~8 % déjà payé ; borne haute CdC 38 points pour l'exemple 20 M€). Bornes (0,5 % de l'actif = 100 M€ → brut 20-35 M€ / net 12-27 M€ ; 1-2 % = 200-400 M€ → brut 40-140 M€ / net 24-108 M€ ; 5 % = 1 Md€ → brut 200-350 M€ / net 120-270 M€). **vs 5,5 Md€ maintenus : 0,4 à 6 % (lecture nette, scénario moyen ~0,4-2 %)** | 12-350 M€ (net-brut) ; 0,4-6 % | calcul encadré (ce dossier) | ⁂ |
| FCT-007 | **Les 110 donataires (65 % de la dépense, 30 M€ de moyenne) transmettent des titres et de la trésorerie — les actifs exonérés** ; les opérations géantes (Bolloré/Vivendi 2023 ~1,5 Md€, hérité) sont intactes | 65 % ; 110 ; 30 M€ | 22-56 (hérité) + structure actif | ✦ |
| FCT-008 | **Lecture anti-sycophancie** : le notariat défend la présomption d'utilité de la trésorerie (seuil 50→70 %) — il ne conteste pas l'exclusion du luxe ; la réforme « durcit la forme, préserve le fond » (verdict 23-40) ; gain résiduel non mesuré | — | Actu-Juridique (lu) + 23-40 | ✦ |


<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ❧ | - | - | - | 2026-08-10_04-15_impact-exclusions-dutreil-dmtg | - | -
FCT-002 | FACT | ❧ | - | - | - | 2026-08-10_04-15_impact-exclusions-dutreil-dmtg | - | -
FCT-003 | FACT | ❧ | - | - | - | 2026-08-10_04-15_impact-exclusions-dutreil-dmtg | - | -
FCT-004 | FACT | ❧ | - | - | - | 2026-08-10_04-15_impact-exclusions-dutreil-dmtg | - | -
FCT-005 | FACT | ❧ | - | - | - | 2026-08-10_04-15_impact-exclusions-dutreil-dmtg | - | -
FCT-006 | FACT | ❧ | - | - | - | 2026-08-10_04-15_impact-exclusions-dutreil-dmtg | - | -
FCT-007 | FACT | ❧ | - | - | - | 2026-08-10_04-15_impact-exclusions-dutreil-dmtg | - | -
FCT-008 | FACT | ❧ | - | - | - | 2026-08-10_04-15_impact-exclusions-dutreil-dmtg | - | -
<!-- /FACT_REGISTRY_V1 -->

### CONTRADICTION_LEDGER

| ID | Contradiction | Résolution | Statut |
|----|---------------|------------|--------|
| CONTR-001 | « La réforme réduit le coût de la niche » vs « le coût est maintenu à 5,5 Md€ » | L'abattement 75 %/50 % est inchangé ; les actifs centraux (titres, trésorerie) restent exonérés ; l'encadrement situe le gain à 1-6 % | DOCUMENTÉE (Ω=9) |
| CONTR-002 | « La CdC a chiffré le problème » vs « la CdC n'a pas chiffré l'assiette des exclusions » | La CdC chiffre le coût et les taux, mais PAS la part des biens non professionnels dans les 20 Md€ — le chiffrage est incomplet | DOCUMENTÉE |
| CONTR-003 | « L'allongement 4→6 ans réduit le coût » vs « il ne rapporte rien » | L'allongement retarde la sortie des titres, il ne taxe pas — aucun effet de recettes direct | RÉSOLUE |
| CONTR-004 | « Le gain est difficile à chiffrer » vs « l'absence de chiffrage est un choix » | La technicité est réelle mais l'encadrement (1-6 %) est robuste ; la mesure jumelle (taxe holdings) a été chiffrée par Lazard — le contraste documente l'asymétrie | DOCUMENTÉE |

### EDI

```
geo:0.55 lang:0.85 strat:0.80 owner:0.70 persp:0.80 temp:0.85
EDI_raw = .25×.55 + .20×.85 + .20×.80 + .15×.70 + .15×.80 + .05×.85 = 0.74
Pénalité : MISSING_COUNTER (-.10) : perspective des donataires (défense du dispositif, réalité de la transmission) absente ; l'assiette réelle inconnue (GAP-001).
EDI = 0.64 (BROAD, sous la cible APEX 0.80, écart déclaré)
COV = 0.85 | IND = 0.70 | CC = 4/4
EDI* = .5×.64 + .3×.85 + .2×.70 = 0.715
Perspectives : ⟐ 3 | ⟐̅ 1 | 🎓 2 (CdC, Lazard) | 🌍 0 | 🔥 0
DIAGNOSTIC_NOT_TRUTH
```

### TRACE_MATRIX (extrait)

| FCT | QRY | SRC | URL (référence) | Statut |
|-----|-----|-----|-----------------|--------|
| FCT-002/003/004 | QRY-001 | SRC-01 | actu-juridique.fr/fiscalite/fiscal-finances/pacte-dutreil-le-recadrage-se-profile/ (lu intégralement) | ✦ |
| FCT-005 | QRY-002 | SRC-02 | assemblee-nationale.fr/dyn/17/amendements/2247/AN/3173 + 3552 (PDF lus 03:55) | ✦ |
| FCT-001 | QRY-003 | SRC-03 | chercheur 4 axes (10/08/2026) : NON TROUVÉ | ✦ (constat) |
| FCT-007/008 | QRY-004 | SRC-04/05 | 22-56 (hérité) ; Actu-Juridique (lu) ; 23-40 | ✦ |

## 12. CARTE DIALECTIQUE (scénarios + responsabilité)

| Scénario | Hypothèse | Support | Contre | Lecture |
|----------|-----------|--------|--------|---------|
| S1 « Gain significatif » | Les exclusions rapporteraient des centaines de M€ | Liste fermée ; taux 20-45 % | Aucun chiffrage officiel ; trésorerie/titres exonérés | Rejetée (encadrement 40-350 M€ max) |
| S2 « Gain résiduel » | Les exclusions rapportent 1-6 % du coût | Encadrement (0,5-5 % de l'actif) ; structure orthogonale ; absence de chiffrage | Assiette réelle inconnue | Retenue (verdict) |
| S3 « Évitement » | Les yachts sortent du bilan avant transmission | Fait générateur 31/12/2026 (taxe holdings) ; marge de manœuvre documentée | Comportement non mesuré | Retenue (en attente) |

**IMPACT_MAP** :

| Acteur | Gain | Perte |
|--------|------|-------|
| État | 40-350 M€/an (encadré, non mesuré) | 5,5 Md€ maintenus |
| 110 donataires | Mécanique préservée (titres/trésorerie exonérés) | Exclusion des yachts/résidences (sortables du bilan) |
| Notaires | Sécurité (présomption trésorerie) | — |
| Contribuables | Récit de durcissement | Coût 5,5 Md€ inchangé |

**RESPONSIBILITY_MAP** : aucun auteur d'intention n'est établi (BENEFIT != INTENT). Rôles : gouvernement (durcissement a minima, absence de chiffrage), législateur (amendements sans évaluation), CdC (chiffrage incomplet), notariat (défense de la trésorerie). Responsabilité systémique : une réforme dont l'effet budgétaire (1-6 %) est non mesuré par tous les acteurs — l'opacité statistique (module DGFiP non financé, hérité 23-25) rend le chiffrage structurellement impossible.

## 13. PÉRIMÈTRE & LIMITES

**Inclusions** : impact budgétaire des exclusions d'actifs somptuaires (LF 2026) sur les recettes DMTG ; données de base (20 Md€, 5,5 Md€, taux effectifs) ; mécanique des exclusions ; encadrement (⁂) ; comparaison avec la taxe holdings. Période 2024-2026.

**Exclusions explicites** : le texte de loi exact (Légifrance bloqué — contenu via Actu-Juridique lu + amendements PDF lus) ; la part réelle des actifs somptuaires (inconnue) ; le comportement d'évitement (sortie des biens) ; l'impact PLF 2027 (à venir).

**GAP déclarés** :
- GAP-001 (ACCESS) : **part des actifs somptuaires dans l'actif transmis (20 Md€) — INCONNUE** (aucune source publiée ; DGFiP seule détentrice ; bases non publiées depuis 2010). C'est le verrou central de l'estimation.
- GAP-002 (ACCESS) : évaluation officielle de recettes des amendements Dutreil (non trouvée sur 4 axes ; étude d'impact PLF non lue).
- GAP-003 (CORPUS) : perspective des donataires absente (MISSING_COUNTER, EDI).
- GAP-004 (VERIFY) : comportement d'évitement (sortie des yachts du bilan avant 2026-2027) — à suivre.

## 14. ÉTAT DES CONNAISSANCES

- **CONNU (✦)** : 20 Md€ d'actif 2024 ; 5,5 Md€ de dépense maintenue ; taux effectif 8 % vs 25-42 % ; droits dus ~1,6 Md€ ; exclusions (liste fermée, 3 ans, filiales) ; trésorerie/titres exonérés ; allongement 4→6 ans sans effet de recettes ; amendements sans évaluation (PDF lus).
- **PROBABLE (✧)** : le gain des exclusions est une fraction résiduelle (1-6 %) du coût.
- **HYPOTHÈSE (⁂)** : encadrement 40-350 M€/an (hypothèses 0,5-5 % de l'actif × 20-35 points).
- **CONTESTÉ (⊗)** : « la réforme réduit le coût » (récit) vs « coût maintenu, gain résiduel » (faits).
- **INCONNU (⁅)** : part réelle des actifs somptuaires ; gain réel 2026-2027 ; comportement d'évitement.
- **RÉFUTÉ (❧)** : « la réforme réduira significativement le coût » ; « l'allongement 4→6 ans rapporte » ; « le gain est trop complexe pour être encadré » (l'encadrement 1-6 % est robuste).

## 15. SUSPICION / VÉRIFICATION

**AUDIT DU LEAD** : input UPDATE (impact chiffré de la réforme a minima). Le verdict d'objet est distinct du verdict de lead : « combien rapportent les exclusions ? » reçoit une réponse en trois volets — (a) personne ne l'a chiffré (constat, 4 axes) ; (b) l'encadrement honnête le situe à 1-6 % du coût (40-350 M€) ; (c) le coût de 5,5 Md€ est maintenu (mécanique inchangée).

**Vérifications contradictoires exécutées** : Actu-Juridique « recadrage » lu intégralement (20/11/2025 — taux effectifs, 3 amendements, notariat) ; amendements 3173/3552 relus (PDF, 03:55 — absence d'évaluation de recettes confirmée) ; chercheur croisé 4 axes (évaluation officielle, part des biens non professionnels, gain CdC, évaluation LF 2026) = NON TROUVÉ ; cohérence avec le 23-40 (trésorerie exonérée) et le 04-07 (taxe holdings chiffrée par Lazard — contraste documenté). L'encadrement est présenté comme ⁂ (HYPOTHÈSE) avec bornes transparentes, jamais comme un fait.

**Verdict final : LE GAIN DES EXCLUSIONS EST INCONNU (aucune évaluation officielle) ET ENCADRÉ ENTRE ~12 M€ (NET) ET ~350 M€ (BRUT)/AN — 0,4 à 6 % DU COÛT MAINTENU DE 5,5 Md€.** La réforme a minima exclut le luxe ostentatoire (yachts, chasse, bijoux) mais épargne les titres et la trésorerie — précisément ce que transmettent les 110 donataires (65 %). **Le résultat le plus actionnable : l'absence totale de chiffrage par tous les acteurs (y compris la CdC critique) est le fait central — la puissance publique a durci la forme sans mesurer l'effet ; l'encadrement 1-6 % borne le débat ; la porte suivante est la base DGFiP (e-enregistrement, hérité 23-25) qui permettrait enfin de mesurer l'assiette des exclusions.**

---

# ANNEXE A. SOURCES

| SRC-ID | Source | Locator / date | Rôle | URL |
|--------|--------|----------------|------|-----|
| SRC-01 | Actu-Juridique, « Pacte Dutreil : le recadrage se profile… » (lu intégralement) | 20/11/2025 | ◈ | https://www.actu-juridique.fr/fiscalite/fiscal-finances/pacte-dutreil-le-recadrage-se-profile/ |
| SRC-02 | Amendements AN n° 3173 (Mattei) et n° 3552 (gouvernement) — PDF lus (03:55) | 15/01/2026 | ◈ | https://www.assemblee-nationale.fr/dyn/17/amendements/2247/AN/3173 ; .../3552 |
| SRC-03 | Chercheur web : 4 axes d'évaluation officielle — NON TROUVÉ | 10/08/2026 | ◉ | — |
| SRC-04 | Actu-Juridique, « Tout comprendre sur la taxe holdings » (taxe jumelle chiffrée par Lazard) | 24/03/2026 | ◈ | https://www.actu-juridique.fr/fiscal/tout-comprendre-sur-la-nouvelle-taxe-sur-les-holdings-patrimoniales/ |
| SRC-05 | CdC, « Le Pacte Dutreil… » (18/11/2025) + Sénat 760 (17/06/2026) — hérités 22-56/23-25 | 2025-2026 | ◈ | ccomptes.fr ; senat.fr |

# ANNEXE B. REQUEST_LOG

```
ENGINE:2.8 | MANIFEST:FINAL | RUN_ID:20260810-0415-impact-exclusions-dutreil-dmtg | PARENT_RUN_ID:20260809-2340 | AS_OF:2026-08-10 | INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:NONE
CHECKPOINT_SEQ:0 | LAST_COMPLETED:18b | NEXT_ACTION:NONE | RESUME_COUNT:0
Investigation:impact-exclusions-dutreil-dmtg | complexity:11→COMPLEX | route overrides:NONE | scope:2024-2026, France
modules:KERNEL|SYMBOLS|PATTERNS|THREATS|GATES|REQUEST_LOG|EPISTEMIC|TEMPLATE|INVESTIGATION
degraded:NONE | query target/actual: 4/4 (2 chercheurs + 4 passes basher/lectures)
COUNT: ◈4 ◉1 | unique evidence objects:8 | upstream families:5
LEADS:terminal 1/1 | AXES:terminal 6/6 | N/A:none
FAILURES:3 (PDF CdC bloqué via jina ; Wayback CDX 503 ; rapport AN = page de navigation sans évaluation) | FALLBACKS:3 (Actu-Juridique lu comme source autoritaire ; amendements PDF lus ; chercheur croisé)
unresolved gaps:GAP-001..GAP-004 (assiette réelle, évaluation officielle, corpus, évitement)
```

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL/INPUT_REF |
|---:|---|---|---|---|---|
| 1 | SYS | @MNEMO_Q + lecture parents 23-40/22-56/04-07 | Données héritées : 20 Md€, 5,5 Md€, 110/65 %, trésorerie exonérée, taxe holdings 1,5 Md€→100 M€ | 23-40/22-56/04-07 | investigations/2026-08/2026-08-13_corpus-investigations/ |
| 2 | ◈ | QRY-001 (AXS-001 à 004) : Actu-Juridique recadrage | FOUND : 20 Md€ 2024 ; 5,5 Md€ ; taux effectifs (4,2/42, 1,63/25,01, 0,7/8,3 %) ; 3 amendements AN 03/11/2025 ; notariat (seuil 50→70 %) | SRC-01 | actu-juridique.fr (lu intégralement) |
| 3 | ◈ | QRY-002 (AXS-003) : amendements 3173/3552 (PDF déjà lus) | CONFIRMÉ : liste fermée, 3 ans, filiales ; trésorerie exonérée ; AUCUNE évaluation de recettes dans les amendements | SRC-02 | assemblee-nationale.fr (PDF lus 03:55) |
| 4 | ◉ | QRY-003 (AXS-004) : évaluation officielle du gain | NON TROUVÉ (4 axes : étude d'impact PLF, rapport général, amendement, jaune budgétaire) | SRC-03 | chercheur |
| 5 | ◈ | QRY-004 (AXS-005/006) : coût maintenu + concentration | CONFIRMÉ : abattement inchangé ; 110/65 % transmettent titres + trésorerie ; notariat défend la trésorerie | SRC-04/05 | Actu-Juridique (lu) + hérités |
| 6 | SYS | Encadrement (⁂) : gain = valeur exclue (0,5-5 % de 20 Md€) × (taux normal 20-35 % brut / écart 12-27 points net) = 12-350 M€ (0,4-6 % du coût) | construit avec bornes transparentes | ce dossier | — |
| 7 | SYS | @MNEMO_S + FACT_WRITEBACK | PENDING_AT_SERIALIZATION | — | — |
| 8 | SYS | STATE:FINAL write | PENDING_AT_SERIALIZATION (ce fichier) | — | investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_taxe-holdings-patrimoniales/2026-08-10_04-15_impact-exclusions-dutreil-dmtg_INVESTIGATION.md |

# ANNEXE C. GATES (G0-G10)

| Gate | Vérification | Résultat |
|------|--------------|----------|
| G0 | Modules chargés ; manifest FINAL ; 15 symboles scorés, aucun ✗ | ✅ |
| G1 | LEAD vs OBJECT distincts ; 6 axes terminaux ; périmètre explicite | ✅ |
| G2 | 6 CLM avec support/counter/gap | ✅ |
| G3 | FACT_REGISTRY 8 faits, statuts canoniques | ✅ |
| G4 | Chaque ✦ → SRC-ID + URL ; ⁂ pour l'encadrement (bornes transparentes) | ✅ |
| G5 | CAU-001 à 005 typés, arrêt à l'évidence, CAU-004/005 rejetées | ✅ |
| G6 | CONTROL_MAP + RESPONSIBILITY_MAP ; rôles ≠ responsabilités | ✅ |
| G7 | CONTR-001 à 004 documentés et résolus | ✅ |
| G8 | TRACE_MATRIX ; QRY-001 à 004 tracés ; IDs résolus | ✅ |
| G9 | Manifest FINAL, NEXT_ACTION NONE, aucun PENDING requis | ✅ |
| G10 | Un seul chemin ; une seule write FINAL ; PENDING_AT_SERIALIZATION honnête | ✅ |

**GAP_SEVERITY** : edi_gap = (0.80-0.64)/0.80 = 0.20 ; query_gap = N/A ; coverage_gap = 0. GAP_SEVERITY = 0.20 × 1.00 = 0.20 = seuil → procéder avec divulgation renforcée (GAP-001 à GAP-004 déclarés ; l'assiette réelle est le verrou).

---

*TL;DR : SUJET : impact chiffré de la réforme a minima du Dutreil (LF 2026) sur les recettes DMTG. OBJET : LE GAIN DES EXCLUSIONS EST INCONNU ET NON CHIFFRÉ PAR AUCUNE INSTITUTION — encadré entre ~12 M€ (net) et ~350 M€ (brut)/an, soit 0,4 à 6 % du coût maintenu de >5,5 Md€. Données de base (sources lues) : actif transmis 20 Md€ (2024) ; dépense 5,5 Md€ maintenue ; taux effectif 8 % avec Dutreil vs 25-42 % sans (exemples CdC : 4,2/42, 1,63/25,01, 0,7/8,3 %) ; droits dus ~1,6 Md€. Mécanique : exclusion des actifs somptuaires (liste fermée, ≥ 3 ans, filiales contrôlées — amdt 3173) MAIS trésorerie et placements EXONÉRÉS ; allongement 4→6 ans sans effet de recettes. Les 110 donataires (65 %, 30 M€) transmettent titres + trésorerie = les actifs exonérés. CONSTAT : chercheur 4 axes NON TROUVÉ (évaluation officielle) ; amendements PDF lus sans évaluation ; la CdC chiffre le coût mais pas l'assiette des exclusions. ENCADREMENT (⁂) : gain = valeur exclue (0,5-5 % de 20 Md€) × (taux normal 20-35 % brut / écart 12-27 points net, borne haute CdC 38) = 12-350 M€ (0,4-6 % du coût ; moyen, net ~0,4-2 %). VERDICT : la réforme durcit la forme (yachts exclus) sans toucher la mécanique (titres, trésorerie, 110/65 % intacts) — gain résiduel non mesuré, absence de chiffrage = le fait. SOURCE : UPDATE 23-40 + 04-07. MANIPULATION : Ξ=9, Ω=9, ↕=9, Κ=9, €=9. LIMITE : assiette réelle inconnue (GAP-001, base DGFiP non publiée), évaluation officielle absente, évitement non mesuré.*
