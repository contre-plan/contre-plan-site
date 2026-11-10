"""Génère exemple-rapport-contre-plan.pdf à partir de tools/exemple-rapport.html."""
import os
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.goto('file://' + os.path.join(ROOT, 'tools', 'exemple-rapport.html')); pg.wait_for_timeout(500)
    pg.pdf(path=os.path.join(ROOT, 'exemple-rapport-contre-plan.pdf'), format='A4', print_background=True,
           margin={'top': '14mm', 'bottom': '16mm', 'left': '15mm', 'right': '15mm'}, display_header_footer=True,
           header_template='<span></span>',
           footer_template='<div style="width:100%;font-size:7px;color:#8d9cc0;padding:0 15mm;display:flex;justify-content:space-between;font-family:Arial"><span>Contre-Plan · contre-plan.com · EXEMPLE : devis créé pour illustrer le format du rapport</span><span><span class="pageNumber"></span>/<span class="totalPages"></span></span></div>')
    b.close()
print('ok')
