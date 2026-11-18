// Lagekarte: Philippinen in Südostasien, Manila markiert. Daten: Natural Earth 50m (gemeinfrei) via world-atlas.
const fs = require('fs');
const topo = require('topojson-client');
const d3 = require('d3-geo');
const world = JSON.parse(fs.readFileSync(require.resolve('world-atlas/countries-50m.json')));
const countries = topo.feature(world, world.objects.countries).features;
const W = 1000, H = 1050;
const box = { type: 'Feature', geometry: { type: 'Polygon', coordinates: [[[96, -6], [96, 27], [134, 27], [134, -6], [96, -6]]] } };
const proj = d3.geoMercator().fitExtent([[0, 0], [W, H]], box);
const path = d3.geoPath(proj);
const isPH = f => f.properties.name === 'Philippines';
const ACC = '#c98a1e', LAND = '#e6d9c3', EDGE = '#fbf5ea', SEA = '#e1eaec', INK = '#1f1f1f', QUIET = '#52514e';
let out = [];
out.push(`<rect x="0" y="0" width="${W}" height="${H}" fill="${SEA}"/>`);
for (const f of countries) {
  const d = path(f);
  if (!d) continue;
  out.push(`<path d="${d}" fill="${isPH(f) ? ACC : LAND}" fill-opacity="${isPH(f) ? 0.85 : 1}" stroke="${EDGE}" stroke-width="1.2"/>`);
}
const [mx, my] = proj([120.98, 14.6]);
out.push(`<circle cx="${mx}" cy="${my}" r="20" fill="#9c4a22" stroke="#fbf5ea" stroke-width="6"/>`);
out.push(`<text x="${mx - 22}" y="${my + 10}" text-anchor="end" font-size="64" font-weight="700" fill="${INK}" stroke="${SEA}" stroke-width="12" paint-order="stroke">Manila</text>`);
const lab = (lon, lat, t, size = 30, col = QUIET, it = false) => {
  const [x, y] = proj([lon, lat]);
  out.push(`<text x="${x}" y="${y}" text-anchor="middle" font-size="${size}" fill="${col}" ${it ? 'font-style="italic"' : ''}>${t}</text>`);
};
lab(125.6, 8.6, 'PHILIPPINEN', 52, INK);
lab(112.0, 8.4, 'Südchine-', 46, '#4f6b78', true);
lab(112.0, 6.0, 'sisches Meer', 46, '#4f6b78', true);
lab(129.5, 21.0, 'Pazifik', 50, '#4f6b78', true);
lab(106.0, 22.0, 'Vietnam', 44);
lab(114.2, 0.8, 'Borneo', 44);
// Maßstab: 500 km bei 15° N
const [sx0, sy0] = proj([100, -3.5]);
const [sx1] = proj([100 + 500 / (111.32 * Math.cos(15 * Math.PI / 180)), -3.5]);
out.push(`<line x1="${sx0}" y1="${sy0}" x2="${sx1}" y2="${sy0}" stroke="${INK}" stroke-width="10"/>`);
out.push(`<text x="${(sx0 + sx1) / 2}" y="${sy0 - 14}" text-anchor="middle" font-size="40" fill="${INK}">500 km</text>`);
// Nordpfeil
out.push(`<path d="M${W - 60} 70 L${W - 78} 120 L${W - 60} 108 L${W - 42} 120 Z" fill="${INK}"/><text x="${W - 60}" y="60" text-anchor="middle" font-size="44" font-weight="700" fill="${INK}">N</text>`);
// Gradnetz-Beschriftung
for (const lat of [0, 10, 20]) { const [, y] = proj([96, lat]); out.push(`<text x="8" y="${y - 6}" font-size="34" fill="${QUIET}">${lat}° N</text><line x1="0" x2="${W}" y1="${y}" y2="${y}" stroke="#c9bfae" stroke-width="1" stroke-dasharray="6 6"/>`); }
for (const lon of [100, 110, 120]) { const [x] = proj([lon, 0]); out.push(`<text x="${x + 6}" y="${H - 10}" font-size="34" fill="${QUIET}">${lon}° O</text><line x1="${x}" x2="${x}" y1="0" y2="${H}" stroke="#c9bfae" stroke-width="1" stroke-dasharray="6 6"/>`); }
const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" font-family="Inter, sans-serif">${out.join('')}<rect x="1" y="1" width="${W - 2}" height="${H - 2}" fill="none" stroke="#b9a68f" stroke-width="2"/></svg>`;
fs.writeFileSync(process.argv[2], svg);
console.log('ok', Math.round(mx), Math.round(my));
