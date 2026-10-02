"""
Gera a Figura 4 (fases do Modelo Manna-Docente) em HTML + SVG inline, no estilo comum dos
diagramas (manna_blocks.py), com a mesma estrutura da Figura 3.
Fontes do conteudo: programacao oficial do Manna no Museu 2025 (14 a 16/03/2025),
Base_Unificada_Manna_87_Respostas_Avaliacao e termos de compromisso.
Execucao: python gerar_figura4_modelo_docente.py  (gera HTML e exporta o PNG usado no LaTeX)
"""
from pathlib import Path
import manna_blocks as mb

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures" / "html"

ROWS = [
    (["CONCEPTION"], mb.SLATE, [
        ("design", ["PROGRAM ON AI,", "QUANTUM AND", "INNOVATION"]),
        ("call", ["PUBLIC CALL", "AND SELECTION", "OF EDUCATORS"]),
        ("plan", ["LOGISTICS AND", "RESOURCE", "PLANNING"]),
    ]),
    (["DIAGNOSTIC", "ASSESSMENT"], mb.BLUE, [
        ("form", ["PROFILE AND", "EXPECTATIONS", "QUESTIONNAIRE"]),
        ("quiz", ["PRE-TEST ON", "EXPONENTIAL", "TECHNOLOGIES"]),
        ("baseline", ["KNOWLEDGE", "BASELINE"]),
    ]),
    (["FORMATIVE", "ASSESSMENT"], mb.SAND, [
        ("teach", ["MINICOURSES", "AND HANDS-ON", "STATIONS"]),
        ("team", ["MANNA VAI", "TEAM DYNAMIC"]),
        ("chat", ["CONTINUOUS", "FEEDBACK", "VIA APP"]),
    ]),
    (["SUMMATIVE", "ASSESSMENT"], mb.SALMON, [
        ("pitch", ["MANNA SHOW", "PITCHES"]),
        ("gain", ["POST-TEST AND", "HAKE GAIN"]),
        ("commit", ["REPLICATION", "COMMITMENTS"]),
    ]),
]
W, H = 960, 664
ROW_Y = [32, 192, 352, 512]


def svg():
    return (f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" '
            f'aria-labelledby="teacher-model-title teacher-model-desc">'
            '<title id="teacher-model-title">Phases of the Manna-Teacher Model</title>'
            '<desc id="teacher-model-desc">Four colour-coded rows, Conception, Diagnostic, Formative and Summative '
            'Assessment, each with three steps of the training delivered to educators; the pre-test establishes the '
            'knowledge baseline and the post-test yields the normalized (Hake) gain.</desc>'
            + mb.defs("f4-arrow") + f'<rect width="100%" height="100%" fill="{mb.PAPER}"/>'
            + mb.flow_rows(ROWS, W, "f4-arrow", ROW_Y) + '</svg>')


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    html = OUT / "manna-teacher-model-phases.html"
    html.write_text(mb.page("Phases of the Manna-Teacher Model", svg()), encoding="utf-8")
    mb.export_png(html, ROOT / "figures" / "manna-teacher-model-phases.png")
    print("ok", html)
