# -*- coding: utf-8 -*-
"""
IA QUE VENDE — Gerador HTML completo
  • Capa embutida (CSS puro)
  • Conteúdo: 13 módulos, 29 mega-prompts
  • @media print  → A4 (Ctrl+P → PDF)
  • @media screen → responsivo (desktop + mobile)
"""
import re, html as hl

SRC = r'C:\Users\Paulo Aleixo\Downloads\ia-que-vende-v2-final6.md'
OUT = 'ia-que-vende-COMPLETO.html'

# ═══════════════════════════════════════════════════════════════════════════
# CSS
# ═══════════════════════════════════════════════════════════════════════════
CSS = """
/* Sem dependência externa — funciona 100% offline */
:root {
  --navy:       #0D1B2A;
  --navy-mid:   #1E3050;
  --navy-dot:   #18273D;
  --cyan:       #00C8E8;
  --cyan-dim:   #007A96;
  --cyan-bg:    #E0F7FA;
  --graphite:   #374151;
  --gray-mid:   #6B7280;
  --gray-light: #F1F5F9;
  --gray-rule:  #E5E7EB;
  --orange:     #F97316;
  --orange-bg:  #FFF7ED;
  --bg:         #F8FAFC;
  --white:      #FFFFFF;
}
* { box-sizing: border-box; margin: 0; padding: 0; }

/* ── base ───────────────────────────────────────────── */
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
  color: var(--graphite);
  line-height: 1.65;
  background: var(--white);
}

/* ══════════════════════════════════════════════════════
   CAPA
══════════════════════════════════════════════════════ */
.cover-page {
  display: flex;
  flex-direction: column;
  background: var(--bg);
  overflow: hidden;
}

/* Bloco navy */
.cover-navy {
  flex: 0 0 60%;
  background-color: var(--navy);
  background-image: radial-gradient(var(--navy-dot) 1.3px, transparent 1.3px);
  background-size: 20px 20px;
  border-bottom: 3px solid var(--cyan);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 14px 24px 16px;
  position: relative;
}

/* Circuit traces SVG (posição absoluta sobre o bloco navy) */
.cover-traces {
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  pointer-events: none;
  overflow: visible;
}

.cover-top-label {
  color: var(--cyan);
  letter-spacing: .14em;
  text-transform: uppercase;
  z-index: 1;
}

.cover-title-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  flex: 1;
  z-index: 1;
}

.cover-ia {
  color: var(--white);
  font-weight: 900;
  line-height: .85;
  letter-spacing: -.02em;
}

.cover-divider-line {
  background: var(--cyan);
  height: 2px;
  width: 72%;
  margin: 10px 0 8px;
}

.cover-que-vende {
  color: var(--white);
  font-weight: 700;
  letter-spacing: .03em;
}

.cover-tagline {
  color: var(--cyan);
  letter-spacing: .12em;
  text-transform: uppercase;
  z-index: 1;
}

/* Seção branca */
.cover-white {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-evenly;
  padding: 12px 24px 10px;
}

.cover-subtitle { color: var(--graphite); text-align: center; line-height: 1.55; }
.cover-sep {
  border: none;
  border-top: .5px solid var(--gray-rule);
  width: 55%;
  margin: 7px auto;
}
.cover-micro { color: var(--gray-mid); text-align: center; }

/* Feature strip */
.cover-features {
  display: flex;
  align-items: center;
  gap: 28px;
}
.cover-feat {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
}
.feat-num { color: var(--navy); font-weight: 700; line-height: 1; }
.feat-accent { width: 18px; height: 2px; background: var(--cyan); margin: 3px 0; }
.feat-lbl { color: var(--gray-mid); text-transform: uppercase; letter-spacing: .08em; font-weight: 500; }
.feat-vsep { width: .5px; background: var(--gray-rule); align-self: stretch; }

/* Badge hexagonal SVG */
.cover-badge-wrap { display: flex; justify-content: center; }
.cover-hex { display: block; }

.cover-footer-text { color: var(--gray-mid); text-align: center; }

/* ══════════════════════════════════════════════════════
   CONTEÚDO
══════════════════════════════════════════════════════ */
.content-wrap { padding-top: 6pt; }

/* ── Tipografia ─────────────────────────────────────── */
h1.section-title {
  font-size: 16pt; font-weight: 700; color: var(--navy);
  margin: 22pt 0 10pt;
  padding-bottom: 6pt;
  border-bottom: 1.5pt solid var(--cyan);
}
h2 { font-size: 13pt; font-weight: 700; color: var(--navy); margin: 18pt 0 8pt; }
h3 { font-size: 11pt; font-weight: 600; color: var(--navy-mid); margin: 14pt 0 6pt; }
p  { margin: 6pt 0; orphans: 3; widows: 3; }
strong { font-weight: 700; color: var(--navy); }
em     { font-style: italic; color: var(--gray-mid); }
code {
  font-family: 'Courier New', monospace;
  background: var(--gray-light);
  padding: 1pt 4pt;
  border-radius: 3pt;
  color: var(--navy);
}
ul, ol { margin: 6pt 0 6pt 18pt; }
li { margin: 3pt 0; line-height: 1.5; }
hr { border: none; border-top: 1pt solid var(--gray-rule); margin: 18pt 0; }

/* ── Module header ──────────────────────────────────── */
.module-header {
  background: var(--navy);
  padding: 18pt 20pt 14pt;
  margin-bottom: 20pt;
  border-bottom: 3pt solid var(--cyan);
}
.module-num {
  font-size: 8pt; color: var(--cyan);
  text-transform: uppercase; letter-spacing: .12em; font-weight: 600;
  margin-bottom: 4pt;
}
.module-title { font-size: 20pt; font-weight: 700; line-height: 1.2; color: var(--white); }

/* ── Badges ─────────────────────────────────────────── */
.prompt-badge {
  display: inline-block;
  background: var(--navy); color: var(--cyan);
  font-size: 7.5pt; font-weight: 700;
  padding: 2pt 9pt; border-radius: 3pt;
  letter-spacing: .08em; margin-bottom: 8pt;
}
.use-tag {
  display: inline-block;
  background: var(--cyan-bg); color: var(--navy);
  font-size: 8pt; font-weight: 600;
  padding: 2pt 8pt; border-radius: 3pt;
  letter-spacing: .04em; text-transform: uppercase;
  margin-bottom: 8pt;
}

/* ── Blocos de conteúdo ─────────────────────────────── */
.block-prompt {
  background: #F8FAFC;
  border: .5pt solid var(--gray-rule);
  border-left: 4pt solid var(--cyan);
  border-radius: 0 5pt 5pt 0;
  padding: 12pt 14pt; margin: 10pt 0 14pt;
}
.block-prompt pre { font-family:'Courier New',monospace; color:var(--graphite); white-space:pre-wrap; word-break:break-word; line-height:1.55; margin:0; }

.block-example {
  background: var(--orange-bg);
  border-left: 4pt solid var(--orange);
  border-radius: 0 5pt 5pt 0;
  padding: 10pt 14pt; margin: 8pt 0 12pt;
}
.block-example::before { content:"EXEMPLO PREENCHIDO"; display:block; font-size:7.5pt; font-weight:700; color:var(--orange); letter-spacing:.1em; margin-bottom:6pt; }
.block-example pre { font-family:'Courier New',monospace; color:#7C3A10; white-space:pre-wrap; word-break:break-word; line-height:1.55; margin:0; }

.block-checklist {
  background: var(--cyan-bg);
  border-left: 4pt solid var(--cyan);
  border-radius: 0 5pt 5pt 0;
  padding: 10pt 14pt; margin: 8pt 0 12pt;
}
.check-item { display:flex; align-items:flex-start; gap:8pt; margin:4pt 0; line-height:1.5; }
.check-box { display:inline-block; width:11pt; height:11pt; border:1.5pt solid var(--cyan); border-radius:2pt; flex-shrink:0; margin-top:1pt; }

.block-framework {
  background: var(--gray-light);
  border: .5pt solid var(--gray-rule);
  border-radius: 5pt;
  padding: 10pt 14pt; margin: 8pt 0 12pt;
}
.block-framework pre { font-family:'Courier New',monospace; color:var(--navy); white-space:pre-wrap; word-break:break-word; line-height:1.6; font-weight:500; margin:0; }

/* ── Callouts ───────────────────────────────────────── */
blockquote {
  background: var(--gray-light);
  border-left: 3.5pt solid var(--navy-mid);
  padding: 8pt 12pt; margin: 10pt 0;
  border-radius: 0 4pt 4pt 0; font-size: 9.5pt;
}
blockquote p { margin: 0; }
.alert {
  background: var(--orange-bg);
  border-left: 3.5pt solid var(--orange);
  padding: 8pt 12pt; margin: 10pt 0;
  border-radius: 0 4pt 4pt 0; font-size: 9.5pt;
}

/* ── Tabelas ────────────────────────────────────────── */
.table-wrap { width:100%; margin:10pt 0 14pt; }
table { width:100%; border-collapse:collapse; }
thead tr { background:var(--navy); color:var(--white); }
thead th { padding:7pt 10pt; text-align:left; font-weight:600; letter-spacing:.04em; }
tbody tr:nth-child(even) { background:var(--gray-light); }
tbody tr:nth-child(odd)  { background:var(--white); }
tbody td { padding:6pt 10pt; border-bottom:.5pt solid var(--gray-rule); vertical-align:top; line-height:1.5; }
tbody tr:last-child td { border-bottom:none; }

/* Intro stats */
.stat-row { display:flex; gap:12pt; margin:12pt 0; }
.stat-box { flex:1; text-align:center; border:.5pt solid var(--gray-rule); border-top:3pt solid var(--cyan); padding:10pt 8pt; border-radius:0 0 4pt 4pt; }
.stat-box .num { font-size:22pt; font-weight:700; color:var(--navy); display:block; }
.stat-box .lbl { font-size:8pt; color:var(--gray-mid); text-transform:uppercase; letter-spacing:.08em; }

/* ══════════════════════════════════════════════════════
   SCREEN — Desktop (preview tipo "documento")
══════════════════════════════════════════════════════ */
@media screen {
  body { background: #D1D5DB; }

  .cover-page {
    max-width: 620px;
    min-height: 877px;
    margin: 28px auto 0;
    box-shadow: 0 8px 40px rgba(0,0,0,.28);
    border-radius: 2px;
  }
  .cover-navy       { min-height: 526px; }
  .cover-ia         { font-size: clamp(70px, 18vw, 145px); }
  .cover-que-vende  { font-size: clamp(32px, 8.5vw, 55px); }
  .cover-top-label  { font-size: 7.5px; }
  .cover-tagline    { font-size: 7.5px; }
  .cover-subtitle   { font-size: 13px; }
  .cover-micro      { font-size: 9px; }
  .feat-num         { font-size: 22px; }
  .feat-lbl         { font-size: 8px; }
  .cover-hex        { width: 118px; height: 118px; }
  .cover-footer-text{ font-size: 8px; }

  .content-wrap {
    max-width: 620px;
    margin: 0 auto 48px;
    background: var(--white);
    padding: 20px 26px 36px;
    box-shadow: 0 2px 16px rgba(0,0,0,.10);
  }

  .module-header { margin-top: 32px; }
  .table-wrap { overflow-x: auto; }

  h1.section-title { font-size: 18px; }
  h2 { font-size: 15px; }
  h3 { font-size: 13px; }
  body { font-size: 14px; }
  .block-prompt pre, .block-example pre, .block-framework pre { font-size: 12.5px; }
  .check-item { font-size: 13px; }
  table { font-size: 12.5px; }
  thead th { font-size: 11px; }
}

/* ══════════════════════════════════════════════════════
   SCREEN — Mobile (≤ 640 px)
══════════════════════════════════════════════════════ */
@media screen and (max-width: 640px) {
  body { background: var(--white); font-size: 15px; }

  .cover-page {
    max-width: 100%;
    min-height: 100svh;
    margin: 0;
    box-shadow: none;
    border-radius: 0;
  }
  .cover-navy       { flex: 0 0 58%; min-height: 0; padding: 12px 16px 14px; }
  .cover-ia         { font-size: 21vw; }
  .cover-que-vende  { font-size: 11vw; }
  .cover-divider-line{ margin: 8px 0 6px; }
  .cover-top-label  { font-size: 6.5px; }
  .cover-tagline    { font-size: 6.5px; }
  .cover-white      { padding: 10px 16px 8px; }
  .cover-subtitle   { font-size: 13px; }
  .cover-micro      { font-size: 8.5px; }
  .feat-num         { font-size: 20px; }
  .feat-lbl         { font-size: 7.5px; }
  .cover-hex        { width: 95px; height: 95px; }
  .cover-footer-text{ font-size: 7.5px; }

  .content-wrap {
    max-width: 100%;
    padding: 16px 14px 28px;
    box-shadow: none;
  }

  h1.section-title { font-size: 17px; margin: 20px 0 9px; }
  h2 { font-size: 14.5px; }
  h3 { font-size: 12.5px; }

  .module-header { padding: 14px 16px 11px; margin-bottom: 16px; }
  .module-title  { font-size: 17px; }

  .block-prompt pre,
  .block-example pre,
  .block-framework pre { font-size: 12px; }
  .check-item    { font-size: 13px; }

  .table-wrap    { overflow-x: auto; -webkit-overflow-scrolling: touch; }
  table          { font-size: 12px; min-width: 380px; }

  .stat-row  { gap: 8px; flex-wrap: wrap; }
  .stat-box  { min-width: calc(50% - 4px); }
  .stat-box .num { font-size: 20px; }
}

/* ══════════════════════════════════════════════════════
   PRINT — A4 PDF
══════════════════════════════════════════════════════ */
@media print {
  /* ── Forçar impressão de cores de fundo ───────────────── */
  *, *::before, *::after {
    -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
  }

  body { background: var(--white); font-size: 10.5pt; }

  /* Primeira página: sem margens (capa sangra até a borda) */
  @page:first { margin: 0; }

  /* Demais páginas: margens A4 + rodapé com número */
  @page {
    size: A4;
    margin: 18mm 16mm 22mm 16mm;
    @bottom-center {
      content: "IA QUE VENDE  ·  " counter(page);
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
      font-size: 7pt; color: #9CA3AF; letter-spacing: .05em;
    }
    @top-right {
      content: "inteligência artificial para pequenos negócios";
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
      font-size: 6.5pt; color: #9CA3AF;
      text-transform: uppercase; letter-spacing: .08em;
    }
  }

  /* Capa: ocupa A4 inteiro (sem margem na primeira página) */
  .cover-page {
    width: 210mm;
    height: 297mm;
    page-break-after: always;
    -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
  }
  .cover-navy {
    flex: 0 0 60%;
    background-color: #0D1B2A !important;
    -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
  }
  .cover-navy * {
    -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
  }
  .cover-ia        { color: #FFFFFF !important; }
  .cover-que-vende { color: #FFFFFF !important; }
  .cover-top-label { color: #00C8E8 !important; }
  .cover-tagline   { color: #00C8E8 !important; }

  .cover-ia         { font-size: 132pt; }
  .cover-que-vende  { font-size: 47pt; }
  .cover-top-label  { font-size: 7pt; }
  .cover-tagline    { font-size: 7pt; }
  .cover-subtitle   { font-size: 11pt; }
  .cover-micro      { font-size: 8pt; }
  .feat-num         { font-size: 18pt; }
  .feat-lbl         { font-size: 7pt; }
  .cover-hex        { width: 112px; height: 112px; }
  .cover-footer-text{ font-size: 7pt; }

  /* Conteúdo: quebras de página */
  .module-header {
    page-break-before: always;
    page-break-inside: avoid;
  }
  .module-header:first-of-type { page-break-before: avoid; }
  h1.section-title, h2, h3 { page-break-after: avoid; }

  .block-prompt, .block-example, .block-checklist,
  .block-framework, blockquote, .alert, .table-wrap {
    page-break-inside: avoid;
  }

  /* Forçar cores em elementos específicos */
  .module-header {
    background-color: #0D1B2A !important;
    -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
  }
  .module-title { color: #FFFFFF !important; }
  .module-num   { color: #00C8E8 !important; }
  thead tr {
    background-color: #0D1B2A !important;
    -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
  }
  thead th { color: #FFFFFF !important; }
  .block-prompt, .block-example, .block-checklist, .block-framework {
    -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
  }

  a::after { content: none !important; }
  a { color: inherit; text-decoration: none; }
}
"""

# ═══════════════════════════════════════════════════════════════════════════
# HTML DA CAPA
# ═══════════════════════════════════════════════════════════════════════════
COVER_HTML = """
<div class="cover-page">

  <!-- Bloco navy -->
  <div class="cover-navy">

    <!-- Circuit traces (SVG absoluto) -->
    <svg class="cover-traces" xmlns="http://www.w3.org/2000/svg"
         viewBox="0 0 620 530" preserveAspectRatio="none">
      <!-- traço esquerda topo -->
      <line x1="0"   y1="90" x2="140" y2="90"  stroke="#1E3A5F" stroke-width="1.5"/>
      <line x1="140" y1="90" x2="140" y2="135" stroke="#1E3A5F" stroke-width="1.5"/>
      <circle cx="140" cy="135" r="4" fill="#00C8E8"/>
      <!-- traço direita topo -->
      <line x1="480" y1="90" x2="620" y2="90"  stroke="#1E3A5F" stroke-width="1.5"/>
      <line x1="480" y1="90" x2="480" y2="135" stroke="#1E3A5F" stroke-width="1.5"/>
      <circle cx="480" cy="135" r="4" fill="#00C8E8"/>
      <!-- traço esquerda base -->
      <line x1="0"   y1="440" x2="76" y2="440" stroke="#1E3A5F" stroke-width="1.5"/>
      <circle cx="76" cy="440" r="4" fill="#00C8E8"/>
      <!-- traço direita base -->
      <line x1="544" y1="440" x2="620" y2="440" stroke="#1E3A5F" stroke-width="1.5"/>
      <circle cx="544" cy="440" r="4" fill="#00C8E8"/>
    </svg>

    <!-- Label topo -->
    <div class="cover-top-label">GUIA DIGITAL &nbsp;·&nbsp; EDIÇÃO 2026</div>

    <!-- Título -->
    <div class="cover-title-wrap">
      <div class="cover-ia">IA</div>
      <div class="cover-divider-line"></div>
      <div class="cover-que-vende">QUE VENDE</div>
    </div>

    <!-- Tagline -->
    <div class="cover-tagline">INTELIGÊNCIA ARTIFICIAL PARA PEQUENOS NEGÓCIOS</div>

  </div><!-- /cover-navy -->

  <!-- Seção branca -->
  <div class="cover-white">

    <div class="cover-subtitle-wrap">
      <p class="cover-subtitle">
        Crie posts, artes, anúncios e mensagens de WhatsApp<br>
        para atrair clientes usando inteligência artificial
      </p>
      <hr class="cover-sep">
      <p class="cover-micro">
        Para donos de pequenos negócios &nbsp;·&nbsp; Sem experiência técnica necessária
      </p>
    </div>

    <!-- Feature strip: 13 | 15 (29 está no badge abaixo) -->
    <div class="cover-features">
      <div class="cover-feat">
        <span class="feat-num">13</span>
        <div class="feat-accent"></div>
        <span class="feat-lbl">Módulos</span>
      </div>
      <div class="feat-vsep"></div>
      <div class="cover-feat">
        <span class="feat-num">15</span>
        <div class="feat-accent"></div>
        <span class="feat-lbl">Nichos</span>
      </div>
    </div>

    <!-- Badge hexagonal SVG -->
    <div class="cover-badge-wrap">
      <svg class="cover-hex" viewBox="0 0 140 140" xmlns="http://www.w3.org/2000/svg">
        <!-- hexágono externo navy -->
        <polygon
          points="126.3,37.5 126.3,102.5 70,135 13.7,102.5 13.7,37.5 70,5"
          fill="#0D1B2A"/>
        <!-- anel interno: só stroke ciano, sem preenchimento -->
        <polygon
          points="119.4,41.5 119.4,98.5 70,127 20.6,98.5 20.6,41.5 70,13"
          fill="none" stroke="#00C8E8" stroke-width="2.5"/>
        <!-- número -->
        <text x="70" y="71"
              text-anchor="middle"
              font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif"
              font-weight="900" font-size="38"
              fill="white">29</text>
        <!-- linha separadora -->
        <line x1="42" y1="78" x2="98" y2="78"
              stroke="#007A96" stroke-width="1.2"/>
        <!-- texto inferior -->
        <text x="70" y="93"
              text-anchor="middle"
              font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif"
              font-weight="400" font-size="10"
              fill="#00C8E8">MEGA-PROMPTS</text>
        <text x="70" y="109"
              text-anchor="middle"
              font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif"
              font-weight="400" font-size="10"
              fill="#00C8E8">PRONTOS</text>
      </svg>
    </div>

    <p class="cover-footer-text">
      Produto digital &nbsp;·&nbsp; Entrega instantânea após o pagamento
    </p>

  </div><!-- /cover-white -->

</div><!-- /cover-page -->
"""

# ═══════════════════════════════════════════════════════════════════════════
# PARSER MARKDOWN → HTML
# ═══════════════════════════════════════════════════════════════════════════

def inline(text):
    text = re.sub(r'`([^`]+)`',
                  lambda m: f'<code>{hl.escape(m.group(1))}</code>', text)
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*(.+?)\*\*',     r'<strong>\1</strong>',          text)
    text = re.sub(r'\*(.+?)\*',         r'<em>\1</em>',                  text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    return text

def detect_code_type(heading, lines):
    text = '\n'.join(lines)
    sl   = [l.strip() for l in lines]
    if any(l.startswith('[ ]') for l in sl):
        return 'checklist'
    if 'MEGA-PROMPT' in heading or heading.startswith('PROMPT '):
        return 'mega-prompt'
    if 'example' in heading.lower():
        return 'example'
    fw = ['C —','O —','A —','T —','CAMADA','===','40%','30%',
          'CRIATIVO','ÂNGULO','MENSAGEM 1','DIA 1','Dia 1']
    if any(p in text for p in fw):
        return 'framework'
    if len(lines) > 6 and any(l.endswith('?') or '[' in l for l in sl):
        return 'mega-prompt'
    return 'framework'

def render_block(btype, lines):
    esc = [hl.escape(l) for l in lines]
    if btype == 'checklist':
        items = []
        for l in lines:
            s = l.strip()
            if s.startswith('[ ]'):
                items.append(
                    f'<div class="check-item">'
                    f'<span class="check-box"></span>'
                    f'{hl.escape(s[3:].strip())}</div>')
            elif s:
                items.append(f'<p style="font-size:9.5pt;margin:3pt 0">'
                             f'{hl.escape(s)}</p>')
        return f'<div class="block-checklist">{"".join(items)}</div>'
    elif btype == 'mega-prompt':
        return f'<div class="block-prompt"><pre>{"".join(l+chr(10) for l in esc).rstrip()}</pre></div>'
    elif btype == 'example':
        return f'<div class="block-example"><pre>{"".join(l+chr(10) for l in esc).rstrip()}</pre></div>'
    else:
        return f'<div class="block-framework"><pre>{"".join(l+chr(10) for l in esc).rstrip()}</pre></div>'

def parse_table(rows):
    if len(rows) < 2:
        return ''
    out = ['<div class="table-wrap"><table><thead><tr>']
    for c in [x.strip() for x in rows[0].strip().strip('|').split('|')]:
        out.append(f'<th>{inline(c)}</th>')
    out.append('</tr></thead><tbody>')
    for row in rows[2:]:
        cells = [x.strip() for x in row.strip().strip('|').split('|')]
        out.append('<tr>')
        for c in cells:
            out.append(f'<td>{inline(c)}</td>')
        out.append('</tr>')
    out.append('</tbody></table></div>')
    return ''.join(out)

def convert(md):
    lines   = md.split('\n')
    out     = []
    i       = 0
    heading = ''
    in_code = False
    code_ln = []
    in_tbl  = False
    tbl_ln  = []
    para    = []
    in_ul   = False
    in_ol   = False

    MOD_RE = re.compile(
        r'^# (MÓDULO\s*\d+|DESAFIO|BÔNUS|PARTE\s+\d+|'
        r'AS IAs|5 PROMPTS|O QUE VOCÊ|COMO USAR|CHECKLISTS|O QUE ESTE GUIA)', re.I)
    H1  = re.compile(r'^# (.+)')
    H2  = re.compile(r'^## (.+)')
    H3  = re.compile(r'^### (.+)')
    BQ  = re.compile(r'^> (.+)')
    UL  = re.compile(r'^[-*] (.+)')
    OL  = re.compile(r'^\d+\. (.+)')
    HR  = re.compile(r'^---+$')
    TB  = re.compile(r'^\|')
    CD  = re.compile(r'^```')

    def fp():
        if para:
            out.append(f'<p>{inline(" ".join(para).strip())}</p>')
            para.clear()
    def cl():
        nonlocal in_ul, in_ol
        if in_ul: out.append('</ul>'); in_ul = False
        if in_ol: out.append('</ol>'); in_ol = False

    while i < len(lines):
        ln = lines[i]

        # ── inside code ──────────────────────────────────
        if in_code:
            if CD.match(ln):
                out.append(render_block(detect_code_type(heading, code_ln), code_ln))
                code_ln = []; in_code = False
            else:
                code_ln.append(ln)
            i += 1; continue

        # ── inside table ─────────────────────────────────
        if in_tbl:
            if TB.match(ln):
                tbl_ln.append(ln); i += 1; continue
            out.append(parse_table(tbl_ln))
            tbl_ln = []; in_tbl = False

        # ── blank ────────────────────────────────────────
        if not ln.strip():
            fp(); cl(); i += 1; continue

        # ── HR ───────────────────────────────────────────
        if HR.match(ln):
            fp(); cl(); out.append('<hr>'); i += 1; continue

        # ── code start ───────────────────────────────────
        if CD.match(ln):
            fp(); cl(); in_code = True; code_ln = []; i += 1; continue

        # ── table ────────────────────────────────────────
        if TB.match(ln):
            fp(); cl(); in_tbl = True; tbl_ln = [ln]; i += 1; continue

        # ── MODULE h1 ────────────────────────────────────
        if MOD_RE.match(ln):
            fp(); cl()
            m = H1.match(ln)
            if m:
                text  = m.group(1)
                heading = text
                nm = re.match(r'(MÓDULO\s*\d+)\s*[—–-]?\s*(.*)', text, re.I)
                if nm:
                    out.append(
                        f'<div class="module-header">'
                        f'<div class="module-num">{nm.group(1).upper()}</div>'
                        f'<div class="module-title">{nm.group(2)}</div></div>')
                else:
                    out.append(
                        f'<div class="module-header">'
                        f'<div class="module-num">SEÇÃO</div>'
                        f'<div class="module-title">{text}</div></div>')
            i += 1; continue

        # ── H1 ───────────────────────────────────────────
        m = H1.match(ln)
        if m:
            fp(); cl()
            text = m.group(1); heading = text
            out.append(f'<h1 class="section-title">{inline(text)}</h1>')
            i += 1; continue

        # ── H2 ───────────────────────────────────────────
        m = H2.match(ln)
        if m:
            fp(); cl()
            text = m.group(1); heading = text
            mp = re.match(r'(MEGA-PROMPT\s*\d+)\s*[—–-]?\s*(.*)', text, re.I)
            if mp:
                out.append(f'<div class="prompt-badge">{mp.group(1).upper()}</div><h2>{inline(mp.group(2))}</h2>')
            else:
                out.append(f'<h2>{inline(text)}</h2>')
            if 'Exemplo preenchido' in text or 'Exemplo' in text:
                heading = 'example'
            i += 1; continue

        # ── H3 ───────────────────────────────────────────
        m = H3.match(ln)
        if m:
            fp(); cl()
            text = m.group(1); heading = text
            pm = re.match(r'(PROMPT\s+[A-Z])\s*[—–-]?\s*(.*)', text, re.I)
            if pm:
                out.append(f'<div class="prompt-badge">{pm.group(1).upper()}</div><h3>{inline(pm.group(2))}</h3>')
                heading = 'mega-prompt'
            else:
                out.append(f'<h3>{inline(text)}</h3>')
            i += 1; continue

        # ── blockquote ───────────────────────────────────
        m = BQ.match(ln)
        if m:
            fp(); cl()
            content = m.group(1)
            um = re.match(r'\*\*Use:\*\*\s*(.*)', content)
            if um:
                out.append(f'<div class="use-tag">Use: {hl.escape(um.group(1))}</div>')
            elif content.startswith('⚠️') or 'Atenção' in content[:10]:
                out.append(f'<div class="alert"><p>{inline(content)}</p></div>')
            else:
                out.append(f'<blockquote><p>{inline(content)}</p></blockquote>')
            i += 1; continue

        # ── UL ───────────────────────────────────────────
        m = UL.match(ln)
        if m:
            fp()
            if not in_ul: cl(); out.append('<ul>'); in_ul = True
            out.append(f'<li>{inline(m.group(1))}</li>')
            i += 1; continue

        # ── OL ───────────────────────────────────────────
        m = OL.match(ln)
        if m:
            fp()
            if not in_ol: cl(); out.append('<ol>'); in_ol = True
            out.append(f'<li>{inline(m.group(1))}</li>')
            i += 1; continue

        # ── parágrafo ────────────────────────────────────
        cl()
        if 'Exemplo preenchido' in ln or ln.strip().startswith('**Exemplo'):
            heading = 'example'
        para.append(ln.strip())
        i += 1

    fp(); cl()
    if in_tbl: out.append(parse_table(tbl_ln))
    return '\n'.join(out)

# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════
def main():
    with open(SRC, 'r', encoding='utf-8') as f:
        md = f.read()

    body = convert(md)

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IA QUE VENDE — Guia Completo</title>
  <style>{CSS}</style>
</head>
<body>

{COVER_HTML}

<div class="content-wrap">

<div class="stat-row">
  <div class="stat-box"><span class="num">13</span><span class="lbl">Módulos</span></div>
  <div class="stat-box"><span class="num">29</span><span class="lbl">Mega-Prompts</span></div>
  <div class="stat-box"><span class="num">15</span><span class="lbl">Nichos</span></div>
  <div class="stat-box"><span class="num">7</span><span class="lbl">Dias de Desafio</span></div>
</div>

{body}

<hr>
<p style="text-align:center;font-size:8.5pt;color:#9CA3AF;margin-top:20pt;">
  <strong>IA QUE VENDE</strong> &nbsp;·&nbsp; Produto digital &nbsp;·&nbsp;
  Entrega instantânea após o pagamento<br>
  Todos os direitos reservados &nbsp;·&nbsp; &copy; 2026
</p>

</div><!-- /content-wrap -->
</body>
</html>"""

    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(html)

    kb = len(html) // 1024
    print(f'[OK] {OUT}  ({kb} KB)')
    print()
    print('COMO USAR:')
    print('  Abrir no Chrome -> Ctrl+P -> Salvar como PDF')
    print('  Configuracoes:  Papel A4 | Margens: Nenhuma | Graficos de fundo: ON')
    print()
    print('CELULAR:')
    print('  Compartilhe o .html — abre no navegador responsivo')
    print('  Ou envie o PDF — legivel com zoom no Adobe/Apple Books')

main()
