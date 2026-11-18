"""Diagramme für das A1-Poster (SVG, in Druckgröße: 1 pt im SVG = 1 pt auf dem Poster)."""
import sys
import matplotlib
matplotlib.use("svg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

for f in fm.findSystemFonts():
    if "/inter/" in f.lower():
        fm.fontManager.addfont(f)

MM = 1 / 25.4
ACC = "#9c4a22"      # Akzent (Referenzpalette Slot 1)
ACC2 = "#eb6834"     # zweite Kategorie (Slot 2)
GREY = "#8a8178"
GREY_L = "#cfcfc8"
INK = "#1f1f1f"
QUIET = "#52514e"
GRID = "#e6d9c3"

plt.rcParams.update({"hatch.linewidth": 1.4, 
    "font.family": "Inter", "font.size": 22, "svg.fonttype": "path",
    "axes.spines.top": False, "axes.spines.right": False, "axes.spines.left": False,
    "axes.edgecolor": "#a0907c", "figure.facecolor": "#fbf5ea", "axes.facecolor": "#fbf5ea", "savefig.facecolor": "#fbf5ea", "xtick.color": QUIET, "ytick.color": QUIET,
})


def de(n):
    return f"{n:,}".replace(",", ".")


def carina(path, w_mm, h_mm):
    rows = [("Marikina", 400063), ("Quezon City", 307971), ("Manila", 142580), ("Caloocan", 94657),
            ("Pasig", 55483), ("Valenzuela", 55252), ("Malabon", 51071), ("San Juan", 27966), ("Makati", 27710),
            ("Taguig", 24926), ("Navotas", 17054), ("Pateros", 16506), ("Mandaluyong", 12693), ("Pasay", 10475),
            ("Las Piñas", 7604), ("Parañaque", 823), ("Muntinlupa", 133)]
    assert sum(v for _, v in rows) == 1252967
    camanava = {"Caloocan", "Malabon", "Navotas", "Valenzuela"}
    fig, ax = plt.subplots(figsize=(w_mm * MM, h_mm * MM))
    names = [n for n, _ in rows][::-1]
    vals = [v for _, v in rows][::-1]
    cols = [ACC if n == "Marikina" else (ACC2 if n in camanava else GREY) for n in names]
    ax.barh(names, vals, color=cols, height=0.72)
    ax.set_xlim(0, 470000)
    ax.set_xticks([0, 100000, 200000, 300000, 400000])
    ax.set_xticklabels(["0", "100.000", "200.000", "300.000", "400.000"], fontsize=18.8)
    ax.tick_params(axis="y", length=0, labelsize=20.3, pad=6)
    ax.tick_params(axis="x", length=0, pad=6)
    ax.grid(axis="x", color=GRID, lw=1)
    ax.set_axisbelow(True)
    for n, v in zip(names, vals):
        if n in ("Marikina", "Quezon City", "Manila", "Makati"):
            lab = de(v) + (" (Geschäftszentrum)" if n == "Makati" else "")
            ax.text(v + 6000, n, lab, va="center", fontsize=20.3,
                    fontweight="semibold" if n == "Marikina" else "normal", color=INK)
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=ACC, label="Marikina (Flusstal des Marikina)"),
                       Patch(color=ACC2, label="CAMANAVA (Küstenstädte, Absenkung)"),
                       Patch(color=GREY, label="übrige Städte der NCR")],
              loc="lower right", bbox_to_anchor=(1.0, 0.02), frameon=False, fontsize=18.8, handlelength=1.2)
    ax.text(455000, 11.6, "Marikina allein: 32 % der\n1.252.967 Betroffenen der NCR", ha="right", fontsize=20.3,
            color=INK, fontweight="semibold", linespacing=1.35)
    ax.set_xlabel("Betroffene Personen (Stand 03.09.2024)", fontsize=18.8, color=QUIET, labelpad=8)
    fig.subplots_adjust(left=0.2, right=0.97, top=0.99, bottom=0.14)
    fig.savefig(path)


def raten(path, w_mm, h_mm):
    rows = [  # label, low, high, verified
        ("Globaler Meeresspiegel,\nProjektion bis 2100 (RCP2.6)", 4.4, 4.4, True),
        ("Globaler Meeresspiegel,\nProjektion bis 2100 (RCP8.5)", 11.2, 11.2, True),
        ("Relativer Meeresspiegel\nManila Bay, 1960–2012", 15, 15, True),
        ("Absenkung Manila und\nCAMANAVA, 2015–2019", 10, 20, False),
        ("Absenkung Bulacan, Cavite,\nLaguna, 2015–2019", 40, 40, False),
    ]
    fig, ax = plt.subplots(figsize=(w_mm * MM, h_mm * MM))
    y = list(range(len(rows)))[::-1]
    for yi, (lab, lo, hi, ok) in zip(y, rows):
        c = ACC if "Manila Bay" in lab else (GREY if ok else ACC2)
        if lo == hi:
            if ok:
                ax.barh(yi, hi, color=c, height=0.62)
            else:
                ax.barh(yi, hi, color="#fbd9c9", height=0.62, hatch="//", edgecolor=ACC2, lw=0)
            txt = ("> " if "Bulacan" in lab else "") + f"{hi:g}".replace(".", ",")
        else:
            ax.barh(yi, hi, color="#fbd9c9", height=0.62, hatch="//", edgecolor=ACC2, lw=0)
            txt = f"{lo:g}–{hi:g}"
        ax.text(hi + 0.8, yi, txt + " mm/Jahr", va="center", fontsize=20.3, color=INK,
                fontweight="semibold" if "Manila Bay" in lab else "normal")
    ax.set_yticks(y)
    ax.set_yticklabels([r[0] for r in rows], fontsize=18.8)
    ax.set_xlim(0, 66)
    ax.set_xticks([0, 10, 20, 30, 40, 50])
    ax.tick_params(length=0, pad=6, labelsize=18.8)
    ax.grid(axis="x", color=GRID, lw=1)
    ax.set_axisbelow(True)
    ax.set_xlabel("Millimeter pro Jahr", fontsize=18.8, color=QUIET, labelpad=8)
    fig.text(0.98, 0.015, "schraffiert = vorläufig (nur aus Suchauszug, Originalstudie nicht abrufbar)", ha="right",
             fontsize=17.4, color=QUIET)
    fig.subplots_adjust(left=0.42, right=0.98, top=0.99, bottom=0.27)
    fig.savefig(path)


def bevoelkerung(path, w_mm, h_mm):
    kern = [(1903, 219928), (1918, 285306), (1939, 623492), (1948, 983906), (1960, 1138611), (1970, 1330788),
            (1980, 1630485), (1990, 1601234), (2000, 1581082), (2010, 1652171), (2015, 1780148),
            (2020, 1846513), (2024, 1902590)]
    ncr = [(1903, 328939), (1918, 461166), (1939, 993889), (1948, 1569128), (1960, 2462488), (1970, 3966695),
           (1975, 4970006), (1980, 5925884), (1990, 7948392), (2000, 9932560), (2010, 11855975),
           (2015, 12877253), (2020, 13484462), (2024, 14001751)]
    un = [(1975, 8329012), (1990, 13910000), (2000, 17800000), (2010, 21070000), (2020, 24010000),
          (2025, 24735305)]
    fig, ax = plt.subplots(figsize=(w_mm * MM, h_mm * MM))
    ax.set_xlim(1900, 2080)
    ax.spines["bottom"].set_bounds(1900, 2050)
    ax.set_ylim(0, 31e6)
    ax.set_yticks([0, 5e6, 10e6, 15e6, 20e6, 25e6])
    ax.set_yticklabels(["0", "5", "10", "15", "20", "25"], fontsize=18.8)
    ax.set_xticks([1900, 1925, 1950, 1975, 2000, 2025, 2050])
    ax.tick_params(length=0, pad=6, labelsize=18.8)
    ax.grid(axis="y", color=GRID, lw=1)
    ax.set_axisbelow(True)
    ax.set_ylabel("Mio. Einwohner", fontsize=18.8, color=QUIET)
    ax.axvline(1975, color="#a0907c", lw=1, ls=(0, (3, 3)))
    ax.text(1973, 18e6, "1975: Gründung\nMetro Manila", ha="right", va="center", fontsize=18.1, color=QUIET)
    for d, c, a in [(kern, GREY, 0.65), (ncr, GREY, 1)]:
        xs, ys = zip(*d)
        ax.plot(xs, ys, color=c, alpha=a, lw=3.4, marker="o", ms=6)
    xs, ys = zip(*un)
    ax.plot(xs, ys, color=ACC, lw=4.2, marker="o", ms=7)
    ax.plot([2025, 2050], [24735305, 27119826], color=ACC, lw=2.4, ls=(0, (5, 4)))
    ax.plot([2050], [27119826], marker="o", ms=6, mfc="#fbf5ea", mec=ACC, mew=2)
    ax.text(2050, 29.6e6, "UN-Agglomeration: 24,7 Mio. (2025);\n27,1 Mio. (2050, Projektion)", fontsize=18.1,
            color=INK, va="center", ha="right")
    ax.text(2030, 14.0e6, "NCR / Metro Manila\n14,0 Mio. (2024)", fontsize=18.1, color=INK, va="center")
    ax.text(2030, 4.6e6, "Kernstadt\n1,9 Mio. (2024)", fontsize=18.1, color=INK, va="center")
    fig.subplots_adjust(left=0.1, right=0.99, top=0.98, bottom=0.12)
    fig.savefig(path)


if __name__ == "__main__" and False:
    out = sys.argv[1]
    carina(f"{out}/abb_carina.svg", 172, 112)
    raten(f"{out}/abb_raten.svg", 172, 72)
    bevoelkerung(f"{out}/abb_bevoelkerung.svg", 172, 96)

if __name__ == "__main__":
    out = sys.argv[1]
    bevoelkerung(f"{out}/abb_bevoelkerung_A1.svg", 260, 150)
    raten(f"{out}/abb_raten_A1.svg", 260, 120)
