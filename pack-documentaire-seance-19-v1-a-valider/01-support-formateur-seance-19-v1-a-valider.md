# Support formateur — JSON local et préparation PWA

**Séance :** vendredi 27 novembre 2026 · Semaine 10 · Module 05  
**Édition :** automne V2 documentaire du 25 novembre 2026 · **Statut :** À VALIDER  
**Pilotage :** Prof. Abderrahman EL HISSE · LAB-NUMÉRIQUE-IA

## Intention et entrée

Faire passer le candidat d’un contenu répété dans le HTML à trois objets JSON chargés et affichés par JavaScript. La préparation PWA sert à comprendre l’étape suivante. La V1 de S18 est une entrée à vérifier ; une copie fictive sert de repli si elle manque. Conserver la V1, travailler dans `04-WEB/mini-site-v2/`.

Avant la séance : vérifier navigateur, éditeur et serveur local déjà disponible ; ouvrir page et console ; préparer trois objets fictifs, un JSON avec deux erreurs de syntaxe et les modèles 02, 04, 05 et 12. Prévoir un serveur sur la boucle locale, sans installation en séance. Le logo ou les icônes PWA ne sont pas des prérequis au socle JSON.

## Conducteur — 110 minutes

| Temps | Formateur et relance | Geste candidat | Observation attendue |
|---|---|---|---|
| 0–10 | Ouvrir V1 : « Quelles informations se répètent ? » | Repérer trois cartes et créer V2 | V1 conservée, chemins identifiés |
| 10–30 | Lire objet, tableau, clé, valeur et type | Associer `title`, `category`, `description` aux zones des cartes | Le candidat explique un objet |
| 30–45 | Présenter guillemet manquant et virgule finale | Corriger et parser le JSON | Syntaxe valide ; les champs restent à contrôler |
| 45–65 | Montrer URL → HTTP → réponse → JSON → DOM | Servir V2, modifier un titre, recharger | Carte modifiée et réponse inspectée |
| 65–80 | « Que voit-on si aucune donnée ne revient ? » | Essayer chargement, succès, `[]`, chemin absent | Quatre états visibles et retour au succès |
| 80–95 | Présenter manifeste, service worker, cache | Associer chaque composant à sa fonction | Préparation S20, aucune activation requise |
| 95–110 | Faire rejouer un test par un binôme | Compléter preuve et relais S20 | Résultat observé, écart et correction consignés |

## Démonstration et remédiation

Montrer le fichier JSON avant le code. Modifier une seule donnée, faire prédire la carte concernée, puis recharger. `fetch()` demande une ressource ; une réponse 404 doit être vérifiée avec `response.ok`. Le parsing ne garantit pas la présence des champs attendus. Créer les cartes avec des éléments DOM et `textContent`.

Pour voir le chargement, utiliser le ralentissement réseau du navigateur ou un délai pédagogique explicitement signalé. Pour le vide, remplacer temporairement les données par `[]` dans une copie. Pour l’erreur, viser un chemin absent. Restaurer le fichier et le chemin après chaque essai. Une erreur volontaire doit rester visible jusqu’à sa lecture.

| Difficulté | Relance |
|---|---|
| Double-clic `file://` | Ouvrir depuis le serveur HTTP local |
| JSON parsable mais carte incomplète | Vérifier les clés et leurs types |
| Écran bloqué sur chargement | Observer réseau, exception et traitement d’erreur |
| Ancienne donnée affichée | Vérifier fichier, URL et éventuel ancien service worker |
| V1 absente | Utiliser le cas fictif, noter la personnalisation à reprendre |

## Variante 90 minutes, si ce format est retenu

10 min entrée ; 15 min lecture JSON ; 10 min validation ; 20 min chargement ; 20 min quatre états ; 5 min repères PWA ; 10 min preuve. Total 90 min. Reporter le développement de la préparation PWA vers S20, conserver les quatre tests.

API, PHP et CORS avancé restent facultatifs. Ni publication ni PWA installable ne constituent un résultat exigé de S19. La revue pédagogique et les résultats candidats restent à renseigner.
