#!/usr/bin/env python3
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
    F, FB = 'Ar', 'ArB'
except Exception as e:
    print('Arial não encontrado, usando Helvetica:', e)
    F, FB = 'Helvetica', 'Helvetica-Bold'

# ── Paleta (Tema Escuro Premium do Site) ────────────────────────────────
BG          = HexColor('#07090F')   # Fundo escuro oficial
CARD        = HexColor('#101422')   # Fundo do card central
BORDER      = HexColor('#1E3A5F')   # Borda ciano escurecido
CYAN        = HexColor('#00C8E8')   # Destaque Ciano
AMBER       = HexColor('#F59E0B')   # Botão Amber oficial
NAVY_MID    = HexColor('#0D1B2A')   # Circuitos e decorações
WHITE       = white
GRAY_MID    = HexColor('#94A3B8')   # Texto secundário

W, H = A4   # 595.28 × 841.89 pts
cx = W / 2

# ── Helpers de Desenho ──────────────────────────────────────────────────
def rect_rounded(c, x, y, w, h, fill_color, border_color=None, rx=8, ry=8):
    c.setFillColor(fill_color)
    if border_color:
        c.setStrokeColor(border_color)
        c.setLineWidth(1)
        c.roundRect(x, y, w, h, rx, fill=1, stroke=1)
    else:
        c.roundRect(x, y, w, h, rx, fill=1, stroke=0)

def hline(c, x1, x2, y, color, lw=0.5):
    c.setStrokeColor(color)
    c.setLineWidth(lw)
    c.line(x1, y, x2, y)

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

# ── Main PDF Generation ────────────────────────────────────────────────
def generate_delivery_pdf(out='ia-que-vende-acesso.pdf'):
    c = pdf_canvas.Canvas(out, pagesize=A4)

    # 1. Background completo escuro
    c.setFillColor(BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # 2. Textura sutil de Grid de Pontos (Discreto)
    gap, r0 = 24, 0.8
    cols = int(W / gap) + 2
    rows = int(H / gap) + 2
    for ix in range(cols):
        for iy in range(rows):
            px = ix * gap
            py = iy * gap
            if 0 <= px <= W and 0 <= py <= H:
                dot(c, px, py, r0, NAVY_MID)

    # 3. Decorações de Circuit Traces (Estilo IA)
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.8)
    # Traços no topo
    c.line(0, H - 20*mm, 45*mm, H - 20*mm)
    c.line(45*mm, H - 20*mm, 45*mm, H - 35*mm)
    dot(c, 45*mm, H - 35*mm, 2.5, CYAN)
    
    c.line(W - 45*mm, H - 20*mm, W, H - 20*mm)
    c.line(W - 45*mm, H - 20*mm, W - 45*mm, H - 35*mm)
    dot(c, W - 45*mm, H - 35*mm, 2.5, CYAN)

    # 4. Cabeçalho Principal
    text_c(c, 'PARABÉNS PELA SUA COMPRA!', FB, 10, CYAN, cx, H - 60*mm)
    text_c(c, 'IA QUE VENDE', FB, 38, WHITE, cx, H - 76*mm)
    text_c(c, 'SÉRIE DE PROMPTS AVANÇADOS', F, 9, GRAY_MID, cx, H - 83*mm)
    hline(c, W*0.35, W*0.65, H - 87*mm, CYAN, 1.5)

    # 5. Card Central de Boas-Vindas e Acesso
    card_x = 40
    card_y = 150
    card_w = W - 80
    card_h = 360
    rect_rounded(c, card_x, card_y, card_w, card_h, CARD, BORDER, 12, 12)

    # Conteúdo do Card
    cy_text = card_y + card_h - 40
    text_c(c, 'BOAS-VINDAS AO SEU NOVO MATERIAL!', FB, 14, WHITE, cx, cy_text)
    hline(c, card_x + 30, card_x + card_w - 30, cy_text - 12, BORDER, 0.5)

    # Mensagem Explicativa (Quebras de parágrafo manuais para centralização limpa)
    p_y = cy_text - 45
    msg = [
        "Olá, obrigado por confiar no nosso trabalho!",
        "Para garantir a melhor experiência de leitura e interação no seu celular",
        "ou computador, nós preparamos todo o seu guia completo de prompts",
        "e estratégias em uma página web interativa exclusiva.",
        "",
        "Isso permite que você copie e cole os comandos com apenas um clique,",
        "assista aos tutoriais integrados e acesse as atualizações gratuitas",
        "que fazemos na plataforma em tempo real."
    ]
    
    for line in msg:
        if line == "":
            p_y -= 8
            continue
        text_c(c, line, F, 11, GRAY_MID, cx, p_y)
        p_y -= 18

    # 6. Botão de Acesso Clicável (Chamada para Ação)
    btn_w = 280
    btn_h = 46
    btn_x = cx - (btn_w / 2)
    btn_y = card_y + 40
    
    # Desenhar o botão visual
    rect_rounded(c, btn_x, btn_y, btn_w, btn_h, AMBER, rx=6, ry=6)
    # Texto do botão centralizado verticalmente
    text_c(c, 'CLIQUE AQUI PARA ACESSAR O PORTAL', FB, 11.5, BG, cx, btn_y + 17)

    # ⚠️ LINK CLICÁVEL (O segredo do ReportLab!)
    # A área retangular para clique é definida por (x1, y1, x2, y2)
    link_rect = (btn_x, btn_y, btn_x + btn_w, btn_y + btn_h)
    url_acesso = "https://aleianegocios.com.br/acesso-ia-que-vende/"
    c.linkURL(url_acesso, link_rect, thickness=0)

    # 7. Rodapé do Card
    text_c(c, 'Se o clique não funcionar, acesse: ' + url_acesso, F, 8, GRAY_MID, cx, card_y + 15)

    # 8. Rodapé Geral do PDF
    hline(c, 30*mm, W - 30*mm, 28*mm, BORDER, 0.4)
    text_c(c, 'Suporte e dúvidas: contato@aleianegocios.com.br', F, 8, GRAY_MID, cx, 20*mm)
    text_c(c, 'Aleia Negócios © 2026 · Todos os direitos reservados.', F, 8, GRAY_MID, cx, 14*mm)

    c.save()
    print(f'[OK] PDF interativo de entrega gerado: {out}')

if __name__ == '__main__':
    generate_delivery_pdf()
