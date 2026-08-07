# AUDIT ANTAGONISTE : « L'ingérence sans mesure » (2026-08-06_22-08_ingerence-sans-mesure_ARTICLE.md)

> **Audit** : 2026-08-07_04-27 CEST
> **Cible** : `articles/2026-08-06_22-08_ingerence-sans-mesure_ARTICLE.md`
> **Méthode** : lecture intégrale de l'article, croisement systématique avec les 15 investigations du dossier ICEBERG (sources primaires internes), et vérification indépendante par recherche web des claims externes (ARCOM, HATVP, Cour des comptes, Viginum, EMIF, EU DisinfoLab, Check First, loi 2024-850, référé 2018, date présidentielle, communiqué Soulard/Heitz, Fawn Mianju, BlackCore).
> **Règle** : vérifier chaque chiffre, chaque citation, chaque source. Lister les échecs numérotés. Honnêteté forensique : un fait contredit par le dossier interne ou par une source primaire est un échec, quelle que soit la beauté de la phrase.

---

## §1. Bilan d'ensemble

**19 échecs numérotés, dont 6 majeurs.** La thèse centrale (vide quantitatif DSA, asymétrie 2017/2026, non-neutralité structurelle) tient : elle repose sur des données primaires vérifiées (DSA, avis du Conseil d'État, textes de loi). Mais **deux échecs majeurs inversent le sens de la preuve** (EMIF, composition ARCOM) et **deux autres falsifient des données** (codes HTTP lus comme des entrées, référé 2018 « zéro usage »). L'article ne doit pas être publié en l'état.

---

## §2. ÉCHECS MAJEURS (erreurs factuelles, publiables = dégâts)

### E1. « l'EMIF ... est alimenté par la Commission à hauteur de 70 à 80 % » : FAUX, sens inversé

**Dans l'article (§7)** : « l'European Media and Information Fund (EMIF), qui subventionne les vérificateurs, est alimenté par la Commission à hauteur de 70 à 80 % ».

**Preuves** :
- Dossier Piste 3, P3F12 : EMIF géré par la Fondation Calouste Gulbenkian + Institut universitaire européen. **Financement initial : Google, 25 M€.** Comité sans membres de la Commission. Le « 70-80 % » désigne la part des fonds **versés à des organisations que l'UE cite comme « corroboration indépendante »** : c'est la destination, pas la source.
- Vérification web indépendante : EMIF ne reçoit pas de financement direct de la Commission ; contributeur inaugural Google (via Google News Initiative), 25 M€ ; multi-donateurs privés.

**Conséquence** : l'article affirme le contraire exact du dossier. Le point vrai du dossier (l'argent est PRIVÉ, Google, et va à des organisations alignées UE) devient « l'UE finance l'EMIF à 70-80 % ». C'est une inversion cause/effet qui affaiblit la thèse au lieu de la servir.

**Correction** : « l'EMIF, qui subventionne les vérificateurs, a été lancé avec 25 millions d'euros de Google, et 70 à 80 % de ses fonds vont à des organisations que l'UE cite comme corroboration indépendante ».

### E2. « référé administratif » / « juge administratif » : FAUX, c'est le juge judiciaire

**Dans l'article** : accroche « référé administratif permanent » ; §1 « Un référé devant le juge administratif » ; §5 « Le référé permanent est confié au juge administratif, corps d'État formé dans la même école que les hauts fonctionnaires, et non au juge judiciaire, dont l'indépendance vient de se manifester ».

**Preuve (dossier interne)** : Investigation D (lecture intégrale de l'avis du Conseil d'État du 16/07/2026, source primaire), fait D5 : « Le nouveau référé (art. 1) serait porté devant le président d'un **tribunal judiciaire spécialement désigné (juge des référés)** ». Le référé électoral 2018 (L.163-2) est judiciaire ; le nouveau référé permanent l'est aussi.

**Conséquence** : le §5 entier (« la loi contourne exactement ce qui vient de se briser... le référé permanent est confié au juge administratif et non au juge judiciaire ») repose sur une erreur factuelle. L'argument de contournement du juge judiciaire s'effondre tel qu'écrit. L'article contredit sa propre investigation D.

**Correction** : « référé devant le juge des référés du tribunal judiciaire », et le §5 doit être réécrit (le contournement passe par le blocage ARCOM sans juge et le contrôle postérieur à la contrainte, pas par un « juge administratif »).

### E3. « Un pouvoir de blocage confié à l'ARCOM : 48 heures ... sans aucune intervention du juge » attribué à la PPL 913 : FAUX, ce pouvoir date de 2024

**Dans l'article** : §1 (au titre de la PPL 913) « Un pouvoir de blocage confié à l'ARCOM : 48 heures pour ordonner le retrait, sans aucune intervention du juge » ; §4 « la loi n° 913 : le référé devient permanent, l'ARCOM gagne un pouvoir de blocage sans juge ».

**Preuves** :
- Piste 1, F15 : le blocage administratif ARCOM en 48 h sans autorisation judiciaire préalable existe depuis la **loi SREN 2024** (n° 2024-449) et le décret 2024-1255.
- Investigation D : les 3 articles de la PPL 913 sont (1) référé permanent, (2) extension du référé électoral à toutes les élections, (3) relèvement des peines. **Aucun pouvoir ARCOM n'y figure**.
- Incohérence interne de l'article : le §4 attribue aussi « le gel de contenus ... confié à l'ARCOM, avec blocage sous 48 heures » à la loi 2024-850. L'ARCOM ne peut pas « gagner » le même pouvoir en 2024 et en 2026.

**Correction** : dire que le blocage ARCOM 48 h sans juge **préexiste** (SREN 2024) et que la PPL 913 étend le référé judiciaire à toutes les élections. C'est l'extension d'un outil déjà existant, pas une nouveauté : la nuance sert la thèse, elle ne la dessert pas.

### E4. « le fichier du 12 juin contient 200 entrées, celui du 13 juin 403 » : FAUX, ce sont des codes HTTP

**Dans l'article** (§2) : « La frontière est exacte : le fichier du 12 juin contient 200 entrées, celui du 13 juin 403, et les mois suivants n'existent plus ».

**Preuve (dossier interne)** : Investigation A-v3, B2 : « 2026-06-12 = 200, 2026-06-13 = 403 » et REQUEST_LOG « HEAD/GET bucket : agrégats juin-juillet-août 403, daily raw 12/06=200 13/06=403 ». **200 et 403 sont les codes de statut HTTP** (200 = accessible, 403 = interdit). Ce ne sont pas des nombres d'entrées.

**Conséquence** : une erreur de lecture des données sources, écrite en toutes lettres. Un lecteur technique la repérera immédiatement, et le chiffre faux discrédite le reste de l'analyse DSA.

**Correction** : « le dernier agrégat quotidien publié est celui du 12 juin ; dès le 13 juin, les fichiers ne sont plus accessibles (erreur 403) ».

### E5. ARCOM « 9 membres nommés 3 par 3 » et « Neuf membres sur neuf désignés par des autorités politiques » : FAUX, c'est 7 sur 9

**Dans l'article** (§7) : « Le collège du régulateur de l'audiovisuel et du numérique compte 9 membres, nommés 3 par 3 par le président de la République, le président de l'Assemblée nationale et le président du Sénat ... Neuf membres sur neuf désignés par des autorités politiques ... Le corpus militant disait 7 sur 9 : la vérification sur le texte de loi corrige vers le haut. C'est 9 sur 9. »

**Preuves** :
- Article 4 de la loi 86-1067 (version en vigueur, LEGIARTI000044259313) : 9 membres, répartis ainsi : **1 nommé par le Président de la République (le président de l'autorité), 3 par le président de l'Assemblée nationale, 3 par le président du Sénat, 1 membre en activité du Conseil d'État désigné par le vice-président du CE, 1 membre de la Cour de cassation désigné par le premier président de la CdC**.
- Donc : **7 membres sur 9 désignés par des autorités politiques ; 2 désignés par les juridictions**.

**Conséquence** : l'article (et la vérification du REGISTRE) a « corrigé vers le haut » une information **exacte** du corpus (« 7 des 9 membres désignés par des instances politiques ») en une information **fausse** (« 3 par 3 », « 9 sur 9 »). La thèse §7 (non-neutralité) reste vraie, mais l'article la sur-affirme faussement, et la phrase de « correction » est elle-même l'erreur.

**Correction** : « 9 membres, dont 7 désignés par des autorités politiques (1 par le président de la République, 3 par le président de l'Assemblée nationale, 3 par le président du Sénat), 2 désignés par le Conseil d'État et la Cour de cassation ».

### E6. « Zéro usage en huit ans » du référé 2018 : FAUX, une saisine documentée (mai 2019)

**Dans l'article** : §4 « En huit ans, il n'a jamais été appliqué. Zéro usage documenté » ; §6 « (zéro usage en huit ans, confirmé par la source la plus officielle possible) » ; §7 « référé jamais utilisé ».

**Preuves** :
- Vérification web indépendante : **TGI Paris, 17 mai 2019, n° 19/53935**, Marie-Pierre Vieu et Pierre Ouzoulias c/ Twitter International et Christophe Castaner : première saisine du référé électoral de l'article L.163-2 (loi 2018-1202, art. 42), **demande rejetée** (conditions non réunies). Documentée par Legalis, Haas Avocats, Landot Avocats.
- Le Conseil d'État (D12) ne dit pas « zéro », il constate un « très faible recours ». La parenthèse « confirmé par la source la plus officielle possible » est fausse : le CE n'a jamais écrit « zéro ».

**Conséquence** : « zéro usage » (répété trois fois) est falsifié par la jurisprudence de mai 2019. Le dossier P1/P2 (« zéro jurisprudence trouvée ») avait raté ce cas ; l'article l'a propagé. La formulation exacte est : « un seul usage connu, une saisine de mai 2019 rejetée ».

**Correction** : remplacer les trois occurrences : « le référé n'a connu qu'un usage, rejeté (TGI Paris, 17 mai 2019), et le Conseil d'État constate son "très faible recours" ».

---

## §3. ÉCHECS MOYENS

### E7. « municipales de mai 2026 » (BlackCore) : le mois est faux

Article §3 : « ("BlackCore", visant des candidats de la gauche aux municipales de mai 2026) ». Vérification web : les élections municipales françaises de 2026 ont eu lieu les **15 et 22 mars 2026** ; BlackCore a visé des candidats LFI (Delogu, Piquemal, Guiraud). Le dossier P4F5 porte la même erreur (« mai 2026 ») ; l'article l'a propagée. **Correction** : « mars 2026 ».

### E8. « C'est le premier depuis 66 ans » (communiqué Soulard/Heitz) : non corroboré

Article §5. Le web confirme le communiqué du 25 juin 2026 et le qualifie « inédit », « exceptionnel », « choix inédit » (CSM, BFMTV, Europe 1) : mais **aucune source ne dit « 66 ans »**. Le dossier P4F8 formule « aucun précédent en 66 ans de Ve République », or la Ve République a **68 ans** en 2026 : incohérence arithmétique interne. Le « 66 ans » doit être sourcé ou retiré.

### E9. « tous adversaires ou concurrents de l'exécutif, aucun proche de la majorité présidentielle »

Article §3, à propos de Philippe, Glucksmann et Attal. **Attal est le patron de Renaissance, le parti du président** (cf. tweet AFP cité dans le dossier : « le candidat et patron de Renaissance »). La sélectivité est réelle pour Philippe et Glucksmann (rivaux de l'exécutif) ; l'inclure dans « aucun proche de la majorité présidentielle » est faux. **Correction** : « trois candidats désignés en six semaines, dont deux rivaux de l'exécutif et un héritier du camp présidentiel ».

### E10. « Viginum a documenté ... israéliennes ("BlackCore") »

Article §3. Fawn Mianju : attribué à Viginum (confirmé). BlackCore : documenté par la presse (Libération, Haaretz, HuffPost) et l'enquête judiciaire (« opérée depuis Israël ») ; **l'attribution par Viginum n'est pas documentée**. À nuancer : « Viginum a documenté le réseau chinois Fawn Mianju ; une campagne israélienne (BlackCore) a été documentée par la presse et la justice ».

### E11. « aucune opération n'a jamais été attribuée par Viginum aux États-Unis, au Qatar, aux Émirats, à l'Arabie saoudite ou à la Turquie »

Fait négatif, non documenté dans le dossier (P1 ne dit que « sous-documentées » pour les États-Unis ; les autres pays n'apparaissent nulle part). Un « jamais » exige une recherche spécifique qui n'a pas été conduite. Affirmation forte sans source. **Soit documenter, soit reformuler** (« aucune attribution publique n'est recensée dans le dossier »).

### E12. « La fenêtre sans données agrégées commence le 25 juin »

Article §2, après avoir écrit que la publication s'est arrêtée au 12 juin. La fenêtre commence donc le **13 juin**, pas le 25. L'article déplace le début de la fenêtre pour l'aligner sur le communiqué Soulard/Heitz : distorsion de datation interne. **Correction** : « la fenêtre sans données agrégées s'ouvre le 13 juin et traverse le communiqué du 25 juin, l'avis du 16 juillet et le dépôt du 22 juillet ».

### E13. « jusqu'à un triplement pour les infractions commises pendant les campagnes »

Article §1 et §4. Le triplement (D14/F12) porte les peines de l'art. L.97 du code électoral de 1 an/15 000 € à **3 ans/45 000 €**, avec circonstance aggravante « puissance étrangère » à 6 ans. L'infraction de L.97 est électorale par nature ; le triplement n'est pas un bonus « en campagne ». La formulation suggère un mécanisme inexistant, et **l'aggravante « puissance étrangère » à 6 ans, cœur de l'art. 3, est omise**. **Correction** : « les peines de l'infraction électorale sont triplées (jusqu'à 3 ans et 45 000 €), portées à 6 ans en cas d'ingérence étrangère ».

### E14. « Glucksmann a cité ce précédent comme un modèle souhaitable » (Roumanie)

Le transcript (Piste 4) documente que Glucksmann a évoqué le scénario roumain pour la présidentielle française ; **« modèle souhaitable » est une qualification non sourcée**. Reformuler : « a évoqué le précédent roumain pour la France ».

### E15. « EU DisinfoLab reçoit environ 46 % de son financement de fondations et de l'Union européenne »

Le 46,3 % est exact (P3F2 : OSF 23,9 % + UE 22,4 %), mais « fondations » est imprécis : c'est **Open Society Foundations** qui est comptée, et une autre fondation (Civitates, 12,5 %) ne l'est pas. **Correction** : « environ 46 % de financement d'Open Society Foundations et de l'Union européenne ».

---

## §4. ÉCHECS MINEURS

### E16. Citation inexacte : « aucune description de phénomènes d'abus non-étrangers observés »

Article §6, entre guillemets. Le texte exact de l'avis (D4) : « ne comporte aucune description de phénomènes relevant d'abus de la liberté de communication qui ne seraient pas d'origine étrangère et qui auraient été observés ». La version de l'article est un condensé présenté comme citation. Soit citer exactement, soit retirer les guillemets.

### E17. « à raison d'une couche par an en moyenne »

7 strates sur 8 ans avec des années vides (2019, 2022, 2023, 2025) et des années doubles (2024, 2026) : « une couche par an » est trompeur. Dire « sept strates en huit ans ».

### E18. Source décorative : Le Monde (sanctions ARCOM C8/CNews)

Citée dans les sources, jamais mobilisée dans le corps du texte. Soit l'utiliser (les sanctions ARCOM documentent la « fabrique des sanctions » du corpus), soit la retirer.

### E19. « environ 491 millions de décisions de modération par mois »

Le 491 M est le chiffre de mai 2026 (mémo DSA), généralisé aux trois mois. « Environ » atténue, mais la source ne couvre que mai. Préciser « en mai 2026 ».

---

## §5. Vérifications CONFORMES (qui passent l'audit)

| Élément | Statut | Preuve |
|:--|:--|:--|
| 542 déclarations « désinformation » sur 24 302 119 le 22/07 (0,002 %) | CONFORME | A-v3 B5, analyse locale validée |
| Zéro désinformation mondiale mars-avril-mai 2026 | CONFORME | Mémo DSA (agrégats) |
| 14 434 contenus électoraux/mois (0,003 %) ; 59 251 le 22/07 (0,24 %) | CONFORME | A-v3 B6, mémo |
| Amazon 55 %, Google Shopping 96 %, CGU 96,5 % | CONFORME | Mémo DSA, A-v3 B11 |
| Arrêt de publication des agrégats au 12 juin (hors « 200 entrées ») | CONFORME | A-v3 B2 |
| Viginum : 65 agents, 7,3 M€, créé par décret 13/07/2021 | CONFORME | Web (SGDSN, Sénat) + P1 F2, P2F1 |
| Loi 2024-850 : jamais contrôlée au fond, saisines irrecevables | CONFORME | Web : décisions 2024-870 DC (10/07/2024) et 2024-871 DC (24/07/2024) |
| Communiqué Soulard/Heitz, 25 juin 2026 | CONFORME | Web (CSM, BFMTV, Europe 1) |
| Fawn Mianju attribué par Viginum | CONFORME | Web (Le Monde, Atlantico) |
| Premier tour présidentielle 18 avril 2027 | CONFORME | Web (service-public.fr, vie-publique.fr) |
| HATVP 2024 : 751 saisines, 95,5 % compatibles, 74,3 % avec réserves | CONFORME | Web (rapport 2024) + REGISTRE |
| Cour des comptes : 260,9 M€ (programme 164, 2025), 76 % de suivi | CONFORME | REGISTRE (correction) + web |
| Conseil constitutionnel : annulation Habib, décision 2022-5773 AN du 03/02/2023 | CONFORME | Web |
| Check First : entreprise privée, Oy, Finlande | CONFORME | Web (Business ID 3143603-4) + P3F4 |
| EMFA jamais utilisé en France, « propaganda loophole » | CONFORME | P2F5, P2F12 |
| Citations de l'avis CE : « grave et imminent », « incertaine », « trop tard », « difficile », « très faible recours », « proportionné », « n'appelant pas de réserves », « ne méconnaissant pas », renommage « protection de la vie démocratique », « ne porte pas sur les seules ingérences étrangères » | CONFORME | D6-D13 (avis lu intégralement) |
| Roumanie : annulation 6 décembre 2024, Commission de Venise « dernier ressort » | CONFORME | CCR, Venise |
| Peines : 3 ans/45 000 €, aggravante 6 ans | CONFORME | D14, F12 (à corriger la formulation, E13) |
| 27 jours entre le 25 juin et le 22 juillet | CONFORME | Calcul exact |
| Débat Sénat 20 octobre 2026 | CONFORME | P2F9, dossier Sénat |

---

## §6. Claims non vérifiables / limites déclarées

1. **Attributions d'ingérence 2026 (unité 29155 pour Philippe, Storm-1516 pour Glucksmann, Matriochka pour Attal)** : fondées sur la presse et les tweets d'août 2026 (dossier P1F13, P4F6). Non vérifiables indépendamment par le web. Acceptables comme actualité datée, à garder attribuées à leurs sources.
2. **« Aucune attribution Viginum aux USA/Qatar/EAU/Arabie/Turquie »** : fait négatif non documenté (E11).
3. **Chiffres du corpus Twitter non audités** (posts 1-13 de l'extraction) : utilisés comme trame, pas comme preuve.
4. **Le « 66 ans »** (E8) : dossier interne uniquement, incohérent.

---

## §7. Verdict

**L'article ne doit pas être publié en l'état.** La thèse tient, mais elle est portée par 6 erreurs factuelles majeures, dont deux qui inversent le sens de la preuve (EMIF, ARCOM) et deux qui falsifient des données (codes HTTP, référé 2018). Le pattern est celui des cycles v7-v10 : le contenu forensique est bon, mais les sur-affirmations de la rédaction créent des angles d'attaque gratuits pour un contradicteur.

**Ordre de correction imposé avant publication** : E1, E2, E3, E4, E5, E6 (bloquants) → E7-E15 (à corriger dans la même passe) → E16-E19 (nettoyage). Après correction, refaire un grep des chiffres et des citations, puis un second passage antagoniste sur le texte corrigé.

**Ce que l'audit ne change pas** : le cœur de l'article : la loi déposée le jour où la base officielle enregistre 0,002 % de désinformation, le filtre du Conseil d'État qui borne la forme et acte le fond, la non-neutralité documentée institution par institution (7/9 à l'ARCOM, 95,5 % à la HATVP) : résiste à l'audit.

---

## §8. SUIVI POST-AUDIT : verification par le texte depose (2026-08-07_05-00)

Vérification de la correction E2 sur la source primaire : PDF officiel du Sénat, projet de loi n° 913, enregistré à la présidence du Sénat le 22 juillet 2026 (https://www.senat.fr/leg/pjl25-913.html ; PDF 2,6 Mo téléchargé, texte intégral extrait).

**E2 VERROUILLÉ** : l'article 1er du texte déposé dispose : « le président d'un tribunal judiciaire spécialement désigné par décret peut, à la demande du ministère public ou de toute personne ayant intérêt à agir, prescrire en référé ... toutes mesures proportionnées et nécessaires pour faire cesser cette diffusion ». Le référé est donc porté devant le juge judiciaire. Zéro occurrence de « tribunal administratif » dans le texte, neuf occurrences de « tribunal judiciaire ». La correction E2 est exacte et alignée sur la source primaire.

**E3 PRÉCISÉ** : l'ARCOM n'apparaît que dans l'exposé des motifs (jurisprudence 2018-773 DC, composition du RCPE), jamais dans le dispositif. La loi 913 étend le référé judiciaire (article 2 : création de l'art. L.48-3, abrogation de L.163-2, « tribunaux judiciaires et cours d'appel déterminés par décret », appel devant le premier président de la cour d'appel), et non un blocage ARCOM. Cinq micro-corrections appliquées à l'article le 07/08/2026 (accroche, §1, §4, §5, §8) pour coller au texte : le blocage ARCOM 48 h (SREN 2024) est désormais présenté comme un pouvoir préexistant qui s'ajoute aux trois mécanismes de la loi, et non comme un mécanisme créé ou étendu par elle.

**Confirmation annexe** : l'article 2 confirme la description du dossier (extension à toutes les élections, abrogation L.163-2, cohérent avec D13/D15 de l'investigation D). L'article 3 (peines) reste à vérifier sur le même PDF pour les montants (3 ans/45 000 €, aggravante 6 ans) ; les points 1-5 de l'article 2 renvoient aux lois 2024-449 (SREN) et 2026-249, cohérents avec le dossier.
