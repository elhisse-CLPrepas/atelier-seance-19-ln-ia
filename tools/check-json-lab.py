"""Contrôle fichiers, HTTP local et ZIP du laboratoire corrigé, sans réseau externe."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from urllib.request import urlopen
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from functools import partial
import threading
import subprocess
import json
import re
import zipfile

root=Path(__file__).resolve().parents[1]
site=root/'05-EXEMPLES-CODE/mini-site-json-seance-19-v1-a-valider'
class Links(HTMLParser):
    def __init__(self): super().__init__();self.refs=[];self.ids=[];self.buttons=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        self.refs.extend(v for k,v in attrs if k in ('href','src') and v)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='button':self.buttons.append(a.get('id'))
js=(site/'js/app.js').read_text(encoding='utf-8')
pages=[]
for p in site.glob('*.html'):
    html=p.read_text(encoding='utf-8');parser=Links();parser.feed(html)
    assert len(parser.ids)==len(set(parser.ids)),f'ID dupliqué dans {p}'
    for ref in parser.refs:
        url=urlsplit(ref)
        if url.scheme or url.netloc:continue
        if url.path:assert (p.parent/unquote(url.path)).exists(),ref
        elif url.fragment:assert url.fragment in parser.ids,ref
    inline='\n'.join(re.findall(r'<script>(.*?)</script>',html,re.S))
    if inline:subprocess.run(['node','--check'],input=inline,text=True,check=True,capture_output=True)
    for button in parser.buttons:
        if button:assert '#'+button in js+inline,f'Bouton sans gestionnaire : {button}'
    pages.append({'page':p.name,'buttons_with_id':len([b for b in parser.buttons if b]),'local_links':'valides'})
for p in (site/'js').glob('*.js'):
    subprocess.run(['node','--check',str(p)],check=True,capture_output=True)
for p in (site/'data').glob('*.json'):json.loads(p.read_text(encoding='utf-8'))
demo=subprocess.run(['node','-e',"global.window={};require(process.argv[1]);console.log(JSON.stringify(window.S19_DEMO_DATA))",str(site/'js/demo-data.js')],check=True,capture_output=True,text=True,encoding='utf-8')
assert json.loads(demo.stdout)==json.loads((site/'data/projets.json').read_text(encoding='utf-8'))
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(site)))
thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
checks=[]
try:
    for rel in ['index.html','preparation-pwa.html','js/app.js','js/demo-data.js','css/styles.css','data/projets.json']:
        with urlopen(f'http://127.0.0.1:{server.server_port}/{rel}') as response:
            assert response.status==200 and response.read()==(site/rel).read_bytes()
            checks.append({'resource':rel,'http':200})
finally:server.shutdown();server.server_close();thread.join()
(site/'resultats-fichiers.json').write_text(json.dumps({'pages':pages,'http':checks,'demo_data_matches_json':True,'syntax':'réussie','browser_visual':'non exécuté'},ensure_ascii=False,indent=2),encoding='utf-8')
archive=root/'mini-site-json-S19-corrige-2026-11-25.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
    for p in site.rglob('*'):
        if p.is_file():z.write(p,p.relative_to(site.parent))
with zipfile.ZipFile(archive) as z:assert z.testzip() is None
print(json.dumps({'pages':len(pages),'http_checks':len(checks),'links':'valides','syntax':'valide','zip':str(archive)},ensure_ascii=False))
