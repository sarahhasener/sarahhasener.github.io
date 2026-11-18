"""Wirkungsgefüge Hochwasser Metro Manila als SVG (Einheiten: 0,1 mm; Breite 178 mm)."""
import sys

W = 1780
ACC = "#2f6690"
ORG = "#5a3426"
RED = "#9c4a22"
GRN = "#5b7a3a"
INK = "#1f1f1f"
QUIET = "#52514e"
LINE = "#8a6a55"
FILL = "#fffaf1"

out = []
FS = 43      # 13 pt ≈ 4,6 mm
FSS = 35     # 11,3 pt


def box(x, y, w, h, title, lines=(), stroke=LINE, fill=FILL, bold=True, tc=INK):
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}" stroke="{stroke}" stroke-width="4"/>')
    cy = y + 62
    out.append(f'<text x="{x + w / 2}" y="{cy}" text-anchor="middle" font-size="{FS}" font-weight="{700 if bold else 400}" fill="{tc}">{title}</text>')
    for i, ln in enumerate(lines):
        out.append(f'<text x="{x + w / 2}" y="{cy + 52 * (i + 1)}" text-anchor="middle" font-size="{FSS}" fill="{QUIET}">{ln}</text>')


def arrow(x1, y1, x2, y2, sign=None, color=LINE, sx=0, sy=0):
    out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="5" marker-end="url(#ah-{color[1:]})"/>')
    if sign:
        mx, my = (x1 + x2) / 2 + sx, (y1 + y2) / 2 + sy
        out.append(f'<circle cx="{mx}" cy="{my}" r="27" fill="#fffaf1" stroke="{color}" stroke-width="3"/>')
        out.append(f'<text x="{mx}" y="{my + 15}" text-anchor="middle" font-size="44" font-weight="700" fill="{color}">{sign}</text>')


# Zeile 1: Ursachen
bw, bh, gap = 410, 250, 46
xs = [0, bw + gap, 2 * (bw + gap), 3 * (bw + gap)]
y1 = 70
out.append(f'<text x="0" y="40" font-size="{FSS}" font-weight="700" fill="{QUIET}" letter-spacing="2">URSACHEN</text>')
box(xs[0], y1, bw, bh, "Klimawandel", ["Meeresspiegel steigt,", "Starkregen (Carina", "2024: 471 mm/24 h)"])
box(xs[1], y1, bw, bh, "Grundwasser", ["übernutzt →", "Landabsenkung", "(cm pro Jahr)"])
box(xs[2], y1, bw, bh, "Müll, Bebauung", ["an Esteros und Flüssen", "blockieren den", "Abfluss"])
box(xs[3], y1, bw, bh, "Landgewinnung", ["Manila Bay; Wirkung", "auf Hochwasser", "umstritten"])

# Zeile 2: Hochwasser
y2 = 450
hx, hw, hh = 440, 900, 130
out.append(f'<rect x="{hx}" y="{y2}" width="{hw}" height="{hh}" rx="14" fill="{ACC}" fill-opacity="0.12" stroke="{ACC}" stroke-width="6"/>')
out.append(f'<text x="{hx + hw / 2}" y="{y2 + 82}" text-anchor="middle" font-size="54" font-weight="700" fill="{INK}">Überflutungen in Metro Manila</text>')
for i, x in enumerate(xs):
    cx = x + bw / 2
    tx = hx + 120 + i * (hw - 240) / 3
    arrow(cx, y1 + bh, tx, y2 - 8, "+", LINE, sx=(-30 if i < 2 else 30), sy=-6)

# Zeile 3: ungleiche Betroffenheit
y3 = 710
lw = 860
box(0, y3, lw, 230, "Hohe Betroffenheit", ["Informelle Siedlungen an Wasserläufen,", "Marikina-Tal, Küstenstädte (CAMANAVA)", "→ wenig Rücklagen, kaum Alternativen"],
    stroke=RED, fill="#f6e2d6")
box(W - lw, y3, lw, 230, "Geringe Betroffenheit", ["Geschäftszentren (Makati, BGC),", "formelle Wohnviertel", "→ höher gelegen, besser geschützt"],
    stroke=GRN, fill="#eaf0df")
arrow(hx + 220, y2 + hh, 430, y3 - 8, "+", RED, sx=-34)
arrow(hx + hw - 220, y2 + hh, W - 430, y3 - 8, None, GRN)

# Zeile 4: Folgen
y4 = 1020
box(0, y4, lw, 170, "Folgen", ["Tote, Leptospirose, Schäden,", "Verlust von Einkommen und Besitz"], stroke=RED, fill="#f6e2d6")
arrow(430, y3 + 230, 430, y4 - 8, "+", RED, sx=-40)

# Zeile 5: Maßnahmen
y5 = 1300
out.append(f'<text x="{W}" y="{y5 - 22}" text-anchor="end" font-size="{FSS}" font-weight="700" fill="{QUIET}" letter-spacing="2">MASSNAHMEN UND GOVERNANCE</text>')
mw = 560
box(0, y5, mw, 260, "Graue Infrastruktur", ["Pumpstationen,", "Flussausbau Pasig-Marikina"], stroke="#b07a12", fill="#f8ebcf")
box(mw + 50, y5, mw, 260, "Umsiedlung", ["Sicherheit ↑: 95,5 % ohne", "Hochwasser; Einkommen ↓", "bei 48,3 % der Haushalte"], stroke="#b07a12", fill="#f8ebcf")
box(2 * (mw + 50), y5, W - 2 * (mw + 50), 260, "Governance-Defizite", ["Korruption,", "zersplitterte", "Zuständigkeiten"], stroke=ORG, fill="#efe1d6")
# Infrastruktur dämpft Überflutung
gx = 280
out.append(f'<path d="M{gx} {y5} V{y4 + 200} H{890} V{y2 + hh + 8}" fill="none" stroke="{ACC}" stroke-width="5" marker-end="url(#ah-{ACC[1:]})"/>')
out.append(f'<circle cx="890" cy="{y3 + 115}" r="27" fill="#fffaf1" stroke="{ACC}" stroke-width="3"/>')
out.append(f'<text x="890" y="{y3 + 130}" text-anchor="middle" font-size="44" font-weight="700" fill="{ACC}">−</text>')
# Umsiedlung reduziert Exposition der Betroffenen, aber erzeugt neue Folgen
ux = 760
out.append(f'<path d="M{ux} {y5} V{y4 + 178}" fill="none" stroke="{ACC}" stroke-width="5" marker-end="url(#ah-{ACC[1:]})"/>')
out.append(f'<text x="{ux - 18}" y="{y4 + 250}" text-anchor="end" font-size="{FSS}" fill="{ACC}" font-weight="700">sozialer Preis</text>')
# Governance schwächt Infrastruktur
out.append(f'<path d="M{2 * (mw + 50)} {y5 + 115} H{2 * mw + 58}" fill="none" stroke="{ORG}" stroke-width="5" marker-end="url(#ah-{ORG[1:]})"/>')
out.append(f'<path d="M{2 * (mw + 50) + 10} {y5 + 220} C {mw + 360} {y5 + 360}, {300} {y5 + 360}, {280} {y5 + 268}" fill="none" stroke="{ORG}" stroke-width="5" marker-end="url(#ah-{ORG[1:]})"/>')
out.append(f'<circle cx="{mw + 330}" cy="{y5 + 330}" r="27" fill="#fffaf1" stroke="{ORG}" stroke-width="3"/>')
out.append(f'<text x="{mw + 330}" y="{y5 + 345}" text-anchor="middle" font-size="44" font-weight="700" fill="{ORG}">−</text>')

H = y5 + 390
# Legende
out.append(f'<text x="{W}" y="{H - 8}" text-anchor="end" font-size="{FSS - 4}" fill="{QUIET}">+ verstärkt   − schwächt</text>')

defs = "".join(
    f'<marker id="ah-{c[1:]}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{c}"/></marker>'
    for c in [LINE, ACC, ORG, RED, GRN])
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-10 0 {W + 20} {H + 10}" font-family="Inter, sans-serif">'
       f'<defs>{defs}</defs>{"".join(out)}</svg>')
open(sys.argv[1], "w").write(svg)
print("ok", H)
