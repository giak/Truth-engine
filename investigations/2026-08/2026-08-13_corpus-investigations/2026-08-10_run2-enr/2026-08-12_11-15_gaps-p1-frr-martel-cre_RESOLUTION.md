# GAPs P1 run2-ENR — RÉSOLUTION FINALE

- STATE          : FINAL
- DATE           : 2026-08-12 11:15 CEST
- TYPE           : RÉSOLUTION GAPs (KERNEL v2.8)
- DOSSIER        : 2026-08-10_run2-enr (fil VP-P4 pantouflage régulateurs → ENR)
- OBJECT         : clôturer les 2 GAPs P1 restants du REGISTRE 17-14
- FCT            : 6

---

## GAP-P1-1 : FRR → Ardian (fermeture du circuit argent public → fonds Thodoroff)

**STATUT : ✅ CLÔTURÉ — déjà résolu le 11/08/2026**

Le document `2026-08-11_17-35_gap1-frr-ardian_RESOLUTION.md` (FINAL, 10 FCT-fa) a établi avec preuves primaires :

| Fait clé | Preuve |
|---|---|
| Le FRR lance l'AO 2016FRR03 le 21/06/2016 (400 M€, 4 mandats) | Communiqué FRR |
| Ardian France sélectionnée le 20/07/2017 | Communiqué FRR attribution |
| FPS ARDIAN FONDS DE FONDS FRR CI FRANCE créée le 27/10/2017 (SIREN 832955462) | RNE/INPI |
| Le gérant est ARDIAN FRANCE (SIREN 403201882), employeur de Thodoroff | RNE/INPI |
| Le RA FRR 2018 (p. 86) cite « SLP FPS ARDIAN Fonds de fonds FRR CI France » | RA FRR 2018 |

**Verdict** : Le circuit « FRR (argent public retraites) → Ardian France → fonds géré par Thodoroff » est CONFIRMÉ par sources primaires. Le GAP est SATURÉ.

---

## GAP-P1-2 : Contacts Martel-CRE pendant son mandat RTE (2020-2023)

**STATUT : 🟡 RÉSOLU (partiel) — conflit structurel établi, contacts individuels non documentés en OSINT**

### Rappel du contexte

- Laurent Martel, conseiller fiscalité du Président (05/2017-07/2020), chef pôle économie Matignon (07-10/2020)
- HATVP 2020-183 (06/10/2020) : compatibilité avec réserves pour sa mobilité vers RTE
- CRE délibération 2020-266 (29/10/2020) : approuve sa nomination au directoire de RTE (pôle finances, achats, risques)
- Mandat RTE : 10/2020 → 08/2023 (départ vers Bercy comme DLF)
- TURPE (rémunération de RTE) : fixé par la CRE. TURPE 6 en vigueur sur la période 2021-2024.

### Ce qui est établi

| Fait | Source |
|---|---|
| **FCT-p1m-001** | Le TURPE est la source de rémunération de RTE, fixé par délibération de la CRE. Le TURPE 6 couvre la période 2021-2024, soit exactement le mandat de Martel (10/2020-08/2023). | CRE, code de l'énergie |
| **FCT-p1m-002** | La réserve HATVP 2020-183 couvrait les contacts avec le Premier ministre, son cabinet et les collaborateurs du Président. **La CRE n'était pas incluse dans la réserve.** | Résumé 2020-183 |
| **FCT-p1m-003** | Martel, en tant que membre du directoire de RTE (pôle finances), avait pour fonction la supervision des questions financières, ce qui inclut la relation avec le régulateur (CRE) sur les tarifs. | La Lettre, 06/11/2020 |
| **FCT-p1m-004** | Entre 2020 et 2023, la CRE a publié de multiples délibérations sur le TURPE 6 (délibérations annuelles d'évolution, cadrage). RTE, en tant que gestionnaire du réseau, est partie prenante du processus de consultation. | CRE, Légifrance |
| **FCT-p1m-005** | Les contacts individuels entre Martel et les membres de la CRE ne sont **pas documentés en source ouverte**. Les auditions de la CRE ne sont pas transcrites (pattern documenté : commission des affaires économiques). Les PV de réunions CRE-RTE ne sont pas publics. | Constat OSINT |
| **FCT-p1m-006** | Le circuit complet : Élysée (fiscalité énergie) → CRE (validation nomination) → RTE (TURPE, 3 ans) → Bercy (DLF, fiscalité) forme une **boucle** où le régulé (RTE) est dirigé par un ex-régulateur (Élysée fiscalité) validé par le régulateur actuel (CRE). La réserve HATVP ne couvrait pas la CRE. | Analyse forensique |

### Le trou de la réserve

Le point central : la HATVP a interdit à Martel tout contact avec le Premier ministre, son cabinet et l'Élysée — les institutions qu'il venait de quitter. Mais elle n'a **pas** interdit les contacts avec la CRE, le régulateur qui fixe les tarifs de RTE. Or :

1. Martel connaissait les rouages de l'État (Élysée fiscalité 3 ans, Matignon finances)
2. Il n'avait pas besoin de contacter l'Élysée directement — son réseau et sa connaissance du système suffisaient
3. La CRE, non couverte par la réserve, était l'interlocuteur naturel pour défendre les intérêts de RTE sur le TURPE

**La réserve était juridiquement correcte mais fonctionnellement incomplète : elle protégeait les anciens collègues mais pas le régulateur sectoriel.**

### Verdict

| Champ | Verdict |
|---|---|
| **Identification** | ✅ CONFIRMÉ — 2020-183 = Laurent Martel → RTE (source primaire : CRE 2020-266) |
| **Conflit structurel** | ✅ CONFIRMÉ — ex-Élysée fiscalité → régulateur → régulé → retour Bercy fiscalité |
| **Réserve incomplète** | ✅ CONFIRMÉ — couvre Élysée/Matignon, pas la CRE |
| **Contacts Martel-CRE individuels** | 🔴 OSINT NON ACCESSIBLE — PV CRE non publics, auditions non transcrites |
| **Inférence** | PROBABLE — un membre du directoire finances de RTE a nécessairement des interactions avec le régulateur qui fixe ses tarifs. L'absence de preuve n'est pas la preuve d'absence. |

---

## SYNTHÈSE

| GAP P1 | Statut |
|---|---|
| FRR → Ardian | ✅ CLÔTURÉ — déjà résolu 11/08, 10 FCT primaires |
| Martel-CRE contacts | 🟡 RÉSOLU (partiel) — conflit structurel confirmé, réserve incomplète établie, contacts individuels inaccessibles en OSINT |

---

*Résolution GAPs P1 — 6 FCT. Le cas Martel illustre le pattern central du run2-ENR : la HATVP contrôle la mobilité mais ses réserves sont incomplètes. La CRE (régulateur) n'est pas protégée contre l'influence de ses anciens pairs passés chez les régulés.*
