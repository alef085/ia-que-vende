from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas as pdf_canvas
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os, math

# ── Fonts (Arial suporta caracteres portugueses) ───────────────────────
fd = 'C:/Windows/Fonts/'
try:
    pdfmetrics.registerFont(TTFont('Ar',     fd + 'arial.ttf'))
    pdfmetrics.registerFont(TTFont('ArB',    fd + 'arialbd.ttf'))
    pdfmetrics.registerFont(TTFont('ArI',    fd + 'ariali.ttf'))
    F, FB = 'Ar', 'ArB'
except Exception as e:
    print('Arial não encontrado, usando Helvetica:', e)
    F, FB = 'Helvetica', 'Helvetica-Bold'

# ── Paleta ─────────────────────────────────────────────────────────────
BG          = HexColor('#F8FAFC')   # fundo quase branco
NAVY        = HexColor('#0D1B2A')   # azul marinho profundo
NAVY_MID    = HexColor('#13263C')   # navy levemente mais claro (grid)
NAVY_TRACE  = HexColor('#1E3A5F')   # circuit traces
CYAN        = HexColor('#00C8E8')   # destaque ciano
CYAN_DIM    = HexColor('#007A96')   # ciano escurecido
GRAPHITE    = HexColor('#374151')   # texto principal (branco)
GRAY_MID    = HexColor('#6B7280')   # texto secundário
GRAY_RULE   = HexColor('#D1D5DB')   # linhas sutis
WHITE       = white

W, H = A4   # 595.28 × 841.89 pts

# ── Helpers ────────────────────────────────────────────────────────────
def rect(c, x, y, w, h, fill_color, stroke=False, stroke_color=None, lw=1):
    c.setFillColor(fill_color)
    if stroke:
        c.setStrokeColor(stroke_color or fill_color)
        c.setLineWidth(lw)
        c.rect(x, y, w, h, fill=1, stroke=1)
    else:
        c.rect(x, y, w, h, fill=1, stroke=0)

def hline(c, x1, x2, y, color, lw=0.5):
    c.setStrokeColor(color)
    c.setLineWidth(lw)
    c.line(x1, y, x2, y)

def vline(c, x, y1, y2, color, lw=0.5):
    c.setStrokeColor(color)
    c.setLineWidth(lw)
    c.line(x, y1, x, y2)

def text_c(c, txt, font, size, color, cx, y):
    c.setFillColor(color)
    c.setFont(font, size)
    c.drawCentredString(cx, y, txt)

def text_l(c, txt, font, size, color, x, y):
    c.setFillColor(color)
    c.setFont(font, size)
    c.drawString(x, y, txt)

def dot(c, x, y, r, color):
    c.setFillColor(color)
    c.circle(x, y, r, fill=1, stroke=0)

def hexagon(c, cx, cy, r, fill_color=None, stroke_color=None, lw=0):
    """Desenha hexágono. fill_color=None = só stroke (sem preenchimento)."""
    path = c.beginPath()
    for i in range(6):
        angle = math.radians(60 * i - 30)
        px = cx + r * math.cos(angle)
        py = cy + r * math.sin(angle)
        if i == 0:
            path.moveTo(px, py)
        else:
            path.lineTo(px, py)
    path.close()
    do_fill   = fill_color is not None
    do_stroke = stroke_color is not None
    if do_fill:
        c.setFillColor(fill_color)
    if do_stroke:
        c.setStrokeColor(stroke_color)
        c.setLineWidth(lw)
    c.drawPath(path, fill=1 if do_fill else 0, stroke=1 if do_stroke else 0)

# ── Main ───────────────────────────────────────────────────────────────
def draw_cover(out='ia-que-vende-capa-v4.pdf'):
    c = pdf_canvas.Canvas(out, pagesize=A4)

    # ────────────────────────────────────────────────
    # 1. BACKGROUND
    # ────────────────────────────────────────────────
    rect(c, 0, 0, W, H, BG)

    # ────────────────────────────────────────────────
    # 2. NAVY BLOCK (top 60% da página)
    # ────────────────────────────────────────────────
    split   = H * 0.40          # y do corte (do fundo)
    navy_h  = H - split         # altura do bloco navy

    rect(c, 0, split, W, navy_h, NAVY)

    # ── Dot-grid texture dentro do navy ──
    gap, r0 = 22, 1.1
    cols = int(W / gap) + 2
    rows = int(navy_h / gap) + 2
    for ix in range(cols):
        for iy in range(rows):
            px = ix * gap
            py = split + iy * gap
            if 0 <= px <= W and split <= py <= H:
                dot(c, px, py, r0, NAVY_MID)

    # ── Circuit traces (decoração sutil) ──
    c.setStrokeColor(NAVY_TRACE)
    c.setLineWidth(0.8)
    ty = H - 18*mm
    # traço esquerda
    c.line(0, ty, 50*mm, ty)
    c.line(50*mm, ty, 50*mm, ty - 14*mm)
    # traço direita
    c.line(W - 50*mm, ty, W, ty)
    c.line(W - 50*mm, ty, W - 50*mm, ty - 14*mm)
    # traço central inferior
    low_ty = split + navy_h * 0.15
    c.line(0, low_ty, 28*mm, low_ty)
    c.line(W - 28*mm, low_ty, W, low_ty)

    # ── Nós ciano nas junções ──
    dot(c, 50*mm,       ty - 14*mm, 2.8, CYAN)
    dot(c, W - 50*mm,   ty - 14*mm, 2.8, CYAN)
    dot(c, 28*mm,       low_ty,     2.8, CYAN)
    dot(c, W - 28*mm,   low_ty,     2.8, CYAN)

    # ────────────────────────────────────────────────
    # 3. LABEL TOPO
    # ────────────────────────────────────────────────
    label_y = H - 8.5*mm
    text_c(c, 'GUIA DIGITAL  ·  EDIÇÃO 2026', F, 7, CYAN, W/2, label_y)
    hline(c, W*0.38, W*0.62, label_y - 3.5, CYAN_DIM, 0.4)

    # ────────────────────────────────────────────────
    # 4. TÍTULO PRINCIPAL
    # ────────────────────────────────────────────────
    ia_y  = split + navy_h * 0.56
    qv_y  = split + navy_h * 0.32
    div_y = split + navy_h * 0.45

    # "IA" — monumental
    text_c(c, 'IA', FB, 152, WHITE, W/2, ia_y)

    # Linha divisora cyan
    hline(c, W*0.14, W*0.86, div_y, CYAN, 1.8)

    # "QUE VENDE"
    text_c(c, 'QUE VENDE', FB, 48, WHITE, W/2, qv_y)

    # ────────────────────────────────────────────────
    # 5. TAGLINE DENTRO DO NAVY
    # ────────────────────────────────────────────────
    tag_y = split + navy_h * 0.16
    text_c(c, 'INTELIGÊNCIA ARTIFICIAL PARA PEQUENOS NEGÓCIOS', F, 8.5, CYAN, W/2, tag_y)

    # ────────────────────────────────────────────────
    # 6. FAIXA CYAN NA DIVISÃO
    # ────────────────────────────────────────────────
    rect(c, 0, split - 3, W, 3, CYAN)

    # ────────────────────────────────────────────────
    # 7. ÁREA BRANCA — SUBTÍTULO
    # ────────────────────────────────────────────────
    sub_y = split - 20*mm
    text_c(c, 'Crie posts, artes, anúncios e mensagens de WhatsApp', F, 12, GRAPHITE, W/2, sub_y)
    text_c(c, 'para atrair clientes usando inteligência artificial',  F, 12, GRAPHITE, W/2, sub_y - 18)

    hline(c, W*0.22, W*0.78, sub_y - 31, GRAY_RULE, 0.5)

    text_c(c, 'Para donos de pequenos negócios · Sem experiência técnica necessária',
           F, 8.5, GRAY_MID, W/2, sub_y - 44)

    # ────────────────────────────────────────────────
    # 8. FEATURE STRIP (2 pilares — 29 está no badge)
    # ────────────────────────────────────────────────
    fs_y = sub_y - 76
    fs_items = [
        ('13', 'Módulos'),
        ('15', 'Nichos'),
    ]
    # Dois itens: posicionados simetricamente em relação ao centro
    xs = [W/2 - 55, W/2 + 55]
    for i, (num, lbl) in enumerate(fs_items):
        cx = xs[i]
        text_c(c, num, FB, 20, NAVY,    cx, fs_y)
        text_c(c, lbl, F,   8, GRAY_MID, cx, fs_y - 14)
        hline(c, cx - 8, cx + 8, fs_y - 3, CYAN, 1.2)

    # Uma linha vertical separadora central
    c.setStrokeColor(GRAY_RULE)
    c.setLineWidth(0.4)
    c.line(W/2, fs_y + 18, W/2, fs_y - 18)

    # ────────────────────────────────────────────────
    # 9. BADGE HEXAGONAL — maior, texto legível
    # ────────────────────────────────────────────────
    bx, by, br = W/2, 40*mm, 62

    # Hexágono externo navy (preenchido)
    hexagon(c, bx, by, br, fill_color=NAVY)
    # Anel interno: SÓ stroke ciano, sem preenchimento (não cobre texto)
    hexagon(c, bx, by, br - 8, fill_color=None, stroke_color=CYAN, lw=2.0)

    # Número "29" — grande, branco sobre navy
    text_c(c, '29',           FB, 40, WHITE, bx, by + 14)

    # Linha separadora fina ciano entre número e texto
    hline(c, bx - 28, bx + 28, by + 8, CYAN_DIM, 0.8)

    # Texto inferior
    text_c(c, 'MEGA-PROMPTS', F,  10, CYAN,  bx, by - 8)
    text_c(c, 'PRONTOS',      F,  10, CYAN,  bx, by - 22)

    # ────────────────────────────────────────────────
    # 10. RODAPÉ
    # ────────────────────────────────────────────────
    hline(c, 18*mm, W - 18*mm, 16*mm, GRAY_RULE, 0.4)
    text_c(c, 'Produto digital · Entrega instantânea após o pagamento', F, 7.5, GRAY_MID, W/2, 11*mm)

    # ────────────────────────────────────────────────
    # SAVE
    # ────────────────────────────────────────────────
    c.save()
    print(f'[OK] Capa salva: {out}')

draw_cover()
