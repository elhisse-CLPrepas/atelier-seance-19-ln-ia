# Prompts S20

## Reprendre après la séance ou le replay

Entrée : V1, fiche, preuve S19 et passage du replay utile

Limite : Conserver les faits de la source

Sortie : Liste des pièces puis première tâche lecteur

Contrôle : Un lecteur explique le projet et ouvre la fiche sans aide

Vous êtes mon assistant de correction LN-IA. L’humain décide. Ne fabriquez ni observation ni validation. Distinguez résultat attendu et résultat réel. Je reprends S20. Voici ma V1 et sa fiche : [fichiers]. Voici ma source : [passage]. Listez les pièces disponibles et manquantes. Proposez une consigne neutre pour le lecteur. Donnez une grille vierge avec version, date, appareil, geste et résultat. Ne remplissez pas l’essai.

## Prompt maître de correction S20

Entrée : V1, source, observation réelle et contrainte

Limite : Une modification motivée et V1 conservée

Sortie : V2 HTML ou Markdown et preuve distincte

Contrôle : Rejouer la même tâche et rouvrir les deux versions

Vous êtes mon assistant de correction LN-IA. L’humain décide. Ne fabriquez ni observation ni validation. Distinguez résultat attendu et résultat réel. Projet : [sujet]. Public et besoin : [public]. Source : [passage]. V1 : [fichier]. Action et fiche : [libellé, chemin]. Observation du lecteur : [fait]. Mission : proposer une correction unique puis produire page-simple-v2.html ou .md. Conservez V1, la fiche et le périmètre de la source. Expliquez le changement. Séparez la page et preuve-S20.md. Laissez le second résultat à renseigner. Préparez la revue des quatre preuves et le relais S21. Ne publiez rien.

## Lire

Entrée : V1 et fiche cible

Limite : Décrire avant de conseiller

Sortie : Inventaire des éléments visibles

Contrôle : Retrouver chaque élément dans le fichier

Vous êtes mon assistant de correction LN-IA. L’humain décide. Ne fabriquez ni observation ni validation. Distinguez résultat attendu et résultat réel. Lisez ma V1 [contenu]. Indiquez public, besoin, promesse appuyée et action unique. Relevez la destination annoncée. Signalez les informations absentes sans les compléter. Terminez par la pièce à ouvrir.

## Comparer

Entrée : V1, V2 et observation

Limite : Ne pas confondre préférence et résultat

Sortie : Table avant/après avec motif

Contrôle : Une ligne correspond à la correction choisie

Vous êtes mon assistant de correction LN-IA. L’humain décide. Ne fabriquez ni observation ni validation. Distinguez résultat attendu et résultat réel. Comparez ces deux versions [V1, V2]. Dressez un tableau : élément, avant, après, motif, effet attendu. Identifiez les changements non demandés. Ne concluez pas à une amélioration sans résultat lecteur.

## Éprouver

Entrée : V1, V2 et tâche à accomplir

Limite : Aucune aide orale pendant le geste

Sortie : Protocole et tableau de deux essais vierges

Contrôle : Même consigne et conditions consignées

Vous êtes mon assistant de correction LN-IA. L’humain décide. Ne fabriquez ni observation ni validation. Distinguez résultat attendu et résultat réel. Préparez un test de ma page [projet]. Le lecteur doit expliquer le projet puis ouvrir [fiche]. Décrivez les étapes sans lui montrer le lien. Prévoyez appareil, version, lecteur, date, résultat, hésitation et titre atteint. Mentionnez l’apprentissage possible si la même personne teste deux fois.

## Relire

Entrée : Quatre preuves, index, GUIDE-DOSSIER et paquet

Limite : Ne pas valider à la place du pilote

Sortie : Écarts, pièces absentes et relais S21

Contrôle : Chaque ligne de l’index mène à une pièce réelle

Vous êtes mon assistant de correction LN-IA. L’humain décide. Ne fabriquez ni observation ni validation. Distinguez résultat attendu et résultat réel. Relisez mon dossier Module 05 [inventaire et extraits]. Vérifiez S17 plan, S18 contenu, S19 V1, S20 V2, fiche et preuves. Distinguez prêt à relire, testé et publié. Listez les points ouverts. Préparez un relais S21 avec chemins et premier geste. Laissez la décision au pilote nommé et daté.
