// Tests de branches réelles dans un DOM simulé, sans prétendre à une recette visuelle.
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert/strict');
const root = path.resolve(__dirname, '../pack-documentaire-seance-19-v3-valide');
const results = [];
class Element {
  constructor() { this.children=[]; this.attrs={}; this.textContent=''; this.value=''; this.hidden=false; this.listeners={}; this.classList={toggle(){}}; }
  append(...nodes){this.children.push(...nodes)}
  replaceChildren(...nodes){this.children=nodes}
  setAttribute(k,v){this.attrs[k]=v}
  getAttribute(k){return this.attrs[k]}
  addEventListener(k,v){this.listeners[k]=v}
}
async function test(folder, enriched) {
  const nodes = new Map();
  const get = s => {if(!nodes.has(s))nodes.set(s,new Element());return nodes.get(s)};
  const data=JSON.parse(fs.readFileSync(path.join(root,'mini-sites',folder,'data/projets.json'),'utf8'));
  let responseData = data;
  let failHttp = false;
  let failNetwork = false;
  let failParse = false;
  let pending;
  const context=vm.createContext({
    document:{querySelector:get,createElement:()=>new Element(),createDocumentFragment:()=>new Element()},
    console:{error(){}},navigator:{onLine:true},window:{location:{href:'http://localhost:8080/'},addEventListener(){}},
    URL,structuredClone,
    fetch: async url=>{
      if(pending)await pending;
      if(failNetwork)throw Error('Network failed');
      return {ok:!failHttp && !url.includes('manquant'),status:404,statusText:'Not Found',json:async()=>{if(failParse)throw SyntaxError('JSON invalide');return structuredClone(responseData)}};
    }
  });
  vm.runInContext(fs.readFileSync(path.join(root,'mini-sites',folder,'js/app.js'),'utf8'), context);
  const load=enriched?'loadResources()':'loadProjects()';
  const grid=get(enriched?'#resources-grid':'#projects');
  const wait=()=>new Promise(r=>setImmediate(r));
  await wait();
  async function check(name,fn){await fn();results.push({site:folder,test:name,status:'réussi'})}
  await check('succès',async()=>{await vm.runInContext(load,context);assert.match(get('#status').textContent,/succès|affichée/);assert(grid.children.length>0)});
  await check('chargement observable',async()=>{let release;pending=new Promise(r=>release=r);const running=vm.runInContext(load,context);assert.match(get('#status').textContent,/Chargement/);assert.equal(grid.attrs['aria-busy'],'true');release();await running;pending=null});
  await check('tableau vide',async()=>{responseData=[];await vm.runInContext(load,context);assert.match(get('#status').textContent,/Aucun/);assert.equal(grid.children.length,0)});
  await check('erreur HTTP',async()=>{responseData=data;failHttp=true;await vm.runInContext(load,context);assert.match(get('#status').textContent,/Impossible|HTTP/);assert.equal(grid.children.length,0);failHttp=false});
  await check('erreur réseau',async()=>{failNetwork=true;await vm.runInContext(load,context);assert.match(get('#status').textContent,/Impossible|Network/);failNetwork=false});
  await check('JSON invalide',async()=>{failParse=true;await vm.runInContext(load,context);assert.match(get('#status').textContent,/Impossible|JSON invalide/);failParse=false});
  await check('racine non tableau',async()=>{responseData={};await vm.runInContext(load,context);assert.match(get('#status').textContent,/Impossible|tableau/)});
  await check('champ absent',async()=>{responseData=structuredClone(data);delete responseData[0].title;await vm.runInContext(load,context);assert.match(get('#status').textContent,/Impossible|champ/);assert.equal(grid.children.length,0)});
  await check('champ vide',async()=>{responseData=structuredClone(data);responseData[0].title=' ';await vm.runInContext(load,context);assert.match(get('#status').textContent,/Impossible|champ/)});
  await check('retour au succès',async()=>{responseData=data;await vm.runInContext(load,context);assert.match(get('#status').textContent,/succès|affichée/);assert.equal(grid.attrs['aria-busy'],'false')});
  if(enriched){
    for(const scenario of ['empty','404','invalid-json','not-array','schema','dangerous','success']){
      await check('scénario '+scenario,async()=>{get('#scenario').value=scenario;await vm.runInContext('runScenario()',context);const msg=get('#status').textContent;assert.match(msg,scenario==='empty'?/Aucun/:scenario==='success'?/affichée/:/Erreur|JSON|tableau|champ|Protocole/)});
    }
    await check('flashcard ouverture/fermeture',async()=>{const button=get('#flashcards-grid').children[0].children[0];button.listeners.click();assert.equal(button.attrs['aria-expanded'],'true');button.listeners.click();assert.equal(button.attrs['aria-expanded'],'false')});
  }
}
(async()=>{
  await test('mini-site-json-seance-19-v1-a-valider',false);
  await test('mini-site-seance-19-V2',true);
  fs.writeFileSync(path.join(root,'resultats-tests-comportement.json'),JSON.stringify({method:'Node vm, DOM simulé ; aucun navigateur réel',results},null,2));
  console.log(`${results.length} tests comportementaux réussis`);
})().catch(error=>{console.error(error);process.exit(1)});
