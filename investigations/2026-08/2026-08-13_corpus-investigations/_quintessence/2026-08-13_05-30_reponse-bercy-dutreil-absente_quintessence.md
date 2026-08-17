# Quintessence : GAP-003 résolu : la « réponse de Bercy » au rapport CdC Dutreil n'existe pas : « Destinataire n'ayant pas répondu »

Source : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_reponse-bercy-dutreil-absente/2026-08-10_08-04_reponse-bercy-dutreil-absente_INVESTIGATION.md` (8 FCT-001..007)
Date extraction : 2026-08-13 05:30 CEST
Pilote : Buffy (FreeBuff) : Sublimator v36 Phase 1 (corpus complet, lot bloc DMTG/BNDP/CDC)

---

## 1. Métadonnées & trace source

- **Autorité** : KERNEL v2.8, format léger, axe anticorruption, bloc connaissance patrimoniale (BNDP/Dutreil)
- **Date source** : 2026-08-10 08:04 CEST, STATE FINAL
- **Identifiants source** : 7 FCT-001..007
- **Object** : la réponse du Gouvernement (Bercy) au rapport CdC Dutreil précise-t-elle le régime d'accès à la BNDP ?
- **Verdict source** : la question se résout par constat d'absence documenté à la source primaire : le ministère de l'économie n'a PAS répondu au rapport ; le silence est une donnée

## 2. Faits atomiques préservés

- FCT-001 : le PDF officiel « Réponses des administrations » du rapport Dutreil (18/11/2025) contient uniquement la mention « Destinataire n'ayant pas répondu : Monsieur le ministre de l'économie, des finances et de la souveraineté industrielle et énergétique » (3 pages, 921 octets de texte, lu intégralement) [L32 (mesuré)]
- FCT-002 : aucune occurrence de BNDP / base nationale / patrimoniales / habilitation / secret fiscal / module statistique / DMTG dans le fascicule (grep exhaustif) [L33 (mesuré)]
- FCT-003 : le téléchargement direct depuis ccomptes.fr fonctionne (HTTP 200, 254 313 octets) : l'échec du 07-46 était un timeout Wayback (504 nginx), pas une indisponibilité du fichier [L34 (mesuré)]
- FCT-004 : le fichier possède un snapshot Wayback alternatif (20251120095126, HTTP 200) : version unique publiée [L35 (mesuré)]
- FCT-005 : la question « la réponse Bercy précise-t-elle le régime d'accès à la BNDP ? » se résout par absence : il n'y a pas de réponse à analyser [L36 (mesuré)]
- FCT-006 : le ministère de l'économie, destinataire nommé par la Cour, est resté silencieux sur un rapport qui documente l'exploitation de sa propre base (BNDP) par la CdC [L37 (mesuré)]
- FCT-007 : limite : le silence ne prouve ni dissimulation ni mépris (agenda, choix de communication possibles) : le fait documenté est le silence lui-même [L38 (mesuré)]

## 3. Acteurs nominaux

**Institutions** : ministère de l'économie, des finances et de la souveraineté industrielle et énergétique (« Bercy », destinataire non-répondant), Cour des comptes (émettrice), DGFiP (gestionnaire BNDP). Personne physique titulaire du portefeuille au 18/11/2025 non vérifiée en session (le raccourci « Lecornu » du 07-46 est impropre pour la personne, correct pour la fonction).

## 4. Sources externes citées

PDF 20251118-reponse-Pacte Dutreil.pdf (ccomptes.fr, lu intégralement), CDX Wayback, dossier 07-46 (Annexe 4 BNDP), dossier 07-51 (BNDP absente du 3056).

## 5. Chronologie datée

18/11/2025 : publication du rapport Dutreil + fascicule de réponses ; 20/11/2025 : snapshot Wayback (HTTP 200) ; 10/08/2026 : téléchargement direct et vérification (GAP-003 résolu).

## 6. Mécanismes / chaînes causales

**M1 — Le triple silence cumulatif** : la CdC nomme la BNDP (Annexe 4), le Sénat 760 la nomme (p. 14), la commission AN ne la nomme jamais (07-51), et le ministère qui gère la BNDP ne répond pas au rapport qui la décrit : la convergence des absences est un fait. Force : EXTRÊME. Niveau : L1. [L37 (mesuré)]
**M2 — La non-réponse comme événement** : pour l'évaluation la plus complète jamais produite sur une niche de 5,5 Md€, le ministère qui gère la dépense et la base est resté silencieux : la pratique des rapports thématiques veut que les destinataires répondent. Force : HAUTE. Niveau : L2. [L36-L37 (mesuré)]
**M3 — L'anti-sur-affirmation** : le silence ne prouve pas de volonté de dissimuler : les causes banales ne sont pas exclues ; le fait documenté est le silence, rien de plus. Force : EXTRÊME (honnêteté). Niveau : L1. [L38 (mesuré)]

## 7. Verbatim et citations

- « Destinataire n'ayant pas répondu : Monsieur le ministre de l'économie, des finances et de la souveraineté industrielle et énergétique » [L32 (mesuré)]
- « Le silence est ici une donnée. Il rejoint le faisceau des absences du corpus : quatre institutions, quatre régimes de parole : l'une la nomme en annexe technique, l'autre en page 14, la troisième jamais, la dernière pas du tout » [L44 (mesuré)]
- « Sur l'un des sujets les plus sensibles du système fiscal français : l'héritage des plus riches : l'administration choisit de ne pas parler, quand elle ne choisit pas de ne pas répondre » [L45 (mesuré)]

## 8. Notes méthodologiques source

- **Fiabilité** : source primaire lue intégralement (PDF 3 pages, 921 octets) ; grep exhaustif ; correction de désignation « Lecornu » (personne vs fonction) ; CONTR-001..003 résolus.
- **F-##** : 7/7 identifiants FCT-001..007 préservés.
- **Méthode** : route directe ccomptes.fr après échec Wayback, confirmation CDX, constat d'absence documenté, limite d'interprétation explicite.

## 9. Limites connues (case-limites)

- L'identité de la personne physique titulaire du portefeuille au 18/11/2025 n'est pas vérifiée en session (GAP-001).
- La procédure exacte de notification (combien de destinataires ont reçu le rapport) n'a pas été vérifiée (GAP-002).
- Le CP de la Cour (20251118-CP-Le-Pacte-Dutreil-Vdéf.pdf) non lu (GAP-003).
- Le silence de Bercy ne prouve ni dissimulation ni mépris : constat borné.
