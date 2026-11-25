# Guide du dossier synchronisé S17–S20

## Utiliser la copie

Extraire le ZIP complet, ouvrir index.html et choisir une séance. Les liens sont relatifs. Les fichiers Markdown se lisent dans un éditeur ; le navigateur peut les télécharger. Les liens externes nécessitent Internet.

## Carnets et preuves

Le carnet transversal 01-SUIVI/carnet-module05.html distingue les quatre séances et sauvegarde ses propres saisies dans le navigateur. Exporter son JSON pour la reprise, une preuve Markdown par séance et un bilan global. Aucun téléchargement n’écrit automatiquement dans le dossier. Comparer avant de remplacer une preuve existante.

Le carnet S17 d’origine est conservé. Les carnets des ateliers et le carnet transversal ont des formats différents : ne pas les confondre ni changer leur signature. Utiliser les fichiers et les preuves Markdown pour assurer la continuité.

## Manipuler le Web

S17 : démonstration et carnet d’essai. S18 : production fictive Déclic Web et sources/trio de production. S19 : exemples dans 04-WEB/EXEMPLES-ATELIERS/S19 ; laboratoire enrichi à six ressources et exemple simple à trois champs. S20 : exemple Cap Études V1/V2 et protocole lecteur.

Pour fetch, servir la racine de ce dossier avec `python -m http.server 8081 --bind 127.0.0.1`, puis ouvrir http://127.0.0.1:8081/. Les simulations PWA ne sont pas une installation ni un fonctionnement hors connexion réel.

## Passage S19 → S20

Lire 01-SUIVI/passage-S19-S20.md. L’importeur S20 actuel ne reconnaît pas le carnet JSON du parcours S19 refondu ni le carnet transversal. Pour un site enrichi, reprendre le code dans l’éditeur et conserver deux versions ; utiliser la revue lecteur et la preuve S20 sans forcer l’import.

## Conservation et diffusion

Les sources d’ateliers ont été lues sans modification. Les références sont copiées dans 00-SOURCES/ATELIERS avec leurs empreintes. Les productions et preuves préexistantes ne sont pas écrasées. Les nouveaux modèles sont regroupés dans 06-PORTFOLIO/modeles-alignes. L’ancien index est conservé ; INDEX-PARCOURS-S17-S20.md décrit le parcours courant.

La copie publique de S19 et son ZIP se reconstruisent depuis ce dossier avec tools/sync-challenge.py à la racine de l’atelier. La synchronisation ne réinitialise pas les saisies ou preuves et ne publie rien.
