"""
Gera a Figura 1 (arquitetura conceitual da Metodologia Manna) em HTML + SVG inline,
no estilo comum dos diagramas (manna_blocks.py). Mesmo conteudo da figura original:
filosofia -> framework -> dois modelos de aplicacao -> quatro fundamentos.
Execucao: python gerar_figura1_arquitetura.py  (gera HTML e exporta o PNG usado no LaTeX)
"""
from pathlib import Path
import manna_blocks as mb

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures" / "html"
W, H = 960, 680
X0, X1 = 96, 928
SX, SW = 16, 56
MID = "f1-arrow"
INK, WHITE, SANS = mb.INK, mb.WHITE, mb.SANS


def box(x, y, w, h, fill):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}"/>'


def t(x, y, s, size, weight=700, color=WHITE, anchor="middle", italic=False, ls="0.04em"):
    it = ' font-style="italic"' if italic else ""
    return (f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" letter-spacing="{ls}" '
            f'font-family="{SANS}" text-anchor="{anchor}"{it}>{s}</text>')


def svg():
    g = []
    a = g.append
    a(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" '
      f'aria-labelledby="arch-title arch-desc">')
    a('<title id="arch-title">Conceptual architecture of the Manna Methodology</title>')
    a('<desc id="arch-desc">Hierarchy of the Manna Methodology: the educational philosophy, the operational framework '
      'with its three dimensions, the two application models (Manna-Student Model and Manna-Teacher Model), and the '
      'four foundations that support them.</desc>')
    a(mb.defs(MID))
    a(f'<rect width="100%" height="100%" fill="{mb.PAPER}"/>')

    cx = (X0 + X1) // 2
    # --- linha 1: filosofia
    y1, h1 = 24, 112
    a(mb.strip(SX, y1, SW, h1, mb.NAVY[0], ["PHILOSOPHY"]))
    a(box(X0, y1, X1 - X0, h1, mb.NAVY[1]))
    a(mb.icon("bulb", X0 + 32, y1 + 36))
    a(t(cx + 32, y1 + 46, "MANNA METHODOLOGY", 24))
    a(t(cx + 32, y1 + 70, "Educational philosophy", 14, 600))
    a(t(cx + 32, y1 + 92, "Convergence of Exponential Technologies and Exponential People", 13, 400, italic=True, ls="0.02em"))
    # seta
    y2, h2 = 168, 136
    a(mb.arrow(cx, y1 + h1, cx, y2 - 2, MID))
    # --- linha 2: framework
    a(mb.strip(SX, y2, SW, h2, mb.BLUE[0], ["FRAMEWORK"]))
    a(box(X0, y2, X1 - X0, h2, mb.BLUE[1]))
    a(mb.icon("cube", X0 + 32, y2 + 44))
    a(t(cx + 32, y2 + 38, "MANNA METHODOLOGY FRAMEWORK", 22))
    a(t(cx + 32, y2 + 62, "Operational structure: Conception, Diagnostic, Formative, and Summative Assessment", 13, 500, ls="0.02em"))
    pills = ["Learning Styles", "Socio-Emotional Competencies", "Exponential Technologies"]
    pw = [152, 232, 208]
    gap = 16
    px = cx + 32 - (sum(pw) + gap * 2) // 2
    for label, w in zip(pills, pw):
        a(f'<rect x="{px}" y="{y2 + 84}" width="{w}" height="32" rx="8" fill="none" stroke="{WHITE}" stroke-width="1.6"/>')
        a(t(px + w // 2, y2 + 105, label, 13, 600, ls="0.02em"))
        px += w + gap
    # --- linha 3: modelos de aplicacao
    y3, h3 = 352, 128
    mw = (X1 - X0 - 32) // 2
    xs = [X0, X0 + mw + 32]
    yb = y2 + h2
    ymid = yb + 20
    for x in xs:
        tx = x + mw // 2
        a(f'<path d="M{cx} {yb} V{ymid - 8} Q{cx} {ymid} {cx + (8 if tx > cx else -8)} {ymid} H{tx + (-8 if tx > cx else 8)} '
          f'Q{tx} {ymid} {tx} {ymid + 8} V{y3 - 2}" stroke="{INK}" stroke-width="2.4" fill="none" marker-end="url(#{MID})"/>')
    a(mb.strip(SX, y3, SW, h3, "#e7e2dc", ["APPLICATION", "MODELS"]))
    models = [
        (mb.SALMON[1], "student", "PHASE 1", "MANNA-STUDENT MODEL", "Immersive IoD bootcamps", "Public school students"),
        (mb.TEAL[1], "teacher", "PHASE 2", "MANNA-TEACHER MODEL", "Immersive training event", "Teachers and school managers"),
    ]
    for x, (fill, ic, eyebrow, name, sub, who) in zip(xs, models):
        a(box(x, y3, mw, h3, fill))
        a(mb.icon(ic, x + 24, y3 + 38))
        mx = x + mw // 2 + 32
        a(t(mx, y3 + 30, eyebrow, 12, 600, ls="0.12em"))
        a(t(mx, y3 + 58, name, 18))
        a(t(mx, y3 + 82, sub, 13, 500, ls="0.02em"))
        a(t(mx, y3 + 104, who, 13, 400, italic=True, ls="0.02em"))
    # --- linha 4: fundamentos
    y4, h4 = 536, 120
    ymerge = y3 + h3 + 28
    for x in xs:
        tx = x + mw // 2
        a(f'<path d="M{tx} {y3 + h3} V{ymerge}" stroke="{INK}" stroke-width="2.4" fill="none"/>')
    a(f'<path d="M{xs[0] + mw // 2} {ymerge} H{xs[1] + mw // 2}" stroke="{INK}" stroke-width="2.4" fill="none"/>')
    a(mb.arrow(cx, ymerge, cx, y4 - 2, MID))
    a(mb.strip(SX, y4, SW, h4, mb.CARD[0], ["FOUNDATIONS"]))
    found = [
        ("target", ["Purpose-Driven", "Education"], ["Real-world problems", "and impact"]),
        ("team", ["Learner-Centered", "Approach"], ["Personalization and", "learner autonomy"]),
        ("linechart", ["Data-Informed", "Decisions"], ["Evidence to guide", "teaching and learning"]),
        ("chip", ["Exponential", "Mindset"], ["Technology, creativity", "and human potential"]),
    ]
    fg = 32
    fw = (X1 - X0 - 3 * fg) // 4
    for k, (ic, title, desc) in enumerate(found):
        x = X0 + k * (fw + fg)
        a(f'<rect x="{x}" y="{y4}" width="{fw}" height="{h4}" rx="8" fill="{mb.CARD[1]}" stroke="#c9d3dc" stroke-width="1"/>')
        a(mb.icon(ic, x + 12, y4 + 14, color=mb.NAVY[1]))
        a(mb.text_lines(x + 68, y4 + 38, title, size=12, weight=700, color=INK, spacing=16, ls="0"))
        for j, ln in enumerate(desc):
            a(t(x + 16, y4 + 86 + 16 * j, ln, 11, 400, color="#4a5468", anchor="start", ls="0.01em"))
        if k < 3:
            a(mb.arrow(x + fw + 6, y4 + h4 // 2, x + fw + fg - 6, y4 + h4 // 2, MID))
    a('</svg>')
    return "".join(g)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    html = OUT / "manna-conceptual-architecture.html"
    html.write_text(mb.page("Conceptual architecture of the Manna Methodology", svg()), encoding="utf-8")
    mb.export_png(html, ROOT / "figures" / "manna-conceptual-architecture.png")
    print("ok", html)
