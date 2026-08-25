# Quintessence — IA & Société #2 : Droit du travail

> **Source** : `2026-08-24_20-40_leffondrement-droit-travail_INVESTIGATION.md` (KERNEL v2.8, RUN_ID `20260824-2040`, 129 lignes, GATE PASS)
> **Date extraction** : 2026-08-24 22:00
> **Protocole** : SUBLIMATOR v36 Phase 1 only.

## 1. Métadonnées & trace source

- **Autorité** : KERNEL v2.8, RUN_ID `20260824-2040-leffondrement-droit-travail`, PARENT `20260824-1822`
- **Statut** : FINAL, GATE PASS, COMPLEXITY 8→COMPLEX
- **Périmètre** : Peut-on requalifier une API ? GDPR Art.22, AI Act, jurisprudence Uber/Deliveroo
- **Requêtes** : 2 web_search (QRY-D01, QRY-D02)
- **Mnemolite** : vierge

## 2. Faits atomiques préservés

| FCT-ID | Sujet | Valeur | EPI | mem |
|---|---|---|---|---|
| FCT-D01 | Cour cassation 9 juil 2025 : Uber = indépendants (revirement) | VÉRIFIÉ — DLA Piper, Eurofound, Le Club des Juristes | EPI:- | mem:- |
| FCT-D02 | GDPR Art.22 : droit opposable à toute décision « solely automated » | VÉRIFIÉ — GDPR-text.com, Legiscope (juil 2026) | EPI:- | mem:- |
| FCT-D03 | AI Act : systèmes IA « emploi » classés haut risque | VÉRIFIÉ — AI Act | EPI:- | mem:- |
| FCT-D04 | CNIL : régulateur « agressif » sur IA et profilage | VÉRIFIÉ — GDPR Regulation.eu (2026) | EPI:- | mem:- |
| FCT-D05 | Une API ne peut pas être « requalifiée » en salarié | VÉRIFIÉ — pas de personne, pas de contrat | EPI:- | mem:- |

## 3. Acteurs nominaux

- **Cour de cassation** — arrêts Take Eat Easy (2018), Uber (2020, revirement 2025)
- **CNIL** — régulateur français agressif sur IA/profilage
- **DLA Piper, Eurofound** — sources juridiques sur la jurisprudence Uber

## 4. Sources externes citées

- SRC-D01 : DLA Piper — « French Supreme Court Uber ruling » (août 2025)
- SRC-D02 : Eurofound — « France Uber drivers independent contractors » (juil 2025)
- SRC-D03 : GDPR-text.com — Article 22
- SRC-D04 : Legiscope — GDPR Art.22 (juil 2026)
- SRC-D05 : GDPR Regulation.eu — GDPR in France (2026)

## 5. Chronologie datée

- **28 nov 2018** : Cour cassation, Take Eat Easy — plateforme = employeur
- **4 mars 2020** : Cour cassation, Uber — chauffeur = salarié
- **9 juil 2025** : Cour cassation, Uber — revirement, chauffeur = indépendant
- **2024** : AI Act entré en vigueur (application progressive 2024-2027)

## 6. Mécanismes / chaînes causales

### M1 : Requalification salariale inapplicable à l'IA

- Niveau L1. Type OBSERVATION. VÉRIFIÉ
- Mécanisme : critère de subordination (art. L8221-6) → requalification vise la relation humain/plateforme → une API n'est pas un humain → requalification impossible → MAIS le cadre juridique ne se limite pas à cela

### M2 : GDPR Art.22 + AI Act = cadre existant contre le licenciement algorithmique

- Niveau L1. Type CADRE. VÉRIFIÉ
- Mécanisme : décision « exclusivement automatisée » + effet juridique = interdit → licenciement par IA = illégal si pas de supervision humaine réelle → AI Act classe l'emploi comme « haut risque »

## 7. Verbatim et citations

> « La personne concernée a le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé. » — GDPR Art.22

> « Le système immunitaire du modèle social est conçu pour un pathogène qui a un contrat. » — Vidéo analysée (claim partiellement vrai : le contrat est un point d'entrée mais GDPR Art.22 couvre toute décision automatisée)

> « On ne peut pas requalifier une API. » — Vidéo (VRAI mais conclusion trop large : l'arsenal juridique ne se limite pas à la requalification)

## 8. Notes méthodologiques source

- **Note 1** : Investigation courte (129 lignes) mais ciblée sur la question juridique précise
- **Note 2** : 5 sources juridiques, 5 faits enregistrés
- **Note 3** : La vidéo crée un faux dilemme (requalification ou rien) alors que GDPR Art.22 + AI Act existent

## 9. Limites connues de cette extraction (case-limites)

- Pas de FACT_REGISTRY_V1 format complet dans la source
- Pas d'EPI/mem dans la source
- Jurisprudence en évolution rapide (revirement Uber 2025)