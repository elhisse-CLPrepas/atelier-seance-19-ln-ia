"""Reconstruction documentaire S19 : lit les sources d'été, sauvegarde le pack,
écrit ses fiches d'automne et son ZIP. Aucun accès réseau ni modification source.
Exécution : python tools/rebuild-pack-s19.py
"""
from pathlib import Path
import hashlib
import json
import re
import zipfile
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / 'pack-documentaire-seance-19-v1-a-valider'
SOURCE = Path('C:/DEV/CHALLENGE-01-Juin-2026/05-PROGRAMME-PEDAGOGIQUE/MODULE-05')
STAMP = datetime.now().strftime('%Y%m%d-%H%M%S')
BACKUP = ROOT / 'docs' / 'sauvegardes' / f'pack-S19-avant-reconstruction-{STAMP}.zip'
BACKUP.parent.mkdir(parents=True, exist_ok=True)
INITIAL_BACKUP = next(iter(sorted(BACKUP.parent.glob('pack-S19-avant-reconstruction-*.zip'))), BACKUP)
with zipfile.ZipFile(BACKUP, 'w', zipfile.ZIP_DEFLATED) as z:
    for p in sorted(PACK.rglob('*')):
        if p.is_file():
            z.write(p, p.relative_to(ROOT))
    old_zip = ROOT / f'{PACK.name}.zip'
    if old_zip.exists():
        z.write(old_zip, old_zip.name)

files = {p.name[:2]: p.name for p in PACK.glob('[0-9][0-9]-*.md')}
comparison = []
for p in sorted(PACK.glob('*.md')):
    original = SOURCE / '01-SEANCES' / PACK.name / p.name
    if original.exists():
        comparison.append({'file': p.name, 'identical_before_rebuild': p.read_bytes() == original.read_bytes()})
HEADER = ('**Séance :** vendredi 27 novembre 2026 · Semaine 10 · Module 05  \n'
          '**Édition :** automne V2 documentaire du 25 novembre 2026 · **Statut :** À VALIDER  \n'
          '**Pilotage :** Prof. Abderrahman EL HISSE · LAB-NUMÉRIQUE-IA\n\n')

def doc(key, title, body):
    (PACK / files[key]).write_text(f'# {title}\n\n{HEADER}{body.strip()}\n', encoding='utf-8')

doc('01', 'Support formateur — JSON local et préparation PWA', '''
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
''')
doc('02', 'Fiche candidat — Séparer et charger les données', '''
## Votre mission

Transformer trois cartes de votre mini-site en données JSON, les charger depuis un serveur local et expliquer ce que voit le lecteur dans quatre situations. Vous préparez ensuite les composants PWA pour S20.

Projet : __________ · Public : __________ · Besoin : __________
V1 conservée : __________ · Copie V2 : __________ · Serveur disponible : __________

1. Remplissez la fiche de départ 12. Si votre V1 manque, utilisez la copie fictive indiquée par le formateur.
2. Repérez titre, catégorie et description sur trois cartes. Retrouvez ces champs dans `data/projets.json`.
3. Vérifiez tableau, objets, guillemets et virgules. Contrôlez que chaque champ attendu contient une chaîne non vide.
4. Ouvrez V2 depuis le serveur local. Modifiez un titre du JSON puis rechargez. Montrez la carte modifiée.
5. Vérifiez dans la console et le panneau Réseau le chemin demandé, le statut HTTP et les données reçues.
6. Testez les quatre situations du tableau. Rétablissez les données après l’essai.
7. Expliquez manifeste, service worker et cache avec la fiche 09, puis remplissez la preuve 05.

| Situation | Manipulation | Résultat attendu | Résultat observé |
|---|---|---|---|
| Chargement | Ralentir la requête | Message « Chargement… » | À COMPLÉTER |
| Succès | Charger les trois objets | Trois cartes avec les bons textes | À COMPLÉTER |
| Vide | Charger une copie contenant `[]` | Message « Aucun projet à afficher » | À COMPLÉTER |
| Erreur | Demander un chemin absent | Message compréhensible et nouvelle tentative possible | À COMPLÉTER |

## Ce que vous remettez

Votre dossier `04-WEB/mini-site-v2/` avec page, styles, JSON, JavaScript et README ; `06-PORTFOLIO/preuve-S19.md` ; `06-PORTFOLIO/relais-S20.md` ; une entrée dans l’index du portfolio. Gardez V1 et V2 distinctes.

Expliquez à un binôme : quelle donnée a changé ? Quel code la charge ? Comment distinguez-vous vide et erreur ? Quel rôle aura le service worker en S20 ? Une case cochée ou un quiz réussi ne vaut pas validation du projet.
''')
prompts = [
('19-A', 'Auditer la V1 et choisir les données', 'V1 et fiche de départ 12', 'Lire sans modifier. Inventorier HTML, styles et JavaScript. Repérer trois cartes répétitives, proposer leurs champs et identifier les données autorisées et exclues. Vérifier les prérequis et proposer une copie V2.', 'Inventaire, correspondance champs/cartes, chemins V1/V2 et points manquants.', 'Un tiers retrouve les trois contenus dans la V1.'),
('19-B', 'Structurer et valider le JSON', 'Inventaire 19-A et trois contenus fictifs', 'Dans la copie V2 autorisée, créer ou adapter data/projets.json : tableau de trois objets avec title, category et description, chaînes non vides. Expliquer objets, clés et types. Vérifier syntaxe et structure. Fournir séparément un exercice contenant un guillemet manquant et une virgule finale, puis sa correction.', 'JSON valide, explication des champs et exercice corrigé.', 'Parsing réussi et chaque objet respecte les champs attendus.'),
('19-C', 'Charger les données', 'V2 et JSON contrôlé en 19-B', 'Adapter js/app.js et la page : fetch relatif, contrôle response.ok, parsing et validation de structure. Construire les cartes avec createElement et textContent. Utiliser les styles locaux. Expliquer la chaîne URL → HTTP → JSON → DOM et le lancement local déjà disponible.', 'Fichiers modifiés et diff expliqué, commande locale et correspondance des champs.', 'Une modification du titre JSON se retrouve sur la bonne carte après rechargement.'),
('19-D', 'Éprouver les quatre états', 'Chargement 19-C et copie de test', 'Rendre chargement, succès, vide et erreur visibles. Vider les anciennes cartes avant un nouvel affichage. Prévoir une nouvelle tentative. Donner les manipulations reproductibles : ralentissement, trois objets, tableau vide et chemin absent. Restaurer ensuite la configuration de succès.', 'Gestion des états et protocole avec attendu/observé séparés.', 'Chaque état peut être provoqué, expliqué et suivi d’un retour au succès.'),
('19-E', 'Auditer sans modifier', 'V2, README et résultats des quatre tests', 'Lire les fichiers sans correction automatique. Examiner syntaxe JSON, schéma attendu, chemins, response.ok, gestion des exceptions, textContent, messages visibles, clavier, mobile et absence de données sensibles. Vérifier que la PWA reste une préparation.', 'Rapport : conforme, bloquant, à corriger, non testé ; chemin et motif de chaque écart.', 'Chaque conclusion est reliée à un fichier ou à un essai documenté.'),
('19-F', 'Documenter et préparer S20', 'Rapport 19-E et observations réellement disponibles', 'Compléter README, preuve-S19.md, entrée d’index et relais-S20.md. Distinguer attendu, observé et non testé. Rappeler comment lancer le serveur, restaurer le JSON et reproduire les quatre états. Décrire les composants PWA à préparer, sans les activer.', 'Documentation, preuve et relais ; rapport des fichiers écrits et tests exécutés.', 'Un tiers peut rouvrir V2, rejouer un test et identifier le premier geste S20.'),
]
body = '''## Cadre commun à copier avant chaque mission

```text
Vous êtes l’assistant pédagogique LN-IA. Préparez S19 du 27 novembre 2026 : JSON local et préparation PWA.
Projet = [NOM] ; V1 = [CHEMIN] ; V2 = [CHEMIN] ; serveur disponible = [OUTIL].
Travaillez dans la copie V2 et les fichiers de preuve indiqués. Lisez les instructions locales.
Conservez une sauvegarde avant modification ; respectez les autorisations déjà données.
Utilisez des données fictives ou autorisées, JavaScript natif et des ressources locales.
N’installez pas de dépendance. N’ajoutez ni API distante, ni secret, ni service worker actif, ni déploiement.
Expliquez les modifications. Signalez les entrées manquantes et les limites.
Terminez par les fichiers lus, créés ou modifiés, les tests exécutés et les essais restants.
Ne renseignez jamais une observation humaine à sa place. Statut de sortie : À VALIDER.
```
'''
for code, title, inputs, mission, outputs, test in prompts:
    body += f'\n## {code} — {title}\n\n```text\nEntrées : {inputs}.\nMission : {mission}\nSorties : {outputs}\nRéussite : {test}\n```\n'
doc('03', 'Prompts candidats — 19-A à 19-F', body)
doc('04', 'Grille de contrôle — Données, affichage et compréhension', '''
Pour chaque critère, renseigner « réussi », « échec » ou « à tester ». Ajouter chemin et observation. Le parsing vérifie la syntaxe, pas à lui seul le modèle des données.

| ID | Critère et essai | Attendu | Résultat / preuve |
|---|---|---|---|
| C01 | Ouvrir V1 et V2 | Versions distinctes, V1 conservée | À COMPLÉTER |
| C02 | Parser projets.json | Tableau lisible de trois objets | À COMPLÉTER |
| C03 | Contrôler les champs | title/category/description : chaînes non vides | À COMPLÉTER |
| C04 | Modifier un titre | Bonne carte mise à jour | À COMPLÉTER |
| C05 | Inspecter la requête | HTTP local, chemin relatif, réponse vérifiée | À COMPLÉTER |
| C06 | Ralentir le réseau | Chargement visible | À COMPLÉTER |
| C07 | Charger trois objets | Succès : trois cartes | À COMPLÉTER |
| C08 | Charger [] | Message vide, aucune ancienne carte | À COMPLÉTER |
| C09 | Demander un chemin absent | Erreur lisible, nouvelle tentative possible | À COMPLÉTER |
| C10 | Rétablir fichier et chemin | Retour au succès | À COMPLÉTER |
| C11 | Contrôler DOM et données | textContent, aucune donnée privée ni secret | À COMPLÉTER |
| C12 | Clavier et largeur 320 px | Contrôles utilisables, textes lisibles sans débordement | À COMPLÉTER |
| C13 | Reformuler PWA | Fonctions manifeste/service worker/cache distinguées | À COMPLÉTER |
| C14 | Rouvrir preuve et relais | Tests traçables, prochaine étape S20 identifiée | À COMPLÉTER |

Erreur de JSON, chargement bloqué, erreur masquée ou données non autorisées : corriger avant de soumettre. Un essai absent reste « à tester ». Le hors connexion et l’installation ne sont pas des critères du socle S19.

Décision du pilote : __________ · Date : __________ · Observations : __________
Statut proposé : À COMPLÉTER / À REVOIR / À VALIDER. VALIDÉ exige la décision humaine datée.
''')
doc('05', 'Modèle de preuve — S19 JSON local et préparation PWA', '''
Copier ce modèle dans `06-PORTFOLIO/preuve-S19.md`. Le nom historique de la présente fiche est conservé pour les liens du pack.

## Identification

- Projet et candidat : À COMPLÉTER
- Date réelle de manipulation : À COMPLÉTER
- Version V1 conservée et chemin V2 : À COMPLÉTER
- Navigateur, serveur, URL locale : À COMPLÉTER
- Statut de la preuve : À COMPLÉTER

## Correspondance données / affichage

| Champ | Type attendu | Élément visible | Chemin du fichier |
|---|---|---|---|
| title | chaîne non vide | titre de carte | À COMPLÉTER |
| category | chaîne non vide | catégorie | À COMPLÉTER |
| description | chaîne non vide | paragraphe | À COMPLÉTER |

## Essais réalisés

| Essai | Action reproductible | Attendu | Observé | Statut, écart et correction |
|---|---|---|---|---|
| Syntaxe et champs | Parser et contrôler les objets | JSON et champs conformes | À COMPLÉTER | À TESTER |
| Chargement | Ralentir la requête | Message visible | À COMPLÉTER | À TESTER |
| Succès | Charger trois objets | Trois cartes | À COMPLÉTER | À TESTER |
| Vide | Utiliser [] dans la copie | Message vide | À COMPLÉTER | À TESTER |
| Erreur | Utiliser un chemin absent | Message erreur | À COMPLÉTER | À TESTER |
| Restauration | Rétablir données et chemin | Succès retrouvé | À COMPLÉTER | À TESTER |
| Clavier/mobile | Tabuler et réduire à 320 px | Contrôles et textes utilisables | À COMPLÉTER | À TESTER |

## Compréhension et limites

Une modification que je peux expliquer : À COMPLÉTER.
Pourquoi utiliser HTTP local plutôt que file:// : À COMPLÉTER.
Rôles du manifeste, du service worker et du cache : À COMPLÉTER.
Essais non réalisés et difficultés : À COMPLÉTER.

## Relais S20

Copier aussi dans `06-PORTFOLIO/relais-S20.md` : chemin V2 et version ; état des quatre tests ; ressources publiques à rendre disponibles hors connexion ; composants PWA à préparer ; premier geste de reprise ; questions au formateur. Ajouter des liens relatifs vers V2 et la preuve dans l’index du portfolio.

## Décision humaine

Pilote : À COMPLÉTER · Date : À COMPLÉTER · Observation : À COMPLÉTER.
Décision : À COMPLÉTER. Aucun statut de validation n’est prérempli.
''')
doc('06', 'Cahier des charges — Exemple JSON minimal S19', '''
## Architecture cible

```text
04-WEB/mini-site-v2/
  index.html
  assets/styles.css
  data/projets.json
  js/app.js
  README.md
06-PORTFOLIO/
  preuve-S19.md
  relais-S20.md
```

Les anciens exemples peuvent utiliser `css/styles.css` ; conserver ce chemin si la page le référence correctement. Les noms anciens `05-web/` et `preuve-19-json-pwa.md` restent des repères d’été.

## Contrat des données

`projets.json` contient un tableau. Chaque objet porte `title`, `category` et `description`, chaînes non vides. Exemple fictif adapté à Déclic Web :

```json
[
  {"title":"Préparer sa page", "category":"Méthode", "description":"Ordonner les sections de son projet."},
  {"title":"Relire ses contenus", "category":"Contrôle", "description":"Vérifier les formulations et les sources."},
  {"title":"Vérifier ses liens", "category":"Pratique", "description":"Ouvrir la pièce annoncée depuis la page."}
]
```

Pour tester le vide, un tableau `[]` reste valide. Un objet racine, un JSON mal formé, un champ absent ou de mauvais type doit produire une erreur compréhensible. Ne pas injecter les chaînes comme HTML.

## Comportement attendu

1. Afficher le chargement et retirer les anciennes cartes.
2. Demander `./data/projets.json` avec `fetch()` et vérifier `response.ok`.
3. Parser la réponse, vérifier tableau et champs.
4. Afficher vide si le tableau est vide ; sinon créer les cartes avec `textContent`.
5. Intercepter les erreurs réseau, HTTP, syntaxe et structure ; afficher un message lisible et proposer de réessayer.

La zone d’état peut utiliser `role="status"` et `aria-live="polite"`. Prévoir titres hiérarchisés, focus visible et adaptation mobile. Aucun CDN ni API ne doit être indispensable. Aucun manifeste ni service worker actif n’est nécessaire.

## Lancement et recette

Depuis le dossier V2, si Python est déjà disponible :

```powershell
python -m http.server 8080 --bind 127.0.0.1
```

Ouvrir `http://127.0.0.1:8080/`, observer les quatre états avec la fiche 04, puis arrêter le serveur par Ctrl+C. Si le port est occupé, choisir un port libre et adapter l’URL. Un serveur statique sert les fichiers ; il n’exécute pas PHP.

Les références d’été sont inventoriées dans SOURCES-ET-SYNCHRONISATION.md. Ce cahier des charges documente la cible ; il n’atteste pas que le mini-site actuel a déjà été reconstruit ou testé.
''')
doc('07', 'Complément formateur — JSON local, API, CORS et PHP', '''
Hors du socle et des 110 minutes. Aucun candidat n’a besoin d’API, de PHP ni de compte pour réussir S19.

| Notion | Explication utile |
|---|---|
| Fichier JSON | Ressource statique servie par HTTP, puis interprétée par JavaScript |
| API | Interface pouvant retourner du JSON calculé ou sélectionné |
| PHP | Code exécuté par un serveur compatible, dont le navigateur reçoit la réponse |
| CORS | Mécanisme HTTP régissant la lecture de certaines réponses entre origines |

Une origine dépend du protocole, du nom d’hôte et du port. Changer de port peut donc changer d’origine. Une erreur CORS ne justifie pas de désactiver les protections du navigateur. CORS ne protège pas une clé placée dans le JavaScript livré.

Si PHP est déjà disponible et si la démonstration est retenue, arrêter le serveur statique avant de démarrer, dans le dossier de démonstration :

```powershell
php -S 127.0.0.1:8080
```

Comparer la réponse d’un fichier JSON et celle de `api.php` du démonstrateur source. Vérifier le statut et le contenu réellement retournés. Ne pas ouvrir un fichier PHP comme une page locale ; un serveur statique ne l’interprète pas et peut en exposer le texte. N’utiliser aucun secret, appel externe ou donnée personnelle. Revenir ensuite à l’exemple JSON local.

Observations de la démonstration : À COMPLÉTER. Aucun essai PHP n’est attesté par cette fiche.
''')
doc('08', 'Référence — Guide HTML interactif et ressources d’été', '''
## Ressources repérées dans MODULE-05 source

- `SORTIES/GUIDE-SUIVI-SEANCE-19-HTML-V1-A-VALIDER/index.html` : guide de suivi historique.
- `05-EXEMPLES-CODE/mini-site-json-seance-19-v1-a-valider/` : exemple minimal, trois objets title/category/description.
- `05-EXEMPLES-CODE/mini-site-seance-19-V2/` : laboratoire enrichi ; son README annonce une PWA inactive, six ressources et sept scénarios.
- `00-ENTREE-SEANCE-19/` : point d’entrée historique.

Le dossier source exact est indiqué dans SOURCES-ET-SYNCHRONISATION.md. Ces références sont locales au poste du formateur et ne constituent pas des liens portables dans un ZIP distribué.

## Usage pour novembre

Utiliser le guide comme référence à adapter. Rouvrir d’abord le prompt de cadrage courant et les prompts 19-A à 19-F du présent pack. Toute étape historique qui demande une PWA complète, un service worker ou une validation d’été doit être replacée dans la préparation S20.

Le parcours de novembre est : fiche de départ → V1 conservée/V2 → trois objets → fetch local → quatre états → preuve → préparation PWA. Les scénarios avancés du laboratoire sont des compléments possibles après le socle.

## Contrôle avant remise d’un guide reconstruit

- Dates, thème, durée et chemins alignés sur le présent pack.
- Prompts identiques à la fiche 03 et preuve initialement vierge.
- Aucun résultat de test ni décision précochée.
- Exports séparant production et preuve, puis réouverture des fichiers exportés.
- Clavier, mobile, copie, impression et éventuelle remise à zéro contrôlés.
- Aucune activation de service worker dans le parcours essentiel.

La présente mise à jour reconstruit le pack Markdown. Le guide historique et le mini-site existant ne sont pas reconstruits par cette fiche ; leur recette interactive reste à effectuer lors de leur adaptation.
''')
doc('09', 'Préparation PWA — Comprendre avant d’intégrer en S20', '''
## Point de départ

En S19, la V2 charge le JSON et rend visibles les quatre états. Une PWA, ou application web progressive, ajoute des composants et des comportements à contrôler. Un affichage mobile ou un fichier manifeste ne prouve pas le fonctionnement hors connexion.

| Composant | Fonction | Travail préparatoire S19 | Essai à prévoir en S20 |
|---|---|---|---|
| Manifeste | Décrire identité et lancement | Choisir nom, nom court, start_url et scope | Chemins, icônes et prise en compte navigateur |
| Icônes | Identifier l’application | Prévoir des images autorisées | Dimensions, formats, rendu |
| Service worker | Traiter des événements et requêtes dans son périmètre | Repérer son rôle et sa portée | Enregistrement, activation, périmètre |
| Cache | Conserver certaines ressources | Sélectionner le noyau public utile | Ressources réellement disponibles et mise à jour |
| Page de repli | Expliquer une navigation indisponible | Rédiger le message attendu | Navigation hors connexion hors cache |
| localhost / HTTPS | Contexte nécessaire aux usages concernés | Distinguer local et hébergement public | Contexte sécurisé et absence d’erreurs |

## Chaîne de compréhension

URL → requête HTTP → réponse et statut → parsing JSON → contrôle des champs → création DOM → état visible. Le cache introduira une autre provenance possible de la réponse : il faudra savoir quelle version est servie.

## Fiche de préparation

Nom public : __________ · Nom court : __________.
Racine et périmètre envisagés : __________.
Ressources publiques utiles sans réseau : __________.
Ressources distantes qui pourraient manquer : __________.
Message de repli : __________.
Version de cache envisagée : __________.

En S19, aucun enregistrement de service worker n’est exigé. Une ancienne application enregistrée sur la même origine peut perturber les essais : faire vérifier son périmètre par le formateur.

## Protocole à préparer pour S20

Conserver une copie de V2 ; intégrer les composants dans une nouvelle version ; contrôler les chemins ; charger en ligne ; vérifier le service worker actif ; couper le réseau ; recharger ; essayer une navigation non cachée ; revenir en ligne ; modifier une ressource et la version ; observer la mise à jour. Ne supprimer que les anciens caches de cette application.

Ces essais sont futurs : laisser leurs résultats à renseigner. La possibilité d’installation dépend aussi du navigateur et de la plateforme. cPanel reste un contexte de déploiement ultérieur, soumis à une décision distincte.
''')
doc('10', 'Inventaire de contenus — V2 JSON et future PWA', '''
## Deux étapes distinctes

Le socle S19 utilise trois objets fictifs. Des cartes supplémentaires, flashcards et filtres peuvent enrichir une autre version après maîtrise des quatre états. La PWA et son cache se préparent pour S20.

| Ressource | S19 | Préparation S20 |
|---|---|---|
| index.html | Point d’entrée fonctionnel | Candidat au noyau hors connexion |
| assets/styles.css ou css/styles.css | Mise en forme locale | Vérifier chemin et version |
| js/app.js | fetch, contrôles et états | Prévoir une stratégie de mise à jour |
| data/projets.json | Trois objets publics ou fictifs | Définir fraîcheur et comportement sans réseau |
| Images réellement utilisées | Locales et autorisées | Sélectionner seulement les utiles |
| manifest.webmanifest | Fonction expliquée | Préparer identité et périmètre |
| Icônes 192 et 512 px | Non exigées pour JSON | Préparer les fichiers adaptés |
| offline.html | Message envisagé | Tester le repli réel |
| service-worker.js | Non activé | Préparer portée et cache versionné |
| Preuves et rapports | Dans le portfolio | Exclus du cache public |

## Inventaire à remplir

| Chemin réel | Utilité | Origine / droits | Public ? | Utile hors connexion ? | Décision |
|---|---|---|---|---|---|
| À COMPLÉTER | À COMPLÉTER | À COMPLÉTER | À COMPLÉTER | À COMPLÉTER | À COMPLÉTER |

Exclure secrets, coordonnées privées, dossiers candidats, sauvegardes, rapports internes et archives de travail. Ne pas mettre en cache une erreur HTTP. Ne pas précacher manuellement le fichier du service worker. Limiter le cache à l’application, versionner son nom et prévoir comment observer une mise à jour. Une ressource externe indispensable peut rendre le parcours incomplet sans réseau.

Les champs title/category/description sont le contrat commun de S19 ; toute évolution de ce contrat doit être reportée dans le code, les consignes et la preuve.
''')
doc('11', 'Traçabilité du cadrage — Fondation P0 et édition de novembre', '''
Le nom historique `11-decisions-p0-future-pwa-validees-2026-07-27.md` est conservé pour préserver les liens. Il ne constitue pas une validation du pack de novembre.

## Chronologie et arbitrage

| Repère | Ce que les documents examinés indiquent | Traitement en novembre |
|---|---|---|
| 27 juillet 2026 | Fiche S19 : JSON local, quatre états, découverte PWA, 110 minutes ; intégration manifeste/service worker en S20 | Base du présent pack |
| Révisions d’août | Plusieurs fiches du pack local demandent une PWA minimale dès S19 et 120 minutes | Extension retirée du socle courant |
| Démonstrateur source V2 | README : PWA inactive, scénarios JSON enrichis | Ressource technique complémentaire |
| Ancienne édition d’automne | Page V1 et fiche locale comme objectif commun | V1 utilisée comme entrée ou repli |
| Demande du pilote, 25 novembre 2026 | Synchroniser le cadrage du 27 juillet pour S19 du 27 novembre | Prompt dédié et reconstruction documentaire |

La fondation historique évoquait le nom « Atelier LN-IA — Module 05 », le nom court « LN-IA M05 » et le scope `/app-module-05/`. Ces valeurs décrivent un projet d’atelier historique ; elles ne sont pas imposées au projet personnel du candidat.

## Cadre appliqué au pack

V1 préservée ; copie V2 ; trois objets ; serveur local ; quatre états ; preuve distincte ; préparation S20. API, PHP et CORS avancé restent facultatifs. Pas d’activation PWA ni de déploiement exigés. Les statuts de validation d’été ne se transmettent pas à novembre.

## Décisions restant à consigner

- Horaire Casablanca : À COMPLÉTER.
- Durée retenue : 110 minutes proposées ; variante 90 minutes disponible en fiche 01.
- V1 ou démonstrateur effectivement utilisé : À COMPLÉTER.
- Revue pédagogique du pack de novembre : À COMPLÉTER.
- Décision ultérieure d’intégration PWA ou de diffusion : À COMPLÉTER.

Pilote : __________ · Date : __________ · Observation et décision : __________.
''')
doc('12', 'Fiche de départ — Projet, V1 et données autorisées', '''
## Projet et usage

Nom du projet : __________.
Mon activité aide [PUBLIC] à [RÉSULTAT] : __________.
Trois informations répétitives que je souhaite afficher : __________.
Une action principale du lecteur : __________.

## Préparation indispensable

- [ ] Je peux ouvrir la V1 ou la copie fictive fournie.
- [ ] Je conserve une V1 intacte et dispose d’une copie V2 distincte.
- [ ] Je retrouve la page, les styles et le JavaScript.
- [ ] Un navigateur avec console et un éditeur sont disponibles.
- [ ] Un serveur local est disponible avant la séance.
- [ ] Mes trois contenus sont fictifs ou autorisés et sans secret.

Si l’ouverture, la copie V2 ou le serveur manque, résoudre ce point avec le formateur ou utiliser le démonstrateur. Le choix ne dépend pas d’un simple nombre de cases manquantes.

## Données à préparer

| Objet | title | category | description | Origine autorisée |
|---|---|---|---|---|
| 1 | À COMPLÉTER | À COMPLÉTER | À COMPLÉTER | À COMPLÉTER |
| 2 | À COMPLÉTER | À COMPLÉTER | À COMPLÉTER | À COMPLÉTER |
| 3 | À COMPLÉTER | À COMPLÉTER | À COMPLÉTER | À COMPLÉTER |

Pas de mot de passe, clé API, donnée client/candidat, téléphone ou courriel privé. Les icônes, les flashcards et un inventaire de 6 à 12 contenus ne sont pas exigés pour démarrer S19.

## Préparation future PWA

Quel contenu serait utile sans réseau ? __________.
Quel composant faut-il encore comprendre ? __________.
Ces réponses alimentent S20 ; elles ne déclenchent pas l’installation ou la publication.

## Choix de départ

- [ ] Travailler sur ma copie V2.
- [ ] Apprendre d’abord sur le cas fictif.
- [ ] Résoudre le prérequis indiqué : __________.

Candidat : __________ · Formateur : __________ · Date : __________.
''')

readme = '# SÉANCE 19 — APPROFONDIR : JSON LOCAL ET PRÉPARATION PWA\n\n' + HEADER
readme += '''Synchronisation du cadrage du 27 juillet 2026 pour le **27 novembre 2026**. Durée proposée : **110 minutes** ; horaire Casablanca à communiquer. Le pack documentaire est reconstruit ; la revue pédagogique reste à effectuer.

Le candidat part de sa V1 ou d’une copie fictive, structure trois objets dans `data/projets.json`, les charge avec `fetch()` et teste **chargement, succès, vide et erreur**. La PWA est expliquée et préparée pour S20. Une PWA complète n’est pas exigée de S19.

## Parcours et documents

'''
labels = ['Support formateur et conducteur', 'Fiche candidat', 'Prompts 19-A à 19-F', 'Grille de contrôle', 'Modèle de preuve et relais', 'Cahier des charges JSON', 'Complément API/PHP facultatif', 'Guide et ressources historiques', 'Préparation PWA', 'Inventaire des contenus', 'Traçabilité des décisions', 'Fiche de départ']
for n, label in enumerate(labels, 1):
    key = f'{n:02d}'
    readme += f'- [{key} — {label}]({files[key]})\n'
readme += '''
Ordre conseillé : 12 → 01 → 02/03 → 04/05 → 09/10 → relais S20. Les fiches 06 et 08 servent de références ; 07 reste facultative. La fiche 11 distingue histoire et cadre courant.

## Livrables et limites

Livrable : `04-WEB/mini-site-v2/` avec HTML, styles locaux, `data/projets.json`, `js/app.js` et README. Preuve : `06-PORTFOLIO/preuve-S19.md`, relais : `06-PORTFOLIO/relais-S20.md`, liens dans l’index du portfolio. V1 reste conservée. Les résultats et décisions des modèles sont vierges.

Le pack livré contient les documents Markdown et leurs traces de synchronisation. Il ne contient pas une nouvelle application, une projection reconstruite, un guide interactif adapté ni des PDF. Les interfaces et supports déjà présents ailleurs dans le projet correspondent encore à une production antérieure et restent à adapter.

Les noms historiques des fichiers et du dossier sont conservés pour les liens ; les en-têtes portent l’édition automne V2 documentaire. Les documents d’été dans `docs/sources/` restent des archives et ne sont pas remplacés par cette édition.

Voir [les sources et arbitrages](SOURCES-ET-SYNCHRONISATION.md), [le rapport de reconstruction](RAPPORT-RECONSTRUCTION.md) et le [prompt de cadrage copié dans le pack](PROMPT-CADRAGE-S19-27-NOVEMBRE-2026.md). Ce dernier permet d’utiliser le pack après extraction dans un autre dossier.
'''
(PACK / 'README.md').write_text(readme, encoding='utf-8')
(PACK / 'PROMPT-CADRAGE-S19-27-NOVEMBRE-2026.md').write_bytes((ROOT / 'docs/PROMPT-CADRAGE-S19-27-NOVEMBRE-2026.md').read_bytes())

source_paths = [
    '01-SEANCES/seance-19-json-pwa-v2-a-valider.md',
    '02-PROMPTS/prompt-maitre-json-pwa-seance-19-v1-a-valider.md',
    '06-RAPPORTS/rapport-production-pack-documentaire-seance-19-2026-07-27.md',
    '06-RAPPORTS/rapport-execution-prompts-seance-19-2026-07-27.md',
    '05-EXEMPLES-CODE/mini-site-seance-19-V2/README.md',
    '05-EXEMPLES-CODE/mini-site-json-seance-19-v1-a-valider/data/projets.json',
]
source_paths += [f'01-SEANCES/{PACK.name}/{p.name}' for p in sorted(PACK.glob('*.md')) if p.name == 'README.md' or p.name[:2] in files]
manifest = []
for rel in source_paths:
    p = SOURCE / rel
    manifest.append({'path': rel, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()})
(PACK / 'manifest-sources.json').write_text(json.dumps({'source_root': str(SOURCE), 'files': manifest, 'comparison_before_rebuild': comparison}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
sources = f'''# Sources et synchronisation — 25 novembre 2026

**Source externe lue sans modification :** `{SOURCE}`.

Le manifeste joint conserve les chemins et empreintes SHA-256 des pièces examinées ou comparées. Les fichiers du pack source ont été comparés au pack local avant reconstruction. Le dossier source n’a pas été modifié.

La fiche S19 datée du 27 juillet fixe 110 minutes, trois objets, quatre états et une préparation PWA pour S20. Le prompt maître JSON/PWA indique également de ne pas intégrer la PWA complète. Le rapport d’exécution distingue contrôles statiques et essais visuels non réalisés. Le README V2 annonce une PWA inactive et un laboratoire enrichi.

Le pack local précédent mêlait ce socle et une extension d’août vers une PWA complète de 120 minutes. La reconstruction retire cette extension du résultat commun, conserve API/PHP comme complément et adapte les chemins à `04-WEB/` et `06-PORTFOLIO/`.

Le présent prompt du 25 novembre et la demande du pilote de reconstruire le pack pour le 27 novembre fixent l’arbitrage courant. La validation historique n’est pas transférée à novembre. Aucun résultat candidat n’est inventé.

## Pièces de référence

'''
sources += '\n'.join(f'- `{item["path"]}`' for item in manifest) + '\n'
(PACK / 'SOURCES-ET-SYNCHRONISATION.md').write_text(sources, encoding='utf-8')

# Contrôles documentaires : liens internes, métadonnées et JSON d'exemple.
broken = []
for p in PACK.glob('*.md'):
    for target in re.findall(r'\]\(([^)]+)\)', p.read_text(encoding='utf-8')):
        if '://' not in target and not (p.parent / target.split('#')[0]).exists():
            broken.append(f'{p.name}: {target}')
for key in files:
    text = (PACK / files[key]).read_text(encoding='utf-8')
    assert '27 novembre 2026' in text and 'À VALIDER' in text
example = re.search(r'```json\n(.*?)\n```', (PACK / files['06']).read_text(encoding='utf-8'), re.S)
data = json.loads(example.group(1))
assert len(data) == 3 and all(set(p) == {'title', 'category', 'description'} for p in data)
assert sum([10, 20, 15, 20, 15, 15, 15]) == 110
assert sum([10, 15, 10, 20, 20, 5, 10]) == 90

report = f'''# Rapport de reconstruction — 25 novembre 2026

Mission : reconstruire le pack documentaire S19 pour JSON local et préparation PWA, séance du 27 novembre 2026.

## Réalisation

- 12 fiches et README réécrits pour l’édition automne V2 documentaire, noms historiques conservés.
- Prompt de cadrage copié pour rendre le ZIP autonome sur le plan documentaire.
- Sources et arbitrages documentés ; manifeste des sources avec empreintes SHA-256.
- Pack et ZIP initiaux conservés dans `{INITIAL_BACKUP.relative_to(ROOT).as_posix()}`.
- État précédant cette exécution sauvegardé dans `{BACKUP.relative_to(ROOT).as_posix()}`.
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
'''
(PACK / 'RAPPORT-RECONSTRUCTION.md').write_text(report, encoding='utf-8')
broken = []
for p in PACK.glob('*.md'):
    for target in re.findall(r'\]\(([^)]+)\)', p.read_text(encoding='utf-8')):
        if '://' not in target and not (p.parent / target.split('#')[0]).exists():
            broken.append(f'{p.name}: {target}')
assert not broken, broken
archive = ROOT / f'{PACK.name}.zip'
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
    for p in sorted(PACK.rglob('*')):
        if p.is_file():
            z.write(p, p.relative_to(ROOT))
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    expected = {p.relative_to(ROOT).as_posix(): p.read_bytes() for p in PACK.rglob('*') if p.is_file()}
    assert set(z.namelist()) == set(expected)
    assert all(z.read(name) == contents for name, contents in expected.items())
print(json.dumps({'documents': len(list(PACK.glob('*.md'))), 'sources': len(manifest), 'checks': 'passed', 'backup': str(BACKUP), 'archive': str(archive)}, ensure_ascii=False))
