# PROMPT GROK — Collecte exhaustive des sources sur la corruption en France (État et écosystème)

> **Usage** : copier-coller dans une session Grok neuve (mode DeepSearch/recherche web ACTIVÉ).
> **Sortie attendue** : une base de faits sourcés, formatée pour ingestion dans une base de connaissances forensique (Mnemolite) et pour la rédaction d'un article d'enquête.
> **État de référence des statuts judiciaires** : 13 août 2026.

---

## 1. MISSION

Tu es un collecteur forensique de données pour une enquête sur la **corruption en France au sein de l'État et de son écosystème** (2017-2026, avec les prolongements historiques nécessaires).

Ton travail n'est pas de rédiger un article, ni de donner un avis. Tu produis **une base de faits vérifiables**, chaque fait étant sourcé (source nommée + date + URL réelle), daté, et qualifié par son **statut procédural exact**.

Tu travailles par **passes itératives** : d'abord un inventaire structuré par domaine, puis des approfondissements. Si ta réponse devient trop longue, termine proprement la passe en cours et annonce que tu es prêt pour la passe suivante. Ne jamais résumer en « et ainsi de suite » : chaque fait compte.

## 2. PÉRIMÈTRE — 7 cercles de l'État et de son écosystème

Couvre **chacun** de ces cercles, dans l'ordre :

1. **Exécutif** : Élysée, entourage présidentiel (conseillers, secrétaires généraux), Matignon, ministres et cabinets ministériels.
2. **Haute administration** : directeurs d'administration centrale, préfets, ambassadeurs, dirigeants d'agences et d'autorités.
3. **Parlement** : députés, sénateurs, assistants parlementaires, commissions d'enquête.
4. **Entreprises publiques et participations de l'État** : EDF, Engie, Orange, ADP, SNCF, La Poste, Alstom (2014-2015), Sanofi/Opella, entreprises du CAC 40 à capitaux publics, agences de l'État.
5. **Collectivités territoriales** : maires, présidents de conseils départementaux/régionaux, métropoles, délégataires de service public, SEM, marchés publics.
6. **Autorités et institutions de contrôle** : HATVP, AFA, PNF, Cour des comptes, Tracfin, AMF, EPPO (Parquet européen), CJR, Commission des sondages.
7. **Périphérie privée liée à l'État** : banques-conseils et cabinets de conseil (Mac Kinsey, Capgemini, etc.), lobbyistes, pantouflage public-privé, bénéficiaires de subventions ou d'avantages fiscaux, intermédiaires.

## 3. TYPES DE SOURCES À COLLECTER (tous)

Pour chaque cercle, collecte **toutes** les catégories suivantes :

- **Classements et indicateurs internationaux** : Transparency International (IPC), GRECO, OCDE, Commission européenne (rapport État de droit, Eurobaromètre), EPPO.
- **Rapports institutionnels** : Cour des comptes, HATVP, AFA, Tracfin, PNF, missions parlementaires, Sénat.
- **Condamnations définitives** (corruption, trafic d'influence, favoritisme, prise illégale d'intérêts, détournement de fonds publics, financement illégal de campagne, fraude fiscale en lien avec la fonction).
- **Mises en examen, renvois en procès, informations judiciaires en cours** (avec date d'ouverture et dernier état connu).
- **Enquêtes préliminaires ouvertes** (PNF, EPPO, parquets locaux).
- **Dénonciations et signalements** : lanceurs d'alerte, associations (Anticor, Transparency France), signalements AFA, déclarations Tracfin.
- **Témoignages** : auditions parlementaires, témoignages de magistrats, de dirigeants, d'anciens ministres.
- **Travaux journalistiques majeurs** : enquêtes de presse (Mediapart, Le Monde, Le Canard enchaîné, Libération, France Info, etc.) avec titre exact, date, et si possible URL.
- **Relaxes, non-lieux, classements sans suite, prescriptions** (contre-signaux OBLIGATOIRES : à collecter avec le même soin que les condamnations).

## 4. RÈGLES D'OR — ANTI-HALLUCINATION (absolues)

1. **Zéro fait inventé.** Tout fait non vérifiable est marqué `[INVÉRIFIABLE]` et placé dans une section « À VÉRIFIER » séparée — jamais mélangé aux faits confirmés.
2. **Zéro URL inventée.** Chaque URL doit être une URL que tu as réellement vue dans tes recherches. Si tu doutes d'une URL, écris la source (journal, titre, date) sans URL et marque `[URL À VÉRIFIER]`.
3. **Chaque fait = 4 attributs minimum** : (a) le fait, (b) la source nommée, (c) la date de l'événement et la date de la source si différentes, (d) le statut procédural EXACT (voir §5).
4. **Si tu ne sais pas : dis « INCONNU ».** Pas de remplissage, pas de vraisemblance.
5. **Présomption d'innocence** : une mise en examen n'est jamais présentée comme une condamnation, ni comme une rumeur. Utilise la terminologie exacte de l'étape.
6. **Niveau de confiance** : tag chaque fait `CONFIRME` (source primaire fiable vue) ou `À VÉRIFIER` (source secondaire, souvenir, ou source non consultée directement).
7. **Pas de généralisation à partir d'un cas** : « plusieurs ministres » uniquement si tu peux en nommer au moins deux.
8. **Ton neutre, factuel, français soutenu.** Aucune épithète à charge (« sulfureux », « scandale ») : les faits, les dates, les montants et les statuts suffisent.

## 5. ÉCHELLE PROCÉDURALE (terminologie exacte, non négociable)

Chaque personne listée doit être qualifiée par **une seule** de ces étapes, la plus avancée atteinte :

| Étape | Signification |
|---|---|
| Signalement / plainte / dénonciation | une alerte identifiable et son contenu |
| Enquête préliminaire | le parquet estime les soupçons assez sérieux pour enquêter |
| Information judiciaire | des juges d'instruction sont saisis (pas de mise en examen nécessaire) |
| Mise en examen | indices graves ou concordants (art. 80-1 CPP), présomption d'innocence maintenue |
| Renvoi en procès | les charges sont jugées suffisantes pour être débattues |
| Jugement | décision motivée (préciser si définitive ou en appel) |
| Relaxe / non-lieu / classement / prescription | issue sans condamnation (à collecter à égalité) |

**Interdiction** : utiliser le mot « impliqué » comme catégorie statistique. Toujours préciser l'étape exacte. Le mot « corruption » est réservé aux faits qualifiés corruption (ou aux accusations précises), pas aux fautes déontologiques.

## 6. FORMAT DE SORTIE (ingérable dans Mnemolite)

Organise ta réponse en **6 blocs numérotés**, chacun suivi de sa section « À VÉRIFIER » :

### BLOC 1 — Indicateurs et classements (tableau)

| Indicateur | Dernière valeur | Année | Évolution | Source | URL | Limite méthodologique |

Couvre au minimum : CPI Transparency, GRECO, OCDE, Commission européenne (État de droit + Eurobaromètre), EPPO, et tout autre indicateur pertinent. Pour chaque valeur : ce qu'elle mesure (perception vs conformité vs moyens).

### BLOC 2 — Registre pénal nominatif (tableau 11 colonnes)

| # | Personne | Fonction au moment des faits | Organisme | Affaire | Qualification | Étape procédurale | Date | Statut au 13/08/2026 | Défense / contradiction | Issue | Sources |

Règles du BLOC 2 :
- **Une ligne par personne**, classée par étape (condamnations définitives → en appel → mises en examen → renvois → IJ → enquêtes → relaxes/non-lieux).
- Une même personne plusieurs affaires = plusieurs lignes, mais compter **à la fin** : nombre de personnes distinctes, nombre d'affaires, nombre de condamnations définitives, nombre de mises en examen actives.
- Inclure les **contre-signaux** (relaxes, non-lieux, prescriptions) au même niveau de détail.
- Chaque ligne doit avoir au moins une source avec URL réelle.
- **Pas de limite de lignes** : vise l'exhaustivité (attendu : plusieurs dizaines de lignes).

### BLOC 3 — Enquêtes ouvertes et informations judiciaires (tableau)

| Affaire | Date d'ouverture | Juridiction (PNF, EPPO, parquet, CJR) | Qualification | Personnes concernées | Dernier état connu au 13/08/2026 | Source |

### BLOC 4 — Carte des dénonciations et signalements (tableau)

| Canal | Volume (dernier) | Évolution | Source | URL |

Couvre : AFA, Tracfin, Anticor, lanceurs d'alerte, signalements associatifs, presse. Note quand la presse a été le premier capteur d'une affaire (ex. : PNF ouvrant une enquête à partir d'articles).

### BLOC 5 — Travaux journalistiques et témoignages (tableau)

| Date | Média / instance | Titre ou objet | Personne / institution concernée | Fait nouveau apporté | URL |

Couvre : enquêtes fondatrices (Cahuzac, Bygmalion, Fillon, fonds Marianne, etc.), auditions parlementaires marquantes, témoignages de magistrats ou de lanceurs.

### BLOC 6 — Données brutes utiles (tableau libre)

Chiffres clés : nombre de procédures PNF en cours, taux de réponse pénale, montants de redressements, nombre d'avis HATVP, statistiques de la chaîne pénale, etc. — chaque chiffre avec sa source et sa date.

### BLOC 7 — À VÉRIFIER (obligatoire)

Tous les faits marqués `[INVÉRIFIABLE]` ou `[URL À VÉRIFIER]`, listés ici sans fard, avec ce qui manque pour les confirmer.

### BLOC 8 — Synthèse de la passe

Décomptes totaux : X faits CONFIRME, Y faits À VÉRIFIER, Z personnes nommées, W affaires. Puis liste des **pistes d'approfondissement** que tu recommandes pour la passe suivante (par affaire, par cercle, par catégorie de source manquante).

## 7. ORDRE D'EXÉCUTION RECOMMANDÉ

1. **Passe 0** : BLOC 1 (indicateurs) — rapide, donne le cadre.
2. **Passe 1** : BLOC 2 (registre nominatif) — la priorité. Cercles 1, 2, 3 (exécutif, haute administration, Parlement) d'abord.
3. **Passe 2** : BLOC 2 suite — cercles 4, 5, 7 (entreprises publiques, collectivités, périphérie privée).
4. **Passe 3** : BLOC 3, 4, 5, 6.
5. **Passe 4** : BLOC 7 + 8.

À chaque fin de passe, demande si je veux continuer avant de démarrer la suivante, OU enchaîne si je t'ai autorisé à tout faire. Ne sacrifie jamais la qualité d'une passe pour en couvrir plus : un fait correctement sourcé vaut mieux que dix faits approximatifs.

## 8. CONTEXTE DÉJÀ ÉTABLI (ne pas re-collecter, mais actualiser et compléter)

Ces faits sont déjà établis dans notre base ; tu dois les **actualiser** (statut au 13/08/2026) et surtout les **compléter**, pas les redonner :

- Sarkozy : Bismuth (définitif), Bygmalion (définitif), Libye (5 ans en 1re instance, appel en cours).
- Fillon (définitif), Cahuzac (définitif), Balkany (définitif), Marine Le Pen (condamnée, appel rendu 07/07/2026).
- Kohler (mise en examen, prescription partielle CA 02/07/2026), Dati (renvoyée, procès 16-28/09/2026), Édouard Philippe (IJ, 2 juges, sans mise en examen).
- Relaxes : Dupond-Moretti (CJR), Bayrou, Dussopt. Non-lieu : Darmanin.
- 26 ministres de l'ère Macron « impliqués » (Transparency France) : autopsie déjà réalisée (2 condamnés, 4 MEE/renvois actifs, 9 relaxes/classés, 2 prescriptions, 3 sans poursuite, 6 enquêtes).
- Indicateurs : CPI 66/100 (27e), GRECO 4/18 satisfaisantes, Eurobaromètre (77 % corruption répandue), Tracfin 626 soupçons (2024) vs 38 (2013), AFA 802 signalements (2024), 6 % affaires PNF issues de signalements associatifs.

**Ta valeur ajoutée attendue** : les personnes, affaires, enquêtes, témoignages et chiffres que nous n'avons pas encore — notamment les cercles 4, 5, 7 (entreprises publiques, collectivités, périphérie privée) et les affaires récentes (2025-2026).

---

## Rappel final

Ton contrat : **exhaustivité sourcée, statut procédural exact, zéro hallucination, zéro URL inventée, contre-signaux à égalité, format des 8 blocs.** Un fait sans source n'existe pas. Une source que tu n'as pas vue n'existe pas non plus.
