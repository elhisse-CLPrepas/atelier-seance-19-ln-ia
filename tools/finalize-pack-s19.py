"""Contrôles finaux reproductibles et archive du pack V3, sans accès externe."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit, quote
from urllib.request import urlopen
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import threading
import hashlib
import json
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / 'pack-documentaire-seance-19-v3-valide'
IMPORT = ROOT / '05-EXEMPLES-CODE'
manifest = json.loads((PACK / 'MANIFEST-IMPORT-S19.json').read_text(encoding='utf-8'))
for item in manifest['files']:
    assert hashlib.sha256((IMPORT / item['path']).read_bytes()).hexdigest() == item['sha256']
    assert hashlib.sha256((Path(manifest['source']) / item['path']).read_bytes()).hexdigest() == item['sha256']

# Conserver l'outil de génération et son rapport dans leur état de livraison.
report = '''# Contrôle d’alignement — V3 du 25 novembre 2026

## Résultat

Pack aligné sur S19 du 27 novembre 2026 : JSON local, quatre états et préparation PWA. Durée de référence : 110 minutes, variante 90 minutes. Trois mini-sites importés et embarqués. La demande du pilote de générer une version validée est consignée dans VALIDATION-V3.md ; elle ne prévalide pas les travaux candidats.

## Corrections et distinction des ressources

- Minimal : trois objets fictifs Déclic Web, mêmes champs title/category/description que la fiche 06 ; contrôle des chaînes non vides ajouté avant affichage.
- Laboratoire enrichi : schéma à six ressources conservé, identifié comme complément formateur ; les données minimales ne sont pas interchangeables avec ce schéma.
- Deux inventaires PWA limités aux fichiers réellement présents et aux composants à préparer en S20.
- Preuves d’été remplacées dans les copies S19 par des modèles vierges. Aucun résultat historique présenté comme essai de novembre.
- Démonstration S17 conservée comme référence historique de prérequis.
- Fiche 08, READMEs, dates, noms V3 et liens alignés ; entrée HTML autonome ajoutée.

## Contrôles exécutés

- 24 fichiers importés : empreintes identiques aux sources externes et copies de référence locales.
- JavaScript : contrôles de syntaxe de chaque fichier externe et script intégré aux pages HTML.
- JSON : parsing de chaque fichier livré.
- Liens Markdown et ressources HTML : présence des cibles locales contrôlée.
- 28 tests de comportement réussis sur les copies S19 : chargement, succès, vide, HTTP, réseau, syntaxe JSON, structure, champs, restauration ; sept scénarios du laboratoire et ouverture/fermeture d’une flashcard.
- Service HTTP local : requêtes sur les ressources des trois mini-sites, puis arrêt du serveur temporaire.
- ZIP : contrôle CRC, noms et contenus identiques au dossier livré ; manifeste SHA-256 de livraison.

Les détails mesurés sont dans resultats-controles.json et resultats-tests-comportement.json.

## Limites et essais restant à faire

Les tests de comportement utilisent Node et un DOM simulé : ils ne prouvent pas le rendu visuel, le focus réel ou l’accessibilité complète. Le contrôle dans un navigateur n’a pas été possible avec les outils disponibles de cette session. Revoir visuellement mobile, clavier, zoom et projection sur le poste du formateur.

Aucun essai d’exécution PHP, de service worker, d’installation ou de fonctionnement hors connexion n’est attesté. Les liens distants ne sont pas vérifiés ; le socle ne doit pas en dépendre. Aucune publication effectuée. Le mini-site général, la présentation et les PDF extérieurs à ce pack restent ceux de la production antérieure.

## Conservation et reprise

Sources C: et pack V2 inchangés. Les imports de référence sont dans 05-EXEMPLES-CODE à la racine du projet ; leurs copies adaptées sont dans mini-sites dans ce pack. Les noms des dossiers importés sont historiques, distincts du statut V3 du pack.

Pour rejouer les contrôles : node tools/test-imported-s19.cjs puis python tools/finalize-pack-s19.py depuis la racine du projet. Le script d’import tools/validate-pack-s19.py refuse d’écraser une livraison V3 déjà présente.
'''
(PACK / 'CONTROLE-ALIGNEMENT.md').write_text(report, encoding='utf-8')

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.refs=[]
    def handle_starttag(self, tag, attrs):
        self.refs.extend(v for k,v in attrs if k in ('src','href') and v)

broken=[]; js_count=0; json_count=0; html_count=0; md_count=0
for p in PACK.rglob('*'):
    if not p.is_file(): continue
    if p.suffix=='.json':
        json.loads(p.read_text(encoding='utf-8-sig')); json_count+=1
    if p.suffix=='.js':
        subprocess.run(['node','--check',str(p)],check=True,capture_output=True); js_count+=1
        assert not re.search(r'navigator\.serviceWorker\.register\s*\(',p.read_text(encoding='utf-8'))
    if p.suffix in ('.html','.md'):
        text=p.read_text(encoding='utf-8')
        if p.suffix=='.html':
            html_count+=1; parser=Links(); parser.feed(text); refs=parser.refs
            for code in re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>',text,re.S):
                check=subprocess.run(['node','--check'],input=code,text=True,capture_output=True)
                assert check.returncode==0,check.stderr
                js_count+=1
        else:
            md_count+=1; refs=re.findall(r'\]\(([^)]+)\)',text)
        for ref in refs:
            url=urlsplit(ref)
            if url.scheme or url.netloc or not url.path:continue
            if not (p.parent/unquote(url.path)).exists():broken.append(f'{p.relative_to(PACK)} → {ref}')
assert not broken,broken

class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(PACK)))
thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
http_results=[]
try:
    for p in sorted((PACK/'mini-sites').rglob('*')):
        if p.suffix not in ('.html','.json','.js','.css','.png'):continue
        rel=p.relative_to(PACK).as_posix()
        with urlopen(f'http://127.0.0.1:{server.server_port}/{quote(rel)}') as response:
            assert response.status==200
            assert response.read()==p.read_bytes()
            http_results.append({'path':rel,'status':200})
finally:
    server.shutdown();server.server_close();thread.join()

behaviors=json.loads((PACK/'resultats-tests-comportement.json').read_text(encoding='utf-8'))
assert len(behaviors['results'])==28 and all(r['status']=='réussi' for r in behaviors['results'])
checks={'import_files':len(manifest['files']),'json_files_parsed':json_count,'javascript_syntax_checks':js_count,'html_pages_checked':html_count,'markdown_files_checked':md_count,'broken_local_targets':broken,'http_checks':http_results,'behavior_tests':len(behaviors['results']),'browser_visual_test':'non exécuté','php_execution':'non exécutée','archive_crc':'réussi, contrôlé après génération','archive_contents':'identiques au dossier, contrôlé après génération'}
(PACK/'resultats-controles.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
delivery=[]
for p in sorted(PACK.rglob('*')):
    if p.is_file() and p.name!='MANIFEST-LIVRAISON.json':
        delivery.append({'path':p.relative_to(PACK).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(PACK/'MANIFEST-LIVRAISON.json').write_text(json.dumps(delivery,ensure_ascii=False,indent=2),encoding='utf-8')
archive=ROOT/(PACK.name+'.zip')
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(PACK.rglob('*')):
        if p.is_file():z.write(p,p.relative_to(ROOT))
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    expected={p.relative_to(ROOT).as_posix():p.read_bytes() for p in PACK.rglob('*') if p.is_file()}
    assert set(z.namelist())==set(expected)
    assert all(z.read(name)==data for name,data in expected.items())
print(json.dumps({'import':len(manifest['files']),'javascript_checks':js_count,'html_pages':html_count,'http_checks':len(http_results),'behavior_tests':28,'zip':str(archive),'zip_bytes':archive.stat().st_size},ensure_ascii=False))
