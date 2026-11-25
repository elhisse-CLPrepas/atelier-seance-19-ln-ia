# Contrôle d’alignement — V3 du 25 novembre 2026

## Résultat

Pack aligné sur S19 du 27 novembre 2026 : JSON local, quatre états et préparation PWA. Durée de référence : 110 minutes, variante 90 minutes. Trois mini-sites importés et embarqués. La demande du pilote de générer une version validée est consignée dans VALIDATION-V3.md ; elle ne prévalide pas les travaux candidats.

## Corrections et distinction des ressources

- Minimal : trois objets fictifs Déclic Web, mêmes champs title/category/description que la fiche 06 ; contrôle des chaînes non vides ajouté avant affichage.
- Laboratoire enrichi : schéma à six ressources conservé, identifié comme complément formateur ; les données minimales ne sont pas interchangeables avec ce schéma.
- Deux inventaires PWA limités aux fichiers réellement présents et aux composants à préparer en S20.
- Preuves d’été remplacées dans les copies S19 par des modèles vierges. Aucun résultat historique présenté comme essai de novembre.
- Démonstration S17 conservée comme référence historique de prérequis.
- Fiche 08, READMEs, dates, noms V3 et liens alignés ; entrée HTML autonome ajoutée.

## Contrôles exécutés

- 24 fichiers importés : empreintes identiques aux sources externes et copies de référence locales.
- JavaScript : contrôles de syntaxe de chaque fichier externe et script intégré aux pages HTML.
- JSON : parsing de chaque fichier livré.
- Liens Markdown et ressources HTML : présence des cibles locales contrôlée.
- 28 tests de comportement réussis sur les copies S19 : chargement, succès, vide, HTTP, réseau, syntaxe JSON, structure, champs, restauration ; sept scénarios du laboratoire et ouverture/fermeture d’une flashcard.
- Service HTTP local : requêtes sur les ressources des trois mini-sites, puis arrêt du serveur temporaire.
- ZIP : contrôle CRC, noms et contenus identiques au dossier livré ; manifeste SHA-256 de livraison.

Les détails mesurés sont dans resultats-controles.json et resultats-tests-comportement.json.

## Limites et essais restant à faire

Les tests de comportement utilisent Node et un DOM simulé : ils ne prouvent pas le rendu visuel, le focus réel ou l’accessibilité complète. Le contrôle dans un navigateur n’a pas été possible avec les outils disponibles de cette session. Revoir visuellement mobile, clavier, zoom et projection sur le poste du formateur.

Aucun essai d’exécution PHP, de service worker, d’installation ou de fonctionnement hors connexion n’est attesté. Les liens distants ne sont pas vérifiés ; le socle ne doit pas en dépendre. Aucune publication effectuée. Le mini-site général, la présentation et les PDF extérieurs à ce pack restent ceux de la production antérieure.

## Conservation et reprise

Sources C: et pack V2 inchangés. Les imports de référence sont dans 05-EXEMPLES-CODE à la racine du projet ; leurs copies adaptées sont dans mini-sites dans ce pack. Les noms des dossiers importés sont historiques, distincts du statut V3 du pack.

Pour rejouer les contrôles : node tools/test-imported-s19.cjs puis python tools/finalize-pack-s19.py depuis la racine du projet. Le script d’import tools/validate-pack-s19.py refuse d’écraser une livraison V3 déjà présente.
