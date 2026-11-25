# Notes formateur S19

Vendredi 27 novembre 2026 · 22 vues · 110 minutes

## 1. JSON local et préparation PWA

Comprendre les mécanismes, puis les mettre à l’épreuve.

- S19 · 27 novembre 2026 : Module 05 · Semaine 10 · 110 minutes
- Point de départ : Un mini-site connu ou le laboratoire V2 fourni
- Résultat : Expliquer, manipuler et conserver une preuve

Geste : Ouvrir le laboratoire et la console.

Note : Présenter le parcours sans demander une PWA complète.

## 2. Pourquoi séparer les données ?

Changer un contenu sans réécrire la structure de chaque carte.

- HTML : Décrit la structure de la page.
- CSS : Met les éléments en forme.
- JavaScript et JSON : Le script charge et affiche ; le JSON décrit les contenus.

Geste : Retrouver un titre dans projets.json et sur la carte.

Note : Faire prédire l’effet d’une modification de titre.

## 3. Une URL désigne une ressource

Le navigateur demande une adresse à un serveur.

- Origine : Protocole, nom d’hôte et port.
- Chemin relatif : ./data/projets.json se résout depuis la page.
- Serveur local : http://127.0.0.1:8080/ pour les essais

Geste : Désigner l’origine et le chemin de l’URL locale.

Note : Écrire l’URL complète avant de parler de fetch.

## 4. La chaîne de chargement

Chaque étape peut réussir ou échouer.

- Demander : URL → requête HTTP
- Lire : Réponse → statut → parsing JSON
- Afficher : Validation des champs → DOM → état visible

Geste : Reformuler la chaîne sans lire la diapositive.

Note : Demander où chercher si la page reste sur Chargement.

## 5. JSON : un format de données

Un tableau rassemble des objets qui portent des clés et des valeurs.

- Tableau : [ ... ] regroupe les ressources.
- Objet : { ... } décrit une ressource.
- Valeur : Chaîne, nombre, booléen, null, objet ou tableau

Geste : Montrer title, sa valeur et son type.

Note : Faire distinguer les accolades des crochets.

## 6. La syntaxe peut être invalide

Le parsing transforme un texte JSON en valeur JavaScript.

- Guillemets doubles : Obligatoires pour les clés et les chaînes.
- Virgules : Séparent les éléments, sans virgule finale.
- JSON.parse : Échoue si le texte ne respecte pas la syntaxe.

Geste : Corriger un guillemet et une virgule finale.

Note : Ne pas assimiler syntaxe valide et données utilisables.

## 7. Le schéma exprime nos attentes

Un JSON parsable peut rester inutilisable pour la page.

- Racine : Un tableau est attendu ici, pas un objet isolé.
- Contrat simple : title, category, description : chaînes non vides
- Contrat du laboratoire : Ajoute id, level, objectives, activity, deliverable, question et answer.

Geste : Repérer pourquoi un champ manquant bloque une ressource.

Note : Expliquer que le contrôle est effectué par des fonctions JavaScript.

## 8. fetch() demande une ressource

Son résultat est une réponse, pas encore le tableau des projets.

- Asynchrone : La page peut montrer un message pendant l’attente.
- response.ok : Vaut vrai pour une réponse HTTP de succès (200 à 299).
- response.json() : Parse le corps ; peut lui aussi échouer.

Geste : Trouver les deux await et la vérification HTTP.

Note : Préciser que fetch ne rejette pas automatiquement une réponse 404.

## 9. Le statut HTTP aide au diagnostic

Distinguer réponse en erreur et absence de réponse.

- 200 : Le serveur a fourni une réponse de succès.
- 404 : Le chemin demandé ne correspond pas à une ressource trouvée.
- Échec réseau : Aucune réponse exploitable ; ce n’est pas forcément une 404.

Geste : Lire le statut et l’URL dans l’onglet Réseau.

Note : Utiliser le scénario 404 et comparer à un arrêt du serveur.

## 10. file:// et HTTP local

Le mode d’ouverture change les possibilités de chargement.

- Double-clic : Le navigateur peut bloquer fetch vers un fichier local.
- Serveur statique : Sert HTML, CSS, JavaScript et JSON sur HTTP.
- Reprise : Lancer le serveur déjà disponible et recharger la bonne URL.

Geste : Ouvrir le laboratoire sur le port 8080.

Note : Le mode intégré hors ligne de l’atelier sera toujours signalé comme une simulation.

## 11. Quatre états à rendre visibles

Le lecteur doit savoir ce qui se passe.

- Chargement : La requête est en cours.
- Succès et vide : Afficher les cartes ou expliquer que la liste est vide.
- Erreur : Donner un diagnostic et permettre une nouvelle tentative.

Geste : Prédire le message avant chaque scénario.

Note : Ne pas remplacer un échec par un écran vide.

## 12. Observer le succès et le vide

Zéro résultat peut être une réponse correcte.

- Succès : Les six ressources du laboratoire sont affichées.
- Vide : [] est un tableau valide sans élément.
- Nettoyage : Retirer les anciennes cartes avant un nouvel affichage.

Geste : Passer du succès au vide puis revenir au succès.

Note : Demander pourquoi le vide ne doit pas afficher une erreur HTTP.

## 13. Lire trois familles d’erreurs

Le lieu de l’échec indique ce qu’il faut vérifier.

- HTTP : Statut 404 : vérifier le chemin.
- Syntaxe : JSON illisible : vérifier guillemets et virgules.
- Structure : Champ absent ou type incorrect : vérifier le contrat.

Geste : Comparer JSON invalide et schéma invalide.

Note : Faire nommer la première étape qui échoue.

## 14. Créer un DOM sûr

Les données textuelles ne doivent pas devenir du code HTML.

- createElement : Crée une structure connue.
- textContent : Insère le texte tel quel.
- Lien : Contrôler son type et son protocole avant href.

Geste : Tester le refus d’un lien javascript:.

Note : Ne jamais exécuter le lien dangereux du scénario.

## 15. Cartes et flashcards accessibles

L’interaction doit être utilisable sans souris.

- Bouton natif : Entrée et Espace déclenchent l’action.
- État annoncé : aria-expanded suit l’ouverture de la réponse.
- Focus : Le contrôle reste visible au clavier.

Geste : Ouvrir puis fermer une flashcard avec le clavier.

Note : Une animation seule ne permet pas de prouver l’accessibilité.

## 16. Sept scénarios pour comprendre

Un scénario change un élément ; le fichier source reste intact.

- Données : Succès, vide et réponse non-tableau
- Erreurs : 404, JSON invalide et schéma invalide
- Sécurité : Lien dangereux refusé

Geste : Noter attendu, observé, cause et retour au succès.

Note : Faire distinguer les simulations des requêtes HTTP réelles.

## 17. JSON local et API

Un même format peut provenir de sources différentes.

- Fichier local servi : Le serveur renvoie un fichier déjà présent.
- API : Une interface peut calculer ou sélectionner une réponse JSON.
- Même vérification : Contrôler HTTP, parsing et structure dans les deux cas.

Geste : Dire si notre laboratoire a besoin d’une API distante.

Note : Réponse attendue : non, le cœur utilise projets.json.

## 18. CORS concerne les origines

Il régit certaines lectures de réponses entre origines.

- Origine : Changer de port peut changer d’origine.
- Serveur : Les en-têtes autorisés se règlent côté serveur concerné.
- Limite : CORS ne protège pas un secret exposé dans JavaScript.

Geste : Comparer localhost:8080 et localhost:8081.

Note : Ne pas proposer de désactiver les protections du navigateur.

## 19. PHP s’exécute côté serveur

Un serveur statique ne transforme pas un fichier PHP en réponse calculée.

- Python statique : Sert les fichiers ; n’interprète pas PHP.
- Serveur PHP : php -S 127.0.0.1:8080, si PHP est déjà disponible
- Facultatif : Arrêter l’autre serveur avant d’utiliser le même port.

Geste : Expliquer le message du bouton PHP sous serveur statique.

Note : La comparaison est guidée ; le candidat n’a pas à installer PHP.

## 20. Passerelle facultative vers la PWA

Comprendre les composants avant de les intégrer.

- Manifeste : Décrit identité, lancement et icônes.
- Service worker et cache : Portée, ressources choisies et version à contrôler.
- Essais futurs : localhost ou HTTPS, coupure réseau et mise à jour en S20

Geste : Ouvrir les simulations de préparation PWA.

Note : Aucun service worker actif ni installation requise dans cette séance.

## 21. Manipuler et expliquer sa correction

La réussite doit pouvoir être rejouée par un tiers.

- Avant : Fichier, valeur et comportement initial
- Après : Correction motivée, état visible et résultat réel
- Rejouer : Rétablir les données et contrôler le retour au succès

Geste : Faire relire un essai par un binôme.

Note : L’IA propose ; le candidat teste ; le pilote statue.

## 22. Conserver la preuve et préparer S20

Une trace distincte des fichiers de l’application.

- Dossier : JSON, script et page dans la copie V2.
- Preuve : Action, attendu, observé, cause, correction et limites
- Relais : Composants PWA à préparer et tests encore à faire

Geste : Exporter puis rouvrir la preuve et le relais.

Note : Ne pas préremplir un résultat humain ou une validation candidate.
