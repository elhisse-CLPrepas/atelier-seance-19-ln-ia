# Complément formateur — JSON local, API, CORS et PHP

**Séance :** vendredi 27 novembre 2026 · Semaine 10 · Module 05  
**Édition :** automne V2 documentaire du 25 novembre 2026 · **Statut :** À VALIDER  
**Pilotage :** Prof. Abderrahman EL HISSE · LAB-NUMÉRIQUE-IA

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
