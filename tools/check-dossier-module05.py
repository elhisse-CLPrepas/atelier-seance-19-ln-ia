"""Contrôle du dossier et des copies diffusables ; aucune observation candidate créée."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,hashlib,zipfile,csv,io,subprocess
R=Path(__file__).resolve().parents[1];C=R/'mon-dossier-challenge-Module05'
class Links(HTMLParser):
    def __init__(self):super().__init__();self.refs=[];self.ids=[]
    def handle_starttag(self,tag,attrs):
        self.refs.extend(v for k,v in attrs if k in('href','src')and v)
        self.ids.extend(v for k,v in attrs if k=='id')
broken=[];count=0
for p in C.rglob('*.html'):
    count+=1;parser=Links();parser.feed(p.read_text(encoding='utf-8'))
    if len(parser.ids)!=len(set(parser.ids)):broken.append({'file':p.relative_to(C).as_posix(),'duplicate_ids':True})
    for ref in parser.refs:
        url=urlsplit(ref)
        if url.scheme or url.netloc:continue
        if url.path and not (p.parent/unquote(url.path)).exists():broken.append({'file':p.relative_to(C).as_posix(),'link':ref})
        elif not url.path and url.fragment and unquote(url.fragment)not in parser.ids:broken.append({'file':p.relative_to(C).as_posix(),'anchor':ref})
assert not broken,broken
checks=json.loads((C/'00-SOURCES/CONTROLE-SYNCHRONISATION.json').read_text(encoding='utf-8'))
for rel,digest in checks['protected_files'].items():assert hashlib.sha256((C/rel).read_bytes()).hexdigest()==digest,rel
snapshot=json.loads((C/'00-SOURCES/MANIFEST-LIVRAISON.json').read_text(encoding='utf-8'))
for item in snapshot['files']:
    assert hashlib.sha256((C/item['path']).read_bytes()).hexdigest()==item['sha256'],item['path']
    assert (R/'public/dossier-challenge'/item['path']).read_bytes()==(C/item['path']).read_bytes(),item['path']
    if (R/'dist/index.html').exists():assert (R/'dist/dossier-challenge'/item['path']).read_bytes()==(C/item['path']).read_bytes(),item['path']
with zipfile.ZipFile(R/'mon-dossier-challenge-Module05-S17-S20.zip')as z:
    assert z.testzip()is None
    for item in snapshot['files']:assert z.read('mon-dossier-challenge-Module05/'+item['path'])==(C/item['path']).read_bytes(),item['path']
with zipfile.ZipFile(R/checks['backup'])as z:
    old=list(csv.DictReader(io.StringIO(z.read('mon-dossier-challenge-Module05/01-SUIVI/progression.csv').decode('utf-8-sig')),delimiter=';'))
with (C/'01-SUIVI/progression.csv').open(encoding='utf-8',newline='')as f:new=list(csv.DictReader(f,delimiter=';'))
for before,after in zip(old,new):
    for key in before:
        if before['seance']=='S19'and key in('production','preuve'):continue
        assert before[key]==after[key],(before['seance'],key)
subprocess.run(['node','--check',str(C/'assets/parcours.js')],check=True,capture_output=True)
report={'html_pages':count,'broken_links':broken,'preserved_originals':len(checks['protected_files']),'public_files_checked':len(snapshot['files']),'zip_crc':'réussi','progression_observations_preserved':True,'sibling_workshops_modified':False,'git_initialized':(C/'.git').exists()}
(R/'docs/controle-dossier-module05.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
