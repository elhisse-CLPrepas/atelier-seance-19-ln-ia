export const escapeHtml=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export const sections=[['accueil','Accueil','house'],['presentation','Présentation','play-circle'],['methode','Méthode','signpost-split'],['demonstration','Démonstration','layers'],['atelier','Atelier','pencil-square'],['prompts','Prompts','braces'],['flashcards','Flashcards','stack'],['quiz','Quiz','question-circle'],['validation','Validation','check2-square'],['portfolio','Portfolio','folder2-open'],['ressources','Ressources','book']];
export const observationFields=[['project','Projet ou cas étudié'],['file','Fichier / URL / version'],['environment','Mode réel : HTTP local ou exemple intégré'],['scenario','Scénario manipulé'],['expected','Résultat attendu avant l’essai'],['observed','Résultat réellement observé'],['cause','Cause expliquée et étape concernée'],['correction','Correction ou maintien motivé'],['reader','Binôme, date et navigateur'],['reopened','Résultat de réouverture des exports'],['next','Limites et prochain essai']];
export const reviewFields=[['pilot','Pilote'],['reviewDate','Date de revue'],['review','Observation et décision motivée']];
export const blankState=()=>({schema:'lnia-s19-mecanismes',version:2,fields:{status:'À COMPLÉTER'},checks:Array(7).fill(false),quiz:Array(8).fill(null),quizDone:false,known:[],cardOrder:Array.from({length:12},(_,i)=>i),card:0,json:'',contract:'simple',updatedAt:null});
export function validationMissing(s){return [...observationFields.slice(0,10),...reviewFields].filter(([k])=>!s.fields[k]?.trim()).map(([,label])=>label).concat(s.checks.every(Boolean)?[]:['sept critères observés']);}
export function normalizeState(input){
 if(input?.schema!=='lnia-s19-mecanismes'||input.version!==2)throw Error('Ce carnet n’appartient pas au parcours JSON S19. Votre ancien carnet d’assemblage reste conservé.');
 const s=blankState();for(const[k]of [...observationFields,...reviewFields,['status']])if(typeof input.fields?.[k]==='string')s.fields[k]=input.fields[k].slice(0,40000);
 if(!['À COMPLÉTER','À REVOIR','À VALIDER','VALIDÉ'].includes(s.fields.status))s.fields.status='À COMPLÉTER';
 s.checks=s.checks.map((_,i)=>input.checks?.[i]===true);s.quiz=s.quiz.map((_,i)=>Number.isInteger(input.quiz?.[i])&&input.quiz[i]>=0&&input.quiz[i]<3?input.quiz[i]:null);s.quizDone=input.quizDone===true;
 s.known=Array.isArray(input.known)?[...new Set(input.known.filter(i=>Number.isInteger(i)&&i>=0&&i<12))]:[];
 if(Array.isArray(input.cardOrder)&&input.cardOrder.length===12&&new Set(input.cardOrder).size===12&&input.cardOrder.every(i=>Number.isInteger(i)&&i>=0&&i<12))s.cardOrder=input.cardOrder;
 if(Number.isInteger(input.card)&&input.card>=0&&input.card<12)s.card=input.card;
 if(typeof input.json==='string')s.json=input.json.slice(0,1000000);s.contract=input.contract==='resource'?'resource':'simple';
 if(s.fields.status==='VALIDÉ'&&validationMissing(s).length)s.fields.status='À VALIDER';return s;
}
export function validateData(value,contract='simple',base='http://localhost:8080/'){
 if(!Array.isArray(value))throw Error('La réponse reçue n’est pas un tableau.');const ids=new Set();
 value.forEach((item,i)=>{
   if(!item||typeof item!=='object'||Array.isArray(item))throw Error(`Objet ${i+1} invalide.`);
   const keys=contract==='resource'?['id','title','category','level','description','activity','deliverable','question','answer']:['title','category','description'];
   for(const k of keys)if(typeof item[k]!=='string'||!item[k].trim())throw Error(`Objet ${i+1} : champ ${k} absent ou invalide (texte non vide attendu).`);
   if(contract==='resource'){
    if(!/^[a-z0-9-]+$/.test(item.id)||ids.has(item.id))throw Error(`Identifiant invalide ou dupliqué : ${item.id}.`);ids.add(item.id);
    if(!Array.isArray(item.objectives)||item.objectives.some(o=>typeof o!=='string'||!o.trim()))throw Error(`Objet ${i+1} : objectifs invalides.`);
   }
   if(item.link!==undefined&&item.link!==''){
    if(typeof item.link!=='string')throw Error(`Objet ${i+1} : lien non textuel.`);
    let url;try{url=new URL(item.link,base)}catch{throw Error(`Objet ${i+1} : lien invalide.`)}
    if(!['http:','https:'].includes(url.protocol))throw Error(`Protocole de lien refusé dans l’objet ${i+1}.`);
   }
 });return value;
}
const val=(s,k)=>s.fields[k]?.trim()||'À COMPLÉTER';
export function proofText(s,data){return '# Preuve S19 — JSON, HTTP et DOM\n\nSéance : 27 novembre 2026\nStatut : '+val(s,'status')+'\n\n'+observationFields.map(([k,l])=>'## '+l+'\n\n'+val(s,k)+'\n').join('\n')+'\n## Critères observés\n\n'+data.criteria.map((c,i)=>`- [${s.checks[i]?'x':' '}] ${c}`).join('\n')+'\n\n## Revue humaine\n\n'+reviewFields.map(([k,l])=>l+' : '+val(s,k)).join('\n')+'\n\nLe quiz ne remplace pas les observations et la décision du pilote.\n';}
export function relayText(s){return '# Relais S19 → S20\n\nFichiers et version : '+val(s,'file')+'\nEssai : '+val(s,'scenario')+'\nRésultat observé : '+val(s,'observed')+'\nCause : '+val(s,'cause')+'\nCorrection : '+val(s,'correction')+'\nEssai restant : '+val(s,'next')+'\nDécision : '+val(s,'status')+'\n\n## Reprise S20\n\nRouvrir V2 et la preuve. Vérifier les quatre états. Choisir les ressources publiques utiles sans réseau. Préparer manifeste, icônes, périmètre du service worker et cache versionné dans une copie. Prévoir les vrais essais hors connexion et de mise à jour ; ne pas les déclarer réussis avant observation.\n';}
export function indexText(s){return '# Entrée S19 à ajouter à mon index\n\n- Séance : 27 novembre 2026 · JSON local et préparation PWA.\n- Dossier : 04-WEB/mini-site-v2/\n- [Preuve S19](preuve-S19.md)\n- [Relais S20](relais-S20.md)\n- Statut : '+val(s,'status')+'\n\nConserver les preuves des séances précédentes.\n';}
export const resources=[
 ['Conserver et reprendre','Dossier commun S17–S20','HTML','dossier-challenge/index.html','Parcours, carnet transversal, exemples et portfolio alignés.'],
 ['Conserver et reprendre','Dossier commun complet S17–S20','ZIP','supports/mon-dossier-challenge-Module05-S17-S20.zip','Copie autonome avec les productions et modèles conservés.'],
 ['Projeter et animer','Projection HTML','HTML','projection-S19.html','22 vues et notes, issues de la même source.'],
 ['Projeter et animer','Présentation PDF','PDF','supports/presentation-S19.pdf','22 vues au format 16:9.'],
 ['Projeter et animer','PowerPoint éditable','PPTX','supports/presentation-S19.pptx','22 diapositives avec notes formateur.'],
 ['Projeter et animer','Conducteur 110 minutes','PDF','supports/conducteur-S19.pdf','Sept phases et relances.'],
 ['Projeter et animer','Notes formateur','MD','supports/notes-formateur-S19.md','Question, geste et explication par vue.'],
 ['Manipuler','Laboratoire S19 V2','HTML','laboratoire-json/index.html','Six ressources, cartes, flashcards et sept scénarios.'],
 ['Manipuler','Laboratoire V2 à emporter','ZIP','supports/laboratoire-json-S19.zip','Copie à servir sur le port 8080.'],
 ['Manipuler','Exemple JSON minimal','HTML','mini-sites/json-minimal/index.html','Trois objets, recherche et import local.'],
 ['Manipuler','Préparation PWA facultative','HTML','laboratoire-json/preparation-pwa.html','Simulations sans service worker actif.'],
 ['Manipuler','Données du laboratoire','JSON','laboratoire-json/data/projets.json','Contrat enrichi du laboratoire.'],
 ['Conserver et reprendre','Kit candidat JSON S19','ZIP','supports/kit-candidat-S19.zip','Laboratoire, modèles de preuve, prompts et relais.'],
 ['Conserver et reprendre','Fiche candidat','PDF','supports/fiche-candidat-S19.pdf','Prédire, observer, expliquer et corriger.'],
 ['Conserver et reprendre','Prompts 19-A à 19-F','MD','supports/prompts-S19.md','Six missions adaptées au périmètre validé.'],
 ['Conserver et reprendre','Révision et quiz corrigé','PDF','supports/revision-S19.pdf','12 cartes, 8 questions et 24 explications.'],
 ['Conserver et reprendre','Grille et preuve vierge','MD','supports/kit-json-S19/06-PORTFOLIO/preuve-S19.md','Aucun résultat candidat prérempli.'],
 ['Conserver et reprendre','Relais S20','MD','supports/kit-json-S19/06-PORTFOLIO/relais-S20.md','Préparer les composants et les futurs tests PWA.'],
 ['Sources et cadre','Fiche S19 de référence','MD','supports/seance-19-json-pwa-v2.md','Source historique datée, cadre courant explicité.'],
 ['Sources et cadre','Périmètre V2 retenu','MD','supports/README-laboratoire-S19-V2.md','Objectif validé par le pilote.'],
 ['Sources et cadre','Sources et synchronisation','MD','supports/SOURCES-ET-SYNCHRONISATION.md','Traçabilité ; le pack V3 n’impose pas son extension.'],
 ['Sources et cadre','Repères de la présente édition','MD','supports/REPERES-S19-ETE-AUTOMNE.md','Comprendre et manipuler avant la PWA.'],
 ['Liens externes','Atelier S16','WEB','https://elhisse-clprepas.github.io/atelier-seance-16-ln-ia/','Source antérieure du parcours.'],
 ['Liens externes','Bootstrap et Vite','WEB','https://getbootstrap.com/docs/5.3/getting-started/vite/','Documentation officielle.'],
 ['Liens externes','Fetch et réponse HTTP','WEB','https://developer.mozilla.org/fr/docs/Web/API/Fetch_API/Using_Fetch','Documentation du navigateur.'],
 ['Liens externes','CORS','WEB','https://developer.mozilla.org/fr/docs/Web/HTTP/Guides/CORS','Origines et autorisations de lecture.'],
 ['Liens externes','Service workers','WEB','https://developer.mozilla.org/fr/docs/Web/API/Service_Worker_API/Using_Service_Workers','Passerelle vers S20.'],
 ['Liens externes','Vite : publication statique','WEB','https://vite.dev/guide/static-deploy.html','Construction du dossier dist.']
].map(([group,title,format,path,detail])=>({group,title,format,path,detail,external:path.startsWith('https:')}));
