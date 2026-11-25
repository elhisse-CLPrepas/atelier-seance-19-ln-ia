"""Reconstruit les supports locaux de l'atelier Vite depuis src/seance.json.
ReportLab : PDF ; OOXML : mise à jour du PowerPoint éditable de référence.
"""
from pathlib import Path
from xml.sax.saxutils import escape
import xml.etree.ElementTree as ET
import json, zipfile, io
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

R=Path(__file__).resolve().parents[1];OUT=R/'public/supports';D=json.loads((R/'src/seance.json').read_text(encoding='utf-8'))
for name,file in [('Body','arial.ttf'),('Bold','arialbd.ttf')]:pdfmetrics.registerFont(TTFont(name,str(Path('C:/Windows/Fonts')/file)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold',italic='Body',boldItalic='Bold')
NAVY='#071B33';GOLD='#D4AA57';MUTED='#52667A';LOGO=str(R/'public/assets/logo-LN-IA.png')
styles=getSampleStyleSheet()
for name,size,lead,font in [('Title',26,32,'Bold'),('Heading1',19,25,'Bold'),('Heading2',14,20,'Bold'),('BodyText',10.5,16,'Body')]:
    styles[name].fontName=font;styles[name].fontSize=size;styles[name].leading=lead;styles[name].textColor=colors.HexColor(NAVY);styles[name].spaceAfter=11
styles.add(ParagraphStyle('Small',fontName='Body',fontSize=9,leading=14,textColor=colors.HexColor(MUTED),spaceAfter=8))
styles.add(ParagraphStyle('Conducteur',fontName='Body',fontSize=10.5,leading=15.5,textColor=colors.HexColor(NAVY),spaceAfter=7))
def p(t,style='BodyText'):return Paragraph(escape(str(t)).replace('\n','<br/>'),styles[style])
def frame(c,doc):
    w,h=doc.pagesize;c.setFillColor(colors.HexColor(NAVY));c.rect(0,h-62,w,62,fill=1,stroke=0)
    c.drawImage(LOGO,40,h-51,76,38,mask='auto');c.setFillColor(colors.white);c.setFont('Bold',10);c.drawString(135,h-27,'LN-IA · S19 · JSON / HTTP / DOM')
    c.setFont('Body',9);c.drawString(135,h-44,'27 novembre 2026 · 110 minutes')
    c.setFillColor(colors.HexColor(MUTED));c.setFont('Body',8);c.drawString(40,25,'Prof. Abderrahman EL HISSE · Préparation PWA facultative');c.drawRightString(w-40,25,str(doc.page))
def pdf(name,story):
    SimpleDocTemplate(str(OUT/name),pagesize=(595.28,841.89),leftMargin=45,rightMargin=45,topMargin=88,bottomMargin=55,title='S19 · '+name,author=D['meta']['author']).build(story,onFirstPage=frame,onLaterPages=frame)

story=[p('Conducteur S19','Title'),p('Comprendre les mécanismes, observer et manipuler.'),p('Avant : V1 conservée ou laboratoire V2 ; serveur local déjà disponible ; console et onglet Réseau ; données fictives. Horaire Casablanca à communiquer.')]
for phase in D['phases']:
    group=[p(phase['time']+' minutes · '+phase['verb'],'Heading1'),p('Vues '+phase['slides'],'Small')]
    for label,key in [('Formateur','trainer'),('Candidat','candidate'),('À observer','observe'),('Relance','relance')]:group+=[p(label+' : '+phase[key],'Conducteur')]
    story.append(KeepTogether(group))
story+=[p('Adaptation','Heading1'),p('Les comparaisons et la passerelle PWA peuvent être reportées pour une variante de 90 minutes. Garder JSON, les quatre états, le diagnostic et la preuve. API, CORS avancé et exécution PHP restent des compléments guidés.')]
pdf('conducteur-S19.pdf',story)
story=[p('Fiche candidat S19','Title'),p('Prédire → tester → expliquer → corriger.'),p('Le laboratoire V2 utilise six ressources. Le contrat simple de l’éditeur attend trois champs ; le contrat enrichi ajoute les champs nécessaires aux activités et flashcards.')]
for label in ['Projet / binôme / date / navigateur','Fichier ou URL, version et mode HTTP ou exemple intégré','Scénario choisi et résultat attendu avant le test','Résultat réellement observé et message affiché','Étape concernée : requête, parsing, validation ou DOM','Cause expliquée et correction ou maintien motivé','Retour au succès et réouverture de la preuve']:
    story += [KeepTogether([p(label,'Heading2'),p('____________________________________________________________________'),Spacer(1,8)])]
story += [PageBreak(),p('Revue et relais','Title')]
for criterion in D['criteria']:story+=[p('À observer : '+criterion),p('Résultat : À COMPLÉTER','Small')]
story += [p('Pilote, date, observation et décision : À COMPLÉTER'),p('Limites / prochain essai S20 : À COMPLÉTER'),p('Fichiers : 04-WEB/mini-site-v2/ ; 06-PORTFOLIO/preuve-S19.md ; relais-S20.md. Aucun résultat de manipulation n’est prérempli.')]
pdf('fiche-candidat-S19.pdf',story)
story=[p('Révision active S19','Title'),p('Répondre avant de lire. Donner un exemple du laboratoire.')]
for q,a in D['cards']:story += [KeepTogether([p(q,'Heading2'),p(a),Spacer(1,6)])]
story += [PageBreak(),p('Quiz corrigé','Title')]
for i,(q,choices,correct,exps) in enumerate(D['quiz'],1):
    group=[p(str(i)+'. '+q,'Heading2')]
    for j,(choice,exp) in enumerate(zip(choices,exps)):group += [p(choice+(' — Choix attendu' if j==correct else ''),'BodyText'),p(exp,'Small')]
    story.append(KeepTogether(group))
pdf('revision-S19.pdf',story)

# Projection PDF 16:9 : chaque bloc est mesuré avant dessin.
W,H=960,540;c=canvas.Canvas(str(OUT/'presentation-S19.pdf'),pagesize=(W,H));c.setTitle(D['meta']['title']);c.setAuthor(D['meta']['author'])
def paragraph(text,x,top,width,size,color,font='Body',maxheight=None):
    st=ParagraphStyle('Slide',fontName=font,fontSize=size,leading=size*1.35,textColor=colors.HexColor(color))
    para=Paragraph(escape(text),st);_,height=para.wrap(width,1000)
    assert maxheight is None or height<=maxheight,(text,height,maxheight)
    para.drawOn(c,x,H-top-height);return height
for i,s in enumerate(D['slides'],1):
    dark=s['dark'];bg=NAVY if dark else '#F4F7FB';ink='#FFFFFF' if dark else NAVY;muted='#D4E0EA' if dark else MUTED
    c.setFillColor(colors.HexColor(bg));c.rect(0,0,W,H,fill=1,stroke=0)
    paragraph('SÉANCE 19 · JSON / HTTP / DOM',45,27,650,10,GOLD,'Bold');c.drawImage(LOGO,820,H-66,95,47.5,mask='auto')
    paragraph(s['title'],45,91,870,30,ink,'Bold',90);paragraph(s['lead'],45,180,860,16,muted,maxheight=48)
    for j,(label,text) in enumerate(s['points']):
        x=45+j*296;c.setStrokeColor(colors.HexColor(GOLD));c.line(x,H-260,x+270,H-260)
        paragraph(label,x,278,266,17,GOLD if dark else NAVY,'Bold',62);paragraph(text,x,347,266,15,ink,maxheight=100)
    paragraph(s['gesture'],45,475,820,12,muted,maxheight=36);paragraph(str(i)+' / 22',865,502,60,9,muted)
    c.showPage()
c.save()

# Réutiliser le paquet PowerPoint de référence, ses masters et son thème.
P='http://schemas.openxmlformats.org/presentationml/2006/main';A='http://schemas.openxmlformats.org/drawingml/2006/main';REL='http://schemas.openxmlformats.org/package/2006/relationships'
ET.register_namespace('p',P);ET.register_namespace('a',A)
original=OUT/'presentation-S19.pptx';blob=original.read_bytes()
def shape(sid,name,x,y,w,h,text,size,color,bold=False):
    paragraphs=''.join('<a:p><a:r><a:rPr lang="fr-FR" sz="'+str(size*100)+'"'+(' b="1"'if bold else '')+'><a:solidFill><a:srgbClr val="'+color+'"/></a:solidFill><a:latin typeface="Arial"/></a:rPr><a:t>'+escape(line)+'</a:t></a:r><a:endParaRPr lang="fr-FR"/></a:p>'for line in text.split('\n'))
    return f'<p:sp><p:nvSpPr><p:cNvPr id="{sid}" name="{name}"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr><p:spPr><a:xfrm><a:off x="{int(x*12700)}" y="{int(y*12700)}"/><a:ext cx="{int(w*12700)}" cy="{int(h*12700)}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/></p:spPr><p:txBody><a:bodyPr wrap="square" lIns="0" tIns="0" rIns="0" bIns="0"/><a:lstStyle/>{paragraphs}</p:txBody></p:sp>'
payload={}
with zipfile.ZipFile(io.BytesIO(blob)) as z:
    payload={name:z.read(name) for name in z.namelist()}
for i,s in enumerate(D['slides'],1):
    dark=s['dark'];ink='FFFFFF'if dark else '071B33';muted='D4E0EA'if dark else '52667A';bg='071B33'if dark else 'F4F7FB'
    shapes=shape(2,'Kicker',45,27,650,30,'SÉANCE 19 · JSON / HTTP / DOM',10,'D4AA57',True)+shape(3,'Titre',45,91,870,90,s['title'],30,ink,True)+shape(4,'Introduction',45,180,860,50,s['lead'],16,muted)
    sid=5
    for j,(label,text) in enumerate(s['points']):
        x=45+j*296;shapes+=shape(sid,'Notion '+str(j+1),x,278,266,62,label,17,'D4AA57'if dark else '071B33',True);sid+=1
        shapes+=shape(sid,'Explication '+str(j+1),x,347,266,100,text,15,ink);sid+=1
    shapes+=shape(15,'Geste',45,475,820,36,s['gesture'],12,muted)+shape(16,'Numéro',865,502,60,20,str(i)+' / 22',9,muted)
    shapes+='<p:pic><p:nvPicPr><p:cNvPr id="17" name="Logo LN-IA"/><p:cNvPicPr/><p:nvPr/></p:nvPicPr><p:blipFill><a:blip r:embed="rIdLogo"/><a:stretch><a:fillRect/></a:stretch></p:blipFill><p:spPr><a:xfrm><a:off x="10477500" y="190500"/><a:ext cx="1143000" cy="571500"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr></p:pic>'
    payload[f'ppt/slides/slide{i}.xml']=(f'<?xml version="1.0" encoding="UTF-8"?><p:sld xmlns:p="{P}" xmlns:a="{A}" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><p:cSld><p:bg><p:bgPr><a:solidFill><a:srgbClr val="{bg}"/></a:solidFill><a:effectLst/></p:bgPr></p:bg><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr/>{shapes}</p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sld>').encode()
    relname=f'ppt/slides/_rels/slide{i}.xml.rels';rels=ET.fromstring(payload[relname])
    for rel in list(rels):
        if rel.get('Id')=='rIdLogo':rels.remove(rel)
    ET.SubElement(rels,'{'+REL+'}Relationship',Id='rIdLogo',Type='http://schemas.openxmlformats.org/officeDocument/2006/relationships/image',Target='../media/s19-logo.png');payload[relname]=ET.tostring(rels,encoding='utf-8',xml_declaration=True)
    notename=f'ppt/notesSlides/notesSlide{i}.xml';notes=ET.fromstring(payload[notename]);bodies=notes.findall('.//{'+P+'}txBody')
    if bodies:
        body=bodies[0]
        for par in list(body.findall('{'+A+'}p')):body.remove(par)
        for line in [s['title'],s['note'],'Geste : '+s['gesture']]:
            para=ET.SubElement(body,'{'+A+'}p');run=ET.SubElement(para,'{'+A+'}r');ET.SubElement(run,'{'+A+'}t').text=line
    payload[notename]=ET.tostring(notes,encoding='utf-8',xml_declaration=True)
payload['ppt/media/s19-logo.png']=(R/'public/assets/logo-LN-IA.png').read_bytes()
with zipfile.ZipFile(original,'w',zipfile.ZIP_DEFLATED)as z:
    for name,content in payload.items():z.writestr(name,content)
with zipfile.ZipFile(original)as z:
    assert z.testzip()is None
    for name in z.namelist():
        if name.endswith('.xml'):ET.fromstring(z.read(name))
print('Supports JSON S19 reconstruits : conducteur, fiche, révision, PDF 16:9 et PPTX éditable.')
