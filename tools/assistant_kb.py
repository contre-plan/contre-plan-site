# Génère assistant-kb.txt : la base de connaissances lue par l'assistant Claude du site
# (route /question du relais Cloudflare). Elle reprend les réponses de chat.js (tarifs, délais,
# fonctionnement…) et la liste des pages publiques du site avec leur description.
# Appelé à la fin de tools/build.py. Ne rien écrire à la main dans assistant-kb.txt.
import html, json, os, re, shutil, subprocess

EXCLUS = {"404.html", "merci.html", "commande-confirmee.html", "avis.html"}


def _faq(root):
    src = open(os.path.join(root, "chat.js"), encoding="utf-8").read()
    a = src.index("var COMEUP")
    b = src.index("\n  ];", src.index("var KB = ["))
    code = src[a:b + 5] + "\nprocess.stdout.write(JSON.stringify(KB.map(e => ({q: e.q, a: e.a, l: (e.l || []).concat(e.l2 || [])}))));"
    node = shutil.which("node")
    if not node:
        return None
    out = subprocess.run([node, "-e", code], capture_output=True, text=True, timeout=30)
    if out.returncode != 0:
        return None
    return json.loads(out.stdout)


def _pages(root):
    pages = []
    for f in sorted(os.listdir(root)):
        if not f.endswith(".html") or f in EXCLUS:
            continue
        s = open(os.path.join(root, f), encoding="utf-8").read()
        t = re.search(r"<title>(.*?)</title>", s, re.S)
        d = re.search(r'<meta name="description" content="(.*?)"', s, re.S)
        url = "https://contre-plan.com/" + ("" if f == "index.html" else f)
        pages.append((url, html.unescape(t.group(1).strip()) if t else f, html.unescape(d.group(1).strip()) if d else ""))
    return pages


def build(root):
    faq = _faq(root)
    out = os.path.join(root, "assistant-kb.txt")
    if faq is None:
        print("assistant-kb.txt : node introuvable ou chat.js illisible, fichier inchangé")
        return
    lignes = ["# Contre-Plan : base de connaissances de l'assistant du site", "",
              "Service : un ingénieur BTP relit à distance les devis de travaux des particuliers en France avant signature et livre un rapport PDF sous 48 h. Commande et paiement par carte sur https://contre-plan.com/commander.html (aussi possible sur ComeUp). Pré-diagnostic gratuit : https://contre-plan.com/contact.html?sujet=prediagnostic . Contact : https://contre-plan.com/contact.html (réponse sous 24 h).",
              "Outils gratuits : décodeur de ligne de devis https://contre-plan.com/decodeur-ligne-devis.html ; contrôle des mentions d'un devis https://contre-plan.com/verifier-mentions-devis.html ; comparateur de deux devis https://contre-plan.com/comparer-deux-devis.html .",
              "", "## Questions fréquentes (réponses à reprendre fidèlement)"]
    for e in faq:
        liens = e["l"]
        lien_txt = " ; ".join(f"{liens[i + 1]} : {liens[i]}" for i in range(0, len(liens) - 1, 2)) if liens else ""
        lignes.append(f"Q : {e['q']}\nR : {e['a']}" + (f"\nLiens : {lien_txt}" if lien_txt else ""))
    lignes += ["", "## Pages du site (adresse, titre, description)"]
    for url, t, d in _pages(root):
        lignes.append(f"{url} | {t} | {d}")
    open(out, "w", encoding="utf-8").write("\n".join(lignes) + "\n")


if __name__ == "__main__":
    build(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
