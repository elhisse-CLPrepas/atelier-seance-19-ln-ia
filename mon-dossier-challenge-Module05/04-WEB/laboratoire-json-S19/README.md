# Laboratoire JSON S19 · LN-IA

Approfondissement guidé après la page V1. Aucun service worker actif.

## Lancer

Depuis ce dossier, avec Python déjà disponible :

```sh
python -m http.server 8000
```

Ouvrir http://localhost:8000/. Arrêter le serveur avec Ctrl+C.
Une ouverture file:// affiche la procédure de reprise sans rester bloquée sur Chargement.

## Manipuler

Modifier le titre du premier objet dans data/projets.json. Recharger les données et retrouver le titre dans la carte. Les valeurs s’affichent avec textContent. Le code vérifie la réponse HTTP, le tableau, les champs requis, l’unicité des identifiants et les liens relatifs vers pieces/.

## Sept scénarios

Succès, vide, HTTP 404, syntaxe JSON invalide, objet au lieu de tableau, champ manquant, lien non autorisé. data/absent.json manque volontairement pour le test HTTP. Ces scénarios correspondent à quatre états : chargement, succès, vide et erreur.

Le journal conserve le dernier essai à l’écran. Copiez votre observation dans preuve-laboratoire-json.md. Une erreur attendue dans le laboratoire ne vaut pas validation de la V1 du candidat.

## Préparer la PWA

Repérer les ressources à garder hors connexion, décrire manifeste, portée du service worker et cache versionné, puis prévoir visite initiale, coupure de réseau et mise à jour. Aucun résultat d’installation ou hors connexion n’est annoncé dans cette édition.

Sources : supports d’été S19 fournis et https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
