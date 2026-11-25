# SUPPORT EXPLICATIF ET PRATIQUE — PRODUIRE UNE PWA

## Séance 19 — Comprendre, construire et tester

**Version :** V1  
**Statut :** À VALIDER  
**Date :** 3 août 2026
**Pilotage humain :** Prof. Abderrahman El Hisse

## 1. Objectif pédagogique

Le candidat part de son activité et d’un mini-site V1. Il construit une copie V2 qui sépare les données de l’interface, puis ajoute les composants minimaux d’une PWA statique. Il doit expliquer chaque composant et prouver les tests effectués.

## 2. Chaîne de compréhension Web

```text
URL demandée
→ requête HTTP
→ réponse et statut HTTP
→ fichier JSON converti en données JavaScript
→ validation du schéma
→ création d’éléments dans le DOM
→ interface affichée
```

Une API peut aussi fournir du JSON, mais le cœur de l’exercice utilise un fichier local. CORS contrôle certaines requêtes entre origines ; il ne protège pas un secret. PHP s’exécute sur un serveur, jamais directement dans le navigateur.

## 3. De quoi partir ?

Le minimum utile est : une activité claire, un public cible, une V1 sauvegardée, une V2 modifiable, des contenus publics, un logo, un navigateur, un éditeur et un serveur local. Les candidats sans V1 peuvent adapter le démonstrateur de l’atelier en conservant son architecture et en remplaçant uniquement les contenus autorisés.

## 4. Le manifeste

`manifest.webmanifest` décrit l’identité et le lancement de l’application. Il ne crée pas à lui seul le mode hors connexion.

```json
{
  "name": "Nom public de mon activité",
  "short_name": "Nom court",
  "start_url": "./",
  "scope": "./",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#071631",
  "icons": [
    {"src":"./assets/icons/icon-192.png","sizes":"192x192","type":"image/png"},
    {"src":"./assets/icons/icon-512.png","sizes":"512x512","type":"image/png"}
  ]
}
```

## 5. Le service worker

Le service worker est séparé de la page. Son cycle principal est : enregistrement, installation, activation et interception des requêtes. Il fonctionne sur `localhost` ou en HTTPS.

Le candidat doit pouvoir repérer dans son code :

- le nom versionné du cache ;
- la liste limitée des ressources initiales ;
- l’attente des écritures du cache ;
- la suppression des seules anciennes versions de cette application ;
- la réponse de secours hors connexion.

## 6. Stratégie de cache minimale

Pour cette séance, mettre en cache l’enveloppe statique stable : page d’accueil, page hors connexion, CSS, JavaScript, JSON public, logo et icônes. Ne jamais mettre en cache des données privées, des jetons ou des réponses d’erreur.

Une stratégie simple ne garantit pas que toutes les fonctionnalités distantes fonctionneront hors connexion. Si Bootstrap ou une autre ressource vient d’un CDN, elle peut manquer hors connexion ; une copie locale validée est préférable si elle est indispensable.

## 7. Procédure de manipulation

1. Lancer le projet avec un serveur local.
2. Vérifier que toutes les ressources répondent correctement.
3. Contrôler le manifeste et les icônes dans les outils du navigateur.
4. Enregistrer le service worker et contrôler son périmètre.
5. Charger l’application une première fois en ligne.
6. Activer le mode hors connexion dans les outils du navigateur.
7. Recharger et observer les ressources disponibles.
8. Tester également un chemin non mis en cache et la page de secours.
9. Revenir en ligne, modifier la version du cache si nécessaire et vérifier la mise à jour.
10. Inscrire uniquement les résultats observés dans la preuve 19.

## 8. Dépannage

| Symptôme | Vérification |
|---|---|
| `fetch()` échoue par double-clic | lancer un serveur local |
| ancienne version affichée | inspecter le service worker et le nom du cache |
| icône absente | contrôler format, dimensions et chemin relatif |
| manifeste ignoré | contrôler syntaxe JSON, type et lien dans `head` |
| hors connexion incomplet | vérifier la liste du cache et les ressources distantes |
| service worker absent | vérifier HTTPS/localhost, console et périmètre |

## 9. Critères de maîtrise

```text
[ ] j’explique la chaîne requête → réponse → JSON → DOM
[ ] j’explique manifeste, service worker et cache
[ ] je sais pourquoi localhost ou HTTPS est nécessaire
[ ] je peux montrer mon JSON et son schéma
[ ] je peux provoquer et expliquer les états d’erreur
[ ] je peux démontrer un test hors connexion réel
[ ] je connais les limites de ma PWA
[ ] je n’ai publié aucune donnée privée
```

## 10. Passage à la suite

La séance 20 peut approfondir la personnalisation, l’installation multi-appareils, les tests responsive, l’optimisation des icônes et la préparation contrôlée au déploiement. La séance 19 doit déjà produire une PWA locale minimale lorsque les prérequis sont réunis.

**Statut maximal : PRÊT POUR VALIDATION HUMAINE.**
