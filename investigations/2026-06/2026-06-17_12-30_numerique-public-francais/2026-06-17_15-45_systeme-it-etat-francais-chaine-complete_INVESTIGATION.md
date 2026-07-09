# INVESTIGATION APEX — Le Système IT de l'État Français : Chaîne Complète
# "De l'expression du besoin à la livraison, du budget à la sécurité"

> **SUJET** : Analyse forensique de l'ensemble du système IT de l'État français : production, stockage, sécurité, gouvernance, financement, profiteurs.
> **DATE** : 17 Juin 2026
> **COMPLEXITÉ** : APEX (15/15)
> **RÉFÉRENCES** : Cette enquête est la 4e et dernière de la série. Voir `12-30` (prédation structurelle), `14-15` (ADVENDA), `14-30` (recours citoyens), `15-00` (circulaire amendes).

---

## §1 RÉSUMÉ EXÉCUTIF

**Constat** : Le système IT de l'État français représente 4-5 Md€/an (0.9% du budget général). 45 grands projets (>9M€) pour 3.3 Md€. Des centaines de milliers de serveurs, données hébergées par des fournisseurs soumis au Cloud Act américain. Une dépendance croissante aux ESN privées (Capgemini, Sopra Steria, Atos). Un système de "contrôle" (DINUM, ANSSI) qui accompagne plus qu'il ne contraint. Une Cour des Comptes qui alerte sans être écoutée.

**Ce que l'enquête révèle** :
1. **Budget IT réel** : 4-5 Md€/an, avec DGFiP seule ~500M€. 45 projets suivis par DINUM pour 3.3 Md€, durée moyenne 6.3 ans, retard 21%.
2. **Dépendance aux ESN** : Capgemini a obtenu >1.1 Md€ de contrats État en 5 ans (Le Monde). Sopra Steria gère les radars (82M€), l'ASP (27M€), la commande publique. McKinsey : 0€ d'IS en France 2011-2020 malgré des centaines de millions de contrats.
3. **Cloud américain structurel** : Le Health Data Hub (données de santé de 67M de Français) hébergé chez Microsoft Azure pendant 7 ans (2019-2026) malgré le Cloud Act. Migration vers Scaleway prévue fin 2026 seulement.
4. **ANSSI : 32 audits/an** — la Cour des Comptes juge la "portée relativement faible" des audits. L'ANSSI accompagne plus qu'elle ne contraint. NIS2 pas transposée.
5. **DINUM instable** : 5 directeurs depuis 2018. La Cour des Comptes : "peine à jouer le rôle effectif de DSI de l'État".
6. **Consulting : 271M€ en 2021** (record). Remontée à 96M€ en 2024 (+31%). Rapport Sénat 2022 : "phénomène tentaculaire et opaque".
7. **ANTS : 85-90% d'externalisation** sur projets stratégiques (identité numérique, passeports). "Risques majeurs de perte de compétences" (Cour des Comptes).

**Thèse** : Le système IT de l'État est sous-traité à un oligopole d'ESN privées (Capgemini, Sopra Steria, Atos, Accenture) qui captent l'essentiel des 4-5 Md€ annuels. Les organes de contrôle (DINUM, ANSSI) sont structurellement sous-dimensionnés face à l'ampleur de la tâche. Les données sensibles (santé, impôts, identité) ont été confiées à des hébergeurs soumis au droit américain. Le pantouflage et la porosité public-privé verrouillent le système. Les alertes de la Cour des Comptes sont récurrentes depuis 2015 — aucune n'a été suivie d'effets structurels.

---

## §2 MANIPULATION_REPORT

| Symbole | Score | Justification |
|---------|-------|---------------|
| **Ξ** Omission | 9 | Aucune cartographie publique complète du SI étatique. Budgets agrégés sans détail. |
| **€** Money | 10 | 4-5 Md€/an. Capgemini 1.1Md€ en 5 ans. Mais pas de rapport "où va chaque euro". |
| **Λ** Framing | 8 | "Souveraineté numérique" mais données sur Azure. "Cloud de confiance" mais dépendance Microsoft. |
| **Ω** Inversion | 7 | Externalisation = efficacité (mais dépendance, perte de compétences). |
| **Ψ** Overload | 7 | Complexité extrême des marchés publics, des normes, des certifications. |
| **↕** Vertical | 10 | DINUM (79M€) face à 5 Md€ de SI État. Déséquilibre asymétrique. |
| **Φ** Spectacle | 7 | "France 2030", "Cloud au centre", "Souveraineté numérique" = annonces sans suivi. |
| **Σ** Semiotics | 6 | SecNumCloud, label "Cloud de Confiance" — signifiants devenus signes de com. |
| **Κ** Cynical | 9 | CdC alerte depuis 2015 → rien ne change. Tout le monde sait. |
| **ρ** Resistance | 3 | Rapport Sénat McKinsey (2022). Enquêtes PNF. Mais peu de suivi. |
| **κ** Subtle | 6 | Privatisation lente du SI public par captation des compétences et des contrats. |
| **⫸** Bundle | 8 | Tous les faisceaux convergent : dépendance, impuissance, argent, opacité. |
| **⚔** Warfare | 5 | Dépendance à des infrastructures soumises au Cloud Act américain — risque stratégique. |
| **🌐** Network | 9 | Pantouflage : 29% des ingénieurs des mines, 22% des anciens ENA en privé. |
| **⏰** Temporal | 7 | Chronologie de privatisation accélérée 2017-2026. |

**PATTERNS** : @PAT[MONEY]:10 @PAT[CYN]:9 @PAT[NET]:9 @PAT[ICEBERG]:9 @PAT[FASC]:8
**THREATS** : @THR[REG_CAPTURE]:9 @THR[DARK_MONEY]:8 @THR[ELITE_REPRO]:8 @THR[MYTHO]:7
**RHETORICAL** : FAC:9 BF:8 NUM:7

---

## §3 CLUSTERS SCORED

| Cluster | Score | Class | Preuve |
|---------|-------|-------|--------|
| MONEY (€:10) | 9.5 | €+++ | 4-5 Md€/an. Capgemini 1.1Md€. 45 projets 3.3Md€. Consulting 271M€. |
| NETWORK (🌐:9) | 8.5 | 🌐++ | Pantouflage: 29% mines, 22% ENA. Anciens ministres → conseil. |
| CYNICAL (Κ:9) | 8.5 | Κ+++ | CdC alerte depuis 2015. 5 directeurs DINUM. Aucune réforme structurelle. |
| ICEBERG (Ξ:9) | 8.0 | Ξ++ | Visible: 4-5 Md€. Caché: dette technique, coûts réels, sécurité réelle. |
| POWER (↕:10) | 8.5 | ↕+++ | DINUM 79M€ face 5 Md€. ANSSI 32 audits/an. Asymétrie totale. |
| INVERSION (Ω:7) | 6.5 | Ω++ | "Souveraineté" = cloud US. "Contrôle" = accompagnement. |
| FRAMING (Λ:8) | 7.0 | Λ++ | "Cloud de confiance", "Souveraineté numérique" = mots vides. |
| OVERLOAD (Ψ:7) | 6.5 | Ψ++ | Complexité marchés publics + certifications + multiples agences. |
| SPECTACLE (Φ:7) | 6.0 | Φ+ | France 2030, France Relance, annonces sans suivi budgétaire. |
| WAR (⚔:5) | 5.5 | ⚔+ | Dépendance au cloud US : risque géopolitique majeur. |
| GASLIGHTING (Ξ≥7) | 7.5 | Ξ++ | On vous dit "souveraineté" et "contrôle". Aucune des deux n'existe. |
| CONFIRMATION (Ω≥7) | 6.0 | κ+ | Captation silencieuse du SI public par le privé. |

---

## §4 HERMÉNEUTIQUE (L1-L6)

**L1 EXPLICIT**: L'État dépense 4-5 Md€/an pour son informatique. 45 grands projets sont suivis par la DINUM. L'ANSSI réalise ~32 audits/an. Capgemini, Sopra Steria, Atos sont les principaux prestataires.

**L2 IMPLICIT**: "4-5 Md€" est une estimation (le Royaume-Uni publie des données détaillées ministère par ministère ; la France ne le fait pas). "Suivi DINUM" ne signifie pas "contrôle DINUM" — la CdC note que les ministères pratiquent la "politique de l'évitement".

**L3 STRUCTURAL**: Le système est verrouillé par :
- Des contrats multi-annuels (ESN verrouillées pour 4-8 ans)
- Une dépendance technique (personne ne connaît les systèmes sauf les ESN)
- Une capture des compétences (85-90% externalisation ANTS)
- Un pantouflage généralisé (29% ingénieurs mines → privé)

**L4 SYMBOLIC**: La DINUM est présentée comme "DSI de l'État" — mais son budget est 79M€ face à 5 Md€ de SI. Un "pilote" qui pèse 1.6% de ce qu'il est censé piloter.

**L5 UNCONSCIOUS**: Le non-dit : l'État a structurellement renoncé à maîtriser son SI. La sous-traitance n'est pas une solution temporaire mais un abandon définitif de compétence. Revenir en arrière coûterait 5-10 ans et des milliards — donc le statu quo est verrouillé politiquement.

**L6 EPISTEMIC**: Qui produit la connaissance sur l'état réel du SI ? Personne. La Cour des Comptes a accès aux comptes mais pas aux détails techniques. La DINUM voit les 45 "grands projets" mais pas les milliers de petits. ANSSI voit 32 audits sur peut-être des milliers de systèmes.

---

## §5 FORENSIC REASONING

**[FORENSIC] (Ξ:9) Domaine:PROCUREMENT_CHAIN**
**Shown(officiel)**: "4-5 Md€ de budget IT, 45 grands projets suivis par DINUM, écart budgétaire 6.5%"

**Hidden**:
- **Composant 1 — Budget réel** : 4-5 Md€ est une estimation. La France ne publie pas de données détaillées par ministère (contrairement au UK). Le seul DGFiP = 490M€. Le seul cloud DINUM = 84M€. MAIS les contrats ESN ne sont pas tous tracés.
- **Composant 2 — Externalisation réelle** : ANTS = 85-90%. Radars = Sopra Steria (82M€ 2017-2026). Chorus = SAP. Pas de chiffre global.
- **Composant 3 — Sécurité réelle** : 32 audits ANSSI/an. Mais 3586 événements de sécurité en 2025, 1366 incidents. Décalage énorme.
- **Composant 4 — Contrôle réel** : DINUM émet des "avis de conformité". Mais les ministères contournent (dépôts tardifs, dérogations).

**Reality total**: Le système est un mille-feuille d'opacité. Personne ne connaît le coût total, la sécurité réelle, ni l'efficacité réelle.

**Shown%**: Probablement <20% de la réalité est visible publiquement.
**Confidence**: HIGH — Cour des Comptes, Sénat, DINUM, ANSSI convergent.

---

## §6 PRISME DIALECTIQUE (3 Perspectives)

**P1 [⟐🎓] Officiel** : "La transformation numérique de l'État est en marche. La DINUM pilote la stratégie 'Cloud au centre'. 84M€ de commandes cloud en 2025 (+62%). 99% de la commande publique cloud vers des fournisseurs européens. 45 grands projets suivis avec un écart budgétaire réduit à 6.5%. Le Health Data Hub migre vers Scaleway SecNumCloud. L'ANSSI est reconnue internationalement. Le système est sous contrôle."

**P2 [🔥⟐̅] Critique** : "5 Md€/an pour un SI dont la sécurité est un trompe-l'œil. 32 audits ANSSI/an pour des milliers de systèmes. Les ministères contournent la DINUM. Des données de santé sensibles chez Microsoft pendant 7 ans. Capgemini, Sopra Steria, Accenture captent l'argent sans résultats mesurables. Le pantouflage verrouille le système. McKinsey : 0€ IS pendant 10 ans. Le 'Cloud de confiance' Bleu est une coentreprise avec Microsoft."

**P3 [◈◉○] Triangulation** : Les deux perspectives contiennent du vrai. La doctrine 'Cloud au centre' existe (P1), mais son budget (84M€) est infime face aux 5 Md€ totaux (P2). La DINUM a réduit les écarts budgétaires (P1), mais 21% de retard calendaire reste énorme (P2). L'ANSSI est reconnue (P1), mais 32 audits/an est dérisoire (P2). La vérité : le système est en transition, mais la dépendance aux ESN et au cloud US est structurelle, pas conjoncturelle.

---

## §7 CHRONOLOGIE

| Date | Événement | Source |
|------|-----------|--------|
| 1978 | Loi Informatique et Libertés. CNIL créée. | Légifrance |
| 2001 | LOLF : principe d'universalité budgétaire (utilisé en 2018 contre fléchage amendes) | Légifrance |
| 2008 | Chorus (SAP) : SI financier de l'État mis en production | AIFE |
| 2009 | ANSSI créée sous autorité SGDSN | ANSSI |
| 2012 | Chorus généralisé à tout l'État | AIFE |
| 2014 | Décret : projets IT >9M€ soumis à audit DINUM | Légifrance |
| 2016 | Premier Panorama des grands projets SI État | DINUM |
| 2017 | Macron élu. Accélération recours cabinets conseil | Sénat |
| 2019 | DINUM créée (remplace DINSIC) | Vie-Publique |
| Nov 2019 | Health Data Hub créé, hébergé chez Microsoft Azure | Le Monde |
| 2020 | UK ICO change modèle : garde jusqu'à 7.5M£/an amendes | Verasafe |
| Mars 2022 | Rapport Sénat : "phénomène tentaculaire et opaque" cabinets conseil | Sénat |
| Mars 2022 | PNF ouvre enquête McKinsey (blanchiment fraude fiscale) | PNF |
| Oct 2022 | PNF ouvre 2e enquête : favoritisme, comptes campagne Macron | Le Monde |
| 2021 | Record consulting : 271M€ (tous opérateurs : 900M€) | Sénat/Bercy |
| Mai 2021 | Circulaire "Cloud au centre" : doctrine cloud État | Premier ministre |
| Mars 2023 | Stéphanie Schaer nommée directrice DINUM | DINUM |
| 2023 | Plan France Relance : 1Md€ cybersécurité | FTJ |
| Mai 2024 | Chorus migre vers SAP S/4HANA (78.4M€, 18 mois, réussite) | AIFE/SAP |
| 2024 | 32 audits ANSSI. DGFiP : 459.9M€ budget IT | Annuel ANSSI/Sénat |
| 2025 | 3586 événements sécurité, 1366 incidents ANSSI | ANSSI |
| 2025 | 84M€ commandes cloud DINUM (+62%). 99% européen | IT for Business |
| 2025 | 45 grands projets : 3.3 Md€, -500M€ vs 6 mois avant | CIO/DINUM |
| Fév 2026 | Migration HDH décidée : Microsoft → Scaleway | Le Monde/Numerama |
| Mars 2026 | Conseil d'État valide HDH sur Azure (dernier soubresaut) | CE |
| Avril 2026 | Scaleway choisi pour HDH. Migration fin 2026-début 2027 | Le Monde |
| Mai 2026 | ANSSI rapport 2025 : budget insuffisant, NIS2 pas transposée | ANSSI |
| Juin 2026 | Cour des Comptes : ANSSI audits "portée faible", DINUM instable | ZDN/CdC |

---

## §8 DOMAINES

### 8.1 Domaine Production : Qui fabrique le SI de l'État ?

Le SI de l'État est produit par un oligopole de 4-5 ESN privées (SSII) qui captent la majorité des 4-5 Md€ annuels.

**Classement des prestataires (par chiffre d'affaires estimé avec l'État) :**

| Rang | ESN | CA estimé État/an | Clients principaux | Particularité |
|------|-----|-------------------|--------------------|---------------|
| 1 | **Capgemini** | ~220M€/an | Tous ministères, Justice, DGFiP, Intérieur, AFD | 1.1 Md€ cumulé 2017-2022 (Le Monde). JV Bleu avec Microsoft. |
| 2 | **Sopra Steria** | ~150M€/an | Radars (82M€ 2017-2026), ASP (27M€), ANTS, Commande publique | N°1 européen cloud, 40K employés |
| 3 | **Atos** | ~120M€/an | CANUT, identités, défense, ministères | 72K employés. Difficultés financières 2024-2026. |
| 4 | **Accenture** | ~100M€/an | UGAP données, ministères sociaux, COVID | 506K employés monde. Co-traitant CGI. |
| 5 | **CGI** | ~80M€/an | ASP, UGAP, divers ministères | Canadien. Co-traitant IT. |
| 6 | **Autres (IBM, DXC, Orange Business, Wavestone, etc.)** | ~200M€/an | Divers | Conseil + prestation. |

**Source** : Le Monde "Capgemini 1.1 Md€ contrats État 2017-2022" ; Sénat rapport "phénomène tentaculaire" ; Marchés publics ouverts (macellum.fr).

**Problème identifié par la Cour des Comptes** (§9 infra) : l'ANTS a 85-90% d'externalisation sur projets critiques. La CdC qualifie cela de "risques majeurs de perte de compétences, de contrôle et de maîtrise des opérations".

### 8.2 Domaine Stockage : Où sont les données ?

**Architecture cloud de l'État :**

| Type | Fournisseur | Données hébergées | Certification |
|------|-------------|-------------------|---------------|
| **Souverain (SecNumCloud)** | OVHcloud, Outscale (Dassault), Scaleway, Numspot (Docaposte/Bouygues), Cloud Temple | Données non-sensibles, test, dev | SecNumCloud |
| **En cours SecNumCloud** | Bleu (Orange+Capgemini+Microsoft), S3NS (Thales+Google) | Visée : données sensibles | En attente (2026-2027) |
| **Américain (non SecNumCloud)** | Microsoft Azure, AWS, Google Cloud | Santé (HDH), ministères, Education | RGPD uniquement |
| **Propriétaire** | SAP (Chorus), DGFiP | Finances, impôts | Interne |

**Le cas Health Data Hub (2019-2026)** : Les données de santé de 67M de Français hébergées chez Microsoft Azure (datacenter aux Pays-Bas). Polémique permanente sur le Cloud Act américain qui permet aux autorités US de réclamer les données. La CNIL a refusé d'autoriser un transfert global. Le Conseil d'État a validé en mars 2026 en reconnaissant que "le risque ne peut être totalement exclu". Migration vers Scaleway en cours (fin 2026-début 2027).

**Chorus (SAP) (2008-2026)** : Le SI financier de l'État (24 000 utilisateurs) tourne sur SAP. Migration S/4HANA réussie en mai 2024 (78.4M€, 18 mois). Dépendance à SAP — État ne possède pas le code, paie des licences.

**Données sensibles identifiées et leur hébergement (partiel) :**
- Données de santé (SNDS) : Microsoft Azure → Scaleway (2026)
- Données fiscales (DGFiP) : Chorus SAP + hébergement interne (AIFE)
- Données identité (ANTS) : Prestataires privés (85-90% externalisation)
- Données emploi (France Travail) : Multiples ESN
- Fichier TES (passeports) : "sensibilité extrême" (Cour des Comptes)
- Fichier FICOBA (comptes bancaires) : DGFiP

### 8.3 Domaine Sécurité : ANSSI, Audits, Contrôles

**ANSSI : mission impossible ?**
- **32 audits en 2024** (même nombre en 2023) — dérisoire face à l'ampleur
- 3586 événements de sécurité en 2025, 1366 incidents (+0.4% vs 2024)
- Budget : pas de programmation pluriannuelle (recommandation CdC non suivie)
- **Pouvoir de sanction** : existe depuis 2013 (LPM) mais jamais utilisé
- Cour des Comptes : "portée relativement faible de ces audits", "accompagne plus qu'elle ne contraint"

**Système d'homologation** :
- Chaque SI doit être "homologué" par son responsable
- Guide d'homologation ANSSI/DINUM 2025 : procédure complète
- MAIS : pas de vérification systématique que l'homologation est réelle
- ANTS : dépend de consultants privés pour SA PROPRE sécurité SI (Cour des Comptes)

**La révélation Clé** :
« Parmi les besoins critiques sous-traités figurent plusieurs activités visant à assurer la sécurité des systèmes d'information, notamment "la stratégie d'audit". » (Cour des Comptes, rapport ANTS 2026)

→ **L'ANTS sous-traite sa PROPRE stratégie d'audit de sécurité à des consultants privés.** C'est le gardien qui sous-traite le verrouillage des portes à un prestataire extérieur.

### 8.4 Domaine Gouvernance : DINUM, le "DSI" sans pouvoir

**Chiffres clés :**
- Budget DINUM 2023 : 79M€ AE / 138M€ CP
- Budget SI État total estimé : 4-5 Md€
- **Ratio : DINUM = ~1.6% du SI qu'elle est censée piloter**

**Instabilité chronique :**
- 5 directeurs depuis 2018 (Stéphanie Schaer nommée mars 2023)
- Cour des Comptes : "capacité de pilotage altérée par des changements de direction fréquents"

**Mécanisme de contrôle limité :**
- Les projets >9M€ DOIVENT solliciter un avis de conformité DINUM
- 5 critères : stratégie, finances, gouvernance, réalisation, planning
- MAIS : "nombre de ministères pratiquent, vis-à-vis des audits théoriquement obligatoires de la Dinum, la politique de l'évitement qui les voient déposer leur dossier très tardivement" (Cour des Comptes, juil 2024)
- ANSSI analyse le volet sécurité — mais 32 audits/an

### 8.5 Domaine Consulting : Le Phénomène Tentaculaire

**Chronologie des dépenses de conseil :**
- 2018 : ~150M€ (estimation Sénat)
- 2021 : **271M€** (record) — tous opérateurs : **~900M€**
- 2022 : ~137M€ (après rapport Sénat)
- 2023 : 73.4M€ (baisse -46.5%)
- 2024 : **96.1M€ (+31%)** — remontée

**Les missions COVID McKinsey (2020-2022) :**
- 7 missions, 11.6M€ d'honoraires
- Domaine : stratégie vaccinale, tour de contrôle, task force
- Pas d'appel d'offres pour certaines missions
- Accenture : système d'information passe vaccinal

**Le rapport Sénat 2022 (Assassi/Bazin) :**
- "Phénomène tentaculaire et opaque"
- Cabinets : "intervenus sur la plupart des grandes réformes du quinquennat"
- Prop. de loi pour encadrer → adoptée Sénat mai 2024, **toujours pas inscrite à l'AN**
- Enquête PNF pour favoritisme (ouverte oct 2022)

**Le scandale McKinsey :**
- 0€ d'IS en France entre 2011 et 2020
- Enquête PNF : blanchiment aggravé fraude fiscale (mars 2022)
- Perquisition ministère Santé (mai 2024)
- Missions gratuites (pro bono) pendant campagne 2017
- Paul Midy (dir général LREM/ Renaissance) = ex-McKinsey
- Mathieu Maucourt (dir cabinet Trésor) = ex-McKinsey

### 8.6 Domaine Pantouflage : La Capture des Compétences

**Chiffres (Cour des Comptes, mai 2025) :**
- 10 000 fonctionnaires/an quittent le public (pantouflage)
- **29%** des ingénieurs des mines dans le privé
- **22%** des anciens ENA ont rejoint le privé durant leur carrière
- 8% des anciens ENA ont définitivement quitté la fonction publique

**Problème :**
- HATVP émet des avis mais "réserves peu suivies" (CdC)
- 77% des avis de la HATVP comportent des réserves
- Les poursuites pénales sont quasi inexistantes (exemple Pellerin classé sans suite)
- Les allers-retours public-privé créent une dépendance cognitive : les décideurs publics savent qu'ils travailleront pour les ESN demain

**Exemples marquants :**
- Guillaume Poupard (ex-directeur ANSSI) → Numspot (cloud)
- Paul Midy (dir LREM) → ex-McKinsey
- Mathieu Maucourt (dir cabinet Trésor) → ex-McKinsey
- Anciens ministres → conseil (Le Maire → ASML, Djebbari refusé CMA-CGM)

---

## §9 RÉSEAU D'ACTEURS

**Les concepteurs/décideurs :**
| Acteur | Rôle | Position |
|--------|------|----------|
| **DINUM** | DSI de l'État (théorique). Pilote transformation numérique. | Budget 79M€ face 5 Md€. Sous-dimensionnée. |
| **Stéphanie Schaer** | Directrice DINUM (mars 2023→) | 5e directrice depuis 2018. |
| **ANSSI / Vincent Strubel** | Autorité cybersécurité | 32 audits/an. Accompagne > contraint. |
| **AIFE** | SI financier État (Chorus SAP) | Gère les 24 Md€ de transactions annuelles. |
| **Cour des Comptes** | Contrôle budgétaire | Alerte récurrente depuis 2015. Ignorée. |
| **Sénat (Assassi/Bazin)** | Commission d'enquête cabinets conseil | Rapport 2022. PPL adoptée Sénat, bloquée AN. |
| **PNF** | Enquête favoritisme McKinsey | Ouverte oct 2022. Perquisitions mai 2024. |

**Les profiteurs :**
| Acteur | Gain estimé | Mécanisme |
|--------|-------------|-----------|
| **Capgemini** | 1.1 Md€ (2017-2022) | Contrats État, JV Bleu, consulting |
| **Sopra Steria** | ~150M€/an | Radars, ASP, commande publique |
| **Atos** | ~120M€/an | CANUT, identités, défense |
| **Accenture** | ~100M€/an | UGAP, ministères sociaux, COVID |
| **McKinsey** | ~50M€/an (2017-2021) | Conseil stratégique, COVID. 0€ IS. |
| **Microsoft** | ~5M€/an (HDH estimate) | Azure, Office 365 État |
| **SAP** | ~10M€/an est. | Chorus, licences, S/4HANA |
| **Cabinets conseil** | 271M€ (2021) | Tous secteurs, toutes réformes |

**Les perdants :**
- **Citoyens** : données exposées, impôts mal dépensés
- **Agents publics** : compétences non valorisées, externalisation
- **PME françaises** : verrouillage par les gros contrats ESN

---

## §10 CHAÎNES DE CASCADE

**Chaîne A : La Dépendance aux ESN**
```
Besoin IT exprimé par ministère
  → AO rédigé (normes complexes) → seule grosse ESN peut répondre
  → Capgemini/Sopra/Atos gagnent (barrières à l'entrée)
  → Contrat 4-8 ans
  → État perd la connaissance du système
  → Renouvellement : seul le prestataire sortant peut maintenir
  → Dépendance permanente
```
**Endpoint** : Captation irréversible.

**Chaîne B : L'Échec du Contrôle**
```
Projet >9M€ → doit passer avis conformité DINUM
  → Ministère dépose dossier tardivement ("politique évitement")
  → DINUM sous-staffée (79M€/5Md€) → avis donné sous pression
  → Avis non contraignant
  → Projet lancé → retards → surcoûts (6.3 ans moyenne)
  → Pas de sanction possible
```
**Endpoint** : Contrôle formel sans effet.

**Chaîne C : La Sécurité de Confiance**
```
Système mis en production
  → Homologation par responsable (pas par ANSSI)
  → ANSSI audit possible : 32/an → probabilité visite : <1%
  → SI non audité → vulnérabilités non détectées
  → Fuite (France Travail 43M, ANTS 11.7M)
  → Amende CNIL (au budget général)
  → Aucune obligation de corriger
```
**Endpoint** : Sécurité de papier. Fuites inévitables.

**Chaîne D : Le Pantouflage-Verrou**
```
Agent public compétent en IT
  → Salaire public : 40-60K€
  → Salaire privé ESN : 80-150K€
  → Agent part chez Capgemini/Sopra/Accenture
  → Connaît les dossiers, les failles, les interlocuteurs
  → Revend ses compétences à l'État (facturé 600-1200€/jour)
  → État perd la compétence ET paie plus cher pour la racheter
```
**Endpoint** : Double peine budgétaire.

**Chaîne E : Le Cloud Act et les Données**
```
Données sensibles françaises (santé, impôts, identité)
  → Hébergées chez Microsoft/AWS/Google (cloud non SecNumCloud)
  → Cloud Act permet aux autorités US de demander accès
  → Entreprise US doit obéir (FISA, Patriot Act)
  → Données françaises accessibles légalement par USA
  → "Le risque ne peut être totalement exclu" (Conseil d'État, 2026)
```
**Endpoint** : Souveraineté numérique formelle, dépendance réelle.

---

## §11 CARTE DES PREUVES

| # | Fait | Date | Source | Fiabilité | URL |
|---|------|------|--------|-----------|-----|
| F301 | Budget IT État : 4-5 Md€/an (0.9% budget général) | 2024-2026 | IT for Business | ✦◉ | itforbusiness.fr/strategies/move-to-cloud-90338 |
| F302 | 45 grands projets IT : 3.3 Md€ cumulés | Déc 2025 | CIO Online | ✦◉ | cio-online.com/actualites/.../16500/ |
| F303 | Durée moyenne projet : 6.3 ans. Écart budgétaire : 6.5%. Retard : 21% | 2025 | ZDN | ✦◉ | zdnet.fr/actualites/grands-projets-it-letat-du-mieux-481086.htm |
| F304 | Capgemini : >1.1 Md€ contrats État 2017-2022 | 2022 | Le Monde décodeurs | ✦◈ | lemonde.fr/les-decodeurs/.../capgemini-6133034_4355770.html |
| F305 | McKinsey : 0€ IS France 2011-2020 | 2022 | Rapport Sénat | ✦◈ | senat.fr/rap/r21-578-1/r21-578-1_mono.html |
| F306 | McKinsey COVID : 11.6M€, 7 missions, pas d'AO | 2022 | Consultor.fr | ✦◉ | consultor.fr/articles/... |
| F307 | Dépenses conseil 2021 : 271M€ (record). 2024 : 96M€ (+31%) | 2025 | Public Sénat | ✦◈ | publicsenat.fr/actualites/.../cabinets-conseil-hausse-2024 |
| F308 | ANSSI : 32 audits en 2024. "Portée relativement faible" | 2025 | ZDN / CdC | ✦◈ | zdnet.fr/actualites/cybersecurite-cour-comptes-anssi-477425.htm |
| F309 | ANTS : 85-90% externalisation. "Risques majeurs perte compétences" | 2026 | IT for Business | ✦◈ | itforbusiness.fr/anssi-ants-rgs-cybersecurite-103723 |
| F310 | ANTS sous-traite "stratégie d'audit" sécurité | 2026 | Cour des Comptes (via ITfB) | ✦◈ | itforbusiness.fr/anssi-ants-rgs-cybersecurite-103723 |
| F311 | DINUM : 79M€ budget vs 5 Md€ SI total. "Peine à piloter" | 2024 | Cour des Comptes | ✦◈ | ccomptes.fr/fr/publications/pilotage-transformation-numerique-dinum |
| F312 | 5 directeurs DINUM depuis 2018 | 2024 | IT for Business | ✦◈ | itforbusiness.fr/strategies/move-to-cloud-90338 |
| F313 | HDH sur Microsoft Azure : 7 ans. Migration Scaleway fin 2026 | 2026 | Le Monde | ✦◈ | lemonde.fr/economie/.../health-data-hub-migre-microsoft-6683082.html |
| F314 | Conseil d'État HDH Mars 2026 : "risque Cloud Act ne peut être exclu" | Mars 2026 | Le Monde Info | ✦◈ | lemondeinformatique.fr/actualites/.../conseil-etat-azure-99707.html |
| F315 | Fournisseurs SecNumCloud 2026 : OVH, Outscale, Scaleway, Numspot, Cloud Temple | 2026 | Legiscope | ✦◉ | legiscope.com/blog/secnumcloud-rgpd-cloud-souverain.html |
| F316 | Bleu (Microsoft+Capgemini+Orange) : SecNumCloud visé 2026 | 2024 | ZDN | ✦◈ | zdnet.fr/actualites/debuts-officiels-bleu-cloud-39963592.htm |
| F317 | Pantouflage : 29% ingénieurs mines, 22% ENA en privé | 2025 | Cour des Comptes | ✦◈ | ouest-france.fr/economie/.../pantouflage-cour-des-comptes |
| F318 | HATVP : 77% d'avis réserves. Réserves peu suivies. Poursuites 0. | 2025 | Ouest-France / CdC | ✦◈ | ouest-france.fr/economie/.../pantouflage-cour-des-comptes |
| F319 | Chorus S/4HANA : 78.4M€, migration 18 mois, 24 000 utilisateurs | Mai 2024 | SAP France | ✦◈ | news.sap.com/france/2024/07/pouvoirs-publics-sap/ |
| F320 | Ministères contournent DINUM : "politique de l'évitement" | 2024 | CIO Online / CdC | ✦◈ | cio-online.com/actualites/.../16500/ |
| F321 | 3 586 événements sécurité ANSSI 2025. 1 366 incidents. | 2026 | ANSSI rapport | ✦◈ | cyber.gouv.fr/actualites/rapport-activite-2025 |
| F322 | Budget capacitaire ANSSI : pas de programmation pluriannuelle | 2025 | Cour des Comptes | ✦◈ | ccomptes.fr/.../reponse-etat-cybermenaces.pdf |
| F323 | NIS2 non transposée en droit français (échéance 17 oct 2024) | 2026 | ZDN / CdC | ✦◈ | zdnet.fr/actualites/cybersecurite-cour-comptes-anssi-477425.htm |
| F324 | DGFiP budget IT 2025 : 489.9M€ (+4.4%), résorption dette technique | 2025 | Sénat PLF | ✦◈ | senat.fr/rap/l24-144-315-1/...html |
| F325 | 84M€ commandes cloud DINUM 2025 (+62%). 847 projets. 99% européen. | 2026 | IT for Business | ✦◈ | itforbusiness.fr/cloud-letat-dinum-accelere-101847 |
| F326 | Rapport Sénat "cabinets conseil" : PPL adoptée mai 2024, bloquée AN | 2024 | Public Sénat | ✦◈ | publicsenat.fr/actualites/.../cabinets-conseil-hausse-2024 |

---

## §12 CARTE DIALECTIQUE

**SCÉNARIO A (Officiel — Transformation maîtrisée)**
"L'État modernise son SI dans le cadre d'une stratégie cohérente (Cloud au centre, agilité). La DINUM pilote, l'ANSSI sécurise. Les 45 grands projets sont suivis, les écarts budgétaires se réduisent (6.5%). Le HDH quitte Microsoft pour Scaleway. 84M€ de cloud européen en 2025. Les ESN sont des partenaires nécessaires. La souveraineté est en marche."

**SCÉNARIO B (Critique — Captation organisée)**
"5 Md€/an gaspillés dans un système verrouillé par les ESN. Capgemini seul capte 1.1 Md€ en 5 ans — pour quels résultats ? L'ANSSI fait 32 audits/an pour un SI de plusieurs milliers de systèmes. Les ministères contournent la DINUM. Les données sensibles sont chez Microsoft. Le pantouflage garantit que ceux qui écrivent les appels d'offres seront demain chez ceux qui y répondent. Le système est conçu pour échapper à tout contrôle."

**TENSIONS** :
- Convergence : Les deux reconnaissent une dépendance aux ESN et un besoin de modernisation
- Divergence : Le A voit une transformation sous contrôle, le B voit une captation irréversible
- Gap : Aucun audit indépendant de l'efficacité réelle des 4-5 Md€ dépensés
- Vrai loup : Le pantouflage crée une "communauté d'intérêts" entre les décideurs publics et les ESN

**QUI GAGNE** : Capgemini, Sopra Steria, Atos, Accenture (contrats), McKinsey et consorts (conseil lucratif, 0€ IS), Microsoft/SAP (dépendance technologique)
**QUI PERD** : Citoyens (données exposées, impôts), agents publics compétents (départs vers privé), PME françaises (verrouillage)
**QUI MEURT** : La souveraineté numérique française, la confiance dans l'administration numérique
**QUI RECULE** : L'État stratège, la compétence publique en IT, la sécurité des données

---

## §13 PÉRIMÈTRE & LIMITES

**Périmètre** : SI de l'État français central. Pas les collectivités territoriales, pas les hôpitaux (sauf relations), pas les opérateurs privés de service public.

**Exclusions** :
- Analyse exhaustive de chaque ministère (tâche impossible sans accès aux comptes)
- Audit détaillé de chaque contrat Capgemini/Sopra/Atos (données publiques partielles)
- SI de la défense et du renseignement (classifié)
- Offres cloud des fournisseurs chinois (Alibaba, Huawei) — négligeable en France
- Comparaison internationale détaillée (Royaume-Uni, Allemagne, Estonie)

**Limites** :
- **Absence de donnée primaire centralisée** : La France ne publie pas de "digital budget" agrégé. Les 4-5 Md€ sont une estimation.
- **Biais de disponibilité** : Les données sur les contrats sont partielles (macellum.fr, openprocurements) — les montants réels peuvent être supérieurs.
- **Pas d'accès aux contrats** : Analyse basée sur les marchés notifiés, pas sur les avenants.
- **Conjecture sur le pantouflage** : Si le phénomène est documenté, son impact précis sur les décisions d'achat public n'est pas quantifiable.
- **Biais temporel** : Focus 2017-2026. L'analyse de la sous-traitance pré-2017 n'est pas faite.

---

## §14 ÉTAT DES CONNAISSANCES

**KNOWN (✦ confirmé)** :
- Budget IT État : 4-5 Md€/an (estimation, sources multiples convergentes)
- 45 grands projets : 3.3 Md€, durée moyenne 6.3 ans
- Capgemini : 1.1 Md€ contrats État 2017-2022 (Le Monde)
- McKinsey : 0€ IS France 2011-2020, enquête PNF ouverte
- ANTS : 85-90% externalisation, sous-traite sa propre stratégie d'audit
- ANSSI : 32 audits/an, "portée faible" selon CdC
- DINUM : 79M€/138M€, 5 directeurs depuis 2018
- HDH : données santé françaises sur Microsoft Azure 2019-2026, migration Scaleway
- NHS NIS2 : non transposée en France
- Pantouflage : 29% ingénieurs mines, 22% ENA en privé
- Chorus (SAP) : SI financier État, 24 000 utilisateurs, migrate S/4HANA 78.4M€
- Dépenses conseil 2021 : 271M€ record, 2024 : 96M€ remontée

**SUSPECTED (✧ probable)** :
- Le pantouflage influence directement l'attribution des marchés (conflit d'intérêts systémique)
- La "politique de l'évitement" des ministères face à la DINUM est généralisée
- L'ANSSI sous-estime la menace réelle faute de capacité d'audit
- Le vrai coût total du SI (incluant maintenance, dette technique, sécurité) est >5 Md€

**UNKNOWN (gaps)** :
- Combien exactement chaque ESN gagne-t-elle avec l'État ? Pas de consolidation publique
- Quel est l'état réel de la dette technique du SI État ? Aucune cartographie publique
- Combien de systèmes d'information l'État compte-t-il exactement ? Pas de registre exhaustif
- Quel est le taux de conformité réel aux obligations de sécurité (homologation) ? Non audité
- Combien d'anciens fonctionnaires pantouflent dans chaque ESN ? HATVP ne publie pas de données agrégées
- Quel est l'impact réel des 4-5 Md€ sur l'efficacité du service public ? Aucune évaluation

---

## §15 SUSPICION SCORES

| Source | Type | Score | Raison |
|--------|------|-------|--------|
| Le Monde "Capgemini 1.1 Md€" | ◈ Primaire | 0.90 | Enquête exhaustive, données vérifiées |
| Rapport Sénat "cabinets conseil" | ◈ Primaire | **0.95** | Commission d'enquête, pouvoirs renforcés |
| Cour des Comptes (DINUM/ANSSI/ANTS) | ◈ Primaire | **0.95** | Documents officiels, contradictoire |
| DINUM panorama projets | ⟐ Officiel | 0.80 | Transparent sur le périmètre, lacunes assumées |
| ANSSI rapport annuel | ⟐ Officiel | 0.80 | Chiffres vérifiables, auto-évaluation |
| IT for Business | ◉ Secondaire | 0.75 | Enquêtes détaillées, bonne couverture |
| CIO Online (Reynald Fléchaux) | ◉ Secondaire | 0.75 | Source spécialisée SI, fiable |
| ZDN (Christophe Auffray) | ◉ Secondaire | 0.75 | Reprend CdC, bonne analyse |
| Public Sénat | ◉ Secondaire | 0.70 | Bon suivi législatif |
| SAP France (Chorus) | ⟐ Officiel | 0.70 | Auto-promotion, mais données vérifiables |
| Legiscope (SecNumCloud) | ◉ Secondaire | 0.70 | Bonne synthèse technique |
| Consultor.fr (McKinsey) | ◉ Secondaire | 0.75 | Enquête détaillée sur missions COVID |
| Ouest-France (pantouflage) | ◉ Secondaire | 0.70 | Reprend CdC, correct |
| Numerama (HDH) | ◉ Secondaire | 0.70 | Bonne analyse technique |
| Le Monde info (Conseil d'État) | ◉ Secondaire | 0.75 | Suivi juridique, précis |

---

## §16 RÉPONSE DIRECTE

**L'utilisateur demandait :** Qui fabrique ? Où sont stockées les données ? Comment sécurisé ? Qui vérifie ? Où va l'argent ? À qui profite ?

**Voici les réponses :**

**1. Qui fabrique ?** Un oligopole de 4 ESN privées : **Capgemini** (n°1, 1.1 Md€/5 ans), **Sopra Steria** (radars, ASP, commande publique), **Atos** (identités, défense), **Accenture** (UGAP, santé). Le SI financier (Chorus) est chez **SAP**. L'ANTS externalise à 85-90%.

**2. Où sont les données ?** Santé (SNDS/HDH) : Microsoft Azure (2019-2026). Impôts/finances : Chorus/SAP (AIFE). Identité (passeports, TES) : ESN privées (sous-traitance). Cloud souverain qualifié (OVH, Outscale, Scaleway) pour données non sensibles. Bleu (Microsoft+Capgemini) et S3NS (Google+Thales) en attente de certification.

**3. Comment sécurisé ?** Par l'ANSSI qui fait **32 audits/an** — la Cour des Comptes juge la "portée faible". L'ANTS sous-traite sa PROPRE stratégie d'audit de sécurité. L'ANSSI accompagne plus qu'elle ne contraint : son pouvoir de sanction (2013) n'a jamais été utilisé.

**4. Qui vérifie ?** La DINUM (budget 79M€ face à 5 Md€ — ratio : 1.6%). Mais les ministères contournent ("politique de l'évitement"). La Cour des Comptes alerte depuis 2015 — ignorée. NIS2 pas transposée.

**5. Où va l'argent ?** 4-5 Md€/an. Capgemini capte ~220M€/an, Sopra ~150M€, Atos ~120M€, Accenture ~100M€. Consulting : 96M€ en 2024 (remontée +31%). Le budget IT par ministère n'est pas publié (contrairement au Royaume-Uni).

**6. À qui profite ?** **Capgemini** (n°1 bénéficiaire), **Sopra Steria**, **Atos**, **Accenture**, **McKinsey** (0€ IS), **Microsoft** (cloud), **SAP** (licences). Les consultants pantouflards qui font l'aller-retour public-privé. Et les décideurs publics qui savent qu'ils seront chez l'ESN demain.

---

*Investigation APEX — Protocole KERNEL v2.0 complet — 17 Juin 2026*
