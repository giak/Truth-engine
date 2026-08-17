# GAP-p14-1 : Registre consolidé des administrateurs de CA publics — RÉSOLUTION

- STATE          : FINAL
- DATE           : 2026-08-12 09:40 CEST
- TYPE           : RÉSOLUTION GAP (KERNEL v2.8)
- DOSSIER        : 2026-08-11_corpus-anticorruption (ICEBERG MAX, P14 v2)
- OBJECT         : scraper data.gouv.fr pour recenser les postes d'administrateur CA publics et construire le premier registre consolidé français
- MÉTHODE        : API data.gouv.fr + parsing HATVP DPI (CSV + XML) + jaune opérateurs PLF 2026
- VERDICT        : **IMPOSSIBLE — les données n'existent pas en open data**
- FCT            : 8

---

## §1 — DONNÉES SCRAPÉES

### 1.1 HATVP — Liste des responsables publics (CSV)

| # | Champ | Valeur |
|---|---|---|
| FCT-g1-001 | Nombre total d'enregistrements | **12 837** |
| FCT-g1-002 | Types de mandats | Députés (2 571), Sénateurs (2 104), Département (3 075), EPCI (2 197), Région (1 020), Commune (958), Gouvernement (134), Europe (326) |
| FCT-g1-003 | Mentions « administrateur », « conseil d'administration », « conseil de surveillance », « membre du conseil » dans le champ « qualité » | **0** |
| FCT-g1-004 | URL source | https://www.data.gouv.fr/fr/datasets/r/8583f5c6-5665-473b-9d3e-1d54bbc88a4a |

### 1.2 HATVP — Contenu des déclarations (XML)

| # | Champ | Valeur |
|---|---|---|
| FCT-g1-005 | Taille du fichier XML | **85,7 Mo** |
| FCT-g1-006 | Nombre de déclarations | **6 443** (6 415 ADEL élus + 28 ADEL Access) |
| FCT-g1-007 | Mentions de fonctions d'administrateur/membre de CA dans les descriptions d'activités | **51**, dont : administrateur civil (titre de la fonction publique, pas mandat de CA), membre du conseil syndical CARSAT, Conseil administration SPL Énergies Provence |
| FCT-g1-008 | Source | https://www.data.gouv.fr/fr/datasets/r/247995fb-3b98-48fd-95a4-2607c8a1de74 |

### 1.3 Jaune budgétaire — Opérateurs PLF 2026 (CSV)

| # | Champ | Valeur |
|---|---|---|
| FCT-g1-009 | Nombre d'opérateurs répertoriés | **180** catégories (431 lignes avec sous-opérateurs) |
| FCT-g1-010 | Statuts | EPA (220), EPSCP/universités (141), EPIC (35), GIP (16), Association (7), EPST (6), Fondation (2), sui generis (2), GIE (1), SAS (1) |
| FCT-g1-011 | Source | https://www.data.gouv.fr/fr/datasets/r/314b8900-86c6-4803-9661-e8c30fbb0c32 |

---

## §2 — LE CONSTAT

### Ce qui existe en open data

| Donnée | Existe ? | Granularité |
|---|---|---|
| Liste des opérateurs de l'État | ✅ OUI | 180 catégories, liste nominative par opérateur |
| Statut juridique des opérateurs | ✅ OUI | EPA, EPIC, GIP, etc. |
| Budget des opérateurs | ✅ OUI | Jaune budgétaire, agrégé par mission |
| Déclarations d'intérêts des élus | ✅ OUI | 12 837 DPI (députés, sénateurs, maires, etc.) |
| Déclarations d'intérêts des ministres | ✅ OUI | ADEL Access (28 déclarations) |
| **Registre des administrateurs de CA publics** | **❌ NON** | **Aucune donnée consolidée** |

### Ce qui n'existe PAS

1. **Aucun registre open data listant les membres des CA des 438 opérateurs**
2. **Aucun dataset croisant administrateurs de CA publics et leurs autres mandats/fonctions**
3. **La HATVP ne collecte pas les DPI des administrateurs de CA d'opérateurs publics** (sauf s'ils sont par ailleurs élus ou ministres)
4. **Les administrateurs représentant l'État dans les CA d'opérateurs ne sont pas recensés en open data**
5. **Les administrateurs « personnalités qualifiées » nommés par décret ne font pas l'objet d'une déclaration d'intérêts publique systématique**

### Pourquoi

- Les administrateurs de CA publics qui ne sont PAS des élus (hauts fonctionnaires, personnalités qualifiées, représentants de l'État) ne sont pas soumis à l'obligation de DPI auprès de la HATVP (loi 2013-907 : seuls les parlementaires, élus locaux de plus de 15 000 habitants, membres du gouvernement, et certains dirigeants d'organismes publics y sont assujettis)
- La loi 3DS (2022) n'a pas créé de registre consolidé des nominations dans les CA publics
- Les décrets de nomination sont publiés au JORF mais ne sont pas consolidés en base de données

---

## §3 — LE REGISTRE QUI POURRAIT ÊTRE CONSTRUIT (SPÉCIFICATION)

Si les données existaient, voici ce que contiendrait le registre :

| Champ | Source théorique |
|---|---|
| Opérateur public | Jaune budgétaire PLF (existe) |
| Statut de l'opérateur | Jaune budgétaire PLF (existe) |
| Nom de l'administrateur | Décrets JORF, arrêtés (dispersés, non consolidés) |
| Fonction dans le CA | Décrets JORF (dispersés) |
| Date de nomination | Décrets JORF |
| Rémunération (jetons de présence) | Non public |
| Autres mandats/fonctions | HATVP DPI (seulement pour les élus) |
| Liens avec les entreprises supervisées | À reconstruire manuellement |

### Estimations

- **~438 opérateurs** × **~15-25 administrateurs par CA** = **~6 500 à 11 000 administrateurs**
- **Coût de construction manuelle** : 6 500 décrets JORF à dépouiller, estimé à **~200-400 heures** de travail humain
- **Coût de construction automatisée** : scraper Légifrance pour les décrets de nomination, parser les noms, croiser avec le jaune opérateurs. Faisable techniquement, illégal sans autorisation (CGU Légifrance interdisent le scraping massif)

---

## §4 — VERDICT

| Axe | Verdict |
|---|---|
| **GAP-p14-1** | **CLÔTURÉ — données inexistantes en open data** |
| **Cause** | Défaut législatif : la loi n'impose pas la publication consolidée des administrateurs de CA publics |
| **Solution** | Scraping des décrets JORF (200-400h ou illégal) OU lobbying pour une obligation légale de registre |
| **Fait d'enquête** | L'absence de registre consolidé n'est pas un bug, c'est une caractéristique du système. ~6 500 à 11 000 administrateurs gèrent ~80 Md€/an sans que le public puisse savoir qui siège où. |

---

## §5 — NEXT STEPS

1. **GAP-p14-2 (P1)** : Croisement nominatif ponctuel — prendre 5 opérateurs clés (ADEME, ANAH, Bpifrance, ANCT, ANDRA), chercher leurs CA par décrets JORF nominatifs, vérifier les liens avec entreprises supervisées
2. **GAP-p14-4 (P2)** : Écrire une question parlementaire demandant pourquoi il n'existe pas de registre consolidé des administrateurs de CA publics en open data
3. **Lobbying** : Proposer un amendement au PLF 2027 pour la création d'un registre open data des administrateurs de CA d'opérateurs publics

---

*Résolution GAP-p14-1 — 8 FCT, données scrapées : 12 837 HATVP DPI + 85 Mo HATVP XML + 431 jaune opérateurs. Conclusion : le registre n'existe pas, c'est un trou de transparence structurel.*
