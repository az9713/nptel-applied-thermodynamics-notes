"""Generate the chapter 22 area–Mach and chapter 23 shock diagrams."""

from pathlib import Path
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

FIGURES = Path(__file__).resolve().parent
sys.path.insert(0, str(FIGURES.parent / "code"))
from chapter_22 import area_ratio, mach_from_area
from chapter_23 import locate_shock, trial_shock

PALETTE = {
    "figure.facecolor": "#121821",
    "axes.facecolor": "#161f2b",
    "axes.labelcolor": "#edf2fa",
    "axes.edgecolor": "#697a93",
    "xtick.color": "#d1dcec",
    "ytick.color": "#d1dcec",
    "text.color": "#edf2fa",
    "font.family": "DejaVu Sans",
    "font.size": 11,
}


def sample(start, stop, count=180):
    """Return evenly spaced coordinates, including both ends."""
    return [start + index * (stop - start) / (count - 1)
            for index in range(count)]


def area_mach_diagram():
    fig, ax = plt.subplots(figsize=(8.0, 4.4), layout="constrained")
    subsonic = sample(0.13, 1)
    supersonic = sample(1, 3.04)
    ax.plot(subsonic, [area_ratio(m) for m in subsonic],
            color="#65d8d0", linewidth=2.7, label="Subsonic branch")
    ax.plot(supersonic, [area_ratio(m) for m in supersonic],
            color="#ffbc73", linewidth=2.7, label="Supersonic branch")
    ax.axhline(2, color="#a9bcdb", linestyle=":", linewidth=1)
    for supersonic_branch in (False, True):
        mach = mach_from_area(2, supersonic_branch)
        ax.scatter(mach, 2, color="#ffffff", zorder=4)
        ax.annotate(f"M = {mach:.3f}", (mach, 2),
                    xytext=(8, 8), textcoords="offset points")
    ax.scatter(1, 1, color="#ffffff", zorder=4)
    ax.annotate("Sonic minimum", (1, 1), xytext=(10, 7),
                textcoords="offset points")
    ax.set(xlim=(0, 3.1), ylim=(0.6, 4.6), xlabel="Mach number, M",
           ylabel="Area ratio, A / A*")
    ax.legend(loc="upper center", frameon=False)
    ax.grid(alpha=0.18)
    fig.savefig(FIGURES / "area-mach.png", dpi=150)
    plt.close(fig)


def shock_diagram():
    exit_to_throat = 3.5
    shock_areas = sample(1, exit_to_throat)
    exit_pressures = [trial_shock(area, exit_to_throat)[0]
                      for area in shock_areas]
    shock = locate_shock(0.5, exit_to_throat)
    fig, ax = plt.subplots(figsize=(8.0, 4.4), layout="constrained")
    ax.plot(shock_areas, exit_pressures, color="#65d8d0", linewidth=2.7)
    ax.axhline(0.5, color="#a9bcdb", linestyle=":", linewidth=1)
    ax.scatter([1, shock, 3.5],
               [exit_pressures[0], 0.5, exit_pressures[-1]],
               color="#ffffff", zorder=4)
    ax.annotate("First choking", (1, exit_pressures[0]), xytext=(14, -7),
                textcoords="offset points")
    ax.annotate(f"Target at A / At = {shock:.3f}", (shock, 0.5),
                xytext=(10, 18), textcoords="offset points")
    ax.annotate("Shock at exit", (3.5, exit_pressures[-1]),
                xytext=(-99, -14), textcoords="offset points")
    ax.set(xlim=(0.92, 3.6), ylim=(0.25, 1.07),
           xlabel="Trial shock area / geometric throat area",
           ylabel="Exit pressure / upstream total pressure")
    ax.grid(alpha=0.18)
    fig.savefig(FIGURES / "shock-pressure.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    with plt.rc_context(PALETTE):
        area_mach_diagram()
        shock_diagram()
