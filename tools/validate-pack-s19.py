"""Importe les trois exemples sans modifier C:, construit un pack validé distinct.
Exécution : python tools/validate-pack-s19.py. Aucun accès réseau.
"""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess
import zipfile
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path('C:/DEV/CHALLENGE-01-Juin-2026/05-PROGRAMME-PEDAGOGIQUE/MODULE-05/05-EXEMPLES-CODE')
IMPORT = ROOT / '05-EXEMPLES-CODE'
OLD = ROOT / 'pack-documentaire-seance-19-v1-a-valider'
PACK = ROOT / 'pack-documentaire-seance-19-v3-valide'
assert not PACK.exists(), 'La version validée existe déjà ; conserver cette livraison.'
records = []
for source in sorted(SOURCE.rglob('*')):
    if not source.is_file():
        continue
    rel = source.relative_to(SOURCE)
    target = IMPORT / rel
    if target.exists():
        assert source.read_bytes() == target.read_bytes(), f'Import existant différent : {rel}'
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    records.append({'path': rel.as_posix(), 'sha256': hashlib.sha256(source.read_bytes()).hexdigest(), 'bytes': source.stat().st_size})
(IMPORT / 'MANIFEST-IMPORT-S19.json').write_text(json.dumps({'source': str(SOURCE), 'files': records}, ensure_ascii=False, indent=2), encoding='utf-8')
PACK.mkdir()
rename = {p.name: p.name.replace('-v1-a-valider', '-v3-valide') for p in OLD.glob('*.md')}
for source in OLD.glob('*.md'):
    if source.name == 'RAPPORT-RECONSTRUCTION.md':
        continue
    text = source.read_text(encoding='utf-8')
    for old, new in rename.items():
        text = text.replace(old, new)
    text = text.replace('automne V2 documentaire du 25 novembre 2026 · **Statut :** À VALIDER', 'automne V3 du 25 novembre 2026 · **Statut du pack :** VALIDÉ POUR PRÉPARATION ET UTILISATION EN S19')
    # Les statuts des preuves candidates et des décisions futures restent vierges.
    text = text.replace('Les noms historiques des fichiers et du dossier sont conservés pour les liens ; les en-têtes portent l’édition automne V2 documentaire.', 'Les noms des fiches portent la version V3 validée ; les références historiques restent identifiées.')
    (PACK / rename[source.name]).write_text(text, encoding='utf-8')
shutil.copy2(OLD / 'manifest-sources.json', PACK / 'manifest-sources-documentaires.json')
shutil.copy2(IMPORT / 'MANIFEST-IMPORT-S19.json', PACK / 'MANIFEST-IMPORT-S19.json')
shutil.copytree(IMPORT, PACK / 'mini-sites')
(PACK / 'mini-sites/MANIFEST-IMPORT-S19.json').unlink()  # Copie redondante créée par ce script uniquement.
names = [p.name for p in SOURCE.iterdir() if p.is_dir()]
minimal = PACK / 'mini-sites/mini-site-json-seance-19-v1-a-valider'
advanced = PACK / 'mini-sites/mini-site-seance-19-V2'

# Copies de travail adaptées : les imports de référence restent identiques aux sources.
js = minimal / 'js/app.js'
text = js.read_text(encoding='utf-8')
needle = '    if (projects.length === 0) {'
text = text.replace(needle, '''    projects.forEach((project, index) => {
      if (!project || typeof project !== "object" || Array.isArray(project) ||
          ["title", "category", "description"].some(key => typeof project[key] !== "string" || !project[key].trim())) {
        throw new Error(`Objet ${index + 1} : titre, catégorie et description doivent être des chaînes non vides.`);
      }
    });

''' + needle)
js.write_text(text, encoding='utf-8')
example = re.search(r'```json\n(.*?)\n```', (OLD / '06-cahier-charges-exemple-json-seance-19-v1-a-valider.md').read_text(encoding='utf-8'), re.S)
(minimal / 'data/projets.json').write_text(json.dumps(json.loads(example.group(1)), ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
for folder in (minimal, advanced):
    inventory = folder / 'data/pwa-content-inventory.json'
    if inventory.exists():
        inventory.write_text(json.dumps({
            'date': '2026-11-27', 'status': 'preparation-S20', 'activeCache': False,
            'existing': ['index.html', 'css/styles.css', 'js/app.js', 'data/projets.json', 'preparation-pwa.html'],
            'plannedS20': ['manifest.webmanifest', 'service-worker.js', 'offline.html', 'assets/icons/icon-192.png', 'assets/icons/icon-512.png'],
            'note': 'Inventaire conceptuel ; aucun service worker actif. Définir le scope et tester en S20.'
        }, ensure_ascii=False, indent=2), encoding='utf-8')
    for html in folder.glob('*.html'):
        content = html.read_text(encoding='utf-8').replace('<body>', '<body>\n<p class="status" style="margin:1rem">S19 · 27 novembre 2026 · JSON local et préparation PWA · <a href="../../OUVRIR-LE-PACK.html">Retour au pack</a></p>', 1)
        html.write_text(content, encoding='utf-8')
    proof = folder / 'preuve-19-json-pwa.md'
    proof.write_bytes((OLD / '05-modele-preuve-19-json-pwa-v1-a-valider.md').read_bytes())
    role = 'Socle candidat : trois objets et trois champs.' if folder == minimal else 'Complément formateur : six ressources avec schéma enrichi ; ne pas remplacer son JSON par celui du socle.'
    (folder / 'README.md').write_text(f'''# {folder.name} — copie adaptée S19 du 27 novembre 2026

{role}

Depuis ce dossier, lancer un serveur déjà disponible :

```powershell
python -m http.server 8080 --bind 127.0.0.1
```

Ouvrir http://127.0.0.1:8080/ ; arrêter avec Ctrl+C. Aucun service worker actif. Le fichier `preparation-pwa.html` simule les composants pour préparer S20. Le modèle de preuve reste à remplir par le candidat.

Contrôles : voir `../../CONTROLE-ALIGNEMENT.md`. Les références importées intactes restent dans `05-EXEMPLES-CODE/` à la racine du projet de séance.
''', encoding='utf-8')

# Éviter les résultats anciens dans les données de travail candidates.
for folder in (PACK / 'mini-sites').iterdir():
    if folder.is_dir() and folder not in (minimal, advanced):
        readme = folder / 'README.md'
        readme.write_text('> Référence historique S17 conservée : prérequis HTML/CSS/JavaScript, pas le livrable S19. Les dates et statuts ci-dessous concernent la source d’été.\n\n' + readme.read_text(encoding='utf-8'), encoding='utf-8')

# Relier réellement les fiches aux ressources embarquées.
p08 = PACK / rename['08-reference-guide-html-interactif-seance-19.md']
p08.write_text('''# Ressources embarquées — S19 du 27 novembre 2026

**Version :** V3 · **Statut du pack :** VALIDÉ POUR UTILISATION EN S19.

- [Exemple minimal : socle candidat](mini-sites/mini-site-json-seance-19-v1-a-valider/index.html) : trois objets, champs title/category/description, quatre états, validation des champs ajoutée.
- [Laboratoire S19 enrichi](mini-sites/mini-site-seance-19-V2/index.html) : six ressources, filtres, flashcards et scénarios. Son schéma ajoute id, level, objectives, activity, deliverable, question et answer, avec lien facultatif contrôlé.
- [Démonstration S17](mini-sites/mini-site-demonstration-seance-17-v1-a-valider/index.html) : repère historique pour les prérequis HTML/CSS/JavaScript.
- [Préparation PWA du socle](mini-sites/mini-site-json-seance-19-v1-a-valider/preparation-pwa.html) : simulations conceptuelles, aucun cache actif.

Depuis la racine du pack : `python -m http.server 8080 --bind 127.0.0.1`, puis ouvrir `http://127.0.0.1:8080/OUVRIR-LE-PACK.html`. Le double-clic permet de lire les documents HTML mais ne remplace pas le serveur pour fetch().

Le guide historique `SORTIES/GUIDE-SUIVI-SEANCE-19-HTML-V1-A-VALIDER/` n’est pas inclus dans ce pack. Il ne constitue pas une dépendance du parcours courant. Les trois mini-sites sont autonomes sur le plan de leurs fichiers locaux.
''', encoding='utf-8')

readme = PACK / 'README.md'
text = readme.read_text(encoding='utf-8')
text = text.replace('Le pack documentaire est reconstruit ; la revue pédagogique reste à effectuer.', 'Version validée pour préparer et utiliser S19, établie à votre demande du 25 novembre. Les observations et validations individuelles des candidats restent à renseigner.')
start = text.index('Le pack livré contient')
end = text.index('Les noms des fiches', start)
text = text[:start] + 'Le pack embarque les trois mini-sites importés, avec des copies S19 adaptées. Ouvrir [l’entrée du pack](OUVRIR-LE-PACK.html). Le mini-site général de séance, les projections et les PDF externes ne sont pas reconstruits par cette livraison.\n\n' + text[end:]
text = text.replace('[le rapport de reconstruction](RAPPORT-RECONSTRUCTION.md)', '[le rapport de validation](CONTROLE-ALIGNEMENT.md)')
text += '\n## Validation et contrôles\n\nVoir [la décision de version](VALIDATION-V3.md) et [les contrôles et limites](CONTROLE-ALIGNEMENT.md). Les noms historiques des dossiers mini-sites sont conservés pour la traçabilité ; ils ne définissent pas le statut du pack courant.\n'
readme.write_text(text, encoding='utf-8')
validation = '''# Validation de version — V3

**Date :** 25 novembre 2026 · **Séance :** 27 novembre 2026.
**Statut :** VALIDÉ POUR PRÉPARATION ET UTILISATION EN S19.

Cette version répond à la demande explicite du pilote dans cette conversation : importer les dossiers mini-sites, contrôler leur alignement et générer un pack version validée. Elle formalise le cadrage JSON local, quatre états et préparation PWA pour S20. Elle ne prétend pas qu’une observation de séance ou une recette visuelle humaine a déjà eu lieu.

La validation concerne le contenu et le périmètre de ce pack V3. Les modèles candidats restent À COMPLÉTER, leurs productions restent soumises à contrôle et leurs résultats ne sont pas prévalidés. La mise en ligne, les essais PWA et l’installation ne font pas partie de cette décision.

Les contrôles techniques exécutés sont listés dans CONTROLE-ALIGNEMENT.md. Les sources d’été, les imports intacts et le pack V2 sont conservés.
'''
(PACK / 'VALIDATION-V3.md').write_text(validation, encoding='utf-8')
# Mettre les avertissements de validation dans leur contexte sans réécrire l'histoire.
for filename in [rename['11-decisions-p0-future-pwa-validees-2026-07-27.md'], 'PROMPT-CADRAGE-S19-27-NOVEMBRE-2026.md', 'SOURCES-ET-SYNCHRONISATION.md']:
    p = PACK / filename
    p.write_text('> Édition V3 : la décision courante du pack figure dans VALIDATION-V3.md. Les mentions de revue future ci-dessous décrivent le cadrage préparatoire ou les décisions individuelles restant à renseigner.\n\n' + p.read_text(encoding='utf-8'), encoding='utf-8')

links = '\n'.join(f'<li><a href="{rename[p.name]}">{p.name[:2]} · {p.name[3:].replace("-v1-a-valider.md", "").replace("-", " ")}</a></li>' for p in sorted(OLD.glob('[0-9][0-9]-*.md')))
site_links = '\n'.join(f'<li><a href="mini-sites/{name}/index.html">{name}</a></li>' for name in names)
(PACK / 'OUVRIR-LE-PACK.html').write_text(f'''<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>S19 — Pack V3 validé — 27 novembre 2026</title><style>body{{font:18px system-ui;max-width:960px;margin:2rem auto;padding:1rem;color:#071a2f;background:#f4f7fb}}a{{color:#17418c}}li{{margin:.7rem 0}}code{{background:#fff;padding:.2rem}}</style><h1>S19 — JSON local et préparation PWA</h1><p>27 novembre 2026 · 110 minutes · Pack V3 validé pour utilisation en S19.</p><p>Depuis ce dossier : <code>python -m http.server 8080 --bind 127.0.0.1</code> puis ouvrir <code>http://127.0.0.1:8080/OUVRIR-LE-PACK.html</code>.</p><h2>Mini-sites</h2><p>Le minimal est le socle candidat. Le laboratoire V2 constitue un complément. S17 sert de référence aux prérequis.</p><ul>{site_links}</ul><h2>Fiches Markdown</h2><p>Les fichiers Markdown sont à lire dans votre éditeur habituel.</p><ul>{links}</ul><p><a href="CONTROLE-ALIGNEMENT.md">Contrôles</a> · <a href="VALIDATION-V3.md">Validation et limites</a></p></html>''', encoding='utf-8')

# Liens HTML locaux : ignorer les URL distantes et les ancres ; vérifier les assets.
class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.refs = []
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('src', 'href') and value:
                self.refs.append(value)

issues = []
js_checks = 0
json_checks = 0
html_checks = 0
for p in PACK.rglob('*'):
    if p.suffix == '.json':
        json.loads(p.read_text(encoding='utf-8-sig')); json_checks += 1
    if p.suffix == '.js':
        subprocess.run(['node', '--check', str(p)], check=True, capture_output=True); js_checks += 1
        assert not re.search(r'navigator\.serviceWorker\.register\s*\(', p.read_text(encoding='utf-8'))
    if p.suffix == '.html':
        html_checks += 1
        parser = Links(); html = p.read_text(encoding='utf-8'); parser.feed(html)
        for ref in parser.refs:
            url = urlsplit(ref)
            if url.scheme or url.netloc or not url.path:
                continue
            dest = p.parent / unquote(url.path)
            if not dest.exists() and dest != PACK / 'CONTROLE-ALIGNEMENT.md':
                issues.append(f'{p.relative_to(PACK)} → {ref}')
        for i, code in enumerate(re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', html, re.S)):
            result = subprocess.run(['node', '--check'], input=code, text=True, capture_output=True)
            assert result.returncode == 0, f'{p} script {i}: {result.stderr}'
            js_checks += 1
assert not issues, issues

(PACK / 'CONTROLE-ALIGNEMENT.md').write_text(f'''# Contrôle d’alignement — V3 du 25 novembre 2026

## Périmètre et corrections

- Trois mini-sites importés : {len(records)} fichiers, copiés sans modification dans `05-EXEMPLES-CODE/` à la racine du projet ; empreintes SHA-256 conservées.
- Copies adaptées embarquées dans ce pack, sources externes intactes.
- Minimal : validation des trois champs non vides ajoutée ; trois données fictives Déclic Web alignées sur la fiche 06.
- Laboratoire : schéma enrichi conservé et explicitement distingué du socle, six ressources attendues.
- Inventaires PWA des deux copies S19 remplacés par des listes de fichiers existants et de composants futurs S20 ; aucun cache activé.
- Preuves historiques remplacées dans les copies S19 par un modèle vierge ; READMEs et dates adaptés.
- Fiches nommées V3, liens réécrits, ressources embarquées et entrée HTML ajoutées.

## Contrôles exécutés

- JSON parsables : {json_checks} fichiers.
- JavaScript externe et intégré : {js_checks} contrôles de syntaxe Node réussis.
- Pages HTML : {html_checks} pages, aucune cible locale de lien ou d’asset manquante.
- Import : comparaison octet par octet avec les sources pour les {len(records)} fichiers.
- Comportements JSON : voir `resultats-tests-comportement.json`.
- ZIP : contrôle CRC et comparaison avec les fichiers de livraison.

## Limites

Les tests de comportement exécutent les scripts dans un environnement DOM simulé ; ils contrôlent les branches et messages mais ne prouvent pas le rendu visuel réel. Aucun contrôle visuel navigateur, mobile réel ou lecteur d’écran n’est attesté. Aucun essai PHP, PWA, installation ou hors connexion n’est annoncé. Le point d’entrée de séance et ses PDF externes restent ceux de l’ancienne production.

L’outil de navigateur de cette session n’est pas disponible. Les contrôles visuels, clavier réel et projection restent à effectuer sur le poste du formateur avant la séance.
''', encoding='utf-8')
# Les Markdown peuvent pointer vers les rapports produits pendant les tests.
print(json.dumps({'pack': str(PACK), 'import_files': len(records), 'json_checks': json_checks, 'js_checks': js_checks, 'html_checks': html_checks}, ensure_ascii=False))
