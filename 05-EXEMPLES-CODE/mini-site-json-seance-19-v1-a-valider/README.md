# Laboratoire JSON local — S19 du 27 novembre 2026

Version corrigée et enrichie du 25 novembre 2026. Le nom du dossier historique reste conservé.

## Ouvrir

Depuis ce dossier, avec Python déjà disponible :

```powershell
python -m http.server 8080 --bind 127.0.0.1
```

Ouvrir http://127.0.0.1:8080/ puis arrêter avec Ctrl+C. Si le port est occupé, choisir un autre port et adapter l’adresse.

Le double-clic sur index.html ouvre un mode de lecture avec données intégrées explicitement signalé. Ce mode ne relit pas automatiquement data/projets.json. Pour voir une modification du fichier, utiliser le serveur HTTP ou importer le JSON.

## Commandes

- Recharger les données : efface les filtres et relit le fichier en HTTP, sans cache ; en mode fichier, restaure l’exemple intégré.
- Recherche : titre, catégorie et description ; ignore accents, casse et espaces en début/fin.
- Catégorie et Effacer les filtres : affiner ou retrouver l’ensemble des cartes.
- Lancer le test : succès, délai pédagogique, tableau vide, chemin absent, syntaxe invalide ou champs invalides.
- Rétablir les données : quitte les simulations et recharge la source.
- Réessayer : rejoue la dernière opération après une erreur.
- Importer : lit un fichier JSON local de 1 Mo maximum sans modifier le disque.
- Copier : utilise le presse-papiers ou sélectionne le texte si l’autorisation manque.
- Exporter : télécharge les données validées ; désactivé pendant un chargement ou après une erreur.
- Préparation PWA : explication du manifeste, parcours du service worker, cache simulé, contexte sécurisé et inventaire.

## Correction de la recharge

L’ancienne page utilisait fetch même en file://, ce qui peut être bloqué par le navigateur. La nouvelle page distingue lecture locale et requête HTTP. Une réponse HTTP en erreur ou un JSON invalide affiche un diagnostic ; un bouton permet de réessayer. Les requêtes précédentes sont annulées et leurs résultats ignorés après une nouvelle commande. Une limite de dix secondes évite le chargement réseau indéfini.

## Données et tests

Contrat : tableau d’objets avec title, category et description, trois chaînes non vides. Les textes sont insérés avec textContent. Aucun service worker, compte, collecte ou API distante.

data/projets.json est la source en mode serveur. js/demo-data.js est sa copie initiale pour la découverte en mode fichier et les simulations ; après une évolution éditoriale, maintenir cette copie ou importer le fichier à jour.

Voir RAPPORT-CORRECTIONS.md et resultats-tests.json. Les tests Node exécutent les scripts réels dans un DOM simulé ; le contrôle visuel, le clavier réel et les téléchargements dans un navigateur restent à vérifier sur le poste utilisateur.

L’import initial intact a été sauvegardé avant correction dans docs/sauvegardes à la racine du projet. Les sources C: n’ont pas été modifiées.
