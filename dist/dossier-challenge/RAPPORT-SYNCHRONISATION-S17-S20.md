# Synchronisation S17–S20 — 26 novembre 2026

Mission : reproduire et enrichir le dossier commun selon les quatre ateliers locaux.

## Réalisation

- Accueil et guide reconstruits ; matrice d’alignement et consignes actualisées.
- Carnet transversal autonome : quatre séances, sauvegarde JSON, reprise, preuve Markdown, bilan, impression et remise à zéro par séance.
- Références des quatre ateliers copiées avec leurs empreintes ; sources externes non modifiées.
- Laboratoire S19 enrichi et minimal intégrés ; exemple S20 Cap Études V1/V2 ajouté.
- Prompts regroupés par séance ; nouveaux modèles et index courant séparés des preuves préexistantes.
- Limite d’import des carnets S19/S20 explicitée ; aucun faux format de compatibilité créé.
- Références S19 du CSV actualisées sans modifier statut, observation, date ni décision.
- Contexte Git corrigé : pas de dépôt initialisé ni de publication présumée.

## Conservation

Sauvegarde intégrale avant intervention : docs/sauvegardes/dossier-module05-avant-alignement-20261126-001639.zip à la racine de l’atelier S19.

70 fichiers préexistants de productions, preuves, trio S18 et carnet S17 ont été contrôlés par SHA-256 : contenus inchangés. Le pack V3 et les ateliers voisins restent intacts. Les anciens modèles S19 d’assemblage sont conservés et distingués du parcours JSON actuel.

## Contrôles

Voir 00-SOURCES/CONTROLE-SYNCHRONISATION.json pour les liens et la conservation. La recette du nouveau carnet est consignée dans docs/recette-dossier-module05.json à la racine S19. Les modèles ne constituent pas des observations de séance. Aucune validation candidate ni publication effectuée.

## Recette finale et diffusion

- 14 contrôles Chromium réussis : accueil, ressources, séances indépendantes, validation, exports, reprise, refus d’ancien format, remise à zéro ciblée, impression, mobile et laboratoire HTTP.
- Captures ordinateur et mobile inspectées ; défaut de contraste du bouton secondaire corrigé.
- Activation au clavier réel du bouton de séance contrôlée.
- 24 pages HTML auditées sans cible locale manquante.
- 70 fichiers préexistants protégés par empreintes SHA-256 : contenus inchangés.
- Les observations du CSV restent identiques ; seules les références de la ligne S19 ont changé.
- Copie publique, copie dist et ZIP synchronisés depuis le dossier source ; intégrité CRC et contenus vérifiés.
- Construction Vite et neuf groupes de contrôles S19 réussis après intégration.

Les résultats détaillés de cette recette sont inclus dans 00-SOURCES/RECETTE-NAVIGATEUR-MODULE05.json et RECETTE-AFFICHAGE-MODULE05.json. Ils décrivent les contrôles techniques, pas les essais personnels des candidats.

Pour diffuser de nouvelles modifications sans réinitialiser le dossier : `python -X utf8 tools/sync-challenge.py` depuis la racine S19. La construction Vite appelle aussi cette synchronisation. L’outil d’enrichissement initial refuse de réécrire un dossier déjà enrichi.

Les ateliers voisins, le pack V3 et les sources C: restent inchangés. Aucune publication, initialisation Git ou opération distante effectuée.
