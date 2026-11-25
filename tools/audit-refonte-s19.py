"""Audit des liens locaux, supports et archives du parcours actuel ; rendu PDF QA."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,re,zipfile,hashlib
import fitz
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[1];OUT=R/'tmp/qa-refonte-S19/pdf';OUT.mkdir(parents=True,exist_ok=True)
class Links(HTMLParser):
    def __init__(self):super().__init__();self.refs=[];self.ids=[]
    def handle_starttag(self,tag,attrs):
        for k,v in attrs:
            if k in ('src','href')and v:self.refs.append(v)
            if k=='id':self.ids.append(v)
pages=[R/'OUVRIR-SEANCE-19.html',R/'PROJECTION-SEANCE-19.html',R/'dist/index.html',R/'dist/projection-S19.html',*list((R/'dist/laboratoire-json').glob('*.html')),*list((R/'dist/mini-sites/json-minimal').glob('*.html'))]
broken=[]
for p in pages:
    parser=Links();parser.feed(p.read_text(encoding='utf-8'))
    assert len(parser.ids)==len(set(parser.ids)),p.name
    for ref in parser.refs:
        url=urlsplit(ref)
        if url.scheme or url.netloc:continue
        if url.path:
            dest=(R/unquote(url.path).lstrip('/'))if url.path.startswith('/')else p.parent/unquote(url.path)
            if not dest.exists():broken.append({'page':str(p.relative_to(R)),'target':ref})
        elif url.fragment and unquote(url.fragment)not in parser.ids:broken.append({'page':str(p.relative_to(R)),'anchor':ref})
assert not broken,broken
pdfs={};thumbs=[];bounds=[]
for name in ['presentation-S19.pdf','conducteur-S19.pdf','fiche-candidat-S19.pdf','revision-S19.pdf']:
    doc=fitz.open(R/'public/supports'/name);pdfs[name]=len(doc)
    for i,p in enumerate(doc):
        for word in p.get_text('words'):
            if word[0]<0 or word[1]<0 or word[2]>p.rect.width+1 or word[3]>p.rect.height+1:bounds.append((name,i+1,word[4]))
        dest=OUT/(name[:-4]+'-'+str(i+1)+'.png');p.get_pixmap(matrix=fitz.Matrix(.7,.7)).save(dest)
        im=Image.open(dest).convert('RGB');im.thumbnail((384,250));tile=Image.new('RGB',(400,280),'#dce3ea');tile.paste(im,((400-im.width)//2,24));ImageDraw.Draw(tile).text((10,5),name+' '+str(i+1),fill='black');thumbs.append(tile)
assert not bounds,bounds
assert pdfs['presentation-S19.pdf']==22
for start in range(0,len(thumbs),12):
    group=thumbs[start:start+12];sheet=Image.new('RGB',(1600,280*((len(group)+3)//4)),'white')
    for j,im in enumerate(group):sheet.paste(im,((j%4)*400,(j//4)*280))
    sheet.save(OUT/('contact-'+str(start//12+1)+'.png'))
archives={}
for name in ['kit-candidat-S19.zip','laboratoire-json-S19.zip']:
    with zipfile.ZipFile(R/'public/supports'/name)as z:
        assert z.testzip()is None
        assert all(not n.startswith('/')and'..'not in Path(n).parts for n in z.namelist())
        archives[name]=len(z.namelist())
        assert any(n.endswith('data/projets.json')for n in z.namelist())
with zipfile.ZipFile(R/'public/supports/presentation-S19.pptx')as z:
    slide_names=[n for n in z.namelist()if re.fullmatch(r'ppt/slides/slide\d+\.xml',n)]
    assert len(slide_names)==22
    for i,s in enumerate(json.loads((R/'src/seance.json').read_text(encoding='utf-8'))['slides'],1):
        assert s['title'].replace('&','&amp;')in z.read(f'ppt/slides/slide{i}.xml').decode()
report={'html_pages_checked':len(pages),'broken_local_links':broken,'pdf_pages':pdfs,'pdf_out_of_bounds':bounds,'pptx_slides':22,'zip_entries':archives,'browser_report':'recette-navigateur-S19.json','visual_previews':'tmp/qa-refonte-S19/'}
(R/'docs/audit-refonte-S19.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
