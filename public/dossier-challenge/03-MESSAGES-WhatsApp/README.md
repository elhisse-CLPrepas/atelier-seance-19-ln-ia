# Studio Messages · LN-IA

Espace de production de messages pour les ateliers du Prof. Abderrahman EL HISSE. Ouvrir `index.html` dans le navigateur, sans installation ni service externe.

## Parcours

1. **Cadrer** : séance, titre, parcours, date, horaire et fuseau, objectif, préparation, liens et signature.
2. **Composer** : choisir annonce, rappel, ressources/replay ou suivi. Modifier le modèle si nécessaire, puis générer le message. Les champs vides deviennent des mentions à compléter. Une modification des paramètres ne réécrit pas silencieusement votre texte : cliquer de nouveau sur Générer.
3. **Relire** : aperçu mobile, champs restants, modalités à communiquer, format Markdown et inventaire des liens. L’accès aux liens doit être contrôlé en les ouvrant.
4. **Partager** : copier, ouvrir le groupe puis coller et envoyer volontairement dans WhatsApp. Consigner ensuite l’envoi réellement effectué dans le journal CSV.

Le bouton « Reprendre l’annonce S18 complète » recharge le texte rédigé pour le lundi 23 novembre 2026. Les paramètres ne sont pas modifiés par ce bouton.

## Sauvegarder et réutiliser

- Les paramètres, les modèles, le message et les 20 dernières versions sont mémorisés dans le navigateur si son stockage est disponible.
- **Conserver cette version** garde un instantané du texte, restaurable depuis la liste des versions.
- **Sauvegarder l’espace JSON** produit le fichier à conserver sur disque. **Reprendre un espace** recharge ses paramètres, modèles, texte et versions.
- Le fichier JSON ne contient pas le champ privé du lien de groupe. Les liens présents dans le message ou les paramètres font toutefois partie de la sauvegarde : relire avant de partager.
- **Nouvel atelier** conserve vos modèles personnalisés, votre parcours et votre signature ; les autres paramètres, le message et les versions sont vidés après confirmation. Exporter d’abord l’atelier précédent.
- **Exporter en .txt** conserve le message à diffuser. **Imprimer / PDF** prépare une sortie imprimable de l’aperçu ; le navigateur choisit la mise en page finale.

Le stockage des pages `file://` varie selon le navigateur et le chemin. Déplacer le dossier ne transporte pas son stockage : utiliser les exports JSON.

## Répliquer dans un autre atelier

Copier le dossier `03-MESSAGES-WhatsApp` et conserver `../assets/logo-LN-IA.png` au même emplacement relatif. Les fichiers nécessaires sont `index.html`, `studio.css`, `studio-core.js`, `studio.js` et `atelier-data.js`. Aucun CDN, compte ni module complémentaire n’est nécessaire.

Une archive réutilisable `STUDIO-MESSAGES-LNIA.zip` est fournie à la racine de S18. Elle contient l’application et son logo, les références et les messages d’exemple. Extraire entièrement, ouvrir `index.html`, puis choisir Nouvel atelier ou Reprendre un espace JSON.

## Modèles et automatisations

Variables : `{seance}`, `{titre}`, `{cycle}`, `{date}`, `{horaire}`, `{objectif}`, `{preparation}`, `{acces}`, `{supports}`, `{replay}`, `{signature}`.

La date est développée en français. Saisir explicitement le fuseau dans l’horaire. Les modèles sont modifiables dans la bibliothèque. Le modèle de référence Markdown reste disponible dans `MODELES-MESSAGES.md`.

Les automatismes couvrent le remplissage des modèles, le formatage de la date, les contrôles de rédaction, la sauvegarde locale, la conversion des titres/gras/liens Markdown et l’aperçu. Aucun envoi ni aucune planification automatique n’est déclenché. Les contrôles ne prouvent pas l’exactitude des informations.

## Configuration du groupe

Charger la configuration JSON `.env.whatsapp` existante depuis le bouton Configuration privée, ou saisir le lien d’invitation. Il est mémorisé séparément seulement sur demande. Le bouton Oublier retire le lien mémorisé. Garder ce fichier hors Git et des archives de diffusion. Le logo du studio n’est pas joint au texte WhatsApp : joindre manuellement une image dans WhatsApp si souhaité.

## Choix techniques et recherche — 21 novembre 2026

- WhatsApp documente `wa.me` pour ouvrir une conversation avec un numéro et éventuellement un texte prérempli : https://faq.whatsapp.com/5913398998672934 . Cette fonction ne justifie pas un envoi automatique dans le groupe choisi ; ce studio utilise copie et ouverture du groupe.
- MDN précise que le comportement de `localStorage` avec les URL `file:` n’est pas défini : https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage . Les exports JSON assurent la reprise entre navigateurs et ateliers.

Aucune bibliothèque supplémentaire n’a été ajoutée. Le texte et les imports sont rendus par des nœuds texte, sans exécuter leur contenu HTML. Les imports d’espace sont contrôlés et limités à 2 Mo. La validation du lien de groupe accepte le domaine `chat.whatsapp.com` en HTTPS.
