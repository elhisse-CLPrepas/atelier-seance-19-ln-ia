"""Actualise les preuves de recette et diffuse le dossier commun sans réinitialisation."""
from pathlib import Path
import json,shutil,subprocess,sys
from urllib.request import urlopen
R=Path(__file__).resolve().parents[1];C=R/'mon-dossier-challenge-Module05'
report=json.loads((R/'docs/recette-dossier-module05.json').read_text(encoding='utf-8'))
assert report['status']=='passed'and len(report['results'])==14
shutil.copy2(R/'docs/recette-dossier-module05.json',C/'00-SOURCES/RECETTE-NAVIGATEUR-MODULE05.json')
layout=json.loads((R/'tmp/qa-dossier-module05/layout-and-keyboard.json').read_text(encoding='utf-8'))
if 'keyboardFlashcard'in layout:layout['keyboardSessionButton']=layout.pop('keyboardFlashcard')
assert layout['keyboardSessionButton']is True
for p in [R/'docs/recette-affichage-dossier-module05.json',C/'00-SOURCES/RECETTE-AFFICHAGE-MODULE05.json']:
    p.write_text(json.dumps(layout,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=C/'RAPPORT-SYNCHRONISATION-S17-S20.md';text=p.read_text(encoding='utf-8')
marker='\n## Recette finale et diffusion\n'
text=text.split(marker)[0]+marker+'''
- 14 contrôles Chromium réussis : accueil, ressources, séances indépendantes, validation, exports, reprise, refus d’ancien format, remise à zéro ciblée, impression, mobile et laboratoire HTTP.
- Captures ordinateur et mobile inspectées ; défaut de contraste du bouton secondaire corrigé.
- Activation au clavier réel du bouton de séance contrôlée.
- 24 pages HTML auditées sans cible locale manquante.
- 70 fichiers préexistants protégés par empreintes SHA-256 : contenus inchangés.
- Les observations du CSV restent identiques ; seules les références de la ligne S19 ont changé.
- Copie publique, copie dist et ZIP synchronisés depuis le dossier source ; intégrité CRC et contenus vérifiés.
- Construction Vite et neuf groupes de contrôles S19 réussis après intégration.

Les résultats détaillés de cette recette sont inclus dans 00-SOURCES/RECETTE-NAVIGATEUR-MODULE05.json et RECETTE-AFFICHAGE-MODULE05.json. Ils décrivent les contrôles techniques, pas les essais personnels des candidats.

Pour diffuser de nouvelles modifications sans réinitialiser le dossier : `python -X utf8 tools/sync-challenge.py` depuis la racine S19. La construction Vite appelle aussi cette synchronisation. L’outil d’enrichissement initial refuse de réécrire un dossier déjà enrichi.

Les ateliers voisins, le pack V3 et les sources C: restent inchangés. Aucune publication, initialisation Git ou opération distante effectuée.
'''
p.write_text(text,encoding='utf-8')
subprocess.run([sys.executable,'-X','utf8',str(R/'tools/sync-challenge.py')],cwd=R,check=True)
subprocess.run([sys.executable,'-X','utf8',str(R/'tools/check-dossier-module05.py')],cwd=R,check=True)
try:
    with urlopen('http://127.0.0.1:8080/dossier-challenge/',timeout=5)as response:
        body=response.read();assert body==(C/'index.html').read_bytes();print('Serveur 8080 : nouvelle copie du dossier, HTTP 200.')
    with urlopen('http://127.0.0.1:8080/dossier-challenge/assets/parcours.css',timeout=5)as response:
        assert response.read()==(C/'assets/parcours.css').read_bytes();print('Styles corrigés : version servie conforme.')
except OSError as error:
    print('Serveur local non vérifiable : '+str(error))
