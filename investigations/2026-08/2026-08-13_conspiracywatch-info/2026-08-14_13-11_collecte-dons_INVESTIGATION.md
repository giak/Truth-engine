# INVESTIGATION — La collecte de dons de CW : HelloAsso + Ulule (174 abonnés, total non publié)

RUN_MANIFEST
ENGINE_VERSION:2.8 | STATE:FINAL | RUN_ID:20260814-1311-collecte-dons | PARENT_RUN_ID:20260814-1234-conspiracywatch-info-registre
AS_OF:2026-08-14 | INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | SUBJECT_SLUG:collecte-dons
COMPLEXITY:SIMPLE | MÉTHODE: KERNEL v2.8

Statuts : ✦ confirmé (primaire) · ✧ probable · ⁕ allégué · ⁅ inconnu.

---

## §0 OBJET ET BORNE

**Question objet** : reconstruire le total collecté par CW auprès du public (dons + abonnements), le « 4e circuit » de financement (après État, philanthropie, avantages fiscaux).

**Borne** : le total précis n'est **pas affiché publiquement**. L'enquête borne la collecte (canaux, plancher) et confirme les affirmations d'auto-qualification « IPG ».

---

## §1 SOURCES

| SRC-ID | Source | Nature | URL |
|---|---|---|---|
| SRC-01 | Ulule, campagne « Soutien Conspiracy Watch » | ◈ primaire | https://fr.ulule.com/soutien-conspiracy-watch/ |
| SRC-02 | HelloAsso, formulaire de don ODC | ◈ primaire | https://www.helloasso.com/associations/observatoire-du-conspirationnisme/formulaires/1 |

---

## §2 FAITS (FACT_REGISTRY)

| FCT-ID | Fait | Statut | Source |
|---|---|---|---|
| FCT-01 | CW collecte via **deux canaux** : HelloAsso (don « Montant libre ») et **Ulule** (abonnements « dès 5 €/mois » + don mensuel/unique). | ✦ | SRC-01/02 |
| FCT-02 | La campagne Ulule affiche **« 174 / 1 000 membres »** (abonnements) — un plancher de **174 abonnés payants**, sur un objectif de 1 000. | ✦ | SRC-01 |
| FCT-03 | **Le total en euros collecté n'est affiché sur aucune des deux pages** (seul le nombre de membres Ulule est public). | ⁅ | SRC-01/02 |
| FCT-04 | CW revendique « **une dizaine de collaborateurs** » (cohérent avec la tranche INSEE 6-9 + une traîne de pigistes). | ✦ | SRC-01 |
| FCT-05 | CW réitère l'auto-qualification : « service de presse reconnu **d'information politique et générale (IPG)**… réduction d'impôt de **66 %** » — la même formulation juridiquement inexacte du dossier 10-56 (le fondement réel est « intérêt général », art. 200 CGI ; CW = 39bisA, pas IPG). | ✦ | SRC-01 |
| FCT-06 | L'équipe est « réunie autour de **Rudy Reichstadt, Valérie Igounet et Tristan Mendès France** » (confirme la structure établie au dossier 13-00). | ✦ | SRC-01 |
| FCT-07 | CW affirme avoir « **systématiquement gagné** » les « procédures-bâillons » engagées contre lui (SLAPP) — corroboré par le contentieux TJ Paris 2024 (nullité d'assignation, dossier 13-00). | ✦ | SRC-01 + dossier 13-00 |

<!-- FACT_REGISTRY_V1 -->
FCT-01 | FACT | ✧ | https://fr.ulule.com/soutien-conspiracy-watch/ | - | - | 13-11_collecte-dons | - | 877127b1-255d-4824-9156-241da40358db
FCT-02 | FACT | ✧ | https://fr.ulule.com/soutien-conspiracy-watch/ | - | - | 13-11_collecte-dons | - | cb3751cc-11b5-40ce-948f-e41663e4e1fe
FCT-03 | FACT | ✧ | https://fr.ulule.com/soutien-conspiracy-watch/ | - | - | 13-11_collecte-dons | - | f48d8153-f4cf-45f5-bf0b-1539d8868b1b
FCT-04 | FACT | ✧ | https://fr.ulule.com/soutien-conspiracy-watch/ | - | - | 13-11_collecte-dons | - | e7ac914d-eeeb-4052-b153-729e7f3429d9
FCT-05 | FACT | ✧ | https://fr.ulule.com/soutien-conspiracy-watch/ | - | - | 13-11_collecte-dons | - | 81953ee5-58cb-4722-b86e-4add707d1063
FCT-06 | FACT | ✧ | https://fr.ulule.com/soutien-conspiracy-watch/ | - | - | 13-11_collecte-dons | - | 97fc027e-f933-41b0-ae5d-c6acae26eaf7
FCT-07 | FACT | ✧ | https://fr.ulule.com/soutien-conspiracy-watch/ | - | - | 13-11_collecte-dons | - | d3496670-a6ca-488a-90f3-e52c791f1b74
<!-- /FACT_REGISTRY_V1 -->

---

## §3 VERDICT (borné)

1. **Le total collecté reste le trou non comblé du 4e circuit.** CW publie le nombre d'abonnés Ulule (174/1 000) mais **pas le total en euros**. Le plancher est calculable : 174 abonnés × 5 €/mois = **~870 €/mois, soit ~10 400 €/an minimum** — mais ce plancher exclut les dons HelloAsso, les dons Ulule uniques, et les abonnés au-delà de 5 €.

2. **L'échelle de la collecte publique est modeste** face aux autres circuits. Même à 174 abonnés + dons ponctuels, la collecte publique est vraisemblablement de l'ordre de **quelques dizaines de milliers d'euros/an** — bien en deçà du budget déclaré (230 k€) et du plancher public (111 k€). La **FMS reste « l'essentiel »**, conformément à la déclaration de Reichstadt.

3. **L'auto-qualification « IPG » est réitérée sur la page de collecte**, sur fond de reçu fiscal 66 % — la même erreur juridique documentée au dossier 10-56. La page de collecte (où l'on demande de l'argent au public) est donc le **lieu précis** où CW maintient une formulation inexacte de son statut.

4. **Borne d'honnêteté** : rien d'illégal (la collecte est déclarée, le reçu fiscal est auto-apprécié). Le point est la **cohérence** : une structure qui demande au public un don défiscalisé en s'affirmant « IPG » alors qu'elle est « 39bisA » — sur la même page où elle omet les subventions publiques (111 k€) qu'elle perçoit.

**Implication pour le corpus** : le 4e circuit (dons) est **le seul que CW publicise activement** (car il sert la collecte), tout en étant le **moins transparent en valeur absolue** (aucun total publié). La structure d'opacité est symétrique : les circuits qui servent la collecte sont maximisés, les circuits qui servent la crédibilité (subventions, FMS) sont minimisés ou omis.

---

## §4 PÉRIMÈTRE & LIMITES

- Le total Ulule en euros (au-delà du nombre de membres) et le total HelloAsso ne sont pas récupérables en l'état (affichage dynamique).
- Le « 70,50 € de don moyen (2025) » (dossier 10-56) n'a pas pu être recoupé sur la page Ulule actuelle.
- Piste de clôture : le rapport annuel du reçu fiscal (obligatoire pour les associations délivrant des reçus) ou le compte rendu financier Ulule/HelloAsso — non publics.

*KERNEL v2.8. Collecte bornée (174 abonnés Ulule, plancher ~10 k€/an) ; total précis non publié ; auto-qualification « IPG » réitérée.*
