import base64, sys, random, io
from pathlib import Path
from PIL import Image

BRAND = Path(sys.argv[1]); COVER = Path(sys.argv[2]); OUT = Path(sys.argv[3])
P = "#1E8A55"; PL = "#5FD39A"; PD = "#0E5232"; BG = "#06110C"; GOLD = "#F2C46D"
WA = "#25D366"; IG = "linear-gradient(45deg,#F9CE34 0%,#EE2A7B 50%,#6228D7 100%)"; MS = "linear-gradient(45deg,#0099FF 0%,#A033FF 60%,#FF5280 100%)"
TOTAL = 7

def b64(p, q=None):
    p = Path(p)
    if q:
        buf = io.BytesIO(); Image.open(p).convert("RGB").save(buf, "JPEG", quality=q)
        return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    mime = "image/png" if p.suffix == ".png" else "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode()
def jx(n, clean=False):
    if not clean: return b64(BRAND / f"james/{n}.png")
    im = Image.open(BRAND / f"james/{n}.png").convert("RGBA"); r,g,b_,a = im.split()
    a = a.point(lambda v: 0 if v < 60 else v); im = Image.merge("RGBA",(r,g,b_,a)).crop(a.getbbox())
    buf = io.BytesIO(); im.save(buf, "PNG"); return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()
FACE = b64(BRAND / "james/avatar-circulo-160.png")

def ico(kind, s=44):
    g = s * 0.56
    if kind == "wa":
        bg, rad = WA, "50%"
        gl = f'<svg width="{g}" height="{g}" viewBox="0 0 24 24" fill="none"><path d="M12 3a9 9 0 0 0-7.8 13.5L3 21l4.6-1.2A9 9 0 1 0 12 3z" stroke="#fff" stroke-width="1.8" stroke-linejoin="round"/><path d="M9 8.2c.3-.5.8-.5 1-.1l.8 1.8c.1.3 0 .6-.2.8l-.5.5c.6 1.2 1.6 2.2 2.8 2.8l.5-.5c.2-.2.5-.3.8-.2l1.8.8c.4.2.4.7-.1 1-1 .9-2.4 1-3.6.3a9 9 0 0 1-3.6-3.6c-.6-1.2-.6-2.6.1-3.6z" fill="#fff"/></svg>'
    elif kind == "ig":
        bg, rad = IG, f"{s*0.28}px"
        gl = f'<svg width="{g}" height="{g}" viewBox="0 0 24 24" fill="none"><rect x="3.5" y="3.5" width="17" height="17" rx="5" stroke="#fff" stroke-width="2"/><circle cx="12" cy="12" r="4" stroke="#fff" stroke-width="2"/><circle cx="17" cy="7" r="1.2" fill="#fff"/></svg>'
    else:
        bg, rad = MS, "50%"
        gl = f'<svg width="{g}" height="{g}" viewBox="0 0 24 24" fill="none"><path d="M12 3C7 3 3 6.7 3 11.3c0 2.6 1.3 4.9 3.3 6.4V21l3-1.7c.9.3 1.8.4 2.7.4 5 0 9-3.7 9-8.4S17 3 12 3z" fill="#fff"/><path d="M7 13.5l3.2-3.4 2 1.6 3.8-2.1-3.2 3.4-2-1.6z" fill="#7B3CF0"/></svg>'
    return f'<span style="width:{s}px;height:{s}px;border-radius:{rad};background:{bg};display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;box-shadow:0 0 18px rgba(95,211,154,0.35),0 6px 16px rgba(0,0,0,0.5);">{gl}</span>'

def bar(i):
    pct = (i + 1) / TOTAL * 100
    return f'''<div style="position:absolute;bottom:0;left:0;right:0;padding:16px 26px 18px;z-index:20;display:flex;align-items:center;gap:10px;">
<div style="flex:1;height:3px;background:rgba(255,255,255,0.14);border-radius:2px;overflow:hidden;"><div style="height:100%;width:{pct}%;background:linear-gradient(90deg,{P},{PL});box-shadow:0 0 8px {PL};"></div></div>
<span style="font-size:11px;color:rgba(255,255,255,0.5);font-weight:500;">{i+1}/{TOTAL}</span></div>'''

def arrow():
    return '''<div style="position:absolute;right:10px;top:50%;transform:translateY(-50%);z-index:20;width:30px;height:30px;border-radius:50%;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.15);display:flex;align-items:center;justify-content:center;">
<svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M9 6l6 6-6 6" stroke="rgba(255,255,255,0.7)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'''

def stage(glow_xy="50% 40%", glow_col="rgba(30,138,85,0.55)", floor=False):
    fl = f'<div style="position:absolute;left:-10%;right:-10%;bottom:-40px;height:160px;background:radial-gradient(ellipse at 50% 0%,rgba(95,211,154,0.22),transparent 65%);"></div>' if floor else ''
    return f'''<div style="position:absolute;inset:0;background:radial-gradient(circle at {glow_xy},{glow_col} 0%,rgba(14,82,50,0.25) 35%,transparent 70%),{BG};"></div>
<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 50% 50%,transparent 55%,rgba(0,0,0,0.6) 100%);"></div>{fl}'''

def orbit(cx, cy, rx, ry, rot, op=0.6):
    return f'''<svg style="position:absolute;left:0;top:0;" width="420" height="525" viewBox="0 0 420 525" fill="none">
<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" transform="rotate({rot} {cx} {cy})" stroke="{PL}" stroke-opacity="{op*0.35}" stroke-width="6"/>
<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" transform="rotate({rot} {cx} {cy})" stroke="{PL}" stroke-opacity="{op}" stroke-width="1.2"/></svg>'''

def tag(num, txt):
    return f'<div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;"><span style="font-size:11px;font-weight:800;color:{BG};background:{PL};padding:2px 7px;border-radius:6px;box-shadow:0 0 12px {PL};">{num}</span><span style="font-size:10px;font-weight:600;letter-spacing:2px;color:{PL};">{txt}</span></div>'

def glass(inner, css=""):
    return f'<div style="background:linear-gradient(160deg,rgba(255,255,255,0.10),rgba(255,255,255,0.03));border:1px solid rgba(95,211,154,0.28);border-radius:16px;box-shadow:0 0 0 1px rgba(255,255,255,0.03) inset,0 18px 40px rgba(0,0,0,0.5),0 0 30px rgba(30,138,85,0.18);backdrop-filter:blur(6px);{css}">{inner}</div>'

def slide(i, art, body, last=False):
    return f'<div class="slide">{art}{body}{"" if last else arrow()}{bar(i)}</div>'

H = 'font-weight:800;letter-spacing:-0.8px;color:#fff;line-height:1.04;'
SUB = 'font-size:13px;line-height:1.5;color:rgba(255,255,255,0.72);'
G = f'color:{PL};text-shadow:0 0 18px rgba(95,211,154,0.55);'
S = []

# ---------- 1 CAPA: imagem do Felipe ----------
cover = b64(COVER, 88)
S.append(slide(0, f'''<div style="position:absolute;inset:0;background:url({cover}) center 0/100% auto no-repeat,{BG};"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:300px;background:linear-gradient(to bottom,transparent 0%,rgba(6,17,12,0.85) 38%,{BG} 70%);"></div>''',
f'''<div style="position:absolute;left:26px;right:26px;bottom:50px;z-index:5;">
<span style="display:inline-block;font-size:9.5px;font-weight:600;letter-spacing:2px;color:{PL};padding:4px 10px;border:1px solid rgba(95,211,154,0.4);border-radius:20px;background:rgba(6,17,12,0.6);margin-bottom:10px;">PRA QUEM ATENDE CLIENTE PELO CELULAR</span>
<h1 style="font-size:30px;{H}">Você abriu um negócio pra vender, <span style="{G}">não pra passar o dia respondendo mensagem.</span></h1>
<p style="{SUB}margin-top:8px;">Arrasta e conheça quem responde por você →</p></div>'''))

# ---------- 2 A MENSAGEM CAI NA ÁREA DO CLIENTE ----------
flow = f'''
<div style="position:absolute;left:26px;top:215px;z-index:3;display:flex;flex-direction:column;gap:8px;">{ico("wa",40)}{ico("ig",40)}{ico("ms",40)}</div>
<svg style="position:absolute;left:0;top:0;z-index:2;" width="420" height="525" viewBox="0 0 420 525" fill="none">
<defs><linearGradient id="fl" x1="0" x2="1"><stop offset="0" stop-color="{PL}" stop-opacity="0.1"/><stop offset="1" stop-color="{PL}"/></linearGradient></defs>
<path d="M70 235 C120 235,120 287,168 287" stroke="url(#fl)" stroke-width="2.5"/>
<path d="M70 283 L168 287" stroke="url(#fl)" stroke-width="2.5"/>
<path d="M70 331 C120 331,120 287,168 287" stroke="url(#fl)" stroke-width="2.5"/>
<circle cx="168" cy="287" r="5" fill="{PL}"/><circle cx="168" cy="287" r="11" fill="{PL}" fill-opacity="0.2"/></svg>
<div style="position:absolute;left:176px;right:46px;top:185px;z-index:3;">{glass(f"""
<div style="display:flex;align-items:center;gap:8px;padding:10px 12px;border-bottom:1px solid rgba(255,255,255,0.08);">
<span style="width:8px;height:8px;border-radius:50%;background:{PL};box-shadow:0 0 8px {PL};"></span><span style="font-size:10.5px;font-weight:700;color:#fff;letter-spacing:1px;">SUA ÁREA DO CLIENTE</span></div>
<div style="padding:10px 12px;display:flex;flex-direction:column;gap:7px;">
<div style="display:flex;gap:7px;align-items:center;">{ico("ig",18)}<p style="font-size:11px;color:rgba(255,255,255,0.85);">Vocês têm horário sábado?</p></div>
<div style="align-self:flex-end;max-width:92%;background:linear-gradient(135deg,{P},#2BAA6C);border-radius:12px 12px 3px 12px;padding:7px 10px;box-shadow:0 0 16px rgba(95,211,154,0.35);">
<p style="font-size:11px;color:#fff;line-height:1.35;">Temos sim! 9h ou 10h, qual prefere? 😊</p></div>
<div style="display:flex;align-items:center;gap:6px;"><img src="{FACE}" style="width:18px;height:18px;border-radius:50%;"><span style="font-size:9.5px;color:{PL};font-weight:600;">James respondeu em 4s</span></div>
</div>""")}</div>'''
S.append(slide(1, stage("70% 35%") + flow,
f'''<div style="position:absolute;left:26px;right:40px;top:28px;z-index:5;">{tag("01","COMO FUNCIONA")}
<h2 style="font-size:27px;{H}">A mensagem chega. <span style="{G}">A IA já está respondendo.</span></h2></div>
<div style="position:absolute;left:26px;right:40px;bottom:52px;z-index:5;"><p style="{SUB}">WhatsApp, Direct ou Messenger: tudo cai num lugar só, a sua área do cliente na StudioWeb360. O James lê, entende e responde na hora, com as informações do seu negócio.</p></div>'''))

# ---------- 3 QUALIFICA ----------
def chip(t, hot=False):
    c = GOLD if hot else PL
    return f'<span style="font-size:10.5px;font-weight:600;color:{c};padding:5px 9px;border-radius:20px;border:1px solid {c}55;background:{c}14;white-space:nowrap;">{t}</span>'
ring_deg = 0.92 * 360
gauge = f'''<div style="position:absolute;left:50%;top:92px;transform:translateX(-50%);z-index:3;width:188px;height:188px;border-radius:50%;
background:conic-gradient({GOLD} 0deg,{PL} {ring_deg}deg,rgba(255,255,255,0.08) {ring_deg}deg);box-shadow:0 0 50px rgba(242,196,109,0.35);display:flex;align-items:center;justify-content:center;">
<div style="width:160px;height:160px;border-radius:50%;background:radial-gradient(circle at 50% 35%,#13261C,{BG});display:flex;flex-direction:column;align-items:center;justify-content:center;">
<span style="font-size:11px;font-weight:700;letter-spacing:2px;color:{GOLD};">LEAD QUENTE 🔥</span>
<span style="font-size:58px;font-weight:800;color:#fff;line-height:1;letter-spacing:-2px;text-shadow:0 0 24px rgba(242,196,109,0.5);">92</span>
<span style="font-size:10px;color:rgba(255,255,255,0.6);">pronto pra comprar</span></div></div>
<div style="position:absolute;left:22px;right:22px;top:292px;z-index:3;display:flex;flex-wrap:wrap;justify-content:center;gap:6px;">
{chip("🎯 Quer: corte + escova")}{chip("📅 Sábado de manhã")}{chip("💰 Até R$ 150", True)}{chip("📍 São Bernardo")}</div>'''
S.append(slide(2, stage("50% 34%", "rgba(242,196,109,0.22)") + orbit(210, 186, 150, 48, -12, 0.45) + gauge,
f'''<div style="position:absolute;left:26px;right:40px;top:26px;z-index:5;">{tag("02","QUALIFICA O CLIENTE")}</div>
<div style="position:absolute;left:26px;right:40px;bottom:52px;z-index:5;">
<h2 style="font-size:25px;{H}">Curioso ou cliente pronto? <span style="{G}">Ele descobre na conversa.</span></h2>
<p style="{SUB}margin-top:8px;">Enquanto atende, o James entende o que a pessoa quer, quando e quanto pode pagar, e te mostra quem está quente pra fechar.</p></div>'''))

# ---------- 4 CRM AO VIVO ----------
def field(lbl, val, new=False):
    hl = f"background:rgba(95,211,154,0.14);box-shadow:0 0 0 1px {PL}66 inset;" if new else "background:rgba(255,255,255,0.04);"
    nb = f'<span style="font-size:8.5px;font-weight:700;color:{BG};background:{PL};padding:1px 5px;border-radius:4px;margin-left:6px;">NOVO</span>' if new else ''
    return f'<div style="padding:7px 10px;border-radius:9px;{hl}"><p style="font-size:8.5px;letter-spacing:1px;color:rgba(255,255,255,0.45);font-weight:600;">{lbl}</p><p style="font-size:11.5px;color:#fff;font-weight:600;">{val}{nb}</p></div>'
stages = "".join(f'<span style="flex:1;height:5px;border-radius:3px;background:{PL if k<3 else "rgba(255,255,255,0.12)"};{"box-shadow:0 0 8px "+PL+";" if k<3 else ""}"></span>' for k in range(4))
crm = f'''<div style="position:absolute;left:22px;width:150px;top:150px;z-index:3;display:flex;flex-direction:column;gap:7px;">
<div style="align-self:flex-start;background:rgba(255,255,255,0.08);border-radius:12px 12px 12px 3px;padding:7px 10px;"><p style="font-size:10.5px;color:rgba(255,255,255,0.9);">Sou a Marina, queria corte e escova</p></div>
<div style="align-self:flex-end;background:linear-gradient(135deg,{P},#2BAA6C);border-radius:12px 12px 3px 12px;padding:7px 10px;"><p style="font-size:10.5px;color:#fff;">Oi Marina! Sábado 10h serve?</p></div>
<div style="align-self:flex-start;background:rgba(255,255,255,0.08);border-radius:12px 12px 12px 3px;padding:7px 10px;"><p style="font-size:10.5px;color:rgba(255,255,255,0.9);">Serve! 🙌</p></div></div>
<svg style="position:absolute;left:0;top:0;z-index:2;" width="420" height="525"><path d="M174 220 L198 220" stroke="{PL}" stroke-width="2" stroke-dasharray="3 4"/><circle cx="200" cy="220" r="4" fill="{PL}"/></svg>
<div style="position:absolute;left:206px;right:46px;top:120px;z-index:3;">{glass(f"""
<div style="display:flex;align-items:center;gap:8px;padding:9px 11px;border-bottom:1px solid rgba(255,255,255,0.08);"><span style="font-size:10.5px;font-weight:700;color:#fff;letter-spacing:1px;">CRM</span>
<span style="margin-left:auto;font-size:9px;font-weight:700;color:#FF6B6B;display:flex;align-items:center;gap:4px;"><span style="width:6px;height:6px;border-radius:50%;background:#FF6B6B;box-shadow:0 0 8px #FF6B6B;"></span>AO VIVO</span></div>
<div style="padding:8px;display:flex;flex-direction:column;gap:5px;">
{field("CLIENTE","Marina Souza")}{field("INTERESSE","Corte + escova", True)}{field("ETAPA","Agendado", True)}
<div style="padding:4px 4px 2px;"><div style="display:flex;gap:4px;">{stages}</div></div></div>""")}</div>'''
S.append(slide(3, stage("60% 40%") + crm,
f'''<div style="position:absolute;left:26px;right:40px;top:28px;z-index:5;">{tag("03","CRM ATUALIZADO")}
<h2 style="font-size:27px;{H}">A conversa acontece. <span style="{G}">O CRM se preenche sozinho.</span></h2></div>
<div style="position:absolute;left:26px;right:40px;bottom:52px;z-index:5;"><p style="{SUB}">Nome, interesse e etapa da venda são atualizados durante o atendimento. Nada de copiar conversa pra planilha no fim do dia.</p></div>'''))

# ---------- 5 AGENDAMENTO ----------
days = ["SEG","TER","QUA","QUI","SEX","SÁB"]
cols = ""
for d_i, d in enumerate(days):
    cells = ""
    for h in range(4):
        busy = (d_i * 3 + h) % 4 == 0
        if d == "SÁB" and h == 1:
            cells += f'<div style="height:40px;border-radius:7px;background:linear-gradient(160deg,{PL},{P});box-shadow:0 0 22px {PL}aa;display:flex;flex-direction:column;align-items:center;justify-content:center;"><span style="font-size:10px;font-weight:800;color:{BG};">10:00</span><span style="font-size:8px;font-weight:700;color:{BG};">Marina</span></div>'
        else:
            cells += f'<div style="height:40px;border-radius:7px;background:{"rgba(255,255,255,0.10)" if busy else "rgba(255,255,255,0.03)"};border:1px solid rgba(255,255,255,0.06);"></div>'
    cols += f'<div style="flex:1;display:flex;flex-direction:column;gap:5px;"><span style="font-size:9px;font-weight:700;text-align:center;color:{PL if d=="SÁB" else "rgba(255,255,255,0.5)"};">{d}</span>{cells}</div>'
cal = f'''<div style="position:absolute;left:24px;right:24px;top:154px;z-index:3;transform:perspective(700px) rotateX(14deg);transform-origin:50% 100%;">{glass(f'<div style="padding:12px;display:flex;gap:5px;">{cols}</div>')}</div>
<div style="position:absolute;right:30px;top:128px;z-index:4;font-size:9.5px;font-weight:700;color:#fff;padding:5px 10px;border-radius:20px;background:#4285F4;box-shadow:0 0 16px rgba(66,133,244,0.6);">✓ Google Agenda sincronizada</div>'''
S.append(slide(4, stage("72% 60%") + cal,
f'''<div style="position:absolute;left:26px;right:40px;top:26px;z-index:5;">{tag("04","AGENDAMENTO AUTOMÁTICO")}
<h2 style="font-size:27px;{H}">Ele marca o horário. <span style="{G}">Sua agenda já sabe.</span></h2></div>
<div style="position:absolute;left:26px;right:40px;bottom:52px;z-index:5;"><p style="{SUB}">O James vê os horários livres, oferece ao cliente, confirma e lança na sua Google Agenda. Sem horário duplicado, sem caderninho.</p></div>'''))

# ---------- 6 PIX ----------
random.seed(7); N = 21
def finder(x, y): return [(x+i, y+j) for i in range(7) for j in range(7) if i in (0,6) or j in (0,6) or (2<=i<=4 and 2<=j<=4)]
fixed = set(finder(0,0) + finder(14,0) + finder(0,14))
reserved = {(x+i, y+j) for (x,y) in [(0,0),(14,0),(0,14)] for i in range(-1,8) for j in range(-1,8)}
cells = ""
c = 6
for x in range(N):
    for y in range(N):
        on = (x,y) in fixed or ((x,y) not in reserved and random.random() < 0.5)
        if on: cells += f'<rect x="{x*c}" y="{y*c}" width="{c}" height="{c}" fill="{BG}"/>'
qr = f'<svg width="{N*c}" height="{N*c}" viewBox="0 0 {N*c} {N*c}">{cells}</svg>'
pix = f'''<div style="position:absolute;left:50%;top:84px;transform:translateX(-50%);z-index:3;display:flex;align-items:center;gap:16px;">
<div style="padding:10px;background:#fff;border-radius:14px;box-shadow:0 0 0 4px rgba(95,211,154,0.35),0 0 50px rgba(95,211,154,0.55);">{qr}</div>
<div><p style="font-size:10px;letter-spacing:2px;font-weight:700;color:{PL};">PIX ENVIADO</p>
<p style="font-size:33px;font-weight:800;color:#fff;letter-spacing:-1.5px;white-space:nowrap;line-height:1;text-shadow:0 0 24px rgba(95,211,154,0.5);">R$ 178<span style="font-size:22px;">,00</span></p>
<p style="font-size:10.5px;color:rgba(255,255,255,0.6);margin-top:4px;">2 kits de presente</p></div></div>
<div style="position:absolute;left:30px;right:50px;top:250px;z-index:3;">{glass(f'<div style="padding:9px 12px;display:flex;align-items:center;gap:9px;">{ico("wa",22)}<div style="flex:1;min-width:0;"><p style="font-size:9px;letter-spacing:1px;color:rgba(255,255,255,0.5);font-weight:600;">PIX COPIA E COLA</p><p style="font-size:10.5px;color:#fff;font-family:monospace;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">00020126580014br.gov.bcb.pix0136a3f9…</p></div><span style="font-size:9px;font-weight:700;color:{BG};background:{PL};padding:3px 8px;border-radius:6px;">COPIAR</span></div>')}</div>'''
S.append(slide(5, stage("50% 30%") + pix,
f'''<div style="position:absolute;left:26px;right:40px;top:26px;z-index:5;">{tag("05","COBRANÇA AUTOMÁTICA")}</div>
<div style="position:absolute;left:26px;right:40px;bottom:52px;z-index:5;">
<h2 style="font-size:27px;{H}">Fechou o pedido? <span style="{G}">O Pix já foi junto.</span></h2>
<p style="{SUB}margin-top:8px;">O James manda o valor certo e o Pix copia e cola no WhatsApp, no Direct ou no Messenger. Você só confere o pagamento no banco.</p></div>'''))

# ---------- 7 CTA ----------
def pill(t): return f'<span style="font-size:11.5px;font-weight:600;color:#fff;padding:6px 11px;border-radius:20px;background:rgba(255,255,255,0.08);border:1px solid rgba(95,211,154,0.4);">{t}</span>'
S.append(slide(6, stage("50% 30%", "rgba(30,138,85,0.75)") + orbit(210, 150, 170, 44, -8, 0.5) +
f'<img src="{jx("sorriso", True)}" style="position:absolute;left:50%;transform:translateX(-50%);top:18px;height:220px;z-index:2;-webkit-mask-image:linear-gradient(to bottom,#000 70%,transparent);mask-image:linear-gradient(to bottom,#000 70%,transparent);">',
f'''<div style="position:absolute;left:26px;right:26px;top:212px;z-index:5;text-align:center;">
<h2 style="font-size:24px;{H}">Quantos apps você usa pra responder cliente hoje?</h2>
<div style="display:flex;justify-content:center;gap:6px;margin-top:10px;">{pill("1️⃣ Só um")}{pill("2️⃣ Dois")}{pill("3️⃣ Todos")}</div>
<p style="font-size:12px;color:rgba(255,255,255,0.8);margin-top:8px;">Responde nos comentários 👇</p>
<div style="margin-top:14px;padding:11px 13px;border-radius:16px;background:linear-gradient(135deg,{P},#2BAA6C);box-shadow:0 0 30px rgba(95,211,154,0.45);display:flex;align-items:center;gap:10px;text-align:left;">
<img src="{FACE}" style="width:38px;height:38px;border-radius:50%;border:2px solid #fff;"><div style="flex:1;"><p style="font-size:13px;font-weight:800;color:#fff;">Siga @studioweb360.ia</p>
<p style="font-size:10.5px;color:rgba(255,255,255,0.88);line-height:1.3;">Toda semana uma dica pra atender e vender mais</p></div>
<span style="font-size:11px;font-weight:800;color:{PD};background:#fff;padding:6px 12px;border-radius:8px;">Seguir</span></div>
<p style="font-size:11.5px;color:rgba(255,255,255,0.75);margin-top:10px;">Quer no seu negócio? Comente <b style="color:{PL};">JAMES</b> · studioweb360.com.br</p></div>''', last=True))

faces = ""
for w in (400, 600, 700, 800):
    b = base64.b64encode((BRAND / f'fonts/bricolage-grotesque-latin-{w}-normal.woff2').read_bytes()).decode()
    faces += f"@font-face{{font-family:'Bricolage Grotesque';font-weight:{w};src:url(data:font/woff2;base64,{b}) format('woff2');}}\n"
html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>James em 3 apps</title><style>{faces}
*{{margin:0;padding:0;box-sizing:border-box;}} body{{font-family:'Bricolage Grotesque',sans-serif;background:#111;}}
.ig-frame{{width:420px;}} .carousel-viewport{{width:420px;height:525px;overflow:hidden;}} .carousel-track{{display:flex;}}
.slide{{min-width:420px;width:420px;height:525px;position:relative;overflow:hidden;background:{BG};}}
</style></head><body><div class="ig-frame"><div class="ig-header"></div><div class="carousel-viewport"><div class="carousel-track">{"".join(S)}</div></div>
<div class="ig-dots"></div><div class="ig-actions"></div><div class="ig-caption"></div></div></body></html>'''
OUT.write_text(html, encoding="utf-8"); print(OUT)
