"""
Phase 2 (educators): pre-test and post-test scores, paired t-test and normalized (Hake) gain.
Data: phase2-educators/data/pre_post_test_87_educators.csv (semicolon-separated, UTF-8).
Normalized gain: g = (post - pre) / (10 - pre), computed for participants with pre < 10.
Run: python scripts/phase2_analysis.py
"""
from pathlib import Path
import pandas as pd
from scipy import stats

DATA = Path(__file__).resolve().parents[1] / "phase2-educators" / "data" / "pre_post_test_87_educators.csv"
MAX = 10.0

df = pd.read_csv(DATA, sep=";")
pre = pd.to_numeric(df["Total Pré"].astype(str).str.replace(",", "."), errors="coerce")
post = pd.to_numeric(df["Total Pós"].astype(str).str.replace(",", "."), errors="coerce")
ok = pre.notna() & post.notna()
pre, post = pre[ok], post[ok]

t, p = stats.ttest_rel(pre, post)
g = ((post - pre) / (MAX - pre))[pre < MAX]

print(f"N = {len(pre)}")
print(f"Pre-test mean  = {pre.mean():.2f}")
print(f"Post-test mean = {post.mean():.2f}")
print(f"Paired t-test: t({len(pre) - 1}) = {t:.2f}, p = {p:.2e}")
print(f"Normalized gain: mean = {g.mean():.2f}, median = {g.median():.2f} (n = {len(g)})")
