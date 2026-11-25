# Cahier des charges — Exemple JSON minimal S19

**Séance :** vendredi 27 novembre 2026 · Semaine 10 · Module 05  
**Édition :** automne V2 documentaire du 25 novembre 2026 · **Statut :** À VALIDER  
**Pilotage :** Prof. Abderrahman EL HISSE · LAB-NUMÉRIQUE-IA

## Architecture cible

```text
04-WEB/mini-site-v2/
  index.html
  assets/styles.css
  data/projets.json
  js/app.js
  README.md
06-PORTFOLIO/
  preuve-S19.md
  relais-S20.md
```

Les anciens exemples peuvent utiliser `css/styles.css` ; conserver ce chemin si la page le référence correctement. Les noms anciens `05-web/` et `preuve-19-json-pwa.md` restent des repères d’été.

## Contrat des données

`projets.json` contient un tableau. Chaque objet porte `title`, `category` et `description`, chaînes non vides. Exemple fictif adapté à Déclic Web :

```json
[
  {"title":"Préparer sa page", "category":"Méthode", "description":"Ordonner les sections de son projet."},
  {"title":"Relire ses contenus", "category":"Contrôle", "description":"Vérifier les formulations et les sources."},
  {"title":"Vérifier ses liens", "category":"Pratique", "description":"Ouvrir la pièce annoncée depuis la page."}
]
```

Pour tester le vide, un tableau `[]` reste valide. Un objet racine, un JSON mal formé, un champ absent ou de mauvais type doit produire une erreur compréhensible. Ne pas injecter les chaînes comme HTML.

## Comportement attendu

1. Afficher le chargement et retirer les anciennes cartes.
2. Demander `./data/projets.json` avec `fetch()` et vérifier `response.ok`.
3. Parser la réponse, vérifier tableau et champs.
4. Afficher vide si le tableau est vide ; sinon créer les cartes avec `textContent`.
5. Intercepter les erreurs réseau, HTTP, syntaxe et structure ; afficher un message lisible et proposer de réessayer.

La zone d’état peut utiliser `role="status"` et `aria-live="polite"`. Prévoir titres hiérarchisés, focus visible et adaptation mobile. Aucun CDN ni API ne doit être indispensable. Aucun manifeste ni service worker actif n’est nécessaire.

## Lancement et recette

Depuis le dossier V2, si Python est déjà disponible :

```powershell
python -m http.server 8080 --bind 127.0.0.1
```

Ouvrir `http://127.0.0.1:8080/`, observer les quatre états avec la fiche 04, puis arrêter le serveur par Ctrl+C. Si le port est occupé, choisir un port libre et adapter l’URL. Un serveur statique sert les fichiers ; il n’exécute pas PHP.

Les références d’été sont inventoriées dans SOURCES-ET-SYNCHRONISATION.md. Ce cahier des charges documente la cible ; il n’atteste pas que le mini-site actuel a déjà été reconstruit ou testé.
