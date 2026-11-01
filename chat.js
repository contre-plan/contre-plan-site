/* Contre-Plan – assistant : orientation en 3 questions + FAQ préparée (dans le navigateur). Une question libre sans réponse préparée est envoyée au relais Cloudflare (route /question), qui répond avec Claude à partir de assistant-kb.txt. Rien n'est enregistré ; seuls des compteurs anonymes GoatCounter sont envoyés. */
(function () {
  var COMEUP = "/commander.html";
  var PREDIAG = ["/contact.html?sujet=prediagnostic", "Demander le pré-diagnostic gratuit"];
  var KB = [
    { c: 1, q: "Combien ça coûte ?", k: ["prix", "tarif", "coût", "cout", "combien", "€", "euro", "payer combien", "ça coute", "ca coute"],
      a: "L'analyse d'un devis coûte 16,50 €, payés par carte sur le site ou sur ComeUp au même prix. 2 devis comparés : 44 € ; 3 devis comparés : 55 € ; devis pour des travaux différents : + 11 € par devis ; express en 24 h : + 5,50 €. Pas de TVA." },
    { c: 1, q: "Quel est le délai ?", k: ["délai", "delai", "quand", "recevoir", "sous combien", "combien de temps", "rapide", "express", "24", "48", "jours", "vite"],
      a: "Vous recevez votre rapport PDF sous 48 h après l'envoi du devis, ou 24 h avec l'option express." },
    { c: 1, q: "Comment ça marche ?", k: ["comment ça marche", "comment ca marche", "marche", "fonctionne", "étapes", "etapes", "commander", "procédure", "envoyer mon devis", "envoie mon devis", "envoyer le devis", "j'envoie"],
      a: "1. Vous choisissez votre formule et payez par carte, sans créer de compte. 2. Vous envoyez votre devis par e-mail, en PDF ou en photo. 3. Vous recevez par e-mail un rapport avec un verdict, les prix poste par poste, les oublis et les questions à poser à l'artisan." },
    { c: 1, q: "Faut-il créer un compte ?", k: ["compte", "inscri", "comeup", "come up", "chèque", "cheque", "carte bancaire", "carte bleue", "paypal", "payer en ligne", "paiement", "payer", "dollar", "$"],
      a: "Non : sur le site, vous payez par carte en 1 minute, sans créer de compte, et la facture arrive par e-mail. Si vous préférez, vous pouvez aussi commander sur la plateforme ComeUp (compte gratuit), qui conserve le paiement jusqu'à la livraison du rapport. Pas encore décidé ? Le pré-diagnostic gratuit se demande sans paiement.", l: PREDIAG },
    { c: 1, q: "Que contient le rapport ?", k: ["rapport", "contient", "reçois", "recois", "livrable", "pdf", "exemple"],
      a: "Un verdict global (cohérent, négociable ou signaux d'alerte), le contrôle des prix poste par poste, les postes oubliés, les incohérences d'enchaînement des travaux, les questions à poser avant de signer, et un échange de suivi inclus.", l: ["/exemple-rapport-contre-plan.pdf", "Voir un exemple de rapport complet (PDF)"] },
    { c: 1, w: 2, q: "J'ai plusieurs devis", k: ["même prix", "meme prix", "quel que soit le montant", "pour 2 devis", "pour 3 devis", "plusieurs devis", "2 devis", "3 devis", "4 devis", "deux devis", "trois devis", "quatre devis", "plusieurs lots", "lots", "tous corps", "rénovation complète", "renovation complete", "gros devis"],
      a: "Chaque devis transmis est analysé. Jusqu'à 3 devis dans la même commande : option « Devis supplémentaire » (+ 11 €) pour le 2e, et option « Troisième devis » (+ 11 €) pour le 3e. Exemple : 3 devis = 16,50 + 11 + 11 = 38,50 €. Pour des devis concurrents sur les mêmes travaux, l'option « comparatif » ajoute un tableau poste par poste. Plusieurs lots ou un gros devis tous corps d'état ? Décrivez-les dans le pré-diagnostic gratuit : je vous dis avant toute commande comment ils seront traités.", l: PREDIAG },
    { w: 2, q: "Le rapport sert-il pour ma banque ?", k: ["pret", "banque", "prêt", "pret immo", "crédit", "credit", "financement", "dossier de prêt", "acquisition", "compromis", "achat"],
      a: "Le rapport n'est pas une expertise et n'a pas de valeur officielle pour une banque. Il vous sert à faire corriger les oublis et les imprécisions des devis avant de les joindre à votre dossier, pour ne pas sous-estimer le budget travaux. Avec plusieurs devis, voyez l'option « 2e devis » ou le pré-diagnostic gratuit.", l: PREDIAG },
    { w: 0.5, q: "Quels travaux analysez-vous ?", k: ["quels travaux", "type de travaux", "salle de bain", "cuisine", "isolation", "toiture", "pompe", "pac", "électricité", "electricite", "plomberie", "maçonnerie", "extension", "fenêtre", "menuiserie", "terrasse", "carrelage", "vmc", "ventilation", "chauffe-eau", "ballon", "photovolta", "panneaux solaires", "solaire", "mur porteur"],
      a: "Rénovation et construction : salle de bain, cuisine, isolation, toiture, pompe à chaleur, électricité, plomberie, maçonnerie, menuiseries, extension, terrasse, véranda, piscine, poêle…", l: ["/#travaux", "Ce que je vérifie selon vos travaux"] },
    { w: 3, q: "Et pour une cuisine de grande enseigne ?", k: ["ixina", "schmidt", "mobalpa", "cuisinella", "leroy", "castorama", "ikea", "cuisiniste", "enseigne", "marque"],
      a: "Oui, quelle que soit l'enseigne : l'analyse porte sur le contenu du devis (meubles, plan de travail, électroménager, pose, raccordements, TVA), pas sur la marque.", l: ["/analyse-devis-cuisine.html", "Ce que je vérifie sur un devis de cuisine"] },
    { c: 1, q: "Mes données sont-elles protégées ?", k: ["données", "donnees", "confidentiel", "nom", "adresse", "personnel", "sécurité", "partag", "anonyme"],
      a: "Vous pouvez masquer votre nom et votre adresse sur le devis : seuls les postes, quantités et prix sont utiles. Votre devis n'est jamais publié, revendu ni transmis à une entreprise.", l: ["/engagements.html", "Mes engagements de confidentialité"] },
    { q: "Vous déplacez-vous ?", k: ["déplace", "deplace", "visite", "sur place", "venir", "expertise"],
      a: "Non, le service est 100 % à distance, sur la base du devis. Ce n'est ni une expertise judiciaire ni une maîtrise d'œuvre." },
    { q: "Mon chantier est en cours", nocta: 1, k: ["litige", "en cours", "supplément", "supplement", "réclame", "reclame", "conflit", "dépasse", "depasse", "avocat", "malfaçon", "malfacon", "abandon", "facture plus", "mise en demeure", "porter plainte"],
      a: "Je n'interviens pas sur un chantier en cours ni dans un litige : l'analyse sert avant de signer. Si l'artisan vous réclame un supplément, le guide ci-dessous explique vos droits et les étapes à suivre (réclamation écrite, médiateur, conciliateur de justice), avec un modèle de message.", l: ["/guide-depassement-devis-travaux-supplementaires.html", "Le guide : l'artisan dépasse le devis"], l2: ["/modeles-messages-artisan.html", "Modèle : contester un supplément"] },
    { q: "Peut-on en parler par téléphone ?", k: ["appel", "téléphone", "telephone", "parler", "visio", "rendez-vous", "rdv", "joindre quelqu"],
      a: "Les échanges se font par écrit : c'est plus précis sur un devis, et vous gardez une trace. Écrivez-moi par le formulaire de contact (réponse sous 24 h), ou demandez le pré-diagnostic gratuit pour savoir, avant toute commande, ce que l'analyse couvrira.", l: ["/contact.html", "Formulaire de contact"], l2: PREDIAG },
    { q: "Quel acompte verser ?", k: ["acompte", "arrhes", "verser", "échéancier", "echeancier", "solde", "avance"],
      a: "L'usage est souvent autour de 30 % à la signature, parfois plus quand du matériel est commandé sur mesure, puis des paiements liés à l'avancement et le solde à la réception. Au-delà de 40 à 50 %, demandez pourquoi et proposez un échéancier.", l: ["/guide-acompte-paiement-devis-travaux.html", "Le guide acompte et paiement"] },
    { w: 2, q: "Quel taux de TVA ?", k: ["tva", "taux", "5,5", "10 %", "20 %", "taxe"],
      a: "5,5 % pour la rénovation énergétique, 10 % pour l'amélioration d'un logement de plus de 2 ans, 20 % dans les autres cas (neuf, agrandissement, certains équipements). Le taux doit correspondre à vos travaux.", l: ["/guide-tva-travaux-renovation.html", "Le guide TVA"] },
    { w: 2, q: "Démarchage, aides, RGE", k: ["démarch", "demarch", "rge", "maprimerenov", "ma prime", "prime", "aide", "cee", "subvention", "anah", "france rénov", "france renov"],
      a: "Le démarchage pour des travaux de rénovation énergétique est interdit par téléphone, et depuis la loi du 30 juin 2025 aussi par message, e-mail et réseaux sociaux, sauf contrat en cours ; un contrat conclu ainsi est nul. Vérifiez l'entreprise dans l'annuaire RGE officiel (france-renov.gouv.fr) et faites le point gratuitement avec un conseiller France Rénov' avant de signer. Attention : MaPrimeRénov' « par geste » ne finance plus l'isolation seule des murs (depuis janvier 2026) ni des combles (depuis septembre 2026). L'analyse vérifie la qualification RGE annoncée, les performances exigées et le détail des primes déduites.", l: ["/analyse-devis-isolation.html", "Ce que je vérifie sur un devis d'isolation"] },
    { q: "Structure, mur porteur", k: ["mur porteur", "structure", "porteur", "note de calcul", "bureau d'études", "bureau d'etudes", "ipn", "poutre", "fondation"],
      a: "Je vérifie que le devis prévoit et chiffre ce qu'il faut : étude ou note de calcul d'un bureau d'études, étaiement, poutre ou linteau dimensionné, reprise des fondations. Je ne fais pas le calcul de structure moi-même : c'est le rôle d'un bureau d'études, et le rapport vous dit s'il manque." },
    { w: 2, q: "D'où viennent vos prix ?", k: ["viennent vos prix", "vos prix de", "comparaison", "d'où viennent", "d'ou viennent", "source", "base de prix", "comment vous savez", "prix du marché", "prix du marche", "fourchette", "référence de prix"],
      a: "Les prix unitaires sont comparés aux fourchettes publiques 2025-2026 affichées sur chaque page Travaux (deux guides de prix recoupés par ligne), et à mon expérience de chantier, en tenant compte de la région quand je la connais. Ce sont des fourchettes indicatives, jamais un « bon prix » au centime.", l: ["/methode.html", "Voir ma méthode"] },
    { q: "Je suis artisan", nocta: 1, k: ["je suis artisan", "suis plombier", "suis électricien", "suis electricien", "suis maçon", "suis macon", "suis chauffagiste", "dénigr", "denigr", "contre les artisans", "mon client veut", "mon devis relu"],
      a: "Je ne juge pas l'entreprise, je fais préciser le devis. La plupart des devis ne sont pas malhonnêtes, juste incomplets : un devis clair et détaillé sort renforcé de l'analyse. Le rapport donne au client des questions à vous poser, pas un verdict sur votre travail.", l: ["/methode.html", "Voir ma méthode"] },
    { q: "Que veut dire ce mot ?", k: ["mot", "terme", "signifie", "veut dire", "définition", "definition", "lexique", "ragréage", "forfait", "ml"],
      a: "Les termes courants d'un devis (forfait, ml, P.U., ragréage, SPEC, RGE, réception…) sont expliqués simplement dans le lexique.", l: ["/lexique-devis-travaux.html", "Ouvrir le lexique"] },
    { q: "Comment comparer mes devis ?", k: ["comparer", "comparatif", "tableau", "lequel choisir"],
      a: "Comparez poste par poste, en HT, en mettant les prestations comparables sur la même ligne : un devis moins cher avec des postes absents peut finir plus cher. Un tableau gratuit est disponible, et l'option « Comparatif multi devis » vous le livre rempli et commenté.", l: ["/comparer-ses-devis.html", "Le tableau comparatif gratuit"] },
    { q: "Qui analyse mon devis ?", k: ["qui", "ingénieur", "ingenieur", "expérience", "experience", "compétent", "competent", "commission", "indépendant"],
      a: "Un ingénieur BTP avec 10 ans d'expérience sur les chantiers et environ 1 000 devis lus et négociés, avant de créer Contre-Plan en octobre 2026. Indépendant : aucune commission d'artisan, aucune entreprise à vous revendre.", l: ["/methode.html", "Voir ma méthode"] },
    { c: 1, q: "Est-ce fiable ?", k: ["arnaque", "fiable", "confiance", "sérieux", "serieux", "escroquerie", "légal", "legal", "siret", "garantie", "rassur"],
      a: "Contre-Plan est une entreprise immatriculée (SIRET 132 070 426 00011), rattachée au médiateur de la consommation CM2C. Le paiement par carte est sécurisé par Stripe (vos données de carte ne me sont jamais transmises), et vous pouvez masquer votre nom et votre adresse sur le devis. Pas sûr que l'analyse vous serve ? Le pré-diagnostic gratuit vous le dit avant toute commande.", l: ["/mentions-legales.html", "Voir les mentions légales"] },
    { w: 2, q: "Mon devis me paraît trop cher", k: ["est-ce cher", "est ce cher", "c'est cher", "trop élevé", "trop cher", "devis cher", "est cher", "paraît cher", "parait cher", "surfactur", "abus", "gonflé", "gonfle", "normal ce prix", "prix normal", "est-ce normal", "c'est cher"],
      a: "C'est exactement ce que vérifie l'analyse : le prix de chaque poste comparé à des ordres de grandeur, les postes oubliés ou comptés deux fois, et les points à négocier. Pour savoir d'abord si l'analyse vaut le coup sur votre devis, demandez le pré-diagnostic gratuit (réponse sous 24 h).", l: PREDIAG },
    { w: 2, q: "Et en outre-mer ?", k: ["outre-mer", "outre mer", "dom", "réunion", "reunion", "guadeloupe", "martinique", "guyane", "mayotte", "974", "971", "972"],
      a: "Oui, j'analyse aussi les devis d'outre-mer, au même prix. Attention, les règles diffèrent : en Guadeloupe, en Martinique et à La Réunion, la TVA est de 2,1 % pour la plupart des travaux de rénovation d'un logement de plus de 2 ans, et de 8,5 % au taux normal ; en Guyane et à Mayotte, la TVA ne s'applique pas. Vérifiez aussi que l'attestation décennale couvre bien votre territoire.", l: ["/guide-tva-travaux-renovation.html#outre-mer", "La TVA en outre-mer"] },
    { w: 2, q: "Mon cas est-il couvert ?", k: ["copro", "copropriété", "assemblée générale", "ccmi", "maison neuve", "constructeur", "piscine", "assainissement", "fosse", "spanc", "amiante", "désamiantage", "véranda", "surélévation", "facture finale", "travaux finis", "travaux terminés"],
      a: "La page « Votre cas est-il couvert ? » fait le point type par type : ce que j'analyse, ce qui se voit au cas par cas avec le pré-diagnostic gratuit, et vers qui aller quand ce n'est pas pour moi.", l: ["/votre-cas.html", "Votre cas est-il couvert ?"], l2: PREDIAG },
    { w: 2, q: "Vous êtes un professionnel ?", k: ["agent immobilier", "agents immobiliers", "agence", "courtier", "notaire", "syndic", "professionnel", "partenariat", "prescripteur", "mes clients"],
      a: "Agents immobiliers, courtiers, notaires, syndics : vos clients peuvent faire relire leurs devis de travaux, sans commission versée ni reçue. La page dédiée explique ce qu'ils reçoivent et comment ça se passe.", l: ["/professionnels.html", "La page professionnels"] },
    { w: 2, q: "Véranda, piscine ou poêle ?", k: ["véranda", "veranda", "piscine", "bassin", "poêle", "poele", "granulés", "granules", "insert", "conduit de fumée", "tubage"],
      a: "Oui, j'analyse ces devis. Chaque page explique ce que je vérifie : dalle et raccord au mur pour une véranda, terrassement et sécurité pour une piscine, conduit et sortie de toit pour un poêle.", l: ["/analyse-devis-veranda.html", "Véranda", "/analyse-devis-piscine.html", "Piscine", "/analyse-devis-poele.html", "Poêle"] },
    { c: 1, q: "Comment vous contacter ?", k: ["contact", "contacter", "écrire", "ecrire", "mail", "email", "message", "formulaire"],
      a: "Par le formulaire de contact, réponse sous 24 h. Le numéro de téléphone de l'entreprise figure aussi dans les mentions légales. Pour faire analyser un devis, commandez directement en ligne : vous m'envoyez ensuite le devis par e-mail.", l: ["/contact.html", "Formulaire de contact"] }
  ];

  var css = "#cp-chat-btn{position:fixed;right:20px;bottom:20px;z-index:9999;display:flex;align-items:center;gap:10px;background:#bf4a17;color:#fff;border:0;border-radius:2px;padding:14px 20px;font:700 16px 'Source Sans 3',Arial,sans-serif;box-shadow:0 8px 24px rgba(0,0,0,.3);cursor:pointer}" +
    "#cp-chat-btn:hover{background:#b8461a}#cp-chat-btn.mini{padding:12px;border-radius:50%}#cp-chat-btn.mini span{position:absolute;left:-9999px}" +
    "#cp-chat{position:fixed;right:20px;bottom:86px;z-index:9999;width:min(380px,calc(100vw - 40px));max-height:min(560px,calc(100vh - 120px));display:none;flex-direction:column;background:#ffffff;color:#14284b;border-radius:10px;box-shadow:0 16px 48px rgba(0,0,0,.35);overflow:hidden;font-family:'Source Sans 3',Arial,sans-serif}" +
    "#cp-chat.open{display:flex}" +
    "#cp-chat header{background:#0f2747;color:#fff;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;gap:10px}" +
    "#cp-chat header b{font-family:Archivo,Arial,sans-serif;}" +
    "#cp-chat header small{display:block;color:#c9d3ea;font-size:13px;font-weight:400;letter-spacing:0}" +
    "#cp-close{background:none;border:0;color:#fff;font-size:26px;line-height:1;cursor:pointer;width:44px;height:44px}" +
    "#cp-log{flex:1;overflow-y:auto;padding:14px;display:flex;flex-direction:column;gap:10px}" +
    ".cp-m{max-width:85%;padding:10px 13px;border-radius:12px;font-size:15px;line-height:1.45;overflow-wrap:anywhere}" +
    ".cp-bot{background:#fff;border:1px solid #d8dee6;align-self:flex-start}" +
    ".cp-user{background:#14284b;color:#fff;align-self:flex-end}" +
    ".cp-chips{display:flex;flex-wrap:wrap;gap:6px}" +
    ".cp-chip{background:#fff;border:1.5px solid #14284b;color:#14284b;border-radius:2px;padding:8px 12px;font:600 14px 'Source Sans 3',Arial,sans-serif;cursor:pointer;min-height:36px}" +
    ".cp-chip:hover{background:#eef2f8}.cp-faqh{margin:6px 0 0;font-size:13px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:#5b6784}" +
    ".cp-cta{display:inline-block;margin-top:6px;background:#bf4a17;color:#fff!important;text-decoration:none;font-weight:700;padding:9px 14px;border-radius:2px}" +
    "#cp-form{display:flex;gap:8px;padding:10px;border-top:1px solid #e6e9ee;background:#fff}" +
    "#cp-in{flex:1;border:1px solid #c5ccd6;border-radius:2px;padding:10px;font:15px 'Source Sans 3',Arial,sans-serif;min-width:0}" +
    "#cp-send{background:#14284b;color:#fff;border:0;border-radius:2px;padding:0 14px;font-weight:700;cursor:pointer;min-height:44px}" +
    "@media (max-width:600px){#cp-chat-btn{right:12px;bottom:12px;padding:12px;border-radius:50%}#cp-chat-btn span{position:absolute;left:-9999px}body{padding-bottom:72px}#cp-chat{left:0;right:0;top:0;bottom:0!important;width:100%;max-height:none;border-radius:0}}";
  var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);

  var btn = document.createElement("button");
  btn.id = "cp-chat-btn"; btn.type = "button"; btn.setAttribute("aria-expanded", "false"); btn.setAttribute("aria-controls", "cp-chat");
  btn.innerHTML = '<svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg><span>Une question ?</span>';

  var box = document.createElement("section");
  box.id = "cp-chat"; box.setAttribute("aria-label", "Assistant Contre-Plan");
  box.innerHTML = '<header><div><b>CONTRE-PLAN</b><small>Assistant automatique : orientation et questions fréquentes</small></div><button id="cp-close" type="button" aria-label="Fermer">×</button></header>' +
    '<div id="cp-log" aria-live="polite"></div>' +
    '<form id="cp-form"><label for="cp-in" style="position:absolute;left:-9999px">Votre question</label><input id="cp-in" type="text" placeholder="Posez votre question…" autocomplete="off"><button id="cp-send" type="submit">Envoyer</button></form>';
  document.body.appendChild(btn); document.body.appendChild(box);

  var log = box.querySelector("#cp-log"), input = box.querySelector("#cp-in"), started = false;

  function add(text, who, html) {
    var d = document.createElement("div"); d.className = "cp-m " + (who === "user" ? "cp-user" : "cp-bot");
    if (html) d.innerHTML = text; else d.textContent = text;
    log.appendChild(d); log.scrollTop = log.scrollHeight; return d;
  }
  var FALLBACK = "Je n'ai pas de réponse toute prête à cette question. Je vous réponds personnellement sous 24 h par le formulaire de contact. Vous pouvez aussi demander le pré-diagnostic gratuit de votre devis.";
  var ctaShown = false;
  var AI_URL = "https://contre-plan-decodeur.bitter-heart-1579.workers.dev/question", SITEKEY = "0x4AAAAAAFuFDFliNKSy-7Rr";
  var hist = [], tsWid = null, tsLoad = null, tsBox = null;
  function tsReady() {
    if (!SITEKEY) return Promise.resolve("");
    if (!tsLoad) tsLoad = new Promise(function (ok) {
      window.cpTs = function () { ok(); };
      var sc = document.createElement("script"); sc.src = "https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit&onload=cpTs"; sc.async = true; sc.onerror = function () { ok(); }; document.head.appendChild(sc);
    });
    return tsLoad.then(function () {
      if (!window.turnstile) return "";
      tsBox = document.createElement("div"); log.appendChild(tsBox);
      tsWid = turnstile.render(tsBox, { sitekey: SITEKEY, appearance: "interaction-only", language: "fr" });
      return new Promise(function (ok) {
        var n = 0, t = setInterval(function () {
          var v = ""; try { v = turnstile.getResponse(tsWid) || ""; } catch (x) {}
          if (n === 12 && !v && window.cpWait) window.cpWait.textContent = "Petite vérification anti-robot : cochez la case ci-dessous, puis patientez.";
          if (v || ++n > 240) { clearInterval(t); ok(v); }
        }, 250);
      });
    });
  }
  function aiAsk(text, done) {
    var wait = window.cpWait = add("Je cherche la réponse…", "bot"), snd = box.querySelector("#cp-send");
    input.disabled = true; snd.disabled = true;
    var fin = done; done = function (m, ok) {
      input.disabled = false; snd.disabled = false; window.cpWait = null;
      try { if (tsWid !== null) turnstile.remove(tsWid); } catch (x) {} tsWid = null; if (tsBox && tsBox.parentNode) tsBox.parentNode.removeChild(tsBox);
      fin(m, ok);
    };
    tsReady().then(function (jeton) {
      if (SITEKEY && !jeton) throw 0;
      return fetch(AI_URL, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ question: text, historique: hist.slice(-6), jeton: jeton }) }).then(function (r) { return r.json(); });
    }).then(function (d) {
      if (d && d.hors_sujet) { gc("ia-hors-sujet"); wait.textContent = "Je réponds seulement aux questions sur les devis de travaux et sur l'analyse Contre-Plan. Pour toute autre demande, écrivez-moi par le formulaire de contact."; done(wait, false); return; }
      if (!d || d.erreur || !d.reponse) throw 0;
      gc("ia-reponse");
      wait.textContent = d.reponse;
      hist.push({ role: "user", texte: text });
      if (d.lien_url && /^\/(?!\/)[A-Za-z0-9._\-\/#]*$/.test(d.lien_url)) { var l = link(d.lien_url, d.lien_texte || "En savoir plus", false); wait.appendChild(document.createElement("br")); wait.appendChild(l); }
      var n0 = document.createElement("small"); n0.style.cssText = "display:block;margin-top:6px;color:#5b6784;font-size:12px"; n0.textContent = "Réponse automatique à partir des informations du site."; wait.appendChild(n0);
      done(wait, true);
    }).catch(function () {
      gc("ia-indisponible");
      wait.textContent = FALLBACK;
      done(wait, false);
    });
  }
  function focusNext() {
    setTimeout(function () { var w = log.querySelectorAll(".cp-chips"), last = w[w.length - 1]; var f = last && last.parentNode && last.querySelector(".cp-chip"); (f || input).focus({ preventScroll: true }); }, 30);
  }
  function chips() {
    var w = document.createElement("div"); w.className = "cp-chips";
    KB.forEach(function (e) {
      if (!e.c) return;
      var c = document.createElement("button"); c.type = "button"; c.className = "cp-chip"; c.textContent = e.q;
      c.onclick = function () { ask(e.q, e); }; w.appendChild(c);
    });
    log.appendChild(w); log.scrollTop = log.scrollHeight;
  }
  function norm(s) { s = s.toLowerCase(); try { s = s.normalize("NFD").replace(/[̀-ͯ]/g, ""); } catch (x) {} return s.replace(/[’]/g, "'"); }
  function find(t) {
    var n = norm(t), best = null, score = 0;
    KB.forEach(function (e) { var s = 0; e.k.forEach(function (k) { if (n.indexOf(norm(k)) !== -1) s += k.length; }); s *= (e.w || 1); if (s > score) { score = s; best = e; } });
    return best;
  }
  function sub(href, text) { var l = link(href, text, false); m0.appendChild(l); }
  var m0 = null;
  function ask(text, entry) {
    add(text, "user");
    var e = entry || find(text);
    gc(e ? "faq-" + e.q : "faq-sans-reponse");
    if (!e && AI_URL) { aiAsk(text, function (m, ok) { m0 = m; if (!ok) { sub("/contact.html", "Formulaire de contact"); sub(PREDIAG[0], PREDIAG[1]); } if (!ctaShown) { ctaShown = true; m.appendChild(document.createElement("br")); m.appendChild(link(COMEUP, "Faire analyser mon devis", true, "clic-commander-chat")); } log.scrollTop = log.scrollHeight; input.focus({ preventScroll: true }); }); return; }
    if (e) hist.push({ role: "user", texte: text });
    setTimeout(function () {
      var m = m0 = add(e ? e.a : FALLBACK, "bot");
      if (!e) { sub("/contact.html", "Formulaire de contact"); sub(PREDIAG[0], PREDIAG[1]); }
      if (e && e.l) for (var li = 0; li < e.l.length; li += 2) sub(e.l[li], e.l[li + 1]);
      if (e && e.l2) sub(e.l2[0], e.l2[1]);
      if (!(e && e.nocta)) {
        if (!ctaShown) { ctaShown = true; m.appendChild(document.createElement("br")); m.appendChild(link(COMEUP, "Faire analyser mon devis", true, "clic-commander-chat")); }
        else sub(COMEUP, "Commander mon analyse");
      }
      log.scrollTop = log.scrollHeight;
      input.focus({ preventScroll: true });
    }, 250);
  }
  function gc(path) { try { window.goatcounter && window.goatcounter.count({ path: "chat/" + path, title: "Assistant : " + path, event: true }); } catch (x) {} }
  function link(href, text, primary, ev) {
    var a = document.createElement("a"); a.href = href; a.textContent = text;
    if (/^https?:/.test(href)) { a.target = "_blank"; a.rel = "noopener"; }
    a.style.cssText = primary ? "" : "display:block;margin-top:8px;color:#b8461a;font-weight:700";
    if (primary) a.className = "cp-cta";
    if (ev) a.onclick = function () { gc(ev); };
    return a;
  }
  function choose(question, options, cb) {
    add(question, "bot");
    var w = document.createElement("div"); w.className = "cp-chips";
    options.forEach(function (o) {
      var c = document.createElement("button"); c.type = "button"; c.className = "cp-chip"; c.textContent = o[0];
      c.onclick = function () { w.remove(); add(o[0], "user"); setTimeout(function () { cb(o); }, 250); };
      w.appendChild(c);
    });
    log.appendChild(w); log.scrollTop = log.scrollHeight; focusNext();
  }
  var PAGES = { sdb: ["/analyse-devis-salle-de-bain.html", "Ce que je vérifie sur un devis de salle de bain"],
    iso: ["/analyse-devis-isolation.html", "Ce que je vérifie sur un devis d'isolation"],
    toit: ["/analyse-devis-toiture.html", "Ce que je vérifie sur un devis de toiture"],
    pac: ["/analyse-devis-pompe-a-chaleur.html", "Ce que je vérifie sur un devis de pompe à chaleur"] };
  function qualify() {
    gc("orientation-debut");
    var r = {};
    choose("C'est pour quels travaux ?", [["Salle de bain", "sdb"], ["Isolation", "iso"], ["Toiture", "toit"], ["Pompe à chaleur", "pac"], ["Cuisine", "cuisine"], ["Autre", "autre"]], function (t) {
      r.t = t[1]; gc("travaux-" + t[1]);
      choose("Le devis fait combien, à peu près ?", [["Moins de 5 000 €", "moins-5k"], ["De 5 000 à 20 000 €", "5-20k"], ["Plus de 20 000 €", "plus-20k"], ["Je n'ai pas encore de devis", "pas-de-devis"]], function (m) {
        r.m = m[1]; gc("montant-" + m[1]);
        if (r.m === "pas-de-devis") return result(r);
        choose("Vous devez signer quand ?", [["Cette semaine", "semaine"], ["Ce mois-ci", "mois"], ["Pas de date pour l'instant", "sans-date"], ["C'est déjà signé", "signe"]], function (d) {
          r.d = d[1]; gc("signature-" + d[1]); result(r);
        });
      });
    });
  }
  function result(r) {
    var m, page = PAGES[r.t];
    if (r.m === "pas-de-devis") {
      gc("resultat-preparer");
      m = add("Vous êtes au bon moment : c'est avant de demander les devis qu'on évite le plus de pièges. Commencez par décrire votre projet de la même façon à chaque artisan, pour recevoir des offres comparables.", "bot");
      m.appendChild(link("/guide-bien-demander-ses-devis.html", "Comment bien demander ses devis", false, "lien-guide-demander"));
      m.appendChild(link("/checklist-devis-travaux.pdf", "La check-list à imprimer (PDF)", false, "lien-checklist"));
      m.appendChild(link("https://docs.google.com/forms/d/e/1FAIpQLScS7zVctXEahK71wNv8hUGD-MjfyqH4h_l8EpJyYPLVM-ToAA/viewform", "Recevoir le conseil devis du mois", false, "lien-conseil-du-mois"));
    } else if (r.d === "signe") {
      gc("resultat-deja-signe");
      m = add("Si vous avez signé chez vous ou à distance, vous avez en principe 14 jours pour vous rétracter. L'analyse vous aide à décider à temps : prenez l'option express pour avoir le rapport en 24 h.", "bot");
      m.appendChild(document.createElement("br")); m.appendChild(link(COMEUP, "Faire analyser mon devis en express", true, "clic-commander-orientation-signe"));
      m.appendChild(link("/guide-annuler-devis-signe-retractation.html", "Vos droits après signature", false, "lien-guide-retractation"));
    } else if (r.d === "semaine") {
      gc("resultat-urgent");
      m = add("Vous signez bientôt : faites relire le devis avant. Choisissez l'option express : vous recevez le rapport sous 24 h, avec les points à négocier et les questions à envoyer à l'artisan.", "bot");
      m.appendChild(document.createElement("br")); m.appendChild(link(COMEUP, "Faire analyser mon devis en express", true, "clic-commander-orientation-urgent"));
    } else if (r.m === "plus-20k") {
      gc("resultat-gros-devis");
      m = add("Sur un devis de plus de 20 000 €, chaque ligne compte. Jusqu'à 30 000 €, vous pouvez commander l'analyse directement. Au-delà, ou pour une rénovation tous corps d'état, demandez d'abord le pré-diagnostic gratuit : le prix vous est annoncé avant toute commande.", "bot");
      m.appendChild(document.createElement("br")); m.appendChild(link(COMEUP, "Faire analyser mon devis", true, "clic-commander-orientation-gros"));
      m.appendChild(link(PREDIAG[0], PREDIAG[1], false, "clic-prediagnostic-orientation-gros"));
    } else {
      gc("resultat-standard");
      m = add("Le bon moment pour faire relire votre devis, c'est avant de le signer. Vous recevez sous 48 h un rapport avec le verdict, les prix poste par poste, les oublis et les questions à poser à l'artisan.", "bot");
      m.appendChild(document.createElement("br")); m.appendChild(link(COMEUP, "Faire analyser mon devis", true, "clic-commander-orientation"));
      m.appendChild(link("/exemple-rapport-contre-plan.pdf", "Voir un exemple de rapport", false, "lien-exemple-rapport"));
    }
    if (page) m.appendChild(link(page[0], page[1], false, "lien-page-" + r.t));
    var w = document.createElement("div"); w.className = "cp-chips";
    var c = document.createElement("button"); c.type = "button"; c.className = "cp-chip"; c.textContent = "J'ai une autre question";
    c.onclick = function () { w.remove(); add("Choisissez une question ou écrivez la vôtre.", "bot"); chips(); focusNext(); };
    w.appendChild(c); log.appendChild(w); log.scrollTop = log.scrollHeight; focusNext();
  }
  function welcome() {
    add("Bonjour ! Je vous oriente en 3 questions, ou je réponds à vos questions sur l'analyse de devis.", "bot");
    var w = document.createElement("div"); w.className = "cp-chips";
    [["J'ai un devis à faire vérifier", function () { qualify(); }], ["J'ai une question", function () { gc("faq-debut"); add("Choisissez une question ou écrivez la vôtre.", "bot"); chips(); focusNext(); }]].forEach(function (o) {
      var c = document.createElement("button"); c.type = "button"; c.className = "cp-chip"; c.textContent = o[0];
      c.onclick = function () { w.remove(); f.remove(); fq.remove(); add(o[0], "user"); setTimeout(o[1], 250); }; w.appendChild(c);
    });
    log.appendChild(w);
    var f = document.createElement("p"); f.className = "cp-faqh"; f.textContent = "Questions fréquentes"; log.appendChild(f);
    var fq = document.createElement("div"); fq.className = "cp-chips";
    KB.forEach(function (e) { if (!e.c) return; var c = document.createElement("button"); c.type = "button"; c.className = "cp-chip"; c.textContent = e.q; c.onclick = function () { w.remove(); f.remove(); fq.remove(); ask(e.q, e); }; fq.appendChild(c); });
    log.appendChild(fq); log.scrollTop = log.scrollHeight;
  }
  function open(v) {
    box.classList.toggle("open", v); btn.setAttribute("aria-expanded", v ? "true" : "false");
    document.body.classList.toggle("cp-chat-open", v);
    if (v && !started) { started = true; gc("ouverture"); welcome(); }
    if (v && innerWidth > 760) input.focus(); else if (v) { var c0 = log.querySelector(".cp-chip"); if (c0) c0.focus({ preventScroll: true }); }
  }
  btn.onclick = function () { open(!box.classList.contains("open")); };
  box.querySelector("#cp-close").onclick = function () { open(false); btn.focus(); };
  document.addEventListener("keydown", function (ev) { if ((ev.key === "Escape" || ev.key === "Esc") && box.classList.contains("open")) { open(false); btn.focus(); } });
  if (/\/(contact|merci)(\.html)?$/.test(location.pathname)) btn.style.display = "none";
  /* Pages avec colonne latérale (sommaire, carte d'achat) : bouton rond, sans texte, pour ne rien recouvrir */
  if (document.querySelector(".cp-side, .cp-sidecard, .cp-toc, .cp-order")) { btn.classList.add("mini"); btn.setAttribute("aria-label", "Une question ?"); btn.title = "Une question ?"; }
  box.querySelector("#cp-form").onsubmit = function (ev) { ev.preventDefault(); var t = input.value.trim(); if (!t) return; input.value = ""; ask(t); };
})();
