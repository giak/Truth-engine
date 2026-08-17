# INVESTIGATION — La gouvernance de l'ODC (SIREN 805407194) : le CA et le président enfin établis

RUN_MANIFEST
ENGINE_VERSION:2.8 | STATE:FINAL | RUN_ID:20260814-1300-odc-gouvernance | PARENT_RUN_ID:20260814-1234-conspiracywatch-info-registre
AS_OF:2026-08-14 | INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | SUBJECT_SLUG:odc-gouvernance
COMPLEXITY:MEDIUM | MÉTHODE: KERNEL v2.8

Statuts : ✦ confirmé (primaire/corroboration) · ✧ probable · ⁕ allégué · ⁅ inconnu.

---

## §0 OBJET ET BORNE

**Question objet** : établir la gouvernance réelle de l'association Observatoire du conspirationnisme (ODC, SIREN 805407194) — président, direction, membres du bureau — qui restait un trou du corpus (on ne connaissait que Reichstadt, Igounet, TMF).

**Borne** : l'enquête porte sur *qui décide* dans la structure éditrice de CW. Elle n'établit aucune infraction (une association déclarée a une gouvernance légale, publique par nature).

---

## §1 SOURCES

| SRC-ID | Source | Nature | URL |
|---|---|---|---|
| SRC-01 | Pappers, fiche ODC (RNA W751225511, SIREN 805407194) | ◈ agrégateur de registres officiels | https://www.pappers.fr/entreprise/observatoire-du-conspirationnisme-805407194 |
| SRC-02 | API recherche-entreprises (data.gouv) | ◈ officiel INSEE/RNA | https://recherche-entreprises.api.gouv.fr/search?q=805407194 |
| SRC-03 | Wikipédia, Iannis Roder | ◉ secondaire | https://fr.wikipedia.org/wiki/Iannis_Roder |
| SRC-04 | HAL-SHS, « L'anti-complotisme officiel » (05/2026) | 🎓 académique | https://shs.hal.science/halshs-05624775v1 |
| SRC-05 | Fondation Jean-Jaurès, rapport d'activité 2023 | ◈ primaire | https://www.jean-jaures.org/wp-content/uploads/2024/04/RA-2023.pdf |
| SRC-06 | AEF Info (18/10/2023) | ◉ presse | — |

---

## §2 FAITS (FACT_REGISTRY)

| FCT-ID | Fait | Statut | Source |
|---|---|---|---|
| FCT-01 | L'ODC (SIREN 805407194, SIRET 805407194 00028, RNA **W751225511**) est une **association déclarée** créée le **21/07/2014**, siège Maison des Associations du 11e, 8 rue du Général Renault, 75011. Convention collective **IDCC 1480** (journalistes). | ✦ | SRC-01/02 |
| FCT-02 | **Le président de l'ODC est Iannis Roder** (professeur agrégé d'histoire-géographie), et **non Rudy Reichstadt** (qui en est le fondateur/directeur). | ✦ | SRC-03/04 |
| FCT-03 | **Iannis Roder est simultanément directeur de l'Observatoire de l'éducation de la Fondation Jean-Jaurès.** | ✦ | SRC-03/05 |
| FCT-04 | **Valérie Igounet est « directrice adjointe de l'Observatoire du conspirationnisme »** (AEF Info, 18/10/2023) ; elle est par ailleurs membre de la **commission « Lutte contre l'antisémitisme » de la FMS** (dossier 10-46). | ✦ | SRC-06 + dossier 10-46 |
| FCT-05 | Roder a été nommé à la présidence (ou à une fonction officielle) le **29/09/2021** (date figurant dans ses bios). | ✧ | SRC-03 |
| FCT-06 | **Le « Liste dirigeants » de l'ODC n'est PAS dans l'API ouverte INSEE/RNA** (champ `dirigeants` vide) ; Pappers indique « Information indisponible. Voir section annonces BODACC. » Les documents « Liste dirigeants » existent à la préfecture (24/07/2014, 08/12/2016, 05/04/2017). | ✦ | SRC-01/02 |
| FCT-07 | JOAFE : CRÉATION 21/07/2014 (277 rue du Fbg St-Antoine), MODIFICATION 20/03/2017, MODIFICATION 26/04/2024 (JOAFE n°20240019, annonce n°1459). | ✦ | SRC-01 |
| FCT-08 | **Effectif** : Pappers affiche « Entre 3 et 5 salariés (donnée 2022) », tandis que la tranche INSEE récente est « 03 » = 6-9 salariés (dossier 10-15). **Écart non réconcilié** — cohérent avec une croissance 2022 → récent, mais à borner. | ⊙ | SRC-01 vs dossier 10-15 |
| FCT-09 | 1 contentieux : Tribunal judiciaire de Paris, 12/06/2024, n° 23/15454, ODC **défendeur**, « prononce la nullité de l'assignation ». **Aucun compte annuel déposé** (confirmé : « Aucun compte n'est disponible »). **Aucune aide européenne** enregistrée. | ✦ | SRC-01 |
| FCT-10 | Objet associatif (JOAFE 2024) : « édition d'un service de presse en ligne **d'information politique et générale** » — confirme l'auto-qualification « IPG » contredite par la CPPAP (39bisA, dossier 11-11). | ✦ | SRC-01 |

---

## §3 VERDICT (borné)

**La gouvernance de l'ODC est désormais établie, et elle révèle un nœud que le corpus n'avait pas cartographié :**

1. **Le président de l'ODC n'est pas Reichstadt.** C'est **Iannis Roder**, professeur agrégé d'histoire et **directeur de l'Observatoire de l'éducation de la Fondation Jean-Jaurès**. Reichstadt est le fondateur/directeur du *site* ; Roder préside l'*association*. La distinction — documentée par la phrase de Reichstadt au Sénat « Je n'en suis pas le président » — est désormais sourcée.

2. **La Fondation Jean-Jaurès est liée à CW à deux niveaux** : (a) Reichstadt y est « expert associé » (dossier RESEAU_WOLF) ; (b) le **président de l'ODC en dirige un observatoire**. La Fondation Jean-Jaurès (think tank du PS) n'était jusqu'ici qu'une appartenance de Reichstadt ; elle est désormais un **nœud de gouvernance** de l'association.

3. **Valérie Igounet cumule deux positions clés** : directrice adjointe de l'ODC **et** membre de la commission « Lutte contre l'antisémitisme » de la FMS (le financeur principal de CW). C'est la **jonction gouvernance-financement** : la même personne siège dans la structure éditrice et dans la commission du financeur.

4. **La structure complète du bureau reste partiellement opaque** : les « Liste dirigeants » (trésorier, secrétaire, autres membres) sont déposées à la préfecture (2014, 2016, 2017) mais **non publiées dans l'API ouverte**. Le corpus a établi le triangle président/directeur/directrice-adjointe, pas le bureau complet.

**Implication pour le corpus** : ce dossier comble le « trou de gouvernance » et ajoute un **nouveau nœud institutionnel** (Fondation Jean-Jaurès) au réseau CW. La configuration « think tank de gauche (Jean-Jaurès) + fondation de la communauté juive (FMS) + subventions d'État (DILCRAH/CIPDR) » est désormais documentée **jusque dans le CA de l'association**.

---

## §4 PÉRIMÈTRE & LIMITES

- Le **bureau complet** (trésorier, secrétaire, administrateurs) reste à extraire des annonces JOAFE 2014/2017/2024 (annonce n°1459) — les noms y figurent mais n'ont pas été dépouillés ici.
- La date exacte d'accession de Roder à la présidence (29/09/2021) est à confirmer contre le PV/statuts 2021 (non consulté).
- L'écart d'effectif (3-5 en 2022 vs 6-9 récent) reste un point à réconcilier — probable croissance, non tranché.

*KERNEL v2.8. Gouvernance établie (Roder préside, Reichstadt dirige, Igounet adjointe) ; bureau complet partiellement opaque.*
