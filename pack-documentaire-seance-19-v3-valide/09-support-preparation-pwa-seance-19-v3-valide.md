# Préparation PWA — Comprendre avant d’intégrer en S20

**Séance :** vendredi 27 novembre 2026 · Semaine 10 · Module 05  
**Édition :** automne V3 du 25 novembre 2026 · **Statut du pack :** VALIDÉ POUR PRÉPARATION ET UTILISATION EN S19  
**Pilotage :** Prof. Abderrahman EL HISSE · LAB-NUMÉRIQUE-IA

## Point de départ

En S19, la V2 charge le JSON et rend visibles les quatre états. Une PWA, ou application web progressive, ajoute des composants et des comportements à contrôler. Un affichage mobile ou un fichier manifeste ne prouve pas le fonctionnement hors connexion.

| Composant | Fonction | Travail préparatoire S19 | Essai à prévoir en S20 |
|---|---|---|---|
| Manifeste | Décrire identité et lancement | Choisir nom, nom court, start_url et scope | Chemins, icônes et prise en compte navigateur |
| Icônes | Identifier l’application | Prévoir des images autorisées | Dimensions, formats, rendu |
| Service worker | Traiter des événements et requêtes dans son périmètre | Repérer son rôle et sa portée | Enregistrement, activation, périmètre |
| Cache | Conserver certaines ressources | Sélectionner le noyau public utile | Ressources réellement disponibles et mise à jour |
| Page de repli | Expliquer une navigation indisponible | Rédiger le message attendu | Navigation hors connexion hors cache |
| localhost / HTTPS | Contexte nécessaire aux usages concernés | Distinguer local et hébergement public | Contexte sécurisé et absence d’erreurs |

## Chaîne de compréhension

URL → requête HTTP → réponse et statut → parsing JSON → contrôle des champs → création DOM → état visible. Le cache introduira une autre provenance possible de la réponse : il faudra savoir quelle version est servie.

## Fiche de préparation

Nom public : __________ · Nom court : __________.
Racine et périmètre envisagés : __________.
Ressources publiques utiles sans réseau : __________.
Ressources distantes qui pourraient manquer : __________.
Message de repli : __________.
Version de cache envisagée : __________.

En S19, aucun enregistrement de service worker n’est exigé. Une ancienne application enregistrée sur la même origine peut perturber les essais : faire vérifier son périmètre par le formateur.

## Protocole à préparer pour S20

Conserver une copie de V2 ; intégrer les composants dans une nouvelle version ; contrôler les chemins ; charger en ligne ; vérifier le service worker actif ; couper le réseau ; recharger ; essayer une navigation non cachée ; revenir en ligne ; modifier une ressource et la version ; observer la mise à jour. Ne supprimer que les anciens caches de cette application.

Ces essais sont futurs : laisser leurs résultats à renseigner. La possibilité d’installation dépend aussi du navigateur et de la plateforme. cPanel reste un contexte de déploiement ultérieur, soumis à une décision distincte.
