import {build} from 'esbuild';import fs from 'node:fs';
const result=await build({metafile:true,entryPoints:['tools-src/cloud-sync.js'],outdir:'vendor/cloud',bundle:true,format:'esm',splitting:true,minify:true,legalComments:'linked',target:'es2020'});
fs.writeFileSync('vendor/cloud/BUILD_INPUTS.json',JSON.stringify({sdk:'firebase13.4.0',inputs:Object.keys(result.metafile.inputs).sort()},null,2)+'\n');
fs.copyFileSync('cloud/FIREBASE_LICENSE','vendor/cloud/FIREBASE-LICENSE');
console.log('Built lazy Firebase Auth/Firestore client; configuration remains disabled.');
