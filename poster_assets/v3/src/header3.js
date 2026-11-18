// Hintergrund (Braun + weißer Kopf mit Wellenkante + Weltkarte) und Globus. Daten: Natural Earth 50m/110m via world-atlas (gemeinfrei).
const fs = require('fs'); const topo = require('topojson-client'); const d3 = require('d3-geo');
const out = process.argv[2];
const land50 = topo.feature(JSON.parse(fs.readFileSync(require.resolve('world-atlas/land-50m.json'))), 'land');
const land110 = topo.feature(JSON.parse(fs.readFileSync(require.resolve('world-atlas/land-110m.json'))), 'land');
const W = 2245, H = 3179, BROWN = '#7a4b39';
// Wellenkante des Kopfbereichs
const wave = `M0 0 H${W} V430 C 1980 470, 1760 520, 1480 505 C 1150 488, 900 430, 600 455 C 360 475, 160 530, 0 510 Z`;
const proj = d3.geoEquirectangular().fitExtent([[-60, -40], [W + 60, 700]], { type: 'Sphere' });
const path = d3.geoPath(proj);
const bg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}">
<rect width="${W}" height="${H}" fill="${BROWN}"/>
<defs><clipPath id="hc"><path d="${wave}"/></clipPath></defs>
<path d="${wave}" fill="#ffffff"/>
<g clip-path="url(#hc)"><path d="${path(land110)}" fill="#ece6dd"/></g>
<path d="${wave.replace(/ Z$/, '').replace(`M0 0 H${W} V430`, `M${W} 430`)}" fill="none" stroke="#e8c98f" stroke-width="6"/>
</svg>`;
fs.writeFileSync(out + '/hintergrund.svg', bg);
// Globus, zentriert auf Manila
const G = 620, R = 230, cx = 280, cy = 300;
const o = d3.geoOrthographic().rotate([-121, -12, -18]).translate([cx, cy]).scale(R).clipAngle(90);
const gp = d3.geoPath(o);
const grat = d3.geoGraticule10();
const [mx, my] = o([120.98, 14.6]);
const globe = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${G} 670">
<path d="M ${cx + 40} ${cy - R - 34} A ${R + 40} ${R + 40} 0 0 1 ${cx + 40} ${cy + R + 46}" fill="none" stroke="#5a3426" stroke-width="16" stroke-linecap="round" transform="rotate(-18 ${cx} ${cy})"/>
<path d="${gp({ type: 'Sphere' })}" fill="#f3dcae"/>
<path d="${gp(grat)}" fill="none" stroke="#dcb978" stroke-width="2"/>
<path d="${gp(land50)}" fill="#a8693f" stroke="#8c5431" stroke-width="1.5"/>
<path d="${gp({ type: 'Sphere' })}" fill="none" stroke="#5a3426" stroke-width="7"/>
<circle cx="${mx}" cy="${my}" r="13" fill="#fff6e4" stroke="#5a3426" stroke-width="5"/>
<rect x="${cx - 14}" y="${cy + R + 40}" width="28" height="60" fill="#5a3426" stroke="#f3dcae" stroke-width="4"/>
<path d="M ${cx - 120} 660 Q ${cx} 590 ${cx + 120} 660 Z" fill="#5a3426" stroke="#f3dcae" stroke-width="4"/>
</svg>`;
fs.writeFileSync(out + '/globus.svg', globe);
console.log('ok', Math.round(mx), Math.round(my));
