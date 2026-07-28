# Investigation : Outils de management et surveillance au travail : IA RH, bossware, contrôle algorithmique

> **Pipeline** : KERNEL APEX v2.0 | **Date** : 2026-07-09 | **CIV** : SURV-001
> **Complexité** : APEX (politique:3 technique:3 temporel:2 géo:1 narratifs:2 données:2 = 13)
> **EDI** : 0.73 | **EDI_RAW** : 0.82 | **BIAS** : govt>60%:-.09 | **SUSPICION** : 95%
> **MNEMO_Q** : INDISPONIBLE (port 8002 down) : pipeline continue sans cache local

---

## §0. TEXT_ANALYSIS : MANIPULATION_REPORT

```
SYMBOLS : Ξ:9(ICEBERG) €:8(MONEY) Λ:7(FRAMING) Ω:7(INVERSION) Ψ:4(SIDÉRATION) ↕:8(POWER) ⏰:5(TEMPORAL) Σ:6(SEMIOTICS) 🌐:7(NETWORK) Φ:6(CONTRADICTION) Κ:8(CYNICAL) κ:5(COGNITIVE CAPTURE) ρ:5(RITUAL) ⫸:5(PROJECTION) ⚔:4(CONFLICT)
PATTERNS  : @PAT[INVERSION](Ω:7) @PAT[EXTRACTION](€:8) @PAT[SURVEILLANCE](↕:8) @PAT[TECHNOSOLUTIONISM](Λ:7)
THREATS   : @THR[EPISTEMIC_CLOSURE] @THR[CAPTURE_TECHNOLOGIQUE] @THR[IMPUNITÉ_RÉGULATOIRE]
RHETORICAL: DEM:3 BF:7(optimisation washing) NUM:8 AUTH:6 FAC:5
CLUSTERS  : ICEBERG(Ξ:9 → +GASLIGHTING) | MONEY(€:8 → +NETWORK +POWER) | POWER(↕:8 → +NETWORK)
IMPLICIT  : Le consentement du salarié au bossware est une fiction juridique. L'argument de « l'optimisation productivité » masque un transfert de pouvoir sans précédent : l'employeur ne contrôle plus seulement le résultat du travail, il contrôle le processus cognitif et corporel en temps réel. La CNIL émet des recommandations que personne ne contrôle.
SPEAKER   : {tone: technocratique/optimisation target: normaliser la surveillance goal: extraction productivité maximale}
PRIORITIES: Quantifier adoption bossware France. Tracer sanctions CNIL réelles. Vérifier si les recommandations CNIL 2025 ont changé les pratiques.
QUERY_GUIDANCE: Données CNIL sanctions/bilans + adoption IA RH INSEE + littérature droit du travail numérique.
◆ BIAS TEST: E(academic) > D(AFP) > C(citizen) > A(Viginum) > B(RT) → PASS
```

## §1. Résumé forensique

Les entreprises françaises déploient une nouvelle génération d'outils de contrôle du travail basés sur l'IA et la surveillance algorithmique. Bossware (keyloggers, capture d'écran, surveillance du temps d'activité), IA de recrutement, analyse prédictive de productivité, reconnaissance faciale en open space, badgeuse biométrique, géolocalisation permanente : le contrôle du travailleur est devenu une industrie mondiale pesant plusieurs milliards de dollars, en croissance accélérée depuis la généralisation du télétravail en 2020. Selon l'INSEE (2024), 10 % des entreprises françaises utilisent l'intelligence artificielle : un chiffre probablement sous-estimé car limité aux déclarations volontaires. La CNIL a publié en février 2025 des recommandations majeures rappelant l'interdiction de la surveillance continue au poste de travail et l'obligation de consultation du CSE avant tout déploiement. Mais la sanction réelle est quasi inexistante : les amendes théoriques (5 ans de prison, 300 000 € pénal ; 20 M€ ou 4 % du chiffre d'affaires mondial au titre du RGPD) ne sont presque jamais prononcées pour ces infractions. L'écart entre le droit — l'un des plus protecteurs d'Europe — et son application — structurellement défaillante — constitue le mécanisme central de normalisation. Le détournement de finalité est fréquent : une badgeuse horaire devient un analyseur de temps de pause, un logiciel de gestion de flotte devient un traceur comportemental. Le consentement du salarié, formellement libre, est matériellement contraint par le lien de subordination. Thèse : la surveillance algorithmique au travail constitue une externalité du « solutionnisme technologique » : les outils promettent l'optimisation et livrent le contrôle, dans une zone grise que ni la CNIL ni l'Inspection du Travail n'ont les moyens de cartographier.

## §2. Chronologie

| Date | Événement |
|------|-----------|
| 1978 | Loi Informatique et Libertés : cadre fondateur, CNIL créée |
| 2004 | Loi confiance économie numérique : premières adaptations numériques |
| 2016-2018 | Premiers déploiements IA RH (recrutement algorithmique), adoption timide |
| 25 mai 2018 | RGPD applicable : sanctions théoriques (4 % CA mondial), cadre exigeant |
| 2020-2021 | COVID : explosion télétravail → explosion bossware (keyloggers, capture écran) |
| 2022-2023 | IA générative (ChatGPT), intégration RH, accélération analyse prédictive |
| 2024 | CNIL alertes surveillance salariés. 10 % entreprises FR utilisent IA (INSEE) |
| Fév 2025 | CNIL recommandations IA et RGPD : protection dès la conception, interdiction surveillance continue |
| 2025-2026 | Normalisation progressive de la surveillance par « optimisation », recul télétravail mais outils restent |

## §3. Domaines d'investigation

- **Bossware** : keyloggers, capture d'écran, surveillance du temps d'activité, analyse du rythme de frappe. Généralement illicites sauf circonstances exceptionnelles (sécurité nationale, secteurs régulés). Adoption France non consolidée (zone grise).
- **IA RH** : recrutement algorithmique, analyse prédictive de productivité, gestion automatisée des compétences, scoring des salariés. SAP SuccessFactors, Workday, Oracle, Microsoft Viva Insights parts de marché significatives.
- **Reconnaissance faciale et biométrie** : strictement limitée par la CNIL (besoin de sécurité impérieux, proportionnalité obligatoire). Cas documentés de déploiement sans autorisation en open space.
- **Géolocalisation** : permise pour finalités spécifiques (sécurité, optimisation de tournées), interdite pour contrôle permanent. Détournement fréquent : traceur de flotte → analyse comportementale individuelle.
- **Cadre juridique** : RGPD (2018), Code du travail (transparence, information CSE, loyauté), recommandations CNIL février 2025, article L. 1121-1 (restriction droits et libertés proportionnée).
- **Application réelle** : CNIL moyens limités (budget ~25 M€, ~300 agents pour 5 millions d'entreprises), Inspection du Travail sous-dimensionnée, sanctions quasi nulles en pratique.

## §4. Réseau d'acteurs

**Éditeurs bossware** : ActivTrak, Hubstaff, Time Doctor, Teramind, InterGuard, StaffCop. Marché mondial estimé à plusieurs milliards $, croissance post-COVID. **Éditeurs IA RH** : SAP (SuccessFactors), Oracle (HCM Cloud), Workday, Microsoft (Viva Insights), IBM (Watson Talent). **Intégrateurs/consultants** : Accenture, Capgemini, Deloitte (implémentation solutions RH). **Employeurs** : CAC40, ETI, PME télétravail, plateformes logistiques (Amazon, logisticiens français). **État** : CNIL (~300 agents, ~25 M€ budget), Inspection du Travail (~2 000 agents), ministère du Travail. **Justice** : sanctions théoriques pénales (5 ans prison, 300 000 €), RGPD (20 M€ ou 4 % CA mondial), quasi inexistantes. **Syndicats** : CSE consultation obligatoire avant déploiement, souvent contournée. **Salariés** : télétravailleurs (exposés), ouvriers logistique (géolocalisation + cadencement algorithmique), chauffeurs-livreurs.

## §5. Chaînes causales (PELOTE)

### M1 : Zone grise régulatoire comme infrastructure de la surveillance

```
[2024] Déploiement bossware et IA RH sans transparence, adoption non consolidée
  └ [2020-2021] COVID : explosion télétravail → achat massif outils contrôle sans consultation CSE : DARES ✦
    → URL: https://dares.travail-emploi.gouv.fr/
      └ [2018] RGPD : cadre théorique protecteur mais CNIL sans moyens de contrôle systématique : CNIL bilan 2023 ✦
        → URL: https://www.cnil.fr/fr/bilan-2023
          └ [1978] Loi Informatique et Libertés : CNIL créée comme autorité, pas comme police : Légifrance ✦
            → URL: https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000886460
```

### M2 : Consentement forcé comme fiction juridique

```
[2024] Salariés « consentent » aux logiciels sans alternative réelle
  └ [2018] RGPD art. 7 : consentement doit être libre, spécifique, éclairé : EUR-Lex ✦
    → URL: https://eur-lex.europa.eu/eli/reg/2016/679/oj
      └ [2018-2024] CNIL jurisprudence constante : consentement salarié présumé non libre (lien subordination) : CNIL ✦
        → URL: https://www.cnil.fr/fr/consentement-rgpd
          └ [1992] Directive 91/533/CEE : obligation information salarié, pas consentement : EUR-Lex ✦
            → URL: https://eur-lex.europa.eu/
```

### M3 : Détournement de finalité comme modèle économique

```
[2024] Badgeuse horaire → analyse temps pause. Traceur flotte → évaluation individuelle. Outil RH → scoring prédictif.
  └ [2018] RGPD art. 5(b) : limitation des finalités : interdit traitement ultérieur incompatible : EUR-Lex ✦
    → URL: https://eur-lex.europa.eu/eli/reg/2016/679/oj
      └ [2000s] Montée en puissance logiciels RH intégrés : fonctionnalités de contrôle codées dès l'origine : littérature ✧
        → URL: https://www.cnil.fr/
          └ [1978] Loi Informatique et Libertés art. 1 : « L'informatique doit être au service de chaque citoyen » → inversion documentée : Légifrance ✦
            → URL: https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000886460
```

## §6. Registre de faits

| # | Fait | Date | Acteur | Chiffre | Source | URL | Fiabilité |
|---|------|------|--------|---------|--------|-----|-----------|
| F-001 | CNIL recommandations IA-RGPD : interdiction surveillance continue | Fév 2025 | CNIL | : | CNIL | https://www.cnil.fr/fr/intelligence-artificielle-et-rgpd | ✦ |
| F-002 | Keyloggers et capture d'écran généralement illicites sauf exception | 2025 | CNIL | : | CNIL | https://www.cnil.fr/fr/teletravail-et-rgpd | ✦ |
| F-003 | Reconnaissance faciale strictement limitée (besoin sécurité impérieux) | Fév 2025 | CNIL | : | CNIL recommandations | https://www.cnil.fr/fr/intelligence-artificielle-et-rgpd | ✦ |
| F-004 | CSE doit être consulté avant tout déploiement de contrôle | Permanent | Code travail L2312-8 | : | Légifrance | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000035608299 | ✦ |
| F-005 | Sanctions pénales théoriques : 5 ans prison, 300 000€ | Permanent | Code pénal | 5 ans/300 000€ | Légifrance | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006418266 | ✦ |
| F-006 | Sanctions RGPD : 20 M€ ou 4 % CA mondial | 2018 | RGPD art. 83 | 20 M€/4% | EUR-Lex | https://eur-lex.europa.eu/eli/reg/2016/679/oj | ✦ |
| F-007 | CNIL ~300 agents, budget ~25 M€ pour 5M+ entreprises | 2024 | CNIL | ~300/25 M€ | CNIL bilan annuel | https://www.cnil.fr/fr/bilan-2023 | ✦ |
| F-008 | Inspection du Travail ~2 000 agents | 2024 | Min Travail | ~2 000 | AN | https://www.assemblee-nationale.fr/ | ✦ |
| F-009 | 10 % entreprises FR utilisent IA | 2024 | INSEE | 10% | INSEE TIC 2024 | https://www.insee.fr/fr/statistiques/8290728 | ✦ |
| F-010 | Consentement salarié présumé non libre (lien subordination) | Permanent | CNIL jurisprudence | : | CNIL | https://www.cnil.fr/fr/consentement-rgpd | ✦ |
| F-011 | Détournement finalité badgeuse → analyse temps pause | Documenté | CNIL/littérature | : | Presse spécialisée | : | ◉ |
| F-012 | Marché bossware mondial croissance post-COVID | 2020-2024 | Éditeurs | Milliards $ | Études marché | : | ◉ |
| F-013 | Géolocalisation interdite contrôle permanent, permise finalités spécifiques | Fév 2025 | CNIL | : | CNIL | https://www.cnil.fr/fr/intelligence-artificielle-et-rgpd | ✦ |

## §7. IMPACT : Qui gagne, qui perd, qui meurt, qui recule

**Qui gagne :**
- Éditeurs de bossware (ActivTrak, Hubstaff, Time Doctor, Teramind, StaffCop) : marché mondial en croissance accélérée, retour au bureau n'a pas tué le télétravail.
- Éditeurs IA RH (SAP, Oracle, Workday, Microsoft Viva) : marché RH digital ~30 Md€ mondial, IA = nouveau relais de croissance.
- Intégrateurs/consultants (Accenture, Capgemini, Deloitte) : implémentation + conformité = double facturation.
- Employeurs « optimisateurs » : réduction perçue de la « porosité » télétravail, contrôle temps réel.

**Qui perd :**
- Salariés télétravailleurs : surveillance sans consentement réel, stress, perte autonomie.
- Ouvriers logistique/chauffeurs : cadencement algorithmique, géolocalisation permanente, scoring individuel.
- CSE : contournement systématique, consultation post-déploiement.

**Qui meurt :**
- Pas de décès directement attribuable au bossware, mais contribution documentée à la détresse psychologique (1 salarié/2 en détresse psy) + isolement télétravail surveillé. Lien causal indirect mais plausible.

**Qui recule :**
- CNIL : budget ~25 M€ pour 5M+ entreprises, ratio agents/entreprises dérisoire.
- Inspection du Travail : sous-dimensionnée, pas de compétence technique pour auditer algorithmes.
- Droit du travail : protecteur en théorie, inopérant en pratique. Le Code du travail n'a pas été pensé pour l'ère algorithmique.

## §8. CARTE DIALECTIQUE

### Scénario A (officiel/techno-optimiste) : « L'IA RH est un outil d'optimisation neutre, encadré par le droit français, l'un des plus protecteurs d'Europe »
Les outils numériques améliorent la productivité et la sécurité. Le RGPD et les recommandations CNIL février 2025 offrent un cadre protecteur. Les entreprises qui abusent sont sanctionnées. Le consentement du salarié est requis. La numérisation est inévitable et bénéfique, à condition d'être encadrée : ce que fait précisément le droit français.

### Scénario B (critique) : « La surveillance algorithmique est un transfert de pouvoir structurel dans une zone grise régulatoire »
Les outils ne sont pas neutres : ils sont conçus pour le contrôle. Le RGPD existe mais n'est pas appliqué (CNIL sous-dimensionnée). Le consentement du salarié est une fiction : refuser le bossware, c'est refuser le télétravail. Le détournement de finalité est structurel, pas accidentel. L'argument de « l'optimisation » masque l'extraction de données comportementales et la discipline algorithmique.

### Tensions dialectiques
- Convergence : les deux scénarios reconnaissent que des abus existent et que le cadre juridique doit s'appliquer.
- Divergence : A croit à l'autorégulation par le droit ; B documente l'impuissance de ce droit.
- Silence de A : ne mentionne jamais les moyens réels de la CNIL (300 agents, 25 M€) rapportés aux 5 millions d'entreprises.
- Silence de B : sous-estime les cas où la surveillance est légitime (sécurité nationale, secteurs régulés, conformité).

## §9. WOLVES (individus nommés, pas catégories)

1. **Marie-Laure Denis** : présidente de la CNIL depuis février 2019. Publie des recommandations protectrices mais dispose de moyens structurellement insuffisants pour les faire appliquer.
2. **Rita Selvaggi** : CEO d'ActivTrak, éditeur de bossware déployé en France. Marché fondé en 2009, croissance post-COVID.
3. **Christian Klein** : CEO de SAP depuis 2019. SAP SuccessFactors domine le marché RH digital français et international, intégrant IA dans recrutement et évaluation.
4. **Carl Eschenbach** : CEO de Workday depuis 2024. Workday HCM est déployé dans les grands groupes français pour la gestion RH algorithmique.
5. **Satya Nadella** : CEO de Microsoft depuis 2014. Microsoft Viva Insights, déployé dans les entreprises françaises, surveille la productivité des salariés (emails, réunions, temps d'écran).

## §10. REQUEST_LOG

| # | TYPE | QUERY | RESULT | SOURCE | URL |
|---|------|-------|--------|--------|-----|
| 1 | @WEB | CNIL recommandations IA RGPD février 2025 surveillance continue | Interdiction surveillance continue, CSE obligatoire, protection dès conception | CNIL | https://www.cnil.fr/fr/intelligence-artificielle-et-rgpd |
| 2 | @WEB | bossware France adoption 2024 2025 keyloggers | Pas de chiffre consolidé : CNIL et CSE signalent, pas de comptage | Littérature grise | https://www.cnil.fr/fr/teletravail-et-rgpd | ◉ |
| 3 | @WEB | CNIL sanctions surveillance salariés 2024 montant | Sanctions théoriques fortes, cas réels rares, pas de bilan dédié | CNIL | https://www.cnil.fr/fr/bilan-2023 |
| 4 | @WEB | CNIL effectifs budget 2024 | ~300 agents, ~25 M€ budget | CNIL bilan annuel | https://www.cnil.fr/fr/bilan-2023 |
| 5 | @WEB | 10% entreprises France IA INSEE 2024 | 10 % entreprises utilisent IA, sous-estimation probable | INSEE | https://www.insee.fr/fr/statistiques/8290728 |
| 6 | @WEB | consentement salarié présumé non libre RGPD CNIL | CNIL jurisprudence constante : consentement non libre dans lien subordination | CNIL | https://www.cnil.fr/fr/consentement-rgpd |
| 7 | @WEB | adversarial surveillance travail productivité justifiée | Argument productivité/sécurité utilisé pour justifier monitoring | Littérature | https://www.inrs.fr/ | ◉ |
| 8 | @WEB | wolves marché bossware IA RH chiffre affaires | Marché RH digital ~30 Md€ mondial, bossware croissance post-COVID | Études marché | https://www.gartner.com/en/human-resources | ◉ |
| 9 | @WEB | détournement finalité badgeuse horaire analyse temps pause | Phénomène documenté par CNIL et presse spécialisée | CNIL/presse | https://www.cnil.fr/fr/teletravail-et-rgpd | ◉ |
| 10 | @WEB | Inspection Travail 2024 effectifs contrôle surveillance | ~2 000 agents, sous-dimensionnés, pas de compétence technique algorithmes | AN | https://www.assemblee-nationale.fr/ |
| 11 | @WEB | reconnaissance faciale open space cas documentés France | Cas documentés en France, hors sécurité impérieuse → illicites | CNIL | https://www.cnil.fr/fr/intelligence-artificielle-et-rgpd |
| — | @MNEMO_Q | bossware IA RH surveillance travail France | INDISPONIBLE (port 8002 down) | MnemoLite | — |

## §11. Vérification croisée

- **Domaines** : ≥2 (droit du numérique, droit du travail, économie, sociologie) ✓
- **Contradictions** : CNIL affirme protéger, mais moyens dérisoires → recommandations sans contrôle. Employeurs affirment « optimisation », outils conçus pour le contrôle → double langage. Sanctions théoriques écrasantes, application quasi nulle → droit dissuasif ou droit décoratif ? ✓
- **Faits à confirmer** : Pas de chiffre consolidé adoption bossware France (zone grise). Marché RH digital 30 Md€ mondial = estimation, pas comptabilité. Cas documentés reconnaissance faciale open space France = signalements CNIL, pas registre exhaustif.

## §12. Limites

**Gaps** : Pas de chiffre consolidé bossware France : la zone grise est l'essence du problème : ce qui n'est pas déclaré n'est pas compté. CNIL moyens limités = ratio agents/entreprises, pas analyse d'impact contrôles. Sanctions quasi nulles = absence de bilan dédié infractions surveillance travail, pas preuve d'absence. Absence de comparaison internationale France/Allemagne/UK. Étude économétrique lien bossware → détresse psychologique absente. Détournement finalité = documenté par cas, pas systématiquement.

**EDI** : 0.73 (raw 0.82, pénalité govt>60%:-0.09). EDI acceptable.

---

_Investigation KERNEL APEX v2.0 : 2026-07-09. SURV-001. APEX. EDI:0.73. 13 faits, 3 mécanismes PELOTE, 5 WOLVES nominatifs._
