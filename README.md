# contre-plan-site

Site vitrine Contre-Plan (GitHub Pages) : index.html, guides (guides.html, guide-*.html), 404.html, mentions-legales.html.
Mesure d'audience : GoatCounter (code contreplan).

## Ajouter ou modifier un guide

Les guides, la page Guides, la page 404 et le sitemap sont générés par `tools/build.py`.

1. Ajouter un appel `article(...)` dans `tools/build.py` (même format que les guides existants), avec `date="AAAA-MM-JJ"` = date de publication.
2. Lancer `python3 tools/build.py` depuis n'importe où : il réécrit les fichiers à la racine du site.
3. Ne jamais modifier à la main les fichiers générés (guide-*.html, guides.html, 404.html, sitemap.xml) : ils seraient écrasés au prochain build.

`index.html` et `mentions-legales.html` ne sont pas générés : on les modifie directement.

## Si les prix changent

Mettre à jour partout en même temps : `tools/build.py` (constante `PRIX`, schéma Service des pages par type de travaux), `index.html` (cartes Tarifs, FAQ et ses données structurées, offres du JSON-LD, `data-prix` du calcul « Votre devis fait combien ? »), `site.js` (texte de la barre mobile « dès 16,50 € »), `tools/build.py` (encadré latéral SIDE et bloc CTA), l'annonce ComeUp et l'agent carrousel.

## Offre de lancement
Le « prix de lancement » (16,50 € au lieu de 33 €) figure dans index.html (badge des tarifs, FAQ et JSON-LD FAQ). Le retirer à ces endroits quand l'offre se termine, et passer le prix à 33 €.

## Typographie et image de partage
- `tools/typo.py` ajoute les espaces insécables (avant ? : ; !, entre nombre et unité). Il est lancé automatiquement à la fin de `tools/build.py` ; après une modification manuelle de index.html, relancer `python3 tools/build.py`.
- `og-image.jpg` (aperçu de partage 1200×630) est généré depuis `tools/og-image.html` par une capture Playwright.

## Conseil devis du mois (emails)
Le lien du formulaire d'inscription (Google Forms) est la constante `NEWS` de `tools/build.py` (encadré latéral et pied de page des pages générées). Il figure aussi en dur dans le pied de page de `index.html`. Les inscriptions arrivent dans le Google Sheets associé au formulaire. Le paragraphe correspondant est dans « Données personnelles » de `mentions-legales.html`.

## Assistant du site
Supprimé le 13/11/2026 (choix d'Arthur : aucun outil d'IA visible sur le site). Les questions passent par contact.html et le bouton « Question » de la barre mobile y renvoie. La route /question du relais Cloudflare n'est plus appelée.

## Identité visuelle (brand.css)

`brand.css` aligne le site sur les carrousels : fond « plan bleu » quadrillé, devis papier scotché, surligneur jaune, feutre rouge, étiquettes orange. Il est chargé après `site.css` sur toutes les pages (accueil, pages générées par `tools/build.py`, mentions légales). Polices : Archivo, Source Sans 3, Caveat (annotations manuscrites). (`anim.css` et `anim.js` supprimés le 04/11/2026.)

## FAQ et données structurées des pages générées
- Guides : la FAQ de chaque guide est dans le dictionnaire `FAQS` de `tools/build.py` (section « Questions fréquentes » visible + données structurées FAQPage). La date de mise à jour affichée et `dateModified` viennent de `UPDATED` : la changer quand un guide est réellement mis à jour.
- Pages « Analyse de devis <travaux> » : nom du service, FAQ et schéma Service dans le dictionnaire `JOBS`.
- Ne pas ajouter de FAQ à la main dans les fichiers HTML générés : elle disparaîtrait au prochain build.

## IndexNow
À chaque push sur `main` qui modifie des pages, `.github/workflows/indexnow.yml` attend le déploiement puis signale les URL modifiées à IndexNow (Bing, Yandex, Seznam…). La clé est le fichier `d3127bda26f9f2f864790c6bf08ae400.txt` à la racine : ne pas le supprimer. Pour renvoyer toutes les pages : onglet Actions, workflow « IndexNow », « Run workflow ».

## Guides et pages ajoutés en octobre 2026
Les 4 guides (décennale, négocier, dépassement de devis, annulation) et les 5 pages par type de travaux (cuisine, électricité, fenêtres, extension, ravalement) sont rédigés dans `tools/nouveaux_guides.py` (listes `GUIDES` et `JOB_PAGES`, FAQ comprises), et générés par `tools/build.py`. Ils apparaissent automatiquement dans la page Guides, le pied de page des pages générées et le sitemap. Sur `index.html` (grille « Par type de chantier » et pied de page) et dans `llms.txt`, les liens sont écrits en dur.

## Décodeur de ligne de devis (outil gratuit avec l'API Claude)
Page générée par `tools/decodeur.py` (appelé par `tools/build.py`), seulement quand `DECODEUR_URL` est rempli : tant qu'il est vide, ni la page, ni ses liens, ni le paragraphe de la politique de confidentialité ne sont publiés. Le relais Cloudflare qui détient la clé API est dans `cloudflare/decodeur/` (non publié sur le site) ; la mise en service est décrite dans `cloudflare/decodeur/README.md`. Compteurs GoatCounter : `decodeur/envoi`, `decodeur/resultat-…`, `decodeur/hors-sujet`, `decodeur/erreur`, `decodeur/copie-questions`, `decodeur/clic-commander`.

## Dépôt du devis avant paiement (novembre 2026)
La page de commande peut recevoir le devis avant le paiement : le formulaire envoie les fichiers à un programme Google Apps Script (`tools/depot-devis/Code.gs`) qui les range dans Google Drive (« Contre-Plan – Devis reçus ») et prévient contact@contre-plan.com. Le site redirige ensuite vers le lien Stripe avec `client_reference_id` = la référence du dépôt (CP-AAAAMMJJ-XXXX) et l'e-mail prérempli. Tant que `DEPOT_URL` est vide dans `tools/build.py`, la page garde l'envoi par e-mail. Mise en service : `tools/depot-devis/GUIDE.md`.

## Grille de prix (04/11/2026)
1 devis (jusqu'à 30 000 €) 16,50 € ; 2 devis comparés 33 € ; 3 devis comparés 49 € ; 1 devis de 30 000 à 60 000 € 39 € ; de 60 000 à 100 000 € 59 € ; devis pour des travaux différents + 11 € ; express + 5,50 €. Liens Stripe dans la constante `STRIPE` de `tools/build.py`. La fiche PDF des professionnels se régénère depuis `tools/fiche-pro.html` (impression PDF A4 avec Playwright).
