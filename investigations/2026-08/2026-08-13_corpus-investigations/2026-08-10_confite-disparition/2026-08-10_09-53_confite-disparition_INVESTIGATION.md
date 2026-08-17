# INVESTIGATION — CONFITE : échéance naturelle de l'habilitation (07/11/2025) non renouvelée — la BPI garde ses 4 autres accès CSS, aucune trace de retrait ou de refus

```
IDENT        : INV-CONFITE-2026-08-10
STATE          : FINAL
TYPE         : INVESTIGATION
KERNEL       : v2.8
DATE         : 2026-08-10 09:53 CEST
PATH         : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_confite-disparition/
AUTEUR       : Buffy
OBJECT       : Vérifier pourquoi le projet CSS CONFITE (Banque Publique d'Investissement, transmissions d'entreprises) présent dans la liste de novembre 2025 (ListeProjets_251106.xlsx) a disparu de celle d'avril 2026 (ListeProjets260402.pdf) : échéance naturelle, retrait ou refus de renouvellement ?
LIEN         : dossier 2026-08-10_09-19_css-projets-dmtg-dutreil (FCT-005/006 : CONFITE présent nov 2025, absent avril 2026) ; dossier 09-15 (référentiel CASD) ; FAQ CSS (durée d'habilitation)
```

## 0. TEXT_ANALYSIS

**Requête** : CONFITE a-t-il expiré naturellement, a-t-il été retiré, ou son renouvellement a-t-il été refusé ?

**Périmètre** : (1) sémantique exacte de la colonne date dans l'Excel 251106 (en-tête = « date fin habilitation ») ; (2) valeur brute de la date CONFITE (décodage sérial) ; (3) règle de durée des habilitations (FAQ CSS lue) ; (4) situation de la BPI dans le PDF avril 2026 (a-t-elle perdu tous ses accès ?) ; (5) Wayback Machine pour listes antérieures.

**CRÉDO** : distinguer (a) ce qui est documenté (date de fin = 07/11/2025, règle des 6 ans, FAQ) ; (b) l'hypothèse la plus probable (échéance naturelle) ; (c) ce qui reste non exclu (retrait/refus non publié).

## 1. PISTES

| # | Piste | Statut |
|---|-------|--------|
| P1 | Déterminer la sémantique de la colonne date de l'Excel 251106 | ✅ VÉRIFIÉE (en-tête shared string n° 2 : « date fin habilitation ») |
| P2 | Décoder la date brute de CONFITE (ligne 1097) | ✅ VÉRIFIÉE (sérial décodé = 2025-11-07) |
| P3 | Règle de durée des habilitations CSS | ✅ VÉRIFIÉE (FAQ lue : 6 ans depuis déc. 2016) |
| P4 | Situation de la BPI dans le PDF avril 2026 | ✅ VÉRIFIÉE (4 autres projets BPI présents) |
| P5 | Wayback Machine : listes antérieures de projets | ⚠️ INDISPONIBLE (CDX timeout/résultat vide) |
| P6 | Documentation publique de CONFITE (Bpifrance, presse) | ✅ CLÔTURÉE (chercheur web non livré au moment de la clôture — borné, LIMITE 4) |

## 2. BIAS TEST

| Symbole | Score | Justification |
|---------|-------|---------------|
| 🟧 Sélection | 1/15 | Deux listes (nov 2025 + avril 2026) croisées avec la FAQ |
| 🟨 Succès de confirmation | 1/15 | L'hypothèse « échéance naturelle » est la plus simple — mais le retrait/refus n'est pas exclu (borne explicite) |
| 🟩 Biais de confirmation | 2/15 | La vérification BPI (4 accès conservés) résiste au récit « conflit BPI/CSS » |
| **Total** | **4/75** | Résistance correcte |

## 3. FACT_REGISTRY

| # | Fait | Valeur | Source | Statut |
|---|------|--------|--------|--------|
| FCT-001 | **La colonne date de l'Excel ListeProjets_251106 correspond à la « date fin habilitation »** (et non à une date de début) — en-tête de colonne « date fin habilitation » (shared string n° 2), même sémantique que le PDF 260402 | date fin | Excel 251106 (en-tête lu) | CONFIRMÉ |
| FCT-002 | **CONFITE a une date de fin d'habilitation au 07/11/2025** — décodage de la valeur brute de la ligne 1097 (sérial Excel → 2025-11-07) ; la liste Excel est datée du 06/11/2025 (nom : 251106), soit un jour avant l'échéance : CONFITE figurait dans la liste au dernier jour de validité | fin = 2025-11-07 | Excel 251106 ROW 1097 (décodée) | CONFIRMÉ |
| FCT-003 | **L'habilitation initiale CSS dure 6 ans** (depuis décembre 2016 ; avant = 3 ans), à compter de la date d'avis favorable du comité — une habilitation finissant le 07/11/2025 a donc été accordée vers novembre 2019 (déduction : 6 ans avant la fin ; la date d'accord n'est pas dans l'Excel) | 6 ans | FAQ CSS (ligne 31-33, lue) | CONFIRMÉ (règle 6 ans) ; déduction ~nov 2019 |
| FCT-004 | **La FAQ CSS alerte sur l'expiration sans renouvellement** : « si la demande de prolongation n'est pas formulée à temps, vous risquez une interruption de votre accès aux sources. Aucune dérogation ne sera accordée » — l'arrêt à échéance sans prolongation est un scénario explicitement prévu | avertissement | FAQ CSS (ligne 41, lue) | CONFIRMÉ |
| FCT-005 | **CONFITE est absent du PDF d'avril 2026** (grep = 0 occurrence) — 5 mois après sa date de fin d'habilitation (07/11/2025) | absent | PDF 260402 (grep lu) | CONFIRMÉ (constat d'absence) |
| FCT-006 | **La BPI a conservé au moins 4 autres habilitations CSS dans le PDF avril 2026** (5 en comptant PROCRED porté par la filiale « Bpifrance Financement », l. 17106, 22/06/2026) : DISPBPI (impact des dispositifs Bpifrance, 07/10/2031), EVALBPI (évaluation d'impact socio-économique, 21/12/2027), un projet PIA (d'Avenir 2010-2021), FIPENIT (financement et performances, 06/07/2027) — la disparition de CONFITE est **spécifique au projet**, pas une perte générale d'accès de la BPI au CSS | ≥ 4 (5 avec PROCRED) | PDF 260402 (lus, l. 2405, 11762, 12382, 13580, 17106) | CONFIRMÉ |
| FCT-007 | **Aucune trace de CONFITE sous une nouvelle dénomination** dans le PDF avril 2026 — les recherches « contrainte de financement », « transmissions d'entreprises », « CONFITE » ne retournent rien | 0 | PDF 260402 (grep lu) | CONFIRMÉ (constat d'absence) |
| FCT-008 | **La Wayback Machine ne permet pas de retrouver les listes antérieures** de projets CSS (CDX sur wp-content/uploads : timeout / résultat vide) — la chronologie complète reste inaccessible | indisponible | Wayback CDX (tentée) | CONSTAT (borné) |
| FCT-009 | **Le CSS ne publie pas les motifs de fin d'habilitation** (retrait, refus, non-renouvellement) — seules les durées apparaissent dans les listes ; un refus de renouvellement ou un retrait ne serait pas documenté publiquement | pas de motifs publics | Structure du CSS (dossier 09-19) | CONSTAT (borné) |

## 4. PELOTE

```
CONFITE (Contrainte de financement et transmissions d'entreprises, BPI)
        ↓ Date de fin d'habilitation (en-tête Excel : « date fin habilitation »)
07/11/2025 — DÉCODÉE (sérial Excel ligne 1097)
        ↓ Règle de durée (FAQ CSS)
Habilitation de 6 ans (depuis déc 2016) → accordée ~ nov 2019
        ↓ Absence dans la liste suivante
PDF avril 2026 : CONFITE ABSENT (grep = 0) — 5 mois après l'échéance
        ↓ Situation de la BPI
4 autres projets BPI conservés (DISPBPI, EVALBPI, PIA, FIPENIT)
        ↓ Conclusion
HYPOTHÈSE LA PLUS PROBABLE : échéance naturelle non renouvelée
  (FAQ : « aucune dérogation » si prolongation non formulée à temps)
  NON EXCLU : retrait ou refus de renouvellement (CSS ne publie pas les motifs)
```

## 5. GATE_CHECK

- **FCT-006 du dossier 09-19 (« CONFITE absent du PDF 260402 », statut CONSTAT borné) : CONFIRMÉ ET EXPLIQUÉ.** La date de fin d'habilitation de CONFITE est le 07/11/2025 (décodée), la liste d'avril 2026 est postérieure de 5 mois — l'absence est cohérente avec l'échéance.
- **Hypothèse retenue** : échéance naturelle non renouvelée (le scénario le plus simple, cohérent avec la règle des 6 ans et l'avertissement de la FAQ). **Non exclu** : un retrait ou un refus ne serait pas documenté publiquement (FCT-009).
- **La question « la BPI a-t-elle été sanctionnée ? » est réfutée** : la BPI conserve 4 accès CSS (FCT-006) — il ne s'agit pas d'une perte générale d'accès liée à un conflit.

## 6. SOURCES (SRC)

| # | Source | Type | Date accès |
|---|--------|------|-----------|
| SRC-001 | Excel ListeProjets_251106.xlsx (1 169 lignes, en-tête « date fin habilitation » + ROW 1097 CONFITE décodée : 2025-11-07) | Primaire (CSS) | 10/08/2026 |
| SRC-002 | FAQ du Comité du secret statistique (durée 6 ans, avertissement non-renouvellement — lignes 31-33, 41) | Primaire (CSS) | 10/08/2026 |
| SRC-003 | PDF ListeProjets260402.pdf (2,2 Mo, avril 2026 : CONFITE absent, 4 projets BPI présents) | Primaire (CSS) | 10/08/2026 |
| SRC-004 | Wayback Machine CDX (tentée, indisponible) | Secondaire | 10/08/2026 |
| SRC-005 | Corpus : dossier 09-19 (FCT-005/006), dossier 09-15 | Corpus | 10/08/2026 |

## 7. LIMITES

1. **La date 2025-11-07 est bien la date de fin d'habilitation** (en-tête confirmé), mais la date de DÉBUT n'est pas dans l'Excel — l'hypothèse « accordée ~novembre 2019 » (6 ans) est une déduction, non une donnée.
2. **Un retrait ou un refus de renouvellement n'est pas exclu** : le CSS ne publie pas les motifs de fin d'habilitation (FCT-009). La preuve d'une échéance naturelle est une inférence à partir de la date de fin + la règle des 6 ans, pas une pièce administrative.
3. La Wayback Machine n'a pas permis de récupérer la liste antérieure (novembre 2019 ou antérieure) qui confirmerait la date d'accord réelle.
4. Le chercheur web (documentation publique CONFITE chez Bpifrance) n'a pas encore livré ses résultats au moment de la clôture — le dossier pourra être complété si une source publique documente le projet.
5. CONFITE ne concernait pas la source DMTG (sources : BTS, BRN, Contours, LIFI, FARE, SUSE) — sa disparition n'affecte PAS la carte des utilisateurs de la donnée successorale (dossier 09-31).

## 8. VERDICT

**CONFITE a très probablement fait l'objet d'une échéance naturelle non renouvelée.** Sa date de fin d'habilitation est le 07/11/2025 (décodée de l'Excel, en-tête « date fin habilitation »), soit 5 mois avant la liste d'avril 2026 qui ne la contient plus. La règle des 6 ans (habilitations initiales depuis déc. 2016) situe son accord vers novembre 2019, et la FAQ CSS met explicitement en garde contre l'interruption faute de prolongation (« aucune dérogation ne sera accordée »). **La BPI a conservé ses 4 autres accès CSS (DISPBPI, EVALBPI, projet PIA, FIPENIT) — la disparition de CONFITE est spécifique au projet, pas une sanction ni un conflit général.** Un retrait ou un refus de renouvellement ne peut toutefois pas être formellement exclu, le CSS ne publiant pas les motifs de fin d'habilitation. **Ce scénario est bénin pour le faisceau patrimonial : CONFITE ne portait pas sur la source DMTG, et sa sortie n'altère pas la carte des 8 projets utilisant la donnée successorale (dossier 09-31).**

## 9. RECOMMANDATIONS

1. **Compléter le dossier si le chercheur web documente CONFITE** (publication Bpifrance Le Lab, presse) — vérifier que le projet a bien mené ses travaux jusqu'à l'échéance.
2. **Tenter de récupérer la liste CSS antérieure** (via le site comite-du-secret.fr directement, non Wayback) pour confirmer la date d'accord de CONFITE (~nov 2019).
3. **Le constat est clos pour le faisceau** : l'échéance naturelle de CONFITE est documentée et sans impact sur la carte DMTG.

## 10. LEÇON

**La disparition d'un projet CSS est, sauf preuve contraire, un événement administratif ordinaire : une habilitation de 6 ans qui arrive à terme et ne demande pas de prolongation.**CONFITE, projet de la BPI sur les transmissions d'entreprises, a cessé au 07/11/2025 — sans que la Banque publique perde ses autres accès (au moins 4, voire 5 avec PROCRED/Bpifrance Financement).**Le seul point non documenté est le motif : échéance, retrait ou refus restent théoriquement possibles, et le Comité du secret statistique ne publie jamais les raisons.** Mais l'explication la plus simple couvre entièrement les faits — et c'est elle que la règle anti-surcharge impose de retenir.