# SÉANCE 19 — APPROFONDIR : JSON LOCAL ET PRÉPARATION PWA

**Module :** 05 — De la page web simple à la mini-application statique déployable
**Semaine :** 10
**Version :** V2
**Statut :** VALIDÉ
**Date de complétion pédagogique :** 27 juillet 2026  
**Date de validation humaine :** 27 juillet 2026
**Durée indicative :** 110 minutes
**Pilotage humain :** Prof. Abderrahman El Hisse

> Cette séance sépare les données du mini-site V2 et prépare la compréhension d’une PWA statique- responsive installable adaptée au mobile. Elle ne déclenche aucune publication et n’introduit ni API privée ni secret côté navigateur.

## 1. Type de séance

Approfondissement guidé, démonstratif et pratique, avec manipulation contrôlée des données.

## 2. Intention

Faire comprendre comment séparer les données du HTML, les charger localement, gérer les principaux états d’affichage et préparer l’évolution du mini-site vers une PWA statique simple avec sw = service worker .

## 3. Résultat essentiel attendu

Le candidat structure un petit jeu de données JSON, observe son chargement dans le mini-site depuis un serveur local, rend visibles les états essentiels et identifie le rôle du manifeste, du service worker et du cache avec déployement sur serveur cPanel.

## 4. Objectifs observables

- distinguer objet, tableau, clé, valeur et type de donnée ;
- produire ou corriger un JSON valide ;
- relier les champs JSON aux éléments affichés ;
- expliquer le rôle de `fetch()` ;
- reconnaître les états chargement, succès, vide et erreur ;
- utiliser la console pour observer un chargement ;
- expliquer pourquoi `file://` ne convient pas toujours à `fetch()` ;
- identifier le rôle du manifeste, du service worker, du cache et de HTTPS ;
- distinguer PWA statique, application serveur et API ;
- conserver une preuve des tests réalisés.

## 5. Compétences visées

- structuration et validation de données ;
- séparation contenu, présentation, interaction et données ;
- lecture d’un chargement asynchrone ;
- gestion élémentaire des erreurs ;
- utilisation prudente d’un serveur local ;
- compréhension guidée des composants PWA ;
- documentation d’un test reproductible.

## 6. Prérequis

- mini-site V1 contrôlé ou copie de démonstration ;
- interaction JavaScript simple comprise ;
- contenus répétitifs identifiés ;
- bases HTML, CSS et JavaScript de la séance 18 ;
- navigateur et console utilisés avec accompagnement ;
- données fictives ou explicitement autorisées.

## 7. Matériel à prévoir

- copie contrôlée du mini-site V2 ;
- navigateur moderne et éditeur déjà disponible ;
- serveur local déjà disponible dans l’environnement ;
- serveur cPanel https://clprepas.com/
- jeu de données fictif `projets.json` ;
- grille de correspondance champs/affichage ;
- modèle de preuve 19 ;
- présentation schématique des composants PWA.

Aucune dépendance ne doit être installée pendant la séance sans autorisation.

## 8. Message d’ouverture

Séparer les données du code rend le projet plus clair, plus facile à mettre à jour et plus simple à contrôler. Une PWA n’est pas un effet visuel : c’est un ensemble de composants précis, servis dans un contexte sécurisé et testés méthodiquement.

## 9. Vocabulaire essentiel

JSON, objet, tableau, clé, valeur, chaîne, nombre, booléen, `fetch()`, promesse, requête, réponse, chargement, erreur, manifeste, service worker, cache, hors connexion, `localhost` et HTTPS.

## 10. Déroulement chronométré

| Phase | Durée | Intention | Activité |
|---|---:|---|---|
| Liaison avec la V1 | 10 min | partir d’un projet connu | repérer les contenus répétitifs et conserver une copie |
| Comprendre JSON | 20 min | structurer les données | identifier objets, tableaux, clés, valeurs et types |
| Valider les données | 15 min | prévenir les erreurs de syntaxe | corriger un jeu de données fictif |
| Charger avec `fetch()` | 20 min | relier données et affichage | lancer le projet sur serveur local et observer la console |
| Gérer les quatre états | 15 min | rendre le comportement compréhensible | tester chargement, succès, vide et erreur |
| Découvrir la PWA | 15 min | comprendre l’architecture | relier manifeste, service worker, cache, localhost et HTTPS |
| Contrôle et preuve | 15 min | reformuler et documenter | exécuter la checklist et compléter la preuve 19 |

**Total : 110 minutes.**

API, CORS avancé et PHP restent hors du socle commun. Ils peuvent être évoqués uniquement comme ouverture contrôlée.

## 11. Démonstration du formateur

À partir d’une copie du mini-site de démonstration :

1. repérer trois contenus répétitifs ;
2. présenter leur équivalent dans `projets.json` ;
3. valider la structure JSON ;
4. démarrer un serveur local déjà disponible ;
5. charger les données avec `fetch()` ;
6. montrer chargement, succès et tableau vide ;
7. provoquer une erreur de chemin et l’expliquer ;
8. présenter sans activation automatique les rôles de `manifest.webmanifest`, `service-worker.js` et d’une page hors connexion.

La démonstration utilise uniquement des données fictives et ne contient aucun jeton, mot de passe ou clé d’API.

## 12. Exercice guidé

Le groupe reçoit trois objets fictifs. Il identifie les clés communes, vérifie les types, corrige deux erreurs de syntaxe, associe chaque clé à une zone du mini-site et prévoit le message à afficher si le tableau est vide.

## 13. Manipulation du candidat

Le candidat duplique sa V1 dans un dossier de travail V2, sélectionne des données non sensibles, adapte `data/projets.json`, valide le JSON, relie les champs à l’affichage, lance le serveur local autorisé, observe les quatre états, corrige les anomalies comprises et complète la preuve 19.

## 14. Exemple commenté

L’exemple technique du futur pack doit rester minimal :

```text
mini-site-v2/
├── index.html
├── assets/
├── data/
│   └── projets.json
├── js/
│   └── app.js
└── README.md
```

Il montrera trois objets fictifs, une zone d’état visible et une gestion d’erreur compréhensible. Le manifeste et le service worker seront présentés séparément comme préparation guidée de la séance 20.

## 15. Prompt de production

Un pack de prompts 19-A à 19-F est recommandé après validation de cette séance :

- 19-A : auditer la V1 et choisir les données ;
- 19-B : proposer puis valider la structure JSON ;
- 19-C : intégrer le chargement local ;
- 19-D : traiter chargement, succès, vide et erreur ;
- 19-E : auditer sans modifier ;
- 19-F : compléter README et preuve 19.

Les prompts devront interdire les secrets, les données réelles non autorisées, les dépendances nouvelles et la publication automatique.

## 16. Erreurs fréquentes à traiter

- virgule finale ou guillemet manquant ;
- confusion entre objet et tableau ;
- clés incohérentes ou type inattendu ;
- chargement direct avec `file://` ;
- chemin relatif incorrect ;
- absence de vérification de la réponse ;
- erreur masquée ou interface vide sans message ;
- ressource distante indispensable ;
- secret placé dans le navigateur ;
- confusion entre PWA et application serveur.

## 17. Procédure de test

- valider la syntaxe JSON et l’origine autorisée des données ;
- démarrer le serveur local sans installation nouvelle ;
- charger la page et observer la console ;
- vérifier chargement, succès, tableau vide et erreur contrôlée ;
- vérifier les chemins relatifs et l’absence de secret ;
- identifier les composants PWA attendus sans les déclarer fonctionnels avant test ;
- consigner chaque résultat dans la preuve 19.

## 18. Critères de contrôle

- JSON valide et lisible ;
- champs cohérents avec l’affichage ;
- chargement compris et reproductible ;
- quatre états visibles ou documentés ;
- erreur expliquée ;
- aucune donnée sensible ;
- différence entre `file://`, `localhost` et HTTPS comprise ;
- rôle des composants PWA reformulé ;
- aucun résultat PWA annoncé sans test ;
- preuve datée et complète.

## 19. Livrable et preuve

```text
05-web/mini-site-v2/data/projets.json
05-web/mini-site-v2/js/app.js
05-web/preuve-19-json-pwa.md
```

Statut attendu : `À VALIDER`.

Le mini-site V2 reste local pendant cette séance. Aucune publication n’est autorisée par ce document.

## 20. Préparation de la séance 20

- vérifier le mini-site V2 et les états d’affichage ;
- préparer les ressources locales ;
- sélectionner les ressources utiles hors connexion ;
- préparer un manifeste minimal et un service worker guidé avec cache versionné ;
- dresser la liste des tests et conserver une copie avant intégration ;
- ne rien publier sans validation distincte.

## Décisions validées par le pilote humain

```text
[x] jeu de démonstration fictif : projets.json
[x] serveur local déjà disponible, sans installation pendant la séance
[x] PWA limitée à une découverte guidée en séance 19
[x] manifeste et service worker intégrés en séance 20
[x] API, CORS avancé et PHP hors du socle commun
[x] modèle de preuve 19 à produire dans le futur pack
[x] prompts 19-A à 19-F à produire après validation
```

**Fin du document — V2 validé par le pilote humain.**
