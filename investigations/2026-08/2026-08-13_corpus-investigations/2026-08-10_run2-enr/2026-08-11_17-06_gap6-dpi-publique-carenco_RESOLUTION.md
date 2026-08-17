# GAP-fd-6 RÉSOLU : LA DPI PUBLIQUE DE CARENCO N'EST PLUS CONSULTABLE (constat d'absence sur 3 preuves), ET AURAIT ÉTÉ ANTÉRIEURE AU MANDAT FEDEREC

- STATE          : FINAL
- DATE           : 2026-08-11 17:06 CEST
- TYPE           : RESOLUTION (KERNEL v2.8, format allégé axe piste)
- DOSSIER        : 2026-08-10_run2-enr (fil VP-P4, GAP-fd-6 ré-ouvert 16:50)
- OBJECT         : récupérer la DPI publique de Carenco (membre du Gouvernement 04/07/2022 - 20/07/2023) sur hatvp.fr et vérifier les fonctions bénévoles déclarées et l'existence d'une déclaration complémentaire mentionnant FEDEREC
- SOURCES        : CSV open data HATVP liste.csv (3,3 Mo, 12 836 lignes, téléchargé 17:00), pages nominatives hatvp.fr, communiqués HATVP du 01/12/2022 et du 08/07/2024 (lus intégralement)
- VERDICT        : CONSTAT D'ABSENCE ROBUSTE - la DPI de Carenco a bien été publiée (01/12/2022) mais n'est plus en ligne : règle HATVP « 6 mois après la fin des fonctions » (fin 20/07/2023 → retrait ~01/2024) ; de plus elle serait antérieure au mandat FEDEREC (14/11/2023)

## 1. La question

Le GAP-fd-6 (ré-ouvert le 16:50 après la correction P1 du 16-45) : la DPI de Carenco en qualité de membre du Gouvernement est **publique** (page officielle HATVP citée dans le 16-45). Il s'agissait de la récupérer pour vérifier : (1) les fonctions bénévoles déclarées, (2) une éventuelle déclaration complémentaire mentionnant FEDEREC.

## 2. Les preuves (3 voies d'accès, toutes convergentes)

| ID | Fait |
|----|------|
| FCT-fd6-001 | Le CSV open data HATVP `https://www.hatvp.fr/livraison/opendata/liste.csv` (3 279 128 octets, 12 836 lignes, téléchargé le 11/08/2026 17:00) ne contient **aucune occurrence de CARENCO** (recherche exhaustive dans tous les champs : 0 hit). |
| FCT-fd6-002 | Le type_mandat `gouvernement` du CSV (134 lignes) ne couvre que les **ministres en exercice 2025-2026** et quelques anciens ministres très récents (De Montchalin, Amiel, Parmentier-Lecocq, Vedrenne, Brégeon, dépôts 2026). Les ministres de l'ère Borne 2022-2023 (Carenco, N'Daye, Schiappa, Le Maire) sont **absents** : l'open data ne remonte pas aux DPI ministérielles de 2022-2023. |
| FCT-fd6-003 | Les pages nominatives HATVP `https://www.hatvp.fr/pages_nominatives/carenco-jean-francois` (et variantes) ne renvoient **aucune fiche** (retour page d'accueil, 0 mention Carenco) : pas de fiche nominative pour lui. |
| FCT-fd6-004 | Le communiqué HATVP du 01/12/2022 « Publication et bilan des déclarations des membres du Gouvernement de Mme Elisabeth Borne » (lu intégralement) liste explicitement « Jean-François CARENCO » parmi les **41 membres du Gouvernement dont les déclarations d'intérêts et de situation patrimoniale ont été publiées sur hatvp.fr**. Preuve positive : la DPI a bien existé et a été publiée. |
| FCT-fd6-005 | Le communiqué HATVP du 08/07/2024 « Publication des déclarations des membres et anciens membres du Gouvernement » (lu intégralement) énonce la règle de consultabilité : « Les déclarations d'intérêts et de situation patrimoniale des membres du Gouvernement sont publiées sur le site internet de la Haute Autorité jusqu'à la fin des fonctions des personnes concernées. **Les déclarations des anciens membres du Gouvernement sont consultables jusqu'à six mois après la fin de leurs fonctions gouvernementales.** » |
| FCT-fd6-006 | Carenco a cessé ses fonctions de ministre délégué chargé des Outre-mer le 20/07/2023 (départ du gouvernement Borne). Application de la règle FCT-fd6-005 : ses DPI étaient consultables jusqu'à ~janvier 2024, puis **retirées du site**. En août 2026, elles ne sont plus en ligne. |
| FCT-fd6-007 | **Croisement de 3 constats d'absence** (CSV open data actuel, pages nominatives, règle de retrait) : la DPI publique de Carenco est inaccessible en ligne à la date d'aujourd'hui. Le GAP-fd-6 se résout en constat d'absence robuste, pas en preuve positive du contenu. |
| FCT-fd6-008 | **Limite chronologique supplémentaire** : même si la DPI avait été consultable, elle aurait été antérieure au mandat FEDEREC. La DPI initiale a été déposée dans les 2 mois de la nomination du 04/07/2022 (source : communiqué 01/12/2022 « toutes les déclarations ont été déposées dans le délai légal de deux mois à compter de la nomination »), soit au plus tard début 09/2022 ; la déclaration actualisée de fin de mandat a été déposée dans les 2 mois suivant le 20/07/2023 (soit ~09/2023), **avant** la nomination FEDEREC du 14/11/2023. Aucune de ces déclarations ne peut documenter FEDEREC, sauf déclaration complémentaire spontanée non identifiée. |
| FCT-fd6-009 | Le point 6 de la FAQ HATVP (« Fonctions bénévoles susceptibles de faire naître un conflit d'intérêts ») précise que seules les activités bénévoles **susceptibles de créer un conflit d'intérêts** sont déclarables (art. 2 loi 2013-907). FEDEREC étant une fédération du recyclage, hors secteur d'activité économique réglementée de Carenco (énergie), la déclarabilité du mandat dans une DPI ministérielle n'est pas établie et relèverait de l'appréciation du déclarant. |
| FCT-fd6-010 | **(DÉDUCTION)** La nomination FEDEREC (14/11/2023) survient **après** la sortie du Gouvernement (20/07/2023) : elle ne déclencherait pas d'obligation de DPI publique nouvelle (l'obligation de dépôt des anciens membres court jusqu'à la fin des fonctions + 2 mois, échue ~09/2023). Le mandat FEDEREC relèverait du **contrôle des mobilités** (art. 23 loi 2013-907), déjà traité par les avis 2023-247/248 (cf. 16-31), et non des DPI. Déduction légale raisonnable, cohérente avec le 16-31, non vérifiée par un texte lu. |
| FCT-fd6-011 | **Verdict** : le bénévolat présumé du 16-45 reste inchangé ; la piste « DPI publique » est épuisée par un constat d'absence robuste. Aucun fait d'infraction. La seule voie restante pour confirmer le bénévolat formellement reste les statuts/comptes de FEDEREC (GAP-fd-5), hors OSINT. |

## 3. Synthèse

| Voie d'accès | Résultat | Statut |
|--------------|----------|--------|
| CSV open data liste.csv (12 836 lignes, extraction 11/08/2026) | CARENCO absent (0 hit) | CONSTAT D'ABSENCE |
| Pages nominatives carenco-* | Aucune fiche | CONSTAT D'ABSENCE |
| Communiqué 01/12/2022 | Carenco bien publié parmi les 41 ministres Borne | PREUVE POSITIVE (existence) |
| Communiqué 08/07/2024 | Règle de retrait : 6 mois après fin des fonctions | RÈGLE (explique l'absence actuelle) |
| Chronologie | DPI 2022 + actualisée 09/2023 < FEDEREC 14/11/2023 | LIMITE DÉFINITIVE |

**Verdict** : le GAP-fd-6 est résolu en **constat d'absence robuste** : la DPI publique de Carenco a existé et a été publiée, mais n'est plus consultable (règle de retrait à 6 mois, fin de fonctions 20/07/2023) et aurait de toute façon été antérieure au mandat FEDEREC. La question « FEDEREC déclaré dans une DPI » est hors de portée OSINT.

## 4. Fichiers liés

| Document | Lien |
|----------|------|
| GAP-fd-4 (16-45) : bénévolat présumé, DPI des membres du Gouvernement publiques (P1 corrigé) | `2026-08-11_16-45_gap4-mandat-federec-benevolat_RESOLUTION.md` |
| GAP-fd-1 (16-31) : saisine HATVP, avis d'incompétence 2023-247 | `2026-08-11_16-31_gap1-saisine-hatvp-federec_RESOLUTION.md` |
| GAP-fd-3 (16-38) : 0 contact CRE déclaré au répertoire RI | `2026-08-11_16-38_gap3-federec-contacts-cre-repertoire-ri_RESOLUTION.md` |
| VP-P4 (13-20) : fil pantouflage régulateurs → ENR | `2026-08-11_13-20_vp4-pantouflage-cre-enr_INVESTIGATION.md` |

## 5. GAPs ouverts

| GAP | Question | Actionnabilité |
|-----|----------|----------------|
| fd-5 | Obtenir les statuts de FEDEREC/FEDERREC (via email ou site, hors courrier) pour vérifier le statut du président délégué | FAIBLE (pas de voie numérique identifiée) |
| rc-2 (hérité 16-38) | Vérifier si les fiches FEDEREC post-11/2023 comportent un champ dirigeant/déclarant reliant les actions à Carenco | MOYEN (JSON agora) |

Revue critique appliquée le 11/08/2026 17:10. P2 corrigés 17:13 (FCT-fd6-008 : datation DPI alignée sur la fenêtre sourcée « au plus tard début 09/2022 » ; FCT-fd6-010 : déduction juridique marquée (DÉDUCTION)).
