# Mini-site autonome — Séance 19 — V2

**Version :** V2
**Statut :** À VALIDER
**PWA active :** non

## Objectif

Présenter la séance 19 indépendamment de la construction complète d’une PWA. L’application permet d’observer et manipuler :

- JSON et validation du schéma ;
- `fetch()`, requête, réponse et statut HTTP ;
- chargement, succès, tableau vide et erreur ;
- création DOM sûre ;
- cartes et flashcards accessibles ;
- scénarios 404, schéma invalide et lien dangereux ;
- différence entre JSON local, API, CORS et PHP ;
- passerelle facultative vers les notions PWA.

## Lancement principal

Le serveur confirmé pour l’atelier utilise le port **8080**.

Dans PowerShell, ouvrir le dossier de l’application :

```powershell
cd "C:\DEV\CHALLENGE-01-Juin-2026\05-PROGRAMME-PEDAGOGIQUE\MODULE-05\05-EXEMPLES-CODE\mini-site-seance-19-V2"
```

Lancer ensuite le serveur statique :

```powershell
python -m http.server 8080 --bind 127.0.0.1
```

Ouvrir ensuite :

```text
http://127.0.0.1:8080/
```

`http://localhost:8080/` fonctionne également dans la plupart des environnements.

Un serveur local déjà installé dans l’éditeur peut être utilisé. L’ouverture directe avec `file://` peut bloquer `fetch()`.

## Démonstration PHP facultative

Le cœur fonctionne sans PHP. Pour tester `api.php`, utiliser un serveur PHP déjà disponible :

```powershell
php -S 127.0.0.1:8080
```

Arrêter d’abord le serveur Python avec `Ctrl+C`, car deux serveurs ne peuvent pas utiliser simultanément le port 8080.

Avec Python, le bouton de test PHP affiche volontairement que PHP n’est pas interprété. Avec le serveur PHP, il doit afficher une réponse JSON produite côté serveur.

## Vérification rapide

Après le lancement, contrôler ces adresses :

```text
http://127.0.0.1:8080/
http://127.0.0.1:8080/data/projets.json
http://127.0.0.1:8080/js/app.js
http://127.0.0.1:8080/css/styles.css
```

Résultats attendus : page visible, six ressources chargées, filtres présents et aucun message d’erreur critique dans la console.

Si le port 8080 est déjà occupé, arrêter l’ancien serveur dans son terminal avec `Ctrl+C` avant de relancer la commande.

## Parcours recommandé

1. Observer la chaîne URL → requête → réponse → JSON → validation → DOM.
2. Charger les six ressources et utiliser les filtres.
3. Ouvrir l’aperçu JSON.
4. Exécuter les sept scénarios : succès, vide, 404, JSON invalide, réponse non-tableau, schéma invalide et lien dangereux.
5. Tester les flashcards à la souris puis au clavier.
6. Comparer JSON local, API et PHP.
7. Compléter la preuve 19.
8. Consulter `preparation-pwa.html` uniquement comme prolongement.

## Fonctionnalités opérationnelles

- indicateur navigateur en ligne ou hors connexion ;
- bouton Réessayer après une erreur ;
- aperçu de la réponse ou du message d’erreur ;
- fichier JSON original jamais modifié par le laboratoire ;
- test PHP facultatif avec explication adaptée au serveur utilisé.

## Sécurité et limites

- données fictives et pédagogiques ;
- aucune clé ou donnée personnelle ;
- aucun contournement de CORS ;
- aucun manifeste ou service worker actif ;
- aucune installation PWA ;
- aucune publication automatique.

**Statut maximal :** `PRÊT POUR VALIDATION HUMAINE`.
