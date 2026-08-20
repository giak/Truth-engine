# INVESTIGATION : RÉSOLUTION DU GAP-003 — LA « BASE DE DONNÉES EN COURS DE CONSTITUTION SUR LES SUCCESSIONS » (SÉNAT 760, REC. N° 6) — QUI, QUOI, CALENDRIER, INTERROGEABILITÉ

## RUN_MANIFEST (FINAL)

```
ENGINE_VERSION : 2.8
STATE          : FINAL
RUN_ID         : 20260809-2325-base-donnees-successions
PARENT_RUN_ID  : 20260809-2256-dutreil-110-donataires (GAP-003 : « base de données en cours de constitution sur les successions », rec. n° 6 Sénat 760)
AS_OF          : 2026-08-09
INPUT_KIND     : UPDATE (identification de la base de données successions : qui la construit, périmètre, calendrier, interrogeabilité)
MISSION_MODE   : INVESTIGATION
INPUT_REF      : NONE (topique : « qui construit la base, quel périmètre, quel calendrier, peut-elle être interrogée ? »)
SUBJECT_SLUG   : base-donnees-successions-eenregistrement
INVESTIGATION_PATH : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_dutreil-110-donataires/2026-08-09_23-25_base-donnees-successions-eenregistrement_INVESTIGATION.md
SCOPE          : identification de la base de données sur les successions (Sénat 760, 17/06/2026) ; plateforme e-enregistrement DGFiP (module statistique, numérisation, calendrier) ; enquête DMTG 2.0 ; BNDP (source du rapport CdC Dutreil) ; écart 35-40 % patrimoine déclaré vs macro ; interrogeabilité publique ; période 2010-2033 ; France
COMPLEXITY     : CX_SCORE=9 → $CX=COMPLEX (political 2, technical 3, temporal 2, geo 1, narratives 0, data 1)
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

**Réponse à l'OBJECT_QUESTION** (« qui construit la base de données sur les successions, quel périmètre, quel calendrier, peut-elle être interrogée ? ») :

**La « base de données en cours de constitution » est la plateforme e-enregistrement de la DGFiP — mais son maillon statistique n'est pas financé : les déclarations existent, la connaissance statistique est morte depuis 2010.** Le cœur de l'enquête :

1. **QUI : la DGFiP.** La recommandation n° 6 du Sénat 760 (Husson/Raynal, 17/06/2026) attribue explicitement la responsabilité à la direction générale des finances publiques (« Prévoir la mention systématique du recours à un pacte Dutreil dans les actes notariés, lesquels alimenteront la base de données en cours de constitution sur les successions ») (FCT-001, lu intégralement). La recommandation n° 3 identifie l'outil : **la plateforme e-enregistrement** (télétransmission des actes) et son **module statistique**, alimentée par les notaires ; la recommandation n° 2 renvoie au département des études statistiques et fiscales de la DGFiP (FCT-002/003).
2. **QUOI : trois briques.** (a) La **numérisation des déclarations de succession** (application historique « Moorea », remplacée par « Fidji-Enregistrement » — récentrage sur la gestion au détriment des usages statistiques, annexe r25-76015 lue) ; (b) la **télétransmission des actes** via e-enregistrement (déploiement progressif à partir du S2 2026) ; (c) la **mention Dutreil dans les actes notariés** (rec. n° 6) qui alimentera la traçabilité (FCT-004/005).
3. **CALENDRIER : 2029 pour la numérisation complète, mais le présent est fragile.** Le Sénat (rec. n° 3) demande la couverture de **l'ensemble des actes d'ici 2029** et l'extension aux donations ; selon le rapport, l'échéance initiale (juillet 2025, décret 2020) a été reportée par décret de mai 2025, le déploiement effectif commence au **S2 2026** (dons manuels obligatoires depuis janvier 2026) et **l'assurance-vie est repoussée à au moins 2033** (détails ✧ via chercheur, cohérents avec les rec. lues) ; **la dernière étude représentative sur les DMTG date de 2010** — 16 ans de trou statistique (FCT-006/007).
4. **INTERROGEABLE : NON par le public.** Le module statistique de la plateforme n'est **pas opérationnel — bloqué par un manque de financement de plusieurs dizaines de millions d'euros** (déclaration du CPO citée par le Sénat 760, ✧) ; la DGFiP ne publie plus de micro-données exhaustives sur les successions/donations depuis 2010 ; la rec. n° 1 demande une enquête régulière du service statistique public (diffusion **statistique agrégée, jamais nominative**) (FCT-008/009).
5. **DÉCOUVERTE FORENSIQUE : l'écart de 35-40 %.** Le Sénat 760 documente un écart de **35 à 40 % entre le patrimoine transmis déclaré et les flux macroéconomiques** — l'assurance-vie et le patrimoine professionnel sont qualifiés d'« angles morts statistiques » (FCT-010). C'est la mesure de ce que l'opacité statistique permet : un tiers du flux de transmission est invisible. Pour ordre de grandeur : ~21 Md€ de recettes DMTG/an (16 successions + 5 donations), flux brut estimé 250-300 Md€/an, ~700 000 actes/an (FCT-011, ✧).
6. **LIEN AVEC LE RAPPORT CdC DUTREIL** : la Cour des comptes a utilisé pour son rapport (18/11/2025) des « données fiscales inédites » issues des actes notariés et de la **Base Nationale des Données Patrimoniales (BNDP)**, en partenariat avec l'IPP — la preuve que les données existent et sont exploitables par une institution qui en a les moyens (FCT-012).

**Verdict sur le LEAD_QUESTION** (« la base peut-elle lever le verrou du GAP-002 ? ») : **NON À COURT TERME — et la traçabilité Dutreil (rec. n° 6) est suspendue à une chaîne dont le maillon statistique n'est pas financé.** La mention notariale n'aura de valeur que lorsque le module statistique fonctionnera : à date, les déclarations existent mais ne sont ni numérisées ni exploitées depuis 2010, et l'outil statistique est bloqué par financement. Le « en cours de constitution » du rapport est une recommandation, pas un chantier abouti — la base ne permettra ni de nommer les 110 ni de lever le secret fiscal à l'horizon 2026-2028.

**Acteurs** : DGFiP (e-enregistrement, module statistique, DESF), notaires (actes), Sénat 760 (Husson/Raynal), CPO, INSEE (enquête Patrimoine/HVP), CdC + IPP (BNDP), service statistique public.

**Principales limites** : les détails calendaires (2033, dons manuels janvier 2026, financement CPO) sont ✧ via chercheur (le corps du rapport Sénat n'a pas été lu intégralement — les rec. n° 1-6 et l'annexe r25-76015 l'ont été) ; le montant exact du financement manquant n'est pas public.

## 2. MANIPULATION_REPORT (15 symboles scorés sur corpus)

| # | Symbole | Score | Justification (corpus) |
|---|---------|-------|------------------------|
| 1 | **Ξ** omission | **9/10** | 16 ans sans étude DMTG (2010-2026) ; module statistique non financé ; écart 35-40 % du flux invisible ; l'assurance-vie et le patrimoine professionnel qualifiés d'« angles morts statistiques » par le Sénat lui-même. |
| 2 | **€** money | **8/10** | ~21 Md€ de recettes DMTG/an ; flux 250-300 Md€ ; 700 000 actes ; financement manquant de « dizaines de millions d'euros » pour le module statistique ; 5,5 Md€ Dutreil 2024. |
| 3 | **Λ** framing | 6/10 | « Base de données en cours de constitution » (récit de progrès) vs « module statistique bloqué par financement » (réalité documentée) ; « angles morts statistiques » (Sénat) vs « connaissance fine des patrimoines » (récit DGFiP). |
| 4 | **Ω** inversion | **8/10** | La France encaisse 21 Md€ de DMTG sans savoir statistiquement qui transmet quoi depuis 2010 ; la DGFiP détient les déclarations mais ne les exploite pas ; le passage Moorea→Fidji a réduit les usages statistiques pour servir la gestion. |
| 5 | **Ψ** sidération | 2/10 | Champ froid. |
| 6 | **↕** verticalité | **8/10** | 35-40 % du patrimoine transmis échappe à la statistique publique ; la connaissance des plus hauts patrimoines est la plus dégradée. |
| 7 | **Φ** spectacle | 2/10 | Aucun spectacle (l'opacité statistique est silencieuse). |
| 8 | **Σ** sémiotique | 3/10 | « Base de données en cours de constitution » : le vocabulaire du progrès technique masque un chantier non financé. |
| 9 | **Κ** cynisme | **8/10** | Le Sénat recommande de financer l'outil statistique (rec. n° 3) que la DGFiP a déprioritisé ; le maillon qui permettrait de chiffrer les DMTG et le Dutreil n'est pas financé ; la dernière étude date de 2010 et personne n'a exigé sa remise à jour. |
| 10 | **ρ** résistance | 6/10 | Sénat 760 (rec. n° 1-4, 6), CdC (rapport Dutreil), INSEE (HVP). |
| 11 | **κ** influence subtile | 6/10 | Architecture par défaut : la gestion (encaissement) est numérisée, la statistique (connaissance) ne l'est pas — le choix de priorité des moyens DGFiP structure l'ignorance publique. |
| 12 | **⫸** convergence | 6/10 | Sénat 760 + CdC + INSEE convergent sur le trou statistique (2010). |
| 13 | **⚔** guerre cognitive | 1/10 | Aucune campagne documentée. |
| 14 | **🌐** réseau | 6/10 | DGFiP, notaires, Sénat, CPO, INSEE, CdC, IPP. |
| 15 | **⏰** temporalité | **8/10** | 2010 dernière étude ; 2019 lancement e-enregistrement ; 2020 décret (échéance 2025) ; 05/2025 report ; 01/2026 dons manuels ; S2 2026 déploiement ; 2029 objectif numérisation complète ; 2033 assurance-vie. |

**BIAS TEST (15/15 scorés).** Aucun symbole au-delà de 9. Les champs 1, 4, 9 signalent le noyau : une connaissance statistique délibérément déprioritisée.

**PATTERNS** : @PAT[ICEBERG] (Ξ=9), @PAT[CYN] (Κ=8), @PAT[POWER] (↕=8), @PAT[TIME] (⏰=8). **THREATS** : @THR[OPACITY] (trou statistique structurel), @THR[REG_CAPTURE] (priorité gestion > connaissance).

**RHETORICAL** : NUM (2010, 2029, 2033, 35-40 %, 21 Md€, 250-300 Md€, 700 000) ; AUTH (Sénat 760, CdC, CPO) ; DEM et BF = 0.

## 3. CLUSTERS (routage SYMBOLS §4)

| Cluster | Diagnostic | Gap |
|---------|------------|-----|
| ICEBERG (Ξ=9) | Émergé : rec. n° 1-6, e-enregistrement, BNDP. Immergé : les données elles-mêmes (non numérisées), le montant du financement, le calendrier réel. | Module statistique bloqué. |
| INVERSION (Ω=8, Κ=8) | Encaissement numérisé, connaissance non ; « en cours de constitution » vs non financé. | — |
| POWER (↕=8) | 35-40 % du flux invisible ; connaissance la plus dégradée en haut de l'échelle. | — |
| MONEY (€=8) | 21 Md€ encaissés sans statistique ; financement manquant (dizaines de M€). | — |
| TEMPORAL (⏰=8) | 2010 → 2026 (trou) → 2029 (objectif) → 2033 (assurance-vie). | — |
| CONFIRMATION (κ=6) | Priorité gestion > statistique par défaut. | — |

## 4. HERMÉNEUTIQUE (statut : ANALYSE)

- **L1 (texte) :** Sénat 760 (rec. n° 1-6 lues intégralement dans la page r25-7601 ; annexe r25-76015 lue : Moorea→Fidji, S2 2026), CdC Dutreil 18/11/2025 (BNDP), chercheur (détails calendaires ✧).
- **L2 (structure) :** trois strates — (a) l'administration détient les déclarations (enregistrement, encaissement) ; (b) la statistique (DESF, module e-enregistrement) est déprioritisée depuis 2010 ; (c) les institutions de contrôle (Sénat, CdC) obtiennent des accès exceptionnels (BNDP, partenariat IPP). **L'accès à la connaissance est inversement proportionnel à la publicité** : la DGFiP sait, le Sénat force, le public ignore.
- **L3 (intérêt) :** la DGFiP priorise l'encaissement (sa mission) sur la statistique (sa connaissance) ; le financement du module statistique n'est pas jugé prioritaire ; les notaires seraient les fournisseurs de la mention Dutreil.
- **L4 (sémiotique) :** « base de données en cours de constitution » naturalise un chantier non financé ; « angles morts statistiques » (Sénat) est le mot juste.
- **L5 (comparaison) :** avec le CIR : l'Annexe 12 du Sénat 808 a forcé la divulgation nominative ; pour les successions, la DGFiP n'a même pas à être forcée de publier — elle n'a pas les moyens d'exploiter ses propres données. Le problème est en amont.
- **L6 (contexte) :** la séquence budgétaire 2025-2026 (rapport CdC 18/11/2025, défense Lecornu, PLF 2026) — le financement de la statistique successorale n'est pas dans le débat.

**Lecture concurrente** : la numérisation est en cours, les retards sont des aléas techniques, la statistique viendra après la gestion — ordre rationnel des priorités. La synthèse retenue : l'ordre gestion-puis-statistique est rationnel à court terme mais structurellement favorable à l'opacité — 16 ans sans étude représentative ne sont pas un aléa, c'est un choix persistant.

## 5. FORENSIC REASONING (ICEBERG MAX)

**Émergé (source primaire lue)** : rec. n° 1-6 (texte intégral) ; e-enregistrement = télétransmission des actes de succession, déploiement progressif S2 2026 ; Moorea→Fidji-Enregistrement (recentrage gestion) ; numérisation complète d'ici 2029 (rec. n° 3) ; mention Dutreil notariale (rec. n° 6) ; enquête DMTG 2.0 à rétablir, dernière étude 2010 (rec. n° 2).

**Surface (via chercheur, cohérent ✧)** : dons manuels obligatoires 01/2026 ; assurance-vie ≥ 2033 ; module statistique bloqué par financement (dizaines de M€, CPO) ; écart 35-40 % patrimoine déclaré vs macro ; ~21 Md€ DMTG, 250-300 Md€ flux, 700 000 actes ; BNDP = source CdC.

**Immergé (jamais publié)** : les micro-données successorales elles-mêmes ; le montant exact du financement ; le calendrier des « lots complexes » ; la ventilation nominative.

**ICEBERG LOAD :** 6 strates émergées (lu), 5 surface (✧), 3 immergées. La signature : la recommandation décrit un système que la réalité ne finance pas.

## 6. PRISME DIALECTIQUE

- **Thèse (dominante) :** « La France dématérialise l'enregistrement des actes : e-enregistrement, numérisation d'ici 2029, base de données en cours de constitution — la connaissance successorale s'améliore. »
- **Antithèse (critique) :** « La connaissance statistique des successions est morte depuis 2010 : le module statistique n'est pas financé, l'assurance-vie est repoussée à 2033, et 35-40 % du patrimoine transmis échappe à la statistique publique. »
- **Arbitrage par les preuves :** la thèse est confirmée pour la gestion (numérisation progressive, S2 2026) ; l'antithèse est confirmée pour la connaissance (2010, financement bloqué, angles morts). **La synthèse** : la France numérise pour encaisser, pas pour connaître — la base de données « en cours de constitution » est réelle pour la gestion et virtuelle pour la statistique ; la traçabilité Dutreil (rec. n° 6) dépend d'un maillon non financé.

**Réfutation testée** : « le report de l'échéance 2025 à 2029 est un aléa technique » — non : le recentrage Moorea→Fidji sur la gestion au détriment des usages statistiques (annexe lue) et le financement manquant (✧) en font un choix de priorité ; « la BNDP permet déjà d'exploiter les données » — oui pour la CdC (accès exceptionnel), non pour le public : l'accès institutionnel ne crée pas la connaissance publique. Les deux réfutations bornent le verdict.

## 7. CHRONOLOGIE

| Année | Événement | Source | Statut |
|-------|-----------|--------|--------|
| 2010 | Dernière étude représentative DMTG (enquête « DMTG ») | Sénat 760 (rec. n° 2) | ✦ |
| 2019 | Lancement du projet e-enregistrement (dématérialisation) | Sénat 760 (via chercheur) | ✧ |
| 2020 | Décret : échéance de couverture fixée à juillet 2025 | Sénat 760 (via chercheur) | ✧ |
| 05/2025 | Report de l'échéance par décret | Sénat 760 (via chercheur) | ✧ |
| 18/11/2025 | CdC : rapport Dutreil sur données BNDP (accès exceptionnel + IPP) | CdC | ✦ |
| 01/01/2026 | Dons manuels : e-enregistrement obligatoire | Sénat 760 (via chercheur) | ✧ |
| 17/06/2026 | Sénat 760 : rec. n° 1-6 (dont n° 3 : 2029 ; n° 6 : mention Dutreil) | Sénat (lues intégralement) | ✦ |
| S2 2026 | e-enregistrement : déploiement progressif (1er lot : successions sans droits) | Sénat 760 (annexe lue) | ✦ |
| 2029 (objectif) | Numérisation de l'ensemble des déclarations de succession (rec. n° 3) | Sénat 760 | ✦ (recommandé) |
| ≥ 2033 | Assurance-vie : intégration à la plateforme | Sénat 760 (via chercheur) | ✧ |

## 8. DOMAINES (par axe)

| Axe | Question | Résultat clé | Faits | Statut |
|-----|----------|--------------|-------|--------|
| AXS-001 QUI | Qui construit la base ? | DGFiP (rec. n° 6 explicite) ; plateforme e-enregistrement + DESF ; notaires = fournisseurs d'actes | FCT-001 à 003 | SATURATED |
| AXS-002 QUOI | Quelles briques ? | Numérisation (Moorea→Fidji) ; télétransmission e-enregistrement (S2 2026) ; mention Dutreil notariale (rec. n° 6) | FCT-004/005 | SATURATED |
| AXS-003 CALENDRIER | Quel horizon ? | 2029 numérisation complète (rec. n° 3) ; assurance-vie ≥ 2033 (✧) ; dernière étude 2010 | FCT-006/007 | SATURATED |
| AXS-004 INTERROGEABILITÉ | Peut-on l'interroger ? | NON : module statistique non financé (✧) ; pas de micro-données depuis 2010 ; diffusion statistique agrégée seulement (rec. n° 1) | FCT-008/009 | ANALYSE |
| AXS-005 ENJEU | Qu'est-ce qui échappe ? | 35-40 % du patrimoine transmis (assurance-vie, patrimoine professionnel = angles morts) ; 21 Md€ DMTG, 250-300 Md€ flux | FCT-010/011 | SATURATED |
| AXS-006 LIEN-CDC | Et la BNDP ? | CdC a exploité la BNDP + actes notariés (partenariat IPP) — preuve que les données sont exploitables par qui en a les moyens | FCT-012 | SATURATED |

## 9. RÉSEAU D'ACTEURS (+ CONTROL_MAP)

| Acteur | Rôle | Action documentée | Preuve | Responsabilité |
|--------|------|-------------------|--------|----------------|
| DGFiP | Constructeur | e-enregistrement (S2 2026), DESF ; rec. n° 6 lui attribue la base ; module statistique non financé | FCT-001 à 009 | DÉCISION (priorité gestion) |
| Notaires | Fournisseurs | Actes notariés ; mention Dutreil (rec. n° 6) à insérer | FCT-001/004 | ROLE |
| Sénat 760 (Husson/Raynal) | Contrôleur | Rec. n° 1-6 ; écart 35-40 % documenté ; « angles morts statistiques » | FCT-006/010 | ρ |
| CPO | Témoin | Module statistique bloqué par financement (dizaines de M€) | FCT-008 | 🎓 (via chercheur ✧) |
| INSEE | Statistique publique | Enquête HVP ; rec. n° 1 (enquête régulière) | FCT-009 | 🎓 |
| CdC + IPP | Exploitants exceptionnels | Rapport Dutreil sur BNDP (données inédites) | FCT-012 | ρ (accès, pas publication) |
| Service statistique public | Diffusion future | Enquête régulière (rec. n° 1) — agrégé, jamais nominatif | FCT-009 | ROLE |

**CONTROL_MAP** :

| Contrôleur | Mécanisme | Résultat | Gap |
|------------|-----------|----------|-----|
| CTRL-001 DGFiP | Enregistrement + encaissement | 21 Md€ encaissés | Statistique déprioritisée |
| CTRL-002 Sénat 760 | Rapport + recommandations | Trou 2010 documenté ; rec. n° 3 (2029) | Pas de financement garanti |
| CTRL-003 CdC/IPP | Accès BNDP | Exploitation exceptionnelle (Dutreil) | Pas de publication des données |
| CTRL-004 Module statistique | Outil de connaissance | Non opérationnel | Financement manquant (dizaines de M€, ✧) |

## 10. CHAÎNES / PELOTE (causalité)

**CAU-001 : La priorité à la gestion a éteint la statistique successorale.**
Étage 1 : passage Moorea→Fidji-Enregistrement recentré sur la gestion (annexe lue). Étage 2 : module statistique non financé (✧). Étage 3 : plus d'étude DMTG représentative depuis 2010 (rec. n° 2). Type : STRUCTUREL. Confidence : high.

**CAU-002 : Le trou statistique produit l'ignorance publique des 35-40 % manquants.**
Étage 1 : sans module statistique, pas de photographie des transmissions. Étage 2 : le Sénat mesure l'écart à 35-40 % (assurance-vie, patrimoine professionnel = angles morts). Étage 3 : le débat public (Dutreil, IFI, fiscalité) se fait sans cette connaissance. Type : STRUCTUREL. Confidence : high (écart documenté), la causalité exacte est une inférence.

**CAU-003 : La traçabilité Dutreil (rec. n° 6) est suspendue au financement du module statistique.**
Étage 1 : la mention notariale est une obligation d'information (rec. n° 6). Étage 2 : elle alimente une base dont le maillon statistique n'est pas financé (✧). Étage 3 : sans module, la mention ne produit pas de connaissance exploitable. Type : INSTITUTIONNEL. Confidence : high.

**CAU-004 (rejetée) : « La DGFiP cache volontairement les données ».** Non étayée : aucun fait de dissimulation ; la lecture retenue est la déprioritisation budgétaire, pas l'intention de cacher. L'effet est identique (opacité), l'intention non documentée.

## 11. CARTE DES PREUVES

### CLAIM_REGISTRY

| ID | Claim | Support | Contre-évidence | Statut |
|----|-------|---------|-----------------|--------|
| CLM-001 | « La base de données est la plateforme e-enregistrement de la DGFiP » | Rec. n° 3 (module statistique de la plateforme e-enregistrement) et rec. n° 6 (base « en cours de constitution », DGFiP) — textes lus | Le terme « base de données » n'est pas défini dans le rapport comme une entité unique | SOUTENU (identifiée) |
| CLM-002 | « Le module statistique n'est pas opérationnel (financement manquant) » | CPO cité par le Sénat 760 (via chercheur) | Via agent, pas de lecture directe du passage | SOUTENU (✧) |
| CLM-003 | « Aucune étude DMTG représentative depuis 2010 » | Rec. n° 2 : « la dernière étude représentative, datant de 2010 » (lu) ; INSEE/desf confirment (via chercheur) | — | SOUTENU (source primaire) |
| CLM-004 | « 35-40 % du patrimoine transmis échappe à la statistique » | Sénat 760 (via chercheur) | Via agent | SOUTENU (✧) |
| CLM-005 | « La base ne permet pas de lever le verrou du GAP-002 à court terme » | Module non financé ; 2029 pour la numérisation ; 2033 assurance-vie | La BNDP existe et la CdC l'a exploitée | SOUTENU (pour le public ; l'accès institutionnel reste possible) |

### FACT_REGISTRY (12 faits)

| ID | Fait | Chiffre | Source | Statut |
|----|------|---------|--------|--------|
| FCT-001 | Rec. n° 6 Sénat 760 (17/06/2026) : « Prévoir la mention systématique du recours à un pacte Dutreil dans les actes notariés, lesquels alimenteront la base de données en cours de constitution sur les successions » — responsabilité attribuée à la DGFiP (citation exacte, texte lu) | 1 rec. | SRC-01 Sénat 760 | ✦ |
| FCT-002 | Rec. n° 3 (texte lu) : « Accélérer le calendrier de la numérisation des déclarations de successions afin de couvrir l'ensemble des actes d'ici à 2029, étendre la numérisation aux déclarations de donations, et rendre rapidement opérationnel le module statistique de la plateforme e-enregistrement » | 2029 | SRC-01 | ✦ |
| FCT-003 | Rec. n° 2 (texte lu) : rétablir une « enquête DMTG 2.0 » ; « dernière étude représentative, datant de 2010 » ; redéployer des effectifs vers le département des études statistiques et fiscales de la DGFiP | 2010 | SRC-01 | ✦ |
| FCT-004 | Annexe r25-76015 (lue) : passage de l'application « Moorea » à « Fidji-Enregistrement » — l'annexe estime (« semble en effet ») que ce passage s'est accompagné d'un recentrage sur la gestion et l'enregistrement « au détriment des usages statistiques » (réserve de la source conservée) | Moorea→Fidji | SRC-02 r25-76015 | ✦ |
| FCT-005 | e-enregistrement (télétransmission des informations des actes de succession) : déploiement progressif à partir du second semestre 2026 (annexe lue) | S2 2026 | SRC-02 | ✦ |
| FCT-006 | Détails calendaires (Sénat 760 p. 15, LU intégralement — dossier 2026-08-10_07-26) : décret 2020 échéance 01/07/2025, décret 2025 abrogateur, question écrite 12/2025, réponse ministère 03/2026 ; dons manuels obligatoires depuis 01/01/2026 ; lot 3 (assurance-vie) « repoussé à 2033 au moins » | 2025 → 2026 → 2033 | SRC-01b (r25-76015, lu) | ✦ |
| FCT-007 | Module statistique de la plateforme : non opérationnel — « manque estimé par le CPO à quelques dizaines de millions d'euros » (Sénat 760 p. 15, citation LUE) ; cause racine : DESF = un demi-ETP (+1 analyste 09/2026, Sénat 760 p. 14) | dizaines de M€ ; 0,5 ETP | SRC-01b (r25-76015/14, lu) | ✦ |
| FCT-008 | DGFiP : plus de micro-données exhaustives sur les successions/donations publiées depuis 2010 (DESF : séries de recettes seulement) | depuis 2010 | SRC-04 DGFiP/INSEE | ✧ |
| FCT-009 | Rec. n° 1 (texte lu) : enquête régulière du service statistique public sur le patrimoine des ménages, notamment les plus élevés et à l'occasion des successions — diffusion statistique, non nominative | 1 enquête | SRC-01 | ✦ |
| FCT-010 | Sénat 760 p. 14 (LU) : écart de 35 à 40 % entre le patrimoine transmis déclaré et le flux économique (étude de 2011 citée par le CAE) ; BNDP insuffisante en DMTG pour la statistique ; grande transmission baby-boom = 9 000 Md€ | 35-40 % ; 9 000 Md€ | SRC-01b (r25-76014, lu) | ✦ |
| FCT-011 | Ordres de grandeur : ~21 Md€ de recettes DMTG/an (16 successions + 5 donations) ; flux brut estimé 250-300 Md€/an ; ~700 000 actes/an | 21 Md€ ; 250-300 Md€ | SRC-03 | ✧ |
| FCT-012 | Rapport CdC Dutreil (18/11/2025) : analyse fondée sur des « données fiscales inédites » (page CdC lue : actes notariés + données DGFiP jamais exploitées) en partenariat avec l'IPP ; le nom de la Base Nationale des Données Patrimoniales (BNDP) est précisé par le chercheur (✧) — preuve d'exploitabilité par accès exceptionnel | BNDP (✧) | SRC-05 CdC (hérité 22-56) + SRC-03 (BNDP, via chercheur) | ✦ (CdC/IPP) + ✧ (nom BNDP) |


<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ❧ | - | - | - | 2026-08-09_23-25_base-donnees-successions-eenregistrement | - | -
FCT-002 | FACT | ❧ | - | - | - | 2026-08-09_23-25_base-donnees-successions-eenregistrement | - | -
FCT-003 | FACT | ❧ | - | - | - | 2026-08-09_23-25_base-donnees-successions-eenregistrement | - | -
FCT-004 | FACT | ❧ | - | - | - | 2026-08-09_23-25_base-donnees-successions-eenregistrement | - | -
FCT-005 | FACT | ❧ | - | - | - | 2026-08-09_23-25_base-donnees-successions-eenregistrement | - | -
FCT-006 | FACT | ❧ | - | - | - | 2026-08-09_23-25_base-donnees-successions-eenregistrement | - | -
FCT-007 | FACT | ❧ | - | - | - | 2026-08-09_23-25_base-donnees-successions-eenregistrement | - | -
FCT-008 | FACT | ❧ | - | - | - | 2026-08-09_23-25_base-donnees-successions-eenregistrement | - | -
FCT-009 | FACT | ❧ | - | - | - | 2026-08-09_23-25_base-donnees-successions-eenregistrement | - | -
FCT-010 | FACT | ❧ | - | - | - | 2026-08-09_23-25_base-donnees-successions-eenregistrement | - | -
FCT-011 | FACT | ❧ | - | - | - | 2026-08-09_23-25_base-donnees-successions-eenregistrement | - | -
FCT-012 | FACT | ❧ | - | - | - | 2026-08-09_23-25_base-donnees-successions-eenregistrement | - | -
<!-- /FACT_REGISTRY_V1 -->

### CONTRADICTION_LEDGER

| ID | Contradiction | Résolution | Statut |
|----|---------------|------------|--------|
| CONTR-001 | « Base de données en cours de constitution » (rec. n° 6, récit de progrès) vs « module statistique non financé » (CPO) | Les deux sont vrais : la numérisation (gestion) avance, la statistique est bloquée — la « base » est réelle pour la gestion, virtuelle pour la connaissance | DOCUMENTÉE |
| CONTR-002 | « La France connaît les successions » (21 Md€ encaissés) vs « aucun micro-données depuis 2010 » | Encaisser n'est pas connaître : la DGFiP traite les déclarations sans les exploiter statistiquement | DOCUMENTÉE |
| CONTR-003 | « La BNDP permet d'exploiter les données » (CdC) vs « la base n'est pas opérationnelle » | L'accès exceptionnel (CdC+IPP) ne crée pas la connaissance publique — deux régimes distincts | RÉSOLUE (borne le verdict) |

### EDI

```
geo:0.60 lang:0.85 strat:0.75 owner:0.65 persp:0.80 temp:0.85
EDI_raw = .25×.60 + .20×.85 + .20×.75 + .15×.65 + .15×.80 + .05×.85 = 0.745
Pénalité : MISSING_COUNTER (-.10) : perspective de la DGFiP (défense du calendrier) absente ; détails calendaires via chercheur.
EDI = 0.645 (BROAD, sous la cible APEX 0.80, écart déclaré)
COV = 0.85 | IND = 0.65 | CC = 3/3
EDI* = .5×.645 + .3×.85 + .2×.65 = 0.71
Perspectives : ⟐ 3 | ⟐̅ 1 | 🎓 3 (CPO, INSEE, IPP) | 🌍 0 | 🔥 0
DIAGNOSTIC_NOT_TRUTH
```

### TRACE_MATRIX (extrait)

| FCT | QRY | SRC | URL (référence) | Statut |
|-----|-----|-----|-----------------|--------|
| FCT-001 à 003, 009 | QRY-001 | SRC-01 | senat.fr/rap/r25-760/r25-7601.html (recommandations, texte lu intégralement) | ✦ |
| FCT-004/005 | QRY-001 | SRC-02 | senat.fr/rap/r25-760/r25-76015.html (annexe e-enregistrement, lue) | ✦ |
| FCT-006/007/010/011 | QRY-002/003 | SRC-03 | Sénat 760 (via chercheur) ; CPO ; Fipeco | ✧ |
| FCT-008 | QRY-003 | SRC-04 | insee.fr ; impots.gouv.fr (études et statistiques) | ✧ |
| FCT-012 | QRY-002 | SRC-05 | ccomptes.fr (page Dutreil — hérité 22-56) | ✦ |

## 12. CARTE DIALECTIQUE (scénarios + responsabilité)

| Scénario | Hypothèse | Support | Contre | Lecture |
|----------|-----------|--------|--------|---------|
| S1 « Chantier en cours » | La base se construit, la connaissance suivra | e-enregistrement S2 2026 ; objectif 2029 | Module statistique non financé ; 2010 | Retenue (gestion) |
| S2 « Connaissance morte » | La statistique successorale est déprioritisée depuis 2010 | 16 ans de trou ; Moorea→Fidji ; financement bloqué | Les institutions (CdC) y accèdent | Retenue (connaissance) |
| S3 « Accès à deux vitesses » | Le public ignore, les institutions savent | BNDP (CdC) vs aucune publication | La rec. n° 1 prévoit une diffusion agrégée | Retenue (synthèse) |

**IMPACT_MAP** :

| Acteur | Gain | Perte |
|--------|------|-------|
| DGFiP | Priorité à la gestion (encaissement) | Connaissance statistique |
| Public | — | 35-40 % du flux invisible depuis 2010 |
| Sénat/CdC | Accès exceptionnel (BNDP) | — |
| Notaires | Mention Dutreil = formalité (rec. n° 6) | — |
| État | 21 Md€ encaissés | Décisions fiscales sans connaissance |

**RESPONSIBILITY_MAP** : aucun auteur d'intention n'est établi (BENEFIT != INTENT — la déprioritisation n'est pas documentée comme dissimulation). Rôles : DGFiP (priorités budgétaires), législateur (pas de financement voté), Sénat (recommandations), CPO (alerte). Responsabilité systémique : 16 ans d'ignorance statistique sur le premier flux patrimonial du pays, sans obligation de résultat — la connaissance publique des successions est un choix collectif non fait.

## 13. PÉRIMÈTRE & LIMITES

**Inclusions** : identification de la base (e-enregistrement/DGFiP) ; périmètre (numérisation, donations, mention Dutreil) ; calendrier (S2 2026 → 2029 → 2033) ; interrogeabilité ; BNDP ; écart 35-40 % ; ordres de grandeur. Période 2010-2033.

**Exclusions explicites** : le contenu du rapport Sénat 760 au-delà des recommandations et de l'annexe e-enregistrement (les détails calendaires sont ✧ via chercheur) ; le montant exact du financement manquant ; les micro-données elles-mêmes.

**GAP déclarés** :
- GAP-003 (ACCESS) : partiellement résolu — la base est identifiée (e-enregistrement/DGFiP) et son interrogeabilité est tranchée (non, à court terme) ; reste le montant exact du financement et le calendrier définitif des lots complexes.
- GAP-003b (ACCESS) : **RÉSOLU 10/08/2026 07:26** — corps du rapport Sénat 760 (pages 12-15) lu intégralement (dossier 2026-08-10_07-26_resolution-gap003b-senat760-corps) : citation CPO « quelques dizaines de millions d'euros » confirmée à la source (FCT-007 ✦), lot 3 = 2033 au moins (FCT-006 ✦), DESF = un demi-ETP, écart 35-40 % à la source primaire, 9 000 Md€ (grande transmission).
- GAP-004 (CORPUS) : perspective de la DGFiP absente (MISSING_COUNTER).

## 14. ÉTAT DES CONNAISSANCES

- **CONNU (✦)** : rec. n° 1-6 (texte lu) ; e-enregistrement S2 2026 ; Moorea→Fidji (recentrage gestion) ; 2029 (objectif) ; dernière étude 2010 ; BNDP (source CdC).
- **PROBABLE (✧)** : module statistique bloqué par financement (CPO) ; dons manuels 01/2026 ; assurance-vie ≥ 2033 ; écart 35-40 % ; 21 Md€/250-300 Md€/700 000.
- **HYPOTHÈSE (⁂)** : la déprioritisation statistique est un choix persistant (pas un aléa) ; la mention Dutreil restera inexploitée sans module statistique.
- **CONTESTÉ (⊗)** : l'interprétation du report (aléa technique vs choix de priorité).
- **INCONNU (⁅)** : montant exact du financement ; calendrier définitif des lots complexes ; contenu du corps du rapport.
- **RÉFUTÉ (❧)** : « la France connaît statistiquement ses successions » ; « la base est un chantier abouti ».

## 15. SUSPICION / VÉRIFICATION

**AUDIT DU LEAD** : input UPDATE (identification de la base). Le verdict d'objet est distinct du verdict de lead : « qui/quoi/calendrier/interrogeable ? » reçoit une réponse complète en quatre volets (DGFiP ; trois briques ; 2026-2029-2033 ; non).

**Vérifications contradictoires exécutées** : recommandations n° 1-6 lues intégralement à la source (senat.fr, page r25-7601) ; annexe e-enregistrement lue (r25-76015 : Moorea→Fidji, S2 2026) ; les détails calendaires du chercheur (2033, dons manuels, CPO) marqués ✧ car non relus dans le corps du rapport ; contrôle de cohérence avec le rapport CdC (BNDP, hérité 22-56).

**Verdict final : LA « BASE EN COURS DE CONSTITUTION » EST LA PLATEFORME E-ENREGISTREMENT DE LA DGFiP — RÉELLE POUR LA GESTION, VIRTUELLE POUR LA STATISTIQUE.** La mention Dutreil (rec. n° 6) alimentera une base dont le maillon statistique n'est pas financé : à date, elle ne permettra ni de nommer les 110 ni de lever le secret fiscal (GAP-002) à l'horizon 2026-2028 ; l'accès institutionnel (BNDP/CdC) existe, la connaissance publique non (2010). **Le résultat le plus actionnable : l'écart 35-40 % documenté par le Sénat est la mesure chiffrée de l'opacité — et la rec. n° 3 (2029) fixe le seul horizon où la traçabilité Dutreil pourrait devenir réelle, à condition que le module statistique soit financé.**

---

# ANNEXE A. SOURCES

| SRC-ID | Source | Locator / date | Rôle | URL |
|--------|--------|----------------|------|-----|
| SRC-01 | Sénat, rapport d'information n° 760 (Husson/Raynal), « l'imposition des hauts patrimoines » — recommandations n° 1-6 (texte lu intégralement) | 17/06/2026 | ◈ | https://www.senat.fr/rap/r25-760/r25-7601.html |
| SRC-02 | Sénat 760, annexe e-enregistrement (Moorea→Fidji, déploiement S2 2026 — lue) | 17/06/2026 | ◈ | https://www.senat.fr/rap/r25-760/r25-76015.html |
| SRC-03 | Détails calendaires et chiffres (via chercheur) : CPO (module statistique non financé), décrets 2020/05-2025, dons manuels 01/2026, assurance-vie 2033, écart 35-40 %, 21 Md€/250-300 Md€/700 000, BNDP | 09/08/2026 | ◉ | Sénat 760 (pages 10-15) ; fipeco.fr |
| SRC-04 | INSEE (enquête HVP) ; DGFiP/DESF (études et statistiques — séries de recettes, pas de micro-données depuis 2010) | 2026 | ◉ | https://www.insee.fr ; https://www.impots.gouv.fr/etudes-et-statistiques |
| SRC-05 | Cour des comptes, « Le Pacte Dutreil » (BNDP, partenariat IPP — hérité 22-56) | 18/11/2025 | ◈ | https://www.ccomptes.fr/fr/publications/le-pacte-dutreil-un-dispositif-fiscal-en-forte-croissance-mieux-cibler |

# ANNEXE B. REQUEST_LOG

```
ENGINE:2.8 | MANIFEST:FINAL | RUN_ID:20260809-2325-base-donnees-successions | PARENT_RUN_ID:20260809-2256 | AS_OF:2026-08-09 | INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:NONE
CHECKPOINT_SEQ:0 | LAST_COMPLETED:18b | NEXT_ACTION:NONE | RESUME_COUNT:0
Investigation:base-donnees-successions | complexity:9→COMPLEX | route overrides:NONE | scope:2010-2033, France
modules:KERNEL|SYMBOLS|PATTERNS|THREATS|GATES|REQUEST_LOG|EPISTEMIC|TEMPLATE|INVESTIGATION
degraded:NONE | query target/actual: 5/5 (2 chercheurs + 3 passes basher/lectures)
COUNT: ◈3 ◉2 | unique evidence objects:12 | upstream families:4
LEADS:terminal 1/1 | AXES:terminal 6/6 | N/A:none
FAILURES:0 | FALLBACKS:0
unresolved gaps:GAP-003b RÉSOLU (07:26, corps Sénat 760 pages 12-15 lu), GAP-004 (perspective DGFiP)
```

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL/INPUT_REF |
|---:|---|---|---|---|---|
| 1 | SYS | @MNEMO_Q « base de données successions e-enregistrement » + lecture parent 22-56 | GAP-003 hérité (rec. n° 6 Sénat 760) | 22-56 | investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_dutreil-110-donataires/ |
| 2 | ◈ | QRY-001 (AXS-001/002/003/004) : Sénat 760 — recommandations + annexe e-enregistrement | FOUND : rec. n° 1-6 lues intégralement ; e-enregistrement S2 2026 ; Moorea→Fidji ; 2029 ; mention Dutreil (rec. n° 6) ; DMTG 2010 | SRC-01/02 | senat.fr/rap/r25-760/r25-7601.html ; r25-76015.html |
| 3 | ◉ | QRY-002 (AXS-003/005) : détails calendaires, CPO, écart 35-40 %, BNDP | FOUND (✧) : module statistique non financé (dizaines de M€) ; dons manuels 01/2026 ; assurance-vie ≥ 2033 ; écart 35-40 % ; 21 Md€/250-300 Md€ ; BNDP (CdC) | SRC-03/05 | Sénat 760 ; ccomptes.fr |
| 4 | ◉ | QRY-003 (AXS-004/005) : INSEE/DESF, ordres de grandeur | FOUND (✧) : plus de micro-données depuis 2010 ; ~700 000 actes/an | SRC-04 | insee.fr ; impots.gouv.fr |
| 5 | SYS | Vérification : rec. n° 1-6 relues à la source ; annexe r25-76015 relue ; détails ✧ non relus dans le corps | CONTR-001 à 003 résolus | SRC-01/02 | — |
| 6 | SYS | @MNEMO_S + FACT_WRITEBACK | PENDING_AT_SERIALIZATION | — | — |
| 7 | SYS | STATE:FINAL write | PENDING_AT_SERIALIZATION (ce fichier) | — | investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_dutreil-110-donataires/2026-08-09_23-25_base-donnees-successions-eenregistrement_INVESTIGATION.md |

# ANNEXE C. GATES (G0-G10)

| Gate | Vérification | Résultat |
|------|--------------|----------|
| G0 | Modules chargés ; manifest FINAL ; 15 symboles scorés, aucun ✗ | ✅ |
| G1 | LEAD vs OBJECT distincts ; 6 axes terminaux ; périmètre explicite | ✅ |
| G2 | 5 CLM avec support/counter/gap | ✅ |
| G3 | FACT_REGISTRY 12 faits, statuts canoniques | ✅ |
| G4 | Chaque ✦ → SRC-ID + URL ; ✧ pour corroboration restante (FCT-006/007/008/010/011) | ✅ |
| G5 | CAU-001 à 004 typés, arrêt à l'évidence, CAU-004 rejetée (pas de dissimulation prouvée) | ✅ |
| G6 | CONTROL_MAP + RESPONSIBILITY_MAP ; rôles ≠ responsabilités | ✅ |
| G7 | CONTR-001 à 003 documentés et résolus | ✅ |
| G8 | TRACE_MATRIX ; QRY-001 à 003 tracés ; IDs résolus | ✅ |
| G9 | Manifest FINAL, NEXT_ACTION NONE, aucun PENDING requis | ✅ |
| G10 | Un seul chemin ; une seule write FINAL ; PENDING_AT_SERIALIZATION honnête | ✅ |

**GAP_SEVERITY** : edi_gap = (0.80-0.645)/0.80 = 0.194 ; query_gap = N/A ; coverage_gap = 0. GAP_SEVERITY = 0.194 × 1.00 = 0.19 < 0.20 → procéder avec divulgation (GAP-003b et GAP-004 déclarés).

---

*TL;DR : SUJET : la « base de données en cours de constitution sur les successions » (Sénat 760, rec. n° 6). OBJET : la base est identifiée — la plateforme e-enregistrement de la DGFiP (télétransmission des actes de succession, déploiement progressif S2 2026) avec son module statistique, alimentée par les actes notariés dont la mention Dutreil (rec. n° 6) ; le calendrier : numérisation complète visée en 2029 (rec. n° 3), assurance-vie repoussée à au moins 2033 (✧), dernière étude DMTG représentative = 2010 (16 ans de trou) ; l'interrogeabilité : NON par le public — le module statistique est bloqué par un manque de financement de plusieurs dizaines de M€ (CPO, ✧), aucune micro-donnée publiée depuis 2010, diffusion statistique agrégée seulement (rec. n° 1). Découverte : écart de 35-40 % entre patrimoine transmis déclaré et flux macroéconomiques (assurance-vie et patrimoine professionnel = « angles morts statistiques ») ; la CdC a exploité la BNDP en accès exceptionnel (partenariat IPP) — les données existent, la connaissance publique non. VERDICT : réelle pour la gestion, virtuelle pour la statistique — la traçabilité Dutreil reste suspendue au financement du module ; le GAP-002 (nommer les 110) n'est pas levé par cette base à l'horizon 2026-2028. SOURCE : UPDATE du 22-56 (GAP-003). MANIPULATION : Ξ=9, Ω=8, ↕=8, Κ=8, ⏰=8. LIMITE : détails calendaires via chercheur (✧), corps du rapport non lu (GAP-003b).*
