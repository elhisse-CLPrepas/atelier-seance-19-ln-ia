# SUPPORT FORMATEUR — SÉANCE 19

**Version :** V1
**Statut :** À VALIDER
**Durée recommandée :** 120 minutes

## Résultat essentiel

Le candidat explique les notions Web mobilisées et produit, à partir d’une copie de son mini-site, une PWA statique simple liée à sa propre activité. Il charge des données JSON, génère une interface accessible, gère les erreurs, installe les composants PWA et fournit des preuves de tests réels.

## Deux objectifs indissociables

- **Comprendre :** relier fichier, URL, requête, réponse HTTP, JSON, DOM, API, CORS, serveur, manifeste, service worker, cache et HTTPS.
- **Produire :** adapter le démonstrateur de l’atelier à un cas d’activité réel, sans données privées et sans publication automatique.

## Prérequis obligatoires

```text
[ ] activité et public cible définis
[ ] besoin utilisateur formulé
[ ] mini-site V1 fonctionnel et sauvegardé
[ ] dossier V2 distinct et modifiable
[ ] 6 à 12 contenus publics, fictifs ou autorisés
[ ] aucun secret ni donnée personnelle
[ ] navigateur, console et serveur local disponibles
[ ] chemins relatifs utilisés
[ ] fiche de départ 12 complétée
```

Si la V1 n’existe pas, utiliser une copie du démonstrateur comme squelette pédagogique et remplacer seulement les contenus autorisés. Si le projet métier est trop complexe, produire une PWA minimale : accueil, liste de contenus, flashcards et page hors connexion.

## Déroulé recommandé

| Phase | Durée | Production ou preuve |
|---|---:|---|
| Cadrage de l’activité et diagnostic V1 | 10 min | fiche de départ validée |
| Notions Web et lecture de l’architecture | 15 min | schéma requête → réponse → JSON → DOM |
| Données métier autorisées | 15 min | `data/data.json` valide |
| `fetch()` et interface dynamique | 20 min | cartes et flashcards |
| États, erreurs et accessibilité | 15 min | scénarios testés |
| Construction PWA | 25 min | manifeste, icônes, service worker, cache, hors connexion |
| Contrôle, preuve et restitution | 20 min | preuve 19 et décision |

## Manipulation guidée

1. Montrer le démonstrateur de `D:\Atelier-seance-19` sans le présenter comme modèle à copier aveuglément.
2. Faire relier chaque fichier à son rôle.
3. Dupliquer la V1 du candidat et travailler seulement dans la V2.
4. Construire `data/data.json` avec un schéma stable et des contenus autorisés.
5. Charger le JSON avec `fetch()`, `response.ok` et `response.json()`.
6. Générer cartes et flashcards avec `createElement` et `textContent`.
7. Tester succès, vide, 404, schéma invalide et lien dangereux.
8. Créer le manifeste, les icônes, `offline.html` et le service worker.
9. Versionner le cache et limiter sa liste à l’enveloppe statique utile.
10. Tester une première visite en ligne, puis un rechargement hors connexion.
11. Désinstaller ou vider les données du site si un ancien service worker perturbe le test.
12. Faire compléter la preuve 19 sans inventer de résultat.

## Noyau obligatoire et extensions

**Noyau obligatoire :** HTML/CSS/JavaScript natifs, JSON local, quatre états, accessibilité de base, manifeste, service worker simple, page hors connexion et test réel.

**Extensions facultatives :** Bootstrap documenté, API publique sans secret, démonstration PHP, filtres avancés, installation sur appareil et déploiement contrôlé.

## Critère de sortie

Le candidat peut expliquer son architecture, lancer sa PWA depuis un serveur local, démontrer au moins un usage hors connexion et identifier ce qui reste à corriger. Le résultat reste `PRÊT POUR VALIDATION HUMAINE`.
