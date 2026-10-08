import base64
from pathlib import Path

HERE = Path(__file__).parent
P = "#1E8A55"; PL = "#5FD39A"; PD = "#0E5232"
LBG = "#F1F6F2"; LBR = "#DCE7DF"; DBG = "#0D1812"; MUTED = "#5d6a62"
GRAD = f"linear-gradient(165deg,{PD} 0%,{P} 55%,{PL} 120%)"
TOTAL = 10
NFEAT = 8

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

def uri(name):
    return "data:image/png;base64," + base64.b64encode((HERE / f"james/{name}.png").read_bytes()).decode()

FACE = uri("rosto")
FADE = "-webkit-mask-image:linear-gradient(to bottom,#000 72%,transparent 100%);mask-image:linear-gradient(to bottom,#000 72%,transparent 100%);"

def james(name, style):
    return f'<img src="{uri(name)}" style="position:absolute;z-index:1;{FADE}{style}">'

def face(size, border="none"):
    return f'<img src="{FACE}" style="width:{size}px;height:{size}px;border-radius:50%;object-fit:cover;background:{P};border:{border};flex-shrink:0;">'

def slide(i, bg, light, body, last=False, justify="flex-end", art=""):
    return f'''<div class="slide" style="background:{bg};">{art}
<div style="position:absolute;inset:0;z-index:2;padding:30px 46px 58px 34px;display:flex;flex-direction:column;justify-content:{justify};">{body}</div>
{'' if last else arrow(light)}{bar(i, light)}</div>'''

def head(n, title, light, sub):
    tc = DBG if light else '#fff'
    nc = P if light else PL
    sc = MUTED if light else 'rgba(255,255,255,0.65)'
    return f'''<div style="display:flex;align-items:baseline;gap:10px;margin-bottom:10px;">
<span class="serif" style="font-size:26px;font-weight:300;color:{nc};">{n:02d}</span>
<span class="sans" style="font-size:10px;font-weight:600;letter-spacing:2px;color:{nc};">DE {NFEAT:02d}</span></div>
<h2 class="serif" style="font-size:29px;font-weight:700;line-height:1.1;letter-spacing:-0.5px;color:{tc};">{title}</h2>
<p class="sans" style="font-size:13.5px;line-height:1.5;color:{sc};margin-top:10px;">{sub}</p>'''

def bub_in(text, light=True, time="23:14", extra=""):
    bg = '#fff' if light else 'rgba(255,255,255,0.08)'
    bd = LBR if light else 'rgba(255,255,255,0.08)'
    tc = '#2a332d' if light else 'rgba(255,255,255,0.9)'
    return f'''<div style="align-self:flex-start;max-width:78%;background:{bg};border:1px solid {bd};border-radius:14px 14px 14px 4px;padding:8px 12px;{extra}">
<p class="sans" style="font-size:12.5px;color:{tc};line-height:1.35;">{text}</p><p class="sans" style="font-size:9.5px;color:#9aa69e;text-align:right;margin-top:2px;">{time}</p></div>'''

def bub_out(text, time="23:14", extra=""):
    return f'''<div style="align-self:flex-end;max-width:80%;background:#D7F2E2;border-radius:14px 14px 4px 14px;padding:8px 12px;{extra}">
<p class="sans" style="font-size:12.5px;color:#183223;line-height:1.35;">{text}</p><p class="sans" style="font-size:9.5px;color:#5f8a70;text-align:right;margin-top:2px;">{time} · James ✓✓</p></div>'''

def chat(inner, gap=8):
    return f'<div style="display:flex;flex-direction:column;gap:{gap}px;margin-bottom:20px;">{inner}</div>'

def pill(t, light):
    if light:
        return f'<span class="sans" style="font-size:12px;padding:6px 12px;background:#fff;border:1px solid {LBR};border-radius:20px;color:{PD};">{t}</span>'
    return f'<span class="sans" style="font-size:12px;padding:6px 12px;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.08);border-radius:20px;color:{PL};">{t}</span>'

def pills(items, light, mb=20):
    return f'<div style="display:flex;flex-wrap:wrap;gap:7px;margin-bottom:{mb}px;">' + "".join(pill(t, light) for t in items) + '</div>'

S = []

# 1 HERO
S.append(slide(0, LBG, True, f'''
<div style="display:flex;align-items:center;gap:10px;margin-bottom:26px;">{face(36)}
<span class="sans" style="font-size:12px;font-weight:600;letter-spacing:0.5px;color:{DBG};">James · Studio Web 360</span></div>
<span class="sans" style="font-size:10px;font-weight:600;letter-spacing:2px;color:{P};margin-bottom:12px;">ATENDENTE DE IA NO WHATSAPP</span>
<h1 class="serif" style="font-size:33px;font-weight:800;line-height:1.04;letter-spacing:-1px;color:{DBG};"><span style="color:{P};">8 coisas</span> que o James faz no seu WhatsApp enquanto você trabalha</h1>
<p class="sans" style="font-size:13.5px;line-height:1.5;color:{MUTED};margin-top:14px;max-width:178px;">A nº 5 é a que mais economiza o seu tempo. Salva pra mostrar pro seu sócio.</p>
<div style="display:grid;grid-template-columns:repeat(4,30px);gap:6px;margin-top:16px;">''' + "".join(f'<span class="serif" style="width:30px;height:30px;border-radius:8px;background:{"#fff" if k!=4 else P};border:1px solid {LBR if k!=4 else P};display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;color:{DBG if k!=4 else "#fff"};">{k+1}</span>' for k in range(8)) + '</div>',
    justify="flex-start", art=james("joinha", "right:-8px;bottom:40px;height:250px;")))

# 2 — 24h no seu número (dark)
S.append(slide(1, DBG, False, chat(
    bub_in("oi! vocês abrem amanhã? queria marcar", False, "23:41") +
    bub_out("Oi! Abrimos sim, das 9h às 18h. Quer que eu já reserve um horário pra você?", "23:41")) +
    head(1, "Responde 24 horas, no número que você já usa", False,
         "Madrugada, domingo, feriado ou no meio do seu atendimento. Conecta pelo QR code, como o WhatsApp Web, ou pela API oficial da Meta. Mesmo número, mesmas conversas.")))

# 3 — aprende o negócio (light)
S.append(slide(2, LBG, True,
    f'<div style="padding:12px;background:#fff;border:1px solid {LBR};border-radius:14px;margin-bottom:18px;box-shadow:0 6px 18px rgba(14,82,50,0.08);"><p class="sans" style="font-size:10px;font-weight:600;letter-spacing:1.5px;color:{P};margin-bottom:8px;">O QUE O JAMES PRECISA SABER</p>' +
    pills(["serviços", "preços", "horários", "endereço", "formas de pagamento", "o que nunca dizer"], True, 0) + '</div>' +
    head(2, "Aprende o seu negócio em um formulário", True,
         "Você responde uma vez o que ele precisa saber. Tem site? Ele lê e já adianta as respostas. Depois é só testar conversando com ele como se fosse um cliente."),
    art=james("pensando", "right:56px;top:6px;height:235px;")))

# 4 — áudio (dark)
wave = "".join(f'<span style="display:inline-block;width:3px;height:{h}px;background:{PL};border-radius:2px;"></span>' for h in [8,14,20,12,22,16,10,18,24,14,8,16,20,12,6,14,18,10,22,12])
S.append(slide(3, DBG, False, chat(
    f'''<div style="align-self:flex-start;display:flex;align-items:center;gap:10px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.08);border-radius:14px 14px 14px 4px;padding:10px 14px;">
<span style="width:24px;height:24px;border-radius:50%;background:rgba(255,255,255,0.15);display:flex;align-items:center;justify-content:center;"><svg width="10" height="10" viewBox="0 0 10 10"><path d="M2 1l7 4-7 4z" fill="#fff"/></svg></span>
<span style="display:flex;align-items:center;gap:2px;">{wave}</span><span class="sans" style="font-size:10px;color:rgba(255,255,255,0.5);">0:14</span></div>''' +
    f'''<div style="align-self:flex-end;display:flex;align-items:center;gap:10px;background:#D7F2E2;border-radius:14px 14px 4px 14px;padding:10px 14px;">
<span style="width:24px;height:24px;border-radius:50%;background:{P};display:flex;align-items:center;justify-content:center;"><svg width="10" height="10" viewBox="0 0 10 10"><path d="M2 1l7 4-7 4z" fill="#fff"/></svg></span>
<span style="display:flex;align-items:center;gap:2px;">{wave.replace(PL, P)}</span><span class="sans" style="font-size:10px;color:#5f8a70;">0:09</span></div>''', 10) +
    head(3, "Ouve áudio e responde em áudio", False,
         "O cliente manda o áudio de sempre e o James responde falando, numa das 6 vozes que você escolhe. Prefere texto? Ele responde por escrito."),
    art=james("rindo", "right:22px;top:4px;height:235px;")))

# 5 — idiomas (light)
S.append(slide(4, LBG, True, chat(
    bub_in("Hi! Do you have a table for two tonight?", True, "19:02") +
    bub_out("Hi! Yes, we do. Would 8pm work for you?", "19:02") +
    bub_in("¿Aceptan tarjeta de crédito?", True, "19:05", "margin-top:4px;")) +
    head(4, "Fala a língua do cliente", True,
         "Turista ou cliente de fora escreveu em inglês, espanhol ou japonês? Ligando a opção, ele entende e responde na mesma língua, até em áudio.")))

# 6 — agenda (dark)  [nº 5 destaque]
days = ["Seg", "Ter", "Qua", "Qui", "Sex"]
cells = ""
marks = {(0,0):"Marina 9h",(1,1):"Carlos 9h30",(2,2):"Diego 10h",(3,0):"Ana 9h",(4,1):"Renata 10h",(0,2):"Júlia 14h30",(3,2):"Vitor 15h30"}
for r in range(3):
    for c in range(5):
        t = marks.get((c, r))
        if t:
            cells += f'<div class="sans" style="height:30px;border-radius:7px;background:{P};color:#fff;font-size:9px;font-weight:600;display:flex;align-items:center;justify-content:center;">{t}</div>'
        else:
            cells += '<div style="height:30px;border-radius:7px;background:rgba(255,255,255,0.05);border:1px dashed rgba(255,255,255,0.1);"></div>'
cal = f'''<div style="margin-bottom:20px;"><div style="display:grid;grid-template-columns:repeat(5,1fr);gap:5px;margin-bottom:5px;">''' + "".join(f'<span class="sans" style="font-size:10px;color:rgba(255,255,255,0.5);text-align:center;">{d}</span>' for d in days) + f'''</div><div style="display:grid;grid-template-columns:repeat(5,1fr);gap:5px;">{cells}</div>
<p class="sans" style="font-size:10px;color:{PL};margin-top:8px;">● marcado pelo James, sem você tocar em nada</p></div>'''
S.append(slide(5, DBG, False, cal +
    head(5, "Marca, lembra e remarca horários sozinho", False,
         "Consulta o que está livre e marca na conversa. Respeita seu expediente, nunca marca duas vezes, lembra o cliente na véspera e libera o horário se ele cancelar.")))

# 7 — todo mundo junto + Instagram (light)
avs = "".join(f'<div style="display:flex;align-items:center;gap:8px;padding:7px 10px;background:#fff;border:1px solid {LBR};border-radius:10px;"><span class="sans" style="width:22px;height:22px;border-radius:50%;background:#E3EEE6;color:{PD};font-size:9px;font-weight:700;display:flex;align-items:center;justify-content:center;">{n[:2]}</span><span class="sans" style="font-size:11px;color:{DBG};flex:1;">{n}</span><span class="sans" style="font-size:9.5px;color:{P};font-weight:600;">{src} · respondido</span></div>' for n, src in [("Paula C.","WhatsApp"),("Bruno T.","Instagram"),("Helena R.","WhatsApp"),("Tiago N.","WhatsApp")])
S.append(slide(6, LBG, True, f'<div style="display:flex;flex-direction:column;gap:6px;margin-bottom:20px;">{avs}</div>' +
    head(6, "Atende todo mundo ao mesmo tempo", True,
         "Dez clientes escrevendo juntos recebem resposta juntos. Ninguém fica na fila. E ele atende também no direct do Instagram.")))

# 8 — painel (dark)
def stat(n, l):
    return f'<div style="flex:1;padding:12px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.08);border-radius:12px;"><p class="serif" style="font-size:26px;font-weight:700;color:#fff;line-height:1;">{n}</p><p class="sans" style="font-size:10px;color:rgba(255,255,255,0.55);margin-top:4px;">{l}</p></div>'
panel = f'''<div style="margin-bottom:20px;"><div style="display:flex;gap:7px;">{stat(28,"conversas hoje")}{stat(26,"James resolveu")}{stat(9,"horários marcados")}</div>
<div style="margin-top:8px;padding:10px 12px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.08);border-radius:12px;display:flex;justify-content:space-between;align-items:center;">
<span class="sans" style="font-size:11px;color:rgba(255,255,255,0.8);">Diego L. · "Queria um orçamento para 3 pessoas"</span>
<span class="sans" style="font-size:10px;padding:4px 10px;border-radius:20px;background:{PL};color:{PD};font-weight:700;">Assumir</span></div></div>'''
S.append(slide(7, DBG, False, panel +
    head(7, "Você acompanha tudo pelo celular", False,
         "Painel ao vivo com as conversas entrando na hora. Quer responder você mesmo? Um toque desliga o James naquele contato. Sem instalar aplicativo.")))

# 9 — chama você (light)
S.append(slide(8, LBG, True, f'''<div style="margin-bottom:20px;padding:14px 16px;background:#fff;border:1px solid {LBR};border-radius:14px;display:flex;gap:12px;align-items:flex-start;">
{face(34)}
<div><p class="sans" style="font-size:12.5px;font-weight:600;color:{DBG};">James precisa de você</p><p class="sans" style="font-size:11.5px;color:{MUTED};margin-top:2px;line-height:1.4;">Cliente pediu um desconto fora do combinado. Passei a conversa pra você.</p></div></div>''' +
    head(8, "Sabe a hora de chamar você", True,
         "Ele só fala do que você cadastrou: preço, prazo e disponibilidade. Assunto delicado, pedido fora do combinado ou cliente irritado? Ele passa a conversa e avisa."),
    art=james("piscando", "right:56px;top:4px;height:235px;")))

# 10 — CTA
S.append(slide(9, GRAD, False, f'''
<div style="text-align:center;display:flex;flex-direction:column;align-items:center;">
<img src="{uri('sorriso')}" style="height:165px;margin-bottom:6px;{FADE}">
<h2 class="serif" style="font-size:30px;font-weight:700;line-height:1.1;letter-spacing:-0.5px;color:#fff;">Quer ver o James atendendo o <em>seu</em> negócio?</h2>
<div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px;margin:12px 0 16px;">''' +
    "".join(f'<span class="sans" style="font-size:11px;padding:5px 11px;background:rgba(255,255,255,0.12);border-radius:20px;color:#fff;">{t}</span>' for t in ["mensal","sem fidelidade","cancela quando quiser"]) + f'''</div>
<div class="sans" style="display:inline-flex;align-items:center;gap:8px;padding:12px 26px;background:{LBG};color:{PD};font-weight:700;font-size:14px;border-radius:28px;">Comente JAMES</div>
<p class="sans" style="font-size:12.5px;color:rgba(255,255,255,0.85);margin-top:14px;">que eu te mostro como funciona no seu negócio<br>ou acesse <b style="color:#fff;">studioweb360.com.br</b></p>
</div>''', last=True, justify="center"))

faces = ""
for w in (300, 400, 600, 700, 800):
    b = base64.b64encode((HERE / f'fonts/bricolage-grotesque-latin-{w}-normal.woff2').read_bytes()).decode()
    faces += f"@font-face{{font-family:'Bricolage Grotesque';font-weight:{w};font-style:normal;src:url(data:font/woff2;base64,{b}) format('woff2');}}\n"

dots_html = "".join(f'<span class="dot{" on" if i==0 else ""}"></span>' for i in range(TOTAL))
html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Carrossel James</title>
<style>
{faces}
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{background:#e9ece9;display:flex;justify-content:center;padding:28px 0;font-family:'Bricolage Grotesque',sans-serif;}}
.serif,.sans{{font-family:'Bricolage Grotesque',sans-serif;}}
.ig-frame{{width:420px;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 10px 30px rgba(0,0,0,0.12);}}
.ig-header{{display:flex;align-items:center;gap:10px;padding:12px 14px;}}
.ig-av{{width:32px;height:32px;border-radius:50%;background:{P};color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:14px;}}
.carousel-viewport{{width:420px;aspect-ratio:4/5;overflow:hidden;position:relative;cursor:grab;}}
.carousel-track{{display:flex;height:100%;transition:transform .35s ease;}}
.slide{{min-width:420px;width:420px;height:525px;position:relative;overflow:hidden;}}
.ig-dots{{display:flex;justify-content:center;gap:4px;padding:10px 0 2px;}}
.dot{{width:6px;height:6px;border-radius:50%;background:#cfd6d1;}} .dot.on{{background:{P};}}
.ig-actions{{display:flex;gap:14px;padding:8px 14px;}}
.ig-caption{{padding:0 14px 14px;font-size:13px;line-height:1.45;color:#222;}}
</style></head><body>
<div class="ig-frame">
<div class="ig-header"><div class="ig-av" style="overflow:hidden;padding:0;">{face(32)}</div><div><div style="font-size:13px;font-weight:600;">studioweb360.ia</div><div style="font-size:11px;color:#888;">James · atendente de IA no WhatsApp</div></div></div>
<div class="carousel-viewport"><div class="carousel-track">{"".join(S)}</div></div>
<div class="ig-dots">{dots_html}</div>
<div class="ig-actions">
<svg width="24" height="24" fill="none" stroke="#222" stroke-width="2" viewBox="0 0 24 24"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 1 0-7.8 7.8L12 21l8.8-8.6a5.5 5.5 0 0 0 0-7.8z"/></svg>
<svg width="24" height="24" fill="none" stroke="#222" stroke-width="2" viewBox="0 0 24 24"><path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 21l2.1-5.6A8.4 8.4 0 1 1 21 11.5z"/></svg>
<svg width="24" height="24" fill="none" stroke="#222" stroke-width="2" viewBox="0 0 24 24"><path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg>
<svg style="margin-left:auto" width="24" height="24" fill="none" stroke="#222" stroke-width="2" viewBox="0 0 24 24"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg></div>
<div class="ig-caption"><b>studioweb360.ia</b> 8 coisas que o James faz no seu WhatsApp 👆<div style="font-size:10px;color:#999;margin-top:6px;letter-spacing:.5px;">2 HOURS AGO</div></div>
</div>
<script>
const track=document.querySelector('.carousel-track'),vp=document.querySelector('.carousel-viewport'),dots=[...document.querySelectorAll('.dot')];
let idx=0,startX=null;const N={TOTAL};
function go(i){{idx=Math.max(0,Math.min(N-1,i));track.style.transform='translateX('+(-idx*420)+'px)';dots.forEach((d,k)=>d.classList.toggle('on',k===idx));}}
vp.addEventListener('pointerdown',e=>{{startX=e.clientX;}});
window.addEventListener('pointerup',e=>{{if(startX===null)return;const dx=e.clientX-startX;if(Math.abs(dx)>30)go(idx+(dx<0?1:-1));else if(Math.abs(dx)<5)go(idx+(e.clientX-vp.getBoundingClientRect().left>210?1:-1));startX=null;}});
document.addEventListener('keydown',e=>{{if(e.key==='ArrowRight')go(idx+1);if(e.key==='ArrowLeft')go(idx-1);}});
</script></body></html>'''
out = Path("/home/claude/carrossel_james_funcionalidades.html")
out.write_text(html, encoding="utf-8")
print(out)
