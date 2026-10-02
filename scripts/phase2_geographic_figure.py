"""
Gera resultados-fase2-distribuicao.png (300 dpi) em inglês.
Execução: python gerar_figura_f5.py
Dependência: pip install matplotlib
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

states = [
    ('PE', 'Pernambuco',        15),
    ('PR', 'Paraná',            10),
    ('AM', 'Amazonas',           8),
    ('SE', 'Sergipe',            6),
    ('GO', 'Goiás',              6),
    ('AL', 'Alagoas',            6),
    ('SP', 'São Paulo',          5),
    ('MG', 'Minas Gerais',       5),
    ('RJ', 'Rio de Janeiro',     5),
    ('PA', 'Pará',               4),
    ('PB', 'Paraíba',            3),
    ('BA', 'Bahia',              3),
    ('DF', 'Federal District',   2),
    ('MA', 'Maranhão',           2),
    ('AP', 'Amapá',              2),
    ('PI', 'Piauí',              2),
    ('RR', 'Roraima',            2),
    ('RS', 'Rio Grande do Sul',  1),
]

states_rev = list(reversed(states))
abbrs  = [s[0] for s in states_rev]
names  = [s[1] for s in states_rev]
counts = [s[2] for s in states_rev]
n      = len(states_rev)

BAR_COLOR  = '#1d4470'
TEXT_DARK  = '#0d1b2a'
TEXT_SUB   = '#5a6e80'
GRID_COLOR = '#dde4ec'
AXIS_COLOR = '#a8b8c8'

fig, ax = plt.subplots(figsize=(8.2, 7.0))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# bars
bars = ax.barh(range(n), counts, height=0.62,
               color=BAR_COLOR, edgecolor='none', zorder=3)

# value labels at end of each bar
for bar, val in zip(bars, counts):
    ax.text(bar.get_width() + 0.18,
            bar.get_y() + bar.get_height() / 2,
            str(val), va='center', ha='left',
            fontsize=9, fontweight='semibold', color=TEXT_DARK)

# y-axis labels: "PE  Pernambuco" combined, right-aligned
ax.set_yticks(range(n))
ax.set_yticklabels(
    [f'{a}  {nm}' for a, nm in zip(abbrs, names)],
    fontsize=9, ha='right', color=TEXT_DARK
)
ax.tick_params(axis='y', pad=8, length=0)

# vertical grid at 0, 4, 8, 12, 16
ax.xaxis.set_major_locator(ticker.MultipleLocator(4))
ax.grid(axis='x', color=GRID_COLOR, linewidth=0.75, zorder=0)
ax.set_axisbelow(True)

# spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color(AXIS_COLOR)

ax.set_xlim(0, 17.5)
ax.set_xlabel('Number of Participants', fontsize=10.5,
              color=TEXT_SUB, labelpad=9)
ax.tick_params(axis='x', labelsize=9.5, colors=TEXT_SUB)

ax.set_title(
    'Geographic Distribution of Responding Participants\n'
    'Phase 2 · N = 87 · 18 Federal Units',
    fontsize=11.5, fontweight='semibold', color=TEXT_DARK,
    pad=14, linespacing=1.55
)

plt.tight_layout(pad=1.6)

out = str(__import__('pathlib').Path(__file__).resolve().parents[1] / 'figures' / 'phase2-geographic-distribution.png')
plt.savefig(out, dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print(f'Salvo: {out}')
