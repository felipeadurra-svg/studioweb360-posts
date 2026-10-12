import base64, sys, random, io
from pathlib import Path
from PIL import Image

BRAND = Path(sys.argv[1]); OUT = Path(sys.argv[2])
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

RED = "#E5484D"
def pixmark(s=40, col=None):
    col = col or PL
    return f'''<svg width="{s}" height="{s}" viewBox="0 0 40 40" fill="none"><g transform="rotate(45 20 20)">
<rect x="9" y="9" width="22" height="22" rx="6" stroke="{col}" stroke-width="3.2"/><rect x="16" y="16" width="8" height="8" rx="2" fill="{col}"/></g></svg>'''
def bin_(t, me=False, extra=""):
    if me:
        return f'<div style="align-self:flex-end;max-width:84%;background:linear-gradient(135deg,{P},#2BAA6C);border-radius:13px 13px 3px 13px;padding:7px 10px;box-shadow:0 0 16px rgba(95,211,154,0.3);{extra}"><p style="font-size:11px;color:#fff;line-height:1.35;">{t}</p></div>'
    return f'<div style="align-self:flex-start;max-width:84%;background:rgba(255,255,255,0.09);border-radius:13px 13px 13px 3px;padding:7px 10px;{extra}"><p style="font-size:11px;color:rgba(255,255,255,0.92);line-height:1.35;">{t}</p></div>'
def ts(t, c="rgba(255,255,255,0.4)"): return f'<p style="font-size:9px;color:{c};text-align:center;font-weight:600;letter-spacing:1px;">{t}</p>'

# ---------- 1 CAPA ----------
coin = f'''<div style="position:absolute;left:34px;top:70px;z-index:3;width:170px;height:170px;border-radius:50%;
background:radial-gradient(circle at 35% 30%,#1c3a2a,{BG} 70%);border:1.5px solid {PL}88;box-shadow:0 0 70px rgba(95,211,154,0.55),0 0 0 10px rgba(95,211,154,0.06);display:flex;align-items:center;justify-content:center;">{pixmark(96)}</div>
<div style="position:absolute;left:30px;top:252px;z-index:5;">{glass(f'<div style="padding:7px 10px;display:flex;align-items:center;gap:7px;">{ico("wa",20)}<div><p style="font-size:8.5px;color:rgba(255,255,255,0.55);font-weight:600;letter-spacing:1px;">JAMES · AGORA</p><p style="font-size:11px;color:#fff;font-weight:700;">Pix de R$ 178,00 enviado ✓</p></div></div>')}</div>
<img src="{jx("corpo-inteiro/corpo-celular-andando", True)}" style="position:absolute;right:18px;top:40px;height:380px;z-index:3;-webkit-mask-image:linear-gradient(to bottom,#000 78%,transparent);mask-image:linear-gradient(to bottom,#000 78%,transparent);">'''
S.append(slide(0, stage("38% 28%", "rgba(30,138,85,0.7)") + orbit(130, 160, 150, 40, -14, 0.5) + coin +
f'<div style="position:absolute;left:0;right:0;bottom:0;height:250px;z-index:4;background:linear-gradient(to bottom,transparent,rgba(6,17,12,0.92) 40%,{BG} 70%);"></div>',
f'''<div style="position:absolute;left:26px;right:26px;bottom:50px;z-index:5;">
<span style="display:inline-block;font-size:9.5px;font-weight:600;letter-spacing:2px;color:{PL};padding:4px 10px;border:1px solid rgba(95,211,154,0.4);border-radius:20px;background:rgba(6,17,12,0.6);margin-bottom:10px;">PRA QUEM VENDE PELO WHATSAPP</span>
<h1 style="font-size:30px;{H}">Quantas vendas você perdeu <span style="{G}">esperando pra mandar a chave Pix?</span></h1>
<p style="{SUB}margin-top:8px;">Arrasta e veja o James cobrando por você →</p></div>'''))

# ---------- 2 O PROBLEMA ----------
chat = f'''<div style="position:absolute;left:46px;right:46px;top:108px;z-index:3;">{glass(f"""
<div style="padding:12px;display:flex;flex-direction:column;gap:7px;">
{ts("14:02")}{bin_("Fechado! Me passa o Pix que já pago 😊")}
{ts("15:10 · SEM RESPOSTA", RED)}{bin_("Oi? Ainda está disponível?")}
{ts("16:47")}{bin_("Desculpa a demora, estava atendendo na loja!", True)}
{bin_("Ah, já comprei em outro lugar 😕", extra=f"box-shadow:0 0 0 1px {RED}88 inset,0 0 18px rgba(229,72,77,0.3);")}
</div>""")}</div>
<img src="{jx("expressoes/preocupado", True)}" style="position:absolute;right:10px;top:300px;height:120px;z-index:4;">'''
S.append(slide(1, stage("50% 45%", "rgba(229,72,77,0.22)") + chat,
f'''<div style="position:absolute;left:26px;right:40px;top:26px;z-index:5;">
<h2 style="font-size:26px;{H}">O cliente queria pagar. <span style="color:{RED};text-shadow:0 0 18px rgba(229,72,77,0.5);">Ninguém mandou o Pix.</span></h2></div>
<div style="position:absolute;left:26px;right:110px;bottom:52px;z-index:5;"><p style="{SUB}">Toda venda que esfria esperando a chave é dinheiro que vai pro concorrente.</p></div>'''))

# ---------- 3 CONFIGURA UMA VEZ ----------
toggle = f'<span style="width:34px;height:19px;border-radius:12px;background:{PL};box-shadow:0 0 12px {PL};position:relative;display:inline-block;"><span style="position:absolute;right:2px;top:2px;width:15px;height:15px;border-radius:50%;background:#fff;"></span></span>'
panel = f'''<div style="position:absolute;left:26px;right:110px;top:150px;z-index:3;">{glass(f"""
<div style="display:flex;align-items:center;gap:8px;padding:10px 12px;border-bottom:1px solid rgba(255,255,255,0.08);">{pixmark(18)}<span style="font-size:10.5px;font-weight:700;color:#fff;letter-spacing:1px;">RECEBER POR PIX</span><span style="margin-left:auto;">{toggle}</span></div>
<div style="padding:10px 12px;display:flex;flex-direction:column;gap:7px;">
<div style="padding:7px 10px;border-radius:9px;background:rgba(95,211,154,0.12);box-shadow:0 0 0 1px {PL}66 inset;"><p style="font-size:8.5px;letter-spacing:1px;color:rgba(255,255,255,0.45);font-weight:600;">SUA CHAVE PIX</p><p style="font-size:11.5px;color:#fff;font-weight:600;">contato@sualoja.com.br</p></div>
<div style="padding:7px 10px;border-radius:9px;background:rgba(255,255,255,0.04);"><p style="font-size:8.5px;letter-spacing:1px;color:rgba(255,255,255,0.45);font-weight:600;">CANAIS</p><div style="display:flex;gap:6px;margin-top:4px;">{ico("wa",22)}{ico("ig",22)}{ico("ms",22)}</div></div>
<p style="font-size:9.5px;color:{PL};font-weight:600;">✓ Salvo · o James já pode cobrar</p></div>""")}</div>
<img src="{jx("expressoes/notebook-2", True)}" style="position:absolute;right:8px;top:250px;height:150px;z-index:4;">'''
S.append(slide(2, stage("35% 50%") + panel,
f'''<div style="position:absolute;left:26px;right:40px;top:26px;z-index:5;">{tag("01","CONFIGURA UMA VEZ")}
<h2 style="font-size:26px;{H}">Cadastre sua chave. <span style="{G}">Pronto, é só isso.</span></h2></div>
<div style="position:absolute;left:26px;right:40px;bottom:52px;z-index:5;"><p style="{SUB}">No painel da StudioWeb360 você liga o "Receber por Pix" e informa a sua chave. O dinheiro cai direto na sua conta.</p></div>'''))

# ---------- 4 CLIENTE FECHA ----------
resumo = f'''<div style="background:linear-gradient(135deg,{P},#2BAA6C);border-radius:13px 13px 3px 13px;padding:9px 11px;align-self:flex-end;width:82%;box-shadow:0 0 20px rgba(95,211,154,0.35);">
<p style="font-size:9px;letter-spacing:1px;font-weight:700;color:rgba(255,255,255,0.8);">RESUMO DO PEDIDO</p>
<div style="display:flex;justify-content:space-between;margin-top:4px;"><span style="font-size:11px;color:#fff;">2× Kit presente</span><span style="font-size:11px;color:#fff;">R$ 158,00</span></div>
<div style="display:flex;justify-content:space-between;"><span style="font-size:11px;color:#fff;">Entrega</span><span style="font-size:11px;color:#fff;">R$ 20,00</span></div>
<div style="height:1px;background:rgba(255,255,255,0.3);margin:5px 0;"></div>
<div style="display:flex;justify-content:space-between;"><span style="font-size:12px;color:#fff;font-weight:800;">Total</span><span style="font-size:12px;color:#fff;font-weight:800;">R$ 178,00</span></div></div>'''
order = f'''<div style="position:absolute;left:40px;right:40px;top:120px;z-index:3;display:flex;flex-direction:column;gap:8px;">
<div style="display:flex;align-items:center;gap:6px;">{ico("ig",18)}<span style="font-size:9.5px;color:rgba(255,255,255,0.55);font-weight:600;letter-spacing:1px;">DIRECT · 21:38</span></div>
{bin_("Quero 2 kits de presente, com entrega no Rudge Ramos")}
{resumo}
{bin_("Isso! Como eu pago?")}</div>'''
S.append(slide(3, stage("70% 45%") + orbit(210, 270, 190, 60, 10, 0.35) + order,
f'''<div style="position:absolute;left:26px;right:40px;top:26px;z-index:5;">{tag("02","O CLIENTE FECHA")}
<h2 style="font-size:26px;{H}">Ele monta o pedido <span style="{G}">e soma o valor certo.</span></h2></div>
<div style="position:absolute;left:26px;right:40px;bottom:52px;z-index:5;"><p style="{SUB}">Mesmo às 21h38, com você fora. O James confirma itens, entrega e total antes de cobrar.</p></div>'''))

# ---------- 5 PIX NA CONVERSA ----------
phone = f'''<div style="position:absolute;left:50%;top:92px;transform:translateX(-50%);width:244px;z-index:3;border-radius:30px;padding:9px;background:linear-gradient(160deg,#1b2a22,#0a130e);border:1px solid rgba(95,211,154,0.35);box-shadow:0 0 60px rgba(95,211,154,0.35),0 24px 50px rgba(0,0,0,0.6);">
<div style="border-radius:22px;background:#0B1712;padding:12px 10px 14px;display:flex;flex-direction:column;gap:8px;">
<div style="display:flex;align-items:center;gap:7px;padding-bottom:7px;border-bottom:1px solid rgba(255,255,255,0.07);"><img src="{FACE}" style="width:22px;height:22px;border-radius:50%;"><span style="font-size:10.5px;color:#fff;font-weight:700;">Sua Loja</span><span style="margin-left:auto;">{ico("wa",18)}</span></div>
{bin_("Perfeito! O total fica R$ 178,00. Vou te mandar o Pix copia e cola na próxima mensagem 👇", True)}
<div style="align-self:flex-end;width:88%;background:linear-gradient(135deg,{P},#2BAA6C);border-radius:13px 13px 3px 13px;padding:8px 10px;box-shadow:0 0 0 2px {PL},0 0 26px {PL}aa;">
<p style="font-size:10px;color:#fff;font-family:monospace;line-height:1.35;word-break:break-all;">00020126580014br.gov.bcb.pix0136a3f9c2e1…6304B1F7</p></div>
</div></div>
<div style="position:absolute;right:16px;top:300px;z-index:4;padding:6px 10px;border-radius:20px;background:{BG};border:1px solid {PL};box-shadow:0 0 16px {PL}88;font-size:9.5px;font-weight:700;color:{PL};">Sozinho na mensagem: 1 toque pra copiar</div>'''
S.append(slide(4, stage("50% 38%", "rgba(30,138,85,0.65)") + phone,
f'''<div style="position:absolute;left:26px;right:40px;top:26px;z-index:5;">{tag("03","O PIX VAI NA CONVERSA")}</div>
<div style="position:absolute;left:26px;right:40px;bottom:52px;z-index:5;">
<h2 style="font-size:26px;{H}">Valor numa mensagem, <span style="{G}">Pix na outra.</span></h2>
<p style="{SUB}margin-top:6px;">O código vai sozinho pro cliente copiar sem erro e pagar no app do banco.</p></div>'''))

# ---------- 6 TRÊS APPS + VOCÊ CONFERE ----------
hub = f'''<div style="position:absolute;left:50%;top:112px;transform:translateX(-50%);z-index:3;width:96px;height:96px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#1c3a2a,{BG});border:1.5px solid {PL};box-shadow:0 0 50px rgba(95,211,154,0.6);display:flex;align-items:center;justify-content:center;">{pixmark(54)}</div>
<div style="position:absolute;left:58px;top:96px;z-index:4;">{ico("wa",46)}</div>
<div style="position:absolute;right:58px;top:96px;z-index:4;">{ico("ig",46)}</div>
<div style="position:absolute;left:50%;transform:translateX(-50%);top:226px;z-index:4;">{ico("ms",46)}</div>
<div style="position:absolute;left:30px;right:50px;top:296px;z-index:3;">{glass(f'<div style="padding:10px 12px;display:flex;align-items:center;gap:10px;"><span style="width:30px;height:30px;border-radius:9px;background:rgba(242,196,109,0.15);border:1px solid {GOLD}88;display:flex;align-items:center;justify-content:center;font-size:15px;">🏦</span><div><p style="font-size:11px;color:#fff;font-weight:700;">Quem confirma o pagamento é você</p><p style="font-size:10px;color:rgba(255,255,255,0.6);line-height:1.35;">O James nunca diz "pago". Sua equipe confere no banco e segue o pedido.</p></div></div>')}</div>'''
S.append(slide(5, stage("50% 30%") + orbit(210, 160, 160, 62, 0, 0.5) + hub,
f'''<div style="position:absolute;left:26px;right:40px;top:26px;z-index:5;">{tag("04","EM TODO LUGAR")}</div>
<div style="position:absolute;left:26px;right:40px;bottom:52px;z-index:5;">
<h2 style="font-size:25px;{H}">WhatsApp, Direct ou Messenger: <span style="{G}">cobra do mesmo jeito.</span></h2></div>'''))

# ---------- 7 CTA ----------
def pill(t): return f'<span style="font-size:11.5px;font-weight:600;color:#fff;padding:6px 11px;border-radius:20px;background:rgba(255,255,255,0.08);border:1px solid rgba(95,211,154,0.4);">{t}</span>'
S.append(slide(6, stage("50% 26%", "rgba(30,138,85,0.75)") + orbit(210, 120, 170, 44, -8, 0.5) +
f'<img src="{jx("expressoes/comemorando-2", True)}" style="position:absolute;left:50%;transform:translateX(-50%);top:22px;height:180px;z-index:2;filter:drop-shadow(0 0 24px rgba(95,211,154,0.4));">',
f'''<div style="position:absolute;left:26px;right:26px;top:206px;z-index:5;text-align:center;">
<h2 style="font-size:23px;{H}">Como a maioria dos seus clientes paga hoje?</h2>
<div style="display:flex;justify-content:center;gap:6px;margin-top:10px;">{pill("1️⃣ Pix")}{pill("2️⃣ Cartão")}{pill("3️⃣ Dinheiro")}</div>
<p style="font-size:12px;color:rgba(255,255,255,0.8);margin-top:8px;">Responde nos comentários 👇</p>
<div style="margin-top:14px;padding:11px 13px;border-radius:16px;background:linear-gradient(135deg,{P},#2BAA6C);box-shadow:0 0 30px rgba(95,211,154,0.45);display:flex;align-items:center;gap:10px;text-align:left;">
<img src="{FACE}" style="width:38px;height:38px;border-radius:50%;border:2px solid #fff;"><div style="flex:1;"><p style="font-size:13px;font-weight:800;color:#fff;">Siga @studioweb360.ia</p>
<p style="font-size:10.5px;color:rgba(255,255,255,0.88);line-height:1.3;">Toda semana uma função do James por dentro</p></div>
<span style="font-size:11px;font-weight:800;color:{PD};background:#fff;padding:6px 12px;border-radius:8px;">Seguir</span></div>
<p style="font-size:11.5px;color:rgba(255,255,255,0.75);margin-top:10px;">Quer no seu negócio? Comente <b style="color:{PL};">JAMES</b> · studioweb360.com.br</p></div>''', last=True))

faces = ""
for w in (400, 600, 700, 800):
    b = base64.b64encode((BRAND / f'fonts/bricolage-grotesque-latin-{w}-normal.woff2').read_bytes()).decode()
    faces += f"@font-face{{font-family:'Bricolage Grotesque';font-weight:{w};src:url(data:font/woff2;base64,{b}) format('woff2');}}\n"
html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>James cobra no Pix</title><style>{faces}
*{{margin:0;padding:0;box-sizing:border-box;}} body{{font-family:'Bricolage Grotesque',sans-serif;background:#111;}}
.ig-frame{{width:420px;}} .carousel-viewport{{width:420px;height:525px;overflow:hidden;}} .carousel-track{{display:flex;}}
.slide{{min-width:420px;width:420px;height:525px;position:relative;overflow:hidden;background:{BG};}}
</style></head><body><div class="ig-frame"><div class="ig-header"></div><div class="carousel-viewport"><div class="carousel-track">{"".join(S)}</div></div>
<div class="ig-dots"></div><div class="ig-actions"></div><div class="ig-caption"></div></div></body></html>'''
OUT.write_text(html, encoding="utf-8"); print(OUT)
