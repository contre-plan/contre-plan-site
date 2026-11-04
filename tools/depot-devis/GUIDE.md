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
- Les devis suivent la règle de la politique de confidentialité : supprimés au plus tard 12 mois après la livraison (et les dépôts sans paiement, au plus tard 30 jours après).
- Si tu modifies `Code.gs` plus tard : **Déployer**, **Gérer les déploiements**, crayon, **Nouvelle version**. L'URL reste la même.
