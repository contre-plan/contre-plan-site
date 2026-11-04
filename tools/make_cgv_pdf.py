"""Génère cgv-contre-plan.pdf à partir de cgv.html (pièce jointe de la confirmation de commande).
À relancer après chaque modification des CGV : python3 tools/make_cgv_pdf.py"""
import os
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = """header,footer,nav,.cp-hd,.cp-foot,.cp-crumbs,#cp-chat-btn,#cp-chat,#cp-bar,.cp-side,aside,.cp-cta-box{display:none!important}
body{background:#fff!important}.cp-ph{background:#fff!important;padding:0!important}.cp-ph *{color:#14284b!important}
.cp-wrap{display:block!important;padding:0!important;max-width:none!important}"""
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.goto('file://' + os.path.join(ROOT, 'cgv.html')); pg.wait_for_timeout(600)
    pg.add_style_tag(content=CSS); pg.emulate_media(media='print')
    pg.pdf(path=os.path.join(ROOT, 'cgv-contre-plan.pdf'), format='A4', print_background=True,
           margin={'top': '14mm', 'bottom': '16mm', 'left': '15mm', 'right': '15mm'}, display_header_footer=True,
           header_template='<span></span>',
           footer_template='<div style="width:100%;font-size:7px;color:#5b6784;padding:0 15mm;display:flex;justify-content:space-between;font-family:Arial"><span>Contre-Plan · conditions générales de vente · contre-plan.com/cgv.html</span><span><span class="pageNumber"></span>/<span class="totalPages"></span></span></div>')
    b.close()
print('ok')
