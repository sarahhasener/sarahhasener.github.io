const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch();
const items=[['ncr_karte.svg','karte_ncr_carina_v3.png',1600,1900,2.5,'#fbf5ea'],['wirkung.svg','wirkungsgefuege_v3.png',1810,1700,2,'#fbf5ea'],['abb_bevoelkerung_A1.svg','diagramm_bevoelkerung_v3.png',1474,850,2.5,'#fbf5ea'],['locator.svg','lagekarte_suedostasien_v3.png',1000,1050,3,'#fbf5ea'],['hintergrund.svg','hintergrund_v3.png',2245,3179,2,'transparent'],['globus.svg','globus_v3.png',620,670,2,'transparent']];
for (const [f,o,w,h,sc,bg] of items){fs.writeFileSync('w.html',`<html><body style="margin:0;background:${bg}"><img src="${f}" style="width:${w}px;height:${h}px;display:block"></body></html>`);
const p=await b.newPage({viewport:{width:w,height:h},deviceScaleFactor:sc});await p.goto('file://'+process.cwd()+'/w.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
await p.screenshot({path:o,clip:{x:0,y:0,width:w,height:h},omitBackground:bg==='transparent'});await p.close();}
await b.close();})()
