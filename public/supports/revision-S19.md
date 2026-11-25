# Révision S19

## Carte 1. Que contient un fichier JSON ?

Des données structurées, pas du JavaScript à exécuter. Une clé d’objet s’écrit entre guillemets doubles.

## Carte 2. Tableau ou objet : quelle différence ?

Un tableau [ ... ] regroupe des éléments. Un objet { ... } associe des clés à des valeurs.

## Carte 3. Syntaxe valide : schéma valide ?

Non. Le texte peut être parsable alors qu’un champ manque ou possède le mauvais type.

## Carte 4. Que renvoie await fetch(url) ?

Une réponse HTTP. Vérifiez response.ok, puis parsez le corps avec response.json().

## Carte 5. Une 404 provoque-t-elle toujours le rejet de fetch ?

Non. Il faut vérifier le statut ou response.ok. Un échec réseau peut rejeter la promesse.

## Carte 6. Pourquoi servir le JSON sur HTTP local ?

Le mode file:// peut bloquer fetch. Un serveur local fournit une origine et des réponses HTTP observables.

## Carte 7. Quels sont les quatre états ?

Chargement, succès, vide et erreur. Une liste vide n’est pas à elle seule une erreur.

## Carte 8. Pourquoi utiliser textContent ?

Pour afficher les chaînes comme du texte. Ne pas injecter des données non contrôlées avec innerHTML.

## Carte 9. Comment contrôler un lien ?

Vérifier qu’il s’agit d’un texte et que le protocole résolu est autorisé, ici HTTP ou HTTPS. Refuser javascript:.

## Carte 10. À quoi sert CORS ?

À régir certaines lectures de réponses entre origines. Le port fait partie de l’origine. CORS ne cache pas un secret.

## Carte 11. JSON, API et PHP : même chose ?

JSON est un format. Une API est une interface. PHP est exécuté par un serveur compatible et peut produire du JSON.

## Carte 12. Manifeste, service worker, cache ?

Le manifeste décrit l’application. Le service worker peut traiter des requêtes dans sa portée. Le cache conserve les ressources choisies ; les essais restent à réaliser.

# Quiz corrigé

## 1. Le serveur renvoie 404. fetch a fourni une réponse. Que faire ?

- Afficher le contenu sans vérifier
  Le corps d’erreur ne constitue pas les projets attendus.
- Tester response.ok et signaler le chemin absent · Choix attendu
  Une 404 est une réponse HTTP en erreur : le chemin est à contrôler.
- Désactiver CORS
  CORS ne répare pas une ressource absente.

## 2. Le JSON se parse, mais title vaut 42. Quel contrôle manque ?

- Le schéma attendu par l’affichage · Choix attendu
  Notre contrat exige une chaîne non vide pour title.
- La couleur du titre
  La mise en forme ne corrige pas le type de donnée.
- L’installation PWA
  La PWA ne valide pas les champs métiers.

## 3. Le serveur renvoie []. Quel message afficher ?

- Une erreur de syntaxe
  Un tableau vide est un JSON valide.
- Un succès avec les anciennes cartes
  Les anciennes cartes feraient croire que des données sont présentes.
- Une liste vide, sans anciennes cartes · Choix attendu
  Le vide est un état distinct et compréhensible.

## 4. Une description contient <img onerror=...>. Comment la montrer ?

- L’injecter dans innerHTML
  Le navigateur pourrait interpréter un balisage dangereux.
- La mettre dans textContent · Choix attendu
  textContent affiche les caractères comme du texte.
- La placer dans href
  Une description n’est pas une destination de lien.

## 5. Un lien vaut javascript:alert(1). Que faire ?

- Le refuser avant de créer le lien · Choix attendu
  Le protocole ne fait pas partie des protocoles autorisés.
- L’exécuter pour vérifier
  Le test doit vérifier le refus, sans exécuter ce code.
- Le mettre en cache
  Le cache ne neutralise pas un lien dangereux.

## 6. Le bouton PHP ne reçoit pas de JSON sous serveur Python statique. Pourquoi ?

- Le JSON nécessite une PWA
  JSON fonctionne sans PWA.
- Il faut désactiver la console
  La console aide au diagnostic.
- Ce serveur n’interprète pas PHP · Choix attendu
  PHP nécessite un serveur compatible ; la démonstration reste facultative.

## 7. localhost:8080 et localhost:8081 : même origine ?

- Oui, car le nom est identique
  Le nom d’hôte ne suffit pas : le port compte aussi.
- Non, le port diffère · Choix attendu
  L’origine comprend protocole, nom d’hôte et port.
- Oui, si le JSON est valide
  Le format de réponse ne change pas l’origine.

## 8. Quelle preuve clôt S19 dans ce périmètre ?

- Une installation PWA annoncée sans essai
  La PWA est une passerelle facultative, pas une promesse à inventer.
- Un score de quiz seul
  Le score n’atteste pas les manipulations.
- Un scénario rejoué avec attendu, observé et correction · Choix attendu
  Une trace reproductible relie compréhension, fichiers et observation.