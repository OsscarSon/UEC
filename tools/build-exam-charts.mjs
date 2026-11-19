import {build} from 'esbuild';import fs from 'node:fs';
fs.mkdirSync('vendor/echarts',{recursive:true});
const r=await build({entryPoints:['tools-src/exam-charts.js'],outfile:'vendor/echarts/exam-charts.js',bundle:true,minify:true,format:'iife',globalName:'UECCharts',target:['es2020'],metafile:true,legalComments:'linked'});
for(const n of ['LICENSE','NOTICE'])fs.copyFileSync('node_modules/echarts/'+n,'vendor/echarts/'+n);
fs.copyFileSync('node_modules/zrender/LICENSE','vendor/echarts/ZRENDER_LICENSE');
fs.writeFileSync('vendor/echarts/BUILD.json',JSON.stringify({version:JSON.parse(fs.readFileSync('node_modules/echarts/package.json')).version,license:'Apache-2.0',upstream:'https://github.com/apache/echarts',entry:'tools-src/exam-charts.js',modules:['HeatmapChart','BarChart','GridComponent','TooltipComponent','VisualMapComponent','LegendComponent','AriaComponent','GraphicComponent','CanvasRenderer'],inputs:Object.keys(r.metafile.inputs),bytes:fs.statSync('vendor/echarts/exam-charts.js').size},null,2)+'\n');
console.log('Built tree-shaken ECharts heatmap/bar module');
