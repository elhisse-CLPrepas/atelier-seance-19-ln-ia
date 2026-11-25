# Prompts d’approfondissement JSON S19

Ces six mandats complètent les six prompts du parcours commun. Ils ne remplacent pas la remise de la page V1. Utiliser des données fictives ou autorisées, sans secret, sans nouvelle dépendance et sans publication automatique.

## 19-A · Auditer la V1

Voici ma V1 et les fichiers disponibles : [joindre]. Repérez les contenus répétitifs pouvant devenir des données. Proposez trois objets fictifs ou autorisés. Ne modifiez pas les fichiers. Sortie : inventaire et champs proposés. Contrôle : chaque champ correspond à une zone visible.

## 19-B · Structurer le JSON

À partir de ces objets : [coller], produisez un tableau JSON valide. Précisez clés, types et champs requis. N’ajoutez aucun fait. Contrôle : parser le JSON, vérifier tableau et identifiants uniques.

## 19-C · Charger les données

Voici mon HTML et mon JSON : [joindre]. Proposez un chargement avec fetch depuis un chemin local relatif. Contrôlez response.ok puis la structure du tableau. Affichez les textes avec textContent. N’ajoutez aucune dépendance. Contrôle : modifier un titre puis le retrouver à l’écran depuis localhost.

## 19-D · Traiter les états

Voici le chargement : [code]. Prévoyez chargement, succès, vide et erreur. Une 404 ou un JSON invalide doit donner un message utile. Gardez un bouton pour réessayer. Contrôle : protocole reproductible pour les quatre états, résultats observés laissés vides.

## 19-E · Auditer sans modifier

Auditez ces fichiers sans les changer : [joindre]. Cherchez erreurs de chemin, types incohérents, états oubliés, liens dangereux et données non autorisées. Classez chaque constat avec fichier et raison. Ne déclarez pas la PWA fonctionnelle sans essai.

## 19-F · Documenter et transmettre

À partir des seuls essais réellement notés : [coller], rédigez README et preuve du laboratoire. Séparez attendu, observé et à tester. Décrivez le lancement sur un serveur déjà disponible. Préparez l’inventaire PWA sans activation ni publication automatique.
