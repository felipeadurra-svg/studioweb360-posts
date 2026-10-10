# Identidade visual dos carrosséis — StudioWeb360 / James

Use estes arquivos em todo post do @studioweb360.ia.

## Cores
| Token | Hex | Uso |
|---|---|---|
| Verde principal | `#1E8A55` | destaques, números, barra de progresso |
| Verde claro | `#5FD39A` | destaques em slides escuros |
| Verde escuro | `#0E5232` | âncora do gradiente, texto do botão |
| Fundo claro | `#F1F6F2` | slides claros |
| Borda clara | `#DCE7DF` | divisórias e cards |
| Fundo escuro | `#0D1812` | slides escuros |
| Vermelho alerta | `#E5484D` | só para perda/dinheiro perdido |

Gradiente (capa final/CTA): `linear-gradient(165deg, #0E5232 0%, #1E8A55 55%, #5FD39A 120%)`

## Tipografia
Bricolage Grotesque (300/400/600/700/800), embutida em base64 a partir de `fonts/`.

## Estrutura
- 4:5, 1080×1350 (layout 420×525 exportado com device_scale_factor 2.5714)
- Alterna slide claro / escuro; último slide no gradiente, sem seta
- Barra de progresso + contador em todos; seta de deslizar em todos menos o último
- Mini-mockups (bolhas de WhatsApp, agenda, painel) em vez de só texto
- Chamada final: "Comente JAMES" + studioweb360.com.br

## James (PNG com fundo transparente em `james/`)
| Arquivo | Expressão | Bom para |
|---|---|---|
| `joinha.png` | meio corpo, joinha, na mesa | capa |
| `sorriso.png` | sorriso, busto | chamada final |
| `rindo.png` | rindo, boca aberta | áudio, conversa, alegria |
| `pensando.png` | mão no queixo | aprender, dúvida, "você já pensou" |
| `piscando.png` | piscadela | "pode deixar", confiança |
| `rosto-sorriso.png` | rosto quadrado | fonte do avatar |
| `avatar-circulo-160.png` | rosto recortado | avatar em círculo (cabeçalho, notificação) |

Posicionamento: no máximo ~5 slides com James; imagem com fade na base
(`mask-image: linear-gradient(to bottom,#000 72%,transparent)`) saindo de trás de um card.

### Expressões extras (`james/expressoes/`, ~250×300 px, recortadas da folha de 20)
Resolução menor: usar até ~200px de altura no layout de 420px (avatar, cantos, cards).
Para destaque grande, preferir os PNGs da tabela acima.

| Arquivo | Bom para |
|---|---|
| `acenando.png` | capa, chamada final, "oi!" |
| `apontando-lado.png` | chamar atenção para número/card ao lado |
| `apresentando.png` | apresentar um recurso, "olha isso" |
| `maos-abertas.png` | "bem-vindo", oferta, "é simples assim" |
| `segurando-celular.png` | painel no celular, WhatsApp |
| `notebook.png` | plataforma, configuração, trabalho |
| `prancheta.png` | formulário, cadastro, anotar pedido/agenda |
| `ouvindo-headset.png` | ouvir áudio, atendimento |
| `ideia-lampada.png` | dica, "sabia que…" |
| `um-momento.png` | "atenção", "só um detalhe", regra importante |
| `surpreso.png` | dado chocante, "você perdeu quanto?!" |
| `pensando-2.png` | dúvida, pergunta, objeção |
| `olhar-de-lado.png` | ironia, "o chatbot que você odiou" |
| `bracos-cruzados.png` | confiança, autoridade |
| `comemorando.png` | resultado, conquista, venda fechada |
| `gargalhada.png` | humor, leveza |
| `piscando-2.png` | "pode deixar", segredo |
| `joinha-2.png` | aprovação, confirmação |
| `coracao-maos.png` | agradecimento, cliente feliz |
| `cafe.png` | madrugada/rotina, "enquanto você descansa" |

## Template
`template/build_carrossel_funcionalidades.py` gera o HTML (componentes: barra, seta, bolhas,
pills, cabeçalho numerado). `template/export_slides.py <html> <saida> 2.5714 <n_slides>` exporta PNGs.
Publicação: JPG no repositório → URLs raw.githubusercontent.com → carrossel via Windsor (Instagram).

### Expressões novas (out/2026, `james/expressoes/`, ~300 px, fundo transparente)
Mesma regra de tamanho das extras: até ~200 px de altura no layout de 420 px.
Não usar mais o James fazendo joinha (pedido do Felipe); as versões com joinha da folha nova não foram incluídas.

| Arquivo | Bom para |
|---|---|
| `chocado.png` | mãos no rosto: notícia chocante, "você não vai acreditar", prejuízo |
| `desconfiado.png` | braços cruzados, sobrancelha franzida: boato, "será?", mito x verdade |
| `rindo-alto.png` | gargalhada de olhos fechados: humor, meme, situação absurda |
| `pensando-3.png` | mão no queixo olhando pra cima: pergunta, quiz, "e se…" |
| `acenando-2.png` | aceno com sorriso: abertura, "oi!", despedida, chamada final |
| `apontando-voce.png` | aponta pra câmera e pisca: "é com você", "você que tem negócio", CTA |
| `preocupado.png` | olhar triste: cliente perdido, dono sobrecarregado, problema |
| `notebook-2.png` | no notebook sorrindo: painel, configuração, plataforma por dentro |
| `comemorando-2.png` | punhos fechados: venda fechada, resultado, meta batida |
| `oculos-escuros.png` | ajustando óculos escuros: tranquilidade, fim de semana, "deixa comigo" |
| `bocejando.png` | bocejo: madrugada, cansaço do dono, mensagem às 23h |
| `coracao-maos-2.png` | coração com as mãos: agradecimento, datas comemorativas, cliente feliz |
| `segredo.png` | dedo nos lábios: dica, "segredo", bastidores |
| `confuso.png` | coçando a cabeça: dúvida, áudio de 3 minutos, cliente confuso |

### Corpo inteiro (out/2026, `james/corpo-inteiro/`, ~250×630 px, fundo transparente)
Para cenas de Reel e capas em que o James aparece de pé, inteiro ou cortado na cintura. As versões com joinha da folha (de pé e sentado à mesa) não foram incluídas.

| Arquivo | Bom para |
|---|---|
| `corpo-apontando-cracha.png` | "sou eu", apresentar o James, apontar para um card ao lado |
| `corpo-notebook.png` | segurando notebook: painel, configurar, plataforma |
| `corpo-pensando.png` | mão no queixo: dúvida, pergunta, "e se…" |
| `corpo-comemorando.png` | punhos pra cima: venda fechada, resultado, conquista |
| `corpo-celular-andando.png` | andando ao telefone: atendimento em movimento, "atende onde você estiver" |
| `corpo-tablet.png` | anotando no tablet: pedido, agenda, cadastro |
| `corpo-apresentando.png` | mão aberta para o lado: apresentar recurso, card ou tela ao lado |
| `corpo-cafe.png` | encostado com café: rotina, segunda de manhã, "enquanto você descansa" |
