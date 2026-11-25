# Atelier S19 · JSON local et préparation PWA

**Vendredi 27 novembre 2026 · Semaine 10 · 110 minutes**  
LAB-NUMÉRIQUE-IA · Prof. Abderrahman EL HISSE

L’atelier présente les notions et mécanismes Web avant la production : JSON et schéma, fetch et HTTP, quatre états, DOM sûr, cartes et flashcards, scénarios d’erreur et comparaison JSON/API/CORS/PHP. La PWA reste une passerelle facultative, sans service worker actif.

## Ouvrir

- [OUVRIR-SEANCE-19.html](OUVRIR-SEANCE-19.html) : les onze rubriques, avec scripts et styles intégrés.
- [PROJECTION-SEANCE-19.html](PROJECTION-SEANCE-19.html) : démarrer les 22 vues.
- Garder ces fichiers à côté de dist, qui contient les ressources, le logo et les laboratoires.

Le portable fonctionne en double-clic. Sa démonstration utilise alors des données intégrées et signale les simulations. Pour observer les véritables requêtes et statuts HTTP :

```powershell
python -m http.server 8080 --bind 127.0.0.1 --directory dist
```

Ouvrir http://127.0.0.1:8080/. Python doit être déjà disponible.

## Développer et reconstruire

```powershell
npm.cmd run dev
npm.cmd run build
npm.cmd run check
```

Le projet conserve Vite, Bootstrap local, les icônes locales et le thème LN-IA. La construction synchronise HTML, PDF, PowerPoint, kits et entrées portables ; elle utilise aussi Python et ReportLab déjà présents sur ce poste. Les sources éditoriales sont src/seance.json et tools/refonte-content-s19.py.

## Les onze rubriques

Accueil ; présentation ; méthode ; démonstration avec sept scénarios ; atelier JSON et trace personnelle ; prompts 19-A à 19-F ; douze flashcards ; huit questions de quiz avec explication des trois choix ; validation sur sept critères ; portfolio ; ressources locales et externes.

Le carnet JSON est distinct de l’ancien carnet d’assemblage. Les preuves et résultats candidats ne sont pas préremplis. Un statut VALIDÉ nécessite des observations et une revue renseignées ; une modification entraîne une nouvelle revue.

## Sources et périmètre

La fiche [seance-19-json-pwa-v2.md](seance-19-json-pwa-v2.md), le [README S19 V2](05-EXEMPLES-CODE/mini-site-seance-19-V2/README.md) validé par le pilote et les informations de synchronisation fondent cette refonte. Le pack V3 est conservé sans mise à jour et son extension de périmètre n’est pas retenue. Les sources C: et les anciens carnets sont préservés.

Voir [le rapport de refonte](docs/MISE-A-JOUR-S19.md), [la recette navigateur](docs/recette-navigateur-S19.json) et [l’audit des fichiers](docs/audit-refonte-S19.json).
