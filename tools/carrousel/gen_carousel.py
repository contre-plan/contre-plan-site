import json,sys,html,os,glob,subprocess,tarfile,shutil,random,math,base64,re
from playwright.sync_api import sync_playwright
spec=json.load(open(sys.argv[1])); out=sys.argv[2]
W,H=1080,1920
E=html.escape
FD=os.path.abspath('fonts')
if not glob.glob(FD+'/archivo-latin-800-normal.woff2'):
    os.makedirs(FD,exist_ok=True); tmp=os.path.abspath('_fonts_tmp'); os.makedirs(tmp,exist_ok=True)
    try:
        subprocess.run(['npm','pack','@fontsource/archivo','@fontsource/source-sans-3','@fontsource/caveat','--silent'],cwd=tmp,check=True,timeout=180)
        for t in glob.glob(tmp+'/*.tgz'):
            with tarfile.open(t) as z:
                for m in z.getmembers():
                    b=os.path.basename(m.name)
                    if b.endswith('-normal.woff2') and '-latin-' in b and '-ext-' not in b:
                        with open(os.path.join(FD,b),'wb') as f: f.write(z.extractfile(m).read())
    except Exception as e: print('polices indisponibles, repli sur Liberation Sans :',e)
    shutil.rmtree(tmp,ignore_errors=True)
def ff(fam,file,w):
    p=os.path.join(FD,file)
    if not os.path.exists(p): return ''
    return "@font-face{font-family:'"+fam+"';font-weight:"+str(w)+";src:url(data:font/woff2;base64,"+base64.b64encode(open(p,'rb').read()).decode()+") format('woff2')}"
FONTS=''.join([ff('Archivo','archivo-latin-800-normal.woff2',800),ff('Archivo','archivo-latin-700-normal.woff2',700),
  ff('Source Sans 3','source-sans-3-latin-400-normal.woff2',400),ff('Source Sans 3','source-sans-3-latin-600-normal.woff2',600),ff('Source Sans 3','source-sans-3-latin-700-normal.woff2',700),
  ff('Caveat','caveat-latin-700-normal.woff2',700)])
NAVY='#0f2747'; INK='#14284b'; OR='#ff6b35'; ORD='#c2410c'; PEN='#d62839'
def svgurl(s): return 'url("data:image/svg+xml;utf8,'+s.replace('#','%23')+'")'
FIBER=svgurl("<svg xmlns='http://www.w3.org/2000/svg' width='420' height='420'><filter id='f' x='0' y='0' width='1' height='1'><feTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='4' stitchTiles='stitch'/><feDiffuseLighting lighting-color='#fff' surfaceScale='1.7' diffuseConstant='1.05'><feDistantLight azimuth='225' elevation='52'/></feDiffuseLighting></filter><rect width='420' height='420' filter='url(#f)'/></svg>")
BLOTCH=svgurl("<svg xmlns='http://www.w3.org/2000/svg' width='1080' height='1920'><filter id='b'><feTurbulence type='fractalNoise' baseFrequency='.004' numOctaves='3' seed='7'/><feColorMatrix values='0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  1.6 0 0 0 -.55'/></filter><rect width='1080' height='1920' filter='url(#b)'/></svg>")
INKMASK=svgurl("<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='m'><feTurbulence type='fractalNoise' baseFrequency='.55' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  -3 0 0 0 2.75'/></filter><rect width='300' height='300' filter='url(#m)'/></svg>")
def hand_ellipse(seed,passes=2):
    r=random.Random(seed); d=''
    for k in range(passes):
        a0=r.uniform(-0.6,0.2); pts=[]
        for j in range(46):
            a=a0+j*(2*math.pi*1.08)/45
            rx=49+r.uniform(-1.6,1.6); ry=18.5+r.uniform(-1.2,1.2)
            pts.append((50+rx*math.cos(a),20+ry*math.sin(a)))
        d+='M'+' L'.join(f'{x:.1f} {y:.1f}' for x,y in pts)+' '
    return f"<svg class='hand' viewBox='0 0 100 40' preserveAspectRatio='none'><path d='{d}' fill='none' stroke='{PEN}' stroke-width='5.5' stroke-linecap='round' stroke-linejoin='round' vector-effect='non-scaling-stroke' opacity='.9'/></svg>"
PENSVG="""<svg class='pen' viewBox='0 0 660 70'><defs>
<linearGradient id='pb' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#6e0b16'/><stop offset='.16' stop-color='#c41f2f'/><stop offset='.3' stop-color='#ff9aa2'/><stop offset='.4' stop-color='#e0303f'/><stop offset='.78' stop-color='#9a1422'/><stop offset='1' stop-color='#4f0810'/></linearGradient>
<linearGradient id='pc' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#3a3f47'/><stop offset='.3' stop-color='#d9dee5'/><stop offset='.45' stop-color='#9aa1ab'/><stop offset='1' stop-color='#2c3036'/></linearGradient>
<linearGradient id='pk' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#4a0710'/><stop offset='.25' stop-color='#b51b2a'/><stop offset='.38' stop-color='#ff7f8a'/><stop offset='.5' stop-color='#c9202f'/><stop offset='1' stop-color='#3d050c'/></linearGradient></defs>
<path d='M4 35 L 30 27 L 30 43 Z' fill='#8e0f1c'/><path d='M30 24 L 78 13 L 78 57 L 30 46 Z' fill='url(#pc)'/>
<rect x='76' y='12' width='400' height='46' rx='8' fill='url(#pb)'/><rect x='96' y='12' width='6' height='46' fill='rgba(0,0,0,.18)'/><rect x='110' y='12' width='6' height='46' fill='rgba(0,0,0,.18)'/>
<text x='200' y='42' font-family='Archivo,sans-serif' font-weight='800' font-size='20' fill='rgba(255,255,255,.55)' letter-spacing='5'>MARKER · FINE</text>
<rect x='470' y='7' width='186' height='56' rx='16' fill='url(#pk)'/><rect x='500' y='0' width='140' height='13' rx='6' fill='url(#pc)'/><rect x='470' y='7' width='10' height='56' fill='rgba(0,0,0,.25)'/></svg>"""
CHK="<svg class='tick' viewBox='0 0 60 50'><path d='M5 27 C 12 31, 17 37, 22 45 C 30 28, 41 14, 56 4' fill='none' stroke='"+PEN+"' stroke-width='7' stroke-linecap='round' stroke-linejoin='round'/></svg>"
def plan(col):
    return f"""<svg class='plan' viewBox='0 0 700 900'><g fill='none' stroke='{col}' stroke-width='10' stroke-linecap='square'>
<path d='M40 40 H 660 V 860 H 40 Z'/><path d='M40 420 H 330 M 420 420 H 660 M 360 40 V 300 M 360 380 V 420 M 360 520 V 860'/></g>
<g fill='none' stroke='{col}' stroke-width='4'><path d='M330 420 A 90 90 0 0 1 420 330' /><path d='M360 300 A 80 80 0 0 0 440 380'/><rect x='470' y='600' width='150' height='220'/><circle cx='545' cy='650' r='26'/><rect x='80' y='470' width='240' height='130'/><path d='M80 760 H 300 V 820 H 80 Z'/></g>
<g stroke='{col}' stroke-width='3' fill='{col}' font-family='Archivo, sans-serif' font-weight='700' font-size='34'>
<path d='M40 -10 V 20 M 360 -10 V 20 M 660 -10 V 20 M 40 5 H 660'/><text x='160' y='-18' stroke='none'>4,20</text><text x='470' y='-18' stroke='none'>3,60</text>
<path d='M690 40 H 720 M 690 420 H 720 M 690 860 H 720 M 705 40 V 860'/><text x='730' y='250' stroke='none'>4,10</text><text x='730' y='660' stroke='none'>4,80</text></g></svg>"""
ZIG="polygon(0 0,100% 0,100% 100%,0 100%,3% 88%,0 76%,3% 64%,0 52%,3% 40%,0 28%,3% 16%)"
CSS=FONTS+"""
*{box-sizing:border-box;margin:0;padding:0}
body{width:%W%px;height:%H%px;overflow:hidden;background:#000}
.s{position:relative;width:%W%px;height:%H%px;overflow:hidden;font-family:'Source Sans 3','Liberation Sans',Arial,sans-serif}
.s>.L{position:absolute;inset:0;pointer-events:none}
.dark{background:radial-gradient(ellipse at 28% 16%,#28528f,#14325f 46%,#081830 100%);color:#fff}
.dark .grid{background-image:linear-gradient(rgba(170,200,255,.16) 2px,transparent 2px),linear-gradient(90deg,rgba(170,200,255,.16) 2px,transparent 2px),linear-gradient(rgba(170,200,255,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(170,200,255,.06) 1px,transparent 1px);background-size:216px 216px,216px 216px,43.2px 43.2px,43.2px 43.2px}
.dark .fib{background:%FIBER%;background-size:420px;mix-blend-mode:overlay;opacity:.55}
.light{background:radial-gradient(ellipse at 28% 14%,#ffffff,#eef0f3 50%,#d9dde3 100%);color:%INK%}
.light .grid{background-image:linear-gradient(rgba(40,90,170,.12) 1px,transparent 1px),linear-gradient(90deg,rgba(40,90,170,.12) 1px,transparent 1px),linear-gradient(rgba(40,90,170,.2) 2px,transparent 2px),linear-gradient(90deg,rgba(40,90,170,.2) 2px,transparent 2px);background-size:43.2px 43.2px,43.2px 43.2px,216px 216px,216px 216px}
.light .fib{background:%FIBER%;background-size:420px;mix-blend-mode:multiply;opacity:.42}
.blot{background:%BLOTCH%;mix-blend-mode:soft-light;opacity:.45}
.crease{background:linear-gradient(90deg,transparent calc(50% - 46px),rgba(0,0,0,.16) calc(50% - 2px),rgba(255,255,255,.2) 50%,rgba(255,255,255,0) calc(50% + 56px)),linear-gradient(180deg,transparent calc(33.3% - 40px),rgba(0,0,0,.14) calc(33.3% - 2px),rgba(255,255,255,.18) 33.3%,rgba(255,255,255,0) calc(33.3% + 50px)),linear-gradient(180deg,transparent calc(66.6% - 40px),rgba(0,0,0,.14) calc(66.6% - 2px),rgba(255,255,255,.18) 66.6%,rgba(255,255,255,0) calc(66.6% + 50px)),linear-gradient(90deg,rgba(255,255,255,.04),rgba(0,0,0,.07) 50%,rgba(255,255,255,.05) 50%,rgba(0,0,0,.05))}
.light .crease{opacity:.6}
.vig{background:radial-gradient(ellipse at 45% 38%,transparent 52%,rgba(0,0,0,.42) 100%)}
.light .vig{background:radial-gradient(ellipse at 45% 38%,transparent 55%,rgba(30,40,60,.22) 100%)}
.plan{position:absolute;z-index:1;width:820px;right:-150px;bottom:-80px;transform:rotate(-8deg);opacity:.15}
.light .plan{opacity:.07}
.in{position:absolute;left:84px;right:110px;top:240px;bottom:500px;z-index:4;display:flex;flex-direction:column;justify-content:center}
.in.hk{justify-content:flex-start;top:250px}
.top{position:absolute;top:118px;left:84px;right:84px;z-index:5;display:flex;justify-content:space-between;align-items:center;font-family:Archivo,'Liberation Sans',sans-serif;font-weight:800;font-size:30px;letter-spacing:4px}
.top .n{font-family:'Source Sans 3',sans-serif;font-weight:700;letter-spacing:1px;font-size:28px;padding:6px 16px;border-radius:30px}
.dark .top{color:#fff;text-shadow:0 2px 6px rgba(0,0,0,.4)} .dark .top .n{background:rgba(255,255,255,.14)} .light .top{color:%INK%} .light .top .n{background:rgba(20,40,75,.08)}
.top .lg{display:flex;align-items:center;gap:14px} .top .lg i{width:30px;height:30px;border:4px solid currentColor;border-radius:4px;position:relative} .top .lg i::after{content:'';position:absolute;inset:6px;background:%OR%;border-radius:50%}
.kick{align-self:flex-start;font-family:Archivo,sans-serif;font-weight:800;font-size:32px;letter-spacing:5px;text-transform:uppercase;padding:14px 26px 12px;border-radius:5px;margin-bottom:42px;transform:rotate(-1.6deg);color:#fff;text-shadow:0 -1px 0 rgba(0,0,0,.35),0 2px 0 rgba(255,255,255,.35);box-shadow:0 2px 0 rgba(0,0,0,.25),0 10px 18px rgba(0,0,0,.35),inset 0 2px 0 rgba(255,255,255,.28),inset 0 -3px 0 rgba(0,0,0,.18)}
.dark .kick{background:linear-gradient(180deg,#ff8650,#f0581f 55%,#d8480f)} .light .kick{background:linear-gradient(180deg,#2b4675,#14284b 60%,#0b1a33)}
.t{font-family:Archivo,'Liberation Sans',sans-serif;font-weight:800;line-height:1.0;letter-spacing:-2px;text-wrap:balance}
.t1{font-size:118px} .t2{font-size:96px} .t3{font-size:72px}
.dark .t{text-shadow:0 3px 0 rgba(0,0,0,.18),0 10px 28px rgba(0,0,0,.35)}
.mk{position:relative;white-space:nowrap;z-index:0}
.dark .mk{color:%OR%;text-shadow:0 1px 0 #d9541f,0 2px 0 #c74a18,0 3px 0 #b54114,0 4px 0 #a33a11,0 5px 0 #8f320e,0 14px 24px rgba(0,0,0,.45)}
.light .mk::before{content:'';position:absolute;left:-12px;right:-12px;bottom:2px;height:46%;background:rgba(255,120,60,.55);mix-blend-mode:multiply;z-index:-1;transform:skew(-8deg) rotate(-1deg);border-radius:4px 16px 6px 14px}
.p{font-size:52px;line-height:1.3;margin-top:40px;text-wrap:pretty} .dark .p{color:#dbe3f3;text-shadow:0 2px 10px rgba(0,0,0,.35)} .light .p{color:#33415f}
.p b{font-weight:700} .dark .p b{color:#fff} .light .p b{color:%INK%}
.dwrap{position:relative;margin-top:90px;perspective:1700px}
.tilt{position:relative;transform:rotateX(10deg) rotateZ(-2.2deg);transform-origin:50% 100%;transform-style:preserve-3d}
.lift{position:absolute;bottom:16px;width:46%;height:40px;z-index:0;box-shadow:0 30px 26px rgba(0,0,0,.55)}
.lift.l{left:14px;transform:rotate(-3.5deg)} .lift.r{right:14px;transform:rotate(3.5deg)}
.light .lift{box-shadow:0 30px 26px rgba(20,30,50,.35)}
.doc{position:relative;z-index:1;background:linear-gradient(172deg,#ffffff,#f6f4ee 55%,#ebe7dd);color:%INK%;border-radius:3px;padding:44px 44px 34px;box-shadow:0 1px 1px rgba(0,0,0,.3),0 8px 14px rgba(0,0,0,.28),0 40px 70px rgba(0,0,0,.35)}
.doc::before{content:'';position:absolute;inset:0;background:%FIBER%;background-size:420px;mix-blend-mode:multiply;opacity:.38;pointer-events:none}
.doc::after{content:'';position:absolute;inset:0;background:linear-gradient(118deg,rgba(255,255,255,.55),rgba(255,255,255,0) 38%,rgba(0,0,0,0) 70%,rgba(0,0,0,.07));pointer-events:none}
.light .doc{box-shadow:0 1px 1px rgba(20,30,50,.25),0 8px 14px rgba(20,30,50,.16),0 40px 70px rgba(20,30,50,.22)}
.scotch{position:absolute;z-index:3;width:200px;height:60px;background:linear-gradient(180deg,rgba(255,253,240,.62),rgba(240,236,220,.5));clip-path:%ZIG%;box-shadow:0 1px 3px rgba(0,0,0,.12)}
.scotch::before{content:'';position:absolute;inset:0;background:%FIBER%;background-size:300px;mix-blend-mode:multiply;opacity:.25}
.scotch.a{left:-48px;top:-18px;transform:rotate(-38deg)} .scotch.b{right:-48px;top:-18px;transform:rotate(36deg) scaleX(-1)}
.doc .dh{display:flex;justify-content:space-between;align-items:baseline;border-bottom:4px solid %INK%;padding-bottom:14px;margin-bottom:6px;position:relative}
.doc .dh b{font-family:Archivo,sans-serif;font-weight:800;font-size:46px;letter-spacing:7px} .doc .dh span{font-size:26px;color:#6b778f}
.doc .r{display:grid;grid-template-columns:1fr 104px 222px;gap:14px;font-size:38px;padding:19px 0;border-bottom:2px dashed #d8dde4;position:relative}
.doc .r span:not(:first-child){text-align:right} .doc .r.hd{font-size:23px;font-weight:700;color:#6b778f;letter-spacing:1px;text-transform:uppercase;padding:10px 0;border-bottom-style:solid}
.doc .r.on{background:linear-gradient(90deg,rgba(255,224,90,.0),rgba(255,224,90,.45) 4%,rgba(255,224,90,.4) 96%,rgba(255,224,90,0))} .doc .r.on span:last-child{font-weight:700} .doc .r.dim{opacity:.55}
.doc .ft{position:relative;font-size:24px;color:#8a93a6;margin-top:16px}
.hand{position:absolute;overflow:visible}
.r .hand.amt{right:-24px;top:-12px;width:244px;height:calc(100% + 24px)} .r .hand.line{left:-36px;top:-12px;width:calc(100% + 64px);height:calc(100% + 24px)}
.postit{position:absolute;z-index:6;right:-6px;top:-118px;width:300px;padding:34px 24px 40px;background:linear-gradient(176deg,#fff07a,#ffe04f 55%,#f4cd34);color:%PEN%;font-family:Caveat,cursive;font-weight:700;font-size:66px;line-height:.95;text-align:center;transform:rotate(6deg);filter:drop-shadow(0 3px 2px rgba(0,0,0,.25)) drop-shadow(0 26px 18px rgba(0,0,0,.4))}
.postit::before{content:'';position:absolute;inset:0;background:%FIBER%;background-size:300px;mix-blend-mode:multiply;opacity:.3}
.postit::after{content:'';position:absolute;left:0;right:0;bottom:0;height:46%;background:linear-gradient(to top,rgba(150,100,0,.22),rgba(255,255,255,.12) 40%,transparent)}
.postit span{position:relative;z-index:1}
.stamp{position:absolute;z-index:5;font-family:Archivo,sans-serif;font-weight:800;font-size:36px;letter-spacing:5px;color:%PEN%;border:6px solid %PEN%;border-radius:9px;padding:6px 18px;transform:rotate(-5deg);opacity:.9;-webkit-mask-image:%INKMASK%;mask-image:%INKMASK%;-webkit-mask-size:300px;mask-size:300px;mix-blend-mode:multiply}
.pen{position:absolute;z-index:4;width:640px;filter:drop-shadow(4px 6px 3px rgba(0,0,0,.35)) drop-shadow(22px 30px 18px rgba(0,0,0,.45))}
.big{font-family:Archivo,sans-serif;font-weight:800;font-size:250px;line-height:.9;letter-spacing:-8px}
.dark .big{color:%OR%;text-shadow:0 2px 0 #e05a24,0 4px 0 #cc4e1c,0 6px 0 #b84517,0 8px 0 #a33c13,0 10px 0 #8c330f,0 12px 0 #762b0c,0 30px 40px rgba(0,0,0,.5)}
.light .big{color:%ORD%}
.bigl{font-size:46px;font-weight:600;margin-top:26px} .dark .bigl{color:#c3cee4} .light .bigl{color:#4a5b7e}
.bars{margin-top:70px;display:flex;flex-direction:column;gap:42px}
.bar .bl{display:flex;justify-content:space-between;font-size:42px;font-weight:700;margin-bottom:14px}
.bar .bt{height:70px;border-radius:4px;border:3px dashed rgba(190,210,255,.35);position:relative} .light .bar .bt{border-color:rgba(20,40,75,.25)}
.bar .bf{position:absolute;left:-6px;top:4px;bottom:4px;background:linear-gradient(180deg,#f3e7c9,#e2d3ad);clip-path:polygon(0 0,calc(100% - 8px) 0,100% 18%,calc(100% - 7px) 36%,100% 55%,calc(100% - 8px) 74%,100% 90%,calc(100% - 5px) 100%,0 100%);filter:drop-shadow(0 6px 5px rgba(0,0,0,.4));transform:rotate(-.6deg)}
.bar .bf::before{content:'';position:absolute;inset:0;background:%FIBER%;background-size:300px;mix-blend-mode:multiply;opacity:.35}
.bar.hot .bf{background:linear-gradient(180deg,#ff8a52,#f05d22);transform:rotate(.5deg)}
.card{position:relative;background:linear-gradient(175deg,#fffefa,#f7f3e8);border-radius:4px;padding:56px 46px 50px 130px;transform:rotate(-1.2deg);box-shadow:0 1px 1px rgba(0,0,0,.25),0 10px 16px rgba(20,30,50,.18),0 40px 60px rgba(20,30,50,.2)}
.card::before{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent 102px,rgba(214,40,57,.55) 102px,rgba(214,40,57,.55) 105px,transparent 105px),repeating-linear-gradient(180deg,transparent 0,transparent 63px,rgba(60,110,190,.28) 63px,rgba(60,110,190,.28) 65px);background-position:0 0,0 30px}
.card::after{content:'';position:absolute;inset:0;background:%FIBER%;background-size:420px;mix-blend-mode:multiply;opacity:.3}
.card .scotch{left:50%;top:-28px;margin-left:-100px;transform:rotate(-3deg)}
.dark .card{background:linear-gradient(175deg,#fffefa,#f7f3e8);color:%INK%}
.it{position:relative;z-index:1;margin-top:44px} .it:first-child{margin-top:0}
.it .tick{position:absolute;left:-102px;top:-6px;width:76px}
.it b{display:block;font-family:Archivo,sans-serif;font-weight:800;font-size:52px;line-height:1.08;color:%INK%} .it span{display:block;font-size:40px;line-height:1.28;margin-top:8px;color:#4a5b7e}
.tr{margin-top:44px;padding:34px 38px;border-radius:6px;background:linear-gradient(175deg,#fffefa,#f5f1e6);box-shadow:0 10px 16px rgba(0,0,0,.18),0 30px 50px rgba(0,0,0,.25);position:relative}
.tr::before{content:'';position:absolute;inset:0;background:%FIBER%;background-size:420px;mix-blend-mode:multiply;opacity:.3}
.tr:nth-child(odd){transform:rotate(-1deg)} .tr:nth-child(even){transform:rotate(.8deg)}
.tr .q{position:relative;font-family:Caveat,cursive;font-weight:700;font-size:66px;color:%PEN%;line-height:1.02} .tr .a{position:relative;font-family:Archivo,sans-serif;font-weight:800;font-size:52px;line-height:1.1;margin-top:14px;color:%INK%}
.swipe{align-self:flex-end;margin-top:34px;z-index:3;display:flex;align-items:center;gap:18px;font-weight:700;font-size:38px;padding:22px 36px;border-radius:60px;background:linear-gradient(180deg,#ffffff,#e4e8ef);color:%NAVY%;box-shadow:0 2px 0 #b9c1cf,0 6px 0 #9aa4b6,0 18px 30px rgba(0,0,0,.4),inset 0 2px 0 #fff}
.light .swipe{background:linear-gradient(180deg,#2b4675,#14284b);color:#fff;box-shadow:0 6px 0 #0a1730,0 18px 30px rgba(20,30,50,.35),inset 0 2px 0 rgba(255,255,255,.2)}
.swipe svg{width:40px;height:40px}
.bm{width:120px;height:150px;margin-bottom:40px;filter:drop-shadow(0 4px 2px rgba(0,0,0,.3)) drop-shadow(0 18px 18px rgba(0,0,0,.4))}
.save{position:relative;display:flex;gap:26px;align-items:center;margin-top:52px;padding:32px 36px;border-radius:10px;font-size:44px;font-weight:700;line-height:1.2;background:linear-gradient(176deg,#ff8650,#f0581f);color:#1a0f08;transform:rotate(-1deg);box-shadow:0 2px 0 rgba(0,0,0,.2),0 14px 26px rgba(0,0,0,.4),inset 0 2px 0 rgba(255,255,255,.3)}
.save::before{content:'';position:absolute;inset:0;border-radius:10px;background:%FIBER%;background-size:300px;mix-blend-mode:multiply;opacity:.3}
.save svg,.save div{position:relative;flex:none} .save div{flex:1} .save svg{width:60px;height:60px}
.offer{margin-top:36px;font-size:42px;font-weight:700;color:%OR%;line-height:1.25} .light .offer{color:%ORD%}
.foot{position:absolute;left:84px;bottom:510px;z-index:5;font-size:30px;font-weight:600} .dark .foot{color:#a9b9d8} .light .foot{color:#6b778f}
.cote{position:absolute;z-index:3;height:0;border-top:3px solid}
.dark .cote{color:rgba(225,235,255,.6);border-color:rgba(225,235,255,.6)} .light .cote{color:rgba(20,40,75,.4);border-color:rgba(20,40,75,.4)}
.cote::before{content:'';position:absolute;left:0;right:0;top:-12px;height:22px;background-image:linear-gradient(90deg,currentColor 3px,transparent 3px);background-size:108px 22px;background-position:var(--o,0) 0}
.cote i{position:absolute;top:-26px;width:5px;height:50px;background:currentColor} .cote i.a{left:0} .cote i.b{right:0}
.cote span{position:absolute;top:-62px;font-family:Archivo,sans-serif;font-weight:700;font-size:28px;letter-spacing:3px}
.tape{position:absolute;z-index:3;left:-120px;right:-120px;height:110px;bottom:190px;transform:rotate(-6deg);background:repeating-linear-gradient(-45deg,#ffb020 0 54px,#17120c 54px 108px);box-shadow:0 6px 6px rgba(0,0,0,.35),0 24px 34px rgba(0,0,0,.45);display:flex;align-items:center;justify-content:center}
.tape::before{content:'';position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.22),transparent 6%,rgba(255,255,255,.18) 12%,transparent 19%,rgba(0,0,0,.2) 31%,transparent 38%,rgba(255,255,255,.16) 47%,transparent 55%,rgba(0,0,0,.22) 66%,transparent 74%,rgba(255,255,255,.15) 83%,transparent 90%,rgba(0,0,0,.2)),linear-gradient(180deg,rgba(255,255,255,.35),transparent 35%,transparent 70%,rgba(0,0,0,.28))}
.tape b{position:relative;background:#17120c;color:#ffb020;font-family:Archivo,sans-serif;font-weight:800;font-size:46px;letter-spacing:9px;padding:12px 30px}
.ruler{position:absolute;z-index:3;left:-6px;top:-20px;bottom:-20px;width:62px;transform:rotate(.6deg);background:linear-gradient(90deg,#8b949e,#eef1f4 22%,#cfd4da 55%,#a7aeb7 85%,#7c858f);box-shadow:6px 0 4px rgba(20,30,50,.18),16px 0 24px rgba(20,30,50,.2)}
.ruler::before{content:'';position:absolute;right:0;top:0;bottom:0;width:30px;background-image:linear-gradient(rgba(30,35,45,.75) 3px,transparent 3px),linear-gradient(rgba(30,35,45,.55) 2px,transparent 2px),linear-gradient(rgba(30,35,45,.45) 1px,transparent 1px);background-size:30px 108px,18px 54px,10px 10.8px;background-repeat:repeat-y;background-position:right 0 top 0,right 0 top 0,right 0 top 0}
.st{position:relative;margin-top:64px}
.st::before{content:'';position:absolute;left:39px;top:44px;bottom:70px;width:5px;background:linear-gradient(180deg,#c9d6f2,#e04a58);border-radius:3px;box-shadow:4px 8px 6px rgba(0,0,0,.35)}
.sp{position:relative;display:flex;gap:34px;align-items:flex-start;margin-top:48px} .sp:first-child{margin-top:0}
.sp .dt{flex:none;width:84px;height:84px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:Archivo,sans-serif;font-weight:800;font-size:38px;color:#fff;text-shadow:0 2px 3px rgba(0,0,0,.45);background:radial-gradient(circle at 34% 28%,#ffffff 0,#b9cdf5 9%,#4f7fd8 32%,#1d3f88 72%,#0d2252 100%);box-shadow:0 6px 4px rgba(0,0,0,.35),10px 22px 18px rgba(0,0,0,.4)}
.sp.bad .dt{background:radial-gradient(circle at 34% 28%,#ffffff 0,#ffc2c8 9%,#ef4c5b 32%,#b3141f 72%,#6d0710 100%)}
.sp b{display:block;font-family:Archivo,sans-serif;font-weight:800;font-size:54px;line-height:1.06} .sp span{display:block;font-size:40px;line-height:1.28;margin-top:8px}
.dark .sp b{text-shadow:0 3px 12px rgba(0,0,0,.35)} .dark .sp span{color:#cdd7ec} .light .sp span{color:#4a5b7e} .dark .sp.bad b{color:#ff8f9a} .light .sp.bad b{color:%PEN%}
"""
# Appel à l'action par défaut de la dernière slide (choix d'Arthur, 11/11/2026) : un outil gratuit, jamais un prix.
CTA_TEST = "Testez votre devis gratuitement en 1\u00a0minute : lien en bio."
CSS+='\n.s.ig{height:1350px}\n.ig .in{top:175px;bottom:110px;right:84px} .ig .in.hk{top:165px}\n.ig .top{top:66px}\n.ig .t1{font-size:96px} .ig .t2{font-size:80px} .ig .t3{font-size:62px}\n.ig .p{font-size:44px;margin-top:26px} .ig .kick{margin-bottom:26px;font-size:28px}\n.ig .dwrap{margin-top:58px} .ig .doc{padding:34px 38px 28px} .ig .doc .r{font-size:34px;padding:14px 0}\n.ig .big{font-size:200px} .ig .bigl{margin-top:16px;font-size:40px}\n.ig .bars{margin-top:40px;gap:30px} .ig .bar .bt{height:56px}\n.ig .card{padding:42px 40px 40px 124px} .ig .it{margin-top:30px} .ig .it b{font-size:46px} .ig .it span{font-size:36px}\n.ig .st{margin-top:40px} .ig .sp{margin-top:32px} .ig .sp b{font-size:48px} .ig .sp span{font-size:36px}\n.ig .tr{margin-top:28px;padding:26px 30px}\n.ig .bm{width:90px;height:112px;margin-bottom:22px} .ig .save{margin-top:34px;padding:24px 30px;font-size:38px}\n.ig .foot{bottom:112px} .ig .postit{top:-64px;width:250px;font-size:54px;padding:24px 18px 28px} .ig .in.hk .dwrap{margin-top:96px} .ig .tape{bottom:36px;height:92px} .ig .plan{width:640px}\n.ig .swipe{margin-top:22px;padding:18px 30px;font-size:34px}\n'
# TikTok : l'appli affiche les photos dans une fenêtre 3:4 (barre de recherche en haut, boutons à droite, légende en bas)
CSS+='\n.s.tk{height:1440px}\n.tk .top{top:150px;right:190px}\n.tk .in{top:250px;bottom:140px;right:190px} .tk .in.hk{top:245px}\n.tk .foot{bottom:150px}\n.tk .t1{font-size:90px} .tk .t2{font-size:76px} .tk .t3{font-size:58px}\n.tk .doc .r{font-size:32px;grid-template-columns:1fr 84px 190px} .tk .doc .dh b{font-size:40px}\n.tk .postit{width:230px;font-size:50px;top:-70px}\n.tk .big{font-size:180px}\n.tk .pen{width:520px}\n'
for k,v in {'%W%':str(W),'%H%':str(H),'%NAVY%':NAVY,'%INK%':INK,'%ORD%':ORD,'%OR%':OR,'%PEN%':PEN,'%FIBER%':FIBER,'%BLOTCH%':BLOTCH,'%INKMASK%':INKMASK,'%ZIG%':ZIG}.items(): CSS=CSS.replace(k,v)
ARROW="<svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'><path d='M5 12h14M13 6l6 6-6 6'/></svg>"
SAVE="<svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2.4' stroke-linejoin='round'><path d='M6 3h12v18l-6-4.5L6 21z'/></svg>"
BIGBM=f"<svg class='bm' viewBox='0 0 24 30'><defs><linearGradient id='bmg' x1='0' x2='1'><stop offset='0' stop-color='#d9481a'/><stop offset='.45' stop-color='#ff8a55'/><stop offset='1' stop-color='#e2521f'/></linearGradient></defs><path d='M3 2h18v26l-9-6.5L3 28z' fill='url(#bmg)'/><path d='M8 12.5l3 3 5.5-6' fill='none' stroke='#1a0f08' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'/></svg>"
NB=chr(160)
def fr(t):
    t=re.sub("(?<=[^ ]) ([?!:;»€%])",lambda m:NB+m.group(1),t); t=t.replace("« ","«"+NB)
    t=re.sub("([0-9]) (?=[0-9]{3}(?![0-9]))",lambda m:m.group(1)+NB,t)
    t=re.sub("([0-9]) (m²|m2|ml|h|kWc|kW|ans|mois|jours|ft|u)(?![A-Za-z0-9])",lambda m:m.group(1)+NB+m.group(2),t)
    return t
def rich(t):
    t=E(fr(t))
    t=re.sub("[*][*](.+?)[*][*]",lambda m:"<b>"+m.group(1)+"</b>",t)
    while '[[' in t and ']]' in t.split('[[',1)[1]:
        x,y=t.split('[[',1); z,w=y.split(']]',1); t=x+"<span class='mk'>"+z+"</span>"+w
    return t
def doc(d,seed=1,hook=False):
    rows=d.get('lines',[]); mark=d.get('mark'); wide=d.get('mark_mode')=='line'
    h="<div class='dh'><b>DEVIS</b><span>N° 2026-0147</span></div><div class='r hd'><span>Désignation</span><span>Qté</span><span>Total HT</span></div>"
    for i,r in enumerate(rows):
        r=(list(r)+['','',''])[:3]; on=(i==mark)
        ring=hand_ellipse(seed+i).replace("class='hand'","class='hand "+('line' if wide else 'amt')+"'") if on else ''
        cl=' on' if on else (' dim' if mark is not None else '')
        h+=f"<div class='r{cl}'><span>{E(fr(r[0]))}</span><span>{E(fr(r[1]))}</span><span>{E(fr(r[2]))}</span>{ring}</div>"
    h+=f"<div class='ft'>{E(fr(d.get('ref','Exemple fictif')))}</div>"
    extra=''
    if d.get('note'): extra+=f"<div class='postit'><span>{E(fr(d['note']))}</span></div>"
    if d.get('stamp'): extra+=f"<div class='stamp' style='right:40px;bottom:-2px'>{E(fr(d['stamp']))}</div>"
    pen=f"<div class='penw' style='position:absolute;left:-150px;bottom:-150px;transform:rotate(-16deg);z-index:4'>{PENSVG}</div>" if hook else ''
    return f"<div class='dwrap'><div class='tilt'><div class='lift l'></div><div class='lift r'></div><div class='doc'>{h}</div><div class='scotch a'></div><div class='scotch b'></div>{extra}</div>{pen}</div>"
def bars(bs,unit):
    mx=max(float(v) for _,v,*_ in bs) or 1
    o="<div class='bars'>"
    for j,b in enumerate(bs):
        lab,v=b[0],float(b[1]); hot=(len(b)>2 and b[2]) or j==len(bs)-1
        val=(f'{v:g}'.replace('.',','))+(NB+unit if unit else '')
        o+=f"<div class='bar{' hot' if hot else ''}'><div class='bl'><span>{E(fr(lab))}</span><span>{E(val)}</span></div><div class='bt'><div class='bf' style='width:calc({max(6,v/mx*100):.0f}% + 6px)'></div></div></div>"
    return o+"</div>"
def slide(s,i,n,ig=False):
    tk=(ig=='tk')
    th=s.get('theme','dark'); ty=s.get('type','text')
    k=f"<div class='kick'>{E(fr(s['kicker']))}</div>" if s.get('kicker') else ''
    P=(lambda key:f"<div class='p'>{rich(s[key])}</div>" if s.get(key) else '')
    if ty=='hook':
        b=f"{k}<div class='t t1'>{rich(s['title'])}</div>"+P('text')+(doc(s['doc'],i*7,True) if s.get('doc') else '')
        if not s.get('noswipe'): b+=f"<div class='swipe'>{E(s.get('swipe','Glissez'))}{ARROW}</div>"
    elif ty=='doc':
        b=f"{k}<div class='t t2'>{rich(s['title'])}</div>"+doc(s['doc'],i*7)+P('text')
    elif ty=='number':
        b=f"{k}<div class='big'>{E(fr(s['number']))}</div><div class='bigl'>{E(fr(s.get('label','')))}</div>"+(bars(s['bars'],s.get('unit','')) if s.get('bars') else '')+(f"<div class='t t3' style='margin-top:56px'>{rich(s['title'])}</div>" if s.get('title') else '')+P('text')
    elif ty=='check':
        its=''.join(f"<div class='it'>{CHK}<b>{E(fr(a.split('|')[0]))}</b>"+(f"<span>{E(fr(a.split('|',1)[1]))}</span>" if '|' in a else '')+"</div>" for a in s['items'])
        b=f"{k}<div class='t t2' style='margin-bottom:64px'>{rich(s['title'])}</div><div class='card'><div class='scotch'></div>{its}</div>"
    elif ty=='traduction':
        b=f"{k}<div class='t t2'>{rich(s['title'])}</div>"+''.join(f"<div class='tr'><div class='q'>« {E(fr(r.split('|')[0]))} »</div><div class='a'>= {E(fr(r.split('|',1)[1]))}</div></div>" for r in s['rows'])
    elif ty=='steps':
        st=s['steps']; ss=''
        for j,a in enumerate(st):
            q=a.split('|'); ss+=f"<div class='sp{' bad' if j==len(st)-1 else ''}'><div class='dt'>{'!' if j==len(st)-1 else j+1}</div><div><b>{E(fr(q[0]))}</b>"+(f"<span>{E(fr(q[1]))}</span>" if len(q)>1 else '')+"</div></div>"
        b=f"{k}<div class='t t2'>{rich(s['title'])}</div><div class='st'>{ss}</div>"
    elif ty=='end':
        b=f"{BIGBM}{k}<div class='t t2'>{rich(s['title'])}</div>"+P('text')+f"<div class='save'>{SAVE}<div>{E(fr(s.get('save','Enregistrez ce post pour votre prochain devis.')))}</div></div>"+f"<div class='offer'>{E(fr(s.get('offer') or CTA_TEST))}</div>"
    else:
        b=f"{k}<div class='t t2'>{rich(s['title'])}</div>"+P('text')
    foot="<div class='foot'>contre-plan.com · Analyse de devis par un ingénieur BTP</div>" if ty=='end' else ''
    cnt=f"<span class='n'>{i}/{n}</span>" if n else ''
    pl=plan('#bcd2ff' if th=='dark' else INK) if ty in ('hook','text','number','end') else ''
    cls='in hk' if ty=='hook' else 'in'
    deco=''
    if n:
        lab="<span style='right:0'>FIN</span>" if i==n else ''
        deco+=f"<div class='cote' style='top:{1440-110 if tk else (1350-70 if ig else H-385)}px;left:{84 if i==1 else 0}px;right:{84 if i==n else 0}px;--o:{-84 if i==1 else 0}px'>{'<i class=a></i>' if i==1 else ''}{'<i class=b></i>' if i==n else ''}{lab}</div>"
    if s.get('alert') or ty=='steps': deco+=f"<div class='tape'><b>{E(s.get('alert_text','ATTENTION'))}</b></div>"
    if th=='light': deco+="<div class='ruler'></div>"
    bg="<div class='L grid'></div><div class='L fib'></div><div class='L blot'></div><div class='L crease'></div>"
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='s {th}{" ig" if ig else ""}{" tk" if tk else ""}'>{bg}{pl}<div class='L vig' style='z-index:2'></div>{deco}<div class='top'><span class='lg'><i></i>CONTRE-PLAN</span>{cnt}</div><div class='{cls}'>{b}</div>{foot}</div></body></html>"
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(viewport={'width':W,'height':H})
    sl=spec['slides']; n=len(sl); bad=[]
    def shot(html_,path):
        pg.set_content(html_); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300); pg.screenshot(path=path)
    for i,s in enumerate(sl,1):
        h_=slide(s,i,n); open(f'{out}/slide{i}.html','w').write(slide(dict(s,noswipe=True),i,n) if s.get('type')=='hook' else h_)
        pg.set_content(h_); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
        o=pg.evaluate("()=>{let m=0,r=0;document.querySelectorAll('.in *').forEach(e=>{if(e.closest('svg,.penw'))return;const b=e.getBoundingClientRect();if(b.width&&b.bottom>m)m=b.bottom;if(b.width&&b.right>r)r=b.right});return [Math.round(m),Math.round(r)]}")
        if o[0]>H-400: bad.append(f'slide{i} dépasse en bas ({o[0]} px > {H-400} px)')
        if o[1]>W-90: bad.append(f'slide{i} dépasse à droite ({o[1]} px > {W-90} px)')
        pg.screenshot(path=f'{out}/slide{i}.png')
        if s.get('type')=='hook': shot(slide(dict(s,noswipe=True),i,n),f'{out}/cover.png')
    pg.set_viewport_size({'width':W,'height':1350})
    for i,s in enumerate(sl,1):
        pg.set_content(slide(s,i,n,True)); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
        o=pg.evaluate("()=>{let m=0,r=0;document.querySelectorAll('.in *').forEach(e=>{if(e.closest('svg,.penw'))return;const b=e.getBoundingClientRect();if(b.width&&b.bottom>m)m=b.bottom;if(b.width&&b.right>r)r=b.right});return [Math.round(m),Math.round(r)]}")
        if o[0]>1350-50 or o[1]>W-50: bad.append(f'ig{i} (Instagram) dépasse ({o[0]} px en bas, {o[1]} px à droite)')
        pg.screenshot(path=f'{out}/ig{i}.png')
    # Carrousel TikTok au format 3:4 (1080x1440) : rien sous la barre de recherche, les boutons ou la légende
    pg.set_viewport_size({'width':W,'height':1440})
    for i,s in enumerate(sl,1):
        pg.set_content(slide(s,i,n,'tk')); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
        o=pg.evaluate("()=>{let m=0,r=0,t=9999;document.querySelectorAll('.in *, .top *').forEach(e=>{if(e.closest('svg,.penw'))return;const b=e.getBoundingClientRect();if(!b.width)return;if(b.bottom>m)m=b.bottom;if(b.right>r)r=b.right;if(b.top<t)t=b.top});return [Math.round(m),Math.round(r),Math.round(t)]}")
        if o[0]>1440-130 or o[1]>W-170 or o[2]<140: bad.append(f'tk{i} (TikTok) sort de la zone visible ({o[0]} px en bas, {o[1]} px à droite, {o[2]} px en haut)')
        pg.screenshot(path=f'{out}/tk{i}.png')
    pg.set_viewport_size({'width':W,'height':H})
    if spec.get('story'): shot(slide(dict(spec['story'],type=spec['story'].get('type','hook'),noswipe=True),0,0),f'{out}/story.png')
    br.close()
print('OK' if not bad else 'A CORRIGER : '+' ; '.join(bad))
