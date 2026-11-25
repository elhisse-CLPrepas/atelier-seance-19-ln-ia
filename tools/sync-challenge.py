"""Copie de diffusion du dossier commun ; aucune réinitialisation des sources.
Exécution : python -X utf8 tools/sync-challenge.py. Pas de Git ni publication.
"""
from pathlib import Path
import json,hashlib,shutil,zipfile
R=Path(__file__).resolve().parents[1]
C=R/'mon-dossier-challenge-Module05'
assert C.is_dir() and C.resolve().parent==R.resolve()
ignore=lambda p: '.git' in p.relative_to(C).parts or '__pycache__' in p.relative_to(C).parts
manifest=C/'00-SOURCES/MANIFEST-LIVRAISON.json'
entries=[]
for p in sorted(C.rglob('*')):
    if p.is_file() and not ignore(p) and p!=manifest:
        entries.append({'path':p.relative_to(C).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
manifest.parent.mkdir(exist_ok=True,parents=True)
manifest.write_text(json.dumps({'scope':'instantané du dossier commun','files':entries},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
target=R/'public/dossier-challenge'
targets=[target]
if (R/'dist/index.html').exists():targets.append(R/'dist/dossier-challenge')
for p in C.rglob('*'):
    if p.is_file() and not ignore(p):
        for destination in targets:
            dest=destination/p.relative_to(C)
            dest.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(p,dest)
            assert dest.read_bytes()==p.read_bytes()
support=R/'public/supports/mon-dossier-challenge-Module05-S17-S20.zip'
support.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(support,'w',zipfile.ZIP_DEFLATED)as z:
    for p in sorted(C.rglob('*')):
        if p.is_file() and not ignore(p):z.write(p,'mon-dossier-challenge-Module05/'+p.relative_to(C).as_posix())
with zipfile.ZipFile(support)as z:
    assert z.testzip() is None
    for p in C.rglob('*'):
        if p.is_file() and not ignore(p):assert z.read('mon-dossier-challenge-Module05/'+p.relative_to(C).as_posix())==p.read_bytes()
shutil.copy2(support,R/'mon-dossier-challenge-Module05-S17-S20.zip')
# Alias conservé pour les anciens liens du site.
shutil.copy2(support,R/'public/supports/mon-dossier-challenge-Module05-S19.zip')
if (R/'dist/index.html').exists():
    for name in ['mon-dossier-challenge-Module05-S17-S20.zip','mon-dossier-challenge-Module05-S19.zip']:
        (R/'dist/supports').mkdir(parents=True,exist_ok=True)
        shutil.copy2(support,R/'dist/supports'/name)
print(json.dumps({'files':len(entries)+1,'copy':str(target),'zip':str(support),'sources_reinitialized':False},ensure_ascii=False))
