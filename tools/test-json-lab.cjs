const fs=require('fs'), path=require('path'), vm=require('vm'), assert=require('assert/strict');
const dir=path.resolve(__dirname,'../05-EXEMPLES-CODE/mini-site-json-seance-19-v1-a-valider');
const results=[];
class El {
 constructor(){this.children=[];this.attrs={};this.dataset={};this.listeners={};this.value='';this.textContent='';this.disabled=false;this.hidden=false;this.files=[];this.classList={toggle(){},remove(){}};}
 append(...n){this.children.push(...n)} replaceChildren(...n){this.children=n}
 setAttribute(k,v){this.attrs[k]=v} getAttribute(k){return this.attrs[k]}
 addEventListener(k,f){this.listeners[k]=f} focus(){this.focused=true} click(){this.clicked=true;return this.listeners.click?.()}
}
function setup(protocol='http:') {
 const nodes=new Map(), get=s=>{if(!nodes.has(s))nodes.set(s,new El());return nodes.get(s)};
 let data=JSON.parse(fs.readFileSync(path.join(dir,'data/projets.json'),'utf8')), waitResponse=null, fetchCount=0;
 const state={httpError:false,invalid:false,network:false,clipboardFail:false,download:false,copied:null,selected:false};
 const context=vm.createContext({document:{querySelector:get,createElement:()=>new El(),createDocumentFragment:()=>new El(),createRange:()=>({selectNodeContents(){state.selected=true}})},
 window:{getSelection:()=>({removeAllRanges(){},addRange(){}})},location:{protocol},
 navigator:{clipboard:{async writeText(text){if(state.clipboardFail)throw Error();state.copied=text}}},
 URL:{createObjectURL(){state.download=true;return 'blob:test'},revokeObjectURL(){}},Blob,AbortController,structuredClone,
 setTimeout:(fn,ms)=>setTimeout(fn,ms===1500?10:ms===1000?1:ms),clearTimeout,
 fetch:async(url,opts)=>{fetchCount++;if(waitResponse)await waitResponse;if(state.network)throw Error('Réseau indisponible');return {ok:!state.httpError&&!url.includes('manquant'),status:404,json:async()=>{if(state.invalid)throw SyntaxError();return structuredClone(data)}};}});
 vm.runInContext(fs.readFileSync(path.join(dir,'js/demo-data.js'),'utf8'),context);
 vm.runInContext(fs.readFileSync(path.join(dir,'js/app.js'),'utf8'),context);
 return {get,state,run:s=>vm.runInContext(s,context),setData:d=>data=d,setWait:p=>waitResponse=p,count:()=>fetchCount,context};
}
async function check(name,f){await f();results.push({test:name,status:'réussi'})}
const tick=()=>new Promise(r=>setImmediate(r));
(async()=>{
 const a=setup();await tick();
 await check('succès HTTP : trois cartes',async()=>{assert.equal(a.get('#projects').children.length,3);assert.equal(a.get('#status').dataset.state,'success')});
 await check('recherche sans accents et casse',async()=>{a.get('#search').value=' COMPETENCES ';a.get('#search').listeners.input();assert.equal(a.get('#projects').children.length,1)});
 await check('recherche sans résultat',async()=>{a.get('#search').value='absent';a.get('#search').listeners.input();assert.match(a.get('#status').textContent,/Aucun résultat/)});
 await check('effacer filtres et focus',async()=>{a.get('#clear-search').click();assert.equal(a.get('#projects').children.length,3);assert(a.get('#search').focused)});
 await check('filtre catégorie',async()=>{a.get('#category').value='Formation';a.get('#category').listeners.change();assert.equal(a.get('#projects').children.length,1)});
 await check('recharger efface filtres et relit la source',async()=>{const n=a.count();await a.get('#reload-button').click();assert(a.count()>n);assert.equal(a.get('#category').value,'');assert.equal(a.get('#projects').children.length,3)});
 for(const [scenario,expected] of [['empty','empty'],['http','error'],['invalid','error'],['schema','error'],['slow','success']]){
  await check('scénario '+scenario,async()=>{a.get('#scenario').value=scenario;const task=a.get('#run-scenario').click();assert.equal(a.get('#status').dataset.state,'loading');await task;assert.equal(a.get('#status').dataset.state,expected);assert.equal(a.get('#projects').getAttribute('aria-busy'),'false')});
 }
 await check('rétablir après erreur',async()=>{await a.get('#restore-button').click();assert.equal(a.get('#projects').children.length,3)});
 await check('erreur réseau puis réessayer',async()=>{a.state.network=true;await a.run('loadProjects()');assert.equal(a.get('#retry-button').hidden,false);a.state.network=false;await a.get('#retry-button').click();assert.equal(a.get('#projects').children.length,3)});
 await check('JSON HTTP invalide',async()=>{a.state.invalid=true;await a.run('loadProjects()');assert.match(a.get('#status').textContent,/JSON invalide/);a.state.invalid=false});
 await check('import valide et export',async()=>{const input=a.get('#import-json');input.files=[{name:'test.json',size:20,text:async()=>JSON.stringify([{title:'Essai',category:'Test',description:'Import'}])}];await input.listeners.change({target:input});assert.equal(a.get('#projects').children.length,1);a.get('#download-json').click();assert(a.state.download)});
 await check('copie presse-papiers',async()=>{await a.get('#copy-json').click();assert.match(a.state.copied,/Essai/)});
 await check('copie de secours sans permission',async()=>{a.state.clipboardFail=true;await a.get('#copy-json').click();assert(a.state.selected);assert.match(a.get('#copy-status').textContent,/Ctrl\+C/)});
 await check('import invalide et export désactivé',async()=>{const input=a.get('#import-json');input.files=[{name:'bad.json',size:2,text:async()=>'{}'}];await input.listeners.change({target:input});assert.equal(a.get('#status').dataset.state,'error');assert.equal(a.get('#download-json').disabled,true)});
 await check('import trop volumineux',async()=>{const input=a.get('#import-json');input.files=[{name:'large.json',size:2000000}];await input.listeners.change({target:input});assert.match(a.get('#status').textContent,/1 Mo/)});
 await check('résultat ancien ignoré après deux recharges',async()=>{let release;a.setWait(new Promise(r=>release=r));const old=a.run('loadProjects()');a.setWait(null);a.setData([{title:'Récent',category:'Test',description:'Nouvelle version'}]);await a.run('loadProjects()');release();await old;assert.match(a.get('#json-preview').textContent,/Récent/);assert.equal(a.get('#projects').getAttribute('aria-busy'),'false')});
 await check('mode file sans fetch et recharge opérationnelle',async()=>{const b=setup('file:');await tick();await b.get('#reload-button').click();assert.equal(b.count(),0);assert.equal(b.get('#projects').children.length,3);assert.match(b.get('#environment').textContent,/Mode fichier/)});
 // Commandes de la page PWA, exécutées depuis son script réel.
 const pwa=fs.readFileSync(path.join(dir,'preparation-pwa.html'),'utf8');const b=setup();await tick();
 const steps=Array.from({length:5},()=>new El()), resources=Array.from({length:3},(_,i)=>{const e=new El();e.dataset.resource=['index.html','css/styles.css','data/projets.json'][i];return e});
 b.context.document.querySelectorAll=s=>s.includes('swFlow')?steps:resources;
 vm.runInContext(pwa.match(/<script>([\s\S]*?)<\/script>/)[1],b.context);
 await check('PWA : lire manifeste',async()=>{b.get('#manifestBtn').click();assert.match(b.get('#manifestOutput').textContent,/start_url/)});
 await check('PWA : étapes et recommencer',async()=>{b.get('#nextStep').click();assert.match(b.get('#flowOutput').textContent,/enregistrement/);b.get('#resetFlow').click();assert.match(b.get('#flowOutput').textContent,/Aucun service worker/)});
 await check('PWA : ajouter ressources sans doublon et vider',async()=>{resources.forEach(e=>{e.click();e.click()});assert.equal(b.get('#cacheBox').children.length,3);b.get('#clearCache').click();assert.equal(b.get('#cacheBox').children.length,1)});
 await check('PWA : choix de contexte',async()=>{for(const value of ['https','localhost','http','']){b.get('#contextSelect').listeners.change({target:{value}});assert(b.get('#contextOutput').textContent.length>5)}});
 await check('PWA : prévisualiser liste',async()=>{b.get('#essential').value='index.html';b.get('#previewList').click();assert.match(b.get('#listOutput').textContent,/index.html/)});
 fs.writeFileSync(path.join(dir,'resultats-tests.json'),JSON.stringify({method:'Scripts réels, DOM simulé Node ; pas de recette visuelle navigateur',results},null,2));
 console.log(results.length+' contrôles réussis');
})().catch(e=>{console.error(e);process.exitCode=1});
