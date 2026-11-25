# Atelier S17 — Comprendre les fondations du Web

Challenge 100 Jours · Module 05 · LN-IA · Prof. Abderrahman EL HISSE

Version 3 · Vendredi 20 novembre 2026 · 90 minutes proposées

Deux dépôts Git locaux indépendants portent l’atelier et le dossier Challenge. Voir [le guide de versionnement](docs/VERSIONNEMENT-LOCAL.md). Le dossier source Challenge est ignoré par le dépôt S17 ; les copies intégrées au pack sont des instantanés de diffusion.

Ouvrez `atelier-module05.code-workspace` dans VS Code pour retrouver les deux dépôts dans le même espace de travail.

## Ouvrir l’atelier

Ouvrez `OUVRIR-SEANCE-17.html` pour l’atelier ou `PROJECTION-SEANCE-17.html` pour la projection. Conservez `dist/` à côté de ces fichiers. Les fonctions et supports locaux restent disponibles sans connexion.

Ouvrez `mon-dossier-challenge-Module05/index.html` pour accéder directement au dossier personnel, au mini-site fourni et au carnet d’essai.

## Objectif de S17

Comprendre les rôles de HTML, CSS, JavaScript et du navigateur à partir du support fourni dans `mini-site-demonstration-seance-17/`.

La copie de travail est intégrée dans `mon-dossier-challenge-Module05/04-WEB/mini-site-demonstration/`. Sa navigation donne accès aux sections, aux fichiers, au dossier et au carnet. Les affiches d’été sont identifiées comme supports visuels ; leurs dates ne désignent pas l’atelier d’automne.

## Carnet et portfolio

Le carnet autonome se trouve dans `mon-dossier-challenge-Module05/01-SUIVI/carnet-essai-S17.html`. Il propose saisie locale, sauvegarde JSON, reprise, export Markdown et impression. La rubrique « Carnet d’essai » de l’atelier propose les questions de compréhension et une préparation facultative du plan pour S18.

Conservez les téléchargements dans `06-PORTFOLIO/carnet-essai-S17.md` et `06-PORTFOLIO/preuve-S17.md`. L’export ne remplace pas automatiquement les modèles sur le disque. Les observations, explications personnelles et revues humaines restent à renseigner.

## Supports

Les neuf affiches originales du dossier `AFFICHES/` sont intégrées à la rubrique Présentation sous forme de galerie avec accès aux images en grand. Elles figurent également en annexe du PowerPoint et du PDF : 22 vues pédagogiques suivies de 9 planches visuelles. `src/affiches.json` fixe leur ordre et leurs légendes. Les dates imprimées sur les supports originaux ne remplacent pas le calendrier d’automne 2026 ; les affiches S18 à S20 et Module 06 présentent la suite du parcours.

Pour l’animation : présenter les affiches Module 05 et S17 en ouverture, reprendre la fiche de départ avec le dossier candidat, puis utiliser les affiches suivantes lors du relais vers S18. Les variantes S20 servent à comparer les attentes du livrable final.

`dist/supports/` contient la présentation PDF et PowerPoint, les notes, le conducteur, la fiche imprimable du carnet, les prompts, la révision et le kit complet. Les 22 vues, 12 cartes et 8 questions utilisent le même support.

## Reconstruire

Avec Node.js 22.12 ou ultérieur et Python équipé de ReportLab et lxml :

```sh
npm ci
node tools/generate.mjs
python tools/sync-presentation.py
python tools/build-documents.py
npm run build
npm run check
python tools/verify-pack.py
```

`src/seance.json` porte le contenu pédagogique. `tools/generate.mjs` produit HTML, notes et modèles du pack, puis intègre une copie du dossier commun sans modifier ses sources. `npm run prepare:challenge` crée uniquement les modèles S17 manquants dans le dépôt commun. `tools/sync-presentation.py` synchronise textes et notes dans le PowerPoint existant et produit le PDF de projection. `tools/build-documents.py` reconstruit les supports imprimables et le ZIP.

Pour modifier le site : `npm run dev`. Le carnet autonome s’ouvre directement depuis son HTML. Exportez un JSON pour reprendre vos réponses dans un autre navigateur.

## Publication

Le déploiement GitHub Pages est configuré dans `.github/workflows/pages.yml`. Chaque envoi sur `main` publie le dossier `dist/` enregistré dans Git, avec les supports et la copie de diffusion du dossier Challenge.

Adresse prévue : https://elhisse-clprepas.github.io/atelier-seance-17-ln-ia/

Avant chaque envoi, reconstruire avec `npm run build`, vérifier avec `npm run check`, puis enregistrer les sources et la sortie `dist/` dans le même commit. Le workflow publie cette version construite sans dépendre du dépôt commun pendant le déploiement. Consulter l’onglet Actions du dépôt pour confirmer la réussite de la publication.

Le plan de page et les modèles S18 à S20 préparent la suite du Module 05.
