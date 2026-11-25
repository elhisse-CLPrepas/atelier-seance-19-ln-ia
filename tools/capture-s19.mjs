// Captures d'une instance Chromium headless dédiée à la recette locale.
import fs from 'node:fs/promises';
const [port,base,out,mode='atelier']=process.argv.slice(2);
const tabs=await(await fetch(`http://127.0.0.1:${port}/json/list`)).json();
const ws=new WebSocket(tabs.find(t=>t.type==='page').webSocketDebuggerUrl);await new Promise(r=>ws.addEventListener('open',r,{once:true}));
let counter=0;const pending=new Map();ws.addEventListener('message',ev=>{const m=JSON.parse(ev.data);if(m.id){const p=pending.get(m.id);if(!p)return;pending.delete(m.id);m.error?p.reject(Error(JSON.stringify(m.error))):p.resolve(m.result)}});
const call=(method,params={})=>new Promise((resolve,reject)=>{const id=++counter;pending.set(id,{resolve,reject});ws.send(JSON.stringify({id,method,params}))});
const evaluate=async expression=>{const r=await call('Runtime.evaluate',{expression,awaitPromise:true,returnByValue:true});if(r.exceptionDetails)throw Error(JSON.stringify(r.exceptionDetails));return r.result.value};
await call('Page.enable');await call('Runtime.enable');
await call('Page.bringToFront');await call('Emulation.setFocusEmulationEnabled',{enabled:true});
const metrics=[];
const dossier=mode==='dossier';
const views=dossier?[['dossier-accueil',1440,'index.html'],['dossier-carnet',1440,'01-SUIVI/carnet-module05.html'],['dossier-mobile',390,'01-SUIVI/carnet-module05.html']]:[['accueil-desktop',1440,'accueil'],['demonstration-desktop',1440,'demonstration'],['atelier-mobile',390,'atelier']];
for(const [name,width,hash]of views){
 await call('Emulation.setDeviceMetricsOverride',{width,height:1100,deviceScaleFactor:1,mobile:width<500});
 await call('Emulation.setEmulatedMedia',{media:'screen'});
 await call('Page.navigate',{url:base+(dossier?'/public/dossier-challenge/'+hash:'/dist/index.html')});
 for(let n=0;n<100;n++){if(await evaluate(dossier?`!!document.querySelector('#resource-count') || !!document.querySelector('#session-title')?.textContent.startsWith('S17')`:`!!document.querySelector('#editor-status')?.textContent.includes('conformes')`))break;await new Promise(r=>setTimeout(r,50))}
 if(!dossier)await evaluate(`location.hash=${JSON.stringify(hash)}; true`);
 if(hash==='demonstration'){
  await evaluate(`document.querySelector('#lab-run').click();true`);
  for(let n=0;n<100;n++){if(await evaluate(`document.querySelector('#lab-cards').getAttribute('aria-busy')==='false'`))break;await new Promise(r=>setTimeout(r,50))}
 }
 await evaluate(`(async()=>{await document.fonts.ready;await new Promise(r=>setTimeout(r,300));window.scrollTo({top:0,behavior:'instant'});await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));return true})()`);
 metrics.push(await evaluate(`({page:${JSON.stringify(name)},width:innerWidth,scrollWidth:document.documentElement.scrollWidth,scrollY,header:getComputedStyle(document.querySelector('${dossier?'header':'.mast'}')).display,headerY:document.querySelector('${dossier?'header':'.mast'}').getBoundingClientRect().y})`));
 const shot=await call('Page.captureScreenshot',{format:'png',captureBeyondViewport:false,fromSurface:true});await fs.writeFile(out+'/'+name+'.png',Buffer.from(shot.data,'base64'));
}
// Clavier réel dans la page mobile : bouton natif + état aria.
if(!dossier)await evaluate(`location.hash='flashcards';true`);await new Promise(r=>setTimeout(r,100));
await evaluate(dossier?`document.querySelector('[data-session="S19"]').focus();true`:`document.querySelector('#flash-flip').focus();true`);
await call('Input.dispatchKeyEvent',{type:'keyDown',key:'Enter',code:'Enter',text:'\r',unmodifiedText:'\r',nativeVirtualKeyCode:13,windowsVirtualKeyCode:13});await call('Input.dispatchKeyEvent',{type:'keyUp',key:'Enter',code:'Enter',windowsVirtualKeyCode:13});
const keyboard=await evaluate(dossier?`document.querySelector('#session-title').textContent.startsWith('S19')`:`document.querySelector('#flash-flip').getAttribute('aria-expanded')==='true'`);
await fs.writeFile(out+'/layout-and-keyboard.json',JSON.stringify({metrics,...(dossier?{keyboardSessionButton:keyboard}:{keyboardFlashcard:keyboard})},null,2));
if(!keyboard)throw Error('Échec du contrôle clavier réel.');
ws.send(JSON.stringify({id:++counter,method:'Browser.close'}));ws.close();console.log('Captures ordinateur/mobile et clavier réel : réussis.');
