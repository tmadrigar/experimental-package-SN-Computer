"""
Phase 1 (students): descriptive statistics of the formative assessments (Kahoot).
For each case study and group: number of students, percentage of correct answers per session
(9 sessions x 5 questions), and the median and interquartile range of each student's overall
percentage of correct answers (45 items). An "X" marks a correct answer; an empty cell marks
no correct answer.
Data: phase1-students/data/case-study-<n>/*.csv
Run: python scripts/phase1_descriptive.py
"""
import csv
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parents[1] / "phase1-students" / "data"
CASES = [
    (1, "Maringá", "Case1_grup_experiment.csv", "Case1_grup_control.csv"),
    (2, "Campo Mourão", "Case2_group_experiment.csv", "Case2_group_control.csv"),
    (3, "Cianorte", "Case3_group_Experimental.csv", "Case3_group_control.csv"),
    (4, "Paranavaí", "Case4_group_experimental.csv", "Case4_group_control.csv"),
]


def load(path):
    rows = list(csv.reader(open(path, encoding="utf-8-sig")))
    return [[c.strip().upper() == "X" for c in r[1:46]] for r in rows[1:] if r and r[0].strip()]


for n, city, fe, fc in CASES:
    print(f"\nCase Study {n} ({city})")
    for label, f in (("Experimental", fe), ("Control", fc)):
        d = load(BASE / f"case-study-{n}" / f)
        sessions = [100 * sum(sum(v[5 * k:5 * k + 5]) for v in d) / (5 * len(d)) for k in range(9)]
        student = np.array([100 * sum(v) / 45 for v in d])
        q1, med, q3 = np.percentile(student, [25, 50, 75])
        print(f"  {label:<12} n={len(d):<3} sessions K1-K9: " + " ".join(f"{x:5.1f}" for x in sessions))
        print(f"  {'':<12} per-student score: median={med:.1f}  IQR={q3 - q1:.1f}")
