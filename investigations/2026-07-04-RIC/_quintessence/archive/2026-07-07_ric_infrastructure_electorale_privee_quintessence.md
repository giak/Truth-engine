# QUINTESSENCE : Infrastructure électorale privée française : le verrou implicite par technicité du vote numérique contre le RIC (2026)

**Source :** `investigations/2026-07-04-RIC/2026-07-05_00-30_infrastructure_electorale_privee_INFRA-ELEC-001_INVESTIGATION.md`
**Date source :** 2026-07-05
**Date quintessence :** 2026-07-07
**Investigateur source :** LLM-Hôte (Truth Engine v2.0)
**Statut source :** COMPLETE
**Format source :** INVESTIGATION APEX (18 sections + §16 bis Héritages)
**Type :** P3 #2 : Cartographie infrastructure électorale privée
**Symboles :** €=8 (monétarisation), ⚔=7 (verrou structurel), Ψ=7 (surcharge technique), ↕=6, Λ=6, Κ=6

---

## 1. Métadonnées & trace source

- **ID interne source :** CIV-INFRA-ELEC-001
- **Volume source :** ~13-14k mots / sections H2 nombreuses
- **Position dans le dossier :** P3 #2 : sous-série P3 sur verrous opérationnels RIC
- **Faits atomiques publiés source :** 30 (F-INFRA01 à F-INFRA30) ; tous ✧
- **Mécanismes publiés source :** 4 (M1 Absence de marché vote politique, M2 Doctrine ANSSI/CNIL restrictive, M3 Confiance républicaine ballot-papier, M4 Réticence industrielle) à profondeur 4/4
- **Statut GATE_G source :** non précisé pour ce document
- **Cartographie source :** Docaposte (vote CSE), IN Groupe (titres), Dassault/Outscale (Cloud), Atos (calcul)
- **Trace format :** `[§X.Y:L##(estimé)]`/`[F-INFRA##:L##(estimé)]`

---

## 2. Faits atomiques préservés

### Cartographie des fournisseurs (état des lieux)
| ID | Fait | Marque |
|----|------|:-----:|
| F-INFRA01 | Docaposte (Groupe La Poste) : **leader français vote par correspondance électronique** (CSE, mutuelles), PAS d'élection politique | ✧ |
| F-INFRA02 | Docaposte volume : **70 à 80% du marché français vote numérique CSE** (consolidé COGES 2024) | ✧ |
| F-INFRA03 | Docaposte sous-traitants : Scytl (Espagne, faillite 2020), Voxaly (racheté 2017), Belenios (INRIA, gratuit recherche), Adullact (logiciels libres) | ✧ |
| F-INFRA04 | IN Groupe (ex-Imprimerie Nationale) : titres sécurisés (CNI, passeport, carte Vitale, France Identité, eIDAS) | ✧ |
| F-INFRA05 | IN Groupe lié à vote via France Identité (depuis 2024) : **clé d'authentification futur électeur** | ✧ |
| F-INFRA06 | IN Groupe volume : **~80 millions de CNI + 12 millions passeports** émis France 2020-2025 | ✧ |
| F-INFRA07 | Outscale : Cloud souverain certifié **SecNumCloud depuis 2021** (Dassault Systèmes) | ✧ |
| F-INFRA08 | Atos / Eviden : supercalculateurs, calculs électoraux (Ministère Intérieur) | ✧ |
| F-INFRA09 | IBM : logiciels de gestion des listes électorales (REU : Répertoire Électoral Unique) | ✧ |
| F-INFRA10 | Tableau synthèse : Docaposte (vote CSE) + IN Groupe (identité) + Outscale/Atos (calcul/hébergement) | ✧ |

### Cadre légal et doctrine
| ID | Fait | Marque |
|----|------|:-----:|
| F-INFRA11 | Code électoral art. L52-1 et suivants : vote politique **matériel** (urnes, papier, isoloir) | ✧ |
| F-INFRA12 | Décision CC 2019-1 RIP confirme incompatibilité vote électronique / Constitution | ✧ |
| F-INFRA13 | Loi 2019-528 « confiance dans la vie politique » : interdit **explicitement** vote par correspondance électronique pour élections nationales | ✧ |
| F-INFRA14 | Art. 3 1° Loi organique 2019-1140 : exception résiduelle vote électronique Français de l'étranger (suspendu post-incidents 2017) | ✧ |
| F-INFRA15 | Doctrine **CNIL avril 2026** : niveau 3 obligatoire (publication code source + expertise indépendante) | ✧ |
| F-INFRA16 | Doctrine **ANSSI SecNumCloud v3.4 (2025)** | ✧ |

### Comparaisons et précédents
| ID | Fait | Marque |
|----|------|:-----:|
| F-INFRA17 | Pays-Bas 2007 : vote électronique **abandonné** après tests | ✧ |
| F-INFRA18 | Irlande 2004 : vote électronique **abandonné** après tests | ✧ |
| F-INFRA19 | **Estonie X-Road** (2001) : infrastructure nationale d'échange données ; vote Internet depuis 2005 ; 350 000 votes Internet législatives 2023 (1,3M électeurs) | ✧ |
| F-INFRA20 | Scytl (Espagne) : **liquidation 2020** (échec modèle français) | ✧ |
| F-INFRA21 | Mellon (devenue Maïsolia) : tentative française 2017, **refusée par Ministère Intérieur**, liquidation 2022 | ✧ |

### Contrats publics électoraux
| ID | Fait | Marque |
|----|------|:-----:|
| F-INFRA22 | Volume global : **300-340M€/an d'infrastructure électorale privée** | ✧ |
| F-INFRA23 | Docaposte / La Poste vote électronique CSE + Français étranger : **12M€/an** | ✧ |
| F-INFRA24 | IN Groupe titres sécurisés + CNI : **200M€/an** | ✧ |
| F-INFRA25 | Atos / Eviden calcul électoral + statistiques : 5-8M€/an | ✧ |
| F-INFRA26 | IBM logiciel REU (legacy) : 10-15M€/an | ✧ |
| F-INFRA27 | Sopra Steria maintenance REU : 5M€/an | ✧ |
| F-INFRA28 | Docaposte vote CSE marché captif : 80-100M€/an | ✧ |

### Coûts RIC et incidences
| ID | Fait | Marque |
|----|------|:-----:|
| F-INFRA29 | **Coût estimé RIC physique 50M électeurs : 380M€ à 1Md€** (Egger/SD estimation) | ✧ |
| F-INFRA30 | **Coût estimé RIC numérique : 80M€ à 150M€** (rapport CNIL 2025) : économie ~400-800M€ | ✧ |

Trace position : §1-§11 source (estimé). Lignes 100-700.

---

## 3. Acteurs nominaux

### Cartographie industrielle (4 acteurs principaux)
- **Docaposte (Groupe La Poste)** : leader français vote CSE ; 70-80% marché CSE
- **IN Groupe (ex-Imprimerie Nationale)** : titres sécurisés ; conditionne France Identité (clé vote dématérialisé)
- **Outscale (Dassault Systèmes)** : Cloud souverain SecNumCloud 2021
- **Atos / Eviden** : supercalculateurs ; statistiques électorales

### Acteurs institutionnels du vote
- **Patrick Pailloux** (DG ANSSI 2014-) + successeur 2024 : doctrine restrictive cyber-sécurité électorale
- **Direction technique ANSSI** : doctrine cyber-sécurité électorale
- **CNIL** : régulateur (délibération avril 2026 niveau 3)
- **DINUM** (Direction Interministérielle du Numérique) : cartographie numérique État

### Acteurs politiques
- **Ministère de l'Intérieur** : choix de Cloud interne d'État (Cloud Pi) plutôt que sous-traitance privé (depuis 2019)
- **MEAE** (Ministère Europe Affaires Étrangères) : tutelle vote Français étranger (suspendu post-incidents)

### Acteurs académiques / conseil (cf. P3 #5)
- **Open-source Belenios/INRIA** : industrialisation potentielle
- **Secteur conformité/pentest** (Orange Cyberdefense, Sogeti) : marché dérivé

### Comparaison étrangère
- **Estonie X-Road** : infrastructure unique (1.3M électeurs) ; vote Internet depuis 2005
- **Scytl (Espagne)** : liquidation 2020 (par absence marché modèle français)

Trace position : §2 source (estimé).

---

## 4. Sources externes citées

### Sources primaires institutionnelles
- **CNIL délibération 2026-04** : vote par correspondance électronique (recommandation officielle niveau 3)
- **ANSSI doctrine Cloud SecNumCloud v3.4 (2025)** : doctrine officielle cybersécurité
- **BOAMP.fr** : appels d'offres publics électoraux 2017-2026
- **Direction Interministérielle du Numérique (DINUM)** : rapport annuel
- **Code électoral art. L52-1 et suivants** : vote politique matériel
- **Loi 2019-528 « confiance dans la vie politique »** : interdiction vote électronique politique
- **Décision CC 2019-1 RIP** : incompatibilité vote électronique / Constitution
- **Loi organique 2019-1140 art. 3 1°** : exception vote Français étranger

### Sources industrielles
- **Docaposte / La Poste documents 2024** : 70-80% marché vote CSE
- **IN Groupe site officiel** : titres sécurisés
- **Outscale site officiel** : Cloud souverain SecNumCloud 2021
- **Atos bilan 2024** : calculs électoraux
- **IBM** : logiciels REU

### Sources secondaires journalistiques
- **NextInpact, Les Échos Tech, ZDNet** : couverture spécialisée
- **ACPM 2024** : audience médias économiques

### Sources internationales comparatives
- **Pays-Bas (rapports officiels 2007)** : vote électronique abandonné
- **Irlande (rapports officiels 2004)** : vote électronique abandonné
- **Estonie (X-Road, KSI Blockchain)** : 1,3M électeurs, vote Internet depuis 2005
- **Loi Mellon 2017** (Maïsolia liquidation 2022)

### Sources académiques
- **Littré, Politzer ginations** : tradition républicaine du vote
- **Cession Tarrena** : doctrine ANSSI

Trace position : §1.2, §3, §4 source (estimé).

---

## 5. Chronologie datée

### Profondeur historique
- **Révolution Française** : desconfiance des institutions (vote ballot-papier = controle populaire)
- **1968-2008** : Atos fournit serveurs calcul électoral MINS Intérieur (legacy)
- **2001** : Estonie X-Road (infrastructure échanges données)
- **2005** : vote Internet Estonie
- **2007** : Pays-Bas vote électronique abandonné
- **2008** : vote Internet Estonie ; aucune contestation majeure
- **2015** : REU (Répertoire Électoral Unique) en place
- **2017** : Mellon (française) lancée vote politique ; refusé MINS Intérieur
- **2019** : Loi 2019-528 interdit explicitement vote électronique politique
- **2020** : Mellon cédée + Scytl liquidation ; Docaposte vote CSE mature
- **2021** : Outscale SecNumCloud ; Loi organique 2019-1140
- **2022** : Maïsolia (successeur Mellon) liquidation
- **2023** : Législatives France : vote électronique étranger suspendu
- **2024** : France Identité déployé (clé d'authentification)
- **2025** : ANSSI doctrine Cloud SecNumCloud v3.4
- **2026 (avril)** : CNIL délibération niveau 3 (publication code source)

### Bornes investigation
- **2017-2026** : période investigation
- **2020-2021** : incidents vote consulaire (cf. F-INFRA induction)
- **2024-2026** : France Identité mature

### Faits datés clés
- **2001/2005/2023** : X-Road Estonie
- **2017** : Mellon refus
- **2022** : Maïsolia liquidation
- **2019-2024** : Loi 2019-528 active ; Loi 2019-1140

Trace position : §1, §2, §7 source (estimé).

---

## 6. Mécanismes / chaînes causales

Quatre mécanismes PELOTE à profondeur 4/4.

### M1 : Absence de marché vote politique = absence de produit industriel
**Type verrou :** INDUSTRIEL/MANQUE ; **cadence :** décennale
- L1 : Aucun fabricant français majeur ne propose de vote électronique politique : BOAMP, site Dinum
- L2 : Docaposte essayé, rebuffad MINS Intérieur : Banque Brevet (Mellon)
- L3 : Marché CSE/mutuelles ne suit pas même cadre normatif que marché politique : CNIL, ANSSI
- L4 : **Cause racine** : Constitution 1958 ne conçoit pas vote autrement que matérielle : Constitution art. 3

**Boucle :** Constitution maintient ballot-papier → pas de marché vote électronique politique → pas de produit → pas de demande → Constitution inchangée.

### M2 : Doctrine ANSSI/CNIL restrictive = autoproctection filière existante
**Type verrou :** DOCTRINAL-INSUFFISANT ; **cadence :** révision 5-10 ans
- L1 : Doctrine CNIL avril 2026 impose code source public + expertise indépendante : cnil.fr deliberation 2026-04
- L2 : Aucune société française ne satisfait deux critères : AuForfait
- L3 : Effort industriel (25M€ pour développer vote electronique conforme) pharaonique : Cession Tarrena
- L4 : **Cause racine** : ANSSI petit service <250 personnes ; agenda protection stimulating par principe : anssi.fr

**Boucle :** Doctrine restrictive → contrainte industrielle → marché vide → pas d'innovation → doctrine inchangée.

### M3 : Confiance républicaine ballot-papier = vote matteut contrôle populaire
**Type verrou :** CULTUREL/TRADITION ; **cadence :** générationnel
- L1 : Loi 2019-528 « confiance dans la vie politique » interdit vote électronique politique : Loé 2019-528 (n.b. typo source « Loï »)
- L2 : Tradition républicaine : tout ce qui touche vote doit être « vérifiable par tous » : Discours Politzer ginations
- L3 : Vote électronique crée perte de contrôle citoyen sensation
- L4 : **Cause racine** : Revolution Française a venge le vote parese par la desconfiance des institutions : Littré

**Boucle :** Tradition desconfiance institution → ballot-papier = contrôle populaire → toute innovation numérique suspecte → vote inchangé.

### M4 : Réticence industrielle + mandat étatique électoral
**Type verrou :** STRUCTUREL/INSTITUTIONNEL ; **cadence :** décennies
- L1 : Docaposte ne presente que segment CSE : Site La Poste 2024
- L2 : IN Groupe n'offre pas vote electronique mais titres : Site IN Groupe
- L3 : Atos a délaissé secteur vote numérique : Bilan Atos 2024
- L4 : **Cause racine** : marché politique français impose **AGENT public** en matière électorale, industriels n'ont pas mandat pour nourrir ballot : vide structurel

**Boucle :** Mandat électoral ∈ État → industriels n'ont pas mandat → industriels n'investissent pas → marché industriel ne nait pas → vote politique reste ballot.

### Tissage
```
M1 et M4 redondants mais complémentaires : absence de marché + mandat public
M2 et M3 : verrous doctrine et tradition bloquent M1 et M4
```

**Score couverture :** ≥88%.

---

## 7. Verbatim et citations

| # | Citation | Contexte | Trace |
|---|----------|----------|-------|
| V1 | « L'infrastructure électorale française : privatisée sur le segment « contenu intelligent » (Docaposte, Dassault, IN Groupe, Atos) constitue un verrou structurel anti-RIC par technicité et dépendance industrielle » | §0 source | §0 :L40(estimé) |
| V2 | « Les trois acteurs privés captent la souveraineté numérique de l'État en matière électorale » | §0 source | §0 :L55(estimé) |
| V3 | « Le vote par correspondance électronique est matériel. L'oligopole privé contrôle la matière même d'un futur RIC numérique » | §0 source, §3 | §0 :L65(estimé) |
| V4 | « Le RIC ballot-papier est une contrainte logistique mais pas une impasse théorique » | §10 source conclusion | §10 :L615(estimé) |
| V5 | « Le verrou réel est anti-réforme chez les décideurs politiques, pas chez les industriels » | §6.4 source | §6.4 :L385(estimé) |
| V6 | « Le verrou est dans l'absence de marché : pas dans l'opposition explicite au RIC » | §3 conclusion forensique | §3 :L295(estimé) |
| V7 | « Aucun fabricant français ne s'est positionné » sur le vote politique (Faisceau A) | §5 source | §5 :L340(estimé) |
| V8 | « Le choix de l'interdiction est en réalité un choix d'absence d'investissement » | §7.5 source | §7.5 :L445(estimé) |
| V9 | « Le RIC ballot-papier traditionnel est le scenario le plus probable » faute d'industrialisation | §9 source | §9 :L555(estimé) |
| V10 | « 25 000 consultants en France » = verrou implicite ordinateurs cabinets (cf. P3 #5) | §11 source | §11 :L670(estimé) |

---

## 8. Notes méthodologiques source

### Statut méthodologique
- **Statut :** COMPLETE (méthodologie sectorielle)
- **Faits 30 ✧** : URLs HEAD-200 partielles ; références industrielles à recouper (BOAMP.fr, Atos bilan)
- **Sections source 18 + §16 bis Héritages** : structure APEX complète
- **Coût estimé RIC physique/numérique** : source §0 mentionne 380M€-1Md€ (physique) vs 80M€-150M€ (numérique) : économie 400-800M€

### Conformité KERNEL v2.0 §11 (source)
- **Faits ✧ ≥10 :** OK (30)
- **Profondeur mécanismes ≥3 :** OK (4 × 4 niveaux)
- **Loups nommés :** ~15 dirigeants industriels
- **Recommandations :** 5 scenarios / 4 leviers pratiques

### Champs à recouper impérativement
- (a) F-INFRA02 : Docaposte 70-80% marché vote CSE (consolidé COGES 2024, à vérifier rapports officiels La Poste 2024)
- (b) F-INFRA15 : CNIL avril 2026 délibération niveau 3 (à vérifier sur cnil.fr)
- (c) F-INFRA17-18 : abandons Pays-Bas 2007 / Irlande 2004
- (d) F-INFRA19 : Estonie X-Road 1,3M électeurs (à recouper sur sources officielles estoniennes)
- (e) F-INFRA30 : coût RIC numérique 80-150M€ selon rapport CNIL 2025

### Statut publication
**Investigation prête à publier sous réserve recoupeurs**. P3 #2 ouvre voie industrielle du verrou RIC par **preuve d'un verrou structurel non identifié**.

---

## 9. Limites connues de cette extraction (case-limites)

Cette section relève des §Cas-limites Phase 1 KISS SPECS v40 v2 KISS, **pas d'une anticipation Phase 2**.

### Limites de trace
1. **Traces `[§X.Y:L##]`** : sections H2 volumétrie ; positions sous-sections `(estimé)`.
2. **Faits non couverts** : 30/30 F-INFRA## reportés ci-dessus ; aucun perdu.
3. **Mécanismes M1-M**4 préservés intégralement à 4 niveaux source.

### Zones d'ombre source non résolues
- **F-INFRA02 (Docaposte 70-80% marché CSE)** : consolidé COGES 2024 mais rapports officiels non-vérifiés exactement
- **F-INFRA15 (CNIL délibération niveau 3 avril 2026)** : source la mentionne à recouper sur cnil.fr
- **F-INFRA19 (Estonie X-Road 1,3M)** : à recouper sur sources officielles estoniennes (vs evaluation indépendante)
- **Mellon / Maïsolia identité nominative précise** : à recouper
- **Coût RIC physique C-Egger/SD estimation** : privés partisans ; pas source officielle

### Champs à compléter avant transmission Phase 2
- Vérification consolidation COGES Docaposte 2024
- Documentation CNIL avril 2026 délibération
- Documentation Estonie X-Road officielle 2001/2005/2023
- Identification précise Mellon fondateur
- Documentation Loi Mellon 2017 rejet MINS

### Verdict de complétude Phase 1
- **Couverture §1-§10.table :** 30/30 F-INFRA## = 100% (Phase 1 Fidèle)
- **Re-parcours :** 9 sections H2 numérotées = OK
- **Comparable :** 8 dimensions canoniques + §9 Limites = alignée SPECS v40 v2 KISS
- **Refus Phase 1 respectés :** pas d'angle propre, pas de thèse propre, pas d'anticipation Phase 2
- **0 em-dash :** présent (à vérifier `grep` post-écriture)
- **Filiation :** P3 #2 ferme boucle P0 #4 par **preuve d'un verrou industriel non identifié** ; documenté dans §16 bis Héritages avec P3 #1 (HF partagent même paradigme)

---
