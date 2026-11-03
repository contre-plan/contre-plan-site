# Page « Décodeur de ligne de devis » : outil gratuit qui explique une ligne de devis avec l'API Claude.
# Le navigateur appelle le relais Cloudflare (cloudflare/decodeur/worker.js), qui détient la clé API.
# Tant que DECODEUR_URL est vide, la page affiche « bientôt disponible » et n'est liée nulle part.

DECODEUR_URL = "https://contre-plan-decodeur.bitter-heart-1579.workers.dev"
TURNSTILE_SITEKEY = "0x4AAAAAAFuFDFliNKSy-7Rr"  # clé de site Cloudflare Turnstile (publique). Vide = pas de vérification anti-robot sur la page.

TRAVAUX = ["Salle de bain", "Cuisine", "Électricité", "Plomberie", "Chauffage, pompe à chaleur", "Isolation",
           "Toiture, charpente", "Fenêtres, menuiseries", "Maçonnerie, gros œuvre", "Carrelage, sols",
           "Peinture, plâtrerie", "Façade", "Extension, construction neuve", "Terrasse, extérieurs", "Autre"]

CSS = """<style>
.dec-form{background:#fff;border:1px solid #d8dee6;border-radius:4px;padding:20px 22px;margin:8px 0 24px;display:flex;flex-direction:column;gap:12px}
.dec-form label{font-weight:700;font-size:17px}
.dec-form textarea,.dec-form select{font:400 17px 'Source Sans 3',Arial,sans-serif;border:1.5px solid #9aa7b8;border-radius:4px;padding:12px 14px;width:100%;box-sizing:border-box;background:#fff;color:#14284b}
.dec-form textarea{min-height:96px;resize:vertical}
.dec-form textarea:focus,.dec-form select:focus{outline:3px solid #f2a33a;outline-offset:1px}
.dec-row{display:flex;flex-wrap:wrap;align-items:center;gap:12px;justify-content:space-between}
.dec-count{font-size:14px;color:#5b6b82}
.dec-form button.btn{border:0;cursor:pointer;align-self:flex-start}
.dec-form button.btn[disabled]{opacity:.6;cursor:wait}
.dec-ex{font-size:15px;color:#5b6b82}.dec-ex button{font:inherit;color:#1d4a8a;background:none;border:0;padding:0;text-decoration:underline;cursor:pointer}
.dec-res{background:#fff;border:1px solid #d8dee6;border-left:5px solid #14284b;border-radius:4px;padding:20px 22px;margin:0 0 24px}
.dec-res h2{margin-top:0!important}
.dec-badge{display:inline-block;font:800 14px Archivo,Arial,sans-serif;text-transform:uppercase;letter-spacing:.04em;padding:5px 10px;border-radius:3px;margin-bottom:10px}
.dec-badge.claire{background:#dff1e6;color:#1f6a3d}.dec-badge.a_preciser{background:#fff1d6;color:#8a5a00}.dec-badge.a_verifier{background:#fde3d8;color:#a33a10}
.dec-q{display:flex;flex-direction:column;gap:8px;margin:10px 0}
.dec-q p{margin:0;background:#f6f8fb;border-left:3px solid #bf4a17;padding:10px 14px}
.dec-err{background:#fde3d8;color:#7a2a0a;border-radius:4px;padding:12px 16px;margin:0 0 24px}
.dec-note{font-size:15px;color:#5b6b82}
</style>"""

FORM = """<form class="dec-form" id="dec-form" novalidate>
<label for="dec-ligne">Collez une ligne de votre devis</label>
<textarea id="dec-ligne" maxlength="400" placeholder="Exemple : Forfait mise en conformité électrique ..... 1 450,00 € HT" required></textarea>
<p class="dec-ex">Pas de devis sous la main ? Essayez un exemple : <button type="button" data-ex="Fourniture et pose receveur extra-plat 90x120 avec paroi fixe, 1 u, 1 280,00 € HT">receveur de douche</button>, <button type="button" data-ex="Main d'œuvre selon temps passé, régie">régie</button>, <button type="button" data-ex="Isolation combles perdus soufflage laine minérale R=7, 60 m²">isolation des combles</button>.</p>
<label for="dec-travaux">Type de travaux <span style="font-weight:400">(facultatif)</span></label>
<select id="dec-travaux"><option value="">Choisir…</option>{opts}</select>
{turnstile}<div class="dec-row"><button type="submit" class="btn" id="dec-go">Décoder la ligne</button><span class="dec-count" id="dec-count">0 / 400</span></div>
<p class="dec-note">Ne collez ni votre nom, ni votre adresse, ni le nom de l'entreprise : seule la ligne est utile. Le texte est envoyé à un outil d'intelligence artificielle pour produire l'explication ; Contre-Plan ne conserve ni le texte ni la réponse. <a href="confidentialite.html#quoi">En savoir plus</a>.</p>
</form>
<div id="dec-out" aria-live="polite"></div>"""

SOON = """<div class="note"><p><b>Bientôt disponible.</b> Le décodeur est en cours de mise en service. En attendant, le <a href="lexique-devis-travaux.html">lexique du devis</a> explique les termes les plus courants.</p></div>"""

JS = """<script>
(function(){
var URL_API = __URL__, SITEKEY = __SITEKEY__, wid = null;
window.decTurnstile = function(){ if (SITEKEY && window.turnstile) wid = turnstile.render("#dec-ts", {sitekey: SITEKEY, appearance: "interaction-only", language: "fr"}); };
var f = document.getElementById('dec-form'); if (!f) return;
var ta = document.getElementById('dec-ligne'), sel = document.getElementById('dec-travaux'), go = document.getElementById('dec-go'),
    out = document.getElementById('dec-out'), cnt = document.getElementById('dec-count');
var NIV = {claire: 'Ligne claire', a_preciser: 'À faire préciser', a_verifier: 'À vérifier avant de signer'};
function ty(x){ return String(x).replace(/ ([?!:;»])/g, '\\u00a0$1').replace(/« /g, '«\\u00a0').replace(/(\\d) (h|€|%|m²|m)(?![A-Za-zÀ-ÿ0-9])/g, '$1\\u00a0$2'); }
function el(t, c, txt){ var e = document.createElement(t); if (c) e.className = c; if (txt != null) e.textContent = ty(txt); return e; }
function count(){ cnt.textContent = ta.value.length + ' / 400'; }
ta.addEventListener('input', count);
Array.prototype.forEach.call(document.querySelectorAll('[data-ex]'), function(b){ b.addEventListener('click', function(){ ta.value = b.getAttribute('data-ex'); count(); ta.focus(); }); });
function err(m){ out.innerHTML = ''; out.appendChild(el('p', 'dec-err', m)); }
function gc(p){ try { if (window.goatcounter && window.goatcounter.count) window.goatcounter.count({path: 'decodeur/' + p, event: true}); } catch(e){} }
f.addEventListener('submit', function(e){
  e.preventDefault();
  var ligne = ta.value.trim();
  if (ligne.length < 4) { err('Collez une ligne de votre devis (au moins quelques mots).'); return; }
  var jeton = '';
  if (SITEKEY) { jeton = (window.turnstile && wid !== null) ? turnstile.getResponse(wid) : ''; if (!jeton) { err('Vérification anti-robot en cours : réessayez dans une seconde.'); return; } }
  go.disabled = true; go.textContent = 'Décodage en cours…'; out.innerHTML = '';
  gc('envoi');
  fetch(URL_API, {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({ligne: ligne, travaux: sel.value, jeton: jeton})})
  .then(function(r){ return r.json().catch(function(){ return {erreur: 'Le décodeur est indisponible pour le moment.'}; }); })
  .then(function(d){
    if (d.erreur) { err(d.erreur); gc('erreur'); return; }
    if (d.hors_sujet) { err("Cette phrase ne ressemble pas à une ligne de devis de travaux. Collez une ligne telle qu'elle apparaît sur votre devis (désignation, quantité, prix)."); gc('hors-sujet'); return; }
    gc('resultat-' + d.niveau);
    var box = el('div', 'dec-res');
    box.appendChild(el('span', 'dec-badge ' + d.niveau, NIV[d.niveau] || ''));
    box.appendChild(el('h2', null, d.intitule));
    box.appendChild(el('p', null, d.explication));
    if (d.a_verifier && d.a_verifier.length) { box.appendChild(el('h3', null, 'Ce qu\\u2019il faut vérifier')); var ul = el('ul'); d.a_verifier.forEach(function(x){ ul.appendChild(el('li', null, x)); }); box.appendChild(ul); }
    if (d.questions && d.questions.length) {
      box.appendChild(el('h3', null, 'Les questions à poser à l\\u2019artisan'));
      var q = el('div', 'dec-q'); d.questions.forEach(function(x){ q.appendChild(el('p', null, x)); }); box.appendChild(q);
      var cp = el('button', 'cp-copy', 'Copier les questions'); cp.type = 'button';
      cp.addEventListener('click', function(){ var t = d.questions.join('\\n'); (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).then(function(){ cp.textContent = 'Questions copiées'; cp.classList.add('ok'); gc('copie-questions'); }, function(){ cp.textContent = 'Sélectionnez le texte pour le copier'; }); });
      box.appendChild(cp);
    }
    box.appendChild(el('p', 'dec-note', "Explication générale produite automatiquement, sans le reste du devis ni les prix de votre région : ce n'est pas une expertise. Vérifiez auprès de l'artisan avant de signer."));
    var cta = el('div', 'cp-sidecard cp-upsell');
    cta.appendChild(el('p', 't', ty('Et le reste du devis ?')));
    if (d.niveau === 'a_verifier') cta.appendChild(el('p', null, ty('Cette ligne est à vérifier avant de signer : d\\u2019autres postes du même devis le sont peut-être aussi.')));
    cta.appendChild(el('p', null, ty('Les oublis et les prix gonflés se voient sur l\\u2019ensemble. Un ingénieur BTP relit tout votre devis : rapport PDF sous 48 h, dès __PRIX__.')));
    var a = el('a', 'cp-btn', 'Faire relire tout mon devis'); a.href = 'commander.html'; a.setAttribute('data-goatcounter-click', 'decodeur/clic-commander'); cta.appendChild(a);
    var ex = el('a', 'cp-sublink', 'Voir un exemple de rapport'); ex.href = 'exemple-rapport-contre-plan.pdf'; ex.target = '_blank'; ex.rel = 'noopener'; ex.setAttribute('data-goatcounter-click', 'decodeur/clic-exemple'); cta.appendChild(ex);
    box.appendChild(cta);
    out.innerHTML = ''; out.appendChild(box); box.scrollIntoView({behavior: 'smooth', block: 'start'});
  })
  .catch(function(){ err('Connexion impossible. Vérifiez votre connexion internet et réessayez.'); gc('erreur-reseau'); })
  .then(function(){ go.disabled = false; go.textContent = 'Décoder la ligne'; if (SITEKEY && window.turnstile && wid !== null) turnstile.reset(wid); });
});
})();
</script>"""

EXPLAIN = """<h2>Ce que fait le décodeur</h2>
<ul><li>Il explique en langage simple ce que la ligne veut dire : ce que l'artisan va faire ou fournir.</li>
<li>Il dit si la ligne est claire, à faire préciser ou à vérifier avant de signer.</li>
<li>Il liste les points à contrôler (quantité, unité, matériau, ce qui est inclus ou non) et les questions à poser à l'artisan, prêtes à copier.</li></ul>
<h2>Ce qu'il ne fait pas</h2>
<ul><li>Il ne dit pas si un prix est trop cher : sans le devis complet ni les prix de votre région, ce serait deviner.</li>
<li>Il ne remplace pas une relecture complète : les vrais pièges sont souvent les postes absents, qu'on ne voit pas sur une seule ligne.</li></ul>
<p>Pour les termes du devis les plus courants, voyez aussi <a href="lexique-devis-travaux.html">le lexique du devis</a>, et pour écrire à l'artisan, <a href="modeles-messages-artisan.html">les modèles de messages</a>.</p>"""


def body():
    opts = "".join(f'<option>{t}</option>' for t in TRAVAUX)
    if not DECODEUR_URL:
        return CSS + SOON + EXPLAIN
    import json
    ts = ('<div id="dec-ts"></div>' if TURNSTILE_SITEKEY else "")
    tsjs = ('<script src="https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit&onload=decTurnstile" async defer></script>' if TURNSTILE_SITEKEY else "")
    return CSS + FORM.replace("{opts}", opts).replace("{turnstile}", ts) + JS.replace("__URL__", json.dumps(DECODEUR_URL)).replace("__SITEKEY__", json.dumps(TURNSTILE_SITEKEY)) + tsjs + EXPLAIN
