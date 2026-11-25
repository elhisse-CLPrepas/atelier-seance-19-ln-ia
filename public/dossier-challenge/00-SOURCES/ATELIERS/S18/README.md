# Atelier S18 · De mes sources à mon pack mini-site

## Version en ligne — GitHub Pages

Adresse : https://elhisse-clprepas.github.io/atelier-seance-18-ln-ia/

Le workflow `.github/workflows/deploy-pages.yml` reconstruit et contrôle le site à chaque push sur `main`, puis publie `dist` sur GitHub Pages. Il peut aussi être relancé depuis l’onglet Actions. Les ZIP du dossier Challenge, du trio de production, des exemples et du livrable Déclic Web sont inclus dans le site publié.

Accès directs : [Dossier Challenge](https://elhisse-clprepas.github.io/atelier-seance-18-ln-ia/dossier-challenge/), [Déclic Web](https://elhisse-clprepas.github.io/atelier-seance-18-ln-ia/livrables/mini-site-declic-web/) et [pack produit](https://elhisse-clprepas.github.io/atelier-seance-18-ln-ia/livrables/mini-site-declic-web.zip). Les versions locales hors ligne restent disponibles. La publication ne remplace pas la revue pédagogique des productions.

## Livrable Déclic Web intégré

Dans **Exemples & sources**, choisir **Déclic Web** puis **Ouvrir le mini-site produit**. Le dossier source à remettre à l’agent et le pack produit sont deux téléchargements distincts. Le site livré comporte six sections, une fiche d’exploration HTML/CSS/JS, une affiche agrandissable, un bouton afficher/masquer et un quiz corrigé.

La production d’origine reste dans `declic-web-sources-S18/livrables/`. La construction copie le site et son ZIP dans `public/livrables/`, puis Vite les diffuse dans `dist/livrables/`. Les empreintes de `LIVRAISON-SHA256.json` servent à vérifier que la copie publiée correspond aux fichiers contrôlés. Le journal, README.md, SOURCES.md et CONTROLE.md expliquent la réalisation et ses limites. La revue du pilote et les observations personnelles restent à compléter.

La nouvelle affiche pratique S18 se télécharge dans **Ressources** ; son PNG original et son prompt restent dans `output/imagegen/`. Les dossiers séparés S17 et VS Code conservent leur périmètre.

## Carnet d’essai — édition du 23 novembre 2026

Ouvrir `OUVRIR-SEANCE-18.html`, puis **Mon carnet d’essai**. Le parcours principal comporte six accès : Démarrer, Exemples & sources, Mon carnet d’essai, Mes 3 documents, Essayer mon pack et Conserver & reprendre. Projection, méthode, cartes, quiz et ressources restent regroupés sous **Animer & réviser**.

Le carnet suit trois étapes : projet et sources, contenu du mini-site, prompt et pack. Les choix techniques et la comparaison de deux accroches sont facultatifs. Après production, le participant renseigne son essai réel et exporte sa preuve ; la revue du pilote reste distincte.

Les documents [instructions participants](INSTRUCTIONS-PARTICIPANTS-S18.md), [prompt maître](PROMPT-MAITRE-PRODUCTION-S18.md) et [méthode AGENT.md](AGENT.md) sont lisibles dans le carnet sans requête réseau. Le téléchargement `dist/supports/trio-production-S18.zip` les réunit. Le prompt personnalisé exporté demande leur utilisation et la production du dossier, du ZIP, de README.md, SOURCES.md et CONTROLE.md.

Les quatre dossiers `dist/supports/exemples/` fournissent chacun un guide fictif enrichi, une affiche SVG originale adaptée au sujet, une fiche cible, les trois documents et un prompt prérempli. Les dimensions du catalogue et les projets du portfolio sont explicitement fictifs. Ces ZIP sont des entrées de production à donner à l’agent, pas des productions personnelles validées.

`npm.cmd run build` régénère le carnet, les affiches, les copies des documents et les archives. Les sources éditables sont `src/workbook.js`, `src/production.js`, `src/content.js`, `src/exports.js`, `src/seance.json` et `tools/production-supports.mjs`. `src/generated/cases.json` est régénéré : modifier les sources, puis reconstruire. `public/` et `dist/` restent des copies de diffusion ; les dossiers séparés S17 et VS Code ne sont pas modifiés.

Contrôles : `npm.cmd run check`. Les scripts `tools/check-s18-browser.mjs` et `tools/check-production-browser.mjs` effectuent les essais navigateur contre un navigateur de test isolé exposé localement sur le port 9331 ; ils ne démarrent pas ce navigateur. Les captures et rapports restent dans `tmp/qa/s18/`, hors Git.

Les supports PDF/PPTX ci-dessous restent des supports complémentaires ; les trois Markdown et le carnet constituent les consignes de production actualisées.

Challenge 100 Jours · Automne 2026 · Module 05 · LN-IA
Prof. Abderrahman EL HISSE

Version 1.0 · Lundi 23 novembre 2026 · 90 minutes proposées
Horaire à communiquer par le formateur en heure de Casablanca.
Statut pédagogique de cette édition : À VALIDER par le pilote.

## Ouvrir la séance

1. Extraire tout le ZIP dans un dossier.
2. Ouvrir OUVRIR-SEANCE-18.html dans Chrome, Edge ou Firefox.
3. Parcourir les onze rubriques avec le menu latéral.
4. Utiliser PROJECTION-SEANCE-18.html pour ouvrir directement le diaporama.

Conserver le dossier dist à côté de ces deux fichiers. Les fonctions et supports locaux n’utilisent pas de CDN. Les adresses externes nécessitent Internet. Si le navigateur limite l’ouverture locale, servir dist avec `python -m http.server 8000 --directory dist` puis ouvrir http://localhost:8000/.

Le carnet est conservé sur le navigateur utilisé. Le bouton « Sauvegarder le carnet JSON » produit une copie pour la reprise. La version enregistrée dans un navigateur reste distincte de vos fichiers Markdown.

## Les onze rubriques

| Rubrique | Travail proposé |
| --- | --- |
| Accueil | Vue globale, question d’ouverture, pièces d’entrée et parcours S17–S20 |
| Présentation | 22 vues, sommaire, clavier, notes et supports PPTX/PDF |
| Méthode | Six phases et conducteur de 90 minutes |
| Démonstration | Quatre cas fictifs, une phrase corrigée à la fois |
| Atelier | Plan et source importés, rédaction, aperçu étroit, comparaison et exports |
| Prompts | Reprise, prompt maître candidat et quatre missions courtes |
| Flashcards | 12 cartes avec retournement, mélange et suivi |
| Quiz | Huit situations, trois choix par question et 24 explications |
| Validation | Sept gestes, observation et décision datée du pilote |
| Portfolio | Preuve, entrée d’index et relais S19 |
| Ressources | Supports, modèles, prototype et références |

## Supports du pack

Dans dist/supports :

- presentation-S18.pptx : 22 diapositives modifiables avec notes.
- presentation-S18.pdf : projection des mêmes 22 vues.
- conducteur-S18.pdf et .md : déroulement et relances.
- fiche-candidat-S18.pdf : trois pages à compléter.
- cas-fictifs-S18.pdf et .md : Roue libre, Cap Études, Terre d’Argile et Studio Nadia.
- revision-S18.pdf et .md : cartes et quiz corrigé.
- guide-web-S18.pdf : rédaction et approfondissement technique.
- prompts-S18.md : six consignes réutilisables.
- kit-candidat-S18.zip : modèles vierges, cas fictifs et prototype.
- prototype-S18.zip : fichiers HTML/CSS/JS commentés, sans installation.

L’affiche se trouve dans dist/assets/affiche-S18.png.

## Progression du candidat

Entrée : 04-WEB/structure-page-projet.md, source corrigée S16 et preuve S17.

Remise S18 :

- 04-WEB/contenu-page-projet.md
- 06-PORTFOLIO/preuve-S18.md
- entrée S18 à ajouter à 06-PORTFOLIO/index-portfolio.md
- 06-PORTFOLIO/relais-S19.md

Rédiger les six sections, comparer deux accroches et raccourcir une phrase en gardant son appui. Faire lire le fichier exporté par un binôme. Conserver ses mots, la correction ou le maintien et le résultat de réouverture.

Le bouton « Conserver une copie de cette version » permet d’archiver un contenu V1 puis V2. Les observations des cas fictifs ne remplissent jamais la preuve personnelle.

Le statut VALIDÉ demande des pièces renseignées, les sept gestes et une décision avec nom, date et observation du pilote. Une modification de contenu après validation remet la revue à reprendre. Le quiz ne valide pas le dossier.

## Été et automne

Le prompt maître d’automne du 12 novembre organise S18 autour du contenu rédigé. S19 assemble la page V1. Les supports joints d’été décrivent une séance HTML/CSS/JS plus longue. Leur réemploi technique se trouve dans l’approfondissement guidé et le prototype.

Les documents anciens sont conservés sans changement dans docs/sources. Leur mention VALIDÉ concerne les versions d’été correspondantes. Voir dist/supports/REPERES-S18-ETE-AUTOMNE.md.

## Modifier le mini-site

Utiliser Node.js 22.12 ou une version ultérieure compatible.

```sh
npm ci
npm run dev
```

Puis :

```sh
npm run build
npm run check
npm run preview
```

Vite 7.3.8, Bootstrap 5.3.9 et Bootstrap Icons 1.13.1 sont verrouillés dans package-lock.json. Le dossier node_modules n’est pas livré.

src/seance.json porte les métadonnées, 22 vues, notes, cas, phases, prompts, cartes, quiz et critères. src/content.js porte les champs du carnet et les ressources. src/render.js construit le HTML initial. src/main.js gère les interactions. src/exports.js produit les fichiers du candidat. src/ln-ia.css conserve l’identité visuelle validée en S17.

tools/generate.mjs reconstruit le HTML et les modèles textuels. tools/build-documents.py produit les supports imprimables avec Python et ReportLab. Après modification de ces supports, relancer npm run build. Le PowerPoint est modifiable directement. En cas de modification des vues, remettre en cohérence PPTX, PDF et src/seance.json avant diffusion.

## Référencement et diffusion

Le site est livré localement. Il n’est pas publié par cette livraison.

Dans site.config.json, renseigner publicUrl avec l’adresse HTTPS publique réelle, sans fragment ni paramètres. Choisir indexable: true puis reconstruire. Le générateur produit canonical, URL et image Open Graph, sitemap et règles d’indexation. Tant que l’adresse n’est pas renseignée, le HTML reste en noindex.

Les métadonnées de description, langue, viewport, partage et LearningResource sont déjà présentes. L’image de partage est l’affiche S18. Sur un hébergement dans un sous-dossier, la base Vite relative conserve les chemins des ressources. Publier le contenu de dist.

## Reprise vers S19

Vendredi 27 novembre 2026 : rouvrir plan S17, contenu S18 et preuve. Joindre la fiche cible. Assembler page-simple-v1.md ou .html. Déplacer une copie du dossier, ouvrir la page puis son lien et consigner le nom de la pièce atteinte.

Consigner uniquement les pièces et essais réellement disponibles dans relais-S19.md.
