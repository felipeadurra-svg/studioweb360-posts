import base64
from pathlib import Path

HERE = Path(__file__).parent
BRAND = HERE.parent / "brand"

P = "#1E8A55"; PL = "#5FD39A"; PD = "#0E5232"
LBG = "#F1F6F2"; LBR = "#DCE7DF"; DBG = "#0D1812"; MUTED = "#5d6a62"; RED = "#E5484D"
GRAD = f"linear-gradient(165deg,{PD} 0%,{P} 55%,{PL} 120%)"
# cores do app (painel real)
APP = "#D2E2D7"; CARD = "#F2F6F3"; INK = "#1c2a22"; SUB = "#5e6d64"; BTN = "#2E6B4A"; LINE = "#DDE7E0"
BUB = "#DDF7D1"; ORANGE = "#C2620E"
TOTAL = 10
NFEAT = 8


def b64(path, mime="image/png"):
    return f"data:{mime};base64," + base64.b64encode(Path(path).read_bytes()).decode()


def jimg(name):
    return b64(BRAND / "james" / f"{name}.png")


AV = jimg("avatar-circulo-160")
FADE = "-webkit-mask-image:linear-gradient(to bottom,#000 74%,transparent 100%);mask-image:linear-gradient(to bottom,#000 74%,transparent 100%);"

FONTS = "".join(
    f"@font-face{{font-family:'Bricolage Grotesque';font-weight:{w};font-style:normal;src:url({b64(BRAND/'fonts'/f'bricolage-grotesque-latin-{w}-normal.woff2','font/woff2')}) format('woff2');}}"
    for w in (300, 400, 600, 700, 800)
)


def bar(i, light):
    pct = (i + 1) / TOTAL * 100
    tr = 'rgba(0,0,0,0.08)' if light else 'rgba(255,255,255,0.14)'
    fi = P if light else '#fff'
    lb = 'rgba(0,0,0,0.35)' if light else 'rgba(255,255,255,0.5)'
    return f'''<div style="position:absolute;bottom:0;left:0;right:0;padding:16px 28px 20px;z-index:10;display:flex;align-items:center;gap:10px;">
<div style="flex:1;height:3px;background:{tr};border-radius:2px;overflow:hidden;"><div style="height:100%;width:{pct}%;background:{fi};border-radius:2px;"></div></div>
<span style="font-size:11px;color:{lb};font-weight:600;">{i+1}/{TOTAL}</span></div>'''


def arrow(light):
    bg = 'rgba(0,0,0,0.05)' if light else 'rgba(255,255,255,0.07)'
    st = 'rgba(0,0,0,0.25)' if light else 'rgba(255,255,255,0.35)'
    return f'''<div style="position:absolute;right:0;top:0;bottom:0;width:40px;z-index:9;display:flex;align-items:center;justify-content:center;background:linear-gradient(to right,transparent,{bg});">
<svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M9 6l6 6-6 6" stroke="{st}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'''


def slide(i, kind, body, art=""):
    light = kind == "light"
    bg = {"light": LBG, "dark": DBG, "grad": GRAD}[kind]
    last = i == TOTAL - 1
    return f'''<div class="slide" style="background:{bg};">{art}{body}
{'' if last else arrow(light)}{bar(i, light)}</div>'''


def copy(n, title, sub, light, top=None):
    tc = DBG if light else '#fff'
    nc = P if light else PL
    sc = MUTED if light else 'rgba(255,255,255,0.66)'
    pos = f"top:{top}px;" if top is not None else "bottom:52px;"
    return f'''<div style="position:absolute;left:30px;right:44px;{pos}z-index:4;">
<div style="display:flex;align-items:baseline;gap:9px;margin-bottom:7px;">
<span style="font-size:24px;font-weight:300;color:{nc};line-height:1;">{n:02d}</span>
<span style="font-size:9.5px;font-weight:700;letter-spacing:2px;color:{nc};">DE {NFEAT:02d}</span></div>
<h2 style="font-size:26px;font-weight:700;line-height:1.08;letter-spacing:-0.6px;color:{tc};">{title}</h2>
<p style="font-size:12.5px;line-height:1.45;color:{sc};margin-top:7px;">{sub}</p></div>'''


def biz(initial, name, niche, color):
    return f'''<div style="display:flex;align-items:center;gap:8px;">
<div style="width:26px;height:26px;border-radius:50%;background:{color};color:#fff;font-size:12px;font-weight:700;display:flex;align-items:center;justify-content:center;">{initial}</div>
<div style="line-height:1.15;"><div style="font-size:11.5px;font-weight:700;color:{INK};">{name}</div>
<div style="font-size:9px;color:{SUB};">{niche}</div></div></div>'''


def card(inner, style=""):
    return f'<div style="background:{CARD};border-radius:14px;border:1px solid rgba(255,255,255,0.6);box-shadow:0 10px 30px rgba(0,0,0,0.18);{style}">{inner}</div>'


def window(inner, style):
    """moldura do app: fundo verde-menta do painel"""
    return f'<div style="position:absolute;z-index:2;background:{APP};border-radius:18px;padding:10px;box-shadow:0 18px 40px rgba(0,0,0,0.22);{style}">{inner}</div>'


def pill(text, fg, bg):
    return f'<span style="display:inline-flex;align-items:center;gap:3px;font-size:8.5px;font-weight:700;color:{fg};background:{bg};padding:2px 7px;border-radius:10px;white-space:nowrap;">{text}</span>'


def initials(name, color):
    return f'<div style="width:28px;height:28px;border-radius:50%;background:{color};color:#fff;font-size:10.5px;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;">{name}</div>'


def avatar(size):
    return f'<img src="{AV}" style="width:{size}px;height:{size}px;border-radius:50%;flex-shrink:0;">'


WAVE = "".join(f'<span style="display:inline-block;width:2px;height:{h}px;background:{BTN};border-radius:1px;margin-right:1.5px;"></span>' for h in [5,9,13,7,11,15,9,6,12,14,8,5,10,13,7,9,12,6,4,8,11,7,5])


def audio(sec):
    return f'''<div style="display:flex;align-items:center;gap:6px;background:rgba(255,255,255,0.75);border-radius:14px;padding:4px 8px;margin-bottom:5px;">
<svg width="9" height="10" viewBox="0 0 9 10"><path d="M0 0l9 5-9 5z" fill="{INK}"/></svg>
<div style="display:flex;align-items:center;">{WAVE}</div><span style="font-size:8px;color:{SUB};">{sec}</span></div>'''


def b_in(text, time, extra=""):
    return f'''<div style="align-self:flex-start;max-width:80%;background:#fff;border-radius:12px 12px 12px 3px;padding:6px 9px;box-shadow:0 1px 1px rgba(0,0,0,0.05);">{extra}
<p style="font-size:10.5px;color:{INK};line-height:1.35;">{text}</p><p style="font-size:8px;color:#8c9a91;text-align:right;margin-top:1px;">{time}</p></div>'''


def b_out(text, time, extra=""):
    return f'''<div style="align-self:flex-end;max-width:82%;background:{BUB};border-radius:12px 12px 3px 12px;padding:6px 9px;box-shadow:0 1px 1px rgba(0,0,0,0.05);">{extra}
<p style="font-size:10.5px;color:{INK};line-height:1.35;">{text}</p>
<p style="font-size:8px;color:#6f8f7c;text-align:right;margin-top:1px;display:flex;align-items:center;justify-content:flex-end;gap:3px;"><img src="{AV}" style="width:10px;height:10px;border-radius:50%;"> {time} ✓✓</p></div>'''


def stat(label, value, color=INK, small=""):
    return f'''<div style="flex:1;background:#fff;border:1px solid {LINE};border-radius:9px;padding:7px 9px;">
<div style="font-size:7.5px;font-weight:700;letter-spacing:0.8px;color:{SUB};">{label}</div>
<div style="font-size:22px;font-weight:700;color:{color};line-height:1.1;margin-top:2px;">{value}</div>{small}</div>'''


def toggle(on):
    return (f'<div style="width:30px;height:17px;border-radius:9px;background:{BTN if on else "#c9d3cd"};position:relative;flex-shrink:0;">'
            f'<div style="position:absolute;top:2px;{"right" if on else "left"}:2px;width:13px;height:13px;border-radius:50%;background:#fff;"></div></div>')


slides = []

# ---------------- 1. CAPA ----------------
s1_ui = window(card(f'''
<div style="padding:12px 12px 10px;">
<div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">{avatar(26)}
<div style="font-size:12px;font-weight:700;color:{INK};">Boa tarde, Clínica Vitalle.</div></div>
<div style="display:flex;flex-direction:column;gap:5px;" class="tight">
{stat("CONVERSAS HOJE", "47")}
{stat("MARCADOS HOJE", "12", P)}
{stat("PRECISAM DE VOCÊ", "2", ORANGE)}
</div>
<div style="display:flex;align-items:center;gap:5px;margin-top:9px;font-size:9px;color:{P};font-weight:600;"><span style="width:6px;height:6px;border-radius:50%;background:{P};"></span>James atendendo agora</div>
</div>'''), "left:30px;top:206px;width:196px;")
s1_art = f'<img src="{jimg("joinha")}" style="position:absolute;z-index:3;right:-18px;bottom:30px;width:255px;{FADE}">'
s1_body = f'''<div style="position:absolute;left:30px;right:40px;top:30px;z-index:4;">
<div style="display:flex;align-items:center;gap:8px;margin-bottom:18px;">{avatar(30)}<span style="font-size:11.5px;font-weight:700;color:{DBG};">James · Studio Web 360</span></div>
<span style="font-size:9.5px;font-weight:700;letter-spacing:2px;color:{P};">POR DENTRO DO PAINEL DO JAMES →</span>
<h1 style="font-size:30px;font-weight:800;line-height:1.04;letter-spacing:-0.9px;color:{DBG};margin-top:8px;">Você abre o celular e <span style="color:{P};">47 clientes</span> já foram atendidos.</h1>
</div>{s1_ui}
'''
slides.append(slide(0, "light", s1_body, s1_art))

# ---------------- 2. PAINEL / CONVERSAS ----------------
convs = [
    ("LM", "#7C5CBF", "Lucas M.", "Fechou corte + barba amanhã 18h30", "agora", pill("● Cliente", P, "#DDF3E6"), ""),
    ("RA", "#C2620E", "Renata A.", "Quer saber se aceita convênio", "1 min", pill("✋ Pediu você", RED, "#FDE4E4"), "background:#FFF6EE;"),
    ("TS", "#2D7DD2", "Thiago S.", "[áudio] Qual o valor da luzes?", "3 min", pill("● Interessado", "#B7791F", "#FDF1DA"), ""),
    ("JP", "#1E8A55", "Júlia P.", "Remarcou para sexta, 10h", "8 min", pill("● Cliente", P, "#DDF3E6"), ""),
    ("MV", "#C0392B", "Marcos V.", "Pediu o endereço e veio", "12 min", pill("● Novo", "#4a5a50", "#E6ECE8"), ""),
]
rows = "".join(f'''<div style="display:flex;align-items:center;gap:8px;padding:7px 10px;border-top:1px solid {LINE};{hl}">{initials(a,c)}
<div style="flex:1;min-width:0;"><div style="display:flex;align-items:center;gap:5px;"><span style="font-size:11px;font-weight:700;color:{INK};">{n}</span>{tag}</div>
<div style="font-size:9.5px;color:{SUB};white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{m}</div></div>
<span style="font-size:8.5px;color:{SUB};align-self:flex-start;margin-top:3px;">{t}</span></div>''' for a, c, n, m, t, tag, hl in convs)
s2_ui = window(card(f'''
<div style="padding:10px 10px 8px;display:flex;justify-content:space-between;align-items:center;">{biz("N","Barbearia Navalha","barbearia","#3b3b3b")}
{pill("● ao vivo", P, "#DDF3E6")}</div>
<div style="padding:0 10px 8px;display:flex;align-items:baseline;justify-content:space-between;"><span style="font-size:13px;font-weight:700;color:{INK};">Conversas</span><span style="font-size:9px;color:{SUB};">32 hoje</span></div>
{rows}''', "overflow:hidden;"), "left:24px;right:52px;top:28px;")
slides.append(slide(1, "dark", s2_ui + copy(1, "Tudo ao vivo, <span style='color:#5FD39A'>sem atualizar</span>", "Cada conversa aparece na hora, com o que o cliente quer e em que pé está. Quem pediu você fica marcado.", False)))

# ---------------- 3. CONVERSA + ASSUMIR ----------------
chat = f'''
<div style="display:flex;align-items:center;gap:8px;padding:9px 10px;border-bottom:1px solid {LINE};">{initials("LM","#7C5CBF")}
<div style="flex:1;line-height:1.2;"><div style="font-size:11.5px;font-weight:700;color:{INK};">Lucas M.</div><div style="font-size:9px;color:{P};">James está respondendo…</div></div>
<div style="background:{BTN};color:#fff;font-size:10px;font-weight:700;padding:5px 11px;border-radius:14px;box-shadow:0 0 0 4px rgba(46,107,74,0.18);">Assumir</div></div>
<div style="background:#EFEAE2;padding:9px 9px 10px;display:flex;flex-direction:column;gap:6px;">
{b_in("<i style='color:#6b756f'>[áudio transcrito]</i> Fala! Tem horário amanhã depois das 18h pra corte e barba?", "18:02", audio("0:06"))}
{b_out("Tenho sim! Amanhã às 18h30 ou 19h com o Rafa. Qual fica melhor pra você?", "18:02", audio("0:07"))}
{b_in("18h30 fechado", "18:03")}
{b_out("Marcado ✅ Amanhã, 18h30, corte + barba com o Rafa. Te lembro uma hora antes!", "18:03")}
</div>'''
s3_ui = window(card(chat, "overflow:hidden;"), "left:24px;right:52px;top:24px;")
slides.append(slide(2, "light", s3_ui + copy(2, "Assumir é um toque", "Ele ouve áudio, entende e responde por texto ou voz. Quer falar você mesmo? Toca em Assumir e a conversa é sua.", True)))

# ---------------- 4. TREINAMENTO: ENSINAR ----------------
chips = "".join(f'<span style="font-size:9.5px;color:{INK};background:#fff;border:1px solid {LINE};padding:4px 9px;border-radius:12px;">{c}</span>' for c in ["Serviços", "Preços", "Horários", "Pagamento", "Endereço", "O que nunca dizer"])
s4_ui = window(card(f'''
<div style="padding:11px 11px 9px;display:flex;gap:10px;align-items:center;">
<img src="{jimg('joinha')}" style="width:62px;height:62px;object-fit:cover;object-position:top;border-radius:12px;background:#E3EEE6;">
<div style="flex:1;line-height:1.2;"><div style="font-size:8px;font-weight:700;letter-spacing:1.2px;color:{P};">ATENDENTE DE IA</div>
<div style="font-size:16px;font-weight:800;color:{INK};">James <span style="font-size:9.5px;font-weight:600;color:{P};">Trocar nome</span></div>
<div style="font-size:9.5px;color:{SUB};">Atendendo <b style="color:{INK};">Pizzaria Forno di Casa</b></div></div></div>
<div style="display:flex;gap:6px;padding:0 11px;">{stat("SITUAÇÃO","<span style='font-size:13px;color:"+P+"'>Atendendo</span>")}{stat("PRODUTOS","40")}{stat("ARQUIVOS","3")}</div>
<div style="margin:9px 11px 11px;background:#fff;border:1px solid {LINE};border-radius:10px;padding:9px 10px;">
<div style="display:flex;justify-content:space-between;align-items:center;"><span style="font-size:11.5px;font-weight:700;color:{INK};">O que James sabe</span><span style="font-size:9.5px;font-weight:700;color:{P};">✎ Editar</span></div>
<div style="display:flex;flex-wrap:wrap;gap:5px;margin-top:7px;">{chips}</div>
<div style="font-size:9.5px;color:{ORANGE};margin-top:8px;font-weight:600;">⚠ 2 assuntos sem resposta — toque para ver</div></div>'''), "left:24px;right:52px;top:24px;")
slides.append(slide(3, "dark", s4_ui + copy(3, "Você ensina, <span style='color:#5FD39A'>ele aprende</span>", "Cadastra serviços, preços e regras, ou manda o cardápio em arquivo. Mudou o preço? Edita e já vale na próxima mensagem.", False)))

# ---------------- 5. TREINAMENTO: TESTAR ----------------
s5_ui = window(card(f'''
<div style="padding:10px 11px;display:flex;align-items:center;justify-content:center;gap:7px;border-bottom:1px solid {LINE};">{avatar(22)}<span style="font-size:12px;font-weight:700;color:{INK};">Converse com o James</span></div>
<div style="padding:10px;display:flex;flex-direction:column;gap:6px;background:#F7FAF8;">
<div style="align-self:flex-end;max-width:80%;background:{BTN};color:#fff;border-radius:12px 12px 3px 12px;padding:6px 9px;font-size:10.5px;line-height:1.35;">Vocês fazem limpeza de pele no sábado?</div>
<div style="align-self:flex-start;max-width:86%;background:#fff;border:1px solid {LINE};border-radius:12px 12px 12px 3px;padding:6px 9px;font-size:10.5px;line-height:1.35;color:{INK};">Fazemos sim! Sábado das 9h às 13h. A limpeza de pele profunda sai por R$ 180 e leva 1h. Quer que eu veja um horário? 😊</div>
<div style="align-self:flex-end;max-width:80%;background:{BTN};color:#fff;border-radius:12px 12px 3px 12px;padding:6px 9px;font-size:10.5px;line-height:1.35;">E botox, vocês fazem?</div>
<div style="align-self:flex-start;max-width:86%;background:#fff;border:1px solid {LINE};border-radius:12px 12px 12px 3px;padding:6px 9px;font-size:10.5px;line-height:1.35;color:{INK};">Esse eu prefiro confirmar com a equipe pra não te passar nada errado. Já te retornam por aqui!</div>
</div>
<div style="margin:8px 10px 10px;border:1px solid {LINE};background:#fff;border-radius:16px;padding:6px 6px 6px 11px;display:flex;align-items:center;justify-content:space-between;">
<span style="font-size:9.5px;color:#93a199;">Pergunte o que um cliente perguntaria</span>
<span style="width:20px;height:20px;border-radius:50%;background:#E3EAE5;display:flex;align-items:center;justify-content:center;font-size:10px;color:{SUB};">↑</span></div>
<div style="padding:0 11px 9px;">{biz("V","Clínica Vitalle","estética","#B5527A")}</div>'''), "left:24px;right:52px;top:22px;")
slides.append(slide(4, "light", s5_ui + copy(4, "Teste antes de ir ao ar", "Pergunte o que um cliente perguntaria e veja a resposta exata. O que ele não sabe, ele não inventa: passa pra você.", True)))

# ---------------- 6. VOZ E LÍNGUA ----------------
voices = [("Feminina 1", "Jovem e animada"), ("Feminina 2", "Calma e acolhedora"), ("Feminina 3", "Firme e clara"),
          ("Masculina 1", "Grave e segura"), ("Masculina 2", "Tranquila"), ("Masculina 3", "Jovem e direta")]
vgrid = "".join(f'''<div style="background:#fff;border:{'1.5px solid '+BTN if i==4 else '1px solid '+LINE};border-radius:9px;padding:6px 7px;{'box-shadow:0 0 0 3px rgba(46,107,74,0.15);' if i==4 else ''}">
<div style="font-size:10px;font-weight:700;color:{INK};">{n}</div><div style="font-size:8px;color:{SUB};">{d}</div>
<div style="font-size:8.5px;font-weight:700;color:{BTN};margin-top:3px;">▷ Ouvir</div></div>''' for i, (n, d) in enumerate(voices))
s6_ui = window(card(f'''
<div style="padding:11px;">
<div style="display:flex;justify-content:space-between;align-items:center;"><span style="font-size:11.5px;font-weight:700;color:{INK};">🎙 Responder em áudio</span>{toggle(True)}</div>
<div style="font-size:9px;color:{SUB};margin:3px 0 8px;line-height:1.35;">Quem manda áudio recebe a resposta em voz.</div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:5px;">{vgrid}</div>
<div style="border-top:1px solid {LINE};margin-top:10px;padding-top:9px;display:flex;justify-content:space-between;align-items:center;">
<span style="font-size:11.5px;font-weight:700;color:{INK};">文A Responder na língua do cliente</span>{toggle(True)}</div>
<div style="display:flex;gap:4px;margin-top:6px;">{pill("English","#2D7DD2","#E3EEFA")}{pill("Español","#B7791F","#FDF1DA")}{pill("日本語","#B5527A","#F9E3EC")}{pill("+ outras","#4a5a50","#E6ECE8")}</div>
<div style="margin-top:9px;">{biz("H","Hostel Maré","hospedagem","#2D7DD2")}</div>
</div>'''), "left:24px;right:52px;top:24px;")
slides.append(slide(5, "dark", s6_ui + copy(5, "A voz e a língua <span style='color:#5FD39A'>do seu negócio</span>", "6 vozes para responder quem manda áudio. Turista escreveu em inglês ou espanhol? Ele responde na mesma língua.", False)))

# ---------------- 7. AGENDA ----------------
days = ["SEG", "TER", "QUA", "QUI", "SEX", "SÁB"]
nums = [5, 6, 7, 8, 9, 10]
# (dia, hora inicio, duracao em slots de 1h, nome, james?)
evs = [(0,0,1,"Ana",1),(0,2,1,"Bia",1),(0,4,1,"Carla",0),(0,5,1,"Duda",1),
       (1,1,1,"Eva",1),(1,2,1,"Fê",1),(1,4,2,"Gabi",1),
       (2,0,1,"Helô",0),(2,1,1,"Iara",1),(2,3,1,"Jade",1),(2,5,1,"Kel",1),
       (3,0,1,"Lia",1),(3,1,1,"Mel",1),(3,2,1,"Nina",1),(3,4,1,"Olga",0),(3,5,1,"Pri",1),
       (4,0,2,"Quel",1),(4,3,1,"Rô",1),(4,4,1,"Sol",1),
       (5,0,1,"Tati",1),(5,1,1,"Uly",1),(5,2,1,"Vivi",1)]
hours = ["09", "10", "11", "14", "15", "16"]
RH = 32
grid_cells = ""
for d in range(6):
    col = ""
    for (dd, h, dur, nm, jm) in evs:
        if dd != d:
            continue
        bg = "#2E8B57" if jm else "#4C6FD8"
        col += f'<div style="position:absolute;left:2px;right:2px;top:{h*RH+2}px;height:{dur*RH-4}px;background:{bg};border-radius:5px;color:#fff;font-size:8px;font-weight:700;padding:3px 4px;line-height:1.1;">{nm}<br><span style="font-weight:400;opacity:.85;">{hours[h]}h</span></div>'
    today = "background:rgba(30,138,85,0.06);" if d == 3 else ""
    grid_cells += f'<div style="position:relative;flex:1;border-left:1px solid {LINE};height:{RH*6}px;{today}">{col}</div>'
lines = "".join(f'<div style="position:absolute;left:0;right:0;top:{k*RH}px;border-top:1px solid {LINE};"></div>' for k in range(1, 6))
hdr = "".join(f'''<div style="flex:1;text-align:center;line-height:1.15;"><div style="font-size:7.5px;font-weight:700;color:{SUB};">{d}</div>
<div style="font-size:11px;font-weight:700;{'color:#fff;background:'+BTN+';border-radius:50%;width:18px;height:18px;margin:1px auto 0;display:flex;align-items:center;justify-content:center;' if i==3 else 'color:'+INK+';'}">{n}</div></div>''' for i, (d, n) in enumerate(zip(days, nums)))
hcol = "".join(f'<div style="height:{RH}px;font-size:8px;color:{SUB};padding-top:2px;">{h}h</div>' for h in hours)
s7_ui = window(card(f'''
<div style="padding:10px 10px 6px;display:flex;justify-content:space-between;align-items:center;">
<span style="font-size:13px;font-weight:700;color:{INK};"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" style="vertical-align:-2px;"><rect x="3" y="5" width="18" height="16" rx="3" stroke="{BTN}" stroke-width="2.2"/><path d="M3 10h18M8 3v4M16 3v4" stroke="{BTN}" stroke-width="2.2" stroke-linecap="round"/></svg> Agenda</span>
<span style="display:flex;align-items:center;gap:5px;font-size:9px;font-weight:700;color:{BTN};background:#E3F2E9;border:1px solid #BFE0CC;padding:3px 8px;border-radius:10px;">Agenda ligada {toggle(True)}</span></div>
<div style="display:flex;padding:0 8px 0 26px;">{hdr}</div>
<div style="display:flex;padding:4px 8px 6px 8px;"><div style="width:18px;">{hcol}</div>
<div style="flex:1;display:flex;position:relative;">{lines}{grid_cells}</div></div>
<div style="display:flex;gap:10px;padding:2px 10px 9px;font-size:8.5px;color:{SUB};align-items:center;">
<span><b style="color:#2E8B57;">■</b> Marcado pelo James <b style="color:{INK};">19</b></span><span><b style="color:#4C6FD8;">■</b> Marcado por você <b style="color:{INK};">3</b></span></div>
<div style="padding:0 10px 9px;">{biz("L","Estúdio Lumi","salão de beleza","#B7791F")}</div>'''), "left:24px;right:52px;top:20px;")
slides.append(slide(6, "light", s7_ui + copy(6, "A agenda se enche sozinha", "Ele vê o horário livre, marca na conversa e lembra o cliente na véspera. Nunca marca duas vezes.", True)))

# ---------------- 8. CRM ----------------
def kcard(ini, color, name, note, when):
    return f'''<div style="background:#fff;border:1px solid {LINE};border-radius:7px;padding:5px 6px;margin-top:4px;">
<div style="display:flex;align-items:center;gap:4px;"><div style="width:15px;height:15px;border-radius:50%;background:{color};color:#fff;font-size:6.5px;font-weight:700;display:flex;align-items:center;justify-content:center;">{ini}</div>
<span style="font-size:8.5px;font-weight:700;color:{INK};">{name}</span></div>
<div style="font-size:7.5px;color:{SUB};margin-top:2px;line-height:1.25;">{note}</div><div style="font-size:6.5px;color:#9aa69e;margin-top:1px;">{when}</div></div>'''


def kcol(dot, title, n, cards):
    return f'''<div style="flex:1;background:#E9F0EB;border-radius:8px;padding:5px;min-width:0;">
<div style="display:flex;justify-content:space-between;align-items:center;"><span style="font-size:8px;font-weight:700;color:{INK};"><span style="color:{dot};">●</span> {title}</span><span style="font-size:7px;color:{SUB};">{n}</span></div>{cards}</div>'''


s8_ui = window(card(f'''
<div style="padding:10px 10px 4px;display:flex;justify-content:space-between;align-items:center;">
<span style="font-size:13px;font-weight:700;color:{INK};">CRM <span style="font-size:8.5px;font-weight:400;color:{SUB};">· 30 dias</span></span>
{biz("M","Studio Move","academia","#2D7DD2")}</div>
<div style="display:flex;gap:5px;padding:4px 10px 6px;">
{stat("NOVOS","38")}{stat("INTERESSADOS","14","#B7791F")}{stat("CLIENTES","11",P,'<div style="font-size:7px;color:'+SUB+';">29% dos novos</div>')}</div>
<div style="display:flex;gap:5px;padding:0 10px 6px;">
<div style="flex:1;background:#FFF1F1;border:1px solid #F6D3D3;border-radius:8px;padding:5px 7px;font-size:8.5px;color:{INK};"><b>✋ Pediram você</b> <b style="float:right;color:{RED};">2</b></div>
<div style="flex:1;background:#FFF8EA;border:1px solid #F1E0B8;border-radius:8px;padding:5px 7px;font-size:8.5px;color:{INK};"><b>⏳ Esfriando</b> <b style="float:right;color:#B7791F;">4</b></div></div>
<div style="display:flex;gap:4px;padding:0 10px 9px;">
{kcol("#8a958e","Novos","9",kcard("AP","#7C5CBF","Ana P.","quer saber o preço do plano","há 5 min")+kcard("DR","#2D7DD2","Diego R.","horário de funcionamento","há 22 min"))}
{kcol("#E2A324","Interessados","14",kcard("BM","#C2620E","Bruno M.","pediu orçamento do plano anual","há 1 h")+kcard("LS","#B5527A","Lara S.","aula experimental sábado","há 2 h"))}
{kcol(P,"Clientes","11",kcard("CF","#1E8A55","Carla F.","fechou plano trimestral","hoje")+kcard("RT","#3b3b3b","Rafa T.","renovou mensalidade","ontem"))}
</div>'''), "left:24px;right:52px;top:16px;")
slides.append(slide(7, "dark", s8_ui + copy(7, "Um CRM que <span style='color:#5FD39A'>se organiza sozinho</span>", "Quem falou com o James, em que pé está e o que quer. E avisa quem está esfriando, pra você chamar de volta.", False)))

# ---------------- 9. PEDIDOS + CONTROLE ----------------
def ped(name, items, when, status, sc, sbg):
    return f'''<div style="display:flex;gap:8px;align-items:center;padding:7px 0;border-top:1px solid {LINE};">
<div style="width:3px;align-self:stretch;background:{BTN};border-radius:2px;"></div>
<div style="flex:1;min-width:0;"><div style="display:flex;justify-content:space-between;"><span style="font-size:10.5px;font-weight:700;color:{INK};">{name}</span><span style="font-size:8px;color:{SUB};">{when}</span></div>
<div style="font-size:9px;color:{SUB};white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{items}</div></div>{pill(status, sc, sbg)}</div>'''


s9_ui = window(card(f'''
<div style="padding:10px 11px 3px;display:flex;justify-content:space-between;align-items:center;">
<span style="font-size:12.5px;font-weight:700;color:{INK};">🛍 Pedidos <span style="font-size:9px;font-weight:400;color:{SUB};">· 3 para preparar</span></span>
<span style="font-size:9px;font-weight:700;color:{INK};background:#fff;border:1px solid {LINE};padding:3px 8px;border-radius:8px;">Abrir →</span></div>
<div style="padding:0 11px 6px;">
{ped("Marina C.", "2 Whey Protein 900g · entrega", "agora", "APROVADO", P, "#DDF3E6")}
{ped("João P.", "Creatina 300g + coqueteleira · retirada", "14 min", "APROVADO", P, "#DDF3E6")}
{ped("Paula R.", "Pré-treino 300g · entrega", "31 min", "NOVO", "#B7791F", "#FDF1DA")}
</div>
<div style="padding:0 11px 9px;">{biz("F","Forma Suplementos","loja","#C2620E")}</div>'''), "left:24px;right:52px;top:22px;")
s9_alert = f'''<div style="position:absolute;z-index:3;left:44px;right:62px;top:232px;background:#fff;border-radius:12px;box-shadow:0 12px 28px rgba(0,0,0,0.18);padding:9px 10px;display:flex;gap:8px;align-items:center;border:1px solid #F1E0B8;">
{avatar(30)}<div style="flex:1;line-height:1.3;"><div style="font-size:10.5px;font-weight:700;color:{INK};">James precisa de você</div>
<div style="font-size:9px;color:{SUB};">Cliente pediu desconto fora do combinado. Passei a conversa pra você.</div></div></div>'''
slides.append(slide(8, "light", s9_ui + s9_alert + copy(8, "Pedido pronto. Você no controle.", "Ele monta o pedido na conversa e deixa pronto pra preparar. Assunto delicado? Te chama. Quer parar tudo? Pausa num toque.", True)))

# ---------------- 10. CTA ----------------
pills_cta = "".join(f'<span style="font-size:10px;padding:4px 10px;border:1px solid rgba(255,255,255,0.35);border-radius:14px;color:#fff;">{t}</span>' for t in ["WhatsApp e Instagram", "API oficial da Meta", "sem fidelidade"])
s10 = f'''<img src="{jimg('sorriso')}" style="position:absolute;z-index:1;left:50%;transform:translateX(-50%);top:10px;width:162px;{FADE}">
<div style="position:absolute;left:30px;right:30px;top:226px;z-index:4;text-align:center;">
<h2 style="font-size:28px;font-weight:800;line-height:1.06;letter-spacing:-0.7px;color:#fff;">Quer esse painel trabalhando pro <span style="font-style:italic;font-weight:600;">seu</span> negócio?</h2>
<div style="display:flex;flex-wrap:wrap;gap:5px;justify-content:center;margin-top:12px;">{pills_cta}</div>
<div style="display:inline-block;margin-top:16px;padding:11px 30px;background:{LBG};color:{PD};font-weight:800;font-size:14px;border-radius:26px;box-shadow:0 8px 20px rgba(0,0,0,0.18);">Comente JAMES</div>
<p style="font-size:11px;color:rgba(255,255,255,0.85);margin-top:10px;line-height:1.4;">que eu te mostro como funciona no seu negócio<br>ou acesse <b>studioweb360.com.br</b></p>
<p style="font-size:8px;color:rgba(255,255,255,0.5);margin-top:10px;">Telas ilustrativas com dados de demonstração.</p></div>'''
slides.append(slide(9, "grad", s10))

# ---------------- HTML ----------------
CSS = FONTS + """
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:'Bricolage Grotesque',sans-serif;background:#e9ece9;display:flex;justify-content:center;padding:30px 0;-webkit-font-smoothing:antialiased;}
.ig-frame{width:420px;background:#fff;border-radius:12px;box-shadow:0 10px 40px rgba(0,0,0,.15);overflow:hidden;}
.ig-header{display:flex;align-items:center;gap:10px;padding:12px 14px;}
.ig-header b{font-size:13px;} .ig-header small{display:block;font-size:11px;color:#888;}
.carousel-viewport{width:420px;height:525px;overflow:hidden;position:relative;cursor:grab;touch-action:pan-y;}
.carousel-track{display:flex;height:100%;transition:transform .35s ease;}
.tight>div{padding:4px 9px !important;} .tight>div>div:nth-child(2){font-size:19px !important;}
.slide{width:420px;height:525px;flex-shrink:0;position:relative;overflow:hidden;}
.ig-dots{display:flex;justify-content:center;gap:4px;padding:10px 0 4px;}
.ig-dots span{width:6px;height:6px;border-radius:50%;background:#ccc;} .ig-dots span.on{background:#1E8A55;}
.ig-actions{display:flex;gap:14px;padding:6px 14px;font-size:20px;}
.ig-caption{padding:2px 14px 14px;font-size:12.5px;line-height:1.45;} .ig-caption small{display:block;color:#999;font-size:10px;margin-top:6px;letter-spacing:.5px;}
"""
html = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Painel do James</title><style>{CSS}</style></head><body>
<div class="ig-frame">
<div class="ig-header">{avatar(32)}<div><b>studioweb360.ia</b><small>James · atendente de IA</small></div></div>
<div class="carousel-viewport"><div class="carousel-track">{''.join(slides)}</div></div>
<div class="ig-dots">{''.join('<span></span>' for _ in slides)}</div>
<div class="ig-actions">♡ 💬 ➤</div>
<div class="ig-caption"><b>studioweb360.ia</b> Por dentro do painel do James: tudo o que você vê enquanto ele atende por você.<small>HÁ 2 HORAS</small></div>
</div>
<script>
const tr=document.querySelector('.carousel-track'),vp=document.querySelector('.carousel-viewport'),dots=[...document.querySelectorAll('.ig-dots span')];let i=0,x0=null;
function go(n){{i=Math.max(0,Math.min(dots.length-1,n));tr.style.transform='translateX('+(-i*420)+'px)';dots.forEach((d,k)=>d.classList.toggle('on',k===i));}}
vp.addEventListener('pointerdown',e=>{{x0=e.clientX;}});
window.addEventListener('pointerup',e=>{{if(x0===null)return;const dx=e.clientX-x0;if(Math.abs(dx)>30)go(i+(dx<0?1:-1));else if(Math.abs(dx)<5)go(i+(e.clientX-vp.getBoundingClientRect().left>210?1:-1));x0=null;}});
document.addEventListener('keydown',e=>{{if(e.key==='ArrowRight')go(i+1);if(e.key==='ArrowLeft')go(i-1);}});
go(0);
</script></body></html>"""
(HERE / "carrossel.html").write_text(html, encoding="utf-8")
print("ok", len(html) // 1024, "KB")
