# AUDIT APEX — S14 : La Défense en berne

> Score global : **8.6/10** — RÉVISION MINEURE
>
> Résumé : Article structurellement solide, bien sourcé sur les faits core (LPM, AUKUS, Barkhane), avec une analyse systémique convaincante de l'abdication stratégique. **Deux problèmes de vérifiabilité** : (1) le blockquote Iran 2026 dans §4 contient des allégations factuelles non sourcées (Araghchi quote, 400k citoyens, MICA épuisés) — partiellement vérifié via La Tribune mais pas dans le FACTCHECK ; (2) le passage « 4 jours » de munitions dans le blockquote §1 ne trouve pas de source — les rapports parlementaires disent « quelques semaines ». Corrections ciblées avant APEX.

## RADAR SCORE

| S1 Struc. | S2 Source | S3 URLs | S4 Ton | S5 §6 | S6 Fond. | S7 Caus. | S8 Cohér. | S9 Écrit. |
|-----------|-----------|---------|--------|-------|----------|----------|-----------|-----------|
| 9.2 | 8.0 | 9.0 | 6.8 | 10.0 | 7.8 | 8.0 | 10.0 | 8.7 |

## CONTRÔLE GATE

- Gate 1 (Structure) : **PASS** (11/12)
- Gate 2 (Sourçage) : **PASS** (8.4/10)
- Gate 3 (Ton) : **PASS** (8.2/10)
- Gate 4 (Fondation) : **PASS** (7.8/10)
- Gate 5 (Écriture) : **PASS** (8.7/10)

## FINDINGS (par ordre de gravité)

### F001 — Blockquote Iran 2026 non sourcé dans le FACTCHECK

| Champ | Valeur |
|-------|--------|
| **Couche** | 4 (4.1 + 4.4) |
| **Localisation** | §4, ligne 97-98 (blockquote dans « La dissuasion nucléaire ne remplace pas la masse ») |
| **Problème** | Le blockquote décrit avec précision des événements de la guerre Iran-États-Unis 2026 : « stocks français de missiles MICA se sont épuisés en quelques jours », « 400 000 citoyens français étaient exposés dans le Golfe », et une citation directe d'Araghchi humiliant Macron. **Aucune de ces allégations n'est dans le FACTCHECK.** |
| **Preuve** | Vérification web : (a) **MICA** — La Tribune (15/03/2026) et Defense Mirror confirment une depletion rapide des MICA des Rafale aux EAU. Partiellement vérifié. (b) **400 000 citoyens** — Pas trouvé de source confirmant ce chiffre. Franceinfo mentionne des rapatriements de Français du Golfe. Non vérifié. (c) **Citation Araghchi** — Introuvable dans aucune source. Araghchi a fait de nombreuses déclarations (AP, Military.com) mais cette citation précise est inverifiable. |
| **Correction** | **(a)** Ajouter une note de source après le blockquote pointant vers l'article de La Tribune (mars 2026) pour la depletion MICA. **(b)** Remplacer « 400 000 citoyens » par une formulation prudente type « des dizaines de milliers de Français exposés » (vérifiable : nombre de Français au Moyen-Orient). **(c)** Supprimer la citation directe d'Araghchi si non vérifiable OU la sourcer avec une URL précise. |
| **Priorité** | Haute |

### F002 — « 4 jours » de munitions non vérifiable

| Champ | Valeur |
|-------|--------|
| **Couche** | 4 (4.1 + 4.4) |
| **Localisation** | §1, ligne 29 (blockquote dans « Le trou des munitions ») |
| **Problème** | Le blockquote affirme : « Les rapports parlementaires de 2025 sont encore plus précis : 4 jours. Quatre jours de capacité avant rupture totale de munitions. » Aucun rapport parlementaire trouvé avec ce chiffre. Les sources disponibles (AN rapport Chenevard/Saint-Pasteur sept 2025, articles mai 2025) disent « quelques semaines », pas « 4 jours ». |
| **Preuve** | Vérification web : (a) Article newsnet.fr (mai 2025) : « quelques semaines ». (b) Rapport AN n°1890 (sept 2025) : « stocks insuffisants pour tenir plus de quelques semaines », pas de mention de « 4 jours ». (c) Rapport Sénat PLF 2026 : évoque les tensions budgétaires mais pas « 4 jours ». |
| **Correction** | Remplacer « 4 jours » par « quelques semaines » pour être cohérent avec la source existante (AN PLF 2026 Tome VII, déjà cité). Alternative : si « 4 jours » vient d'une audition spécifique non publiée en ligne, ajouter une note sourçant précisément cette déclaration. |
| **Priorité** | Haute |

### F003 — URL source 5 : ID placeholder

| Champ | Valeur |
|-------|--------|
| **Couche** | 2 (2.3) |
| **Localisation** | Source 5 : `l17b9999_rapport-information.pdf` |
| **Problème** | Le pattern `9999` est un placeholder générique de l'AN, pas un ID de document réel. |
| **Correction** | Remplacer par l'URL du rapport AN sur les drones effectivement publié (rechercher l'ID réel sur assemblee-nationale.fr). |
| **Priorité** | Basse |

### F004 — Faits secondaires non sourcés dans le FACTCHECK

| Champ | Valeur |
|-------|--------|
| **Couche** | 2 (2.1) |
| **Localisation** | §1-§4, dispersé |
| **Problème** | Plusieurs affirmations factuelles n'ont pas de source inline et ne sont pas dans le FACTCHECK : « 200 000 soldats », « 21,6 Md€ d'exportations 2024 », contrats Rafale par pays (Égypte 24, Qatar 36, etc.). Ces faits sont plausibles et généralement connus mais la rigueur forensique exige qu'ils soient traçables. |
| **Preuve** | Aucune entrée FACTCHECK pour ces chiffres. Les contrats Rafale sont documentés par Dassault Aviation (source 13), le 21,6 Md€ par le rapport au Parlement (source 14) — mais pas d'inline « selon [source] » dans le texte pour ces chiffres. |
| **Correction** | Ajouter des inline sources pour : (a) « 200 000 soldats » → selon CIA World Factbook ou ministère. (b) « 21,6 Md€ d'exportations » → selon le rapport au Parlement 2024. (c) Ajouter les contrats Rafale dans le FACTCHECK (SP23-SP28). |
| **Priorité** | Moyenne |

## RECOMMANDATIONS PRIORITAIRES

1. **[HAUTE] F001** — Corriger le blockquote Iran 2026 : ajouter source La Tribune pour MICA, reformuler 400k, supprimer citation Araghchi. Effort : 15min.
2. **[HAUTE] F002** — Remplacer « 4 jours » par le chiffre vérifié « quelques semaines ». Effort : 5min.
3. **[MOYENNE] F004** — Ajouter inline sources pour les faits secondaires (200k soldats, 21,6 Md€). Effort : 15min.
4. **[BASSE] F003** — Corriger URL source 5. Effort : 10min.

## NOTES LLM (métriques détaillées)

### Couche 1 — Conformité structurelle : 11/12
| Point | Statut |
|-------|--------|
| H1 format | ✅ |
| Sous-titre | ✅ |
| Ligne série | ✅ |
| §0 complet | ✅ |
| ## §N | ✅ |
| --- entre sections | ✅ |
| H3 subsections | ✅ |
| À lire ensuite | ✅ |
| Footer | ✅ |
| ## Sources H2 | ✅ |
| URLs spécifiques | ⚠️ Source 5 placeholder 9999 |
| §6 présent | ✅ |

### Couche 2 — Sourçage : 8.4/10
- 2.1 Saturation : 6/10 (~4-5 phrases sans source inline)
- 2.2 Diversité : 10/10 (≥10 sources différentes)
- 2.3 Précision URLs : 9.0/10 (1 URL sur 20 problématique)
- 2.4 Fraîcheur : 10/10 (sources 2023-2025)

### Couche 3 — Ton & Rhétorique : 8.2/10
- 3.1 Intentionnaliste : 8/10 (~15% de marqueurs, acceptable)
- 3.2 Ton polémique : 5/10 (3 occurrences de langage évaluatif)
- 3.3 Cohérence §6 : 10/10 (4/4 critères)

### Couche 4 — Fidélité Fondation : 7.8/10
- 4.1 Exactitude : 8/10 (core facts match FACTCHECK, blockquote non couvert)
- 4.2 Fidélité interprétative : 8/10 (1 saut : blockquote Iran sans fondation)
- 4.3 Omissions : 10/10
- 4.4 Vérification web : 6/10 (2 faits contestés non vérifiés)
- 4.5 Agrégations : 10/10

### Couche 5 — Écriture : 8.7/10
- 5.1 Visibilité système : 9/10 (excellente, §5 nomme le mécanisme)
- 5.2 Démonstration traçable : 8/10 (blockquote Iran est un saut)
- 5.3 Respiration : 8/10 (bon équilibre, §1 un peu dense)
- 5.4 Cohérence catégorielle : 10/10
