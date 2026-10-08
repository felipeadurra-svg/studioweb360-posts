import base64, sys
from pathlib import Path

BRAND = Path("/tmp/studioweb360-posts/brand")
HERO_IMG = Path(sys.argv[1])          # James corpo inteiro, PNG recortado
OUT = Path(sys.argv[2])

P = "#1E8A55"; PL = "#5FD39A"; PD = "#0E5232"
LBG = "#F1F6F2"; LBR = "#DCE7DF"; DBG = "#0D1812"; MUTED = "#5d6a62"
GRAD = f"linear-gradient(165deg,{PD} 0%,{P} 55%,{PL} 120%)"
WA = "#25D366"; IG = "linear-gradient(45deg,#F9CE34 0%,#EE2A7B 50%,#6228D7 100%)"; MS = "linear-gradient(45deg,#0099FF 0%,#A033FF 60%,#FF5280 100%)"
TOTAL = 7

def b64(p):
    mime = "image/png" if str(p).endswith(".png") else "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(Path(p).read_bytes()).decode()

HERO = b64(HERO_IMG)
FACE = b64(BRAND / "james/avatar-circulo-160.png")
def jx(name): return b64(BRAND / f"james/{name}.png")
FADE = "-webkit-mask-image:linear-gradient(to bottom,#000 72%,transparent 100%);mask-image:linear-gradient(to bottom,#000 72%,transparent 100%);"

# ---- ícones dos canais (glifos simplificados + nome escrito) ----
def ico(kind, s=44, r=None):
    r = r if r is not None else s * 0.28
    g = s * 0.56
    if kind == "wa":
        bg = WA; rad = "50%"
        glyph = f'<svg width="{g}" height="{g}" viewBox="0 0 24 24" fill="none"><path d="M12 3a9 9 0 0 0-7.8 13.5L3 21l4.6-1.2A9 9 0 1 0 12 3z" stroke="#fff" stroke-width="1.8" stroke-linejoin="round"/><path d="M9 8.2c.3-.5.8-.5 1-.1l.8 1.8c.1.3 0 .6-.2.8l-.5.5c.6 1.2 1.6 2.2 2.8 2.8l.5-.5c.2-.2.5-.3.8-.2l1.8.8c.4.2.4.7-.1 1-1 .9-2.4 1-3.6.3a9 9 0 0 1-3.6-3.6c-.6-1.2-.6-2.6.1-3.6z" fill="#fff"/></svg>'
    elif kind == "ig":
        bg = IG; rad = f"{r}px"
        glyph = f'<svg width="{g}" height="{g}" viewBox="0 0 24 24" fill="none"><rect x="3.5" y="3.5" width="17" height="17" rx="5" stroke="#fff" stroke-width="2"/><circle cx="12" cy="12" r="4" stroke="#fff" stroke-width="2"/><circle cx="17" cy="7" r="1.2" fill="#fff"/></svg>'
    elif kind == "go":
        bg = "#fff"; rad = "50%"
        glyph = f'<svg width="{g*1.05}" height="{g*1.05}" viewBox="0 0 24 24" fill="none" stroke-width="3.3"><path d="M6.64 7.5A7 7 0 0 1 17.36 7.5" stroke="#EA4335"/><path d="M6.64 16.5A7 7 0 0 1 6.64 7.5" stroke="#FBBC05"/><path d="M17.36 16.5A7 7 0 0 1 6.64 16.5" stroke="#34A853"/><path d="M19 12A7 7 0 0 1 17.36 16.5M12.2 12H19.6" stroke="#4285F4"/></svg>'
    else:
        bg = MS; rad = "50%"
        glyph = f'<svg width="{g}" height="{g}" viewBox="0 0 24 24" fill="none"><path d="M12 3C7 3 3 6.7 3 11.3c0 2.6 1.3 4.9 3.3 6.4V21l3-1.7c.9.3 1.8.4 2.7.4 5 0 9-3.7 9-8.4S17 3 12 3z" fill="#fff"/><path d="M7 13.5l3.2-3.4 2 1.6 3.8-2.1-3.2 3.4-2-1.6z" fill="#7B3CF0"/></svg>'
    return f'<span style="width:{s}px;height:{s}px;border-radius:{rad};background:{bg};display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;box-shadow:0 0 0 1px rgba(255,255,255,0.15),0 8px 22px rgba(0,0,0,0.35);">{glyph}</span>'

def bar(i, light):
    pct = (i + 1) / TOTAL * 100
    tr = 'rgba(0,0,0,0.08)' if light else 'rgba(255,255,255,0.14)'
    fi = P if light else '#fff'
    lb = 'rgba(0,0,0,0.35)' if light else 'rgba(255,255,255,0.5)'
    return f'''<div style="position:absolute;bottom:0;left:0;right:0;padding:16px 28px 20px;z-index:10;display:flex;align-items:center;gap:10px;">
<div style="flex:1;height:3px;background:{tr};border-radius:2px;overflow:hidden;"><div style="height:100%;width:{pct}%;background:{fi};border-radius:2px;"></div></div>
<span class="sans" style="font-size:11px;color:{lb};font-weight:500;">{i+1}/{TOTAL}</span></div>'''

def arrow(light):
    bg = 'rgba(0,0,0,0.05)' if light else 'rgba(255,255,255,0.07)'
    st = 'rgba(0,0,0,0.25)' if light else 'rgba(255,255,255,0.35)'
    return f'''<div style="position:absolute;right:0;top:0;bottom:0;width:44px;z-index:9;display:flex;align-items:center;justify-content:center;background:linear-gradient(to right,transparent,{bg});">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M9 6l6 6-6 6" stroke="{st}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'''

def slide(i, bg, light, body, last=False, justify="flex-end", art="", pad="30px 46px 58px 34px"):
    return f'''<div class="slide" style="background:{bg};">{art}
<div style="position:absolute;inset:0;z-index:2;padding:{pad};display:flex;flex-direction:column;justify-content:{justify};">{body}</div>
{'' if last else arrow(light)}{bar(i, light)}</div>'''

def face(size, border="none"):
    return f'<img src="{FACE}" style="width:{size}px;height:{size}px;border-radius:50%;object-fit:cover;background:{P};border:{border};flex-shrink:0;">'

def head(tag, title, light, sub, tagc=None):
    tc = DBG if light else '#fff'
    nc = tagc or (P if light else PL)
    sc = MUTED if light else 'rgba(255,255,255,0.68)'
    return f'''<span class="sans" style="font-size:10px;font-weight:600;letter-spacing:2px;color:{nc};margin-bottom:10px;">{tag}</span>
<h2 class="serif" style="font-size:29px;font-weight:700;line-height:1.1;letter-spacing:-0.5px;color:{tc};">{title}</h2>
<p class="sans" style="font-size:13.5px;line-height:1.5;color:{sc};margin-top:10px;">{sub}</p>'''

def bub_in(text, light=True, time="23:14", r="14px 14px 14px 4px"):
    bg = '#fff' if light else 'rgba(255,255,255,0.08)'
    bd = LBR if light else 'rgba(255,255,255,0.08)'
    tc = '#2a332d' if light else 'rgba(255,255,255,0.9)'
    return f'''<div style="align-self:flex-start;max-width:80%;background:{bg};border:1px solid {bd};border-radius:{r};padding:8px 12px;">
<p class="sans" style="font-size:12.5px;color:{tc};line-height:1.35;">{text}</p><p class="sans" style="font-size:9.5px;color:#9aa69e;text-align:right;margin-top:2px;">{time}</p></div>'''

def bub_out(text, time="23:14", bg="#D7F2E2", tc="#183223", mc="#5f8a70"):
    return f'''<div style="align-self:flex-end;max-width:82%;background:{bg};border-radius:14px 14px 4px 14px;padding:8px 12px;">
<p class="sans" style="font-size:12.5px;color:{tc};line-height:1.35;">{text}</p><p class="sans" style="font-size:9.5px;color:{mc};text-align:right;margin-top:2px;">{time} · James ✓</p></div>'''

def window(kind, title, inner, light):
    bg = '#fff' if light else 'rgba(255,255,255,0.04)'
    bd = LBR if light else 'rgba(255,255,255,0.09)'
    tc = DBG if light else '#fff'
    return f'''<div style="background:{bg};border:1px solid {bd};border-radius:16px;padding:10px 12px 12px;margin-bottom:18px;{'box-shadow:0 8px 22px rgba(14,82,50,0.08);' if light else ''}">
<div style="display:flex;align-items:center;gap:8px;padding-bottom:9px;margin-bottom:10px;border-bottom:1px solid {bd};">{ico(kind, 22, 6)}
<span class="sans" style="font-size:11.5px;font-weight:600;color:{tc};">{title}</span>
<span class="sans" style="margin-left:auto;font-size:9.5px;color:{P if light else PL};font-weight:600;">● James online</span></div>
<div style="display:flex;flex-direction:column;gap:7px;">{inner}</div></div>'''

S = []

# ---------- 1 HERO (tech) ----------
grid = ("background-image:linear-gradient(rgba(95,211,154,0.07) 1px,transparent 1px),"
        "linear-gradient(90deg,rgba(95,211,154,0.07) 1px,transparent 1px);background-size:28px 28px;")
import math
CX, CY, RX, RY, ROT = 210, 352, 182, 50, -9
def opt(t):
    t=math.radians(t); r=math.radians(ROT)
    x=RX*math.cos(t); y=RY*math.sin(t)
    return CX + x*math.cos(r) - y*math.sin(r), CY + x*math.sin(r) + y*math.cos(r)
def trail(t, n=22, span=55, w=7):
    segs=""
    for k in range(n):
        t0=t-span+span*k/n; t1=t-span+span*(k+1)/n
        (x0,y0),(x1,y1)=opt(t0),opt(t1)
        segs+=f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="#BFFFDD" stroke-opacity="{0.15+((k+1)/n)**1.3*0.85:.2f}" stroke-width="{w*(0.4+0.6*(k+1)/n):.1f}" stroke-linecap="round"/>'
    return segs
def orbit_icon(kind, label, t, s, z):
    x,y=opt(t)
    op = "1" if z==3 else "0.92"
    return f'''<div style="position:absolute;left:{x-s/2:.0f}px;top:{y-s/2:.0f}px;z-index:{z};opacity:{op};display:flex;flex-direction:column;align-items:center;gap:4px;width:{s}px;">
{ico(kind, s)}<span class="sans" style="font-size:8.5px;font-weight:600;letter-spacing:1px;color:rgba(255,255,255,0.85);background:rgba(13,24,18,0.75);padding:2px 7px;border-radius:10px;border:1px solid rgba(95,211,154,0.3);white-space:nowrap;">{label}</span></div>'''
ICONS=[("wa","WHATSAPP",128,54,3),("ms","MESSENGER",52,54,3),("ig","INSTAGRAM",312,42,1),("go","GOOGLE",228,42,1)]
def ring(half):  # half: "back" (topo) ou "front" (base)
    pts=[opt(t) for t in (range(180,361,4) if half=="back" else range(0,181,4))]
    d="M"+" L".join(f"{x:.1f} {y:.1f}" for x,y in pts)
    op = 0.35 if half=="back" else 0.75
    tr="".join(trail(t) for k,l,t,sz,z in ICONS if (z==1)==(half=="back"))
    return f'''<svg style="position:absolute;left:0;top:0;z-index:{1 if half=="back" else 3};pointer-events:none;" width="420" height="525" viewBox="0 0 420 525" fill="none">
<path d="{d}" stroke="{PL}" stroke-opacity="{op}" stroke-width="1.4"/><path d="{d}" stroke="{PL}" stroke-opacity="{op*0.35}" stroke-width="7"/>{tr}</svg>'''
hero_art = f'''
<div style="position:absolute;inset:0;{grid}-webkit-mask-image:radial-gradient(circle at 50% 62%,#000 20%,transparent 75%);mask-image:radial-gradient(circle at 50% 62%,#000 20%,transparent 75%);"></div>
<div style="position:absolute;left:50%;top:330px;width:380px;height:380px;transform:translate(-50%,-50%);border-radius:50%;background:radial-gradient(circle,rgba(30,138,85,0.55) 0%,rgba(30,138,85,0.12) 45%,transparent 70%);"></div>
<svg style="position:absolute;left:0;top:0;z-index:1;" width="420" height="525" viewBox="0 0 420 525" fill="none">
  <ellipse cx="210" cy="480" rx="88" ry="12" fill="rgba(95,211,154,0.18)"/>
  <ellipse cx="210" cy="480" rx="88" ry="12" stroke="{PL}" stroke-opacity="0.5"/>
</svg>
{ring("back")}
{"".join(orbit_icon(k,l,t,sz,z) for k,l,t,sz,z in ICONS if z==1)}
<img src="{HERO}" style="position:absolute;z-index:2;left:50%;transform:translateX(-50%);bottom:40px;height:332px;filter:drop-shadow(0 0 18px rgba(95,211,154,0.35));">
{ring("front")}
{"".join(orbit_icon(k,l,t,sz,z) for k,l,t,sz,z in ICONS if z==3)}
<div style="position:absolute;right:26px;top:196px;z-index:3;padding:7px 10px;border-radius:10px;background:rgba(13,24,18,0.75);border:1px solid rgba(95,211,154,0.35);">
<p class="serif" style="font-size:20px;font-weight:800;color:{PL};line-height:1;">24h</p><p class="sans" style="font-size:8.5px;color:rgba(255,255,255,0.7);letter-spacing:1px;">ONLINE</p></div>'''
S.append(slide(0, DBG, False, f'''
<div style="text-align:center;">
<span class="sans" style="display:inline-block;font-size:9.5px;font-weight:600;letter-spacing:2px;color:{PL};padding:4px 10px;border:1px solid rgba(95,211,154,0.35);border-radius:20px;margin-bottom:10px;">● JAMES · ATENDENTE DE IA</span>
<h1 class="serif" style="font-size:28px;font-weight:800;line-height:1.05;letter-spacing:-1px;color:#fff;">Um atendente.<br><span style="color:{PL};">Todos os canais.</span><br>Zero cliente esperando.</h1>
</div>''', justify="flex-start", art=hero_art, pad="26px 30px 58px 30px"))

# ---------- 2 PROBLEMA (light) ----------
def notif(kind, app, who, msg, t):
    return f'''<div style="display:flex;gap:10px;align-items:center;padding:9px 11px;background:#fff;border:1px solid {LBR};border-radius:12px;">{ico(kind, 28, 8)}
<div style="flex:1;min-width:0;"><p class="sans" style="font-size:11px;font-weight:600;color:{DBG};">{who} <span style="font-weight:400;color:#9aa69e;">· {app}</span></p>
<p class="sans" style="font-size:11px;color:{MUTED};white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{msg}</p></div>
<span class="sans" style="font-size:9px;color:#E5484D;font-weight:600;">{t}</span></div>'''
S.append(slide(1, LBG, True, f'''<div style="display:flex;flex-direction:column;gap:6px;margin-bottom:20px;">
{notif("wa","WhatsApp","Marina","Oi, ainda tem horário pra sábado?","há 3h")}
{notif("ig","Direct","@bruno.tav","Qual o valor do pacote?","há 5h")}
{notif("ms","Messenger","Helena R.","Vocês entregam no meu bairro?","ontem")}
{notif("wa","WhatsApp","Carlos","Alguém aí? 😕","ontem")}
</div>''' + head("O PROBLEMA", "Seu cliente chama em 3 lugares. Você responde em um.", True,
    "Enquanto você responde o WhatsApp, o Direct e o Messenger acumulam. Quem não recebe resposta rápida fecha com quem respondeu primeiro.")))

# ---------- 3 WHATSAPP (dark) ----------
S.append(slide(2, DBG, False, window("wa", "WhatsApp · seu número",
    bub_in("Boa noite! Vocês atendem sábado?", False, "22:47") +
    bub_out("Boa noite! Atendemos sim, das 9h às 14h. Quer que eu já reserve um horário pra você?", "22:47") +
    bub_in("Pode ser 10h 🙏", False, "22:48"), False) +
    head("CANAL 1 · WHATSAPP", "No WhatsApp, no número que você já usa", False,
    "Texto ou áudio, de madrugada ou no domingo. O James responde na hora, tira dúvida e marca horário sem você parar o que está fazendo.", WA)))

# ---------- 4 INSTAGRAM (light) ----------
S.append(slide(3, LBG, True, window("ig", "Direct · @seunegocio",
    bub_in("vi o post de vocês! quanto custa o pacote completo?", True, "14:05", "18px") +
    bub_out("Oi! Que bom que gostou 😊 O pacote completo sai por R$ 180. Quer ver os horários da semana?", "14:05", "#EFE7FB", "#2b1a4a", "#8a73b5") +
    bub_in("quero sim!", True, "14:06", "18px"), True) +
    head("CANAL 2 · INSTAGRAM", "No Direct, enquanto o post ainda está quente", True,
    "Quem viu seu post e chamou no Direct recebe resposta na mesma hora, com preço e horários. O interesse não esfria esperando você.", "#C2338A")))

# ---------- 5 MESSENGER (dark) ----------
S.append(slide(4, DBG, False, window("ms", "Messenger · página do Facebook",
    bub_in("Olá, vocês entregam em São Bernardo?", False, "09:12", "18px") +
    bub_out("Olá! Entregamos sim, o prazo é de 1 dia útil. Quer que eu te passe as opções?", "09:12", "#2E3BFF22", "#fff", "rgba(255,255,255,0.55)") +
    bub_in("Quero, obrigada!", False, "09:13", "18px"), False) +
    head("CANAL 3 · FACEBOOK MESSENGER", "No Messenger da sua página do Facebook", False,
    "Muita gente ainda chama pela página do Facebook. O James também está lá, com as mesmas informações e o mesmo jeito de atender.", "#8C7BFF")))

# ---------- 6 PAINEL ÚNICO (light) ----------
def row(kind, who, msg, status):
    return f'''<div style="display:flex;align-items:center;gap:9px;padding:8px 10px;background:#fff;border:1px solid {LBR};border-radius:11px;">{ico(kind, 24, 7)}
<div style="flex:1;min-width:0;"><p class="sans" style="font-size:11px;font-weight:600;color:{DBG};">{who}</p><p class="sans" style="font-size:10.5px;color:{MUTED};white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{msg}</p></div>
<span class="sans" style="font-size:9px;padding:3px 8px;border-radius:20px;background:#E3F3EA;color:{PD};font-weight:600;">{status}</span></div>'''
S.append(slide(5, LBG, True, f'''<div style="display:flex;flex-direction:column;gap:6px;margin-bottom:20px;">
{row("wa","Marina","Horário de sábado 10h confirmado","marcado")}
{row("ig","@bruno.tav","Enviou preço do pacote completo","respondido")}
{row("ms","Helena R.","Passou o prazo de entrega","respondido")}
{row("wa","Carlos","Pediu desconto fora do combinado","com você")}
</div>''' + head("TUDO NUM LUGAR SÓ", "Três canais, um painel só", True,
    "Você acompanha as conversas dos três canais pelo celular. Quer assumir algum cliente? Um toque e a conversa é sua."),
    art=f'<img src="{jx("expressoes/apontando-lado")}" style="position:absolute;z-index:1;left:34px;top:-2px;height:150px;{FADE}">'))

# ---------- 7 CTA ----------
S.append(slide(6, GRAD, False, f'''
<div style="text-align:center;display:flex;flex-direction:column;align-items:center;">
<img src="{jx('sorriso')}" style="height:160px;margin-bottom:6px;{FADE}">
<div style="display:flex;gap:10px;margin-bottom:12px;">{ico("wa",34)}{ico("ig",34,10)}{ico("ms",34)}{ico("go",34)}</div>
<h2 class="serif" style="font-size:29px;font-weight:700;line-height:1.1;letter-spacing:-0.5px;color:#fff;">Quer o James atendendo nos <em>seus</em> canais?</h2>
<div class="sans" style="display:inline-flex;align-items:center;gap:8px;padding:12px 26px;margin-top:16px;background:{LBG};color:{PD};font-weight:700;font-size:14px;border-radius:28px;">Comente JAMES</div>
<p class="sans" style="font-size:12.5px;color:rgba(255,255,255,0.88);margin-top:14px;">que eu te mostro como funciona no seu negócio<br>ou acesse <b style="color:#fff;">studioweb360.com.br</b></p>
</div>''', last=True, justify="center"))

faces = ""
for w in (300, 400, 600, 700, 800):
    b = base64.b64encode((BRAND / f'fonts/bricolage-grotesque-latin-{w}-normal.woff2').read_bytes()).decode()
    faces += f"@font-face{{font-family:'Bricolage Grotesque';font-weight:{w};font-style:normal;src:url(data:font/woff2;base64,{b}) format('woff2');}}\n"

dots_html = "".join(f'<span class="dot{" on" if i==0 else ""}"></span>' for i in range(TOTAL))
html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>James em 3 canais</title>
<style>
{faces}
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{background:#e9ece9;display:flex;justify-content:center;padding:28px 0;font-family:'Bricolage Grotesque',sans-serif;}}
.serif,.sans{{font-family:'Bricolage Grotesque',sans-serif;}}
.ig-frame{{width:420px;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 10px 30px rgba(0,0,0,0.12);}}
.ig-header{{display:flex;align-items:center;gap:10px;padding:12px 14px;}}
.carousel-viewport{{width:420px;aspect-ratio:4/5;overflow:hidden;position:relative;cursor:grab;}}
.carousel-track{{display:flex;height:100%;transition:transform .35s ease;}}
.slide{{min-width:420px;width:420px;height:525px;position:relative;overflow:hidden;}}
.ig-dots{{display:flex;justify-content:center;gap:4px;padding:10px 0 2px;}}
.dot{{width:6px;height:6px;border-radius:50%;background:#cfd6d1;}} .dot.on{{background:{P};}}
.ig-actions{{display:flex;gap:14px;padding:8px 14px;}}
.ig-caption{{padding:0 14px 14px;font-size:13px;line-height:1.45;color:#222;}}
</style></head><body>
<div class="ig-frame">
<div class="ig-header">{face(32)}<div><div style="font-size:13px;font-weight:600;">studioweb360.ia</div><div style="font-size:11px;color:#888;">James · WhatsApp, Instagram e Messenger</div></div></div>
<div class="carousel-viewport"><div class="carousel-track">{"".join(S)}</div></div>
<div class="ig-dots">{dots_html}</div>
<div class="ig-actions">
<svg width="24" height="24" fill="none" stroke="#222" stroke-width="2" viewBox="0 0 24 24"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 1 0-7.8 7.8L12 21l8.8-8.6a5.5 5.5 0 0 0 0-7.8z"/></svg>
<svg width="24" height="24" fill="none" stroke="#222" stroke-width="2" viewBox="0 0 24 24"><path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 21l2.1-5.6A8.4 8.4 0 1 1 21 11.5z"/></svg>
<svg width="24" height="24" fill="none" stroke="#222" stroke-width="2" viewBox="0 0 24 24"><path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg>
<svg style="margin-left:auto" width="24" height="24" fill="none" stroke="#222" stroke-width="2" viewBox="0 0 24 24"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg></div>
<div class="ig-caption"><b>studioweb360.ia</b> O James agora atende no WhatsApp, no Direct e no Messenger 👆<div style="font-size:10px;color:#999;margin-top:6px;letter-spacing:.5px;">2 HOURS AGO</div></div>
</div>
<script>
const track=document.querySelector('.carousel-track'),vp=document.querySelector('.carousel-viewport'),dots=[...document.querySelectorAll('.dot')];
let idx=0,startX=null;const N={TOTAL};
function go(i){{idx=Math.max(0,Math.min(N-1,i));track.style.transform='translateX('+(-idx*420)+'px)';dots.forEach((d,k)=>d.classList.toggle('on',k===idx));}}
vp.addEventListener('pointerdown',e=>{{startX=e.clientX;}});
window.addEventListener('pointerup',e=>{{if(startX===null)return;const dx=e.clientX-startX;if(Math.abs(dx)>30)go(idx+(dx<0?1:-1));else if(Math.abs(dx)<5)go(idx+(e.clientX-vp.getBoundingClientRect().left>210?1:-1));startX=null;}});
document.addEventListener('keydown',e=>{{if(e.key==='ArrowRight')go(idx+1);if(e.key==='ArrowLeft')go(idx-1);}});
</script></body></html>'''
OUT.write_text(html, encoding="utf-8")
print(OUT)
