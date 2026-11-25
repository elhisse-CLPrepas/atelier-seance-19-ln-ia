from pathlib import Path
import re,zipfile,io,json,hashlib
from html.parser import HTMLParser
from urllib.parse import unquote,urlsplit
import fitz
from PIL import Image,ImageOps,ImageDraw
R=Path(__file__).resolve().parents[1]
bad=re.compile(r'roue|pneu|frein|cyclist',re.I)
issues=[];counts={'files':0,'archives':0,'pdf':0,'links':0}
def inspect(name,b):
    counts['files']+=1
    if bad.search(name):issues.append('Nom : '+name)
    suffix=Path(name).suffix.lower()
    if suffix in ['.zip','.pptx']:
        counts['archives']+=1
        with zipfile.ZipFile(io.BytesIO(b)) as z:
            for n in z.namelist():
                if not n.endswith('/'):inspect(name+'!'+n,z.read(n))
    elif suffix=='.pdf':
        counts['pdf']+=1
        with fitz.open(stream=b,filetype='pdf') as doc:
            text='\n'.join(p.get_text() for p in doc)
        if bad.search(text):issues.append('Texte PDF : '+name)
    elif suffix in ['.html','.md','.txt','.json','.js','.xml','.svg','.mjs','.css']:
        text=b.decode('utf-8',errors='replace')
        if bad.search(text):issues.append('Texte : '+name)
for base in ['src','public','dist','docs','mon-dossier-challenge-Module05']:
    for p in (R/base).rglob('*'):
        if p.is_file() and p.name!='SHA256SUMS.txt':inspect(p.relative_to(R).as_posix(),p.read_bytes())
for name in ['OUVRIR-SEANCE-19.html','PROJECTION-SEANCE-19.html']:inspect(name,(R/name).read_bytes())

class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[]
    def handle_starttag(self,tag,attrs):
        for k,v in attrs:
            if k in ['href','src'] and v:self.links.append(v)
for base in ['public/dossier-challenge','dist/dossier-challenge','mon-dossier-challenge-Module05']:
    for p in (R/base).rglob('*.html'):
        h=Links();h.feed(p.read_text(encoding='utf-8'))
        for href in h.links:
            u=urlsplit(href)
            if u.scheme or u.netloc or not u.path or u.path.startswith('/'):continue
            counts['links']+=1
            if not (p.parent/unquote(u.path)).exists():issues.append('Lien absent : '+str(p.relative_to(R))+' -> '+href)

# Planche de contrôle : toutes les pages des six PDF.
thumbs=[]
for p in sorted((R/'public/supports').glob('*.pdf')):
    with fitz.open(p) as doc:
        for i,page in enumerate(doc):
            pix=page.get_pixmap(matrix=fitz.Matrix(.38,.38))
            tile=Image.new('RGB',(250,350),'#e4e9ef')
            img=Image.open(io.BytesIO(pix.tobytes('png'))).convert('RGB');img.thumbnail((240,320))
            tile.paste(img,((250-img.width)//2,20))
            ImageDraw.Draw(tile).text((5,3),p.stem+' '+str(i+1),fill='black')
            thumbs.append(tile)
out=R/'tmp/pdfs';out.mkdir(parents=True,exist_ok=True)
for batch in range(0,len(thumbs),20):
    items=thumbs[batch:batch+20];sheet=Image.new('RGB',(1250,350*((len(items)+4)//5)),'white')
    for j,tile in enumerate(items):sheet.paste(tile,((j%5)*250,(j//5)*350))
    sheet.save(out/f'controle-{batch//20+1}.png')
report={'counts':counts,'issues':issues,'status':'OK' if not issues else 'À CORRIGER'}
(R/'docs/audit-S19.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
if issues:raise SystemExit(1)
