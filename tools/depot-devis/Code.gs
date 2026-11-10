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
 * Si un devis déposé n'est pas payé au bout de 24 h, le client reçoit UN seul e-mail de rappel
 * (lien de paiement, possibilité de demander la suppression). Jamais de deuxième relance.
 * Cette information figure sous le formulaire et dans la politique de confidentialité.
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
var JOURS_SANS_PAIEMENT = 30;      // dépôts sans paiement supprimés après ce délai (CGV, confidentialité)
var JOURS_CONSERVATION = 365;      // devis payés supprimés 12 mois après (confidentialité)
var HEURES_AVANT_RELANCE = 24;     // un seul rappel si le dépôt n'est pas payé après ce délai
var LIENS = {
  '1': 'https://buy.stripe.com/28EaEZ1N22bE7b95g4cMM00',
  '2': 'https://buy.stripe.com/9B6cN74ZeeYq7b9bEscMM03',
  '3': 'https://buy.stripe.com/14A00l1N22bE1QPdMAcMM04'
};
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
      JSON.stringify({ accord: accord, formule: formule, quand: Date.now(), dossier: dossier.getId(), email: email }));

    MailApp.sendEmail({
      to: NOTIF,
      subject: 'Devis déposé ' + ref + ' – ' + FORMULES[formule],
      body: texte + '\n\nDossier : ' + dossier.getUrl() + '\n' + liens.join('\n') +
        "\n\nPaiement pas encore confirmé. Tu recevras un e-mail « Paiement reçu » dès qu'il le sera, et le dossier sera renommé « PAYÉ ». Sans paiement au bout de " + HEURES_AVANT_RELANCE + " h, le client reçoit un seul e-mail de rappel. Sans paiement, le dossier est supprimé automatiquement après " + JOURS_SANS_PAIEMENT + ' jours.'
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
    var cgv = null, payesRecents = {};
    sessions.forEach(function (s) {
      if (s.payment_status !== 'paid') return;
      if (s.client_reference_id) payesRecents[s.client_reference_id] = true;
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
      try { marquerPaye(ref, dep); } catch (e) { console.error('marquerPaye ' + e); }
      try { planifierRappel(s, email, ref, dep); } catch (e) { console.error('planifierRappel ' + e); }
    });
    envoyerRappels();
    relancerDepotsNonPayes(payesRecents);
    nettoyerUneFoisParJour(cle);
  } finally { lock.releaseLock(); }
}

/* ---------- Suivi : dossier payé, rappel de livraison, nettoyage ---------- */

function dossierDe(ref, dep) {
  if (dep && dep.dossier) { try { return DriveApp.getFolderById(dep.dossier); } catch (e) {} }
  var it = dossierRacine().getFolders();
  while (it.hasNext()) { var f = it.next(); if (f.getName().indexOf(ref) !== -1) return f; }
  return null;
}

function marquerPaye(ref, dep) {
  if (!ref) return;
  var f = dossierDe(ref, dep);
  if (f && f.getName().indexOf('PAYÉ') !== 0) f.setName('PAYÉ – ' + f.getName());
}

function estExpress(s, cle) {
  try {
    var r = UrlFetchApp.fetch('https://api.stripe.com/v1/checkout/sessions/' + s.id + '/line_items?limit=20',
      { headers: { Authorization: 'Bearer ' + cle }, muteHttpExceptions: true });
    if (r.getResponseCode() !== 200) return false;
    return (JSON.parse(r.getContentText()).data || []).some(function (l) { return /express|24\s?h/i.test(l.description || ''); });
  } catch (e) { return false; }
}

function planifierRappel(s, email, ref, dep) {
  var props = PropertiesService.getScriptProperties();
  var express = estExpress(s, props.getProperty('STRIPE_KEY'));
  var paye = s.created * 1000, delai = (express ? 24 : 48) * 3600000;
  var depart = paye, note = '';
  if (dep && !dep.accord) { depart = paye + 14 * 86400000; note = "Pas de démarrage immédiat demandé : délai compté à partir de la fin des 14 jours (sauf si le client t'a envoyé la phrase d'accord)."; }
  if (!dep) note = "Devis attendu par e-mail : le délai court à partir de sa réception. Rappel calé sur l'heure du paiement.";
  var limite = depart + delai;
  props.setProperty('liv_' + s.id, JSON.stringify({
    rappel: limite - 8 * 3600000, limite: limite, email: email, ref: ref, express: express, montant: s.amount_total, note: note }));
}

function envoyerRappels() {
  var props = PropertiesService.getScriptProperties(), all = props.getProperties(), now = Date.now();
  Object.keys(all).forEach(function (k) {
    if (k.indexOf('liv_') !== 0) return;
    var r; try { r = JSON.parse(all[k]); } catch (e) { props.deleteProperty(k); return; }
    if (now < r.rappel) return;
    var quand = Utilities.formatDate(new Date(r.limite), 'Europe/Paris', "EEEE dd/MM 'à' HH'h'mm");
    MailApp.sendEmail({ to: NOTIF,
      subject: 'Rapport à livrer avant ' + quand + (r.ref ? ' – ' + r.ref : '') + (r.express ? ' (express)' : ''),
      body: 'Client : ' + r.email + '\nRéférence : ' + (r.ref || 'aucune (devis envoyé par e-mail)') + '\nMontant : ' + euros(r.montant) +
        '\nDélai : ' + (r.express ? '24 h (express)' : '48 h') + ', à livrer avant ' + quand + '.' + (r.note ? '\n\n' + r.note : '') +
        '\n\nSi le rapport est déjà parti, ignore ce message.' });
    props.deleteProperty(k);
  });
}

/* Un seul rappel au client si son dépôt n'est pas payé 24 h après. Fenêtre 24 h - 72 h :
   la liste Stripe lue à chaque passage couvre les 3 derniers jours, donc un paiement fait
   entre-temps est toujours vu. Les dépôts plus anciens que 72 h ne sont jamais relancés. */
function relancerDepotsNonPayes(payesRecents) {
  var props = PropertiesService.getScriptProperties(), all = props.getProperties(), now = Date.now();
  Object.keys(all).forEach(function (k) {
    if (k.indexOf('dep_') !== 0) return;
    var ref = k.slice(4), dep;
    try { dep = JSON.parse(all[k]); } catch (e) { return; }
    if (!dep || !dep.email || dep.relance || payesRecents[ref]) return;
    var age = now - Number(dep.quand || 0);
    if (age < HEURES_AVANT_RELANCE * 3600000 || age > 72 * 3600000) return;
    var lien = (LIENS[dep.formule] || LIENS['1']) + '?client_reference_id=' + encodeURIComponent(ref) +
      '&prefilled_email=' + encodeURIComponent(dep.email);
    MailApp.sendEmail({
      to: dep.email, replyTo: NOTIF, name: 'Contre-Plan',
      subject: 'Votre devis est bien arrivé, il manque le paiement – ' + ref,
      body: texteRelance(ref, dep, lien)
    });
    dep.relance = now;
    props.setProperty(k, JSON.stringify(dep));
  });
}

function texteRelance(ref, dep, lien) {
  return [
    'Bonjour,', '',
    'Vous avez déposé votre devis sur contre-plan.com le ' + Utilities.formatDate(new Date(Number(dep.quand)), 'Europe/Paris', "dd/MM 'à' HH'h'mm") +
      ' (référence ' + ref + '), mais le paiement n\'a pas été finalisé. Votre devis est en attente, rien n\'a été analysé ni débité.', '',
    'Si vous voulez votre rapport, voici le lien de paiement sécurisé (Stripe), déjà relié à votre devis :', lien, '',
    'Si vous avez changé d\'avis, il n\'y a rien à faire : votre devis sera supprimé automatiquement au plus tard ' + JOURS_SANS_PAIEMENT +
      ' jours après le dépôt. Pour qu\'il le soit tout de suite, répondez simplement « supprimer ».', '',
    'Une question avant de commander ? Répondez à cet e-mail.', '',
    'Si vous avez payé entre-temps, ignorez ce message. C\'est le seul rappel que vous recevrez.', '',
    'Arthur, ingénieur BTP – Contre-Plan',
    'Contre-Plan, entreprise individuelle · SIRET 132 070 426 00029 · ' + ADRESSE + ' · contact@contre-plan.com'
  ].join('\n');
}

/** Test : envoie à contact@ un exemple du rappel de dépôt non payé. */
function testerRelance() {
  var dep = { formule: '1', quand: Date.now() - 25 * 3600000, email: NOTIF };
  MailApp.sendEmail({ to: NOTIF, name: 'Contre-Plan', subject: '[TEST] Votre devis est bien arrivé, il manque le paiement – CP-20261109-TEST',
    body: texteRelance('CP-20261109-TEST', dep, LIENS['1'] + '?client_reference_id=CP-20261109-TEST') });
}

function refsPayees(cle) {
  var refs = {}, depuis = Math.floor(Date.now() / 1000) - (JOURS_CONSERVATION + 30) * 86400, apres = '', tour = 0;
  while (tour++ < 20) {
    var r = UrlFetchApp.fetch('https://api.stripe.com/v1/checkout/sessions?limit=100&status=complete&created%5Bgte%5D=' + depuis + (apres ? '&starting_after=' + apres : ''),
      { headers: { Authorization: 'Bearer ' + cle }, muteHttpExceptions: true });
    if (r.getResponseCode() !== 200) return null; // en cas de doute, on ne supprime rien
    var j = JSON.parse(r.getContentText());
    (j.data || []).forEach(function (s) { if (s.payment_status === 'paid' && s.client_reference_id) refs[s.client_reference_id] = true; });
    if (!j.has_more || !j.data.length) break;
    apres = j.data[j.data.length - 1].id;
  }
  return refs;
}

function nettoyerUneFoisParJour(cle) {
  var props = PropertiesService.getScriptProperties();
  var jour = Utilities.formatDate(new Date(), 'Europe/Paris', 'yyyy-MM-dd');
  if (props.getProperty('NETTOYAGE') === jour) return;
  var payes = refsPayees(cle);
  if (!payes) return;
  var now = Date.now(), it = dossierRacine().getFolders(), supprimes = [];
  while (it.hasNext()) {
    var f = it.next(), nom = f.getName(), m = nom.match(/CP-\d{8}-[A-Z0-9]{4}/);
    if (!m) continue;
    var age = (now - f.getDateCreated().getTime()) / 86400000, ref = m[0];
    var paye = payes[ref] || nom.indexOf('PAYÉ') === 0;
    if (paye && nom.indexOf('PAYÉ') !== 0 && age < JOURS_CONSERVATION) { f.setName('PAYÉ – ' + nom); continue; }
    if ((!paye && age > JOURS_SANS_PAIEMENT) || (paye && age > JOURS_CONSERVATION)) {
      f.setTrashed(true); props.deleteProperty('dep_' + ref); supprimes.push(nom);
    }
  }
  props.setProperty('NETTOYAGE', jour);
  if (supprimes.length) console.log('Dossiers supprimés : ' + supprimes.join(', '));
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

/* Version HTML du texte : évite que les lignes soient coupées en plein milieu sur téléphone. */
function enHtml(t) {
  var esc = String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  esc = esc.replace(/(https?:\/\/[^\s<]+)/g, '<a href="$1">$1</a>');
  return '<div style="font-family:Arial,sans-serif;font-size:15px;line-height:1.5;color:#1b2a41">' +
    esc.split('\n\n').map(function (p) { return '<p style="margin:0 0 14px">' + p.replace(/\n/g, '<br>') + '</p>'; }).join('') + '</div>';
}

/* E-mail au client, envoyé par Gmail (GmailApp) depuis contact@ : même chemin que les e-mails envoyés à la main. */
function mailClient(email, ref, corps, cgv) {
  GmailApp.sendEmail(email, 'Confirmation de votre commande Contre-Plan' + (ref ? ' – ' + ref : ''), corps,
    { name: 'Contre-Plan', replyTo: NOTIF, htmlBody: enHtml(corps), attachments: cgv ? [cgv] : [] });
}

function envoyerConfirmation(s, email, ref, dep, cgv) {
  var corps = texteConfirmation(s, ref, dep);
  mailClient(email, ref, corps, cgv);
  MailApp.sendEmail({
    to: NOTIF,
    subject: 'Paiement reçu ' + euros(s.amount_total) + (ref ? ' – ' + ref : ' – devis à recevoir par e-mail'),
    body: 'Client : ' + email + '\nMontant : ' + euros(s.amount_total) + '\nRéférence : ' + (ref || 'aucune (paiement sans dépôt)') +
      '\nDémarrage immédiat : ' + (dep ? (dep.accord ? 'oui' : 'non, après 14 jours') : 'à vérifier dans le message du client') +
      '\n\nConfirmation envoyée au client :\n\n' + corps
  });
}

/** Renvoie au client la confirmation d'une commande déjà payée. Mets la référence ci-dessous, puis Exécuter. */
var REF_A_RENVOYER = 'CP-20261110-CF23';
function renvoyerConfirmation() {
  var props = PropertiesService.getScriptProperties(), cle = props.getProperty('STRIPE_KEY');
  var r = UrlFetchApp.fetch('https://api.stripe.com/v1/checkout/sessions?limit=100&status=complete&created%5Bgte%5D=' +
    (Math.floor(Date.now() / 1000) - 30 * 86400), { headers: { Authorization: 'Bearer ' + cle }, muteHttpExceptions: true });
  var s = (JSON.parse(r.getContentText()).data || []).filter(function (x) { return x.client_reference_id === REF_A_RENVOYER && x.payment_status === 'paid'; })[0];
  if (!s) { console.log('Aucun paiement trouvé pour ' + REF_A_RENVOYER); return; }
  var dep = null; try { dep = JSON.parse(props.getProperty('dep_' + REF_A_RENVOYER) || 'null'); } catch (e) {}
  mailClient(s.customer_details.email, REF_A_RENVOYER, texteConfirmation(s, REF_A_RENVOYER, dep), pdfCgv());
  console.log('Confirmation renvoyée à ' + s.customer_details.email);
}

/** Test : envoie à contact@ un exemple de confirmation (sans rien marquer comme envoyé). */
function testerConfirmation() {
  var cgv = pdfCgv();
  var s = { id: 'test', created: Math.floor(Date.now() / 1000), amount_total: 1650 };
  MailApp.sendEmail({ to: NOTIF, name: 'Contre-Plan', subject: '[TEST] Confirmation de votre commande Contre-Plan – CP-20261105-TEST',
    body: texteConfirmation(s, 'CP-20261105-TEST', { accord: true, formule: '1' }), attachments: cgv ? [cgv] : [] });
}
