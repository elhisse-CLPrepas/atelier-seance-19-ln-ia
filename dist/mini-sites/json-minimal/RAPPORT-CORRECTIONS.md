# Corrections du laboratoire JSON — 25 novembre 2026

## Résultat

Mini-site minimal enrichi pour S19 du 27 novembre : recherche, catégorie, compteur, six scénarios, import, aperçu JSON, copie avec solution de repli et export. Les boutons de la page de préparation PWA ont également été contrôlés.

## Défauts traités

- Ouverture en file:// : l’ancien fetch pouvait échouer. Mode de lecture locale explicite avec exemple intégré et consigne HTTP pour lire le vrai fichier.
- Recharges concurrentes : annulation et numéro de requête pour empêcher un résultat ancien de remplacer le dernier.
- Chargement réseau bloqué : délai maximal de dix secondes et nouvelle tentative.
- Données parsables mais incorrectes : contrôle du tableau et des trois chaînes non vides avant affichage.
- États difficiles à provoquer : scénarios accessibles sans modifier le JSON d’origine.
- Recherche et filtrage : normalisation des accents et de la casse, remise à zéro et message sans résultat.
- Ressources et commandes : export désactivé après erreur ; copie de secours lorsque le presse-papiers n’est pas disponible.

## Fichiers

index.html, js/app.js, css/styles.css et README.md modifiés ; js/demo-data.js, ce rapport et les résultats de tests ajoutés. data/projets.json et preparation-pwa.html conservés. Source C: inchangée.

Sauvegarde préalable : `docs/sauvegardes/mini-site-json-avant-correction-2026-11-25.zip` à la racine du projet.

## Vérification

26 contrôles automatisés réussis, utilisant les scripts réels dans un DOM simulé : recherche, filtre, recharge, scénarios, reprise après erreur, import valide/invalide/trop volumineux, copie et repli, export, concurrence, mode fichier et commandes de préparation PWA. Détails dans resultats-tests.json. Contrôles complémentaires dans resultats-fichiers.json.

Cette vérification ne constitue pas une recette visuelle dans un navigateur. Mobile, focus réel, sélection du presse-papiers et téléchargement effectif restent à vérifier sur le poste utilisateur. Aucun test PWA active ni publication effectué. Le pack V3 antérieur reste inchangé ; ce correctif porte sur le dossier explicitement demandé.
