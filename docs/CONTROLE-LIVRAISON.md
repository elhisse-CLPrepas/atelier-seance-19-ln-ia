# Contrôle de livraison · S19

Édition 1.0 · 17 novembre 2026.
Séance prévue le vendredi 27 novembre 2026. Revue pédagogique du formateur à effectuer.

## Vérifications effectuées

| Élément | Résultat observé |
| --- | --- |
| Construction Vite | `npm run build` terminé sans erreur |
| Contrôles de logique et de fichiers | 14 groupes réussis avec `npm run check` |
| Contenu | 11 rubriques, 22 diapositives, 4 cas, 12 cartes, 8 questions et 24 explications |
| Validation | 7 gestes, observation réelle, nom et date exigés avant le statut VALIDÉ |
| Ressources du mini-site | 21 fichiers locaux présents |
| Références locales HTML | 37 chemins vérifiés dans chacune des deux entrées portables et 39 dans dist/index.html |
| Dossiers des quatre cas | ZIP extraits, sommes de contrôle CRC valides, cible relative résolue depuis chaque copie |
| ZIP du moteur d’export | Texte UTF-8 et octets d’une pièce binaire relus à l’identique après extraction |
| Données saisies | Échappement HTML, refus des cibles script et des chemins sortants contrôlés |
| Carnet JSON | Schéma S19, longueurs, réponses, cartes et statut normalisés |
| Laboratoire JSON | Requêtes HTTP locales : succès, vide, 404, syntaxe invalide, type incorrect, champ absent et lien refusé contrôlés |
| Ouverture directe du laboratoire | Message de reprise par localhost contrôlé |
| PowerPoint | 22 diapositives et 22 parties de notes. Structure, géométrie et réimportation contrôlées |
| Rendu du diaporama | Les 22 images de diapositives ont été examinées. La vue 19 a été réorganisée pour garder les chemins lisibles |
| PDF | Présentation 22 pages, conducteur 3, fiche candidat 3, cas 4, guide 3 et révision 7 |
| Sources | Cadre d’automne distingué des documents historiques d’été. Les anciens statuts ne valident pas cette édition |

Les contrôles des cas portent sur l’existence des fichiers et la résolution de leurs chemins. Ils ne constituent pas un essai lecteur. Les observations personnelles du candidat restent vierges.

Le test du laboratoire exécute les requêtes HTTP et la logique de traitement avec une simulation minimale des éléments de page. Il ne vérifie pas le rendu graphique.

## Essais à réaliser sur le poste d’animation

Le navigateur de contrôle était indisponible pendant cette édition. Le parcours interactif complet et son rendu sur téléphone n’ont donc pas été vérifiés dans un navigateur.

1. Ouvrir `OUVRIR-SEANCE-19.html` après extraction complète. Parcourir les onze rubriques.
2. Projeter les vues, essayer les flèches, les notes, le plein écran et Échap.
3. Charger Déclic Web, exporter le dossier, le déplacer et ouvrir la fiche depuis sa page.
4. Saisir un projet personnel, joindre une fiche autonome, exporter puis rouvrir page et preuve.
5. Sauvegarder le carnet JSON, le reprendre et sélectionner de nouveau la fiche importée.
6. Essayer cartes, quiz et revue. Vérifier qu’un dossier incomplet ne devient pas VALIDÉ.
7. Ouvrir le laboratoire depuis localhost et relever les sept scénarios.
8. Vérifier les téléchargements, la lecture sur téléphone et l’ouverture du PPTX dans PowerPoint. Les polices natives n’ont pas été vérifiées dans PowerPoint. Le PDF conserve le rendu examiné.

## Périmètre de diffusion

La sortie `dist` et les entrées portables sont livrées. Aucune publication externe n’a été exécutée. L’indexation reste désactivée tant que l’adresse publique réelle n’est pas renseignée. Aucun service worker n’est actif. La PWA reste un prolongement à concevoir et tester.
