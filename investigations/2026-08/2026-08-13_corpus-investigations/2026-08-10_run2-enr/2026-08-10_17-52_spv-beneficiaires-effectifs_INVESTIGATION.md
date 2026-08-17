# INVESTIGATION : SPV ET BÉNÉFICIAIRES EFFECTIFS DES PARCS ENR

- STATE          : FINAL
- DATE           : 2026-08-10 17:52 CEST
- TYPE           : INVESTIGATION (KERNEL v2.8, format allégé axe de piste)
- DOSSIER        : 2026-08-10_run2-enr (piste ENR 07-29, axe B)
- OBJECT         : cartographier qui détient réellement les parcs ENR français via les sociétés de projet (SPV), les montages et les registres de bénéficiaires effectifs ; tester la méthode sur un cas concret (PARC EOLIEN DE MOULINS HOLDINGS)
- SOURCES        : SRC-1 à SRC-6 (voir §4)
- GAP_SEVERITY   : 0.30 (méthode testée, mais l'identité des bénéficiaires effectifs finaux non résolue sur le cas test)

## 1. VERDICT

**Le canal d'investigation existe et est public : le registre des bénéficiaires effectifs (RBE), tenu par l'INPI en France et par le Luxembourg Business Registers au Luxembourg, avec un point d'entrée européen (BORIS). La donnée « qui détient les parcs ENR » est donc juridiquement accessible, mais son exploitation passe par des recherches nominatives société par société (pas de jeu de données agrégé public sur la propriété des parcs).**

Sur le cas test (PARC EOLIEN DE MOULINS HOLDINGS, SIREN 821 148 830, Strasbourg) :
- Holding SAS au capital de 10 €, créée 03/06/2016, siège 1 rue des Arquebusiers 67000 Strasbourg, greffe de Strasbourg.
- Dirigeants déclarés : Bhogal Joginder, Zhou Feng, Beaumont Didier (Pappers, données 2026).
- Résultats : CA nul (holding), résultat net -18,4 K€ (2024), EBITDA -9,2 K€.
- **Le bénéficiaire effectif final n'est pas identifié dans les sources gratuites** : Pappers affiche les dirigeants mais pas l'actionnaire de la holding. Le RBE INPI (data.inpi.fr) exige une navigation par onglet et n'est pas agrégé en open data exploitable par script.

**Verdict honnête** : la méthode est validée en principe (RBE = canal public), mais le cas test montre que **l'identité des propriétaires finaux des SPV est un travail nominatif coûteux** : ~1 à 3 consultations par société, accès RBE INPI par page web (pas d'API), et les holdings intermédiaires (souvent au Luxembourg) nécessitent des consultations croisées dans 2 registres. Ce n'est pas un « trou noir » (la donnée existe), c'est une **résistance par friction administrative**.

## 2. FAITS

| ID | Fait | Source | Statut |
|----|------|--------|--------|
| FCT-spv-001 | PARC EOLIEN DE MOULINS HOLDINGS : SAS, SIREN 821 148 830, SIRET 821 148 830 00028, capital social 10 €, RCS Strasbourg 821 148 830, immatriculée 29/06/2016 (création établissement 03/06/2016) | SRC-1 | CONFIRMÉ |
| FCT-spv-002 | Activité déclarée : 64.20Z (activités des sociétés holding), forme d'exercice « gestion de biens » | SRC-1 | CONFIRMÉ |
| FCT-spv-003 | Dirigeants déclarés (donnée 2026) : Bhogal Joginder, Zhou Feng, Beaumont Didier | SRC-1 | CONFIRMÉ |
| FCT-spv-004 | Résultats 2024 : CA non publié, EBITDA -9,2 K€, résultat net -18,4 K€ ; BFR 78 K€ ; délai de paiement fournisseurs 298 jours | SRC-1 | CONFIRMÉ |
| FCT-spv-005 | Le RBE (registre des bénéficiaires effectifs) français est tenu par l'INPI ; la consultation passe par data.inpi.fr (navigation web, pas d'API publique agrégée) | SRC-2 | CONFIRMÉ |
| FCT-spv-006 | Le Luxembourg gère son RBE via le Luxembourg Business Registers (LBR, IRE) depuis le 1/03/2019 (loi du 13/01/2019) ; l'accès public au RBE est en réalité RESTREINT depuis l'arrêt de la CJUE du 22/11/2022 (C-37/20 et C-601/20) qui a jugé la publicité totale contraire au RGPD, y compris pour le registre luxembourgeois | SRC-3 | PARTIEL (statut d'accès à vérifier au cas par cas) |
| FCT-spv-007 | BORIS est l'outil européen reliant les registres centraux nationaux de bénéficiaires effectifs (point d'entrée unique pour la consultation inter-régistres) | SRC-3 | CONFIRMÉ |
| FCT-spv-008 | Le cas « PARC EOLIEN DE MOULINS HOLDINGS » apparaît aussi sur societe.com : holding à Strasbourg, CA 0 €, activité holdings | SRC-1 | CONFIRMÉ |
| FCT-spv-009 | Aucune donnée agrégée publique ne relie les SPV ENR à leurs propriétaires finaux (pas de base « propriété des parcs ENR » en open data) | SRC-2, SRC-4 | CONSTAT D'ABSENCE |
| FCT-spv-010 | L'API RNE INPI (registre-national-entreprises.inpi.fr/api/search) a renvoyé une réponse minimale (139 octets) sans champ RBE : probablement une erreur de requête ou une non-exposition du RBE dans la réponse de recherche ; à re-tester avec la route exacte | SRC-5 | CONSTAT TECHNIQUE (à re-tester) |
| FCT-spv-011 | data.inpi.fr bloque les requêtes scriptées (Cloudflare « Attention Required ») : l'exploitation à la volée est limitée à la navigation | SRC-5 | CONSTAT TECHNIQUE |
| FCT-spv-012 | La mention « EIH S.à.r.l. (Enbridge et CPP Investments) » dans les consortiums éoliens en mer montre l'usage de structures luxembourgeoises (S.à.r.l.) dans les parcs français | SRC-6 | CONFIRMÉ |

## 3. ANALYSE

### 3.1 La chaîne d'accès à la propriété réelle (méthode)

1. Identifier la SPV (SIREN via recensement des parcs, registres DECP, presse, ou registre des installations).
2. Consulter le RBE INPI sur data.inpi.fr (gratuit, par société) : bénéficiaires effectifs déclarés en France.
3. Si la SPV est détenue par une holding étrangère (Luxembourg, Pays-Bas, etc.) : consulter le RBE du pays (LBR pour le Luxembourg ; Kamer van Koophandel pour les Pays-Bas). ATTENTION : depuis l'arrêt CJUE du 22/11/2022 (C-37/20, C-601/20), l'accès public aux registres de bénéficiaires effectifs est restreint (intérêt légitime à démontrer) : l'accès luxembourgeois n'est plus inconditionnel, contrairement à l'hypothèse initiale. Ce point durcit la friction documentaire.
4. Remonter les niveaux jusqu'à la personne physique ou l'actionnaire de contrôle.

### 3.2 Le cas test : Moulins, un signal de « structure coquille » ?

Le profil de PARC EOLIEN DE MOULINS HOLDINGS (capital 10 €, CA nul, résultats négatifs sur 4 ans, holding strasbourgeoise) est typique d'une **holding de portage** : elle ne produit rien, elle détient. Le nom suggère un parc éolien à Moulins (lieu-dit ou commune). Deux lectures possibles :
- Lecture A (banale) : holding familiale ou locale de portage de parts d'un parc existant (montage fiscal courant, non illégal).
- Lecture B (à vérifier) : chaîne de détention aboutissant à un acteur non identifié (investisseur financier, fonds, personne liée) via une ou des holdings.

La recherche ciblée (nom + dirigeants Bhogal/Zhou/Beaumont) n'a rien donné en sources ouvertes : **aucune publication reliant ces noms à un groupe ENR connu**. C'est un signal faible mais réel : les 3 dirigeants n'apparaissent dans aucune fiche publique de promoteur éolien français (Valorem, Neoen, Engie, EDF, Boralex, etc.).

### 3.3 Le levier systémique

Le point le plus rentable n'est pas le cas Moulins (isolé), c'est la **carte des chaînes de détention des parcs soutenus par l'État** : pour chaque parc ayant un contrat de complément de rémunération ou une obligation d'achat, qui est le bénéficiaire effectif ? Cette carte existe potentiellement dans les registres CRE (les contrats mentionnent les SPV) et dans le RBE, mais nulle part elle n'est agrégée. Un rapprochement « liste des SPV bénéficiant d'un contrat de soutien (CRE) » × « RBE (INPI) » produirait la première cartographie publique de la propriété des parcs ENR français.

## 4. SOURCES

- SRC-1 : https://www.pappers.fr/entreprise/parc-eolien-de-moulins-holdings-821148830 (fiche complète, lue 17:40) + societe.com (extraits DDG)
- SRC-2 : https://data.inpi.fr (documentation du RBE, consultation des bénéficiaires effectifs) ; page RBE consultée via jina
- SRC-3 : https://ire.lu/fr/registre-beneficiaires-effectifs/ et guichet.public.lu (LBR, RBE Luxembourg, BORIS) ; extraits DDG
- SRC-4 : https://www.inpi.fr (communication sur le RBE et l'open data)
- SRC-5 : tests API : registre-national-entreprises.inpi.fr/api/search (réponse 139 octets, sans RBE) et data.inpi.fr/api/v2/companies (bloqué Cloudflare)
- SRC-6 : https://www.eoliennesenmer.fr (pages parcs : mention EIH S.à.r.l. Luxembourg dans les consortiums Saint-Nazaire, Fécamp, Courseulles)

Artefacts /tmp : pappers_moulins.html, pappers_m2.txt, inpi_moulins.txt, inpi2.json, rne_moulins.json, jina_spv.txt, moulins_qui.txt.

## 5. GAP ET PROCHAINES ÉTAPES

1. **GAP-1 (à faire)** : consulter le RBE INPI pour PARC EOLIEN DE MOULINS HOLDINGS (navigation manuelle data.inpi.fr, onglet « bénéficiaires effectifs ») : identifier les bénéficiaires déclarés et la chaîne. Pour les niveaux luxembourgeois : vérifier la procédure d'accès post-CJUE 2022 (intérêt légitime).
2. **GAP-2 (à faire)** : chercher le parc éolien « Moulins » lui-même (localisation, promoteur, contrat de soutien) pour comprendre à quel actif la holding est adossée : si le parc est détenu par un grand groupe, la holding est un maillon intermédiaire ; si le parc est détenu par des personnes physiques, le profil change.
3. **GAP-3 (à faire, rentabilité forte)** : construire la carte « SPV × contrats de soutien CRE × RBE » sur un échantillon de 10 parcs (5 éoliens + 5 solaires, choisis dans des zones où la concentration est documentée). C'est la méthode qui transforme la friction en cartographie.
4. **GAP-4 (leçon pour le protocole)** : documenter dans le playbook d'accès aux données que le RBE INPI est consultable par page web (navigation), que data.inpi.fr bloque le scraping (Cloudflare), et que le RBE luxembourgeois est public. Alternative : demandes d'extraction via l'API officielle INPI si accessible (compte).

## 6. CONCLUSION

Le volet SPV est **actionnable mais coûteux** : la donnée de propriété réelle existe (RBE), mais sa collecte est nominative et résiste aux scripts. Le cas test Moulins (holding 10 €, CA nul, dirigeants hors des radars des promoteurs connus) est un **signal faible de structure de portage à identifier**, pas une preuve de quoi que ce soit. La rentabilité est dans la carte agrégée (GAP-3), pas dans le cas isolé.
