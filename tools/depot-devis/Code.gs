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
 * Aucun e-mail n'est envoyé à l'adresse saisie par le visiteur (pour qu'on ne puisse pas
 * se servir du formulaire pour écrire à un tiers).
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

function doPost(e) {
  try {
    var d = JSON.parse(e.postData.contents);

    // Champ piège invisible : un humain le laisse vide.
    if (d.site) return reponse({ ok: true, ref: 'CP-0' });

    if (!limiteOk()) return reponse({ ok: false, erreur: 'Trop de dépôts en ce moment. Réessayez dans une heure ou envoyez votre devis par e-mail.' });

    var email = String(d.email || '').trim().slice(0, 120);
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) return reponse({ ok: false, erreur: 'Adresse e-mail invalide.' });
    var formule = FORMULES[String(d.formule)] ? String(d.formule) : '1';
    if (d.accord !== true) return reponse({ ok: false, erreur: 'Merci de cocher la demande de démarrage immédiat.' });

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
      "Accord de démarrage immédiat et perte du droit de rétractation une fois le rapport livré (article 6 des CGV) : oui, coché le " +
        Utilities.formatDate(new Date(), 'Europe/Paris', 'dd/MM/yyyy HH:mm'),
      'Fichiers : ' + blobs.length
    ].join('\n');
    dossier.createFile('demande.txt', texte, MimeType.PLAIN_TEXT);

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

/** À lancer une fois à la main depuis l'éditeur : crée le dossier et demande les autorisations. */
function installer() {
  var f = dossierRacine();
  MailApp.getRemainingDailyQuota();
  Logger.log('Dossier prêt : ' + f.getUrl());
}
