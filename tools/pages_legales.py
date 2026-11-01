# Pages légales générées par build.py : conditions générales de vente et politique de confidentialité.
# Modèle d'information générale, à faire relire par un professionnel du droit.
# SIRET et adresse renseignés le 28/10/2026. Médiateur CM2C : adhésion du 29/10/2026, valable jusqu'au 29/10/2029 (à renouveler).

EDITEUR = "Contre-Plan, entreprise individuelle (EI) dont l'identité complète de l'exploitant figure dans les <a href=\"mentions-legales.html\">mentions légales</a>"
# Le nom de l'exploitant n'apparaît que sur mentions-legales.html (choix d'anonymat commercial).
NOM_EXPLOITANT = "Arthur Demange"
ADRESSE = "10 rue du Point de Vue, 88000 Épinal"
SIRET = "132 070 426 00011"
TEL = "06 75 83 65 61"
MEDIATEUR = "CM2C (Centre de la Médiation de la Consommation de Conciliateurs de Justice), 49 rue de Ponthieu, 75008 Paris, tél. 01 89 47 00 14, litiges@cm2c.net. Saisine en ligne : <a href=\"https://www.cm2c.net/declarer-un-litige.php\" target=\"_blank\" rel=\"noopener\">www.cm2c.net/declarer-un-litige.php</a>"
import decodeur as _DEC
MAJ = "31 octobre 2026" if _DEC.DECODEUR_URL else "30 octobre 2026"
DEC_LI = ("<li><strong>Décodeur de ligne de devis</strong> : la ligne de devis que vous collez (et le type de travaux, si vous le choisissez) est transmise, via un relais technique hébergé par Cloudflare, à l'outil d'intelligence artificielle Claude d'Anthropic, uniquement pour produire l'explication affichée (intérêt légitime à fournir l'outil demandé). Contre-Plan n'enregistre ni le texte, ni la réponse, ni votre adresse IP ; " + ("Une vérification anti-robot (Cloudflare Turnstile) contrôle que la demande vient d'un navigateur humain, sans cookie publicitaire. " if _DEC.TURNSTILE_SITEKEY else "") + " Anthropic traite ce texte selon ses conditions applicables aux services professionnels de son API. Ne collez ni nom, ni adresse, ni coordonnées.</li>\n" if _DEC.DECODEUR_URL else "")
MEN_LI = ("<li><strong>Contrôle des mentions du devis</strong> : la photo ou le PDF du devis que vous envoyez est transmis, via le même relais Cloudflare, à l'outil d'intelligence artificielle Claude d'Anthropic, uniquement pour produire le contrôle affiché (intérêt légitime à fournir l'outil demandé). Le document peut contenir votre nom et votre adresse : vous pouvez les masquer avant l'envoi. Contre-Plan n'enregistre ni le fichier, ni le résultat, ni votre adresse IP ; Anthropic traite ce document selon ses conditions applicables aux services professionnels de son API.</li>\n" if _DEC.DECODEUR_URL else "")
ASSIST_LI = ("<li><strong>Assistant de questions</strong> : il répond d'abord dans votre navigateur avec des réponses préparées à l'avance. Si votre question n'y figure pas, son texte (et les derniers échanges de la conversation) est transmis, via le relais Cloudflare, à l'outil d'intelligence artificielle Claude d'Anthropic, qui répond à partir des seules informations du site. Contre-Plan n'enregistre ni vos messages ni les réponses ; seul le thème de la réponse est compté, de façon anonyme, par GoatCounter. N'y écrivez pas de données personnelles.</li>" if _DEC.DECODEUR_URL else "<li><strong>Assistant de questions</strong> : il fonctionne dans votre navigateur, avec des réponses préparées à l'avance. Ce que vous y écrivez n'est ni envoyé ni enregistré ; seul le thème de la réponse affichée est compté, de façon anonyme, par GoatCounter.</li>")
DEC_QUI = (", Cloudflare, Inc. (relais technique des outils gratuits du site et vérification anti-robot) et Anthropic (outil d'intelligence artificielle Claude, pour les outils gratuits et l'assistant)" if _DEC.DECODEUR_URL else "")

CGV_BODY = f"""<p><em>Conditions en vigueur au {MAJ}.</em></p>
<h2 id="vendeur">1. Qui vend</h2>
<p>{EDITEUR}. Adresse : {ADRESSE}. SIRET : {SIRET}. Téléphone : <a href="tel:+33675836561">{TEL}</a>. E-mail : <a href="mailto:contact@contre-plan.com">contact@contre-plan.com</a>. TVA non applicable, article 293 B du Code général des impôts.</p>

<h2 id="champ">2. Champ d'application</h2>
<p>Les présentes conditions générales de vente s'appliquent aux prestations de Contre-Plan commandées par un particulier ou par un professionnel (agent immobilier, syndic, gestionnaire de biens…). Les règles propres aux consommateurs, notamment le droit de rétractation (article 6) et la médiation de la consommation (article 9), bénéficient aux particuliers.</p>
<p>Les commandes peuvent être passées de deux façons :</p>
<ul>
<li><strong>Sur le site contre-plan.com</strong>, avec paiement par carte via le prestataire de paiement Stripe. Le contrat est conclu directement avec Contre-Plan, et les présentes conditions s'appliquent en totalité.</li>
<li><strong>Sur la plateforme ComeUp</strong> : ses conditions générales régissent alors le parcours de commande, l'encaissement du paiement, la facturation et le versement des remboursements. Les présentes conditions s'appliquent pour tout le reste, notamment la prestation (article 3), les délais (article 5), le droit de rétractation (article 6), la responsabilité (article 7), la confidentialité (article 8), les réclamations et la médiation (article 9).</li>
</ul>
<p>Passer commande vaut acceptation des présentes conditions.</p>

<h2 id="prestation">3. Ce que comprend la prestation</h2>
<p>Contre-Plan réalise une <strong>analyse documentaire</strong> d'un devis de travaux transmis par le client : lecture ligne par ligne, cohérence des quantités et des prix unitaires, postes manquants ou flous, taux de TVA, mentions et conditions de paiement, questions à poser à l'entreprise. Le résultat est un rapport écrit (PDF) qui constitue un <strong>avis technique fondé uniquement sur les documents transmis</strong>.</p>
<p>La prestation ne comprend pas :</p>
<ul>
<li>de visite du chantier ni de vérification sur place des mesures, de l'état existant ou de la faisabilité ;</li>
<li>de contrôle de l'entreprise au-delà des informations publiques consultables (immatriculation, qualifications affichées) ;</li>
<li>de conseil juridique, fiscal ou financier personnalisé ;</li>
<li>de validation du devis, de garantie sur un prix, sur un montant d'économie ou sur le résultat d'une négociation ;</li>
<li>de maîtrise d'œuvre, de suivi de chantier ni de mise en relation avec des entreprises.</li>
</ul>
<p>Le client reste seul décisionnaire de la suite qu'il donne au devis. Les prix de comparaison cités sont des ordres de grandeur, qui varient selon la région, l'accès au chantier et l'état de l'existant.</p>

<h2 id="prix">4. Prix et paiement</h2>
<p>Les prix sont indiqués en euros, toutes taxes comprises (TVA non applicable), sur la <a href="commander.html">page de commande</a> du site et sur la page de paiement, ou sur la page de commande ComeUp. Le prix applicable est celui affiché au moment de la commande.</p>
<p><strong>Commande sur le site</strong> : le paiement est effectué en une fois, par carte bancaire, au moment de la commande, sur la page de paiement sécurisée de Stripe. Contre-Plan n'a jamais accès aux données de la carte. La facture est envoyée par e-mail après le paiement.</p>
<p><strong>Commande sur ComeUp</strong> : le paiement est effectué en ligne à la commande ; ComeUp le conserve jusqu'à la livraison et à la validation de la prestation, selon ses conditions. La facture ou le justificatif de paiement est mis à disposition selon les modalités de ComeUp.</p>

<h2 id="delais">5. Documents à fournir et délais</h2>
<p>Le client transmet le devis complet et lisible (PDF ou photo nette) : par e-mail à contact@contre-plan.com pour une commande passée sur le site, ou dans la messagerie de la commande pour une commande ComeUp. Il peut masquer son nom et son adresse. Le rapport est livré par le même canal. Le délai de livraison annoncé (48 heures, ou 24 heures avec l'option express) court à partir de la réception de tous les documents nécessaires. Si un document manque ou est illisible, Contre-Plan le signale et le délai part de la réception du document complet. Une question de suivi sur le rapport est incluse dans les jours qui suivent la livraison.</p>

<h2 id="retractation">6. Droit de rétractation</h2>
<p>Pour une commande passée à distance, le client dispose d'un délai de <strong>14 jours</strong> à compter de la conclusion du contrat pour se rétracter, sans avoir à se justifier (article L221-18 du Code de la consommation).</p>
<p>Pour recevoir son rapport avant la fin de ce délai, le client demande expressément que la prestation commence tout de suite. S'il se rétracte alors que l'analyse est commencée mais pas terminée, il paie la part déjà réalisée, proportionnellement au prix total (article L221-25). <strong>Le droit de rétractation ne peut plus être exercé une fois le rapport livré</strong>, lorsque le client a donné son accord préalable et exprès à l'exécution immédiate et reconnu qu'il perd ce droit une fois la prestation pleinement exécutée (article L221-28, 1°). Cet accord est recueilli par écrit avant le début de l'analyse : dans le message qui accompagne l'envoi du devis (e-mail pour une commande sur le site, messagerie de la commande sur ComeUp).</p>
<p>Pour se rétracter, il suffit d'envoyer une déclaration claire, par exemple avec le formulaire ci-dessous, à <a href="mailto:contact@contre-plan.com?subject=R%C3%A9tractation">contact@contre-plan.com</a> (objet « Rétractation ») ou dans la messagerie de la commande ComeUp. Un accusé de réception est envoyé, et le remboursement intervient au plus tard 14 jours après la réception de la demande, sur le moyen de paiement utilisé : par Contre-Plan via Stripe pour une commande passée sur le site, par l'intermédiaire de ComeUp pour une commande ComeUp.</p>
<div class="note"><p><strong>Formulaire de rétractation</strong> (à compléter et renvoyer seulement si vous souhaitez vous rétracter) : « À l'attention de Contre-Plan, contact@contre-plan.com. Je vous notifie par la présente ma rétractation du contrat portant sur la prestation suivante : … Commandée le : … Nom du client : … Date : … »</p></div>

<h2 id="responsabilite">7. Responsabilité</h2>
<p>Contre-Plan s'engage à réaliser l'analyse avec soin, selon les règles de l'art de la lecture de devis, dans le périmètre décrit à l'article 3 (obligation de moyens). Sa responsabilité peut être engagée en cas de faute dans l'exécution de cette analyse. Elle ne peut pas l'être pour des éléments que le client n'a pas transmis, pour des informations inexactes figurant dans les documents fournis, ni pour l'exécution des travaux par l'entreprise choisie. Rien dans les présentes conditions ne prive le client des droits que la loi lui reconnaît.</p>

<h2 id="donnees">8. Confidentialité des devis</h2>
<p>Les devis transmis servent à réaliser l'analyse. Ils ne sont jamais publiés ni transmis à des tiers sans l'accord écrit du client. Le détail figure dans la <a href="confidentialite.html">politique de confidentialité</a>.</p>

<h2 id="reclamations">9. Réclamations et médiation</h2>
<p>Pour toute réclamation, écrivez d'abord à <a href="mailto:contact@contre-plan.com">contact@contre-plan.com</a> : une réponse est apportée sous 7 jours. En cas de désaccord persistant, le client peut recourir gratuitement au médiateur de la consommation (articles L612-1 et suivants du Code de la consommation), dans le délai d'un an à compter de sa réclamation écrite. Le médiateur ne peut être saisi que si le client justifie avoir d'abord tenté de résoudre le litige directement par une réclamation écrite. Chaque partie reste libre d'accepter ou de refuser la solution proposée. Médiateur de la consommation : {MEDIATEUR}.</p>

<h2 id="droit">10. Droit applicable</h2>
<p>Les présentes conditions sont soumises au droit français. En cas de litige, le client peut saisir la juridiction du lieu où il demeurait au moment de la commande ou de la survenance du fait dommageable.</p>
"""

CONF_BODY = f"""<p><em>Politique en vigueur au {MAJ}.</em></p>
<h2 id="responsable">Responsable du traitement</h2>
<p>{EDITEUR}. Adresse : {ADRESSE}. Contact : <a href="mailto:contact@contre-plan.com">contact@contre-plan.com</a>.</p>

<h2 id="quoi">Quelles données, pourquoi, combien de temps</h2>
<ul>
<li><strong>Formulaire de contact</strong> : nom ou pseudo, e-mail, sujet et message, pour vous répondre (intérêt légitime à traiter votre demande). Enregistrés via Google Forms et conservés au plus 12 mois.</li>
<li><strong>Prise de rendez-vous</strong> (service arrêté le 1er novembre 2026) : pour les appels réservés auparavant, nom, e-mail et réponses au questionnaire, enregistrés via Google Agenda et supprimés au plus tard 12 mois après le rendez-vous.</li>
<li><strong>Conseil devis du mois</strong> : adresse e-mail, sur la base de votre consentement, pour vous envoyer au plus un e-mail par mois. Supprimée dès que vous vous désinscrivez (répondez « stop » à n'importe quel e-mail).</li>
<li><strong>Devis transmis pour une analyse</strong> : le devis et les informations qu'il contient, pour réaliser l'analyse (exécution du contrat). Vous pouvez masquer votre nom et votre adresse avant l'envoi. Les devis et rapports sont conservés au plus 12 mois après la livraison, pour répondre à vos questions de suivi, puis supprimés. Les éléments comptables (numéro de commande, date, montant) sont conservés 10 ans, comme la loi l'impose.</li>
<li><strong>Paiement sur le site</strong> : le paiement est traité par Stripe (Stripe Payments Europe, Ltd., Irlande), qui reçoit les données de carte ; Contre-Plan ne les voit jamais. Contre-Plan reçoit le nom, l'adresse e-mail, l'adresse postale de facturation, la formule et le montant payés, pour exécuter la commande et établir la facture (exécution du contrat et obligation légale). Ces éléments comptables sont conservés 10 ans.</li>
<li><strong>Avis des clients</strong> : prénom ou initiales, adresse e-mail, note et texte de l'avis, pour vérifier que l'avis vient bien d'une commande et améliorer le service (intérêt légitime). Un avis n'est publié sur le site qu'avec votre accord, avec votre prénom ou vos initiales seulement ; l'e-mail n'est jamais publié. Aucune contrepartie n'est proposée en échange d'un avis. Conservés au plus 3 ans, ou jusqu'à votre demande de retrait.</li>
<li><strong>Statistiques de prix</strong> : les prix des postes des devis analysés peuvent être conservés sans aucune donnée personnelle (ni nom, ni adresse, ni entreprise, ni ville), sous forme d'ordres de grandeur par type de travaux, pour améliorer les analyses suivantes.</li>
<li><strong>Publication anonymisée</strong> : un devis n'est jamais montré publiquement, même rendu anonyme, sans votre accord écrit préalable.</li>
<li><strong>Prospection des professionnels</strong> : Contre-Plan peut écrire à des professionnels de l'immobilier (agences, courtiers, notaires, syndics) à leur adresse e-mail professionnelle publique, pour leur présenter le service, sur la base de son intérêt légitime et parce que le message concerne leur activité. Seuls le nom de la structure, sa ville et l'adresse utilisée sont conservés, au plus 3 ans après le dernier contact. Chaque message permet de refuser les suivants en répondant « stop » : l'adresse n'est alors plus jamais contactée.</li>
{DEC_LI}{MEN_LI}{ASSIST_LI}
<li><strong>Mesure d'audience</strong> : GoatCounter compte les pages vues sans cookie ni donnée permettant de vous identifier. Ce site ne dépose aucun cookie.</li>
</ul>

<h2 id="qui">Qui y a accès</h2>
<p>Seul Contre-Plan traite vos données. Elles sont hébergées par des prestataires techniques : Google (Google Ireland Limited : formulaires, agenda, messagerie et stockage des fichiers), GitHub, Inc. (hébergement du site, journaux techniques de connexion), GoatCounter (statistiques anonymes), Stripe (paiement des commandes passées sur le site, selon sa propre politique de confidentialité){DEC_QUI} et, pour les commandes passées sur ComeUp, la plateforme ComeUp selon ses propres conditions. Contre-Plan s'aide d'outils d'intelligence artificielle pour préparer certaines analyses ; ces outils ne servent qu'à exécuter la prestation et chaque rapport est relu avant envoi. Certains prestataires peuvent traiter des données hors de l'Union européenne, avec les garanties prévues par le RGPD. Vos données ne sont jamais vendues ni utilisées à des fins publicitaires.</p>

<h2 id="droits">Vos droits</h2>
<p>Vous pouvez demander l'accès à vos données, leur rectification, leur effacement, la limitation du traitement, leur portabilité, ou vous opposer à un traitement, et retirer votre consentement à tout moment : écrivez à <a href="mailto:contact@contre-plan.com">contact@contre-plan.com</a>. Une réponse est apportée sous un mois. Si vous estimez que vos droits ne sont pas respectés, vous pouvez adresser une réclamation à la CNIL (<a href="https://www.cnil.fr/fr/plaintes" target="_blank" rel="noopener">cnil.fr</a>).</p>
"""
