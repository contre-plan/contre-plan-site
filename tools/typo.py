"""Espaces insécables à la française dans le texte des pages (hors scripts, styles et attributs).
Idempotent : peut être relancé sans effet de bord."""
import re, sys, glob, os
NB = " "
def fix_text(t):
    t = re.sub(r"(?<=\S) ([?!:;»])", NB + r"\1", t)          # avant ? ! : ; »
    t = re.sub(r"(«) (?=\S)", r"\1" + NB, t)                  # après «
    t = re.sub(r"(\d) (%|€|h\b|min\b|m²|m\b|ans\b|jours\b)", r"\1" + NB + r"\2", t)  # unités
    t = re.sub(r"(\d) (\d{3})(?!\d)", r"\1" + NB + r"\2", t)  # milliers : 1 000
    t = re.sub(r"([+−-]) (?=\d)", r"\1" + NB, t)             # + 11 €, − 450 €
    return t
def fix_html(s):
    out, pos = [], 0
    prev = ""
    for m in re.finditer(r"<script\b.*?</script>|<style\b.*?</style>|<[^>]+>", s, re.S):
        seg = fix_text(s[pos:m.start()])
        if re.match(r"</(strong|b|a|em|i|span|sup)>$", prev):   # « </strong> : » → espace insécable
            seg = re.sub(r"^ (?=[?!:;»])", NB, seg)
        out.append(seg); out.append(m.group(0)); prev = m.group(0); pos = m.end()
    out.append(fix_text(s[pos:]))
    return "".join(out)
if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    n = 0
    for f in glob.glob(os.path.join(root, "*.html")):
        s = open(f, encoding="utf-8").read(); t = fix_html(s)
        if t != s: open(f, "w", encoding="utf-8").write(t); n += 1
    print("typo", n, "fichiers")
