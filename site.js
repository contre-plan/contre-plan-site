/* Éléments interactifs Contre-Plan (fonctionnent avec ou sans animations) */
(function () {
  var NEWS = 'https://docs.google.com/forms/d/e/1FAIpQLScS7zVctXEahK71wNv8hUGD-MjfyqH4h_l8EpJyYPLVM-ToAA/viewform';
  var COMEUP = 'commander.html';
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function each(l, f) { Array.prototype.forEach.call(l, f); }
  function gc(path) { try { if (window.goatcounter && goatcounter.count) goatcounter.count({ path: path, title: path, event: true }); } catch (e) {} }

  /* ---------- Mini-test ---------- */
  function test() {
    var box = document.getElementById('cp-test'); if (!box) return;
    box.classList.add('cp-pas');
    var qs = box.querySelectorAll('.cp-q'), bar = box.querySelector('.cp-test-bar i'), res = box.querySelector('.cp-res'), cnt = box.querySelector('.cp-test-n'), done = false, last = false;
    function summary() {
      var out = [];
      each(qs, function (q) {
        var on = q.querySelector('button[aria-pressed="true"]'); if (!on) return;
        out.push(q.querySelector('p').textContent.replace(/\s*\(.*\)\s*\?$/, ' ?') + ' ' + on.textContent);
      });
      return 'Résultat du test en 6 questions :\n' + out.join('\n');
    }
    function update() {
      var answered = 0, issues = [];
      each(qs, function (q) {
        var on = q.querySelector('button[aria-pressed="true"]');
        if (on) { answered++; if (on.getAttribute('data-v') !== 'oui') issues.push(q.getAttribute('data-tip')); }
      });
      bar.style.width = (answered / qs.length * 100) + '%';
      var nxt = null; each(qs, function (q) { var on = !!q.querySelector('button[aria-pressed="true"]'); q.classList.toggle('done', on); if (!on && !nxt) nxt = q; });
      each(qs, function (q) { q.classList.toggle('cur', q === nxt); });
      if (cnt) cnt.textContent = nxt ? 'Question ' + (Array.prototype.indexOf.call(qs, nxt) + 1) + ' sur ' + qs.length + (answered ? ' · ' + answered + ' réponse' + (answered > 1 ? 's' : '') : '') : 'Terminé : votre résultat ci-dessous';
      if (answered < qs.length) {
        res.classList.remove('on');
        if (last && nxt && innerWidth < 761) setTimeout(function () { nxt.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'center' }); }, 180);
        return;
      }
      var n = issues.length, h, p;
      if (n === 0) { h = 'Votre devis coche les bases.'; p = 'Bonne nouvelle pour la forme. Reste ce qu\'un test ne peut pas voir : les prix poste par poste, les oublis techniques et l\'enchaînement des travaux.'; }
      else if (n <= 2) { h = n + ' point' + (n > 1 ? 's' : '') + ' à clarifier avant de signer.'; p = 'Rien d\'alarmant en soi, mais à faire préciser par écrit par l\'artisan :'; }
      else { h = n + ' points à vérifier : ne signez pas en l\'état.'; p = 'Ce sont autant de sources de suppléments ou de litiges. À faire préciser par écrit avant de vous engager :'; }
      res.innerHTML = '<h3>' + h + '</h3><p>' + p + '</p>' + (n ? '<ul>' + issues.map(function (t) { return '<li>' + t + '</li>'; }).join('') + '</ul>' : '') +
        '<p>Je peux relire votre devis ligne par ligne et vous dire précisément quoi demander.</p>' +
        '<a class="cp-cta" href="' + COMEUP + '" data-goatcounter-click="clic-commander-test">Faire analyser mon devis</a>' +
        '<p class="cp-more">Pas encore prêt ? <a href="contact.html?sujet=prediagnostic&amp;test=' + encodeURIComponent(summary()) + '" data-goatcounter-click="clic-prediagnostic-test">Envoyer ces réponses en pré-diagnostic gratuit</a>' +
        '<a href="' + NEWS + '" target="_blank" rel="noopener" data-goatcounter-click="clic-conseil-du-mois-test">Recevoir le conseil devis du mois par e-mail</a></p>';
      res.classList.add('on');
      if (!done) { done = true; gc('test-devis-termine'); setTimeout(function () { res.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' }); }, 120); }
    }
    update();
    each(qs, function (q) {
      each(q.querySelectorAll('button'), function (b) {
        b.addEventListener('click', function () {
          each(q.querySelectorAll('button'), function (o) { o.setAttribute('aria-pressed', o === b ? 'true' : 'false'); });
          last = true; update();
        });
      });
    });
  }

  /* ---------- Avant / après ---------- */
  function slider() {
    var ba = document.getElementById('cp-ba'); if (!ba) return;
    var input = ba.querySelector('input');
    function set(v) { ba.style.setProperty('--x', v + '%'); }
    input.addEventListener('input', function () { set(input.value); });
    set(input.value);
    if (reduce || !('IntersectionObserver' in window)) return;
    var io = new IntersectionObserver(function (en) {
      if (!en[0].isIntersecting) return; io.disconnect();
      var t0 = null, from = 92, to = 50;
      function step(t) { if (!t0) t0 = t; var k = Math.min(1, (t - t0) / 1400), e = 1 - Math.pow(1 - k, 3), v = from + (to - from) * e; set(v); input.value = v; if (k < 1) requestAnimationFrame(step); }
      setTimeout(function () { requestAnimationFrame(step); }, 300);
    }, { threshold: 0.5 });
    set(92); input.value = 92; io.observe(ba);
  }

  /* ---------- Calcul ---------- */
  function calc() {
    var c = document.getElementById('cp-calc'); if (!c) return;
    var input = c.querySelector('input'), out = c.querySelector('.out'), price = parseFloat(c.getAttribute('data-prix'));
    function fmt(v, d) { return v.toLocaleString('fr-FR', { minimumFractionDigits: d, maximumFractionDigits: d }); }
    function upd() {
      var m = parseFloat(String(input.value).replace(/\s/g, '').replace(',', '.'));
      if (!m || m < 100) { out.innerHTML = 'Exemple : sur un devis de 8\u00a0000\u00a0€, l\'analyse à ' + fmt(price, 2) + '\u00a0€ représente <b>' + fmt(price / 8000 * 100, 2) + '\u00a0%</b> du montant. Saisissez le vôtre.'; return; }
      var pct = price / m * 100, ex = m * 0.05;
      out.innerHTML = 'L\'analyse à ' + fmt(price, 2) + '\u00a0€ représente <b>' + fmt(pct, pct < 0.1 ? 2 : 1) + '\u00a0%</b> de votre devis de ' + fmt(m, 0) + '\u00a0€.<br>À titre d\'exemple, un écart de prix de 5\u00a0% sur ce devis représente ' + fmt(ex, 0) + '\u00a0€.';
    }
    input.addEventListener('input', upd); upd();
  }

  /* ---------- Barre mobile ---------- */
  function bar() {
    if (!('IntersectionObserver' in window) || document.getElementById('cp-depot') || document.querySelector('.cp-depot-ok')) return;
    var b = document.createElement('div'); b.id = 'cp-bar';
    b.innerHTML = '<span><b>Relu par un ingénieur</b>16,50 € · rapport 48 h</span><button type="button" class="cp-bar-q"><svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>Question</button><a href="' + COMEUP + '" data-goatcounter-click="clic-commander-barre">Faire analyser</a>';
    b.querySelector('.cp-bar-q').addEventListener('click', function () { var c = document.getElementById('cp-chat-btn'); if (c) c.click(); });
    document.body.appendChild(b);
    var top = document.getElementById('top') || document.querySelector('header');
    var past = false, hide = 0;
    var typing = false;
    function show() { var on = past && hide === 0 && !typing; b.classList.toggle('on', on); document.body.classList.toggle('cp-bar-on', on); }
    document.addEventListener('focusin', function (e) { typing = !!(e.target.closest && e.target.closest('#cp-calc, form, #cp-chat')); show(); });
    document.addEventListener('focusout', function () { setTimeout(function () { var a = document.activeElement; typing = !!(a && a.closest && a.closest('#cp-calc, form, #cp-chat')); show(); }, 0); });
    if (top) new IntersectionObserver(function (en) { past = !en[0].isIntersecting && en[0].boundingClientRect.top < 0; show(); }).observe(top);
    var ends = document.querySelectorAll('footer, section:last-of-type');
    var vis = new Set();
    var io = new IntersectionObserver(function (en) { en.forEach(function (e) { if (e.isIntersecting) vis.add(e.target); else vis.delete(e.target); }); hide = vis.size; show(); });
    each(ends, function (e) { io.observe(e); });
  }


  /* ---------- Boutons « Copier » ---------- */
  function copy() {
    each(document.querySelectorAll('.cp-copy'), function (b) {
      b.addEventListener('click', function () {
        var t = document.getElementById(b.getAttribute('data-copy')); if (!t) return;
        var txt = t.innerText, label = b.textContent;
        function done() { b.textContent = 'Copié ✓'; b.classList.add('ok'); gc('copie-modele-message'); setTimeout(function () { b.textContent = label; b.classList.remove('ok'); }, 1800); }
        if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(txt).then(done, function () { fallback(); });
        else fallback();
        function fallback() { var r = document.createRange(); r.selectNodeContents(t); var sel = getSelection(); sel.removeAllRanges(); sel.addRange(r); try { document.execCommand('copy'); done(); } catch (e) {} }
      });
    });
  }

  /* ---------- « Vous signez quand ? » ---------- */
  function when() {
    var w = document.querySelector('.cp-when'); if (!w) return;
    var r = w.querySelector('.r');
    var T = {
      vite: 'Prenez l\'option express (+ 5,50 €, une case à cocher en commandant) : le rapport arrive en 24 h, à temps pour répondre à l\'artisan. <a href="commander.html?express=1" data-goatcounter-click="clic-commander-quand-vite">Commander avec l\'express</a>',
      plus: 'L\'analyse standard suffit : rapport sous 48 h. Vous pouvez d\'abord faire <a href="#test">le test en 1 minute</a>.',
      signe: 'Signé chez vous ou à distance ? Vous avez en principe 14 jours pour vous rétracter, et l\'analyse vous aide à décider à temps. <a href="guide-annuler-devis-signe-retractation.html">Vos droits</a>'
    };
    each(w.querySelectorAll('button'), function (b) {
      b.addEventListener('click', function () {
        each(w.querySelectorAll('button'), function (o) { o.setAttribute('aria-pressed', o === b ? 'true' : 'false'); });
        r.innerHTML = T[b.getAttribute('data-w')]; gc('quand-signez-' + b.getAttribute('data-w'));
      });
    });
  }
  /* ---------- Page de commande : la formule choisie règle le bouton de paiement ---------- */
  /* Formule + case express : lien Stripe, prix du bouton et total à payer */
  function order() {
    var pay = document.getElementById('cp-pay'); if (!pay) return;
    var ex = document.getElementById('cp-express');
    function upd() {
      var r = document.querySelector('.cp-opt input:checked'); if (!r) return;
      var e = !!(ex && ex.checked), v = parseFloat(r.getAttribute('data-prix').replace(',', '.')) + (e ? 5.5 : 0);
      var t = (v % 1 ? v.toFixed(2).replace('.', ',') : String(v)) + '\u00a0€';
      pay.href = r.getAttribute(e ? 'data-href-e' : 'data-href');
      pay.setAttribute('data-goatcounter-click', 'clic-stripe-' + r.value + (e ? '-express' : ''));
      each(document.querySelectorAll('.pp, .cp-total .pt'), function (x) { x.textContent = t; });
      var t1 = document.querySelector('.cp-total-1'); if (t1) t1.hidden = r.value !== '1';
    }
    each(document.querySelectorAll('.cp-opt input'), function (r) {
      r.addEventListener('change', function () { if (r.checked) { upd(); gc('formule-' + r.value); } });
    });
    if (ex) ex.addEventListener('change', function () { upd(); gc('express-' + (ex.checked ? 'oui' : 'non')); });
    var m = location.search.match(/[?&]formule=(g1|g2|[123])/);
    if (m) { var r = document.querySelector('.cp-opt input[value="' + m[1] + '"]'); if (r) r.checked = true; }
    if (ex && /[?&]express=1/.test(location.search)) ex.checked = true;
    upd();
  }
  /* ---------- Page de commande : dépôt du devis avant paiement (programme Google, voir tools/depot-devis) ---------- */
  function depot() {
    var f = document.getElementById('cp-depot');
    if (!f) {
      var ok = document.querySelector('.cp-depot-ok'), ref = null;
      try { ref = sessionStorage.getItem('cp-depot'); } catch (e) {}
      if (ok && ref) {
        ok.hidden = false; ok.querySelector('.cp-depot-ref').textContent = ref;
        var m = document.querySelector('.cp-envoi-mail'); if (m) m.hidden = true;
        try { sessionStorage.removeItem('cp-depot'); } catch (e) {}
      }
      return;
    }
    var st = f.querySelector('.cp-depot-st'), btn = f.querySelector('button[type="submit"]');
    function err(t) { st.className = 'cp-depot-st err'; st.textContent = t; btn.disabled = false; }
    var acc = f.elements.accord, dl = f.querySelector('.cp-delai');
    function delai() {
      if (!acc || !dl) return;
      var ex = document.getElementById('cp-express');
      if (acc.checked) { dl.textContent = 'Rapport sous ' + (ex && ex.checked ? '24' : '48') + ' h après réception de votre devis.'; dl.className = 'cp-delai ok'; return; }
      var d = new Date(Date.now() + 16 * 86400000);
      dl.textContent = 'Case non cochée : la loi m\'oblige à attendre la fin du délai de rétractation de 14 jours avant de commencer.'; dl.className = 'cp-delai';
    }
    if (acc) { acc.addEventListener('change', delai); delai(); }
    var ex0 = document.getElementById('cp-express'); if (ex0) ex0.addEventListener('change', delai);
    var fin = f.elements.fichiers, fl = f.querySelector('.cp-file-list'), fz = f.querySelector('.cp-file');
    if (fin && fl) fin.addEventListener('change', function () {
      var n = [].map.call(fin.files, function (x) { return x.name; });
      fl.textContent = n.length ? (n.length > 1 ? n.length + ' fichiers ajoutés : ' : 'Fichier ajouté : ') + n.join(', ') : '';
      if (fz) fz.classList.toggle('ok', n.length > 0);
    });
    function type(n) { n = n.toLowerCase(); return /\.pdf$/.test(n) ? 'application/pdf' : /\.png$/.test(n) ? 'image/png' : /\.(heic|heif)$/.test(n) ? 'image/heic' : /\.webp$/.test(n) ? 'image/webp' : 'image/jpeg'; }
    function brut(file) {
      return new Promise(function (ok, ko) {
        var fr = new FileReader();
        fr.onload = function () { var s = String(fr.result); ok({ nom: file.name, type: file.type || type(file.name), data: s.slice(s.indexOf(',') + 1), taille: file.size }); };
        fr.onerror = ko; fr.readAsDataURL(file);
      });
    }
    /* Photos de téléphone : réduites à 2200 px (JPEG) avant l'envoi, pour passer sous 10 Mo. Si le navigateur ne sait pas lire l'image, on envoie l'original. */
    function lire(file) {
      var t = file.type || type(file.name);
      if (!/^image\//.test(t) || file.size < 1.2e6) return brut(file);
      return new Promise(function (ok) {
        var url = URL.createObjectURL(file), img = new Image();
        img.onload = function () {
          var k = Math.min(1, (lire.n > 4 ? 1800 : 2200) / Math.max(img.naturalWidth, img.naturalHeight)), c = document.createElement('canvas');
          c.width = Math.round(img.naturalWidth * k); c.height = Math.round(img.naturalHeight * k);
          c.getContext('2d').drawImage(img, 0, 0, c.width, c.height); URL.revokeObjectURL(url);
          var d = c.toDataURL('image/jpeg', 0.85), data = d.slice(d.indexOf(',') + 1);
          ok({ nom: file.name.replace(/\.[^.]+$/, '') + '.jpg', type: 'image/jpeg', data: data, taille: Math.round(data.length * 0.75) });
        };
        img.onerror = function () { URL.revokeObjectURL(url); brut(file).then(ok); };
        img.src = url;
      });
    }
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var files = f.elements.fichiers.files, email = f.elements.email.value.trim(), r = document.querySelector('.cp-opt input:checked'), tot = 0, i;
      [f.elements.fichiers, f.elements.email].forEach(function (x) { x.removeAttribute('aria-invalid'); });
      function errChamp(x, t) { err(t); x.setAttribute('aria-invalid', 'true'); var z = x.id === 'cp-fichiers' ? f.querySelector('.cp-file') : x; if (z.scrollIntoView) z.scrollIntoView({ block: 'center' }); x.focus(); }
      if (!files.length) return errChamp(f.elements.fichiers, 'Ajoutez votre devis (PDF ou photo).');
      if (files.length > 10) return errChamp(f.elements.fichiers, 'Dix fichiers au maximum.');
      for (i = 0; i < files.length; i++) if (!/^image\//.test(files[i].type || type(files[i].name))) tot += files[i].size;
      if (tot > 10 * 1024 * 1024) return err('PDF trop lourd : 10 Mo au total au maximum. Envoyez les pages en photo ou passez par l\'e-mail ci-dessous.');
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) return errChamp(f.elements.email, 'Vérifiez votre adresse e-mail.');
      btn.disabled = true; st.className = 'cp-depot-st'; st.textContent = 'Envoi de votre devis…';
      lire.n = files.length;
      Promise.all([].map.call(files, lire)).then(function (arr) {
        var t2 = arr.reduce(function (a, x) { return a + (x.taille || 0); }, 0);
        if (t2 > 10 * 1024 * 1024) throw new Error('Fichiers trop lourds, même réduits (10 Mo au total).');
        arr.forEach(function (x) { delete x.taille; });
        return fetch(f.getAttribute('data-url'), { method: 'POST', body: JSON.stringify({
          formule: r ? r.value : '1', express: !!(document.getElementById('cp-express') || {}).checked, email: email, travaux: f.elements.travaux.value, echeance: f.elements.echeance.value,
          message: f.elements.message.value, accord: f.elements.accord.checked, site: f.elements.site.value, fichiers: arr }) });
      }).then(function (x) { return x.json(); }).then(function (d) {
        if (!d || !d.ok) throw new Error((d && d.erreur) || '');
        try { sessionStorage.setItem('cp-depot', d.ref); } catch (x) {}
        gc('depot-ok-' + (r ? r.value : '1'));
        st.textContent = 'Devis reçu (référence ' + d.ref + '). Redirection vers le paiement…';
        var u = document.getElementById('cp-pay').href;
        location.href = u + (u.indexOf('?') < 0 ? '?' : '&') + 'client_reference_id=' + encodeURIComponent(d.ref) + '&prefilled_email=' + encodeURIComponent(email);
      }).catch(function (x) {
        gc('depot-erreur');
        err(((x && x.message) || 'Le dépôt n\'a pas fonctionné.') + ' Vous pouvez aussi payer puis envoyer votre devis par e-mail (lien ci-dessous).');
      });
    });
  }
  /* ---------- Accueil : bouton « Une question ? » affiché seulement après le haut de page ---------- */
  function attente() {
    if (!document.querySelector('.hero2')) return;
    var b = document.body; function f() { b.classList.toggle('cp-attente', scrollY < innerHeight * 0.6); }
    f(); addEventListener('scroll', f, { passive: true });
  }
  function start() { test(); slider(); calc(); bar(); copy(); when(); order(); depot(); attente(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();

  (function () {
    var m = location.search.match(/[?&]sujet=([^&]+)/), sel = document.querySelector('.cp-form select');
    if (!m || !sel) return;
    if (m[1] === 'professionnel') { sel.value = 'Partenariat ou presse'; return; }
    if (m[1] === 'prediagnostic') { sel.value = 'Pré-diagnostic gratuit'; var t = document.querySelector('.cp-form textarea'); if (t && !t.value) t.placeholder = "Type de travaux, montant du devis, date de signature prévue, ce qui vous inquiète (3 lignes suffisent)."; var tm = location.search.match(/[?&]test=([^&]+)/); if (t && tm && !t.value) { try { t.value = decodeURIComponent(tm[1].replace(/\+/g, ' ')) + '\n\nTravaux et montant du devis : \nDate de signature prévue : '; } catch (e) {} } }
  })();

  /* ---------- Formulaire de contact : remerciement immédiat, envoi en arrière-plan ---------- */
  (function () {
    var f = document.querySelector('.cp-form'), box = document.getElementById('cp-form-ok');
    if (!f || !box || !window.fetch || !window.FormData) return;   // sans JavaScript : envoi classique vers Google Forms
    function show(html, err) {
      box.className = 'cp-form-ok' + (err ? ' err' : ''); box.innerHTML = html; box.hidden = false;
      box.scrollIntoView({ behavior: 'smooth', block: 'center' }); box.focus({ preventScroll: true });
    }
    f.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var hp = document.getElementById('cp-hp'); if (hp && hp.value) return;   // robot
      var data = new FormData(f), saved = {};
      var src = document.getElementById('cp-source'), msg = f.querySelector('textarea');
      if (src && src.value && msg) { data.set(msg.name, msg.value + "\n\n[Comment m'avez-vous connu : " + src.value + "]"); gc('source-' + src.value.toLowerCase().replace(/[^a-z]+/g, '-')); }
      Array.prototype.forEach.call(f.elements, function (el) { if (el.name && el.type !== 'hidden') saved[el.name] = el.value; });
      // Le visiteur n'attend pas la réponse du service d'envoi (souvent plusieurs secondes)
      f.reset();
      if (f.classList.contains('cp-avis')) show('<p class="t">Merci, votre avis est bien envoyé.</p><p>Je le lis personnellement. S\'il est publié, ce sera uniquement avec votre prénom ou vos initiales, et seulement si vous l\'avez accepté.</p>');
      else show('<p class="t">Merci, votre message est bien envoyé.</p><p>Je vous réponds sous 24 h à l\'adresse que vous avez indiquée. Pensez à regarder vos courriers indésirables.</p>');
      gc('formulaire-contact-envoye');
      // Google Forms ne renvoie pas de réponse lisible (mode no-cors) : seule une coupure réseau est détectable
      fetch(f.action, { method: 'POST', body: new URLSearchParams(data), mode: 'no-cors', keepalive: true })
        .catch(function () {
          // Échec : on remet le texte du visiteur et on le prévient
          Array.prototype.forEach.call(f.elements, function (el) { if (el.name && saved[el.name] != null) el.value = saved[el.name]; });
          show('<p class="t">Le message n\'est finalement pas parti.</p><p>Votre texte a été remis dans le formulaire : réessayez dans un instant, ou écrivez directement à <a href="mailto:contact@contre-plan.com">contact@contre-plan.com</a>.</p>', true);
          gc('formulaire-contact-echec');
        });
    });
  })();
})();
