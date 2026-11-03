# Page « Contrôle des mentions obligatoires d'un devis » : outil gratuit qui envoie la photo ou le PDF
# d'un devis au relais Cloudflare (route /mentions), lequel interroge l'API Claude. Rien n'est conservé.
# Publiée seulement si decodeur.DECODEUR_URL est rempli (même relais que le décodeur).
import json
import decodeur as DEC

CSS = """<style>
.men-drop{display:flex;flex-direction:column;align-items:center;gap:10px;border:2px dashed #9aa7b8;border-radius:6px;padding:26px 16px;text-align:center;background:#f6f8fb;cursor:pointer}
.men-drop:focus-within,.men-drop.on{border-color:#bf4a17;background:#fff7f2}
.men-drop input{position:absolute;left:-9999px}
.men-drop b{font:800 18px Archivo,Arial,sans-serif;color:#14284b}
.men-file{font-size:15px;color:#33415f;word-break:break-all}
.men-sum{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 12px}
.men-sum span{font:800 14px Archivo,Arial,sans-serif;padding:6px 10px;border-radius:3px}
.men-list{list-style:none;padding:0!important;margin:0 0 16px!important;display:flex;flex-direction:column;gap:8px}
.men-list li{display:grid;grid-template-columns:28px 1fr;gap:8px;align-items:start;background:#fff;border:1px solid #e1e6ee;border-radius:4px;padding:10px 12px;margin:0!important}
.men-list li::before{display:none!important}
.men-i{font:800 16px Archivo,Arial,sans-serif;width:24px;height:24px;border-radius:50%;display:grid;place-items:center;color:#fff}
.men-a_revoir .men-i{background:#5b6784}.men-presente .men-i{background:#2e7d4f}.men-incomplete .men-i{background:#c98a00}.men-absente .men-i{background:#bf4a17}.men-non_concernee .men-i{background:#9aa7b8}
.men-list b{display:block;font-size:16px}.men-list small{display:block;font-size:15px;color:#4a5872}
.s-presente{background:#dff1e6;color:#1f6a3d}.s-incomplete{background:#fff1d6;color:#8a5a00}.s-absente{background:#fde3d8;color:#a33a10}
</style>"""

FORM = """<form class="dec-form" id="men-form" novalidate>
<label class="men-drop" id="men-drop" for="men-file"><b>Choisir la photo ou le PDF du devis</b><span>Photo nette de chaque page, ou PDF de 4 Mo maximum</span><input id="men-file" type="file" accept="image/*,application/pdf"><span class="men-file" id="men-name"></span></label>
{turnstile}<div class="dec-row"><button type="submit" class="btn" id="men-go">Contrôler les mentions</button></div>
<p class="dec-note">Vous pouvez masquer votre nom et votre adresse avant l'envoi : ils ne servent pas au contrôle. Le fichier est transmis à un outil d'intelligence artificielle pour produire le résultat ; Contre-Plan ne conserve ni le fichier ni le résultat. <a href="confidentialite.html#quoi">En savoir plus</a>.</p>
</form>
<div id="men-out" aria-live="polite"></div>"""

JS = """<script>
(function(){
var URL_API = __URL__ + '/mentions', SITEKEY = __SITEKEY__, wid = null, envoi = null;
window.menTurnstile = function(){ if (SITEKEY && window.turnstile) wid = turnstile.render('#men-ts', {sitekey: SITEKEY, appearance: 'interaction-only', language: 'fr'}); };
var f = document.getElementById('men-form'); if (!f) return;
var inp = document.getElementById('men-file'), nm = document.getElementById('men-name'), go = document.getElementById('men-go'), out = document.getElementById('men-out'), drop = document.getElementById('men-drop');
var ICO = {presente: '✓', incomplete: '!', absente: '✕', non_concernee: '–', a_revoir: '?'};
var LIB = {presente: 'présente', incomplete: 'à préciser', absente: 'non trouvée sur le document', non_concernee: 'non concernée', a_revoir: 'à vérifier vous-même'};
function ty(x){ return String(x).replace(/ ([?!:;»])/g, '\\u00a0$1').replace(/« /g, '«\\u00a0').replace(/(\\d) (h|€|%|m²|m|Mo)(?![A-Za-zÀ-ÿ0-9])/g, '$1\\u00a0$2'); }
function el(t, c, txt){ var e = document.createElement(t); if (c) e.className = c; if (txt != null) e.textContent = ty(txt); return e; }
function err(m){ out.innerHTML = ''; out.appendChild(el('p', 'dec-err', m)); }
function gc(p){ try { if (window.goatcounter && window.goatcounter.count) window.goatcounter.count({path: 'mentions/' + p, event: true}); } catch(e){} }
inp.addEventListener('change', function(){ envoi = null; var x = inp.files && inp.files[0]; nm.textContent = x ? x.name : ''; drop.classList.toggle('on', !!x); });
['dragover','dragenter'].forEach(function(t){ drop.addEventListener(t, function(e){ e.preventDefault(); drop.classList.add('on'); }); });
drop.addEventListener('drop', function(e){ e.preventDefault(); if (e.dataTransfer.files[0]) { inp.files = e.dataTransfer.files; inp.dispatchEvent(new Event('change')); } });
function lire(file){
  return new Promise(function(ok, ko){
    if (file.type === 'application/pdf') {
      if (file.size > 4.4e6) return ko('PDF trop lourd (4 Mo maximum). Envoyez seulement les pages du devis, ou des photos.');
      var r = new FileReader(); r.onload = function(){ ok({type: 'application/pdf', data: String(r.result).split(',')[1]}); }; r.onerror = function(){ ko('Fichier illisible.'); }; r.readAsDataURL(file); return;
    }
    if (!/^image\\//.test(file.type)) return ko('Envoyez une photo ou un PDF.');
    var url = URL.createObjectURL(file), img = new Image();
    img.onload = function(){
      var k = Math.min(1, 2000 / Math.max(img.naturalWidth, img.naturalHeight)), c = document.createElement('canvas');
      c.width = Math.round(img.naturalWidth * k); c.height = Math.round(img.naturalHeight * k);
      c.getContext('2d').drawImage(img, 0, 0, c.width, c.height); URL.revokeObjectURL(url);
      ok({type: 'image/jpeg', data: c.toDataURL('image/jpeg', 0.85).split(',')[1]});
    };
    img.onerror = function(){ URL.revokeObjectURL(url); ko("Cette photo n'a pas pu être lue. Essayez une capture d'écran ou un PDF."); };
    img.src = url;
  });
}
f.addEventListener('submit', function(e){
  e.preventDefault();
  var file = inp.files && inp.files[0];
  if (!file) { err('Choisissez d\\u2019abord la photo ou le PDF de votre devis.'); return; }
  var jeton = '';
  if (SITEKEY) { jeton = (window.turnstile && wid !== null) ? turnstile.getResponse(wid) : ''; if (!jeton) { err('Vérification anti-robot en cours : réessayez dans une seconde.'); return; } }
  go.disabled = true; go.textContent = 'Contrôle en cours (jusqu\\u2019à 30 s)…'; out.innerHTML = '';
  gc('envoi');
  lire(file).then(function(fic){
    return fetch(URL_API, {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({fichier: fic.data, type: fic.type, jeton: jeton})})
      .then(function(r){ return r.json().catch(function(){ return {erreur: 'Le contrôle est indisponible pour le moment.'}; }); });
  }).then(function(d){
    if (d.erreur) { err(d.erreur); gc('erreur'); return; }
    if (d.est_devis === false) { err("Ce document ne ressemble pas à un devis de travaux. Envoyez la photo ou le PDF du devis lui-même."); gc('pas-un-devis'); return; }
    if (d.lisible === false) { err("Le devis est difficile à lire (flou, coupé ou trop petit). Reprenez une photo bien nette, à plat et en pleine lumière, ou envoyez le PDF."); gc('illisible'); return; }
    var n = {presente: 0, incomplete: 0, absente: 0};
    d.mentions.forEach(function(m){ if (n[m.statut] != null) n[m.statut]++; });
    gc('resultat-' + (n.absente ? 'absentes' : n.incomplete ? 'incompletes' : 'complet'));
    var box = el('div', 'dec-res');
    box.appendChild(el('h2', null, 'Mentions du devis' + (d.type_travaux ? ' : ' + d.type_travaux.toLowerCase() : '')));
    var sum = el('div', 'men-sum');
    sum.appendChild(el('span', 's-presente', n.presente + ' présentes')); sum.appendChild(el('span', 's-incomplete', n.incomplete + ' à préciser')); sum.appendChild(el('span', 's-absente', n.absente + ' non trouvées'));
    box.appendChild(sum);
    [['regl', 'Mentions prévues par la réglementation'], ['reco', 'Précisions recommandées']].forEach(function(g){
      var ms = d.mentions.filter(function(m){ return m.categorie === g[0]; }); if (!ms.length) return;
      box.appendChild(el('h3', null, g[1]));
      var ul = el('ul', 'men-list');
      ms.forEach(function(m){ var li = el('li', 'men-' + m.statut); li.appendChild(el('span', 'men-i', ICO[m.statut] || '?')); var t = el('div'); t.appendChild(el('b', null, m.libelle + ' : ' + (LIB[m.statut] || m.statut))); if (m.detail) t.appendChild(el('small', null, m.detail)); li.appendChild(t); ul.appendChild(li); });
      box.appendChild(ul);
    });
    if (d.a_retenir) box.appendChild(el('p', null, d.a_retenir));
    var manq = d.mentions.filter(function(m){ return m.statut === 'absente' || m.statut === 'incomplete'; });
    if (manq.length) {
      var msg = 'Bonjour,\\n\\nMerci pour votre devis. Avant de le signer, pourriez-vous me préciser ou ajouter les points suivants :\\n' + manq.map(function(m){ return '- ' + m.libelle.replace(/ \\((sur le devis|utile pour)[^)]*\\)$/, '').replace(/ \\(utile pour les aides\\)$/, ''); }).join('\\n') + '\\n\\nMerci par avance.\\nCordialement';
      var cp = el('button', 'cp-copy', 'Copier un message à envoyer à l\\u2019artisan'); cp.type = 'button';
      cp.addEventListener('click', function(){ (navigator.clipboard ? navigator.clipboard.writeText(msg) : Promise.reject()).then(function(){ cp.textContent = 'Message copié'; cp.classList.add('ok'); gc('copie-message'); }, function(){ cp.textContent = 'Copie impossible sur ce navigateur'; }); });
      box.appendChild(cp);
    }
    box.appendChild(el('p', 'dec-note', "Contrôle automatique du document transmis : une mention peut figurer dans des conditions générales non envoyées. Ce n'est pas une expertise et les prix ne sont pas vérifiés."));
    var cta = el('div', 'cp-sidecard cp-upsell');
    cta.appendChild(el('p', 't', ty('Les mentions ne disent pas tout')));
    cta.appendChild(el('p', null, ty('Un devis en règle peut cacher un prix gonflé ou un poste oublié. Un ingénieur BTP le relit ligne par ligne : rapport PDF sous 48 h, dès __PRIX__.')));
    var a = el('a', 'cp-btn', 'Faire relire mon devis'); a.href = 'commander.html'; a.setAttribute('data-goatcounter-click', 'mentions/clic-commander'); cta.appendChild(a);
    var ex = el('a', 'cp-sublink', 'Voir un exemple de rapport'); ex.href = 'exemple-rapport-contre-plan.pdf'; ex.target = '_blank'; ex.rel = 'noopener'; ex.setAttribute('data-goatcounter-click', 'mentions/clic-exemple'); cta.appendChild(ex);
    box.appendChild(cta);
    out.innerHTML = ''; out.appendChild(box); box.scrollIntoView({behavior: 'smooth', block: 'start'});
  }, function(m){ err(typeof m === 'string' ? m : 'Connexion impossible. Vérifiez votre connexion internet et réessayez.'); gc('erreur-lecture'); })
  .catch(function(){ err('Connexion impossible. Vérifiez votre connexion internet et réessayez.'); gc('erreur-reseau'); })
  .then(function(){ go.disabled = false; go.textContent = 'Contrôler les mentions'; if (SITEKEY && window.turnstile && wid !== null) turnstile.reset(wid); });
});
})();
</script>"""

EXPLAIN = """<h2>Ce que vérifie le contrôle</h2>
<p>Deux familles d'informations. D'abord les mentions prévues par la réglementation pour un devis de travaux : identité, SIRET et assurance de l'entreprise, date du devis, délai d'exécution, prix et TVA, gestion des déchets de chantier, conditions de paiement, médiateur de la consommation. Ensuite des précisions recommandées, qui ne sont pas obligatoires mais évitent les mauvaises surprises : détail des quantités et prix unitaires, références des matériaux, main-d'œuvre et, pour la rénovation énergétique, la qualification RGE et les performances utiles aux aides. Le détail est expliqué dans <a href="guide-mentions-obligatoires-devis.html">le guide des mentions d'un devis</a>.</p>
<h2>Ce qu'il ne vérifie pas</h2>
<ul><li>Les prix : sans connaître votre chantier ni votre région, ce serait deviner.</li>
<li>Les oublis techniques et l'enchaînement des travaux : un devis peut avoir toutes ses mentions et oublier l'étanchéité de la douche.</li></ul>
<p>Une ligne précise vous intrigue ? Essayez <a href="decodeur-ligne-devis.html">le décodeur de ligne de devis</a>.</p>"""


def body():
    ts = '<div id="men-ts"></div>' if DEC.TURNSTILE_SITEKEY else ""
    tsjs = ('<script src="https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit&onload=menTurnstile" async defer></script>' if DEC.TURNSTILE_SITEKEY else "")
    return DEC.CSS + CSS + FORM.replace("{turnstile}", ts) + JS.replace("__URL__", json.dumps(DEC.DECODEUR_URL)).replace("__SITEKEY__", json.dumps(DEC.TURNSTILE_SITEKEY)) + tsjs + EXPLAIN
