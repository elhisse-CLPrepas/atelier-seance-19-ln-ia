# Préparer un prolongement PWA après S19

La page V1 essentielle reste indépendante de la PWA. Aucun service worker n’est enregistré automatiquement dans le mini-site ou le laboratoire livré.

## Rôles à distinguer

| Élément | Rôle | Pièce à préparer |
| --- | --- | --- |
| Manifeste | Décrit nom, lancement, affichage et icônes | manifest.webmanifest |
| Service worker | Intercepte les requêtes selon sa portée | service-worker.js |
| Cache | Stocke les ressources choisies | Nom de cache propre au projet et versionné |
| Repli | Explique une ressource indisponible | offline.html |

Un manifeste ne prouve ni l’installation ni le fonctionnement hors connexion. Prévoir localhost ou HTTPS, une portée limitée au dossier du projet et des icônes locales.

## Inventaire à compléter

| Ressource | Utile hors connexion ? | Stratégie à décider | Test réel |
| --- | --- | --- | --- |
| Page V1 | | | À tester |
| Fiche cible | | | À tester |
| CSS et JavaScript | | | À tester |
| JSON | | | À tester |
| Logo et icônes | | | À tester |

## Protocole à reprendre avec le formateur

1. Dupliquer le dossier avant intégration.
2. Choisir explicitement les ressources à conserver et le nom du cache.
3. Limiter la portée du service worker au projet. Ne supprimer que les anciens caches portant son préfixe.
4. Faire une première visite sur localhost ou HTTPS.
5. Vérifier l’activation puis couper le réseau avec les outils du navigateur.
6. Rouvrir page et fiche. Consigner chaque succès et chaque ressource absente.
7. Modifier une ressource et la version du cache, rétablir le réseau puis vérifier l’actualisation.
8. Prévoir une procédure de désactivation pour le projet et garder une copie de référence.

## Trace de décision

Périmètre choisi :

Ressources incluses :

Version du cache :

Observations hors connexion :

Observations après mise à jour :

Pilote, date et décision :

Référence : https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers
