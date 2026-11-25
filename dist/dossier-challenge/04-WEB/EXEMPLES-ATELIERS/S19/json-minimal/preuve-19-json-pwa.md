# PREUVE 19 — EXÉCUTION JSON LOCAL ET PRÉPARATION PWA

**Date :** 27 juillet 2026  
**Projet :** Mini-site de démonstration — projets fictifs  
**Statut :** PRÊT POUR VALIDATION HUMAINE  
**Cadre :** LAB-NUMÉRIQUE-IA

## Production contrôlée

```text
index.html
css/styles.css
js/app.js
data/projets.json
README.md
```

## Résultat des prompts

| Prompt | Résultat |
|---|---|
| 19-A | trois contenus répétitifs fictifs identifiés |
| 19-B | tableau JSON de trois objets validé |
| 19-C | chargement local avec fetch() et response.ok confirmé |
| 19-D | quatre états présents dans le code |
| 19-E | aucune anomalie bloquante détectée |
| 19-F | README conservé et preuve créée |

## Données

- trois objets fictifs ;
- clés : `title`, `category`, `description` ;
- types : chaînes de caractères ;
- aucune donnée personnelle ;
- aucune clé, aucun jeton et aucun mot de passe.

## Tests réellement exécutés

| Test | Résultat |
|---|---|
| parsing JSON | réussi — 3 objets |
| syntaxe JavaScript | réussie |
| page exemple via serveur local | HTTP 200 |
| fichier JSON via serveur local | HTTP 200 — application/json |
| fichier app.js via serveur local | HTTP 200 |
| guide interactif via serveur local | HTTP 200 |
| logo local du guide | HTTP 200 — image/png |
| chemins et ressources distantes | aucune ressource distante |
| signatures de secrets | aucune détectée |

## États

- chargement : implémenté avant `fetch()` ;
- succès : implémenté après réception du tableau ;
- vide : implémenté lorsque le tableau ne contient aucun objet ;
- erreur : implémentée pour erreur HTTP, JSON invalide ou chargement impossible.

Les états vide et erreur doivent encore être simulés visuellement par le pilote humain.

## Préparation PWA

Le candidat peut expliquer le rôle futur du manifeste, du service worker, du cache et de HTTPS. Aucun composant PWA actif n’a été ajouté pendant la séance 19.

## Tests humains restant à exécuter

```text
[ ] affichage visuel ordinateur
[ ] largeur mobile
[ ] navigation clavier
[ ] focus visible
[ ] simulation tableau vide
[ ] simulation chemin JSON erroné
[ ] impression du guide
```

## Sécurité

```text
[x] données fictives
[x] aucun secret
[x] aucune API réelle
[x] aucune dépendance
[x] aucune publication
```

**Décision finale :** validation humaine requise.
