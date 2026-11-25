# Contrôle du pack Déclic Web — S18 V1

Date : 23 novembre 2026 · Agent : Codex · Environnement : Windows, Chrome de test isolé, ouverture file:// d’un ZIP extrait dans un autre emplacement. Revue du pilote : **À examiner**.

## Contrôles exécutés par l’agent

| Vérification | Méthode et environnement | Résultat observé | Statut | Suite |
| --- | --- | --- | --- | --- |
| Structure, liens et ancres | Analyse des trois pages HTML et des fichiers locaux | Six sections, identifiants uniques, toutes les cibles présentes dans le pack | Réussi | Refaire après modification |
| Syntaxe JavaScript | node --check js/app.js | Aucune erreur de syntaxe | Réussi | Refaire après modification |
| Ouverture après extraction | Chrome, file://, copie extraite dans tmp/qa | Page et images affichées ; fiche principale et fiche source ouvertes | Réussi | Essai personnel à compléter |
| Explication au clavier | Focus sur le bouton, Entrée deux fois | Zone ouverte puis refermée ; aria-expanded et libellé actualisés | Réussi | Essayer aussi sur votre appareil |
| Affiche et focus | Tab, Entrée, Échap, bouton Fermer | Dialogue ouvert puis fermé ; focus revenu au bouton d’ouverture | Réussi | Essai lecteur d’écran restant |
| Quiz de trois questions | Aucune réponse, trois erreurs, trois réponses correctes, modification, remise à zéro | 0/3 et 3/3 cohérents ; correction visible ; ancien résultat invalidé ; réponses effacées au reset | Réussi | Le score ne valide pas le projet |
| Mise en page adaptable | Captures et mesure du débordement à 390, 720 et 1440 px | Aucun débordement horizontal de la page | Réussi | Appareils physiques non essayés |
| Équivalent layout 200 % | 720 px CSS et facteur d’échelle 2, surface physique 1440 px | Sections conservées sans débordement | Réussi | Simulation, distincte du zoom réel du navigateur |
| Zoom via menu du navigateur à 200 % | Non réalisé par le protocole de test | Non exécuté | Non exécuté | Activer 200 % dans votre navigateur, puis contrôler les textes et boutons |
| Fonctionnement sans réseau | Requêtes http/https bloquées, ouverture locale | Aucune requête externe ; page, affiche et interactions fonctionnent | Réussi | Débrancher le réseau pour votre essai personnel |
| Exceptions JavaScript | Écoute des exceptions pendant le scénario | Aucune exception applicative | Réussi | Garder un contrôle de la console après modification |
| Archive finale | Contrôle CRC, extraction distincte et comparaison SHA-256 avec le dossier livré | Dix fichiers identiques, dossier racine unique, ZIP extérieur au dossier | Réussi | Refaire après toute correction |
| Entrées originales | Comparaison des empreintes conservées dans ENTREES-SHA256.json | Les huit fichiers de démarrage et d’entrée restent inchangés | Réussi | Conserver les originaux |

Les captures desktop-accueil.png, mobile-accueil.png, zoom-200.png et le rapport JSON sont conservés dans tmp/qa/declic-web-S18 du poste de production, hors du pack. La version du navigateur figure dans ce rapport. Les contrôles automatiques ne remplacent pas une revue d’accessibilité complète.

## Essais du participant et du binôme — à renseigner

- Nom ou initiales : À compléter.
- Date et appareil : À compléter.
- Résultat d’ouverture du ZIP extrait : À compléter.
- Action principale, images, documents et interactions : À compléter.
- Clavier et zoom réel 200 % : À compléter.
- Observation, correction et réouverture : À compléter.

## Revue humaine et S19

Pilote, date et décision : À compléter. Statut : **À examiner**. Lecteur d’écran, appareils physiques et zoom réel à 200 % restent à essayer. Reprendre ces points en S19 avec les éventuelles anomalies personnelles ; aucun résultat humain n’a été inventé.
