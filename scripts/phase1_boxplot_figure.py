"""
Gera a Figura 9 (boxplot da Fase 1) em HTML + SVG inline, sistema diagram-design, perfil manna-a4.
Fonte: base original anonimizada em phase1-students/data.
Variavel: percentual de acertos de cada aluno nos 45 itens formativos (9 Kahoots x 5 questoes);
celula vazia = sem acerto. Uma caixa por grupo em cada estudo de caso.
Quartis pelo metodo linear (numpy.percentile); bigodes ate 1,5 x IQR; pontos alem disso = atipicos.
Execucao: python gerar_figura9_boxplot.py
"""
import csv
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parents[1] / "phase1-students" / "data"
OUT = Path(__file__).resolve().parents[1] / "figures" / "html"

CASES = [
    (1, "Maringá", "Case1_grup_experiment.csv", "Case1_grup_control.csv"),
    (2, "Campo Mourão", "Case2_group_experiment.csv", "Case2_group_control.csv"),
    (3, "Cianorte", "Case3_group_Experimental.csv", "Case3_group_control.csv"),
    (4, "Paranavaí", "Case4_group_experimental.csv", "Case4_group_control.csv"),
]

PAPER, INK, MUTED, ACCENT = "#ffffff", "#1A2133", "#3380B0", "#D4510D"
ACCENT_TINT, MUTED_TINT = "rgba(212,81,13,0.10)", "rgba(51,128,176,0.08)"
SOFT_TXT = "#4a5468"
GRID, AXIS = "rgba(26,33,51,0.10)", "rgba(26,33,51,0.35)"
MONO, SANS = "'Geist Mono', monospace", "'Geist', sans-serif"

W, H = 640, 424
X0, X1, Y0, Y1 = 64, 616, 24, 324
GW = (X1 - X0) / 4          # largura de cada grupo de cidade
BW = 40                     # largura da caixa
def y(p): return round(Y1 - 3 * p, 1)


def scores(path):
    rows = list(csv.reader(open(path, encoding="utf-8-sig")))
    return np.array([100 * sum(c.strip().upper() == "X" for c in r[1:46]) / 45
                     for r in rows[1:] if r and r[0].strip()])


def stats(x):
    q1, med, q3 = np.percentile(x, [25, 50, 75])
    iqr = q3 - q1
    lo, hi = x[x >= q1 - 1.5 * iqr].min(), x[x <= q3 + 1.5 * iqr].max()
    out = x[(x < q1 - 1.5 * iqr) | (x > q3 + 1.5 * iqr)]
    return q1, med, q3, lo, hi, out


def box(a, cx, st, stroke, fill, dash):
    q1, med, q3, lo, hi, out = st
    d = ' stroke-dasharray="5,3"' if dash else ""
    a(f'<line x1="{cx}" y1="{y(hi)}" x2="{cx}" y2="{y(q3)}" stroke="{stroke}" stroke-width="1.2"{d}/>')
    a(f'<line x1="{cx}" y1="{y(q1)}" x2="{cx}" y2="{y(lo)}" stroke="{stroke}" stroke-width="1.2"{d}/>')
    for v in (hi, lo):
        a(f'<line x1="{cx - 8}" y1="{y(v)}" x2="{cx + 8}" y2="{y(v)}" stroke="{stroke}" stroke-width="1.2"/>')
    h = max(y(q1) - y(q3), 1.5)
    a(f'<rect x="{cx - BW / 2}" y="{y(q3)}" width="{BW}" height="{h}" rx="2" fill="{fill}" '
      f'stroke="{stroke}" stroke-width="1.4"{d}/>')
    a(f'<line x1="{cx - BW / 2}" y1="{y(med)}" x2="{cx + BW / 2}" y2="{y(med)}" stroke="{stroke}" stroke-width="2.4"/>')
    for v in out:
        a(f'<circle cx="{cx}" cy="{y(v)}" r="3.2" fill="{PAPER}" stroke="{stroke}" stroke-width="1.2"/>')


def svg(data):
    a = []
    ap = a.append
    ap(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" '
       f'aria-labelledby="phase1-box-title phase1-box-desc">')
    ap('<title id="phase1-box-title">Distribution of formative scores by group in the four case studies</title>')
    ap('<desc id="phase1-box-desc">Box plots of each student\'s percentage of correct answers across the nine '
       'Kahoot formative assessments, for the experimental and control groups of Maringá, Campo Mourão, '
       'Cianorte and Paranavaí.</desc>')
    ap(f'<rect width="100%" height="100%" fill="{PAPER}"/>')
    for v in range(0, 101, 20):
        ap(f'<line x1="{X0}" y1="{y(v)}" x2="{X1}" y2="{y(v)}" stroke="{GRID}" stroke-width="0.8"/>')
        ap(f'<text x="{X0 - 8}" y="{y(v) + 4}" fill="{SOFT_TXT}" font-size="12" font-family="{MONO}" '
           f'text-anchor="end">{v}</text>')
    ap(f'<line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y1}" stroke="{AXIS}" stroke-width="1"/>')
    ap(f'<line x1="{X0}" y1="{Y1}" x2="{X1}" y2="{Y1}" stroke="{AXIS}" stroke-width="1"/>')
    ap(f'<text transform="rotate(-90 16 {(Y0 + Y1) // 2})" x="16" y="{(Y0 + Y1) // 2}" fill="{SOFT_TXT}" '
       f'font-size="12" font-family="{SANS}" text-anchor="middle">Correct answers per student (%)</text>')
    for i, (n, city, e, c) in enumerate(data):
        gx = X0 + GW * i + GW / 2
        if i:
            ap(f'<line x1="{X0 + GW * i}" y1="{Y0}" x2="{X0 + GW * i}" y2="{Y1}" stroke="{GRID}" stroke-width="0.8"/>')
        box(ap, gx - 28, stats(e), ACCENT, ACCENT_TINT, False)
        box(ap, gx + 28, stats(c), MUTED, MUTED_TINT, True)
        ap(f'<text x="{gx}" y="{Y1 + 20}" fill="{INK}" font-size="12" font-family="{SANS}" '
           f'text-anchor="middle">{city}</text>')
        ap(f'<text x="{gx}" y="{Y1 + 36}" fill="{SOFT_TXT}" font-size="12" font-family="{MONO}" '
           f'text-anchor="middle">n = {len(e)} / {len(c)}</text>')
    ly = 392
    ap(f'<line x1="{X0}" y1="{ly - 12}" x2="{X1}" y2="{ly - 12}" stroke="{GRID}" stroke-width="0.8"/>')
    ap(f'<rect x="{X0}" y="{ly}" width="24" height="16" rx="2" fill="{ACCENT_TINT}" stroke="{ACCENT}" stroke-width="1.4"/>')
    ap(f'<text x="{X0 + 32}" y="{ly + 12}" fill="{INK}" font-size="12" font-family="{SANS}">Experimental group</text>')
    lx = X0 + 200
    ap(f'<rect x="{lx}" y="{ly}" width="24" height="16" rx="2" fill="{MUTED_TINT}" stroke="{MUTED}" '
       f'stroke-width="1.4" stroke-dasharray="5,3"/>')
    ap(f'<text x="{lx + 32}" y="{ly + 12}" fill="{INK}" font-size="12" font-family="{SANS}">Control group</text>')
    ap(f'<circle cx="{lx + 196}" cy="{ly + 8}" r="3.2" fill="{PAPER}" stroke="{INK}" stroke-width="1.2"/>')
    ap(f'<text x="{lx + 208}" y="{ly + 12}" fill="{INK}" font-size="12" font-family="{SANS}">Outlier (&gt; 1.5 IQR)</text>')
    ap('</svg>')
    return "\n    ".join(a)


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Phase 1 formative scores</title>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: 'Geist', system-ui, sans-serif; background: #ffffff; color: #1A2133; min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 3rem 2rem; }}
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
    data = []
    for n, city, fe, fc in CASES:
        e, c = scores(BASE / f"case-study-{n}" / fe), scores(BASE / f"case-study-{n}" / fc)
        data.append((n, city, e, c))
        for g, x in (("E", e), ("C", c)):
            q1, med, q3, lo, hi, out = stats(x)
            print(f"Caso {n} {g} n={len(x)} Q1={q1:.1f} med={med:.1f} Q3={q3:.1f} IQR={q3 - q1:.1f}")
    (OUT / "phase1-formative-boxplot.html").write_text(PAGE.format(svg=svg(data)), encoding="utf-8")
