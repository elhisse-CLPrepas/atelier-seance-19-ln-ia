# Rapport de reconstruction — 25 novembre 2026

Mission : reconstruire le pack documentaire S19 pour JSON local et préparation PWA, séance du 27 novembre 2026.

## Réalisation

- 12 fiches et README réécrits pour l’édition automne V2 documentaire, noms historiques conservés.
- Prompt de cadrage copié pour rendre le ZIP autonome sur le plan documentaire.
- Sources et arbitrages documentés ; manifeste des sources avec empreintes SHA-256.
- Pack et ZIP initiaux conservés dans `docs/sauvegardes/pack-S19-avant-reconstruction-20261125-214808.zip`.
- État précédant cette exécution sauvegardé dans `docs/sauvegardes/pack-S19-avant-reconstruction-20261125-214842.zip`.
- ZIP du pack reconstruit à la racine du projet.

## Contrôles exécutés

- Présence des 12 fiches, date du 27 novembre et statut À VALIDER : conforme.
- Liens Markdown relatifs du pack : aucune cible manquante.
- JSON de l’exemple documentaire : parsing réussi, trois objets avec les trois clés attendues.
- Déroulé de référence : 110 minutes ; variante : 90 minutes.
- Archive : comparaison des noms et contenus avec le dossier, contrôle CRC.

## Limites et revue restante

Aucun test navigateur, mobile, PHP, PWA ou hors connexion n’a été exécuté pour cette reconstruction documentaire. Les résultats historiques ne sont pas réutilisés comme preuve de novembre. Mini-site, guide interactif, présentation et PDF existants restent à adapter lors de la construction de la séance. Aucune publication effectuée.

Les sources externes et `docs/sources/pack-documentaire-ete/` restent inchangées. Le pack est À VALIDER : revoir la progression et confirmer durée, horaire, support d’entrée et décisions pédagogiques.

Outil de reconstruction : `tools/rebuild-pack-s19.py`. Chaque relance sauvegarde le pack avant réécriture ; les corrections manuelles doivent être reportées dans cet outil avant relance pour être conservées dans la nouvelle sortie.
