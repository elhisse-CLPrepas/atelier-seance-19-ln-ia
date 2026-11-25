# Ressources embarquées — S19 du 27 novembre 2026

**Version :** V3 · **Statut du pack :** VALIDÉ POUR UTILISATION EN S19.

- [Exemple minimal : socle candidat](mini-sites/mini-site-json-seance-19-v1-a-valider/index.html) : trois objets, champs title/category/description, quatre états, validation des champs ajoutée.
- [Laboratoire S19 enrichi](mini-sites/mini-site-seance-19-V2/index.html) : six ressources, filtres, flashcards et scénarios. Son schéma ajoute id, level, objectives, activity, deliverable, question et answer, avec lien facultatif contrôlé.
- [Démonstration S17](mini-sites/mini-site-demonstration-seance-17-v1-a-valider/index.html) : repère historique pour les prérequis HTML/CSS/JavaScript.
- [Préparation PWA du socle](mini-sites/mini-site-json-seance-19-v1-a-valider/preparation-pwa.html) : simulations conceptuelles, aucun cache actif.

Depuis la racine du pack : `python -m http.server 8080 --bind 127.0.0.1`, puis ouvrir `http://127.0.0.1:8080/OUVRIR-LE-PACK.html`. Le double-clic permet de lire les documents HTML mais ne remplace pas le serveur pour fetch().

Le guide historique `SORTIES/GUIDE-SUIVI-SEANCE-19-HTML-V1-A-VALIDER/` n’est pas inclus dans ce pack. Il ne constitue pas une dépendance du parcours courant. Les trois mini-sites sont autonomes sur le plan de leurs fichiers locaux.
