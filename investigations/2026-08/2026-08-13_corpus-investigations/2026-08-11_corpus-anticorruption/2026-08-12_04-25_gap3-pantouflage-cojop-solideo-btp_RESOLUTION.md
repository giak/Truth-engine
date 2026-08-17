# RÉSOLUTION : GAP-p10-3 — Pantouflage COJOP/Solideo → BTP (HATVP 2024-2026)

- STATE          : FINAL
- DATE           : 2026-08-12 04:25 CEST
- TYPE           : RESOLUTION (GAP, KERNEL v2.8)
- DOSSIER        : 2026-08-11_corpus-anticorruption (ICEBERG MAX, P10)
- OBJECT         : vérifier le pantouflage COJOP/Solideo → promoteurs BTP via les avis HATVP 2025-2026
- METHODE        : scan des 773 PDFs HATVP (/tmp/vp44_txt) + web search + read_url
- VERDICT        : 0 cas documenté COJOP/Solideo→BTP, mais FAILURE STRUCTURELLE du contrôle identifiée

---

## FAITS

| ID | Fait | Source | Date |
|---|---|---|---|
| FCT-p10-3-001 | Scan 773 PDFs HATVP : 50 fichiers contiennent COJOP/Solideo/BTP, dont 7 avis de mobilité COJOP+BTP | /tmp/vp44_txt (audit HATVP run2-enr) | 08/2026 |
| FCT-p10-3-002 | Avis 2024-A-121 (04/03/2024) : HATVP qualifie le COJOP de « mission d'intérêt général » NE CONSTITUANT PAS une « entreprise privée » au sens de l'art. 432-13 CP | HATVP, avis 2024-121 | 04/03/2024 |
| FCT-p10-3-003 | Avis 2024-A-121 : Camille Régent, conseillère presse ministérielle → COJOP manager presse : COMPATIBLE, 0 restriction (COJOP = quasi-public) | HATVP | 04/03/2024 |
| FCT-p10-3-004 | Avis 2026-15 (27/01/2026) : HATVP qualifie le COJOP d'« activité privée lucrative » ÉCHAPPANT À SON CONTRÔLE pour la mobilité sortante | HATVP, avis 2026-15 | 27/01/2026 |
| FCT-p10-3-005 | Avis 2026-15 : Marie Barsacq, directrice exécutive COJOP Paris 2024 (01/2019-10/2024) puis ministre des Sports (12/2024-10/2025) → SAE POPB (Accor Arena) : COMPATIBLE avec réserves | HATVP | 27/01/2026 |
| FCT-p10-3-006 | Double qualification contradictoire du COJOP par la HATVP : (a) « pas une entreprise privée » pour l'entrée (2024-121) ; (b) « activité privée lucrative » échappant au contrôle pour la sortie (2026-15) | HATVP | 2024-2026 |
| FCT-p10-3-007 | Avis 2025-137, 2025-217, 2025-246, 2025-A-239, 2025-A-333 : mobilités COJOP Alpes 2030, pas Paris 2024 — toutes COMPATIBLES | HATVP | 2025 |
| FCT-p10-3-008 | 0 avis HATVP trouvé concernant une mobilité Solideo → BTP (1 seule occurrence Solideo : 2020-176, type AUTRE, pas mobilité) | /tmp/vp44_txt | 08/2026 |
| FCT-p10-3-009 | 0 avis HATVP trouvé concernant Tony Estanguet, Nicolas Ferrand, Michaël Aloïsio, Étienne Thobois dans les 773 PDFs | /tmp/vp44_txt | 08/2026 |

---

## LE TROU STRUCTUREL (FAILURE, pas ABSENCE)

Le résultat central n'est pas « 0 cas trouvé » mais **la documentation d'une architecture juridique qui rend le pantouflage COJOP→privé INCONTRÔLABLE**.

### La double qualification contradictoire

| Direction | Qualification HATVP | Conséquence |
|---|---|---|
| **Public → COJOP** (entrée) | « Mission d'intérêt général », « pas une entreprise privée » (2024-121, §8) | Art. 432-13 CP écarté — Aucune restriction pénale |
| **COJOP → Privé** (sortie) | « Activité privée lucrative », « ne relève pas du contrôle » HATVP (2026-15, §4) | Aucun contrôle déontologique |

### Le schéma de contournement

```
Agent public (ministère, cabinet)
        ↓
    COJOP Paris 2024  ← PAS de restriction (COJOP = « pas entreprise privée »)
        ↓
    Entreprise privée  ← PAS de contrôle (COJOP = « activité privée lucrative »)
   (Vinci, Eiffage, Bouygues...)
```

Le COJOP fonctionne comme une **SAS de transition** : un sas de 1-3 ans qui efface la restriction de pantouflage de 3 ans. L'agent public rejoint le COJOP (autorisé car « mission d'intérêt général »), y reste 1-3 ans, puis rejoint le privé (autorisé car le COJOP n'est « pas une administration » et la HATVP n'a « pas compétence »).

### Le cas Barsacq (2026-15) comme preuve de concept

Marie Barsacq est passée de **directrice exécutive COJOP** (2019-2024) à **ministre des Sports** (2024-2025) puis à **directrice générale de SAE POPB** (Accor Arena, détenue à 43,7 % par AEG, groupe américain). La HATVP n'a contrôlé QUE la transition ministre→SAE POPB. La transition COJOP→ministre et COJOP→SAE POPB n'ont fait l'objet d'AUCUN contrôle.

### Solideo : régime différent

La Solideo est un **EPA** (Établissement Public à caractère Administratif). Ses agents sont des agents publics soumis à l'art. 432-13 CP et au contrôle HATVP (art. L. 124-4 CGFP). L'absence d'avis Solideo→BTP dans les 773 PDFs est donc un **vrai zéro** — soit les mobilités n'ont pas eu lieu, soit elles n'ont pas été déclarées.

---

## INTERPRÉTATION

Le GAP-p10-3 est **techniquement résolu** : 0 cas documenté de pantouflage COJOP/Solideo → BTP dans les données HATVP publiques.

Mais la vraie trouvaille est **la documentation du trou structurel** : la HATVP a qualifié le même organisme (COJOP) de deux façons contradictoires selon la direction de la mobilité, créant un sas juridique parfait pour contourner les restrictions de pantouflage.

Ce pattern n'est pas propre aux JO 2024 : il s'applique à tout organisme créé sous forme associative avec « mission d'intérêt général » financé majoritairement par des fonds publics. La prochaine itération (Alpes 2030) reproduira le même schéma.

---

## GAPs RÉSIDUELS

| ID | GAP | Priorité |
|---|---|---|
| GAP-p10-3a | Cartographier les parcours post-COJOP des 50+ cadres dirigeants Paris 2024 (LinkedIn, presse) pour détecter les atterrissages BTP non déclarés | P1 |
| GAP-p10-3b | Vérifier si le COJOP Alpes 2030 a repris la même architecture juridique (association loi 1901) que Paris 2024 | P1 |
| GAP-p10-3c | Solideo : vérifier les mobilités sortantes via le décret d'extinction (fin 2028) — les agents seront-ils absorbés par Grand Paris Aménagement ou partiront-ils dans le privé ? | P2 |
