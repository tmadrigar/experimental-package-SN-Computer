# Experimental package: Manna Methodology (SN Computer Science)

Research data, instruments, and scripts supporting the article:

> Madrigar, T. T., Calvo, R., & Aylon, L. B. R. **Manna Methodology: An Integrative Framework for
> Learning, Assessment, and Socio-Emotional Skills in Education 5.0.** *SN Computer Science*
> (manuscript SNCS-D-25-06649, accepted subject to minor revisions).

It extends the conference paper:

> Madrigar, T. T., Calvo, R., & Aylon, L. B. R. (2025). Manna Methodology: A Novel Approach to
> Education 5.0 Through Learning and Socio-Emotional Assessment in IoD Bootcamps. *Proceedings of
> CSEDU 2025*, Vol. 2, pp. 504–515. SciTePress. https://doi.org/10.5220/0013220900003932

## Overview

The Manna Methodology is a four-phase framework (Conception, Diagnostic, Formative, and Summative
Assessment) with two application models:

- **Phase 1, Manna-Student Model:** 195 public school students in Internet of Drones (IoD) bootcamps
  in four cities of Paraná, Brazil (January 2024). Experimental teams were formed from learning style
  (LSI) and socio-emotional (SECD) profiles; control teams followed the usual class composition.
- **Phase 2, Manna-Teacher Model:** 235 educators from across Brazil in a three-day immersive training
  ("Manna at the Museum 2025", March 2025), with pre-test and post-test and app-based feedback.

## Repository structure

```
.
├── phase1-students/
│   ├── data/case-study-1 … case-study-4/   Kahoot formative assessments, one CSV per group
│   ├── data/preliminary-study/              learning style inventory of the 2023 preliminary study (n = 45)
│   └── instruments/                         SECD scale, curriculum, and competition rubric
├── phase2-educators/
│   ├── data/                                pre/post-test results
│   └── instruments/                         program of the training and description of instruments
├── scripts/                                 analysis and figure scripts
└── figures/                                 figures of the article (PNG) and their HTML/SVG sources
```

## Data

### Phase 1: formative assessments (`phase1-students/data/`)

One CSV per case study and group. Each row is a student (anonymized code `Aluno1` to `Aluno195`);
columns `Kahoot k - Qj` are the 45 items (9 sessions × 5 questions). `X` = correct answer; empty =
no correct answer.

| Case study | City | Experimental | Control | Total |
|---|---|---|---|---|
| 1 | Maringá | 26 | 24 | 50 |
| 2 | Campo Mourão | 15 | 15 | 30 |
| 3 | Cianorte | 39 | 39 | 78 |
| 4 | Paranavaí | 19 | 18 | 37 |
| | **Total** | **99** | **96** | **195** |

### Preliminary study (`phase1-students/data/preliminary-study/`)

`preliminary_study_LSI_45_participants.xlsx`: item responses of 45 volunteers (anonymized as
`participante1` to `participante45`) to the learning style inventory used in the 2023 preliminary study.
Item columns 1–12, 13–23, 24–34, and 35–44 are summed into the Accommodator, Converger, Assimilator,
and Diverger scores used in Figure 2.

### Phase 2: educators (`phase2-educators/data/`)

- `pre_post_test_87_educators.csv` (semicolon-separated, UTF-8): one row per educator with complete
  pre-test and post-test (N = 87). Columns in Portuguese: profile questions, state (`Estado`), age group
  (`Faixa etária`), item results `Pré Qk` / `Pós Qk` (1 = correct, 0 = incorrect), totals
  (`Total Pré`, `Total Pós`, 0 to 10) and normalized gain (`Ganho Hake`).

The spontaneous comments recorded during the event are open texts that may identify participants
and are therefore not published; their analysis is described in Section 4.2.3 of the article.

## Reproducing the results

```bash
pip install -r requirements.txt
python scripts/phase1_descriptive.py           # Phase 1: correct answers per session and per student
python scripts/phase2_analysis.py              # Phase 2: pre/post means, paired t-test, normalized gain
python scripts/figure1_architecture.py         # Figure 1
python scripts/figure3_framework.py            # Figure 3
python scripts/phase2_teacher_model_figure.py  # Figure 4
python scripts/phase1_case_figures.py          # Figures 5–8
python scripts/phase1_boxplot_figure.py        # Figure 9
python scripts/figures2_10_11_charts.py        # Figures 2, 10, and 11
```

Each figure script writes an HTML/SVG source to `figures/html/`; the PNG files in `figures/` were
exported from these sources at 3× scale (figure scripts that export PNG directly require
`pip install playwright` and `playwright install chromium`).

| Figure / result in the article | Source |
|---|---|
| Figure 1 (conceptual architecture) | `figure1_architecture.py` |
| Figure 2 (correlation matrix of learning styles) | `figures2_10_11_charts.py` + `phase1-students/data/preliminary-study/` |
| Figure 3 (operational flow of the framework) | `figure3_framework.py` |
| Figure 4 (phases of the Manna-Teacher Model) | `phase2_teacher_model_figure.py` |
| Figures 5–8 (correct answers per Kahoot session) | `phase1_case_figures.py` + `phase1-students/data/` |
| Figure 9 (distribution of formative scores) | `phase1_boxplot_figure.py` + `phase1-students/data/` |
| Figures 10–11 (educators by federal unit; pre/post-test scores) | `figures2_10_11_charts.py` + `phase2-educators/data/` |
| Pre/post-test means, paired t-test, and normalized gain (Section 4.2.2) | `phase2_analysis.py` + `phase2-educators/data/` |

## Ethics and privacy

The research was approved by the Permanent Committee for Ethics in Research of the State University
of Maringá (COPEP/UEM), consolidated opinion no. 7.740.231 (CAAE 90289025.0.0000.0104). Informed
consent (TCLE) and assent (TALE) were obtained from all participants. All published data are
anonymized: no names, identification numbers, contact data, or photographs are included.

## License

- Data and documentation: [CC BY 4.0](LICENSE-DATA)
- Code: [MIT](LICENSE)

## Contact

Tiago Tadeu Madrigar, State University of Maringá (UEM), Brazil: tiago@madrigar.com.br
