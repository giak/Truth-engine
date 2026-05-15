# INVESTIGATION — Acheteurs des données volées : le marché invisible

**Date :** 21 avril 2026
**Complexité :** MEDIUM (political:1, technical:2, temporal:2, geo:2, narratives:2, data:2 = 11/18 → MEDIUM)
**Sujet :** Qui achète les 280 millions de données françaises volées et que font-ils ?

---

## MANIPULATION_REPORT

```
SYMBOLS: Ξ:8 €:6 Λ:3 Ω:4 Ψ:5 ↕:4 Φ:2 Σ:2 Κ:3 ρ:2 κ:4 ⫸:3 ⚔:5 🌐:3 ⏰:3
PATTERNS: @PAT[ICEBERG](Ξ:8), @PAT[MONEY](€:6), @PAT[WAR](⚔:5)
THREATS: @THR[SHOCK], @THR[BIDERMAN], @THR[DARK_MONEY]
RHETORICAL: DEM:1 BF:2 NUM:4 AUTH:2 FAC:1
CLUSTERS LOADED: ICEBERG(Ξ:8), MONEY(€:6), WAR(⚔:5)
IMPLICIT: Les acheteurs sont invisibles par conception ; le cycle de vie des données est structuré comme une chaîne de valeur criminelle
SPEAKER: {tone: forensique, target: marché clandestin, goal: documenter chaîne de valeur}
PRIORITIES: prix dark web ; groupes ransomware ; lien fuites→fraudes
```

---

## §0 RÉSUMÉ

Les 280 millions de données françaises exfiltrées depuis 2026 (ANTS : 19 M, France Travail : 30 M, santé : 35 M, FICOBA : 1,2 M, EduConnect : 3,5 M) alimentent une chaîne de valeur criminelle structurée : exfiltration → tri/enrichissement → revente → exploitation. Les prix sur le dark web varient de 0,20 € (carte bancaire basique) à 33 € (« fullz » complet pour usurpation d'identité) à 100 € (dossier médical ou carte de crédit avec solde). Les groupes ransomware (Cl0p, Qilin, LockBit) opèrent en Ransomware-as-a-Service avec double extorsion (chiffrement + menace de publication). Qilin a demandé jusqu'à 50 M$ de rançon. Le lien entre fuites étatiques et fraude d'identité est documenté : la centralisation des données augmente l'impact massif en cas de faille.

---

## §1 CHRONOLOGIE

| Date | Événement | Source |
|------|-----------|--------|
| 2024-2026 | Campagnes Cl0p (MOVEit), LockBit, Qilin sur cibles françaises | Europol IOCTA |
| 2025 | 40 % des Français victimes de cyber-malveillance | Crédoc/Franceinfo |
| 2025-2026 | France championne d'Europe des fuites de données | FrenchBreaches |
| 15 avril 2026 | Piratage ANTS : 18-19 M données en vente dark web | BFMTV |

---

## §2 DOMAINES

**Marché dark web** : Les données sont triées, enrichies et catégorisées avant revente. Un « fullz » (nom + prénom + date de naissance + adresse + téléphone) se vend ~33 €. Les données de santé et bancaires atteignent 100 € par enregistrement. Les données sont revendues plusieurs fois sous forme de kits.

**Groupes ransomware** : Cl0p (exploitation de vulnérabilités massives), LockBit (RaaS, centaines de victimes), Qilin (rançon jusqu'à 50 M$). Modèle : double extorsion (chiffrement + menace de publication). Alliances cartellaires : Qilin + LockBit + DragonForce.

**Cycle de vie des données** :
1. Exfiltration (phishing, vulnérabilités, erreurs humaines)
2. Tri, enrichissement, catégorisation
3. Mise en vente (forums darknet, canaux Telegram)
4. Revente multiple (kits, « fullz »)
5. Exploitation : fraude d'identité, phishing ciblé, extorsion, escroqueries

**Lien fuites → fraudes** : Les données étatiques centralisées (ANTS, France Travail, FICOBA) sont particulièrement prisées car elles contiennent des données d'identité complètes permettant l'usurpation. La centralisation augmente l'impact d'une seule faille.

---

## §3 CHAÎNES CAUSALES

**Chaîne 1 : Exfiltration → Revente → Usurpation**
1. Groupe ransomware exfiltre données (ex: ANTS 19 M)
2. Données triées et mises en vente sur dark web
3. Acheteurs exploitent pour usurpation d'identité, fraude bancaire, phishing ciblé
4. 40 % des Français victimes de cyber-malveillance (Crédoc 2025)

**Chaîne 2 : Centralisation → Risque systémique**
1. État centralise données dans des bases uniques (ANTS, France Travail, FICOBA)
2. Une seule faille expose des millions d'enregistrements complets
3. Les données d'identité étatiques sont les plus prisées (qualité, complétude)
4. Le marché clandestin s'auto-alimente : plus de données → plus de fraudes → plus de demande

---

## §4 PREUVES (FACT_REGISTRY)

| # | Fait | Date | Acteur | Source | URL | Fiabilité |
|---|------|------|--------|--------|-----|-----------|
| 1 ✧ | Prix dark web : fullz ~33 €, carte bancaire 0,20-10 €, dossier médical dès 5 € | 2025-2026 | Multiples | Ouest-France | https://www.ouest-france.fr/leditiondusoir/2023-05-10/vos-donnees-personnelles-piratees-valent-parfois-de-l-or-voici-leurs-prix-de-revente-sur-le-dark-web-e7d0478b-3149-4b9e-9bb5-90b84d483174 | ◉ |
| 2 ✧ | Cl0p, LockBit, Qilin : modèle RaaS, double extorsion, rançon moyenne ~324 000 € | 2025 | Europol | IOCTA | https://www.europol.europa.eu/publications-events/main-reports/iocta-report | ◈◉ |
| 3 ✧ | Qilin : rançon demandée jusqu'à 50 M$ | 2025 | CybelAngel | CybelAngel | https://cybelangel.com/fr/blog/qilin-ransomware-tactics-attack/ | ◉ |
| 4 ✧ | Alliances cartellaires : Qilin + LockBit + DragonForce | 2025 | SOS Ransomware | SOS Ransomware | https://sosransomware.com/groupes-de-ransomware/ | ◉ |
| 5 ✦ | 40 % des Français victimes de cyber-malveillance en 2025 | Fév 2026 | Crédoc | Franceinfo | https://www.franceinfo.fr/replay-radio/le-decryptage-eco/info-franceinfo-quatre-francais-sur-dix-ont-ete-victimes-de-cyber-malveillance-en-2025-selon-une-enquete-du-credoc_7787678.html | ◈◉ |
| 6 ✧ | Données ANTS (19 M) en vente sur dark web après piratage | Avr 2026 | ANTS | BFMTV/Numerama | https://www.numerama.com/cyberguerre/2236101-france-titres-ants-a-ete-pirate.html | ◉ |
| 7 ⁕ | Acheteurs spécifiques non identifiés publiquement (opacité structurelle du marché) | 2026 | Non vérifié | — | — | ○ |

---

## §5 LIMITES

1. **Acheteurs invisibles** : Les marchés du dark web sont opaques par conception. Les acheteurs spécifiques (États, réseaux criminels, concurrents) ne sont pas identifiables publiquement.
2. **Prix fluctuants** : Les prix du dark web varient selon la fraîcheur, la rareté et la demande. Les chiffres cités sont des estimations à un instant donné.
3. **Lien fuites→fraudes** : La corrélation est documentée mais la causalité directe (telle fuite → telle fraude) est rarement prouvable.
4. **Europol IOCTA** : Les rapports Europol agrègent des données à haut niveau. Les détails spécifiques sur les cibles françaises sont limités.

---

## REQUEST_LOG

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL |
|---|------|----------------|--------|--------|-----|
| 1 | @WEB | Dark web data prices France fullz medical bank prices | 33€ fullz, 0.20-10€ CB, 5€+ médical | Ouest-France | https://www.ouest-france.fr/ |
| 2 | @WEB | Europol IOCTA 2025 ransomware buyers stolen data | RaaS, double extorsion, professionalization | Europol | https://www.europol.europa.eu/publications-events/main-reports/iocta-report |
| 3 | @WEB | Qilin LockBit Cl0p ransomware RaaS revenue France | Qilin 50M$, alliance cartellaire | CybelAngel | https://cybelangel.com/fr/blog/qilin-ransomware-tactics-attack/ |

---

_KERNEL v2.0 — Investigation MEDIUM — 7 faits (1✦ 5✧ 1⁕) — 2 chaînes causales_
_Chaîne de valeur criminelle structurée : l'opacité du marché est la condition de sa pérennité_
