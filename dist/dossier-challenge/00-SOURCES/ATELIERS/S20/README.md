# Atelier séance 20 · LN-IA

Une V2 éprouvée par un lecteur — clôture du Module 05.
Lundi 30 novembre 2026 · semaine 10 · 90 minutes proposées. Horaire à communiquer.

## Ouvrir le pack

1. Extraire tout le ZIP dans un dossier. Ne pas ouvrir ses fichiers depuis l’aperçu de l’archive.
2. Ouvrir OUVRIR-SEANCE-20.html par double-clic.
3. Utiliser PROJECTION-SEANCE-20.html pour présenter les 22 vues.
4. Les supports sont dans dist/supports et public/supports. Conserver dist à côté des deux entrées HTML.

La version portable embarque les scripts et les styles. Elle charge ses images et téléchargements depuis dist. Elle ne demande pas Node pour parcourir les 11 rubriques. Le démonstrateur PWA se sert séparément sur localhost ou HTTPS.

## Contenu

- 11 rubriques : Accueil, Présentation, Méthode, Démonstration, Atelier, Prompts, Flashcards, Quiz, Validation, Portfolio, Ressources.
- 22 vues HTML, PowerPoint modifiable avec notes et PDF.
- Conducteur de 90 minutes, fiche candidat, quatre cas V1/V2, six prompts, 12 flashcards et huit questions corrigées.
- Carnet local : sauvegarde JSON, reprise d’un carnet S19 ou S20, import simple d’une V1 HTML, conservation des versions et export ZIP.
- Grille de sept critères, preuve S20, preuve globale, index et relais S21.
- Démonstrateur PWA séparé, trois fiches fictives, recette de portée, cache et mise à jour.

## Pratiquer

Reprendre la V1 S19, sa fiche et sa preuve. Donner une consigne stable à un lecteur extérieur. Noter les faits puis choisir une seule correction. Conserver la V1 et produire la V2. Rejouer la consigne et consigner les limites de comparaison.

L’import JSON S19 reconstruit la V1 à partir des champs. Pour conserver le HTML S19 original, utiliser « Importer la V1 HTML ». Cet import vise les pages simples exportées par les ateliers, avec une action relative et trois sous-titres. Les autres pages restent à conserver et à modifier dans votre éditeur.

Une fiche PDF/HTML/TXT/MD importée reste dans la mémoire de l’onglet. Il faut la sélectionner à nouveau après reprise du carnet. L’export ZIP conserve une fiche commune aux deux versions. Pour corriger aussi la fiche, créer et tester ses deux versions hors de ce générateur.

Le stockage navigateur dépend de son contexte et de ses réglages. Télécharger le carnet JSON pour garder une sauvegarde transportable. Les preuves S17 à S19 sont celles du participant : les joindre avant de vérifier les liens du portfolio.

## Modifier et reconstruire

Node.js 22.12 ou supérieur (24 convient) et npm. Les dépendances sont fixées dans package-lock.json.

```sh
npm ci
npm run dev
npm run build
npm run check
```

Le site utilise Vite 7.3.8, Bootstrap 5.3.9 et Bootstrap Icons 1.13.1. Le thème LN-IA et le contenu sont locaux. La commande build régénère le HTML statique, les cas et les modèles, construit dist puis produit les deux entrées portables. Les documents PDF et PPTX livrés restent disponibles.

Pour régénérer les supports de travail PDF, installer ReportLab dans votre environnement Python puis exécuter python tools/build-documents.py après tools/generate.mjs. Pour modifier les diapositives, ouvrir le PPTX livré. Le contenu pédagogique est aussi dans src/seance.json et les notes Markdown.

## Préparer une publication

Dans site.config.json, renseigner publicUrl avec l’adresse HTTPS réelle se terminant par /, puis indexable à true après décision de diffusion. Reconstruire. Le HTML contiendra canonical, Open Graph, Twitter Card, LearningResource et le sitemap correspondant. Sans URL décidée, la livraison reste en noindex et robots.txt refuse l’indexation.

L’adresse n’est pas inventée. Aucune publication n’a été effectuée. Le workflow GitHub Pages fourni se déclenche manuellement, après configuration Pages / GitHub Actions. Le dossier de déploiement est dist, pas le pack entier.

## Statuts et vérifications

À COMPLÉTER, À REVOIR, À VALIDER et VALIDÉ décrivent la revue pédagogique. Diffusion et déploiement sont distincts. Le score du quiz ne remplace pas l’ouverture des pièces devant le pilote.

Les vérifications exécutées et les contrôles restant à faire figurent dans docs/RAPPORT-VERIFICATION-S20.md. Les essais navigateur interactifs, mobiles et PWA doivent être consignés sur l’environnement d’utilisation.

## Sources et identité

Le master d’automne est conservé dans docs. Les supports historiques d’été sont séparés dans docs/sources. Voir docs/SOURCES-ET-CHOIX.md pour les adaptations.

Logo LN-IA fourni par le formateur. Les exemples sont fictifs. Les licences des dépendances sont dans docs/licences. Les droits sur les documents et marques d’origine restent à leurs titulaires.
