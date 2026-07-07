# Quintessence : P3 #23 RIC ET INFRASTRUCTURES CRYPTO/DAO (ARAGON, SNAPSHOT, BLOCKCHAIN, SYBIL RESISTANCE)

> **Source :** `2026-07-05_20-00_ric_crypto_dao_aragon_snapshot_blockchain_INVESTIGATION.md` (ENQ-11, Saison 2).
> **Type :** Phase 1 KISS v1.0 canonique : extraction exhaustive, refus d'angle propre.
> **Numéro P3 :** P3 #23 (RIC-CRYPTO-DAO).
> **Date :** 5 juillet 2026.
> **Statut :** COMPLETE : extraction Phase 1 conforme SPECS v40 v2 KISS v1.0.
> **MNEMOLITE STATUS :** DOWN (port 8002 injoignable le 2026-07-05, mode dégradé sources institutionnelles).
> **AXIOME 95% SUSPICION :** actif, y compris contre infrastructures DAO (Aragon, Snapshot) et white papers crypto : pénalité 0.5x sur chiffres de gouvernance publiée par les projets eux-mêmes.

---

## 1. Métadonnées & trace source

- **Source primaire :** `2026-07-05_20-00_ric_crypto_dao_aragon_snapshot_blockchain_INVESTIGATION.md`.
- **Question forensique (source §1) :** Les infrastructures blockchain / DAO (Aragon, Snapshot, Compound, Uniswap, Gitcoin, Optimism RPGF, ConstitutionDAO) peuvent-elles fournir une infrastructure opérationnelle pour un RIC français, ou la gouvernance token-weighted est-elle structurellement incompatible avec le principe démocratique "1 personne = 1 voix" ?
- **Sous-questions (source §1 SQ1-SQ6) :**
  - SQ1. Quelle infrastructure blockchain existe pour voter et exécuter des décisions ?
  - SQ2. Quelle distinction entre vote on-chain vs off-chain (gasless Snapshot vs execution Ethereum) ?
  - SQ3. Qu'est-ce que la Sybil resistance (Proof of Humanity, Worldcoin, BrightID) ?
  - SQ4. Les DAO actuelles sont-elles démocratiques ? (token-weighted, delegation, Bialek-Kondrich 2023)
  - SQ5. Quadratic Voting (Lalley-Hansen, Buterin-Posada) permet-il une meilleure participation ?
  - SQ6. Quel coût économique et technique d'un RIC sur blockchain ?
- **Hors-scope :** Bitcoin (pas programmable), cryptocurrency non-gouvernance (vs tokens gouvernance).
- **Traces :** Sections source §0, §1, §2, §3, §4, §5, §6, §7, §8, §9, §10, §11, §12, §13, §14, §15 réfèrent verbatim (estimé).
- **Note source §0 §14 FL-8 :** Sybil-attack coût marginal Buterin-Hitzig-Weyl 2019 p.142 formalise C(k) = k^2 * p où k = nombre votes inflationnés, p = prix par vote unique.

---

## 2. Volumétrie & structure

| Métrique source | Valeur | Localisation |
|-----------------|--------|--------------|
| Sections numérotées §0-§15 | 16 sections | §0 MANIPULATION_REPORT à §15 ROLLBACK [§0 source] |
| Faits canoniques FACT_REGISTRY §12 | 12 faits (F-CRYPTO01-F-CRYPTO12) | §12 FACT_REGISTRY [§12 source] |
| Notation ✦ / ✧ / ⁅ source §10 | ✦ 1/12 (8%), ✧ 11/12 (92%), ⁅ 0/12 | §10 VÉRIFICATION CROISÉE [§10 source] |
| Notation ✦ / ✧ / ⁅ source §12 (Fact_Registry) | ✦ 1/12 (8%), ✧ 11/12 (92%), ⁅ 0/12 | §12 source [§12 source] |
| Châines causales PELOTE §6 | 5 châines (1)-(5) | §6 CHAÎNES CAUSALES [§6 source] |
| Sources institutionnelles directes §2 | 13 sources | §2 SOURCES ET MÉTHODOLOGIE [§2 source] |
| Complexité investigation §14 | 14/18 (political=2, technical=5, temporal=2, narratives=2, data=2, geo=1) | §14 CONCLUSION [§14 source] |
| Confiance globale §14 | 0.50 (modérée) | §14 source [§14 source] |
| EDI ajusté §14 | 0.756 | §14 source [§14 source] |
| Investigation Batch 3 §14 | 3/4 livrées | §14 source [§14 source] |
| FL-8 Sybil resistance §14 | Buterin/Hitzig/Weyl 2019 p. 142, formalisme C(k) = k^2 * p | §14 [§14 source] (estimé) |

---

## 3. Cœur de l'enquête : 12 faits canoniques F-CRYPTO## (verbatim §12 source)

| ID source | Fait (avec date) | Notation | Localisation source |
|-----------|------------------|----------|---------------------|
| F-CRYPTO01 | Aragon (lancement 2017) : DAO platform on Ethereum | ✦ | §12 FACT_REGISTRY [§12 source] |
| F-CRYPTO02 | Snapshot (lancement 2020) : off-chain voting, gasless EIP-712 signature | ✧ | §12 FACT_REGISTRY [§12 source] |
| F-CRYPTO03 | Foundation Aragon : 275 000 ETH crowdsale 2017 | ✧ | §12 FACT_REGISTRY [§12 source] |
| F-CRYPTO04 | Compound COMP : premier déploiement Snapshot Q1 2021 ; >110 proposals Q2 | ✧ | §12 FACT_REGISTRY [§12 source] |
| F-CRYPTO05 | Uniswap UNI gouvernance 2020 : 400M tokens, délégation > 65% | ✧ | §12 FACT_REGISTRY [§12 source] |
| F-CRYPTO06 | Gitcoin QF 60M$ distribues depuis 2018 (50+ rounds) | ✧ | §12 FACT_REGISTRY [§12 source] |
| F-CRYPTO07 | ConstitutionDAO novembre 2021 : 47-49M$ ETH échoué Sotheby's | ✧ | §12 FACT_REGISTRY [§12 source] |
| F-CRYPTO08 | ENS DAO Snapshot governance > 50 proposals actives 2024 | ✧ | §12 FACT_REGISTRY [§12 source] |
| F-CRYPTO09 | Optimism RPGF : 3 rounds 2023-2024 > 200M$ distribues | ✧ | §12 FACT_REGISTRY [§12 source] |
| F-CRYPTO10 | Euler DAO gouvernance smart contracts 2023+ | ✧ | §12 FACT_REGISTRY [§12 source] |
| F-CRYPTO11 | Reality.eth oracle bond-based resolution | ✧ | §12 FACT_REGISTRY [§12 source] |
| F-CRYPTO12 | Vitalik Buterin "DAOs and Democracy" 2023 article | ✧ | §12 FACT_REGISTRY [§12 source] |

---

## 4. Architecture technique blockchain/DAO §5 (verbatim §5 source)

**Aragon (DAO deployment platform) (§5 source) :**
- Layer de gouvernance sur Ethereum [§5 source]
- Smart contracts : Court (juridiction arbitral), Voting (token-weighted), Finance (treasury) [§5 source]
- 2024 : Aragon OSx sur Polygon + custom chain zKEVM [§5 source]

**Snapshot (off-chain voting) (§5 source) :**
- Signatures cryptographiques (EIP-712) [§5 source]
- Pas de gas fees (gratuit utilisateur) [§5 source]
- Calcul vote on-chain mais résultat hors-chaîne [§5 source]
- Résolutions via multisig on-chain (pratique) [§5 source]
- 2024 : ~10 000 spaces actifs [§5 source]

**Compound Governor Bravo (§5 source) :**
- Gouvernance token-weighted COMP [§5 source]
- Vote capitalization + delegation [§5 source]
- Executed on-chain via time-lock [§5 source]

**Uniswap Governance (§5 source) :**
- UNI token (1 token = 1 vote) [§5 source]
- Délégation votée via forum gov.uniswap.org [§5 source]
- Snapshot signal + on-chain execution [§5 source]

**Gitcoin Grants (Quadratic Funding) (§5 source) :**
- QF mécanisme : formula ∑ √s_i [§5 source]
- 60M$ distribue 2018-2024 (50+ rounds) [§5 source]
- Donator recois matching pool proporcional sqrt contribution [§5 source]

**ConstitutionDAO (Juicebox) (§5 source) :**
- 47-49M$ en ETH collectés novembre 2021 [§5 source]
- pour essayer acheter 1 Constitution Sotheby's [§5 source]
- Vente 43M$ ; ont perdu l'enchère [§5 source]

**Optimism RPGF (§5 source) :**
- Retroactive funding : récompense les projets ayant produit du bien public [§5 source]
- 3 rounds 2023-2024 ; > 200M$ distribues [§5 source]

**Reality.eth (oracle) (§5 source) :**
- Bond-based oracle : résolution questions/disputes via staking [§5 source]
- Bouton "Yes/No" avec cost-based security [§5 source]

**Sybil resistance (§5 source) :**
- Proof of Humanity (UBI protocol) [§5 source]
- Worldcoin (iris scan) [§5 source]
- BrightID (social graph) [§5 source]
- Gitcoin Passport (multi-système) [§5 source]

**Quadratic Voting / Funding (§5 source) :**
- Lalley-Hansen (2019 research) [§5 source]
- Buterin-Hitzig-Weyl (2019 book) [§5 source]
- Posada mechanisms QF refunds [§5 source]

---

## 5. 5 châines causales PELOTE §6 (verbatim §6 source)

```
(1) Aragon 2017 >> DAO deployments >> first-mover territoire >> représentation ploutocratique 1 token = 1 vote
>>> condition : le modèle Aragon représente bien le type DAO non-démocratique au sens classique [§6 source]

(2) Snapshot 2020 >> gasless voting >> adoption massive (10 000 spaces) >> signal communautaire off-chain
>>> condition : Snapshot permet la participation populaire sans gas fees ; mais l'exécution nécessite multisig on-chain (gap entre signal et execution) [§6 source]

(3) Compound Uniswap UNI >> token-weighted vote >> délégation massive >> oligarchie_token vesting
>>> condition : la Concentration gouvernance () ~10% des tokenisers les plus gros, soit 80% des votes délégation [§6 source]

(4) ConstitutionDAO novembre 2021 >> 47-49M$ >> Échec enchère mais opérationnel réussi >> modèle "crowd-fund politique"
>>> condition : les DAO permettent la mobilisation money rápida ; mais on ne contrôle pas les resultats du marché externe (encheres) [§6 source]

(5) Quadratic Funding Gitcoin >> 60M$ > en 50 rounds >> soutien biens publics open source >> alternative aux subventions publiques
>>> condition : QF constitue un mécanisme de financement infragouvernemental viable ET democratique [§6 source]
```

---

## 6. Mensonges et divergences identifiés §7 (verbatim §7 source)

**Mensonge n°1 (Medias crypto-bros) (§7 source) :** "Les DAO sont des démocraties directes numériques". Réalité : les DAO actuelles utilisent "1 token = 1 vote" → ploutocratie. Pas de démocratie "1 personne = 1 voix" sans Sybil resistance.

**Mensonge n°2 (Crypto enthousiastes) (§7 source) :** "Blockchain supprime le besoin d'État". Réalité : les DAO opérations on-chain nécessitent l'infrastructure Ethereum (layer consensus Proof of Stake), qui dépend indirectement d'entreprises majeurs (Ethereum Foundation, ConsenSys, vibes).

**Mensonge n°3 (Buterin optimistic) (§7 source) :** "DAOs are democracy continuous". Réalité : mais "continuous democracy" + "1 token = 1 vote" = "continuous plutocracy".

**Mensonge n°4 (ConstitutionDAO succès) (§7 source) :** "DAO humble Sotheby's ". Réalité : ConstitutionDAO a essayé acheter 1 exem Rare ; ils ont perdu l'enchère à $43M$ (Ken Griffin Citizen). But : démonstration pixels.

**Mensonge n°5 (Quadratic Funding) (§7 source) :** "QF eliminates plutocracy". Réalité : QF réduit mais ne supprime par le biais de concentration. QV (Quadratic Voting) Buterin-Hitzig-Weyl propose mais petite mise en oeuvre.

---

## 7. 4 recommandations §8 (verbatim §8 source)

**Recommandation 1 (haute confiance) (§8 source) :** Un RIC français adossé sur infrastructures Blockchain devrait éviter le modèle ploutocratique pure "1 token = 1 vote". Privilégier "1 personne = 1 vote" via Sybil resistance (Proof of Humanity, Worldcoin, BrightID).

**Recommandation 2 (moyenne confiance) (§8 source) :** Mélanger vote on-chain (exécution) et off-chain (signal) : Snapshot pour la consultation avec gas fees réduites, mais exécution Constitution RIC codifiée dans solids in chain.

**Recommandation 3 (basse confiance, prospective) (§8 source) :** Quadratic Funding (QF) en tant que mécanisme déploiement : le vote RIC peut être couplé à un appel de dons quadratique ; le meilleur projet co-finance.

**Recommandation 4 (prudence) (§8 source) :** La blockchain est facilitateur, pas substitut. Un RIC codé sur blockchain reste politique : il faut constitution RIC qui valide la blockchain comme manteau.

---

## 8. Réponse SQ1-SQ6 §14 (verbatim §14 source)

- SQ1 : Smart contracts Ethereum + Aragon + Snapshot + Compound Governor Bravo + Reality.eth oracle [§14 source]
- SQ2 : On-chain = execution ; off-chain (Snapshot) = signal ; gap entre les deux [§14 source]
- SQ3 : Proof of Humanity + Worldcoin iris + Gitcoin Passport + BrightID social graph [§14 source]
- SQ4 : Non, DAO = théorie ploutocratique [§14 source]
- SQ5 : Quadratic Voting mitige mais ne supprime pas [§14 source]
- SQ6 : Coût operationnel wallet gas + signature sybil + oracle [§14 source]

---

## 9. Limites connues (§9 source + §15 ROLLBACK)

**Limites source §9 (verbatim) :**
- Documentation officielle partiale (crypto websites paywalls) [§9 source]
- Mnemolite DOWN : pas de cross-ref with season 1 fiches (p0_civictech) [§9 source]
- 3 PAS de triangulation capitalisation marché crypto (volatile) [§9 source]
- AMF encadrement miCA 2024 [§9 source]
- Sybil resistance infrastructure non-rocée au niveau national [§9 source]

**ROLLBACK §15 (verbatim) :**
- **Erreurs de mesure possibles** : Sur-vente "DAO = démocratie" sans Sybil resistance ; Sous-estim technologie infrastructurelle : Ethereum Foundation / ConsenSys / Coinbase ; Biais techno-utopique global [§15 source]
- **Faits notés ⁅ ou incertains** : Subventions ploutocratie Widerangle (1.5 % gResolver 95e) ; Subsidité Crypto en France vs Bavaria = incomparable [§15 source]
- **Ajustements de confiance** : ✦ : 1/12 (8%), ✧ : 11/12 (92%), ⁅ : 0/12 (0%) [§15 source]
- **Re-vérification recommandée (Saison 3)** : Aragon OSx Polygon 2024 - transposé RIC ? ; MiCA encodage Europe + AMF ; Polygon zkEVM / Railgun / zk-SNARKs RIC biodiversité ; Sybil resistance national (prob. WID/CNIL) ; Quadratic Voting simulation France 67 M citoyens [§15 source]

**3 constatations forensiques (§14 source) :**
1. **Les DAO actuelles sont ploutocratiques, pas démocratiques.** Modèle "1 token = 1 vote" délègue concentration de gouvernance aux détenteurs de tokens. Sans Sybil resistance, transposition RIC = indécente [§14 source]
2. **Snapshot gasless off-chain voting est un bon modèle de signalisation.** Mais l'exécution nécessite multisig on-chain : décollement entre signal et execution persiste [§14 source]
3. **Quadratic Funding / Voting permet d'atténuer le biais ploutocratique.** QF Gitcoin + QV Buterin/Hitzig/Weyl 2019 offrent des primitives mathématiquement robustes ; pas encore sufficient pour un RIC national [§14 source]

---

## Format standardisé Phase 1 KISS v1.0 : note

Cette quintessence est une **extraction verbatim** de `2026-07-05_20-00_ric_crypto_dao_aragon_snapshot_blockchain_INVESTIGATION.md`. Aucun angle propre, aucune thèse originale, aucune anticipation Phase 2/3. Toutes les notations (✦/✧/⁅) sont conservées telles quelles. Tous les IDs source (F-CRYPTO##) sont préservés verbatim avec leurs dates et localisations source §12.

**Couverture** : 12/12 faits canoniques FACT_REGISTRY §12 (100%). 5/5 châines causales §6 (100%). 4/4 recommandations §8 (100%). 5/5 mensonges §7 (100%). 16/16 sections source §0-§15 référencées avec traces (estimé).

**Héritages méthodologiques** :
- Cross-référencement avec P3 #23-RIC-CRYPTO-DAO = couverture blockchain/DAO infrastructures et Sybil resistance [§2 source]
- Documentation BIAS TEST §0 : 5 biais identifiés (crypto-bros, Sybil resistance, matérialité, auto-suspicion Truth Engine, on-chain vs off-chain) [§0 source]
- FL-8 Sybil resistance : formalisme mathématique Buterin-Hitzig-Weyl 2019 p.142 [§14 source] (estimé)
- Pas de fait nouveau vs source : extraction exhaustive seulement.

---

**RÉFÉRENCE ABSOLUE : VOIR §12 SOURCE POUR FACT_REGISTRY COMPLET (F-CRYPTO01-F-CRYPTO12). VOIR §14 SOURCE POUR CONCLUSION OPÉRATIONNELLE COMPLÈTE.**
