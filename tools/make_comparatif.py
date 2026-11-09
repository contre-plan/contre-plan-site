"""Génère tableau-comparatif-devis.xlsx et tableau-comparatif-devis.pdf (modèles gratuits)."""
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule, CellIsRule
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAVY, ORANGE, BEIGE, INPUT = "14284B", "C44C19", "F3F0E8", "FFF6D6"
F = lambda **k: Font(name="Arial", **k)
thin = Side(style="thin", color="DDD8CA")
B = Border(left=thin, right=thin, top=thin, bottom=thin)
EUR = '#,##0.00 €;-#,##0.00 €;""'
PCT = '0.0 %'

def build(ws, example=None):
    ws.sheet_view.showGridLines = False
    for col, w in zip("ABCDE", (42, 20, 20, 20, 38)): ws.column_dimensions[col].width = w
    ws["A1"] = "Contre-Plan · Tableau comparatif de devis"; ws["A1"].font = F(bold=True, size=15, color=NAVY)
    ws["A2"] = "Remplissez les cases jaunes. Les totaux, la TVA, l'acompte et les écarts se calculent seuls." + ("  (Feuille d'exemple fictif)" if example else "")
    ws["A2"].font = F(italic=True, size=9, color="5B6784")
    ws["A3"] = "Une case de montant vide sur un poste = un poste absent du devis, à faire chiffrer (elle apparaît en orange)."
    ws["A3"].font = F(italic=True, size=9, color="5B6784")
    def head(r, text):
        ws.cell(r, 1, text).font = F(bold=True, color="FFFFFF")
        for c in range(1, 6):
            ws.cell(r, c).fill = PatternFill("solid", fgColor=NAVY); ws.cell(r, c).border = B
    def lab(r, text, bold=False):
        c = ws.cell(r, 1, text); c.font = F(bold=bold, color=NAVY); c.border = B; c.alignment = Alignment(wrap_text=True, vertical="center")
        ws.cell(r, 5).border = B; ws.cell(r, 5).fill = PatternFill("solid", fgColor=INPUT); ws.cell(r, 5).font = F(size=9)
    def inp(r, fmt=None):
        for c in (2, 3, 4):
            x = ws.cell(r, c); x.fill = PatternFill("solid", fgColor=INPUT); x.border = B; x.font = F(color="0000FF")
            x.alignment = Alignment(horizontal="center")
            if fmt: x.number_format = fmt
    def frm(r, f, fmt=EUR, bold=False):
        for i, c in enumerate("BCD"):
            x = ws[f"{c}{r}"]; x.value = f.replace("#", c); x.number_format = fmt; x.border = B
            x.font = F(bold=bold, color="000000"); x.fill = PatternFill("solid", fgColor=BEIGE); x.alignment = Alignment(horizontal="center")
    head(5, "Élément"); [ws.cell(5, i + 2, t) for i, t in enumerate(["Artisan 1", "Artisan 2", "Artisan 3", "Remarques"])]
    for c in range(2, 6): ws.cell(5, c).font = F(bold=True, color="FFFFFF"); ws.cell(5, c).alignment = Alignment(horizontal="center")
    rows_info = [(6, "Nom de l'entreprise", None), (7, "Date du devis", "dd/mm/yyyy"), (8, "Validité du devis", None),
                 (9, "SIRET et immatriculation vérifiés (annuaire-entreprises.data.gouv.fr)", None),
                 (10, "Attestation d'assurance décennale reçue", None), (11, "Qualification RGE (si vous visez des aides)", None)]
    for r, t, fmt in rows_info: lab(r, t); inp(r, fmt)
    head(13, "Postes : montants HT en €  (mettez les postes comparables sur la même ligne)")
    for r in range(14, 29):
        lab(r, ""); ws.cell(r, 1).fill = PatternFill("solid", fgColor=INPUT); ws.cell(r, 1).font = F(color="0000FF"); inp(r, EUR)
    lab(29, "Total HT", True); frm(29, "=SUM(#14:#28)", bold=True)
    lab(30, "Taux de TVA appliqué"); inp(30, PCT)
    lab(31, "TVA"); frm(31, "=#29*#30")
    lab(32, "Total TTC", True); frm(32, "=#29+#31", bold=True)
    lab(33, "Écart avec le devis le moins cher (TTC)"); frm(33, '=IF(#29=0,"",#32-_xlfn.MINIFS($B$32:$D$32,$B$29:$D$29,">0"))')
    lab(34, "Nombre de postes non chiffrés"); frm(34, '=SUMPRODUCT(($A$14:$A$28<>"")*(#14:#28=""))', fmt="0")
    head(36, "Conditions")
    lab(37, "Acompte demandé à la signature (%)"); inp(37, PCT)
    lab(38, "Acompte en €"); frm(38, "=#32*#37")
    lab(39, "Paiements liés à l'avancement des travaux"); inp(39)
    lab(40, "Date de début des travaux"); inp(40, "dd/mm/yyyy")
    lab(41, "Délai d'exécution ferme indiqué"); inp(41)
    lab(42, "Gestion des déchets chiffrée"); inp(42)
    lab(43, "Marques et références des matériaux indiquées"); inp(43)
    head(45, "Points à faire préciser par écrit")
    for r in (46, 47, 48): lab(r, ""); ws.cell(r, 1).fill = PatternFill("solid", fgColor=INPUT); inp(r); [setattr(ws.cell(r, c), "alignment", Alignment(wrap_text=True)) for c in (2, 3, 4)]
    ws["A50"] = "Repères : l'usage est d'environ 30 % d'acompte à la signature. Le taux de TVA dépend des travaux et de l'âge du logement (5,5 %, 10 % ou 20 %)."
    ws["A50"].font = F(italic=True, size=9, color="5B6784")
    ws["A51"] = "Un avis d'ingénieur BTP sur vos devis : contre-plan.com (formules « 2 ou 3 devis comparés »)."
    ws["A51"].font = F(bold=True, size=10, color=ORANGE); ws["A51"].hyperlink = "https://contre-plan.com/"
    dv = DataValidation(type="list", formula1='"Oui,Non,Sans objet"', allow_blank=True); ws.add_data_validation(dv)
    for r in (9, 10, 11, 39, 41, 42, 43): dv.add(f"B{r}:D{r}")
    ws.conditional_formatting.add("B14:D28", FormulaRule(formula=['AND($A14<>"",B14="")'], fill=PatternFill("solid", fgColor="F9DCCB")))
    ws.conditional_formatting.add("B6:D43", CellIsRule(operator="equal", formula=['"Non"'], fill=PatternFill("solid", fgColor="FBEBEB"), font=Font(name="Arial", color="B3261E", bold=True)))
    ws.conditional_formatting.add("B37:D37", CellIsRule(operator="greaterThan", formula=["0.3"], fill=PatternFill("solid", fgColor="F9DCCB")))
    ws.freeze_panes = "B6"
    ws.page_setup.orientation = "landscape"; ws.page_setup.fitToWidth = 1; ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    if example:
        for (r, c), v in example.items(): ws.cell(r, c).value = v

wb = Workbook(); ws = wb.active; ws.title = "Comparatif"; build(ws)
ex = {(6,2):"Entreprise A",(6,3):"Entreprise B",(6,4):"Entreprise C",(8,2):"3 mois",(8,3):"1 mois",(8,4):"2 mois",
      (9,2):"Oui",(9,3):"Oui",(9,4):"Oui",(10,2):"Oui",(10,3):"Non",(10,4):"Oui",(11,2):"Sans objet",(11,3):"Sans objet",(11,4):"Sans objet",
      (14,1):"Dépose carrelage et sanitaires",(14,2):1700,(14,3):1250,(14,4):1400,
      (15,1):"Évacuation des gravats",(15,3):320,(15,4):280,
      (16,1):"Étanchéité sous carrelage",(16,2):540,(16,4):610,
      (17,1):"Receveur et paroi de douche",(17,2):1150,(17,3):980,(17,4):1240,
      (18,1):"Faïence et carrelage (fourniture et pose)",(18,2):1860,(18,3):1720,(18,4):1950,
      (19,1):"Plomberie",(19,2):1150,(19,3):900,(19,4):1300,
      (20,1):"Électricité et ventilation",(20,2):480,(20,3):520,(20,4):450,
      (30,2):0.1,(30,3):0.1,(30,4):0.1,(37,2):0.5,(37,3):0.3,(37,4):0.3,(39,2):"Non",(39,3):"Oui",(39,4):"Oui",
      (41,2):"Non",(41,3):"Oui",(41,4):"Oui",(42,2):"Non",(42,3):"Oui",(42,4):"Oui",(43,2):"Oui",(43,3):"Non",(43,4):"Oui",
      (46,1):"À demander",(46,2):"Chiffrer les gravats, acompte 30 %",(46,3):"Chiffrer l'étanchéité, attestation décennale",(46,4):"Rien d'essentiel"}
ws2 = wb.create_sheet("Exemple fictif"); build(ws2, ex)
ws3 = wb.create_sheet("Mode d'emploi"); ws3.sheet_view.showGridLines = False; ws3.column_dimensions["A"].width = 110
lines = ["Mode d'emploi du tableau comparatif Contre-Plan",
 "1. Inscrivez une ligne par poste, en regroupant les postes comparables (même travail, même surface).",
 "2. Reportez pour chaque artisan le montant HT du poste. Laissez vide si le poste n'apparaît pas sur son devis.",
 "3. Une case orange = un poste chiffré chez un artisan mais absent chez un autre : demandez-lui de le chiffrer avant de comparer.",
 "4. Renseignez le taux de TVA et l'acompte : les totaux TTC, l'acompte en € et l'écart avec le moins cher se calculent seuls.",
 "5. Un « Non » s'affiche en rouge : c'est un point à faire préciser par écrit.",
 "Le devis le moins cher n'est pas forcément le meilleur : comparez ce qui est inclus, les garanties et les conditions.",
 "Voir la feuille « Exemple fictif » pour un tableau rempli. Besoin d'un avis d'ingénieur ? contre-plan.com"]
for i, t in enumerate(lines, 1):
    ws3.cell(i * 2 - 1, 1, t).font = F(bold=(i == 1), size=13 if i == 1 else 11, color=NAVY)
wb.save(os.path.join(ROOT, "tableau-comparatif-devis.xlsx"))
print("xlsx ok")
