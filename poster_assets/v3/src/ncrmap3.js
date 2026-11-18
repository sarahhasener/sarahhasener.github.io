// Thematische Karte: Betroffene durch Carina + Südwestmonsun 2024 je Stadt der NCR (DSWD DROMIC #62, 03.09.2024).
const fs = require('fs');
const d3 = require('d3-geo');
const dir = process.argv[2];
const ncr = JSON.parse(fs.readFileSync(dir + '/ncr_lgus.geojson'));
const ctx = JSON.parse(fs.readFileSync(dir + '/context_provinces.geojson'));
// Ringe für d3 (sphärisch, im Uhrzeigersinn) korrigieren
function rewind(f) {
  if (d3.geoArea(f) > 2 * Math.PI) {
    const g = f.geometry;
    const rev = poly => poly.map(r => r.slice().reverse());
    if (g.type === 'Polygon') g.coordinates = rev(g.coordinates);
    else g.coordinates = g.coordinates.map(rev);
  }
  return f;
}
ncr.features.forEach(rewind); ctx.features.forEach(rewind);
const data = { 'Marikina': 400063, 'Quezon City': 307971, 'Manila': 142580, 'Caloocan': 94657, 'Pasig': 55483, 'Valenzuela': 55252,
  'Malabon': 51071, 'San Juan': 27966, 'Makati': 27710, 'Taguig': 24926, 'Navotas': 17054, 'Pateros': 16506, 'Mandaluyong': 12693,
  'Pasay': 10475, 'Las Piñas': 7604, 'Parañaque': 823, 'Muntinlupa': 133 };
const total = Object.values(data).reduce((a, b) => a + b, 0);
if (total !== 1252967) throw new Error('Summe falsch: ' + total);
const W = 1600, H = 1900;
const proj = d3.geoMercator().fitExtent([[40, 40], [W - 40, H - 360]], ncr);
const path = d3.geoPath(proj);
const SEA = '#e1eaec', CTX = '#efe6d6', CITY = '#fffaf1', EDGE = '#9b8576', ACC = '#9c4a22', ORG = '#d7932a', INK = '#1f1f1f', QUIET = '#52514e';
const camanava = new Set(['Caloocan', 'Malabon', 'Navotas', 'Valenzuela']);
let o = [`<rect width="${W}" height="${H}" fill="${SEA}"/>`];
for (const f of ctx.features) o.push(`<path d="${path(f)}" fill="${CTX}" stroke="#d6c8b2" stroke-width="2"/>`);
for (const f of ncr.features) o.push(`<path d="${path(f)}" fill="${CITY}" stroke="${EDGE}" stroke-width="2.5"/>`);
// Provinznamen
for (const f of ctx.features) {
  const c = path.centroid(f);
  if (!isFinite(c[0])) continue;
  const x = Math.min(Math.max(c[0], 120), W - 120), y = Math.min(Math.max(c[1], 60), H - 300);
  o.push(`<text x="${x}" y="${y}" text-anchor="middle" font-size="40" fill="#a0907c" font-style="italic">${f.properties.name}</text>`);
}
// Proportionale Kreise (Fläche ~ Betroffene)
const rMax = 150, r = v => rMax * Math.sqrt(v / 400063);
const feats = ncr.features.slice().sort((a, b) => data[b.properties.name] - data[a.properties.name]);
for (const f of feats) {
  const n = f.properties.name, v = data[n];
  const [cx, cy] = path.centroid(f);
  const col = n === 'Marikina' ? ACC : camanava.has(n) ? ORG : '#8a8178';
  o.push(`<circle cx="${cx}" cy="${cy}" r="${Math.max(r(v), 5)}" fill="${col}" fill-opacity="0.55" stroke="${col}" stroke-width="3"/>`);
}
// Beschriftung ausgewählter Städte
const labels = { 'Marikina': [0, 0], 'Quezon City': [0, -10], 'Manila': [-10, 0], 'Caloocan': [0, 0], 'Makati': [-20, 40], 'Pasig': [0, 0],
  'Valenzuela': [0, 0], 'Malabon': [30, 45], 'Navotas': [-90, -25], 'Taguig': [0, 30], 'Muntinlupa': [0, 0], 'Parañaque': [-20, 0],
  'Las Piñas': [-30, 0], 'Pasay': [-40, 0], 'San Juan': [0, 0], 'Mandaluyong': [0, 0], 'Pateros': [0, 0] };
const big = new Set(['Marikina', 'Quezon City', 'Manila', 'Makati']);
for (const f of ncr.features) {
  const n = f.properties.name;
  const [cx, cy] = path.centroid(f);
  const [dx, dy] = labels[n] || [0, 0];
  const fs_ = big.has(n) ? 44 : 32;
  o.push(`<text x="${cx + dx}" y="${cy + dy + 12}" text-anchor="middle" font-size="${fs_}" font-weight="${big.has(n) ? 700 : 500}" fill="${INK}" stroke="#fffaf1" stroke-width="7" paint-order="stroke">${n}</text>`);
}
// Gewässer
const lab = (lon, lat, t, s) => { const [x, y] = proj([lon, lat]); o.push(`<text x="${x}" y="${y}" text-anchor="middle" font-size="${s}" fill="#4f6b78" font-style="italic">${t}</text>`); };
lab(120.905, 14.55, 'Manila Bay', 52);
lab(121.17, 14.38, 'Laguna de Bay', 46);
// Legende
const ly = H - 330;
o.push(`<rect x="0" y="${ly - 15}" width="${W}" height="${H - ly + 15}" fill="#fbf5ea"/>`);
o.push(`<text x="560" y="${ly + 45}" font-size="40" font-weight="700" fill="${INK}">Betroffene je Stadt (Kreisfläche), 03.09.2024</text>`);
// verschachtelte Legendenkreise, unten bündig
const base = H - 20, lcx = 175;
for (const v of [400000, 100000, 20000]) {
  const rr = r(v);
  o.push(`<circle cx="${lcx}" cy="${base - rr}" r="${rr}" fill="none" stroke="${QUIET}" stroke-width="3"/>`);
  o.push(`<line x1="${lcx}" x2="${lcx + 190}" y1="${base - 2 * rr}" y2="${base - 2 * rr}" stroke="${QUIET}" stroke-width="2" stroke-dasharray="6 5"/>`);
  o.push(`<text x="${lcx + 200}" y="${base - 2 * rr + 12}" font-size="34" fill="${INK}">${v.toLocaleString('de-DE')}</text>`);
}
o.push(`<circle cx="590" cy="${ly + 115}" r="20" fill="${ACC}" fill-opacity="0.55" stroke="${ACC}" stroke-width="3"/><text x="625" y="${ly + 127}" font-size="36" fill="${INK}">Marikina (Flusstal)</text>`);
o.push(`<circle cx="590" cy="${ly + 180}" r="20" fill="${ORG}" fill-opacity="0.55" stroke="${ORG}" stroke-width="3"/><text x="625" y="${ly + 192}" font-size="36" fill="${INK}">CAMANAVA (Küste, Absenkung)</text>`);
o.push(`<circle cx="590" cy="${ly + 245}" r="20" fill="#8a8178" fill-opacity="0.55" stroke="#8a8178" stroke-width="3"/><text x="625" y="${ly + 257}" font-size="36" fill="${INK}">übrige Städte · Summe NCR: 1.252.967</text>`);
// Nordpfeil + Maßstab 5 km
o.push(`<path d="M${W - 80} 80 L${W - 100} 140 L${W - 80} 126 L${W - 60} 140 Z" fill="${INK}"/><text x="${W - 80}" y="70" text-anchor="middle" font-size="40" font-weight="700" fill="${INK}">N</text>`);
const [ax] = proj([121.0, 14.45]), [bx] = proj([121.0 + 5 / (111.32 * Math.cos(14.45 * Math.PI / 180)), 14.45]);
o.push(`<line x1="${W - 60 - (bx - ax)}" x2="${W - 60}" y1="200" y2="200" stroke="${INK}" stroke-width="8"/><text x="${W - 60 - (bx - ax) / 2}" y="182" text-anchor="middle" font-size="34" fill="${INK}">5 km</text>`);
const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" font-family="Inter, sans-serif">${o.join('')}</svg>`;
fs.writeFileSync(process.argv[3], svg);
console.log('ok', total);
