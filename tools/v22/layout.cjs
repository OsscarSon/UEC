const fs=require('fs'),{chromium}=require('playwright');
(async()=>{
 const a=JSON.parse(fs.readFileSync('reports/v22/ASSET_REVIEW.json'));
 const b=await chromium.launch({headless:true,executablePath:'/usr/bin/chromium',args:['--no-sandbox']});const p=await b.newPage();
 const report=[];
 for(const x of a.filter(x=>x.reviewed_path)){
  await p.setContent(fs.readFileSync(x.reviewed_path,'utf8'));await p.evaluate(()=>document.fonts.ready);
  const issues=await p.evaluate(()=>{
   const root=document.querySelector('svg'),v=root.viewBox.baseVal;
   return [...root.querySelectorAll('text')].map((e,i)=>{
    const z=e.getBBox(),m=root.getScreenCTM().inverse().multiply(e.getScreenCTM()),q=[[z.x,z.y],[z.x+z.width,z.y],[z.x,z.y+z.height],[z.x+z.width,z.y+z.height]].map(([x,y])=>new DOMPoint(x,y).matrixTransform(m)),xs=q.map(p=>p.x),ys=q.map(p=>p.y);return {i,text:e.textContent,x:Math.min(...xs),y:Math.min(...ys),w:Math.max(...xs)-Math.min(...xs),h:Math.max(...ys)-Math.min(...ys),limit:v.width};
   }).filter(z=>z.x<-.5||z.y<-.5||z.x+z.w>v.width+0.5||z.y+z.h>v.height+0.5);
  });
  report.push({code:x.code,issues});
 }
 fs.writeFileSync('reports/v22/TEXT_BOUNDS.json',JSON.stringify(report,null,2)+'\n');
 const bad=report.filter(x=>x.issues.length);await b.close();
 if(bad.length)throw new Error(JSON.stringify(bad));
 console.log(`PASS ${report.length} reviewed SVG text bounds (including transformed text)`);
})();
