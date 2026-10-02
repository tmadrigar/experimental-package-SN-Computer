"""
Gera a Figura 3 (fluxo operacional do Framework da Metodologia Manna) em HTML + SVG inline,
no estilo comum dos diagramas (manna_blocks.py). Mesmo conteudo da figura original.
Execucao: python gerar_figura3_framework.py  (gera HTML e exporta o PNG usado no LaTeX)
"""
from pathlib import Path
import manna_blocks as mb

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures" / "html"

ROWS = [
    (["CONCEPTION AND", "STRUCTURING"], mb.SLATE, [
        ("design", ["INSTRUCTIONAL", "DESIGN"]),
        ("plan", ["LOGISTICAL AND", "RESOURCE PLANNING"]),
    ]),
    (["DIAGNOSTIC", "ASSESSMENT"], mb.BLUE, [
        ("form", ["SELECTION AND", "PREPARATION OF", "INSTRUMENTS"]),
        ("stars", ["APPLICATION", "AND DATA", "COLLECTION"]),
        ("gears", ["PROCESSING", "AND GROUPING"]),
    ]),
    (["FORMATIVE", "ASSESSMENT"], mb.SAND, [
        ("teach", ["CONDUCTION OF", "DIDACTIC", "ACTIVITIES"]),
        ("gain", ["PROGRESS", "EVALUATION"]),
        ("chat", ["CONTINUOUS", "FEEDBACK"]),
    ]),
    (["SUMMATIVE", "ASSESSMENT"], mb.SALMON, [
        ("pitch", ["FINAL PROJECT", "PRESENTATIONS"]),
        ("criteria", ["APPLICATION OF", "EVALUATION", "CRITERIA"]),
        ("linechart", ["CONSOLIDATION", "AND ANALYSIS", "OF RESULTS"]),
    ]),
]
W, H = 960, 664
ROW_Y = [32, 192, 352, 512]


def svg():
    return (f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" '
            f'aria-labelledby="framework-title framework-desc">'
            '<title id="framework-title">Operational flow of the Manna Methodology Framework</title>'
            '<desc id="framework-desc">Four colour-coded rows, Conception and Structuring, Diagnostic, Formative '
            'and Summative Assessment, each with the steps of the framework, from instructional design to the '
            'consolidation and analysis of results.</desc>'
            + mb.defs("f3-arrow") + f'<rect width="100%" height="100%" fill="{mb.PAPER}"/>'
            + mb.flow_rows(ROWS, W, "f3-arrow", ROW_Y) + '</svg>')


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    html = OUT / "manna-framework-operational-flow.html"
    html.write_text(mb.page("Manna Methodology Framework", svg()), encoding="utf-8")
    mb.export_png(html, ROOT / "figures" / "manna-framework-operational-flow.png")
    print("ok", html)
