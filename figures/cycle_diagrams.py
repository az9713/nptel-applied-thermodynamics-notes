from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
out = Path("figures")
out.mkdir(exist_ok=True)
plt.rcParams.update({
    "figure.facecolor": "#111924", "axes.facecolor": "#111924",
    "text.color": "#e5ecf4", "axes.labelcolor": "#e5ecf4",
    "axes.edgecolor": "#416078", "xtick.color": "#c4d1df", "ytick.color": "#c4d1df",
    "axes.spines.top": False, "axes.spines.right": False, "grid.color": "#33455c",
    "font.size": 12, "axes.grid": True, "figure.dpi": 145,
})
cyan, orange = "#70d6ee", "#f6ad6a"
a = 2/7
ratio = np.geomspace(1.001, 5**(1/a)*0.999, 330)
scale = ratio**a
work = 1.005*(1500*(1-1/scale) - 300*(scale-1))
efficiency = 100*(1-1/scale)
optimum = 5**(1/(2*a))
fig, ax = plt.subplots(2, 1, sharex=True, figsize=(9,5.8), layout="constrained")
ax[0].set_title("Peak specific work and rising thermal efficiency", loc="left", pad=13)
ax[0].plot(ratio, work, c=cyan, lw=3)
ax[0].scatter([optimum], [1.005*(np.sqrt(1500)-np.sqrt(300))**2], color=cyan, s=40, zorder=5)
ax[0].annotate("Maximum work at 16.7", (optimum, 460.65), xytext=(29,400), arrowprops={"color":"#c4d1df","arrowstyle":"-"})
ax[0].set_ylabel("Net work (kJ/kg)")
ax[1].plot(ratio, efficiency, c=orange, lw=3)
ax[1].set_ylabel("Thermal efficiency (%)")
ax[1].set_xlabel("Overall pressure ratio (log scale)")
for axis in ax:
    axis.axvline(optimum, c="#8095ab", lw=1.2, ls="--")
    axis.set_xscale("log")
    axis.set_xlim(1,300)
fig.savefig(out/"chapter-10-brayton-tradeoff.png", bbox_inches="tight", pad_inches=.18)
plt.close(fig)

fig, ax = plt.subplots(figsize=(8.7,4.7), layout="constrained")
r, k, p1, t1, t3 = 10, 1.4, 100, 300, 1800
v2, v1 = 1/r, 1
t2 = t1*r**(k-1)
p2 = p1*r**k
cutoff = t3/t2
p3_otto = p1*(t3/t1)*r
vol = np.linspace(v2,v1,180)
ax.plot(vol,p1*(v1/vol)**k, ls="--", c="#c4d1df", lw=2, label="Common compression")
for title, start, p3, color in (("Otto",v2,p3_otto,cyan),("Diesel",v2*cutoff,p2,orange)):
    expansion = np.linspace(start,v1,170)
    ax.plot([v2,start], [p2,p3], c=color, lw=2.6, label=title)
    ax.plot(expansion,p3*(start/expansion)**k, c=color, lw=2.6)
    ax.plot([v1,v1],[p3*start**k,p1],c=color,lw=2.6)
    ax.scatter([start],[p3],c=color,s=36,zorder=4)
ax.set(xscale="log",yscale="log",xlabel="Specific volume / intake specific volume (log scale)",ylabel="Cylinder pressure (kPa, log scale)",xlim=(0.088,1.17),ylim=(87,8200))
ax.set_title("Same compression and peak temperature, different heating paths",loc="left", pad=13)
ax.legend(loc="upper right",facecolor="#111924",edgecolor="#416078",labelcolor="#e5ecf4")
fig.savefig(out/"chapter-12-heating-paths.png", bbox_inches="tight", pad_inches=.18)
