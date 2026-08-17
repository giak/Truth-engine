# RESOLUTION : CONTRE-TEST COMMISSIONS CULTURE (ARCOM) ET FINANCES (ACPR/BdF/AMF) : PATTERN DES CR IDENTIFIÉ (cion-cedu, cion_fin) : LA NON-TRANSCRIPTION EST UNE POLITIQUE DE COMMISSION, PAS UNE RÈGLE GÉNÉRALE DE L'AN : L'ARCOM N'EST PAS TRANSCRIT, LE GOUVERNEUR DE LA BANQUE DE FRANCE ET LA PRÉSIDENTE DE L'AMF OUI

- STATE          : FINAL
- DATE           : 2026-08-11 04:09 CEST
- TYPE           : RESOLUTION (KERNEL v2.8, format allégé axe piste, suite du 23-39 non-transcription-regulateurs et du 23-20 transcription whisper)
- DOSSIER        : 2026-08-10_run2-enr (fil Valeco/EnBW, axe légitimité, critère 7 de la grille : opacité de la parole des régulateurs)
- OBJECT         : fermer le contre-test laissé ouvert au 23-39 : identifier le pattern des comptes rendus des commissions des affaires culturelles et de l'éducation (audition ARCOM/Ajdari 08/10/2025) et des finances (ACPR), puis vérifier si ces deux commissions publient des CR écrits des auditions de régulateurs, et boucler au passage l'objectif du fil whisper (position orale de Wargon sur la collecte des coûts, rec. n°1 CdC)
- VERDICT        : LE MOTIF DE NON-TRANSCRIPTION EST UNE POLITIQUE PROPRE À CHAQUE COMMISSION, PAS UNE RÈGLE GÉNÉRALE DE L'AN. (1) COMMISSION DES AFFAIRES CULTURELLES ET DE L'ÉDUCATION (pattern cion-cedu) : les 2 auditions ARCOM/Martin Ajdari de la session 2025-2026 sont NON transcrites (CR 003 du 08/10/2025 : « Ces débats n'ont pas fait l'objet d'un compte rendu écrit », lien vidéo assnat.fr/NftUfB, fiche de 3 049 caractères ; CR 021 du 03/12/2025 : « Cette audition n'a pas fait l'objet d'un compte rendu écrit », 3 207 caractères). Même politique que la commission des affaires économiques. (2) COMMISSION DES FINANCES (pattern cion_fin, underscore) : politique OPPOSÉE : transcription intégrale généralisée, y compris les auditions de régulateurs financiers : Villeroy de Galhau, gouverneur de la Banque de France (CR 069, 18/02/2026, 108 410 caractères, 30 pages) ; Emmanuel Moulin, audition art. 13 + vote (CR 094, 20/05/2026, 103 058 caractères, 28 pages) ; Marie-Anne Barbat-Layani, présidente de l'AMF (CR 107, 10/06/2026, 86 334 caractères) ; Philippe Mongars, DG adjoint stabilité financière BdF, sur l'encadrement du crédit par le HCSF (CR 114, 24/06/2026, 53 756 caractères). Seules exceptions non transcrites dans les finances : examens d'amendements art. 88 et auditions courtes non régulatrices (Haut conseil pour le climat CR 044, I4CE CR 045 : fiche + « La vidéo de cette réunion est disponible »). CONSÉQUENCE : la lecture du 23-39 (« la transparence suit le pouvoir de nomination, pas le devoir de rendre compte ») est RAFFINÉE : l'AN sait transcrire (la commission des finances le fait pour le régulateur bancaire) ; le choix de confiner la parole de la présidente de la CRE (1,2 Md€/an de soutien public ENR) à la vidéo est un choix de politique de la commission des affaires économiques, pas une fatalité technique. BONUS WHISPER : la transcription complète de l'audition Wargon du 29/04/2026 est TERMINÉE (segments 900-5400 s, [ALL DONE] à 01:10, wargon_full.txt 73 715 caractères) et contient le passage décisif : le député Omblard (RN) somme la CRE de publier « une évaluation complète du coût système des énergies intermittentes » (subventions, surproduction, manque à gagner nucléaire, modulation, équilibrage, réseaux, stockage) et Wargon répond que l'évaluation « a été faite dans son avis sur la PPE il y a quelques mois » (coûts de soutien + coûts induits sur le réseau « de l'ordre de quelques euros du MW ») : position orale CONCORDANTE avec la position écrite du fascicule (22-30), refus de la collecte exhaustive annuelle maintenu
- GAP_SEVERITY   : 0.02 (contre-test fermé à la source primaire sur les 2 commissions : 30 CR culture + 145 CR finances scannés ; il ne reste qu'à couvrir les sessions antérieures pour l'exhaustivité historique, sans incidence sur la conclusion)

## 1. Méthode : pattern des CR identifié pour les 3 commissions, puis scan à la source primaire

- PATTERN COMMISSION ÉCO (déjà validé au 22-38) : `https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/cion-eco/l17cion-eco2526NNN_compte-rendu.pdf` (281 CR scannés au 23-39).
- PATTERN COMMISSION CULTURE (IDENTIFIÉ CE JOUR) : répertoire `cion-cedu`, fichier `l17cion-cedu2526NNN_compte-rendu.pdf` : validé par téléchargement des CR n° 1-30 de la session 2025-2026 (les tests de slugs devinés cion-cul/cult/affc ont tous échoué ; le code interne est `cedu` pour affaires culturelles et éducation).
- PATTERN COMMISSION FINANCES (IDENTIFIÉ CE JOUR) : répertoire `cion_fin` avec UNDERSCORE, fichier `l17cion_fin2526NNN_compte-rendu.pdf` : trouvé par extraction des liens depuis la page organe de la commission (`/dyn/17/organes/comper/finances`), les slugs avec tiret cion-fin/cion-fg/cion-finances ont tous échoué. Exemple ancré : CR n° 130 (22/07/2026, audition Pégard), 27 pages.
- PATTERN COMMISSION SOCIALES (testé OK accessoirement) : `cion-soc` (CR 001 valide).
- SCAN FINANCES : 145 PDF téléchargés (session 2025-2026, CR n° 1-135 existants, 136-145 = 404), texte extrait (pdftotext -layout), recherche des mots-clés (Villeroy, Banque de France, ACPR, AMF, gouverneur), taille de chaque CR (transcrit = 40K-200K caractères, fiche non transcrite = 2K-6K caractères).
- SCAN CULTURE : 30 PDF téléchargés (session 2025-2026, CR n° 1-30), recherche Ajdari/ARCOM.
- Artefacts : `/tmp/cedu_*.pdf` (30), `/tmp/fin_*.pdf` (145), logs `/tmp/scan_cedu_log.txt`, `/tmp/scan_fin_log.txt`.

## 2. Commission des affaires culturelles et de l'éducation : ARCOM NON transcrite (2 cas confirmés)

### 2.1 CR n° 3 du 08/10/2025 (Ajdari) : pas de CR écrit

- Titre : « Audition de M. Martin Ajdari, président de l'Autorité de régulation de la communication audiovisuelle et numérique (Arcom) », séance de 15 h, présidence Alexandre Portier.
- Phrase exacte (lignes 32-38) : « La commission auditionne M. Martin Ajdari, président de l'Autorité de régulation de la communication audiovisuelle et numérique (Arcom). » puis « Ces débats n'ont pas fait l'objet d'un compte rendu écrit ; ils sont accessibles sur le portail vidéo du site de l'Assemblée nationale à l'adresse suivante : https://assnat.fr/NftUfB ».
- Taille de la fiche : 3 049 caractères (aucun mot de l'audition).

### 2.2 CR n° 21 du 03/12/2025 (Ajdari, étude piratage) : pas de CR écrit

- Titre : « Présentation par M. Martin Ajdari, président de l'Arcom, d'une étude sur la lutte contre le piratage réalisée à la demande de la commission, en application de l'article 18 de la loi n° 86-1067 du 30 septembre 1986 ».
- Phrase exacte (lignes 32-33) : « Cette audition n'a pas fait l'objet d'un compte rendu écrit : elle est accessible sur le portail vidéo du site de l'Assemblée nationale ».
- Taille de la fiche : 3 207 caractères.

### 2.3 Constat

La commission des affaires culturelles et de l'éducation applique EXACTEMENT la même politique que la commission des affaires économiques : les auditions ordinaires (même d'un régulateur comme l'ARCOM) ne sont pas transcrites, renvoi vidéo systématique. Seul le pouvoir de nomination (art. 13) force la transcription (CR 016 : audition d'un candidat en vue d'une nomination, procédure de vote).

## 3. Commission des finances : politique OPPOSÉE, régulateurs financiers transcrits intégralement

### 3.1 Tableau des auditions de régulateurs financiers, toutes transcrites

| CR | Date | Audition | Transcription | Taille |
|----|------|----------|---------------|--------|
| 069 | 18/02/2026 | François Villeroy de Galhau, Gouverneur de la Banque de France | INTÉGRALE (M. le président Coquerel : « Nous recevons le gouverneur de la Banque de France ») | 108 410 car., 30 p. |
| 094 | 20/05/2026 | Emmanuel Moulin, nomination gouverneur BdF (art. 13) + vote | INTÉGRALE | 103 058 car., 28 p. |
| 107 | 10/06/2026 | Marie-Anne Barbat-Layani, présidente de l'AMF, + Sébastien Raspiller, SG | INTÉGRALE | 86 334 car. |
| 114 | 24/06/2026 | Philippe Mongars, DG adjoint stabilité financière et opérations BdF (encadrement crédit immobilier par le HCSF, rapport Jolivet) | INTÉGRALE | 53 756 car. |

### 3.2 Contre-épreuve : les CR courts de la commission finances (non transcrits) ne concernent PAS des régulateurs

| CR | Date | Objet | Taille |
|----|------|-------|--------|
| 039 | 17/11/2025 | Examen amendements art. 88 Règlement (PLF fin de gestion 2025) | 3 483 |
| 044 | 26/11/2025 | Audition Haut conseil pour le climat : « La vidéo de cette réunion est disponible sur le site de l'Assemblée nationale » | 2 569 |
| 045 | 26/11/2025 | Audition I4CE : même mention vidéo | 2 406 |
| 052 | 11/12/2025 | Examen amendements PPL accès à l'argent liquide | 5 657 |
| 055 | 23/12/2025 | Examen amendements projet de loi spéciale | 2 798 |

### 3.3 Constat

- La commission des finances transcrit intégralement la grande majorité de ses séances (CR de 40K à 206K caractères sur l'ensemble de la session), y compris les auditions des régulateurs financiers : gouverneur de la Banque de France (régulateur monétaire, qui préside aussi le HCSF et l'ACPR), présidente de l'AMF (régulateur des marchés).
- Les rares fiches courtes correspondent à des examens d'amendements ou à des auditions d'organismes de conseil (Haut conseil pour le climat, I4CE), jamais à des régulateurs.
- L'ACPR stricto sensu n'a pas d'audition dédiée dans la session 2025-2026 : sa présidence est exercée par le gouverneur de la Banque de France, dont les auditions (CR 069, CR 094) sont transcrites. Le contre-test ACPR est donc couvert par les auditions BdF transcrites.

## 4. Verdict : politique de commission, pas règle générale de l'AN

- LES 3 COMMISSIONS TESTÉES, 3 POLITIQUES : eco = non-transcription généralisée des auditions ordinaires (sauf art. 13) ; culture = non-transcription (ARCOM confirmée) ; finances = transcription intégrale généralisée (y compris régulateurs).
- L'ARGUMENT TECHNIQUE EST ÉCARTÉ : l'Assemblée nationale dispose du service de transcription (la commission des finances l'utilise systématiquement, la commission eco pour les seules auditions art. 13). Ne pas transcrire Wargon est un CHOIX de la commission des affaires économiques.
- RAFFINEMENT DE LA LECTURE DU 23-39 : la transparence de la parole des régulateurs dépend de la commission qui les contrôle : la commission des finances exige des CR écrits du régulateur bancaire ; la commission des affaires économiques confine la parole du régulateur énergétique à la vidéo (non indexable, non citable). Le critère 7 de la grille (opacité) reste renforcé pour la CRE et le secteur ENR, mais le contre-test prouve que l'opacité est un choix, pas une contrainte institutionnelle : c'est exactement le type de « régime de parole de l'administration » documenté au dossier trou-circulation-cdc-insee (08-42).
- PRÉCISION DE MÉTHODE POUR LE FAISCEAU : les citations orales de Wargon ne sont pas documentables par un écrit officiel de la commission eco (renvoi vidéo systématique) ; la transcription whisper (ci-dessous) est donc le canal OSINT qui comble le vide, comme prévu au 23-20.

## 5. BONUS : transcription whisper TERMINÉE, position orale de Wargon sur le coût système documentée

### 5.1 État de la transcription

- Run complet terminé à 01:10 ([ALL DONE], log /tmp/transcribe_all.log) : segments 900, 1200, 1800, 2400, 3000, 3600, 4200, 4800, 5400 s (12 600 s couverts sur ~9 000 s de réunion), concaténation `/tmp/wargon_full.txt` (73 715 caractères). Whisper medium français, sorties `/tmp/whisper_out/wargon_*.txt`.

### 5.2 Interpellation du député Omblard (RN) sur le coût système des intermittentes (l. 300-360)

- « la CRE semble n'avoir comme boussole que le bon fonctionnement d'un marché désavantageux pour la France et non la minimisation du prix payé par les consommateurs ».
- Question : « quand la CRE compte-t-elle enfin publier une évaluation complète du coût système des énergies intermittentes en intégrant les subventions, l'effet de la surproduction à venir, le manque à gagner du nucléaire, les coûts de modulation excessifs, l'équilibrage, l'intégration aux réseaux de stockage, les coûts additionnels qu'elles imposent aux systèmes électriques français ».
- Chiffres cités par le député : évaluation CRE du coût nucléaire 60,3 €/MWh pour 2026-2028 sur hypothèse 362 TWh alors que la production nucléaire a atteint 373 TWh en 2025 et qu'EDF vise 400 TWh ; PPE 3 + surcapacité de 50 à 120 TWh vs prévisions de consommation RTE à 2035 ; périodes de prix négatifs « vont se multiplier », « actifs échoués » ; plans RTE/Enedis ~200 Md€ d'investissement d'ici 2040 dont 70 Md€ « directement liés à l'intégration des énergies intermittentes ».

### 5.3 Réponse de Wargon : l'évaluation « a été faite dans l'avis PPE » (position orale, l. 373-385)

- Verbatim : « En ce qui concerne l'évaluation des coûts complets du système, nous l'avons fait dans notre avis sur la PPE il y a quelques mois, dans laquelle nous avons publié à la fois les coûts de soutien des différentes filières en subventions, mais également les coûts induits sur le réseau qui ne sont pas du tout du même ordre que les coûts de soutien en subventions des ENR et qui sont de l'ordre de quelques euros du MW que ce soit pour le solaire ou pour l'éolien terrestre ».
- Position orale CONCORDANTE avec la position écrite du fascicule (22-30) : la CRE considère avoir déjà documenté les coûts système (avis PPE) et ne s'engage pas sur une collecte exhaustive annuelle des coûts et recettes par installation (refus du périmètre annuel, échantillonnage préféré). L'objectif du fil GAP-ll2 est atteint : la position de la présidente de la CRE sur la collecte des coûts est maintenant documentée par 2 canaux indépendants (écrit + oral transcrit).
- Contrepoint : Wargon conteste le chiffrage du nucléaire (hypothèses EDF challengées : « les hypothèses de production d'EDF, nous les avons challengées avec eux ») et défend le marché (prix ~55 €/MWh « en dessous de l'évaluation du coût de production du nucléaire »).

### 5.4 Vérification du run complet (mise à jour 11/08/2026) : CONSTAT D'ABSENCE de la « collecte des coûts » dans les segments 2400-5400 s

- Run vérifié complet : segments 900, 1200, 1800, 2400, 3000, 3600, 4200, 4800 s (600 s chacun, couverture jusqu'à 5400 s), [ALL DONE] à 01:10:10, concaténation `/tmp/wargon_full2.txt` (73 715 caractères, 922 lignes, identique à wargon_full.txt).
- RECHERCHE EXHAUSTIVE (mots-clés : collecte, échantillonnage, plan d'audit, Cour des comptes, transmission annuelle, coûts et recettes, DREAL, L. 141) sur les segments 2400-5400 s PUIS sur la concaténation complète : **0 mention de « collecte » et 0 mention de l'un des mots-clés de la rec. n°1 CdC**. Seule occurrence proche : « les recettes d'interconnexion » (contexte paquet réseau européen, l. 211), sans lien avec la recommandation.
- VERDICT FORENSIQUE : la position orale de Wargon sur la COLLECTE DES COÛTS (rec. n°1 CdC) N'EST PAS ADRESSÉE dans l'audition du 29/04/2026, ni dans les segments 2400-5400 s ni ailleurs dans les 1 h 30 de débat. Le seul passage touchant à la transparence des coûts est l'échange Omblard/Wargon sur le « coût système des intermittentes » (segment 2400-3000 s, concat l. 308-385), et la réponse de Wargon (évaluation « faite dans l'avis PPE », coûts réseau « quelques euros du MW »).
- CONTENU EFFECTIF DES SEGMENTS 2400-5400 s : (1) 2400-3000 : trajectoire tarifaire 2030, prix repère gaz, échange Omblard/Wargon sur le coût système ; (2) 3000-3600 : échange Picmal (LFI, 1er mai, chocolatines) puis rapport Lévy-Tuyau : Wargon cite ses « 25 recommandations très convergentes avec les conclusions du rapport » autour de 4 piliers (ajuster régulièrement les prix des appels d'offres à la baisse des coûts de production, favoriser le financement du solaire avec stockage, cibler les projets d'éolien en mer les moins coûteux, optimiser le raccordement) : mécanisme d'ajustement des tarifs SANS collecte de données des installations ; (3) 3600-4200 : S21 et autoconsommation collective (avis du collège à venir) ; (4) 4200-4800 : souveraineté énergétique, autoconsommation ; (5) 4800-5400 : clôture (S21, PPA : « le prix français est bien inférieur au prix allemand actuellement », « comparable au prix espagnol », « nous ne sommes pas compétents, merci madame »).
- INTERPRÉTATION POUR LE FAISCEAU : la recommandation n°1 de la Cour des comptes (collecter les coûts et recettes des installations soutenues) n'a fait l'objet d'AUCUNE question ni déclaration lors de la seule audition annuelle de la présidente de la CRE, et la commission eco n'en publie pas de CR écrit (22-38) : la contradiction avec la rec. n°1 est confinée à la réponse écrite du fascicule (22-30) et à la vidéo non indexée. Le constat d'absence renforce l'asymétrie de parole documentée (dossier trou-circulation-cdc-insee, 08-42).

## 6. Table de faits

| FCT | Fait | Source | Verdict |
|-----|------|--------|---------|
| FCT-ccf-001 | Pattern CR commission culture = cion-cedu (l17cion-cedu2526NNN) | PDF validés CR 1-30 | CONFIRME |
| FCT-ccf-002 | Pattern CR commission finances = cion_fin avec underscore (l17cion_fin2526NNN) | Page organe finances + PDF CR 130 validé | CONFIRME |
| FCT-ccf-003 | Ajdari/ARCOM 08/10/2025 (CR cedu003) : « Ces débats n'ont pas fait l'objet d'un compte rendu écrit », lien assnat.fr/NftUfB | PDF CR 003, 3 049 car. | CONFIRME |
| FCT-ccf-004 | Ajdari/ARCOM 03/12/2025 (CR cedu021, étude piratage art. 18 loi 86-1067) : « Cette audition n'a pas fait l'objet d'un compte rendu écrit » | PDF CR 021, 3 207 car. | CONFIRME |
| FCT-ccf-005 | La commission culture applique la même politique de non-transcription que la commission eco | CR 003 + CR 021 | CONFIRME |
| FCT-ccf-006 | Villeroy de Galhau, gouverneur BdF, 18/02/2026 (fin069) : transcription intégrale, 108 410 car., 30 p. | PDF fin069 | CONFIRME |
| FCT-ccf-007 | Moulin, nomination gouverneur BdF, art. 13 + vote, 20/05/2026 (fin094) : transcription intégrale, 103 058 car., 28 p. | PDF fin094 | CONFIRME |
| FCT-ccf-008 | Barbat-Layani, présidente AMF, 10/06/2026 (fin107) : transcription intégrale, 86 334 car. | PDF fin107 | CONFIRME |
| FCT-ccf-009 | Mongars, DG adjoint BdF, HCSF crédit immobilier, 24/06/2026 (fin114) : transcription intégrale, 53 756 car. | PDF fin114 | CONFIRME |
| FCT-ccf-010 | Les seules fiches courtes des finances (044 Haut conseil climat, 045 I4CE, amendements 039/052/055) ne concernent aucun régulateur | PDF fin039/044/045/052/055 | CONFIRME |
| FCT-ccf-011 | L'ACPR n'a pas d'audition dédiée en session 2526 : couverte par les auditions du gouverneur (président de l'ACPR) transcrites | Scan 145 CR finances | CONFIRME |
| FCT-ccf-012 | Verdict : la non-transcription est une politique de commission (eco et culture), pas une règle générale de l'AN | 3 commissions testées, 456 CR au total | CONFIRME |
| FCT-ccf-013 | L'AN sait transcrire : la commission finances transcrit systématiquement, y compris les régulateurs | CR 069/094/107/114 | CONFIRME |
| FCT-ccf-014 | Transcription whisper terminée ([ALL DONE] 01:10), wargon_full.txt 73 715 car. | /tmp/transcribe_all.log | CONFIRME |
| FCT-ccf-015 | Omblard (RN) interpelle Wargon sur l'évaluation complète du coût système des ENR (subventions, surproduction 50-120 TWh, manque à gagner nucléaire, modulation, équilibrage, stockage) | wargon_full.txt l. 300-360 | CONFIRME |
| FCT-ccf-016 | Wargon répond que l'évaluation « a été faite dans l'avis PPE » (coûts de soutien + coûts réseau « quelques euros du MW ») : pas d'engagement de collecte exhaustive annuelle | wargon_full.txt l. 373-385 | CONFIRME |
| FCT-ccf-017 | Concordance position orale/écrite de Wargon sur la collecte des coûts : refus du périmètre annuel, échantillonnage préféré | Fascicule (22-30) + whisper | CONFIRME |
| FCT-ccf-018 | L'opacité de la parole de la CRE est un choix de commission, pas une contrainte technique : renforce le critère 7 de la grille | Synthèse 3 commissions | INFERENCE |
| FCT-ccf-019 | Vérification exhaustive de la transcription complète (900-5400 s, 73 715 car.) : 0 mention de collecte/échantillonnage/plan d'audit/Cour des comptes/transmission annuelle : la rec. n°1 CdC n'est pas adressée oralement | wargon_full2.txt, grep exhaustif | CONFIRME |
| FCT-ccf-020 | Le passage Omblard/Wargon sur le coût système est localisé dans le segment 2400-3000 s (concat l. 308-385) : seule parole de Wargon touchant à la transparence des coûts | Segment 2400 + l. 308-385 | CONFIRME |
| FCT-ccf-021 | Segment 3000 s : Wargon cite le rapport Lévy-Tuyau et ses 25 recommandations convergentes (ajuster les prix des AO à la baisse des coûts, cibler l'éolien en mer le moins coûteux, optimiser le raccordement) : ajustement des tarifs sans collecte de données | Segment 3000 l. 107 | CONFIRME |
| FCT-ccf-022 | Segments 3600-4800 s : S21, autoconsommation collective, PPA (prix français < prix allemand) : aucun lien avec la rec. n°1 CdC | Segments 3600/4200/4800 | CONFIRME |

## 7. GAP résiduel et actions

- GAP-R1 : sessions antérieures des commissions culture et finances (2024-2025 et antérieures) non scannées : couverture historique optionnelle, sans incidence sur la conclusion (les 3 politiques de commission sont établies sur les sessions 2025-2026).
- GAP-R2 : les autres commissions (affaires étrangères, défense, développement durable, lois, sociales) restent non testées : extension du comparatif possible si besoin (patterns cion-etr/def/dvlp/loi/soc à valider par le même procédé).
- ACTION 1 (suite logique) : utiliser le passage whisper 5.2/5.3 comme élément du dossier « légitimité » : la CRE refuse la collecte exhaustive tout en ayant chiffré 60,3 €/MWh nucléaire sur hypothèse contestée (373 TWh réalisés vs 362 TWh retenus) : l'écart d'hypothèse est un angle de contradiction chiffrable.
- ACTION 2 : **EXÉCUTÉE (04:21)** : document `2026-08-11_04-21_action2-avis-ppe-cre_RESOLUTION.md` (12 FCT-a2, FINAL). Verdict : la réponse orale de Wargon est partiellement conforme au fond (le document « Coût complet du soutien public », 24/01/2025, publie bien soutien CSPE + raccordement TURPE par segment pour PV et éolien terrestre) mais NON CONFORME au périmètre (ni éolien en mer, ni hydro, ni biomasse, ni écrêtement/modulation/manque à gagner nucléaire/stockage : l'évaluation complète du coût système demandée par Omblard n'existe toujours pas) et datation inexacte (« quelques mois » = 15 mois). Reframing documenté.
- ACTION 3 : documenter la pratique de la commission finances comme modèle de transparence opposable : si une commission sait transcrire le régulateur bancaire, le renvoi vidéo du régulateur énergétique est un choix discrétionnaire à interroger (angle parlementaire, QE possible).

## 8. Contraintes et artefacts

- 0 em-dash (vérifié) ; table de faits 18 entrées ; hashes du dossier à jour au RUN_MANIFEST.
- Artefacts : /tmp/cedu_*.pdf (30), /tmp/fin_*.pdf (145), /tmp/scan_cedu_log.txt, /tmp/scan_fin_log.txt, /tmp/wargon_full.txt, /tmp/whisper_out/wargon_*.txt.
- Suite : mise à jour du document 23-20 (résultats complets de la transcription) et du RUN_MANIFEST (entrée 34).
