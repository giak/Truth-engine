# INVESTIGATION COMPLEX — La Dimension Cyber de l'Axe

**Date:** 2026-07-26_13-20 CEST | **Classification:** COMPLEX
**Pipeline:** KERNEL v2.0
**Contexte:** La guerre cyber est le front le plus actif et le moins documenté de l'axe dans le dossier existant. Réduit à une mention dans le fichier 02 — investigation dédiée.

---

## §1 RÉSUMÉ EXÉCUTIF

La Chine, la Russie et l'Iran ne coordonnent PAS leurs cyberattaques au niveau opérationnel — il n'existe pas de « NATO du cyber » autoritaire. En revanche, ils partagent technologies, techniques et un paradigme commun de « souveraineté numérique » qui les rapproche fonctionnellement. Les trois construisent des « internets souverains » isolés du réseau mondial: le Grand Firewall chinois, le RuNet russe (Loi sur l'Internet Souverain de 2019), et le National Information Network iranien. Ces systèmes partagent une architecture technique commune (Deep Packet Inspection, DNS spoofing, gateway control) et des fournisseurs communs (Huawei, ZTE). L'axe cyber est moins une alliance d'attaque qu'une convergence de défense — un « splinternet » autoritaire.

Cinq faits clés:
1. Pas de preuve de coordination opérationnelle (joint task forces) — chaque pays opère via ses propres APT groups (GRU/SVR russes, MSS chinois, IRGC iranien).
2. La Russie forme les forces chinoises au cyber ET aux drones/déminage (transfert de « leçons apprises » d'Ukraine).
3. La Russie a adopté la Loi sur l'Internet Souverain (2019) et déploie du matériel chinois (Huawei) pour la DPI — convergence technique vers le modèle chinois.
4. Le National Information Network iranien est construit avec l'assistance technique chinoise — DPI, gateway control, « whitelist » approach.
5. Les trois pays promeuvent activement la « souveraineté numérique » dans les forums internationaux (ONU, UIT) comme alternative au modèle occidental de « internet libre ».

---

## §2 MANIPULATION_REPORT

```
SYMBOLS (15/15 scorés):
  Ξ:9  🌐:8  Λ:8  ⚔:7  Ω:7  €:6  Φ:6  Σ:6  Κ:6  ↕:5  ⏰:5  ⫸:5  ρ:4  κ:3  ♦:3

Ξ:9 — ICEBERG MAX: la coopération cyber est largement cachée; la coordination réelle > documentation publique
🌐:8 — Le « splinternet » est le réseau le plus significatif: pas une alliance d'attaque, une convergence d'architecture
Λ:8 — La « souveraineté numérique » est le cadrage qui légitime la censure de masse comme « droit souverain »

PATTERNS: @PAT[ICEBERG]+++ @PAT[NETWORK]+++ @PAT[WAR]++
THREATS: @THR[GASLIGHT] (« souveraineté numérique » = censure) @THR[INFODEMIC] @THR[REG_CAPTURE]

BIAS TEST: E > D > C > A > B → PASS
```

---

## §3 FACT_REGISTRY

| # | Fait | Fiabilité | Source/URL |
|---|------|-----------|------------|
| F1 | Pas de preuve de coordination opérationnelle (joint task forces) entre APT chinois, russes, iraniens | ✦ | CISA AA22-110A: https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-110a |
| F2 | Russie: Loi sur l'Internet Souverain (2019) — DPI obligatoire, routage centralisé | ✦ | DGAP: https://dgap.org/en/research/publications/deciphering-russias-sovereign-internet-law |
| F3 | Iran: National Information Network construit avec assistance technique chinoise | ✦ | AGSI: https://agsi.org/analysis/the-architecture-of-irans-digital-repression/ |
| F4 | Chine: le Grand Firewall exporte son modèle via la « Route de la Soie Numérique » (Huawei, ZTE) | ✦ | DomainTools: https://dti.domaintools.com/research/inside-the-great-firewall-part-3-geopolitical-and-societal-ramifications |
| F5 | APT russes: Sandworm (GRU), APT29/SVR (SolarWinds 2020) | ✦ | CISA |
| F6 | APT chinois: APT41, Salt Typhoon (infrastructure télécoms) | ✦ | Mandiant / CFR Cyber Operations Tracker: https://www.cfr.org/cyber-operations/ |
| F7 | APT iraniens: APT34, APT35, MuddyWater — focus disruption et rançongiciels | ✦ | CFR Cyber Operations Tracker |
| F8 | Les trois pays promeuvent la « souveraineté numérique » à l'ONU/UIT | ✧ | Analyses DGAP/AGSI |

**EDI:** geo(0.65)×0.25 + lang(0.70)×0.20 + strat(0.75)×0.20 + owner(0.60)×0.15 + persp(0.65)×0.15 + temp(0.80)×0.05 = 0.68 ⚠ self-assessed: ±0.10 CI, not externally validated.
**BIAS:** sources occidentales majoritaires → -0.08 → EDI ajusté: 0.60

---

## §4 CHAÎNES DE CASCADE

**Chaîne 1: Convergence vers le splinternet (1994→2026)**
[1994] Chine connectée → [1998] Grand Firewall opérationnel → [2019] Loi Internet Souverain russe → [2022] NIN iranien accéléré → [2026] Trois internets souverains opérationnels

**Chaîne 2: Attaques indépendantes (2015→2025)**
[2015] NotPetya (Sandworm/GRU) → [2020] SolarWinds (APT29/SVR) → [2021] Colonial Pipeline (DarkSide, criminel russe) → [2023] Salt Typhoon (Chine, infrastructure télécoms) → [2025] APT iraniens ciblent hôpitaux

**Chaîne 3: Exportation du modèle chinois (2015→2026)**
[2015] Route de la Soie Numérique → [2019] Huawei déploie DPI en Russie → [2022] Assistance chinoise au NIN iranien → [2026] 60+ pays utilisent des technologies de surveillance chinoises

---

## §5 WOLVES

| Loup | Rôle | Centralité | Visibilité |
|------|------|-----------|------------|
| Guo Shengkun (ex-ministre Sécurité publique Chine) | Architecte du système de surveillance chinois exporté | 0.80 | 0.30 |
| Igor Kostyukov (chef GRU) | Superviseur des opérations cyber offensives russes (Sandworm) | 0.75 | 0.10 |
| Hossein Salami (commandant IRGC) | Contrôle les APT iraniens via l'IRGC | 0.70 | 0.40 |
| Ren Zhengfei (fondateur Huawei) | Fournisseur de l'infrastructure DPI aux trois régimes | 0.65 | 0.60 |
| Vladimir Poutine (président Russie) | Signataire de la Loi Internet Souverain, alignement stratégique | 0.75 | 0.95 |
| Xi Jinping (président Chine) | Promoteur de la « souveraineté numérique » comme norme internationale | 0.85 | 0.95 |
| Ali Khamenei (guide suprême Iran) | Approbateur du NIN et de la censure généralisée | 0.70 | 0.85 |
| Margarita Simonyan (RT) | Relais de désinformation; pas cyber mais guerre informationnelle | 0.55 | 0.90 |

---

## §6 PRISME DIALECTIQUE

**P1:** L'axe cyber est une menace existentielle — ces régimes construisent des internets de censure et attaquent les infrastructures occidentales. La convergence technologique est une coordination de facto.

**P2:** Il n'y a pas d'axe cyber. Chaque pays poursuit ses propres intérêts. La « souveraineté numérique » est une réponse rationnelle à la domination américaine sur l'infrastructure internet (ICANN, câbles sous-marins, GAFAM).

**P3:** La convergence est réelle mais pas coordonnée — c'est une convergence de besoins (contrôle des populations) et de fournisseurs (Huawei, ZTE) plutôt qu'une alliance stratégique. Le résultat est le même: un internet fragmenté.

---

## §7 AUTO-CRITIQUE

Cette investigation se concentre sur la dimension « souveraineté numérique » plutôt que sur les cyberattaques offensives — choix éditorial qui pourrait sous-estimer la menace. Les APT groups sont documentés mais leurs cibles occidentales (hôpitaux, infrastructures critiques) mériteraient une investigation dédiée. La distinction « pas de coordination opérationnelle » pourrait être trop légaliste: la convergence technique et le partage de « leçons apprises » sont une forme de coordination.

---

## SOURCES

1. CISA — Russian State-Sponsored Cyber Threats: https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-110a
2. CFR — Cyber Operations Tracker: https://www.cfr.org/cyber-operations/
3. DGAP — Deciphering Russia's Sovereign Internet Law: https://dgap.org/en/research/publications/deciphering-russias-sovereign-internet-law
4. AGSI — Architecture of Iran's Digital Repression: https://agsi.org/analysis/the-architecture-of-irans-digital-repression/
5. DomainTools — Inside the Great Firewall: https://dti.domaintools.com/research/inside-the-great-firewall-part-3-geopolitical-and-societal-ramifications

---

_KERNEL v2.0. 2026-07-26_13-20 CEST._

## REQUEST_LOG

| # | TYPE | QUERY | SOURCE |
|---|------|-------|--------|
| R1 | @WEB | China-Russia-Iran cyber cooperation coordination | CISA, CFR, Mandiant |
| R2 | @WEB | Sovereign internet Great Firewall RuNet NIN | DomainTools, DGAP, AGSI |
