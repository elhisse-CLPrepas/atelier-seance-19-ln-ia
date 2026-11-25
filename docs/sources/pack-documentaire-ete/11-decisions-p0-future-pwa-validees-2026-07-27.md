# DÉCISIONS HUMAINES — FONDATION P0 DE LA PWA MODULE 05

**Date de la décision initiale :** 27 juillet 2026
**Statut historique :** VALIDÉ POUR CONSTRUCTION DE LA FONDATION P0
**Révision de cadrage :** 3 août 2026
**Statut actuel :** DÉCISION HISTORIQUE REMPLACÉE POUR LA SÉANCE 19
**Pilote humain :** Prof. Abderrahman El Hisse

## Avertissement de lecture

La décision du 27 juillet autorisait seulement une fondation chargeant des JSON et utilisant une progression locale. Elle reportait le manifeste, le service worker et le cache.

Le cadrage pédagogique confirmé le 3 août 2026 étend la séance 19 : lorsque les prérequis sont réunis, le candidat peut construire et tester localement une PWA statique minimale. Cette extension n’autorise pas une publication automatique.

## Décision initiale conservée

- nom public : **Atelier LN-IA — Module 05** ;
- nom court : **LN-IA M05** ;
- scope envisagé : **`/app-module-05/`** ;
- nature : application statique pédagogique, sans compte ni collecte ;
- contenus P0 : accueil, séances 17 à 20, projets fictifs, prompts candidats, ressources publiques et progression locale non nominative.

Les prompts 17-A, 17-B, 18-A à 18-F et 19-A à 19-F étaient destinés à être publiables après validation. Les prompts maîtres, sauvegardes et rapports internes restaient exclus.

## Décision actualisée pour la séance 19

Sont désormais autorisés dans une copie locale contrôlée :

- `manifest.webmanifest` ;
- icônes 192 × 192 et 512 × 512 ;
- `offline.html` ;
- enregistrement d’un service worker ;
- cache versionné et limité ;
- test du fonctionnement hors connexion ;
- adaptation du démonstrateur au projet personnel du candidat.

## Conditions obligatoires

```text
[ ] V1 sauvegardée et V2 distincte
[ ] contenus publics, fictifs ou autorisés
[ ] aucun secret ni donnée personnelle
[ ] serveur local ou HTTPS
[ ] chemins relatifs et périmètre contrôlé
[ ] résultats hors connexion réellement testés
[ ] preuve 19 renseignée
[ ] validation humaine avant publication
```

## Ce qui reste interdit sans nouvelle décision

- publication automatique ;
- remplacement d’une version publique sans sauvegarde ;
- connexion d’une API privée ;
- stockage d’un secret dans le navigateur ;
- collecte de données personnelles ;
- annonce d’un résultat non testé ;
- modification d’un budget, d’un hébergement ou d’un domaine sans validation.

## Traçabilité

La décision P0 initiale est conservée dans les sauvegardes datées. Le présent fichier documente explicitement son remplacement partiel afin d’éviter qu’un ancien cadrage soit appliqué comme instruction actuelle.

**Statut maximal de la production :** `PRÊT POUR VALIDATION HUMAINE`.
