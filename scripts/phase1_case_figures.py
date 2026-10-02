"""
Gera as figuras dos 4 estudos de caso da Fase 1 (HTML + SVG inline, sistema diagram-design, perfil manna-a4).
Fonte: base original anonimizada em phase1-students/data (CSVs dos Kahoots, 9 sessoes x 5 questoes).
Metrica: percentual de acertos do grupo em cada Kahoot = X marcados / (alunos do grupo x 5).
Execucao: python gerar_figuras_fase1.py
"""
import csv
from pathlib import Path

BASE = Path(__file__).resolve().parents[1] / "phase1-students" / "data"
OUT = Path(__file__).resolve().parents[1] / "figures" / "html"

CASES = [
    (1, "Maringá", "Case1_grup_experiment.csv", "Case1_grup_control.csv"),
    (2, "Campo Mourão", "Case2_group_experiment.csv", "Case2_group_control.csv"),
    (3, "Cianorte", "Case3_group_Experimental.csv", "Case3_group_control.csv"),
    (4, "Paranavaí", "Case4_group_experimental.csv", "Case4_group_control.csv"),
]

# perfil manna-a4
PAPER, INK, MUTED, ACCENT = "#ffffff", "#1A2133", "#3380B0", "#D4510D"
SOFT_TXT = "#4a5468"
GRID, AXIS = "rgba(26,33,51,0.10)", "rgba(26,33,51,0.35)"
MONO, SANS, SERIF = "'Geist Mono', monospace", "'Geist', sans-serif", "'Instrument Serif', serif"

# geometria (grade de 4px)
W, H = 640, 424
X0, X1, Y0, Y1 = 64, 616, 24, 324          # area de plotagem; y=324 corresponde a 0%
XS = [84 + 64 * i for i in range(9)]       # 84 ... 596
def y(p): return round(Y1 - 3 * p, 1)      # 3px por ponto percentual


def load(path):
    rows = list(csv.reader(open(path, encoding="utf-8-sig")))
    return [[c.strip().upper() == "X" for c in r[1:46]] for r in rows[1:] if r and r[0].strip()]


def pct(data):
    return [100 * sum(sum(v[5 * k:5 * k + 5]) for v in data) / (5 * len(data)) for k in range(9)]


def svg(n, city, pe, pc, ne, nc):
    slug = f"phase1-case{n}"
    g = []
    a = g.append
    a(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" '
      f'aria-labelledby="{slug}-title {slug}-desc">')
    a(f'<title id="{slug}-title">Case Study {n} ({city}): correct answers per formative assessment</title>')
    a(f'<desc id="{slug}-desc">Line chart of the percentage of correct answers of the experimental group '
      f'(n = {ne}) and the control group (n = {nc}) in each of the nine Kahoot formative assessments of '
      f'Case Study {n}. Experimental ranges from {pe[0]:.1f}% to {pe[-1]:.1f}%; control from {pc[0]:.1f}% '
      f'to {pc[-1]:.1f}%.</desc>')
    a(f'<rect width="100%" height="100%" fill="{PAPER}"/>')
    # grade e eixo Y
    for v in range(0, 101, 20):
        yy = y(v)
        a(f'<line x1="{X0}" y1="{yy}" x2="{X1}" y2="{yy}" stroke="{GRID}" stroke-width="0.8"/>')
        a(f'<text x="{X0 - 8}" y="{yy + 4}" fill="{SOFT_TXT}" font-size="12" font-family="{MONO}" '
          f'text-anchor="end">{v}</text>')
    a(f'<line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y1}" stroke="{AXIS}" stroke-width="1"/>')
    a(f'<line x1="{X0}" y1="{Y1}" x2="{X1}" y2="{Y1}" stroke="{AXIS}" stroke-width="1"/>')
    a(f'<text transform="rotate(-90 16 {(Y0 + Y1) // 2})" x="16" y="{(Y0 + Y1) // 2}" fill="{SOFT_TXT}" '
      f'font-size="12" font-family="{SANS}" text-anchor="middle">Correct answers (%)</text>')
    # eixo X
    for i, x in enumerate(XS):
        a(f'<text x="{x}" y="{Y1 + 20}" fill="{SOFT_TXT}" font-size="12" font-family="{MONO}" '
          f'text-anchor="middle">K{i + 1}</text>')
    a(f'<text x="{(X0 + X1) // 2}" y="{Y1 + 44}" fill="{SOFT_TXT}" font-size="12" font-family="{SANS}" '
      f'text-anchor="middle">Formative assessment (Kahoot session)</text>')
    # controle (nao focal, tracejado para leitura em escala de cinza)
    pts = " ".join(f"{x},{y(p)}" for x, p in zip(XS, pc))
    a(f'<polyline points="{pts}" fill="none" stroke="{MUTED}" stroke-width="1.6" '
      f'stroke-dasharray="6,4" stroke-linejoin="round"/>')
    # experimental (focal)
    pts = " ".join(f"{x},{y(p)}" for x, p in zip(XS, pe))
    a(f'<polyline points="{pts}" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linejoin="round"/>')
    for x, p in zip(XS, pe):
        a(f'<circle cx="{x}" cy="{y(p)}" r="4" fill="{ACCENT}"/>')
    # legenda (faixa inferior)
    ly = 392
    a(f'<line x1="{X0}" y1="{ly - 12}" x2="{X1}" y2="{ly - 12}" stroke="{GRID}" stroke-width="0.8"/>')
    a(f'<line x1="{X0}" y1="{ly + 8}" x2="{X0 + 28}" y2="{ly + 8}" stroke="{ACCENT}" stroke-width="2"/>')
    a(f'<circle cx="{X0 + 14}" cy="{ly + 8}" r="4" fill="{ACCENT}"/>')
    a(f'<text x="{X0 + 36}" y="{ly + 12}" fill="{INK}" font-size="12" font-family="{SANS}">'
      f'Experimental group (n = {ne})</text>')
    lx = X0 + 280
    a(f'<line x1="{lx}" y1="{ly + 8}" x2="{lx + 28}" y2="{ly + 8}" stroke="{MUTED}" stroke-width="1.6" '
      f'stroke-dasharray="6,4"/>')
    a(f'<text x="{lx + 36}" y="{ly + 12}" fill="{INK}" font-size="12" font-family="{SANS}">'
      f'Control group (n = {nc})</text>')
    a('</svg>')
    return "\n      ".join(g)


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Case Study {n} · {city}</title>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    :root {{ --color-paper:{paper}; --color-ink:{ink}; --color-muted:{muted}; --font-sans:'Geist',system-ui,sans-serif; --font-serif:'Instrument Serif',serif; --font-mono:'Geist Mono',ui-monospace,monospace; }}
    body {{ font-family: var(--font-sans); background: var(--color-paper); color: var(--color-ink); min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 3rem 2rem; }}
    .frame {{ max-width: 880px; width: 100%; }}
    svg {{ width: 100%; display: block; }}
  </style>
</head>
<body>
  <div class="frame">
    {svg}
  </div>
</body>
</html>
"""

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for n, city, fe, fc in CASES:
        e, c = load(BASE / f"case-study-{n}" / fe), load(BASE / f"case-study-{n}" / fc)
        pe, pc = pct(e), pct(c)
        html = PAGE.format(n=n, city=city, paper=PAPER, ink=INK, muted=MUTED,
                           svg=svg(n, city, pe, pc, len(e), len(c)))
        (OUT / f"phase1-case{n}.html").write_text(html, encoding="utf-8")
        print(f"Caso {n} {city}: E n={len(e)} {[round(p, 1) for p in pe]}")
        print(f"          C n={len(c)} {[round(p, 1) for p in pc]}")
