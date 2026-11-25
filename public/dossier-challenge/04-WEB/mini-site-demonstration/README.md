# Mini-site de démonstration — Séance 17

**Version :** V1  
**Statut :** À VALIDER  
**Usage :** démonstration locale du Module 05  
**Publication :** aucune publication automatique

## Objectif

Montrer aux candidats comment HTML, CSS et JavaScript coopèrent dans une page web simple.

## Fichiers

```text
index.html                              structure et contenu
css/styles.css                          identité visuelle et responsive
js/app.js                               interaction afficher/masquer
assets/images/affiche-presentation-module-05.png
assets/images/affiche-presentation-seance-17.png  miniature commentée et agrandissable
assets/images/logo-LN-IA.png              logo officiel affiché dans l’en-tête
README.md                               mode d’emploi
```

Le visuel est une copie non modifiée de `Affiprésentation-MODULE05.png`, renommée pour un usage web compatible.

Le logo est une copie non modifiée de `logo-LN-IA.png` placé à la racine du projet. Il est chargé avec un chemin relatif et s’adapte à la largeur mobile.

L’affiche de la séance 17 est présentée sous forme de miniature afin de ne pas surcharger la page. Un bouton permet de l’agrandir dans une fenêtre accessible. La section associée commente les étapes « Observer, expliquer, appliquer » et rappelle la différence entre projet local et site publié.

## Ouvrir localement

1. ouvrir le dossier du mini-site ;
2. ouvrir `index.html` dans un navigateur moderne ;
3. vérifier que l’affiche apparaît ;
4. activer le bouton « Afficher l’explication » ;
5. ouvrir les outils de développement et observer le message informatif dans la console.

Aucun serveur, aucune installation et aucune connexion externe ne sont nécessaires pour cette démonstration.

## Interaction

Le bouton de la section « Observer un événement » :

- est un véritable bouton HTML ;
- fonctionne au clic et au clavier ;
- modifie `aria-expanded` ;
- affiche ou masque une zone locale ;
- actualise son libellé ;
- écrit un message informatif sans donnée privée dans la console.

## Scénario de démonstration — 20 minutes

1. afficher le résultat ;
2. demander ce que les candidats observent ;
3. montrer l’arborescence ;
4. relier le contenu à `index.html` ;
5. relier la présentation à `css/styles.css` ;
6. déclencher le bouton ;
7. relier l’événement à `js/app.js` ;
8. ouvrir la console ;
9. expliquer local, paquet contrôlé et publié ;
10. conclure avec la validation humaine.

## Tests à effectuer

```text
[ ] index.html s’ouvre localement
[ ] l’affiche apparaît
[ ] les trois cartes sont présentes
[ ] le bouton fonctionne à la souris
[ ] le bouton fonctionne au clavier
[ ] le texte du bouton change
[ ] la zone est affichée puis masquée
[ ] le focus est visible
[ ] la page reste lisible sur mobile
[ ] le zoom à 200 % conserve le contenu essentiel
[ ] les liens internes fonctionnent
[ ] aucune erreur critique n’apparaît dans la console
[ ] aucun chemin absolu ou secret n’est exposé
```

## Limites

- pas de JSON ;
- pas de PWA ;
- pas d’API ;
- pas de PHP ;
- pas de formulaire ;
- pas de collecte de données ;
- pas de publication.

## Contrôle humain

Le mini-site reste `À VALIDER`. Le formateur contrôle le scénario et le pilote humain décide de toute utilisation publique future.

## Intégration dans S17

Le menu donne accès aux fichiers, au dossier Challenge et au carnet d’essai. Une copie de travail se trouve dans `mon-dossier-challenge-Module05/04-WEB/mini-site-demonstration/`. Le pied de page situe les affiches d’été dans la séance d’automne ; aucune observation de candidat ni validation publique n’est prédéfinie.
