# CAHIER DES CHARGES — PWA MÉTIER MINIMALE — SÉANCE 19

**Version :** V1  
**Statut :** À VALIDER

## Objectif

Produire une mini-application statique adaptée à l’activité du candidat. Elle présente 6 à 12 contenus autorisés, génère des cartes et des flashcards depuis un JSON local, gère les principaux états et reste utile hors connexion après une première visite réussie.

## Arborescence minimale

```text
mini-application-pwa-v1-a-valider/
├── index.html
├── offline.html
├── manifest.webmanifest
├── service-worker.js
├── css/styles.css
├── js/app.js
├── data/data.json
├── assets/icons/icon-192.png
├── assets/icons/icon-512.png
├── README.md
└── preuve-19-json-pwa.md
```

## Exigences fonctionnelles

- présenter l’activité et sa valeur pour le public cible ;
- charger `./data/data.json` avec `fetch()` ;
- valider le tableau, le schéma et les types ;
- générer cartes et flashcards sans injection HTML non fiable ;
- afficher chargement, succès, vide et erreur avec Réessayer ;
- rester navigable au clavier et lisible sur mobile ;
- proposer une page hors connexion compréhensible ;
- conserver uniquement des ressources statiques publiques dans le cache.

## Exigences PWA

- manifeste JSON valide ;
- `start_url` et `scope` égaux à `./` ;
- icônes PNG 192 × 192 et 512 × 512 ;
- service worker enregistré sur `localhost` ou HTTPS ;
- nom de cache versionné ;
- installation du cache avec attente correcte des écritures ;
- suppression limitée aux anciennes versions de cette application ;
- aucune réponse HTTP en erreur mise en cache ;
- comportement hors connexion réellement testé.

## Tests minimaux

- JSON valide, succès, vide, 404 et schéma invalide ;
- clavier, contraste, réduction des animations et largeur 320 px ;
- manifeste et icônes visibles dans les outils du navigateur ;
- périmètre du service worker contrôlé ;
- rechargement hors connexion après première mise en cache ;
- retour en ligne et mise à jour du cache vérifiés ;
- console sans erreur critique.

## Limites

Le cœur fonctionne sans API, PHP ni Bootstrap. L’installation dépend du navigateur et ne doit pas être promise. La publication reste interdite sans validation humaine.
