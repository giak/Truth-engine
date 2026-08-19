# Preuve de bout en bout de la chaîne fact-checking

Date : 2026-08-18 22:18 CEST. Objet : prouver sur un fait réel la chaîne
fetch → write_memory → capture id → mem: → read_memory(id).

## 1. Le fait

L'ouvrage d'Emmanuel Blanchard, « La Police parisienne et les Algériens (1944-1962) »,
a été publié aux Éditions du Nouveau Monde en 2011.

## 2. Sources (2 familles indépendantes, fetchées HTTP 200)

- A (éditeur, primaire) : Éditions du Nouveau Monde, catalogue en ligne.
  « septembre 2011 », ISBN 9782847366273, 450 pages.
  https://www.nouveau-monde.net/catalogue/la-police-parisienne-et-les-algeriens-1944-1962/
- E (recension académique) : Muriel Cohen, « New Light on a Colonial Massacre »,
  Books & Ideas / La Vie des Idées, 24 avril 2012 : « Paris, Nouveau Monde éditions, 2011, 447 p. »
  https://laviedesidees.fr/New-Light-on-a-Colonial-Massacre

## 3. Écriture et bouclage (les 4 étapes prouvées)

1. write_memory → id retourné : 2533f312-6440-4202-b44e-bf0cf76889b2 (aucun duplicate_warning).
2. Tags écrits : status:CONFIRME, verifie-2026-08-18, source:1e86c287f2, epi:fact, blanchard, police, algeriens, livre.
3. read_memory(2533f312-6440-4202-b44e-bf0cf76889b2) → contenu identique renvoyé (round-trip OK).
4. mem:<id> écrit dans FACT_REGISTRY_V1 (9e champ), parsé sans violation.

## 4. Registre des faits

<!-- FACT_REGISTRY_V1 -->
FCT-001|FACT|✦|https://www.nouveau-monde.net/catalogue/la-police-parisienne-et-les-algeriens-1944-1962/|A,E|2026-08-18|blanchard-police-parisienne-algeriens-2011|Emmanuel Blanchard, La Police parisienne et les Algériens (1944-1962), Éditions du Nouveau Monde, 2011|2533f312-6440-4202-b44e-bf0cf76889b2
<!-- /FACT_REGISTRY_V1 -->

## 5. Verdict

- Chaîne prouvée de bout en bout sur 1 fait réel : OUI.
- Deux observations de fond :
  1. Le serveur Mnemolite normalise les tags en minuscules (epi:FACT → epi:fact) et
     émet un warning « namespace de tag inconnu epi: » (EPIC-60). Le contrat
     FACT_VERIFICATION (epi:FACT) diverge du registre de tags du serveur.
  2. La divergence 450 p. (éditeur) vs 447 p. (recension) n'affecte pas le fait :
     titre, auteur, éditeur et année identiques dans les deux familles.
