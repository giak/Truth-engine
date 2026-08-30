# XQ203 - Journal d'audit ciblé du « ×12 »

**Date du contrôle final :** 24 août 2026  
**Objet :** documenter une recherche négative bornée, sans transformer l'absence de résultat en preuve d'inexistence.

## 1. Question

Un article de fact-checking publié par l'une des quatre unités suivantes entre le 12 juillet et le 30 septembre 2021 a-t-il été retrouvé comme vérification directe de la formule d'Emmanuel Macron ou d'Olivier Véran selon laquelle les vaccins « divisent par 12 » le pouvoir de contamination du variant Delta ?

Unités auditées :

- AFP Factuel ;
- franceinfo / Vrai ou Fake ;
- Le Monde / Les Décodeurs ;
- Libération / CheckNews.

## 2. Critère d'équivalence directe

Un résultat est équivalent s'il réunit les quatre conditions suivantes :

1. publication dans la fenêtre du 12 juillet au 30 septembre 2021 ;
2. identification de la formule « ×12 », « 12 fois » ou « divisent par 12 » attribuée à Macron ou Véran ;
3. examen de la provenance Pasteur ou du caractère modélisé du ratio ;
4. jugement explicite sur la validité, les hypothèses ou la portée de cette formule.

Un article général sur l'efficacité vaccinale, le passe sanitaire, Blanquer, Castex ou la transmission ne remplit pas ce critère s'il n'examine pas directement le « ×12 ».

## 3. Requêtes rejouées le 24 août 2026

Requêtes par unité :

```text
AFP Factuel Macron divise par 12 contamination vaccin 2021
Franceinfo Vrai ou Fake Macron divise par 12 contamination vaccin 2021
Les Décodeurs Macron divise par 12 contamination vaccin 2021
CheckNews Macron divise par 12 contamination vaccin 2021
```

Variantes de contrôle :

```text
site:factuel.afp.com (Macron OR Véran) ("divisent par 12" OR "12 fois") vaccin contamination juillet 2021
site:francetvinfo.fr (Macron OR Véran) ("divisent par 12" OR "12 fois") vaccin contamination juillet 2021
site:lemonde.fr/les-decodeurs (Macron OR Véran) ("divisent par 12" OR "12 fois") vaccin contamination juillet 2021
site:liberation.fr/checknews (Macron OR Véran) ("divisent par 12" OR "12 fois") vaccin contamination juillet 2021
```

Contrôle de l'index Covid d'AFP Factuel : recherche interne des chaînes `divisent par 12` et `12 fois` dans la page https://factuel.afp.com/le-coronavirus-les-verifications-faites-par-lafp.

## 4. Résultats

- Aucun résultat répondant aux quatre critères d'équivalence directe n'a été retrouvé par ces requêtes.
- L'index Covid d'AFP Factuel ne contient pas les chaînes exactes `divisent par 12` ou `12 fois` lors du contrôle final.
- Les requêtes directes vers franceinfo et CheckNews ont rencontré des restrictions d'accès automatisé ; leur résultat négatif est donc moins fort.
- Des vérifications contemporaines distinctes ont bien été retrouvées sur les formulations de Jean-Michel Blanquer et Jean Castex : elles ne sont pas reclassées comme équivalents du « ×12 ».
- Une page Yahoo Actualités datée du 23 juillet 2021 et consacrée au ratio reste indexée, mais son corps n'était pas accessible dans le contrôle final. Elle prouve l'existence d'un questionnement médiatique, pas la qualité ni le contenu précis de son analyse.
- AFP Factuel a publié le 18 octobre 2022 une contextualisation rétrospective portant explicitement sur les raccourcis de 2021 : https://factuel.afp.com/doc.afp.com.32LA33T.

## 5. Limites et conclusion autorisée

Le journal du contrôle du 22 août mentionné dans XQ202 n'a pas été retrouvé comme fichier autonome. XQ203 ne le présente donc plus comme une pièce directement rejouable. Le présent document conserve la réexécution du 24 août, ses requêtes et ses restrictions d'accès.

Conclusion autorisée :

> Aucun fact-check contemporain directement équivalent n'a été retrouvé dans ces quatre unités, cette fenêtre temporelle et avec ces voies d'accès. Une contextualisation AFP explicite existe en octobre 2022.

Conclusions interdites :

- « aucun média n'en a parlé » ;
- « aucun fact-check n'a existé » ;
- « les quatre rédactions ont volontairement ignoré la formule » ;
- toute fréquence ou hiérarchie générale déduite de ce résultat négatif.
