# Recette du démonstrateur PWA S20

Statut initial : À VALIDER par un essai réel dans votre navigateur.
Ce dossier contient uniquement trois cas fictifs. Aucune donnée personnelle n’est demandée.

## 1. Servir le dossier

Avec Python déjà installé, ouvrez un terminal dans app-module-05 puis lancez :

```sh
python -m http.server 8000
```

Ouvrez http://localhost:8000/ . Si le dossier est servi depuis le pack complet, ouvrez le chemin exact vers public/approfondissement/app-module-05/ . Le double-clic file:// ne permet pas de contrôler une PWA.

## 2. Première lecture en ligne

Ouvrez les trois fiches. Relevez le titre, l’adresse et le résultat. Activez « Activer l’essai PWA ». Attendez l’installation du worker puis rechargez. Relevez la portée affichée et vérifiez que la page est contrôlée.

Dans les outils du navigateur, inspectez Application / Manifest, Service Workers et Cache Storage (intitulés variables). Le cache porte un préfixe incluant la portée du dossier, suivi de v1. Les icônes de 192 et 512 px sont fournies.

## 3. Hors connexion réel

Après la visite en ligne et un rechargement sous contrôle du worker, passez en mode hors connexion dans les outils du navigateur. Rechargez. Vérifiez les trois cartes et ouvrez une fiche. Un indicateur navigator.onLine ne suffit pas à prouver ce fonctionnement.

Demandez ensuite une adresse absente, par exemple inconnue.html dans ce même dossier. Le repli « Cette adresse n’est pas en cache » doit s’afficher avec un retour vers la racine de l’application.

## 4. Mise à jour

Revenez en ligne. Dans data/projets.json, changez un titre sans modifier sa clé ni son chemin. Dans service-worker.js, changez VERSION de v1 en v2. Sauvegardez les fichiers. Cliquez « Rechercher une mise à jour ». Quand la nouvelle version attend, cliquez « Appliquer la nouvelle version ». La page se recharge.

Le nouveau worker ne s’impose pas automatiquement. Vérifiez la nouvelle donnée, le cache v2 et la suppression des seuls caches anciens de cette portée. Repassez hors connexion et rechargez. Relevez ce qui reste disponible.

## 5. Installation et nettoyage

Le bouton d’installation s’affiche seulement si le navigateur propose cet événement. Consignez « non proposé dans ce navigateur » si nécessaire. Un manifeste correct ne garantit pas l’offre d’installation.

Pour terminer l’essai, désinscrivez uniquement le worker de cette portée et supprimez uniquement ses caches depuis les outils du navigateur. Rechargez en ligne. Ne supprimez pas les données des autres applications du domaine.

## 6. Grille à compléter

| Essai | Attendu | Observé | Date et navigateur | Décision |
| --- | --- | --- | --- | --- |
| Première lecture | 3 cartes et 3 bonnes fiches | | | |
| Portée | Dossier app-module-05 seulement | | | |
| Page contrôlée | Contrôleur après activation et rechargement | | | |
| Cache | Ressources prévues dans le cache de cette portée | | | |
| Hors connexion | Page et fiche déjà précachées lisibles | | | |
| Adresse inconnue hors ligne | Repli puis retour à l’accueil du dossier | | | |
| Retour en ligne | Donnée reçue sans blocage | | | |
| Mise à jour | v2 appliquée après décision, ancienne version isolée supprimée | | | |
| Second essai hors ligne | Nouvelle donnée accessible | | | |
| Installation | Résultat ou indisponibilité consignée | | | |
| Clavier et mobile | Navigation, focus et lecture utilisables | | | |

Pilote :
Écarts :
Décision datée :

## Stratégie livrée

Le worker n’intercepte que GET, même origine et dans sa portée. Les pages et le JSON utilisent le réseau d’abord puis leur cache. Les ressources statiques précachées utilisent le cache d’abord. Les écritures attendent leur achèvement. Seules les URL prévues peuvent enrichir ce cache. Les réponses HTTP en erreur ne sont pas conservées. Un repli couvre une navigation hors connexion absente du cache.

Une fiche modifiée exige une nouvelle version du cache pour remplacer sa copie statique. Les scripts, styles, images et trois fiches sont locaux. Le worker du démonstrateur n’est pas celui du mini-site d’atelier.
