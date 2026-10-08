"""Gera capas (1080x1920) e stories (1080x1920) dos Destaques do @studioweb360.ia.
Uso: python3 build_destaques.py <pasta_saida>
Layout 360x640 exportado com device_scale_factor 3.
Zona segura do story: ~84px no topo e ~113px na base (layout) ficam livres.
"""
import asyncio, base64, sys
from pathlib import Path
from playwright.async_api import async_playwright

HERE = Path(__file__).resolve().parent.parent  # brand/
OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "destaques")
P = "#1E8A55"; PL = "#5FD39A"; PD = "#0E5232"
LBG = "#F1F6F2"; LBR = "#DCE7DF"; DBG = "#0D1812"; MUTED = "#5d6a62"
GRAD = f"linear-gradient(165deg,{PD} 0%,{P} 55%,{PL} 120%)"
FADE = "-webkit-mask-image:linear-gradient(to bottom,#000 74%,transparent 100%);mask-image:linear-gradient(to bottom,#000 74%,transparent 100%);"

def uri(name):
    return "data:image/png;base64," + base64.b64encode((HERE / f"james/{name}.png").read_bytes()).decode()

FONTS = ""
for w in (300, 400, 600, 700, 800):
    b = base64.b64encode((HERE / f"fonts/bricolage-grotesque-latin-{w}-normal.woff2").read_bytes()).decode()
    FONTS += f"@font-face{{font-family:'B';font-weight:{w};src:url(data:font/woff2;base64,{b}) format('woff2');}}"

def page(inner, bg):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{width:360px;height:640px;overflow:hidden;font-family:'B',sans-serif;background:{bg};position:relative;}}
.z{{position:absolute;left:26px;right:26px;top:92px;bottom:120px;display:flex;flex-direction:column;}}
.k{{font-size:10.5px;font-weight:600;letter-spacing:2.2px;}}
h1{{font-weight:800;letter-spacing:-1px;line-height:1.03;}}
h2{{font-weight:700;letter-spacing:-.5px;line-height:1.1;}}
p{{line-height:1.45;}}
</style></head><body>{inner}</body></html>"""

# ---------- ícones das capas (traço branco, viewBox 24) ----------
ICONS = {
 "como-funciona": '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/>',
 "demonstracao": '<path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 21l2.1-5.5A8.4 8.4 0 1 1 21 11.5z"/><path d="M10 8.5l5 3-5 3z" fill="#fff"/>',
 "planos": '<path d="M20.6 13.4l-7.2 7.2a2 2 0 0 1-2.8 0L2 12V2h10l8.6 8.6a2 2 0 0 1 0 2.8z"/><circle cx="7" cy="7" r="1.5" fill="#fff"/>',
 "duvidas": '<circle cx="12" cy="12" r="10"/><path d="M9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3"/><circle cx="12" cy="17" r=".6" fill="#fff"/>',
}

def cover(key):
    if key == "james":
        mid = f'<img src="{uri("rosto-sorriso")}" style="width:250px;height:250px;border-radius:50%;object-fit:cover;border:5px solid rgba(255,255,255,.9);">'
    else:
        mid = f'<svg width="150" height="150" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{ICONS[key]}</svg>'
    return page(f'''<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;">
<div style="width:300px;height:300px;border-radius:50%;background:rgba(255,255,255,.08);display:flex;align-items:center;justify-content:center;">{mid}</div></div>''', GRAD)

# ---------- componentes dos stories ----------
def tag(t, light):
    return f'<span class="k" style="color:{P if light else PL};margin-bottom:12px;">{t}</span>'

def bub_in(t, time="23:41", light=True):
    bg, bd, tc = ("#fff", LBR, "#2a332d") if light else ("rgba(255,255,255,.08)", "rgba(255,255,255,.08)", "rgba(255,255,255,.92)")
    return f'<div style="align-self:flex-start;max-width:80%;background:{bg};border:1px solid {bd};border-radius:14px 14px 14px 4px;padding:8px 12px;"><p style="font-size:13px;color:{tc};line-height:1.35;">{t}</p><p style="font-size:9.5px;color:#9aa69e;text-align:right;margin-top:2px;">{time}</p></div>'

def bub_out(t, time="23:41"):
    return f'<div style="align-self:flex-end;max-width:82%;background:#D7F2E2;border-radius:14px 14px 4px 14px;padding:8px 12px;"><p style="font-size:13px;color:#183223;line-height:1.35;">{t}</p><p style="font-size:9.5px;color:#5f8a70;text-align:right;margin-top:2px;">{time} · James ✓✓</p></div>'

def cta_pill(t="Comente JAMES no último post"):
    return f'<div style="align-self:center;padding:12px 24px;background:{LBG};color:{PD};font-weight:700;font-size:14px;border-radius:28px;">{t}</div>'

def check_list(items, light):
    tc = DBG if light else "#fff"
    ic = P if light else PL
    return '<div style="display:flex;flex-direction:column;gap:10px;">' + "".join(
        f'<div style="display:flex;gap:10px;align-items:flex-start;"><span style="flex-shrink:0;width:20px;height:20px;border-radius:50%;background:{ic};display:flex;align-items:center;justify-content:center;"><svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="{"#fff" if light else PD}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5 9-10"/></svg></span><p style="font-size:14px;color:{tc};line-height:1.35;">{t}</p></div>'
        for t in items) + "</div>"

def faq(q, a, light):
    bg, bd, qc, ac = ("#fff", LBR, DBG, MUTED) if light else ("rgba(255,255,255,.05)", "rgba(255,255,255,.08)", "#fff", "rgba(255,255,255,.68)")
    return f'<div style="padding:13px 15px;background:{bg};border:1px solid {bd};border-radius:14px;"><p style="font-size:14px;font-weight:700;color:{qc};margin-bottom:4px;">{q}</p><p style="font-size:12.5px;color:{ac};">{a}</p></div>'

def james(name, style):
    return f'<img src="{uri(name)}" style="position:absolute;z-index:0;{FADE}{style}">'

# ---------- stories ----------
S = {}

S["james"] = [
 page(f'''{james("sorriso", "left:50%;transform:translateX(-50%);top:48px;height:280px;")}
<div class="z" style="justify-content:flex-end;z-index:1;">
{tag("ATENDENTE DE IA · STUDIO WEB 360", False)}
<h1 style="font-size:40px;color:#fff;">Oi! Eu sou o <span style="color:{PL};">James</span>.</h1>
<p style="font-size:15px;color:rgba(255,255,255,.75);margin-top:12px;">Eu atendo os clientes do seu negócio no WhatsApp, 24 horas por dia. Respondo, tiro dúvidas e marco horários enquanto você trabalha (ou dorme).</p>
</div>''', DBG),
 page(f'''<div class="z">
{tag("O QUE EU FAÇO", True)}
<h2 style="font-size:28px;color:{DBG};margin-bottom:20px;">Um atendente que <span style="color:{P};">não tira folga</span></h2>
{check_list(["Respondo na hora, de madrugada e no domingo","Entendo áudio e respondo em áudio","Marco, lembro e remarco horários","Atendo vários clientes ao mesmo tempo","Chamo você quando o assunto é delicado"], True)}
</div>{james("joinha", "right:-14px;bottom:96px;height:200px;")}''', LBG),
]

S["como-funciona"] = [
 page(f'''<div class="z">
{tag("COMO FUNCIONA", False)}
<h2 style="font-size:30px;color:#fff;margin-bottom:22px;">Do zero ao James atendendo em <span style="color:{PL};">3 passos</span></h2>
''' + "".join(f'''<div style="display:flex;gap:14px;align-items:flex-start;padding:14px 0;border-top:1px solid rgba(255,255,255,.1);">
<span style="font-size:30px;font-weight:300;color:{PL};line-height:1;width:34px;">{n}</span>
<div><p style="font-size:15px;font-weight:700;color:#fff;">{t}</p><p style="font-size:12.5px;color:rgba(255,255,255,.65);margin-top:3px;">{d}</p></div></div>'''
    for n, t, d in [("01","Ensina o seu negócio","Você responde um formulário com serviços, preços, horários e regras. Tem site? Ele lê e adianta."),
                    ("02","Conecta o seu WhatsApp","Pelo QR code ou pela API oficial da Meta. Mesmo número, mesmas conversas."),
                    ("03","Ele começa a atender","Você acompanha tudo pelo painel e assume qualquer conversa com um toque.")]) +
 '</div>', DBG),
 page(f'''<div class="z">
{tag("VOCÊ NO CONTROLE", True)}
<h2 style="font-size:28px;color:{DBG};margin-bottom:18px;">Acompanha tudo pelo celular</h2>
<div style="display:flex;gap:7px;margin-bottom:10px;">''' + "".join(
    f'<div style="flex:1;padding:12px 10px;background:#fff;border:1px solid {LBR};border-radius:12px;"><p style="font-size:24px;font-weight:700;color:{DBG};line-height:1;">{n}</p><p style="font-size:10px;color:{MUTED};margin-top:4px;">{l}</p></div>'
    for n, l in [("28","conversas"),("26","resolvidas"),("9","agendados")]) + f'''</div>
<div style="padding:12px 14px;background:#fff;border:1px solid {LBR};border-radius:12px;display:flex;align-items:center;gap:10px;margin-bottom:16px;">
<img src="{uri("avatar-circulo-160")}" style="width:32px;height:32px;border-radius:50%;">
<div style="flex:1;"><p style="font-size:12.5px;font-weight:700;color:{DBG};">James precisa de você</p><p style="font-size:11px;color:{MUTED};">Cliente pediu desconto fora do combinado.</p></div>
<span style="font-size:10.5px;padding:5px 11px;border-radius:20px;background:{P};color:#fff;font-weight:700;">Assumir</span></div>
<p style="font-size:13px;color:{MUTED};max-width:190px;">Ele só fala do que você cadastrou. Pedido fora do combinado ou cliente irritado? Ele passa a conversa para você e avisa.</p>
</div>{james("piscando", "right:0px;bottom:112px;height:150px;")}''', LBG),
]

S["demonstracao"] = [
 page(f'''<div class="z">
{tag("DEMONSTRAÇÃO · 23:41 DE UM DOMINGO", False)}
<div style="display:flex;flex-direction:column;gap:9px;margin-top:6px;">
{bub_in("oi, vcs atendem amanhã? queria marcar uma limpeza de pele", "23:41", False)}
{bub_out("Oi! Atendemos sim, das 9h às 18h 😊 Amanhã tenho 10h, 14h30 ou 16h. Qual fica melhor?")}
{bub_in("14h30", "23:42", False)}
{bub_out("Prontinho! Limpeza de pele segunda às 14h30. Vou te lembrar no dia. Precisa de mais alguma coisa?", "23:42")}
{bub_in("só isso, obrigada!!", "23:42", False)}
</div>
<div style="margin-top:auto;padding:12px 14px;border-radius:12px;background:rgba(95,211,154,.12);border:1px solid rgba(95,211,154,.3);">
<p style="font-size:12.5px;color:{PL};font-weight:600;">✓ Horário marcado na agenda, sem ninguém da equipe acordado.</p></div>
</div>''', DBG),
 page(f'''<div class="z">
{tag("ÁUDIO E OUTROS IDIOMAS", True)}
<h2 style="font-size:27px;color:{DBG};margin-bottom:16px;">Cliente mandou áudio? Ou escreveu em inglês?</h2>
<div style="display:flex;flex-direction:column;gap:9px;">
<div style="align-self:flex-start;display:flex;align-items:center;gap:8px;background:#fff;border:1px solid {LBR};border-radius:14px 14px 14px 4px;padding:9px 12px;">
<span style="width:22px;height:22px;border-radius:50%;background:#E3EEE6;display:flex;align-items:center;justify-content:center;"><svg width="9" height="9" viewBox="0 0 10 10"><path d="M2 1l7 4-7 4z" fill="{PD}"/></svg></span>
<span style="display:flex;align-items:center;gap:2px;">''' + "".join(f'<span style="display:inline-block;width:3px;height:{h}px;background:{P};border-radius:2px;"></span>' for h in [7,13,19,11,21,15,9,17,22,13,7,15,19,11,6,13]) + f'''</span><span style="font-size:10px;color:#9aa69e;">0:14</span></div>
{bub_out("Oi! Respondi seu áudio 🎧 O valor é R$ 120 e dá pra parcelar.", "10:03")}
{bub_in("Hi! Do you have a table for two tonight?", "19:02")}
{bub_out("Hi! Yes, we do. Would 8pm work for you?", "19:02")}
</div>
<p style="font-size:12.5px;color:{MUTED};margin-top:14px;">Ele ouve, entende e responde em texto ou áudio, na língua do cliente.</p>
</div>''', LBG),
]

S["planos"] = [
 page(f'''{james("expressoes/comemorando", "right:16px;top:150px;height:150px;")}
<div class="z" style="justify-content:flex-end;">
{tag("PLANOS", False)}
<h2 style="font-size:31px;color:#fff;margin-bottom:16px;max-width:215px;">Um plano do tamanho do <span style="color:{PL};">seu negócio</span></h2>
<div style="display:flex;flex-wrap:wrap;gap:7px;margin-bottom:18px;">''' + "".join(
    f'<span style="font-size:12.5px;padding:7px 13px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.1);border-radius:20px;color:{PL};">{t}</span>'
    for t in ["mensal","sem fidelidade","cancela quando quiser","configuração inclusa"]) + f'''</div>
{check_list(["WhatsApp 24h com o seu número","Agenda automática com lembretes","Painel para acompanhar e assumir conversas","Suporte direto com a equipe"], False)}
</div>''', DBG),
 page(f'''<div class="z" style="justify-content:center;align-items:center;text-align:center;">
<img src="{uri("sorriso")}" style="height:190px;margin-bottom:8px;{FADE}">
<h2 style="font-size:29px;color:#fff;">Quer saber o valor para o <em>seu</em> negócio?</h2>
<p style="font-size:14px;color:rgba(255,255,255,.85);margin:12px 0 20px;">Chama no direct ou fale com o James pelo link da bio. A gente monta a proposta com você.</p>
{cta_pill("Envie JAMES no direct")}
<p style="font-size:13px;color:rgba(255,255,255,.85);margin-top:14px;"><b style="color:#fff;">studioweb360.com.br</b></p>
</div>''', GRAD),
]

S["duvidas"] = [
 page(f'''<div class="z">
{tag("DÚVIDAS FREQUENTES · 1/2", True)}
<h2 style="font-size:28px;color:{DBG};margin-bottom:16px;">Perguntas que todo mundo faz</h2>
<div style="display:flex;flex-direction:column;gap:9px;">
{faq("Ele é um robô de menu?", "Não. Ele conversa de forma natural, entende o contexto e responde com as informações do seu negócio.", True)}
{faq("Preciso trocar de número?", "Não. Ele atende no número que você já usa, pelo QR code ou pela API oficial da Meta.", True)}
{faq("E se ele não souber responder?", "Ele não inventa. Passa a conversa para você e te avisa na hora.", True)}
</div></div>''', LBG),
 page(f'''<div class="z">
{tag("DÚVIDAS FREQUENTES · 2/2", False)}
<div style="display:flex;flex-direction:column;gap:9px;margin-bottom:18px;">
{faq("Consigo responder eu mesmo?", "Sim. Um toque no painel pausa o James naquele contato e você assume.", False)}
{faq("Funciona no Instagram?", "Sim. Ele também atende o direct do Instagram.", False)}
{faq("Tem fidelidade?", "Não. O plano é mensal e você cancela quando quiser.", False)}
</div>
<p style="font-size:14px;color:#fff;font-weight:600;text-align:center;margin-bottom:12px;">Ficou outra dúvida? Pergunta pro próprio James 👇</p>
{cta_pill("Link na bio")}
</div>''', DBG),
]

ORDER = ["james", "como-funciona", "demonstracao", "planos", "duvidas"]

async def main():
    OUT.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 360, "height": 640}, device_scale_factor=3)
        for n, key in enumerate(ORDER, 1):
            d = OUT / f"{n}-{key}"; d.mkdir(exist_ok=True)
            frames = [("capa", cover(key))] + [(f"story-{i}", h) for i, h in enumerate(S[key], 1)]
            for name, html in frames:
                await pg.set_content(html, wait_until="networkidle")
                await pg.wait_for_timeout(250)
                await pg.screenshot(path=str(d / f"{name}.png"))
        await b.close()

asyncio.run(main())
