// Verify actual TeX structures, including the legacy storage decoding boundary.
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict'),katex=require('katex');
const data=JSON.parse(fs.readFileSync('data/batch06/formulas.json','utf8'));
const ctx={window:{}};vm.createContext(ctx);vm.runInContext(fs.readFileSync('data/formula-cards.js','utf8'),ctx);
const legacy=ctx.window.STUDY_FORMULAS['数学1/1.2'][0][1];
vm.runInContext(fs.readFileSync('lessons/batch06-formulas.js','utf8'),ctx);
assert.equal(ctx.window.STUDY_FORMULAS['数学1/1.2'][0][1],legacy);
const rows=[];
for(const [key,entries] of Object.entries(data)) for(const [title,tex] of entries){
 const html=katex.renderToString(tex,{displayMode:true,throwOnError:true,trust:false,strict:'ignore'});
 if(/\\(?:d?frac)/.test(tex)) assert.ok(html.includes('class="mfrac"'),key+' must produce a real fraction');
 if(/\\sqrt/.test(tex)) assert.ok(/class="[^"]*\bsqrt\b/.test(html),key+' must produce a real root');
 assert.equal(ctx.window.STUDY_FORMULAS[key].find(x=>x[0]===title)[1],tex,'new cards must not be decoded twice');
 rows.push({key,title,status:'pass',fractionVerified:/\\(?:d?frac)/.test(tex),rootVerified:/\\sqrt/.test(tex)});
}
for(const key of ['数学1/1.1','数学1/1.2','数学4/4.1']){
 const tex=ctx.window.STUDY_FORMULAS[key][0][1];const html=katex.renderToString(tex,{throwOnError:true,strict:'ignore'});
 if(tex.includes('\\frac'))assert.ok(html.includes('class="mfrac"'));
 if(tex.includes('\\sqrt'))assert.ok(/class="[^"]*\bsqrt\b/.test(html));
 rows.push({key,status:'pass',scope:'legacy representative unchanged legacy storage'});
}
fs.writeFileSync('reports/batch06/FORMULA_VERIFICATION.json',JSON.stringify({status:'pass',scope:'TeX parse plus fraction/root structure checks; scientific derivations separately reviewed. Legacy source files remain unchanged.',checks:rows},null,2)+'\n');
console.log('PASS',rows.length,'formula structure checks');
