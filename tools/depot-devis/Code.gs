/**
 * Contre-Plan : dépôt des devis depuis la page de commande (contre-plan.com/commander.html).
 *
 * Le site envoie le ou les devis ici AVANT le paiement Stripe. Ce programme :
 *  1. vérifie la demande (taille, type de fichier, champs obligatoires, accord de rétractation) ;
 *  2. range les fichiers dans Google Drive, dossier « Contre-Plan – Devis reçus / <référence> » ;
 *  3. envoie un e-mail de notification à contact@contre-plan.com ;
 *  4. renvoie la référence (CP-AAAAMMJJ-XXXX) que le site transmet à Stripe (client_reference_id),
 *     pour relier le paiement au dépôt.
 *
 * Toutes les 15 minutes, verifierPaiements() lit les paiements Stripe terminés et envoie au client
 * la confirmation de commande (article L221-13 du Code de la consommation) : récapitulatif, demande
 * de démarrage immédiat, formulaire de rétractation et CGV en PDF. Elle prévient aussi Contre-Plan.
 * Le formulaire de dépôt, lui, n'écrit jamais à l'adresse saisie (seuls les clients qui ont payé
 * reçoivent un e-mail, à l'adresse donnée à Stripe).
 *
 * Déploiement : voir GUIDE.md dans ce dossier.
 */

var DOSSIER = 'Contre-Plan – Devis reçus';
var NOTIF = 'contact@contre-plan.com';
var MAX_OCTETS = 10 * 1024 * 1024;   // 10 Mo au total
var MAX_FICHIERS = 3;
var MAX_PAR_HEURE = 30;               // protection contre les envois en masse
var TYPES = ['application/pdf', 'image/jpeg', 'image/png', 'image/heic', 'image/heif', 'image/webp'];
var FORMULES = { '1': '1 devis', '2': '2 devis comparés', '3': '3 devis comparés' };
var CGV_PDF = 'https://contre-plan.com/cgv-contre-plan.pdf';
var ADRESSE = '47 rue Vivienne, 75002 Paris';
var PHRASE_ACCORD = "Je demande que l'analyse commence tout de suite, sans attendre la fin du délai de rétractation de 14 jours. Je sais qu'une fois le rapport livré, je ne pourrai plus me rétracter.";

function doPost(e) {
  try {
    var d = JSON.parse(e.postData.contents);

    // Champ piège invisible : un humain le laisse vide.
    if (d.site) return reponse({ ok: true, ref: 'CP-0' });

    if (!limiteOk()) return reponse({ ok: false, erreur: 'Trop de dépôts en ce moment. Réessayez dans une heure ou envoyez votre devis par e-mail.' });

    var email = String(d.email || '').trim().slice(0, 120);
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) return reponse({ ok: false, erreur: 'Adresse e-mail invalide.' });
    var formule = FORMULES[String(d.formule)] ? String(d.formule) : '1';
    var accord = d.accord === true;

    var fichiers = Array.isArray(d.fichiers) ? d.fichiers : [];
    if (!fichiers.length) return reponse({ ok: false, erreur: 'Ajoutez au moins un devis.' });
    if (fichiers.length > MAX_FICHIERS) return reponse({ ok: false, erreur: 'Trois fichiers au maximum.' });

    var blobs = [], total = 0;
    for (var i = 0; i < fichiers.length; i++) {
      var f = fichiers[i] || {};
      var type = String(f.type || '').toLowerCase();
      if (TYPES.indexOf(type) === -1) return reponse({ ok: false, erreur: 'Format non accepté : PDF, JPG, PNG ou HEIC uniquement.' });
      var octets = Utilities.base64Decode(String(f.data || ''));
      total += octets.length;
      if (total > MAX_OCTETS) return reponse({ ok: false, erreur: 'Fichiers trop lourds (10 Mo au total).' });
      var nom = String(f.nom || ('devis-' + (i + 1))).replace(/[^\w.\- ]+/g, '_').slice(0, 80);
      blobs.push(Utilities.newBlob(octets, type, nom));
    }

    var ref = 'CP-' + Utilities.formatDate(new Date(), 'Europe/Paris', 'yyyyMMdd') + '-' +
      Utilities.getUuid().replace(/-/g, '').slice(0, 4).toUpperCase();

    var racine = dossierRacine();
    var dossier = racine.createFolder(ref + ' – ' + FORMULES[formule]);
    var liens = blobs.map(function (b) { return dossier.createFile(b).getUrl(); });

    var texte = [
      'Référence : ' + ref,
      'Date : ' + Utilities.formatDate(new Date(), 'Europe/Paris', 'dd/MM/yyyy HH:mm'),
      'Formule choisie : ' + FORMULES[formule] + ' (paiement Stripe à vérifier : client_reference_id = ' + ref + ')',
      'E-mail : ' + email,
      'Travaux : ' + propre(d.travaux, 200),
      "Répondre à l'artisan avant le : " + propre(d.echeance, 40),
      "Ce qui l'inquiète : " + propre(d.message, 2000),
      "Demande de démarrage immédiat et perte du droit de rétractation une fois le rapport livré (article 6 des CGV) : " +
        (accord ? 'oui, cochée le ' + Utilities.formatDate(new Date(), 'Europe/Paris', 'dd/MM/yyyy HH:mm')
                : "non : l'analyse commence à la fin du délai de rétractation de 14 jours"),
      'Fichiers : ' + blobs.length
    ].join('\n');
    dossier.createFile('demande.txt', texte, MimeType.PLAIN_TEXT);
    PropertiesService.getScriptProperties().setProperty('dep_' + ref,
      JSON.stringify({ accord: accord, formule: formule, quand: Date.now() }));

    MailApp.sendEmail({
      to: NOTIF,
      subject: 'Devis déposé ' + ref + ' – ' + FORMULES[formule],
      body: texte + '\n\nDossier : ' + dossier.getUrl() + '\n' + liens.join('\n') +
        "\n\nLe paiement n'est pas encore confirmé : cherchez " + ref + ' dans Stripe (Paiements, champ « Référence client »).'
    });

    return reponse({ ok: true, ref: ref });
  } catch (err) {
    console.error(err);
    return reponse({ ok: false, erreur: "Le dépôt n'a pas fonctionné. Vous pouvez envoyer votre devis par e-mail." });
  }
}

function doGet() {
  return reponse({ ok: true, service: 'depot-devis Contre-Plan' });
}

function reponse(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}

function propre(v, max) {
  return String(v || '').replace(/[\u0000-\u0008\u000b-\u001f]/g, '').trim().slice(0, max) || '—';
}

function dossierRacine() {
  var props = PropertiesService.getScriptProperties();
  var id = props.getProperty('DOSSIER_ID');
  if (id) { try { return DriveApp.getFolderById(id); } catch (e) {} }
  var it = DriveApp.getFoldersByName(DOSSIER);
  var f = it.hasNext() ? it.next() : DriveApp.createFolder(DOSSIER);
  props.setProperty('DOSSIER_ID', f.getId());
  return f;
}

function limiteOk() {
  var cache = CacheService.getScriptCache();
  var cle = 'n-' + Utilities.formatDate(new Date(), 'Europe/Paris', 'yyyyMMddHH');
  var n = Number(cache.get(cle) || 0) + 1;
  cache.put(cle, String(n), 3700);
  return n <= MAX_PAR_HEURE;
}

/** À lancer à la main depuis l'éditeur (une fois, puis après chaque mise à jour du code) :
 *  crée le dossier, la vérification des paiements toutes les 15 minutes, et demande les autorisations. */
function installer() {
  var f = dossierRacine();
  MailApp.getRemainingDailyQuota();
  UrlFetchApp.fetch('https://contre-plan.com/', { muteHttpExceptions: true });
  var props = PropertiesService.getScriptProperties();
  if (!props.getProperty('DEBUT')) props.setProperty('DEBUT', String(Math.floor(Date.now() / 1000)));
  var existe = ScriptApp.getProjectTriggers().some(function (t) { return t.getHandlerFunction() === 'verifierPaiements'; });
  if (!existe) ScriptApp.newTrigger('verifierPaiements').timeBased().everyMinutes(15).create();
  Logger.log('Dossier prêt : ' + f.getUrl());
  Logger.log(props.getProperty('STRIPE_KEY') ? 'Clé Stripe : présente' : 'Clé Stripe : ABSENTE (Paramètres du projet > Propriétés du script > STRIPE_KEY)');
  Logger.log('Vérification des paiements : toutes les 15 minutes');
}

/* ---------- Confirmation de commande après paiement ---------- */

function verifierPaiements() {
  var lock = LockService.getScriptLock();
  if (!lock.tryLock(5000)) return;
  try {
    var props = PropertiesService.getScriptProperties();
    var cle = props.getProperty('STRIPE_KEY');
    if (!cle) return;
    var debut = Number(props.getProperty('DEBUT') || 0);
    var depuis = Math.max(debut, Math.floor(Date.now() / 1000) - 3 * 86400);
    var r = UrlFetchApp.fetch('https://api.stripe.com/v1/checkout/sessions?limit=100&status=complete&created%5Bgte%5D=' + depuis,
      { headers: { Authorization: 'Bearer ' + cle }, muteHttpExceptions: true });
    if (r.getResponseCode() !== 200) { console.error('Stripe ' + r.getResponseCode() + ' ' + r.getContentText().slice(0, 300)); return; }
    var sessions = JSON.parse(r.getContentText()).data || [];
    var cgv = null;
    sessions.forEach(function (s) {
      if (s.payment_status !== 'paid') return;
      var k = 'conf_' + s.id;
      if (props.getProperty(k)) return;
      var email = s.customer_details && s.customer_details.email;
      if (!email) return;
      if (!cgv) cgv = pdfCgv();
      if (!cgv) return; // on réessaiera au prochain passage
      var ref = String(s.client_reference_id || '');
      var dep = null;
      if (/^CP-\d{8}-[A-Z0-9]{4}$/.test(ref)) { try { dep = JSON.parse(props.getProperty('dep_' + ref) || 'null'); } catch (e) {} }
      envoyerConfirmation(s, email, ref, dep, cgv);
      props.setProperty(k, String(Date.now()));
    });
  } finally { lock.releaseLock(); }
}

function pdfCgv() {
  var r = UrlFetchApp.fetch(CGV_PDF, { muteHttpExceptions: true });
  if (r.getResponseCode() !== 200) { console.error('CGV PDF ' + r.getResponseCode()); return null; }
  return r.getBlob().setName('Conditions-generales-de-vente-Contre-Plan.pdf');
}

function euros(c) { return (c / 100).toFixed(2).replace('.', ',').replace(',00', '') + ' €'; }

function texteConfirmation(s, ref, dep) {
  var fmt = function (d, f) { return Utilities.formatDate(d, 'Europe/Paris', f); };
  var quand = new Date(s.created * 1000);
  var fin = new Date(quand.getTime() + 14 * 86400000);
  var L = [];
  L.push('Bonjour,', '', 'Merci pour votre commande. Voici sa confirmation, à conserver.', '');
  L.push('VOTRE COMMANDE');
  L.push("- Prestation : analyse de devis de travaux par un ingénieur BTP, rapport PDF envoyé par e-mail" +
    (dep && FORMULES[dep.formule] ? ' (formule « ' + FORMULES[dep.formule] + ' »)' : ''));
  L.push('- Montant payé : ' + euros(s.amount_total) + ' TTC (TVA non applicable, article 293 B du CGI). Le détail et la facture figurent dans l\'e-mail de Stripe.');
  L.push('- Date : ' + fmt(quand, "dd/MM/yyyy 'à' HH:mm"));
  if (ref) L.push('- Référence : ' + ref);
  L.push('', 'VOTRE DEVIS');
  if (dep) {
    L.push('Votre devis est bien reçu.');
    if (dep.accord) {
      L.push("Vous avez demandé que l'analyse commence dès réception de votre devis, sans attendre la fin du délai de rétractation de 14 jours : le rapport arrive sous 48 h (24 h si vous avez choisi l'express).");
    } else {
      L.push("Vous n'avez pas demandé de démarrage immédiat : l'analyse commencera à la fin du délai de rétractation, le " + fmt(fin, 'dd/MM/yyyy') + ", et le rapport arrivera sous 48 h ensuite.");
      L.push('Si vous voulez votre rapport plus tôt, répondez à cet e-mail avec cette phrase :', '« ' + PHRASE_ACCORD + ' »');
    }
  } else {
    L.push('Envoyez votre devis (PDF ou photo nette) en répondant à cet e-mail. Vous pouvez masquer votre nom et votre adresse.');
    L.push("Le rapport arrive sous 48 h après sa réception (24 h si vous avez choisi l'express). Pour que l'analyse commence sans attendre la fin du délai de rétractation de 14 jours, ajoutez à votre message :", '« ' + PHRASE_ACCORD + ' »');
  }
  L.push('', 'VOTRE DROIT DE RÉTRACTATION');
  L.push("Vous pouvez vous rétracter pendant 14 jours à compter de la commande, sans avoir à vous justifier, en répondant à cet e-mail ou avec le formulaire ci-dessous. Si l'analyse a commencé à votre demande, vous payez seulement la part déjà réalisée. Une fois le rapport livré, le droit de rétractation ne peut plus être exercé (articles L221-18, L221-25 et L221-28 du Code de la consommation, article 6 des conditions de vente).");
  L.push('', 'Formulaire de rétractation (à compléter et renvoyer seulement si vous souhaitez vous rétracter) :');
  L.push("À l'attention de Contre-Plan, " + ADRESSE + ', contact@contre-plan.com :');
  L.push('Je vous notifie par la présente ma rétractation du contrat portant sur la prestation de services ci-dessous :');
  L.push('Commandée le : ' + fmt(quand, 'dd/MM/yyyy') + (ref ? ' (référence ' + ref + ')' : ''));
  L.push('Nom du client :', 'Adresse du client :', 'Signature du client (uniquement en cas d\'envoi sur papier) :', 'Date :');
  L.push('', 'CONDITIONS DE VENTE ET RECOURS');
  L.push('Les conditions générales de vente sont jointes à cet e-mail (PDF) et consultables sur https://contre-plan.com/cgv.html');
  L.push('En cas de litige non résolu après une réclamation écrite : médiateur de la consommation CM2C, 49 rue de Ponthieu, 75008 Paris, www.cm2c.net.');
  L.push('', 'Une question ? Répondez simplement à cet e-mail.', '', 'Arthur, ingénieur BTP – Contre-Plan');
  L.push('Contre-Plan, entreprise individuelle · SIRET 132 070 426 00029 · ' + ADRESSE + ' · contact@contre-plan.com');
  return L.join('\n');
}

function envoyerConfirmation(s, email, ref, dep, cgv) {
  var corps = texteConfirmation(s, ref, dep);
  MailApp.sendEmail({
    to: email, replyTo: NOTIF, name: 'Contre-Plan',
    subject: 'Confirmation de votre commande Contre-Plan' + (ref ? ' – ' + ref : ''),
    body: corps, attachments: [cgv]
  });
  MailApp.sendEmail({
    to: NOTIF,
    subject: 'Paiement reçu ' + euros(s.amount_total) + (ref ? ' – ' + ref : ' – devis à recevoir par e-mail'),
    body: 'Client : ' + email + '\nMontant : ' + euros(s.amount_total) + '\nRéférence : ' + (ref || 'aucune (paiement sans dépôt)') +
      '\nDémarrage immédiat : ' + (dep ? (dep.accord ? 'oui' : 'non, après 14 jours') : 'à vérifier dans le message du client') +
      '\n\nConfirmation envoyée au client :\n\n' + corps
  });
}

/** Test : envoie à contact@ un exemple de confirmation (sans rien marquer comme envoyé). */
function testerConfirmation() {
  var cgv = pdfCgv();
  var s = { id: 'test', created: Math.floor(Date.now() / 1000), amount_total: 1650 };
  MailApp.sendEmail({ to: NOTIF, name: 'Contre-Plan', subject: '[TEST] Confirmation de votre commande Contre-Plan – CP-20261105-TEST',
    body: texteConfirmation(s, 'CP-20261105-TEST', { accord: true, formule: '1' }), attachments: cgv ? [cgv] : [] });
}
