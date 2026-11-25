# Prompts candidats — 19-A à 19-F

**Séance :** vendredi 27 novembre 2026 · Semaine 10 · Module 05  
**Édition :** automne V2 documentaire du 25 novembre 2026 · **Statut :** À VALIDER  
**Pilotage :** Prof. Abderrahman EL HISSE · LAB-NUMÉRIQUE-IA

## Cadre commun à copier avant chaque mission

```text
Vous êtes l’assistant pédagogique LN-IA. Préparez S19 du 27 novembre 2026 : JSON local et préparation PWA.
Projet = [NOM] ; V1 = [CHEMIN] ; V2 = [CHEMIN] ; serveur disponible = [OUTIL].
Travaillez dans la copie V2 et les fichiers de preuve indiqués. Lisez les instructions locales.
Conservez une sauvegarde avant modification ; respectez les autorisations déjà données.
Utilisez des données fictives ou autorisées, JavaScript natif et des ressources locales.
N’installez pas de dépendance. N’ajoutez ni API distante, ni secret, ni service worker actif, ni déploiement.
Expliquez les modifications. Signalez les entrées manquantes et les limites.
Terminez par les fichiers lus, créés ou modifiés, les tests exécutés et les essais restants.
Ne renseignez jamais une observation humaine à sa place. Statut de sortie : À VALIDER.
```

## 19-A — Auditer la V1 et choisir les données

```text
Entrées : V1 et fiche de départ 12.
Mission : Lire sans modifier. Inventorier HTML, styles et JavaScript. Repérer trois cartes répétitives, proposer leurs champs et identifier les données autorisées et exclues. Vérifier les prérequis et proposer une copie V2.
Sorties : Inventaire, correspondance champs/cartes, chemins V1/V2 et points manquants.
Réussite : Un tiers retrouve les trois contenus dans la V1.
```

## 19-B — Structurer et valider le JSON

```text
Entrées : Inventaire 19-A et trois contenus fictifs.
Mission : Dans la copie V2 autorisée, créer ou adapter data/projets.json : tableau de trois objets avec title, category et description, chaînes non vides. Expliquer objets, clés et types. Vérifier syntaxe et structure. Fournir séparément un exercice contenant un guillemet manquant et une virgule finale, puis sa correction.
Sorties : JSON valide, explication des champs et exercice corrigé.
Réussite : Parsing réussi et chaque objet respecte les champs attendus.
```

## 19-C — Charger les données

```text
Entrées : V2 et JSON contrôlé en 19-B.
Mission : Adapter js/app.js et la page : fetch relatif, contrôle response.ok, parsing et validation de structure. Construire les cartes avec createElement et textContent. Utiliser les styles locaux. Expliquer la chaîne URL → HTTP → JSON → DOM et le lancement local déjà disponible.
Sorties : Fichiers modifiés et diff expliqué, commande locale et correspondance des champs.
Réussite : Une modification du titre JSON se retrouve sur la bonne carte après rechargement.
```

## 19-D — Éprouver les quatre états

```text
Entrées : Chargement 19-C et copie de test.
Mission : Rendre chargement, succès, vide et erreur visibles. Vider les anciennes cartes avant un nouvel affichage. Prévoir une nouvelle tentative. Donner les manipulations reproductibles : ralentissement, trois objets, tableau vide et chemin absent. Restaurer ensuite la configuration de succès.
Sorties : Gestion des états et protocole avec attendu/observé séparés.
Réussite : Chaque état peut être provoqué, expliqué et suivi d’un retour au succès.
```

## 19-E — Auditer sans modifier

```text
Entrées : V2, README et résultats des quatre tests.
Mission : Lire les fichiers sans correction automatique. Examiner syntaxe JSON, schéma attendu, chemins, response.ok, gestion des exceptions, textContent, messages visibles, clavier, mobile et absence de données sensibles. Vérifier que la PWA reste une préparation.
Sorties : Rapport : conforme, bloquant, à corriger, non testé ; chemin et motif de chaque écart.
Réussite : Chaque conclusion est reliée à un fichier ou à un essai documenté.
```

## 19-F — Documenter et préparer S20

```text
Entrées : Rapport 19-E et observations réellement disponibles.
Mission : Compléter README, preuve-S19.md, entrée d’index et relais-S20.md. Distinguer attendu, observé et non testé. Rappeler comment lancer le serveur, restaurer le JSON et reproduire les quatre états. Décrire les composants PWA à préparer, sans les activer.
Sorties : Documentation, preuve et relais ; rapport des fichiers écrits et tests exécutés.
Réussite : Un tiers peut rouvrir V2, rejouer un test et identifier le premier geste S20.
```
