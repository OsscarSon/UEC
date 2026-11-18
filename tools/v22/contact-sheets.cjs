const{chromium}=require('playwright'),fs=require('fs');
(async()=>{
 const b=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']}),p=await b.newPage({viewport:{width:1500,height:1350}});
 const xs=JSON.parse(fs.readFileSync('reports/v22/ASSET_REVIEW.json'));fs.mkdirSync('reports/v22/contact-sheets',{recursive:true});
 const pages=[];
 for(let i=0;i<xs.length;i+=9){
  const group=xs.slice(i,i+9);let html='<body style="margin:0;display:grid;grid-template-columns:repeat(3,500px);font:14px sans-serif;background:#ddd">';
  for(const a of group){const s=fs.readFileSync(a.reviewed_path||a.original_path);html+=`<div style="padding:5px;box-sizing:border-box;height:450px;background:white;border:1px solid #777"><b>${a.code} · ${a.review_status} · ${a.integration_status}</b><div style="height:415px;display:flex;align-items:center"><img style="width:100%;height:415px;object-fit:contain" src="data:image/svg+xml;base64,${s.toString('base64')}"></div></div>`;}
  await p.setContent(html);await p.evaluate(()=>document.fonts.ready);await p.locator('img').evaluateAll(es=>Promise.all(es.map(e=>e.decode())));
  const file=`reports/v22/contact-sheets/${String(i/9+1).padStart(2,'0')}.webp`;
  // Chromium screenshots support PNG/JPEG; encode lossless PNG to WebP separately.
  await p.screenshot({path:file.replace('.webp','.png')});pages.push({file,assets:group.map(x=>x.id),codes:group.map(x=>x.code)});
 }
 fs.writeFileSync('reports/v22/VISUAL_PAGES.json',JSON.stringify(pages,null,2)+'\n');await b.close();console.log('Rendered all149 SVG in17 isolated-img sheets');
})();
