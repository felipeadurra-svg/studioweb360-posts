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

RED = "#E5484D"; GBLUE = "#4285F4"
def bin_(t, me=False, extra=""):
    if me:
        return f'<div style="align-self:flex-end;max-width:84%;background:linear-gradient(135deg,{P},#2BAA6C);border-radius:13px 13px 3px 13px;padding:7px 10px;box-shadow:0 0 16px rgba(95,211,154,0.3);{extra}"><p style="font-size:11px;color:#fff;line-height:1.35;">{t}</p></div>'
    return f'<div style="align-self:flex-start;max-width:84%;background:rgba(255,255,255,0.09);border-radius:13px 13px 13px 3px;padding:7px 10px;{extra}"><p style="font-size:11px;color:rgba(255,255,255,0.92);line-height:1.35;">{t}</p></div>'
def ts(t, c="rgba(255,255,255,0.4)"): return f'<p style="font-size:9px;color:{c};text-align:center;font-weight:600;letter-spacing:1px;">{t}</p>'
def calicon(s=40, col=None):
    col = col or PL
    return f'<svg width="{s}" height="{s}" viewBox="0 0 40 40" fill="none"><rect x="5" y="8" width="30" height="27" rx="6" stroke="{col}" stroke-width="3"/><path d="M5 16h30" stroke="{col}" stroke-width="3"/><path d="M13 4v8M27 4v8" stroke="{col}" stroke-width="3" stroke-linecap="round"/><path d="M14 25l4 4 8-8" stroke="{col}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def chipg(t): return f'<span style="font-size:9.5px;font-weight:700;color:#fff;padding:5px 10px;border-radius:20px;background:{GBLUE};box-shadow:0 0 16px rgba(66,133,244,0.6);white-space:nowrap;">{t}</span>'
def chip(t, c=None):
    c = c or PL
    return f'<span style="font-size:10px;font-weight:600;color:{c};padding:5px 9px;border-radius:20px;border:1px solid {c}55;background:{c}14;white-space:nowrap;">{t}</span>'

# ---------- 1 CAPA ----------
cell = lambda t, on=False: f'<div style="height:30px;border-radius:7px;{"background:linear-gradient(160deg,"+PL+","+P+");box-shadow:0 0 18px "+PL+"aa;" if on else "background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.06);"}display:flex;align-items:center;justify-content:center;font-size:9.5px;font-weight:800;color:{BG if on else "rgba(255,255,255,0.35)"};">{t}</div>'
mini = "".join(cell(t, t in ("10:20","15:00","16:40")) for t in ["09:00","10:20","11:40","14:00","15:00","16:40"])
cover = f'''<div style="position:absolute;left:28px;top:56px;width:186px;z-index:3;transform:perspective(600px) rotateY(12deg);">{glass(f"""
<div style="display:flex;align-items:center;gap:7px;padding:9px 11px;border-bottom:1px solid rgba(255,255,255,0.08);">{calicon(18)}<span style="font-size:10px;font-weight:700;color:#fff;letter-spacing:1px;">SÁBADO, 17</span></div>
<div style="padding:9px;display:grid;grid-template-columns:1fr 1fr;gap:5px;">{mini}</div>""")}</div>
<div style="position:absolute;left:30px;top:250px;z-index:5;">{glass(f'<div style="padding:7px 10px;display:flex;align-items:center;gap:7px;">{ico("wa",20)}<div><p style="font-size:8.5px;color:rgba(255,255,255,0.55);font-weight:600;letter-spacing:1px;">JAMES · AGORA</p><p style="font-size:11px;color:#fff;font-weight:700;">Lembrete enviado pra 6 clientes ✓</p></div></div>')}</div>
<img src="{jx("corpo-inteiro/corpo-tablet", True)}" style="position:absolute;right:14px;top:36px;height:390px;z-index:3;-webkit-mask-image:linear-gradient(to bottom,#000 78%,transparent);mask-image:linear-gradient(to bottom,#000 78%,transparent);">'''
S.append(slide(0, stage("32% 30%", "rgba(30,138,85,0.7)") + orbit(130, 150, 150, 42, -12, 0.45) + cover +
f'<div style="position:absolute;left:0;right:0;bottom:0;height:250px;z-index:4;background:linear-gradient(to bottom,transparent,rgba(6,17,12,0.92) 40%,{BG} 70%);"></div>',
f'''<div style="position:absolute;left:26px;right:26px;bottom:50px;z-index:5;">
<span style="display:inline-block;font-size:9.5px;font-weight:600;letter-spacing:2px;color:{PL};padding:4px 10px;border:1px solid rgba(95,211,154,0.4);border-radius:20px;background:rgba(6,17,12,0.6);margin-bottom:10px;">PRA QUEM TRABALHA COM HORÁRIO MARCADO</span>
<h1 style="font-size:30px;{H}">Quanto custa um horário vazio <span style="{G}">porque o cliente esqueceu?</span></h1>
<p style="{SUB}margin-top:8px;">Arrasta e veja o James cuidando da sua agenda →</p></div>'''))

# ---------- 2 O PROBLEMA ----------
prob = f'''<div style="position:absolute;left:40px;right:40px;top:104px;z-index:3;">{glass(f"""
<div style="padding:12px;display:flex;flex-direction:column;gap:7px;">
{bin_("Me encaixa amanhã às 15h?")}
{bin_("Pode vir! 👍", True)}
{ts("NA AGENDA, 15H JÁ ERA DA CARLA", RED)}
<div style="display:flex;gap:6px;"><div style="flex:1;padding:7px 9px;border-radius:9px;background:rgba(229,72,77,0.14);box-shadow:0 0 0 1px {RED}88 inset;"><p style="font-size:9px;color:{RED};font-weight:700;letter-spacing:1px;">15:00</p><p style="font-size:11px;color:#fff;font-weight:600;">Carla</p></div>
<div style="flex:1;padding:7px 9px;border-radius:9px;background:rgba(229,72,77,0.14);box-shadow:0 0 0 1px {RED}88 inset;"><p style="font-size:9px;color:{RED};font-weight:700;letter-spacing:1px;">15:00</p><p style="font-size:11px;color:#fff;font-weight:600;">Rodrigo</p></div></div>
{ts("E O CLIENTE DAS 10H? NÃO APARECEU.", RED)}
</div>""")}</div>
<img src="{jx("expressoes/confuso", True)}" style="position:absolute;right:8px;top:300px;height:112px;z-index:4;">'''
S.append(slide(1, stage("50% 45%", "rgba(229,72,77,0.22)") + prob,
f'''<div style="position:absolute;left:26px;right:40px;top:26px;z-index:5;">
<h2 style="font-size:26px;{H}">Horário duplicado, <span style="color:{RED};text-shadow:0 0 18px rgba(229,72,77,0.5);">cliente que esquece.</span></h2></div>
<div style="position:absolute;left:26px;right:120px;bottom:52px;z-index:5;"><p style="{SUB}">Agenda no caderno e marcação pelo WhatsApp não conversam. Quem paga é o seu caixa.</p></div>'''))

# ---------- 3 REGRAS ----------
def rule(lbl, val):
    return f'<div style="display:flex;justify-content:space-between;align-items:center;padding:7px 10px;border-radius:9px;background:rgba(255,255,255,0.05);"><span style="font-size:10px;color:rgba(255,255,255,0.6);">{lbl}</span><span style="font-size:11px;color:#fff;font-weight:700;">{val}</span></div>'
rules = f'''<div style="position:absolute;left:26px;right:112px;top:128px;z-index:3;">{glass(f"""
<div style="display:flex;align-items:center;gap:8px;padding:10px 12px;border-bottom:1px solid rgba(255,255,255,0.08);">{calicon(18)}<span style="font-size:10.5px;font-weight:700;color:#fff;letter-spacing:1px;">REGRAS DA AGENDA</span></div>
<div style="padding:9px;display:flex;flex-direction:column;gap:5px;">
{rule("Expediente","Seg–Sáb · 9h às 18h")}{rule("Almoço","12h às 13h")}{rule("Corte + escova","1h20")}{rule("Antecedência mínima","2 horas")}{rule("Folgas e feriados","Bloqueados")}</div>""")}</div>
<img src="{jx("expressoes/prancheta", True)}" style="position:absolute;right:6px;top:268px;height:140px;z-index:4;">'''
S.append(slide(2, stage("35% 50%") + rules,
f'''<div style="position:absolute;left:26px;right:40px;top:26px;z-index:5;">{tag("01","VOCÊ DEFINE AS REGRAS")}
<h2 style="font-size:26px;{H}">Seu expediente, <span style="{G}">do seu jeito.</span></h2></div>
<div style="position:absolute;left:26px;right:40px;bottom:52px;z-index:5;"><p style="{SUB}">No painel você cadastra horários, duração de cada serviço, pausas e folgas. O James nunca marca fora disso.</p></div>'''))

# ---------- 4 MARCA NA CONVERSA ----------
slots = "".join(f'<span style="font-size:10.5px;font-weight:700;color:{BG if s=="10:20" else "#fff"};padding:5px 10px;border-radius:8px;background:{PL if s=="10:20" else "rgba(255,255,255,0.12)"};{"box-shadow:0 0 14px "+PL+";" if s=="10:20" else ""}">{s}</span>' for s in ["09:00","10:20","11:40"])
book = f'''<div style="position:absolute;left:38px;right:38px;top:136px;z-index:3;display:flex;flex-direction:column;gap:8px;">
<div style="display:flex;align-items:center;gap:6px;">{ico("wa",18)}<span style="font-size:9.5px;color:rgba(255,255,255,0.55);font-weight:600;letter-spacing:1px;">WHATSAPP · 22:14</span></div>
{bin_("Oi! Tem horário amanhã de manhã pra corte e escova?")}
<div style="align-self:flex-end;width:84%;background:linear-gradient(135deg,{P},#2BAA6C);border-radius:13px 13px 3px 13px;padding:8px 10px;box-shadow:0 0 16px rgba(95,211,154,0.3);">
<p style="font-size:11px;color:#fff;line-height:1.35;margin-bottom:6px;">Tenho estes horários livres amanhã:</p><div style="display:flex;gap:5px;">{slots}</div></div>
{bin_("10h20!")}
{bin_("Marcado, Marina! Amanhã às 10h20 ✅", True)}
<div style="align-self:flex-end;">{chipg("✓ Lançado na Google Agenda")}</div></div>'''
S.append(slide(3, stage("70% 45%") + orbit(210, 270, 190, 60, 10, 0.35) + book,
f'''<div style="position:absolute;left:26px;right:40px;top:26px;z-index:5;">{tag("02","MARCA NA CONVERSA")}
<h2 style="font-size:26px;{H}">Ele mostra o que está livre <span style="{G}">e já marca.</span></h2></div>
<div style="position:absolute;left:26px;right:40px;bottom:52px;z-index:5;"><p style="{SUB}">Até às 22h, com você descansando. Sem horário duplicado: o que já está ocupado nem aparece.</p></div>'''))

# ---------- 5 LEMBRA E REMARCA ----------
remind = f'''<div style="position:absolute;left:36px;right:36px;top:110px;z-index:3;">{glass(f"""
<div style="padding:12px;display:flex;flex-direction:column;gap:7px;">
{ts("VÉSPERA · 18:00")}
{bin_("Oi Marina! Lembrete: amanhã às 10h20 😊<br>Responda <b>1</b> pra confirmar ou <b>2</b> pra remarcar.", True)}
{bin_("2")}
{bin_("Sem problema! Tenho amanhã às 14h ou 15h20. Qual fica melhor?", True)}
{bin_("15h20")}
{bin_("Remarcado pra 15h20 ✅", True)}
</div>""")}</div>
<div style="position:absolute;left:36px;right:36px;top:392px;z-index:4;display:flex;gap:6px;flex-wrap:wrap;justify-content:center;">{chip("🔓 10h20 liberado na agenda", GOLD)}{chip("🎥 Online? Link do Meet enviado")}</div>'''
S.append(slide(4, stage("50% 38%", "rgba(30,138,85,0.6)") + remind,
f'''<div style="position:absolute;left:26px;right:40px;top:26px;z-index:5;">{tag("03","LEMBRA E REMARCA")}
<h2 style="font-size:24px;{H}">Lembrete na véspera. <span style="{G}">Remarcação sem você.</span></h2></div>'''))

# ---------- 6 CENTRO DE GESTÃO ----------
days = ["SEG","TER","QUA","QUI","SEX","SÁB"]
import itertools
cols = ""
pattern = {0:[1,0,2,0],1:[0,1,1,0],2:[2,1,0,1],3:[0,1,0,2],4:[1,1,0,1],5:[1,2,1,1]}
for d_i, d in enumerate(days):
    cells = ""
    for h in range(4):
        v = pattern[d_i][h]
        if v == 1: st = f"background:linear-gradient(160deg,{PL},{P});box-shadow:0 0 10px {PL}88;"
        elif v == 2: st = f"background:rgba(66,133,244,0.85);box-shadow:0 0 10px rgba(66,133,244,0.6);"
        else: st = "background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);"
        cells += f'<div style="height:26px;border-radius:6px;{st}"></div>'
    cols += f'<div style="flex:1;display:flex;flex-direction:column;gap:4px;"><span style="font-size:8.5px;font-weight:700;text-align:center;color:rgba(255,255,255,0.55);">{d}</span>{cells}</div>'
def kpi(n, l, c=None):
    c = c or PL
    return f'<div style="flex:1;text-align:center;padding:8px 4px;border-radius:10px;background:rgba(255,255,255,0.05);"><p style="font-size:24px;font-weight:800;color:{c};line-height:1;text-shadow:0 0 14px {c}88;">{n}</p><p style="font-size:8.5px;color:rgba(255,255,255,0.6);margin-top:3px;line-height:1.2;">{l}</p></div>'
panel = f'''<div style="position:absolute;left:24px;right:46px;top:94px;z-index:3;">{glass(f"""
<div style="display:flex;align-items:center;gap:8px;padding:9px 11px;border-bottom:1px solid rgba(255,255,255,0.08);"><span style="font-size:10.5px;font-weight:700;color:#fff;letter-spacing:1px;">SEU PAINEL · HOJE</span>
<span style="margin-left:auto;font-size:9px;font-weight:700;color:#FF6B6B;display:flex;align-items:center;gap:4px;"><span style="width:6px;height:6px;border-radius:50%;background:#FF6B6B;box-shadow:0 0 8px #FF6B6B;"></span>AO VIVO</span></div>
<div style="padding:9px;display:flex;gap:6px;">{kpi("18","conversas")}{kpi("7","horários marcados")}{kpi("1","pede sua atenção",GOLD)}</div>
<div style="padding:0 9px 9px;display:flex;gap:4px;">{cols}</div>
<div style="padding:0 11px 10px;display:flex;gap:12px;"><span style="font-size:9px;color:rgba(255,255,255,0.7);display:flex;align-items:center;gap:5px;"><span style="width:9px;height:9px;border-radius:3px;background:{PL};"></span>marcado pelo James</span><span style="font-size:9px;color:rgba(255,255,255,0.7);display:flex;align-items:center;gap:5px;"><span style="width:9px;height:9px;border-radius:3px;background:{GBLUE};"></span>marcado por você</span></div>""")}</div>'''
S.append(slide(5, stage("50% 40%") + panel,
f'''<div style="position:absolute;left:26px;right:40px;top:26px;z-index:5;">{tag("04","CENTRO DE GESTÃO")}</div>
<div style="position:absolute;left:26px;right:40px;bottom:52px;z-index:5;">
<h2 style="font-size:24px;{H}">A semana inteira <span style="{G}">num painel só.</span></h2>
<p style="{SUB}margin-top:6px;">O que o James marcou e o que você marcou, lado a lado, com os números do dia.</p></div>'''))

# ---------- 7 CTA ----------
def pill(t): return f'<span style="font-size:11.5px;font-weight:600;color:#fff;padding:6px 11px;border-radius:20px;background:rgba(255,255,255,0.08);border:1px solid rgba(95,211,154,0.4);">{t}</span>'
S.append(slide(6, stage("50% 26%", "rgba(30,138,85,0.75)") + orbit(210, 120, 170, 44, -8, 0.5) +
f'<img src="{jx("expressoes/oculos-escuros", True)}" style="position:absolute;left:50%;transform:translateX(-50%);top:22px;height:180px;z-index:2;">',
f'''<div style="position:absolute;left:26px;right:26px;top:206px;z-index:5;text-align:center;">
<h2 style="font-size:23px;{H}">Quantos clientes faltam por mês sem avisar?</h2>
<div style="display:flex;justify-content:center;gap:6px;margin-top:10px;">{pill("1️⃣ Nenhum")}{pill("2️⃣ 1 a 3")}{pill("3️⃣ Mais de 3")}</div>
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
html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>James cuida da agenda</title><style>{faces}
*{{margin:0;padding:0;box-sizing:border-box;}} body{{font-family:'Bricolage Grotesque',sans-serif;background:#111;}}
.ig-frame{{width:420px;}} .carousel-viewport{{width:420px;height:525px;overflow:hidden;}} .carousel-track{{display:flex;}}
.slide{{min-width:420px;width:420px;height:525px;position:relative;overflow:hidden;background:{BG};}}
</style></head><body><div class="ig-frame"><div class="ig-header"></div><div class="carousel-viewport"><div class="carousel-track">{"".join(S)}</div></div>
<div class="ig-dots"></div><div class="ig-actions"></div><div class="ig-caption"></div></div></body></html>'''
OUT.write_text(html, encoding="utf-8"); print(OUT)
