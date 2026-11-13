"""Changer un prix (ou une mention) partout sur le site en une seule fois.

Usage :
  python3 tools/changer_prix.py "16,50 €" "39 €"                 # aperçu (rien n'est modifié)
  python3 tools/changer_prix.py "16,50 €" "39 €" --appliquer     # modifie puis reconstruit le site
  python3 tools/changer_prix.py "au tarif de lancement" "" --appliquer

Fichiers traités : index.html, site.js (écrits à la main) et les constantes
PRIX_TXT / PRIX_MENTION de tools/build.py (pages générées). Les espaces insécables sont gérés.
Pensez aussi à : l'annonce ComeUp, les CGV si le mode de paiement change, l'exemple de calcul des commandes.
"""
import os, re, sys, subprocess
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FICHIERS = ["index.html", "site.js", "tools/build.py"]

def motif(t):
    return re.escape(t).replace(r"\ ", "[   ]")

def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    ancien, nouveau, appliquer = sys.argv[1], sys.argv[2], "--appliquer" in sys.argv
    total = 0
    for f in FICHIERS:
        p = os.path.join(ROOT, f); s = open(p, encoding="utf-8").read()
        n = len(re.findall(motif(ancien), s)); total += n
        print(f"{f}: {n} occurrence(s)")
        if appliquer and n:
            open(p, "w", encoding="utf-8").write(re.sub(motif(ancien), lambda m: nouveau, s))
    print(f"Total : {total}")
    if appliquer and total:
        subprocess.run([sys.executable, os.path.join(ROOT, "tools", "build.py")], check=True)
        print("Site reconstruit. Vérifiez puis poussez sur une branche.")
    elif not appliquer:
        print("Aperçu seulement : ajoutez --appliquer pour modifier.")

if __name__ == "__main__":
    main()
