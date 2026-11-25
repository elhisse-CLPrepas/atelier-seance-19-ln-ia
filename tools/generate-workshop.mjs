import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {execFileSync} from 'node:child_process';
import {renderSite} from '../src/workshop-render.js';
import {blankState,proofText,indexText,relayText} from '../src/workshop-state.js';
import {createZip} from '../src/zip.js';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const read=p=>fs.readFile(path.join(root,p),'utf8');
const d=JSON.parse(await read('src/seance.json')),config=JSON.parse(await read('site.config.json'));
async function write(p,c){await fs.mkdir(path.dirname(path.join(root,p)),{recursive:true});await fs.writeFile(path.join(root,p),c)}
async function copy(from,to){await fs.mkdir(path.dirname(path.join(root,to)),{recursive:true});await fs.copyFile(path.join(root,from),path.join(root,to))}
async function resetGenerated(relative){
 const allowed=['public/laboratoire-json','public/mini-sites/json-minimal','public/supports/kit-json-S19'];
 if(!allowed.includes(relative))throw Error('Destination générée non autorisée');
 const absolute=path.resolve(root,relative),publicRoot=path.resolve(root,'public')+path.sep;
 if(!absolute.startsWith(publicRoot))throw Error('Destination hors de public');
 await fs.rm(absolute,{recursive:true,force:true});
}
if(config.publicUrl){const u=new URL(config.publicUrl);if(u.protocol!=='https:'||u.search||u.hash)throw Error('publicUrl doit être une adresse HTTPS sans paramètres ni fragment.')}
await write('index.html',renderSite(d,config));
await write('public/projection-S19.html',renderSite(d,config).replace('data-resource-base="./"','data-resource-base="./" data-project="true"'));
const base='public/supports/',kit=base+'kit-json-S19/';
for(const relative of ['public/laboratoire-json','public/mini-sites/json-minimal','public/supports/kit-json-S19'])await resetGenerated(relative);
await fs.cp(path.join(root,'05-EXEMPLES-CODE/mini-site-seance-19-V2'),path.join(root,'public/laboratoire-json'),{recursive:true});
await fs.cp(path.join(root,'05-EXEMPLES-CODE/mini-site-json-seance-19-v1-a-valider'),path.join(root,'public/mini-sites/json-minimal'),{recursive:true});
// La fiche locale est la source de cadrage. Les anciens packs restent intacts.
await copy('seance-19-json-pwa-v2.md',base+'seance-19-json-pwa-v2.md');
await copy('pack-documentaire-seance-19-v1-a-valider/SOURCES-ET-SYNCHRONISATION.md',base+'SOURCES-ET-SYNCHRONISATION.md');
const labReadme=(await read('05-EXEMPLES-CODE/mini-site-seance-19-V2/README.md')).replace(/cd "C:[^"]+"/,'# Ouvrir le dossier laboratoire-json extrait de ce kit.');
await write(base+'README-laboratoire-S19-V2.md',labReadme);
await write('public/laboratoire-json/README.md',labReadme);
await write(base+'REPERES-S19-ETE-AUTOMNE.md',`# Repères de cette édition S19\n\n27 novembre 2026 · 110 minutes.\n\nLa fiche seance-19-json-pwa-v2.md conserve ses dates historiques du 27 juillet. La présente édition synchronise le cadre pour le 27 novembre. Le README du mini-site S19 V2, explicitement validé par le pilote dans sa demande de refonte, fixe le périmètre : notions, mécanismes et manipulations, indépendamment d’une PWA complète.\n\nJSON, schéma, fetch, HTTP, quatre états, DOM sûr, cartes et flashcards accessibles, scénarios 404/schéma/lien dangereux forment le travail guidé. API/CORS/PHP se comparent ; l’exécution PHP reste facultative. Manifeste, service worker et cache se préparent pour S20 sans activation.\n\nLe pack V3 antérieur est conservé ; sa mise à jour n’est pas retenue comme autorité de cadrage pour cette refonte. Les observations candidates restent vierges.\n`);
await write(base+'notes-formateur-S19.md',`# Notes formateur S19\n\n${d.meta.dateLabel} · ${d.slides.length} vues · ${d.meta.duration} minutes\n\n`+d.slides.map((s,i)=>`## ${i+1}. ${s.title}\n\n${s.lead}\n\n${s.points.map(([a,b])=>'- '+a+' : '+b).join('\n')}\n\nGeste : ${s.gesture}\n\nNote : ${s.note}\n`).join('\n'));
await write(base+'conducteur-S19.md',`# Conducteur S19 — JSON local et préparation PWA\n\n${d.meta.dateLabel} · 110 minutes · Horaire Casablanca à communiquer.\n\nAvant : V1 conservée ou laboratoire V2, navigateur et console, serveur déjà disponible, données fictives.\n\n`+d.phases.map(p=>`## ${p.time} minutes · ${p.verb} · vues ${p.slides}\n\nFormateur : ${p.trainer}\n\nCandidat : ${p.candidate}\n\nObservation : ${p.observe}\n\nRelance : ${p.relance}\n`).join('\n')+'\nUne variante de 90 minutes peut reporter les comparaisons et la passerelle PWA. Ne pas retirer les quatre états ni la preuve.\n');
await write(base+'prompts-S19.md','# Prompts S19 — notions et mécanismes\n\n'+d.prompts.map(p=>`## ${p.title}\n\nEntrée : ${p.input}\n\nLimites : ${p.limit}\n\nSortie : ${p.output}\n\nTest : ${p.test}\n\n${p.text}\n`).join('\n'));
await write(base+'revision-S19.md','# Révision S19\n\n'+d.cards.map(([q,a],i)=>`## Carte ${i+1}. ${q}\n\n${a}\n`).join('\n')+'\n# Quiz corrigé\n\n'+d.quiz.map(([q,choices,correct,exps],i)=>`## ${i+1}. ${q}\n\n`+choices.map((c,j)=>`- ${c}${j===correct?' · Choix attendu':''}\n  ${exps[j]}`).join('\n')).join('\n\n'));
const s=blankState();
await write('public/laboratoire-json/preuve-19-json-pwa.md',proofText(s,d));
for(const[name,body]of [['preuve-S19.md',proofText(s,d)],['index-portfolio.md',indexText(s)],['relais-S20.md',relayText(s)]])await write(kit+'06-PORTFOLIO/'+name,body);
await write(kit+'06-PORTFOLIO/grille-revue-S19.md','# Revue JSON S19\n\n'+d.criteria.map(c=>'- [ ] '+c).join('\n')+'\n\nPilote : À COMPLÉTER\nDate : À COMPLÉTER\nObservation : À COMPLÉTER\nDécision : À COMPLÉTER\n');
await write(kit+'LISEZ-MOI.md','# Kit JSON S19 · 27 novembre 2026\n\nComprendre avant de construire. Ouvrir le laboratoire depuis un serveur local déjà disponible sur le port 8080 ; exécuter les sept scénarios, observer les quatre états et utiliser les flashcards au clavier. Conserver les originaux et travailler dans une copie.\n\n04-WEB/mini-site-v2 contient le laboratoire enrichi ; le contrat de ses six ressources est plus riche que le contrat de trois champs de l’exemple simple. 06-PORTFOLIO contient les traces vierges. Les prompts guident l’explication et les tests. Aucune PWA complète n’est demandée.\n');
await fs.cp(path.join(root,'public/laboratoire-json'),path.join(root,kit+'04-WEB/mini-site-v2'),{recursive:true});
await copy(base+'prompts-S19.md',kit+'prompts-S19.md');
try{await copy(base+'fiche-candidat-S19.pdf',kit+'fiche-candidat-S19.pdf')}catch(error){if(error.code!=='ENOENT')throw error}
await copy(base+'REPERES-S19-ETE-AUTOMNE.md',kit+'REPERES-S19.md');
async function zipFolder(folder,name,prefix){const entries=[];async function walk(dir){for(const item of await fs.readdir(dir,{withFileTypes:true})){const p=path.join(dir,item.name);if(item.isDirectory())await walk(p);else entries.push({name:prefix+path.relative(folder,p).split(path.sep).join('/'),data:new Uint8Array(await fs.readFile(p))})}}await walk(folder);await write(name,new Uint8Array(await createZip(entries).arrayBuffer()))}
await zipFolder(path.join(root,'public/laboratoire-json'),base+'laboratoire-json-S19.zip','laboratoire-json/');
await zipFolder(path.join(root,kit),base+'kit-candidat-S19.zip','kit-JSON-S19/');
await copy('public/assets/logo-LN-IA.png','public/assets/favicon.png');
await write('public/robots.txt',config.indexable&&config.publicUrl?'User-agent: *\nAllow: /\n':'User-agent: *\nDisallow: /\n');
console.log('S19 : onze rubriques, projection, prompts, kit JSON et laboratoires synchronisés.');
execFileSync('python',[path.join(root,'tools/sync-challenge.py')],{cwd:root,stdio:'inherit'});
