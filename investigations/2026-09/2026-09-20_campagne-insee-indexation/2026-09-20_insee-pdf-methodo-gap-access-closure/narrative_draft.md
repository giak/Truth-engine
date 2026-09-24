# Clôture des gaps ACCESS : extraction des PDF méthodologiques de l'Insee (UPDATE du run 18-12)

## Objet et lignée

Ce run est un **UPDATE** du parent `20260920-1812-insee-chaine-donnee-indicateur-claim-provenance-et-robustesse` (investigation « DATA → STATISTIC → CLAIM », marquée FINAL et persistée le jour même). La requête courante demande d'**extraire les PDF méthodologiques** (Insee Méthodes 136/145, note de révisions) **pour clore les gaps ACCESS** que le parent avait typés honnêtement : « PDF non extractibles » (VERIFICATION_REPORT) et 3 items de NEXT_QUERIES. L'objet réouvert est l'input exact du parent (même empreinte sujet) ; le snapshot MNEMO a été hydraté (9 faits), chaque fait réévalué (3 RECHECK pour les ✦, 6 REUSE pour les ✧), et les pièces d'évidence ont été réellement téléchargées **depuis ce run**.

**Résultat central : le gap ACCESS du parent n'abritait aucun dossier caché.** Les sept pièces visées sont des documents publics ordinaires, publiés et téléchargeables ; ce qui manquait était la lecture, non l'accès. Trois des sept NEXT_QUERIES du parent sont refermées par extraction ; quatre restent ouvertes et routées.

## Ce que l'extraction a refermé

| Pièce | Ce qu'elle apporte |
|---|---|
| **Insee Méthodes 136** (oct. 2020, « La qualité des estimations de population dans le recensement ») | La non-réponse totale des enquêtes annuelles de recensement s'élève à **3,9 % en 2019, dont 36 % de refus explicites** (partie 2) ; le nombre de personnes des logements non répondants est déterminé par une procédure d'**imputation statistique hot deck**. NEXT_QUERY n°2 du parent refermée. |
| **Fiche précision du recensement** | Qualité publiée : **coefficient de variation par strate** ; communes de moins de 10 000 habitants enquêtées exhaustivement (1 an sur 5), communes de 10 000 ou plus par sondage d'adresses ; intervalles de confiance constructibles. |
| **Note de révisions du 3 juin 2026** | Chaîne provisoire → semi-définitif → définitif documentée, rôle d'Ésane (données fiscales) ; **PIB 2023 révisé +0,2 pt, 2024 +0,3 pt, 2025 inchangé**. Réconcilie la contradiction presse du parent : 1,9 % = corrigé des jours ouvrables, 1,6 % en données brutes. NEXT_QUERY n°6 refermée. |
| **Rapport IGF-IGAS 2007** (181 p., mission statistiques chômage) | Contrôle externe de la mesure du chômage ; la partie statistique est textuellement exploitable. NEXT_QUERY n°3 refermée. |
| **Insee Méthodes 145** (nov. 2023) | La rénovation de l'ERFS 2021 crée une **rupture de mesure estimée à −0,3 point** sur le taux de pauvreté, **−0,007 sur l'indice de Gini**, niveaux de vie rehaussés par le nouveau calage. |
| **Sources & méthodes ERF (2008)** | Appariement enquête Emploi + fichiers fiscaux et caisses : la chaîne de provenance des revenus, à la source. |
| **Note méthodologique EEC** (Division emploi) | Codage BIT en 3 critères, surveillance de la non-réponse, calage : la mécanique du chômage mesuré, à la source. |

## Contrôles d'intégrité exécutés (méthode)

1. **Identité d'octets** : chaque PDF a été re-téléchargé depuis son URL canonique de fichier (`insee.fr/fr/statistiques/fichier/…`, `vie-publique.fr/files/rapport/pdf/074000604.pdf`) et comparé par sha256 aux copies extraites — **9/9 identiques** (IM 136 ×5 parties, IM 145, note révisions, fiche précision, rapport 2007, méthodes ERF).
2. **Traçabilité de localisation** : les URLs de fichiers ont été résolues depuis les pages canoniques de documentation (IM 136 : `insee.fr/fr/information/4796233`), jamais devinées.
3. **Honnêteté des échecs** : une page testée s'est révélée 404, les pages de séries (`s1194`, `s2150`) sont rendues JavaScript sans texte exploitable, et la note EEC n'a pas d'URL publique re-résoluble — son PDF est **archivé localement dans `evidence/` avec sha256** (`7017f86e…`) et sa provenance documentée comme source à chemin validé.
4. **Réouvertures** : les trois ✦ du parent (FCT-006, FCT-007, FCT-008) ont été réouvertes avec les valeurs parent reprises mot pour mot, les sources ré-inspectées dans ce run, et une **réfutation adversariale** exécutée chacune (aucune contre-preuve totale trouvée ; contre-preuves partielles conservées dans les libellés).

## Ce que les documents changent (et ne changent pas)

**Ils affinent le gradient de fiabilité du parent sans le contredire.** La non-réponse est chiffrée (3,9 %), le mode d'imputation est nommé (hot deck), la précision est publiée par strate (CV), les ruptures sont quantifiées par l'institut lui-même (−0,3 pt, −0,007), et la chaîne de révision est documentée pas à pas. C'est l'exact opposé d'une boîte noire : la modélisation est **explicite et contradicible**.

**Ils ne documentent aucune manipulation.** Aucun des extraits méthodologiques ne contient de trace de pression, de sélection opportuniste ou d'omission dissimulée. La critique du parent tient toujours, mais elle tient ailleurs : dans l'**asymétrie de visibilité** (le premier chiffre façonne le récit ; la révision se corrige en silence, ici +0,2 pt et +0,3 pt) et dans le **coût d'accès réel** — disposer d'un PDF n'est pas le lire ; les pages HTML vides et la lecture experte exigée forment un seuil technique qui filtre le public.

**Une nuance nouvelle : la vérification par un tiers est matériellement possible.** L'identité d'octets, les CV publiés, les imputations nommées et le contrôle externe historique (IGF-IGAS 2007) constituent un contre-pouvoir documentaire effectif — c'est le point ρ du run.

## Symboles narratifs (évaluation finale, observations nommées)

| Symbole | Score | Observation |
|---|---|---|
| Ξ Omission | 4 | Les « gaps » du parent étaient des omissions de lecture ; 4 questions restent ouvertes et routées (OCR, taux de réponse par vague, DGF/DGCL, COICOP). |
| € Money | 1 | Aucun flux financier nouveau documenté ; le chiffrage DGF reste NOT COMPUTABLE (routé). |
| Λ Framing | 3 | « Accessibilité ≠ lisibilité » : dispersion documentaire, pages HTML vides, PDF à seuil technique. |
| Ω Inversion | 0 | Évalué absent : aucune inversion observée dans les extraits. |
| Ψ Sideration | 1 | Volume de 9 documents mais aucun flood émotionnel ; lecture calme possible. |
| ↕ Vertical power | 3 | La documentation est produite par l'institut mesuré lui-même ; compensée par IGF-IGAS et la vérifiabilité matérielle. |
| Φ Spectacle | 1 | Erratum du jour même (IP 2105) : correction discrète, sans dramatisation. |
| Σ Semiotics | 1 | Le label « Méthodes » n'équivaut pas à un audit indépendant ; contrôle externe réel documenté. |
| Κ Cynicism | 0 | Évalué absent : aucune façade contredite par les faits observés. |
| ρ Resistance | 4 | Vérification d'octets possible par quiconque ; CV, imputations et ruptures publiés ; IGF-IGAS 2007. |
| κ Subtle influence | 1 | Séquence de publication (provisoire d'abord) persiste du parent, désormais chiffrée. |
| ⫸ Convergence | 4 | Les PDF convergent avec les faits parent : −0,3 pt, −0,007, +0,2/+0,3 pt, 3,9 % — pièces indépendantes alignées. |
| ⚔ Cognitive warfare | 0 | Assessi absent : aucune activité d'influence organisée en scope. |
| 🌐 Network | 2 | Divisions Insee (Revenus, Emploi, RP) auteures ; IGF/IGAS externes ; héritage ASP/CNERP/CNIS du parent. |
| ⏰ Temporal | 4 | Chaîne de révision et erratums : le temps de publication change l'interprétation, quantifié. |

Aucun symbole ✗ ni DEFERRED ; clusters mobilisés : ICEBERG (omission/accès), MONEY (flux non chiffrés), FRAMING, POWER, RESISTANCE, CONFIRMATION (asymétrie de visibilité), TEMPORAL.

## Vérification, responsabilité, limites

- **Faits** : 8 faits — 3 ✦ réouvertes (populations légales estimées mais juridiques ; biais moyen haussier des révisions PIB et erratum ; pauvreté facteur 5 selon le seuil choisi) et 5 ✧ nouvelles issues des PDF (non-réponse 3,9 % et hot deck ; ruptures ERFS 2021 chiffrées ; précision publiée par strate ; révisions 2023-2025 chiffrées ; réouverture ✧ du chômage BIT). Chaque ✦ porte ≥2 familles de provenance dérivées et une réfutation terminale.
- **Responsabilité** : les divisions Insee assument la documentation (IM 136/145, fiches) ; IGF/IGAS le contrôle externe ; la direction la publication des révisions. L'auditabilité technique est directe : non-réponse, imputations et CV sont publics.
- **Limites explicites** : tableaux partiels non OCR-isés ; taux de réponse par vague EEC non centralisés ; note EEC sourcée par chemin local validé (URL d'origine non re-résoluble) ; une page 404 et deux pages JavaScript sans texte documentées comme échecs réels. Quatre gaps restent ouverts et routés vers NEXT_QUERIES.

## Verdict

**Établi** : les gaps ACCESS du parent sont refermés à 3/7 par extraction, avec identité d'octets vérifiée ; la machine statistique est documentée jusque dans ses imputations et ses variances ; les révisions sont quantifiées par l'institut lui-même. **Non établi** : toute manipulation dans les documents extraits. Le lead se déplace une fois de plus vers sa version soluble : la transparence existe, **à seuil technique** — et l'asymétrie entre le chiffre qui fait titre et la révision qui se corrige en silence reste le mécanisme de pouvoir le mieux documenté de toute la chaîne.
