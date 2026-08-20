# Test du premier candidat SQLite

## Identité

- `RECORD_ID` : `FC17_0033BA3236A3D267`
- `RECORD_TYPE` : `ECOSYSTEM_RELATION`
- `DATA_CLASS` : `ECOSYSTEM_GRAPH`
- `SUBJECT` : European Digital Media Observatory (EDMO)
- `PREDICATE` : `CONSORTIUM_PARTNER`
- `OBJECT` : Athens Technology Center (ATC)
- `SOURCE_URL` : <https://edmo.eu/about-us/>
- `SOURCE_TYPE` : `PRIMARY_OR_PROJECT_PAGE`
- Statut SQLite brut : `FACT`
- Statut de vérification : `VERIFIE` (L1, source officielle unique ; L2 non établi)

## Procédure effectuée

1. Recherche Mnemolite mémoire-d'abord sur EDMO, Athens Technology Center et le lien de consortium, avec filtre `status:CONFIRME`.
2. Aucun résultat retourné ne documente explicitement le couple EDMO → Athens Technology Center.
3. Lecture de l'URL primaire fournie par le SQLite.
4. Recherche web de corroboration accessible.
5. Lecture de l'artefact local cité par la chaîne d'investigation.
6. Recherche de la source institutionnelle de remplacement dans le SQLite et les artefacts Cycle 18.
7. Lecture de la page de la Commission européenne et recherches web ciblées.
8. Write-back contrôlé en `status:VERIFIE`, avec `dedup_check=true`.

## Résultats

- `read_url` sur `https://edmo.eu/about-us/` : `403 Forbidden` pour l'accès automatisé.
- Chrome headless a obtenu la page, mais son texte visible ne contenait pas le couple EDMO / Athens Technology Center. La page générale est donc insuffisante pour ce record.
- Le SQLite et les artefacts Cycle 18 fournissent une URL institutionnelle plus précise : `https://digital-strategy.ec.europa.eu/en/news/european-digital-media-observatory-continues-its-activities`.
- `read_url` sur cette URL : HTTP 200, titre « European Digital Media Observatory continues its activities », dernière mise à jour 4 mai 2026.
- Extrait primaire : « The consortium which will manage EDMO’s activities is led by the European University Institute in Florence (Italy) and includes the Athens Technology Center (Greece), GLOBSEC (Slovakia), MEDEA (Belgium) and the Fact-Checking Factory (Italy). »
- Locator exact de type section/paragraphe non enregistré dans la trace initiale. L'extrait prouve le lien institutionnel, mais ne permet pas de valider L2 après coup.
- Trois recherches web ciblées ont été tentées. `web_search` n'a retourné aucun résultat exploitable ; cette absence est classée comme limite de l'outil, pas comme réfutation.
- Mnemolite contenait des faits EDMO connexes, mais aucun fait `CONFIRME` explicite sur ce couple. Ils n'ont pas été utilisés comme preuve.
- Le record local et l'URL de remplacement convergent ; l'URL de remplacement a été lue directement.

## Verdict

```text
EPI              : FACT
NIVEAU           : L1, source officielle lue ; locator L2 non établi
GAP_TYPE         : ANCHOR_NON_ESTABLISHED pour L2, aucun gap pour L1
VERIFICATION     : VERIFIE
MEMORY_ID        : 9bb04db0-d4c2-4800-adf0-da00924cd075
WRITE_MNEMOLITE  : effectué en status:VERIFIE
CONFIRMATION     : interdite sans recoupement indépendant
```

Le statut SQLite `FACT`, la confiance `HIGH` et `PUBLICATION_SAFE=YES` n'ont pas servi de preuve. La preuve utilisée est l'extrait de la page institutionnelle de la Commission européenne. Le claim probant est borné à : « la Commission indique que l'Athens Technology Center fait partie du consortium chargé des activités d'EDMO ». La qualification temporelle ou éditoriale supplémentaire du record n'est pas transférée sans présence dans l'extrait. Le write-back porte `status:VERIFIE`, la date, l'URL utilisée, l'URL initiale, l'extrait et le `RECORD_ID` SQLite.

## Suite nécessaire

Pour atteindre L2, ajouter un locator exact et rejouable. Pour atteindre `status:CONFIRME`, atteindre ensuite L3 avec au moins une famille de provenance indépendante, lire sa source, puis appliquer la contre-recherche L4. En l'état, la mémoire est consommable comme fait `VERIFIE` à source unique, pas comme fait ancré ni confirmé par recoupement.
