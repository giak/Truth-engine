# Tranche F11 — les trois défauts de la relecture fermés

**Date** : 14 septembre 2026
**Objet** : `01_TARGET/ARTICLE_MASTERWORK_SOUVERAINETE_2026.md`
**Mandat** : appliquer la tranche F11 issue de la relecture complète (`RELECTURE_COMPLETE_F10_4_2026-09-14.md`) : reformuler la phrase des agences, sourcer ou reformuler le « 70 % » du cloud et le SIPRI, corriger le « 63 » de la trace F10.
**Objet modifié** : `25b32297…` → **`94c93001…`**, 318 → 320 lignes, 62 439 → 63 622 octets. Sauvegarde pré-édition : `/tmp/ARTICLE_MASTERWORK_AVANT_F11.md`.

---

## 1. F-A — la phrase des agences (partie III.3) reformulée sur ses pièces

**Avant** : « Les recherches universitaires de Boumans (2018) [29] et Vogler (2024) [30] révèlent que plus de 60 % de la couverture des affaires internationales publiée par la presse en ligne européenne est directement recopiée ou traduite à partir des dépêches de trois agences mondiales (AFP, Reuters, Associated Press). »

**Après** : « Les études universitaires disponibles portent sur des paysages nationaux, mais elles convergent : aux Pays-Bas, Boumans et ses coauteurs (2018) établissent que les dépêches d’agence alimentent jusqu’à 75 % de l’actualité en ligne, en grande partie reprises verbatim [29] ; en Suisse, Vogler et ses coauteurs (2024) documentent le même rôle structurant du matériel d’agence dans les rédactions [30]. Aucune de ces études ne mesure l’Europe dans son ensemble : l’hypothèse d’une dépendance comparable de la presse en ligne européenne aux dépêches des grandes agences mondiales, dont AFP, Reuters et Associated Press, reste à établir par une mesure dédiée. »

**Pourquoi** : la page de l’*International Journal of Communication* de Boumans et al. (2018) a été lue à la relecture : paysage **néerlandais** (n = 247 161 items), conclusion « up to 75 % » des articles de news **en ligne**, reprise verbatim fréquente. Vogler et al. (2024) porte sur les rédactions **suisses** (texte intégral non relu, bloqué par Anubis côté Zora et 403 côté Taylor & Francis ; portée nationale établie par sources secondaires concordantes). Ni l’une ni l’autre ne mesure la « couverture internationale européenne » ni le trio AFP/Reuters/AP. La phrase reformulée conserve l’argument du verrou (concentration des flux d’origine) sans lui prêter un chiffre agrégé inexistant.

**Effets en cascade, cohérences maintenues** :
- la ligne de la figure « 60 %+ du contenu d’actualité internationale dans les médias européens » devient « [Rédactions en ligne fortement dépendantes du matériel d’agence] » ;
- la ligne de la matrice (partie V) devient : « Dépendance des rédactions en ligne au matériel d’agence établie au niveau national (Pays-Bas, Suisse) ; généralisation européenne non mesurée » ;
- l’introducteur « Les recherches universitaires … révèlent que » disparaît : c’est lui qui portait la surgeneralisation.

## 2. F-B — le « 70 % » du cloud, attribué à sa portée réelle

Le chiffre existe, il n’est pas français : Synergy Research Group (24 juillet 2025) documente AWS + Microsoft + Google à environ **70 % du marché européen du cloud d’infrastructure**, fournisseurs européens à 15 %.

| Emplacement | Avant | Après |
|---|---|---|
| Sous-titre (l. 3) | « un marché du cloud détenu à 70 % » | « un marché du **cloud européen** détenu à 70 % » |
| Prologue (l. 11) | « environ 70 % de **son** marché du cloud est détenu par trois fournisseurs américains » | « environ 70 % du **marché européen** du cloud est détenu par trois fournisseurs américains [80] » |
| Monospace (l. 19) | « • Marché cloud 70 % (3 acteurs US) » | « • Cloud UE : 70 % (3 acteurs US) » |

**Nouvelle entrée [80]** : Synergy Research Group, *European Cloud Providers’ Local Market Share Now Holds Steady at 15%*, 24 juillet 2025, avec URL. La phrase du prologue gagne son renvoi et perd l’ambiguïté de portée ; les données publiques et de santé confiées à ces acteurs restent documentées par [51] et [73].

## 3. F-C — le SIPRI du prologue reçoit sa pièce

Le « 2e rang mondial des exportateurs d’armement » est vrai mais vivait hors registre. **Nouvelle entrée [81]** : SIPRI, *Trends in International Arms Transfers, 2024* (communiqué du 10 mars 2025 : la France deuxième fournisseur mondial d’armements majeurs sur 2020-2024), avec renvoi **[81]** posé dans la phrase du prologue.

## 4. L’erratum comptable de la trace F10

Le §7 de `SEMANTIC_DIFF_F10_2026-09-14.md` annonçait « renvois 61 → 63 » ; la relecture a compté **62** à l’état final. Un **erratum** a été ajouté au §7 de la trace, qui déclare : le compte exact à partir de F10.3 est **62** ; la comptabilité pas à pas de F10.3 ne peut plus être reconstituée avec certitude (l’état intermédiaire sauvegardé `AVANT_F10c_check` porte déjà 60 occurrences avec [78] ×1 et [79] ×2) ; l’alinéa faux est conservé tel quel par décision de ne pas réécrire les états de tranche. La même correction est portée par la relecture (`RELECTURE_COMPLETE…` §1) et le `SUIVI` (complément de §6.20) depuis avant la tranche.

## 5. Contrôles post-tranche

| Contrôle | Résultat |
|---|---|
| Lignes / octets / empreinte | 320 / 63 622 / **`94c93001…`** |
| Registre | 81 entrées, numérotation continue 1→81 |
| Renvois `[n]` dans la prose | 64 occurrences, 53 numéros distincts |
| Orphelins | 0 (le seul motif hors registre reste « [2010] », écart déclaré) |
| Balises « (contexte) » | 29, ensemble vérifié identique aux jamais-citées (ni plus ni moins) — aucune sur [80]/[81], qui sont citées |
| Apostrophes ASCII / tirets cadratins / insécables | 0 / 0 / 0 |
| Largeurs de cadres monospace | blocs 1, 4, 5 : toutes les lignes à la largeur modale de leur bloc (75, 84, 75) — deux bordures faussées par l’édition ont été détectées et corrigées |
| [80] / [81] | citées chacune une fois dans la prose, présentes au registre |

## 6. Ce que la tranche ne prétend pas

- Le texte intégral de **Vogler 2024** n’a pas été relu (protections éditeur et dépôt institutionnel) : la portée suisse est établie par sources secondaires concordantes, l’entrée [30] reste inchangée.
- Le **70 %** reste un chiffre d’un cabinet d’analyse de marché (Synergy), pas d’une donnée réglementaire : l’entrée [80] le déclare par son intitulé.
- La **généralisation européenne** de la dépendance aux agences est désormais explicitement une **hypothèse non mesurée** dans l’article : si une mesure dédiée est trouvée plus tard, la phrase devra être rouverte.

## 7. Write-back mémoire

Fait à la relecture (`5ddd102d…`, `ee20d828…`) : portée réelle des deux études agences, chiffre cloud européen, confirmations Photonis/Rockhopper/ISOC/SIPRI/DGSI. La présente tranche n’apporte aucun fait nouveau : elle aligne l’article sur ces vérifications.
