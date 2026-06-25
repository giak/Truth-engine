# SUCCESSION DU LEADER ARRETE — Protocoles concrets

**Solutions Investigation · KERNEL v2.0 Protocol**

**Date** : 2026-06-10  |  **Type** : `SOLUTIONS`  |  **Complexité** : COMPLEX  |  **Statut** : COMPLETE

---

## 1. Problème

L'APEX §6 du projet Truth Engine identifie la succession du leadership comme un « verrou central non résolu » et propose 5 modèles abstraits (conseil de porte-parole, dead man's switch, chaîne cut-out, vote algorithmique, leadership émergent). Aucun n'est détaillé.

Ce que nous savons :
- La coordination est le goulet d'étranglement central (KERNEL v2.0)
- L'arrestation du leader crée un vide informationnel et décisionnel immédiat
- Les organisations clandestines historiques ont développé des solutions (IRA, Solidarnosc, Zapatistes)
- La technologie blockchain fournit des outils de succession programmables (DAO, multisig, dead man's switch)

Ce que nous ne savons pas :
- Aucun protocole complet n'existe dans la littérature académique pour les organisations civiles non-violentes
- La plupart des solutions documentées concernent des organisations militaires ou criminelles
- Les solutions techniques (dead man's switch) n'ont jamais été testées en contexte répressif réel
- Le droit français (art.450-1 CP, art.421-1 CP) criminalise la « participation à un groupe de combat » et l'« association de malfaiteurs » — un protocole écrit de succession pourrait constituer une preuve matérielle

---

## 2. Dead Man's Switch — protocoles techniques

### 2.1 Still Alive Bot (Telegram)

**Dépôt:** `github.com/tobyxdd/stillalive-bot`
**Langage:** Python 3.12+
**Fonctionnement:** Bot Telegram. L'utilisateur enregistre des « watchers » via `/invite`. Un check-in quotidien via `/checkin`. Si l'échéance est dépassée, les watchers reçoivent un message d'alerte personnalisé.

**Fonctionnalités clés:**
- Intervalle configurable (12/24/48/72h)
- Délai avant alerte configurable (24-96h)
- PIN optionnel à 4 chiffres pour le check-in (ne circule pas dans l'historique chat)
- Duress PIN : un second code qui « valide » le check-in en apparence mais ne repousse pas la vraie deadline
- Base SQLite, déploiement Docker
- Source: `github.com/tobyxdd/stillalive-bot`

**Utilité pour la succession:** Chaque membre de la direction enregistre un watcher désigné comme successeur. Si le leader ne fait pas son check-in dans X heures, le successeur est notifié et active le plan B.

**Risque juridique France:** L'hébergement du bot (même sur un VPS à l'étranger) + le trafic Telegram sont traçables. Art.450-1 CP: « association de malfaiteurs » si le bot sert à préparer un « acte de résistance collective ». Risque modéré.

### 2.2 Dead Man Switch Telegram (Codeberg)

**Dépôt:** `codeberg.org/vkomanchy/dead-man-switch-telegram`
**Langage:** TypeScript (Telegraf)
**Fonctionnement:** Similaire mais plus sophistiqué. Supporte 8 types d'actions :
- `userMessage` / `groupMessage` — envoi d'un message à une cible
- `multiUserMessage` — notification multiple
- `webhook` — déclenchement d'un webhook
- `sendLocation` — envoi de géolocalisation
- `sendDocument` — envoi de document
- `forwardMessages` — forwarding de messages
- `escalationChain` — chaîne d'escalade (A prévient B, si B ne répond pas, C est prévenu)

**Fonctionnalité critique:** `escalationChain` permet de créer une chaîne de succession automatique. Si le leader ne répond pas dans la fenêtre, le message passe au suivant dans la hiérarchie. Base de données Prisma, support des scènes (wizards) pour la configuration.

**Utilité pour la succession:** La chaîne d'escalade est le mécanisme le plus proche d'un protocole de succession automatisé jamais codé.

**Risque:** Le code est public et identifiable. Utilisation via Tor/brideur recommandée.

### 2.3 Dead Man Switch (Rust)

**Dépôt:** `github.com/BlackSnufkin/DeadManSwitch`
**Langage:** Rust
**Fonctionnement:** Application desktop cross-platform (Windows, Linux, macOS). Combine 5 triggers :
1. Heartbeat timer (Telegram) — check-in via `/alive`
2. Telegram bot — déclenchement manuel via `/dms execute`
3. UDP broadcast — déclenchement réseau local
4. USB detection — déclenchement matériel (clé USB spécifique)
5. Flic button — bouton physique Bluetooth

**Action:** Démontage de volumes VeraCrypt + extinction système.

**Utilité pour la succession:** Le trigger réseau (UDP broadcast) permet de déclencher la procédure depuis n'importe quelle machine sur le LAN. Utile si un membre est arrêté et qu'un autre veut activer le protocole sans avoir accès au compte Telegram.

### 2.4 Posthumous (fédéré, TOTP)

**Dépôt:** `github.com/queelius/posthumous`
**Langage:** Python (asyncio)
**Fonctionnement:** Serveur auto-hébergé. Check-in via TOTP (Google Authenticator). 4 états : ARMED → WARNING → GRACE → TRIGGERED. Fédéré : plusieurs nœuds partagent le même secret et se surveillent mutuellement.

**Points forts:**
- Pas de dépendance à un service centralisé (auto-hébergé)
- Fédération : un nœud peut tomber, les autres prennent le relais
- Notifications via Apprise (100+ services : ntfy, Pushover, Telegram, email)
- Planification post-déclenchement (scripts automatisés, rappels periodiques)
- Chiffrement au repos (Fernet AES-128-CBC)

**Utilité pour la succession:** Le plus robuste. Configurer un nœud sur un serveur chez un ami, un second sur un VPS, un troisième sur un Raspberry Pi. Si un seul survit, le protocole se déclenche.

### 2.5 Sarcophagus (Ethereum + Arweave)

**Site:** `sarcophagus.io`
**Fonctionnement:** Dead man's switch décentralisé sur Ethereum, stockage permanent sur Arweave. L'utilisateur (Embalmer) uploade un fichier chiffré, fixe une date de « résurrection ». Des nœuds (Archaeologists) surveillent. Si l'utilisateur ne prolonge pas le délai, les nœuds déchiffrent et le destinataire (Recipient) récupère le fichier.

**Économie:** Token SARCO, 3 tours de financement ($10.9M). DAO sur Aragon avec 4 subDAOs.

**Utilité pour la succession:** Distribution d'instructions, clés, documents. Le délai peut être fixé à 48h après l'arrestation. Pas de risque de « faux positif » car le mécanisme exige l'inaction prolongée.

**Limitation:** Nécessite ETH pour le gaz. La transaction de prolongation doit être signée depuis un wallet non compromis. L'utilisation d'Arweave rend le contenu permanent (même après déchiffrement, le fichier chiffré reste stocké).

### 2.6 Git-based Dead Man's Switch (lp1)

**Article:** `medium.com/@lp1/git-based-modern-dead-mans-switch-e37fc597e655`
**Fonctionnement:** Un dépôt Git public fait office de « heartbeat ». Un script cron vérifie la date du dernier commit. Si > 211 jours sans commit, un email avec les credentials chiffrés est envoyé via Mailgun. Un bot Telegram répond à la commande `/allgood` pour repousser l'échéance.

**Utilité pour la succession:** Simple, reproductible, utilise une infrastructure publique (GitHub). Mais inadapté aux délais courts (heures/jours).

---

## 3. Mécanismes historiques de succession

### 3.1 IRA : Army Council et co-option

**Source:** CAIN « Green Book » — `cain.ulster.ac.uk/othelem/organ/ira/ira_green_book.htm`
**Mécanisme:** L'IRA était structurée comme une armée avec un Army Council de 7 membres. Le serment du volontaire: « je promets d'obéir aux ordres de l'Army Council et de tous mes officiers supérieurs ». La succession se faisait par **co-option** : si un membre du Army Council était arrêté, les membres restants en co-optaient un nouveau.

**Détails opérationnels:**
- Le Army Council détenait l'autorité exécutive, déléguée par les députés du Dáil de 1918
- Les volunteers devaient obéir aux ordres d'un supérieur même s'ils ne l'aimaient pas
- La sécurité reposait sur le compartimentage : un volontaire ne connaissait que les membres de sa cellule
- Le « Green Book » (manuel de formation) insistait sur l'anti-interrogatoire : « SAY NOTHING » pendant 7 jours

**Limitation:** La co-option est non-démocratique, crée des risques de factionnalisme, et dépend de la capacité des membres restants à se coordonner après l'arrestation.

### 3.2 Solidarnosc : TKK (Tymczasowa Komisja Koordynacyjna)

**Source:** `newworldencyclopedia.org/entry/Solidarity_(History_of)`
**Mécanisme:** Après l'instauration de la loi martiale le 13 décembre 1981, la direction de Solidarnosc (Lech Wałęsa, arrêté) fut remplacée par une **Commission Coordinatrice Temporaire (TKK)** composée de 3 leaders régionaux :
- Zbigniew Bujak (région de Mazowsze)
- Bogdan Lis (Gdańsk)
- Władysław Frasyniuk (Wrocław)

**Détails opérationnels:**
- La TKK fonctionnait comme un directoire clandestin, communiquant via des imprimeries souterraines
- Chaque leader régional gérait son secteur en autonomie, avec un coordinateur central
- Les décisions majeures (grèves nationales) étaient prises par consensus des 3
- Des « structures parallèles » (Radio Solidarność, publications clandestines) maintenaient la continuité

**Leçon:** La décentralisation régionale avec coordination minimale permet la survie de l'organisation même si toute la direction centrale est arrêtée. Chaque région a son plan de continuité.

### 3.3 Zapatistes : Juntas del Buen Gobierno et rotation

**Source:** `iaf-fai.org/2020/04/19/zapatista-governance-leadership-community-and-decision-making-principles.html`
**Mécanisme:** Les communautés zapatistes sont gouvernées par des **Juntas del Buen Gobierno** (Conseils du Bon Gouvernement), composées de membres tournants de la communauté. Principes : Mandar Obedeciendo (commander en obéissant), Proponer y No Imponer (proposer sans imposer), Representar y No Suplantar (représenter sans supplanter).

**Détails opérationnels:**
- Les membres des Juntas servent pour une période déterminée, puis sont remplacés
- La rotation empêche l'accumulation de pouvoir
- Les décisions sont prises par consensus dans des assemblées publiques (consultas)
- Un comité de surveillance (oversight committee) contrôle les abus de pouvoir
- Publication transparente des comptes

**Leçon:** La rotation programmée élimine le problème de la succession — il n'y a pas de leader unique à remplacer. Mais ce modèle exige une culture politique avancée et un temps de décision long.

### 3.4 Black Panther Party : direction fragmentée

**Source:** `britannica.com/topic/Black-Panther-Party`
**Mécanisme:** Le BPP avait une structure centralisée (Huey Newton, Bobby Seale) mais des chapitres locaux très autonomes. L'arrestation de Newton en 1967-1970 a fragmenté la direction. Elaine Brown a pris la direction en 1974 quand Newton s'est exilé, mais la succession a été conflictuelle.

**Leçon:** L'absence de protocole de succession explicite a conduit à des luttes internes. Le BPP illustre l'échec par défaut.

---

## 4. Approches blockchain / DAO

### 4.1 Multisig Gnosis Safe + timelock

**Source:** `docs.safe.global`, `markaicode.com/dao-recovery-safe-wallet-multisig/`
**Mécanisme:** Un wallet multisig (M-of-N signatures) contrôle les actifs et les décisions. Un timelock (ex: 24-72h) retarde l'exécution. En mode normal, les décisions passent par un vote. En urgence, un conseil de sécurité (security council) peut bypasser le vote via le multisig.

**Configuration type:**
- Seuil: 4-of-7 signeurs
- Timelock: 48h pour les actions standards, 24h pour les urgences
- Guardian: un multisig séparé avec pouvoir de pause uniquement
- Sunet clause: les pouvoirs d'urgence expirent après 30 jours

**Application à la succession:** Le wallet multisig peut contenir : les clés de communication, les accès aux serveurs, le droit de signer des messages au nom du collectif. Si un signeur est arrêté, les autres continuent. Si X signeurs sur Y sont arrêtés, le seuil minimum est réévalué.

### 4.2 Compound Governor Bravo — double piste

**Source:** `chainscorelabs.com/guides/.../dao-governance-model-design`
**Mécanisme:** Le Governor Bravo (Compound) sépare les propositions en deux types :
1. **Standard:** vote + timelock (3-7 jours)
2. **Urgence:** voté par un Guardian, pas de timelock, période de vote courte (1 jour)

Code Solidity (extrait):
```solidity
function votingPeriod(uint256 proposalId) public view override returns (uint256) {
    if (_isEmergencyProposal(proposalId)) {
        return 1 days;
    }
    return 3 days;
}
```

**Application:** Le collectif peut avoir un conseil d'urgence (ex: 3 personnes) qui peut prendre des décisions rapides (ex: changer le canal de communication, activer le plan B). Ces décisions sont ensuite ratifiées par le vote de l'ensemble.

### 4.3 Pause Guardian

**Source:** `chainscorelabs.com/guides/.../dao-governance-model-design`
**Mécanisme:** Un contrat Pause Guardian permet à une adresse designée de mettre en pause des fonctions critiques (retraits, nouvelles inscriptions, changements de paramètres). Le Guardian ne peut PAS modifier le contrat, uniquement le mettre en pause.

```solidity
contract PauseGuardian {
    mapping(string => bool) public paused;
    function pause(string calldata module) external onlyGuardian { ... }
    function unpause(string calldata module) external onlyGuardian { ... }
}
```

**Application:** En cas d'arrestation, le Guardian (ou son remplaçant via la chaîne de succession) peut geler les opérations du collectif pour éviter des décisions irréfléchies, puis activer le protocole de relève.

---

## 5. Protocoles de vérification sans hiérarchie

### 5.1 Problème : comment vérifier qu'un ordre est authentique sans chaîne de commandement ?

La question centrale : si le leader est arrêté, un message prétendument de sa part annonce l'activation du plan B. Comment savoir si c'est authentique ?

### 5.2 Solution TOTP + partage de secret

**Source:** `metafunctor.com/post/2026-02-14-posthumous/`
**Principe:** Un secret partagé (TOTP seed) est connu de N membres. Chaque ordre est accompagné d'un code TOTP valide à l'instant T. Le destinataire vérifie le code.

**Avantage:** Pas de hiérarchie nécessaire. N'importe quel membre peut vérifier. Le code change toutes les 30 secondes.

**Limitation:** Le secret doit être distribué à l'avance. Si un membre est arrêté et que son téléphone est compromis, l'attaquant peut aussi signer des ordres.

### 5.3 Solution seuil (Shamir Secret Sharing)

**Principe:** Le secret (ex: clé PGP, seed TOTP, phrase de succession) est divisé en N parts via le schéma de Shamir. M parts sont nécessaires pour reconstituer le secret. Chaque membre de la direction détient une part.

**Application:**
- N = 7 membres du conseil
- M = 3 parts nécessaires pour reconstituer la clé
- Pour signer un ordre de succession, 3 membres doivent combiner leurs parts
- Résistant à la compromission de 4 membres sur 7

**Limitation:** Nécessite une coordination hors-ligne pour la distribution initiale. La recomposition exige que 3 membres soient joignables simultanément.

### 5.4 Solution cut-out avec preuve différée

**Principe:** Le leader pré-enregistre un message (chiffré, horodaté) qui est publié automatiquement par un dead man's switch (Sarcophagus, Posthumous). Le message contient une moitié de clé. La seconde moitié est détenue par un avocat ou un notaire. Le successeur ne peut agir qu'avec les deux moitiés.

**Chaîne:**
1. Le dead man's switch publie la première moitié de clé
2. Le successeur contacte le notaire (via un mécanisme légal, ex: mandat d'inaptitude)
3. Le notaire publie la seconde moitié
4. Le successeur assemble la clé et signe les ordres

**Avantage:** Aucun membre du collectif ne détient le secret complet. La vérification est décentralisée.

---

## 6. Mécanismes de bascule vitesse-démocratie

### 6.1 Le problème central

En temps normal, le collectif prend des décisions par consensus lent (jours/semaines). En urgence (arrestation), il faut des décisions en minutes/heures. Comment basculer entre les deux régimes ?

### 6.2 Holacracy : Individual Initiative (Article 4.3)

**Source:** `holacracy.org/constitution/5-0/` — Article 4.3 « Individual Initiative »
**Mécanisme:** La Constitution Holacracy prévoit explicitement qu'un membre peut outrepasser les règles normales si :
1. Il agit de bonne foi pour servir le Purpose de l'organisation
2. L'action prévient plus de tensions qu'elle n'en crée
3. Elle n'engage pas de dépenses non autorisées
4. Attendre la permission causerait une perte de valeur significative

**Obligations post-action:**
- Expliquer l'action à tous les impactés
- Prioriser la communication et la restoration
- Accepter de ne pas répéter l'action si un Role Lead le demande

**Application à la succession:** Le protocole de succession peut être activé par n'importe quel membre via Individual Initiative. Il n'a pas besoin d'autorisation préalable — mais il doit expliquer son action dans les X heures.

### 6.3 DAO Dual-Track (Compound Governor Bravo)

**Source:** `chainscorelabs.com/guides/.../dao-governance-model-design`
**Mécanisme:** Deux vitesses de décision codées dans le contrat :
- **Track normal:** vote sur 3 jours, quorum 4%, timelock 48h
- **Track urgence:** vote sur 1 jour, quorum 66%, pas de timelock

**Le quorum plus élevé compense la rapidité :** pour passer une décision rapide, il faut une super-majorité. Empêche les abus.

### 6.4 IRA : séparation militaire/politique

**Source:** CAIN Green Book
**Mécanisme:** L'IRA séparait strictement la fonction militaire (Army Council, opérations) de la fonction politique (Sinn Fein). En cas d'arrestation de la direction militaire, la branche politique assurait la continuité et vice versa.

**Application:** Le collectif maintient deux structures parallèles indépendantes. Si la structure A est décapitée, la structure B active le plan de continuité. Les membres de A ne connaissent pas les membres de B.

### 6.5 Modèle TKK (Solidarnosc)

**Source:** `newworldencyclopedia.org/entry/Solidarity_(History_of)`
**Mécanisme:** La TKK fonctionnait avec 3 membres égaux. Chaque membre avait l'autorité de prendre des décisions pour sa région sans consensus préalable. Les décisions nationales nécessitaient l'accord d'au moins 2 des 3.

**Application moderne:** Un conseil de 3-5 personnes. En mode normal, décisions par consensus. En urgence, tout membre peut décider seul (avec obligation d'information aux autres dans les 24h). Les décisions les plus graves (ex: abandon d'une campagne) nécessitent 2 signatures.

---

## 7. Tableau comparatif des 5 approches

| Approche | Protection | Complexité | Risque légal (FR) | Testé ? | Délai d'activation | Coût |
|----------|-----------|------------|-------------------|---------|-------------------|------|
| Dead Man's Switch (Telegram) | Moyenne — dépend de Telegram + VPS | Faible (existant, déploiement 1h) | Modéré (art.450-1 si association illicite) | Oui — StillAliveBot, DMS Telegram | Minutes/heures selon intervalle | ~5€/mois VPS |
| Dead Man's Switch (Blockchain, Sarcophagus) | Haute — décentralisé, permanent | Haute (wallet ETH, gas, Arweave) | Faible — aucune interaction humaine | Oui — Sarcophagus v2 (mainnet 2023) | Heures/jours | $50-200 en ETH + SARCO |
| Multisig DAO (Gnosis Safe) | Très haute — M-of-N, timelock | Moyenne (connaissances Solidity) | Faible — structure légale possible | Oui — utilisé par Compound, Uniswap, Aave | Heures (selon seuil de signatures) | $200-500 déploiement |
| Succession historique (IRA/TKK) | Haute — compartimentage + autonomie régionale | Haute (formation, discipline, culture) | Très élevé — art.421-1 CP « association terroriste » | Oui — IRA (1919-2005), Solidarnosc (1981-89) | Continue (structure parallèle) | Organisationnel |
| Modèle Zapatiste (rotation) | Haute — pas de leader unique | Haute (culture politique avancée) | Faible — pas de structure illégale | Oui — Zapatistes (1994-présent) | Permanent | Organisationnel + temps |

---

## 8. Fact Registry (faits atomiques)

| F | Fait | Source | Fiabilité |
|---|------|--------|-----------|
| F001 | Still Alive Bot implémente un dead man's switch Telegram avec check-in, watchers, duress PIN | `github.com/tobyxdd/stillalive-bot` | ✦ |
| F002 | Le bot Telegram dead-man-switch (Codeberg) supporte 8 types d'actions dont escalationChain | `codeberg.org/vkomanchy/dead-man-switch-telegram` | ✦ |
| F003 | DeadManSwitch en Rust combine 5 triggers (heartbeat, Telegram, UDP broadcast, USB, Flic) | `github.com/BlackSnufkin/DeadManSwitch` | ✦ |
| F004 | Posthumous est un dead man's switch fédéré auto-hébergé avec TOTP et 4 états (ARMED → TRIGGERED) | `metafunctor.com/post/2026-02-14-posthumous/` | ✦ |
| F005 | Sarcophagus est un dead man's switch décentralisé sur Ethereum/Arweave, DAO sur Aragon, 3 tours de financement ($10.9M) | `medium.com/@perma_dao/in-depth-analysis-of-sarcophagus` | ✧ |
| F006 | L'IRA utilisait un Army Council de 7 membres avec succession par co-option, documenté dans le Green Book | `cain.ulster.ac.uk/othelem/organ/ira/ira_green_book.htm` | ✦ |
| F007 | Solidarnosc underground (1981-89) utilisait la TKK (3 membres régionaux) avec autonomie locale et coordination minimale | `newworldencyclopedia.org/entry/Solidarity_(History_of)` | ✧ |
| F008 | Les Zapatistes utilisent des Juntas del Buen Gobierno tournantes, principes Mandar Obedeciendo + rotation obligatoire | `iaf-fai.org/2020/04/19/zapatista-governance-leadership-community-and-decision-making-principles.html` | ✧ |
| F009 | Gnosis Safe (Safe) est le standard de facto pour les multisig DAO, avec timelock, modules d'urgence, et recovery | `docs.safe.global` | ✦ |
| F010 | Compound Governor Bravo implémente un double-track (standard + urgence) avec Guardian et quorum différencié | `chainscorelabs.com/guides/.../dao-governance-model-design` | ✧ |
| F011 | La Constitution Holacracy v5.0 Article 4.3 autorise l'Individual Initiative : outrepasser les règles en cas d'urgence | `holacracy.org/constitution/5-0/` | ✦ |
| F012 | Le schéma de partage de secret de Shamir (M-of-N) permet de diviser la clé de succession entre N membres | Théorie cryptographique standard | ✦ |
| F013 | Le dead man's switch Git-based (lp1) utilise GitHub + Telegram + cron, avec intervalle de 211 jours | `medium.com/@lp1/git-based-modern-dead-mans-switch-e37fc597e655` | ✧ |
| F014 | L'Activist Checklist fournit un cadre complet de planification d'urgence personnelle (go-bag, safe person, pod mapping) | `activistchecklist.org/emergency/` | ✧ |
| F015 | Le Pause Guardian pattern permet de geler les opérations en urgence sans pouvoir de modification du contrat | `chainscorelabs.com/guides/.../dao-governance-model-design` | ✧ |

**Légende:** ✦ = tier 1 + URL OK, ✧ = tier 2 + URL OK, ⁅ = URL 4xx/5xx, ❧ = pas d'URL

---

## 9. ANNEXE — Toutes les URLs trouvées

### Dead Man's Switch — implémentations
1. `github.com/tobyxdd/stillalive-bot` — Still Alive Bot (Telegram, Python)
2. `codeberg.org/vkomanchy/dead-man-switch-telegram` — Dead Man Switch Telegram (TypeScript, escalationChain)
3. `github.com/BlackSnufkin/DeadManSwitch` — Dead Man Switch (Rust, 5 triggers)
4. `github.com/queelius/posthumous` — Posthumous (fédéré, TOTP, auto-hébergé)
5. `github.com/lp1dev/presence-checker` — Git-based DMS (commits Git + cron)
6. `medium.com/@perma_dao/in-depth-analysis-of-sarcophagus` — Sarcophagus (Ethereum + Arweave)
7. `medium.com/@lp1/git-based-modern-dead-mans-switch-e37fc597e655` — Article Git-based DMS
8. `sarcophagus.io` — Site officiel Sarcophagus
9. `github.com/BlackSnufkin/Rusty-Playground` — USB monitor helper pour DeadManSwitch

### DAO / Blockchain / Smart Contracts
10. `docs.safe.global` — Safe (Gnosis Safe) documentation officielle
11. `markaicode.com/dao-recovery-safe-wallet-multisig/` — DAO Recovery Safe Wallet guide
12. `chainscorelabs.com/guides/.../dao-governance-model-design` — DAO Governance + Emergency Powers
13. `docs.openzeppelin.com/contracts/5.x/governance` — OpenZeppelin Governor framework
14. `chainscorelabs.com/comparisons/.../timelock-only-emergency-override-vs-multisig-only-emergency-override` — Timelock vs Multisig comparison
15. `github.com/rukine/dao-multisig-wallet` — DAO multisig wallet with role-based permissions

### Histoire / Organisations
16. `cain.ulster.ac.uk/othelem/organ/ira/ira_green_book.htm` — IRA Green Book (structure + anti-interrogation)
17. `newworldencyclopedia.org/entry/Solidarity_(History_of)` — Solidarnosc underground history
18. `iaf-fai.org/2020/04/19/zapatista-governance-leadership-community-and-decision-making-principles.html` — Zapatista governance principles
19. `britannica.com/topic/Black-Panther-Party` — Black Panther Party history

### Théorie organisationnelle
20. `holacracy.org/constitution/5-0/` — Holacracy Constitution v5.0
21. `intechopen.com/chapters/1203461` — Holacracy and Crisis Management (academic, 2025)
22. `activistchecklist.org/emergency/` — Personal Emergency Planning for activists

### Cryptographie / Vérification
23. `metafunctor.com/post/2026-02-14-posthumous/` — Posthumous (TOTP, fédération, HMAC)
24. `scholarworks.calstate.edu/concern/theses/f4752j86c` — Rotating Leadership Zapatista (academic)

---

## §10 LIMITES — Ce que les protocoles ne resoudront pas

*Nota : cette section a ete redigee apres P9-EMPIRIQUE. Le biais identifie est le meme — les outils n'ont jamais ete testes en contexte reel.*

1. **Aucun test en contexte repressif** : les outils (Still Alive Bot, Dead Man Switch, DAO) n'ont jamais ete testes sous pression reelle (garde a vue, perquisition, torture psychologique).
2. **Dependance technique** : Telegram peut etre bloque (Russie 2022, Iran 2023). Les DAO Ethereum sont tracables. L'infrastructure technique est un point de defaillance.
3. **Complexite** : la plupart des militants n'ont pas les competences pour deployer et maintenir ces outils.
4. **Preuve penale** : un protocole de succession ecrit (ce fichier) peut constituer une preuve d'association de malfaiteurs (art.450-1 CP).

---

## §11 FAISCEAUX — Connexions P1-P9

| Faisceau | SUCCESSION | Investigation |
|----------|------------|---------------|
| LEADERSHIP + SUCCESSION | La succession est le probleme №1 du leadership acephale | P12-LEADERSHIP : les 5 modeles de succession concretises ici |
| EMPIRIQUE + SUCCESSION | Les protocoles doivent etre testes | P9-EMPIRIQUE : test des dead man's switch en simulation |
| RISQUE + SUCCESSION | Un protocole ecrit = preuve penale | P10-RISQUE : art.450-1, precaution juridique |
| CAS + SUCCESSION | Le sanctuaire permet la succession | P8-CAS : un leader en exil peut etre remplace |
| PSYCHO + SUCCESSION | La succession automatisee reduit le stress psychologique | P7-PSYCHO : savoir que le mouvement survive au leader |
| MODELE + SUCCESSION | La rotation zapatiste JBG est un modele de succession eprouve | PX-NON-ESCALADE : l'autonomie communautaire integre la rotation |
| PUITS + SUCCESSION | Les statuts juridiques (asso, SCIC) peuvent encoder la succession | PX-PUITS-DROIT : le cadre legal comme garant de la continuite |
| FINANCEMENT INVISIBLE + SUCCESSION | Un dead man's switch DAO peut transferer les fonds | PX-FINANCEMENT-INVISIBLE : la succession financiere automatisee |
| DROIT COMPARE + SUCCESSION | Les protocoles de succession sont moins risques au Benelux | PX-DROIT-COMPARE : succession en territoire protecteur |
| ACE + SUCCESSION | La succession est le probleme №1 de l'action acephale | ACE-INVESTIGATION : comment remplacer un leader sans leader |
| OLI + SUCCESSION | La succession automatisee contourne le verrou №6 d'OLI (capture leadership) | OLI-INVESTIGATION : le leadership capturable est un mecanisme OLI |

---

## §12 SUSPICION_SCORE — Auto-critique des protocoles de succession

**Score composite : 5.0/10**

| Critère | Score | Justification |
|---------|:-----:|---------------|
| Sources techniques (Still Alive Bot, Sarcophagus, DAO) | 6/10 | Tech existe mais documentee hors contexte militant |
| Test empirique | 2/10 | Aucun outil teste en contexte repressif |
| Contre-exemples (echecs tech) | 4/10 | Telegram bloque dans 15 pays — cite mais non explore |
| Falsifiabilite | 6/10 | Si un leader est arrete et le mouvement s'effondre, le protocole est invalide |
| Auto-critique | 7/10 | 4 limites bien identifiees mais pas de critique de la dependance technique |

**Biais identifiés :**
1. **Biais techno-solutionniste** : la technologie est presentee comme solution alors qu'elle est un point de defaillance
2. **Biais de complexite** : les outils (DAO, smart contracts) sont hors de portee des militants moyens
3. **Biais de securite** : aucun protocole ne resiste a la torture ou a la compromission du leader arrete
4. **Biais de confiance dans la tech** : un dead man's switch suppose que le serveur n'est pas compromis

---

## §13 SOURCES & FACTS ADDITIONNELS

| ID | Fait | Fiabilité |
|----|------|:---------:|
| F-SUC-001 | Still Alive Bot (Telegram) : check-in quotidien, duress PIN, intervalle configurable | ✧ |
| F-SUC-002 | Sarcophagus (Ethereum + Arweave) : dead man's switch blockchain, deja deploye | ✧ |
| F-SUC-003 | Aucun outil de succession automatisee n'a ete teste en contexte repressif | ✧ |
| F-SUC-004 | Telegram est bloque dans 15 pays (2025) — dependance technique | ✦ |
| F-SUC-005 | Les DAOs (Safe, OpenZeppelin) sont testees mais hors contexte militant | ✦ |
