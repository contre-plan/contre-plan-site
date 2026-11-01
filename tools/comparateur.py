# Page « Comparateur de deux devis » : outil gratuit qui envoie deux devis (photo ou PDF) au relais
# Cloudflare (route /comparer), lequel interroge l'API Claude. Rien n'est conservé.
# Publiée seulement si decodeur.DECODEUR_URL est rempli (même relais que le décodeur).
import json
import decodeur as DEC

SLUG = "comparer-deux-devis"

CSS = """<style>
.cmp-files{display:grid;grid-template-columns:1fr 1fr;gap:12px}
@media(max-width:640px){.cmp-files{grid-template-columns:1fr}}
.cmp-drop{position:relative;display:flex;flex-direction:column;align-items:center;gap:8px;border:2px dashed #9aa7b8;border-radius:6px;padding:20px 12px;text-align:center;background:#f6f8fb;cursor:pointer}
.cmp-drop.on{border-color:#bf4a17;background:#fff7f2}
.cmp-drop input{position:absolute;left:-9999px}
.cmp-drop b{font:800 18px Archivo,Arial,sans-serif;color:#14284b}
.cmp-name{font-size:15px;color:#33415f;word-break:break-all}
.cmp-wrap{overflow-x:auto;margin:0 0 16px}
.cmp-t{width:100%;border-collapse:collapse;font-size:15px;table-layout:fixed}
@media(max-width:640px){.cmp-t{font-size:13.5px}.cmp-t th,.cmp-t td{padding:6px 6px!important;word-wrap:break-word}}
.cmp-t th,.cmp-t td{border:1px solid #e1e6ee;padding:8px 10px;text-align:left;vertical-align:top}
.cmp-t thead th{background:#14284b;color:#fff;font:800 15px Archivo,Arial,sans-serif}
.cmp-t tbody th{background:#f6f8fb;font-weight:700}
.cmp-t thead th:first-child{width:30%}
.cmp-seulement_a td.cmp-b,.cmp-seulement_b td.cmp-a{background:#fde3d8;color:#a33a10}
.cmp-different td.cmp-a,.cmp-different td.cmp-b{background:#fff1d6}
.cmp-a_preciser td.cmp-a,.cmp-a_preciser td.cmp-b{background:#f1f3f7}
.cmp-leg{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 12px;font-size:14px}
.cmp-leg span{padding:4px 8px;border-radius:3px}
</style>"""

FORM = """<form class="dec-form" id="cmp-form" novalidate>
<div class="cmp-files">
<label class="cmp-drop" id="cmp-drop-a" for="cmp-file-a"><b>Devis A</b><span>Photo nette ou PDF (2 Mo maximum)</span><input id="cmp-file-a" type="file" accept="image/*,application/pdf"><span class="cmp-name" id="cmp-name-a"></span></label>
<label class="cmp-drop" id="cmp-drop-b" for="cmp-file-b"><b>Devis B</b><span>Photo nette ou PDF (2 Mo maximum)</span><input id="cmp-file-b" type="file" accept="image/*,application/pdf"><span class="cmp-name" id="cmp-name-b"></span></label>
</div>
{turnstile}<div class="dec-row"><button type="submit" class="btn" id="cmp-go">Comparer les deux devis</button></div>
<p class="dec-note">Pour chaque devis : une photo nette de la page qui détaille les travaux et les totaux, ou le PDF complet (5 pages maximum). Vous pouvez masquer votre nom et votre adresse avant l'envoi : ils ne servent pas à la comparaison. Les fichiers sont transmis à un outil d'intelligence artificielle pour produire le résultat ; Contre-Plan ne conserve ni les fichiers ni le résultat. <a href="confidentialite.html#quoi">En savoir plus</a>.</p>
</form>
<div id="cmp-out" aria-live="polite"></div>"""

JS = """<script>
(function(){
var URL_API = __URL__ + '/comparer', SITEKEY = __SITEKEY__, wid = null;
window.cmpTurnstile = function(){ if (SITEKEY && window.turnstile) wid = turnstile.render('#cmp-ts', {sitekey: SITEKEY, appearance: 'interaction-only', language: 'fr'}); };
var f = document.getElementById('cmp-form'); if (!f) return;
var go = document.getElementById('cmp-go'), out = document.getElementById('cmp-out');
var LIB = {identique: 'identique', different: 'différent', seulement_a: 'seulement dans A', seulement_b: 'seulement dans B', a_preciser: 'à préciser'};
function ty(x){ return String(x).replace(/ ([?!:;»])/g, '\\u00a0$1').replace(/« /g, '«\\u00a0').replace(/(\\d) (h|€|%|m²|m|Mo)(?![A-Za-zÀ-ÿ0-9])/g, '$1\\u00a0$2'); }
function el(t, c, txt){ var e = document.createElement(t); if (c) e.className = c; if (txt != null) e.textContent = ty(txt); return e; }
function err(m){ out.innerHTML = ''; out.appendChild(el('p', 'dec-err', m)); }
function gc(p){ try { if (window.goatcounter && window.goatcounter.count) window.goatcounter.count({path: 'comparateur/' + p, event: true}); } catch(e){} }
['a','b'].forEach(function(k){
  var inp = document.getElementById('cmp-file-' + k), nm = document.getElementById('cmp-name-' + k), drop = document.getElementById('cmp-drop-' + k);
  inp.addEventListener('change', function(){ var x = inp.files && inp.files[0]; nm.textContent = x ? x.name : ''; drop.classList.toggle('on', !!x); });
  ['dragover','dragenter'].forEach(function(t){ drop.addEventListener(t, function(e){ e.preventDefault(); drop.classList.add('on'); }); });
  drop.addEventListener('drop', function(e){ e.preventDefault(); if (e.dataTransfer.files[0]) { inp.files = e.dataTransfer.files; inp.dispatchEvent(new Event('change')); } });
});
function lire(file, nom){
  return new Promise(function(ok, ko){
    if (file.type === 'application/pdf') {
      if (file.size > 2.0e6) return ko('PDF du ' + nom + ' trop lourd (2 Mo maximum). Envoyez seulement les pages du devis, ou une photo.');
      var r = new FileReader(); r.onload = function(){ ok({type: 'application/pdf', data: String(r.result).split(',')[1]}); }; r.onerror = function(){ ko('Fichier du ' + nom + ' illisible.'); }; r.readAsDataURL(file); return;
    }
    if (!/^image\\//.test(file.type)) return ko('Pour le ' + nom + ', envoyez une photo ou un PDF.');
    var url = URL.createObjectURL(file), img = new Image();
    img.onload = function(){
      var k = Math.min(1, 1800 / Math.max(img.naturalWidth, img.naturalHeight)), c = document.createElement('canvas');
      c.width = Math.round(img.naturalWidth * k); c.height = Math.round(img.naturalHeight * k);
      c.getContext('2d').drawImage(img, 0, 0, c.width, c.height); URL.revokeObjectURL(url);
      ok({type: 'image/jpeg', data: c.toDataURL('image/jpeg', 0.82).split(',')[1]});
    };
    img.onerror = function(){ URL.revokeObjectURL(url); ko("La photo du " + nom + " n'a pas pu être lue. Essayez une capture d'écran ou un PDF."); };
    img.src = url;
  });
}
function liste(box, titre, items){ if (!items || !items.length) return; box.appendChild(el('h3', null, titre)); var ul = el('ul'); items.forEach(function(x){ ul.appendChild(el('li', null, x)); }); box.appendChild(ul); }
f.addEventListener('submit', function(e){
  e.preventDefault();
  var fa = document.getElementById('cmp-file-a').files[0], fb = document.getElementById('cmp-file-b').files[0];
  if (!fa || !fb) { err('Choisissez les deux devis : le devis A et le devis B.'); return; }
  var jeton = '';
  if (SITEKEY) { jeton = (window.turnstile && wid !== null) ? turnstile.getResponse(wid) : ''; if (!jeton) { err('Vérification anti-robot en cours : réessayez dans une seconde.'); return; } }
  go.disabled = true; go.textContent = 'Comparaison en cours (jusqu\\u2019à 1 min)…'; out.innerHTML = '';
  gc('envoi');
  Promise.all([lire(fa, 'devis A'), lire(fb, 'devis B')]).then(function(x){
    return fetch(URL_API, {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({type_a: x[0].type, fichier_a: x[0].data, type_b: x[1].type, fichier_b: x[1].data, jeton: jeton})})
      .then(function(r){ return r.json().catch(function(){ return {erreur: 'La comparaison est indisponible pour le moment.'}; }); });
  }).then(function(d){
    if (d.erreur) { err(d.erreur); gc('erreur'); return; }
    if (d.sont_devis === false) { err("L'un des documents ne ressemble pas à un devis de travaux. Envoyez la photo ou le PDF des deux devis."); gc('pas-un-devis'); return; }
    if (d.lisibles === false) { err("L'un des devis est difficile à lire (flou, coupé ou trop petit). Reprenez une photo bien nette, à plat et en pleine lumière, ou envoyez le PDF."); gc('illisible'); return; }
    gc(d.meme_projet ? 'resultat' : 'resultat-projets-differents');
    var box = el('div', 'dec-res');
    box.appendChild(el('h2', null, 'Comparaison des deux devis' + (d.type_travaux ? ' : ' + d.type_travaux.toLowerCase() : '')));
    if (!d.meme_projet) box.appendChild(el('p', 'dec-err', "Attention : ces deux devis ne semblent pas porter sur les mêmes travaux. La comparaison ci-dessous est donc à prendre avec prudence."));
    var w1 = el('div', 'cmp-wrap'), t1 = el('table', 'cmp-t'), th = el('thead'), hr = el('tr');
    ['', 'Devis A', 'Devis B'].forEach(function(x){ hr.appendChild(el('th', null, x)); }); th.appendChild(hr); t1.appendChild(th);
    var tb = el('tbody');
    [['total_ttc','Total TTC'],['total_ht','Total HT'],['tva','TVA'],['acompte','Acompte'],['delai','Délai'],['validite','Validité']].forEach(function(r){
      var tr = el('tr'); tr.appendChild(el('th', null, r[1])); tr.appendChild(el('td', null, d.devis_a[r[0]])); tr.appendChild(el('td', null, d.devis_b[r[0]])); tb.appendChild(tr);
    });
    t1.appendChild(tb); w1.appendChild(t1); box.appendChild(w1);
    if (d.ecart_total) box.appendChild(el('p', null, d.ecart_total));
    box.appendChild(el('h3', null, 'Poste par poste'));
    var leg = el('div', 'cmp-leg');
    var l1 = el('span', null, 'Présent d\\u2019un seul côté'); l1.style.background = '#fde3d8'; leg.appendChild(l1);
    var l2 = el('span', null, 'Différent'); l2.style.background = '#fff1d6'; leg.appendChild(l2);
    var l3 = el('span', null, 'À préciser'); l3.style.background = '#f1f3f7'; leg.appendChild(l3);
    box.appendChild(leg);
    var w2 = el('div', 'cmp-wrap'), t2 = el('table', 'cmp-t'), th2 = el('thead'), hr2 = el('tr');
    ['Poste', 'Devis A', 'Devis B'].forEach(function(x){ hr2.appendChild(el('th', null, x)); }); th2.appendChild(hr2); t2.appendChild(th2);
    var tb2 = el('tbody');
    d.postes.forEach(function(p){ var tr = el('tr', 'cmp-' + p.ecart); tr.title = LIB[p.ecart] || ''; tr.appendChild(el('th', null, p.poste)); tr.appendChild(el('td', 'cmp-a', p.a)); tr.appendChild(el('td', 'cmp-b', p.b)); tb2.appendChild(tr); });
    t2.appendChild(tb2); w2.appendChild(t2); box.appendChild(w2);
    liste(box, 'Ce qui empêche de comparer à égalité', d.points_attention);
    liste(box, 'Questions à poser à l\\u2019entreprise du devis A', d.questions_a);
    liste(box, 'Questions à poser à l\\u2019entreprise du devis B', d.questions_b);
    if (d.a_retenir) box.appendChild(el('p', null, d.a_retenir));
    box.appendChild(el('p', 'dec-note', "Comparaison automatique de ce qui est écrit sur les documents transmis. Elle ne dit pas quel devis choisir et ne juge pas les prix. Ce n'est pas une expertise."));
    var cta = el('div', 'note'), p = el('p');
    p.appendChild(el('b', null, 'Le moins cher n\\u2019est pas toujours le moins coûteux. ')); p.appendChild(document.createTextNode(ty('Pour savoir si les prix sont cohérents et ce qui manque techniquement, faites relire vos devis ligne par ligne par un ingénieur BTP, rapport sous 48 h. ')));
    var a = el('a', null, 'Voir les formules'); a.href = 'commander.html'; a.setAttribute('data-goatcounter-click', 'comparateur/clic-commander'); p.appendChild(a);
    cta.appendChild(p); box.appendChild(cta);
    out.innerHTML = ''; out.appendChild(box); box.scrollIntoView({behavior: 'smooth', block: 'start'});
  }, function(m){ err(typeof m === 'string' ? m : 'Connexion impossible. Vérifiez votre connexion internet et réessayez.'); gc('erreur-lecture'); })
  .catch(function(){ err('Connexion impossible. Vérifiez votre connexion internet et réessayez.'); gc('erreur-reseau'); })
  .then(function(){ go.disabled = false; go.textContent = 'Comparer les deux devis'; if (SITEKEY && window.turnstile && wid !== null) turnstile.reset(wid); });
});
})();
</script>"""

EXPLAIN = """<h2>Ce que fait le comparateur</h2>
<p>Il met vos deux devis côte à côte : totaux, TVA, acompte, délai, durée de validité, puis chaque poste de travaux. Il repère ce qui figure dans un devis et pas dans l'autre, les quantités différentes pour le même ouvrage et les postes compris dans un forfait sans détail. Il vous donne ensuite les questions à poser à chaque entreprise pour comparer à égalité.</p>
<h2>Ce qu'il ne fait pas</h2>
<ul><li>Il ne vous dit pas quel devis choisir et ne juge pas les prix : sans connaître votre chantier ni votre région, ce serait deviner.</li>
<li>Il ne repère pas les oublis communs aux deux devis : si aucun ne prévoit l'étanchéité sous la douche, le tableau ne le montrera pas.</li></ul>
<p>Vous préférez remplir vous-même un tableau ? Utilisez <a href="comparer-ses-devis.html">le tableau comparatif à imprimer</a>. Pour vérifier les mentions d'un seul devis, voyez <a href="verifier-mentions-devis.html">le contrôle des mentions</a>.</p>"""


def body():
    ts = '<div id="cmp-ts"></div>' if DEC.TURNSTILE_SITEKEY else ""
    tsjs = ('<script src="https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit&onload=cmpTurnstile" async defer></script>' if DEC.TURNSTILE_SITEKEY else "")
    return DEC.CSS + CSS + FORM.replace("{turnstile}", ts) + JS.replace("__URL__", json.dumps(DEC.DECODEUR_URL)).replace("__SITEKEY__", json.dumps(DEC.TURNSTILE_SITEKEY)) + tsjs + EXPLAIN
