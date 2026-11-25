# Inventaire de contenus — V2 JSON et future PWA

**Séance :** vendredi 27 novembre 2026 · Semaine 10 · Module 05  
**Édition :** automne V3 du 25 novembre 2026 · **Statut du pack :** VALIDÉ POUR PRÉPARATION ET UTILISATION EN S19  
**Pilotage :** Prof. Abderrahman EL HISSE · LAB-NUMÉRIQUE-IA

## Deux étapes distinctes

Le socle S19 utilise trois objets fictifs. Des cartes supplémentaires, flashcards et filtres peuvent enrichir une autre version après maîtrise des quatre états. La PWA et son cache se préparent pour S20.

| Ressource | S19 | Préparation S20 |
|---|---|---|
| index.html | Point d’entrée fonctionnel | Candidat au noyau hors connexion |
| assets/styles.css ou css/styles.css | Mise en forme locale | Vérifier chemin et version |
| js/app.js | fetch, contrôles et états | Prévoir une stratégie de mise à jour |
| data/projets.json | Trois objets publics ou fictifs | Définir fraîcheur et comportement sans réseau |
| Images réellement utilisées | Locales et autorisées | Sélectionner seulement les utiles |
| manifest.webmanifest | Fonction expliquée | Préparer identité et périmètre |
| Icônes 192 et 512 px | Non exigées pour JSON | Préparer les fichiers adaptés |
| offline.html | Message envisagé | Tester le repli réel |
| service-worker.js | Non activé | Préparer portée et cache versionné |
| Preuves et rapports | Dans le portfolio | Exclus du cache public |

## Inventaire à remplir

| Chemin réel | Utilité | Origine / droits | Public ? | Utile hors connexion ? | Décision |
|---|---|---|---|---|---|
| À COMPLÉTER | À COMPLÉTER | À COMPLÉTER | À COMPLÉTER | À COMPLÉTER | À COMPLÉTER |

Exclure secrets, coordonnées privées, dossiers candidats, sauvegardes, rapports internes et archives de travail. Ne pas mettre en cache une erreur HTTP. Ne pas précacher manuellement le fichier du service worker. Limiter le cache à l’application, versionner son nom et prévoir comment observer une mise à jour. Une ressource externe indispensable peut rendre le parcours incomplet sans réseau.

Les champs title/category/description sont le contrat commun de S19 ; toute évolution de ce contrat doit être reportée dans le code, les consignes et la preuve.
