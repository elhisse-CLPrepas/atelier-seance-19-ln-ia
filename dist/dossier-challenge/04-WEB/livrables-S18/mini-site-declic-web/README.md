# Déclic Web — Mini-site S18 · V1

Exemple pédagogique fictif LN-IA, produit le 23 novembre 2026. Public : débutants du Module 05. Objectif : observer HTML, CSS, JavaScript et le navigateur dans une page locale. Revue du pilote : **À examiner**.

## Ouvrir et essayer

1. Extraire tout mini-site-declic-web.zip dans un nouveau dossier.
2. Ouvrir mini-site-declic-web/index.html dans un navigateur moderne.
3. Suivre « Explorer les trois fichiers » pour ouvrir la fiche incluse.
4. Essayer l’explication afficher/masquer, l’affiche agrandie et le quiz corrigé.

Aucun serveur, compte, installation ou accès réseau n’est requis. JavaScript doit être activé pour les interactions. Le site ne collecte aucune donnée et ne conserve pas les réponses après fermeture.

## Organisation

- index.html : six sections, contenu et structure.
- css/styles.css : présentation LN-IA, mobile et focus.
- js/app.js : bouton, dialogue de l’affiche et quiz.
- assets/images/affiche-declic-web.svg : affiche fournie, copie identique.
- pieces/fiche-web.html : fiche adaptée et accès aux sources modifiables.
- pieces/fiche-web-source.html : fiche d’origine conservée.
- pieces/guide-source.md : guide d’origine conservé.
- SOURCES.md : références, utilisations et limites.
- CONTROLE.md : contrôles de l’agent et essais humains restant à faire.

## Comprendre et modifier

HTML organise le contenu, CSS le présente et JavaScript réagit aux événements. Le navigateur lit les fichiers et affiche le résultat. Cette organisation reprend S17 sans reprendre ses validations.

Modifier le texte dans index.html, les couleurs dans les variables au début de css/styles.css et les interactions ou corrections du quiz dans js/app.js. Changer une chose à la fois, actualiser et noter ce qui change. Conserver les chemins relatifs.

## Refaire le ZIP

Depuis livrables dans PowerShell, conserver la version précédente en utilisant un nouveau nom :

```powershell
Compress-Archive -LiteralPath .\mini-site-declic-web -DestinationPath .\mini-site-declic-web-V1-revision.zip
```

Extraire ailleurs et essayer la nouvelle copie. Le dossier mini-site-declic-web doit être l’unique racine de l’archive.

## Limites et reprise S19

Initiation fictive : ni maîtrise complète du Web, ni serveur, API ou publication automatique. La marque LN-IA est composée en texte ; aucun logo graphique supplémentaire n’est inventé. Le quiz sert à réviser, sans validation automatique. Les observations du participant, du binôme et la décision du pilote restent à renseigner. Reprendre en S19 les anomalies constatées et les essais non exécutés.
