# QUINTESSENCE : RIC et Infrastructures Crypto/DAO (Aragon, Snapshot, Blockchain, Sybil resistance)

**Source :** `investigations/2026-07-04-RIC/2026-07-05_20-00_ric_crypto_dao_aragon_snapshot_blockchain_INVESTIGATION.md`
**Date source :** 2026-07-05 [§0(estimé)]
**Date quintessence :** 2026-07-08
**Investigateur source :** Truth Engine v2.0 [§0(estimé)]
**Statut source :** COMPLETE
**Type :** ENQ-11 du Manifeste RIC H2 2026
**Périmètre source :** Aragon DAO platform + Snapshot off-chain voting + Compound/Uniswap governance + Gitcoin Grants QF + ConstitutionDAO + Optimism RPGF + Vitalik Buterin [§0(estimé)]
**Format quintessence :** Phase 1 KISS v1.0 canonique (9 H2 numérotés, post-refonte prompt-v35.md 2026-07-08)

---

## 1. Métadonnées & trace source

- **Question forensique :** Les infrastructures blockchain / DAO (Aragon, Snapshot, Compound, Uniswap, Gitcoin, Optimism RPGF, ConstitutionDAO) peuvent-elles fournir une infrastructure opérationnelle pour un RIC français, ou la gouvernance token-weighted est-elle structurellement incompatible avec le principe démocratique « 1 personne = 1 voix » ? [§1(estimé)]
- **Sous-questions SQ1-SQ6 :**
  - SQ1 : Quelle infrastructure blockchain existe pour voter et exécuter des décisions ? [§1(estimé)]
  - SQ2 : Quelle distinction entre vote on-chain vs off-chain (gasless Snapshot vs execution Ethereum) ? [§1(estimé)]
  - SQ3 : Qu'est-ce que la Sybil resistance (Proof of Humanity, Worldcoin, BrightID) ? [§1(estimé)]
  - SQ4 : Les DAO actuelles sont-elles démocratiques ? (token-weighted, delegation, Bialek-Kondrich 2023) [§1(estimé)]
  - SQ5 : Quadratic Voting (Lalley-Hansen, Buterin-Posada) permet-il une meilleure participation ? [§1(estimé)]
  - SQ6 : Quel coût économique et technique d'un RIC sur blockchain ? [§1(estimé)]
- **Hors-scope :** Bitcoin (pas programmable), cryptocurrency non-gouvernance (vs tokens gouvernance) [§1(estimé)]
- **Statut source :** COMPLETE
- **MNEMOLITE STATUS :** DOWN (port 8002 injoignable le 2026-07-05, mode dégradé sources institutionnelles) [§0(estimé)]
- **AXIOME 95% SUSPICION :** actif, y compris contre infrastructures DAO (Aragon, Snapshot) et white papers crypto - pénalité 0.5x sur chiffres de gouvernance publiée par les projets eux-mêmes (bias classic auto-promotion) [§0(estimé)]
- **13 sources institutionnelles directes (§2 source) :** Aragon Network, Snapshot.org, Compound governance, Uniswap governance forum, Gitcoin, OpenZeppelin, Juicebox, ENS docs, Optimism governance, Euler Foundation, Reality.eth, Vitalik Buterin, AMF [§2:L30-L70(estimé)]
- **Notation notation :**
  - ✦ : 1/12 (8%)
  - ✧ : 11/12 (92%)
  - ⁅ : 0/12 (0%)
  - Taux de vérification insuffisant - beaucoup de faits crypto pas primary source [§15(estimé)]

---

## 2. Faits atomiques préservés

12 faits canoniques (F-CRYPTO01 à F-CRYPTO12) du FACT_REGISTRY §12, notation source conservée.

| ID | Fait (avec date) | Notation | Trace |
|----|------------------|----------|-------|
| F-CRYPTO01 | Aragon (lancement 2017) : DAO platform on Ethereum | ✦ | [§12:L320-L325(estimé)] |
| F-CRYPTO02 | Snapshot (lancement 2020) : off-chain voting, gasless EIP-712 signature | ✧ | [§12:L325-L330(estimé)] |
| F-CRYPTO03 | Foundation Aragon : 275 000 ETH crowdsale 2017 | ✧ | [§12:L330-L335(estimé)] |
| F-CRYPTO04 | Compound COMP : premier déploiement Snapshot Q1 2021 ; >110 proposals Q2 | ✧ | [§12:L335-L340(estimé)] |
| F-CRYPTO05 | Uniswap UNI gouvernance 2020 : 400M tokens, délégation > 65% | ✧ | [§12:L340-L345(estimé)] |
| F-CRYPTO06 | Gitcoin QF 60M$ distribues depuis 2018 (50+ rounds) | ✧ | [§12:L345-L350(estimé)] |
| F-CRYPTO07 | ConstitutionDAO novembre 2021 : 47-49M$ ETH échoué Sotheby's | ✧ | [§12:L350-L355(estimé)] |
| F-CRYPTO08 | ENS DAO Snapshot governance > 50 proposals actives 2024 | ✧ | [§12:L355-L360(estimé)] |
| F-CRYPTO09 | Optimism RPGF : 3 rounds 2023-2024 > 200M$ distribues | ✧ | [§12:L360-L365(estimé)] |
| F-CRYPTO10 | Euler DAO gouvernance smart contracts 2023+ | ✧ | [§12:L365-L370(estimé)] |
| F-CRYPTO11 | Reality.eth oracle bond-based resolution | ✧ | [§12:L370-L375(estimé)] |
| F-CRYPTO12 | Vitalik Buterin « DAOs and Democracy » 2023 article | ✧ | [§12:L375-L380(estimé)] |

**Statut :** 12/12 F-CRYPTO## préservés verbatim. Notation : ✦ : 1/12 (8%) ; ✧ : 11/12 (92%) ; ⁅ : 0/12 (0%). Taux de vérification insuffisant - beaucoup de faits crypto pas primary source.

---

## 3. Acteurs nominaux

### Crypto Acteurs

| Acteur | Rôle / Position | Trace |
|--------|-----------------|-------|
| **Luu, Luis** (CTO Kyber Network, co-fondateur Aragon) | Promoteur « gouvernance algorithmique » | [§4(estimé)] |
| **Buterin, Vitalik** (co-fondateur Ethereum) | Article 2023 « DAOs and Democracy » | [§4(estimé)] |
| **Schoedon, Rain** (Aragon Foundation) | Conseil et gouvernance | [§4(estimé)] |
| **Hassan, Niberts** (Snapshot developers) | Plateforme off-chain | [§4(estimé)] |
| **Leshner, Robert** (Compound founder) | Gouvernance token-weighted COMP | [§4(estimé)] |
| **Adams, Hayden** (Uniswap founder) | Gouvernance UNI 400M tokens | [§4(estimé)] |
| **Buterin + Hitzig + Weyl** (Quadratic Voting book 2019) | QV/ pluralisme radical | [§4(estimé)] |
| **Posada, Martin** (QF research) | Mécanismes QF refunds | [§4(estimé)] |

### Régulateurs

| Acteur | Position | Trace |
|--------|----------|-------|
| **AMF** (Autorité des Marchés Financiers) | Encadrement crypto France depuis 2019 | [§4(estimé)] |
| **BCE** | Sénateur crypto consolidation 2024 | [§4(estimé)] |
| **ESMA** (European Securities Markets Authority) | Encadrement MiCA 2023 | [§4(estimé)] |
| **Babacan, Emine** (BCE Supervisory Board, ex-ING Direct) | Position crypto restrictive | [§4(estimé)] |

### Critiques académiques

| Acteur | Position | Trace |
|--------|----------|-------|
| **Bialek, Stephen** (Princeton) | « DAO governance and oligarchy » (2022) | [§4(estimé)] |
| **Kondrich, Samuel** | « Sybil resistance in DAO voting » | [§4(estimé)] |
| **Buterin vs Hitzig + Weyl (2019)** | Pluralisme radical vs quadratic voting | [§4(estimé)] |

---

## 4. Sources externes citées

### Sources institutionnelles directes (13)

| Source | URL | Trace |
|--------|-----|-------|
| Aragon Network (site officiel) | https://aragon.org/about | [§2(estimé)] |
| Snapshot.org (docs) | https://docs.snapshot.org/ | [§2(estimé)] |
| Compound governance | https://comp.xyz/t/governance | [§2(estimé)] |
| Uniswap governance forum | https://gov.uniswap.org/ | [§2(estimé)] |
| Gitcoin mechanisms | https://gitcoin.co/mechanisms | [§2(estimé)] |
| OpenZeppelin docs | https://docs.openzeppelin.com/ | [§2(estimé)] |
| Juicebox (ConstitutionDAO success story) | https://juicebox.money/success-stories/constitutiondao | [§2(estimé)] |
| ENS docs | https://docs.ens.domains/ | [§2(estimé)] |
| Optimism governance | https://gov.optimism.io/ | [§2(estimé)] |
| Euler Foundation | https://euler.foundation/ | [§2(estimé)] |
| Reality.eth oracle | https://reality.eth.limo/ | [§2(estimé)] |
| Vitalik Buterin « DAOs and Democracy » | https://vitalik.eth.limo/general/2023 | [§2(estimé)] |
| AMF (encadrement crypto France) | https://www.amf-france.org/ | [§2(estimé)] |

### Doctrine secondaire (§13 source)

| Auteur | Œuvre | Trace |
|--------|-------|-------|
| Buterin, Vitalik + Hitzig + Weyl (2019) | *RadicalxChange: Pluralism Quadratic Voting* | [§13(estimé)] |
| Lalley, Steven + Hanson, Robin (2019) | *Quadratic Voting* | [§13(estimé)] |
| Bialek, Stephen (2022) | *DAO governance and oligarchy* | [§13(estimé)] |
| Wright, Aaron (2021) | *The Rise of Decentralized Autonomous Organizations* | [§13(estimé)] |
| Morrison, Will (2024) | *Crypto Democracy and the limits of decentralization* | [§13(estimé)] |

---

## 5. Chronologie datée

### Cadrage temporel 2013-2024

| Borne | Date | Événement | Trace |
|-------|------|-----------|-------|
| Ethereum | 2013 | Vitalik Buterin lance Ethereum whitepaper ; concept de smart contracts programmable | [§3(estimé)] |
| Aragon | mars 2017 | Aragon Network lancée : première plateforme complète de création de DAO. Crowdsale : 275 000 ETH levés (~26 Md€ au pic ETH 2021). Couche de gouvernance sur Ethereum | [§3(estimé)] |
| DAO stack | mai 2018 | Infrastructure technique Aragon | [§3(estimé)] |
| Uniswap gouvernance | septembre 2020 | Décentralisation governance UNI token (initialement 400M UNI). Délégation voting à 65% en 6 mois | [§3(estimé)] |
| Snapshot | août 2020 | Snapshot.org lancée : voting platform off-chain (signature cryptographique sans gas fees). Devient le standard DAO voting 2021+ | [§3(estimé)] |
| Compound | avril 2021 | Premier déploiement majoritaire Snapshot. 110 proposals Q2 2021 | [§3(estimé)] |
| ConstitutionDAO | mai-juillet 2021 | Crowd-fund de 47-49 M$ en ETH pour enchérir sur une copie de la Constitution US (vendue Sotheby's). Échec enchère | [§3(estimé)] |
| Gitcoin Grants rounds | 2021+ | Mécanisme quadratic funding (QF) distribué > 60M$ depuis 2018 | [§3(estimé)] |
| Optimism RPGF | 2023 | Optimism lance RPGF (Retroactive Public Goods Funding) : 3 rounds distribués > 200M$ en tokens OP | [§3(estimé)] |
| Vitalik « DAOs and Democracy » | 2023 | Vitalik Buterin publie « DAOs and Democracy » : « DAOs are not democracies but continuous democracy » - analyse critique | [§3(estimé)] |
| ENS DAO | 2024 | ENS DAO gouvernance décentralisée sur Snapshot ; > 50 proposals actives | [§3(estimé)] |

### Profondeur historique

2013-2024 (11 ans). Bornes investigation : 2017-2024 (7 ans depuis Aragon).

---

## 6. Mécanismes / chaînes causales

5 chaînes causales PELOTE source §6 (sans anticipation Phase 2/2.5/2.6/3).

### Chaîne (1) : Aragon 2017 >> DAO deployments >> first-mover territoire >> représentation ploutocratique 1 token = 1 vote
- **Condition :** le modèle Aragon représente bien le type DAO non-démocratique au sens classique
- **Trace :** [§6:L210-L220(estimé)]

### Chaîne (2) : Snapshot 2020 >> gasless voting >> adoption massive (10 000 spaces) >> signal communautaire off-chain
- **Condition :** Snapshot permet la participation populaire sans gas fees ; mais l'exécution nécessite multisig on-chain (gap entre signal et execution)
- **Trace :** [§6:L220-L230(estimé)]

### Chaîne (3) : Compound Uniswap UNI >> token-weighted vote >> délégation massive >> oligarchie_token vesting
- **Condition :** la Concentration gouvernance () ~10% des tokenisers les plus gros, soit 80% des votes délégation
- **Trace :** [§6:L230-L240(estimé)]

### Chaîne (4) : ConstitutionDAO novembre 2021 >> 47-49M$ >> Échec enchère mais opérationnel réussi >> modèle « crowd-fund politique »
- **Condition :** les DAO permettent la mobilisation money rápida ; mais on ne contrôle pas les resultats du marché externe (encheres)
- **Trace :** [§6:L240-L250(estimé)]

### Chaîne (5) : Quadratic Funding Gitcoin >> 60M$ > en 50 rounds >> soutien biens publics open source >> alternative aux subventions publiques
- **Condition :** QF constitue un mécanisme de financement infragouvernemental viable ET democratique
- **Trace :** [§6:L250-L260(estimé)]

### Tissage des 5 chaînes

**Architecture technique (§5 source)** :
- **Aragon (DAO deployment platform) :** Layer de gouvernance sur Ethereum. Smart contracts : Court (juridiction arbitral), Voting (token-weighted), Finance (treasury). 2024 : Aragon OSx sur Polygon + custom chain zKEVM.
- **Snapshot (off-chain voting) :** Signatures cryptographiques (EIP-712). Pas de gas fees (gratuit utilisateur). Calcul vote on-chain mais résultat hors-chaîne. Résolutions via multisig on-chain (pratique). 2024 : ~10 000 spaces actifs.
- **Compound Governor Bravo :** Gouvernance token-weighted COMP. Vote capitalization + delegation. Executed on-chain via time-lock.
- **Uniswap Governance :** UNI token (1 token = 1 vote). Délégation votée via forum gov.uniswap.org. Snapshot signal + on-chain execution.
- **Gitcoin Grants (Quadratic Funding) :** QF mécanisme : formula \sum \sqrt{s_i}. 60M$ distribue 2018-2024 (50+ rounds). Donator recois matching pool proporcional sqrt contribution.
- **ConstitutionDAO (Juicebox) :** 47-49M$ en ETH collectés novembre 2021. Pour essayer acheter 1 Constitution Sotheby's. Vente 43M$ ; ont perdu l'enchère.
- **Optimism RPGF :** Retroactive funding : récompense les projets ayant produit du bien public. 3 rounds 2023-2024 ; > 200M$ distribues.
- **Reality.eth (oracle) :** Bond-based oracle : résolution questions/disputes via staking. Bouton « Yes/No » avec cost-based security.
- **Sybil resistance :** Proof of Humanity (UBI protocol), Worldcoin (iris scan), BrightID (social graph), Gitcoin Passport (multi-système).
- **Quadratic Voting / Funding :** Lalley-Hansen (2019 research), Buterin-Hitzig-Weyl (2019 book), Posada mechanisms QF refunds.

[§5:L160-L210(estimé)]

---

## 7. Verbatim et citations

| # | Citation | Source | Trace |
|---|----------|--------|-------|
| V1 | « Les DAO actuelles utilisent « 1 token = 1 vote » → ploutocratie. Pas de démocratie « 1 personne = 1 voix » sans Sybil resistance. » | §7 Mensonge n°1 | [§7:L270-L280(estimé)] |
| V2 | « les DAO opérations on-chain nécessitent l'infrastructure Ethereum (layer consensus Proof of Stake), qui dépend indirectement d'entreprises majeurs (Ethereum Foundation, ConsenSys, vibes). » | §7 Mensonge n°2 | [§7:L280-L290(estimé)] |
| V3 | « DAOs are not democracies but continuous democracy » - analyse critique. | Vitalik Buterin (2023) | [§3(estimé)] |
| V4 | « « continuous democracy » + « 1 token = 1 vote » = « continuous plutocracy ». » | §7 Mensonge n°3 | [§7:L290-L300(estimé)] |
| V5 | « ConstitutionDAO a essayé acheter 1 exem Rare ; ils ont perdu l'enchère à 43M$ (Ken Griffin Citizen). » | §7 Mensonge n°4 | [§7:L300-L310(estimé)] |
| V6 | « QF réduit mais ne supprime par le biais de concentration. QV (Quadratic Voting) Buterin-Hitzig-Weyl propose mais petite mise en oeuvre. » | §7 Mensonge n°5 | [§7:L310-L320(estimé)] |
| V7 | « Un RIC français adossé sur infrastructures Blockchain devrait éviter le modèle ploutocratique pure « 1 token = 1 vote ». Privilégier « 1 personne = 1 vote » via Sybil resistance (Proof of Humanity, Worldcoin, BrightID). » | §8 Recommandation 1 | [§8:L330-L340(estimé)] |
| V8 | « Mélanger vote on-chain (exécution) et off-chain (signal) : Snapshot pour la consultation avec gas fees réduites, mais exécution Constitution RIC codifiée dans solids in chain. » | §8 Recommandation 2 | [§8:L340-L350(estimé)] |
| V9 | « Quadratic Funding (QF) en tant que mécanisme déploiement : le vote RIC peut être couplé à un appel de dons quadratique ; le meilleur projet co-finance. » | §8 Recommandation 3 | [§8:L350-L360(estimé)] |
| V10 | « La blockchain est facilitateur, pas substitut. Un RIC codé sur blockchain reste politique - il faut constitution RIC qui valide la blockchain comme manteau. » | §8 Recommandation 4 | [§8:L360-L370(estimé)] |
| V11 | « Un attaquant contrôlant n identités artificielles doit payer un coût C(k) = k^2 * p où k = nombre de votes inflationnés, p = prix par vote unique. Pour prouver l'identité (1 personne = 1 voix), le modèle Sybil-resistance doit présenter un coût marginal d'attaque > valeur extraite du vote, sinon le mécanisme est économiquement attaquable. » | Buterin, Hitzig & Weyl (2019) page 142 | [§14 / F-CRYPTO12(estimé)] |

---

## 8. Notes méthodologiques source

- **Statut source :** COMPLETE [§14(estimé)]
- **Format source :** INVESTIGATION 16 sections §0-§15 [§0(estimé)]
- **Faits atomiques :** 12 (F-CRYPTO01 à F-CRYPTO12) [§12(estimé)]
- **13 sources institutionnelles directes** : Aragon Network, Snapshot.org, Compound governance, Uniswap governance forum, Gitcoin, OpenZeppelin, Juicebox, ENS docs, Optimism governance, Euler Foundation, Reality.eth, Vitalik Buterin, AMF [§2(estimé)]
- **BIAS TEST (5 biais identifiés §0 source) :**
  1. ✦ Biais crypto-bros : souvent présentée comme « democracy 2.0 », mais gouvernance DAO actuelles sont ploutocratiques (1 token = 1 vote) ; pas de démocratie directe au sens classique [§0(estimé)]
  2. ✧ Biais Sybil resistance : une identité = une voix présuppose Sybil resistance robuste (Proof of Humanity, Worldcoin) ; infrastructures encore expérimentales [§0(estimé)]
  3. ✧ Biais de matérialité : adoption très faible (millions d'utilisateurs Ethereum vs 67M Français) ; transposition RIC + DAO hasardeuse [§0(estimé)]
  4. ✦ Auto-suspicion Truth Engine : produit dossier piloté par LLM, biais structurel possible pro-blockchain (techno-utopie) ; compenser par triangulation critique AMF/BCE [§0(estimé)]
  5. ✧ Méthodologie : vote on-chain vs off-chain produit effets différents (gasless vs execution) ; ne pas confondre [§0(estimé)]
- **STATUT BIAS TEST :** PASS (5 biais identifiés, contre-mesures documentées en §11 PELOTE) [§0(estimé)]
- **Mensonge n°1 (Medias crypto-bros) :** « Les DAO sont des démocraties directes numériques ». Réalité : les DAO actuelles utilisent « 1 token = 1 vote » → ploutocratie. Pas de démocratie « 1 personne = 1 voix » sans Sybil resistance [§7(estimé)]
- **Mensonge n°2 (Crypto enthousiastes) :** « Blockchain supprime le besoin d'État ». Réalité : les DAO opérations on-chain nécessitent l'infrastructure Ethereum (layer consensus Proof of Stake), qui dépend indirectement d'entreprises majeurs (Ethereum Foundation, ConsenSys, vibes) [§7(estimé)]
- **Mensonge n°3 (Buterin optimistic) :** « DAOs are democracy continuous ». Réalité : mais « continuous democracy » + « 1 token = 1 vote » = « continuous plutocracy » [§7(estimé)]
- **Mensonge n°4 (ConstitutionDAO succès) :** « DAO humble Sotheby's ». Réalité : ConstitutionDAO a essayé acheter 1 exem Rare ; ils ont perdu l'enchère à 43M$ (Ken Griffin Citizen) [§7(estimé)]
- **Mensonge n°5 (Quadratic Funding) :** « QF eliminates plutocracy ». Réalité : QF réduit mais ne supprime par le biais de concentration. QV (Quadratic Voting) Buterin-Hitzig-Weyl propose mais petite mise en oeuvre [§7(estimé)]
- **Réponse SQ1-SQ6 :**
  - SQ1 : Smart contracts Ethereum + Aragon + Snapshot + Compound Governor Bravo + Reality.eth oracle [§14(estimé)]
  - SQ2 : On-chain = execution ; off-chain (Snapshot) = signal ; gap entre les deux [§14(estimé)]
  - SQ3 : Proof of Humanity + Worldcoin iris + Gitcoin Passport + BrightID social graph [§14(estimé)]
  - SQ4 : Non, DAO = théorie ploutocratique [§14(estimé)]
  - SQ5 : Quadratic Voting mitige mais ne supprime pas [§14(estimé)]
  - SQ6 : Coût operationnel wallet gas + signature sybil + oracle [§14(estimé)]
- **FL-8 Sybil-attack opérationnalisation (Saison 3) :** Buterin, Hitzig & Weyl, « RadicalxChange: Pluralism Quadratic Voting » (2019), page 142, formalisent mathématiquement le coût d'une attaque Sybil [§14(estimé)]
- **Métadonnées forensiques :**
  - Complexité investigation : 14/18 (political=2, technical=5, temporal=2, narratives=2, data=2, geo=1) [§14(estimé)]
  - Confiance globale : 0.50 (modérée) [§14(estimé)]
  - EDI ajusté : 0.756 [§14(estimé)]
  - Investigation Batch 3 - 3/4 livrées [§14(estimé)]
- **Notation notation notation notation :**
  - ✦ : 1/12 (8%)
  - ✧ : 11/12 (92%)
  - ⁅ : 0/12 (0%)
  - Position intermédiaire [§15(estimé)]
- **PELOTE 12 phases :** research / diverge / trace / verify / extensions / anti-bullshit / outillage / weak signals / incoherences / falsifications / indirect evidence / registre [§11(estimé)]
- **Re-vérification recommandée (Saison 3) :** Aragon OSx Polygon 2024 - transposé RIC ? ; MiCA encodage Europe + AMF ; Polygon zkEVM / Railgun / zk-SNARKs RIC biodiversité ; Sybil resistance national (prob. WID/CNIL) ; Quadratic Voting simulation France 67 M citoyens [§15(estimé)]

---

## 9. Limites connues de cette extraction (case-limites)

| Cas-limite | Statut | Documenté par |
|------------|--------|---------------|
| Traces `[Lxx]` approximatives pour positions sections H2 et tables (estimation ±10-30 lignes faute grep explicite) | global | SPECS v40 v2 KISS Règle absolue |
| Documentation officielle partiale (crypto websites paywalls) | gap | [§9(estimé)] |
| Mnemolite DOWN : pas de cross-ref with season 1 fiches (p0_civictech) | gap | [§9(estimé)] |
| PAS de triangulation capitalisation marché crypto (volatile) | gap | [§9(estimé)] |
| AMF encadrement miCA 2024 | gap | [§9(estimé)] |
| Sybil resistance infrastructure non-rocée au niveau national | gap | [§9(estimé)] |
| Notation ✦ (1/12) faible : pas de primary source pour faits crypto | threshold | [§15(estimé)] |
| Sur-vente « DAO = démocratie » sans Sybil resistance | erreur mesure | [§15(estimé)] |
| Sous-estim technologie infrastructurelle : Ethereum Foundation / ConsenSys / Coinbase | erreur mesure | [§15(estimé)] |
| Biais techno-utopique global | erreur mesure | [§15(estimé)] |
| Phases en aval (Phase 2/2.5/2.6/3) non anticipées | global | SPECS v40 v2 KISS §Refus |
| Recommandations §8 source : listées verbatim sans hiérarchisation doxa/contre-doxa (Phase 1 neutre) | §8 | SPECS v40 v2 §Refus |

**Verdict de complétude Phase 1** : 12/12 F-CRYPTO## préservés verbatim, 5/5 chaînes causales PELOTE préservées, 0 em-dash, refus Phase 1 (pas d'angle, pas de thèse, pas d'anticipation Phase 2), 9 sections H2 numérotées canoniques, §7 (11 citations verbatim) et §8 (15 notes méthodologiques) remplies.

---
