# Fiche candidat — Séparer et charger les données

**Séance :** vendredi 27 novembre 2026 · Semaine 10 · Module 05  
**Édition :** automne V3 du 25 novembre 2026 · **Statut du pack :** VALIDÉ POUR PRÉPARATION ET UTILISATION EN S19  
**Pilotage :** Prof. Abderrahman EL HISSE · LAB-NUMÉRIQUE-IA

## Votre mission

Transformer trois cartes de votre mini-site en données JSON, les charger depuis un serveur local et expliquer ce que voit le lecteur dans quatre situations. Vous préparez ensuite les composants PWA pour S20.

Projet : __________ · Public : __________ · Besoin : __________
V1 conservée : __________ · Copie V2 : __________ · Serveur disponible : __________

1. Remplissez la fiche de départ 12. Si votre V1 manque, utilisez la copie fictive indiquée par le formateur.
2. Repérez titre, catégorie et description sur trois cartes. Retrouvez ces champs dans `data/projets.json`.
3. Vérifiez tableau, objets, guillemets et virgules. Contrôlez que chaque champ attendu contient une chaîne non vide.
4. Ouvrez V2 depuis le serveur local. Modifiez un titre du JSON puis rechargez. Montrez la carte modifiée.
5. Vérifiez dans la console et le panneau Réseau le chemin demandé, le statut HTTP et les données reçues.
6. Testez les quatre situations du tableau. Rétablissez les données après l’essai.
7. Expliquez manifeste, service worker et cache avec la fiche 09, puis remplissez la preuve 05.

| Situation | Manipulation | Résultat attendu | Résultat observé |
|---|---|---|---|
| Chargement | Ralentir la requête | Message « Chargement… » | À COMPLÉTER |
| Succès | Charger les trois objets | Trois cartes avec les bons textes | À COMPLÉTER |
| Vide | Charger une copie contenant `[]` | Message « Aucun projet à afficher » | À COMPLÉTER |
| Erreur | Demander un chemin absent | Message compréhensible et nouvelle tentative possible | À COMPLÉTER |

## Ce que vous remettez

Votre dossier `04-WEB/mini-site-v2/` avec page, styles, JSON, JavaScript et README ; `06-PORTFOLIO/preuve-S19.md` ; `06-PORTFOLIO/relais-S20.md` ; une entrée dans l’index du portfolio. Gardez V1 et V2 distinctes.

Expliquez à un binôme : quelle donnée a changé ? Quel code la charge ? Comment distinguez-vous vide et erreur ? Quel rôle aura le service worker en S20 ? Une case cochée ou un quiz réussi ne vaut pas validation du projet.
