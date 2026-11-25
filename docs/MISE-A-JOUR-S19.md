# Refonte S19 — JSON local, HTTP et DOM — 25 novembre 2026

La séance du vendredi 27 novembre 2026 est reconstruite autour de la compréhension des notions et mécanismes, puis de manipulations observables. La durée proposée est 110 minutes. L’horaire reste à communiquer en heure de Casablanca.

## Cadre retenu

La demande courante du pilote, la fiche seance-19-json-pwa-v2.md et le README du mini-site-seance-19-V2 explicitement validé fixent le périmètre. Les informations de SOURCES-ET-SYNCHRONISATION.md servent à distinguer les versions historiques. Le pack documentaire V3 est conservé sans modification ; son extension de périmètre n’est pas reprise comme instruction de cette refonte.

Le travail porte sur JSON et schéma, fetch et HTTP, quatre états, DOM sûr, cartes et flashcards, sept scénarios et comparaison JSON/API/CORS/PHP. L’exécution PHP reste facultative et la PWA une passerelle conceptuelle vers S20. Aucun service worker actif, installation PWA ou déploiement n’est demandé.

## Onze rubriques reconstruites

| Rubrique | Contenu et comportement |
|---|---|
| Accueil | Intention, prérequis, date, 110 minutes, quatre états et accès projection/laboratoire. |
| Présentation | 22 vues, sommaire, navigation clavier, notes, HTML, PDF 16:9 et PowerPoint éditable. |
| Méthode | Chaîne URL → HTTP → parsing → validation → DOM, distinctions de notions et conducteur en sept phases. |
| Démonstration | Six ressources V2, sept scénarios, filtres, flashcards, aperçu et journal HTTP ; mode intégré explicitement signalé en file://. |
| Atelier | Éditeur JSON, contrat simple ou enrichi, import local, validation, affichage sûr et export ; trace de compréhension distincte. |
| Prompts | Six missions 19-A à 19-F, avec entrées, limites, sorties et critères. |
| Flashcards | Douze notions, retournement, navigation, mélange et suivi personnel. |
| Quiz | Huit situations, trois choix expliqués, omissions signalées et remise à zéro. |
| Validation | Sept critères observables, revue humaine, blocage d’un statut VALIDÉ incomplet et remise à revoir après modification. |
| Portfolio | Exports séparés de preuve, index, relais et ZIP de données/traces. |
| Ressources | Laboratoires, supports reconstruits, sources de cadrage et documentation externe. |

## Technologie et conservation

Vite, Bootstrap local, polices d’icônes locales, logo officiel et thème bleu nuit/or LN-IA sont conservés. Les deux entrées portables sont reconstruites avec styles et scripts intégrés ; elles gardent dist à leurs côtés pour les ressources.

Un stockage dédié lnia-atelier-s19-mecanismes-v2 préserve les anciens carnets d’assemblage. Les modèles de preuve restent vierges et aucune observation candidate n’est inventée. Les sources C:, le pack V3 et les productions personnelles du dossier commun restent inchangés.

Sauvegarde de l’état antérieur : docs/sauvegardes/atelier-S19-avant-refonte-contenu-2026-11-25.zip.

## Supports reconstruits

- Projection HTML : 22 vues.
- PowerPoint éditable : 22 diapositives et notes mises à jour.
- Projection PDF 16:9 : 22 pages.
- Conducteur PDF : 2 pages, 110 minutes.
- Fiche candidat PDF : 2 pages.
- Révision PDF : 5 pages, 12 cartes et 8 questions corrigées.
- Notes, prompts, modèles, laboratoire autonome et kit candidat JSON actualisés.

Les PDF sont rendus et relus visuellement. Le PowerPoint est ouvert par conversion LibreOffice headless : 22 pages rendues et inspectées. Les titres et l’ordre correspondent à la source des vues HTML.

## Vérifications effectuées

- npm.cmd run build : réussi ; la commande génère aussi les supports et les ZIP.
- npm.cmd run check : 9 groupes de contrôles de données, exports, états, champs et ressources réussis.
- Chromium réel : 24 contrôles fonctionnels réussis, sans erreur JavaScript collectée, dont navigation, projection, scénarios HTTP, import/export, validation et quiz.
- Largeur 375 px : les onze rubriques ne présentent pas de débordement horizontal.
- Captures réelles à 1440 et 390 px : style, logo et adaptation mobile inspectés.
- Clavier réel : activation de la flashcard par Entrée, état aria-expanded contrôlé.
- Liens et ressources locales : 8 pages actives auditées, aucune cible manquante ; les destinations de la version portable ont été corrigées.
- PDF : aucun texte détecté hors des limites des pages ; coupures de blocs corrigées.
- ZIP : intégrité et chemins contrôlés ; les anciens fichiers du laboratoire ne sont plus inclus dans le nouveau kit.

Détails : audit-refonte-S19.json, recette-navigateur-S19.json et recette-affichage-clavier-S19.json.

Les tests PHP, installation et fonctionnement hors connexion PWA ne sont pas annoncés comme exécutés. Les destinations externes sont conservées ; leur disponibilité distante n’a pas été auditée. Aucune publication distante effectuée.

## Reprendre

Modifier src/seance.json pour le contenu éditorial. tools/refonte-content-s19.py en conserve la génération initiale ; ne pas le relancer après une correction manuelle sans y reporter celle-ci.

npm.cmd run dev lance le travail Vite. npm.cmd run build reconstruit HTML, supports, ZIP et entrées portables. npm.cmd run check vérifie le parcours. python -X utf8 tools/audit-refonte-s19.py contrôle les fichiers et rend les PDF. La recette Chromium utilise une instance headless de test distincte du navigateur utilisateur.
