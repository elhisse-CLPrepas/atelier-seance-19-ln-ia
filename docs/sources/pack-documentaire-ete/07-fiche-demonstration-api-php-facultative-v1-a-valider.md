# FICHE FORMATEUR FACULTATIVE — API, CORS ET PHP

**Version :** V1  
**Statut :** À VALIDER  
**Usage :** démonstration technique courte après validation du socle JSON/PWA

## Objectif

Situer le JSON local par rapport à une API et montrer, avec l’exemple `api.php` de l’atelier, qu’un serveur peut produire une réponse JSON. Cette extension ne doit pas remplacer la production principale et n’est pas nécessaire au fonctionnement de la PWA statique.

## Prérequis

```text
[ ] JSON local chargé avec succès
[ ] quatre états compris
[ ] aucune clé ni donnée privée
[ ] serveur PHP déjà disponible ou hébergement compatible
[ ] démonstration limitée dans le temps
```

## Comparaison essentielle

| Élément | Où s’exécute-t-il ? | Rôle | Séance 19 |
|---|---|---|---|
| JSON local | dossier public du site | données statiques | pratique obligatoire |
| `fetch()` | navigateur | demande une ressource | pratique obligatoire |
| API | serveur local ou distant | produit ou fournit des données | notion et démonstration |
| CORS | navigateur + en-têtes serveur | contrôle certaines requêtes entre origines | notion |
| PHP | serveur | exécute une logique et peut répondre en JSON | démonstration facultative |
| secret | serveur sécurisé | authentifie un service | interdit dans le navigateur |

## Démonstration avec `api.php`

Le fichier de référence se trouve dans :

```text
D:\Atelier-seance-19\PACK-SEANCE-19-MODULE-05\demonstrateur-mini-site-v2\api.php
```

Le serveur statique Python ne peut pas interpréter PHP. Utiliser uniquement un environnement PHP déjà disponible :

```powershell
php -S localhost:8080
```

Puis tester l’adresse prévue par le démonstrateur. Faire observer :

1. la requête dans l’onglet Réseau ;
2. le statut HTTP ;
3. le type de contenu JSON ;
4. la réponse produite par le serveur ;
5. le message d’erreur si PHP n’est pas interprété.

## Messages à faire reformuler

- une API peut retourner du JSON, mais une API n’est pas simplement un fichier JSON ;
- PHP s’exécute côté serveur ;
- CORS ne protège pas un secret exposé dans JavaScript ;
- une clé privée reste sur un serveur sécurisé ;
- la PWA principale doit continuer à fonctionner sans PHP ;
- aucune disponibilité hors connexion ne peut être promise pour une API distante.

## Interdictions

- aucune installation pendant l’atelier sans autorisation ;
- aucune clé, aucun compte réel et aucun endpoint privé ;
- aucun contournement de CORS ;
- aucune donnée candidat transmise ;
- aucune publication ou modification serveur automatique.

## Preuve facultative

```text
Serveur utilisé :
URL testée :
Statut HTTP observé :
Type de contenu observé :
Différence comprise entre JSON local et réponse PHP :
Anomalie rencontrée :
```
