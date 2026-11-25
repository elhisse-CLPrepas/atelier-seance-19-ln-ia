# PROMPTS CANDIDATS — SÉANCE 19

## Du projet d’activité à la PWA

**Version :** V1  
**Statut :** À VALIDER

> Exécuter dans l’ordre. Remplacer les champs entre crochets. Contrôler et valider humainement chaque étape. Ne transmettre aucun secret ni donnée personnelle.

## 19-A — Auditer, cadrer et choisir les données

```text
Tu es développeur web pédagogique dans le cadre LN-IA.
Analyse le mini-site V1 de mon activité sans le modifier.
Activité : [ACTIVITÉ]. Public : [PUBLIC]. Besoin : [BESOIN].
Inventorie les fichiers, explique leur rôle, repère les contenus répétitifs et les contenus utiles hors connexion.
Propose une PWA minimale adaptée à cette activité, un schéma JSON et un plan fichier par fichier.
Repère tout secret ou donnée sensible sans l’afficher.
N’applique aucun changement. Termine par une checklist et : VALIDATION DU PÉRIMÈTRE REQUISE.
```

## 19-B — Construire et valider `data/data.json`

```text
À partir des contenus validés de mon activité, propose data/data.json avec 6 à 12 objets utilisant le même schéma.
Chaque objet comporte au minimum : id, titre, description, categorie, niveau, objectifs, activite, livrable, question et reponse.
Utilise uniquement mes contenus. Marque "À compléter" toute donnée manquante.
Contrôle : JSON valide, UTF-8, identifiants uniques, types cohérents, aucun secret et aucun protocole dangereux.
Explique comment ce JSON alimentera les cartes et les flashcards. N’écrase aucun fichier existant.
```

## 19-C — Charger les données et générer l’interface

```text
Intègre ./data/data.json avec JavaScript natif, async/await et fetch().
Teste response.ok, response.json(), le tableau reçu, le schéma et les types de chaque objet.
Génère cartes et flashcards avec createElement et textContent. N’injecte pas de contenu JSON avec innerHTML.
Utilise de vrais boutons accessibles au clavier. Prévois prefers-reduced-motion.
Affiche chargement, succès avec compteur, tableau vide et erreur avec bouton Réessayer.
Propose d’abord les modifications ; après mon accord, sauvegarde et applique seulement le diff validé.
```

## 19-D — Tester les réponses et les limites Web

```text
Construis puis fais exécuter un protocole couvrant : succès, 404, JSON invalide, tableau vide, donnée non-tableau, schéma invalide, lien dangereux, bouton Réessayer, clavier, lecteur d’écran, contraste, responsive et console.
Explique simplement requête, réponse, statut HTTP et CORS.
Compare JSON local, API publique et API protégée. N’utilise aucune vraie clé et ne contourne pas CORS.
Produis un tableau : test, manipulation, attendu, observé, statut. N’invente aucun résultat.
```

## 19-E — Construire la PWA statique

```text
Prépare mon mini-site V2 comme PWA statique simple.
Crée ou révise manifest.webmanifest, service-worker.js, offline.html, l’enregistrement dans js/app.js, les métadonnées PWA et les icônes 192x192 et 512x512.
Utilise start_url "./", scope "./" et des chemins relatifs compatibles avec un sous-dossier.
Versionne le cache, mets seulement l’enveloppe statique utile en cache, ne conserve aucune réponse d’erreur et ne supprime pas les caches d’autres applications.
Ne garantis pas le hors connexion avant test. Ne mets aucune donnée privée en cache. Ne déploie rien.
Explique installation, activation, interception et procédure de test dans le navigateur.
```

## 19-F — Auditer, documenter et préparer la validation

```text
Audite la structure, les chemins, le HTML, les métadonnées, le responsive, le clavier, les états, le JSON, les liens, les flashcards, le manifeste, le service worker, le cache, le hors connexion, les secrets, README et preuve 19.
Classe les anomalies en bloquantes, importantes et mineures.
Produis les corrections minimales proposées, la procédure de test local, la checklist avant publication, l’arborescence à transférer et un plan de retour arrière.
Ne publie rien et ne modifie aucun dépôt distant.
Termine exactement par : PRÊT POUR VALIDATION HUMAINE.
```
