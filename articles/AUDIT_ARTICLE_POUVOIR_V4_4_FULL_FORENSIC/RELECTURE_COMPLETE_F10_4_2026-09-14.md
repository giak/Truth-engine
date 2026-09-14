# Relecture complète du masterwork à l'état F10.4 — avant publication

**Objet** : `01_TARGET/ARTICLE_MASTERWORK_SOUVERAINETE_2026.md`
**Date** : 14 septembre 2026
**Méthode** : lecture intégrale de bout en bout (318 lignes) + contrôles mécaniques re-exécutés + vérification externe ciblée des affirmations porteuses. Protocole Mémoire d'abord respecté : quatre recherches Mnemolite (cache miss sur les cinq points testés, voisins sans rapport), puis web, puis write-back (`5ddd102d…`, `ee20d828…`).

---

## 1. État mécanique à l'empreinte `25b32297…`

| Contrôle | Résultat |
|---|---|
| Lignes / octets | 318 / 62 439 |
| Registre | 79 entrées, numérotation continue 1→79, aucun trou |
| Renvois `[n]` dans la prose | 62 occurrences, 50 numéros distincts cités |
| Orphelins (cités, absents du registre) | 0 — le seul motif `[…]` non registre est `[2010]`, date du monospace Alstom, écart déclaré par F3 |
| Balises « (contexte) » | 29, ensembles vérifiés par diff : identiques aux 29 entrées jamais citées, ni plus ni moins |
| Apostrophes ASCII | 0 |
| Tirets cadratins | 0 |
| Emprunt de contexte / duplication de phrase | aucun résidu détecté à la lecture |

**Constat comptable que je dois porter** : la trace F10.4 annonce « renvois 63 ». Le compte réel est **62**. Reconstitutation par la chaîne des sauvegardes : avant F10 = 85 occurrences dont 48 numérotées en tête de registre… la série exploitable est : pré-F10.2 = 57, pré-F10.3 = 60, courant = 62. F10.3 a ajouté [78] (×2) et [79] (×1) = +3 sur 60 → 63 **à l'état intermédiaire** ; la lecture finale du même jour a retiré ou recomposé une occurrence (probablement lors du rescrit de la phrase 432-13, où la substitution a repris un renvoi) sans que la trace le note. Rien n'est perdu fonctionnellement : 0 orphelin, 0 entrée morte. Mais **la chaîne des empreintes porte un chiffre faux**, ce qui est exactement le genre d'écart que ce projet s'interdit. À corriger dans la trace, pas dans l'article.

---

## 2. Vérification externe ciblée (ce que la lecture a fait faire)

Chaque affirmation porteuse a été confrontée à sa pièce ou à une source indépendante :

| Affirmation (l.) | Verdict | Pièce de contrôle |
|---|---|---|
| Veto Photonis/Teledyne « en 2020 » (§V) | **Exact** | Refus notifié le 18 décembre 2020 (Le Monde 19/12/2020 ; Lexology 13/01/2021) ; reprise HLD, actif resté français (Les Échos 15/02/2021) |
| *Rockhopper* : 190 M€ (§II.2) | **Exact** | Sentence finale 23 août 2022, ARB/17/14 : « EUR 190 million (USD 216.3 million), plus interest » (Dentons, Ciarb, Climate Case Chart) ; annulation 2 juin 2025 confirmée |
| FAQ ISOC « février 2022 » (§III.2, [28]) | **Exact** | Datée du 22 février 2022 (CRS R48902, WTSA/ISOC) |
| DGSI, neuf relais de stations (§I.6, [67]) | **Exact** | Question écrite n° 1675 (5 nov. 2024) : « La DGSI a identifié 9 “stations de police” » ; fermeture début 2026 (Le Monde 17/06/2026) |
| Dérogation ePrivacy « rétablie jusqu'au 3 avril 2028 », volontaire, E2EE exclues (§I.3, [69]) | **Exact** | Règlement (UE) 2026/1881 adopté le 24 juillet 2026, JO du 28, applicable « until 3 April 2028 », détection volontaire (EU Law Live, 28/07/2026). Le communiqué PE du 9 juillet décrivait l'état intermédiaire, pas l'issue |
| *Bank Melli* C-124/20, 21 déc. 2021, premier arrêt CJUE sur le règlement de blocage (§I.2, [12]) | **Exact** | Grand chambre, 21/12/2021, premier jugement d'interprétation du Blocking Statute (Steptoe, Curtis, Mayer Brown) |
| SIPRI « 2e exportateur mondial » (prologue, l. 7) | **Vrai mais non sourcé** | Confirmé (France 2e fournisseur 2020–24 et 2021–25, 9,8 % des exports) mais **aucune entrée de registre ne porte cette affirmation** — voir défaut R-2 |
| 57,1 Md€ défense 2026 (prologue, [76]) | Déjà vérifié à F9 (source ministérielle lue) | — |
| 432-11 / 432-13 / 433-2 / directive 2026/1021 (§IV.2) | Déjà vérifiés à F10.3/F10.4 (Légifrance lu, PE-CONS 1/26 lu en intégralité) | — |

---

## 3. Défauts trouvés

### Défauts de fond (3 — tous réparables en une tranche mécanique)

**F-A — Surgeneralisation de la portée des deux études agences (l. ~148 et l. ~160).** C'est le défaut le plus sérieux, et il est de la même classe que celui réparé à F9 sur VIGINUM : une pièce dit une chose précise, la phrase lui fait dire sa généralisation.

La phrase : « Les recherches universitaires de Boumans (2018) [29] et Vogler (2024) [30] révèlent que plus de 60 % de la couverture des affaires internationales publiée par la presse en ligne européenne est directement recopiée ou traduite à partir des dépêches de trois agences mondiales (AFP, Reuters, Associated Press). »

Ce que les pièces disent réellement :
- **Boumans et al. 2018 (lue intégralement sur la page de l'IJoC)** : landscape **néerlandais** uniquement, n = 247 161 items (119 452 articles, une année), conclusion : l'agence est responsable de « **up to 75 %** » des articles de news **en ligne** néerlandaises, avec forte proportion de reprise verbatim. Elle ne mesure ni l'Europe, ni les seules affaires internationales, ni le triptyque AFP/Reuters/AP.
- **Vogler et al. 2024** : landscape **suisse** (rédactions suisses ; je n'ai pas pu lire le texte intégral, Anubis et 403 — la portée nationale est établie par les sources secondaires concordantes, le chiffre exact reste non relu).

Le « plus de 60 % », l'« européenne » et le trio d'agences nommé comme mesuré sont donc **une agrégation que aucune des deux pièces ne porte**. La monospace de la figure en hérite (« 60 %+ du contenu d'actualité internationale dans les médias européens »). Réparation honnête : dire ce que les pièces disent (dépendance forte et reprise verbatim au niveau national, l'un aux Pays-Bas avec jusqu'à 75 % de l'actualité en ligne, l'autre en Suisse), et formuler l'inférence européenne comme une hypothèse de concentration, pas comme un chiffre. La thèse du verrou III y perd peu ; y perdre un faux précision, tout y gagner.

**F-B — Le « 70 % » du cloud n'est sourcé pour aucun de ses trois usages (l. 3, l. 11, l. 19).** Le chiffre 70 % existe bel et bien : Synergy Research (juillet 2025, reprises DCD, ITPro, fierce-network) documente **70 % du marché européen du cloud** pour AWS+Microsoft+Google, fournisseurs européens à 15 % ; 63 % à l'échelle mondiale (nov. 2025). Mais :
- le sous-titre (l. 3) et la monospace (l. 19) disent « un marché du cloud détenu à 70 % » sans portée géographique ;
- le prologue (l. 11) dit « **son** marché du cloud » — la France — portée pour laquelle je n'ai aucune pièce (les estimations de parts françaises existent mais aucune n'est au registre, et le masterwork n'en cite aucune) ;
- **aucune entrée du registre ne porte ce chiffre**, alors qu'il ouvre l'article et son sous-titre.

C'est structurellement le défaut HATVP inverse : une affirmation headline sans pièce, dans un article dont tout l'appareil repose sur le renvoi. Réparation : soit sourcer le 70 % comme européen (Synergy) et reformuler les trois occurrences (« près de 70 % du marché européen »), soit le réduire à ce que les pièces [51]/[73] (dépendances documentées Azure, EUCS) portent sans chiffre agregé. Deux nouvelles entrées de registre au besoin.

**F-C — Le SIPRI du prologue n'a pas de pièce (l. 7).** « Se classe au 2e rang mondial des exportateurs d'armement » : vrai, vérifié deux fois (2020–24, 2021–25), mais aucune entrée du registre. Même traitement que F-B : une entrée SIPRI et un renvoi, ou une formulation attribuée sans numéro si on préfère ne pas ouvrir le registre pour un élément de contexte.

### Défauts d'appareil (2 — comptabilité, pas contenu)

**R-1 — Le « 63 » de la trace F10.4 est faux (62 réels).** Voir §1. À corriger dans `SEMANTIC_DIFF_F10_2026-09-14.md` avec la note d'erreur, comme cela a été fait pour la liste provisoire de F10.2.

**R-2 — Deux affirmations de prologue vivent hors registre** (F-B et F-C ci-dessus). Cohérence d'ensemble : tout ce que la prose avance de factuel doit avoir soit une pièce, soit une borne explicite.

### Cosmétique relevé à la lecture (non bloquant)

- L. 19, monospace : « Membre permanent Conseil de Sec. » — abréviation rognée par la largeur de colonne ; acceptable en figure, à voir si on garde la figure.
- L. 30 : « Conseil de sécurité des Nations unies, se classe » — ok, mais la phrase 3 du prologue porte trois affirmations de puissance dont une seule est sourcée ([76]) ; les deux autres (dissuasion, CSNU) sont de common knowledge admissible, je le note pour exhaustivité sans demander d'entrée.
- La monospace Alstom dit « 772,29 M$ » et le corps « 772,29 millions de dollars » : cohérents entre eux.

---

## 4. Ce que la lecture confirme comme solide

- **La chaîne probatoire IV.2** (432-11 [78], 432-13 [79], 433-2 [41], directive [42]) est désormais exacte dans ses termes et dans ses dates, après les deux corrections de F10.3 et la réécriture F10.4 ; l'angle mort reste correctement argumenté sur les exigences de fait, pas sur un délai mal lu.
- **L'auto-défense épistémologique** (partie V et épilogue) est tenue de bout en bout : la thèse de la convergence est déclarée « lecture proposée », le chaînage ouvert, l'inventaire « ne démontre pas un système ». Les deux phrases antérieures qui universalisaient ont été réparées par les tranches T/F.
- **La matrice de 14 instruments** (F7) : chaque ligne porte sa pièce ; les deux nombres classés non sourçables à F7 n'ont pas été importés ; aucune ligne ne mélange deux natures.
- **Les huit nombres** (F9) sont bornés correctement, y compris les deux adossés à des sources secondaires déclarées ([71] CNBC, [74] The Conversation sur DER).
- **Typographie et convention des renvois** : 0 apostrophe ASCII, 0 cadratin, la convention « nom dans la prose + [n] + (contexte) » est énoncée dans le registre et respectée.

## 5. Ce que je n'ai pas pu faire (et que personne n'a fait)

- **Relire les 59 pièces** entrée par entrée : la note de vérification l'avait déjà déclaré hors de portée ; cette relecture n'a pas levé cette limite, elle l'a rétrécie en revérifiant les affirmations porteuses citées plus haut.
- **Lire le texte intégral de Vogler 2024** : Anubis (Zora) et 403 (Taylor & Francis). La portée suisse est établie par sources secondaires ; le pourcentage exact suisse reste non relu.
- **Comparaison byte à byte PE-CONS 1/26 vs version JO de la directive 2026/1021** : caveat hérité de F10.4, inchangé.

## 6. Verdict

**L'article n'est pas encore publiable en l'état, mais l'écart est court et mécanique.** Trois défauts de fond (F-A, F-B, F-C), tous du même type — une affirmation qui excède ou contourne sa pièce — et deux corrections de comptabilité. Aucun n'atteint la structure, la matrice, la chaîne légale ou l'auto-défense. Une tranche **F11** (sourçage/réécriture des trois défauts + correction du « 63 » dans la trace) ferme l'écart ; elle est estimée à une session de travail unique, sans nouvelle investigation.

Après F11, la relecture de contrôle finale peut se limiter aux phrases modifiées et à la re-numérotation du registre (80-81 si deux entrées nouvelles).

---

## 7. Chaîne des empreintes

| Tranche | Empreinte | Lignes |
|---|---|---|
| Fin F10.2 | `997e76a6…` | 316 |
| Fin F10.3 | `150da463…` | 318 |
| Fin F10.4 — **état relu** | `25b32297…` | 318 |
| (après F11, à compléter) | — | — |

## 8. Write-back mémoire

- `5ddd102d…` — portée réelle des études agences (Boumans/Pays-Bas 75 % online, Vogler/Suisse) et du chiffre cloud 70 % (marché européen, Synergy).
- `ee20d828…` — confirmations web : Photonis 18/12/2020, Rockhopper EUR 190 M, ISOC 22/02/2022, SIPRI 2e exportateur, DGSI 9 stations.
