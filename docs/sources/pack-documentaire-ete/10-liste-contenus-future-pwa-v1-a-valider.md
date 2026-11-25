# CONTENUS ET STRATÉGIE DE CACHE — PWA DE LA SÉANCE 19

**Version :** V2
**Statut :** À VALIDER  
**Date de révision :** 3 août 2026
**Pilotage humain :** Prof. Abderrahman El Hisse

## 1. Deux niveaux de production

### Niveau candidat — PWA personnelle minimale

Chaque candidat adapte la méthode à sa propre activité : accueil, 6 à 12 contenus publics, cartes, flashcards, quatre états, manifeste, icônes, service worker, cache limité et page hors connexion.

### Niveau atelier — PWA pédagogique enrichie

Le démonstrateur de `D:\Atelier-seance-19` présente neuf ressources couvrant les séances 17 à 19, un laboratoire de scénarios, une comparaison JSON/API/PHP, des filtres et une préparation au déploiement.

Le démonstrateur est une référence d’architecture, pas un contenu à recopier sans adaptation.

## 2. Ressources minimales de la PWA candidat

| Ressource | Fonction | Cache initial |
|---|---|:---:|
| `./` et `index.html` | point d’entrée | oui |
| `offline.html` | message de secours | oui |
| `css/styles.css` | présentation | oui |
| `js/app.js` | logique principale | oui |
| `data/data.json` | contenus publics | oui si stable |
| `manifest.webmanifest` | identité installable | accessible, pas nécessairement précaché |
| `assets/icons/icon-192.png` | petite icône | oui |
| `assets/icons/icon-512.png` | grande icône | oui |
| `service-worker.js` | stratégie de cache | ne pas le précacher manuellement |

Chaque chemin déclaré doit exister. Une ressource absente peut faire échouer l’installation du cache.

## 3. Contenus métier autorisés

- nom public et présentation de l’activité ;
- services ou ressources destinés au public ;
- conseils, étapes, questions fréquentes et flashcards ;
- liens HTTP/HTTPS déjà vérifiés ;
- logo et images dont l’utilisation est autorisée ;
- coordonnées explicitement destinées à être publiques.

## 4. Contenus exclus

- mots de passe, clés API, jetons et identifiants ;
- téléphones ou courriels privés ;
- données clients, candidats ou patients ;
- sauvegardes et rapports internes ;
- fichiers `A-VALIDER` non autorisés pour publication ;
- chemins locaux absolus ;
- archives ZIP et documents de travail inutiles ;
- API ou CDN indispensables au fonctionnement minimal hors connexion.

## 5. Stratégie simple recommandée

```text
installation
→ précacher l’enveloppe statique minimale
→ attendre la fin des écritures importantes

activation
→ supprimer uniquement les anciennes versions du cache de cette PWA

requête
→ utiliser une stratégie simple adaptée au projet
→ ne jamais mettre une réponse HTTP en erreur dans le cache
→ afficher offline.html lorsque la navigation échoue hors connexion
```

Le nom du cache doit être versionné, par exemple `mon-activite-pwa-v1`. Toute évolution importante du noyau exige une nouvelle version.

## 6. Contenus avancés facultatifs

- filtres de catégories ;
- progression locale non nominative ;
- auto-évaluation ;
- génération locale d’une preuve ;
- données structurées Schema.org ;
- Open Graph et Twitter Cards ;
- `robots.txt` et `sitemap.xml` ;
- exemple PHP facultatif ;
- procédure cPanel et retour arrière.

## 7. Contrôle avant validation

```text
[ ] tous les chemins du cache existent
[ ] start_url et scope utilisent ./
[ ] icônes PNG 192 × 192 et 512 × 512
[ ] aucune donnée privée dans les fichiers ou le cache
[ ] service worker limité au bon sous-dossier
[ ] succès, vide et erreurs contrôlés
[ ] responsive contrôlé à 320 px
[ ] clavier et animations réduites contrôlés
[ ] rechargement hors connexion réellement observé
[ ] mise à jour du cache comprise
[ ] plan de retour arrière documenté avant publication
```

## 8. Principe de sélection

```text
contenus publics utiles
+ noyau technique minimal
+ JSON contrôlé
+ cache limité et versionné
- données privées
- dépendances inutiles
- fichiers internes
= PWA claire, légère et transmissible
```
