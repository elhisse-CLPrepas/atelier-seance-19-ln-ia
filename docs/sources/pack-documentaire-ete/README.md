# PACK DOCUMENTAIRE — SÉANCE 19

## Comprendre le Web et produire une première PWA métier

**Module :** 05 — De la page web simple à la mini-application statique déployable  
**Séance :** 19 — APPROFONDIR ET MANIPULER
**Version :** V1  
**Statut :** À VALIDER  
**Durée recommandée :** 120 minutes
**Pilotage humain :** Prof. Abderrahman El Hisse

## Double rôle de la séance

1. Approfondir les notions Web : HTML, CSS, JavaScript, JSON, requête, réponse HTTP, `fetch()`, API, CORS, PHP, manifeste, service worker, cache, HTTPS et chemins relatifs.
2. Guider une manipulation réelle : transformer le mini-site d’une activité en PWA statique simple, testée localement et préparée pour une validation humaine.

Le démonstrateur validé de `D:\Atelier-seance-19` sert de modèle pédagogique. Le candidat ne doit pas le recopier sans comprendre : il adapte la méthode, les données et l’identité visuelle à sa propre activité.

## Ce dont le candidat a besoin au départ

- une activité ou un projet formulé en une phrase ;
- un public cible et un besoin utilisateur précis ;
- un mini-site V1 fonctionnel, conservé intact ;
- une copie V2 de travail ;
- 6 à 12 contenus publics, fictifs ou autorisés ;
- un logo et, si possible, deux icônes carrées de 192 × 192 et 512 × 512 px ;
- un ordinateur avec navigateur moderne et éditeur de code ;
- un serveur local déjà disponible, par exemple Live Server ou `python -m http.server 8080` ;
- l’autorisation de modifier uniquement la copie V2 ;
- aucun secret, compte client, téléphone privé, courriel privé ou jeton API.

La fiche `12-fiche-depart-projet-activite-pwa-v1-a-valider.md` permet de vérifier ces éléments avant de coder.

## Parcours

```text
projet d’activité cadré
→ V1 sauvegardée et V2 créée
→ contenus autorisés structurés dans data/data.json
→ cartes et flashcards générées avec fetch()
→ états chargement, succès, vide et erreur testés
→ manifeste, icônes, page hors connexion et service worker intégrés
→ cache et mode hors connexion testés
→ preuve 19 et audit final
→ validation humaine avant toute publication
```

## Livrables candidats

- `index.html` ;
- `css/styles.css` ;
- `js/app.js` ;
- `data/data.json` ;
- `manifest.webmanifest` ;
- `service-worker.js` ;
- `offline.html` ;
- `assets/icons/icon-192.png` et `icon-512.png` ;
- `README.md` ;
- `preuve-19-json-pwa.md`.

## Utilisation des supports

1. Vérifier le départ avec la fiche 12.
2. Préparer la séance avec le support 01.
3. Faire remplir la fiche candidat 02.
4. Exécuter les prompts 19-A à 19-F du support 03.
5. Contrôler avec la grille 04.
6. Renseigner la preuve 05.
7. Utiliser le cahier des charges 06 comme référence minimale.
8. Réserver API, CORS et PHP au complément facultatif 07.
9. Utiliser le guide interactif référencé en 08.
10. Expliquer et manipuler la PWA avec le support 09.

## Limites

- aucune publication automatique ;
- aucune API distante nécessaire au cœur de la production ;
- aucune clé privée dans le navigateur ;
- aucun résultat hors connexion annoncé sans test réel ;
- aucune donnée personnelle dans le JSON ou le cache public ;
- toute mise en ligne exige une sauvegarde, HTTPS et une validation humaine.

**Statut maximal produit par l’IA :** `PRÊT POUR VALIDATION HUMAINE`.
