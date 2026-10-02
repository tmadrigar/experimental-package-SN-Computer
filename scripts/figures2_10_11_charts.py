"""
Gera as Figuras 2, 10 e 11 em HTML + SVG inline, no mesmo estilo dos graficos das Figuras 5 a 9
(sistema diagram-design, perfil manna-a4), e exporta os PNG usados no LaTeX.
  Fig. 2  Matriz de correlacao dos estilos de aprendizagem (estudo preliminar, n = 45)
          data/preliminary_study_LSI_45_participants.xlsx; colunas 1-12 Acomodador, 13-23 Convergente,
          24-34 Assimilador, 35+ Divergente (mesma regra do script original do CSEDU 2025)
  Fig. 10 Distribuicao dos educadores respondentes por unidade federativa (N = 87)
  Fig. 11 Notas no pre-teste e no pos-teste dos educadores (N = 87)
          data/Base_Unificada_Manna_87_Respostas_Avaliacao.csv
Execucao: python gerar_graficos_fig2_fig10_fig11.py
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_P1 = ROOT / "phase1-students" / "data" / "preliminary-study"
DATA_P2 = ROOT / "phase2-educators" / "data"
OUT = ROOT / "figures" / "html"

# perfil manna-a4 (mesmos valores de gerar_figuras_fase1.py)
PAPER, INK, MUTED, ACCENT = "#ffffff", "#1A2133", "#3380B0", "#D4510D"
SOFT_TXT = "#4a5468"
GRID, AXIS = "rgba(26,33,51,0.10)", "rgba(26,33,51,0.35)"
MONO, SANS = "'Geist Mono', monospace", "'Geist', sans-serif"
NAVY = "#0C3B6B"


def page(title, svg):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: 'Geist', system-ui, sans-serif; background: {PAPER}; color: {INK}; min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 3rem 2rem; }}
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


def head(slug, w, h, title, desc):
    return (f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" '
            f'aria-labelledby="{slug}-title {slug}-desc"><title id="{slug}-title">{title}</title>'
            f'<desc id="{slug}-desc">{desc}</desc><rect width="100%" height="100%" fill="{PAPER}"/>')


def mix(c1, c2, t):
    a = [int(c1[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(c2[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x + (y - x) * t):02x}" for x, y in zip(a, b))


# ---------------------------------------------------------------- Fig. 2
def fig2():
    d = pd.read_excel(DATA_P1 / "preliminary_study_LSI_45_participants.xlsx")
    c = d.columns
    styles = {"Accommodator": c[1:13], "Converger": c[13:24], "Assimilator": c[24:35], "Diverger": c[35:]}
    for k, cols in styles.items():
        d[k] = d[cols].sum(axis=1)
    m = d[list(styles)].corr()
    names = list(styles)
    W, H = 640, 448
    X0, Y0, S = 136, 24, 96
    lo, hi = 0.4, 1.0
    g = [head("corr", W, H, "Correlation matrix of learning styles",
              f"Pearson correlations between the four Kolb learning style scores of {len(d)} participants of the "
              "preliminary study; Accommodator and Diverger correlate at 0.79 and Converger and Assimilator at 0.68.")]
    for i, r in enumerate(names):
        for j, cname in enumerate(names):
            v = m.loc[r, cname]
            t = (v - lo) / (hi - lo)
            fill = mix("#E8F0F7", NAVY, max(0, min(1, t)))
            x, y = X0 + j * S, Y0 + i * S
            g.append(f'<rect x="{x}" y="{y}" width="{S - 4}" height="{S - 4}" rx="4" fill="{fill}"/>')
            col = "#ffffff" if t > 0.55 else INK
            g.append(f'<text x="{x + (S - 4) / 2}" y="{y + (S - 4) / 2 + 6}" fill="{col}" font-size="16" '
                     f'font-family="{MONO}" text-anchor="middle">{v:.2f}</text>')
        g.append(f'<text x="{X0 - 12}" y="{Y0 + i * S + (S - 4) / 2 + 4}" fill="{INK}" font-size="12" '
                 f'font-family="{SANS}" text-anchor="end">{r}</text>')
        g.append(f'<text x="{X0 + i * S + (S - 4) / 2}" y="{Y0 + 4 * S + 16}" fill="{INK}" font-size="12" '
                 f'font-family="{SANS}" text-anchor="middle">{r}</text>')
    # escala de cor
    bx, by, bh = X0 + 4 * S + 24, Y0, 4 * S - 4
    steps = 40
    for k in range(steps):
        t = 1 - k / steps
        g.append(f'<rect x="{bx}" y="{by + k * bh / steps:.1f}" width="16" height="{bh / steps + 0.6:.1f}" fill="{mix("#E8F0F7", NAVY, t)}"/>')
    for v in (0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0):
        y = by + (1 - (v - lo) / (hi - lo)) * bh
        g.append(f'<line x1="{bx + 16}" y1="{y:.1f}" x2="{bx + 20}" y2="{y:.1f}" stroke="{AXIS}" stroke-width="1"/>')
        g.append(f'<text x="{bx + 24}" y="{y + 4:.1f}" fill="{SOFT_TXT}" font-size="12" font-family="{MONO}">{v:.1f}</text>')
    g.append(f'<text transform="rotate(-90 {bx + 64} {by + bh / 2})" x="{bx + 64}" y="{by + bh / 2}" fill="{SOFT_TXT}" '
             f'font-size="12" font-family="{SANS}" text-anchor="middle">Pearson correlation</text>')
    g.append("</svg>")
    return "".join(g)


# ---------------------------------------------------------------- base da Fase 2
def base2():
    return pd.read_csv(DATA_P2 / "pre_post_test_87_educators.csv", sep=";")


UF = {"PE": "Pernambuco", "PR": "Paraná", "AM": "Amazonas", "SE": "Sergipe", "GO": "Goiás", "AL": "Alagoas",
      "SP": "São Paulo", "MG": "Minas Gerais", "RJ": "Rio de Janeiro", "PA": "Pará", "PB": "Paraíba",
      "BA": "Bahia", "DF": "Federal District", "MA": "Maranhão", "AP": "Amapá", "PI": "Piauí",
      "RR": "Roraima", "RS": "Rio Grande do Sul"}


# ---------------------------------------------------------------- Fig. 10
def fig10():
    d = base2()
    vc = d["Estado"].value_counts()
    order = sorted(vc.items(), key=lambda kv: (-kv[1], kv[0]))
    n = len(order)
    W, RH = 640, 22
    X0, X1, Y0 = 176, 600, 16
    H = Y0 + n * RH + 56
    mx = 16
    sx = (X1 - X0) / mx
    g = [head("geo", W, H, "Educators by federal unit (Phase 2)",
              f"Horizontal bar chart of the {int(vc.sum())} responding educators by Brazilian federal unit; "
              f"{n} units are represented, led by Pernambuco ({order[0][1]}) and Paraná ({order[1][1]}).")]
    for v in range(0, mx + 1, 4):
        x = X0 + v * sx
        g.append(f'<line x1="{x:.1f}" y1="{Y0 - 4}" x2="{x:.1f}" y2="{Y0 + n * RH}" stroke="{GRID}" stroke-width="0.8"/>')
        g.append(f'<text x="{x:.1f}" y="{Y0 + n * RH + 18}" fill="{SOFT_TXT}" font-size="12" font-family="{MONO}" '
                 f'text-anchor="middle">{v}</text>')
    for i, (uf, c) in enumerate(order):
        y = Y0 + i * RH
        g.append(f'<rect x="{X0}" y="{y + 4}" width="{c * sx:.1f}" height="{RH - 8}" rx="2" fill="{MUTED}"/>')
        g.append(f'<text x="{X0 + c * sx + 6:.1f}" y="{y + RH / 2 + 4}" fill="{INK}" font-size="12" '
                 f'font-family="{MONO}">{c}</text>')
        g.append(f'<text x="{X0 - 10}" y="{y + RH / 2 + 4}" fill="{INK}" font-size="12" font-family="{SANS}" '
                 f'text-anchor="end">{UF.get(uf, uf)} ({uf})</text>')
    g.append(f'<line x1="{X0}" y1="{Y0 - 4}" x2="{X0}" y2="{Y0 + n * RH}" stroke="{AXIS}" stroke-width="1"/>')
    g.append(f'<text x="{(X0 + X1) / 2}" y="{Y0 + n * RH + 42}" fill="{SOFT_TXT}" font-size="12" font-family="{SANS}" '
             f'text-anchor="middle">Number of educators</text>')
    g.append("</svg>")
    return "".join(g)


# ---------------------------------------------------------------- Fig. 11
def fig11():
    d = base2()
    pre = pd.to_numeric(d["Total Pré"], errors="coerce")
    post = pd.to_numeric(d["Total Pós"], errors="coerce")
    pairs = pd.crosstab(pre, post)
    W, H = 640, 424
    X0, X1, Y0, Y1 = 64, 616, 24, 324
    xa, xb = 200, 480
    lo, hi = 6, 10

    def y(v): return Y1 - (v - lo) / (hi - lo) * (Y1 - Y0)

    g = [head("prepost", W, H, "Pre-test and post-test scores of Phase 2 educators",
              f"Paired slope chart for {len(pre)} educators: lines connect each pre-test score to the post-test score, "
              f"with thickness proportional to the number of educators; mean scores rose from {pre.mean():.2f} "
              f"to {post.mean():.2f} out of 10.")]
    for v in range(lo, hi + 1):
        g.append(f'<line x1="{X0}" y1="{y(v)}" x2="{X1}" y2="{y(v)}" stroke="{GRID}" stroke-width="0.8"/>')
        g.append(f'<text x="{X0 - 8}" y="{y(v) + 4}" fill="{SOFT_TXT}" font-size="12" font-family="{MONO}" '
                 f'text-anchor="end">{v}</text>')
    g.append(f'<line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y1}" stroke="{AXIS}" stroke-width="1"/>')
    g.append(f'<line x1="{X0}" y1="{Y1}" x2="{X1}" y2="{Y1}" stroke="{AXIS}" stroke-width="1"/>')
    g.append(f'<text transform="rotate(-90 16 {(Y0 + Y1) // 2})" x="16" y="{(Y0 + Y1) // 2}" fill="{SOFT_TXT}" '
             f'font-size="12" font-family="{SANS}" text-anchor="middle">Score (out of 10)</text>')
    for x, lab in ((xa, "Pre-test"), (xb, "Post-test")):
        g.append(f'<text x="{x}" y="{Y1 + 22}" fill="{INK}" font-size="12" font-family="{SANS}" '
                 f'text-anchor="middle">{lab}</text>')
    # linhas pareadas (desenhadas primeiro), linha das medias, depois rotulos e nos
    LABEL_T = {(7, 9): 0.62, (7, 10): 0.40, (8, 9): 0.80, (8, 10): 0.50}
    labels = []
    for a in pairs.index:
        for b in pairs.columns:
            n = int(pairs.loc[a, b])
            if not n:
                continue
            w = 1.2 + n * 0.26
            g.append(f'<line x1="{xa}" y1="{y(a)}" x2="{xb}" y2="{y(b)}" stroke="{MUTED}" stroke-opacity="0.55" '
                     f'stroke-width="{w:.1f}" stroke-linecap="round"/>')
            t = LABEL_T.get((int(a), int(b)), 0.5)
            labels.append((xa + (xb - xa) * t, y(a) + (y(b) - y(a)) * t, n))
    g.append(f'<line x1="{xa}" y1="{y(pre.mean()):.1f}" x2="{xb}" y2="{y(post.mean()):.1f}" stroke="{ACCENT}" '
             f'stroke-width="2" stroke-dasharray="6,4"/>')
    for mxp, myp, n in labels:
        g.append(f'<rect x="{mxp - 16:.1f}" y="{myp - 9:.1f}" width="32" height="16" rx="3" fill="{PAPER}" '
                 f'stroke="{MUTED}" stroke-width="0.8"/>')
        g.append(f'<text x="{mxp:.1f}" y="{myp + 3:.1f}" fill="{INK}" font-size="11" font-family="{MONO}" '
                 f'text-anchor="middle">{n}</text>')
    for x, s_, side in ((xa, pre, "end"), (xb, post, "start")):
        for v, n in s_.value_counts().sort_index().items():
            g.append(f'<circle cx="{x}" cy="{y(v)}" r="5" fill="{MUTED}"/>')
            dx = -12 if side == "end" else 12
            g.append(f'<text x="{x + dx}" y="{y(v) + 4}" fill="{SOFT_TXT}" font-size="11" font-family="{MONO}" '
                     f'text-anchor="{side}">n = {n}</text>')
    for x, v in ((xa, pre.mean()), (xb, post.mean())):
        g.append(f'<circle cx="{x}" cy="{y(v):.1f}" r="5" fill="{ACCENT}"/>')
    # legenda
    ly = 380
    g.append(f'<line x1="{X0}" y1="{ly - 12}" x2="{X1}" y2="{ly - 12}" stroke="{GRID}" stroke-width="0.8"/>')
    g.append(f'<line x1="{X0}" y1="{ly + 8}" x2="{X0 + 28}" y2="{ly + 8}" stroke="{MUTED}" stroke-opacity="0.55" stroke-width="6" stroke-linecap="round"/>')
    g.append(f'<text x="{X0 + 36}" y="{ly + 12}" fill="{INK}" font-size="12" font-family="{SANS}">Educators per score change (line width)</text>')
    lx = X0 + 320
    g.append(f'<line x1="{lx}" y1="{ly + 8}" x2="{lx + 28}" y2="{ly + 8}" stroke="{ACCENT}" stroke-width="2" stroke-dasharray="6,4"/>')
    g.append(f'<circle cx="{lx + 14}" cy="{ly + 8}" r="4" fill="{ACCENT}"/>')
    g.append(f'<text x="{lx + 36}" y="{ly + 12}" fill="{INK}" font-size="12" font-family="{SANS}">'
             f'Mean ({pre.mean():.2f} to {post.mean():.2f})</text>')
    g.append("</svg>")
    return "".join(g)


def export(html, png):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(device_scale_factor=3)
        pg.goto(html.resolve().as_uri())
        pg.wait_for_load_state("networkidle")
        pg.locator("svg").first.screenshot(path=str(png))
        b.close()


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for fn, svgf, title, png in (
        ("learning-styles-correlation-matrix.html", fig2, "Correlation matrix of learning styles", "learning-styles-correlation-matrix.png"),
        ("phase2-geographic-distribution.html", fig10, "Educators by federal unit", "phase2-geographic-distribution.png"),
        ("phase2-pre-post-scores.html", fig11, "Pre-test and post-test scores", "phase2-hake-gain-distribution.png"),
    ):
        html = OUT / fn
        html.write_text(page(title, svgf()), encoding="utf-8")
        export(html, ROOT / "figures" / png)
        print("ok", fn, "->", png)
