'use strict';
const $=id=>document.getElementById(id), C=window.LNIA;
const key='lnia-messages-workspace-v1', groupKey='lnia-whatsapp-group';
const read=k=>{try{return localStorage.getItem(k)}catch{return null}};
const save=(k,v)=>{try{localStorage.setItem(k,v);return true}catch{return false}};
const status=t=>{$('status').textContent=t};
const fresh=()=>({schema:'lnia-messages',version:1,fields:{...C.defaults},models:{...C.models},message:window.LNIA_S18,versions:[]});
let state=fresh();
try{const stored=read(key);if(stored)state=C.validateWorkspace(JSON.parse(stored));else if(read('lnia-whatsapp-draft')!==null)state.message=read('lnia-whatsapp-draft')}catch{status('La sauvegarde du navigateur est illisible. Vous pouvez reprendre un export JSON.')}
const labels={seance:'Séance',titre:'Titre',cycle:'Parcours / module',date:'Date',horaire:'Horaire et fuseau',objectif:'Objectif concret',preparation:'À préparer',acces:'Lien de connexion',supports:'Lien des supports',replay:'Lien du replay',signature:'Signature'};
for(const [name,label]of Object.entries(labels)){
 const wrap=document.createElement('label');wrap.textContent=label;
 const input=document.createElement(['objectif','preparation','signature'].includes(name)?'textarea':'input');
 input.id='f-'+name;if(input.tagName==='INPUT')input.type=name==='date'?'date':['acces','supports','replay'].includes(name)?'url':'text';
 if(name==='horaire')input.placeholder='Ex. 20 h · Casablanca';
 input.oninput=()=>{state.fields[name]=input.value;persist();$('preview-title').textContent=state.fields.seance+' · '+state.fields.titre};wrap.append(input);$('fields').append(wrap);
}
function persist(){const ok=save(key,JSON.stringify(state));$('storage').textContent=ok?'Brouillon mémorisé sur ce navigateur':'Stockage indisponible : exportez votre espace JSON.'}
function linkNode(url){const a=document.createElement('a');a.href=url;a.textContent=url;a.target='_blank';a.rel='noopener noreferrer';return a}
function preview(){
 const text=state.message,box=$('preview');box.replaceChildren();
 for(const part of text.split(/(https?:\/\/[^\s<>]+|\*[^*\n]+\*|_[^_\n]+_|~[^~\n]+~)/g)){
  if(/^https?:/.test(part))box.append(linkNode(part));
  else if(/^([*_~]).+\1$/.test(part)){const n=document.createElement({'*':'strong','_':'em','~':'s'}[part[0]]);n.textContent=part.slice(1,-1);box.append(n)}
  else box.append(document.createTextNode(part));
 }
 const words=text.trim()?text.trim().split(/\s+/).length:0;
 $('count').textContent=`${text.length} caractères · ${words} mots · lecture estimée : ${Math.max(1,Math.ceil(words/200))} min`;
 const checks=[[!!text.trim(),'Message renseigné','Le message est vide.'],[!(/\[[^\]]+\]|\{[a-z]+\}/i.test(text)),'Aucun champ de modèle restant','Des champs restent à compléter.'],[!(/à communiquer|à compléter/i.test(text)),'Aucune modalité annoncée comme manquante','Une date, un horaire ou un accès reste peut-être à préciser.'],[!(/\]\(https?:|^#{1,6}\s|\*\*[^*]+\*\*/m.test(text)),'Format adapté à WhatsApp','Du Markdown reste à adapter.']];
 $('checks').replaceChildren(...checks.map(([ok,yes,no])=>{const li=document.createElement('li');li.className=ok?'':'warn';li.textContent=(ok?'✓ ':'À relire · ')+(ok?yes:no);return li}));
 $('links').replaceChildren(...C.links(text).map(url=>{const li=document.createElement('li');li.append(linkNode(url));return li}));
 if(!C.links(text).length){const li=document.createElement('li');li.textContent='Aucun lien dans ce message.';$('links').append(li)}
}
function versions(){
 $('versions').replaceChildren();
 [...state.versions].reverse().forEach((v,i)=>{const btn=document.createElement('button');btn.className='secondary';btn.textContent=`Version ${state.versions.length-i} · ${v.date} · ${v.text.length} caractères`;btn.onclick=()=>replace(v.text);$('versions').append(btn)});
}
function paint(){for(const k in labels)$('f-'+k).value=state.fields[k];$('message').value=state.message;$('model').value=state.models[$('template').value];$('preview-title').textContent=state.fields.seance+' · '+state.fields.titre;preview();versions();persist()}
function replace(text){if(state.message.trim()&&state.message!==text&&!confirm('Remplacer le texte actuel ? Vous pouvez d’abord conserver une version.'))return false;state.message=text;$('message').value=text;preview();persist();return true}
function filename(ext){return 'message-'+(state.fields.seance||'atelier').replace(/[^a-z0-9-]/gi,'-')+'.'+ext}
function download(name,text,type){const url=URL.createObjectURL(new Blob([text],{type})),a=document.createElement('a');a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000)}
async function importFile(input,handler){const file=input.files[0];if(!file)return;try{if(file.size>2000000)throw Error('Fichier trop volumineux (maximum 2 Mo).');handler(await file.text());}catch(e){status('Import impossible : '+e.message)}finally{input.value=''}}
$('message').oninput=()=>{state.message=$('message').value;preview();persist()};
$('template').onchange=()=>{$('model').value=state.models[$('template').value]};
$('model').oninput=()=>{state.models[$('template').value]=$('model').value;persist()};
$('model-reset').onclick=()=>{if(confirm('Restaurer le modèle sélectionné ?')){state.models[$('template').value]=C.models[$('template').value];$('model').value=state.models[$('template').value];persist()}};
$('generate').onclick=()=>{if(replace(C.generate(state.models[$('template').value],state.fields)))status('Message généré. Relisez les modalités et les liens.')};
$('load-s18').onclick=()=>{if(replace(window.LNIA_S18))status('Annonce S18 chargée. Les paramètres d’atelier restent inchangés.')};
$('normalize').onclick=()=>{if(replace(C.normalize(state.message)))status('Titres, gras et liens Markdown adaptés. Relisez le résultat.')};
$('import').onchange=()=>importFile($('import'),text=>{if(replace(C.normalize(text)))status('Texte importé.')});
$('snapshot').onclick=()=>{if(!state.message.trim())return status('Rédigez un message avant de conserver une version.');state.versions.push({text:state.message,date:new Date().toLocaleString('fr-FR',{timeZone:'Africa/Casablanca'})});state.versions=state.versions.slice(-20);versions();persist();status('Version conservée. Les 20 dernières versions sont gardées dans l’espace.')};
$('workspace-export').onclick=()=>{download('espace-'+filename('json'),JSON.stringify(state,null,2),'application/json;charset=utf-8');status('Export demandé. Le lien privé du groupe est exclu ; relisez les données présentes dans votre texte avant de partager le fichier.')};
$('workspace-import').onchange=()=>importFile($('workspace-import'),text=>{const next=C.validateWorkspace(JSON.parse(text));if(confirm('Remplacer les paramètres, modèles, texte et versions par cet espace ?')){state=next;paint();status('Espace repris.')}});
$('new').onclick=()=>{if(confirm('Créer un atelier vierge ? Sauvegardez l’espace actuel si vous souhaitez le conserver.')){const next=fresh();next.models={...state.models};for(const k in next.fields)next.fields[k]=['cycle','signature'].includes(k)?state.fields[k]:'';next.message='';state=next;paint();status('Nouvel atelier créé ; modèles, parcours et signature conservés.')}};
$('export').onclick=()=>{if(!state.message.trim())return status('Le message est vide.');download(filename('txt'),state.message,'text/plain;charset=utf-8');status('Export du texte demandé.')};
$('copy').onclick=async()=>{if(!state.message.trim())return status('Le message est vide.');if(/\[[^\]]+\]|\{[a-z]+\}/i.test(state.message))return status('Complétez les champs restants avant la copie.');try{await navigator.clipboard.writeText(state.message);status('Message copié. Vérifiez le groupe avant de coller dans WhatsApp.')}catch{$('message').focus();$('message').select();status('Utilisez Ctrl+C pour copier le texte sélectionné.')}};
$('clear').onclick=()=>{if(confirm('Vider le message ? Les versions conservées restent disponibles.')){state.message='';paint()}};
document.querySelectorAll('[data-wrap]').forEach(btn=>btn.onclick=()=>{const t=$('message'),start=t.selectionStart,end=t.selectionEnd;if(start===end)return status('Sélectionnez le texte à mettre en forme.');t.setRangeText(btn.dataset.wrap+t.value.slice(start,end)+btn.dataset.wrap,start,end,'select');state.message=t.value;preview();persist();t.focus()});
$('print').onclick=()=>window.print();
$('group').value=read(groupKey)||'';
$('remember').onclick=()=>{const url=$('group').value.trim();if(!C.validGroup(url))return status('Renseignez un lien d’invitation HTTPS valide.');status(save(groupKey,url)?'Lien du groupe mémorisé.':'Stockage indisponible.')};
$('forget').onclick=()=>{$('group').value='';save(groupKey,'');status('Lien du groupe oublié.')};
$('config').onchange=()=>importFile($('config'),text=>{const config=JSON.parse(text);if(!C.validGroup(config.groupUrl))throw Error('Lien du groupe invalide.');$('group').value=config.groupUrl;status('Configuration privée chargée. Mémorisez-la si nécessaire.')});
$('open').onclick=()=>{const url=$('group').value.trim();if(!C.validGroup(url))return status('Renseignez le lien du groupe ou chargez la configuration privée.');window.open(url,'_blank','noopener,noreferrer');status('Ouverture du groupe demandée. Vérifiez sa destination avant tout envoi.')};
paint();
