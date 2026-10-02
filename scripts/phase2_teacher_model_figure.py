"""
Gera a Figura 4 (Manna-Teacher Model nas quatro fases do framework) em HTML + SVG inline.
Layout e cores reproduzem a Figura 3 (manna-framework-operational-flow.png), para que as duas
figuras sejam lidas como par: faixa lateral clara com o nome da fase, caixas preenchidas na cor
da fase, icone de linha branca, texto branco em maiusculas, setas entre caixas e conector
em zigue-zague entre as linhas. Cores amostradas da Figura 3.
Fontes do conteudo: programacao oficial do Manna no Museu 2025 (14 a 16/03/2025),
Base_Unificada_Manna_87_Respostas_Avaliacao, base de comentarios e termos de compromisso.
Execucao: python gerar_figura4_modelo_docente.py
"""
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "figures" / "html"

PAPER = "#fdfdfd"
CONNECTOR = "#2a3f51"
WHITE = "#ffffff"
SANS = "'Geist', 'Inter', 'Helvetica Neue', Arial, sans-serif"

# (rotulo da faixa em linhas, cor da faixa, cor das caixas, [(icone, linhas do texto)])
ROWS = [
    (["CONCEPTION"], "#d6dce0", "#758d9a", [
        ("design", ["PROGRAM ON AI,", "QUANTUM AND", "INNOVATION"]),
        ("call", ["PUBLIC CALL", "AND SELECTION", "OF EDUCATORS"]),
        ("plan", ["LOGISTICS AND", "RESOURCE", "PLANNING"]),
    ]),
    (["DIAGNOSTIC", "ASSESSMENT"], "#cfe0f2", "#6f9cc4", [
        ("form", ["PROFILE AND", "EXPECTATIONS", "QUESTIONNAIRE"]),
        ("quiz", ["PRE-TEST ON", "EXPONENTIAL", "TECHNOLOGIES"]),
        ("baseline", ["KNOWLEDGE", "BASELINE"]),
    ]),
    (["FORMATIVE", "ASSESSMENT"], "#f6e7c9", "#e9c786", [
        ("teach", ["MINICOURSES", "AND HANDS-ON", "STATIONS"]),
        ("team", ["MANNA VAI", "TEAM DYNAMIC"]),
        ("chat", ["CONTINUOUS", "FEEDBACK", "VIA APP"]),
    ]),
    (["SUMMATIVE", "ASSESSMENT"], "#f0d3d1", "#d48578", [
        ("pitch", ["MANNA SHOW", "PITCHES"]),
        ("gain", ["POST-TEST AND", "HAKE GAIN"]),
        ("commit", ["REPLICATION", "COMMITMENTS"]),
    ]),
]

W, H = 960, 664
SX, SW = 16, 56                 # faixa lateral
BX = [96, 400, 704]             # inicio das 3 caixas
BW, BH = 224, 112
ROW_Y = [32, 192, 352, 512]     # topo de cada linha (passo 160)
R = 8


def icon(kind, x, y):
    """Icone de linha branca, area 48x48 com origem em (x, y)."""
    s = f'fill="none" stroke="{WHITE}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"'
    if kind == "design":    # compasso
        return (f'<circle cx="{x+24}" cy="{y+24}" r="22" {s}/>'
                f'<circle cx="{x+24}" cy="{y+12}" r="3" {s}/>'
                f'<path d="M{x+22} {y+15} L{x+14} {y+38} M{x+26} {y+15} L{x+34} {y+38} M{x+17} {y+30} L{x+31} {y+30}" {s}/>')
    if kind == "call":      # documento com selo
        return (f'<path d="M{x+8} {y+2} H{x+30} L{x+40} {y+12} V{y+46} H{x+8} Z" {s}/>'
                f'<path d="M{x+30} {y+2} V{y+12} H{x+40}" {s}/>'
                f'<path d="M{x+14} {y+20} H{x+34} M{x+14} {y+28} H{x+34} M{x+14} {y+36} H{x+26}" {s}/>')
    if kind == "plan":      # prancheta com checks
        return (f'<rect x="{x+8}" y="{y+6}" width="32" height="40" rx="3" {s}/>'
                f'<rect x="{x+17}" y="{y+2}" width="14" height="8" rx="2" {s}/>'
                f'<path d="M{x+14} {y+20} l3 3 l5 -6 M{x+26} {y+20} H{x+34} M{x+14} {y+33} l3 3 l5 -6 M{x+26} {y+33} H{x+34}" {s}/>')
    if kind == "form":      # formulario com caixas
        return (f'<rect x="{x+6}" y="{y+2}" width="32" height="42" rx="3" {s}/>'
                f'<rect x="{x+12}" y="{y+10}" width="6" height="6" {s}/><path d="M{x+22} {y+13} H{x+32}" {s}/>'
                f'<rect x="{x+12}" y="{y+21}" width="6" height="6" {s}/><path d="M{x+22} {y+24} H{x+32}" {s}/>'
                f'<rect x="{x+12}" y="{y+32}" width="6" height="6" {s}/><path d="M{x+22} {y+35} H{x+28}" {s}/>'
                f'<path d="M{x+36} {y+40} L{x+46} {y+28}" {s}/>')
    if kind == "quiz":      # balao com estrelas/ponto de interrogacao
        return (f'<path d="M{x+4} {y+8} H{x+44} V{y+34} H{x+18} L{x+8} {y+44} V{y+34} H{x+4} Z" {s}/>'
                f'<path d="M{x+19} {y+16} q5 -6 10 0 q2 4 -5 7 v3" {s}/><circle cx="{x+24}" cy="{y+30}" r="1" fill="{WHITE}" stroke="{WHITE}"/>')
    if kind == "baseline":  # barras com linha de base
        return (f'<path d="M{x+4} {y+44} H{x+44}" {s}/>'
                f'<rect x="{x+8}" y="{y+26}" width="8" height="18" {s}/>'
                f'<rect x="{x+20}" y="{y+18}" width="8" height="26" {s}/>'
                f'<rect x="{x+32}" y="{y+30}" width="8" height="14" {s}/>'
                f'<path d="M{x+2} {y+12} H{x+46}" {s} stroke-dasharray="4,3"/>')
    if kind == "teach":     # professor e quadro
        return (f'<rect x="{x+18}" y="{y+4}" width="28" height="20" rx="2" {s}/>'
                f'<circle cx="{x+9}" cy="{y+12}" r="5" {s}/>'
                f'<path d="M{x+3} {y+44} V{y+26} q6 -6 12 0 V{y+44} M{x+15} {y+28} L{x+24} {y+20}" {s}/>'
                f'<circle cx="{x+26}" cy="{y+34}" r="3" {s}/><circle cx="{x+38}" cy="{y+34}" r="3" {s}/>'
                f'<path d="M{x+21} {y+44} q5 -6 10 0 M{x+33} {y+44} q5 -6 10 0" {s}/>')
    if kind == "team":      # tres pessoas
        return (f'<circle cx="{x+24}" cy="{y+12}" r="7" {s}/>'
                f'<path d="M{x+12} {y+42} q12 -20 24 0" {s}/>'
                f'<circle cx="{x+8}" cy="{y+20}" r="5" {s}/><path d="M{x+0} {y+42} q6 -12 14 -8" {s}/>'
                f'<circle cx="{x+40}" cy="{y+20}" r="5" {s}/><path d="M{x+48} {y+42} q-6 -12 -14 -8" {s}/>')
    if kind == "chat":      # pessoa com balao
        return (f'<path d="M{x+20} {y+2} H{x+46} V{y+22} H{x+32} L{x+26} {y+28} V{y+22} H{x+20} Z" {s}/>'
                f'<path d="M{x+26} {y+10} H{x+40} M{x+26} {y+16} H{x+36}" {s}/>'
                f'<circle cx="{x+12}" cy="{y+28}" r="6" {s}/><path d="M{x+2} {y+46} q10 -14 20 0" {s}/>')
    if kind == "pitch":     # tela de apresentacao
        return (f'<rect x="{x+4}" y="{y+4}" width="40" height="28" rx="2" {s}/>'
                f'<path d="M{x+20} {y+12} L{x+30} {y+18} L{x+20} {y+24} Z" {s}/>'
                f'<path d="M{x+24} {y+32} V{y+38} M{x+14} {y+46} L{x+24} {y+38} L{x+34} {y+46}" {s}/>')
    if kind == "gain":      # grafico com seta para cima
        return (f'<path d="M{x+4} {y+44} H{x+44}" {s}/>'
                f'<rect x="{x+8}" y="{y+32}" width="7" height="12" {s}/>'
                f'<rect x="{x+20}" y="{y+24}" width="7" height="20" {s}/>'
                f'<rect x="{x+32}" y="{y+16}" width="7" height="28" {s}/>'
                f'<path d="M{x+6} {y+20} L{x+22} {y+10} L{x+30} {y+14} L{x+44} {y+4} M{x+36} {y+4} H{x+44} V{y+12}" {s}/>')
    if kind == "commit":    # documento com caneta
        return (f'<rect x="{x+4}" y="{y+6}" width="30" height="38" rx="3" {s}/>'
                f'<path d="M{x+10} {y+16} H{x+28} M{x+10} {y+24} H{x+24} M{x+10} {y+34} q4 -6 8 0 q4 6 8 0" {s}/>'
                f'<path d="M{x+30} {y+34} L{x+44} {y+14} L{x+48} {y+18} L{x+34} {y+38} L{x+29} {y+40} Z" {s}/>')
    return ""


def arrow_h(x1, x2, y):
    return (f'<path d="M{x1} {y} H{x2 - 2}" stroke="{CONNECTOR}" stroke-width="2.4" fill="none" '
            f'marker-end="url(#f4-arrow)"/>')


def svg():
    g = []
    a = g.append
    a(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" '
      f'aria-labelledby="teacher-model-title teacher-model-desc">')
    a('<title id="teacher-model-title">Manna-Teacher Model across the four framework phases</title>')
    a('<desc id="teacher-model-desc">Four colour-coded rows, Conception, Diagnostic Assessment, Formative '
      'Assessment and Summative Assessment, each with three steps of the training delivered to educators, '
      'mirroring the layout of the general framework figure; the pre-test establishes the knowledge baseline '
      'and the post-test yields the normalized (Hake) gain.</desc>')
    a(f'<defs><marker id="f4-arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">'
      f'<path d="M1 1 L9 4 L1 7" fill="none" stroke="{CONNECTOR}" stroke-width="1.6" '
      f'stroke-linecap="round" stroke-linejoin="round"/></marker></defs>')
    a(f'<rect width="100%" height="100%" fill="{PAPER}"/>')

    # conectores em zigue-zague entre linhas (desenhados antes das caixas)
    right = BX[2] + BW
    xr = right + 24
    for i in range(3):
        y_out = ROW_Y[i] + BH // 2
        y_mid = ROW_Y[i] + BH + 24
        x_in = BX[0] + 24
        d = (f"M{right} {y_out} H{xr - R} Q{xr} {y_out} {xr} {y_out + R} "
             f"V{y_mid - R} Q{xr} {y_mid} {xr - R} {y_mid} H{x_in + R} "
             f"Q{x_in} {y_mid} {x_in} {y_mid + R} V{ROW_Y[i + 1] - 2}")
        a(f'<path d="{d}" stroke="{CONNECTOR}" stroke-width="2.4" fill="none" marker-end="url(#f4-arrow)"/>')

    for (label, strip, fill, cells), y in zip(ROWS, ROW_Y):
        # faixa lateral com o nome da fase (vertical, como na Figura 3)
        a(f'<rect x="{SX}" y="{y}" width="{SW}" height="{BH}" rx="8" fill="{strip}"/>')
        cx, cy = SX + SW // 2, y + BH // 2
        n = len(label)
        for k, ln in enumerate(label):
            off = (k - (n - 1) / 2) * 15
            a(f'<text transform="rotate(-90 {cx + off} {cy})" x="{cx + off}" y="{cy + 4}" fill="{CONNECTOR}" '
              f'font-size="11" font-weight="600" letter-spacing="0.06em" font-family="{SANS}" '
              f'text-anchor="middle">{ln}</text>')
        for j, ((ic, lines), bx) in enumerate(zip(cells, BX)):
            a(f'<rect x="{bx}" y="{y}" width="{BW}" height="{BH}" rx="8" fill="{fill}"/>')
            a(icon(ic, bx + 16, y + BH // 2 - 24))
            top = y + BH // 2 - (len(lines) - 1) * 9 + 5
            for k, ln in enumerate(lines):
                a(f'<text x="{bx + 80}" y="{top + 18 * k}" fill="{WHITE}" font-size="14" font-weight="700" '
                  f'letter-spacing="0.04em" font-family="{SANS}">{ln}</text>')
            if j < 2:
                a(arrow_h(bx + BW + 16, BX[j + 1] - 16, y + BH // 2))
    a('</svg>')
    return "\n    ".join(g)


PAGE = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Manna-Teacher Model phases</title>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: 'Geist', system-ui, sans-serif; background: {PAPER}; color: {CONNECTOR}; min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 3rem 2rem; }}
    .frame {{ max-width: 1200px; width: 100%; }}
    svg {{ width: 100%; display: block; }}
  </style>
</head>
<body>
  <div class="frame">
    {svg()}
  </div>
</body>
</html>
"""

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    (OUT / "manna-teacher-model-phases.html").write_text(PAGE, encoding="utf-8")
    print("ok", OUT / "manna-teacher-model-phases.html")
