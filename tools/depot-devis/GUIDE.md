# Mettre en service le dépôt des devis (10 minutes, une seule fois)

Tant que l'adresse du programme n'est pas renseignée dans `tools/build.py` (constante `DEPOT_URL`), la page de commande garde l'ancien fonctionnement (payer, puis envoyer le devis par e-mail). Rien ne casse en attendant.

## 1. Créer le programme dans ton compte Google Contre-Plan

1. Connecte-toi à Google avec **contact@contre-plan.com** (pas ton compte perso).
2. Ouvre https://script.google.com puis clique sur **Nouveau projet**.
3. Renomme le projet (en haut à gauche) : `Contre-Plan – dépôt des devis`.
4. Efface le contenu de `Code.gs` et colle tout le fichier `tools/depot-devis/Code.gs` du site (Claude te le donne aussi dans la conversation).
5. Clique sur l'icône de disquette pour enregistrer.

## 2. Autoriser le programme

1. Dans la liste en haut, choisis la fonction **installer**, puis clique sur **Exécuter**.
2. Google demande l'autorisation : choisis contact@contre-plan.com, puis **Autoriser** (le programme a besoin de Drive pour ranger les devis et de Gmail pour te prévenir).
3. Le journal affiche « Dossier prêt » : le dossier « Contre-Plan – Devis reçus » est créé dans ton Drive.

## 3. Publier

1. Clique sur **Déployer**, puis **Nouveau déploiement**.
2. Roue dentée à côté de « Sélectionner le type » : **Application Web**.
3. Description : `v1`. **Exécuter en tant que : Moi** (contact@contre-plan.com). **Qui a accès : Tout le monde**.
4. **Déployer**, puis copie l'**URL de l'application Web** (elle finit par `/exec`).
5. Envoie cette URL à Claude : il la met dans le site et vérifie que tout fonctionne.

Si « Tout le monde » n'apparaît pas, c'est un réglage de Google Workspace : console d'administration, Applications, Google Workspace, Drive et Docs… ou demande à Claude de te guider.

## Ensuite

- Chaque dépôt crée un sous-dossier `CP-AAAAMMJJ-XXXX – formule` avec les fichiers et un fichier `demande.txt`, et t'envoie un e-mail.
- La même référence apparaît dans Stripe (champ « Référence client » du paiement) : c'est ce qui relie le paiement au dépôt.
- Un dépôt sans paiement correspondant n'est pas une commande : ne lance pas l'analyse.
- Les devis suivent la règle de la politique de confidentialité : supprimés au plus tard 3 mois après la livraison (et les dépôts sans paiement, au plus tard 30 jours après).
- Si tu modifies `Code.gs` plus tard : **Déployer**, **Gérer les déploiements**, crayon, **Nouvelle version**. L'URL reste la même.

## Mise à jour du 05/11/2026 : case facultative et confirmation de commande automatique

1. **Clé Stripe en lecture seule** : Stripe > Développeurs > Clés API > **Créer une clé restreinte**. Nom : `Confirmation commandes`. Permission : **Checkout Sessions : Lecture** (tout le reste sur « Aucun »). Crée-la et copie la clé (`rk_live_…`).
2. **Apps Script** (connecté avec contact@contre-plan.com, en fenêtre privée) : remplace tout `Code.gs` par la nouvelle version, enregistre.
3. Roue dentée **Paramètres du projet** > **Propriétés du script** > Ajouter : nom `STRIPE_KEY`, valeur = la clé `rk_live_…`. Enregistre.
4. Choisis la fonction **installer** > **Exécuter** et accepte les nouvelles autorisations (accès à un service externe, déclencheurs). Le journal doit afficher « Clé Stripe : présente ».
5. **Déployer** > **Gérer les déploiements** > crayon > Version : **Nouvelle version** > Déployer. L'adresse /exec ne change pas.
6. Test : choisis **testerConfirmation** > Exécuter. Tu reçois sur contact@ un exemple d'e-mail de confirmation avec les CGV en PDF.

Ensuite, toutes les 15 minutes, chaque nouveau paiement Stripe déclenche l'e-mail de confirmation au client et un e-mail « Paiement reçu » pour toi. Les paiements antérieurs à l'installation ne sont pas concernés.
Si les CGV changent : `python3 tools/make_cgv_pdf.py` pour régénérer `cgv-contre-plan.pdf`.

## Mise à jour du 09/11/2026 : suivi automatique

Avec la vérification des paiements (toutes les 15 minutes), le programme :
- renomme « PAYÉ – … » le dossier Drive d'un devis payé ;
- t'envoie « Rapport à livrer avant … » 8 h avant l'échéance (48 h, ou 24 h si l'option express a été prise ; 14 jours + 48 h si le client n'a pas demandé le démarrage immédiat) ;
- une fois par jour, met à la corbeille les dossiers non payés de plus de 30 jours et les dossiers payés de plus de 12 mois (CGV et politique de confidentialité). S'il ne peut pas joindre Stripe, il ne supprime rien.
- 24 h après un dépôt non payé, envoie au client UN seul e-mail de rappel (lien de paiement déjà relié à son devis, possibilité de répondre « supprimer »). Jamais de deuxième relance, et rien au-delà de 72 h. Si un client répond « supprimer », mets son dossier à la corbeille dans Drive.

Mise en place : remplacer Code.gs, enregistrer, puis Déployer > Gérer les déploiements > crayon > Nouvelle version > Déployer. Pas besoin de relancer installer().
Pour voir le rappel : lancer testerRelance() depuis l'éditeur, un exemple arrive sur contact@. Les dépôts faits avant la mise à jour ne sont pas relancés (leur e-mail n'était pas enregistré à part).
