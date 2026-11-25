"""Enrichit le dossier commun depuis les ateliers locaux S17-S20 (lecture seule).
Sauvegarde préalable ; ne remplace ni productions ni preuves existantes.
Exécution : python -X utf8 tools/enrich-challenge.py
"""
from pathlib import Path
from datetime import datetime
import json,shutil,zipfile,hashlib,csv,html,re
R=Path(__file__).resolve().parents[1];C=R/'mon-dossier-challenge-Module05';PARENT=R.parent
assert C.resolve().parent==R.resolve()
if (C/'00-SOURCES/CONTROLE-SYNCHRONISATION.json').exists():
    raise SystemExit('Dossier déjà enrichi : utiliser tools/sync-challenge.py pour diffuser sans réinitialiser les contenus.')
stamp=datetime.now().strftime('%Y%m%d-%H%M%S');backup=R/'docs/sauvegardes'/('dossier-module05-avant-alignement-'+stamp+'.zip');backup.parent.mkdir(parents=True,exist_ok=True)
original={p.relative_to(C).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()for p in C.rglob('*')if p.is_file()and'.git'not in p.relative_to(C).parts}
with zipfile.ZipFile(backup,'w',zipfile.ZIP_DEFLATED)as z:
    for rel in original:z.write(C/rel,'mon-dossier-challenge-Module05/'+rel)
protected={k:v for k,v in original.items()if k.startswith(('04-WEB/','06-PORTFOLIO/','02-PROMPTS/S18/'))or k=='01-SUIVI/carnet-essai-S17.html'}
def write(rel,text):
    p=C/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text.strip()+'\n',encoding='utf-8')
def copy(src,rel):
    p=C/rel;p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,p)
references=[]
for sid in ['S17','S18','S19','S20']:
    n=sid[1:];workshop=PARENT/f'atelier-seance-{n}-ln-ia'
    candidates=['README.md','src/seance.json',f'public/supports/prompts-{sid}.md']
    if sid=='S18':candidates+=['INSTRUCTIONS-PARTICIPANTS-S18.md','AGENT.md']+[p.name for p in workshop.glob('PROMPT-MAITRE-PRODUCTION-S18*.md')]
    if sid=='S19':candidates+=['seance-19-json-pwa-v2.md','05-EXEMPLES-CODE/mini-site-seance-19-V2/README.md','pack-documentaire-seance-19-v1-a-valider/SOURCES-ET-SYNCHRONISATION.md']
    if sid=='S20':candidates+=['src/exports.js','public/supports/checklist-paquet-S20.md','public/supports/trame-orale-S20.md','public/supports/recette-PWA-S20.md']
    for relative in candidates:
        source=workshop/relative
        if not source.exists():continue
        dest=f'00-SOURCES/ATELIERS/{sid}/{relative}';copy(source,dest)
        references.append({'session':sid,'source':str(source),'copy':dest,'sha256':hashlib.sha256(source.read_bytes()).hexdigest()})
    prompt=workshop/f'public/supports/prompts-{sid}.md'
    if prompt.exists():copy(prompt,f'02-PROMPTS/PARCOURS/{sid}/prompts.md')
for fromdir,dest in [(R/'05-EXEMPLES-CODE/mini-site-seance-19-V2','04-WEB/EXEMPLES-ATELIERS/S19/laboratoire-v2'),(R/'05-EXEMPLES-CODE/mini-site-json-seance-19-v1-a-valider','04-WEB/EXEMPLES-ATELIERS/S19/json-minimal'),(PARENT/'atelier-seance-20-ln-ia/public/supports/cas/cap-etudes','04-WEB/EXEMPLES-ATELIERS/S20/cap-etudes')]:
    target=C/dest
    # Les exemples déjà présents ne sont pas écrasés : une relance conserve les essais locaux.
    if not target.exists():shutil.copytree(fromdir,target)
    for p in fromdir.rglob('*'):
        if p.is_file():references.append({'session':'S20'if'S20'in dest else'S19','source':str(p),'copy':dest+'/'+p.relative_to(fromdir).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
for name in ['parcours.css','parcours.js']:copy(R/'tools/challenge-assets'/name,'assets/'+name)

sessions=[
dict(id='S17',date='2026-11-20',dateLabel='Vendredi 20 novembre 2026',duration=90,title='Comprendre les fondations du Web',goal='Observer HTML, CSS, JavaScript et le navigateur ; prédire, essayer et expliquer.',entry='Mini-site de démonstration fourni et carnet d’essai S17.',production='06-PORTFOLIO/carnet-essai-S17.md et preuve-S17.md',example='04-WEB/mini-site-demonstration/index.html',proof='06-PORTFOLIO/preuve-S17.md',proofName='preuve-S17.md',prompt='02-PROMPTS/PARCOURS/S17/prompts.md',next='Rassembler projet et sources pour produire le pack S18.'),
dict(id='S18',date='2026-11-23',dateLabel='Lundi 23 novembre 2026',duration=90,title='De mes sources à mon pack mini-site',goal='Cadrer le projet, préparer les trois documents et le prompt, produire puis essayer le pack.',entry='Compréhension S17, sources autorisées, projet et besoin.',production='04-WEB/mon-projet-S18/ : site, ZIP, README, SOURCES et CONTROLE',example='04-WEB/livrables-S18/mini-site-declic-web/index.html',proof='06-PORTFOLIO/preuve-S18.md',proofName='preuve-S18.md',prompt='02-PROMPTS/PARCOURS/S18/prompts.md',next='Conserver la V1 et repérer les contenus répétitifs pour JSON et HTTP en S19.'),
dict(id='S19',date='2026-11-27',dateLabel='Vendredi 27 novembre 2026',duration=110,title='JSON local, HTTP et préparation PWA',goal='Comprendre JSON, schéma, fetch, quatre états et DOM sûr ; manipuler sept scénarios et les flashcards.',entry='V1 S18 conservée ou laboratoire V2 fictif, navigateur et serveur local déjà disponible.',production='04-WEB/mon-projet-S19/ et 06-PORTFOLIO/preuve-S19-json-http-dom.md',example='04-WEB/EXEMPLES-ATELIERS/S19/laboratoire-v2/index.html',proof='06-PORTFOLIO/preuve-S19-json-http-dom.md',proofName='preuve-S19-json-http-dom.md',prompt='02-PROMPTS/PARCOURS/S19/prompts.md',next='Transmettre la V2 JSON, les états testés et une consigne lecteur pour S20 ; PWA facultative.'),
dict(id='S20',date='2026-11-30',dateLabel='Lundi 30 novembre 2026',duration=90,title='Éprouver une V2 et clôturer le module',goal='Faire essayer, motiver une correction, comparer deux versions et rouvrir les quatre preuves.',entry='Projet fonctionnel conservé, preuve S19 et tâche stable confiée à un lecteur.',production='Deux versions distinctes, preuve-S20.md, bilan Module 05 et relais-S21.md',example='04-WEB/EXEMPLES-ATELIERS/S20/cap-etudes/04-WEB/page-simple-v2.html',proof='06-PORTFOLIO/preuve-S20.md',proofName='preuve-S20.md',prompt='02-PROMPTS/PARCOURS/S20/prompts.md',next='Rouvrir sources, versions et preuves pour l’organisation du projet en S21.')]
labels=dict(project='Projet personnel ou cas fictif',input='Fichiers / URL / versions d’entrée',task='Manipulation ou consigne lecteur',expected='Résultat attendu avant l’essai',observed='Résultat réellement observé',cause='Cause expliquée et mécanisme concerné',correction='Correction motivée / avant et après',secondTest='Résultat du second essai avec la même consigne',limits='Limites et essais non réalisés',next='Prochaine séance : fichier et premier geste',reader='Lecteur ou binôme',date='Date réelle de l’essai',browser='Navigateur / appareil / mode local ou HTTP',pilot='Pilote',reviewDate='Date de revue',review='Observation et décision motivée',status='Statut')
config={'updated':'2026-11-26','sessions':sessions,'labels':labels}
write('00-SOURCES/parcours-S17-S20.json',json.dumps(config,ensure_ascii=False,indent=2))
write('00-SOURCES/SYNCHRONISATION-S17-S20.json',json.dumps({'date':'2026-11-26','sources_modified':False,'references':references},ensure_ascii=False,indent=2))
config_html='<script type="application/json" id="module-config">'+json.dumps(config,ensure_ascii=False).replace('<','\\u003c')+'</script>'
def shell(title,body,prefix='',view='hub'):
    return f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} · LN-IA</title><meta name="description" content="Parcours Module 05 : comprendre le Web, produire, manipuler JSON et éprouver ses versions. S17 à S20."><meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="#071a2f"><link rel="stylesheet" href="{prefix}assets/parcours.css"><script src="{prefix}assets/parcours.js" defer></script></head><body data-view="{view}"><a class="skip" href="#main">Aller au contenu</a><header><a class="identity" href="{prefix}index.html"><img src="{prefix}assets/logo-LN-IA.png" width="110" height="55" alt="LN-IA"><span>Mon dossier Challenge<small>Module 05 · S17 à S20</small></span></a><nav aria-label="Parcours"><a href="{prefix}index.html#parcours">Les quatre séances</a><a href="{prefix}01-SUIVI/carnet-module05.html">Mon carnet</a><a href="{prefix}06-PORTFOLIO/INDEX-PARCOURS-S17-S20.md">Portfolio</a><a href="{prefix}GUIDE-DOSSIER.md">Guide</a></nav></header><main id="main">{body}</main><footer>LAB-NUMÉRIQUE-IA · Prof. Abderrahman EL HISSE · Synchronisation du 26 novembre 2026. Les observations restent à renseigner.</footer>{config_html}</body></html>'''
cards=''.join(f'''<article class="card"><p class="date">{s['id']} · {s['dateLabel']} · {s['duration']} min</p><h3>{s['title']}</h3><p>{s['goal']}</p><p class="muted"><b>Entrée :</b> {s['entry']}</p><div class="links"><a href="{s['example']}">Ouvrir l’exemple</a><a href="01-SUIVI/consignes-{s['id']}.md">Consignes</a><a href="{s['prompt']}">Prompts</a><a href="{s['proof']}">Preuve</a></div></article>'''for s in sessions)
hub='''<div class="hero"><p class="eyebrow">Challenge 100 Jours · Automne 2026</p><h1>Un projet.<br>Quatre étapes pour comprendre et progresser.</h1><p>Observer le Web en S17, produire son pack en S18, manipuler les données en S19, puis éprouver ses versions en S20. Retrouver les bons fichiers et conserver ses preuves.</p><div class="actions"><a class="button gold" href="01-SUIVI/carnet-module05.html">Ouvrir mon carnet S17–S20</a><a class="button" href="01-SUIVI/carnet-essai-S17.html">Carnet S17 d’origine</a></div></div>'''
hub+='<section id="parcours"><p class="eyebrow">01 · Progression</p><h2>Les quatre séances, leurs entrées et leurs sorties</h2><div class="cards">'+cards+'</div></section>'
hub+='''<div class="note"><h3>Passage S19 → S20 : conserver les mécanismes et la revue lecteur</h3><p>S19 porte sur JSON/HTTP/DOM ; le carnet S20 actuel attend une ancienne page simple ou son ancien carnet S19. Les nouveaux carnets JSON et Module 05 ne sont pas importables directement dans cet outil. Reprendre les fichiers et les preuves Markdown ; pour un mini-site enrichi, travailler dans l’éditeur en conservant deux versions.</p><a href="01-SUIVI/passage-S19-S20.md">Lire le passage et ses limites</a></div>'''
hub+='''<section><p class="eyebrow">02 · Observer et manipuler</p><h2>Les exemples intégrés</h2><div class="grid"><div class="panel"><h3>S19 · JSON, HTTP et DOM</h3><p>Le laboratoire enrichi contient six ressources et sept scénarios. Le minimal propose trois champs, recherche, import et export. Les deux contrats restent distingués.</p><div class="links"><a href="04-WEB/EXEMPLES-ATELIERS/S19/laboratoire-v2/index.html">Laboratoire V2</a><a href="04-WEB/EXEMPLES-ATELIERS/S19/json-minimal/index.html">Exemple minimal</a><a href="04-WEB/EXEMPLES-ATELIERS/S19/laboratoire-v2/preparation-pwa.html">PWA : simulations facultatives</a></div></div><div class="panel"><h3>S20 · Comparer avant et après</h3><p>Le cas fictif Cap Études contient deux pages et leur fiche commune. Utiliser une même consigne et consigner les observations réelles.</p><div class="links"><a href="04-WEB/EXEMPLES-ATELIERS/S20/cap-etudes/04-WEB/page-simple-v1.html">Voir la V1 fictive</a><a href="04-WEB/EXEMPLES-ATELIERS/S20/cap-etudes/04-WEB/page-simple-v2.html">Voir la V2 fictive</a></div></div></div></section>'''
hub+='''<section><p class="eyebrow">03 · Productions conservées</p><h2>Vos pièces antérieures restent disponibles</h2><p>La synchronisation n’écrase pas les preuves et productions existantes. Les anciens modèles S19 d’assemblage sont conservés à titre historique ; les consignes et la preuve JSON font foi pour le parcours courant.</p><div class="links"><a href="04-WEB/livrables-S18/mini-site-declic-web/index.html">Production fictive Déclic Web S18</a><a href="04-WEB/livrables-S18/mini-site-declic-web.zip">ZIP S18 conservé</a><a href="06-PORTFOLIO/index-portfolio.md">Index antérieur</a><a href="06-PORTFOLIO/INDEX-PARCOURS-S17-S20.md">Index aligné</a><a href="03-MESSAGES-WhatsApp/index.html">Messages et modèles</a></div></section>'''
resource_rows=[('GUIDE-DOSSIER.md','Guide du dossier','Mode local, HTTP, preuves et reprise.'),('01-SUIVI/MATRICE-S17-S20.md','Matrice d’alignement','Dates, entrées, sorties et tests.'),('00-SOURCES/SYNCHRONISATION-S17-S20.json','Provenance et empreintes','Sources locales examinées sans modification.'),('FLUX-VERSIONNEMENT.md','Versionnement réel de cette copie','Aucun dépôt Git ni push supposé.'),('06-PORTFOLIO/BILAN-PARCOURS-MODULE05.md','Bilan et relais S21','Quatre preuves à rouvrir.'),('RAPPORT-SYNCHRONISATION-S17-S20.md','Rapport de synchronisation','Conservation et contrôles.'),('00-SOURCES/ATELIERS/S19/seance-19-json-pwa-v2.md','Fiche S19 historique','Source de juillet, synchronisée pour novembre.')]
for s in sessions:resource_rows.append((s['prompt'],'Prompts '+s['id'],s['title']))
hub+='<section id="ressources"><h2>Sources, guides et modèles</h2><label class="field">Filtrer les ressources<input id="resource-search" type="search" placeholder="Séance, guide, preuve…"></label><p id="resource-count" class="count">'+str(len(resource_rows))+' ressources disponibles.</p>'+''.join(f'<a class="resource" href="{url}"><b>{title}</b><small>{detail}</small></a>'for url,title,detail in resource_rows)+'</section>'
write('index.html',shell('Mon dossier Module 05 · parcours synchronisé',hub))
def field(k,rows=3):
    label=labels[k]
    if k=='status':control='<select id="f-status" name="status">'+''.join('<option>'+s+'</option>'for s in ['À COMPLÉTER','À REVOIR','À VALIDER','VALIDÉ'])+'</select>'
    elif k in ('date','reviewDate'):control=f'<input type="date" id="f-{k}" name="{k}">'
    else:control=f'<textarea id="f-{k}" name="{k}" rows="{rows}" placeholder="À compléter avec vos propres observations"></textarea>'
    return f'<label class="field" for="f-{k}">{label}{control}</label>'
body='''<p class="eyebrow">Carnet transversal · indépendant des carnets propres aux ateliers</p><h1>Mon parcours S17 à S20</h1><p>Les saisies restent dans ce navigateur. Les exports se téléchargent : rangez-les dans votre copie, après comparaison avec vos fichiers existants.</p><p class="status" id="save-status" role="status">Prêt à renseigner vos observations.</p><div class="stage-select" role="group" aria-label="Choisir la séance">'''+''.join(f'<button type="button" data-session="{s["id"]}" aria-pressed="false">{s["id"]} · {s["date"][8:]}/{s["date"][5:7]}</button>'for s in sessions)+'''</div><section class="panel"><h2 id="session-title"></h2><p id="session-context"></p><p><b>Entrée :</b> <span id="session-input"></span></p><p><b>Sortie :</b> <span id="session-output"></span></p><p><b>Suite :</b> <span id="session-next"></span></p><div class="links"><a id="session-example" href="#">Ouvrir l’exemple</a><a id="session-prompt" href="#">Lire les prompts</a></div></section><form id="evidence-form"><section><h2>Prédire, observer et expliquer</h2><div class="grid">'''+''.join(field(k)for k in ['project','input','task','expected','observed','cause'])+'''</div></section><details><summary>Correction, second essai et limites</summary><div class="panel grid">'''+''.join(field(k)for k in ['correction','secondTest','limits','next'])+'''</div></details><section><h2>Contexte de l’essai</h2><div class="grid">'''+''.join(field(k,2)for k in ['reader','date','browser'])+'''</div></section><details class="review"><summary>Revue du pilote</summary><p>Les modèles et le score d’un quiz ne valident pas une production. Une modification après validation remet la séance à revoir.</p><div class="grid">'''+''.join(field(k,2)for k in ['pilot','reviewDate','review','status'])+'''</div><p id="review-status" role="status"></p></details></form><div class="actions"><button type="button" class="primary" id="export-proof">Exporter la preuve de cette séance</button><button type="button" id="export-module">Exporter le bilan des quatre séances</button><button type="button" id="export-json">Sauvegarder le carnet JSON</button><label class="file-button">Reprendre ce carnet<input id="import-json" type="file" accept=".json,application/json"></label><button type="button" id="print-carnet">Imprimer</button><button type="button" id="reset-session">Vider cette séance</button></div><details><summary>Relire la preuve avant export</summary><pre id="proof-preview"></pre></details><div class="note">Ce carnet transversal possède son format JSON propre. Il n’est pas importable directement dans les carnets S17, S18, S19 ou S20. Utilisez les preuves Markdown et les fichiers du projet pour passer d’un atelier à l’autre.</div>'''
write('01-SUIVI/carnet-module05.html',shell('Carnet transversal S17 à S20',body,'../','carnet'))

matrix='# Matrice d’alignement S17–S20\n\nSynchronisation du 26 novembre 2026. Les dates sont celles de la programmation ; les essais réels restent à renseigner.\n\n| Séance | Date / durée | Entrée | Travail | Sortie et relais |\n|---|---|---|---|---|\n'+''.join(f'| {s["id"]} | {s["dateLabel"]} / {s["duration"]} min | {s["entry"]} | {s["goal"]} | {s["production"]} ; {s["next"]} |\n'for s in sessions)
matrix+='\nLe périmètre S20 reflète les fichiers actuels de cet atelier : revue lecteur et comparaison de versions. La construction complète d’une PWA n’est pas imposée par la synchronisation. Le pack V3 S19 n’a pas été modifié ni pris comme autorité de cadrage.\n'
write('01-SUIVI/MATRICE-S17-S20.md',matrix)
for s in sessions:
    text=f'# {s["id"]} — {s["title"]}\n\n{s["dateLabel"]} · {s["duration"]} minutes proposées · Horaire Casablanca à communiquer.\n\n## Entrée\n\n{s["entry"]}\n\n## Travail\n\n{s["goal"]}\n\n## Production\n\n{s["production"]}\n\n## Preuve et reprise\n\nRenseigner le carnet transversal ou celui de l’atelier. Exporter attendu, observé, cause et correction sans remplacer automatiquement vos fichiers sur disque. Le modèle aligné est dans 06-PORTFOLIO/modeles-alignes/.\n\n{s["next"]}\n'
    if s['id']=='S19':text+='\nUtiliser EXEMPLES-ATELIERS/S19/laboratoire-v2 pour les six ressources et sept scénarios ; json-minimal pour les trois champs. Servir le dossier avec HTTP local pour fetch. Les composants PWA sont seulement expliqués. L’ancienne preuve-S19.md d’assemblage est conservée ; la preuve courante est preuve-S19-json-http-dom.md.\n'
    if s['id']=='S20':text+='\nNe pas importer le nouveau carnet JSON S19 ou ce carnet transversal dans l’ancien importeur S20. Lire passage-S19-S20.md. Pour un site enrichi, garder deux dossiers versionnés et utiliser l’éditeur ; le générateur S20 importe seulement ses pages simples compatibles.\n'
    write(f'01-SUIVI/consignes-{s["id"]}.md',text)
    model=f'# Modèle aligné {s["id"]} — {s["title"]}\n\nStatut : À COMPLÉTER\n\n'+''.join('## '+label+'\n\nÀ COMPLÉTER\n\n'for key,label in labels.items()if key!='status')
    write(f'06-PORTFOLIO/modeles-alignes/preuve-{s["id"]}.md',model)
    if s['id']=='S19'and not(C/s['proof']).exists():write(s['proof'],model)
    write(f'02-PROMPTS/PARCOURS/{s["id"]}/LIRE-MOI.md',f'# Prompts {s["id"]}\n\nSource : atelier local {s["id"]}, copie du 26 novembre 2026.\n\nObjectif : {s["goal"]}\n\nLes prompts ne remplissent pas les observations à la place du candidat. Le parcours courant et les limites de passage sont décrits dans 01-SUIVI/MATRICE-S17-S20.md à la racine du dossier commun.\n')
write('01-SUIVI/passage-S18-S19.md','''# Passage S18 → S19

Conserver le site et le ZIP S18, ses sources, README, SOURCES et CONTROLE. Ouvrir une copie de travail ou le laboratoire fictif fourni. Repérer les données répétitives, puis suivre URL → HTTP → JSON → validation → DOM. Tester chargement, succès, vide et erreur ; comparer schéma invalide et lien refusé. Conserver une preuve JSON/HTTP/DOM sans prétendre construire une PWA complète.

Les anciennes productions d’assemblage et preuves sont conservées. Utiliser la preuve-S19-json-http-dom.md pour cette édition.
''')
write('01-SUIVI/passage-S19-S20.md','''# Passage S19 JSON → S20 revue lecteur

## Ce qui se transmet

- La V1 S18 intacte et la copie V2 JSON, ou le cas fictif étudié.
- Le JSON, le script de chargement, les résultats des quatre états et la preuve S19.
- Une consigne lecteur stable : retrouver une ressource, lire sa carte ou utiliser une flashcard.
- Le mécanisme compris et l’écart observé, sans résultat inventé.

## Compatibilité des carnets

L’atelier S20 actuel sait importer l’ancien carnet `lnia-s19` version 1 consacré à une page simple. Le carnet S19 refondu utilise `lnia-s19-mecanismes` version 2 ; le carnet transversal utilise `lnia-module05-parcours` version 1. Ces deux nouveaux formats ne sont pas importables directement dans S20. Ne pas modifier leur signature pour forcer l’import.

Pour un projet JSON enrichi : reprendre les fichiers dans votre éditeur, garder deux versions distinctes, faire essayer la même consigne et compléter la preuve S20 ou le carnet transversal. Pour utiliser le générateur S20, partir d’une page simple compatible ou de son exemple Cap Études. Le README S20 copié dans 00-SOURCES/ATELIERS/S20 explique ses limites.

## Revue S20

Noter lecteur, appareil et date du premier essai ; choisir une correction motivée ; conserver l’ancienne version ; produire la suivante ; rejouer la consigne ; comparer les faits et limites. Rouvrir les quatre preuves et préparer S21. La PWA reste un approfondissement séparé, soumis à ses propres tests.
''')
write('01-SUIVI/carnet-module05.md','# Suivi du parcours Module 05\n\nLe carnet interactif actuel est carnet-module05.html. Les observations existantes ne sont pas réécrites par une synchronisation.\n\n'+matrix[matrix.index('| Séance'):])
index='# Index courant du parcours S17–S20\n\nLes productions et preuves antérieures restent conservées. Les nouveaux modèles alignés ne constituent pas des résultats observés.\n\n'
for s in sessions:index+=f'- **{s["id"]} · {s["title"]}** : [preuve disponible]({Path(s["proof"]).name}) · [modèle aligné](modeles-alignes/preuve-{s["id"]}.md) · [consignes](../01-SUIVI/consignes-{s["id"]}.md).\n'
index+='\n[Ancien index conservé](index-portfolio.md) · [Bilan courant](BILAN-PARCOURS-MODULE05.md) · [Relais S21 conservé](relais-S21.md).\n'
write('06-PORTFOLIO/INDEX-PARCOURS-S17-S20.md',index)
write('06-PORTFOLIO/BILAN-PARCOURS-MODULE05.md','''# Bilan courant Module 05

Statut : À COMPLÉTER

| Séance | Fichier réellement rouvert | Observation | Pièce manquante / correction | Décision du pilote |
|---|---|---|---|---|
| S17 · Comprendre | À COMPLÉTER | À COMPLÉTER | À COMPLÉTER | À COMPLÉTER |
| S18 · Produire le pack | À COMPLÉTER | À COMPLÉTER | À COMPLÉTER | À COMPLÉTER |
| S19 · JSON / HTTP / DOM | À COMPLÉTER | À COMPLÉTER | À COMPLÉTER | À COMPLÉTER |
| S20 · Éprouver et comparer | À COMPLÉTER | À COMPLÉTER | À COMPLÉTER | À COMPLÉTER |

Avant S21 : rassembler sources, versions, README et quatre preuves ; préciser les limites et les fichiers à conserver. Ne pas supposer un commit, un push ou une diffusion.
''')
# Modifier les seules références de S19 dans le tableau, jamais ses observations.
progress=C/'01-SUIVI/progression.csv'
with progress.open(encoding='utf-8-sig',newline='')as f:reader=csv.DictReader(f,delimiter=';');headers=reader.fieldnames;rows=list(reader)
for row in rows:
    if row.get('seance')=='S19':row['production']=sessions[2]['example'];row['preuve']=sessions[2]['proof']
with progress.open('w',encoding='utf-8',newline='')as f:writer=csv.DictWriter(f,fieldnames=headers,delimiter=';');writer.writeheader();writer.writerows(rows)
write('README.md','''# Mon dossier Challenge — Module 05 · S17 à S20

Édition synchronisée du 26 novembre 2026 · LAB-NUMÉRIQUE-IA · Prof. Abderrahman EL HISSE.

Ouvrir index.html : parcours, exemples, carnet transversal, prompts et portfolio. Le dossier s’ouvre par double-clic ; le laboratoire JSON exige HTTP local pour observer les véritables requêtes.

Depuis ce dossier : `python -m http.server 8081 --bind 127.0.0.1`, puis http://127.0.0.1:8081/. Le port 8081 évite de remplacer l’atelier S19 déjà servi sur 8080. Utiliser un Python déjà disponible.

- S17 : comprendre HTML/CSS/JavaScript et le navigateur.
- S18 : partir des sources pour produire et essayer le pack mini-site.
- S19 : comprendre JSON, schéma, HTTP, fetch et DOM sûr ; éprouver les quatre états et sept scénarios.
- S20 : faire essayer, corriger, comparer et clôturer le module ; PWA en approfondissement distinct.

Les fichiers dans EXEMPLES-ATELIERS sont des références fictives : les copier dans son dossier personnel avant adaptation. Les productions S18, les preuves existantes et le carnet S17 d’origine sont conservés. Le nouveau carnet ne remplace aucun fichier sur disque automatiquement.

La copie locale ne contient pas de dépôt Git initialisé. Aucun commit, remote, push ou état publié n’est supposé. Voir FLUX-VERSIONNEMENT.md avant tout choix de versionnement.

Voir GUIDE-DOSSIER.md, 01-SUIVI/MATRICE-S17-S20.md et RAPPORT-SYNCHRONISATION-S17-S20.md.
''')
write('GUIDE-DOSSIER.md','''# Guide du dossier synchronisé S17–S20

## Utiliser la copie

Extraire le ZIP complet, ouvrir index.html et choisir une séance. Les liens sont relatifs. Les fichiers Markdown se lisent dans un éditeur ; le navigateur peut les télécharger. Les liens externes nécessitent Internet.

## Carnets et preuves

Le carnet transversal 01-SUIVI/carnet-module05.html distingue les quatre séances et sauvegarde ses propres saisies dans le navigateur. Exporter son JSON pour la reprise, une preuve Markdown par séance et un bilan global. Aucun téléchargement n’écrit automatiquement dans le dossier. Comparer avant de remplacer une preuve existante.

Le carnet S17 d’origine est conservé. Les carnets des ateliers et le carnet transversal ont des formats différents : ne pas les confondre ni changer leur signature. Utiliser les fichiers et les preuves Markdown pour assurer la continuité.

## Manipuler le Web

S17 : démonstration et carnet d’essai. S18 : production fictive Déclic Web et sources/trio de production. S19 : exemples dans 04-WEB/EXEMPLES-ATELIERS/S19 ; laboratoire enrichi à six ressources et exemple simple à trois champs. S20 : exemple Cap Études V1/V2 et protocole lecteur.

Pour fetch, servir la racine de ce dossier avec `python -m http.server 8081 --bind 127.0.0.1`, puis ouvrir http://127.0.0.1:8081/. Les simulations PWA ne sont pas une installation ni un fonctionnement hors connexion réel.

## Passage S19 → S20

Lire 01-SUIVI/passage-S19-S20.md. L’importeur S20 actuel ne reconnaît pas le carnet JSON du parcours S19 refondu ni le carnet transversal. Pour un site enrichi, reprendre le code dans l’éditeur et conserver deux versions ; utiliser la revue lecteur et la preuve S20 sans forcer l’import.

## Conservation et diffusion

Les sources d’ateliers ont été lues sans modification. Les références sont copiées dans 00-SOURCES/ATELIERS avec leurs empreintes. Les productions et preuves préexistantes ne sont pas écrasées. Les nouveaux modèles sont regroupés dans 06-PORTFOLIO/modeles-alignes. L’ancien index est conservé ; INDEX-PARCOURS-S17-S20.md décrit le parcours courant.

La copie publique de S19 et son ZIP se reconstruisent depuis ce dossier avec tools/sync-challenge.py à la racine de l’atelier. La synchronisation ne réinitialise pas les saisies ou preuves et ne publie rien.
''')
write('CONTEXTE-SYNCHRONISATION.md','''# Contexte local — Module 05

Copie enrichie le 26 novembre 2026 depuis les sources locales S17, S18, S19 et S20. Les ateliers voisins et les sources C: n’ont pas été modifiés. La progression courante est décrite par 01-SUIVI/MATRICE-S17-S20.md.

Aucun dépôt Git n’est initialisé dans cette copie. Les anciennes mentions de remote décrivent les dépôts de référence et ne prouvent ni rattachement ni push. Les décisions pédagogiques et les observations réelles restent celles du pilote et des participants.
''')
write('FLUX-VERSIONNEMENT.md','''# Versionnement de cette copie

Cette copie locale ne possède pas de métadonnées .git. Elle ne constitue pas automatiquement le dépôt autonome mon-dossier-challenge-Module05 ni le dépôt de S18. Aucun remote n’a été attaché et aucun push n’a été effectué par cette synchronisation.

Avant de versionner : choisir explicitement le dépôt de destination, contrôler les fichiers et les exclusions, puis seulement initialiser ou rattacher la copie. Ne pas exécuter les commandes d’un ancien atelier depuis cette copie en supposant qu’elle partage son remote.

Les JSON exportés des navigateurs et les preuves doivent être rangés sur disque après comparaison. Les données personnelles et secrets ne doivent pas entrer dans une copie publique. Les sources se trouvent ici ; public/dossier-challenge et dist/dossier-challenge sont des copies de diffusion régénérées par l’atelier S19. Les ateliers voisins ne sont pas modifiés automatiquement.
''')
for rel,digest in protected.items():assert hashlib.sha256((C/rel).read_bytes()).hexdigest()==digest,'Fichier personnel modifié : '+rel
for ref in references:assert hashlib.sha256(Path(ref['source']).read_bytes()).hexdigest()==ref['sha256'],'Source changée pendant la copie'
write('RAPPORT-SYNCHRONISATION-S17-S20.md',f'''# Synchronisation S17–S20 — 26 novembre 2026

Mission : reproduire et enrichir le dossier commun selon les quatre ateliers locaux.

## Réalisation

- Accueil et guide reconstruits ; matrice d’alignement et consignes actualisées.
- Carnet transversal autonome : quatre séances, sauvegarde JSON, reprise, preuve Markdown, bilan, impression et remise à zéro par séance.
- Références des quatre ateliers copiées avec leurs empreintes ; sources externes non modifiées.
- Laboratoire S19 enrichi et minimal intégrés ; exemple S20 Cap Études V1/V2 ajouté.
- Prompts regroupés par séance ; nouveaux modèles et index courant séparés des preuves préexistantes.
- Limite d’import des carnets S19/S20 explicitée ; aucun faux format de compatibilité créé.
- Références S19 du CSV actualisées sans modifier statut, observation, date ni décision.
- Contexte Git corrigé : pas de dépôt initialisé ni de publication présumée.

## Conservation

Sauvegarde intégrale avant intervention : {backup.relative_to(R).as_posix()} à la racine de l’atelier S19.

{len(protected)} fichiers préexistants de productions, preuves, trio S18 et carnet S17 ont été contrôlés par SHA-256 : contenus inchangés. Le pack V3 et les ateliers voisins restent intacts. Les anciens modèles S19 d’assemblage sont conservés et distingués du parcours JSON actuel.

## Contrôles

Voir 00-SOURCES/CONTROLE-SYNCHRONISATION.json pour les liens et la conservation. La recette du nouveau carnet est consignée dans docs/recette-dossier-module05.json à la racine S19. Les modèles ne constituent pas des observations de séance. Aucune validation candidate ni publication effectuée.
''')
write('00-SOURCES/CONTROLE-SYNCHRONISATION.json',json.dumps({'date':'2026-11-26','backup':str(backup.relative_to(R)),'protected_files':protected,'preserved':len(protected),'source_files':len(references),'source_workshops_modified':False},ensure_ascii=False,indent=2))
print(json.dumps({'backup':str(backup),'preserved':len(protected),'references':len(references),'root':str(C)},ensure_ascii=False))
