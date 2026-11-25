"use strict";
const config=JSON.parse(document.querySelector('#module-config').textContent);
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
if(document.body.dataset.view==='hub'){
 $('#resource-search').addEventListener('input',ev=>{const plain=s=>s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase().trim(),term=plain(ev.target.value);let count=0;$$('.resource').forEach(a=>{a.hidden=!plain(a.textContent).includes(term);if(!a.hidden)count++});$('#resource-count').textContent=count+' ressource(s) affichée(s).'});
}else{
 const keys=['project','input','task','expected','observed','cause','correction','secondTest','limits','next','reader','date','browser','pilot','reviewDate','review','status'];
 const KEY='lnia-module05-parcours-s17-s20-v1';
 const blank=()=>({schema:'lnia-module05-parcours',version:1,current:'S17',sessions:Object.fromEntries(config.sessions.map(s=>[s.id,{status:'À COMPLÉTER'}]))});
 const validStatuses=['À COMPLÉTER','À REVOIR','À VALIDER','VALIDÉ'];
 let state=blank(),storage=true;
 const session=()=>config.sessions.find(s=>s.id===state.current);
 function required(f,id=state.current){return ['project','input','task','expected','observed','reader','date','pilot','reviewDate','review',...(id==='S20'?['correction','secondTest']:[])].filter(k=>!f[k]?.trim());}
 function normalize(input){
  if(input?.schema!=='lnia-module05-parcours'||input.version!==1)throw Error('Carnet Module 05 attendu. Les carnets propres aux ateliers utilisent un autre format.');
  const out=blank();if(config.sessions.some(s=>s.id===input.current))out.current=input.current;
  for(const s of config.sessions)for(const k of keys)if(typeof input.sessions?.[s.id]?.[k]==='string')out.sessions[s.id][k]=input.sessions[s.id][k].slice(0,20000);
  for(const s of config.sessions){const f=out.sessions[s.id];if(!validStatuses.includes(f.status))f.status='À COMPLÉTER';if(f.status==='VALIDÉ'&&required(f,s.id).length)f.status='À VALIDER'}return out;
 }
 try{const saved=localStorage.getItem(KEY);if(saved)state=normalize(JSON.parse(saved))}catch{storage=false}
 function notify(t,error=false){$('#save-status').textContent=t;$('#save-status').classList.toggle('error',error)}
 function save(){try{localStorage.setItem(KEY,JSON.stringify(state));storage=true;notify('Carnet enregistré sur ce navigateur. Exportez le JSON pour le conserver ailleurs.')}catch{storage=false;notify('Stockage indisponible : exportez votre carnet JSON.',true)}}
 function proof(id){const s=config.sessions.find(s=>s.id===id),f=state.sessions[id],v=k=>f[k]?.trim()||'À COMPLÉTER';return '# Preuve '+id+' — '+s.title+'\n\nDate prévue : '+s.dateLabel+'\nStatut : '+v('status')+'\n\n'+keys.filter(k=>k!=='status').map(k=>'## '+config.labels[k]+'\n\n'+v(k)+'\n').join('\n')+'\nProduction conseillée : '+s.production+'\n\nLes résultats attendus et observés restent distincts. Exporter ne remplace aucun fichier existant automatiquement.\n';}
 function preview(){$('#proof-preview').textContent=proof(state.current);const f=state.sessions[state.current];$('#review-status').textContent=f.status==='VALIDÉ'?'Revue renseignée ; décision à assumer par le pilote.':'La revue et les résultats réels restent à renseigner. La présence des modèles ne vaut pas validation.';}
 function populate(){const s=session(),f=state.sessions[state.current];$('#session-title').textContent=s.id+' · '+s.title;$('#session-context').textContent=s.dateLabel+' · '+s.duration+' minutes · '+s.goal;$('#session-input').textContent=s.entry;$('#session-output').textContent=s.production;$('#session-next').textContent=s.next;$('#session-prompt').href='../'+s.prompt;$('#session-example').href='../'+s.example;for(const k of keys)$('#f-'+k).value=f[k]||'';$$('[data-session]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.session===s.id)));preview();}
 function download(name,content,type='text/markdown;charset=utf-8'){const url=URL.createObjectURL(new Blob([content],{type})),a=document.createElement('a');a.href=url;a.download=name;document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);notify('Téléchargement préparé : '+name+'. Rangez-le dans votre copie du dossier.');}
 $$('[data-session]').forEach(b=>b.onclick=()=>{state.current=b.dataset.session;save();populate()});
 $('#evidence-form').addEventListener('input',ev=>{const k=ev.target.name;if(!keys.includes(k))return;const f=state.sessions[state.current];f[k]=ev.target.value;if(k!=='status'&&f.status==='VALIDÉ'){f.status='À REVOIR';$('#f-status').value='À REVOIR'}save();preview();});
 $('#f-status').addEventListener('change',ev=>{const f=state.sessions[state.current];f.status=ev.target.value;const missing=required(f);if(f.status==='VALIDÉ'&&missing.length){f.status='À VALIDER';ev.target.value=f.status;save();notify('Validation incomplète : '+missing.map(k=>config.labels[k]).join(', '),true)}else save();preview()});
 $('#evidence-form').onsubmit=ev=>ev.preventDefault();
 $('#export-proof').onclick=()=>download(session().proofName,proof(state.current));
 $('#export-module').onclick=()=>download('bilan-parcours-module05.md','# Mon parcours Module 05\n\n'+config.sessions.map(s=>proof(s.id)).join('\n---\n\n'));
 $('#export-json').onclick=()=>download('carnet-module05-S17-S20.json',JSON.stringify(state,null,2),'application/json;charset=utf-8');
 $('#import-json').onchange=async ev=>{const file=ev.target.files[0];if(!file)return;try{if(file.size>2000000)throw Error('Fichier trop volumineux (2 Mo maximum).');const next=normalize(JSON.parse(await file.text()));if(confirm('Remplacer le carnet Module 05 courant ? Exportez d’abord votre JSON pour conserver les saisies actuelles.')){state=next;save();populate()}}catch(error){notify('Import impossible : '+error.message,true)}finally{ev.target.value=''}};
 $('#print-carnet').onclick=()=>window.print();
 let printDetails=[];
 window.addEventListener('beforeprint',()=>{printDetails=$$('details').map(d=>[d,d.open]);printDetails.forEach(([d])=>d.open=true)});
 window.addEventListener('afterprint',()=>printDetails.forEach(([d,open])=>d.open=open));
 $('#reset-session').onclick=()=>{if(confirm('Vider uniquement les saisies de '+state.current+' ? Les trois autres séances et les fichiers sur disque seront conservés.')){state.sessions[state.current]={status:'À COMPLÉTER'};save();populate()}};
 populate();if(!storage)notify('Stockage indisponible ou carnet illisible : exportez une copie JSON.',true);
}
