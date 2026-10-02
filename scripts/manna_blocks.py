"""
Estilo comum dos diagramas do artigo (Figuras 1, 3 e 4): blocos arredondados preenchidos,
faixa lateral clara com o nome da secao, icones de linha branca, texto em maiusculas,
setas e conectores escuros. Sistema diagram-design, cores derivadas da Figura 3 original.
"""
from pathlib import Path

PAPER = "#fdfdfd"
INK = "#2a3f51"          # setas, conectores, texto escuro
WHITE = "#ffffff"
SANS = "'Geist', 'Inter', 'Helvetica Neue', Arial, sans-serif"

# pares (faixa clara, bloco) amostrados da Figura 3 + dois tons complementares
SLATE = ("#d6dce0", "#758d9a")
BLUE = ("#cfe0f2", "#6f9cc4")
SAND = ("#f6e7c9", "#e9c786")
SALMON = ("#f0d3d1", "#d48578")
NAVY = ("#d6dce0", "#4f6b85")
TEAL = ("#d3e8e5", "#5c9c94")
CARD = ("#e8ecf0", "#eef2f5")   # cartoes claros (fundamentos)


def icon(kind, x, y, color=WHITE):
    """Icone de linha, area 48x48 com origem em (x, y)."""
    s = (f'fill="none" stroke="{color}" stroke-width="2.4" stroke-linecap="round" '
         f'stroke-linejoin="round"')
    dot = f'fill="{color}" stroke="{color}"'
    k = {
        "design": f'<circle cx="{x+24}" cy="{y+24}" r="22" {s}/><circle cx="{x+24}" cy="{y+12}" r="3" {s}/>'
                  f'<path d="M{x+22} {y+15} L{x+14} {y+38} M{x+26} {y+15} L{x+34} {y+38} M{x+17} {y+30} L{x+31} {y+30}" {s}/>',
        "call": f'<path d="M{x+8} {y+2} H{x+30} L{x+40} {y+12} V{y+46} H{x+8} Z" {s}/><path d="M{x+30} {y+2} V{y+12} H{x+40}" {s}/>'
                f'<path d="M{x+14} {y+20} H{x+34} M{x+14} {y+28} H{x+34} M{x+14} {y+36} H{x+26}" {s}/>',
        "plan": f'<rect x="{x+8}" y="{y+6}" width="32" height="40" rx="3" {s}/><rect x="{x+17}" y="{y+2}" width="14" height="8" rx="2" {s}/>'
                f'<path d="M{x+14} {y+20} l3 3 l5 -6 M{x+26} {y+20} H{x+34} M{x+14} {y+33} l3 3 l5 -6 M{x+26} {y+33} H{x+34}" {s}/>',
        "form": f'<rect x="{x+6}" y="{y+2}" width="32" height="42" rx="3" {s}/>'
                f'<rect x="{x+12}" y="{y+10}" width="6" height="6" {s}/><path d="M{x+22} {y+13} H{x+32}" {s}/>'
                f'<rect x="{x+12}" y="{y+21}" width="6" height="6" {s}/><path d="M{x+22} {y+24} H{x+32}" {s}/>'
                f'<rect x="{x+12}" y="{y+32}" width="6" height="6" {s}/><path d="M{x+22} {y+35} H{x+28}" {s}/>'
                f'<path d="M{x+36} {y+40} L{x+46} {y+28}" {s}/>',
        "quiz": f'<path d="M{x+4} {y+8} H{x+44} V{y+34} H{x+18} L{x+8} {y+44} V{y+34} H{x+4} Z" {s}/>'
                f'<path d="M{x+19} {y+16} q5 -6 10 0 q2 4 -5 7 v3" {s}/><circle cx="{x+24}" cy="{y+30}" r="1" {dot}/>',
        "stars": f'<path d="M{x+4} {y+8} H{x+44} V{y+34} H{x+18} L{x+8} {y+44} V{y+34} H{x+4} Z" {s}/>'
                 f'<path d="M{x+14} {y+16} l1.6 3.4 3.6 .4 -2.7 2.4 .8 3.6 -3.3 -1.9 -3.3 1.9 .8 -3.6 -2.7 -2.4 3.6 -.4 Z '
                 f'M{x+24} {y+16} l1.6 3.4 3.6 .4 -2.7 2.4 .8 3.6 -3.3 -1.9 -3.3 1.9 .8 -3.6 -2.7 -2.4 3.6 -.4 Z '
                 f'M{x+34} {y+16} l1.6 3.4 3.6 .4 -2.7 2.4 .8 3.6 -3.3 -1.9 -3.3 1.9 .8 -3.6 -2.7 -2.4 3.6 -.4 Z" {s} stroke-width="1.6"/>',
        "gears": f'<circle cx="{x+18}" cy="{y+18}" r="8" {s}/><circle cx="{x+18}" cy="{y+18}" r="3" {s}/>'
                 f'<path d="M{x+18} {y+4} V{y+8} M{x+18} {y+28} V{y+32} M{x+4} {y+18} H{x+8} M{x+28} {y+18} H{x+32} '
                 f'M{x+8} {y+8} l3 3 M{x+25} {y+25} l3 3 M{x+28} {y+8} l-3 3 M{x+8} {y+28} l3 -3" {s}/>'
                 f'<circle cx="{x+35}" cy="{y+35}" r="6" {s}/><circle cx="{x+35}" cy="{y+35}" r="2" {s}/>'
                 f'<path d="M{x+35} {y+25} V{y+28} M{x+35} {y+42} V{y+45} M{x+25} {y+35} H{x+28} M{x+42} {y+35} H{x+45}" {s}/>',
        "baseline": f'<path d="M{x+4} {y+44} H{x+44}" {s}/><rect x="{x+8}" y="{y+26}" width="8" height="18" {s}/>'
                    f'<rect x="{x+20}" y="{y+18}" width="8" height="26" {s}/><rect x="{x+32}" y="{y+30}" width="8" height="14" {s}/>'
                    f'<path d="M{x+2} {y+12} H{x+46}" {s} stroke-dasharray="4,3"/>',
        "teach": f'<rect x="{x+18}" y="{y+4}" width="28" height="20" rx="2" {s}/><circle cx="{x+9}" cy="{y+12}" r="5" {s}/>'
                 f'<path d="M{x+3} {y+44} V{y+26} q6 -6 12 0 V{y+44} M{x+15} {y+28} L{x+24} {y+20}" {s}/>'
                 f'<circle cx="{x+26}" cy="{y+34}" r="3" {s}/><circle cx="{x+38}" cy="{y+34}" r="3" {s}/>'
                 f'<path d="M{x+21} {y+44} q5 -6 10 0 M{x+33} {y+44} q5 -6 10 0" {s}/>',
        "team": f'<circle cx="{x+24}" cy="{y+12}" r="7" {s}/><path d="M{x+12} {y+42} q12 -20 24 0" {s}/>'
                f'<circle cx="{x+8}" cy="{y+20}" r="5" {s}/><path d="M{x+0} {y+42} q6 -12 14 -8" {s}/>'
                f'<circle cx="{x+40}" cy="{y+20}" r="5" {s}/><path d="M{x+48} {y+42} q-6 -12 -14 -8" {s}/>',
        "chat": f'<path d="M{x+20} {y+2} H{x+46} V{y+22} H{x+32} L{x+26} {y+28} V{y+22} H{x+20} Z" {s}/>'
                f'<path d="M{x+26} {y+10} H{x+40} M{x+26} {y+16} H{x+36}" {s}/>'
                f'<circle cx="{x+12}" cy="{y+28}" r="6" {s}/><path d="M{x+2} {y+46} q10 -14 20 0" {s}/>',
        "pitch": f'<rect x="{x+4}" y="{y+4}" width="40" height="28" rx="2" {s}/>'
                 f'<path d="M{x+20} {y+12} L{x+30} {y+18} L{x+20} {y+24} Z" {s}/>'
                 f'<path d="M{x+24} {y+32} V{y+38} M{x+14} {y+46} L{x+24} {y+38} L{x+34} {y+46}" {s}/>',
        "gain": f'<path d="M{x+4} {y+44} H{x+44}" {s}/><rect x="{x+8}" y="{y+32}" width="7" height="12" {s}/>'
                f'<rect x="{x+20}" y="{y+24}" width="7" height="20" {s}/><rect x="{x+32}" y="{y+16}" width="7" height="28" {s}/>'
                f'<path d="M{x+6} {y+20} L{x+22} {y+10} L{x+30} {y+14} L{x+44} {y+4} M{x+36} {y+4} H{x+44} V{y+12}" {s}/>',
        "linechart": f'<path d="M{x+4} {y+44} H{x+44}" {s}/><rect x="{x+8}" y="{y+30}" width="6" height="14" {s}/>'
                     f'<rect x="{x+20}" y="{y+24}" width="6" height="20" {s}/><rect x="{x+32}" y="{y+28}" width="6" height="16" {s}/>'
                     f'<path d="M{x+6} {y+16} L{x+18} {y+8} L{x+30} {y+14} L{x+44} {y+4}" {s}/>'
                     f'<circle cx="{x+6}" cy="{y+16}" r="2" {s}/><circle cx="{x+18}" cy="{y+8}" r="2" {s}/>'
                     f'<circle cx="{x+30}" cy="{y+14}" r="2" {s}/><circle cx="{x+44}" cy="{y+4}" r="2" {s}/>',
        "criteria": f'<rect x="{x+4}" y="{y+6}" width="30" height="38" rx="3" {s}/><rect x="{x+12}" y="{y+2}" width="14" height="8" rx="2" {s}/>'
                    f'<path d="M{x+10} {y+20} l3 3 l5 -6 M{x+10} {y+32} l3 3 l5 -6" {s}/>'
                    f'<circle cx="{x+38}" cy="{y+36}" r="9" {s}/>'
                    f'<path d="M{x+38} {y+30} l1.8 3.6 4 .5 -3 2.7 .9 4 -3.7 -2.1 -3.7 2.1 .9 -4 -3 -2.7 4 -.5 Z" {s} stroke-width="1.4"/>',
        "commit": f'<rect x="{x+4}" y="{y+6}" width="30" height="38" rx="3" {s}/>'
                  f'<path d="M{x+10} {y+16} H{x+28} M{x+10} {y+24} H{x+24} M{x+10} {y+34} q4 -6 8 0 q4 6 8 0" {s}/>'
                  f'<path d="M{x+30} {y+34} L{x+44} {y+14} L{x+48} {y+18} L{x+34} {y+38} L{x+29} {y+40} Z" {s}/>',
        "bulb": f'<path d="M{x+16} {y+36} q-10 -8 -10 -18 a18 18 0 0 1 36 0 q0 10 -10 18 Z" {s}/>'
                f'<path d="M{x+18} {y+40} H{x+30} M{x+19} {y+45} H{x+29} M{x+24} {y+36} V{y+22} M{x+19} {y+20} q5 6 10 0" {s}/>'
                f'<path d="M{x+24} {y-4} V{y-9} M{x+4} {y+4} l-4 -4 M{x+44} {y+4} l4 -4" {s}/>',
        "cube": f'<path d="M{x+24} {y+2} L{x+44} {y+13} V{y+35} L{x+24} {y+46} L{x+4} {y+35} V{y+13} Z M{x+4} {y+13} L{x+24} {y+24} L{x+44} {y+13} M{x+24} {y+24} V{y+46}" {s}/>'
                f'<circle cx="{x+24}" cy="{y+2}" r="2.6" {dot}/><circle cx="{x+44}" cy="{y+13}" r="2.6" {dot}/>'
                f'<circle cx="{x+4}" cy="{y+13}" r="2.6" {dot}/><circle cx="{x+24}" cy="{y+24}" r="2.6" {dot}/>'
                f'<circle cx="{x+4}" cy="{y+35}" r="2.6" {dot}/><circle cx="{x+44}" cy="{y+35}" r="2.6" {dot}/>'
                f'<circle cx="{x+24}" cy="{y+46}" r="2.6" {dot}/>',
        "student": f'<path d="M{x+4} {y+12} L{x+24} {y+4} L{x+44} {y+12} L{x+24} {y+20} Z M{x+12} {y+15} V{y+22} q12 6 24 0 V{y+15} M{x+44} {y+12} V{y+22}" {s}/>'
                   f'<circle cx="{x+24}" cy="{y+28}" r="6" {s}/><path d="M{x+10} {y+48} q14 -18 28 0" {s}/>',
        "teacher": f'<circle cx="{x+14}" cy="{y+8}" r="6" {s}/><path d="M{x+4} {y+30} q10 -16 20 0 M{x+24} {y+20} L{x+40} {y+6}" {s}/>'
                   f'<circle cx="{x+10}" cy="{y+38}" r="4" {s}/><circle cx="{x+24}" cy="{y+38}" r="4" {s}/><circle cx="{x+38}" cy="{y+38}" r="4" {s}/>'
                   f'<path d="M{x+3} {y+50} q7 -8 14 0 M{x+17} {y+50} q7 -8 14 0 M{x+31} {y+50} q7 -8 14 0" {s}/>',
        "target": f'<circle cx="{x+22}" cy="{y+26}" r="20" {s}/><circle cx="{x+22}" cy="{y+26}" r="12" {s}/>'
                  f'<circle cx="{x+22}" cy="{y+26}" r="4" {s}/><path d="M{x+22} {y+26} L{x+44} {y+4} M{x+36} {y+4} H{x+44} V{y+12}" {s}/>',
        "chip": f'<rect x="{x+10}" y="{y+10}" width="28" height="28" rx="3" {s}/><rect x="{x+18}" y="{y+18}" width="12" height="12" {s}/>'
                f'<path d="M{x+16} {y+4} V{y+10} M{x+24} {y+4} V{y+10} M{x+32} {y+4} V{y+10} M{x+16} {y+38} V{y+44} M{x+24} {y+38} V{y+44} M{x+32} {y+38} V{y+44} '
                f'M{x+4} {y+16} H{x+10} M{x+4} {y+24} H{x+10} M{x+4} {y+32} H{x+10} M{x+38} {y+16} H{x+44} M{x+38} {y+24} H{x+44} M{x+38} {y+32} H{x+44}" {s}/>',
    }
    return k[kind]


def defs(mid):
    return (f'<defs><marker id="{mid}" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">'
            f'<path d="M1 1 L9 4 L1 7" fill="none" stroke="{INK}" stroke-width="1.6" stroke-linecap="round" '
            f'stroke-linejoin="round"/></marker></defs>')


def strip(x, y, w, h, color, lines, size=11):
    """Faixa lateral com o nome da secao em texto vertical."""
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{color}"/>']
    cx, cy, n = x + w // 2, y + h // 2, len(lines)
    for k, ln in enumerate(lines):
        off = (k - (n - 1) / 2) * 15
        out.append(f'<text transform="rotate(-90 {cx + off} {cy})" x="{cx + off}" y="{cy + 4}" fill="{INK}" '
                   f'font-size="{size}" font-weight="600" letter-spacing="0.06em" font-family="{SANS}" '
                   f'text-anchor="middle">{ln}</text>')
    return "".join(out)


def text_lines(x, cy, lines, size=14, weight=700, color=WHITE, anchor="start", spacing=18, italic=False, ls="0.04em"):
    top = cy - (len(lines) - 1) * spacing / 2 + size * 0.36
    st = ' font-style="italic"' if italic else ""
    return "".join(f'<text x="{x}" y="{top + spacing * k:.1f}" fill="{color}" font-size="{size}" font-weight="{weight}" '
                   f'letter-spacing="{ls}" font-family="{SANS}" text-anchor="{anchor}"{st}>{ln}</text>'
                   for k, ln in enumerate(lines))


def arrow(x1, y1, x2, y2, mid):
    return (f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{INK}" stroke-width="2.4" fill="none" '
            f'marker-end="url(#{mid})"/>')


def page(title, svg_markup):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: 'Geist', system-ui, sans-serif; background: {PAPER}; color: {INK}; min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 3rem 2rem; }}
    .frame {{ max-width: 1200px; width: 100%; }}
    svg {{ width: 100%; display: block; }}
  </style>
</head>
<body>
  <div class="frame">
    {svg_markup}
  </div>
</body>
</html>
"""


def flow_rows(rows, W, mid, row_y, bh=112, x0=96, x1=928, sx=16, sw=56, gap=80, r=8):
    """Linhas de etapas ligadas por setas e conector em zigue-zague (padrao das Figuras 3 e 4).
    rows: lista de (linhas_do_rotulo, (cor_faixa, cor_bloco), [(icone, linhas_texto), ...])."""
    g = []
    geo = []
    for (label, (stripc, fill), cells), y in zip(rows, row_y):
        n = len(cells)
        bw = (x1 - x0 - (n - 1) * gap) / n
        xs = [x0 + k * (bw + gap) for k in range(n)]
        geo.append((xs, bw, y))
    xr = x1 + 20
    for i in range(len(rows) - 1):
        xs, bw, y = geo[i]
        y_out, y_mid = y + bh // 2, y + bh + (row_y[i + 1] - y - bh) // 2
        x_in = geo[i + 1][0][0] + 24
        d = (f"M{xs[-1] + bw:.0f} {y_out} H{xr - r} Q{xr} {y_out} {xr} {y_out + r} V{y_mid - r} "
             f"Q{xr} {y_mid} {xr - r} {y_mid} H{x_in + r} Q{x_in} {y_mid} {x_in} {y_mid + r} V{row_y[i + 1] - 2}")
        g.append(f'<path d="{d}" stroke="{INK}" stroke-width="2.4" fill="none" marker-end="url(#{mid})"/>')
    for (label, (stripc, fill), cells), (xs, bw, y) in zip(rows, geo):
        g.append(strip(sx, y, sw, bh, stripc, label))
        n = len(cells)
        for j, ((ic, lines), bx) in enumerate(zip(cells, xs)):
            g.append(f'<rect x="{bx:.0f}" y="{y}" width="{bw:.0f}" height="{bh}" rx="8" fill="{fill}"/>')
            g.append(icon(ic, bx + 16, y + bh // 2 - 24))
            g.append(text_lines(bx + 80, y + bh // 2, lines))
            if j < n - 1:
                g.append(arrow(bx + bw + 16, y + bh // 2, xs[j + 1] - 18, y + bh // 2, mid))
    return "".join(g)


def export_png(html_path, png_path, scale=3):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(device_scale_factor=scale)
        pg.goto(Path(html_path).resolve().as_uri())
        pg.wait_for_load_state("networkidle")
        pg.locator("svg").first.screenshot(path=str(png_path))
        b.close()
